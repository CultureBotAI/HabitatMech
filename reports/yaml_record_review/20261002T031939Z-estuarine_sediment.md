# YAML Record Review: Estuarine sediment

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/aquatic/estuarine_sediment.yaml`
- Started UTC: 2026-10-02T03:15:00Z
- Finished UTC: 2026-10-02T03:19:39Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.aed863b800` |
| Label | `Estuarine sediment` |
| File | `data/habitats/aquatic/estuarine_sediment.yaml` |
| Category | `AQUATIC` |
| Grounding | `UNGROUNDED` |
| Mapping | `SEEDED` |
| Source | GOLD `gold.ecosystem:7881` |
| GOLD path | `Environmental > Aquatic > Freshwater > Lake > Estuarine sediment` |
| Generated status | Generated from `data/raw/*`; `data/habitats/` is read-only generated output. |

The full generated YAML was read. The record has one GOLD source attestation, one parent, no definition, no xrefs, no environmental parameters, no characteristic taxa, no record-level evidence, no causal graphs, no discussions, and no datasets. Its only curated decision is a class-level `CONFIRM_UNGROUNDED` row; no item-level row has reviewed this exact GOLD source concept.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/estuarine_sediment.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/aquatic/estuarine_sediment.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus` | Passed; expected 3,206 records, found 3,206 on disk, 0 missing, 0 extra, 0 differing. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the generated term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records were valid against `src/habitatmech/schema/history.yaml`. |
| `just worklist --status all --out /tmp/habitatmech-estuarine-sediment-worklist.tsv` | Passed; wrote 953 ungrounded worklist rows. The exact row for `habitatmech:GOLD.aed863b800` has 5 assertions, one GOLD source path, `decided=TRUE`, and candidate terms `ENVO:03000033` `marine sediment`, `ENVO:00002113` `deep marine sediment`, and `ENVO:00002127` `stream sediment`. |
| `just report --out /tmp/habitatmech-estuarine-sediment-report.tsv` | Passed; the per-record row for `habitatmech:GOLD.aed863b800` reports `AQUATIC`, `UNGROUNDED`, `SEEDED`, source `GOLD`, 1 source, 5 assertions, `has_definition=False`, 1 parent, 0 parameters, 0 taxa, and 0 causal graphs at `data/habitats/aquatic/estuarine_sediment.yaml`. |

`iModulonDB` was not applicable: the record names no gene, locus tag, regulator, pathway, stress response, trait, or transcriptomics dataset.

## Identity and Grounding

The generated identifier, label, category, and GOLD attestation agree with the committed source inventory:

| Claim | Maintained input |
|---|---|
| Stable slug | `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.aed863b800` to `estuarine_sediment`. |
| Source path | `data/raw/gold_ecosystem_paths.tsv` has the exact path `Environmental > Aquatic > Freshwater > Lake > Estuarine sediment`. |
| Source node | The exact GOLD path has one node, `gold.ecosystem:7881`. |
| Source count | The exact GOLD path has 5 organism assertions, 0 studies, 0 biosamples, and 5 total assertions. |
| Curation row | `curation/decisions.tsv` has a `CONFIRM_UNGROUNDED` row for `habitatmech:GOLD.aed863b800`. |

The curation row is not enough to sign off the identity. It has `review_depth=CLASS` and says only that no term matched the label during the mechanical class-level sweep; by design it did not assess whether this exact GOLD path is a habitat, a duplicate of another source concept, or a candidate for a new term.

The lone `ENVO:00000021` parent is not supported as a strict broader habitat. `ENVO:00000021` is `freshwater lake`, while the GOLD leaf denotes sediment; the source path places the sediment in a freshwater-lake branch, but that containment is not an `is_a` claim from estuarine sediment to freshwater lake.

## Evidence

| Claim | Evidence checked | Assessment |
|---|---|---|
| The record denotes GOLD node `gold.ecosystem:7881`. | `data/raw/gold_ecosystem_paths.tsv` maps the exact canonical path to `gold.ecosystem:7881`, and the generated `source_attestations` row preserves that id. | Supported. |
| The record has 5 GOLD organism assertions. | The same source row has `organism_count=5` and `total_assertions=5`. | Supported. |
| The record is `AQUATIC`. | The exact GOLD path starts with `Environmental > Aquatic`. | Supported. |
| The record has no definition, parameters, taxa, evidence, causal graph, discussion, or dataset. | Exact hidden/ignored-inclusive searches over `data/raw`, maintained curation inputs, `history`, `research`, existing review reports, `data/habitats/PATHS.tsv`, generated habitat YAML, `src`, and rendered HTML found no maintained term request, causal overlay, history record, deep-research report, or environmental-parameter row for `habitatmech:GOLD.aed863b800`, `gold.ecosystem:7881`, or its exact source path. | Supported for the current maintained inputs. |
| The record should remain a separate ungrounded concept. | The only exact decision row is class-level, and the already-reviewed `Estuary: Sediment` report flagged this record as needing an item-level merge/split decision. | Unsupported until item review. |
| The record is a kind of freshwater lake. | This follows only from the inherited GOLD source-path parent. | Unsupported; the leaf is a sediment material, not a lake. |

The exact GOLD path is present only in `data/raw/gold_ecosystem_paths.tsv` among the raw GOLD tables; exact hidden/ignored-inclusive searches did not find it in `data/raw/gold_path_triads.tsv`, `data/raw/gold_path_biosamples.tsv`, or `data/raw/gold_studies.tsv`.

## Completeness

Consequential curation gaps remain:

- The exact source concept needs item-level review against `habitatmech:GOLD.4849010f40`, the separate GOLD record for `Environmental > Aquatic > Marine > Intertidal zone > Estuary: Sediment`.
- If the two GOLD concepts name the same estuarine-sediment material, this record should merge with the reviewed survivor through `SAME_AS`.
- If the freshwater/lake `Estuarine sediment` path is intentionally kept separate, this record needs an item-level decision explaining that split, a defensible broader material such as `ENVO:00002007` `sediment`, and suppression of the false source-path `freshwater lake` parent.

The empty optional slots are otherwise acceptable for the current inputs. No maintained row supplies a definition, causal graph, environmental parameter, characteristic taxon, discussion, or dataset for this source concept.

## Findings

| ID | Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| HM-ESTUARINE-SEDIMENT-001 | Major | `habitatmech:GOLD.aed863b800` has not been item-reviewed against the existing estuary-sediment GOLD concept. | The only maintained decision for `habitatmech:GOLD.aed863b800` is a class-level `CONFIRM_UNGROUNDED` row. A prior review of `habitatmech:GOLD.4849010f40` identified this source concept as a likely duplicate that must be deliberately merged with `SAME_AS` or kept separate with explicit evidence. | `curation/decisions.tsv`. |
| HM-ESTUARINE-SEDIMENT-002 | Major | `ENVO:00000021` `freshwater lake` is recorded as a parent even though the leaf denotes sediment. | The record lists `ENVO:00000021` in `parent_habitats` because the GOLD source path is under `Environmental > Aquatic > Freshwater > Lake`. A sediment material can be located in a lake, but it is not a subtype of the lake itself. | New maintained source-path parent-edge override in `curation/`, plus `src/habitatmech/seed.py` support for suppressing one inherited GOLD parent edge, unless this source is instead retired by `SAME_AS`. |

No blockers or minor findings were found.

## Recommended Edits

| Priority | Edit | Owner | Follow-up validator |
|---:|---|---|---|
| 1 | Item-review `habitatmech:GOLD.aed863b800` against `habitatmech:GOLD.4849010f40`. If `Environmental > Aquatic > Freshwater > Lake > Estuarine sediment` and `Environmental > Aquatic > Marine > Intertidal zone > Estuary: Sediment` are the same sediment habitat, replace the existing class-level row for `habitatmech:GOLD.aed863b800` with an item-level `SAME_AS` decision targeting `habitatmech:GOLD.4849010f40`. | `curation/decisions.tsv` | `just seed`, `just seed-canary habitatmech:GOLD.4849010f40`, `just verify-corpus`. |
| 2 | If the record intentionally remains separate, replace the class-level sweep row with an item-level decision that hangs the concept under a real broader material such as `ENVO:00002007` `sediment`. | `curation/decisions.tsv` | `just seed`, `just seed-canary habitatmech:GOLD.aed863b800`, then inspect `data/habitats/aquatic/estuarine_sediment.yaml` for `mapping_status: REVIEWED` and a `sediment` parent. |
| 3 | If the record intentionally remains separate, suppress only the inherited `Environmental > Aquatic > Freshwater > Lake` parent edge before reseeding. | New curation input plus `src/habitatmech/seed.py` | `just seed`, `just seed-canary habitatmech:GOLD.aed863b800`, then inspect the regenerated record to confirm `ENVO:00000021` is gone. |
| 4 | Add append-only curation history for the future merge-boundary or hierarchy correction. | `history/` | `just validate-history`. |

## Follow-up Checks

After curation, run:

- `just seed`
- `just seed-canary habitatmech:GOLD.4849010f40`, if merging with `SAME_AS`; otherwise `just seed-canary habitatmech:GOLD.aed863b800`
- `just validate data/habitats/aquatic/estuary_sediment.yaml`, if merging with `SAME_AS`; otherwise `just validate data/habitats/aquatic/estuarine_sediment.yaml`
- `just validate-strict data/habitats/aquatic/estuary_sediment.yaml`, if merging with `SAME_AS`; otherwise `just validate-strict data/habitats/aquatic/estuarine_sediment.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus`
- `just report`

Then manually confirm the regenerated corpus either merged `gold.ecosystem:7881` into the chosen estuary-sediment survivor as a second source attestation, or kept it as a reviewed separate source concept without the false freshwater-lake parent.

## Additional Notes

The rendered `pages/habitats/estuarine-sediment-habitatmech-gold-aed863b800.html` page mirrors the generated YAML.

Ignored files were included in all absence searches. `find reports/yaml_record_review -name '*estuarine_sediment*' -type f` found no prior exact report for this record; exact `rg --no-ignore --hidden` searches over raw data, maintained curation inputs, history, research, prior review reports, generated habitat YAML, `data/habitats/PATHS.tsv`, `src`, and rendered HTML found only the generated record/page, the PATHS row, the raw GOLD aggregate row, the class-level decision, and the prior `estuary_sediment` review's note that this record needs item-level review.
