"""Keep the reviewed building graph's sampling and evidence boundaries explicit."""

import yaml

from habitatmech.curate.causal_graphs import load_causal_graph_curation_files
from habitatmech.text_map_inputs import semantic_text


def _curation(repo_root):
    path = repo_root / "curation/causal_graphs/building.yaml"
    return load_causal_graph_curation_files([path])["ENVO:00000073"]


def test_building_graph_keeps_air_and_surface_evidence_separate(repo_root):
    graph = _curation(repo_root).causal_graphs[0]
    edges = {edge["edge_id"]: edge for edge in graph["edges"]}
    surface = edges["building_contains_indoor_surfaces"]
    assert {item["reference"] for item in surface["evidence"]} == {"PMID:25398865"}
    air = edges["ventilation_introduces_outdoor_air"]
    assert (air["subject"], air["object"]) == (
        "ventilation_strategy", "outdoor_air_inoculation"
    )
    assert {item["reference"] for item in air["evidence"]} == {"PMID:23621155"}
    assert not any(
        edge["subject"] == "outdoor_air_inoculation"
        and edge["object"] in {"indoor_surfaces", "surface_recolonization"}
        for edge in graph["edges"]
    )


def test_building_graph_does_not_promote_populations_or_hypotheses(repo_root):
    graph = _curation(repo_root).causal_graphs[0]
    nodes = {node["node_id"]: node for node in graph["nodes"]}
    assert not {
        "human_associated_bacteria", "viable_surface_reservoir", "indoor_surface_microbiome"
    } & nodes.keys()
    assert nodes["surface_recolonization"]["node_type"] == "COMMUNITY_PROCESS"
    assert nodes["cleaning_disturbance"]["node_type"] == "EXPERIMENTAL_FACTOR"
    assert nodes["indoor_surfaces"]["node_type"] == "HABITAT"
    edges = {edge["edge_id"]: edge for edge in graph["edges"]}
    assert not {
        "surface_materials_filter_deposited_cells",
        "room_connectivity_controls_dispersal",
        "viable_reservoir_reseeds_surface_microbiome",
        "low_organic_matter_filters_surface_reservoir",
        "desiccation_filters_surface_reservoir",
    } & edges.keys()
    assert edges["cleaning_precedes_surface_succession"]["predicate"] == "precedes observed"
    assert edges["human_occupancy_supports_occupant_source_inference"]["predicate"] == (
        "supports source inference for"
    )


def test_building_evidence_has_inspected_locators_and_preserves_history(repo_root):
    curation = _curation(repo_root)
    for edge in curation.causal_graphs[0]["edges"]:
        for item in edge["evidence"]:
            assert item["reference"] in {"PMID:25170151", "PMID:23621155", "PMID:25398865"}
            assert len(item["snippet"].split()) >= 4
            assert "Abstract" in item["notes"] or "Materials and Methods" in item["notes"]
    assert curation.curation_history[0]["action"] == "ADD_CAUSAL_GRAPH"
    assert curation.curation_history[0]["timestamp"] == "2026-09-04T00:00:00Z"
    assert curation.curation_history[-1]["action"] == "REVISE_CAUSAL_GRAPH"


def test_building_generated_graph_matches_overlay_without_changing_map_text(repo_root):
    record = yaml.safe_load(
        (repo_root / "data/habitats/engineered/building.yaml").read_text()
    )
    curation = _curation(repo_root)
    assert record["causal_graphs"] == list(curation.causal_graphs)
    assert all(event in record["curation_history"] for event in curation.curation_history)
    without_graph = {
        key: value for key, value in record.items()
        if key not in {"causal_graphs", "curation_history"}
    }
    assert semantic_text(record) == semantic_text(without_graph)
