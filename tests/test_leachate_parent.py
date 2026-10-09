"""A source landfill context is not a proven strict genus of leachate liquid."""

from habitatmech import seed
from habitatmech.curate.gold_parent_exclusions import load_gold_parent_exclusions
from habitatmech.text_map_inputs import semantic_text


def test_leachate_exclusion_preserves_every_other_record_and_claim(monkeypatch):
    identifier = "habitatmech:GOLD.6898d82b83"
    parent = "habitatmech:GOLD.0f40aa60ce"
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    monkeypatch.setattr(
        seed, "load_gold_parent_exclusions",
        lambda path: {key: row for key, row in exclusions.items() if key != identifier},
    )
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {identifier}
    old, new = before[identifier], after[identifier]
    assert old["parent_habitats"] == ["ENVO:00002141", parent]
    assert new["parent_habitats"] == ["ENVO:00002141"]
    assert new["curation_history"][:-1] == old["curation_history"]
    event = new["curation_history"][-1]
    assert event["action"] == "SOURCE_PARENT_EXCLUDED"
    assert event["curator"] == "codex-gpt-5"
    assert event["timestamp"] == "2026-10-09T00:00:00Z"
    assert identifier in event["changes"]
    assert parent in event["changes"]
    for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
        assert new.get(field) == old.get(field), field
    assert new["grounding_status"] == "NARROW"
    assert new["mapping_status"] == "SEEDED"
    assert new["habitat_category"] == "ENGINEERED"
    assert len(new["source_attestations"]) == 1
    attestation = new["source_attestations"][0]
    assert attestation["source_id"] == "gold.ecosystem:5666"
    assert attestation["source_path"] == exclusions[identifier].source_path
    assert seed.mint("GOLD", attestation["source_path"]) == identifier
    assert exclusions[identifier].parent_id == parent
    assert "assertion_count" not in attestation
    assert "assertion_unit" not in attestation
    assert "2 GOLD ecosystem node ids" in attestation["notes"]
    # The unrelated endpoint contract (#1398) is deliberately not changed here.
    assert attestation["mapping_predicate"] == "skos:narrowMatch"
    labels = {key: value["label"] for key, value in after.items()}
    assert semantic_text(new, labels) == semantic_text(old, labels).replace(
        "broader habitat: Municipal landfill\n", ""
    )
