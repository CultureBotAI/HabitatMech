# YAML Record Review: Microbial mats

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/microbial_mats__d16dafc1.yaml`
- Started UTC: 2026-10-04T18:02:33Z
- Finished UTC: 2026-10-04T18:07:35Z
- Verdict: needs curation

## Target

Entire generated HabitatRecord habitatmech:GOLD.c8481605f8, Microbial mats,
AQUATIC, NARROW/REVIEWED. Two parents, one uncounted GOLD attestation with
skos:narrowMatch and two history events are present. Definition, synonyms,
xrefs, parameters, taxa, citations, graphs, discussions, datasets and
replacement links are not emitted.

The exact source is gold.ecosystem:7894,
`Environmental > Aquatic > Non-marine Saline and Alkaline > Hypersaline lake > Microbial mats`.
The actual mint matches; PATHS.tsv:2756 pins the stem. This is the mat,
not the whole hypersaline lake, its microbialite sibling, or the mat under
the separate Hypersaline water environment source path.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/microbial_mats__d16dafc1.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/microbial_mats__d16dafc1.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Shared fresh run PASS: 1,179 canonical pairs, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | PASS: 953 ungrounded records, 1,810 decisions. |
| `just qc` | Terminal PASS: 457 tests, three skipped, two warnings in 763.06 seconds; 90 history records, 3,206 strict records, 32 graph curations, exact reproduction and all site/redirect/term-request and remaining gates passed. |
| Source/reference checks | Full target, maintained row, all 14 raw tables, actual resolver, typed OWL/current OLS and complete page/semantic comparisons inspected. |

The final target's validator and diagnostic output was truncated by the
tool context. No matching process remained; those checks were rerun and
their terminal results inspected before this report. No export execution
or SSSOM/KGX compatibility certification is claimed.

## Identity and Grounding

The genuine ITEM decision at `curation/decisions.tsv:1113`, dated
2026-08-12, uses GROUND_AS_PARENT with ENVO:01000008 microbial mat.
The retained minted identity, generic mat parent, REVIEWED state and two
events reproduce that decision. The batch's official ENVO inspection
distinguishes the layered microbial structure ENVO:01000008 from material
derived from it, ENVO:01000157; the latter is not an identity substitute.

Current official [ENVO:01001020 hypersaline lake](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001020)
is active and denotes a lake whose water is saltier than ocean water. Typed
OWL makes it a subclass of saline lake, with a hypersaline-water composition
restriction. A mat occurring in that lake is not itself a kind of whole lake.
This is a confirmed false strict parent, unlike the separately reviewed,
potentially broader environmental-system interpretation of ENVO:01001043.
No lake-wide salinity measurement or threshold is asserted for this mat.

## Evidence

Physical `gold_ecosystem_paths.tsv:1562` gives the exact depth-five path,
one node, zero organism/study/biosample counters and zero total assertions.
Omitting assertion_count and assertion_unit is faithful; it does not assert
that the habitat is biologically empty. The complete 14-table scan found no
exact-target bulk samples, API triads, study memberships, parameters, PREGO
or BacDive taxa. These are bounded snapshot misses, not biological absence.

Current official GOLD vocabulary lookup for w3id.org/gold.path/7894 returned
404. The committed source is verified, but current original node contents
were not recovered. The 404 does not prove retirement. No direct organism
or quantitative environmental evidence is inferred from the source label.

The actual default resolver with the complete normalized mapping table gives
gold_unmatched/UNGROUNDED/no predicate. Applying the maintained ITEM row
yields curated_ground_as_parent_from_gold_unmatched, NARROW,
skos:narrowMatch, extra parent ENVO:01000008 and reviewed=True.
`seed.py:554-566` owns that route, applied at `:839-843`. The separate GOLD
parent pass at `:898-907` adds the false whole-lake parent.

Predicate emission at `:890-891` reproduces #1398: schema
`habitatmech.yaml:317-322` and `:776-790` declare source/record comparisons,
but this decision compares the retained identity with an ontology parent
not represented as the attestation's target. Reversing the predicate alone
does not reconcile the endpoints. No formal SKOS inconsistency is asserted.

## Completeness

Ignored-inclusive ID/key, stem, source-node/path and hypersaline-lake label
searches covered curation, history, research, reports, PATHS and RETIRED.
A separate filename inventory found adjacent lake reports, not a
target-owned definition, overlay, dedicated research, session history,
retirement or prior individual mat review. The ITEM decision and path lock
are present. Broader inland-saline research and other lake/mat reports are
leads, not primary evidence for this exact source. No full parent-record
review or transfer of its organism cohort is claimed here.

Optional omissions are not defects. iModulonDB is inapplicable without a
gene, regulator or expression dataset claim.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | The hypersaline-lake mat inherits the whole lake as a strict broader identity. | GOLD parent pass or governed exclusion for GOLD.c8481605f8 and expected parent ENVO:01001020, #1397. |
| Major | Curated NARROW/skos:narrowMatch use ontology-parent endpoints rather than the declared source/record comparison. | Resolver, attestation emitter, schema and consumers, #1398. |

Counts: zero blockers, two major, zero minor. Mat identity, true generic
parent, count omission, ITEM review and event derivation remain sound.

## Recommended Edits

1. Suppress only the whole-lake parent contribution. Preserve ENVO:01000008,
   source identity/path/node, faithful uncounted attestation and review history.
2. Reconcile endpoint and grounding semantics across actual routes,
   preserving legitimate mappings and distinct source mat identities.
3. Add exact-edge/source-preservation and endpoint regressions, append
   required correction history and regenerate from maintained inputs.

## Follow-up Checks

After correction run `just seed`, then
`just seed-canary habitatmech:GOLD.c8481605f8 --force`. Inspect the complete
canary, absent count/unit, true mat parent, REVIEWED derivation and prior
events plus required correction history before `just seed-apply --force`.
Do not prune partial runs. These commands describe future curation, not edits
performed by this review.

Require ordinary/strict schema, labels, source/history and mapping-consumer
checks, `just verify-corpus` and `just qc`. The complete page lists the lake
under Broader habitats. Removing only that parent in the full-context
semantic adapter removes `broader habitat: hypersaline lake`; scientific
repair needs genuine map/site refresh under #1217. Predicate-only omission
was separately text-neutral. Protect #1218/runtime pins and inspect actual
SSSOM/KGX output before claiming compatibility.

## Additional Notes

The all-state exact-source issue search returned no matches; the broader
hypersaline-lake/mat search returned #1397 and #1398. Extend those issues
with this independently verified witness rather than duplicating them.

The maintained rationale's Path fragment ends at `Mi`. The full attestation
path and keyed ITEM target are intact; the event copies maintained text
verbatim, not a serializer truncation. Official typed ENVO OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No scientific data, prior report/history or paid research changed.
