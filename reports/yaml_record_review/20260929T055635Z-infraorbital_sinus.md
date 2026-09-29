# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/infraorbital_sinus.yaml`
- Started UTC: 2026-09-29T05:48:10Z
- Finished UTC: 2026-09-29T05:56:35Z
- Verdict: pass with minor issues

## Target

`data/habitats/host_associated/infraorbital_sinus.yaml` is a generated,
UBERON-grounded GOLD record:

| Field | Value |
|---|---|
| Identifier | `UBERON:0011985` |
| Label | `infraorbital sinus` |
| Definition source | `UBERON` |
| Habitat category | `HOST_ASSOCIATED` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |
| Parents | `UBERON:0001825`, `habitatmech:GOLD.0c74807e42` |
| Source | `GOLD`, `gold.ecosystem:7447`, `Host-associated > Birds > Respiratory system > Infraorbital sinus` |

The exact GOLD source concept is `habitatmech:GOLD.1673eaaf3d`, the content hash
of `GOLD:Host-associated > Birds > Respiratory system > Infraorbital sinus`.
The generated URL slug is pinned at `data/habitats/PATHS.tsv:1129`.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/infraorbital_sinus.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/host_associated/infraorbital_sinus.yaml` | Passed; 1 file scanned, 0 files with errors, 0 error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the 109-term generated request table is current. |
| `just verify-corpus` | Passed; 3,206 expected records, 3,206 found, 0 missing, 0 extra, 0 differing. |
| `just report --out /tmp/habitatmech-report-infraorbital-sinus.tsv` | Passed; wrote `/tmp/habitatmech-report-infraorbital-sinus.tsv`. |
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist-infraorbital-sinus.tsv` | Passed; wrote 953 ungrounded rows to `/tmp/habitatmech-worklist-infraorbital-sinus.tsv`. |

`/tmp/habitatmech-report-infraorbital-sinus.tsv` confirms this record is
GOLD-only, `EXACT`, `SEEDED`, backed by one source attestation with one
organism assertion, and generated at
`data/habitats/host_associated/infraorbital_sinus.yaml`. The target is absent
from the all-status ungrounded worklist.

## Identity and Grounding

The record identity and exact grounding agree. In the committed GOLD inventory,
the path has two GOLD ecosystem nodes, one organism assertion, no study
assertions, no biosample assertions, and one total assertion:

| Raw row | Path | Depth | GOLD node count | Organism count | Study count | Biosample count | Total assertions | GOLD node IDs |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `data/raw/gold_ecosystem_paths.tsv:1030` | `Host-associated > Birds > Respiratory system > Infraorbital sinus` | 4 | 2 | 1 | 0 | 0 | 1 | `gold.ecosystem:7447|gold.ecosystem:7448` |

The vendored ontology target matches the GOLD path. In
`data/raw/ontology_terms.tsv:13437`, `UBERON:0011985` is labeled
`infraorbital sinus`, defined as an air-filled recess in the head of birds
lateral to and opening into the nasal cavity, carries the exact UBERON synonym
`sinus infraorbitalis`, and is not deprecated.
`data/raw/ontology_subclass_edges.tsv:11736` contains the direct subclass edge
from `UBERON:0011985` to the generated ontology parent `UBERON:0001825` /
`paranasal sinus`.

The source-path parent is `habitatmech:GOLD.0c74807e42`, GOLD's
`Host-associated > Birds > Respiratory system` concept. It is strictly broader
source context for the avian Infraorbital sinus leaf.

## Evidence

The full GOLD path supplies the avian respiratory-system context for the leaf
label `Infraorbital sinus`. The UBERON target supplies a matching definition
and direct ontology parent for the generated record.

Exact hidden/ignored-inclusive searches for `habitatmech:GOLD.1673eaaf3d`,
`gold.ecosystem:7447`, `gold.ecosystem:7448`, `Host-associated > Birds >
Respiratory system > Infraorbital sinus`, and `infraorbital_sinus` across
`curation/`, `history/`, `research/`, `reports/yaml_record_review/`, `conf/`,
`data/raw/`, and `data/habitats/`, excluding only generated `data/text_map/`
and `pages/`, found the expected raw GOLD row, the generated YAML, and the
generated slug. They found no target-specific item-level decision,
append-only history record, causal overlay, or prior YAML-record review.

The record has no generated characteristic taxa, environmental parameters,
curator evidence objects, or causal edges. That is appropriate here: the
GOLD row contributes source occurrence counts, but not a curated claim that
any taxon is characteristic of the infraorbital sinus habitat.

iModulonDB was not applicable: the target is a GOLD anatomical habitat, not a
gene, locus tag, UniProt accession, regulator, iModulon, pathway,
stress-response record, or transcriptomics dataset.

## Completeness

The record is complete enough for its current GOLD and UBERON inputs. It keeps
the exact ontology grounding, the ontology definition, the direct ontology
parent, the broader GOLD respiratory-system parent, and the source attestation
count and unit.

The remaining gap is provenance depth: no `curation/decisions.tsv` row records
the exact `habitatmech:GOLD.1673eaaf3d` judgement at item level, so the
generated record remains `mapping_status: SEEDED`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Minor | The exact GOLD source concept has not received item-level grounding review. | Exact hidden/ignored-inclusive searches for `habitatmech:GOLD.1673eaaf3d`, `gold.ecosystem:7447`, `gold.ecosystem:7448`, and the full GOLD source path found no `curation/decisions.tsv` row or history record for this source concept, and the generated record remains `mapping_status: SEEDED`. The current `UBERON:0011985` exact grounding itself is supported by the full GOLD path and the vendored ontology row. | `curation/decisions.tsv` |

## Recommended Edits

1. Add an item-level `GROUND` row for `habitatmech:GOLD.1673eaaf3d` to
   `curation/decisions.tsv`, with `object_id: UBERON:0011985`, `object_label:
   infraorbital sinus`, `grounding_status: EXACT`, and `review_depth: ITEM`.
   Its notes should record that the full GOLD path names the avian
   respiratory-system infraorbital sinus.
2. Rerun `just seed`, canary
   `data/habitats/host_associated/infraorbital_sinus.yaml`, and apply the
   generated corpus update. The regenerated record should stay exact-grounded
   to `UBERON:0011985` and move from `SEEDED` to `REVIEWED`.

## Follow-up Checks

| Follow-up | Purpose |
|---|---|
| `just validate data/habitats/host_associated/infraorbital_sinus.yaml` | Validate the regenerated target shape. |
| `just validate-strict data/habitats/host_associated/infraorbital_sinus.yaml` | Confirm the regenerated target is still closed-schema valid. |
| `just verify-corpus` | Prove the maintained `curation/decisions.tsv` row reproduces the generated habitat record. |
| `just report --out /tmp/habitatmech-report-after-infraorbital-sinus.tsv` | Confirm the regenerated target becomes `REVIEWED` while retaining `EXACT` grounding. |

## Additional Notes

The current record has no blocker or major issue. It is a faithful generated
projection of a two-node, one-assertion GOLD path onto a matching UBERON
anatomical habitat.
