"""Scoped parent corrections from the seawater and sediment record reviews."""

from dataclasses import replace

import pytest

from habitatmech import seed


@pytest.fixture(scope="module")
def documents():
    return {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}


def test_context_exclusions_preserve_all_other_claims(documents, monkeypatch):
    targets = {
        "habitatmech:GOLD.a4fe9adfc7": (
            "habitatmech:GOLD.f9af2e0686", "ENVO:00002007", "gold.ecosystem:8010",
            "Engineered > Artificial ecosystem > Aquaculture > Molluscs tank > Sediment",
            "SEEDED", None,
        ),
        "habitatmech:GOLD.87598cbdca": (
            "habitatmech:GOLD.6a0644fced", "ENVO:00002007", "gold.ecosystem:4690",
            "Engineered > Wastewater > Industrial wastewater > Mine water > Sediment",
            "SEEDED", 4,
        ),
        "habitatmech:GOLD.d6c97cc5bd": (
            "habitatmech:GOLD.3e0abbfef7", "ENVO:00002007", "gold.ecosystem:8040",
            "Engineered > Artificial ecosystem > Aquaculture > Marine fish farm > Sediment",
            "SEEDED", None,
        ),
        "habitatmech:GOLD.0cadaca0bf": (
            "ENVO:01000620", "ENVO:00002149", "gold.ecosystem:6459",
            "Engineered > Artificial ecosystem > Mesocosm > Seawater",
            "REVIEWED", None,
        ),
    }
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    assert targets.keys() <= exclusions.keys()
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda _: {
        key: value for key, value in exclusions.items() if key not in targets
    })
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == documents.keys()
    assert {key for key in before if before[key] != documents[key]} == targets.keys()

    for identifier, (removed, retained, source_id, path, status, count) in targets.items():
        old, new = before[identifier], documents[identifier]
        exclusion = exclusions[identifier]
        assert exclusion.source_path == path
        assert exclusion.parent_id == removed
        assert exclusion.date == "2026-10-10"
        assert exclusion.curator == "codex-gpt-5"
        assert old["parent_habitats"] == sorted([removed, retained])
        assert new["parent_habitats"] == [retained]
        assert new["grounding_status"] == "NARROW"
        assert new["mapping_status"] == status

        additions = [e for e in new["curation_history"] if e not in old["curation_history"]]
        assert len(additions) == 1
        event = additions[0]
        assert [e for e in new["curation_history"] if e != event] == old["curation_history"]
        assert event["action"] == "SOURCE_PARENT_EXCLUDED"
        assert event["timestamp"] == "2026-10-10T00:00:00Z"
        assert event["curator"] == "codex-gpt-5"
        assert identifier in event["changes"] and removed in event["changes"]
        assert path in event["changes"] and exclusion.notes in event["changes"]
        allowed = {"parent_habitats", "curation_history"}
        assert {k: v for k, v in new.items() if k not in allowed} == {
            k: v for k, v in old.items() if k not in allowed
        }, identifier

        assert len(new["source_attestations"]) == 1
        attestation = new["source_attestations"][0]
        assert attestation["source"] == "GOLD"
        assert attestation["source_id"] == source_id
        assert attestation["source_path"] == path
        assert seed.mint("GOLD", path) == identifier
        assert attestation["mapping_predicate"] == "skos:narrowMatch"
        if count is None:
            assert "assertion_count" not in attestation
            assert "assertion_unit" not in attestation
        else:
            assert attestation["assertion_count"] == count
            assert attestation["assertion_unit"] == "ORGANISM"

    freshwater = "habitatmech:GOLD.44534a15ca"
    assert before[freshwater] == documents[freshwater]
    assert documents[freshwater]["parent_habitats"] == ["ENVO:00002007"]
    assert documents[freshwater]["source_attestations"][0]["assertion_count"] == 1
    assert documents[freshwater]["source_attestations"][0]["assertion_unit"] == "ORGANISM"


def test_item_decisions_change_only_the_two_resolved_sources(documents, monkeypatch):
    targets = {
        "habitatmech:GOLD.c483f43031": (
            "ENVO:00002197", "saline water aquarium", "ENVO:00010622",
            "gold.ecosystem:8027",
            "Engineered > Artificial ecosystem > Vivarium > Seawater aquarium", 2,
        ),
        "habitatmech:GOLD.68d650a84d": (
            "ENVO:01000621", "microcosm", "habitatmech:GOLD.0acae9a1a4",
            "gold.ecosystem:7950",
            "Engineered > Artificial ecosystem > Seawater microcosm", 3,
        ),
    }
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    baseline = dict(decisions)
    for identifier, (parent, label, *_rest) in targets.items():
        decision = decisions[identifier]
        assert decision.decision == "GROUND_AS_PARENT"
        assert decision.review_depth == "ITEM"
        assert decision.object_id == parent
        assert decision.object_label == label
        assert decision.grounding_status == "NARROW"
        assert decision.relation == "parent"
        assert decision.date == "2026-10-10"
        assert decision.curator == "codex-gpt-5"
        baseline[identifier] = replace(
            decision, decision="CONFIRM_UNGROUNDED", object_id="", object_label="",
            grounding_status="", review_depth="CLASS", curator="claude-opus-5",
            date="2026-08-12", notes="Unreviewed class-level baseline.",
        )
    monkeypatch.setattr(seed, "load_decisions", lambda _: baseline)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == documents.keys()
    assert {key for key in before if before[key] != documents[key]} == targets.keys()

    allowed = {"grounding_status", "mapping_status", "parent_habitats",
               "source_attestations", "curation_history"}
    for identifier, (parent, label, retained, source_id, path, node_count) in targets.items():
        old, new = before[identifier], documents[identifier]
        assert {k: v for k, v in new.items() if k not in allowed} == {
            k: v for k, v in old.items() if k not in allowed
        }, identifier
        assert old["grounding_status"] == "UNGROUNDED"
        assert old["mapping_status"] == "SEEDED"
        assert new["grounding_status"] == "NARROW"
        assert new["mapping_status"] == "REVIEWED"
        assert old["parent_habitats"] == [retained]
        assert new["parent_habitats"] == sorted([parent, retained])
        assert len(old["source_attestations"]) == len(new["source_attestations"]) == 1
        old_source, new_source = old["source_attestations"][0], new["source_attestations"][0]
        assert "mapping_predicate" not in old_source
        assert new_source == {**old_source, "mapping_predicate": "skos:narrowMatch"}
        assert new_source["source"] == "GOLD"
        assert new_source["source_id"] == source_id
        assert new_source["source_path"] == path
        assert seed.mint("GOLD", path) == identifier
        assert f"{node_count} GOLD ecosystem node ids" in new_source["notes"]
        assert "assertion_count" not in new_source and "assertion_unit" not in new_source
        assert "definition" not in new and "xrefs" not in new

        events = [e for e in new["curation_history"] if e["action"] == "GROUND_AS_PARENT"]
        assert len(events) == 1
        event = events[0]
        assert event["timestamp"] == "2026-10-10T00:00:00Z"
        assert event["curator"] == "codex-gpt-5"
        assert identifier in event["changes"] and parent in event["changes"]
        assert label in event["changes"] and decisions[identifier].notes in event["changes"]
        class_events = [e for e in old["curation_history"] if e["action"] == "CONFIRM_UNGROUNDED"]
        assert len(class_events) == 1
        assert "[CLASS-level]" in class_events[0]["changes"]
        assert not any(e["action"] == "CONFIRM_UNGROUNDED" for e in new["curation_history"])

        # ITEM replaces CLASS; the generated seed summary follows the new grounding.
        expected_history = []
        seed_events = [e for e in old["curation_history"] if e["action"] == "SEEDED_FROM_SOURCES"]
        assert len(seed_events) == 1
        for previous in old["curation_history"]:
            if previous in class_events:
                continue
            if previous in seed_events:
                assert previous["changes"] == (
                    "Seeded from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED."
                )
                previous = {
                    **previous,
                    "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NARROW.",
                }
            expected_history.append(previous)
        assert [e for e in new["curation_history"] if e != event] == expected_history

    freshwater = "habitatmech:GOLD.44534a15ca"
    assert before[freshwater] == documents[freshwater]
