# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/drinking_water_treatment_plant.yaml
- Started UTC: 2026-09-24T13:00:46Z
- Finished UTC: 2026-09-24T13:00:46Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Path | `data/habitats/engineered/drinking_water_treatment_plant.yaml` |
| Class | `HabitatRecord` |
| Identifier | `ENVO:03600004` |
| Label | `drinking water treatment plant` |
| Category | `ENGINEERED` |
| Generated or maintained | Generated from committed source inventories, the vendored ontology slice, and `data/habitats/PATHS.tsv`; `data/habitats/` remains read-only |
| Locked slug | `data/habitats/PATHS.tsv:926` maps `ENVO:03600004` to `drinking_water_treatment_plant` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |

## Validation

| Check | Result |
| --- | --- |
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-drinking_water_treatment_plant.md' -print` | Passed; no prior exact `drinking_water_treatment_plant` review was present before this report was written. `find` included ignored files under `reports/yaml_record_review`. |
| `just validate data/habitats/engineered/drinking_water_treatment_plant.yaml` | Passed; no LinkML issues found. |
| `just validate-strict data/habitats/engineered/drinking_water_treatment_plant.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Reference validator | Not applicable; the target record has no record-level `evidence`, no causal graph, and no DOI, PMID, or URL evidence items to validate. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; 3206 records were expected, 3206 were present, and there were 0 missing, extra, or differing records. |
| `just worklist --limit 2000` | Passed; 0 ungrounded records are still undecided and 1810 decisions are on file. |
| `just report` | Passed; completed the corpus report for 3206 records. |
| `git diff --check` | Passed before report creation. |

## Identity and Grounding

The current identity is generated from ENVO. `data/raw/ontology_terms.tsv:10053` labels `ENVO:03600004` as `drinking water treatment plant`, gives it the definition `An industrial building in which water undergoes a purification process to make it fit for human consumption.`, and leaves the `deprecated` column empty. `data/raw/ontology_subclass_edges.tsv:8448` asserts `ENVO:03600004 rdfs:subClassOf ENVO:00003861`, and `data/raw/ontology_terms.tsv:7401` identifies `ENVO:00003861` as `industrial building`.

The source attestation is otherwise traceable. `data/raw/gold_ecosystem_paths.tsv:889` lists the canonical path `Engineered > Built environment > Drinking water treatment plant`, leaf label `Drinking water treatment plant`, `gold_node_count` 3, `organism_count` 1, and node ids `gold.ecosystem:5491|gold.ecosystem:8451|gold.ecosystem:8452`. The generated attestation reports `gold.ecosystem:5491` as the first node id and records one `ORGANISM` assertion.

The exact source concept key is `habitatmech:GOLD.1a2ab4986f`, from `GOLD:Engineered > Built environment > Drinking water treatment plant`. An ignored/hidden-inclusive exact search over `curation`, `history`, `research`, `reports`, `data/habitats/PATHS.tsv`, and `data/habitats` found no maintained decision or generated curation event for that key, so `mapping_status: SEEDED` is appropriate.

The two parents are explainable. `ENVO:00003861` is the vendored ontology parent of `ENVO:03600004`, and `mesh:D000076624` is the generated record for the immediate GOLD parent path `Engineered > Built environment`.

## Evidence

| Claim | Evidence | Status |
| --- | --- | --- |
| The generated record denotes the ENVO class `ENVO:03600004` `drinking water treatment plant`. | `data/habitats/engineered/drinking_water_treatment_plant.yaml:1` and `data/raw/ontology_terms.tsv:10053` | Supported exactly. |
| `ENVO:03600004` is current in the vendored ontology slice. | `data/raw/ontology_terms.tsv:10053` leaves `deprecated` empty and sets `directly_referenced` to `TRUE`. | Supported exactly. |
| ENVO `drinking water treatment plant` is a subclass of `industrial building`. | `data/raw/ontology_subclass_edges.tsv:8448` asserts `ENVO:03600004 rdfs:subClassOf ENVO:00003861`. | Supported exactly. |
| The GOLD source path is `Engineered > Built environment > Drinking water treatment plant`. | `data/raw/gold_ecosystem_paths.tsv:889` lists that canonical path with leaf label `Drinking water treatment plant`. | Supported exactly. |
| The GOLD source has three node ids and one counted organism assertion in the aggregate path table. | `data/raw/gold_ecosystem_paths.tsv:889` reports `gold_node_count` 3, `organism_count` 1, `total_assertions` 1, and node ids `gold.ecosystem:5491|gold.ecosystem:8451|gold.ecosystem:8452`. | Supported exactly. |
| The exact GOLD source has been reviewed. | An ignored/hidden-inclusive exact search for `habitatmech:GOLD.1a2ab4986f` found no curation decision or history event. | Unsupported; the generated exact match is still only a seeded lexical grounding. |
| No causal overlay is attached to `ENVO:03600004`. | Ignored/hidden-inclusive exact search over `curation/causal_graphs` found no `identifier: ENVO:03600004`, and `find curation/causal_graphs -maxdepth 1 -type f -name '*treatment*' -print` returned no files. | Supported exactly. |

## Completeness

The generated record is complete for the current raw source row and the vendored ENVO row: it has the ENVO definition, the sole GOLD source path that exactly names a drinking-water treatment plant, the first of three GOLD ecosystem node ids, the GOLD assertion count, the ENVO subclass parent, and the inherited GOLD path parent. It has no synonyms, xrefs, environmental parameters, characteristic taxa, record-level evidence, causal graphs, discussions, datasets, or quality flags.

Ignored/hidden-inclusive exact searches covered `data/raw`, `curation`, `history`, `research`, `reports`, `data/habitats/PATHS.tsv`, and `data/habitats`. They found the ENVO term, ENVO subclass row, locked slug, GOLD path, GOLD node ids, BACDIVE and GOLD parent uses of `ENVO:03600004`, two generated GOLD child paths under this target, and a cooling-tower research report that mentions the term only as an adjacent built-water-facility pattern. They found no prior YAML review, term request, history record, causal overlay, or maintained curation decision for the target source concept `habitatmech:GOLD.1a2ab4986f`.

The generated `Drinking water` and `Drinking water filter` child records inherit `ENVO:03600004` from the raw GOLD child paths `Engineered > Built environment > Drinking water treatment plant > Drinking water` and `Engineered > Built environment > Drinking water treatment plant > Drinking water filter`. Those inherited `parent_habitats` edges follow the same GOLD parent path and are not an inconsistency.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

`data/raw/ontology_terms.tsv` has columns `term_id`, `ontology`, `label`, `definition`, `synonyms`, `deprecated`, `directly_referenced`, and `label_only`. On the `ENVO:03600004` row, `deprecated` is empty, `directly_referenced` is `TRUE`, and `label_only` is `FALSE`.
