"""Constrain 13 finger..free_living_state cohort identity, parent, and synonym repairs."""

import dataclasses

from jinja2 import Environment

from habitatmech import seed
from habitatmech.curate.decisions import Decision

PARENTS = {
    "habitatmech:GOLD.52f22e84ee": ("habitatmech:GOLD.52f22e84ee", "habitatmech:GOLD.8a68d0f6f5"),
    "habitatmech:GOLD.cd6e81f421": ("habitatmech:GOLD.cd6e81f421", "habitatmech:GOLD.c8e85f3c84"),
    "habitatmech:GOLD.bd1664969c": ("habitatmech:GOLD.bd1664969c", "habitatmech:GOLD.d7cff86ce8"),
    "habitatmech:GOLD.8997340b18": ("habitatmech:GOLD.8997340b18", "habitatmech:GOLD.acc41d1792"),
    "habitatmech:GOLD.fe78a4c113": ("habitatmech:GOLD.fe78a4c113", "habitatmech:GOLD.6eecdf150d"),
    "habitatmech:GOLD.9558a262cc": ("BTO:0000480", "habitatmech:GOLD.d3869ad37f"),
    "habitatmech:GOLD.319c3f351e": ("habitatmech:GOLD.319c3f351e", "habitatmech:GOLD.d4e02cf775"),
    "habitatmech:GOLD.67f3cde908": ("habitatmech:GOLD.67f3cde908", "habitatmech:GOLD.50722c7871"),
}
SOURCE_PATHS = {
    "habitatmech:GOLD.52f22e84ee": "Host-associated > Fish > Digestive system > Foregut",
    "habitatmech:GOLD.cd6e81f421": "Host-associated > Mammals > Digestive system > Foregut",
    "habitatmech:GOLD.bd1664969c": (
        "Host-associated > Arthropoda: Insects > Digestive system > Foregut"
    ),
    "habitatmech:GOLD.8997340b18": (
        "Host-associated > Arthropoda: Myriapoda > Digestive system > Foregut"
    ),
    "habitatmech:GOLD.fe78a4c113": (
        "Host-associated > Arthropoda: Crustaceans > Digestive system > Foregut"
    ),
    "habitatmech:GOLD.9558a262cc": (
        "Host-associated > Mammals > Digestive system > Stomach > Forestomach"
    ),
    "habitatmech:GOLD.319c3f351e": "Host-associated > Arthropoda: Insects > Larva > Gut > Frass",
    "habitatmech:GOLD.67f3cde908": (
        "Host-associated > Arthropoda: Insects > Digestive system > Hindgut > Frass"
    ),
}
RETAINED_PARENTS = {
    "habitatmech:GOLD.52f22e84ee": ["UBERON:0001041"],
    "habitatmech:GOLD.cd6e81f421": ["UBERON:0001041"],
    "habitatmech:GOLD.bd1664969c": ["UBERON:0001041"],
    "habitatmech:GOLD.8997340b18": ["UBERON:0001041"],
    "habitatmech:GOLD.fe78a4c113": ["UBERON:0001041"],
    "BTO:0000480": ["BTO:0001307"],
    "habitatmech:GOLD.319c3f351e": ["ENVO:00002003"],
    "habitatmech:GOLD.67f3cde908": ["ENVO:00002003"],
    "habitatmech:PREGO.ce9c3a92e9": ["ENVO:01001000"],
    "habitatmech:PREGO.267811fd7a": [],
    "habitatmech:GOLD.80220dc4d4": ["UBERON:0000029"],
    "habitatmech:PREGO.6c4660c2ae": [],
}
LABEL_EXCLUSIONS = {
    "habitatmech:GOLD.3d529a667e": ("Fish", "fish-associated environment"),
    "habitatmech:PREGO.ce9c3a92e9": ("flagellate", "flagellate-associated environment"),
    "habitatmech:GOLD.80220dc4d4": ("Forelegs", "mammalian forelimb lymph node"),
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
    assert definitions["habitatmech:GOLD.3d529a667e"].exact_synonyms == ("fish host environment",)
    assert definitions["habitatmech:PREGO.ce9c3a92e9"].parent_class == "ENVO:01001000"
    assert definitions["habitatmech:PREGO.ce9c3a92e9"].parent_mode == "REPLACE"
    assert definitions["habitatmech:GOLD.80220dc4d4"].parent_class == "UBERON:0000029"
    assert definitions["habitatmech:GOLD.80220dc4d4"].parent_mode == "REPLACE"
    assert decisions["habitatmech:PREGO.ce9c3a92e9"].decision == "CONFIRM_UNGROUNDED"
    assert decisions["habitatmech:PREGO.ce9c3a92e9"].object_id == "BTO:0000464"
    assert decisions["habitatmech:PREGO.ce9c3a92e9"].relation == "xref"
    assert decisions["habitatmech:PREGO.267811fd7a"].decision == "NOT_APPLICABLE"
    assert decisions["habitatmech:PREGO.267811fd7a"].object_id == "BTO:0002292"
    assert decisions["habitatmech:PREGO.267811fd7a"].relation == "xref"
    assert decisions["habitatmech:GOLD.80220dc4d4"].decision == "CONFIRM_UNGROUNDED"
    assert decisions["habitatmech:GOLD.80220dc4d4"].object_id == "UBERON:0000029"
    assert decisions["habitatmech:GOLD.80220dc4d4"].relation == "parent"
    assert decisions["habitatmech:PREGO.6c4660c2ae"].decision == "NOT_APPLICABLE"
    assert decisions["habitatmech:PREGO.6c4660c2ae"].object_id == "BTO:0001551"
    assert decisions["habitatmech:PREGO.6c4660c2ae"].relation == "xref"
    template = Environment(autoescape=True).from_string("{{ notes|urlize }}")
    for row in rows:
        urls = [
            word
            for word in row.notes.split()
            if word.startswith("https://github.com/CultureBotAI/HabitatMech/issues/")
        ]
        assert len(urls) == 1 and urls[0].rsplit("/", 1)[1].isdigit()
        assert f'href="{urls[0]}"' in template.render(notes=row.notes)


def test_thirteen_record_delta_preserves_unrelated_claims(monkeypatch):
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    label_exclusions = seed.load_definition_source_label_exclusions(
        seed.DEFINITION_SOURCE_LABEL_EXCLUSIONS_PATH
    )
    definitions = seed.load_curated_definitions(seed.CURATED_DEFINITIONS_PATH)
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    reverted_definitions = {
        k: v
        for k, v in definitions.items()
        if k not in {"habitatmech:PREGO.ce9c3a92e9", "habitatmech:GOLD.80220dc4d4"}
    }
    reverted_definitions["habitatmech:GOLD.3d529a667e"] = dataclasses.replace(
        definitions["habitatmech:GOLD.3d529a667e"],
        exact_synonyms=("Fish",),
    )

    reverted_decisions = {
        k: v
        for k, v in decisions.items()
        if k
        not in {
            "habitatmech:PREGO.ce9c3a92e9",
            "habitatmech:PREGO.267811fd7a",
            "habitatmech:PREGO.6c4660c2ae",
        }
    }
    reverted_decisions["habitatmech:GOLD.80220dc4d4"] = Decision(
        identifier="habitatmech:GOLD.80220dc4d4",
        decision="GROUND",
        object_id="BTO:0006514",
        object_label="foreleg",
        grounding_status="EXACT",
        curator="claude-opus-5",
        date="2026-08-12",
        notes=(
            "Leaf label equals the BTO label exactly and no other source concept claims it. "
            "Path: Host-associated > Mammals > Lymphatic system > Lymph nodes > Forelegs"
        ),
        review_depth="ITEM",
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

    for key, expected_parents in RETAINED_PARENTS.items():
        assert after[key].get("parent_habitats", []) == expected_parents
    assert [s["synonym_text"] for s in after["habitatmech:GOLD.3d529a667e"].get("synonyms", [])] == [
        "fish host environment"
    ]
    assert after["habitatmech:PREGO.ce9c3a92e9"].get("xrefs") == ["BTO:0000464"]
    assert after["habitatmech:PREGO.267811fd7a"].get("xrefs") == ["BTO:0002292"]
    assert after["habitatmech:PREGO.6c4660c2ae"].get("xrefs") == ["BTO:0001551"]

    before_unchanged = {
        k: v
        for k, v in before.items()
        if k not in {"BTO:0000464", "BTO:0002292", "BTO:0006514", "BTO:0001551"}
    }
    after_unchanged = {
        k: v
        for k, v in after.items()
        if k
        not in {
            "habitatmech:PREGO.ce9c3a92e9",
            "habitatmech:PREGO.267811fd7a",
            "habitatmech:GOLD.80220dc4d4",
            "habitatmech:PREGO.6c4660c2ae",
        }
    }
    assert before_unchanged.keys() == after_unchanged.keys()
    changed_same_id = {
        k for k in before_unchanged if before_unchanged[k] != after_unchanged[k]
    }
    assert changed_same_id == {
        "habitatmech:GOLD.3d529a667e",
        "habitatmech:GOLD.52f22e84ee",
        "habitatmech:GOLD.cd6e81f421",
        "habitatmech:GOLD.bd1664969c",
        "habitatmech:GOLD.8997340b18",
        "habitatmech:GOLD.fe78a4c113",
        "BTO:0000480",
        "habitatmech:GOLD.319c3f351e",
        "habitatmech:GOLD.67f3cde908",
    }
    assert {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts} == after
