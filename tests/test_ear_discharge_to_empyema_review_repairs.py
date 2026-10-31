"""Constrain eleven ear_discharge..empyema cohort parent, grounding, and exact-synonym repairs."""

import dataclasses

from jinja2 import Environment

from habitatmech import seed

PARENTS = {
    "habitatmech:GOLD.4f987722bc": ("BTO:0002323", "habitatmech:GOLD.dc86c8917c"),
    "habitatmech:GOLD.e21234318e": ("habitatmech:GOLD.e21234318e", "habitatmech:GOLD.4b37ab4b76"),
    "habitatmech:GOLD.2047d759aa": ("habitatmech:GOLD.2047d759aa", "habitatmech:GOLD.51e593a6a4"),
    "habitatmech:GOLD.279140e15d": ("habitatmech:GOLD.279140e15d", "habitatmech:GOLD.33c4a7e711"),
    "habitatmech:GOLD.55552c8f52": ("UBERON:3010636", "habitatmech:GOLD.3c7ab95a73"),
    "habitatmech:GOLD.7b8cf8839b": ("habitatmech:GOLD.7b8cf8839b", "habitatmech:GOLD.d23207689e"),
    "habitatmech:GOLD.d6c49dfec6": ("UBERON:0001996", "habitatmech:GOLD.d8b9309d5e"),
    "habitatmech:GOLD.818c9729e2": ("habitatmech:GOLD.818c9729e2", "UBERON:0002402"),
}
SOURCE_PATHS = {
    "habitatmech:GOLD.4f987722bc": (
        "Host-associated > Mammals: Human > Integumentary system > Eccrine sweat glands"
    ),
    "habitatmech:GOLD.e21234318e": (
        "Host-associated > Mammals: Human > Integumentary system > Skin > Eczema"
    ),
    "habitatmech:GOLD.2047d759aa": (
        "Host-associated > Mammals: Human > Auditory/Hearing system > Middle ear > Effusion"
    ),
    "habitatmech:GOLD.279140e15d": (
        "Host-associated > Mammals > Auditory/Hearing system > Middle ear > Effusion"
    ),
    "habitatmech:GOLD.55552c8f52": (
        "Host-associated > Annelida > Reproductive system > Egg capsule"
    ),
    "habitatmech:GOLD.7b8cf8839b": (
        "Host-associated > Arthropoda: Insects > Ootheca/Egg mass > Eggs"
    ),
    "habitatmech:GOLD.d6c49dfec6": (
        "Host-associated > Mammals > Skeletal system > Cartilage > Elastic"
    ),
    "habitatmech:GOLD.818c9729e2": (
        "Host-associated > Mammals > Respiratory system > Pleural cavity > Empyema"
    ),
}
RETAINED_PARENTS = {
    "BTO:0002323": ["BTO:0001331", "BTO:0002324"],
    "habitatmech:GOLD.e21234318e": ["ENVO:2100003"],
    "habitatmech:GOLD.2047d759aa": ["UBERON:0006314"],
    "habitatmech:GOLD.279140e15d": ["UBERON:0006314"],
    "UBERON:3010636": ["UBERON:0000476", "UBERON:0000478"],
    "habitatmech:GOLD.7b8cf8839b": ["BTO:0000369"],
    "UBERON:0001996": ["UBERON:0011589"],
    "habitatmech:GOLD.818c9729e2": ["UBERON:0000175"],
}
LABEL_EXCLUSIONS = {
    "habitatmech:GOLD.e1f435d44b": ("Echinodermata", "echinoderm-associated environment"),
    "habitatmech:GOLD.e21234318e": ("Eczema", "human eczematous skin lesion"),
    "habitatmech:GOLD.2047d759aa": ("Effusion", "human middle ear effusion"),
    "habitatmech:GOLD.279140e15d": ("Effusion", "mammalian middle ear effusion"),
    "habitatmech:GOLD.32330da5da": ("Embryo", "brown algal embryo"),
    "habitatmech:GOLD.9f162205a6": ("Embryo", "fish embryo-associated environment"),
    "habitatmech:GOLD.818c9729e2": ("Empyema", "mammalian pleural empyema exudate"),
}
EXPECTED_SYNONYMS = {
    "habitatmech:GOLD.e1f435d44b": [],
    "habitatmech:GOLD.e21234318e": ["atopic dermatitis skin lesion"],
    "habitatmech:GOLD.2047d759aa": [
        "human tympanic cavity effusion",
        "human middle ear fluid",
    ],
    "habitatmech:GOLD.279140e15d": [
        "mammalian tympanic cavity effusion",
        "mammalian middle ear fluid",
    ],
    "habitatmech:GOLD.32330da5da": ["Phaeophyceae embryo"],
    "habitatmech:GOLD.9f162205a6": ["fish egg-associated environment"],
    "habitatmech:GOLD.818c9729e2": ["pleural empyema fluid"],
}


def test_reviewed_guards_and_public_evidence_links():
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    label_exclusions = seed.load_definition_source_label_exclusions(
        seed.DEFINITION_SOURCE_LABEL_EXCLUSIONS_PATH
    )
    definitions = seed.load_curated_definitions(seed.CURATED_DEFINITIONS_PATH)
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
    for key, expected_syns in EXPECTED_SYNONYMS.items():
        assert list(definitions[key].exact_synonyms) == expected_syns
    assert definitions["habitatmech:GOLD.2047d759aa"].parent_class == "UBERON:0006314"
    assert definitions["habitatmech:GOLD.279140e15d"].parent_class == "UBERON:0006314"
    assert definitions["habitatmech:GOLD.818c9729e2"].parent_class == "UBERON:0000175"
    template = Environment(autoescape=True).from_string("{{ notes|urlize }}")
    for row in rows:
        urls = [
            word
            for word in row.notes.split()
            if word.startswith("https://github.com/CultureBotAI/HabitatMech/issues/")
        ]
        assert len(urls) == 1 and urls[0].rsplit("/", 1)[1].isdigit()
        assert f'href="{urls[0]}"' in template.render(notes=row.notes)


def test_eleven_record_delta_preserves_unrelated_claims(monkeypatch):
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    label_exclusions = seed.load_definition_source_label_exclusions(
        seed.DEFINITION_SOURCE_LABEL_EXCLUSIONS_PATH
    )
    definitions = seed.load_curated_definitions(seed.CURATED_DEFINITIONS_PATH)
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    reverted_definitions = dict(definitions)
    reverted_definitions.pop("habitatmech:GOLD.2047d759aa", None)
    reverted_definitions.pop("habitatmech:GOLD.279140e15d", None)
    reverted_definitions["habitatmech:GOLD.e1f435d44b"] = dataclasses.replace(
        definitions["habitatmech:GOLD.e1f435d44b"],
        exact_synonyms=("Echinodermata",),
    )
    reverted_definitions["habitatmech:GOLD.e21234318e"] = dataclasses.replace(
        definitions["habitatmech:GOLD.e21234318e"],
        exact_synonyms=("Eczema", "atopic dermatitis skin lesion"),
        notes=(
            "Defined human eczematous skin lesion under ENVO:2100003 'skin environment'; "
            "supported by atopic dermatitis flare microbiome studies (PMID 22484416)."
        ),
        parent_mode="ADD",
    )
    reverted_definitions["habitatmech:GOLD.7b8cf8839b"] = dataclasses.replace(
        definitions["habitatmech:GOLD.7b8cf8839b"],
        notes=(
            "ITEM curation: GOLD 'Host-associated > Arthropoda: Insects > Ootheca/Egg mass > Eggs' "
            "denotes insect eggs within an egg mass or ootheca. Define under BTO:0000369 (egg) "
            "and exclude bare 'Eggs' (PMID 25085349; DOI:10.1038/ismej.2014.129). Path: "
            "Host-associated > Arthropoda: Insects > Ootheca/Egg mass > Eggs"
        ),
        parent_mode="ADD",
    )
    reverted_definitions["habitatmech:GOLD.32330da5da"] = dataclasses.replace(
        definitions["habitatmech:GOLD.32330da5da"],
        exact_synonyms=("Embryo", "Phaeophyceae embryo"),
    )
    reverted_definitions["habitatmech:GOLD.9f162205a6"] = dataclasses.replace(
        definitions["habitatmech:GOLD.9f162205a6"],
        exact_synonyms=("Embryo", "fish egg-associated environment"),
    )
    reverted_definitions["habitatmech:GOLD.818c9729e2"] = dataclasses.replace(
        definitions["habitatmech:GOLD.818c9729e2"],
        parent_class="UBERON:0002402",
        parent_label="pleural cavity",
        definition=(
            "A pleural cavity purulent exudate accumulated within the mammalian pleural space "
            "during bacterial pleuropneumonia or thoracic infection (pleural empyema)."
        ),
        exact_synonyms=("Empyema", "pleural empyema fluid"),
        date="2026-10-17",
        notes=(
            "Defined mammalian pleural empyema exudate under UBERON:0002402 'pleural cavity'; "
            "supported by pleural empyema 16S and metagenomic studies (PMID 30915025)."
        ),
        parent_mode="ADD",
    )

    reverted_decisions = dict(decisions)
    reverted_decisions["habitatmech:GOLD.2047d759aa"] = dataclasses.replace(
        decisions["habitatmech:GOLD.2047d759aa"],
        decision="GROUND_AS_PARENT",
        object_id="UBERON:0000175",
        object_label="pleural effusion",
        grounding_status="NARROW",
        curator="claude-opus-5",
        date="2026-08-12",
        notes=(
            "GOLD's Effusion is generic; UBERON only offers the pleural case, which is narrower, "
            "so it is recorded as a parent rather than the identity. Path: Host-associated > "
            "Mammals: Human > Auditory/Hearing system > Middle ea"
        ),
    )
    reverted_decisions["habitatmech:GOLD.279140e15d"] = dataclasses.replace(
        decisions["habitatmech:GOLD.279140e15d"],
        decision="GROUND_AS_PARENT",
        object_id="UBERON:0000175",
        object_label="pleural effusion",
        grounding_status="NARROW",
        curator="claude-opus-5",
        date="2026-08-12",
        notes=(
            "GOLD's Effusion is generic; UBERON only offers the pleural case, which is narrower, "
            "so it is recorded as a parent rather than the identity. Path: Host-associated > "
            "Mammals > Auditory/Hearing system > Middle ear > Eff"
        ),
    )
    reverted_decisions["habitatmech:GOLD.818c9729e2"] = dataclasses.replace(
        decisions["habitatmech:GOLD.818c9729e2"],
        date="2026-10-17",
        notes=(
            "Defined mammalian pleural empyema exudate under UBERON:0002402 'pleural cavity'; "
            "supported by pleural empyema 16S and metagenomic studies (PMID 30915025)."
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

    expected = set(RETAINED_PARENTS.keys()) | set(EXPECTED_SYNONYMS.keys())
    assert len(expected) == 11
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == expected
    for key, expected_parents in RETAINED_PARENTS.items():
        assert after[key].get("parent_habitats", []) == expected_parents
    for key, expected_syns in EXPECTED_SYNONYMS.items():
        assert sorted(s["synonym_text"] for s in after[key].get("synonyms", [])) == sorted(
            expected_syns
        )
    assert {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts} == after
