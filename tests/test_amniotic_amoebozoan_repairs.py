"""Keep fluid hierarchy and host-name repairs confined to three reviewed records."""

from dataclasses import replace

from habitatmech import seed

AMOEBOZOA = "habitatmech:GOLD.6a7bcba80d"
FLUID_PARENTS = {
    "habitatmech:GOLD.e29c7e3964": "habitatmech:GOLD.baffd7f6c7",
    "habitatmech:GOLD.73051a70cb": "habitatmech:GOLD.433d96f0dd",
}


def test_amniotic_and_amoebozoan_repairs_preserve_exact_corpus_scope(monkeypatch):
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    aliases = seed.load_definition_source_label_exclusions(
        seed.DEFINITION_SOURCE_LABEL_EXCLUSIONS_PATH
    )
    definitions = seed.load_curated_definitions(seed.CURATED_DEFINITIONS_PATH)
    assert FLUID_PARENTS.keys() <= exclusions.keys()
    assert AMOEBOZOA in aliases
    assert not definitions[AMOEBOZOA].exact_synonyms
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    with monkeypatch.context() as old:
        old.setattr(seed, "load_gold_parent_exclusions", lambda _: {
            key: row for key, row in exclusions.items() if key not in FLUID_PARENTS
        })
        old.setattr(seed, "load_definition_source_label_exclusions", lambda _: {
            key: row for key, row in aliases.items() if key != AMOEBOZOA
        })
        old.setattr(seed, "load_curated_definitions", lambda _: {
            **definitions, AMOEBOZOA: replace(definitions[AMOEBOZOA], exact_synonyms=("Amoebozoa",))
        })
        before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    assert before.keys() == after.keys()
    changed = {key for key in before if before[key] != after[key]}
    assert changed == FLUID_PARENTS.keys() | {AMOEBOZOA}
    for key in changed:
        old, new = before[key], after[key]
        allowed = {"parent_habitats", "curation_history"} if key in FLUID_PARENTS else {
            "synonyms", "curation_history"
        }
        assert {k: v for k, v in old.items() if k not in allowed} == {
            k: v for k, v in new.items() if k not in allowed
        }
        assert new["curation_history"][:-1] == old["curation_history"]
        expected_event = "SOURCE_PARENT_EXCLUDED" if key in FLUID_PARENTS else "SOURCE_SYNONYM_EXCLUDED"
        assert new["curation_history"][-1]["action"] == expected_event

    for key, parent in FLUID_PARENTS.items():
        assert before[key]["parent_habitats"] == ["UBERON:0000173", parent]
        assert after[key]["parent_habitats"] == ["UBERON:0000173"]
        assert after[key]["grounding_status"] == "NARROW"
        assert after[key]["mapping_status"] == "SEEDED"
        assert after[key]["source_attestations"][0]["mapping_predicate"] == "skos:narrowMatch"
    mammal = after["habitatmech:GOLD.e29c7e3964"]["source_attestations"][0]
    human = after["habitatmech:GOLD.73051a70cb"]["source_attestations"][0]
    assert "assertion_count" not in mammal
    assert human["assertion_count"] == 3 and human["assertion_unit"] == "ORGANISM"

    assert before[AMOEBOZOA]["synonyms"] == [{
        "synonym_text": "Amoebozoa", "synonym_type": "EXACT_SYNONYM", "source": "HabitatMech curation"
    }]
    assert not after[AMOEBOZOA].get("synonyms")
    assert after[AMOEBOZOA]["parent_habitats"] == ["ENVO:01001000", "habitatmech:GOLD.eee7408afd"]
    assert after[AMOEBOZOA]["mapping_status"] == "REVIEWED"
    first, second = after[AMOEBOZOA]["source_attestations"]
    assert first["assertion_count"] == 13 and first["assertion_unit"] == "ORGANISM"
    assert "assertion_count" not in second
    assert first["source_label"] == second["source_label"] == "Amoebozoa"

    # Clearing the authored synonym alone still invokes the old-label fallback.
    with monkeypatch.context() as fallback:
        fallback.setattr(seed, "load_definition_source_label_exclusions", lambda _: {
            key: row for key, row in aliases.items() if key != AMOEBOZOA
        })
        restored = next(c for c in seed.build_corpus().concepts if c.identifier == AMOEBOZOA)
        assert seed.build_document(restored)["synonyms"] == before[AMOEBOZOA]["synonyms"]

    repeated = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert repeated == after
