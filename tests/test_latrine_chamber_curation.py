"""A chamber label does not justify a solid-waste material genus."""

from habitatmech import seed
from habitatmech.text_map_inputs import semantic_text


def test_latrine_exclusion_changes_only_context_parent_and_audit(monkeypatch):
    identifier = "habitatmech:GOLD.23dcd93012"
    path = "Engineered > Solid waste > Latrine chamber"
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    exclusion = exclusions.pop(identifier)
    assert exclusion.source_path == path
    assert exclusion.parent_id == "mesh:D062611"
    assert seed.mint("GOLD", path) == identifier
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda _: exclusions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {identifier}
    old, new = before[identifier], after[identifier]
    assert old["parent_habitats"] == ["mesh:D062611"]
    assert "parent_habitats" not in new
    assert new["curation_history"][:-1] == old["curation_history"]
    event = new["curation_history"][-1]
    assert event["action"] == "SOURCE_PARENT_EXCLUDED"
    assert event["timestamp"] == "2026-10-09T00:00:00Z"
    assert event["curator"] == "codex-gpt-5"
    assert all(value in event["changes"] for value in (identifier, path, "mesh:D062611"))
    for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
        assert new.get(field) == old.get(field), field
    assert new["grounding_status"] == "UNGROUNDED"
    assert new["mapping_status"] == "SEEDED"
    assert new["source_attestations"] == [{
        "source": "GOLD", "source_id": "gold.ecosystem:4952",
        "source_label": "Latrine chamber", "source_path": path,
    }]
    assert new["curation_history"][0]["action"] == "CONFIRM_UNGROUNDED"
    assert "[CLASS-level]" in new["curation_history"][0]["changes"]
    child = after["habitatmech:GOLD.aab5671566"]
    assert child["parent_habitats"] == ["ENVO:00002170", identifier]
    row = next(r for r in seed.read_tsv("gold_ecosystem_paths.tsv")
               if r["canonical_path"] == path)
    assert row["gold_node_ids"] == "gold.ecosystem:4952"
    context = {"mesh:D062611": "Solid Waste"}
    assert semantic_text(new, context) != semantic_text(old, context)
