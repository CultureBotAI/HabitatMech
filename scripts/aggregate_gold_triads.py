#!/usr/bin/env python3
"""Aggregate per-biosample GOLD ENVO triads into a reviewable path inventory."""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SOURCE = REPO_ROOT / "data" / "raw" / "gold_biosample_triads.tsv"
DEFAULT_OUTPUT = REPO_ROOT / "data" / "raw" / "gold_path_triads.tsv"
SLOTS = ("broad", "local", "medium")
SLOT_FIELDS = {
    "broad": ("envo_broad_scale", "envo_broad_label"),
    "local": ("envo_local_scale", "envo_local_label"),
    "medium": ("envo_medium", "envo_medium_label"),
}
OUTPUT_COLUMNS = [
    "canonical_path",
    "slot",
    "samples",
    "studies",
    "distinct_terms",
    "top_term",
    "top_label",
    "top_share",
    "studies_agreeing",
]


def aggregate(source: Path) -> list[dict[str, str]]:
    groups: dict[tuple[str, str], list[tuple[str, str, str]]] = defaultdict(list)
    with source.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            path = row["canonical_path"]
            study = row["study_gold_id"]
            # Aggregate complete triads only. Mixing samples that carry just
            # one or two slots gives each slot a different denominator and can
            # make a stray partial annotation outrank the coherent triads.
            if not path or not all(row[field] for field, _label in SLOT_FIELDS.values()):
                continue
            for slot in SLOTS:
                term_field, label_field = SLOT_FIELDS[slot]
                term = row[term_field]
                if term:
                    groups[(path, slot)].append((term, row[label_field], study))

    rows = []
    slot_order = {slot: n for n, slot in enumerate(SLOTS)}
    for (path, slot), values in sorted(groups.items(), key=lambda item: (item[0][0], slot_order[item[0][1]])):
        terms = Counter(term for term, _label, _study in values)
        # Counter preserves first-seen order for ties. The input is sorted by
        # biosample id, so this is deterministic and reproduces the original
        # aggregation contract.
        top_term, top_count = terms.most_common(1)[0]
        labels = Counter(label for term, label, _study in values if term == top_term)
        top_label = labels.most_common(1)[0][0]
        studies = {study for _term, _label, study in values if study}
        agreeing = {study for term, _label, study in values if term == top_term and study}
        rows.append(
            {
                "canonical_path": path,
                "slot": slot,
                "samples": str(len(values)),
                "studies": str(len(studies)),
                "distinct_terms": str(len(terms)),
                "top_term": top_term,
                "top_label": top_label,
                "top_share": f"{top_count / len(values):.2f}",
                "studies_agreeing": str(len(agreeing)),
            }
        )
    return rows


def render(rows: list[dict[str, str]]) -> str:
    lines = ["\t".join(OUTPUT_COLUMNS)]
    lines.extend("\t".join(row[column] for column in OUTPUT_COLUMNS) for row in rows)
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv or sys.argv[1:])

    if not args.source.exists():
        raise SystemExit(
            f"{args.source} not found; it is an untracked API-sweep intermediate. "
            "Run `python scripts/gold_enumerate.py --studies` first or pass --source."
        )
    text = render(aggregate(args.source))
    if args.check:
        if not args.output.exists() or args.output.read_text(encoding="utf-8") != text:
            print(f"{args.output} does not reproduce from {args.source}", file=sys.stderr)
            return 1
        print(f"{args.output} reproduces from {args.source}")
        return 0
    args.output.write_text(text, encoding="utf-8")
    print(f"wrote {args.output}: {text.count(chr(10)) - 1} path-slot rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
