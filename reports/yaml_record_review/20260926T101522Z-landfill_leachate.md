# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/landfill_leachate.yaml
- Started UTC: 2026-09-26T10:15:22Z
- Finished UTC: 2026-09-26T10:15:22Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.4020b8821e` |
| Label | `Landfill leachate` |
| Class | `HabitatRecord` |
| Category | `ENGINEERED` |
| Generated path | `data/habitats/engineered/landfill_leachate.yaml` |
| Maintained path lock | `data/habitats/PATHS.tsv:1773` maps `habitatmech:GOLD.4020b8821e` to `landfill_leachate` |
| Source concept | GOLD `gold.ecosystem:3838` and `gold.ecosystem:4269` |
| Source path | `Engineered > Wastewater > Industrial wastewater > Landfill leachate` |
| Grounding | `UNGROUNDED` |
| Mapping | `SEEDED` |

The reviewed file is generated from the GOLD source inventory and a
class-level curation decision. It should not be patched directly.

## Validation

| Command | Result |
|---|---|
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist.tsv` | Passed; wrote 953 rows and placed `habitatmech:GOLD.4020b8821e` immediately after the already reviewed `Hadopelagic zone/Ocean trenches`. |
| `just validate data/habitats/engineered/landfill_leachate.yaml` | Passed with `No issues found`. |
| `just validate-strict data/habitats/engineered/landfill_leachate.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; 3206 expected records, 3206 found, 0 missing, 0 extra, 0 differing. |
| `just report` | Passed; no stale class-level sweep, contradictory path term, or non-habitat label contradiction was reported for this record. |
| `git diff --check` | Passed before this report was written. |

## Identity and Grounding

The generated identifier, label, category, source attestation, and assertion
count agree with the GOLD source inventory:

| Claim | Evidence | Assessment |
|---|---|---|
| The target is the collapsed GOLD `Landfill leachate` path. | `data/raw/gold_ecosystem_paths.tsv:667` records `Engineered > Wastewater > Industrial wastewater > Landfill leachate` with leaf label `Landfill leachate`, depth 4, two GOLD nodes, four organism assertions, and source IDs `gold.ecosystem:3838|gold.ecosystem:4269`. | Supported exactly. |
| The generated `source_attestations` block preserves the representative raw source ID, path, count, and unit. | The generated YAML carries `source: GOLD`, `source_id: gold.ecosystem:3838`, the same full source path, `assertion_count: 4`, `assertion_unit: ORGANISM`, and a note that two GOLD ecosystem node IDs share the path. | Supported exactly. |
| The generated `ENGINEERED` category agrees with GOLD's top-level path. | The source path begins with `Engineered`, and the target file has `habitat_category: ENGINEERED`. | Supported exactly. |
| The generated `ENVO:01000964` parent is inherited from the immediate GOLD `Industrial wastewater` path parent. | The target source path's parent is `Engineered > Wastewater > Industrial wastewater`; the generated parent record `data/habitats/engineered/industrial_wastewater.yaml` grounds that GOLD parent to `ENVO:01000964` `industrial wastewater`. | Supported as source-path context and plausible as a broader wastewater class, but not item-reviewed for this leaf. |
| `Landfill leachate` is not the same concept as `ENVO:00000533` `landfill`. | `ENVO:00000533` defines a landfill as a depression containing discarded objects and materials, while `ENVO:00002141` defines `leachate` as a liquid produced when water percolates through any permeable material. | Supported. The target label names a material generated from a landfill, not the landfill site itself. |
| `UNGROUNDED` is currently explained only by a class-level no-match sweep. | `curation/decisions.tsv:440` has `CONFIRM_UNGROUNDED` with `review_depth` `CLASS`; the generated curation history repeats that no ontology term fit by any lexical route and that habitat status was not assessed. | Reproducible but incomplete. `CLASS` depth does not establish that the leaf denotes a habitat, that no exact term fits, or which strictly broader material parent should be requested. |

A bounded hidden/ignored-inclusive search of `data/raw/`, `curation/`,
`history/`, `research/`, `reports/yaml_record_review/`, `data/habitats/`, and
`pages/habitats/` for `habitatmech:GOLD.4020b8821e`,
`gold.ecosystem:3838`, `gold.ecosystem:4269`, `landfill_leachate`,
`Landfill leachate`, and the exact source path found the expected generated
record, page, path lock, raw GOLD aggregate row, and class-level decision row.
It found no target-specific term request, generated term-request row, causal
overlay, append-only history entry, deep-research report, or prior exact YAML
review for this target.

## Evidence

| Record claim | Nearest source | Assessment |
|---|---|---|
| `source: GOLD`, `source_id: gold.ecosystem:3838`, `source_label: Landfill leachate`, and the full source path | `data/raw/gold_ecosystem_paths.tsv:667` | Supported exactly. |
| The note that two GOLD ecosystem node IDs share this path | `data/raw/gold_ecosystem_paths.tsv:667` lists `gold.ecosystem:3838|gold.ecosystem:4269`. | Supported exactly. |
| `assertion_count: 4`, `assertion_unit: ORGANISM` | `data/raw/gold_ecosystem_paths.tsv:667` has `organism_count=4`, `study_count=0`, `biosample_count=0`, and `total_assertions=4`. | Supported; the count is a GOLD `ORGANISM` aggregate and is not study or biosample evidence. |
| Parent `ENVO:01000964` | GOLD places the source concept under `Engineered > Wastewater > Industrial wastewater`; the generated record for that immediate path is `ENVO:01000964` `industrial wastewater`. | Supported as generated source-path inheritance. Item review should confirm whether all landfill leachate should be modeled as industrial wastewater or only as a leachate material from a landfill. |
| Absence of direct GOLD side-table rows | Exact hidden/ignored-inclusive searches of `data/raw/gold_studies.tsv`, `data/raw/gold_path_biosamples.tsv`, and `data/raw/gold_path_triads.tsv` found no row for the target source path or its two GOLD node IDs. | Supported. The target's four assertions come only from the aggregate organism count on the collapsed GOLD ecosystem-path row. |
| Absence of characteristic taxa, record evidence, and causal graphs | Exact hidden/ignored-inclusive searches across `data/raw/`, `curation/causal_graphs/`, and the generated YAML found no target-specific taxa or curated overlay, and GOLD path aggregates do not emit inline characteristic-taxon claims. | Supported. |

The vendored ontology slice has useful near terms but no exact
`landfill leachate` identity:

| CURIE | Label | Relationship to the GOLD leaf |
|---|---|---|
| `ENVO:00002141` | `leachate` | Strictly broader material candidate; its definition covers liquids produced when water percolates through any permeable material. |
| `ENVO:01000964` | `industrial wastewater` | Current inherited parent from GOLD's `Industrial wastewater` path. It is broader if landfill leachate is wastewater produced by industrial activity. |
| `ENVO:00000533` | `landfill` | Related generator or site, not a broader material identity for the leachate itself. |

The nearby generated records keep these concepts separate. `ENVO:00000533`
`landfill` is the exact GOLD/PREGO landfill site record;
`habitatmech:GOLD.de8a7c8184` is a GOLD soil-under-landfill record with
`ENVO:00000533` and `ENVO:00001998` parents; and the target `Landfill leachate`
record remains a separate material-like path.

## Completeness

The generated record preserves the raw GOLD aggregate row and class-level
curation decision and correctly avoids unsupported characteristic taxa,
environmental parameters, evidence items, and causal graph claims.

It is incomplete as an item-reviewed habitat. The only maintained decision is a
class-level no-match sweep that did not assess whether the source concept is a
habitat. The exact GOLD path has no committed study, biosample, or MIxS triad
side rows that could distinguish a landfill-specific leachate material, an
industrial-wastewater subtype, or a landfill site. No committed term request
defines the target under `ENVO:00002141` `leachate` or explains whether to keep
the generated `industrial wastewater` parent.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| HM-LANDFILL-LEACHATE-001 | Major | `Landfill leachate` is still backed only by `review_depth` `CLASS`. The generated `UNGROUNDED` and `SEEDED` statuses are reproducible, but the maintained row explicitly says no one assessed whether the source concept is a habitat. The label is material-like and narrower than the existing `ENVO:00002141` `leachate`, so it needs item review before HabitatMech treats it as a true novel habitat. | `curation/decisions.tsv`; if the record is a real habitat, `curation/term_requests.tsv` |
| HM-LANDFILL-LEACHATE-002 | Major | The record has only `ENVO:01000964` `industrial wastewater` as a parent and lacks a leachate genus. GOLD source-path inheritance explains the current parent, but a future definition should record whether landfill leachate is strictly an industrial wastewater or instead a landfill-derived leachate that should inherit from `ENVO:00002141` `leachate` with source hierarchy replaced or augmented. | `curation/term_requests.tsv`, regenerated `data/habitats/engineered/landfill_leachate.yaml` |

## Recommended Edits

1. Item-review `habitatmech:GOLD.4020b8821e` in
   `curation/decisions.tsv`, replacing the class-level row with an item-level
   decision.
2. Inspect GOLD nodes `gold.ecosystem:3838` and `gold.ecosystem:4269`,
   including the four organism assertions behind the aggregate row, to confirm
   whether GOLD is using this path for leachate liquid from landfills rather
   than a landfill site or a generic industrial wastewater sample.
3. If the GOLD concept is the landfill-specific liquid material, retain a
   minted `CONFIRM_UNGROUNDED` decision at item depth and add a
   `curation/term_requests.tsv` definition under `ENVO:00002141` `leachate`.
4. Set the term request's parent mode deliberately: use `ADD` if the
   `industrial wastewater` source-path parent is strictly true for the target,
   and `REPLACE` only if item review establishes that the GOLD parent is a
   contextual bin rather than a strict `is_a`.
5. If the GOLD source concept is a landfill site, ground or merge it toward the
   existing `ENVO:00000533` `landfill` record instead of defining a novel
   leachate material.

Do not hand-edit `data/habitats/engineered/landfill_leachate.yaml`;
regenerate it from maintained TSVs after curation changes.

## Follow-up Checks

After adding item-level curation, rerun:

- `just seed`
- `just seed-canary habitatmech:GOLD.4020b8821e`
- inspect `data/habitats/engineered/landfill_leachate.yaml`
- `just validate-strict data/habitats/engineered/landfill_leachate.yaml`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just report`

If a causal overlay is added later, also run
`just validate-causal curation/causal_graphs/landfill_leachate.yaml` and
`just validate-causal-all`.

## Additional Notes

None.
