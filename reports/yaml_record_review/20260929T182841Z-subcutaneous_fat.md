# YAML Record Review: Subcutaneous fat

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/subcutaneous_fat.yaml`
- Started UTC: 2026-09-29T18:28:41Z
- Finished UTC: 2026-09-29T18:28:41Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.18f4c772f7` |
| Label | `Subcutaneous fat` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `NARROW` |
| Mapping status | `SEEDED` |
| Source concept | `Host-associated > Birds > Integumentary system > Adipose tissue > Subcutaneous fat` |
| Maintained owner | Generated from the GOLD path inventory and `data/habitats/PATHS.tsv`; generated YAML remains read-only |
| Locked slug | `data/habitats/PATHS.tsv:1460` maps `habitatmech:GOLD.18f4c772f7` to `subcutaneous_fat` |

This is the generated GOLD record for the bird-specific subcutaneous-fat path.
Its source key is deterministic: `sha1("GOLD:Host-associated > Birds >
Integumentary system > Adipose tissue > Subcutaneous fat")[:10]` is
`18f4c772f7`, matching the generated identifier.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/subcutaneous_fat.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/host_associated/subcutaneous_fat.yaml` | Passed; 1 file scanned, 0 files with errors, 0 total error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the 109-term generated request table is current. |
| `just verify-corpus --max-diffs 1` | Passed; 3,206 expected records, 3,206 found, 0 missing, 0 extra, 0 differing. |
| `just report --ungrounded-top 0 --out /private/var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/habitatmech-report-bird-subcutaneous-fat.tsv` | Passed; wrote `/private/var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/habitatmech-report-bird-subcutaneous-fat.tsv`. |
| `just worklist --limit 40 --status all --out /private/var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/habitatmech-worklist-bird-subcutaneous-fat.tsv` | Passed; wrote `/private/var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/habitatmech-worklist-bird-subcutaneous-fat.tsv`. |

The generated report has a row for `habitatmech:GOLD.18f4c772f7` as a
GOLD-only `NARROW`, `SEEDED` record with one source attestation, no upstream
assertions, no characteristic taxa, no environmental parameters, and no causal
graphs. The target is absent from the all-status ungrounded worklist.

## Identity and Grounding

The record identity is reproducible and internally consistent:

| Raw row | Path | Depth | GOLD node count | Organism count | Study count | Biosample count | Total assertions | GOLD node IDs |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `data/raw/gold_ecosystem_paths.tsv:1882` | `Host-associated > Birds > Integumentary system > Adipose tissue > Subcutaneous fat` | 5 | 1 | 0 | 0 | 0 | 0 | `gold.ecosystem:7463` |

The generated `source_id: gold.ecosystem:7463`, `source_label:
Subcutaneous fat`, and full GOLD source path match that raw row exactly.
Because the row has no upstream organism, study, biosample, or total
assertions, the generated source attestation correctly omits
`assertion_count` and `assertion_unit`.

The ontology parent is appropriate. `data/raw/ontology_terms.tsv:13132`
labels `UBERON:0002190` as `subcutaneous adipose tissue` and lists
`subcutaneous fat` as a synonym. `data/raw/ontology_subclass_edges.tsv:11346`
places it under `UBERON:0001013` / `adipose tissue`, matching the GOLD parent
leaf.

`grounding_status: NARROW` is also appropriate. The GOLD inventory contains
three equal-depth `Subcutaneous fat` leaves under different host branches at
`data/raw/gold_ecosystem_paths.tsv:1882`, `2056`, and `2252`, so the
unqualified UBERON class is broader than any one bird-, mammal-, or
human-scoped GOLD path. HabitatMech's ambiguous-leaf rule keeps the source
concept minted and uses `UBERON:0002190` only as a broader parent.

The generated source-path parent is the expected bird adipose-tissue record:
`data/habitats/host_associated/adipose_tissue__2f4c0234.yaml` represents
`Host-associated > Birds > Integumentary system > Adipose tissue`, is pinned to
`habitatmech:GOLD.7d70febb4c`, and was itself reviewed as a faithful
zero-assertion GOLD parent in
`reports/yaml_record_review/20260923T065349Z-adipose_tissue__2f4c0234.md`.

## Evidence

| Claim | Nearest source | Review |
|---|---|---|
| GOLD contains a bird integumentary-system path labelled `Subcutaneous fat` under `Adipose tissue`. | `data/raw/gold_ecosystem_paths.tsv:1882` | Supported exactly. |
| The path has one GOLD ecosystem node and zero upstream assertions. | `data/raw/gold_ecosystem_paths.tsv:1882` | Supported exactly. |
| `UBERON:0002190` is a valid broader adipose-tissue parent for the leaf string `Subcutaneous fat`. | `data/raw/ontology_terms.tsv:13132`; `data/raw/ontology_subclass_edges.tsv:11346` | Supported exactly. |
| This bird-specific record should not merge directly onto generic `UBERON:0002190`. | Same-depth GOLD sibling rows at `data/raw/gold_ecosystem_paths.tsv:1882`, `2056`, and `2252` | Supported exactly by the source hierarchy and ambiguous-leaf anti-conflation rule. |

Ignored/hidden-inclusive exact searches for
`habitatmech:GOLD.18f4c772f7`, `gold.ecosystem:7463`,
`subcutaneous_fat`, the exact GOLD source path, and `UBERON:0002190` across
`curation/`, `history/`, `research/`, `reports/yaml_record_review/`,
`data/habitats/`, `data/raw/`, and `conf/` found the expected raw GOLD row,
the generated path lock, the generated target, the two other generated
same-label subcutaneous-fat records, and the UBERON ontology rows. They found
no target-specific maintained decision row, term request, curation-history
record, causal overlay, or research report.

Targeted exact searches across `data/raw/gold_path_biosamples.tsv`,
`data/raw/gold_path_triads.tsv`, and `data/raw/gold_studies.tsv` found no
direct rows for this zero-assertion aggregate source path.

The record has no generated characteristic taxa, environmental parameters,
record-level evidence, causal graphs, discussion links, datasets, or quality
flags. Those absences match the source shape: the GOLD path row supplies an
inventory concept with no assertions, no GOLD triads, no PREGO taxa, and no
curated overlay.

iModulonDB was not applicable: the target is a GOLD anatomical habitat, not a
gene, locus tag, UniProt accession, regulator, iModulon, pathway,
stress-response record, or transcriptomics dataset.

Unsupported or over-scoped claims: None found.

## Completeness

The generated record is complete for `data/raw/gold_ecosystem_paths.tsv:1882`:
it carries the source-specific minted identity, the broader
`UBERON:0002190` ontology parent, the bird adipose-tissue source-path parent,
the exact representative GOLD source node, `skos:narrowMatch`, and the full
GOLD source path.

No curated term request or definition is expected because the source concept
already has a valid broader ontology anchor in `UBERON:0002190`. No causal
graph is expected because this is a generated seed record and the repository
requires independent literature evidence before mechanism edges can be
authored.

## Findings

None found.

No blocker findings.

No major findings.

No minor findings.

## Recommended Edits

None required.

If a future curator wants to promote this seeded GOLD record to reviewed
status, add an item-level `GROUND_AS_PARENT` row for
`habitatmech:GOLD.18f4c772f7` in `curation/decisions.tsv`. That should be a
status-only change: keep the identifier minted, keep `UBERON:0002190` and
`habitatmech:GOLD.7d70febb4c` as broader parents, and keep the GOLD
attestation unchanged unless `data/raw/gold_ecosystem_paths.tsv` changes
upstream.

## Follow-up Checks

None required beyond the validators already run for this report.

For any future status-only review row, run:

- `just seed`
- `just seed-canary habitatmech:GOLD.18f4c772f7`
- `just validate data/habitats/host_associated/subcutaneous_fat.yaml`
- `just validate-strict data/habitats/host_associated/subcutaneous_fat.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 40 --status all`
- `just report --ungrounded-top 0`
- `git diff --check`

## Additional Notes

A `find` filename search under `reports/yaml_record_review/`,
`research/habitats/`, `history/`, and `curation/causal_graphs/` included
ignored files and found no prior `subcutaneous_fat` review, target-specific
research report, history record, or causal overlay.

Exact hidden/ignored-inclusive content searches for
`habitatmech:GOLD.18f4c772f7`, `subcutaneous_fat`, the exact GOLD source path,
`gold.ecosystem:7463`, and `UBERON:0002190` found the cited raw, path-lock,
ontology, and generated-record rows, and no target-specific curated input
rows.
