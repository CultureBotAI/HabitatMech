"""Exact material/context corrections for the sludge and wastewater review."""

from dataclasses import replace

import pytest

from habitatmech import seed

PARENTS = {
    "habitatmech:GOLD.7dc780d154": "ENVO:00002124",
    "habitatmech:GOLD.1029237e41": "ENVO:00002001",
    "habitatmech:GOLD.3c86a15d35": "ENVO:00003043",
    "habitatmech:GOLD.5bfe97c820": "habitatmech:GOLD.b1f94cf5f5",
    "habitatmech:GOLD.33ad86bb23": "habitatmech:GOLD.24cf427e7d",
    "habitatmech:GOLD.17cac82e1c": "ENVO:03600010",
    "habitatmech:GOLD.1032e10222": "ENVO:00002124",
    "habitatmech:GOLD.ca2df10cfe": "ENVO:03600010",
    "habitatmech:GOLD.760974c19d": "habitatmech:GOLD.5e086933bc",
    "habitatmech:GOLD.8d1a6819a4": "habitatmech:GOLD.4a2450370b",
    "habitatmech:GOLD.344aa1f6cc": "habitatmech:GOLD.df1d688f27",
    "habitatmech:GOLD.203ab14b02": "ENVO:00002126",
    "habitatmech:GOLD.c662161205": "habitatmech:GOLD.c07aaa941d",
    "habitatmech:GOLD.036ffbf88b": "ENVO:03600021",
    "habitatmech:GOLD.353a834cfd": "ENVO:00003043",
    "habitatmech:GOLD.335e6f8d6c": "ENVO:00002043",
    "habitatmech:GOLD.39ec66994a": "ENVO:00002124",
    "habitatmech:GOLD.a2b1243a87": "habitatmech:GOLD.24cf427e7d",
    "habitatmech:GOLD.5e086933bc": "ENVO:00002123",
    "habitatmech:GOLD.a2d3d5127a": "habitatmech:GOLD.b6ea996423",
}
WATER = "habitatmech:GOLD.a2d3d5127a"
EFFLUENT = "habitatmech:GOLD.2e804e3e32"


@pytest.fixture(scope="module")
def documents():
    return {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}


def test_twenty_context_exclusions_have_exact_field_scope(documents, monkeypatch):
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    assert PARENTS.keys() <= exclusions.keys()
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda _: {
        key: row for key, row in exclusions.items() if key not in PARENTS
    })
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == documents.keys()
    assert {key for key in before if before[key] != documents[key]} == PARENTS.keys()
    for identifier, parent in PARENTS.items():
        old, new = before[identifier], documents[identifier]
        row = exclusions[identifier]
        assert row.parent_id == parent
        assert row.source_path == new["source_attestations"][0]["source_path"]
        assert parent in old["parent_habitats"]
        assert new["parent_habitats"] == [p for p in old["parent_habitats"] if p != parent]
        allowed = {"parent_habitats", "curation_history"}
        assert {k: v for k, v in old.items() if k not in allowed} == {
            k: v for k, v in new.items() if k not in allowed
        }
        additions = [e for e in new["curation_history"] if e not in old["curation_history"]]
        assert len(additions) == 1
        event = additions[0]
        assert [e for e in new["curation_history"] if e != event] == old["curation_history"]
        assert event["action"] == "SOURCE_PARENT_EXCLUDED"
        assert event["curator"] == "codex-gpt-5"
        assert event["timestamp"] == "2026-10-11T00:00:00Z"
        assert identifier in event["changes"] and parent in event["changes"]
        assert row.notes in event["changes"]


def test_water_decision_changes_only_grounding_comparison_and_history(documents, monkeypatch):
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    decision = decisions[WATER]
    assert decision.decision == "GROUND_AS_PARENT" and decision.review_depth == "ITEM"
    assert decision.object_id == "ENVO:00002001" and decision.grounding_status == "NARROW"
    decisions[WATER] = replace(decision, object_id="ENVO:03600004",
                              object_label="drinking water treatment plant", grounding_status="BROAD")
    monkeypatch.setattr(seed, "load_decisions", lambda _: decisions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == documents.keys()
    assert {key for key in before if before[key] != documents[key]} == {WATER}
    old, new = before[WATER], documents[WATER]
    assert old["parent_habitats"] == ["ENVO:03600004"]
    assert new["parent_habitats"] == ["ENVO:00002001"]
    assert old["grounding_status"] == "BROAD" and new["grounding_status"] == "NARROW"
    assert new["mapping_status"] == "REVIEWED"
    allowed = {"parent_habitats", "grounding_status", "source_attestations", "curation_history"}
    assert {k: v for k, v in old.items() if k not in allowed} == {
        k: v for k, v in new.items() if k not in allowed
    }
    old_source, new_source = old["source_attestations"][0], new["source_attestations"][0]
    assert old_source["mapping_predicate"] == "skos:broadMatch"
    assert new_source["mapping_predicate"] == "skos:narrowMatch"
    assert {k: v for k, v in old_source.items() if k != "mapping_predicate"} == {
        k: v for k, v in new_source.items() if k != "mapping_predicate"
    }
    assert new_source["assertion_count"] == 205 and new_source["assertion_unit"] == "ORGANISM"
    # Correcting the implicit comparison does not resolve mapping endpoint issue #1398.


def test_effluent_keeps_water_parent_without_inheriting_facility(documents):
    assert documents[EFFLUENT]["parent_habitats"] == ["habitatmech:GOLD.335e6f8d6c"]
    seen, todo = set(), [EFFLUENT]
    while todo:
        identifier = todo.pop()
        if identifier in seen:
            continue
        seen.add(identifier)
        todo.extend(documents.get(identifier, {}).get("parent_habitats", []))
    assert "ENVO:00002001" in seen and "ENVO:00002043" not in seen
    assert documents[EFFLUENT]["source_attestations"][0]["assertion_count"] == 80


@pytest.mark.parametrize("identifier", PARENTS)
def test_material_genera_and_frozen_provenance_are_preserved(identifier, documents):
    doc = documents[identifier]
    source = doc["source_attestations"][0]
    assert len(doc["source_attestations"]) == 1 and source["source"] == "GOLD"
    assert seed.mint("GOLD", source["source_path"]) == identifier
    raw = next(r for r in seed.read_tsv("gold_ecosystem_paths.tsv")
               if r["canonical_path"] == source["source_path"])
    assert raw["gold_node_ids"].split("|")[0] == source["source_id"]
    count = int(raw["organism_count"])
    if count:
        assert source["assertion_count"] == count and source["assertion_unit"] == "ORGANISM"
    else:
        assert "assertion_count" not in source and "assertion_unit" not in source
    genus = ("ENVO:00002129" if identifier in {"habitatmech:GOLD.7dc780d154", "habitatmech:GOLD.1032e10222"}
             else "ENVO:00002044" if doc["label"] == "Sludge" else "ENVO:00002001")
    assert doc["parent_habitats"] == [genus]
    assert doc["grounding_status"] == "NARROW"
    assert doc["mapping_status"] == ("REVIEWED" if identifier == WATER else "SEEDED")
