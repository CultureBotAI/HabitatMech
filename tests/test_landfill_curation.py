"""A landfill landform is not a type of the waste material it contains."""

from habitatmech import seed
from habitatmech.text_map_inputs import semantic_text


def test_landfill_exclusion_changes_only_material_parent_and_audit(monkeypatch):
    identifier = "ENVO:00000533"
    source_id = "habitatmech:GOLD.baf1d9bbc6"
    path = "Engineered > Solid waste > Landfill"
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    exclusion = exclusions.pop(source_id)
    assert exclusion.source_path == path
    assert exclusion.parent_id == "mesh:D062611"
    assert seed.mint("GOLD", path) == source_id
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda _: exclusions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {identifier}
    old, new = before[identifier], after[identifier]
    assert old["parent_habitats"] == ["ENVO:00000309", "ENVO:01001884", "mesh:D062611"]
    assert new["parent_habitats"] == ["ENVO:00000309", "ENVO:01001884"]
    assert new["curation_history"][:-1] == old["curation_history"]
    event = new["curation_history"][-1]
    assert event["action"] == "SOURCE_PARENT_EXCLUDED"
    assert event["timestamp"] == "2026-10-09T00:00:00Z"
    assert event["curator"] == "codex-gpt-5"
    assert all(value in event["changes"] for value in (source_id, path, "mesh:D062611"))
    for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
        assert new.get(field) == old.get(field), field
    assert new["grounding_status"] == "EXACT"
    assert new["mapping_status"] == "REVIEWED"
    gold, prego = new["source_attestations"]
    assert gold == {
        "source": "GOLD", "source_id": "gold.ecosystem:3513",
        "source_label": "Landfill", "source_path": path,
        "mapping_predicate": "skos:exactMatch", "assertion_count": 30,
        "assertion_unit": "ORGANISM",
        "notes": "3 GOLD ecosystem node ids share this path; first shown. "
                 "See data/raw/gold_ecosystem_paths.tsv.",
    }
    assert prego == {
        "source": "PREGO", "source_id": identifier, "source_label": "landfill",
        "assertion_count": 5, "assertion_unit": "TAXON", "score": 4.0,
        "evidence_channels": "annotated_genomes_isolates",
    }
    taxa = new["characteristic_taxa"]
    assert [t["taxon_id"] for t in taxa] == [
        "NCBITaxon:1132443", "NCBITaxon:1385515", "NCBITaxon:1549639",
        "NCBITaxon:51173", "NCBITaxon:266265",
    ]
    assert [t["rank"] for t in taxa] == [1, 2, 3, 4, 5]
    assert [t["score"] for t in taxa] == [4.0, 4.0, 4.0, 4.0, 3.0]
    assert all(t["candidate_pool"] == 5 and not t.get("is_characteristic") for t in taxa)
    row = next(r for r in seed.read_tsv("gold_ecosystem_paths.tsv")
               if r["canonical_path"] == path)
    assert row["gold_node_ids"] == "gold.ecosystem:3513|gold.ecosystem:3845|gold.ecosystem:4277"
    context = {"mesh:D062611": "Solid Waste"}
    assert semantic_text(new, context) != semantic_text(old, context)
