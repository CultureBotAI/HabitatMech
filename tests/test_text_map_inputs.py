"""Semantic input contracts run without a model or a complete corpus."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest
import yaml

from habitatmech import text_map_inputs as adapter


def write_record(root: Path, name: str, **extra) -> Path:
    path = root / "data" / adapter.CORPUS / "example" / name
    path.parent.mkdir(parents=True, exist_ok=True)
    record = {"identifier": "ENVO:1", "label": "Test entity", adapter.CATEGORY_FIELD: "OTHER"}
    record.update(extra)
    path.write_text(yaml.safe_dump(record), encoding="utf-8")
    return path


def test_jsonl_contract_and_no_input_mutation(tmp_path):
    path = write_record(tmp_path, "one.yaml")
    before = path.read_bytes()
    preview = adapter.export_inputs(tmp_path, None)
    output = tmp_path / "inputs.jsonl"
    exported = adapter.export_inputs(tmp_path, output)
    row = json.loads(output.read_text())
    assert set(row) == {
        "identifier",
        "label",
        "category",
        "page",
        "source_path",
        "text",
        "text_sha256",
        "adapter_version",
    }
    assert row["text"]
    assert row["text_sha256"] == hashlib.sha256(row["text"].encode()).hexdigest()
    assert row["source_path"] == path.relative_to(tmp_path).as_posix()
    assert preview["scope"] == exported["scope"] == "full"
    assert preview["records"] == exported["records"] == 1
    assert preview["jsonl_sha256"] == exported["jsonl_sha256"]
    assert path.read_bytes() == before


def test_duplicate_identifier_refuses_partial_output(tmp_path):
    write_record(tmp_path, "a.yaml")
    write_record(tmp_path, "b.yaml")
    output = tmp_path / "inputs.jsonl"
    output.write_text("preserve me\n")
    with pytest.raises(ValueError, match="duplicate record identifier"):
        adapter.export_inputs(tmp_path, output)
    assert output.read_text() == "preserve me\n"
    assert not list(tmp_path.glob(".text-map-*"))


def test_selecting_path_outside_corpus_is_refused(tmp_path):
    write_record(tmp_path, "a.yaml")
    elsewhere = tmp_path / "elsewhere.yaml"
    elsewhere.write_text("identifier: ENVO:1\nlabel: elsewhere\n")
    with pytest.raises(ValueError, match="leaves the corpus"):
        list(adapter.iter_inputs(tmp_path, records=["elsewhere.yaml"]))


def test_symlink_records_are_refused(tmp_path):
    real = write_record(tmp_path, "a.yaml")
    (real.parent / "linked.yaml").symlink_to(real)
    with pytest.raises(ValueError, match="symlink"):
        list(adapter.iter_inputs(tmp_path))


def test_subset_is_explicit_and_order_is_stable(tmp_path):
    first = write_record(tmp_path, "a.yaml")
    write_record(tmp_path, "z.yaml", identifier="ENVO:2")
    output = tmp_path / "canary.jsonl"
    receipt = adapter.export_inputs(tmp_path, output, limit=1)
    assert receipt["scope"] == "subset"
    assert receipt["records"] == 1
    assert json.loads(output.read_text())["source_path"] == first.relative_to(tmp_path).as_posix()
    assert (
        adapter.export_inputs(tmp_path, None, records=[first.relative_to(tmp_path).as_posix()])["scope"]
        == "subset"
    )


def test_output_suffix_and_invalid_limit_are_refused(tmp_path):
    source = write_record(tmp_path, "a.yaml")
    with pytest.raises(ValueError, match=".jsonl"):
        adapter.export_inputs(tmp_path, source)
    with pytest.raises(ValueError, match="positive"):
        adapter.export_inputs(tmp_path, None, limit=0)


def test_habitat_text_distinguishes_observation_and_parent_scope():
    record = {
        "identifier": "ENVO:1",
        "label": "salt lake",
        "definition": "A saline lake.",
        "habitat_category": "AQUATIC",
        "parent_habitats": ["ENVO:2"],
        "synonyms": [{"synonym_text": "saline lake", "source": "DOI:excluded"}],
        "environmental_parameters": [
            {
                "parameter": "SALINITY",
                "minimum_value": 0,
                "maximum_value": 10,
                "unit": "percent",
                "source": "excluded source",
            }
        ],
        "characteristic_taxa": [
            {"taxon_label": "Observed organism", "score": 999},
            {
                "taxon_label": "Characteristic organism",
                "is_characteristic": True,
                "reference": "PMID:excluded",
            },
        ],
        "curation_history": [{"changes": "excluded curation"}],
        "source_attestations": [{"notes": "excluded notes", "assertion_count": 123}],
    }
    text = adapter.semantic_text(record, {"ENVO:2": "lake"})
    assert "broader habitat: lake" in text
    assert "observed taxon: Observed organism" in text
    assert "characteristic taxon: Characteristic organism" in text
    assert "minimum 0" in text and "maximum 10" in text and "percent" in text
    for excluded in ("excluded", "ENVO:", "999", "123"):
        assert excluded not in text


def test_habitat_canary_and_full_parent_text_agree(tmp_path):
    child = write_record(tmp_path, "a.yaml", identifier="ENVO:1", parent_habitats=["ENVO:2"])
    write_record(tmp_path, "z.yaml", identifier="ENVO:2", label="broader habitat")
    full = list(adapter.iter_inputs(tmp_path))
    selected = list(adapter.iter_inputs(tmp_path, records=[child.relative_to(tmp_path).as_posix()]))
    assert full[0]["text_sha256"] == selected[0]["text_sha256"]
    assert "broader habitat: broader habitat" in selected[0]["text"]


def test_habitat_page_uses_renderer_identity_slug():
    from scripts.render_pages import slugify

    record = {"identifier": "habitatmech:GOLD.ab12", "label": "A/B <lake>"}
    assert (
        adapter.page_target(record)
        == f"habitats/{slugify(record['label'] + '-' + record['identifier'])}.html"
    )


def test_numeric_unit_identifiers_are_not_silently_dropped():
    text = adapter.semantic_text(
        {
            "label": "salty habitat",
            "environmental_parameters": [
                {"parameter": "SALINITY", "minimum_value": 1, "unit": "UO:0000185"},
            ],
        }
    )
    assert "minimum 1; unit UO:0000185" in text
