# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/actinic_keratosis.yaml`
- Started UTC: 2026-09-23T04:50:00Z
- Finished UTC: 2026-09-23T04:54:24Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/host_associated/actinic_keratosis.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.9c17a8a454` |
| Label | `Actinic keratosis` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `NOT_APPLICABLE` |
| Mapping status | `REVIEWED` |
| Record status | Generated from one GOLD source concept plus an item-level `curation/decisions.tsv` review |

This is the generated record for the GOLD path `Host-associated > Mammals: Human > Malignant tumor > Carcinoma > Actinic keratosis`. The source-concept key is `habitatmech:GOLD.9c17a8a454`, computed from `sha1("GOLD:Host-associated > Mammals: Human > Malignant tumor > Carcinoma > Actinic keratosis")[:10]`.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/actinic_keratosis.yaml` | Passed; LinkML validation reported no issues. |
| `just validate-strict data/habitats/host_associated/actinic_keratosis.yaml` | Passed; 1 file scanned with 0 error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; expected 3206 generated records, found 3206, with 0 missing, 0 extra, and 0 differing. |
| `just worklist --limit 2000` | Passed; 0 ungrounded records are still undecided and 1810 decisions are on file. |
| `just report` | Passed; the report completed and did not flag `habitatmech:GOLD.9c17a8a454` in the risky-grounding, stale-sweep, non-habitat-claim, GOLD-triad, unsupported-prefix, or organism-identity sections. |
| `git diff --check` | Passed; no whitespace errors. |

## Identity and Grounding

The GOLD source identity is supported:

| Raw field | Value |
|---|---|
| `canonical_path` | `Host-associated > Mammals: Human > Malignant tumor > Carcinoma > Actinic keratosis` |
| `ecosystem` | `Host-associated` |
| `ecosystem_category` | `Mammals: Human` |
| `ecosystem_type` | `Malignant tumor` |
| `ecosystem_subtype` | `Carcinoma` |
| `specific_ecosystem` | `Actinic keratosis` |
| `leaf_label` | `Actinic keratosis` |
| `depth` | `5` |
| `gold_node_count` | `1` |
| `organism_count` | `0` |
| `study_count` | `0` |
| `biosample_count` | `0` |
| `total_assertions` | `0` |
| `gold_node_ids` | `gold.ecosystem:6193` |

`source_attestations` matches `data/raw/gold_ecosystem_paths.tsv:2324`: the record keeps `gold.ecosystem:6193` as the source id, records the `Actinic keratosis` leaf label and canonical GOLD path exactly, omits `assertion_count` and `assertion_unit` because the raw ecosystem-path row has 0 organism assertions, and omits a multi-node note because the raw row has a single GOLD node id.

The reviewed `NOT_APPLICABLE` disposition is supported by `curation/decisions.tsv:906`. The decision has no object term, no relation, and `review_depth: ITEM`; it records that `Actinic keratosis` names a disease, intervention, sampling artifact, or no-value filler rather than a place.

The generated parent is also supported. `GOLD:Host-associated > Mammals: Human > Malignant tumor > Carcinoma` hashes to `habitatmech:GOLD.9bb307824f`; `data/raw/gold_ecosystem_paths.tsv:2323` records that exact Carcinoma parent path; `data/habitats/PATHS.tsv:2445` pins it to `carcinoma`; and `data/habitats/host_associated/carcinoma.yaml` is itself an item-level reviewed `NOT_APPLICABLE` disease record. Keeping that parent preserves GOLD's original disease hierarchy while both records remain reviewed as non-habitats.

## Evidence

| Claim | Nearest support | Review |
|---|---|---|
| The generated record represents the GOLD path `Host-associated > Mammals: Human > Malignant tumor > Carcinoma > Actinic keratosis`. | `data/raw/gold_ecosystem_paths.tsv:2324`; `data/habitats/PATHS.tsv:2450` | Supported exactly. |
| The source row comes from one GOLD ecosystem node with 0 organism assertions. | `data/raw/gold_ecosystem_paths.tsv:2324` | Supported exactly. |
| `Actinic keratosis` is reviewed as non-applicable. | `curation/decisions.tsv:906` | Supported exactly. The item-level row decided this disease leaf individually after pulling it out of the class-level sweep. |
| `habitatmech:GOLD.9bb307824f` is the immediate GOLD Carcinoma parent. | `data/raw/gold_ecosystem_paths.tsv:2323`; `data/habitats/PATHS.tsv:2445`; `data/habitats/host_associated/carcinoma.yaml` | Supported exactly. |

Unsupported or over-scoped claims: None found. The record carries only GOLD source provenance, the reviewed non-habitat disposition, the source-path parent, and generated audit metadata. It does not claim a habitat grounding, definition, environmental parameter, characteristic taxon, causal mechanism, record-level evidence item, or dataset reference.

## Completeness

The direct GOLD source attestation is complete for a zero-organism, one-node raw row: it carries the source name, source id, source label, and source path, while correctly omitting organism `assertion_count`, `assertion_unit`, score, evidence-channel, and multi-node note fields.

Separate GOLD side tables contain context but do not imply a missing generated field. `data/raw/gold_path_biosamples.tsv:772` records 5 biosamples for ecosystem path `6193`, and `data/raw/gold_studies.tsv:3157` records one multi-path study containing the exact Actinic keratosis path.

No term request is expected for this record because the item-level review already decided that the GOLD source concept is not a habitat. Exact ignored/hidden-inclusive searches for `habitatmech:GOLD.9c17a8a454`, `gold.ecosystem:6193`, `Actinic keratosis`, and `actinic_keratosis` found the maintained decision, the raw GOLD rows, the locked `PATHS.tsv` row, and the generated YAML; the same target-specific search found no `curation/term_requests.tsv`, `curation/term_requests_excluded.tsv`, `curation/causal_graphs`, `history`, `research/habitats`, or prior `reports/yaml_record_review` artifact for this source concept. Generated `data/text_map`, `pages`, and `build` outputs were excluded only from broad exact content searches.

The exact pre-report filename check `find reports/yaml_record_review -maxdepth 1 -type f -name '*-actinic_keratosis.md' -print` returned no rows; `find` includes ignored files under the searched directory.

## Findings

None found.

No blocker findings.

No major findings.

No minor findings.

## Recommended Edits

None required.

## Follow-up Checks

None required beyond the validators already run for this review.

Re-run the same focused validation set if a future curation change reopens this disease leaf or one of its Carcinoma siblings:

- `just validate data/habitats/host_associated/actinic_keratosis.yaml`
- `just validate-strict data/habitats/host_associated/actinic_keratosis.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `git diff --check`

## Additional Notes

- The Actinic keratosis leaf matches the previously reviewed Bowen's disease and breast-cancer GOLD disease records: a `NOT_APPLICABLE` source concept under a generated `NOT_APPLICABLE` disease parent.
- Exact no-ignore searches found no raw `data/raw/gold_path_triads.tsv` row for the Actinic keratosis path. That absence search included ignored files in `data/raw`.
- Broad exact content searches used `rg --no-ignore --hidden` and excluded generated `data/text_map`, `pages`, and `build` outputs. Exact filename searches used `find` and therefore included ignored files in the searched directories.
