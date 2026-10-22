"""Constrain eleven GOLD context exclusions and the diatoms exact-alias repair."""

import dataclasses
from collections import Counter

from jinja2 import Environment

from habitatmech import seed

PARENTS = {
    "habitatmech:GOLD.26b1d1137f": ("habitatmech:GOLD.26b1d1137f", "habitatmech:GOLD.92d1e65695"),
    "habitatmech:GOLD.7ec36a9a02": ("habitatmech:GOLD.7ec36a9a02", "habitatmech:GOLD.2f62ba7993"),
    "habitatmech:GOLD.e4346a5cee": ("UBERON:0003672", "UBERON:0000167"),
    "habitatmech:GOLD.10b9b050da": ("UBERON:0000412", "habitatmech:GOLD.4b37ab4b76"),
    "habitatmech:GOLD.25fd1f31a1": ("habitatmech:GOLD.25fd1f31a1", "habitatmech:GOLD.c896f9520f"),
    "habitatmech:GOLD.fdd6965162": ("habitatmech:GOLD.fdd6965162", "habitatmech:GOLD.4b37ab4b76"),
    "habitatmech:GOLD.d545430f8f": ("UBERON:0002067", "habitatmech:GOLD.4b37ab4b76"),
    "habitatmech:GOLD.8634c1815d": ("UBERON:0001158", "habitatmech:GOLD.5b0aa7456c"),
    "habitatmech:GOLD.1219b1a720": ("habitatmech:GOLD.1219b1a720", "habitatmech:GOLD.4b37ab4b76"),
    "habitatmech:GOLD.a287a77880": ("habitatmech:GOLD.a287a77880", "habitatmech:GOLD.e36ba981d1"),
    "habitatmech:GOLD.c84e967b80": ("habitatmech:GOLD.c84e967b80", "habitatmech:GOLD.fac4f63f3b"),
}
SOURCE_PATHS = {
    "habitatmech:GOLD.26b1d1137f": (
        "Host-associated > Mammals > Digestive system > Oral cavity > Dental plaque"
    ),
    "habitatmech:GOLD.7ec36a9a02": (
        "Host-associated > Mammals: Human > Remains > Skeletonized remains > Dentin"
    ),
    "habitatmech:GOLD.e4346a5cee": (
        "Host-associated > Fish > Digestive system > Oral/Buccal cavity > Teeth"
    ),
    "habitatmech:GOLD.10b9b050da": (
        "Host-associated > Mammals: Human > Integumentary system > Skin > Dermal papilla"
    ),
    "habitatmech:GOLD.25fd1f31a1": (
        "Host-associated > Mammals > Integumentary system > Skin > Dermatitis"
    ),
    "habitatmech:GOLD.fdd6965162": (
        "Host-associated > Mammals: Human > Integumentary system > Skin > Dermatitis"
    ),
    "habitatmech:GOLD.d545430f8f": (
        "Host-associated > Mammals: Human > Integumentary system > Skin > Dermis"
    ),
    "habitatmech:GOLD.8634c1815d": (
        "Host-associated > Mammals: Human > Digestive system > Large intestine > Descending colon"
    ),
    "habitatmech:GOLD.1219b1a720": (
        "Host-associated > Mammals: Human > Integumentary system > Skin > Diabetic foot ulcer (DFU)"
    ),
    "habitatmech:GOLD.a287a77880": (
        "Host-associated > Mammals: Human > Respiratory system > Diaphragm"
    ),
    "habitatmech:GOLD.c84e967b80": (
        "Host-associated > Mammals > Respiratory system > Diaphragm"
    ),
}
RETAINED_PARENTS = {
    "habitatmech:GOLD.26b1d1137f": ["UBERON:0016482"],
    "habitatmech:GOLD.7ec36a9a02": ["BTO:0003453"],
    "UBERON:0003672": ["UBERON:0034925"],
    "UBERON:0000412": ["UBERON:0000479"],
    "habitatmech:GOLD.25fd1f31a1": ["ENVO:2100003"],
    "habitatmech:GOLD.fdd6965162": [],
    "UBERON:0002067": ["UBERON:0004121", "UBERON:0004923", "UBERON:0010314", "UBERON:0013754"],
    "UBERON:0001158": ["UBERON:0000168"],
    "habitatmech:GOLD.1219b1a720": [],
    "habitatmech:GOLD.a287a77880": ["UBERON:0001103"],
    "habitatmech:GOLD.c84e967b80": ["UBERON:0001103"],
}
DIATOMS_ID = "habitatmech:GOLD.1276bea544"


def test_reviewed_guards_and_public_evidence_links():
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    label_exclusions = seed.load_definition_source_label_exclusions(
        seed.DEFINITION_SOURCE_LABEL_EXCLUSIONS_PATH
    )
    definitions = seed.load_curated_definitions(seed.CURATED_DEFINITIONS_PATH)
    assert PARENTS.keys() == SOURCE_PATHS.keys()
    assert PARENTS.keys() <= parents.keys()
    assert DIATOMS_ID in label_exclusions
    assert DIATOMS_ID in definitions
    rows = []
    for key, (_, parent) in PARENTS.items():
        row = parents[key]
        assert row.source_path == SOURCE_PATHS[key]
        assert seed.mint("GOLD", row.source_path) == key
        assert row.parent_id == parent
        rows.append(row)
    diatoms_excl = label_exclusions[DIATOMS_ID]
    assert diatoms_excl.source_label == "Diatoms"
    assert diatoms_excl.requested_label == "diatom-associated environment"
    rows.append(diatoms_excl)
    diatoms_def = definitions[DIATOMS_ID]
    assert diatoms_def.exact_synonyms == ("diatom host environment",)
    template = Environment(autoescape=True).from_string("{{ notes|urlize }}")
    for row in rows:
        urls = [
            word
            for word in row.notes.split()
            if word.startswith("https://github.com/CultureBotAI/HabitatMech/issues/")
        ]
        assert len(urls) == 1 and urls[0].rsplit("/", 1)[1].isdigit()
        assert f'href="{urls[0]}"' in template.render(notes=row.notes)


def test_twelve_record_delta_preserves_unrelated_claims(monkeypatch):
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    label_exclusions = seed.load_definition_source_label_exclusions(
        seed.DEFINITION_SOURCE_LABEL_EXCLUSIONS_PATH
    )
    definitions = seed.load_curated_definitions(seed.CURATED_DEFINITIONS_PATH)
    assert PARENTS.keys() <= parents.keys()
    assert DIATOMS_ID in label_exclusions and DIATOMS_ID in definitions
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    reverted_definitions = dict(definitions)
    reverted_definitions[DIATOMS_ID] = dataclasses.replace(
        definitions[DIATOMS_ID],
        exact_synonyms=("Diatoms", "diatom host environment"),
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
                key: row for key, row in label_exclusions.items() if key != DIATOMS_ID
            },
        )
        old_ctx.setattr(
            seed,
            "load_curated_definitions",
            lambda _: reverted_definitions,
        )
        before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    expected_parent_targets = {target for target, _ in PARENTS.values()}
    assert len(PARENTS) == len(expected_parent_targets) == 11
    assert expected_parent_targets == RETAINED_PARENTS.keys()
    expected = expected_parent_targets | {DIATOMS_ID}
    assert len(expected) == 12
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == expected
    for source, (key, parent) in PARENTS.items():
        old_doc, new_doc = before[key], after[key]
        removed = {parent}
        allowed = {"parent_habitats", "curation_history"}
        history = old_doc["curation_history"]
        assert new_doc["curation_history"][: len(history)] == history
        events = new_doc["curation_history"][len(history) :]
        assert Counter(e["action"] for e in events) == {"SOURCE_PARENT_EXCLUDED": 1}
        exclusion = parents[source]
        event = next(e for e in new_doc["curation_history"] if e["action"] == "SOURCE_PARENT_EXCLUDED")
        assert event == {
            "timestamp": f"{exclusion.date}T00:00:00Z",
            "curator": exclusion.curator,
            "action": "SOURCE_PARENT_EXCLUDED",
            "changes": (
                f"Excluded GOLD source-path parent contribution {parent} "
                f"for {source} ({exclusion.source_path}). {exclusion.notes}"
            ),
        }
        assert removed <= set(old_doc["parent_habitats"])
        assert new_doc.get("parent_habitats", []) == [
            p for p in old_doc["parent_habitats"] if p not in removed
        ]
        assert new_doc.get("parent_habitats", []) == RETAINED_PARENTS[key]
        assert {k: v for k, v in old_doc.items() if k not in allowed} == {
            k: v for k, v in new_doc.items() if k not in allowed
        }
    old_diatoms, new_diatoms = before[DIATOMS_ID], after[DIATOMS_ID]
    assert [s["synonym_text"] for s in old_diatoms["synonyms"]] == [
        "Diatoms",
        "diatom host environment",
    ]
    assert [s["synonym_text"] for s in new_diatoms["synonyms"]] == ["diatom host environment"]
    diatoms_history = old_diatoms["curation_history"]
    assert new_diatoms["curation_history"][: len(diatoms_history)] == diatoms_history
    diatoms_events = new_diatoms["curation_history"][len(diatoms_history) :]
    assert Counter(e["action"] for e in diatoms_events) == {"SOURCE_SYNONYM_EXCLUDED": 1}
    assert {
        k: v for k, v in old_diatoms.items() if k not in {"synonyms", "curation_history"}
    } == {
        k: v for k, v in new_diatoms.items() if k not in {"synonyms", "curation_history"}
    }
    assert {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts} == after
