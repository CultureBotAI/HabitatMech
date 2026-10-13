# YAML Record Review: anterior fornix of vagina

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/anterior_fornix_of_vagina.yaml`
- Started UTC: 2026-10-04T02:10:45Z
- Finished UTC: 2026-10-04T02:12:58Z
- Verdict: needs curation

## Target

Read the entire generated HabitatRecord `UBERON:0016487`: HOST_ASSOCIATED,
CLOSE, REVIEWED. It contains an ontology definition, four source/ontology
synonyms, two parents, one uncounted GOLD attestation and two events. The
source is Human > Reproductive system > Vagina > Anterior fornix, not the
posterior fornix, vaginal fluid or whole vagina. The actual `mint` helper
reproduces source key `habitatmech:GOLD.c3e9d3ce0b`; `PATHS.tsv:1143` pins
the current filename.

## Validation

- `just validate data/habitats/host_associated/anterior_fornix_of_vagina.yaml`:
  passed, no issues.
- `just validate-strict data/habitats/host_associated/anterior_fornix_of_vagina.yaml`:
  one file, zero errors.
- Fresh batch `just validate-products`: passed, 1,179 canonical pairs,
  one synonym, five configured exceptions and 2,054 no-adapter skips.
- Fresh QC remains running. Lint, documentation, raw provenance, 457 tests
  (three skipped, two dependency warnings), 85 history records, 3,206 strict
  records, 32 overlays, curation floor and exact corpus reproduction passed.
  Generated-site and later gates have not yet returned a terminal result.
- Browser OLS retrieval failed; direct official term and typed-graph requests
  succeeded and were inspected. Failed retrievals are not source evidence.

## Identity and Grounding

Current [UBERON:0016487](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0016487)
is non-obsolete and agrees with vendored `ontology_terms.tsv:13488` on label,
definition and the three ontology synonyms. Its location in front of the
cervix is compatible with the exact human source path. The ontology
definition's inherited wording is not a new local transcription defect.

`curation/decisions.tsv:1751` is ITEM REVIEW of the seeder's CLOSE resolution.
The record faithfully carries that conservative relation, source predicate,
REVIEWED status and two August 16 events. An exact-status upgrade is not
required merely because the source phrase is a synonym; this review does not
change identity or adjudicate a new merge. ITEM status alone does not endorse
every independently contributed parent.

The current [anterior-fornix graph](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0016487/graph)
asserts subclass UBERON:0000051, fornix of vagina. Vendored subclass edge
11800 and term row 12889 agree. That is the valid broader anatomy.

The separately inspected [fornix graph](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000051/graph)
asserts subclass anatomical cavity, but BFO:0000050 part_of
UBERON:0000996, vagina. The part-of edge is on the superclass, not falsely
reported as a direct edge from this anterior-fornix node. Current definitions
and non-obsolete statuses were checked for both fornix and vagina.

The complete `vagina__a4a4e1ad.yaml` identifies the second parent,
`habitatmech:GOLD.1daee83236`, as the whole human vagina, NARROW beneath
[UBERON:0000996](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0000996).
The current UBERON definition denotes a fibromuscular tract, not a genus of
vaginal recesses, and the source record has no authored broader environmental
definition. Typed relations and definitions establish containment rather
than the published whole-organ is-a relation.

## Evidence

`gold_ecosystem_paths.tsv:2413` supplies node 6560, the exact five-level path,
one source node and zero organism/study/biosample assertions. Generated
source ID, source label, full path and absence of a positive count are
faithful. The parent record's 475 ORGANISM assertions do not belong to this
anterior recess, and they do not establish a target microbial taxon.

Full structured scans of 2,562 tree paths, 1,040 bulk rows, 4,587 study rows
and 1,587 triads find only the exact tree row for anterior-fornix wording or
UBERON:0016487. No target bulk, study or triad entry was found. Posterior
fornix or other vaginal sampling sites are not interchangeable attestations.
No live sample metadata or primary-study microbiota is invented.

`src/habitatmech/seed.py:898-907` adds the whole-vagina source parent. The
strict broader/is-a rule in `docs/CURATION.md` binds this source-path
contribution as well as ontology and curated-definition parents. A faithful
GOLD breadcrumb is not a valid superclass merely because it reproduces.

## Completeness

Ignored-inclusive target/source/parent identifiers, label and filename
searches covered curation, history, research, prior reviews, raw inventories,
PATHS and RETIRED. They found the ITEM decision and ontology data but no
target definition request, overlay, session record or earlier exact-target
review. Missing later-style history for older curation is not a defect.

Full scans of 162 BacDive sources, 3,081 BacDive taxa, 770 parameters,
358 mappings, 58 Madin habitats, 1,378 Madin taxa, 719 PREGO habitats and
8,807 PREGO taxa found no anterior-fornix or UBERON:0016487 match. This is
a bounded inventory result, not a claim that the site lacks microorganisms.
Optional taxa, parameters and graphs are not quotas. iModulonDB is not
applicable: no gene, regulator or expression-module claim is present.

## Findings

1. **Major - HM-ANTERIOR-FORNIX-001:** the supported fornix identity also
   carries an unsupported whole-vagina superclass from GOLD nesting.
   Maintained owner: `src/habitatmech/seed.py:898-907` or a governed
   source-specific exclusion. Filed as
   [#1333](https://github.com/CultureBotAI/HabitatMech/issues/1333).

No blocker or minor finding established. Identity, definition, conservative
grounding, fornix superclass and faithful source copying remain supported.

## Recommended Edits

Correct or exclude this exact GOLD parent while retaining UBERON:0016487,
UBERON:0000051, the human source fields and intended status. Do not replace
the record with whole vagina or posterior fornix, encode part-of as an
equivalence xref, globally delete GOLD parents or hand-edit generated YAML.

A read-only copy through the real `semantic_text` adapter confirms that
removing the source parent drops the Vagina broader-habitat line and changes
the input. Append required history, inspect a guarded canary and regenerate
map/site through supported tooling. #1217 remains relevant; draft #1218 is
not assumed merged. No scientific correction is claimed in this report.

## Follow-up Checks

Regress this exact source contribution and retain valid fornix ancestry,
source node, absent positive count and intended CLOSE/REVIEWED states unless
a separate ITEM decision changes them. Require strict schema, OAK, history,
full ancestry, corpus reproduction, semantic/site/redirect freshness and QC.

## Additional Notes

All 488 existing issue bodies and returned comments were searched for the
target/source/parent keys, fornix and vaginal-parent wording. No matching
repair was found. Historical #12 was checked as background, not a scientific
endorsement. Parent reads do not count as new target reviews. No scientific
input, generated record or history changed, and no paid research ran.
