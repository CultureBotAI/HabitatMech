"""Source-context exclusions must never erase independent hierarchy evidence."""

from __future__ import annotations

import csv
from dataclasses import asdict, replace

import pytest

from habitatmech import seed
from habitatmech.curate.gold_parent_exclusions import (
    GoldParentExclusion,
    GoldParentExclusionError,
    load_gold_parent_exclusions,
)

PATH = "Environmental > Aquatic > Freshwater"
EXCLUSION = GoldParentExclusion(
    seed.mint("GOLD", PATH), PATH, "ENVO:00002030", "test", "2026-10-03",
    "Source context is not a strictly broader material class.",
)


def write_table(path, rows):
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(asdict(EXCLUSION)), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def test_loader_round_trip_and_required_file(tmp_path):
    path = tmp_path / "exclusions.tsv"
    with pytest.raises(FileNotFoundError):
        load_gold_parent_exclusions(path)
    write_table(path, [asdict(EXCLUSION)])
    assert load_gold_parent_exclusions(path) == {EXCLUSION.identifier: EXCLUSION}


@pytest.mark.parametrize("field,value", [
    ("identifier", "ENVO:00002011"), ("parent_id", "not a curie"),
    ("source_path", ""), ("curator", ""), ("notes", "too short"),
    ("date", "20261003"), ("date", "2026-02-30"),
])
def test_loader_rejects_invalid_values(tmp_path, field, value):
    row = asdict(EXCLUSION)
    row[field] = value
    path = tmp_path / "exclusions.tsv"
    write_table(path, [row])
    with pytest.raises(GoldParentExclusionError):
        load_gold_parent_exclusions(path)


@pytest.mark.parametrize("contents", [
    "identifier\tnotes\n", "\t".join(asdict(EXCLUSION)) + "\n\t\n",
    "\t".join(asdict(EXCLUSION)) + "\n" + "\t".join(asdict(EXCLUSION).values()) + "\textra\n",
])
def test_loader_rejects_malformed_shape(tmp_path, contents):
    path = tmp_path / "exclusions.tsv"
    path.write_text(contents, encoding="utf-8")
    with pytest.raises(GoldParentExclusionError):
        load_gold_parent_exclusions(path)


def test_loader_rejects_duplicates(tmp_path):
    path = tmp_path / "exclusions.tsv"
    write_table(path, [asdict(EXCLUSION), asdict(EXCLUSION)])
    with pytest.raises(GoldParentExclusionError, match="duplicate"):
        load_gold_parent_exclusions(path)


def gold_rows():
    rows = []
    for path in ["Environmental", "Environmental > Aquatic", PATH, PATH + " > Sediment"]:
        levels = path.split(" > ")
        row = {key: levels[i] if i < len(levels) else "" for i, key in enumerate(seed.GOLD_LEVELS)}
        row.update(canonical_path=path, leaf_label=levels[-1], depth=str(len(levels)),
                   gold_node_ids="gold.ecosystem:1", organism_count="2")
        rows.append(row)
    return rows


def ontology(edges=(), freshwater_synonyms=""):
    terms = [{"term_id": term, "ontology": "ENVO", "label": label, "synonyms": ""}
             for term, label in [("ENVO:00002011", "Freshwater"),
                                 ("ENVO:00002030", "Aquatic")]]
    terms[0]["synonyms"] = freshwater_synonyms
    return seed.OntologyIndex(terms, list(edges))


@pytest.mark.parametrize("independent_parent", [False, True])
def test_only_source_contribution_is_excluded(independent_parent):
    edges = ([{"subject": "ENVO:00002011", "predicate": "rdfs:subClassOf",
               "object": EXCLUSION.parent_id}] if independent_parent else [])
    store = seed.ConceptStore(ontology(edges))
    resolved = seed.ingest_gold(store, gold_rows(), {}, seed.Counter(),
                                parent_exclusions={EXCLUSION.identifier: EXCLUSION})
    child = store.concepts[resolved[PATH]]
    assert (EXCLUSION.parent_id in child.parents) is independent_parent
    assert child.attestations[0]["source_path"] == PATH
    assert child.attestations[0]["assertion_count"] == 2
    assert child.identifier in store.concepts[resolved[PATH + " > Sediment"]].parents
    doc = seed.build_document(child)
    assert doc["mapping_status"] == "SEEDED"
    assert doc["grounding_status"] == "EXACT"
    assert doc["curation_history"][-1]["action"] == "SOURCE_PARENT_EXCLUDED"
    assert doc == seed.build_document(child)


def test_independent_curator_parent_is_preserved():
    decision = seed.Decision(
        EXCLUSION.identifier, "GROUND_AS_PARENT", EXCLUSION.parent_id, "Aquatic",
        "NARROW", "test", "2026-10-03", "Independent curator parent contribution.",
    )
    store = seed.ConceptStore(ontology())
    resolved = seed.ingest_gold(
        store, gold_rows(), {}, seed.Counter(),
        decisions={decision.identifier: decision},
        parent_exclusions={EXCLUSION.identifier: EXCLUSION},
    )
    child = store.concepts[resolved[PATH]]
    assert child.parents == {EXCLUSION.parent_id}
    assert child.gold_parent_exclusions_applied == [EXCLUSION]
    assert seed.build_document(child)["mapping_status"] == "REVIEWED"


@pytest.mark.parametrize("reverse_rows", [False, True])
def test_independent_gold_source_parent_is_preserved(reverse_rows):
    rows = gold_rows()
    other_path = "Environmental > Aquatic > Springwater"
    rows.append({
        **rows[2], "canonical_path": other_path, "leaf_label": "Springwater",
        "ecosystem_type": "Springwater", "gold_node_ids": "gold.ecosystem:2",
    })
    if reverse_rows:
        rows.reverse()
    store = seed.ConceptStore(ontology(freshwater_synonyms="Springwater"))
    resolved = seed.ingest_gold(
        store, rows, {}, seed.Counter(),
        parent_exclusions={EXCLUSION.identifier: EXCLUSION},
    )
    assert resolved[PATH] == resolved[other_path]
    child = store.concepts[resolved[PATH]]
    assert child.parents == {EXCLUSION.parent_id}
    assert {a["source_path"] for a in child.attestations} == {PATH, other_path}
    assert child.gold_parent_exclusions_applied == [EXCLUSION]


def test_identity_merge_makes_existing_exclusion_stale():
    decision = seed.Decision(
        EXCLUSION.identifier, "GROUND", EXCLUSION.parent_id, "Aquatic", "EXACT",
        "test", "2026-10-03", "Synthetic identity change invalidates the old exclusion.",
    )
    with pytest.raises(GoldParentExclusionError, match="stale"):
        seed.ingest_gold(
            seed.ConceptStore(ontology()), gold_rows(), {}, seed.Counter(),
            decisions={decision.identifier: decision},
            parent_exclusions={EXCLUSION.identifier: EXCLUSION},
        )


@pytest.mark.parametrize("exclusion", [
    replace(EXCLUSION, parent_id="ENVO:99999999"),
    replace(EXCLUSION, source_path="Environmental > Other"),
    replace(EXCLUSION, identifier="habitatmech:GOLD.0000000000"),
    replace(EXCLUSION, identifier=seed.mint("GOLD", "Environmental"), source_path="Environmental"),
])
def test_stale_or_unmatched_exclusion_stops_ingest(exclusion):
    with pytest.raises(GoldParentExclusionError, match="stale|unmatched"):
        seed.ingest_gold(seed.ConceptStore(ontology()), gold_rows(), {}, seed.Counter(),
                         parent_exclusions={exclusion.identifier: exclusion})


def test_real_corpus_changes_only_subterranean_estuary_parent_and_audit(tmp_path, monkeypatch):
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    identifier = "habitatmech:GOLD.58415258eb"
    empty = tmp_path / "empty.tsv"
    write_table(empty, [
        asdict(row) for key, row in load_gold_parent_exclusions(
            seed.GOLD_PARENT_EXCLUSIONS_PATH
        ).items() if key != identifier
    ])
    monkeypatch.setattr(seed, "GOLD_PARENT_EXCLUSIONS_PATH", empty)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert after.keys() == before.keys()
    assert {key for key in before if before[key] != after[key]} == {identifier}
    old, new = before[identifier], after[identifier]
    assert old["parent_habitats"] == ["habitatmech:GOLD.115edc36f8"]
    assert not new.get("parent_habitats")
    assert new["curation_history"][:-1] == old["curation_history"]
    assert new["curation_history"][-1]["action"] == "SOURCE_PARENT_EXCLUDED"
    for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
        assert new.get(field) == old.get(field), field
    assert new["grounding_status"] == "UNGROUNDED"
    assert new["mapping_status"] == "SEEDED"
    assert new["source_attestations"] == [{
        "source": "GOLD",
        "source_id": "gold.ecosystem:8255",
        "source_label": "Subterranean estuary",
        "source_path": (
            "Environmental > Aquatic > Marine > Intertidal zone > Subterranean estuary"
        ),
    }]


def test_lake_and_subtidal_curation_has_exact_corpus_scope(monkeypatch):
    freshwater = "habitatmech:GOLD.51eb0120ab"
    deep = "habitatmech:GOLD.937bf682c4"
    coastal = "habitatmech:GOLD.059724892c"
    targets = {freshwater, deep, coastal}
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    for identifier in (freshwater, deep):
        decisions[identifier] = replace(
            decisions[identifier], object_id="", object_label="", category="",
            relation="parent", curator="claude-opus-5", date="2026-08-12",
            review_depth="CLASS", notes=(
                "Class-level sweep (see docs/HARMONIZATION.md#class-level-sweep): "
                "no term in the vendored slice matched this label by any search route. "
                "Whether the concept is a habitat at all was NOT assessed, so this "
                "is not yet a term-request candidate."
            ),
        )
    exclusions = {
        key: row for key, row in load_gold_parent_exclusions(
            seed.GOLD_PARENT_EXCLUSIONS_PATH
        ).items() if key not in targets
    }
    monkeypatch.setattr(seed, "load_decisions", lambda path: decisions)
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda path: exclusions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == targets
    assert after[freshwater]["parent_habitats"] == ["ENVO:00000058"]
    assert after[deep]["parent_habitats"] == [
        "ENVO:00000058", "habitatmech:GOLD.21222434e2",
    ]
    assert not after[coastal].get("parent_habitats")
    assert after[coastal]["curation_history"][:-1] == before[coastal]["curation_history"]
    for identifier in targets:
        old, new = before[identifier], after[identifier]
        allowed = {"parent_habitats", "mapping_status", "curation_history"}
        for field in (old.keys() | new.keys()) - allowed:
            assert new.get(field) == old.get(field), (identifier, field)
        assert new["grounding_status"] == "UNGROUNDED"
        assert new["mapping_status"] == ("SEEDED" if identifier == coastal else "REVIEWED")
        assert len(new["source_attestations"]) == 1
        attestation = new["source_attestations"][0]
        assert "mapping_predicate" not in attestation
        assert "assertion_count" not in attestation
        assert "assertion_unit" not in attestation
        old_seed = [e for e in old["curation_history"] if e["action"] == "SEEDED_FROM_SOURCES"]
        new_seed = [e for e in new["curation_history"] if e["action"] == "SEEDED_FROM_SOURCES"]
        assert new_seed == old_seed
    for identifier in (freshwater, deep):
        decision_events = [
            event for event in after[identifier]["curation_history"]
            if event["action"] == "CONFIRM_UNGROUNDED"
        ]
        assert len(decision_events) == 1
        assert decision_events[0]["timestamp"] == "2026-10-06T00:00:00Z"
        assert "[CLASS-level]" not in decision_events[0]["changes"]
