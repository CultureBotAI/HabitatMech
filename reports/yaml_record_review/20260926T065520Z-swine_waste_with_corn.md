# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/swine_waste_with_corn.yaml
- Started UTC: 2026-09-26T06:52:39Z
- Finished UTC: 2026-09-26T06:55:20Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.288559828e` |
| Label | `Swine waste with corn` |
| Class | `HabitatRecord` |
| Category | `ENGINEERED` |
| Generated path | `data/habitats/engineered/swine_waste_with_corn.yaml` |
| Maintained path lock | `data/habitats/PATHS.tsv:1582` maps `habitatmech:GOLD.288559828e` to `swine_waste_with_corn` |
| Source concept | GOLD `gold.ecosystem:6482` / `gold.ecosystem:6483` |
| Source path | `Engineered > Animal feed production > Fermentation > Swine waste with corn` |
| Grounding | `UNGROUNDED` |
| Mapping | `SEEDED` |

The reviewed file is a generated GOLD-only record. It is not a maintained
curation input and should not be patched directly.

## Validation

| Command | Result |
|---|---|
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist.tsv` | Passed; wrote 953 rows and kept `habitatmech:GOLD.288559828e` as the next row after `Soy sauce`. |
| `just validate data/habitats/engineered/swine_waste_with_corn.yaml` | Passed with `No issues found`. |
| `just validate-strict data/habitats/engineered/swine_waste_with_corn.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; 3206 expected records, 3206 found, 0 missing, 0 extra, 0 differing. |
| `just report` | Passed; no stale class-level sweep, contradictory path term, or non-habitat label contradiction was reported for this record. |
| `git diff --check` | Passed before this report was written. |

## Identity and Grounding

The generated identifier, label, category, and source attestation agree with the
GOLD source inventory:

| Claim | Evidence | Assessment |
|---|---|---|
| The target is the GOLD `Swine waste with corn` leaf under animal-feed fermentation. | `data/raw/gold_ecosystem_paths.tsv:626` gives the canonical path `Engineered > Animal feed production > Fermentation > Swine waste with corn`, leaf label `Swine waste with corn`, depth `4`, and `gold.ecosystem:6482|gold.ecosystem:6483`. | Supported. |
| The generated source attestation uses the first collapsed GOLD node ID and records the duplicate-node note. | The same raw row lists two GOLD ecosystem node IDs; `data/habitats/engineered/swine_waste_with_corn.yaml` emits `source_id: gold.ecosystem:6482` and says two GOLD ecosystem node IDs share the path. | Supported. |
| The direct GOLD row has five organism-level assertions. | `data/raw/gold_ecosystem_paths.tsv:626` has `organism_count=5`, `study_count=0`, `biosample_count=0`, and `total_assertions=5`. | Supported; the count is a GOLD `ORGANISM` aggregate and is not study or biosample evidence. |
| The only generated parent is the immediate GOLD source-path parent `Fermentation`. | The target has `parent_habitats: habitatmech:GOLD.79e523eace`; `data/habitats/engineered/fermentation__cbf94220.yaml` is the generated record for `Engineered > Animal feed production > Fermentation`. | Unsupported as a `parent_habitats` edge. That parent has an item-level `NOT_APPLICABLE` decision because it names an animal-feed production process, not the fermenting feed material or vessel. |
| `UNGROUNDED` is currently explained only by a class-level no-match sweep. | `curation/decisions.tsv:317` has `CONFIRM_UNGROUNDED` with `review_depth` `CLASS`; the generated curation history repeats that no ontology term fit by any lexical route and that habitat status was not assessed. | Reproducible but incomplete. `CLASS` depth does not establish that Swine waste with corn is a real microbial habitat or that no manual broader parent or novel term should be attached. |

A bounded ignored/hidden-inclusive search of `data/raw/`, `curation/`,
`history/`, `research/`, `reports/yaml_record_review/`,
`data/habitats/PATHS.tsv`, `data/habitats/engineered/`, and the generated target
page for `habitatmech:GOLD.288559828e`, `gold.ecosystem:6482`,
`gold.ecosystem:6483`, `Swine waste with corn`, `swine_waste_with_corn`,
`swine-waste-with-corn`, and the full GOLD path found the expected generated
record, page, path lock, raw GOLD aggregate row, and class-level decision row.
It found no target-specific term request, term-request exclusion, causal overlay,
append-only history entry, exact-path GOLD biosample or study row, advisory
sample row, or prior YAML review. The search also found one non-target mention
in the BacDive Suidae deep-research report, which only categorized this record
as an engineered waste stream.

## Evidence

| Record claim | Nearest source | Assessment |
|---|---|---|
| `source: GOLD`, `source_id: gold.ecosystem:6482`, `source_label: Swine waste with corn`, and the full GOLD path | `data/raw/gold_ecosystem_paths.tsv:626` | Supported exactly. |
| The two-GOLD-node collapse note | `data/raw/gold_ecosystem_paths.tsv:626` lists `gold.ecosystem:6482|gold.ecosystem:6483`. | Supported exactly. |
| `assertion_count: 5`, `assertion_unit: ORGANISM` | `data/raw/gold_ecosystem_paths.tsv:626` records 5 organism assertions. | Supported exactly. |
| Parent `habitatmech:GOLD.79e523eace` | The GOLD path places `Swine waste with corn` below `Engineered > Animal feed production > Fermentation`; the parent generated record has identifier `habitatmech:GOLD.79e523eace` and an item-level `NOT_APPLICABLE` decision. | Supported as GOLD path containment, but unsupported as a strict broader microbial habitat. |
| Absence of characteristic taxa, environmental parameters, record evidence, and causal graphs | Exact ignored/hidden-inclusive searches across `data/raw/`, `curation/causal_graphs/`, and the generated YAML found no `gold_path_biosamples.tsv`, `gold_path_triads.tsv`, or `gold_studies.tsv` rows for this path and no curated causal overlay. | Supported. GOLD organism aggregates are not characteristic-taxon claims, and no curated causal overlay exists. |

## Completeness

The generated record preserves the one existing raw GOLD aggregate row and the
class-level curation decision, and it correctly avoids unsupported
characteristic taxa, environmental parameters, record evidence, and causal graph
claims. It is incomplete in two curation-relevant ways:

- The class-level decision is not an item review. A curator has not yet
  inspected `gold.ecosystem:6482`, `gold.ecosystem:6483`, or the five organism
  assertions behind the aggregate to decide whether this GOLD leaf denotes a
  habitat, an input waste material, a fermented feed substrate, or a mixed
  upstream bucket.
- The only generated parent is a source-path process already ruled out as
  non-habitat. Because `parent_habitats` means a strict is-a relationship, the
  record currently has no supported broader habitat parent.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| HM-SWINE-WASTE-WITH-CORN-001 | Major | The record inherits `habitatmech:GOLD.79e523eace` `Fermentation` as its only `parent_habitats` value even though that parent has an item-level `NOT_APPLICABLE` decision: `Engineered > Animal feed production > Fermentation` names a production process, not a habitat. GOLD path containment supports the upstream path but not the generated `is-a` claim. | `src/habitatmech/seed.py`, where GOLD parent-path links are added in the second pass of `ingest_gold` |
| HM-SWINE-WASTE-WITH-CORN-002 | Major | `Swine waste with corn` is still backed only by `review_depth` `CLASS`. The maintained row says no vendored ontology term matched lexically and explicitly says no one assessed whether the concept is a habitat, so the generated `UNGROUNDED` and `SEEDED` statuses are reproducible but materially incomplete for a possible feed/waste term-request candidate. | `curation/decisions.tsv`; if a novel term is requested, `curation/term_requests.tsv` |

## Recommended Edits

1. Change GOLD source-path parent generation in `src/habitatmech/seed.py` so a
   child does not receive a `parent_habitats` edge to a concept whose grounding
   status is `NOT_APPLICABLE`.
2. Add a focused regression test for `ingest_gold` proving that a child below a
   `NOT_APPLICABLE` GOLD parent keeps its source attestation but does not claim
   that parent as a broader habitat.
3. Item-review `habitatmech:GOLD.288559828e` in `curation/decisions.tsv`.
4. Inspect GOLD nodes `gold.ecosystem:6482` and `gold.ecosystem:6483`, including
   the five organism assertions behind the aggregate row, to confirm whether the
   leaf denotes a real fermented swine-feed or waste-stream habitat rather than
   a production-process byproduct bucket.
5. If the source concept is a real habitat with no exact ontology term, keep the
   minted identity, replace the class-level row with an item-level
   `CONFIRM_UNGROUNDED`, and consider a novel ENVO term with a strictly broader
   animal-feed or fermentation-material genus.
6. If the GOLD node is instead a non-habitat input or process bucket, replace
   the class-level row with an item-level `NOT_APPLICABLE`.

Do not hand-edit `data/habitats/engineered/swine_waste_with_corn.yaml`;
regenerate it from the maintained Python and TSV inputs.

## Follow-up Checks

After changing GOLD source-path parent generation, rerun:

- `just seed`
- `just validate-strict data/habitats/engineered/swine_waste_with_corn.yaml`
- `just verify-corpus --max-diffs 1`
- `just report`

After adding item-level curation for this source concept, rerun:

- `just seed`
- `just seed-canary habitatmech:GOLD.288559828e`
- inspect `data/habitats/engineered/swine_waste_with_corn.yaml`
- `just validate-strict data/habitats/engineered/swine_waste_with_corn.yaml`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just report`

If a causal overlay is added later, also run
`just validate-causal curation/causal_graphs/swine_waste_with_corn.yaml` and
`just validate-causal-all`.

## Additional Notes

The false-parent problem is broader than this one record because GOLD path
parents are attached after per-source decisions are applied. A later code fix
should measure how many generated records currently point to `NOT_APPLICABLE`
GOLD parents before changing the parent builder, then inspect the resulting
diff by class.
