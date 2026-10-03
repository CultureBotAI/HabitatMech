"""Curated exclusions of GOLD context edges, not of independent is-a evidence."""

from __future__ import annotations

import csv
import datetime
import re
from dataclasses import dataclass
from pathlib import Path


class GoldParentExclusionError(SystemExit):
    """An invalid or stale source-parent exclusion must stop regeneration."""


@dataclass(frozen=True)
class GoldParentExclusion:
    identifier: str
    source_path: str
    parent_id: str
    curator: str
    date: str
    notes: str


def load_gold_parent_exclusions(path: Path) -> dict[str, GoldParentExclusion]:
    """Read a required table, rejecting malformed rows rather than losing intent."""
    columns = list(GoldParentExclusion.__dataclass_fields__)
    exclusions = {}
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        if reader.fieldnames != columns:
            raise GoldParentExclusionError(f"{path}: expected columns {columns}")
        for line_no, row in enumerate(reader, 2):
            if None in row or any(not (row.get(key) or "").strip() for key in columns):
                raise GoldParentExclusionError(f"{path}:{line_no}: incomplete or extra fields")
            exclusion = GoldParentExclusion(**{key: row[key].strip() for key in columns})
            if not re.fullmatch(r"habitatmech:GOLD\.[0-9a-f]{10}", exclusion.identifier):
                raise GoldParentExclusionError(f"{path}:{line_no}: expected a GOLD source identifier")
            if not re.fullmatch(r"[A-Za-z][A-Za-z0-9._-]*:[A-Za-z0-9._-]+", exclusion.parent_id):
                raise GoldParentExclusionError(f"{path}:{line_no}: parent_id must be a CURIE")
            try:
                parsed_date = datetime.date.fromisoformat(exclusion.date)
                if parsed_date.isoformat() != exclusion.date:
                    raise ValueError
            except ValueError:
                raise GoldParentExclusionError(f"{path}:{line_no}: date must be YYYY-MM-DD") from None
            if len(exclusion.notes) < 20:
                raise GoldParentExclusionError(f"{path}:{line_no}: explain why the parent is not broader")
            if exclusion.identifier in exclusions:
                raise GoldParentExclusionError(
                    f"{path}:{line_no}: duplicate exclusion {exclusion.identifier}"
                )
            exclusions[exclusion.identifier] = exclusion
    return exclusions
