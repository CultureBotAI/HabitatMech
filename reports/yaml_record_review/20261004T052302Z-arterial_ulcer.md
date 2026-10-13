# YAML Record Review: Arterial ulcer

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/arterial_ulcer.yaml`
- Started UTC: 2026-10-04T05:16:41Z
- Finished UTC: 2026-10-04T05:23:02Z
- Verdict: pass with minor issues

## Target

Read the entire generated HabitatRecord `habitatmech:GOLD.03b138e563`:
HOST_ASSOCIATED, NOT_APPLICABLE, REVIEWED. It has one GOLD attestation, one
parent and two August 12/16 events. Source scope is Human > Multisystem
conditions > Arterial ulcer, not arterial blood, an artery, or the separate
Lesion site child. The actual `mint` helper reproduces the identifier;
`data/habitats/PATHS.tsv:1294` pins the filename.

## Validation

- `just validate data/habitats/host_associated/arterial_ulcer.yaml`:
  passed, no issues.
- `just validate-strict data/habitats/host_associated/arterial_ulcer.yaml`:
  one file, zero errors.
- Fresh batch `just validate-products`: passed; 1,179 canonical pairs,
  one synonym, five configured exceptions and 2,054 no-adapter skips.
- Full QC for the unchanged baseline `c198d8d123a4d19d283d98f2744e474bc7eadced`
  passed in [run 37179294525](https://github.com/CultureBotAI/HabitatMech/actions/runs/37179294525).
  The matching merge-group run 37178947305 passed 457 tests with three skips
  and two warnings, plus corpus reproduction and the other QC gates. No
  fresh full local QC is claimed for this read-only review.
- PubMed's browser page challenged access; primary EFetch XML succeeded.
  No inaccessible full text is treated as inspected evidence.

## Identity and Grounding

`curation/decisions.tsv:117` is an ITEM NOT_APPLICABLE decision. Generated
status and history accurately reproduce it, but its generic list of disease,
intervention, artifact or filler does not explain which interpretation applies.

The complete reference records establish a meaningful source distinction:
`multisystem_conditions.yaml` is the class-swept clinical umbrella
`habitatmech:GOLD.25f514731f` (node 6357), whereas `lesion_site.yaml` is the
separate class-swept child `habitatmech:GOLD.2f12ab3480` (node 7034) below this
target (node 7033). This is source-specific support for retaining a clinical-
condition interpretation of node 7033. It is not proof about sampled material.
The parent is not grounded to a whole anatomical organ; no independent
whole-organ superclass defect like the appendix-abscess case is established.
This is not an approval of every edge in the surrounding clinical branch.

Current OLS searches for arterial ulcer and ischemic ulcer returned disease,
phenotype and procedure candidates, including SNOMED lexical matches. Only
the first 12 results per query were inspected, not an exhaustive ontology
inventory. No exact environment identity was verified or adopted, and no
candidate's non-obsolete status is claimed from search results alone. A
disease-term label match is not habitat equivalence.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:2352-2353` contains the target and its
Lesion site child, each with one node and zero organism, study, biosample and
total assertions. Source label, path and node ID agree. Omission of count/unit
is consistent with the seeder's nonzero-organism rule, not a lost observation.

Complete structured scans of 2,562 GOLD paths, 1,040 bulk rows, 4,587 studies
and 1,587 triads found only those two tree rows for the target key and
arterial/ischemic/ischaemic-ulcer variants. No specimen-level source evidence
was found to decide a different disposition.

The complete primary abstract of [Schmidt et al.](https://pubmed.ncbi.nlm.nih.gov/10731891/)
describes ulcer-area swabs in a 63-patient cohort that includes arterial leg
ulcers. EFetch's primary ArticleIdList verifies PMID:10731891 and
DOI:10.1024/0301-1526.29.1.62. It supports arterial-ulcer wounds as physical
microbial sites, not a particular interpretation of GOLD node 7033 versus
7034. No taxa, percentages, mechanisms or treatment claims are imported;
positive culture is not equated with clinical infection. Only the abstract,
not the full methods, was inspected.

## Completeness

Ignored-inclusive identifier/label/stem searches covered curation, raw data,
history, research, prior review reports, PATHS and RETIRED. They found no
target definition request, overlay, session record, research report, earlier
exact-target review or retired-URL match. References from other reviews are
not reviews of this target. An older decision lacking later-style session
history is not a separate defect.

Full structured scans of 162 BacDive sources, 3,081 BacDive taxa, 770
parameter rows, 358 mappings, 58 Madin habitats, 1,378 Madin taxa, 719 PREGO
habitats and 8,807 PREGO taxa found no target-key or inspected ulcer-variant
match. These are bounded inventory searches, including ignored files, not
claims that ulcer research or ontology terms do not exist. Optional taxa,
parameters and graphs need not be filled. iModulonDB is not applicable: no
gene, regulator or expression claim is supplied.

## Findings

1. **Minor - HM-ARTERIAL-ULCER-001:** the exclusion rationale is generic and
   can be read as denying that a physical arterial-ulcer wound is a habitat.
   Explain the retained clinical-condition interpretation using GOLD's
   separate Lesion site child, and acknowledge the physical-site evidence
   without claiming that it identifies this source node. Owner:
   `curation/decisions.tsv:117`. The broader disease/site family is already
   tracked in [#220](https://github.com/CultureBotAI/HabitatMech/issues/220).

No blocker or major finding established for this target. Lack of specimen
evidence is unresolved uncertainty, not proof that the current disposition
is wrong. Neither the ITEM flag alone nor primary wound microbiology alone
settles that question.

## Recommended Edits

Replace the boilerplate with a node-specific explanation; retain identity,
NOT_APPLICABLE, ITEM depth, source path and counts. Attribute the new reasoning
to its actual agent/date, append session history, and regenerate through the
guarded seeder. Do not merge Lesion site, ground to a disease or arterial blood,
or mass-reclassify ulcer sources. Keep #220 open for the broader modeling work.

## Follow-up Checks

Inspect the canary and verify that only audit content changes. Run strict
validation, history validation, corpus reproduction, render freshness and
full QC. The actual semantic adapter gives unchanged text when history or
grounding status alone changes; removing the parent does change it. Thus a
rationale-only correction does not depend on map-runtime issue #1217, while
future definition or hierarchy changes require an actual map-input comparison.

## Additional Notes

The full 501-issue body/returned-comment scan found #220 as the existing owner
for the target/family search. Reuse it rather than creating a duplicate family
issue. This report itself changes no scientific input, generated artifact,
status or history; a later curation step may implement the minor correction.
Reference reads do not increase record-review coverage. No paid research ran.
