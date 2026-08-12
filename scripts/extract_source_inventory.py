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
import hashlib
import os
import re
import sqlite3
import subprocess
import sys
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
    # occurrence counts, split by the GOLD id class of the asserting subject
    # (Go = organism, Gs = study, Gb = biosample, Ga = analysis project).
    counts: dict[str, Counter] = defaultdict(Counter)
    for row in read_tsv(edges_path):
        pred = row.get("predicate")
        subj, obj = row.get("subject", ""), row.get("object", "")
        if pred == "biolink:subclass_of" and subj.startswith("gold.ecosystem:"):
            parent[subj] = obj
        elif pred == "biolink:occurs_in" and obj.startswith("gold.ecosystem:"):
            local = subj.split(":", 1)[-1]
            kind = local[:2] if local[:1] == "G" else "other"
            counts[obj][kind] += 1

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

def extract_bacdive(kgm: Path) -> list[dict[str, Any]]:
    nodes_path = kgm / "data" / "transformed" / "bacdive" / "nodes.tsv"
    edges_path = kgm / "data" / "transformed" / "bacdive" / "edges.tsv"

    sources: dict[str, str] = {}
    for row in read_tsv(nodes_path):
        if row["id"].startswith("bacdive.isolation_source:"):
            sources[row["id"]] = (row.get("name") or "").strip()

    strain_counts: Counter = Counter()
    for row in read_tsv(edges_path):
        subj = row.get("subject", "")
        if subj.startswith("bacdive.isolation_source:"):
            strain_counts[subj] += 1

    rows = [
        {
            "bacdive_id": src_id,
            "label": label,
            "source_slug": src_id.split(":", 1)[-1],
            "strain_count": strain_counts.get(src_id, 0),
        }
        for src_id, label in sources.items()
    ]
    rows.sort(key=lambda r: (-r["strain_count"], r["label"]))
    return rows


# ---------------------------------------------------------------------------
# PREGO habitats
# ---------------------------------------------------------------------------

def extract_prego(kgm: Path, top_taxa: int) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
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
    return habitat_rows, taxa_rows


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

    parents: dict[str, set[str]] = defaultdict(set)
    for subj, pred, obj in all_edges:
        if pred in ("biolink:subclass_of", "rdfs:subClassOf") and subj in all_terms:
            parents[subj].add(obj)

    seeds: set[str] = {t for t in referenced if t in all_terms}
    # ENVO and BTO in full.
    seeds |= {t for t in all_terms if t.startswith(("ENVO:", "BTO:"))}
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
        if hash_inputs:
            lines.append(f"    sha256: {sha256_of(path)}")
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
    bacdive_rows = extract_bacdive(kgm)
    print(f"  {len(bacdive_rows)} isolation sources")

    print("extracting PREGO habitats ...")
    prego_rows, prego_taxa_rows = extract_prego(kgm, args.top_taxa)
    print(f"  {len(prego_rows)} PREGO habitat terms, {len(prego_taxa_rows)} top-taxa rows")

    print("extracting environment parameter table ...")
    param_rows = extract_environment_parameters(kgm)
    print(f"  {len(param_rows)} parameter assertions")

    print("extracting curated isolation-source groundings ...")
    grounding_rows = extract_groundings(kgm)
    print(f"  {len(grounding_rows)} mapping rows")

    referenced: set[str] = set()
    for row in grounding_rows:
        if row["object_id"]:
            referenced.add(row["object_id"])
    for row in prego_rows:
        referenced.add(row["prego_id"])
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
            ["bacdive_id", "label", "source_slug", "strain_count"],
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
        "prego_habitat_taxa.tsv": (
            ["prego_id", "rank", "taxon_id", "taxon_label", "prego_score", "direct_flag", "channels"],
            prego_taxa_rows,
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
