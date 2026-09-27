# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/host_associated/periprosthetic_joint_hip.yaml
- Started UTC: 2026-09-27T17:38:50Z
- Finished UTC: 2026-09-27T17:38:50Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Record path | `data/habitats/host_associated/periprosthetic_joint_hip.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.459a01a714` |
| Label | `Periprosthetic joint: Hip` |
| Habitat category | `HOST_ASSOCIATED` |
| Grounding status | `NARROW` |
| Mapping status | `REVIEWED` |
| Maintained owner | Generated from `data/raw/gold_ecosystem_paths.tsv`, `data/habitats/PATHS.tsv`, and `curation/decisions.tsv`; do not hand-edit this YAML. |

The target is the reviewed, generated record for the GOLD source path
`Host-associated > Mammals: Human > Skeletal system > Periprosthetic joint:
Hip`. `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.459a01a714` to the
`periprosthetic_joint_hip` slug.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/periprosthetic_joint_hip.yaml` | Pass. `linkml-validate` found no issues for this record. |
| `just validate-strict data/habitats/host_associated/periprosthetic_joint_hip.yaml` | Pass. Strict closed-schema validation scanned 1 file with 0 files in error and 0 error rows. |
| `just validate-causal curation/causal_graphs/<overlay>.yaml` | Not applicable. Ignored-inclusive searches for `habitatmech:GOLD.459a01a714`, `gold.ecosystem:6590`, `gold.ecosystem:6591`, the exact GOLD path, and the slug found no causal-graph overlay for this record. |
| `just validate-causal-all` | Pass. All 32 causal-graph curation files and 32 graphs validated. |
| Reference validator | Not applicable. The record has no `evidence`, `datasets`, or `causal_graphs` references to validate. |
| `just term-requests-check` | Pass. The generated term-request table is current at 109 terms. |
| `just validate-history` | Pass. 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus` | Pass. 3,206 expected records were present with 0 missing, 0 extra, and 0 differing generated YAML files. |
| `just worklist --status all --out /tmp/habitatmech-worklist.tsv` | Pass. The worklist completed and wrote 953 ungrounded rows; this `NARROW` target was absent, while the broader `Periprosthetic joint` record appeared as a GOLD-only class-swept row. |
| `just report --out /tmp/habitatmech-report.tsv` | Pass. The corpus report completed and included this record as `NARROW`, `REVIEWED`, sourced only from GOLD, carrying two parent habitats, and carrying zero direct upstream assertions. |
| `git diff --check` | Pass before and after report creation. |

## Identity and Grounding

| Claim | Evidence | Assessment |
|---|---|---|
| The generated record denotes the exact GOLD `Periprosthetic joint: Hip` path, not the generic `Periprosthetic joint` path or the knee sibling. | `data/raw/gold_ecosystem_paths.tsv` has a single exact `Host-associated > Mammals: Human > Skeletal system > Periprosthetic joint: Hip` row with depth 4, leaf label `Periprosthetic joint: Hip`, two GOLD node IDs, and node IDs `gold.ecosystem:6590|gold.ecosystem:6591`. The generated record repeats the source path, source label, representative `gold.ecosystem:6590` ID, and two-node-collapse note. | Supported exactly. |
| The generated `BTO:0001457` `hip` parent comes from an item-level curation decision rather than a class-level sweep. | `curation/decisions.tsv` has an `ITEM`-depth `GROUND_AS_PARENT` decision for `habitatmech:GOLD.459a01a714` to `BTO:0001457` `hip`, with status `NARROW`. | Supported. The target stays minted and `NARROW` rather than claiming identity with the broader hip region. |
| The source-path `Skeletal system` parent is a generated broader host-associated context. | `data/raw/gold_ecosystem_paths.tsv` places `Periprosthetic joint: Hip` directly under `Host-associated > Mammals: Human > Skeletal system`; `data/habitats/PATHS.tsv` maps the inherited parent `habitatmech:GOLD.ea67ca30cb` to `skeletal_system__437a4825`; and the parent record denotes the human skeletal-system GOLD source path. | Supported as source-path hierarchy. |
| The exact hip path has no committed direct GOLD biosample, study, or MIxS triad side rows. | The exact `data/raw/gold_ecosystem_paths.tsv` row has `organism_count=0`, `study_count=0`, `biosample_count=0`, and `total_assertions=0`. Exact ignored-inclusive searches for `gold.ecosystem:6590`, `gold.ecosystem:6591`, and the exact source path found no matching row in `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`, or `data/raw/gold_studies.tsv`. | Supported exactly. The generic periprosthetic-joint sonicate-fluid child has MIxS triad and biosample rows, but those rows do not annotate this hip-specific leaf. |

## Evidence

The record has no authored definition, evidence entries, environmental
parameters, characteristic taxa, datasets, or causal graphs.

| Assertion | Evidence | Assessment |
|---|---|---|
| GOLD has a direct `Periprosthetic joint: Hip` path with two collapsed upstream nodes. | The exact `data/raw/gold_ecosystem_paths.tsv` row stores `gold_node_count=2` and `gold.ecosystem:6590|gold.ecosystem:6591`. | Supported exactly. |
| `BTO:0001457` is present in the vendored ontology slice as `hip`. | `data/raw/ontology_terms.tsv` defines `BTO:0001457` `hip` as the laterally projecting region of the mammalian trunk formed by pelvic and upper-femoral structures together with their fleshy coverings, and `data/habitats/host_associated/hip.yaml` is the generated `EXACT` PREGO record for that ontology term. | Supported as a broader anatomical-region term. |
| This hip-specific path is not backed by the generic periprosthetic-joint side rows. | The only committed periprosthetic biosample, study, and MIxS triad side rows are for `Host-associated > Mammals: Human > Skeletal system > Periprosthetic joint > Sonicate fluid`, a child of the separate generic `Periprosthetic joint` record. Exact ignored-inclusive searches found no committed side rows for `Periprosthetic joint: Hip` or `Periprosthetic joint: Hip > Sonicate fluid`. | Supported. The target's source attestation correctly omits `assertion_count` and `assertion_unit`. |

No snippet or citation mismatch was present because this generated placeholder
record carries only source-inventory, reviewed grounding, and generated
hierarchy facts.

## Completeness

This generated record is sparse but faithful to the maintained inputs. It
keeps a minted GOLD identity, the reviewed broader `BTO:0001457` hip parent,
the generated human skeletal-system source parent, and the exact GOLD source
attestation.

The hip-specific sonicate-fluid child remains class-swept and unreviewed, but
that does not invalidate this parent record. The generic `Periprosthetic joint`
record is also still a class-swept ungrounded placeholder; that broader curation
gap belongs to `habitatmech:GOLD.d113abe60e`, not to this already item-reviewed
hip target.

Ignored- and hidden-file-inclusive exact searches covered `data/raw`,
`data/habitats`, `curation`, `research`, `reports/yaml_record_review`,
`history`, `conf`, and generated habitat pages for the minted identifier, GOLD
node IDs, exact GOLD path, and slug. Targeted ignored-inclusive searches also
covered vendored ontology rows and source-adjacent hip, hip-joint, and
skeletal-joint candidates. A separate `find` check of `history`, `curation`,
`research/habitats`, and `reports/yaml_record_review` found no prior
`periprosthetic_joint_hip` review report, causal overlay, or research report.

## Findings

No blockers, major findings, or minor findings were found.

## Recommended Edits

None.

## Follow-up Checks

| Check | Purpose |
|---|---|
| Review `habitatmech:GOLD.d113abe60e` | Item-review the generic `Periprosthetic joint` parent, which still has only a class-level `CONFIRM_UNGROUNDED` decision despite ten direct GOLD organism assertions and one child path with 442 biosamples. |
| Review `habitatmech:GOLD.a170fb9296` | Item-review the hip-specific `Periprosthetic joint: Hip > Sonicate fluid` child before using it as evidence for or against the hip parent. |
| Review `habitatmech:GOLD.89edd438c6` | Check the analogous `Periprosthetic joint: Knee` record and its `BTO:0003595` parent in a separate record review. |

## Additional Notes

- The absence checks in this review used `rg --no-ignore --hidden` and `find`,
  so ignored and hidden files were included.
- `BTO:0001502` `hip joint` and `UBERON:0000982` `skeletal joint` are both
  present in the vendored slice, but neither is an exact identity for a
  periprosthetic site around a hip implant, and neither is currently linked from
  the committed `Periprosthetic joint: Hip` curation decision.
- The parent-level `Periprosthetic joint > Sonicate fluid` MIxS rows place
  `UBERON:0000982` `skeletal joint` in the local slot and `UBERON:0006314`
  `bodily fluid` in the medium slot for one triad-annotated study. They should
  not be projected onto the zero-assertion hip-specific GOLD path.
