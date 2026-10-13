# YAML Record Review: fresh water aquarium

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/fresh_water_aquarium.yaml`
- Started UTC: 2026-10-08T15:37:34Z
- Finished UTC: 2026-10-08T15:40:06Z
- Verdict: pass

## Target

Generated HabitatRecord ENVO:00002198, fresh water aquarium, ENGINEERED /
EXACT / REVIEWED. The complete target and both immediate parent records were
read. Baseline: 442d03d669bcd7f32c761862b378c5f638612d87. This reviews the
new ontology-identified record, not the superseded minted YAML reviewed in
`20261008T144523Z-freshwater_aquarium.md`.

## Validation

- `UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/fresh_water_aquarium.yaml`:
  passed, no issues.
- `UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/fresh_water_aquarium.yaml`:
  passed, one file, zero errors.
- The complete parsed target equals `seed.build_document()` from a fresh
  full corpus build: one contributing source, one ITEM-reviewed contributor.
  Actual target and immediate GOLD parent resolvers used complete ontology,
  mapping and claimant indexes; both content-derived mints were recomputed.
- Full QC was not repeated for new-report-only work. Fresh quiet git comparison
  proves this baseline equals validated head d824000c0. Its completed local QC
  passed 594 tests with three skips, 191 histories, 3,207 strict-valid and
  exactly reproduced records, 32 overlays, provenance, floor, site, redirects,
  term requests and report. Separate ontology correspondence and final-head/
  queue checks passed; see the [PR #1730 receipt](https://github.com/CultureBotAI/HabitatMech/pull/1730#issuecomment-6063458458).
- Original organism/sample joins and SSSOM/KGX export compatibility were not
  independently verified in this review.

## Identity and Grounding

The maintained ITEM GROUND decision at `curation/decisions.tsv:707` maps
source mint `habitatmech:GOLD.772964032b` to ENVO:00002198. Its default
`gold_unmatched` result is overridden through `curated_ground_from_gold_unmatched`,
yielding EXACT/skos:exactMatch and the explicit ENGINEERED category. The source
path is `Engineered > Artificial ecosystem > Vivarium > Freshwater aquarium`.
Both path and definition denote the freshwater-containing enclosure, not its
water, sediment or organisms. The joined-versus-separated spelling is a
defensible exact source synonym in this ITEM-reviewed scope.

`PATHS.tsv:678` agrees with the new identity and stem. The ontology contributes
ENVO:00002196 aquarium; the GOLD parent mint `habitatmech:GOLD.d379e579ab`
contributes ENVO:00010622 vivarium through `gold_leaf_label`, without an override.
Both are strictly broader, and the ontology independently places aquarium below
vivarium. Retaining the transitive vivarium parent is not a false contextual edge.

The sole contributor's ITEM decision justifies REVIEWED. It does not imply
independent validation of every historical organism observation. The generated
events follow the current seeder and decision; the earlier minted/class-screened
state remains traceable through the prior report, git history and append-only
session record. This review creates no new curation event or status change.

## Evidence

- `gold_ecosystem_paths.tsv:770` preserves nodes 8025/8026, the full path,
  two ORGANISM assertions and zero study/biosample counters. The displayed
  first node and two-node collapse note reproduce correctly. These are not
  two named species, samples or a community composition estimate.
- Fresh [pinned ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
  inspection verifies the active target and both broader classes, their
  definitions and typed ancestry. The target definition is reproduced from ENVO,
  not authored from a generic aquarium example. SHA256
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`;
  9,614,229 bytes. Local term: physical line 7281, CSV logical row 7275;
  direct target edge: `ontology_subclass_edges.tsv:5393`.
- Fresh [GOLD workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths),
  `site data` row 58, confirms node 8026 at the target path. Row 57 is the
  distinct Sediment child, node 8037. Complete worksheet iteration reset the
  declared dimensions. SHA256
  `f8e4cb5cf89ecc88d3cf28170cfc3a1cf47daed8218408a52914c53667dfd3d4`;
  84,174 bytes. This does not reconstruct historical node 8025 or its joins.
  The inspected [GOLD classification guide](https://gold.jgi.doe.gov/ecosystem_classification)
  describes collection surroundings; it does not supply unrecorded biology.
- `history/mappings/freshwater_aquarium/2026-10-08T150152Z-codex-gpt-5-8f86b6.yaml`
  records the supported grounding, inspected source hashes and validation
  boundary with correct agent attribution. The previous review's missed-candidate
  finding was resolved in PR #1730; that old report remains historical evidence.

## Completeness

No xrefs, parameters, taxa, mechanism graphs, literature evidence objects,
discussions or datasets are asserted. Their optional absence is not a defect.
Do not inherit the aquarium parent's PREGO taxon or the Sediment child's single
organism assertion. Those context records were not independently reviewed here.
iModulonDB is not applicable: the target makes no strain-specific gene,
regulator or expression-module claim.

Ignored-inclusive ID, source mint, both label spellings and stem searches covered
curation, raw inventories, PATHS/RETIRED, configuration, docs, tests, history,
research and individual reports; filename traversal covered curation/history/
research. The maintained decision, history, regressions and prior minted-record
review exist. No target-owned authored definition, causal overlay or research
file was found in those bounds; the child-specific exclusion is not an exclusion
of either target parent.

Exact-field/pipe-member scanning of every raw TSV found the target ecosystem,
ontology term and subclass rows, but no target-specific sample/study/triad/taxon
membership row. Fresh ignored-inclusive find under build, data/raw and configured
kg-microbe data found no original GOLD node/edge dumps, bulk workbook or sample/
triad intermediates. This is bounded local unavailability, not source-wide absence.

## Findings

None found: zero blockers, zero major findings, zero minor findings.
This bounded pass verifies the current representation, not the unavailable
original organism-level joins or unrelated aquarium records.

## Recommended Edits

No scientific edit is established. Preserve the ITEM decision, true enclosure
parents, exact spelling synonym, count/unit, full source path and history.
The maintained redirect at `RETIRED.tsv:101` preserves the retired minted URL;
do not remove it because the old YAML is no longer live. The child's independent
sediment parent and source-context exclusion should not be undone by this pass.

## Follow-up Checks

If original GOLD scope or membership evidence changes, reassess this exact mint
in `curation/decisions.tsv` before changing identity. Validate candidate scope,
source units and all parent contributors, dry-seed and inspect a canary, then
check labels, history, provenance, exact reproduction, redirects, semantic-map
inputs, site freshness and full QC. No observation should be invented to fill
the missing historical joins.

## Additional Notes

Only this new report was authored. No scientific/generated input, older report,
curation event, lifecycle status, history or GitHub item changed in this pass.
