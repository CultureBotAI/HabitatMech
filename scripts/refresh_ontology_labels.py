#!/usr/bin/env python3
"""Verify a pinned OWL source and replay the reviewed canonical-label updates."""

from __future__ import annotations

import argparse
import json

import yaml

from habitatmech.extract import RAW_DIR, read_tsv, write_tsv
from habitatmech.ontology_labels import (
    PLAN_PATH,
    RECEIPT_PATH,
    apply_label_refresh,
    load_plan,
    make_receipt,
)


class ManifestDumper(yaml.SafeDumper):
    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)


def main() -> int:
    from pathlib import Path

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True, help="Downloaded pinned RDF/XML")
    parser.add_argument("--plan", type=Path, default=PLAN_PATH)
    parser.add_argument("--check", action="store_true", help="Verify without writing")
    args = parser.parse_args()
    plan = load_plan(args.plan)
    receipt = make_receipt(args.source, plan)
    inventory = RAW_DIR / "ontology_terms.tsv"
    terms = list(read_tsv(inventory))
    updated = apply_label_refresh(terms, receipt)
    encoded = json.dumps(receipt, indent=2, ensure_ascii=True) + "\n"
    manifest_path = RAW_DIR / "MANIFEST.yaml"
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    expected_note = (
        "reviewed rdfs:label updates replayed after the kg-microbe slice; "
        "other ontology fields retain the kg-microbe snapshot."
    )
    if args.check:
        if terms != updated or RECEIPT_PATH.read_text(encoding="utf-8") != encoded:
            parser.error("ontology labels or receipt are stale")
        if manifest.get("ontology_label_refresh") != "../ontology_label_refresh.json":
            parser.error("inventory manifest does not identify the label refresh")
        if manifest.get("ontology_label_note") != expected_note:
            parser.error("inventory manifest does not identify the refresh scope")
    else:
        write_tsv(inventory, list(terms[0]), updated)
        RECEIPT_PATH.write_text(encoded, encoding="utf-8")
        manifest["ontology_label_refresh"] = "../ontology_label_refresh.json"
        manifest["ontology_label_note"] = expected_note
        if "mappings_note" in manifest:
            manifest["mappings_note"] = (
                "pinned separately from kg_microbe_source. mappings_staged_at is a local "
                "path; the sha256 below identifies the bytes."
            )
        manifest_path.write_text(
            "# Generated inventory provenance; label-only refresh identified below.\n"
            + yaml.dump(manifest, Dumper=ManifestDumper, sort_keys=False, width=10000),
            encoding="utf-8",
        )
    print(f"Verified {len(receipt['terms'])} canonical labels against {receipt['source_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
