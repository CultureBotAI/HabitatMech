"""Regression boundaries for compost and its shared source-ingestion findings."""

from dataclasses import replace

import pytest

from habitatmech import seed
from habitatmech.curate.decisions import Decision
from habitatmech.text_map_inputs import semantic_text


def _ontology():
    return seed.OntologyIndex([
        {"term_id": "ENVO:00002170", "label": "compost", "ontology": "ENVO",
         "synonyms": "independent alias"},
    ], [])


def _decision(identifier, **kwargs):
    return Decision(
        identifier=identifier, decision="GROUND", object_id="ENVO:00002170",
        object_label="compost", grounding_status="CLOSE", curator="test",
        date="2026-10-07", notes="Source scope assessed separately from canonical identity.",
        **kwargs,
    )


def _gold_row(label="Source compost"):
    path = f"Engineered > Solid waste > {label}"
    levels = path.split(" > ")
    return {
        **{key: levels[i] if i < len(levels) else ""
           for i, key in enumerate(seed.GOLD_LEVELS)},
        "canonical_path": path, "leaf_label": label, "depth": "3",
        "gold_node_ids": "gold.ecosystem:1", "organism_count": "2",
    }


@pytest.mark.parametrize("source", ["GOLD", "BACDIVE"])
@pytest.mark.parametrize("status", ["CLOSE", "BROAD", "EXACT"])
@pytest.mark.parametrize("label", ["Source compost", "independent alias"])
def test_source_synonym_scope_respects_its_own_mapping(source, status, label):
    store = seed.ConceptStore(_ontology())
    # A co-attestor's stronger status must not promote this source's alias.
    store.get("ENVO:00002170", "compost", "EXACT")
    row = _gold_row(label)
    key = seed.mint(source, row["canonical_path"] if source == "GOLD" else "source:1")
    decision = replace(_decision(key), grounding_status=status)
    if source == "GOLD":
        seed.ingest_gold(store, [row], {}, seed.Counter(), {key: decision})
    else:
        seed.ingest_bacdive(store, [{"bacdive_id": "source:1", "label": label,
                                    "source_slug": label}], {},
                           seed.Counter(), {key: decision})
    concept = store.concepts["ENVO:00002170"]
    scope = "RELATED_SYNONYM" if status in {"CLOSE", "BROAD"} else "EXACT_SYNONYM"
    assert (label, scope) in concept.synonyms
    assert concept.synonyms[("independent alias", "EXACT_SYNONYM")] == "ENVO"
    if status in {"CLOSE", "BROAD"} and label != "independent alias":
        assert (label, "EXACT_SYNONYM") not in concept.synonyms
    assert concept.attestations[0]["source_label"] == label
    assert concept.attestations[0]["mapping_predicate"] == (
        {"CLOSE": "skos:closeMatch", "BROAD": "skos:broadMatch", "EXACT": "skos:exactMatch"}[status]
    )
    assert concept.grounding_status == "EXACT"
    doc = seed.build_document(concept)
    events = [e for e in doc["curation_history"] if e["action"] == "SOURCE_SYNONYM_SCOPED"]
    assert len(events) == (1 if status in {"CLOSE", "BROAD"} else 0)
    if events:
        assert f"a {status} source mapping" in events[0]["changes"]
        assert events[0]["timestamp"] == (
            "2026-10-07T00:00:00Z" if status == "CLOSE" else "2026-10-09T00:00:00Z"
        )
    assert seed.build_document(concept) == doc


@pytest.mark.parametrize("status", ["CLOSE", "BROAD"])
def test_shared_nonexact_spelling_retains_both_source_attestations_and_audit(status):
    store = seed.ConceptStore(_ontology())
    row = _gold_row()
    gold_key = seed.mint("GOLD", row["canonical_path"])
    bacdive_key = seed.mint("BACDIVE", "source:1")
    decisions = {key: replace(_decision(key), grounding_status=status)
                 for key in (gold_key, bacdive_key)}
    seed.ingest_gold(store, [row], {}, seed.Counter(), decisions)
    seed.ingest_bacdive(store, [{"bacdive_id": "source:1", "label": row["leaf_label"],
                                "source_slug": row["leaf_label"]}],
                       {}, seed.Counter(), decisions)
    concept = store.concepts["ENVO:00002170"]
    assert concept.synonyms[(row["leaf_label"], "RELATED_SYNONYM")] == "GOLD"
    assert (row["leaf_label"], "EXACT_SYNONYM") not in concept.synonyms
    assert {a["source"] for a in concept.attestations} == {"GOLD", "BACDIVE"}
    scoped = (concept.close_source_synonyms if status == "CLOSE"
              else concept.broad_source_synonyms)
    assert scoped == {
        ("GOLD", row["leaf_label"]), ("BacDive", row["leaf_label"]),
    }


def _bands(env_type="compost"):
    return [{"term_ids": "ENVO:00002170", "env_type": env_type,
             "parameter": axis, "value": value}
            for axis, value in [("Water", "medium"), ("Nutrients", "high")]]


@pytest.mark.parametrize("existing", [False, True])
@pytest.mark.parametrize("review", ["ITEM", "CLASS", None])
def test_environment_source_is_counted_once_with_all_bands(existing, review):
    store = seed.ConceptStore(_ontology())
    if existing:
        concept = store.get("ENVO:00002170", "compost", "EXACT")
        concept.source_concepts = concept.reviewed_sources = 1
    key = seed.mint("ENVIRONMENTS_TABLE", "compost")
    decisions = {} if review is None else {
        key: replace(_decision(key, review_depth=review), decision="REVIEW")}
    seed.ingest_parameters(store, _bands(), seed.Counter(), decisions)
    concept = store.concepts["ENVO:00002170"]
    assert concept.source_concepts == 1 + int(existing)
    assert concept.reviewed_sources == int(review == "ITEM") + int(existing)
    assert len(concept.parameters) == 2
    assert len(concept.attestations) == 1
    assert len(concept.decisions_applied) == int(review is not None)
    doc = seed.build_document(concept)
    assert doc["mapping_status"] == ("REVIEWED" if review == "ITEM" else "SEEDED")
    assert len([e for e in doc["curation_history"] if e["action"] == "REVIEW"]) == (
        int(review is not None)
    )


def test_distinct_environment_sources_on_one_record_are_not_collapsed():
    store = seed.ConceptStore(_ontology())
    key = seed.mint("ENVIRONMENTS_TABLE", "compost")
    decision = replace(_decision(key), decision="REVIEW")
    seed.ingest_parameters(store, _bands() + _bands("another source"), seed.Counter(),
                           {key: decision})
    concept = store.concepts["ENVO:00002170"]
    assert (concept.source_concepts, concept.reviewed_sources) == (2, 1)
    assert len(concept.parameters) == 4
    assert {a["source_id"] for a in concept.attestations} == {"compost", "another source"}
    assert seed.build_document(concept)["mapping_status"] == "SEEDED"


@pytest.fixture(scope="module")
def corpus():
    return seed.build_corpus()


def test_compost_exclusion_changes_only_one_parent_and_audit(corpus, monkeypatch):
    after = {c.identifier: seed.build_document(c) for c in corpus.concepts}
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    exclusion = exclusions.pop("habitatmech:GOLD.4741a9f8bb")
    assert exclusion.source_path == "Engineered > Solid waste > Composting"
    assert exclusion.parent_id == "mesh:D062611"
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda _: exclusions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {"ENVO:00002170"}
    old, new = before["ENVO:00002170"], after["ENVO:00002170"]
    assert old["parent_habitats"] == ["ENVO:03501300", "mesh:D062611"]
    assert new["parent_habitats"] == ["ENVO:03501300"]
    assert all(e in new["curation_history"] for e in old["curation_history"])
    additions = [e for e in new["curation_history"] if e not in old["curation_history"]]
    assert len(additions) == 1
    assert additions[0]["action"] == "SOURCE_PARENT_EXCLUDED"
    for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
        assert old.get(field) == new.get(field), field


def test_real_compost_and_water_source_audit_and_close_synonyms(corpus):
    concepts = {c.identifier: c for c in corpus.concepts}
    compost = concepts["ENVO:00002170"]
    assert (compost.source_concepts, compost.reviewed_sources) == (5, 5)
    assert len(compost.parameters) == 11
    for label in ("Composting", "Oil palm"):
        assert compost.synonyms[(label, "RELATED_SYNONYM")] == "GOLD"
        assert (label, "EXACT_SYNONYM") not in compost.synonyms
    for target, source in [("ENVO:00002170", "compost"), ("ENVO:00002006", "water")]:
        key = seed.mint("ENVIRONMENTS_TABLE", source)
        assert sum(d.identifier == key for d in concepts[target].decisions_applied) == 1
        doc = seed.build_document(concepts[target])
        assert sum(key in e["changes"] for e in doc["curation_history"]) == 1
        assert doc["mapping_status"] == "REVIEWED"
    for concept in corpus.concepts:
        for source, label in concept.close_source_synonyms:
            assert (label, "RELATED_SYNONYM") in concept.synonyms
            # Independent exact evidence may coexist; this source may not supply it.
            assert concept.synonyms.get((label, "EXACT_SYNONYM")) != source
            assert any(a["source"].upper() == source.upper() and a["source_label"] == label
                       for a in concept.attestations)
        if concept.close_source_synonyms:
            doc = seed.build_document(concept)
            old_scope = {**doc, "synonyms": [
                {**s, "synonym_type": "EXACT_SYNONYM"} for s in doc["synonyms"]]}
            assert semantic_text(doc) == semantic_text(old_scope)


def test_compost_graph_uses_material_axis_and_community_process(corpus):
    concept = next(c for c in corpus.concepts if c.identifier == "ENVO:00002170")
    graph, = concept.causal_graphs
    nodes = {n["node_id"]: n for n in graph["nodes"]}
    assert nodes["organic_solid_waste"]["node_type"] == "HABITAT"
    assert nodes["compost_temperature"]["node_type"] == "ENVIRONMENTAL_PARAMETER"
    assert nodes["thermophilic_community_succession"]["node_type"] == "COMMUNITY_PROCESS"
    assert not {n["node_type"] for n in nodes.values()} & {"STATE", "TAXON"}
    assert len(nodes) == 6
    assert len(graph["edges"]) == 5
    for edge in graph["edges"]:
        assert edge["subject"] in nodes and edge["object"] in nodes
        assert edge["evidence"]
    assert {e["reference"] for edge in graph["edges"] for e in edge["evidence"]} == {
        "PMID:16454493", "DOI:10.1186/s40538-023-00381-z",
    }
    assert [e["action"] for e in concept.causal_graph_events] == [
        "ADD_CAUSAL_GRAPH", "CORRECT_CAUSAL_GRAPH",
    ]
