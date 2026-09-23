# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/aquatic/brackish_water_body.yaml
- Started UTC: 2026-09-23T14:17:10Z
- Finished UTC: 2026-09-23T14:21:52Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | ENVO:01001321 |
| Label | brackish water body |
| Class | HabitatRecord |
| Category | AQUATIC |
| Grounding status | CLOSE |
| Mapping status | REVIEWED |
| Maintained owner | generated from `data/raw/bacdive_isolation_sources.tsv`, `data/raw/isolation_source_groundings.tsv`, `data/raw/bacdive_source_taxa.tsv`, `data/raw/ontology_terms.tsv`, `data/raw/ontology_subclass_edges.tsv`, and `curation/decisions.tsv` |

`data/habitats/aquatic/brackish_water_body.yaml` is generated and must remain read-only. It is the BacDive isolation-source record for `bacdive.isolation_source:brackish`, harmonized to the ENVO term `brackish water body`.

The exact target was resolved with ignored-file-inclusive searches:

- `find data/habitats -type f -name 'brackish_water_body.yaml' -print` found exactly one generated YAML record.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-brackish_water_body.md' -print` found no prior exact report.
- Exact `rg --no-ignore --hidden` searches for `ENVO:01001321`, `brackish_water_body`, `bacdive.isolation_source:brackish`, and `habitatmech:BACDIVE.a72887327e` across `curation`, `data/raw`, `data/habitats/PATHS.tsv`, `history`, `research`, and non-review `reports` found the expected maintained BacDive, ontology, PATHS, and decision rows only.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/brackish_water_body.yaml` | pass; no LinkML issues found |
| `just validate-strict data/habitats/aquatic/brackish_water_body.yaml` | pass; 1 file scanned, 0 files with ERROR, 0 total ERROR rows |
| `just validate-causal curation/causal_graphs/brackish_water_body.yaml` | not applicable; exact `find curation/causal_graphs -maxdepth 1 -type f -name 'brackish_water_body.yaml' -print` found no overlay |
| `just validate-causal-all` | pass; 32 causal-graph curation files with 32 graphs validated |
| Reference validator | not applicable; this generated BacDive record has no causal graph and no DOI, PMID, or URL evidence slots to inspect |
| `just term-requests-check` | pass; term-request table is current with 109 terms |
| `just validate-history` | pass; no issues found; 77 history records valid against `src/habitatmech/schema/history.yaml` |
| `just verify-corpus --max-diffs 1` | pass; 3206 expected, 3206 found, 0 missing, 0 extra, 0 differing |
| `just worklist --limit 2000` | pass; 0 ungrounded records still undecided; 1810 decisions on file |
| `just report` | pass; 3206 records; no risky groundings not yet reviewed and no global issue specific to `brackish_water_body` |
| `git diff --check` | pass |

## Identity and Grounding

The record identity is coherent:

- `data/raw/bacdive_isolation_sources.tsv` contains `bacdive.isolation_source:brackish` with label `Brackish`, source slug `brackish`, 86 strains, and 85 taxa.
- `data/raw/isolation_source_groundings.tsv` maps the normalized BacDive label `brackish` to `ENVO:01001321` / `brackish water body` with `skos:closeMatch`, `medium` confidence, `semapv:LexicalMatching`, curator `ols4_auto`, source dataset `bacdive`, and verified date `2026-05-01`.
- `curation/decisions.tsv` has an item-level `REVIEW` for `habitatmech:BACDIVE.a72887327e` accepting the seeder's resolution. The note explicitly reviewed the only semantic narrowing at issue: `water body` is ENVO's head-noun convention for the brackish environment named by BacDive, not an unsupported claim.
- `data/raw/ontology_terms.tsv` supplies `ENVO:01001321`, canonical label `brackish water body`, definition `A body of water which is primarily composed of brackish water.`, and exact synonym `brackish body of water`.
- `data/raw/ontology_subclass_edges.tsv` asserts `ENVO:01001321 rdfs:subClassOf ENVO:01001319`, matching the generated sole parent `saline water body`.
- `data/habitats/PATHS.tsv` pins `ENVO:01001321` to `brackish_water_body`.

`grounding_status: CLOSE` matches the upstream `skos:closeMatch` predicate, and `mapping_status: REVIEWED` is justified because the record has a single contributing BacDive source concept and that concept has an `ITEM`-depth review decision.

The generated synonyms are supported and scoped:

- `Brackish` is the BacDive source label and is recorded as an exact BacDive synonym for findability.
- `brackish body of water` is ENVO's exact synonym for `ENVO:01001321`.

## Evidence

This record has no causal graph and no curator-authored literature evidence. All material generated claims trace to maintained rows:

- The BacDive attestation mirrors `data/raw/bacdive_isolation_sources.tsv`: source `BACDIVE`, source ID `bacdive.isolation_source:brackish`, source label `Brackish`, 86 upstream strain assertions, and assertion unit `STRAIN`.
- The `skos:closeMatch` bridge to `ENVO:01001321` mirrors `data/raw/isolation_source_groundings.tsv`.
- The top-25 BacDive taxon rows mirror `data/raw/bacdive_source_taxa.tsv` ranks 1-25 for `bacdive.isolation_source:brackish`. The generated `association_count` values equal the BacDive strain counts, the ranks are unchanged, and `candidate_pool: 85` correctly carries the source row's full taxon count.
- Two BacDive taxon rows, `NCBITaxon:110539` and `NCBITaxon:1257027`, have blank source labels. The generated record preserves those IDs without inventing a label, which is allowed by the optional `taxon_label` slot.
- No taxon row sets `is_characteristic`; this avoids upgrading BacDive strain observations into a stronger curator claim.

No DOI, PMID, URL, or snippet evidence is cited in the record, so there is no external reference to verify for this generated BacDive projection.

## Completeness

The generated record is complete enough for its current BacDive-owned scope:

- It carries the ontology definition and parent supplied by ENVO.
- It carries the one BacDive source attestation that generated it.
- It carries the top 25 of 85 BacDive-associated taxa with rank and candidate-pool context.
- It intentionally has no GOLD `source_path`, no PREGO/MADIN score or evidence channels, and no environmental-parameter rows because no raw GOLD, PREGO, MADIN, or environment-table row asserts `ENVO:01001321`.
- Exact ignored-file-inclusive searches of `history`, `curation/term_requests.tsv`, `curation/causal_graphs`, `research`, and non-review `reports` for `brackish water body`, `brackish_water_body`, `BACDIVE.a72887327e`, `bacdive.isolation_source:brackish`, and `ENVO:01001321` found no maintained overlay, term request, curation-history file, research report, or auxiliary report for this record.
- Existing raw `environment_parameters.tsv`, PREGO, and Madin rows for `brackish water` key to `ENVO:00002019`, the water material record, not to `ENVO:01001321`, the water-body container record. Their absence from this record is therefore not a missing-data defect.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No corrective checks are required. If a future curation pass changes the BacDive grounding, BacDive source taxa, or ENVO parentage, the narrowest checks are:

- `just seed`
- `just seed-canary ENVO:01001321`
- `just validate data/habitats/aquatic/brackish_water_body.yaml`
- `just validate-strict data/habitats/aquatic/brackish_water_body.yaml`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000`
- `just report`

## Additional Notes

The BacDive source label is adjectival, while the ENVO target is a water-body class. That would usually be a narrowed grounding worth review; the existing `curation/decisions.tsv` row already did that item-level check and accepted the ENVO convention that a salinity adjective names the corresponding environmental water body.
