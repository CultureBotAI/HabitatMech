"""Four bounded repairs preserve all other corpus claims and source observations."""

from habitatmech import seed

PRESERVED = "FOODON:00002158"
CORRECTION = "food-preserved-ontology-synonym-scope"
PARENTS = {
    "habitatmech:GOLD.f6b4333781": ("habitatmech:GOLD.f6b4333781", []),
    "FOODON:00001258": ("habitatmech:GOLD.b2c3ae1ed5", ["FOODON:00002501", "FOODON:00002645"]),
    "habitatmech:GOLD.2aeb0d8390": ("habitatmech:GOLD.2aeb0d8390", []),
}


def test_exact_corpus_delta_and_preserved_source_claims(monkeypatch):
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    sources = {item[0] for item in PARENTS.values()}
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    annotations = seed.load_record_annotation_corrections(seed.RECORD_ANNOTATION_CORRECTIONS_PATH)
    assert sources <= exclusions.keys()
    assert sum(row.correction_id == CORRECTION for row in annotations) == 1
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda _: {
        key: row for key, row in exclusions.items() if key not in sources
    })
    monkeypatch.setattr(seed, "load_record_annotation_corrections", lambda _: [
        row for row in annotations if row.correction_id != CORRECTION
    ])
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {*PARENTS, PRESERVED}
    for identifier in [*PARENTS, PRESERVED]:
        old, new = before[identifier], after[identifier]
        allowed = {"curation_history"}
        added = [event for event in new["curation_history"] if event not in old["curation_history"]]
        assert len(added) == 1
        assert [event for event in new["curation_history"] if event not in added] == old["curation_history"]
        assert added[0]["curator"] == "codex-gpt-5"
        assert added[0]["timestamp"] == "2026-10-14T00:00:00Z"
        if identifier == PRESERVED:
            allowed.add("synonyms")
            assert added[0]["action"] == "ANNOTATION_CORRECTED"
            assert "'preserved' (FOODON) from 'EXACT_SYNONYM' to 'BROAD_SYNONYM'" in added[0]["changes"]
            assert "issues/2069" in added[0]["changes"]
            expected = [dict(row) for row in old["synonyms"]]
            assert expected == [
                {"synonym_text": "Preserved", "synonym_type": "RELATED_SYNONYM", "source": "BacDive"},
                {"synonym_text": "preserved", "synonym_type": "EXACT_SYNONYM", "source": "FOODON"},
            ]
            expected[1]["synonym_type"] = "BROAD_SYNONYM"
            assert new["synonyms"] == expected
        else:
            allowed.add("parent_habitats")
            source, retained = PARENTS[identifier]
            assert old["parent_habitats"] == sorted([*retained, "FOODON:03530206"])
            assert new.get("parent_habitats", []) == retained
            assert seed.mint("GOLD", exclusions[source].source_path) == source
            assert exclusions[source].parent_id == "FOODON:03530206"
            assert added[0]["action"] == "SOURCE_PARENT_EXCLUDED"
            assert source in added[0]["changes"]
        assert {k: v for k, v in old.items() if k not in allowed} == {
            k: v for k, v in new.items() if k not in allowed
        }
