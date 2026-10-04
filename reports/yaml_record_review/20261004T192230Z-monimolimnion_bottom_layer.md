# YAML Record Review: Monimolimnion/Bottom layer

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/monimolimnion_bottom_layer.yaml`
- Started UTC: 2026-10-04T19:21:12Z
- Finished UTC: 2026-10-04T19:22:30Z
- Verdict: needs curation

## Target

Entire generated HabitatRecord habitatmech:GOLD.e070d4c2be,
Monimolimnion/Bottom layer, AQUATIC, UNGROUNDED/SEEDED. One parent, one
uncounted GOLD attestation without mapping predicate and two events are
present. Definition, synonyms, xrefs, parameters, taxa, evidence, graphs,
discussions and datasets are not emitted.

Exact source: gold.ecosystem:8541,
`Environmental > Aquatic > Freshwater > Meromictic lake > Monimolimnion/Bottom layer`.
The actual mint matches; `PATHS.tsv:2959` pins the stem. This is the
bottom water layer, not lake-bottom sediment or the whole meromictic lake.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/monimolimnion_bottom_layer.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/monimolimnion_bottom_layer.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Fresh shared PASS: 1,179 canonical, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | PASS: 953 ungrounded records, 1,810 decisions. |
| `just qc` | Terminal PASS: 457 tests passed, three skipped, two warnings in 558.32s; history, all 3,206 strict records, 32 graph curations, exact reproduction and all remaining site/redirect/term-request/QC gates passed. |
| Source/reference checks | Full target, maintained rows, all 14 raw tables, actual resolver, fresh typed official ENVO/OLS and GOLD lookup, shared fully read lake parent/report, inspected primary terminology source and full page/semantic comparisons. |

Identifier-label validation is not an SSSOM/KGX modeling audit. No downstream
export execution, compatibility certification or observed export failure is claimed.

## Identity and Grounding

`curation/decisions.tsv:1244` is CLASS CONFIRM_UNGROUNDED dated 2026-08-12.
The note leaves habitat meaning unassessed. Actual full normalized-table
resolution gives gold_unmatched/UNGROUNDED/no predicate; applying the row
gives curated_confirm_ungrounded_from_gold_unmatched, reviewed=False and no
extra parent. The two events and SEEDED status are faithful to that limited row.

Current [ENVO:00000199 meromictic lake](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000199)
denotes a whole lake with non-intermixing water layers. Its typed definition
and lake superclass are distinct from OLS's exposed explanatory comment
about oxygen and bottom organisms. Do not import that comment as a universal
anoxia claim, or as evidence that this layer lacks microorganisms.

Current [ENVO:01000283 lake layer](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000283)
defines a layer that is part of a lake. Typed OWL separately represents its
named superclasses and part-of-lake restriction. It supplies a supported
broader genus for this layer; the part relation is not an is-a relation to
the whole lake. The current sole parent ENVO:00000199 is therefore false.

The [Storesund et al. primary article](https://pmc.ncbi.nlm.nih.gov/articles/PMC7464441/),
inspected in the preceding individual review in this batch, distinguishes
deep monimolimnetic waters from the circulating upper mixolimnion. Its
Norwegian study concerns a brackish/saline lake, not an identified member
of this Freshwater GOLD bin. Neither its organism distribution nor its
depths, chemistry and lake-management history are universal target evidence.

Fresh current ENVO:00002130 hypolimnion describes the dense bottom layer
below a thermocline in a thermally stratified lake. Its named parent is
lake layer, with a separate part-of-meromictic-lake restriction. Shared
bottom-layer position and that restriction do not establish exact synonymy
with monimolimnion, whose distinction concerns persistent separation from
the circulating layer. No automatic hypolimnion match is justified by the
inspected evidence; preserve this source-specific identity while investigating.

The complete generated lake parent and its earlier report were read in the
preceding review. Its GOLD/PREGO attestations, taxon and actual ITEM history
belong to the whole lake and must not be copied to this layer. Repairing the
lake's own false fresh-water-material parent does not repair this incoming
layer-to-whole edge.

## Evidence

Physical `gold_ecosystem_paths.tsv:1483` gives the exact depth-five path,
node 8541, zero organism/study/biosample counters and total zero. Omitted
count/unit is faithful, not evidence of biological absence. The independent
complete 14-table scan used exact path equality and pipe membership and found
no target bulk samples, API triads, study memberships, parameters, PREGO or
BacDive taxon rows. No exact-source experiment or quantitative oxygen,
temperature, salinity or sulfide range is established.

Current official GOLD vocabulary lookup for node 8541 returned 404. The
committed source is verified; current original contents were not recovered,
and the response does not prove retirement. No original study URL is supplied
by the inspected exact-source inventory.

`seed.py:898-907` adds the whole meromictic-lake parent independently of
the CLASS decision. No current mapping predicate is emitted, consistent with
retained source identity. #1398 is not a current attestation finding here;
future GROUND_AS_PARENT curation must reconcile its affected endpoint/status
contract instead of introducing that known defect unnoticed.

## Completeness

Ignored-inclusive exact ID/node, label and stem searches covered curation,
history, research, reports, conf, PATHS and RETIRED, plus filename inventory.
They found the decision and path lock, not a target-owned definition, overlay,
dedicated research, session history, retirement or earlier individual review.
Parent, hypolimnion and newly written mixolimnion mentions are context, not
this record's prior review or exact-source primary evidence.

Ignored-inclusive term/request searches found no monimolimnion identity in
the vendored tables; lake layer and hypolimnion were inspected as candidates.
This is not global ontology absence. Deduplicate current exact terms before
requesting a new definition. Empty optional fields are appropriate without
claim-specific evidence. iModulonDB is inapplicable without a gene, regulator
or expression claim.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | The bottom lake layer is emitted as a kind of whole meromictic lake. | Governed exclusion for GOLD.e070d4c2be and expected parent ENVO:00000199, or GOLD parent pass in src/habitatmech/seed.py; coordinate #1245. |
| Major | The source remains CLASS/UNGROUNDED although a defensible lake-layer genus exists. | ITEM curation in curation/decisions.tsv and any supported, deduplicated definition in curation/term_requests.tsv. |

Counts: zero blockers, two major, zero minor. Source identity, count omission
and generated status/history are faithful. The unresolved exact hypolimnion
relation is not an additional confirmed defect.

## Recommended Edits

1. Suppress only the false whole-lake parent contribution through maintained
   inputs, preserving lake context in provenance or a justified relation.
2. Replace the CLASS row with evidence-backed ITEM curation beneath verified
   lake layer unless a current exact monimolimnion term is established.
   Preserve Freshwater/meromictic/bottom-layer scope; do not exact-merge into
   hypolimnion, whole lake, sediment, or an anoxic-water material by analogy.
3. Add a deduplicated definition if needed. Any REPLACE mode must document
   that the sole inherited parent is false, not merely prefer a different
   genus. Coordinate future mapping semantics with #1398.
4. Add exact-source/edge/endpoint regressions, required new history and
   governed regeneration. Never edit generated YAML or previous history.

## Follow-up Checks

After correction run `just seed`, then
`just seed-canary habitatmech:GOLD.e070d4c2be --force`. Inspect the complete
canary, absent whole-lake edge, selected genus, intact source provenance,
count omission and genuine new ITEM history before `just seed-apply --force`.
Never prune partial runs. These are future curation commands, not review edits.

Require ordinary/strict validation, labels, history/source/consumer regressions,
exact reproduction and full QC. The complete page shows the whole lake as
Broader habitat. Independently executed whole-lake removal and lake-layer
addition both change actual semantic text, requiring genuine map/site refresh
under #1217. Preserve #1218/runtime pins and inspect actual SSSOM/KGX output
before compatibility claims.

## Additional Notes

All-state monimolimnion and exact-key issue searches returned no matches.
The already inspected #1245 body/comments cover other lake-layer hierarchy
witnesses; extend them with this exact source, while explicitly tracking
the additional grounding gap. Publication implements neither scientific repair.
Official typed ENVO OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No scientific input, generated product, old report/history or paid research changed.
