"""Guard the final engineered cohort's material-versus-setting corrections."""

import pytest

from habitatmech import seed

CASES = {
    "habitatmech:GOLD.0533686915": "ENVO:00000014",
    "habitatmech:GOLD.c22928551b": "habitatmech:GOLD.fcfbc02d98",
    "habitatmech:GOLD.f9d0b8af79": "habitatmech:GOLD.b076c78736",
    "habitatmech:GOLD.4f0fb37d6f": "habitatmech:GOLD.961229841c",
}


@pytest.fixture(scope="module")
def documents():
    return {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}


def test_four_exclusions_change_only_parents_and_append_history(documents, monkeypatch):
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    assert CASES.keys() <= exclusions.keys()
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda _: {
        key: row for key, row in exclusions.items() if key not in CASES
    })
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == documents.keys()
    assert {key for key in before if before[key] != documents[key]} == CASES.keys()
    for identifier, parent in CASES.items():
        old, new = before[identifier], documents[identifier]
        row = exclusions[identifier]
        assert row.parent_id == parent
        assert row.source_path == new["source_attestations"][0]["source_path"]
        assert seed.mint("GOLD", row.source_path) == identifier
        assert parent in old["parent_habitats"]
        assert new.get("parent_habitats", []) == [
            p for p in old["parent_habitats"] if p != parent
        ]
        allowed = {"parent_habitats", "curation_history"}
        assert {k: v for k, v in old.items() if k not in allowed} == {
            k: v for k, v in new.items() if k not in allowed
        }
        additions = [e for e in new["curation_history"] if e not in old["curation_history"]]
        assert len(additions) == 1
        event = additions[0]
        assert [e for e in new["curation_history"] if e != event] == old["curation_history"]
        assert event["action"] == "SOURCE_PARENT_EXCLUDED"
        assert event["curator"] == "codex-gpt-5"
        assert event["timestamp"] == "2026-10-11T00:00:00Z"
        assert identifier in event["changes"] and parent in event["changes"]
        assert row.notes in event["changes"]


@pytest.mark.parametrize("identifier", CASES)
def test_frozen_source_nodes_and_count_units_are_preserved(identifier, documents):
    doc = documents[identifier]
    assert CASES[identifier] not in doc.get("parent_habitats", [])
    assert len(doc["source_attestations"]) == 1
    attestation = doc["source_attestations"][0]
    assert attestation["source"] == "GOLD"
    raw = next(r for r in seed.read_tsv("gold_ecosystem_paths.tsv")
               if r["canonical_path"] == attestation["source_path"])
    assert raw["gold_node_ids"].split("|")[0] == attestation["source_id"]
    count = int(raw["organism_count"])
    if count:
        assert attestation["assertion_count"] == count
        assert attestation["assertion_unit"] == "ORGANISM"
    else:
        assert "assertion_count" not in attestation and "assertion_unit" not in attestation


def test_water_keeps_material_genus_without_claiming_endpoint_repair(documents):
    water = documents["habitatmech:GOLD.0533686915"]
    assert water["parent_habitats"] == ["ENVO:00002006"]
    assert water["grounding_status"] == "NARROW"
    assert water["mapping_status"] == "REVIEWED"
    assert water["source_attestations"][0]["mapping_predicate"] == "skos:narrowMatch"
    for identifier in CASES.keys() - {water["identifier"]}:
        assert not documents[identifier].get("parent_habitats")
        assert documents[identifier]["grounding_status"] == "UNGROUNDED"
        assert documents[identifier]["mapping_status"] == "SEEDED"


def test_all_six_subway_surfaces_exclude_the_whole_environment(documents):
    for suffix in (
        "2082ed6ba7", "4f0fb37d6f", "8ef066825a",
        "d4694eed69", "4f9191d466", "e856cf26a5",
    ):
        doc = documents["habitatmech:GOLD." + suffix]
        assert "habitatmech:GOLD.961229841c" not in doc.get("parent_habitats", [])
        assert doc["source_attestations"][0]["source_path"].startswith(
            "Engineered > Built environment > City > Subway > "
        )
