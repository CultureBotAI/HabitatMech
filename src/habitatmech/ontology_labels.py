"""Replay a reviewed, source-verified label refresh without refreshing other axioms.

The kg-microbe inventory remains the source of definitions, synonyms and edges.
This deliberately narrow operation is not a general ontology migration: any
changed concept scope must be assessed separately in curation/decisions.tsv.
"""

from __future__ import annotations

import copy
import datetime
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
PLAN_PATH = ROOT / "conf" / "ontology_label_refresh.yaml"
RECEIPT_PATH = ROOT / "data" / "ontology_label_refresh.json"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
RDFS = "{http://www.w3.org/2000/01/rdf-schema#}"
OWL = "{http://www.w3.org/2002/07/owl#}"
XML = "{http://www.w3.org/XML/1998/namespace}"


def load_plan(path: Path = PLAN_PATH) -> dict:
    plan = yaml.safe_load(path.read_text(encoding="utf-8"))
    required = {"version", "source_url", "source_sha256", "reviewed_date", "terms"}
    if not isinstance(plan, dict) or set(plan) != required or plan["version"] != 1:
        raise ValueError("invalid ontology label refresh plan")
    if not re.fullmatch(
        r"https://raw\.githubusercontent\.com/[^/]+/[^/]+/[0-9a-f]{40}/[^?#]+\.owl",
        str(plan["source_url"]),
    ):
        raise ValueError("ontology label source must be commit-pinned RDF/XML")
    if not re.fullmatch(r"[0-9a-f]{64}", str(plan["source_sha256"])):
        raise ValueError("ontology label source needs a SHA256")
    datetime.date.fromisoformat(str(plan["reviewed_date"]))
    if not isinstance(plan["terms"], dict) or not plan["terms"]:
        raise ValueError("ontology label refresh must name terms")
    for term_id, labels in plan["terms"].items():
        if not re.fullmatch(r"[A-Z][A-Z0-9]*:[0-9]+", term_id):
            raise ValueError(f"invalid ontology label term: {term_id}")
        if not isinstance(labels, dict) or set(labels) != {"previous_label", "label"}:
            raise ValueError(f"invalid ontology label fields: {term_id}")
        if any(not isinstance(s, str) or not s.strip() or s != s.strip()
               or any(c in s for c in "\r\n\t") for s in labels.values()):
            raise ValueError(f"invalid ontology label text: {term_id}")
        if labels["previous_label"] == labels["label"]:
            raise ValueError(f"unchanged ontology label: {term_id}")
    return plan


def source_labels(source: Path, plan: dict) -> dict[str, str]:
    digest = hashlib.sha256()
    with source.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    if digest.hexdigest() != plan["source_sha256"]:
        raise ValueError("ontology label source SHA256 mismatch")
    wanted = {
        "http://purl.obolibrary.org/obo/" + term.replace(":", "_"): term
        for term in plan["terms"]
    }
    labels: dict[str, set[str]] = {term: set() for term in wanted.values()}
    # Keep a complete top-level class, including restrictions, until inspected.
    depth = 0
    for event, element in ET.iterparse(source, events=("start", "end")):
        if event == "start":
            depth += 1
            continue
        if depth == 2:
            term = wanted.get(element.get(RDF + "about", ""))
            if term and element.tag in {OWL + "Class", RDF + "Description"}:
                if any((e.text or "").strip().lower() in {"true", "1"}
                       for e in element.findall(OWL + "deprecated")):
                    raise ValueError(f"cannot refresh an obsolete term: {term}")
                labels[term].update(
                    e.text.strip() for e in element.findall(RDFS + "label")
                    if e.text and e.get(XML + "lang", "") in {"", "en"}
                )
            element.clear()
        depth -= 1
    result = {}
    for term, found in labels.items():
        if found != {plan["terms"][term]["label"]}:
            raise ValueError(f"source label mismatch for {term}: {sorted(found)}")
        result[term] = next(iter(found))
    return result


def make_receipt(source: Path, plan: dict) -> dict:
    labels = source_labels(source, plan)
    return {
        "version": 1,
        "generator": "scripts/refresh_ontology_labels.py",
        "scope": "rdfs:label only; other ontology fields retain their original snapshot",
        "source_url": plan["source_url"],
        "source_sha256": plan["source_sha256"],
        "source_bytes": source.stat().st_size,
        "reviewed_date": plan["reviewed_date"],
        "terms": {term: {**plan["terms"][term], "label": labels[term]}
                  for term in sorted(labels)},
    }


def load_receipt(path: Path = RECEIPT_PATH, plan_path: Path = PLAN_PATH) -> dict:
    plan = load_plan(plan_path)
    receipt = json.loads(path.read_text(encoding="utf-8"))
    required = {
        "version", "generator", "scope", "source_url", "source_sha256",
        "source_bytes", "reviewed_date", "terms",
    }
    if not isinstance(receipt, dict) or set(receipt) != required:
        raise ValueError("invalid ontology label receipt fields")
    for key in ("version", "source_url", "source_sha256", "reviewed_date", "terms"):
        if receipt[key] != plan[key]:
            raise ValueError(f"ontology label receipt disagrees with plan: {key}")
    if receipt["generator"] != "scripts/refresh_ontology_labels.py":
        raise ValueError("invalid ontology label generator")
    if receipt["scope"] != (
        "rdfs:label only; other ontology fields retain their original snapshot"
    ):
        raise ValueError("invalid ontology label refresh scope")
    if type(receipt["source_bytes"]) is not int or receipt["source_bytes"] <= 0:
        raise ValueError("invalid ontology label source size")
    return receipt


def apply_label_refresh(terms: list[dict[str, str]], receipt: dict) -> list[dict[str, str]]:
    result = copy.deepcopy(terms)
    seen = set()
    for row in result:
        term = row["term_id"]
        if term not in receipt["terms"]:
            continue
        if term in seen:
            raise ValueError(f"duplicate ontology label target: {term}")
        seen.add(term)
        labels = receipt["terms"][term]
        if row["label"] not in {labels["previous_label"], labels["label"]}:
            raise ValueError(f"ontology label target drifted: {term}: {row['label']}")
        row["label"] = labels["label"]
    missing = receipt["terms"].keys() - seen
    if missing:
        raise ValueError(f"ontology label targets missing: {sorted(missing)}")
    return result
