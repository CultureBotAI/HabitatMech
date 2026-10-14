"""Exact source-context exclusions must preserve every unrelated corpus claim."""

from habitatmech import seed

REPAIRS = {
    "FOODON:03306632": (
        "habitatmech:GOLD.84d2657848", "FOODON:03530206", ["FOODON:00001172"],
    ),
    "habitatmech:GOLD.d6e78c89e8": (
        "habitatmech:GOLD.d6e78c89e8", "FOODON:03530206", [],
    ),
    "habitatmech:GOLD.30043c5bd8": (
        "habitatmech:GOLD.30043c5bd8", "habitatmech:GOLD.0d60ee305c", [],
    ),
    "habitatmech:GOLD.aff0c7b92a": (
        "habitatmech:GOLD.aff0c7b92a", "FOODON:03530206", [],
    ),
    "habitatmech:GOLD.43005e4de2": (
        "habitatmech:GOLD.43005e4de2", "FOODON:00001006", [],
    ),
}


def test_five_exclusions_change_only_immediate_parents_and_history(monkeypatch):
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    sources = {values[0] for values in REPAIRS.values()}
    assert sources <= exclusions.keys()
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda _: {
        key: row for key, row in exclusions.items() if key not in sources
    })
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == set(REPAIRS)
    for identifier, (source, removed, retained) in REPAIRS.items():
        old, new = before[identifier], after[identifier]
        assert old["parent_habitats"] == sorted([removed, *retained])
        assert new.get("parent_habitats", []) == retained
        assert exclusions[source].parent_id == removed
        assert seed.mint("GOLD", exclusions[source].source_path) == source
        assert new["source_attestations"][0]["source_path"] == exclusions[source].source_path
        added = [event for event in new["curation_history"] if event not in old["curation_history"]]
        assert len(added) == 1
        event = added[0]
        assert event["action"] == "SOURCE_PARENT_EXCLUDED"
        assert event["curator"] == "codex-gpt-5"
        assert event["timestamp"] == "2026-10-14T00:00:00Z"
        assert source in event["changes"] and removed in event["changes"]
        assert [item for item in new["curation_history"] if item != event] == old["curation_history"]
        allowed = {"parent_habitats", "curation_history"}
        assert {k: v for k, v in old.items() if k not in allowed} == {
            k: v for k, v in new.items() if k not in allowed
        }

    # Distinct source scopes and open findings are not silently fixed by an exclusion.
    assert after["habitatmech:GOLD.30043c5bd8"]["mapping_status"] == "SEEDED"
    assert after["habitatmech:GOLD.30043c5bd8"]["habitat_category"] == "FOOD"
    assert after["habitatmech:GOLD.cdf0825f85"]["parent_habitats"] == ["ENVO:01000001"]
    raw_milk = after["habitatmech:GOLD.d750ff157a"]
    assert raw_milk["source_attestations"][0]["mapping_predicate"] == "skos:narrowMatch"
