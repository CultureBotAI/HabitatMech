#!/usr/bin/env python3
"""Seed data/habitats/<category>/<slug>.yaml from the inventories in data/raw/.

This is the harmonization step. Three source vocabularies describe where
microbes live, in three incompatible idioms:

    GOLD     "Environmental > Aquatic > Marine > Sediment"   (5-level path)
    BacDive  "Marine-sediment"                               (flat label)
    PREGO    ENVO:00002113                                   (ontology CURIE)

Each becomes a *source concept*. Every source concept is resolved to an
identifier — an ontology CURIE where one is defensible, otherwise a minted,
content-hashed ``habitatmech:`` CURIE — and source concepts that resolve to the
same identifier are merged into one HabitatRecord carrying all of their
attestations. That merge is the product: a record with GOLD, BacDive, and PREGO
attestations is corroborated three ways, and the per-source assertion counts
say how much data sits behind each.

Grounding routes, in the order tried
------------------------------------
PREGO concepts are already ENVO/BTO CURIEs, so they ground to themselves.

BacDive concepts go through kg-microbe's curated
``isolation_source_to_ontology.tsv`` — every one of the 162 sources has a row.
A row with an empty ``object_id`` is an upstream curator's deliberate refusal
to ground (the notes say why), and is honoured as UNGROUNDED rather than
re-guessed here. A row pointing at a non-habitat ontology (PATO qualities,
CHEBI chemicals, NCBITaxon organisms) is recorded as an xref and marked
NOT_APPLICABLE — "Acidic" is a property of a habitat, not a habitat.

GOLD has no upstream mapping table, so its concepts are matched lexically
against the vendored ontology labels and synonyms:

  1. the composed label from the last two path levels ("marine sediment") —
     an exact hit here is EXACT, because the path context is included;
  2. the leaf label alone ("sediment"), when no other GOLD path shares that
     leaf — also EXACT;
  3. the leaf label alone when other GOLD paths share that leaf. Here the
     *shallowest* path claims the term and the rest do not. Ten GOLD paths end
     in "Soil"; "Environmental > Terrestrial > Soil" (depth 3) is what ENVO
     means by soil, while "Environmental > Terrestrial > Cave > Soil" is
     narrower, so the shallowest one grounds to ENVO:00001998 and the others
     get a minted identifier, grounding status NARROW, and ENVO:00001998 as a
     `parent_habitats` entry — which is what the relationship actually is.
     When several paths tie at the shallowest depth there is no principled
     winner ("...Human > ...> Fecal" and "...Birds > ...> Fecal" are both
     depth 5 and neither is *the* feces), so none of them claims the term and
     all become NARROW children of it;
  4. the isolation-source mapping table, keyed on the leaf label;
  5. nothing — minted identifier, UNGROUNDED. These are the ENVO term-request
     backlog, and `just report` counts them.

Lexical matches are unreviewed by construction; that is what
``mapping_status: SEEDED`` means. Nothing here mints a REVIEWED record.

Usage
-----
    python3 scripts/seed_from_sources.py                     # dry-run report
    python3 scripts/seed_from_sources.py --apply --only ENVO:00000019
    python3 scripts/seed_from_sources.py --apply             # write everything
    python3 scripts/seed_from_sources.py --apply --force     # also overwrite
"""

from __future__ import annotations

import argparse
import contextlib
import csv
import hashlib
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from habitatmech.curate.curation_event import record_curation_event  # noqa: E402
from habitatmech.curate.decisions import (  # noqa: E402
    Decision,
    load_decisions,
    validate_decisions,
)
from habitatmech.validation.write_validated import (  # noqa: E402
    ValidationFailedError,
    write_validated_habitat,
)

RAW_DIR = REPO_ROOT / "data" / "raw"
HABITATS_DIR = REPO_ROOT / "data" / "habitats"
DECISIONS_PATH = REPO_ROOT / "curation" / "decisions.tsv"

GOLD_LEVELS = ["ecosystem", "ecosystem_category", "ecosystem_type", "ecosystem_subtype", "specific_ecosystem"]

# Ontologies whose terms can legitimately BE a habitat. Anything else in the
# upstream mapping table describes a habitat rather than being one.
HABITAT_PREFIXES = {"ENVO", "UBERON", "FOODON", "BTO", "PO", "PCO", "FAO", "NCIT", "mesh", "SNOMED"}
# Search order for lexical grounding: the environment ontology first, then
# anatomy, then food, then the tissue vocabulary. A GOLD leaf "blood" should
# reach UBERON before BTO, and "cheese" should reach FOODON.
LEXICAL_PRIORITY = ["ENVO", "UBERON", "FOODON", "BTO"]

# GOLD ecosystem (level 1) + ecosystem category (level 2) -> HabitatCategoryEnum.
# GOLD's own top-two levels are the most reliable category signal available —
# they are curated, complete, and cover 2562 of the source concepts — so they
# take precedence over ontology-ancestry inference when a record merges.
GOLD_CATEGORY_BY_ECOSYSTEM = {
    "Host-associated": "HOST_ASSOCIATED",
    "Engineered": "ENGINEERED",
}
GOLD_CATEGORY_BY_CATEGORY = {
    ("Environmental", "Terrestrial"): "TERRESTRIAL",
    ("Environmental", "Aquatic"): "AQUATIC",
    ("Environmental", "Air"): "AIR",
    ("Engineered", "Food production"): "FOOD",
}

# ENVO anchors for categorising terms that arrive without a GOLD path (PREGO
# habitats, BacDive groundings). Checked against a term's full subclass
# ancestry, first match wins, so the list is ordered most-specific-first.
# ENVO's upper levels are not biome-based (a saline lake's ancestors are
# `water body` / `astronomical body part`, never `aquatic biome`), so these
# anchor on the mid-level classes that actually appear in ancestry chains.
ENVO_CATEGORY_ANCHORS: list[tuple[str, str]] = [
    ("ENVO:01001201", "AQUATIC"),   # marine environmental zone
    ("ENVO:03000033", "AQUATIC"),   # marine sediment
    ("ENVO:01000685", "AQUATIC"),   # water mass
    ("ENVO:00000063", "AQUATIC"),   # water body
    ("ENVO:00002006", "AQUATIC"),   # liquid water
    ("ENVO:00002030", "AQUATIC"),   # aquatic biome
    ("ENVO:00002005", "AIR"),       # air
    ("ENVO:01000267", "AIR"),       # atmosphere
    ("ENVO:00001998", "TERRESTRIAL"),  # soil
    ("ENVO:00000446", "TERRESTRIAL"),  # terrestrial biome
    ("ENVO:00001995", "TERRESTRIAL"),  # rock
    ("ENVO:00002007", "TERRESTRIAL"),  # sediment (aquatic anchors are tried first)
    ("ENVO:00003074", "ENGINEERED"),   # manufactured product
    ("ENVO:01001813", "ENGINEERED"),   # construction
    # Added from the observed ancestry of the terms that were falling through to
    # OTHER, rather than guessed (#11). Aquatic anchors stay above the
    # terrestrial ones, so a hydrographic feature is not caught by `landform`.
    ("ENVO:00000012", "AQUATIC"),      # hydrographic feature
    ("ENVO:01001199", "TERRESTRIAL"),  # terrestrial environmental zone
    ("ENVO:01001886", "TERRESTRIAL"),  # landform
    ("ENVO:00000191", "TERRESTRIAL"),  # solid astronomical body part
]

# Ontology prefix -> category, for terms with no GOLD path and no ENVO anchor.
PREFIX_CATEGORY = {
    "UBERON": "HOST_ASSOCIATED",
    "BTO": "HOST_ASSOCIATED",
    "PO": "HOST_ASSOCIATED",
    "FOODON": "FOOD",
    "NCIT": "CLINICAL",
    "mesh": "CLINICAL",
    "SNOMED": "CLINICAL",
}

PREDICATE_TO_GROUNDING = {
    "skos:exactMatch": "EXACT",
    "skos:broadMatch": "BROAD",
    "skos:narrowMatch": "NARROW",
    "skos:closeMatch": "CLOSE",
}

SEED_CURATOR = "seed_from_sources"


def norm_label(text: str) -> str:
    """Lexical-matching key: lowercase, runs of non-alphanumerics to one space."""
    return re.sub(r"[^a-z0-9]+", " ", (text or "").lower()).strip()


def slugify(text: str, maxlen: int = 72) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", (text or "").lower()).strip("_")
    return (slug[:maxlen].rstrip("_")) or "unnamed"


def mint(kind: str, key: str) -> str:
    """Deterministic minted identifier for a source concept with no defensible
    ontology term. Content-hashed rather than sequential so that adding a
    concept never renumbers its neighbours — a re-seed after an upstream
    refresh should produce a diff only where the data changed."""
    digest = hashlib.sha1(f"{kind}:{key}".encode()).hexdigest()[:10]
    return f"habitatmech:{kind}.{digest}"


def read_tsv(name: str) -> list[dict[str, str]]:
    path = RAW_DIR / name
    if not path.exists():
        raise SystemExit(
            f"missing inventory {path}.\n"
            "Run `just extract-inventory` against a kg-microbe checkout first."
        )
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


# ---------------------------------------------------------------------------
# Ontology index
# ---------------------------------------------------------------------------

class OntologyIndex:
    """Labels, definitions, synonyms, and subclass ancestry for the vendored slice."""

    def __init__(self, terms: list[dict[str, str]], edges: list[dict[str, str]]):
        self.terms = {t["term_id"]: t for t in terms}
        self.parents: dict[str, set[str]] = defaultdict(set)
        for edge in edges:
            self.parents[edge["subject"]].add(edge["object"])

        self.by_label: dict[str, str] = {}
        self.by_synonym: dict[str, str] = {}
        # Index in priority order so a label present in several ontologies
        # resolves to the preferred one deterministically.
        for prefix in LEXICAL_PRIORITY:
            for term_id, term in terms_in(terms, prefix):
                key = norm_label(term["label"])
                if key and key not in self.by_label:
                    self.by_label[key] = term_id
                for syn in (term.get("synonyms") or "").split("|"):
                    skey = norm_label(syn)
                    if skey and skey not in self.by_synonym:
                        self.by_synonym[skey] = term_id

    def label(self, term_id: str) -> str:
        return (self.terms.get(term_id) or {}).get("label", "")

    def definition(self, term_id: str) -> str:
        return (self.terms.get(term_id) or {}).get("definition", "")

    def synonyms(self, term_id: str) -> list[str]:
        raw = (self.terms.get(term_id) or {}).get("synonyms", "")
        return [s.strip() for s in raw.split("|") if s.strip()]

    def direct_parents(self, term_id: str) -> list[str]:
        return sorted(self.parents.get(term_id, ()))

    def ancestors(self, term_id: str) -> set[str]:
        seen: set[str] = set()
        frontier = [term_id]
        while frontier:
            node = frontier.pop()
            for parent in self.parents.get(node, ()):
                if parent not in seen:
                    seen.add(parent)
                    frontier.append(parent)
        return seen


def terms_in(terms: list[dict[str, str]], prefix: str):
    for term in terms:
        if term["ontology"] == prefix:
            yield term["term_id"], term


# ---------------------------------------------------------------------------
# Concept accumulator
# ---------------------------------------------------------------------------

@dataclass
class Concept:
    identifier: str
    label: str
    grounding_status: str
    category: str | None = None
    # Category confidence: a GOLD-derived category beats an inferred one when
    # concepts merge, because GOLD's is curated and the inference is not.
    category_is_authoritative: bool = False
    definition: str = ""
    definition_source: str = ""
    synonyms: dict[tuple[str, str], str] = field(default_factory=dict)
    parents: set[str] = field(default_factory=set)
    xrefs: set[str] = field(default_factory=set)
    attestations: list[dict[str, Any]] = field(default_factory=list)
    parameters: list[dict[str, Any]] = field(default_factory=list)
    taxa: dict[str, dict[str, Any]] = field(default_factory=dict)
    # Best (most specific) grounding status seen, so a merge cannot silently
    # downgrade an EXACT record to a NARROW one or vice versa.
    # How many source concepts feed this record, and how many a curator has
    # signed off on. A merged record is REVIEWED only when the two agree —
    # a record aggregating GOLD, BacDive and PREGO is not checked until all
    # three have been looked at.
    source_concepts: int = 0
    reviewed_sources: int = 0
    _grounding_rank_seen: int = 0

    def add_synonym(self, text: str, syn_type: str, source: str) -> None:
        if not text or norm_label(text) == norm_label(self.label):
            return
        self.synonyms.setdefault((text, syn_type), source)


GROUNDING_RANK = {
    "EXACT": 5,
    "CLOSE": 4,
    "NARROW": 3,
    "BROAD": 2,
    "UNGROUNDED": 1,
    "NOT_APPLICABLE": 0,
}


class ConceptStore:
    def __init__(self, ontology: OntologyIndex):
        self.ontology = ontology
        self.concepts: dict[str, Concept] = {}

    def get(self, identifier: str, label: str, grounding_status: str) -> Concept:
        concept = self.concepts.get(identifier)
        if concept is None:
            concept = Concept(identifier=identifier, label=label, grounding_status=grounding_status)
            concept._grounding_rank_seen = GROUNDING_RANK.get(grounding_status, 0)
            # An ontology-grounded record takes its label, definition, and
            # parents from the ontology, so the record and the term agree.
            if identifier in self.ontology.terms:
                concept.label = self.ontology.label(identifier) or label
                concept.definition = self.ontology.definition(identifier)
                if concept.definition:
                    concept.definition_source = identifier.split(":", 1)[0]
                for syn in self.ontology.synonyms(identifier):
                    concept.add_synonym(syn, "EXACT_SYNONYM", identifier.split(":", 1)[0])
                concept.parents.update(self.ontology.direct_parents(identifier))
            self.concepts[identifier] = concept
        else:
            rank = GROUNDING_RANK.get(grounding_status, 0)
            if rank > concept._grounding_rank_seen:
                concept.grounding_status = grounding_status
                concept._grounding_rank_seen = rank
        return concept

    def set_category(self, concept: Concept, category: str, authoritative: bool) -> None:
        if concept.category is None or (authoritative and not concept.category_is_authoritative):
            concept.category = category
            concept.category_is_authoritative = authoritative


# ---------------------------------------------------------------------------
# Grounding resolution
# ---------------------------------------------------------------------------

@dataclass
class Resolution:
    identifier: str
    grounding_status: str
    mapping_predicate: str | None = None
    # Terms to attach as parents rather than as the identifier — the ambiguous
    # GOLD-leaf case, where the matched term is broader than the concept.
    extra_parents: list[str] = field(default_factory=list)
    extra_xrefs: list[str] = field(default_factory=list)
    route: str = ""
    # True when a curator signed off on this source concept. A merged record is
    # only REVIEWED when every source concept feeding it is.
    reviewed: bool = False


def apply_decision(default: Resolution, minted: str, decisions: dict[str, Decision]) -> Resolution:
    """Let a curator override the seeder's automatic resolution.

    Keyed on the *minted* identifier rather than the resolved one, because that
    names exactly one source concept and is stable across re-seeds (it is a hash
    of the GOLD path or BacDive id). The resolved identifier is shared by every
    concept that merged onto it, so keying there would move all of them at once.

    Returns the automatic resolution untouched when no decision applies, so an
    uncurated corpus behaves exactly as before.
    """
    decision = decisions.get(minted)
    if decision is None:
        return default

    if decision.decision == "GROUND":
        return Resolution(
            decision.object_id,
            decision.grounding_status,
            mapping_predicate=_GROUNDING_TO_PREDICATE.get(decision.grounding_status),
            route=f"curated_ground_from_{default.route}",
            # Uniform with the other branches. validate_decisions() forbids a
            # CLASS-depth grounding, so today this is always True — but the
            # invariant belongs in the validator as policy, not here as an
            # assumption a future change could silently invalidate (#23).
            reviewed=decision.counts_as_reviewed,
        )
    if decision.decision == "GROUND_AS_PARENT":
        # Narrower than the named term: the term becomes a parent, never the
        # identity. Adopting it would merge every sibling that is also a kind
        # of it — the same conflation the seeder's ambiguous-leaf rule avoids.
        return Resolution(
            minted,
            decision.grounding_status,
            mapping_predicate=_GROUNDING_TO_PREDICATE.get(decision.grounding_status),
            extra_parents=[decision.object_id],
            route=f"curated_ground_as_parent_from_{default.route}",
            reviewed=decision.counts_as_reviewed,
        )
    if decision.decision == "NOT_APPLICABLE":
        return Resolution(
            minted,
            "NOT_APPLICABLE",
            extra_xrefs=[decision.object_id] if decision.object_id else [],
            route=f"curated_not_applicable_from_{default.route}",
            reviewed=decision.counts_as_reviewed,
        )
    if decision.decision == "CONFIRM_UNGROUNDED":
        # A nearest-broader term becomes a parent, never the identity: the
        # curator has said explicitly that no term fits, and adopting a broader
        # one would merge distinct concepts (every host clade onto
        # "animal-associated environment", say) under a false equivalence.
        return Resolution(
            minted,
            "UNGROUNDED",
            extra_parents=[decision.object_id] if decision.object_id else [],
            route=f"curated_confirm_ungrounded_from_{default.route}",
            reviewed=decision.counts_as_reviewed,
        )
    # REVIEW: the curator checked the seeder's own answer and endorsed it.
    return replace(default, route=f"curated_review_of_{default.route}",
                   reviewed=decision.counts_as_reviewed)


_GROUNDING_TO_PREDICATE = {
    "EXACT": "skos:exactMatch",
    "BROAD": "skos:broadMatch",
    "NARROW": "skos:narrowMatch",
    "CLOSE": "skos:closeMatch",
}


def resolve_bacdive(row: dict[str, str], mapping: dict[str, dict[str, str]]) -> Resolution:
    key = norm_label(row["label"])
    match = mapping.get(key) or mapping.get(norm_label(row["source_slug"]))
    minted = mint("BACDIVE", row["bacdive_id"])
    if match is None:
        return Resolution(minted, "UNGROUNDED", route="bacdive_unmapped")
    object_id = (match.get("object_id") or "").strip()
    if not object_id:
        # Upstream curator looked at this and declined to ground it. Honour
        # that rather than re-guessing with a weaker method.
        return Resolution(minted, "UNGROUNDED", route="bacdive_declined_upstream")
    prefix = object_id.split(":", 1)[0]
    if prefix not in HABITAT_PREFIXES:
        # Grounded upstream, but to a quality/chemical/organism. Keep the link
        # as an xref so the information survives, but do not pretend the
        # concept is that thing.
        return Resolution(
            minted, "NOT_APPLICABLE", extra_xrefs=[object_id], route="bacdive_non_habitat_target"
        )
    status = PREDICATE_TO_GROUNDING.get((match.get("predicate_id") or "").strip(), "CLOSE")
    return Resolution(object_id, status, mapping_predicate=match.get("predicate_id") or None,
                      route="bacdive_mapping_table")


def leaf_claimants(rows: list[dict[str, str]]) -> dict[str, str | None]:
    """For each normalised GOLD leaf label, which canonical path (if any) may
    claim a matching ontology term as its own identity.

    The shallowest path wins, because depth in GOLD's ecosystem tree is
    specificity: the depth-3 "Environmental > Terrestrial > Soil" is the
    generic soil an ontology term denotes, and everything below it is a kind of
    soil. Ties at the shallowest depth return None — no path claims the term,
    and they all become NARROW children of it instead.
    """
    by_leaf: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_leaf[norm_label(row["leaf_label"])].append(row)

    claimants: dict[str, str | None] = {}
    for leaf, group in by_leaf.items():
        shallowest = min(int(r["depth"]) for r in group)
        tied = [r for r in group if int(r["depth"]) == shallowest]
        claimants[leaf] = tied[0]["canonical_path"] if len(tied) == 1 else None
    return claimants


def composed_claimants(rows: list[dict[str, str]]) -> dict[str, str | None]:
    """Which GOLD path may take a term matched on its *composed* two-level label.

    The composed route used to skip this check entirely, on the reasoning that
    the composed label already carries its context (#15). That holds when the
    paths sharing it differ only by HOST — UBERON:0001977 *is* blood serum
    whether the host is human or a bird, and the host belongs to the taxon — but
    not when they differ by SETTING. Three GOLD paths compose to "anaerobic
    sludge" under plain Bioreactor, DHS reactor and MBR; those are different
    engineered environments, and merging them is the same conflation the leaf
    rule exists to prevent.

    GOLD's own top level separates the two cases: under Host-associated the
    differing prefix is a clade, everywhere else it is a setting. So paths that
    are all Host-associated still merge, and the rest fall back to
    shallowest-claims-it with ties left unclaimed.
    """
    by_composed: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        levels = [row[lvl] for lvl in GOLD_LEVELS if row[lvl]]
        if len(levels) < 2:
            continue
        by_composed[norm_label(" ".join(levels[-2:]))].append(row)

    claimants: dict[str, str | None] = {}
    for composed, group in by_composed.items():
        if len(group) == 1:
            claimants[composed] = group[0]["canonical_path"]
            continue
        if all(r["canonical_path"].startswith("Host-associated") for r in group):
            # Host clade differences are immaterial to the habitat term; every
            # path may take it and they merge, as feces and blood serum do.
            claimants[composed] = ANY_PATH_MAY_CLAIM
            continue
        shallowest = min(int(r["depth"]) for r in group)
        tied = [r for r in group if int(r["depth"]) == shallowest]
        claimants[composed] = tied[0]["canonical_path"] if len(tied) == 1 else None
    return claimants


# Sentinel: every path sharing this composed label may claim the term, because
# they differ only by host clade and so denote the same habitat.
ANY_PATH_MAY_CLAIM = "*"


def resolve_gold(
    row: dict[str, str],
    ontology: OntologyIndex,
    mapping: dict[str, dict[str, str]],
    claimants: dict[str, str | None],
    composed_claim: dict[str, str | None] | None = None,
) -> Resolution:
    levels = [row[lvl] for lvl in GOLD_LEVELS if row[lvl]]
    leaf = norm_label(row["leaf_label"])
    composed = norm_label(" ".join(levels[-2:])) if len(levels) >= 2 else leaf
    minted = mint("GOLD", row["canonical_path"])
    may_claim = claimants.get(leaf) == row["canonical_path"]

    # NOTE: the composed routes deliberately do NOT consult `may_claim`, unlike
    # the leaf routes below. The composed label already carries the path
    # context, so the matched term is not broader than this path the way
    # "sediment" is broader than "marine sediment" — UBERON:0001977 *is* blood
    # serum whether the host is human or bird, and the host distinction belongs
    # to the taxon, not the habitat term. Forcing the guard here would mint
    # three near-identical serum records.
    #
    # The cost: 6 terms are each claimed by 2-3 GOLD paths and merged
    # (blood serum, blood plasma, milk, eye lens, lake sediment, anaerobic
    # sludge). Every path survives in `source_attestations` with its full
    # `source_path`, so nothing is lost — but `anaerobic sludge` across three
    # bioreactor types is a weaker case than the anatomical ones, and nothing
    # here distinguishes "prefix context immaterial" from "prefix context
    # material". Tracked in issue #15.
    composed_claim = composed_claim or {}
    may_claim_composed = composed_claim.get(composed) in (
        ANY_PATH_MAY_CLAIM,
        row["canonical_path"],
    )
    for index, status, predicate, route in (
        (ontology.by_label, "EXACT", "skos:exactMatch", "gold_composed_label"),
        (ontology.by_synonym, "CLOSE", "skos:closeMatch", "gold_composed_synonym"),
    ):
        if not composed or composed not in index:
            continue
        if may_claim_composed:
            return Resolution(index[composed], status, predicate, route=route)
        return Resolution(
            minted, "NARROW", "skos:narrowMatch", extra_parents=[index[composed]],
            route=f"gold_narrower_than_{route}",
        )

    matched = ontology.by_label.get(leaf) or ontology.by_synonym.get(leaf)
    if matched:
        if may_claim:
            exact = leaf in ontology.by_label
            return Resolution(
                matched,
                "EXACT" if exact else "CLOSE",
                "skos:exactMatch" if exact else "skos:closeMatch",
                route="gold_leaf_label" if exact else "gold_leaf_synonym",
            )
        # This path is narrower than the matched term (or tied with a sibling
        # for shallowest). The term becomes a parent, not the identity —
        # merging every GOLD "Sediment" onto ENVO:00002007 would conflate
        # marine, freshwater, and hot-spring sediments into one record.
        return Resolution(
            minted,
            "NARROW",
            "skos:narrowMatch",
            extra_parents=[matched],
            route="gold_narrower_than_leaf_match",
        )

    match = mapping.get(leaf)
    if match and (match.get("object_id") or "").strip():
        object_id = match["object_id"].strip()
        if object_id.split(":", 1)[0] in HABITAT_PREFIXES:
            if may_claim:
                status = PREDICATE_TO_GROUNDING.get((match.get("predicate_id") or "").strip(), "CLOSE")
                return Resolution(object_id, status, match.get("predicate_id") or None,
                                  route="gold_mapping_table")
            return Resolution(minted, "NARROW", "skos:narrowMatch", extra_parents=[object_id],
                              route="gold_narrower_than_mapping_match")

    return Resolution(minted, "UNGROUNDED", route="gold_unmatched")


def infer_category(identifier: str, ontology: OntologyIndex) -> str:
    prefix = identifier.split(":", 1)[0]
    if prefix == "ENVO":
        ancestry = ontology.ancestors(identifier) | {identifier}
        for anchor, category in ENVO_CATEGORY_ANCHORS:
            if anchor in ancestry:
                return category
        return "OTHER"
    return PREFIX_CATEGORY.get(prefix, "OTHER")


# ---------------------------------------------------------------------------
# Ingest per source
# ---------------------------------------------------------------------------

def ingest_gold(
    store: ConceptStore,
    rows: list[dict[str, str]],
    mapping,
    routes: Counter,
    decisions: dict[str, Decision] | None = None,
) -> dict[str, str]:
    claimants = leaf_claimants(rows)
    composed_claim = composed_claimants(rows)
    path_to_identifier: dict[str, str] = {}

    decisions = decisions or {}
    for row in rows:
        res = apply_decision(
            resolve_gold(row, store.ontology, mapping, claimants, composed_claim),
            mint("GOLD", row["canonical_path"]),
            decisions,
        )
        routes[res.route] += 1
        concept = store.get(res.identifier, row["leaf_label"], res.grounding_status)
        concept.source_concepts += 1
        concept.reviewed_sources += 1 if res.reviewed else 0
        path_to_identifier[row["canonical_path"]] = res.identifier

        levels = [row[lvl] for lvl in GOLD_LEVELS if row[lvl]]
        # Authoritative only when GOLD actually resolved a category. Falling
        # through to OTHER is the *absence* of an answer, not a curated one, and
        # treating it as authoritative let three detached GOLD root nodes with 0
        # assertions ("Sediment", "Mid stream", "Low land river systems") pin
        # real records to OTHER — ENVO:00002007 sediment sat in other/ despite
        # being an explicit TERRESTRIAL anchor (#11).
        category = GOLD_CATEGORY_BY_CATEGORY.get(
            (levels[0], levels[1]) if len(levels) >= 2 else ("", "")
        ) or GOLD_CATEGORY_BY_ECOSYSTEM.get(levels[0] if levels else "")
        if category:
            store.set_category(concept, category, authoritative=True)

        concept.add_synonym(row["leaf_label"], "EXACT_SYNONYM", "GOLD")
        concept.parents.update(res.extra_parents)
        concept.xrefs.update(res.extra_xrefs)

        attestation: dict[str, Any] = {
            "source": "GOLD",
            "source_label": row["leaf_label"],
            "source_path": row["canonical_path"],
        }
        node_ids = [n for n in (row["gold_node_ids"] or "").split("|") if n]
        if node_ids:
            # A canonical path collapses several GOLD node ids; name the first
            # and let gold_node_count carry the rest rather than emitting a
            # multi-kilobyte id list onto the record.
            attestation["source_id"] = node_ids[0]
            if len(node_ids) > 1:
                attestation["notes"] = (
                    f"{len(node_ids)} GOLD ecosystem node ids share this path; "
                    f"first shown. See data/raw/gold_ecosystem_paths.tsv."
                )
        if res.mapping_predicate:
            attestation["mapping_predicate"] = res.mapping_predicate
        organisms = int(row.get("organism_count") or 0)
        if organisms:
            attestation["assertion_count"] = organisms
            attestation["assertion_unit"] = "ORGANISM"
        concept.attestations.append(attestation)

    # Second pass: link each GOLD concept to the concept of its parent path.
    for row in rows:
        levels = [row[lvl] for lvl in GOLD_LEVELS if row[lvl]]
        if len(levels) < 2:
            continue
        parent_path = " > ".join(levels[:-1])
        parent_id = path_to_identifier.get(parent_path)
        child_id = path_to_identifier[row["canonical_path"]]
        if parent_id and parent_id != child_id:
            store.concepts[child_id].parents.add(parent_id)
    return path_to_identifier


def ingest_bacdive(
    store: ConceptStore,
    rows: list[dict[str, str]],
    mapping,
    routes: Counter,
    decisions: dict[str, Decision] | None = None,
    taxa_rows: list[dict[str, str]] | None = None,
) -> None:
    decisions = decisions or {}
    taxa_by_source: dict[str, list[dict[str, str]]] = defaultdict(list)
    for taxon_row in taxa_rows or []:
        taxa_by_source[taxon_row["bacdive_id"]].append(taxon_row)
    for row in rows:
        res = apply_decision(
            resolve_bacdive(row, mapping), mint("BACDIVE", row["bacdive_id"]), decisions
        )
        routes[res.route] += 1
        concept = store.get(res.identifier, row["label"], res.grounding_status)
        concept.source_concepts += 1
        concept.reviewed_sources += 1 if res.reviewed else 0
        if concept.category is None:
            store.set_category(concept, infer_category(res.identifier, store.ontology), authoritative=False)
        concept.add_synonym(row["label"], "EXACT_SYNONYM", "BacDive")
        concept.parents.update(res.extra_parents)
        concept.xrefs.update(res.extra_xrefs)

        attestation: dict[str, Any] = {
            "source": "BACDIVE",
            "source_id": row["bacdive_id"],
            "source_label": row["label"],
        }
        if res.mapping_predicate:
            attestation["mapping_predicate"] = res.mapping_predicate
        strains = int(row.get("strain_count") or 0)
        if strains:
            attestation["assertion_count"] = strains
            attestation["assertion_unit"] = "STRAIN"
        if res.route == "bacdive_declined_upstream":
            attestation["notes"] = (
                "kg-microbe's isolation-source mapping table has a row for this "
                "source with no ontology target; treated as ungrounded rather "
                "than re-grounded by lexical match."
            )
        elif res.route == "bacdive_non_habitat_target":
            attestation["notes"] = (
                "Upstream mapping targets a non-habitat ontology "
                f"({', '.join(res.extra_xrefs)}); kept as an xref."
            )
        concept.attestations.append(attestation)

        # Taxa reached by the isolation-source -> strain -> taxon join. Counted
        # by distinct strain, so unlike PREGO's near-tied scores (#8) the
        # ranking discriminates: 400 strains beats 1.
        for taxon_row in taxa_by_source.get(row["bacdive_id"], []):
            taxon_id = taxon_row["taxon_id"]
            if not taxon_id.startswith("NCBITaxon:") or taxon_id in concept.taxa:
                continue
            entry: dict[str, Any] = {"taxon_id": taxon_id, "source": "BACDIVE"}
            if taxon_row.get("taxon_label"):
                entry["taxon_label"] = taxon_row["taxon_label"]
            with contextlib.suppress(KeyError, ValueError):
                entry["association_count"] = int(taxon_row["strain_count"])
            concept.taxa[taxon_id] = entry


def ingest_prego(
    store: ConceptStore,
    rows: list[dict[str, str]],
    taxa_rows: list[dict[str, str]],
    routes: Counter,
    decisions: dict[str, Decision] | None = None,
) -> None:
    decisions = decisions or {}
    taxa_by_habitat: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in taxa_rows:
        taxa_by_habitat[row["prego_id"]].append(row)

    for row in rows:
        # PREGO concepts ground to themselves, but they still get a minted key
        # so a curator can address one — to endorse it, or to rule it out as a
        # non-habitat — the same way as any other source concept.
        res = apply_decision(
            Resolution(row["prego_id"], "EXACT", route="prego_self_grounded"),
            mint("PREGO", row["prego_id"]),
            decisions,
        )
        identifier = res.identifier
        routes[res.route] += 1
        concept = store.get(identifier, identifier, res.grounding_status)
        concept.source_concepts += 1
        concept.reviewed_sources += 1 if res.reviewed else 0
        # Both, not just xrefs: a CONFIRM_UNGROUNDED decision records its
        # nearest-broader term as a parent, and dropping it here would silently
        # lose the placement the curator recorded (#21).
        concept.parents.update(res.extra_parents)
        concept.xrefs.update(res.extra_xrefs)
        # The attestation and the taxa describe the PREGO *term*, so they keep
        # using prego_id even when a curator redirected the concept elsewhere —
        # otherwise a redirect would silently reattribute PREGO's assertions to
        # whatever the concept was pointed at, and drop its taxa on the floor.
        prego_id = row["prego_id"]
        if not concept.label or concept.label == identifier:
            # PREGO nodes carry no label of their own; fall back to the first
            # synonym so a record without an ontology label is still readable.
            synonyms = [s for s in (row.get("prego_synonyms") or "").split("|") if s]
            concept.label = store.ontology.label(identifier) or (synonyms[0] if synonyms else identifier)
        if concept.category is None:
            store.set_category(concept, infer_category(identifier, store.ontology), authoritative=False)
        for syn in (row.get("prego_synonyms") or "").split("|"):
            concept.add_synonym(syn.strip(), "RELATED_SYNONYM", "PREGO")

        attestation: dict[str, Any] = {
            "source": "PREGO",
            "source_id": prego_id,
            "source_label": store.ontology.label(prego_id) or prego_id,
        }
        taxon_count = int(row.get("taxon_count") or 0)
        if taxon_count:
            attestation["assertion_count"] = taxon_count
            attestation["assertion_unit"] = "TAXON"
        score = float(row.get("max_prego_score") or 0)
        if score:
            attestation["score"] = score
        if row.get("channels"):
            attestation["evidence_channels"] = row["channels"]
        concept.attestations.append(attestation)

        for taxon_row in taxa_by_habitat.get(prego_id, []):
            taxon_id = taxon_row["taxon_id"]
            if not taxon_id.startswith("NCBITaxon:") or taxon_id in concept.taxa:
                continue
            entry: dict[str, Any] = {"taxon_id": taxon_id, "source": "PREGO"}
            if taxon_row.get("taxon_label"):
                entry["taxon_label"] = taxon_row["taxon_label"]
            with contextlib.suppress(KeyError, ValueError):
                entry["score"] = float(taxon_row["prego_score"])
            concept.taxa[taxon_id] = entry


def ingest_parameters(store: ConceptStore, rows: list[dict[str, str]], stats: Counter) -> None:
    """Attach physicochemical parameters, but only for rows that name exactly
    one term.

    A row like ``soil_mineral`` lists ``ENVO:00001998|ENVO:01000256`` — the
    conjunction "soil AND mineral material", which neither term denotes on its
    own. ``sediment_marine_cold`` is worse: it composes an ENVO habitat with a
    PATO temperature quality. Attaching either row's parameters to its first
    term would put compound-environment values on the general habitat, so
    multi-term rows are skipped and counted rather than guessed at.
    """
    parameter_names = {
        "Water": "WATER_AVAILABILITY",
        "water variability": "WATER_VARIABILITY",
        "Nutrients": "NUTRIENTS",
        "Gradients": "GRADIENTS",
        "Organic": "ORGANIC_MATTER",
        "Structural": "STRUCTURAL_COMPLEXITY",
        "Pressure": "PRESSURE",
        "Temperature": "TEMPERATURE",
        "temp variability": "TEMPERATURE_VARIABILITY",
        "Salinity": "SALINITY",
        "salinity variability": "SALINITY_VARIABILITY",
        "pH": "PH",
    }
    attested: set[str] = set()
    for row in rows:
        term_ids = [t for t in (row.get("term_ids") or "").split("|") if t]
        if len(term_ids) != 1:
            stats["parameter_rows_skipped_multi_term"] += 1
            continue
        identifier = term_ids[0]
        concept = store.concepts.get(identifier)
        if concept is None:
            # The term is real and habitat-shaped but no source vocabulary
            # attested it, so no concept exists yet. Create one rather than
            # dropping the parameters: the environment table is itself a source
            # of habitats, not merely an annotation layer on other sources, and
            # treating it as the latter is why only 29 records carried
            # parameters (#13).
            if identifier.split(":", 1)[0] not in HABITAT_PREFIXES:
                stats["parameter_rows_skipped_non_habitat_term"] += 1
                continue
            if identifier not in store.ontology.terms:
                stats["parameter_rows_skipped_unknown_term"] += 1
                continue
            concept = store.get(identifier, store.ontology.label(identifier), "EXACT")
            concept.source_concepts += 1
            store.set_category(
                concept, infer_category(identifier, store.ontology), authoritative=False
            )
            stats["concepts_created_from_parameter_table"] += 1
        parameter = parameter_names.get(row["parameter"])
        if parameter is None:
            stats["parameter_rows_skipped_unknown_axis"] += 1
            continue
        concept.parameters.append(
            {
                "parameter": parameter,
                "qualitative_value": row["value"],
                "source": f"kg-microbe environments.csv ({row['env_type']})",
            }
        )
        stats["parameter_assertions_attached"] += 1
        if identifier not in attested:
            attested.add(identifier)
            concept.attestations.append(
                {
                    "source": "ENVIRONMENTS_TABLE",
                    "source_id": row["env_type"],
                    "source_label": row["env_type"],
                    "notes": "Physicochemical parameter bands from kg-microbe's environment table.",
                }
            )


# ---------------------------------------------------------------------------
# Record emission
# ---------------------------------------------------------------------------

# Field order for an emitted attestation. Fixed so every record reads the same
# way regardless of which ingest built it — YAML is emitted with sort_keys=False
# to keep the schema's field order, which otherwise leaks each ingest's
# construction order into the corpus.
ATTESTATION_FIELD_ORDER = [
    "source",
    "source_id",
    "source_label",
    "source_path",
    "mapping_predicate",
    "assertion_count",
    "assertion_unit",
    "score",
    "evidence_channels",
    "notes",
]


def order_attestation(attestation: dict[str, Any]) -> dict[str, Any]:
    ordered = {k: attestation[k] for k in ATTESTATION_FIELD_ORDER if k in attestation}
    # Anything not in the list would otherwise be silently dropped.
    ordered.update({k: v for k, v in attestation.items() if k not in ordered})
    return ordered


def build_document(concept: Concept) -> dict[str, Any]:
    doc: dict[str, Any] = {
        "identifier": concept.identifier,
        "label": concept.label,
    }
    if concept.definition:
        doc["definition"] = concept.definition
    if concept.definition_source:
        doc["definition_source"] = concept.definition_source
    doc["habitat_category"] = concept.category or "OTHER"
    doc["grounding_status"] = concept.grounding_status
    doc["mapping_status"] = (
        "REVIEWED"
        if concept.source_concepts and concept.reviewed_sources == concept.source_concepts
        else "SEEDED"
    )

    if concept.synonyms:
        doc["synonyms"] = [
            {"synonym_text": text, "synonym_type": syn_type, "source": source}
            for (text, syn_type), source in sorted(concept.synonyms.items())
        ]
    parents = sorted(p for p in concept.parents if p != concept.identifier)
    if parents:
        doc["parent_habitats"] = parents
    if concept.xrefs:
        doc["xrefs"] = sorted(concept.xrefs)

    doc["source_attestations"] = [
        order_attestation(a)
        for a in sorted(
            concept.attestations,
            key=lambda a: (a["source"], a.get("source_id") or "", a["source_label"]),
        )
    ]
    if concept.parameters:
        doc["environmental_parameters"] = sorted(
            concept.parameters, key=lambda p: (p["parameter"], p["qualitative_value"])
        )
    if concept.taxa:
        doc["characteristic_taxa"] = sorted(
            concept.taxa.values(), key=lambda t: (-(t.get("score") or 0), t["taxon_id"])
        )

    sources = sorted({a["source"] for a in concept.attestations})
    record_curation_event(
        doc,
        curator=SEED_CURATOR,
        action="SEEDED_FROM_SOURCES",
        changes=(
            f"Seeded from data/raw/ inventories; attested by {', '.join(sources)}. "
            f"Grounding: {concept.grounding_status}."
        ),
        timestamp=SEED_TIMESTAMP,
    )
    return doc


# Committed identifier -> slug lockfile. See assign_paths() for why it exists.
PATHS_LOCKFILE = HABITATS_DIR / "PATHS.tsv"
# A slug becomes a filename, so it must not be able to escape the corpus
# directory. The lockfile is hand-editable (that is the rename mechanism), so
# this is validated on load rather than assumed.
SLUG_PATTERN = re.compile(r"^[a-z0-9][a-z0-9_]*$")


def load_lockfile(path: Path = PATHS_LOCKFILE) -> dict[str, str]:
    """Read the committed identifier -> slug assignments.

    Missing file is not an error: the first seed of a fresh corpus mints every
    slug. Malformed or unsafe slugs ARE an error — the file is hand-editable,
    and a slug containing a path separator would write outside the corpus.
    """
    if not path.exists():
        return {}
    lock: dict[str, str] = {}
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        for line_no, row in enumerate(reader, start=2):
            identifier = (row.get("identifier") or "").strip()
            slug = (row.get("slug") or "").strip()
            if not identifier or not slug:
                raise SystemExit(f"{path}:{line_no}: blank identifier or slug")
            if not SLUG_PATTERN.match(slug):
                raise SystemExit(
                    f"{path}:{line_no}: unsafe slug {slug!r} — slugs must match "
                    f"{SLUG_PATTERN.pattern} so they cannot escape {HABITATS_DIR.name}/"
                )
            if identifier in lock:
                raise SystemExit(f"{path}:{line_no}: duplicate identifier {identifier}")
            lock[identifier] = slug
    taken: dict[str, str] = {}
    for identifier, slug in lock.items():
        if slug in taken:
            raise SystemExit(
                f"{path}: slug {slug!r} claimed by both {taken[slug]} and {identifier}"
            )
        taken[slug] = identifier
    return lock


def write_lockfile(assignments: dict[str, str], path: Path = PATHS_LOCKFILE) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["identifier", "slug"], delimiter="\t",
                                lineterminator="\n")
        writer.writeheader()
        for identifier in sorted(assignments):
            writer.writerow({"identifier": identifier, "slug": assignments[identifier]})


def assign_paths(
    concepts: list[Concept], lockfile: dict[str, str] | None = None
) -> tuple[dict[str, Path], dict[str, str]]:
    """Map each concept to its output file. Returns (paths, slug assignments).

    Filenames are pinned by ``data/habitats/PATHS.tsv`` rather than recomputed
    from scratch, because recomputing them is not stable. Two habitats can share
    a label ("Sediment" under several GOLD paths, once minted separately), and
    the previous scheme gave the bare slug to whichever of them sorted first by
    identifier — so an upstream refresh that added a lower-sorting concept
    renamed the incumbent, a delete+add in the diff for a record whose content
    identity never changed. 954 of 3299 files sit on that mechanism.

    With the lockfile:

    * a concept already in the lockfile keeps its slug, always. Nothing about
      the rest of the corpus can move it.
    * a new concept takes ``slugify(label)``, or ``<base>__<id hash>`` if that
      is taken by anything else. If both are taken this raises rather than
      silently colliding.
    * slugs are unique **corpus-wide**, not per-directory. The directory comes
      from ``habitat_category``, which is heuristic and expected to improve
      (issue #11) — corpus-wide uniqueness means a record moving between
      categories can never collide at its destination.
    * the lockfile is rebuilt from the current concept set each run, so an
      entry whose concept disappeared upstream is dropped; it cannot rot.

    Renaming a record is therefore a deliberate edit to PATHS.tsv followed by a
    re-seed — an explicit, reviewable one-line diff instead of an invisible
    consequence of sort order.
    """
    lockfile = lockfile or {}
    assignments: dict[str, str] = {}
    taken: set[str] = set()

    ordered = sorted(concepts, key=lambda c: c.identifier)
    # Honour existing assignments first, so a pinned slug is never stolen by a
    # new concept that happens to sort earlier.
    for concept in ordered:
        slug = lockfile.get(concept.identifier)
        if slug is not None:
            assignments[concept.identifier] = slug
            taken.add(slug)

    for concept in ordered:
        if concept.identifier in assignments:
            continue
        base = slugify(concept.label)
        if base not in taken:
            slug = base
        else:
            suffix = hashlib.sha1(concept.identifier.encode()).hexdigest()[:8]
            slug = f"{base}__{suffix}"
            if slug in taken:
                raise SystemExit(
                    f"slug collision for {concept.identifier}: both {base!r} and "
                    f"{slug!r} are taken. Resolve by hand in {PATHS_LOCKFILE}."
                )
        assignments[concept.identifier] = slug
        taken.add(slug)

    paths = {
        concept.identifier: HABITATS_DIR
        / (concept.category or "OTHER").lower()
        / f"{assignments[concept.identifier]}.yaml"
        for concept in ordered
    }
    return paths, assignments


def find_stale_files(expected: set[Path]) -> list[Path]:
    """Record files on disk that the current assignment does not account for.

    A record whose `habitat_category` changed moves to a different directory,
    and the old file is left behind — two files claiming one identifier, which
    `tests/test_corpus_integrity.py::test_identifiers_are_unique` would fail on.
    Reported always, deleted only with --prune.
    """
    return sorted(p for p in HABITATS_DIR.rglob("*.yaml") if p not in expected)


def _seed_timestamp() -> str:
    """When the data this corpus is built from was extracted.

    Taken from data/raw/MANIFEST.yaml rather than now(): the corpus must be
    byte-reproducible, so a wall-clock stamp would make every re-seed a
    3187-file diff. A frozen literal achieved that too, but lied — a re-seed in
    six months would assert the corpus was seeded on a date it was not (#3).
    The manifest's extracted_at is the honest answer to "when is this data
    from", and it changes only when the data does.
    """
    manifest = RAW_DIR / "MANIFEST.yaml"
    if manifest.exists():
        for line in manifest.read_text(encoding="utf-8").splitlines():
            if line.startswith("extracted_at:"):
                return line.split(":", 1)[1].strip().strip("'\"")
    return "1970-01-01T00:00:00Z"


SEED_TIMESTAMP = _seed_timestamp()


def break_parent_cycles(concepts: list[Concept], ontology: OntologyIndex) -> int:
    """Remove the minimum of non-ontology parent edges needed to make
    `parent_habitats` acyclic. Returns how many were dropped.

    `parent_habitats` is fed from three places that cannot see each other: the
    grounding ontology's own subclass edges, the GOLD parent-path link, and a
    curator's nearest-broader term. The first is a subsumption hierarchy and is
    acyclic by construction. The GOLD link is not — it expresses *containment
    in a classification*, which does not always run the same direction as
    subsumption, and once enough concepts are grounded the two orderings meet
    and close a loop:

        fresh water -> liquid water   (ENVO subclass)
        liquid water -> canal         (GOLD path link, unsound as subsumption)
        canal -> watercourse          (ENVO subclass)
        watercourse -> lotic water body (ENVO subclass)
        lotic water body -> fresh water (GOLD path link)

    A cycle hangs any consumer that walks the hierarchy, so one edge has to go.
    The ontology's edges are authoritative and are never dropped; the GOLD and
    curated ones are heuristics, so a cycle is broken by removing the first
    non-ontology edge on it. Iteration order is sorted, so the choice is
    deterministic and a re-seed drops the same edge.
    """
    known = {c.identifier: c for c in concepts}
    dropped = 0

    def find_cycle() -> list[str] | None:
        """Iterative DFS returning one cycle as a node path, or None.

        Iterative rather than recursive on purpose: raising the interpreter's
        recursion limit to cover a hypothetical deep graph would also disarm it
        for everything else in the process, turning a genuine runaway into a C
        stack overflow instead of a catchable RecursionError. The observed
        parent-chain depth is 12, so there is nothing to cover anyway (#24).
        """
        WHITE, GREY, BLACK = 0, 1, 2
        color = dict.fromkeys(known, WHITE)

        for root in sorted(known):
            if color[root] != WHITE:
                continue
            # Each frame is (node, iterator over its parents); `path` mirrors
            # the frames so a discovered cycle can be reported in full.
            stack: list[tuple[str, object]] = [(root, iter(sorted(known[root].parents)))]
            color[root] = GREY
            path = [root]
            while stack:
                node, parents = stack[-1]
                advanced = False
                for parent in parents:  # type: ignore[union-attr]
                    if parent not in known:
                        continue
                    if color[parent] == GREY:
                        return path[path.index(parent):] + [parent]
                    if color[parent] == WHITE:
                        color[parent] = GREY
                        stack.append((parent, iter(sorted(known[parent].parents))))
                        path.append(parent)
                        advanced = True
                        break
                if not advanced:
                    color[node] = BLACK
                    stack.pop()
                    path.pop()
        return None

    while (cycle := find_cycle()) is not None:
        # The cycle is path + [node, parent] where parent reappears earlier;
        # every consecutive pair in it is a real edge.
        # Consecutive pairs along the cycle; cycle[1:] is deliberately one
        # shorter, so this is not a strict zip.
        edges = [(cycle[i], cycle[i + 1]) for i in range(len(cycle) - 1)]
        target = next(
            (
                (child, parent)
                for child, parent in edges
                if parent not in ontology.direct_parents(child)
            ),
            None,
        )
        if target is None:
            # Would mean the ontology's own hierarchy is cyclic. Refuse rather
            # than silently mangling it.
            raise SystemExit(f"cycle consists only of ontology edges: {' -> '.join(cycle)}")
        known[target[0]].parents.discard(target[1])
        dropped += 1
    return dropped


@dataclass
class Corpus:
    """The harmonized concept set plus the counters describing how it was built.

    Split out of ``main`` so ``scripts/verify_corpus.py`` can run exactly the
    same pipeline and compare its output to what is committed. A verifier that
    reimplemented any of this would drift from the seeder and stop testing what
    it claims to.
    """

    ontology: OntologyIndex
    concepts: list[Concept]
    routes: Counter
    stats: Counter
    source_concept_total: int
    source_counts: dict[str, int]


def build_corpus() -> Corpus:
    """Read data/raw/ and harmonize it into the full concept set."""
    ontology = OntologyIndex(read_tsv("ontology_terms.tsv"), read_tsv("ontology_subclass_edges.tsv"))
    mapping: dict[str, dict[str, str]] = {}
    for row in read_tsv("isolation_source_groundings.tsv"):
        for key in (norm_label(row["subject_label"]), norm_label(row["subject_label_normalized"])):
            if key:
                mapping.setdefault(key, row)

    store = ConceptStore(ontology)
    routes: Counter = Counter()
    stats: Counter = Counter()

    gold_rows = read_tsv("gold_ecosystem_paths.tsv")
    bacdive_rows = read_tsv("bacdive_isolation_sources.tsv")
    prego_rows = read_tsv("prego_habitats.tsv")
    prego_taxa = read_tsv("prego_habitat_taxa.tsv")
    parameter_rows = read_tsv("environment_parameters.tsv")

    # Curator decisions are validated before any of them is applied, so a
    # single unverifiable target fails the whole seed rather than silently
    # grounding 3298 records correctly and one to a term that does not exist.
    decisions = load_decisions(DECISIONS_PATH)
    validate_decisions(
        decisions,
        {term_id: term["label"] for term_id, term in ontology.terms.items()},
        path=DECISIONS_PATH,
    )
    stats["curation_decisions_loaded"] = len(decisions)

    ingest_gold(store, gold_rows, mapping, routes, decisions)
    ingest_bacdive(store, bacdive_rows, mapping, routes, decisions,
                   taxa_rows=read_tsv("bacdive_source_taxa.tsv"))
    ingest_prego(store, prego_rows, prego_taxa, routes, decisions)
    ingest_parameters(store, parameter_rows, stats)

    addressable = (
        {mint("GOLD", row["canonical_path"]) for row in gold_rows}
        | {mint("BACDIVE", row["bacdive_id"]) for row in bacdive_rows}
        | {mint("PREGO", row["prego_id"]) for row in prego_rows}
    )
    unused = sorted(set(decisions) - addressable)
    if unused:
        # A decision that matches no source concept is dead weight: the concept
        # it names vanished upstream, or its identifier was mistyped. Either way
        # the curator's intent is not being honoured and they should know.
        print(
            f"WARNING: {len(unused)} curation decision(s) matched no source concept "
            f"(upstream change, or a typo'd identifier): {unused[:5]}",
            file=sys.stderr,
        )
    stats["curation_decisions_unmatched"] = len(unused)

    concepts = list(store.concepts.values())
    for concept in concepts:
        if concept.category is None:
            concept.category = infer_category(concept.identifier, ontology)

    stats["parent_edges_dropped_to_break_cycles"] = break_parent_cycles(concepts, ontology)

    counts = {"GOLD": len(gold_rows), "BacDive": len(bacdive_rows), "PREGO": len(prego_rows)}
    return Corpus(
        ontology=ontology,
        concepts=concepts,
        routes=routes,
        stats=stats,
        source_concept_total=sum(counts.values()),
        source_counts=counts,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--apply", action="store_true", help="Write files (default is a dry-run report).")
    parser.add_argument("--force", action="store_true", help="Overwrite records that already exist.")
    parser.add_argument(
        "--prune",
        action="store_true",
        help="Delete record files the current assignment does not account for "
        "(a record whose category changed leaves its old file behind). Ignored "
        "on --only/--limit runs, whose path set is not authoritative.",
    )
    parser.add_argument(
        "--only",
        nargs="*",
        metavar="IDENTIFIER",
        help="Seed only these identifiers. Use for the one-record canary before a bulk run.",
    )
    parser.add_argument("--limit", type=int, help="Seed at most N records (after sorting by identifier).")
    args = parser.parse_args(argv)

    corpus = build_corpus()
    concepts = corpus.concepts
    routes, stats = corpus.routes, corpus.stats

    source_concept_total = corpus.source_concept_total
    print("=== harmonization ===")
    breakdown = ", ".join(f"{name} {count}" for name, count in corpus.source_counts.items())
    print(f"  source concepts in:    {source_concept_total} ({breakdown})")
    print(f"  habitat records out:   {len(concepts)}")
    print(f"  merged away:           {source_concept_total - len(concepts)}")

    print("\n=== grounding route ===")
    for route, count in routes.most_common():
        print(f"  {route:34s} {count:6d}")

    print("\n=== grounding status ===")
    for status, count in Counter(c.grounding_status for c in concepts).most_common():
        print(f"  {status:16s} {count:6d}")

    print("\n=== category ===")
    for category, count in Counter(c.category for c in concepts).most_common():
        print(f"  {category:18s} {count:6d}")

    corroboration = Counter(len({a["source"] for a in c.attestations}) for c in concepts)
    print("\n=== sources per record ===")
    for n, count in sorted(corroboration.items()):
        print(f"  {n} source(s)        {count:6d}")

    if stats:
        print("\n=== parameter attachment ===")
        for key, value in sorted(stats.items()):
            print(f"  {key:42s} {value:6d}")

    selected = concepts
    if args.only:
        wanted = set(args.only)
        selected = [c for c in concepts if c.identifier in wanted]
        missing = wanted - {c.identifier for c in selected}
        if missing:
            print(f"\nERROR: --only identifiers not found: {', '.join(sorted(missing))}", file=sys.stderr)
            return 2
    if args.limit:
        selected = sorted(selected, key=lambda c: c.identifier)[: args.limit]

    lockfile = load_lockfile()
    paths, assignments = assign_paths(concepts, lockfile)

    # A full run covers every concept, so its path set is authoritative; a
    # --only/--limit run's is not, and must never drive a prune.
    full_run = not args.only and not args.limit
    inherited = sum(1 for i in assignments if i in lockfile)
    minted = len(assignments) - inherited
    dropped = sorted(set(lockfile) - set(assignments))
    stale = find_stale_files(set(paths.values())) if HABITATS_DIR.exists() else []

    print("\n=== filename assignment ===")
    print(f"  pinned by {PATHS_LOCKFILE.relative_to(REPO_ROOT)}: {inherited}")
    print(f"  newly minted:                    {minted}")
    if dropped:
        print(f"  lockfile entries dropped (concept gone upstream): {len(dropped)}")
        for identifier in dropped[:5]:
            print(f"    {identifier} ({lockfile[identifier]})")
    if stale:
        label = "stale files (record moved category, or concept gone)"
        print(f"  {label}: {len(stale)}")
        for path in stale[:5]:
            print(f"    {path.relative_to(REPO_ROOT)}")
        if not full_run:
            print("    (partial run — not pruning; re-run a full seed to reconcile)")
        elif not args.prune:
            print("    (pass --prune to delete them)")

    if not args.apply:
        print(f"\n--dry-run: would write {len(selected)} record(s) under {HABITATS_DIR}")
        for concept in sorted(selected, key=lambda c: c.identifier)[:5]:
            print(f"  {concept.identifier:32s} -> {paths[concept.identifier].relative_to(REPO_ROOT)}")
        if len(selected) > 5:
            print(f"  ... and {len(selected) - 5} more")
        print("\nRun with --apply to write. Seed one record first: --apply --only <IDENTIFIER>")
        return 0

    written = skipped = failed = 0
    for concept in sorted(selected, key=lambda c: c.identifier):
        path = paths[concept.identifier]
        if path.exists() and not args.force:
            skipped += 1
            continue
        doc = build_document(concept)
        try:
            write_validated_habitat(doc, path)
        except ValidationFailedError as exc:
            failed += 1
            print(f"\nFAILED {concept.identifier} -> {path}", file=sys.stderr)
            print(exc.summary(), file=sys.stderr)
            if failed >= 5:
                print("\naborting after 5 validation failures", file=sys.stderr)
                return 1
            continue
        written += 1

    # Written after the records, so a run that aborts on validation failures
    # does not leave a lockfile promising files that were never created.
    #
    # Only on a full run. assign_paths() covers every concept regardless of
    # --only/--limit (that is what keeps assignments selection-independent), so
    # a partial run would persist 3299 entries beside a handful of files and
    # strand the rest as orphans. A partial run needs no persistence anyway:
    # the same concept set recomputes the same assignments.
    if full_run:
        write_lockfile(assignments)
        print(f"wrote {PATHS_LOCKFILE.relative_to(REPO_ROOT)} ({len(assignments)} assignments)")
    else:
        print(f"partial run — {PATHS_LOCKFILE.relative_to(REPO_ROOT)} left unchanged")

    pruned = 0
    if stale and full_run and args.prune:
        for path in stale:
            path.unlink()
            pruned += 1
        for directory in sorted(HABITATS_DIR.rglob("*"), reverse=True):
            if directory.is_dir() and not any(directory.iterdir()):
                directory.rmdir()
        print(f"pruned {pruned} stale record file(s)")

    print(
        f"\nwrote {written}, skipped {skipped} "
        f"(already present; --force to overwrite), failed {failed}"
    )
    if stale and not pruned:
        print(
            f"WARNING: {len(stale)} stale file(s) remain on disk. Until they are "
            "removed, more than one file may claim the same identifier.",
            file=sys.stderr,
        )
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
