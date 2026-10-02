# YAML Record Review: reproductive system

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/reproductive_system.yaml`
- Started UTC: 2026-10-02T13:13:00Z
- Finished UTC: 2026-10-02T13:16:33Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `BTO:0000081` |
| Label | reproductive system |
| Definition source | `BTO` |
| Habitat category | `HOST_ASSOCIATED` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Source concepts | PREGO `BTO:0000081`; source curation key `habitatmech:PREGO.0ce0a5364f` |
| Generated path | `data/habitats/host_associated/reproductive_system.yaml` |

The record is generated from committed PREGO and ontology inventories. It has no
maintained item-level curation decision, causal overlay, history record, or
exact YAML review report yet.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/reproductive_system.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/host_associated/reproductive_system.yaml --out /tmp/habitatmech-reproductive-system-instance-validation.tsv --quiet` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus` | Passed; 3,206 expected records, 3,206 found, 0 missing, 0 extra, 0 differing. |
| `just validate-causal-all` | Passed; 32 curation files and 32 graphs validated. |
| `just term-requests-check` | Passed; the generated ENVO term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records validated. |
| `just worklist --status all --out /tmp/habitatmech-reproductive-system-worklist.tsv` | Passed; wrote 953 all-status ungrounded rows. |
| `just report --out /tmp/habitatmech-reproductive-system-report.tsv` | Passed; row for `BTO:0000081` reports `HOST_ASSOCIATED`, `EXACT`, `SEEDED`, one PREGO source, four assertions, a definition, no parents, no parameters, four taxa, and no causal graphs. |
| `just validate-products` | Not run locally; this report does not change any grounding, and the pull request's `label-correspondence` workflow is the blocking OAK-based id-label gate. |

## Identity and Grounding

- `data/raw/ontology_terms.tsv` contains `BTO:0000081` with label
  `reproductive system` and the generated human female/male reproductive-system
  definition. The generated record preserves this identifier, label, definition,
  and `definition_source`.
- `data/raw/prego_habitats.tsv` has a direct `BTO:0000081` source row with
  ontology `BTO`, category `biolink:GrossAnatomicalStructure`, `taxon_count=4`,
  `direct_assertion_count=4`, `max_prego_score=3`, evidence channel
  `annotated_genomes_isolates`, and PREGO synonyms for `animal reproductive
  system`, `genitalia`, `genital system`, `organa genitalia`, `reproductive
  tissue`, and `reproductive tract`.
- `src/habitatmech/seed.py` self-grounds PREGO ENVO/BTO habitat ids to the same
  ontology CURIE, preserving the source under the minted curation key
  `habitatmech:PREGO.0ce0a5364f`. The current `EXACT` grounding is therefore
  faithful to the PREGO row and the vendored BTO term.
- The source concept denotes an animal anatomical system sampled as a host site,
  so `HOST_ASSOCIATED` is the right broad category.
- `data/raw/ontology_terms.tsv` also contains the exact UBERON anatomy class
  `UBERON:0000990` `reproductive system` with matching animal-reproductive
  synonyms, and `data/raw/ontology_subclass_edges.tsv` places it under
  `UBERON:0000467` `anatomical system`. The Bryozoa-specific GOLD
  `Reproductive system` review already treats `UBERON:0000990` as the generic
  anatomy class broader than a host-branch-specific GOLD path. PREGO's source
  is not host-branch-specific, so it needs an item-level `GROUND` decision to
  redirect the BTO source to the generic UBERON term instead of keeping the
  default BTO self-grounding.

## Evidence

- The BTO ontology row supports the generated record identity and definition.
- The PREGO habitat row supports the single PREGO source attestation, its
  assertion count of four distinct taxa, PREGO score `3.0`, evidence channel
  `annotated_genomes_isolates`, and PREGO synonyms.
- `data/raw/prego_habitat_taxa.tsv` supports all four seeded taxon
  associations: `NCBITaxon:1306407` / `Treponema phagedenis 4A`,
  `NCBITaxon:1382230` / `Asaia platycodi SF2.1`, `NCBITaxon:187101` /
  `Sneathia vaginalis`, and `NCBITaxon:2098` / `Metamycoplasma hominis`.
  Each has PREGO score `3`, direct flag `TRUE`, channel
  `annotated_genomes_isolates`, and `candidate_pool: 4` from the corresponding
  PREGO habitat `taxon_count`.
- The target carries no parent habitats, environmental parameters,
  curator-authored evidence, datasets, discussions, or causal graph. The absent
  parent list is consistent with an ignored/hidden exact search of `data/raw`,
  which found `BTO:0000081` only as the object of child edges for
  `BTO:0000082`, `BTO:0000083`, `BTO:0005454`, and `BTO:0006162`, not as the
  subject of a broader edge.

## Completeness

- The record is complete for its current single PREGO source: it retains the
  source id, exact source label, untruncated taxon count, PREGO score, aggregate
  evidence channel, PREGO synonyms, and all four top taxon rows.
- The aggregate TSV report row for `BTO:0000081` confirms one source, four
  upstream assertions, one definition, no parent habitats, no environmental
  parameters, four characteristic taxa, and no causal graphs.
- An ignored/hidden exact search over `curation`, `history`,
  `data/habitats/RETIRED.tsv`, `data/habitats/PATHS.tsv`,
  `reports/yaml_record_review`, `.git/refs`, and `.git/packed-refs` found no
  maintained item-level curation decision, term request, history row,
  retirement row, exact prior YAML review report, or existing review branch for
  `BTO:0000081`, `habitatmech:PREGO.0ce0a5364f`,
  `reproductive_system.yaml`, or `review-reproductive-system`.
- `reports/yaml_record_review/20260930T014652Z-reproductive_system__e62e83f1.md`
  is a review of a separate Bryozoa-specific GOLD child source. It is useful
  evidence that `UBERON:0000990` is already vendored and used as the generic
  broader anatomy term for reproductive-system leaves, but it is not a review
  of PREGO `BTO:0000081`.
- The all-status worklist mentions `UBERON:0000990` only as a lexical candidate
  for the unrelated GOLD `Genital warts` record; it does not list PREGO
  `BTO:0000081` because that source is currently self-grounded.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | PREGO `BTO:0000081` is self-grounded to a BTO reproductive-system term even though the vendored `UBERON:0000990` class exactly names the generic animal reproductive system denoted by the PREGO source. | `data/raw/ontology_terms.tsv` contains both the generated `BTO:0000081` term and `UBERON:0000990`; the UBERON term has a generic animal-system definition, matching genital-system synonyms, and a subclass edge to `UBERON:0000467` `anatomical system`, while the BTO term contributes no broader parent edge to this record. GOLD host-specific `Reproductive system` paths already keep `UBERON:0000990` as their generic anatomy parent. | Add an item-level `GROUND` row for `habitatmech:PREGO.0ce0a5364f` in `curation/decisions.tsv`, redirecting the PREGO source to `UBERON:0000990` with expected label `reproductive system`, then regenerate instead of editing `data/habitats/host_associated/reproductive_system.yaml`. |

## Recommended Edits

1. Add an item-level PREGO `GROUND` decision in `curation/decisions.tsv` for
   source concept `habitatmech:PREGO.0ce0a5364f`.
2. Redirect PREGO's `BTO:0000081` source to `UBERON:0000990` with expected label
   `reproductive system` and `grounding_status` `EXACT`.
3. Rerun `just seed`, canary `UBERON:0000990`, and run
   `just seed-apply --force` so the generated YAML is rewritten from maintained
   inputs.
4. Rerun the target-file validators, `just verify-corpus`, history and
   term-request checks, and the report/worklist exports.

## Follow-up Checks

- Confirm the next generated generic reproductive-system record has identifier
  `UBERON:0000990`, label `reproductive system`, a PREGO source attestation
  still pointing at `BTO:0000081`, and a `GROUND`/`ITEM` curation event for
  `habitatmech:PREGO.0ce0a5364f`.
- Confirm the regenerated record inherits `UBERON:0000467` from
  `data/raw/ontology_subclass_edges.tsv` rather than staying parentless under
  the BTO source id.
- Confirm the sibling PREGO records `BTO:0000082` `male reproductive system`
  and `BTO:0000083` `female reproductive system` keep their generated child
  relationship to whichever generic reproductive-system record survives.
- Run `just verify-corpus` after regeneration; it is the check that proves
  `data/habitats/` matches maintained curation and raw inputs.

## Additional Notes

- This review did not assess the sibling `male reproductive system` or
  `female reproductive system` records. They are the next two locked PREGO
  rows after the generic reproductive-system record in `data/habitats/PATHS.tsv`
  and each has a direct BTO child edge to `BTO:0000081`.
- The four PREGO characteristic taxa are emitted from exactly four raw PREGO
  taxon rows and should stay attached to the PREGO source after an exact UBERON
  redirect.
