"""The write gate, and the round-trip property that makes bulk edits reviewable.

If re-emitting a record through the helper is not byte-identical, then any
script that touches one field reformats the whole file, and the real change is
buried in reflow churn. That has bitten the sibling Mech repos before, so it is
enforced over the corpus rather than assumed.
"""

from __future__ import annotations

import pytest
import yaml

from habitatmech.validation.write_validated import (
    ValidationFailedError,
    emit_habitat_yaml,
    validate_habitat,
    write_validated_habitat,
)

MINIMAL = {
    "identifier": "ENVO:00000019",
    "label": "saline lake",
    "habitat_category": "AQUATIC",
    "grounding_status": "EXACT",
    "mapping_status": "SEEDED",
    "source_attestations": [{"source": "PREGO", "source_label": "saline lake"}],
}


def test_valid_record_passes():
    assert validate_habitat(MINIMAL) == []


def test_missing_required_field_is_rejected():
    doc = {k: v for k, v in MINIMAL.items() if k != "label"}
    assert validate_habitat(doc)


def test_unknown_field_is_rejected():
    """Closed-mode validation is the point of this helper. In LinkML's default
    open mode a typo'd field name is silently accepted and the data is lost."""
    doc = dict(MINIMAL, habitat_catgory="AQUATIC")
    assert validate_habitat(doc)


def test_bad_enum_value_is_rejected():
    assert validate_habitat(dict(MINIMAL, habitat_category="SWAMPY"))


def test_bad_identifier_pattern_is_rejected():
    assert validate_habitat(dict(MINIMAL, identifier="not a curie"))


def test_causal_edge_without_evidence_is_rejected():
    """Mechanism claims are curator-asserted and nothing upstream vouches for
    them, so the schema requires edge-level evidence."""
    doc = dict(
        MINIMAL,
        causal_graphs=[
            {
                "graph_id": "g1",
                "nodes": [
                    {"node_id": "a", "label": "salinity", "node_type": "ENVIRONMENTAL_PARAMETER"},
                    {"node_id": "b", "label": "compatible solutes", "node_type": "CHEMICAL"},
                ],
                "edges": [{"subject": "a", "predicate": "selects for", "object": "b"}],
            }
        ],
    )
    assert validate_habitat(doc)


def test_invalid_record_is_not_written(tmp_path):
    path = tmp_path / "bad.yaml"
    with pytest.raises(ValidationFailedError):
        write_validated_habitat({"identifier": "ENVO:1"}, path)
    assert not path.exists(), "an invalid record must not reach disk"


def test_valid_record_is_written(tmp_path):
    path = tmp_path / "nested" / "good.yaml"
    write_validated_habitat(dict(MINIMAL), path)
    assert path.exists()
    assert yaml.safe_load(path.read_text())["identifier"] == MINIMAL["identifier"]


def test_emit_is_stable_across_calls():
    assert emit_habitat_yaml(MINIMAL) == emit_habitat_yaml(MINIMAL)


def test_every_seeded_record_round_trips_byte_identically(records):
    """Re-emitting the corpus through the helper must change nothing. When this
    fails, a bulk script's diff stops being reviewable."""
    drifted = []
    for path, doc in records:
        if emit_habitat_yaml(doc) != path.read_text(encoding="utf-8"):
            drifted.append(str(path))
    assert not drifted, (
        f"{len(drifted)} record(s) are not what emit_habitat_yaml would write, "
        f"e.g. {drifted[:5]}. Reformat them through the helper rather than "
        "loosening this test."
    )
