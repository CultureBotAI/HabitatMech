# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/engineered/crustaceans_raceway.yaml`
- Started UTC: `2026-09-24T21:26:36Z`
- Finished UTC: `2026-09-24T21:28:49Z`
- Verdict: needs curation

## Target

Reviewed the complete generated record at `data/habitats/engineered/crustaceans_raceway.yaml`. The record is a GOLD-only engineered habitat for the canonical path `Engineered > Artificial ecosystem > Aquaculture > Crustaceans raceway`, minted as `habitatmech:GOLD.a904b6974e`.

The generated file has `grounding_status: UNGROUNDED` and `mapping_status: SEEDED`. Its only parent is the immediate GOLD source-path parent, `habitatmech:GOLD.0287e1b2a9` `Aquaculture`. Its only source attestation shows `gold.ecosystem:8015` and a note that two GOLD ecosystem node IDs share the same canonical path.

## Validation

| Check | Result |
|---|---|
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-crustaceans_raceway.md' -print` | Passed before this report was written; no existing exact `crustaceans_raceway` review was found. `find` is not `.gitignore`-filtered. |
| `just validate data/habitats/engineered/crustaceans_raceway.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/engineered/crustaceans_raceway.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Focused causal overlay validator | Not applicable; an exact ignored-inclusive search in `curation/causal_graphs/` found no `habitatmech:GOLD.a904b6974e`, `gold.ecosystem:8015`, `gold.ecosystem:8018`, `crustaceans_raceway`, `Crustaceans raceway`, or exact source-path overlay. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| Reference validator | Not applicable; the target record has no record-level `evidence` entries and no causal graph edges with citation references. |
| `just term-requests-check` | Passed; the generated ENVO term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; 3,206 expected records all exist on disk, with 0 missing, 0 extra, and 0 differing records. |
| `just worklist --limit 2000` | Passed; it reported 0 still-undecided ungrounded records and 1,810 decisions on file. |
| `just report` | Passed; the corpus report completed for 3,206 records. |
| `git diff --check` | Passed before this report was written. |

## Identity and Grounding

The generated identifier, label, category, parent, source attestation, and zero-assertion shape agree with the committed GOLD inventory. `data/raw/gold_ecosystem_paths.tsv` has the row `Engineered > Artificial ecosystem > Aquaculture > Crustaceans raceway` at depth 4 with `gold_node_count` 2, no direct GOLD organism, study, or biosample assertions, and node IDs `gold.ecosystem:8015|gold.ecosystem:8018`. `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.a904b6974e` to the stable `crustaceans_raceway` slug.

The record's `UNGROUNDED` status comes from `curation/decisions.tsv`, which has only a class-level `CONFIRM_UNGROUNDED` decision for `habitatmech:GOLD.a904b6974e`. That row records a reproducible lexical miss against the vendored slice, but its note explicitly says the source concept's habitathood was not assessed.

The local ontology slice did not provide an exact crustaceans-raceway or aquaculture-raceway term in the bounded candidate search. Nearby terms do need item review before this record is promoted: `ENVO:03600074` `aquaculture farm` is a plausible broader habitat target, `ENVO:03600047` `raceway pond` names an algae-specific raceway pond rather than this crustacean raceway, `ENVO:00000294` `fish farm` is too narrow in the wrong organism direction, and `ENVO:01001249` `crustacean farming process` is a process rather than a habitat identity.

## Evidence

- Supported: the `GOLD` source attestation is traceable to `data/raw/gold_ecosystem_paths.tsv`, including the two collapsed GOLD node IDs.
- Supported: the sole generated parent, `habitatmech:GOLD.0287e1b2a9`, is the immediate GOLD path parent for `Engineered > Artificial ecosystem > Aquaculture`; that path is plausibly a broader aquaculture context for a crustacean raceway.
- Supported: the `CONFIRM_UNGROUNDED` history event in the generated record mirrors the class-level decision row from `curation/decisions.tsv`.
- Supported side-table context: the raw GOLD inventories contain the direct zero-assertion `Engineered > Artificial ecosystem > Aquaculture > Crustaceans raceway > Sediment` child at `gold.ecosystem:8016`, but they contain no exact biosample, study, or MIxS triad row for the parent `Crustaceans raceway` path.
- Under-reviewed: the record has no item-level decision, authored definition, term request, record-level evidence, discussion, dataset, characteristic taxon, environmental parameter, or causal graph.

## Completeness

The absence of parent-path GOLD biosample, study, and MIxS triad rows is faithful to the committed source inventories. An exact ignored-inclusive search across `data/raw/`, `data/habitats/`, `curation/`, `history/`, `research/`, `conf/`, and `reports/yaml_record_review/` for `habitatmech:GOLD.a904b6974e`, `gold.ecosystem:8015`, `gold.ecosystem:8018`, `crustaceans_raceway`, and the exact source path found the class-level curation row, the canonical GOLD ecosystem-path row, the `PATHS.tsv` row, the generated target, and the generated sediment child; it found no item-level decision, term request, history entry, research report, label-correspondence residual, or prior exact review report.

The generated sediment child at `data/habitats/engineered/sediment__8fdad19e.yaml` is consistent with the raw child path `Engineered > Artificial ecosystem > Aquaculture > Crustaceans raceway > Sediment`, but it should be reviewed separately because it denotes sediment in this engineered raceway rather than the raceway itself.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | `Crustaceans raceway` remains only class-reviewed even though the GOLD path places it under Aquaculture and nearby ontology terms require an item-level broader-term decision. | The only maintained decision is a `CLASS` `CONFIRM_UNGROUNDED` row whose note says habitathood was not assessed. The vendored slice has no exact crustaceans-raceway term in the bounded candidate search, but it does have `aquaculture farm`, an algae-specific `raceway pond` near miss, and the non-habitat `crustacean farming process` near miss that a curator should explicitly accept or reject before promotion from `SEEDED`. | `curation/decisions.tsv`; if no exact term fits, `curation/term_requests.tsv` |

## Recommended Edits

1. Item-review `habitatmech:GOLD.a904b6974e` in `curation/decisions.tsv` against the exact `Engineered > Artificial ecosystem > Aquaculture > Crustaceans raceway` source path, `ENVO:03600074` `aquaculture farm`, `ENVO:03600047` `raceway pond`, `ENVO:00000294` `fish farm`, and `ENVO:01001249` `crustacean farming process`.
2. If the item review confirms a real habitat with no exact ontology term, retain the minted identifier and either record a `GROUND_AS_PARENT` decision for a strictly broader term or leave a reviewed `CONFIRM_UNGROUNDED` decision with reasoning that rejects the broader candidates.
3. If no exact ontology term fits, define the minted Crustaceans raceway concept in `curation/term_requests.tsv` with a true engineered-aquaculture raceway genus and `parent_mode=ADD`, so regeneration keeps the source-path Aquaculture parent alongside any authored ontology parent.

## Follow-up Checks

- Run `just seed`, then `just seed-canary habitatmech:GOLD.a904b6974e`, and inspect `data/habitats/engineered/crustaceans_raceway.yaml` before any wider `just seed-apply --force`.
- Run `just validate data/habitats/engineered/crustaceans_raceway.yaml`, `just validate-strict data/habitats/engineered/crustaceans_raceway.yaml`, `just term-requests-check`, `just validate-history`, `just verify-corpus --max-diffs 1`, `just worklist --limit 2000`, `just report`, and `git diff --check` after the maintained input changes.

## Additional Notes

The review did not find a target causal overlay, so there was no focused `just validate-causal curation/causal_graphs/<slug>.yaml` invocation to run. The whole-overlay validator still passed.

The source-path edge from Crustaceans raceway to its Aquaculture parent is plausible as a strict broader edge. The generated sediment child already inherits this record as a source-path parent, and that child deserves its own review because the containment edge is likely a weaker `is_a` claim than the raceway-to-aquaculture edge.
