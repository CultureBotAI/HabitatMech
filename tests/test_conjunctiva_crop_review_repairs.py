"""Constrain ten GOLD context exclusions and two nonavian crop decisions."""

from collections import Counter

from jinja2 import Environment

from habitatmech import seed

PARENTS = {
    "habitatmech:GOLD.539290062d": ("habitatmech:GOLD.539290062d", "habitatmech:GOLD.020f82703b"),
    "habitatmech:GOLD.fd0221f092": ("habitatmech:GOLD.fd0221f092", "habitatmech:GOLD.4166733314"),
    "habitatmech:GOLD.b521e12f22": ("habitatmech:GOLD.b521e12f22", "habitatmech:GOLD.4b46114446"),
    "habitatmech:GOLD.5068cb6b3d": ("habitatmech:GOLD.5068cb6b3d", "habitatmech:GOLD.b7f1694b87"),
    "habitatmech:GOLD.994d82c95b": ("UBERON:0001851", "PO:0009005"),
    "habitatmech:GOLD.5446ce4c6d": ("habitatmech:GOLD.5446ce4c6d", "habitatmech:GOLD.d011f4b43c"),
    "habitatmech:GOLD.d712a910ec": ("habitatmech:GOLD.d712a910ec", "habitatmech:GOLD.b2fc8fb1e4"),
    "habitatmech:GOLD.d3e8ec1eb1": ("habitatmech:GOLD.d3e8ec1eb1", "habitatmech:GOLD.fb6caa2908"),
    "habitatmech:GOLD.57011086ca": ("habitatmech:GOLD.57011086ca", "habitatmech:GOLD.bd1664969c"),
    "habitatmech:GOLD.57a0497838": ("habitatmech:GOLD.57a0497838", "habitatmech:GOLD.b2fc8fb1e4"),
}
SOURCE_PATHS = {
    "habitatmech:GOLD.539290062d": "Host-associated > Mammals: Human > Visual system > Conjunctiva",
    "habitatmech:GOLD.fd0221f092": "Host-associated > Mammals > Visual system > Conjunctiva",
    "habitatmech:GOLD.b521e12f22": "Host-associated > Mammals > Visual system > Eye > Cornea",
    "habitatmech:GOLD.5068cb6b3d": "Host-associated > Mammals: Human > Visual system > Eye > Cornea",
    "habitatmech:GOLD.994d82c95b": "Host-associated > Plants > Roots > Cortex",
    "habitatmech:GOLD.5446ce4c6d": "Host-associated > Annelida > Digestive system > Crop",
    "habitatmech:GOLD.d712a910ec": "Host-associated > Birds > Digestive system > Esophagus > Crop",
    "habitatmech:GOLD.d3e8ec1eb1": "Host-associated > Birds > Digestive system > Crop",
    "habitatmech:GOLD.57011086ca": (
        "Host-associated > Arthropoda: Insects > Digestive system > Foregut > Crop"
    ),
    "habitatmech:GOLD.57a0497838": "Host-associated > Birds > Digestive system > Esophagus > Crop content",
}
NONAVIAN = {"habitatmech:GOLD.5446ce4c6d", "habitatmech:GOLD.57011086ca"}
RETAINED_PARENTS = {
    "habitatmech:GOLD.539290062d": ["UBERON:0001811"],
    "habitatmech:GOLD.fd0221f092": ["UBERON:0001811"],
    "habitatmech:GOLD.b521e12f22": ["UBERON:0000964"],
    "habitatmech:GOLD.5068cb6b3d": ["UBERON:0000964"],
    "UBERON:0001851": ["UBERON:0000064"],
    "habitatmech:GOLD.5446ce4c6d": [],
    "habitatmech:GOLD.d712a910ec": ["UBERON:0007356"],
    "habitatmech:GOLD.d3e8ec1eb1": ["UBERON:0007356"],
    "habitatmech:GOLD.57011086ca": [],
    "habitatmech:GOLD.57a0497838": [],
}


def test_reviewed_guards_and_public_evidence_links():
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    assert PARENTS.keys() == SOURCE_PATHS.keys()
    assert PARENTS.keys() <= parents.keys()
    assert decisions.keys() >= NONAVIAN
    rows = []
    for key, (_, parent) in PARENTS.items():
        row = parents[key]
        assert row.source_path == SOURCE_PATHS[key]
        assert seed.mint("GOLD", row.source_path) == key
        assert row.parent_id == parent
        rows.append(row)
    for key in NONAVIAN:
        decision = decisions[key]
        assert decision.decision == "CONFIRM_UNGROUNDED"
        assert decision.review_depth == "ITEM"
        assert not decision.object_id and not decision.object_label
        assert not decision.grounding_status and not decision.category
        rows.append(decision)
    template = Environment(autoescape=True).from_string("{{ notes|urlize }}")
    for row in rows:
        urls = [word for word in row.notes.split()
                if word.startswith("https://github.com/CultureBotAI/HabitatMech/issues/")]
        assert len(urls) == 1 and urls[0].rsplit("/", 1)[1].isdigit()
        assert f'href="{urls[0]}"' in template.render(notes=row.notes)


def test_ten_record_delta_preserves_unrelated_claims(monkeypatch):
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    assert PARENTS.keys() <= parents.keys() and decisions.keys() >= NONAVIAN
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    with monkeypatch.context() as old:
        old.setattr(seed, "load_gold_parent_exclusions", lambda _: {
            key: row for key, row in parents.items() if key not in PARENTS
        })
        old.setattr(seed, "load_decisions", lambda _: {
            key: row for key, row in decisions.items() if key not in NONAVIAN
        })
        before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    expected = {target for target, _ in PARENTS.values()}
    assert len(PARENTS) == len(expected) == 10
    assert expected == RETAINED_PARENTS.keys()
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == expected
    for source, (key, parent) in PARENTS.items():
        old, new = before[key], after[key]
        removed = {parent}
        allowed = {"parent_habitats", "curation_history"}
        if key in NONAVIAN:
            removed.add("UBERON:0007356")
            allowed.update({"grounding_status", "mapping_status", "source_attestations"})
            assert old["grounding_status"] == "NARROW"
            assert old["mapping_status"] == "SEEDED"
            assert new["grounding_status"] == "UNGROUNDED"
            assert new["mapping_status"] == "REVIEWED"
            assert all(a["mapping_predicate"] == "skos:narrowMatch"
                       for a in old["source_attestations"])
            assert new["source_attestations"] == [
                {k: v for k, v in att.items() if k != "mapping_predicate"}
                for att in old["source_attestations"]
            ]
            assert len(old["curation_history"]) == 1
            assert old["curation_history"][0]["action"] == "SEEDED_FROM_SOURCES"
            assert Counter(e["action"] for e in new["curation_history"]) == {
                "SEEDED_FROM_SOURCES": 1, "CONFIRM_UNGROUNDED": 1, "SOURCE_PARENT_EXCLUDED": 1,
            }
            seeded = next(e for e in new["curation_history"] if e["action"] == "SEEDED_FROM_SOURCES")
            assert seeded == {
                **old["curation_history"][0],
                "changes": old["curation_history"][0]["changes"].replace("NARROW", "UNGROUNDED"),
            }
            decision = decisions[key]
            event = next(e for e in new["curation_history"] if e["action"] == "CONFIRM_UNGROUNDED")
            assert event["curator"] == decision.curator
            assert event["timestamp"] == f"{decision.date}T00:00:00Z"
            assert decision.notes in event["changes"] and key in event["changes"]
        else:
            history = old["curation_history"]
            assert new["curation_history"][:len(history)] == history
            events = new["curation_history"][len(history):]
            assert Counter(e["action"] for e in events) == {"SOURCE_PARENT_EXCLUDED": 1}
        exclusion = parents[source]
        event = next(e for e in new["curation_history"] if e["action"] == "SOURCE_PARENT_EXCLUDED")
        assert event == {
            "timestamp": f"{exclusion.date}T00:00:00Z",
            "curator": exclusion.curator,
            "action": "SOURCE_PARENT_EXCLUDED",
            "changes": (
                f"Excluded GOLD source-path parent contribution {parent} "
                f"for {source} ({exclusion.source_path}). {exclusion.notes}"
            ),
        }
        assert removed <= set(old["parent_habitats"])
        assert new.get("parent_habitats", []) == [p for p in old["parent_habitats"] if p not in removed]
        assert new.get("parent_habitats", []) == RETAINED_PARENTS[key]
        assert {k: v for k, v in old.items() if k not in allowed} == {
            k: v for k, v in new.items() if k not in allowed
        }
    assert {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts} == after
