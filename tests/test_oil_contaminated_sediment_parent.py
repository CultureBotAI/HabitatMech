"""Oil-contaminated sediment is material, not a refinery building."""

from habitatmech import seed
from habitatmech.text_map_inputs import build_context, semantic_text


def test_sediment_exclusion_preserves_all_other_records_and_claims(monkeypatch):
    identifier = "habitatmech:GOLD.6e0c4e4356"
    parent = "ENVO:03600078"
    path = "Engineered > Built environment > Oil refinery > Oil-contaminated sediment"
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    assert exclusions[identifier].source_path == path
    assert exclusions[identifier].parent_id == parent
    assert seed.mint("GOLD", path) == identifier
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    monkeypatch.setattr(
        seed, "load_gold_parent_exclusions",
        lambda _: {key: row for key, row in exclusions.items() if key != identifier},
    )
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {identifier}
    context = build_context(seed.REPO_ROOT)
    assert {key for key in before
            if semantic_text(before[key], context) != semantic_text(after[key], context)} == {
        identifier,
    }
    old, new = before[identifier], after[identifier]
    assert old["parent_habitats"] == [parent]
    assert "parent_habitats" not in new
    assert new["curation_history"][:-1] == old["curation_history"]
    event = new["curation_history"][-1]
    assert event["action"] == "SOURCE_PARENT_EXCLUDED"
    assert event["timestamp"] == "2026-10-09T00:00:00Z"
    assert event["curator"] == "codex-gpt-5"
    assert identifier in event["changes"] and parent in event["changes"]
    for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
        assert new.get(field) == old.get(field), field
    assert new["grounding_status"] == "UNGROUNDED"
    assert new["mapping_status"] == "SEEDED"
    assert new["habitat_category"] == "ENGINEERED"
    source, = new["source_attestations"]
    assert source["source_id"] == "gold.ecosystem:5765"
    assert source["source_path"] == path
    assert source["assertion_count"] == 14
    assert source["assertion_unit"] == "ORGANISM"
    assert "2 GOLD ecosystem node ids" in source["notes"]
    assert "mapping_predicate" not in source
    row = next(row for row in seed.read_tsv("gold_ecosystem_paths.tsv")
               if row["canonical_path"] == path)
    assert row["gold_node_ids"].split("|") == ["gold.ecosystem:5765", "gold.ecosystem:5766"]
    assert seed.load_decisions(seed.DECISIONS_PATH)[identifier].review_depth == "CLASS"
