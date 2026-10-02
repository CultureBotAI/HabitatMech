# YAML Record Review: amniotic cavity

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/amniotic_cavity.yaml`
- Started UTC: 2026-10-02T10:33:00Z
- Finished UTC: 2026-10-02T10:37:38Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `BTO:0000025` |
| Label | amniotic cavity |
| Definition source | `BTO` |
| Habitat category | `HOST_ASSOCIATED` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Source concepts | PREGO `BTO:0000025`; source curation key `habitatmech:PREGO.f914cf5ea0` |
| Generated path | `data/habitats/host_associated/amniotic_cavity.yaml` |

The record is generated from the committed raw PREGO and ontology inventories. No maintained
curation row, term request, causal overlay, or history record owns an item-level change for this
source concept yet.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/amniotic_cavity.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/host_associated/amniotic_cavity.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus` | Passed; 3,206 expected records, 3,206 found, 0 missing, 0 extra, 0 differing. |
| `just validate-causal-all` | Passed; 32 curation files and 32 graphs validated. |
| `just term-requests-check` | Passed; the generated ENVO term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records validated. |
| `just worklist --status all --out /tmp/habitatmech-amniotic-cavity-worklist.tsv` | Passed; wrote 953 all-status ungrounded rows. |
| `just report --out /tmp/habitatmech-amniotic-cavity-report.tsv` | Passed; row for `BTO:0000025` reports `HOST_ASSOCIATED`, `EXACT`, `SEEDED`, one PREGO source, one assertion, a definition, no parents, no parameters, one taxon, and no causal graphs. |
| `just validate-products` | Not run locally; this report does not change any grounding, and the pull request's `label-correspondence` workflow is the blocking OAK-based id-label gate. |

## Identity and Grounding

- `data/raw/ontology_terms.tsv` contains `BTO:0000025` with label `amniotic cavity`
  and definition "The space within the amnion."; this exactly matches the generated
  `identifier`, `label`, `definition`, and `definition_source`.
- `data/raw/prego_habitats.tsv` uses the same `BTO:0000025` identifier, ontology `BTO`,
  category `biolink:GrossAnatomicalStructure`, `taxon_count=1`,
  `direct_assertion_count=1`, `max_prego_score=3`, channel
  `annotated_genomes_isolates`, and synonyms `amniotic cavities|amniotic cavity`.
- `src/habitatmech/seed.py` self-grounds PREGO ENVO/BTO habitat ids to the same ontology
  CURIE, preserving the source concept under the minted curation key
  `habitatmech:PREGO.f914cf5ea0`. The generated `EXACT` grounding is therefore
  consistent with the PREGO source id and the vendored BTO term.
- The generated `HOST_ASSOCIATED` category is appropriate for a BTO gross anatomical
  structure denoting the space inside the amnion.
- There are separate GOLD `Amniotic sac` records at
  `habitatmech:GOLD.433d96f0dd` and `habitatmech:GOLD.8a86b174ba`; they are
  zero-assertion minted concepts from distinct GOLD paths and do not contribute to
  this PREGO/BTO record.

## Evidence

- The BTO ontology row supports the exact identity and definition.
- The PREGO habitat row supports the single PREGO source attestation, its
  assertion count of one distinct taxon, PREGO score `3.0`, and evidence channel
  `annotated_genomes_isolates`.
- `data/raw/prego_habitat_taxa.tsv` supports the one seeded taxon association:
  `NCBITaxon:2098` / `Metamycoplasma hominis`, rank `1`, PREGO score `3`, direct
  flag `TRUE`, channel `annotated_genomes_isolates`; `candidate_pool: 1` comes
  from the corresponding PREGO habitat `taxon_count`.
- The target carries no environmental parameters, curator-authored evidence,
  datasets, discussions, or causal graph; there are no unsupported claims in
  those slots.

## Completeness

- The record is complete for its current single PREGO source: it retains the
  source id, exact source label, untruncated taxon count, PREGO score, aggregate
  evidence channel, PREGO synonyms, and the one top taxon row.
- No parent habitat is generated. An ignored/hidden exact search of `data/raw`
  found no `BTO:0000025` subclass row in the vendored ontology edges, so there is
  no ontology parent for the seeder to copy.
- An ignored/hidden exact search over `curation`, `history`,
  `reports/yaml_record_review`, `research`, `data/raw`, and `data/habitats/PATHS.tsv`
  found no maintained item-level decision, term request, causal overlay, history
  record, or prior YAML review for `BTO:0000025`, `amniotic_cavity`, `amniotic
  cavity`, or `habitatmech:PREGO.f914cf5ea0`.
- The two GOLD `Amniotic sac` records remain unreviewed class-sweep records with
  candidate `BTO:0000025`. Their possible merge or broader/narrower relationship
  is a separate item-level GOLD review and is not required to validate this
  exact PREGO/BTO source record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No record repair is needed. If a future curator reviews the PREGO source
  concept, add an item-level `REVIEW` row for `habitatmech:PREGO.f914cf5ea0` in
  `curation/decisions.tsv`, regenerate with `just seed` and
  `just seed-canary BTO:0000025`, then prove reproduction with
  `just verify-corpus`.
- Review the two zero-assertion GOLD `Amniotic sac` records separately before
  deciding whether either is equivalent to, broader than, or merely related to
  `BTO:0000025`.

## Additional Notes

- The all-status worklist row for the GOLD `Amniotic sac` records lists
  `BTO:0000025=amniotic cavity` as a candidate for both
  `habitatmech:GOLD.433d96f0dd` and `habitatmech:GOLD.8a86b174ba`.
- `data/raw/ontology_terms.tsv` also contains nearby but distinct anatomy and
  material terms for `BTO:0000065` `amnion`, `BTO:0000068` `amniotic fluid`,
  `ENVO:02000021` `amniotic fluid material`, and `UBERON:0000173`
  `amniotic fluid`; the target is the cavity itself, not the membrane or fluid.
