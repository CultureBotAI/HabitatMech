# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/drinking_water_pipeline_network.yaml
- Started UTC: 2026-09-24T12:35:31Z
- Finished UTC: 2026-09-24T12:35:31Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Path | `data/habitats/engineered/drinking_water_pipeline_network.yaml` |
| Class | `HabitatRecord` |
| Identifier | `ENVO:03600003` |
| Label | `drinking water pipeline network` |
| Category | `ENGINEERED` |
| Generated or maintained | Generated from committed source inventories, the vendored ontology slice, and `data/habitats/PATHS.tsv`; `data/habitats/` remains read-only |
| Locked slug | `data/habitats/PATHS.tsv:925` maps `ENVO:03600003` to `drinking_water_pipeline_network` |
| Grounding | `CLOSE` |
| Mapping status | `REVIEWED` |

## Validation

| Check | Result |
| --- | --- |
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-drinking_water_pipeline_network.md' -print` | Passed; no prior exact `drinking_water_pipeline_network` review was present before this report was written. `find` included ignored files under `reports/yaml_record_review`. |
| `just validate data/habitats/engineered/drinking_water_pipeline_network.yaml` | Passed; no LinkML issues found. |
| `just validate-strict data/habitats/engineered/drinking_water_pipeline_network.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Reference validator | Not applicable; the target record has no record-level `evidence`, no causal graph, and no DOI, PMID, or URL evidence items to validate. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; 3206 records were expected, 3206 were present, and there were 0 missing, extra, or differing records. |
| `just worklist --limit 2000` | Passed; 0 ungrounded records are still undecided and 1810 decisions are on file. |
| `just report` | Passed; completed the corpus report for 3206 records. |
| `git diff --check` | Passed before report creation. |

## Identity and Grounding

The identifier, label, definition, synonym, and direct ontology parent are copied from the vendored ENVO slice. `data/raw/ontology_terms.tsv:10052` defines `ENVO:03600003` as `drinking water pipeline network` with exact synonym `drinking water pipeline`, and `data/raw/ontology_subclass_edges.tsv:8447` asserts `ENVO:03600003 rdfs:subClassOf ENVO:03600014`. `data/raw/ontology_terms.tsv:10063` then defines `ENVO:03600014` as `pipeline network`.

The source attestation is traceable to the raw GOLD aggregate. `data/raw/gold_ecosystem_paths.tsv:1276` lists the canonical path `Engineered > Built environment > Pipeline > Drinking water pipeline`, leaf label `Drinking water pipeline`, `gold_node_count` 1, zero organism, study, and biosample assertions, and node id `gold.ecosystem:5700`.

`grounding_status: CLOSE`, `mapping_predicate: skos:closeMatch`, and `mapping_status: REVIEWED` are all backed by maintained curation. `curation/decisions.tsv:1741` records a `REVIEW` decision for source concept `habitatmech:GOLD.e6a1b33fe8`, and the generated curation history carries that exact source key. The GOLD leaf names a singular drinking-water pipeline while the ENVO identity is a network used to transport drinking water to consumers, so the CLOSE review is an honest predicate: stricter than broad/narrow, but avoiding an over-claim of exact equality.

The parent set is also coherent. `ENVO:03600014` is the asserted ENVO genus of this ontology term, and `habitatmech:GOLD.edec297c39` is the generated HabitatMech record for the immediate GOLD parent path `Engineered > Built environment > Pipeline`.

## Evidence

| Claim | Evidence | Status |
| --- | --- | --- |
| The HabitatMech record denotes the ENVO class `ENVO:03600003` `drinking water pipeline network`. | `data/raw/ontology_terms.tsv:10052` and `data/habitats/engineered/drinking_water_pipeline_network.yaml:1` | Supported exactly. |
| ENVO `drinking water pipeline network` is a subclass of `pipeline network`. | `data/raw/ontology_subclass_edges.tsv:8447` asserts `ENVO:03600003 rdfs:subClassOf ENVO:03600014`. | Supported exactly. |
| The source GOLD path is `Engineered > Built environment > Pipeline > Drinking water pipeline`. | `data/raw/gold_ecosystem_paths.tsv:1276` lists that canonical path with leaf label `Drinking water pipeline` and node id `gold.ecosystem:5700`. | Supported exactly. |
| The GOLD source has one node id and no counted organism, study, or biosample assertions in the aggregate path table. | `data/raw/gold_ecosystem_paths.tsv:1276` reports `gold_node_count` 1 and 0 for `organism_count`, `study_count`, `biosample_count`, `independent_studies`, and `total_assertions`. | Supported exactly. |
| The source-specific CLOSE mapping has been reviewed. | `curation/decisions.tsv:1741` records an item-level `REVIEW` decision for `habitatmech:GOLD.e6a1b33fe8`; the generated record repeats that source concept in its `REVIEW` history entry. | Supported exactly. |
| The immediate GOLD parent path is `Pipeline`. | `data/raw/gold_ecosystem_paths.tsv:1275` lists `Engineered > Built environment > Pipeline`; `data/habitats/engineered/pipeline.yaml:1` carries the corresponding `habitatmech:GOLD.edec297c39` identifier. | Supported exactly. |
| No causal overlay is attached to `ENVO:03600003`. | Ignored/hidden-inclusive exact search over `curation/causal_graphs` found no `identifier: ENVO:03600003`, and `find curation/causal_graphs -maxdepth 1 -type f -name '*drinking*' -print` returned no files. | Supported exactly. |

## Completeness

The record is intentionally sparse for the inspected source concept. GOLD has only the one aggregate path for `Drinking water pipeline`, with no upstream organism, study, biosample, or triad assertion counts on the exact source path row. ENVO supplies the identity, exact synonym, definition, and direct is-a parent; maintained curation supplies the source-specific CLOSE review.

Ignored/hidden-inclusive exact searches covered `data/raw`, `curation`, `history`, `research`, `reports`, `data/habitats/PATHS.tsv`, and `data/habitats`. They found the expected ENVO term, ENVO subclass row, locked slug, GOLD path, GOLD node id, GOLD parent path, parent record, #12 curation decision, and generated target record. The same searches found no prior YAML review, term request, history record, or causal overlay for `ENVO:03600003`, `drinking_water_pipeline_network`, or `habitatmech:GOLD.e6a1b33fe8`.

The generated `Biofilm` child at `data/habitats/engineered/biofilm__3952f25d.yaml` inherits `ENVO:03600003` from the raw GOLD child path `Engineered > Built environment > Pipeline > Drinking water pipeline > Biofilm`. That edge is relevant to the record under review, but it is not an inconsistency: the child source path is explicitly under the same drinking-water pipeline GOLD branch.

## Findings

No findings.

## Recommended Edits

No edits recommended.

## Follow-up Checks

No follow-up curation is required for this record.

If a future pass reviews the generated `Pipeline` parent itself, rerun `just seed-canary ENVO:03600003` or `just verify-corpus --max-diffs 1` afterward to confirm `drinking_water_pipeline_network.yaml` still keeps a coherent parent set.

## Additional Notes

The sibling oil/gas pipeline research report mentions this record as evidence that GOLD's `Pipeline` branch can be reviewed at item specificity. That discussion does not change this record: unlike the oil/gas sibling, the drinking-water leaf already has an ENVO class and a maintained CLOSE review decision.
