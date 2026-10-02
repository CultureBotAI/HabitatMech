# YAML Record Review: cardiovascular system

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/cardiovascular_system.yaml`
- Started UTC: 2026-10-02T14:45:12Z
- Finished UTC: 2026-10-02T14:47:36Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `BTO:0000088` |
| Label | cardiovascular system |
| Definition source | `BTO` |
| Habitat category | `HOST_ASSOCIATED` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Source concepts | PREGO `BTO:0000088`; source curation key `habitatmech:PREGO.5a4c2815eb` |
| Generated path | `data/habitats/host_associated/cardiovascular_system.yaml` |

The record is generated from one PREGO source row plus the vendored BTO slice.
It has two direct PREGO taxon assertions, no environmental parameters, no
curator-authored evidence block, no causal graph, no generated parent
habitats, and no maintained item-level decision row yet.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/cardiovascular_system.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/host_associated/cardiovascular_system.yaml --out /tmp/habitatmech-cardiovascular-system-instance-validation.tsv --quiet` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus` | Passed; 3,206 expected records, 3,206 found, 0 missing, 0 extra, 0 differing. |
| `just validate-causal-all` | Passed; 32 curation files and 32 graphs validated. |
| `just term-requests-check` | Passed; the generated ENVO term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records validated. |
| `just worklist --status all --out /tmp/habitatmech-cardiovascular-system-worklist.tsv` | Passed; wrote 953 all-status ungrounded rows. |
| `just report --out /tmp/habitatmech-cardiovascular-system-report.tsv` | Passed; row for `BTO:0000088` reports `HOST_ASSOCIATED`, `EXACT`, `SEEDED`, one PREGO source, two assertions, a definition, no parents, no parameters, two taxa, and no causal graphs. |
| `git diff --check` | Passed. |
| `just validate-products` | Not run locally; this report does not change any grounding, and the pull request's `label-correspondence` workflow is the blocking OAK-based id-label gate. |

## Identity and Grounding

- `data/raw/ontology_terms.tsv` contains `BTO:0000088` with label
  `cardiovascular system` and definition
  `The system of heart and blood vessels.` The generated record preserves this
  identifier, label, definition, and `definition_source: BTO`.
- `data/raw/prego_habitats.tsv` has a direct `BTO:0000088` source row with
  ontology `BTO`, category `biolink:GrossAnatomicalStructure`, `taxon_count=2`,
  `direct_assertion_count=2`, `max_prego_score=3`, evidence channel
  `annotated_genomes_isolates`, and PREGO synonyms for `CV system`,
  `cardiovascular system`, `circulatory system`, and the German/Latin
  `Herz und Gefaesssystem`.
- `src/habitatmech/seed.py` self-grounds PREGO ENVO/BTO habitat ids to the same
  ontology CURIE while preserving each PREGO source under a minted curation
  key. For this source, that key is `habitatmech:PREGO.5a4c2815eb`, computed
  from `PREGO:BTO:0000088`.
- The source concept denotes an animal anatomical system sampled as a host
  site, so `HOST_ASSOCIATED` is the right broad category. It is anatomy rather
  than a disease, quality, process, procedure, sample artifact, or whole host
  taxon.
- `data/raw/ontology_subclass_edges.tsv` has no edge for `BTO:0000088`, so the
  generated record is parentless under the current BTO self-grounding.
- `data/raw/ontology_terms.tsv` also contains `UBERON:0001009` `circulatory
  system` with a generic organ-system definition, and
  `data/raw/ontology_subclass_edges.tsv` places it under `UBERON:0000467`
  `anatomical system`. The PREGO source's own `circulatory system` synonym
  matches this UBERON class exactly.

## Evidence

- The BTO ontology row supports the generated record identity and definition.
- The PREGO habitat row supports the single source attestation, its assertion
  count of two distinct taxa, PREGO score `3.0`, evidence channel
  `annotated_genomes_isolates`, and the PREGO synonyms that are not identical
  to the canonical label.
- `data/raw/prego_habitat_taxa.tsv` supports both seeded taxon associations:
  rank 1 `NCBITaxon:1276220` / `Spiroplasma taiwanense CT-1` and rank 2
  `NCBITaxon:1276221` / `Spiroplasma diminutum CUAS-1`. Both have PREGO score
  `3`, direct flag `TRUE`, channel `annotated_genomes_isolates`, no
  corroborating source, and `candidate_pool: 2` from the corresponding PREGO
  habitat `taxon_count`.
- The target carries no xrefs, environmental parameters, curator-authored
  evidence, datasets, discussions, or causal graph. Ignored/hidden exact
  searches over `curation`, `history`, and `curation/causal_graphs` found no
  maintained input that should currently populate those fields.

## Completeness

- The record is complete for its current single PREGO source: it retains the
  source id, exact source label, one untruncated PREGO taxon count, PREGO
  score, evidence channel, every non-canonical PREGO synonym, and the two top
  taxon rows.
- The aggregate TSV report row for `BTO:0000088` confirms one source, two
  upstream assertions, one definition, no parent habitats, no environmental
  parameters, two characteristic taxa, and no causal graphs.
- `just worklist --status all` does not list `BTO:0000088`; that is expected
  because the PREGO source is already self-grounded to an exact ontology class,
  not minted as an ungrounded backlog row.
- Ignored/hidden exact searches over `curation`, `history`,
  `reports/yaml_record_review`, `data/raw`, `data/habitats`, `.git/refs`, and
  `.git/packed-refs` found the expected raw PREGO rows, BTO ontology row, the
  path lock, the generated target, and no maintained decision row, term
  request, history row, causal overlay, or prior exact YAML review report for
  `BTO:0000088`, `habitatmech:PREGO.5a4c2815eb`, or
  `cardiovascular_system.yaml`.
- The current exact BTO grounding is faithful to the generated PREGO row, but
  it is not complete against the current kg-microbe modeling target because a
  generic UBERON circulatory-system class is already vendored and should own
  the PREGO `BTO:0000088` source concept.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | PREGO `BTO:0000088` is self-grounded to a BTO cardiovascular-system term even though the vendored `UBERON:0001009` class exactly names the generic circulatory system denoted by the PREGO source. | `data/raw/ontology_terms.tsv` contains both the generated `BTO:0000088` term and `UBERON:0001009`; the PREGO synonym list includes `circulatory system`, which exactly matches the UBERON label, and the UBERON term has a subclass edge to `UBERON:0000467` `anatomical system` while the BTO term contributes no broader parent edge. GOLD host-specific `Circulatory system` records already keep `UBERON:0001009` as their generic anatomy parent. | Add an item-level `GROUND` row for `habitatmech:PREGO.5a4c2815eb` in `curation/decisions.tsv`, redirecting the PREGO source to `UBERON:0001009` with expected label `circulatory system`, then regenerate instead of editing `data/habitats/host_associated/cardiovascular_system.yaml`. |

## Recommended Edits

1. Add an item-level PREGO `GROUND` decision in `curation/decisions.tsv` for
   source concept `habitatmech:PREGO.5a4c2815eb`.
2. Redirect PREGO's `BTO:0000088` source to `UBERON:0001009` with expected
   label `circulatory system` and `grounding_status` `EXACT`.
3. Rerun `just seed`, canary `UBERON:0001009`, and run
   `just seed-apply --force --prune` so the generated YAML is rewritten from
   maintained inputs and the stale `BTO:0000088` output is removed.
4. Rerun the target-file validators, `just verify-corpus`, history and
   term-request checks, and the report/worklist exports.

## Follow-up Checks

- Confirm the regenerated generic circulatory-system record has identifier
  `UBERON:0001009`, label `circulatory system`, a PREGO source attestation
  still pointing at `BTO:0000088`, and a `GROUND`/`ITEM` curation event for
  `habitatmech:PREGO.5a4c2815eb`.
- Confirm the regenerated record inherits `UBERON:0000467` from
  `data/raw/ontology_subclass_edges.tsv` rather than staying parentless under
  the BTO source id.
- Confirm the two PREGO taxon rows stay attached to the PREGO source after the
  exact UBERON redirect.
- Run `just verify-corpus` after regeneration; it is the check that proves
  `data/habitats/` matches maintained curation and raw inputs.

## Additional Notes

- Existing host-specific GOLD `Circulatory system` records are stricter than
  generic `UBERON:0001009`; keeping that UBERON term as their parent is
  compatible with adopting it as the exact target for a generic PREGO source.
- iModulonDB structured source checks were not applicable: the record names a
  PREGO/BTO anatomical habitat and no genes, locus tags, regulators, pathways,
  stress-response terms, or transcriptomic datasets.
