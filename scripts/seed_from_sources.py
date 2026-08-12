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
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from habitatmech.curate.curation_event import record_curation_event  # noqa: E402
from habitatmech.validation.write_validated import (  # noqa: E402
    ValidationFailedError,
    write_validated_habitat,
)

RAW_DIR = REPO_ROOT / "data" / "raw"
HABITATS_DIR = REPO_ROOT / "data" / "habitats"

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


def resolve_gold(
    row: dict[str, str],
    ontology: OntologyIndex,
    mapping: dict[str, dict[str, str]],
    claimants: dict[str, str | None],
) -> Resolution:
    levels = [row[lvl] for lvl in GOLD_LEVELS if row[lvl]]
    leaf = norm_label(row["leaf_label"])
    composed = norm_label(" ".join(levels[-2:])) if len(levels) >= 2 else leaf
    minted = mint("GOLD", row["canonical_path"])
    may_claim = claimants.get(leaf) == row["canonical_path"]

    if composed and composed in ontology.by_label:
        return Resolution(
            ontology.by_label[composed], "EXACT", "skos:exactMatch", route="gold_composed_label"
        )
    if composed and composed in ontology.by_synonym:
        return Resolution(ontology.by_synonym[composed], "CLOSE", "skos:closeMatch",
                          route="gold_composed_synonym")

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

def ingest_gold(store: ConceptStore, rows: list[dict[str, str]], mapping, routes: Counter) -> dict[str, str]:
    claimants = leaf_claimants(rows)
    path_to_identifier: dict[str, str] = {}

    for row in rows:
        res = resolve_gold(row, store.ontology, mapping, claimants)
        routes[res.route] += 1
        concept = store.get(res.identifier, row["leaf_label"], res.grounding_status)
        path_to_identifier[row["canonical_path"]] = res.identifier

        levels = [row[lvl] for lvl in GOLD_LEVELS if row[lvl]]
        category = GOLD_CATEGORY_BY_CATEGORY.get(
            (levels[0], levels[1]) if len(levels) >= 2 else ("", "")
        ) or GOLD_CATEGORY_BY_ECOSYSTEM.get(levels[0] if levels else "") or "OTHER"
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


def ingest_bacdive(store: ConceptStore, rows: list[dict[str, str]], mapping, routes: Counter) -> None:
    for row in rows:
        res = resolve_bacdive(row, mapping)
        routes[res.route] += 1
        concept = store.get(res.identifier, row["label"], res.grounding_status)
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


def ingest_prego(
    store: ConceptStore,
    rows: list[dict[str, str]],
    taxa_rows: list[dict[str, str]],
    routes: Counter,
) -> None:
    taxa_by_habitat: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in taxa_rows:
        taxa_by_habitat[row["prego_id"]].append(row)

    for row in rows:
        identifier = row["prego_id"]
        routes["prego_self_grounded"] += 1
        concept = store.get(identifier, identifier, "EXACT")
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
            "source_id": identifier,
            "source_label": store.ontology.label(identifier) or identifier,
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

        for taxon_row in taxa_by_habitat.get(identifier, []):
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
            stats["parameter_rows_skipped_unknown_concept"] += 1
            continue
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


def build_document(concept: Concept, ontology: OntologyIndex) -> dict[str, Any]:
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
    doc["mapping_status"] = "SEEDED"

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


def assign_paths(concepts: list[Concept]) -> dict[str, Path]:
    """Map each concept to its output file, resolving slug collisions.

    Two habitats can share a label ("Sediment" under several GOLD paths, once
    minted separately). The first by identifier keeps the bare slug; the rest
    get their identifier hash appended, so the filename stays stable for a
    given identifier regardless of what else is in the corpus.
    """
    paths: dict[str, Path] = {}
    used: dict[Path, str] = {}
    for concept in sorted(concepts, key=lambda c: c.identifier):
        directory = HABITATS_DIR / (concept.category or "OTHER").lower()
        base = slugify(concept.label)
        candidate = directory / f"{base}.yaml"
        if candidate in used:
            suffix = hashlib.sha1(concept.identifier.encode()).hexdigest()[:8]
            candidate = directory / f"{base}__{suffix}.yaml"
        used[candidate] = concept.identifier
        paths[concept.identifier] = candidate
    return paths


SEED_TIMESTAMP = "2026-08-12T00:00:00Z"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--apply", action="store_true", help="Write files (default is a dry-run report).")
    parser.add_argument("--force", action="store_true", help="Overwrite records that already exist.")
    parser.add_argument(
        "--only",
        nargs="*",
        metavar="IDENTIFIER",
        help="Seed only these identifiers. Use for the one-record canary before a bulk run.",
    )
    parser.add_argument("--limit", type=int, help="Seed at most N records (after sorting by identifier).")
    args = parser.parse_args(argv)

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

    ingest_gold(store, gold_rows, mapping, routes)
    ingest_bacdive(store, bacdive_rows, mapping, routes)
    ingest_prego(store, prego_rows, prego_taxa, routes)
    ingest_parameters(store, parameter_rows, stats)

    concepts = list(store.concepts.values())
    for concept in concepts:
        if concept.category is None:
            concept.category = infer_category(concept.identifier, ontology)

    source_concept_total = len(gold_rows) + len(bacdive_rows) + len(prego_rows)
    print("=== harmonization ===")
    print(f"  source concepts in:    {source_concept_total} "
          f"(GOLD {len(gold_rows)}, BacDive {len(bacdive_rows)}, PREGO {len(prego_rows)})")
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

    paths = assign_paths(concepts)

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
        doc = build_document(concept, ontology)
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

    print(
        f"\nwrote {written}, skipped {skipped} "
        f"(already present; --force to overwrite), failed {failed}"
    )
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
