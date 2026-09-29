# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/respiratory_system__431eac8d.yaml`
- Started UTC: 2026-09-29T06:05:00Z
- Finished UTC: 2026-09-29T06:27:58Z
- Verdict: pass with minor issues

## Target

`data/habitats/host_associated/respiratory_system__431eac8d.yaml` is a
generated, minted GOLD record:

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.0c74807e42` |
| Label | `Respiratory system` |
| Definition source | None |
| Habitat category | `HOST_ASSOCIATED` |
| Grounding | `NARROW` |
| Mapping status | `SEEDED` |
| Parents | `UBERON:0001004`, `habitatmech:GOLD.47e603cf4f` |
| Source | `GOLD`, `gold.ecosystem:3600`, `Host-associated > Birds > Respiratory system` |

`habitatmech:GOLD.0c74807e42` is the first 10 hex characters of the SHA-1 for
`GOLD:Host-associated > Birds > Respiratory system`; the local checksum is
`0c74807e42af1a497e2dbd96b60d2988171226ed`. The generated URL slug is pinned
at `data/habitats/PATHS.tsv:1366`.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/respiratory_system__431eac8d.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/host_associated/respiratory_system__431eac8d.yaml` | Passed; 1 file scanned, 0 files with errors, 0 error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the 109-term generated request table is current. |
| `just verify-corpus` | Passed; 3,206 expected records, 3,206 found, 0 missing, 0 extra, 0 differing. |
| `just report --out /tmp/habitatmech-report-respiratory-system-431eac8d.tsv` | Passed; wrote `/tmp/habitatmech-report-respiratory-system-431eac8d.tsv`. |
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist-respiratory-system-431eac8d.tsv` | Passed; wrote 953 ungrounded rows to `/tmp/habitatmech-worklist-respiratory-system-431eac8d.tsv`. |
| `git diff --check` | Passed. |

`/tmp/habitatmech-report-respiratory-system-431eac8d.tsv` confirms this record
is GOLD-only, `NARROW`, `SEEDED`, backed by one source attestation with 53
organism assertions, and generated at
`data/habitats/host_associated/respiratory_system__431eac8d.yaml`. The target
is absent from the all-status ungrounded worklist.

## Identity and Grounding

The record identity and narrow grounding agree. In the committed GOLD
inventory, the exact path has three GOLD ecosystem nodes, 53 organism
assertions, no study assertions, no biosample assertions, and 53 total
assertions:

| Raw row | Path | Depth | GOLD node count | Organism count | Study count | Biosample count | Total assertions | GOLD node IDs |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `data/raw/gold_ecosystem_paths.tsv:299` | `Host-associated > Birds > Respiratory system` | 3 | 3 | 53 | 0 | 0 | 53 | `gold.ecosystem:3600\|gold.ecosystem:3715\|gold.ecosystem:4155` |

The vendored ontology parent is the expected broader anatomy term.
`data/raw/ontology_terms.tsv:12987` has `UBERON:0001004` labeled
`respiratory system`, defines it as a functional system consisting of
structures involved in respiration, carries exact respiratory-system synonyms,
and is not deprecated.

The generated source-path parent is also sound:
`habitatmech:GOLD.47e603cf4f` is the reviewed `bird-associated environment`
record. Its maintained `curation/decisions.tsv:479` row confirms the root GOLD
`Host-associated > Birds` concept remains minted and ungrounded while using
`ENVO:01001002` only as a broader animal-associated parent.

## Evidence

The full GOLD path supports the label and avian host context exactly. The
`Respiratory system` leaf under `Host-associated > Birds` denotes the avian
respiratory-system branch rather than the taxon-neutral UBERON class itself,
so keeping the record minted and placing `UBERON:0001004` in
`parent_habitats` is the appropriate generated shape.

Exact hidden/ignored-inclusive searches for `habitatmech:GOLD.0c74807e42`,
`gold.ecosystem:3600`, `gold.ecosystem:3715`, `gold.ecosystem:4155`,
`respiratory_system__431eac8d`, and the exact GOLD source path across
`curation/`, `history/`, `research/`, `reports/yaml_record_review/`,
`data/habitats/`, `data/raw/`, and `conf/`, excluding only generated
`data/text_map/` and `pages/`, found the expected raw GOLD row, the generated
path lock, the generated target, child records that inherit this source-path
parent, and contextual mentions in prior child-record reviews. They found no
item-level decision row, append-only history record, causal overlay, or prior
exact review report for this target source concept.

The record has no generated characteristic taxa, environmental parameters,
curator evidence objects, or causal edges. That is appropriate here: the 53
GOLD organism assertions are source occurrence counts, not a curated claim
that any taxon is characteristic of this habitat.

iModulonDB was not applicable: the target is a GOLD anatomical habitat, not a
gene, locus tag, UniProt accession, regulator, iModulon, pathway,
stress-response record, or transcriptomics dataset.

## Completeness

The record is complete enough for its current generated inputs. It preserves
the source-specific GOLD identity, the broader UBERON respiratory-system
parent, the reviewed bird-associated source-path parent, and the source
attestation count and unit.

The remaining gap is provenance depth: no `curation/decisions.tsv` row records
the broader `UBERON:0001004` judgement at item level, so the generated record
remains `mapping_status: SEEDED`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Minor | The GOLD source concept has not received item-level grounding review. | Exact hidden/ignored-inclusive searches for `habitatmech:GOLD.0c74807e42`, the three GOLD node ids, the path-locked slug, and the full GOLD source path found no maintained decision or history record for this source concept, and the generated record remains `mapping_status: SEEDED`. The current `UBERON:0001004` parent itself is supported by the full GOLD path and the vendored ontology row. | `curation/decisions.tsv` |

## Recommended Edits

1. Add an item-level `GROUND_AS_PARENT` row for
   `habitatmech:GOLD.0c74807e42` to `curation/decisions.tsv`, with
   `object_id: UBERON:0001004`, `object_label: respiratory system`,
   `grounding_status: NARROW`, and `review_depth: ITEM`. The notes should
   record that GOLD's `Host-associated > Birds > Respiratory system` source
   concept is an avian branch for which the taxon-neutral UBERON term is
   broader, not identical.
2. Add the corresponding append-only curation history record under `history/`,
   then rerun `just seed`, canary
   `data/habitats/host_associated/respiratory_system__431eac8d.yaml`, and
   apply the generated corpus update. The regenerated record should stay
   minted as `habitatmech:GOLD.0c74807e42`, retain `UBERON:0001004` and
   `habitatmech:GOLD.47e603cf4f` as parents, and move from `SEEDED` to
   `REVIEWED`.

## Follow-up Checks

| Follow-up | Purpose |
|---|---|
| `just validate data/habitats/host_associated/respiratory_system__431eac8d.yaml` | Validate the regenerated target shape. |
| `just validate-strict data/habitats/host_associated/respiratory_system__431eac8d.yaml` | Confirm the regenerated target is still closed-schema valid. |
| `just validate-history` | Confirm the new curation-history record is valid. |
| `just verify-corpus` | Prove the maintained `curation/decisions.tsv` row and history record reproduce the generated habitat record. |
| `just report --out /tmp/habitatmech-report-after-respiratory-system-431eac8d.tsv` | Confirm the regenerated target becomes `REVIEWED` while retaining `NARROW` grounding. |

## Additional Notes

The current record has no blocker or major issue. It is a faithful generated
projection of a three-node, 53-organism GOLD branch under the reviewed
bird-associated environment record.

A `find` filename search under `reports/yaml_record_review/` and
`research/habitats/` included ignored files and found no prior
`respiratory_system__431eac8d` review or target-specific respiratory-system
research report.
