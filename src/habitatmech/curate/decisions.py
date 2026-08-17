"""Curator decisions, and the validation that keeps them honest.

Records under ``data/habitats/`` are generated from ``data/raw/`` and
``scripts/verify_corpus.py`` gates that they reproduce exactly, so curation
cannot be a hand-edit to a record — it would be silently reverted by the next
re-seed. Curation therefore lives in ``curation/decisions.tsv``, which the
seeder reads as an input. The benefits are the point rather than a side effect:

* a curation pass is a small, reviewable diff in one file, not 3299 rewritten
  YAMLs;
* every decision carries its curator, date, and reason, so the *why* survives;
* the corpus stays fully reproducible, so `verify_corpus` keeps working
  unchanged;
* the decisions can be re-applied after an upstream refresh, because they key
  on content-hashed identifiers that survive re-seeding.

Anti-hallucination
------------------
A curator (human or LLM) writing ``UBERON:0001988`` has to be checked, because
a plausible-looking but wrong CURIE is indistinguishable from a right one in
the output. Every ``GROUND`` decision must therefore name both the target CURIE
and the label it expects, and :func:`validate_decisions` fails the load unless
the term exists in the vendored ontology slice *and* its label matches exactly.
An invented term ID cannot pass, and neither can a real term ID paired with the
wrong concept.
"""

from __future__ import annotations

import csv
import datetime
from dataclasses import dataclass
from pathlib import Path

__all__ = [
    "Decision",
    "DECISION_KINDS",
    "load_decisions",
    "validate_decisions",
    "DecisionError",
]

# What a curator can decide about a source concept.
DECISION_KINDS = {
    # Redirect this source concept onto an ontology term. The record merges with
    # any other concept resolving to the same term.
    "GROUND",
    # Not a habitat at all (a host taxon, a disease process, a quality). Keeps
    # the minted identifier so the concept stays citable; the term that
    # describes it, if any, is kept as an xref.
    "NOT_APPLICABLE",
    # Genuinely a habitat, genuinely no term that fits as its identity. This is
    # the reviewed form of UNGROUNDED and is the ENVO term-request list. It may
    # carry an object_id naming the nearest *broader* term, which is attached as
    # a parent rather than adopted as the identity — that keeps the placement
    # machine-readable without asserting an equivalence that does not hold.
    "CONFIRM_UNGROUNDED",
    # This source concept IS the concept another minted identifier already
    # names. Merging otherwise only happens when two concepts resolve to the
    # same ONTOLOGY term, so before this there was no way to say that two novel
    # concepts — ones no ontology names — are the same thing. GOLD's
    # "Mammals: Human" and BacDive's "Human" sat as two permanent records
    # holding 40,432 and 11,697 assertions for one habitat (#116).
    "SAME_AS",
    # Narrower than an existing term: keep the minted identity, record the term
    # as a parent, and mark the grounding NARROW. This is the curated form of
    # the seeder's ambiguous-leaf rule. Six GOLD paths end in "Microbial mats"
    # and only the shallowest can BE ENVO:01000008; the others are kinds of it,
    # and grounding them all there would merge marine, hot-spring and
    # hypersaline mats into one record.
    "GROUND_AS_PARENT",
    # No grounding change; the curator checked the record as the seeder built it.
    "REVIEW",
}

GROUNDING_STATUSES = {"EXACT", "BROAD", "NARROW", "CLOSE"}

# How closely a curator looked. ITEM means this specific concept was examined
# against its source path and candidate terms. CLASS means it was decided as a
# member of a mechanically-defined group — for instance "no term in the
# vendored slice matches this label by exact, variant, composed or substring
# search", which is verifiable but is not the same as someone having thought
# about this habitat. Only ITEM decisions count toward mapping_status REVIEWED;
# without the distinction a bulk sweep would report the corpus as reviewed when
# nobody had read a line of it.
REVIEW_DEPTHS = {"ITEM", "CLASS"}

# Categories a decision may override the seeder's inference with. Kept in step
# with HabitatCategoryEnum by tests/test_schema.py.
CATEGORIES = {
    "TERRESTRIAL", "AQUATIC", "AIR", "HOST_ASSOCIATED",
    "ENGINEERED", "FOOD", "CLINICAL", "OTHER",
}
DEFAULT_REVIEW_DEPTH = "ITEM"

# How a decision's object_id attaches to the record. `parent` asserts the term
# is BROADER than the concept, which is what parent_habitats means; `xref`
# asserts only that the two are related. Without the second, a term that is
# neither the concept's identity nor broader than it could not be kept at all:
# BacDive's "Contamination" against ENVO's *anthropogenic contamination
# feature* had to drop the link entirely, because every kind that placed a term
# placed it as an identity or an is-a (#99).
RELATIONS = {"parent", "xref"}
DEFAULT_RELATION = "parent"

REQUIRED_COLUMNS = [
    "identifier",
    "decision",
    "object_id",
    "object_label",
    "grounding_status",
    "curator",
    "date",
    "notes",
]

# A decision without a reason is not reviewable — the next curator cannot tell
# whether it was considered or guessed.
MIN_NOTES_CHARS = 20


class DecisionError(SystemExit):
    """Raised on a malformed or unverifiable decision. Fails the seed."""


@dataclass(frozen=True)
class Decision:
    identifier: str
    decision: str
    object_id: str
    object_label: str
    grounding_status: str
    curator: str
    date: str
    notes: str
    review_depth: str = DEFAULT_REVIEW_DEPTH
    # Overrides the seeder's category inference for the record this concept
    # lands in. The inference follows GOLD's path, which encodes the SETTING a
    # sample came from — right for "marine sediment" but wrong when the leaf
    # names a different kind of thing entirely, as GOLD's Air branch does for
    # the biofilm growing inside an air scrubber. Blanket rules do worse: using
    # the matched term's own category instead would move 90 marine and lake
    # sediments out of AQUATIC.
    category: str = ""
    # See RELATIONS. Defaults to `parent`, so decisions written before this
    # existed keep the behaviour they were reviewed under.
    relation: str = DEFAULT_RELATION

    @property
    def counts_as_reviewed(self) -> bool:
        """Only per-item judgement promotes a record to REVIEWED."""
        return self.review_depth == "ITEM"

    @property
    def is_grounding(self) -> bool:
        return self.decision in ("GROUND", "GROUND_AS_PARENT")


def load_decisions(path: Path) -> dict[str, Decision]:
    """Read the decisions file. Missing file means no curation yet, not an error."""
    if not path.exists():
        return {}
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        missing = set(REQUIRED_COLUMNS) - set(reader.fieldnames or [])
        if missing:
            raise DecisionError(f"{path}: missing columns {sorted(missing)}")
        decisions: dict[str, Decision] = {}
        for line_no, row in enumerate(reader, start=2):
            identifier = (row["identifier"] or "").strip()
            if not identifier or identifier.startswith("#"):
                continue
            if identifier in decisions:
                raise DecisionError(f"{path}:{line_no}: duplicate decision for {identifier}")
            decisions[identifier] = Decision(
                identifier=identifier,
                decision=(row["decision"] or "").strip().upper(),
                object_id=(row["object_id"] or "").strip(),
                object_label=(row["object_label"] or "").strip(),
                grounding_status=(row["grounding_status"] or "").strip().upper(),
                curator=(row["curator"] or "").strip(),
                date=(row["date"] or "").strip(),
                notes=(row["notes"] or "").strip(),
                review_depth=(row.get("review_depth") or DEFAULT_REVIEW_DEPTH).strip().upper()
                or DEFAULT_REVIEW_DEPTH,
                category=(row.get("category") or "").strip().upper(),
                relation=(row.get("relation") or DEFAULT_RELATION).strip().lower()
                or DEFAULT_RELATION,
            )
    return decisions


def resolve_same_as(decisions: dict[str, Decision]) -> dict[str, str]:
    """Follow SAME_AS chains to the identifier each concept finally lands on.

    Chains are allowed because they arise naturally — three sources naming one
    concept means two SAME_AS rows, and requiring a curator to point both at the
    same winner makes the second decision depend on the first. Cycles are not:
    A SAME_AS B SAME_AS A has no answer, and silently picking one would make the
    corpus depend on dict ordering.
    """
    targets = {
        identifier: decision.object_id
        for identifier, decision in decisions.items()
        if decision.decision == "SAME_AS" and decision.object_id
    }
    resolved: dict[str, str] = {}
    for start in targets:
        seen, node = [start], start
        while node in targets:
            node = targets[node]
            if node in seen:
                raise DecisionError(
                    "SAME_AS cycle: " + " -> ".join([*seen, node])
                )
            seen.append(node)
        resolved[start] = node
    return resolved


def validate_decisions(
    decisions: dict[str, Decision],
    ontology_label: dict[str, str],
    *,
    path: Path | None = None,
    label_only: set[str] | None = None,
) -> None:
    """Fail loudly on any decision that is malformed or cannot be verified.

    ``ontology_label`` maps term id -> label for the vendored slice. A GROUND
    target absent from it is either invented or outside what the repo vendors;
    either way the seeder must not act on it silently.

    ``label_only`` names the terms the slice has a label for but no place for —
    pulled in to check a mapping target, never positioned in a hierarchy. A
    record grounded onto one has no parents, no siblings and nothing above it,
    and until #46 that was indistinguishable here from a properly vendored term.
    """
    where = f"{path}: " if path else ""
    problems: list[str] = []

    for identifier, decision in sorted(decisions.items()):
        prefix = f"{where}{identifier}"

        if decision.decision not in DECISION_KINDS:
            problems.append(
                f"{prefix}: unknown decision {decision.decision!r}; "
                f"expected one of {sorted(DECISION_KINDS)}"
            )
            continue
        if decision.category and decision.category not in CATEGORIES:
            problems.append(
                f"{prefix}: category {decision.category!r} not in {sorted(CATEGORIES)}"
            )
        if decision.category and decision.review_depth != "ITEM":
            problems.append(
                f"{prefix}: a category override is a per-record judgement and cannot be "
                "CLASS depth"
            )
        if decision.relation not in RELATIONS:
            problems.append(
                f"{prefix}: relation {decision.relation!r} not in {sorted(RELATIONS)}"
            )
        if decision.relation == "xref" and decision.decision == "GROUND":
            # GROUND makes the term the record's identity; there is nothing
            # left for a relation to say, and accepting it would let a curator
            # believe they had asked for a weaker link than they got.
            problems.append(
                f"{prefix}: relation 'xref' is meaningless on GROUND, which adopts "
                "the term as the record's identity"
            )
        if decision.relation != DEFAULT_RELATION and not decision.object_id:
            problems.append(
                f"{prefix}: relation {decision.relation!r} set but there is no "
                "object_id for it to place"
            )
        if decision.review_depth not in REVIEW_DEPTHS:
            problems.append(
                f"{prefix}: review_depth {decision.review_depth!r} not in {sorted(REVIEW_DEPTHS)}"
            )
        if decision.review_depth == "CLASS" and decision.is_grounding:
            # A grounding asserts an equivalence about one concept; that is
            # never a class-level call.
            problems.append(
                f"{prefix}: {decision.decision} cannot be CLASS depth — grounding a "
                "concept to a term is a per-item judgement"
            )
        if not decision.curator:
            problems.append(f"{prefix}: no curator")
        if not _is_iso_date(decision.date):
            problems.append(f"{prefix}: date {decision.date!r} is not YYYY-MM-DD")
        if len(decision.notes) < MIN_NOTES_CHARS:
            problems.append(
                f"{prefix}: notes too short ({len(decision.notes)} chars); "
                "record why this decision was made, not just what it was"
            )

        if decision.decision in ("GROUND", "GROUND_AS_PARENT"):
            if not identifier.startswith("habitatmech:"):
                # A non-minted identifier is shared by every source concept that
                # resolved to it, so a GROUND keyed there would silently move
                # all of them.
                problems.append(
                    f"{prefix}: GROUND must key on a minted habitatmech: identifier "
                    "(one source concept), not a shared ontology CURIE"
                )
            if not decision.object_id:
                problems.append(f"{prefix}: {decision.decision} needs an object_id")
            if decision.grounding_status not in GROUNDING_STATUSES:
                problems.append(
                    f"{prefix}: grounding_status {decision.grounding_status!r} "
                    f"not in {sorted(GROUNDING_STATUSES)}"
                )
        elif decision.grounding_status:
            problems.append(
                f"{prefix}: grounding_status is only meaningful for GROUND "
                f"(got {decision.grounding_status!r} on {decision.decision})"
            )

        # CONFIRM_UNGROUNDED may name a nearest-broader term (attached as a
        # parent, not adopted as the identity), so object_id is allowed here —
        # but it is still label-verified below, like every other target.

        if decision.decision == "SAME_AS":
            # The target is another SOURCE CONCEPT, not an ontology term, so the
            # slice check below does not apply and would reject every valid one.
            if not decision.object_id.startswith("habitatmech:"):
                problems.append(
                    f"{prefix}: SAME_AS must name another minted habitatmech: identifier "
                    f"(got {decision.object_id!r}). To merge onto an ontology term, use GROUND"
                )
            elif decision.object_id == identifier:
                problems.append(f"{prefix}: SAME_AS names itself")
            if decision.relation != DEFAULT_RELATION:
                problems.append(
                    f"{prefix}: relation is meaningless on SAME_AS — the target is the "
                    "record's own identity, not a term placed beside it"
                )
            continue

        # The anti-hallucination check. Applies to GROUND targets and to the
        # xref an NOT_APPLICABLE decision may carry.
        if decision.object_id:
            actual = ontology_label.get(decision.object_id)
            if actual is None:
                problems.append(
                    f"{prefix}: {decision.object_id} is not in the vendored ontology "
                    "slice — it does not exist, or the ontology is not vendored "
                    "(see data/raw/ontology_terms.tsv)"
                )
            elif not decision.object_label:
                problems.append(
                    f"{prefix}: object_label is required so the target can be "
                    f"verified; {decision.object_id} is {actual!r}"
                )
            elif actual.strip().lower() != decision.object_label.strip().lower():
                problems.append(
                    f"{prefix}: {decision.object_id} is {actual!r}, "
                    f"not {decision.object_label!r} — wrong term, or wrong label"
                )
            elif decision.is_grounding and decision.object_id in (label_only or set()):
                problems.append(
                    f"{prefix}: {decision.object_id} is in the slice as a bare label with "
                    "no position in any hierarchy, so grounding onto it would produce a "
                    "record with no parents and no siblings. Vendor its ancestry (see "
                    "_reference_ancestry in the extractor) or ground somewhere placed (#46)"
                )

    if problems:
        raise DecisionError(
            "curation decisions failed validation:\n  "
            + "\n  ".join(problems[:40])
            + (f"\n  ... and {len(problems) - 40} more" if len(problems) > 40 else "")
        )


def _is_iso_date(value: str) -> bool:
    try:
        datetime.date.fromisoformat(value)
    except (ValueError, TypeError):
        return False
    return True
