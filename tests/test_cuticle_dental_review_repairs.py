"""Constrain ten context exclusions and three arthropod cuticle decisions."""

from collections import Counter

from jinja2 import Environment

from habitatmech import seed

PARENTS = {
    "habitatmech:GOLD.82cc79ac14": ("UBERON:0009964", "habitatmech:GOLD.d0a97e09fe"),
    "habitatmech:GOLD.f43331961c": ("UBERON:0012114", "habitatmech:GOLD.d3869ad37f"),
    "habitatmech:GOLD.3d911344b7": ("habitatmech:GOLD.3d911344b7", "habitatmech:GOLD.8f7b1d316e"),
    "habitatmech:GOLD.9ad201f9cc": ("habitatmech:GOLD.9ad201f9cc", "habitatmech:GOLD.9570fb16f7"),
    "habitatmech:GOLD.bb4731e6fe": ("habitatmech:GOLD.bb4731e6fe", "habitatmech:GOLD.3da0b4697d"),
    "habitatmech:GOLD.c859639497": ("habitatmech:GOLD.c859639497", "habitatmech:GOLD.dd76069e56"),
    "habitatmech:GOLD.2cdf4f2c7f": ("habitatmech:GOLD.2cdf4f2c7f", "habitatmech:GOLD.4b37ab4b76"),
    "habitatmech:GOLD.db17f52768": ("habitatmech:GOLD.db17f52768", "habitatmech:GOLD.99880772e1"),
    "habitatmech:GOLD.893217d90a": ("habitatmech:GOLD.893217d90a", "habitatmech:GOLD.99880772e1"),
    "habitatmech:GOLD.e287a243a5": ("habitatmech:GOLD.e287a243a5", "habitatmech:GOLD.99880772e1"),
}
SOURCE_PATHS = {
    "habitatmech:GOLD.82cc79ac14": (
        "Host-associated > Arthropoda: Crustaceans > Excretory system > Maxillary glands"
    ),
    "habitatmech:GOLD.f43331961c": "Host-associated > Mammals > Digestive system > Stomach > Cud",
    "habitatmech:GOLD.3d911344b7": "Host-associated > Annelida > Integument > Cuticle",
    "habitatmech:GOLD.9ad201f9cc": (
        "Host-associated > Arthropoda: Myriapoda > Integumentary system > Cuticle"
    ),
    "habitatmech:GOLD.bb4731e6fe": "Host-associated > Arthropoda: Myriapoda > Integument > Cuticle",
    "habitatmech:GOLD.c859639497": (
        "Host-associated > Arthropoda: Crustaceans > Integumentary system > Cuticle"
    ),
    "habitatmech:GOLD.2cdf4f2c7f": (
        "Host-associated > Mammals: Human > Integumentary system > Skin > Cuticle"
    ),
    "habitatmech:GOLD.db17f52768": (
        "Host-associated > Mammals: Human > Digestive system > Oral cavity > Dental abscess"
    ),
    "habitatmech:GOLD.893217d90a": (
        "Host-associated > Mammals: Human > Digestive system > Oral cavity > Dental calculus"
    ),
    "habitatmech:GOLD.e287a243a5": (
        "Host-associated > Mammals: Human > Digestive system > Oral cavity > Dental plaque"
    ),
}
MINERAL = {
    "habitatmech:GOLD.9ad201f9cc", "habitatmech:GOLD.bb4731e6fe", "habitatmech:GOLD.c859639497",
}
RETAINED_PARENTS = {
    "UBERON:0009964": ["UBERON:0009962"],
    "UBERON:0012114": ["UBERON:0036017"],
    "habitatmech:GOLD.3d911344b7": ["UBERON:0001002"],
    "habitatmech:GOLD.9ad201f9cc": [],
    "habitatmech:GOLD.bb4731e6fe": [],
    "habitatmech:GOLD.c859639497": [],
    "habitatmech:GOLD.2cdf4f2c7f": ["UBERON:0001002"],
    "habitatmech:GOLD.db17f52768": [],
    "habitatmech:GOLD.893217d90a": [],
    "habitatmech:GOLD.e287a243a5": ["UBERON:0016482"],
}


def test_reviewed_guards_and_public_evidence_links():
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    assert PARENTS.keys() == SOURCE_PATHS.keys()
    assert PARENTS.keys() <= parents.keys()
    assert decisions.keys() >= MINERAL
    rows = []
    for key, (_, parent) in PARENTS.items():
        row = parents[key]
        assert row.source_path == SOURCE_PATHS[key]
        assert seed.mint("GOLD", row.source_path) == key
        assert row.parent_id == parent
        rows.append(row)
    for key in MINERAL:
        decision = decisions[key]
        assert decision.decision == "CONFIRM_UNGROUNDED"
        assert decision.review_depth == "ITEM"
        assert not decision.object_id and not decision.object_label
        assert not decision.grounding_status and not decision.category
        assert "not proof that no suitable ontology term exists" in decision.notes
        assert "PMID:" not in decision.notes
        for pmid in ("15670859", "18550385"):
            url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
            assert url in decision.notes
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
    assert PARENTS.keys() <= parents.keys() and decisions.keys() >= MINERAL
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    with monkeypatch.context() as old:
        old.setattr(seed, "load_gold_parent_exclusions", lambda _: {
            key: row for key, row in parents.items() if key not in PARENTS
        })
        old.setattr(seed, "load_decisions", lambda _: {
            key: row for key, row in decisions.items() if key not in MINERAL
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
        if key in MINERAL:
            removed.add("UBERON:0001002")
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
