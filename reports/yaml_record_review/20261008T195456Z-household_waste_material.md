# YAML Record Review: household waste material

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/household_waste_material.yaml`
- Started UTC: 2026-10-08T19:50:52Z
- Finished UTC: 2026-10-08T19:54:56Z
- Verdict: needs curation (0 blocker, 1 major, 0 minor)

## Target

Read the complete generated HabitatRecord ENVO:01000372 at
`55b6ab62ae8585358b44db80e681000a02ebb3ec`: ENGINEERED / CLOSE / REVIEWED,
with an ENVO definition, two provenance-qualified synonyms, two parents,
one GOLD attestation and three generated events. There are no taxon,
parameter, xref, causal-graph, discussion or literature assertions.
The complete Solid Waste parent was read as context, not counted as a
separate completed review. Earlier interrupted exploration was resumed by
rereading the target and rerunning the primary-source checks.

## Validation

Fresh commands used `UV_CACHE_DIR=build/uv-cache`:

- `just validate data/habitats/engineered/household_waste_material.yaml`:
  no issues.
- `just validate-strict data/habitats/engineered/household_waste_material.yaml`:
  one file, zero errors.
- `just verify-corpus`: all 3,208 records reproduce, with zero missing,
  extra or differing files.
- `just validate-history`: all 201 session histories valid.
- `just provenance-check`: 14 inventories and two GOLD sources current.

Fresh full-index construction exactly reproduces the complete parsed target:
one contributor, one ITEM-reviewed contributor, the two recorded parents,
and no authored definition or GOLD-parent exclusion. The default and applied
GOLD resolutions were evaluated directly. A probe initially used `path`
instead of the actual `canonical_path` column; the corrected probe completed.

Full QC was not rerun for report-only work. Guidance, implementation, inputs,
tests and generated records are unchanged from c6c94db6f, whose inspected
`build/pr1743-qc.log` records 597 passing tests, three skips and all local
gates passed. Prior label correspondence has no MeSH adapter and does not
check synonym predicates. Direct primary checks below address those limits;
neither local QC nor this review establishes successful pending CI or
SSSOM/KGX modeling compatibility.

## Identity and Grounding

`PATHS.tsv:842` agrees with the ontology ID and filename. The recomputed
source key is `habitatmech:GOLD.f4c1f8a330`. Its default `gold_leaf_synonym`
route yields ENVO:01000372 / CLOSE / skos:closeMatch. The ITEM REVIEW at
`curation/decisions.tsv:1744` endorses that route without adding a target,
parent or xref, explaining REVIEWED. This is not an EXACT source mapping.

Fresh [pinned ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
confirms the canonical label, residential-origin definition and named
superclass ENVO:00002264, waste material. The material is a plausible
microbial habitat; it is not the act of disposal, its composting child or
the household building. No deprecation assertion appears on either class.

The ontology types `household waste` as `hasBroadSynonym`, not exact. The
record instead emits EXACT_SYNONYM attributed to ENVO. The distinct GOLD
label `Household waste` correctly retains RELATED_SYNONYM under the CLOSE
source guard; that correction does not fix the independent ontology entry.

The second parent, mesh:D062611, comes from the GOLD path's Solid waste
ancestor. Its source mint is `habitatmech:GOLD.4233e9003d`, resolved through
`gold_mapping_table`. Fresh [MeSH descriptor](https://id.nlm.nih.gov/mesh/D062611.json)
and [preferred concept](https://id.nlm.nih.gov/mesh/M0568791.json) confirm
active Solid Waste and its scope, including refuse, sludge and contained
material while excluding specified dissolved waste streams. The explicit
GOLD path supports that source classification. Merely observing that some
household waste is liquid does not disprove this MeSH parent. No specific
counterexample to the record's parent was established; source classification
is not an original-member audit or proof about every possible residential
waste stream.

## Evidence

- `gold_ecosystem_paths.tsv:1367` supplies depth three, three collapsed nodes
  4905 / 8154 / 8155, and zero direct organism/study/biosample totals in that
  extraction. The record shows the first ID and explicitly notes the collapse.
  Omitting assertion_count/unit for zero direct assertions is consistent with
  the generator, not evidence that the habitat has no organisms.
- The separate bulk-export inventory `gold_path_biosamples.tsv:881` records
  two BIOSAMPLEs for node 8155. `gold_studies.tsv:1608` records Gs0130338
  across four paths: this target, Food waste, Anaerobic bioreactor and its
  Leachate child. These are not target-specific organism counts or proof that
  every sample/study belongs exclusively to household waste.
- `ontology_terms.tsv` logical row 7868 (physical line 7874) supplies the
  definition and untyped synonym pipe. `ontology_subclass_edges.tsv:6096`
  supplies the waste-material parent. `ConceptStore.get` in
  `src/habitatmech/seed.py:412` converts every imported ontology alias to
  EXACT_SYNONYM. `_load_tsv_ontology` in `src/habitatmech/extract.py:778`
  retains the upstream untyped KGX pipe. The primary OWL disproves the
  stronger emitted scope, even though reproduction is exact.
- Fresh [GOLD ecosystem workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths)
  contains node 8155 under the target with two Unclassified fillers and
  node 4907 under its Composting child. Fresh
  [GOLD organism tree](https://gold.jgi.doe.gov/download?mode=organismEcosystemsJson)
  shows branch count six, entirely in Composting, and zero in the target's
  Unclassified chain. Do not assign the child's six ORGANISM assertions
  to this direct target or sum repeated ancestor/Unclassified counts.

## Completeness

Ignored-inclusive content searches for the target ID, source mint, label,
stem and representative GOLD ID covered curation, all raw inventories,
PATHS/RETIRED, configuration, docs, tests, history, research and individual
reports. Filename traversal also covered curation/history/research. The
decision and related child/study reports were found; no target-owned
authored definition, overlay, parent exclusion, session history, research
dossier or prior individual report was found within those bounds. Incidental
Dust/ash research mentions are not primary target evidence.

A complete CSV exact-field/pipe-member scan of every raw TSV found the
target path, separate biosample and study rows, and ontology rows. No direct
target triad, parameter or taxon row was found. Ignored-inclusive `find`
under build, data/raw and the configured kg-microbe data directory found
none of the named original GOLD node/edge dumps, goldData.xlsx,
gold_biosample_triads.tsv or biosample JSONL files. Both manifests preserve
source receipts, not the missing member joins. Optional ecology and
mechanisms should not be inferred from generic waste literature.
iModulonDB is not applicable: no gene, regulator or expression claim exists.

## Findings

1. **Major: ENVO broad synonym is promoted to exact.** The primary typed
   assertion for `household waste` conflicts with the generated ENVO
   EXACT_SYNONYM. This is another concrete witness of
   [#1249](https://github.com/CultureBotAI/HabitatMech/issues/1249), freshly
   verified OPEN. Maintained owners are the ontology acquisition/extraction
   contract and `src/habitatmech/extract.py`, then ontology synonym loading
   and emission in `src/habitatmech/seed.py`. The existing schema already
   permits BROAD_SYNONYM. Zero blockers and zero minor findings.

## Recommended Edits

Recover typed synonym predicates through a reproducible, provenance-bound
source refresh; retain ENVO's broad assertion and the independent GOLD
related assertion. Do not hand-edit this YAML, globally downgrade genuine
exact synonyms or patch inventory checksums. A flat-pipe lexical match alone
must not become evidence of source equivalence. Reassess the target's
mapping with source context if typed-synonym changes affect its resolver;
no replacement identity or automatic parent deletion is established here.

## Follow-up Checks

Add a regression for this ENVO broad synonym alongside exact/narrow/related,
unknown-scope and mixed-source cases. Preserve the source mint, three-node
collapse, separate count units and waste-material superclass. Verify the
GOLD source relation independently of the ontology alias. With curation
authorized, record append-only history, dry-seed, inspect the target canary,
then run provenance, strict/history/label, exact-corpus, site and full QC
checks. Compare semantic-map inputs before deciding whether to rebuild.
Original source-member recovery is needed for stronger membership claims.

## Additional Notes

Only this new report was written; no scientific input, generated artifact,
old report, history, status or GitHub item was changed. The first issue read
failed to connect; a repeated read succeeded. Primary bytes were parsed in
memory, not installed as refreshed inventories:

- ENVO: 9,614,229 bytes, SHA256
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
- GOLD workbook: 84,174 bytes, SHA256
  `f8e4cb5cf89ecc88d3cf28170cfc3a1cf47daed8218408a52914c53667dfd3d4`.
- GOLD tree: 1,450,415 bytes, SHA256
  `49ef0a3e654a79f6b7e7140d2cdb2ac0ce0bb1df2ccb8decae68d129eeb7ca11`.
- MeSH descriptor/concept: 2,538 / 1,244 bytes; SHA256 respectively
  `c8d7c3d97743516fd01aca9d2557dff4c8129ade61c144d9d6eea96c7d8020be`
  and `fd053e6e3d981eac537719f71ba518297a3eb4b044fd80906b3a4eee5045fc54`.
