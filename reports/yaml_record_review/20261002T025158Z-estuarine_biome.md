# YAML Record Review: estuarine biome

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/estuarine_biome.yaml`
- Started UTC: 2026-10-02T02:43:00Z
- Finished UTC: 2026-10-02T02:51:58Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `ENVO:01000020` |
| Label | `estuarine biome` |
| File | `data/habitats/aquatic/estuarine_biome.yaml` |
| Category | `AQUATIC` |
| Grounding | `EXACT` |
| Mapping | `SEEDED` |
| Source | PREGO `ENVO:01000020` |
| Generated status | Generated from `data/raw/*`; `data/habitats/` is read-only generated output. |

The full generated YAML was read. The record has:

- ENVO's `estuarine biome` label and definition;
- ontology parent `ENVO:00000447`;
- one PREGO attestation for `ENVO:01000020`;
- three PREGO related synonyms;
- 25 ranked PREGO taxon associations;
- no environmental parameters, evidence objects, causal graphs, discussions, datasets, or curator-authored curation events.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/estuarine_biome.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/aquatic/estuarine_biome.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus` | Passed; expected 3,206 records, found 3,206 on disk, 0 missing, 0 extra, 0 differing. |
| `just report --out /tmp/habitatmech-report.tsv` | Passed; the per-record row for `ENVO:01000020` reports `AQUATIC`, `EXACT`, `SEEDED`, source `PREGO`, 1 source, 1,160 assertions, 1 parent, 25 taxa, 0 parameters, and 0 causal graphs at `data/habitats/aquatic/estuarine_biome.yaml`. |

`iModulonDB` was not applicable: the record names no gene, locus tag, regulator, pathway, stress response, trait, or transcriptomics dataset.

## Identity and Grounding

The identity is exact. `data/raw/prego_habitats.tsv` uses `ENVO:01000020` as the PREGO habitat id, and `data/raw/ontology_terms.tsv` labels `ENVO:01000020` as `estuarine biome` with the same definition used in the generated record.

The ontology parent is supported. `data/raw/ontology_subclass_edges.tsv` has `ENVO:01000020 rdfs:subClassOf ENVO:00000447`, and `data/raw/ontology_terms.tsv` labels `ENVO:00000447` as `marine biome`.

The PREGO synonyms are supported. The PREGO source row lists `estuarine|estuarine biome|estuarines|estuarinous`; the generated record correctly omits `estuarine biome` as a self-synonym and keeps the three spelling variants as `RELATED_SYNONYM` rows from PREGO.

Ignored files were included in exact searches. `find reports/yaml_record_review -name '*estuarine_biome*' -type f` found no prior report for this record. Exact `rg --no-ignore --hidden` searches for `ENVO:01000020`, `estuarine biome`, `estuarine`, `estuarines`, and `estuarinous` over `data/raw`, maintained curation inputs, `history`, `research`, existing review reports, `data/habitats/PATHS.tsv`, `data/habitats/aquatic`, `src`, and rendered HTML found no maintained decision, term request, causal overlay, history record, or research report specific to `ENVO:01000020`.

## Evidence

| Claim | Evidence checked | Assessment |
|---|---|---|
| The record denotes `ENVO:01000020` `estuarine biome`. | `data/raw/ontology_terms.tsv` and `data/raw/prego_habitats.tsv` both carry that exact id and label. | Supported. |
| The definition is ontology-provided. | `data/raw/ontology_terms.tsv` has the generated definition text for `ENVO:01000020`. | Supported. |
| The parent is `ENVO:00000447`. | `data/raw/ontology_subclass_edges.tsv` places `ENVO:01000020` directly under `ENVO:00000447`. | Supported. |
| The PREGO attestation has 1,160 taxon assertions, score 3.0, and `annotated_genomes_isolates|environmental_samples` channels. | `data/raw/prego_habitats.tsv` row `ENVO:01000020` has `taxon_count=1160`, `max_prego_score=3`, and those channels. | Supported. |
| The 25 generated taxon rows are the top 25 PREGO rows for the source. | `data/raw/prego_habitat_taxa.tsv` rows 7353-7377 are ranks 1-25 for `ENVO:01000020` and match the generated NCBITaxon ids, labels where present, scores, and source. | Supported. |
| The PREGO taxa are associated taxa rather than characteristic taxa. | No generated row sets `is_characteristic: true`; the rows preserve PREGO ranks and scores as source associations. | Supported. |

## Completeness

No consequential gaps were found. The record already has the ontology label, definition, and parent for its exact ENVO identity plus the PREGO attestation, synonyms, and top 25 ranked taxon associations.

The empty optional slots are justified. No maintained row supplies an environmental parameter, causal graph, discussion, dataset, or literature evidence object for `ENVO:01000020`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No curation follow-up is required. If this PREGO source is later promoted from `SEEDED` to `REVIEWED`, rerun:

- `just seed`
- `just seed-canary ENVO:01000020`
- `just verify-corpus`
- `just qc`

## Additional Notes

The rendered `pages/habitats/estuarine-biome-envo-01000020.html` page mirrors the generated YAML. Existing `brackish_water` mechanism content mentions estuarine salinity gradients and estuarine bacterioplankton, but that overlay targets `ENVO:00002019` and does not assert a causal graph for `ENVO:01000020`.
