# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/engineered/crustaceans_tank.yaml`
- Started UTC: `2026-09-24T22:04:12Z`
- Finished UTC: `2026-09-24T22:06:33Z`
- Verdict: needs curation

## Target

Reviewed the complete generated record at `data/habitats/engineered/crustaceans_tank.yaml`. The record is a GOLD-only engineered habitat for the canonical path `Engineered > Artificial ecosystem > Aquaculture > Crustaceans tank`, minted as `habitatmech:GOLD.21698a99df`.

The generated file has `grounding_status: UNGROUNDED` and `mapping_status: SEEDED`. Its only parent is the immediate GOLD source-path parent, `habitatmech:GOLD.0287e1b2a9` `Aquaculture`. Its only source attestation shows `gold.ecosystem:8013`, one GOLD organism assertion, and a note that two GOLD ecosystem node IDs share the canonical path.

## Validation

| Check | Result |
|---|---|
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-crustaceans_tank.md' -print` | Passed before this report was written; no existing exact `crustaceans_tank` review was found. `find` is not `.gitignore`-filtered. |
| `just validate data/habitats/engineered/crustaceans_tank.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/engineered/crustaceans_tank.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Focused causal overlay validator | Not applicable; an exact ignored-inclusive search in `curation/causal_graphs/` found no `habitatmech:GOLD.21698a99df`, `gold.ecosystem:8013`, `gold.ecosystem:8017`, `crustaceans_tank`, `Crustaceans tank`, or exact source-path overlay. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| Reference validator | Not applicable; the target record has no record-level `evidence` entries and no causal graph edges with citation references. |
| `just term-requests-check` | Passed; the generated ENVO term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; 3,206 expected records all exist on disk, with 0 missing, 0 extra, and 0 differing records. |
| `just worklist --limit 2000` | Passed; it reported 0 still-undecided ungrounded records and 1,810 decisions on file. |
| `just report` | Passed; the corpus report completed for 3,206 records. |
| `git diff --check` | Passed before this report was written. |

## Identity and Grounding

The generated identifier, label, category, parent, source attestation, and assertion count agree with the committed GOLD inventory. `data/raw/gold_ecosystem_paths.tsv` has the row `Engineered > Artificial ecosystem > Aquaculture > Crustaceans tank` at depth 4 with `gold_node_count` 2, `organism_count` 1, no study or biosample assertions in the aggregate ecosystem-path row, and node IDs `gold.ecosystem:8013|gold.ecosystem:8017`. `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.21698a99df` to the stable `crustaceans_tank` slug.

The record's `UNGROUNDED` status comes from `curation/decisions.tsv`, which has only a class-level `CONFIRM_UNGROUNDED` decision for `habitatmech:GOLD.21698a99df`. That row records a reproducible lexical miss against the vendored slice, but its note explicitly says the source concept's habitathood was not assessed.

The local ontology slice did not provide an exact crustaceans-tank or aquaculture-tank term in the bounded candidate search. Nearby terms need item review before this record is promoted: `ENVO:03600074` `aquaculture farm` is a plausible broader habitat target, `ENVO:03501254` `water tank` and `ENVO:00002196` `aquarium` are related container terms that do not exactly denote aquaculture crustacean tanks, `ENVO:00000294` `fish farm` is too narrow in the wrong organism direction, and `ENVO:01001249` `crustacean farming process` is a process rather than a habitat identity.

## Evidence

- Supported: the `GOLD` source attestation is traceable to `data/raw/gold_ecosystem_paths.tsv`, including the two collapsed GOLD node IDs and the single GOLD organism assertion that becomes `assertion_count: 1` with `assertion_unit: ORGANISM`.
- Supported: the sole generated parent, `habitatmech:GOLD.0287e1b2a9`, is the immediate GOLD path parent for `Engineered > Artificial ecosystem > Aquaculture`; that path is plausibly a broader aquaculture context for a crustacean tank.
- Supported: the `CONFIRM_UNGROUNDED` history event in the generated record mirrors the class-level decision row from `curation/decisions.tsv`.
- Supported side-table context: the raw GOLD inventories contain the direct zero-assertion `Engineered > Artificial ecosystem > Aquaculture > Crustaceans tank > Sediment` child at `gold.ecosystem:8014`, but they contain no exact biosample, study, or MIxS triad row for the parent `Crustaceans tank` path.
- Out of scope: two host-associated larva research reports mention the `Crustaceans tank` aquaculture branch as distinct rearing water that can be confused with crustacean larvae as hosts. They are not target-specific research reports or maintained inputs for this engineered parent record.
- Under-reviewed: the record has no item-level decision, authored definition, term request, record-level evidence, discussion, dataset, characteristic taxon, environmental parameter, or causal graph.

## Completeness

The absence of parent-path GOLD biosample, study, and MIxS triad rows is faithful to the committed source inventories. An ignored-inclusive search across `data/raw/` for `gold.ecosystem:8013`, `gold.ecosystem:8017`, and the Crustaceans tank source-path string found the canonical GOLD ecosystem-path row and the direct sediment child row, but no parent-path MIxS triad, biosample, or study row to audit.

Exact ignored-inclusive searches in `history/`, `research/`, `curation/term_requests.tsv`, `curation/causal_graphs/`, `conf/`, and `reports/yaml_record_review/` found no target-specific history entry, research report, minted definition, causal overlay, label-correspondence residual, or prior exact review report for `crustaceans_tank`, `habitatmech:GOLD.21698a99df`, `Crustaceans tank`, `gold.ecosystem:8013`, `gold.ecosystem:8017`, or the exact source path.

The generated sediment child at `data/habitats/engineered/sediment__f02aa11f.yaml` is consistent with the raw child path `Engineered > Artificial ecosystem > Aquaculture > Crustaceans tank > Sediment`, but it should be reviewed separately because it denotes sediment in this engineered tank rather than the tank itself.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | `Crustaceans tank` remains only class-reviewed even though the GOLD path places it under Aquaculture and nearby ontology terms require an item-level broader-term decision. | The only maintained decision is a `CLASS` `CONFIRM_UNGROUNDED` row whose note says habitathood was not assessed. The vendored slice has no exact crustaceans-tank term in the bounded candidate search, but it does have `aquaculture farm`, related `water tank` and `aquarium` near misses, and the non-habitat `crustacean farming process` near miss that a curator should explicitly accept or reject before promotion from `SEEDED`. | `curation/decisions.tsv`; if no exact term fits, `curation/term_requests.tsv` |

## Recommended Edits

1. Item-review `habitatmech:GOLD.21698a99df` in `curation/decisions.tsv` against the exact `Engineered > Artificial ecosystem > Aquaculture > Crustaceans tank` source path, `ENVO:03600074` `aquaculture farm`, `ENVO:03501254` `water tank`, `ENVO:00002196` `aquarium`, `ENVO:00000294` `fish farm`, and `ENVO:01001249` `crustacean farming process`.
2. If the item review confirms a real habitat with no exact ontology term, retain the minted identifier and either record a `GROUND_AS_PARENT` decision for a strictly broader term or leave a reviewed `CONFIRM_UNGROUNDED` decision with reasoning that rejects the broader candidates.
3. If no exact ontology term fits, define the minted Crustaceans tank concept in `curation/term_requests.tsv` with a true engineered-aquaculture tank genus and `parent_mode=ADD`, so regeneration keeps the source-path Aquaculture parent alongside any authored ontology parent.

## Follow-up Checks

- Run `just seed`, then `just seed-canary habitatmech:GOLD.21698a99df`, and inspect `data/habitats/engineered/crustaceans_tank.yaml` before any wider `just seed-apply --force`.
- Run `just validate data/habitats/engineered/crustaceans_tank.yaml`, `just validate-strict data/habitats/engineered/crustaceans_tank.yaml`, `just term-requests-check`, `just validate-history`, `just verify-corpus --max-diffs 1`, `just worklist --limit 2000`, `just report`, and `git diff --check` after the maintained input changes.

## Additional Notes

The review did not find a target causal overlay, so there was no focused `just validate-causal curation/causal_graphs/<slug>.yaml` invocation to run. The whole-overlay validator still passed.

The source-path edge from Crustaceans tank to its Aquaculture parent is plausible as a strict broader edge. The generated sediment child already inherits this record as a source-path parent, and that child deserves its own review because the containment edge is likely a weaker `is_a` claim than the tank-to-aquaculture edge.
