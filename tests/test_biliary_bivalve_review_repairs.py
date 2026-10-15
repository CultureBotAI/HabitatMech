"""Bound biliary, surface-film and host-name repairs across the complete corpus."""

from dataclasses import replace

from habitatmech import seed

PARENTS = {
    "habitatmech:GOLD.4db3420b06": "habitatmech:GOLD.de5efc0eb8",
    "habitatmech:GOLD.e30fd28de3": "habitatmech:GOLD.133311ddf9",
    "habitatmech:GOLD.bbb4a18cfe": "habitatmech:GOLD.133311ddf9",
    "habitatmech:GOLD.f8aad47f0f": "habitatmech:GOLD.004065681a",
    "habitatmech:GOLD.94d216ff38": "habitatmech:GOLD.133311ddf9",
    "habitatmech:GOLD.ce334980d0": "habitatmech:GOLD.de5efc0eb8",
    "habitatmech:GOLD.004065681a": "habitatmech:GOLD.8a68d0f6f5",
    "habitatmech:GOLD.133311ddf9": "habitatmech:GOLD.f6720bccf0",
    "habitatmech:GOLD.569ad8bc20": "habitatmech:GOLD.fb6caa2908",
    "habitatmech:GOLD.de5efc0eb8": "habitatmech:GOLD.c8e85f3c84",
    "habitatmech:GOLD.134eb9e767": "habitatmech:GOLD.26a84185d3",
    "habitatmech:GOLD.6ee20226a2": "habitatmech:GOLD.bcbf6eec9b",
    "habitatmech:GOLD.5766ea07fe": "habitatmech:GOLD.02383c20a7",
    "habitatmech:GOLD.f1e0d494f8": "PO:0025034",
}
RESOLVED = {
    "habitatmech:GOLD.e30fd28de3": "UBERON:0001970",
    "habitatmech:GOLD.bbb4a18cfe": "UBERON:0001970",
    "habitatmech:GOLD.ce334980d0": "BTO:0000122",
    "habitatmech:GOLD.5766ea07fe": "ENVO:01000909",
}
HOSTS = {
    "habitatmech:GOLD.47e603cf4f": "Birds",
    "habitatmech:GOLD.59e8d1205d": "Bivalves",
}
CORRECTIONS = {"bile-fel-synonym-scope", "bile-gall-synonym-scope"}


def test_review_repairs_preserve_complete_corpus(monkeypatch):
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    exclusions = seed.load_definition_source_label_exclusions(
        seed.DEFINITION_SOURCE_LABEL_EXCLUSIONS_PATH
    )
    definitions = seed.load_curated_definitions(seed.CURATED_DEFINITIONS_PATH)
    corrections = seed.load_record_annotation_corrections(seed.RECORD_ANNOTATION_CORRECTIONS_PATH)
    assert PARENTS.keys() <= parents.keys()
    assert HOSTS.keys() <= exclusions.keys()
    assert {row.correction_id for row in corrections} >= CORRECTIONS
    for key, alias in HOSTS.items():
        assert alias not in definitions[key].exact_synonyms
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    with monkeypatch.context() as old:
        old.setattr(seed, "load_gold_parent_exclusions", lambda _: {
            key: row for key, row in parents.items() if key not in PARENTS
        })
        old.setattr(seed, "load_definition_source_label_exclusions", lambda _: {
            key: row for key, row in exclusions.items() if key not in HOSTS
        })
        old.setattr(seed, "load_curated_definitions", lambda _: {
            key: replace(row, exact_synonyms=(HOSTS[key], *row.exact_synonyms))
            if key in HOSTS else row for key, row in definitions.items()
        })
        old.setattr(seed, "load_record_annotation_corrections", lambda _: [
            row for row in corrections if row.correction_id not in CORRECTIONS
        ])
        before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    affected_parents = {RESOLVED.get(key, key) for key in PARENTS}
    expected = affected_parents | HOSTS.keys()
    assert len(expected) == 15
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == expected
    for key in expected:
        allowed = {"curation_history"}
        if key in affected_parents:
            allowed.add("parent_habitats")
        if key in HOSTS or key == "UBERON:0001970":
            allowed.add("synonyms")
        assert {k: v for k, v in before[key].items() if k not in allowed} == {
            k: v for k, v in after[key].items() if k not in allowed
        }
        prior = before[key]["curation_history"]
        assert after[key]["curation_history"][:len(prior)] == prior
    for source, parent in PARENTS.items():
        key = RESOLVED.get(source, source)
        assert parent in before[key]["parent_habitats"]
        assert after[key].get("parent_habitats", []) == [
            p for p in before[key]["parent_habitats"] if p != parent
        ]
    assert after["UBERON:0001970"]["parent_habitats"] == [
        "UBERON:0000456", "UBERON:0006314"
    ]
    assert after["ENVO:01000909"]["parent_habitats"] == ["ENVO:01001311"]
    assert after["habitatmech:GOLD.f1e0d494f8"]["parent_habitats"] == ["ENVO:00002034"]
    for key, alias in HOSTS.items():
        assert after[key].get("synonyms", []) == [
            s for s in before[key]["synonyms"] if s["synonym_text"] != alias
        ]
        assert after[key]["source_attestations"][0]["source_label"] == alias
    assert after["UBERON:0001970"]["synonyms"] == [
        {**s, "synonym_type": "RELATED_SYNONYM"}
        if s["source"] == "UBERON" and s["synonym_text"] in {"fel", "gall"} else s
        for s in before["UBERON:0001970"]["synonyms"]
    ]
    assert {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts} == after
