# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/drinking_water_filter.yaml
- Started UTC: 2026-09-24T13:49:27Z
- Finished UTC: 2026-09-24T13:49:27Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/habitats/engineered/drinking_water_filter.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.697d4c6359` |
| Label | `Drinking water filter` |
| Category | `ENGINEERED` |
| Generated or maintained | Generated from committed GOLD source inventories, vendored ontology terms, `curation/decisions.tsv`, and `data/habitats/PATHS.tsv`; `data/habitats/` remains read-only |
| Locked slug | `data/habitats/PATHS.tsv:2058` maps `habitatmech:GOLD.697d4c6359` to `drinking_water_filter` |
| Grounding | `UNGROUNDED` |
| Mapping status | `SEEDED` |

## Validation

| Check | Result |
| --- | --- |
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-drinking_water_filter.md' -print` | Passed; no prior exact `drinking_water_filter` review was present before this report was written. `find` included ignored files under `reports/yaml_record_review`. |
| `just validate data/habitats/engineered/drinking_water_filter.yaml` | Passed; no LinkML issues found. |
| `just validate-strict data/habitats/engineered/drinking_water_filter.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Reference validator | Not applicable; the target record has no record-level `evidence`, no causal graph, and no DOI, PMID, or URL evidence items to validate. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; 3206 records were expected, 3206 were present, and there were 0 missing, extra, or differing records. |
| `just worklist --limit 2000` | Passed; 0 ungrounded records are still undecided and 1810 decisions are on file. |
| `just report` | Passed; completed the corpus report for 3206 records. |
| `git diff --check` | Passed before report creation. |

## Identity and Grounding

The minted identifier denotes the GOLD path `Engineered > Built environment > Drinking water treatment plant > Drinking water filter`. `data/raw/gold_ecosystem_paths.tsv:890` lists that exact canonical path, leaf label `Drinking water filter`, depth 4, `gold_node_count` 2, `organism_count` 1, `total_assertions` 1, and node ids `gold.ecosystem:5492|gold.ecosystem:5493`. The generated source attestation at `data/habitats/engineered/drinking_water_filter.yaml:8-16` repeats the path, keeps the first node id as `gold.ecosystem:5492`, and records the two-node aggregation note.

The existing maintained decision is not an item-level review. `curation/decisions.tsv:624` is a `CONFIRM_UNGROUNDED` row with no `object_id`, no `object_label`, and `review_depth` `CLASS`; its note says the class-level sweep found no term by lexical route and explicitly did not assess whether the concept is a habitat. That provenance is enough to keep the generated record `SEEDED`, but it is not enough to confirm a novel drinking-water-filter habitat.

An ignored/hidden-inclusive exact search for `Drinking water filter`, `drinking water filter`, and `water filter` over `data/raw/ontology_terms.tsv`, `curation/term_requests.tsv`, and `curation/term_requests_excluded.tsv` found no existing exact term request and found `ENVO:03600086` `water filter` in the vendored ontology slice. `data/raw/ontology_terms.tsv:10122` defines that class as a manufactured product used to remove contaminants from water, and `data/raw/ontology_subclass_edges.tsv:8520` puts it under `ENVO:00003074` `manufactured product`.

The current source-derived `ENVO:03600004` parent is not a strict superclass of the leaf concept. `data/raw/ontology_terms.tsv:10053` labels `ENVO:03600004` as `drinking water treatment plant` and defines it as an industrial building where water is purified for human consumption. A drinking water filter can be installed in, or be part of, that plant, but the filter is not itself an industrial building.

## Evidence

| Claim | Evidence | Status |
| --- | --- | --- |
| The generated record denotes the GOLD path `Engineered > Built environment > Drinking water treatment plant > Drinking water filter`. | `data/raw/gold_ecosystem_paths.tsv:890` lists that canonical path with leaf label `Drinking water filter`; `data/habitats/engineered/drinking_water_filter.yaml:8-16` repeats it in the GOLD source attestation. | Supported exactly. |
| The GOLD aggregate has two node ids and one organism assertion. | `data/raw/gold_ecosystem_paths.tsv:890` reports `gold_node_count` 2, `organism_count` 1, `total_assertions` 1, and node ids `gold.ecosystem:5492|gold.ecosystem:5493`. | Supported exactly. |
| The exact GOLD path appears in additional raw GOLD inventories. | Ignored/hidden-inclusive exact search found one `data/raw/gold_path_biosamples.tsv` row for `gold.ecosystem:5493` with 47 biosamples and four `data/raw/gold_studies.tsv` rows, `Gs0153664`, `Gs0153796`, `Gs0153850`, and `Gs0154207`, for the same path. | Supported exactly as additional path inventory. |
| No exact `drinking water filter` ontology term or term request is already present. | Ignored/hidden-inclusive exact search over `data/raw/ontology_terms.tsv`, `curation/term_requests.tsv`, and `curation/term_requests_excluded.tsv` found no `Drinking water filter` or `drinking water filter` row. | Supported exactly for those bounded files. |
| `ENVO:03600086` is an available broader `water filter` candidate. | `data/raw/ontology_terms.tsv:10122` labels `ENVO:03600086` `water filter` and `data/raw/ontology_subclass_edges.tsv:8520` asserts `ENVO:03600086 rdfs:subClassOf ENVO:00003074`. | Supported exactly; item review still needs to decide whether this is the right genus for the GOLD drinking-water child. |
| The current maintained decision is class-level only. | `curation/decisions.tsv:624` sets `review_depth` to `CLASS`; `docs/CURATION.md` and `docs/HARMONIZATION.md` state that only `ITEM` means the source path and candidate terms were examined. | Supported exactly. |
| The current `ENVO:03600004` parent is the immediate GOLD parent path. | `data/raw/gold_ecosystem_paths.tsv:889` contains the prefix path `Engineered > Built environment > Drinking water treatment plant`. | Supported as source-path context, but unsupported as an ontology `is-a` parent for a filter component. |
| The target has no MIxS triads to emit as `environmental_parameters`. | Ignored/hidden-inclusive exact search for the target path in `data/raw/gold_path_triads.tsv` found no rows. | Supported exactly. |
| No causal overlay is attached to `habitatmech:GOLD.697d4c6359`. | Ignored/hidden-inclusive exact search over `curation/causal_graphs` found no `habitatmech:GOLD.697d4c6359`, and `find curation/causal_graphs -maxdepth 1 -type f -name '*filter*' -print` returned no files. | Supported exactly. |

## Completeness

The generated record is complete for the current committed inputs but inherits one unsupported hierarchy claim from the source path. It has the GOLD aggregate row, the locked slug, one class-level decision, one additional biosample-path row, four study rows, no GOLD MIxS triads, no record-level evidence, no causal graph, no characteristic taxa, and no environmental parameters.

Ignored/hidden-inclusive exact searches covered `curation/decisions.tsv`, `curation/term_requests.tsv`, `curation/term_requests_excluded.tsv`, `history`, `research`, `reports`, `data/habitats/PATHS.tsv`, `data/habitats/engineered`, `data/raw/gold_ecosystem_paths.tsv`, `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_studies.tsv`, `data/raw/gold_path_triads.tsv`, `data/raw/ontology_terms.tsv`, `data/raw/ontology_subclass_edges.tsv`, and `curation/causal_graphs`. They found no target-specific term request, no target-specific history event, no committed research report, no causal overlay, and no exact `drinking water filter` ontology term.

The next curation pass should inspect the GOLD organism, biosample, and study context before defining the minted term. The raw path has more biosample and study inventory than the generated `ORGANISM` assertion count alone shows, but those rows are leads, not claim-level evidence for a definition.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | The target is left at a class-level `CONFIRM_UNGROUNDED` decision whose own note says habitathood was not assessed. That does not support the record-level conclusion that `Drinking water filter` has been reviewed and still lacks a fitting identity term, especially with the vendored `ENVO:03600086` `water filter` genus available as a broader candidate. | `curation/decisions.tsv:624`; add supporting definition and hierarchy in `curation/term_requests.tsv` if no exact term fits. |
| Major | `parent_habitats: ENVO:03600004` turns the GOLD parent path into an `is-a` edge from a filter to a drinking water treatment plant. The source path places the filter under the plant operationally, but `ENVO:03600004` denotes the plant building, not manufactured water-filter equipment or filter media. | `curation/term_requests.tsv`, using `parent_mode=REPLACE` if the curated genus should replace the inherited GOLD parent. |

## Recommended Edits

1. Reopen `habitatmech:GOLD.697d4c6359` in `curation/decisions.tsv` with `review_depth` `ITEM`; after exact ontology review, keep it `CONFIRM_UNGROUNDED` only if no exact drinking-water-filter class exists.
2. If item review confirms that the GOLD source denotes a drinking-water filter inside a treatment plant, add a `curation/term_requests.tsv` row for `habitatmech:GOLD.697d4c6359` with requested label `drinking water filter`, parent class `ENVO:03600086`, an evidence-backed definition, and `parent_mode` `REPLACE` so the generated record drops the false `ENVO:03600004` `is-a` parent.
3. Rerun `just seed`, canary `habitatmech:GOLD.697d4c6359`, apply the regenerated corpus, and validate that the generated record becomes item-reviewed with a true water-filter parent and no generated drift.

## Follow-up Checks

- `rg --no-ignore --hidden -n 'habitatmech:GOLD\.697d4c6359' curation/decisions.tsv curation/term_requests.tsv history research data/habitats/engineered`
- `just seed-canary habitatmech:GOLD.697d4c6359`
- `just seed-apply --force`
- `just validate data/habitats/engineered/drinking_water_filter.yaml`
- `just validate-strict data/habitats/engineered/drinking_water_filter.yaml`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just report`

## Additional Notes

The ignored/hidden-inclusive causal-overlay search found no target overlay, so no focused `just validate-causal curation/causal_graphs/<slug>.yaml` command applies to this record.
