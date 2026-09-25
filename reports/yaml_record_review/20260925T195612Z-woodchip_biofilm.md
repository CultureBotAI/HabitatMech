# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/engineered/woodchip_biofilm.yaml`
- Started UTC: `2026-09-25T19:56:12Z`
- Finished UTC: `2026-09-25T19:56:17Z`
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.f9d0b8af79` |
| Label | `Woodchip biofilm` |
| Category | `ENGINEERED` |
| Grounding | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Maintained source | generated from `data/raw/gold_ecosystem_paths.tsv`, `data/habitats/PATHS.tsv`, and the class-level row in `curation/decisions.tsv` |

Reviewed the complete generated record at `data/habitats/engineered/woodchip_biofilm.yaml`. The record is a GOLD-only engineered habitat candidate for `Engineered > Bioreactor > Denitrification > Woodchip Bioreactor (WBR) > Woodchip biofilm`, with source ID `gold.ecosystem:5853`.

## Validation

| Check | Result |
|---|---|
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-woodchip_biofilm.md' -print` | Passed before this report was written; no existing exact `woodchip_biofilm` review was found. `find` is not `.gitignore`-filtered. |
| `just validate data/habitats/engineered/woodchip_biofilm.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/engineered/woodchip_biofilm.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Focused causal overlay validator | Not applicable; `find curation/causal_graphs -maxdepth 1 -type f -name 'woodchip_biofilm.yaml' -print` found no target overlay. `find` is not `.gitignore`-filtered. |
| Reference validator | Not applicable; the generated GOLD-only record has no record-level `evidence` entries, no causal graph, and no environmental-parameter references. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the generated ENVO term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; 3,206 expected records all exist on disk, with 0 missing, 0 extra, and 0 differing records. |
| `just worklist --limit 0 --status all --out /tmp/habitatmech-woodchip-biofilm-worklist.tsv` | Passed; the worklist wrote 953 ungrounded rows to the requested `/tmp` TSV. |
| `just report` | Passed; the corpus report completed for 3,206 records. |

## Identity and Grounding

The generated identifier, label, category, source attestation, and source-derived parent agree with the committed GOLD inventory. `data/raw/gold_ecosystem_paths.tsv` has the canonical path `Engineered > Bioreactor > Denitrification > Woodchip Bioreactor (WBR) > Woodchip biofilm` at depth 5, `gold_node_count` 1, no direct organism, study, biosample, or total assertions, and `gold_node_ids` `gold.ecosystem:5853`. `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.f9d0b8af79` to the stable `woodchip_biofilm` slug.

The current `UNGROUNDED` status is under-reviewed. The only maintained curation row for `habitatmech:GOLD.f9d0b8af79` is a class-level `CONFIRM_UNGROUNDED` decision whose note explicitly says the habitat identity was not assessed. Exact ignored-inclusive searches found no exact target-specific item decision, term request, history entry, research report, target-specific causal overlay, or prior exact review report. A bounded `woodchip`, `wood chip`, `wood-chip`, and exact `WBR` search in `data/raw/ontology_terms.tsv` found no woodchip-specific or WBR-specific ontology term.

The vendored slice already has strict broader terms for two parts of this source path. `ENVO:00002034` `biofilm` exactly matches the GOLD MIxS `medium` slot for this path and is the most direct broader candidate for the source concept. `ENVO:00002123` `bioreactor` exactly matches the GOLD MIxS `local` slot, corroborating the engineered reactor context inherited from the parent `Woodchip Bioreactor (WBR)` source node.

## Evidence

- Supported: the displayed source path and `gold.ecosystem:5853` source ID match `data/raw/gold_ecosystem_paths.tsv`.
- Supported side-table context: the exact path appears in `data/raw/gold_studies.tsv` for study `Gs0154092` and in `data/raw/gold_path_biosamples.tsv` with 26 biosamples for `gold.ecosystem:5853`.
- Supported side-table context: `data/raw/gold_path_triads.tsv` has a three-slot MIxS triad for this exact path: broad `ENVO:01000313` `anthropogenic environment`, local `ENVO:00002123` `bioreactor`, and medium `ENVO:00002034` `biofilm`, each with 1 sample, 1 study, 1 distinct term, and 1.00 top share.
- Under-reviewed: the class-level `CONFIRM_UNGROUNDED` decision only confirms that no ontology term matched the isolated `Woodchip biofilm` label by the sweep's lexical routes. It does not decide whether the exact source concept should be `GROUND_AS_PARENT` to the existing generic `ENVO:00002034` `biofilm` term or should receive a new woodchip-biofilm term request under that parent.
- No record-level citations, characteristic taxa, environmental parameters, authored definition, or causal edges are present, so there are no attached snippets or literature references to validate.

## Completeness

The committed source inventories are sufficient to explain the sparse generated record. Exact ignored-inclusive searches over `data/raw/`, `curation/`, `history/`, `research/`, `reports/`, `.claude/`, the focused generated target, and the path-lock file found the generated record, its stable `PATHS.tsv` row, the class-level `curation/decisions.tsv` row, the canonical `gold_ecosystem_paths.tsv` row, the exact-path study row, the exact-path biosample row, and exact-path MIxS triad rows. They found no item-level decision, no term request, no history entry, no target-specific causal overlay, and no prior exact review report before this report was written.

The empty optional slots are appropriate for a seeded GOLD record with no curated overlay. No maintained input currently provides a definition, characteristic taxa, environmental parameters, record-level cited evidence, causal edges, discussions, or datasets for the `Woodchip biofilm` source concept.

The parent `Woodchip Bioreactor (WBR)` source concept was reviewed separately and found under-reviewed under a class-level `CONFIRM_UNGROUNDED` sweep. It must stay separate from this child review: the parent denotes a bioreactor system, while this target denotes a biofilm within that system.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | `woodchip_biofilm.yaml` is still `UNGROUNDED` under a class-level sweep even though GOLD's own MIxS triad and the vendored ontology support a strict broader `ENVO:00002034` `biofilm` parent. | The exact source path is `Engineered > Bioreactor > Denitrification > Woodchip Bioreactor (WBR) > Woodchip biofilm`; `data/raw/gold_path_triads.tsv` says its `env_medium` top term is `ENVO:00002034` `biofilm` with 1.00 share; and `data/raw/ontology_terms.tsv` contains generic `biofilm` but no exact woodchip/WBR term. The only `curation/decisions.tsv` row for `habitatmech:GOLD.f9d0b8af79` has `review_depth` `CLASS` and says the concept's habitat identity was not assessed. | `curation/decisions.tsv`; if retained as a novel habitat, also `curation/term_requests.tsv` |

## Recommended Edits

1. Item-review `habitatmech:GOLD.f9d0b8af79` in `curation/decisions.tsv` against the exact `Engineered > Bioreactor > Denitrification > Woodchip Bioreactor (WBR) > Woodchip biofilm` source path, `ENVO:00002034` `biofilm`, and the exact GOLD biosample, study, and MIxS triad side-table rows.
2. If no exact woodchip-biofilm ontology term is found, replace the class-level `CONFIRM_UNGROUNDED` row with an item-level `GROUND_AS_PARENT` row to `ENVO:00002034` `biofilm`.
3. If a curator chooses to author an exact woodchip-biofilm term, add the definition in `curation/term_requests.tsv` under `ENVO:00002034` with `parent_mode=ADD`.
4. Revisit the inherited `habitatmech:GOLD.b076c78736` `Woodchip Bioreactor (WBR)` parent after that parent has an item-level decision, so this child does not depend on an under-reviewed source-path node as its only parent.

## Follow-up Checks

- `just seed`
- `just seed-canary habitatmech:GOLD.f9d0b8af79`
- Inspect `data/habitats/engineered/woodchip_biofilm.yaml`
- `just validate data/habitats/engineered/woodchip_biofilm.yaml`
- `just validate-strict data/habitats/engineered/woodchip_biofilm.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000`
- `just report`
- `git diff --check`

## Additional Notes

- No blocker finding was found: the generated YAML validates, its source attestation is internally consistent, and the record denotes a biofilm within a woodchip bioreactor rather than a non-habitat.
- No minor finding was found.
- This review left generated products and curation inputs unchanged.
