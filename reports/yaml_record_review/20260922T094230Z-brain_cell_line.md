# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/brain_cell_line.yaml`
- Started UTC: 2026-09-22T09:42:30Z
- Finished UTC: 2026-09-22T09:42:30Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `BTO:0000255` |
| Label | `brain cell line` |
| Class | `HabitatRecord` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Maintained owner | Generated from the PREGO inventory plus the vendored ontology slice; generated YAML remains read-only |
| Locked slug | `data/habitats/PATHS.tsv:46` maps `BTO:0000255` to `brain_cell_line` |

This is the seeded PREGO record for the BRENDA Tissue Ontology `brain cell line` class. The record is exactly grounded because PREGO uses `BTO:0000255` directly as its habitat identifier, and the seeder carries that CURIE through instead of minting a HabitatMech source identifier.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/brain_cell_line.yaml` | Pass; `linkml-validate` reported `No issues found` |
| `just validate-strict data/habitats/host_associated/brain_cell_line.yaml` | Pass; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate-causal-all` | Pass; 32 causal-graph curation files with 32 graphs validated |
| `just term-requests-check` | Pass; term-request table is current with 109 terms |
| `just validate-history` | Pass; 77 history records are valid against `src/habitatmech/schema/history.yaml` |
| `just verify-corpus --max-diffs 1` | Pass; expected 3206 records, found 3206, with 0 missing, 0 extra, 0 differing |
| `git diff --check` | Pass; no whitespace or patch errors after this report was staged |

## Identity and Grounding

The exact identity, label, path lock, PREGO attestation, and emitted taxon are supported by the vendored ontology and PREGO source tables:

- `data/habitats/PATHS.tsv:46` pins `BTO:0000255` to slug `brain_cell_line`, matching the reviewed YAML path.
- `data/raw/ontology_terms.tsv:257` gives `BTO:0000255` the ontology label `brain cell line`, marks it directly referenced, and marks `label_only: FALSE`.
- `data/raw/prego_habitats.tsv:541` records PREGO source id `BTO:0000255`, vocabulary `BTO`, Biolink type `GrossAnatomicalStructure`, one taxon assertion, one direct assertion, maximum PREGO score `3`, evidence channel `annotated_genomes_isolates`, and synonyms `brain cell line|brain cell lines|brain cell linous`.
- `data/raw/prego_habitat_taxa.tsv:375` is the only exact PREGO taxon row for `BTO:0000255`; it emits rank `1`, `NCBITaxon:1392869`, label `Escherichia coli K1`, PREGO score `3`, `direct_flag: TRUE`, evidence channel `annotated_genomes_isolates`, and no corroborating source.
- `data/raw/ontology_subclass_edges.tsv:445`, `:1043`, `:1747`, `:2292`, and `:2961` name `BTO:0000255` as an object, not a subject, so the vendored ontology contributes narrower child classes but no broader parent for this record.

`grounding_status: EXACT` is correct because the PREGO row is self-grounded to the same BTO class. `mapping_status: SEEDED` is also expected because ignored/hidden-inclusive exact searches found no item-level decision row for `BTO:0000255`.

## Evidence

Every generated scientific claim in this record is source-derived:

| Claim | Nearest source | Review |
|---|---|---|
| Ontology identity and label | `data/raw/ontology_terms.tsv:257` | Supported exactly |
| Locked filename | `data/habitats/PATHS.tsv:46` | Supported exactly |
| PREGO `source_id`, `source_label`, 1-taxon assertion count, score `3.0`, and evidence channel | `data/raw/prego_habitats.tsv:541` | Supported exactly |
| Related synonyms `brain cell lines` and `brain cell linous` | `data/raw/prego_habitats.tsv:541` | Supported; the canonical `brain cell line` synonym collapses against the record label |
| The sole `characteristic_taxa` row for `NCBITaxon:1392869` | `data/raw/prego_habitat_taxa.tsv:375` | Supported exactly |

The record has no definition, `parent_habitats`, xrefs, environmental parameters, record-level evidence, causal graphs, discussion links, or datasets. Those absences are consistent with exact ignored/hidden-inclusive searches that found no maintained decision, term request, causal-graph overlay, history entry, research artifact, or dataset row for `BTO:0000255`. The vendored subclass edges for `BTO:0000255` all point from child classes to `BTO:0000255`; they do not name any broader class to emit as a parent.

## Completeness

No consequential slot is underfilled for the maintained inputs that feed this record:

- The sole `source_attestations` entry captures the complete PREGO source id, source label, assertion count, `TAXON` unit, maximum score, and evidence-channel set.
- The synonym list carries the two non-canonical PREGO alternate forms after de-duplicating the raw canonical label `brain cell line`.
- The only PREGO taxon row for `BTO:0000255` is emitted as the sole `characteristic_taxa` entry and retains its taxon id, label, score, rank, source, and one-taxon candidate pool.
- No `parent_habitats` entry is required because exact ignored/hidden-inclusive searches found only narrower ontology children of `BTO:0000255`, not a vendored broader parent row.

Ignored/hidden-inclusive exact searches covered `curation`, `history`, `research`, `reports`, `data/raw`, `data/habitats/PATHS.tsv`, and the generated target, excluding generated `build`, `data/text_map`, and `pages` trees. They found the expected PREGO habitat row, PREGO taxon row, ontology row, child subclass edges, path lock, and generated YAML, and no maintained decision, term request, history record, causal-graph overlay, target-specific research report, dataset row, or prior exact YAML review report for `BTO:0000255`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the same focused validation set if future curation changes the PREGO rollup, BTO vendored terms, path lock, or characteristic-taxon emission:

- `just validate data/habitats/host_associated/brain_cell_line.yaml`
- `just validate-strict data/habitats/host_associated/brain_cell_line.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `git diff --check`

If future review redirects `BTO:0000255` away from this direct PREGO self-grounding, add an explicit `curation/decisions.tsv` row first, regenerate with `just seed`, and verify that the PREGO attestation and rank-1 characteristic taxon remain attached to the surviving record.

## Additional Notes

- `find reports/yaml_record_review -name '*brain_cell_line*' -print` found no pre-existing exact review report for this record before this file was written.
- Exact ignored/hidden-inclusive content searches for `BTO:0000255`, `brain_cell_line`, `brain cell line`, and `NCBITaxon:1392869` found the path lock, generated YAML, raw PREGO rows, and vendored ontology rows cited above, and no target-specific maintained curation or research artifacts.
