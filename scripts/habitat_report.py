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
from seed_from_sources import mint, norm_label  # noqa: E402

# How an upstream mapping's object label relates to the words in the subject it
# claims to map. The seeder's label check (#39, #41) compares the object_id
# against the object_label and catches a mismatch between the two; it is blind
# by construction when they agree and the *mapping* is still wrong. These
# cohorts are the screen for that second defect class. Measured over the 280
# grounded rows: 136 identical, 62 overlap, 42 subset, 40 disjoint.
COHORTS = {
    # The object label is exactly the subject. Nothing a curator adds here that
    # the mechanical check does not already cover.
    "identical": "no review needed",
    # Shares words, neither contains the other — "acid mine drainage" ->
    # "acid mine drainage site". Low risk.
    "overlap": "low risk",
    # The object's words are a strict subset of the subject's: the mapping
    # dropped modifiers. "Cooling-tower" -> Tower, "Sterilized-plant-part" ->
    # Part. Half of these are fine, because the subject is an enumeration
    # ("Feces-Stool" -> feces) — so this ranks, it does not decide.
    "subset": "modifiers dropped; over-generic targets and merges live here",
    # No shared word: matched on a synonym or a scientific name. Mostly right
    # ("Chicken" -> Gallus gallus), but over-NARROWING hides here — "Reptilia"
    # -> Lepidosauria drops turtles and crocodilians.
    "disjoint": "synonym match; over-narrowing hides here",
}
RISK_COHORTS = ("subset", "disjoint")


def _words(text: str) -> set[str]:
    return {w for w in norm_label(text).split() if w}


# Longest suffix an inflection may add before two labels stop counting as the
# same word: "compost"/"composting" is 3, and nothing useful is longer.
_INFLECTION_SLACK = 3


def label_cohort(subject: str, object_label: str) -> str:
    subject_words, object_words = _words(subject), _words(object_label)
    if not object_words:
        return "overlap"

    # Word-set comparison alone calls "Wastewater" -> "waste water" and
    # "Composting" -> "compost" disjoint, which is a tokenization artefact
    # rather than a mapping defect. Comparing the labels with the spaces taken
    # out catches both, and dropping a short inflectional tail catches the
    # second. Deliberately narrow: it must not swallow "Cooling-tower" ->
    # "Tower", where the missing word is the whole of the meaning.
    flat_subject, flat_object = "".join(sorted(subject_words)), "".join(sorted(object_words))
    joined_subject = norm_label(subject).replace(" ", "")
    joined_object = norm_label(object_label).replace(" ", "")
    if flat_subject == flat_object or joined_subject == joined_object:
        return "identical"
    longer, shorter = sorted((joined_subject, joined_object), key=len, reverse=True)
    if shorter and longer.startswith(shorter) and len(longer) - len(shorter) <= _INFLECTION_SLACK:
        return "identical"

    if subject_words == object_words:
        return "identical"
    if object_words < subject_words:
        return "subset"
    if not subject_words & object_words:
        return "disjoint"
    return "overlap"


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


def _mapping_cohorts(decided: set[str]) -> tuple[Counter, int, list[tuple]]:
    """Split the upstream mappings by cohort and rank the undecided risky ones.

    A row is "decided" once every source concept it feeds has a per-item entry
    in curation/decisions.tsv, so this shrinks as the review proceeds — like the
    ungrounded backlog, and unlike a one-off audit.

    Both routes into the mapping table are joined. BacDive resolves a source by
    normalized label falling back to slug; GOLD reaches the same table by its
    leaf label. Joining only the first understated the backlog by 52 concepts
    and blamed the gap on rows this corpus does not carry (#52).
    """
    raw = REPO_ROOT / "data" / "raw"
    mapping_path = raw / "isolation_source_groundings.tsv"
    sources_path = raw / "bacdive_isolation_sources.tsv"
    gold_path = raw / "gold_ecosystem_paths.tsv"
    if not mapping_path.exists() or not sources_path.exists():
        return Counter(), 0, []

    # Invert each source's own join so a mapping row can name the minted
    # identifiers a decision would have to key on. Value is (minted id, volume).
    by_key: dict[str, list[tuple[str, int]]] = defaultdict(list)
    with sources_path.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            entry = (mint("BACDIVE", row["bacdive_id"]), int(row.get("strain_count") or 0))
            for key in (norm_label(row["label"]), norm_label(row["source_slug"])):
                if key:
                    by_key[key].append(entry)
    if gold_path.exists():
        with gold_path.open(newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                key = norm_label(row.get("leaf_label", ""))
                if key:
                    by_key[key].append((
                        mint("GOLD", row["canonical_path"]),
                        int(row.get("total_assertions") or 0),
                    ))

    counts: Counter = Counter()
    risky = 0
    backlog = []
    with mapping_path.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            target = (row.get("object_id") or "").strip()
            if not target:
                continue
            cohort = label_cohort(row["subject_label_normalized"], row["object_label"])
            counts[cohort] += 1
            if cohort not in RISK_COHORTS:
                continue
            risky += 1
            # A source is indexed under several keys that collide for most of
            # them — dedupe or a row lists once per key that matched.
            seen: set[str] = set()
            for identifier, volume in by_key.get(norm_label(row["subject_label"]), ()):
                if identifier in decided or identifier in seen:
                    continue
                seen.add(identifier)
                backlog.append((
                    # A target the seeder would adopt as the record's identity
                    # is worth more attention than one it can only keep as an
                    # xref, so rank on that before assertion volume.
                    target.split(":", 1)[0] in _IDENTITY_PREFIXES,
                    volume, cohort,
                    row["subject_label"], target, row["object_label"], identifier,
                ))
    return counts, risky, sorted(backlog, reverse=True)


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
    # A CLASS-depth sweep did not read the mapping, so it does not clear a row
    # from the cohort backlog; only per-item judgement does.
    item_decided: set[str] = set()
    decisions_path = REPO_ROOT / "curation" / "decisions.tsv"
    if decisions_path.exists():
        with decisions_path.open(newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                if (row.get("review_depth") or "ITEM").strip().upper() == "CLASS":
                    class_swept_ids.add(row["identifier"])
                else:
                    item_decided.add(row["identifier"])

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

    cohorts, risky_total, cohort_backlog = _mapping_cohorts(item_decided)
    if cohorts:
        total_mapped = sum(cohorts[c] for c in COHORTS)
        print(f"\n=== {total_mapped} upstream mappings, by how the object label relates "
              "to the subject ===")
        print("  (the seeder checks object_id against object_label; it is blind by")
        print("   construction when those agree and the mapping itself is wrong)")
        for cohort, why in COHORTS.items():
            marker = "  <-" if cohort in RISK_COHORTS else "    "
            print(f"  {cohort:12s} {cohorts.get(cohort, 0):5d}{marker} {why}")

    if cohort_backlog and args.ungrounded_top:
        identity = sum(1 for row in cohort_backlog if row[0])
        shown = min(args.ungrounded_top, len(cohort_backlog))
        print(f"\n=== {len(cohort_backlog)} of {risky_total} risky mappings still "
              "undecided ===")
        print(f"  ({identity} would become a record's identity and rank first; the rest are")
        print("   kept only as an xref. The gap to the cohort total is rows already decided")
        print("   per-item, or naming a subject neither BacDive nor GOLD brings into this")
        print(f"   corpus. Volume is strains for BacDive, assertions for GOLD. Showing {shown}.)")
        for is_identity, strains, cohort, subject, target, label, identifier in (
            cohort_backlog[: args.ungrounded_top]
        ):
            flag = "id " if is_identity else "   "
            print(f"  {flag}{strains:7d}  {cohort:8s} {subject[:26]:26s} -> {target:18s} "
                  f"{label[:26]:26s} {identifier}")

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
