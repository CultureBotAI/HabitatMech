#!/usr/bin/env python3
"""Validate repository history records against the vendored claw schema.

One implementation, called by both `just validate-history` and `scripts/run_qc.py`,
so the gate does not depend on the task runner being installed: CI runs qc with
uv alone.

    python scripts/validate_history.py                     # everything under history/
    python scripts/validate_history.py history/records/x/y.yaml

Two checks, in order. A structural pre-check mirrors what claw's own
`kg-microbe-history validate` refuses before it reaches the schema: a record that
still carries the scaffolder's TODO placeholder in an event's details is not a
record, it is a draft, and must not be committed. Then `linkml-validate` runs
against the vendored `history.yaml` with target class HistoryRecord.
"""

from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA = REPO_ROOT / "src" / "habitatmech" / "schema" / "history.yaml"
TARGET_CLASS = "HistoryRecord"
PLACEHOLDER = "TODO: replace this placeholder"


def records(target: Path) -> list[Path]:
    if target.is_dir():
        return sorted(p for p in target.rglob("*") if p.suffix in {".yaml", ".yml"})
    return [target]


def structural_problem(path: Path) -> str | None:
    """The pre-checks claw applies before schema validation, kept in step with it."""
    try:
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:  # pragma: no cover - exercised by hand
        return f"not parseable YAML: {exc}"
    if not isinstance(doc, dict):
        return "top level is not a mapping"
    session = doc.get("session")
    if not isinstance(session, dict):
        return "session is missing or not a mapping"
    actors = session.get("actors")
    if not isinstance(actors, list) or not actors:
        return "session.actors is missing, not a list, or empty"
    events = doc.get("events")
    if not isinstance(events, list) or not events:
        return "events is missing, not a list, or empty"
    for i, event in enumerate(events):
        if not isinstance(event, dict):
            return f"events[{i}] is not a mapping"
        details = event.get("details")
        if not isinstance(details, str) or not details.strip():
            return f"events[{i}].details is missing or not a non-empty string"
        if details.strip().startswith(PLACEHOLDER):
            return f"events[{i}].details still holds the scaffolder placeholder"
    return None


def validator_command() -> list[str] | None:
    """The linkml validator, invoked through the interpreter that is running.

    Not the `linkml-validate` console script: its shebang is the absolute path of
    the interpreter that existed when the virtualenv was built, so moving the
    checkout leaves a script that cannot start, and execve reports that as a bare
    ENOENT rather than as the stale shebang it is. Calling the same entry point
    with `sys.executable` cannot go stale that way, and it guarantees the
    validator runs in the environment that just parsed these records.
    """
    if importlib.util.find_spec("linkml.validator") is None:
        return None
    return [sys.executable, "-c", "from linkml.validator.cli import cli; cli()"]


def main() -> int:
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO_ROOT / "history"
    if not target.exists():
        print(f"validate-history: {target} does not exist", file=sys.stderr)
        return 2
    paths = records(target)
    if not paths:
        print(f"No history records under {target}.")
        return 0

    failures = 0
    for path in paths:
        problem = structural_problem(path)
        if problem:
            failures += 1
            print(f"{path}: {problem}", file=sys.stderr)
    if failures:
        return 1

    command = validator_command()
    if command is None:
        print("validate-history: linkml is not installed in this environment; run "
              "`just validate-history`, or `uv run python scripts/validate_history.py`",
              file=sys.stderr)
        return 2
    result = subprocess.run(
        [*command, "--schema", str(SCHEMA), "--target-class", TARGET_CLASS,
         *[str(p) for p in paths]],
        cwd=REPO_ROOT, check=False,
    )
    if result.returncode:
        return result.returncode
    print(f"{len(paths)} history record(s) valid against {SCHEMA.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
