"""Constrain fourteen epicuticular_wax..excretory_system cohort parent, grounding, and synonym repairs."""

import dataclasses

from jinja2 import Environment

from habitatmech import seed

PARENTS = {
    "habitatmech:GOLD.284cf93966": ("PO:0025388", "PO:0025034"),
    "habitatmech:GOLD.bbe542f86d": ("UBERON:0035963", "habitatmech:GOLD.e36ba981d1"),
    "habitatmech:GOLD.6ee13ba963": ("BTO:0000424", "habitatmech:GOLD.d25ff4a586"),
    "habitatmech:GOLD.45b27bdccd": ("habitatmech:GOLD.45b27bdccd", "habitatmech:GOLD.974cd3759a"),
    "habitatmech:GOLD.5d6c618e63": ("habitatmech:GOLD.5d6c618e63", "habitatmech:GOLD.fe78a4c113"),
    "habitatmech:GOLD.b5205a5f5b": ("habitatmech:GOLD.b5205a5f5b", "habitatmech:GOLD.52f22e84ee"),
    "habitatmech:GOLD.b2fc8fb1e4": ("habitatmech:GOLD.b2fc8fb1e4", "habitatmech:GOLD.fb6caa2908"),
    "habitatmech:GOLD.974cd3759a": ("habitatmech:GOLD.974cd3759a", "habitatmech:GOLD.f6720bccf0"),
    "habitatmech:GOLD.01c242b3b0": ("habitatmech:GOLD.01c242b3b0", "habitatmech:GOLD.c8e85f3c84"),
    "habitatmech:GOLD.55cb603eb1": ("UBERON:0001679", "habitatmech:GOLD.67f49f8b15"),
    "habitatmech:GOLD.1f8a962fa9": ("habitatmech:GOLD.1f8a962fa9", "habitatmech:GOLD.33c4a7e711"),
    "habitatmech:GOLD.2127bae21d": ("habitatmech:GOLD.2127bae21d", "habitatmech:GOLD.51e593a6a4"),
    "habitatmech:GOLD.3a0549cbd8": ("habitatmech:GOLD.3a0549cbd8", "habitatmech:GOLD.dba2a83b95"),
}
SOURCE_PATHS = {
    "habitatmech:GOLD.284cf93966": (
        "Host-associated > Plants > Phyllosphere > Phylloplane/Leaf > Epicuticular wax"
    ),
    "habitatmech:GOLD.bbe542f86d": (
        "Host-associated > Mammals: Human > Respiratory system > Epithelial lining fluid"
    ),
    "habitatmech:GOLD.6ee13ba963": (
        "Host-associated > Mammals: Human > Circulatory system > Blood > Erythrocytes"
    ),
    "habitatmech:GOLD.45b27bdccd": (
        "Host-associated > Mammals: Human > Digestive system > Esophagus > Esophageal ulcer"
    ),
    "habitatmech:GOLD.5d6c618e63": (
        "Host-associated > Arthropoda: Crustaceans > Digestive system > Foregut > Esophagus"
    ),
    "habitatmech:GOLD.b5205a5f5b": (
        "Host-associated > Fish > Digestive system > Foregut > Esophagus"
    ),
    "habitatmech:GOLD.b2fc8fb1e4": (
        "Host-associated > Birds > Digestive system > Esophagus"
    ),
    "habitatmech:GOLD.974cd3759a": (
        "Host-associated > Mammals: Human > Digestive system > Esophagus"
    ),
    "habitatmech:GOLD.01c242b3b0": (
        "Host-associated > Mammals > Digestive system > Esophagus"
    ),
    "habitatmech:GOLD.55cb603eb1": (
        "Host-associated > Mammals: Human > Skeletal system > Bone > Scull: Ethmoid"
    ),
    "habitatmech:GOLD.1f8a962fa9": (
        "Host-associated > Mammals > Auditory/Hearing system > Middle ear > Eustachian tube"
    ),
    "habitatmech:GOLD.2127bae21d": (
        "Host-associated > Mammals: Human > Auditory/Hearing system > Middle ear > Eustachian tube"
    ),
    "habitatmech:GOLD.3a0549cbd8": (
        "Host-associated > Arthropoda: Insects > Excretory system"
    ),
}
RETAINED_PARENTS = {
    "PO:0025388": ["PO:0025386"],
    "UBERON:0035963": ["UBERON:0006314"],
    "BTO:0000424": ["BTO:0000574"],
    "habitatmech:GOLD.45b27bdccd": [],
    "habitatmech:GOLD.5d6c618e63": ["UBERON:0001043"],
    "habitatmech:GOLD.b5205a5f5b": ["UBERON:0001043"],
    "habitatmech:GOLD.b2fc8fb1e4": ["UBERON:0001043"],
    "habitatmech:GOLD.974cd3759a": ["UBERON:0001043"],
    "habitatmech:GOLD.01c242b3b0": ["UBERON:0001043"],
    "UBERON:0001679": ["UBERON:0002513", "UBERON:0003462", "UBERON:0011164"],
    "habitatmech:GOLD.1f8a962fa9": ["UBERON:0002393"],
    "habitatmech:GOLD.2127bae21d": ["UBERON:0002393"],
    "habitatmech:GOLD.3a0549cbd8": ["UBERON:8450002"],
}
LABEL_EXCLUSIONS = {
    "habitatmech:BACDIVE.09c3544e85": ("Equidae-Horse", "equid-associated environment"),
}


def test_reviewed_guards_and_public_evidence_links():
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    label_exclusions = seed.load_definition_source_label_exclusions(
        seed.DEFINITION_SOURCE_LABEL_EXCLUSIONS_PATH
    )
    definitions = seed.load_curated_definitions(seed.CURATED_DEFINITIONS_PATH)
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    assert PARENTS.keys() == SOURCE_PATHS.keys()
    assert PARENTS.keys() <= parents.keys()
    assert LABEL_EXCLUSIONS.keys() <= label_exclusions.keys()
    rows = []
    for key, (_, parent) in PARENTS.items():
        row = parents[key]
        assert row.source_path == SOURCE_PATHS[key]
        assert seed.mint("GOLD", row.source_path) == key
        assert row.parent_id == parent
        rows.append(row)
    for key, (source_label, requested_label) in LABEL_EXCLUSIONS.items():
        excl = label_exclusions[key]
        assert excl.source_label == source_label
        assert excl.requested_label == requested_label
        rows.append(excl)
    assert list(definitions["habitatmech:BACDIVE.09c3544e85"].exact_synonyms) == []
    assert decisions["habitatmech:GOLD.55cb603eb1"].grounding_status == "CLOSE"
    template = Environment(autoescape=True).from_string("{{ notes|urlize }}")
    for row in rows:
        urls = [
            word
            for word in row.notes.split()
            if word.startswith("https://github.com/CultureBotAI/HabitatMech/issues/")
        ]
        assert len(urls) == 1 and urls[0].rsplit("/", 1)[1].isdigit()
        assert f'href="{urls[0]}"' in template.render(notes=row.notes)


def test_fourteen_record_delta_preserves_unrelated_claims(monkeypatch):
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    label_exclusions = seed.load_definition_source_label_exclusions(
        seed.DEFINITION_SOURCE_LABEL_EXCLUSIONS_PATH
    )
    definitions = seed.load_curated_definitions(seed.CURATED_DEFINITIONS_PATH)
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    reverted_definitions = dict(definitions)
    reverted_definitions["habitatmech:BACDIVE.09c3544e85"] = dataclasses.replace(
        definitions["habitatmech:BACDIVE.09c3544e85"],
        exact_synonyms=("Equidae-Horse",),
    )

    reverted_decisions = dict(decisions)
    reverted_decisions["habitatmech:GOLD.55cb603eb1"] = dataclasses.replace(
        decisions["habitatmech:GOLD.55cb603eb1"],
        grounding_status="EXACT",
        notes=(
            "Variant-match review (#12): the seeder grounds on exact labels only, so GOLD's slash "
            "and plural conventions hid a term that says exactly this. GOLD writes 'Scull: Ethmoid'; "
            "the path is Skeletal system > Bone, so the ethmoid bone is meant. Path: "
            "Host-associated > Mammals: Human > Skeletal system > Bone > Scull: Ethmoid"
        ),
    )

    with monkeypatch.context() as old_ctx:
        old_ctx.setattr(
            seed,
            "load_gold_parent_exclusions",
            lambda _: {key: row for key, row in parents.items() if key not in PARENTS},
        )
        old_ctx.setattr(
            seed,
            "load_definition_source_label_exclusions",
            lambda _: {
                key: row for key, row in label_exclusions.items() if key not in LABEL_EXCLUSIONS
            },
        )
        old_ctx.setattr(
            seed,
            "load_curated_definitions",
            lambda _: reverted_definitions,
        )
        old_ctx.setattr(
            seed,
            "load_decisions",
            lambda _: reverted_decisions,
        )
        before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    expected = set(RETAINED_PARENTS.keys()) | {"habitatmech:BACDIVE.09c3544e85"}
    assert len(expected) == 14
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == expected
    for key, expected_parents in RETAINED_PARENTS.items():
        assert after[key].get("parent_habitats", []) == expected_parents
    assert after["habitatmech:BACDIVE.09c3544e85"].get("synonyms", []) == []
    assert after["UBERON:0001679"].get("grounding_status") == "CLOSE"
    assert [
        s for s in after["UBERON:0001679"].get("synonyms", []) if s["synonym_text"] == "Scull: Ethmoid"
    ] == [{"synonym_text": "Scull: Ethmoid", "synonym_type": "RELATED_SYNONYM", "source": "GOLD"}]
    assert {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts} == after
