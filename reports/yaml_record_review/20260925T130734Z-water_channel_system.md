# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/water_channel_system.yaml
- Started UTC: 2026-09-25T13:04:00Z
- Finished UTC: 2026-09-25T13:07:34Z
- Verdict: pass

## Target

Reviewed the complete generated record at `data/habitats/engineered/water_channel_system.yaml`. The record is the curated GOLD-only engineered habitat for `Engineered > Artificial ecosystem > Water channel system`, minted as `habitatmech:GOLD.87bf5e5370` and relabeled from GOLD's bare `Water channel system` source label to `artificial water channel system`.

The generated file has `definition_source: HabitatMech`, `habitat_category: ENGINEERED`, `grounding_status: UNGROUNDED`, and `mapping_status: REVIEWED`. Its parents are the curated ENVO genus `ENVO:00010622` `vivarium` and the inherited immediate GOLD path parent `habitatmech:GOLD.0acae9a1a4` `Artificial ecosystem`. Its only source attestation is GOLD node `gold.ecosystem:8489`.

The generated fields are owned by maintained inputs: the item-level grounding decision in `curation/decisions.tsv`, the authored label/definition/genus in `curation/term_requests.tsv`, and the committed GOLD path in `data/raw/gold_ecosystem_paths.tsv`. There is no target causal-graph overlay under `curation/causal_graphs/`.

## Validation

All required local checks passed:

- `just validate data/habitats/engineered/water_channel_system.yaml`
- `just validate-strict data/habitats/engineered/water_channel_system.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000 --status all --out /tmp/habitatmech-water-channel-system-worklist.tsv`
- `just report`

No validator was skipped.

## Identity and Grounding

The generated identifier, label, category, source attestation, and path slug agree with the maintained inputs. `data/raw/gold_ecosystem_paths.tsv` has the exact `Engineered > Artificial ecosystem > Water channel system` row at depth 3 with one GOLD node ID, zero `organism_count`, `study_count`, `biosample_count`, and `total_assertions` values in this bulk-export summary, and `gold.ecosystem:8489` as the node list. `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.87bf5e5370` to the stable `water_channel_system` slug.

The generated `UNGROUNDED` and `REVIEWED` statuses follow from an item-level `CONFIRM_UNGROUNDED` row for `habitatmech:GOLD.87bf5e5370` in `curation/decisions.tsv`. That row explicitly reads the GOLD branch as an experimental artificial-stream habitat and rejects exact identity to `ENVO:00010622` `vivarium`, `ENVO:00000121` `artificial channel`, `ENVO:00000079` `flume`, and `ENVO:01000620` `mesocosm`.

The authored label, definition, and ENVO genus follow from `curation/term_requests.tsv` row `habitatmech:GOLD.87bf5e5370`, with `parent_mode=ADD`; `ADD` correctly retains the inherited broader GOLD parent while adding `ENVO:00010622`. The committed Indoor artificial water-channel research report was written for the child `habitatmech:GOLD.b4e93f5d66`, but it explicitly identifies this missing parent and recommends the exact `artificial water channel system` label and definition now present in the record.

The internal `Water channel system` exact synonym is the expected source-label synonym added by `src/habitatmech/seed.py` when an authored definition relabels a non-PREGO minted concept. It is separate from the ENVO term-request row's blank `exact_synonym` column.

## Evidence

- Supported as generated GOLD provenance: exact ignored-inclusive searches found `gold.ecosystem:8489` and `Engineered > Artificial ecosystem > Water channel system` in `data/raw/gold_ecosystem_paths.tsv`, and the generated source attestation reproduces them.
- Supported as item-level grounding: `curation/decisions.tsv` confirms this source concept is a real habitat without an exact ontology identity, and the near-miss terms it names are present in `data/raw/ontology_terms.tsv`.
- Supported as authored definition and hierarchy: `curation/term_requests.tsv` defines `artificial water channel system` under `ENVO:00010622` `vivarium`, and `data/raw/ontology_terms.tsv` defines `ENVO:00010622` as `vivarium`.
- Supported as curation status: this record has one contributing source concept, and the source concept has an `ITEM` decision, so the generated `mapping_status: REVIEWED` follows from the decision table.

The record has no causal graphs, environmental parameters, characteristic taxa, datasets, discussions, or claim-level `EvidenceItem` objects to inspect.

## Completeness

The generated attestation is complete for the committed GOLD ecosystem inventory. The exact GOLD source path has one node ID, and the generated source attestation correctly omits a multi-node note.

Exact ignored-inclusive searches of the GOLD API side tables found no `gold.ecosystem:8489`, `habitatmech:GOLD.87bf5e5370`, or exact `Engineered > Artificial ecosystem > Water channel system` rows in `data/raw/gold_studies.tsv`, `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`, `data/raw/environment_parameters.tsv`, PREGO, BacDive, or Madin side tables; no study, biosample, MIxS triad, environmental-parameter, taxon, or source corroboration rows are committed for this exact concept.

Exact ignored-inclusive searches over `curation/causal_graphs/`, `conf/id_label_targets.yaml`, `reports/habitat_research_manifest.tsv`, and `reports/yaml_record_review/`, excluding generated `pages/` and `data/text_map/`, found no target causal overlay, label-correspondence residual, target-specific research-manifest entry, or prior exact review report for `habitatmech:GOLD.87bf5e5370`, `gold.ecosystem:8489`, or the exact source path. The only prior review hits for `Water channel system` are non-target mentions in the Artificial ecosystem parent review.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If future curation changes this grounding or the authored term request, rerun `just seed`, a focused `just seed-canary habitatmech:GOLD.87bf5e5370`, `just validate-strict data/habitats/engineered/water_channel_system.yaml`, `just term-requests-check`, `just validate-history`, `just validate-causal-all`, `just verify-corpus --max-diffs 1`, and `just report`.

## Additional Notes

The worklist output still lists `habitatmech:GOLD.87bf5e5370` because `just worklist --status all` ranks ungrounded records whether they are `SEEDED` or `REVIEWED`. Its presence there is not a defect.

All absence checks in this review used ignored-inclusive `rg --no-ignore --hidden` or `find`, bounded to maintained curation, history, research, raw inventory, generated habitat, configuration, and review-report paths. No negative claim relied on a search of rendered `pages/` or generated text-map JSON.
