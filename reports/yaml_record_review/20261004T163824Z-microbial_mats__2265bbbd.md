# YAML Record Review: Microbial mats

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/microbial_mats__2265bbbd.yaml`
- Started UTC: 2026-10-04T16:35:41Z
- Finished UTC: 2026-10-04T16:38:24Z
- Verdict: needs curation

## Target

Entire generated HabitatRecord habitatmech:GOLD.b76e4c6e4a, Microbial mats,
AQUATIC, NARROW/REVIEWED. Two parents, one uncounted GOLD attestation with
skos:narrowMatch, one ITEM GROUND_AS_PARENT event and one seed event are
present. Definition, synonyms, taxa, parameters, citations, graphs, datasets,
discussions, xrefs and replacement links are not emitted.

The source is gold.ecosystem:8539,
`Environmental > Aquatic > Freshwater > Meromictic lake > Microbial mats`.
The actual mint reproduces this identifier; PATHS.tsv:2634 pins the stem.
This review concerns that lake-specific mat, not the whole meromictic lake.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/microbial_mats__2265bbbd.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/microbial_mats__2265bbbd.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Shared batch run PASS: 1,179 canonical pairs, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | PASS: 953 ungrounded records, 1,810 decisions. |
| `just qc` | Fresh authorized batch invocation is active in tests; lint, documentation and raw provenance passed. No terminal result claimed. |
| Source/reference checks | Full target and ITEM row, structured scan of all 14 raw TSVs, actual default/decision-applied resolver, official typed OWL/current OLS and actual page/semantic comparisons inspected. |

The first diagnostic invocation failed at shell quoting before executing;
the corrected read-only invocation completed successfully. Later full-QC
results belong in the publication receipt, not this completion-time observation.

## Identity and Grounding

The ITEM row at `curation/decisions.tsv:1034`, dated 2026-08-12, retains
this source identity beneath ENVO:01000008 microbial mat. Its single source
is ITEM-reviewed, so REVIEWED and the two history events are faithful.
The generic mat parent is supported; ENVO:01000157 is instead material
derived from a mat, not an automatic identity replacement.

Current [ENVO:00000199 meromictic lake](https://purl.obolibrary.org/obo/ENVO_00000199)
is active. Official typed OWL defines a lake with non-intermixing water
layers and supplies lake, ENVO:00000020, as its named parent. OLS exposes
an explanatory comment in its description field; this is not the typed
definition. Neither that comment's generalization about bottom organisms
nor lake stratification establishes a property of this particular mat.
A mat situated in the lake is not itself a kind of whole lake.

NARROW follows the maintained decision's generic-ontology comparison, but
the schema describes a source/record comparison. This is distinct from
the false lake parent and does not invalidate the retained mat identity.

## Evidence

Physical `data/raw/gold_ecosystem_paths.tsv:1481` contains the exact
depth-five path, one source node and zero organism/study/biosample assertions.
Count omission is faithful to the positive-organism-only emission rule.
The complete 14-table scan found no exact-target bulk sample, study, triad,
parameter, PREGO or BacDive taxon row. These bounded misses do not establish
biological absence or justify importing the parent lake's taxon association.

With the full normalized mapping table constructed using the seeder's
setdefault rule, actual default resolution is gold_unmatched/UNGROUNDED,
without a predicate. Actual `apply_decision` returns
curated_ground_as_parent_from_gold_unmatched, NARROW, skos:narrowMatch,
extra parent ENVO:01000008 and reviewed=True. This is not the automatic
singular-leaf route. The owner is `src/habitatmech/seed.py:554-566`, applied
at `:839-843`; `:890-891` emits its predicate and `:898-907` separately adds
the lake context parent.

SourceAttestation.mapping_predicate at
`src/habitatmech/schema/habitatmech.yaml:317-322` and GroundingStatusEnum
at `:776-790` compare source and generated identifier. The mint retains
the source identity, while the decision compares it with the ontology
parent. That ontology endpoint is explicit in the decision, not the emitted
attestation. This independently reproduces #1398; it is not a formal SKOS
inconsistency or a reason to reverse predicates without fixing endpoints.

Current official OLS GOLD lookup for w3id.org/gold.path/8539 returned 404.
The committed source is verified; current original contents were not
recovered, and no retirement inference is made.

## Completeness

Ignored-inclusive exact ID/key, node, path and stem searches covered
curation, history, research, individual reports, PATHS and RETIRED. A separate
ignored-inclusive filename inventory and meromictic-label search found the
parent report; generic plural-mat searches found unrelated research leads.
No target-owned definition, overlay, dedicated research, separate session
history, retirement entry or previous individual target report was found.
The ITEM row and path lock are present. Generic leads were not used as
source-specific evidence.

The full parent report `20261004T142143Z-meromictic_lake.md` was read as
context. Its whole-lake/fresh-water defect and parent-level PREGO strain
evidence do not resolve or support this child's mat-to-lake edge. Empty
optional fields are not additional defects. iModulonDB is not applicable:
no gene, regulator, expression dataset or mechanism is asserted.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | The meromictic-lake mat inherits a whole lake as strict broader identity. | GOLD parent-path pass, or governed exclusion for GOLD.b76e4c6e4a and expected parent ENVO:00000199. |
| Major | Curated NARROW/skos:narrowMatch use ontology-parent endpoints inconsistent with source/record field contracts. | GROUND_AS_PARENT resolver, attestation emitter and schema contracts, #1398. |

Counts: zero blockers, two major, zero minor. The mat identity, generic
parent, ITEM-derived REVIEWED state, count omission and history remain sound.

## Recommended Edits

1. Exclude only the lake context-parent contribution. Preserve ENVO:01000008,
   the exact source mint/path/node, count omission and ITEM decision/history.
   Do not borrow the parent lake's strain association or sediment commentary.
2. Reconcile #1398 across curated and automatic routes with explicit endpoints
   and coherent status meaning; do not merge mat contexts or blindly reverse
   predicates. Preserve legitimate imported mappings.
3. Add exact-edge/source-preservation and curated-route contract regressions,
   append required correction history and inspect guarded regeneration.
   Scientific input changes belong upstream, not in generated YAML or pages.

## Follow-up Checks

Require ordinary/strict schema, labels, source/history checks, full corpus
reproduction, mapping-consumer tests and full QC. Reinspect the entire
generated target, REVIEWED state and both events after correction.

The complete page lists meromictic lake and microbial mat as Broader habitats.
An actual full-context semantic comparison excluding only the lake removes
`broader habitat: meromictic lake`; the hierarchy correction requires the
real map/site refresh in #1217. Predicate-only omission is text-neutral,
so not every contract fix needs inference. Protect draft #1218 and runtime
pins. No downstream SSSOM/KGX execution or compatibility verdict is claimed.

## Additional Notes

All-state exact-key and meromictic/mat issue searches returned no match.
Extend the independently verified witness sets of #1397 and #1398; the
parent lake's #1220 follow-up is a different whole-to-material relationship.
Report publication does not implement or close either scientific correction.

Official typed ENVO OWL inspected has SHA-256
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
The web viewer failed, but direct official OLS requests succeeded for the
three ontology classes. No scientific edit, status promotion, paid research
or history rewrite occurred.
