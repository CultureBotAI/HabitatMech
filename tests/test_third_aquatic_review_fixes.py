"""Guard exact aquatic hierarchy and graph corrections without promoting status."""

import pytest
from jinja2 import Environment

from habitatmech import seed

CASES = {
    "ENVO:00002150": {
        "slug": "coastal_sea_water",
        "retained": ["ENVO:00002149"],
        "sources": {
            "habitatmech:GOLD.1a3d0aff0c": "ENVO:00001999",
            "habitatmech:GOLD.89754b31f3": "ENVO:00001999",
            "habitatmech:GOLD.ad324e6267": "ENVO:01000125",
        },
    },
    "habitatmech:GOLD.dc31418f43": {
        "slug": "cold_methane_seep",
        "retained": [],
        "sources": {"habitatmech:GOLD.dc31418f43": "habitatmech:GOLD.22656a226b"},
    },
    "ENVO:01000263": {
        "slug": "cold_seep",
        "retained": ["ENVO:01000262"],
        "sources": {"habitatmech:GOLD.95dbf8d7ac": "ENVO:00001999"},
    },
    "ENVO:01000298": {
        "slug": "continental_margin",
        "retained": ["ENVO:00002000"],
        "sources": {"habitatmech:GOLD.a8e7b22a71": "ENVO:00001999"},
    },
    "ENVO:00000150": {
        "slug": "coral_reef",
        "retained": ["ENVO:01000143"],
        "sources": {"habitatmech:GOLD.172000a05a": "habitatmech:GOLD.115edc36f8"},
    },
    "ENVO:03600082": {
        "slug": "crustal_fluid",
        "retained": ["ENVO:02000140"],
        "sources": {"habitatmech:GOLD.d5c8338629": "ENVO:00000207"},
    },
    "habitatmech:GOLD.9eab385243": {
        "slug": "cryoconite__08651766",
        "retained": [],
        "sources": {"habitatmech:GOLD.9eab385243": "ENVO:01001511"},
    },
    "habitatmech:GOLD.d022c1c4c5": {
        "slug": "cryoconite__af2a9806",
        "retained": [],
        "sources": {"habitatmech:GOLD.d022c1c4c5": "ENVO:00002200"},
    },
    "ENVO:03000039": {
        "slug": "cryoconite_hole",
        "retained": ["ENVO:03000048"],
        "sources": {"habitatmech:GOLD.be661308d8": "habitatmech:GOLD.6faa98a0aa"},
    },
    "habitatmech:GOLD.9b43a12f0c": {
        "slug": "cyanobacterial_aggregates",
        "retained": [],
        "sources": {"habitatmech:GOLD.9b43a12f0c": "ENVO:00000021"},
    },
    "ENVO:03600071": {
        "slug": "cyanobacterial_bloom",
        "retained": ["ENVO:00000012"],
        "sources": {"habitatmech:GOLD.95bd6f3756": "ENVO:00000021"},
    },
    "habitatmech:GOLD.21222434e2": {
        "slug": "deep_subsurface__45e0aabf",
        "retained": [],
        "sources": {"habitatmech:GOLD.21222434e2": "ENVO:00002030"},
    },
    "habitatmech:GOLD.3841c9c3af": {
        "slug": "deep_subsurface__f51dcfb9",
        "retained": [],
        "sources": {"habitatmech:GOLD.3841c9c3af": "ENVO:00001999"},
    },
    "habitatmech:GOLD.835443324e": {
        "slug": "delivery_networks",
        "retained": [],
        "sources": {"habitatmech:GOLD.835443324e": "habitatmech:GOLD.99a88ecb51"},
    },
    "habitatmech:GOLD.615df5f198": {
        "slug": "demersal_zone",
        "retained": [],
        "sources": {"habitatmech:GOLD.615df5f198": "ENVO:00001999"},
    },
    "habitatmech:GOLD.3b64b1f98f": {
        "slug": "desert_springs",
        "retained": [],
        "sources": {"habitatmech:GOLD.3b64b1f98f": "ENVO:00002011"},
    },
    "ENVO:00000140": {
        "slug": "drainage_ditch",
        "retained": ["ENVO:00000037"],
        "sources": {"habitatmech:GOLD.a4179e8fdc": "ENVO:00002011"},
    },
    "habitatmech:GOLD.4558077daa": {
        "slug": "drainage_pipe_biofilm",
        "retained": [],
        "sources": {"habitatmech:GOLD.4558077daa": "ENVO:01001267"},
    },
    "habitatmech:GOLD.3d72ae189f": {
        "slug": "driven_well",
        "retained": [],
        "sources": {"habitatmech:GOLD.3d72ae189f": "habitatmech:GOLD.22a80cbd14"},
    },
    "habitatmech:GOLD.f87245a357": {
        "slug": "dug_well",
        "retained": [],
        "sources": {"habitatmech:GOLD.f87245a357": "habitatmech:GOLD.22a80cbd14"},
    },
    "ENVO:00002131": {
        "slug": "epilimnion",
        "retained": ["ENVO:01000283"],
        "sources": {"habitatmech:GOLD.2e68a7f68d": "ENVO:00000021"},
    },
    "habitatmech:GOLD.c299b80057": {
        "slug": "epilimnion__460c092c",
        "retained": ["ENVO:00002131"],
        "sources": {"habitatmech:GOLD.c299b80057": "ENVO:01001319"},
    },
    "habitatmech:GOLD.7b556045ad": {
        "slug": "epilimnion__7dae03ad",
        "retained": ["ENVO:00002131"],
        "sources": {"habitatmech:GOLD.7b556045ad": "ENVO:01000617"},
    },
    "habitatmech:GOLD.7f25f9a103": {
        "slug": "epipelagic",
        "retained": [],
        "sources": {"habitatmech:GOLD.7f25f9a103": "ENVO:00001999"},
    },
    "habitatmech:GOLD.aed863b800": {
        "slug": "estuarine_sediment",
        "retained": [],
        "sources": {"habitatmech:GOLD.aed863b800": "ENVO:00000021"},
    },
}


@pytest.fixture(scope="module")
def documents():
    return {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}


def test_twenty_seven_exclusions_change_only_parents_and_history(documents, monkeypatch):
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    sources = {source for case in CASES.values() for source in case["sources"]}
    assert len(sources) == 27
    assert sources <= exclusions.keys()
    monkeypatch.setattr(
        seed,
        "load_gold_parent_exclusions",
        lambda _: {key: row for key, row in exclusions.items() if key not in sources},
    )
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == documents.keys()
    assert {key for key in before if before[key] != documents[key]} == CASES.keys()
    for identifier, case in CASES.items():
        old, new = before[identifier], documents[identifier]
        removed = set(case["sources"].values())
        assert new.get("parent_habitats", []) == case["retained"]
        assert sorted(set(old["parent_habitats"]) - removed) == case["retained"]
        allowed = {"parent_habitats", "curation_history"}
        assert {k: v for k, v in old.items() if k not in allowed} == {
            k: v for k, v in new.items() if k not in allowed
        }
        additions = [e for e in new["curation_history"] if e not in old["curation_history"]]
        assert len(additions) == len(case["sources"])
        assert [e for e in new["curation_history"] if e not in additions] == old["curation_history"]
        for source, parent in case["sources"].items():
            row = exclusions[source]
            assert row.parent_id == parent
            assert seed.mint("GOLD", row.source_path) == source
            events = [e for e in additions if source in e["changes"]]
            assert len(events) == 1
            event = events[0]
            assert event["action"] == "SOURCE_PARENT_EXCLUDED"
            assert event["curator"] == "codex-gpt-5"
            assert event["timestamp"] == "2026-10-12T00:00:00Z"
            assert parent in event["changes"] and row.notes in event["changes"]


@pytest.mark.parametrize("identifier", CASES)
def test_source_nodes_counts_and_independent_parents(identifier, documents):
    doc, case = documents[identifier], CASES[identifier]
    assert doc.get("parent_habitats", []) == case["retained"]
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    raw_rows = seed.read_tsv("gold_ecosystem_paths.tsv")
    for source in case["sources"]:
        path = exclusions[source].source_path
        attestations = [a for a in doc["source_attestations"] if a.get("source_path") == path]
        assert len(attestations) == 1
        attestation = attestations[0]
        raw = next(r for r in raw_rows if r["canonical_path"] == path)
        assert raw["gold_node_ids"].split("|")[0] == attestation["source_id"]
        assert attestation["source"] == "GOLD"
        count = int(raw["organism_count"])
        if count:
            assert attestation["assertion_count"] == count
            assert attestation["assertion_unit"] == "ORGANISM"
        else:
            assert "assertion_count" not in attestation and "assertion_unit" not in attestation


def test_context_links_render_without_punctuation_suffix():
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    template = Environment(autoescape=True).from_string("{{ changes|urlize }}")
    url = "https://github.com/CultureBotAI/HabitatMech/issues/1987"
    for case in CASES.values():
        for source in case["sources"]:
            assert f'href="{url}"' in template.render(changes=exclusions[source].notes)


def test_valid_material_and_waterbody_parents_are_retained(documents):
    assert documents["ENVO:00000138"]["parent_habitats"] == ["ENVO:00000137"]
    assert documents["ENVO:00000045"]["parent_habitats"] == ["ENVO:00000063"]
    assert documents["ENVO:00003064"]["parent_habitats"] == ["ENVO:00002011"]


def test_deep_sediment_environment_and_community_types(documents):
    graph = documents["ENVO:00002113"]["causal_graphs"][0]
    nodes = {n["node_id"]: n for n in graph["nodes"]}
    for name in ("anoxic_porewater", "methanogenic_sediment", "sulfate_methane_transition_zone"):
        assert nodes[name]["node_type"] == "HABITAT"
    for name in ("sulfate_reducing_microorganisms", "sulfate_reducing_bacteria"):
        assert nodes[name]["node_type"] == "COMMUNITY"
        assert "shared" in nodes[name]["description"]
    assert nodes["anme_archaea"]["node_type"] == "TAXON"
    assert len(graph["nodes"]) == 12 and len(graph["edges"]) == 15
    assert all(edge["evidence"] for edge in graph["edges"])
