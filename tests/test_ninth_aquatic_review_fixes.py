"""Exact-source saline, seawater and sediment review corrections."""

import json
from dataclasses import replace
from pathlib import Path

import pytest

from habitatmech import seed

CASES = json.loads((Path(__file__).parent / "data/ninth_aquatic_review_cases.json").read_text())


@pytest.fixture(scope="module")
def documents():
    return {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}


def test_only_exact_reviewed_records_change(documents, monkeypatch):
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    definitions = seed.load_curated_definitions(seed.CURATED_DEFINITIONS_PATH)
    overlays = seed.load_causal_graph_curations()
    sources = {s["source"] for case in CASES.values() for s in case["sources"]}
    assert len(CASES) == 32 and len(sources) == 29
    old_decisions = dict(decisions)
    old_definitions = dict(definitions)
    old_overlays = dict(overlays)
    for identifier, case in CASES.items():
        if "decision" in case:
            row = case["decision"]["old"]
            old_decisions[identifier] = seed.Decision(**dict(row, relation=row["relation"] or "parent"))
        if "definition" in case:
            row = case["definition"]["old"]
            old_definitions[identifier] = replace(
                definitions[identifier], exact_synonyms=tuple(row["exact_synonym"].split("|")),
                curator=row["curator"], date=row["date"], notes=row["notes"],
            )
        if "graph" in case:
            row = case["graph"]
            old_overlays[identifier] = replace(
                overlays[identifier], causal_graphs=tuple(row["causal_graphs"]),
                curation_history=tuple(row["curation_history"]),
            )
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda _: {
        key: row for key, row in exclusions.items() if key not in sources
    })
    monkeypatch.setattr(seed, "load_decisions", lambda _: old_decisions)
    monkeypatch.setattr(seed, "load_curated_definitions", lambda _: old_definitions)
    monkeypatch.setattr(seed, "load_causal_graph_curations", lambda _: old_overlays)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == documents.keys()
    assert {key for key in before if before[key] != documents[key]} == CASES.keys()
    for identifier, case in CASES.items():
        old, new = before[identifier], documents[identifier]
        allowed = {"parent_habitats", "curation_history"}
        if "decision" in case:
            allowed |= {"grounding_status", "mapping_status", "source_attestations"}
            assert new["grounding_status"] == "NARROW"
            assert new["mapping_status"] == "REVIEWED"
            def strip(doc):
                return [
                    {k: v for k, v in a.items() if k != "mapping_predicate"}
                    for a in doc["source_attestations"]
                ]
            assert strip(old) == strip(new)
            assert all(a["mapping_predicate"] == "skos:narrowMatch" for a in new["source_attestations"])
        if "definition" in case:
            allowed.add("synonyms")
            assert new["synonyms"] == [s for s in old["synonyms"] if s["synonym_text"] != "Seaweed"]
        if "graph" in case:
            allowed.add("causal_graphs")
            assert all(e in new["curation_history"] for e in old["curation_history"])
        assert {k: v for k, v in old.items() if k not in allowed} == {
            k: v for k, v in new.items() if k not in allowed
        }, identifier
        assert new.get("parent_habitats", []) == case["retained"]


@pytest.mark.parametrize("identifier", CASES)
def test_exact_source_guards_and_unchanged_denominators(identifier, documents):
    case, doc = CASES[identifier], documents[identifier]
    assert doc.get("parent_habitats", []) == case["retained"]
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    for source in case["sources"]:
        row = exclusions[source["source"]]
        assert seed.mint("GOLD", row.source_path) == source["source"]
        assert row.parent_id == source["removed"]
        raw = next(
            r for r in seed.read_tsv("gold_ecosystem_paths.tsv") if r["canonical_path"] == row.source_path
        )
        attestation = next(a for a in doc["source_attestations"] if a.get("source_path") == row.source_path)
        assert attestation["source_id"] == raw["gold_node_ids"].split("|")[0]
        if int(raw["organism_count"]):
            assert attestation["assertion_count"] == int(raw["organism_count"])
            assert attestation["assertion_unit"] == "ORGANISM"
        else:
            assert "assertion_count" not in attestation and "assertion_unit" not in attestation
        assert any(row.notes in e["changes"] for e in doc["curation_history"])


def test_pond_liquid_and_sediment_are_not_interchanged(documents):
    assert documents["habitatmech:GOLD.277843111f"]["parent_habitats"] == [
        "ENVO:03600092", "habitatmech:GOLD.ce244e62cd",
    ]
    assert documents["habitatmech:GOLD.f75e192814"]["parent_habitats"] == ["ENVO:00002010"]
    for identifier in (
        "habitatmech:GOLD.7dbe12a9d1", "habitatmech:GOLD.1bb701a40c",
        "habitatmech:GOLD.96f7d4c555", "habitatmech:GOLD.e63a1a61c3",
    ):
        assert documents[identifier]["parent_habitats"] == ["ENVO:00002007"]
        assert "definition" not in documents[identifier]


def test_uncertain_scopes_are_not_promoted_or_silently_erased(documents):
    for identifier in ("habitatmech:GOLD.ca1e46c594", "habitatmech:GOLD.56c9d8587d"):
        doc = documents[identifier]
        assert not doc.get("parent_habitats")
        assert doc["mapping_status"] == "SEEDED" and doc["grounding_status"] == "UNGROUNDED"
        assert "definition" not in doc
    for identifier in (
        "habitatmech:GOLD.2ff751e0a6", "habitatmech:GOLD.63502a6d41", "habitatmech:GOLD.335c06a602",
    ):
        assert any(p.startswith("habitatmech:") for p in documents[identifier]["parent_habitats"])
    assert "habitatmech:GOLD.ce244e62cd" in documents["ENVO:00000019"]["parent_habitats"]
    seaweed = documents["habitatmech:GOLD.0e7a5162bb"]
    assert "FOODON:03412266" in seaweed["xrefs"]
    assert seaweed["source_attestations"][0]["source_label"] == "Seaweed"
    assert not any(s["synonym_text"].casefold() == "seaweed" for s in seaweed.get("synonyms", []))


def test_seawater_graph_preserves_ids_but_bounds_biological_and_model_scope(documents):
    old = CASES["ENVO:00002149"]["graph"]["causal_graphs"][0]
    new = documents["ENVO:00002149"]["causal_graphs"][0]
    assert new["graph_id"] == old["graph_id"]
    assert {n["node_id"] for n in new["nodes"]} == {n["node_id"] for n in old["nodes"]}
    nodes = {n["node_id"]: n for n in new["nodes"]}
    assert nodes["oligotrophic_marine_bacteria"]["node_type"] == "TAXON"
    assert "Pelagibacter ubique" in nodes["oligotrophic_marine_bacteria"]["label"]
    assert nodes["streamlined_genomes"]["node_type"] == "TRAIT"
    assert nodes["ocean_microbiome_dom_cycling"]["node_type"] == "COMMUNITY_PROCESS"
    edges = {e["edge_id"]: e for e in new["edges"]}
    assert set(edges) == {e["edge_id"] for e in old["edges"]}
    for prior in old["edges"]:
        current = edges[prior["edge_id"]]
        assert (current["subject"], current["object"]) == (prior["subject"], prior["object"])
        assert {e["reference"] for e in prior["evidence"]} <= {e["reference"] for e in current["evidence"]}
    assert new["edges"][:2] == old["edges"][:2]
    assert "model" in edges["nutrient_transporters_control_oligotrophy"]["predicate"]
    assert "not measured community flux" in edges["dilute_uptake_enables_dom_cycling"]["description"]
