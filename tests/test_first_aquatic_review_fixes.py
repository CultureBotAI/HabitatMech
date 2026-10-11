"""Guard the first aquatic cohort's context-versus-genus corrections."""

import pytest

from habitatmech import seed

# Source mint -> generated identity, excluded contribution, independent parents.
CASES = {
    "habitatmech:GOLD.d727388954": (
        "ENVO:00001997",
        "habitatmech:GOLD.7f8e268653",
        ["ENVO:00001996", "ENVO:01000964"],
    ),
    "habitatmech:GOLD.2a6cc2b868": ("habitatmech:GOLD.2a6cc2b868", "habitatmech:GOLD.90a084a03e", []),
    "habitatmech:GOLD.41f771c2b4": ("habitatmech:GOLD.41f771c2b4", "habitatmech:GOLD.90a084a03e", []),
    "habitatmech:GOLD.4a2e9ede31": ("ENVO:01001898", "habitatmech:GOLD.22a80cbd14", ["ENVO:00000027"]),
    "habitatmech:GOLD.245555f695": ("habitatmech:GOLD.245555f695", "habitatmech:GOLD.09350714a0", []),
    "habitatmech:GOLD.a16a79bd0c": ("habitatmech:GOLD.a16a79bd0c", "ENVO:00002011", ["ENVO:00000114"]),
    "habitatmech:GOLD.b3f000fa4a": ("ENVO:2000004", "ENVO:00000021", ["ENVO:00000012"]),
    "habitatmech:GOLD.784eaddd71": ("ENVO:01001894", "habitatmech:GOLD.22a80cbd14", ["ENVO:00000125"]),
    "habitatmech:GOLD.b75e4aa08f": ("habitatmech:GOLD.b75e4aa08f", "ENVO:00000021", []),
    "habitatmech:GOLD.9f7a6c66a7": ("ENVO:00012408", "habitatmech:GOLD.7f8e268653", ["ENVO:01001275"]),
    "habitatmech:GOLD.f8b744283b": ("habitatmech:GOLD.f8b744283b", "ENVO:00001999", ["ENVO:00012408"]),
    "habitatmech:GOLD.d61fa6c9ee": ("habitatmech:GOLD.d61fa6c9ee", "ENVO:00002011", ["ENVO:00012408"]),
    "habitatmech:GOLD.8ec9c78331": ("ENVO:00000220", "ENVO:00001999", ["ENVO:01001784"]),
}


@pytest.fixture(scope="module")
def documents():
    return {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}


def test_thirteen_exclusions_change_only_parents_and_append_history(documents, monkeypatch):
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    assert CASES.keys() <= exclusions.keys()
    monkeypatch.setattr(
        seed,
        "load_gold_parent_exclusions",
        lambda _: {key: row for key, row in exclusions.items() if key not in CASES},
    )
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == documents.keys()
    assert {key for key in before if before[key] != documents[key]} == {
        values[0] for values in CASES.values()
    }
    for source, (identifier, parent, retained) in CASES.items():
        old, new, row = before[identifier], documents[identifier], exclusions[source]
        assert row.parent_id == parent
        assert seed.mint("GOLD", row.source_path) == source
        assert parent in old["parent_habitats"]
        assert new.get("parent_habitats", []) == retained
        assert retained == [p for p in old["parent_habitats"] if p != parent]
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
def test_frozen_source_nodes_counts_and_independent_parents(source, documents):
    identifier, removed, retained = CASES[source]
    doc = documents[identifier]
    assert doc.get("parent_habitats", []) == retained
    assert removed not in retained
    row = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)[source]
    attestations = [a for a in doc["source_attestations"] if a.get("source_path") == row.source_path]
    assert len(attestations) == 1
    attestation = attestations[0]
    assert attestation["source"] == "GOLD"
    raw = next(r for r in seed.read_tsv("gold_ecosystem_paths.tsv") if r["canonical_path"] == row.source_path)
    assert raw["gold_node_ids"].split("|")[0] == attestation["source_id"]
    count = int(raw["organism_count"])
    if count:
        assert attestation["assertion_count"] == count
        assert attestation["assertion_unit"] == "ORGANISM"
    else:
        assert "assertion_count" not in attestation and "assertion_unit" not in attestation


def test_uncertain_abyssal_source_is_not_remapped_from_spelling(documents):
    doc = documents["habitatmech:GOLD.5520b30ba7"]
    assert doc["grounding_status"] == "UNGROUNDED"
    assert doc["parent_habitats"] == ["ENVO:00000207"]


def test_endpoint_defect_and_facet_interpretation_are_not_silently_changed(documents):
    for source in (
        "habitatmech:GOLD.a16a79bd0c",
        "habitatmech:GOLD.f8b744283b",
        "habitatmech:GOLD.d61fa6c9ee",
    ):
        doc = documents[source]
        assert doc["grounding_status"] == "NARROW"
        assert doc["source_attestations"][0]["mapping_predicate"] == "skos:narrowMatch"
    assert documents["habitatmech:GOLD.90a084a03e"]["grounding_status"] == "NOT_APPLICABLE"
