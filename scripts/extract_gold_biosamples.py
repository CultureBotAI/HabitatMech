#!/usr/bin/env python3
"""Derive a reviewable biosample inventory from GOLD's bulk export.

`data/raw/gold_ecosystem_paths.tsv` carries `biosample_count` and it is 0 on all
2,562 rows — kg-microbe's KGX dump does not expose biosamples, so the column was
emitted empty and nothing noticed. That matters more than a missing statistic:
without it there is no way to know which GOLD paths have samples behind them,
and therefore which could ever carry an ENVO triad (#126).

GOLD's bulk export has the answer. It is 223 MB, regenerated daily, and stays
UNTRACKED for the same reason a kg-microbe checkout does — `data/raw/` is small
inventories that `verify-corpus` reproduces byte-for-byte, not vendored dumps.
This script is the boundary between the two.

What the export does NOT have is the ENVO triad. Its Biosample sheet is fifteen
columns and none of them is ENVO; its own Readme says it "is not meant to
replicate the exact user experience". The triad is API-only. What the export
gives instead is the thing that made the API usable at all: a list of study ids,
so `gold_api.py` can query studies that exist rather than walking an id space
that is 0.8% dense and rate-limited (#126).

The sheet is 236 MB of XML with inline strings, so it is streamed rather than
loaded. Reading it into memory needs several GB and gains nothing.

Usage:
    python3 scripts/extract_gold_biosamples.py
    python3 scripts/extract_gold_biosamples.py --check
"""

from __future__ import annotations

import argparse
import collections
import csv
import sys
import zipfile
from pathlib import Path
from xml.etree.ElementTree import iterparse

REPO_ROOT = Path(__file__).resolve().parent.parent
EXPORT = REPO_ROOT / "data" / "raw" / "goldData.xlsx"
OUT = REPO_ROOT / "data" / "raw" / "gold_path_biosamples.tsv"
STUDIES_OUT = REPO_ROOT / "data" / "raw" / "gold_studies.tsv"

NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
# Sheet order in the export: Readme, Study, Biosample, Organism, SP, AP.
SHEET_BIOSAMPLE = "xl/worksheets/sheet3.xml"
# The Sequencing Project sheet is the only one carrying STUDY GOLD ID and
# BIOSAMPLE GOLD ID on the same row. Without it there is no way to know which
# studies to ask the API about, and the alternative is sweeping all 61,365 —
# of which only 4,634 have any biosample at all.
SHEET_SEQPROJECT = "xl/worksheets/sheet5.xml"

# GOLD writes this where a level is absent. Treating it as a real level would
# produce paths like "Soil > Unclassified" that match nothing in the corpus.
UNSET = "Unclassified"


def rows(archive: zipfile.ZipFile, sheet: str):
    """Stream a worksheet as lists of cell strings.

    Inline strings only — this export has no sharedStrings table, which is
    unusual and worth stating, because the shared-string path is what most
    xlsx readers assume and it would silently yield empty cells here.
    """
    with archive.open(sheet) as handle:
        row: list[str] = []
        for _event, element in iterparse(handle, events=("end",)):
            if element.tag == f"{NS}c":
                inline = element.find(f"{NS}is/{NS}t")
                value = element.find(f"{NS}v")
                text = inline.text if inline is not None else (
                    value.text if value is not None else "")
                row.append(text or "")
                element.clear()
            elif element.tag == f"{NS}row":
                yield row
                row = []
                element.clear()


def canonical_path(cells: list[str]) -> str:
    """The five ecosystem levels joined the way data/raw/ writes them."""
    return " > ".join(c for c in cells[10:15] if c and c != UNSET)


def extract() -> tuple[list[dict], list[dict]]:
    if not EXPORT.exists():
        raise SystemExit(
            f"{EXPORT.relative_to(REPO_ROOT)} not found. It is untracked by design — "
            "download it from https://gold.jgi.doe.gov/download?mode=site_excel\n"
            "Note that download has failed mid-transfer when fetched anonymously; a "
            "logged-in browser session is what produced the copy this was written against."
        )
    archive = zipfile.ZipFile(EXPORT)

    counts: collections.Counter[str] = collections.Counter()
    path_ids: dict[str, str] = {}
    biosample_paths: dict[str, str] = {}
    for n, cells in enumerate(rows(archive, SHEET_BIOSAMPLE)):
        if n == 0 or len(cells) < 15:
            continue
        path = canonical_path(cells)
        if not path:
            continue
        counts[path] += 1
        if cells[0]:
            biosample_paths[cells[0]] = path
        # The numeric id GOLD uses for the path, which our gold_node_ids
        # reference as `gold.ecosystem:NNNN`.
        path_ids.setdefault(path, cells[9])

    # Which studies to ask the API for a triad about. Only studies with a
    # biosample on a path this corpus holds — 4,587 of 61,365, which is the
    # difference between a feasible sweep and an inconsiderate one.
    with (REPO_ROOT / "data" / "raw" / "gold_ecosystem_paths.tsv").open(
        newline="", encoding="utf-8") as fh:
        corpus_paths = {r["canonical_path"] for r in csv.DictReader(fh, delimiter="\t")}

    header: dict[str, int] = {}
    study_paths: collections.defaultdict[str, set[str]] = collections.defaultdict(set)
    for n, cells in enumerate(rows(archive, SHEET_SEQPROJECT)):
        if n == 0:
            header = {v: i for i, v in enumerate(cells)}
            continue
        s_i, b_i = header.get("STUDY GOLD ID"), header.get("BIOSAMPLE GOLD ID")
        if s_i is None or b_i is None or len(cells) <= max(s_i, b_i):
            continue
        study, biosample = cells[s_i], cells[b_i]
        if study and biosample in biosample_paths:
            study_paths[study].add(biosample_paths[biosample])

    studies = [
        {"study_gold_id": study,
         "path_count": str(len(paths)),
         "paths": "|".join(sorted(paths))}
        for study, paths in sorted(study_paths.items())
        if paths & corpus_paths
    ]

    inventory = [
        {"canonical_path": path, "ecosystem_path_id": path_ids.get(path, ""),
         "biosample_count": str(count)}
        for path, count in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    ]
    return inventory, studies


def write(path: Path, rows_out: list[dict], columns: list[str]) -> str:
    body = ["\t".join(columns)]
    body += ["\t".join(r.get(c, "") for c in columns) for r in rows_out]
    text = "\n".join(body) + "\n"
    path.write_text(text, encoding="utf-8")
    return text


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="fail if the committed inventories differ from the export")
    args = parser.parse_args(argv or sys.argv[1:])

    inventory, studies = extract()
    inv_cols = ["canonical_path", "ecosystem_path_id", "biosample_count"]
    std_cols = ["study_gold_id", "path_count", "paths"]

    if args.check:
        for target, data, cols in ((OUT, inventory, inv_cols), (STUDIES_OUT, studies, std_cols)):
            want = "\n".join(["\t".join(cols)] +
                             ["\t".join(r.get(c, "") for c in cols) for r in data]) + "\n"
            if not target.exists() or target.read_text(encoding="utf-8") != want:
                print(f"{target.relative_to(REPO_ROOT)} is stale; regenerate with "
                      "`python3 scripts/extract_gold_biosamples.py`")
                return 1
        print(f"inventories current ({len(inventory)} paths, {len(studies)} studies)")
        return 0

    write(OUT, inventory, inv_cols)
    write(STUDIES_OUT, studies, std_cols)
    total = sum(int(r["biosample_count"]) for r in inventory)
    print(f"wrote {OUT.relative_to(REPO_ROOT)}: {len(inventory)} paths, {total:,} biosamples")
    print(f"wrote {STUDIES_OUT.relative_to(REPO_ROOT)}: {len(studies)} studies worth querying")

    with (REPO_ROOT / "data" / "raw" / "gold_ecosystem_paths.tsv").open(
        newline="", encoding="utf-8") as fh:
        ours = {r["canonical_path"] for r in csv.DictReader(fh, delimiter="\t")}
    known = [r for r in inventory if r["canonical_path"] in ours]
    print(f"\n  of those paths, {len(known)} are in the corpus and "
          f"{len(inventory) - len(known)} are not")
    print("  the missing ones are GOLD classifications kg-microbe's snapshot predates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
