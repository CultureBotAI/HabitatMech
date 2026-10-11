"""Keep the bounded biomass and reactor corrections separate from open findings."""

import copy
import xml.etree.ElementTree as ET

import yaml

from habitatmech import seed
from habitatmech.curate.causal_graphs import load_causal_graph_curation_files
from habitatmech.curate.gold_parent_exclusions import load_gold_parent_exclusions
from habitatmech.text_map_inputs import semantic_text
from scripts.mechanism_graph import graph_svg


def graph(repo_root):
    path = repo_root / "curation/causal_graphs/bioreactor.yaml"
    return load_causal_graph_curation_files([path])["ENVO:00002123"].causal_graphs[0]


def test_pna_biomass_exclusion_is_isolated_and_preserves_genus(monkeypatch):
    identifier = "habitatmech:GOLD.497ed1acca"
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda path: {
        key: row for key, row in exclusions.items() if key != identifier
    })
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {identifier}
    old, new = before[identifier], after[identifier]
    assert old["parent_habitats"] == ["ENVO:01000155", "habitatmech:GOLD.9f519b94cc"]
    assert new["parent_habitats"] == ["ENVO:01000155"]
    assert new["curation_history"][:-1] == old["curation_history"]
    assert new["curation_history"][-1]["action"] == "SOURCE_PARENT_EXCLUDED"
    for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
        assert new.get(field) == old.get(field), field
    assert (new["grounding_status"], new["mapping_status"]) == ("NARROW", "SEEDED")
    source = new["source_attestations"][0]
    assert source["source_id"] == "gold.ecosystem:8551"
    assert source["source_path"] == exclusions[identifier].source_path
    assert source["mapping_predicate"] == "skos:narrowMatch"  # #1398 remains open.
    assert "assertion_count" not in source and "assertion_unit" not in source


def test_community_entity_is_distinct_from_taxon_and_process_and_renders(repo_root):
    current = graph(repo_root)  # Closed-schema validation accepts COMMUNITY.
    nodes = {node["node_id"]: node for node in current["nodes"]}
    assert nodes["retained_microbiome"]["node_type"] == "COMMUNITY"
    assert "grounding" not in nodes["retained_microbiome"]
    assert nodes["anaerobic_syntrophy"]["node_type"] == "COMMUNITY_PROCESS"
    assert nodes["methanogenic_archaea"]["node_type"] == "TAXON"
    html = str(graph_svg(current, "community"))
    root = ET.fromstring(html[html.index("<svg "):html.index("</svg>") + 6])
    ns = {"s": "http://www.w3.org/2000/svg"}
    node = root.find('.//s:g[@data-node-id="retained_microbiome"]', ns)
    assert node is not None
    assert "COMMUNITY" in "".join(node.itertext())
    assert len(root.findall('.//s:g[@class="graph-edge"]', ns)) == 19


def test_reactor_scope_and_hydrogen_roles_are_explicit(repo_root):
    current = graph(repo_root)
    assert "not requirements for every bioreactor" in current["description"]
    assert "issue 1638" in current["description"]
    edges = {edge["edge_id"]: edge for edge in current["edges"]}
    assert "does not require liquid" in edges["bioreactor_determined_by_containment"]["description"]
    assert "In liquid-culture designs" in edges["containment_maintains_liquid_medium"]["description"]
    dilution = edges["hydraulic_retention_creates_dilution"]["description"]
    assert "without independent cell retention" in dilution
    assert "inference" in edges["mixing_aeration_shapes_microbiome"]["description"]
    retention = edges["attached_biofilm_retains_microbiome"]["description"]
    assert "detachment and washout can still occur" in retention
    substrate = edges["methanogens_convert_intermediates_to_methane"]
    assert "electron donor" in substrate["description"]
    assert "carbon dioxide" in substrate["description"]
    assert "alternative guild activities" in substrate["description"]
    assert "Table 1 (p119)" in substrate["evidence"][0]["notes"]


def test_generated_reactor_keeps_observations_and_graph_is_map_neutral(repo_root):
    record = yaml.safe_load((repo_root / "data/habitats/engineered/bioreactor.yaml").read_text())
    assert record["causal_graphs"] == [graph(repo_root)]
    assert record["mapping_status"] == "SEEDED"
    assert len(record["source_attestations"]) == 4
    assert len(record["characteristic_taxa"]) == 49
    assert len(record["environmental_parameters"]) == 5
    without_graph = copy.deepcopy(record)
    without_graph.pop("causal_graphs")
    without_graph.pop("curation_history")
    assert semantic_text(record) == semantic_text(without_graph)
