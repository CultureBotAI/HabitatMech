# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/integumentary_system__e212bc7d.yaml`
- Started UTC: 2026-09-29T18:08:22Z
- Finished UTC: 2026-09-29T18:08:22Z
- Verdict: pass with minor issues

## Target

`data/habitats/host_associated/integumentary_system__e212bc7d.yaml` is a
generated, minted GOLD record:

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.968051b240` |
| Label | `Integumentary system` |
| Definition source | None |
| Habitat category | `HOST_ASSOCIATED` |
| Grounding | `NARROW` |
| Mapping status | `SEEDED` |
| Parents | `UBERON:0002416`, `habitatmech:GOLD.47e603cf4f` |
| Source | `GOLD`, `gold.ecosystem:6903`, `Host-associated > Birds > Integumentary system` |

`habitatmech:GOLD.968051b240` is the first 10 hex characters of the SHA-1 for
`GOLD:Host-associated > Birds > Integumentary system`; the local checksum is
`968051b240e5656b80c32b1f2b6fd4143b482bf8`. The generated URL slug is pinned
at `data/habitats/PATHS.tsv:2402`.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/integumentary_system__e212bc7d.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/host_associated/integumentary_system__e212bc7d.yaml` | Passed; 1 file scanned, 0 files with errors, 0 total error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the 109-term generated request table is current. |
| `just verify-corpus --max-diffs 1` | Passed; 3,206 expected records, 3,206 found, 0 missing, 0 extra, 0 differing. |
| `just report --ungrounded-top 0 --out /private/var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/habitatmech-report-bird-integumentary-system.tsv` | Passed; wrote `/private/var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/habitatmech-report-bird-integumentary-system.tsv`. |
| `just worklist --limit 40 --status all --out /private/var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/habitatmech-worklist-bird-integumentary-system.tsv` | Passed; wrote `/private/var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/habitatmech-worklist-bird-integumentary-system.tsv`. |

The generated report has a row for `habitatmech:GOLD.968051b240` as a
GOLD-only `NARROW`, `SEEDED` record with one source attestation, no upstream
assertions, no characteristic taxa, no environmental parameters, and no causal
graphs. The target is absent from the all-status ungrounded worklist.

## Identity and Grounding

The record identity and narrow grounding agree. In the committed GOLD
inventory, the exact path has three GOLD ecosystem nodes and no organism,
study, biosample, or total assertions:

| Raw row | Path | Depth | GOLD node count | Organism count | Study count | Biosample count | Total assertions | GOLD node IDs |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `data/raw/gold_ecosystem_paths.tsv:1880` | `Host-associated > Birds > Integumentary system` | 3 | 3 | 0 | 0 | 0 | 0 | `gold.ecosystem:6903`, `gold.ecosystem:7451`, `gold.ecosystem:7452` |

The vendored ontology parent is the expected broader animal anatomy term.
`data/raw/ontology_terms.tsv:13160` has `UBERON:0002416` labeled
`integumental system`, defines it as a connected anatomical system forming a
barrier between an animal and its environment, and gives `integumentary
system` as an exact synonym. `data/raw/ontology_subclass_edges.tsv:11391`
places it under `UBERON:0000467`.

The source-path parent is also sound: `habitatmech:GOLD.47e603cf4f` is the
reviewed `bird-associated environment` record. Its maintained
`curation/decisions.tsv:479` and `curation/term_requests.tsv:6` rows keep the
root `Host-associated > Birds` concept minted, define it as
`bird-associated environment`, and use `ENVO:01001002` only as a broader
animal-associated parent to avoid merging every host clade onto one record.

## Evidence

The full GOLD path supports the label and avian host context exactly. The
`Integumentary system` leaf under `Host-associated > Birds` denotes the avian
integumentary-system branch rather than the taxon-neutral UBERON class itself,
so keeping the record minted and placing `UBERON:0002416` in
`parent_habitats` is the appropriate generated shape.

The `UBERON:0002416` parent is host-appropriate here. The slice also contains
an animal/plant false-match correction for
`Host-associated > Plants > Phyllosphere > Surface`, where `surface` matched a
synonym of `UBERON:0002416`; that correction rejects `UBERON:0002416` for an
aerial plant surface. This record is different: GOLD's source path is the
bird-specific `Integumentary system` branch, so the animal anatomy term is in
the right kingdom and at the right organ-system level.

Generated child records corroborate the parent branch. Bird `Skin`,
`Adipose tissue`, `Claws/Talon`, and `Uropygial/Preen gland` records inherit
`habitatmech:GOLD.968051b240` as their GOLD source-path parent. The
`Claws/Talon` and `Uropygial/Preen gland` children also already have
item-level exact grounding decisions in `curation/decisions.tsv`, which is
consistent with the parent branch being a real avian integumentary subtree
rather than an orphan label.

Exact hidden/ignored-inclusive searches for `habitatmech:GOLD.968051b240`,
`integumentary_system__e212bc7d`, `gold.ecosystem:6903`,
`gold.ecosystem:7451`, `gold.ecosystem:7452`,
`Host-associated > Birds > Integumentary system`, and `UBERON:0002416`
across `curation/`, `history/`, `research/`, `reports/yaml_record_review/`,
`data/habitats/`, `data/raw/`, and `conf/` found the expected raw GOLD row,
the generated path lock, the generated target, generated child records that
inherit this source-path parent, the UBERON ontology rows, and contextual
mentions in prior child-record reviews. Targeted exact searches across the
GOLD biosample, triad, and study side tables found no direct rows for this
zero-assertion aggregate source path.

The record has no generated characteristic taxa, environmental parameters,
curator evidence objects, or causal edges. That is appropriate here: the raw
GOLD row carries no upstream organism, study, biosample, or total assertions.

iModulonDB was not applicable: the target is a GOLD anatomical habitat, not a
gene, locus tag, UniProt accession, regulator, iModulon, pathway,
stress-response record, or transcriptomics dataset.

## Completeness

The record is complete enough for its current generated inputs. It preserves
the source-specific GOLD identity, the broader UBERON integumental-system
parent, the reviewed bird-associated source-path parent, and the complete GOLD
attestation. Because all upstream assertion counts are zero, the source
attestation correctly omits `assertion_count` and `assertion_unit`.

The remaining gap is provenance depth: no `curation/decisions.tsv` row records
the broader `UBERON:0002416` judgment at item level, so the generated record
remains `mapping_status: SEEDED`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Minor | The GOLD source concept has not received item-level grounding review. | Exact hidden/ignored-inclusive searches for `habitatmech:GOLD.968051b240`, the three GOLD node IDs, the path-locked slug, and the full GOLD source path found no maintained decision or history record for this source concept, and the generated record remains `mapping_status: SEEDED`. The current `UBERON:0002416` parent itself is supported by the full GOLD path and the vendored ontology row. | `curation/decisions.tsv` |

## Recommended Edits

1. Add an item-level `GROUND_AS_PARENT` row for
   `habitatmech:GOLD.968051b240` to `curation/decisions.tsv`, with
   `object_id: UBERON:0002416`, `object_label: integumental system`,
   `grounding_status: NARROW`, and `review_depth: ITEM`. The notes should
   record that GOLD's `Host-associated > Birds > Integumentary system` source
   concept is an avian branch for which the taxon-neutral UBERON term is
   broader, not identical.
2. Add the corresponding append-only curation history record under `history/`,
   then rerun `just seed`, canary
   `data/habitats/host_associated/integumentary_system__e212bc7d.yaml`, and
   apply the generated corpus update. The regenerated record should stay
   minted as `habitatmech:GOLD.968051b240`, retain `UBERON:0002416` and
   `habitatmech:GOLD.47e603cf4f` as parents, and move from `SEEDED` to
   `REVIEWED`.

## Follow-up Checks

| Follow-up | Purpose |
|---|---|
| `just validate data/habitats/host_associated/integumentary_system__e212bc7d.yaml` | Validate the regenerated target shape. |
| `just validate-strict data/habitats/host_associated/integumentary_system__e212bc7d.yaml` | Confirm the regenerated target is still closed-schema valid. |
| `just validate-history` | Confirm the new curation-history record is valid. |
| `just verify-corpus --max-diffs 1` | Prove the maintained `curation/decisions.tsv` row and history record reproduce the generated habitat record. |
| `just report --out /tmp/habitatmech-report-after-bird-integumentary-system.tsv` | Confirm the regenerated target becomes `REVIEWED` while retaining `NARROW` grounding. |

## Additional Notes

The current record has no blocker or major issue. It is a faithful generated
projection of a three-node, zero-assertion GOLD branch under the reviewed
bird-associated environment record.

A `find` filename search under `reports/yaml_record_review/`,
`research/habitats/`, `history/`, and `curation/causal_graphs/` included
ignored files and found no prior `integumentary_system__e212bc7d` review,
target-specific research report, history record, or causal overlay.

Exact hidden/ignored-inclusive content searches for
`habitatmech:GOLD.968051b240`, `integumentary_system__e212bc7d`, the exact
GOLD source path, `gold.ecosystem:6903`, `gold.ecosystem:7451`,
`gold.ecosystem:7452`, and `UBERON:0002416` found the cited raw, path-lock,
ontology, and generated-record rows, and no target-specific curated input
rows.
