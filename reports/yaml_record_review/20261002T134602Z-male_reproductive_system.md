# YAML Record Review: male reproductive system

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/male_reproductive_system.yaml`
- Started UTC: 2026-10-02T13:41:00Z
- Finished UTC: 2026-10-02T13:46:16Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `BTO:0000082` |
| Label | male reproductive system |
| Definition source | `BTO` |
| Habitat category | `HOST_ASSOCIATED` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Parent habitats | `BTO:0000081` |
| Source concepts | PREGO `BTO:0000082`; source curation key `habitatmech:PREGO.31da26e113` |
| Generated path | `data/habitats/host_associated/male_reproductive_system.yaml` |

The record is generated from one PREGO source row plus the vendored BTO slice.
It has one direct PREGO taxon assertion, no environmental parameters, no
curator-authored evidence block, no causal graph, and no maintained item-level
decision row yet.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/male_reproductive_system.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/host_associated/male_reproductive_system.yaml --out /tmp/habitatmech-male-reproductive-system-instance-validation.tsv --quiet` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus` | Passed; 3,206 expected records, 3,206 found, 0 missing, 0 extra, 0 differing. |
| `just validate-causal-all` | Passed; 32 curation files and 32 graphs validated. |
| `just term-requests-check` | Passed; the generated ENVO term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records validated. |
| `just worklist --status all --out /tmp/habitatmech-male-reproductive-system-worklist.tsv` | Passed; wrote 953 all-status ungrounded rows. |
| `just report --out /tmp/habitatmech-male-reproductive-system-report.tsv` | Passed; row for `BTO:0000082` reports `HOST_ASSOCIATED`, `EXACT`, `SEEDED`, one PREGO source, one assertion, a definition, one parent, no parameters, one taxon, and no causal graphs. |
| `just validate-products` | Not run locally; this report does not change any grounding, and the pull request's `label-correspondence` workflow is the blocking OAK-based id-label gate. |

## Identity and Grounding

- `data/raw/ontology_terms.tsv` contains `BTO:0000082` with label
  `male reproductive system` and definition `The internal and external
  reproductive organs in the male.` The generated record preserves this
  identifier, label, definition, and `definition_source: BTO`.
- `data/raw/ontology_subclass_edges.tsv` has the direct BTO edge
  `BTO:0000082 rdfs:subClassOf BTO:0000081`, so the generated
  `BTO:0000081` parent is source-owned ontology hierarchy and is strictly
  broader than the male-specific child term.
- `data/raw/prego_habitats.tsv` has a direct `BTO:0000082` source row with
  ontology `BTO`, category `biolink:GrossAnatomicalStructure`, `taxon_count=1`,
  `direct_assertion_count=1`, `max_prego_score=3`, evidence channel
  `annotated_genomes_isolates`, and PREGO synonyms for male genital organ,
  male genital system, male genitalia, male reproductive system, and
  `systema genitale masculinum`.
- `src/habitatmech/seed.py` self-grounds PREGO ENVO/BTO habitat ids to the same
  ontology CURIE while preserving each PREGO source under a minted curation
  key. For this source, that key is `habitatmech:PREGO.31da26e113`, computed
  from `PREGO:BTO:0000082`.
- The source concept denotes a male animal anatomical system sampled as a host
  site, so `HOST_ASSOCIATED` is the right broad category. It is anatomy rather
  than a disease, quality, process, procedure, sample artifact, or whole host
  taxon.
- No UBERON term in the vendored slice exactly names the whole male
  reproductive system. The local UBERON slice has related component terms such
  as `UBERON:0003135` `male reproductive organ`, `UBERON:0005399` `male
  reproductive gland`, and `UBERON:0005904` `duct of male reproductive system`;
  all are parts or substructures, not exact replacements for BTO's whole-system
  class.

## Evidence

- The BTO ontology row supports the generated record identity and definition.
- The BTO subclass edge supports `BTO:0000081` as the generated
  `parent_habitats` value.
- The PREGO habitat row supports the single source attestation, its assertion
  count of one distinct taxon, PREGO score `3.0`, evidence channel
  `annotated_genomes_isolates`, and the PREGO synonyms that are not identical
  to the canonical label.
- `data/raw/prego_habitat_taxa.tsv` supports the sole seeded taxon
  association: rank 1 `NCBITaxon:1382230` / `Asaia platycodi SF2.1`, PREGO
  score `3`, direct flag `TRUE`, channel `annotated_genomes_isolates`, no
  corroborating source, and `candidate_pool: 1` from the corresponding PREGO
  habitat `taxon_count`.
- The target carries no xrefs, environmental parameters, curator-authored
  evidence, datasets, discussions, or causal graph. Ignored/hidden searches
  over `curation`, `history`, and the exact generated paths found no maintained
  input that should currently populate those fields.

## Completeness

- The record is complete for its current single PREGO source: it retains the
  source id, exact source label, one-taxon count, PREGO score, evidence channel,
  every non-canonical PREGO synonym, and the lone top taxon row.
- The aggregate TSV report row for `BTO:0000082` confirms one source, one
  upstream assertion, one definition, one parent habitat, no environmental
  parameters, one characteristic taxon, and no causal graphs.
- `just worklist --status all` does not list `BTO:0000082`; that is expected
  because the PREGO source is already self-grounded to an exact ontology class,
  not minted as an ungrounded backlog row.
- Ignored/hidden exact searches over `curation`, `history`,
  `reports/yaml_record_review`, `data/raw`, `data/habitats`, `.git/refs`, and
  `.git/packed-refs` found the expected raw PREGO rows, BTO ontology rows, the
  path lock, the generated target, and sibling mentions in the generic
  `reproductive system` report, but no maintained decision row, term request,
  history row, causal overlay, existing review branch, or prior exact YAML
  review report for `BTO:0000082`,
  `habitatmech:PREGO.31da26e113`, or
  `male_reproductive_system.yaml`.
- `find curation history -name '*male*' -o -name '*reproductive*'` found no
  target-specific curation or history artifact; `find` includes ignored files
  under the checked directories.

## Findings

None found.

## Recommended Edits

None required.

If a future curator wants to mark this PREGO self-grounding as item-reviewed,
add a `REVIEW` row for `habitatmech:PREGO.31da26e113` in
`curation/decisions.tsv` and regenerate through the seeder. That should promote
the record from `SEEDED` to `REVIEWED` without changing the identifier,
definition, `BTO:0000081` ontology parent, PREGO source attestation, or the
single PREGO taxon row.

## Follow-up Checks

- Rerun the same focused validation set if future curation changes the PREGO
  source row, the BTO vendored terms, path lock, definition handling, or taxon
  emission for `BTO:0000082`.
- If the generic `BTO:0000081` PREGO source is redirected to
  `UBERON:0000990`, confirm this child record still retains a strict broader
  reproductive-system parent and passes `just verify-corpus`.
- Review the sibling PREGO `BTO:0000083` `female reproductive system` record;
  it is the next locked sibling after `BTO:0000082` in
  `data/habitats/PATHS.tsv`.

## Additional Notes

- The current `BTO:0000081` parent is a valid broader BTO ontology class even
  though the PREGO source concept for the generic reproductive-system row
  should be separately reviewed against `UBERON:0000990`.
- The PREGO taxon row here is already one of the four generic
  `BTO:0000081` rows: `NCBITaxon:1382230` ranks second for the generic system
  and first for `male reproductive system`.
- iModulonDB structured source checks were not applicable: the record names a
  PREGO/BTO anatomical habitat and no genes, locus tags, regulators, pathways,
  stress-response terms, or transcriptomic datasets.
