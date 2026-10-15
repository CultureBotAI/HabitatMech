"""Constrain reviewed host aliases, anatomical parents and colon synonym scope."""

from dataclasses import replace

from habitatmech import seed

PARENTS = {
    "habitatmech:GOLD.b183820c16": "habitatmech:GOLD.6c6aab19d3",
    "habitatmech:GOLD.c36ec4b6b6": "habitatmech:GOLD.67f49f8b15",
    "habitatmech:GOLD.ee0d0ceedd": "habitatmech:GOLD.28cfbd7dee",
    "habitatmech:GOLD.0d9cfc05b6": "habitatmech:GOLD.5b0aa7456c",
    "habitatmech:GOLD.197861c6ca": "BTO:0001782",
    "habitatmech:GOLD.b19b7cb64a": "habitatmech:GOLD.f9f745629a",
    "habitatmech:GOLD.f3fef23d8d": "UBERON:0003684",
}
RESOLVED = {
    "habitatmech:GOLD.b183820c16": "BTO:0006188",
    "habitatmech:GOLD.0d9cfc05b6": "UBERON:0001156",
}
HOSTS = {
    "habitatmech:GOLD.44a2cbbd60": "Arthropoda: Chelicerates",
    "habitatmech:GOLD.2959225799": "Arthropoda: Crustaceans",
    "habitatmech:GOLD.dba2a83b95": "Arthropoda: Insects",
    "habitatmech:GOLD.2333d6225a": "Arthropoda: Myriapoda",
    "habitatmech:GOLD.34c28836da": "Ascidians",
}
COLON = "UBERON:0001156"
CORRECTION = "ascending-colon-spiral-synonym-scope"


def test_review_repairs_preserve_corpus_scope(monkeypatch):
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    exclusions = seed.load_definition_source_label_exclusions(
        seed.DEFINITION_SOURCE_LABEL_EXCLUSIONS_PATH
    )
    definitions = seed.load_curated_definitions(seed.CURATED_DEFINITIONS_PATH)
    corrections = seed.load_record_annotation_corrections(seed.RECORD_ANNOTATION_CORRECTIONS_PATH)
    assert PARENTS.keys() <= parents.keys()
    assert HOSTS.keys() <= exclusions.keys()
    assert all(label not in definitions[key].exact_synonyms for key, label in HOSTS.items())
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    with monkeypatch.context() as old:
        old.setattr(seed, "load_gold_parent_exclusions", lambda _: {
            key: row for key, row in parents.items() if key not in PARENTS
        })
        old.setattr(seed, "load_definition_source_label_exclusions", lambda _: {
            key: row for key, row in exclusions.items() if key not in HOSTS
        })
        old.setattr(seed, "load_curated_definitions", lambda _: {
            **definitions, **{
                key: replace(definitions[key], exact_synonyms=(label, *definitions[key].exact_synonyms))
                for key, label in HOSTS.items()
            }
        })
        old.setattr(seed, "load_record_annotation_corrections", lambda _: [
            row for row in corrections if row.correction_id != CORRECTION
        ])
        before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    expected = {RESOLVED.get(key, key) for key in PARENTS} | HOSTS.keys()
    assert len(expected) == 12
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == expected
    for key in expected:
        allowed = {"curation_history"}
        if key in HOSTS or key == COLON:
            allowed.add("synonyms")
        if key not in HOSTS:
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
    assert after["BTO:0006188"]["parent_habitats"] == ["BTO:0000089"]
    assert after[COLON]["parent_habitats"] == ["UBERON:0000168"]
    for source, label in HOSTS.items():
        assert after[source].get("synonyms", []) == [
            s for s in before[source]["synonyms"] if s["synonym_text"] != label
        ]
        assert after[source]["source_attestations"][0]["source_label"] == label
        assert after[source]["mapping_status"] == "REVIEWED"
    assert after["habitatmech:GOLD.34c28836da"]["synonyms"] == [{
        "synonym_text": "sea squirt-associated environment",
        "synonym_type": "EXACT_SYNONYM", "source": "HabitatMech curation",
    }]
    assert {(s["source"], s["synonym_text"]): s["synonym_type"]
            for s in after[COLON]["synonyms"]} == {
        ("UBERON", "colon ascendens"): "EXACT_SYNONYM",
        ("UBERON", "spiral colon"): "RELATED_SYNONYM",
    }
    assert {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts} == after
