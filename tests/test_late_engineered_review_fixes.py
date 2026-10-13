"""Bounded context exclusions for the slum-through-tailings review cohort."""

import pytest

from habitatmech import seed

# Keys are source mints, which differ from adopted ontology record identifiers.
CASES = {
    "habitatmech:GOLD.765d4bdada": ("ENVO:01000653", "habitatmech:GOLD.d8d3393339"),
    "habitatmech:GOLD.b1d707114a": ("habitatmech:GOLD.b1d707114a", "ENVO:01000621"),
    "habitatmech:GOLD.e9844fc187": ("habitatmech:GOLD.e9844fc187", "habitatmech:GOLD.86cf49cefb"),
    "habitatmech:GOLD.3e86b794ef": ("habitatmech:GOLD.3e86b794ef", "ENVO:01000620"),
    "habitatmech:GOLD.f96ea35aa9": ("ENVO:01003000", "habitatmech:GOLD.013b99db03"),
    "habitatmech:GOLD.2d40c87aeb": ("habitatmech:GOLD.2d40c87aeb", "ENVO:00000856"),
    "habitatmech:GOLD.8c6192908f": ("habitatmech:GOLD.8c6192908f", "habitatmech:GOLD.a8b8ee2424"),
    "habitatmech:GOLD.e856cf26a5": ("habitatmech:GOLD.e856cf26a5", "habitatmech:GOLD.961229841c"),
    "habitatmech:GOLD.ef9152b355": ("habitatmech:GOLD.ef9152b355", "habitatmech:GOLD.853ee40b1d"),
    "habitatmech:GOLD.288559828e": ("habitatmech:GOLD.288559828e", "habitatmech:GOLD.79e523eace"),
    "habitatmech:GOLD.84053fba17": ("habitatmech:GOLD.84053fba17", "ENVO:01000964"),
}


@pytest.fixture(scope="module")
def documents():
    return {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}


def test_eleven_exclusions_change_only_parents_and_append_history(documents, monkeypatch):
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    assert CASES.keys() <= exclusions.keys()
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda _: {
        key: row for key, row in exclusions.items() if key not in CASES
    })
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == documents.keys()
    assert {key for key in before if before[key] != documents[key]} == {
        identifier for identifier, _ in CASES.values()
    }
    for source, (identifier, parent) in CASES.items():
        old, new = before[identifier], documents[identifier]
        row = exclusions[source]
        assert row.parent_id == parent
        assert row.source_path == new["source_attestations"][0]["source_path"]
        assert seed.mint("GOLD", row.source_path) == source
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
        assert source in event["changes"] and parent in event["changes"]
        assert row.notes in event["changes"]


@pytest.mark.parametrize("source", CASES)
def test_frozen_source_nodes_and_count_units_are_preserved(source, documents):
    identifier, parent = CASES[source]
    doc = documents[identifier]
    assert parent not in doc.get("parent_habitats", [])
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


def test_independent_genera_and_unresolved_mapping_contract_remain(documents):
    for identifier in (
        "habitatmech:GOLD.b1d707114a",
        "habitatmech:GOLD.e9844fc187",
        "habitatmech:GOLD.3e86b794ef",
    ):
        assert documents[identifier]["parent_habitats"] == ["ENVO:00001998"]
        assert documents[identifier]["grounding_status"] == "NARROW"
        assert documents[identifier]["mapping_status"] == "SEEDED"
        # Hierarchy curation deliberately does not silently resolve shared #1398.
        assert documents[identifier]["source_attestations"][0]["mapping_predicate"] == "skos:narrowMatch"
    assert documents["ENVO:01000653"]["parent_habitats"] == ["ENVO:01000658"]
    assert documents["ENVO:01003000"]["parent_habitats"] == ["ENVO:01000604"]
    assert documents["habitatmech:GOLD.8c6192908f"]["parent_habitats"] == ["ENVO:0010001"]
    assert documents["habitatmech:GOLD.84053fba17"]["parent_habitats"] == ["ENVO:03600021"]


def test_space_station_keeps_spacecraft_without_inheriting_cleanroom(documents):
    station = documents["ENVO:03600050"]
    assert station["parent_habitats"] == ["ENVO:01003000", "mesh:D000076624"]
    seen, todo = set(), [station["identifier"]]
    while todo:
        identifier = todo.pop()
        if identifier in seen:
            continue
        seen.add(identifier)
        todo.extend(documents.get(identifier, {}).get("parent_habitats", []))
    assert "ENVO:01003000" in seen and "ENVO:01000604" in seen
    assert "habitatmech:GOLD.013b99db03" not in seen
    assert station["grounding_status"] == "BROAD"
    assert station["source_attestations"][0]["assertion_count"] == 937
