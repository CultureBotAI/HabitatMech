"""Curation decisions: the validation that stops a wrong term reaching a record.

A curator writing `UBERON:0001988` has to be checked. A plausible-looking but
wrong CURIE is indistinguishable from a right one once it is in the output, and
these decisions are exactly where an LLM-assisted pass would introduce one. So
the tests that matter here are the ones proving the validator *rejects* things.
"""

from __future__ import annotations

import pytest

from habitatmech.curate.decisions import (
    DecisionError,
    load_decisions,
    validate_decisions,
)

ONTOLOGY = {"UBERON:0001988": "feces", "ENVO:00000051": "hot spring"}

HEADER = "identifier\tdecision\tobject_id\tobject_label\tgrounding_status\tcurator\tdate\tnotes\n"
GOOD_NOTE = "Verified against the source path; this is the exact concept."


def _write(tmp_path, *rows):
    path = tmp_path / "decisions.tsv"
    path.write_text(HEADER + "".join("\t".join(r) + "\n" for r in rows), encoding="utf-8")
    return path


def _ground(identifier="habitatmech:GOLD.abcdef0123", object_id="UBERON:0001988",
            label="feces", status="EXACT", curator="tester", date="2026-08-12", notes=GOOD_NOTE):
    return (identifier, "GROUND", object_id, label, status, curator, date, notes)


def test_a_valid_grounding_passes(tmp_path):
    decisions = load_decisions(_write(tmp_path, _ground()))
    validate_decisions(decisions, ONTOLOGY)


def test_invented_term_id_is_rejected(tmp_path):
    """The core anti-hallucination case: a CURIE that does not exist."""
    decisions = load_decisions(_write(tmp_path, _ground(object_id="UBERON:9999999")))
    with pytest.raises(DecisionError, match="not in the vendored ontology slice"):
        validate_decisions(decisions, ONTOLOGY)


def test_real_term_with_the_wrong_label_is_rejected(tmp_path):
    """The subtler case: a real CURIE paired with the concept the curator
    *meant*, which is not the concept the CURIE denotes. Without the label
    check this is invisible."""
    decisions = load_decisions(_write(tmp_path, _ground(label="sputum")))
    with pytest.raises(DecisionError, match="is 'feces', not 'sputum'"):
        validate_decisions(decisions, ONTOLOGY)


def test_label_check_is_case_insensitive(tmp_path):
    decisions = load_decisions(_write(tmp_path, _ground(label="Feces")))
    validate_decisions(decisions, ONTOLOGY)


def test_grounding_without_a_label_is_rejected(tmp_path):
    """An empty label would make the anti-hallucination check vacuous."""
    decisions = load_decisions(_write(tmp_path, _ground(label="")))
    with pytest.raises(DecisionError, match="object_label is required"):
        validate_decisions(decisions, ONTOLOGY)


def test_unknown_decision_kind_is_rejected(tmp_path):
    row = ("habitatmech:GOLD.abcdef0123", "PROBABLY_FINE", "", "", "",
           "tester", "2026-08-12", GOOD_NOTE)
    with pytest.raises(DecisionError, match="unknown decision"):
        validate_decisions(load_decisions(_write(tmp_path, row)), ONTOLOGY)


def test_grounding_keyed_on_a_shared_ontology_curie_is_rejected(tmp_path):
    """An ontology CURIE names the merged record, not one source concept, so a
    GROUND keyed there would silently move every concept that resolved to it."""
    decisions = load_decisions(_write(tmp_path, _ground(identifier="ENVO:00000051")))
    with pytest.raises(DecisionError, match="must key on a minted"):
        validate_decisions(decisions, ONTOLOGY)


def test_bad_grounding_status_is_rejected(tmp_path):
    decisions = load_decisions(_write(tmp_path, _ground(status="PROBABLY")))
    with pytest.raises(DecisionError, match="grounding_status"):
        validate_decisions(decisions, ONTOLOGY)


def test_grounding_status_on_a_non_grounding_decision_is_rejected(tmp_path):
    row = ("habitatmech:GOLD.abcdef0123", "NOT_APPLICABLE", "", "", "EXACT",
           "tester", "2026-08-12", GOOD_NOTE)
    with pytest.raises(DecisionError, match="only meaningful for GROUND"):
        validate_decisions(load_decisions(_write(tmp_path, row)), ONTOLOGY)


def test_missing_curator_is_rejected(tmp_path):
    decisions = load_decisions(_write(tmp_path, _ground(curator="")))
    with pytest.raises(DecisionError, match="no curator"):
        validate_decisions(decisions, ONTOLOGY)


def test_bad_date_is_rejected(tmp_path):
    decisions = load_decisions(_write(tmp_path, _ground(date="last tuesday")))
    with pytest.raises(DecisionError, match="not YYYY-MM-DD"):
        validate_decisions(decisions, ONTOLOGY)


def test_a_decision_without_a_reason_is_rejected(tmp_path):
    """A decision with no rationale is not reviewable: the next curator cannot
    tell whether it was considered or guessed."""
    decisions = load_decisions(_write(tmp_path, _ground(notes="looks right")))
    with pytest.raises(DecisionError, match="notes too short"):
        validate_decisions(decisions, ONTOLOGY)


def test_confirm_ungrounded_may_carry_a_broader_parent(tmp_path):
    """CONFIRM_UNGROUNDED can name a nearest-broader term, attached as a parent
    rather than adopted as identity — and it is still label-verified."""
    row = ("habitatmech:GOLD.abcdef0123", "CONFIRM_UNGROUNDED", "ENVO:00000051",
           "hot spring", "", "tester", "2026-08-12", GOOD_NOTE)
    validate_decisions(load_decisions(_write(tmp_path, row)), ONTOLOGY)

    bad = ("habitatmech:GOLD.abcdef0123", "CONFIRM_UNGROUNDED", "ENVO:00000051",
           "cold spring", "", "tester", "2026-08-12", GOOD_NOTE)
    with pytest.raises(DecisionError, match="not 'cold spring'"):
        validate_decisions(load_decisions(_write(tmp_path, bad)), ONTOLOGY)


def test_duplicate_identifier_is_rejected(tmp_path):
    with pytest.raises(DecisionError, match="duplicate decision"):
        load_decisions(_write(tmp_path, _ground(), _ground(status="CLOSE")))


def test_missing_file_is_not_an_error(tmp_path):
    assert load_decisions(tmp_path / "absent.tsv") == {}


def test_every_committed_decision_addresses_a_real_source_concept(repo_root, raw_tsv):
    """A decision keyed on an identifier no source concept produces is dead: it
    never fires, the curator's intent is silently not applied, and the seeder
    only warns on stderr where CI output buries it. This makes it a failure.

    It is also the check that catches an upstream refresh removing a concept a
    decision was written against — the minted key is a content hash, so a
    changed GOLD path yields a different key and the old decision goes stale.
    """
    import sys

    sys.path.insert(0, str(repo_root / "scripts"))
    from seed_from_sources import mint

    addressable = (
        {mint("GOLD", r["canonical_path"]) for r in raw_tsv("gold_ecosystem_paths.tsv")}
        | {mint("BACDIVE", r["bacdive_id"]) for r in raw_tsv("bacdive_isolation_sources.tsv")}
        | {mint("PREGO", r["prego_id"]) for r in raw_tsv("prego_habitats.tsv")}
    )
    decisions = load_decisions(repo_root / "curation" / "decisions.tsv")
    stale = sorted(set(decisions) - addressable)
    assert not stale, (
        f"{len(stale)} decision(s) match no source concept in data/raw/: {stale[:10]}. "
        "Either the identifier is mistyped, or the concept changed upstream and "
        "the decision needs re-targeting."
    )


def test_every_committed_decision_verifies(repo_root, raw_tsv):
    """The real decisions file, checked against the real ontology slice. This is
    what would catch a term that drifted out of the vendored slice after an
    upstream refresh."""
    labels = {t["term_id"]: t["label"] for t in raw_tsv("ontology_terms.tsv")}
    decisions = load_decisions(repo_root / "curation" / "decisions.tsv")
    assert decisions, "no curation decisions on file"
    validate_decisions(decisions, labels)


def test_class_depth_does_not_promote_a_record_to_reviewed(tmp_path):
    """A bulk sweep decides many concepts at once on a mechanically-checkable
    property. That is worth recording, but it is not someone having read the
    habitat — so it must not report the corpus as reviewed."""
    row = ("habitatmech:GOLD.abcdef0123", "CONFIRM_UNGROUNDED", "", "", "",
           "tester", "2026-08-12", GOOD_NOTE, "CLASS")
    path = tmp_path / "decisions.tsv"
    path.write_text(HEADER.rstrip("\n") + "\treview_depth\n" + "\t".join(row) + "\n",
                    encoding="utf-8")
    decision = load_decisions(path)["habitatmech:GOLD.abcdef0123"]
    assert decision.review_depth == "CLASS"
    assert decision.counts_as_reviewed is False


def test_review_depth_defaults_to_item(tmp_path):
    decisions = load_decisions(_write(tmp_path, _ground()))
    assert decisions["habitatmech:GOLD.abcdef0123"].counts_as_reviewed is True


def test_a_grounding_cannot_be_class_depth(tmp_path):
    """Grounding a concept to a term asserts an equivalence about that one
    concept; there is no mechanically-checkable class that licenses it."""
    row = ("habitatmech:GOLD.abcdef0123", "GROUND", "UBERON:0001988", "feces", "EXACT",
           "tester", "2026-08-12", GOOD_NOTE, "CLASS")
    path = tmp_path / "decisions.tsv"
    path.write_text(HEADER.rstrip("\n") + "\treview_depth\n" + "\t".join(row) + "\n",
                    encoding="utf-8")
    with pytest.raises(DecisionError, match="cannot be CLASS depth"):
        validate_decisions(load_decisions(path), ONTOLOGY)
