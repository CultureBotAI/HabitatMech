# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/engineered/woodchip_bioreactor_wbr.yaml`
- Started UTC: `2026-09-25T19:35:13Z`
- Finished UTC: `2026-09-25T19:35:18Z`
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.b076c78736` |
| Label | `Woodchip Bioreactor (WBR)` |
| Category | `ENGINEERED` |
| Grounding | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Maintained source | generated from `data/raw/gold_ecosystem_paths.tsv`, `data/habitats/PATHS.tsv`, and the class-level row in `curation/decisions.tsv` |

Reviewed the complete generated record at `data/habitats/engineered/woodchip_bioreactor_wbr.yaml`. The record is a GOLD-only engineered habitat candidate for `Engineered > Bioreactor > Denitrification > Woodchip Bioreactor (WBR)`, with representative source ID `gold.ecosystem:5852` and two collapsed GOLD ecosystem node IDs.

## Validation

| Check | Result |
|---|---|
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-woodchip_bioreactor_wbr.md' -print` | Passed before this report was written; no existing exact `woodchip_bioreactor_wbr` review was found. `find` is not `.gitignore`-filtered. |
| `just validate data/habitats/engineered/woodchip_bioreactor_wbr.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/engineered/woodchip_bioreactor_wbr.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Focused causal overlay validator | Not applicable; `find curation/causal_graphs -maxdepth 1 -type f -name 'woodchip_bioreactor_wbr.yaml' -print` found no target overlay. `find` is not `.gitignore`-filtered. |
| Reference validator | Not applicable; the generated GOLD-only record has no record-level `evidence` entries, no causal graph, and no environmental-parameter references. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the generated ENVO term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; 3,206 expected records all exist on disk, with 0 missing, 0 extra, and 0 differing records. |
| `just worklist --limit 0 --status all --out /tmp/habitatmech-woodchip-bioreactor-worklist.tsv` | Passed; the worklist wrote 953 ungrounded rows to the requested `/tmp` TSV. |
| `just report` | Passed; the corpus report completed for 3,206 records. |
| `git diff --check` | Passed after this report was written. |

## Identity and Grounding

The generated identifier, label, category, source attestation, and source-derived parent agree with the committed GOLD inventory. `data/raw/gold_ecosystem_paths.tsv` has the collapsed path `Engineered > Bioreactor > Denitrification > Woodchip Bioreactor (WBR)` at depth 4, `gold_node_count` 2, no direct organism, study, biosample, or total assertions, and `gold_node_ids` `gold.ecosystem:5852|gold.ecosystem:5951`. `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.b076c78736` to the stable `woodchip_bioreactor_wbr` slug.

The current `UNGROUNDED` status is under-reviewed. The only maintained curation row for `habitatmech:GOLD.b076c78736` is a class-level `CONFIRM_UNGROUNDED` decision whose note explicitly says the habitat identity was not assessed. Exact ignored-inclusive searches found no exact target-specific item decision, term request, history entry, research report, target-specific causal overlay, or prior exact review report. The vendored slice also has no woodchip-specific or WBR-specific ontology term: a bounded `woodchip`, `wood chip`, `wood-chip`, and `wbr` search in `data/raw/ontology_terms.tsv` found only the unrelated `drawbridge` label via the substring `wbr`.

The generated source-path parent, `habitatmech:GOLD.9097df4ce9` `Denitrification`, is plausibly broader only if the parent source node is item-reviewed as a denitrification-bioreactor habitat. That parent was reviewed separately and was also found under-reviewed under a class-level `CONFIRM_UNGROUNDED` sweep. The more immediate gap in this child is the missing item-level broader grounding to `ENVO:00002123` `bioreactor`; the vendored ENVO slice defines `bioreactor` as a biomaterial containment unit capable of containing environmental material that hosts active organisms and maintaining conditions for their metabolic activities, and the source path and label both identify this target as a bioreactor.

## Evidence

- Supported: the displayed source path, representative `gold.ecosystem:5852` source ID, two-node collapse, and first-shown note match `data/raw/gold_ecosystem_paths.tsv`.
- Supported side-table context: the exact parent path appears in `data/raw/gold_studies.tsv` for study `Gs0154205` and in `data/raw/gold_path_biosamples.tsv` with 8 biosamples for `gold.ecosystem:5951`. Those rows show that GOLD has submitter context on this path but do not currently populate the generated `source_attestations`, which are built from `gold_ecosystem_paths.tsv`.
- Supported: no Woodchip Bioreactor MIxS triad currently corroborates a narrower ontology grounding. An exact search for `Engineered > Bioreactor > Denitrification > Woodchip Bioreactor (WBR)\t` in `data/raw/gold_path_triads.tsv` and `data/raw/environment_parameters.tsv` found no row.
- Under-reviewed: the class-level `CONFIRM_UNGROUNDED` decision only confirms that no ontology term matched the isolated `Woodchip Bioreactor (WBR)` label by the sweep's lexical routes. It does not decide whether the exact source concept should be `GROUND_AS_PARENT` to the existing generic `ENVO:00002123` `bioreactor` term or should receive a new woodchip-bioreactor term request under that parent.
- No record-level citations, characteristic taxa, environmental parameters, authored definition, or causal edges are present, so there are no attached snippets or literature references to validate.

## Completeness

The committed source inventories are sufficient to explain the sparse generated record. Exact ignored-inclusive searches over `curation/`, `history/`, `research/`, `reports/`, `.claude/`, the focused generated target and path-lock files, and the focused GOLD side tables found the generated record, its stable `PATHS.tsv` row, the class-level `curation/decisions.tsv` row, the canonical `gold_ecosystem_paths.tsv` row, the parent-path study row, the parent-path biosample row, and child woodchip-biofilm rows. They found no item-level decision, no term request, no history entry, no target-specific causal overlay, no parent-path MIxS triad row, and no prior exact review report before this report was written.

The empty optional slots are appropriate for a seeded GOLD record with no curated overlay. No maintained input currently provides a definition, characteristic taxa, environmental parameters, record-level cited evidence, causal edges, discussions, or datasets for the parent Woodchip Bioreactor node.

The child `Woodchip biofilm` rows in the GOLD side tables must stay separate from this parent review. They may eventually help review the descendant biofilm record, but they do not by themselves define the parent `Woodchip Bioreactor (WBR)` source concept.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | `woodchip_bioreactor_wbr.yaml` is still `UNGROUNDED` under a class-level sweep even though the vendored ontology contains a strict broader `ENVO:00002123` `bioreactor` parent. | The exact source path is `Engineered > Bioreactor > Denitrification > Woodchip Bioreactor (WBR)`, the source label itself names a bioreactor, and `data/raw/ontology_terms.tsv` contains generic `ENVO:00002123` `bioreactor` but no exact woodchip/WBR term. The only `curation/decisions.tsv` row for `habitatmech:GOLD.b076c78736` has `review_depth` `CLASS` and says the concept's habitat identity was not assessed. | `curation/decisions.tsv`; if retained as a novel habitat, also `curation/term_requests.tsv` |

## Recommended Edits

1. Item-review `habitatmech:GOLD.b076c78736` in `curation/decisions.tsv` against the exact `Engineered > Bioreactor > Denitrification > Woodchip Bioreactor (WBR)` source path, `ENVO:00002123` `bioreactor`, and the parent-path study and biosample side-table rows.
2. If no exact woodchip-bioreactor ontology term is found, replace the class-level `CONFIRM_UNGROUNDED` row with an item-level `GROUND_AS_PARENT` row to `ENVO:00002123` `bioreactor`.
3. If a curator chooses to author an exact woodchip-bioreactor term, add the definition in `curation/term_requests.tsv` under `ENVO:00002123` with `parent_mode=ADD`.
4. Revisit the inherited `habitatmech:GOLD.9097df4ce9` `Denitrification` parent after that parent has an item-level decision, so this child does not depend on an under-reviewed process-named source-path node as its only parent.

## Follow-up Checks

- `just seed`
- `just seed-canary habitatmech:GOLD.b076c78736`
- Inspect `data/habitats/engineered/woodchip_bioreactor_wbr.yaml`
- `just validate data/habitats/engineered/woodchip_bioreactor_wbr.yaml`
- `just validate-strict data/habitats/engineered/woodchip_bioreactor_wbr.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000`
- `just report`
- `git diff --check`

## Additional Notes

- No blocker finding was found: the generated YAML validates, its source attestation is internally consistent, and the record denotes a bioreactor rather than a non-habitat.
- No minor finding was found.
- This review left generated products and curation inputs unchanged.
