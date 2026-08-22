from __future__ import annotations

import csv

import pytest

from habitatmech.curate.definitions import (
    DefinitionError,
    load_curated_definitions,
)


def test_authored_definitions_are_applied_to_generated_concepts(repo_root):
    from habitatmech.seed import build_corpus, build_document

    corpus = build_corpus()
    concepts = {concept.identifier: concept for concept in corpus.concepts}
    authored = load_curated_definitions(repo_root / "curation" / "term_requests.tsv")
    assert authored

    for identifier, definition in authored.items():
        concept = concepts[identifier]
        assert concept.label == definition.label
        assert concept.definition == definition.definition
        assert concept.definition_source == "HabitatMech"
        assert definition.parent_class in concept.parents

    example = concepts["habitatmech:GOLD.cd0b0940e5"]
    doc = build_document(example)
    assert any(
        event["action"] == "DEFINED"
        and event["curator"] == authored[example.identifier].curator
        for event in doc["curation_history"]
    )
    assert {synonym["synonym_text"] for synonym in doc["synonyms"]} >= {
        "Mammals: Human",
        "Human",
        "human host",
    }


def test_pending_definition_worklist_excludes_authored_and_rejected(repo_root):
    from scripts import build_term_requests, research_habitat

    pending = research_habitat.undefined_novel_terms()
    pending_ids = {identifier for _volume, _label, identifier in pending}
    authored = {
        row["identifier"] for row in build_term_requests.load_requests()
    }
    excluded = set(build_term_requests.excluded())

    assert not pending_ids & authored
    assert not pending_ids & excluded

    with (repo_root / "curation" / "decisions.tsv").open(
        newline="", encoding="utf-8"
    ) as fh:
        decisions = {row["identifier"]: row for row in csv.DictReader(fh, delimiter="\t")}
    expected = build_term_requests.unrequested(
        build_term_requests.load_corpus(), authored, decisions
    )
    assert pending == expected


def test_curated_definition_loader_rejects_duplicate_identifiers(tmp_path):
    path = tmp_path / "definitions.tsv"
    header = (
        "identifier\trequested_label\tparent_class\tparent_label\tdefinition\t"
        "exact_synonym\tcurator\tdate\tnotes\n"
    )
    row = (
        "habitatmech:x\tx environment\tENVO:1\tenvironment\t"
        "An environment.\tX\ttest\t2026-08-21\tA considered definition.\n"
    )
    path.write_text(header + row + row, encoding="utf-8")

    with pytest.raises(DefinitionError, match="duplicate definition"):
        load_curated_definitions(path)


def test_curated_definition_loader_rejects_duplicate_labels(tmp_path):
    path = tmp_path / "definitions.tsv"
    header = (
        "identifier\trequested_label\tparent_class\tparent_label\tdefinition\t"
        "exact_synonym\tcurator\tdate\tnotes\n"
    )
    first = (
        "habitatmech:x\tshared environment\tENVO:1\tenvironment\t"
        "An environment.\tX\ttest\t2026-08-21\tA considered definition.\n"
    )
    second = (
        "habitatmech:y\t Shared   Environment \tENVO:2\thabitat\t"
        "A habitat.\tY\ttest\t2026-08-21\tAnother considered definition.\n"
    )
    path.write_text(header + first + second, encoding="utf-8")

    with pytest.raises(DefinitionError, match="merge duplicate concepts"):
        load_curated_definitions(path)
