"""Food review corrections preserve independent genera and frozen observations."""

import pytest

from habitatmech import seed

PROCESS = "FOODON:03530206"
RAW_CHOP = "habitatmech:GOLD.413b64dcc1"
GENERIC_CHOP = "FOODON:02020979"
CASES = {
    "habitatmech:GOLD.6d46057e78": ("Baby formula", "habitatmech:GOLD.6d46057e78", [], 27, "UNGROUNDED", "SEEDED"),
    "FOODON:00002753": ("Beans", "habitatmech:GOLD.effa0d6ca3", ["FOODON:00001635", "FOODON:03310646"], 0, "EXACT", "REVIEWED"),
    "FOODON:00003202": ("Beverages", "habitatmech:GOLD.96754211ed", ["FOODON:03301977", "FOODON:03430130"], 96, "EXACT", "REVIEWED"),
    "FOODON:00001183": ("Bread production", "habitatmech:GOLD.b37828b7b3", ["FOODON:00002456"], 380, "CLOSE", "REVIEWED"),
    "FOODON:00001093": ("Grains/Grain products", "habitatmech:GOLD.c25f588dad", ["FOODON:00001173"], 0, "CLOSE", "REVIEWED"),
}


@pytest.fixture(scope="module")
def documents():
    return {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}


def test_exact_change_scope_and_parent_only_preservation(documents, monkeypatch):
    sources = {case[1] for case in CASES.values()}
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    assert sources <= exclusions.keys()
    assert RAW_CHOP in decisions
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda _: {
        k: v for k, v in exclusions.items() if k not in sources
    })
    monkeypatch.setattr(seed, "load_decisions", lambda _: {
        k: v for k, v in decisions.items() if k != RAW_CHOP
    })
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert documents.keys() - before.keys() == {RAW_CHOP}
    assert before.keys() - documents.keys() == {GENERIC_CHOP}
    assert {k for k in before.keys() & documents.keys() if before[k] != documents[k]} == CASES.keys()
    for identifier, (_, _, parents, _, _, _) in CASES.items():
        old, new = before[identifier], documents[identifier]
        assert sorted(set(old["parent_habitats"]) - {PROCESS}) == parents
        assert new.get("parent_habitats", []) == parents
        allowed = {"parent_habitats", "curation_history"}
        assert {k: v for k, v in old.items() if k not in allowed} == {
            k: v for k, v in new.items() if k not in allowed
        }
        added = [e for e in new["curation_history"] if e not in old["curation_history"]]
        assert len(added) == 1
        assert added[0]["action"] == "SOURCE_PARENT_EXCLUDED"
        assert added[0]["curator"] == "codex-gpt-5"
        assert [e for e in new["curation_history"] if e not in added] == old["curation_history"]
    old_source = before[GENERIC_CHOP]["source_attestations"][0].copy()
    new_source = documents[RAW_CHOP]["source_attestations"][0].copy()
    assert old_source.pop("mapping_predicate") == "skos:exactMatch"
    assert new_source.pop("mapping_predicate") == "skos:narrowMatch"
    assert old_source == new_source


@pytest.mark.parametrize("identifier", CASES)
def test_source_guards_counts_and_native_status(identifier, documents):
    label, source, parents, count, grounding, status = CASES[identifier]
    doc = documents[identifier]
    exclusion = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)[source]
    path = "Engineered > Food production > " + label
    assert exclusion.source_path == path
    assert exclusion.parent_id == PROCESS
    assert seed.mint("GOLD", path) == source
    raw = next(r for r in seed.read_tsv("gold_ecosystem_paths.tsv") if r["canonical_path"] == path)
    assert int(raw["gold_node_count"]) == 3
    assert int(raw["organism_count"]) == count
    assert len(doc["source_attestations"]) == 1
    attestation = doc["source_attestations"][0]
    assert attestation["source_path"] == path
    assert attestation["source_id"] == raw["gold_node_ids"].split("|")[0]
    if count:
        assert attestation["assertion_count"] == count
        assert attestation["assertion_unit"] == "ORGANISM"
    else:
        assert "assertion_count" not in attestation
        assert "assertion_unit" not in attestation
    assert doc["grounding_status"] == grounding
    assert doc["mapping_status"] == status
    assert doc.get("parent_habitats", []) == parents


def test_raw_chop_keeps_qualification_without_retyping_generic_class(documents):
    doc = documents[RAW_CHOP]
    assert GENERIC_CHOP not in documents
    assert doc["grounding_status"] == "NARROW"
    assert doc["mapping_status"] == "REVIEWED"
    assert doc["habitat_category"] == "FOOD"
    assert doc["parent_habitats"] == [GENERIC_CHOP, "habitatmech:GOLD.43005e4de2"]
    assert "definition" not in doc
    assert doc["source_attestations"] == [{
        "source": "GOLD", "source_id": "gold.ecosystem:6425", "source_label": "Beef chop",
        "source_path": "Engineered > Food production > Meat products > Raw meat > Beef chop",
        "mapping_predicate": "skos:narrowMatch",
    }]
    decision = seed.load_decisions(seed.DECISIONS_PATH)[RAW_CHOP]
    assert decision.decision == "GROUND_AS_PARENT"
    assert decision.review_depth == "ITEM"
    assert decision.object_id == GENERIC_CHOP


def test_adjacent_bread_and_beef_claims_are_not_silently_recurated(documents):
    bread = documents["FOODON:03000288"]
    assert bread["parent_habitats"] == ["FOODON:00001183"]
    assert bread["mapping_status"] == "SEEDED"
    assert bread["source_attestations"][0]["assertion_count"] == 2
    product = documents["FOODON:00001183"]
    assert product["grounding_status"] == "CLOSE"
    assert product["source_attestations"][0]["source_label"] == "Bread production"
    assert documents["FOODON:00002574"]["source_attestations"][0]["assertion_count"] == 152
    assert documents["FOODON:00002574"]["grounding_status"] == "CLOSE"
