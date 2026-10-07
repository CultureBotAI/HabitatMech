"""The cathode component is not a subtype of its complete fuel-cell system."""

from habitatmech import seed


def test_cathode_exclusion_changes_only_its_context_parent_and_audit(monkeypatch):
    identifier = "habitatmech:GOLD.5d36b86f15"
    parent = "habitatmech:GOLD.cdf0160423"
    path = "Engineered > Bioreactor > Microbial fuel cells/MFC > Cathode"
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = {
        key: row for key, row in seed.load_gold_parent_exclusions(
            seed.GOLD_PARENT_EXCLUSIONS_PATH
        ).items() if key != identifier
    }
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda path: exclusions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {identifier}
    old, new = before[identifier], after[identifier]
    assert old["parent_habitats"] == [parent]
    assert "parent_habitats" not in new
    assert new["curation_history"][:-1] == old["curation_history"]
    event = new["curation_history"][-1]
    assert event["action"] == "SOURCE_PARENT_EXCLUDED"
    assert event["timestamp"] == "2026-10-07T00:00:00Z"
    assert event["curator"] == "codex-gpt-5"
    assert identifier in event["changes"]
    assert parent in event["changes"]
    for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
        assert new.get(field) == old.get(field), field
    assert new["label"] == "Cathode"
    assert new["habitat_category"] == "ENGINEERED"
    assert new["grounding_status"] == "UNGROUNDED"
    assert new["mapping_status"] == "SEEDED"
    assert len(new["source_attestations"]) == 1
    attestation = new["source_attestations"][0]
    assert attestation["source_id"] == "gold.ecosystem:7656"
    assert attestation["source_path"] == path
    assert "2 GOLD ecosystem node ids" in attestation["notes"]
    assert "assertion_count" not in attestation
    assert "assertion_unit" not in attestation
    assert "mapping_predicate" not in attestation
    assert seed.mint("GOLD", path) == identifier
    row = next(row for row in seed.read_tsv(seed.RAW_DIR / "gold_ecosystem_paths.tsv")
               if row["canonical_path"] == path)
    assert set(row["gold_node_ids"].split("|")) == {
        "gold.ecosystem:7656", "gold.ecosystem:7657",
    }
