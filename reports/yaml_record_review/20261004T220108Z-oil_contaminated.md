# YAML Record Review: Oil-contaminated

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/oil_contaminated.yaml`
- Started UTC: 2026-10-04T21:57:44Z
- Finished UTC: 2026-10-04T22:01:08Z
- Verdict: needs curation

## Target

Entire generated HabitatRecord habitatmech:GOLD.a83d030599, Oil-contaminated,
AQUATIC/NARROW/REVIEWED. The exact source path is Environmental > Aquatic >
Marine > Intertidal zone > Oil-contaminated. The record has two parents,
one GOLD attestation without count/unit, and two history events. Definition,
synonyms, taxa, parameters, xrefs, evidence, graphs, discussions and datasets
are absent. `data/habitats/PATHS.tsv:2527` pins the filename.

This review concerns the intertidal qualified-water source, not the identically
labelled Oceanic source, oil-contaminated sediment, soil, or an oil spill
considered independently of the water it affects.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/oil_contaminated.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/oil_contaminated.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Fresh batch PASS: 1,179 canonical, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | PASS: 953 ungrounded records, 1,810 decisions. |
| `just qc` | Fresh authorized run active in tests; lint, documentation and 14-inventory provenance passed. No terminal result claimed. |
| Source/reference checks | Entire target and contextual parent, actual child/parent resolvers, full generated-field equality, all 14 raw tables, current typed ENVO/OLS and GOLD, original-study attempt, W3C mapping specification, full page and semantic comparison. |

Full construction reproduces all fields with one source concept and one
reviewed source. Schema and reproduction success do not establish scientific
correctness of hierarchy or the mapping-field contract. The prior PR #1416
post-merge QC was still live when polled; it was not restarted or counted
as this batch's terminal result. No SSSOM/KGX compatibility audit is claimed.

## Identity and Grounding

Actual minting reproduces habitatmech:GOLD.a83d030599. Automatic resolution
is gold_unmatched/UNGROUNDED. ITEM GROUND_AS_PARENT at decisions.tsv:960,
dated 2026-08-13, retains that identity, adds ENVO:00002149 sea water, and
produces curated_ground_as_parent_from_gold_unmatched, NARROW and
skos:narrowMatch. REVIEWED and the GROUND_AS_PARENT/seed events faithfully
reflect this decision, not an independently established exact ENVO identity.

The curated water interpretation is consistent with the exact-path medium
annotation below. Current [ENVO:00002149 sea water](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002149)
is active and denotes water whose properties arise from marine processes.
Oil contamination does not make that water a soil or justify exact-grounding
all oil-contaminated contexts to one generic term. Preserve the seawater genus
and the path-specific identity; keep the material interpretation bounded by
the single sample and the unavailable original study.

Current [GOLD node 4020](https://www.ebi.ac.uk/ols4/api/ontologies/gold/terms/https%253A%252F%252Fw3id.org%252Fgold.path%252F4020)
is active for this exact path. It supplies marine-biome broad context and
oil-spill local context, but no exact-match or medium assertion in the
inspected live response. Those contextual terms do not replace source identity.
Current ENVO:00002061 oil spill denotes the result of an unintentional
petroleum release from human activity, not specifically the sampled seawater.

The contextual parent file was read completely. GOLD Intertidal zone is
habitatmech:GOLD.115edc36f8, NARROW/SEEDED, with ENVO:00000316 and marine
water body as parents. Its actual gold_narrower_than_leaf_match route retains
the minted geographic identity. Current [ENVO:00000316](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000316)
describes the shore/seabed area between tidal marks. Contaminated seawater
in that zone is not a subtype of the geographic area. The extra parent is
introduced independently by seed.py:898-907, the unconditional GOLD path pass.

There is also a distinct endpoint-contract defect. Schema lines 317-322
define SourceAttestation.mapping_predicate as source concept to record
identifier, omitted when the record is the source concept. GroundingStatusEnum
lines 776-790 describes that same comparison. Here both source and record
retain the exact minted path identity, while GROUND_AS_PARENT at seed.py:554-566
derives NARROW/narrowMatch from the comparison with an ontology parent and
seed.py:890-891 copies it into the attestation. That is not the declared target.

The inspected [W3C SKOS mapping reference](https://www.w3.org/TR/skos-reference/#mapping)
distinguishes broad/narrow mapping direction and does not prohibit hierarchical
self-links. This finding is the application's endpoint mismatch, not a formal
SKOS inconsistency. A global broadMatch/narrowMatch swap would not repair the
implicit-target problem. This explicit-curation route is another #1398 witness.

## Evidence

| Exact source locator | Supported account |
| --- | --- |
| gold_ecosystem_paths.tsv:1526 | Depth five, one node 4020, zero organism/study/biosample counters and zero total assertions in this inventory. |
| gold_path_biosamples.tsv:972 | One separately counted bulk sample at node 4020. |
| gold_path_triads.tsv:554-556 | One complete-triad sample in one study: broad ENVO:00000447 marine biome, local ENVO:00002061 oil spill, medium ENVO:00002149 sea water; each share 1.00 and one agreeing study. |
| gold_studies.tsv:158 | Gs0050523 spans two paths: this intertidal source and the distinct Oceanic oil-contaminated source. |

All triad identifiers and current definitions were verified. These are three
roles from one sample, not three independent studies. The one/one API/bulk
counts do not by themselves identify an exact sample crosswalk. Zero organism
assertions is why the seeder omits count and unit; do not replace them with
one ORGANISM by borrowing the separate biosample count. The rendered page
faithfully leaves the assertion count blank.

The original Gs0050523 page returned HTTP 403. A bounded exact-accession web
search recovered no usable scientific account; an unrelated identifier
collision was not treated as this study. No organism, experiment, oil
concentration, salinity threshold, or bioremediation mechanism was recovered.
Shared study membership does not merge the two source paths or their samples.

The complete structured exact-path/source-ID scan covered all 14 raw TSVs.
No PREGO, BacDive, MADIN, taxon or parameter contribution feeds this target.
Generic oil-water literature and neighboring soil research are not evidence
for these inaccessible original samples. No #1249 synonym-scope witness
exists in this record's empty synonym list.

## Completeness

Ignored-inclusive ID, parent key, exact path, label/stem and filename searches
covered curation, history, research, conf, raw inventories, reports, PATHS and
RETIRED. The maintained ITEM decision and path lock were found; no target-owned
definition, overlay, session history, retirement or prior individual report
was found. Same-label neighboring paths remain distinct, not duplicates to
delete. Candidate searches in the committed ontology slice found related
oil/soil/production-water terms, not evidence for an exact identity here;
no exhaustive claim about every possible ontology release is made.

A future definition can make the seawater genus and intertidal qualifier
explicit through curation/term_requests.tsv after original scope is checked.
The optional empty definition alone is not a schema failure. Do not fabricate
taxa, measurements or causal edges to fill empty fields. iModulonDB is
inapplicable without gene, regulator or expression assertions.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | A geographic intertidal-zone parent is asserted as strict genus of qualified seawater. | Governed source-specific parent control and src/habitatmech/seed.py:898-907. |
| Major | GROUND_AS_PARENT emits a parent-comparison predicate/status into fields describing source-to-record identity. | Schema, decision resolution and mapping consumers under shared #1398. |

Counts: zero blockers, two major, zero minor. Preserve genuine seawater
ancestry, source identity, evidence and review history while addressing them.

## Recommended Edits

1. Suppress only this source's unsupported GOLD.115edc36f8 parent through a
   maintained rule. Retain ENVO:00002149 and the exact path; do not hand-edit
   generated YAML or globally remove all GOLD hierarchy.
2. Resolve #1398 with explicit subject/object semantics for source identity
   and record-to-parent mappings. Cover the curated GROUND_AS_PARENT route
   in regression tests; do not just reverse every predicate or force exact
   identity with generic seawater.
3. Append new curation history for actual corrections. Recover original
   sample evidence before adding a definition, taxa, measurements or graphs;
   update the existing decision rather than insert a duplicate.

## Follow-up Checks

Dry seed, inspect `just seed-canary habitatmech:GOLD.a83d030599 --force`, then
guarded full regeneration without partial prune. Require parent-retention
and endpoint tests, schema/strict/products/history/provenance checks, exact
reproduction, site/redirect/term-request checks and full QC.

Actual full-context removal of only the geographic parent changes semantic
text, requiring real map/site refresh under #1217. A predicate-only removal
is text-neutral. Preserve protected draft #1218 and runtime pins. Audit actual
SSSOM/KGX triples and their endpoints before making compatibility claims.

## Additional Notes

All-state source-key/label and exact-node searches found no dedicated target
issue; the broad label query returned unrelated closed #38. Full #1253
concerns the parent record's own marine-waterbody edge, not this child's
edge. Full #1398 owns the shared endpoint contract. These are separate
implementation concerns, not fixes accomplished by this report.

Official typed ENVO OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No scientific input, generated artifact, old report/history, paid research
or GitHub item was changed by this individual review.
