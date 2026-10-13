# YAML Record Review: Mixolimnion/Top layer

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/mixolimnion_top_layer.yaml`
- Started UTC: 2026-10-04T19:17:54Z
- Finished UTC: 2026-10-04T19:20:20Z
- Verdict: needs curation

## Target

Entire generated HabitatRecord habitatmech:GOLD.58a0fb1252,
Mixolimnion/Top layer, AQUATIC, UNGROUNDED/SEEDED. One parent, one uncounted
GOLD attestation without mapping predicate and two events are present.
Definition, synonyms, xrefs, parameters, taxa, evidence, causal graphs,
discussions and datasets are not emitted.

Exact source: gold.ecosystem:8540,
`Environmental > Aquatic > Freshwater > Meromictic lake > Mixolimnion/Top layer`.
The actual mint matches; `PATHS.tsv:1938` pins the stem. This is the layer,
not the whole meromictic lake or a generic top layer outside that context.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/mixolimnion_top_layer.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/mixolimnion_top_layer.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Fresh shared PASS: 1,179 canonical, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | PASS: 953 ungrounded records, 1,810 decisions. |
| `just qc` | Active in final corpus report. Tests: 457 passed, three skipped, two warnings in 558.32s; history, strict schema, graph curations, exact reproduction, site and preceding gates passed. No terminal result claimed. |
| Source/reference checks | Full target and lake parent, earlier parent report and related issue, maintained rows, all 14 raw tables, actual resolver, typed official ENVO/current OLS, GOLD node attempt, inspected primary article and full page/semantic comparisons. |

Later QC completion belongs in the publication receipt. No SSSOM/KGX export
execution, compatibility audit or observed downstream failure is claimed.

## Identity and Grounding

`curation/decisions.tsv:552` is CLASS CONFIRM_UNGROUNDED dated 2026-08-12.
Its rationale did not assess habitat meaning. Actual full normalized-table
resolution gives gold_unmatched/UNGROUNDED/no predicate; application gives
curated_confirm_ungrounded_from_gold_unmatched, reviewed=False, no extra
parent. SEEDED and the two events are faithful to that limited decision.

Current [ENVO:00000199 meromictic lake](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000199)
is a whole lake with non-intermixing water layers. Typed OWL places its
definition in IAO:0000115 and lake as its named parent. OLS instead exposes
an explanatory comment about bottom oxygen and sediment organisms as its
description. That commentary is not adopted as a universal biological claim.

A mixolimnion is a layer within a meromictic lake, not a kind of whole lake.
Current [ENVO:01000283 lake layer](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000283)
is the appropriate broader genus to consider. Its typed OWL distinguishes
named superclass edges from a separate part-of-lake restriction. That
restriction does not authorize an is-a edge to lake. Vendored row 7786
agrees with the layer definition.

The inspected [Storesund et al. primary article](https://pmc.ncbi.nlm.nih.gov/articles/PMC7464441/)
defines mixolimnion as the upper circulating water masses and monimolimnion
as the deep, persistently separated waters. Its introduction distinguishes
these from thermal-layer terminology. The studied Norwegian lake is
brackish/saline; it supplies terminology, not evidence that this Freshwater
GOLD bin has the same salinity, organisms, depths or interventions.

ENVO:00002131 epilimnion defines the upper layer of a thermally stratified
lake. Its typed part-of-meromictic-lake restriction is not proof that every
mixolimnion is an epilimnion, and the shared top-layer wording does not
establish exact equivalence. The inspected evidence distinguishes circulation
and thermal roles; retain the source-specific identity while evaluating an
exact term, rather than making an unproved epilimnion match.

The full parent `meromictic_lake.yaml` and its earlier individual report
were read. Its two sources, PREGO taxon and review events belong to the
whole lake. Its separately reported fresh-water-material parent defect
does not repair this incoming layer-to-whole edge and supplies no taxon
or mechanism evidence for the mixolimnion.

## Evidence

Physical `gold_ecosystem_paths.tsv:1482` gives the exact depth-five path,
node 8540, zero organism/study/biosample counters and total zero. Count/unit
omission is correct, not biological absence. The complete 14-table scan
with exact path equality and pipe membership found no target bulk samples,
API triads, study memberships, environmental parameters, PREGO or BacDive
taxon rows. No sample-level temperature, oxygen or salinity is established.

Current official GOLD vocabulary lookup for node 8540 returned 404. The
committed path is verified; current original contents were not recovered,
and retirement is not inferred. No original study URL is supplied for this
source in the inspected inventory. General meromictic-lake literature cannot
fill an exact-source cohort that has not been recovered.

The false whole-lake parent is contributed independently by the GOLD
parent pass at `seed.py:898-907`. No mapping predicate is currently emitted;
the source retains its identity, so the current attestation does not reproduce
#1398. Future GROUND_AS_PARENT curation must reconcile that affected route's
endpoint/status contract rather than silently introducing the known defect.

## Completeness

Ignored-inclusive exact ID/node, label and stem searches covered curation,
history, research, reports, conf, PATHS and RETIRED, with filename inventory.
They found the CLASS decision and path lock, not a target definition, overlay,
dedicated research, session history, retirement or prior individual review.
The parent report's child mention is not this record's review.

Ignored-inclusive term/request searches found no mixolimnion or monimolimnion
identity in the vendored tables, but did find lake layer and thermal-layer
near misses. This is bounded, not global ontology absence. Before any novel
request, check current exact-term availability and define the circulation
scope. Empty optional taxa/parameters/graphs are appropriate; iModulonDB is
inapplicable without a gene/regulator/expression claim.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | A lake layer inherits the containing whole meromictic lake as a strict broader habitat. | Governed exclusion for GOLD.58a0fb1252 and expected parent ENVO:00000199, or GOLD parent pass in src/habitatmech/seed.py; coordinate #1245. |
| Major | The source remains CLASS/UNGROUNDED although a supported lake-layer genus is available. | ITEM curation in curation/decisions.tsv and any supported, deduplicated definition in curation/term_requests.tsv. |

Counts: zero blockers, two major, zero minor. Source identity, count omission
and status/history derivation are faithful. Sparse optional fields and the
unresolved exact epilimnion relation are not additional confirmed defects.

## Recommended Edits

1. Remove only the false whole-lake parent contribution through maintained
   inputs, preserving the lake context in provenance or a justified relation.
2. Replace the CLASS decision with evidence-backed ITEM curation beneath
   verified lake layer unless an exact mixolimnion term is established.
   Preserve Freshwater/meromictic/circulating-layer scope; do not merge with
   generic epilimnion on top-layer wording alone.
3. Add a deduplicated definition if needed, with parent-mode evidence. The
   sole inherited parent is false, so any REPLACE rationale must state that
   specific fact. Reconcile future mapping semantics with #1398.
4. Add exact-edge, source-preservation and endpoint regressions, append
   required new history and regenerate through maintained inputs only.

## Follow-up Checks

After correction run `just seed`, then
`just seed-canary habitatmech:GOLD.58a0fb1252 --force`. Inspect the entire
canary, absent whole-lake edge, selected genus, exact source provenance,
count omission and genuine new ITEM history before `just seed-apply --force`.
Never prune partial runs. These are future commands, not review actions.

Require ordinary/strict validation, labels, history/source/consumer tests,
exact corpus reproduction and full QC. The full page shows meromictic lake
as Broader habitat. Separately executed whole-lake removal and lake-layer
addition both change actual semantic text. Scientific correction needs
genuine map/site refresh under #1217; protect #1218/runtime pins and audit
actual SSSOM/KGX products before compatibility claims.

## Additional Notes

All-state mixolimnion and exact-source issue searches returned no matches.
The full #1245 body/comments cover six other independently verified hierarchy
witnesses, including hypolimnion and metalimnion. Extend it with this distinct
source, while tracking the additional grounding gap explicitly. Report
publication implements neither scientific repair.

The attempted USGS Big Soda Lake publication page returned 403; its search
snippet was not used as inspected primary evidence. Official typed ENVO OWL
SHA-256: `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No scientific input, generated product, old report/history or paid research changed.
