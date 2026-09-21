# YAML Record Review: alkaline water

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/aquatic/alkaline_water.yaml
- Started UTC: 2026-09-21T14:28:45Z
- Finished UTC: 2026-09-21T14:28:45Z
- Verdict: pass

## Target

The target is the generated `HabitatRecord` at `data/habitats/aquatic/alkaline_water.yaml`.

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `ENVO:01000357` |
| Label | `alkaline water` |
| Category | `AQUATIC` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| MADIN source concept | `habitatmech:MADIN.1aa3827c6d` |
| MADIN source ID | `ENVO:01000357` |
| Locked stem | `alkaline_water` in `data/habitats/PATHS.tsv` |

This review covers the single MADIN source concept that self-grounds to vendored ENVO term `ENVO:01000357`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/alkaline_water.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/aquatic/alkaline_water.yaml --quiet` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; 3,206 expected records, 3,206 records on disk, 0 missing, 0 extra, 0 differing. |
| Reference validator | Not checked: this record has no DOI/PMID/URL `EvidenceItem`, no causal-edge evidence, and no target-specific `curation/causal_graphs/` overlay. |

## Identity and Grounding

The record denotes alkaline water, using the same `ENVO:01000357` CURIE and `alkaline water` label that Madin supplies in `data/raw/madin_habitats.tsv`. The vendored ENVO row for `ENVO:01000357` has label `alkaline water` and definition `A portion of alkaline water is a portion of water with a pH greater than 7.`, so the generated identifier, label, definition text, and `definition_source: ENVO` agree.

The ontology parent is direct and strictly broader: `data/raw/ontology_subclass_edges.tsv` contains `ENVO:01000357 rdfs:subClassOf ENVO:00002006`, and `data/raw/ontology_terms.tsv` labels `ENVO:00002006` as `liquid water`.

`mapping_status: SEEDED` is correct because the source concept key `habitatmech:MADIN.1aa3827c6d` has no item-level row in `curation/decisions.tsv`. Exact hidden/ignored-inclusive searches before this report was created covered the maintained `curation/`, `history/`, and `data/raw/` surfaces plus `data/habitats/PATHS.tsv` and prior `reports/yaml_record_review/` reports; they found the maintained MADIN, ontology, environment-parameter, GOLD-triad, and PATHS rows cited here plus contextual mentions in the prior `alkaline__02df7139` report, but no `curation/decisions.tsv`, `curation/term_requests.tsv`, or `curation/causal_graphs/` row or file for `ENVO:01000357`, `alkaline_water`, `alkaline water`, or `habitatmech:MADIN.1aa3827c6d`.

## Evidence

| Claim | Evidence | Assessment |
|---|---|---|
| MADIN attests `ENVO:01000357` as `alkaline water`. | `data/raw/madin_habitats.tsv` has the row `ENVO:01000357	ENVO	alkaline water	23`. | Supported. |
| The generated label and definition match the vendored ENVO identity. | `data/raw/ontology_terms.tsv` contains `ENVO:01000357` with label `alkaline water` and the same definition. | Supported. |
| The ontology parent `ENVO:00002006` is a direct superclass of alkaline water. | `data/raw/ontology_subclass_edges.tsv` contains `ENVO:01000357 rdfs:subClassOf ENVO:00002006`; `data/raw/ontology_terms.tsv` labels `ENVO:00002006` as `liquid water`. | Supported. |
| `data/habitats/aquatic/alkaline_water.yaml` is the stable file path for this record. | `data/habitats/PATHS.tsv` maps `ENVO:01000357` to `alkaline_water`. | Supported. |
| The source attestation count is 23 MADIN taxon associations. | `data/raw/madin_habitats.tsv` lists `taxon_count=23`, and `data/raw/madin_habitat_taxa.tsv` has 23 rows for `ENVO:01000357`. | Supported. |
| The generated taxon set preserves the current MADIN associations. | The 23 `NCBITaxon` IDs and labels in `data/raw/madin_habitat_taxa.tsv` match the target record's 23 MADIN `characteristic_taxa`, each with `candidate_pool: 23`. | Supported. |
| Existing target-specific causal evidence belongs on this record. | Exact hidden/ignored-inclusive searches of the maintained curation surfaces, `history`, and prior review reports found no target-specific overlay, term request, or prior review for `alkaline_water`, `ENVO:01000357`, or `habitatmech:MADIN.1aa3827c6d` before this report was created. | Not supported by current maintained inputs. |

## Completeness

The generated record preserves every current MADIN fact for the target: the ENVO source ID, the source label, the 23-taxon assertion count, the `TAXON` unit, and the 23 emitted taxon IDs and source labels. MADIN supplies no score, rank, or citation per association, and the seeder deliberately does not manufacture rank or score for these rows.

The empty `environmental_parameters` list is appropriate for the current maintained inputs. `data/raw/environment_parameters.tsv` has nine `water_fresh_alkaline` rows that mention `ENVO:01000357`, but each row is keyed to the conjunction `ENVO:00002011|ENVO:01000357` / `fresh water|alkaline water`. The seeder skips multi-term environment-parameter rows because their values belong to the compound environment rather than to either component term in isolation.

Empty `evidence`, `causal_graphs`, `discussions`, and `datasets` are also appropriate for this seeded MADIN-only record. No maintained input currently supplies those fields, and no target-specific causal overlay exists.

## Findings

None found.

## Recommended Edits

None found.

## Follow-up Checks

None found.

## Additional Notes

GOLD MIxS triad rows also mention `ENVO:01000357` as a medium for `Environmental > Aquatic > Non-marine Saline and Alkaline > Alkaline` and `Environmental > Aquatic > Non-marine Saline and Alkaline > Alkaline > Mine pit pond`. Those rows support the presence of `alkaline water` in the generated `alkaline__02df7139` context; they are not source attestations for this MADIN alkaline-water record.

If this MADIN source concept is ever promoted to item-reviewed, the maintained decision should key on `habitatmech:MADIN.1aa3827c6d`.
