#!/usr/bin/env python3
"""Extract habitat/environment source inventories from a kg-microbe checkout.

HabitatMech does not vendor kg-microbe's multi-gigabyte KGX dumps. It vendors
the *inventories* derived from them — small, reviewable TSVs that name every
habitat concept each source asserts, how often it is asserted, and (where
kg-microbe already curated one) its ontology grounding. Those TSVs under
``data/raw/`` are the seed input for ``scripts/seed_from_sources.py``.

Sources read (all under the kg-microbe checkout):

* ``data/raw/gold/GOLD_{nodes,edges}.tsv`` — the JGI GOLD ecosystem
  classification. The 5-level path (Ecosystem > Ecosystem Category >
  Ecosystem Type > Ecosystem Subtype > Specific Ecosystem) is reconstructed by
  walking ``biolink:subclass_of`` edges up to the ``root`` node, and
  ``biolink:occurs_in`` edges give per-node assertion counts. Note the
  *transformed* GOLD nodes carry the label "Unclassified" for every ecosystem
  node, so labels must come from the raw dump.
* ``data/transformed/bacdive/{nodes,edges}.tsv`` — BacDive isolation sources
  (``bacdive.isolation_source:*``) and their strain counts.
* ``data/transformed/prego/{nodes,edges}.tsv`` — PREGO habitat terms (ENVO and
  BTO) and their taxon-association counts, scores, and evidence channels.
* ``data/raw/environments.csv`` — the Cobo-Simon-style environment parameter
  table (water/nutrients/pH/salinity/temperature/pressure qualifiers per
  environment type, with ENVO ids).
* ``mappings/isolation_source_to_ontology.tsv`` — kg-microbe's curated
  isolation-source → ontology mapping table (ENVO/UBERON/FOODON/PO/NCIT/...).
* ``data/transformed/ontologies/{envo,uberon,foodon}_{nodes,edges}.tsv`` and
  ``data/raw/bto.db`` — authoritative labels, definitions, synonyms, and
  subclass edges for the terms anything above grounds to.

Usage
-----
    python3 scripts/extract_source_inventory.py --kg-microbe /path/to/kg-microbe
    python3 scripts/extract_source_inventory.py --dry-run     # counts only, no writes
"""

from __future__ import annotations

import argparse
import csv
import datetime
import gzip
import hashlib
import os
import re
import sqlite3
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from collections.abc import Iterator
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = REPO_ROOT / "data" / "raw"
CONF_PATH = REPO_ROOT / "conf" / "sources.yaml"

# GOLD uses this literal as the "no value at this level" filler at every level
# of the ecosystem path, so a path's real depth is where the fillers start.
GOLD_UNCLASSIFIED = "Unclassified"
GOLD_ROOT_LABEL = "root"

# The five GOLD ecosystem path levels, below the synthetic `root` node.
GOLD_LEVELS = [
    "ecosystem",
    "ecosystem_category",
    "ecosystem_type",
    "ecosystem_subtype",
    "specific_ecosystem",
]

# Ontologies we pull labels/definitions/edges from. BTO is handled separately
# because kg-microbe carries it as a semsql SQLite build, not a KGX TSV pair.
TSV_ONTOLOGIES = ["envo", "uberon", "foodon"]

# csv's default field-size limit (128 KiB) is smaller than some kg-microbe
# description/synonym cells. Raise it to the platform maximum rather than
# letting the reader raise mid-stream on one long row.
def _raise_csv_limit() -> None:
    limit = sys.maxsize
    while True:
        try:
            csv.field_size_limit(limit)
            return
        except OverflowError:
            limit //= 2


def read_tsv(path: Path) -> Iterator[dict[str, str]]:
    """Stream a KGX-style TSV as dicts. Raises if the file is missing."""
    if not path.exists():
        raise FileNotFoundError(f"required source file not found: {path}")
    with path.open(newline="", encoding="utf-8") as fh:
        yield from csv.DictReader(fh, delimiter="\t")


def write_tsv(path: Path, fieldnames: list[str], rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, delimiter="\t", extrasaction="raise")
        writer.writeheader()
        for row in rows:
            writer.writerow({k: ("" if row.get(k) is None else row.get(k)) for k in fieldnames})


def sha256_of(path: Path, chunk: int = 1 << 20) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        while block := fh.read(chunk):
            digest.update(block)
    return digest.hexdigest()


# ---------------------------------------------------------------------------
# GOLD ecosystem classification
# ---------------------------------------------------------------------------

def extract_gold(kgm: Path) -> tuple[list[dict[str, Any]], list[str]]:
    """Reconstruct GOLD ecosystem paths and collapse them to distinct concepts.

    GOLD's ecosystem tree is a *path* tree: many distinct node ids spell out the
    same 5-level path because a node exists per (path, source-record) pairing,
    and unfilled levels repeat the "Unclassified" filler. Collapsing on the
    filler-stripped path is what turns 4226 nodes into the set of distinct
    ecosystem concepts, and the per-node assertion counts sum across the nodes
    that collapse together.
    """
    nodes_path = kgm / "data" / "raw" / "gold" / "GOLD_nodes.tsv"
    edges_path = kgm / "data" / "raw" / "gold" / "GOLD_edges.tsv"

    labels: dict[str, str] = {}
    for row in read_tsv(nodes_path):
        if "EnvironmentalFeature" in (row.get("category") or ""):
            labels[row["id"]] = (row.get("name") or "").strip()

    parent: dict[str, str] = {}
    multi_parent: list[str] = []
    # occurrence counts, split by the GOLD id class of the asserting subject
    # (Go = organism, Gs = study, Gb = biosample, Ga = analysis project).
    counts: dict[str, Counter] = defaultdict(Counter)
    for row in read_tsv(edges_path):
        pred = row.get("predicate")
        subj, obj = row.get("subject", ""), row.get("object", "")
        if pred == "biolink:subclass_of" and subj.startswith("gold.ecosystem:"):
            if subj in parent and parent[subj] != obj:
                # Single-valued by assumption. A second parent would change the
                # node's canonical_path, hence its depth (which decides who
                # claims an ontology term) and its minted identifier (hashed
                # from the path) — silently. 0 of 4226 nodes have one today, so
                # this is prophylactic; it must fail rather than pick one (#18).
                multi_parent.append(subj)
            parent[subj] = obj
        elif pred == "biolink:occurs_in" and obj.startswith("gold.ecosystem:"):
            local = subj.split(":", 1)[-1]
            kind = local[:2] if local[:1] == "G" else "other"
            counts[obj][kind] += 1

    if multi_parent:
        raise SystemExit(
            f"{len(multi_parent)} GOLD ecosystem node(s) have more than one subclass_of "
            f"parent, e.g. {sorted(set(multi_parent))[:5]}. The path reconstruction "
            "assumes a tree; decide what a multi-parent path means before proceeding (#18)."
        )

    truncated: list[str] = []

    def path_labels(node: str) -> list[str]:
        """Root-to-node label path, cycle-guarded.

        A cycle in GOLD's parent chain must not spin forever, but it must not
        pass silently either: a truncated path changes the concept's `depth`
        (which decides who claims an ontology term in the seeder's
        shallowest-path rule) and changes its minted identifier (hashed from
        the path). Truncations are collected and reported by the caller rather
        than swallowed here.
        """
        seen: set[str] = set()
        out: list[str] = []
        cur: str | None = node
        while cur and cur not in seen:
            seen.add(cur)
            out.append(labels.get(cur, cur))
            cur = parent.get(cur)
        if cur is not None:
            truncated.append(node)
        out.reverse()
        if out and out[0] == GOLD_ROOT_LABEL:
            out = out[1:]
        return out

    collapsed: dict[tuple[str, ...], dict[str, Any]] = {}
    for node in labels:
        levels = path_labels(node)
        # Strip trailing fillers: "Soil > Unclassified > Unclassified" is the
        # concept "Soil", not three concepts. Interior fillers are kept as ""
        # so the level columns stay positionally faithful to GOLD's schema.
        while levels and levels[-1] == GOLD_UNCLASSIFIED:
            levels.pop()
        if not levels:
            continue
        key = tuple(levels)
        entry = collapsed.setdefault(
            key,
            {
                "canonical_path": " > ".join(levels),
                **{
                    lvl: (levels[i] if i < len(levels) and levels[i] != GOLD_UNCLASSIFIED else "")
                    for i, lvl in enumerate(GOLD_LEVELS)
                },
                "leaf_label": levels[-1],
                "depth": len(levels),
                "_node_ids": [],
                "_counts": Counter(),
            },
        )
        entry["_node_ids"].append(node)
        entry["_counts"].update(counts.get(node, Counter()))

    rows = []
    for entry in collapsed.values():
        node_ids = sorted(entry.pop("_node_ids"))
        tally = entry.pop("_counts")
        entry["gold_node_ids"] = "|".join(node_ids)
        entry["gold_node_count"] = len(node_ids)
        entry["organism_count"] = tally.get("Go", 0)
        entry["study_count"] = tally.get("Gs", 0)
        entry["biosample_count"] = tally.get("Gb", 0)
        entry["total_assertions"] = sum(tally.values())
        rows.append(entry)

    rows.sort(key=lambda r: (-r["total_assertions"], r["canonical_path"]))
    return rows, truncated


# ---------------------------------------------------------------------------
# BacDive isolation sources
# ---------------------------------------------------------------------------

def extract_bacdive(
    kgm: Path, top_taxa: int
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, set[str]]]:
    """Return (isolation-source rows, top-taxa rows).

    BacDive links an isolation source to a *strain*, and the strain to a taxon,
    so reaching taxa needs a two-hop join that the first cut skipped (#9). It is
    the second-largest body of evidence in the corpus — 144k strain-level
    assertions across 162 sources — and without it host-associated and clinical
    habitats got taxa only where a PREGO term happened to merge in.

    Unlike PREGO's near-tied scores, these are counts of distinct strains, which
    discriminate: a taxon isolated 400 times from a source is genuinely more
    characteristic of it than one isolated once.
    """
    nodes_path = kgm / "data" / "transformed" / "bacdive" / "nodes.tsv"
    edges_path = kgm / "data" / "transformed" / "bacdive" / "edges.tsv"

    sources: dict[str, str] = {}
    for row in read_tsv(nodes_path):
        if row["id"].startswith("bacdive.isolation_source:"):
            sources[row["id"]] = (row.get("name") or "").strip()

    strain_counts: Counter = Counter()
    source_strains: dict[str, set[str]] = defaultdict(set)
    strain_taxon: dict[str, str] = {}
    for row in read_tsv(edges_path):
        subj, obj = row.get("subject", ""), row.get("object", "")
        if subj.startswith("bacdive.isolation_source:"):
            strain_counts[subj] += 1
            if obj.startswith("kgmicrobe.strain:"):
                source_strains[subj].add(obj)
        elif (
            subj.startswith("kgmicrobe.strain:")
            and row.get("predicate") == "biolink:subclass_of"
            and obj.startswith("NCBITaxon:")
        ):
            strain_taxon[subj] = obj

    rows = [
        {
            "bacdive_id": src_id,
            "label": label,
            "source_slug": src_id.split(":", 1)[-1],
            "strain_count": strain_counts.get(src_id, 0),
            # The pool a kept taxon was ranked out of. Without it a record shows
            # "rank 3" with no way to tell whether that is 3 of 5 or 3 of 8715.
            "taxon_count": len(
                {strain_taxon[st] for st in source_strains.get(src_id, ()) if st in strain_taxon}
            ),
        }
        for src_id, label in sources.items()
    ]
    rows.sort(key=lambda r: (-r["strain_count"], r["label"]))

    # Second hop: isolation source -> strain -> taxon, counted by distinct strain.
    full_taxa: dict[str, set[str]] = {}
    kept: dict[str, list[tuple[str, int]]] = {}
    needed: set[str] = set()
    for src_id, strains in source_strains.items():
        tally: Counter = Counter()
        for strain in strains:
            taxon = strain_taxon.get(strain)
            if taxon:
                tally[taxon] += 1
        full_taxa[src_id] = set(tally)
        ranked = sorted(tally.items(), key=lambda kv: (-kv[1], kv[0]))[:top_taxa]
        if ranked:
            kept[src_id] = ranked
            needed.update(t for t, _ in ranked)

    labels = _load_taxon_labels(kgm, needed)
    taxa_rows = [
        {
            "bacdive_id": src_id,
            "rank": rank,
            "taxon_id": taxon,
            "taxon_label": labels.get(taxon, ""),
            "strain_count": count,
        }
        for src_id in sorted(kept)
        for rank, (taxon, count) in enumerate(kept[src_id], start=1)
    ]
    return rows, taxa_rows, full_taxa


# ---------------------------------------------------------------------------
# PREGO habitats
# ---------------------------------------------------------------------------

def extract_prego(
    kgm: Path, top_taxa: int
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, set[str]]]:
    """Return (habitat rows, top-taxa rows).

    PREGO asserts up to ~8700 taxa for a single habitat, so the full
    habitat-taxon matrix is neither committable nor useful inline on a record.
    We keep the top ``top_taxa`` per habitat by PREGO score — enough to
    populate `characteristic_taxa` with the strongest associations — and record
    the untruncated total as `taxon_count` so a reader can see what was cut.
    """
    nodes_path = kgm / "data" / "transformed" / "prego" / "nodes.tsv"
    edges_path = kgm / "data" / "transformed" / "prego" / "edges.tsv"

    habitats: dict[str, dict[str, str]] = {}
    for row in read_tsv(nodes_path):
        node_id = row["id"]
        if node_id.startswith(("ENVO:", "BTO:")):
            habitats[node_id] = {
                "category": row.get("category", ""),
                "synonyms": row.get("synonym", ""),
            }

    # Best (score, direct) per (habitat, taxon); a pair can appear once per
    # evidence channel, and keeping the max avoids counting a taxon twice.
    best: dict[str, dict[str, tuple[float, bool, set[str]]]] = defaultdict(dict)
    channels: dict[str, Counter] = defaultdict(Counter)
    max_score: dict[str, float] = defaultdict(float)
    direct: Counter = Counter()
    for row in read_tsv(edges_path):
        subj = row.get("subject", "")
        if subj not in habitats:
            continue
        taxon = row.get("object", "")
        chan = row.get("prego_channel") or ""
        if chan:
            channels[subj][chan] += 1
        try:
            score = float(row.get("prego_score") or 0)
        except ValueError:
            score = 0.0
        is_direct = (row.get("prego_direct_flag") or "").upper() == "TRUE"
        max_score[subj] = max(max_score[subj], score)
        if is_direct:
            direct[subj] += 1
        prev = best[subj].get(taxon)
        if prev is None:
            best[subj][taxon] = (score, is_direct, {chan} if chan else set())
        else:
            best[subj][taxon] = (
                max(prev[0], score),
                prev[1] or is_direct,
                prev[2] | ({chan} if chan else set()),
            )

    full_taxa: dict[str, set[str]] = {h: set(t) for h, t in best.items()}
    kept: dict[str, list[tuple[str, float, bool, set[str]]]] = {}
    needed_taxa: set[str] = set()
    for hab_id, taxa in best.items():
        ranked = sorted(
            ((t, s, d, c) for t, (s, d, c) in taxa.items()),
            key=lambda x: (-x[1], not x[2], x[0]),
        )[:top_taxa]
        kept[hab_id] = ranked
        needed_taxa.update(t for t, _, _, _ in ranked)

    taxon_labels = _load_taxon_labels(kgm, needed_taxa)

    habitat_rows = []
    for hab_id, meta in habitats.items():
        habitat_rows.append(
            {
                "prego_id": hab_id,
                "ontology": hab_id.split(":", 1)[0],
                "biolink_category": meta["category"],
                "taxon_count": len(best.get(hab_id, {})),
                "direct_assertion_count": direct.get(hab_id, 0),
                "max_prego_score": f"{max_score.get(hab_id, 0.0):g}",
                "channels": "|".join(sorted(channels.get(hab_id, {}))),
                "prego_synonyms": meta["synonyms"],
            }
        )
    habitat_rows.sort(key=lambda r: (-r["taxon_count"], r["prego_id"]))

    taxa_rows = [
        {
            "prego_id": hab_id,
            "taxon_id": taxon,
            "taxon_label": taxon_labels.get(taxon, ""),
            "prego_score": f"{score:g}",
            "direct_flag": "TRUE" if is_direct else "FALSE",
            "channels": "|".join(sorted(chans)),
            "rank": rank,
        }
        for hab_id in sorted(kept)
        for rank, (taxon, score, is_direct, chans) in enumerate(kept[hab_id], start=1)
    ]
    return habitat_rows, taxa_rows, full_taxa


def extract_madin(kgm: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, set[str]]]:
    """Return (habitat rows, all habitat-taxon rows, full taxon sets).

    Madin et al. is a literature-curated compilation, and kg-microbe already
    transforms it into ``biolink:location_of`` edges pointing habitat -> taxon,
    the same shape and direction PREGO uses. The habitats are already CURIEs
    (mostly ENVO) or ``bacdive.isolation_source:`` ids that this repo already
    carries, so almost none of the grounding work has to be redone (#40).

    Unlike PREGO and BacDive this returns **every** pair rather than a top-N,
    because Madin supplies no score to rank by and inventing an order here would
    read as a ranking that does not exist. The trim happens after corroboration
    is computed, where "another source agrees" is a real reason to prefer one
    pair over another — see :func:`_trim_unranked`.
    """
    nodes_path = kgm / "data" / "transformed" / "madin_etal" / "nodes.tsv"
    edges_path = kgm / "data" / "transformed" / "madin_etal" / "edges.tsv"
    if not edges_path.exists():
        print(f"  WARNING: {edges_path} not found; Madin is not being ingested")
        return [], [], {}

    labels: dict[str, str] = {}
    for row in read_tsv(nodes_path):
        if (row.get("name") or "").strip():
            labels[row["id"]] = row["name"].strip()

    taxa: dict[str, set[str]] = defaultdict(set)
    for row in read_tsv(edges_path):
        if row.get("predicate") != "biolink:location_of":
            continue
        obj = row.get("object", "")
        if obj.startswith("NCBITaxon:"):
            taxa[row["subject"]].add(obj)

    habitat_rows = [
        {
            "madin_id": habitat,
            "vocabulary": habitat.split(":", 1)[0],
            "label": labels.get(habitat, ""),
            "taxon_count": len(found),
        }
        for habitat, found in taxa.items()
    ]
    habitat_rows.sort(key=lambda r: (-r["taxon_count"], r["madin_id"]))

    taxa_rows = [
        {
            "madin_id": habitat,
            "taxon_id": taxon,
            "taxon_label": labels.get(taxon, ""),
            "corroborated_by": "",
        }
        for habitat in sorted(taxa)
        for taxon in sorted(taxa[habitat])
    ]
    return habitat_rows, taxa_rows, dict(taxa)


def _trim_unranked(
    taxa_rows: list[dict[str, Any]], key: str, limit: int
) -> list[dict[str, Any]]:
    """Cut an unranked source's taxon rows to `limit` per habitat.

    A source with no score still has to be cut down to what fits on a record,
    and the choice of which to keep is a real one. Corroborated pairs go first:
    "an independent source agrees" is the only quality signal available here,
    and it is the one #8 established as worth more than any single source's
    ranking. The rest fall back to taxon id, which is arbitrary but stable
    across runs — the corpus has to be byte-reproducible.
    """
    by_habitat: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in taxa_rows:
        by_habitat[row[key]].append(row)
    kept: list[dict[str, Any]] = []
    for habitat in sorted(by_habitat):
        rows = sorted(
            by_habitat[habitat],
            key=lambda r: (not r.get("corroborated_by"), r["taxon_id"]),
        )
        kept.extend(rows[:limit])
    return kept


def _load_taxon_labels(kgm: Path, wanted: set[str]) -> dict[str, str]:
    """Scientific names for the taxa we kept. One pass over kg-microbe's
    ~925k-row NCBITaxon node table, filtered to `wanted`, rather than loading
    the whole thing into memory for a few thousand lookups."""
    path = kgm / "data" / "transformed" / "ontologies" / "ncbitaxon_nodes.tsv"
    labels: dict[str, str] = {}
    if not wanted or not path.exists():
        return labels
    for row in read_tsv(path):
        node_id = row["id"]
        if node_id in wanted:
            labels[node_id] = (row.get("name") or "").strip()
            if len(labels) == len(wanted):
                break
    return labels


# ---------------------------------------------------------------------------
# Environment parameter table
# ---------------------------------------------------------------------------

def extract_environment_parameters(kgm: Path) -> list[dict[str, Any]]:
    """Normalise data/raw/environments.csv into a habitat-keyed parameter table.

    The upstream CSV is one row per environment type with a column per
    physicochemical axis and an ``ENVO_ids`` cell that may list several terms.
    "NA" is the upstream missing-value marker and is dropped rather than
    carried through as a literal parameter value.

    ``ENVO_ids`` is emitted here as ``term_ids``: despite the upstream name it
    is not ENVO-only. Compound environment types spell themselves out with a
    qualifier from another ontology — ``sediment_marine_cold`` is ENVO's marine
    sediment plus PATO:0001306 "cold", and ``milk`` is UBERON:0001913 — so a
    consumer that assumes the ENVO prefix will mis-handle 149 of these rows.
    """
    path = kgm / "data" / "raw" / "environments.csv"
    if not path.exists():
        raise FileNotFoundError(f"required source file not found: {path}")

    param_columns = [
        "Water",
        "water variability",
        "Nutrients",
        "Gradients",
        "Organic",
        "Structural",
        "Pressure",
        "Temperature",
        "temp variability",
        "Salinity",
        "salinity variability",
        "pH",
    ]

    rows: list[dict[str, Any]] = []
    with path.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            env_type = (row.get("Type") or "").strip()
            if not env_type:
                continue
            term_ids = [t.strip() for t in (row.get("ENVO_ids") or "").split(",") if t.strip()]
            term_labels = [t.strip() for t in (row.get("ENVO_terms") or "").split(",") if t.strip()]
            for column in param_columns:
                value = (row.get(column) or "").strip()
                if not value or value.upper() == "NA":
                    continue
                rows.append(
                    {
                        "env_type": env_type,
                        "main_group": (row.get("Main group") or "").strip(),
                        "cobo_simon_habitat": (row.get("Cobo-Simon habitat") or "").strip(),
                        "parameter": column,
                        "value": value,
                        "term_ids": "|".join(term_ids),
                        "term_labels": "|".join(term_labels),
                    }
                )
    rows.sort(key=lambda r: (r["main_group"], r["env_type"], r["parameter"]))
    return rows


# ---------------------------------------------------------------------------
# Curated isolation-source groundings
# ---------------------------------------------------------------------------

def extract_groundings(kgm: Path) -> list[dict[str, Any]]:
    path = kgm / "mappings" / "isolation_source_to_ontology.tsv"
    rows = []
    for row in read_tsv(path):
        rows.append(
            {
                "subject_label": row.get("subject_label", ""),
                "subject_label_normalized": row.get("subject_label_normalized", ""),
                "object_id": row.get("object_id", ""),
                "object_label": row.get("object_label", ""),
                "object_source": row.get("object_source", ""),
                "predicate_id": row.get("predicate_id", ""),
                "confidence": row.get("confidence", ""),
                "mapping_justification": row.get("mapping_justification", ""),
                "curator": row.get("curator", ""),
                "source_dataset": row.get("source_dataset", ""),
                "verified_date": row.get("verified_date", ""),
            }
        )
    rows.sort(key=lambda r: r["subject_label"])
    return rows


# ---------------------------------------------------------------------------
# Ontology term labels / definitions / hierarchy
# ---------------------------------------------------------------------------

def _load_tsv_ontology(kgm: Path, name: str) -> tuple[dict[str, dict[str, str]], list[tuple[str, str, str]]]:
    base = kgm / "data" / "transformed" / "ontologies"
    terms: dict[str, dict[str, str]] = {}
    prefix = name.upper() + ":"
    for row in read_tsv(base / f"{name}_nodes.tsv"):
        node_id = row["id"]
        if not node_id.startswith(prefix):
            continue
        terms[node_id] = {
            "label": (row.get("name") or "").strip(),
            "definition": (row.get("description") or "").strip(),
            "synonyms": (row.get("synonym") or "").strip(),
            "deprecated": (row.get("deprecated") or "").strip(),
        }
    edges: list[tuple[str, str, str]] = []
    for row in read_tsv(base / f"{name}_edges.tsv"):
        edges.append((row.get("subject", ""), row.get("predicate", ""), row.get("object", "")))
    return terms, edges


def _load_owl_ontology(
    path: Path, prefix: str
) -> tuple[dict[str, dict[str, str]], list[tuple[str, str, str]]]:
    """Labels/definitions/subclass edges from a plain RDF/XML OBO ontology.

    kg-microbe ships PO only as ``po.owl`` — there is no KGX node/edge pair for
    it — so it is parsed directly rather than skipped. Without PO, plant
    structure habitats ("Roots", "Seeds", "Phylloplane/Leaf") had no term to
    reach and were grounded to BTO equivalents as a workaround (#10).
    """
    if not path.exists():
        return {}, []
    ns = {
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "owl": "http://www.w3.org/2002/07/owl#",
        "obo": "http://purl.obolibrary.org/obo/",
        "oboInOwl": "http://www.geneontology.org/formats/oboInOwl#",
    }
    about = f"{{{ns['rdf']}}}about"
    resource = f"{{{ns['rdf']}}}resource"

    def curie(iri: str) -> str | None:
        if not iri or not iri.startswith(ns["obo"]):
            return None
        local = iri[len(ns["obo"]):]
        return local.replace("_", ":", 1) if "_" in local else None

    terms: dict[str, dict[str, str]] = {}
    edges: list[tuple[str, str, str]] = []
    for _, element in ET.iterparse(str(path), events=("end",)):
        if element.tag != f"{{{ns['owl']}}}Class":
            continue
        term_id = curie(element.get(about) or "")
        if term_id and term_id.startswith(prefix + ":"):
            label = element.findtext(f"{{{ns['rdfs']}}}label") or ""
            definition = element.findtext(f"{{{ns['obo']}}}IAO_0000115") or ""
            synonyms = [
                (e.text or "").strip()
                for tag in ("hasExactSynonym", "hasNarrowSynonym", "hasBroadSynonym",
                            "hasRelatedSynonym")
                for e in element.findall(f"{{{ns['oboInOwl']}}}{tag}")
            ]
            terms[term_id] = {
                "label": label.strip(),
                "definition": " ".join(definition.split()),
                "synonyms": "|".join(s for s in synonyms if s),
                "deprecated": "",
            }
            for parent in element.findall(f"{{{ns['rdfs']}}}subClassOf"):
                parent_id = curie(parent.get(resource) or "")
                if parent_id and parent_id.startswith(prefix + ":"):
                    edges.append((term_id, "biolink:subclass_of", parent_id))
        element.clear()
    return terms, edges


def _load_bto(kgm: Path) -> tuple[dict[str, dict[str, str]], list[tuple[str, str, str]]]:
    """BTO ships as a semsql SQLite build; read labels/definitions/subclass
    edges out of its generic ``statements`` table."""
    db_path = kgm / "data" / "raw" / "bto.db"
    if not db_path.exists():
        return {}, []
    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    try:
        terms: dict[str, dict[str, str]] = {}
        for subject, value in conn.execute(
            "SELECT subject, value FROM statements "
            "WHERE predicate = 'rdfs:label' AND subject LIKE 'BTO:%'"
        ):
            terms.setdefault(subject, {"label": "", "definition": "", "synonyms": "", "deprecated": ""})
            terms[subject]["label"] = value or ""
        for subject, value in conn.execute(
            "SELECT subject, value FROM statements "
            "WHERE predicate = 'IAO:0000115' AND subject LIKE 'BTO:%'"
        ):
            if subject in terms:
                terms[subject]["definition"] = value or ""
        edges = [
            (subject, "biolink:subclass_of", obj)
            for subject, obj in conn.execute(
                "SELECT subject, object FROM statements "
                "WHERE predicate = 'rdfs:subClassOf' AND subject LIKE 'BTO:%' "
                "AND object LIKE 'BTO:%'"
            )
        ]
        return terms, edges
    finally:
        conn.close()


def _reference_labels(kgm: Path, wanted: set[str]) -> dict[str, str]:
    """Labels for mapping targets that live outside the four vendored ontologies.

    The seeder verifies kg-microbe's isolation-source mappings by comparing the
    row's ``object_label`` against the ontology's own label, which is what stops
    a wrong id reaching a record (#39, and upstream kg-microbe#777). That check
    can only run on terms present in the vendored slice, so it silently did
    nothing for 87 of 283 mapping targets — including three that are wrong
    (#41):

        Nectar      CHEBI:50292     claims "nectar"        is cadmium sulfate
        Heavy-metal CHEBI:25555     claims "monoatomic ion" is nitrogen atom
        Tick        NCBITaxon:6939  claims "Ixodida"        is Ixodidae

    Only the referenced terms are pulled in — roughly ninety rows — not whole
    ontologies. NCBITaxon alone would be 925k. They are label-only: no ancestry,
    because nothing walks the hierarchy of a CHEBI or NCIT mapping target.

    Every source here is optional, so a missing file degrades to "unverifiable"
    rather than failing — which is the wrong default to leave silent, because it
    is indistinguishable from upstream simply not using that ontology. Anything
    unresolved is reported by prefix, naming the paths that were tried (#45).
    """
    found: dict[str, str] = {}
    remaining = set(wanted)
    tried: dict[str, list[Path]] = defaultdict(list)

    for name in ("chebi", "go", "pato", "ncbitaxon", "mondo", "upa", "ec", "hp"):
        path = kgm / "data" / "transformed" / "ontologies" / f"{name}_nodes.tsv"
        if not remaining:
            continue
        tried[name.upper()].append(path)
        if not path.exists():
            continue
        for row in read_tsv(path):
            if row["id"] in remaining and (row.get("name") or "").strip():
                found[row["id"]] = row["name"].strip()
                remaining.discard(row["id"])

    ncit_db = kgm / "data" / "raw" / "ncit.db"
    ncit_wanted = {t for t in remaining if t.startswith("NCIT:")}
    if ncit_wanted:
        tried["NCIT"].append(ncit_db)
    if ncit_wanted and ncit_db.exists():
        conn = sqlite3.connect(f"file:{ncit_db}?mode=ro", uri=True)
        try:
            placeholders = ",".join("?" * len(ncit_wanted))
            for subject, value in conn.execute(
                f"SELECT subject, value FROM statements WHERE predicate = 'rdfs:label' "
                f"AND subject IN ({placeholders})",
                sorted(ncit_wanted),
            ):
                if value:
                    found[subject] = value.strip()
                    remaining.discard(subject)
        finally:
            conn.close()

    # The dump is named for its release — mesh2026.nt.gz — so pinning the year
    # would quietly stop finding anything the next time MeSH is refreshed.
    mesh_dumps = sorted((kgm / "data" / "raw").glob("mesh*.nt.gz"))
    mesh_wanted = {t for t in remaining if t.startswith("mesh:")}
    if mesh_wanted:
        tried["MESH"].extend(mesh_dumps or [kgm / "data" / "raw" / "mesh*.nt.gz"])
    if mesh_wanted and mesh_dumps:
        locals_ = {t.split(":", 1)[1]: t for t in mesh_wanted}
        # MeSH URIs carry the release year too: .../mesh/2026/D000038. Labels
        # are language-tagged literals.
        pattern = re.compile(
            r"<http://id\.nlm\.nih\.gov/mesh/(?:\d{4}/)?([^>]+)>\s+"
            r"<http://www\.w3\.org/2000/01/rdf-schema#label>\s+\"([^\"]+)\""
        )
        with gzip.open(mesh_dumps[-1], "rt", encoding="utf-8", errors="replace") as fh:
            for line in fh:
                match = pattern.match(line)
                if match and match.group(1) in locals_:
                    found[locals_[match.group(1)]] = match.group(2).strip()
                    remaining.discard(locals_[match.group(1)])
                    if not {t for t in remaining if t.startswith("mesh:")}:
                        break

    # A prefix we looked for and could not find a file for is a local
    # misconfiguration; one we never had a source for is an upstream fact. Only
    # the first is actionable, so only the first is a WARNING.
    for prefix, unresolved in sorted(_by_prefix(remaining).items()):
        missing = [p for p in tried.get(prefix.upper(), ()) if not p.exists()]
        if missing:
            print(
                f"  WARNING: {len(unresolved)} {prefix} mapping target(s) unresolved; "
                f"expected {', '.join(str(p) for p in missing)} — the seeder cannot "
                "label-check them (#45)"
            )
    unsourced = {t for t in remaining if t.split(":", 1)[0].upper() not in tried}
    if unsourced:
        prefixes = ", ".join(sorted(_by_prefix(unsourced)))
        print(
            f"  NOTE: {len(unsourced)} mapping target(s) have no label available "
            f"({prefixes}), so the seeder cannot check them; `just report` lists them"
        )
    return found


def _by_prefix(terms: set[str]) -> dict[str, set[str]]:
    out: dict[str, set[str]] = defaultdict(set)
    for term in terms:
        out[term.split(":", 1)[0]].add(term)
    return out


def _norm_label(text: str) -> str:
    """Fold a label to a lexical-matching key: lowercase, non-alphanumerics to
    single spaces. Deliberately aggressive so GOLD's "Rock-dwelling (endoliths)"
    and BacDive's "Animal-habitation-Nest,Burrow" can meet an ontology label."""
    return re.sub(r"[^a-z0-9]+", " ", (text or "").lower()).strip()


def extract_ontology_terms(
    kgm: Path, referenced: set[str], source_labels: set[str]
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Emit the ontology slice HabitatMech actually needs.

    Three things go in, plus the subclass ancestors of all of them so the
    hierarchy in data/raw is self-contained:

    * every term anything in the source inventories already grounds to;
    * ENVO and BTO *in full* — ENVO is the habitat ontology and BTO is what
      PREGO speaks, both are small (~6.5k terms each), and the seeder's lexical
      grounding is only as good as the label pool it can search. An earlier cut
      kept referenced-terms-only and grounded just a third of GOLD, because the
      terms GOLD's labels would have matched were never in the slice;
    * UBERON and FOODON terms whose label or synonym matches a source label —
      those two are large (25k / 39k) and mostly irrelevant here, so they come
      in by need rather than wholesale.
    """
    all_terms: dict[str, dict[str, str]] = {}
    all_edges: list[tuple[str, str, str]] = []
    for name in TSV_ONTOLOGIES:
        terms, edges = _load_tsv_ontology(kgm, name)
        all_terms.update(terms)
        all_edges.extend(edges)
    bto_terms, bto_edges = _load_bto(kgm)
    all_terms.update(bto_terms)
    all_edges.extend(bto_edges)
    po_terms, po_edges = _load_owl_ontology(kgm / "data" / "raw" / "po.owl", "PO")
    all_terms.update(po_terms)
    all_edges.extend(po_edges)

    parents: dict[str, set[str]] = defaultdict(set)
    for subj, pred, obj in all_edges:
        if pred in ("biolink:subclass_of", "rdfs:subClassOf") and subj in all_terms:
            parents[subj].add(obj)

    seeds: set[str] = {t for t in referenced if t in all_terms}
    # ENVO and BTO in full.
    # ENVO, BTO and PO in full: each is small (~4-7k terms) and each is a
    # vocabulary a habitat can legitimately BE.
    seeds |= {t for t in all_terms if t.startswith(("ENVO:", "BTO:", "PO:"))}
    # UBERON / FOODON by lexical need.
    if source_labels:
        for term_id, meta in all_terms.items():
            if not term_id.startswith(("UBERON:", "FOODON:")) or term_id in seeds:
                continue
            keys = {_norm_label(meta["label"])}
            keys.update(_norm_label(s) for s in (meta["synonyms"] or "").split("|"))
            if keys & source_labels:
                seeds.add(term_id)

    # Transitive closure over the seeds, so every kept term's ancestry is
    # present and the hierarchy in data/raw is self-contained.
    keep: set[str] = set()
    frontier = set(seeds)
    while frontier:
        node = frontier.pop()
        if node in keep:
            continue
        keep.add(node)
        frontier |= {p for p in parents.get(node, ()) if p in all_terms and p not in keep}

    term_rows = [
        {
            "term_id": term_id,
            "ontology": term_id.split(":", 1)[0],
            "label": all_terms[term_id]["label"],
            "definition": all_terms[term_id]["definition"],
            "synonyms": all_terms[term_id]["synonyms"],
            "deprecated": all_terms[term_id]["deprecated"],
            "directly_referenced": "TRUE" if term_id in referenced else "FALSE",
        }
        for term_id in sorted(keep)
    ]
    edge_rows = [
        {"subject": subj, "predicate": "rdfs:subClassOf", "object": obj}
        for subj in sorted(keep)
        for obj in sorted(parents.get(subj, ()))
        if obj in keep
    ]
    # Mapping targets outside the four vendored ontologies, label-only. Without
    # them the seeder's label check silently passes on 87 of 283 targets (#41).
    extra = _reference_labels(kgm, {t for t in referenced if t not in keep})
    term_rows.extend(
        {
            "term_id": term_id,
            "ontology": term_id.split(":", 1)[0],
            "label": label,
            "definition": "",
            "synonyms": "",
            "deprecated": "",
            "directly_referenced": "TRUE",
        }
        for term_id, label in sorted(extra.items())
    )
    term_rows.sort(key=lambda r: r["term_id"])
    return term_rows, edge_rows


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------

def _describe_source(kgm: Path) -> str:
    """Identify the kg-microbe checkout in a machine-independent way.

    The absolute path is useless to anyone else and leaks a contributor's
    local layout into a public repo. The git commit is what actually pins
    which release of the sources the inventories came from; the per-input
    sha256s below cover the rest.
    """
    try:
        result = subprocess.run(
            ["git", "-C", str(kgm), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
        if result.returncode == 0 and result.stdout.strip():
            return f"kg-microbe@{result.stdout.strip()}"
    except (OSError, subprocess.SubprocessError):
        pass
    return f"{kgm.name} (not a git checkout; commit unknown)"


def _utc_now_iso() -> str:
    now = datetime.datetime.now(datetime.timezone.utc)
    return now.isoformat(timespec="seconds").replace("+00:00", "Z")


def build_manifest(
    kgm: Path,
    inputs: list[Path],
    outputs: dict[str, int],
    *,
    hash_inputs: bool,
    gold_truncated_paths: int = 0,
) -> str:
    lines = [
        "# Provenance for the inventories in data/raw/.",
        "# Regenerate with: just extract-inventory",
        "# Emitted by scripts/extract_source_inventory.py — do not hand-edit.",
        f"extracted_at: '{_utc_now_iso()}'",
        f"kg_microbe_source: {_describe_source(kgm)}",
        # A non-zero count means GOLD's parent chain contained a cycle and some
        # canonical paths are truncated — see the extractor's WARNING output.
        f"gold_truncated_paths: {gold_truncated_paths}",
        "inputs:",
    ]
    for path in inputs:
        stat = path.stat()
        mtime = datetime.datetime.fromtimestamp(stat.st_mtime, datetime.timezone.utc)
        lines.append(f"  - path: {path.relative_to(kgm)}")
        lines.append(f"    bytes: {stat.st_size}")
        stamp = mtime.isoformat(timespec="seconds").replace("+00:00", "Z")
        lines.append(f"    mtime: '{stamp}'")
        # Say that hashing was skipped rather than omitting the key. A manifest
        # with no sha256 anywhere is otherwise indistinguishable from an older
        # format or a bug, and the provenance claim quietly weakens (#44).
        lines.append(f"    sha256: {sha256_of(path) if hash_inputs else 'skipped (--no-hash)'}")
    lines.append("outputs:")
    for name, count in sorted(outputs.items()):
        lines.append(f"  - path: {name}")
        lines.append(f"    rows: {count}")
    return "\n".join(lines) + "\n"


def default_kg_microbe_root() -> Path | None:
    env = os.environ.get("KG_MICROBE_ROOT")
    if env:
        return Path(env).expanduser()
    if CONF_PATH.exists():
        for line in CONF_PATH.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("kg_microbe_root:"):
                value = line.split(":", 1)[1].strip().strip("'\"")
                if value:
                    return Path(value).expanduser()
    return None


def main(argv: list[str] | None = None) -> int:
    _raise_csv_limit()
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--kg-microbe",
        type=Path,
        default=default_kg_microbe_root(),
        help="Path to a kg-microbe checkout (default: KG_MICROBE_ROOT env var, "
        "else kg_microbe_root in conf/sources.yaml).",
    )
    parser.add_argument("--out", type=Path, default=RAW_DIR, help="Output directory (default: data/raw).")
    parser.add_argument("--dry-run", action="store_true", help="Report counts without writing files.")
    parser.add_argument("--no-hash", action="store_true", help="Skip sha256 of inputs in the manifest.")
    parser.add_argument(
        "--top-taxa",
        type=int,
        default=25,
        help="Per-habitat cap on PREGO taxon associations kept (default: 25). "
        "The untruncated total stays in prego_habitats.taxon_count.",
    )
    args = parser.parse_args(argv)

    if args.kg_microbe is None:
        parser.error("no kg-microbe path: pass --kg-microbe, set KG_MICROBE_ROOT, or fill conf/sources.yaml")
    kgm: Path = args.kg_microbe.resolve()
    if not kgm.is_dir():
        parser.error(f"kg-microbe path is not a directory: {kgm}")

    print(f"kg-microbe root: {kgm}")

    print("extracting GOLD ecosystem paths ...")
    gold_rows, gold_truncated = extract_gold(kgm)
    print(f"  {len(gold_rows)} distinct GOLD ecosystem concepts")
    if gold_truncated:
        print(
            f"  WARNING: {len(gold_truncated)} ecosystem node(s) hit a cycle in the "
            f"GOLD parent chain and have TRUNCATED paths, e.g. {gold_truncated[:3]}. "
            "Their depth and minted identifiers are unreliable."
        )

    print("extracting BacDive isolation sources ...")
    bacdive_rows, bacdive_taxa_rows, bacdive_full = extract_bacdive(kgm, args.top_taxa)
    print(f"  {len(bacdive_rows)} isolation sources, {len(bacdive_taxa_rows)} top-taxa rows")

    print("extracting PREGO habitats ...")
    prego_rows, prego_taxa_rows, prego_full = extract_prego(kgm, args.top_taxa)
    print(f"  {len(prego_rows)} PREGO habitat terms, {len(prego_taxa_rows)} top-taxa rows")

    print("extracting Madin et al. habitat associations ...")
    madin_rows, madin_taxa_rows, madin_full = extract_madin(kgm)
    print(f"  {len(madin_rows)} Madin habitats, {len(madin_taxa_rows)} habitat-taxon pairs")

    print("extracting environment parameter table ...")
    param_rows = extract_environment_parameters(kgm)
    print(f"  {len(param_rows)} parameter assertions")

    print("extracting curated isolation-source groundings ...")
    grounding_rows = extract_groundings(kgm)
    print(f"  {len(grounding_rows)} mapping rows")

    # Cross-source corroboration. PREGO reaches taxa by text mining and genome
    # annotation, BacDive by counting strains actually isolated, so agreement
    # between them is not one method agreeing with itself — it is the strongest
    # evidence available for a taxon-habitat pair (#8).
    #
    # The comparison has to run against each source's FULL taxon set, which only
    # exists here: intersecting the two truncated top-N lists finds almost
    # nothing, because they rank different things out of pools of very different
    # size. Habitats are linked through kg-microbe's isolation-source mapping,
    # which is the same table the seeder grounds BacDive with.
    print("computing cross-source taxon corroboration ...")
    bacdive_target = {
        _norm_label(row["subject_label"]): row["object_id"]
        for row in grounding_rows
        if row["object_id"]
    }

    # Every source's habitats reduced to one shared key so their taxon sets can
    # be compared. PREGO and Madin already use ontology CURIEs; BacDive reaches
    # one through the isolation-source mapping, which is the same table the
    # seeder grounds it with. Madin's own bacdive.isolation_source: subjects key
    # directly on the BacDive id, so they line up without going through an
    # ontology term at all.
    per_source: dict[str, dict[str, set[str]]] = {
        "PREGO": {},
        "BACDIVE": {},
        "MADIN": {},
    }
    local_key: dict[str, dict[str, str]] = {"PREGO": {}, "BACDIVE": {}, "MADIN": {}}
    for prego_id, found in prego_full.items():
        per_source["PREGO"].setdefault(prego_id, set()).update(found)
        local_key["PREGO"][prego_id] = prego_id
    for bacdive_row in bacdive_rows:
        bacdive_id = bacdive_row["bacdive_id"]
        key = bacdive_target.get(_norm_label(bacdive_row["label"])) or bacdive_id
        per_source["BACDIVE"].setdefault(key, set()).update(bacdive_full.get(bacdive_id, set()))
        local_key["BACDIVE"][bacdive_id] = key
    for madin_id, found in madin_full.items():
        key = madin_id
        if madin_id.startswith("bacdive.isolation_source:"):
            # Madin points at the BacDive vocabulary directly; route it through
            # the same mapping so it meets BacDive and PREGO on one key.
            key = bacdive_target.get(_norm_label(madin_id.split(":", 1)[1])) or madin_id
        per_source["MADIN"].setdefault(key, set()).update(found)
        local_key["MADIN"][madin_id] = key

    # For each source, which taxa at each habitat some OTHER source also
    # asserts, and which sources those were.
    agrees: dict[str, dict[str, dict[str, set[str]]]] = {
        source: defaultdict(lambda: defaultdict(set)) for source in per_source
    }
    multi_source_habitats = 0
    keys = {k for source in per_source.values() for k in source}
    for key in keys:
        present = [s for s in per_source if key in per_source[s]]
        if len(present) < 2:
            continue
        multi_source_habitats += 1
        for source in present:
            for other in present:
                if other == source:
                    continue
                for taxon in per_source[source][key] & per_source[other][key]:
                    agrees[source][key][taxon].add(other)

    def _mark(rows: list[dict[str, Any]], source: str, id_column: str) -> None:
        for row in rows:
            key = local_key[source].get(row[id_column])
            others = agrees[source].get(key, {}).get(row["taxon_id"]) if key else None
            if others:
                row["corroborated_by"] = "|".join(sorted(others))

    _mark(prego_taxa_rows, "PREGO", "prego_id")
    _mark(bacdive_taxa_rows, "BACDIVE", "bacdive_id")
    _mark(madin_taxa_rows, "MADIN", "madin_id")

    # Madin has no score, so its trim runs here — after corroboration, which is
    # the only signal available to choose by (#40).
    madin_taxa_rows = _trim_unranked(madin_taxa_rows, "madin_id", args.top_taxa)

    corroborated = sum(
        1
        for r in (*prego_taxa_rows, *bacdive_taxa_rows, *madin_taxa_rows)
        if r.get("corroborated_by")
    )
    print(
        f"  {multi_source_habitats} habitats attested by more than one source; "
        f"{corroborated} kept taxa corroborated"
    )

    referenced: set[str] = set()
    for row in grounding_rows:
        if row["object_id"]:
            referenced.add(row["object_id"])
    for row in prego_rows:
        referenced.add(row["prego_id"])
    for row in madin_rows:
        # Madin habitats are already CURIEs, so they need vendoring the same
        # way PREGO's do — otherwise a Madin-only habitat has no label (#40).
        if ":" in row["madin_id"] and not row["madin_id"].startswith("bacdive."):
            referenced.add(row["madin_id"])
    for row in param_rows:
        referenced.update(t for t in row["term_ids"].split("|") if t)

    # Label pool the seeder will try to ground lexically — used to decide which
    # UBERON/FOODON terms are worth vendoring.
    source_labels: set[str] = set()
    for row in gold_rows:
        levels = [row[lvl] for lvl in GOLD_LEVELS if row[lvl]]
        if levels:
            source_labels.add(_norm_label(levels[-1]))
            if len(levels) >= 2:
                source_labels.add(_norm_label(" ".join(levels[-2:])))
    for row in bacdive_rows:
        source_labels.add(_norm_label(row["label"]))
        source_labels.add(_norm_label(row["label"].replace("-", " ")))
    source_labels.discard("")

    print("extracting ontology term slice ...")
    term_rows, edge_rows = extract_ontology_terms(kgm, referenced, source_labels)
    print(
        f"  {len(term_rows)} terms ({len(referenced)} directly referenced), "
        f"{len(edge_rows)} subclass edges"
    )

    outputs = {
        "gold_ecosystem_paths.tsv": (
            [
                "canonical_path",
                *GOLD_LEVELS,
                "leaf_label",
                "depth",
                "gold_node_count",
                "organism_count",
                "study_count",
                "biosample_count",
                "total_assertions",
                "gold_node_ids",
            ],
            gold_rows,
        ),
        "bacdive_isolation_sources.tsv": (
            ["bacdive_id", "label", "source_slug", "strain_count", "taxon_count"],
            bacdive_rows,
        ),
        "prego_habitats.tsv": (
            [
                "prego_id",
                "ontology",
                "biolink_category",
                "taxon_count",
                "direct_assertion_count",
                "max_prego_score",
                "channels",
                "prego_synonyms",
            ],
            prego_rows,
        ),
        "bacdive_source_taxa.tsv": (
            ["bacdive_id", "rank", "taxon_id", "taxon_label", "strain_count", "corroborated_by"],
            bacdive_taxa_rows,
        ),
        "prego_habitat_taxa.tsv": (
            ["prego_id", "rank", "taxon_id", "taxon_label", "prego_score", "direct_flag",
             "channels", "corroborated_by"],
            prego_taxa_rows,
        ),
        "madin_habitats.tsv": (
            ["madin_id", "vocabulary", "label", "taxon_count"],
            madin_rows,
        ),
        # No rank and no score columns on purpose: Madin supplies neither, and a
        # rank column filled with the sort order would read as one.
        "madin_habitat_taxa.tsv": (
            ["madin_id", "taxon_id", "taxon_label", "corroborated_by"],
            madin_taxa_rows,
        ),
        "environment_parameters.tsv": (
            ["main_group", "env_type", "cobo_simon_habitat", "parameter", "value", "term_ids", "term_labels"],
            param_rows,
        ),
        "isolation_source_groundings.tsv": (
            [
                "subject_label",
                "subject_label_normalized",
                "object_id",
                "object_label",
                "object_source",
                "predicate_id",
                "confidence",
                "mapping_justification",
                "curator",
                "source_dataset",
                "verified_date",
            ],
            grounding_rows,
        ),
        "ontology_terms.tsv": (
            ["term_id", "ontology", "label", "definition", "synonyms", "deprecated", "directly_referenced"],
            term_rows,
        ),
        "ontology_subclass_edges.tsv": (["subject", "predicate", "object"], edge_rows),
    }

    if args.dry_run:
        print("\n--dry-run: no files written")
        for name, (_, rows) in outputs.items():
            print(f"  would write {args.out / name}: {len(rows)} rows")
        return 0

    for name, (fields, rows) in outputs.items():
        write_tsv(args.out / name, fields, rows)
        print(f"wrote {args.out / name} ({len(rows)} rows)")

    manifest_inputs = [
        kgm / "data" / "raw" / "gold" / "GOLD_nodes.tsv",
        kgm / "data" / "raw" / "gold" / "GOLD_edges.tsv",
        kgm / "data" / "transformed" / "bacdive" / "nodes.tsv",
        kgm / "data" / "transformed" / "bacdive" / "edges.tsv",
        kgm / "data" / "transformed" / "prego" / "nodes.tsv",
        kgm / "data" / "transformed" / "prego" / "edges.tsv",
        kgm / "data" / "transformed" / "madin_etal" / "nodes.tsv",
        kgm / "data" / "transformed" / "madin_etal" / "edges.tsv",
        kgm / "data" / "raw" / "environments.csv",
        kgm / "mappings" / "isolation_source_to_ontology.tsv",
    ]
    manifest = build_manifest(
        kgm,
        [p for p in manifest_inputs if p.exists()],
        {name: len(rows) for name, (_, rows) in outputs.items()},
        hash_inputs=not args.no_hash,
        gold_truncated_paths=len(gold_truncated),
    )
    (args.out / "MANIFEST.yaml").write_text(manifest, encoding="utf-8")
    print(f"wrote {args.out / 'MANIFEST.yaml'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
