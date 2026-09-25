# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/soil_microcosm.yaml
- Started UTC: 2026-09-25T08:46:00Z
- Finished UTC: 2026-09-25T08:57:56Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| LinkML class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.853ee40b1d` |
| Label | `Soil microcosm` |
| File | `data/habitats/engineered/soil_microcosm.yaml` |
| Category | `ENGINEERED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Generated or maintained | Generated from `data/raw/` inventories and `curation/decisions.tsv` by `scripts/seed_from_sources.py` |

The record is the GOLD path `Engineered > Artificial ecosystem > Soil
microcosm`. Its source row is `data/raw/gold_ecosystem_paths.tsv:1148`, a
depth-3 row with leaf label `Soil microcosm`, three collapsed GOLD ecosystem
node IDs `gold.ecosystem:5847|gold.ecosystem:5848|gold.ecosystem:5849`, and
zero organism, study, biosample, and total assertion counts in the core
kg-microbe inventory.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/engineered/soil_microcosm.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/engineered/soil_microcosm.yaml` | Passed; 1 file scanned, 0 files with errors, 0 total error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the term-request table is current for 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against the vendored history schema. |
| `just verify-corpus --max-diffs 1` | Passed; expected 3206 records, found 3206, with 0 missing, 0 extra, and 0 differing records. |
| `just worklist --limit 2000 --status all --out /tmp/habitatmech-soil-microcosm-worklist.tsv` | Passed; wrote 953 ungrounded rows and retained `Soil microcosm` with the sole suggested lexical candidate `ENVO:01000621=microcosm`. |
| `just report` | Passed; rebuilt the corpus report over 3206 records. |

No validator was skipped.

## Identity and Grounding

- The record's minted identifier `habitatmech:GOLD.853ee40b1d` is a generated,
  content-hashed GOLD identifier and is pinned to slug `soil_microcosm` in
  `data/habitats/PATHS.tsv:2276`.
- The only upstream attestation is GOLD, with `source_id: gold.ecosystem:5847`,
  `source_label: Soil microcosm`, and `source_path: Engineered > Artificial
  ecosystem > Soil microcosm`. This agrees with
  `data/raw/gold_ecosystem_paths.tsv:1148`.
- The attestation note is consistent with the raw source row: three GOLD node
  IDs collapse to the same canonical path, and `src/habitatmech/seed.py`
  intentionally records the first ID and points back to
  `data/raw/gold_ecosystem_paths.tsv` rather than emitting the full ID list.
- The parent `habitatmech:GOLD.0acae9a1a4` is the generated record for the next
  broader source path `Engineered > Artificial ecosystem`, so the source-path
  hierarchy is preserved.
- `mapping_status: SEEDED` is consistent with the absence of an item-level
  curation decision for `habitatmech:GOLD.853ee40b1d`.
- `grounding_status: UNGROUNDED` follows from the current
  `curation/decisions.tsv:789` class-level `CONFIRM_UNGROUNDED` row, but that
  row is now too weak for the specific path. The source label names a
  microcosm, `data/raw/ontology_terms.tsv:8122` contains the vendored broader
  term `ENVO:01000621` `microcosm`, and
  `data/raw/ontology_subclass_edges.tsv:6376` keeps that term under
  `ENVO:00010622` `vivarium`. The exact Soil microcosm concept still lacks a
  vendored exact match: an ignored-inclusive, case-insensitive search for
  `soil microcosm` in `data/raw/ontology_terms.tsv` and
  `curation/term_requests.tsv` found no existing ontology term or pending term
  request.
- An ignored-inclusive exact search of the committed GOLD path inventories for
  `Engineered > Artificial ecosystem > Soil microcosm >` found two direct
  narrower GOLD descendants: `Contaminated soil` and `Surface biofilm`.
  `data/habitats/terrestrial/contaminated_soil.yaml` and
  `data/habitats/engineered/surface_biofilm.yaml` preserve
  `habitatmech:GOLD.853ee40b1d` as a generated parent.

## Evidence

- The record has no curator-authored `evidence` entries, causal graphs,
  environmental parameters, characteristic taxa, discussions, or datasets.
- No claim-level literature evidence is required for the generated GOLD source
  attestation itself. The attestation is backed by the committed raw GOLD path
  row.
- The supplemental GOLD biosample inventory records 868 biosamples for
  `Engineered > Artificial ecosystem > Soil microcosm` at
  `data/raw/gold_path_biosamples.tsv:39`.
- The supplemental GOLD study inventory lists nine studies containing this
  exact path at `data/raw/gold_studies.tsv` lines 537, 2142, 2182, 3871, 3985,
  4027, 4060, 4069, and 4445.
- `data/raw/gold_path_triads.tsv:23-25` records three-study MIxS triad leads
  for this exact path: `env_broad_scale` mapped to `ENVO:00000446`
  `terrestrial biome`, `env_local_scale` mapped to `ENVO:00005801`
  `rhizosphere`, and `env_medium` mapped to `ENVO:00001998` `soil`. The soil
  medium row is compatible with the source label, but these MIxS rows are
  contextual evidence and are not automatic identity, parameter, or hierarchy
  inputs for this generated record.

## Completeness

- The empty optional record slots are acceptable for a generated GOLD-only path
  with no direct organism assertions and no inspected literature evidence.
  `src/habitatmech/seed.py` currently emits GOLD `assertion_count` only from
  the nonzero `organism_count` in `data/raw/gold_ecosystem_paths.tsv`, so the
  supplemental 868 biosamples do not create a source-attestation count in this
  record.
- An ignored-inclusive exact search of `curation`, `history`, `research`,
  `data/habitats/PATHS.tsv`, `data/raw`, `data/habitats`, and prior review
  reports for `habitatmech:GOLD.853ee40b1d` found the PATHS slug row, the
  class-level `curation/decisions.tsv` row, the generated target, and two child
  generated parent references before this report was added. It found no
  item-level decision, term request, causal overlay, history, research, prior
  review report, or raw source row carrying the minted identifier.
- An ignored-inclusive exact search of `curation`, `term_requests`, `graphs`,
  `history`, `research`, `data/raw`, `data/habitats/PATHS.tsv`, and prior
  review reports for `Soil microcosm` and `Engineered > Artificial ecosystem >
  Soil microcosm` found the raw parent row, the raw Contaminated soil and
  Surface biofilm child rows, nine supplemental study rows, one supplemental
  biosample row, three supplemental MIxS triad rows, and the generated target
  before this report was added.
- `find reports/yaml_record_review -name '*soil_microcosm*.md'` found no prior
  review report for this record; `find` included gitignored entries below
  `reports/yaml_record_review`.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | `Soil microcosm` is only class-swept `UNGROUNDED`, but the vendored slice contains `ENVO:01000621` `microcosm`, a strictly broader parent for this engineered artificial-ecosystem path. Leaving the record at a class-level `CONFIRM_UNGROUNDED` keeps the missing broader grounding invisible and leaves `mapping_status` at `SEEDED` even though the specific GOLD path can be item-reviewed as narrower than `microcosm`. | `curation/decisions.tsv` |

No blocker or minor findings were found.

## Recommended Edits

1. Replace the `curation/decisions.tsv` row for
   `habitatmech:GOLD.853ee40b1d` with an item-level `GROUND_AS_PARENT`
   decision targeting `ENVO:01000621` `microcosm` with `relation: NARROW`.
   Keep the exact concept minted because the vendored ontology slice contains
   the broader `microcosm` term but no exact `Soil microcosm` term.
2. Re-run `just seed`, `just seed-canary habitatmech:GOLD.853ee40b1d`,
   inspect `data/habitats/engineered/soil_microcosm.yaml`, then run
   `just seed-apply --force`.
3. Do not add a Soil microcosm term request without separate evidence. The
   current review verifies that `ENVO:01000621` is broader and that no exact
   `soil microcosm` term or pending request is present, but it does not inspect
   literature sufficient to author a durable definition.

## Follow-up Checks

- `just validate data/habitats/engineered/soil_microcosm.yaml`
- `just validate-strict data/habitats/engineered/soil_microcosm.yaml`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000 --status all --out /tmp/habitatmech-soil-microcosm-worklist.tsv`
- `just report`
- Confirm the regenerated record has `grounding_status: NARROW`,
  `mapping_status: REVIEWED`, `parent_habitats` containing `ENVO:01000621`,
  and a `source_attestations` entry with `mapping_predicate: skos:narrowMatch`.

## Additional Notes

- The GOLD path `Engineered > Artificial ecosystem > Microcosm` already grounds
  exactly to `ENVO:01000621`, while its `Soil` child carries both
  `ENVO:01000621` and `ENVO:00001998` as broader parents. Updating `Soil
  microcosm` to the same broader `microcosm` parent would bring this parallel
  artificial ecosystem path into the same hierarchy shape.
- A future definition curation pass can decide whether an exact Soil microcosm
  term request should add `ENVO:00001998` `soil` as a second broader parent.
  That is separate from the immediate grounding issue: the GOLD label and path
  already establish `ENVO:01000621` `microcosm` as strictly broader than the
  source concept.
