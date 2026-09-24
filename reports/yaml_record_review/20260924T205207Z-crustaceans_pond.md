# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/engineered/crustaceans_pond.yaml`
- Started UTC: `2026-09-24T20:49:28Z`
- Finished UTC: `2026-09-24T20:52:07Z`
- Verdict: needs curation

## Target

Reviewed the complete generated record at `data/habitats/engineered/crustaceans_pond.yaml`. The record is a GOLD-only engineered habitat for the canonical path `Engineered > Artificial ecosystem > Aquaculture > Crustaceans pond`, minted as `habitatmech:GOLD.be4a7c95b6`.

The generated file has `grounding_status: UNGROUNDED` and `mapping_status: SEEDED`. Its only parent is the immediate GOLD source-path parent, `habitatmech:GOLD.0287e1b2a9` `Aquaculture`. Its only source attestation shows `gold.ecosystem:8002`, four GOLD organism assertions, and a note that two GOLD ecosystem node IDs share the canonical path.

## Validation

| Check | Result |
|---|---|
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-crustaceans_pond.md' -print` | Passed before this report was written; no existing exact `crustaceans_pond` review was found. `find` is not `.gitignore`-filtered. |
| `just validate data/habitats/engineered/crustaceans_pond.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/engineered/crustaceans_pond.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Focused causal overlay validator | Not applicable; an exact ignored-inclusive search in `curation/causal_graphs/` found no `habitatmech:GOLD.be4a7c95b6`, `gold.ecosystem:8002`, `gold.ecosystem:8003`, `crustaceans_pond`, `Crustaceans pond`, or exact Crustaceans pond source-path overlay. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| Reference validator | Not applicable; the target record has no record-level `evidence` entries and no causal graph edges with citation references. |
| `just term-requests-check` | Passed; the generated ENVO term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; 3,206 expected records all exist on disk, with 0 missing, 0 extra, and 0 differing records. |
| `just worklist --limit 2000` | Passed; it reported 0 still-undecided ungrounded records and 1,810 decisions on file. |
| `just report` | Passed; the corpus report completed for 3,206 records. |
| `git diff --check` | Passed before this report was written. |

## Identity and Grounding

The generated identifier, label, category, parent, source attestation, and assertion count agree with the committed GOLD inventory. `data/raw/gold_ecosystem_paths.tsv` has the row `Engineered > Artificial ecosystem > Aquaculture > Crustaceans pond` at depth 4 with `gold_node_count` 2, `organism_count` 4, no study or biosample assertions in the aggregate ecosystem-path row, and node IDs `gold.ecosystem:8002|gold.ecosystem:8003`. `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.be4a7c95b6` to the stable `crustaceans_pond` slug.

The record's `UNGROUNDED` status comes from `curation/decisions.tsv`, which has only a class-level `CONFIRM_UNGROUNDED` decision for `habitatmech:GOLD.be4a7c95b6`. That row records a reproducible lexical miss against the vendored slice, but its note explicitly says the source concept's habitathood was not assessed.

The local ontology slice did not provide an exact crustaceans-pond or crustacean-pond term in exact bounded searches across `data/raw/ontology_terms.tsv`, `curation/decisions.tsv`, `curation/term_requests.tsv`, `curation/term_requests/`, and `conf/id_label_targets.yaml`. Nearby terms do need item review before this record is promoted: `ENVO:03600074` `aquaculture farm` and `ENVO:00000033` `pond` are plausible broader habitat targets, while `ENVO:01001249` `crustacean farming process` is a process rather than a habitat identity.

## Evidence

- Supported: the `GOLD` source attestation is traceable to `data/raw/gold_ecosystem_paths.tsv`, including the two collapsed GOLD node IDs and the four GOLD organism assertions that become `assertion_count: 4` with `assertion_unit: ORGANISM`.
- Supported: the sole generated parent, `habitatmech:GOLD.0287e1b2a9`, is the immediate GOLD path parent for `Engineered > Artificial ecosystem > Aquaculture`.
- Supported: the `CONFIRM_UNGROUNDED` history event in the generated record mirrors the class-level decision row from `curation/decisions.tsv`.
- Supported side-table context: `data/raw/gold_path_biosamples.tsv` has six biosamples for the same Crustaceans pond path at upstream ecosystem path ID `8003`, and `data/raw/gold_studies.tsv` lists study `Gs0161494` across five paths, including the parent Crustaceans pond path and its sediment child.
- Out of scope for the parent: the only matching `data/raw/gold_path_triads.tsv` rows are for `Engineered > Artificial ecosystem > Aquaculture > Crustaceans pond > Sediment`, not for the parent pond itself. Those triads use `ENVO:03600074` as broad scale, `ENVO:00000033` as local scale, and `ENVO:00002007` as medium for the sediment child.
- Under-reviewed: the record has no item-level decision, authored definition, term request, record-level evidence, discussion, dataset, characteristic taxon, environmental parameter, or causal graph.

## Completeness

The absence of a parent-path `data/raw/gold_path_triads.tsv` row is faithful to the committed source inventories. An exact ignored-inclusive search across `data/raw/` for `gold.ecosystem:8002`, `gold.ecosystem:8003`, and the exact parent source path found the canonical GOLD ecosystem-path row, the biosample row for path ID `8003`, the multi-path `Gs0161494` study row, and the direct sediment child rows; it found no exact parent-path MIxS triad row to audit.

Exact ignored-inclusive searches in `history/`, `research/`, `curation/term_requests.tsv`, `curation/term_requests/`, and `conf/id_label_targets.yaml` found no target-specific research report, history entry, minted definition, generated term-request row, or label-correspondence residual for `crustaceans_pond`, `habitatmech:GOLD.be4a7c95b6`, `Crustaceans pond`, `gold.ecosystem:8002`, `gold.ecosystem:8003`, or the exact source path.

The generated sediment child at `data/habitats/engineered/sediment__79de4694.yaml` is consistent with the raw child path `Engineered > Artificial ecosystem > Aquaculture > Crustaceans pond > Sediment`, but it should be reviewed separately because it denotes sediment in this engineered pond, not the parent Crustaceans pond itself.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | `Crustaceans pond` remains only class-reviewed even though the GOLD path places it under Aquaculture and nearby ontology terms require an item-level broader-term decision. | The only maintained decision is a `CLASS` `CONFIRM_UNGROUNDED` row whose note says habitathood was not assessed. The vendored slice has no exact crustaceans-pond term in the bounded exact search, but it does have aquaculture-farm and pond broader candidates plus the non-habitat crustacean-farming process near miss that a curator should explicitly accept or reject before promotion from `SEEDED`. | `curation/decisions.tsv`; if no exact term fits, `curation/term_requests.tsv` |

## Recommended Edits

1. Item-review `habitatmech:GOLD.be4a7c95b6` in `curation/decisions.tsv` against the exact `Engineered > Artificial ecosystem > Aquaculture > Crustaceans pond` source path, `ENVO:03600074` `aquaculture farm`, `ENVO:00000033` `pond`, and `ENVO:01001249` `crustacean farming process`.
2. If the item review confirms a real habitat with no exact ontology term, retain a minted identifier and either record a `GROUND_AS_PARENT` decision for a strictly broader term or leave a reviewed `CONFIRM_UNGROUNDED` decision with reasoning that rejects the broader candidates.
3. If no exact ontology term fits, define the minted Crustaceans pond concept in `curation/term_requests.tsv` with a true engineered-aquaculture pond genus and `parent_mode=ADD`, so regeneration keeps the source-path Aquaculture parent alongside any authored ontology parent.

## Follow-up Checks

- Run `just seed`, then `just seed-canary habitatmech:GOLD.be4a7c95b6`, and inspect `data/habitats/engineered/crustaceans_pond.yaml` before any wider `just seed-apply --force`.
- Run `just validate data/habitats/engineered/crustaceans_pond.yaml`, `just validate-strict data/habitats/engineered/crustaceans_pond.yaml`, `just term-requests-check`, `just validate-history`, `just verify-corpus --max-diffs 1`, `just worklist --limit 2000`, `just report`, and `git diff --check` after the maintained input changes.

## Additional Notes

The review did not find a target causal overlay, so there was no focused `just validate-causal curation/causal_graphs/<slug>.yaml` invocation to run. The whole-overlay validator still passed.

The Crustaceans pond sediment child already inherits this record as a source-path parent. That generated edge deserves its own review: the child path has MIxS triads for `aquaculture farm`, `pond`, and `sediment`, and a contained sediment material is not automatically a subtype of the engineered pond that contains it.
