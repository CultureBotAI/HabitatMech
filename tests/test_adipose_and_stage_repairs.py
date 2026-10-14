"""Scoped anatomy repairs preserve provenance and unrelated source concepts."""

from dataclasses import replace

from habitatmech import seed

ADENOID = "habitatmech:GOLD.b21e68a415"
ADULT = "habitatmech:PREGO.57e0a5faae"
ADIPOSE = {
    "habitatmech:GOLD.9ddd7a2cf6": "habitatmech:GOLD.d980919c41",
    "habitatmech:GOLD.7d70febb4c": "habitatmech:GOLD.968051b240",
    "habitatmech:GOLD.62b3ac2c20": "habitatmech:GOLD.dc86c8917c",
    "habitatmech:GOLD.6fe7c283e0": "habitatmech:GOLD.56e0776270",
}
ADRENAL = {
    "habitatmech:GOLD.e9371b4536": "habitatmech:GOLD.c26b92ece6",
    "habitatmech:GOLD.5b2265e44e": "habitatmech:GOLD.2f5a0b5455",
}


def test_anatomy_repairs_change_only_seven_source_records(monkeypatch):
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    definitions = seed.load_curated_definitions(seed.CURATED_DEFINITIONS_PATH)
    aliases = seed.load_definition_source_label_exclusions(
        seed.DEFINITION_SOURCE_LABEL_EXCLUSIONS_PATH
    )
    removed = ADIPOSE | ADRENAL
    assert exclusions.keys() >= removed.keys()
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda _: {
        key: row for key, row in exclusions.items() if key not in removed
    })
    original_adenoid = replace(
        decisions[ADENOID], object_id="BTO:0000777", object_label="adenoid",
        curator="claude-opus-5", date="2026-08-12",
        notes="Slash alternative; the pharyngeal tonsil is the adenoid. "
        "Path: Host-associated > Mammals: Human > Lymphatic system > Tonsils > Adenoi",
    )
    monkeypatch.setattr(seed, "load_decisions", lambda _: {
        **{key: row for key, row in decisions.items() if key != ADULT},
        ADENOID: original_adenoid,
    })
    monkeypatch.setattr(seed, "load_curated_definitions", lambda _: {
        key: row for key, row in definitions.items() if key != ADULT
    })
    monkeypatch.setattr(seed, "load_definition_source_label_exclusions", lambda _: {
        key: row for key, row in aliases.items() if key != ADULT
    })
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() - after.keys() == {"BTO:0000777", "BTO:0001043"}
    assert after.keys() - before.keys() == {"BTO:0004715", ADULT}
    changed = {key for key in before.keys() & after.keys() if before[key] != after[key]}
    assert changed == ADIPOSE.keys() | {"BTO:0000047"}
    for identifier in changed:
        old, new = before[identifier], after[identifier]
        parents = {ADIPOSE[identifier]} if identifier in ADIPOSE else set(ADRENAL.values())
        assert parents <= set(old["parent_habitats"])
        assert new["parent_habitats"] == [p for p in old["parent_habitats"] if p not in parents]
        allowed = {"parent_habitats", "curation_history"}
        assert {k: v for k, v in old.items() if k not in allowed} == {
            k: v for k, v in new.items() if k not in allowed
        }
        events = [e for e in new["curation_history"] if e["action"] == "SOURCE_PARENT_EXCLUDED"]
        assert len(events) == len(parents)
        for event in events:
            assert event["curator"] == "codex-gpt-5"
            assert event["timestamp"] == "2026-10-14T00:00:00Z"
        for attestation in new["source_attestations"]:
            if attestation["source"] == "GOLD":
                key = seed.mint("GOLD", attestation["source_path"])
                assert exclusions[key].source_path == attestation["source_path"]
                assert exclusions[key].parent_id == removed[key]

    for identifier in ADIPOSE:
        assert after[identifier]["parent_habitats"] == ["UBERON:0001013"]
        assert after[identifier]["grounding_status"] == "NARROW"
        assert after[identifier]["mapping_status"] == "SEEDED"
    assert after["BTO:0000047"]["parent_habitats"] == ["BTO:0001488", "BTO:0001491"]

    old, new = before["BTO:0000777"], after["BTO:0004715"]
    assert new["label"] == "nasopharyngeal tonsil"
    assert new["parent_habitats"] == ["BTO:0001387"]
    assert "obstruct" not in new["definition"] and "enlarged" not in new["definition"]
    assert new["source_attestations"] == old["source_attestations"]
    assert new["mapping_status"] == old["mapping_status"] == "REVIEWED"
    assert new["grounding_status"] == old["grounding_status"] == "EXACT"
    assert decisions[ADENOID].notes.endswith(new["source_attestations"][0]["source_path"])
    assert seed.load_lockfile()["BTO:0004715"] == "adenoid"

    old, new = before["BTO:0001043"], after[ADULT]
    assert new["label"] == "adult-associated environment"
    assert new["grounding_status"] == "UNGROUNDED" and new["mapping_status"] == "REVIEWED"
    assert new["parent_habitats"] == ["ENVO:01001000"]
    assert new["xrefs"] == ["BTO:0001043"]
    assert new["source_attestations"] == old["source_attestations"]
    assert new["characteristic_taxa"] == old["characteristic_taxa"]
    assert new["source_attestations"][0]["assertion_count"] == 378
    assert len(new["characteristic_taxa"]) == 25
    assert not any(s["synonym_type"] == "EXACT_SYNONYM" for s in new.get("synonyms", []))
    assert seed.load_lockfile()[ADULT] == "adult"
    assert "BTO:0001043" not in seed.load_lockfile()

    # The unresolved adenoma disposition is not silently promoted or reinterpreted.
    adenoma = after["habitatmech:GOLD.5dd1030108"]
    assert adenoma == before["habitatmech:GOLD.5dd1030108"]
    assert adenoma["mapping_status"] == "SEEDED"
    assert adenoma["grounding_status"] == "UNGROUNDED"
