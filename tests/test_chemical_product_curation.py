"""A chemical product is not a subtype of its industrial-production context."""

from habitatmech import seed


def test_chemical_product_exclusion_preserves_genus_and_all_other_claims(monkeypatch):
    identifier = "ENVO:2000000"
    source = "habitatmech:GOLD.413b4cb862"
    parent = "habitatmech:GOLD.a744ade0d8"
    path = "Engineered > Industrial production > Chemical products"
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = {
        key: row for key, row in seed.load_gold_parent_exclusions(
            seed.GOLD_PARENT_EXCLUSIONS_PATH
        ).items() if key != source
    }
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda path: exclusions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {identifier}
    old, new = before[identifier], after[identifier]
    assert old["parent_habitats"] == ["ENVO:00003074", parent]
    assert new["parent_habitats"] == ["ENVO:00003074"]
    assert new["curation_history"][:-1] == old["curation_history"]
    event = new["curation_history"][-1]
    assert event["action"] == "SOURCE_PARENT_EXCLUDED"
    assert event["timestamp"] == "2026-10-07T00:00:00Z"
    assert event["curator"] == "codex-gpt-5"
    assert source in event["changes"]
    assert parent in event["changes"]
    for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
        assert new.get(field) == old.get(field), field
    assert new["label"] == "chemical product"
    assert new["definition_source"] == "ENVO"
    assert new["habitat_category"] == "ENGINEERED"
    assert new["grounding_status"] == "EXACT"
    assert new["mapping_status"] == "REVIEWED"
    assert len(new["source_attestations"]) == 1
    attestation = new["source_attestations"][0]
    assert attestation["source_id"] == "gold.ecosystem:5579"
    assert attestation["source_label"] == "Chemical products"
    assert attestation["source_path"] == path
    assert attestation["assertion_count"] == 10
    assert attestation["assertion_unit"] == "ORGANISM"
    assert attestation["mapping_predicate"] == "skos:exactMatch"
    assert "3 GOLD ecosystem node ids" in attestation["notes"]
    assert seed.mint("GOLD", path) == source
    row = next(row for row in seed.read_tsv(seed.RAW_DIR / "gold_ecosystem_paths.tsv")
               if row["canonical_path"] == path)
    assert set(row["gold_node_ids"].split("|")) == {
        "gold.ecosystem:5579", "gold.ecosystem:5787", "gold.ecosystem:5788",
    }
