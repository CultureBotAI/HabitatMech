# YAML Record Review: Hydrothermal plume

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/hydrothermal_plume.yaml`
- Started UTC: 2026-10-03T12:14:10Z
- Finished UTC: 2026-10-03T12:22:53Z
- Verdict: needs curation

## Target

The entire generated `HabitatRecord` was read: `habitatmech:GOLD.437f639705`,
Hydrothermal plume, `AQUATIC`, `UNGROUNDED`, `SEEDED`. Its sole source is GOLD
node 8198 on `Environmental > Aquatic > Marine > Hydrothermal vents >
Hydrothermal plume`; its sole parent is `ENVO:00000215` hydrothermal vent.
There is no definition or invented source count. The record has a class-level
no-match decision event and a seed event. `PATHS.tsv:1797` locks the stem.

## Validation

- `just validate data/habitats/aquatic/hydrothermal_plume.yaml`: pass.
- `just validate-strict data/habitats/aquatic/hydrothermal_plume.yaml`:
  one file, zero errors.
- The mint function reproduces the identifier from the exact GOLD path.
- Live OLS verified the vent parent and the plume candidates; a live ENVO
  search returned `ENVO:01000130` as the direct marine-hydrothermal-plume hit.
- Baseline `just qc`: all gates passed; 451 tests passed, three skipped,
  two dependency warnings; 3,206 records reproduce and validate, with current
  site/redirects. OAK label correspondence is a separate CI gate.
- No PMID, DOI, taxon, gene, or mechanism claim is present to validate.
  iModulonDB is not applicable. The public GOLD study page could not be
  retrieved; study/path verification here is against the committed snapshot.

## Identity and Grounding

The marine path identifies a plausible habitat feature, not the geological
opening that emits it. Current `ENVO:00000215` defines a vent as the fissure
from which heated water issues. The stored parent is therefore not a strictly
broader class of plume.
[Hydrothermal vent](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000215).

`curation/decisions.tsv:457` still carries the CLASS-depth lexical no-match
sweep. However, `data/raw/ontology_terms.tsv:7636` already contains
`ENVO:01000130` marine hydrothermal plume, and live OLS confirms the active
term. Its definition describes a high-temperature water jet associated with
a marine vent; its direct parent is `ENVO:01001308` hydroform, not a vent.
It is a strong candidate that the old decision has not assessed.
[Marine hydrothermal plume](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000130).

Do not automatically equate every plume sample with a near-source jet.
NOAA distinguishes rising mixed fluids from laterally dispersed neutrally
buoyant plumes, including signals beyond vent fields. Those are related
physical stages, not vent fissures. The available source row does not specify
which stage its one sample represents. [NOAA plume formation](https://www.pmel.noaa.gov/eoi/PlumeStudies/plumes-whatis.html),
[NOAA mixing and neutral buoyancy](https://www.pmel.noaa.gov/eoi/PlumeStudies/plumes-whystudy.html).

The generic `ENVO:01001743` plume is also current but much broader and not
automatically the best grounding. `BTO:0002480` plume is an anatomical
structure and is explicitly not a candidate for this marine water feature.
`SEEDED` correctly reflects the absence of ITEM-level curation.

## Evidence

| Claim | Inspected support and scope |
|---|---|
| Exact GOLD identity | `gold_ecosystem_paths.tsv:1519` has this five-level path, one node (8198), and zero recorded organism/study/biosample counters in that inventory. The generated omission of `assertion_count` is correct. |
| Independent biosample inventory | `gold_path_biosamples.tsv:971` has one biosample for path ID 8198. This separate inventory is not a reason to invent a one-ORGANISM assertion. |
| Study membership | `gold_studies.tsv:4522`, `Gs0161798`, lists this as its only path. No extra stage, chemistry, or microbial mechanism follows from the path alone. |
| Candidate present in maintained evidence | `ontology_terms.tsv:7636` and `ontology_subclass_edges.tsv:5780` provide the marine plume candidate and hydroform parent. Both agree with live OLS. |
| Plume/vent distinction | NOAA's inspected plume descriptions explain fluid discharge, seawater entrainment, buoyant ascent, and lateral dispersal. None makes the emitted plume a subclass of the emitting fissure. |

No exact-path triad row was found in the ignored-inclusive raw-inventory
search. Related vent-fluid mechanisms and nearby vent records cannot be
transferred as evidence for this particular source concept.

## Completeness

The material gap is ITEM-level scope/grounding review, not missing optional
taxa, numeric parameters, or a generic mechanism graph. The candidate must be
compared with source-study/sample descriptions before choosing exact identity,
a broader relation, or a justified minted definition.

Hidden/ignored-inclusive searches covered the ID, label, stem, full path,
candidate IDs, and source key across `curation`, `history`, `research`, `conf`,
the raw inventories, and path lock. They found the class decision and the
candidate ontology row, but no target-specific definition, session history,
or causal overlay. Mentions of plume formation in `hydrothermal_vent.yaml`
belong to that separate target. Exact report-header coverage includes ignored
files and found no previous individual report for this record.

## Findings

1. **Major: the plume is asserted to be a kind of vent fissure.** The GOLD
   path describes origin/context, not a supported is-a relation. Owner: GOLD
   parent-path contribution in `src/habitatmech/seed.py` and a validated
   maintained exclusion/curation input. Grounding to the plume term alone
   must not leave the inappropriate GOLD vent parent behind.
2. **Minor: a class-level no-match decision omits an existing, relevant
   ontology candidate.** `ENVO:01000130` is present in both the snapshot and
   current ENVO; the source's Marine path strengthens its relevance. The old
   lexical result cannot stand in for an ITEM-level scope assessment. This is
   an unresolved candidate, not proof that the present identity is wrong. Owner:
   `curation/decisions.tsv`, optionally `curation/term_requests.tsv` only if
   the inspected source scope genuinely needs a minted definition.

Blockers: none. Total: one major, one minor.

## Recommended Edits

1. Remove only the unsupported GOLD vent-parent contribution and retain the
   full source path. Preserve any independently supported hydroform or other
   true broader parent introduced by a later reviewed decision.
2. Inspect the source study/sample scope and compare it with the current
   marine plume definition, explicitly distinguishing a hot jet from a
   dispersed neutrally buoyant plume. Record an ITEM decision with the
   supported relation; do not auto-ground from lexical similarity alone.
3. Keep sample and organism inventory units separate. Do not manufacture
   numeric parameters or mechanism evidence while resolving identity.

## Follow-up Checks

Append session history for actual curation, run dry seeding and a forced
canary, and inspect identity, parents, counts, and generated review status.
Run focused schema/strict validation, OAK `just validate-products`,
`just validate-history`, and `just verify-corpus`. A changed identity may
require the repository's path-lock/redirect workflow; do not rename files
manually. Regenerate and validate the complete semantic map and site before
full QC if semantic fields change.

## Additional Notes

This report does not establish an exact mapping or authorize replacing the
whole plume by its fluid component. It documents the unassessed candidate and
the independently unsupported source-parent edge. No corpus or curation
input was changed.
