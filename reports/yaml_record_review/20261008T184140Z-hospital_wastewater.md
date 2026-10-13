# YAML Record Review: Hospital wastewater

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/hospital_wastewater.yaml`
- Started UTC: 2026-10-08T18:38:33Z
- Finished UTC: 2026-10-08T18:41:40Z
- Verdict: pass with minor issues (0 blocker, 0 major, 1 minor)

## Target

Read the entire generated HabitatRecord `habitatmech:GOLD.242c0c0793`,
Hospital wastewater, ENGINEERED / UNGROUNDED / SEEDED, and the complete
Industrial wastewater parent. One source attestation, one parent and two
history events; no authored definition. Exact source:
`Engineered > Wastewater > Industrial wastewater > Hospital wastewater`.
Baseline: 2058819d402cf5e464d09615f5fe464ec1f48ed4.

## Validation

- `UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/hospital_wastewater.yaml`:
  passed, no issues.
- `UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/hospital_wastewater.yaml`:
  passed, one file, zero errors.
- Fresh full-corpus construction exactly reproduces the complete parsed target:
  one source, zero reviewed contributors, no authored definition or exclusion.
  Actual target/parent default and applied resolutions used complete indexes.
- Full QC is reused, not rerun for report-only work. Fresh same-turn comparison
  verifies the baseline equals the PR #1742 reviewed tree. Head/queue QC,
  labels and vendored checks passed; head QC recorded 595 tests passed, three
  skipped, 197 valid histories and 3,207 reproduced records with all gates
  passing. [Receipt](https://github.com/CultureBotAI/HabitatMech/pull/1742#issuecomment-6066368637).
- Direct ENVO checks below supplement that receipt. No target graph/literature
  references or separate session histories need a focused validator. Original
  study/member joins and SSSOM/KGX compatibility were not verified.

## Identity and Grounding

The exact path regenerates the identifier and matches `PATHS.tsv:1557`.
Default `gold_unmatched` becomes `curated_confirm_ungrounded_from_gold_unmatched`
through the CLASS decision at `curation/decisions.tsv:305`, without a predicate.
The two events and SEEDED state correctly avoid implying completed ITEM review.
This is a wastewater-material source concept, not the hospital building,
a treatment plant, clinical procedure or patient taxon.

The source parent mint `habitatmech:GOLD.229580fa29` resolves by
`gold_leaf_label` to `ENVO:01000964` industrial wastewater, EXACT, without an
override. That ontology term requires industrial origin and chemical
contaminants beyond those associated with urine/feces; its asserted broader
term is `ENVO:00002001` waste water. The target receives this parent only
through the GOLD path, not an independent ontology, ambiguous-leaf or authored
definition contribution.

Unlike a generic ontology-grounded material that acquires every source context
as a universal parent, this record retains the industrially classified GOLD
mint. No independent evidence establishes that this particular source bin is
misclassified. Nevertheless, the path alone is not a chemical assay or a
definition of all hospital wastewater. The precise qualified-source boundary
needs explicit verification before generic renaming, a definition or ITEM
endorsement. Neither automatic exclusion nor universal industrial classification
is justified by the present evidence.

## Evidence

- `gold_ecosystem_paths.tsv:440` supplies nodes 4917/4918, 17 ORGANISM
  assertions, zero study/biosample counters and total 17. The first-node ID,
  two-node note, count and unit all agree; these are not 17 named taxa.
- Fresh [GOLD workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths)
  row 434 contains node 4918 with this path and trailing Unclassified.
  Worksheet dimensions were reset before iteration. SHA256
  `f8e4cb5cf89ecc88d3cf28170cfc3a1cf47daed8218408a52914c53667dfd3d4`,
  84,174 bytes. It corroborates classification, not the historical organism join.
- Fresh [GOLD organism-tree JSON](https://gold.jgi.doe.gov/download?mode=organismEcosystemsJson)
  contains the exact source branch with count 17 and an Unclassified child also
  counted 17. These are not independent observations to add. SHA256
  `49ef0a3e654a79f6b7e7140d2cdb2ac0ce0bb1df2ccb8decae68d129eeb7ca11`,
  1,450,415 bytes.
- Fresh [pinned ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
  confirms industrial wastewater, waste water and sewage meanings and parents.
  General waste water is broader; sewage requires fecal/urinary contamination;
  neither is an exact hospital-source identity. SHA256
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`,
  9,614,229 bytes.
- Inspected [WHO training module 23](https://www.who.int/docs/default-source/wash-documents/wash-in-hcf/training-modules-in-health-care-waste-management/module-23---management-of-health-care-wastewater.pdf?sfvrsn=b41a0db0_2),
  PDF pages 4-7, describes water affected during healthcare services and varied
  ward, kitchen, laundry, toilet and technical/laboratory sources. It distinguishes
  blackwater and greywater and discusses non-excreta chemical constituents.
  This supports a heterogeneous healthcare effluent category, not a fixed
  contaminant requirement for every stream or equivalence to industrial activity.
  Its clinical hazards, concentrations, treatment instructions and regulatory
  implications are not adopted as target claims or current practice guidance.

`gold_path_biosamples.tsv:309` independently records 65 BIOSAMPLE observations
for this path. Eight study rows refer to it: Gs0121340, Gs0145189, Gs0145269,
Gs0150505, Gs0150605, Gs0150672, Gs0150673 and Gs0150735. Gs0150505 also
names the parent industrial-wastewater path. These inventory memberships do
not establish independent replication, current study contents, uniform chemistry,
or 65 organisms; original submissions were not reconstructed or recounted.

## Completeness

Ignored-inclusive identifier, label, stem, node and path searches covered raw
inventories, curation, configuration, docs, tests, PATHS/RETIRED, histories,
research, its manifest and individual reviews. Filename traversal covered
curation/history/research. No target-owned ITEM decision, definition, exclusion,
overlay, session history, research file or prior individual report was found
in those bounds beyond the existing CLASS row.

Exact-field/pipe-member scanning of all raw TSVs found the ecosystem row,
biosample aggregate and eight study rows, but no target triad, parameter or
taxon row. Same-turn ignored-inclusive find under build, data/raw and configured
kg-microbe data found no original GOLD dumps, bulk workbook or sample/triad
intermediates. A complete local label/synonym scan, including waste-water
spacing variants and hospital/healthcare/medical/clinic combinations, and a
whole pinned-OWL label/synonym scan found no exact hospital-effluent term.
That is a bounded candidate search, not a global ontology-absence claim.

Optional taxa, chemistry, mechanisms, citations, discussions and datasets should
remain empty without source-specific support. A missing definition or CLASS
status alone is not a finding. iModulonDB is not applicable without a gene,
regulator, strain-expression or transcriptomic assertion.

## Findings

1. **Minor: the industrially qualified source scope remains implicit beyond
   its path.** The bare label can be read as all hospital discharge, whereas
   the retained parent has a more specific origin/composition definition and
   WHO describes heterogeneous healthcare streams. This is a bounded scope-
   verification gap, not proof that the parent is false for GOLD's classified
   subset. Owners: `curation/decisions.tsv` for the source-level ITEM rationale
   and `curation/term_requests.tsv` only if a precise definition is supported.
   No blocker or major correction is established from the available evidence.

## Recommended Edits

Recover the actual source members and determine whether the bin denotes all
hospital discharge or a specific industrially classified stream. Preserve the
mint, 17 ORGANISM assertions, both source nodes and separate biosample/study
units. Record the resulting scope explicitly through maintained inputs before
renaming or exact grounding. If that inspection disproves the industrial genus,
use `curation/gold_parent_exclusions.tsv` for only that contribution and assess
a broader waste-water relation; do not remove it merely because the generic
label is wider or because an optional definition is absent.

## Follow-up Checks

Check source-member scope against both defining conditions of the industrial
parent. Verify candidates and typed synonyms, all parent contributions and
preservation of distinct units. For any authorized curation: dry seed, inspect
a canary, append history, then schema, labels, provenance, exact reproduction,
map/site freshness, redirects and full QC. Do not infer universal antibiotics,
resistance genes, treatment state or a characteristic microbiome from this bin.

## Additional Notes

Only this new report was written. Scientific/generated inputs, prior reviews,
history, review status and GitHub remain unchanged. The larger WHO handbook
failed to open in the web tool; its search excerpt was not used as inspected
evidence. The separate module cited above was actually read. Parent context
reads do not count as an individual Industrial wastewater review.
