# YAML Record Review: distilled water

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/distilled_water.yaml`
- Started UTC: 2026-10-08T09:38:01Z
- Finished UTC: 2026-10-08T09:42:09Z
- Verdict: pass with minor issues

## Target

Read the complete generated HabitatRecord ENVO:00003065 at
`82420ea0e9e81542398c1ea1a09961ef6114c238`. It represents distilled-water
material, not a still, distillation procedure, or the water molecule. It is
ENGINEERED / EXACT / SEEDED, with two parents, one GOLD attestation and one
seeding event. Definition, synonyms, xrefs, parameters, named taxa, evidence,
graphs, discussions and datasets are absent.

## Validation

Fresh commands used `UV_CACHE_DIR=build/uv-cache`:

- `just validate data/habitats/engineered/distilled_water.yaml`: no issues.
- `just validate-strict data/habitats/engineered/distilled_water.yaml`:
  one file, zero errors.
- `just verify-corpus`: 3,207 records reproduce, with no missing, extra or
  differing files.
- `just validate-history`: 180 session histories valid.
- `just provenance-check`: 14 inventories and two GOLD sources current.

Read-only `build_corpus` / `build_document` exactly reproduces the record:
one source concept, zero ITEM-reviewed sources. Actual default and curated
GOLD resolutions were executed with complete ontology, normalized mapping,
leaf-claimant and composed-claimant indexes for target and source parent.
The review skill, checklist and relevant schema were reread; the previously
read repository/curation guidance is unchanged from the preceding baseline.

Full QC was not rerun for report-only changes. This exact baseline passed
full local QC (582 passed, three skipped, all gates) and native-queue
[QC](https://github.com/CultureBotAI/HabitatMech/actions/runs/37756389398)
and [labels](https://github.com/CultureBotAI/HabitatMech/actions/runs/37756389428).
These gates do not validate every logical source-parent claim or original
sample interpretation. Original GOLD re-extraction and live study verification
were unavailable within the bounds below. No standalone literature-reference
validator applies to this citation-free record.

## Identity and Grounding

`PATHS.tsv:715` pins the filename. The source mint recomputes to
`habitatmech:GOLD.972c5ee2d4`. It has no maintained decision; both executed
routes are `gold_leaf_label`, yielding ENVO:00003065 and skos:exactMatch.
The unreviewed route correctly leaves SEEDED. Capitalization alone does not
require a redundant source synonym.

Fresh [official ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl)
confirms active distilled water, its named superclass ENVO:00002006 liquid
water, and no IAO textual definition or typed synonym on the target class.
The empty definition is therefore reproduced source sparsity, not dropped
curation. Liquid water is an environmental material, not CHEBI:15377 molecular
identity. Local `ontology_terms.tsv:7377` and
`ontology_subclass_edges.tsv:5496` agree with this target route.

Read the entire contextual `chemical_product.yaml`. The immediate GOLD
prefix resolves by its ITEM decision from `habitatmech:GOLD.413b4cb862` to
ENVO:2000000; the independent GOLD parent pass adds that identifier here.
It is not an ENVO subclass axiom of distilled water. Current ENVO defines
chemical product as a manufactured mixture produced through chemical
engineering. The product reading is plausible, but the mixture qualification
and its applicability to the generic distilled-water class are not established
by classification membership alone. This is not proof of a false edge or of
absolute chemical purity. The parent's REVIEWED status and ten ORGANISM
assertions do not transfer to this child; its own outgoing exclusion is not
an exclusion of this incoming child edge.

## Evidence

The exact-field/pipe-member scan of all 14 raw TSVs found:

- `gold_ecosystem_paths.tsv:535`: the exact depth-four path, nodes 5911 and
  5912, nine ORGANISM assertions, and zero tree study/biosample counters.
  The first-node display and two-node collapse note agree.
- `gold_path_biosamples.tsv:363`: 45 BIOSAMPLE observations for node 5912,
  a separate bulk/API source unit, not additional organisms.
- `gold_studies.tsv:2198,3939,4172,4174`: Gs0136072, Gs0154255,
  Gs0156857 and Gs0156859 contain this exact path among respectively nine,
  two, three and three study memberships. Other paths include soil, fecal,
  strait and modeled environments; they are not equivalent to distilled water.

No target-specific taxon, parameter or MIxS-triad row was found. No organisms,
recipes, purity thresholds, sterility or growth mechanisms should be inferred
from these aggregate counts.

The fresh [GOLD classification workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths)
confirms node 5912 at `site data` row 307, with the exact Industrial
production / Chemical products / Distilled water path and an Unclassified
filler. This confirms current classification, not historical node 5911,
biological counts, sample roles or the interpretation of each source edge.
All four live study pages were attempted and inaccessible. They remain
inventory-backed accessions; no blank-versus-isolation interpretation is
invented from their heterogeneous study memberships.

The inspected [USGS water-quality FAQ, question 22](https://water.usgs.gov/owq/FAQ.htm)
distinguishes ideal chemical purity from laboratory water made nearly pure
by distillation and other treatments. It supports a processed water-material
reading without assigning exact purity or chemistry to this source bin.
The inspected [FDA high-purity-water guide](https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/inspection-guides/high-purity-water-system-793)
is explicitly dated 1993. Its engineering discussion distinguishes water,
stills and distribution systems and describes possible system contamination.
It is not used as current regulatory guidance or as evidence for any of these
nine GOLD organism assertions. No pharmaceutical water grade or microbial
limit is transferred to the record.

## Completeness

Ignored-inclusive ID, source-mint, label/stem and node searches covered
curation, raw inventories, corpus, path/retirement registries, configuration,
docs, tests, history, research, its manifest and previous reports. No
target-owned decision, definition request, exclusion, causal overlay, research
report, session history, retirement or prior individual review was found in
those bounds. The chemical-product review's child mention is not this
target's individual review.

Ignored-inclusive filename traversal of `build`, `data/raw` and the configured
kg-microbe `data` tree found no GOLD node/edge dumps, goldData.xlsx or searched
biosample JSONL intermediate. The public classification workbook does not
replace those biological sources. No gene, regulator, organism or expression
claim makes iModulonDB applicable. Missing optional biology and definition
slots alone are not defects.

## Findings

Zero blockers, zero major findings, one minor finding.

1. **Minor: the source-induced chemical-product parent's mixture scope is
   not explicitly assessed for this target.** Manufacturing context is
   plausible, but a global strict-parent claim is stronger than the source
   classification. Owners: the exact source's assessment in
   `curation/decisions.tsv`, and `curation/gold_parent_exclusions.tsv` only
   if review establishes that this contribution is contextual rather than
   broader. This does not establish a wrong ENVO identity or warrant removing
   the supported liquid-water parent.

## Recommended Edits

During ITEM curation, compare the original source scope and ENVO chemical-
product definition explicitly. Retain the parent if its full meaning is
broader; use an exact-source/path/expected-parent exclusion if it is only
production context. Do not assume distilled water is perfectly pure or
sterile, change it to a molecule, or use an invented definition to suppress
an edge. Preserve both nodes, separate count units and honest lifecycle.

## Follow-up Checks

Regress the executed `gold_leaf_label` route, exact mapping predicate,
ENVO:00002006 parent, both source nodes, nine ORGANISM assertions and the
independent 45-sample/four-study context. Any exclusion must guard the full
path, source mint and resolved ENVO:2000000 parent without dropping ontology
parents. If later curation is authorized, append history, dry-seed, inspect
a forced canary, regenerate affected outputs and run strict/history/provenance/
labels/corpus/full QC. Compare complete semantic-map inputs before publishing.

## Additional Notes

Only this new review report was written. No scientific input, generated
record/page, status, session history or GitHub state changed. No paid research
or delegation. No SSSOM/KGX readiness claim. Fresh primary bytes parsed in memory:
ENVO 9,614,229 bytes, SHA256
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`;
GOLD workbook 84,174 bytes, SHA256
`f8e4cb5cf89ecc88d3cf28170cfc3a1cf47daed8218408a52914c53667dfd3d4`.
