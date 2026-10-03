from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def _graph(slug):
    path = ROOT / "curation" / "causal_graphs" / f"{slug}.yaml"
    graph = yaml.safe_load(path.read_text())["causal_graphs"][0]
    return (
        {node["node_id"]: node for node in graph["nodes"]},
        {edge["edge_id"]: edge for edge in graph["edges"]},
    )


def test_hot_spring_growth_capacity_and_carbon_fixation_endpoints():
    nodes, edges = _graph("hot_spring")
    selection = edges["high_temperature_selects_thermophiles"]
    assert nodes[selection["object"]]["node_type"] == "CAPACITY"
    assert selection["object"] == "thermophilic_growth"
    assert selection["evidence"][0]["reference"] == "PMID:30038374"

    fixation = edges["primary_production_fixes_inorganic_carbon"]
    assert fixation["predicate"] == "involves"
    assert nodes[fixation["subject"]]["node_type"] == "COMMUNITY_PROCESS"
    assert nodes[fixation["object"]]["node_type"] == "BIOLOGICAL_PROCESS"
    assert "low-organic" not in fixation["description"]
    assert "p. 342" in fixation["evidence"][0]["notes"]


def test_vent_capacities_and_contexts_are_not_taxa_or_cell_states():
    nodes, edges = _graph("hydrothermal_vent")
    assert nodes["mixing_zone"]["node_type"] == "HABITAT"
    assert nodes["surface_associated_growth"]["node_type"] == "BIOLOGICAL_PROCESS"
    for prefix in ("sulfur", "hydrogen"):
        capacity = f"{prefix}_oxidation_capacity"
        assert nodes[capacity]["node_type"] == "CAPACITY"
        metabolism = edges[f"{prefix}_oxidizers_perform_{prefix}_oxidation"]
        assert metabolism["subject"] == capacity
        assert metabolism["predicate"] == "enables"
        fixation = edges[f"{prefix}_oxidation_fuels_carbon_fixation"]
        assert fixation["predicate"] == "can fuel"

    hydrogen = edges["hydrogen_oxidation_fuels_carbon_fixation"]
    evidence = {item["reference"]: item for item in hydrogen["evidence"]}
    assert set(evidence) == {"PMID:29891698", "PMID:30532749"}
    assert "Crab" in evidence["PMID:29891698"]["notes"]
    assert "heterotrophic" in evidence["PMID:30532749"]["notes"]
    assert "vent_biofilms" not in nodes
