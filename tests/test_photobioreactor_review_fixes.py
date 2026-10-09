"""Keep photobioreactor identity independent of one application context."""

from dataclasses import replace

from habitatmech import seed
from habitatmech.text_map_inputs import build_context, semantic_text

IDENTIFIER = "ENVO:03600077"
SOURCE = "habitatmech:GOLD.96bbd55dce"
PATH = "Engineered > Artificial ecosystem > Aquaculture > Photobioreactor (PBR)"
PARENT = "habitatmech:GOLD.0287e1b2a9"


def documents():
    return {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}


def test_context_exclusion_preserves_sources_status_and_other_records(monkeypatch):
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    exclusion = exclusions[SOURCE]
    assert exclusion.source_path == PATH
    assert exclusion.parent_id == PARENT
    assert seed.mint("GOLD", PATH) == SOURCE
    after = documents()
    monkeypatch.setattr(
        seed, "load_gold_parent_exclusions",
        lambda _: {key: row for key, row in exclusions.items() if key != SOURCE},
    )
    before = documents()
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {IDENTIFIER}
    context = build_context(seed.REPO_ROOT)
    assert {key for key in before
            if semantic_text(before[key], context) != semantic_text(after[key], context)} == {
        IDENTIFIER,
    }
    old, new = before[IDENTIFIER], after[IDENTIFIER]
    assert old["parent_habitats"] == ["ENVO:00002123", PARENT]
    assert new["parent_habitats"] == ["ENVO:00002123"]
    assert new["curation_history"][:-1] == old["curation_history"]
    event = new["curation_history"][-1]
    assert event["action"] == "SOURCE_PARENT_EXCLUDED"
    assert event["timestamp"] == "2026-10-09T00:00:00Z"
    assert event["curator"] == "codex-gpt-5"
    assert exclusion.notes in event["changes"]
    for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
        assert new.get(field) == old.get(field), field
    assert new["grounding_status"] == "EXACT"
    assert new["mapping_status"] == "REVIEWED"
    assert new["habitat_category"] == "ENGINEERED"
    assert new["synonyms"] == [{
        "synonym_text": "Photobioreactor (PBR)",
        "synonym_type": "EXACT_SYNONYM", "source": "GOLD",
    }]
    direct, aquaculture = new["source_attestations"]
    assert direct["source_path"] == "Engineered > Bioreactor > Photobioreactor (PBR)"
    assert direct["source_id"] == "gold.ecosystem:5844"
    assert direct["assertion_count"] == 1 and direct["assertion_unit"] == "ORGANISM"
    assert aquaculture["source_path"] == PATH
    assert aquaculture["source_id"] == "gold.ecosystem:7996"
    assert "assertion_count" not in aquaculture and "assertion_unit" not in aquaculture
    assert all(a["mapping_predicate"] == "skos:exactMatch" for a in (direct, aquaculture))
    rows = {r["canonical_path"]: r for r in seed.read_tsv("gold_ecosystem_paths.tsv")}
    assert rows[direct["source_path"]]["gold_node_ids"].split("|") == [
        "gold.ecosystem:5844", "gold.ecosystem:8184", "gold.ecosystem:8185",
    ]
    assert rows[PATH]["gold_node_ids"].split("|") == [
        "gold.ecosystem:7996", "gold.ecosystem:7997",
    ]
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    assert all(decisions[seed.mint("GOLD", a["source_path"])].review_depth == "ITEM"
               for a in (direct, aquaculture))


def test_note_correction_changes_only_one_generated_history_string(monkeypatch):
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    decision = decisions[SOURCE]
    assert decision.notes == "Parenthetical is just the acronym. Path: " + PATH
    assert (decision.decision, decision.object_id, decision.object_label) == (
        "GROUND", IDENTIFIER, "photobioreactor",
    )
    assert (decision.date, decision.curator, decision.review_depth) == (
        "2026-08-12", "claude-opus-5", "ITEM",
    )
    after = documents()
    monkeypatch.setattr(seed, "load_decisions", lambda _: {
        **decisions, SOURCE: replace(decision, notes=decision.notes[:-1]),
    })
    before = documents()
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {IDENTIFIER}
    old, new = before[IDENTIFIER], after[IDENTIFIER]
    for field in (old.keys() | new.keys()) - {"curation_history"}:
        assert new.get(field) == old.get(field), field
    old_events, new_events = old["curation_history"], new["curation_history"]
    assert len(old_events) == len(new_events)
    changes = [(a, b) for a, b in zip(old_events, new_events, strict=True) if a != b]
    assert len(changes) == 1
    old_event, new_event = changes[0]
    assert old_event["action"] == "GROUND"
    assert new_event == {
        **old_event,
        "changes": old_event["changes"].replace("(PBR (source concept", "(PBR) (source concept"),
    }
    context = build_context(seed.REPO_ROOT)
    assert all(semantic_text(before[key], context) == semantic_text(after[key], context)
               for key in before)
