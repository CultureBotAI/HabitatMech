#!/usr/bin/env python3
"""Rank the curation backlog and suggest candidate terms for each entry.

`just report` says *how much* is ungrounded; this says *what to do about it*.
For each undecided record, ranked by upstream assertion volume, it prints the
minted identifier a decision must key on, the source labels and paths that give
the concept its meaning, and the ontology terms whose label or synonym is
lexically close to it.

The suggestions are a starting point for a curator, never an answer: they are
lexical, and a lexical match is exactly what the seeder already declined to act
on. Anything written into curation/decisions.tsv is re-verified against the
ontology slice at seed time, so a bad suggestion cannot slip through by being
copied.

Usage:
    python3 scripts/curation_worklist.py                 # top 40 undecided
    python3 scripts/curation_worklist.py --limit 100
    python3 scripts/curation_worklist.py --out reports/worklist.tsv
    python3 scripts/curation_worklist.py --status all    # include decided ones
"""

from __future__ import annotations

import argparse
import csv
import difflib
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from habitatmech.curate.decisions import load_decisions  # noqa: E402
from habitatmech.seed import (  # noqa: E402
    DECISIONS_PATH,
    build_corpus,
    norm_label,
)


def suggest(label: str, index: dict[str, str], limit: int = 4) -> list[tuple[str, str]]:
    """Ontology terms whose label or synonym is closest to `label`."""
    key = norm_label(label)
    if not key:
        return []
    exact = [(tid, lbl) for lbl, tid in ((k, v) for k, v in index.items()) if lbl == key]
    if exact:
        return [(tid, lbl) for tid, lbl in exact][:limit]
    close = difflib.get_close_matches(key, index.keys(), n=limit, cutoff=0.72)
    return [(index[c], c) for c in close]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--limit", type=int, default=40)
    parser.add_argument("--status", choices=("undecided", "all"), default="undecided")
    parser.add_argument("--out", type=Path, help="Write the full worklist as TSV here.")
    args = parser.parse_args(argv)

    corpus = build_corpus()
    decided = set(load_decisions(DECISIONS_PATH))

    # Lexical index over every vendored term: normalised label/synonym -> id.
    index: dict[str, str] = {}
    for term_id, term in corpus.ontology.terms.items():
        for text in [term["label"], *(term.get("synonyms") or "").split("|")]:
            key = norm_label(text)
            if key:
                index.setdefault(key, term_id)

    rows = []
    for concept in corpus.concepts:
        if concept.grounding_status != "UNGROUNDED":
            continue
        assertions = sum(a.get("assertion_count") or 0 for a in concept.attestations)
        sources = "|".join(sorted({a["source"] for a in concept.attestations}))
        paths = "; ".join(
            a.get("source_path") or a.get("source_label", "") for a in concept.attestations
        )
        is_decided = concept.identifier in decided
        if args.status == "undecided" and is_decided:
            continue
        suggestions = suggest(concept.label, index)
        rows.append(
            {
                "identifier": concept.identifier,
                "label": concept.label,
                "category": concept.category or "",
                "assertions": assertions,
                "sources": sources,
                "source_paths": paths,
                "decided": "TRUE" if is_decided else "FALSE",
                "candidates": "|".join(f"{tid}={lbl}" for tid, lbl in suggestions),
            }
        )

    rows.sort(key=lambda r: (-r["assertions"], r["label"]))

    print(f"{len(rows)} ungrounded record(s) {'still undecided' if args.status == 'undecided' else ''}")
    print(f"decisions on file: {len(decided)}\n")
    for row in rows[: args.limit]:
        print(f"{row['assertions']:>7}  {row['label'][:46]:46s}  {row['identifier']}")
        print(f"         {row['source_paths'][:150]}")
        if row["candidates"]:
            for cand in row["candidates"].split("|"):
                print(f"           ? {cand}")
        print()

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        fields = ["identifier", "label", "category", "assertions", "sources",
                  "source_paths", "decided", "candidates"]
        with args.out.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=fields, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows({k: r[k] for k in fields} for r in rows)
        print(f"wrote {args.out} ({len(rows)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
