"""Keep clinical source identity and GOLD containment out of broader claims."""

from dataclasses import replace

import pytest

from habitatmech import seed

MEDICAL = "habitatmech:BACDIVE.5e52ea1bba"
HOSPITAL = "ENVO:00002173"
HAY = "ENVO:00002869"
BEDROOM = "habitatmech:GOLD.9cc7667041"
EXCLUSIONS = {
    "habitatmech:GOLD.162c34f9a7": (HAY, "habitatmech:GOLD.e292616707"),
    BEDROOM: (BEDROOM, HOSPITAL),
}


@pytest.fixture(scope="module")
def corpus():
    return seed.build_corpus()


def test_hay_and_bedroom_exclusions_preserve_all_other_claims(corpus, monkeypatch):
    after = {c.identifier: seed.build_document(c) for c in corpus.concepts}
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    monkeypatch.setattr(
        seed, "load_gold_parent_exclusions",
        lambda path: {key: row for key, row in exclusions.items() if key not in EXCLUSIONS},
    )
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {HAY, BEDROOM}
    for source, (target, parent) in EXCLUSIONS.items():
        old, new = before[target], after[target]
        assert set(new.get("parent_habitats", [])) == set(old["parent_habitats"]) - {parent}
        assert new["curation_history"][:-1] == old["curation_history"]
        event = new["curation_history"][-1]
        assert event["action"] == "SOURCE_PARENT_EXCLUDED"
        assert event["timestamp"] == "2026-10-08T00:00:00Z"
        assert event["curator"] == "codex-gpt-5"
        assert source in event["changes"] and parent in event["changes"]
        for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
            assert old.get(field) == new.get(field), (target, field)
        assert new["mapping_status"] == "SEEDED"
        attestation, = new["source_attestations"]
        assert seed.mint("GOLD", attestation["source_path"]) == source
        assert exclusions[source].source_path == attestation["source_path"]
        assert exclusions[source].parent_id == parent
    hay = after[HAY]
    assert hay["parent_habitats"] == ["ENVO:0010003"]
    assert hay["grounding_status"] == "EXACT"
    assert hay["source_attestations"][0]["assertion_count"] == 3
    assert hay["source_attestations"][0]["assertion_unit"] == "ORGANISM"
    bedroom = after[BEDROOM]
    assert "parent_habitats" not in bedroom
    assert bedroom["grounding_status"] == "UNGROUNDED"
    assert bedroom["source_attestations"] == [{
        "source": "GOLD", "source_id": "gold.ecosystem:5489",
        "source_label": "Hospital bedroom",
        "source_path": "Engineered > Built environment > Hospital > Hospital bedroom",
    }]


def test_medical_environment_split_preserves_source_evidence(corpus, monkeypatch):
    after = {c.identifier: seed.build_document(c) for c in corpus.concepts}
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    decision = decisions[MEDICAL]
    assert decision.decision == "CONFIRM_UNGROUNDED"
    assert decision.review_depth == "ITEM"
    assert not decision.object_id and not decision.grounding_status
    decisions[MEDICAL] = replace(
        decision, decision="GROUND", object_id=HOSPITAL, object_label="hospital",
        grounding_status="NARROW", category="", curator="claude-opus-5", date="2026-08-12",
        notes=(
            "Medical-environment covers hospitals plus clinics and other care settings, "
            "so ENVO:00002173 hospital is narrower than the source concept. Best available; "
            "a generic healthcare-facility environment term would be better."
        ),
    )
    monkeypatch.setattr(seed, "load_decisions", lambda path: decisions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert after.keys() - before.keys() == {MEDICAL}
    assert not before.keys() - after.keys()
    assert {key for key in before if before[key] != after[key]} == {HOSPITAL}
    old, hospital, medical = before[HOSPITAL], after[HOSPITAL], after[MEDICAL]
    for field in (old.keys() | hospital.keys()) - {
        "source_attestations", "characteristic_taxa", "synonyms", "curation_history",
    }:
        assert hospital.get(field) == old.get(field), field
    assert hospital["grounding_status"] == "EXACT"
    assert hospital["mapping_status"] == "REVIEWED"
    assert hospital["parent_habitats"] == ["ENVO:03501134", "mesh:D000076624"]
    assert hospital["source_attestations"] == [
        a for a in old["source_attestations"] if a["source"] != "BACDIVE"
    ]
    assert [(a["source"], a["assertion_count"], a["assertion_unit"])
            for a in hospital["source_attestations"]] == [
        ("GOLD", 551, "ORGANISM"), ("PREGO", 6, "TAXON"),
    ]
    assert hospital["synonyms"] == [s for s in old["synonyms"] if s["source"] != "BacDive"]
    assert hospital["characteristic_taxa"] == [
        t for t in old["characteristic_taxa"] if t["source"] == "PREGO"
    ]
    assert len(hospital["characteristic_taxa"]) == 6
    assert medical["label"] == "Medical-environment"
    assert medical["habitat_category"] == "CLINICAL"
    assert medical["grounding_status"] == "UNGROUNDED"
    assert medical["mapping_status"] == "REVIEWED"
    assert all(key not in medical for key in ("parent_habitats", "xrefs", "definition", "synonyms"))
    old_attestation, = [a for a in old["source_attestations"] if a["source"] == "BACDIVE"]
    assert old_attestation["mapping_predicate"] == "skos:narrowMatch"
    assert medical["source_attestations"] == [{
        key: value for key, value in old_attestation.items() if key != "mapping_predicate"
    }]
    assert medical["source_attestations"][0]["assertion_count"] == 438
    assert medical["source_attestations"][0]["assertion_unit"] == "STRAIN"
    assert medical["characteristic_taxa"] == [
        t for t in old["characteristic_taxa"] if t["source"] == "BACDIVE"
    ]
    assert len(medical["characteristic_taxa"]) == 25
    assert {t["candidate_pool"] for t in medical["characteristic_taxa"]} == {269}
    assert not any("is_characteristic" in t for t in medical["characteristic_taxa"])
    assert all(MEDICAL not in e["changes"] for e in hospital["curation_history"])
    event = medical["curation_history"][-1]
    assert event["action"] == "CONFIRM_UNGROUNDED" and MEDICAL in event["changes"]
    assert event["timestamp"] == "2026-10-08T00:00:00Z"
