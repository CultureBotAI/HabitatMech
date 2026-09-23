# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/aquatic/brackish_estuary.yaml
- Started UTC: 2026-09-23T13:23:00Z
- Finished UTC: 2026-09-23T13:40:39Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/aquatic/brackish_estuary.yaml` |
| Class | `HabitatRecord` |
| Identifier | `ENVO:00002137` |
| Label | `brackish estuary` |
| Category | `AQUATIC` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Maintained inputs | `data/raw/prego_habitats.tsv`, `data/raw/prego_habitat_taxa.tsv`, `data/raw/ontology_terms.tsv`, `data/raw/ontology_subclass_edges.tsv`, `data/habitats/PATHS.tsv` |
| Generated output | Yes. `data/habitats/` records are emitted from `src/habitatmech/seed.py`; future curation belongs in the maintained inputs above, `curation/decisions.tsv`, `curation/term_requests.tsv`, or a relevant `curation/causal_graphs/*.yaml` overlay. |

The full record was reviewed. It is a PREGO-only ENVO-seeded habitat record with one PREGO source attestation, one PREGO taxon association, one PREGO source synonym, the ENVO definition, the ENVO parent `ENVO:00000045`, and the generated seed history event.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/brackish_estuary.yaml` | Pass: LinkML validation reported no issues. |
| `just validate-strict data/habitats/aquatic/brackish_estuary.yaml` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-causal-all` | Pass: 32 causal-graph curation files and 32 graphs validated. |
| `just term-requests-check` | Pass: committed term-request table is current at 109 terms. |
| `just validate-history` | Pass: no issues found; 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Pass: 3206 expected records, 3206 records found, 0 missing, 0 extra, 0 differing; the corpus reproduces exactly from `data/raw/`. |
| `just worklist --limit 2000` | Pass: 0 ungrounded records still undecided; 1810 decisions on file. |
| `just report` | Pass: full corpus report completed for 3206 records. |
| `git diff --check` | Pass: no whitespace errors. |
| Reference validator | Not applicable: this bare seeded record has no reference-bearing `evidence`, `causal_graphs`, `environmental_parameters.reference`, `discussions`, or `datasets`, and HabitatMech exposes no focused reference validator for such a record. |

## Identity and Grounding

| Assertion | Review |
|---|---|
| `identifier: ENVO:00002137` | Supported. `data/raw/ontology_terms.tsv` carries `ENVO:00002137` as an ENVO term with canonical label `brackish estuary` and the same definition copied into the generated record. |
| `label: brackish estuary` | Supported by the vendored ontology row and matches the PREGO source concept label emitted by `ingest_prego`. |
| PREGO source identity | Supported. `data/raw/prego_habitats.tsv` has one row for `ENVO:00002137` with `taxon_count=1`, `direct_assertion_count=1`, `max_prego_score=3`, channel `annotated_genomes_isolates`, and synonyms `brackish estuaries|brackish estuary`. |
| `grounding_status: EXACT` | Supported for this seeded state. PREGO concepts are ENVO/BTO CURIEs; `src/habitatmech/seed.py` self-grounds PREGO rows exactly unless a curation decision overrides them. |
| `mapping_status: SEEDED` | Supported. Gitignore-independent searches of `curation`, `history`, and `research` found no item-level curation decision, term request, causal overlay, or history record for `ENVO:00002137`, so the seeder correctly leaves the generated record `SEEDED`. |
| `habitat_category: AQUATIC` | Supported by ENVO ancestry and the seeder's category inference for an ENVO water-body class. |
| `parent_habitats: ENVO:00000045` | Supported. `data/raw/ontology_subclass_edges.tsv` asserts `ENVO:00002137 rdfs:subClassOf ENVO:00000045`, and `data/raw/ontology_terms.tsv` carries `ENVO:00000045` as the vendored `estuary` class. |
| Path slug | Supported. `data/habitats/PATHS.tsv` maps `ENVO:00002137` to `brackish_estuary`. |

The parent is strictly broader: `ENVO:00000045` denotes estuaries in general, while this record denotes the more specific brackish-water kind of estuary. No sibling, near-match, process, chemical, quality, or host-taxon concept is being adopted as the record identity.

## Evidence

| Record field | Nearest maintained evidence | Review |
|---|---|---|
| Definition | `data/raw/ontology_terms.tsv` row for `ENVO:00002137` | Supported. The generated `definition` exactly matches the vendored ENVO definition, and `definition_source: ENVO` is the correct provenance for that source-owned text. |
| `source_attestations[0]` | `data/raw/prego_habitats.tsv` row for `ENVO:00002137` | Supported. Source, source ID, source label, count/unit, score, and channel match the raw PREGO habitat row: one distinct taxon, score 3, `annotated_genomes_isolates`. |
| PREGO synonym `brackish estuaries` | `data/raw/prego_habitats.tsv` `prego_synonyms` for `ENVO:00002137` | Supported. The seeder suppresses the source synonym equal to the record label and retains the plural source spelling as a PREGO `RELATED_SYNONYM`. |
| `characteristic_taxa[0]` | `data/raw/prego_habitat_taxa.tsv` row for `ENVO:00002137` | Supported. `NCBITaxon:94122` / `Shewanella sp. ANA-3`, score 3, rank 1, and candidate pool 1 match the sole PREGO taxon row for this habitat. |
| Causal graph evidence | `curation/causal_graphs/*.yaml` | Correctly absent. Searches for `ENVO:00002137`, `brackish estuary`, and `brackish_estuary` in the curated overlays and curation tables found no overlay that would generate causal edges. |

The PREGO taxon association is not overclaimed as a curated characteristic assertion. The generated `CharacteristicTaxon` lacks `is_characteristic`, so under the schema and seeder comments it records a reported PREGO association only.

## Completeness

No consequential gaps were found for a generated, PREGO-only, exactly grounded ENVO seed:

| Area | Review |
|---|---|
| Definition | Present from ENVO and faithfully preserved. |
| Xrefs | None expected from the inspected PREGO and ontology inputs. |
| Environmental parameters | None expected; this habitat is not supplied by `data/raw/environment_parameters.tsv`. |
| Causal graphs | None expected; no maintained overlay targets this one-assertion record. |
| Discussions or datasets | None expected for a seeded record with no curator-authored uncertainty. |
| Prior reports | `find reports/yaml_record_review -maxdepth 1 -type f -name '*-brackish_estuary.md' -print` found no earlier exact report; the search included ignored files through `find`. |
| Existing curation | Gitignore-independent searches found no `ENVO:00002137`, `brackish estuary`, or `brackish_estuary` curation row in `curation/*.tsv`, `curation/term_requests/*.tsv`, or `curation/causal_graphs/*.yaml`. |
| External research | Gitignore-independent searches found no `ENVO:00002137`, `brackish estuary`, `brackish_estuary`, or `NCBITaxon:94122` hit in `research/` or existing YAML review reports. |

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No follow-up is required. If a future curator promotes this PREGO source from `SEEDED` to `REVIEWED`, add an item-level row for the PREGO source concept in `curation/decisions.tsv`, regenerate through the seeder, and rerun:

- `just validate data/habitats/aquatic/brackish_estuary.yaml`
- `just validate-strict data/habitats/aquatic/brackish_estuary.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just report`
- `git diff --check`

## Additional Notes

- Exact searches for absence checks used `find` or `rg --no-ignore --hidden`, so ignored files were included.
- The same `NCBITaxon:94122` strain also appears in the raw Madin and PREGO taxon tables for `ENVO:01000357` and `ENVO:00005792`, which feed separate generated alkaline-water and underground-water records. Those source observations do not conflict with this record's one-row PREGO brackish-estuary association.
