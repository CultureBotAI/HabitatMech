# YAML Record Review: Drugs/Supplements

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/drugs_supplements.yaml`
- Started UTC: 2026-10-08T10:22:58Z
- Finished UTC: 2026-10-08T10:25:18Z
- Verdict: pass with minor issues

## Target

Read the entire generated HabitatRecord habitatmech:GOLD.52b1824f90 at
`ff2ba9a9b5e5f36fecfa5e74aec1962a8b46ccda`. It is the depth-three
GOLD Drugs/Supplements bin, ENGINEERED / UNGROUNDED / SEEDED, with one
Drugs production parent, one GOLD attestation, a CLASS decision event and
a seeding event. Definition, synonyms, xrefs, named taxa, parameters,
evidence, graphs and datasets are empty. The slash is retained as source
wording, not split into two newly asserted identities.

## Validation

Fresh commands used `UV_CACHE_DIR=build/uv-cache`:

- `just validate data/habitats/engineered/drugs_supplements.yaml`: no issues.
- `just validate-strict data/habitats/engineered/drugs_supplements.yaml`:
  one record, zero errors.

Read-only `build_corpus` / `build_document` exactly reproduced all fields:
one source concept and zero ITEM-reviewed sources. Actual target and parent
default/curated routes were executed with complete ontology, mapping and
claimant indexes. Fresh shared corpus/history/provenance gates passed:
3,207 records reproduce, 180 histories are valid, and 14 inventories plus
two GOLD sources have current provenance. No scientific input changed
between those checks and this review.

Full QC was not repeated for report-only edits. The exact baseline tree
passed full local QC (582 passed, three skipped, all gates) and native-queue
[QC](https://github.com/CultureBotAI/HabitatMech/actions/runs/37760786908)
and [labels](https://github.com/CultureBotAI/HabitatMech/actions/runs/37760786916).
These checks do not recover original organism records or adjudicate every
source-parent meaning. Original GOLD re-extraction was unavailable within the
bounds below. No standalone literature-reference validator applies to the
record's empty citation slots; the primary example used in this review was
read directly through open full-text XML.

## Identity and Grounding

`PATHS.tsv:1892` pins the filename and the canonical path reproduces the mint.
The automatic route is `gold_unmatched`; the CLASS CONFIRM_UNGROUNDED row
at `curation/decisions.tsv:527` produces
`curated_confirm_ungrounded_from_gold_unmatched`. It adds no ontology
identity, mapping predicate or ITEM approval. The generated caveat and
SEEDED status correctly retain the unassessed source scope.

Read the complete actual parent `drugs_production.yaml`,
habitatmech:GOLD.7e78e4fa2a, and executed its same unmatched/CLASS-confirmed
route. Its immediate source-path contribution is the target's only parent;
no ontology or authored definition establishes an independent genus.

The inspected [GOLD classification guidance](https://gold.jgi.doe.gov/ecosystem_classification)
explains ecosystem types as broad groupings within categories of sampled
environments. That supports retaining the source bin, but does not resolve
whether its member observations concern finished product matrices,
production surroundings, or both. No specific drug, facility, probiotic or
vaccine ontology identity is currently overclaimed. A bounded label/synonym
search over the committed ontology slice and subject-label search over the
isolation-source mapping table found no drug/supplement/probiotic/vaccine
candidate; this is not a global ontology-absence claim.

## Evidence

Exact-field/pipe-member scanning of all 14 raw TSVs found only
`gold_ecosystem_paths.tsv:778` for the target keys. It gives nodes 8294,
8295 and 8296, two ORGANISM assertions, zero tree study/biosample counters
and total two. First-node display, three-node collapse note, count and unit
agree. These are not two named taxa, products, patients, samples or
independent prevalence observations.

The current [GOLD workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths),
parsed earlier in this session, confirms node 8296 at `site data` row 240
with Engineered / Drugs production / Drugs/Supplements and Unclassified
fillers. Adjacent rows 239 and 241 confirm the Probiotics and Vaccine child
paths; the corresponding raw rows are 1291 and 1292, each with zero tree
organism counts. These children must not be merged with the target or used
to manufacture its missing organism identities. The workbook does not
independently verify historical nodes 8294/8295 or the two assertions.

Ignored-inclusive searches found no target contribution in the biosample,
study or complete-triad inventories. There is no target accession or exact
organism record available there for primary verification.

The primary study [DOI:10.1371/journal.pone.0213841, open full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6430388/fullTextXML)
was inspected at its article metadata, abstract, product-isolation methods
and isolation results. It cultured microorganisms from commercial probiotic
supplements and beverages and distinguished intended ingredients from a
possible contaminant. This establishes that a finished supplement can be
a microbial source; it is not evidence for this GOLD bin's unnamed members
or for all drugs. No product identities, taxa, counts, laboratory growth
conditions or therapeutic claims are transferred to the record. The XML
confirms the article DOI and PMCID; browser PMC access was challenged.

## Completeness

Ignored-inclusive ID, label/stem, node and full-path searches covered the
curation tables/overlays/samples, raw inventories, corpus, path/retirement
registries, configuration, docs, tests, history, research and prior reports.
They found the CLASS decision and generated child references, but no
target-owned ITEM decision, definition request, exclusion, causal overlay,
research report, history session, retirement or prior individual review.
The parent review's contextual mention is not an earlier review of this child.

The shared ignored-inclusive filename traversal of `build`, `data/raw` and
configured kg-microbe `data` found none of the searched original GOLD node/
edge dumps, `goldData.xlsx`, `gold_biosample_triads.tsv` or biosample JSONL
intermediates. Original organism-level reconstruction remains unavailable,
not disproved. No record gene, regulator, organism or expression claim makes
iModulonDB applicable. Empty optional biological fields alone are not defects.

## Findings

Zero blockers, zero major findings, one minor finding.

1. **Minor: the strict parent relation has an unresolved product-versus-
   production-setting scope.** The source grouping is faithfully retained,
   but neither maintained definition nor original member evidence establishes
   how a finished drug/supplement matrix is subsumed by the production
   environment category. A broad source-environment reading remains plausible;
   this review does not establish a false edge. Owner: exact-source ITEM
   assessment in `curation/decisions.tsv`, with a supported definition in
   `curation/term_requests.tsv` if warranted, and a guarded
   `curation/gold_parent_exclusions.tsv` row only if the edge is established
   to be contextual rather than broader.

## Recommended Edits

Resolve the original source scope before changing hierarchy. Retain the
parent if Drugs production genuinely denotes a broader class of these
product-associated habitats. Exclude only the exact source contribution if
it instead describes manufacturing context, preserving any independent
future genus. Do not invent a definition to suppress the edge, automatically
call all microbes contaminants, use NOT_APPLICABLE merely because the label
names products, or equate the bin with one probiotic study.

Preserve all three nodes, verbatim source path, two ORGANISM assertions,
minted identity and honest lifecycle. No immediate scientific edit follows
solely from the uncertainty reported here.

## Follow-up Checks

Recover the original organism annotations and distinguish formulation
ingredients, contaminants, product isolates and manufacturing-environment
samples before adjudicating scope. Regress the actual unmatched/CLASS route,
node collapse, count/unit and any intended parent change without altering
Probiotics or Vaccine descendants. Later authorized curation should append
history, dry-seed, inspect a forced target canary, regenerate affected outputs
and pass schema/history/provenance/labels/corpus/site/full QC. Compare complete
semantic-map inputs before publishing a scientific change.

## Additional Notes

Only this new report was written for the target. No scientific input,
generated output, status, history or GitHub item changed; no paid research or
delegation. No SSSOM/KGX readiness claim. Primary XML was 161,990 bytes,
SHA256 `16291bfe82fcdc0649fc134d4051a15b7f54032fff67c3244cc611bf99470538`.
The session's GOLD workbook was 84,174 bytes, SHA256
`f8e4cb5cf89ecc88d3cf28170cfc3a1cf47daed8218408a52914c53667dfd3d4`.
