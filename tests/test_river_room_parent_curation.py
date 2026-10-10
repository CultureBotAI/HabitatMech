"""Distinguish watercourses, water material and room surfaces from their context."""

from habitatmech import seed
from habitatmech.text_map_inputs import build_context, semantic_text


CASES = {
    "habitatmech:GOLD.33a923764f": (
        "ENVO:00000022", "ENVO:00002001", ["ENVO:00000023"], "EXACT", "REVIEWED",
    ),
    "habitatmech:GOLD.5a98f4a82a": (
        "ENVO:01000599", "ENVO:01000620", ["ENVO:03605006"], "EXACT", "SEEDED",
    ),
    "habitatmech:GOLD.5c998a4ea9": (
        "habitatmech:GOLD.5c998a4ea9", "habitatmech:GOLD.9cc7667041", [],
        "UNGROUNDED", "SEEDED",
    ),
}


def test_context_exclusions_preserve_all_other_claims_and_records(monkeypatch):
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    monkeypatch.setattr(
        seed, "load_gold_parent_exclusions",
        lambda _: {key: row for key, row in exclusions.items() if key not in CASES},
    )
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    changed = {case[0] for case in CASES.values()}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == changed
    context = build_context(seed.REPO_ROOT)
    assert {key for key in before
            if semantic_text(before[key], context) != semantic_text(after[key], context)} == changed

    for source_id, (target_id, parent_id, retained, grounding, status) in CASES.items():
        old, new = before[target_id], after[target_id]
        exclusion = exclusions[source_id]
        assert exclusion.parent_id == parent_id
        assert set(old["parent_habitats"]) == {parent_id, *retained}
        assert new.get("parent_habitats", []) == retained
        assert new["curation_history"][:-1] == old["curation_history"]
        event = new["curation_history"][-1]
        assert event["action"] == "SOURCE_PARENT_EXCLUDED"
        assert event["timestamp"] == "2026-10-10T00:00:00Z"
        assert event["curator"] == "codex-gpt-5"
        assert exclusion.notes in event["changes"]
        for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
            assert new.get(field) == old.get(field), (target_id, field)
        assert (new["grounding_status"], new["mapping_status"]) == (grounding, status)
        attestation = next(a for a in new["source_attestations"] if a["source"] == "GOLD")
        assert attestation["source_path"] == exclusion.source_path
        assert seed.mint("GOLD", attestation["source_path"]) == source_id
        assert "assertion_count" not in attestation
        assert "assertion_unit" not in attestation
