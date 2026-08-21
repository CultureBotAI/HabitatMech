"""Committed raw inventories have complete, byte-checked provenance."""

from __future__ import annotations

from scripts import check_provenance


def test_every_committed_raw_tsv_has_valid_provenance():
    assert not check_provenance.problems()
