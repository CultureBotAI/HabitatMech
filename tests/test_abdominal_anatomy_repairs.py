"""Reviewed anatomy repairs stay scoped to their source concepts."""

from dataclasses import replace

from habitatmech import seed

PLEON = "habitatmech:GOLD.1e0a05a113"
INSECT = "habitatmech:GOLD.c6b0b54290"
LARVA = "habitatmech:GOLD.e02956e1eb"
LYMPH_NODE = "habitatmech:GOLD.1743ebf24f"
EXCLUSIONS = {PLEON, "habitatmech:GOLD.6c776ebafd"}
SCOPES = {
    "UBERON:0003684": {"cavitas abdominis"},
    "UBERON:0007358": {
        "fourth stomach", "maw", "read", "rennet-bag", "ruminant true stomach",
    },
}


def test_anatomy_repairs_preserve_every_unrelated_corpus_claim(monkeypatch):
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    corrections = seed.load_record_annotation_corrections(seed.RECORD_ANNOTATION_CORRECTIONS_PATH)
    assert exclusions.keys() >= EXCLUSIONS
    assert sum(c.identifier in SCOPES and c.item in SCOPES[c.identifier]
               for c in corrections) == 6

    original_decisions = {
        key: value for key, value in decisions.items() if key not in {INSECT, LARVA, LYMPH_NODE}
    }
    original_decisions[PLEON] = replace(
        decisions[PLEON], decision="GROUND", object_id="UBERON:0000916",
        object_label="abdomen", grounding_status="EXACT", curator="claude-opus-5",
        date="2026-08-12", notes="Slash alternative; pleon is the arthropod abdomen. "
        "Path: Host-associated > Arthropoda: Crustaceans > Whole body > Abdomen/Pleon",
    )
    monkeypatch.setattr(seed, "load_decisions", lambda _: original_decisions)
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda _: {
        key: value for key, value in exclusions.items() if key not in EXCLUSIONS
    })
    monkeypatch.setattr(seed, "load_record_annotation_corrections", lambda _: [
        c for c in corrections if c.identifier not in SCOPES or c.item not in SCOPES[c.identifier]
    ])
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    assert before.keys() - after.keys() == {"UBERON:0000916"}
    assert after.keys() - before.keys() == {PLEON}
    changed = {key for key in before.keys() & after.keys() if before[key] != after[key]}
    assert changed == {INSECT, LARVA, LYMPH_NODE, *SCOPES}
    expected_parents = {
        INSECT: ["habitatmech:GOLD.dba2a83b95"],
        LARVA: ["habitatmech:GOLD.1cbfc76870"],
        LYMPH_NODE: ["UBERON:0000029"],
        "UBERON:0003684": before["UBERON:0003684"]["parent_habitats"],
        "UBERON:0007358": ["UBERON:0011953"],
    }
    for identifier in changed:
        old, new = before[identifier], after[identifier]
        assert new["parent_habitats"] == expected_parents[identifier]
        allowed = {"parent_habitats", "curation_history"}
        if identifier in {INSECT, LARVA, LYMPH_NODE}:
            allowed |= {"grounding_status", "mapping_status", "source_attestations"}
            assert new["mapping_status"] == "REVIEWED"
            assert new["grounding_status"] == ("NARROW" if identifier == LYMPH_NODE else "UNGROUNDED")
            expected = [dict(a) for a in old["source_attestations"]]
            if identifier != LYMPH_NODE:
                for attestation in expected:
                    attestation.pop("mapping_predicate", None)
            assert new["source_attestations"] == expected
        if identifier in SCOPES:
            allowed.add("synonyms")
            expected = [dict(s) for s in old["synonyms"]]
            for synonym in expected:
                if synonym["synonym_text"] in SCOPES[identifier]:
                    assert synonym["source"] == "UBERON"
                    assert synonym["synonym_type"] == "EXACT_SYNONYM"
                    synonym["synonym_type"] = "RELATED_SYNONYM"
            assert new["synonyms"] == expected
        assert {k: v for k, v in old.items() if k not in allowed} == {
            k: v for k, v in new.items() if k not in allowed
        }
        assert any(e["curator"] == "codex-gpt-5" for e in new["curation_history"])

    old, new = before["UBERON:0000916"], after[PLEON]
    assert new["identifier"] == PLEON and new["label"] == "Abdomen/Pleon"
    assert new["grounding_status"] == "UNGROUNDED" and new["mapping_status"] == "REVIEWED"
    assert not new.get("parent_habitats")
    assert not new.get("definition") and not new.get("synonyms")
    expected = [dict(a) for a in old["source_attestations"]]
    for attestation in expected:
        attestation.pop("mapping_predicate", None)
    assert new["source_attestations"] == expected
    assert {e["action"] for e in new["curation_history"]} == {
        "CONFIRM_UNGROUNDED", "SOURCE_PARENT_EXCLUDED", "SEEDED_FROM_SOURCES",
    }

    # Do not "repair" uncertain PREGO associations or the valid fish genus by analogy.
    for identifier in ["BTO:0003167", "BTO:0002196", "BTO:0004041", "BTO:0000018",
                       "BTO:0000020", "habitatmech:GOLD.f9f745629a"]:
        assert after[identifier] == before[identifier]
