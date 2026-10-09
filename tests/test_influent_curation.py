"""Incoming liquid is not a subtype of its receiving treatment plant."""

from habitatmech import seed


def test_influent_exclusion_changes_only_facility_parent_and_audit(monkeypatch):
    identifier = "habitatmech:GOLD.2bf3ab7d2f"
    parent = "ENVO:00002043"
    source_path = "Engineered > WWTP > Influent"
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    exclusion = exclusions.pop(identifier)
    assert exclusion.source_path == source_path
    assert exclusion.parent_id == parent
    assert seed.mint("GOLD", source_path) == identifier
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda path: exclusions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {identifier}
    old, new = before[identifier], after[identifier]
    assert old["parent_habitats"] == [parent]
    assert "parent_habitats" not in new
    assert new["curation_history"][:-1] == old["curation_history"]
    event = new["curation_history"][-1]
    assert event["action"] == "SOURCE_PARENT_EXCLUDED"
    assert event["timestamp"] == "2026-10-09T00:00:00Z"
    assert event["curator"] == "codex-gpt-5"
    assert identifier in event["changes"]
    assert source_path in event["changes"]
    assert parent in event["changes"]
    for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
        assert new.get(field) == old.get(field), field
    assert new["label"] == "Influent"
    assert new["habitat_category"] == "ENGINEERED"
    assert new["grounding_status"] == "UNGROUNDED"
    assert new["mapping_status"] == "SEEDED"
    assert new["source_attestations"] == [{
        "source": "GOLD", "source_id": "gold.ecosystem:6077",
        "source_label": "Influent", "source_path": source_path,
    }]
    row = next(row for row in seed.read_tsv(seed.RAW_DIR / "gold_ecosystem_paths.tsv")
               if row["canonical_path"] == source_path)
    assert row["gold_node_ids"] == "gold.ecosystem:6077"
    assert int(row["total_assertions"]) == 0
