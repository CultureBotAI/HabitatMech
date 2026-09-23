# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/activated_sludge__e116af8f.yaml`
- Started UTC: 2026-09-23T10:41:00Z
- Finished UTC: 2026-09-23T10:44:34Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.5d1a568147` |
| Label | `Activated sludge` |
| Category | `ENGINEERED` |
| Grounding status | `NARROW` |
| Mapping status | `SEEDED` |
| Source | `GOLD` |
| Source ID | `gold.ecosystem:8225` |
| Source path | `Engineered > WWTP > A/O treatment system > A/O bioreactor > Activated sludge` |
| Record status | Generated from `data/raw/` plus maintained curation inputs; generated YAML remains read-only |

This is the generated GOLD record for activated sludge under an A/O bioreactor. `data/habitats/PATHS.tsv:1967` locks `habitatmech:GOLD.5d1a568147` to the `activated_sludge__e116af8f` slug, and the identifier matches `sha1("GOLD:Engineered > WWTP > A/O treatment system > A/O bioreactor > Activated sludge")[:10]`.

The generated record has no direct row in `curation/decisions.tsv`, no authored definition in `curation/term_requests.tsv`, and no causal-graph overlay under `curation/causal_graphs`. Its maintained direct source row is `data/raw/gold_ecosystem_paths.tsv:1385`.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/engineered/activated_sludge__e116af8f.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/engineered/activated_sludge__e116af8f.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the committed term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; expected 3206 records, found 3206, with 0 missing, 0 extra, and 0 differing. |
| `just worklist --limit 2000` | Passed; 0 ungrounded records are still undecided and 1810 decisions are on file. |
| `just report` | Passed; the generated corpus still has 3206 records, 2520 `SEEDED` mappings, 686 `REVIEWED` mappings, 0 risky unreviewed groundings, and 0 swept concepts whose label or path currently names a non-habitat. |
| Reference validator | Not applicable; this record has no record-level `evidence`, no `causal_graphs`, and therefore no literature references for a reference-specific validator to resolve. |
| `git diff --check` | Passed before writing this report; no whitespace or patch errors were present. |

## Identity and Grounding

The direct GOLD identity is supported by `data/raw/gold_ecosystem_paths.tsv:1385`:

| Raw field | Value |
|---|---|
| `canonical_path` | `Engineered > WWTP > A/O treatment system > A/O bioreactor > Activated sludge` |
| `ecosystem` | `Engineered` |
| `ecosystem_category` | `WWTP` |
| `ecosystem_type` | `A/O treatment system` |
| `ecosystem_subtype` | `A/O bioreactor` |
| `specific_ecosystem` | `Activated sludge` |
| `leaf_label` | `Activated sludge` |
| `depth` | `5` |
| `gold_node_count` | `1` |
| `organism_count` | `0` |
| `study_count` | `0` |
| `biosample_count` | `0` |
| `total_assertions` | `0` |
| `gold_node_ids` | `gold.ecosystem:8225` |

The ontology parent is supported: `data/raw/ontology_terms.tsv:7191` carries `ENVO:00002046` with label `activated sludge`, and `data/raw/ontology_subclass_edges.tsv:5293` records `ENVO:00002046 rdfs:subClassOf ENVO:00002044`. `data/raw/ontology_terms.tsv:7189` labels `ENVO:00002044` as `sludge`.

The second generated parent is the problematic one. `src/habitatmech/seed.py` links every GOLD path to the identifier resolved for its immediate path prefix; for this child, that prefix is `Engineered > WWTP > A/O treatment system > A/O bioreactor`, which resolves to `habitatmech:GOLD.bf15464676` and is locked to `data/habitats/engineered/a_o_bioreactor.yaml`. That explains why `parent_habitats` contains `habitatmech:GOLD.bf15464676`, but it does not make activated sludge a kind of A/O bioreactor.

## Evidence

| Claim | Nearest support | Review |
|---|---|---|
| The generated record represents GOLD node `gold.ecosystem:8225`. | `data/raw/gold_ecosystem_paths.tsv:1385` | Supported. The raw `gold_node_ids` cell is exactly `gold.ecosystem:8225`, and the generated `source_attestations` entry emits that id. |
| The GOLD label and path are `Activated sludge` at `Engineered > WWTP > A/O treatment system > A/O bioreactor > Activated sludge`. | `data/raw/gold_ecosystem_paths.tsv:1385` | Supported. `source_label` and `source_path` match the raw row. |
| The GOLD source row has no direct organism assertion count. | `data/raw/gold_ecosystem_paths.tsv:1385` | Supported. The organism, study, biosample, and total assertion fields are all zero, so the source attestation correctly omits `assertion_count` and `assertion_unit`. |
| This minted record is narrower than generic activated sludge. | `data/raw/ontology_terms.tsv:7191`; `data/raw/ontology_subclass_edges.tsv:5293`; `data/raw/gold_ecosystem_paths.tsv:1385` | Supported. The GOLD leaf names activated sludge in a specific A/O bioreactor context, while `ENVO:00002046` names activated sludge generically. |
| This minted record is a kind of `habitatmech:GOLD.bf15464676` `A/O bioreactor`. | `data/raw/gold_ecosystem_paths.tsv:1384-1385`; `data/habitats/engineered/activated_sludge__e116af8f.yaml` | Unsupported as an is-a claim. The raw hierarchy supplies the A/O bioreactor context, but the child record denotes the activated-sludge material in that system, not the bioreactor itself. |

Unsupported or over-scoped claims: `parent_habitats` turns a GOLD context edge into the false statement that this A/O-bioreactor activated sludge material is itself a subtype of the `A/O bioreactor` vessel/context.

## Completeness

No direct source fields are missing for the maintained GOLD row. The generated record carries the source name, only GOLD node id, leaf label, and canonical path; it correctly leaves out direct assertion counts because the raw row has zero organism, study, biosample, and total assertions.

The record has no synonyms, xrefs, authored definition, environmental parameters, characteristic taxa, record-level evidence, causal graphs, discussions, datasets, or quality flags. Exact gitignore-independent searches for `habitatmech:GOLD.5d1a568147`, `5d1a568147`, `activated_sludge__e116af8f`, `gold.ecosystem:8225`, and the exact source path covered `curation`, `history`, `research`, `reports`, `data/raw`, `data/habitats/PATHS.tsv`, and generated records while excluding `build`, `data/text_map`, and `pages`; they found the expected raw row, generated target, slug lock, and sibling review references, and no target-specific maintained curation input.

The consequential gap is the inherited GOLD hierarchy. `src/habitatmech/seed.py` records every resolved GOLD path and then attaches each child to the next path prefix without checking whether the edge is an is-a relationship. Here that gives a material record the parent `A/O bioreactor`. The previous review of `a_o_bioreactor.yaml` also found that the same branch contains a `NOT_APPLICABLE` `A/O treatment system` ancestor, so the current target is downstream of a broader hierarchy issue as well as its own material-versus-vessel edge.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| HM-ACTSLUDGE-E116AF8F-001 | major | `parent_habitats` asserts `habitatmech:GOLD.5d1a568147` is a kind of `habitatmech:GOLD.bf15464676` `A/O bioreactor`, but the child is activated sludge and the supported material parent is `ENVO:00002046` `activated sludge` under `ENVO:00002044` `sludge`. `parent_habitats` is an is-a relation, and this path edge turns GOLD's A/O-bioreactor context into the false claim that activated sludge is the reactor itself. | Add an item-level decision for `habitatmech:GOLD.5d1a568147` in `curation/decisions.tsv`; if the concept stays minted, add a `curation/term_requests.tsv` definition with `parent_mode=REPLACE` so the generated record keeps `ENVO:00002046` and drops the inherited `A/O bioreactor` parent. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Add an item-level decision for `habitatmech:GOLD.5d1a568147` in `curation/decisions.tsv`, keyed to the generated identifier and scoped to `Engineered > WWTP > A/O treatment system > A/O bioreactor > Activated sludge`.

2. If the record remains a minted A/O-bioreactor-specific activated-sludge concept, add an authored definition under `curation/term_requests.tsv` with `ENVO:00002046` `activated sludge` as the genus and `parent_mode=REPLACE` so the next seed keeps the true activated-sludge parent and removes the false source-path parent.

3. Regenerate the corpus and confirm `data/habitats/engineered/activated_sludge__e116af8f.yaml` no longer names `habitatmech:GOLD.bf15464676` under `parent_habitats`.

## Follow-up Checks

- `just seed`
- `just seed-canary habitatmech:GOLD.5d1a568147`
- `just seed-apply --force`
- `just validate data/habitats/engineered/activated_sludge__e116af8f.yaml`
- `just validate-strict data/habitats/engineered/activated_sludge__e116af8f.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just report`
- `git diff --check`
- Exact gitignore-independent searches for `habitatmech:GOLD.5d1a568147`, `gold.ecosystem:8225`, and `Engineered > WWTP > A/O treatment system > A/O bioreactor > Activated sludge` across `curation`, `data/raw`, `data/habitats`, `history`, and `research` to verify that no target-specific maintained input was missed.

## Additional Notes

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-activated_sludge__e116af8f.md' -print` included ignored files and found no pre-existing exact report for this record before this file was written.
- The exact content search for `Engineered > WWTP > A/O treatment system > A/O bioreactor > Activated sludge` across `data/raw`, `curation`, `data/habitats/PATHS.tsv`, and `reports/yaml_record_review` included hidden and ignored files and found only `data/raw/gold_ecosystem_paths.tsv:1385`.
- An exact hidden/ignored-inclusive search of `data/raw/gold_path_triads.tsv`, `data/raw/gold_path_biosamples.tsv`, and `data/raw/gold_studies.tsv` found no rows for the target source path, matching the zero study and biosample counts in `data/raw/gold_ecosystem_paths.tsv:1385`.
- The direct false parent is not caused by a hand edit: `just verify-corpus --max-diffs 1` reproduced all 3206 generated records exactly from maintained inputs.
