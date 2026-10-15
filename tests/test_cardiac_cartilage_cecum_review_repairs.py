"""Keep anatomical components and cross-host homonyms scientifically distinct."""

import json
from collections import Counter
from dataclasses import replace
from pathlib import Path

from jinja2 import Environment

from habitatmech import seed

PARENT_PATHS = {
    "Host-associated > Mammals: Human > Circulatory system > Heart > Atria":
        ("UBERON:0002081", "habitatmech:GOLD.805ee181bd"),
    "Host-associated > Mammals: Human > Circulatory system > Heart > Septum":
        ("UBERON:0002099", "habitatmech:GOLD.805ee181bd"),
    "Host-associated > Mammals: Human > Circulatory system > Heart > Cardiac skeleton":
        ("UBERON:0004292", "habitatmech:GOLD.805ee181bd"),
    "Host-associated > Arthropoda: Crustaceans > Digestive system > Foregut > Cardiac stomach":
        ("UBERON:0008250", "habitatmech:GOLD.fe78a4c113"),
    "Host-associated > Mammals: Human > Skeletal system > Cartilage":
        ("habitatmech:GOLD.53fd337784", "habitatmech:GOLD.ea67ca30cb"),
    "Host-associated > Fish > Skeletal system > Cartilage":
        ("habitatmech:GOLD.e1b5f9301d", "habitatmech:GOLD.b1f5d69111"),
    "Host-associated > Mammals > Skeletal system > Cartilage":
        ("habitatmech:GOLD.d8b9309d5e", "habitatmech:GOLD.092eae5cd7"),
    "Host-associated > Mammals > Respiratory system > Pharynx/Throat > Catarrh":
        ("habitatmech:GOLD.62dfa9436e", "UBERON:0000341"),
    "Host-associated > Mammals > Respiratory system > Paranasal sinuses > Catarrh":
        ("habitatmech:GOLD.d225bacabd", "habitatmech:GOLD.8eba55841e"),
    "Host-associated > Birds > Digestive system > Ceca":
        ("habitatmech:GOLD.2629408066", "habitatmech:GOLD.fb6caa2908"),
    "Host-associated > Mollusca > Digestive system > Ceca":
        ("habitatmech:GOLD.8c5f1eb1b0", "habitatmech:GOLD.3baeffe4f8"),
    "Host-associated > Birds > Digestive system > Large intestine > Ceca":
        ("habitatmech:GOLD.d1f4d0cde1", "habitatmech:GOLD.b091b80314"),
    "Host-associated > Mammals > Digestive system > Large intestine > Cecotropes/Night fecs":
        ("habitatmech:GOLD.dc062a959c", "habitatmech:GOLD.6bda0871e2"),
    "Host-associated > Mollusca > Digestive system > Hindgut > Cecum/Intestinal cecum":
        ("BTO:0000166", "habitatmech:GOLD.c336fb0bb7"),
    "Host-associated > Mammals > Digestive system > Large intestine > Cecum":
        ("habitatmech:GOLD.a8f8c792c1", "habitatmech:GOLD.6bda0871e2"),
}
STOMACH = "habitatmech:GOLD.34dfea04f9"
MOLLUSC = "habitatmech:GOLD.37d9cdc188"
CECA = "habitatmech:GOLD.8c5f1eb1b0"
REDECIDED = {STOMACH, MOLLUSC, CECA}
OLD_STOMACH = "UBERON:0008250"
PREGO = "BTO:0000166"


def test_reviewed_input_guards_and_public_links():
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    template = Environment(autoescape=True).from_string("{{ notes|urlize }}")
    rows = []
    for path, (_, parent) in PARENT_PATHS.items():
        row = parents[seed.mint("GOLD", path)]
        assert row.source_path == path
        assert row.parent_id == parent
        rows.append(row)
    for key in REDECIDED:
        row = decisions[key]
        assert row.decision == "CONFIRM_UNGROUNDED"
        assert row.review_depth == "ITEM"
        assert not row.object_id
        rows.append(row)
    for row in rows:
        urls = [word for word in row.notes.split()
                if word.startswith("https://github.com/CultureBotAI/HabitatMech/issues/")]
        assert len(urls) == 1
        assert urls[0].rsplit("/", 1)[1].isdigit()
        assert f'href="{urls[0]}"' in template.render(notes=row.notes)
    assert decisions[MOLLUSC].notes.endswith(
        "Path: Host-associated > Mollusca > Digestive system > Hindgut > Cecum/Intestinal cecum"
    )


def source_multiset(documents):
    return Counter(
        json.dumps({k: v for k, v in att.items() if k != "mapping_predicate"}, sort_keys=True)
        for doc in documents.values() for att in doc["source_attestations"]
    )


def test_repairs_preserve_full_corpus_and_exact_source_partition(monkeypatch):
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    prior = json.loads(Path(__file__).with_name("data").joinpath(
        "cardiac_cartilage_cecum_prior_decisions.json"
    ).read_text())
    parent_keys = {seed.mint("GOLD", path) for path in PARENT_PATHS}
    assert parent_keys <= parents.keys()
    assert decisions.keys() >= REDECIDED
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    with monkeypatch.context() as old:
        old.setattr(seed, "load_gold_parent_exclusions", lambda _: {
            key: row for key, row in parents.items() if key not in parent_keys
        })
        old.setattr(seed, "load_decisions", lambda _: {
            key: replace(row, **prior[key]) if key in prior else row
            for key, row in decisions.items() if key not in {STOMACH, CECA}
        })
        before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    assert before.keys() - after.keys() == {OLD_STOMACH}
    assert after.keys() - before.keys() == {STOMACH, MOLLUSC}
    changed = {key for key in before.keys() & after.keys() if before[key] != after[key]}
    assert changed == {key for key, _ in PARENT_PATHS.values()} - {OLD_STOMACH}
    assert len(changed) == 14
    assert source_multiset(before) == source_multiset(after)
    assert {k: v.get("characteristic_taxa") for k, v in before.items()
            if v.get("characteristic_taxa")} == {
        k: v.get("characteristic_taxa") for k, v in after.items()
        if v.get("characteristic_taxa")
    }
    for key, parent in PARENT_PATHS.values():
        newkey = STOMACH if key == OLD_STOMACH else key
        removed = {parent}
        if key == CECA:
            removed.add("UBERON:0001153")
        if key == OLD_STOMACH:
            removed.add("UBERON:0004921")
        assert removed <= set(before[key]["parent_habitats"])
        assert after[newkey].get("parent_habitats", []) == [
            p for p in before[key]["parent_habitats"] if p not in removed
        ]
        if key in {CECA, OLD_STOMACH, PREGO}:
            continue
        assert {k: v for k, v in before[key].items()
                if k not in {"parent_habitats", "curation_history"}} == {
            k: v for k, v in after[key].items()
            if k not in {"parent_habitats", "curation_history"}
        }
        history = before[key]["curation_history"]
        assert after[key]["curation_history"][:len(history)] == history
        assert len(after[key]["curation_history"]) == len(history) + 1

    for newkey, oldkey in [(STOMACH, OLD_STOMACH), (MOLLUSC, PREGO), (CECA, CECA)]:
        doc = after[newkey]
        assert doc["grounding_status"] == "UNGROUNDED"
        assert doc["mapping_status"] == "REVIEWED"
        assert doc["habitat_category"] == "HOST_ASSOCIATED"
        assert not any(doc.get(k) for k in ["definition", "xrefs", "parent_habitats"])
        assert doc["source_attestations"] == [
            {k: v for k, v in att.items() if k != "mapping_predicate"}
            for att in before[oldkey]["source_attestations"] if att["source"] == "GOLD"
        ]
    assert after[PREGO]["source_attestations"] == [
        att for att in before[PREGO]["source_attestations"] if att["source"] == "PREGO"
    ]
    assert after[PREGO]["source_attestations"][0]["assertion_count"] == 549
    assert after[PREGO]["synonyms"] == [
        s for s in before[PREGO]["synonyms"] if s.get("source") != "GOLD"
    ]
    assert {k: v for k, v in before[PREGO].items()
            if k not in {"source_attestations", "synonyms", "parent_habitats", "curation_history"}} == {
        k: v for k, v in after[PREGO].items()
        if k not in {"source_attestations", "synonyms", "parent_habitats", "curation_history"}
    }
    assert {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts} == after
