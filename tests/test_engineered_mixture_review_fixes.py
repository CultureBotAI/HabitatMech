"""Bounded hierarchy and source-kind corrections for reviewed GOLD records."""

from dataclasses import replace

import pytest

from habitatmech import seed

PARENTS = {
    "habitatmech:GOLD.26717179e1": "ENVO:00002124",
    "habitatmech:GOLD.821fc6dd72": "ENVO:00002124",
    "habitatmech:GOLD.b1f94cf5f5": "ENVO:01000964",
    "habitatmech:GOLD.d64c9575e7": "habitatmech:GOLD.7c91485eb8",
    "habitatmech:GOLD.0bab26d396": "ENVO:04000007",
}
SEQUENCES = {"habitatmech:GOLD.4f2d583075", "habitatmech:GOLD.9203c1c268"}


@pytest.fixture(scope="module")
def documents():
    return {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}


def test_five_exclusions_change_only_exact_parents_and_audit(documents, monkeypatch):
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    assert PARENTS.keys() <= exclusions.keys()
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda _: {
        key: row for key, row in exclusions.items() if key not in PARENTS
    })
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == documents.keys()
    assert {key for key in before if before[key] != documents[key]} == PARENTS.keys()
    for identifier, parent in PARENTS.items():
        old, new = before[identifier], documents[identifier]
        row = exclusions[identifier]
        assert row.parent_id == parent
        assert row.source_path == new["source_attestations"][0]["source_path"]
        assert parent in old["parent_habitats"]
        assert new.get("parent_habitats", []) == [p for p in old["parent_habitats"] if p != parent]
        allowed = {"parent_habitats", "curation_history"}
        assert {k: v for k, v in old.items() if k not in allowed} == {
            k: v for k, v in new.items() if k not in allowed
        }
        assert new["curation_history"][:-1] == old["curation_history"]
        event = new["curation_history"][-1]
        assert event["action"] == "SOURCE_PARENT_EXCLUDED"
        assert event["curator"] == "codex-gpt-5"
        assert event["timestamp"] == "2026-10-11T00:00:00Z"
        assert identifier in event["changes"] and parent in event["changes"]
        assert new["mapping_status"] == "SEEDED"
    manure = documents["habitatmech:GOLD.26717179e1"]
    assert manure["parent_habitats"] == ["ENVO:03501300"]
    assert manure["grounding_status"] == "NARROW"
    assert manure["source_attestations"][0]["mapping_predicate"] == "skos:narrowMatch"


def test_sequence_decisions_change_only_two_statuses_and_history(documents, monkeypatch):
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    for identifier in SEQUENCES:
        decision = decisions[identifier]
        assert decision.decision == "NOT_APPLICABLE" and decision.review_depth == "ITEM"
        assert "https://gold.jgi.doe.gov/biosample?id=" in decision.notes
        decisions[identifier] = replace(decision, decision="CONFIRM_UNGROUNDED", review_depth="CLASS")
    monkeypatch.setattr(seed, "load_decisions", lambda _: decisions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == documents.keys()
    assert {key for key in before if before[key] != documents[key]} == SEQUENCES
    for identifier in SEQUENCES:
        old, new = before[identifier], documents[identifier]
        assert old["grounding_status"] == "UNGROUNDED" and old["mapping_status"] == "SEEDED"
        assert new["grounding_status"] == "NOT_APPLICABLE" and new["mapping_status"] == "REVIEWED"
        allowed = {"grounding_status", "mapping_status", "curation_history"}
        assert {k: v for k, v in old.items() if k not in allowed} == {
            k: v for k, v in new.items() if k not in allowed
        }
        assert new["parent_habitats"] == ["habitatmech:GOLD.5df162af13"]
    # The broader mixed-scope category and physical-mixture siblings are not reclassified.
    for identifier in (
        "habitatmech:GOLD.5df162af13", "habitatmech:GOLD.e96d7e84d0", "habitatmech:GOLD.0e7aeb7635",
    ):
        assert before[identifier] == documents[identifier]
    assert before["habitatmech:GOLD.68f3852be5"] == documents["habitatmech:GOLD.68f3852be5"]


@pytest.mark.parametrize("identifier", [*PARENTS, *sorted(SEQUENCES)])
def test_source_identity_counts_and_nodes_are_preserved(identifier, documents):
    doc = documents[identifier]
    assert doc["habitat_category"] == "ENGINEERED"
    assert len(doc["source_attestations"]) == 1
    attestation = doc["source_attestations"][0]
    assert attestation["source"] == "GOLD"
    path = attestation["source_path"]
    assert seed.mint("GOLD", path) == identifier
    raw = next(r for r in seed.read_tsv("gold_ecosystem_paths.tsv") if r["canonical_path"] == path)
    assert raw["gold_node_ids"].split("|")[0] == attestation["source_id"]
    count = int(raw["organism_count"])
    assert count == 0
    assert "assertion_count" not in attestation and "assertion_unit" not in attestation
