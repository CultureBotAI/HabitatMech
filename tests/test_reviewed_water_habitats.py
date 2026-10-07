"""Bounded publication fixes must preserve unrelated scientific assertions."""

from dataclasses import replace

from habitatmech import seed


def test_wood_fall_context_exclusion_has_exact_scope(monkeypatch):
    identifier = "ENVO:01000142"
    source = "habitatmech:GOLD.615f1a92a4"
    parent = "ENVO:01000024"
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    row = exclusions.pop(source)
    assert row.source_path == "Environmental > Aquatic > Marine > Benthic > Wood fall"
    assert row.parent_id == parent
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda path: exclusions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {identifier}
    old, new = before[identifier], after[identifier]
    assert old["parent_habitats"] == [parent, "ENVO:01000138"]
    assert new["parent_habitats"] == ["ENVO:01000138"]
    assert new["curation_history"][:-1] == old["curation_history"]
    event = new["curation_history"][-1]
    assert event["action"] == "SOURCE_PARENT_EXCLUDED"
    assert event["curator"] == "codex-gpt-5"
    assert event["timestamp"] == "2026-10-07T00:00:00Z"
    assert source in event["changes"] and parent in event["changes"]
    for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
        assert new.get(field) == old.get(field), field
    assert new["grounding_status"] == "EXACT" and new["mapping_status"] == "SEEDED"
    assert new["source_attestations"] == [{
        "source": "GOLD", "source_id": "gold.ecosystem:5712", "source_label": "Wood fall",
        "source_path": row.source_path, "mapping_predicate": "skos:exactMatch",
    }]


def test_whale_fall_parent_and_white_smoker_note_have_exact_scope(monkeypatch):
    whale, smoker = "ENVO:01000140", "ENVO:01000257"
    whale_source = "habitatmech:GOLD.6de51dbee8"
    smoker_source = "habitatmech:GOLD.d28b62ff00"
    parent = "habitatmech:GOLD.88e2b29307"
    old_note = "Leaf label equals the ENVO label exactly and no other source concept claims it."
    new_note = (
        "The plural source label is curator-recognized as equivalent to the singular ENVO "
        "label in this marine hydrothermal context; normalized labels are not equal and "
        "the automatic route is gold_unmatched. No other source concept claims this leaf."
    )
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    row = exclusions.pop(whale_source)
    assert row.parent_id == parent
    assert row.source_path == "Environmental > Aquatic > Marine > Fossil > Whale fall"
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    decision = decisions[smoker_source]
    assert new_note in decision.notes
    assert seed.norm_label("White smokers") != seed.norm_label("white smoker")
    decisions[smoker_source] = replace(decision, notes=decision.notes.replace(new_note, old_note))
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda path: exclusions)
    monkeypatch.setattr(seed, "load_decisions", lambda path: decisions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {whale, smoker}
    old, new = before[whale], after[whale]
    assert old["parent_habitats"] == ["ENVO:01000139", parent]
    assert new["parent_habitats"] == ["ENVO:01000139"]
    assert new["curation_history"][:-1] == old["curation_history"]
    event = new["curation_history"][-1]
    assert event["action"] == "SOURCE_PARENT_EXCLUDED"
    assert event["curator"] == "codex-gpt-5"
    assert event["timestamp"] == "2026-10-07T00:00:00Z"
    assert whale_source in event["changes"] and parent in event["changes"]
    for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
        assert new.get(field) == old.get(field), field
    assert new["grounding_status"] == "EXACT" and new["mapping_status"] == "SEEDED"
    assert new["source_attestations"] == [{
        "source": "GOLD", "source_id": "gold.ecosystem:4000", "source_label": "Whale fall",
        "source_path": row.source_path, "mapping_predicate": "skos:exactMatch",
    }]

    old, new = before[smoker], after[smoker]
    for field in (old.keys() | new.keys()) - {"curation_history"}:
        assert new.get(field) == old.get(field), field
    assert len(old["curation_history"]) == len(new["curation_history"]) == 2
    assert new["curation_history"][0] == {
        **old["curation_history"][0],
        "changes": old["curation_history"][0]["changes"].replace(old_note, new_note),
    }
    assert new["curation_history"][0]["curator"] == "claude-opus-5"
    assert new["curation_history"][0]["timestamp"] == "2026-08-12T00:00:00Z"
    assert new["curation_history"][1] == old["curation_history"][1]
    assert new["grounding_status"] == "EXACT" and new["mapping_status"] == "REVIEWED"
    assert new["parent_habitats"] == ["ENVO:00000215", "ENVO:01000122"]
    assert new["source_attestations"] == [{
        "source": "GOLD", "source_id": "gold.ecosystem:8303", "source_label": "White smokers",
        "source_path": "Environmental > Aquatic > Marine > Hydrothermal vents > White smokers",
        "mapping_predicate": "skos:exactMatch",
    }]


def test_wetland_area_context_exclusions_have_exact_scope(monkeypatch):
    identifier = "ENVO:00000043"
    expected = {
        "habitatmech:GOLD.5f6044871d": (
            "Environmental > Terrestrial > Soil > Wetlands", "ENVO:00001998",
        ),
        "habitatmech:GOLD.92ce88cda1": (
            "Environmental > Aquatic > Marine > Wetlands", "ENVO:00001999",
        ),
        "habitatmech:GOLD.a981586d10": (
            "Environmental > Aquatic > Freshwater > Wetlands", "ENVO:00002011",
        ),
    }
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    for source, (path, parent) in expected.items():
        row = exclusions.pop(source)
        assert (row.source_path, row.parent_id) == (path, parent)
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda path: exclusions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {identifier}
    old, new = before[identifier], after[identifier]
    assert old["parent_habitats"] == [
        "ENVO:00001998", "ENVO:00001999", "ENVO:00002011", "ENVO:01001305",
    ]
    assert new["parent_habitats"] == ["ENVO:01001305"]
    assert new["curation_history"][:-3] == old["curation_history"]
    for event, source in zip(new["curation_history"][-3:], sorted(expected), strict=True):
        assert event["action"] == "SOURCE_PARENT_EXCLUDED"
        assert event["curator"] == "codex-gpt-5"
        assert event["timestamp"] == "2026-10-07T00:00:00Z"
        assert source in event["changes"]
        assert expected[source][1] in event["changes"]
    for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
        assert new.get(field) == old.get(field), field
    assert new["grounding_status"] == "EXACT"
    assert new["mapping_status"] == "REVIEWED"
    assert len(new["characteristic_taxa"]) == 25
    assert len(new["source_attestations"]) == 4
    gold = [row for row in new["source_attestations"] if row["source"] == "GOLD"]
    assert {(row["source_id"], row["assertion_count"]) for row in gold} == {
        ("gold.ecosystem:3783", 3), ("gold.ecosystem:3795", 61),
        ("gold.ecosystem:3815", 29),
    }
    assert all(row["assertion_unit"] == "ORGANISM" for row in gold)
    assert all(row["mapping_predicate"] == "skos:exactMatch" for row in gold)
    prego = next(row for row in new["source_attestations"] if row["source"] == "PREGO")
    assert prego["assertion_count"] == 50 and prego["assertion_unit"] == "TAXON"
    assert "mapping_predicate" not in prego
    assert "ENVO:00000043" not in after["ENVO:00000233"]["parent_habitats"]


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
