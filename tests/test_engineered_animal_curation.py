"""Keep the reviewed component, ecosystem and qualified material scopes distinct."""

from dataclasses import replace

from habitatmech import seed


def test_anode_and_aquaculture_exclusions_preserve_other_claims(monkeypatch):
    anode = "habitatmech:GOLD.9b7ba22de1"
    farm_source = "habitatmech:GOLD.add1edcd6d"
    farm = "ENVO:03600074"
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = {
        key: row for key, row in seed.load_gold_parent_exclusions(
            seed.GOLD_PARENT_EXCLUSIONS_PATH
        ).items() if key not in {anode, farm_source}
    }
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda path: exclusions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {anode, farm}
    assert before[anode]["parent_habitats"] == ["habitatmech:GOLD.cdf0160423"]
    assert not after[anode].get("parent_habitats")
    assert before[farm]["parent_habitats"] == ["ENVO:00000077", "ENVO:01000964"]
    assert after[farm]["parent_habitats"] == ["ENVO:00000077"]
    for identifier in (anode, farm):
        old, new = before[identifier], after[identifier]
        assert new["curation_history"][:-1] == old["curation_history"]
        event = new["curation_history"][-1]
        assert event["action"] == "SOURCE_PARENT_EXCLUDED"
        assert event["timestamp"] == "2026-10-07T00:00:00Z"
        for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
            assert new.get(field) == old.get(field), (identifier, field)
    assert after[anode]["mapping_status"] == "SEEDED"
    assert after[anode]["grounding_status"] == "UNGROUNDED"
    assert after[farm]["mapping_status"] == "REVIEWED"
    assert len(after[farm]["characteristic_taxa"]) == 25
    assert after[farm]["source_attestations"][0]["assertion_count"] == 109
    assert after[farm]["source_attestations"][0]["assertion_unit"] == "STRAIN"


def test_solid_animal_waste_split_preserves_every_source_observation(monkeypatch):
    solid = "habitatmech:BACDIVE.a862e7c17e"
    generic = "ENVO:00002276"
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    decisions[solid] = replace(
        decisions[solid], decision="GROUND", grounding_status="EXACT",
        curator="claude-opus-5", date="2026-08-13", category="", notes=(
            "Solid animal waste is exactly ENVO's animal waste material; it was "
            "merged into the generic waste material class alongside plant and domestic waste."
        ),
    )
    monkeypatch.setattr(seed, "load_decisions", lambda path: decisions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert after.keys() - before.keys() == {solid}
    assert not before.keys() - after.keys()
    assert {key for key in before if before[key] != after[key]} == {generic}
    old, retained, separated = before[generic], after[generic], after[solid]
    assert separated["label"] == "Solid-animal-waste"
    assert separated["habitat_category"] == "ENGINEERED"
    assert separated["grounding_status"] == "NARROW"
    assert separated["mapping_status"] == "REVIEWED"
    assert separated["parent_habitats"] == [generic]
    assert not separated.get("definition")
    assert not separated.get("synonyms")
    old_bacdive = next(a for a in old["source_attestations"] if a["source"] == "BACDIVE")
    assert separated["source_attestations"] == [
        {**old_bacdive, "mapping_predicate": "skos:narrowMatch"}
    ]
    assert old_bacdive["assertion_count"] == 11
    assert old_bacdive["assertion_unit"] == "STRAIN"
    assert separated["characteristic_taxa"] == [
        taxon for taxon in old["characteristic_taxa"] if taxon["source"] == "BACDIVE"
    ]
    assert len(separated["characteristic_taxa"]) == 8
    assert retained["characteristic_taxa"] == [
        taxon for taxon in old["characteristic_taxa"] if taxon["source"] != "BACDIVE"
    ]
    assert len(retained["characteristic_taxa"]) == 10
    assert retained["source_attestations"] == [
        a for a in old["source_attestations"] if a["source"] != "BACDIVE"
    ]
    assert retained["synonyms"] == [s for s in old["synonyms"] if s["source"] != "BacDive"]
    allowed = {"source_attestations", "characteristic_taxa", "synonyms", "curation_history"}
    for field in (old.keys() | retained.keys()) - allowed:
        assert retained.get(field) == old.get(field), field
    old_reviews = [e for e in old["curation_history"] if e["action"] == "REVIEW"]
    assert [e for e in retained["curation_history"] if e["action"] == "REVIEW"] == old_reviews
    assert [e["action"] for e in separated["curation_history"]] == [
        "SEEDED_FROM_SOURCES", "GROUND_AS_PARENT",
    ]
    assert separated["curation_history"][-1]["timestamp"] == "2026-10-07T00:00:00Z"
