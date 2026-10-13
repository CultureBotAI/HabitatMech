"""Bound the clinical/anaerobic review fixes without promoting source claims."""

from dataclasses import replace

import pytest

from habitatmech import seed
from habitatmech.text_map_inputs import semantic_text

PARENTS = {
    "habitatmech:GOLD.3f58fb59be": ("habitatmech:GOLD.3f58fb59be", "ENVO:00002043"),
    "habitatmech:GOLD.93b148cc23": ("ENVO:00003965", "habitatmech:GOLD.3f58fb59be"),
    "habitatmech:GOLD.ed87e682a9": ("habitatmech:GOLD.ed87e682a9", "ENVO:00002001"),
    "habitatmech:GOLD.f96483345a": ("ENVO:00002129", "ENVO:00002124"),
    "habitatmech:GOLD.9f519b94cc": ("habitatmech:GOLD.9f519b94cc", "habitatmech:GOLD.5f3cbd7563"),
}
BIOPSY = "habitatmech:BACDIVE.3d4fdc29fb"
BROAD_LABELS = {
    "ENVO:03000033": "Sediment", "ENVO:00000021": "Lake",
    "ENVO:01000297": "River", "ENVO:00002129": "Sludge",
    "ENVO:01001511": "Ice", "ENVO:00005795": "Mud",
    "ENVO:00002209": "Sediment", "ENVO:00003965": "Sludge",
    "ENVO:01000125": "Littoral zone", "ENVO:01000910": "Biocrust",
    "UBERON:0005384": "Epithelium", "UBERON:0002099": "Septum",
}


@pytest.fixture(scope="module")
def corpus():
    return seed.build_corpus()


def test_biopsy_and_parent_curation_has_exact_scope(corpus, monkeypatch):
    after = {c.identifier: seed.build_document(c) for c in corpus.concepts}
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    decisions[BIOPSY] = replace(decisions[BIOPSY], decision="CONFIRM_UNGROUNDED")
    exclusions = {
        key: row for key, row in seed.load_gold_parent_exclusions(
            seed.GOLD_PARENT_EXCLUSIONS_PATH
        ).items() if key not in PARENTS
    }
    monkeypatch.setattr(seed, "load_decisions", lambda path: decisions)
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda path: exclusions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == (
        {BIOPSY} | {target for target, parent in PARENTS.values()}
    )
    for source, (target, parent) in PARENTS.items():
        old, new = before[target], after[target]
        assert set(new.get("parent_habitats", [])) == set(old["parent_habitats"]) - {parent}
        additions = [e for e in new["curation_history"] if e not in old["curation_history"]]
        assert len(additions) == 1
        assert additions[0]["action"] == "SOURCE_PARENT_EXCLUDED"
        assert source in additions[0]["changes"]
        assert all(e in new["curation_history"] for e in old["curation_history"])
        for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
            assert old.get(field) == new.get(field), (target, field)
    assert after["ENVO:00002129"]["parent_habitats"] == ["ENVO:00002044"]
    assert after["ENVO:00003965"]["parent_habitats"] == ["ENVO:00002129"]
    old, new = before[BIOPSY], after[BIOPSY]
    assert old["grounding_status"] == "UNGROUNDED"
    assert new["grounding_status"] == "NOT_APPLICABLE"
    for field in (old.keys() | new.keys()) - {"grounding_status", "curation_history"}:
        assert old.get(field) == new.get(field), field
    assert new["mapping_status"] == "REVIEWED"
    assert new["habitat_category"] == "CLINICAL"
    assert new["xrefs"] == ["NCIT:C15189"]
    assert len(new["characteristic_taxa"]) == 25
    assert {t["candidate_pool"] for t in new["characteristic_taxa"]} == {73}
    assert new["source_attestations"][0]["assertion_count"] == 95
    assert new["source_attestations"][0]["assertion_unit"] == "STRAIN"
    assert any(e["action"] == "NOT_APPLICABLE" for e in new["curation_history"])
    assert semantic_text(old) == semantic_text(new)


def test_canonical_ancestor_synonym_scope_has_bounded_corpus_impact(corpus):
    affected = {c.identifier: c for c in corpus.concepts if c.gold_broader_synonyms}
    assert affected.keys() == BROAD_LABELS.keys()
    for identifier, label in BROAD_LABELS.items():
        concept = affected[identifier]
        doc = seed.build_document(concept)
        assert (label, "EXACT_SYNONYM") not in concept.synonyms
        assert concept.synonyms[(label, "RELATED_SYNONYM")] == "GOLD"
        assert any(a["source"] == "GOLD" and a["source_label"] == label
                   for a in doc["source_attestations"])
        events = [e for e in doc["curation_history"] if e["action"] == "SOURCE_SYNONYM_SCOPED"]
        assert len(events) == 1
        assert events[0]["timestamp"] == "2026-10-07T00:00:00Z"
        assert seed.build_document(concept) == doc
        old_scope = {**doc, "synonyms": [
            {**s, "synonym_type": "EXACT_SYNONYM"}
            if s["source"] == "GOLD" and s["synonym_text"] == label else s
            for s in doc["synonyms"]
        ]}
        assert semantic_text(doc) == semantic_text(old_scope)


@pytest.mark.parametrize("ancestry", ["unrelated", "strict", "cycle"])
def test_gold_synonym_guard_requires_strict_canonical_ancestry(ancestry):
    terms = [
        {"term_id": "ENVO:00002044", "ontology": "ENVO", "label": "sludge", "synonyms": ""},
        {"term_id": "ENVO:00002129", "ontology": "ENVO", "label": "anaerobic sludge",
         "synonyms": "synthetic exact alias"},
    ]
    edges = ([{"subject": "ENVO:00002129", "predicate": "rdfs:subClassOf",
               "object": "ENVO:00002044"}] if ancestry != "unrelated" else [])
    if ancestry == "cycle":
        edges.append({"subject": "ENVO:00002044", "predicate": "rdfs:subClassOf",
                      "object": "ENVO:00002129"})
    ontology = seed.OntologyIndex(terms, edges)
    path = "Engineered > Bioreactor > Anaerobic > Sludge"
    levels = path.split(" > ")
    row = {key: levels[i] if i < len(levels) else ""
           for i, key in enumerate(seed.GOLD_LEVELS)}
    row.update(canonical_path=path, leaf_label="Sludge", depth="4", gold_node_ids="")
    store = seed.ConceptStore(ontology)
    seed.ingest_gold(store, [row], {}, seed.Counter())
    concept = store.concepts["ENVO:00002129"]
    related = ancestry == "strict"
    scope = "RELATED_SYNONYM" if related else "EXACT_SYNONYM"
    assert concept.synonyms[("Sludge", scope)] == "GOLD"
    assert concept.synonyms[("synthetic exact alias", "EXACT_SYNONYM")] == "ENVO"
    assert bool(concept.gold_broader_synonyms) is related
