# YAML Record Review: External surfaces

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/external_surfaces.yaml`
- Started UTC: 2026-10-08T12:20:58Z
- Finished UTC: 2026-10-08T12:24:40Z
- Verdict: needs curation

## Target

Generated HabitatRecord `habitatmech:GOLD.24c703f190`, External surfaces,
ENGINEERED / UNGROUNDED / SEEDED. The entire target and immediate spacecraft
record were read. The target is the full depth-five path
`Engineered > Built environment > Spacecraft Assembly Cleanrooms > Spacecraft > External surfaces`,
not generic external surfaces or an unspecified in-orbit microbial environment.
Baseline: e2572cfdd.

## Validation

- `UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/external_surfaces.yaml`:
  passed, no issues.
- `UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/external_surfaces.yaml`:
  passed, one file, zero errors.
- Complete target regeneration in memory matched the parsed YAML exactly;
  one source, zero ITEM-reviewed contributors. Target and parent routes were
  executed with full current indexes and decisions.
- Same-session `just verify-corpus`, `just validate-history` and
  `just provenance-check` passed: 3,207 matching records, 184 valid histories,
  14 inventories and two GOLD sources current.
- Full QC reuses unchanged scientific/code/history/configuration baseline
  a56b92e16, verified by fresh git comparison: 590 tests passed, three skipped,
  all remaining gates and queue label checks passed. See [PR #1715 receipt](https://github.com/CultureBotAI/HabitatMech/pull/1715#issuecomment-6059147859).
  Those checks do not establish the semantics of a source-derived parent.
- Original sample-level reconstruction and export compatibility were not checked;
  the necessary original GOLD files were unavailable in the searched local bounds.

## Identity and Grounding

The full-path hash reproduces the target mint; `PATHS.tsv:1561` locks the stem.
Automatic resolution is `gold_unmatched`. The CLASS CONFIRM_UNGROUNDED row
at `curation/decisions.tsv:308` preserves that mint, no mapping predicate and
UNGROUNDED. The history explicitly records that habitat identity was not
assessed by the class sweep. SEEDED accurately reflects that limitation.

The immediate Spacecraft path has mint `habitatmech:GOLD.f96ea35aa9` and takes
`gold_leaf_label` to ENVO:01003000, EXACT, unchanged by decisions. Its source-
path contribution is the target's sole parent. The active ontology class is
a spaceflight vehicle, not the surface of one. The reference resolves correctly
but makes the wrong is-a assertion. No definition or independent ontology
subclass supplies a second justification for the edge.

## Evidence

- `data/raw/gold_ecosystem_paths.tsv:1283` contains the exact path, single
  node `gold.ecosystem:8287`, and zero organism, study, biosample and total
  assertions. The generated source ID, label and path agree; omitted count,
  unit and multi-node note are correct. Zero snapshot assertions do not prove
  microbial absence or sterility.
- The primary [GOLD ecosystem workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths),
  fetched with worksheet dimensions reset, confirms node 8287 and the complete
  path at `site data` row 227. It confirms the classification, not a particular
  mission, assembly phase, sample or organism.
- The inspected [pinned ENVO source](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
  confirms active ENVO:01003000 spacecraft and its vehicle parent ENVO:01000604.
  The local canonical label and definition agree with that source.
- The inspected [NASA JPL mission-implementation page](https://planetaryprotection.jpl.nasa.gov/mission-implementation)
  distinguishes spacecraft hardware from its exposed surfaces and describes
  swab/wipe recovery of biological material during cleanroom sampling. This
  supports treating a surface as a microbial sampling context rather than
  a whole vehicle. It does not identify node 8287's original samples or prove
  viable growth on every surface. No mission, taxon, assay result, sterilization
  condition or current regulatory requirement was transferred to the record.

## Completeness

Definition, synonyms, xrefs, parameters, taxa, evidence, causal graphs,
discussions and datasets are empty. Their absence is not itself a defect.
Cleanroom context does not support inferred vacuum exposure, radiation tolerance,
spaceflight survival, a particular alloy, or a characteristic microbial community.
iModulonDB is not applicable to this taxon-free category record.

Ignored-inclusive exact ID/path/stem/node and broader external-surface searches
covered curation, raw inventories, PATHS/RETIRED, history, research, configuration,
docs, tests and reports. Filename traversal covered curation/history/research,
including ignored files. These found the CLASS decision and source/lock rows;
broader research hits concern unrelated host surfaces. No target-owned definition,
exclusion, causal overlay, research report, session history or earlier individual
review was found in those bounds. Exact-field/pipe-member inspection of all raw
TSVs found only the ecosystem row for this target, not a study, bulk-count,
complete-triad, parameter or taxon contribution.

A full local ontology label/synonym scan found no external-surface or spacecraft-
surface lexical candidate. This is not a claim that no suitable ontology term
exists elsewhere. Fresh ignored-inclusive find under build, data/raw and the
configured local kg-microbe data tree found no original GOLD node/edge dumps,
goldData.xlsx, gold_biosample_triads.tsv or biosample JSONL intermediates.

## Findings

1. **Major: a spacecraft surface is incorrectly a kind of spacecraft.**
   `parent_habitats: ENVO:01003000` comes from the immediate source path,
   whereas the inspected vehicle class and primary sampling description
   establish a surface/whole-object distinction. Maintained owner:
   `curation/gold_parent_exclusions.tsv`, guarded by this mint, complete
   five-level path and expected resolved ENVO:01003000 parent.

No blockers or separate minor findings. The record's unknown biological
membership is preserved rather than treated as an invalid source category.

## Recommended Edits

In a separately authorized curation change, exclude only the exact GOLD
spacecraft-parent contribution, append required history, canary and regenerate.
Retain source identity, file lock, full path, omitted counts, ENGINEERED and
CLASS/SEEDED lifecycle. Do not invent a surface definition to suppress the edge.
If a broader surface/material class or richer part/context relation is later
supported, represent it through an appropriate maintained input rather than
turning the whole spacecraft into a genus.

## Follow-up Checks

Inspect the canary for loss of only ENVO:01003000 and the corresponding
SOURCE_PARENT_EXCLUDED event, with all source metadata preserved. Run strict
validation, exact reproduction, history and full QC after curation. Any future
definition needs the actual assembly/sample context; do not generalize from
orbital external-surface studies or the cleanroom's own taxa. Compare semantic-
map inputs after scientific changes before deciding whether inference is needed.

## Additional Notes

Read-only review: one new timestamped report, no scientific, generated,
historical-report or GitHub changes. Reading the spacecraft parent does not
count as a completed review of that parent. No SSSOM/KGX readiness claim.
