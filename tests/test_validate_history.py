"""The history validator's structural pre-check stays in step with claw's.

claw's `kg-microbe-history validate` refuses a record before schema validation
when it is structurally incomplete or still carries the scaffolder placeholder.
scripts/validate_history.py mirrors that check so `just qc` rejects the same
drafts without a claw checkout; this pins the surface most likely to drift.
"""

from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_history", REPO_ROOT / "scripts" / "validate_history.py"
)
validate_history = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(validate_history)

RECORDS = sorted((REPO_ROOT / "history").rglob("*.yaml"))


def _write(tmp_path: Path, doc: dict) -> Path:
    path = tmp_path / "record.yaml"
    path.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")
    return path


def _committed() -> dict:
    assert RECORDS, "the repository ships at least one history record"
    return yaml.safe_load(RECORDS[0].read_text(encoding="utf-8"))


def test_placeholder_matches_claws_prefix():
    assert validate_history.PLACEHOLDER == "TODO: replace this placeholder"


def test_every_committed_record_passes_the_pre_check():
    for path in RECORDS:
        assert validate_history.structural_problem(path) is None, path


def test_a_scaffolder_placeholder_is_refused(tmp_path):
    doc = copy.deepcopy(_committed())
    doc["events"][0]["details"] = "TODO: replace this placeholder before committing."
    problem = validate_history.structural_problem(_write(tmp_path, doc))
    assert problem and "placeholder" in problem


def test_missing_actors_events_or_details_are_refused(tmp_path):
    base = _committed()

    doc = copy.deepcopy(base)
    doc["session"]["actors"] = []
    assert "actors" in (validate_history.structural_problem(_write(tmp_path, doc)) or "")

    doc = copy.deepcopy(base)
    doc["session"]["actors"] = "claude-code"
    assert "actors" in (validate_history.structural_problem(_write(tmp_path, doc)) or "")

    doc = copy.deepcopy(base)
    doc["events"] = []
    assert "events" in (validate_history.structural_problem(_write(tmp_path, doc)) or "")

    doc = copy.deepcopy(base)
    doc["events"][0]["details"] = 123
    assert "details" in (validate_history.structural_problem(_write(tmp_path, doc)) or "")
