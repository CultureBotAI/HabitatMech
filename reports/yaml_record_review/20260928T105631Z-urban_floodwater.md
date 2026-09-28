# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/urban_floodwater.yaml`
- Started UTC: 2026-09-28T10:56:31Z
- Finished UTC: 2026-09-28T10:56:31Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Record path | `data/habitats/aquatic/urban_floodwater.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.4d5e767cac` |
| Label | `Urban floodwater` |
| Habitat category | `AQUATIC` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Parent habitats | `ENVO:01001267` |
| Maintained owner | Generated from `data/raw/gold_ecosystem_paths.tsv`, `data/habitats/PATHS.tsv`, and `curation/decisions.tsv`; do not hand-edit this YAML. |

The target is the generated HabitatMech record for the GOLD source path
`Environmental > Aquatic > Freshwater > Storm water > Urban floodwater`.
`data/habitats/PATHS.tsv` maps `habitatmech:GOLD.4d5e767cac` to the
`urban_floodwater` slug.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/urban_floodwater.yaml` | Pass. `linkml-validate` reported `No issues found`. |
| `just validate-strict data/habitats/aquatic/urban_floodwater.yaml` | Pass. Strict closed-schema validation scanned 1 file with 0 files in error and 0 total error rows. |
| `just validate-causal curation/causal_graphs/<overlay>.yaml` | Not applicable. Ignored- and hidden-file-inclusive searches for `habitatmech:GOLD.4d5e767cac` and `urban_floodwater` found no maintained causal-graph overlay for this record. |
| `just validate-causal-all` | Pass. All 32 causal-graph curation files and 32 graphs validated. |
| Reference validator | Not applicable. The generated record has no `evidence`, `datasets`, or `causal_graphs` references. |
| `just term-requests-check` | Pass. The generated term-request table is current at 109 terms. |
| `just validate-history` | Pass. 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus` | Pass. 3,206 expected records were present with 0 missing, 0 extra, and 0 differing generated YAML files. |
| `just worklist --status all --out /tmp/habitatmech-urban-floodwater-worklist.tsv` | Pass. Wrote 953 ungrounded rows and listed `habitatmech:GOLD.4d5e767cac` as a decided GOLD-only row with nearby candidates `ENVO:01001268` `urban stormwater` and `ENVO:01000718` `urban flooding`. |
| `just report --out /tmp/habitatmech-urban-floodwater-report.tsv` | Pass. Wrote the 3,206-record corpus TSV and listed this record at row 1857 as `UNGROUNDED`, `SEEDED`, GOLD-only, zero source assertions, one parent, no parameters, no taxa, and no causal graphs. |
| `git diff --check` | Pass after report creation. |

## Identity and Grounding

| Claim | Evidence | Assessment |
|---|---|---|
| The generated record denotes GOLD's `Urban floodwater` ecosystem path. | `data/raw/gold_ecosystem_paths.tsv` has one exact row for `Environmental > Aquatic > Freshwater > Storm water > Urban floodwater` with leaf label `Urban floodwater`, depth 5, `gold_node_count=1`, and `gold.ecosystem:7513`. The generated `source_attestations` entry repeats that source ID, label, and path. | Supported exactly. |
| `grounding_status: UNGROUNDED` is generated from a class-level `CONFIRM_UNGROUNDED` decision, not an item-level habitat judgement. | `curation/decisions.tsv` records `CONFIRM_UNGROUNDED` for `habitatmech:GOLD.4d5e767cac`, but its `review_depth` is `CLASS` and the note says whether the concept is a habitat at all was not assessed. | Structurally supported, but incomplete for final curation. |
| `mapping_status: SEEDED` follows from the maintained curation depth. | HabitatMech treats class-level decisions as screening decisions, and `docs/HARMONIZATION.md` says `CLASS` means a mechanically defined group was decided rather than the concept being individually examined against its source path and candidates. | Supported. |
| The generated `ENVO:01001267` `stormwater` parent is inherited from the GOLD parent path. | The exact path is a child of `Environmental > Aquatic > Freshwater > Storm water`; `data/habitats/aquatic/stormwater.yaml` is the generated record for that parent path, and `data/raw/ontology_terms.tsv` defines `ENVO:01001267` as water that accumulates on a solid surface during precipitation and snow or ice melt. | Supported as a broader generated parent. It is less specific than the vendored `ENVO:01001268` `urban stormwater` candidate that now appears in the worklist. |
| `ENVO:01001268` is a vendored stormwater candidate for item review. | `data/raw/ontology_terms.tsv` contains `ENVO:01001268` with label `urban stormwater`, definition `Stormwater which accumulates in an urban ecosystem.`, and synonym `urban storm water`; `data/raw/ontology_subclass_edges.tsv` makes it a subclass of `ENVO:01001267` `stormwater`; the target's `just worklist --status all` row ranks both the label and synonym beside the process term `ENVO:01000718` `urban flooding`. | Supported as a close candidate that the class-level sweep did not resolve. Manual review still has to decide exact, broader, close, or no-match status for GOLD `Urban floodwater`. |

## Evidence

The record has no authored definition, evidence entries, environmental
parameters, characteristic taxa, datasets, or causal graphs.

| Assertion | Evidence | Assessment |
|---|---|---|
| The GOLD inventory has a direct urban-floodwater ecosystem path. | The exact `data/raw/gold_ecosystem_paths.tsv` row stores `gold_node_count=1` and `gold.ecosystem:7513` for this path. | Supported exactly. |
| The exact GOLD path appears in one GOLD study and ten path-level biosamples. | `data/raw/gold_studies.tsv` lists `Gs0156854` for the exact path, and `data/raw/gold_path_biosamples.tsv` lists 10 biosamples for path ID 7513. | Supported exactly. |
| GOLD does not expose organism assertions directly on the grouping row. | The exact raw ecosystem-path row has `organism_count=0`, `study_count=0`, `biosample_count=0`, and `total_assertions=0`; the generated source attestation therefore has no `assertion_count` or `assertion_unit`. | Supported exactly. |
| The first generated curation-history event reflects the maintained class-level sweep row. | `data/habitats/aquatic/urban_floodwater.yaml` repeats the `2026-08-12` `CONFIRM_UNGROUNDED` action, curator, class depth, and source concept from `curation/decisions.tsv`. | Supported exactly. |

No snippet or citation mismatch was present because this generated placeholder
record carries only source-inventory and curation-history facts.

## Completeness

This record is reproducible, source-backed, and internally consistent at the
schema level, but it is not complete enough for reviewed habitat curation. The
GOLD path has a concrete aquatic leaf label with ten path-level biosamples and
one GOLD study. Its only maintained decision is still the class-level lexical
sweep, so no item-level row has assessed whether `Urban floodwater` is exactly
`ENVO:01001268` `urban stormwater`, narrower than that term, related to the
nearby `ENVO:01000718` `urban flooding` process, or genuinely absent from the
vendored slice.

The existing `ENVO:01001267` `stormwater` parent is a supported broader parent
from the GOLD source path. It should still be rechecked in item review because
`ENVO:01001268` is a strictly more specific stormwater candidate already present
in the vendored slice.

Ignored- and hidden-file-inclusive searches covered `data/raw`, `curation`,
`history`, `research`, `reports`, `data/habitats`, `pages/habitats`, and `docs`
for `habitatmech:GOLD.4d5e767cac`, `gold.ecosystem:7513`, the exact GOLD path,
`urban_floodwater`, `Urban floodwater`, `urban stormwater`, and
`ENVO:01001268`. They found the maintained class-level decision, the generated
target and page, the source-inventory rows, the vendored ontology candidate,
and the `PATHS.tsv` slug lock, but no prior YAML review report, research report,
term request, item-level history record, or causal-graph overlay for this exact
record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | `Urban floodwater` needs item-level curation before the current `UNGROUNDED` decision is trusted as final. | The generated record is backed by a real GOLD path with 10 path-level biosamples and one GOLD study, but `curation/decisions.tsv` has only a class-level `CONFIRM_UNGROUNDED` row for `habitatmech:GOLD.4d5e767cac`. `just worklist --status all` now lists vendored near candidates `ENVO:01001268` `urban stormwater`, its `urban storm water` synonym, and the process term `ENVO:01000718` `urban flooding`; `ENVO:01001268` is a subclass of the generated `stormwater` parent. | `curation/decisions.tsv`; if item review confirms no exact term, `curation/term_requests.tsv`. |

No blockers or minor findings were found.

## Recommended Edits

1. Revisit `habitatmech:GOLD.4d5e767cac` in `curation/decisions.tsv` at
   `ITEM` depth. Verify the exact GOLD path, the 10 path-level biosamples, the
   one GOLD study, and nearby ontology candidates including `ENVO:01001268`
   `urban stormwater`, `ENVO:01000718` `urban flooding`, and `ENVO:01001267`
   `stormwater`.
2. Decide the maintained relationship to `ENVO:01001268`. Use `GROUND` only if
   `urban stormwater` exactly denotes GOLD `Urban floodwater`; use
   `GROUND_AS_PARENT` if it is strictly broader; use an xref if it is related
   but not broader; or keep `CONFIRM_UNGROUNDED` at `ITEM` depth if no exact or
   broader term fits.
3. If item review keeps the minted `habitatmech:GOLD.4d5e767cac` identifier
   because no exact term exists, add a definition in
   `curation/term_requests.tsv` and select `ADD` or `REPLACE` parent mode based
   on whether the inherited stormwater parent is strictly true.
4. Regenerate the target record from maintained inputs instead of editing
   `data/habitats/aquatic/urban_floodwater.yaml` directly.

## Follow-up Checks

| Check | Purpose |
|---|---|
| Manual GOLD/ontology candidate review | Confirm the item-level relationship to `urban stormwater`, `urban flooding`, and `stormwater` without conflating a water material with a flooding process. |
| `just seed` | Preview the regenerated corpus from the edited maintained inputs. |
| `just seed-canary habitatmech:GOLD.4d5e767cac` | Confirm the one generated target carries the new item-depth decision, optional definition, parent choice, and expected generated history. |
| `just seed-apply --force` | Rebuild generated YAML after inspecting the canary output. |
| `just validate data/habitats/aquatic/urban_floodwater.yaml` | Check the regenerated target against the LinkML `HabitatRecord` schema. |
| `just validate-strict data/habitats/aquatic/urban_floodwater.yaml` | Check the regenerated target under the closed-schema validator. |
| `just term-requests-check` | Confirm generated ENVO term-request products are current if a novel term was added. |
| `just validate-history` | Confirm the append-only history record for the curation session is valid. |
| `just verify-corpus` | Prove generated `data/habitats/` still reproduces from `data/raw/` and curation inputs. |
| `just worklist --status all --out /tmp/habitatmech-urban-floodwater-worklist-after.tsv` | Confirm this record moves out of the class-level sweep worklist after item review. |
| `just report --out /tmp/habitatmech-urban-floodwater-report-after.tsv` | Confirm the regenerated row has the expected grounding and mapping statuses. |
| `git diff --check` | Catch whitespace errors in the maintained and generated diffs. |

## Additional Notes

- iModulonDB structured adapters were not applicable because this GOLD habitat
  row names no gene, locus, regulator, pathway, stress response, trait, or
  transcriptomics dataset.
- The exact hidden/ignored-inclusive searches found no `gold_path_triads.tsv`
  row for `Environmental > Aquatic > Freshwater > Storm water > Urban
  floodwater`, so this review did not use MIxS broad, local, or medium slots
  as identity evidence.
