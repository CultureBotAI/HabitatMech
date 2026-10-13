# YAML Record Review: Microbial mats

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/microbial_mats__cfca43d0.yaml`
- Started UTC: 2026-10-04T17:59:47Z
- Finished UTC: 2026-10-04T18:01:42Z
- Verdict: needs curation

## Target

Entire generated HabitatRecord habitatmech:GOLD.2c1e36b661, Microbial mats,
AQUATIC, NARROW/REVIEWED. Two parents, one GOLD attestation with two ORGANISM
assertions and skos:narrowMatch, and two history events are present. Definition,
synonyms, xrefs, parameters, taxa, citations, graphs, discussions, datasets
and replacement links are not emitted.

The exact source is gold.ecosystem:7886,
`Environmental > Aquatic > Non-marine Saline and Alkaline > Hypersaline soda lake > Microbial mats`.
The actual mint matches; PATHS.tsv:1613 pins the stem. This is the mat, not
the lake, its microbialite/sediment siblings or the separate plain soda-lake mat.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/microbial_mats__cfca43d0.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/microbial_mats__cfca43d0.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Shared fresh run PASS: 1,179 canonical pairs, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | PASS: 953 ungrounded records, 1,810 decisions. |
| `just qc` | Terminal PASS: 457 tests, three skipped, two warnings in 763.06 seconds; 90 history records, 3,206 strict records, 32 graph curations, exact reproduction and all site/redirect/term-request and remaining gates passed. |
| Source/reference checks | Full target and parent, maintained rows, earlier parent report, all 14 raw tables, actual resolver, typed OWL/current OLS and full page/semantic comparisons inspected. |

Identifier-label validation does not certify SSSOM/KGX compatibility. No
downstream export execution or observed export failure is claimed.

## Identity and Grounding

The real ITEM decision at `curation/decisions.tsv:339`, dated 2026-08-12,
uses GROUND_AS_PARENT with ENVO:01000008 microbial mat. The true generic
mat parent, retained source identity, REVIEWED state and two events follow
that decision. ENVO:01000157 is material derived from a mat, not an automatic
identity substitute; both were checked against official ENVO in this batch.

The full `hypersaline_soda_lake.yaml` parent is
habitatmech:GOLD.3098ee8fe8, UNGROUNDED/SEEDED, with 29 ORGANISM assertions
and two collapsed nodes. `curation/decisions.tsv:366` is a CLASS-level
no-match sweep, not an ITEM assessment. The mat's own genuine ITEM review
does not depend on the parent's lifecycle state. It denotes a mat occurring
in the lake, not a kind of the whole lake, so the source-path parent is false
under the repository's strict broader-habitat contract.

Current [ENVO:01001020 hypersaline lake](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001020)
and [ENVO:00002121 alkaline salt lake](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002121)
are distinct lake candidates: the former requires salts above seawater and
the latter high pH. Typed OWL records soda lake as a RELATED synonym of the
latter, not an exact one. Neither is a microbial-mat identity or genus.
Any later parent-lake grounding must not convert the current false edge
into an ontology-backed mat-to-lake is-a.

The complete earlier `20261003T133136Z-hypersaline_soda_lake.md` report
was read. Its pass concerns that parent record's own represented claims,
not this child's incoming edge. Its literature examples are not an inspected
crosswalk to this mat's two organisms and are not borrowed here.

## Evidence

Physical `gold_ecosystem_paths.tsv:804` gives the exact depth-five path,
one node, two organisms, zero study/biosample counters and total two. The
generated count and unit are faithful. The complete 14-table scan found
no exact-target bulk samples, API triads, study memberships, parameters,
PREGO or BacDive taxa. These are bounded snapshot misses, not biological
absence or a reason to transfer the parent lake's count, measurements or taxa.

Current official GOLD vocabulary lookup for w3id.org/gold.path/7886 returned
404. The exact committed source is verified; current original node contents
were not recovered, and no retirement inference is made. The path is not a
measurement of this mat's pH, salinity or metabolism.

Actual resolution with the complete normalized mapping table gives default
gold_unmatched/UNGROUNDED/no predicate. Applying the ITEM row yields
curated_ground_as_parent_from_gold_unmatched, NARROW, skos:narrowMatch,
extra parent ENVO:01000008 and reviewed=True. The owner is `seed.py:554-566`,
applied at `:839-843`; the separate GOLD parent pass at `:898-907` adds the
false whole-lake parent.

Predicate emission at `:890-891` also reproduces #1398. Schema
`habitatmech.yaml:317-322` and `:776-790` declare source/record comparisons,
but the decision compares the retained identity with an ontology parent not
represented as the attestation's target. Reversing the predicate alone is
insufficient. No formal SKOS inconsistency is asserted.

## Completeness

Ignored-inclusive ID/key, stem, source-node/path and hypersaline-soda-lake
label searches covered curation, history, research, reports, PATHS and RETIRED.
A separate filename inventory found the parent report, not a target-owned
definition, overlay, dedicated research, session history, retirement or
prior individual mat review. The ITEM decision and path lock are present.
Broader inland-saline research mentions are leads, not primary source-specific
evidence. Optional omissions are not defects. iModulonDB is inapplicable
without a gene, regulator or expression dataset claim.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | The hypersaline-soda-lake mat inherits the whole lake as a strict broader identity. | GOLD parent pass or governed exclusion for GOLD.2c1e36b661 and expected parent GOLD.3098ee8fe8, #1397. |
| Major | Curated NARROW/skos:narrowMatch compare ontology-parent endpoints rather than the declared source/record fields. | Resolver, attestation emitter, schema and consumers, #1398. |

Counts: zero blockers, two major, zero minor. Mat identity, true generic
parent, two-ORGANISM count, ITEM review and event derivation remain sound.

## Recommended Edits

1. Suppress only the whole-lake parent contribution. Preserve ENVO:01000008,
   exact source identity/path/node/count and actual review history. Keep the
   exclusion valid through any later grounding of the parent lake.
2. Reconcile endpoint and grounding semantics across actual routes,
   preserving legitimate mappings and distinct source mat identities.
3. Add exact-edge/source-preservation and endpoint regressions, append
   required correction history and regenerate from maintained inputs.

## Follow-up Checks

After correction run `just seed`, then
`just seed-canary habitatmech:GOLD.2c1e36b661 --force`. Inspect the complete
canary, two-ORGANISM count, true mat parent, REVIEWED derivation and prior
events plus required correction history before `just seed-apply --force`.
Do not prune partial runs. These are future curation commands, not review edits.

Require ordinary/strict schema, labels, source/history and mapping-consumer
checks, `just verify-corpus` and `just qc`. The complete page lists the lake
as a Broader habitat. Removing only it in the full-context semantic adapter
removes `broader habitat: Hypersaline soda lake`; scientific repair needs
genuine map/site refresh under #1217. Predicate-only omission was separately
text-neutral. Protect #1218/runtime pins and audit actual SSSOM/KGX output
before a compatibility claim.

## Additional Notes

All-state exact-source and hypersaline-soda issue searches returned no
matches. Extend the independently verified #1397/#1398 witnesses; a pass for
the parent does not resolve this child's edge or the mapping contract.

The maintained rationale's Path fragment stops at the parent label. The full
attestation path and keyed ITEM target remain correct, and the event copies
the maintained text verbatim. Unlike the separately reviewed plain soda-lake
mat, this row actually targets the microbial-mat genus, not a lake.
Official typed ENVO OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No scientific data, prior report/history or paid research changed.
