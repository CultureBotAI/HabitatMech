"""Tests for HabitatMech deep-research command wiring."""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from research_habitat import build_command, load_record, main, template_vars  # noqa: E402

IDENTIFIER = "habitatmech:PREGO.c312b0d6fc"


def test_record_lookup_and_template_context():
    path, doc = load_record(IDENTIFIER)
    assert path.name == "tuberclar.yaml"
    variables = template_vars(doc)
    assert variables["habitat_identifier"] == IDENTIFIER
    assert variables["habitat_label"] == "tuberclar"
    assert "PREGO" in variables["attestations"]


def test_openscientist_command_uses_isolated_multiword_client():
    _path, doc = load_record(IDENTIFIER)
    command = build_command(
        provider="openscientist",
        output_file=Path("research/report.md"),
        variables=template_vars(doc),
        passthrough=[],
        client_command="uvx --from deep-research-client deep-research-client",
    )
    assert command[:5] == [
        "uvx",
        "--from",
        "deep-research-client",
        "deep-research-client",
        "research",
    ]
    assert command[command.index("--provider") + 1] == "openscientist"


def test_codex_dry_run_uses_native_validated_lane(capsys):
    assert main(["--identifier", IDENTIFIER, "--provider", "codex", "--dry-run"]) == 0
    output = capsys.readouterr().out
    assert "codex --search --ask-for-approval never exec" in output
    assert "schema validated" in output
