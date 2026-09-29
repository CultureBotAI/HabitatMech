# YAML Record Review: Nervous system

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/host_associated/nervous_system__b360fe7b.yaml`
- Started UTC: `2026-09-29T22:27:30Z`
- Finished UTC: `2026-09-29T22:33:02Z`
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.bbbdbf55b3` |
| Label | `Nervous system` |
| Stable slug | `nervous_system__b360fe7b` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `NARROW` |
| Mapping status | `SEEDED` |
| Source concept | `habitatmech:GOLD.bbbdbf55b3` |
| Source attestation | `GOLD`, `gold.ecosystem:6908`, `Host-associated > Birds > Nervous system`, `skos:narrowMatch` |

The record is the generated GOLD concept for the Bird-specific `Nervous
system` path. It is intentionally minted because `Host-associated > Birds >
Nervous system` is narrower than the generic UBERON `nervous system` anatomy
class. The generated record preserves `UBERON:0001016` as a broader anatomical
parent and `habitatmech:GOLD.47e603cf4f` as the immediate GOLD source-path
parent for `Host-associated > Birds`.

The record has one GOLD source attestation, no assertion count, no authored
definition, no synonyms, no environmental parameters, no characteristic taxa,
no record-level evidence block, and no causal graphs.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/nervous_system__b360fe7b.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/habitats/host_associated/nervous_system__b360fe7b.yaml` | Passed; 1 file scanned, 0 files with errors, 0 error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; expected 3206 records, found 3206 on disk, with 0 missing, 0 extra, and 0 differing. |
| `just report --ungrounded-top 0 --out /private/tmp/habitatmech-report-bird-nervous-system.tsv` | Passed; wrote the TSV snapshot and reported `habitatmech:GOLD.bbbdbf55b3` as `NARROW`, `SEEDED`, 1 source, 0 assertions, no definition, 2 parents, 0 parameters, 0 taxa, and 0 causal graphs. |
| `just worklist --limit 40 --status all --out /private/tmp/habitatmech-worklist-bird-nervous-system.tsv` | Passed; wrote 953 ungrounded backlog rows. `habitatmech:GOLD.bbbdbf55b3` is NARROW, not UNGROUNDED, so it is not a ranked ungrounded item. |

## Identity and Grounding

The generated identity is sound. `data/raw/gold_ecosystem_paths.tsv` has the
exact source row `Host-associated > Birds > Nervous system` with leaf label
`Nervous system`, depth 3, three collapsed GOLD ecosystem node IDs, zero
aggregate assertions, and source IDs
`gold.ecosystem:6908|gold.ecosystem:6909|gold.ecosystem:6910`.

`data/habitats/PATHS.tsv` pins `habitatmech:GOLD.bbbdbf55b3` to the stable
`nervous_system__b360fe7b` slug, and the generated target YAML uses that
identifier and slug for exactly this Bird source path.

The `NARROW` grounding against `UBERON:0001016` is appropriate. The vendored
ontology slice labels `UBERON:0001016` as `nervous system` and defines it as an
organ system containing predominantly neuron and glial cells. The GOLD source
path adds the Bird host-clade context, so the record should stay a minted
habitat narrower than the generic UBERON anatomy term rather than adopting
`UBERON:0001016` as an exact identity.

The two generated parents are traceable to input data:

| Parent | Support |
|---|---|
| `UBERON:0001016` | The source leaf is a case variant of the UBERON `nervous system` anatomy label, and the generic anatomy class is broader than this Bird-specific source concept. |
| `habitatmech:GOLD.47e603cf4f` | GOLD has the immediate broader path `Host-associated > Birds`; that generated record is the curated `bird-associated environment` parent. |

The target is also distinct from the other minted host-associated Nervous
system source paths for Mammals, Mammals: Human, Fish, Reptilia, and
Arthropoda: Insects. All of those records preserve their host-clade context in
separate `habitatmech:GOLD.*` identifiers instead of merging onto
`UBERON:0001016`.

## Evidence

The record carries no curator-authored evidence block. Its identity is backed
by the GOLD path inventory and the seeder's lexical narrower-than-ontology
route, not by an item-level curation decision.

The zero assertion total is supported by the raw GOLD inventory. The exact raw
row reports `organism_count = 0`, `study_count = 0`, `biosample_count = 0`,
`mixs_triad_count = 0`, `gold_triad_count = 0`, and `total_assertions = 0` for
this path, and an ignored/hidden-inclusive search for `gold.ecosystem:6908`,
`gold.ecosystem:6909`, and `gold.ecosystem:6910` found no rows in
`data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`, or
`data/raw/gold_studies.tsv`.

No causal graph is attached to this record. Ignored/hidden-inclusive searches
found no causal overlay keyed by `habitatmech:GOLD.bbbdbf55b3`, the
`nervous_system__b360fe7b` slug, or any exact source GOLD ecosystem ID under
`curation/causal_graphs`.

## Completeness

- The rendered page
  `pages/habitats/nervous-system-habitatmech-gold-bbbdbf55b3.html` reflects
  the same minted identifier, label, category, `NARROW` grounding,
  `SEEDED` mapping status, GOLD source path, and two broader habitats as the
  YAML.
- The exact ignored/hidden-inclusive search for
  `habitatmech:GOLD.bbbdbf55b3`, `nervous_system__b360fe7b`,
  `gold.ecosystem:6908`, `gold.ecosystem:6909`, `gold.ecosystem:6910`, and the
  full source path covered `curation`, `history`, `research`, `conf/`,
  `data/raw/`, `data/habitats/`, and the prior YAML review reports. It found
  the expected generated YAML, path lock, raw GOLD row, rendered target page,
  and Bird Brain review cross-reference, but no target-specific maintained
  curation artifact, research report, history record, or prior exact review.
- Empty optional slots are appropriate for this seeded zero-assertion parent
  record. No raw side-table rows support generated environmental parameters or
  taxa, and no maintained overlay supplies causal graphs.

## Findings

None found.

## Recommended Edits

None found.

## Follow-up Checks

None required.

## Additional Notes

- The prior `reports/yaml_record_review/20260922T092818Z-brain__f0593337.md`
  report references this record only as the immediate GOLD parent of
  `Host-associated > Birds > Nervous system > Brain`; it is not a review of
  `habitatmech:GOLD.bbbdbf55b3` itself.
- iModulonDB structured source checks were not applicable: the record names a
  GOLD anatomical habitat path and no genes, locus tags, regulators, pathways,
  stress-response terms, or transcriptomic datasets.
