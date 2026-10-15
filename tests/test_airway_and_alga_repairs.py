"""Scoped airway and synonym repairs preserve frozen source claims."""

from dataclasses import replace

from habitatmech import seed

AIR_SAC = "UBERON:0009060"
TRACHEA = "habitatmech:GOLD.2a2774b70a"
INSECT_SAC = "habitatmech:GOLD.3982893194"
ALGA = "habitatmech:GOLD.02383c20a7"
EXCLUSIONS = {
    "habitatmech:GOLD.1dec05f10e": "habitatmech:GOLD.0c74807e42",
    "habitatmech:GOLD.9a9d51388c": "habitatmech:GOLD.0d343fdd03",
    "habitatmech:GOLD.a74e46ebe4": "habitatmech:GOLD.5bbc13545b",
    TRACHEA: "habitatmech:GOLD.867362bd5a",
}
CORRECTION = "air-sac-postcranial-synonym-scope"


def test_airway_and_alga_corrections_have_exact_five_record_scope(monkeypatch):
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    definitions = seed.load_curated_definitions(seed.CURATED_DEFINITIONS_PATH)
    corrections = seed.load_record_annotation_corrections(
        seed.RECORD_ANNOTATION_CORRECTIONS_PATH
    )
    assert EXCLUSIONS.keys() <= exclusions.keys()
    assert TRACHEA in decisions and decisions[TRACHEA].review_depth == "ITEM"
    assert not definitions[ALGA].exact_synonyms
    assert sum(c.correction_id == CORRECTION for c in corrections) == 1
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda _: {
        key: row for key, row in exclusions.items() if key not in EXCLUSIONS
    })
    monkeypatch.setattr(seed, "load_decisions", lambda _: {
        key: row for key, row in decisions.items() if key != TRACHEA
    })
    monkeypatch.setattr(seed, "load_curated_definitions", lambda _: {
        **definitions, ALGA: replace(definitions[ALGA], exact_synonyms=("Algae",))
    })
    monkeypatch.setattr(seed, "load_record_annotation_corrections", lambda _: [
        c for c in corrections if c.correction_id != CORRECTION
    ])
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    changed = {key for key in before if before[key] != after[key]}
    alveoli = {"habitatmech:GOLD.9a9d51388c", "habitatmech:GOLD.a74e46ebe4"}
    assert changed == alveoli | {AIR_SAC, TRACHEA, ALGA}
    for key in changed:
        old, new = before[key], after[key]
        allowed = {"parent_habitats", "synonyms", "curation_history", "mapping_status"}
        assert {k: v for k, v in old.items() if k not in allowed} == {
            k: v for k, v in new.items() if k not in allowed
        }
        assert all(event in new["curation_history"] for event in old["curation_history"])
        if key != TRACHEA:
            assert new["mapping_status"] == old["mapping_status"]
    for key in alveoli:
        assert after[key]["parent_habitats"] == ["UBERON:0002299"]
        assert before[key]["parent_habitats"] == ["UBERON:0002299", EXCLUSIONS[key]]
        assert after[key]["mapping_status"] == "SEEDED"
        assert after[key]["grounding_status"] == "NARROW"
        assert after[key]["source_attestations"] == before[key]["source_attestations"]
    assert "assertion_count" not in after["habitatmech:GOLD.9a9d51388c"]["source_attestations"][0]
    assert after["habitatmech:GOLD.a74e46ebe4"]["source_attestations"][0]["assertion_count"] == 1
    assert after[AIR_SAC]["parent_habitats"] == ["UBERON:0010000"]
    old_aliases = {s["synonym_text"]: s for s in before[AIR_SAC]["synonyms"]}
    new_aliases = {s["synonym_text"]: s for s in after[AIR_SAC]["synonyms"]}
    assert old_aliases.keys() == new_aliases.keys()
    assert new_aliases["psotcranial air sac"] == {
        **old_aliases["psotcranial air sac"], "synonym_type": "RELATED_SYNONYM"
    }
    for alias in ("Air sacs", "sacci pneumatici"):
        assert new_aliases[alias] == old_aliases[alias]
    assert before[TRACHEA]["parent_habitats"] == ["UBERON:0003126", EXCLUSIONS[TRACHEA]]
    assert after[TRACHEA]["parent_habitats"] == ["UBERON:0003127"]
    assert before[TRACHEA]["mapping_status"] == "SEEDED"
    assert after[TRACHEA]["mapping_status"] == "REVIEWED"
    assert after[TRACHEA]["grounding_status"] == "NARROW"
    assert after[INSECT_SAC] == before[INSECT_SAC]
    assert after[INSECT_SAC]["parent_habitats"] == ["UBERON:0003127", TRACHEA]
    assert not after[ALGA].get("synonyms")
    assert after[ALGA]["curation_history"] == before[ALGA]["curation_history"]
    assert after[ALGA]["xrefs"] == ["FOODON:03411301"]
    assert after[ALGA]["source_attestations"] == before[ALGA]["source_attestations"]
    assert len(after[ALGA]["characteristic_taxa"]) == 25
