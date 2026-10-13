# YAML Record Review: Oil-contaminated sediment

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/oil_contaminated_sediment__b1bb8113.yaml`
- Started UTC: 2026-10-04T22:11:48Z
- Finished UTC: 2026-10-04T22:16:03Z
- Verdict: needs curation

## Target

Entire generated HabitatRecord habitatmech:GOLD.7c79bcbca8, Oil-contaminated
sediment, AQUATIC/NARROW/REVIEWED. It has two parents, one GOLD attestation
with one ORGANISM assertion and two history events. Definition, synonyms,
taxa, parameters, xrefs, evidence, graphs, discussions and datasets are absent.
`data/habitats/PATHS.tsv:2206` pins the current stem.

The exact source is Environmental > Aquatic > Marine > Intertidal zone >
Oil-contaminated sediment. This is the sediment source, not the separate
Intertidal zone > Oil-contaminated water interpretation or either offshore
or coastal same-label sediment record.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/oil_contaminated_sediment__b1bb8113.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/oil_contaminated_sediment__b1bb8113.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Shared batch PASS: 1,179 canonical, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | Shared PASS: 953 ungrounded records, 1,810 decisions. |
| `just qc` | Shared run terminal PASS: 457 tests passed, three skipped, two dependency warnings in 530.76 seconds; all remaining quality gates passed. |
| Source/reference checks | Entire target, actual resolution and full generated-field equality, all 14 raw tables, typed/current ENVO comparisons, attempted current GOLD lookup, full rendered page and semantic comparisons. |

Full construction reproduces every field, with one contributing source and
one reviewed source. Whole-run QC includes 90 valid history files, 3,206
strict-valid records, 32 valid causal overlays, curation floor, byte-exact
corpus reproduction, current site/redirect/term-request products and report.
These checks prove reproducibility, not that sediment is a kind of seawater.
Earlier reports correctly retain their earlier, still-running QC observations.

## Identity and Grounding

Actual minting reproduces habitatmech:GOLD.7c79bcbca8. The default
gold_unmatched resolution is UNGROUNDED. ITEM GROUND_AS_PARENT at
curation/decisions.tsv:738, dated 2026-08-13, retains that minted identity,
adds ENVO:00002149 sea water and yields NARROW/skos:narrowMatch. Its rationale
calls this intertidal water despite the sediment head noun in its own exact
path. Generated history faithfully repeats that wrong material interpretation.

The maintained inventory identifies gold.ecosystem:7144. Its
[current GOLD OLS endpoint](https://www.ebi.ac.uk/ols4/api/ontologies/gold/terms/https%253A%252F%252Fw3id.org%252Fgold.path%252F7144)
returned HTTP 404. This limits current source verification; it does not prove
the committed source is invalid or retired. Do not copy active node 4020's
non-sediment intertidal annotations or node 4007's offshore sediment evidence
onto this source.

Current [ENVO:00002149 sea water](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002149)
is marine-process-influenced water, not a sediment genus. Current
[ENVO:03000033 marine sediment](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A03000033)
is an active sediment class with named parent ENVO:00002007. It is a material-
genus candidate consistent with this marine sediment path, not exact identity
with the oil-contaminated intertidal qualification.

Current [ENVO:00002115 petroleum enriched sediment](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002115)
is another active candidate, with named parent ENVO:00002202 organically
enriched sediment. It requires petroleum-specific scope; the label alone
does not prove oil composition or establish exact equivalence. Compare these
existing candidates rather than relying on the old soil-only rationale.

The independent parent habitatmech:GOLD.115edc36f8 is Intertidal zone, whose
entire record and actual resolution were inspected contextually in this
batch's first review. Its ENVO:00000316 parent is a geographic shore/seabed
zone between tidal marks. Intertidal location does not make sediment a subtype
of that zone. seed.py:898-907 adds the resolved GOLD parent path independently
of the curated seawater genus. Fixing one route will not fix the other.

Finally, source and retained record denote the same minted concept, while
seed.py:554-566 derives NARROW/narrowMatch against the ontology parent and
lines 890-891 copy the predicate into the attestation. Schema lines 317-322
describe source-to-record endpoints, with omission for source identity;
GroundingStatusEnum at 776-790 likewise compares record versus source.
This is the shared #1398 application-contract defect, not a formal SKOS
self-link contradiction or something a global predicate swap can resolve.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:950` records depth five, one node 7144,
one organism and zero study/biosample counters. The emitted count/unit are
faithful and must not become sample counts or characteristic-taxon evidence.
The complete exact-path/source-ID scan covered all 14 raw TSV inventories.
No exact-path biosample, triad, study, taxon or environmental-parameter
contribution was found, including ignored inputs in the bounded searches.

The inventory exposes no original organism or study accession for this row,
so organism-specific ecology and the original oil exposure remain unverified.
Neighboring water and offshore sediment paths have other counts and study
memberships; none is evidence for this exact source. There are no target
literature citations, snippets or causal assertions to validate.

The entire rendered page was inspected. It accurately repeats the one-
organism attestation, both unsupported parents and the water rationale.
That establishes propagation, not independent scientific support.

## Completeness

Ignored-inclusive ID, exact path, label/stem and filename searches covered
curation, conf, history, research, reports, all raw inventories, PATHS and
RETIRED. The exact target has the existing decision, path lock and raw GOLD
row, but no located target-owned definition, causal overlay, session history,
retirement or prior individual review. Other oil-contaminated records are
distinct source concepts, not duplicates merely because labels coincide.

Optional measurements, mechanisms and taxa should remain empty without
source-specific evidence. A future authored definition, if needed, belongs
in curation/term_requests.tsv after comparing existing sediment genera.
iModulonDB is inapplicable without gene/regulator/expression claims. Empty
synonyms do not support a synonym-scope finding.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | ITEM curation treats an explicitly sediment source as seawater in both parent and rationale. | Existing curation/decisions.tsv:738; any supported authored definition belongs in curation/term_requests.tsv. |
| Major | Independent GOLD nesting promotes geographic intertidal context into a strict sediment parent. | Governed source-specific parent control and src/habitatmech/seed.py:898-907. |
| Major | Parent comparison is emitted into the source-to-record predicate/status contract. | Schema, decision resolver and consumers under #1398. |

Counts: zero blockers, three major, zero minor. Preserve source identity,
sediment label and organism provenance; correct claims about its parents.

## Recommended Edits

1. Re-curate the existing ITEM decision as sediment. Compare marine and
   petroleum-enriched sediment using exact source evidence; retain the minted
   qualified identity unless equivalence is established, and replace the false
   water genus/rationale without rewriting historical source inventories.
2. Suppress only this independent geographic GOLD path-parent contribution.
   Add a regression proving a supported sediment genus survives while both
   false parents disappear. Do not remove all source hierarchy.
3. Include this curated GROUND_AS_PARENT witness in #1398's endpoint repair.
   Preserve historical events, append new curation history, and regenerate
   through maintained inputs rather than editing generated YAML/pages.

## Follow-up Checks

Dry seed and inspect `just seed-canary habitatmech:GOLD.7c79bcbca8 --force`
before guarded full regeneration without partial prune. Require candidate-
scope, parent-retention and explicit-endpoint regressions; ordinary/strict,
products/history/provenance checks; exact reproduction and full QC.

Actual full-context comparisons show removal of the intertidal parent and
an illustrative replacement of both parents with ENVO:03000033 each change
semantic text. Predicate-only removal is neutral. A real parent/definition
repair needs genuine map/site rebuilding under #1217. Preserve protected
draft #1218 and runtime pins, and audit actual SSSOM/KGX before compatibility
claims. All semantic probes were in memory and made no corpus changes.

## Additional Notes

All-state exact-key/node issue search returned no matching issue; earlier
oil-contaminated-sediment searches were also checked. #1398 owns the shared
contract separately from the two scientific parent defects. Current ENVO
comparisons use the typed official OWL and fresh batch OLS observations;
OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No scientific input, generated artifact, old report/history, paid research
or GitHub item was changed by this individual review.
