from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def _graph():
    path = ROOT / "curation" / "causal_graphs" / "hypersaline_water.yaml"
    graph = yaml.safe_load(path.read_text())["causal_graphs"][0]
    return (
        {node["node_id"]: node for node in graph["nodes"]},
        {edge["edge_id"]: edge for edge in graph["edges"]},
    )


def test_salinity_promotes_the_low_water_activity_condition():
    nodes, edges = _graph()
    edge = edges["salinity_reduces_water_activity"]
    assert edge["object"] == "low_water_activity"
    assert nodes[edge["object"]]["node_type"] == "ENVIRONMENTAL_FACTOR"
    assert edge["predicate"] == "promotes"


def test_salt_in_requires_compatible_machinery_not_universal_proteome_acidity():
    nodes, edges = _graph()
    assert "acidic_proteome" not in nodes
    assert "salt_in_requires_acidic_proteome" not in edges
    edge = edges["salt_in_requires_salt_adapted_machinery"]
    assert edge["subject"] == "potassium_chloride_accumulation"
    assert edge["predicate"] == "requires"
    assert edge["object"] == "salt_adapted_intracellular_machinery"
    assert nodes[edge["object"]]["node_type"] == "TRAIT"
    evidence = {item["reference"]: item for item in edge["evidence"]}
    assert set(evidence) == {"PMID:18412960", "PMID:22527048"}
    assert "Halanaerobiales" in evidence["PMID:22527048"]["notes"]
    assert "universal" in evidence["PMID:22527048"]["notes"]
