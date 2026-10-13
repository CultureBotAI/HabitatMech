# YAML Record Review: fermentation pit

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/fermentation_pit.yaml`
- Started UTC: 2026-10-08T14:26:42Z
- Finished UTC: 2026-10-08T14:30:50Z
- Verdict: needs curation

## Target

Generated HabitatRecord ENVO:03600039, fermentation pit, ENGINEERED / EXACT /
SEEDED. The entire target and immediate Built Environment record were read.
Its sole source is GOLD's `Engineered > Built environment > Fermentation pit`,
mint `habitatmech:GOLD.0e491690d7`. Baseline: 60bdbace5d44a9b1e0ea5f0dbe769792196bd236.

## Validation

- `UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/fermentation_pit.yaml`:
  passed, no issues.
- `UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/fermentation_pit.yaml`:
  passed, one file, zero errors.
- Complete parsed target equals `seed.build_document()` from a fresh full
  corpus build: one source concept, zero ITEM-reviewed contributors.
- Actual target and immediate-parent resolvers were executed with complete
  ontology, mapping and claimant indexes; both full-path mints were recomputed.
- Full QC is reused, not repeated for report-only work. A fresh quiet git diff
  proves this tree equals validated 9b901cc28. Full local QC passed 592 tests
  with three skips, all 3,207 strict schemas and exact reproduction, 189 histories,
  32 overlays, provenance, floor, site, redirects, terms and report. OAK and
  merge-group checks passed: [PR #1725 receipt](https://github.com/CultureBotAI/HabitatMech/pull/1725#issuecomment-6062037613).
- Original sample-level joins and SSSOM/KGX compatibility were not verified.

## Identity and Grounding

`PATHS.tsv:935` locks this identity and stem. The active ENVO label and
definition reproduce the source ontology. Its definition is not generic:
it restricts the constructed pit to fermentation yielding alcoholic spirits.
The source path does not state that restriction. `gold_leaf_label` adopts
EXACT/skos:exactMatch without a target decision. SEEDED correctly exposes the
lack of ITEM review, but does not supply missing evidence for that equivalence.

The construction, not its mud, contents or fermentation process, is the
plausible habitat referent. However, exact source equivalence is unresolved:
the same label has a documented non-spirit engineering use, and the original
GOLD members are unavailable. This review does not assert that GOLD5450
actually denotes wastewater treatment or force a replacement identity.

The two named ENVO superclasses are human construction ENVO:00000070 and pit
ENVO:01001871. Their definitions support a deliberately constructed ground
depression. The third parent comes from the GOLD parent mint
`habitatmech:GOLD.d601823ae4`, resolved through `gold_mapping_table` to
mesh:D000076624 Built Environment, without an ITEM override. NLM's scope
includes constructed physical elements and infrastructure, so this construction
fits that broad class. No false parent edge was established; do not suppress
these parents simply because many other GOLD paths encode context rather than is-a.

## Evidence

- `gold_ecosystem_paths.tsv:1260` contains GOLD5450, the exact full path and
  zero organism, study, biosample and total assertions in this snapshot. The
  absent count/unit and collapse-note fields faithfully reproduce a single
  zero-count source node; they are not claims of microbial absence.
- Fresh [pinned ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
  inspection verifies the active target, both named superclasses and their
  definitions/typed edges. Bytes: 9,614,229; SHA256
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
  The local edges are `ontology_subclass_edges.tsv:8477-8478`.
  ENVO:03600090 alcohol fermentation pit is a named child; ENVO:03600091 clay
  fermentation pit has its own construction-material scope. Neither is evidence
  that every member of the GOLD bin has those properties.
- Fresh [NLM descriptor D000076624](https://meshb.nlm.nih.gov/record/ui?ui=D000076624)
  confirms Built Environment and its broad man-made-physical-elements scope.
  The local slice has no definition for that parent; none was invented.
- The fresh [GOLD workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths)
  contains the target prefix within the Mud leaf at `site data` row 196,
  node 5452. It does not independently verify historical interior node 5450.
  Worksheet dimensions were reset before complete iteration. Bytes: 84,174;
  SHA256 `f8e4cb5cf89ecc88d3cf28170cfc3a1cf47daed8218408a52914c53667dfd3d4`.
  [GOLD's guide](https://gold.jgi.doe.gov/ecosystem_classification) describes
  sample-surroundings categories, not proof of every ontology restriction.
- The primary [California Water Board technical description](https://waterboards.ca.gov/coloradoriver/board_decisions/adopted_orders/orders/2012/0002wdr.pdf),
  page 2, findings 7-8, calls an excavated wastewater-solids digestion and
  stabilization structure a fermentation pit. This establishes genuine lexical
  ambiguity, not membership in GOLD5450. No site-specific operating values,
  chemistry, organisms or legal requirements are transferred to this habitat;
  the historical document is not being presented as current legal guidance.

## Completeness

No synonyms, xrefs, parameters, taxa, evidence objects, causal graphs,
discussions or datasets are asserted. Optional empties are not defects, and
neither parent-level organisms nor the Mud child's observations should be
inherited. The alcohol-fermentation-pit triad belongs to the distinct
`Engineered > Food production > Fermented beverages` path, not this record.
iModulonDB is not applicable: no strain-specific gene, regulator or expression
claim is made.

Ignored-inclusive ID, label, stem, source-node, source-path and mint searches
covered curation, raw inventories, PATHS/RETIRED, configuration, docs, tests,
history, research and individual reports. Filename traversal included ignored
files under curation/history/research. No target-owned decision, definition,
exclusion, overlay, history or earlier target review was found within those
bounds. Related fermentation/food reports are context, not independent evidence.

Exact-field/pipe-member scanning of every raw TSV found only the target
ecosystem and ontology rows, not target sample memberships, bulk counts,
triads, parameters or taxa. Fresh ignored-inclusive find under build, data/raw
and configured kg-microbe data found no original GOLD node/edge dumps, bulk
workbook or sample/triad intermediates. A domain-filtered GOLD web search
returned no indexed match; that is not evidence of absence from GOLD itself.

## Findings

1. **Major: exact grounding imports an unverified alcoholic-spirit restriction.**
   The lexical source category and its available prefix/child evidence do not
   establish the defining purpose of ENVO:03600039. The primary engineering
   counterexample shows that the bare label is not uniquely diagnostic. This
   is a source-specific identity-evidence gap, not proof of a wrong wastewater
   identity, a broken reference, or a rule that every SEEDED record is defective.
   Maintained owner: the ITEM assessment for `habitatmech:GOLD.0e491690d7` in
   `curation/decisions.tsv`, informed by recovered versioned GOLD source scope.

No separate hierarchy, blocker or minor finding.

## Recommended Edits

Recover the original category/member descriptions and assess the full source
extension against ENVO's alcoholic-spirit restriction. If supported, add an
evidence-specific ITEM decision; if not, retain an appropriately scoped minted
habitat and only demonstrated broader relations through maintained decisions
and, where justified, `curation/term_requests.tsv`. Do not substitute the
water-treatment example, a pit-mud material, clay pit or process from label
similarity. The currently supported construction/pit/built-environment hierarchy
should not be erased to compensate for unresolved source identity.

## Follow-up Checks

Validate the new source-scope evidence, candidate ID/label and relation direction;
reassess the Mud child and all parent contributions if identity changes.
Dry-seed and inspect a canary, append curation-session provenance, then check
schema, labels, history, reproduction, provenance and full QC. Check filenames,
redirects and actual semantic-map inputs before regeneration. No original node
or zero-count provenance should be lost or converted into invented observations.

## Additional Notes

Only this new timestamped report was authored. No scientific/generated input,
old report, curation event, review status or GitHub item changed. The checklist
was read from the curate skill's referenced path after a guessed review-skill
subdirectory failed; that failed read was not used as an absence finding.
