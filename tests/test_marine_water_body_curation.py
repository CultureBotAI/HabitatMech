from copy import deepcopy
from pathlib import Path

import yaml

from habitatmech.text_map_inputs import semantic_text

ROOT = Path(__file__).resolve().parents[1]


def test_marine_carbon_pump_evidence_and_conditional_scope():
    overlay = yaml.safe_load((ROOT / "curation/causal_graphs/marine_water_body.yaml").read_text())
    graph = overlay["causal_graphs"][0]
    edges = {edge["edge_id"]: edge for edge in graph["edges"]}
    assert len(graph["nodes"]) == len(edges) == 15
    assert "not a universal" in graph["description"]
    assert "not a complete carbon budget" in graph["description"]
    particle = edges["sinking_particles_select_particle_bacteria"]
    assert particle["predicate"] == "supports"
    assert particle["evidence"][0]["reference"] == "DOI:10.1038/ngeo1921"
    assert "Aerobic" in edges["remineralization_consumes_oxygen"]["description"]
    for edge in edges.values():
        assert edge["evidence"]
        for evidence in edge["evidence"]:
            assert evidence["reference"] != "PMID:23139690"
            assert evidence["notes"]
    # The superseded citation remains in history, not in active evidence.
    assert "PMID:23139690" in overlay["curation_history"][0]["changes"]
    assert overlay["curation_history"][-1]["action"] == "UPDATE_CAUSAL_GRAPH"


def test_graph_and_audit_only_changes_do_not_change_semantic_map_text():
    record = yaml.safe_load((ROOT / "data/habitats/aquatic/marine_water_body.yaml").read_text())
    context = {parent: parent for parent in record["parent_habitats"]}
    changed = deepcopy(record)
    changed["causal_graphs"] = []
    changed["curation_history"] = []
    assert semantic_text(changed, context) == semantic_text(record, context)
