# YAML Record Review: Dairy processing facility

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/dairy_processing_facility.yaml`
- Started UTC: 2026-10-08T07:53:45Z
- Finished UTC: 2026-10-08T07:57:20Z
- Verdict: pass

## Target

Read the complete generated HabitatRecord `habitatmech:GOLD.b69e4553bb` at
`85ff7e88ff35ba5c42604d9ad46709a911875e78`. Its exact GOLD path is
`Engineered > Built environment > Dairy processing facility`.
It is ENGINEERED / UNGROUNDED / SEEDED, with one parent, one GOLD attestation
and two history events. Definition, synonyms, xrefs, parameters, named taxa,
literature evidence, graphs, discussions and datasets are absent.

This pass assesses the fidelity and defensibility of the seeded source
representation. It is not an ITEM grounding decision or a declaration that
the original samples and every possible ontology candidate have been resolved.

## Validation

Fresh `UV_CACHE_DIR=build/uv-cache just validate
data/habitats/engineered/dairy_processing_facility.yaml` passed.
Fresh `just validate-strict data/habitats/engineered/dairy_processing_facility.yaml`
reported one file and zero errors. Read-only `build_corpus` / `build_document`
reproduced every field: one source concept, zero item-reviewed sources.
Default and curated GOLD resolution were executed with complete ontology,
normalized mapping, leaf-claimant and composed-claimant indexes.

Fresh session-wide checks were reused: `just verify-corpus` reproduced all
3,207 records; `just validate-history` validated 176 sessions;
`just provenance-check` passed 14 inventories/two GOLD sources; and
`uv run pytest tests/test_corpus_integrity.py -q -k 'parent or reviewed_records
or history or causal_edges_reference'` passed six existing tests, 33
deselected. The selection is not an additional generated-history test.

Full QC and label correspondence were not repeated for report-only changes.
The exact baseline passed native-queue
[QC](https://github.com/CultureBotAI/HabitatMech/actions/runs/37743657081) and
[label correspondence](https://github.com/CultureBotAI/HabitatMech/actions/runs/37743657069),
plus full preceding local QC: 581 tests passed, three skipped, all gates passed.
The local label gate passed 1,177 canonical pairs, one synonym and five
existing exceptions, with 2,057 explicit no-adapter skips. Neither label
matching nor reproduction proves habitat scope or sample ecology. Original
GOLD re-extraction and independent study metadata verification were unavailable
within the bounds below. No standalone literature-reference check applies to
the citation-free target.

## Identity and Grounding

The mint recomputes from the exact source path, and `PATHS.tsv:2629` agrees.
Default resolution is `gold_unmatched`, UNGROUNDED, with no mapping predicate
or extra parent. The CLASS `CONFIRM_UNGROUNDED` decision at
`curation/decisions.tsv:1032` retains this identity through
`curated_confirm_ungrounded_from_gold_unmatched`. CLASS screening does not
count as ITEM review; SEEDED and both generated history events are correct.
The absent mapping predicate does not conceal a claim to an ontology identity.

The sole parent, `mesh:D000076624`, is supplied by the independent GOLD
parent-path pass. The entire contextual `built_environment.yaml` was read.
Its separate 282 ORGANISM assertions are not transferred to the target.
Primary [NLM descriptor metadata](https://id.nlm.nih.gov/mesh/D000076624.json)
confirms active Built Environment and identifies preferred concept M000622402.
The [preferred concept scope](https://id.nlm.nih.gov/mesh/M000622402.json)
covers constructed physical elements, including buildings and infrastructure.
A dairy-processing facility fits that broader constructed-environment class;
this is not a material-to-location substitution. The target's edge comes from
GOLD, not an asserted NLM subclass axiom. Reading the parent is not a separate
completed review or blanket endorsement of its own hierarchy.

Current [official ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl)
was inspected for nearby candidates. ENVO:00003862 dairy requires a building
where milk is harvested, optionally processed, while its comment acknowledges
regional terminology differences. The GOLD source name does not establish
milk harvesting at every processing facility. ENVO:03501296 cheese processing
plant is product-specific; ENVO:00003967 creamery is a component for separating
cream. Neither is an exact general dairy-processing identity. ENVO:01000536
factory and ENVO:03501295 processing plant are broader candidates requiring
source-scope assessment, not exact substitutions. These inspected candidate
classes have no deprecation assertion. Keeping the source mint avoids guessing
among facility, component, farm and food-product meanings.

## Evidence

An exact-field/pipe-member scan of all 14 raw TSV inventories found:

- `gold_ecosystem_paths.tsv:184`: depth three, nodes 5713/5714/5715,
  110 ORGANISM assertions and zero study/biosample tree counters.
- `gold_path_biosamples.tsv:782`: four BIOSAMPLE observations for node 5715.
- `gold_studies.tsv:3812`: Gs0153900 associated with two paths, this facility
  and the distinct modeled Simulated communities (microbial mixture) category.

The source count/unit, first-node display and three-node note reproduce the
classification inventory. Four biosamples are not four additional organisms,
and a multi-path study is not independent replication or an assertion that a
physical facility is a simulated community. No exact target triad, named-taxon
or environmental-parameter row was found. The aggregate does not identify
110 species, facility prevalence, a processing regime or a microbial mechanism.

The current [GOLD classification workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths)
confirms node 5715 at `site data` row 192 with the exact target path and two
trailing Unclassified fillers. It does not independently verify historical
nodes 5713/5714 or the original organism counts. Workbook: 84,174 bytes;
SHA256 `f8e4cb5cf89ecc88d3cf28170cfc3a1cf47daed8218408a52914c53667dfd3d4`.

The primary [GOLD study page](https://gold.jgi.doe.gov/study?id=Gs0153900)
was inaccessible through the browser, and an exact-accession search returned
no usable result. Its identifier and two-path membership remain backed by the
committed inventory, not independently inspected original sample metadata.
The neighboring dairy PREGO record's 15 taxa are not evidence for this distinct
GOLD source and were not imported into the assessment.

## Completeness

Ignored-inclusive searches for the mint, exact path, label, stem and source
nodes covered curation, raw inventories, the habitat corpus and path/retirement
registries, configuration, docs, tests, history, research, its manifest and
previous reports. They found the maintained CLASS decision and source rows,
but no target-owned authored definition, parent exclusion, overlay, research
entry, session history, retirement, descendant record or previous individual
review. These are bounded search results, not proof of worldwide absence.

Ignored-inclusive filename traversal of `build`, `data/raw` and the configured
kg-microbe `data` tree found no original GOLD node/edge dumps, goldData.xlsx
or biosample-sweep intermediate. Public workbook availability does not replace
the frozen bulk/API inputs. Missing optional biological details should not be
filled with generic dairy literature. With no named organism, gene, regulator,
pathway or expression assertion, iModulonDB is not applicable to this target.

## Findings

Zero blockers, zero major findings, zero minor findings. None found within
the inspected scope. The record faithfully retains its source identity and
does not overstate item-level review, exact grounding, count semantics or
microbial characteristic presence.

Original study metadata and an item-level ontology/definition assessment
remain unverified. Those limits are not converted into unsupported defect
claims or a declaration that the record is fully curated.

## Recommended Edits

No corrective edit is established by this review. Preserve the source mint,
node provenance, 110 ORGANISM count, broad supported built-environment parent
and honest SEEDED status.

For a later authorized ITEM assessment, inspect original source/sample scope
and compare all relevant active facility candidates. Distinguish collection
from processing, an entire site from a component, and facility from product.
Any grounded decision belongs in `curation/decisions.tsv`; an evidence-backed
minted definition and genus belong in `curation/term_requests.tsv`. Do not
promote the existing CLASS row or request an ontology term merely because a
review report now exists, and do not hand-edit generated YAML.

## Follow-up Checks

If a future curation changes identity or hierarchy, regress exact source-path
resolution, source-to-record mapping endpoints, all three nodes, count/unit
preservation, separate biosample/study accounting and ITEM-derived lifecycle.
Add append-only session history; dry-seed and inspect a canary; run strict,
provenance, history, label, reproduction and full QC gates. Identity/URL
changes additionally require post-commit redirect handling and site rebuilding;
semantic text changes require full-context map comparison and affected-artifact
refresh. This review does not certify SSSOM/KGX or current kg-microbe readiness.

## Additional Notes

Only this new target report was written. No scientific inputs, generated
records/pages, statuses, histories or GitHub items changed. No paid research
or delegation was used. Browser access to GOLD/NLM failed; primary workbook
and JSON were parsed in memory through HTTPS. Workbook dimensions were reset
before row traversal. Fresh ENVO OWL: 9,614,229 bytes; SHA256
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
