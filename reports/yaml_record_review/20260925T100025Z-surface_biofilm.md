# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/surface_biofilm.yaml
- Started UTC: 2026-09-25T10:00:25Z
- Finished UTC: 2026-09-25T10:00:25Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/engineered/surface_biofilm.yaml` |
| Identifier | `habitatmech:GOLD.ef9152b355` |
| Label | `Surface biofilm` |
| Category | `ENGINEERED` |
| Grounding | `UNGROUNDED` |
| Mapping | `SEEDED` |
| Maintained owner | `curation/decisions.tsv`; if retained as a novel path-qualified biofilm, `curation/term_requests.tsv` |

The record is generated from the single GOLD source path
`Engineered > Artificial ecosystem > Soil microcosm > Surface biofilm`.
`data/raw/gold_ecosystem_paths.tsv` collapses two GOLD ecosystem node IDs,
`gold.ecosystem:7703|gold.ecosystem:7704`, onto that canonical path; the
generated source attestation shows `gold.ecosystem:7703` and points back to the
raw row for the full list.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/engineered/surface_biofilm.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/engineered/surface_biofilm.yaml` | Passed; 1 file scanned with 0 files carrying errors and 0 total error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the term-request table is current for 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; expected 3,206 records, found 3,206 records, with 0 missing, 0 extra, and 0 differing. |
| `just worklist --limit 2000 --status all --out /tmp/habitatmech-surface-biofilm-worklist.tsv` | Passed and wrote 953 ungrounded rows. `Surface biofilm` is retained as row 881 with one lexical candidate, `ENVO:02000059` `surface soil`. |
| `just report` | Passed; rebuilt the corpus report over 3,206 records. |

No validator was skipped.

## Identity and Grounding

- `habitatmech:GOLD.ef9152b355` is a generated content-hashed GOLD identifier
  pinned to slug `surface_biofilm` in `data/habitats/PATHS.tsv`.
- The source attestation agrees with the raw GOLD source row: both have source
  label `Surface biofilm` and source path `Engineered > Artificial ecosystem >
  Soil microcosm > Surface biofilm`.
- The current `UNGROUNDED` status follows from a class-level
  `CONFIRM_UNGROUNDED` row in `curation/decisions.tsv`. That row only records
  that no lexical route matched `Surface biofilm`; it explicitly did not assess
  whether the concept is a real habitat.
- The vendored slice contains `ENVO:00002034` `biofilm`, defined as a complex
  aggregation of microorganisms usually adhering to a substratum. That is the
  established genus for path-qualified GOLD biofilm leaves such as
  `air scrubber biofilm`.
- The worklist's `ENVO:02000059` `surface soil` candidate is a false lexical
  match. It accounts for `Surface` while ignoring the `biofilm` head.

The generated `habitatmech:GOLD.853ee40b1d` parent is also suspect. The raw
GOLD path says this source is nested below `Soil microcosm`, but a surface
biofilm in a soil microcosm is not a subtype of soil microcosm. The source-path
parent is context, the same "biofilm inside X" pattern already curated for the
`air scrubber biofilm` record with `parent_mode=REPLACE`.

## Evidence

- **Supported:** the GOLD path itself exists and has two collapsed source node
  IDs in `data/raw/gold_ecosystem_paths.tsv`.
- **Supported:** the source occurs in GOLD's supplemental API-derived side
  tables. `data/raw/gold_path_biosamples.tsv` records 24 biosamples under
  node `7704`, and `data/raw/gold_studies.tsv` records one study for the exact
  path.
- **Supported:** GOLD submitters treated this exact path as a biofilm sample.
  `data/raw/gold_path_triads.tsv` records 24 biosamples from one study whose
  MIxS `env_medium` is `ENVO:01000156` `biofilm material`.
- **Supported:** `ENVO:00002034` `biofilm` is the established broader class for
  path-qualified GOLD biofilm leaves. `curation/term_requests.tsv` defines
  `habitatmech:GOLD.7f436f8aff` `air scrubber biofilm` under `ENVO:00002034`
  and uses `parent_mode=REPLACE` to drop an inherited device parent.
- **Unsupported:** the generated strict parent edge to
  `habitatmech:GOLD.853ee40b1d` `Soil microcosm`. The source path supports a
  contextual soil-microcosm setting, not an `is-a` claim.
- **Unsupported:** exact grounding to `ENVO:02000059` `surface soil`. The
  record is a biofilm, not topsoil.

## Completeness

Ignored-file-inclusive exact searches used `rg --no-ignore --hidden` over
`curation`, `history`, `research`, `reports/yaml_record_review`, `data/raw`,
`data/habitats/PATHS.tsv`, and generated `data/habitats`, plus `find` under
`reports/yaml_record_review`.

- Exact searches for `habitatmech:GOLD.ef9152b355` found the PATHS slug row,
  the class-level decision row, and the generated target. They found no
  item-level decision, term request, term-request exclusion, history record,
  research report, causal overlay, or prior review report.
- Exact searches for `gold.ecosystem:7703`, `gold.ecosystem:7704`, and
  `Engineered > Artificial ecosystem > Soil microcosm > Surface biofilm` found
  the raw ecosystem-path row, the supplemental 24-biosample row, the
  one-study row, the three GOLD triad rows, and the generated target.
- Broader searches for `ENVO:00002034` and `biofilm` found the generic
  vendored biofilm term, the generic biofilm causal overlay, existing
  path-qualified biofilm records, the `air scrubber biofilm` term request, and
  prior YAML reviews that already document why source-path parents for
  `Biofilm` leaves are often contextual. They found no maintained curation for
  this exact target.
- `find reports/yaml_record_review -maxdepth 1 -name '*surface_biofilm*.md'`
  found no prior report for this stem; `find` includes ignored files.

The optional `definition`, `evidence`, `environmental_parameters`,
`characteristic_taxa`, `causal_graphs`, `discussions`, and `datasets` slots are
empty. That is structurally acceptable for a generated GOLD-only record, but a
retained path-qualified biofilm will need a definition in
`curation/term_requests.tsv` to remove the false source-path parent.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | `Surface biofilm` is still class-swept `UNGROUNDED`, but the vendored slice contains `ENVO:00002034` `biofilm`, a verified broader parent for path-qualified GOLD biofilm leaves. The row needs item review rather than a class-level `CONFIRM_UNGROUNDED` decision whose only evidence was a failed lexical match against the full label. | `curation/decisions.tsv` |
| Major | `parent_habitats` asserts that this surface biofilm is a kind of `habitatmech:GOLD.853ee40b1d` `Soil microcosm`. The GOLD path and MIxS medium support a biofilm in a soil-microcosm context; they do not make the sampled biofilm a subtype of the whole microcosm. | `curation/term_requests.tsv` |

No blockers or minor findings were found.

## Recommended Edits

1. Replace the class-level `curation/decisions.tsv` row for
   `habitatmech:GOLD.ef9152b355` with an item-level `GROUND_AS_PARENT` decision
   to `ENVO:00002034` `biofilm`. Do not ground to `ENVO:02000059` `surface
   soil`, and do not ground to `ENVO:01000156` `biofilm material` unless item
   review finds that GOLD meant biofilm-derived material rather than the
   attached aggregate itself.

2. If item review retains this as a distinct soil-microcosm surface biofilm,
   define it in `curation/term_requests.tsv` under `ENVO:00002034` `biofilm`
   with `parent_mode=REPLACE`, so regeneration drops the inherited
   `habitatmech:GOLD.853ee40b1d` parent.

3. Add an append-only history record for the curation session that changes the
   decision or term request. Do not edit the generated
   `data/habitats/engineered/surface_biofilm.yaml` directly.

## Follow-up Checks

- `just seed`
- `just seed-canary habitatmech:GOLD.ef9152b355`
- `just seed-apply --force`
- `just validate data/habitats/engineered/surface_biofilm.yaml`
- `just validate-strict data/habitats/engineered/surface_biofilm.yaml`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000 --status all --out /tmp/habitatmech-surface-biofilm-worklist.tsv`
- `just report`

After reseeding, inspect the generated record and confirm that it is `NARROW`,
has a `skos:narrowMatch` source attestation to `ENVO:00002034`, no longer has
`habitatmech:GOLD.853ee40b1d` in `parent_habitats`, and has curation-history
events for the item-level decision and definition.

## Additional Notes

- `ENVO:01000156` `biofilm material` remains a useful MIxS medium lead, but it
  is already an exact PREGO-backed record in this corpus. The GOLD source label
  says `Surface biofilm`, not `Biofilm material`.
- The generic `ENVO:00002034` `biofilm` causal overlay does not prove any
  mechanism specific to surface biofilms in soil microcosms.
