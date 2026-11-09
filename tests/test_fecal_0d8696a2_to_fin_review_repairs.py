"""Constrain seven fecal__0d8696a2..fin cohort parent, grounding, and synonym repairs."""

import dataclasses

from jinja2 import Environment

from habitatmech import seed
from habitatmech.curate.decisions import Decision

PARENTS = {
    "habitatmech:GOLD.53337a753d": ("UBERON:0001988", "UBERON:0001555"),
    "habitatmech:GOLD.d11c365b20": ("UBERON:0001988", "habitatmech:GOLD.5b0aa7456c"),
    "habitatmech:GOLD.3671b973b2": ("UBERON:0001988", "habitatmech:GOLD.6bda0871e2"),
    "habitatmech:GOLD.515763f493": ("UBERON:0001988", "habitatmech:GOLD.b091b80314"),
    "habitatmech:GOLD.8634ec53de": ("UBERON:0008897", "habitatmech:GOLD.92e3c832eb"),
}
SOURCE_PATHS = {
    "habitatmech:GOLD.53337a753d": (
        "Host-associated > Annelida > Digestive system > Digestive tube > Cast"
    ),
    "habitatmech:GOLD.d11c365b20": (
        "Host-associated > Mammals: Human > Digestive system > Large intestine > Fecal"
    ),
    "habitatmech:GOLD.3671b973b2": (
        "Host-associated > Mammals > Digestive system > Large intestine > Fecal"
    ),
    "habitatmech:GOLD.515763f493": (
        "Host-associated > Birds > Digestive system > Large intestine > Fecal"
    ),
    "habitatmech:GOLD.8634ec53de": "Host-associated > Fish > Integumentary system > Skin > Fin",
}
RETAINED_PARENTS = {
    "UBERON:0001988": ["ENVO:00002276", "UBERON:0000174"],
    "UBERON:0008897": ["UBERON:0000026"],
    "habitatmech:GOLD.1ad500c492": ["UBERON:0000479"],
    "habitatmech:GOLD.c8a2e380c1": ["ENVO:01001002", "habitatmech:GOLD.e889967f4f"],
    "habitatmech:GOLD.f2a6418a5c": ["ENVO:01001002", "habitatmech:GOLD.cd0b0940e5"],
    "habitatmech:GOLD.fb56a964a6": ["NCIT:C3824"],
}
LABEL_EXCLUSIONS = {
    "habitatmech:BACDIVE.e6b73de092": ("Felidae-Cat", "felid-associated environment"),
    "habitatmech:GOLD.c8a2e380c1": ("Fetus", "mammalian fetus-associated environment"),
    "habitatmech:GOLD.f2a6418a5c": ("Fetus", "human fetus-associated environment"),
    "habitatmech:GOLD.fb56a964a6": ("Fibroma", "human fibroma lesion"),
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
    assert definitions["habitatmech:GOLD.1ad500c492"].parent_class == "UBERON:0000479"
    assert definitions["habitatmech:GOLD.1ad500c492"].parent_mode == "REPLACE"
    assert definitions["habitatmech:GOLD.c8a2e380c1"].parent_class == "ENVO:01001002"
    assert definitions["habitatmech:GOLD.c8a2e380c1"].parent_mode == "ADD"
    assert definitions["habitatmech:GOLD.f2a6418a5c"].parent_class == "ENVO:01001002"
    assert definitions["habitatmech:GOLD.f2a6418a5c"].parent_mode == "ADD"
    assert definitions["habitatmech:GOLD.fb56a964a6"].parent_class == "NCIT:C3824"
    assert definitions["habitatmech:GOLD.fb56a964a6"].parent_mode == "REPLACE"
    assert decisions["habitatmech:GOLD.c8a2e380c1"].object_id == "BTO:0000449"
    assert decisions["habitatmech:GOLD.c8a2e380c1"].relation == "xref"
    assert decisions["habitatmech:GOLD.f2a6418a5c"].object_id == "BTO:0000449"
    assert decisions["habitatmech:GOLD.f2a6418a5c"].relation == "xref"
    assert decisions["habitatmech:GOLD.fb56a964a6"].review_depth == "ITEM"
    template = Environment(autoescape=True).from_string("{{ notes|urlize }}")
    for row in rows:
        urls = [
            word
            for word in row.notes.split()
            if word.startswith("https://github.com/CultureBotAI/HabitatMech/issues/")
        ]
        assert len(urls) == 1 and urls[0].rsplit("/", 1)[1].isdigit()
        assert f'href="{urls[0]}"' in template.render(notes=row.notes)


def test_seven_record_delta_preserves_unrelated_claims(monkeypatch):
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
        if k
        not in {
            "habitatmech:GOLD.c8a2e380c1",
            "habitatmech:GOLD.f2a6418a5c",
            "habitatmech:GOLD.fb56a964a6",
        }
    }
    reverted_definitions["habitatmech:BACDIVE.e6b73de092"] = dataclasses.replace(
        definitions["habitatmech:BACDIVE.e6b73de092"],
        exact_synonyms=("Felidae-Cat",),
        curator="claude-opus-5",
        date="2026-08-26",
        notes=(
            "Definition follows the established <clade>-associated environment family for BacDive "
            "host buckets, whose naming rule the corpus already fixes: a -inae source label yields "
            "-ine (Bovinae-Cow,-Cattle -> bovine) and a -idae source label yields -id "
            "(Equidae-Horse -> equid, Leporidae-Rabbit/Hare -> leporid, Suidae-Pig,Swine -> suid). "
            "No deep-research run was commissioned: the genus, the wording pattern and the "
            "near-miss reasoning are already settled by those five siblings and by NCBITaxon, so a "
            "billed report would add nothing this slice turns on. Worded like the equid sibling for "
            "the same reason as the canid row: NCBITaxon:9681 'Felidae' is wider than the domestic "
            "cat the source label names."
        ),
    )
    reverted_definitions["habitatmech:GOLD.1ad500c492"] = dataclasses.replace(
        definitions["habitatmech:GOLD.1ad500c492"],
        date="2026-10-17",
        notes=(
            "Defined human fetal tissue under UBERON:0000479 'tissue'; supported by human perinatal "
            "and fetal tissue microbiology studies (PMID 32499646)."
        ),
        parent_mode="ADD",
    )

    reverted_decisions = {
        k: v
        for k, v in decisions.items()
        if k not in {"habitatmech:GOLD.c8a2e380c1", "habitatmech:GOLD.f2a6418a5c"}
    }
    reverted_decisions["habitatmech:GOLD.fb56a964a6"] = Decision(
        identifier="habitatmech:GOLD.fb56a964a6",
        decision="CONFIRM_UNGROUNDED",
        object_id="",
        object_label="",
        grounding_status="",
        curator="claude-opus-5",
        date="2026-08-12",
        notes=(
            "Class-level sweep (see docs/HARMONIZATION.md#class-level-sweep): no term in the "
            "vendored slice matched this label by any search route. Whether the concept is a "
            "habitat at all was NOT assessed, so this is not yet a term-request candidate."
        ),
        review_depth="CLASS",
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

    expected = set(RETAINED_PARENTS.keys()) | {"habitatmech:BACDIVE.e6b73de092"}
    assert len(expected) == 7
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == expected
    for key, expected_parents in RETAINED_PARENTS.items():
        assert after[key].get("parent_habitats", []) == expected_parents
    assert [s["synonym_text"] for s in after["habitatmech:BACDIVE.e6b73de092"].get("synonyms", [])] == [
        "cat-associated environment",
        "feline host environment",
    ]
    assert after["habitatmech:GOLD.c8a2e380c1"].get("xrefs") == ["BTO:0000449"]
    assert after["habitatmech:GOLD.f2a6418a5c"].get("xrefs") == ["BTO:0000449"]
    assert "mapping_predicate" not in after["habitatmech:GOLD.c8a2e380c1"]["source_attestations"][0]
    assert "mapping_predicate" not in after["habitatmech:GOLD.f2a6418a5c"]["source_attestations"][0]
    assert {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts} == after
