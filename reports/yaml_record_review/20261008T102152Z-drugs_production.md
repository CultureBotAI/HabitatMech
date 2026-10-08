# YAML Record Review: Drugs production

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/drugs_production.yaml`
- Started UTC: 2026-10-08T10:19:11Z
- Finished UTC: 2026-10-08T10:21:52Z
- Verdict: pass

## Target

Read the entire generated HabitatRecord habitatmech:GOLD.7e78e4fa2a at
`ff2ba9a9b5e5f36fecfa5e74aec1962a8b46ccda`. It represents the depth-two
GOLD Drugs production category, not an individually identified drug,
manufacturing process, production facility or probiotic strain. It is
ENGINEERED / UNGROUNDED / SEEDED, with one Engineered parent, one GOLD
attestation, one CLASS decision event and one seeding event. Definition,
synonyms, xrefs, parameters, named taxa, evidence, graphs and datasets are empty.

## Validation

Fresh `UV_CACHE_DIR=build/uv-cache just validate
data/habitats/engineered/drugs_production.yaml` found no issues. Fresh
`just validate-strict` on the same file scanned one record with zero errors.
Read-only `build_corpus` / `build_document` reproduced every field, with one
source concept and zero ITEM-reviewed sources. Actual default and curated
resolutions for the target and parent were executed using complete indexes.

Fresh session-wide `just verify-corpus` reproduced all 3,207 records;
`just validate-history` passed 180 histories; `just provenance-check` passed
14 inventories and two GOLD sources. No scientific input changed between
those checks and this review. Repository guidance is unchanged from the
previously read baseline. Full QC was not repeated for report-only edits:
the exact baseline tree passed full local QC (582 passed, three skipped,
all gates) and native-queue [QC](https://github.com/CultureBotAI/HabitatMech/actions/runs/37760786908)
and [labels](https://github.com/CultureBotAI/HabitatMech/actions/runs/37760786916).
These are reproduction/validation checks, not proof of every biological
interpretation. Original GOLD re-extraction was unavailable within the
documented bounds. No standalone literature-reference validator applies to
the empty reference slots, and no target study accession was found to verify.

## Identity and Grounding

`PATHS.tsv:2223` pins the filename; the exact full-path mint agrees with the
identifier. The automatic route is `gold_unmatched`. The CLASS
CONFIRM_UNGROUNDED decision at `curation/decisions.tsv:751` produces
`curated_confirm_ungrounded_from_gold_unmatched`, with no mapping predicate,
ontology identity or ITEM promotion. Its caveat that habitat-hood was not
individually assessed is retained in the generated history.

Read the full actual parent `engineered__900b76ad.yaml`,
habitatmech:GOLD.2acb39dd08. It represents the Engineered source root and
has the same unmatched/CLASS-confirmed route, five collapsed nodes and
68 ORGANISM assertions. Those assertions do not become this child's count.
The child parent edge comes from the immediate GOLD prefix, not an ontology
axiom or authored definition.

Freshly inspected [GOLD classification guidance](https://gold.jgi.doe.gov/ecosystem_classification)
describes paths as sampled surroundings, with Engineered covering engineered
environments and ecosystem categories grouping environments by shared
features. Inference: this production-associated category has a defensible
broad environmental interpretation within that umbrella. An activity-like
label alone does not establish a process-only identity. This does not define
one facility or product, endorse every child edge as is-a, or substitute for
an ITEM definition.

A bounded label/synonym search over all committed ontology rows found no
exact drug-production category candidate. Its pharmaceutical-ink hit is a
particular manufactured material, not an equivalent production environment.
This is not a global assertion that no appropriate ontology term exists.

## Evidence

Exact-field/pipe-member scanning across all 14 raw TSVs found only
`gold_ecosystem_paths.tsv:1290` for the target keys. It carries the exact
Engineered / Drugs production path, nodes 8293, 8373, 8374 and 8375, and
zero organism, study and biosample counters. The first-node display,
four-node note and omitted assertion count/unit are faithful. Zero source
counts are not evidence of a biologically empty environment.

The fresh [GOLD workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths)
confirms node 8375 at `site data` row 244 with that category and subsequent
Unclassified fillers. Rows 239-243 confirm the Drugs/Supplements,
Probiotics, Vaccine, Tobacco production and Snuff descendants. The committed
tree contains the same five descendant paths; only Drugs/Supplements has
a nonzero tree count, two organisms. Neither its count nor any descendant's
product properties belong on this aggregate category by inheritance.
The workbook confirms classification, not the historical identity of every
collapsed node or an original organism-level assertion.

Ignored-inclusive searches of the biosample, triad and study inventories
found no target path contribution. Numeric substring matches in unrelated
study accessions were not evidence for this category. The earlier sample
review of Tobacco production concerns that descendant, not this target.
No named taxon, parameter, mechanism or independent biological dataset was
found for the target in the inspected inputs.

## Completeness

Ignored-inclusive ID, label/stem, parent and node searches covered curation,
raw inventories, path/retirement registries, configuration, docs, tests,
history, research and prior individual reports. Beyond the CLASS decision,
no target-owned ITEM decision, term request, exclusion, causal overlay,
research report, session history, retirement or prior individual review was
found. A broad Environmental research report lists this category but is not
independent evidence about its scope. The contextual parent review is not
a completed review of this child.

The shared ignored-inclusive filename search over `build`, `data/raw` and
configured kg-microbe `data` found none of the searched original GOLD
node/edge dumps, `goldData.xlsx`, `gold_biosample_triads.tsv` or biosample
JSONL intermediates. Original source reconstruction remains unperformed;
the committed manifests verify inventory integrity instead.

No consequential missing required representation was established. An ITEM
definition could clarify which settings and matrices the category includes,
but its absence does not falsify an honestly seeded source category. No
organism, gene, regulator or expression claim makes iModulonDB applicable.
Optional biological slots should not be filled using neighboring records.

## Findings

None found: zero blockers, zero major findings and zero minor findings within
the reviewed scope. This passes the current seeded representation, not a
completed ontology definition or validation of all descendant relationships.

## Recommended Edits

No corrective edit is established. Preserve the mint, source path, four-node
collapse, broad Engineered parent, omitted zero count/unit and
UNGROUNDED/SEEDED status. Do not use NOT_APPLICABLE merely because the label
contains production, or replace the category with a drug molecule, printing
material, probiotic or one kind of factory.

If later ITEM curation is requested, inspect original source scope and
descendants before recording an assessment in `curation/decisions.tsv` and
any supported novel environment definition in `curation/term_requests.tsv`.
Retain the separation between production surroundings and individual products.

## Follow-up Checks

Any future source refresh should recheck all four node IDs and category
boundaries, without propagating descendant counts or taxa. Authorized
curation should append history, dry-seed, inspect
`just seed-canary habitatmech:GOLD.7e78e4fa2a --force`, and run strict,
history, provenance, corpus, site and full QC after regeneration. An adopted
ontology term additionally needs primary ID/label verification and the label
gate. Compare semantic-map inputs before publishing scientific edits.

## Additional Notes

Only this new report was written for the target. No scientific input,
generated record/page, status, history or GitHub state changed. No paid
research or delegation, and no SSSOM/KGX readiness claim. A guessed
`research/manifest*` shell glob did not resolve; the subsequent ignored-
inclusive search traversed the actual entire research tree instead.
The fresh GOLD workbook was 84,174 bytes, SHA256
`f8e4cb5cf89ecc88d3cf28170cfc3a1cf47daed8218408a52914c53667dfd3d4`.
