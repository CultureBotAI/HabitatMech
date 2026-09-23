# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/acute_lymphoblastic_leukemia_cell.yaml`
- Started UTC: 2026-09-23T05:12:52Z
- Finished UTC: 2026-09-23T05:16:38Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `BTO:0000731` |
| Label | `acute lymphoblastic leukemia cell` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Maintained owner | Generated from the PREGO inventory plus the vendored ontology slice; generated YAML remains read-only |
| Locked slug | `data/habitats/PATHS.tsv:135` maps `BTO:0000731` to `acute_lymphoblastic_leukemia_cell` |

This is the generated BTO-grounded PREGO record for `acute lymphoblastic leukemia cell`. PREGO uses the BTO CURIE directly, so the seeder keeps `BTO:0000731` as the record identifier with `grounding_status: EXACT`.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/acute_lymphoblastic_leukemia_cell.yaml` | Pass; `linkml-validate` reported `No issues found` |
| `just validate-strict data/habitats/host_associated/acute_lymphoblastic_leukemia_cell.yaml` | Pass; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate-causal-all` | Pass; 32 causal-graph curation files with 32 graphs validated |
| `just term-requests-check` | Pass; term-request table is current with 109 terms |
| `just validate-history` | Pass; 77 history records are valid against `src/habitatmech/schema/history.yaml` |
| `just verify-corpus --max-diffs 1` | Pass; expected 3206 records, found 3206, with 0 missing, 0 extra, 0 differing |
| `just worklist --limit 2000` | Pass; 0 ungrounded records are still undecided and 1810 decisions are on file |
| `just report` | Pass; the report completed and kept the corpus at 3206 records with 0 risky groundings, 0 stale class sweeps, 0 swept path/leaf contradictions, and 0 records claiming a non-habitat is a habitat |
| `git diff --check` | Pass; no whitespace errors |

## Identity and Grounding

The exact identity, host-associated category, BTO label, BTO definition, ontology parent, path lock, PREGO attestation, and emitted taxon are supported by committed inputs:

- `data/habitats/PATHS.tsv:135` pins `BTO:0000731` to slug `acute_lymphoblastic_leukemia_cell`, matching the reviewed YAML path.
- `data/raw/ontology_terms.tsv:732` gives `BTO:0000731` the ontology label `acute lymphoblastic leukemia cell`, the lymphocytic leukemia cell definition, `is_directly_referenced: TRUE`, and `label_only: FALSE`.
- `data/raw/ontology_subclass_edges.tsv:473` records `BTO:0000731 rdfs:subClassOf BTO:0003676`, which supports the generated `parent_habitats` entry.
- `data/raw/ontology_terms.tsv:3676` labels parent `BTO:0003676` as `lymphoblastic leukemia cell`.
- `data/raw/prego_habitats.tsv:559` records PREGO source id `BTO:0000731`, vocabulary `BTO`, Biolink type `GrossAnatomicalStructure`, one taxon assertion, one direct assertion, maximum PREGO score `3`, evidence channel `annotated_genomes_isolates`, and synonyms `ALL cell|ALL cells|acute lymphoblastic leukemia cell|acute lymphoblastic leukemia cells|acute lymphocytic leukemia cell|acute lymphocytic leukemia cells`.
- `data/raw/prego_habitat_taxa.tsv:1173` is the only exact PREGO taxon row for `BTO:0000731`; it emits rank `1`, `NCBITaxon:243365`, label `Chromobacterium violaceum ATCC 12472`, PREGO score `3`, `direct_flag: TRUE`, evidence channel `annotated_genomes_isolates`, and no corroborating source.

The deterministic PREGO source-concept key is `habitatmech:PREGO.a0429ba065`, computed from `sha1("PREGO:BTO:0000731")[:10]`. An ignored/hidden-inclusive exact search found no row for that key in `curation/decisions.tsv`, so `mapping_status: SEEDED` is expected. `habitat_category: HOST_ASSOCIATED` is also expected because BTO identifiers fall through `PREFIX_CATEGORY` to host-associated when no curator override is present.

## Evidence

Every generated scientific claim in this record is source-derived:

| Claim | Nearest source | Review |
|---|---|---|
| Record identifier, label, definition, and `definition_source: BTO` | `data/raw/ontology_terms.tsv:732` | Supported exactly |
| BTO parent `BTO:0003676` | `data/raw/ontology_subclass_edges.tsv:473` | Supported exactly |
| Locked filename | `data/habitats/PATHS.tsv:135` | Supported exactly |
| PREGO `source_id`, one-taxon assertion count, score `3.0`, and evidence channel | `data/raw/prego_habitats.tsv:559` | Supported exactly |
| PREGO `source_label` | `data/raw/ontology_terms.tsv:732` | Supported exactly; PREGO rows carry ontology CURIEs, and `ingest_prego()` emits `source_label` from `store.ontology.label(prego_id)` |
| Related synonyms `ALL cell`, `ALL cells`, `acute lymphoblastic leukemia cells`, `acute lymphocytic leukemia cell`, and `acute lymphocytic leukemia cells` | `data/raw/prego_habitats.tsv:559` | Supported exactly; the remaining PREGO lexical variant, `acute lymphoblastic leukemia cell`, is the ontology primary label |
| The sole `characteristic_taxa` row for `NCBITaxon:243365` | `data/raw/prego_habitat_taxa.tsv:1173` | Supported exactly |

The record has no xrefs, environmental parameters, record-level evidence, causal graphs, discussion links, datasets, or quality flags. Those absences match ignored/hidden-inclusive searches that found no maintained decision, term request, causal-graph overlay, history entry, target-specific research artifact, dataset row, or prior exact YAML review report for `BTO:0000731`, `acute_lymphoblastic_leukemia_cell`, `acute lymphoblastic leukemia cell`, `NCBITaxon:243365`, or `habitatmech:PREGO.a0429ba065`.

Unsupported or over-scoped claims: None found.

## Completeness

No consequential slot is underfilled for the maintained inputs that feed this record:

- The sole `source_attestations` entry captures the complete PREGO source id, source label, assertion count, `TAXON` unit, maximum score, and evidence channel.
- All five non-primary raw PREGO lexical variants are emitted as related synonyms, while the sixth raw PREGO lexical variant is the exact BTO primary label.
- The only PREGO taxon row for `BTO:0000731` is emitted as the sole `characteristic_taxa` entry and retains its taxon id, taxon label, PREGO score, rank, source, and one-taxon candidate pool.
- The only broader BTO parent edge from the vendored ontology slice is emitted as `parent_habitats: [BTO:0003676]`.
- No authored definition or term request is expected because the record uses the existing exact BTO `acute lymphoblastic leukemia cell` term.

Ignored/hidden-inclusive exact searches covered `curation`, `history`, `research`, `reports`, `data/raw`, `data/habitats/PATHS.tsv`, and the generated target, excluding generated `build`, `data/text_map`, and `pages` trees where broad searches would otherwise hit generated artifacts. They found the expected PREGO habitat row, PREGO taxon row, ontology term rows, subclass edges, path lock, generated YAML, unrelated PREGO reuse of `NCBITaxon:243365` under other BTO terms, and no target-specific maintained curation or research artifacts.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the same focused validation set if future curation changes the PREGO rollup, BTO vendored terms, path lock, or characteristic-taxon emission:

- `just validate data/habitats/host_associated/acute_lymphoblastic_leukemia_cell.yaml`
- `just validate-strict data/habitats/host_associated/acute_lymphoblastic_leukemia_cell.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000`
- `just report`
- `git diff --check`

If future review redirects `BTO:0000731` away from this direct PREGO self-grounding, add an explicit `curation/decisions.tsv` row for `habitatmech:PREGO.a0429ba065` first, regenerate with `just seed`, and verify that the PREGO attestation and rank-1 characteristic taxon remain attached to the surviving record.

## Additional Notes

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-acute_lymphoblastic_leukemia_cell.md' -print` found no pre-existing exact review report for this record before this file was written, and `find` included ignored files under the searched directory.
- Exact ignored/hidden-inclusive content searches for `BTO:0000731`, `acute_lymphoblastic_leukemia_cell`, `acute lymphoblastic leukemia cell`, `ALL cell`, `acute lymphocytic leukemia cell`, `NCBITaxon:243365`, `BTO:0003676`, and `habitatmech:PREGO.a0429ba065` found the path lock, generated YAML, raw PREGO rows, and vendored ontology rows cited above, plus unrelated hits noted under Completeness, and no target-specific maintained curation or research artifacts.
