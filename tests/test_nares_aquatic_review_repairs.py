"""Constrain the reviewed anatomy parents and aquatic-host alias corrections."""

from dataclasses import replace

from habitatmech import seed

PARENTS = {
    "habitatmech:GOLD.48ff047301": "habitatmech:GOLD.c9756cb050",
    "habitatmech:GOLD.cdc9731b44": "habitatmech:GOLD.bcb2f8b7f3",
    "habitatmech:GOLD.30303e874d": "habitatmech:GOLD.56e0776270",
    "habitatmech:GOLD.f3c6dc4883": "habitatmech:GOLD.dc86c8917c",
    "habitatmech:GOLD.d0912b66fe": "habitatmech:GOLD.dc86c8917c",
    "habitatmech:GOLD.9a7b884ca1": "habitatmech:GOLD.6bda0871e2",
    "habitatmech:GOLD.e68ce62892": "habitatmech:GOLD.5b0aa7456c",
    "habitatmech:GOLD.0512cf397f": "habitatmech:GOLD.5b0aa7456c",
    "habitatmech:GOLD.2a1b56ffda": "habitatmech:GOLD.aceda5f881",
}
RESOLVED = {
    "habitatmech:GOLD.30303e874d": "BTO:0001684",
    "habitatmech:GOLD.f3c6dc4883": "BTO:0001458",
    "habitatmech:GOLD.2a1b56ffda": "UBERON:0001796",
}
HOSTS = {
    "habitatmech:BACDIVE.15180e7ff9": ("Aquatic-mammal", 69, 46),
    "habitatmech:BACDIVE.38260eea00": ("Aquatic-plant", 66, 59),
}


def test_review_repairs_are_scoped_and_preserve_source_claims(monkeypatch):
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    aliases = seed.load_definition_source_label_exclusions(
        seed.DEFINITION_SOURCE_LABEL_EXCLUSIONS_PATH
    )
    definitions = seed.load_curated_definitions(seed.CURATED_DEFINITIONS_PATH)
    assert PARENTS.keys() <= parents.keys()
    assert HOSTS.keys() <= aliases.keys()
    assert all(not definitions[key].exact_synonyms for key in HOSTS)
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    with monkeypatch.context() as old:
        old.setattr(seed, "load_gold_parent_exclusions", lambda _: {
            key: row for key, row in parents.items() if key not in PARENTS
        })
        old.setattr(seed, "load_definition_source_label_exclusions", lambda _: {
            key: row for key, row in aliases.items() if key not in HOSTS
        })
        old.setattr(seed, "load_curated_definitions", lambda _: {
            **definitions, **{
                key: replace(definitions[key], exact_synonyms=(values[0],))
                for key, values in HOSTS.items()
            }
        })
        before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    expected = {RESOLVED.get(key, key) for key in PARENTS} | HOSTS.keys()
    assert before.keys() == after.keys()
    assert len(expected) == 11
    assert {key for key in before if before[key] != after[key]} == expected
    for key in expected:
        allowed = {"curation_history", "synonyms" if key in HOSTS else "parent_habitats"}
        assert {k: v for k, v in before[key].items() if k not in allowed} == {
            k: v for k, v in after[key].items() if k not in allowed
        }
        old_history = before[key]["curation_history"]
        assert after[key]["curation_history"][:len(old_history)] == old_history

    for source, parent in PARENTS.items():
        key = RESOLVED.get(source, source)
        assert parent in before[key]["parent_habitats"]
        assert after[key].get("parent_habitats", []) == [
            p for p in before[key]["parent_habitats"] if p != parent
        ]
        assert after[key]["source_attestations"] == before[key]["source_attestations"]

    assert after["BTO:0001458"]["parent_habitats"] == ["BTO:0001162", "BTO:0001331"]
    assert after["UBERON:0001796"]["parent_habitats"] == [
        "UBERON:0006312", "UBERON:0006314"
    ]
    for key, (label, count, pool) in HOSTS.items():
        assert not after[key].get("synonyms")
        assert after[key]["mapping_status"] == "REVIEWED"
        attestation = after[key]["source_attestations"][0]
        assert attestation["source_label"] == label
        assert attestation["assertion_count"] == count
        assert attestation["assertion_unit"] == "STRAIN"
        assert len(after[key]["characteristic_taxa"]) == 25
        assert all(t["candidate_pool"] == pool for t in after[key]["characteristic_taxa"])

    assert {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts} == after
