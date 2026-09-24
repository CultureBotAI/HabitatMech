# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/aquatic/coalbed_methane_well_water.yaml
- Started UTC: 2026-09-24T08:26:09Z
- Finished UTC: 2026-09-24T08:26:09Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Record path | `data/habitats/aquatic/coalbed_methane_well_water.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.1b19e33e8c` |
| Label | `Coalbed methane well water` |
| Habitat category | `AQUATIC` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Maintained owner | Generated from `data/raw/gold_ecosystem_paths.tsv`, `data/habitats/PATHS.tsv`, and `curation/decisions.tsv`; do not hand-edit this YAML. |

The target is a generated GOLD leaf for the source path
`Environmental > Aquatic > Deep subsurface > Groundwater > Coalbed methane well
water`. `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.1b19e33e8c` to the
`coalbed_methane_well_water` slug.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/coalbed_methane_well_water.yaml` | Pass. `linkml-validate` found no issues for this record. |
| `just validate-strict data/habitats/aquatic/coalbed_methane_well_water.yaml` | Pass. Strict closed-schema validation scanned 1 file with 0 files in error and 0 error rows. |
| `just validate-causal curation/causal_graphs/<overlay>.yaml` | Not applicable. An ignored-inclusive search for `habitatmech:GOLD.1b19e33e8c`, `gold.ecosystem:5963`, the exact GOLD path, label, and slug found no causal-graph overlay for this record. |
| `just validate-causal-all` | Pass. All 32 causal-graph curation files and 32 graphs validated. |
| Reference validator | Not applicable. The record has no `evidence`, `datasets`, or `causal_graphs` references to validate. |
| `just term-requests-check` | Pass. The generated term-request table is current at 109 terms. |
| `just validate-history` | Pass. 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Pass. 3,206 expected records were present with 0 missing, 0 extra, and 0 differing generated YAML files. |
| `just worklist --limit 2000` | Pass. The curation worklist command completed and reported 1,810 decisions on file. |
| `just report` | Pass. The corpus report command completed. |
| `git diff --check` | Pass after report creation. |

## Identity and Grounding

| Claim | Evidence | Assessment |
|---|---|---|
| The generated record denotes the GOLD `Coalbed methane well water` aquatic deep-subsurface groundwater leaf. | `data/raw/gold_ecosystem_paths.tsv` has one exact row for `Environmental > Aquatic > Deep subsurface > Groundwater > Coalbed methane well water` with node `gold.ecosystem:5963`, leaf label `Coalbed methane well water`, depth 5, and 1 organism assertion. The generated `source_attestations` entry repeats that source ID, label, path, count, and `ORGANISM` assertion unit. | Supported. |
| The record is scoped to water and is distinct from the terrestrial coalbed-methane `Coal core` and `Coal slurry` leaves. | The exact GOLD path is under `Aquatic > Deep subsurface > Groundwater`. The one exact study, `Gs0141001`, also lists `Environmental > Terrestrial > Deep subsurface > Coalbed methane well > Coal core` and `... > Coal slurry`, and the raw path and triad inventories keep those as separate terrestrial source concepts. | Supported. |
| `habitatmech:GOLD.22a80cbd14` `Groundwater` is a broader source-path parent for this source concept. | `data/habitats/aquatic/groundwater.yaml` is the generated record for `Environmental > Aquatic > Deep subsurface > Groundwater`, and the coalbed-methane well-water source path is a child of that path in `data/raw/gold_ecosystem_paths.tsv`. | Supported. |
| `mapping_status: SEEDED` follows from the maintained curation depth. | `curation/decisions.tsv` has a `CONFIRM_UNGROUNDED` row for `habitatmech:GOLD.1b19e33e8c`, but its `review_depth` is `CLASS`; HabitatMech class-level decisions do not promote records to `REVIEWED`. | Supported. |
| `grounding_status: UNGROUNDED` reflects the class-level decision, but is not an item-level judgment. | The decision note says the class-level sweep found no matching term in the vendored slice and explicitly says whether the concept is a habitat at all was not assessed. | Structurally supported, but incomplete for curation. |
| GOLD MIxS triads provide contextual evidence for this source path. | `data/raw/gold_path_triads.tsv` lists `ENVO:00002030` as broad scale, `ENVO:00002169` as local scale, and `ENVO:00005792` as medium for the exact path. All three terms exist in `data/raw/ontology_terms.tsv` with canonical labels `aquatic biome`, `coal mine`, and `underground water`. | Contextual only. `aquatic biome` and `underground water` are broader than this leaf, and `coal mine` is the local feature rather than the water habitat identity. |

## Evidence

The record has no authored definition, evidence entries, environmental
parameters, characteristic taxa, datasets, or causal graphs.

| Assertion | Evidence | Assessment |
|---|---|---|
| GOLD attests this exact source path with 1 organism assertion. | `data/raw/gold_ecosystem_paths.tsv` has assertion count `1` for node `gold.ecosystem:5963`, and the generated attestation preserves the same count and `ORGANISM` unit. | Supported. |
| GOLD has biosample and study context for the exact coalbed-methane well-water path. | `data/raw/gold_path_biosamples.tsv` has 17 biosamples for node `5963`; `data/raw/gold_studies.tsv` lists `Gs0141001` on the exact path. | Supported as source context not yet surfaced in the YAML. |
| The class-level ungrounded curation event records an exact maintained decision. | The first curation event mirrors the `curation/decisions.tsv` row for `habitatmech:GOLD.1b19e33e8c`, including `CONFIRM_UNGROUNDED`, the `2026-08-12` curator/date, and the class-sweep note. | Supported. |

No snippet or citation mismatch was present because this generated placeholder
record carries only source inventory and curation-history facts.

## Completeness

This record is reproducible but not complete enough for reviewed habitat
curation. The exact GOLD path has class-level screening, raw MIxS triads, 17
biosamples, and 1 GOLD study, but no item-level decision has verified whether
the coalbed-methane well-water leaf is a real habitat, whether any exact
ontology term exists, or whether the minted record should receive a novel-term
definition.

An ignored-inclusive search over `curation/term_requests.tsv`,
`curation/external_xrefs.tsv`, `curation/causal_graphs`, `history`, `research`,
and `reports/yaml_record_review` for the minted ID, GOLD node, exact GOLD path,
label, and slug found no exact term request, external xref, causal overlay,
item-level history record, research report, or prior exact review.

The empty optional slots are otherwise unsurprising for a small GOLD-only
record: GOLD does not supply curated causal edges, `is_characteristic` taxa, or
claim-level evidence snippets for this leaf.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | `Coalbed methane well water` still needs item-level habitat review and a novel-term decision. | The generated YAML is sourced from a real GOLD water leaf, and source inventories provide exact node, biosample, study, and MIxS triad rows. The only maintained decision for `habitatmech:GOLD.1b19e33e8c` is a class-level `CONFIRM_UNGROUNDED` row whose note explicitly did not assess whether this source concept is a habitat or a term-request candidate. Consequently the generated record has `mapping_status: SEEDED`, no authored definition, and no `curation/term_requests.tsv` row. | `curation/decisions.tsv`; if item review confirms no exact term, `curation/term_requests.tsv`. |

No blockers or minor findings were found.

## Recommended Edits

1. Revisit `habitatmech:GOLD.1b19e33e8c` in `curation/decisions.tsv` at
   `ITEM` depth. Verify the exact aquatic GOLD path, the terrestrial
   coalbed-methane well paths that co-occur in `Gs0141001`, the MIxS
   broad/local/medium triads, and nearby ontology candidates before deciding
   whether the source is a coalbed-methane well-water habitat.
2. If no exact vendored or external OBO term denotes this leaf, keep the minted
   identifier with `CONFIRM_UNGROUNDED` or a strictly broader
   `GROUND_AS_PARENT` relation as appropriate. Do not ground directly to
   `ENVO:00005792` `underground water` or `ENVO:00002169` `coal mine`; those
   terms are medium and local-feature context rather than exact identities for
   the full GOLD leaf.
3. If item review confirms this is a real habitat with no exact ontology term,
   add a `curation/term_requests.tsv` definition for the minted
   coalbed-methane well-water habitat, retaining `habitatmech:GOLD.22a80cbd14`
   as the source-derived parent unless item evidence shows the groundwater
   parent is false.
4. Regenerate the target record from the maintained inputs instead of editing
   `data/habitats/aquatic/coalbed_methane_well_water.yaml` directly.

## Follow-up Checks

| Check | Purpose |
|---|---|
| Manual GOLD/ontology candidate review | Confirm the ITEM decision does not conflate the water leaf with the terrestrial coal core or coal slurry leaves. |
| `just seed` | Preview the regenerated corpus from the edited maintained inputs. |
| `just seed-canary habitatmech:GOLD.1b19e33e8c` | Confirm the one generated target carries the new item-depth decision, mapping status, definition, parents, and history expected from the maintained rows. |
| `just seed-apply --force` | Rebuild generated YAML after inspecting the canary output. |
| `just validate data/habitats/aquatic/coalbed_methane_well_water.yaml` | Check the regenerated target against the LinkML `HabitatRecord` schema. |
| `just validate-strict data/habitats/aquatic/coalbed_methane_well_water.yaml` | Check the regenerated target under the closed-schema validator. |
| `just term-requests-check` | Confirm generated ENVO term-request products are current if a novel term was added. |
| `just validate-history` | Confirm the append-only history record for the curation session is valid. |
| `just verify-corpus --max-diffs 1` | Prove generated `data/habitats/` still reproduces from `data/raw/` and curation inputs. |
| `just report` | Confirm the record moves out of the class-level sweep bucket after item review. |
| `git diff --check` | Catch whitespace errors in the maintained and generated diffs. |

## Additional Notes

- The absence checks in this review used `rg --no-ignore --hidden` and `find`,
  so ignored and hidden files were included.
- This record has no maintained causal overlay. `just validate-causal-all`
  covers all existing overlays, and no focused `just validate-causal` target
  applies.
