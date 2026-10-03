# YAML Record Review: peripheral blood

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/peripheral_blood.yaml`
- Started UTC: 2026-10-03T01:33:33Z
- Finished UTC: 2026-10-03T01:36:17Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `BTO:0000553` |
| Label | peripheral blood |
| Definition source | `BTO` |
| Habitat category | `HOST_ASSOCIATED` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Parent habitats | None |
| Source concepts | PREGO `BTO:0000553`; source curation key `habitatmech:PREGO.4d6347cdeb` |
| Generated path | `data/habitats/host_associated/peripheral_blood.yaml` |
| Closest nearby record | `BTO:0001025` (`peripheral blood mononuclear cell`) is separate and already reviewed |

The generated record is a direct PREGO self-grounding to BTO's current
`peripheral blood` class. It preserves the BTO definition, one non-canonical
PREGO synonym, one PREGO source attestation, both retained PREGO taxon rows, no
ontology parents, no xrefs, no environmental parameters, no curator-authored
evidence, no causal graph, and no maintained item-level decision row for its
PREGO source key.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/peripheral_blood.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/host_associated/peripheral_blood.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus` | Passed; 3,206 expected records, 3,206 found, 0 missing, 0 extra, 0 differing. |
| `just validate-causal-all` | Passed; 32 curation files and 32 graphs validated. |
| `just validate-history` | Passed; 77 history records validated. |
| `just term-requests-check` | Passed; the generated ENVO term-request table is current with 109 terms. |
| `just redirects-check` | Passed; `RETIRED.tsv` is current with 231 redirects. |
| `just render-check` | Passed; rendered 3,206 habitat pages, 231 redirect stubs, 8 categories, and 123 term requests to a temporary tree, and `pages/` is in step with the corpus. |
| `just worklist --status all --out /tmp/habitatmech-bto-peripheral-blood-worklist.tsv` | Passed; wrote 953 all-status ungrounded rows, none for `BTO:0000553` or `habitatmech:PREGO.4d6347cdeb`. |
| `just report` | Passed; printed the current 3,206-record corpus report. |
| `just report --out /tmp/habitatmech-bto-peripheral-blood-report.tsv` | Passed; the row for `BTO:0000553` reports `HOST_ASSOCIATED`, `EXACT`, `SEEDED`, one PREGO source, 2 upstream assertions, a definition, no parents, no parameters, 2 retained taxa, and no causal graphs. |
| `git diff --check` | Passed before this report was written. |
| `just validate-products` | Not run locally; this report does not change any grounding, and the pull request's `label-correspondence` workflow is the blocking OAK-based id-label gate. |

## Identity and Grounding

- `data/habitats/PATHS.tsv` pins `BTO:0000553` to `peripheral_blood`,
  matching `data/habitats/host_associated/peripheral_blood.yaml`.
- `data/raw/ontology_terms.tsv` contains `BTO:0000553` with label
  `peripheral blood` and a BTO definition for blood circulating throughout the
  body. The row has an empty `deprecated` column, `directly_referenced=TRUE`,
  and `label_only=FALSE`.
- `data/raw/prego_habitats.tsv` has one direct `BTO:0000553` source row with
  ontology `BTO`, source category `biolink:GrossAnatomicalStructure`,
  `taxon_count=2`, `direct_assertion_count=2`, `max_prego_score=3`, evidence
  channel `annotated_genomes_isolates`, and `prego_synonyms` containing
  canonical `peripheral blood` plus `peripheral bloods`.
- `src/habitatmech/seed.py` self-grounds PREGO ENVO/BTO habitat ids to the
  same ontology CURIE while preserving each PREGO source under a minted
  curation key. For this source, that key is
  `habitatmech:PREGO.4d6347cdeb`, computed from `PREGO:BTO:0000553`.
- The `BTO` prefix falls through the seeder's `PREFIX_CATEGORY` map to
  `HOST_ASSOCIATED`, matching the generated `habitat_category`.
- Exact ignored/hidden-inclusive searches separate this record from the nearby
  `peripheral blood mononuclear cell` record. `BTO:0001025` has its own
  generated YAML and rendered page, and the one matching item-level decision in
  `curation/decisions.tsv` belongs to GOLD source concept
  `habitatmech:GOLD.a3a9e33eec`, not to `BTO:0000553` or
  `habitatmech:PREGO.4d6347cdeb`.

## Evidence

- The BTO peripheral-blood ontology row supports the generated identifier,
  label, definition, current non-deprecated vendored state, and BTO
  provenance.
- The PREGO habitat row supports the single source attestation, its two-taxon
  assertion count, PREGO score `3.0`, evidence channel
  `annotated_genomes_isolates`, and the generated non-canonical PREGO synonym
  `peripheral bloods`.
- `data/raw/prego_habitat_taxa.tsv` has exactly two retained rows for
  `BTO:0000553`, both with PREGO score `3`, direct flag `TRUE`, channel
  `annotated_genomes_isolates`, and no corroborating source. The generated
  `characteristic_taxa` array preserves those taxon ids, labels, ranks 1 and
  2, scores, and `candidate_pool: 2`.
- `curation/samples/exact-20260814.tsv` independently sampled `BTO:0000553`
  in the `EXACT` slice and recorded an `ok` verdict for the
  `peripheral blood` / `peripheral blood` source-label match. That sample
  supports the current identity read but does not count as an item-level
  source-concept decision for mapping status.
- The rendered page at
  `pages/habitats/peripheral-blood-bto-0000553.html` mirrors the generated
  record: one PREGO source row, both PREGO taxon rows, the one non-canonical
  PREGO synonym, and `SEEDED` status.
- The target carries no parent habitats, xrefs, environmental parameters,
  curator-authored evidence, datasets, discussions, or causal graph. Exact
  gitignore-independent searches over maintained curation, history, and report
  surfaces, raw PREGO and ontology inventories, generated habitat paths, and
  rendered habitat pages found no maintained row for
  `habitatmech:PREGO.4d6347cdeb` and no prior dedicated YAML review for the
  `BTO:0000553` `peripheral blood` target before this report was written. The
  searches included ignored and hidden files.

## Completeness

- The record is complete for the current committed PREGO top-taxon slice: it
  retains the source id, ontology-derived `source_label`, full PREGO candidate
  pool, PREGO score, evidence channel, non-canonical PREGO synonym, and both
  ranked PREGO taxon rows vendored for `BTO:0000553`.
- The generated hierarchy is complete for the vendored BTO slice: no maintained
  decision row supplies a broader or related term, and the aggregate report row
  confirms that the generated record has no parent habitats.
- The aggregate TSV report row for `BTO:0000553` confirms one source, 2
  upstream assertions, one definition, no parent habitats, no environmental
  parameters, 2 characteristic-taxon rows, and no causal graphs.
- `just worklist --status all` does not list `BTO:0000553` as a worklist
  record.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | No item-level PREGO `REVIEW` decision exists yet for source concept `habitatmech:PREGO.4d6347cdeb`. | Exact ignored/hidden-inclusive searches for the source key found no maintained decision or history row, and the generated BTO record remains `mapping_status: SEEDED`. The `EXACT` sample row says this target was sampled and found `ok`, but samples are measurement artifacts, not per-source maintained decisions. | `curation/decisions.tsv` |

## Recommended Edits

1. Add an item-level PREGO `REVIEW` decision in `curation/decisions.tsv` for
   source concept `habitatmech:PREGO.4d6347cdeb`, with notes explaining that
   PREGO directly asserts the non-deprecated `BTO:0000553` peripheral-blood
   class.
2. Add an append-only history record describing the maintained decision change.
3. Rerun `just seed`, canary `BTO:0000553`, and rerun the corpus validators,
   worklist export, and report export to confirm the generated record becomes
   `REVIEWED`.
4. Do not edit `data/habitats/host_associated/peripheral_blood.yaml` by hand;
   it must stay generated from PREGO, the vendored BTO slice, and any future
   maintained decision row.

## Follow-up Checks

- Confirm the regenerated `BTO:0000553` record still has one PREGO source
  attestation, the one non-canonical PREGO synonym, 2 retained
  characteristic-taxon rows with `candidate_pool: 2`, no ontology parent, and
  no causal graph.
- Confirm the PREGO `peripheral blood` row still carries 2 unique upstream
  taxa, 2 direct assertions, and that every committed PREGO top taxon is still
  represented.

## Additional Notes

- iModulonDB structured source checks were not applicable: the record names a
  PREGO/BTO gross anatomical structure and no genes, locus tags, regulators,
  pathways, stress-response terms, or transcriptomic datasets.
