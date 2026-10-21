from __future__ import annotations

from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
CAUSAL_GRAPHS_DIR = REPO_ROOT / "curation" / "causal_graphs"


def test_groundwater_causal_graph_overlay_is_present_and_grounded():
    overlay_path = CAUSAL_GRAPHS_DIR / "groundwater.yaml"
    assert overlay_path.exists()
    doc = yaml.safe_load(overlay_path.read_text(encoding="utf-8"))
    assert doc["identifier"] == "ENVO:01001004"
    graphs = doc["causal_graphs"]
    assert len(graphs) == 1
    graph = graphs[0]
    assert graph["graph_id"] == "groundwater_subsurface_fermentation_handoffs"
    nodes = {n["node_id"]: n for n in graph["nodes"]}
    assert nodes["groundwater"]["node_type"] == "HABITAT"
    assert nodes["groundwater"]["grounding"] == "ENVO:01001004"
    assert nodes["ultra_small_candidate_phyla_bacteria"]["node_type"] == "COMMUNITY"
    refs = {
        ev["reference"]
        for edge in graph["edges"]
        for ev in edge.get("evidence", [])
    }
    assert refs == {"PMID:26121419", "PMID:23019650", "PMID:27779183"}


def test_forested_area_stursova_edges_use_fems_doi_not_schneider_pmid():
    overlay_path = CAUSAL_GRAPHS_DIR / "forested_area.yaml"
    doc = yaml.safe_load(overlay_path.read_text(encoding="utf-8"))
    edges = {
        edge["edge_id"]: edge
        for edge in doc["causal_graphs"][0]["edges"]
    }
    for edge_id in (
        "forest_litter_contains_lignocellulose",
        "lignocellulose_selects_saprotrophs",
        "forest_bacteria_contribute_to_decomposition",
    ):
        refs = [ev["reference"] for ev in edges[edge_id]["evidence"]]
        assert "PMID:22402400" not in refs
        assert "DOI:10.1111/j.1574-6941.2012.01343.x" in refs


def test_all_18_previously_single_event_overlays_record_revision_history():
    revised_slugs = [
        "agricultural_soil",
        "aquatic_biome",
        "forest_soil",
        "forested_area",
        "fungi_associated_environment",
        "grassland_soil",
        "intestine_environment",
        "leaf",
        "milk",
        "peat_soil",
        "plant_associated_environment",
        "plant_litter",
        "root_nodule",
        "sediment",
        "sludge",
        "soil",
        "terrestrial_biome",
        "waste_water",
    ]
    for slug in revised_slugs:
        doc = yaml.safe_load((CAUSAL_GRAPHS_DIR / f"{slug}.yaml").read_text(encoding="utf-8"))
        history = doc.get("curation_history", [])
        assert len(history) >= 2, f"{slug}.yaml missing revision history"
        assert history[-1]["action"] == "REVISE_CAUSAL_GRAPH"
