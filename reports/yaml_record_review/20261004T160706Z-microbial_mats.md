# YAML Record Review: Microbial mats

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/microbial_mats.yaml`
- Started UTC: 2026-10-04T16:03:08Z
- Finished UTC: 2026-10-04T16:07:06Z
- Verdict: needs curation

## Target

Entire generated HabitatRecord habitatmech:GOLD.056292f510, Microbial mats,
AQUATIC, NARROW/REVIEWED. It contains two parents, one uncounted GOLD
attestation with skos:narrowMatch, an ITEM GROUND_AS_PARENT event and a seed
event. Definition, synonyms, taxa, parameters, citations/graphs, datasets,
discussions, xrefs and replacement links are not emitted.

The exact source is gold.ecosystem:8525,
`Environmental > Aquatic > Thermal springs > Near-boiling (>90C) > Microbial mats`.
The actual mint reproduces the identifier; PATHS.tsv:1308 pins the stem.
The unqualified filename and plural label do not identify all microbial mats.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/microbial_mats.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/microbial_mats.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Shared batch run PASS: 1,179 canonical pairs, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | Shared run PASS: 953 ungrounded records, 1,810 decisions. |
| `just qc` | Shared batch invocation observed terminal PASS. 457 tests passed, three skipped, two warnings in 736.65 seconds; all quality gates passed, including 90 history records, 3,206 strict records, 32 graph curations, reproduction and site checks. |
| Reference/source checks | Entire target and qualifier parent, both ITEM rows, all 14 raw TSVs, actual default plus decision-applied resolver, official mat ontology and actual semantic/page checks inspected. |

REVIEWED reflects decision coverage, not proof that every generated hierarchy
or mapping contract is correct.

## Identity and Grounding

`curation/decisions.tsv:129` is an ITEM GROUND_AS_PARENT decision, dated
2026-08-12, retaining this source mint beneath ENVO:01000008 microbial mat.
Its rationale distinguishes source settings rather than merging plural mat
labels into one ontology identity. Current [ENVO microbial mat](https://purl.obolibrary.org/obo/ENVO_01000008)
supports that generic structure parent. The derived-material class
ENVO:01000157 is not an automatic replacement identity.

The complete `near_boiling_90c__f7b76591.yaml` parent is
GOLD.8b53067bc5, Near-boiling (>90C), NOT_APPLICABLE/REVIEWED.
The ITEM row at `curation/decisions.tsv:817` explicitly identifies it as a
temperature band qualifying the spring, not a habitat. A microbial mat
cannot inherit this reviewed non-habitat qualifier as an is-a superclass.
The parent's separate hot-spring edge does not justify rewiring the mat
directly to a whole spring.

The target's REVIEWED state correctly follows its sole contributing ITEM
decision; its two history events are faithful. NARROW expresses the decision's
intended relation to the generic ontology parent, but conflicts with the
different source/identifier comparison declared in the shared schema.

## Evidence

Physical `data/raw/gold_ecosystem_paths.tsv:1582` contains the exact
depth-five path, one node and zero organism/study/biosample assertions.
The uncounted attestation is faithful. The qualifier parent's three ORGANISM
assertions and collapsed-node note do not belong to this child.

All 14 raw TSVs were scanned structurally. Only the exact tree row matched:
no target bulk sample, study, triad, parameter, PREGO or BacDive taxon row
was found. These bounded misses do not establish biological absence.
The source's >90C bucket is not a measured temperature for a recovered mat,
nor evidence for phototrophy or a particular organism's thermal tolerance.
The nearby Alkaline sibling's samples and triads must not be borrowed.

This is not the automatic singular-mat route. With the full mapping table
constructed by the seeder's normalization/setdefault rule, the actual default
resolver returns gold_unmatched, UNGROUNDED and no predicate. Applying the
maintained decisions via `apply_decision` returns
curated_ground_as_parent_from_gold_unmatched, NARROW, skos:narrowMatch,
ENVO:01000008 as extra parent and reviewed=True.

The relevant owner is the GROUND_AS_PARENT branch at
`src/habitatmech/seed.py:554-566`, applied during GOLD ingest at `:839-843`;
`:890-891` copies its locally generated predicate into the attestation.
The independent source-parent pass at `:898-907` adds the temperature qualifier.

SourceAttestation.mapping_predicate at
`src/habitatmech/schema/habitatmech.yaml:317-322` and GroundingStatusEnum
at `:776-790` describe source/record comparison. Here the record retains the
source path's own identity, while the decision compares that identity with
its generic ontology parent. The corresponding ontology target is explicit
in the maintained decision but not in the emitted attestation. This extends
#1398 to a curated route; it is not merely another automatic-leaf example.
A blind predicate reversal leaves the implicit attestation target wrong.
No formal SKOS inconsistency or downstream export failure is claimed.

Current OLS GOLD lookup for w3id.org/gold.path/8525 returned 404.
The committed node/path remain verified; original current contents were
not recovered and no source retirement is inferred.

## Completeness

Ignored-inclusive ID/key, node, path, label and filename searches covered
curation, history, research, individual reports, PATHS and RETIRED; an
additional ignored-inclusive filename inventory covered curation/history/
research/reports. They found both ITEM rows, path locks and sibling-review
mentions, but no target definition, overlay, dedicated research, separate
session history, retirement entry or prior individual target report.

The full `20260921T133058Z-alkaline__43fce277.md` sibling report was read.
Its recommendation to inspect this mat is not proof of a completed mat
review or scientific repair. Empty optional fields are not separate defects.
iModulonDB is not applicable: no gene, regulator, expression dataset or
mechanism is asserted. No SSSOM/KGX execution was performed here.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | The mat inherits an ITEM-rejected temperature qualifier as strict broader habitat. | GOLD source-parent pass, or governed exclusion for GOLD.056292f510 and expected parent GOLD.8b53067bc5. |
| Major | Curated GROUND_AS_PARENT emits NARROW/skos:narrowMatch using ontology-parent comparison endpoints inconsistent with the source/record field contracts. | `seed.py:554-566`, attestation emission and schema contracts; expand #1398 beyond its automatic-route witnesses. |

Counts: zero blockers, two major, zero minor. Retained identity, generic mat
parent, ITEM-derived REVIEWED status, source count omission and history are sound.

## Recommended Edits

1. Exclude this exact qualifier-parent contribution. Keep ENVO:01000008,
   source mint/path/node, existing ITEM decision/history and count omission.
   Do not replace the qualifier with a whole-hot-spring parent or turn its
   temperature bucket into an unsupported universal measured parameter.
2. Reconcile #1398 across automatic and curated routes with explicit endpoints
   and coherent grounding semantics. Preserve the decision's legitimate
   generic mat placement; do not merge all source contexts or erase review history.
3. Add qualifier-edge and curated-route endpoint regressions, append required
   correction history and inspect guarded regeneration. Future authored
   definitions belong in maintained term requests after evidence review.

## Follow-up Checks

Require schema, labels, provenance/history, exact corpus reproduction,
curated mapping-consumer regressions and full QC. Inspect the generated
REVIEWED status and both history events after a correction.

The complete page currently displays Near-boiling (>90C) and microbial mat
as Broader habitats. An actual full-context adapter comparison removing
only the qualifier drops `broader habitat: Near-boiling (>90C)` and needs
the real map/site rebuild in #1217. Predicate-only omission is text-neutral;
do not impose that runtime blocker on every contract-only fix. Preserve
protected draft #1218 and runtime pins.

## Additional Notes

All-state exact target/parent, Near-boiling and temperature-band searches
returned no matching issue. A broader NOT_APPLICABLE/parent search found
#1233; its full body/empty comments address Hot (42-90C) -> hot spring and
explicitly require separate incoming-child review. It is not this mat's
qualifier edge. Extend the mat-context hierarchy issue #1397 with this
distinct qualifier case and #1398 with the independently executed curated route.

Official typed ENVO OWL inspected this batch has SHA-256
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No scientific edit, status promotion, paid research or history rewrite occurred.
