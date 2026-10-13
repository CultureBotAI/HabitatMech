"""Bounded hierarchy and source-alias repairs from the laboratory reviews."""

import pytest

from habitatmech import seed
from habitatmech.text_map_inputs import semantic_text


@pytest.fixture(scope="module")
def corpus():
    return seed.build_corpus()


def test_lake_water_exclusion_preserves_ontology_and_source_claims(corpus, monkeypatch):
    identifier = "ENVO:04000007"
    source_id = "habitatmech:GOLD.a32131f499"
    path = "Engineered > Artificial ecosystem > Mesocosm > Lake water"
    after = {c.identifier: seed.build_document(c) for c in corpus.concepts}
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    exclusion = exclusions.pop(source_id)
    assert exclusion.source_path == path
    assert exclusion.parent_id == "ENVO:01000620"
    assert seed.mint("GOLD", path) == source_id
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda _: exclusions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {identifier}
    old, new = before[identifier], after[identifier]
    assert old["parent_habitats"] == ["ENVO:00002006", "ENVO:01000620", "ENVO:01000813"]
    assert new["parent_habitats"] == ["ENVO:00002006", "ENVO:01000813"]
    assert new["curation_history"][:-1] == old["curation_history"]
    event = new["curation_history"][-1]
    assert event["action"] == "SOURCE_PARENT_EXCLUDED"
    assert event["curator"] == "codex-gpt-5"
    assert event["timestamp"] == "2026-10-09T00:00:00Z"
    assert all(value in event["changes"] for value in (source_id, path, "ENVO:01000620"))
    for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
        assert new.get(field) == old.get(field), field
    assert new["grounding_status"] == "EXACT"
    assert new["mapping_status"] == "SEEDED"
    assert new["source_attestations"] == [{
        "source": "GOLD", "source_id": "gold.ecosystem:7858",
        "source_label": "Lake water", "source_path": path,
        "mapping_predicate": "skos:exactMatch", "assertion_count": 1,
        "assertion_unit": "ORGANISM",
        "notes": "2 GOLD ecosystem node ids share this path; first shown. "
                 "See data/raw/gold_ecosystem_paths.tsv.",
    }]
    row = next(r for r in seed.read_tsv("gold_ecosystem_paths.tsv")
               if r["canonical_path"] == path)
    assert row["gold_node_ids"] == "gold.ecosystem:7858|gold.ecosystem:7859"
    context = {"ENVO:01000620": "mesocosm"}
    assert semantic_text(new, context) != semantic_text(old, context)


def test_broad_alias_repair_changes_only_source_scope_and_audit(corpus, monkeypatch):
    concepts = {c.identifier: c for c in corpus.concepts}
    after = {key: seed.build_document(c) for key, c in concepts.items()}
    monkeypatch.setattr(seed, "RELATED_SOURCE_MAPPING_STATUSES", frozenset({"CLOSE"}))
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    affected = {key for key in before if before[key] != after[key]}
    assert affected == {
        "ENVO:01000989", "ENVO:01001001", "ENVO:01001405", "ENVO:03600050",
        "FOODON:00001258", "PO:0025034", "UBERON:0001988", "UBERON:0002097",
    }
    for key in affected:
        old, new = before[key], after[key]
        for field in (old.keys() | new.keys()) - {"synonyms", "curation_history"}:
            assert new.get(field) == old.get(field), (key, field)
        assert all(e in new["curation_history"] for e in old["curation_history"])
        additions = [e for e in new["curation_history"] if e not in old["curation_history"]]
        assert len(additions) == len(concepts[key].broad_source_synonyms)
        for event in additions:
            assert event["action"] == "SOURCE_SYNONYM_SCOPED"
            assert event["timestamp"] == "2026-10-09T00:00:00Z"
            assert "a BROAD source mapping" in event["changes"]
        for source, label in concepts[key].broad_source_synonyms:
            assert (label, "RELATED_SYNONYM") in concepts[key].synonyms
            assert concepts[key].synonyms.get((label, "EXACT_SYNONYM")) != source
            assert any(a["source"].upper() == source.upper() and a["source_label"] == label
                       and a["mapping_predicate"] == "skos:broadMatch"
                       for a in new["source_attestations"])
        assert semantic_text(new) == semantic_text(old)
    laboratory = after["ENVO:01001405"]
    assert laboratory["synonyms"] == [{
        "synonym_text": "Lab synthesis", "synonym_type": "RELATED_SYNONYM", "source": "GOLD",
    }]
    assert laboratory["source_attestations"][0]["assertion_count"] == 549
    assert laboratory["source_attestations"][0]["assertion_unit"] == "ORGANISM"
    assert laboratory["grounding_status"] == "BROAD"
    assert laboratory["mapping_status"] == "REVIEWED"
