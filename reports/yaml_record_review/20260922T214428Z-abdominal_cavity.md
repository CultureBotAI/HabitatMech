# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/abdominal_cavity.yaml`
- Started UTC: 2026-09-22T21:40:28Z
- Finished UTC: 2026-09-22T21:44:28Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/host_associated/abdominal_cavity.yaml` |
| Class | `HabitatRecord` |
| Identifier | `UBERON:0003684` |
| Label | `abdominal cavity` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Record status | Generated from one GOLD source concept grounded to UBERON |

This is the generated record for the GOLD path `Host-associated > Mammals > Abdominal cavity`. The GOLD source-concept key is `habitatmech:GOLD.0f0e988a89`, computed from `sha1("GOLD:Host-associated > Mammals > Abdominal cavity")[:10]`, and the generated record resolves to `UBERON:0003684` because the GOLD leaf label exactly matches the vendored UBERON `abdominal cavity` label.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/abdominal_cavity.yaml` | Passed; LinkML validation reported no issues. |
| `just validate-strict data/habitats/host_associated/abdominal_cavity.yaml` | Passed; one file scanned with 0 error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; expected 3206 generated records, found 3206, with 0 missing, 0 extra, and 0 differing. |
| `git diff --check` | Passed; no whitespace errors. |

## Identity and Grounding

The GOLD source identity is supported:

| Raw field | Value |
|---|---|
| `canonical_path` | `Host-associated > Mammals > Abdominal cavity` |
| `ecosystem` | `Host-associated` |
| `ecosystem_category` | `Mammals` |
| `ecosystem_type` | `Abdominal cavity` |
| `leaf_label` | `Abdominal cavity` |
| `depth` | `3` |
| `gold_node_count` | `1` |
| `organism_count` | `0` |
| `study_count` | `0` |
| `biosample_count` | `0` |
| `total_assertions` | `0` |
| `gold_node_ids` | `gold.ecosystem:6742` |

The UBERON grounding is supported. `data/raw/ontology_terms.tsv:13210` defines `UBERON:0003684` as `abdominal cavity`, with the exact synonyms `cavitas abdominis`, `cavity of abdominal compartment`, `cavity of compartment of abdomen`, and `space of abdominal compartment`. The generated identifier, label, definition, definition source, and four `EXACT_SYNONYM` rows all match that ontology row.

`source_attestations` matches `data/raw/gold_ecosystem_paths.tsv:1979`: the record keeps `gold.ecosystem:6742` as the source id, records the `Abdominal cavity` leaf label and canonical GOLD path exactly, omits `assertion_count` because the raw organism count is zero, and does not add a multi-node note because the path has only one GOLD node id.

Both generated parents are supported and strictly broader:

- `UBERON:0000464` comes from `data/raw/ontology_subclass_edges.tsv:11451`, which states `UBERON:0003684 rdfs:subClassOf UBERON:0000464`; `data/raw/ontology_terms.tsv:12941` labels that parent `anatomical space`.
- `habitatmech:GOLD.e889967f4f` comes from GOLD source hierarchy. `data/raw/gold_ecosystem_paths.tsv:9` records the immediate parent path `Host-associated > Mammals`, and `data/habitats/host_associated/mammals.yaml` is the reviewed, defined `mammal-associated environment` record for that path.

`grounding_status: EXACT` is mechanically expected for an uncurated exact GOLD-to-ontology label match. `mapping_status: SEEDED` is also expected: ignored/hidden-inclusive exact searches for `habitatmech:GOLD.0f0e988a89` and `UBERON:0003684` found no maintained `curation/decisions.tsv` row for the source concept, so there is no item-level decision to promote this record to `REVIEWED`.

## Evidence

| Claim | Nearest support | Review |
|---|---|---|
| The generated record represents the GOLD path `Host-associated > Mammals > Abdominal cavity`. | `data/raw/gold_ecosystem_paths.tsv:1979` | Supported exactly. |
| The GOLD source row has no upstream organism, study, or biosample assertions. | `data/raw/gold_ecosystem_paths.tsv:1979` | Supported exactly. |
| `UBERON:0003684` contributes the label, definition, and synonyms. | `data/raw/ontology_terms.tsv:13210` | Supported exactly. |
| `UBERON:0000464` is an ontology parent of `UBERON:0003684`. | `data/raw/ontology_subclass_edges.tsv:11451`; `data/raw/ontology_terms.tsv:12941` | Supported exactly. |
| `habitatmech:GOLD.e889967f4f` is the source-path parent. | `data/raw/gold_ecosystem_paths.tsv:9`; `curation/decisions.tsv:1285`; `curation/term_requests.tsv:5`; `data/habitats/host_associated/mammals.yaml` | Supported. The GOLD parent path is `Host-associated > Mammals`, and its reviewed generated record is defined as `mammal-associated environment`. |

Unsupported or over-scoped claims: None found. The record keeps only GOLD source provenance, UBERON lexical data, the UBERON asserted superclass, and the GOLD source-path parent. It does not claim organism associations, environmental parameters, characteristic taxa, or causal mechanisms.

## Completeness

The direct GOLD source attestation is complete for a zero-assertion, one-node raw row: the record carries the source name, source id, source label, source path, and exact-match predicate, while correctly omitting assertion-count and multi-node-note fields.

The immediate GOLD children `Host-associated > Mammals > Abdominal cavity > Ascites`, `Peritoneal fluid`, and `Peritoneum` appear as separate generated records under the `UBERON:0003684` parent. Their existence confirms that the source hierarchy is represented downstream; they need their own item-level review and do not imply missing direct claims on this parent record.

No maintained curation input was found for `habitatmech:GOLD.0f0e988a89`, `UBERON:0003684`, `gold.ecosystem:6742`, `abdominal_cavity`, or the exact source path; the ignored/hidden-inclusive searches covered `curation`, `history`, `research`, `reports`, `data/raw`, and `data/habitats`, excluding only generated `data/text_map`, `pages`, and `build` outputs from the broad exact content searches.

No maintained causal overlay, history file, raw research report, or prior exact YAML review report was found by filename for `abdominal_cavity` or `abdominal-cavity` under `curation/causal_graphs`, `history`, `research`, or `reports/yaml_record_review`; the `find` search included ignored files beneath those checked directories.

## Findings

None found.

No blocker findings.

No major findings.

No minor findings.

## Recommended Edits

None required.

If a future curator wants to mark the GOLD exact match item-reviewed, add a `REVIEW` row for `habitatmech:GOLD.0f0e988a89` in `curation/decisions.tsv` and rerun `just seed-canary UBERON:0003684`. That should be a status-only change: keep the identifier at `UBERON:0003684` and keep both existing parents.

## Follow-up Checks

None required beyond the validators already run for this report.

For any future status-promotion-only edit, run:

- `just seed-canary UBERON:0003684`
- `just validate data/habitats/host_associated/abdominal_cavity.yaml`
- `just validate-strict data/habitats/host_associated/abdominal_cavity.yaml`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `git diff --check`

## Additional Notes

- The pre-report exact filename check `find reports/yaml_record_review -maxdepth 1 -type f -name '*abdominal_cavity*' -print` returned no previous exact report; `find` includes ignored files.
- `just worklist` did not list `habitatmech:GOLD.0f0e988a89`, `UBERON:0003684`, or `Abdominal cavity`, consistent with a GOLD leaf whose label is already generated as `EXACT`.
- `just report` completed successfully and did not flag `UBERON:0003684` or `habitatmech:GOLD.0f0e988a89` in any risky-grounding, GOLD-triad, novel-label, unsupported-prefix, or non-habitat section.
