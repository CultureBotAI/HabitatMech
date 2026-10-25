"""Constrain eight GOLD context exclusions and the dinoflagellates exact-alias repair."""

import dataclasses
from collections import Counter

from jinja2 import Environment

from habitatmech import seed

PARENTS = {
    "habitatmech:GOLD.421614c436": ("UBERON:0001555", "habitatmech:GOLD.d011f4b43c"),
    "habitatmech:GOLD.9bfaa32c03": ("habitatmech:GOLD.9bfaa32c03", "habitatmech:GOLD.f131dcac3d"),
    "habitatmech:GOLD.d1ffda8340": ("habitatmech:GOLD.d1ffda8340", "habitatmech:GOLD.f131dcac3d"),
    "habitatmech:GOLD.4e3f079a4d": ("habitatmech:GOLD.4e3f079a4d", "habitatmech:GOLD.d3160a0c40"),
    "habitatmech:GOLD.87d8aea294": ("habitatmech:GOLD.87d8aea294", "habitatmech:GOLD.333c28fb9f"),
    "habitatmech:GOLD.4cb9c65c22": ("UBERON:0001690", "habitatmech:GOLD.b842078e17"),
    "habitatmech:GOLD.57fa2ba2ad": ("habitatmech:GOLD.57fa2ba2ad", "habitatmech:GOLD.1930d3bfbc"),
    "habitatmech:GOLD.8b135afbf6": ("habitatmech:GOLD.8b135afbf6", "habitatmech:GOLD.1821934761"),
}
SOURCE_PATHS = {
    "habitatmech:GOLD.421614c436": (
        "Host-associated > Annelida > Digestive system > Digestive tube"
    ),
    "habitatmech:GOLD.9bfaa32c03": (
        "Host-associated > Mammals: Human > Digestive system > Small intestine > Duodenal ulcer"
    ),
    "habitatmech:GOLD.d1ffda8340": (
        "Host-associated > Mammals: Human > Digestive system > Small intestine > Duodenum"
    ),
    "habitatmech:GOLD.4e3f079a4d": (
        "Host-associated > Mammals > Digestive system > Small intestine > Duodenum"
    ),
    "habitatmech:GOLD.87d8aea294": (
        "Host-associated > Birds > Digestive system > Small intestine > Duodenum"
    ),
    "habitatmech:GOLD.4cb9c65c22": (
        "Host-associated > Mammals: Human > Auditory/Hearing system > Ear"
    ),
    "habitatmech:GOLD.57fa2ba2ad": (
        "Host-associated > Mammals > Auditory/Hearing system > Outer ear > Ear canal"
    ),
    "habitatmech:GOLD.8b135afbf6": (
        "Host-associated > Mammals: Human > Auditory/Hearing system > Outer ear > Ear canal"
    ),
}
RETAINED_PARENTS = {
    "UBERON:0001555": ["UBERON:0000025"],
    "habitatmech:GOLD.9bfaa32c03": [],
    "habitatmech:GOLD.d1ffda8340": ["UBERON:0002114"],
    "habitatmech:GOLD.4e3f079a4d": ["UBERON:0002114"],
    "habitatmech:GOLD.87d8aea294": ["UBERON:0002114"],
    "UBERON:0001690": ["UBERON:0000020", "UBERON:0010314"],
    "habitatmech:GOLD.57fa2ba2ad": ["UBERON:0001352"],
    "habitatmech:GOLD.8b135afbf6": ["UBERON:0001352"],
}
DINOFLAGELLATES_ID = "habitatmech:GOLD.94019ddb33"


def test_reviewed_guards_and_public_evidence_links():
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    label_exclusions = seed.load_definition_source_label_exclusions(
        seed.DEFINITION_SOURCE_LABEL_EXCLUSIONS_PATH
    )
    definitions = seed.load_curated_definitions(seed.CURATED_DEFINITIONS_PATH)
    assert PARENTS.keys() == SOURCE_PATHS.keys()
    assert PARENTS.keys() <= parents.keys()
    assert DINOFLAGELLATES_ID in label_exclusions
    assert DINOFLAGELLATES_ID in definitions
    rows = []
    for key, (_, parent) in PARENTS.items():
        row = parents[key]
        assert row.source_path == SOURCE_PATHS[key]
        assert seed.mint("GOLD", row.source_path) == key
        assert row.parent_id == parent
        rows.append(row)
    dino_excl = label_exclusions[DINOFLAGELLATES_ID]
    assert dino_excl.source_label == "Dinoflagellates"
    assert dino_excl.requested_label == "dinoflagellate-associated environment"
    rows.append(dino_excl)
    dino_def = definitions[DINOFLAGELLATES_ID]
    assert dino_def.exact_synonyms == ("dinoflagellate host environment",)
    template = Environment(autoescape=True).from_string("{{ notes|urlize }}")
    for row in rows:
        urls = [
            word
            for word in row.notes.split()
            for word in [word]
            if word.startswith("https://github.com/CultureBotAI/HabitatMech/issues/")
        ]
        assert len(urls) == 1 and urls[0].rsplit("/", 1)[1].isdigit()
        assert f'href="{urls[0]}"' in template.render(notes=row.notes)


def test_nine_record_delta_preserves_unrelated_claims(monkeypatch):
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    label_exclusions = seed.load_definition_source_label_exclusions(
        seed.DEFINITION_SOURCE_LABEL_EXCLUSIONS_PATH
    )
    definitions = seed.load_curated_definitions(seed.CURATED_DEFINITIONS_PATH)
    assert PARENTS.keys() <= parents.keys()
    assert DINOFLAGELLATES_ID in label_exclusions and DINOFLAGELLATES_ID in definitions
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    reverted_definitions = dict(definitions)
    reverted_definitions[DINOFLAGELLATES_ID] = dataclasses.replace(
        definitions[DINOFLAGELLATES_ID],
        exact_synonyms=("Dinoflagellates",),
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
                key: row for key, row in label_exclusions.items() if key != DINOFLAGELLATES_ID
            },
        )
        old_ctx.setattr(
            seed,
            "load_curated_definitions",
            lambda _: reverted_definitions,
        )
        before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    expected_parent_targets = {target for target, _ in PARENTS.values()}
    assert len(PARENTS) == len(expected_parent_targets) == 8
    assert expected_parent_targets == RETAINED_PARENTS.keys()
    expected = expected_parent_targets | {DINOFLAGELLATES_ID}
    assert len(expected) == 9
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
    old_dino, new_dino = before[DINOFLAGELLATES_ID], after[DINOFLAGELLATES_ID]
    assert [s["synonym_text"] for s in old_dino["synonyms"]] == [
        "Dinoflagellates",
    ]
    assert [s["synonym_text"] for s in new_dino["synonyms"]] == [
        "dinoflagellate host environment",
    ]
    dino_history = old_dino["curation_history"]
    assert new_dino["curation_history"][: len(dino_history)] == dino_history
    dino_events = new_dino["curation_history"][len(dino_history) :]
    assert Counter(e["action"] for e in dino_events) == {"SOURCE_SYNONYM_EXCLUDED": 1}
    assert {
        k: v for k, v in old_dino.items() if k not in {"synonyms", "curation_history"}
    } == {
        k: v for k, v in new_dino.items() if k not in {"synonyms", "curation_history"}
    }
    assert {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts} == after
