"""Remove an unsupported habitat edge without deciding the GOLD source meaning."""

from habitatmech import seed


def test_anammox_exclusion_changes_only_parent_and_history(monkeypatch):
    identifier = "habitatmech:GOLD.d3e01e5908"
    parent = "habitatmech:GOLD.92b66873c0"
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    exclusion = exclusions[identifier]
    assert exclusion.source_path == (
        "Engineered > Wastewater > Nutrient removal > Nitrogen removal > Anammox"
    )
    assert exclusion.parent_id == parent
    assert seed.mint("GOLD", exclusion.source_path) == identifier
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda _: {
        key: row for key, row in exclusions.items() if key != identifier
    })
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {identifier}
    old, new = before[identifier], after[identifier]
    assert old["parent_habitats"] == [parent]
    assert not new.get("parent_habitats")
    for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
        assert new.get(field) == old.get(field), field
    additions = [event for event in new["curation_history"] if event not in old["curation_history"]]
    assert len(additions) == 1
    event = additions[0]
    assert event["action"] == "SOURCE_PARENT_EXCLUDED"
    assert event["timestamp"] == "2026-10-11T00:00:00Z"
    assert event["curator"] == "codex-gpt-5"
    assert identifier in event["changes"] and parent in event["changes"]
    assert "#1614" in event["changes"]
    assert [item for item in new["curation_history"] if item != event] == old["curation_history"]
    assert new["grounding_status"] == "NOT_APPLICABLE"
    assert new["mapping_status"] == "REVIEWED"
    assert new["source_attestations"] == [{
        "source": "GOLD", "source_id": "gold.ecosystem:4256", "source_label": "Anammox",
        "source_path": exclusion.source_path, "assertion_count": 1, "assertion_unit": "ORGANISM",
    }]
