"""Review provenance must survive the repository's squash-and-delete workflow."""

import importlib.util
import os
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def reviews():
    spec = importlib.util.spec_from_file_location("publication_reviews", ROOT / "scripts/record_review.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def git(root, *args, check=True):
    return subprocess.run(["git", "-C", str(root), *args], check=check,
                          capture_output=True, text=True)


def assert_retained_base(root, revision, base):
    ancestor = git(root, "merge-base", "--is-ancestor", revision, base, check=False)
    assert ancestor.returncode in (0, 1), "review or trusted base commit is unavailable"
    if ancestor.returncode == 0:
        return
    ref = f"refs/tags/record-review-base/{revision}"
    tag = git(root, "cat-file", "-t", ref, check=False)
    assert tag.returncode == 0 and tag.stdout.strip() == "tag", f"missing durable annotated {ref}"
    assert git(root, "rev-parse", f"{ref}^{{commit}}").stdout.strip() == revision


def test_saved_review_bases_survive_publication(reviews):
    base = os.environ.get("RECORD_REVIEW_BASE", "origin/main")
    for path in reviews.review_paths(ROOT):
        review = reviews.read_review(ROOT, path)
        assert_retained_base(ROOT, review["source"]["git_revision"], base)


def test_provenance_tag_restores_squashed_review_base(tmp_path, reviews):
    origin = tmp_path / "origin"
    origin.mkdir()
    git(origin, "init", "-b", "main")
    git(origin, "config", "user.name", "Publication fixture")
    git(origin, "config", "user.email", "fixture@example.invalid")
    (origin / "record.yaml").write_text("id: EX:initial\n")
    git(origin, "add", ".")
    git(origin, "commit", "-m", "Initial fixture")
    git(origin, "switch", "-c", "review")
    (origin / "record.yaml").write_text("id: EX:reviewed\n")
    git(origin, "commit", "-am", "Reviewed inputs")
    revision = git(origin, "rev-parse", "HEAD").stdout.strip()
    review = {"source": {"git_revision": revision, "state": "working_tree"}}
    git(origin, "switch", "main")
    git(origin, "merge", "--squash", "review")
    git(origin, "commit", "-m", "Squashed review")
    git(origin, "branch", "-D", "review")
    with pytest.raises(AssertionError, match="missing durable annotated"):
        assert_retained_base(origin, revision, "main")

    fresh = tmp_path / "fresh"
    git(tmp_path, "clone", "--no-local", "--single-branch", "--no-tags",
        "--branch", "main", str(origin), str(fresh))
    assert reviews.source_provenance(fresh, review)["status"] == "unverified"
    tag = f"record-review-base/{revision}"
    git(origin, "tag", "-a", tag, revision, "-m", "Retain immutable review provenance")
    git(fresh, "fetch", "--tags", "origin")
    assert_retained_base(fresh, revision, "main")
    assert reviews.source_provenance(fresh, review)["status"] == "working_tree_attestation"

    # A tag bearing the expected name must not point at a different commit.
    git(fresh, "tag", "-d", tag)
    git(fresh, "config", "user.name", "Publication fixture")
    git(fresh, "config", "user.email", "fixture@example.invalid")
    git(fresh, "tag", "-a", tag, "main", "-m", "Deliberately wrong test target")
    with pytest.raises(AssertionError):
        assert_retained_base(fresh, revision, "main")
