"""Shared lexical keys for seeding and curation consistency checks."""

from __future__ import annotations

import re


def norm_label(text: str) -> str:
    """Lexical-matching key: lowercase, runs of non-alphanumerics to one space."""
    return re.sub(r"[^a-z0-9]+", " ", (text or "").lower()).strip()
