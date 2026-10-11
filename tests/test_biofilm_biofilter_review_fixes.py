"""Keep location, device and attached-material identities distinct."""

from dataclasses import replace

from habitatmech import seed


def test_six_biofilm_biofilter_exclusions_only_change_parent_and_audit(monkeypatch):
    targets = {
        "habitatmech:GOLD.4788e5d28f": ("ENVO:03600003", "ENVO:00002034", "5701"),
        "habitatmech:GOLD.905d58ea72": ("habitatmech:GOLD.b4e93f5d66", "ENVO:00002034", "8494"),
        "habitatmech:GOLD.6c12d05420": ("ENVO:00002124", "ENVO:00002034", "8156"),
        "habitatmech:GOLD.667125d07b": ("habitatmech:GOLD.c483f43031", "ENVO:00002034", "8042"),
        "habitatmech:GOLD.2aa590f12e": ("habitatmech:GOLD.95eace5af2", "ENVO:00002152", "8320"),
        "habitatmech:GOLD.c023583133": ("habitatmech:GOLD.2b5caaea9b", "ENVO:00002152", "8322"),
    }
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    assert targets.keys() <= exclusions.keys()
    monkeypatch.setattr(
        seed, "load_gold_parent_exclusions",
        lambda path: {key: row for key, row in exclusions.items() if key not in targets},
    )
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == targets.keys()
    for identifier, (removed, genus, node) in targets.items():
        old, new = before[identifier], after[identifier]
        assert old["parent_habitats"] == sorted([removed, genus])
        assert new["parent_habitats"] == [genus]
        assert new["curation_history"][:-1] == old["curation_history"]
        event = new["curation_history"][-1]
        assert event["action"] == "SOURCE_PARENT_EXCLUDED"
        assert event["curator"] == "codex-gpt-5"
        assert event["timestamp"] == "2026-10-11T00:00:00Z"
        assert identifier in event["changes"] and removed in event["changes"]
        for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
            assert old.get(field) == new.get(field), (identifier, field)
        assert new["mapping_status"] == "SEEDED"
        assert new["grounding_status"] == "NARROW"
        source = new["source_attestations"][0]
        assert source["source_id"] == "gold.ecosystem:" + node
        assert source["source_path"] == exclusions[identifier].source_path
        assert seed.mint("GOLD", source["source_path"]) == identifier
        assert source["mapping_predicate"] == "skos:narrowMatch"
        if identifier == "habitatmech:GOLD.2aa590f12e":
            assert source["assertion_count"] == 1 and source["assertion_unit"] == "ORGANISM"
        else:
            assert "assertion_count" not in source and "assertion_unit" not in source


def test_scrubber_biofilm_definition_requires_location_not_pollutant_metabolism(monkeypatch):
    identifier = "habitatmech:GOLD.7f436f8aff"
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    doc = after[identifier]
    assert doc["definition"] == "A biofilm which grows on an interior surface of an air scrubber."
    assert doc["parent_habitats"] == ["ENVO:00002034"]
    assert doc["mapping_status"] == "REVIEWED" and doc["grounding_status"] == "UNGROUNDED"
    aliases = {(s["synonym_text"], s["synonym_type"]) for s in doc["synonyms"]}
    assert ("Biofilm", "RELATED_SYNONYM") in aliases
    assert ("Biofilm", "EXACT_SYNONYM") not in aliases
    assert ("scrubber biofilm", "EXACT_SYNONYM") in aliases
    source = doc["source_attestations"][0]
    assert source["source_id"] == "gold.ecosystem:5806"
    assert source["source_path"] == "Environmental > Air > Indoor Air > Air scrubber > Biofilm"
    assert "assertion_count" not in source and "assertion_unit" not in source
    definitions = seed.load_curated_definitions(seed.CURATED_DEFINITIONS_PATH)
    assert definitions[identifier].parent_mode == "REPLACE"
    definitions[identifier] = replace(
        definitions[identifier],
        definition="A biofilm which grows on wetted packing, wall, or sump surfaces inside "
        "an air scrubber and is sustained by pollutants transferred from the treated gas "
        "stream into the scrubbing liquid.",
    )
    monkeypatch.setattr(seed, "load_curated_definitions", lambda path: definitions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {identifier}
    for field in doc.keys() | before[identifier].keys():
        if field != "definition":
            assert doc.get(field) == before[identifier].get(field), field
