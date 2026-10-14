"""Six food-record repairs preserve all unrelated claims and observations."""

from habitatmech import seed

STARTER = "ENVO:03600040"
CASES = {
    "habitatmech:GOLD.0d60ee305c": ("habitatmech:GOLD.0d60ee305c", []),
    STARTER: ("habitatmech:GOLD.814fb91f0e", ["ENVO:00003074"]),
    "habitatmech:GOLD.8f5ec46a28": ("habitatmech:GOLD.8f5ec46a28", []),
    "FOODON:00001314": ("habitatmech:GOLD.5b7d7e2e70", ["FOODON:00001258"]),
    "habitatmech:GOLD.4f8bcf2e70": ("habitatmech:GOLD.4f8bcf2e70", []),
    "habitatmech:GOLD.2a0aafbf59": ("habitatmech:GOLD.2a0aafbf59", []),
}


def test_exact_corpus_change_scope_and_claim_preservation(monkeypatch):
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    sources = {item[0] for item in CASES.values()}
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    assert sources <= exclusions.keys()
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda _: {
        key: item for key, item in exclusions.items() if key not in sources
    })
    monkeypatch.setattr(seed, "load_record_annotation_corrections", lambda _: [])
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == CASES.keys()
    for identifier, (source, parents) in CASES.items():
        old, new = before[identifier], after[identifier]
        removed = "FOODON:00001006" if identifier == "FOODON:00001314" else "FOODON:03530206"
        assert new.get("parent_habitats", []) == parents
        assert set(old["parent_habitats"]) - set(parents) == {removed}
        assert exclusions[source].parent_id == removed
        assert seed.mint("GOLD", exclusions[source].source_path) == source
        added = [event for event in new["curation_history"] if event not in old["curation_history"]]
        assert [e for e in new["curation_history"] if e not in added] == old["curation_history"]
        assert [e["action"] for e in added].count("SOURCE_PARENT_EXCLUDED") == 1
        allowed = {"parent_habitats", "curation_history"}
        if identifier == STARTER:
            allowed |= {"synonyms", "characteristic_taxa"}
            assert len(added) == 3
            assert new["synonyms"] == [
                {"synonym_text": "Daqu", "synonym_type": "NARROW_SYNONYM", "source": "ENVO"},
                {"synonym_text": "Starter-culture", "synonym_type": "EXACT_SYNONYM", "source": "BacDive"},
            ]
            expected = [dict(row) for row in old["characteristic_taxa"]]
            assert len(expected) == 15
            assert expected[-1]["taxon_id"] == "NCBITaxon:86957"
            expected[-1]["taxon_label"] = "Schleiferibacter lacticifex"
            assert new["characteristic_taxa"] == expected
        else:
            assert len(added) == 1
        assert {k: v for k, v in old.items() if k not in allowed} == {
            k: v for k, v in new.items() if k not in allowed
        }


def test_daqu_is_not_an_existing_source_identity():
    for table, field in [("gold_ecosystem_paths.tsv", "leaf_label"),
                         ("bacdive_isolation_sources.tsv", "label")]:
        assert all(row.get(field, "").casefold() != "daqu" for row in seed.read_tsv(table))
