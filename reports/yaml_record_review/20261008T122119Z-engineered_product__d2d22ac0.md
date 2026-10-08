# YAML Record Review: Engineered product

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/engineered_product__d2d22ac0.yaml`
- Started UTC: 2026-10-08T12:17:03Z
- Finished UTC: 2026-10-08T12:21:19Z
- Verdict: pass with minor issues

## Target

Generated HabitatRecord `habitatmech:GOLD.74bb2a619a`, Engineered product,
ENGINEERED / UNGROUNDED / SEEDED. The entire target and actual parent
`industrial_production__f961ebd0.yaml` were read. This is the exact GOLD
`Engineered > Industrial production > Engineered product` bin, not the
BacDive Engineered-product source or a particular product child.
Baseline: e2572cfddcb7d9d8be12bb4866d6f5ba0ddad990.

## Validation

- `UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/engineered_product__d2d22ac0.yaml`:
  passed, no issues.
- `UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/engineered_product__d2d22ac0.yaml`:
  passed, one file, zero errors.
- Complete target regeneration in memory from `seed.build_corpus()` matched
  the parsed record; one source, zero ITEM-reviewed contributors. Actual
  target/parent resolution used the full current ontology, mappings, claimant
  indexes and decisions.
- Fresh shared checks passed: `just verify-corpus` (3,207 expected/present,
  zero missing/extra/differing), `just validate-history` (184 valid records),
  and `just provenance-check` (14 inventories and two GOLD sources current).
- Full QC was not rerun for report-only work. Current code, inputs, corpus,
  history, configuration and guidance match the validated a56b92e16 baseline
  by fresh `git diff --exit-code`. Prior local QC passed 590 tests with three
  skips and all remaining gates; merge-queue checks passed, as recorded in
  the [PR #1715 receipt](https://github.com/CultureBotAI/HabitatMech/pull/1715#issuecomment-6059147859).
- Original organism/sample joins could not be reconstructed from the available
  large sources. No biological-member census or export compatibility audit was done.

## Identity and Grounding

The exact path hash and `PATHS.tsv:2149` agree with the identifier and filename.
Both target and parent `habitatmech:GOLD.a744ade0d8` take `gold_unmatched`, then
CLASS CONFIRM_UNGROUNDED decisions (`decisions.tsv:695` and `:959`). Neither
decision adds an ontology target, predicate or ITEM endorsement. Their generated
history caveats and SEEDED state are faithful to that limited review depth.

The sole parent is the immediate GOLD Industrial production category. No
definition fixes whether that category means a manufacturing process, its
physical surroundings, or all associated product habitats. A broad source-
environment interpretation is plausible; equating the parent with an ontology
manufacturing process would be an unsupported extra assertion.

ENVO:00003074 manufactured product is a serious candidate for future item
assessment, not an automatic identity. Its inspected definition includes
intermediate and final human-processed material entities; its OWL relates
products to manufacturing through an output relation rather than subclassing
the process. The source bin's child vocabulary and limited triads favor a
product reading, but do not establish its entire sample-level extension or
its exact equality with that ontology class.

## Evidence

- `data/raw/gold_ecosystem_paths.tsv:221` contains nodes 3523/3860/4294,
  83 ORGANISM assertions and zero study/biosample counts in the ecosystem
  snapshot. Generated first-node ID, three-node note, count and unit agree.
- `gold_path_biosamples.tsv:163` separately records 163 biosamples for node
  4294. Exact pipe-member scanning finds 18 study rows for this path in
  `gold_studies.tsv`, including studies also classified as laboratory media,
  host samples, reagent/PCR blanks and natural environments. These are not
  163 organisms or 18 independent confirmations of one uniform product habitat.
  No study-wide organism, parameter or sample-role claim was transferred.
- `gold_path_triads.tsv:113-115` summarizes two samples from two studies, with
  two distinct terms in every slot. Each displayed top term has share 0.50
  and one agreeing study: broad ENVO:00003074 manufactured product, local
  NCIT:C171256 Non-Medical Object or Device, medium ENVO:03501263 hand tool.
  These are marginal slot summaries, not proof that all three displayed terms
  belonged to the same sample. They are also not measurements of product ecology.
- Primary [ENVO source](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
  inspection verified the active product, hand-tool and manufacturing-process
  classes. SHA256 `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
  [NCI's concept API](https://api-evsrest.nci.nih.gov/api/v1/concept/ncit/C171256)
  independently returned C171256, the expected name, DEFAULT status and version
  26.09d; it describes a manufactured object intended for non-medical use.
  That external resolution does not add the term to the vendored habitat slice.
- The actual `_triad_inventory_review()` helper marks the two ENVO rows
  groundable and the NCIT row missing from the slice. This is a compatibility
  screen, not approval of their MIxS roles. The primary [ENVO/MIxS guidance](https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS)
  expects a broad environmental system and material medium; an individual
  product in broad scale and a countable hand tool in medium require source
  review, not copying into habitat identity or environmental parameters.
- The primary [GOLD workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths)
  confirms node 4294 at `site data` row 328. Rows 315-329 retain the product
  descendants. Worksheet dimensions were reset before parsing; SHA256
  `f8e4cb5cf89ecc88d3cf28170cfc3a1cf47daed8218408a52914c53667dfd3d4`.
  This confirms classification, not historical nodes 3523/3860 or the 83 assertions.
- Current [GOLD classification guidance](https://gold.jgi.doe.gov/ecosystem_classification)
  describes sample surroundings and nested contextual groupings. It does not
  say every source-path step is a strict ontology subclass.

## Completeness

Definition, synonyms, xrefs, parameters, named taxa, evidence objects, graphs,
discussions and datasets are empty. They should remain empty without scoped
evidence. Neither descendants nor the distinct BacDive source's 526 strains
and 378 taxa are evidence for this target's own organisms. iModulonDB is not
applicable to an unnamed-organism source-category record.

Ignored-inclusive ID, label/stem, source-path and node searches covered
curation, raw inventories, PATHS/RETIRED, history, research, configuration, docs,
tests and individual reports. Exact-field/pipe-member parsing separated the
target's rows from descendant paths after a broad search produced many hits.
Filename traversal included ignored files under curation/history/research.
There is a CLASS decision and contextual material/bioanode/filter research or
review, but no target-owned definition, exclusion, causal overlay, research
report, session history or prior individual review in those bounds. The
descendant solid-manufactured-material definition does not define this parent.

Fresh ignored-inclusive find under build, data/raw and configured kg-microbe
data found none of the searched GOLD node/edge dumps, goldData.xlsx,
gold_biosample_triads.tsv or biosample JSONL intermediates. Thus original
member scope remains unavailable locally, not disproved. Empty generated
fields and a CLASS lifecycle do not by themselves constitute major defects.

## Findings

1. **Minor: product-versus-production-setting scope is unresolved for the
   strict parent relation.** The source grouping is reproduced, but neither
   record has a maintained definition that establishes how the product bin is
   subsumed by Industrial production as a habitat class. The small, discordant
   triad subset is insufficient to settle all members. This review flags an
   unresolved hierarchy claim, not a proven formal product/process conflation.
   Owner: exact-source ITEM assessment in `curation/decisions.tsv`, supported
   definitions in `curation/term_requests.tsv` if appropriate, and an exact
   `curation/gold_parent_exclusions.tsv` row only if contextual scope is established.

No blocker or major finding. The triad source-quality caveats are not defects
in an assertion the generated record never makes.

## Recommended Edits

Recover original product/source descriptions before judging the strict parent
or adopting ENVO:00003074 as identity or genus. Distinguish manufactured
objects, product-associated material, manufacturing surroundings and controls;
do not force them into one reading from the label alone. Preserve the parent
if evidence establishes a true broader habitat class; exclude only its exact
GOLD contribution if it instead encodes production context. Do not invent a
definition to remove an edge, merge the BacDive bin, or extend the material
child's solid-only restriction to fuels and all other products.

## Follow-up Checks

Trace the two complete-triad samples independently, inspect their non-top
terms and study identities, and adjudicate MIxS role compatibility separately
from ontology existence. Inspect all 18 study memberships without attributing
their other paths to this target. Later authorized curation should preserve
nodes, units, mint and descendants unless specific evidence changes them,
append history, canary, regenerate and pass reproduction/strict/provenance/
labels/site/full QC. Compare semantic-map inputs when scientific text changes.

## Additional Notes

Only this new timestamped report was authored. No scientific inputs, generated
records, historical reports, review status or GitHub state changed. Initial
guessed unsuffixed parent/sibling paths did not resolve; authoritative PATHS
lookup identified the actual parent before any judgement. No global absence
or SSSOM/KGX readiness claim is made.
