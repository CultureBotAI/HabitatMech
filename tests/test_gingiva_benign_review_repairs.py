"""Bound the gingiva-through-benign-tumor review repairs and preserve provenance."""

from dataclasses import replace

from habitatmech import seed

PARENTS = {
    "habitatmech:GOLD.1b82504233": "habitatmech:GOLD.99880772e1",
    "habitatmech:GOLD.d672a250b4": "habitatmech:GOLD.92d1e65695",
    "habitatmech:GOLD.b3344a5da2": "BTO:0006350",
    "habitatmech:GOLD.383b9034af": "habitatmech:GOLD.4b37ab4b76",
    "habitatmech:GOLD.cfa530990d": "habitatmech:GOLD.1daee83236",
    "habitatmech:GOLD.17b7f17bc1": "habitatmech:GOLD.9bb307824f",
    "habitatmech:GOLD.1a8c452712": "habitatmech:GOLD.e7296678c2",
    "habitatmech:GOLD.333c18201f": "habitatmech:GOLD.cd0b0940e5",
}
RESOLVED = {"habitatmech:GOLD.383b9034af": "UBERON:0009472"}
HOST = "habitatmech:GOLD.029baaef9e"
SCOPES = {
    "UBERON:0012348": ("autopod_pad", {"paw pad"}),
    "UBERON:0009472": ("axilla", {"armpits", "axillae", "oxter", "underarm"}),
}
CORRECTIONS = {
    slug.replace("_", "-") + "-" + alias.replace(" ", "-") + "-synonym-scope"
    for slug, aliases in SCOPES.values() for alias in aliases
}


def test_review_repairs_preserve_complete_corpus(monkeypatch):
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    exclusions = seed.load_definition_source_label_exclusions(
        seed.DEFINITION_SOURCE_LABEL_EXCLUSIONS_PATH
    )
    definitions = seed.load_curated_definitions(seed.CURATED_DEFINITIONS_PATH)
    corrections = seed.load_record_annotation_corrections(seed.RECORD_ANNOTATION_CORRECTIONS_PATH)
    assert PARENTS.keys() <= parents.keys()
    assert HOST in exclusions and "Bacteria" not in definitions[HOST].exact_synonyms
    assert {row.correction_id for row in corrections} >= CORRECTIONS
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    with monkeypatch.context() as old:
        old.setattr(seed, "load_gold_parent_exclusions", lambda _: {
            key: row for key, row in parents.items() if key not in PARENTS
        })
        old.setattr(seed, "load_definition_source_label_exclusions", lambda _: {
            key: row for key, row in exclusions.items() if key != HOST
        })
        old.setattr(seed, "load_curated_definitions", lambda _: {
            **definitions,
            HOST: replace(definitions[HOST], exact_synonyms=(
                "Bacteria", *definitions[HOST].exact_synonyms
            )),
        })
        old.setattr(seed, "load_record_annotation_corrections", lambda _: [
            row for row in corrections if row.correction_id not in CORRECTIONS
        ])
        before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    expected = {RESOLVED.get(key, key) for key in PARENTS} | {HOST} | SCOPES.keys()
    assert len(expected) == 10
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == expected
    for key in expected:
        allowed = {"curation_history"}
        if key in SCOPES or key == HOST:
            allowed.add("synonyms")
        if key in {RESOLVED.get(k, k) for k in PARENTS}:
            allowed.add("parent_habitats")
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
    assert after["UBERON:0009472"]["parent_habitats"] == ["UBERON:0034929"]
    assert after[HOST].get("synonyms", []) == [
        s for s in before[HOST]["synonyms"] if s["synonym_text"] != "Bacteria"
    ]
    assert after[HOST]["source_attestations"][0]["source_label"] == "Bacteria"
    for key, (_, aliases) in SCOPES.items():
        expected_synonyms = [
            {**s, "synonym_type": "RELATED_SYNONYM"}
            if s["source"] == "UBERON" and s["synonym_text"] in aliases else s
            for s in before[key]["synonyms"]
        ]
        assert after[key]["synonyms"] == expected_synonyms
    for key in ["habitatmech:GOLD.cfa530990d", "habitatmech:GOLD.17b7f17bc1",
                "habitatmech:GOLD.333c18201f"]:
        assert after[key]["grounding_status"] == "NOT_APPLICABLE"
    assert {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts} == after
