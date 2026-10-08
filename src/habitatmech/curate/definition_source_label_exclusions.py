"""Guarded opt-outs from retaining a renamed native term's source label."""

from __future__ import annotations

import csv
import datetime
import re
from dataclasses import dataclass
from pathlib import Path

from habitatmech.curate.definitions import CuratedDefinition
from habitatmech.labels import norm_label


class DefinitionSourceLabelExclusionError(SystemExit):
    """Invalid or stale alias exclusions stop regeneration."""


@dataclass(frozen=True)
class DefinitionSourceLabelExclusion:
    identifier: str
    source_label: str
    requested_label: str
    curator: str
    date: str
    notes: str


def load_definition_source_label_exclusions(
    path: Path,
) -> dict[str, DefinitionSourceLabelExclusion]:
    columns = list(DefinitionSourceLabelExclusion.__dataclass_fields__)
    exclusions = {}
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        if reader.fieldnames != columns:
            raise DefinitionSourceLabelExclusionError(f"{path}: expected columns {columns}")
        for line_no, row in enumerate(reader, 2):
            prefix = f"{path}:{line_no}"
            if None in row or any(not (row.get(key) or "").strip() for key in columns):
                raise DefinitionSourceLabelExclusionError(f"{prefix}: incomplete or extra fields")
            item = DefinitionSourceLabelExclusion(**{key: row[key].strip() for key in columns})
            if not re.fullmatch(r"habitatmech:[A-Za-z0-9._-]+", item.identifier):
                raise DefinitionSourceLabelExclusionError(f"{prefix}: expected a native identifier")
            try:
                if datetime.date.fromisoformat(item.date).isoformat() != item.date:
                    raise ValueError
            except ValueError:
                raise DefinitionSourceLabelExclusionError(
                    f"{prefix}: date must be YYYY-MM-DD"
                ) from None
            if len(item.notes) < 20:
                raise DefinitionSourceLabelExclusionError(f"{prefix}: explain the alias exclusion")
            if item.identifier in exclusions:
                raise DefinitionSourceLabelExclusionError(f"{prefix}: duplicate exclusion")
            exclusions[item.identifier] = item
    return exclusions


def validate_definition_source_label_exclusions(
    exclusions: dict[str, DefinitionSourceLabelExclusion],
    definitions: dict[str, CuratedDefinition],
    concepts: dict[str, object],
) -> None:
    for identifier, item in exclusions.items():
        definition, concept = definitions.get(identifier), concepts.get(identifier)
        problem = ""
        if definition is None or concept is None:
            problem = "no matching generated concept and authored definition"
        elif item.source_label != getattr(concept, "label", None):
            problem = "stale source_label"
        elif item.requested_label != definition.label:
            problem = "stale requested_label"
        elif norm_label(item.source_label) == norm_label(item.requested_label):
            problem = "source label is not renamed"
        elif any(norm_label(s) == norm_label(item.source_label) for s in definition.exact_synonyms):
            problem = "excluded source label is an authored exact synonym"
        if problem:
            raise DefinitionSourceLabelExclusionError(f"{identifier}: {problem}")
