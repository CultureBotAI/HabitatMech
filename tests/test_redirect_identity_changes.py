"""Pinned YAML paths must not hide retired identifiers from URL recovery."""

from __future__ import annotations

import subprocess

import pytest
import yaml

from scripts import build_redirects


@pytest.fixture
def history_repo(tmp_path, monkeypatch):
    def git(*args):
        return subprocess.run(
            ["git", "-c", "user.name=Test", "-c", "user.email=test@example.org", *args],
            cwd=tmp_path, check=True, capture_output=True, text=True,
        ).stdout

    git("init", "-q")
    habitats = tmp_path / "data/habitats"
    habitats.mkdir(parents=True)
    pages = tmp_path / "pages/habitats"
    pages.mkdir(parents=True)
    record = habitats / "pinned.yaml"
    doc = {
        "identifier": "ENVO:01001667", "label": "thalassic",
        "habitat_category": "AQUATIC", "grounding_status": "EXACT",
        "source_attestations": [{
            "source": "GOLD", "source_id": "gold.ecosystem:3976",
            "source_label": "Thalassic", "assertion_count": 1,
            "assertion_unit": "ORGANISM",
        }],
    }
    record.write_text(yaml.safe_dump(doc, sort_keys=False))
    (pages / "thalassic-envo-01001667.html").write_text("Published habitat page")
    git("add", ".")
    git("commit", "-qm", "Publish original identity")
    monkeypatch.setattr(build_redirects, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(build_redirects, "HABITATS_DIR", habitats)
    monkeypatch.setattr(build_redirects, "RETIRED_PATH", habitats / "RETIRED.tsv")
    monkeypatch.setattr(build_redirects, "RETRACTED_PATH", tmp_path / "retractions.tsv")
    return git, record, doc


@pytest.mark.parametrize("change", ["in_place", "rename", "delete"])
def test_retired_identity_follows_source_even_when_path_is_pinned(history_repo, change):
    git, record, doc = history_repo
    if change != "in_place":
        old = record
        record = record.with_name("new.yaml")
        old.rename(record)
    if change == "delete":
        git("config", "diff.renames", "false")
    doc["identifier"] = "habitatmech:GOLD.3fece6dbf7"
    doc["label"] = "Thalassic"
    record.write_text(yaml.safe_dump(doc, sort_keys=False))
    git("add", "-A")
    git("commit", "-qm", "Correct source identity")
    status = git("diff", "--name-status", "HEAD^", "HEAD")
    assert {"in_place": "M\t", "rename": "R", "delete": "D\t"}[change] in status
    assert build_redirects.build() == [{
        "retired_slug": "thalassic-envo-01001667",
        "retired_identifier": "ENVO:01001667",
        "retired_label": "thalassic",
        "current_identifiers": "habitatmech:GOLD.3fece6dbf7",
        "resolved_by": "source_concepts_merged",
    }]


def test_record_edits_and_pure_moves_do_not_retire_identity(history_repo):
    git, record, doc = history_repo
    doc["definition"] = "A changed description, not an identity change."
    record.write_text(yaml.safe_dump(doc, sort_keys=False))
    git("add", "-A")
    git("commit", "-qm", "Edit description")
    assert build_redirects.retired_record_details() == ({}, {})
    record.rename(record.with_name("moved.yaml"))
    git("add", "-A")
    git("commit", "-qm", "Move unchanged record")
    sources, labels = build_redirects.retired_record_details()
    assert sources == {doc["identifier"]: {"gold.ecosystem:3976"}}
    assert labels == {doc["identifier"]: doc["label"]}
    assert build_redirects.build() == []


def test_identifier_serialization_change_does_not_retire_identity(history_repo):
    git, record, _ = history_repo
    record.write_text(record.read_text().replace(
        "identifier: ENVO:01001667", "identifier: 'ENVO:01001667'",
    ))
    git("add", "-A")
    git("commit", "-qm", "Quote unchanged identifier")
    assert build_redirects.retired_record_details() == ({}, {})
    assert build_redirects.build() == []
