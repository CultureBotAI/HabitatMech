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
    from seed_from_sources import _madin_key, mint

    # Every source that mints a key. A source added without being listed here
    # makes its decisions look stale, which is the same drift MINTED_PATTERN
    # hit in test_corpus_integrity — keep both in step with mint() callers.
    addressable = (
        {mint("GOLD", r["canonical_path"]) for r in raw_tsv("gold_ecosystem_paths.tsv")}
        | {mint("BACDIVE", r["bacdive_id"]) for r in raw_tsv("bacdive_isolation_sources.tsv")}
        | {mint("PREGO", r["prego_id"]) for r in raw_tsv("prego_habitats.tsv")}
        | {_madin_key(r["madin_id"]) for r in raw_tsv("madin_habitats.tsv")}
        | {mint("ENVIRONMENTS_TABLE", r["env_type"]) for r in raw_tsv("environment_parameters.tsv")}
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


def test_no_class_swept_concept_has_a_lexical_candidate(repo_root):
    """The class-level sweep's whole claim is that no term matched by any search
    route. If a swept concept turns out to have a candidate, the note on it is
    simply false — which is what happened when the first sweep was applied to
    the proposal file without filtering to the `none` tier, and again when
    vendoring PO put terms in reach that had not been there before.

    This makes the claim self-checking: re-vendoring an ontology, or improving
    the matcher, now fails the suite instead of silently invalidating 994 notes.
    """
    import sys

    sys.path.insert(0, str(repo_root / "scripts"))
    from propose_decisions import build_index, classify
    from seed_from_sources import build_corpus

    corpus = build_corpus()
    swept = {
        identifier
        for identifier, decision in load_decisions(
            repo_root / "curation" / "decisions.tsv"
        ).items()
        if decision.review_depth == "CLASS"
    }
    by_label, by_synonym = build_index(corpus.ontology.terms)
    matched = [
        (concept.label, concept.identifier)
        for concept in corpus.concepts
        if concept.identifier in swept and classify(concept.label, by_label, by_synonym)[0] != "none"
    ]
    assert not matched, (
        f"{len(matched)} class-swept concept(s) now have a candidate term, so their "
        f"'no term matched' note is false: {matched[:8]}. Curate them individually "
        "(`just worklist`) rather than leaving the claim standing."
    )


def test_a_category_override_actually_moves_the_record(repo_root, records):
    """`apply_decision` puts the override on the Resolution, but three of the
    five ingest routes only read `res.category` back when it was still None —
    so the override validated, looked live, and did nothing. A minted Madin or
    PREGO identifier gives `infer_category` nothing to read, so the override is
    the only way to fix those at all (#63)."""
    import sys

    sys.path.insert(0, str(repo_root / "scripts"))
    from seed_from_sources import _madin_key, mint

    from habitatmech.curate.decisions import load_decisions

    overrides = {
        d.identifier: d.category
        for d in load_decisions(repo_root / "curation" / "decisions.tsv").values()
        if d.category
    }
    if not overrides:
        return

    def keys_of(attestation: dict) -> list[str]:
        """The minted keys a decision could use to address this attestation."""
        source, source_id = attestation.get("source"), attestation.get("source_id") or ""
        if source == "GOLD" and attestation.get("source_path"):
            return [mint("GOLD", attestation["source_path"])]
        if source == "MADIN":
            return [_madin_key(source_id)]
        if source in ("BACDIVE", "PREGO", "ENVIRONMENTS_TABLE"):
            return [mint(source, source_id)]
        return []

    ignored, seen = [], set()
    for _, doc in records:
        for attestation in doc.get("source_attestations") or []:
            for key in keys_of(attestation):
                if key not in overrides:
                    continue
                seen.add(key)
                if doc.get("habitat_category") != overrides[key]:
                    ignored.append((key, overrides[key], doc.get("habitat_category")))
    assert seen, "no category override could be matched to a record at all"
    assert not ignored, f"category overrides that had no effect: {ignored[:5]}"


def test_the_recorded_sample_is_the_one_the_sampler_draws(repo_root):
    """A rate is a claim about a specific set of records. Selecting by position
    made the draw a function of the whole population, so curating two records
    inside one PR silently invalidated the sample that had just been judged
    (#71). Selection by identifier hash survives the corpus moving; this pins
    that the committed sample is still the one the script produces."""
    import csv
    import sys

    sys.path.insert(0, str(repo_root / "scripts"))
    from sample_groundings import DEFAULT_SEED, population, select

    recorded = repo_root / "curation" / "samples" / f"exact-{DEFAULT_SEED}.tsv"
    if not recorded.exists():
        return
    with recorded.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    drawn = {d["identifier"] for d in select(population("EXACT", False), len(rows), DEFAULT_SEED)}
    on_file = {r["identifier"] for r in rows}
    # Curating a sampled record removes it from the SEEDED population, which is
    # expected and fine — what must not happen is the rest of the draw moving.
    assert on_file - drawn == set() or len(on_file - drawn) < len(on_file) / 4, (
        f"the recorded sample and a fresh draw diverge by {len(on_file - drawn)} of "
        f"{len(on_file)} records; selection is not stable under corpus change"
    )
    assert all(r["verdict"] for r in rows), "recorded sample has unjudged rows"


def test_curation_notes_do_not_cite_evidence_that_does_not_exist(repo_root, raw_tsv):
    """`object_id` and `object_label` are verified; `notes` are prose and were
    verified by nothing — yet they are the only record of WHY a decision was
    made, and they are most of what an LLM-assisted pass produces. A
    plausible-sounding citation is as hard to spot as a plausible-looking CURIE
    was before #39 (#51).

    Three claims a note can make that are checkable against the repo:
    a GOLD path, a term id, and a label quoted next to that id.
    """
    import csv
    import re
    import sys

    sys.path.insert(0, str(repo_root / "scripts"))
    from seed_from_sources import mint

    paths = {
        mint("GOLD", r["canonical_path"]): r["canonical_path"]
        for r in raw_tsv("gold_ecosystem_paths.tsv")
    }
    labels = {r["term_id"]: r["label"] for r in raw_tsv("ontology_terms.tsv")}
    curie = re.compile(r"\b((?:[A-Z][A-Za-z]{1,9}|mesh):(?:C\d+|D\d+|\d{4,}))\b")

    # A term can be real without being in the vendored slice: Madin names its
    # habitats *by* ontology id, and some of those ids are not in kg-microbe's
    # ENVO/FOODON builds, so the record carries them as an xref instead of an
    # identity (#58). A note explaining that decision has to be able to say
    # which term it is talking about. These ids are still checked against
    # committed data — data/raw/ rather than the slice — so this widens what
    # counts as evidence, not whether evidence is required.
    attested = set()
    for name, columns in (("madin_habitats.tsv", ("madin_id",)),
                          ("environment_parameters.tsv", ("term_ids",)),
                          ("isolation_source_groundings.tsv", ("object_id",))):
        for row in raw_tsv(name):
            for column in columns:
                attested.update(curie.findall(row.get(column) or ""))

    invented, wrong_path, wrong_label = [], [], []
    with (repo_root / "curation" / "decisions.tsv").open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            note = row["notes"] or ""

            claimed = re.search(r"\bPath:\s*(.+?)\s*$", note)
            actual = paths.get(row["identifier"])
            if claimed and actual:
                said = claimed.group(1).strip()
                # Either direction is fine: the worklist truncates a long path
                # for display, and a note may continue with prose after it.
                if not (actual.startswith(said) or said.startswith(actual)):
                    wrong_path.append((row["identifier"], said[:60], actual[:60]))

            for found in curie.findall(note):
                if found not in labels and found not in attested:
                    invented.append((row["identifier"], found))
                    continue
                # Either quote character: one note uses double quotes, and a
                # form the check does not recognise is a claim nobody verifies,
                # which is the failure this whole test is about (#78).
                quoted = re.search(
                    re.escape(found) + r"""\s+['"]([^'"]{2,80})['"]""", note
                )
                if not quoted:
                    continue
                if found not in labels:
                    # Attested upstream but unlabelable here, so quoting a label
                    # for it asserts something nobody in this repo can check —
                    # exactly the unverified claim the test exists to catch.
                    wrong_label.append((row["identifier"], found, "no label in the slice"))
                elif quoted.group(1).strip().lower() != labels[found].strip().lower():
                    wrong_label.append((row["identifier"], found, quoted.group(1)))

    assert not invented, f"notes citing a term not in the vendored slice: {invented[:5]}"
    assert not wrong_path, f"notes citing the wrong GOLD path: {wrong_path[:5]}"
    assert not wrong_label, f"notes quoting a label the term does not have: {wrong_label[:5]}"


def test_no_class_sweep_asserts_a_negative_the_slice_now_contradicts(repo_root, records):
    """A class-level sweep asserts "no term in the vendored slice matched this
    label by exact, variant or composed search". That is a claim about the
    SLICE, not the concept, and it decays as the slice grows: vendoring PO (#10)
    and the referenced ancestry (#46) falsified it for 25 swept concepts while
    each still read as a considered judgement (#12, #84).

    Re-tested with `propose_decisions.classify`, the same function the sweep
    used, so the variant logic cannot drift from the claim it verifies. The
    index is built here rather than by `build_index`, which filters to the five
    grounding ontologies — right when proposing a grounding, exactly wrong here,
    since the staleness was CAUSED by vendoring NCIT, mesh and CHEBI. With the
    filtered index this found 0 of 20 known cases."""
    import csv
    import sys

    sys.path.insert(0, str(repo_root / "scripts"))
    import habitat_report as report

    with (repo_root / "curation" / "decisions.tsv").open(newline="", encoding="utf-8") as fh:
        swept = {
            r["identifier"] for r in csv.DictReader(fh, delimiter="\t")
            if (r.get("review_depth") or "ITEM").strip().upper() == "CLASS"
        }
    assert swept, "no class-level sweep decisions found"
    contradicted = report._stale_class_sweeps(swept, records)
    assert not contradicted, (
        f"{len(contradicted)} sweep(s) claim no term matched, but one does now: "
        f"{contradicted[:5]}. Vendoring an ontology invalidates the claim; re-decide them."
    )


def test_decision_dates_are_not_in_the_future(repo_root):
    """`date` is when a human or an assisted pass made the call, and it is the
    only thing distinguishing a decision made before a re-seed from one made
    after it. Nothing read the field back, so a wrong one would sit there.

    Compared against **UTC**, because that is what everything else in the repo
    is stamped in — MANIFEST's `extracted_at` and every `curation_history`
    timestamp end in `Z`. Reading it in local time is what makes a correct row
    look a day ahead: at 21:30 Pacific it is already tomorrow in UTC, and a
    check anchored locally would flag every decision written that evening.

    A day of slack on top, since a curator in UTC+13 writing their own local
    date is a day ahead of UTC and is not wrong either.
    """
    import csv
    import datetime

    today = datetime.datetime.now(datetime.timezone.utc).date()
    limit = today + datetime.timedelta(days=1)
    ahead = []
    with (repo_root / "curation" / "decisions.tsv").open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            raw = (row.get("date") or "").strip()
            if not raw:
                continue
            try:
                when = datetime.date.fromisoformat(raw)
            except ValueError:
                ahead.append((row["identifier"], raw, "not an ISO date"))
                continue
            if when > limit:
                ahead.append((row["identifier"], raw, f"after {limit.isoformat()}"))

    assert not ahead, f"decisions dated in the future: {ahead[:5]}"


def test_a_curated_record_records_who_curated_it(records):
    """A decision that shaped a record has to be visible *in* the record.

    `curation/decisions.tsv` is an input, not a published artifact — the site
    serves the YAML. Before #94 every REVIEWED record's history held one event,
    `curator: seed_from_sources`, which attributed a human's grounding to the
    seeder and gave a reader no way to see who decided it or why.

    Checked as an invariant rather than a count, so it holds as curation grows.
    """
    seed_only, checked = [], 0
    for _path, doc in records:
        if doc.get("mapping_status") != "REVIEWED":
            continue
        checked += 1
        actions = {e.get("action") for e in doc.get("curation_history") or []}
        if actions <= {"SEEDED_FROM_SOURCES"}:
            seed_only.append(doc["identifier"])

    assert checked, "no REVIEWED records — this test would pass vacuously"
    assert not seed_only, (
        f"{len(seed_only)} REVIEWED record(s) whose history names no decision: "
        f"{seed_only[:5]}"
    )


def test_curation_history_is_in_chronological_order(records):
    """The seed event is stamped from the extraction time, which is normally
    *later* than the decisions applied on top of it — so appending in
    construction order showed records being seeded after they were curated."""
    out_of_order, multi = [], 0
    for _path, doc in records:
        stamps = [e.get("timestamp") or "" for e in doc.get("curation_history") or []]
        multi += len(stamps) > 1
        if stamps != sorted(stamps):
            out_of_order.append(doc["identifier"])

    assert multi, "no record has two events — ordering would be untested"
    assert not out_of_order, (
        f"{len(out_of_order)} record(s) with a non-chronological history: "
        f"{out_of_order[:5]}"
    )
