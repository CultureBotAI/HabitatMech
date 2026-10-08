# YAML Record Review: Fruit processing

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/fruit_processing.yaml`
- Started UTC: 2026-10-08T15:41:14Z
- Finished UTC: 2026-10-08T15:43:42Z
- Verdict: pass

## Target

Generated HabitatRecord `habitatmech:GOLD.eafd8aafe3`, Fruit processing,
ENGINEERED / UNGROUNDED / SEEDED. The whole target and its actual industrial
waste material parent were read. Sole source: `Engineered > Solid waste > Industrial waste > Fruit processing`.
Baseline: 442d03d66.

## Validation

- `UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/fruit_processing.yaml`:
  passed, no issues.
- `UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/fruit_processing.yaml`:
  passed, one file, zero errors.
- Complete parsed target equals `seed.build_document()` from a fresh full
  corpus build: one source, zero ITEM-reviewed contributors. Actual target and
  parent resolvers ran with full ontology, mapping and claimant indexes; both
  source mints were recomputed.
- Full QC is reused, not rerun for report-only work. Fresh same-turn tree
  comparison proves baseline 442d03d66 equals validated d824000c0: 594 tests
  passed, three skipped, all remaining local gates passed, including 3,207
  strict-valid/reproduced records, 191 histories, provenance, site, terms and
  redirects. OAK and queue checks passed; [PR #1730 receipt](https://github.com/CultureBotAI/HabitatMech/pull/1730#issuecomment-6063458458).
- Original organism/sample joins and SSSOM/KGX compatibility were not verified.

## Identity and Grounding

The exact full-path mint agrees with `PATHS.tsv:3039`. Automatic resolution is
`gold_unmatched`; the CLASS CONFIRM_UNGROUNDED row at `curation/decisions.tsv:1300`
retains the mint through `curated_confirm_ungrounded_from_gold_unmatched`.
No mapping predicate or external exact identity is asserted. SEEDED correctly
does not present the old mechanical sweep as ITEM review.

The bare label names an activity, but the full source class is explicitly nested
under solid industrial waste. The most defensible reading of this source context
is waste classified by fruit-processing origin. This is a context-based
interpretation, not a recovered description of every original source member.
It does not justify converting the record to a generic processing procedure,
plant organ, factory building or fruit species. In particular, a process-like
leaf alone is insufficient evidence for NOT_APPLICABLE.

The sole parent ENVO:00002267 industrial waste material is contributed by parent
mint `habitatmech:GOLD.8faa599672`. Its default `gold_leaf_synonym` CLOSE/
skos:closeMatch answer is retained by an ITEM REVIEW. ENVO defines a material
class covering manufacturing-derived waste across physical phases. Fruit-
processing solid waste fits that broader material scope. No contrary source
evidence or false target parent was established. The parent's separately
generated synonym scope is not inherited by this target, which has no synonyms.

The bounded candidate scan of all vendored ontology rows, including labels and
synonyms containing fruit with waste/process/pomace and separate pomace/fruit
waste/food waste searches, found no exact fruit-processing-waste candidate.
ENVO:03600006 food waste is not an exact substitute for a specific industrial
source bin; its uneaten-food definition also cannot be assumed to cover every
processing residue. This is not a claim about every external ontology.

## Evidence

- `gold_ecosystem_paths.tsv:909` supplies nodes 8403/8404, the full path,
  one ORGANISM assertion and zero study/biosample counters. The first-node
  display, two-node collapse note and count/unit reproduce exactly. One source
  assertion is not an identified characteristic organism or a community survey.
- Fresh [GOLD workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths),
  `site data` row 405, confirms node 8404 at the same path. Worksheet dimensions
  were reset before complete iteration. SHA256
  `f8e4cb5cf89ecc88d3cf28170cfc3a1cf47daed8218408a52914c53667dfd3d4`.
  This verifies the classification, not historical node 8403 or its joins.
- Fresh [pinned ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
  confirms the active parent, its definition and its subclass relation to waste
  material ENVO:00002264. Its industrial-waste synonym is typed BROAD in OWL;
  this is not an exact synonym asserted by the target. SHA256
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
- Inspected primary FAO [Fruit products for profit](https://www.fao.org/4/i2472e/i2472e00.pdf),
  printed page 49 / PDF page 55, distinguishes processing operations from
  their solid residues and liquid outputs. FAO's [fruit-juice-processing guide,
  chapter 10](https://www.fao.org/4/y2515e/y2515e11.htm) likewise distinguishes
  residual materials, wash water and possible by-product uses. These sources
  corroborate the material-versus-operation distinction; they do not identify
  GOLD8403/8404 members or justify assigning particular fruits, residues,
  chemistry, disposal methods or recovered products to this record.

## Completeness

No definition, synonyms, xrefs, parameters, named taxa, mechanism graphs,
literature evidence objects, discussions or datasets are asserted. Their optional
absence is not itself a defect. In particular, no sugar content, pH, oxygen
condition, fermentation capability, fruit species or microbial taxon should be
inferred from general fruit-processing examples. iModulonDB is not applicable
without a target gene, regulator or strain-specific expression claim.

Ignored-inclusive identifier, label, stem, full path and source-node searches
covered curation, raw inventories, PATHS/RETIRED, configuration, docs, tests,
history, research and individual reports; filename traversal covered curation/
history/research. Only the target's CLASS decision was found among maintained
curation inputs. No target-owned definition, exclusion, overlay, separate session
history, research file or earlier individual report was found within those bounds.

Exact-field/pipe-member scanning of every raw TSV found only this ecosystem row,
not target sample/study/triad/parameter/taxon memberships. The same-turn ignored-
inclusive find under build, data/raw and configured kg-microbe data found no
original GOLD dumps, bulk workbook or sample/triad intermediates. Source-member
reconstruction therefore remains unavailable within those local bounds.

## Findings

None found: zero blockers, zero major findings, zero minor findings.
The pass is bounded: the record preserves an unresolved source category without
asserting an unsupported exact term, definition or specific biological traits.
It is not an ITEM endorsement or proof of every original member's meaning.

## Recommended Edits

No immediate scientific edit is established. Before promoting this source to
ITEM review or proposing a novel term, recover its original scope and resolve
the material-versus-operation interpretation in `curation/decisions.tsv`.
If a waste-material concept is confirmed, an evidence-backed clarifying name
and definition can belong in `curation/term_requests.tsv`. Do not manufacture
an exclusion, NOT_APPLICABLE decision or exact food-waste mapping from the
bare label, and do not overwrite the source's verbatim path.

## Follow-up Checks

Check original node/member evidence, physical-material scope and candidate
identity before any decision. Preserve source nodes and count/unit; assess all
parent contributions separately. Dry-seed and inspect a canary, append required
session provenance, then run schema, labels, history, provenance, exact corpus
reproduction and full QC. Regenerate site/map inputs only for actual changes.

## Additional Notes

Only this new report was written. A guessed parent filename failed; an ignored-
inclusive identifier/PATHS search located `industrial_waste_material.yaml`,
which was then read in full. That failed guess was not an absence finding.
FAO AGRIS bibliographic search results were leads, not evidence adopted without
inspection. No scientific/generated artifact, old report, status or GitHub item
was changed in this review.
