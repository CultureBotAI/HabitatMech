"""Keep source classification context separate from habitat subsumption."""

from habitatmech import seed


def test_genetic_and_gowning_exclusions_preserve_every_other_claim(monkeypatch):
    targets = {
        "habitatmech:GOLD.ba9317369a": (
            "ENVO:01001405", "gold.ecosystem:3499", 100, "UNGROUNDED", "SEEDED",
        ),
        "habitatmech:GOLD.2eecc8ad2c": (
            "habitatmech:GOLD.77c5518fff", "gold.ecosystem:4386", 1704,
            "NOT_APPLICABLE", "REVIEWED",
        ),
        "habitatmech:GOLD.ec294980eb": (
            "habitatmech:GOLD.013b99db03", "gold.ecosystem:5485", None,
            "UNGROUNDED", "SEEDED",
        ),
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
    for identifier, (parent, source_id, count, grounding, status) in targets.items():
        old, new = before[identifier], after[identifier]
        assert old["parent_habitats"] == [parent]
        assert "parent_habitats" not in new
        assert new["curation_history"][:-1] == old["curation_history"]
        event = new["curation_history"][-1]
        assert event["action"] == "SOURCE_PARENT_EXCLUDED"
        assert event["timestamp"] == "2026-10-08T00:00:00Z"
        assert event["curator"] == "codex-gpt-5"
        assert identifier in event["changes"] and parent in event["changes"]
        for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
            assert new.get(field) == old.get(field), (identifier, field)
        assert new["grounding_status"] == grounding
        assert new["mapping_status"] == status
        assert new["habitat_category"] == "ENGINEERED"
        assert len(new["source_attestations"]) == 1
        source = new["source_attestations"][0]
        assert source["source_id"] == source_id
        assert seed.mint("GOLD", source["source_path"]) == identifier
        assert source["source_path"] == exclusions[identifier].source_path
        assert exclusions[identifier].parent_id == parent
        assert "mapping_predicate" not in source
        if count is None:
            assert "assertion_count" not in source and "assertion_unit" not in source
        else:
            assert source["assertion_count"] == count
            assert source["assertion_unit"] == "ORGANISM"
            assert "3 GOLD ecosystem node ids" in source["notes"]

    floor = after["habitatmech:GOLD.2b2e32d265"]
    assert floor == before[floor["identifier"]]
    assert "habitatmech:GOLD.ec294980eb" in floor["parent_habitats"]
