#!/usr/bin/env python3
"""Propose curation decisions for the undecided backlog, for a curator to review.

This is deliberately NOT an auto-curator. It splits the backlog into what can be
decided mechanically without judgement and what cannot, and it is conservative
about which is which, because a wrong grounding is worse than no grounding: it
looks identical to a right one in the output.

Tiers
-----
``auto``    The normalised leaf label (or its singular) equals an ontology
            term's *label* exactly, and exactly one term matches. Nothing is
            inferred — this is string equality against an authoritative label,
            the same evidence a curator would use. Emitted as GROUND/EXACT.

``review``  A candidate exists but the match needs judgement: it came from a
            synonym, from a plural/parenthetical/slash variant, or several terms
            matched. These are emitted with their top candidates and a blank
            decision for a curator to fill in.

``none``    No candidate at all in the vendored slice.

Why synonym matches are never auto-accepted: ENVO lists "grassland" as a synonym
of `agricultural field`, and "wetland" as a synonym of `marsh`, while the terms
a curator actually wants (`grassland area`, `wetland area`) exist separately.
An auto-accepting matcher grounds both wrongly and confidently.

Usage:
    python3 scripts/propose_decisions.py --out reports/proposals.tsv
    python3 scripts/propose_decisions.py --tier review --limit 40
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from pathlib import Path

from habitatmech.curate.decisions import load_decisions
from habitatmech.seed import DECISIONS_PATH, build_corpus, norm_label

REPO_ROOT = Path(__file__).resolve().parents[2]

# Ontology preference when several ontologies carry the same label.
PRIORITY = {"ENVO": 0, "UBERON": 1, "FOODON": 2, "BTO": 3}


def label_variants(label: str) -> list[str]:
    """Forms of a source label worth testing, most faithful first.

    GOLD writes alternatives with a slash ("Phylloplane/Leaf"), glosses with
    parentheses ("AGS (Aerobic granular sludge)"), and qualifies with a colon
    ("Abscess: Furuncle/Boil"). Splitting these is not inference — it is undoing
    a formatting convention — but the pieces are still only ever *proposals*.
    """
    out: list[str] = [label.strip()]
    text = label.strip()
    if "/" in text:
        out += [p.strip() for p in text.split("/")]
    match = re.match(r"^(.*?)\s*\((.*)\)\s*$", text)
    if match:
        out += [match.group(1).strip(), match.group(2).strip()]
    if ":" in text:
        out += [p.strip() for p in text.split(":")]
    for variant in list(out):
        if variant.lower().endswith("s") and len(variant) > 4:
            out.append(variant[:-1])
    return [v for v in dict.fromkeys(out) if v]


def build_index(terms: dict) -> tuple[dict, dict]:
    """normalised text -> [(term_id, label)], separately for labels and synonyms.

    Lists, not first-wins: collapsing to one term is how "grassland" silently
    became `agricultural field` instead of `grassland area`.
    """
    by_label: dict[str, list[tuple[str, str]]] = defaultdict(list)
    by_synonym: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for term_id, term in terms.items():
        ontology = term_id.split(":", 1)[0]
        if ontology not in PRIORITY:
            continue
        key = norm_label(term["label"])
        if key:
            by_label[key].append((term_id, term["label"]))
        for synonym in (term.get("synonyms") or "").split("|"):
            skey = norm_label(synonym)
            if skey:
                by_synonym[skey].append((term_id, term["label"]))
    for index in (by_label, by_synonym):
        for key in index:
            index[key].sort(key=lambda t: (PRIORITY.get(t[0].split(":", 1)[0], 9), t[0]))
    return by_label, by_synonym


def classify(label: str, by_label: dict, by_synonym: dict) -> tuple[str, list[tuple[str, str]], str]:
    """Return (tier, candidates, evidence) for one source label."""
    variants = label_variants(label)
    # Exact label match on the unmodified label, unique -> safe to auto-accept.
    head = norm_label(variants[0])
    exact = by_label.get(head, [])
    if len(exact) == 1:
        return "auto", exact, f"label=={exact[0][1]!r}"
    if len(exact) > 1:
        return "review", exact, f"{len(exact)} terms share this label"

    # Singular of the unmodified label, unique -> also string equality.
    if len(variants) > 1:
        for variant in variants[1:]:
            if variant.lower() == label.strip().lower()[:-1]:
                singular = by_label.get(norm_label(variant), [])
                if len(singular) == 1:
                    return "auto", singular, f"singular label=={singular[0][1]!r}"

    candidates: list[tuple[str, str]] = []
    evidence = ""
    for variant in variants:
        key = norm_label(variant)
        if key in by_label:
            candidates = by_label[key]
            evidence = f"variant {variant!r} == label"
            break
        if key in by_synonym:
            candidates = by_synonym[key]
            evidence = f"variant {variant!r} == synonym"
            break
    if candidates:
        return "review", candidates[:3], evidence
    return "none", [], ""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", type=Path, help="Write proposals here as TSV.")
    parser.add_argument("--tier", choices=("auto", "review", "none", "all"), default="all")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--min-assertions", type=int, default=0)
    args = parser.parse_args(argv)

    corpus = build_corpus()
    decided = set(load_decisions(DECISIONS_PATH))
    by_label, by_synonym = build_index(corpus.ontology.terms)

    rows = []
    for concept in corpus.concepts:
        if concept.grounding_status != "UNGROUNDED" or concept.identifier in decided:
            continue
        assertions = sum(a.get("assertion_count") or 0 for a in concept.attestations)
        if assertions < args.min_assertions:
            continue
        tier, candidates, evidence = classify(concept.label, by_label, by_synonym)
        rows.append(
            {
                "identifier": concept.identifier,
                "label": concept.label,
                "assertions": assertions,
                "tier": tier,
                "evidence": evidence,
                "candidates": "|".join(f"{tid}={lbl}" for tid, lbl in candidates),
                "source_paths": "; ".join(
                    a.get("source_path") or a.get("source_label", "") for a in concept.attestations
                )[:200],
            }
        )
    rows.sort(key=lambda r: (r["tier"], -r["assertions"], r["label"]))

    counts: dict[str, int] = defaultdict(int)
    for row in rows:
        counts[row["tier"]] += 1
    print(f"{len(rows)} undecided ungrounded concept(s)")
    for tier in ("auto", "review", "none"):
        weighted = sum(r["assertions"] for r in rows if r["tier"] == tier)
        print(f"  {tier:8s} {counts[tier]:5d}   ({weighted} upstream assertions)")

    shown = [r for r in rows if args.tier in ("all", r["tier"])]
    if args.limit:
        shown = shown[: args.limit]
        print()
        for row in shown:
            print(f"{row['assertions']:>7}  {row['label'][:38]:38s}  {row['identifier']}")
            print(f"         {row['source_paths'][:120]}")
            print(f"         {row['evidence']}  ->  {row['candidates']}")
            print()

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        fields = ["identifier", "label", "assertions", "tier", "evidence",
                  "candidates", "source_paths"]
        with args.out.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=fields, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
        print(f"\nwrote {args.out} ({len(rows)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
