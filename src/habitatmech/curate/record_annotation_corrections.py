"""Reviewed, record-scoped corrections to imported annotation values."""

from __future__ import annotations

import csv
import datetime
import re
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from habitatmech.seed import Concept


class RecordAnnotationCorrectionError(SystemExit):
    """Malformed or stale annotation corrections stop regeneration."""


@dataclass(frozen=True)
class RecordAnnotationCorrection:
    correction_id: str
    identifier: str
    field: str
    item: str
    source: str
    expected: str
    replacement: str
    curator: str
    date: str
    evidence: str
    notes: str


def load_record_annotation_corrections(path: Path) -> list[RecordAnnotationCorrection]:
    columns = list(RecordAnnotationCorrection.__dataclass_fields__)
    corrections, ids, claims = [], set(), set()
    scopes = {"EXACT_SYNONYM", "NARROW_SYNONYM", "BROAD_SYNONYM", "RELATED_SYNONYM"}
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames != columns:
            raise RecordAnnotationCorrectionError(f"{path}: expected columns {columns}")
        for line, row in enumerate(reader, 2):
            prefix = f"{path}:{line}"
            if None in row or any(not (row.get(key) or "").strip() for key in columns):
                raise RecordAnnotationCorrectionError(f"{prefix}: incomplete or extra fields")
            item = RecordAnnotationCorrection(**{key: row[key].strip() for key in columns})
            if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", item.correction_id):
                raise RecordAnnotationCorrectionError(f"{prefix}: invalid correction_id")
            if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*:[A-Za-z0-9._-]+", item.identifier):
                raise RecordAnnotationCorrectionError(f"{prefix}: invalid record identifier")
            if item.field == "synonym_type":
                if item.source == "habitatmech" or item.source != item.identifier.split(":")[0]:
                    raise RecordAnnotationCorrectionError(f"{prefix}: expected ontology source")
                if item.expected not in scopes or item.replacement not in scopes:
                    raise RecordAnnotationCorrectionError(f"{prefix}: invalid synonym scope")
            elif item.field == "taxon_label":
                if not re.fullmatch(r"NCBITaxon:[0-9]+", item.item):
                    raise RecordAnnotationCorrectionError(f"{prefix}: invalid taxon identifier")
                if item.source not in {"BACDIVE", "PREGO", "MADIN"}:
                    raise RecordAnnotationCorrectionError(f"{prefix}: invalid taxon source")
            else:
                raise RecordAnnotationCorrectionError(f"{prefix}: unsupported annotation field")
            if item.expected == item.replacement:
                raise RecordAnnotationCorrectionError(f"{prefix}: no-op correction")
            try:
                if datetime.date.fromisoformat(item.date).isoformat() != item.date:
                    raise ValueError
            except ValueError:
                raise RecordAnnotationCorrectionError(f"{prefix}: date must be YYYY-MM-DD") from None
            if not item.evidence.startswith("https://") or len(item.notes) < 20:
                raise RecordAnnotationCorrectionError(f"{prefix}: evidence and rationale required")
            claim = (item.identifier, item.field, item.item)
            if item.correction_id in ids or claim in claims:
                raise RecordAnnotationCorrectionError(f"{prefix}: duplicate correction or claim")
            ids.add(item.correction_id)
            claims.add(claim)
            corrections.append(item)
    return corrections


def apply_record_annotation_corrections(
    concepts: dict[str, Concept], corrections: list[RecordAnnotationCorrection],
) -> None:
    # Validate every precondition before changing any concept.
    for item in corrections:
        concept = concepts.get(item.identifier)
        problem = ""
        if concept is None:
            problem = "unmatched record"
        elif item.field == "synonym_type":
            matches = {key: source for key, source in concept.synonyms.items() if key[0] == item.item}
            if matches != {(item.item, item.expected): item.source}:
                problem = "stale or conflicting synonym annotation"
        elif item.field == "taxon_label":
            taxon = concept.taxa.get(item.item, {})
            if taxon.get("source") != item.source or taxon.get("taxon_label") != item.expected:
                problem = "stale taxon label or source"
        else:
            problem = "unsupported annotation field"
        if problem:
            raise RecordAnnotationCorrectionError(f"{item.correction_id}: {problem}")
    for item in corrections:
        concept = concepts[item.identifier]
        if item.field == "synonym_type":
            del concept.synonyms[(item.item, item.expected)]
            concept.synonyms[(item.item, item.replacement)] = item.source
        else:
            concept.taxa[item.item]["taxon_label"] = item.replacement
        concept.annotation_corrections_applied.append(item)
