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
    # No grounding change; the curator checked the record as the seeder built it.
    "REVIEW",
}

GROUNDING_STATUSES = {"EXACT", "BROAD", "NARROW", "CLOSE"}

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

    @property
    def is_grounding(self) -> bool:
        return self.decision == "GROUND"


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
            )
    return decisions


def validate_decisions(
    decisions: dict[str, Decision],
    ontology_label: dict[str, str],
    *,
    path: Path | None = None,
) -> None:
    """Fail loudly on any decision that is malformed or cannot be verified.

    ``ontology_label`` maps term id -> label for the vendored slice. A GROUND
    target absent from it is either invented or outside what the repo vendors;
    either way the seeder must not act on it silently.
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
        if not decision.curator:
            problems.append(f"{prefix}: no curator")
        if not _is_iso_date(decision.date):
            problems.append(f"{prefix}: date {decision.date!r} is not YYYY-MM-DD")
        if len(decision.notes) < MIN_NOTES_CHARS:
            problems.append(
                f"{prefix}: notes too short ({len(decision.notes)} chars); "
                "record why this decision was made, not just what it was"
            )

        if decision.decision == "GROUND":
            if not identifier.startswith("habitatmech:"):
                # A non-minted identifier is shared by every source concept that
                # resolved to it, so a GROUND keyed there would silently move
                # all of them.
                problems.append(
                    f"{prefix}: GROUND must key on a minted habitatmech: identifier "
                    "(one source concept), not a shared ontology CURIE"
                )
            if not decision.object_id:
                problems.append(f"{prefix}: GROUND needs an object_id")
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
