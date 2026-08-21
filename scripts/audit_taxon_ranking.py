#!/usr/bin/env python3
"""Measure whether PREGO's taxon ranking carries signal, against BacDive.

Issue #8 observed that PREGO's scores for a large habitat all sit at the top of
the range — for soil, 8,715 taxa between 4.0000 and 4.0073 — and proposed
ranking by evidence-channel breadth or direct-assertion count instead. Both
proposals are testable, and so is the premise, so this measures rather than
assumes.

Two questions:

1. **Which available signal discriminates most?** Counting distinct values a
   signal takes across a habitat's taxa. A signal with four possible values
   cannot order 8,715 taxa however intuitive it seems.

2. **Does the ranking correlate with an independent source?** BacDive reaches
   taxa by a completely different route (isolation source -> strain -> taxon,
   counted by distinct strain), so for habitats both sources attest, the overlap
   between PREGO's top-N and BacDive's taxa is a check no amount of reasoning
   about the scores can substitute for. The baseline is what that overlap would
   be if PREGO's order were random, which is the fraction of PREGO's taxa that
   BacDive knows at all, times N.

   Madin et al. is a second yardstick, literature-curated at species level, and
   independent of BacDive as well as of PREGO (#40). One yardstick agreeing
   could be one route's bias meeting another's; two independent yardsticks
   agreeing is harder to explain that way. They are reported separately rather
   than pooled, because pooling would let the larger overlap carry the smaller
   one and hide a disagreement between them.

Usage:
    python3 scripts/audit_taxon_ranking.py --kg-microbe /path/to/kg-microbe
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from habitatmech.extract import _raise_csv_limit, default_kg_microbe_root  # noqa: E402
from habitatmech.seed import build_corpus  # noqa: E402


def signal_spread(edges: list[dict[str, str]]) -> None:
    """How many distinct values each candidate ranking signal actually takes."""
    per: dict[str, dict] = defaultdict(
        lambda: {"score": 0.0, "channels": set(), "evidence": set(), "direct": 0, "edges": 0}
    )
    for row in edges:
        entry = per[row["object"]]
        entry["score"] = max(entry["score"], float(row.get("prego_score") or 0))
        if row.get("prego_channel"):
            entry["channels"].add(row["prego_channel"])
        if row.get("prego_evidence"):
            entry["evidence"].add(row["prego_evidence"])
        if (row.get("prego_direct_flag") or "").upper() == "TRUE":
            entry["direct"] += 1
        entry["edges"] += 1

    print(f"  taxa: {len(per)}")
    for name, fn in (
        ("max score", lambda e: round(e["score"], 4)),
        ("distinct evidence", lambda e: len(e["evidence"])),
        ("distinct channels", lambda e: len(e["channels"])),
        ("direct assertions", lambda e: e["direct"]),
        ("edge count", lambda e: e["edges"]),
    ):
        values = [fn(e) for e in per.values()]
        distinct = len(set(values))
        top = max(values)
        tied = sum(1 for v in values if v == top)
        print(f"    {name:20s} distinct values: {distinct:6d}   tied at max: {tied}")


def main(argv: list[str] | None = None) -> int:
    _raise_csv_limit()
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--kg-microbe", type=Path, default=default_kg_microbe_root())
    parser.add_argument("--top", type=int, default=25, help="N for the top-N overlap test.")
    parser.add_argument("--example", default="ENVO:00001998", help="Habitat for question 1.")
    args = parser.parse_args(argv)
    if args.kg_microbe is None or not args.kg_microbe.is_dir():
        parser.error("needs a kg-microbe checkout: --kg-microbe, KG_MICROBE_ROOT, or conf/sources.yaml")
    kgm = args.kg_microbe

    corpus = build_corpus()

    def paired_with(other: str) -> dict[str, tuple[str, str, str]]:
        """Habitats PREGO and `other` both attest, with each one's source id."""
        found: dict[str, tuple[str, str, str]] = {}
        for concept in corpus.concepts:
            ids = {a["source"]: a.get("source_id") for a in concept.attestations}
            if ids.get("PREGO") and ids.get(other):
                found[concept.identifier] = (concept.label, ids["PREGO"], ids[other])
        return found

    both = paired_with("BACDIVE")
    with_madin = paired_with("MADIN")

    wanted_prego = (
        {p for _, p, _ in both.values()} | {p for _, p, _ in with_madin.values()} | {args.example}
    )
    prego: dict[str, dict[str, float]] = defaultdict(dict)
    example_edges: list[dict[str, str]] = []
    with (kgm / "data" / "transformed" / "prego" / "edges.tsv").open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            subject = row["subject"]
            if subject not in wanted_prego:
                continue
            if subject == args.example:
                example_edges.append(row)
            taxon = row["object"]
            score = float(row.get("prego_score") or 0)
            prego[subject][taxon] = max(prego[subject].get(taxon, 0.0), score)

    print(f"=== 1. signal discrimination for {args.example} ===")
    signal_spread(example_edges)

    wanted_bacdive = {b for _, _, b in both.values()}
    source_strains: dict[str, set[str]] = defaultdict(set)
    strain_taxon: dict[str, str] = {}
    with (kgm / "data" / "transformed" / "bacdive" / "edges.tsv").open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            subject, obj = row["subject"], row["object"]
            if subject in wanted_bacdive and obj.startswith("kgmicrobe.strain:"):
                source_strains[subject].add(obj)
            elif (
                subject.startswith("kgmicrobe.strain:")
                and row.get("predicate") == "biolink:subclass_of"
                and obj.startswith("NCBITaxon:")
            ):
                strain_taxon[subject] = obj
    bacdive: dict[str, set[str]] = {
        src: {strain_taxon[s] for s in strains if s in strain_taxon}
        for src, strains in source_strains.items()
    }

    madin: dict[str, set[str]] = defaultdict(set)
    madin_edges = kgm / "data" / "transformed" / "madin_etal" / "edges.tsv"
    if madin_edges.exists():
        with madin_edges.open(newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                if row.get("predicate") == "biolink:location_of" and row["object"].startswith(
                    "NCBITaxon:"
                ):
                    madin[row["subject"]].add(row["object"])

    yardsticks = [("BacDive", both, bacdive), ("Madin", with_madin, dict(madin))]
    for name, pairs, known_by_id in yardsticks:
        _enrichment(name, pairs, prego, known_by_id, args.top)
    return 0


def _enrichment(
    name: str,
    pairs: dict[str, tuple[str, str, str]],
    prego: dict[str, dict[str, float]],
    known_by_id: dict[str, set[str]],
    top_n: int,
) -> None:
    print(f"\n=== does PREGO's top-{top_n} beat chance against {name}? ===")
    print(f"  {len(pairs)} habitats attested by both sources")
    other = f"|{name}|"
    print(f"  {'habitat':28s} {'|PREGO|':>8} {other:>10} {'shared':>7} {'hits':>5} {'chance':>7}")
    hits_total = expected_total = 0.0
    tested = 0
    for label, prego_id, other_id in sorted(pairs.values()):
        pool, known = prego.get(prego_id, {}), known_by_id.get(other_id, set())
        shared = set(pool) & known
        if len(pool) < 50 or len(known) < 10 or len(shared) < 5:
            continue
        top = sorted(pool, key=lambda t: -pool[t])[:top_n]
        hits = len(set(top) & known)
        # If PREGO's order carried no information, a top-N slice would contain
        # the same fraction of yardstick-known taxa as the pool as a whole.
        expected = top_n * len(shared) / len(pool)
        hits_total += hits
        expected_total += expected
        tested += 1
        print(
            f"  {label[:28]:28s} {len(pool):8d} {len(known):10d} "
            f"{len(shared):7d} {hits:5d} {expected:7.2f}"
        )

    print(f"\n  habitats tested: {tested}")
    print(f"  top-{top_n} hits: {hits_total:.0f}   expected by chance: {expected_total:.1f}")
    if expected_total:
        print(f"  enrichment vs {name}: {hits_total / expected_total:.2f}x")
        print(
            "\n  A ratio near 1.0 would mean the ranking is noise and should be replaced.\n"
            "  Above 1.0 means it carries signal — but note the sample is small, so this\n"
            "  is evidence that the ranking is not arbitrary, not that it is good."
        )


if __name__ == "__main__":
    raise SystemExit(main())
