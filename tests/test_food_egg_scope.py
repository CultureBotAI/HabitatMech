"""Exact-source food corrections must not discard observations or alter neighbors."""

from dataclasses import replace

import pytest

from habitatmech import seed

EGG = "habitatmech:BACDIVE.d48ce9485d"
FOOD_EGG = "FOODON:00001274"
CASES = {
    "FOODON:03000287": (
        "habitatmech:GOLD.58a308b569", "habitatmech:GOLD.4a2834cfef", ["FOODON:00001013"], 582,
    ),
    "habitatmech:GOLD.09d3541be1": (
        "habitatmech:GOLD.09d3541be1", "FOODON:00001006", [], 2,
    ),
    "FOODON:00001256": (
        "habitatmech:GOLD.c6aaede3c0", "FOODON:03530206", ["FOODON:00001092", "FOODON:00005501"], 1319,
    ),
    "habitatmech:GOLD.363486c188": (
        "habitatmech:GOLD.363486c188", "FOODON:03530206", [], 9,
    ),
}


@pytest.fixture(scope="module")
def documents():
    return {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}


def test_only_reviewed_sources_change(documents, monkeypatch):
    sources = {case[0] for case in CASES.values()}
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    old_decision = replace(
        decisions[EGG], decision="REVIEW", category="", curator="claude-opus-5", date="2026-08-16",
        notes="Historical food-only mapping endorsement, used only for the counterfactual regression.",
    )
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda _: {
        k: v for k, v in exclusions.items() if k not in sources
    })
    monkeypatch.setattr(seed, "load_decisions", lambda _: {**decisions, EGG: old_decision})
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert documents.keys() - before.keys() == {EGG}
    assert before.keys() - documents.keys() == {FOOD_EGG}
    assert {k for k in before.keys() & documents.keys() if before[k] != documents[k]} == CASES.keys()
    for identifier, (_, parent, parents, _) in CASES.items():
        old, new = before[identifier], documents[identifier]
        assert sorted(set(old["parent_habitats"]) - {parent}) == parents
        assert new.get("parent_habitats", []) == parents
        allowed = {"parent_habitats", "curation_history"}
        assert {k: v for k, v in old.items() if k not in allowed} == {
            k: v for k, v in new.items() if k not in allowed
        }
        events = [e for e in new["curation_history"] if e not in old["curation_history"]]
        assert len(events) == 1
        assert events[0]["action"] == "SOURCE_PARENT_EXCLUDED"
        assert [e for e in new["curation_history"] if e not in events] == old["curation_history"]
    old, new = before[FOOD_EGG], documents[EGG]
    assert old["characteristic_taxa"] == new["characteristic_taxa"]
    source = old["source_attestations"][0].copy()
    assert source.pop("mapping_predicate") == "skos:closeMatch"
    assert new["source_attestations"] == [source]


@pytest.mark.parametrize("identifier", CASES)
def test_exact_path_guards_and_counts(identifier, documents):
    source, parent, parents, count = CASES[identifier]
    doc = documents[identifier]
    exclusion = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)[source]
    assert exclusion.parent_id == parent
    assert seed.mint("GOLD", exclusion.source_path) == source
    assert doc["source_attestations"][0]["source_path"] == exclusion.source_path
    assert doc["source_attestations"][0]["assertion_count"] == count
    assert doc["source_attestations"][0]["assertion_unit"] == "ORGANISM"
    assert doc.get("parent_habitats", []) == parents


def test_egg_identity_and_taxon_observations(documents):
    doc = documents[EGG]
    assert doc["label"] == "Egg"
    assert doc["grounding_status"] == "UNGROUNDED"
    assert doc["mapping_status"] == "REVIEWED"
    assert doc["habitat_category"] == "HOST_ASSOCIATED"
    assert not {"definition", "parent_habitats", "xrefs"} & doc.keys()
    assert doc["source_attestations"] == [{
        "source": "BACDIVE", "source_id": "bacdive.isolation_source:egg", "source_label": "Egg",
        "assertion_count": 35, "assertion_unit": "STRAIN",
    }]
    taxa = doc["characteristic_taxa"]
    assert len(taxa) == 25
    assert {t["candidate_pool"] for t in taxa} == {30}
    assert [t["rank"] for t in taxa] == list(range(1, 26))
    assert sum(t["association_count"] for t in taxa) == 30
    assert all("is_characteristic" not in t for t in taxa)
    assert {"NCBITaxon:1122175", "NCBITaxon:1123347"} <= {t["taxon_id"] for t in taxa}
    decision = seed.load_decisions(seed.DECISIONS_PATH)[EGG]
    assert decision.decision == "CONFIRM_UNGROUNDED"
    assert decision.review_depth == "ITEM"
    assert not decision.object_id


def test_neighbor_and_status_boundaries(documents):
    assert documents["FOODON:03000287"]["mapping_status"] == "SEEDED"
    assert documents["FOODON:00001256"]["mapping_status"] == "REVIEWED"
    assert documents["habitatmech:GOLD.09d3541be1"]["mapping_status"] == "SEEDED"
    assert documents["habitatmech:GOLD.363486c188"]["mapping_status"] == "SEEDED"
    assert documents["habitatmech:GOLD.3140150c43"]["parent_habitats"] == ["habitatmech:GOLD.09d3541be1"]
    assert documents["habitatmech:GOLD.bb809618f0"]["parent_habitats"] == ["habitatmech:GOLD.f6b4333781"]
    assert documents["FOODON:00001006"]["grounding_status"] == "NARROW"
    assert documents["habitatmech:GOLD.4a2834cfef"]["mapping_status"] == "SEEDED"
