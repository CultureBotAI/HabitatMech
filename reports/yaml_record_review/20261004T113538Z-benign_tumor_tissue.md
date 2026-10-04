# YAML Record Review: Benign tumor tissue

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/benign_tumor_tissue.yaml`
- Started UTC: 2026-10-04T11:30:00Z
- Finished UTC: 2026-10-04T11:35:38Z
- Verdict: needs curation

## Target

The complete generated HabitatRecord was read: `habitatmech:GOLD.5f05ab4527`,
Benign tumor tissue, HOST_ASSOCIATED, NOT_APPLICABLE, REVIEWED. It has one
source parent, one uncounted GOLD attestation and two curation events. It has
no definition, synonyms, xrefs, taxa, parameters, evidence objects, graphs,
datasets or discussions.

The actual `mint` of Host-associated > Mammals > Tumor > Benign tumor tissue
reproduces the identifier. `PATHS.tsv:1987` pins the stem. This explicitly
tissue-named mammalian source is not the separate human Benign tumor grouping,
a cell line, or an identity limited to human breast tissue.

## Validation

- `just validate data/habitats/host_associated/benign_tumor_tissue.yaml`:
  PASS, no issues.
- `just validate-strict data/habitats/host_associated/benign_tumor_tissue.yaml`:
  PASS, one file, zero errors.
- `just validate-products`: PASS in this unchanged-corpus session,
  1,179 canonical pairs, one synonym, five exceptions and 2,054 no-adapter
  skips. The minted identity is outside the configured ontology label surface;
  the tissue comparison term was separately checked against current OLS.
- `just worklist --status all --limit 5`: PASS, 953 ungrounded records and
  1,810 decisions. Target and parent ITEM rows were read independently.
- `just qc` is not yet terminal at report completion. Tests passed: 457 passed,
  three skipped, two dependency warnings, 850.33 seconds. Lint, documentation,
  provenance, 90 history records, all 3,206 strict schema records, 32 overlays,
  curation floor, exact corpus reproduction, site, 231 redirects and 109 emitted
  term requests passed. Site checking examined 123 term requests. The final
  corpus-report step is still running; full terminal QC success is not claimed.
  Log: `/private/tmp/habitatmech-bcp-qc-20261004.log`.
- Actual full-context `semantic_text` changes if the current parent is removed.
  This was a read-only diagnostic, not a scientific correction.

## Identity and Grounding

`curation/decisions.tsv:582` is ITEM NOT_APPLICABLE, dated August 12,
using the generic disease/intervention/artifact/filler rationale. The emitted
mapping status and both history events reproduce that input accurately.
The substantive question is whether that rationale fits an explicit tissue
source, not whether an ITEM row exists.

Current [NCI tumor terminology](https://www.cancer.gov/publications/dictionaries/cancer-terms/def/tumor)
identifies physical abnormal tissue masses, which can be benign or malignant.
The source's explicit tissue label therefore needs assessment as material,
not automatic exclusion as a diagnosis. This does not prove that every tumor
is colonized, or that this zero-assertion GOLD node has a recoverable specimen.

Current official OLS confirms active UBERON:0000479, tissue, and its
multicellular-anatomical-structure definition. It is a broad comparison
candidate, not an exact identity for specialized benign tumor tissue. A
complete exact-label/synonym scan of all 13,604 vendored terms found no exact
Benign tumor tissue match. No absence from all ontologies is claimed.

The full `tumor.yaml` parent was read: `habitatmech:GOLD.0193e22ae0`,
Tumor, itself ITEM NOT_APPLICABLE via `curation/decisions.tsv:107`, without
an authored physical-habitat definition. Source nesting supplies it through
`src/habitatmech/seed.py:898-907`. A tissue specialization could fit a suitably
defined tumor-tissue genus, but the current excluded parent is not validated
as a broader habitat just by its source position. Parent consistency must be
resolved alongside the child's physical-versus-diagnostic interpretation.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:2133` contains the exact depth-four path,
nodes 7621/7622, and zero organism, study, biosample and total assertions.
The first ID and two-node note are copied correctly. Omitting a positive
count is correct; zero retained counts are not proof of non-habitat identity.

All 14 raw TSVs were structurally scanned for the exact mint/path, including
study-list members and extra-column values. Only the tree row matched. No
exact target bulk-biosample, study, triad or other-source association was
found. Data from the human benign-tumor subtree were not transferred here.
Current OLS GOLD-filter searches for the label and full path returned no
hits; current exact-node metadata remains unverified, not proven retired.

The original [breast-tissue study](https://pmc.ncbi.nlm.nih.gov/articles/PMC9965790/),
PMID:36836409, DOI:10.3390/jpm13020174, was inspected through official
Europe PMC XML, including collection, processing and sample-group sections.
It analyzes eight benign-group breast tissue samples from women with benign
tumors, separately from malignant and adjacent-normal groups, using 16S DNA
sequencing with negative controls. This supports a physical sampling context.
It is not proof of viable intratumoral bacteria, every benign neoplastic
tissue, all mammalian hosts, or this exact GOLD source. No taxon, abundance,
cohort count, causality or clinical recommendation is imported into the record.

The [GOLD classification guide](https://gold.jgi.doe.gov/ecosystem_classification)
frames paths as collection surroundings. It supports re-examining tissue
scope, but is not specimen-level evidence or a reason to merge distinct paths.

## Completeness

Ignored-inclusive ID, label, stem and exact-path searches covered curation,
history, research, existing review reports, PATHS, RETIRED and raw inventories.
They found the ITEM decision but no target definition request, overlay,
separate history ledger, individual research/prior review or retired URL.
The immediately preceding Benign tumor review mentions this distinct source
for comparison; that mention was not counted as its individual review.

The lack of optional taxa, parameters or mechanisms is appropriate without
exact supporting inputs. No gene, locus, regulator or expression dataset is
asserted; iModulonDB is not applicable. Missing a separate legacy ledger is
not independently a blocking history defect.

## Findings

- **Major (1): unsupported non-habitat disposition for an explicit tissue
  source.** The generic rationale does not explain why this material identity
  should be treated as a disease or artifact rather than physical habitat
  tissue. Owners: `curation/decisions.tsv:582`, a supported definition in
  `curation/term_requests.tsv` if warranted, and reviewed parent/source handling.
  Tracked in [#1376](https://github.com/CultureBotAI/HabitatMech/issues/1376).
- Blockers: 0. Minors: 0. The excluded parent is a coupled consistency check,
  not a second unsupported claim that benign tissue cannot specialize a
  tumor-tissue genus. No source-ID, copied-count or status-generation defect
  was found.

## Recommended Edits

1. Reassess the exact tissue/material versus diagnosis/artifact interpretation.
   If retained as a habitat, author a reviewed scope and supported genus while
   preserving the specialized mint. If exclusion remains, supply a specific
   source rationale that addresses the tissue label; zero counts alone do not.
2. Reconcile the exact Tumor parent with the chosen scope. Preserve source
   breadcrumbs and both source IDs; do not accept an excluded node as a habitat
   genus without reviewing it, or globally delete source-parent contributions.
3. Do not narrow all mammals to human breast specimens, merge the separate
   human Benign tumor category, ground exactly to generic tissue, import study
   taxa, hand-edit generated records/pages, or rewrite old history.

## Follow-up Checks

Test exact source identity, reviewed disposition, parent consistency and
unchanged source-count semantics. Append history for actual edits, canary/
reseed, re-read the target and require strict schema, ontology correspondence,
provenance, history, exact corpus reproduction, site and full QC.

The actual current semantic text includes `broader habitat: Tumor`; removing
it changes text. Any definition/label alternative also needs a comparison of
real full inputs. Text-changing repairs require the governed map/site rebuild
under OPEN #1217, not fabricated hashes or weakened freshness. Protected
draft #1218 remains unchanged.

## Additional Notes

All 517 returned open/closed issue bodies were screened. Exact target-ID
title/body/comment search returned zero; the exact label search returned only
#1375, whose body and returned comments were inspected. That issue explicitly
concerns the different human grouping and does not own this tissue decision.

The publisher browser request returned HTTP 429. Official Europe PMC core
metadata and XML succeeded; search excerpts were not used as the source for
the study's sample-scope claims. Only this new report was added. Scientific
inputs, generated records/pages and curation status are unchanged; #1376
remains open and unimplemented.
