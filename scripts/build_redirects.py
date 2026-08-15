#!/usr/bin/env python3
"""Rebuild data/habitats/RETIRED.tsv — the map from dead record URLs to live ones.

A record page is named ``slugify(f"{label}-{identifier}")``, so the URL moves
whenever a curator improves either. That is most of what curation *does*:
re-grounding a concept changes its identifier, and adopting the ontology's own
label changes its label. 43 published URLs had already 404'd across five merges
before this existed, and the rate rises with the curation backlog (#54).

That undercuts the point of a content-hashed identifier. A record advertised as
stable and citable, whose URL dies the first time someone improves its
grounding, is not citable.

This walks git history to recover them:

* every ``pages/habitats/*.html`` that has ever existed on the branch and does
  not exist now is a dead URL;
* its identifier comes from the page's own meta description;
* the target is that identifier's current record if it still has one — the
  common case, a pure label change — and otherwise the record that inherited
  its *source concepts*, which is what a merge actually does. Source ids
  (``gold.ecosystem:5826``, ``bacdive.isolation_source:nectar``) are stable
  upstream keys, so they survive the merge that the identifier did not.

Re-run after a merge that retires records. `just redirects`.

Usage:
    python3 scripts/build_redirects.py            # rewrite RETIRED.tsv
    python3 scripts/build_redirects.py --check    # fail if it is out of date
"""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from render_pages import slugify  # noqa: E402

HABITATS_DIR = REPO_ROOT / "data" / "habitats"
RETIRED_PATH = HABITATS_DIR / "RETIRED.tsv"
COLUMNS = ["retired_slug", "retired_identifier", "current_identifiers", "resolved_by"]

# The identifier as the page's own meta description states it: "label (ID): ...".
_META_ID = re.compile(r'<meta name="description" content="[^"(]*\(([^)]+)\)')


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(REPO_ROOT), *args],
        capture_output=True, text=True, check=False,
    )
    return result.stdout if result.returncode == 0 else ""


def dead_page_slugs(live: set[str]) -> dict[str, str]:
    """Retired page slug -> the commit whose parent still had the file.

    `live` is derived from the corpus rather than from what is on disk under
    pages/: once the stubs are written they occupy those very filenames, so
    reading the directory would make every retired slug look alive again and
    the map would empty itself on the second run.
    """
    out: dict[str, str] = {}
    commit = ""
    for line in git("log", "--diff-filter=DR", "--name-status", "--format=%H",
                    "--", "pages/habitats").splitlines():
        if line and "\t" not in line:
            commit = line.strip()
            continue
        parts = line.split("\t")
        if len(parts) < 2 or not commit:
            continue
        # A rename retires the old path just as a delete does.
        slug = Path(parts[1]).stem
        if slug not in live:
            out.setdefault(slug, commit)
    return out


def identifier_of_dead_page(slug: str, commit: str) -> str:
    html = git("show", f"{commit}^:pages/habitats/{slug}.html")
    match = _META_ID.search(html)
    return match.group(1).strip() if match else ""


def retired_record_source_ids() -> dict[str, set[str]]:
    """Every retired record's identifier -> the source ids it carried.

    Source ids are upstream keys (``gold.ecosystem:5826``), so they survive the
    merge that the record identifier did not — they are what links a dead record
    to the live one that absorbed it.

    Built in a single pass over the deletions rather than by searching history
    per identifier: the corpus is 3200 records over dozens of commits, and the
    naive form is thousands of `git show` calls.
    """
    found: dict[str, set[str]] = {}
    commit = ""
    for line in git("log", "--diff-filter=DR", "--name-status", "--format=%H",
                    "--", "data/habitats").splitlines():
        if line and "\t" not in line:
            commit = line.strip()
            continue
        parts = line.split("\t")
        if len(parts) < 2 or not commit or not parts[1].endswith(".yaml"):
            continue
        blob = git("show", f"{commit}^:{parts[1]}")
        if not blob:
            continue
        try:
            doc = yaml.safe_load(blob)
        except yaml.YAMLError:
            continue
        if not isinstance(doc, dict) or "identifier" not in doc:
            continue
        source_ids = {
            a.get("source_id") for a in (doc.get("source_attestations") or [])
            if a.get("source_id")
        }
        # Latest wins: `git log` is newest-first, so the first sighting of an
        # identifier is the state it was in when it was retired.
        found.setdefault(doc["identifier"], source_ids)
    return found


def slug_for(doc: dict) -> str:
    """The page name the renderer gives this record. Must stay in step with
    render_pages, which is why it imports that module's slugify rather than
    reimplementing it."""
    return slugify(f"{doc['label']}-{doc['identifier']}")


def load_corpus() -> tuple[dict[str, dict], dict[str, str]]:
    """(identifier -> doc, source_id -> identifier) over the live corpus."""
    by_id: dict[str, dict] = {}
    by_source: dict[str, str] = {}
    for path in sorted(HABITATS_DIR.rglob("*.yaml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(doc, dict) or "identifier" not in doc:
            continue
        by_id[doc["identifier"]] = doc
        for attestation in doc.get("source_attestations") or []:
            source_id = attestation.get("source_id")
            if source_id:
                by_source.setdefault(source_id, doc["identifier"])
    return by_id, by_source


def build() -> list[dict[str, str]]:
    by_id, by_source = load_corpus()
    retired_sources = retired_record_source_ids()
    live_slugs = {slug_for(doc) for doc in by_id.values()}
    rows: list[dict[str, str]] = []
    for slug, commit in sorted(dead_page_slugs(live_slugs).items()):
        identifier = identifier_of_dead_page(slug, commit)
        if not identifier:
            continue
        if identifier in by_id:
            # The record is alive; only its label moved. Nothing to look up.
            rows.append({
                "retired_slug": slug, "retired_identifier": identifier,
                "current_identifiers": identifier, "resolved_by": "label_changed",
            })
            continue
        # The identifier is gone, so the concept merged or was re-grounded.
        # Follow its source concepts to whatever absorbed them.
        landed = sorted({
            by_source[s] for s in retired_sources.get(identifier, ()) if s in by_source
        })
        if not landed:
            continue
        # A retired record can have SPLIT rather than merged: NCIT:C17649 "Other"
        # held both Invertebrates-Other and Rodentia-Other, and curating it sent
        # them to different records. There is no single right target then, and
        # picking the most common one silently sends half the readers to the
        # wrong habitat — so all of them are kept and the stub offers a choice.
        rows.append({
            "retired_slug": slug, "retired_identifier": identifier,
            "current_identifiers": "|".join(landed),
            "resolved_by": "source_concepts_split" if len(landed) > 1 else "source_concepts_merged",
        })
    return rows


def write(rows: list[dict[str, str]], path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda r: r["retired_slug"]))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="Fail if RETIRED.tsv is not what this would write.")
    args = parser.parse_args(argv)

    # A shallow clone has no history to reconstruct from, and would silently
    # produce an empty map that --check then reports as "out of date" for the
    # wrong reason. Fail with the actual cause instead (#45's lesson).
    if git("rev-parse", "--is-shallow-repository").strip() == "true":
        print("this is a shallow clone; build_redirects needs full history "
              "(actions/checkout with fetch-depth: 0)", file=sys.stderr)
        return 2

    rows = build()
    if args.check:
        existing = RETIRED_PATH.read_text(encoding="utf-8") if RETIRED_PATH.exists() else ""
        import io
        buffer = io.StringIO()
        writer = csv.DictWriter(buffer, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda r: r["retired_slug"]))
        if buffer.getvalue() != existing:
            print("RETIRED.tsv is out of date; run `just redirects`", file=sys.stderr)
            return 1
        print(f"RETIRED.tsv is current ({len(rows)} redirects)")
        return 0

    write(rows, RETIRED_PATH)
    by_reason = Counter(r["resolved_by"] for r in rows)
    print(f"wrote {RETIRED_PATH.relative_to(REPO_ROOT)}: {len(rows)} redirect(s)")
    for reason, count in sorted(by_reason.items()):
        print(f"  {reason:26s} {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
