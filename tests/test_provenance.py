"""Committed raw inventories have complete, byte-checked provenance."""

from __future__ import annotations

from copy import deepcopy

import pytest
import yaml

from scripts import check_provenance


def test_every_committed_raw_tsv_has_valid_provenance():
    assert not check_provenance.problems()


def manifest_documents():
    kg = yaml.safe_load(check_provenance.KG_MANIFEST.read_text(encoding="utf-8"))
    gold = yaml.safe_load(check_provenance.GOLD_MANIFEST.read_text(encoding="utf-8"))
    return kg, gold


@pytest.mark.parametrize("field", ["generator", "source", "bytes", "rows", "sha256"])
def test_gold_output_integrity_fields_are_required(field):
    kg, gold = manifest_documents()
    broken = deepcopy(gold)
    del broken["outputs"][0][field]
    failures = check_provenance.manifest_contract_problems(kg, broken)
    assert any(f"missing {field}" in failure for failure in failures)


def test_pipeline_commit_is_required():
    kg, gold = manifest_documents()
    gold["pipeline_commit"] = ""
    failures = check_provenance.manifest_contract_problems(kg, gold)
    assert any("pipeline_commit" in failure for failure in failures)


def test_api_query_scope_is_required():
    kg, gold = manifest_documents()
    api_source = next(source for source in gold["sources"] if source["kind"] == "api_sweep")
    del api_source["query_scope"]["studies_requested"]
    failures = check_provenance.manifest_contract_problems(kg, gold)
    assert any("studies_requested" in failure for failure in failures)


def test_legacy_output_row_contract_is_required():
    kg, gold = manifest_documents()
    del kg["outputs"][0]["rows"]
    failures = check_provenance.manifest_contract_problems(kg, gold)
    assert any("missing rows" in failure for failure in failures)
