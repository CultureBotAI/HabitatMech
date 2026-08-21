#!/usr/bin/env python3
"""Verify hashes and coverage for every committed data/raw TSV inventory."""

from __future__ import annotations

import csv
import hashlib
import subprocess
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = REPO_ROOT / "data" / "raw"
KG_MANIFEST = RAW_DIR / "MANIFEST.yaml"
GOLD_MANIFEST = RAW_DIR / "GOLD_MANIFEST.yaml"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def tsv_rows(path: Path) -> int:
    with path.open(newline="", encoding="utf-8") as fh:
        return sum(1 for _row in csv.reader(fh, delimiter="\t")) - 1


def load_manifests() -> tuple[dict[str, dict], list[dict]]:
    kg = yaml.safe_load(KG_MANIFEST.read_text(encoding="utf-8"))
    gold = yaml.safe_load(GOLD_MANIFEST.read_text(encoding="utf-8"))
    outputs = {entry["path"]: entry for entry in kg.get("outputs", [])}
    for entry in gold.get("outputs", []):
        if entry["path"] in outputs:
            raise ValueError(f"inventory appears in two manifests: {entry['path']}")
        outputs[entry["path"]] = entry
    return outputs, gold.get("sources", [])


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
    outputs, sources = load_manifests()
    failures = []
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

    for source in sources:
        for field in ("name", "location", "local_name", "retrieved_at", "bytes", "sha256"):
            if not source.get(field):
                failures.append(f"GOLD source {source.get('name', '<unnamed>')}: missing {field}")
        if source.get("committed") is not False:
            failures.append(f"GOLD source {source.get('name')}: large source must remain uncommitted")
        if len(str(source.get("sha256", ""))) != 64:
            failures.append(f"GOLD source {source.get('name')}: invalid sha256")
    return failures


def main() -> int:
    failures = problems()
    if failures:
        print("provenance check failed:\n  " + "\n  ".join(failures), file=sys.stderr)
        return 1
    outputs, sources = load_manifests()
    print(f"provenance current: {len(outputs)} committed inventories, {len(sources)} GOLD sources")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
