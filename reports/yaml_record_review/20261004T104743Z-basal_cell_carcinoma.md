# YAML Record Review: Basal cell carcinoma

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/basal_cell_carcinoma.yaml`
- Started UTC: 2026-10-04T10:41:39Z
- Finished UTC: 2026-10-04T10:47:43Z
- Verdict: needs curation

## Target

The full generated HabitatRecord was read: `habitatmech:GOLD.17b7f17bc1`,
Basal cell carcinoma, HOST_ASSOCIATED, NOT_APPLICABLE, REVIEWED. It has one
source parent, one uncounted GOLD attestation and two curation events. It
asserts no definition, synonyms, xrefs, taxa, parameters, citations, graphs,
datasets or discussions.

The actual `mint` of Host-associated > Mammals: Human > Malignant tumor >
Carcinoma > Basal cell carcinoma matches the identifier. `PATHS.tsv:1450`
pins the filename. This is the cancer-class source, not a separately defined
tumor-tissue habitat, basal carcinoma cell, cell line or epidermal compartment.

## Validation

- `just validate data/habitats/host_associated/basal_cell_carcinoma.yaml`:
  PASS, no issues.
- `just validate-strict data/habitats/host_associated/basal_cell_carcinoma.yaml`:
  PASS, one file, zero errors.
- `just validate-products`: PASS in this unchanged-corpus session,
  1,179 canonical pairs, one synonym, five exceptions and 2,054 no-adapter
  skips. The minted excluded identity is not an ontology label pair covered
  by that gate; the BTO near miss was checked separately against current OLS.
- `just worklist --status all --limit 5`: PASS, 953 ungrounded records and
  1,810 decisions. Exact target/parent ITEM rows were read independently.
- `just qc`: terminal PASS. Tests: 457 passed, three skipped, two dependency
  warnings, 822.22 seconds. Lint, docs, 14-inventory/two-GOLD-source provenance,
  90 history records, 3,206 schema records, 32 overlays, curation floor, exact
  corpus reproduction, site, 231 redirects, 109 emitted term requests and
  final report passed. Site checking examined 123 term requests; that is not
  the emitted-template count. No narrower reference/history gate was invented.
- The actual full-context `semantic_text` diagnostic proves that removing
  the sole parent changes map input. Generated page and template were also
  inspected; neither was edited.

## Identity and Grounding

`curation/decisions.tsv:226` is ITEM NOT_APPLICABLE dated 2026-08-12. The
target reproduces that decision, REVIEWED status and both decision/seeding
events. This differs from the still-CLASS breast-cancer target discussed in
#482; that issue is not evidence that this target lacks ITEM review.

Current [NCI basal cell carcinoma terminology](https://www.cancer.gov/publications/dictionaries/cancer-terms/def/basal-cell-carcinoma)
identifies a skin cancer originating in the epidermis. The source's explicit
Malignant tumor > Carcinoma hierarchy is a cancer classification, supporting
the existing disease-class exclusion. This does not mean physical tumor
tissue, a sampled skin compartment or an experimentally infected cancer cell
could never be a microbial habitat. Those are different identity claims.

Current active BTO:0001298 is **basal cell carcinoma cell**, matching
`ontology_terms.tsv:1299`; BTO:0001286 is the broader skin-cancer-cell term.
The cell term is a near miss, not an exact grounding for this disease grouping.
Its inherited epidemiological prose was not adopted as a current prevalence
claim. No clinical ontology or cell term was imported as a replacement.

The complete `carcinoma.yaml` parent was read. It is also ITEM-reviewed
NOT_APPLICABLE, via `curation/decisions.tsv:901`, with identity
`habitatmech:GOLD.9bb307824f`. Current [NCI carcinoma terminology](https://www.cancer.gov/publications/dictionaries/cancer-terms/def/carcinoma)
supports the clinical subclass relation: basal cell carcinoma is a carcinoma.
This review does not dispute that relation or require reversal of either
non-habitat decision.

The representation is nevertheless inconsistent with the declared slot:
`parent_habitats` means broader habitats, not an untyped source taxonomy.
`src/habitatmech/seed.py:898-907` adds the parent from source nesting without
regard to the exclusion. The actual generated page presents Carcinoma under
Broader habitats, and the actual semantic adapter emits
`broader habitat: Carcinoma`. No exception for excluded cancer-class ancestry
was found in ignored-inclusive searches of the schema, CLAUDE, curation and
harmonization guidance. A true clinical subclass should not become a habitat
ancestry assertion merely to preserve source context.

## Evidence

| Source | Verified content and limits |
| --- | --- |
| `gold_ecosystem_paths.tsv:2325` | Exact depth-five path, node 6176, one node and zero organism/study/biosample assertions. Omission of a positive generated count is correct. |
| `gold_path_biosamples.tsv:417` | Separate bulk count of 33 biosamples for path 6176. It does not replace the tree's organism-count surface or prove microbial occupancy. |
| `gold_studies.tsv:1926` | Gs0133340 includes this path among 12 paths, including cancer groups, cell line, blood, malignant ascites and reagent blank. Other paths are not this target's sample identity. |
| `gold_studies.tsv:3099` | Gs0150275 includes this path among 16 paths. Its other tumor types, blood and colon-mucosa contexts cannot all be attributed to basal cell carcinoma. |

All 14 raw TSV inventories were structurally scanned for the exact path, mint
and basal-cell-carcinoma wording, including extra-column values. Only those
three GOLD tables and the BTO cell-term descriptions matched. No exact target
triad, BacDive, PREGO, Madin, isolation mapping or parameter row was found.
The multiple-myeloma triad in a shared study is not this target's triad.

The current GOLD path IRI 6176 returned 404. Browser retrieval of the exact
Gs0133340 and Gs0150275 pages failed, and both direct requests returned 403.
Their committed crosswalks and bulk count are verified; current study details
and individual specimen types remain unverified. Neither zero tree counts nor
failed access is biological absence evidence. No cohort-wide cell-culture,
tissue-colonization, contamination or taxon conclusion is inferred.

## Completeness

Ignored-inclusive searches of curation, history, research, review reports,
the research manifest, PATHS and RETIRED found the ITEM row but no target
definition request, overlay, separate history ledger, individual research/
prior review or retired URL. The multiple-myeloma report's contextual mention
does not count as an individual review of this record. Missing optional
fields should not be populated from a shared study's other sample categories.

The old multiple-myeloma report and closed #879 were inspected for the
corrected one-sample triad scope, not treated as primary evidence for this
target. That correction is preserved. Its broader wording about cell types
not being habitats is not adopted as a universal rule here.

No gene, locus, regulator or expression dataset is asserted; iModulonDB is
not applicable. A separate legacy history ledger is advisory, while validity
of the existing corpus history is covered by the passing full gate.

## Findings

- **Major (1): excluded cancer taxonomy is published as habitat ancestry.**
  Clinical subtype, stable source identity and existing exclusions are sound;
  presenting the parent as a broader habitat is not. Owner: maintained
  source-parent handling in `src/habitatmech/seed.py`, with governed typed
  source/classification representation or an exact-source exclusion.
  Tracked in [#1372](https://github.com/CultureBotAI/HabitatMech/issues/1372).
- Blockers: 0. Minors: 0. No unsupported new disposition reversal, false
  clinical-subclass allegation or copied-count defect is asserted.

## Recommended Edits

Separate or suppress this exact cancer-class contribution from habitat
ancestry while retaining the complete source path and cancer classification
as provenance. Keep both ITEM exclusions, target mint/node and count semantics
unless a separate source-specific review supports another interpretation.
If a structured cancer-taxonomy relation is needed, represent it explicitly
rather than through the broader-habitat slot.

Do not globally remove valid habitat parents, turn a disease into a habitat
to satisfy the current field, hand-edit generated outputs, or automatically
ground to a cell, skin or generic tumor-tissue term. No scientific correction
was made by this report.

## Follow-up Checks

Regress this target's disease-versus-habitat relation interpretation and
preserved source provenance. Append history, dry-run/canary/reseed, re-read
the target and rendered page, and run strict schema, current ontology checks,
provenance, history, exact corpus reproduction, generated-site and full QC.

The full-context diagnostic removes `broader habitat: Carcinoma` and changes
semantic text. The correction therefore requires a real map/site rebuild
under #1217's supported-runtime constraint. Protected draft #1218 remains
unmodified. Do not fake map hashes or relax freshness. Individual biosample
metadata must be recovered before making sample-level biological claims.

## Additional Notes

All 514 returned issue bodies were screened. Exact basal-cell-carcinoma
title/body/comment search returned zero; a Carcinoma/parent search returned
only #482 and closed #22. #482 concerns a different CLASS-swept cancer leaf.
#1324's excluded-quality parent issue was read, but does not already own this
specific excluded-cancer edge. #879 is a closed report-scope correction, not
an open scientific finding for basal cell carcinoma.

This is a new individual report, not an edit to old reports or history.
Scientific inputs, generated YAML/pages and curation status are unchanged.
