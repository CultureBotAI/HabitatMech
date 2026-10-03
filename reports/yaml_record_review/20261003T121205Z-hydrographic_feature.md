# YAML Record Review: hydrographic feature

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/hydrographic_feature.yaml`
- Started UTC: 2026-10-03T12:10:00Z
- Finished UTC: 2026-10-03T12:22:53Z
- Verdict: pass with minor issues

## Target

The complete generated `HabitatRecord` was read: `ENVO:00000012`, hydrographic
feature, `AQUATIC`, `EXACT`, `SEEDED`. It includes an ENVO definition, 13
source-qualified synonyms, one parent, one PREGO attestation, 25 associated
taxa, and one seed-history event. `data/habitats/PATHS.tsv:432` locks the stem.
The PREGO source key recomputes to `habitatmech:PREGO.79534379c9`.

## Validation

- `just validate data/habitats/aquatic/hydrographic_feature.yaml`: pass.
- `just validate-strict data/habitats/aquatic/hydrographic_feature.yaml`:
  one record, zero errors.
- All 25 complete taxon dictionaries match the named raw PREGO columns,
  including the absent label on rank 17.
- Current OLS verified identity, definition, synonym, and the geographic-feature
  parent. NCBI EFetch returned 25 taxon records: 24 unchanged IDs and one
  explicit replacement/alias mapping, checked separately.
- Baseline `just qc`: all gates passed; 451 tests passed, three skipped,
  two dependency warnings; 3,206 records reproduce and validate, with current
  site/redirects. OAK label correspondence is a separate CI gate.
- No PMID, DOI, mechanism edge, gene, regulator, or transcriptomic dataset is
  asserted. A causal or iModulonDB evidence lookup is not applicable here.

## Identity and Grounding

PREGO names `ENVO:00000012` itself, so grounding is identifier-based rather
than a potentially ambiguous synonym match. `data/raw/ontology_terms.tsv:6610`
and live OLS agree on the water-associated geographic-feature definition and
the ENVO synonym `fluvial feature`. This broad class must not be silently
replaced by `ENVO:00000063` water body or `ENVO:00000409` whirlpool just because
those records also carry overlapping vocabulary.
[Hydrographic feature](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000012).

The parent `ENVO:00000000` geographic feature is current and supported by
`ontology_subclass_edges.tsv:4639` and live OLS. OLS additionally returns
`RO:0002577` system, an external upper-level term not emitted by this vendored
habitat slice. The record does not claim that its displayed habitat parent
list is the full current imported ontology closure. This is not an unsupported
parent. [Geographic feature](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000000).

The target has no ITEM curation decision; `SEEDED` correctly communicates
that fact. This report is not a status-promotion decision.

## Evidence

| Claim | Inspected evidence |
|---|---|
| PREGO occurrence/count/channel | `data/raw/prego_habitats.tsv:60` records 1,427 taxa, a separate 1,427 direct-assertion count, maximum score 1.81611, and `environmental_samples`. The generated unit remains TAXON. Equal counters do not make their meanings interchangeable. |
| Synonyms | The generated ENVO exact synonym comes from the ontology slice; all other forms come from the PREGO row and are RELATED_SYNONYM, not exact ontology labels. Duplicate text across sources retains separate provenance. |
| All 25 taxon entries | `prego_habitat_taxa.tsv:3138-3162` supplies ranks 1-25, scores 1.81611 through 1.7424, candidate pool 1,427, and the corresponding source names. Every generated dictionary matches. No characteristic-status or measured-abundance assertion is added. |
| Taxon identity maintenance | NCBI returns 24 original IDs with the supplied names among current names/aliases. Querying `342610` returns `3042615`, Paraglaciecola sp. T6c, explicitly listing 342610 as an alternate ID and historical T6c names. |
| Missing rank-17 label | The raw taxon row itself has an empty label. The generated omission is faithful and schema-valid, not a fabricated name or local data loss. |

The current replacement identifies the same strain lineage rather than a new
habitat association: [NCBI taxonomy replacement](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3042615).
The structured EFetch response lists alternate ID 342610 and the names
Paraglaciecola atlantica T6c and Pseudoalteromonas atlantica T6c. Updating this
source reference should preserve that identity trail.

## Completeness

No habitat-specific pH, salinity, temperature, causal mechanism, or
characteristic-taxon claim is required for this broad source concept.
The environmental-sample channel does not establish which sampled feature,
strain physiology, or causal mechanism produced an association.

Hidden/ignored-inclusive searches covered ID, label, stem, and minted key in
`curation`, `history`, `research/habitats`, `conf`, relevant raw tables, and the
path lock. They found no target-specific decision, term request, overlay,
research report, or session history. Structured scans of GOLD paths, Madin
habitats, and environment-parameter rows found no exact ID or label-substring
match. Exact `Record:` header coverage, including ignored files, found no
previous individual report. These are bounded repository misses, not proof
that hydrographic features lack microbiological literature.

## Findings

1. **Minor: an associated taxon uses a retired identifier and lacks a display
   label.** Rank 17 keeps `NCBITaxon:342610`; NCBI explicitly redirects it to
   `NCBITaxon:3042615`, Paraglaciecola sp. T6c. The association remains traceable
   and there is no conflicting strain claim. Owner: PREGO taxon extraction and
   label resolution in `src/habitatmech/extract.py`, together with its governed
   source snapshot and regenerated `data/raw/prego_habitat_taxa.tsv`. Do not
   hand-edit the generated record or silently rewrite the original source ID.

Blockers and major findings: none. Total: zero major, one minor.

## Recommended Edits

During a controlled source refresh, resolve taxon aliases against a versioned
NCBI mapping, retain the original source identifier as provenance, and supply
the current T6c identifier/name without changing its score, rank, or association
count. Apply deduplication only after checking whether other rows already use
the replacement ID. A new mechanism graph or ITEM review is not needed merely
to repair this source reference.

## Follow-up Checks

Test the old-to-current taxon mapping and preservation of source rank/score,
including the case where both identifiers occur. Validate inventory provenance,
run dry seeding and a forced canary, inspect all affected records, then run
focused strict validation and `just verify-corpus`. If adding the taxon label
changes semantic input, rebuild/validate the complete map and render before
full QC. Do not bypass the generated-file or provenance checks.

## Additional Notes

PREGO's unusual lexical forms, including `OVERFALLSs` and `overfallses`, are
retained as source-reported related synonyms. They are not evidence for a
different canonical identity and should not be indiscriminately normalized
without a separate source-quality policy. No corpus or curation input changed.
