# YAML Record Review: Cosmetic Product

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/cosmetic_product.yaml`
- Started UTC: 2026-10-08T05:41:54Z
- Finished UTC: 2026-10-08T05:44:05Z
- Verdict: pass with minor issues

## Target

Read the complete generated HabitatRecord `ENVO:00003893` at
`8f8453fde62d9eacf305cb781c6104f9fc181936`. It is ENGINEERED / EXACT /
REVIEWED and denotes a cosmetic product, not the factory, manufacturing
process, human skin or a particular formulation. It has an ENVO definition,
one exact plural synonym, two parents, one GOLD attestation and two events.
Parameters, taxa, literature evidence, graphs, discussions and datasets are empty.

## Validation

Fresh `UV_CACHE_DIR=build/uv-cache just validate
data/habitats/engineered/cosmetic_product.yaml` passed; fresh
`just validate-strict data/habitats/engineered/cosmetic_product.yaml` reported
one file and zero errors. Full read-only `build_corpus` / `build_document`
comparison reproduced every field, one source concept and one reviewed source.
Executed default and curated resolution with complete ontology, normalized
mapping and both claimant indexes; mint recomputation and `PATHS.tsv:720` agree.

Fresh session-wide checks, reused rather than rerun per target: `just
verify-corpus` reproduced all 3,207 records; `just validate-history` validated
171 histories; `just provenance-check` passed 14 inventories/two GOLD sources;
`uv run pytest tests/test_corpus_integrity.py -q -k 'parent or reviewed_records
or history or causal_edges_reference'` passed six existing parent/status/reference
tests, with 33 deselected. `just validate-products` using
`OAKLIB_HOME=$PWD/build/oak-current-20261008` passed 1,177 canonical pairs,
one synonym and five unchanged exceptions, with 2,057 no-adapter skips.

Full QC is reused from exact-baseline native queue
[37732242717](https://github.com/CultureBotAI/HabitatMech/actions/runs/37732242717):
578 tests passed, three skipped, all offline gates passed. It was not repeated
for report-only additions. No standalone literature-reference check applies
to this citation-free record. Original GOLD source-count re-extraction could
not run without the original source payloads in the bounded local search.

## Identity and Grounding

Source mint `habitatmech:GOLD.0792bc5bfe` belongs to the exact path
`Engineered > Industrial production > Chemical products > Cosmetic products`.
Default resolution is `gold_unmatched`, UNGROUNDED. The ITEM GROUND decision
at `curation/decisions.tsv:141` produces `curated_ground_from_gold_unmatched`,
ENVO:00003893, EXACT/skos:exactMatch and reviewed true. This mapping compares
the source concept with the ontology-grounded record, unlike the retained-mint
narrow-match defect elsewhere. One of one ITEM decisions explains REVIEWED.

The source plural and canonical singular denote the same product category
in this path; keeping the original label as an exact synonym is appropriate.
They are not literally equal strings, however, and `norm_label` does not
singularize. The actual unmatched default is evidence against the decision
note's claim of literal lexical equality, not against the semantic grounding.

ENVO:00003074, manufactured product, is the explicit ontology parent at
`ontology_subclass_edges.tsv:5526` and the genus of the definition. It resolves
in the ontology slice; an ontology parent need not have a separate emitted
HabitatRecord. ENVO:2000000, chemical product, is contributed separately by
the GOLD parent path. Its complete `chemical_product.yaml` record was read.
The two product-level parents are compatible with this explicitly formulated,
chemical-product source category; the second is source-supported, not a
subclass axiom asserted by the local ENVO slice. No formulation-specific
composition or microbial property follows from it. The manufacturing-context
parent already excluded from the chemical-product record must not be restored.

## Evidence

An exact-field/pipe-member scan of all 14 raw TSVs found the target's source
row at `gold_ecosystem_paths.tsv:1309`: depth four, nodes 8328 and 8329, and
zero organism/study/biosample/total counters. The attestation's first-node
display, two-node note and omitted count/unit reproduce that row. No exact
target biosample, study, triad, taxon or environmental-parameter inventory row
was found. The parent chemical product's ten ORGANISM assertions belong to
the parent, not to this target. Zero counters do not establish sterility.

Fresh official OLS metadata verifies active
[cosmetic product](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00003893),
[manufactured product](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00003074)
and [chemical product](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A2000000),
with labels and definitions agreeing with the slice. The cosmetic definition
still contains the phrase "to modifying" in both current source and generated
record. This is inherited editorial text, not local serializer corruption.

Individual GOLD node URLs were inaccessible. The current
[classification workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths)
confirms node 8329 and this exact path at row 306, with a final Unclassified
filler. It does not independently verify historical node 8328 or source counts.
Download: 84,174 bytes; SHA256
`f8e4cb5cf89ecc88d3cf28170cfc3a1cf47daed8218408a52914c53667dfd3d4`.
No recipe, contamination organism, preservative mechanism or safety claim is
inferred from a generic product category.

## Completeness

Ignored-inclusive exact-ID, source-mint, label, stem, path and node searches
covered maintained curation, raw inventories, path/retirement registries,
configuration, tests, docs, history, research, its manifest and prior reviews.
They found the decision, ontology/source rows and face-cream subclass, but no
target-owned authored definition, exclusion, overlay, research entry,
retirement or earlier individual review. The subclass is not equivalent to
all cosmetics and is not a reason to narrow this record to face cream.

The session's ignored-inclusive search of `build`, `data/raw` and configured
kg-microbe `data` found no original GOLD node/edge dumps, goldData.xlsx or
biosample-sweep intermediate; a current OAK BTO cache exists. Optional absent
biology is not a defect. iModulonDB is not applicable without a named organism,
gene, regulator, pathway or expression claim.

## Findings

Zero blockers, zero major findings, two minor findings.

1. **Minor: inherited definition grammar.** The definition says "to modifying"
   rather than "to modify". Current official ENVO metadata has the same typo.
   Owner: upstream ENVO definition and a governed ontology-definition refresh,
   not the generated YAML or the label-only refresh plan.
2. **Minor: inaccurate lexical rationale.** The ITEM decision and generated
   event claim literal label equality, although GOLD says `Cosmetic products`
   and ENVO says `cosmetic product`; default matching demonstrably fails.
   Owner: the target's maintained `curation/decisions.tsv` note. The semantic
   equivalence and ITEM-backed lifecycle remain defensible.

## Recommended Edits

Correct the definition upstream and import it through a reproducible governed
refresh that includes definitions. Do not silently edit generated text,
manually change inventory checksums or misuse the label-only refresh mechanism.
Clarify the maintained decision rationale as an item-level singular/plural
equivalence judgment, preserving the source label and exact mapping. Record
future curation with an append-only session history; do not rewrite a published
review or directly mutate the generated history.

## Follow-up Checks

Verify the refreshed primary definition and source receipt; regress exact
source/record endpoints, the plural synonym, both parent contributions,
zero-count omission, two historical nodes and REVIEWED derivation. For an
authorized change, dry-seed, inspect a canary and run strict, history,
provenance, label, full reproduction and QC gates. Product/model compatibility
is outside this individual review; no SSSOM/KGX readiness claim is made.

## Additional Notes

Only this new report was added for this target. No scientific input, generated
record/page, history/status, GitHub item or paid research changed. No
delegation was used. The workbook was parsed in memory after resetting its
incorrect A1-only dimensions. Contextual parent and child reads do not count
as additional completed record reviews.
