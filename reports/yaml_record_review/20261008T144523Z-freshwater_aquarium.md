# YAML Record Review: Freshwater aquarium

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/freshwater_aquarium.yaml`
- Started UTC: 2026-10-08T14:42:06Z
- Finished UTC: 2026-10-08T14:45:23Z
- Verdict: needs curation

## Target

Generated HabitatRecord `habitatmech:GOLD.772964032b`, Freshwater aquarium,
ENGINEERED / UNGROUNDED / SEEDED. The whole target and immediate Vivarium
record were read. Sole source: `Engineered > Artificial ecosystem > Vivarium > Freshwater aquarium`.
Baseline: 60bdbace5.

## Validation

- `UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/freshwater_aquarium.yaml`:
  passed, no issues.
- `UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/freshwater_aquarium.yaml`:
  passed, one file, zero errors.
- Complete parsed target equals `seed.build_document()` from a fresh full
  corpus build: one source, zero ITEM-reviewed contributors.
- Target and parent resolvers were executed with full ontology, mapping and
  claimant indexes; the source mints were recomputed.
- Full QC is reused, not rerun for report-only changes. Fresh same-turn tree
  comparison proves baseline 60bdbace5 equals validated 9b901cc28: 592 tests
  passed, three skipped, all remaining local gates passed, including 3,207
  strict-valid/reproduced records, 189 histories, provenance, site, terms and
  redirects. OAK and queue checks passed: [PR #1725 receipt](https://github.com/CultureBotAI/HabitatMech/pull/1725#issuecomment-6062037613).
- Original node-to-organism/sample joins and SSSOM/KGX compatibility were not
  independently verified.

## Identity and Grounding

The full-path mint and `PATHS.tsv:2163` agree. This source names a freshwater
aquarium within Vivarium, not freshwater material, a natural lake, fish taxon,
or aquarium sediment. ENGINEERED is consistent with that enclosure context.

The default `gold_unmatched` route remains UNGROUNDED after the CLASS
CONFIRM_UNGROUNDED decision at `curation/decisions.tsv:707`. No mapping
predicate is emitted. SEEDED and the two generated events faithfully expose
the class-level screen rather than claiming ITEM review. However, the absence
of a lexical match is not an adequate current scientific grounding assessment.

Active ENVO:00002198, canonical label fresh water aquarium, is already in
the vendored slice. Its definition is an aquarium with freshwater as its
primary ecological medium. The spelling difference between Freshwater and
fresh water does not supply a biological distinction. Both the source path
and typed ontology hierarchy support the enclosure-with-medium interpretation.
The broader generic aquarium ENVO:00002196 and saline-water sibling
ENVO:00002197 must not replace the more specific matching candidate.

The sole current parent ENVO:00010622 vivarium is supported. It comes from
parent mint `habitatmech:GOLD.d379e579ab`, automatically resolved by
`gold_leaf_label` without a decision. ENVO independently places freshwater
aquarium under aquarium under vivarium. This is a valid broader-habitat
relation, not merely a location edge to remove.

## Evidence

- `gold_ecosystem_paths.tsv:770` contains nodes 8025/8026, the exact path,
  two ORGANISM assertions and zero other tree counters. The generated
  first-node display, two-node collapse note, count/unit, missing predicate
  and old history reproduce correctly. Two assertions are not two named
  characteristic organisms or a complete ecological community.
- Fresh [GOLD workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths),
  `site data` row 58, confirms node 8026 and the exact target path. Row 57
  separately names the Sediment child, node 8037; rows 62-64 separately name
  the Seawater aquarium branch and its material children. The source tree
  distinguishes the aquarium setting from sampled sediment/biofilm.
  Worksheet dimensions were reset before full iteration. SHA256
  `f8e4cb5cf89ecc88d3cf28170cfc3a1cf47daed8218408a52914c53667dfd3d4`.
  This does not reconstruct historical node 8025 or original organism joins.
- Fresh [pinned ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
  confirms active ENVO:00002198, ENVO:00002196, ENVO:00002197 and
  ENVO:00010622, their definitions and typed edges. SHA256
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
  Local named edges at `ontology_subclass_edges.tsv:5393` and `:5391`
  preserve fresh water aquarium -> aquarium -> vivarium. A salinity-specific
  sibling is not an exact substitute.
- Complete current in-memory corpus membership and ignored-inclusive
  data/habitats, curation and history searches find no existing live
  ENVO:00002198 record/decision in those bounds. The ontology term does exist;
  its absence from the live habitat corpus must not become a novel-term request.

## Completeness

No definition, synonyms, xrefs, parameters, named taxa, evidence objects,
mechanism graphs, discussions or datasets are asserted. Their optional
absence is not a separate finding. Existing ENVO could supply a supported
definition after an ITEM grounding decision; do not invent a novel definition,
tank size, temperature, fish community or numerical salinity measurement.
iModulonDB is not applicable: no strain-specific gene, regulator or expression
claim is made.

Ignored-inclusive identifier, label, stem, full path and source-node searches
covered curation, raw inventories, PATHS/RETIRED, configuration, docs, tests,
history, research and reports. Filename traversal included ignored files
under curation/history/research. Beyond the CLASS row, no target-owned
definition, exclusion, overlay, separate history, research file or earlier
individual target review was found within those bounds. Sibling Seawater
aquarium and Vivarium reports are not reviews of this target.

An exact-field/pipe-member scan of every raw TSV found only the target
ecosystem row, not sample/study/triad/parameter/taxon memberships. Its
Sediment child's single organism is not this record's observation. Same-turn
ignored-inclusive find under build, data/raw and configured kg-microbe data
found no original GOLD dumps, bulk workbook or sample/triad intermediates.
Original sample-level reconstruction remains unavailable locally.

## Findings

1. **Major: the ungrounded decision misses an existing matching ENVO concept.**
   ENVO:00002198 fresh water aquarium is present, active, defined and
   consistent with the full source path. The CLASS lexical miss leaves this
   source unharmonized and undefined despite that concrete candidate.
   Maintained owner: ITEM curation of `habitatmech:GOLD.772964032b` in
   `curation/decisions.tsv`. This is not an invalid vivarium parent, a need
   for an ontology import, or justification for broad global whitespace rules.

No separate blocker or minor finding.

## Recommended Edits

Perform the explicit ITEM scope check and, if no contrary original-source
restriction emerges, GROUND this source to ENVO:00002198 with its exact
canonical label. The source path, candidate definition and typed ancestry
support that specific curation direction. Do not ground it merely to freshwater
material, generic aquarium, saline water aquarium or the Sediment child.
Keep source nodes, count/unit, full path and audit provenance. Retain the
valid vivarium contribution and inspect the candidate's direct aquarium parent.

## Follow-up Checks

Confirm the final source-to-candidate scope and label, then dry-seed and inspect
a canary. Regress the identifier transition, source mapping endpoints,
hierarchy, count preservation, contributor-derived status and Sediment child
reference. Append session history and use the maintained PATHS/redirect
workflow for any retired minted page. Run schema, labels, provenance, history,
exact reproduction and full QC; regenerate actual semantic-map/site changes.
No source count should be converted to a taxon list or biological parameter.

## Additional Notes

Only this timestamped report was written. No scientific/generated artifact,
historical report, curation event, lifecycle status or GitHub item changed.
General web results about museum aquariums were not used as evidence for
GOLD's original members or as substitutes for the inspected primary ontology.
