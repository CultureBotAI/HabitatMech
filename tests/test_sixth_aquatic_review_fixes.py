"""Bounded aquatic hierarchy and marine graph corrections for PR #2003."""

import pytest
from jinja2 import Environment

from habitatmech import seed

CASES = {
    "ENVO:00000210": {
        "slug": "marine_aphotic_zone",
        "sources": [{"source": "habitatmech:GOLD.de5b5dffd1", "removed": "ENVO:00000207"}],
        "removed": ["ENVO:00000207"],
        "issue": 1273,
        "retained": ["ENVO:01000295"],
    },
    "habitatmech:GOLD.5a296e32d2": {
        "slug": "marine_basin_floor",
        "sources": [{"source": "habitatmech:GOLD.5a296e32d2", "removed": "ENVO:00001999"}],
        "removed": ["ENVO:00001999"],
        "issue": 1274,
        "retained": [],
    },
    "ENVO:00000211": {
        "slug": "marine_bathypelagic_zone",
        "sources": [{"source": "habitatmech:GOLD.e02911103f", "removed": "ENVO:00001999"}],
        "removed": ["ENVO:00001999"],
        "issue": 1275,
        "retained": ["ENVO:00000210"],
    },
    "ENVO:01000024": {
        "slug": "marine_benthic_biome",
        "sources": [
            {"source": "habitatmech:GOLD.01adfdcfa4", "removed": "ENVO:00000207"},
            {"source": "habitatmech:GOLD.d0bf6f6843", "removed": "ENVO:00001999"},
        ],
        "removed": ["ENVO:00000207", "ENVO:00001999"],
        "issue": 1280,
        "retained": ["ENVO:00000447", "habitatmech:GOLD.3b64b1f98f"],
    },
    "ENVO:03600041": {
        "slug": "marine_lake",
        "sources": [{"source": "habitatmech:GOLD.e746c98e4b", "removed": "ENVO:00001999"}],
        "removed": ["ENVO:00001999"],
        "issue": 1282,
        "retained": ["ENVO:00000020"],
    },
    "ENVO:01000125": {
        "slug": "marine_littoral_zone",
        "sources": [{"source": "habitatmech:GOLD.2a3e25f443", "removed": "ENVO:00001999"}],
        "removed": ["ENVO:00001999"],
        "issue": 1283,
        "retained": ["ENVO:01000407"],
    },
    "ENVO:00000213": {
        "slug": "marine_mesopelagic_zone",
        "sources": [{"source": "habitatmech:GOLD.76bc4edc73", "removed": "ENVO:00001999"}],
        "removed": ["ENVO:00001999"],
        "issue": 1285,
        "retained": ["ENVO:00000210"],
    },
    "ENVO:00005795": {
        "slug": "marine_mud",
        "sources": [{"source": "habitatmech:GOLD.7429158f71", "removed": "ENVO:00001999"}],
        "removed": ["ENVO:00001999"],
        "issue": 1287,
        "retained": ["ENVO:01000001", "ENVO:01000813"],
    },
    "ENVO:00000208": {
        "slug": "marine_pelagic_zone",
        "sources": [{"source": "habitatmech:GOLD.e089065baa", "removed": "ENVO:00001999"}],
        "removed": ["ENVO:00001999"],
        "issue": 1288,
        "retained": ["ENVO:01000295"],
    },
    "ENVO:00000209": {
        "slug": "marine_photic_zone",
        "sources": [{"source": "habitatmech:GOLD.7d154f5642", "removed": "ENVO:00000207"}],
        "removed": ["ENVO:00000207"],
        "issue": 1289,
        "retained": ["ENVO:01000295"],
    },
    "ENVO:03000033": {
        "slug": "marine_sediment",
        "sources": [{"source": "habitatmech:GOLD.da51ff29f9", "removed": "ENVO:00001999"}],
        "removed": ["ENVO:00001999"],
        "issue": 1293,
        "retained": ["ENVO:00002007"],
    },
    "ENVO:01000124": {
        "slug": "marine_supra_littoral_zone",
        "sources": [{"source": "habitatmech:GOLD.600724f138", "removed": "ENVO:00001999"}],
        "removed": ["ENVO:00001999"],
        "issue": 1297,
        "retained": ["ENVO:01001201"],
    },
    "ENVO:00001999": {
        "slug": "marine_water_body",
        "sources": [{"source": "habitatmech:GOLD.5856c699e4", "removed": "ENVO:00002030"}],
        "removed": ["ENVO:00002030"],
        "issue": 1300,
        "retained": ["ENVO:01000617"],
    },
    "ENVO:00000035": {
        "slug": "marsh",
        "sources": [{"source": "habitatmech:GOLD.8298c8eeda", "removed": "ENVO:00000043"}],
        "removed": ["ENVO:00000043"],
        "issue": 1302,
        "retained": ["ENVO:01001209"],
    },
    "ENVO:03000040": {
        "slug": "melt_pond",
        "sources": [{"source": "habitatmech:GOLD.4020effdf7", "removed": "ENVO:00002200"}],
        "removed": ["ENVO:00002200"],
        "issue": 1223,
        "retained": ["ENVO:00000063"],
    },
    "ENVO:01000722": {
        "slug": "meltwater",
        "sources": [{"source": "habitatmech:GOLD.963dbebfe9", "removed": "habitatmech:GOLD.6faa98a0aa"}],
        "removed": ["habitatmech:GOLD.6faa98a0aa"],
        "issue": 1223,
        "retained": ["ENVO:00002006"],
    },
    "ENVO:00000199": {
        "slug": "meromictic_lake",
        "sources": [{"source": "habitatmech:GOLD.4f1a9febbf", "removed": "ENVO:00002011"}],
        "removed": ["ENVO:00002011"],
        "issue": 1220,
        "retained": ["ENVO:00000020"],
    },
    "ENVO:00002132": {
        "slug": "metalimnion",
        "sources": [{"source": "habitatmech:GOLD.7defa41cfd", "removed": "ENVO:00000021"}],
        "removed": ["ENVO:00000021"],
        "issue": 1245,
        "retained": ["ENVO:00002269", "ENVO:01000813"],
    },
    "habitatmech:GOLD.943a41f487": {
        "slug": "microbial_mat__2020a793",
        "sources": [{"source": "habitatmech:GOLD.943a41f487", "removed": "habitatmech:GOLD.d39a2ed099"}],
        "removed": ["habitatmech:GOLD.d39a2ed099"],
        "issue": 1397,
        "retained": ["ENVO:01000008"],
    },
    "habitatmech:GOLD.675b6b6cab": {
        "slug": "microbial_mat__23532df8",
        "sources": [{"source": "habitatmech:GOLD.675b6b6cab", "removed": "ENVO:03600041"}],
        "removed": ["ENVO:03600041"],
        "issue": 1397,
        "retained": ["ENVO:01000008"],
    },
    "habitatmech:GOLD.292d5d6ada": {
        "slug": "microbial_mat__5129baa2",
        "sources": [{"source": "habitatmech:GOLD.292d5d6ada", "removed": "ENVO:00000023"}],
        "removed": ["ENVO:00000023"],
        "issue": 1397,
        "retained": ["ENVO:01000008"],
    },
    "habitatmech:GOLD.9b3b1cd806": {
        "slug": "microbial_mat__54ad7767",
        "sources": [{"source": "habitatmech:GOLD.9b3b1cd806", "removed": "habitatmech:GOLD.2a6cc2b868"}],
        "removed": ["habitatmech:GOLD.2a6cc2b868"],
        "issue": 1397,
        "retained": ["ENVO:01000008"],
    },
    "habitatmech:GOLD.e066163fc8": {
        "slug": "microbial_mat__8a9e02e4",
        "sources": [{"source": "habitatmech:GOLD.e066163fc8", "removed": "ENVO:00000043"}],
        "removed": ["ENVO:00000043"],
        "issue": 1397,
        "retained": ["ENVO:01000008"],
    },
    "habitatmech:GOLD.cdfbc8d8b6": {
        "slug": "microbial_mat__b6425172",
        "sources": [{"source": "habitatmech:GOLD.cdfbc8d8b6", "removed": "habitatmech:GOLD.c9a99e0db8"}],
        "removed": ["habitatmech:GOLD.c9a99e0db8"],
        "issue": 1397,
        "retained": ["ENVO:01000008"],
    },
    "habitatmech:GOLD.f962316223": {
        "slug": "microbial_mat__eb27cff0",
        "sources": [{"source": "habitatmech:GOLD.f962316223", "removed": "habitatmech:GOLD.22656a226b"}],
        "removed": ["habitatmech:GOLD.22656a226b"],
        "issue": 1397,
        "retained": ["ENVO:01000008"],
    },
    "habitatmech:GOLD.f128d45ecf": {
        "slug": "microbial_mat__fc2dbb7f",
        "sources": [{"source": "habitatmech:GOLD.f128d45ecf", "removed": "habitatmech:GOLD.41f771c2b4"}],
        "removed": ["habitatmech:GOLD.41f771c2b4"],
        "issue": 1397,
        "retained": ["ENVO:01000008"],
    },
    "habitatmech:GOLD.056292f510": {
        "slug": "microbial_mats",
        "sources": [{"source": "habitatmech:GOLD.056292f510", "removed": "habitatmech:GOLD.8b53067bc5"}],
        "removed": ["habitatmech:GOLD.8b53067bc5"],
        "issue": 1397,
        "retained": ["ENVO:01000008"],
    },
    "habitatmech:GOLD.ff22e48912": {
        "slug": "microbial_mats__200e1828",
        "sources": [{"source": "habitatmech:GOLD.ff22e48912", "removed": "ENVO:01000297"}],
        "removed": ["ENVO:01000297"],
        "issue": 1397,
        "retained": ["ENVO:01000008"],
    },
}


@pytest.fixture(scope="module")
def documents():
    return {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}


def test_twenty_nine_exclusions_change_only_parents_and_history(documents, monkeypatch):
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    sources = {s["source"] for c in CASES.values() for s in c["sources"]}
    assert len(CASES) == 28 and len(sources) == 29 and sources <= exclusions.keys()
    monkeypatch.setattr(
        seed,
        "load_gold_parent_exclusions",
        lambda _: {key: value for key, value in exclusions.items() if key not in sources},
    )
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == documents.keys()
    assert {key for key in before if before[key] != documents[key]} == CASES.keys()
    for identifier, case in CASES.items():
        old, new = before[identifier], documents[identifier]
        assert new.get("parent_habitats", []) == case["retained"]
        assert sorted(set(old["parent_habitats"]) - set(case["removed"])) == case["retained"]
        allowed = {"parent_habitats", "curation_history"}
        assert {k: v for k, v in old.items() if k not in allowed} == {
            k: v for k, v in new.items() if k not in allowed
        }
        additions = [e for e in new["curation_history"] if e not in old["curation_history"]]
        assert len(additions) == len(case["sources"])
        assert [e for e in new["curation_history"] if e not in additions] == old["curation_history"]
        for source in case["sources"]:
            row = exclusions[source["source"]]
            assert seed.mint("GOLD", row.source_path) == source["source"]
            assert row.parent_id == source["removed"]
            events = [
                e for e in additions
                if row.notes in e["changes"] and f"for {source['source']} (" in e["changes"]
            ]
            assert len(events) == 1
            event = events[0]
            assert event["action"] == "SOURCE_PARENT_EXCLUDED"
            assert event["curator"] == "codex-gpt-5"
            assert event["timestamp"] == "2026-10-12T00:00:00Z"


@pytest.mark.parametrize("identifier", CASES)
def test_exact_source_paths_counts_units_and_retained_parents(identifier, documents):
    case, doc = CASES[identifier], documents[identifier]
    assert doc.get("parent_habitats", []) == case["retained"]
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    for source in case["sources"]:
        row = exclusions[source["source"]]
        raw = next(
            r for r in seed.read_tsv("gold_ecosystem_paths.tsv") if r["canonical_path"] == row.source_path
        )
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


def test_independent_ontology_and_mat_genera_remain(documents):
    assert documents["ENVO:00000210"]["parent_habitats"] == ["ENVO:01000295"]
    assert documents["ENVO:03000033"]["parent_habitats"] == ["ENVO:00002007"]
    assert documents["ENVO:00001999"]["parent_habitats"] == ["ENVO:01000617"]
    assert documents["ENVO:00000035"]["parent_habitats"] == ["ENVO:01001209"]
    for identifier, case in CASES.items():
        if case["slug"].startswith("microbial_mat"):
            assert documents[identifier]["parent_habitats"] == ["ENVO:01000008"]
            assert documents[identifier]["identifier"] == identifier


def test_sulfur_graph_conditional_chemistry_and_evidence(documents):
    graph = documents["ENVO:03000033"]["causal_graphs"][0]
    assert graph["graph_id"] == "marine_sediment_sulfate_sulfur_cycling"
    assert "conditional" in graph["description"] and "oxic to basement" in graph["description"]
    assert "inorganic carbon" in graph["description"]
    nodes = {n["node_id"]: n for n in graph["nodes"]}
    edges = {e["edge_id"]: e for e in graph["edges"]}
    assert len(nodes) == len(edges) == 14
    assert nodes["anoxic_porewater"]["node_type"] == "HABITAT"
    for key in ("sulfate_reducing_microorganisms", "sulfur_oxidizing_microorganisms"):
        assert nodes[key]["node_type"] == "COMMUNITY"
        assert "modeled sediment" in nodes[key]["label"]
    assert edges["oxygen_depletion_creates_anoxic_porewater"]["predicate"] == "can create"
    assert "can overlap" in edges["anoxic_porewater_enables_sulfate_reduction"]["description"]
    assert (
        "not a carbon-mineralization product" in edges["sulfate_reduction_mineralizes_carbon"]["description"]
    )
    assert "PMID:31105660" in {e["reference"] for e in edges["reactive_iron_traps_sulfide"]["evidence"]}
    assert all("snippet" not in evidence for e in edges.values() for evidence in e["evidence"])
    assert all(e["subject"] in nodes and e["object"] in nodes and e["evidence"] for e in edges.values())


def test_water_body_uses_habitat_community_and_gene_product_nodes(documents):
    graph = documents["ENVO:00001999"]["causal_graphs"][0]
    assert graph["graph_id"] == "marine_water_body_biological_carbon_pump"
    assert "interacting functional assemblages" in graph["description"]
    nodes = {n["node_id"]: n for n in graph["nodes"]}
    assert len(nodes) == len(graph["edges"]) == 15
    assert nodes["euphotic_zone"]["node_type"] == nodes["dark_ocean"]["node_type"] == "HABITAT"
    for key in ("marine_phytoplankton", "particle_associated_bacteria", "free_living_heterotrophs"):
        assert nodes[key]["node_type"] == "COMMUNITY"
    assert nodes["extracellular_enzymes"]["node_type"] == "GENE_OR_PROTEIN"


def test_issue_links_render_without_punctuation_suffix():
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    template = Environment(autoescape=True).from_string("{{ changes|urlize }}")
    for case in CASES.values():
        url = f"https://github.com/CultureBotAI/HabitatMech/issues/{case['issue']}"
        for source in case["sources"]:
            assert f'href="{url}"' in template.render(changes=exclusions[source["source"]].notes)
