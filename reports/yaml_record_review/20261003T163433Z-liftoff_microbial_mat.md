# YAML Record Review: Liftoff microbial mat

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/liftoff_microbial_mat.yaml`
- Started UTC: 2026-10-03T16:31:39Z
- Finished UTC: 2026-10-03T16:34:33Z
- Verdict: needs curation

## Target

Read the complete generated `HabitatRecord`, `habitatmech:GOLD.2f4b860753`,
label Liftoff microbial mat, AQUATIC, UNGROUNDED, SEEDED. The single source is
GOLD node 7783 at Environmental > Aquatic > Freshwater > Ice > Liftoff
microbial mat. `PATHS.tsv:1635` pins the record stem. The CLASS-level
CONFIRM_UNGROUNDED row in `curation/decisions.tsv:359` explicitly does not
establish habitat validity; its history and the deterministic seed event do
not constitute ITEM review.

## Validation

- `just validate data/habitats/aquatic/liftoff_microbial_mat.yaml`: pass.
- `just validate-strict data/habitats/aquatic/liftoff_microbial_mat.yaml`:
  one file, zero errors.
- Fresh `just qc` was running at review finish: lint, documentation and raw
  provenance passed; tests were active. Corpus reproduction, full history,
  causal-overlay, site, redirect and term-request gates are full-corpus checks
  in that runner, not claimed passed before completion.
- Inspected `conf/id_label_targets.yaml`: minted IDs are deliberately skipped
  by OAK. Current ENVO terms below were checked directly through official OLS
  JSON. The web fetch of the API failed; a direct structured request succeeded.
- No record-level DOI/PMID, taxon, graph, dataset or parameter references exist
  to validate. GOLD study membership below was checked in the committed
  inventory, not asserted to be a live study-page verification.

## Identity and Grounding

The minted identity correctly preserves a specific source concept. The record
is a microbial mat in a freshwater ice-associated setting, not ice itself.
Current ENVO defines `ENVO:01001511` freshwater ice as water ice formed from
fresh water. The complete current freshwater-ice parent record was also read.
Its presence in the GOLD path explains the edge but does not make the mat a
subclass of ice.

`ENVO:01000008` microbial mat is an inspected broader candidate, not exact
identity for the qualified source. `ENVO:01000157` microbial mat material is
material derived from a mat; the API medium annotation alone must not change
the whole mat into sampled material. No claim is made that every ontology
lacks an exact lift-off class.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:1473` has one depth-five node and zero
organism assertions. Omitting an assertion count is faithful, not evidence of
an uninhabited habitat. `gold_path_biosamples.tsv:729` independently records
six samples. `gold_studies.tsv:1057` links Gs0118069 to this path and Glacier
meltwater; that shared study does not equate the two habitats.

API rows 311-313 have six samples, one study and complete agreement within
each slot: broad `ENVO:01000252` freshwater lake biome; local `ENVO:00000488`
glacial lake; medium `ENVO:01000157` microbial mat material. All three IDs and
definitions were inspected via current official OLS JSON. These are contextual
triad roles, not three equivalent habitat identities, and are not summed with
the separately sourced bulk sample count.

The inspected primary [2025 liftoff-mat study](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JG008516),
especially the abstract and methods on mat morphologies, documents
bubble-deformed mats in Antarctic lakes. Some remain attached; others detach
and reach the underside of lake ice. This supports the distinction between
mat and ice, not a requirement that every lift-off mat already be detached,
frozen, Antarctic, or endowed with an identical microbial community. The
article is new review evidence, not a citation already present in the YAML.

## Completeness

Ignored-inclusive identifier, label, stem and node searches covered curation,
raw inventories, PATHS, history, research and prior review reports. They found
the CLASS row and source context, but no target ITEM decision, authored
definition, causal overlay, dedicated history record or previous individual
report. Related ice/glacier reports were context, not new completed reviews.

The missing definition merits bounded ITEM curation together with the false
parent, not a second count of the same hierarchy finding. Optional taxa,
parameters, mechanisms and datasets should remain empty absent specific
evidence. iModulonDB is not applicable: this record has no organism/strain,
gene, regulator or expression-module claim.

## Findings

- **Major M1: microbial mat is asserted to be freshwater ice.** The sole
  `parent_habitats` value, `ENVO:01001511`, is location/context rather than
  strictly broader identity. Owner: GOLD's second parent pass in
  `src/habitatmech/seed.py:898`, with target-specific maintained curation
  controls or a justified definition in `curation/term_requests.tsv` and an
  ITEM row in `curation/decisions.tsv`. Adding a true mat parent while retaining
  ice does not fix the error.
- Blockers: 0. Major: 1. Minor: 0.

## Recommended Edits

Perform ITEM review, preserve the minted source and its ice/freshwater context,
and establish microbial mat as a broader genus without exact-merging the
specific source into all mats. Remove the false ice parent through the
maintained source-parent mechanism, or use definition `REPLACE` only after
documenting that the single inherited parent is false. Distinguish mat from
mat-derived material and do not define all lift-off mats as already floating.
Append curation history, canary, reproduce and regenerate through supported
pipelines. No scientific input or generated record was changed by this review.

## Follow-up Checks

Run `just seed`, the exact-source canary, focused normal/strict validation,
`just validate-products`, `just verify-corpus`, supported map/site regeneration
and `just qc`. Assert that the false ice edge is gone while source node, full
path, independent inventory units and minted identity remain intact. Existing
regeneration dependencies #1217/#1218 must not be bypassed.

## Additional Notes

All 433 returned open/closed issues and their comments were searched. #1223
already owns related ice-context parent errors, including additional individual
cases; this target can extend it without claiming its fix is present in draft
#1218. Review reports do not promote generated mapping status or append
curation history. Only this target counts toward completed-record coverage.
