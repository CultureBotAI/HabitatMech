"""Curated definitions for HabitatMech-native habitat terms.

The generated corpus cannot be curated by editing ``data/habitats`` directly.
Definitions for minted terms therefore live in ``curation/term_requests.tsv``
and are applied by the seeder just like decisions.  The historical filename is
retained because the table is also emitted as an OBO ROBOT template, but these
rows are HabitatMech's own term definitions rather than untrusted suggestions.
"""

from __future__ import annotations

import csv
import datetime
from dataclasses import dataclass
from pathlib import Path

__all__ = [
    "CuratedDefinition",
    "DefinitionError",
    "load_curated_definitions",
    "validate_curated_definitions",
]


REQUIRED_COLUMNS = {
    "identifier",
    "requested_label",
    "parent_class",
    "parent_label",
    "definition",
    "exact_synonym",
    "curator",
    "date",
    "notes",
}

PARENT_MODES = {"ADD", "REPLACE"}
DEFAULT_PARENT_MODE = "ADD"


class DefinitionError(SystemExit):
    """A malformed or unverifiable curated definition."""


@dataclass(frozen=True)
class CuratedDefinition:
    identifier: str
    label: str
    parent_class: str
    parent_label: str
    definition: str
    exact_synonyms: tuple[str, ...]
    curator: str
    date: str
    notes: str
    # ADD preserves source-derived hierarchy and supplies an ontology genus.
    # REPLACE is an explicit curator ruling that the inherited parents are
    # false for this concept, so only the authored genus should remain.
    parent_mode: str = DEFAULT_PARENT_MODE


def load_curated_definitions(path: Path) -> dict[str, CuratedDefinition]:
    """Load the definition table, rejecting incomplete or duplicate rows."""
    if not path.exists():
        return {}
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        missing = REQUIRED_COLUMNS - set(reader.fieldnames or [])
        if missing:
            raise DefinitionError(f"{path}: missing columns {sorted(missing)}")

        definitions: dict[str, CuratedDefinition] = {}
        labels: dict[str, tuple[str, int]] = {}
        for line_no, row in enumerate(reader, start=2):
            identifier = (row.get("identifier") or "").strip()
            if not identifier or identifier.startswith("#"):
                continue
            if identifier in definitions:
                raise DefinitionError(
                    f"{path}:{line_no}: duplicate definition for {identifier}"
                )
            definition = CuratedDefinition(
                identifier=identifier,
                label=(row.get("requested_label") or "").strip(),
                parent_class=(row.get("parent_class") or "").strip(),
                parent_label=(row.get("parent_label") or "").strip(),
                definition=(row.get("definition") or "").strip(),
                exact_synonyms=tuple(
                    synonym.strip()
                    for synonym in (row.get("exact_synonym") or "").split("|")
                    if synonym.strip()
                ),
                curator=(row.get("curator") or "").strip(),
                date=(row.get("date") or "").strip(),
                notes=(row.get("notes") or "").strip(),
                parent_mode=(row.get("parent_mode") or DEFAULT_PARENT_MODE).strip().upper()
                or DEFAULT_PARENT_MODE,
            )
            problems = []
            if not definition.label:
                problems.append("requested_label is required")
            if not definition.parent_class or not definition.parent_label:
                problems.append("parent_class and parent_label are required")
            if not definition.definition.endswith("."):
                problems.append("definition must be a sentence ending in '.'")
            if not definition.curator:
                problems.append("curator is required")
            try:
                datetime.date.fromisoformat(definition.date)
            except ValueError:
                problems.append(f"date {definition.date!r} is not YYYY-MM-DD")
            if not definition.notes:
                problems.append("notes are required")
            if definition.parent_mode not in PARENT_MODES:
                problems.append(
                    f"parent_mode {definition.parent_mode!r} is not one of "
                    f"{sorted(PARENT_MODES)}"
                )
            if problems:
                raise DefinitionError(
                    f"{path}:{line_no}: " + "; ".join(problems)
                )
            normalized_label = " ".join(definition.label.split()).casefold()
            previous = labels.get(normalized_label)
            if previous is not None:
                previous_identifier, previous_line = previous
                raise DefinitionError(
                    f"{path}:{line_no}: requested_label {definition.label!r} is "
                    f"already authored for {previous_identifier} on line "
                    f"{previous_line}; merge duplicate concepts before defining them"
                )
            labels[normalized_label] = (identifier, line_no)
            definitions[identifier] = definition
    return definitions


def validate_curated_definitions(
    definitions: dict[str, CuratedDefinition],
    concepts: dict[str, object],
    ontology_labels: dict[str, str],
    *,
    path: Path,
) -> None:
    """Verify that every definition describes a real minted ungrounded term."""
    problems = []
    for identifier, row in definitions.items():
        concept = concepts.get(identifier)
        prefix = f"{path.name}: {identifier}"
        if concept is None:
            problems.append(f"{prefix}: no such record is generated")
            continue
        if not identifier.startswith("habitatmech:"):
            problems.append(f"{prefix}: ontology-owned terms cannot be redefined here")
        if getattr(concept, "grounding_status", None) != "UNGROUNDED":
            problems.append(
                f"{prefix}: record is {getattr(concept, 'grounding_status', None)}, "
                "not UNGROUNDED"
            )
        actual_parent = ontology_labels.get(row.parent_class)
        if actual_parent is None:
            problems.append(
                f"{prefix}: parent {row.parent_class} is absent from the vendored slice"
            )
        elif actual_parent.casefold() != row.parent_label.casefold():
            problems.append(
                f"{prefix}: parent_label says {row.parent_label!r} but "
                f"{row.parent_class} is {actual_parent!r}"
            )
    if problems:
        raise DefinitionError(
            "curated definitions cannot be applied:\n  " + "\n  ".join(problems)
        )
