"""The gate that asks whether the curation inputs still contain what they did.

Everything else in `just qc` compares generated output against these files, so
a file that loses rows produces a corpus that is internally consistent and
merely missing decisions -- and passes. That happened in a merge (#219).
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest


@pytest.fixture
def repo(tmp_path):
    """A throwaway repository with one curation input and one commit."""
    def git(*args):
        subprocess.run(["git", *args], cwd=tmp_path, check=True,
                       capture_output=True, text=True)

    git("init", "-q", "-b", "main")
    git("config", "user.email", "t@example.invalid")
    git("config", "user.name", "test")
    (tmp_path / "curation").mkdir()
    (tmp_path / "scripts").mkdir()
    script = Path(__file__).resolve().parents[1] / "scripts" / "check_curation_floor.py"
    (tmp_path / "scripts" / "check_curation_floor.py").write_text(
        script.read_text(encoding="utf-8"), encoding="utf-8"
    )
    tsv = tmp_path / "curation" / "term_requests.tsv"
    tsv.write_text("identifier\trequested_label\nhabitatmech:A\ta\nhabitatmech:B\tb\n",
                   encoding="utf-8")
    git("add", "-A")
    git("commit", "-qm", "first")
    return tmp_path, tsv


def run(cwd, *args):
    return subprocess.run(
        [sys.executable, "scripts/check_curation_floor.py", *args],
        cwd=cwd, capture_output=True, text=True,
    )


def test_an_unchanged_input_passes(repo):
    cwd, _ = repo
    done = run(cwd, "--base", "HEAD")
    assert done.returncode == 0, done.stderr


def test_an_appended_row_passes(repo):
    """Curation inputs are append-mostly; growth is the normal case."""
    cwd, tsv = repo
    tsv.write_text(tsv.read_text() + "habitatmech:C\tc\n", encoding="utf-8")
    done = run(cwd, "--base", "HEAD")
    assert done.returncode == 0, done.stderr


def test_a_lost_row_fails_and_names_the_identifier(repo):
    """The mutation the gate exists for: a row silently disappears."""
    cwd, tsv = repo
    tsv.write_text("identifier\trequested_label\nhabitatmech:A\ta\n", encoding="utf-8")
    done = run(cwd, "--base", "HEAD")
    assert done.returncode == 1, done.stdout
    assert "habitatmech:B" in done.stderr, done.stderr


def test_an_edited_row_is_invisible(repo):
    """Identity, not content. Reworded notes and re-decided rows are the
    everyday case and must not trip a gate about disappearance."""
    cwd, tsv = repo
    tsv.write_text("identifier\trequested_label\nhabitatmech:A\tCHANGED\nhabitatmech:B\tb\n",
                   encoding="utf-8")
    assert run(cwd, "--base", "HEAD").returncode == 0


def test_a_deleted_file_is_a_loss(repo):
    cwd, tsv = repo
    tsv.unlink()
    done = run(cwd, "--base", "HEAD")
    assert done.returncode == 1
    assert "missing from the working tree" in done.stderr, done.stderr


def test_allow_loss_reports_but_does_not_fail(repo):
    """A curator removing a row deliberately needs an exit that is not a wall."""
    cwd, tsv = repo
    tsv.write_text("identifier\trequested_label\nhabitatmech:A\ta\n", encoding="utf-8")
    done = run(cwd, "--allow-loss", "--base", "HEAD")
    assert done.returncode == 0
    assert "habitatmech:B" in done.stderr, done.stderr


def test_an_unresolvable_base_is_reported_not_silently_clean(repo):
    """Absent evidence is unknown, not clean -- the stance the non-habitat
    screen already takes. A base that does not resolve must say so, because a
    gate that silently passes when it cannot run is worse than no gate."""
    cwd, _ = repo
    done = run(cwd, "--base", "refs/heads/no-such-branch")
    assert done.returncode == 0
    assert "not checked" in done.stdout, done.stdout


def test_the_union_of_bases_is_the_floor(repo):
    """The #219 loss was of rows that existed on the branch and never on the
    trunk, so a single-base check reported clean. Both parents of a merge have
    to be honoured."""
    cwd, tsv = repo
    subprocess.run(["git", "checkout", "-q", "-b", "side"], cwd=cwd, check=True)
    tsv.write_text(tsv.read_text() + "habitatmech:ONLY_ON_BRANCH\tx\n", encoding="utf-8")
    subprocess.run(["git", "commit", "-qam", "branch row"], cwd=cwd, check=True)
    # Drop the branch-only row while keeping everything main ever had.
    tsv.write_text("identifier\trequested_label\nhabitatmech:A\ta\nhabitatmech:B\tb\n",
                   encoding="utf-8")

    against_trunk = run(cwd, "--base", "main")
    assert against_trunk.returncode == 0, "main alone cannot see a branch-only row"

    done = run(cwd, "--base", "main", "--base", "HEAD")
    assert done.returncode == 1, done.stdout
    assert "habitatmech:ONLY_ON_BRANCH" in done.stderr, done.stderr
