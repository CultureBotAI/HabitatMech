"""Source-verified label updates do not silently change habitat scope."""

from __future__ import annotations

import copy
import hashlib
import json

import pytest
import yaml

from habitatmech import seed
from habitatmech.ontology_labels import (
    apply_label_refresh,
    load_plan,
    load_receipt,
    make_receipt,
    source_labels,
)


@pytest.fixture
def label_source(tmp_path):
    source = tmp_path / "source.owl"
    source.write_text('''<rdf:RDF
      xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
      xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
      xmlns:owl="http://www.w3.org/2002/07/owl#">
      <owl:Class rdf:about="http://purl.obolibrary.org/obo/FOODON_00003202">
        <rdfs:label xml:lang="en">beverage (liquid)</rdfs:label>
        <rdfs:label xml:lang="fr">boisson</rdfs:label>
        <rdfs:subClassOf><owl:Restriction>
          <rdfs:label>not a class label</rdfs:label>
        </owl:Restriction></rdfs:subClassOf>
      </owl:Class>
      <owl:Class rdf:about="http://purl.obolibrary.org/obo/FOODON_03315272">
        <rdfs:label>wheat pastry</rdfs:label>
      </owl:Class>
    </rdf:RDF>''', encoding="utf-8")
    plan = load_plan()
    plan["source_sha256"] = hashlib.sha256(source.read_bytes()).hexdigest()
    return source, plan


def test_source_labels_use_direct_english_annotations(label_source):
    source, plan = label_source
    assert source_labels(source, plan) == {
        "FOODON:00003202": "beverage (liquid)", "FOODON:03315272": "wheat pastry",
    }
    receipt = make_receipt(source, plan)
    assert receipt["source_bytes"] == source.stat().st_size
    assert receipt == make_receipt(source, plan)


def test_source_bytes_are_checked_before_labels(label_source):
    source, plan = label_source
    source.write_text(source.read_text() + "\n")
    with pytest.raises(ValueError, match="SHA256 mismatch"):
        source_labels(source, plan)


@pytest.mark.parametrize("replacement", [
    "",
    "<rdfs:label>wrong label</rdfs:label>",
    "<rdfs:label>wheat pastry</rdfs:label><rdfs:label>different label</rdfs:label>",
    "<rdfs:label>wheat pastry</rdfs:label><owl:deprecated>true</owl:deprecated>",
    "<rdfs:label>wheat pastry</rdfs:label><owl:deprecated> true </owl:deprecated>",
    "<rdfs:label>wheat pastry</rdfs:label><owl:deprecated> 1 </owl:deprecated>",
])
def test_missing_ambiguous_wrong_and_obsolete_terms_are_rejected(label_source, replacement):
    source, plan = label_source
    source.write_text(source.read_text().replace(
        "<rdfs:label>wheat pastry</rdfs:label>", replacement,
    ))
    plan["source_sha256"] = hashlib.sha256(source.read_bytes()).hexdigest()
    with pytest.raises(ValueError, match="source label mismatch|obsolete term"):
        source_labels(source, plan)


def test_refresh_is_idempotent_and_preserves_every_other_field():
    receipt = load_receipt()
    original = seed.read_tsv("ontology_terms.tsv")
    baseline = copy.deepcopy(original)
    for term in baseline:
        if term["term_id"] in receipt["terms"]:
            term["label"] = receipt["terms"][term["term_id"]]["previous_label"]
    untouched = copy.deepcopy(baseline)
    updated = apply_label_refresh(baseline, receipt)
    assert baseline == untouched
    assert updated == original
    assert apply_label_refresh(updated, receipt) == updated
    changes = []
    for before, after in zip(baseline, updated, strict=True):
        if before != after:
            changes.append(before["term_id"])
            assert {k for k in before if before[k] != after[k]} == {"label"}
    assert set(changes) == {"FOODON:00003202", "FOODON:03315272"}


@pytest.mark.parametrize("failure", ["missing", "duplicate", "drift"])
def test_refresh_rejects_stale_or_ambiguous_inventory(failure):
    receipt = load_receipt()
    terms = [{"term_id": term, "label": labels["previous_label"]}
             for term, labels in receipt["terms"].items()]
    if failure == "missing":
        terms.pop()
    elif failure == "duplicate":
        terms.append(terms[0].copy())
    else:
        terms[0]["label"] = "unexpected upstream change"
    with pytest.raises(ValueError, match="missing|duplicate|drifted"):
        apply_label_refresh(terms, receipt)


@pytest.mark.parametrize("field,value", [
    ("source_url", "https://raw.githubusercontent.com/FoodOntology/foodon/master/foodon.owl"),
    ("source_sha256", "bad"), ("version", 2), ("terms", {}),
])
def test_plan_rejects_unpinned_or_incomplete_provenance(tmp_path, field, value):
    plan = load_plan()
    plan[field] = value
    path = tmp_path / "plan.yaml"
    path.write_text(yaml.safe_dump(plan))
    with pytest.raises(ValueError):
        load_plan(path)


def test_receipt_must_match_reviewed_plan(tmp_path):
    receipt = load_receipt()
    receipt["terms"]["FOODON:03315272"]["label"] = "pastry"
    path = tmp_path / "receipt.json"
    path.write_text(json.dumps(receipt))
    with pytest.raises(ValueError, match="disagrees with plan: terms"):
        load_receipt(path)


def test_full_extraction_records_local_label_inputs():
    from habitatmech.extract import REPO_ROOT, _manifest_inputs
    from habitatmech.ontology_labels import PLAN_PATH, RECEIPT_PATH

    inputs = dict(_manifest_inputs(REPO_ROOT, None))
    assert inputs["habitatmech/conf/ontology_label_refresh.yaml"] == PLAN_PATH
    assert inputs["habitatmech/data/ontology_label_refresh.json"] == RECEIPT_PATH


def test_current_foodon_labels_do_not_make_generic_pastry_wheat_only():
    documents = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    pastry_id = seed.mint("GOLD", "Engineered > Food production > Pastry")
    pastry = documents[pastry_id]
    assert "FOODON:03315272" not in documents
    assert pastry["label"] == "Pastry"
    assert pastry["habitat_category"] == "FOOD"
    assert pastry["grounding_status"] == "UNGROUNDED"
    assert pastry["mapping_status"] == "REVIEWED"
    assert pastry["parent_habitats"] == ["FOODON:03530206"]
    assert "synonyms" not in pastry
    assert "definition" not in pastry
    assert pastry["source_attestations"] == [{
        "source": "GOLD", "source_id": "gold.ecosystem:5942", "source_label": "Pastry",
        "source_path": "Engineered > Food production > Pastry",
        "notes": "3 GOLD ecosystem node ids share this path; first shown. "
                 "See data/raw/gold_ecosystem_paths.tsv.",
    }]
    beverage = documents["FOODON:00003202"]
    assert beverage["label"] == "beverage (liquid)"
    assert beverage["definition"] == "A liquid prepared for consumption"
    assert beverage["grounding_status"] == "EXACT"
    assert beverage["mapping_status"] == "REVIEWED"
    assert beverage["parent_habitats"] == [
        "FOODON:03301977", "FOODON:03430130", "FOODON:03530206",
    ]
    assert beverage["source_attestations"] == [{
        "source": "GOLD", "source_id": "gold.ecosystem:5924", "source_label": "Beverages",
        "source_path": "Engineered > Food production > Beverages",
        "mapping_predicate": "skos:exactMatch", "assertion_count": 96,
        "assertion_unit": "ORGANISM",
        "notes": "3 GOLD ecosystem node ids share this path; first shown. "
                 "See data/raw/gold_ecosystem_paths.tsv.",
    }]
    assert "FOODON:00003202" in documents["BTO:0000659"]["parent_habitats"]


def test_foodon_refresh_changes_only_the_two_intended_records(monkeypatch):
    from dataclasses import replace

    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    pastry_id = "habitatmech:GOLD.d6e78c89e8"
    beverage_id = "FOODON:00003202"
    receipt = load_receipt()
    read = seed.read_tsv

    def previous_inventory(name):
        rows = read(name)
        if name == "ontology_terms.tsv":
            for row in rows:
                if row["term_id"] in receipt["terms"]:
                    row["label"] = receipt["terms"][row["term_id"]]["previous_label"]
        return rows

    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    decisions.pop(pastry_id)
    key = "habitatmech:GOLD.96754211ed"
    decisions[key] = replace(
        decisions[key], object_label="beverage", curator="claude-opus-5", date="2026-08-12",
        notes="Leaf label equals the FOODON label exactly and no other source concept "
              "claims it. Path: Engineered > Food production > Beverages",
    )
    monkeypatch.setattr(seed, "read_tsv", previous_inventory)
    monkeypatch.setattr(seed, "load_decisions", lambda path: decisions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    assert before.keys() - after.keys() == {"FOODON:03315272"}
    assert after.keys() - before.keys() == {pastry_id}
    assert {key for key in before.keys() & after.keys()
            if before[key] != after[key]} == {beverage_id}
    old, new = before[beverage_id], after[beverage_id]
    assert {key for key in old.keys() | new.keys()
            if old.get(key) != new.get(key)} == {"label", "curation_history"}
    old, new = before["FOODON:03315272"], after[pastry_id]
    assert old["habitat_category"] == new["habitat_category"] == "FOOD"
    old_source = old["source_attestations"][0].copy()
    assert old_source.pop("mapping_predicate") == "skos:exactMatch"
    assert new["source_attestations"] == [old_source]
    assert new["parent_habitats"] == [
        p for p in old["parent_habitats"] if p != "FOODON:00002350"
    ]
