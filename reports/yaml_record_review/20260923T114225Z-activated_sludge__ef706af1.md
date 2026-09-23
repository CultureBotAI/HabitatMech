# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/activated_sludge__ef706af1.yaml`
- Started UTC: 2026-09-23T11:40:00Z
- Finished UTC: 2026-09-23T11:42:25Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.9d25d6d7ef` |
| Label | `Activated sludge` |
| Category | `ENGINEERED` |
| Grounding status | `NARROW` |
| Mapping status | `SEEDED` |
| Source | `GOLD` |
| Source ID | `gold.ecosystem:5673` |
| Source path | `Engineered > WWTP > Aerobic digester > Activated sludge` |
| Record status | Generated from `data/raw/` plus maintained curation inputs; generated YAML remains read-only |

This is the generated GOLD record for activated sludge under `Engineered > WWTP > Aerobic digester`. `data/habitats/PATHS.tsv:2459` locks `habitatmech:GOLD.9d25d6d7ef` to the `activated_sludge__ef706af1` slug, and the identifier matches `sha1("GOLD:Engineered > WWTP > Aerobic digester > Activated sludge")[:10]`.

The target has no direct item-level row in `curation/decisions.tsv`, no authored definition in `curation/term_requests.tsv`, and no causal-graph overlay under `curation/causal_graphs`. Its maintained direct source row is `data/raw/gold_ecosystem_paths.tsv:790`.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/engineered/activated_sludge__ef706af1.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/engineered/activated_sludge__ef706af1.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the committed term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; expected 3206 records, found 3206, with 0 missing, 0 extra, and 0 differing. |
| `just worklist --limit 2000` | Passed; 0 ungrounded records are still undecided and 1810 decisions are on file. |
| `just report` | Passed; the generated corpus still has 3206 records, 2520 `SEEDED` mappings, 686 `REVIEWED` mappings, 0 risky unreviewed groundings, and 0 swept concepts whose label or path currently names a non-habitat. |
| Reference validator | Not applicable; this record has no record-level `evidence`, no `causal_graphs`, and therefore no literature references for a reference-specific validator to resolve. |
| `git diff --check` | Passed before writing this report; no whitespace or patch errors were present. |

## Identity and Grounding

The direct GOLD identity is supported by `data/raw/gold_ecosystem_paths.tsv:790`:

| Raw field | Value |
|---|---|
| `canonical_path` | `Engineered > WWTP > Aerobic digester > Activated sludge` |
| `ecosystem` | `Engineered` |
| `ecosystem_category` | `WWTP` |
| `ecosystem_type` | `Aerobic digester` |
| `ecosystem_subtype` | `Activated sludge` |
| `specific_ecosystem` | empty |
| `leaf_label` | `Activated sludge` |
| `depth` | `4` |
| `gold_node_count` | `2` |
| `organism_count` | `2` |
| `study_count` | `0` |
| `biosample_count` | `0` |
| `total_assertions` | `2` |
| `gold_node_ids` | `gold.ecosystem:5673\|gold.ecosystem:5674` |

The generic activated-sludge ontology parent is supported: `data/raw/ontology_terms.tsv:7191` carries `ENVO:00002046` with label `activated sludge`, and `data/raw/ontology_subclass_edges.tsv:5293` records `ENVO:00002046 rdfs:subClassOf ENVO:00002044`. `data/raw/ontology_terms.tsv:7189` labels `ENVO:00002044` as `sludge`.

The generated source-path parent is the unsupported claim. The immediate GOLD parent path `Engineered > WWTP > Aerobic digester` resolves to `habitatmech:GOLD.03fc563fae`, locked to `data/habitats/engineered/aerobic_digester.yaml` by `data/habitats/PATHS.tsv:1295`. `data/raw/gold_ecosystem_paths.tsv:1388` backs that parent path, but its only maintained decision is the class-level `CONFIRM_UNGROUNDED` row at `curation/decisions.tsv:118`, whose note explicitly says habitat validity was not assessed. Activated sludge is a sludge material in an aerobic digester or wastewater-treatment-plant context, not a narrower kind of aerobic digester.

## Evidence

| Claim | Nearest support | Review |
|---|---|---|
| The generated record represents GOLD path `Engineered > WWTP > Aerobic digester > Activated sludge`. | `data/raw/gold_ecosystem_paths.tsv:790` | Supported. The raw `canonical_path`, `leaf_label`, and generated `source_path` agree. |
| The generated `source_id` is `gold.ecosystem:5673`, and the duplicate-node note is warranted. | `data/raw/gold_ecosystem_paths.tsv:790`; `src/habitatmech/seed.py` | Supported. The raw row lists two GOLD ecosystem node ids with `gold.ecosystem:5673` first; the seeder emits the first id and notes the collapsed node count when a canonical GOLD path has several node ids. |
| The source row carries 2 GOLD organism assertions. | `data/raw/gold_ecosystem_paths.tsv:790` | Supported. `organism_count` and `total_assertions` are both 2, and the generated source attestation records `assertion_count: 2` with `assertion_unit: ORGANISM`. |
| GOLD has exact side-table context for the target path. | `data/raw/gold_path_biosamples.tsv:148`; `data/raw/gold_studies.tsv:551`, `:709`, `:1505`, `:3025`, `:4088` | Supported as contextual metadata only. The side tables link 197 biosamples and five study rows to the exact path; they do not make activated sludge a subtype of an aerobic digester. |
| The source concept is narrower than generic activated sludge. | `data/raw/ontology_terms.tsv:7191`; `data/raw/ontology_subclass_edges.tsv:5293`; sibling `Activated sludge` GOLD paths in `data/raw/gold_ecosystem_paths.tsv` | Supported. GOLD has many engineered `Activated sludge` leaves, while `ENVO:00002046` names activated sludge generically. |
| The target path is a kind of `habitatmech:GOLD.03fc563fae` `Aerobic digester`. | Generated from the GOLD `Engineered > WWTP > Aerobic digester` parent path after the seeder resolves that parent to `habitatmech:GOLD.03fc563fae`. | Unsupported. The parent path denotes the aerobic digester context; the child denotes activated-sludge material under that context rather than a narrower kind of digester. |

Unsupported or over-scoped claims: `parent_habitats` turns a GOLD aerobic-digester context edge into the false statement that the activated-sludge material is itself a subtype of aerobic digester.

## Completeness

No direct source fields are missing for the maintained GOLD row. The generated record carries the source name, first GOLD node id, leaf label, canonical path, duplicate-node note, `skos:narrowMatch` mapping predicate, 2-organism assertion count, the activated-sludge ontology parent, and the immediate GOLD path parent.

The record has no synonyms, xrefs, authored definition, environmental parameters, characteristic taxa, record-level evidence, causal graphs, discussions, datasets, or quality flags. Exact hidden/ignored-inclusive searches for `habitatmech:GOLD.9d25d6d7ef`, `activated_sludge__ef706af1`, `gold.ecosystem:5673`, `gold.ecosystem:5674`, and the exact source path covered `curation`, `history`, `research`, `reports`, `data/raw`, `data/habitats/PATHS.tsv`, and generated records while excluding broad generated `build`, `data/text_map`, and `pages` outputs; they found the expected raw rows, generated target, path lock, and no target-specific maintained curation input.

The same ignored/hidden-inclusive search found one aggregate path row, one 197-biosample row, and five study rows for `Engineered > WWTP > Aerobic digester > Activated sludge`. It found no exact `data/raw/gold_path_triads.tsv` row for this path, so the generated target correctly lacks an environmental-parameter entry.

The consequential gap is the inherited GOLD hierarchy. `src/habitatmech/seed.py` stores every resolved GOLD path, then adds the resolved next path prefix to each child as a parent; `build_document()` serializes that set as `parent_habitats`. Here that converts an aerobic-digester reactor/container context into an is-a parent for activated sludge.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| HM-ACTSLUDGE-EF706AF1-001 | major | `parent_habitats` asserts `habitatmech:GOLD.9d25d6d7ef` is a kind of `habitatmech:GOLD.03fc563fae` `Aerobic digester`, but the child is activated sludge and the supported material parent is `ENVO:00002046` `activated sludge` under `ENVO:00002044` `sludge`. `parent_habitats` is an is-a relation, and this path edge turns GOLD's aerobic-digester context into the false claim that activated sludge is the digester itself. | Add an item-level decision for `habitatmech:GOLD.9d25d6d7ef` in `curation/decisions.tsv`; if the concept stays minted, add a `curation/term_requests.tsv` definition with `parent_mode=REPLACE` so the generated record keeps `ENVO:00002046` and drops the inherited `Aerobic digester` parent. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Add an item-level decision for `habitatmech:GOLD.9d25d6d7ef` in `curation/decisions.tsv`, keyed to the generated identifier and scoped to `Engineered > WWTP > Aerobic digester > Activated sludge`.

2. If the record denotes generic activated sludge rather than an aerobic-digester-specific subtype, ground it directly to `ENVO:00002046` so the GOLD attestation merges into the existing activated-sludge identity.

3. If the record remains a minted aerobic-digester-specific activated-sludge concept, add an authored definition under `curation/term_requests.tsv` with `ENVO:00002046` `activated sludge` as the genus and `parent_mode=REPLACE` so the next seed keeps the true activated-sludge parent and removes the false source-path parent.

4. Regenerate the corpus rather than editing `data/habitats/engineered/activated_sludge__ef706af1.yaml` directly.

## Follow-up Checks

- `just seed`
- `just seed-canary habitatmech:GOLD.9d25d6d7ef`
- Inspect `data/habitats/engineered/activated_sludge__ef706af1.yaml`, or confirm the record intentionally merged away after an exact `GROUND`.
- `just seed-apply --force`
- `just validate data/habitats/engineered/activated_sludge__ef706af1.yaml` if the record stays minted; otherwise validate the record that absorbed its source attestation.
- `just validate-strict data/habitats/engineered/activated_sludge__ef706af1.yaml` if the record stays minted; otherwise validate the record that absorbed its source attestation.
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000`
- `just report`
- `git diff --check`
- Exact gitignore-independent searches for `habitatmech:GOLD.9d25d6d7ef`, `gold.ecosystem:5673`, `gold.ecosystem:5674`, and `Engineered > WWTP > Aerobic digester > Activated sludge` across `curation`, `data/raw`, `data/habitats`, `history`, and `research` to verify that no target-specific maintained input was missed.

## Additional Notes

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-activated_sludge__ef706af1.md' -print` included ignored files and found no pre-existing exact report for this record before this file was written.
- The direct false parent is not caused by a hand edit: `just verify-corpus --max-diffs 1` reproduced all 3206 generated records exactly from maintained inputs.
- The generated source-path parent currently has a true WWTP parent, `ENVO:00002043` `wastewater treatment plant`, but that edge is about the parent aerobic-digester concept and does not make activated sludge a subtype of either an aerobic digester or a wastewater treatment plant.
