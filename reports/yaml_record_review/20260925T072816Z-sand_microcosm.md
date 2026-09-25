# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/sand_microcosm.yaml
- Started UTC: 2026-09-25T07:25:05Z
- Finished UTC: 2026-09-25T07:28:25Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| LinkML class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.14789d9032` |
| Label | `Sand microcosm` |
| File | `data/habitats/engineered/sand_microcosm.yaml` |
| Category | `ENGINEERED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Generated or maintained | Generated from `data/raw/` inventories and `curation/decisions.tsv` by `scripts/seed_from_sources.py` |

The record is the GOLD path `Engineered > Artificial ecosystem > Sand microcosm`.
Its source row is `data/raw/gold_ecosystem_paths.tsv:1144`, a depth-3 row with
leaf label `Sand microcosm`, three collapsed GOLD ecosystem node IDs
`gold.ecosystem:5872|gold.ecosystem:5873|gold.ecosystem:5874`, and zero
organism, study, biosample, and total assertion counts in the core kg-microbe
inventory.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/engineered/sand_microcosm.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/engineered/sand_microcosm.yaml` | Passed; 1 file scanned, 0 files with errors, 0 total error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the term-request table is current for 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against the vendored history schema. |
| `just verify-corpus --max-diffs 1` | Passed; expected 3206 records, found 3206, with 0 missing, 0 extra, and 0 differing records. |
| `just worklist --limit 2000 --status all --out /tmp/habitatmech-sand-microcosm-worklist.tsv` | Passed; wrote 953 ungrounded rows and retained `Sand microcosm` with the sole suggested candidate `ENVO:01000621=microcosm`. |
| `just report` | Passed; rebuilt the corpus report over 3206 records. |

No validator was skipped.

## Identity and Grounding

- The record's minted identifier `habitatmech:GOLD.14789d9032` is a generated,
  content-hashed GOLD identifier and is pinned to slug `sand_microcosm` in
  `data/habitats/PATHS.tsv:1428`.
- The only upstream attestation is GOLD, with `source_id: gold.ecosystem:5872`,
  `source_label: Sand microcosm`, and `source_path: Engineered > Artificial
  ecosystem > Sand microcosm`. This agrees with
  `data/raw/gold_ecosystem_paths.tsv:1144`.
- The attestation note is consistent with the raw source row: three GOLD node
  IDs collapse to the same canonical path, and `src/habitatmech/seed.py`
  intentionally records the first ID and points back to
  `data/raw/gold_ecosystem_paths.tsv` rather than emitting the full ID list.
- The parent `habitatmech:GOLD.0acae9a1a4` is the generated record for the next
  broader source path `Engineered > Artificial ecosystem`, so the source-path
  hierarchy is preserved.
- `mapping_status: SEEDED` is consistent with the absence of an item-level
  curation decision for `habitatmech:GOLD.14789d9032`.
- `grounding_status: UNGROUNDED` follows from the current
  `curation/decisions.tsv:210` class-level `CONFIRM_UNGROUNDED` row, but that
  row is now too weak for the specific path. The source label names a
  microcosm, `data/raw/ontology_terms.tsv:8122` contains the vendored broader
  term `ENVO:01000621` `microcosm`, and `data/raw/ontology_subclass_edges.tsv:6376`
  keeps that term under `ENVO:00010622` `vivarium`. The exact Sand microcosm
  concept still lacks a vendored exact match: an ignored-inclusive,
  case-insensitive search for `sand microcosm` in `data/raw/ontology_terms.tsv`
  and `curation/term_requests.tsv` found no existing ontology term or pending
  term request.
- An ignored-inclusive exact search of the committed GOLD path inventories for
  `Engineered > Artificial ecosystem > Sand microcosm >` found no narrower GOLD
  descendants below this path.

## Evidence

- The record has no curator-authored `evidence` entries, causal graphs,
  environmental parameters, characteristic taxa, discussions, or datasets.
- No claim-level literature evidence is required for the generated GOLD source
  attestation itself. The attestation is backed by the committed raw GOLD path
  row.
- The supplemental GOLD biosample inventory records 24 biosamples for
  `Engineered > Artificial ecosystem > Sand microcosm` at
  `data/raw/gold_path_biosamples.tsv:478`.
- The supplemental GOLD study inventory lists two studies containing this path
  at `data/raw/gold_studies.tsv:856` and `data/raw/gold_studies.tsv:1448`.
- `data/raw/gold_path_triads.tsv:20-22` records two-study MIxS triad leads for
  this exact path: `env_broad_scale` mapped to `ENVO:01000253`, `env_local_scale`
  mapped to `ENVO:01000621`, and `env_medium` mapped to `ENVO:01000017`. The
  `env_local_scale` row is compatible with the broader microcosm parent, and
  the `env_medium` row records sand as sampled material; these MIxS rows are
  contextual evidence and are not automatic identity, parameter, or hierarchy
  inputs for this generated record.

## Completeness

- The empty optional record slots are acceptable for a generated GOLD-only path
  with no direct organism assertions and no inspected literature evidence.
  `src/habitatmech/seed.py` currently emits GOLD `assertion_count` only from
  the nonzero `organism_count` in `data/raw/gold_ecosystem_paths.tsv`, so the
  supplemental 24 biosamples do not create a source-attestation count in this
  record.
- An ignored-inclusive exact search of `curation`, `history`, `research`,
  `data/habitats/PATHS.tsv`, `data/raw`, and `data/habitats` for
  `habitatmech:GOLD.14789d9032` found the PATHS slug row, the class-level
  `curation/decisions.tsv` row, and the generated record before this report
  was added. It found no item-level decision, term-request, causal overlay,
  history, research, or raw source row carrying the minted identifier.
- An ignored-inclusive exact search of `curation`, `history`, `research`,
  `data/raw`, `data/habitats/PATHS.tsv`, and prior review reports for
  `Sand microcosm` and `Engineered > Artificial ecosystem > Sand microcosm`
  found the raw GOLD ecosystem row, two supplemental study rows, one
  supplemental biosample row, three supplemental MIxS triad rows, and the
  generated record before this report was added.
- `find reports/yaml_record_review -name '*sand_microcosm*.md'` found no prior
  review report for this record; `find` included gitignored entries below
  `reports/yaml_record_review`.
- An ignored-inclusive exact search of prior review reports for the full source
  path `Engineered > Artificial ecosystem > Sand microcosm` found no prior
  report covering this generated record.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | `Sand microcosm` is still only class-swept `UNGROUNDED` even though the vendored ENVO slice has the strictly broader habitat `ENVO:01000621` `microcosm`. The current record is not the wrong identity, but it is missing the defensible ontology parent that makes it a `NARROW` engineered microcosm record rather than a fully ungrounded Artificial ecosystem child. | `curation/decisions.tsv` row for `habitatmech:GOLD.14789d9032` |

## Recommended Edits

1. Replace the class-level `CONFIRM_UNGROUNDED` row for
   `habitatmech:GOLD.14789d9032` in `curation/decisions.tsv` with an
   item-level `GROUND_AS_PARENT` decision targeting `ENVO:01000621`
   `microcosm`, with relation `NARROW`, curator/date metadata, and a note that
   GOLD's `Engineered > Artificial ecosystem > Sand microcosm` source denotes a
   microcosm using sand as the sampled or dominant experimental substrate.
2. Run `just seed`, then
   `just seed-canary habitatmech:GOLD.14789d9032`; inspect the generated
   `data/habitats/engineered/sand_microcosm.yaml` canary before running
   `just seed-apply --force`.
3. Do not add a Sand microcosm term request without separate evidence. The
   current review verifies that `ENVO:01000621` is broader and that no exact
   `sand microcosm` term or pending request is present, but it does not inspect
   literature sufficient to author a durable definition.

## Follow-up Checks

- `just validate data/habitats/engineered/sand_microcosm.yaml`
- `just validate-strict data/habitats/engineered/sand_microcosm.yaml`
- `just verify-corpus --max-diffs 1`
- `just term-requests-check`
- `just validate-history`
- `just report`
- Confirm the regenerated record has `grounding_status: NARROW`,
  `mapping_status: REVIEWED`, `parent_habitats` containing `ENVO:01000621`,
  and a `source_attestations` entry with `mapping_predicate: skos:narrowMatch`.

## Additional Notes

- The GOLD path `Engineered > Artificial ecosystem > Microcosm` already grounds
  exactly to `ENVO:01000621`, while its `Freshwater` and `Soil` children carry
  `ENVO:01000621` as a broader parent. Updating `Sand microcosm` to the same
  broader parent would bring this sibling path into the same hierarchy shape.
