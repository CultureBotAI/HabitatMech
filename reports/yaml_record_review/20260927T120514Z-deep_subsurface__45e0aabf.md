# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/aquatic/deep_subsurface__45e0aabf.yaml`
- Started UTC: `2026-09-27T12:05:14Z`
- Finished UTC: `2026-09-27T12:05:14Z`
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/aquatic/deep_subsurface__45e0aabf.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.21222434e2` |
| Label | `Deep subsurface` |
| Category | `AQUATIC` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Source provenance | GOLD `Environmental > Aquatic > Deep subsurface` |
| Generated status | Generated from `data/raw/`, `curation/decisions.tsv`, and `src/habitatmech/seed.py`; `data/habitats/PATHS.tsv` pins `habitatmech:GOLD.21222434e2` to `deep_subsurface__45e0aabf` |

The complete generated record was read before making this judgment. It contains
a minted GOLD identifier, one parent, one GOLD source attestation, and two
curation-history events. It has no definition, synonyms, xrefs, record-level
evidence, environmental parameters, characteristic taxa, causal graphs,
discussion links, external datasets, or quality flags.

Ignored-inclusive exact searches over `data/raw`, `data/habitats`,
`curation`, `history`, `research`, `reports`, and `conf` for
`habitatmech:GOLD.21222434e2`, `gold.ecosystem:5952`, and the exact
`Environmental > Aquatic > Deep subsurface` source path found the expected
GOLD raw row, `curation/decisions.tsv` class-level decision, `PATHS.tsv` pin,
generated target, and generated child references from deeper GOLD paths. The
same searches found no term-request row, causal-graph overlay, history entry,
research report, GOLD biosample row, GOLD MIxS triad row, exact-path GOLD study
row, or prior YAML review report for this source concept. Those
`rg --no-ignore --hidden` checks included ignored and hidden files.

Two other generated GOLD records have the same leaf label but are distinct
source concepts: `Environmental > Aquatic > Marine > Deep subsurface` is
`habitatmech:GOLD.3841c9c3af`, and `Environmental > Terrestrial > Deep
subsurface` is `habitatmech:GOLD.151ba43519`. This review covers only
`data/habitats/aquatic/deep_subsurface__45e0aabf.yaml`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/deep_subsurface__45e0aabf.yaml` | Passed; LinkML reported no issues. |
| `just validate-all data/habitats/aquatic/deep_subsurface__45e0aabf.yaml --out /tmp/habitatmech-deep-subsurface-45e0aabf-validate-all.tsv` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just validate-strict data/habitats/aquatic/deep_subsurface__45e0aabf.yaml --quiet --out /tmp/habitatmech-deep-subsurface-45e0aabf-validate-strict.tsv` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs were valid. |
| `just validate-history` | Passed; 77 history records were valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; the corpus has the expected 3206 records and reproduces exactly from `data/raw/`. |
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist-deep-subsurface-45e0aabf.tsv` | Passed; wrote 953 ungrounded rows and reported 1810 decisions on file. |
| `just report` | Passed; emitted the corpus diagnostic report for 3206 records, including 468 `AQUATIC` records, 2520 `SEEDED` records, 953 `UNGROUNDED` records, and 830 class-level swept ungrounded records. |
| Focused reference validator | Not checked: an ignored-inclusive exact `rg` search of `justfile`, `.claude`, `docs`, `scripts`, `src`, and `tests` found no `validate-references` command, and this record has no evidence references or causal graph edges. |

## Identity and Grounding

The source identity is supported. `data/raw/gold_ecosystem_paths.tsv` has one
canonical path row for `Environmental > Aquatic > Deep subsurface`, with leaf
label `Deep subsurface`, depth 3, three collapsed GOLD node IDs
`gold.ecosystem:5952|gold.ecosystem:8301|gold.ecosystem:8302`, and seven
`ORGANISM` assertions. The seeder's `mint` helper returns
`habitatmech:GOLD.21222434e2` for that exact source path, matching the
generated identifier.

The single source attestation is also supported. The generated
`source_id: gold.ecosystem:5952` is the first of the three collapsed node IDs,
the generated `source_label` and `source_path` match the raw path, the note
correctly reports that three node IDs share the path, and
`assertion_count: 7` with `assertion_unit: ORGANISM` matches the raw
`organism_count`.

The generated `grounding_status: UNGROUNDED` and `mapping_status: SEEDED`
follow from the class-level `CONFIRM_UNGROUNDED` row in
`curation/decisions.tsv`. That row records a lexical no-match sweep, not an
item-level habitat review, so the source concept remains in the worklist and
is correctly not promoted to `REVIEWED`. The worklist still surfaces only an
irrelevant lexical candidate, `UBERON:0010409` `eye surface`, for this target.

The current sole parent is not supported as a strict broader habitat.
`ENVO:00002030` is the record for ENVO `aquatic biome`, defined in the
vendored slice as a biome determined by a water body and by ecological climax
communities adapted to life in or on water. The target GOLD path is a
subsurface grouping whose immediate GOLD children are `Groundwater`,
`Shale gas/oil reservoir`, `Subglacial lake`, and `Subterranean lake`. The raw
path explains how the edge was generated: `Environmental > Aquatic` is the
source parent of `Environmental > Aquatic > Deep subsurface`, and the
`Environmental > Aquatic` record resolves to `ENVO:00002030`, but the GOLD bin
is not itself a kind of climax-community aquatic biome.

## Evidence

The record has no record-level evidence objects, causal graph, references, or
curator-authored mechanism claims. Its only source-level claim is the GOLD path
attestation described above, and that claim traces exactly to
`data/raw/gold_ecosystem_paths.tsv`.

The generated `ENVO:00002030` parent is mechanically traceable but
evidentially over-scoped. `parent_habitats` is an is-a slot for strictly
broader habitats; it is not a place to preserve the fact that GOLD filed this
deep-subsurface bin under its broad `Aquatic` branch. A future curation row can
define the minted source concept under a true subsurface parent and use
`parent_mode=REPLACE` to drop the inherited `aquatic biome` edge.

## Completeness

No committed source rows appear to be omitted from this generated record.
Ignored-inclusive exact searches found no exact-path rows for
`Environmental > Aquatic > Deep subsurface` in `data/raw/gold_path_biosamples.tsv`,
`data/raw/gold_path_triads.tsv`, or `data/raw/gold_studies.tsv`; no
`curation/term_requests.tsv` or `curation/causal_graphs/` entry for
`habitatmech:GOLD.21222434e2`; and no PREGO, Madin, BacDive, environment-table,
research, or history input for the source concept. The empty optional slots are
therefore expected in the generated YAML.

The consequential gap is item-level review. The class-level sweep has only
established that no vendored term matched the label by its automated lexical
routes; it explicitly did not decide whether this source path is a habitat or
whether a novel ENVO request is warranted. Until a curator performs that
item-level review, the record should stay `SEEDED`.

## Findings

| ID | Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| HM-DEEP-SUBSURFACE-45E0AABF-001 | Major | `parent_habitats` asserts a false or at least unsupported is-a edge from GOLD `Environmental > Aquatic > Deep subsurface` to `ENVO:00002030` `aquatic biome`. | The raw GOLD row places this source under `Environmental > Aquatic`, and `data/habitats/PATHS.tsv` maps that parent source record to `aquatic_biome`; the seeder therefore emits `ENVO:00002030`. The vendored ENVO row defines `aquatic biome` as a biome determined by a water body and ecological climax communities, while the target record denotes the GOLD deep-subsurface aquatic bin that contains groundwater, shale gas/oil reservoir, subglacial lake, and subterranean lake children. | Perform item-level curation in `curation/decisions.tsv`, add a definition and true genus for `habitatmech:GOLD.21222434e2` in `curation/term_requests.tsv`, and use `parent_mode=REPLACE` so regeneration drops the inherited `ENVO:00002030` parent. |

## Recommended Edits

1. Re-read GOLD `Environmental > Aquatic > Deep subsurface` and its four
   immediate child bins, then update the existing
   `curation/decisions.tsv` row for `habitatmech:GOLD.21222434e2` from a
   class-level `CONFIRM_UNGROUNDED` row to an item-level decision that records
   the path interpretation and confirms the source concept remains a real
   habitat bin.
2. Add a `curation/term_requests.tsv` row for
   `habitatmech:GOLD.21222434e2` with a label that carries the missing aquatic
   deep-subsurface context, a subsurface environmental genus such as
   `ENVO:01001046` `planetary subsurface environment` if item review confirms
   it is strict, and `parent_mode=REPLACE` to remove `ENVO:00002030`.
3. Include a curation-history record for the item-level review and term-request
   addition before regenerating this record.
4. Regenerate with `just seed`, canary
   `just seed-canary habitatmech:GOLD.21222434e2`, inspect
   `data/habitats/aquatic/deep_subsurface__45e0aabf.yaml`, and then apply the
   generated change with `just seed-apply --force` once the canary has the
   expected parent set.

## Follow-up Checks

1. Run `just validate data/habitats/aquatic/deep_subsurface__45e0aabf.yaml`.
2. Run `just validate-all data/habitats/aquatic/deep_subsurface__45e0aabf.yaml`.
3. Run `just validate-history`.
4. Run `just term-requests-check`.
5. Run `just verify-corpus --max-diffs 1`.
6. Run `just render`.
7. Run `just qc`.
8. Re-read the regenerated target and confirm that it keeps the GOLD
   attestation, has the curated label and definition, no longer lists
   `ENVO:00002030`, and remains the only file pinned to
   `habitatmech:GOLD.21222434e2`.

## Additional Notes

The same exact leaf label appears at three GOLD paths with different scope:
aquatic deep subsurface, aquatic marine deep subsurface, and terrestrial deep
subsurface. The source path, not the leaf label alone, is the identity-bearing
field for this generated record.
