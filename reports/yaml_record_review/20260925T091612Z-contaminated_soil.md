# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/terrestrial/contaminated_soil.yaml
- Started UTC: 2026-09-25T09:11:30Z
- Finished UTC: 2026-09-25T09:16:12Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| LinkML class | `HabitatRecord` |
| Identifier | `ENVO:00002116` |
| Label | `contaminated soil` |
| File | `data/habitats/terrestrial/contaminated_soil.yaml` |
| Category | `TERRESTRIAL` |
| Grounding status | `EXACT` |
| Mapping status | `REVIEWED` |
| Generated or maintained | Generated from `data/raw/` inventories and `curation/decisions.tsv` by `scripts/seed_from_sources.py` |

The record merges six GOLD source concepts and one PREGO self-grounded source
concept onto `ENVO:00002116`. The GOLD attestation in the current artificial
ecosystem sweep is `Engineered > Artificial ecosystem > Soil microcosm >
Contaminated soil`, row 1149 of `data/raw/gold_ecosystem_paths.tsv`, a depth-4
row with leaf label `Contaminated soil`, GOLD ecosystem node ID
`gold.ecosystem:6044`, and zero organism, study, biosample, and total
assertion counts in the core kg-microbe inventory.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/terrestrial/contaminated_soil.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/terrestrial/contaminated_soil.yaml` | Passed; 1 file scanned, 0 files with errors, 0 total error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the term-request table is current for 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against the vendored history schema. |
| `just verify-corpus --max-diffs 1` | Passed; expected 3206 records, found 3206, with 0 missing, 0 extra, and 0 differing records. |
| `just worklist --limit 2000 --status all --out /tmp/habitatmech-contaminated-soil-worklist.tsv` | Passed; wrote 953 ungrounded rows. The target is `EXACT` and `REVIEWED`, so no row was keyed by `ENVO:00002116`. |
| `just report` | Passed; rebuilt the corpus report over 3206 records. |

No validator was skipped.

## Identity and Grounding

- The record's identifier, label, and definition come from the vendored ENVO
  row `data/raw/ontology_terms.tsv:7212`: `ENVO:00002116` `contaminated soil`
  is a portion of soil with elevated levels of some contaminant.
- The generated slug `contaminated_soil` is pinned to `ENVO:00002116` in
  `data/habitats/PATHS.tsv:638`.
- The PREGO source concept is `ENVO:00002116` and is therefore an exact
  self-grounded attestation; `data/raw/prego_habitats.tsv:691` records one
  taxon assertion, one direct assertion, a maximum PREGO score of 3, and the
  annotated-genomes-isolates evidence channel.
- Two GOLD soil paths are exact enough to merge into this generic ENVO record:
  `Environmental > Terrestrial > Soil > Contaminated` is a two-node collapsed
  row at `data/raw/gold_ecosystem_paths.tsv:235`, and `Environmental >
  Terrestrial > Soil > Unclassified > Contaminated` at
  `data/raw/gold_ecosystem_paths.tsv:167` uses GOLD's filler `Unclassified`
  level without changing the composed habitat identity.
- Four current GOLD attestations are narrower contexts, not exact identities:
  `Environmental > Terrestrial > Soil > Clay > Contaminated` at
  `data/raw/gold_ecosystem_paths.tsv:544` denotes contaminated clay soil,
  `Environmental > Terrestrial > Soil > Loam > Contaminated` at
  `data/raw/gold_ecosystem_paths.tsv:823` denotes contaminated loam,
  `Environmental > Terrestrial > Soil > Paddy field/soil > Contaminated` at
  `data/raw/gold_ecosystem_paths.tsv:1669` denotes contaminated paddy field
  soil, and `Engineered > Artificial ecosystem > Soil microcosm >
  Contaminated soil` at `data/raw/gold_ecosystem_paths.tsv:1149` denotes
  contaminated soil in a soil microcosm.
- `ENVO:00003082` `enriched soil` is the vendored ENVO superclass of
  `ENVO:00002116` in `data/raw/ontology_subclass_edges.tsv:5314`.
  `ENVO:00001998` `soil` is also a true broader habitat via the source paths.
- `ENVO:00002258` `loam`, `ENVO:00005740` `paddy field soil`,
  `habitatmech:GOLD.ceceb38473` `Clay`, and
  `habitatmech:GOLD.853ee40b1d` `Soil microcosm` are not true parents of the
  generic `ENVO:00002116` class even though they are currently emitted in
  `parent_habitats`.

## Evidence

- The record has no curator-authored `evidence` entries, causal graphs,
  environmental parameters, discussions, or datasets.
- No claim-level literature evidence is required for the generated GOLD and
  PREGO source attestations themselves. GOLD source attestations are backed by
  the committed GOLD ecosystem rows, and the PREGO attestation is backed by
  `data/raw/prego_habitats.tsv:691`.
- The PREGO taxon entry is the single row for `ENVO:00002116` in
  `data/raw/prego_habitat_taxa.tsv:5991`. It records rank 1 of 1 for
  `NCBITaxon:651661` `Dyadobacter psychrophilus` with score 3 from
  annotated-genomes-isolates.
- The supplemental GOLD biosample inventory records 129 biosamples for the
  filler-stripped `Environmental > Terrestrial > Soil > Contaminated` path at
  `data/raw/gold_path_biosamples.tsv:192`, 16 for `Loam > Contaminated` at
  `data/raw/gold_path_biosamples.tsv:549`, 9 for `Clay > Contaminated` at
  `data/raw/gold_path_biosamples.tsv:652`, and 2 for `Paddy field/soil >
  Contaminated` at `data/raw/gold_path_biosamples.tsv:903`.
- `data/raw/gold_path_triads.tsv` lines 962-964, 971-973, and 1076-1078
  record contextual MIxS triad rows for the clay, generic contaminated-soil,
  and paddy-field paths. They agree that the material is soil or contaminated
  soil, but they are contextual evidence and are not automatic identity or
  hierarchy inputs for this generated record.
- An ignored-inclusive exact search of the supplemental GOLD biosample, triad,
  and study inventories for `Engineered > Artificial ecosystem > Soil
  microcosm > Contaminated soil` followed by a tab found no direct supplemental
  row for that path; the only supplemental rows below it belong to the
  narrower `Hydrocarbon` child.

## Completeness

- The record's empty optional `evidence`, `causal_graphs`,
  `environmental_parameters`, `discussions`, and `datasets` slots are
  acceptable for a generated record with no maintained causal overlay, no
  curated record-level literature, and no environment-parameter row.
- The single PREGO `characteristic_taxa` entry is weak but self-contained: it
  carries `rank: 1` and `candidate_pool: 1`, and the field description states
  that seeded taxa are observational associations unless `is_characteristic`
  is set. It does not set `is_characteristic`.
- An ignored-inclusive exact search of `curation`, `history`, `research`,
  `data/raw`, `data/habitats/PATHS.tsv`, `data/habitats`, and prior review
  reports for `ENVO:00002116` found the PATHS slug row, the vendored ENVO term
  and subclass edges, the PREGO habitat and taxon rows, the generated record,
  the current exact GOLD decision rows, and other records that correctly use
  `ENVO:00002116` as a broader parent. It found no term request, prior review
  report, or curation-history entry for the target.
- An ignored-inclusive exact search of `curation/causal_graphs` and `history`
  for `ENVO:00002116` and `contaminated soil` found no causal overlay or
  target-specific history.
- An ignored-inclusive exact search of `data/habitats/PATHS.tsv`,
  `data/habitats`, `curation`, `history`, `research`, and prior review reports
  for the four narrower source-concept identifiers
  `habitatmech:GOLD.6df8395f3e`, `habitatmech:GOLD.7f389946d7`,
  `habitatmech:GOLD.8dbd5ff857`, and `habitatmech:GOLD.7352fc4b9b` found only
  the current `curation/decisions.tsv` rows and the generated target's curation
  history before this report was added. It found no separate generated records
  for those narrower source concepts.
- `find reports/yaml_record_review -name '*contaminated_soil*.md'` found no
  prior review report for this record; `find` included gitignored entries below
  `reports/yaml_record_review`.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | Four narrower GOLD source concepts are merged exactly into generic `ENVO:00002116`, so their source-path parents are emitted as parents of all contaminated soil. The resulting record says contaminated soil is a kind of `Clay`, `loam`, `paddy field soil`, and `Soil microcosm`; those are true of only one source path each and are false as `parent_habitats` for the merged ENVO class. | `curation/decisions.tsv` rows for `habitatmech:GOLD.6df8395f3e`, `habitatmech:GOLD.7f389946d7`, `habitatmech:GOLD.8dbd5ff857`, and `habitatmech:GOLD.7352fc4b9b` |

No blocker or minor findings were found.

## Recommended Edits

1. Replace the `curation/decisions.tsv` rows for
   `habitatmech:GOLD.6df8395f3e`,
   `habitatmech:GOLD.7f389946d7`,
   `habitatmech:GOLD.8dbd5ff857`, and
   `habitatmech:GOLD.7352fc4b9b` with item-level `GROUND_AS_PARENT` decisions
   targeting `ENVO:00002116` `contaminated soil` with `relation: NARROW`.
   Explain in each note that the source path denotes a clay-soil, loam,
   paddy-field-soil, or soil-microcosm context that is narrower than generic
   contaminated soil.
2. Run `just seed`, then canary both the existing target and the four newly
   minted source concepts:
   `just seed-canary ENVO:00002116 habitatmech:GOLD.6df8395f3e
   habitatmech:GOLD.7f389946d7 habitatmech:GOLD.8dbd5ff857
   habitatmech:GOLD.7352fc4b9b`. Inspect all five generated YAML records
   before running `just seed-apply --force`.
3. Confirm the regenerated `data/habitats/terrestrial/contaminated_soil.yaml`
   keeps only true generic broader parents such as `ENVO:00003082` and
   `ENVO:00001998`, retains the generic GOLD soil and PREGO source
   attestations, and no longer lists the clay, loam, paddy-field, or
   soil-microcosm GOLD paths as exact source attestations.

## Follow-up Checks

- `just validate data/habitats/terrestrial/contaminated_soil.yaml`
- `just validate-strict data/habitats/terrestrial/contaminated_soil.yaml`
- `just validate-all`
- `just verify-corpus --max-diffs 1`
- `just term-requests-check`
- `just validate-history`
- `just report`
- Manual inspection of the four new `habitatmech:GOLD.*` records to confirm
  each has `grounding_status: NARROW`, `mapping_status: REVIEWED`,
  `ENVO:00002116` in `parent_habitats`, a `skos:narrowMatch` source
  attestation, and its context-specific source-path parent.

## Additional Notes

- Issue #223 already tracks true-but-redundant superclass edges in
  `parent_habitats`. The false `Clay`, `loam`, `paddy field soil`, and `Soil
  microcosm` parents on `ENVO:00002116` are a different problem: the inherited
  edges are not true of generic contaminated soil.
- The `Environmental > Terrestrial > Soil > Contaminated` exact source path has
  two narrower children, `Pesticide` and `Uranium contaminated`, which
  correctly keep `ENVO:00002116` as a broader parent. The `Engineered >
  Artificial ecosystem > Soil microcosm > Contaminated soil` path likewise has
  the narrower `Hydrocarbon` child.
