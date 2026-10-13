"""Alias opt-outs must be explicit, fail closed and preserve unrelated claims."""

from __future__ import annotations

import csv
from dataclasses import asdict, replace

import pytest

from habitatmech import seed
from habitatmech.curate.definition_source_label_exclusions import (
    DefinitionSourceLabelExclusion,
    DefinitionSourceLabelExclusionError,
    load_definition_source_label_exclusions,
)
from habitatmech.curate.definitions import CuratedDefinition
from habitatmech.text_map_inputs import semantic_text

EXCLUSION = DefinitionSourceLabelExclusion(
    "habitatmech:test", "Indoor", "indoor channel", "test", "2026-10-08",
    "The bare adjective is ambiguous outside its source context.",
)


def write_table(path, rows):
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(asdict(EXCLUSION)), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def fixture_store():
    store = seed.ConceptStore(seed.OntologyIndex([
        {"term_id": "ENVO:test", "label": "vivarium", "ontology": "ENVO"},
    ], []))
    concept = store.get(EXCLUSION.identifier, EXCLUSION.source_label, "UNGROUNDED")
    concept.attestations = [{"source": "GOLD", "source_label": "Indoor"}]
    definition = CuratedDefinition(
        identifier=concept.identifier, label=EXCLUSION.requested_label,
        parent_class="ENVO:test", parent_label="vivarium",
        definition="A vivarium with a channel indoors.", exact_synonyms=("indoor test channel",),
        curator="test", date="2026-09-18", notes="The original definition.",
    )
    return store, concept, definition


def test_loader_round_trip_and_required_file(tmp_path):
    path = tmp_path / "exclusions.tsv"
    with pytest.raises(FileNotFoundError):
        load_definition_source_label_exclusions(path)
    write_table(path, [asdict(EXCLUSION)])
    assert load_definition_source_label_exclusions(path) == {EXCLUSION.identifier: EXCLUSION}


@pytest.mark.parametrize("field,value", [
    ("identifier", "ENVO:1"), ("source_label", ""), ("requested_label", ""),
    ("curator", ""), ("notes", "short"), ("date", "20261008"), ("date", "2026-02-30"),
])
def test_loader_rejects_malformed_rows(tmp_path, field, value):
    path = tmp_path / "exclusions.tsv"
    write_table(path, [{**asdict(EXCLUSION), field: value}])
    with pytest.raises(DefinitionSourceLabelExclusionError):
        load_definition_source_label_exclusions(path)


def test_loader_rejects_duplicate_and_extra_fields(tmp_path):
    path = tmp_path / "exclusions.tsv"
    write_table(path, [asdict(EXCLUSION)] * 2)
    with pytest.raises(DefinitionSourceLabelExclusionError, match="duplicate"):
        load_definition_source_label_exclusions(path)
    write_table(path, [asdict(EXCLUSION)])
    path.write_text(path.read_text().rstrip("\n") + "\textra\n")
    with pytest.raises(DefinitionSourceLabelExclusionError, match="extra fields"):
        load_definition_source_label_exclusions(path)
    path.write_text("identifier\n")
    with pytest.raises(DefinitionSourceLabelExclusionError, match="expected columns"):
        load_definition_source_label_exclusions(path)


@pytest.mark.parametrize("field,value,message", [
    ("identifier", "habitatmech:missing", "no matching"),
    ("source_label", "Outdoor", "stale source_label"),
    ("requested_label", "outdoor channel", "stale requested_label"),
])
def test_stale_exclusions_fail_before_mutation(field, value, message):
    store, concept, definition = fixture_store()
    item = replace(EXCLUSION, **{field: value})
    with pytest.raises(DefinitionSourceLabelExclusionError, match=message):
        seed.apply_curated_definitions(store, {concept.identifier: definition}, {item.identifier: item})
    assert concept.label == "Indoor"
    assert concept.definition == ""


@pytest.mark.parametrize("alias", ["Indoor", " INDOOR ", "(Indoor)"])
def test_excluded_label_cannot_be_reauthored_as_exact(alias):
    store, concept, definition = fixture_store()
    definition = replace(definition, exact_synonyms=(alias,))
    with pytest.raises(DefinitionSourceLabelExclusionError, match="authored exact synonym"):
        seed.apply_curated_definitions(
            store, {concept.identifier: definition}, {EXCLUSION.identifier: EXCLUSION},
        )


def test_no_op_exclusion_is_rejected():
    store, concept, definition = fixture_store()
    definition = replace(definition, label="INDOOR")
    item = replace(EXCLUSION, requested_label=definition.label)
    with pytest.raises(DefinitionSourceLabelExclusionError, match="not renamed"):
        seed.apply_curated_definitions(store, {concept.identifier: definition}, {item.identifier: item})


def test_only_automatic_retention_is_omitted():
    store, concept, definition = fixture_store()
    concept.add_synonym("indoor facility", "RELATED_SYNONYM", "independent source")
    seed.apply_curated_definitions(
        store, {concept.identifier: definition}, {EXCLUSION.identifier: EXCLUSION},
    )
    assert concept.synonyms == {
        ("indoor facility", "RELATED_SYNONYM"): "independent source",
        ("indoor test channel", "EXACT_SYNONYM"): "HabitatMech curation",
    }
    doc = seed.build_document(concept)
    assert doc["source_attestations"][0]["source_label"] == "Indoor"
    event = doc["curation_history"][-1]
    assert event["action"] == "SOURCE_SYNONYM_EXCLUDED"
    assert event["timestamp"] == "2026-10-08T00:00:00Z"
    assert event["curator"] == EXCLUSION.curator
    assert EXCLUSION.notes in event["changes"]


@pytest.mark.parametrize("source,scope", [("GOLD", "EXACT_SYNONYM"), ("PREGO", "RELATED_SYNONYM")])
def test_omitting_policy_preserves_default_source_scope(source, scope):
    store, concept, definition = fixture_store()
    concept.attestations[0]["source"] = source
    seed.apply_curated_definitions(store, {concept.identifier: definition})
    assert ("Indoor", scope) in concept.synonyms
    assert not concept.definition_source_label_exclusions_applied


def test_indoor_exclusion_changes_only_fallback_alias_and_audit(monkeypatch):
    identifier = "habitatmech:GOLD.b4e93f5d66"
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = load_definition_source_label_exclusions(seed.DEFINITION_SOURCE_LABEL_EXCLUSIONS_PATH)
    monkeypatch.setattr(seed, "load_definition_source_label_exclusions", lambda path: {
        key: row for key, row in exclusions.items() if key != identifier
    })
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {identifier}
    old, new = before[identifier], after[identifier]
    assert old["synonyms"] == [{
        "synonym_text": "Indoor", "synonym_type": "EXACT_SYNONYM", "source": "HabitatMech curation",
    }]
    assert not new.get("synonyms")
    assert new["curation_history"][:-1] == old["curation_history"]
    assert new["curation_history"][-1]["action"] == "SOURCE_SYNONYM_EXCLUDED"
    for field in (old.keys() | new.keys()) - {"synonyms", "curation_history"}:
        assert new.get(field) == old.get(field), field
    assert new["mapping_status"] == "REVIEWED"
    assert new["grounding_status"] == "UNGROUNDED"
    assert new["parent_habitats"] == ["ENVO:00010622", "habitatmech:GOLD.87bf5e5370"]
    attestation = new["source_attestations"][0]
    assert attestation["source_id"] == "gold.ecosystem:8490"
    assert attestation["source_label"] == "Indoor"
    assert "assertion_count" not in attestation
    assert "assertion_unit" not in attestation


def test_material_exclusion_preserves_definition_provenance_and_other_records(monkeypatch):
    identifier = "habitatmech:GOLD.7dd45e072b"
    path = "Engineered > Industrial production > Engineered product > Material"
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = load_definition_source_label_exclusions(seed.DEFINITION_SOURCE_LABEL_EXCLUSIONS_PATH)
    exclusion = exclusions.pop(identifier)
    assert exclusion.source_label == "Material"
    assert exclusion.requested_label == "solid manufactured material"
    assert seed.mint("GOLD", path) == identifier
    monkeypatch.setattr(seed, "load_definition_source_label_exclusions", lambda _: exclusions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {identifier}
    old, new = before[identifier], after[identifier]
    assert old["synonyms"] == [{
        "synonym_text": "Material", "synonym_type": "EXACT_SYNONYM", "source": "HabitatMech curation",
    }]
    assert not new.get("synonyms")
    assert new["curation_history"][:-1] == old["curation_history"]
    event = new["curation_history"][-1]
    assert event["action"] == "SOURCE_SYNONYM_EXCLUDED"
    assert event["timestamp"] == "2026-10-09T00:00:00Z"
    assert event["curator"] == "codex-gpt-5"
    assert exclusion.notes in event["changes"]
    for field in (old.keys() | new.keys()) - {"synonyms", "curation_history"}:
        assert new.get(field) == old.get(field), field
    assert new["label"] == "solid manufactured material"
    assert new["definition_source"] == "HabitatMech"
    assert new["mapping_status"] == "REVIEWED"
    assert new["grounding_status"] == "UNGROUNDED"
    assert new["parent_habitats"] == ["ENVO:00003074", "habitatmech:GOLD.74bb2a619a"]
    assert len(new["source_attestations"]) == 1
    attestation = new["source_attestations"][0]
    assert attestation["source"] == "GOLD"
    assert attestation["source_id"] == "gold.ecosystem:8333"
    assert attestation["source_label"] == "Material"
    assert attestation["source_path"] == path
    assert "2 GOLD ecosystem node ids" in attestation["notes"]
    assert not {"assertion_count", "assertion_unit", "mapping_predicate"} & attestation.keys()
    assert semantic_text(new) != semantic_text(old)
