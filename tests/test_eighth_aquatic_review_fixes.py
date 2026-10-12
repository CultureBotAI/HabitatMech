"""Exact-source ocean, sediment and water hierarchy corrections."""

import json
from pathlib import Path

import pytest

from habitatmech import seed

CASES = json.loads((Path(__file__).parent / "data/eighth_aquatic_review_cases.json").read_text())


@pytest.fixture(scope="module")
def documents():
    return {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}


def test_only_reviewed_records_change_and_source_populations_survive(documents, monkeypatch):
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    sources = {s["source"] for case in CASES.values() for s in case["sources"]}
    assert len(CASES) == 32 and len(sources) == 29
    old_decisions = dict(decisions)
    for identifier, case in CASES.items():
        if "decision" not in case:
            continue
        old = case["decision"]["old"]
        if old is None:
            del old_decisions[identifier]
        else:
            old = dict(old, relation=old["relation"] or "parent")
            old_decisions[identifier] = seed.Decision(**old)
    monkeypatch.setattr(
        seed,
        "load_gold_parent_exclusions",
        lambda _: {key: row for key, row in exclusions.items() if key not in sources},
    )
    monkeypatch.setattr(seed, "load_decisions", lambda _: old_decisions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == documents.keys()
    assert {key for key in before if before[key] != documents[key]} == CASES.keys()
    for identifier, case in CASES.items():
        old, new = before[identifier], documents[identifier]
        allowed = {"parent_habitats", "curation_history"}
        if "decision" in case:
            allowed |= {"grounding_status", "mapping_status", "source_attestations"}
            assert new["grounding_status"] == "NARROW"
            assert new["mapping_status"] == "REVIEWED"

            def strip(doc):
                return [
                    {k: v for k, v in a.items() if k != "mapping_predicate"}
                    for a in doc["source_attestations"]
                ]

            assert strip(old) == strip(new)
            assert all(a["mapping_predicate"] == "skos:narrowMatch" for a in new["source_attestations"])
        assert {k: v for k, v in old.items() if k not in allowed} == {
            k: v for k, v in new.items() if k not in allowed
        }
        assert new.get("parent_habitats", []) == case["retained"]


@pytest.mark.parametrize("identifier", CASES)
def test_exact_context_guards_and_source_units(identifier, documents):
    case = CASES[identifier]
    doc = documents[identifier]
    assert doc.get("parent_habitats", []) == case["retained"]
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    for source in case["sources"]:
        row = exclusions[source["source"]]
        assert seed.mint("GOLD", row.source_path) == source["source"]
        assert row.parent_id == source["removed"]
        raw = next(
            r for r in seed.read_tsv("gold_ecosystem_paths.tsv") if r["canonical_path"] == row.source_path
        )
        attestation = next(a for a in doc["source_attestations"] if a.get("source_path") == row.source_path)
        assert attestation["source_id"] == raw["gold_node_ids"].split("|")[0]
        if int(raw["organism_count"]):
            assert attestation["assertion_count"] == int(raw["organism_count"])
            assert attestation["assertion_unit"] == "ORGANISM"
        else:
            assert "assertion_count" not in attestation and "assertion_unit" not in attestation
        assert any(row.notes in e["changes"] for e in doc["curation_history"])


def test_sediment_water_and_waterbody_genera_are_distinct(documents):
    for identifier in (
        "habitatmech:GOLD.e6839bcc8f",
        "habitatmech:GOLD.7c79bcbca8",
        "habitatmech:GOLD.77996bd8e6",
        "habitatmech:GOLD.b3725fa211",
    ):
        assert documents[identifier]["parent_habitats"] == ["ENVO:00002007"]
    assert documents["habitatmech:GOLD.b46d816f26"]["parent_habitats"] == [
        "ENVO:00002010",
        "habitatmech:GOLD.22a80cbd14",
    ]
    assert documents["habitatmech:GOLD.1c0744c357"]["parent_habitats"] == [
        "ENVO:03600009",
        "habitatmech:GOLD.22a80cbd14",
    ]
    assert documents["habitatmech:GOLD.5b56a06a4c"]["parent_habitats"] == ["ENVO:00000020"]
    assert documents["habitatmech:GOLD.e13608a63a"]["parent_habitats"] == [
        "ENVO:00000020",
        "habitatmech:GOLD.5b56a06a4c",
    ]
    assert documents["habitatmech:GOLD.d250342fe1"]["parent_habitats"] == ["ENVO:01000871"]
    assert documents["habitatmech:GOLD.46309b7794"]["parent_habitats"] == ["ENVO:01000057"]


def test_valid_material_contexts_and_unresolved_scope_are_not_erased(documents):
    for identifier in (
        "habitatmech:GOLD.23cd8889db",
        "habitatmech:GOLD.3fb6b22200",
        "habitatmech:GOLD.aeb3ec93d9",
    ):
        assert documents[identifier]["parent_habitats"] == ["ENVO:01000063"]
    assert documents["habitatmech:GOLD.da6a051c8b"]["parent_habitats"] == ["ENVO:01000156"]
    for identifier in ("habitatmech:GOLD.dad9be1112", "habitatmech:GOLD.236abc4b8a"):
        assert any(
            parent.startswith("habitatmech:GOLD.") for parent in documents[identifier]["parent_habitats"]
        )
    assert "ENVO:01000124" in documents["ENVO:00000151"]["parent_habitats"]
    for identifier in (
        "habitatmech:GOLD.9272fc9901",
        "habitatmech:GOLD.dfb551a1fb",
        "habitatmech:GOLD.09350714a0",
    ):
        assert not documents[identifier].get("parent_habitats")
        assert documents[identifier]["mapping_status"] == "SEEDED"
    reservoir = documents["ENVO:00000025"]
    assert {(a["assertion_unit"], a["assertion_count"]) for a in reservoir["source_attestations"]} == {
        ("STRAIN", 75),
        ("ORGANISM", 34),
        ("TAXON", 2),
    }
