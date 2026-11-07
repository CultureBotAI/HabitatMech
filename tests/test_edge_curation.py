"""Native HabitatMech decisions retain review depth and mapping direction."""

import csv
import importlib
import io
import os
from pathlib import Path

import pytest

from habitatmech import edge_curation as adapter
from habitatmech.edge_curation import SCHEMA, SEMANTICS, SOURCE, adapt_decision


@pytest.fixture(autouse=True)
def shared_contract():
    if os.environ.get("REQUIRE_EDGE_CONTRACT") == "1":
        importlib.import_module("kg_microbe_curation.native")
    else:
        pytest.importorskip("kg_microbe_curation.native")


def decision(**changes):
    return {
        "identifier": "habitatmech:GOLD.example",
        "decision": "GROUND_AS_PARENT",
        "object_id": "ENVO:00001998",
        "object_label": "soil",
        "review_depth": "ITEM",
        "curator": "native curator",
        "date": "2026-11-07",
        "notes": "Specific source path is narrower than the reviewed target; preserve its scope.",
        "relation": "parent",
        **changes,
    }


def adapt(row):
    return adapt_decision(
        row,
        position=1,
        commit="a" * 40,
        hashes={SOURCE: "b" * 64, SCHEMA: "c" * 64, SEMANTICS: "d" * 64},
        prefixes={"ENVO": "http://purl.obolibrary.org/obo/ENVO_"},
    )


def test_native_parent_decision_keeps_its_original_relation_scope():
    row = decision()
    actual = adapt(row)
    assert actual["payload"]["native_payload"] == row
    assert actual["payload"]["predicate"] == "habitatmech:GROUND_AS_PARENT"
    assert actual["payload"]["native_payload"]["relation"] == "parent"
    assert actual["native_review"]["payload"] == row
    assert actual["assurance"] == "inherited_native_review"
    assert actual["independent_scientific_review"] is False


@pytest.mark.parametrize(
    "changes",
    [
        {"review_depth": "CLASS"},
        {"decision": "REVIEW"},
        {"decision": "NOT_APPLICABLE"},
        {"decision": "CONFIRM_UNGROUNDED", "object_id": ""},
    ],
)
def test_other_native_states_do_not_gain_mapping_review(changes):
    row = decision(**changes)
    actual = adapt(row)
    assert actual["payload"]["native_payload"] == row
    assert actual["assurance"] == "unassessed"
    assert actual["native_review"]["locator"] is None
    assert actual["payload"]["predicate"] == "habitatmech:curation_decision"


@pytest.mark.parametrize("changes", [{"object_id": ""}, {"curator": ""}, {"notes": "short"}])
def test_incomplete_item_review_fails(changes):
    with pytest.raises(ValueError, match="Incomplete"):
        adapt(decision(**changes))


def test_changed_source_scope_changes_identity():
    assert (
        adapt(decision())["assertion_id"]
        != adapt(decision(notes="A different source scope remains a different native mapping claim."))[
            "assertion_id"
        ]
    )


def test_absent_optional_fields_remain_unassessed_and_lossless():
    original = decision(review_depth=None, relation=None)
    actual = adapt(original)
    assert actual["assurance"] == "unassessed"
    assert actual["payload"]["native_payload"] == original


@pytest.mark.parametrize("mutation", ["reverse", "duplicate"])
def test_export_rejects_changed_persisted_valid_membership(tmp_path, monkeypatch, mutation):
    first = decision(grounding_status="NARROW")
    stream = io.StringIO()
    writer = csv.DictWriter(stream, fieldnames=list(first), delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows([first, {**first, "identifier": "habitatmech:GOLD.other"}])
    sources = {
        SOURCE: stream.getvalue().encode(),
        SCHEMA: b"prefixes: {}\n",
        SEMANTICS: b"Native habitat scope.\n",
    }

    def git(command, **kwargs):
        if "get-url" in command:
            return "https://github.com/CultureBotAI/HabitatMech.git\n"
        return sources[command[-1].split(":", 1)[1]]

    monkeypatch.setattr(adapter.subprocess, "check_output", git)
    original_open = Path.open
    changed = False

    def mutate_readback(path, mode="r", *args, **kwargs):
        nonlocal changed
        if path.name == "assertions.jsonl" and mode == "rb" and not changed:
            changed = True
            with original_open(path, "rb") as handle:
                lines = handle.readlines()
            replacement = lines[::-1] if mutation == "reverse" else [lines[0], lines[0]]
            with original_open(path, "wb") as handle:
                handle.writelines(replacement)
        return original_open(path, mode, *args, **kwargs)

    monkeypatch.setattr(Path, "open", mutate_readback)
    output = tmp_path / "output"
    with pytest.raises(ValueError, match="Persisted native bytes"):
        adapter.export_assertions(tmp_path, "a" * 40, output, None)
    assert changed
    assert not output.exists()
