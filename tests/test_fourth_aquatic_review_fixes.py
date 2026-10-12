"""Bounded aquatic hierarchy and freshwater mechanism corrections (#1994/#1995)."""

from dataclasses import replace

import pytest
from jinja2 import Environment

from habitatmech import seed

CASES = {'habitatmech:GOLD.5ac437e3dc': {'slug': 'estuary__5f780975',
                                 'source': 'habitatmech:GOLD.5ac437e3dc',
                                 'removed': 'ENVO:00000021',
                                 'retained': ['ENVO:00000045']},
 'habitatmech:GOLD.bd318592b2': {'slug': 'estuary__bae88a25',
                                 'source': 'habitatmech:GOLD.bd318592b2',
                                 'removed': 'habitatmech:GOLD.115edc36f8',
                                 'retained': ['ENVO:00000045']},
 'habitatmech:GOLD.57a5257707': {'slug': 'estuary_microbial_mat',
                                 'source': 'habitatmech:GOLD.57a5257707',
                                 'removed': 'habitatmech:GOLD.115edc36f8',
                                 'retained': ['ENVO:01000008']},
 'habitatmech:GOLD.4849010f40': {'slug': 'estuary_sediment',
                                 'source': 'habitatmech:GOLD.4849010f40',
                                 'removed': 'habitatmech:GOLD.115edc36f8',
                                 'retained': ['ENVO:00002007']},
 'habitatmech:GOLD.22656a226b': {'slug': 'floodplain__7ad4b08f',
                                 'source': 'habitatmech:GOLD.22656a226b',
                                 'removed': 'ENVO:00002011',
                                 'retained': ['ENVO:00000255']},
 'habitatmech:GOLD.135b9b67f7': {'slug': 'floodplain__98d09203',
                                 'source': 'habitatmech:GOLD.135b9b67f7',
                                 'removed': 'ENVO:00002030',
                                 'retained': ['ENVO:00000255']},
 'habitatmech:GOLD.93f4cea4a4': {'slug': 'floodplain_lake',
                                 'source': 'habitatmech:GOLD.93f4cea4a4',
                                 'removed': 'ENVO:00002011',
                                 'retained': []},
 'ENVO:03600007': {'slug': 'formation_fluid',
                   'source': 'habitatmech:GOLD.5f736096fc',
                   'removed': 'habitatmech:GOLD.f8b744283b',
                   'retained': ['ENVO:02000140']},
 'habitatmech:GOLD.88e2b29307': {'slug': 'fossil',
                                 'source': 'habitatmech:GOLD.88e2b29307',
                                 'removed': 'ENVO:00001999',
                                 'retained': []},
 'habitatmech:GOLD.3426da4c96': {'slug': 'fracking_water__af948aea',
                                 'source': 'habitatmech:GOLD.3426da4c96',
                                 'removed': 'habitatmech:GOLD.ce244e62cd',
                                 'retained': ['ENVO:01001869']},
 'ENVO:00002011': {'slug': 'fresh_water',
                   'source': 'habitatmech:GOLD.ad12f0169a',
                   'removed': 'ENVO:00002030',
                   'retained': ['ENVO:00002006']},
 'ENVO:01001511': {'slug': 'freshwater_ice',
                   'source': 'habitatmech:GOLD.c18afe6ef1',
                   'removed': 'ENVO:00002011',
                   'retained': ['ENVO:01000277', 'ENVO:02000140']},
 'ENVO:00000021': {'slug': 'freshwater_lake',
                   'source': 'habitatmech:GOLD.d14ddff103',
                   'removed': 'ENVO:00002011',
                   'retained': ['ENVO:00000020', 'ENVO:01001320']},
 'ENVO:01000297': {'slug': 'freshwater_river',
                   'source': 'habitatmech:GOLD.b9a8cb85e1',
                   'removed': 'ENVO:00002011',
                   'retained': ['ENVO:00000022', 'ENVO:03605007']},
 'ENVO:00000488': {'slug': 'glacial_lake',
                   'source': 'habitatmech:GOLD.a5e461ce2b',
                   'removed': 'ENVO:01001511',
                   'retained': ['ENVO:00000020']},
 'habitatmech:GOLD.6faa98a0aa': {'slug': 'glacier__0eab88a6',
                                 'source': 'habitatmech:GOLD.6faa98a0aa',
                                 'removed': 'ENVO:00002011',
                                 'retained': ['ENVO:00000133']},
 'habitatmech:GOLD.0c89489e1b': {'slug': 'glacier__efa45690',
                                 'source': 'habitatmech:GOLD.0c89489e1b',
                                 'removed': 'ENVO:01001511',
                                 'retained': ['ENVO:00000133']},
 'habitatmech:GOLD.f3dc60ff11': {'slug': 'glacier_meltwater',
                                 'source': 'habitatmech:GOLD.f3dc60ff11',
                                 'removed': 'ENVO:01001511',
                                 'retained': []},
 'habitatmech:GOLD.cbad89b6dd': {'slug': 'glacier_stream',
                                 'source': 'habitatmech:GOLD.cbad89b6dd',
                                 'removed': 'habitatmech:GOLD.6faa98a0aa',
                                 'retained': []},
 'habitatmech:GOLD.22a80cbd14': {'slug': 'groundwater',
                                 'source': 'habitatmech:GOLD.22a80cbd14',
                                 'removed': 'habitatmech:GOLD.21222434e2',
                                 'retained': ['ENVO:01001004']},
 'habitatmech:GOLD.4100d83c91': {'slug': 'hadalpelagic',
                                 'source': 'habitatmech:GOLD.4100d83c91',
                                 'removed': 'ENVO:00001999',
                                 'retained': []},
 'habitatmech:GOLD.3fe7cdc936': {'slug': 'harbor__5962cec6',
                                 'source': 'habitatmech:GOLD.3fe7cdc936',
                                 'removed': 'ENVO:00002011',
                                 'retained': ['ENVO:00000463']},
 'habitatmech:GOLD.c085f6141a': {'slug': 'hot_42_90c',
                                 'source': 'habitatmech:GOLD.c085f6141a',
                                 'removed': 'ENVO:00000051',
                                 'retained': []},
 'ENVO:00000051': {'slug': 'hot_spring',
                   'source': 'habitatmech:GOLD.f0e9ce4655',
                   'removed': 'ENVO:00002030',
                   'retained': ['ENVO:00000027']},
 'habitatmech:GOLD.db79f0142d': {'slug': 'hydrocarbon__a75cc82e',
                                 'source': 'habitatmech:GOLD.db79f0142d',
                                 'removed': 'habitatmech:GOLD.3841c9c3af',
                                 'retained': []}}


@pytest.fixture(scope="module")
def documents():
    return {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}


def test_twenty_five_exclusions_change_only_parents_and_history(documents, monkeypatch):
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    sources = {case["source"] for case in CASES.values()}
    assert len(sources) == 25 and sources <= exclusions.keys()
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


def test_estuary_genus_corrections_preserve_qualified_identity(documents, monkeypatch):
    targets = {"habitatmech:GOLD.57a5257707": "ENVO:01000008",
               "habitatmech:GOLD.4849010f40": "ENVO:00002007"}
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    for identifier, parent in targets.items():
        assert decisions[identifier].object_id == parent
        decisions[identifier] = replace(
            decisions[identifier], object_id="ENVO:00000045", object_label="estuary"
        )
    monkeypatch.setattr(seed, "load_decisions", lambda _: decisions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == documents.keys()
    assert {key for key in before if before[key] != documents[key]} == targets.keys()
    for identifier, parent in targets.items():
        old, new = before[identifier], documents[identifier]
        assert old["parent_habitats"] == ["ENVO:00000045"]
        assert new["parent_habitats"] == [parent]
        assert new["grounding_status"] == "NARROW" and new["mapping_status"] == "REVIEWED"
        allowed = {"parent_habitats", "curation_history"}
        assert {k: v for k, v in old.items() if k not in allowed} == {
            k: v for k, v in new.items() if k not in allowed
        }


def test_positive_water_material_and_inherited_ontology_controls(documents):
    assert documents["habitatmech:GOLD.4467744e70"]["parent_habitats"] == [
        "ENVO:00002011", "habitatmech:GOLD.22a80cbd14"]
    assert documents["habitatmech:GOLD.7f8e268653"]["parent_habitats"] == [
        "ENVO:00002011", "ENVO:01001004"]
    assert documents["ENVO:01001511"]["parent_habitats"] == ["ENVO:01000277", "ENVO:02000140"]
    assert documents["habitatmech:GOLD.c085f6141a"]["grounding_status"] == "NOT_APPLICABLE"
    assert documents["habitatmech:GOLD.db79f0142d"]["grounding_status"] == "NOT_APPLICABLE"
    assert documents["ENVO:00000039"]["parent_habitats"] == ["ENVO:00000137", "ENVO:00001999"]


def test_freshwater_downshock_types_and_lipid_gating(documents):
    graph = documents["ENVO:00002011"]["causal_graphs"][0]
    assert graph["graph_id"] == "freshwater_hypoosmotic_response"
    assert "downshock" in graph["description"] and "higher-osmolarity" in graph["description"]
    nodes = {n["node_id"]: n for n in graph["nodes"]}
    assert nodes["water_influx"]["node_type"] == "BIOLOGICAL_PROCESS"
    assert nodes["high_turgor_pressure"]["node_type"] == "STATE"
    assert len(nodes) == 6 and len(graph["edges"]) == 5
    edge = next(e for e in graph["edges"] if e["edge_id"] == "turgor_opens_mechanosensitive_channels")
    assert "lipid-bilayer" in edge["description"] and "wall tension" not in edge["description"]
    assert {e["reference"] for e in edge["evidence"]} == {
        "DOI:10.1017/qrd.2022.3", "DOI:10.1085/jgp.201411296"
    }
    assert all(e["evidence"] for e in graph["edges"])


def test_issue_links_render_without_punctuation_suffix():
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    template = Environment(autoescape=True).from_string("{{ changes|urlize }}")
    url = "https://github.com/CultureBotAI/HabitatMech/issues/1994"
    for case in CASES.values():
        assert f'href="{url}"' in template.render(changes=exclusions[case["source"]].notes)
