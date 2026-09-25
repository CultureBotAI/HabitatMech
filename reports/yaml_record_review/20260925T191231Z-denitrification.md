# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/engineered/denitrification.yaml`
- Started UTC: `2026-09-25T19:12:31Z`
- Finished UTC: `2026-09-25T19:12:45Z`
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.9097df4ce9` |
| Label | `Denitrification` |
| Category | `ENGINEERED` |
| Grounding | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Maintained source | generated from `data/raw/gold_ecosystem_paths.tsv`, `data/habitats/PATHS.tsv`, and the class-level row in `curation/decisions.tsv` |

Reviewed the complete generated record at `data/habitats/engineered/denitrification.yaml`. The record is a GOLD-only engineered habitat candidate for `Engineered > Bioreactor > Denitrification`, with representative source ID `gold.ecosystem:5851` and three collapsed GOLD ecosystem node IDs.

## Validation

| Check | Result |
|---|---|
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-denitrification.md' -print` | Passed before this report was written; no existing exact `denitrification` review was found. `find` is not `.gitignore`-filtered. |
| `just validate data/habitats/engineered/denitrification.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/engineered/denitrification.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Focused causal overlay validator | Not applicable; `find curation/causal_graphs -maxdepth 1 -type f -name 'denitrification.yaml' -print` found no target overlay. `find` is not `.gitignore`-filtered. |
| Reference validator | Not applicable; the generated GOLD-only record has no record-level `evidence` entries, no causal graph, and no environmental-parameter references. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the generated ENVO term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; 3,206 expected records all exist on disk, with 0 missing, 0 extra, and 0 differing records. |
| `just worklist --limit 2000 --status all --out /tmp/habitatmech-denitrification-worklist.tsv` | Passed; the worklist wrote 953 ungrounded rows to the requested `/tmp` TSV. |
| `just report` | Passed; the corpus report completed for 3,206 records. |
| `git diff --check` | Passed after this report was written. |

## Identity and Grounding

The generated identifier, label, category, source attestation, and source-derived parent agree with the committed GOLD inventory. `data/raw/gold_ecosystem_paths.tsv` has the collapsed path `Engineered > Bioreactor > Denitrification` at depth 3, `gold_node_count` 3, no direct organism, study, biosample, or total assertions, and `gold_node_ids` `gold.ecosystem:5851|gold.ecosystem:6985|gold.ecosystem:6986`. `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.9097df4ce9` to the stable `denitrification` slug.

The generated `parent_habitats` edge to `ENVO:00002123` `bioreactor` is plausibly strict and broader for a denitrification-bioreactor habitat. The vendored ENVO slice defines `bioreactor` as a biomaterial containment unit that hosts organisms and maintains conditions conducive to their metabolic activities, and the GOLD path places `Denitrification` directly under `Engineered > Bioreactor`.

The `UNGROUNDED` status is under-reviewed rather than wrong outright. The only maintained curation row for `habitatmech:GOLD.9097df4ce9` is a class-level `CONFIRM_UNGROUNDED` decision whose note explicitly says the habitat identity was not assessed. Exact ignored-inclusive searches found no exact `denitrification` or `denitrifying` term in `data/raw/ontology_terms.tsv`, and the `just report` class-sweep diagnostics did not find a now-matching vendored term for this path. That rules out a stale exact ontology hit but still leaves the key item-level question undecided: whether this GOLD path denotes a denitrification bioreactor habitat or a process-only grouping for denitrification-related bioreactors.

## Evidence

- Supported: the displayed source path, representative `gold.ecosystem:5851` source ID, three-node collapse, and first-shown note match `data/raw/gold_ecosystem_paths.tsv`.
- Supported side-table context: the exact parent path appears in `data/raw/gold_studies.tsv` for study `Gs0154595` and in `data/raw/gold_path_biosamples.tsv` with 8 biosamples for `gold.ecosystem:6986`. Those rows show that GOLD has submitter context on this path but do not currently populate the generated `source_attestations`, which are built from `gold_ecosystem_paths.tsv`.
- Supported: no parent-path MIxS triad currently corroborates a narrower ontology grounding. An exact search for `Engineered > Bioreactor > Denitrification\t` in `data/raw/gold_path_triads.tsv` and `data/raw/environment_parameters.tsv` found no row.
- Under-reviewed: the class-level `CONFIRM_UNGROUNDED` decision only confirms that no ontology term matched the isolated `Denitrification` label by the sweep's lexical routes. It does not decide whether the `Engineered > Bioreactor > Denitrification` source concept is a habitat, a process qualifier, a grouping node, or an ENVO term request candidate.
- No record-level citations, characteristic taxa, environmental parameters, authored definition, or causal edges are present, so there are no attached snippets or literature references to validate.

## Completeness

The committed source inventories are sufficient to explain the sparse generated record. Exact ignored-inclusive searches over `curation/`, `history/`, `research/`, `reports/`, `.claude/`, the focused generated target and path-lock files, and the focused GOLD side tables found the generated record, its stable `PATHS.tsv` row, the class-level `curation/decisions.tsv` row, the canonical `gold_ecosystem_paths.tsv` row, the parent-path study row, the parent-path biosample row, and woodchip-bioreactor child rows. They found no item-level decision, no term request, no history entry, no target-specific causal overlay, no parent-path MIxS triad row, and no prior exact review report before this report was written.

The empty optional slots are appropriate for a seeded GOLD record with no curated overlay. No maintained input currently provides a definition, characteristic taxa, environmental parameters, record-level cited evidence, causal edges, discussions, or datasets for the parent denitrification node.

The child `Woodchip Bioreactor (WBR)` and `Woodchip biofilm` rows in the GOLD side tables must stay separate from this parent review. They may eventually help review narrower descendant records, but they do not by themselves define the parent `Denitrification` source concept.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | `denitrification.yaml` is still a process-named, class-sweeped GOLD node with no item-level decision saying whether `Engineered > Bioreactor > Denitrification` is a habitat, a process qualifier, or a grouping node. | The only `curation/decisions.tsv` row for `habitatmech:GOLD.9097df4ce9` has `review_depth` `CLASS` and says the concept's habitat identity was not assessed. The generated record has no definition, no cited evidence, no term request, and no discussion that narrows the leaf label with its bioreactor path context. | `curation/decisions.tsv`; if retained as a novel habitat, also `curation/term_requests.tsv` |

## Recommended Edits

1. Item-review `habitatmech:GOLD.9097df4ce9` in `curation/decisions.tsv` against the exact `Engineered > Bioreactor > Denitrification` source path, `ENVO:00002123` `bioreactor`, and the parent-path study and biosample side-table rows.
2. Decide whether GOLD's parent `Denitrification` node denotes a denitrification bioreactor habitat or only a process/grouping node for descendant woodchip-bioreactor records.
3. If the source concept is a habitat and no exact ontology term exists, replace the class-level `CONFIRM_UNGROUNDED` row with an item-level decision and add a term-request row defining a denitrification-bioreactor habitat under `ENVO:00002123` with `parent_mode=ADD`.
4. If the source concept is not itself a habitat, replace the class-level row with an item-level non-habitat decision rather than leaving a process label as a candidate habitat record.

## Follow-up Checks

- `just seed`
- `just seed-canary habitatmech:GOLD.9097df4ce9`
- Inspect `data/habitats/engineered/denitrification.yaml`
- `just validate data/habitats/engineered/denitrification.yaml`
- `just validate-strict data/habitats/engineered/denitrification.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000`
- `just report`
- `git diff --check`

## Additional Notes

- No blocker finding was found: the generated YAML validates, its source attestation is internally consistent, and `ENVO:00002123` `bioreactor` is a plausible broader parent for a denitrification-bioreactor habitat.
- No minor finding was found.
- This review left generated products and curation inputs unchanged.
