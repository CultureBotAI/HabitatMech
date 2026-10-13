# YAML Record Review: laboratory environment

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/laboratory_environment.yaml`
- Started UTC: 2026-10-09T02:52:11Z
- Finished UTC: 2026-10-09T02:55:15Z
- Verdict: needs curation (0 blocker, 1 major, 0 minor)

## Target

Read the complete generated HabitatRecord ENVO:01001405 at baseline
`893f468d11748cef519a6f1191f294af37559d04`: ENGINEERED / BROAD / REVIEWED.
It has an ENVO definition, one exact GOLD synonym, two parents, one
four-node GOLD attestation, 549 ORGANISM assertions and two events. Its
sole source is `Engineered > Lab synthesis`, not a direct observation of
every laboratory environment. The complete anthropogenic-environment and
Engineered parents, Genetic cross child and separate BacDive Lab-synthesis
record were read as context, not counted as additional completed reviews.

## Validation

- Fresh `UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/laboratory_environment.yaml`:
  no issues.
- Fresh strict validation with the same cache setting: one file, zero errors.
- Full-index construction and `build_document()` reproduced every field:
  one source, one ITEM-reviewed source, no authored definition and no
  applied target parent exclusion.
- Shared fresh session checks passed: 3,208 records reproduce exactly,
  208 histories valid, and 14 inventories/two GOLD sources current.
- Full QC was not repeated per read-only record. Local and
  [exact-baseline queue QC](https://github.com/CultureBotAI/HabitatMech/actions/runs/37874456969)
  passed all gates with 622 tests and three skips; baseline
  [label correspondence](https://github.com/CultureBotAI/HabitatMech/actions/runs/37874456975)
  and vendored sync passed. They do not certify source identity or synonym
  scope. No SSSOM/KGX readiness audit was performed.

The target asserts no named taxa, literature evidence or causal edges
requiring an additional claim-level reference validator.

## Identity and Grounding

`PATHS.tsv:891` agrees with the ontology ID/stem. The source mint is
`habitatmech:GOLD.e4a3c08b86`. With complete mapping and claimant indexes,
its default route is `gold_unmatched`. The ITEM GROUND row at
`curation/decisions.tsv:1265` produces `curated_ground_from_gold_unmatched`,
adopts ENVO:01001405, sets BROAD/skos:broadMatch and reviewed=True. REVIEWED
therefore correctly describes the existing decision, not scientific proof
of that decision's equivalence.

Complete [pinned primary ENVO](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
class elements confirm the label and building-bounded controlled-environment
definition. They give the direct superclass ENVO:01000313 anthropogenic
environment and no ontology synonym Lab synthesis. The definition and
ontology parent are valid for the ontology class, not an independent
definition of GOLD's synthesis category. The same-session verified source
SHA256 is `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.

The curation rationale itself says the target is broader than synthesis.
Nevertheless, `seed.py:_decided` adopts its ID for GROUND, and `ingest_gold`
emits Lab synthesis as EXACT_SYNONYM. The latter branches at lines 906-913
weaken strict-ancestor leaf aliases and CLOSE mappings, but BROAD reaches
the exact fallback. Neither a broad mapping nor proximity to a laboratory
establishes exact lexical or entity equivalence. This is source-label
handling, distinct from the flat ontology-synonym defect tracked in #1249.

The additional Engineered parent comes from the immediate source path. Its
undefined native root was freshly inspected/resolved in this session.
For the actual building-bounded ontology class an engineered-environment
reading is defensible; no separate definite false-parent finding is made.
That does not settle the genus of a future source-specific synthesis record.

## Evidence

- `gold_ecosystem_paths.tsv:68` contains the exact depth-two path, nodes
  2883/3498/3820/4247 and 549 ORGANISM assertions. First ID, four-node note,
  path, count/unit and broad predicate faithfully reflect the current inputs.
- `gold_path_biosamples.tsv:608` separately records 11 BIOSAMPLEs for
  node 4247. These are not 11 additional organisms or samples of every
  laboratory environment.
- Exact-field/pipe-member scanning of all 14 inventories found four study
  memberships at physical `gold_studies.tsv` lines 795 Gs0114365 (two paths),
  1093 Gs0118444 (12), 2188 Gs0136062 (three), and 2841 Gs0145102 (one).
  Multi-path studies also include marine sediment, built surfaces, fish
  intestine, laboratory-grade water or serum; they do not equate those
  habitats. The [single-path Gs0145102 page](https://gold.jgi.doe.gov/study?id=Gs0145102)
  was inaccessible. Gs0136062 also failed during this session's water review;
  the other two pages were not independently inspected. Original members
  and their synthesis-versus-setting meaning remain unresolved.
- No direct target triad, taxon or environmental-parameter row was found.
  The target CURIE does occur as a local-scale annotation for two different
  paths: contaminated soil (31 samples/eight studies, four terms, 0.35 top
  share, one agreeing study) and tissue-engineered tendon (one sample/study).
  `gold_path_triads.tsv:972,1341` is contextual annotation, not extra target
  sources, characteristic taxa or proof of the Lab synthesis mapping.
- `ontology_terms.tsv:8898` agrees with the primary label/definition and
  contains no synonym. The all-table scan finds only the true direct
  anthropogenic-environment superclass edge for the target ontology ID.
- Fresh [GOLD workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths)
  parsing after resetting worksheet dimensions confirms node 4247 at
  `site data` row 354 with three Unclassified fillers; row 353 is the
  separate Genetic cross child, node 4720. The 84,174-byte response SHA256
  is `3933e5f0664915c1bbfa00212e17d013da360fb33dd52e509254050813135396`.
  Current classification is not a definition or refreshed historical count.

## Completeness

Xrefs, parameters, taxa, evidence, graphs, discussions and datasets are
empty. No gene/regulator claim makes iModulonDB applicable. The parent's
3,087-TAXON PREGO aggregate and 25 displayed associations do not transfer
to this target; those taxa were not independently re-reviewed here.

The separate BacDive record `habitatmech:BACDIVE.0e92e77cd4`, Lab-synthesis,
has three STRAIN assertions and three taxa under an intentionally blank
upstream mapping. It is not a co-attestation or automatic merge candidate.
Its older individual report was read as context, not current primary proof
or endorsement of its CLASS-based major finding; its taxa were not freshly
validated by this target review. Ignored-inclusive identifier searches
resolved its actual `other/` path and the anthropogenic parent's path after
initial wrong-category guesses.

Ignored-inclusive ID, source mint, label/stem, path and node searches across
curation, history, research, configuration, raw inventories, PATHS/RETIRED
and individual reports found the ITEM row and contextual mentions, but no
target-owned authored definition, overlay, exclusion, session history,
dossier or previous individual target report within those bounds.
The child-owned exclusion at `gold_parent_exclusions.tsv:8` already removes
its unsupported ENVO:01001405 parent; the current child was checked in full.

## Findings

1. **Major: a broader source correspondence is promoted into identity and
   exact synonymy.** The ITEM rationale and skos:broadMatch distinguish
   Lab synthesis from laboratory environment, yet GROUND substitutes the
   ontology identity and GOLD alias emission asserts exact synonymy. The
   building-enclosed environmental system is not thereby established as the
   source entity. This is one scope-inflation finding with two repair owners:
   the source decision in `curation/decisions.tsv:1265` and the non-exact
   source-label fallback in `src/habitatmech/seed.py:913`.

Zero blockers and zero minor findings. Unresolved original-source scope is
part of the major finding's repair limit, not an additional count defect.
All-state issue title/body searches found adjacent cases; the complete
closed [#1459](https://github.com/CultureBotAI/HabitatMech/issues/1459) body
and comments show its implemented repair covers CLOSE, not this BROAD
fallback. No exact-source implementation issue was found in those bounds;
comments on every other issue were not exhaustively searched.

## Recommended Edits

Reassess GOLD.e4a3c08b86 using original category/member evidence. Preserve
source identity when equivalence is unsupported. Use GROUND_AS_PARENT only
if a genuinely narrower physical habitat is established; use a contextual
xref, an ungrounded habitat decision or NOT_APPLICABLE only when the actual
entity warrants it. Do not assume an activity or material is a kind of the
building envelope merely because synthesis occurs in a laboratory.

Independently prevent BROAD source mappings from implying exact synonyms
through the shared source handler. Preserve the original label in the
attestation and select a justified weaker alias treatment; do not globally
downgrade genuine exact aliases or blindly translate mapping direction into
a lexical synonym type. A scope-only alias repair does not settle the
source identity question or the BacDive record's equivalence.

Audit the Genetic cross exclusion's expected resolved parent before any
identity split; a stale guard must not be bypassed. Do not rewrite unrelated
triad CURIEs or infer that an ontology URL should redirect to a non-equivalent
source concept. Preserve primary ENVO identity/definition wherever the
ontology class remains independently represented.

## Follow-up Checks

Add BROAD-versus-EXACT source-alias regressions alongside the existing CLOSE
and ancestor cases. Test source identity, parent placement, genuine review
status, four-node provenance, 549 ORGANISM versus 11 BIOSAMPLE units, and
all four study memberships. Full-corpus comparison must expose downstream
references, exclusion guards and redirect consequences. Authorized repair
requires append-only history, dry seed, inspected canary, strict,
provenance/history, label, corpus/site and full QC. Compare semantic inputs:
scope-only changes may be text-neutral, but changed identity, label or
hierarchy requires the actual supported map rebuild when hashes change.

## Additional Notes

Only this report was written. No curation, generated artifacts, review
status, history or GitHub item changed. Primary source failure is reported
as an access limit, not evidence that original biological metadata do not
exist. The ontology's valid definition is not itself a wording defect.
