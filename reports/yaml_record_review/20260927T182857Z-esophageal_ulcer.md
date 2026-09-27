# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/host_associated/esophageal_ulcer.yaml
- Started UTC: 2026-09-27T18:28:57Z
- Finished UTC: 2026-09-27T18:28:57Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Record path | `data/habitats/host_associated/esophageal_ulcer.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.45b27bdccd` |
| Label | `Esophageal ulcer` |
| Habitat category | `HOST_ASSOCIATED` |
| Grounding status | `NOT_APPLICABLE` |
| Mapping status | `REVIEWED` |
| Maintained owner | Generated from `data/raw/gold_ecosystem_paths.tsv`, `data/habitats/PATHS.tsv`, and the item-level row in `curation/decisions.tsv`; do not hand-edit this YAML. |

The target is the reviewed, generated record for the GOLD source path
`Host-associated > Mammals: Human > Digestive system > Esophagus > Esophageal
ulcer`. `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.45b27bdccd` to the
`esophageal_ulcer` slug.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/esophageal_ulcer.yaml` | Pass. `linkml-validate` found no issues for this record. |
| `just validate-strict data/habitats/host_associated/esophageal_ulcer.yaml` | Pass. Strict closed-schema validation scanned 1 file with 0 files in error and 0 error rows. |
| `just validate-causal curation/causal_graphs/<overlay>.yaml` | Not applicable. Exact `find curation/causal_graphs -maxdepth 1 -type f -name '*esophageal*' -print` found no overlay for this record. |
| `just validate-causal-all` | Pass. All 32 causal-graph curation files and 32 graphs validated. |
| Reference validator | Not applicable. The record has no `evidence`, `datasets`, or `causal_graphs` references to validate. |
| `just term-requests-check` | Pass. The generated term-request table is current at 109 terms. |
| `just validate-history` | Pass. 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus` | Pass. 3,206 expected records were present with 0 missing, 0 extra, and 0 differing generated YAML files. |
| `just worklist --status all --out /tmp/habitatmech-esophageal-ulcer-worklist.tsv` | Pass. The worklist completed and wrote 953 ungrounded rows; this `NOT_APPLICABLE` target was absent. |
| `just report --out /tmp/habitatmech-esophageal-ulcer-report.tsv` | Pass. The corpus report completed and included this record as `NOT_APPLICABLE`, `REVIEWED`, sourced only from GOLD, carrying one parent habitat, and carrying zero direct upstream assertions. |
| `git diff --check` | Pass. No whitespace or patch errors after this report was written. |

## Identity and Grounding

| Claim | Evidence | Assessment |
|---|---|---|
| The generated record denotes the exact GOLD `Esophageal ulcer` path. | `data/raw/gold_ecosystem_paths.tsv` has a single exact `Host-associated > Mammals: Human > Digestive system > Esophagus > Esophageal ulcer` row with depth 5, leaf label `Esophageal ulcer`, one GOLD node id, and `gold.ecosystem:7023`. The generated record repeats that source path, source label, and GOLD node id. | Supported exactly. |
| The reviewed non-habitat disposition comes from an item-level curation decision rather than a class-level sweep. | `curation/decisions.tsv` has an `ITEM`-depth `NOT_APPLICABLE` decision for `habitatmech:GOLD.45b27bdccd`, with a note saying `'Esophageal ulcer' names a disease, an intervention, a sampling artefact or a no-value filler rather than a place.` | Supported. The target is correctly `REVIEWED` and does not remain in the `UNGROUNDED` lexical-miss bucket. |
| The immediate GOLD source-path parent is the human `Esophagus` record. | `data/raw/gold_ecosystem_paths.tsv` places `Esophageal ulcer` directly under `Host-associated > Mammals: Human > Digestive system > Esophagus`; `data/habitats/PATHS.tsv` maps the inherited parent `habitatmech:GOLD.974cd3759a` to `esophagus__e0ae9e65`; and `data/habitats/host_associated/esophagus__e0ae9e65.yaml` is the generated parent record for that human esophagus source path. | Supported as source-path hierarchy. |
| The exact ulcer path has no committed direct GOLD biosample, study, or MIxS triad side rows. | The exact `data/raw/gold_ecosystem_paths.tsv` row has `organism_count=0`, `study_count=0`, `biosample_count=0`, and `total_assertions=0`. Exact ignored-inclusive searches for `gold.ecosystem:7023` and the exact source path found no matching row in `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`, or `data/raw/gold_studies.tsv`. | Supported exactly. The generated source attestation correctly omits `assertion_count` and `assertion_unit`. |

## Evidence

The record has no authored definition, synonyms, xrefs, evidence entries,
environmental parameters, characteristic taxa, datasets, or causal graphs.

| Assertion | Evidence | Assessment |
|---|---|---|
| GOLD has a direct `Esophageal ulcer` path with one upstream node. | `data/raw/gold_ecosystem_paths.tsv` stores `gold_node_count=1` and only `gold.ecosystem:7023` for the exact path. | Supported exactly. |
| The record is a locked generated GOLD record. | `data/habitats/PATHS.tsv:1816` pins `habitatmech:GOLD.45b27bdccd` to `esophageal_ulcer`. | Supported exactly. |
| No target-specific review artifact supersedes the maintained `NOT_APPLICABLE` decision. | Exact ignored-inclusive searches for `habitatmech:GOLD.45b27bdccd`, `gold.ecosystem:7023`, `Esophageal ulcer`, and `esophageal_ulcer` found no causal overlay, history record, target-specific research report, prior exact YAML review report, term request, external xref, environment-parameter row, dataset row, biosample row, study row, or MIxS triad row for this record. | Supported exactly. |

No snippet or citation mismatch was present because this generated placeholder
record carries only source-inventory, reviewed non-habitat, and generated
source-hierarchy facts.

## Completeness

This generated record is sparse but faithful to the maintained inputs. It keeps
the GOLD source concept citable under a minted identifier while marking the
source leaf `NOT_APPLICABLE`, because an esophageal ulcer is a pathological
lesion context rather than a habitat identity to ground or an environment term
to request.

No consequential slot is underfilled:

- The item-level decision captures the full curator judgement needed for a
  `NOT_APPLICABLE` generated record.
- The sole source attestation carries the exact GOLD path, the sole GOLD node
  id, and the leaf label.
- The parent list preserves the immediate GOLD path parent, `Esophagus`, so the
  generated record remains browsable in its source hierarchy even though its
  own leaf is not a valid habitat identity.

Ignored- and hidden-file-inclusive exact searches covered `curation`, `history`,
`research`, `reports/yaml_record_review`, `data/raw`, `data/habitats`,
`conf`, `docs`, `src`, and `tests` for the target identifier, GOLD node id,
exact GOLD path, label, and slug. Separate `find` checks of `history`,
`curation/causal_graphs`, `research/habitats`, and `reports/yaml_record_review`
found no target-specific history record, causal overlay, research report, or
pre-existing exact review report.

## Findings

No blockers, major findings, or minor findings were found.

## Recommended Edits

None.

## Follow-up Checks

| Check | Purpose |
|---|---|
| Review `habitatmech:GOLD.974cd3759a` | Item-review the immediate human `Esophagus` source parent, which is still `NARROW` and `SEEDED`. |
| Review `Host-associated > Mammals > Digestive system > Esophagus` | Check the non-human mammal `Esophagus` sibling in a separate record review before relying on it as a comparison record. |
| Review `Host-associated > Birds > Digestive system > Esophagus` | Check the bird `Esophagus` sibling in a separate record review before relying on crop-associated child paths as evidence for or against this human ulcer leaf. |

## Additional Notes

- The absence checks in this review used `rg --no-ignore --hidden` and `find`,
  so ignored and hidden files were included.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*esophageal*' -print`
  found no pre-existing exact review report for this record before this file
  was written.
- The broader search for `Digestive system > Esophagus` found the non-human
  mammal and bird esophagus paths. Those rows are neighboring GOLD source
  concepts; they do not feed the zero-assertion human esophageal-ulcer leaf.
