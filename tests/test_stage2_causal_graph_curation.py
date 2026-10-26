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
        assert doc["curation_history"][0]["action"] == "ADD_CAUSAL_GRAPH"
        for edge in graph["edges"]:
            for ev in edge.get("evidence", []):
                snippet = ev.get("snippet", "")
                assert "<i>" not in snippet and "</i>" not in snippet
                assert "\u00a0" not in snippet

    volcano_nodes = {
        n["node_id"]: n
        for n in yaml.safe_load((CAUSAL_GRAPHS_DIR / "volcano.yaml").read_text(encoding="utf-8"))[
            "causal_graphs"
        ][0]["nodes"]
    }
    assert volcano_nodes["hyperthermophilic_and_thermoacidophilic_archaea"]["node_type"] == "COMMUNITY"
    assert volcano_nodes["acidotolerant_thermophilic_anaerobic_bacteria"]["node_type"] == "COMMUNITY"

    fecal_nodes = {
        n["node_id"]: n
        for n in yaml.safe_load(
            (CAUSAL_GRAPHS_DIR / "fecal_environment.yaml").read_text(encoding="utf-8")
        )["causal_graphs"][0]["nodes"]
    }
    assert fecal_nodes["keystone_amylolytic_and_cellulolytic_degraders"]["node_type"] == "COMMUNITY"

    vagina_nodes = {
        n["node_id"]: n
        for n in yaml.safe_load((CAUSAL_GRAPHS_DIR / "vagina.yaml").read_text(encoding="utf-8"))[
            "causal_graphs"
        ][0]["nodes"]
    }
    assert (
        vagina_nodes["epithelial_glycogen_and_mucosal_alpha_amylase"]["node_type"]
        == "BIOLOGICAL_PROCESS"
    )

    nasopharynx_graph = yaml.safe_load(
        (CAUSAL_GRAPHS_DIR / "nasopharynx.yaml").read_text(encoding="utf-8")
    )["causal_graphs"][0]
    nasopharynx_nodes = {n["node_id"]: n for n in nasopharynx_graph["nodes"]}
    assert (
        nasopharynx_nodes["upper_airway_mucosal_and_triacylglycerol_surface"]["node_type"]
        == "ENVIRONMENTAL_FACTOR"
    )
    assert nasopharynx_nodes["commensal_airway_corynebacterium_guild"]["node_type"] == "COMMUNITY"
    nasopharynx_edges = {e["edge_id"]: e for e in nasopharynx_graph["edges"]}
    supply_refs = {
        ev["reference"]
        for ev in nasopharynx_edges[
            "nasopharynx_provides_upper_airway_mucosal_and_triacylglycerol_surface"
        ]["evidence"]
    }
    assert supply_refs == {"PMID:28316330", "PMID:26733066"}


def test_cycle2_stage3_protein_examples_and_source_limited_notes_are_present():
    habitat_paths = {
        "fresh_water": REPO_ROOT / "data" / "habitats" / "aquatic" / "fresh_water.yaml",
        "root_nodule": REPO_ROOT / "data" / "habitats" / "host_associated" / "root_nodule__0f1c7944.yaml",
        "sea_water": REPO_ROOT / "data" / "habitats" / "aquatic" / "sea_water.yaml",
        "vagina": REPO_ROOT / "data" / "habitats" / "host_associated" / "vagina__96a5db8d.yaml",
        "milk": REPO_ROOT / "data" / "habitats" / "host_associated" / "milk.yaml",
        "nasopharynx": REPO_ROOT / "data" / "habitats" / "host_associated" / "nasopharynx__087171fc.yaml",
        "skin_environment": REPO_ROOT / "data" / "habitats" / "other" / "skin_environment.yaml",
        "fecal_environment": REPO_ROOT / "data" / "habitats" / "other" / "fecal_environment.yaml",
        "peat_soil": REPO_ROOT / "data" / "habitats" / "terrestrial" / "peat_soil.yaml",
        "forest_soil": REPO_ROOT / "data" / "habitats" / "terrestrial" / "forest_soil.yaml",
        "plant_litter": REPO_ROOT / "data" / "habitats" / "terrestrial" / "plant_litter.yaml",
        "soil": REPO_ROOT / "data" / "habitats" / "terrestrial" / "soil.yaml",
        "terrestrial_biome": REPO_ROOT / "data" / "habitats" / "terrestrial" / "terrestrial_biome.yaml",
    }
    expected_protein_nodes = {
        "fresh_water": {
            "mechanosensitive_channels": ["UniProtKB:P0C0S1", "UniProtKB:P0A742"],
        },
        "root_nodule": {
            "leghemoglobin": ["UniProtKB:P02233", "UniProtKB:O48668", "UniProtKB:O80405"],
            "nitrogenase": [
                "UniProtKB:Q1M7Z2",
                "UniProtKB:Q1M7Z3",
                "UniProtKB:Q1M7Z4",
                "UniProtKB:Q0RAV4",
                "UniProtKB:Q0RAV5",
                "UniProtKB:Q0RAV6",
            ],
        },
        "sea_water": {
            "nutrient_transport_systems": [
                "UniProtKB:Q4FMH4",
                "UniProtKB:Q4FKZ8",
                "UniProtKB:Q4FM26",
                "UniProtKB:Q4FMK2",
            ],
        },
        "vagina": {
            "mucosal_alpha_amylase": ["UniProtKB:P0DUB6", "UniProtKB:P04746"],
        },
        "milk": {
            "bifidobacterial_hmo_transporters_and_glycosidases": [
                "UniProtKB:B7GPC7",
                "UniProtKB:B7GNN8",
                "UniProtKB:B7GNP9",
            ],
        },
    }
    total_examples = 0
    for slug, node_map in expected_protein_nodes.items():
        doc = yaml.safe_load((CAUSAL_GRAPHS_DIR / f"{slug}.yaml").read_text(encoding="utf-8"))
        hab_doc = yaml.safe_load(habitat_paths[slug].read_text(encoding="utf-8"))
        assert hab_doc["causal_graphs"] == doc["causal_graphs"]
        nodes = {n["node_id"]: n for n in doc["causal_graphs"][0]["nodes"]}
        for node_id, expected_ids in node_map.items():
            node = nodes[node_id]
            assert node["node_type"] == "GENE_OR_PROTEIN"
            examples = node.get("protein_examples", [])
            assert [ex["accession"] for ex in examples] == expected_ids
            for ex in examples:
                assert ex.get("crc64") and len(ex["crc64"]) == 16
                assert ex.get("sequence_length", 0) > 0
                assert ex.get("evidence")
                if ex["accession"] == "UniProtKB:B7GNN8":
                    assert "GH29 alpha-L-fucosidase Blon_2336" in ex["evidence"][0]["notes"]
            total_examples += len(examples)
    assert total_examples == 20

    expected_documented_nodes = {
        "nasopharynx": (
            "lips1_free_fatty_acid_and_protease_secretion",
            "COMMUNITY_PROCESS",
            "UPI0003FCC60A",
        ),
        "skin_environment": (
            "microbial_triacylglycerol_lipase_hydrolysis",
            "COMMUNITY_PROCESS",
            "UPI0003FCC60A",
        ),
        "fecal_environment": (
            "fecal_methylotrophic_methanogenesis",
            "COMMUNITY_PROCESS",
            "UniProtKB:G3EKH7",
        ),
        "peat_soil": (
            "methane_oxidation",
            "PATHWAY",
            "UniProtKB:Q93K59",
        ),
        "forest_soil": (
            "lignocellulolytic_enzymes",
            "MOLECULAR_FUNCTION",
            "Multispecies community pool",
        ),
        "plant_litter": (
            "fungal_extracellular_enzymes",
            "MOLECULAR_FUNCTION",
            "Multispecies community pool",
        ),
        "soil": (
            "extracellular_enzyme_activity",
            "MOLECULAR_FUNCTION",
            "Multispecies community pool",
        ),
        "terrestrial_biome": (
            "extracellular_enzymes",
            "MOLECULAR_FUNCTION",
            "Multispecies community pool",
        ),
    }
    for slug, (node_id, expected_type, expected_substr) in expected_documented_nodes.items():
        doc = yaml.safe_load((CAUSAL_GRAPHS_DIR / f"{slug}.yaml").read_text(encoding="utf-8"))
        hab_doc = yaml.safe_load(habitat_paths[slug].read_text(encoding="utf-8"))
        assert hab_doc["causal_graphs"] == doc["causal_graphs"]
        nodes = {n["node_id"]: n for n in doc["causal_graphs"][0]["nodes"]}
        node = nodes[node_id]
        assert node["node_type"] == expected_type
        assert expected_substr in node.get("description", "")


def test_cycle3_stage2_ten_new_causal_graph_overlays_are_present_and_grounded():
    expected = {
        "permafrost": (
            "ENVO:00000134",
            "permafrost_subzero_cryoadaptation_and_thaw_methanogenesis",
            {
                "PMID:20154119",
                "PMID:25739499",
                "PMID:38860762",
                "PMID:34310124",
                "PMID:37766397",
            },
            REPO_ROOT / "data" / "habitats" / "terrestrial" / "permafrost.yaml",
        ),
        "peatland": (
            "ENVO:00000044",
            "peatland_acidiphilic_methanogenesis_and_type_ii_methanotrophy",
            {
                "PMID:20154331",
                "PMID:25998264",
                "PMID:18093158",
                "PMID:19719661",
            },
            REPO_ROOT / "data" / "habitats" / "terrestrial" / "peatland.yaml",
        ),
        "paddy_field_soil": (
            "ENVO:00005740",
            "paddy_field_soil_rhizosphere_methanogenesis_and_methane_oxidation",
            {
                "PMID:14997675",
                "PMID:38801181",
                "PMID:41582156",
            },
            REPO_ROOT / "data" / "habitats" / "terrestrial" / "paddy_field_soil.yaml",
        ),
        "marine_salt_marsh_biome": (
            "ENVO:01000022",
            "marine_salt_marsh_spartina_sulfur_cycling_and_diazotrophy",
            {
                "PMID:35227326",
                "PMID:18929068",
            },
            REPO_ROOT / "data" / "habitats" / "aquatic" / "marine_salt_marsh_biome.yaml",
        ),
        "freshwater_biome": (
            "ENVO:00000873",
            "freshwater_biome_dom_photolysis_and_ph_bacterioplankton_sorting",
            {
                "PMID:20636377",
                "PMID:22452571",
                "PMID:33148818",
            },
            REPO_ROOT / "data" / "habitats" / "aquatic" / "freshwater_biome.yaml",
        ),
        "sea_grass_bed": (
            "ENVO:01000059",
            "sea_grass_bed_rhizosphere_rol_sulfide_and_nitrogen_cycling",
            {
                "PMID:29687545",
                "PMID:40508259",
                "PMID:39503478",
            },
            REPO_ROOT / "data" / "habitats" / "aquatic" / "sea_grass_bed.yaml",
        ),
        "black_smoker": (
            "ENVO:00000218",
            "black_smoker_hydrothermal_chemolithoautotrophy_and_archaeoglobus_sulfate_reduction",
            {
                "PMID:24414410",
                "PMID:28484604",
                "PMID:34335500",
            },
            REPO_ROOT / "data" / "habitats" / "aquatic" / "black_smoker.yaml",
        ),
        "nectar": (
            "BTO:0000537",
            "nectar_osmotic_climatic_selection_and_pollinator_attractiveness",
            {
                "PMID:25041632",
                "PMID:33370885",
            },
            REPO_ROOT / "data" / "habitats" / "host_associated" / "nectar.yaml",
        ),
        "pitcher": (
            "BTO:0001069",
            "pitcher_phytotelm_prey_digestion_and_diazotrophic_nutrient_supply",
            {
                "PMID:35734258",
                "PMID:35384233",
                "PMID:38995889",
                "PMID:38441172",
            },
            REPO_ROOT / "data" / "habitats" / "host_associated" / "pitcher.yaml",
        ),
        "sewage": (
            "ENVO:00002018",
            "sewage_conveyance_selection_and_antibiotic_resistance_reservoir",
            {
                "PMID:35762794",
                "PMID:30682717",
            },
            REPO_ROOT / "data" / "habitats" / "engineered" / "sewage.yaml",
        ),
    }
    assert len(list(CAUSAL_GRAPHS_DIR.glob("*.yaml"))) == 53
    for slug, (expected_id, expected_graph_id, expected_refs, hab_path) in expected.items():
        overlay_path = CAUSAL_GRAPHS_DIR / f"{slug}.yaml"
        assert overlay_path.exists(), f"{slug}.yaml missing"
        assert hab_path.exists(), f"{hab_path} missing"
        doc = yaml.safe_load(overlay_path.read_text(encoding="utf-8"))
        hab_doc = yaml.safe_load(hab_path.read_text(encoding="utf-8"))
        assert doc["identifier"] == expected_id
        assert hab_doc["identifier"] == expected_id
        assert hab_doc["causal_graphs"] == doc["causal_graphs"]
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
        assert doc["curation_history"][0]["action"] == "ADD_CAUSAL_GRAPH"
        for edge in graph["edges"]:
            for ev in edge.get("evidence", []):
                snippet = ev.get("snippet", "")
                assert "<i>" not in snippet and "</i>" not in snippet
                assert "\u00a0" not in snippet




