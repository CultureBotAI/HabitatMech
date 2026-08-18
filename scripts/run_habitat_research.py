#!/usr/bin/env python3
"""Batch deep research over the novel terms that still need a definition.

118 records name a concept no vendored ontology has a term for and have no
definition (#110). Each call takes about ten minutes and costs money, so this is
built to be interrupted and resumed rather than run once perfectly:

* **Resume keys on the output file existing**, which is the same check
  `research_habitat.py` makes. Killing this runner and restarting it re-queues
  only what has no report.
* **A failure does not stop the batch.** One record's provider error is recorded
  and the rest continue — the alternative is that hour 4 of a 5-hour run throws
  away hours 1 through 3.
* **The manifest is appended as work completes**, not written at the end, so a
  killed run still says what it did.

Verification is of the artifact, not the exit code. A provider can return
success, cost real money, and write nothing; `research_habitat.py` already
raises on that, and this records it as a failure rather than a silent skip.

Usage:
    python3 scripts/run_habitat_research.py --dry-run     # free: what would run
    python3 scripts/run_habitat_research.py --workers 4
    python3 scripts/run_habitat_research.py --limit 5     # a smaller fan-out first
"""

from __future__ import annotations

import argparse
import csv
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST = REPO_ROOT / "reports" / "habitat_research_manifest.tsv"
MANIFEST_COLUMNS = ["identifier", "label", "assertions", "status", "seconds", "bytes", "detail"]

sys.path.insert(0, str(Path(__file__).resolve().parent))
from research_habitat import (  # noqa: E402
    DEFAULT_PROVIDER,
    load_record,
    output_path,
    resolve_provider,
    undefined_novel_terms,
)


def already_done(identifier: str, provider: str) -> Path | None:
    """The report this record would resume from, if it exists and is non-empty.

    Zero-length counts as not done: a truncated file is worse than a missing
    one, because resume would skip it forever.
    """
    try:
        _path, doc = load_record(identifier)
    except SystemExit:
        return None
    out = output_path(doc, provider)
    return out if out.exists() and out.stat().st_size else None


# Lines that are the wrapper failing, not the provider explaining why. Taking
# the last line of stderr looked right and captured exactly these: a
# CalledProcessError repr that re-prints the whole command and says nothing.
_WRAPPER_NOISE = ("Traceback (most recent", "  File \"", "    ", "subprocess.CalledProcessError",
                  "raise SystemExit", "During handling of")


def provider_error(stderr: str | None) -> str:
    """The most informative line of stderr, for a one-column manifest field."""
    lines = [ln.rstrip() for ln in (stderr or "").splitlines() if ln.strip()]
    if not lines:
        return "no stderr"
    # An explicit error class from the provider beats anything else.
    for line in reversed(lines):
        if any(k in line for k in ("Error:", "error:", "Exception", "refused", "timeout")) \
                and not line.startswith(_WRAPPER_NOISE):
            return line[:300]
    for line in reversed(lines):
        if not line.startswith(_WRAPPER_NOISE):
            return line[:300]
    return lines[-1][:300]


# The claude_code provider fails opaquely under load — "Claude Code exited with
# code 1: <no stderr>", sometimes in 4 seconds and sometimes 240 seconds in. The
# same records succeed when retried later, so it is rate limiting rather than
# anything about the record. Retrying in-process is much cheaper than a rerun:
# resume only skips COMPLETED work, so without this a failed record waits for a
# whole new pass.
RETRY_ATTEMPTS = 3
RETRY_BACKOFF_SECONDS = 90


def run_one(identifier: str, label: str, assertions: int, provider: str) -> dict:
    for attempt in range(1, RETRY_ATTEMPTS + 1):
        row = _attempt_one(identifier, label, assertions, provider)
        if row["status"] == "ok" or attempt == RETRY_ATTEMPTS:
            if attempt > 1:
                row["detail"] = f"[attempt {attempt}] {row['detail']}"
            return row
        # Linear, not exponential: the limit is a rolling window, so waiting
        # longer each time mostly wastes the window rather than clearing it.
        time.sleep(RETRY_BACKOFF_SECONDS * attempt)
    raise AssertionError("unreachable")


def _attempt_one(identifier: str, label: str, assertions: int, provider: str) -> dict:
    started = time.monotonic()
    command = [
        sys.executable, str(REPO_ROOT / "scripts" / "research_habitat.py"),
        "--identifier", identifier, "--provider", provider,
    ]
    try:
        completed = subprocess.run(
            command, cwd=REPO_ROOT, capture_output=True, text=True, timeout=3600
        )
    except subprocess.TimeoutExpired:
        return {"identifier": identifier, "label": label, "assertions": assertions,
                "status": "timeout", "seconds": f"{time.monotonic() - started:.0f}",
                "bytes": "0", "detail": "exceeded 3600s"}

    elapsed = f"{time.monotonic() - started:.0f}"
    out = already_done(identifier, provider)
    if completed.returncode != 0:
        return {"identifier": identifier, "label": label, "assertions": assertions,
                "status": "failed", "seconds": elapsed, "bytes": "0",
                "detail": provider_error(completed.stderr)}
    if out is None:
        return {"identifier": identifier, "label": label, "assertions": assertions,
                "status": "empty", "seconds": elapsed, "bytes": "0",
                "detail": "provider reported success but wrote nothing"}
    return {"identifier": identifier, "label": label, "assertions": assertions,
            "status": "ok", "seconds": elapsed, "bytes": str(out.stat().st_size),
            "detail": str(out.relative_to(REPO_ROOT))}


def append_manifest(row: dict) -> None:
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    new = not MANIFEST.exists()
    with MANIFEST.open("a", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=MANIFEST_COLUMNS, delimiter="\t",
                                lineterminator="\n")
        if new:
            writer.writeheader()
        writer.writerow({c: row.get(c, "") for c in MANIFEST_COLUMNS})


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provider", default=DEFAULT_PROVIDER)
    parser.add_argument("--workers", type=int, default=2,
                        help="concurrent provider calls. 2 is measured, not guessed: at 4, "
                             "13 of 16 calls failed in under 10 seconds with 'Claude Code "
                             "exited with code 1: <no stderr>', while the same records "
                             "succeeded one at a time. At 2, 10 of 10 succeeded.")
    parser.add_argument("--limit", type=int, help="research only the top N by volume")
    parser.add_argument("--dry-run", action="store_true",
                        help="list what would run, and what resume already covers. Free.")
    args = parser.parse_args(argv or sys.argv[1:])

    provider = resolve_provider(args.provider)
    worklist = undefined_novel_terms()
    pending, done = [], []
    for assertions, label, identifier in worklist:
        (done if already_done(identifier, provider) else pending).append(
            (assertions, label, identifier)
        )
    if args.limit:
        pending = pending[: args.limit]

    print(f"{len(worklist)} novel terms need a definition")
    print(f"  {len(done)} already researched with {provider} (resume skips these)")
    print(f"  {len(pending)} to run, {args.workers} at a time")
    if pending:
        estimate = len(pending) * 10 / max(args.workers, 1)
        print(f"  rough estimate: {estimate / 60:.1f} hours at ~10 min per call")
    if args.dry_run:
        for assertions, label, identifier in pending[:20]:
            print(f"    {assertions:7d}  {label[:34]:34s} {identifier}")
        if len(pending) > 20:
            print(f"    ... and {len(pending) - 20} more")
        return 0
    if not pending:
        return 0

    counts: dict[str, int] = {}
    completed_n = 0
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(run_one, identifier, label, assertions, provider): identifier
            for assertions, label, identifier in pending
        }
        for future in as_completed(futures):
            row = future.result()
            append_manifest(row)
            counts[row["status"]] = counts.get(row["status"], 0) + 1
            completed_n += 1
            print(f"  [{completed_n}/{len(pending)}] {row['status']:8s} "
                  f"{row['label'][:30]:30s} {row['seconds']}s {row['bytes']}B",
                  flush=True)

    print(f"\ndone: {counts}")
    print(f"manifest: {MANIFEST.relative_to(REPO_ROOT)}")
    # A non-zero exit on any failure, so a wrapper cannot mistake a half-finished
    # batch for a complete one.
    return 0 if set(counts) <= {"ok"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
