"""Tests for the seeder's grounding and merge rules.

These pin the decisions that are easy to break silently: minted identifiers
must be stable across runs, the ambiguous-leaf rule must not collapse distinct
habitats onto one ontology term, and an upstream curator's refusal to ground a
BacDive source must not be re-guessed here.
"""

from __future__ import annotations

import seed_from_sources as seed


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
    row = _gold_row("Environmental > Aquatic > Marine > Sediment", "Sediment", 4)

    res = seed.resolve_gold(row, ontology, {}, {"sediment": None})

    assert res.identifier == "ENVO:03000033"
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


def test_attestation_ordering_keeps_unknown_fields():
    """order_attestation reorders for readability; dropping a field it does not
    know about would silently lose curated data."""
    ordered = seed.order_attestation(
        {"source_label": "x", "source": "GOLD", "some_future_field": 1}
    )
    assert list(ordered) == ["source", "source_label", "some_future_field"]
    assert ordered["some_future_field"] == 1
