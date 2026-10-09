"""A park's city location is not an is-a relationship."""

from habitatmech import seed
from habitatmech.text_map_inputs import build_context, semantic_text


def test_park_exclusion_preserves_sources_taxa_and_other_records(monkeypatch):
    identifier = "ENVO:00000562"
    source_id = "habitatmech:GOLD.fc89e5f170"
    parent = "ENVO:00000856"
    path = "Engineered > Built environment > City > Park"
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    assert exclusions[source_id].source_path == path
    assert exclusions[source_id].parent_id == parent
    assert seed.mint("GOLD", path) == source_id
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    monkeypatch.setattr(
        seed, "load_gold_parent_exclusions",
        lambda _: {key: row for key, row in exclusions.items() if key != source_id},
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
    assert old["parent_habitats"] == ["ENVO:00000002", parent]
    assert new["parent_habitats"] == ["ENVO:00000002"]
    assert new["curation_history"][:-1] == old["curation_history"]
    event = new["curation_history"][-1]
    assert event["action"] == "SOURCE_PARENT_EXCLUDED"
    assert event["timestamp"] == "2026-10-09T00:00:00Z"
    assert event["curator"] == "codex-gpt-5"
    assert source_id in event["changes"] and parent in event["changes"]
    for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
        assert new.get(field) == old.get(field), field
    assert new["grounding_status"] == "EXACT"
    assert new["mapping_status"] == "REVIEWED"
    assert new["habitat_category"] == "ENGINEERED"
    gold, prego = new["source_attestations"]
    assert gold["source_id"] == "gold.ecosystem:4397"
    assert gold["source_path"] == path
    assert gold["mapping_predicate"] == "skos:exactMatch"
    assert "assertion_count" not in gold and "assertion_unit" not in gold
    assert "2 GOLD ecosystem node ids" in gold["notes"]
    assert prego["assertion_count"] == 8
    assert prego["assertion_unit"] == "TAXON"
    assert prego["score"] == 3.0
    assert prego["evidence_channels"] == "annotated_genomes_isolates"
    taxa = new["characteristic_taxa"]
    assert len(taxa) == 8
    assert [t["rank"] for t in taxa] == list(range(1, 9))
    assert all(t["score"] == 3.0 and t["candidate_pool"] == 8 for t in taxa)
    assert all("is_characteristic" not in t for t in taxa)
    assert taxa[2]["taxon_id"] == "NCBITaxon:1830138"
    assert "taxon_label" not in taxa[2]
    row = next(row for row in seed.read_tsv("gold_ecosystem_paths.tsv")
               if row["canonical_path"] == path)
    assert row["gold_node_ids"].split("|") == ["gold.ecosystem:4397", "gold.ecosystem:4398"]
    assert seed.load_decisions(seed.DECISIONS_PATH)[source_id].review_depth == "ITEM"
