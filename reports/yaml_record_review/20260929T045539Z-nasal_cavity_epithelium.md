# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/nasal_cavity_epithelium.yaml`
- Started UTC: 2026-09-29T04:43:00Z
- Finished UTC: 2026-09-29T04:55:39Z
- Verdict: pass with minor issues

## Target

`data/habitats/host_associated/nasal_cavity_epithelium.yaml` is a generated,
UBERON-grounded GOLD record:

| Field | Value |
|---|---|
| Identifier | `UBERON:0005384` |
| Label | `nasal cavity epithelium` |
| Definition source | `UBERON` |
| Habitat category | `HOST_ASSOCIATED` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |
| Parents | `UBERON:0003350`, `UBERON:0004814`, `UBERON:0019306`, `habitatmech:GOLD.f3560ae8d1` |
| Source | `GOLD`, `gold.ecosystem:7446`, `Host-associated > Birds > Respiratory system > Nasal cavity > Epithelium` |

The exact GOLD source concept is `habitatmech:GOLD.05469f9598`, the content hash
of `GOLD:Host-associated > Birds > Respiratory system > Nasal cavity >
Epithelium`. The generated URL slug is pinned at `data/habitats/PATHS.tsv:1088`.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/nasal_cavity_epithelium.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/host_associated/nasal_cavity_epithelium.yaml` | Passed; 1 file scanned, 0 files with errors, 0 error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the 109-term generated request table is current. |
| `just verify-corpus` | Passed; 3,206 expected records, 3,206 found, 0 missing, 0 extra, 0 differing. |
| `just report --out /tmp/habitatmech-report-nasal-cavity-epithelium.tsv` | Passed; wrote `/tmp/habitatmech-report-nasal-cavity-epithelium.tsv`. |
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist-nasal-cavity-epithelium.tsv` | Passed; wrote 953 ungrounded rows to `/tmp/habitatmech-worklist-nasal-cavity-epithelium.tsv`. |

`/tmp/habitatmech-report-nasal-cavity-epithelium.tsv` confirms this record is
GOLD-only, `EXACT`, `SEEDED`, backed by one source attestation, and generated
at `data/habitats/host_associated/nasal_cavity_epithelium.yaml`. The exact
record and source concept are absent from the all-status ungrounded worklist.

## Identity and Grounding

The record identity and exact grounding agree. The target denotes the
epithelium child of GOLD's `Host-associated > Birds > Respiratory system >
Nasal cavity` path. In the committed GOLD inventory, that path has one GOLD
node, zero organism assertions, zero studies, zero biosamples, and zero total
assertions:

| Raw row | Path | Depth | GOLD node count | Organism count | Study count | Biosample count | Total assertions | GOLD node IDs |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `data/raw/gold_ecosystem_paths.tsv:1902` | `Host-associated > Birds > Respiratory system > Nasal cavity > Epithelium` | 5 | 1 | 0 | 0 | 0 | 0 | `gold.ecosystem:7446` |

The vendored ontology slice supports the generated target. In
`data/raw/ontology_terms.tsv:13275`, `UBERON:0005384` is labeled `nasal cavity
epithelium`, is defined as an epithelium that lines the nasal cavity, carries
the exact UBERON synonyms `nasal epithelium` and `nasal mucosa`, and is not
deprecated. `data/raw/ontology_subclass_edges.tsv:11532-11534` contains direct
subclass edges from `UBERON:0005384` to the three generated ontology parents:
`UBERON:0003350`, `UBERON:0004814`, and `UBERON:0019306`.

The source-path parent is also strictly broader. `habitatmech:GOLD.f3560ae8d1`
denotes GOLD's `Host-associated > Birds > Respiratory system > Nasal cavity`
path and is generated as a narrow record under `UBERON:0001707` / `nasal
cavity` plus its GOLD respiratory-system parent.

## Evidence

The full GOLD path supplies the nasal-cavity context that is missing from the
leaf label `Epithelium`. The UBERON target supplies a matching definition and
direct ontology parents for the generated record.

Exact hidden/ignored-inclusive searches for `habitatmech:GOLD.05469f9598`,
`gold.ecosystem:7446`, `Host-associated > Birds > Respiratory system > Nasal
cavity > Epithelium`, and `nasal_cavity_epithelium` across `data/raw/`,
`curation/`, `history/`, `research/`, `reports/yaml_record_review/`, `conf/`,
`data/habitats/`, and `data/habitats/PATHS.tsv`, excluding only generated
`data/text_map/` and `pages/`, found the raw GOLD row, the generated YAML, and
the generated slug. They found no target-specific item-level decision, history
record, research report, causal overlay, or prior YAML-record review.

The record has no generated characteristic taxa, environmental parameters,
curator evidence objects, or causal edges, which is appropriate for a
zero-assertion GOLD leaf.

iModulonDB was not applicable: the target is a GOLD anatomical habitat, not a
gene, locus tag, UniProt accession, regulator, iModulon, pathway,
stress-response record, or transcriptomics dataset.

## Completeness

The record is complete enough for its current GOLD and UBERON inputs. It keeps
the exact ontology grounding, the ontology definition, all direct ontology
parents, and the stricter GOLD source-path parent, and it does not invent taxa,
physicochemical parameters, or mechanism evidence.

The remaining gap is provenance depth: no `curation/decisions.tsv` row records
the exact `habitatmech:GOLD.05469f9598` judgement at item level, so the
generated record remains `mapping_status: SEEDED`.

The vendored UBERON target exports `nasal mucosa` as an exact synonym for
`UBERON:0005384`, while HabitatMech also contains a separate generated
`data/habitats/host_associated/nasal_mucosa.yaml` record exact-mapped to
`BTO:0000912` from the human GOLD path `Host-associated > Mammals: Human >
Respiratory system > Nasal cavity > Nasal mucosa`. That does not make this
avian epithelium record the wrong entity, but it is worth keeping in mind if
the project later adds maintained synonym filtering for ontology-exported
synonyms.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Minor | The exact GOLD source concept has not received item-level grounding review. | Exact hidden/ignored-inclusive searches for `habitatmech:GOLD.05469f9598`, `gold.ecosystem:7446`, and the full GOLD source path found no `curation/decisions.tsv` row or history record for this source concept, and the generated record remains `mapping_status: SEEDED`. The current `UBERON:0005384` exact grounding itself is supported by the full GOLD path and the vendored ontology row. | `curation/decisions.tsv` |

## Recommended Edits

1. Add an item-level `GROUND` row for `habitatmech:GOLD.05469f9598` to
   `curation/decisions.tsv`, with `object_id: UBERON:0005384`, `object_label:
   nasal cavity epithelium`, `grounding_status: EXACT`, and `review_depth:
   ITEM`. Its notes should record that the full GOLD path narrows the generic
   `Epithelium` leaf label to an epithelium lining the nasal cavity.
2. Rerun `just seed`, canary
   `data/habitats/host_associated/nasal_cavity_epithelium.yaml`, and apply the
   generated corpus update. The regenerated record should stay exact-grounded
   to `UBERON:0005384` and move from `SEEDED` to `REVIEWED`.

## Follow-up Checks

| Follow-up | Purpose |
|---|---|
| `just validate data/habitats/host_associated/nasal_cavity_epithelium.yaml` | Validate the regenerated target shape. |
| `just validate-strict data/habitats/host_associated/nasal_cavity_epithelium.yaml` | Confirm the regenerated target is still closed-schema valid. |
| `just verify-corpus` | Prove the maintained `curation/decisions.tsv` row reproduces the generated habitat record. |
| `just report --out /tmp/habitatmech-report-after-nasal-cavity-epithelium.tsv` | Confirm the regenerated target becomes `REVIEWED` while retaining `EXACT` grounding. |

## Additional Notes

The current record has no blocker or major issue. It is a faithful generated
projection of a one-node, zero-assertion GOLD path onto a matching UBERON
anatomical habitat.
