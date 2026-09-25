# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/wetland_sediment.yaml
- Started UTC: 2026-09-25T08:27:00Z
- Finished UTC: 2026-09-25T08:31:05Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| LinkML class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.c22928551b` |
| Label | `Wetland sediment` |
| File | `data/habitats/engineered/wetland_sediment.yaml` |
| Category | `ENGINEERED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Generated or maintained | Generated from `data/raw/` inventories and `curation/decisions.tsv` by `scripts/seed_from_sources.py` |

The record is the GOLD path `Engineered > Artificial ecosystem > Sediment
microcosm > Wetland sediment`. Its source row is
`data/raw/gold_ecosystem_paths.tsv:1147`, a depth-4 row with leaf label
`Wetland sediment`, two collapsed GOLD ecosystem node IDs
`gold.ecosystem:5996|gold.ecosystem:5997`, and zero organism, study,
biosample, and total assertion counts in the core kg-microbe inventory.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/engineered/wetland_sediment.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/engineered/wetland_sediment.yaml` | Passed; 1 file scanned, 0 files with errors, 0 total error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the term-request table is current for 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against the vendored history schema. |
| `just verify-corpus --max-diffs 1` | Passed; expected 3206 records, found 3206, with 0 missing, 0 extra, and 0 differing records. |
| `just worklist --limit 2000 --status all --out /tmp/habitatmech-wetland-sediment-worklist.tsv` | Passed; wrote 953 ungrounded rows and retained `Wetland sediment` as an ungrounded backlog row with adjacent sediment lexical candidates only. |
| `just report` | Passed; rebuilt the corpus report over 3206 records. |

No validator was skipped.

## Identity and Grounding

- The record's minted identifier `habitatmech:GOLD.c22928551b` is a generated,
  content-hashed GOLD identifier and is pinned to slug `wetland_sediment` in
  `data/habitats/PATHS.tsv:2716`.
- The only upstream attestation is GOLD, with `source_id: gold.ecosystem:5996`,
  `source_label: Wetland sediment`, and `source_path: Engineered > Artificial
  ecosystem > Sediment microcosm > Wetland sediment`. This agrees with
  `data/raw/gold_ecosystem_paths.tsv:1147`.
- The attestation note is consistent with the raw source row: two GOLD node IDs
  collapse to the same canonical path, and `src/habitatmech/seed.py`
  intentionally records the first ID and points back to
  `data/raw/gold_ecosystem_paths.tsv` rather than emitting the full ID list.
- The parent `habitatmech:GOLD.fcfbc02d98` is the generated record for the next
  broader source path `Engineered > Artificial ecosystem > Sediment microcosm`,
  so the GOLD source-path hierarchy is preserved.
- `mapping_status: SEEDED` is consistent with the absence of an item-level
  curation decision for `habitatmech:GOLD.c22928551b`.
- `grounding_status: UNGROUNDED` follows from the current
  `curation/decisions.tsv:1085` class-level `CONFIRM_UNGROUNDED` row, but that
  row is now too weak for the specific path. The source concept denotes a
  wetland-sediment child of `Sediment microcosm`,
  `data/raw/ontology_terms.tsv:7170` contains the vendored broader term
  `ENVO:00002007` `sediment`, and `data/habitats/terrestrial/sediment.yaml`
  confirms that term already has an exact generated HabitatMech record.
- The exact Wetland sediment microcosm concept still lacks a vendored exact
  match: an ignored-inclusive, case-insensitive search for `wetland sediment`
  in `data/raw/ontology_terms.tsv` and `curation/term_requests.tsv` found no
  existing ontology term or pending term request. The same bounded search found
  only the parent `Sediment microcosm` review in prior
  `reports/yaml_record_review` files.
- The worklist's lexical suggestions for this record were
  `ENVO:01000118` `sandy sediment`, `ENVO:00000546` `lake sediment`, and
  `ENVO:01000120` `clay sediment`. Those are sediment subclasses, not exact
  identities or guaranteed broader terms for this source path.
- An ignored-inclusive exact search of the committed GOLD path inventories for
  `Engineered > Artificial ecosystem > Sediment microcosm > Wetland sediment >`
  found no narrower GOLD descendants below this path.

## Evidence

- The record has no curator-authored `evidence` entries, causal graphs,
  environmental parameters, characteristic taxa, discussions, or datasets.
- No claim-level literature evidence is required for the generated GOLD source
  attestation itself. The attestation is backed by the committed raw GOLD path
  row.
- The supplemental GOLD biosample inventory records 9 biosamples for
  `Engineered > Artificial ecosystem > Sediment microcosm > Wetland sediment`
  at `data/raw/gold_path_biosamples.tsv:643`.
- The supplemental GOLD study inventory lists one study, `Gs0154348`, with
  only this path at `data/raw/gold_studies.tsv:3987`.
- An ignored-inclusive exact search for the full source path found no
  `data/raw/gold_path_triads.tsv` row for `Engineered > Artificial ecosystem >
  Sediment microcosm > Wetland sediment`.

## Completeness

- The empty optional record slots are acceptable for a generated GOLD-only path
  with no direct organism assertions, no committed MIxS triad rows, and no
  inspected literature evidence. `src/habitatmech/seed.py` currently emits GOLD
  `assertion_count` only from the nonzero `organism_count` in
  `data/raw/gold_ecosystem_paths.tsv`, so the supplemental 9 biosamples do not
  create a source-attestation count in this record.
- An ignored-inclusive exact search of `curation`, `history`, `research`,
  `data/raw`, `data/habitats/PATHS.tsv`, `data/habitats`, and prior review
  reports for `habitatmech:GOLD.c22928551b` found the PATHS slug row, the
  class-level `curation/decisions.tsv` row, and the generated target before
  this report was added. It found no item-level decision, term-request, causal
  overlay, history, research, prior review report, or raw source row carrying
  the minted identifier.
- An ignored-inclusive exact search of `curation`, `history`, `research`,
  `data/raw`, `data/habitats/PATHS.tsv`, and prior review reports for
  `Wetland sediment` and `Engineered > Artificial ecosystem > Sediment
  microcosm > Wetland sediment` found the raw GOLD ecosystem row, one
  supplemental study row, one supplemental biosample row, the generated record,
  and mentions in the parent `Sediment microcosm` review before this report was
  added.
- Exact ignored-inclusive searches for `gold.ecosystem:5996` and
  `gold.ecosystem:5997` across `data/raw`, `data/habitats`, `curation`,
  `history`, `research`, and prior review reports found only the raw GOLD
  ecosystem row and the generated record's first-node `source_id`; the second
  collapsed node remains represented by the generated attestation note.
- `find reports/yaml_record_review -name '*wetland_sediment*.md'` found no
  prior review report for this record; `find` included gitignored entries below
  `reports/yaml_record_review`.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | `Wetland sediment` is only class-swept `UNGROUNDED`, but the vendored slice contains `ENVO:00002007` `sediment`, a strictly broader parent for this depth-4 wetland-sediment path. Leaving the record at a class-level `CONFIRM_UNGROUNDED` keeps the missing broader material grounding invisible and leaves `mapping_status` at `SEEDED` even though the specific GOLD path can be item-reviewed as narrower than `sediment`. | `curation/decisions.tsv` |

No blocker or minor findings were found.

## Recommended Edits

1. Replace the `curation/decisions.tsv` row for
   `habitatmech:GOLD.c22928551b` with an item-level `GROUND_AS_PARENT`
   decision targeting `ENVO:00002007` `sediment` with `relation: NARROW`.
   Keep the exact concept minted because the vendored ontology slice contains
   the broader `sediment` material term but no exact Wetland sediment microcosm
   term.
2. Re-run `just seed`, `just seed-canary habitatmech:GOLD.c22928551b`, inspect
   `data/habitats/engineered/wetland_sediment.yaml`, then run
   `just seed-apply --force`.

## Follow-up Checks

- `just validate data/habitats/engineered/wetland_sediment.yaml`
- `just validate-strict data/habitats/engineered/wetland_sediment.yaml`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000 --status all --out /tmp/habitatmech-wetland-sediment-worklist.tsv`
- `just report`

## Additional Notes

- The current source-path parent, `Sediment microcosm`, should remain a parent
  because it captures the Engineered > Artificial ecosystem context that is not
  implied by the ENVO `sediment` material term.
- The sibling review for `Sediment microcosm` already identified a separate
  missing `ENVO:01000621` `microcosm` parent on that source concept. Once that
  future curation fix lands, `Wetland sediment` will inherit microcosm ancestry
  through its source-path parent.
