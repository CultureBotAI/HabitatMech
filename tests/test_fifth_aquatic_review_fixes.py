"""Scoped hierarchy and liquid-water mechanism fixes reviewed in PR #1999."""

import pytest
from jinja2 import Environment

from habitatmech import seed

CASES = {'habitatmech:GOLD.437f639705': {'slug': 'hydrothermal_plume',
                                 'source': 'habitatmech:GOLD.437f639705',
                                 'removed': 'ENVO:00000215',
                                 'issue': 1235,
                                 'retained': []},
 'ENVO:00000215': {'slug': 'hydrothermal_vent',
                   'source': 'habitatmech:GOLD.77ae835059',
                   'removed': 'ENVO:00001999',
                   'issue': 1235,
                   'retained': ['ENVO:00000027']},
 'ENVO:01001043': {'slug': 'hypersaline_water_environment',
                   'source': 'habitatmech:GOLD.4398c0543d',
                   'removed': 'habitatmech:GOLD.ce244e62cd',
                   'issue': 1245,
                   'retained': ['ENVO:01000307']},
 'ENVO:00002130': {'slug': 'hypolimnion',
                   'source': 'habitatmech:GOLD.2d82ee602e',
                   'removed': 'ENVO:00000021',
                   'issue': 1245,
                   'retained': ['ENVO:01000283']},
 'habitatmech:GOLD.7daa92d793': {'slug': 'hypolimnion__78bbb31f',
                                 'source': 'habitatmech:GOLD.7daa92d793',
                                 'removed': 'ENVO:01000617',
                                 'issue': 1245,
                                 'retained': ['ENVO:00002130']},
 'habitatmech:GOLD.28daa326da': {'slug': 'hypolimnion__d888743c',
                                 'source': 'habitatmech:GOLD.28daa326da',
                                 'removed': 'ENVO:01001319',
                                 'issue': 1245,
                                 'retained': ['ENVO:00002130']},
 'habitatmech:GOLD.fa45416ff4': {'slug': 'hypoxic_zone',
                                 'source': 'habitatmech:GOLD.fa45416ff4',
                                 'removed': 'ENVO:00001999',
                                 'issue': 1245,
                                 'retained': []},
 'habitatmech:GOLD.5d66d49938': {'slug': 'ice',
                                 'source': 'habitatmech:GOLD.5d66d49938',
                                 'removed': 'habitatmech:GOLD.6faa98a0aa',
                                 'issue': 1223,
                                 'retained': ['ENVO:01001125']},
 'ENVO:00000380': {'slug': 'ice_shelf',
                   'source': 'habitatmech:GOLD.83ce4e95f2',
                   'removed': 'ENVO:00001999',
                   'issue': 1247,
                   'retained': ['ENVO:01001547', 'UBERON:0000061']},
 'ENVO:00000475': {'slug': 'inlet',
                   'source': 'habitatmech:GOLD.c590c36168',
                   'removed': 'ENVO:00001999',
                   'issue': 1248,
                   'retained': ['ENVO:00000012']},
 'habitatmech:GOLD.40bfbe291f': {'slug': 'insect_burrows',
                                 'source': 'habitatmech:GOLD.40bfbe291f',
                                 'removed': 'habitatmech:GOLD.e4e91038b5',
                                 'issue': 1250,
                                 'retained': []},
 'habitatmech:GOLD.54055df52f': {'slug': 'intertidal_zone__3d85893c',
                                 'source': 'habitatmech:GOLD.54055df52f',
                                 'removed': 'ENVO:01000125',
                                 'issue': 1254,
                                 'retained': ['ENVO:00000316']},
 'ENVO:00000311': {'slug': 'kettle',
                   'source': 'habitatmech:GOLD.3486e75e52',
                   'removed': 'ENVO:00002011',
                   'issue': 1255,
                   'retained': ['ENVO:00000309', 'ENVO:01001884']},
 'habitatmech:GOLD.d3da9a2ed0': {'slug': 'lake_biofilm',
                                 'source': 'habitatmech:GOLD.d3da9a2ed0',
                                 'removed': 'ENVO:00000021',
                                 'issue': 1259,
                                 'retained': []},
 'ENVO:01000617': {'slug': 'lentic_water_body',
                   'source': 'habitatmech:GOLD.312657c243',
                   'removed': 'ENVO:00002011',
                   'issue': 1260,
                   'retained': ['ENVO:00000063']},
 'habitatmech:GOLD.2f4b860753': {'slug': 'liftoff_microbial_mat',
                                 'source': 'habitatmech:GOLD.2f4b860753',
                                 'removed': 'ENVO:01001511',
                                 'issue': 1223,
                                 'retained': []},
 'habitatmech:GOLD.1c8b5d3fe5': {'slug': 'limnetic_zone',
                                 'source': 'habitatmech:GOLD.1c8b5d3fe5',
                                 'removed': 'ENVO:01000617',
                                 'issue': 1260,
                                 'retained': []},
 'habitatmech:GOLD.00de24c347': {'slug': 'littoral_zone',
                                 'source': 'habitatmech:GOLD.00de24c347',
                                 'removed': 'ENVO:01000617',
                                 'issue': 1260,
                                 'retained': ['ENVO:01000407']},
 'habitatmech:GOLD.5b730a58b7': {'slug': 'littoral_zone__9f547c9b',
                                 'source': 'habitatmech:GOLD.5b730a58b7',
                                 'removed': 'ENVO:00000021',
                                 'issue': 1265,
                                 'retained': ['ENVO:01000407']},
 'ENVO:01000618': {'slug': 'lotic_water_body',
                   'source': 'habitatmech:GOLD.283c698731',
                   'removed': 'ENVO:00002011',
                   'issue': 1268,
                   'retained': ['ENVO:00000063']},
 'habitatmech:GOLD.376c23f892': {'slug': 'mangrove_sediment',
                                 'source': 'habitatmech:GOLD.376c23f892',
                                 'removed': 'habitatmech:GOLD.115edc36f8',
                                 'issue': 1269,
                                 'retained': []},
 'habitatmech:GOLD.abc3a7c55b': {'slug': 'mangrove_soil',
                                 'source': 'habitatmech:GOLD.abc3a7c55b',
                                 'removed': 'habitatmech:GOLD.115edc36f8',
                                 'issue': 1269,
                                 'retained': ['ENVO:02000138']},
 'ENVO:00000057': {'slug': 'mangrove_swamp',
                   'source': 'habitatmech:GOLD.79cfdb171a',
                   'removed': 'habitatmech:GOLD.115edc36f8',
                   'issue': 1270,
                   'retained': ['ENVO:00000230']}}


@pytest.fixture(scope="module")
def documents():
    return {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}


def test_twenty_three_exclusions_change_only_parents_and_history(documents, monkeypatch):
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    sources = {case["source"] for case in CASES.values()}
    assert len(sources) == 23 and sources <= exclusions.keys()
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda _: {
        key: value for key, value in exclusions.items() if key not in sources
    })
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == documents.keys()
    assert {key for key in before if before[key] != documents[key]} == CASES.keys()
    for identifier, case in CASES.items():
        old, new = before[identifier], documents[identifier]
        assert new.get("parent_habitats", []) == case["retained"]
        assert sorted(set(old["parent_habitats"]) - {case["removed"]}) == case["retained"]
        allowed = {"parent_habitats", "curation_history"}
        assert {k: v for k, v in old.items() if k not in allowed} == {
            k: v for k, v in new.items() if k not in allowed
        }
        additions = [e for e in new["curation_history"] if e not in old["curation_history"]]
        assert len(additions) == 1
        assert [e for e in new["curation_history"] if e not in additions] == old["curation_history"]
        event = additions[0]
        row = exclusions[case["source"]]
        assert seed.mint("GOLD", row.source_path) == case["source"]
        assert row.parent_id == case["removed"]
        assert event["action"] == "SOURCE_PARENT_EXCLUDED"
        assert event["curator"] == "codex-gpt-5"
        assert event["timestamp"] == "2026-10-12T00:00:00Z"
        assert case["removed"] in event["changes"] and row.notes in event["changes"]


@pytest.mark.parametrize("identifier", CASES)
def test_exact_source_paths_counts_units_and_retained_parents(identifier, documents):
    case, doc = CASES[identifier], documents[identifier]
    assert doc.get("parent_habitats", []) == case["retained"]
    row = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)[case["source"]]
    raw = next(r for r in seed.read_tsv("gold_ecosystem_paths.tsv") if r["canonical_path"] == row.source_path)
    attestations = [a for a in doc["source_attestations"] if a.get("source_path") == row.source_path]
    assert len(attestations) == 1
    attestation = attestations[0]
    assert attestation["source_id"] == raw["gold_node_ids"].split("|")[0]
    assert attestation["source"] == "GOLD"
    if int(raw["organism_count"]):
        assert attestation["assertion_count"] == int(raw["organism_count"])
        assert attestation["assertion_unit"] == "ORGANISM"
    else:
        assert "assertion_count" not in attestation and "assertion_unit" not in attestation


def test_supported_material_and_ontology_parents_remain(documents):
    assert documents["habitatmech:GOLD.c4f57235c7"]["parent_habitats"] == ["ENVO:01001511"]
    assert documents["habitatmech:GOLD.115edc36f8"]["parent_habitats"] == ["ENVO:00000316"]
    assert documents["ENVO:00000476"]["parent_habitats"] == ["ENVO:00000475"]
    assert documents["ENVO:01000617"]["grounding_status"] == "EXACT"
    assert documents["ENVO:01000618"]["grounding_status"] == "EXACT"


def test_liquid_water_is_a_conditional_marine_model(documents):
    graph = documents["ENVO:00002006"]["causal_graphs"][0]
    assert graph["graph_id"] == "liquid_water_planktonic_solute_foraging"
    assert "marine water column" in graph["description"]
    assert "liquid phase alone" in graph["description"]
    nodes = {n["node_id"]: n for n in graph["nodes"]}
    edges = {e["edge_id"]: e for e in graph["edges"]}
    assert len(nodes) == 13 and len(edges) == 14
    assert nodes["bulk_aqueous_phase"]["node_type"] == "HABITAT"
    assert nodes["free_living_bacteria"]["node_type"] == "COMMUNITY"
    assert nodes["bacterial_biomass"]["node_type"] == "BIOLOGICAL_PROCESS"
    assert all(n["node_type"] != "STATE" for n in nodes.values())
    assert edges["high_water_activity_permits_aquatic_growth"]["object"] == "bacterial_biomass"
    assert edges["liquid_water_provides_high_water_activity"]["predicate"] == "can provide"
    assert "not on liquid phase alone" in edges["liquid_water_provides_high_water_activity"]["description"]
    assert "suspended or sinking" in edges["liquid_water_suspends_polymeric_particles"]["description"]
    assert "costs" in edges["chemotaxis_increases_dom_uptake"]["description"]
    assert "respiration" in edges["uptake_generates_bacterial_biomass"]["description"]
    assert "all free-living bacteria" in edges["dom_supports_heterotrophic_bacteria"]["description"]
    for edge in edges.values():
        assert edge["subject"] in nodes and edge["object"] in nodes and edge["evidence"]
    for edge_id in ("liquid_water_forms_bulk_aqueous_phase", "liquid_water_suspends_polymeric_particles",
                    "uptake_generates_bacterial_biomass", "bacterial_biomass_feeds_microbial_loop"):
        assert "PMID:23204367" in {e["reference"] for e in edges[edge_id]["evidence"]}


def test_issue_links_render_without_punctuation_suffix():
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    template = Environment(autoescape=True).from_string("{{ changes|urlize }}")
    for case in CASES.values():
        url = f'https://github.com/CultureBotAI/HabitatMech/issues/{case["issue"]}'
        assert f'href="{url}"' in template.render(changes=exclusions[case["source"]].notes)
