"""Pore-water material retains its genus, not a denitrification context parent."""

from habitatmech import seed


def test_interstitial_exclusion_changes_only_context_parent_and_audit(monkeypatch):
    identifier = "ENVO:03600009"
    source_id = "habitatmech:GOLD.b099e463e2"
    parent = "habitatmech:GOLD.f07ee97491"
    source_path = (
        "Engineered > Bioreactor > Sulphur Autotrophic Denitrification > "
        "Interstitial water"
    )
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    exclusion = exclusions.pop(source_id)
    assert exclusion.source_path == source_path
    assert exclusion.parent_id == parent
    assert seed.mint("GOLD", source_path) == source_id
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda path: exclusions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {identifier}
    old, new = before[identifier], after[identifier]
    assert old["parent_habitats"] == ["ENVO:00002006", parent]
    assert new["parent_habitats"] == ["ENVO:00002006"]
    assert new["curation_history"][:-1] == old["curation_history"]
    event = new["curation_history"][-1]
    assert event["action"] == "SOURCE_PARENT_EXCLUDED"
    assert event["timestamp"] == "2026-10-09T00:00:00Z"
    assert event["curator"] == "codex-gpt-5"
    assert source_id in event["changes"]
    assert source_path in event["changes"]
    assert parent in event["changes"]
    for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
        assert new.get(field) == old.get(field), field
    assert new["label"] == "interstitial water"
    assert new["habitat_category"] == "ENGINEERED"
    assert new["grounding_status"] == "EXACT"
    assert new["mapping_status"] == "SEEDED"
    assert new["source_attestations"] == [{
        "source": "GOLD", "source_id": "gold.ecosystem:5661",
        "source_label": "Interstitial water", "source_path": source_path,
        "mapping_predicate": "skos:exactMatch",
        "notes": "2 GOLD ecosystem node ids share this path; first shown. "
                 "See data/raw/gold_ecosystem_paths.tsv.",
    }]
    row = next(row for row in seed.read_tsv(seed.RAW_DIR / "gold_ecosystem_paths.tsv")
               if row["canonical_path"] == source_path)
    assert row["gold_node_ids"] == "gold.ecosystem:5661|gold.ecosystem:5662"
    assert int(row["total_assertions"]) == 0
