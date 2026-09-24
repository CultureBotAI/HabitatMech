# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/aquatic/cave_pool_sediment.yaml`
- Started UTC: 2026-09-24T00:35:00Z
- Finished UTC: 2026-09-24T00:54:41Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.62bafb5e20` |
| Label | `Cave pool sediment` |
| File | `data/habitats/aquatic/cave_pool_sediment.yaml` |
| Category | `AQUATIC` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Source | `GOLD` |
| Source ID | `gold.ecosystem:5968` |
| Source path | `Environmental > Aquatic > Deep subsurface > Groundwater > Cave pool sediment` |
| Maintained owner | Generated from `data/raw/gold_ecosystem_paths.tsv`, `data/habitats/PATHS.tsv`, and `curation/decisions.tsv`; do not edit `data/habitats/aquatic/cave_pool_sediment.yaml` directly. |

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/cave_pool_sediment.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/habitats/aquatic/cave_pool_sediment.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| Target causal overlay | Not applicable. Exact ignored-inclusive searches for `habitatmech:GOLD.62bafb5e20` and `Cave pool sediment`, plus `find` checks for `*cave*` and `*sediment*` causal-graph filenames, found no target overlay in `curation/causal_graphs/`. |
| Reference validator | Not applicable. This target has no record-level `evidence`, no `characteristic_taxa.reference`, and no `causal_graphs` edges requiring cited evidence. |
| `just term-requests-check` | Passed; the ENVO term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; 3,206 records expected, 3,206 found, 0 missing, 0 extra, 0 differing. |
| `just worklist --limit 2000` | Passed; 0 ungrounded records are still undecided and 1,810 decisions are on file. |
| `just report` | Passed; the corpus report completed and emitted current grounding, source, GOLD triad, and curation statistics. |
| `git diff --check` | Passed before writing this report. |

## Identity and Grounding

The generated identifier is stable and correct for this GOLD path:

| Claim | Check |
|---|---|
| Minted identifier | `mint("GOLD", "Environmental > Aquatic > Deep subsurface > Groundwater > Cave pool sediment")` returned `habitatmech:GOLD.62bafb5e20`, matching the generated record. |
| Slug lock | `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.62bafb5e20` to `cave_pool_sediment`. |
| GOLD source row | `data/raw/gold_ecosystem_paths.tsv` has exactly one node for the path, source id `gold.ecosystem:5968`, depth 5, label `Cave pool sediment`, 7 GOLD KGX organism assertions, 0 GOLD KGX sample assertions, and 0 GOLD KGX study assertions. |
| Curation row | `curation/decisions.tsv` has one class-level `CONFIRM_UNGROUNDED` row for `habitatmech:GOLD.62bafb5e20`; the row records that the lexical sweep did not assess whether the concept is a habitat or term-request candidate. |
| Class-sweep sample | `curation/samples/class_swept_unscreened-20260814.tsv` sampled this concept and marked it a habitat, but that sample did not add an item-level grounding decision. |

The current direct source-path parent,
`habitatmech:GOLD.22a80cbd14` `Groundwater`, is generated from the GOLD parent
path `Environmental > Aquatic > Deep subsurface > Groundwater`. That parent is
not a strict broader class for this leaf: cave pool sediment is deposited
particulate material in a cave pool, not a kind of groundwater.

The vendored ontology slice has no exact `cave pool sediment` class. It does
have `ENVO:00002007` `sediment`, defined as particulate environmental material
formed through transport and deposition of particles by flowing liquid. That
term is strictly broader than cave pool sediment and is the candidate parent the
class-level sweep missed because its search could not use the source-path pool
context to reinterpret the compound leaf as a cave-specific sediment material.

## Evidence

The generated record is traceable to maintained inputs:

| Claim | Maintained input or inventory |
|---|---|
| GOLD source id and exact source path | `data/raw/gold_ecosystem_paths.tsv` row for `gold.ecosystem:5968` |
| Stable HabitatMech identifier and slug | `data/habitats/PATHS.tsv` row for `habitatmech:GOLD.62bafb5e20` |
| Class-level `CONFIRM_UNGROUNDED` status | `curation/decisions.tsv` row for `habitatmech:GOLD.62bafb5e20` |
| Generated source-path parent | `data/raw/gold_ecosystem_paths.tsv` row for the parent path `Environmental > Aquatic > Deep subsurface > Groundwater` plus `data/habitats/PATHS.tsv` mapping `habitatmech:GOLD.22a80cbd14` to `groundwater` |

The record has no record-level literature entry, and the committed GOLD rows do
not attach any biosamples, studies, MIxS triads, or environmental parameters to
`gold.ecosystem:5968`. Exact ignored-inclusive searches for
`gold.ecosystem:5968` and the full source path found the target row in
`data/raw/gold_ecosystem_paths.tsv`, the class-sweep sample row, the generated
target record, and a sibling Cave pool review note that mentions this source as
context, but no `data/raw/gold_path_biosamples.tsv`,
`data/raw/gold_studies.tsv`, or `data/raw/gold_path_triads.tsv` rows for this
source path.

No causal graph is attached to this record, so there are no mechanism edges
needing claim-level `EvidenceItem` support.

## Completeness

The required generated identity, category, source attestation, source-derived
parent, class-level curation history, and seeded mapping status are present.

The empty optional slots are acceptable for the generated record as it stands:

| Slot | Review |
|---|---|
| `environmental_parameters` | Empty. No committed GOLD or curator-authored environmental-parameter row was found for `gold.ecosystem:5968`. |
| `characteristic_taxa` | Empty. GOLD contributes only an aggregate source attestation for this path; the record has no BacDive or PREGO taxon rows and HabitatMech does not infer characteristic taxa from a source-tree label. |
| `evidence` | Empty. The class-level sweep did not inspect cave-pool-sediment literature, and no maintained literature artifact was found for this record. |
| `causal_graphs` | Empty. Exact ignored-inclusive searches found no target overlay in `curation/causal_graphs/`. |
| `discussions` and `datasets` | Empty. No maintained discussion or dataset input exists for this record. |

Exact ignored-inclusive searches for `habitatmech:GOLD.62bafb5e20`,
`gold.ecosystem:5968`, `cave_pool_sediment`, `Cave pool sediment`, and the GOLD
source path found the generated record, its `PATHS.tsv` row, the raw GOLD path
row, and the class-level decision and sample rows. They did not find a
target-specific term request, causal overlay, history record, research report,
or prior exact YAML review report. The exact report check used `find` under
`reports/yaml_record_review`, which includes ignored files.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | None found | The YAML validates, the generated identifier matches the GOLD source path, and the record correctly remains `SEEDED` because its only curation decision is class-level. | Not applicable |
| Major | The class-level `CONFIRM_UNGROUNDED` row missed `ENVO:00002007` `sediment` as a strictly broader term for Cave pool sediment and left the generated record under the non-strict `Groundwater` source-path parent. | `data/raw/ontology_terms.tsv` includes `ENVO:00002007` `sediment`, a particulate environmental-material term. `ENVO:01001004` `groundwater` names underground water in pore spaces of rock or unconsolidated deposits, while this GOLD path names sediment deposited in a cave-pool context. The source path places the concept under GOLD's groundwater branch, but the leaf is a sediment material rather than a kind of pore-space water. | `curation/decisions.tsv`; probably `curation/term_requests.tsv` if Cave pool sediment remains a novel minted child of `ENVO:00002007` |
| Minor | None found | The remaining empty optional slots are consistent with the absence of maintained item-level curation, sample or study rows, MIxS triads, BacDive or PREGO taxa, and a causal overlay. | Not applicable |

## Recommended Edits

| Priority | Edit | Maintained path |
|---|---|---|
| Major | Replace the class-level row for `habitatmech:GOLD.62bafb5e20` with an item-level `GROUND_AS_PARENT` decision to `ENVO:00002007` `sediment`, yielding `grounding_status` `NARROW`. | `curation/decisions.tsv` |
| Major | If Cave pool sediment stays distinct from generic `ENVO:00002007`, add an authored `cave pool sediment` term request with parent `ENVO:00002007` and `parent_mode=REPLACE` so the regenerated record drops the inherited `habitatmech:GOLD.22a80cbd14` `Groundwater` parent. | `curation/term_requests.tsv` |

Do not hand-edit `data/habitats/aquatic/cave_pool_sediment.yaml`; regenerate it
from the maintained inputs after item-level curation changes.

## Follow-up Checks

| Edit | Narrowest proving checks |
|---|---|
| Item-level Cave pool sediment grounding | Exact ignored-inclusive `rg` for `habitatmech:GOLD.62bafb5e20`, `gold.ecosystem:5968`, and `ENVO:00002007` should find the new maintained decision and any term request; `just seed-canary habitatmech:GOLD.62bafb5e20`, `just term-requests-check`, `just validate data/habitats/aquatic/cave_pool_sediment.yaml`, `just validate-strict data/habitats/aquatic/cave_pool_sediment.yaml`, `just validate-history`, and `just verify-corpus --max-diffs 1` should still pass. |
| Parent replacement | The regenerated `data/habitats/aquatic/cave_pool_sediment.yaml` should list `ENVO:00002007`, not `habitatmech:GOLD.22a80cbd14`, under `parent_habitats`; run `just validate data/habitats/aquatic/cave_pool_sediment.yaml`, `just validate-strict data/habitats/aquatic/cave_pool_sediment.yaml`, and `just verify-corpus --max-diffs 1`. |

## Additional Notes

- Searches used to establish absence included ignored and hidden files. Broad
  exact content searches excluded `data/text_map/**`, `pages/**`, `build/**`,
  and `.git/**` so generated text-map, rendered-page, build-product, and git
  object matches did not dominate the results.
- The exact `gold.ecosystem:5968` and full source-path searches also hit
  `reports/yaml_record_review/20260924T003355Z-cave_pool.md` because that Cave
  pool report mentions Cave pool sediment as a sibling record; it is not a prior
  review of `data/habitats/aquatic/cave_pool_sediment.yaml`.
