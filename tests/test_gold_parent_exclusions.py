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


def test_subtidal_supratidal_swamp_curation_has_exact_scope(monkeypatch):
    zone = "habitatmech:GOLD.313e2bf386"
    sediment = "habitatmech:GOLD.785879d721"
    supra = "habitatmech:GOLD.2ef6207bd1"
    swamp_source = "habitatmech:GOLD.0f3918255c"
    swamp = "ENVO:00000233"
    targets = {zone, sediment, supra, swamp}
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    decisions[sediment] = replace(
        decisions[sediment], object_id="", object_label="", category="",
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
        ).items() if key not in {zone, sediment, supra, swamp_source}
    }
    monkeypatch.setattr(seed, "load_decisions", lambda path: decisions)
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda path: exclusions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == targets
    expected_parents = {
        zone: [], sediment: ["ENVO:03000033"], supra: ["ENVO:01000124"],
        swamp: ["ENVO:01001209"],
    }
    for identifier in targets:
        old, new = before[identifier], after[identifier]
        assert new.get("parent_habitats", []) == expected_parents[identifier]
        allowed = {"parent_habitats", "curation_history"}
        if identifier == sediment:
            allowed.add("mapping_status")
        for field in (old.keys() | new.keys()) - allowed:
            assert new.get(field) == old.get(field), (identifier, field)
        assert new["curation_history"][-1]["action"] == "SOURCE_PARENT_EXCLUDED"
        if identifier != sediment:
            assert new["curation_history"][:-1] == old["curation_history"]
        assert [e for e in new["curation_history"] if e["action"] == "SEEDED_FROM_SOURCES"] == [
            e for e in old["curation_history"] if e["action"] == "SEEDED_FROM_SOURCES"
        ]
    assert after[sediment]["grounding_status"] == "UNGROUNDED"
    assert after[sediment]["mapping_status"] == "REVIEWED"
    events = [e for e in after[sediment]["curation_history"]
              if e["action"] == "CONFIRM_UNGROUNDED"]
    assert len(events) == 1
    event = events[0]
    assert event["timestamp"] == "2026-10-06T00:00:00Z"
    assert "[CLASS-level]" not in event["changes"]
    for identifier in (zone, sediment, supra):
        assert "assertion_count" not in after[identifier]["source_attestations"][0]
    assert "mapping_predicate" not in after[sediment]["source_attestations"][0]
    assert after[supra]["source_attestations"][0]["mapping_predicate"] == "skos:narrowMatch"
    assert len(after[swamp]["source_attestations"]) == 3
    assert len(after[swamp]["characteristic_taxa"]) == 26


def test_intertidal_pool_and_bush_exclusions_have_exact_scope(monkeypatch):
    zone = "habitatmech:GOLD.115edc36f8"
    pool = "habitatmech:GOLD.d39a2ed099"
    bush = "habitatmech:GOLD.b36274f0b9"
    removed = {
        zone: "ENVO:00001999", pool: "ENVO:00002011", bush: "ENVO:00000215",
    }
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = {
        key: row for key, row in load_gold_parent_exclusions(
            seed.GOLD_PARENT_EXCLUSIONS_PATH
        ).items() if key not in removed
    }
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda path: exclusions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == set(removed)
    for identifier, parent in removed.items():
        old, new = before[identifier], after[identifier]
        assert parent in old["parent_habitats"]
        assert new.get("parent_habitats", []) == [
            value for value in old["parent_habitats"] if value != parent
        ]
        assert new["curation_history"][:-1] == old["curation_history"]
        assert new["curation_history"][-1]["action"] == "SOURCE_PARENT_EXCLUDED"
        for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
            assert new.get(field) == old.get(field), (identifier, field)
        assert new["mapping_status"] == "SEEDED"
    assert after[zone]["parent_habitats"] == ["ENVO:00000316"]
    assert after[zone]["grounding_status"] == "NARROW"
    assert after[zone]["source_attestations"][0]["assertion_count"] == 77
    assert after[zone]["source_attestations"][0]["assertion_unit"] == "ORGANISM"
    assert after[zone]["source_attestations"][0]["source_id"] == "gold.ecosystem:3770"
    assert "2 GOLD ecosystem node ids" in after[zone]["source_attestations"][0]["notes"]
    for identifier, node in ((pool, "gold.ecosystem:8268"), (bush, "gold.ecosystem:5751")):
        assert after[identifier]["grounding_status"] == "UNGROUNDED"
        attestation = after[identifier]["source_attestations"][0]
        assert attestation["source_id"] == node
        assert "assertion_count" not in attestation
        assert "assertion_unit" not in attestation
        assert "mapping_predicate" not in attestation
    assert "2 GOLD ecosystem node ids" in after[pool]["source_attestations"][0]["notes"]
    assert zone in after["ENVO:00000241"]["parent_habitats"]
    assert "ENVO:00000192" in after["ENVO:00000241"]["parent_habitats"]
    # This child is unchanged, not scientifically endorsed by the parent correction.
    assert pool in after["habitatmech:GOLD.943a41f487"]["parent_habitats"]
    assert after["habitatmech:GOLD.d29a0aa94b"] == before["habitatmech:GOLD.d29a0aa94b"]


def test_volcanic_exclusion_changes_only_context_parent_and_audit(monkeypatch):
    identifier = "habitatmech:GOLD.72de01aaaa"
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = {
        key: row for key, row in load_gold_parent_exclusions(
            seed.GOLD_PARENT_EXCLUSIONS_PATH
        ).items() if key != identifier
    }
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda path: exclusions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {identifier}
    old, new = before[identifier], after[identifier]
    assert old["parent_habitats"] == ["ENVO:00000094", "ENVO:00001999"]
    assert new["parent_habitats"] == ["ENVO:00000094"]
    assert new["curation_history"][:-1] == old["curation_history"]
    event = new["curation_history"][-1]
    assert event["action"] == "SOURCE_PARENT_EXCLUDED"
    assert event["timestamp"] == "2026-10-06T00:00:00Z"
    for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
        assert new.get(field) == old.get(field), field
    assert new["grounding_status"] == "NARROW"
    assert new["mapping_status"] == "SEEDED"
    assert len(new["source_attestations"]) == 1
    attestation = new["source_attestations"][0]
    assert attestation["source_id"] == "gold.ecosystem:3772"
    assert attestation["source_path"] == "Environmental > Aquatic > Marine > Volcanic"
    assert attestation["mapping_predicate"] == "skos:narrowMatch"
    assert attestation["assertion_count"] == 107
    assert attestation["assertion_unit"] == "ORGANISM"
    assert "2 GOLD ecosystem node ids" in attestation["notes"]
    row = next(row for row in seed.read_tsv(seed.RAW_DIR / "gold_ecosystem_paths.tsv")
               if row["canonical_path"] == attestation["source_path"])
    assert set(row["gold_node_ids"].split("|")) == {
        "gold.ecosystem:3772", "gold.ecosystem:4022",
    }


def test_water_ice_core_exclusion_changes_only_context_parent_and_audit(monkeypatch):
    source = "habitatmech:GOLD.d023ed65ca"
    identifier = "ENVO:01001530"
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = {
        key: row for key, row in load_gold_parent_exclusions(
            seed.GOLD_PARENT_EXCLUSIONS_PATH
        ).items() if key != source
    }
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda path: exclusions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {identifier}
    old, new = before[identifier], after[identifier]
    assert old["parent_habitats"] == ["ENVO:00000019", "ENVO:01000293"]
    assert new["parent_habitats"] == ["ENVO:01000293"]
    assert new["curation_history"][:-1] == old["curation_history"]
    event = new["curation_history"][-1]
    assert event["action"] == "SOURCE_PARENT_EXCLUDED"
    assert event["timestamp"] == "2026-10-06T00:00:00Z"
    assert event["curator"] == "codex-gpt-5"
    for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
        assert new.get(field) == old.get(field), field
    assert new["grounding_status"] == "CLOSE"
    assert new["mapping_status"] == "REVIEWED"
    assert new["source_attestations"] == [{
        "source": "GOLD",
        "source_id": "gold.ecosystem:7982",
        "source_label": "Ice core",
        "source_path": (
            "Environmental > Aquatic > Non-marine Saline and Alkaline > Saline lake > Ice core"
        ),
        "mapping_predicate": "skos:closeMatch",
    }]
    assert seed.mint("GOLD", new["source_attestations"][0]["source_path"]) == source


def test_bagasse_and_bench_exclusions_change_only_context_parents_and_audit(monkeypatch):
    bagasse = "ENVO:00002872"
    bench = "habitatmech:GOLD.4f9191d466"
    sources = {"habitatmech:GOLD.feb21b0386", bench}
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = {
        key: row for key, row in load_gold_parent_exclusions(
            seed.GOLD_PARENT_EXCLUSIONS_PATH
        ).items() if key not in sources
    }
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda path: exclusions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {bagasse, bench}
    assert before[bagasse]["parent_habitats"] == ["ENVO:00002264", "mesh:D062611"]
    assert after[bagasse]["parent_habitats"] == ["ENVO:00002264"]
    assert before[bench]["parent_habitats"] == ["habitatmech:GOLD.961229841c"]
    assert "parent_habitats" not in after[bench]
    for identifier in (bagasse, bench):
        old, new = before[identifier], after[identifier]
        assert new["curation_history"][:-1] == old["curation_history"]
        event = new["curation_history"][-1]
        assert event["action"] == "SOURCE_PARENT_EXCLUDED"
        assert event["timestamp"] == "2026-10-07T00:00:00Z"
        assert event["curator"] == "codex-gpt-5"
        for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
            assert new.get(field) == old.get(field), (identifier, field)
        assert new["mapping_status"] == "SEEDED"
    attestation = after[bagasse]["source_attestations"][0]
    assert attestation["source_path"] == "Engineered > Solid waste > Bagasse"
    assert attestation["source_id"] == "gold.ecosystem:4925"
    assert attestation["assertion_count"] == 23
    assert attestation["assertion_unit"] == "ORGANISM"
    assert "3 GOLD ecosystem node ids" in attestation["notes"]
    assert after[bench]["source_attestations"] == [{
        "source": "GOLD", "source_id": "gold.ecosystem:5464", "source_label": "Bench surface",
        "source_path": "Engineered > Built environment > City > Subway > Bench surface",
    }]


def test_thalassic_and_thrombolite_curation_has_exact_scope(monkeypatch):
    thalassic = "habitatmech:GOLD.3fece6dbf7"
    quality = "ENVO:01001667"
    marine = "habitatmech:GOLD.7937011195"
    microbialite = "habitatmech:GOLD.e53e2c6e8e"
    freshwater = "habitatmech:GOLD.b8b289be4a"
    targets = {thalassic, marine, microbialite}
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    decision = decisions.pop(thalassic)
    assert decision.review_depth == "ITEM"
    assert decision.decision == "CONFIRM_UNGROUNDED"
    assert decision.object_id == quality
    assert decision.relation == "xref"
    exclusions = {
        key: row for key, row in load_gold_parent_exclusions(
            seed.GOLD_PARENT_EXCLUSIONS_PATH
        ).items() if key not in targets
    }
    monkeypatch.setattr(seed, "load_decisions", lambda path: decisions)
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda path: exclusions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    assert before.keys() - after.keys() == {quality}
    assert after.keys() - before.keys() == {thalassic}
    assert {key for key in before.keys() & after.keys()
            if before[key] != after[key]} == {marine, microbialite}
    assert after[freshwater] == before[freshwater]
    assert after[freshwater]["parent_habitats"] == [microbialite]
    assert before[microbialite]["parent_habitats"] == ["ENVO:00002011", "ENVO:03600064"]
    assert after[microbialite]["parent_habitats"] == ["ENVO:03600064"]
    assert before[marine]["parent_habitats"] == ["habitatmech:GOLD.115edc36f8"]
    assert not after[marine].get("parent_habitats")
    for identifier in (marine, microbialite):
        old, new = before[identifier], after[identifier]
        assert new["curation_history"][:-1] == old["curation_history"]
        for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
            assert new.get(field) == old.get(field), (identifier, field)
        assert "assertion_count" not in new["source_attestations"][0]
        assert "assertion_unit" not in new["source_attestations"][0]
    assert after[marine]["mapping_status"] == "SEEDED"
    assert after[microbialite]["mapping_status"] == "REVIEWED"
    assert "2 GOLD ecosystem node ids" in after[microbialite]["source_attestations"][0]["notes"]

    old, new = before[quality], after[thalassic]
    assert old["grounding_status"] == "EXACT"
    assert new["grounding_status"] == "UNGROUNDED"
    assert new["mapping_status"] == "REVIEWED"
    assert new["label"] == "Thalassic"
    assert new["habitat_category"] == old["habitat_category"] == "AQUATIC"
    assert new["xrefs"] == [quality]
    for field in ("parent_habitats", "definition", "definition_source"):
        assert field not in new
    attestation = new["source_attestations"][0]
    assert old["source_attestations"][0]["mapping_predicate"] == "skos:exactMatch"
    assert "mapping_predicate" not in attestation
    assert new["source_attestations"] == [
        {key: value for key, value in old["source_attestations"][0].items()
         if key != "mapping_predicate"}
    ]
    assert attestation["source_id"] == "gold.ecosystem:3976"
    assert attestation["assertion_count"] == 1
    assert attestation["assertion_unit"] == "ORGANISM"
    assert seed.mint("GOLD", attestation["source_path"]) == thalassic
    assert [e["action"] for e in new["curation_history"]] == [
        "SEEDED_FROM_SOURCES", "CONFIRM_UNGROUNDED", "SOURCE_PARENT_EXCLUDED",
    ]
    # Seed events summarize the current reproducible build, not append-only history.
    for field in ("timestamp", "curator", "action"):
        assert new["curation_history"][0][field] == old["curation_history"][0][field]
    for identifier in targets:
        assert after[identifier]["curation_history"][-1]["action"] == "SOURCE_PARENT_EXCLUDED"
