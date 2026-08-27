"""Curation decisions: the validation that stops a wrong term reaching a record.

A curator writing `UBERON:0001988` has to be checked. A plausible-looking but
wrong CURIE is indistinguishable from a right one once it is in the output, and
these decisions are exactly where an LLM-assisted pass would introduce one. So
the tests that matter here are the ones proving the validator *rejects* things.
"""

from __future__ import annotations

import pytest

from habitatmech.curate.decisions import (
    Decision,
    DecisionError,
    load_decisions,
    validate_decisions,
)

ONTOLOGY = {"UBERON:0001988": "feces", "ENVO:00000051": "hot spring"}

HEADER = ("identifier\tdecision\tobject_id\tobject_label\tgrounding_status\tcurator\t"
          "date\tnotes\treview_depth\tcategory\trelation\n")
GOOD_NOTE = "Verified against the source path; this is the exact concept."


def _write(tmp_path, *rows):
    path = tmp_path / "decisions.tsv"
    path.write_text(HEADER + "".join("\t".join(r) + "\n" for r in rows), encoding="utf-8")
    return path


def _ground(identifier="habitatmech:GOLD.abcdef0123", object_id="UBERON:0001988",
            label="feces", status="EXACT", curator="tester", date="2026-08-12", notes=GOOD_NOTE,
            depth="ITEM", category="", relation=""):
    return (identifier, "GROUND", object_id, label, status, curator, date, notes,
            depth, category, relation)


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

    from habitatmech.seed import _madin_key, mint

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
           "tester", "2026-08-12", GOOD_NOTE, "CLASS", "", "")
    decision = load_decisions(_write(tmp_path, row))["habitatmech:GOLD.abcdef0123"]
    assert decision.review_depth == "CLASS"
    assert decision.counts_as_reviewed is False


def test_review_depth_defaults_to_item(tmp_path):
    decisions = load_decisions(_write(tmp_path, _ground()))
    assert decisions["habitatmech:GOLD.abcdef0123"].counts_as_reviewed is True


def test_a_grounding_cannot_be_class_depth(tmp_path):
    """Grounding a concept to a term asserts an equivalence about that one
    concept; there is no mechanically-checkable class that licenses it."""
    decisions = load_decisions(_write(tmp_path, _ground(depth="CLASS")))
    with pytest.raises(DecisionError, match="cannot be CLASS depth"):
        validate_decisions(decisions, ONTOLOGY)


def test_no_class_swept_concept_has_a_lexical_candidate(repo_root):
    """The class-level sweep's whole claim is that no term matched by any search
    route. If a swept concept turns out to have a candidate, the note on it is
    simply false — which is what happened when the first sweep was applied to
    the proposal file without filtering to the `none` tier, and again when
    vendoring PO put terms in reach that had not been there before.

    This makes the claim self-checking: re-vendoring an ontology, or improving
    the matcher, now fails the suite instead of silently invalidating 994 notes.
    """

    from habitatmech.proposals import build_index, classify
    from habitatmech.seed import build_corpus

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

    from habitatmech.curate.decisions import load_decisions
    from habitatmech.seed import _madin_key, mint

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

    from habitatmech.sampling import DEFAULT_SEED, population, select

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

    from habitatmech.seed import mint

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

    from habitatmech import report

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


def test_no_record_repeats_the_same_curation_event(records):
    """Two class-level sweeps share their rationale verbatim, so a merged record
    fed by two swept concepts published the same paragraph twice with nothing to
    say they were about different concepts — 110 records did. Each event names
    the source concept it decided, which is what makes it distinct."""
    repeated, multi = [], 0
    for _path, doc in records:
        events = [
            (e.get("action"), e.get("curator"), e.get("timestamp"), e.get("changes"))
            for e in (doc.get("curation_history") or [])
            if e.get("action") != "SEEDED_FROM_SOURCES"
        ]
        multi += len(events) > 1
        if len(events) != len(set(events)):
            repeated.append(doc["identifier"])

    assert multi, "no record has two decisions — duplication would be untested"
    assert not repeated, f"{len(repeated)} record(s) repeating an event: {repeated[:5]}"


def test_every_decision_kind_has_a_curation_event_summary(repo_root):
    """A kind added without a summary used to fall through to REVIEW's wording,
    publishing "reviewed and endorsed the seeder's resolution" about a record
    where no such thing happened. It now refuses instead."""

    from habitatmech.curate.decisions import DECISION_KINDS
    from habitatmech.seed import _decision_summary

    for kind in sorted(DECISION_KINDS):
        decision = Decision(
            identifier="habitatmech:GOLD.abcdef0123", decision=kind,
            object_id="ENVO:00000051", object_label="hot spring",
            grounding_status="EXACT" if kind == "GROUND" else "",
            curator="tester", date="2026-08-12", notes=GOOD_NOTE,
        )
        summary = _decision_summary(decision)
        assert summary.strip(), f"{kind} produced an empty summary"
        assert GOOD_NOTE in summary, f"{kind} dropped the curator's reasoning"

    unknown = Decision(
        identifier="habitatmech:GOLD.abcdef0123", decision="INVENTED_KIND",
        object_id="", object_label="", grounding_status="",
        curator="tester", date="2026-08-12", notes=GOOD_NOTE,
    )
    with pytest.raises(SystemExit, match="no curation-event summary"):
        _decision_summary(unknown)


def test_confirm_ungrounded_summary_describes_the_recorded_relation():
    """Published history must not call an xref a broader parent (#167)."""
    from habitatmech.seed import _decision_summary

    def summary(relation):
        return _decision_summary(Decision(
            identifier="habitatmech:GOLD.abcdef0123",
            decision="CONFIRM_UNGROUNDED",
            object_id="NCBITaxon:2864",
            object_label="dinoflagellates",
            grounding_status="",
            curator="tester",
            date="2026-08-12",
            notes=GOOD_NOTE,
            relation=relation,
        ))

    assert "kept as an xref" in summary("xref")
    assert "attached as a parent" not in summary("xref")
    assert "Nearest broader term" in summary("parent")
    assert "attached as a parent" in summary("parent")


def test_no_swept_concept_is_named_by_its_own_path(repo_root, records):
    """A class-level sweep asserts "no term matched by any search route". Every
    route reads the GOLD leaf alone, so the claim was false for a whole class of
    anatomy where the leaf is a bare adjective — "Hyaline" under Cartilage is
    hyaline cartilage, and searched alone it finds PATO's *transparent*.

    Kept as a gate rather than a one-off cleanup because the population grows:
    a new GOLD path, or a term newly vendored, can refill it, and nothing else
    re-checks a sweep's negative.
    """
    import csv

    from habitatmech import report

    with (repo_root / "curation" / "decisions.tsv").open(newline="", encoding="utf-8") as fh:
        swept = {
            r["identifier"] for r in csv.DictReader(fh, delimiter="\t")
            if (r.get("review_depth") or "ITEM").strip().upper() == "CLASS"
        }
    assert swept, "no class-level sweep decisions found"
    named = report._compound_path_candidates(swept, records)
    assert not named, (
        f"{len(named)} sweep(s) claim no term matched, but their own path names one: "
        f"{[(n[1], n[2], n[3]) for n in named[:5]]}. Read each against its full path."
    )


def test_relation_defaults_to_parent(tmp_path):
    """Decisions written before `relation` existed keep the behaviour they were
    reviewed under, so adding the column cannot silently move 1,700 terms."""
    decisions = load_decisions(_write(tmp_path, _ground()))
    assert decisions["habitatmech:GOLD.abcdef0123"].relation == "parent"


def test_xref_relation_keeps_a_term_without_asserting_is_a(tmp_path):
    """The case that motivated it: a term related to the concept but neither its
    identity nor broader than it. `parent_habitats` means "broader habitats", so
    a parent would publish the same over-claim as a grounding (#99)."""
    row = ("habitatmech:GOLD.abcdef0123", "CONFIRM_UNGROUNDED", "ENVO:00000051",
           "hot spring", "", "tester", "2026-08-12", GOOD_NOTE, "ITEM", "", "xref")
    decisions = load_decisions(_write(tmp_path, row))
    validate_decisions(decisions, ONTOLOGY)
    assert decisions["habitatmech:GOLD.abcdef0123"].relation == "xref"


def test_unknown_relation_is_rejected(tmp_path):
    row = ("habitatmech:GOLD.abcdef0123", "CONFIRM_UNGROUNDED", "ENVO:00000051",
           "hot spring", "", "tester", "2026-08-12", GOOD_NOTE, "ITEM", "", "sibling")
    with pytest.raises(DecisionError, match="relation 'sibling' not in"):
        validate_decisions(load_decisions(_write(tmp_path, row)), ONTOLOGY)


def test_xref_relation_on_a_grounding_is_rejected(tmp_path):
    """GROUND adopts the term as the record's identity, so there is nothing left
    for a relation to weaken — accepting it would let a curator believe they had
    asked for a looser link than they got."""
    with pytest.raises(DecisionError, match="meaningless on GROUND"):
        validate_decisions(load_decisions(_write(tmp_path, _ground(relation="xref"))), ONTOLOGY)


def test_relation_without_an_object_is_rejected(tmp_path):
    row = ("habitatmech:GOLD.abcdef0123", "CONFIRM_UNGROUNDED", "", "", "",
           "tester", "2026-08-12", GOOD_NOTE, "ITEM", "", "xref")
    with pytest.raises(DecisionError, match="no object_id for it to place"):
        validate_decisions(load_decisions(_write(tmp_path, row)), ONTOLOGY)


def test_xref_relation_places_the_term_as_an_xref_not_a_parent(repo_root):
    """End to end through the seeder's own placement, not just the dataclass."""

    from habitatmech.seed import _placement

    def make(relation, object_id="ENVO:00000051"):
        return Decision(identifier="habitatmech:GOLD.abcdef0123",
                        decision="CONFIRM_UNGROUNDED", object_id=object_id,
                        object_label="hot spring", grounding_status="",
                        curator="tester", date="2026-08-12", notes=GOOD_NOTE,
                        relation=relation)

    assert _placement(make("xref")) == {"extra_parents": [], "extra_xrefs": ["ENVO:00000051"]}
    assert _placement(make("parent")) == {"extra_parents": ["ENVO:00000051"], "extra_xrefs": []}
    assert _placement(make("xref", "")) == {"extra_parents": [], "extra_xrefs": []}


def test_every_recorded_sample_is_fully_judged(repo_root):
    """A sample is only an argument if the draw AND the verdicts are on record.
    "We checked 40 and found none wrong" is unfalsifiable without the 40, and a
    blank or unrecognised verdict silently shrinks the denominator — which makes
    the published rate better than the evidence supports."""

    from habitatmech.sampling import recorded_samples, verdict_of

    samples = recorded_samples()
    assert samples, "no recorded samples — the sampling argument rests on nothing"
    for sample in samples:
        assert sample["judged"] == sample["drawn"], (
            f"{sample['file']}: {sample['drawn']} drawn but {sample['judged']} judged — "
            "an unjudged row is a claim with no evidence behind it"
        )
        assert not sample["unparsed"], (
            f"{sample['file']}: {sample['unparsed']} verdict(s) not understood. "
            "Reading 'ok' as a defect once reported a clean slice as 100% wrong."
        )

    assert verdict_of("ok — homonym risk, but PREGO named the CURIE") == "pass"
    assert verdict_of("wrong: the term is an eye structure") == "fail"
    assert verdict_of("probably fine?") is None
    assert verdict_of("") is None


def test_not_applicable_is_never_used_on_an_organism_target(repo_root):
    """NOT_APPLICABLE says the CONCEPT is not a habitat. An organism target says
    only that the TERM is not a place, and those are different claims.

    Conflating them marked 4,920 assertions as non-habitats — Mollusca,
    Porifera, Fungi, Bovinae, Protozoa — while the identical concept was a term
    request for Sponge, Nematoda and Mammals. `Host-associated > Porifera` was
    NOT_APPLICABLE while its own child `Porifera > Sponge` was not (#114).

    A host is where the microbe lives. The right shape is CONFIRM_UNGROUNDED
    with the taxon as an xref, which keeps the upstream link without asserting
    either that the record IS a phylum or that it is not a habitat.
    """
    import collections
    import csv

    from habitatmech import report

    up = collections.defaultdict(list)
    with (repo_root / "data" / "raw" / "ontology_subclass_edges.tsv").open(
        newline="", encoding="utf-8"
    ) as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            up[row["subject"]].append(row["object"])

    offenders, checked = [], 0
    with (repo_root / "curation" / "decisions.tsv").open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            if row["decision"] != "NOT_APPLICABLE":
                continue
            checked += 1
            target = (row.get("object_id") or "").strip()
            if target and report._is_organism(target, up):
                offenders.append((row["identifier"], target, row.get("object_label")))

    assert checked, "no NOT_APPLICABLE decisions — this would pass vacuously"
    assert not offenders, (
        f"{len(offenders)} NOT_APPLICABLE decision(s) target an organism term. A host is a "
        f"habitat; use CONFIRM_UNGROUNDED with relation=xref instead: {offenders[:5]}"
    )


def _same_as(identifier="habitatmech:GOLD.abcdef0123", target="habitatmech:BACDIVE.0123456789",
             relation=""):
    return (identifier, "SAME_AS", target, "some other concept", "", "tester",
            "2026-08-12", GOOD_NOTE, "ITEM", "", relation)


def test_same_as_merges_two_novel_concepts(tmp_path):
    """The gap it closes: merging otherwise only happens when two concepts
    resolve to the same ONTOLOGY term, so two sources naming one habitat that no
    ontology names produced two permanent records (#116)."""
    decisions = load_decisions(_write(tmp_path, _same_as()))
    validate_decisions(decisions, ONTOLOGY)
    assert decisions["habitatmech:GOLD.abcdef0123"].object_id == "habitatmech:BACDIVE.0123456789"


def test_same_as_discards_the_sources_automatic_grounding(tmp_path):
    """The source identity is rejected, so its CLOSE status and predicate must
    not outrank or otherwise describe the minted survivor (#180)."""
    from habitatmech.seed import ConceptStore, OntologyIndex, Resolution, _decided

    decision = load_decisions(_write(tmp_path, _same_as()))[
        "habitatmech:GOLD.abcdef0123"
    ]
    resolved = _decided(
        Resolution(
            "ENVO:01000951",
            "CLOSE",
            mapping_predicate="skos:closeMatch",
            route="gold_leaf_synonym",
        ),
        "habitatmech:GOLD.abcdef0123",
        decision,
    )

    assert resolved.identifier == "habitatmech:BACDIVE.0123456789"
    assert resolved.grounding_status == "UNGROUNDED"
    assert resolved.mapping_predicate is None
    assert resolved.contributes_grounding is False

    def merged_status(source_first):
        store = ConceptStore(OntologyIndex([], []))
        calls = [
            (resolved.grounding_status, resolved.contributes_grounding),
            ("NOT_APPLICABLE", True),
        ]
        if not source_first:
            calls.reverse()
        for status, contributes in calls:
            store.get(
                resolved.identifier,
                "some other concept",
                status,
                contributes_grounding=contributes,
            )
        return store.concepts[resolved.identifier].grounding_status

    assert merged_status(source_first=True) == "NOT_APPLICABLE"
    assert merged_status(source_first=False) == "NOT_APPLICABLE"


def test_same_as_onto_an_ontology_term_is_rejected(tmp_path):
    """That is what GROUND is for, and accepting it here would give two
    different decisions the same effect by two different code paths."""
    with pytest.raises(DecisionError, match="must name another minted"):
        validate_decisions(load_decisions(_write(tmp_path, _same_as(target="ENVO:00000051"))),
                           ONTOLOGY)


def test_same_as_itself_is_rejected(tmp_path):
    with pytest.raises(DecisionError, match="names itself"):
        validate_decisions(
            load_decisions(_write(tmp_path, _same_as(target="habitatmech:GOLD.abcdef0123"))),
            ONTOLOGY,
        )


def test_relation_on_same_as_is_rejected(tmp_path):
    """The target IS the record's identity, so there is nothing beside it for a
    relation to place."""
    with pytest.raises(DecisionError, match="meaningless on SAME_AS"):
        validate_decisions(load_decisions(_write(tmp_path, _same_as(relation="xref"))), ONTOLOGY)


def test_same_as_chains_resolve_to_the_end(tmp_path):
    """Three sources naming one concept means two SAME_AS rows. Requiring both
    to point at the same winner would make the second decision depend on the
    first having been written first."""
    from habitatmech.curate.decisions import resolve_same_as

    rows = (
        _same_as("habitatmech:GOLD.aaaaaaaaaa", "habitatmech:GOLD.bbbbbbbbbb"),
        _same_as("habitatmech:GOLD.bbbbbbbbbb", "habitatmech:GOLD.cccccccccc"),
    )
    resolved = resolve_same_as(load_decisions(_write(tmp_path, *rows)))
    assert resolved["habitatmech:GOLD.aaaaaaaaaa"] == "habitatmech:GOLD.cccccccccc"
    assert resolved["habitatmech:GOLD.bbbbbbbbbb"] == "habitatmech:GOLD.cccccccccc"


def test_same_as_cycles_are_rejected(tmp_path):
    """A -> B -> A has no answer, and picking one silently would make the corpus
    depend on dict ordering."""
    from habitatmech.curate.decisions import resolve_same_as

    rows = (
        _same_as("habitatmech:GOLD.aaaaaaaaaa", "habitatmech:GOLD.bbbbbbbbbb"),
        _same_as("habitatmech:GOLD.bbbbbbbbbb", "habitatmech:GOLD.aaaaaaaaaa"),
    )
    with pytest.raises(DecisionError, match="SAME_AS cycle"):
        resolve_same_as(load_decisions(_write(tmp_path, *rows)))


def test_a_merged_record_keeps_every_source_attestation(records):
    """Merging must not lose evidence. The human record is the case: 40,432 GOLD
    organisms and 11,697 BacDive strains for one habitat, which read as two
    separate records until #116."""
    merged = [
        doc for _path, doc in records
        if doc.get("identifier", "").startswith("habitatmech:")
        and len({a["source"] for a in doc.get("source_attestations") or []}) > 1
    ]
    assert merged, "no minted record merges two sources — SAME_AS is not exercised"
    for doc in merged:
        attestations = doc.get("source_attestations") or []
        sources = {a["source"] for a in attestations}
        # Merging pools evidence rather than replacing it: both sources are
        # still named, and each keeps its own count so a reader can still see
        # where the number came from.
        assert len(sources) >= 2, f"{doc['identifier']}: merged but only {sources}"
        assert all((a.get("assertion_count") or 0) > 0 for a in attestations), (
            f"{doc['identifier']}: an attestation lost its count in the merge"
        )


def test_environmental_provenance_bins_merge_without_losing_scope(records):
    """GOLD and BacDive use one level-1 provenance concept; publishing two
    records split 19,739 assertions and invited conflicting definitions (#179)."""
    docs = {doc["identifier"]: doc for _path, doc in records}
    survivor = docs["habitatmech:BACDIVE.0f1e92a02c"]

    assert "habitatmech:GOLD.c3fa7fc4c2" not in docs
    assert survivor["label"] == "free-living environment"
    assert survivor["definition_source"] == "HabitatMech"
    assert "ENVO:01000254" in survivor.get("parent_habitats", [])
    assert "ENVO:01000951" in survivor.get("xrefs", [])
    attestations = {
        (attestation["source"], attestation["assertion_unit"]):
        attestation["assertion_count"]
        for attestation in survivor["source_attestations"]
    }
    assert attestations == {("BACDIVE", "STRAIN"): 18454, ("GOLD", "ORGANISM"): 1285}
    assert survivor.get("characteristic_taxa"), "BacDive taxa were lost in the merge"
    history = " ".join(event["changes"] for event in survivor["curation_history"])
    assert "BacDive's Paddy" not in history
    assert "Paddy-Ricefield" not in history


def test_saline_or_alkaline_sources_merge_under_the_reviewed_genus(records):
    """The source labels name an inland aquatic environment, not a bare
    quality; the curated genus replaces GOLD's false biome inheritance (#185)."""
    docs = {doc["identifier"]: doc for _path, doc in records}
    survivor = docs["habitatmech:GOLD.ce244e62cd"]

    assert "habitatmech:BACDIVE.9a0a53afc1" not in docs
    assert survivor["label"] == "inland saline or alkaline aquatic environment"
    assert survivor["habitat_category"] == "AQUATIC"
    assert survivor["grounding_status"] == "UNGROUNDED"
    assert survivor["mapping_status"] == "REVIEWED"
    assert survivor["definition_source"] == "HabitatMech"
    assert survivor.get("parent_habitats") == ["ENVO:01000317"]
    assert "PATO:0001430" not in survivor.get("xrefs", [])

    attestations = {
        (attestation["source"], attestation["assertion_unit"]):
        attestation["assertion_count"]
        for attestation in survivor["source_attestations"]
    }
    assert attestations == {("BACDIVE", "STRAIN"): 37, ("GOLD", "ORGANISM"): 121}
    bacdive = next(
        attestation for attestation in survivor["source_attestations"]
        if attestation["source"] == "BACDIVE"
    )
    assert "curated decision deliberately does not carry" in bacdive["notes"]
    assert any(
        taxon["source"] == "BACDIVE"
        for taxon in survivor.get("characteristic_taxa", [])
    ), "BacDive taxa were lost in the merge"
    history = " ".join(event["changes"] for event in survivor["curation_history"])
    assert "a quality, not a place" not in history
    assert "a quality is a property" not in history


def test_bacdive_attestations_never_claim_an_empty_xref_was_kept(records):
    """A curation override must describe the automatic target, not interpolate
    the final resolution's intentionally empty xref list (#186)."""
    for _path, doc in records:
        for attestation in doc.get("source_attestations", []):
            if attestation.get("source") == "BACDIVE":
                assert "ontology ()" not in attestation.get("notes", ""), doc["identifier"]


def test_rodentia_other_is_a_residual_host_bucket_not_a_term_request(records):
    """The BacDive partition is a real host habitat but an unstable ontology
    class; its Muridae sibling must remain a separate record (#192)."""
    from scripts import build_term_requests

    docs = {doc["identifier"]: doc for _path, doc in records}
    rodentia = docs["habitatmech:BACDIVE.745e245512"]

    assert rodentia["habitat_category"] == "HOST_ASSOCIATED"
    assert rodentia["grounding_status"] == "UNGROUNDED"
    assert rodentia["mapping_status"] == "REVIEWED"
    assert rodentia.get("parent_habitats") == ["ENVO:01001002"]
    assert "NCIT:C17649" not in rodentia.get("xrefs", [])
    assert rodentia["source_attestations"][0]["assertion_count"] == 97
    assert rodentia.get("characteristic_taxa")
    # The Muridae sibling must stay a SEPARATE record. The two BacDive buckets
    # are disjoint by construction — `Rodentia (Other)` means rodent hosts NOT
    # assigned to the Muridae sibling — so merging them would erase the
    # family-rank boundary the source draws. That reason is why this assertion
    # exists, and unlike the sibling's grounding status it does not expire:
    # #194 has since curated Muridae-Mouse/Rat into murid-associated
    # environment, and the two records are still disjoint (#201).
    assert "habitatmech:BACDIVE.ab17ecb10f" in docs

    excluded = build_term_requests.excluded()
    assert "habitatmech:BACDIVE.745e245512" in excluded
    pending = {identifier for _count, _label, identifier in build_term_requests.unrequested(
        build_term_requests.load_corpus(),
        {row["identifier"] for row in build_term_requests.load_requests()},
        {},
    )}
    assert "habitatmech:BACDIVE.745e245512" not in pending


HOST_TAXON_FAMILY = {
    "habitatmech:BACDIVE.33fde10528": ("canid-associated environment", "NCBITaxon:9608", 344),
    "habitatmech:BACDIVE.e6b73de092": ("felid-associated environment", "NCBITaxon:9681", 95),
    "habitatmech:BACDIVE.ab17ecb10f": ("murid-associated environment", "NCBITaxon:10114", 325),
}


def test_dog_cat_and_mouse_rat_are_habitats_with_the_taxon_only_as_an_xref(records):
    """The last members of #114's family, reached by #194.

    All three said `NOT_APPLICABLE` — the schema's "the source concept is not a
    habitat" — over 764 strains, on the host-taxon reasoning #114 reversed for
    their bovine, caprine, equid, leporid and suid siblings. Dog and Cat had no
    decision row at all; Mouse/Rat's `REVIEW` discussed only xref narrowness and
    ratified the status as a side effect.

    The xref assertion is the one that matters most: `_placement` builds a fresh
    Resolution for `CONFIRM_UNGROUNDED` and does not carry `default.extra_xrefs`
    forward, so the organism term survives only because the decision names it.
    CLAUDE.md requires exactly that — the taxon stays an xref and never becomes
    the identity.
    """
    docs = {doc["identifier"]: doc for _path, doc in records}

    for identifier, (label, taxon, strains) in HOST_TAXON_FAMILY.items():
        doc = docs[identifier]
        assert doc["label"] == label
        assert doc["grounding_status"] == "UNGROUNDED", (
            f"{label} still claims it is not a habitat")
        assert doc["mapping_status"] == "REVIEWED"
        assert doc["habitat_category"] == "HOST_ASSOCIATED"
        assert doc.get("parent_habitats") == ["ENVO:01001002"]
        assert doc.get("xrefs") == [taxon], (
            f"{label} lost the organism term; CONFIRM_UNGROUNDED drops the "
            "automatic xref unless the decision names it")
        assert taxon not in (doc.get("parent_habitats") or []), (
            "a taxon is a class of organisms, not a broader habitat")
        assert sum(a.get("assertion_count") or 0
                   for a in doc["source_attestations"]) == strains
        assert doc["definition_source"] == "HabitatMech"


def test_no_record_calls_an_animal_host_a_non_habitat(records):
    """The class-level form of #194, so the next one cannot land silently.

    A record whose only ontology link is an NCBITaxon term and whose status is
    NOT_APPLICABLE is the exact shape all four defects had: the seeder's
    automatic non-habitat-target route fired and nothing curated it afterwards.
    """
    offenders = [
        doc["label"] for _path, doc in records
        if doc.get("grounding_status") == "NOT_APPLICABLE"
        and any(x.startswith("NCBITaxon:") for x in (doc.get("xrefs") or []))
    ]
    assert not offenders, (
        f"{len(offenders)} record(s) assert a taxon-linked concept is not a "
        f"habitat: {offenders[:5]} (#114, #194)")


def test_animal_host_parentage_and_category_agree(records):
    """Claiming ENVO:01001002 as parent IS the claim that a living animal host
    defines the habitat, so the category cannot say otherwise.

    Five domestic-mammal records disagreed for 2,038 strains — bovine, suid,
    caprine, equid and leporid — because #114 left the `category` column blank
    and the seeder's default stood. No data was wrong; the site's own
    host-associated filter silently omitted the cow, the pig, the goat, the
    horse and the rabbit (#200).

    Asserted over the parent rather than over a list of identifiers, so the next
    record to join the family is covered without editing this test.
    """
    off = [
        (doc["label"], doc.get("habitat_category"))
        for _path, doc in records
        if "ENVO:01001002" in (doc.get("parent_habitats") or [])
        and doc.get("habitat_category") != "HOST_ASSOCIATED"
    ]
    assert not off, (
        f"{len(off)} record(s) claim an animal host as parent but are filed "
        f"elsewhere: {off[:5]}")


def test_decomposing_algae_is_a_material_not_a_host(records):
    """Judged apart from the three animal hosts, deliberately.

    The algae are dead, so `HOST_ASSOCIATED` — "defined by a living host" — does
    not apply and no <clade>-associated term is requested. `NOT_APPLICABLE` was
    still wrong: decomposing algal material is a place microbes live. The
    over-narrow `NCBITaxon:2836` claim #43 reported upstream is dropped rather
    than carried onto the record (#194).
    """
    docs = {doc["identifier"]: doc for _path, doc in records}
    doc = docs["habitatmech:BACDIVE.dded810572"]

    assert doc["grounding_status"] == "NARROW"
    assert doc.get("parent_habitats") == ["ENVO:01001189"]
    assert doc["habitat_category"] != "HOST_ASSOCIATED"
    assert "NCBITaxon:2836" not in (doc.get("xrefs") or [])
    # Not detritus: its definition requires dead PARTICULATE matter, which a
    # decomposing algal mass is not, so it is not safely broader.
    assert "ENVO:01001103" not in (doc.get("parent_habitats") or [])
    assert doc.get("definition_source") != "HabitatMech", (
        "four strains did not warrant a new term request")


def test_madin_alga_merges_into_the_defined_gold_host_environment(records):
    """Two source vocabularies name the same broad algal-host habitat; merging
    must retain Madin's taxa and its incomparable TAXON count (#183)."""
    docs = {doc["identifier"]: doc for _path, doc in records}
    survivor = docs["habitatmech:GOLD.02383c20a7"]

    assert "habitatmech:MADIN.5eeeec4db2" not in docs
    assert survivor["label"] == "alga-associated environment"
    assert survivor["habitat_category"] == "HOST_ASSOCIATED"
    assert survivor["definition_source"] == "HabitatMech"
    assert "ENVO:01001000" in survivor.get("parent_habitats", [])
    attestations = {
        (attestation["source"], attestation["assertion_unit"]):
        attestation["assertion_count"]
        for attestation in survivor["source_attestations"]
    }
    assert attestations == {("GOLD", "ORGANISM"): 394, ("MADIN", "TAXON"): 88}
    assert any(
        taxon["source"] == "MADIN" for taxon in survivor.get("characteristic_taxa", [])
    ), "Madin taxa were lost in the merge"


def test_termite_paunch_is_not_merged_with_ruminant_rumen(records):
    """A shared English synonym must not erase incompatible anatomy (#170)."""
    docs = {doc["identifier"]: doc for _path, doc in records}

    termite = docs["habitatmech:GOLD.86aef52360"]
    assert termite["label"] == "Paunch/P3 segment"
    assert termite["grounding_status"] == "NARROW"
    assert "UBERON:0001046" in termite.get("parent_habitats", [])
    assert any(
        attestation.get("source_id") == "gold.ecosystem:7159"
        for attestation in termite.get("source_attestations", [])
    )

    rumen = docs["UBERON:0007365"]
    assert "BTO:0001194" not in docs, "duplicate rumen identity returned (#172)"
    assert all(
        synonym.get("synonym_text") != "Paunch/P3 segment"
        for synonym in rumen.get("synonyms", [])
    )
    assert all(
        attestation.get("source_id") != "gold.ecosystem:7159"
        for attestation in rumen.get("source_attestations", [])
    )
    assert {
        attestation.get("source") for attestation in rumen.get("source_attestations", [])
    } >= {"MADIN", "PREGO"}
    assert any(
        attestation.get("source_id") == "BTO:0001194"
        for attestation in rumen.get("source_attestations", [])
    )
    assert rumen.get("characteristic_taxa"), "PREGO rumen taxa were lost in the merge"
