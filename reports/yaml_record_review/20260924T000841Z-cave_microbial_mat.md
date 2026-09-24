# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/aquatic/cave_microbial_mat.yaml`
- Started UTC: `2026-09-24T00:06:35Z`
- Finished UTC: `2026-09-24T00:08:41Z`
- Verdict: `needs curation`

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/aquatic/cave_microbial_mat.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.aed29e2fc1` |
| Label | `Cave microbial mat` |
| Generated or maintained | Generated from `data/raw/gold_ecosystem_paths.tsv`, `data/habitats/PATHS.tsv`, and `curation/decisions.tsv` |
| Habitat category | `AQUATIC` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Source concept | `Environmental > Aquatic > Deep subsurface > Groundwater > Cave microbial mat` |

This is the generated GOLD Cave microbial mat leaf beneath Groundwater. Its
identifier reproduces from
`mint("GOLD", "Environmental > Aquatic > Deep subsurface > Groundwater > Cave microbial mat")`
as `habitatmech:GOLD.aed29e2fc1`, and `data/habitats/PATHS.tsv` pins the
identifier to the corpus-wide `cave_microbial_mat` slug.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/cave_microbial_mat.yaml` | Passed; LinkML accepted the record as `HabitatRecord`. |
| `just validate-strict data/habitats/aquatic/cave_microbial_mat.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Focused causal validator | Not applicable: ignored-inclusive `find`/`rg` checks found no `curation/causal_graphs/*cave*` or `curation/causal_graphs/*microbial*` overlay and no causal overlay mentioning `habitatmech:GOLD.aed29e2fc1`. |
| `just validate-causal-all` | Passed; 32 curated causal-graph files with 32 graphs validated. |
| Reference validator | Not applicable: `CLAUDE.md` and `justfile` do not document a standalone reference validator for records without causal overlays. |
| `just term-requests-check` | Passed; `curation/term_requests/envo_robot_template.tsv` is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; 3,206 records expected, 3,206 found, 0 missing, 0 extra, 0 differing. |
| `just worklist --limit 2000` | Passed; 0 ungrounded records still undecided, 1,810 decisions on file. |
| `just report` | Passed; corpus report completed after counting 3,206 records and 686 `REVIEWED` records. |
| `git diff --check` | Passed. |

## Identity and Grounding

The minted source identity is internally consistent. `data/raw/gold_ecosystem_paths.tsv`
has one collapsed GOLD ecosystem concept for the exact canonical path, with
leaf label `Cave microbial mat`, depth 5, `gold_node_count` 1,
`total_assertions` 0, and `gold_node_ids` `gold.ecosystem:5967`. The generated
`source_attestations` entry carries the same source id, source label, and
source path, with no generated assertion count or count unit because the KGX
assertion inventory has no organism assertions for this GOLD path.

The repository has additional source inventory proving GOLD did attach samples
to this concept. `data/raw/gold_path_biosamples.tsv` has three bulk-export
biosamples for the same `gold.ecosystem:5967` path, and
`data/raw/gold_studies.tsv` places those biosamples in three studies. Two of
the three biosamples have complete MIxS triads in `data/raw/gold_path_triads.tsv`;
both set the local scale to `ENVO:00000067` `cave`, and one sets the medium to
`ENVO:01000157` `microbial mat material`. That separate biosample inventory
does not feed the generated `source_attestations` assertion count, so the
record's zero-count source attestation is faithful to the committed
`gold_ecosystem_paths.tsv` row.

The current grounding is only class-level. `curation/decisions.tsv` carries a
`CONFIRM_UNGROUNDED` row from the August 2026 class-level sweep for
`habitatmech:GOLD.aed29e2fc1`; the generated `curation_history` explicitly
notes that the sweep matched no vendored term by lexical route and did not
assess whether this exact concept is a habitat or term-request candidate. The
resulting `SEEDED` mapping status is therefore correct for an unreviewed GOLD
source concept, but the decision row is not an item-level review.

The inherited parent is not a strict is-a parent. The generated parent,
`habitatmech:GOLD.22a80cbd14` `Groundwater`, is the GOLD parent path
`Environmental > Aquatic > Deep subsurface > Groundwater`; it is itself a
generated `NARROW` record beneath `ENVO:01001004` `groundwater`. ENVO defines
groundwater as underground water in pore spaces of rock or unconsolidated
deposits. A cave microbial mat may be associated with groundwater-fed caves,
but the mat is not itself underground pore-space water.

## Evidence

The generated record is traceable to maintained inputs:

| Claim | Maintained input or inventory |
|---|---|
| GOLD source id and exact source path | `data/raw/gold_ecosystem_paths.tsv` row for `gold.ecosystem:5967` |
| Stable HabitatMech identifier and slug | `data/habitats/PATHS.tsv` row for the Cave microbial mat GOLD path |
| Class-level `CONFIRM_UNGROUNDED` status | `curation/decisions.tsv` row for `habitatmech:GOLD.aed29e2fc1` |
| Three GOLD biosamples for the path | `data/raw/gold_path_biosamples.tsv` row for `gold.ecosystem:5967` |
| Three GOLD studies containing those biosamples | `data/raw/gold_studies.tsv` rows `Gs0118431`, `Gs0118434`, and `Gs0153647` |
| Cave and microbial-mat material MIxS triads | `data/raw/gold_path_triads.tsv` rows for the Cave microbial mat GOLD path |

The record has no record-level literature entry. A spot-check of Engel et al.
2003, DOI `10.1128/AEM.69.9.5503-5511.2003`, corroborates that groundwater-fed
sulfidic cave springs can contain directly sampled microbial mats dominated by
filamentous bacteria, but that paper is not a maintained HabitatMech input and
was not linked to `gold.ecosystem:5967` during this review.

No causal graph is attached to this record, so there are no mechanism edges
needing claim-level `EvidenceItem` support.

## Completeness

The required generated identity, category, source attestation, source-derived
parent, curation history, and seeded mapping status are present.

The empty optional slots are acceptable for the current generated record:

| Slot | Review |
|---|---|
| `environmental_parameters` | Empty. The GOLD path has committed aggregate MIxS triads but no source row in the maintained `environmental_parameters.tsv`, and no curator-authored parameter row is expected for a review-only generated concept. |
| `characteristic_taxa` | Empty. The GOLD aggregate does not commit organism names or taxon identities for `gold.ecosystem:5967`. |
| `evidence` | Empty. There is no item-level curation row, causal overlay, or maintained literature artifact for this record yet. |
| `causal_graphs` | Empty. Exact ignored-inclusive searches found no relevant `curation/causal_graphs/*cave*` or `curation/causal_graphs/*microbial*` overlay and no overlay keyed to `habitatmech:GOLD.aed29e2fc1`. |
| `discussions` and `datasets` | Empty. No maintained discussion or dataset input exists for this record. |

Exact ignored-inclusive searches for `habitatmech:GOLD.aed29e2fc1`,
`gold.ecosystem:5967`, `cave_microbial_mat`, `Cave microbial mat`, and the GOLD
source path found the generated record, its `PATHS.tsv` row, the raw GOLD path
inventories, and the class-level decision row. They did not find a
target-specific term request, causal overlay, history record, research report,
or prior YAML review report.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | None found | The generated record validates, denotes the expected GOLD source path, and carries the correct `SEEDED` status for a source concept with only a class-level decision. | Not applicable |
| Major | The class-level `CONFIRM_UNGROUNDED` row missed the vendored `ENVO:01000008` `microbial mat` parent and left Cave microbial mat under a non-strict `Groundwater` parent. This is a real cave microbial mat habitat, not a lexical false positive; it needs item-level curation to attach the same microbial-mat parent used by other setting-specific GOLD microbial-mat records. | `data/raw/ontology_terms.tsv` includes `ENVO:01000008` `microbial mat`, and existing item-level `GROUND_AS_PARENT` rows in `curation/decisions.tsv` use that term as the broader parent for GOLD microbial-mat records whose settings keep them distinct from the generic ontology term. `data/raw/gold_path_triads.tsv` also assigns `ENVO:01000157` `microbial mat material` as the medium term for one of two complete Cave microbial mat triad samples and `ENVO:00000067` `cave` as the local term for both. | `curation/decisions.tsv`; possibly `curation/term_requests.tsv` if item-level review requests an explicit cave-microbial-mat term |
| Minor | None found | The remaining empty optional slots are consistent with the absence of maintained item-level curation or a causal overlay. | Not applicable |

## Recommended Edits

| Priority | Edit | Maintained path |
|---|---|---|
| Major | Revisit `habitatmech:GOLD.aed29e2fc1` with item-level curation. Replace the class-level lexical decision with a `GROUND_AS_PARENT` decision to `ENVO:01000008` `microbial mat` and `grounding_status` `NARROW`, unless deeper item-level review finds a more specific exact term or merge target. | `curation/decisions.tsv` |
| Major | If Cave microbial mat stays as a distinct novel term after item-level review, replace the inherited GOLD `Groundwater` parent with `ENVO:01000008` so the generated hierarchy does not claim every cave microbial mat is pore-space groundwater. | `curation/term_requests.tsv` |

Do not hand-edit `data/habitats/aquatic/cave_microbial_mat.yaml`; regenerate it
from the maintained input after item-level curation changes.

## Follow-up Checks

| Edit | Narrowest proving checks |
|---|---|
| Item-level Cave microbial mat grounding | Exact ignored-inclusive `rg` for `habitatmech:GOLD.aed29e2fc1`, `gold.ecosystem:5967`, and `ENVO:01000008` should find the new maintained decision and any term request; `just seed-canary habitatmech:GOLD.aed29e2fc1`, `just term-requests-check`, `just validate data/habitats/aquatic/cave_microbial_mat.yaml`, `just validate-strict data/habitats/aquatic/cave_microbial_mat.yaml`, `just validate-history`, and `just verify-corpus --max-diffs 1` should still pass. |
| Parent replacement, if Cave microbial mat stays distinct | The regenerated `data/habitats/aquatic/cave_microbial_mat.yaml` should list `ENVO:01000008`, not `habitatmech:GOLD.22a80cbd14`, under `parent_habitats`; run `just validate data/habitats/aquatic/cave_microbial_mat.yaml`, `just validate-strict data/habitats/aquatic/cave_microbial_mat.yaml`, and `just verify-corpus --max-diffs 1`. |

## Additional Notes

- Searches used to establish absence included ignored and hidden files. Broad
  exact content searches excluded `data/text_map/**`, `pages/**`, `build/**`,
  and `.git/**` so generated text-map, rendered-page, build-product, and git
  object matches did not dominate the results.
- `ENVO:00000067` `cave` is a cave microbial mat's setting, not a broader
  parent of the mat. `ENVO:01000157` `microbial mat material` is the sampled
  medium in the GOLD triad row, while local GOLD precedent uses `ENVO:01000008`
  `microbial mat` as the strict broader parent for setting-specific microbial
  mat records.
- `data/raw/gold_path_biosamples.tsv` and `data/raw/gold_path_triads.tsv` are
  derived from GOLD's bulk export and API sweep, while
  `data/raw/gold_ecosystem_paths.tsv` comes from the kg-microbe KGX dump. The
  Cave microbial mat record's missing `assertion_count` is therefore expected
  even though the bulk/API inventory has three biosamples and two complete
  triads for `gold.ecosystem:5967`.
