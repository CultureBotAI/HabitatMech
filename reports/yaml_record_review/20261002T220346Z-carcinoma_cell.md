# YAML Record Review: carcinoma cell

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/carcinoma_cell.yaml`
- Started UTC: 2026-10-02T22:03:46Z
- Finished UTC: 2026-10-02T22:03:46Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `BTO:0000176` |
| Label | carcinoma cell |
| Definition source | `BTO` |
| Habitat category | `HOST_ASSOCIATED` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Parent habitats | `BTO:0000415` epithelioma cell |
| Source concepts | PREGO `BTO:0000176`; source curation key `habitatmech:PREGO.01336cc428` |
| Generated path | `data/habitats/host_associated/carcinoma_cell.yaml` |

The record is generated from one direct PREGO source row plus the vendored BTO
slice. It preserves the BTO carcinoma-cell definition, the BTO superclass
`epithelioma cell`, nine non-canonical PREGO synonyms, one direct PREGO taxon
assertion, one retained PREGO taxon row, no environmental parameters, no xrefs,
no curator-authored evidence block, no causal graph, and no maintained
item-level decision row for its PREGO source key.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/carcinoma_cell.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/host_associated/carcinoma_cell.yaml --out /tmp/habitatmech-bto-carcinoma-cell-instance-validation.tsv --quiet` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus` | Passed; 3,206 expected records, 3,206 found, 0 missing, 0 extra, 0 differing. |
| `just validate-causal-all` | Passed; 32 curation files and 32 graphs validated. |
| `just term-requests-check` | Passed; the generated ENVO term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records validated. |
| `just worklist --status all --out /tmp/habitatmech-bto-carcinoma-cell-worklist.tsv` | Passed; wrote 953 all-status ungrounded rows, none for `BTO:0000176`. |
| `just report --out /tmp/habitatmech-bto-carcinoma-cell-report.tsv` | Passed; row for `BTO:0000176` reports `HOST_ASSOCIATED`, `EXACT`, `SEEDED`, one PREGO source, one assertion, a definition, one parent, no parameters, one retained taxon, and no causal graphs. |
| `git diff --check` | Passed before this report was written. |
| `just validate-products` | Not run locally; this report does not change any grounding, and the pull request's `label-correspondence` workflow is the blocking OAK-based id-label gate. |

## Identity and Grounding

- `data/habitats/PATHS.tsv` pins `BTO:0000176` to `carcinoma_cell`,
  matching `data/habitats/host_associated/carcinoma_cell.yaml`.
- `data/raw/ontology_terms.tsv` contains `BTO:0000176` with label
  `carcinoma cell` and a BTO definition for a malignant epithelial new-growth
  cell. The generated record preserves this identifier, label, definition, and
  `definition_source: BTO`.
- `data/raw/ontology_subclass_edges.tsv` has one direct broader edge for this
  identifier, `BTO:0000176 rdfs:subClassOf BTO:0000415`, and
  `data/raw/ontology_terms.tsv` labels `BTO:0000415` as `epithelioma cell`.
  The generated record keeps exactly that direct parent in `parent_habitats`.
- `data/raw/prego_habitats.tsv` has a direct `BTO:0000176` source row with
  ontology `BTO`, source category `biolink:GrossAnatomicalStructure`,
  `taxon_count=1`, `direct_assertion_count=1`, `max_prego_score=3`, evidence
  channel `annotated_genomes_isolates`, and a `prego_synonyms` pipe containing
  `carcinoma cell` plus basal-cell-epithelioma, epithelial-cancer-cell,
  epithelial-carcinoma-cell, and malignant-epithelioma variants.
- `src/habitatmech/seed.py` self-grounds PREGO ENVO/BTO habitat ids to the
  same ontology CURIE while preserving each PREGO source under a minted
  curation key. For this source, that key is
  `habitatmech:PREGO.01336cc428`, computed from `PREGO:BTO:0000176`.
- The `BTO` prefix falls through the seeder's `PREFIX_CATEGORY` map to
  `HOST_ASSOCIATED`, matching the generated `habitat_category`.

## Evidence

- The BTO ontology row supports the generated `carcinoma cell` identifier,
  label, definition, and BTO provenance.
- The PREGO habitat row supports the single source attestation, its one-taxon
  assertion count, PREGO score `3.0`, evidence channel
  `annotated_genomes_isolates`, and the nine generated PREGO synonyms:
  `basal cell epithelioma cell`, `basal cell epithelioma cells`,
  `carcinoma cells`, `epithelial cancer cell`, `epithelial cancer cells`,
  `epithelial carcinoma cell`, `epithelial carcinoma cells`,
  `malignant epithelioma cell`, and `malignant epithelioma cells`.
- `data/raw/prego_habitat_taxa.tsv` has exactly one row for `BTO:0000176`,
  carrying rank `1`, taxon `NCBITaxon:1150864`, label
  `Micromonospora lupini str. Lupac 08`, PREGO score `3`, direct flag `TRUE`,
  channel `annotated_genomes_isolates`, and no corroborating source. The
  generated `characteristic_taxa` entry preserves the taxon id, label, PREGO
  score, rank, and `candidate_pool: 1`; the channel is preserved on the PREGO
  `source_attestations` row.
- The rendered page at `pages/habitats/carcinoma-cell-bto-0000176.html`
  mirrors the generated record: one PREGO source row, one `epithelioma cell`
  broader habitat, the one PREGO taxon, the nine non-canonical PREGO synonyms,
  and `SEEDED` status.
- The target carries no xrefs, environmental parameters,
  curator-authored evidence, datasets, discussions, or causal graph.
  Ignored/hidden exact searches over maintained curation, history, reports,
  research, raw and generated habitat paths, rendered pages, `.git/refs`, and
  `.git/packed-refs` found no maintained row for
  `habitatmech:PREGO.01336cc428` and no prior dedicated YAML review for the
  `BTO:0000176` `carcinoma_cell` target. A gitignore-independent `find` found
  no `curation/causal_graphs/*carcinoma*` overlay and no dedicated
  `reports/yaml_record_review/*carcinoma*` report; the one
  `*carcinoma*` report it did find targets the separate Bowen's disease record.

## Completeness

- The record is complete for its current single PREGO source: it retains the
  source id, ontology-derived `source_label`, untruncated PREGO taxon count,
  PREGO score, evidence channel, non-canonical PREGO synonyms, and the sole
  ranked PREGO taxon row.
- The parent hierarchy is complete for the vendored BTO slice: the generated
  record keeps the one direct superclass, `BTO:0000415`, and does not flatten
  any narrower carcinoma-cell children into this broader `BTO:0000176` record.
- The aggregate TSV report row for `BTO:0000176` confirms one source, one
  upstream assertion, one definition, one parent habitat, no environmental
  parameters, one characteristic taxon, and no causal graphs.
- `just worklist --status all` does not list `BTO:0000176` as a worklist
  record.

## Findings

- Major: no item-level PREGO `REVIEW` decision exists yet for source concept
  `habitatmech:PREGO.01336cc428`. The generated `BTO:0000176` record is an
  exact PREGO self-grounding, but no maintained decision row signs off on that
  source concept and the record remains `SEEDED`.

## Recommended Edits

1. Add an item-level PREGO `REVIEW` decision in `curation/decisions.tsv` for
   source concept `habitatmech:PREGO.01336cc428`, with notes explaining that
   PREGO directly asserts `BTO:0000176` and that the BTO class exactly denotes
   a carcinoma cell.
2. Rerun `just seed`, canary `BTO:0000176`, and rerun the corpus validators,
   worklist export, and report export to confirm the generated record becomes
   `REVIEWED`.
3. Do not edit `data/habitats/host_associated/carcinoma_cell.yaml` by hand; it
   must stay generated from PREGO, the vendored BTO slice, and any future
   maintained decision row.

## Follow-up Checks

- Confirm the regenerated `BTO:0000176` record still has exactly one PREGO
  source attestation, one retained characteristic-taxon row, the `BTO:0000415`
  parent, and no causal graphs.
- Confirm the PREGO `carcinoma cell` row still carries one uncapped upstream
  taxon assertion and that the raw PREGO taxon row remains represented.

## Additional Notes

- iModulonDB structured source checks were not applicable: the record names a
  PREGO/BTO anatomical cell type and no genes, locus tags, regulators,
  pathways, stress-response terms, or transcriptomic datasets.
