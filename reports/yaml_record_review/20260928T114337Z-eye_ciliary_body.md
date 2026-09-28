# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/eye_ciliary_body.yaml`
- Started UTC: 2026-09-28T11:43:37Z
- Finished UTC: 2026-09-28T11:43:53Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Record path | `data/habitats/host_associated/eye_ciliary_body.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.4d81fdaa51` |
| Label | `Eye: Ciliary body` |
| Habitat category | `HOST_ASSOCIATED` |
| Grounding status | `NARROW` |
| Mapping status | `REVIEWED` |
| Parent habitats | `UBERON:0000970`, `habitatmech:GOLD.020f82703b` |
| Maintained owner | Generated from `data/raw/gold_ecosystem_paths.tsv`, `curation/decisions.tsv`, and `data/habitats/PATHS.tsv`; do not hand-edit this YAML. |

The target is the GOLD record for `Host-associated > Mammals: Human > Visual
system > Eye: Ciliary body`. `data/habitats/PATHS.tsv` maps
`habitatmech:GOLD.4d81fdaa51` to `eye_ciliary_body`, while
`habitatmech:GOLD.aceda5f881` keeps the collision-resolved
`eye_ciliary_body__832768c5` slug for the parallel `Host-associated > Mammals >
Visual system > Eye: Ciliary body` source path.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/eye_ciliary_body.yaml` | Pass. `linkml-validate` reported `No issues found`. |
| `just validate-strict data/habitats/host_associated/eye_ciliary_body.yaml` | Pass. Strict closed-schema validation scanned 1 file with 0 files in error and 0 total error rows. |
| `just validate-causal curation/causal_graphs/<overlay>.yaml` | Not applicable. Ignored- and hidden-file-inclusive searches found no maintained causal-graph overlay for `habitatmech:GOLD.4d81fdaa51`. |
| `just validate-causal-all` | Pass. All 32 causal-graph curation files and 32 graphs validated. |
| Reference validator | Not applicable. The generated record has no `evidence`, `datasets`, or `causal_graphs` references. |
| `just term-requests-check` | Pass. The generated term-request table is current at 109 terms. |
| `just validate-history` | Pass. 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus` | Pass. 3,206 expected records were present with 0 missing, 0 extra, and 0 differing generated YAML files. |
| `just worklist --status all --out /tmp/habitatmech-eye-ciliary-worklist.tsv` | Pass. Wrote 953 ungrounded rows; this `NARROW` record correctly did not appear in that ungrounded worklist. |
| `just report --out /tmp/habitatmech-eye-ciliary-report.tsv` | Pass. Wrote the 3,206-record corpus TSV and listed this record at row 1859 as `NARROW`, `REVIEWED`, GOLD-only, 0 direct assertions, two parents, no parameters, no taxa, and no causal graphs. |

## Identity and Grounding

| Claim | Evidence | Assessment |
|---|---|---|
| The generated record denotes GOLD's human ciliary-body source concept. | `data/raw/gold_ecosystem_paths.tsv` has an exact row for `Host-associated > Mammals: Human > Visual system > Eye: Ciliary body` with leaf label `Eye: Ciliary body`, depth 4, `gold_node_count=1`, 0 direct assertions, and `gold.ecosystem:6183`; the generated `source_attestations` entry repeats the same source ID, label, and path. | Supported exactly. |
| `mapping_status: REVIEWED` follows from maintained inputs. | The sole GOLD source concept has an `ITEM` decision in `curation/decisions.tsv`, and the generated history records the resulting `GROUND_AS_PARENT` event. | Mechanically supported, although that reviewed decision is wrong; see Findings. |
| `UBERON:0000970` is a broader term, not an exact identity. | The vendored ontology slice labels `UBERON:0000970` as `eye`. The ciliary body is a part of the eye, as the decision note says; it is not identical to the whole eye. | The broader relationship is sound. |
| The generated record should not retain a minted GOLD identity. | `data/raw/ontology_terms.tsv` contains `BTO:0000260` with the exact label `ciliary body` and a definition for the ciliary-body tissue that includes muscles acting on the eye lens and ciliary epithelium secreting aqueous humour. GOLD's colon-formatted leaf `Eye: Ciliary body` denotes that same anatomical structure under the eye path. | Unsupported as curated. `curation/decisions.tsv` should ground this source concept exactly to `BTO:0000260`, not only hang a minted identity under `UBERON:0000970`. |
| The inherited GOLD parent remains broader. | `habitatmech:GOLD.020f82703b` is the generated source-path parent for `Host-associated > Mammals: Human > Visual system`, which is broader than `Eye: Ciliary body`. | Supported. |

## Evidence

| Assertion | Evidence | Assessment |
|---|---|---|
| The target GOLD source path has no direct GOLD organism, study, or biosample assertions. | The exact `data/raw/gold_ecosystem_paths.tsv` row for `gold.ecosystem:6183` has zero organism, study, biosample, and total assertions. Ignored- and hidden-file-inclusive anchored searches found no exact target row in `data/raw/gold_path_triads.tsv` or `data/raw/gold_path_biosamples.tsv`; a separator-aware exact-path search found no direct hit in `data/raw/gold_studies.tsv`, whose only `Eye: Ciliary body` substring hit is the aqueous-humor child path. | Supported; empty `assertion_count` and `environmental_parameters` are expected. |
| A parallel Mammals-path source concept has the same source leaf and the same grounding defect. | `habitatmech:GOLD.aceda5f881` at `data/habitats/host_associated/eye_ciliary_body__832768c5.yaml` has `source_path: Host-associated > Mammals > Visual system > Eye: Ciliary body` and the same broader-only `GROUND_AS_PARENT` decision to `UBERON:0000970` in `curation/decisions.tsv`. | Supported as sibling context. This review is for `habitatmech:GOLD.4d81fdaa51`, but a future fix should inspect both ciliary-body rows. |
| The aqueous-humor child is a separate, narrower source concept. | `data/habitats/host_associated/intraocular_fluid_aqueous_humor__548ffdf6.yaml` has source ID `gold.ecosystem:6184`, the child path `Host-associated > Mammals: Human > Visual system > Eye: Ciliary body > Intraocular fluid/Aqueous humor`, and parent `habitatmech:GOLD.4d81fdaa51`. | Supported; its separate reviewed aqueous-humor decision is not evidence that the parent ciliary-body identity should stay minted. |

The generated target has no claim-level `evidence` entries, no
`characteristic_taxa`, no `environmental_parameters`, and no causal graph edges.

## Completeness

The record is structurally complete for its current generated state, but not
semantically complete as a reviewed habitat. GOLD `gold.ecosystem:6183` has an
item-level decision, a source-path parent, a reproducible path lock entry, and
generated curation history. It correctly leaves direct assertion counts and MIxS
environmental parameters empty because the exact GOLD row has no direct sample
or study support.

The consequential gap is exact anatomy grounding: the vendored slice already
has `BTO:0000260` `ciliary body`, and no maintained decision row currently uses
that term. Ignored- and hidden-file-inclusive searches covered
`curation/causal_graphs`, `history`, `research`, `reports/yaml_record_review`,
`reports/habitat_research_manifest.tsv`, `curation/decisions.tsv`, `data/raw`,
and `data/habitats` for `habitatmech:GOLD.4d81fdaa51`,
`gold.ecosystem:6183`, `Eye: Ciliary body`, `eye_ciliary_body`, and
`BTO:0000260`. They found the generated target, the maintained path and
decision rows, the parallel ciliary-body record, the aqueous-humor child, and
the exact BTO ontology term, but no prior exact `eye_ciliary_body` YAML review
report, no causal-graph overlay, no append-only history item, no deep-research
report, and no existing HabitatMech use of `BTO:0000260`.

## Findings

### Major: `Eye: Ciliary body` is left `NARROW` despite an exact BTO term

- Evidence: `data/raw/ontology_terms.tsv` contains `BTO:0000260` with canonical
  label `ciliary body`, while `curation/decisions.tsv` currently records
  `habitatmech:GOLD.4d81fdaa51` as `GROUND_AS_PARENT` to the broader
  `UBERON:0000970` `eye`.
- Impact: the generated record remains a minted `habitatmech:GOLD.*` child of
  eye instead of adopting the exact ciliary-body anatomy identifier. That
  duplicates ontology coverage and prevents same-anatomy GOLD paths from
  merging under the exact term.
- Maintained owner: `curation/decisions.tsv`.

## Recommended Edits

1. Update `curation/decisions.tsv` for `habitatmech:GOLD.4d81fdaa51` from
   `GROUND_AS_PARENT` / `UBERON:0000970` / `NARROW` to an item-level `GROUND`
   decision for `BTO:0000260` / `ciliary body` / `EXACT`, noting that GOLD's
   `Eye: Ciliary body` path names the ciliary body anatomical site exactly.
2. Inspect and likely update the sibling `habitatmech:GOLD.aceda5f881` decision
   in `curation/decisions.tsv` the same way, because it represents the Mammals
   version of the same `Eye: Ciliary body` source leaf.
3. Regenerate with `just seed`, `just seed-canary BTO:0000260`, and then the
   normal `just seed-apply` flow so `data/habitats/host_associated/eye_ciliary_body.yaml`
   is retired or rewritten only through the seeder.

## Follow-up Checks

| Check | Purpose |
|---|---|
| `just seed` | Confirm the edited decision rows resolve and preview the exact merge outcome. |
| `just seed-canary BTO:0000260` | Regenerate the expected exact ciliary-body record through `write_validated_habitat`. |
| `just validate-strict data/habitats/host_associated/<new-ciliary-body>.yaml` | Prove the regenerated exact record is closed-schema valid. |
| `just verify-corpus` | Prove `data/habitats/` exactly matches `data/raw/` plus the edited curation decision rows. |
| `just report --out /tmp/habitatmech-ciliary-body-fixed-report.tsv` | Confirm the former `habitatmech:GOLD.4d81fdaa51` source attestation now lands in an `EXACT` record for `BTO:0000260`. |
| `just qc` | Run the full offline quality gate after seeding and any redirect or page regeneration required by the identity change. |

## Additional Notes

- iModulonDB structured adapters were not applicable because this GOLD habitat
  row names no gene, locus, regulator, pathway, stress response, trait, or
  transcriptomics dataset.
- The exact BTO term is sufficient to establish the identity defect; no paid
  deep-research run is needed for this anatomy grounding review.
