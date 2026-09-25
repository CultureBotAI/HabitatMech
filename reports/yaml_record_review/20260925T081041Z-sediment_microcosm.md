# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/sediment_microcosm.yaml
- Started UTC: 2026-09-25T07:59:45Z
- Finished UTC: 2026-09-25T08:10:41Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| LinkML class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.fcfbc02d98` |
| Label | `Sediment microcosm` |
| File | `data/habitats/engineered/sediment_microcosm.yaml` |
| Category | `ENGINEERED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Generated or maintained | Generated from `data/raw/` inventories and `curation/decisions.tsv` by `scripts/seed_from_sources.py` |

The record is the GOLD path `Engineered > Artificial ecosystem > Sediment
microcosm`. Its source row is `data/raw/gold_ecosystem_paths.tsv:1146`, a
depth-3 row with leaf label `Sediment microcosm`, one GOLD ecosystem node ID
`gold.ecosystem:5995`, and zero organism, study, biosample, and total assertion
counts in the core kg-microbe inventory.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/engineered/sediment_microcosm.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/engineered/sediment_microcosm.yaml` | Passed; 1 file scanned, 0 files with errors, 0 total error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the term-request table is current for 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against the vendored history schema. |
| `just verify-corpus --max-diffs 1` | Passed; expected 3206 records, found 3206, with 0 missing, 0 extra, and 0 differing records. |
| `just worklist --limit 2000 --status all --out /tmp/habitatmech-sediment-microcosm-worklist.tsv` | Passed; wrote 953 ungrounded rows and retained `Sediment microcosm` as an ungrounded backlog row with no lexical candidate. |
| `just report` | Passed; rebuilt the corpus report over 3206 records. |

No validator was skipped.

## Identity and Grounding

- The record's minted identifier `habitatmech:GOLD.fcfbc02d98` is a generated,
  content-hashed GOLD identifier and is pinned to slug `sediment_microcosm` in
  `data/habitats/PATHS.tsv:3170`.
- The only upstream attestation is GOLD, with `source_id: gold.ecosystem:5995`,
  `source_label: Sediment microcosm`, and `source_path: Engineered >
  Artificial ecosystem > Sediment microcosm`. This agrees with
  `data/raw/gold_ecosystem_paths.tsv:1146`.
- The parent `habitatmech:GOLD.0acae9a1a4` is the generated record for the next
  broader source path `Engineered > Artificial ecosystem`, so the source-path
  hierarchy is preserved.
- `mapping_status: SEEDED` is consistent with the absence of an item-level
  curation decision for `habitatmech:GOLD.fcfbc02d98`.
- `grounding_status: UNGROUNDED` follows from the current
  `curation/decisions.tsv:1386` class-level `CONFIRM_UNGROUNDED` row, but that
  row is now too weak for the specific path. The source label names a
  microcosm, `data/raw/ontology_terms.tsv:8122` contains the vendored broader
  term `ENVO:01000621` `microcosm`, and
  `data/raw/ontology_subclass_edges.tsv:6376` keeps that term under
  `ENVO:00010622` `vivarium`. The exact Sediment microcosm concept still lacks
  a vendored exact match: an ignored-inclusive, case-insensitive search for
  `sediment microcosm` in `data/raw/ontology_terms.tsv` and
  `curation/term_requests.tsv` found no existing ontology term or pending term
  request.
- An ignored-inclusive exact search of the committed GOLD path inventories for
  `Engineered > Artificial ecosystem > Sediment microcosm >` found one narrower
  GOLD descendant, the Wetland sediment row at
  `data/raw/gold_ecosystem_paths.tsv:1147`; that descendant is correctly a
  separate record, `data/habitats/engineered/wetland_sediment.yaml`.

## Evidence

- The record has no curator-authored `evidence` entries, causal graphs,
  environmental parameters, characteristic taxa, discussions, or datasets.
- No claim-level literature evidence is required for the generated GOLD source
  attestation itself. The attestation is backed by the committed raw GOLD path
  row.
- An ignored-inclusive exact search for the full source path plus a trailing
  tab found no `data/raw/gold_path_biosamples.tsv`,
  `data/raw/gold_studies.tsv`, or `data/raw/gold_path_triads.tsv` row for the
  direct `Engineered > Artificial ecosystem > Sediment microcosm` path.
- The only supplemental GOLD rows found under this path belong to the narrower
  `Engineered > Artificial ecosystem > Sediment microcosm > Wetland sediment`
  child, not to `Sediment microcosm` itself.

## Completeness

- The empty optional record slots are acceptable for a generated GOLD-only path
  with no direct organism, study, biosample, or triad assertions and no
  inspected literature evidence.
- An ignored-inclusive exact search of `curation`, `history`, `research`,
  `data/habitats/PATHS.tsv`, `data/raw`, `data/habitats`, and prior review
  reports for `habitatmech:GOLD.fcfbc02d98` found the PATHS slug row, the
  class-level `curation/decisions.tsv` row, the generated target, and one child
  reference from `data/habitats/engineered/wetland_sediment.yaml`. It found no
  item-level decision, term-request, causal overlay, history, research, prior
  review report, or raw source row carrying the minted identifier.
- An ignored-inclusive exact search of `curation`, `history`, `research`,
  `data/raw`, `data/habitats/PATHS.tsv`, and prior review reports for
  `Sediment microcosm` and `Engineered > Artificial ecosystem > Sediment
  microcosm` found the raw parent row, the raw Wetland sediment child rows, and
  the generated parent record before this report was added.
- `find reports/yaml_record_review -name '*sediment_microcosm*.md'` found no
  prior review report for this record; `find` included gitignored entries below
  `reports/yaml_record_review`.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | `Sediment microcosm` is only class-swept `UNGROUNDED`, but the vendored slice contains `ENVO:01000621` `microcosm`, a strictly broader parent for this engineered artificial-ecosystem path. Leaving the record at a class-level `CONFIRM_UNGROUNDED` keeps the missing broader grounding invisible and leaves `mapping_status` at `SEEDED` even though the specific GOLD path can be item-reviewed as narrower than `microcosm`. | `curation/decisions.tsv` |

No blocker or minor findings were found.

## Recommended Edits

1. Replace the `curation/decisions.tsv` row for
   `habitatmech:GOLD.fcfbc02d98` with an item-level `GROUND_AS_PARENT`
   decision targeting `ENVO:01000621` `microcosm` with `relation: NARROW`.
   Keep the exact concept minted because the vendored ontology slice contains
   the broader `microcosm` term but no exact `Sediment microcosm` term.
2. Re-run `just seed`, `just seed-canary habitatmech:GOLD.fcfbc02d98`,
   inspect `data/habitats/engineered/sediment_microcosm.yaml`, then run
   `just seed-apply --force`.

## Follow-up Checks

- `just validate data/habitats/engineered/sediment_microcosm.yaml`
- `just validate-strict data/habitats/engineered/sediment_microcosm.yaml`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000 --status all --out /tmp/habitatmech-sediment-microcosm-worklist.tsv`
- `just report`

## Additional Notes

- A future definition curation pass can decide whether an exact Sediment
  microcosm term request should add `ENVO:00002007` `sediment` as a second
  broader parent. That is separate from the immediate grounding issue: the GOLD
  label and path already establish `ENVO:01000621` `microcosm` as strictly
  broader than the source concept.
