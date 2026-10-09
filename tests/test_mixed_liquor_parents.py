"""Mixed liquor is material in treatment equipment, not a type of equipment."""

from habitatmech import seed


def test_mixed_liquor_exclusions_preserve_every_other_claim(monkeypatch):
    targets = {
        "habitatmech:GOLD.904cce6b84": ("ENVO:03600010", "gold.ecosystem:8158", 2),
        "habitatmech:GOLD.ef87a64b1a": ("ENVO:00002043", "gold.ecosystem:5789", 3),
    }
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    monkeypatch.setattr(
        seed, "load_gold_parent_exclusions",
        lambda path: {key: row for key, row in exclusions.items() if key not in targets},
    )
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == targets.keys()
    for identifier, (parent, source_id, nodes) in targets.items():
        old, new = before[identifier], after[identifier]
        assert old["parent_habitats"] == [parent]
        assert "parent_habitats" not in new
        assert new["curation_history"][:-1] == old["curation_history"]
        event = new["curation_history"][-1]
        assert event["action"] == "SOURCE_PARENT_EXCLUDED"
        assert event["timestamp"] == "2026-10-09T00:00:00Z"
        assert event["curator"] == "codex-gpt-5"
        assert identifier in event["changes"] and parent in event["changes"]
        for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
            assert new.get(field) == old.get(field), (identifier, field)
        assert new["grounding_status"] == "UNGROUNDED"
        assert new["mapping_status"] == "SEEDED"
        assert new["habitat_category"] == "ENGINEERED"
        assert len(new["source_attestations"]) == 1
        source = new["source_attestations"][0]
        assert source["source_id"] == source_id
        assert seed.mint("GOLD", source["source_path"]) == identifier
        assert source["source_path"] == exclusions[identifier].source_path
        assert exclusions[identifier].parent_id == parent
        assert f"{nodes} GOLD ecosystem node ids" in source["notes"]
        for field in ("assertion_count", "assertion_unit", "mapping_predicate"):
            assert field not in source
