from __future__ import annotations

import pytest
import yaml

from habitatmech.curate.causal_graphs import (
    CausalGraphCurationError,
    load_causal_graph_curation_files,
    validate_causal_graph_curations,
)
from scripts import validate_causal_graph_curations as validate_causal_graphs_cli


def _overlay(identifier: str = "ENVO:00002012") -> dict:
    return {
        "identifier": identifier,
        "causal_graphs": [
            {
                "graph_id": "g1",
                "nodes": [
                    {
                        "node_id": "salinity",
                        "label": "salinity",
                        "node_type": "ENVIRONMENTAL_PARAMETER",
                    },
                    {
                        "node_id": "compatible_solutes",
                        "label": "compatible solutes",
                        "node_type": "CHEMICAL",
                    },
                ],
                "edges": [
                    {
                        "edge_id": "e1",
                        "subject": "salinity",
                        "predicate": "selects for",
                        "object": "compatible_solutes",
                        "evidence": [
                            {
                                "reference": "PMID:29529204",
                                "snippet": "compatible solutes",
                            }
                        ],
                    }
                ],
            }
        ],
        "curation_history": [
            {
                "timestamp": "2026-09-04T00:00:00Z",
                "curator": "test",
                "action": "ADD_CAUSAL_GRAPH",
            }
        ],
    }


def _write(tmp_path, doc: dict, name: str = "overlay.yaml"):
    path = tmp_path / name
    path.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")
    return path


def test_valid_causal_graph_overlay_loads(tmp_path):
    path = _write(tmp_path, _overlay())
    curations = load_causal_graph_curation_files([path])

    assert curations["ENVO:00002012"].causal_graphs[0]["graph_id"] == "g1"


def test_overlay_schema_is_closed(tmp_path):
    doc = _overlay()
    doc["unknown"] = "nope"

    with pytest.raises(CausalGraphCurationError, match="LinkML validation"):
        load_causal_graph_curation_files([_write(tmp_path, doc)])


def test_dangling_causal_graph_edge_is_rejected(tmp_path):
    doc = _overlay()
    doc["causal_graphs"][0]["edges"][0]["object"] = "missing"

    with pytest.raises(CausalGraphCurationError, match="undeclared object 'missing'"):
        load_causal_graph_curation_files([_write(tmp_path, doc)])


def test_causal_graph_edges_must_have_evidence(tmp_path):
    doc = _overlay()
    doc["causal_graphs"][0]["edges"][0]["evidence"] = []

    with pytest.raises(CausalGraphCurationError, match="must include evidence"):
        load_causal_graph_curation_files([_write(tmp_path, doc)])


def test_duplicate_overlay_identifier_is_rejected(tmp_path):
    first = _write(tmp_path, _overlay(), "one.yaml")
    second = _write(tmp_path, _overlay(), "two.yaml")

    with pytest.raises(CausalGraphCurationError, match="duplicate"):
        load_causal_graph_curation_files([first, second])


def test_causal_graph_overlay_must_target_a_generated_record(tmp_path):
    path = _write(tmp_path, _overlay("ENVO:99999999"))
    curations = load_causal_graph_curation_files([path])

    with pytest.raises(CausalGraphCurationError, match="missing HabitatRecord"):
        validate_causal_graph_curations(curations, {"ENVO:00002012": object()}, path=tmp_path)


def test_validate_causal_graph_cli_uses_requested_root(tmp_path, monkeypatch):
    root = tmp_path / "overlays"
    root.mkdir()
    _write(root, _overlay())
    seen = {}

    def fake_build_corpus(*, causal_graphs_root):
        seen["causal_graphs_root"] = causal_graphs_root

    monkeypatch.setattr(validate_causal_graphs_cli, "build_corpus", fake_build_corpus)

    assert validate_causal_graphs_cli.main(["--root", str(root)]) == 0
    assert seen == {"causal_graphs_root": root}
