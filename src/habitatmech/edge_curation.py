"""Native curation-decision transport for EdgeMech, preserving item-level scope.

Only explicit ITEM GROUND/GROUND_AS_PARENT/SAME_AS decisions supply inherited
mapping review. Other decisions remain unassessed transport entries. No
habitat-taxon association, aggregate count, preference or mechanism is inferred.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import re
import subprocess
import tempfile
from collections import Counter
from pathlib import Path

import yaml

from habitatmech.edge_publication import publish_stage

REPOSITORY = "CultureBotAI/HabitatMech"
SOURCE = "curation/decisions.tsv"
SCHEMA = "src/habitatmech/schema/habitatmech.yaml"
SEMANTICS = "docs/CURATION.md"
CLAW_COMMIT = "1b5391d083ba85ac94e5279c3cba25ac4fde243c"


def sha(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def adapt_decision(row: dict, *, position: int, commit: str, hashes: dict, prefixes: dict) -> dict:
    """Preserve a whole native decision; ITEM status never reviews other claims."""
    from kg_microbe_curation.identity import sha256_json
    from kg_microbe_curation.native import NATIVE_CONTRACT, native_assertion_id, validate_native_assertion

    predicates = {
        "GROUND": "habitatmech:GROUND",
        "GROUND_AS_PARENT": "habitatmech:GROUND_AS_PARENT",
        "SAME_AS": "habitatmech:SAME_AS",
    }
    supported = row.get("review_depth") == "ITEM" and row.get("decision") in predicates
    if supported and (
        not row.get("object_id") or not row.get("curator") or len(row.get("notes", "").strip()) < 20
    ):
        raise ValueError("Incomplete item-level native mapping decision")
    predicate = predicates[row["decision"]] if supported else "habitatmech:curation_decision"
    target = row["object_id"] if supported else row["decision"]
    selector = {"source_position": position, "identifier": row["identifier"]}

    def locator(path, selected=None):
        return {"repository": REPOSITORY, "commit": commit, "path": path, "selector": selected or {}}

    native_payload_sha = sha256_json(row)
    review_payload = row if supported else {}
    assertion = {
        "contract": NATIVE_CONTRACT,
        "native_locator": {
            **locator(SOURCE, selector),
            "source_sha256": hashes[SOURCE],
            "payload_sha256": native_payload_sha,
        },
        "payload": {
            "subject": row["identifier"],
            "predicate": predicate,
            "object": target,
            "native_payload": row,
            "context": {
                "scope": (
                    "native_habitat_mapping_decision_only"
                    if supported
                    else "native_habitat_curation_state_only"
                ),
                "source_concept_identifier": row["identifier"],
                "native_review_depth": row.get("review_depth"),
                "native_decision": row["decision"],
                "withheld_is_global_ban": False,
                "matching_policy": "exact_native_payload_and_dependency_bindings",
                "match_selector": {
                    "subject": row["identifier"],
                    "predicate": predicate,
                    "object": target,
                    "native_payload_sha256": native_payload_sha,
                    "source_sha256": hashes[SOURCE],
                },
            },
            "interpretation": {
                "normalization_contract": "habitatmech-native-curation-decisions/v1",
                "normalizer_contract_sha256": hashes[SEMANTICS],
                "schema_sha256": hashes[SCHEMA],
                "prefix_map_sha256": sha256_json(prefixes),
            },
        },
        "evidence": [
            {"evidence_id": "native-file:" + path, "locator": locator(path), "sha256": digest, "ancestry": []}
            for path, digest in sorted(hashes.items())
        ],
        "native_review": {
            "status": "supported" if supported else "unassessed",
            "locator": locator(SOURCE, selector) if supported else None,
            "sha256": hashes[SOURCE] if supported else None,
            "payload": review_payload,
            "payload_sha256": sha256_json(review_payload),
            "rationale": (
                row["notes"]
                if supported
                else (
                    "Native curation state is preserved; no explicit item-level mapping approval "
                    "is exported for this decision kind or depth."
                )
            ),
        },
        "assurance": "inherited_native_review" if supported else "unassessed",
        "limitations": [
            (
                "The native decision concerns one source concept and its stated target; "
                "no independent scientific review was performed."
            ),
            (
                "Native source scope and notes remain verbatim. Aggregate source counts "
                "cannot reconstruct organism-level or taxon-level observations."
            ),
            (
                "Characteristic taxa, habitat preferences and causal mechanisms are "
                "outside this curation-decision export."
            ),
            (
                "External citations in native notes are retained references; their content "
                "was not fetched or independently verified."
            ),
            (
                "Native decision enums are retained as predicates; no reviewed projection "
                "to SKOS or KG edge predicates is supplied."
            ),
        ],
        "independent_scientific_review": False,
    }
    assertion["assertion_id"] = native_assertion_id(assertion)
    validate_native_assertion(assertion)
    return assertion


def export_assertions(root: Path, commit: str, output: Path, positions: list[int] | None) -> dict:
    """Publish a complete or bounded immutable native decision surface as JSONL."""
    from kg_microbe_curation.identity import canonical_json
    from kg_microbe_curation.native import validate_native_assertion

    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise ValueError("An immutable source commit is required")
    if output.exists() or output.is_symlink():
        raise ValueError("Output must be a new directory")
    origin = subprocess.check_output(
        ["git", "-C", str(root), "remote", "get-url", "origin"], text=True
    ).strip()
    if origin not in {
        f"https://github.com/{REPOSITORY}.git",
        f"https://github.com/{REPOSITORY}",
        f"git@github.com:{REPOSITORY}.git",
    }:
        raise ValueError("Native Git origin identity mismatch")
    sources = {
        path: subprocess.check_output(["git", "-C", str(root), "show", f"{commit}:{path}"])
        for path in (SOURCE, SCHEMA, SEMANTICS)
    }
    hashes = {path: sha(content) for path, content in sources.items()}
    schema = yaml.safe_load(sources[SCHEMA])
    reader = csv.DictReader(io.StringIO(sources[SOURCE].decode()), delimiter="\t", strict=True)
    if not reader.fieldnames or len(reader.fieldnames) != len(set(reader.fieldnames)):
        raise ValueError("Invalid native TSV header")
    selected = set(positions) if positions is not None else None
    if positions is not None and (
        not positions
        or len(selected) != len(positions)
        or any(type(i) is not int or i < 1 for i in positions)
    ):
        raise ValueError("Positions must be unique positive source rows")
    output.parent.mkdir(parents=True, exist_ok=True)
    counts, source_rows, written, ignored_rows = Counter(), 0, 0, 0
    with tempfile.TemporaryDirectory(prefix=".native-assertions-", dir=output.parent) as temporary:
        stage = Path(temporary) / "export"
        stage.mkdir()
        content_hash = hashlib.sha256()
        membership_hash = hashlib.sha256()
        with (stage / "assertions.jsonl").open("wb") as stream:
            for source_rows, row in enumerate(reader, 1):
                if not row.get("identifier") or row["identifier"].startswith("#"):
                    ignored_rows += 1
                    continue
                required = (
                    "identifier",
                    "decision",
                    "object_id",
                    "object_label",
                    "grounding_status",
                    "curator",
                    "date",
                    "notes",
                )
                if (
                    None in row
                    or any(row.get(field) is None for field in required)
                    or not row.get("decision")
                ):
                    raise ValueError(f"Malformed native curation row at source position {source_rows}")
                if selected is not None and source_rows not in selected:
                    continue
                assertion = adapt_decision(
                    row, position=source_rows, commit=commit, hashes=hashes, prefixes=schema["prefixes"]
                )
                data = canonical_json(assertion) + b"\n"
                stream.write(data)
                content_hash.update(data)
                membership_hash.update(canonical_json([assertion["assertion_id"], source_rows]) + b"\n")
                counts[assertion["native_review"]["status"]] += 1
                written += 1
            stream.flush()
            os.fsync(stream.fileno())
        if selected is not None and (max(selected) > source_rows or written != len(selected)):
            raise ValueError("Requested source row is outside the native surface")
        persisted = Counter()
        persisted_hash, persisted_membership = hashlib.sha256(), hashlib.sha256()
        with (stage / "assertions.jsonl").open("rb") as stream:
            for line in stream:
                persisted_hash.update(line)
                assertion = json.loads(line)
                validate_native_assertion(assertion)
                persisted[assertion["native_review"]["status"]] += 1
                persisted_membership.update(
                    canonical_json(
                        [
                            assertion["assertion_id"],
                            assertion["native_locator"]["selector"]["source_position"],
                        ]
                    )
                    + b"\n"
                )
        if (
            persisted != counts
            or persisted_hash.digest() != content_hash.digest()
            or persisted_membership.digest() != membership_hash.digest()
        ):
            raise ValueError("Persisted native bytes, identity membership or counters differ")
        manifest = {
            "schema_version": 1,
            "contract": "kg-microbe-native-assertion/v1",
            "repository": REPOSITORY,
            "source_commit": commit,
            "claw_contract_commit": CLAW_COMMIT,
            "source_positions": positions,
            "source_rows": source_rows,
            "rows": written,
            "native_status_counts": dict(counts),
            "ignored_nondecision_rows": ignored_rows,
            "assertions_sha256": content_hash.hexdigest(),
            "assertion_membership_sha256": membership_hash.hexdigest(),
            "assertions_bytes": (stage / "assertions.jsonl").stat().st_size,
            "source_files": hashes,
            "independent_scientific_reviews": 0,
            "kg_occurrences_approved": 0,
            "scope": (
                "Complete authoritative curation decision table; "
                "bounded positions only when explicitly selected."
            ),
            "excluded_surfaces": [
                (
                    "Generated habitat-taxon associations and source aggregate counts "
                    "lack exact reviewed observation bindings in this adapter."
                ),
                "Causal mechanism assertions are outside the native mapping surface.",
            ],
        }
        (stage / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
        publish_stage(stage, output)
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--output", type=Path, required=True)
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--positions", nargs="+", type=int)
    selection.add_argument("--all", action="store_true")
    args = parser.parse_args()
    print(
        json.dumps(
            export_assertions(args.root, args.source_commit, args.output, args.positions),
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
