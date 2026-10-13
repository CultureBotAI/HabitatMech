# YAML Record Review: industrial waste material

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/industrial_waste_material.yaml`
- Started UTC: 2026-10-08T23:57:49Z
- Finished UTC: 2026-10-09T00:03:22Z
- Verdict: needs curation (0 blocker, 1 major, 0 minor)

## Target

Read the entire generated HabitatRecord ENVO:00002267 at baseline
`d054c5813515fa33ec1872de1b44ebac948ee50e`: ENGINEERED / CLOSE / REVIEWED,
with an ENVO definition, two source-qualified synonyms, two parents, one GOLD
attestation and three generated events. The complete waste material and Solid
Waste parent records were read for context, not counted as separate reviews.
The target is manufacturing-derived waste material, not its production
activity, an individual waste stream, or its Composting child.

## Validation

Fresh commands used `UV_CACHE_DIR=build/uv-cache`:

- `just validate data/habitats/engineered/industrial_waste_material.yaml`:
  no issues.
- `just validate-strict data/habitats/engineered/industrial_waste_material.yaml`:
  one file, zero errors.
- `just verify-corpus`: 3,208 expected/present, zero missing/extra/differing.
- `just validate-history`: 205 valid records.
- `just provenance-check`: 14 inventories and two GOLD sources current.

Full-index in-memory construction and `build_document()` matched the entire
parsed target: one source, one ITEM-reviewed contributor, no authored
definition and no target-owned GOLD parent exclusion. Both target and source
parent resolutions were evaluated with complete mapping and claimant indexes.

Full QC was not rerun during this read-only review. The unchanged baseline's
immediately preceding local publication run passed 620 tests with three skips
and all gates (`build/pr-industrial-production-qc.log`); its native queue
[QC run](https://github.com/CultureBotAI/HabitatMech/actions/runs/37861582587)
also passed on this exact commit, as did
[label correspondence](https://github.com/CultureBotAI/HabitatMech/actions/runs/37861582591).
The label checker does not verify synonym scope and has no MeSH adapter.
Scientific inputs, implementation, tests and generated products remain
unchanged. No original organism-member reconstruction or export audit was done.

## Identity and Grounding

The ontology identifier, label, definition and `PATHS.tsv:695` agree. The
recomputed source mint is `habitatmech:GOLD.8faa599672`. Its default route is
`gold_leaf_synonym`, yielding ENVO:00002267 / CLOSE / skos:closeMatch. The
ITEM REVIEW at `curation/decisions.tsv:1745` endorses that resolution through
`curated_review_of_gold_leaf_synonym`, explaining REVIEWED. This is a close
source association, not an exact equivalence claim.

The inspected [pinned ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
confirms the active label, manufacturing-origin definition and direct named
superclass ENVO:00002264, waste material. It types `industrial waste` as
`hasBroadSynonym`. The target instead emits that ENVO alias as EXACT_SYNONYM.
The separate GOLD `Industrial waste` label correctly retains RELATED_SYNONYM
and its SOURCE_SYNONYM_SCOPED event. That source-label safeguard does not fix
the independent ontology alias.

The MeSH parent comes from GOLD's immediate `Engineered > Solid waste` path,
mint `habitatmech:GOLD.4233e9003d`, resolved through `gold_mapping_table` to
mesh:D062611. Primary [NLM descriptor](https://id.nlm.nih.gov/mesh/D062611.json)
and [preferred concept](https://id.nlm.nih.gov/mesh/M0568791.json) responses
confirm active Solid Waste and its scope. That scope covers refuse/sludge and
specified solid, semi-solid or contained material, while excluding specified
dissolved sewage, irrigation-return and industrial-discharge material. A
liquid-versus-solid label comparison alone cannot disprove the parent. The
source classification is supported; original member descriptions and universal
subsumption of the wider ENVO class were not established here. No automatic
parent deletion is justified by this review.

## Evidence

- `data/raw/gold_ecosystem_paths.tsv:537` contains the exact depth-three
  path, nodes 4937/7131/7132, nine ORGANISM assertions and zero direct
  study/biosample counts. The generated first ID, full path, three-node note,
  count and unit agree. The parent's 81 organisms are a separate source
  count, not target members or a denominator.
- An exact-field/pipe-member scan of all 14 raw TSVs found the target
  ecosystem, ontology and mapping rows, but no exact target biosample,
  study, triad, taxon or parameter row. This is bounded inventory absence,
  not evidence that the original organisms or studies do not exist.
- `isolation_source_groundings.tsv:159` separately maps BacDive's
  Industrial-waste label to this ENVO ID. That row is not this GOLD route:
  the earlier synonym route wins. No BacDive attestation or strain count
  is present in the target, and none was imported into its interpretation.
- Fresh [GOLD classification workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths)
  parsing confirms node 7132 at `site data` row 407, with two Unclassified
  fillers after Industrial waste. Rows 404-406 are distinct child paths.
  The workbook confirms current classification, not historical nodes 4937
  and 7131 or the nine organism assertions. Its 84,174 bytes have SHA256
  `f8e4cb5cf89ecc88d3cf28170cfc3a1cf47daed8218408a52914c53667dfd3d4`.
- The inspected ENVO OWL has SHA256
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
  Complete target/genus class elements, including synonym predicate and
  subclass statements, were inspected, not only search snippets.
- `ontology_terms.tsv:7342` preserves only an untyped synonym pipe.
  `_load_tsv_ontology` in `src/habitatmech/extract.py` copies the upstream
  KGX synonym string, and `ConceptStore.get` in `src/habitatmech/seed.py`
  emits every imported ontology alias as exact. Exact corpus reproduction
  therefore does not establish the stronger synonym claim.

## Completeness

No taxon, environmental parameter, xref, mechanism, discussion or literature
assertion needs to be invented from an anonymous organism count. Parent or
child taxa are not target taxa. iModulonDB is not applicable to the claims in
this record. Optional empty fields are not findings.

Ignored-inclusive identifier, source-mint, label/stem, source-path and node
searches covered curation, raw inventories, PATHS, history, research,
configuration and individual reports. They found the ITEM decision and
contextual child/waste-gas material, but no target-owned authored definition,
parent exclusion, causal overlay, session history, research dossier or earlier
individual target review within those bounds. Those contextual reviews are
not independent scientific evidence. The original nine-organism crosswalk
was not reconstructed; a current classification list cannot substitute for it.

## Findings

1. **Major: a broad ontology synonym is promoted to exact.** ENVO's typed
   `hasBroadSynonym` assertion for `industrial waste` contradicts the
   target's ENVO EXACT_SYNONYM. This is a concrete additional witness for
   [#1249](https://github.com/CultureBotAI/HabitatMech/issues/1249), freshly
   verified OPEN. Owners: the provenance-bound ontology acquisition and
   extraction contract in `src/habitatmech/extract.py`, followed by synonym
   loading/emission in `src/habitatmech/seed.py`. The existing schema already
   permits BROAD_SYNONYM. No blocker or minor finding.

## Recommended Edits

Recover typed ontology synonym assertions through a reproducible governed
refresh and emit the actual broad scope. Preserve the independent GOLD
related synonym and source path/count. Do not hand-edit generated YAML,
patch checksums, or globally downgrade genuinely exact aliases. Reassess
the source resolution if restoring typed synonyms changes its lexical route;
this review does not establish a replacement identity or an automatic parent
exclusion. No change to the target's lifecycle is made by publishing a report.

## Follow-up Checks

Add a regression for this broad alias alongside exact, narrow, related,
unknown-scope and mixed-source cases. Preserve the nine ORGANISM assertions,
three nodes, source mint and independent waste-material superclass. Later
authorized curation should append history, dry-seed, inspect a target canary,
then run strict/history/provenance/label, corpus reproduction, site and full
QC checks. Compare semantic-map input bytes before deciding on a rebuild.
Recover source members before making stronger claims about material phase,
excluded dissolved streams, constituent chemistry or ecological mechanisms.

## Additional Notes

Only this timestamped report was authored. No scientific input, generated
record/page, old report, history, status or GitHub state changed. The first
OLS request failed; pinned primary OWL supplied the term evidence. The NLM
HTML shell supplied no concept content; the JSON descriptor/concept did.
An initial raw-table probe stopped on an unrelated extra-column biosample
row; a corrected CSV scan flattened surplus cells and completed all tables.
The extra row concerns Hadopelagic zone/Ocean trenches, not this target.
Neither that probe correction nor this report changes an inventory.
