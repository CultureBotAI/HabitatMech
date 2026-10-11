"""Guard exact aquatic hierarchy and graph corrections without promoting status."""

import pytest
from jinja2 import Environment

from habitatmech import seed

CASES = {
    "ENVO:00000091": {
        "slug": "beach",
        "retained": ["ENVO:01001884"],
        "sources": {"habitatmech:GOLD.f37e2809fc": "habitatmech:GOLD.115edc36f8"},
    },
    "habitatmech:GOLD.c08255b2d2": {
        "slug": "benthic_zone",
        "retained": [],
        "sources": {"habitatmech:GOLD.c08255b2d2": "ENVO:00001999"},
    },
    "habitatmech:GOLD.e331fc84ae": {
        "slug": "biofilm__599a99de",
        "retained": ["ENVO:00002034"],
        "sources": {"habitatmech:GOLD.e331fc84ae": "ENVO:00000023"},
    },
    "habitatmech:GOLD.5298ffd023": {
        "slug": "biofilm__5f164a0f",
        "retained": ["ENVO:00002034"],
        "sources": {"habitatmech:GOLD.5298ffd023": "habitatmech:GOLD.d61fa6c9ee"},
    },
    "ENVO:00002034": {
        "slug": "biofilm__cc6fe05a",
        "retained": ["ENVO:01000549"],
        "sources": {
            "habitatmech:GOLD.3911678ce4": "habitatmech:GOLD.3ec896865d",
            "habitatmech:GOLD.00cc26ac8b": "habitatmech:GOLD.4bd2954af9",
            "habitatmech:GOLD.f8048a6e2a": "habitatmech:GOLD.ec116f9a37",
        },
    },
    "habitatmech:GOLD.748b381af4": {
        "slug": "biofilm__e72e4f05",
        "retained": ["ENVO:00002034"],
        "sources": {"habitatmech:GOLD.748b381af4": "ENVO:00000021"},
    },
    "habitatmech:GOLD.15bcd61a84": {
        "slug": "biofouling",
        "retained": [],
        "sources": {"habitatmech:GOLD.15bcd61a84": "habitatmech:GOLD.22a80cbd14"},
    },
    "habitatmech:GOLD.3ec896865d": {
        "slug": "biofouling__438bcaa2",
        "retained": [],
        "sources": {"habitatmech:GOLD.3ec896865d": "ENVO:00002011"},
    },
    "habitatmech:GOLD.ec116f9a37": {
        "slug": "biofouling__50243100",
        "retained": [],
        "sources": {"habitatmech:GOLD.ec116f9a37": "habitatmech:GOLD.ce244e62cd"},
    },
    "habitatmech:GOLD.4bd2954af9": {
        "slug": "biofouling__fa010eab",
        "retained": [],
        "sources": {"habitatmech:GOLD.4bd2954af9": "ENVO:00001999"},
    },
    "habitatmech:GOLD.96e16482f3": {
        "slug": "bog_lake",
        "retained": [],
        "sources": {"habitatmech:GOLD.96e16482f3": "ENVO:00002011"},
    },
    "ENVO:00002226": {
        "slug": "borehole",
        "retained": ["ENVO:00000070", "ENVO:03000117"],
        "sources": {"habitatmech:GOLD.61d35511fd": "habitatmech:GOLD.22a80cbd14"},
    },
    "habitatmech:GOLD.cc5b244380": {
        "slug": "brine__2299825d",
        "retained": ["ENVO:00003044"],
        "sources": {"habitatmech:GOLD.cc5b244380": "habitatmech:GOLD.713c7f352a"},
    },
    "habitatmech:GOLD.656eda3dea": {
        "slug": "canal__c42831a4",
        "retained": ["ENVO:00000014"],
        "sources": {"habitatmech:GOLD.656eda3dea": "ENVO:00002011"},
    },
    "habitatmech:GOLD.d9fb6dd542": {
        "slug": "cave_lake",
        "retained": [],
        "sources": {"habitatmech:GOLD.d9fb6dd542": "habitatmech:GOLD.22a80cbd14"},
    },
    "habitatmech:GOLD.aed29e2fc1": {
        "slug": "cave_microbial_mat",
        "retained": [],
        "sources": {"habitatmech:GOLD.aed29e2fc1": "habitatmech:GOLD.22a80cbd14"},
    },
    "habitatmech:GOLD.afb49b0d4b": {
        "slug": "cave_pool",
        "retained": [],
        "sources": {"habitatmech:GOLD.afb49b0d4b": "habitatmech:GOLD.22a80cbd14"},
    },
    "habitatmech:GOLD.62bafb5e20": {
        "slug": "cave_pool_sediment",
        "retained": [],
        "sources": {"habitatmech:GOLD.62bafb5e20": "habitatmech:GOLD.22a80cbd14"},
    },
    "habitatmech:GOLD.c0b02b63b9": {
        "slug": "cave_stream",
        "retained": [],
        "sources": {"habitatmech:GOLD.c0b02b63b9": "habitatmech:GOLD.22a80cbd14"},
    },
    "habitatmech:GOLD.5c3db359b7": {
        "slug": "cave_stream_sediment",
        "retained": [],
        "sources": {"habitatmech:GOLD.5c3db359b7": "habitatmech:GOLD.22a80cbd14"},
    },
    "ENVO:00002270": {
        "slug": "chemocline",
        "retained": ["ENVO:01000258"],
        "sources": {"habitatmech:GOLD.a1ead6c3f8": "ENVO:00000199"},
    },
}


@pytest.fixture(scope="module")
def documents():
    return {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}


def test_twenty_three_exclusions_change_only_parents_and_history(documents, monkeypatch):
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    sources = {source for case in CASES.values() for source in case["sources"]}
    assert len(sources) == 23
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
            assert event["timestamp"] == "2026-10-11T00:00:00Z"
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
    url = "https://github.com/CultureBotAI/HabitatMech/issues/1979"
    for case in CASES.values():
        for source in case["sources"]:
            assert f'href="{url}"' in template.render(changes=exclusions[source].notes)


def test_valid_material_and_waterbody_parents_are_retained(documents):
    assert documents["habitatmech:GOLD.fd7b992495"]["parent_habitats"] == ["ENVO:00002150", "ENVO:00003044"]
    assert documents["ENVO:00002226"]["parent_habitats"] == ["ENVO:00000070", "ENVO:03000117"]
    assert documents["ENVO:00000091"]["parent_habitats"] == ["ENVO:01001884"]
    assert documents["ENVO:00002270"]["parent_habitats"] == ["ENVO:01000258"]


@pytest.mark.parametrize(
    "identifier,names,edge_count",
    [
        ("ENVO:00002034", {"microbial_aggregate", "stress_tolerant_subpopulations"}, 16),
        (
            "ENVO:00002019",
            {"freshwater_bacterioplankton", "marine_bacterioplankton", "estuarine_bacterioplankton"},
            17,
        ),
    ],
)
def test_graph_assemblages_are_communities(identifier, names, edge_count, documents):
    graph = documents[identifier]["causal_graphs"][0]
    nodes = {n["node_id"]: n for n in graph["nodes"]}
    assert all(nodes[name]["node_type"] == "COMMUNITY" for name in names)
    assert len(graph["edges"]) == edge_count
    assert all(edge["evidence"] for edge in graph["edges"])


def test_brackish_transport_and_growth_wording(documents):
    edges = {e["edge_id"]: e for e in documents["ENVO:00002019"]["causal_graphs"][0]["edges"]}
    transport = edges["osmotic_stress_selects_osmoregulatory_transport"]
    assert "biosynthesis is a distinct mechanism" in transport["description"]
    accumulation = edges["transport_enables_compatible_solutes"]
    assert "synthesis is a separate route" in accumulation["description"]
    growth = edges["growth_and_residence_time_establish_estuarine_bacteria"]
    assert "doubling time is much shorter than water residence time" in growth["description"]
    assert growth["evidence"][0]["reference"] == "PMID:15006771"
