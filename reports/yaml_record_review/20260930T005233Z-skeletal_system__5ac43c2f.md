# YAML Record Review: Skeletal system

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/host_associated/skeletal_system__5ac43c2f.yaml`
- Started UTC: `2026-09-30T00:40:30Z`
- Finished UTC: `2026-09-30T00:52:33Z`
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.3756d4bb39` |
| Label | `Skeletal system` |
| Stable slug | `skeletal_system__5ac43c2f` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `NARROW` |
| Mapping status | `SEEDED` |
| Source concept | `habitatmech:GOLD.3756d4bb39` |
| Source attestation | `GOLD`, `gold.ecosystem:7476`, `Host-associated > Birds > Skeletal system`, `skos:narrowMatch` |

The record is the generated GOLD concept for the Bird-specific `Skeletal
system` path. It is intentionally minted because `Host-associated > Birds >
Skeletal system` is narrower than the generic UBERON `skeletal system`
anatomy class. The generated record preserves `UBERON:0001434` as a broader
anatomical parent and `habitatmech:GOLD.47e603cf4f` as the immediate GOLD
source-path parent for `Host-associated > Birds`.

The record has one GOLD source attestation, no assertion count, no authored
definition, no synonyms, no environmental parameters, no characteristic taxa,
no record-level evidence block, and no causal graphs.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/skeletal_system__5ac43c2f.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/habitats/host_associated/skeletal_system__5ac43c2f.yaml` | Passed; 1 file scanned, 0 files with errors, 0 error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; expected 3206 records, found 3206 on disk, with 0 missing, 0 extra, and 0 differing. |
| `just report --out /private/tmp/habitatmech-report-bird-skeletal-system.tsv` | Passed; wrote the TSV snapshot and reported `habitatmech:GOLD.3756d4bb39` as `NARROW`, `SEEDED`, 1 source, 0 assertions, no definition, 2 parents, 0 parameters, 0 taxa, and 0 causal graphs. |
| `just worklist --limit 40 --status all --out /private/tmp/habitatmech-worklist-bird-skeletal-system.tsv` | Passed; wrote 953 ungrounded backlog rows. `habitatmech:GOLD.3756d4bb39` is `NARROW`, not `UNGROUNDED`, so it is not a ranked ungrounded item. |
| `git diff --check` | Passed. |

## Identity and Grounding

The generated identity is sound. `data/raw/gold_ecosystem_paths.tsv` has the
exact source row `Host-associated > Birds > Skeletal system` with leaf label
`Skeletal system`, depth 3, three collapsed GOLD ecosystem node IDs, zero
aggregate assertions, and source IDs
`gold.ecosystem:7476|gold.ecosystem:7477|gold.ecosystem:7478`.

`data/habitats/PATHS.tsv` pins `habitatmech:GOLD.3756d4bb39` to the stable
`skeletal_system__5ac43c2f` slug, and the generated target YAML uses that
identifier and slug for exactly this Bird source path.

The `NARROW` grounding against `UBERON:0001434` is appropriate. The vendored
ontology slice labels `UBERON:0001434` as `skeletal system` and defines it as
an anatomical system consisting of the skeleton and the articular system. The
GOLD source path adds the Bird host-clade context, so the record should stay a
minted habitat narrower than the generic UBERON anatomy term rather than
adopting `UBERON:0001434` as an exact identity.

The taxon-neutral `BTO:0001486` `skeletal system` PREGO record is separate. It
has its own exact BTO identity and PREGO taxon attestations, while the reviewed
GOLD record keeps the Bird source-path context as part of its identifier.

The two generated parents are traceable to input data:

| Parent | Support |
|---|---|
| `UBERON:0001434` | The source leaf is a case variant of the UBERON `skeletal system` anatomy label, and the generic anatomy class is broader than this Bird-specific source concept. |
| `habitatmech:GOLD.47e603cf4f` | GOLD has the immediate broader path `Host-associated > Birds`; that generated record is the curated `bird-associated environment` parent. |

The target is also distinct from the other minted host-associated `Skeletal
system` source paths for Fish, Reptilia, Mammals, and Mammals: Human. Those
records preserve their host-branch context in separate `habitatmech:GOLD.*`
identifiers instead of merging onto `UBERON:0001434`.

## Evidence

The record carries no curator-authored evidence block. Its identity is backed
by the GOLD path inventory and the seeder's lexical narrower-than-ontology
route, not by an item-level curation decision.

The zero assertion total is supported by the raw GOLD inventory. The exact raw
row reports `organism_count = 0`, `study_count = 0`, `biosample_count = 0`,
`mixs_triad_count = 0`, `gold_triad_count = 0`, and `total_assertions = 0` for
this path, and ignored/hidden-inclusive exact searches for
`gold.ecosystem:7476`, `gold.ecosystem:7477`, `gold.ecosystem:7478`, and the
exact Bird source path found no rows in `data/raw/gold_path_biosamples.tsv`,
`data/raw/gold_path_triads.tsv`, or `data/raw/gold_studies.tsv`.

No causal graph is attached to this record. Ignored/hidden-inclusive exact
searches found no maintained causal overlay, curation decision, history
record, research report, or configuration row keyed by
`habitatmech:GOLD.3756d4bb39`, `skeletal_system__5ac43c2f`,
`gold.ecosystem:7476`, `gold.ecosystem:7477`, `gold.ecosystem:7478`, or the
exact Bird source path.

## Completeness

- The rendered page
  `pages/habitats/skeletal-system-habitatmech-gold-3756d4bb39.html` reflects
  the same minted identifier, label, category, `NARROW` grounding, `SEEDED`
  mapping status, GOLD source path, collapsed-node note, and two broader
  habitats as the YAML.
- Before this report was added, exact ignored/hidden-inclusive searches found
  no prior exact review report for
  `data/habitats/host_associated/skeletal_system__5ac43c2f.yaml`. The prior
  `reports/yaml_record_review/20260922T062132Z-bone_element.md` report
  references this record only as the immediate GOLD parent of
  `Host-associated > Birds > Skeletal system > Bones`.
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

- `Host-associated > Birds > Skeletal system > Bones` already has an exact
  prior review through `data/habitats/host_associated/bone_element.yaml`; that
  child record remains a separate curated merge into `UBERON:0001474`.
- The ignored/hidden-inclusive exact searches covered `curation`, `history`,
  `research`, `conf`, `data/raw`, `data/habitats`, the generated target page,
  and `reports/yaml_record_review`.
- iModulonDB structured source checks were not applicable: the record names a
  GOLD anatomical habitat path and no genes, locus tags, regulators, pathways,
  stress-response terms, or transcriptomic datasets.
