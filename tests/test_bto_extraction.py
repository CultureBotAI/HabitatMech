"""BTO semsql extraction must preserve declared deprecation metadata."""

import sqlite3

import pytest

from habitatmech.extract import _load_bto


@pytest.mark.parametrize("literal", ["true", "false", "1", "0", " true "])
def test_bto_deprecation_is_preserved_without_changing_other_fields(tmp_path, literal):
    raw = tmp_path / "data" / "raw"
    raw.mkdir(parents=True)
    with sqlite3.connect(raw / "bto.db") as conn:
        conn.execute("CREATE TABLE statements (subject TEXT, predicate TEXT, object TEXT, value TEXT)")
        conn.executemany("INSERT INTO statements VALUES (?, ?, ?, ?)", [
            ("BTO:0000316", "rdfs:label", None, "culture medium"),
            ("BTO:0000316", "IAO:0000115", None, "A cultivation substance."),
            ("BTO:0000316", "owl:deprecated", None, literal),
            ("BTO:0002233", "rdfs:label", None, "culture fluid"),
            ("BTO:0002233", "rdfs:subClassOf", "BTO:0000001", None),
            ("BTO:9999999", "owl:deprecated", None, "true"),
            ("ENVO:0000001", "rdfs:label", None, "other ontology"),
            ("ENVO:0000001", "owl:deprecated", None, "true"),
        ])

    terms, edges = _load_bto(tmp_path)
    assert terms == {
        "BTO:0000316": {
            "label": "culture medium", "definition": "A cultivation substance.",
            "synonyms": "", "deprecated": literal.strip(),
        },
        "BTO:0002233": {
            "label": "culture fluid", "definition": "", "synonyms": "", "deprecated": "",
        },
    }
    assert edges == [("BTO:0002233", "biolink:subclass_of", "BTO:0000001")]


def test_missing_bto_database_is_not_created(tmp_path):
    assert _load_bto(tmp_path) == ({}, [])
    assert not (tmp_path / "data" / "raw" / "bto.db").exists()
