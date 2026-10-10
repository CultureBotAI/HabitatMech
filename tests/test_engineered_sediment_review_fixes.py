"""Bounded hierarchy corrections for the fifteen reviewed sediment materials."""

import pytest

from habitatmech import seed

TARGETS = {
    "habitatmech:GOLD.89569f7bcc": (
        "habitatmech:GOLD.236eb735d7",
        "Engineered > Artificial ecosystem > Aquaculture > Molluscs pond > Sediment",
    ),
    "habitatmech:GOLD.4f4488b5d8": (
        "habitatmech:GOLD.984e197faf",
        "Engineered > Artificial ecosystem > Aquaculture > Fish pen > Sediment",
    ),
    "habitatmech:GOLD.601cb8619f": (
        "habitatmech:GOLD.f0461d363e",
        "Engineered > Artificial ecosystem > Aquaculture > Fish pond > Sediment",
    ),
    "habitatmech:GOLD.7e27a52150": (
        "ENVO:00001997",
        "Engineered > Wastewater > Industrial wastewater > Acid mine drainage > Sediment",
    ),
    "habitatmech:GOLD.39b18ceeda": (
        "habitatmech:GOLD.96a29ab857",
        "Engineered > Built environment > Canal > Town canal > Sediment",
    ),
    "habitatmech:GOLD.088ff19037": (
        "habitatmech:GOLD.9ae5e17a12",
        "Engineered > Artificial ecosystem > Aquaculture > Molluscs farm > Sediment",
    ),
    "habitatmech:GOLD.70845c6a72": (
        "habitatmech:GOLD.be4a7c95b6",
        "Engineered > Artificial ecosystem > Aquaculture > Crustaceans pond > Sediment",
    ),
    "habitatmech:GOLD.f18dafe21d": (
        "habitatmech:GOLD.a904b6974e",
        "Engineered > Artificial ecosystem > Aquaculture > Crustaceans raceway > Sediment",
    ),
    "habitatmech:GOLD.b72faf3adf": (
        "ENVO:00000036",
        "Engineered > Built environment > Canal > Irrigation canal > Sediment",
    ),
    "habitatmech:GOLD.b8c468051f": (
        "habitatmech:GOLD.84053fba17",
        "Engineered > Wastewater > Industrial wastewater > Tailings pond > Sediment",
    ),
    "habitatmech:GOLD.085f791375": (
        "habitatmech:GOLD.c483f43031",
        "Engineered > Artificial ecosystem > Vivarium > Seawater aquarium > Sediment",
    ),
    "habitatmech:GOLD.6d45562fe0": (
        "habitatmech:GOLD.1a33387187",
        "Engineered > Artificial ecosystem > Aquaculture > Fish tank > Sediment",
    ),
    "habitatmech:GOLD.45953bb291": (
        "habitatmech:GOLD.e474187df8",
        "Engineered > Artificial ecosystem > Aquaculture > Algae raceway pond > Sediment",
    ),
    "habitatmech:GOLD.dbd07e057b": (
        "habitatmech:GOLD.b1f94cf5f5",
        "Engineered > Wastewater > Industrial wastewater > Settling tank > Sediment",
    ),
    "habitatmech:GOLD.c7282659d0": (
        "habitatmech:GOLD.21698a99df",
        "Engineered > Artificial ecosystem > Aquaculture > Crustaceans tank > Sediment",
    ),
}


@pytest.fixture(scope="module")
def documents():
    return {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}


def test_sediment_context_exclusions_have_exact_corpus_scope(documents, monkeypatch):
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    assert TARGETS.keys() <= exclusions.keys()
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda _: {
        key: row for key, row in exclusions.items() if key not in TARGETS
    })
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == documents.keys()
    assert {key for key in before if before[key] != documents[key]} == TARGETS.keys()

    for identifier, (parent, path) in TARGETS.items():
        old, new = before[identifier], documents[identifier]
        exclusion = exclusions[identifier]
        assert exclusion.source_path == path
        assert exclusion.parent_id == parent
        assert exclusion.curator == "codex-gpt-5"
        assert exclusion.date == "2026-10-10"
        assert old["parent_habitats"] == sorted([parent, "ENVO:00002007"])
        assert new["parent_habitats"] == ["ENVO:00002007"]
        allowed = {"parent_habitats", "curation_history"}
        assert {k: v for k, v in old.items() if k not in allowed} == {
            k: v for k, v in new.items() if k not in allowed
        }, identifier

        additions = [e for e in new["curation_history"] if e not in old["curation_history"]]
        assert len(additions) == 1
        event = additions[0]
        assert [e for e in new["curation_history"] if e != event] == old["curation_history"]
        assert event["action"] == "SOURCE_PARENT_EXCLUDED"
        assert event["timestamp"] == "2026-10-10T00:00:00Z"
        assert event["curator"] == "codex-gpt-5"
        assert identifier in event["changes"] and parent in event["changes"]
        assert path in event["changes"] and exclusion.notes in event["changes"]

    # A sediment microcosm is an experimental ecosystem, not another material leaf.
    microcosm = "habitatmech:GOLD.fcfbc02d98"
    assert documents[microcosm] == before[microcosm]
    assert documents[microcosm]["parent_habitats"] == ["habitatmech:GOLD.0acae9a1a4"]
    assert documents[microcosm]["grounding_status"] == "UNGROUNDED"


@pytest.mark.parametrize("identifier", TARGETS)
def test_sediment_source_scope_and_frozen_units_are_preserved(identifier, documents):
    doc = documents[identifier]
    assert doc["label"] == "Sediment"
    assert doc["habitat_category"] == "ENGINEERED"
    assert doc["grounding_status"] == "NARROW"
    assert doc["mapping_status"] == "SEEDED"
    assert len(doc["source_attestations"]) == 1
    attestation = doc["source_attestations"][0]
    path = TARGETS[identifier][1]
    assert attestation["source"] == "GOLD"
    assert attestation["source_path"] == path
    assert seed.mint("GOLD", path) == identifier
    # Shared issue #1398 is not silently disposed of by a hierarchy-only repair.
    assert attestation["mapping_predicate"] == "skos:narrowMatch"
    raw = next(row for row in seed.read_tsv("gold_ecosystem_paths.tsv")
               if row["canonical_path"] == path)
    assert raw["gold_node_ids"] == attestation["source_id"]
    count = int(raw["organism_count"])
    if count:
        assert attestation["assertion_count"] == count
        assert attestation["assertion_unit"] == "ORGANISM"
    else:
        assert "assertion_count" not in attestation
        assert "assertion_unit" not in attestation
