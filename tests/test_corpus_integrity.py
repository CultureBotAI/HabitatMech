"""Invariants the whole corpus must hold, independent of the schema.

LinkML validates each record in isolation; nothing there can see that two
records claim the same identifier, or that a `parent_habitats` entry points at
a record that does not exist. Those are the failure modes a bad merge rule
produces, so they are checked here.
"""

from __future__ import annotations

import re
from collections import Counter

import pytest

# Every source that mints keys. PREGO and ENVIRONMENTS_TABLE were absent while
# only GOLD and BacDive minted, so the pattern silently stopped covering them as
# each new source became curatable — keep this in step with mint() callers.
MINTED_PATTERN = re.compile(
    r"^habitatmech:(GOLD|BACDIVE|PREGO|MADIN|ENVIRONMENTS_TABLE)\.[0-9a-f]{10}$"
)
CURIE_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9._-]*:[A-Za-z0-9._-]+$")


def test_identifiers_are_unique(records):
    """One identifier, one file. A duplicate means the merge key leaked — two
    source concepts resolved to the same identifier but landed in separate
    files, so half the attestations are silently missing from each."""
    counts = Counter(doc["identifier"] for _, doc in records)
    duplicates = {ident: n for ident, n in counts.items() if n > 1}
    assert not duplicates, f"duplicate identifiers across files: {duplicates}"


def test_file_paths_are_unique_per_record(records):
    paths = [path for path, _ in records]
    assert len(paths) == len(set(paths))


def test_identifiers_are_well_formed_curies(records):
    bad = [doc["identifier"] for _, doc in records if not CURIE_PATTERN.match(doc["identifier"])]
    assert not bad, f"malformed identifiers: {bad[:10]}"


def test_minted_identifiers_follow_the_minting_scheme(records):
    """A minted id must be recognisably minted. If a record carries a
    `habitatmech:` id in some other shape, something built an identifier
    outside `mint()` and its stability across re-seeds is not guaranteed."""
    bad = [
        doc["identifier"]
        for _, doc in records
        if doc["identifier"].startswith("habitatmech:") and not MINTED_PATTERN.match(doc["identifier"])
    ]
    assert not bad, f"minted identifiers not matching the scheme: {bad[:10]}"


def test_no_record_is_its_own_parent(records):
    bad = [
        doc["identifier"]
        for _, doc in records
        if doc["identifier"] in (doc.get("parent_habitats") or [])
    ]
    assert not bad, f"records listing themselves as a parent: {bad[:10]}"


def test_minted_records_are_never_grounding_exact(records):
    """A minted identifier exists precisely because no ontology term fit. If
    one is also marked EXACT the two fields contradict each other and the
    grounding statistics in `just report` are wrong."""
    bad = [
        doc["identifier"]
        for _, doc in records
        if doc["identifier"].startswith("habitatmech:") and doc.get("grounding_status") == "EXACT"
    ]
    assert not bad, f"minted identifiers claiming EXACT grounding: {bad[:10]}"


def test_ontology_grounded_records_are_never_ungrounded(records):
    bad = [
        doc["identifier"]
        for _, doc in records
        if not doc["identifier"].startswith("habitatmech:")
        and doc.get("grounding_status") == "UNGROUNDED"
    ]
    assert not bad, f"ontology-identified records marked UNGROUNDED: {bad[:10]}"


def test_every_record_has_at_least_one_attestation(records):
    """A record with no attestation has no reason to exist — nothing upstream
    asserts the habitat and no curator proposed it."""
    bad = [doc["identifier"] for _, doc in records if not (doc.get("source_attestations") or [])]
    assert not bad, f"records with no source_attestations: {bad[:10]}"


def test_assertion_counts_carry_their_unit(records):
    """`assertion_count` without `assertion_unit` is an uninterpretable number:
    GOLD counts organisms, BacDive counts strains, PREGO counts taxa, and they
    are not summable."""
    bad = []
    for _, doc in records:
        for attestation in doc.get("source_attestations") or []:
            if attestation.get("assertion_count") and not attestation.get("assertion_unit"):
                bad.append((doc["identifier"], attestation.get("source")))
    assert not bad, f"assertion_count without assertion_unit: {bad[:10]}"


def test_record_lives_in_its_category_directory(records):
    """The directory is derived from habitat_category; if they disagree the
    corpus cannot be browsed by category."""
    bad = [
        (str(path), doc.get("habitat_category"))
        for path, doc in records
        if path.parent.name != (doc.get("habitat_category") or "OTHER").lower()
    ]
    assert not bad, f"records filed under the wrong category directory: {bad[:10]}"


def test_parent_habitats_are_curies(records):
    bad = []
    for _, doc in records:
        for parent in doc.get("parent_habitats") or []:
            if not CURIE_PATTERN.match(parent):
                bad.append((doc["identifier"], parent))
    assert not bad, f"malformed parent CURIEs: {bad[:10]}"


def test_minted_parents_resolve_to_a_record(records):
    """A `habitatmech:` parent must exist in the corpus. Ontology parents
    (ENVO:, UBERON:, ...) may legitimately point outside it — the vendored
    slice does not carry every ancestor's record — but a minted id has no
    meaning anywhere else, so a dangling one is a broken link."""
    known = {doc["identifier"] for _, doc in records}
    dangling = []
    for _, doc in records:
        for parent in doc.get("parent_habitats") or []:
            if parent.startswith("habitatmech:") and parent not in known:
                dangling.append((doc["identifier"], parent))
    assert not dangling, f"minted parents with no record: {dangling[:10]}"


def test_parent_habitats_have_no_cycles(records):
    """`parent_habitats` is assembled from four independent contributors —
    ontology subclass parents, the GOLD parent-path link, the ambiguous-leaf
    rule's `extra_parents`, and the genus of a curated definition in
    `curation/term_requests.tsv` — and none of them can see the others. A cycle
    would hang any consumer that walks the hierarchy. There are none today; this
    keeps it that way."""
    parents = {doc["identifier"]: (doc.get("parent_habitats") or []) for _, doc in records}

    WHITE, GREY, BLACK = 0, 1, 2
    color = dict.fromkeys(parents, WHITE)

    def walk(start: str) -> list[str] | None:
        # Iterative DFS: the corpus is 3300 records deep enough that recursion
        # is a needless risk, and an explicit stack makes the cycle reportable.
        stack: list[tuple[str, list[str]]] = [(start, [])]
        while stack:
            node, path = stack.pop()
            if node == "__POP__":
                color[path[-1]] = BLACK
                continue
            if color[node] == BLACK:
                continue
            color[node] = GREY
            stack.append(("__POP__", path + [node]))
            for parent in parents.get(node, []):
                if parent not in color:
                    continue  # ontology-external parent; outside the corpus
                if color[parent] == GREY:
                    return path + [node, parent]
                if color[parent] == WHITE:
                    stack.append((parent, path + [node]))
        return None

    for identifier in parents:
        if color[identifier] == WHITE:
            cycle = walk(identifier)
            assert cycle is None, f"parent_habitats cycle: {' -> '.join(cycle)}"


def test_characteristic_taxa_are_ncbitaxon(records):
    bad = []
    for _, doc in records:
        for taxon in doc.get("characteristic_taxa") or []:
            if not taxon["taxon_id"].startswith("NCBITaxon:"):
                bad.append((doc["identifier"], taxon["taxon_id"]))
    assert not bad, f"non-NCBITaxon characteristic_taxa: {bad[:10]}"


def test_every_record_file_matches_the_path_lockfile(records, path_lockfile):
    """`data/habitats/PATHS.tsv` is what makes filenames stable across re-seeds.
    A record whose filename disagrees with its lockfile entry means someone
    renamed a file by hand without recording it, and the next `seed-apply` will
    recreate it under the pinned name — leaving two files for one identifier."""
    mismatched = []
    for path, doc in records:
        identifier = doc["identifier"]
        expected = path_lockfile.get(identifier)
        if expected is None:
            mismatched.append((str(path), identifier, "<no lockfile entry>"))
        elif path.stem != expected:
            mismatched.append((str(path), identifier, expected))
    assert not mismatched, (
        "record filenames disagree with PATHS.tsv "
        f"({len(mismatched)}): {mismatched[:5]}. "
        "To rename a record, edit its slug in PATHS.tsv and re-seed."
    )


def test_lockfile_slugs_are_unique_corpus_wide(path_lockfile):
    """Corpus-wide (not per-directory) uniqueness is what lets a record change
    `habitat_category` — and so change directory — without ever colliding at
    its destination."""
    counts = Counter(path_lockfile.values())
    duplicates = {slug: n for slug, n in counts.items() if n > 1}
    assert not duplicates, f"slugs claimed more than once: {duplicates}"


def test_lockfile_has_no_entries_without_a_record(records, path_lockfile):
    """After a full seed the two sets agree exactly. A leftover entry would
    reserve a slug forever for a record that no longer exists."""
    orphans = set(path_lockfile) - {doc["identifier"] for _, doc in records}
    assert not orphans, f"lockfile entries with no record: {sorted(orphans)[:10]}"


def test_lockfile_slugs_cannot_escape_the_corpus_directory(path_lockfile):
    """Slugs become filenames and the lockfile is hand-editable."""
    bad = [s for s in path_lockfile.values() if not re.match(r"^[a-z0-9][a-z0-9_]*$", s)]
    assert not bad, f"unsafe slugs: {bad[:10]}"


def test_reviewed_records_are_backed_by_curation_decisions(records, repo_root):
    """A record can only be REVIEWED because a curator decided every source
    concept feeding it. If one appears without any decision behind it, the
    review status is being set by something other than curation — which is the
    one thing `mapping_status: REVIEWED` is supposed to mean."""
    import csv as _csv

    path = repo_root / "curation" / "decisions.tsv"
    if not path.exists():
        reviewed = [d["identifier"] for _, d in records if d.get("mapping_status") == "REVIEWED"]
        assert not reviewed, "records are REVIEWED but there is no decisions file"
        return

    with path.open(newline="", encoding="utf-8") as fh:
        decided = {r["identifier"] for r in _csv.DictReader(fh, delimiter="\t")}

    # A minted record is REVIEWED iff its own identifier was decided. An
    # ontology-identified record is reviewed via its constituent source
    # concepts, whose minted keys are not the record id — so those are checked
    # by reconstructing the key from each attestation, which is the same thing
    # apply_decision() looks up. Checking only the minted case would leave the
    # 22 grounded REVIEWED records unverified, which is most of the value.

    from habitatmech.seed import mint

    def keys_for(doc: dict) -> list[str]:
        out = []
        for attestation in doc.get("source_attestations") or []:
            source = attestation.get("source")
            if source == "GOLD" and attestation.get("source_path"):
                out.append(mint("GOLD", attestation["source_path"]))
            elif source in ("BACDIVE", "PREGO") and attestation.get("source_id"):
                out.append(mint(source, attestation["source_id"]))
        return out

    orphans = []
    for _, doc in records:
        if doc.get("mapping_status") != "REVIEWED":
            continue
        if doc["identifier"].startswith("habitatmech:"):
            if doc["identifier"] not in decided:
                orphans.append((doc["identifier"], "own identifier not decided"))
            continue
        undecided = [k for k in keys_for(doc) if k not in decided]
        if undecided:
            orphans.append((doc["identifier"], f"{len(undecided)} source concept(s) undecided"))
    assert not orphans, f"REVIEWED with no decision behind it: {orphans[:10]}"


def test_not_applicable_records_are_all_curated(records, repo_root):
    """NOT_APPLICABLE is a judgement that a source concept is not a habitat.
    The seeder makes it automatically in exactly one case (an upstream mapping
    to a non-habitat ontology, kept as an xref); every other one must come from
    a decision, or something is quietly reclassifying records."""
    import csv as _csv

    path = repo_root / "curation" / "decisions.tsv"
    decided = set()
    if path.exists():
        with path.open(newline="", encoding="utf-8") as fh:
            decided = {r["identifier"] for r in _csv.DictReader(fh, delimiter="\t")}

    unexplained = [
        doc["identifier"]
        for _, doc in records
        if doc.get("grounding_status") == "NOT_APPLICABLE"
        and doc["identifier"] not in decided
        and not (doc.get("xrefs") or [])
    ]
    assert not unexplained, (
        "NOT_APPLICABLE with neither a curation decision nor an upstream xref "
        f"to justify it: {unexplained[:10]}"
    )


def test_seeded_records_carry_a_curation_event(records):
    bad = [doc["identifier"] for _, doc in records if not (doc.get("curation_history") or [])]
    assert not bad, f"records with no curation_history: {bad[:10]}"


def test_causal_edges_all_carry_evidence(records):
    """The schema requires it, but the schema is only enforced at write time;
    a hand-edited record could slip through. Mechanism claims are the one thing
    in this repo that nothing upstream vouches for."""
    bad = []
    for _, doc in records:
        for graph in doc.get("causal_graphs") or []:
            for edge in graph.get("edges") or []:
                if not (edge.get("evidence") or []):
                    bad.append((doc["identifier"], graph.get("graph_id"), edge.get("predicate")))
    assert not bad, f"causal edges without evidence: {bad[:10]}"


def test_causal_edges_reference_declared_nodes(records):
    bad = []
    for _, doc in records:
        for graph in doc.get("causal_graphs") or []:
            node_ids = {n["node_id"] for n in graph.get("nodes") or []}
            for edge in graph.get("edges") or []:
                for end in ("subject", "object"):
                    if edge.get(end) not in node_ids:
                        bad.append((doc["identifier"], graph.get("graph_id"), edge.get(end)))
    assert not bad, f"causal edges pointing at undeclared nodes: {bad[:10]}"


def test_taxon_rank_always_carries_its_candidate_pool(records):
    """`rank` without `candidate_pool` is the misreading #8 was about: "rank 1"
    out of 8,715 near-tied taxa and "rank 1" out of twelve look identical on the
    page, and only the second is much of a claim."""
    bad = []
    for _, doc in records:
        for taxon in doc.get("characteristic_taxa") or []:
            if taxon.get("rank") and not taxon.get("candidate_pool"):
                bad.append((doc["identifier"], taxon["taxon_id"]))
    assert not bad, f"rank without candidate_pool: {bad[:10]}"


def test_corroboration_never_names_the_asserting_source(records):
    """`corroborated_by` is for *other* sources. A source listed as corroborating
    its own assertion would inflate the one signal in this field that is
    genuinely independent evidence."""
    bad = []
    for _, doc in records:
        for taxon in doc.get("characteristic_taxa") or []:
            if taxon.get("source") in (taxon.get("corroborated_by") or []):
                bad.append((doc["identifier"], taxon["taxon_id"], taxon["source"]))
    assert not bad, f"taxa corroborated by their own source: {bad[:10]}"


def test_corroborated_taxa_are_listed_first(records):
    """Cross-source agreement outranks any single source's position, so the
    corroborated entries have to be the ones a reader sees first."""
    bad = []
    for _, doc in records:
        taxa = doc.get("characteristic_taxa") or []
        depths = [len(t.get("corroborated_by") or []) for t in taxa]
        if depths != sorted(depths, reverse=True):
            bad.append(doc["identifier"])
    assert not bad, f"corroborated taxa not listed first: {bad[:10]}"


def test_coverage_over_ontologies_partitions_the_corpus(repo_root, records):
    """HabitatMech's headline claim is how much it holds that ENVO does not, so
    the arithmetic behind it has to be a partition — every record in exactly one
    bucket. A double-counted record inflates the contribution; a dropped one
    understates it, and neither is visible in a percentage.
    """

    from habitatmech.report import COVERAGE_KINDS, _coverage_over_ontologies

    kinds, assertions = _coverage_over_ontologies(records)
    assert set(kinds) <= {key for key, _ in COVERAGE_KINDS}, (
        f"a bucket exists that COVERAGE_KINDS does not describe, so the site "
        f"would silently omit it: {set(kinds) - {k for k, _ in COVERAGE_KINDS}}"
    )
    assert sum(kinds.values()) == len(records), (
        f"buckets hold {sum(kinds.values())} of {len(records)} records — not a partition"
    )

    corpus_assertions = sum(
        a.get("assertion_count") or 0
        for _p, doc in records
        for a in (doc.get("source_attestations") or [])
    )
    assert sum(assertions.values()) == corpus_assertions

    # A record with an ENVO identity is covered; one that merely hangs under an
    # ENVO term is not, because the ambiguous-leaf rule mints an identifier
    # exactly when the matched term is BROADER than the concept. Counting those
    # as covered would understate the contribution by hundreds of records.
    envo_identities = sum(
        1 for _p, doc in records if doc.get("identifier", "").startswith("ENVO:")
    )
    assert kinds["named_by_envo"] == envo_identities


def test_no_record_is_counted_as_covered_by_a_term_it_only_hangs_under(repo_root, records):
    """The distinction the headline number rests on, asserted directly."""

    from habitatmech.report import _coverage_over_ontologies

    kinds, _ = _coverage_over_ontologies(records)
    minted_under_envo = [
        doc["identifier"]
        for _p, doc in records
        if doc.get("identifier", "").startswith("habitatmech:")
        and any(p.startswith("ENVO:") for p in (doc.get("parent_habitats") or []))
    ]
    assert minted_under_envo, "no minted record hangs under an ENVO term — check the fixture"
    assert kinds["refines_envo"] == len(minted_under_envo)
    assert kinds["named_by_envo"] + kinds["named_by_other_obo"] < len(records)


def test_triad_evidence_ranks_by_studies_not_samples(repo_root, records):
    """The ranking's whole value is that it counts independent studies.

    Of 140 GOLD paths where every biosample agrees on a triad, 122 are one study
    repeating itself. `Environmental > Air > Indoor Air > Dust` is unanimous
    across 116 samples for `sports facility` — a fact about one study of a
    sports centre, not about indoor dust. A screen ranked by sample count puts
    exactly that case first and calls it the strongest evidence in the corpus.

    So this asserts the ordering is by corroborating studies, and that a
    single-study path can never outrank a multi-study one however many samples
    it has.
    """
    import csv

    from habitatmech import report

    ranked = report._triad_evidence(records)
    if not ranked:
        pytest.skip("no GOLD triad inventory present")

    corroborated = [row[0] for row in ranked]
    assert corroborated == sorted(corroborated, reverse=True), (
        "ranking is not ordered by corroborated slots first"
    )

    # A slot only counts as corroborated when 2+ studies assert the same term.
    triads = repo_root / "data" / "raw" / "gold_path_triads.tsv"
    with triads.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    single_study_unanimous = [
        r for r in rows
        if r["distinct_terms"] == "1" and int(r["studies_agreeing"]) < 2
    ]
    assert single_study_unanimous, (
        "no single-study unanimous slot in the inventory — the case this "
        "ranking exists to demote is absent, so the test proves nothing"
    )
    top = [r for r in ranked if r[0] > 0]
    assert top, "nothing is corroborated by 2+ studies; the screen would be empty"


def test_triad_inventory_records_study_counts(repo_root):
    """Without `studies_agreeing` the inventory cannot distinguish agreement
    from repetition, and every consumer of it would have to re-derive that from
    the 39 MB per-biosample file that is deliberately not committed."""
    import csv

    triads = repo_root / "data" / "raw" / "gold_path_triads.tsv"
    if not triads.exists():
        pytest.skip("no GOLD triad inventory present")
    with triads.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        assert "studies_agreeing" in (reader.fieldnames or [])
        assert "studies" in (reader.fieldnames or [])
        for row in reader:
            assert int(row["studies_agreeing"]) <= int(row["studies"]), (
                f"{row['canonical_path']}: more studies agree than exist"
            )


def test_triad_inventory_review_partitions_every_source_slot(repo_root):
    import csv

    from habitatmech import report

    triads = repo_root / "data" / "raw" / "gold_path_triads.tsv"
    with triads.open(newline="", encoding="utf-8") as fh:
        source_rows = list(csv.DictReader(fh, delimiter="\t"))

    review = report._triad_inventory_review()

    def keys(rows):
        return {(row["canonical_path"], row["slot"]) for row in rows}

    source_keys = keys(source_rows)
    partition = [keys(review[kind]) for kind in ("groundable", "missing", "organism")]
    assert not partition[0] & partition[1]
    assert not partition[0] & partition[2]
    assert not partition[1] & partition[2]
    assert set().union(*partition) == source_keys
    assert sum(len(review[kind]) for kind in ("groundable", "missing", "organism")) == len(
        source_rows
    )


def test_triad_inventory_review_surfaces_filtered_and_stale_source_data():
    """Known source defects must remain visible after ranking rejects them."""
    from habitatmech import report

    review = report._triad_inventory_review()
    assert review["missing"], "no out-of-slice annotation was reported"
    assert review["organism"], "no organism-like/taxon-valued annotation was reported"
    assert {
        (row["top_term"], row["top_label"])
        for row in review["organism"]
    } == {("NCBITaxon:662107", "phyllosphere metagenome")}
    rejected = [*review["missing"], *review["organism"]]
    assert len(rejected) == 41
    assert len({row["canonical_path"] for row in rejected}) == 38

    distinct_mismatches = report._distinct_triad_label_mismatches(
        review["label_mismatch"]
    )
    assert len(review["label_mismatch"]) == 11
    assert len(distinct_mismatches) == 4
    mismatches = {
        term: (gold_label, slice_label)
        for term, gold_label, slice_label in distinct_mismatches
    }
    assert mismatches == {
        "ENVO:00000077": ("agricultural feature", "agricultural ecosystem"),
        "ENVO:00000463": ("harbor", "harbour"),
        "ENVO:00002164": ("fossil", "fossil material"),
        "UBERON:0001913": ("milk (mammary secretion)", "milk"),
    }

    missing = {
        (row["top_term"], row["top_label"])
        for row in review["missing"]
    }
    assert ("ENVO:00002002", "obsolete food product") in missing


def test_triad_evidence_only_offers_groundable_terms(repo_root, records):
    """A slot is only evidence if its term could ever become a grounding.

    Two overlapping ways it cannot, both present in the inventory (#130): 41
    slots are absent from the vendored slice, which the seeder's label check
    would refuse, including five prefixes this repo does not vendor and
    `ENVO:00002002 "obsolete food product"`, a deprecated term GOLD still
    annotates live biosamples with. One of those 41 is also taxon-valued:
    `NCBITaxon:662107 "phyllosphere metagenome"` appears as an env_local_scale.

    Every one is filtered out today anyway, because thinly evidenced
    annotations are also the malformed ones. This asserts it as a property
    rather than the luck it was: the inventory must still CONTAIN such slots,
    or the test proves nothing.
    """
    import collections
    import csv

    from habitatmech import report

    triads = repo_root / "data" / "raw" / "gold_path_triads.tsv"
    if not triads.exists():
        pytest.skip("no GOLD triad inventory present")

    slice_terms = report._slice_term_labels()
    parents = collections.defaultdict(list)
    with (repo_root / "data" / "raw" / "ontology_subclass_edges.tsv").open(
        newline="", encoding="utf-8"
    ) as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            parents[row["subject"]].append(row["object"])

    with triads.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    ungroundable = [
        r for r in rows
        if r["top_term"] not in slice_terms
        or report._is_organism(r["top_term"], parents)
    ]
    assert ungroundable, (
        "the inventory contains no ungroundable slot, so this test cannot show "
        "the filter works"
    )

    offered = {
        row["top_term"]
        for _c, _s, _l, _p, _i, slots in report._triad_evidence(records)
        for row in slots.values()
    }
    leaked = [
        t for t in offered
        if t not in slice_terms or report._is_organism(t, parents)
    ]
    assert not leaked, f"ranked slots whose term cannot be grounded: {leaked[:5]}"


def test_no_record_claims_a_process_is_a_habitat(repo_root, records):
    """MIxS rules a process out of the environmental triad in the same sentence
    that rules out organisms and groups of organisms, and CLAUDE.md quotes it.

    Four records carried `ENVO:06105023 biofouling` as a broader habitat — "a
    fouling PROCESS during which biological matter accumulates on a solid
    surface". The concept is the fouling layer, not the fouling (#127).

    Ancestry, never the label: `FOODON:00002645 "food material by process"` is a
    material classified by the process that made it, and a label test flags it.
    Fermented and preserved food are habitats.
    """
    import collections
    import csv

    from habitatmech import report

    parents = collections.defaultdict(list)
    with (repo_root / "data" / "raw" / "ontology_subclass_edges.tsv").open(
        newline="", encoding="utf-8"
    ) as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            parents[row["subject"]].append(row["object"])

    offenders = []
    for _path, doc in records:
        for term in [doc.get("identifier", ""), *(doc.get("parent_habitats") or [])]:
            if term and not term.startswith("habitatmech:") and report._is_process(term, parents):
                offenders.append((doc.get("identifier"), doc.get("label"), term))

    assert not offenders, (
        f"{len(offenders)} record(s) claim a process is a habitat: {offenders[:5]}"
    )
