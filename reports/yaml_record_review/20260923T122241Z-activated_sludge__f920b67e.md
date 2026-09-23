# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/activated_sludge__f920b67e.yaml`
- Started UTC: 2026-09-23T12:20:00Z
- Finished UTC: 2026-09-23T12:22:41Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.81ee86290d` |
| Label | `Activated sludge` |
| Category | `ENGINEERED` |
| Grounding status | `NARROW` |
| Mapping status | `SEEDED` |
| Source | `GOLD` |
| Source ID | `gold.ecosystem:8162` |
| Source path | `Engineered > Bioreactor > MBR (Membrane bioreactor) > Activated sludge` |
| Record status | Generated from `data/raw/` plus maintained curation inputs; generated YAML remains read-only |

This is the generated GOLD record for activated sludge under `Engineered > Bioreactor > MBR (Membrane bioreactor)`. `data/habitats/PATHS.tsv:2251` locks `habitatmech:GOLD.81ee86290d` to the `activated_sludge__f920b67e` slug, and the identifier matches `sha1("GOLD:Engineered > Bioreactor > MBR (Membrane bioreactor) > Activated sludge")[:10]`.

The target has no direct item-level row in `curation/decisions.tsv`, no authored definition in `curation/term_requests.tsv`, and no causal-graph overlay under `curation/causal_graphs`. Its maintained direct source row is `data/raw/gold_ecosystem_paths.tsv:1190`.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/engineered/activated_sludge__f920b67e.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/engineered/activated_sludge__f920b67e.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the committed term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; expected 3206 records, found 3206, with 0 missing, 0 extra, and 0 differing. |
| `just worklist --limit 2000` | Passed; 0 ungrounded records are still undecided and 1810 decisions are on file. |
| `just report` | Passed; the generated corpus still has 3206 records, 2520 `SEEDED` mappings, 686 `REVIEWED` mappings, 0 risky unreviewed groundings, and 0 swept concepts whose label or path currently names a non-habitat. |
| Reference validator | Not applicable; this record has no record-level `evidence`, no `causal_graphs`, and therefore no literature references for a reference-specific validator to resolve. |
| `git diff --check` | Passed before writing this report; no whitespace or patch errors were present. |

## Identity and Grounding

The direct GOLD identity is supported by `data/raw/gold_ecosystem_paths.tsv:1190`:

| Raw field | Value |
|---|---|
| `canonical_path` | `Engineered > Bioreactor > MBR (Membrane bioreactor) > Activated sludge` |
| `ecosystem` | `Engineered` |
| `ecosystem_category` | `Bioreactor` |
| `ecosystem_type` | `MBR (Membrane bioreactor)` |
| `ecosystem_subtype` | `Activated sludge` |
| `specific_ecosystem` | empty |
| `leaf_label` | `Activated sludge` |
| `depth` | `4` |
| `gold_node_count` | `2` |
| `organism_count` | `0` |
| `study_count` | `0` |
| `biosample_count` | `0` |
| `total_assertions` | `0` |
| `gold_node_ids` | `gold.ecosystem:8162\|gold.ecosystem:8163` |

The generic activated-sludge ontology parent is supported: `data/raw/ontology_terms.tsv:7191` carries `ENVO:00002046` with label `activated sludge`, and `data/raw/ontology_subclass_edges.tsv:5293` records `ENVO:00002046 rdfs:subClassOf ENVO:00002044`. `data/raw/ontology_terms.tsv:7189` labels `ENVO:00002044` as `sludge`.

The generated source-path parent is the unsupported claim. The immediate GOLD parent path `Engineered > Bioreactor > MBR (Membrane bioreactor)` resolves to `ENVO:03600010` `membrane bioreactor`, is locked to `data/habitats/engineered/membrane_bioreactor.yaml` by `data/habitats/PATHS.tsv:930`, and has an item-level `GROUND` decision at `curation/decisions.tsv:1108`. That correctly makes the parent path an exact membrane-bioreactor record, but it does not make the activated-sludge child path a narrower kind of membrane bioreactor.

## Evidence

| Claim | Nearest support | Review |
|---|---|---|
| The generated record represents GOLD path `Engineered > Bioreactor > MBR (Membrane bioreactor) > Activated sludge`. | `data/raw/gold_ecosystem_paths.tsv:1190` | Supported. The raw `canonical_path`, `leaf_label`, and generated `source_path` agree. |
| The generated `source_id` is `gold.ecosystem:8162`, and the duplicate-node note is warranted. | `data/raw/gold_ecosystem_paths.tsv:1190`; `src/habitatmech/seed.py` | Supported. The raw row lists two GOLD ecosystem node ids with `gold.ecosystem:8162` first; the seeder emits the first id and notes the collapsed node count when a canonical GOLD path has several node ids. |
| The source attestation should omit `assertion_count` and `assertion_unit`. | `data/raw/gold_ecosystem_paths.tsv:1190`; `src/habitatmech/seed.py` | Supported. The raw row has `organism_count=0`, and the seeder emits GOLD organism counts only when this value is nonzero. |
| The source concept is narrower than generic activated sludge. | `data/raw/ontology_terms.tsv:7191`; `data/raw/ontology_subclass_edges.tsv:5293`; sibling `Activated sludge` GOLD paths in `data/raw/gold_ecosystem_paths.tsv` | Supported. GOLD has many engineered `Activated sludge` leaves, while `ENVO:00002046` names activated sludge generically. |
| The target path is a kind of `ENVO:03600010` `membrane bioreactor`. | Generated from the GOLD `Engineered > Bioreactor > MBR (Membrane bioreactor)` parent path after the seeder resolves that parent to `ENVO:03600010`. | Unsupported. The parent path denotes the membrane-bioreactor context; the child denotes activated-sludge material in that context rather than a narrower kind of reactor. |

Unsupported or over-scoped claims: `parent_habitats` turns a GOLD membrane-bioreactor context edge into the false statement that activated-sludge material is itself a subtype of membrane bioreactor.

## Completeness

No direct source fields are missing for the maintained GOLD row. The generated record carries the source name, first GOLD node id, leaf label, canonical path, duplicate-node note, `skos:narrowMatch` mapping predicate, the activated-sludge ontology parent, and the immediate GOLD path parent.

The generated target correctly omits `assertion_count`, `assertion_unit`, environmental parameters, and characteristic taxa because the direct raw row has zero organism assertions and no exact rows in `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`, or `data/raw/gold_studies.tsv`. Exact hidden/ignored-inclusive searches for `habitatmech:GOLD.81ee86290d`, `activated_sludge__f920b67e`, `gold.ecosystem:8162`, `gold.ecosystem:8163`, and the exact source path covered `curation`, `history`, `research`, `reports`, `data/raw`, `data/habitats/PATHS.tsv`, and generated records while excluding broad generated `build`, `data/text_map`, and `pages` outputs; they found the expected raw row, generated target, path lock, and no target-specific maintained curation input.

The record has no synonyms, xrefs, authored definition, record-level evidence, causal graphs, discussions, datasets, or quality flags. The consequential gap is the inherited GOLD hierarchy: `src/habitatmech/seed.py` stores every resolved GOLD path, then adds the resolved next path prefix to each child as a parent; `build_document()` serializes that set as `parent_habitats`. Here that converts a membrane-bioreactor reactor/container context into an is-a parent for activated sludge.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| HM-ACTSLUDGE-F920B67E-001 | major | `parent_habitats` asserts `habitatmech:GOLD.81ee86290d` is a kind of `ENVO:03600010` `membrane bioreactor`, but the child is activated sludge and the supported material parent is `ENVO:00002046` `activated sludge` under `ENVO:00002044` `sludge`. `parent_habitats` is an is-a relation, and this path edge turns GOLD's membrane-bioreactor context into the false claim that activated sludge is the reactor itself. | Add an item-level decision for `habitatmech:GOLD.81ee86290d` in `curation/decisions.tsv`; if the concept stays minted, add a `curation/term_requests.tsv` definition with `parent_mode=REPLACE` so the generated record keeps `ENVO:00002046` and drops the inherited `ENVO:03600010` parent. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Add an item-level decision for `habitatmech:GOLD.81ee86290d` in `curation/decisions.tsv`, keyed to the generated identifier and scoped to `Engineered > Bioreactor > MBR (Membrane bioreactor) > Activated sludge`.

2. If the record denotes generic activated sludge rather than a membrane-bioreactor-specific subtype, ground it directly to `ENVO:00002046` so the GOLD attestation merges into the existing activated-sludge identity.

3. If the record remains a minted membrane-bioreactor-specific activated-sludge concept, add an authored definition under `curation/term_requests.tsv` with `ENVO:00002046` `activated sludge` as the genus and `parent_mode=REPLACE` so the next seed keeps the true activated-sludge parent and removes the false source-path parent.

4. Regenerate the corpus rather than editing `data/habitats/engineered/activated_sludge__f920b67e.yaml` directly.

## Follow-up Checks

- `just seed`
- `just seed-canary habitatmech:GOLD.81ee86290d`
- Inspect `data/habitats/engineered/activated_sludge__f920b67e.yaml`, or confirm the record intentionally merged away after an exact `GROUND`.
- `just seed-apply --force`
- `just validate data/habitats/engineered/activated_sludge__f920b67e.yaml` if the record stays minted; otherwise validate the record that absorbed its source attestation.
- `just validate-strict data/habitats/engineered/activated_sludge__f920b67e.yaml` if the record stays minted; otherwise validate the record that absorbed its source attestation.
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000`
- `just report`
- `git diff --check`
- Exact gitignore-independent searches for `habitatmech:GOLD.81ee86290d`, `gold.ecosystem:8162`, `gold.ecosystem:8163`, and `Engineered > Bioreactor > MBR (Membrane bioreactor) > Activated sludge` across `curation`, `data/raw`, `data/habitats`, `history`, and `research` to verify that no target-specific maintained input was missed.

## Additional Notes

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-activated_sludge__f920b67e.md' -print` included ignored files and found no pre-existing exact report for this record before this file was written.
- The direct false parent is not caused by a hand edit: `just verify-corpus --max-diffs 1` reproduced all 3206 generated records exactly from maintained inputs.
- Exact hidden/ignored-inclusive search found MBR sibling side-table rows for `Sludge` and `Mixed liquor`, but no side-table row for this exact activated-sludge path.
