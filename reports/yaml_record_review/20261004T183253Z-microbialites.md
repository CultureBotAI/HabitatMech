# YAML Record Review: Microbialites

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/microbialites.yaml`
- Started UTC: 2026-10-04T18:29:29Z
- Finished UTC: 2026-10-04T18:32:53Z
- Verdict: needs curation

## Target

Entire generated HabitatRecord habitatmech:GOLD.2d24faa338, Microbialites,
AQUATIC, NARROW/REVIEWED. Two parents, one uncounted GOLD attestation with
skos:narrowMatch and two history events are present. Definition, synonyms,
xrefs, parameters, taxa, citations, graphs, discussions, datasets and
replacement links are not emitted.

The exact source is gold.ecosystem:7933,
`Environmental > Aquatic > Non-marine Saline and Alkaline > Hypersaline soda lake > Microbialites`.
The actual mint matches; PATHS.tsv:1620 pins this stem. This is the
microbialite, not the lake or its separately reviewed microbial-mat child.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/microbialites.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/microbialites.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Fresh batch run PASS: 1,179 canonical pairs, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | PASS: 953 ungrounded records, 1,810 decisions. |
| `just qc` | Fresh batch run active in tests; lint, documentation and raw provenance passed. No terminal result claimed. |
| Source/reference checks | Full target and parent, maintained rows, earlier parent report, all 14 raw tables, actual resolver, typed OWL/current OLS and full page/semantic comparisons inspected. |

The preceding PR #1402's separate main QC is now terminal SUCCESS, but it
does not substitute for this live batch run. Later QC completion belongs in
the publication receipt, not a backdated change to this observation.
No SSSOM/KGX export or compatibility audit was executed.

## Identity and Grounding

`curation/decisions.tsv:343` is a real ITEM GROUND_AS_PARENT decision dated
2026-08-12 for ENVO:03600064 microbialite. The retained identity, REVIEWED
status and ITEM-plus-seed history follow that row mechanically.

Current official [ENVO:03600064 microbialite](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A03600064)
is active. Its definition is explicitly sedimentary carbonate rock formed
with microbial mediation in a benthic setting; its named parent is
ENVO:00002016 sedimentary rock. The vendored definition at
`ontology_terms.tsv:10100` agrees; the subclass edge is at
`ontology_subclass_edges.tsv:8498`. This is not an unmineralized mat, a
whole lake, or an unrestricted microbial assemblage.

The genus is label-aligned and selected by genuine ITEM curation, but the
available exact-source evidence does not independently establish mineralogy.
Preserve the carbonate restriction in any future assessment rather than
claiming that every possible use of Microbialites is covered. No inspected
counterexample proves this particular bin non-carbonate; this is a bounded
scope uncertainty, not an automatic genus-removal finding.

The full parent `hypersaline_soda_lake.yaml` is habitatmech:GOLD.3098ee8fe8,
UNGROUNDED/SEEDED, with 29 ORGANISM assertions and two collapsed nodes.
Its CLASS decision at `curation/decisions.tsv:366` does not supply this
child's ITEM review. A microbialite located in a lake is not a kind of
whole lake. Current hypersaline-lake and alkaline-salt-lake classes describe
water bodies; typed ENVO marks soda lake as a RELATED synonym of the latter,
not exact. Re-grounding the parent lake would not repair this false is-a.

The complete earlier `20261003T133136Z-hypersaline_soda_lake.md` report was
read. Its parent-level pass and literature examples do not validate this
incoming edge or establish mineralogy, taxa or conditions for this source.

## Evidence

Physical `gold_ecosystem_paths.tsv:1565` gives the exact depth-five path,
one source node and zero organism/study/biosample counters and total.
Count/unit omission is faithful, not an assertion of biological absence.
The complete 14-table structured scan found no exact-target bulk samples,
API triads, study memberships, parameters, PREGO or BacDive taxon rows.
The parent's 29 organisms are a different cohort and are not borrowed.

Current official GOLD vocabulary lookup for w3id.org/gold.path/7933 returned
404. The committed source is verified; current original contents were not
recovered. No retirement, chemical measurement or mechanism is inferred.

Actual resolution with the complete normalized mapping table and seeder's
setdefault rule gives default gold_unmatched/UNGROUNDED/no predicate.
Applying the ITEM row yields curated_ground_as_parent_from_gold_unmatched,
NARROW/skos:narrowMatch, extra parent ENVO:03600064 and reviewed=True.
The curated route is `seed.py:554-566`, applied at `:839-843`. The separate
GOLD parent pass at `:898-907` adds the false whole-lake parent.

Predicate emission at `:890-891` independently reproduces #1398 beyond mat
records: schema `habitatmech.yaml:317-322` and `:776-790` compare source and
record, while this route compares the retained source identity with an
ontology parent not represented as the attestation's target. Reversing the
predicate alone is insufficient. No formal SKOS inconsistency is asserted.

## Completeness

Ignored-inclusive exact ID/node, label and stem searches covered curation,
history, research, reports, PATHS and RETIRED, with a separate filename
inventory. They found the decision and lock, not a target-owned definition,
overlay, dedicated research, session history, retirement or prior individual
review. Broader inland-saline and microbial-host research mentions are leads,
not evidence for this exact source. Optional omissions are not defects.
iModulonDB is inapplicable without a gene, regulator or expression claim.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | A microbialite inherits its whole hypersaline soda lake as a strict broader identity. | GOLD parent pass or governed exclusion for GOLD.2d24faa338 and expected parent GOLD.3098ee8fe8; coordinate the analogous mat issue #1397. |
| Major | Curated NARROW/skos:narrowMatch use ontology-parent endpoints rather than the declared source/record comparison. | Resolver, attestation emitter, schema and consumers, #1398. |

Counts: zero blockers, two major, zero minor. Source identity, count omission
and review/history derivation are faithful. The carbonate-genus boundary is
unresolved, not a third confirmed defect or a claimed mineralogical result.

## Recommended Edits

1. Suppress only the false lake context-parent contribution through maintained
   inputs; preserve source identity/path/node, count omission and actual history.
2. Reconcile endpoint/status semantics across real routes, preserving distinct
   source identities and legitimate mappings. Do not simply reverse predicates.
3. Assess exact source scope against ENVO:03600064's carbonate restriction
   before any genus change. Do not replace the genus with a mat or lake, or
   discard it merely because exact-source mineralogy is unavailable.
4. Add source/edge/endpoint regressions, append required correction history
   and regenerate through maintained inputs, not generated records or old history.

## Follow-up Checks

After correction run `just seed`, then
`just seed-canary habitatmech:GOLD.2d24faa338 --force`. Inspect the entire
canary, selected genus scope, absent count/unit, REVIEWED derivation and prior
events plus required new history before `just seed-apply --force`. Never prune
partial runs. These are future curation commands, not review actions.

Require ordinary/strict validation, labels, source/history and mapping-consumer
tests, `just verify-corpus` and `just qc`. The full page lists the whole lake
as Broader habitat. Its isolated removal changes full-context semantic text
by removing `broader habitat: Hypersaline soda lake`; scientific repair needs
genuine map/site refresh under #1217. Predicate-only omission was separately
text-neutral. Protect #1218/runtime pins and audit actual SSSOM/KGX products
before claiming compatibility.

## Additional Notes

Prepublication correction at 2026-10-04T18:37:19Z, tracked in #1404:
the named parent is sedimentary rock, verified against current typed OWL/OLS
and `ontology_terms.tsv:7178`. The earlier draft mislabeled it carbonate rock;
the carbonate restriction belongs to the microbialite definition. Findings
and the original completion-time QC observation are unchanged.

All-state microbialite, microbialite/parent and exact-key issue searches
returned no matches. A bounded microbialite hierarchy issue should coordinate
with #1397; extend #1398 for the shared endpoint contract. Publication does
not implement or close scientific findings.

The maintained rationale's Path fragment stops at the parent lake, but the
key and full attestation path are intact. The event copies maintained text
verbatim. Web-viewer OLS access failed while direct official API retrieval
succeeded. A non-carbonate-microbialite literature lead could not be opened
(429/unavailable); search snippets were not adopted as primary evidence or
as proof about this source bin. Official typed ENVO OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No scientific input, prior report/history, generated product or paid research changed.
