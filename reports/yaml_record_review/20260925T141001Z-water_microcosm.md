# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/water_microcosm.yaml
- Started UTC: 2026-09-25T14:06:30Z
- Finished UTC: 2026-09-25T14:10:01Z
- Verdict: needs curation

## Target

Reviewed the complete generated record at `data/habitats/engineered/water_microcosm.yaml`. The record is the GOLD-only engineered habitat for `Engineered > Artificial ecosystem > Water microcosm`, minted as `habitatmech:GOLD.e55451492a`.

The generated file has `label: Water microcosm`, `habitat_category: ENGINEERED`, `grounding_status: UNGROUNDED`, and `mapping_status: SEEDED`. Its only generated parent is the immediate GOLD source-path parent `habitatmech:GOLD.0acae9a1a4` `Artificial ecosystem`. Its only source attestation is representative GOLD node `gold.ecosystem:6451`; the raw GOLD row collapses three node IDs, `gold.ecosystem:6451|gold.ecosystem:6452|gold.ecosystem:6453`, onto this exact path.

The file is generated from `data/raw/` and a class-level row in `curation/decisions.tsv`. No authored term request, source extractor override, or target causal-graph overlay currently contributes to this record. Future item review belongs in `curation/decisions.tsv`; a future path-qualified definition or multi-parent authored term belongs in `curation/term_requests.tsv`; future causal overlays belong under `curation/causal_graphs/`.

## Validation

All required local checks passed:

- `just validate data/habitats/engineered/water_microcosm.yaml`
- `just validate-strict data/habitats/engineered/water_microcosm.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000 --status all --out /tmp/habitatmech-water-microcosm-worklist.tsv`
- `just report`

No validator was skipped.

## Identity and Grounding

The generated identifier, label, category, source attestation, and path slug agree with the maintained inputs. `data/raw/gold_ecosystem_paths.tsv` has the exact `Engineered > Artificial ecosystem > Water microcosm` row at depth 3, with three GOLD node IDs, zero `organism_count`, `study_count`, `biosample_count`, and `total_assertions` values in the core bulk-export summary, and `gold.ecosystem:6451|gold.ecosystem:6452|gold.ecosystem:6453` as the node list. `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.e55451492a` to the stable `water_microcosm` slug.

The generated `UNGROUNDED` status follows from a class-level `CONFIRM_UNGROUNDED` row for `habitatmech:GOLD.e55451492a` in `curation/decisions.tsv`. That row only records that no lexical route matched the full `Water microcosm` label in the August 2026 sweep; by design, class-level rows do not establish the right broader term and do not promote the generated record to `REVIEWED`.

The vendored ontology slice contains `ENVO:01000621` `microcosm`, and the already-reviewed GOLD parent path `Engineered > Artificial ecosystem > Microcosm` exact-grounds to that term. The Water microcosm source concept is not exactly all microcosms, but its label and source path make `ENVO:01000621` a strictly broader parent in the same way that the prior Sand, Sediment, Seawater, and Soil microcosm reviews recommended `microcosm` as a parent for path-qualified microcosm children.

The GOLD API side tables add one contextual lead: `Gs0156825` is a two-path study that tags both `Engineered > Artificial ecosystem > Water microcosm` and `Environmental > Aquatic > Freshwater > Lake`; the 14 committed Water microcosm biosamples all carry a MIxS triad with `ENVO:01000252` `freshwater lake biome`, `ENVO:00000021` `freshwater lake`, and `ENVO:04000007` `lake water`. Those rows support a freshwater-lake source material or context for this particular water-microcosm batch. They do not make an engineered water microcosm identical to a freshwater lake or to lake water.

The inherited `habitatmech:GOLD.0acae9a1a4` parent is reproducible from the GOLD source hierarchy but unresolved as a strict broader class. That parent record still has only a class-level `CONFIRM_UNGROUNDED` row and a prior `needs curation` review.

## Evidence

- Supported as generated source provenance: exact ignored-inclusive searches found `gold.ecosystem:6451`, `gold.ecosystem:6452`, `gold.ecosystem:6453`, and the exact `Engineered > Artificial ecosystem > Water microcosm` row in `data/raw/gold_ecosystem_paths.tsv`; the generated source attestation reproduces the representative `gold.ecosystem:6451` node plus the multi-node note.
- Supported as supplemental source context: exact path searches found `data/raw/gold_studies.tsv`, `data/raw/gold_path_biosamples.tsv`, and `data/raw/gold_path_triads.tsv` rows for `Engineered > Artificial ecosystem > Water microcosm`.
- Supported as class-swept only: `curation/decisions.tsv` has only a `CLASS` review-depth row for `habitatmech:GOLD.e55451492a`; `just worklist --status all` still ranks the record and shows `ENVO:01000621=microcosm` as the sole lexical candidate; `curation/term_requests.tsv` has no matching `water microcosm` definition row.
- Supported as a missing broader parent: `data/raw/ontology_terms.tsv` defines `ENVO:01000621` as `microcosm`, and `data/raw/ontology_subclass_edges.tsv` places it under `ENVO:00010622` `vivarium`.

The record has no definition, environmental parameters, characteristic taxa, claim-level `EvidenceItem` objects, causal graphs, discussions, or datasets to inspect.

## Completeness

The generated source attestation is complete for the committed GOLD ecosystem inventory. `data/raw/gold_ecosystem_paths.tsv` lists all three source node IDs, and the generated note correctly says that three GOLD ecosystem node IDs share this path.

The supplemental GOLD API rows are present but not emitted into this generated record. `data/raw/gold_path_biosamples.tsv` records 14 biosamples for the `6453` ecosystem path ID; `data/raw/gold_studies.tsv` records `Gs0156825` as a two-path study shared with `Environmental > Aquatic > Freshwater > Lake`; and `data/raw/gold_path_triads.tsv` records the 14 Water microcosm samples' freshwater-lake biome, freshwater-lake local, and lake-water medium terms. Exact ignored-inclusive searches found no exact Water microcosm rows in `data/raw/environment_parameters.tsv`, PREGO, BacDive, or Madin side tables, so no environmental-parameter or taxon rows are committed for this exact concept.

Before this report was written, exact ignored-inclusive searches over `history/`, `research/habitats/`, `curation/causal_graphs/`, `curation/term_requests.tsv`, `curation/term_requests/`, `curation/term_requests_excluded.tsv`, `conf/id_label_targets.yaml`, and `reports/yaml_record_review/` found no target-specific append-only history record, research report, causal overlay, authored term request, generated ENVO term-request row, term-request exclusion, label-correspondence residual, or prior exact review report for `habitatmech:GOLD.e55451492a`, `gold.ecosystem:6451`, `gold.ecosystem:6452`, `gold.ecosystem:6453`, or the exact source path.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | `Engineered > Artificial ecosystem > Water microcosm` is only class-swept `UNGROUNDED`, but the vendored slice contains `ENVO:01000621` `microcosm`, a strictly broader parent for this engineered artificial-ecosystem path. | `curation/decisions.tsv` has only a `CLASS` `CONFIRM_UNGROUNDED` row for `habitatmech:GOLD.e55451492a`; `just worklist --status all` still ranks it for real curation with `ENVO:01000621=microcosm` as the sole candidate; `curation/term_requests.tsv` has no matching `water microcosm` definition row. | `curation/decisions.tsv`; optionally `curation/term_requests.tsv` after literature-supported definition work. |

No blockers or minor findings were found.

## Recommended Edits

1. Replace the class-level `curation/decisions.tsv` row for `habitatmech:GOLD.e55451492a` with an item-level `GROUND_AS_PARENT` decision targeting `ENVO:01000621` `microcosm`, with relation `NARROW`, curator/date metadata, and a note that GOLD's `Engineered > Artificial ecosystem > Water microcosm` source denotes an engineered water microcosm, not every microcosm.
2. In that item review, explicitly keep the freshwater-lake MIxS triad as contextual evidence from `Gs0156825`, not as an exact grounding to `ENVO:00000021` `freshwater lake` or `ENVO:04000007` `lake water`.
3. Do not add a `water microcosm` term request without separate literature support. This review verifies that `ENVO:01000621` is broader and that no exact vendored or pending term currently names Water microcosm, but it does not inspect literature sufficient to author a durable definition.
4. If a future definition pass does add `water microcosm`, consider whether `ENVO:04000007` `lake water` is too narrow for GOLD's generic Water microcosm branch and whether `parent_mode=ADD` should preserve the generated Artificial ecosystem parent.

## Follow-up Checks

- After updating `curation/decisions.tsv`, run `just seed`, `just seed-canary habitatmech:GOLD.e55451492a`, and inspect the regenerated `data/habitats/engineered/water_microcosm.yaml`.
- If the canary is correct, run `just seed-apply --force`, then `just validate data/habitats/engineered/water_microcosm.yaml`, `just validate-strict data/habitats/engineered/water_microcosm.yaml`, `just term-requests-check`, `just validate-history`, `just validate-causal-all`, `just verify-corpus --max-diffs 1`, `just worklist --limit 2000 --status all --out /tmp/habitatmech-water-microcosm-worklist.tsv`, and `just report`.
- Confirm the regenerated record has `grounding_status: NARROW`, `mapping_status: REVIEWED`, `parent_habitats` containing `ENVO:01000621`, and a `source_attestations` entry with `mapping_predicate: skos:narrowMatch`.

## Additional Notes

All absence checks in this review used ignored-inclusive `rg --no-ignore --hidden`, exact scans of the committed raw GOLD side tables, or `find`, bounded to maintained curation, history, research, raw inventory, generated habitat, label-residual, and review-report paths. No search depended on rendered `pages/` or text-map JSON.

The GOLD path `Engineered > Artificial ecosystem > Microcosm` already grounds exactly to `ENVO:01000621`, while several material-scoped microcosm children have already been reviewed as needing `ENVO:01000621` as a broader parent. Updating Water microcosm to the same broader parent would bring this parallel artificial-ecosystem path into the same hierarchy shape.
