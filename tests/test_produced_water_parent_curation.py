"""Keep petroleum produced-water material distinct from its reservoir landform."""

from habitatmech import seed
from habitatmech.text_map_inputs import build_context, semantic_text

WATER = "habitatmech:GOLD.bfd6bfa0f1"
RESERVOIR = "ENVO:00002185"


def test_produced_water_exclusion_preserves_other_claims_and_records(monkeypatch):
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    monkeypatch.setattr(
        seed, "load_gold_parent_exclusions",
        lambda _: {key: row for key, row in exclusions.items() if key != WATER},
    )
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {WATER}
    context = build_context(seed.REPO_ROOT)
    assert {key for key in before
            if semantic_text(before[key], context) != semantic_text(after[key], context)} == {WATER}

    old, new = before[WATER], after[WATER]
    exclusion = exclusions[WATER]
    assert exclusion.parent_id == RESERVOIR
    assert old["parent_habitats"] == [RESERVOIR]
    assert "parent_habitats" not in new
    assert new["curation_history"][:-1] == old["curation_history"]
    event = new["curation_history"][-1]
    assert event["action"] == "SOURCE_PARENT_EXCLUDED"
    assert event["timestamp"] == "2026-10-10T00:00:00Z"
    assert event["curator"] == "codex-gpt-5"
    assert exclusion.notes in event["changes"]
    for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
        assert new.get(field) == old.get(field), field
    assert (new["grounding_status"], new["mapping_status"]) == ("UNGROUNDED", "SEEDED")
    assert new["source_attestations"] == [{
        "source": "GOLD", "source_id": "gold.ecosystem:7639", "source_label": "Produced water",
        "source_path": (
            "Engineered > Wastewater > Industrial wastewater > Petroleum reservoir > Produced water"
        ),
        "assertion_count": 1, "assertion_unit": "ORGANISM",
    }]
    attestation = new["source_attestations"][0]
    assert attestation["source_path"] == exclusion.source_path
    assert seed.mint("GOLD", attestation["source_path"]) == WATER
    assert seed.load_decisions(seed.DECISIONS_PATH)[WATER].review_depth == "CLASS"
