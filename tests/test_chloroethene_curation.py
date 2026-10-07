"""Chemical-indexed source context does not establish habitat subsumption."""

from habitatmech import seed


def test_chloroethene_exclusion_changes_only_parent_and_audit(monkeypatch):
    identifier = "habitatmech:GOLD.9c0c555f09"
    parent = "habitatmech:GOLD.063960efcc"
    child = "habitatmech:GOLD.b4b6e9b05c"
    path = "Engineered > Bioremediation > Tetrachloroethylene and derivatives > Chloroethene"
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
    assert not new.get("parent_habitats")
    assert new["curation_history"][:-1] == old["curation_history"]
    event = new["curation_history"][-1]
    assert event["action"] == "SOURCE_PARENT_EXCLUDED"
    assert event["timestamp"] == "2026-10-07T00:00:00Z"
    assert event["curator"] == "codex-gpt-5"
    assert identifier in event["changes"]
    assert parent in event["changes"]
    for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
        assert new.get(field) == old.get(field), field
    assert new["label"] == "Chloroethene"
    assert new["habitat_category"] == "ENGINEERED"
    assert new["grounding_status"] == "UNGROUNDED"
    assert new["mapping_status"] == "SEEDED"
    assert len(new["source_attestations"]) == 1
    attestation = new["source_attestations"][0]
    assert attestation["source_id"] == "gold.ecosystem:3862"
    assert attestation["source_label"] == "Chloroethene"
    assert attestation["source_path"] == path
    for field in ("assertion_count", "assertion_unit", "mapping_predicate"):
        assert field not in attestation
    assert "2 GOLD ecosystem node ids" in attestation["notes"]
    assert seed.mint("GOLD", path) == identifier
    row = next(row for row in seed.read_tsv(seed.RAW_DIR / "gold_ecosystem_paths.tsv")
               if row["canonical_path"] == path)
    assert set(row["gold_node_ids"].split("|")) == {
        "gold.ecosystem:3862", "gold.ecosystem:4298",
    }
    assert after[child] == before[child]
    assert identifier in after[child]["parent_habitats"]
    assert after[parent] == before[parent]
    assert after["ENVO:00000856"] == before["ENVO:00000856"]
