# YAML Record Review: Unchlorinated

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/unchlorinated.yaml`
- Started UTC: 2026-10-06T18:18:29Z
- Finished UTC: 2026-10-06T18:21:27Z
- Verdict: needs curation

## Target

The entire generated `HabitatRecord` was read at baseline
`7507858f867f57eb3a552f032dc84a16ed2a21f2`: identifier
`habitatmech:GOLD.d29a0aa94b`, label Unchlorinated, AQUATIC,
UNGROUNDED/SEEDED. It contains one parent, one GOLD attestation with
12 ORGANISM assertions, and two history events. It denotes the freshwater
drinking-water path qualified as unchlorinated, not a standalone quality,
chlorine chemical, dechlorination process or arbitrary untreated water.

## Validation

- `UV_CACHE_DIR=build/uv-cache just validate data/habitats/aquatic/unchlorinated.yaml`:
  pass, no issues.
- `UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/aquatic/unchlorinated.yaml`:
  one file, zero errors; the ignored validator diagnostic TSV refreshed.
- Actual `seed.build_corpus()` / `seed.build_document()` execution and full
  parsed-document comparison: pass, one source, zero ITEM-reviewed sources,
  zero taxa, two history events.
- Shared current-session checks on unchanged scientific inputs:
  `just verify-corpus` reproduced all 3,206 records with no differences;
  `just validate-history` validated all 104 histories;
  `just term-requests-check` found all 109 terms current.
- [Full QC 37507480894](https://github.com/CultureBotAI/HabitatMech/actions/runs/37507480894)
  and [label gate 37507480900](https://github.com/CultureBotAI/HabitatMech/actions/runs/37507480900)
  passed on this exact baseline. Full QC/OAK, provenance, causal and site
  gates were not independently rerun for each Markdown-only report.
- Current official ENVO RDF/XML was parsed for drinking water, fresh water
  and aquatic biome. All three are active classes. No taxon, gene, DOI, PMID
  or causal-edge identifiers are asserted in the target.
- Rendered page text was inspected and agrees with the YAML, including the
  full path, count/unit, parent and explicit CLASS-sweep qualification.
  No browser screenshot or visual QA is claimed.

## Identity and Grounding

Minting the full path
`Environmental > Aquatic > Freshwater > Drinking water > Unchlorinated`
reproduces GOLD.d29a0aa94b; `PATHS.tsv:2846` pins the slug. The full path
supplies the omitted noun, so the short source label is not grounds to reject
this microbial water habitat as NOT_APPLICABLE. AQUATIC is the inherited
coarse bucket, not a claim that drinking-water infrastructure is natural.

Actual `resolve_gold` takes `gold_unmatched`. The CLASS CONFIRM_UNGROUNDED
decision at `curation/decisions.tsv:1165` retains the minted ID and produces
`curated_confirm_ungrounded_from_gold_unmatched`, with `reviewed=False`.
SEEDED is accurate. No source-to-record mapping predicate is emitted; the
source concept is its own retained record. The historical lexical non-match
is not proof that no future exact term or definition can be supplied.

The immediate parent, `habitatmech:GOLD.99a88ecb51`, is the same freshwater
Drinking water path without the final qualifier. Its actual default/applied
route is `gold_narrower_than_leaf_match`, retaining the minted parent with
ENVO:00003064 as a broader term. Unchlorinated drinking water is narrower
than drinking water; no removal of this direct edge is justified.

[ENVO at a2455d1a77e46bb8a664d65a157166b539269042](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
defines drinking water ENVO:00003064 as a water material and places it under
fresh water ENVO:00002011. The inspected minted parent carries both terms;
that material hierarchy is consistent. The name/ontology definition does not
independently certify the safety of any particular environmental sample.

The closure also reaches a false ancestor through the current fresh-water
record: ENVO:00002011 has both its true liquid-water parent and a generated
ENVO:00002030 aquatic-biome parent. Actual route execution resolves GOLD
Freshwater to the water material and its preceding Aquatic path to the biome;
the second source-path pass creates the edge. The ontology itself gives the
fresh-water term only the liquid-water named parent. A water material is not
the ecological biome it helps determine. This inherited defect is distinct
from the valid immediate Unchlorinated-to-Drinking-water relationship.

## Evidence

All 14 committed raw TSVs were scanned with structured exact field/pipe-list
matching for the path, minted ID, source node and label:

- `gold_ecosystem_paths.tsv:495` supplies node `gold.ecosystem:4547`, the
  exact five-level path, one node, depth 5, 12 organism assertions, and zero
  study/biosample counts in that snapshot. The YAML preserves count and unit.
- The [current public GOLD ecosystem workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths)
  independently verifies node 4547 and the full path at row 563. The 84,174
  downloaded bytes had SHA-256
  `01c8c8500c86297101fbe3ecc42ff63c058096977cba5238524b8a83770ec2e0`.
  Incorrect A1:A1 dimensions were reset before complete worksheet iteration.
- `gold_path_biosamples.tsv:672` separately records eight biosamples. They
  are not replacements for the 12 older ORGANISM assertions.
- `gold_studies.tsv:709` and `:1505` associate Gs0111485 and Gs0128957 with
  the path among 25 and 13 paths respectively. These are verified inventory
  memberships, not freshly inspected study-page/sample crosswalks or evidence
  for a universal microbiome. No exact target triad row was found.

The inspected primary study [van der Wielen et al.,
DOI:10.1128/AEM.01591-13](https://journals.asm.org/doi/10.1128/aem.01591-13)
sampled treated, unchlorinated drinking water from distribution systems of
five Dutch treatment plants. It provides a concrete microbial-habitat example
and demonstrates that unchlorinated does not mean untreated. Its microbial
observations are specific to the sampled systems, not universal attributes
of all water in this GOLD class. No crosswalk proves that this paper owns the
GOLD samples above; none is claimed.

The source path alone does not establish a disinfectant-residual detection
limit, the absence of every other treatment, source-water origin, sterile
status, a salinity value or pathogen prevalence. No such claim was added.
The title's research marker gene is not a gene assertion in the habitat YAML.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden` searches used the exact ID,
label, slug and GOLD node across `curation/`, `history/`, `research/`,
`conf/`, `docs/`, `src/`, `tests/`, PATHS and RETIRED. Focused searches
covered term requests, causal overlays, GOLD exclusions, research and its
manifest. No target-owned authored definition, exclusion, causal overlay or
research report was found in those maintained surfaces. The broad all-TSV
scan found no exact target parameter, BacDive, PREGO, Madin, ontology identity
or isolation-source-mapping row. Ignored files were included; these are
bounded repository findings, not statements about all published literature.

The record is otherwise complete for its maintained inputs. Empty optional
definition, taxa, parameter, dataset, discussion and mechanism slots are not
defects by themselves. A future definition could expand the short label to
unchlorinated drinking water while retaining the original source label and
path, but should not silently turn it into raw, untreated or undisinfected
water. iModulonDB is not applicable: there is no record gene, regulator,
protein or expression-dataset assertion to cross-check.

## Findings

1. **Major: the retained material hierarchy inherits an aquatic-biome is-a.**
   The current chain is GOLD.d29a0aa94b -> GOLD.99a88ecb51 ->
   ENVO:00002011 -> ENVO:00002030 (also reachable through drinking water's
   ontology ancestry). The final edge conflates water material with a biome.
   Current source routes, generated ancestors and official definitions were
   independently inspected; this is not inferred solely from an older report.
   Owner: the exact GOLD.ad12f0169a Freshwater source contribution to
   ENVO:00002030 in `curation/gold_parent_exclusions.tsv`. Preserve the
   target's valid drinking-water parent and the true liquid-water hierarchy.

Totals: zero blockers, one major finding, zero minor findings. The finding is
shared ancestor debt, not a new local source-identity or count defect.

## Recommended Edits

1. Complete the governed Freshwater-to-aquatic-biome correction at its actual
   source owner; do not suppress the target's true immediate parent or alter
   all freshwater source assertions to mask it. Preserve PREGO/Madin/material
   data on the water record and keep exact source paths/counts intact.
2. Coordinate existing work rather than creating competing scientific changes:
   [#1215](https://github.com/CultureBotAI/HabitatMech/issues/1215) is currently
   CLOSED/COMPLETED, but its inspected comment points to the correction in
   [draft PR #1218](https://github.com/CultureBotAI/HabitatMech/pull/1218).
   That PR remains OPEN/DRAFT at
   `18c93452a789218f5c653d02723d11388d972055`; [#1217](https://github.com/CultureBotAI/HabitatMech/issues/1217)
   remains open for the generated map/site follow-up. Closed issue state does
   not prove a landed scientific fix, and the current main-line record still
   contains the edge. The draft and issues were inspected, not modified.
3. Optionally perform future ITEM-level definition work through
   `curation/decisions.tsv` and `curation/term_requests.tsv`, preserving the
   drinking-water scope and uncertainty about other disinfection. Do not
   promote status merely because this review report exists.

## Follow-up Checks

After the ancestor curation, inspect forced canaries for the corrected
fresh-water record and this descendant; verify the valid direct parent and
12 ORGANISM attestation remain unchanged while the false biome ancestor is
removed. Run history, closed/open schema, ontology labels, provenance, exact
corpus reproduction and full QC. Rebuild map/site from genuine changed
semantic inputs and complete the draft's own evidence/merge gates.

Before adding taxa or mechanisms, inspect the exact study/sample provenance
and distinguish bulk water, pipe biofilm and deposits. No health-safety claim,
current disinfection recommendation, SSSOM export or KGX modeling certification
is supplied by this review.

## Additional Notes

The earlier Drinking water and fresh-water reports were read as leads, not
treated as current proof. The present verdict relies on freshly inspected
records, source routes, ontology and remote workflow states. This report is
the only authored target change; no scientific record, history, source,
generated page or GitHub item was edited. The original CLASS and seed events
reproduce. The full-corpus goal remains active and incomplete.
