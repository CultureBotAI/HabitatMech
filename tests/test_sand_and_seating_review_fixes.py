"""Scoped corrections from the sand, sequence and seating record reviews."""

from dataclasses import replace

import pytest

from habitatmech import seed


@pytest.fixture(scope="module")
def documents():
    return {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}


def test_context_exclusions_preserve_all_other_claims(documents, monkeypatch):
    targets = {
        "habitatmech:GOLD.94b0ed7936": (
            "habitatmech:GOLD.94b0ed7936", "ENVO:01000965", [], "gold.ecosystem:5595",
        ),
        "ENVO:00002055": (
            "habitatmech:GOLD.08c61f0426", "habitatmech:GOLD.8c6192908f",
            ["ENVO:01000271"], "gold.ecosystem:7127",
        ),
        "habitatmech:GOLD.2934cf4eee": (
            "habitatmech:GOLD.2934cf4eee", "habitatmech:GOLD.2d40c87aeb", [],
            "gold.ecosystem:8306",
        ),
        "habitatmech:GOLD.2b85027dc1": (
            "habitatmech:GOLD.2b85027dc1", "ENVO:03600051", [], "gold.ecosystem:5577",
        ),
    }
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    sources = {values[0] for values in targets.values()}
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda _: {
        key: value for key, value in exclusions.items() if key not in sources
    })
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == documents.keys()
    assert {key for key in before if before[key] != documents[key]} == targets.keys()
    for identifier, (source, removed, retained, source_id) in targets.items():
        old, new = before[identifier], documents[identifier]
        assert old["parent_habitats"] == sorted([removed, *retained])
        assert new.get("parent_habitats", []) == retained
        additions = [e for e in new["curation_history"] if e not in old["curation_history"]]
        assert len(additions) == 1
        event = additions[0]
        assert [e for e in new["curation_history"] if e != event] == old["curation_history"]
        assert event["action"] == "SOURCE_PARENT_EXCLUDED"
        assert event["timestamp"] == "2026-10-10T00:00:00Z"
        assert event["curator"] == "codex-gpt-5"
        assert source in event["changes"] and removed in event["changes"]
        for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
            assert new.get(field) == old.get(field), (identifier, field)
        attestation = next(a for a in new["source_attestations"] if a["source"] == "GOLD")
        assert attestation["source_id"] == source_id
        assert seed.mint("GOLD", attestation["source_path"]) == source
        assert attestation["source_path"] == exclusions[source].source_path
        assert exclusions[source].parent_id == removed
        if identifier != "ENVO:00002055":
            assert new["grounding_status"] == "UNGROUNDED"
            assert new["mapping_status"] == "SEEDED"
            assert "assertion_count" not in attestation
            assert "assertion_unit" not in attestation
        else:
            assert new["grounding_status"] == "EXACT"
            assert new["mapping_status"] == "REVIEWED"
            assert attestation["assertion_count"] == 1
            assert attestation["assertion_unit"] == "ORGANISM"
            assert len(new["characteristic_taxa"]) == 17
            assert new["source_attestations"][1]["assertion_unit"] == "TAXON"


def test_item_decisions_change_only_the_two_resolved_sources(documents, monkeypatch):
    microcosm = "habitatmech:GOLD.14789d9032"
    sanger = "habitatmech:GOLD.68f3852be5"
    targets = {microcosm, sanger}
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    for identifier in targets:
        assert decisions[identifier].review_depth == "ITEM"
        decisions[identifier] = replace(
            decisions[identifier], decision="CONFIRM_UNGROUNDED", object_id="",
            object_label="", grounding_status="", review_depth="CLASS",
            curator="test", date="2026-08-12", notes="Unreviewed class-level baseline.",
        )
    monkeypatch.setattr(seed, "load_decisions", lambda _: decisions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == documents.keys()
    assert {key for key in before if before[key] != documents[key]} == targets
    allowed = {"grounding_status", "mapping_status", "parent_habitats",
               "source_attestations", "curation_history"}
    for identifier in targets:
        old, new = before[identifier], documents[identifier]
        for field in (old.keys() | new.keys()) - allowed:
            assert new.get(field) == old.get(field), (identifier, field)
        assert old["grounding_status"] == "UNGROUNDED"
        assert old["mapping_status"] == "SEEDED"
        assert new["mapping_status"] == "REVIEWED"
        assert len(new["source_attestations"]) == 1
        old_source, new_source = old["source_attestations"][0], new["source_attestations"][0]
        assert {k: v for k, v in new_source.items() if k != "mapping_predicate"} == old_source
        assert seed.mint("GOLD", new_source["source_path"]) == identifier
        assert "assertion_count" not in new_source and "assertion_unit" not in new_source
        assert "definition" not in new and "xrefs" not in new
        events = [e for e in new["curation_history"] if e["curator"] == "codex-gpt-5"]
        assert len(events) == 1
        assert events[0]["timestamp"] == "2026-10-10T00:00:00Z"
        assert identifier in events[0]["changes"]
        assert events[0]["action"] == (
            "GROUND_AS_PARENT" if identifier == microcosm else "NOT_APPLICABLE"
        )
    assert documents[microcosm]["grounding_status"] == "NARROW"
    assert documents[microcosm]["parent_habitats"] == [
        "ENVO:01000621", "habitatmech:GOLD.0acae9a1a4",
    ]
    assert documents[microcosm]["source_attestations"][0]["source_id"] == "gold.ecosystem:5872"
    assert "3 GOLD ecosystem node ids" in documents[microcosm]["source_attestations"][0]["notes"]
    assert documents[sanger]["grounding_status"] == "NOT_APPLICABLE"
    assert documents[sanger]["parent_habitats"] == before[sanger]["parent_habitats"]
    assert documents[sanger]["source_attestations"] == before[sanger]["source_attestations"]
    assert documents[sanger]["source_attestations"][0]["source_id"] == "gold.ecosystem:3872"
    assert "2 GOLD ecosystem node ids" in documents[sanger]["source_attestations"][0]["notes"]
