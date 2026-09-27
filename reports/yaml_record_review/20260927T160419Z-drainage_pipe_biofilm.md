# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/aquatic/drainage_pipe_biofilm.yaml
- Started UTC: 2026-09-27T16:04:19Z
- Finished UTC: 2026-09-27T16:04:19Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Record path | `data/habitats/aquatic/drainage_pipe_biofilm.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.4558077daa` |
| Label | `Drainage pipe biofilm` |
| Habitat category | `AQUATIC` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Maintained owner | Generated from `data/raw/gold_ecosystem_paths.tsv`, `data/habitats/PATHS.tsv`, and `curation/decisions.tsv`; do not hand-edit this YAML. |

The target is the generated HabitatMech record for the GOLD source path
`Environmental > Aquatic > Freshwater > Storm water > Drainage pipe biofilm`.
`data/habitats/PATHS.tsv` maps `habitatmech:GOLD.4558077daa` to the
`drainage_pipe_biofilm` slug.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/drainage_pipe_biofilm.yaml` | Pass. `linkml-validate` found no issues for this record. |
| `just validate-strict data/habitats/aquatic/drainage_pipe_biofilm.yaml` | Pass. Strict closed-schema validation scanned 1 file with 0 files in error and 0 error rows. |
| `just validate-causal curation/causal_graphs/<overlay>.yaml` | Not applicable. Ignored-inclusive searches for `habitatmech:GOLD.4558077daa`, `gold.ecosystem:4190`, the exact GOLD path, the slug, and the label found no causal-graph overlay for this record. |
| `just validate-causal-all` | Pass. All 32 causal-graph curation files and 32 graphs validated. |
| Reference validator | Not applicable. The record has no `evidence`, `datasets`, or `causal_graphs` references to validate. |
| `just term-requests-check` | Pass. The generated term-request table is current at 109 terms. |
| `just validate-history` | Pass. 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus` | Pass. 3,206 expected records were present with 0 missing, 0 extra, and 0 differing generated YAML files. |
| `just worklist --status all --out /tmp/habitatmech-worklist.tsv` | Pass. The worklist completed, wrote 953 ungrounded rows, and included this record as a GOLD-only class-swept row. |
| `just report --out /tmp/habitatmech-report.tsv` | Pass. The corpus report completed and included this record as `UNGROUNDED`, `SEEDED`, and sourced only from GOLD. |
| `git diff --check` | Pass after report creation. |

## Identity and Grounding

| Claim | Evidence | Assessment |
|---|---|---|
| The generated record denotes the GOLD `Drainage pipe biofilm` path. | `data/raw/gold_ecosystem_paths.tsv` has one exact row for `Environmental > Aquatic > Freshwater > Storm water > Drainage pipe biofilm`, leaf label `Drainage pipe biofilm`, depth 5, one GOLD node ID, and `gold.ecosystem:4190`. The generated `source_attestations` entry repeats that source ID, label, and path. | Supported exactly. |
| `grounding_status: UNGROUNDED` reflects the class-level decision, but is not an item-level judgment. | `curation/decisions.tsv` has a `CONFIRM_UNGROUNDED` row for `habitatmech:GOLD.4558077daa`; its `review_depth` is `CLASS`, and the note explicitly says whether the concept is a habitat at all was not assessed. | Structurally supported, but incomplete for a path with biosample triads. |
| `mapping_status: SEEDED` follows from the maintained curation depth. | HabitatMech class-level decisions do not promote records to `REVIEWED`; no item-level row exists for this exact GOLD source concept. | Supported. |
| The generated `ENVO:01001267` parent comes from the GOLD source path, not the leaf label. | The exact GOLD path is a child of `Environmental > Aquatic > Freshwater > Storm water`, and the generated record lists `ENVO:01001267` `stormwater` as its sole `parent_habitats` value. | Supported as source-path context, but not as a strict parent. A drainage-pipe biofilm is not a subclass of stormwater. |
| GOLD MIxS triads provide local and medium context for the exact path. | `data/raw/gold_path_triads.tsv` records four samples in one study with broad `ENVO:00002030` `aquatic biome`, local `ENVO:00000121` `artificial channel`, and medium `ENVO:01000156` `biofilm material`, all with `share=1.00`. | Supported as submitter-supplied context evidence; none of these three terms is an exact identity for a drainage-pipe biofilm. |

## Evidence

The record has no authored definition, evidence entries, environmental
parameters, characteristic taxa, datasets, or causal graphs.

| Assertion | Evidence | Assessment |
|---|---|---|
| GOLD has a direct drainage-pipe-biofilm ecosystem path. | The exact `data/raw/gold_ecosystem_paths.tsv` row stores `gold_node_count=1` and `gold.ecosystem:4190` for the exact path. | Supported exactly. |
| The exact GOLD path is represented in one GOLD study with four biosamples. | `data/raw/gold_studies.tsv` lists `Gs0046156` for this path, and `data/raw/gold_path_biosamples.tsv` lists 4 biosamples for path ID `4190`. | Supported exactly. |
| GOLD does not expose organism assertions directly on the grouping row. | The exact raw ecosystem-path row has `organism_count=0`, `study_count=0`, `biosample_count=0`, and `total_assertions=0`; the generated `source_attestations` row therefore has no assertion count. | Supported exactly. |
| The maintained class-level decision is reproduced in curation history. | The first generated curation event mirrors the `curation/decisions.tsv` row for `habitatmech:GOLD.4558077daa`, including `CONFIRM_UNGROUNDED`, the `2026-08-12` curator/date, and the class-sweep note. | Supported exactly. |

No snippet or citation mismatch was present because this generated placeholder
record carries only source-inventory and curation-history facts.

## Completeness

This record is reproducible but not complete enough for reviewed habitat
curation. The exact GOLD path has a concrete drainage-pipe-biofilm label, four
path-level biosamples, one GOLD study, and MIxS triads that coherently place
the path in an artificial-channel local context with biofilm material as the
sampled medium. Its only maintained decision is still the class-level lexical
sweep, so no item-level curation has evaluated whether the source concept is a
real biofilm habitat, which vendored or external terms are close misses, or
whether a novel term should be requested.

The existing `stormwater` parent is the main generated hierarchy gap. GOLD's
source path makes storm water a path context, but `data/raw/ontology_terms.tsv`
defines `ENVO:01001267` as water accumulating on a solid surface during
precipitation or melt events. A drainage-pipe biofilm can be wetted by
stormwater; it is not a kind of stormwater.

Ignored- and hidden-file-inclusive searches covered `data/raw`, `curation`,
`research`, `reports/yaml_record_review`, `conf`, and `data/habitats` for the
minted identifier, GOLD node ID, exact GOLD path, slug, and label. Before this
report was written, separate `find` checks of `reports/yaml_record_review`,
`curation/causal_graphs`, and `research/habitats` found no prior exact
drainage-pipe-biofilm review report, causal overlay, or research report.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | `Drainage pipe biofilm` still needs item-level habitat review and a novel drainage-pipe biofilm term decision. | The generated YAML is sourced from a real GOLD path with 4 biosamples, one exact-path GOLD study, and MIxS triads that place all four samples in artificial-channel local context with biofilm material as the medium. The only maintained decision for `habitatmech:GOLD.4558077daa`, however, is a class-level `CONFIRM_UNGROUNDED` row whose note explicitly did not assess whether this source concept is a habitat or a term-request candidate. | `curation/decisions.tsv`; if item review confirms no exact term, `curation/term_requests.tsv`. |
| Major | The generated record falsely asserts that a drainage-pipe biofilm is a kind of `stormwater`. | `data/habitats/aquatic/drainage_pipe_biofilm.yaml` lists `ENVO:01001267` as its sole parent because the exact GOLD path sits below `Storm water`. The source label and exact-path MIxS medium indicate a biofilm, while `data/raw/ontology_terms.tsv` defines `stormwater` as water that accumulates during precipitation or melt events. | `curation/term_requests.tsv` with `parent_mode=REPLACE`, or future maintained parent-edge suppression if the item review keeps a generated identity without a term request. |

No blockers or minor findings were found.

## Recommended Edits

1. Revisit `habitatmech:GOLD.4558077daa` in `curation/decisions.tsv` at
   `ITEM` depth. Verify the exact GOLD path, the four path-level biosamples,
   the one-study MIxS triads, and nearby ontology candidates including
   `stormwater`, `artificial channel`, `biofilm material`, and
   `aquatic biome`.
2. If no exact vendored or external OBO term denotes this path, keep the minted
   identifier with `CONFIRM_UNGROUNDED` or a strictly broader grounding as
   appropriate, and add a `curation/term_requests.tsv` definition for a
   drainage-pipe biofilm habitat.
3. Do not retain `ENVO:01001267` as a strict parent just because `Storm water`
   appears in the GOLD path. Model stormwater as source context, and use
   `parent_mode=REPLACE` or an equivalent maintained parent suppression so the
   regenerated record drops the false stormwater `is-a` edge.
4. Regenerate the target record from the maintained inputs instead of editing
   `data/habitats/aquatic/drainage_pipe_biofilm.yaml` directly.

## Follow-up Checks

| Check | Purpose |
|---|---|
| Manual GOLD/ontology candidate review | Confirm the ITEM decision does not conflate drainage-pipe biofilm with the stormwater that wets it, the artificial-channel local context, the aquatic biome broad context, or the biofilm-material medium. |
| `just seed` | Preview the regenerated corpus from the edited maintained inputs. |
| `just seed-canary habitatmech:GOLD.4558077daa` | Confirm the one generated target carries the new item-depth decision, definition, parent choice, and history expected from the maintained rows. |
| `just seed-apply --force` | Rebuild generated YAML after inspecting the canary output. |
| `just validate data/habitats/aquatic/drainage_pipe_biofilm.yaml` | Check the regenerated target against the LinkML `HabitatRecord` schema. |
| `just validate-strict data/habitats/aquatic/drainage_pipe_biofilm.yaml` | Check the regenerated target under the closed-schema validator. |
| `just term-requests-check` | Confirm generated ENVO term-request products are current if a novel term was added. |
| `just validate-history` | Confirm the append-only history record for the curation session is valid. |
| `just verify-corpus` | Prove generated `data/habitats/` still reproduces from `data/raw/` and curation inputs. |
| `just report` | Confirm the record moves out of the class-level sweep bucket after item review. |
| `git diff --check` | Catch whitespace errors in the maintained and generated diffs. |

## Additional Notes

- The absence checks in this review used `rg --no-ignore --hidden` and `find`,
  so ignored and hidden files were included.
- `ENVO:01000156` `biofilm material` is material derived from a biofilm. It is
  strong medium-slot context in the GOLD MIxS triads, but it should not be used
  as an exact identity for the whole drainage-pipe biofilm habitat.
- `ENVO:00000121` `artificial channel` is the local-scale MIxS term for all
  four exact-path biosamples. It points toward drainage-pipe context but does
  not by itself name a biofilm.
