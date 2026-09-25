# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/seawater_aquarium.yaml
- Started UTC: 2026-09-25T11:45:50Z
- Finished UTC: 2026-09-25T11:45:50Z
- Verdict: needs curation

## Target

Reviewed the complete generated record at `data/habitats/engineered/seawater_aquarium.yaml`. The record is a GOLD-only engineered habitat for `Engineered > Artificial ecosystem > Vivarium > Seawater aquarium`, currently carried as the minted identifier `habitatmech:GOLD.c483f43031`.

The generated file has `habitat_category: ENGINEERED`, `grounding_status: UNGROUNDED`, and `mapping_status: SEEDED`. Its only parent is `ENVO:00010622` `vivarium`, inherited from the immediate GOLD source-path parent after the parent path was grounded exactly to ENVO.

The file is generated from `data/raw/` and a class-level sweep row in `curation/decisions.tsv`; no item-level decision, authored term request, source extractor override, or causal-graph overlay currently contributes to this record. Future grounding changes belong in `curation/decisions.tsv`; future authored definition or parent-mode changes belong in `curation/term_requests.tsv`; future causal overlays belong under `curation/causal_graphs/`.

## Validation

All required local checks passed:

- `just validate data/habitats/engineered/seawater_aquarium.yaml`
- `just validate-strict data/habitats/engineered/seawater_aquarium.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000 --status all --out /tmp/habitatmech-seawater-aquarium-worklist.tsv`
- `just report`

No validator was skipped.

## Identity and Grounding

The generated identifier, label, category, source attestation, and path slug agree with the maintained inputs. `data/raw/gold_ecosystem_paths.tsv` has the exact `Engineered > Artificial ecosystem > Vivarium > Seawater aquarium` row at depth 4, with two GOLD node IDs, zero `organism_count`, `study_count`, `biosample_count`, and `total_assertions` values in this bulk-export summary, and `gold.ecosystem:8027|gold.ecosystem:8028` as the node list. `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.c483f43031` to the stable `seawater_aquarium` slug.

The broader parent is traceable and strictly broader. `data/raw/ontology_terms.tsv` defines `ENVO:00010622` with canonical label `vivarium`, and the reviewed generated Vivarium record shows `Engineered > Artificial ecosystem > Vivarium` is grounded exactly to that ENVO term. The Seawater aquarium source path is one GOLD level below Vivarium, so the generated parent does not collapse the child into its genus.

The `UNGROUNDED` grounding follows from `curation/decisions.tsv:1094`, which stores a `CONFIRM_UNGROUNDED` decision for `habitatmech:GOLD.c483f43031`, but the row has `review_depth` `CLASS`. `docs/HARMONIZATION.md` defines that sweep as a lexical no-match bucket and says it does not establish whether the concept is a habitat at all; `docs/CURATION.md` likewise says only `ITEM` review means the source path and candidate terms were examined. The `just worklist --status all` row for `habitatmech:GOLD.c483f43031` now lists `ENVO:00002197` `saline water aquarium`, via its exact synonym `salt water aquarium`, as a nearby candidate; that row also lists `ENVO:00002198` `fresh water aquarium` as a contrast term.

## Evidence

- Supported as generated source provenance: exact ignored-inclusive searches found `gold.ecosystem:8027`, `gold.ecosystem:8028`, and an exact tab-delimited `Engineered > Artificial ecosystem > Vivarium > Seawater aquarium` row in `data/raw/gold_ecosystem_paths.tsv`; `gold.ecosystem:8027` is the first node shown in the generated source attestation.
- Supported as generated hierarchy: the path parent `Engineered > Artificial ecosystem > Vivarium` resolves to `ENVO:00010622` `vivarium`, and this Seawater aquarium record is minted as a narrower child.
- Supported as unadjudicated candidate evidence: the vendored slice contains `ENVO:00002197` `saline water aquarium`, synonym `salt water aquarium`, as a subclass of `ENVO:00002196` `aquarium`; this should be read against GOLD's `Seawater aquarium` source label before the parent record remains minted.
- Supported as generated child hierarchy: the Biofilm and Sediment child records name `habitatmech:GOLD.c483f43031` as a parent, which follows from their `Engineered > Artificial ecosystem > Vivarium > Seawater aquarium > ...` GOLD paths.
- Not yet supported as individually reviewed identity: the only target decision is the class-level lexical sweep, and no item-level decision decides whether `ENVO:00002197` exactly fits this source path.

The record has no causal graphs, environmental parameters, characteristic taxa, datasets, discussions, or claim-level `EvidenceItem` objects to inspect.

## Completeness

The generated source attestation is complete for the committed GOLD ecosystem inventory. `data/raw/gold_ecosystem_paths.tsv` lists both source node IDs, and the generated record's first-node note accounts for the second node ID.

Exact ignored-inclusive searches of the GOLD API side tables found no `gold.ecosystem:8027`, `gold.ecosystem:8028`, or exact tab-delimited `Engineered > Artificial ecosystem > Vivarium > Seawater aquarium` rows in `data/raw/gold_studies.tsv`, `data/raw/gold_path_biosamples.tsv`, or `data/raw/gold_path_triads.tsv`; no GOLD study, biosample, or MIxS triad context is committed for this exact parent path.

Before this report was written, exact ignored-inclusive searches over `history/`, `research/habitats/`, `curation/causal_graphs/`, `curation/term_requests.tsv`, `curation/term_requests/`, `curation/term_requests_excluded.tsv`, `conf/id_label_targets.yaml`, and `reports/yaml_record_review/` found no target-specific append-only history record, research report, causal overlay, authored term request, generated ENVO term-request row, term-request exclusion, or label-correspondence residual for `habitatmech:GOLD.c483f43031`, `gold.ecosystem:8027`, or `gold.ecosystem:8028`. The exact `Seawater aquarium` label search found the raw parent and child paths, the generated parent and child YAML files, the Seawater aquarium Biofilm research report, and an out-of-scope sibling note in the prior Oceanarium report, but no prior Seawater aquarium review. Before this report was written, `find reports/yaml_record_review -maxdepth 1 -type f -iname '*seawater*aquarium*.md' -print` found no prior Seawater aquarium review report.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Seawater aquarium remains only class-swept even though the current vendored slice has a plausible exact aquarium candidate. | `curation/decisions.tsv:1094` is a `CLASS` `CONFIRM_UNGROUNDED` row for `habitatmech:GOLD.c483f43031`. `just worklist --status all` lists `ENVO:00002197` `saline water aquarium` / `salt water aquarium` as a candidate, and exact ignored-inclusive searches found no item-level decision or target-specific history for this identifier. | `curation/decisions.tsv`; if the source is still distinct after item review, `curation/term_requests.tsv` and a new append-only `history/` record. |

## Recommended Edits

1. Item-review `habitatmech:GOLD.c483f43031` against the exact `Engineered > Artificial ecosystem > Vivarium > Seawater aquarium` GOLD path, `ENVO:00002197` `saline water aquarium`, and nearby aquarium terms such as `ENVO:00002198` `fresh water aquarium`.
2. If `ENVO:00002197` is an exact fit, replace the class-level row in `curation/decisions.tsv` with an `ITEM` `GROUND` decision targeting `ENVO:00002197` and preserving the source-path rationale.
3. If no exact ontology term fits, replace the class-level row with an `ITEM` `CONFIRM_UNGROUNDED` decision documenting the checked candidates, and add a `curation/term_requests.tsv` row defining Seawater aquarium under `ENVO:00010622` `vivarium` or another reviewed genus with `parent_mode=ADD`.
4. Add an append-only `history/` record for that future curation session.

## Follow-up Checks

- After updating `curation/decisions.tsv` and, if needed, `curation/term_requests.tsv`, run `just seed`, `just seed-canary habitatmech:GOLD.c483f43031`, and inspect the regenerated `data/habitats/engineered/seawater_aquarium.yaml`.
- If the canary is correct, run `just seed-apply --force`, then `just validate-strict data/habitats/engineered/seawater_aquarium.yaml`, `just term-requests-check`, `just validate-history`, `just validate-causal-all`, `just verify-corpus --max-diffs 1`, and `just report`.
- If the future item review adds a causal overlay, run the focused `just validate-causal curation/causal_graphs/<slug>.yaml` before `just validate-causal-all`.

## Additional Notes

All absence checks in this review used ignored-inclusive `rg --no-ignore --hidden`, exact scans of the committed raw side tables, or `find`, bounded to maintained curation, history, research, raw inventory, generated habitat, label-residual, and review-report paths. No search depended on rendered `pages/` or text-map JSON.

The immediate Vivarium parent has already been reviewed with a `pass` verdict in `reports/yaml_record_review/20260925T102201Z-vivarium.md`. Its exact ENVO grounding makes the Seawater aquarium parent edge stronger than the earlier engineered records that still inherited `habitatmech:GOLD.0acae9a1a4` `Artificial ecosystem` directly.

The child Seawater aquarium Biofilm and Seawater aquarium Sediment records remain out of scope for this single-record review.
