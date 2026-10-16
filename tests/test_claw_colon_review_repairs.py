"""Constrain reviewed context, synonym and cross-host grounding repairs."""

from collections import Counter

from jinja2 import Environment

from habitatmech import seed

PARENTS = {
    "habitatmech:GOLD.85999f8943": ("BTO:0001719", "habitatmech:GOLD.56e0776270"),
    "habitatmech:GOLD.efa84cfb9b": ("BTO:0001719", "habitatmech:GOLD.968051b240"),
    "habitatmech:GOLD.037d4112ea": ("habitatmech:GOLD.037d4112ea", "habitatmech:GOLD.b091b80314"),
    "habitatmech:GOLD.cdfe01fc7e": ("habitatmech:GOLD.cdfe01fc7e", "habitatmech:GOLD.6bda0871e2"),
    "habitatmech:GOLD.2b136a90dd": ("UBERON:0011997", "habitatmech:GOLD.6e10201167"),
    "habitatmech:GOLD.c484d9a195": ("habitatmech:GOLD.c484d9a195", "habitatmech:GOLD.50722c7871"),
    "habitatmech:GOLD.195d07bc47": ("habitatmech:GOLD.195d07bc47", "habitatmech:GOLD.b091b80314"),
    "habitatmech:GOLD.0bb82ca5d9": ("habitatmech:GOLD.0bb82ca5d9", "habitatmech:GOLD.b091b80314"),
    "habitatmech:GOLD.3d5616ccf7": ("habitatmech:GOLD.3d5616ccf7", "habitatmech:GOLD.5b0aa7456c"),
    "habitatmech:GOLD.e428c46d06": ("habitatmech:GOLD.e428c46d06", "habitatmech:GOLD.6bda0871e2"),
    "habitatmech:GOLD.d7a86e335f": ("UBERON:0001914", "habitatmech:GOLD.1a6a558ccf"),
}
INSECT = "habitatmech:GOLD.c484d9a195"
COELOM = "UBERON:0011997"
SCOPES = {"coelomic cavity": "RELATED_SYNONYM", "enterocoelom": "NARROW_SYNONYM"}
CORRECTIONS = {"coelom-coelomic-cavity-scope", "coelom-enterocoelom-scope"}


def test_reviewed_guards_and_public_evidence_links():
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    corrections = seed.load_record_annotation_corrections(seed.RECORD_ANNOTATION_CORRECTIONS_PATH)
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    assert PARENTS.keys() <= parents.keys()
    rows = []
    for key, (_, parent) in PARENTS.items():
        row = parents[key]
        assert seed.mint("GOLD", row.source_path) == key
        assert row.parent_id == parent
        rows.append(row)
    scoped = [r for r in corrections if r.correction_id in CORRECTIONS]
    assert len(scoped) == 2
    for row in scoped:
        assert row.identifier == COELOM and row.source == "UBERON"
        assert row.field == "synonym_type" and row.expected == "EXACT_SYNONYM"
        assert row.replacement == SCOPES[row.item]
    rows.extend(scoped)
    decision = decisions[INSECT]
    assert decision.decision == "CONFIRM_UNGROUNDED"
    assert decision.review_depth == "ITEM" and not decision.object_id
    rows.append(decision)
    template = Environment(autoescape=True).from_string("{{ notes|urlize }}")
    for row in rows:
        urls = [word for word in row.notes.split()
                if word.startswith("https://github.com/CultureBotAI/HabitatMech/issues/")]
        assert len(urls) == 1 and urls[0].rsplit("/", 1)[1].isdigit()
        assert f'href="{urls[0]}"' in template.render(notes=row.notes)


def test_ten_record_delta_preserves_unrelated_claims(monkeypatch):
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    corrections = seed.load_record_annotation_corrections(seed.RECORD_ANNOTATION_CORRECTIONS_PATH)
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    assert PARENTS.keys() <= parents.keys() and INSECT in decisions
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    with monkeypatch.context() as old:
        old.setattr(seed, "load_gold_parent_exclusions", lambda _: {
            key: row for key, row in parents.items() if key not in PARENTS
        })
        old.setattr(seed, "load_record_annotation_corrections", lambda _: [
            row for row in corrections if row.correction_id not in CORRECTIONS
        ])
        old.setattr(seed, "load_decisions", lambda _: {
            key: row for key, row in decisions.items() if key != INSECT
        })
        before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    expected = {target for target, _ in PARENTS.values()}
    assert len(expected) == 10
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == expected
    for key in expected:
        old, new = before[key], after[key]
        removed = {parent for target, parent in PARENTS.values() if target == key}
        allowed = {"parent_habitats", "curation_history"}
        if key == COELOM:
            allowed.add("synonyms")
            assert new["synonyms"] == [
                {**s, "synonym_type": SCOPES.get(s["synonym_text"], s["synonym_type"])}
                for s in old["synonyms"]
            ]
        if key == INSECT:
            removed.add("UBERON:0001155")
            allowed.update({"grounding_status", "mapping_status", "source_attestations"})
            assert new["grounding_status"] == "UNGROUNDED"
            assert new["mapping_status"] == "REVIEWED"
            assert new["source_attestations"] == [
                {k: v for k, v in att.items() if k != "mapping_predicate"}
                for att in old["source_attestations"]
            ]
            assert Counter(e["action"] for e in new["curation_history"]) == {
                "SEEDED_FROM_SOURCES": 1, "CONFIRM_UNGROUNDED": 1, "SOURCE_PARENT_EXCLUDED": 1,
            }
            seeded = next(e for e in new["curation_history"] if e["action"] == "SEEDED_FROM_SOURCES")
            assert seeded == {
                **old["curation_history"][0],
                "changes": old["curation_history"][0]["changes"].replace("NARROW", "UNGROUNDED"),
            }
        else:
            history = old["curation_history"]
            assert new["curation_history"][:len(history)] == history
            events = new["curation_history"][len(history):]
            actions = {"SOURCE_PARENT_EXCLUDED": len(removed)}
            if key == COELOM:
                actions["ANNOTATION_CORRECTED"] = 2
            assert Counter(e["action"] for e in events) == actions
            assert all(e["curator"] == "codex-gpt-5" for e in events)
        assert removed <= set(old["parent_habitats"])
        assert new.get("parent_habitats", []) == [p for p in old["parent_habitats"] if p not in removed]
        assert {k: v for k, v in old.items() if k not in allowed} == {
            k: v for k, v in new.items() if k not in allowed
        }
    assert after[COELOM]["parent_habitats"] == ["UBERON:0000481"]
    assert after["UBERON:0001914"]["parent_habitats"] == ["UBERON:0006539"]
    assert after["BTO:0001719"]["parent_habitats"] == ["BTO:0001492"]
    assert {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts} == after
