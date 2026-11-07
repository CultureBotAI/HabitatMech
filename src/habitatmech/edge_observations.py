"""Export scoped native habitat/taxon associations without inheriting mapping review.

The three committed inventories retain selected upstream associations. Their
source concepts are not silently replaced by reviewed habitat groundings, and
their rows do not establish characteristicness, growth or causal mechanisms.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import multiprocessing
import os
import re
import subprocess
import tempfile
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from itertools import islice
from pathlib import Path

import yaml

from habitatmech.edge_curation import CLAW_COMMIT, REPOSITORY, SCHEMA, SEMANTICS, sha
from habitatmech.edge_publication import publish_stage

MANIFEST = "data/raw/MANIFEST.yaml"
HARMONIZATION = "docs/HARMONIZATION.md"
EXTRACTOR = "src/habitatmech/extract.py"
PREDICATE = "habitatmech:characteristic_taxa"
BATCH_ROWS = 64
SURFACES = {
    "bacdive": {
        "source": "data/raw/bacdive_source_taxa.tsv",
        "owner": "data/raw/bacdive_isolation_sources.tsv",
        "key": "bacdive_id",
        "required": {"rank", "strain_count", "corroborated_by"},
        "selection": "retained source ranking by strain count; upstream pool may be larger",
    },
    "prego": {
        "source": "data/raw/prego_habitat_taxa.tsv",
        "owner": "data/raw/prego_habitats.tsv",
        "key": "prego_id",
        "required": {"rank", "prego_score", "direct_flag", "channels", "corroborated_by"},
        "selection": "retained source ranking by PREGO score; upstream pool may be larger",
    },
    "madin": {
        "source": "data/raw/madin_habitat_taxa.tsv",
        "owner": "data/raw/madin_habitats.tsv",
        "key": "madin_id",
        "required": {"corroborated_by"},
        "selection": "bounded corroboration-first source subset; taxon-ID ordering is not a rank",
    },
}


def table_rows(data: bytes, required: set[str]):
    reader = csv.DictReader(io.StringIO(data.decode("utf-8")), delimiter="\t", strict=True)
    if (
        not reader.fieldnames
        or len(reader.fieldnames) != len(set(reader.fieldnames))
        or not required.issubset(reader.fieldnames)
    ):
        raise ValueError("Missing or ambiguous native association columns")
    for position, row in enumerate(reader, 1):
        if None in row or any(value is None for value in row.values()):
            raise ValueError("Malformed native association row")
        yield position, row


def prepare(root: Path, commit: str, surface: str) -> dict:
    if not re.fullmatch(r"[0-9a-f]{40}", commit) or surface not in SURFACES:
        raise ValueError("An immutable native commit and known surface are required")
    origin = subprocess.check_output(
        ["git", "-C", str(root), "remote", "get-url", "origin"], text=True
    ).strip()
    if origin not in {
        f"https://github.com/{REPOSITORY}.git",
        f"https://github.com/{REPOSITORY}",
        f"git@github.com:{REPOSITORY}.git",
    }:
        raise ValueError("Native Git origin identity mismatch")
    profile = SURFACES[surface]
    paths = (profile["source"], profile["owner"], MANIFEST, SCHEMA, SEMANTICS, HARMONIZATION, EXTRACTOR)
    sources = {
        path: subprocess.check_output(["git", "-C", str(root), "show", f"{commit}:{path}"]) for path in paths
    }
    provenance = yaml.safe_load(sources[MANIFEST])
    owners = {}
    for position, row in table_rows(sources[profile["owner"]], {profile["key"], "taxon_count"}):
        key = row[profile["key"]]
        if not key or key in owners or not row["taxon_count"].isdigit():
            raise ValueError("Missing, duplicate or malformed native owner")
        owners[key] = (position, row)
    counts, total = Counter(), 0
    required = {profile["key"], "taxon_id", "taxon_label"} | profile["required"]
    for _position, row in table_rows(sources[profile["source"]], required):
        total += 1
        if row[profile["key"]] not in owners:
            raise ValueError("Native association lacks its exact source owner")
        counts[row[profile["key"]]] += 1
    for path, expected in ((profile["source"], total), (profile["owner"], len(owners))):
        entries = [entry for entry in provenance["outputs"] if entry["path"] == Path(path).name]
        if len(entries) != 1 or type(entries[0]["rows"]) is not int or entries[0]["rows"] != expected:
            raise ValueError("Native inventory count differs from its provenance manifest")
    if any(count > int(owners[key][1]["taxon_count"]) for key, count in counts.items()):
        raise ValueError("Retained associations exceed their native owner candidate pool")
    return {
        "source": sources[profile["source"]],
        "owners": owners,
        "retained": counts,
        "source_rows": total,
        "required": required,
        "common": {
            "commit": commit,
            "surface": surface,
            "hashes": {path: sha(content) for path, content in sources.items()},
            "prefixes": yaml.safe_load(sources[SCHEMA])["prefixes"],
            "upstream": provenance["kg_microbe_source"],
        },
    }


def adapt_observation(row, *, position, owner, retained, commit, surface, hashes, prefixes, upstream):
    from kg_microbe_curation.identity import sha256_json
    from kg_microbe_curation.native import NATIVE_CONTRACT, native_assertion_id, validate_native_assertion

    profile = SURFACES[surface]
    owner_position, owner_row = owner
    if row[profile["key"]] != owner_row[profile["key"]] or not re.fullmatch(
        r"NCBITaxon:[0-9]+", row["taxon_id"]
    ):
        raise ValueError("Native owner or taxon identity differs")
    if "rank" in row and (not row["rank"].isdigit() or int(row["rank"]) < 1):
        raise ValueError("Native association rank must be explicit and positive")
    if "strain_count" in row and not row["strain_count"].isdigit():
        raise ValueError("Native strain count must be explicit and nonnegative")

    def locator(path, selector=None):
        return {"repository": REPOSITORY, "commit": commit, "path": path, "selector": selector or {}}

    payload_sha = sha256_json(row)
    context = {
        "scope": "native_habitat_source_taxon_association_only",
        "native_slot": "characteristic_taxa",
        "native_source": surface.upper(),
        "subject_scope": "unprojected native source concept; habitat grounding is not inherited",
        "upstream_snapshot": upstream,
        "review_evidence_status": "unavailable_exact_native_association_review",
        "matching_policy": "exact_native_payload_and_dependency_bindings",
        "match_selector": {
            "subject": row[profile["key"]],
            "predicate": PREDICATE,
            "object": row["taxon_id"],
            "native_payload_sha256": payload_sha,
            "source_sha256": hashes[profile["source"]],
        },
        "owner_binding": {
            "locator": locator(profile["owner"], {"source_position": owner_position}),
            "source_sha256": hashes[profile["owner"]],
            "payload_sha256": sha256_json(owner_row),
            "native_payload": owner_row,
        },
        "selection_policy": profile["selection"],
        "retained_rows_for_source_concept": retained,
        "candidate_pool": owner_row["taxon_count"],
        "candidate_pool_unit": "TAXON",
        "native_inventory_is_subset": retained < int(owner_row["taxon_count"]),
        "characteristicness": "not asserted by this source association",
    }
    if surface == "bacdive":
        context["association_count_unit"] = "STRAIN"
    assertion = {
        "contract": NATIVE_CONTRACT,
        "native_locator": {
            **locator(profile["source"], {"source_position": position}),
            "source_sha256": hashes[profile["source"]],
            "payload_sha256": payload_sha,
        },
        "payload": {
            "subject": row[profile["key"]],
            "predicate": PREDICATE,
            "object": row["taxon_id"],
            "native_payload": row,
            "context": context,
            "interpretation": {
                "normalization_contract": "habitatmech-native-source-association-exact-lexical/v1",
                "normalizer_contract_sha256": sha256_json(
                    {path: hashes[path] for path in (SEMANTICS, HARMONIZATION, EXTRACTOR)}
                ),
                "schema_sha256": hashes[SCHEMA],
                "prefix_map_sha256": sha256_json(prefixes),
            },
        },
        "evidence": [
            {"evidence_id": "native-file:" + path, "locator": locator(path), "sha256": digest, "ancestry": []}
            for path, digest in sorted(hashes.items())
        ],
        "native_review": {
            "status": "unassessed",
            "locator": None,
            "sha256": None,
            "payload": {},
            "payload_sha256": sha256_json({}),
            "rationale": "The extracted association has no exact native assertion review proof. "
            "Grounding decisions and owner/cohort review do not review this association.",
        },
        "assurance": "unassessed",
        "limitations": [
            "Complete committed selected inventory only; upstream candidate pools can be larger.",
            "Native source concept identity is retained; no reviewed SKOS or KG predicate projection.",
            "Counts, scores, direct flags and channels retain source meaning; no growth, preference, "
            "characteristicness, negative observation or causal claim is inferred.",
            "Primary upstream files named in the provenance manifest were not fetched or reverified. "
            "BacDive aggregate strain counts do not identify individual strains.",
            "No independent scientific review or KG occurrence approval is supplied.",
        ],
        "independent_scientific_review": False,
    }
    assertion["assertion_id"] = native_assertion_id(assertion)
    validate_native_assertion(assertion)
    return assertion


def _adapt_batch(jobs, common):
    return [
        (position, adapt_observation(row, position=position, owner=owner, retained=retained, **common))
        for position, row, owner, retained in jobs
    ]


def _validated(jobs, common, workers):
    if workers == 1:
        for job in jobs:
            yield from _adapt_batch([job], common)
        return
    with ProcessPoolExecutor(
        max_workers=workers, mp_context=multiprocessing.get_context("spawn")
    ) as executor:
        while window := list(islice(jobs, workers * BATCH_ROWS)):
            pending = [
                executor.submit(_adapt_batch, window[i : i + BATCH_ROWS], common)
                for i in range(0, len(window), BATCH_ROWS)
            ]
            for future in pending:
                yield from future.result()


def export_observations(root, commit, surface, output, positions, *, workers=1):
    from kg_microbe_curation.identity import canonical_json

    if type(workers) is not int or not 1 <= workers <= 4:
        raise ValueError("workers must be an integer from 1 to 4")
    if output.exists() or output.is_symlink():
        raise ValueError("Output must be a new directory")
    prepared = prepare(root, commit, surface)
    if positions is not None and (
        not positions
        or len(set(positions)) != len(positions)
        or any(type(value) is not int or not 1 <= value <= prepared["source_rows"] for value in positions)
    ):
        raise ValueError("Positions must be unique valid native source rows")
    selected = set(positions) if positions is not None else None
    profile = SURFACES[surface]

    def jobs():
        for position, row in table_rows(prepared["source"], prepared["required"]):
            if selected is None or position in selected:
                key = row[profile["key"]]
                yield position, row, prepared["owners"][key], prepared["retained"][key]

    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".native-associations-", dir=output.parent) as temporary:
        stage = Path(temporary) / "export"
        stage.mkdir()
        content_hash, membership_hash = hashlib.sha256(), hashlib.sha256()
        written = 0
        with (stage / "assertions.jsonl").open("wb") as handle:
            for position, assertion in _validated(jobs(), prepared["common"], workers):
                line = canonical_json(assertion) + b"\n"
                handle.write(line)
                content_hash.update(line)
                membership_hash.update(canonical_json([assertion["assertion_id"], position]) + b"\n")
                written += 1
            handle.flush()
            os.fsync(handle.fileno())
        if written != (len(positions) if positions is not None else prepared["source_rows"]):
            raise ValueError("Export did not preserve selected native membership")
        persisted_hash, persisted_membership, persisted = hashlib.sha256(), hashlib.sha256(), Counter()
        with (stage / "assertions.jsonl").open("rb") as handle:
            for line in handle:
                persisted_hash.update(line)
                assertion = json.loads(line)
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
            persisted_hash.digest() != content_hash.digest()
            or persisted_membership.digest() != membership_hash.digest()
            or persisted != Counter({"unassessed": written})
        ):
            raise ValueError("Persisted native bytes, membership or counters differ")
        manifest = {
            "schema_version": 1,
            "contract": "kg-microbe-native-assertion/v1",
            "repository": REPOSITORY,
            "source_commit": commit,
            "claw_contract_commit": CLAW_COMMIT,
            "surface": surface,
            "source_positions": positions,
            "source_rows": prepared["source_rows"],
            "source_owner_rows": len(prepared["owners"]),
            "rows": written,
            "native_status_counts": {"unassessed": written},
            "assertions_sha256": content_hash.hexdigest(),
            "assertion_membership_sha256": membership_hash.hexdigest(),
            "assertions_bytes": (stage / "assertions.jsonl").stat().st_size,
            "source_files": prepared["common"]["hashes"],
            "validation_workers": workers,
            "validation_batch_size": BATCH_ROWS,
            "independent_scientific_reviews": 0,
            "kg_occurrences_approved": 0,
            "scope": (
                "Complete committed selected source-association inventory; " "no resolved habitat projection."
            ),
            "selection_policy": profile["selection"],
            "predicate": PREDICATE,
            "review_evidence_status": "unavailable_exact_native_association_review",
            "excluded_surfaces": [
                "Original upstream associations omitted from the committed selected inventories.",
                "Individual strain observations, reviewed KG/SKOS projections, "
                "growth, preference and causal claims.",
                "Grounding decisions are a separate native export and do not review these associations.",
            ],
        }
        (stage / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
        publish_stage(stage, output)
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--surface", choices=SURFACES, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--workers", type=int, choices=range(1, 5), default=1)
    parser.add_argument("--plan", action="store_true")
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--positions", type=int, nargs="+")
    selection.add_argument("--all", action="store_true")
    args = parser.parse_args()
    if args.plan:
        prepared = prepare(args.root, args.source_commit, args.surface)
        print(
            json.dumps(
                {
                    "surface": args.surface,
                    "source_rows": prepared["source_rows"],
                    "owner_rows": len(prepared["owners"]),
                    "predicate": PREDICATE,
                    "status": "unassessed",
                    "workers": args.workers,
                    "source_files": prepared["common"]["hashes"],
                },
                indent=2,
                sort_keys=True,
            )
        )
        return
    print(
        json.dumps(
            export_observations(
                args.root, args.source_commit, args.surface, args.output, args.positions, workers=args.workers
            ),
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
