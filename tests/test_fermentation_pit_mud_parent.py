"""Pit-lining mud is material, not a type of its containing vessel."""

from habitatmech import seed


def test_pit_mud_exclusion_preserves_other_records_and_claims(monkeypatch):
    identifier = "habitatmech:GOLD.cdf0825f85"
    parent = "ENVO:03600039"
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    monkeypatch.setattr(
        seed, "load_gold_parent_exclusions",
        lambda path: {key: row for key, row in exclusions.items() if key != identifier},
    )
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {identifier}
    old, new = before[identifier], after[identifier]
    assert old["parent_habitats"] == ["ENVO:01000001", parent]
    assert new["parent_habitats"] == ["ENVO:01000001"]
    assert new["curation_history"][:-1] == old["curation_history"]
    event = new["curation_history"][-1]
    assert event["action"] == "SOURCE_PARENT_EXCLUDED"
    assert event["timestamp"] == "2026-10-09T00:00:00Z"
    assert event["curator"] == "codex-gpt-5"
    assert identifier in event["changes"] and parent in event["changes"]
    for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
        assert new.get(field) == old.get(field), field
    assert new["grounding_status"] == "NARROW"
    assert new["mapping_status"] == "SEEDED"
    assert new["habitat_category"] == "ENGINEERED"
    assert len(new["source_attestations"]) == 1
    source = new["source_attestations"][0]
    assert source["source_id"] == "gold.ecosystem:5451"
    assert source["source_path"] == exclusions[identifier].source_path
    assert seed.mint("GOLD", source["source_path"]) == identifier
    assert exclusions[identifier].parent_id == parent
    assert "2 GOLD ecosystem node ids" in source["notes"]
    assert "assertion_count" not in source
    assert "assertion_unit" not in source
    # The independent endpoint-contract defect remains tracked in #1398.
    assert source["mapping_predicate"] == "skos:narrowMatch"
