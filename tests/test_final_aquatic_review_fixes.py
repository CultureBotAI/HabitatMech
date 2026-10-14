"""Exact-source hierarchy corrections for the final aquatic review cohort."""

import pytest

from habitatmech import seed

CASES = {
    "habitatmech:GOLD.486b52b120": {
        "source": "habitatmech:GOLD.486b52b120",
        "path": "Environmental > Aquatic > Thermal springs > Warm (34-42C)",
        "removed": "ENVO:00000051",
        "retained": [],
        "nodes": "gold.ecosystem:3759|gold.ecosystem:3986",
        "count": 1,
        "grounding": "NOT_APPLICABLE",
        "status": "REVIEWED",
    },
    "habitatmech:GOLD.cea7ead8dd": {
        "source": "habitatmech:GOLD.cea7ead8dd",
        "path": "Environmental > Aquatic > Marine > Waste",
        "removed": "ENVO:00001999",
        "retained": [],
        "nodes": "gold.ecosystem:8417|gold.ecosystem:8420",
        "count": 5,
        "grounding": "UNGROUNDED",
        "status": "SEEDED",
    },
    "ENVO:03501254": {
        "source": "habitatmech:GOLD.1c5da9f7f3",
        "path": "Environmental > Aquatic > Freshwater > Water tank",
        "removed": "ENVO:00002011",
        "retained": ["ENVO:00003074"],
        "nodes": "gold.ecosystem:5209|gold.ecosystem:5210",
        "count": 36,
        "grounding": "EXACT",
        "status": "SEEDED",
    },
}


@pytest.fixture(scope="module")
def documents():
    return {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}


def test_only_three_records_change_in_parents_and_appended_history(documents, monkeypatch):
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    sources = {case["source"] for case in CASES.values()}
    assert sources <= exclusions.keys()
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda _: {
        key: value for key, value in exclusions.items() if key not in sources
    })
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == documents.keys()
    assert {key for key in before if before[key] != documents[key]} == CASES.keys()
    for identifier, case in CASES.items():
        old, new = before[identifier], documents[identifier]
        assert sorted(set(old["parent_habitats"]) - {case["removed"]}) == case["retained"]
        assert new.get("parent_habitats", []) == case["retained"]
        allowed = {"parent_habitats", "curation_history"}
        assert {k: v for k, v in old.items() if k not in allowed} == {
            k: v for k, v in new.items() if k not in allowed
        }
        added = [e for e in new["curation_history"] if e not in old["curation_history"]]
        assert len(added) == 1
        assert [e for e in new["curation_history"] if e not in added] == old["curation_history"]
        event = added[0]
        assert event["action"] == "SOURCE_PARENT_EXCLUDED"
        assert event["curator"] == "codex-gpt-5"
        assert event["timestamp"] == "2026-10-14T00:00:00Z"
        assert exclusions[case["source"]].notes in event["changes"]


@pytest.mark.parametrize("identifier", CASES)
def test_source_guards_counts_units_and_status_are_preserved(identifier, documents):
    case, doc = CASES[identifier], documents[identifier]
    row = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)[case["source"]]
    assert row.source_path == case["path"]
    assert seed.mint("GOLD", row.source_path) == case["source"]
    assert row.parent_id == case["removed"]
    raw = next(r for r in seed.read_tsv("gold_ecosystem_paths.tsv")
               if r["canonical_path"] == case["path"])
    assert raw["gold_node_ids"] == case["nodes"]
    assert int(raw["organism_count"]) == case["count"]
    assert len(doc["source_attestations"]) == 1
    attestation = doc["source_attestations"][0]
    assert attestation["source"] == "GOLD"
    assert attestation["source_path"] == case["path"]
    assert attestation["source_id"] == case["nodes"].split("|")[0]
    assert attestation["assertion_count"] == case["count"]
    assert attestation["assertion_unit"] == "ORGANISM"
    assert doc["grounding_status"] == case["grounding"]
    assert doc["mapping_status"] == case["status"]
    assert doc.get("parent_habitats", []) == case["retained"]


def test_waste_scope_is_not_invented_and_water_tank_retains_container_identity(documents):
    waste = documents["habitatmech:GOLD.cea7ead8dd"]
    assert "definition" not in waste
    decision = seed.load_decisions(seed.DECISIONS_PATH)[waste["identifier"]]
    assert decision.review_depth == "CLASS"
    tank = documents["ENVO:03501254"]
    assert tank["definition"] == "A container for storing water."
    assert tank["definition_source"] == "ENVO"
    assert tank["source_attestations"][0]["mapping_predicate"] == "skos:exactMatch"
