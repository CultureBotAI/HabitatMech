# YAML Record Review: Cultivation Substrate

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/cultivation_substrate.yaml`
- Started UTC: 2026-10-08T06:34:39Z
- Finished UTC: 2026-10-08T06:37:26Z
- Verdict: needs curation

## Target

Read the entire generated HabitatRecord `habitatmech:GOLD.083ab65161` at
`6f0de147db0cfa1c186620880965d227bb20eafd`. It denotes GOLD's mushroom-farm
cultivation-substrate category, not all agricultural substrates, a mushroom
organism, the farm itself, or the cultivation process. It is ENGINEERED /
UNGROUNDED / SEEDED, with one parent, one attestation and two history events.
Definition, synonyms, xrefs, parameters, taxa, literature evidence, graphs,
discussions and datasets are absent.

## Validation

Fresh `UV_CACHE_DIR=build/uv-cache just validate
data/habitats/engineered/cultivation_substrate.yaml` passed. Fresh
`just validate-strict data/habitats/engineered/cultivation_substrate.yaml`
reported one file and zero errors. Full read-only `build_corpus` /
`build_document` comparison reproduced every target field: one source concept,
zero item-reviewed sources. Mint recomputation agrees with `PATHS.tsv:1328`.
Executed default and curated resolution with complete ontology, normalized
mapping, leaf-claimant and composed-claimant indexes.

Fresh session-wide checks, reused rather than rerun per target:
`just verify-corpus` reproduced all 3,207 records; `just validate-history`
validated 172 sessions; `just provenance-check` passed 14 inventories/two GOLD
sources; `uv run pytest tests/test_corpus_integrity.py -q -k 'parent or
reviewed_records or history or causal_edges_reference'` passed six existing
parent/status/reference tests, 33 deselected. This selection is not an extra
generated-history test.

Full QC and label correspondence were not repeated for report-only changes.
The exact baseline's native queue
[QC](https://github.com/CultureBotAI/HabitatMech/actions/runs/37736853501) and
[label gate](https://github.com/CultureBotAI/HabitatMech/actions/runs/37736853478)
passed. The publication's local label gate likewise passed 1,177 canonical
pairs, one synonym and five existing exceptions, with 2,057 no-adapter skips.
Label correspondence does not establish ontology eligibility or parent meaning.
No standalone literature-reference check applies to this citation-free record.
Original GOLD re-extraction was unavailable within the searched source bounds.

## Identity and Grounding

Exact source path:
`Engineered > Built environment > Mushroom farm > Cultivation substrate`.
The default is `gold_unmatched`, UNGROUNDED, without predicate or extra
parents. The CLASS `CONFIRM_UNGROUNDED` row at `curation/decisions.tsv:143`
retains the same mint via `curated_confirm_ungrounded_from_gold_unmatched`.
It does not establish ITEM review, so SEEDED and both generated events agree
with maintained provenance. Omission of a self-mapping predicate is correct.

The sole parent, `habitatmech:GOLD.583dbbd71a`, is contributed independently
by the GOLD parent-path pass. The complete `mushroom_farm.yaml` was read;
it is itself an undefined, CLASS-screened farm category, with three historical
source nodes and zero counters. It does not define cultivation substrate as a
subtype of farm. A material used in a farm is not the entire setting.

For contextual comparison, primary
[ENVO farm metadata](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000078)
describes a land area including agricultural constructions. This distinguishes
a farm from substrate material; it is not a decision to ground the minted
mushroom-farm parent to the generic farm class or to ground this material to it.

## Evidence

An exact-field/pipe-member scan of all 14 raw TSV inventories found only the
target's classification row at `gold_ecosystem_paths.tsv:1270`: depth four,
nodes 7851 and 7852, and zero organism/study/biosample/total counters. The
first-node display, two-node note and absent count/unit reproduce that row.
No exact target biosample, study, triad, named-taxon or parameter contribution
was found. Zero counters are not evidence that the material is sterile.

The current [GOLD classification workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths)
confirms node 7852 at `site data` row 210 with a trailing Unclassified filler,
the distinct Wheat straw child at row 211/node 7853, and Mushroom farm at
row 212/node 7850. It does not independently verify historical node 7851 or
the original source counts. Download: 84,174 bytes; SHA256
`f8e4cb5cf89ecc88d3cf28170cfc3a1cf47daed8218408a52914c53667dfd3d4`.

The full child `wheat_straw.yaml`, `habitatmech:GOLD.dc36405736`, was read.
Its exact source path, zero-count attestation and separate CLASS history
support a distinct child category, not equivalence between all substrate and
wheat straw. They do not identify a cultivated fungal species or supply a
recipe, temperature, community, gene or causal mechanism for this target.

Primary [ENVO mushroom compost metadata](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00003033)
confirms that active ENVO:00003033 concerns residual compost waste from
mushroom production. Its formulation description is not evidence that every
source cultivation substrate is composted or already spent. Do not equate
this broader source bin with that candidate from the shared mushroom context.

The local slice's BTO:0000316 culture medium was also checked against current
[official BTO metadata](https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms?obo_id=BTO%3A0000316).
It is now explicitly obsolete, with a note about addition as a synonym of
culture fluid. Its historical solid-or-liquid cultivation-substance definition
does not license automatic grounding of this farm material, and a migration
to a liquid-only term would require its own scope assessment. The target is
not currently grounded to BTO:0000316; this is candidate-screening context,
not a second defect asserted in the target.

## Completeness

Ignored-inclusive searches for the exact source ID, label, stem, path and
both node IDs covered curation, raw inventories, path/retirement registries,
configuration, docs, tests, history, research, its manifest and previous
individual reports. They found the decision/source rows and contextual
parent/child records, but no target-owned definition, parent exclusion,
overlay, research entry, session history, retirement or earlier review.

The session's ignored-inclusive filename search across `build`, `data/raw`
and configured kg-microbe `data` found no original GOLD node/edge dumps,
goldData.xlsx or biosample-sweep intermediate. This is a bounded availability
limit, not global absence. Optional unfilled biology is not a defect. No
named organism, gene, regulator, pathway or expression assertion makes the
iModulonDB adapter applicable; the word mushroom is not a covered strain key.

## Findings

Zero blockers, one major finding, zero minor findings.

1. **Major: substrate material inherits its farm setting as a strict parent.**
   The generated edge to `habitatmech:GOLD.583dbbd71a` treats the whole
   mushroom-farm context as an is-a genus. The source hierarchy and wheat-straw
   child support material used in that setting, not a farm subtype. Neither
   CLASS decision supplies a contrary material definition. Owner:
   `curation/gold_parent_exclusions.tsv` for this exact GOLD contribution;
   future item-level identity/definition work belongs in
   `curation/decisions.tsv` and `curation/term_requests.tsv`.

## Recommended Edits

Suppress only this exact source-path contribution to the expected minted
mushroom-farm parent. Preserve source identity, both historical nodes, count
omissions, child separation and honest SEEDED status. A false-edge repair is
not evidence of ITEM identity review or grounds for NOT_APPLICABLE.

For a later item assessment, distinguish in-use substrate, spent material,
compost, unprocessed feedstock and the cultivated organism. Define the actual
source category and choose a supported material genus; do not invent a
definition merely to suppress the edge. Do not equate the whole bin to wheat
straw, mushroom compost, an obsolete culture-medium term or a liquid-only
replacement. Do not hand-edit generated records or import optional biology
from contextual neighbors.

## Follow-up Checks

Regress exact path/parent matching, independent GOLD parent contribution,
two-node collapse, zero-count omission, default and curated resolution,
lifecycle and the separate Wheat straw child. Authorized curation needs
append-only session history, dry seed, inspected canary, strict/provenance/
history/label/corpus checks and full QC. Compare full semantic-map inputs
after changing parent context and rebuild affected artifacts when needed.
No SSSOM/KGX or current kg-microbe model certification follows from this review.

## Additional Notes

Only this target's new report was written. Scientific inputs, generated
records/pages, lifecycle/history and GitHub remained unchanged. No paid
research or delegation was used. Primary API and workbook responses were
parsed in memory after the browser could not expose their contents. Parent
and child reads supply context, not additional completed individual reviews.
