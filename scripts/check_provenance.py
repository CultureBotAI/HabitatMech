#!/usr/bin/env python3
"""Verify hashes and coverage for every committed data/raw TSV inventory."""

from __future__ import annotations

import csv
import hashlib
import re
import subprocess
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = REPO_ROOT / "data" / "raw"
KG_MANIFEST = RAW_DIR / "MANIFEST.yaml"
GOLD_MANIFEST = RAW_DIR / "GOLD_MANIFEST.yaml"
SHA256_RE = re.compile(r"[0-9a-f]{64}")
COMMIT_RE = re.compile(r"[0-9a-f]{40}")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def tsv_rows(path: Path) -> int:
    with path.open(newline="", encoding="utf-8") as fh:
        return sum(1 for _row in csv.reader(fh, delimiter="\t")) - 1


def load_manifests() -> tuple[dict, dict]:
    kg = yaml.safe_load(KG_MANIFEST.read_text(encoding="utf-8"))
    gold = yaml.safe_load(GOLD_MANIFEST.read_text(encoding="utf-8"))
    return kg, gold


def combined_outputs(kg: dict, gold: dict) -> dict[str, dict]:
    outputs = {entry["path"]: entry for entry in kg.get("outputs", [])}
    for entry in gold.get("outputs", []):
        if entry["path"] in outputs:
            raise ValueError(f"inventory appears in two manifests: {entry['path']}")
        outputs[entry["path"]] = entry
    return outputs


def _missing(entry: dict, fields: tuple[str, ...]) -> list[str]:
    return [field for field in fields if entry.get(field) in (None, "")]


def manifest_contract_problems(kg: dict, gold: dict) -> list[str]:
    """Reject metadata deletion before optional-looking checks weaken QC."""
    failures = []
    if gold.get("manifest_version") != 1:
        failures.append("GOLD manifest: manifest_version must be 1")
    if not COMMIT_RE.fullmatch(str(gold.get("pipeline_commit", ""))):
        failures.append("GOLD manifest: pipeline_commit must be a 40-character commit hash")

    kg_paths = []
    for entry in kg.get("outputs", []):
        missing = _missing(entry, ("path", "rows"))
        if missing:
            label = entry.get("path", "<unnamed>")
            failures.append(f"kg-microbe output {label}: missing {', '.join(missing)}")
        if entry.get("path"):
            kg_paths.append(entry["path"])
    if len(kg_paths) != len(set(kg_paths)):
        failures.append("kg-microbe manifest: duplicate output paths")

    source_names = set()
    for source in gold.get("sources", []):
        label = source.get("name", "<unnamed>")
        missing = _missing(
            source,
            ("name", "kind", "location", "local_name", "retrieved_at", "bytes", "sha256"),
        )
        if missing:
            failures.append(f"GOLD source {label}: missing {', '.join(missing)}")
        if source.get("committed") is not False:
            failures.append(f"GOLD source {label}: committed must be false")
        if not SHA256_RE.fullmatch(str(source.get("sha256", ""))):
            failures.append(f"GOLD source {label}: sha256 must be 64 lowercase hexadecimal characters")
        if source.get("kind") == "api_sweep":
            scope = source.get("query_scope") or {}
            scope_missing = _missing(
                scope,
                ("route", "studies_requested", "unique_biosamples_returned", "complete_triads"),
            )
            if scope_missing:
                failures.append(f"GOLD source {label}: query_scope missing {', '.join(scope_missing)}")
            if not source.get("authentication"):
                failures.append(f"GOLD source {label}: missing authentication handling note")
        if source.get("local_name"):
            source_names.add(source["local_name"])

    gold_paths = []
    required_output = ("path", "generator", "source", "bytes", "rows", "sha256")
    for entry in gold.get("outputs", []):
        label = entry.get("path", "<unnamed>")
        missing = _missing(entry, required_output)
        if missing:
            failures.append(f"GOLD output {label}: missing {', '.join(missing)}")
        if entry.get("source") and entry["source"] not in source_names:
            failures.append(f"GOLD output {label}: unknown source {entry['source']}")
        if entry.get("generator") and not (REPO_ROOT / entry["generator"]).is_file():
            failures.append(f"GOLD output {label}: generator does not exist: {entry['generator']}")
        if not SHA256_RE.fullmatch(str(entry.get("sha256", ""))):
            failures.append(f"GOLD output {label}: sha256 must be 64 lowercase hexadecimal characters")
        if entry.get("path"):
            gold_paths.append(entry["path"])
    if len(gold_paths) != len(set(gold_paths)):
        failures.append("GOLD manifest: duplicate output paths")
    return failures


def tracked_raw_tsvs() -> set[str]:
    completed = subprocess.run(
        ["git", "ls-files", "--", "data/raw/*.tsv"],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return {Path(line).name for line in completed.stdout.splitlines() if line}


def problems() -> list[str]:
    kg, gold = load_manifests()
    failures = manifest_contract_problems(kg, gold)
    outputs = combined_outputs(kg, gold)
    tracked = tracked_raw_tsvs()
    uncovered = sorted(tracked - outputs.keys())
    stale = sorted(outputs.keys() - tracked)
    if uncovered:
        failures.append(f"committed raw TSVs without provenance: {', '.join(uncovered)}")
    if stale:
        failures.append(f"manifest outputs not committed as raw TSVs: {', '.join(stale)}")

    for name in sorted(tracked & outputs.keys()):
        entry = outputs[name]
        path = RAW_DIR / name
        if "rows" in entry and tsv_rows(path) != int(entry["rows"]):
            failures.append(f"{name}: row count differs from its manifest")
        if "bytes" in entry and path.stat().st_size != int(entry["bytes"]):
            failures.append(f"{name}: byte count differs from its manifest")
        if "sha256" in entry and sha256(path) != entry["sha256"]:
            failures.append(f"{name}: sha256 differs from its manifest")

    return failures


def main() -> int:
    failures = problems()
    if failures:
        print("provenance check failed:\n  " + "\n  ".join(failures), file=sys.stderr)
        return 1
    kg, gold = load_manifests()
    outputs = combined_outputs(kg, gold)
    print(
        f"provenance current: {len(outputs)} committed inventories, "
        f"{len(gold.get('sources', []))} GOLD sources"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
