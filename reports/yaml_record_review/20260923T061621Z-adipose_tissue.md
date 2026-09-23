# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/adipose_tissue.yaml`
- Started UTC: 2026-09-23T06:12:55Z
- Finished UTC: 2026-09-23T06:16:21Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `BTO:0001487` |
| Label | `adipose tissue` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Maintained owner | Generated from the PREGO inventory and the vendored BTO slice; generated YAML remains read-only |
| Locked slug | `data/habitats/PATHS.tsv:278` maps `BTO:0001487` to `adipose_tissue` |

This is the generated PREGO/BTO record for adipose tissue. PREGO supplies the source concept as `BTO:0001487`; the deterministic source key for any future PREGO-specific review row is `habitatmech:PREGO.975eb060ef`, computed from `sha1("PREGO:BTO:0001487")[:10]`.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/adipose_tissue.yaml` | Pass; `linkml-validate` reported `No issues found` |
| `just validate-strict data/habitats/host_associated/adipose_tissue.yaml` | Pass; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate-causal-all` | Pass; 32 causal-graph curation files with 32 graphs validated |
| `just term-requests-check` | Pass; term-request table is current with 109 terms |
| `just validate-history` | Pass; 77 history records are valid against `src/habitatmech/schema/history.yaml` |
| `just verify-corpus --max-diffs 1` | Pass; expected 3206 records, found 3206, with 0 missing, 0 extra, 0 differing |
| `just worklist --status all --limit 2000` | Pass; 953 ungrounded records and 1810 decisions are on file |
| `just report` | Pass; the report completed and kept the corpus at 3206 records |
| `git diff --check` | Pass; no whitespace errors |

## Identity and Grounding

The PREGO self-grounding is internally consistent:

- `data/raw/prego_habitats.tsv:265` directly attests `BTO:0001487` as a `biolink:GrossAnatomicalStructure`, with `taxon_count: 29`, `direct_assertion_count: 29`, maximum PREGO score `1.45999`, channel `environmental_samples`, and the 10 pipe-delimited synonym strings emitted into the generated record.
- `data/raw/ontology_terms.tsv:1487` gives `BTO:0001487` the label `adipose tissue`, the generated definition, `is_directly_referenced: TRUE`, and `label_only: FALSE`.
- `data/raw/ontology_subclass_edges.tsv:1016` records `BTO:0001487 rdfs:subClassOf BTO:0000421`, which supports the generated `connective tissue` parent.
- `data/habitats/PATHS.tsv:278` pins the reviewed identifier to the `adipose_tissue` slug.

`identifier`, `label`, `definition`, `definition_source: BTO`, `grounding_status: EXACT`, and `habitat_category: HOST_ASSOCIATED` therefore follow from committed PREGO and BTO inputs. The vendored UBERON slice also contains `UBERON:0001013` with the same primary label, but PREGO's source id is already the BTO CURIE, so the generated record correctly preserves that source identity instead of remapping to a parallel UBERON class without a curator decision.

`mapping_status: SEEDED` is expected. Ignored/hidden-inclusive exact searches for `habitatmech:PREGO.975eb060ef` and `BTO:0001487` found no item-level row in `curation/decisions.tsv`, so there is no reviewed PREGO source concept that would promote the generated record to `REVIEWED`.

## Evidence

| Claim | Nearest source | Review |
|---|---|---|
| PREGO directly attests `BTO:0001487` as adipose tissue. | `data/raw/prego_habitats.tsv:265`; `data/raw/ontology_terms.tsv:1487` | Supported exactly |
| PREGO contributes 29 distinct associated taxa by `environmental_samples`, with maximum score `1.45999`. | `data/raw/prego_habitats.tsv:265` | Supported exactly |
| The source-owned PREGO synonyms are `adipose`, `adipose tissue`, `adipose tissues`, `adiposes`, `bodyfat`, `bodyfatic`, `bodyfats`, `fat`, `fat tissue`, and `fat tissues`. | `data/raw/prego_habitats.tsv:265` | Supported exactly |
| `BTO:0001487` is a child of `BTO:0000421`. | `data/raw/ontology_subclass_edges.tsv:1016`; `data/raw/ontology_terms.tsv:423` | Supported exactly; `connective tissue` is broader than adipose tissue |
| The 25 emitted PREGO taxa preserve rank, score, channel, and any non-empty label from the raw top-25 rows. | `data/raw/prego_habitat_taxa.tsv:2331-2355` | Supported exactly |

The record has no xrefs, environmental parameters, record-level evidence, causal graphs, discussion links, datasets, or quality flags. Those absences match ignored/hidden-inclusive exact searches that found no maintained decision, term request, causal-graph overlay, history entry, target-specific research artifact, dataset row, or prior exact YAML review report for `BTO:0001487`, `habitatmech:PREGO.975eb060ef`, `adipose_tissue`, or `adipose tissue`.

Unsupported or over-scoped claims: None found. The generated `characteristic_taxa` remain observational PREGO associations: none have `is_characteristic`, `reference`, or `corroborated_by`, so the record does not strengthen PREGO's reported-from signal into a curated claim that a taxon typifies adipose tissue.

## Completeness

The PREGO attestation is complete for `data/raw/prego_habitats.tsv:265`: the record carries the source id, BTO-derived label, distinct-taxon assertion count, assertion unit, maximum score, evidence channel, and every PREGO synonym. PREGO lists 29 taxa for the source concept; the generated record intentionally keeps the top 25 and stores `candidate_pool: 29` on every emitted row, matching the truncation policy in `docs/HARMONIZATION.md`.

The three emitted taxa without `taxon_label` are also faithful to the raw input. `data/raw/prego_habitat_taxa.tsv:2339`, `2340`, and `2347` have empty labels for `NCBITaxon:35493`, `NCBITaxon:541000`, and `NCBITaxon:55087`, and the generated YAML omits labels for exactly those ranks.

No curated term request, external xref, or definition row is expected because the BTO term already supplies the record identity, definition, and broader parent. No causal graph is expected because this is a generated seed record and the repository requires independent literature evidence before mechanism edges can be authored.

Ignored/hidden-inclusive exact searches covered the target BTO id, PREGO curation key, record stem, record label, BTO parent, parallel UBERON adipose-tissue class, and the three emitted taxon ids that lacked labels, excluding generated `build`, `data/text_map`, and `pages` trees for broad content searches. They found the cited PREGO rows, BTO rows, UBERON lexical alternative, path lock, generated YAML, and expected mentions in earlier adipose-tissue review context, and no maintained row that should already have changed this target.

## Findings

None found.

No blocker findings.

No major findings.

No minor findings.

## Recommended Edits

None required.

If a future curator wants to promote this PREGO self-grounding to reviewed status, add an item-level `REVIEW` row for `habitatmech:PREGO.975eb060ef` in `curation/decisions.tsv` and rerun a BTO canary. That should be a status-only change: keep the identifier at `BTO:0001487`, keep `BTO:0000421` as the only parent, keep the PREGO source attestation and synonyms unchanged, and keep the PREGO taxa observational unless independent evidence supports stronger `is_characteristic` flags.

## Follow-up Checks

None required beyond the validators already run for this report.

For any future status-only review row, run:

- `just seed`
- `just seed-canary BTO:0001487`
- `just validate data/habitats/host_associated/adipose_tissue.yaml`
- `just validate-strict data/habitats/host_associated/adipose_tissue.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just worklist --status all --limit 2000`
- `just report`
- `git diff --check`

## Additional Notes

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-adipose_tissue.md' -print` found no pre-existing exact review report for this record before this file was written, and `find` included ignored files under the searched directory.
- Exact ignored/hidden-inclusive content searches for `BTO:0001487`, `BTO:0000421`, `UBERON:0001013`, `habitatmech:PREGO.975eb060ef`, `adipose_tissue`, `adipose tissue`, `NCBITaxon:35493`, `NCBITaxon:541000`, and `NCBITaxon:55087` found the cited PREGO, BTO, UBERON, path-lock, and generated-record rows, plus unrelated raw rows and prior reports noted above.
