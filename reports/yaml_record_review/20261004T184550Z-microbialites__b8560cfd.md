# YAML Record Review: Microbialites

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/microbialites__b8560cfd.yaml`
- Started UTC: 2026-10-04T18:44:34Z
- Finished UTC: 2026-10-04T18:45:50Z
- Verdict: needs curation

## Target

Entire generated HabitatRecord habitatmech:GOLD.f46eba7b40, Microbialites,
AQUATIC, NARROW/REVIEWED. Two parents, one uncounted GOLD attestation with
skos:narrowMatch and two history events are present. Definition, synonyms,
xrefs, parameters, taxa, citations, graphs, discussions, datasets and
replacement links are not emitted.

The exact source is gold.ecosystem:7935,
`Environmental > Aquatic > Non-marine Saline and Alkaline > Hypersaline lake > Microbialites`.
The actual mint matches; PATHS.tsv:3111 pins the stem. The microbialite is
not the whole lake, its microbial-mat sibling or the separate Hypersaline
water-environment microbialite source.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/microbialites__b8560cfd.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/microbialites__b8560cfd.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Fresh shared run PASS: 1,179 canonical pairs, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | PASS: 953 ungrounded records, 1,810 decisions. |
| `just qc` | Terminal PASS: 457 tests, three skipped, two warnings in 635.50 seconds; 90 history records, 3,206 strict records, 32 graph curations, exact reproduction and all remaining site/redirect/term-request/QC gates passed. |
| Source/reference checks | Full target, maintained row, all 14 raw tables with exact path membership, actual resolver, typed OWL/current OLS and full page/semantic comparisons inspected. |

Identifier-label validation is not a complete SSSOM/KGX modeling audit.
No downstream export execution or observed export failure is claimed.

## Identity and Grounding

`curation/decisions.tsv:1350` is a genuine ITEM GROUND_AS_PARENT row dated
2026-08-12 for ENVO:03600064 microbialite. The retained source identity,
REVIEWED state and two events follow this maintained decision.

Current official [ENVO:03600064 microbialite](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A03600064)
is active and explicitly carbonate-mud scoped, with microbial-mediated
benthic formation. Its named parent ENVO:00002016 is sedimentary rock.
This is not a generic unmineralized mat or whole microbial assemblage.
The candidate is label-aligned and curator-selected, but no exact-source
mineralogical evidence was recovered for this bin. Preserve that limitation;
neither universal carbonate composition nor a non-carbonate counterexample
has been independently established here. It is not an automatic genus-removal
finding.

Current [ENVO:01001020 hypersaline lake](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001020)
is a lake whose water has more dissolved salts than ocean water. Its typed
OWL has named parent saline lake and a separate hypersaline-water composition
restriction. A microbialite located in a hypersaline lake is not a kind of
whole lake. The source path is environmental context, not a valid is-a edge
or a quantitative measurement for each microbialite.

## Evidence

Physical `gold_ecosystem_paths.tsv:1563` gives the exact depth-five path,
one node, zero organism/study/biosample counters and zero total. Omitted
assertion_count and assertion_unit faithfully follow the emission rule;
they do not establish biological absence. The complete 14-table exact-path
scan found no target bulk samples, API triads, study memberships, parameters,
PREGO or BacDive taxa. No parent-lake or sibling-mat cohort is borrowed.

Current official GOLD vocabulary lookup for w3id.org/gold.path/7935 returned
404. The committed source path is verified; current original contents were
not recovered. This does not prove retirement or justify filling optional
composition, taxon, salinity or mechanism fields from generic literature.

Actual resolution with the complete normalized mapping table/setdefault rule
gives default gold_unmatched/UNGROUNDED/no predicate. Applying the ITEM row
yields curated_ground_as_parent_from_gold_unmatched, NARROW/skos:narrowMatch,
extra parent ENVO:03600064 and reviewed=True. The route is `seed.py:554-566`,
applied at `:839-843`. The separate GOLD parent pass at `:898-907` adds
the false whole-lake parent.

Predicate emission at `:890-891` reproduces #1398 beyond the mat cohort.
Schema `habitatmech.yaml:317-322` and `:776-790` compare source and record;
this decision compares the retained identity with an ontology parent not
represented as the attestation's target. Reversing the predicate alone does
not reconcile those endpoints. No formal SKOS inconsistency is asserted.

## Completeness

Ignored-inclusive exact ID/node/path and stem searches, the shared microbialite
label scan and separate hypersaline-lake filename inventory covered curation,
history, research, reports, PATHS and RETIRED. They found the decision and
lock, not a target-owned definition, overlay, dedicated research, session
history, retirement or prior individual review. Adjacent lake reports and
broader inland-saline research are leads, not primary evidence for this source.
No full new audit of the parent lake is claimed. Optional omissions are not
defects; iModulonDB is inapplicable without a gene/regulator/expression claim.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | The microbialite inherits its whole hypersaline lake as a strict broader identity. | GOLD parent pass or governed exclusion for GOLD.f46eba7b40 and expected parent ENVO:01001020. |
| Major | Curated NARROW/skos:narrowMatch use ontology-parent endpoints rather than the declared source/record comparison. | Resolver, attestation emitter, schema and consumers, #1398. |

Counts: zero blockers, two major, zero minor. Source identity, count omission
and review/history derivation remain faithful. Carbonate-genus scope remains
a bounded uncertainty, not an additional confirmed defect.

## Recommended Edits

1. Suppress only the false lake-parent contribution, preserving source
   identity/path/node, count omission and actual review history.
2. Reconcile endpoint/status semantics across real routes, preserving distinct
   source concepts and legitimate mappings rather than reversing predicates.
3. Assess exact source scope against the microbialite definition before
   changing its genus; do not replace it with the lake or a mat by analogy.
4. Add exact-source/edge/endpoint regressions, append required correction
   history and regenerate through maintained inputs.

## Follow-up Checks

After correction run `just seed`, then
`just seed-canary habitatmech:GOLD.f46eba7b40 --force`. Inspect the whole
canary, absent count/unit, selected genus, REVIEWED derivation and prior events
plus required new history before `just seed-apply --force`. Never prune
partial runs. These are future curation commands, not executed review edits.

Require ordinary/strict schema, labels, source/history and mapping-consumer
tests, `just verify-corpus` and `just qc`. The full page lists hypersaline
lake under Broader habitats. Its isolated removal changes full-context
semantic text by removing `broader habitat: hypersaline lake`; scientific
repair needs genuine map/site refresh under #1217. Predicate-only omission
was separately text-neutral. Protect #1218/runtime pins and audit actual
SSSOM/KGX products before claiming compatibility.

## Additional Notes

All-state exact-key and shared microbialite searches returned no matches.
Track the bounded microbialite hierarchy witness and extend #1398; neither
scientific defect is repaired by report publication.

The maintained rationale ends at `Mi`; the event copies it verbatim while
the full attestation path is intact. Official typed ENVO OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No scientific input, generated product, prior report/history or paid research changed.
