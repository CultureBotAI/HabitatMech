"""Source-context repairs must not reinterpret unrelated habitats or specimens."""

from dataclasses import replace

from habitatmech import seed

ABDOMINAL = "habitatmech:GOLD.9c78e65e82"
GLAND = "habitatmech:GOLD.453b1756ab"
EXCLUDED = {
    "habitatmech:GOLD.5d784b0218": "habitatmech:GOLD.4b37ab4b76",
    "habitatmech:GOLD.d1d916a248": "habitatmech:GOLD.523243d1da",
    "habitatmech:GOLD.8423e76015": "habitatmech:GOLD.752ac1c5aa",
    ABDOMINAL: "BTO:0001782",
    "habitatmech:GOLD.f007734d4a": "habitatmech:GOLD.0191e307b9",
    "habitatmech:GOLD.6d1b8fc8fc": "habitatmech:GOLD.bcb2f8b7f3",
    "habitatmech:GOLD.9c459b5a33": "habitatmech:GOLD.e7296678c2",
    "habitatmech:GOLD.ef667faebd": "habitatmech:GOLD.4b37ab4b76",
    "habitatmech:GOLD.628407fcc7": "habitatmech:GOLD.4b37ab4b76",
    GLAND: "habitatmech:GOLD.fcc934bd13",
    "habitatmech:GOLD.70fd1acd87": "habitatmech:GOLD.4b37ab4b76",
    "habitatmech:GOLD.9c17a8a454": "habitatmech:GOLD.9bb307824f",
}


def test_repairs_change_only_twelve_reviewed_source_records(monkeypatch):
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    definitions = seed.load_curated_definitions(seed.CURATED_DEFINITIONS_PATH)
    assert exclusions.keys() >= EXCLUDED.keys()
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda _: {
        key: row for key, row in exclusions.items() if key not in EXCLUDED
    })
    monkeypatch.setattr(seed, "load_decisions", lambda _: {
        key: row for key, row in decisions.items() if key != ABDOMINAL
    })
    old_definition = replace(
        definitions[GLAND],
        definition="A reproductive gland which lies in the mantle cavity of a sexually mature "
        "female decapodiform cephalopod and contains epithelium-lined tubules whose lumina "
        "house a dense extracellular bacterial consortium that is environmentally acquired "
        "and discharged into egg jelly.",
        date="2026-09-10",
        notes="Definition authored from the record's committed deep-research report under "
        "research/habitats/, read in full; no new paid research was commissioned. The report "
        "interprets GOLD's Host-associated > Mollusca > Reproductive system > Accessory "
        "nidamental gland (ANG) leaf as the dissected cephalopod symbiotic reproductive "
        "organ, not the main nidamental gland, egg jelly coat, light organ, or mantle cavity. "
        "UBERON:0003937 'reproductive gland' is the tightest vendored genus; ENVO:01000162 "
        "'organ' is a true but coarser ENVO precedent for symbiont-housing organs, "
        "UBERON:0005398 'female reproductive gland' is tighter but unvendored, and "
        "CEPH:0000001 exactly names the organ in an inactive, unvendored ontology. ADD "
        "preserves GOLD's source-derived Mollusca reproductive-system parent while adding "
        "the anatomy genus.",
    )
    monkeypatch.setattr(seed, "load_curated_definitions", lambda _: {
        **definitions, GLAND: old_definition,
    })
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    assert before.keys() - after.keys() == {"mesh:D000038"}
    assert after.keys() - before.keys() == {ABDOMINAL}
    changed = {key for key in before.keys() & after.keys() if before[key] != after[key]}
    assert changed == EXCLUDED.keys() - {ABDOMINAL}
    for identifier in changed:
        old, new = before[identifier], after[identifier]
        removed = EXCLUDED[identifier]
        assert removed in old["parent_habitats"]
        assert new.get("parent_habitats", []) == [
            p for p in old["parent_habitats"] if p != removed
        ]
        allowed = {"parent_habitats", "curation_history"}
        if identifier == GLAND:
            allowed.add("definition")
        assert {k: v for k, v in old.items() if k not in allowed} == {
            k: v for k, v in new.items() if k not in allowed
        }
        event = next(e for e in new["curation_history"]
                     if e["action"] == "SOURCE_PARENT_EXCLUDED")
        assert event["timestamp"] == "2026-10-14T00:00:00Z"
        assert event["curator"] == "codex-gpt-5"
        assert identifier in event["changes"] and removed in event["changes"]
        source = new["source_attestations"][0]
        assert seed.mint("GOLD", source["source_path"]) == identifier
        assert exclusions[identifier].source_path == source["source_path"]
        assert exclusions[identifier].parent_id == removed

    old, new = before["mesh:D000038"], after[ABDOMINAL]
    assert new["grounding_status"] == "NARROW" and new["mapping_status"] == "REVIEWED"
    assert new["parent_habitats"] == ["mesh:D000038"]
    assert "mesh:D013492" not in new["parent_habitats"]
    expected = [dict(a) for a in old["source_attestations"]]
    expected[0]["mapping_predicate"] = "skos:narrowMatch"
    assert new["source_attestations"] == expected
    assert expected[0]["assertion_count"] == 4
    assert expected[0]["assertion_unit"] == "ORGANISM"
    assert expected[0]["source_id"] == "gold.ecosystem:6346"
    assert seed.load_lockfile()[ABDOMINAL] == "abscess__35b7623f"
    assert "mesh:D000038" not in seed.load_lockfile()

    assert after[GLAND]["parent_habitats"] == ["UBERON:0003937"]
    assert after[GLAND]["xrefs"] == ["CEPH:0000001"]
    assert "Developing glands can precede sexual maturity and dense colonization" in (
        after[GLAND]["definition"]
    )
    assert "mature glands can supply bacteria to egg jelly" in after[GLAND]["definition"]
    # Parent removal does not settle the two source-member interpretation questions.
    for identifier in ["habitatmech:GOLD.ef667faebd", "habitatmech:GOLD.628407fcc7"]:
        assert after[identifier]["grounding_status"] == "NOT_APPLICABLE"
        assert after[identifier]["mapping_status"] == "REVIEWED"
        assert "assertion_count" not in after[identifier]["source_attestations"][0]
        assert "assertion_unit" not in after[identifier]["source_attestations"][0]
