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
        if definition.parent_mode == "REPLACE":
            assert concept.parents == {definition.parent_class}

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


def test_host_definition_batch_preserves_habitat_and_xref_semantics(repo_root):
    from habitatmech.seed import build_corpus, build_document

    expected = {
        "habitatmech:GOLD.44a2cbbd60": (
            "chelicerate-associated environment",
            "ENVO:01001002",
            {"NCBITaxon:6656"},
        ),
        "habitatmech:GOLD.184cc9e802": (
            "green-alga-associated environment",
            "ENVO:01001001",
            {"FOODON:03412502"},
        ),
        "habitatmech:GOLD.1cbfc76870": (
            "insect larva-associated environment",
            "ENVO:01001002",
            {"UBERON:0002548"},
        ),
        "habitatmech:GOLD.34c28836da": (
            "ascidian-associated environment",
            "ENVO:01001176",
            set(),
        ),
        "habitatmech:GOLD.e789c273d0": (
            "red-alga-associated environment",
            "ENVO:01001000",
            {"FOODON:03411743"},
        ),
        "habitatmech:GOLD.5e1a5d695c": (
            "lichen-associated environment",
            "ENVO:01001041",
            {"FOODON:03412345"},
        ),
        "habitatmech:GOLD.1276bea544": (
            "diatom-associated environment",
            "ENVO:01001000",
            {"NCBITaxon:2836"},
        ),
    }

    concepts = {concept.identifier: concept for concept in build_corpus().concepts}
    definitions = load_curated_definitions(repo_root / "curation" / "term_requests.tsv")
    for identifier, (label, parent, xrefs) in expected.items():
        concept = concepts[identifier]
        doc = build_document(concept)
        authored = definitions[identifier]
        assert concept.label == label
        assert parent in concept.parents
        assert xrefs <= set(doc.get("xrefs", []))
        assert set(authored.exact_synonyms) <= {
            synonym["synonym_text"] for synonym in doc.get("synonyms", [])
        }
        assert doc["definition_source"] == "HabitatMech"

    # ADD is deliberately backward-compatible: the authored ontology genus
    # supplements a true GOLD hierarchy edge rather than erasing it (#191).
    assert concepts["habitatmech:GOLD.1276bea544"].parents >= {
        "ENVO:01001000",
        "habitatmech:GOLD.02383c20a7",
    }


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

    with pytest.raises(DefinitionError) as raised:
        load_curated_definitions(path)

    # The message has to name BOTH exits. Its first wording said only "merge
    # duplicate concepts before defining them", which is the wrong instruction
    # for the majority of real collisions: human-skin Lesion and fish-skin
    # Lesion share a source label and are different concepts, and merging them
    # would destroy the host distinction (#161).
    message = str(raised.value)
    assert "SAME_AS" in message, message
    assert "its own label" in message, message


def test_curated_definition_loader_rejects_unknown_parent_mode(tmp_path):
    path = tmp_path / "definitions.tsv"
    path.write_text(
        "identifier\trequested_label\tparent_class\tparent_label\tdefinition\t"
        "exact_synonym\tcurator\tdate\tnotes\tparent_mode\n"
        "habitatmech:x\tx environment\tENVO:1\tenvironment\t"
        "An environment.\tX\ttest\t2026-08-21\tA considered definition.\tRESET\n",
        encoding="utf-8",
    )

    with pytest.raises(DefinitionError, match="parent_mode 'RESET'"):
        load_curated_definitions(path)
