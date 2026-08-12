"""Invariants the whole corpus must hold, independent of the schema.

LinkML validates each record in isolation; nothing there can see that two
records claim the same identifier, or that a `parent_habitats` entry points at
a record that does not exist. Those are the failure modes a bad merge rule
produces, so they are checked here.
"""

from __future__ import annotations

import re
from collections import Counter

MINTED_PATTERN = re.compile(r"^habitatmech:(GOLD|BACDIVE)\.[0-9a-f]{10}$")
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
    """`parent_habitats` is assembled from three independent contributors —
    ontology subclass parents, the GOLD parent-path link, and the ambiguous-leaf
    rule's `extra_parents` — and none of them can see the others. A cycle would
    hang any consumer that walks the hierarchy. There are none today; this keeps
    it that way."""
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

    # A minted record is REVIEWED iff its own identifier was decided. A merged
    # ontology-identified record is reviewed via its constituents, whose minted
    # keys are not the record id — so only the minted case is checkable here.
    orphans = [
        doc["identifier"]
        for _, doc in records
        if doc.get("mapping_status") == "REVIEWED"
        and doc["identifier"].startswith("habitatmech:")
        and doc["identifier"] not in decided
    ]
    assert not orphans, f"minted records REVIEWED with no decision on file: {orphans[:10]}"


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
