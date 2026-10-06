"""Bounded publication fixes must preserve unrelated scientific assertions."""

from dataclasses import replace

from habitatmech import seed


def test_well_context_and_watercourse_note_corrections_have_exact_scope(monkeypatch):
    well = "ENVO:00000026"
    biofilm = "habitatmech:GOLD.1f74489d04"
    watercourse = "ENVO:00000029"
    well_source = "habitatmech:GOLD.0d87c411c3"
    watercourse_source = "habitatmech:BACDIVE.1106e09fbe"
    parent = "habitatmech:GOLD.22a80cbd14"
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = {
        key: row for key, row in seed.load_gold_parent_exclusions(
            seed.GOLD_PARENT_EXCLUSIONS_PATH
        ).items() if key not in {well_source, biofilm}
    }
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    decision = decisions[watercourse_source]
    assert "existing PREGO watercourse record" in decision.notes
    decisions[watercourse_source] = replace(
        decision, notes=decision.notes.replace(
            "existing PREGO watercourse record", "existing GOLD watercourse record"
        ),
    )
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda path: exclusions)
    monkeypatch.setattr(seed, "load_decisions", lambda path: decisions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {
        well, biofilm, watercourse,
    }
    for identifier in (well, biofilm):
        old, new = before[identifier], after[identifier]
        assert parent in old["parent_habitats"]
        assert new.get("parent_habitats", []) == [
            value for value in old["parent_habitats"] if value != parent
        ]
        assert new["curation_history"][:-1] == old["curation_history"]
        event = new["curation_history"][-1]
        assert event["action"] == "SOURCE_PARENT_EXCLUDED"
        assert event["curator"] == "codex-gpt-5"
        assert event["timestamp"] == "2026-10-06T00:00:00Z"
        for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
            assert new.get(field) == old.get(field), (identifier, field)
        assert new["mapping_status"] == "SEEDED"

    assert after[well]["parent_habitats"] == ["ENVO:00000002"]
    assert after[well]["grounding_status"] == "EXACT"
    assert after[well]["source_attestations"] == [{
        "source": "GOLD", "source_id": "gold.ecosystem:8262", "source_label": "Well",
        "source_path": "Environmental > Aquatic > Deep subsurface > Groundwater > Well",
        "mapping_predicate": "skos:exactMatch",
        "assertion_count": 1, "assertion_unit": "ORGANISM",
    }]
    assert after[biofilm]["grounding_status"] == "UNGROUNDED"
    assert after[biofilm]["source_attestations"] == [{
        "source": "GOLD", "source_id": "gold.ecosystem:5960", "source_label": "Well biofilm",
        "source_path": (
            "Environmental > Aquatic > Deep subsurface > Groundwater > Well biofilm"
        ),
    }]
    old, new = before[watercourse], after[watercourse]
    for field in (old.keys() | new.keys()) - {"curation_history"}:
        assert new.get(field) == old.get(field), field
    assert len(old["curation_history"]) == len(new["curation_history"])
    changes = 0
    for old_event, new_event in zip(old["curation_history"], new["curation_history"], strict=True):
        if old_event != new_event:
            changes += 1
            assert new_event == {
                **old_event,
                "changes": old_event["changes"].replace(
                    "existing GOLD watercourse record", "existing PREGO watercourse record"
                ),
            }
    assert changes == 1


def test_well_sediment_context_exclusion_has_exact_scope(monkeypatch):
    identifier = "habitatmech:GOLD.71a5958fdc"
    parent = "habitatmech:GOLD.22a80cbd14"
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    exclusion = exclusions.pop(identifier)
    assert exclusion.parent_id == parent
    assert exclusion.source_path == (
        "Environmental > Aquatic > Deep subsurface > Groundwater > Well sediment"
    )
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda path: exclusions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {identifier}
    old, new = before[identifier], after[identifier]
    assert old["parent_habitats"] == [parent]
    assert "parent_habitats" not in new
    assert new["curation_history"][:-1] == old["curation_history"]
    event = new["curation_history"][-1]
    assert event["action"] == "SOURCE_PARENT_EXCLUDED"
    assert event["curator"] == "codex-gpt-5"
    assert event["timestamp"] == "2026-10-06T00:00:00Z"
    assert identifier in event["changes"] and parent in event["changes"]
    for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
        assert new.get(field) == old.get(field), field
    assert new["grounding_status"] == "UNGROUNDED"
    assert new["mapping_status"] == "SEEDED"
    assert "[CLASS-level]" in new["curation_history"][0]["changes"]
    assert new["source_attestations"] == [{
        "source": "GOLD", "source_id": "gold.ecosystem:5959", "source_label": "Well sediment",
        "source_path": exclusion.source_path,
        "assertion_count": 1, "assertion_unit": "ORGANISM",
    }]
