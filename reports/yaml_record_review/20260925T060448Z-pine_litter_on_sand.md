# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/pine_litter_on_sand.yaml
- Started UTC: 2026-09-25T06:01:40Z
- Finished UTC: 2026-09-25T06:04:48Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| LinkML class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.1d6e2dd200` |
| Label | `Pine litter on sand` |
| File | `data/habitats/engineered/pine_litter_on_sand.yaml` |
| Category | `ENGINEERED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Generated or maintained | Generated from `data/raw/` inventories by `scripts/seed_from_sources.py` |

The record is the GOLD path `Engineered > Artificial ecosystem >
Nutrient-poor > Pine litter on sand`. Its source row is
`data/raw/gold_ecosystem_paths.tsv:1140`, a depth-4 row with leaf label
`Pine litter on sand`, two collapsed GOLD ecosystem node IDs
`gold.ecosystem:6282|gold.ecosystem:6283`, and zero organism, study,
biosample, and total assertion counts in the core kg-microbe inventory.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/engineered/pine_litter_on_sand.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/engineered/pine_litter_on_sand.yaml` | Passed; 1 file scanned, 0 files with errors, 0 total error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the term-request table is current for 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against the vendored history schema. |
| `just verify-corpus --max-diffs 1` | Passed; expected 3206 records, found 3206, with 0 missing, 0 extra, and 0 differing records. |
| `just worklist --limit 2000` | Passed; 0 ungrounded records remain undecided, with 1810 decisions on file. |
| `just report` | Passed; rebuilt the corpus report over 3206 records. |

No validator was skipped.

## Identity and Grounding

- The record's minted identifier `habitatmech:GOLD.1d6e2dd200` is a generated,
  content-hashed GOLD identifier and is pinned to slug `pine_litter_on_sand`
  in `data/habitats/PATHS.tsv:1500`.
- The only upstream attestation is GOLD, with `source_id:
  gold.ecosystem:6282`, `source_label: Pine litter on sand`, and
  `source_path: Engineered > Artificial ecosystem > Nutrient-poor > Pine
  litter on sand`. This agrees with `data/raw/gold_ecosystem_paths.tsv:1140`.
- The attestation note is consistent with the raw source row: two GOLD node
  IDs collapse to the same canonical path, and `src/habitatmech/seed.py`
  intentionally records the first ID and points back to
  `data/raw/gold_ecosystem_paths.tsv` rather than emitting the full ID list.
- `grounding_status: UNGROUNDED` is traceable to the maintained class-level
  decision in `curation/decisions.tsv:261`. That row confirms that no term in
  the vendored slice matched this label by any search route, but does not
  promote the source concept to a term request or to item-level review.
- `mapping_status: SEEDED` is therefore consistent with the `CLASS`
  `review_depth` of the only decision row for `habitatmech:GOLD.1d6e2dd200`.
- The parent `habitatmech:GOLD.06fb1f0fdd` is the generated record for the
  next broader source path `Engineered > Artificial ecosystem > Nutrient-poor`,
  so the hierarchy preserves GOLD's source-path structure.

## Evidence

- The record has no curator-authored `evidence` entries, causal graphs,
  environmental parameters, characteristic taxa, discussions, or datasets.
- No claim-level literature evidence is required for the generated GOLD source
  attestation itself. The attestation is backed by the committed raw GOLD path
  row.
- The supplemental GOLD biosample inventory records 173 biosamples for
  `Engineered > Artificial ecosystem > Nutrient-poor > Pine litter on sand`
  at `data/raw/gold_path_biosamples.tsv:156`, and the supplemental GOLD study
  inventory lists one study containing this path at
  `data/raw/gold_studies.tsv:4065`.
- An ignored-inclusive exact search of `data/raw/gold_path_triads.tsv` for
  `Engineered > Artificial ecosystem > Nutrient-poor > Pine litter on sand`
  found no matching MIxS triad rows that should be considered as
  environmental-parameter curation leads for this generated record.

## Completeness

- The empty optional slots are acceptable for this generated GOLD path. The
  core GOLD inventory has no organism assertions for the path, and
  `src/habitatmech/seed.py` currently emits GOLD `assertion_count` only from
  the nonzero `organism_count` in `data/raw/gold_ecosystem_paths.tsv`.
- Ignored-inclusive exact searches of `data/raw`, `curation`, `history`, and
  `research` for `habitatmech:GOLD.1d6e2dd200`, `gold.ecosystem:6282`,
  `gold.ecosystem:6283`, `pine_litter_on_sand`, and
  `Pine litter on sand` found only the maintained class-level decision row,
  the PATHS slug row, the raw GOLD ecosystem row, one supplemental biosample
  row, and one supplemental study row before this report was added.
- `find curation/causal_graphs -name '*pine*'` found no causal overlay for
  this record; `find` included gitignored entries below `curation/causal_graphs`.
- `find reports/yaml_record_review -name '*pine_litter_on_sand.md'` found no
  prior review report for this record; `find` included gitignored entries
  below `reports/yaml_record_review`.

## Findings

None found.

## Recommended Edits

None found.

## Follow-up Checks

None found.

## Additional Notes

- The supplemental GOLD biosample and study inventories are used to decide
  which GOLD study IDs are worth querying for API-only MIxS triads. This path
  has no committed exact row in `data/raw/gold_path_triads.tsv`, so there is
  no exact triad evidence for this review to assess.
- The broader `Nutrient-poor` parent record is still a seeded class-level
  term-request concept, but that upstream review gap does not make this
  generated child internally inconsistent.
