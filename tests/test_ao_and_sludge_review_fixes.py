"""Scoped corrections for A/O settings and source-qualified sludge materials."""

from dataclasses import replace

import pytest

from habitatmech import seed

SYSTEM = "habitatmech:GOLD.7c91485eb8"
BIOREACTOR = "habitatmech:GOLD.bf15464676"
TARGETS = {
    "habitatmech:GOLD.bf15464676": (
        "habitatmech:GOLD.7c91485eb8",
        "Engineered > WWTP > A/O treatment system > A/O bioreactor",
    ),
    "habitatmech:GOLD.7c91485eb8": ("ENVO:00002043", "Engineered > WWTP > A/O treatment system"),
    "habitatmech:GOLD.6ba6dd1c82": (
        "habitatmech:GOLD.bb0eb00ccb",
        "Engineered > Wastewater > Nutrient removal > Dissolved organics (anaerobic) > Activated sludge",
    ),
    "habitatmech:GOLD.adf7e16a3a": ("ENVO:00002126", "Engineered > Bioreactor > Aerobic > Activated sludge"),
    "habitatmech:GOLD.25b680d9bc": (
        "habitatmech:GOLD.4a2450370b",
        "Engineered > Bioreactor > EBPR > Anaerobic-Aerobic > Activated sludge",
    ),
    "habitatmech:GOLD.dab267c443": (
        "habitatmech:GOLD.17461837d0",
        "Engineered > Wastewater > Nutrient removal > Dissolved organics (aerobic) > Activated sludge",
    ),
    "habitatmech:GOLD.43c33f3ecc": (
        "habitatmech:GOLD.353a834cfd",
        "Engineered > Sewage treatment plant > Wastewater > Activated sludge",
    ),
    "habitatmech:GOLD.f459151394": (
        "habitatmech:GOLD.5e086933bc",
        "Engineered > Bioreactor > Wastewater > Activated sludge",
    ),
    "habitatmech:GOLD.cc5ac8910b": (
        "habitatmech:GOLD.03345a3f86",
        "Engineered > Wastewater > Nutrient removal > Biological phosphorus removal > Activated sludge",
    ),
    "habitatmech:GOLD.2edc84b874": (
        "habitatmech:GOLD.c07aaa941d",
        "Engineered > Bioreactor > SBR-EBPR > Anaerobic-Aerobic > Activated sludge",
    ),
    "habitatmech:GOLD.032b7dd40b": ("ENVO:00002043", "Engineered > WWTP > Activated sludge"),
    "habitatmech:GOLD.5d1a568147": (
        "habitatmech:GOLD.bf15464676",
        "Engineered > WWTP > A/O treatment system > A/O bioreactor > Activated sludge",
    ),
    "habitatmech:GOLD.645add8636": (
        "ENVO:00003043",
        "Engineered > Sewage treatment plant > Activated sludge",
    ),
    "habitatmech:GOLD.090dc47d34": (
        "habitatmech:GOLD.9ab362de60",
        "Engineered > Bioremediation > Terephthalate > Wastewater > Activated sludge",
    ),
    "habitatmech:GOLD.9d25d6d7ef": (
        "habitatmech:GOLD.03fc563fae",
        "Engineered > WWTP > Aerobic digester > Activated sludge",
    ),
    "habitatmech:GOLD.0d353772af": ("ENVO:00002001", "Engineered > Wastewater > Activated Sludge"),
    "habitatmech:GOLD.81ee86290d": (
        "ENVO:03600010",
        "Engineered > Bioreactor > MBR (Membrane bioreactor) > Activated sludge",
    ),
}


@pytest.fixture(scope="module")
def documents():
    return {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}


def test_context_exclusions_preserve_exact_corpus_scope(documents, monkeypatch):
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    assert TARGETS.keys() <= exclusions.keys()
    monkeypatch.setattr(
        seed,
        "load_gold_parent_exclusions",
        lambda _: {key: row for key, row in exclusions.items() if key not in TARGETS},
    )
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == documents.keys()
    assert {key for key in before if before[key] != documents[key]} == TARGETS.keys()
    for identifier, (parent, source_path) in TARGETS.items():
        old, new = before[identifier], documents[identifier]
        row = exclusions[identifier]
        assert row.source_path == source_path and row.parent_id == parent
        assert row.curator == "codex-gpt-5" and row.date == "2026-10-10"
        assert parent in old["parent_habitats"]
        assert new.get("parent_habitats", []) == [
            value for value in old["parent_habitats"] if value != parent
        ]
        allowed = {"parent_habitats", "curation_history"}
        assert {k: v for k, v in old.items() if k not in allowed} == {
            k: v for k, v in new.items() if k not in allowed
        }
        additions = [event for event in new["curation_history"] if event not in old["curation_history"]]
        assert len(additions) == 1
        event = additions[0]
        assert [e for e in new["curation_history"] if e != event] == old["curation_history"]
        assert event["action"] == "SOURCE_PARENT_EXCLUDED"
        assert event["curator"] == "codex-gpt-5"
        assert identifier in event["changes"] and parent in event["changes"]
        assert source_path in event["changes"] and row.notes in event["changes"]


def test_system_decision_changes_only_applicability_and_history(documents, monkeypatch):
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    decision = decisions[SYSTEM]
    assert decision.decision == "CONFIRM_UNGROUNDED"
    assert decision.review_depth == "ITEM"
    decisions[SYSTEM] = replace(decision, decision="NOT_APPLICABLE")
    monkeypatch.setattr(seed, "load_decisions", lambda _: decisions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == documents.keys()
    assert {key for key in before if before[key] != documents[key]} == {SYSTEM}
    old, new = before[SYSTEM], documents[SYSTEM]
    assert old["grounding_status"] == "NOT_APPLICABLE"
    assert new["grounding_status"] == "UNGROUNDED"
    assert new["mapping_status"] == "REVIEWED"
    allowed = {"grounding_status", "curation_history"}
    assert {k: v for k, v in old.items() if k not in allowed} == {
        k: v for k, v in new.items() if k not in allowed
    }


@pytest.mark.parametrize("identifier", TARGETS)
def test_source_identity_and_native_status_are_preserved(identifier, documents):
    doc = documents[identifier]
    assert doc["habitat_category"] == "ENGINEERED"
    assert len(doc["source_attestations"]) == 1
    attestation = doc["source_attestations"][0]
    path = TARGETS[identifier][1]
    assert attestation["source"] == "GOLD" and attestation["source_path"] == path
    assert seed.mint("GOLD", path) == identifier
    raw = next(row for row in seed.read_tsv("gold_ecosystem_paths.tsv") if row["canonical_path"] == path)
    assert raw["gold_node_ids"].split("|")[0] == attestation["source_id"]
    count = int(raw["organism_count"])
    if count:
        assert attestation["assertion_count"] == count
        assert attestation["assertion_unit"] == "ORGANISM"
    else:
        assert "assertion_count" not in attestation and "assertion_unit" not in attestation
    if identifier in {SYSTEM, BIOREACTOR}:
        assert doc["grounding_status"] == "UNGROUNDED"
        assert doc["mapping_status"] == ("REVIEWED" if identifier == SYSTEM else "SEEDED")
        assert not doc.get("parent_habitats")
        assert "mapping_predicate" not in attestation
    else:
        assert doc["grounding_status"] == "NARROW"
        assert doc["mapping_status"] == "SEEDED"
        assert doc["parent_habitats"] == ["ENVO:00002046"]
        # Hierarchy-only fixes do not resolve the separate endpoint contract #1398.
        assert attestation["mapping_predicate"] == "skos:narrowMatch"
