from habitatmech import seed


def test_doormat_exclusion_changes_only_the_context_parent(monkeypatch):
    identifier = "habitatmech:GOLD.a50c61f322"
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    exclusion = exclusions.pop(identifier)
    assert exclusion.source_path == "Engineered > Built environment > House > Doormat"
    assert exclusion.parent_id == "ENVO:01000417"
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda path: exclusions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {identifier}
    old, new = before[identifier], after[identifier]
    assert old["parent_habitats"] == ["ENVO:01000417"]
    assert "parent_habitats" not in new
    assert new["curation_history"][:-1] == old["curation_history"]
    assert new["curation_history"][-1]["action"] == "SOURCE_PARENT_EXCLUDED"
    for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
        assert old.get(field) == new.get(field), field
    assert new["mapping_status"] == "SEEDED"
    assert new["grounding_status"] == "UNGROUNDED"
    source = new["source_attestations"][0]
    assert source["source_id"] == "gold.ecosystem:4846"
    assert source["source_path"] == exclusion.source_path
    assert "2 GOLD ecosystem node ids" in source["notes"]
    assert "assertion_count" not in source and "assertion_unit" not in source


def test_genus_scope_guard_has_two_current_consumers():
    docs = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    targets = {
        "habitatmech:GOLD.398aeb6c37": ("Dust", "house dust", "ENVO:00002008"),
        "habitatmech:GOLD.7f436f8aff": ("Biofilm", "scrubber biofilm", "ENVO:00002034"),
    }
    scoped = {
        identifier for identifier, doc in docs.items()
        if any(e["action"] == "SOURCE_SYNONYM_SCOPED" and "authored strict genus" in e["changes"]
               for e in doc["curation_history"])
    }
    assert scoped == targets.keys()
    for identifier, (source_label, exact_alias, parent) in targets.items():
        doc = docs[identifier]
        aliases = {(s["synonym_text"], s["synonym_type"]) for s in doc["synonyms"]}
        assert (source_label, "RELATED_SYNONYM") in aliases
        assert (source_label, "EXACT_SYNONYM") not in aliases
        assert (exact_alias, "EXACT_SYNONYM") in aliases
        assert doc["parent_habitats"] == [parent]
        assert doc["grounding_status"] == "UNGROUNDED"
        assert doc["mapping_status"] == "REVIEWED"
        assert doc["source_attestations"][0]["source_label"] == source_label
    dust = docs["habitatmech:GOLD.398aeb6c37"]
    assert all(s["synonym_text"] != "settled dust" for s in dust["synonyms"])
    source = dust["source_attestations"][0]
    assert source["assertion_count"] == 65 and source["assertion_unit"] == "ORGANISM"
    assert source["source_id"] == "gold.ecosystem:4619"
    assert source["source_path"] == "Environmental > Air > Indoor Air > Dust"
    assert "2 GOLD ecosystem node ids" in source["notes"]
    biofilm = docs["habitatmech:GOLD.7f436f8aff"]["source_attestations"][0]
    assert biofilm["source_id"] == "gold.ecosystem:5806"
    assert "assertion_count" not in biofilm and "assertion_unit" not in biofilm
