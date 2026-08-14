#!/usr/bin/env python3
"""Corpus report over data/habitats/.

Answers the questions a curator actually has about the seeded corpus: how much
of it is grounded, which records are corroborated by more than one source, and
where the ungrounded mass sits (those are the ENVO term-request backlog).

Usage:
    python3 scripts/habitat_report.py
    python3 scripts/habitat_report.py --out reports/corpus.tsv
    python3 scripts/habitat_report.py --ungrounded-top 40
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
HABITATS_DIR = REPO_ROOT / "data" / "habitats"

sys.path.insert(0, str(REPO_ROOT / "scripts"))

# The prefixes a habitat record's identifier may use. Imported rather than
# copied: the flag it drives separates "a wrong id here becomes a record" from
# "a wrong id here is only an xref", and a second copy would quietly stop
# flagging any prefix the seeder later gains (#48).
from seed_from_sources import HABITAT_PREFIXES as _IDENTITY_PREFIXES  # noqa: E402


def load_records(root: Path) -> list[tuple[Path, dict]]:
    records = []
    for path in sorted(root.rglob("*.yaml")):
        with path.open(encoding="utf-8") as fh:
            doc = yaml.safe_load(fh)
        if isinstance(doc, dict):
            records.append((path, doc))
    return records


def table(title: str, counts: Counter, total: int) -> None:
    print(f"\n=== {title} ===")
    for key, count in counts.most_common():
        share = f"{100 * count / total:5.1f}%" if total else "    -"
        print(f"  {str(key):26s} {count:6d}  {share}")


def _unverifiable_mapping_targets() -> list[tuple[str, str, str, bool]]:
    """Upstream mapping targets whose label the seeder cannot check.

    The check compares an upstream row's `object_label` against the ontology's
    own label, which is what stops a wrong id reaching a record. It can only run
    for terms in the vendored slice, so anything outside it passes unexamined —
    and that silence is worth printing, because upstream has a measured error
    rate on the rows that can be checked (#41).
    """
    raw = REPO_ROOT / "data" / "raw"
    terms_path, mapping_path = raw / "ontology_terms.tsv", raw / "isolation_source_groundings.tsv"
    if not terms_path.exists() or not mapping_path.exists():
        return []
    with terms_path.open(newline="", encoding="utf-8") as fh:
        known = {r["term_id"] for r in csv.DictReader(fh, delimiter="\t")}
    out = []
    with mapping_path.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            target = (row.get("object_id") or "").strip()
            if target and target not in known:
                out.append((
                    row.get("subject_label", ""), target, row.get("object_label", ""),
                    target.split(":", 1)[0] in _IDENTITY_PREFIXES,
                ))
    return sorted(out, key=lambda r: (not r[3], r[0]))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=HABITATS_DIR)
    parser.add_argument("--out", type=Path, help="Write a per-record TSV here.")
    parser.add_argument(
        "--ungrounded-top",
        type=int,
        default=20,
        help="Show the N ungrounded records with the most upstream assertions "
        "(the highest-yield ENVO term requests).",
    )
    args = parser.parse_args(argv)

    if not args.root.exists():
        raise SystemExit(f"no corpus at {args.root}; run `just seed-apply` first")

    # Decisions taken at CLASS depth are recorded but do not promote a record to
    # REVIEWED; reporting them with the wholly-undecided ones would hide that a
    # sweep happened, and with the term requests would overstate it.
    class_swept_ids: set[str] = set()
    decisions_path = REPO_ROOT / "curation" / "decisions.tsv"
    if decisions_path.exists():
        with decisions_path.open(newline="", encoding="utf-8") as fh:
            class_swept_ids = {
                r["identifier"]
                for r in csv.DictReader(fh, delimiter="\t")
                if (r.get("review_depth") or "ITEM").strip().upper() == "CLASS"
            }

    records = load_records(args.root)
    total = len(records)
    if not total:
        raise SystemExit(f"no records under {args.root}")

    print(f"=== HabitatMech corpus: {total} records under {args.root.relative_to(REPO_ROOT)} ===")

    by_category: Counter = Counter()
    by_grounding: Counter = Counter()
    by_status: Counter = Counter()
    by_prefix: Counter = Counter()
    by_source: Counter = Counter()
    corroboration: Counter = Counter()
    field_coverage: Counter = Counter()
    # An ungrounded record that a curator has confirmed is a term request;
    # one nobody has looked at yet is backlog. Reporting them together hides
    # all the progress and all the remaining work at once.
    term_requests: list[tuple[int, str, str]] = []
    class_swept: list[tuple[int, str, str]] = []
    undecided: list[tuple[int, str, str]] = []
    source_totals: dict[str, int] = defaultdict(int)
    rows = []

    for path, doc in records:
        identifier = doc.get("identifier", "")
        by_category[doc.get("habitat_category", "?")] += 1
        by_grounding[doc.get("grounding_status", "?")] += 1
        by_status[doc.get("mapping_status", "?")] += 1
        by_prefix[identifier.split(":", 1)[0]] += 1

        attestations = doc.get("source_attestations") or []
        sources = sorted({a.get("source", "?") for a in attestations})
        for source in sources:
            by_source[source] += 1
        corroboration[len(sources)] += 1

        assertions = 0
        for attestation in attestations:
            count = attestation.get("assertion_count") or 0
            assertions += count
            source_totals[attestation.get("source", "?")] += count

        for field in ("definition", "environmental_parameters", "characteristic_taxa",
                      "parent_habitats", "causal_graphs", "evidence"):
            if doc.get(field):
                field_coverage[field] += 1

        if doc.get("grounding_status") == "UNGROUNDED":
            if doc.get("mapping_status") == "REVIEWED":
                bucket = term_requests
            elif identifier in class_swept_ids:
                bucket = class_swept
            else:
                bucket = undecided
            bucket.append((assertions, doc.get("label", ""), identifier))

        rows.append(
            {
                "identifier": identifier,
                "label": doc.get("label", ""),
                "habitat_category": doc.get("habitat_category", ""),
                "grounding_status": doc.get("grounding_status", ""),
                "mapping_status": doc.get("mapping_status", ""),
                "sources": "|".join(sources),
                "source_count": len(sources),
                "assertion_total": assertions,
                "has_definition": bool(doc.get("definition")),
                "n_parents": len(doc.get("parent_habitats") or []),
                "n_parameters": len(doc.get("environmental_parameters") or []),
                "n_taxa": len(doc.get("characteristic_taxa") or []),
                "n_causal_graphs": len(doc.get("causal_graphs") or []),
                "path": str(path.relative_to(REPO_ROOT)),
            }
        )

    table("habitat_category", by_category, total)
    table("grounding_status", by_grounding, total)
    table("mapping_status", by_status, total)
    table("identifier prefix", by_prefix, total)
    table("records attested by each source", by_source, total)
    table("field coverage", field_coverage, total)

    print("\n=== source corroboration ===")
    for n, count in sorted(corroboration.items()):
        print(f"  attested by {n} source(s)  {count:6d}  {100 * count / total:5.1f}%")

    print("\n=== upstream assertions behind the corpus ===")
    print("  (counts are per-source units and are NOT summable across sources)")
    for source, count in sorted(source_totals.items(), key=lambda kv: -kv[1]):
        print(f"  {source:22s} {count:9d}")

    if term_requests:
        term_requests.sort(reverse=True)
        print(f"\n=== ENVO term requests: {len(term_requests)} examined individually ===")
        print("  (a curator read these and confirmed no term fits)")
        for assertions, label, identifier in term_requests[: args.ungrounded_top or len(term_requests)]:
            print(f"  {assertions:8d}  {label[:52]:52s}  {identifier}")

    if class_swept:
        class_swept.sort(reverse=True)
        total_assertions = sum(a for a, _, _ in class_swept)
        print(f"\n=== class-level sweep: {len(class_swept)} ungrounded, {total_assertions} assertions ===")
        print("  (no term matched by any lexical route, but nobody read them one by one —")
        print("   they do NOT count as REVIEWED. `just worklist` ranks them for real curation.)")
        for assertions, label, identifier in class_swept[: args.ungrounded_top]:
            print(f"  {assertions:8d}  {label[:52]:52s}  {identifier}")

    if args.ungrounded_top and undecided:
        undecided.sort(reverse=True)
        print(f"\n=== top {args.ungrounded_top} wholly UNDECIDED ungrounded records ===")
        for assertions, label, identifier in undecided[: args.ungrounded_top]:
            print(f"  {assertions:8d}  {label[:52]:52s}  {identifier}")

    unverifiable = _unverifiable_mapping_targets()
    if unverifiable:
        print(f"\n=== {len(unverifiable)} upstream mapping target(s) that cannot be label-checked ===")
        print("  (their ontology is not vendored, so a wrong id here would not be caught;")
        print("   upstream has a measured error rate on the rows that CAN be checked)")
        for subject, target, claimed, identity in unverifiable:
            flag = "  <- can be a record identity" if identity else ""
            print(f"  {subject[:26]:26s} {target:18s} claims {claimed!r}{flag}")

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with args.out.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows(sorted(rows, key=lambda r: r["identifier"]))
        print(f"\nwrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
