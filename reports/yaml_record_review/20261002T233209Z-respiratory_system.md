# YAML Record Review: respiratory system

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/respiratory_system.yaml`
- Started UTC: 2026-10-02T23:32:09Z
- Finished UTC: 2026-10-02T23:32:09Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `BTO:0000203` |
| Label | respiratory system |
| Definition source | `BTO` |
| Habitat category | `HOST_ASSOCIATED` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Parent habitats | none |
| Source concepts | PREGO `BTO:0000203`; source curation key `habitatmech:PREGO.3a1dd1bd18` |
| Generated path | `data/habitats/host_associated/respiratory_system.yaml` |
| Same-label vendored term | `UBERON:0001004` (`respiratory system`) |

The record is generated from one direct PREGO source row plus the vendored BTO
slice. It preserves the BTO respiratory-system definition, eight non-canonical
PREGO synonyms, one direct PREGO source attestation, the top 25 retained PREGO
taxon rows out of a 100-taxon candidate pool, no direct parent habitat, no
environmental parameters, no xrefs, no curator-authored evidence block, no
causal graph, and no maintained item-level decision row for its PREGO source
key.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/respiratory_system.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/host_associated/respiratory_system.yaml --out /tmp/habitatmech-bto-respiratory-system-instance-validation.tsv --quiet` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus` | Passed; 3,206 expected records, 3,206 found, 0 missing, 0 extra, 0 differing. |
| `just validate-causal-all` | Passed; 32 curation files and 32 graphs validated. |
| `just term-requests-check` | Passed; the generated ENVO term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records validated. |
| `just worklist --status all --out /tmp/habitatmech-bto-respiratory-system-worklist.tsv` | Passed; wrote 953 all-status ungrounded rows, none for `BTO:0000203`. |
| `just report --out /tmp/habitatmech-bto-respiratory-system-report.tsv` | Passed; row for `BTO:0000203` reports `HOST_ASSOCIATED`, `EXACT`, `SEEDED`, one PREGO source, 100 assertions, a definition, no parents, no parameters, 25 retained taxa, and no causal graphs. |
| `git diff --check` | Passed before this report was written. |
| `just validate-products` | Not run locally; this report does not change any grounding, and the pull request's `label-correspondence` workflow is the blocking OAK-based id-label gate. |

## Identity and Grounding

- `data/habitats/PATHS.tsv` pins `BTO:0000203` to
  `respiratory_system`, matching
  `data/habitats/host_associated/respiratory_system.yaml`.
- `data/raw/ontology_terms.tsv` contains `BTO:0000203` with label
  `respiratory system` and a BTO definition for an organ system subserving
  respiration. The generated record preserves this identifier, label,
  definition, and `definition_source: BTO`; the row has an empty
  `deprecated` column, `directly_referenced=TRUE`, and `label_only=FALSE`.
- The same vendored ontology slice also contains `UBERON:0001004` with label
  `respiratory system`, an empty `deprecated` column, and
  `label_only=FALSE`. That same-label UBERON row is already used as a broader
  parent for several generated GOLD respiratory-system records, but the PREGO
  source reviewed here directly asserted `BTO:0000203` and therefore
  self-grounded to the BTO CURIE.
- `data/raw/ontology_subclass_edges.tsv` has no direct broader edge with
  `BTO:0000203` as subject, so the generated record has no
  `parent_habitats`. The BTO slice does use `BTO:0000203` as a parent for
  four more specific classes, including gill, lung, and trachea records.
- `data/raw/prego_habitats.tsv` has a direct `BTO:0000203` source row with
  ontology `BTO`, source category `biolink:GrossAnatomicalStructure`,
  `taxon_count=100`, `direct_assertion_count=101`, `max_prego_score=3`,
  evidence channel `annotated_genomes_isolates`, and a `prego_synonyms` pipe
  containing canonical `respiratory system` plus eight PREGO variants.
- `src/habitatmech/seed.py` self-grounds PREGO ENVO/BTO habitat ids to the
  same ontology CURIE while preserving each PREGO source under a minted
  curation key. For this source, that key is
  `habitatmech:PREGO.3a1dd1bd18`, computed from `PREGO:BTO:0000203`.
- The `BTO` prefix falls through the seeder's `PREFIX_CATEGORY` map to
  `HOST_ASSOCIATED`, matching the generated `habitat_category`.

## Evidence

- The BTO ontology row supports the generated `respiratory system`
  identifier, label, definition, current non-deprecated vendored state, and
  BTO provenance. The same-label `UBERON:0001004` row is available in the
  slice, but it is not the direct PREGO source id behind this record.
- The PREGO habitat row supports the single source attestation, its 100-taxon
  candidate count, PREGO score `3.0`, evidence channel
  `annotated_genomes_isolates`, and the eight generated non-canonical PREGO
  synonyms: `Atmungssystem`, `Atmungssystems`, `apparatus respiratorius`,
  `apparatus respiratorius s`, `respiratory systems`,
  `respiratory tract`, `respiratory tractic`, and `respiratory tracts`.
- `data/raw/prego_habitat_taxa.tsv` has 25 retained rows for
  `BTO:0000203`, with ranks 1 through 25, PREGO score `3`, direct flag
  `TRUE`, channel `annotated_genomes_isolates`, and no corroborating source.
  The generated `characteristic_taxa` entries preserve each retained taxon id,
  label, PREGO score, rank, and `candidate_pool: 100`; the channel is
  preserved on the PREGO `source_attestations` row.
- The rendered page at
  `pages/habitats/respiratory-system-bto-0000203.html` mirrors the generated
  record: one PREGO source row, no broader-habitat section, 25 PREGO taxa, the
  eight non-canonical PREGO synonyms, and `SEEDED` status.
- The target carries no xrefs, environmental parameters,
  curator-authored evidence, datasets, discussions, or causal graph.
  Ignored/hidden exact searches over maintained curation, history, reports,
  research, raw and generated habitat paths, rendered pages, `.git/refs`, and
  `.git/packed-refs` found no maintained row for
  `habitatmech:PREGO.3a1dd1bd18` and no prior dedicated YAML review for the
  `BTO:0000203` `respiratory_system` target before this report was written.
  Gitignore-independent `find` checks found no
  `curation/causal_graphs/*respiratory*` overlay and, excluding the distinct
  GOLD `respiratory_system__431eac8d` report, no dedicated
  `reports/yaml_record_review/*respiratory*` report for this exact BTO record.

## Completeness

- The record is complete for the current committed PREGO top-25 taxon slice:
  it retains the source id, ontology-derived `source_label`, full PREGO
  candidate pool, PREGO score, evidence channel, non-canonical PREGO synonyms,
  and all 25 ranked PREGO taxon rows vendored for `BTO:0000203`.
- The generated parent hierarchy is complete for the vendored BTO slice:
  the slice has no direct superclass row for `BTO:0000203`, and generated
  child records keep respiratory system as their parent instead of being
  flattened into this broader record.
- The aggregate TSV report row for `BTO:0000203` confirms one source,
  100 upstream assertions, one definition, no parent habitats, no
  environmental parameters, 25 characteristic taxa, and no causal graphs.
- `just worklist --status all` does not list `BTO:0000203` as a worklist
  record.

## Findings

- Major: no item-level PREGO `REVIEW` decision exists yet for source concept
  `habitatmech:PREGO.3a1dd1bd18`. The generated `BTO:0000203` record is an
  exact PREGO self-grounding, but no maintained decision row signs off on that
  source concept and the record remains `SEEDED`.

## Recommended Edits

1. Add an item-level PREGO `REVIEW` decision in `curation/decisions.tsv` for
   source concept `habitatmech:PREGO.3a1dd1bd18`, with notes explaining that
   PREGO directly asserts `BTO:0000203`, the committed kg-microbe slice does
   not mark that BTO row deprecated, and the same-label `UBERON:0001004` row
   was considered but not used because it is not PREGO's direct source id.
2. Rerun `just seed`, canary `BTO:0000203`, and rerun the corpus validators,
   worklist export, and report export to confirm the generated record becomes
   `REVIEWED`.
3. Do not edit `data/habitats/host_associated/respiratory_system.yaml` by
   hand; it must stay generated from PREGO, the vendored BTO slice, and any
   future maintained decision row.

## Follow-up Checks

- Confirm the regenerated `BTO:0000203` record still has exactly one PREGO
  source attestation, 25 retained characteristic-taxon rows with
  `candidate_pool: 100`, no parent habitats, and no causal graphs.
- Confirm the PREGO `respiratory system` row still carries 100 unique upstream
  taxa, 101 direct assertions, and that the committed top-25 PREGO taxon rows
  remain represented.

## Additional Notes

- iModulonDB structured source checks were not applicable: the record names a
  PREGO/BTO anatomical organ system and no genes, locus tags, regulators,
  pathways, stress-response terms, or transcriptomic datasets.
