# YAML Record Review: Hospital bedroom

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/hospital_bedroom.yaml`
- Started UTC: 2026-10-08T18:35:18Z
- Finished UTC: 2026-10-08T18:37:24Z
- Verdict: needs curation (0 blocker, 1 major, 0 minor)

## Target

Read the complete generated HabitatRecord `habitatmech:GOLD.9cc7667041`,
Hospital bedroom, ENGINEERED / UNGROUNDED / SEEDED. One GOLD source,
one parent and two history events; no definition or additional claims.
Baseline: 2058819d402cf5e464d09615f5fe464ec1f48ed4. Hospital was fully read
in this session; the complete Room surface child was read as context only.

## Validation

- `UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/hospital_bedroom.yaml`:
  passed, no issues.
- `UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/hospital_bedroom.yaml`:
  passed, one file, zero errors.
- Fresh full-corpus construction reproduces the entire parsed target exactly:
  one source, zero reviewed contributors, no authored definition or exclusion.
  Default/applied target resolution used complete ontology/mapping/claimant
  indexes. The same-turn actual Hospital parent resolution is reused.
- Reused full QC from the unchanged scientific baseline, not a new full run:
  PR #1742 head/queue QC, labels and vendored checks passed; 595 tests passed,
  three skipped, 197 histories valid and 3,207 records reproduced.
  Fresh same-turn comparison confirms baseline/reviewed-tree equality.
  [Receipt](https://github.com/CultureBotAI/HabitatMech/pull/1742#issuecomment-6066368637).
- Direct ENVO checks below verify the parent and candidates. No graph/literature
  references or target session histories need a separate focused validator.
  Original GOLD joins and SSSOM/KGX compatibility were not verified.

## Identity and Grounding

The full source path `Engineered > Built environment > Hospital > Hospital bedroom`
mints the recorded ID and agrees with `PATHS.tsv:2454`. Default `gold_unmatched`
becomes `curated_confirm_ungrounded_from_gold_unmatched` through the CLASS
CONFIRM_UNGROUNDED decision at `curation/decisions.tsv:910`, without a mapping
predicate. The sampling sidecar at
`curation/samples/class_swept_unscreened-20260814.tsv:23` calls it a habitat;
that sidecar is not an ITEM decision or an identity/parent assessment. SEEDED
correctly reflects the maintained input, not completed individual curation.

The source names a room within a hospital. Its sole parent `ENVO:00002173`
is the hospital building identity, supplied by GOLD containment. The target
has no ontology, ambiguous-leaf or authored-definition parent contribution.
A room is part of a building, not a subtype of the whole hospital.

A complete local label/synonym scan found `ENVO:03501180` patient room and
`ENVO:01000426` room. The former includes care during a visit or stay in any
healthcare facility, not just a hospital bedroom. Critically, the pinned OWL
types patient bed room and examination room as narrow synonyms, while the
vendored TSV flattens their scopes. Their presence is not an exact grounding
license. A room parent is supported by the source meaning; a more specific
patient-room relation needs source-role assessment before an ITEM decision.

## Evidence

- `gold_ecosystem_paths.tsv:1262` contains node 5489 and all-zero direct
  organism/study/biosample/total counters. Count/unit omission is correct.
- The same-turn inspected [GOLD workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths)
  row 197 contains node 5490 under Hospital bedroom > Room surface. It confirms
  the intermediate path, not an independent direct bedroom count or historical
  join for node 5489. SHA256
  `f8e4cb5cf89ecc88d3cf28170cfc3a1cf47daed8218408a52914c53667dfd3d4`,
  84,174 bytes; worksheet dimensions were reset before iteration.
- Fresh [GOLD organism-tree JSON](https://gold.jgi.doe.gov/download?mode=organismEcosystemsJson)
  contains this exact bedroom node and Room surface child, both count zero.
  SHA256 `49ef0a3e654a79f6b7e7140d2cdb2ac0ce0bb1df2ccb8decae68d129eeb7ca11`,
  1,450,415 bytes. This is classification, not absence of microbes or samples.
- Fresh [pinned ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
  confirms hospital as a building, room as a building part and patient room as
  a room subclass with a part-of restriction to healthcare facility. It also
  supplies the typed narrow synonyms discussed above. SHA256
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`,
  9,614,229 bytes. None of these axioms makes a patient room a kind of hospital.

The Room surface child owns 1,660 BIOSAMPLE observations at
`gold_path_biosamples.tsv:19`. Its study is Gs0153813 at `gold_studies.tsv:3726`.
Child triads at rows 65-67 use anthropogenic terrestrial biome (broad), room
(local) and building floor (medium), one distinct term per slot with frequency
1.00 in that aggregation. These slot-specific values are not bedroom identity,
floor equivalence or quantitative room conditions. The original study page
was inaccessible through the web tool; its sample membership was not independently
recovered. No child count or triad is copied into the parent.

## Completeness

Ignored-inclusive searches for ID, label, stem, node and path covered all raw
inventories, curation, configuration, docs, tests, PATHS/RETIRED, histories,
research, its manifest and individual reviews. Filename traversal covered
curation/history/research. Apart from the CLASS row and sampling sidecar,
no target-owned ITEM decision, definition, exclusion, overlay, session history,
research file or earlier individual report was found in those bounds.

Exact-field/pipe-member scanning of all raw TSVs found only the target and
child ecosystem rows when the level label was included. Child biosample,
study and triad rows were separately identified above; no direct target row
in those inventories was found. The same-turn ignored-inclusive original-GOLD
artifact search under build, data/raw and configured kg-microbe data was empty;
live classification cannot restore historical sample joins.

No optional synonym, xref, parameter, taxon, mechanism, evidence, discussion
or dataset needs invention. iModulonDB is not applicable without a gene,
regulator, strain-expression or transcriptomic assertion.

## Findings

1. **Major: hospital containment is emitted as a broader-habitat relation.**
   The only parent asserts that a hospital bedroom is a kind of hospital,
   contradicting the room-versus-building scope verified above. Owner:
   `curation/gold_parent_exclusions.tsv`, key `habitatmech:GOLD.9cc7667041`,
   exact source path above and expected parent `ENVO:00002173`. The separate
   Hospital review's BacDive merge blocker does not cause or resolve this
   room/building error, and is not counted again here.

## Recommended Edits

1. In authorized curation, exclude only the GOLD hospital-parent contribution.
   Preserve the mint, full path, source ID and zero-count omission. Do not
   replace the room with its building or transfer Room surface observations.
2. Assess `curation/decisions.tsv` for a supported broader room relation; retain
   the mint unless exact equivalence is proved. Patient room is a candidate,
   not an exact hospital-bedroom match merely because its flattened synonyms
   contain patient bed room. A novel definition, if justified, belongs in
   `curation/term_requests.tsv`; do not invent one just to suppress the edge.

## Follow-up Checks

Verify all parent contributors and unchanged source/child evidence before/after
any maintained-input change. Dry seed, inspect a target canary, append required
session history, then schema, label, provenance, full reproduction, map/site
freshness, redirects and full QC. Source-level patient/staff-room scope remains
to be recovered before a more specific identity decision or review promotion.

## Additional Notes

Only this new report was written. Scientific/generated inputs, old reports,
history, review status and GitHub remain unchanged. Context reads and the
earlier Hospital review do not count as additional record reviews.
