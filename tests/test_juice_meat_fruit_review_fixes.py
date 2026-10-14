"""Scoped genus repairs must preserve source assertions and unrelated records."""

from dataclasses import replace

from habitatmech import seed

FRUIT = "habitatmech:BACDIVE.ba016fe448"
PARENTS = {
    "habitatmech:GOLD.76339b995e": (
        "habitatmech:GOLD.76339b995e", "habitatmech:GOLD.40c1d45ca3", [],
    ),
    "BTO:0000659": ("habitatmech:GOLD.15460dfe60", "FOODON:00003202", []),
    "FOODON:00001006": (
        "habitatmech:GOLD.0347e0d978", "FOODON:03530206",
        ["FOODON:00001092", "FOODON:00005501"],
    ),
}


def test_four_scoped_fixes_preserve_source_claims_and_unrelated_corpus(monkeypatch):
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    sources = {values[0] for values in PARENTS.values()}
    assert sources <= exclusions.keys()
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda _: {
        key: row for key, row in exclusions.items() if key not in sources
    })
    old_fruit = replace(
        decisions[FRUIT], decision="GROUND_AS_PARENT", object_id="FOODON:00001015",
        object_label="plant food product", grounding_status="NARROW", category="FOOD",
        curator="claude-opus-5", date="2026-08-16",
        notes="Counterfactual restoration of the reviewed unsupported food genus.",
    )
    monkeypatch.setattr(seed, "load_decisions", lambda _: {**decisions, FRUIT: old_fruit})
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {*PARENTS, FRUIT}
    for identifier, (source, removed, retained) in PARENTS.items():
        old, new = before[identifier], after[identifier]
        assert old["parent_habitats"] == sorted([removed, *retained])
        assert new.get("parent_habitats", []) == retained
        allowed = {"parent_habitats", "curation_history"}
        assert {k: v for k, v in old.items() if k not in allowed} == {
            k: v for k, v in new.items() if k not in allowed
        }
        added = [e for e in new["curation_history"] if e not in old["curation_history"]]
        assert len(added) == 1
        assert [e for e in new["curation_history"] if e not in added] == old["curation_history"]
        assert added[0]["action"] == "SOURCE_PARENT_EXCLUDED"
        assert added[0]["curator"] == "codex-gpt-5"
        assert added[0]["timestamp"] == "2026-10-14T00:00:00Z"
        assert seed.mint("GOLD", exclusions[source].source_path) == source
        assert exclusions[source].parent_id == removed

    old, new = before[FRUIT], after[FRUIT]
    assert old["parent_habitats"] == ["FOODON:00001015"]
    assert not new.get("parent_habitats")
    assert new["habitat_category"] == "OTHER"
    assert new["grounding_status"] == "UNGROUNDED"
    assert old["mapping_status"] == new["mapping_status"] == "REVIEWED"
    old_source, new_source = old["source_attestations"][0], new["source_attestations"][0]
    assert old_source["mapping_predicate"] == "skos:narrowMatch"
    assert "mapping_predicate" not in new_source
    assert {k: v for k, v in old_source.items() if k != "mapping_predicate"} == new_source
    assert new_source["assertion_count"] == 228
    assert new_source["assertion_unit"] == "STRAIN"
    assert len(new["characteristic_taxa"]) == 25
    assert all(t["candidate_pool"] == 157 for t in new["characteristic_taxa"])
    allowed = {"parent_habitats", "curation_history", "habitat_category",
               "grounding_status", "source_attestations"}
    assert {k: v for k, v in old.items() if k not in allowed} == {
        k: v for k, v in new.items() if k not in allowed
    }
