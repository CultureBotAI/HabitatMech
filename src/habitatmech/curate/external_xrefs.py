"""Curated labels for xrefs to terms outside the vendored ontology slice."""

from __future__ import annotations

import csv
import datetime
import re
from dataclasses import dataclass
from pathlib import Path

__all__ = [
    "ExternalXref",
    "ExternalXrefError",
    "load_external_xrefs",
]


REQUIRED_COLUMNS = {
    "term_id",
    "term_label",
    "source_ontology",
    "source_status",
    "curator",
    "date",
    "notes",
}
CURIE = re.compile(r"^[A-Za-z][A-Za-z0-9._-]*:[A-Za-z0-9._-]+$")
MIN_NOTES_CHARS = 20


class ExternalXrefError(SystemExit):
    """A malformed or duplicate curated external xref."""


@dataclass(frozen=True)
class ExternalXref:
    term_id: str
    label: str
    source_ontology: str
    source_status: str
    curator: str
    date: str
    notes: str


def load_external_xrefs(path: Path) -> dict[str, ExternalXref]:
    """Load external xrefs that are allowed beside, never instead of, habitats."""
    if not path.exists():
        return {}
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        missing = REQUIRED_COLUMNS - set(reader.fieldnames or [])
        if missing:
            raise ExternalXrefError(f"{path}: missing columns {sorted(missing)}")

        xrefs: dict[str, ExternalXref] = {}
        for line_no, row in enumerate(reader, start=2):
            term_id = (row.get("term_id") or "").strip()
            if not term_id or term_id.startswith("#"):
                continue
            if term_id in xrefs:
                raise ExternalXrefError(f"{path}:{line_no}: duplicate xref for {term_id}")

            xref = ExternalXref(
                term_id=term_id,
                label=(row.get("term_label") or "").strip(),
                source_ontology=(row.get("source_ontology") or "").strip(),
                source_status=(row.get("source_status") or "").strip(),
                curator=(row.get("curator") or "").strip(),
                date=(row.get("date") or "").strip(),
                notes=(row.get("notes") or "").strip(),
            )
            problems = []
            if not CURIE.fullmatch(xref.term_id):
                problems.append("term_id must be a CURIE")
            if xref.term_id.startswith("habitatmech:"):
                problems.append("term_id must name an external ontology term")
            if not xref.label:
                problems.append("term_label is required")
            if not xref.source_ontology:
                problems.append("source_ontology is required")
            if not xref.source_status:
                problems.append("source_status is required")
            if not xref.curator:
                problems.append("curator is required")
            try:
                datetime.date.fromisoformat(xref.date)
            except ValueError:
                problems.append(f"date {xref.date!r} is not YYYY-MM-DD")
            if len(xref.notes) < MIN_NOTES_CHARS:
                problems.append(
                    f"notes too short ({len(xref.notes)} chars); record why this "
                    "external term is retained"
                )
            if problems:
                raise ExternalXrefError(f"{path}:{line_no}: " + "; ".join(problems))
            xrefs[term_id] = xref
    return xrefs
