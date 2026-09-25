# YAML Record Review

- Repository: HabitatMech
- Record: `data/habitats/engineered/high_salinity_high_ph.yaml`
- Started UTC: 2026-09-25T20:56:10Z
- Finished UTC: 2026-09-25T20:56:20Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Identifier | `habitatmech:GOLD.7038eb7dcc` |
| Label | `High-salinity/high-pH` |
| Class | `HabitatRecord` |
| Category | `ENGINEERED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Source concept | GOLD `Engineered > Bioreactor > High-salinity/high-pH` |
| Maintained owner | Generated from `data/raw/gold_ecosystem_paths.tsv`, `data/habitats/PATHS.tsv`, and `curation/decisions.tsv`; the YAML record is read-only |
| Locked slug | `data/habitats/PATHS.tsv:2120` maps `habitatmech:GOLD.7038eb7dcc` to `high_salinity_high_ph` |

The generated record denotes the collapsed GOLD depth-3 node
`Engineered > Bioreactor > High-salinity/high-pH`.
`data/raw/gold_ecosystem_paths.tsv:1188` lists leaf label
`High-salinity/high-pH`, depth `3`, no direct organism, study, biosample, or
total assertions in the KGX-derived aggregate row, and three GOLD node ids:
`gold.ecosystem:7798`, `gold.ecosystem:7799`, and `gold.ecosystem:7800`.

`data/habitats/engineered/high_salinity_high_ph.yaml:1-13` preserves that
source identity with `identifier: habitatmech:GOLD.7038eb7dcc`, the source
label, source path, first collapsed source id `gold.ecosystem:7798`, and a note
that the other two node ids share this path.

## Validation

| Command | Result |
| --- | --- |
| `just validate data/habitats/engineered/high_salinity_high_ph.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/engineered/high_salinity_high_ph.yaml` | Passed; 1 file scanned, 0 files with errors, 0 total error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; `curation/term_requests.tsv` is current for 109 generated terms. |
| `just validate-history` | Passed; 77 history records were valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; expected and found 3206 records, with 0 missing, 0 extra, and 0 differing files. |
| `just worklist --limit 0 --status all --out /tmp/habitatmech-high-salinity-worklist.tsv` | Passed; wrote 953 ungrounded rows and ranked `habitatmech:GOLD.7038eb7dcc` at row 601 with no lexical candidate term. |
| `just report` | Passed; the corpus report completed and kept the class-level sweep separate from individually examined term requests. |

No validator was skipped.

## Identity and Grounding

`data/raw/gold_ecosystem_paths.tsv:1188` supports the generated GOLD identity
exactly. The raw row is for `Engineered > Bioreactor > High-salinity/high-pH`,
has leaf label `High-salinity/high-pH`, and collapses source nodes
`gold.ecosystem:7798`, `gold.ecosystem:7799`, and `gold.ecosystem:7800`.
The generated source attestation at
`data/habitats/engineered/high_salinity_high_ph.yaml:8-13` repeats the first
source node and the exact path, with the expected note pointing back to
`data/raw/gold_ecosystem_paths.tsv` for the remaining node ids.

The only maintained grounding decision is still a lexical class sweep.
`curation/decisions.tsv:671` records `CONFIRM_UNGROUNDED` with no object term,
no object label, no relation, and `review_depth` `CLASS`. The note says no term
in the vendored ontology slice matched by the class-level search routes, and it
explicitly says the sweep did not assess whether the source concept is a
habitat.

The `ENVO:00002123` `bioreactor` parent is traceable to the source hierarchy's
`Engineered > Bioreactor` parent path, but it has not been item-reviewed as the
true genus of a high-salinity/high-pH bioreactor habitat. Ignored/hidden-
inclusive searches of `data/raw/ontology_terms.tsv` for spelling variants and
nearby concepts found generic and adjacent terms, including `ENVO:00002123`
`bioreactor`, `ENVO:01000316` `alkaline environment`, and `ENVO:01001043`
`hypersaline water environment`, but no exact term for a combined high-salinity
and high-pH bioreactor habitat.

## Evidence

| Claim | Evidence | Status |
| --- | --- | --- |
| The record denotes the GOLD path `Engineered > Bioreactor > High-salinity/high-pH`. | `data/raw/gold_ecosystem_paths.tsv:1188` lists that canonical path, leaf label `High-salinity/high-pH`, and node ids `gold.ecosystem:7798|gold.ecosystem:7799|gold.ecosystem:7800`; `data/habitats/engineered/high_salinity_high_ph.yaml:8-13` repeats the first source node and the path. | Supported exactly. |
| The KGX-derived GOLD path row has no direct organism assertions. | `data/raw/gold_ecosystem_paths.tsv:1188` reports `organism_count` 0, `study_count` 0, `biosample_count` 0, and `total_assertions` 0. | Supported exactly; the generated source attestation correspondingly omits `assertion_count` and `assertion_unit`. |
| Supplemental GOLD side inventories contain sparse support for the same path. | `data/raw/gold_path_biosamples.tsv:935` records one biosample for node `7800`, and `data/raw/gold_studies.tsv:2974` lists the exact source path in study `Gs0145714`. | Supported exactly as side-table context; these inventories are not materialized into the generated source attestation. |
| The committed GOLD MIxS-triad side table has no direct row for this path. | An ignored/hidden-inclusive exact search for `Engineered > Bioreactor > High-salinity/high-pH` found no row in `data/raw/gold_path_triads.tsv`. | Supported for the current raw table. |
| No causal overlay is attached to this record. | An ignored/hidden-inclusive search over `curation/causal_graphs` found no `identifier: habitatmech:GOLD.7038eb7dcc`, and `find curation/causal_graphs -maxdepth 1 -type f -name 'high_salinity_high_ph.yaml' -print` returned no files. | Supported exactly. |

## Completeness

The record is complete for the currently generated source state but incomplete
as curation. It has the exact GOLD source path, a locked slug, one generated
`ENVO:00002123` parent, one class-level `CONFIRM_UNGROUNDED` decision, no
definition, no synonyms, no xrefs, no direct organism assertion count, no
environmental parameters, no characteristic taxa, no causal graph, no
discussion, and no dataset.

Ignored/hidden-inclusive exact searches covered `curation`, `history`,
`research`, `reports/yaml_record_review`, `conf/id_label_targets.yaml`,
`data/habitats/PATHS.tsv`,
`data/habitats/engineered/high_salinity_high_ph.yaml`,
`data/raw/gold_ecosystem_paths.tsv`, `data/raw/gold_path_biosamples.tsv`,
`data/raw/gold_studies.tsv`, `data/raw/gold_path_triads.tsv`, and
`data/raw/ontology_terms.tsv`. They found the generated target, the locked
slug, the source inventory row, one biosample side-table row, one study
side-table row, the `curation/decisions.tsv` class-level row, and no
target-specific term request, excluded term-request row, history record,
committed research report, causal overlay, direct MIxS-triad row, or
pre-existing `*-high_salinity_high_ph.md` review report.

The exact path has sparse side-table use in GOLD, so the source concept is not
an entirely unattested source folder. That evidence is still too thin to decide
whether `High-salinity/high-pH` should be modeled as a habitat, an operating
condition on a bioreactor, or an informal source bucket without an item-level
review of the study, biosample, and any underlying metadata.

## Findings

| ID | Severity | Finding | Maintained owner |
| --- | --- | --- | --- |
| HM-HIGHSALPH-001 | Major | `High-salinity/high-pH` remains at `review_depth` `CLASS`. The only maintained decision at `curation/decisions.tsv:671` explicitly did not assess habitathood, while the exact path has one committed GOLD biosample and one GOLD study in the side inventories. No item-level curation has decided whether this is a true combined saline/alkaline bioreactor habitat that should remain minted and hang under `ENVO:00002123`, a combination of physicochemical qualities that should be modeled elsewhere, or a non-habitat source bucket. | `curation/decisions.tsv`; if the concept stays minted, add a definition and authored hierarchy in `curation/term_requests.tsv`. |

## Recommended Edits

1. Reopen `habitatmech:GOLD.7038eb7dcc` in `curation/decisions.tsv` with
   `review_depth` `ITEM`; inspect GOLD study `Gs0145714`, node `7800`, and any
   underlying biosample metadata to decide whether
   `Engineered > Bioreactor > High-salinity/high-pH` denotes a real microbial
   habitat or only an operating-condition bucket.
2. If the concept is a real habitat with no exact ontology identity, keep it
   minted with `CONFIRM_UNGROUNDED`, add an evidence-backed
   `curation/term_requests.tsv` definition, and keep `ENVO:00002123` only if
   item-level review confirms that `bioreactor` is a strict broader parent.
3. If the source concept is only a quality conjunction rather than a habitat,
   mark it `NOT_APPLICABLE` and rerun seeding so the generated record is
   retired instead of promoted as a term-request candidate.

## Follow-up Checks

- `rg --no-ignore --hidden -n 'habitatmech:GOLD\.7038eb7dcc|Engineered > Bioreactor > High-salinity/high-pH|gold\.ecosystem:(7798|7799|7800)' curation/decisions.tsv curation/term_requests.tsv history research data/habitats/engineered`
- `just seed`
- `just seed-canary habitatmech:GOLD.7038eb7dcc`
- `just seed-apply --force`
- `just validate data/habitats/engineered/high_salinity_high_ph.yaml`
- `just validate-strict data/habitats/engineered/high_salinity_high_ph.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just report`

## Additional Notes

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*high_salinity_high_ph.md' -print` found no pre-existing exact review report before this file was written; `find` included ignored files under the searched directory.
- `find curation/causal_graphs -maxdepth 1 -type f -name 'high_salinity_high_ph.yaml' -print` found no slug-matched causal overlay before this report was written; `find` included ignored files under the searched directory.
- A repository-root `find . -maxdepth 3 -name AGENTS.md -print` found no local `AGENTS.md` files before this report was written; `find` included ignored files under the searched tree.
