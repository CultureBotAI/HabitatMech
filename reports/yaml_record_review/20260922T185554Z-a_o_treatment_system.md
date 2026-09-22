# YAML Record Review: A/O treatment system

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/a_o_treatment_system.yaml`
- Started UTC: 2026-09-22T18:54:35Z
- Finished UTC: 2026-09-22T18:55:54Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/engineered/a_o_treatment_system.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.7c91485eb8` |
| Label | `A/O treatment system` |
| Category | `ENGINEERED` |
| Grounding status | `NOT_APPLICABLE` |
| Mapping status | `REVIEWED` |
| Record status | Generated from `data/raw/` plus maintained curation decisions |

This is the generated GOLD record for the path `Engineered > WWTP > A/O treatment system`. Its identifier is the deterministic minted id `habitatmech:GOLD.7c91485eb8`, computed from `sha1("GOLD:Engineered > WWTP > A/O treatment system")[:10]`.

The maintained owner of the current identity decision is `curation/decisions.tsv:739`, an item-level `NOT_APPLICABLE` decision for `habitatmech:GOLD.7c91485eb8`. `data/raw/gold_ecosystem_paths.tsv:1383` is the raw GOLD inventory row for the source path, label, and node id.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/engineered/a_o_treatment_system.yaml` | Passed; LinkML validation reported no issues. |
| `just validate-strict data/habitats/engineered/a_o_treatment_system.yaml` | Passed; one file scanned with 0 error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; expected 3206 generated records, found 3206, with 0 missing, 0 extra, and 0 differing. |
| `git diff --check` | Passed; no whitespace errors. |

## Identity and Grounding

`data/raw/gold_ecosystem_paths.tsv:1383` supports the generated source identity:

| Raw field | Value |
|---|---|
| `canonical_path` | `Engineered > WWTP > A/O treatment system` |
| `leaf_label` | `A/O treatment system` |
| `path_depth` | `3` |
| `gold_node_count` | `1` |
| `organism_count` | `0` |
| `metagenome_count` | `0` |
| `biosample_count` | `0` |
| `total_assertions` | `0` |
| `gold_node_ids` | `gold.ecosystem:8223` |

The `REVIEWED` mapping status is mechanically consistent with the maintained item-level decision in `curation/decisions.tsv:739`. The generated curation history also reflects that `NOT_APPLICABLE` decision plus the `seed_from_sources` event.

The grounding itself is internally inconsistent with the hierarchy emitted into the generated record. The schema describes `grounding_status: NOT_APPLICABLE` as a source concept that is not a habitat, so grounding it as one would be wrong. The same schema describes `parent_habitats` as broader habitats. This generated record still asserts `parent_habitats: [ENVO:00002043]`, making `A/O treatment system` narrower than `wastewater treatment plant` after accepting an item-level decision that says `A/O treatment system` is not a habitat.

The asserted ENVO parent is not a spurious identifier: `data/raw/ontology_terms.tsv:7188` confirms `ENVO:00002043` as `wastewater treatment plant`, `data/raw/ontology_subclass_edges.tsv:5290` places that class under `ENVO:00002272`, `data/raw/gold_ecosystem_paths.tsv:575` records `Engineered > WWTP`, and `curation/decisions.tsv:1336` grounds the GOLD WWTP source concept `habitatmech:GOLD.f1d23444f9` to `ENVO:00002043` with `EXACT`. The defect is that a non-habitat source concept keeps a broader-habitat edge, not that `ENVO:00002043` is an unsupported wastewater-treatment-plant class.

## Evidence

| Claim | Nearest support | Review |
|---|---|---|
| The generated record represents GOLD node `gold.ecosystem:8223` at `Engineered > WWTP > A/O treatment system`. | `data/raw/gold_ecosystem_paths.tsv:1383` | Supported. The canonical path, leaf label, node count, and node id match the `source_attestations` entry. |
| `A/O treatment system` has no direct GOLD organism, metagenome, biosample, or total assertions. | `data/raw/gold_ecosystem_paths.tsv:1383` | Supported. The four assertion-count fields are zero, so the generated `source_attestations` entry correctly omits `assertion_count` and `assertion_unit`. |
| The source concept has an item-level review. | `curation/decisions.tsv:739` | Supported. The row is scoped to `ITEM`, so generated `mapping_status: REVIEWED` is expected. |
| The source concept is `NOT_APPLICABLE`. | `curation/decisions.tsv:739` | Mechanically supported, but the maintained rationale is the future curation owner. The decision's note classifies the GOLD path as non-habitat; the generated record should not also represent the same path as a child habitat of `ENVO:00002043`. |
| `ENVO:00002043` is `wastewater treatment plant`. | `data/raw/ontology_terms.tsv:7188`; `curation/decisions.tsv:1336` | Supported. The ontology slice and the GOLD WWTP decision agree on the target label. |
| `ENVO:00002043` is a broader habitat for this `NOT_APPLICABLE` record. | `data/habitats/engineered/a_o_treatment_system.yaml`; `src/habitatmech/schema/habitatmech.yaml`; `curation/decisions.tsv:739` | Unsupported. `parent_habitats` has habitat semantics; the maintained decision says this source concept is not a habitat. |

Unsupported or over-scoped claims: the only unsupported claim in the record is the `parent_habitats` edge from the `NOT_APPLICABLE` `A/O treatment system` record to `ENVO:00002043`.

## Completeness

No required source attestation is missing for the direct GOLD source row: the generated record carries the source name, first and only source id, label, and canonical source path, and it correctly omits direct assertion counts because the raw GOLD row has zero organism, metagenome, biosample, and total assertions.

No maintained causal overlay, history file, or raw research report was found by filename for `a_o_treatment_system` under `curation/causal_graphs`, `history`, `research`, or `reports/yaml_record_review`; the `find` search included ignored files beneath those checked directories. That absence is acceptable for this zero-assertion, `NOT_APPLICABLE` GOLD source record.

The completeness gap is in inherited hierarchy generation. `ingest_gold()` first stores every GOLD path's resolved identifier and then links each source path to the next level up, without checking whether that parent path or child path resolved to a `NOT_APPLICABLE` concept. `build_document()` then serializes every stored parent except the record's own identifier. As a result, the current `NOT_APPLICABLE` record still receives `ENVO:00002043`, and child paths can still inherit this `NOT_APPLICABLE` node as a parent.

`data/raw/gold_ecosystem_paths.tsv:1384`, `data/raw/gold_ecosystem_paths.tsv:1385`, `data/raw/gold_ecosystem_paths.tsv:1386`, and `data/raw/gold_ecosystem_paths.tsv:1387` show the raw GOLD descendants beneath `A/O treatment system`. The previously merged `reports/yaml_record_review/20260922T183921Z-a_o_bioreactor.md` already documents one concrete downstream symptom: `A/O bioreactor` points at this non-habitat `habitatmech:GOLD.7c91485eb8` parent.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | `a_o_treatment_system.yaml` is generated as `NOT_APPLICABLE` but still asserts a broader-habitat edge to `ENVO:00002043`. A record whose source concept is maintained as non-habitat should not itself be emitted as a narrower habitat of wastewater treatment plant. | The reviewed record contains `grounding_status: NOT_APPLICABLE` plus `parent_habitats: [ENVO:00002043]`; `curation/decisions.tsv:739` is the item-level `NOT_APPLICABLE` owner for the source concept; `src/habitatmech/schema/habitatmech.yaml` defines `NOT_APPLICABLE` as a source concept that is not a habitat and `parent_habitats` as broader habitats. | Revisit `curation/decisions.tsv:739`; if the decision remains `NOT_APPLICABLE`, update the GOLD hierarchy logic in `src/habitatmech/seed.py`. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Revisit `curation/decisions.tsv:739` for `habitatmech:GOLD.7c91485eb8`.
   If `A/O treatment system` is a real engineered habitat with no exact ontology term, replace the `NOT_APPLICABLE` row with an item-level `CONFIRM_UNGROUNDED` decision and reasoning scoped to the source path `Engineered > WWTP > A/O treatment system`.
2. If `A/O treatment system` is intentionally non-habitat, update `src/habitatmech/seed.py` so generated `NOT_APPLICABLE` records do not emit `parent_habitats` and GOLD descendants skip `NOT_APPLICABLE` path segments when choosing their nearest valid generated ancestor.
3. Regenerate the corpus so `data/habitats/engineered/a_o_treatment_system.yaml`, `data/habitats/engineered/a_o_bioreactor.yaml`, `data/habitats/engineered/settling_tank__54e3a311.yaml`, and any lower descendants under `Engineered > WWTP > A/O treatment system` all reflect the revisited decision.

## Follow-up Checks

- `just seed-canary habitatmech:GOLD.7c91485eb8`
- `just verify-corpus --max-diffs 1`
- `just validate data/habitats/engineered/a_o_treatment_system.yaml`
- `just validate data/habitats/engineered/a_o_bioreactor.yaml`
- `just validate data/habitats/engineered/settling_tank__54e3a311.yaml`
- Exact ignored/hidden-inclusive searches for `habitatmech:GOLD.7c91485eb8` and `Engineered > WWTP > A/O treatment system` across `curation`, `data/raw`, and `data/habitats`, excluding generated text maps and pages, to verify that no generated record still names a `NOT_APPLICABLE` parent.

## Additional Notes

- The pre-report exact filename check `find reports/yaml_record_review -maxdepth 1 -name '*a_o_treatment_system*' -print` returned no previous exact report.
- Exact ignored/hidden-inclusive content searches for `habitatmech:GOLD.7c91485eb8`, `gold.ecosystem:8223`, `Engineered > WWTP > A/O treatment system`, `ENVO:00002043`, and `habitatmech:GOLD.f1d23444f9` found the generated target, raw GOLD rows, generated descendant records, path lock, parent WWTP decision, ontology rows, and generated `wastewater_treatment_plant` record cited above.
- Generated `data/habitats/PATHS.tsv:2208` maps `habitatmech:GOLD.7c91485eb8` to the expected stem `a_o_treatment_system`.
