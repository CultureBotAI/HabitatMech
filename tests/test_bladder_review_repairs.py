"""Bladder curation must distinguish organ context from a broader site class."""

from dataclasses import replace

from jinja2 import Environment

from habitatmech import seed

POLYP = "habitatmech:GOLD.2c26547de4"
STONE_SOURCE = "habitatmech:GOLD.c245efd1e3"
STONE = "NCIT:C26707"
PARENTS = {
    POLYP: "BTO:0006350",
    STONE_SOURCE: "habitatmech:GOLD.20fae79b01",
}


def test_bladder_issue_links_exclude_prose_punctuation():
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    template = Environment(autoescape=True).from_string("{{ notes|urlize }}")
    for notes, number in [
        (parents[POLYP].notes, 2181),
        (parents[STONE_SOURCE].notes, 2182),
        (decisions[POLYP].notes, 2181),
    ]:
        url = f"https://github.com/CultureBotAI/HabitatMech/issues/{number}"
        rendered = template.render(notes=notes)
        assert f'href="{url}"' in rendered
        assert f'href="{url}:"' not in rendered


def test_bladder_repairs_preserve_unrelated_corpus_and_source_evidence(monkeypatch):
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    assert PARENTS.keys() <= parents.keys()
    assert decisions[POLYP].decision == "CONFIRM_UNGROUNDED"
    assert decisions[POLYP].relation == "xref"
    assert decisions[POLYP].object_id == "UBERON:0001255"
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    old_decision = replace(
        decisions[POLYP], decision="GROUND_AS_PARENT", relation="parent",
        grounding_status="NARROW", curator="claude-opus-5", date="2026-08-13",
        notes="A bladder polyp, not the bladder. GOLD's path places it under Benign tumor. "
        "Path: Host-associated > Mammals: Human > Benign tumor > Polyps > Bladder",
    )
    with monkeypatch.context() as old:
        old.setattr(seed, "load_gold_parent_exclusions", lambda _: {
            key: row for key, row in parents.items() if key not in PARENTS
        })
        old.setattr(seed, "load_decisions", lambda _: {**decisions, POLYP: old_decision})
        before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {POLYP, STONE}
    for key in (POLYP, STONE):
        allowed = {"parent_habitats", "curation_history"}
        if key == POLYP:
            allowed |= {"grounding_status", "source_attestations", "xrefs"}
        assert {k: v for k, v in before[key].items() if k not in allowed} == {
            k: v for k, v in after[key].items() if k not in allowed
        }
        assert after[key]["mapping_status"] == "REVIEWED"

    assert before[POLYP]["parent_habitats"] == ["BTO:0006350", "UBERON:0001255"]
    assert not after[POLYP].get("parent_habitats")
    assert after[POLYP]["xrefs"] == ["UBERON:0001255"]
    assert after[POLYP]["grounding_status"] == "UNGROUNDED"
    assert after[POLYP]["source_attestations"] == [
        {k: v for k, v in att.items() if k != "mapping_predicate"}
        for att in before[POLYP]["source_attestations"]
    ]
    assert "assertion_count" not in after[POLYP]["source_attestations"][0]
    assert "assertion_unit" not in after[POLYP]["source_attestations"][0]
    old_seed = next(e for e in before[POLYP]["curation_history"]
                    if e["action"] == "SEEDED_FROM_SOURCES")
    new_seed = next(e for e in after[POLYP]["curation_history"]
                    if e["action"] == "SEEDED_FROM_SOURCES")
    assert new_seed == {
        **old_seed, "changes": old_seed["changes"].replace("NARROW", "UNGROUNDED"),
    }
    assert len(after[POLYP]["curation_history"]) == 3
    assert {e["action"] for e in after[POLYP]["curation_history"]} >= {
        "CONFIRM_UNGROUNDED", "SOURCE_PARENT_EXCLUDED",
    }

    assert before[STONE]["parent_habitats"] == ["NCIT:C26905", PARENTS[STONE_SOURCE]]
    assert after[STONE]["parent_habitats"] == ["NCIT:C26905"]
    assert after[STONE]["grounding_status"] == "CLOSE"
    assert after[STONE]["curation_history"][:-1] == before[STONE]["curation_history"]
    assert after[STONE]["curation_history"][-1]["action"] == "SOURCE_PARENT_EXCLUDED"
    assert {(a["source"], a["assertion_count"], a["assertion_unit"])
            for a in after[STONE]["source_attestations"]} == {
        ("BACDIVE", 7, "STRAIN"), ("GOLD", 1, "ORGANISM"),
    }
    assert {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts} == after
