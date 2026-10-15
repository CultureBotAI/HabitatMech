"""Separate reviewed anatomical contexts, host labels and vertebrate homonyms."""

import json
from dataclasses import replace
from pathlib import Path

from jinja2 import Environment

from habitatmech import seed

PARENT_PATHS = {
    "Host-associated > Mammals > Digestive system > Oral cavity > Buccal mucosa":
        ("habitatmech:GOLD.4caaf1fb4f", "habitatmech:GOLD.92d1e65695"),
    "Host-associated > Mammals: Human > Digestive system > Oral cavity > Buccal mucosa":
        ("habitatmech:GOLD.1a8d5400cc", "habitatmech:GOLD.99880772e1"),
    "Host-associated > Mammals: Human > Circulatory system > Blood > Buffy coat":
        ("BTO:0006181", "habitatmech:GOLD.d25ff4a586"),
    "Host-associated > Plants > Rhizome > Bulb":
        ("BTO:0000159", "BTO:0001181"),
    "Host-associated > Birds > Lymphatic system > Bursa of Fabricius":
        ("UBERON:0003903", "habitatmech:GOLD.f65007e88e"),
    "Host-associated > Mammals > Digestive system > Stomach > C1/Glandular saccules":
        ("habitatmech:GOLD.003eca7f24", "habitatmech:GOLD.d3869ad37f"),
    "Host-associated > Mammals > Digestive system > Stomach > C2":
        ("habitatmech:GOLD.e89f860f72", "habitatmech:GOLD.d3869ad37f"),
    "Host-associated > Mammals > Digestive system > Stomach > C3":
        ("habitatmech:GOLD.5f6ed7c41e", "habitatmech:GOLD.d3869ad37f"),
    "Host-associated > Arthropoda: Crustaceans > Digestive system > Midgut > Caeca":
        ("habitatmech:GOLD.15af5884e8", "habitatmech:GOLD.5c1b0d44e2"),
    "Host-associated > Arthropoda: Insects > Digestive system > Midgut > Caeca":
        ("habitatmech:GOLD.ca7333c915", "habitatmech:GOLD.67c565f695"),
    "Host-associated > Arthropoda: Insects > Digestive system > Midgut > Caeca: Bacteriome":
        ("habitatmech:GOLD.2d506b9526", "habitatmech:GOLD.67c565f695"),
    "Host-associated > Mammals > Visual system > Canthus":
        ("habitatmech:GOLD.4d8b9e6fe9", "habitatmech:GOLD.4166733314"),
    "Host-associated > Mammals: Human > Visual system > Canthus":
        ("habitatmech:GOLD.9d97d0af50", "habitatmech:GOLD.020f82703b"),
}
HOSTS = {
    "habitatmech:GOLD.3e4ecbed63": "Brown Algae",
    "habitatmech:BACDIVE.33fde10528": "Canidae-Dog",
    "habitatmech:BACDIVE.4d3086a839": "Caprinae-Sheep/Goat",
}
CAECAL_PARENTS = {
    "habitatmech:GOLD.15af5884e8": "UBERON:0001153",
    "habitatmech:GOLD.ca7333c915": "UBERON:0001153",
    "habitatmech:GOLD.2d506b9526": "BTO:0000166",
}
BROWN = "habitatmech:GOLD.3e4ecbed63"
BACTERIOME = "habitatmech:GOLD.2d506b9526"
NEW_DECISIONS = set(CAECAL_PARENTS) - {BACTERIOME}


def test_reviewed_input_guards_and_public_links():
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    aliases = seed.load_definition_source_label_exclusions(
        seed.DEFINITION_SOURCE_LABEL_EXCLUSIONS_PATH
    )
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    template = Environment(autoescape=True).from_string("{{ notes|urlize }}")
    rows = []
    for path, (_, parent) in PARENT_PATHS.items():
        row = parents[seed.mint("GOLD", path)]
        assert row.source_path == path
        assert row.parent_id == parent
        rows.append(row)
    rows.extend(aliases[key] for key in HOSTS)
    rows.extend(decisions[key] for key in {*CAECAL_PARENTS, BROWN})
    for row in rows:
        urls = [word for word in row.notes.split()
                if word.startswith("https://github.com/CultureBotAI/HabitatMech/issues/")]
        assert len(urls) == 1
        assert urls[0].rsplit("/", 1)[1].isdigit()
        assert f'href="{urls[0]}"' in template.render(notes=row.notes)


def test_repairs_preserve_exact_full_corpus_scope(monkeypatch):
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    aliases = seed.load_definition_source_label_exclusions(
        seed.DEFINITION_SOURCE_LABEL_EXCLUSIONS_PATH
    )
    definitions = seed.load_curated_definitions(seed.CURATED_DEFINITIONS_PATH)
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    prior_rows = json.loads(
        Path(__file__).with_name("data").joinpath(
            "buccal_camelid_caeca_prior_decisions.json"
        ).read_text()
    )
    parent_keys = {seed.mint("GOLD", path) for path in PARENT_PATHS}
    assert parent_keys <= parents.keys()
    assert HOSTS.keys() <= aliases.keys()
    assert decisions.keys() >= NEW_DECISIONS
    assert all(label not in definitions[key].exact_synonyms for key, label in HOSTS.items())
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    with monkeypatch.context() as old:
        old.setattr(seed, "load_gold_parent_exclusions", lambda _: {
            key: row for key, row in parents.items() if key not in parent_keys
        })
        old.setattr(seed, "load_definition_source_label_exclusions", lambda _: {
            key: row for key, row in aliases.items() if key not in HOSTS
        })
        old.setattr(seed, "load_curated_definitions", lambda _: {
            key: replace(row, exact_synonyms=(HOSTS[key], *row.exact_synonyms))
            if key in HOSTS else row for key, row in definitions.items()
        })
        old.setattr(seed, "load_decisions", lambda _: {
            key: replace(row, **prior_rows[key]) if key in prior_rows else row
            for key, row in decisions.items() if key not in NEW_DECISIONS
        })
        before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    expected = {target for target, _ in PARENT_PATHS.values()} | HOSTS.keys()
    assert len(expected) == 16
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == expected
    for key in expected:
        allowed = {"curation_history"}
        if key in HOSTS:
            allowed.add("synonyms")
        else:
            allowed.add("parent_habitats")
        if key in CAECAL_PARENTS:
            allowed |= {"grounding_status", "mapping_status", "source_attestations"}
        assert {k: v for k, v in before[key].items() if k not in allowed} == {
            k: v for k, v in after[key].items() if k not in allowed
        }
        if key not in {*CAECAL_PARENTS, BROWN}:
            prior = before[key]["curation_history"]
            assert after[key]["curation_history"][:len(prior)] == prior
            assert len(after[key]["curation_history"]) == len(prior) + 1

    for key, parent in PARENT_PATHS.values():
        removed = {parent}
        if key in CAECAL_PARENTS:
            removed.add(CAECAL_PARENTS[key])
        assert removed <= set(before[key]["parent_habitats"])
        assert after[key].get("parent_habitats", []) == [
            p for p in before[key]["parent_habitats"] if p not in removed
        ]
    for key, label in HOSTS.items():
        assert after[key].get("synonyms", []) == [
            s for s in before[key]["synonyms"] if s["synonym_text"] != label
        ]
        assert after[key]["source_attestations"][0]["source_label"] == label
        assert [e for e in after[key]["curation_history"] if e["action"] == "DEFINED"] == [
            e for e in before[key]["curation_history"] if e["action"] == "DEFINED"
        ]
    for key in CAECAL_PARENTS:
        assert decisions[key].decision == "CONFIRM_UNGROUNDED"
        assert decisions[key].review_depth == "ITEM"
        assert after[key]["grounding_status"] == "UNGROUNDED"
        assert after[key]["mapping_status"] == "REVIEWED"
        assert not after[key].get("xrefs")
        assert after[key]["source_attestations"] == [
            {k: v for k, v in att.items() if k != "mapping_predicate"}
            for att in before[key]["source_attestations"]
        ]
    assert after[BACTERIOME]["source_attestations"][0]["assertion_count"] == 5
    assert after[BACTERIOME]["source_attestations"][0]["assertion_unit"] == "ORGANISM"
    assert decisions[BACTERIOME].notes.endswith(
        "Path: Host-associated > Arthropoda: Insects > Digestive system > Midgut > Caeca: Bacteriome"
    )
    assert "no textual definition" in decisions[BROWN].notes
    assert after["BTO:0000159"]["parent_habitats"] == ["BTO:0000720"]
    assert after["habitatmech:GOLD.e89f860f72"]["parent_habitats"] == ["UBERON:0009870"]
    assert after["habitatmech:GOLD.4caaf1fb4f"]["source_attestations"][0][
        "mapping_predicate"
    ] == "skos:narrowMatch"
    assert {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts} == after
