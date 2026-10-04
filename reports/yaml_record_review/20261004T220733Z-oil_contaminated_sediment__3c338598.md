# YAML Record Review: Oil-contaminated sediment

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/oil_contaminated_sediment__3c338598.yaml`
- Started UTC: 2026-10-04T22:05:34Z
- Finished UTC: 2026-10-04T22:07:33Z
- Verdict: needs curation

## Target

Entire generated HabitatRecord habitatmech:GOLD.e6839bcc8f, Oil-contaminated
sediment, AQUATIC/NARROW/REVIEWED. It contains two water-related parents,
one GOLD attestation for four ORGANISM assertions and two history events.
Definition, synonyms, taxa, parameters, xrefs, evidence, graphs, discussions
and datasets are absent. `data/habitats/PATHS.tsv:3003` pins the stem.

The exact path is Environmental > Aquatic > Marine > Oceanic >
Oil-contaminated sediment. Preserve its sediment head noun and offshore
context; it is not the separate Oceanic Oil-contaminated water source or
same-label sediment sources from other settings.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/oil_contaminated_sediment__3c338598.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/oil_contaminated_sediment__3c338598.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Shared batch PASS: 1,179 canonical, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | Shared PASS: 953 ungrounded records, 1,810 decisions. |
| `just qc` | Active at history validation; tests passed: 457 passed, three skipped, two warnings in 530.76 seconds. No terminal whole-run result claimed. |
| Source/reference checks | Complete target, actual resolution and full generated-field equality, all 14 raw tables, current typed ENVO/OLS and GOLD, all six original-study attempts, entire page and full semantic comparisons. |

Full construction reproduces every field with one source and one reviewed
source. The wrong curation input is reproducible and schema-valid; those
properties do not make sediment a kind of seawater. Later QC completion
belongs in the publication receipt, not this earlier timestamped result.

## Identity and Grounding

Actual source minting reproduces habitatmech:GOLD.e6839bcc8f. The default
gold_unmatched answer is UNGROUNDED. ITEM GROUND_AS_PARENT at
curation/decisions.tsv:1272, dated 2026-08-13, retains the minted identifier
but adds ENVO:00002149 sea water and NARROW/skos:narrowMatch. Its rationale
calls this oil-contaminated open-ocean water even though its own path ends
in sediment. The generated history faithfully exposes this mismatch.

Current [GOLD node 4007](https://www.ebi.ac.uk/ols4/api/ontologies/gold/terms/https%253A%252F%252Fw3id.org%252Fgold.path%252F4007)
is active for the exact sediment path. It provides broad marine-biome and
local ocean annotations, marked partial, with no inspected medium/exact-match
assertion. Source label, context and the committed medium summary support
sediment, not a seawater genus. Do not repair this by renaming the record
water or deleting the sediment qualification.

Current [ENVO:03000033 marine sediment](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A03000033)
is active, describes sediment transported through the marine water column
and settling on the seafloor, and has ENVO:00002007 sediment as its named
superclass. It is present at physical ontology_terms.tsv:9589 and subclass
row 7974. This is a defensible material-genus candidate; the generic marine
term is broader than the qualified oil-contaminated offshore source.

Current [ENVO:00002115 petroleum enriched sediment](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002115)
is also active and present at ontology_terms.tsv:7211, with named parent
ENVO:00002202 organically enriched sediment at subclass row 5313. It is a
more specific candidate to compare once original oil composition/scope is
recovered, not a license to equate every oil with petroleum or erase marine
and offshore qualifications. The old soil-only rationale is not an adequate
candidate comparison for this sediment source.

The other current parent, ENVO:00000207 oceanic zone, is an off-shelf water
mass, not sediment. It is added by seed.py:898-907 from GOLD Oceanic's
reviewed exact identity. That parent route was executed independently in
the immediately preceding water-source review and has not changed. Neither
marine setting nor deposition through water makes sediment a subtype of
that water mass. Correcting the curated seawater parent alone will not
remove this independently contributed context edge.

The third defect is the shared #1398 contract. The retained source and
record identity are the same minted concept. GROUND_AS_PARENT at
seed.py:554-566 nevertheless derives NARROW/narrowMatch from comparison
with its ontology parent; lines 890-891 copy the predicate into a field
whose schema at 317-322 says source-to-record, omitted for source identity.
GroundingStatusEnum at 776-790 describes the same source/record endpoints.
The endpoint problem survives even after choosing a sound sediment genus.
It is not a formal SKOS self-link inconsistency or a global predicate-swap fix.

## Evidence

`gold_ecosystem_paths.tsv:670` gives depth five, one node 4007, four ORGANISM
assertions and zero study/biosample counters in that inventory. The emitted
attestation is faithful. `gold_path_biosamples.tsv:450` separately gives 27
bulk samples; neither number should replace or be summed with the other.

Triad rows 626-628 summarize 11 complete-triad samples and three studies:
broad ENVO:01000024 marine benthic biome, local ENVO:01000105 marine benthic
feature, medium ENVO:03000033 marine sediment. Each slot has two distinct
terms, top share 0.91 and two agreeing studies. This is strong modal support
for a benthic sediment reading, not universal agreement or three independent
replicates per slot. The nonmodal sample annotations and the 11/27 API/bulk
crosswalk are not recovered from the aggregate tables.

Current ENVO:01000024 is active. Current ENVO:01000105 is explicitly obsolete
marine benthic feature, with several consider suggestions and no single
automatic replacement asserted in the inspected response. That historical
raw local annotation is not a live record identity or parent. Preserve the
source-version distinction, do not newly ground to it, and do not hand-edit
historical inventories merely to hide the old term. Current GOLD's broad
marine-biome/local-ocean annotations differ from these older modal summaries.

Study memberships at physical rows 189, 469, 558, 744, 943 and 2636 identify
Gs0053056, Gs0090383, Gs0110103, Gs0113788, Gs0116840 and Gs0144775.
All six original study pages returned HTTP 403. Several span generic marine,
sediment, saline or mangrove contexts. Their complete experiments and taxa
were not recovered or borrowed wholesale to this exact path.

The complete structured scan covered all 14 raw tables. No PREGO, BacDive,
MADIN, named taxon or environmental-parameter contribution feeds this
target. The empty taxon list does not negate four organism assertions.
The full rendered page accurately repeats the unsupported parents and
water rationale, demonstrating propagation rather than independent support.

## Completeness

Ignored-inclusive ID, exact path, label/stem and filename searches covered
curation, history, research, conf, reports, raw inventories, PATHS and RETIRED.
Only the maintained decision and path lock were found for this exact target;
there was no target-owned definition, overlay, session history, retirement or
prior individual review. Broader oil-label searches expose separate water,
soil and sediment records, not a basis to collapse them.

Optional measurements and mechanisms remain empty without target-specific
evidence. A future definition should make the sediment genus and source
qualifications explicit through curation/term_requests.tsv if needed; do
not invent a novel term before comparing existing candidates. iModulonDB
is inapplicable without gene/regulator/expression assertions. No synonym-
scope finding applies to an empty synonym list.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | ITEM curation assigns seawater as the genus of an explicitly sediment source and calls it water in the rationale. | Existing curation/decisions.tsv:1272; any supported authored definition belongs in curation/term_requests.tsv. |
| Major | Independent GOLD nesting adds oceanic water mass as a strict parent of sediment. | Governed source-specific parent control and src/habitatmech/seed.py:898-907. |
| Major | Parent comparison is emitted into the source-to-record predicate/status contract. | Schema, decision resolver and consumers under #1398. |

Counts: zero blockers, three major, zero minor. The minted source identifier,
sediment label and four-organism provenance survive; the parent claims need
correction, not source erasure or a forced merge.

## Recommended Edits

1. Re-curate the existing decision as sediment, comparing marine sediment
   and petroleum-enriched sediment with exact source evidence. Preserve the
   minted qualified identity unless genuine equivalence is established;
   replace the false seawater genus and water rationale, not the raw source.
2. Suppress only the independent ENVO:00000207 path-parent contribution.
   Add regressions demonstrating a valid sediment genus survives while both
   water-related false parents are removed. Do not drop all source hierarchy.
3. Cover this curated route in #1398's explicit-endpoint correction. Append
   new curation history, retain prior events, source path/count/unit and
   optional-slot honesty, and never hand-edit generated YAML/pages.

## Follow-up Checks

Dry seed and inspect `just seed-canary habitatmech:GOLD.e6839bcc8f --force`,
then guarded full regeneration without partial prune. Require candidate-
scope, parent-retention and endpoint tests; ordinary/strict/products/history
and provenance checks; exact reproduction, site/redirect/term-request gates
and full QC. Inspect every affected source if any future identity changes.

Actual full-context comparison shows both removal of the oceanic parent
and an illustrative replacement of both parents with ENVO:03000033 change
semantic text. Predicate-only removal is neutral. A real parent/definition
repair needs genuine map/site rebuilding under #1217; preserve protected
draft #1218/runtime pins and inspect actual SSSOM/KGX before compatibility
claims. The illustrative in-memory probe made no corpus changes.

## Additional Notes

All-state exact-key and oil-contaminated-sediment issue searches returned
no matching issue. #1398 owns the shared contract separately from the
target's two scientific parent defects. Official typed ENVO OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No scientific input, generated artifact, old report/history, paid research
or GitHub item was changed by this individual review.
