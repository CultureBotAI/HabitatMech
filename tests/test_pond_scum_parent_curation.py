"""Keep sampled pond scum distinct from its enclosing constructed pond."""

from habitatmech import seed
from habitatmech.text_map_inputs import build_context, semantic_text

SCUM = "habitatmech:GOLD.6e0470a1d8"
POND = "habitatmech:GOLD.e474187df8"


def test_scum_exclusion_preserves_all_other_claims_and_records(monkeypatch):
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    monkeypatch.setattr(
        seed, "load_gold_parent_exclusions",
        lambda _: {key: row for key, row in exclusions.items() if key != SCUM},
    )
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {SCUM}
    context = build_context(seed.REPO_ROOT)
    assert {key for key in before
            if semantic_text(before[key], context) != semantic_text(after[key], context)} == {SCUM}

    old, new = before[SCUM], after[SCUM]
    exclusion = exclusions[SCUM]
    assert exclusion.parent_id == POND
    assert old["parent_habitats"] == [POND]
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
        "source": "GOLD", "source_id": "gold.ecosystem:8140", "source_label": "Pond scum",
        "source_path": "Engineered > Artificial ecosystem > Aquaculture > Algae raceway pond > Pond scum",
    }]
    attestation = new["source_attestations"][0]
    assert attestation["source_path"] == exclusion.source_path
    assert seed.mint("GOLD", attestation["source_path"]) == SCUM
    assert seed.load_decisions(seed.DECISIONS_PATH)[SCUM].review_depth == "CLASS"
