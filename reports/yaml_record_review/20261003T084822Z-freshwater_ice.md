# YAML Record Review: freshwater ice

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/freshwater_ice.yaml`
- Started UTC: 2026-10-03T08:48:22Z
- Finished UTC: 2026-10-03T08:49:49Z
- Verdict: needs curation

## Target

The complete generated `HabitatRecord` denotes `ENVO:01001511`, freshwater
ice, in category `AQUATIC`, with `EXACT` grounding and `SEEDED` mapping.
Its source concept is `habitatmech:GOLD.c18afe6ef1`, derived from
`Environmental > Aquatic > Freshwater > Ice`; its pinned slug is at
`data/habitats/PATHS.tsv:892`. Review baseline:
`3cfdfff350ad925214be41e08836ad2783d0ef80`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/freshwater_ice.yaml` | Pass; no issues found |
| `just validate-strict data/habitats/aquatic/freshwater_ice.yaml` | Pass; one record, zero errors |
| Live OLS checks | Target, all three parents, and relevant solid/liquid ancestry inspected; IDs active |
| Full `just qc` | Running for this report-only branch when this individual review finished; final result belongs to the batch PR |

No literature references or causal graphs occur in this target. The full OAK
label gate was not rerun specifically for this report; relevant ontology IDs
were checked directly. Structural validity and faithful reproduction do not
make an inherited source-context edge scientifically valid.

## Identity and Grounding

`data/raw/gold_ecosystem_paths.tsv:223` supports the exact four-level path,
two source nodes (`3785`, `4061`), and 81 organism assertions. The composed
label freshwater ice is an exact ENVO label; the target is not generic ice,
water ice, a glacial lake, or liquid fresh water. The exact lexical resolution
does not constitute item review, and `SEEDED` correctly records that limit.

The [current ENVO term](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001511)
defines this material by freezing fresh water. The committed term row
`ontology_terms.tsv:9004` has no definition, explaining its omission from
the generated record; a future source refresh can supply the newer definition.

The direct ENVO parents are `ENVO:01000277` water ice and `ENVO:02000140`
fluid environmental material, matching both live OLS and
`ontology_subclass_edges.tsv:7382-7383`. The additional `ENVO:00002011`
parent comes from the GOLD Freshwater path. That term specializes liquid
water (`ontology_subclass_edges.tsv:5272`), while ice specializes solid
environmental material through `ENVO:01001125` (row 6939). A freezing input
or source context is not an is-a superclass of the resulting ice.

The fluid-material parent is an upstream ENVO assertion, not another GOLD
addition. Its shear-response definition and the simultaneous solid ancestry
deserve ontology-level clarification. This review does not claim that fidelity
to ENVO independently proves the intended rheological interpretation, nor
does it prescribe deleting an ontology edge with a source-path exclusion.

## Evidence

| Claim | Inspected support | Assessment |
|---|---|---|
| `EXACT`, `skos:exactMatch`, source ID/path and category | GOLD row 223; composed-label route in `resolve_gold` | Supported as the current automatic resolution |
| 81 ORGANISM assertions | `organism_count=81`, two nodes in raw GOLD row | Correct unit; row's zero study/biosample counters are not absence claims about separate API inventories |
| Eleven biosamples | `gold_path_biosamples.tsv:611`, path node 4061 | Context inventory only; not an additional organism count |
| Environmental triads | `gold_path_triads.tsv:293-295`, eight samples across three studies | Broad aquatic biome and local saline lake each have share 0.38 and one agreeing study; medium ice has share 1.00 and three agreeing studies |
| Study crosswalk | Five exact path memberships in `gold_studies.tsv` | Source provenance, not five mechanistic citations or a replacement assertion count |
| Source alias `Ice` | GOLD leaf label with GOLD provenance | Path-qualified source spelling; not justification to merge generic ice with freshwater ice |
| Fresh-water is-a parent | Only the resolved immediate GOLD path | Unsupported phase substitution; see finding |

The triads describe different environmental roles. A saline-lake local-scale
annotation does not itself establish the salinity of the ice; neither this
minority local context nor the generic ice medium can automatically replace
the qualified source identity. No taxon or mechanism is inferred from counts.

## Completeness

Ignored/hidden-inclusive searches across `curation`, `history`, `research`,
`conf`, `data/raw`, `reports/yaml_record_review`, and the slug lock used the
target ID, source-concept ID, exact source path, label, source node, and slug.
No target item decision, authored definition, causal overlay, research report,
or prior target review was found in those locations. Cryoconite review mentions
concern a different target and do not count as this record's review.

The inspected record has no taxa, parameters, authored evidence, graphs,
discussions, or datasets. Those optional omissions are not defects merely
because literature about freshwater ice exists. The available source slices
do not identify the 81 organisms individually.

## Findings

One major; zero blockers; zero minor.

**HM-FRESHWATER-ICE-001 (major): liquid fresh water is an unsupported parent.**
`src/habitatmech/seed.py:ingest_gold` adds `ENVO:00002011` solely because the
source path is nested under Freshwater. The
[liquid-water definition](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002006)
and [ice definition](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001125)
make the phase mismatch explicit. A future maintained GOLD parent exclusion
must target source `habitatmech:GOLD.c18afe6ef1`, not remove all ontology
parents or rewrite the raw source path. Related infrastructure is proposed in
draft PR #1218; it is not part of this review baseline.

## Recommended Edits

1. After the maintained source-parent exclusion interface is available, exclude
   this source concept's `ENVO:00002011` contribution. Preserve the target ID,
   source path/count, source node note, and independent ENVO parents.
2. Review the upstream fluid-material assertion separately against ENVO's
   intended physical-state/rheology modeling. An upstream correction belongs in
   ENVO followed by a provenance-tracked ontology refresh, not a handcrafted
   generated-record patch.
3. An item review can endorse the qualified identity and a later source refresh
   can supply ENVO's definition. Do not promote mapping status from this report.

## Follow-up Checks

Run `just seed` and `just seed-canary ENVO:01001511 --force`; inspect the
source-specific parent removal, preserved ontology parents and 81-organism
attestation. Run focused schema/strict validation, `just validate-products`,
and `just verify-corpus`. Record actual curation history, refresh the full
semantic map when parent text changes, then `just render` and `just qc`.
Check descendant records without assuming their source-path parents are is-a.

## Additional Notes

iModulonDB is not applicable: no gene, regulator, taxon, or expression claim
occurs here. GOLD verification used committed inventories rather than an
authenticated live query. Searches located ecological papers, but unavailable
full-page responses were not treated as inspected evidence. This report does
not edit generated data or implement either hierarchy correction.
