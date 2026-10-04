# YAML Record Review: Microbial mats

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/microbial_mats__91e1bc3c.yaml`
- Started UTC: 2026-10-04T17:39:40Z
- Finished UTC: 2026-10-04T17:43:09Z
- Verdict: needs curation

## Target

Entire generated HabitatRecord habitatmech:GOLD.df20aa5a67, Microbial mats,
AQUATIC, NARROW/REVIEWED. It has two parents, one GOLD attestation with nine
ORGANISM assertions and skos:narrowMatch, and two history events. Definition,
synonyms, xrefs, parameters, taxa, citations, graphs, discussions, datasets
and replacement links are not emitted.

The exact gold.ecosystem:3979 path is
`Environmental > Aquatic > Non-marine Saline and Alkaline > Hypersaline > Microbial mats`.
The actual mint matches; PATHS.tsv:2943 pins the stem. This is not the
separate Hypersaline lake mat or the parent environment's 219-organism cohort.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/microbial_mats__91e1bc3c.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/microbial_mats__91e1bc3c.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Shared fresh run PASS: 1,179 canonical pairs, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | PASS: 953 ungrounded records, 1,810 decisions. |
| `just qc` | Fresh batch run active in tests, beyond 62%; lint, documentation and raw provenance passed. No terminal result claimed. |
| Source/reference checks | Full target and parent, decision, all 14 raw tables, actual resolver, typed OWL/current OLS, prior parent report, issue scope and full page/semantic comparisons inspected. |

This records the observed completion-time state; later shared QC results
belong in the publication receipt. No downstream export run was performed.

## Identity and Grounding

`curation/decisions.tsv:1234` is a genuine ITEM GROUND_AS_PARENT decision
dated 2026-08-12 for ENVO:01000008 microbial mat. The retained source identity,
generic mat parent, REVIEWED status and two events follow this maintained row.
Current official ENVO distinguishes that layered structure from material
derived from it, ENVO:01000157. The latter is not an automatic identity substitute.

The second parent is [ENVO:01001043 hypersaline water environment](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001043).
Its typed OWL definition is an environmental system whose properties and
dynamics are determined by hypersaline water, not a whole lake, bare salinity
quality or the water material itself. Named parent ENVO:01000307 is saline
water environment; the OWL also has separate water-related restrictions.
Current ENVO:01000254 defines environmental system broadly, while microbial
mat is under ENVO:01000549 mass of biological material. These class descriptions
do not by themselves establish disjointness or prove that a hypersaline mat
can never function as a water-determined environmental system.

Consequently the whole-lake and qualifier arguments from adjacent mat reviews
do not establish a false edge here. An ecological-system interpretation may
support this broader environment; a strict material interpretation needs a
more explicit model. No direct-parent removal is prescribed on that ambiguity
alone. The exact extent of the GOLD bin and the intended mat/system boundary
remain a bounded follow-up, not a second confirmed finding.

The complete parent `hypersaline_water_environment.yaml` and its earlier
individual report were read. Its CLOSE mapping and erroneous global-to-inland
parent are tracked in #1245. That parent's own scope defect does not prove
this source-specific child's link to the global environment false. Its
organism counts and observations must not be copied to this mat.

## Evidence

Physical `gold_ecosystem_paths.tsv:542` gives one node, depth five, nine
organisms, zero study/biosample counters and total nine. `gold_path_biosamples.tsv:158`
independently gives 172 bulk samples. Triad rows 704-706 cover 171 complete-
triad samples across eight studies:

| Role | Top term | Share | Distinct terms | Agreeing studies |
| --- | --- | ---: | ---: | ---: |
| Broad | ENVO:00002030 aquatic biome | 1.00 | 1 | 8 |
| Local | ENVO:01001020 hypersaline lake | 0.92 | 6 | 3 |
| Medium | ENVO:01000157 microbial mat material | 0.99 | 2 | 7 |

The current [hypersaline-lake class](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001020)
is a lake containing water saltier than ocean water. That local annotation
describes a sampling feature, not mat identity. Its large sample share spans
only three agreeing studies and six local terms; medium is also heterogeneous.
The inspected aggregator counts studies containing the top term, not audited
experimental independence. There is no inspected sample-level crosswalk
establishing the 171 as a particular subset of the 172 bulk samples.

Nine exact study memberships were inspected:

| Physical row in gold_studies.tsv | Accession | Path count |
| --- | --- | ---: |
| 390 | Gs0067861 | 14 |
| 741 | Gs0113752 | 1 |
| 1382 | Gs0121729 | 1 |
| 1383 | Gs0126206 | 1 |
| 1384 | Gs0126207 | 1 |
| 1386 | Gs0126224 | 1 |
| 1635 | Gs0131229 | 1 |
| 1977 | Gs0133438 | 3 |
| 2043 | Gs0134635 | 2 |

All nine original study-page requests returned 403. Current experimental
contents were not recovered. Nine memberships are not the eight-study triad
cohort; path counts are not observations. Mixed thermal/marine paths in
Gs0067861 and rock-dwelling biofilm paths in Gs0133438 do not make this mat
thermal, marine or rock-attached. The complete 14-table scan found no exact-
target parameter, PREGO or BacDive taxon rows.

Current official GOLD vocabulary node 3979 is active with the full path and
partial annotations: broad ENVO:00002030 aquatic biome, medium ENVO:01000008
microbial mat, no local annotation. Those vocabulary assertions differ from
the sample-summary lake/material terms and do not certify every sample's scope.

Actual full normalized-table resolution gives gold_unmatched/UNGROUNDED/no
predicate. Applying the ITEM decision yields
curated_ground_as_parent_from_gold_unmatched, NARROW, skos:narrowMatch,
extra parent ENVO:01000008 and reviewed=True. `seed.py:554-566` owns that
route, applied at `:839-843`, with predicate emission at `:890-891`.
Schema `habitatmech.yaml:317-322` and `:776-790` declare source/record
comparisons, while the decision compares the retained source identity with
an ontology parent. The attestation's target is not that ontology endpoint.
This independently reproduces #1398; reversing the predicate alone is not a fix.

## Completeness

Ignored-inclusive ID/key, stem, node and exact-path searches covered curation,
history, research, reports, PATHS and RETIRED. Separate hypersaline-label and
filename inventories found adjacent water/lake reports, a water overlay and
history, and broader research leads, not a target-owned definition, overlay,
dedicated research, session history, retirement or prior individual mat review.
The ITEM decision and path lock exist. Broader research is not direct evidence
for this source's organisms or every mat's environmental-system classification.
Optional omissions are not defects. iModulonDB is inapplicable because no gene,
regulator or expression dataset is asserted.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | Curated NARROW/skos:narrowMatch use ontology-parent endpoints inconsistent with the declared source/record comparison. | GROUND_AS_PARENT resolver, attestation emitter, schema and consumers, #1398. |

Counts: zero blockers, one major, zero minor. No second confirmed hierarchy
defect: the environmental-system boundary is unresolved, not proven wrong by
analogy with whole-water-body parents. No formal SKOS inconsistency or observed
SSSOM/KGX export failure is asserted.

## Recommended Edits

1. Reconcile endpoint and grounding semantics across curated/automatic routes,
   preserving exact source identity, nine-ORGANISM count, generic mat parent,
   genuine ITEM review/history and legitimate imported mappings.
2. Audit the ecological-system interpretation and exact source/sample scope
   before changing ENVO:01001043. Coordinate the parent-level #1245 repair;
   do not automatically add this source to #1397's removal set or relabel it
   as a hypersaline lake based on sample triads.
3. Add subject/predicate/object/status and source-preservation regressions,
   append required correction history, and regenerate from maintained inputs.

## Follow-up Checks

For a maintained-input correction run `just seed`, then
`just seed-canary habitatmech:GOLD.df20aa5a67 --force`. Inspect the entire
canary, count/unit, selected parent semantics, REVIEWED state and both events
before `just seed-apply --force`; never prune partial runs. These are future
curation commands, not actions taken by this read-only review.

Require ordinary/strict schema, labels, source/history, mapping-consumer tests,
`just verify-corpus` and `just qc`. The full page displays both parents. An
exploratory in-memory removal of only ENVO:01001043 changes semantic text by
removing `broader habitat: hypersaline water environment`; this diagnoses
refresh impact, not correctness or authorization of that removal. Any such
chosen hierarchy change needs the genuine #1217 map/site refresh. Predicate-
only omission was separately text-neutral. Keep #1218 and runtime pins intact;
audit actual SSSOM/KGX products before a compatibility claim.

## Additional Notes

All-state exact-source issue search found none. Hypersaline/environment
search found #1245, #1397 and #12; #1245's full body/comments concern parent
scope and other layer/whole-body cases, not a proof of this child's false is-a.
Extend #1398 with this definite endpoint witness, leaving hierarchy uncertainty
explicit rather than manufacturing another confirmed exclusion.

Decision notes end with `Microbi`; the event faithfully carries the maintained
text while the full attestation path is intact. Official typed OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No scientific input, generated product, prior report/history or paid research changed.
