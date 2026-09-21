# YAML Record Review: alkaline salt lake

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/aquatic/alkaline_salt_lake.yaml
- Started UTC: 2026-09-21T13:48:35Z
- Finished UTC: 2026-09-21T13:50:50Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Path | `data/habitats/aquatic/alkaline_salt_lake.yaml` |
| Identifier | `ENVO:00002121` |
| Label | `alkaline salt lake` |
| Category | `AQUATIC` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Source | PREGO |
| Source ID | `ENVO:00002121` |
| Source label | `alkaline salt lake` |

The target is a generated PREGO-only record grounded directly to the ENVO term
PREGO cites. It has an ENVO definition, ENVO and PREGO synonyms, one ENVO
parent, one PREGO source attestation, 22 PREGO taxon associations, and a
generated seed event. It has no xrefs, environmental parameters, record-level
evidence, causal graph, discussions, or datasets.

`data/habitats/PATHS.tsv` pins `ENVO:00002121` to the stable
`alkaline_salt_lake` slug. If a future curator wants to promote this source
concept to `REVIEWED`, the maintained decision key is
`habitatmech:PREGO.fd951b4ee2`, the first ten hex characters of
`sha1("PREGO:ENVO:00002121")`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/alkaline_salt_lake.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/aquatic/alkaline_salt_lake.yaml --quiet` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just term-requests-check` | Passed; the generated term-request table is current with 109 terms. |
| Reference validator | Not checked: this record has no `EvidenceItem` references or causal overlay, and this repository documents no standalone reference validator for a generated record without those objects. |
| `just validate-history` | Passed; 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; 3,206 expected records were present, with 0 missing, 0 extra, and 0 differing files. |

## Identity and Grounding

The generated identity is reproducible and exact:

| Claim | Review |
|---|---|
| PREGO source ID | Supported. `data/raw/prego_habitats.tsv` has the exact `prego_id` `ENVO:00002121`. |
| Ontology term | Supported. `data/raw/ontology_terms.tsv` contains `ENVO:00002121` with label `alkaline salt lake`, definition `A saline lake which has a high pH.`, and synonym `soda lake`. |
| Label and definition | Supported. `ConceptStore.get` seeds ontology-grounded labels, definitions, and ENVO exact synonyms from `ontology_terms.tsv`; the generated label and definition match the vendored ENVO row. |
| Category | Supported. PREGO concepts do not carry a GOLD path, so `src/habitatmech/seed.py` derives `AQUATIC` from the ENVO ancestry of `ENVO:00002121`. |
| `grounding_status: EXACT` | Supported. `ingest_prego` initially resolves each PREGO CURIE to itself with route `prego_self_grounded`; no `curation/decisions.tsv` override changes this source concept. |
| `mapping_status: SEEDED` | Supported. The PREGO source concept has no item-level maintained decision, so `mapping_status` stays `SEEDED` even though the lexical grounding itself is direct. |

The hierarchy is also sound. `data/raw/ontology_subclass_edges.tsv` states
`ENVO:00002121 rdfs:subClassOf ENVO:00000019`, and `ENVO:00000019` is the
vendored `saline lake` term. The generated `parent_habitats` list therefore
preserves a direct ENVO is-a edge from alkaline salt lake to saline lake.

## Evidence

Supported:

| Claim | Evidence |
|---|---|
| PREGO attests the `ENVO:00002121` habitat with 22 taxa. | `data/raw/prego_habitats.tsv` has `taxon_count=22`, `direct_assertion_count=22`, `max_prego_score=3`, and `channels=annotated_genomes_isolates` for `ENVO:00002121`; the generated `SourceAttestation` records 22 `TAXON` assertions, score `3.0`, and the same evidence channel. |
| The record carries all PREGO synonyms. | `prego_synonyms` is `alkaline salt lake|alkaline salt lakes|soda lake|soda lakes`; `ingest_prego` adds each non-label synonym as a `RELATED_SYNONYM` from `PREGO`, while `ConceptStore.get` adds ENVO's `soda lake` synonym as an `EXACT_SYNONYM`. |
| The taxon table is a lossless copy of the exact PREGO rows. | `data/raw/prego_habitat_taxa.tsv` has 22 rows for `ENVO:00002121`; the generated record carries the same 22 `NCBITaxon` identifiers, labels, ranks, scores, and `candidate_pool: 22` values. |
| No PREGO rows were truncated away. | The PREGO habitat row reports `taxon_count=22`, matching the 22 retained rows in both `prego_habitat_taxa.tsv` and the generated record. |

Unsupported or over-scoped:

None found.

No literature citations, record-level evidence, causal edges, environmental
parameters, discussions, or datasets are attached to this record.

## Completeness

The record is complete enough for the current generated PREGO surface:

- The ENVO identity, label, definition, synonym, and direct parent are all
  present in the vendored ontology slice.
- The single PREGO source attestation preserves the exact upstream source ID,
  source label, taxon count, max score, and channel summary.
- Every exact PREGO taxon row is retained, and every rank is interpretable
  because `candidate_pool` matches the full 22-taxon PREGO pool.
- Empty `xrefs`, environmental parameters, causal graphs, discussions, and
  datasets are appropriate; there is no maintained curation input requiring
  any of those optional fields for this record.

Bounded absence checks:

| Query | Scope | Result |
|---|---|---|
| `ENVO:00002121` and `alkaline_salt_lake` | Hidden/ignored-inclusive search over `curation/decisions.tsv`, `curation/term_requests.tsv`, `curation/causal_graphs`, `data/habitats/PATHS.tsv`, `reports/yaml_record_review`, and `research/habitats` | Found the `PATHS` slug row and two contextual mentions in a neighboring `non-marine_saline_and_alkaline` research report; found no maintained decision row, term request, causal overlay, or prior YAML review for this record. |
| `ENVO:00002121` | Hidden/ignored-inclusive search over `data/raw/prego_habitats.tsv`, `data/raw/prego_habitat_taxa.tsv`, `data/raw/ontology_terms.tsv`, and `data/raw/ontology_subclass_edges.tsv` | Found the exact PREGO habitat row, all 22 exact PREGO taxon rows, the ENVO term row, and the ENVO direct subclass edge to `ENVO:00000019`. |

## Findings

### Blocker

None found.

### Major

None found.

### Minor

None found.

## Recommended Edits

None found.

## Follow-up Checks

None required beyond the validators already run.

## Additional Notes

- The generated YAML section name `characteristic_taxa` does not claim these
  PREGO rows typify alkaline salt lakes. The schema defines the class as taxa
  associated with the habitat, and the rendered page correctly presents them
  as taxa reported from the habitat.
- None of the 22 PREGO taxa for `ENVO:00002121` are corroborated by a second
  source in this record. All 22 have the same PREGO score, so their rank is
  PREGO's own tie ordering rather than stronger per-taxon evidence.
- The repeated `soda lake` synonym is intentional provenance preservation:
  ENVO supplies it as an exact synonym and PREGO independently supplies the
  same string as a lexical variant.
