"""The shared QC runner preserves the intent and flags of its component gates."""

from __future__ import annotations

from scripts import run_qc


def gates() -> dict[str, tuple[list[str], str]]:
    return {name: (command, rationale) for name, command, rationale in run_qc.COMMANDS}


def test_every_qc_gate_explains_why_it_exists():
    for name, _command, rationale in run_qc.COMMANDS:
        assert len(rationale.split()) >= 6, f"{name} lost its operational rationale"


def test_noisy_full_corpus_commands_keep_their_quiet_flags():
    by_name = gates()
    assert by_name["tests"][0][-1] == "-q"
    assert by_name["schema validation"][0][-1] == "--quiet"


def test_corpus_wide_tests_run_before_per_record_schema_validation():
    names = [name for name, _command, _rationale in run_qc.COMMANDS]
    assert names.index("tests") < names.index("schema validation")
