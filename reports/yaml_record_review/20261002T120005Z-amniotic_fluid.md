# YAML Record Review: amniotic fluid

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/amniotic_fluid.yaml`
- Started UTC: 2026-10-02T11:52:00Z
- Finished UTC: 2026-10-02T12:00:05Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `BTO:0000068` |
| Label | amniotic fluid |
| Definition source | `BTO` |
| Habitat category | `HOST_ASSOCIATED` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Source concepts | PREGO `BTO:0000068`; source curation key `habitatmech:PREGO.d55bca41f4` |
| Generated path | `data/habitats/host_associated/amniotic_fluid.yaml` |

The record is generated from committed PREGO and ontology inventories. No
maintained item-level curation row, term request, causal overlay, history record,
or YAML review report owns a correction for this PREGO source concept yet.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/amniotic_fluid.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/host_associated/amniotic_fluid.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus` | Passed; 3,206 expected records, 3,206 found, 0 missing, 0 extra, 0 differing. |
| `just validate-causal-all` | Passed; 32 curation files and 32 graphs validated. |
| `just term-requests-check` | Passed; the generated ENVO term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records validated. |
| `just worklist --status all --out /tmp/habitatmech-amniotic-fluid-worklist.tsv` | Passed; wrote 953 all-status ungrounded rows. |
| `just report --out /tmp/habitatmech-amniotic-fluid-report.tsv` | Passed; row for `BTO:0000068` reports `HOST_ASSOCIATED`, `EXACT`, `SEEDED`, one PREGO source, one assertion, a definition, no parents, no parameters, one taxon, and no causal graphs. |
| `just validate-products` | Not run locally; this report does not change any grounding, and the pull request's `label-correspondence` workflow is the blocking OAK-based id-label gate. |

## Identity and Grounding

- `data/raw/ontology_terms.tsv` contains `BTO:0000068` with label `amniotic
  fluid`, BTO as the ontology, and a definition for the fluid within the
  amniotic cavity produced by the amnion early in embryonic development and
  later by fetal lungs and kidneys. The generated record preserves this
  identifier, label, definition, and `definition_source`.
- `data/raw/prego_habitats.tsv` has a direct `BTO:0000068` source row with
  ontology `BTO`, category `biolink:GrossAnatomicalStructure`, `taxon_count=1`,
  `direct_assertion_count=1`, `max_prego_score=3`, evidence channel
  `annotated_genomes_isolates`, and synonyms `acqua amnii|acqua
  amniis|amniotic fluid|amniotic fluids|liquor amnii|liquor amniis`.
- `src/habitatmech/seed.py` self-grounds PREGO ENVO/BTO habitat ids to the same
  ontology CURIE, preserving the source under the minted curation key
  `habitatmech:PREGO.d55bca41f4`. The generated `EXACT` grounding is therefore
  consistent with both the PREGO source id and the vendored BTO fluid term.
- The generated `HOST_ASSOCIATED` category is appropriate for a body fluid
  enclosed by the amnion in a host-associated context.
- `data/raw/ontology_terms.tsv` also contains exact or near-exact neighboring
  terms for `UBERON:0000173` `amniotic fluid` and `ENVO:02000021` `amniotic
  fluid material`. Those do not make the generated BTO identity unsupported:
  this record is an exact BTO/PREGO source record, while two later GOLD
  `Amniotic fluid` records are generated as `NARROW` minted concepts parented
  to `UBERON:0000173`.

## Evidence

- The BTO ontology row supports the record identity and definition.
- The PREGO habitat row supports the single PREGO source attestation, its
  assertion count of one distinct taxon, PREGO score `3.0`, evidence channel
  `annotated_genomes_isolates`, and PREGO-provided synonyms.
- `data/raw/prego_habitat_taxa.tsv` supports the one seeded taxon association:
  `NCBITaxon:2098` / `Metamycoplasma hominis`, rank `1`, PREGO score `3`,
  direct flag `TRUE`, and evidence channel `annotated_genomes_isolates`;
  `candidate_pool: 1` comes from the corresponding PREGO habitat `taxon_count`.
- The target carries no parent habitats, environmental parameters,
  curator-authored evidence, datasets, discussions, or causal graph. The absent
  parent list is consistent with an ignored/hidden exact search of `data/raw`,
  which found no `BTO:0000068` row in `ontology_subclass_edges.tsv`.

## Completeness

- The record is complete for its current single PREGO source: it retains the
  source id, exact source label, untruncated taxon count, PREGO score, aggregate
  evidence channel, PREGO synonyms, and the single top taxon row.
- The aggregate TSV report row for `BTO:0000068` confirms one source, one
  upstream assertion, one definition, no parent habitats, no environmental
  parameters, one characteristic taxon, and no causal graphs.
- An ignored/hidden exact search over `curation`, `history`,
  `data/habitats/RETIRED.tsv`, and `reports/yaml_record_review` found no
  maintained item-level curation decision, term request, history row,
  retirement row, or prior YAML review report for `BTO:0000068`,
  `amniotic_fluid`, or `habitatmech:PREGO.d55bca41f4`. The only existing review
  report hit is a nearby-term note in the `BTO:0000025` amniotic-cavity review.
- The two GOLD `Amniotic fluid` records at `habitatmech:GOLD.73051a70cb` and
  `habitatmech:GOLD.e29c7e3964` are distinct downstream GOLD path records. They
  remain separate from this PREGO/BTO record and should be reviewed in their own
  `PATHS.tsv` positions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No record repair is needed. If a future curator reviews the PREGO source
  concept, add an item-level `REVIEW` row for
  `habitatmech:PREGO.d55bca41f4` in `curation/decisions.tsv`, regenerate with
  `just seed` and `just seed-canary BTO:0000068`, then prove reproduction with
  `just verify-corpus`.
- Review `data/habitats/host_associated/amniotic_fluid__ff65cb2e.yaml` and
  `data/habitats/host_associated/amniotic_fluid__8d4e7d01.yaml` separately
  before making a same-as or hierarchy decision between GOLD amniotic-fluid
  paths and the PREGO/BTO record.

## Additional Notes

- `data/raw/isolation_source_groundings.tsv` contains a separate BacDive
  lexical grounding from source value `Amniotic-fluid` to `UBERON:0000173`.
  That is supporting evidence for UBERON as an exact amniotic-fluid concept,
  not an item-level decision for the PREGO `BTO:0000068` source concept.
- A prior reviewed BacDive intratissue report mentions amniotic fluid among
  enclosed sterile fluids when justifying that a broad intratissue source
  value means a mixture of internal tissues and fluids. It does not override
  this exact BTO fluid record.
