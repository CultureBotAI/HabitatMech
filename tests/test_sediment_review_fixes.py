"""Two exact sediment corrections preserve every unrelated generated claim."""

from dataclasses import replace

from habitatmech import seed

SODA = "habitatmech:GOLD.faaf9502b6"
WETLAND = "habitatmech:GOLD.98d936714f"


def documents():
    return {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}


def test_sediment_context_exclusions_are_independent_of_material_genus(monkeypatch):
    after = documents()
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    monkeypatch.setattr(
        seed, "load_gold_parent_exclusions",
        lambda path: {key: row for key, row in exclusions.items() if key not in {SODA, WETLAND}},
    )
    before = documents()
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {SODA, WETLAND}
    for identifier, parent, node, count, status in (
        (SODA, "habitatmech:GOLD.b11bdfbd7c", "gold.ecosystem:7889", 91, "REVIEWED"),
        (WETLAND, "ENVO:00000043", "gold.ecosystem:4183", 20, "SEEDED"),
    ):
        old, new = before[identifier], after[identifier]
        assert old["parent_habitats"] == sorted(["ENVO:00002007", parent])
        assert new["parent_habitats"] == ["ENVO:00002007"]
        assert new["curation_history"][:-1] == old["curation_history"]
        assert new["curation_history"][-1]["action"] == "SOURCE_PARENT_EXCLUDED"
        assert new["curation_history"][-1]["curator"] == "codex-gpt-5"
        for field in old.keys() | new.keys():
            if field not in {"parent_habitats", "curation_history"}:
                assert old.get(field) == new.get(field), (identifier, field)
        assert new["grounding_status"] == "NARROW"
        assert new["mapping_status"] == status
        assert new["source_attestations"] == [{
            "source": "GOLD", "source_id": node, "source_label": "Sediment",
            "source_path": exclusions[identifier].source_path,
            "mapping_predicate": "skos:narrowMatch", "assertion_count": count,
            "assertion_unit": "ORGANISM",
        }]


def test_soda_sediment_decision_uses_material_without_merging_identity(monkeypatch):
    after = documents()
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    current = decisions[SODA]
    assert current.decision == "GROUND_AS_PARENT"
    assert current.object_id == "ENVO:00002007"
    assert current.review_depth == "ITEM"
    old = replace(current, object_id="ENVO:00000019", object_label="saline lake")
    monkeypatch.setattr(seed, "load_decisions", lambda path: {**decisions, SODA: old})
    before = documents()
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {SODA}
    assert before[SODA]["parent_habitats"] == ["ENVO:00000019"]
    assert after[SODA]["parent_habitats"] == ["ENVO:00002007"]
    for field in before[SODA].keys() | after[SODA].keys():
        if field not in {"parent_habitats", "curation_history"}:
            assert before[SODA].get(field) == after[SODA].get(field)
