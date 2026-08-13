"""Tests for the seeder's grounding and merge rules.

These pin the decisions that are easy to break silently: minted identifiers
must be stable across runs, the ambiguous-leaf rule must not collapse distinct
habitats onto one ontology term, and an upstream curator's refusal to ground a
BacDive source must not be re-guessed here.
"""

from __future__ import annotations

import pytest
import seed_from_sources as seed

from habitatmech.curate.decisions import Decision


def test_minted_identifiers_are_deterministic():
    """Minted ids are content-hashed so a re-seed after an upstream refresh
    diffs only where the data changed. Sequential numbering would renumber
    every record after an insertion."""
    first = seed.mint("GOLD", "Environmental > Aquatic > Marine > Sediment")
    second = seed.mint("GOLD", "Environmental > Aquatic > Marine > Sediment")
    assert first == second
    assert first.startswith("habitatmech:GOLD.")


def test_minted_identifiers_differ_by_source_kind_and_key():
    assert seed.mint("GOLD", "Soil") != seed.mint("BACDIVE", "Soil")
    assert seed.mint("GOLD", "Soil") != seed.mint("GOLD", "Sand")


def test_norm_label_folds_source_punctuation():
    """GOLD and BacDive spell compound labels with punctuation an ontology
    never uses; without folding, none of them would ever match a term."""
    assert seed.norm_label("Rock-dwelling (endoliths)") == "rock dwelling endoliths"
    assert seed.norm_label("Animal-habitation-Nest,Burrow") == "animal habitation nest burrow"
    assert seed.norm_label("Mammals: Human") == "mammals human"


def test_leaf_claimants_picks_the_shallowest_path():
    rows = [
        {"leaf_label": "Soil", "depth": "3", "canonical_path": "Environmental > Terrestrial > Soil"},
        {"leaf_label": "Soil", "depth": "4", "canonical_path": "Environmental > Terrestrial > Cave > Soil"},
    ]
    claimants = seed.leaf_claimants(rows)
    assert claimants["soil"] == "Environmental > Terrestrial > Soil"


def test_leaf_claimants_refuses_to_break_a_tie():
    """Two paths tied at the shallowest depth have no principled winner —
    "Human > ... > Fecal" and "Birds > ... > Fecal" are both depth 5, and
    neither is what an ontology means by feces. Nobody claims the term."""
    rows = [
        {"leaf_label": "Fecal", "depth": "5",
         "canonical_path": "Host-associated > Mammals: Human > D > L > Fecal"},
        {"leaf_label": "Fecal", "depth": "5",
         "canonical_path": "Host-associated > Birds > D > L > Fecal"},
    ]
    assert seed.leaf_claimants(rows)["fecal"] is None


class _Ontology:
    """Minimal stand-in for OntologyIndex over a handful of terms."""

    def __init__(self, by_label=None, by_synonym=None):
        self.by_label = by_label or {}
        self.by_synonym = by_synonym or {}
        self.terms = {}

    def ancestors(self, _term_id):
        return set()


def _gold_row(path: str, leaf: str, depth: int) -> dict[str, str]:
    levels = path.split(" > ")
    row = {lvl: (levels[i] if i < len(levels) else "") for i, lvl in enumerate(seed.GOLD_LEVELS)}
    row.update({"canonical_path": path, "leaf_label": leaf, "depth": str(depth), "gold_node_ids": ""})
    return row


def test_ambiguous_gold_leaf_becomes_a_narrow_child_not_the_term():
    """The core anti-conflation rule. Marine sediment and freshwater sediment
    are different habitats; grounding both to ENVO:00002007 "sediment" would
    merge them into a single record whose attestations mix the two."""
    ontology = _Ontology(by_label={"sediment": "ENVO:00002007"})
    claimants = {"sediment": "some > other > path"}  # this row is NOT the claimant
    row = _gold_row("Environmental > Aquatic > Marine > Sediment", "Sediment", 4)

    res = seed.resolve_gold(row, ontology, {}, claimants)

    assert res.identifier.startswith("habitatmech:GOLD.")
    assert res.grounding_status == "NARROW"
    assert res.extra_parents == ["ENVO:00002007"]


def test_claimant_gold_leaf_takes_the_term():
    ontology = _Ontology(by_label={"soil": "ENVO:00001998"})
    path = "Environmental > Terrestrial > Soil"
    row = _gold_row(path, "Soil", 3)

    res = seed.resolve_gold(row, ontology, {}, {"soil": path})

    assert res.identifier == "ENVO:00001998"
    assert res.grounding_status == "EXACT"


def test_composed_label_beats_the_leaf():
    """"Marine sediment" is a real ENVO term and a strictly better grounding
    than "sediment", so the two-level composed label is tried first."""
    ontology = _Ontology(by_label={"sediment": "ENVO:00002007", "marine sediment": "ENVO:03000033"})
    path = "Environmental > Aquatic > Marine > Sediment"
    row = _gold_row(path, "Sediment", 4)

    res = seed.resolve_gold(row, ontology, {}, {"sediment": None}, {"marine sediment": path})

    assert res.identifier == "ENVO:03000033"
    assert res.grounding_status == "EXACT"


def test_composed_match_shared_by_settings_does_not_merge():
    """Three GOLD paths compose to "anaerobic sludge" under different reactor
    types. The composed route used to ground all of them to ENVO:00002129 and
    merge three engineered environments into one record (#15)."""
    ontology = _Ontology(by_label={"anaerobic sludge": "ENVO:00002129"})
    path = "Engineered > Bioreactor > MBR (Membrane bioreactor) > Anaerobic > Sludge"
    row = _gold_row(path, "Sludge", 5)

    res = seed.resolve_gold(row, ontology, {}, {"sludge": None}, {"anaerobic sludge": None})

    assert res.identifier.startswith("habitatmech:GOLD.")
    assert res.grounding_status == "NARROW"
    assert res.extra_parents == ["ENVO:00002129"]


def test_composed_match_shared_only_by_host_clade_still_merges():
    """Human, mammal and bird serum all compose to "blood serum". UBERON:0001977
    *is* blood serum whatever the host, and the host lives in the taxon, so
    these merge — the sentinel says every path may claim it."""
    ontology = _Ontology(by_label={"blood serum": "UBERON:0001977"})
    row = _gold_row("Host-associated > Birds > Circulatory system > Blood > Serum", "Serum", 5)

    res = seed.resolve_gold(
        row, ontology, {}, {"serum": None}, {"blood serum": seed.ANY_PATH_MAY_CLAIM}
    )

    assert res.identifier == "UBERON:0001977"
    assert res.grounding_status == "EXACT"


def test_unmatched_gold_path_is_ungrounded_not_forced():
    ontology = _Ontology()
    row = _gold_row("Environmental > Terrestrial > Deep subsurface > Shale carbon reservoir",
                    "Shale carbon reservoir", 4)

    res = seed.resolve_gold(row, ontology, {}, {"shale carbon reservoir": row["canonical_path"]})

    assert res.grounding_status == "UNGROUNDED"
    assert res.identifier.startswith("habitatmech:GOLD.")


def test_bacdive_upstream_refusal_is_honoured():
    """kg-microbe's mapping table has a row for every BacDive source. An empty
    object_id is a curator who looked and declined; re-grounding it here with a
    weaker lexical method would overwrite a human decision with a guess."""
    row = {"bacdive_id": "bacdive.isolation_source:abort", "label": "Abort", "source_slug": "abort"}
    mapping = {"abort": {"object_id": "", "predicate_id": ""}}

    res = seed.resolve_bacdive(row, mapping)

    assert res.grounding_status == "UNGROUNDED"
    assert res.route == "bacdive_declined_upstream"


def test_bacdive_non_habitat_target_is_kept_as_an_xref():
    """"Acidic" maps upstream to PATO:0001429, a quality. A quality is a
    property of a habitat, not a habitat, so the record must not adopt it as
    its identity — but the link is still worth keeping."""
    row = {"bacdive_id": "bacdive.isolation_source:acidic", "label": "Acidic", "source_slug": "acidic"}
    mapping = {"acidic": {"object_id": "PATO:0001429", "predicate_id": "skos:exactMatch"}}

    res = seed.resolve_bacdive(row, mapping)

    assert res.grounding_status == "NOT_APPLICABLE"
    assert res.identifier.startswith("habitatmech:BACDIVE.")
    assert res.extra_xrefs == ["PATO:0001429"]


def test_bacdive_habitat_target_is_adopted():
    row = {"bacdive_id": "bacdive.isolation_source:abdomen", "label": "Abdomen", "source_slug": "abdomen"}
    mapping = {"abdomen": {"object_id": "UBERON:0000916", "predicate_id": "skos:exactMatch"}}

    res = seed.resolve_bacdive(row, mapping)

    assert res.identifier == "UBERON:0000916"
    assert res.grounding_status == "EXACT"


class _Concept:
    """Minimal stand-in for Concept: assign_paths only reads these three."""

    def __init__(self, identifier: str, label: str, category: str):
        self.identifier = identifier
        self.label = label
        self.category = category


def test_lockfile_pins_a_slug_against_a_lower_sorting_newcomer():
    """The bug this lockfile exists for. Without it, the bare slug goes to
    whichever same-slug concept sorts first by identifier, so an upstream
    refresh adding a lower-sorting concept renames the incumbent — a
    delete+add in the diff for a record whose content identity never changed."""
    incumbent = _Concept("ENVO:00002007", "sediment", "AQUATIC")
    _, lock = seed.assign_paths([incumbent])
    assert lock == {"ENVO:00002007": "sediment"}

    newcomer = _Concept("BTO:0000001", "sediment", "TERRESTRIAL")
    corpus = [newcomer, incumbent]

    unpinned, _ = seed.assign_paths(corpus)
    assert unpinned["ENVO:00002007"].name != "sediment.yaml", (
        "guard: without a lockfile the incumbent is expected to lose the slug; "
        "if this stops being true the test no longer covers the bug"
    )

    pinned, _ = seed.assign_paths(corpus, lock)
    assert pinned["ENVO:00002007"].name == "sediment.yaml"
    assert pinned["BTO:0000001"].name.startswith("sediment__")


def test_category_change_moves_the_directory_but_keeps_the_slug():
    """habitat_category is heuristic and expected to improve (#11), so records
    will move between category directories. The filename must survive that."""
    lock = {"ENVO:00002007": "sediment"}
    paths, _ = seed.assign_paths([_Concept("ENVO:00002007", "sediment", "TERRESTRIAL")], lock)
    assert paths["ENVO:00002007"].name == "sediment.yaml"
    assert paths["ENVO:00002007"].parent.name == "terrestrial"


def test_slugs_are_unique_corpus_wide_not_per_directory():
    """Per-directory uniqueness would let a category change collide at the
    destination. Corpus-wide uniqueness makes that impossible."""
    corpus = [
        _Concept("ENVO:00000001", "sediment", "AQUATIC"),
        _Concept("ENVO:00000002", "sediment", "TERRESTRIAL"),
    ]
    _, lock = seed.assign_paths(corpus)
    assert len(set(lock.values())) == 2


def test_lockfile_entries_for_vanished_concepts_are_dropped():
    """The lockfile is rebuilt from the current concept set, so it cannot
    accumulate entries for concepts that no longer exist upstream."""
    stale = {"ENVO:99999999": "gone", "ENVO:00002007": "sediment"}
    _, lock = seed.assign_paths([_Concept("ENVO:00002007", "sediment", "AQUATIC")], stale)
    assert lock == {"ENVO:00002007": "sediment"}


def test_load_lockfile_rejects_a_slug_that_could_escape_the_corpus(tmp_path):
    """The lockfile is hand-editable — that is the rename mechanism — and its
    slugs become filenames, so a path separator must not survive the read."""
    path = tmp_path / "PATHS.tsv"
    path.write_text("identifier\tslug\nENVO:1\t../../etc/passwd\n", encoding="utf-8")
    with pytest.raises(SystemExit, match="unsafe slug"):
        seed.load_lockfile(path)


def test_load_lockfile_rejects_two_identifiers_claiming_one_slug(tmp_path):
    path = tmp_path / "PATHS.tsv"
    path.write_text("identifier\tslug\nENVO:1\tsoil\nENVO:2\tsoil\n", encoding="utf-8")
    with pytest.raises(SystemExit, match="claimed by both"):
        seed.load_lockfile(path)


def test_load_lockfile_is_absent_tolerant(tmp_path):
    """A fresh corpus has no lockfile; the first seed mints every slug."""
    assert seed.load_lockfile(tmp_path / "nope.tsv") == {}


def test_lockfile_round_trips(tmp_path):
    path = tmp_path / "PATHS.tsv"
    original = {"ENVO:00002007": "sediment", "BTO:0000001": "sediment__855ef662"}
    seed.write_lockfile(original, path)
    assert seed.load_lockfile(path) == original


def _ingest_with_decision(source: str, decision):
    """Run one source concept through its ingest with `decision` applied,
    and return the resulting Concept."""
    store = seed.ConceptStore(seed.OntologyIndex([], []))
    routes = seed.Counter()
    if source == "GOLD":
        path = "Environmental > Terrestrial > Soil"
        row = _gold_row(path, "Soil", 3)
        row.update({"organism_count": "1", "gold_node_ids": "gold.ecosystem:1"})
        seed.ingest_gold(store, [row], {}, routes, {seed.mint("GOLD", path): decision})
    elif source == "BACDIVE":
        bid = "bacdive.isolation_source:soil"
        row = {"bacdive_id": bid, "label": "Soil", "source_slug": "soil", "strain_count": "1"}
        seed.ingest_bacdive(store, [row], {}, routes, {seed.mint("BACDIVE", bid): decision})
    else:
        pid = "ENVO:00001998"
        row = {"prego_id": pid, "prego_synonyms": "soil", "taxon_count": "1",
               "max_prego_score": "3", "channels": ""}
        seed.ingest_prego(store, [row], [], routes, {seed.mint("PREGO", pid): decision})
    return next(iter(store.concepts.values()))


@pytest.mark.parametrize("source", ["GOLD", "BACDIVE", "PREGO"])
def test_every_ingest_applies_a_decisions_broader_parent(source):
    """CONFIRM_UNGROUNDED records a nearest-broader term as a parent. An ingest
    that forgets to apply `extra_parents` silently discards the placement the
    curator recorded, and nothing reports it — the decision still counts as
    applied and the seed still passes. That is exactly what #21 was."""
    decision = Decision(
        identifier="k", decision="CONFIRM_UNGROUNDED",
        object_id="ENVO:01001002", object_label="animal-associated environment",
        grounding_status="", curator="t", date="2026-08-12", notes="n" * 30,
    )
    concept = _ingest_with_decision(source, decision)
    assert "ENVO:01001002" in concept.parents, f"{source} ingest dropped extra_parents"


@pytest.mark.parametrize("source", ["GOLD", "BACDIVE", "PREGO"])
def test_every_ingest_applies_a_decisions_xref(source):
    decision = Decision(
        identifier="k", decision="NOT_APPLICABLE",
        object_id="NCBITaxon:9606", object_label="", grounding_status="",
        curator="t", date="2026-08-12", notes="n" * 30,
    )
    concept = _ingest_with_decision(source, decision)
    assert "NCBITaxon:9606" in concept.xrefs, f"{source} ingest dropped extra_xrefs"


@pytest.mark.parametrize("source", ["GOLD", "BACDIVE", "PREGO"])
def test_every_ingest_counts_a_decision_as_a_review(source):
    """The REVIEWED rule depends on every ingest reporting its review votes; an
    ingest that forgot would silently hold records at SEEDED forever."""
    decision = Decision(
        identifier="k", decision="REVIEW", object_id="", object_label="",
        grounding_status="", curator="t", date="2026-08-12", notes="n" * 30,
    )
    concept = _ingest_with_decision(source, decision)
    assert concept.source_concepts == 1
    assert concept.reviewed_sources == 1


def test_attestation_ordering_keeps_unknown_fields():
    """order_attestation reorders for readability; dropping a field it does not
    know about would silently lose curated data."""
    ordered = seed.order_attestation(
        {"source_label": "x", "source": "GOLD", "some_future_field": 1}
    )
    assert list(ordered) == ["source", "source_label", "some_future_field"]
    assert ordered["some_future_field"] == 1
