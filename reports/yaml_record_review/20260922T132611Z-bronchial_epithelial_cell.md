# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/bronchial_epithelial_cell.yaml`
- Started UTC: 2026-09-22T13:26:11Z
- Finished UTC: 2026-09-22T13:26:11Z
- Verdict: pass with minor issues

## Target

| Field | Value |
|---|---|
| Identifier | `BTO:0002922` |
| Label | `bronchial epithelial cell` |
| Class | `HabitatRecord` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `EXACT` |
| Mapping status | `REVIEWED` |
| Maintained owner | `curation/decisions.tsv:605` grounds the GOLD source concept to `BTO:0002922` |
| Locked slug | `data/habitats/PATHS.tsv:351` maps `BTO:0002922` to `bronchial_epithelial_cell` |

This is the reviewed exact record for the GOLD path `Host-associated > Mammals: Human > Respiratory system > Bronchi > Bronchial epithelial cells`. The generated YAML correctly adopts `BTO:0002922` because the item-level decision grounds the minted GOLD source concept to `bronchial epithelial cell` with `EXACT` status. The record's only correctness issue is limited to human-readable provenance text: the `curation/decisions.tsv` note truncates the final source-path token from `Bronchial epithelial cells` to `Bronchial epithelial cel`, and that typo is faithfully carried into generated `curation_history`.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/bronchial_epithelial_cell.yaml` | Pass; `linkml-validate` reported `No issues found` |
| `just validate-strict data/habitats/host_associated/bronchial_epithelial_cell.yaml` | Pass; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate-causal-all` | Pass; 32 causal-graph curation files with 32 graphs validated |
| `just term-requests-check` | Pass; term-request table is current with 109 terms |
| `just validate-history` | Pass; 77 history records are valid against `src/habitatmech/schema/history.yaml` |
| `just verify-corpus --max-diffs 1` | Pass; expected 3206 records, found 3206, with 0 missing, 0 extra, 0 differing |
| `git diff --check` | Pass; no whitespace or patch errors after this report was written |

## Identity and Grounding

The generated BTO identity, GOLD source attestation, exact mapping predicate, host-associated category, and path lock are supported by maintained inputs:

- `data/raw/gold_ecosystem_paths.tsv:2418` is the raw GOLD row for this source concept. Its canonical path is `Host-associated > Mammals: Human > Respiratory system > Bronchi > Bronchial epithelial cells`; its leaf label is `Bronchial epithelial cells`; it is a depth-5 path with one GOLD node id, `gold.ecosystem:6627`, and zero organism, study, biosample, or literature assertions.
- `curation/decisions.tsv:605` is an item-level `GROUND` decision for `habitatmech:GOLD.62f0ba9899`, grounding that exact GOLD path to `BTO:0002922` `bronchial epithelial cell` with `EXACT` status.
- `data/raw/ontology_terms.tsv:2922` provides `BTO:0002922` `bronchial epithelial cell`, with definition `A normal cell of the bronchial epithelium.`; `data/habitats/PATHS.tsv:351` pins that ontology record to `bronchial_epithelial_cell`.
- The decision note is copied verbatim into the generated `GROUND` history event, including the truncated final source-path word `cel`.
- The raw source path's parent is the GOLD path `Host-associated > Mammals: Human > Respiratory system > Bronchi`; that parent mints to `habitatmech:GOLD.67ad6b3f36` and is still preserved as the generated parent of this reviewed BTO record.

The exact identity is defensible: the GOLD leaf is the plural form of the BTO class label, the decision is item-scoped, and no other source concept resolves into `BTO:0002922` in the generated corpus.

## Evidence

Every generated claim in this record is source-derived or curated:

| Claim | Nearest source | Review |
|---|---|---|
| Identifier `BTO:0002922`, label `bronchial epithelial cell`, definition, and `EXACT` status | `curation/decisions.tsv:605`, `data/raw/ontology_terms.tsv:2922` | Supported exactly |
| `mapping_status: REVIEWED` | `curation/decisions.tsv:605` has `review_depth` `ITEM` | Supported exactly |
| GOLD source id `gold.ecosystem:6627`, source label, source path, and absent assertion count | `data/raw/gold_ecosystem_paths.tsv:2418` | Supported exactly |
| `skos:exactMatch` | `curation/decisions.tsv:605` records `grounding_status` `EXACT` | Supported exactly |
| Parent `habitatmech:GOLD.67ad6b3f36` | GOLD parent-path emission in `src/habitatmech/seed.py`, backed by `data/raw/gold_ecosystem_paths.tsv:570` and `:2418` | Supported exactly |
| Locked filename | `data/habitats/PATHS.tsv:351` | Supported exactly |

The record has no xrefs, environmental parameters, characteristic taxa, record-level evidence, causal graphs, discussion links, or datasets. Those absences are consistent with the single zero-assertion GOLD row that feeds this record and the absence of target-specific side-table, causal-graph, and research entries.

## Completeness

The generated slots are faithful to the maintained inputs that feed this record, aside from the note typo:

- The sole `source_attestations` entry captures the exact child GOLD path and its single GOLD node id.
- The BTO definition and exact synonym from the GOLD source label are complete for the current ontology and source inputs.
- The item-level curation decision is sufficient to make this single-source record `REVIEWED`.
- This GOLD path has no generated child records and no exact rows in `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_studies.tsv`, or `data/raw/gold_path_triads.tsv`.
- The current GOLD parent is valid generated structure. A future item-level decision for `habitatmech:GOLD.67ad6b3f36` should preserve this record under a strictly broader bronchus parent if it retires the minted human `Bronchi` parent.

Ignored/hidden-inclusive exact searches covered `curation`, `history`, `research`, `reports`, `data/raw`, `data/habitats/PATHS.tsv`, and the generated host-associated records, excluding generated `build`, `data/text_map`, and `pages` trees. They found the target raw GOLD row, item-level decision, BTO ontology row, path lock, generated YAML, and the previously added parent `Bronchi` YAML report; they found no target-specific term request, causal overlay, history record, research report, GOLD biosample row, GOLD study row, GOLD triad row, generated child record, or prior exact YAML review report.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Minor | The curated provenance note for `habitatmech:GOLD.62f0ba9899` truncates the source path from `Bronchial epithelial cells` to `Bronchial epithelial cel`, and the generated YAML carries that typo into its `GROUND` history event. This does not change the record identity or validation result, but it makes the published curation explanation point at a non-existent GOLD leaf spelling. | Correct the note text in `curation/decisions.tsv:605`, then regenerate `BTO:0002922`. |

## Recommended Edits

- Correct the `curation/decisions.tsv:605` note from `Bronchial epithelial cel` to `Bronchial epithelial cells`.
- Regenerate the target with `just seed` and preview `BTO:0002922` with `just seed-canary BTO:0002922` before applying the full generated corpus.

## Follow-up Checks

After correcting the maintained decision note, re-run the same focused validation set and confirm the generated `GROUND` history event carries the full `Bronchial epithelial cells` leaf:

- `just validate data/habitats/host_associated/bronchial_epithelial_cell.yaml`
- `just validate-strict data/habitats/host_associated/bronchial_epithelial_cell.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `git diff --check`

## Additional Notes

- `find reports/yaml_record_review -maxdepth 1 -name '*bronchial_epithelial_cell*' -print` found no pre-existing exact review report for this record before this file was written.
- Exact ignored/hidden-inclusive content searches for `habitatmech:GOLD.62f0ba9899`, `Host-associated > Mammals: Human > Respiratory system > Bronchi > Bronchial epithelial cells`, `gold.ecosystem:6627`, and `BTO:0002922` found only the maintained source, decision, ontology, path-lock, generated, and parent-review rows cited above for this target.
