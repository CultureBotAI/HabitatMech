# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/activated_sludge__e45bf91b.yaml`
- Started UTC: 2026-09-23T11:00:00Z
- Finished UTC: 2026-09-23T11:03:06Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.645add8636` |
| Label | `Activated sludge` |
| Category | `ENGINEERED` |
| Grounding status | `NARROW` |
| Mapping status | `SEEDED` |
| Source | `GOLD` |
| Source ID | `gold.ecosystem:5622` |
| Source path | `Engineered > Sewage treatment plant > Activated sludge` |
| Record status | Generated from `data/raw/` plus maintained curation inputs; generated YAML remains read-only |

This is the generated GOLD record for activated sludge under `Engineered > Sewage treatment plant`. `data/habitats/PATHS.tsv:2021` locks `habitatmech:GOLD.645add8636` to the `activated_sludge__e45bf91b` slug, and the identifier matches `sha1("GOLD:Engineered > Sewage treatment plant > Activated sludge")[:10]`.

The target has no direct item-level row in `curation/decisions.tsv`, no authored definition in `curation/term_requests.tsv`, and no causal-graph overlay under `curation/causal_graphs`. Its maintained direct source row is `data/raw/gold_ecosystem_paths.tsv:430`.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/engineered/activated_sludge__e45bf91b.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/engineered/activated_sludge__e45bf91b.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the committed term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; expected 3206 records, found 3206, with 0 missing, 0 extra, and 0 differing. |
| `just worklist --limit 2000` | Passed; 0 ungrounded records are still undecided and 1810 decisions are on file. |
| `just report` | Passed; the generated corpus still has 3206 records, 2520 `SEEDED` mappings, 686 `REVIEWED` mappings, 0 risky unreviewed groundings, and 0 swept concepts whose label or path currently names a non-habitat. |
| Reference validator | Not applicable; this record has no record-level `evidence`, no `causal_graphs`, and therefore no literature references for a reference-specific validator to resolve. |
| `git diff --check` | Passed before writing this report; no whitespace or patch errors were present. |

## Identity and Grounding

The direct GOLD identity is supported by `data/raw/gold_ecosystem_paths.tsv:430`:

| Raw field | Value |
|---|---|
| `canonical_path` | `Engineered > Sewage treatment plant > Activated sludge` |
| `ecosystem` | `Engineered` |
| `ecosystem_category` | `Sewage treatment plant` |
| `ecosystem_type` | `Activated sludge` |
| `leaf_label` | `Activated sludge` |
| `depth` | `3` |
| `gold_node_count` | `3` |
| `organism_count` | `18` |
| `study_count` | `0` |
| `biosample_count` | `0` |
| `total_assertions` | `18` |
| `gold_node_ids` | `gold.ecosystem:5622|gold.ecosystem:5623|gold.ecosystem:5624` |

The ontology material parent is supported: `data/raw/ontology_terms.tsv:7191` carries `ENVO:00002046` with label `activated sludge`, and `data/raw/ontology_subclass_edges.tsv:5293` records `ENVO:00002046 rdfs:subClassOf ENVO:00002044`. `data/raw/ontology_terms.tsv:7189` labels `ENVO:00002044` as `sludge`.

The generated source-path parent is the unsupported claim. The immediate GOLD parent path `Engineered > Sewage treatment plant` resolves to `ENVO:00003043`, locked to `data/habitats/engineered/sewage_plant.yaml` by `data/habitats/PATHS.tsv:712`. `data/raw/ontology_terms.tsv:7373` labels `ENVO:00003043` as `sewage plant` and defines it as a waste treatment plant, and `data/raw/ontology_subclass_edges.tsv:5492` places it under `ENVO:00002272`. Activated sludge is material in a sewage plant, not a narrower sewage-plant facility.

## Evidence

| Claim | Nearest support | Review |
|---|---|---|
| The generated record represents GOLD path `Engineered > Sewage treatment plant > Activated sludge`. | `data/raw/gold_ecosystem_paths.tsv:430` | Supported. The raw `canonical_path`, `leaf_label`, and generated `source_path` agree. |
| The generated `source_id` is `gold.ecosystem:5622` and the duplicate-node note is warranted. | `data/raw/gold_ecosystem_paths.tsv:430`; `src/habitatmech/seed.py` | Supported. The row lists three GOLD ecosystem node ids with `gold.ecosystem:5622` first; the seeder emits the first id and notes the collapsed node count when a canonical GOLD path has several node ids. |
| The source row carries 18 GOLD organism assertions. | `data/raw/gold_ecosystem_paths.tsv:430` | Supported. `organism_count` and `total_assertions` are both 18, and the generated source attestation records `assertion_count: 18` with `assertion_unit: ORGANISM`. |
| The source concept is narrower than generic activated sludge. | `data/raw/ontology_terms.tsv:7191`; `data/raw/ontology_subclass_edges.tsv:5293`; sibling `Activated sludge` GOLD paths in `data/raw/gold_ecosystem_paths.tsv` | Supported. GOLD has many engineered `Activated sludge` leaves, while `ENVO:00002046` names activated sludge generically. |
| The target path is a kind of `ENVO:00003043` `sewage plant`. | Generated from the GOLD `Engineered > Sewage treatment plant` parent path after the seeder resolves that parent to `ENVO:00003043`. | Unsupported. `ENVO:00003043` denotes the treatment plant facility; the child denotes activated-sludge material inside that treatment context. |

Unsupported or over-scoped claims: `parent_habitats` turns a GOLD sewage-plant context edge into the false statement that the activated-sludge material is itself a subtype of a sewage plant.

## Completeness

No direct source fields are missing for the maintained GOLD row. The generated record carries the source name, first GOLD node id, leaf label, canonical path, duplicate-node note, `skos:narrowMatch` mapping predicate, and 18-organism assertion count.

The record has no synonyms, xrefs, authored definition, environmental parameters, characteristic taxa, record-level evidence, causal graphs, discussions, datasets, or quality flags. Exact hidden/ignored-inclusive searches for `habitatmech:GOLD.645add8636`, `645add8636`, `activated_sludge__e45bf91b`, `gold.ecosystem:5622`, `gold.ecosystem:5623`, `gold.ecosystem:5624`, and the exact source path covered `curation`, `history`, `research`, `reports`, `data/raw`, `data/habitats/PATHS.tsv`, and generated records while excluding `build`, `data/text_map`, and `pages`; they found the expected raw row, generated target, path lock, and one prior sibling-review mention, and no target-specific maintained curation input.

An exact ignored/hidden-inclusive search of `data/raw/gold_path_triads.tsv`, `data/raw/gold_path_biosamples.tsv`, and `data/raw/gold_studies.tsv` found no rows for `Engineered > Sewage treatment plant > Activated sludge`, matching the zero study and biosample counts in `data/raw/gold_ecosystem_paths.tsv:430`.

The consequential gap is the inherited GOLD hierarchy. `src/habitatmech/seed.py` stores every resolved GOLD path, then adds the resolved next path prefix to each child as a parent; `build_document()` serializes that set as `parent_habitats`. Here that converts a sewage-plant container/context into an is-a parent for activated sludge.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| HM-ACTSLUDGE-E45BF91B-001 | major | `parent_habitats` asserts `habitatmech:GOLD.645add8636` is a kind of `ENVO:00003043` `sewage plant`, but the child is activated sludge and the supported material parent is `ENVO:00002046` `activated sludge` under `ENVO:00002044` `sludge`. `parent_habitats` is an is-a relation, and this path edge turns GOLD's sewage-treatment-plant context into the false claim that activated sludge is the treatment plant itself. | Add an item-level decision for `habitatmech:GOLD.645add8636` in `curation/decisions.tsv`; if the concept stays minted, add a `curation/term_requests.tsv` definition with `parent_mode=REPLACE` so the generated record keeps `ENVO:00002046` and drops the inherited `ENVO:00003043` sewage-plant parent. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Add an item-level decision for `habitatmech:GOLD.645add8636` in `curation/decisions.tsv`, keyed to the generated identifier and scoped to `Engineered > Sewage treatment plant > Activated sludge`.

2. If the record remains a minted sewage-treatment-plant-specific activated-sludge concept, add an authored definition under `curation/term_requests.tsv` with `ENVO:00002046` `activated sludge` as the genus and `parent_mode=REPLACE` so the next seed keeps the true activated-sludge parent and removes the false source-path parent.

3. Regenerate the corpus and confirm `data/habitats/engineered/activated_sludge__e45bf91b.yaml` no longer names `ENVO:00003043` under `parent_habitats`.

## Follow-up Checks

- `just seed`
- `just seed-canary habitatmech:GOLD.645add8636`
- `just seed-apply --force`
- `just validate data/habitats/engineered/activated_sludge__e45bf91b.yaml`
- `just validate-strict data/habitats/engineered/activated_sludge__e45bf91b.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just report`
- `git diff --check`
- Exact gitignore-independent searches for `habitatmech:GOLD.645add8636`, `gold.ecosystem:5622`, `gold.ecosystem:5623`, `gold.ecosystem:5624`, and `Engineered > Sewage treatment plant > Activated sludge` across `curation`, `data/raw`, `data/habitats`, `history`, and `research` to verify that no target-specific maintained input was missed.

## Additional Notes

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-activated_sludge__e45bf91b.md' -print` included ignored files and found no pre-existing exact report for this record before this file was written.
- The direct false parent is not caused by a hand edit: `just verify-corpus --max-diffs 1` reproduced all 3206 generated records exactly from maintained inputs.
- This review intentionally treats the standalone `ENVO:00003043` `sewage plant` record as supported. The defect is the GOLD path edge that makes an activated-sludge material a subtype of that plant.
