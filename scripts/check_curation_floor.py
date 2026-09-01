"""Refuse a curation input that has lost rows relative to a base revision.

Every other gate in this repository compares generated output against the
curation inputs. None of them asserts anything about what those inputs should
contain, so an input that loses rows reproduces a corpus that is internally
consistent and simply missing decisions -- `just qc` passes on it (#219).

That happened in a merge: two hand-resolved curation files were overwritten by
a blanket `git checkout --theirs` before they were staged, and the loss was
visible only as a smaller count in passing output.

Curation inputs are append-mostly. A row leaves one when a curator deliberately
removes it, which is rare and deliberate; rows leaving silently is the failure
this catches. Comparison is by identifier, not by line, so reordering, an edited
note or a reworded decision are all invisible here -- only a disappearance is
reported.

The base to compare against is every revision that is supposed to be contained
in the result, not just the trunk. The loss in #219 was of rows that existed on
the BRANCH and never on `main`, so comparing against `origin/main` alone reports
a clean tree -- checked, and it does. `HEAD` and, mid-merge, `MERGE_HEAD` are
the bases that actually see it: a merge must not drop what either parent had.
"""

from __future__ import annotations

import argparse
import csv
import io
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

# Each input, and the column holding the identity of a row.
INPUTS = {
    "curation/decisions.tsv": "identifier",
    "curation/term_requests.tsv": "identifier",
    "curation/term_requests_excluded.tsv": "identifier",
    "curation/redirects_retracted.tsv": "retired_slug",
}


def _identifiers(text: str, column: str) -> set[str]:
    reader = csv.DictReader(io.StringIO(text), delimiter="\t")
    return {
        value.strip()
        for row in reader
        if (value := (row.get(column) or ""))
        if value.strip()
    }


def _at_revision(revision: str, path: str) -> str | None:
    """The file's content at a revision, or None if it is not there.

    A missing file and a failed git call must not look the same: returning ""
    for both is how a broken invocation becomes a silent pass (#219 again, and
    the redirect-count failure before it). A non-zero exit that is not a
    "path does not exist" is re-raised.
    """
    done = subprocess.run(
        ["git", "show", f"{revision}:{path}"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    if done.returncode == 0:
        return done.stdout
    stderr = done.stderr.lower()
    if "does not exist" in stderr or "exists on disk, but not in" in stderr:
        return None
    raise SystemExit(f"git show {revision}:{path} failed: {done.stderr.strip()}")


def _resolves(revision: str) -> bool:
    return subprocess.run(
        ["git", "rev-parse", "--verify", "--quiet", f"{revision}^{{commit}}"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    ).returncode == 0


def check(bases: list[str]) -> int:
    live = [b for b in bases if _resolves(b)]
    if not live:
        # Deliberately not a failure, and deliberately not silence: absent
        # evidence is unknown, not clean. Same stance as the non-habitat screen.
        print(f"curation floor: none of {bases} resolves here — not checked")
        return 0

    problems = []
    for path, column in INPUTS.items():
        current = REPO_ROOT / path
        # Every base is supposed to be contained in the result, so the floor is
        # the union of what they all had -- not any single one of them.
        required: set[str] = set()
        seen_at = []
        for base in live:
            before = _at_revision(base, path)
            if before is None:
                continue
            seen_at.append(base)
            required |= _identifiers(before, column)
        if not seen_at:
            continue
        if not current.exists():
            problems.append(
                f"{path}: present at {', '.join(seen_at)} and missing from the working tree"
            )
            continue
        lost = required - _identifiers(current.read_text(encoding="utf-8"), column)
        if lost:
            shown = ", ".join(sorted(lost)[:8])
            more = f" (and {len(lost) - 8} more)" if len(lost) > 8 else ""
            problems.append(
                f"{path}: {len(lost)} identifier(s) present at "
                f"{', '.join(seen_at)} and gone now: {shown}{more}"
            )

    if problems:
        print("curation inputs have lost rows:", file=sys.stderr)
        for problem in problems:
            print(f"  {problem}", file=sys.stderr)
        print(
            "\nIf a row was removed deliberately, say so in the commit message and "
            "re-run with --allow-loss. If not, it was probably dropped by a merge, "
            "a rebase or a truncation — recover it before regenerating anything, "
            "because every generated artifact will reproduce faithfully without it.",
            file=sys.stderr,
        )
        return 1

    print(f"curation floor: no identifier lost since {', '.join(live)}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", action="append", dest="bases", metavar="REV",
                        help="revision to compare against; repeatable. "
                             "Default: origin/main, HEAD and MERGE_HEAD.")
    parser.add_argument("--allow-loss", action="store_true",
                        help="report losses but do not fail; for a deliberate removal")
    args = parser.parse_args(argv)
    status = check(args.bases or ["origin/main", "HEAD", "MERGE_HEAD"])
    return 0 if args.allow_loss else status


if __name__ == "__main__":
    raise SystemExit(main())
