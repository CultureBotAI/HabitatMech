"""Annotation repairs must be exact, auditable and independent of source data."""

import copy
import csv
from dataclasses import asdict, replace

import pytest

from habitatmech import seed
from habitatmech.curate.record_annotation_corrections import (
    RecordAnnotationCorrection,
    RecordAnnotationCorrectionError,
    apply_record_annotation_corrections,
    load_record_annotation_corrections,
)

SYNONYM = RecordAnnotationCorrection(
    "starter-synonym", "ENVO:03600040", "synonym_type", "Daqu", "ENVO",
    "EXACT_SYNONYM", "NARROW_SYNONYM", "test", "2026-10-14",
    "https://pubmed.ncbi.nlm.nih.gov/24863368/", "Evidence establishes narrower starter scope.",
)
TAXON = replace(
    SYNONYM, correction_id="starter-taxon", field="taxon_label", item="NCBITaxon:86957",
    source="BACDIVE", expected="Schleiferibacter lactififex",
    replacement="Schleiferibacter lacticifex",
)


def write_table(path, rows):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(SYNONYM)), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def concept():
    result = seed.Concept(SYNONYM.identifier, "fermentation starter", "EXACT", category="FOOD")
    result.synonyms = {("Daqu", "EXACT_SYNONYM"): "ENVO", ("Starter-culture", "EXACT_SYNONYM"): "BacDive"}
    result.taxa = {TAXON.item: {"taxon_id": TAXON.item, "source": "BACDIVE",
        "taxon_label": TAXON.expected, "association_count": 1, "rank": 15, "candidate_pool": 15}}
    return result


def test_loader_requires_file_and_roundtrips(tmp_path):
    path = tmp_path / "corrections.tsv"
    with pytest.raises(FileNotFoundError):
        load_record_annotation_corrections(path)
    write_table(path, [asdict(SYNONYM), asdict(TAXON)])
    assert load_record_annotation_corrections(path) == [SYNONYM, TAXON]


@pytest.mark.parametrize("field,value", [
    ("correction_id", "Invalid key"), ("identifier", "no curie"), ("field", "definition"),
    ("source", "BACDIVE"), ("expected", "EXACT"), ("replacement", "EXACT_SYNONYM"),
    ("date", "20261014"), ("date", "2026-02-30"), ("evidence", "unverified"),
    ("notes", "short"), ("curator", ""), ("item", ""),
])
def test_loader_rejects_invalid_annotations(tmp_path, field, value):
    path = tmp_path / "corrections.tsv"
    write_table(path, [{**asdict(SYNONYM), field: value}])
    with pytest.raises(RecordAnnotationCorrectionError):
        load_record_annotation_corrections(path)


@pytest.mark.parametrize("field,value", [("item", "ENVO:1"), ("source", "GOLD")])
def test_loader_rejects_invalid_taxon_scope(tmp_path, field, value):
    path = tmp_path / "corrections.tsv"
    write_table(path, [{**asdict(TAXON), field: value}])
    with pytest.raises(RecordAnnotationCorrectionError):
        load_record_annotation_corrections(path)


@pytest.mark.parametrize("other", [SYNONYM, replace(SYNONYM, correction_id="other-id")])
def test_loader_rejects_duplicate_id_or_claim(tmp_path, other):
    path = tmp_path / "corrections.tsv"
    write_table(path, [asdict(SYNONYM), asdict(other)])
    with pytest.raises(RecordAnnotationCorrectionError, match="duplicate"):
        load_record_annotation_corrections(path)


@pytest.mark.parametrize("contents", [
    "identifier\tnotes\n", "\t".join(asdict(SYNONYM)) + "\n\t\n",
    "\t".join(asdict(SYNONYM)) + "\n" + "\t".join(asdict(SYNONYM).values()) + "\textra\n",
])
def test_loader_rejects_malformed_shape(tmp_path, contents):
    path = tmp_path / "corrections.tsv"
    path.write_text(contents, encoding="utf-8")
    with pytest.raises(RecordAnnotationCorrectionError):
        load_record_annotation_corrections(path)


def test_annotation_changes_and_audit_are_narrow_and_reproducible():
    current = concept()
    old = copy.deepcopy(current)
    apply_record_annotation_corrections({current.identifier: current}, [SYNONYM, TAXON])
    assert current.synonyms == {("Daqu", "NARROW_SYNONYM"): "ENVO",
                                ("Starter-culture", "EXACT_SYNONYM"): "BacDive"}
    assert current.taxa[TAXON.item] == {**old.taxa[TAXON.item], "taxon_label": TAXON.replacement}
    doc = seed.build_document(current)
    assert doc == seed.build_document(current)
    events = [e for e in doc["curation_history"] if e["action"] == "ANNOTATION_CORRECTED"]
    assert len(events) == 2
    assert all(e["curator"] == "test" and e["timestamp"] == "2026-10-14T00:00:00Z" for e in events)
    assert doc["mapping_status"] == "SEEDED"


@pytest.mark.parametrize("change", [
    "missing-record", "synonym-source", "synonym-scope", "conflicting-scope",
    "missing-taxon", "taxon-source", "taxon-label",
])
def test_all_stale_preconditions_fail_before_any_mutation(change):
    current = concept()
    concepts = {current.identifier: current}
    if change == "missing-record":
        concepts = {}
    elif change == "synonym-source":
        current.synonyms[("Daqu", "EXACT_SYNONYM")] = "GOLD"
    elif change == "synonym-scope":
        current.synonyms = {("Daqu", "RELATED_SYNONYM"): "ENVO"}
    elif change == "conflicting-scope":
        current.synonyms[("Daqu", "NARROW_SYNONYM")] = "ENVO"
    elif change == "missing-taxon":
        current.taxa = {}
    elif change == "taxon-source":
        current.taxa[TAXON.item]["source"] = "PREGO"
    else:
        current.taxa[TAXON.item]["taxon_label"] = TAXON.replacement
    before = copy.deepcopy(concepts)
    with pytest.raises(RecordAnnotationCorrectionError):
        apply_record_annotation_corrections(concepts, [SYNONYM, TAXON])
    assert concepts == before
