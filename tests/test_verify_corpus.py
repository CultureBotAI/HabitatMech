"""The corpus-reproducibility gate.

Every other check in this repo is internal: schema validation checks a record's
shape, the corpus tests check cross-record invariants, the round-trip test
checks the emit format. None of them notices if a record's *content* stops
matching what data/raw/ produces. This is the check that does, so it needs a
test proving it actually fails on drift rather than passing vacuously.
"""

from __future__ import annotations

import pytest

from scripts import verify_corpus


@pytest.fixture(scope="module")
def corpus_matches() -> int:
    return verify_corpus.main([])


def test_committed_corpus_reproduces_from_data_raw(corpus_matches):
    assert corpus_matches == 0, (
        "data/habitats/ is not what data/raw/ produces. Re-seed with "
        "`just seed-apply --force --prune`, or if the change was intended, make "
        "it in the seeder so it survives the next re-seed."
    )


def test_verifier_fails_on_a_tampered_record(tmp_path, monkeypatch, repo_root):
    """Guard against a vacuous pass. If the comparison silently stopped
    comparing — a swallowed exception, an empty expected set — the test above
    would still pass and the gate would be worthless."""
    habitats = repo_root / "data" / "habitats"
    victim = next(habitats.rglob("*.yaml"))
    original = victim.read_text(encoding="utf-8")
    try:
        victim.write_text(original.replace("label:", "label: TAMPERED", 1), encoding="utf-8")
        assert verify_corpus.main([]) == 1
    finally:
        victim.write_text(original, encoding="utf-8")

    # And the corpus is intact afterwards, so a failure here cannot leave the
    # working tree dirty for the next test.
    assert verify_corpus.main([]) == 0
