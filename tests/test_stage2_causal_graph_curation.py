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


def test_cycle2_stage2_ten_new_causal_graph_overlays_are_present_and_grounded():
    expected = {
        "root": (
            "PO:0009005",
            "root_microbiome_two_step_selection",
            {"PMID:22859206", "PMID:22859207", "PMID:23373698"},
        ),
        "rhizosphere": (
            "ENVO:00005801",
            "rhizosphere_exudate_disease_suppressive_assembly",
            {"PMID:16669762", "PMID:29050989", "PMID:24056930", "PMID:21551032"},
        ),
        "volcano": (
            "ENVO:00000247",
            "volcano_geothermal_chemolithoautotrophic_colonization",
            {"PMID:15970992", "PMID:23720654", "PMID:15184674"},
        ),
        "endolithic_environment": (
            "ENVO:01000303",
            "endolithic_rock_pore_uv_desiccation_refuge",
            {"PMID:17506683", "PMID:39228380", "PMID:19850879"},
        ),
        "petroleum": (
            "ENVO:00002984",
            "petroleum_anaerobic_hydrocarbon_methanogenic_souring",
            {"PMID:25104386", "PMID:14628064", "PMID:18075503"},
        ),
        "skin_environment": (
            "ENVO:2100003",
            "skin_lipid_acid_mantle_commensal_colonization",
            {"PMID:29332945", "PMID:42267822", "PMID:21407241", "PMID:26733066"},
        ),
        "mouth_environment": (
            "ENVO:08000002",
            "mouth_salivary_flow_multispecies_biofilm_succession",
            {"PMID:20514044", "PMID:30301974"},
        ),
        "vagina": (
            "UBERON:0000996",
            "vagina_glycogen_amylase_lactobacillus_acidification",
            {"PMID:24737800", "PMID:20534435", "PMID:28435139", "PMID:26171967"},
        ),
        "nasopharynx": (
            "UBERON:0001728",
            "nasopharynx_corynebacterium_gatekeeper_colonization_resistance",
            {"PMID:28316330", "PMID:26733066", "PMID:39705185"},
        ),
        "fecal_environment": (
            "ENVO:01001029",
            "fecal_complex_polysaccharide_fermentation_and_methanogenesis",
            {"PMID:22572875", "PMID:22343308", "PMID:21357460", "PMID:22859731", "PMID:31162794"},
        ),
    }
    for slug, (expected_id, expected_graph_id, expected_refs) in expected.items():
        overlay_path = CAUSAL_GRAPHS_DIR / f"{slug}.yaml"
        assert overlay_path.exists(), f"{slug}.yaml missing"
        doc = yaml.safe_load(overlay_path.read_text(encoding="utf-8"))
        assert doc["identifier"] == expected_id
        graphs = doc["causal_graphs"]
        assert len(graphs) == 1
        graph = graphs[0]
        assert graph["graph_id"] == expected_graph_id
        nodes = {n["node_id"]: n for n in graph["nodes"]}
        assert nodes[slug]["node_type"] == "HABITAT"
        assert nodes[slug]["grounding"] == expected_id
        refs = {
            ev["reference"]
            for edge in graph["edges"]
            for ev in edge.get("evidence", [])
        }
        assert refs == expected_refs
        assert doc["curation_history"][-1]["action"] == "ADD_CAUSAL_GRAPH"

