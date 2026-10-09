# YAML Record Review: industrial wastewater

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/industrial_wastewater.yaml`
- Started UTC: 2026-10-09T00:04:35Z
- Finished UTC: 2026-10-09T00:07:32Z
- Verdict: pass (0 blocker, 0 major, 0 minor)

## Target

Read the entire generated HabitatRecord ENVO:01000964 at
`d054c5813515fa33ec1872de1b44ebac948ee50e`: ENGINEERED / EXACT / SEEDED,
with an ENVO definition, one parent, one GOLD attestation and one seed event.
The exact source path is `Engineered > Wastewater > Industrial wastewater`.
The complete parent `waste_water.yaml` was read for context; its taxa,
parameters and causal graph are not target assertions or separately reviewed
here. The target is a wastewater material, not a facility or treatment process.

## Validation

- Fresh `UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/industrial_wastewater.yaml`:
  no issues.
- Fresh strict validation with that cache setting: one file, zero errors.
- Full-index in-memory construction and `build_document()` matched every
  target field: one contributor, zero reviewed contributors, no applied
  decision, authored definition or GOLD parent exclusion.
- Shared checks freshly run in this report-only session passed:
  `just verify-corpus` (3,208 expected/present, no differences),
  `just validate-history` (205 valid histories), and `just provenance-check`
  (14 inventories and two GOLD sources current).
- Full QC was not rerun per target. The unchanged baseline passed 620 tests,
  three skips and all gates in the immediately preceding local publication
  run and native queue [QC](https://github.com/CultureBotAI/HabitatMech/actions/runs/37861582587).
  Baseline [label correspondence](https://github.com/CultureBotAI/HabitatMech/actions/runs/37861582591)
  passed. These checks do not validate original biological-member assignments
  or the interpretation of every environmental-triad row.

No original organism/sample join or SSSOM/KGX compatibility audit was performed.

## Identity and Grounding

The exact source mint is `habitatmech:GOLD.229580fa29`; `PATHS.tsv:868`
locks the resolved ontology ID to this filename. Actual default and applied
resolution, using the complete ontology/mapping/claimant indexes, both use
`gold_leaf_label`: ENVO:01000964 / EXACT / skos:exactMatch, with no decision
and reviewed=False. SEEDED honestly reflects that lifecycle. The separate
BacDive mapping row at `isolation_source_groundings.tsv:160` is not this
earlier direct-label resolution and adds no BacDive attestation.

Primary [pinned ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
confirms the active canonical label, definition of industrially affected
wastewater with non-sanitary chemical contaminants, and direct superclass
ENVO:00002001, waste water. The target has no ontology synonym assertion to
mis-scope. Its label and full source path support the selected material
identity without dropping a narrower source modifier.

The sole parent is independently supported by that ENVO subclass axiom and
by the immediate GOLD Wastewater path. Parent source mint
`habitatmech:GOLD.1a43260310` takes `gold_mapping_table`, followed by an ITEM
REVIEW, to the same ENVO:00002001. Its review status, four-source merged
record and broader ecological assertions do not transfer to this target.

## Evidence

- `data/raw/gold_ecosystem_paths.tsv:106` has depth three, nodes
  3509/3836/4267 and 252 ORGANISM assertions, with zero direct study/biosample
  counts in that extraction. The generated first node, full path, three-node
  note, count and unit agree. These are not the parent's 1,140 organisms.
- The independently extracted `gold_path_biosamples.tsv:97` contains 325
  BIOSAMPLEs for node 4267. Exact pipe-member scanning found 26 study rows
  in `gold_studies.tsv`. Some studies also include sludge, soil, fecal,
  hypersaline, bioreactor, manure, rumen or hospital-wastewater paths.
  Membership does not transfer those other contexts or organisms to this
  target, and the distinct count units must not be summed.
- `gold_path_triads.tsv:155-157` represents two samples from one study, with
  one distinct term per slot and top share 1.00: broad ENVO:00000873
  freshwater biome, local ENVO:01000965 constructed swimming pool, and medium
  ENVO:00002011 fresh water. Complete primary OWL class inspection confirms
  all three IDs and labels. They denote a freshwater environmental system,
  a leisure-water construction and a low-solute water material, respectively.
- The primary [ENVO/MIxS guidance](https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS)
  distinguishes broad environmental systems, local surrounding entities and
  sampled materials. These are separate roles, not interchangeable habitat
  identities. This small pool-associated subset requires original sample
  context before interpreting its industrial classification; it does not
  establish that all 325 biosamples or 252 organisms came from pools.
  Fresh water also does not mean contaminant-free water. No universal pool,
  salinity, treatment or chemical-composition assertion is made by the target.
- Fresh [GOLD classification workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths)
  parsing, with worksheet dimensions reset, confirms node 4267 at `site data`
  row 451, followed by two Unclassified fillers. Its 84,174 bytes have SHA256
  `f8e4cb5cf89ecc88d3cf28170cfc3a1cf47daed8218408a52914c53667dfd3d4`.
  This verifies current classification, not historical nodes 3509/3836 or
  the frozen organism count.
- The inspected ENVO OWL SHA256 is
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
  The vendored target row at `ontology_terms.tsv:8459` and subclass row at
  `ontology_subclass_edges.tsv:6759` agree with the target/genus content.

## Completeness

Synonyms, xrefs, parameters, named taxa, literature evidence, causal graphs,
discussions and datasets are absent from the target. None should be populated
from the generic parent's microbial-treatment graph or from the small triad
subset. No gene, locus, regulator or expression claim makes iModulonDB
applicable. A seeded record need not have every optional field or an ITEM
decision to avoid a demonstrated defect.

Ignored-inclusive ID, mint, label/stem, full-path and node searches covered
curation, all raw inventories, PATHS/RETIRED, history, research, configuration
and individual reports. No target-owned decision, definition, parent exclusion,
causal overlay, research dossier, session history or earlier individual target
report was found within those bounds. Child-specific parent exclusions and
other wastewater research are not decisions about this target. Structured
exact-field/pipe-member scanning covered all 14 raw TSVs; it found no direct
target taxon or physicochemical parameter row.

## Findings

None found: zero blockers, zero major findings and zero minor findings in
the record's current assertions. This verdict does not certify the source
assignment of every original sample or resolve the two-sample pool context.
The unimported triad subset is an evidence limitation, not proof that the
record asserts a false pool identity or that all industrial wastewater has
those properties. Child records using this target as a parent require their
own assessments; their problems do not automatically invalidate this class.

## Recommended Edits

No scientific edit is established by this review. Preserve the identity,
definition, independent waste-water parent, node collapse, count/unit and
SEEDED lifecycle. Before any ITEM promotion or new ecological claim, recover
the original 252-organism crosswalk and the two triad-bearing sample records;
distinguish their contexts from the other memberships of the 26 studies.
Do not replace the identity with a swimming-pool term or import broad-parent
taxa/mechanisms to fill optional fields.

## Follow-up Checks

Any later identity assessment belongs in `curation/decisions.tsv` under
GOLD.229580fa29. Source-metadata corrections belong in the governed GOLD
extraction/inventory path, not generated YAML. Preserve separate organism,
biosample and study units in regressions. After authorized scientific edits,
append session history, dry-seed, inspect a target canary, and run strict,
history/provenance/label, corpus/site and full QC checks. Verify sample-level
triads before adopting them as claim-level evidence.

## Additional Notes

Only this new report was authored for this target; no scientific inputs,
generated artifacts, old reviews, history, status or GitHub state changed.
An inspected archived EPA industrial-wastewater-treatment page describes a
particular reporting category, not the original GOLD members or a universal
definition; it was not used to infer this record's industries or treatment.
A broader original-dump filename walk encountered a concurrently removed
external temporary worktree and ended with an error. No exhaustive original-
file absence claim is based on that walk. All current-state source absences
above are the bounded, completed content/table checks specified explicitly.
