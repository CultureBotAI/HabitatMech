# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/aquatic/cryoconite_hole.yaml`
- Started UTC: `2026-09-27T10:01:17Z`
- Finished UTC: `2026-09-27T10:01:17Z`
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/aquatic/cryoconite_hole.yaml` |
| Class | `HabitatRecord` |
| Identifier | `ENVO:03000039` |
| Label | `cryoconite hole` |
| Category | `AQUATIC` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Source provenance | One GOLD source concept, `gold.ecosystem:7968` |
| Generated status | Generated from `data/raw/`, the vendored ontology slice, and `src/habitatmech/seed.py`; `data/habitats/PATHS.tsv` pins `ENVO:03000039` to `cryoconite_hole` |

The complete generated record was read before making this judgment. It
contains the ENVO identifier and definition, one ENVO synonym, the ontology
parent `ENVO:03000048`, one generated GOLD-parent `parent_habitats` edge, one
GOLD source attestation, and the seeder history event. It has no xrefs,
environmental parameters, characteristic taxa, evidence, causal graphs,
discussions, external datasets, or quality flags.

Before this report was written, ignored-inclusive exact searches over
`data/raw`, `data/habitats`, `curation`, `history`, `research`, and `conf` for
`ENVO:03000039`, `gold.ecosystem:7968`, `habitatmech:GOLD.6faa98a0aa`, and
the exact GOLD path found the path lock, the expected vendored ontology rows,
the expected GOLD source row, the generated source-path parent, and this
generated target record. A `find` under `curation/causal_graphs` found no
`*cryoconite*` causal overlay, a `find` under `research/habitats` found no
`*cryoconite*` research report, and a `find` under
`reports/yaml_record_review` found no pre-existing `*cryoconite_hole*`
YAML-record review report. Those `rg --no-ignore --hidden` and `find` checks
included ignored files.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/cryoconite_hole.yaml` | Passed; LinkML reported no issues. |
| `just validate-all data/habitats/aquatic/cryoconite_hole.yaml --out /tmp/habitatmech-cryoconite-hole-validate-all.tsv` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just validate-strict data/habitats/aquatic/cryoconite_hole.yaml --quiet --out /tmp/habitatmech-cryoconite-hole-validate-strict.tsv` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs were valid. |
| `just validate-history` | Passed; 77 history records were valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; the corpus has the expected 3206 records and reproduces exactly from `data/raw/`. |
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist-cryoconite-hole.tsv` | Passed; wrote 953 ungrounded rows and reported 1810 decisions on file. |
| `just report` | Passed; emitted the corpus diagnostic report for 3206 records, including 468 `AQUATIC` records, 2520 `SEEDED` records, 1060 `EXACT` records, and 953 `UNGROUNDED` records. |
| Focused reference validator | Not checked: an ignored-inclusive exact `rg` search of `justfile`, `.claude`, `docs`, `scripts`, `src`, and `tests` found no `validate-references` command, and this target has no `evidence` entries to dereference. |

## Identity and Grounding

The GOLD source identity is supported. `data/raw/gold_ecosystem_paths.tsv`
contains exactly `Environmental > Aquatic > Freshwater > Glacier >
Cryoconite hole` with leaf label `Cryoconite hole` and
`gold.ecosystem:7968`. The raw aggregate row is a single GOLD node at depth 5
with zero organism, study, biosample, and total assertions, which matches the
generated source attestation: it preserves the GOLD node, label, and path, and
correctly omits `assertion_count`, `assertion_unit`, and any duplicate-node
note.

The exact ENVO grounding is supported. `data/raw/ontology_terms.tsv` contains
`ENVO:03000039` with canonical label `cryoconite hole`, the generated
definition text, and exact synonym `cryoconite holes`. The GOLD leaf label is
an exact case-insensitive match to the ENVO label, and the ENVO definition
denotes the same habitat type: a vertical thaw hole in an ice mass formed by
local ice melt associated with cryoconite deposits.

The generated ontology parent is supported. `data/raw/ontology_subclass_edges.tsv`
records `ENVO:03000039 rdfs:subClassOf ENVO:03000048`, and
`data/raw/ontology_terms.tsv` defines `ENVO:03000048` `thaw hole` as a channel
traversing an ice mass floating on a water body.

The generated GOLD source-path parent is not supported. The parent path
`Environmental > Aquatic > Freshwater > Glacier` resolves to
`habitatmech:GOLD.6faa98a0aa`, whose record denotes GOLD `Glacier`. A
cryoconite hole is a thaw-hole channel within an ice mass, not a glacier.
`src/habitatmech/seed.py` adds this edge unconditionally in its second GOLD
pass by resolving every child path to the concept of its parent path and then
calling `store.concepts[child_id].parents.add(parent_id)`.

## Evidence

The record has no claim-level `evidence` objects or curator-authored mechanism
claims. Its generated source-attestation, grounding, and hierarchy claims trace
to maintained raw and ontology inputs:

| Claim | Nearest support | Assessment |
|---|---|---|
| The HabitatRecord denotes `ENVO:03000039` `cryoconite hole`. | `data/raw/ontology_terms.tsv` carries that id, label, definition, and exact synonym; `data/habitats/PATHS.tsv` pins that identifier to the generated slug. | Supported exactly. |
| The source concept is GOLD `gold.ecosystem:7968` `Cryoconite hole` under `Environmental > Aquatic > Freshwater > Glacier`. | `data/raw/gold_ecosystem_paths.tsv:1466` carries that exact collapsed GOLD path and node. | Supported exactly. |
| The record has no GOLD assertion count. | `data/raw/gold_ecosystem_paths.tsv:1466` reports zero organism, study, biosample, and total assertions, and exact ignored-inclusive searches of `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`, and `data/raw/gold_studies.tsv` found no row for the exact target path. | Supported exactly. |
| `ENVO:03000048` is a broader parent. | `data/raw/ontology_subclass_edges.tsv:7980` records the direct ENVO subclass edge. | Supported exactly. |
| `habitatmech:GOLD.6faa98a0aa` is a broader parent. | Generated by `src/habitatmech/seed.py` from the GOLD parent path `Environmental > Aquatic > Freshwater > Glacier`. | Unsupported as an is-a parent; see `HM-CRYOCONITE-HOLE-001`. |

## Completeness

The source attestation is complete for the currently committed GOLD source
inventories: the exact path has one GOLD node and no direct organism, study,
biosample, or MIxS-triad rows.

The ENVO grounding is complete enough for a seeded lexical exact match. No
target-specific `ITEM` decision endorses it yet, but the identifier, label,
definition, synonym, and ontology parent all agree with the vendored ontology
slice and with the GOLD leaf identity.

The hierarchy is incomplete because GOLD path context is being emitted as an
`is-a` edge even where the source tree has modeled location rather than
subtyping. The record should retain its ENVO thaw-hole parent and stop
claiming that a cryoconite hole is a kind of `Glacier`.

## Findings

| ID | Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| HM-CRYOCONITE-HOLE-001 | Major | `parent_habitats` includes false parent `habitatmech:GOLD.6faa98a0aa` `Glacier`. | The target's GOLD source path is `Environmental > Aquatic > Freshwater > Glacier > Cryoconite hole`; the parent path resolves to the generated `Glacier` record; and `src/habitatmech/seed.py` unconditionally adds resolved GOLD parent paths as `parent_habitats`. ENVO defines `cryoconite hole` as a thaw hole within an ice mass, not as the ice mass or glacier itself. | Add a maintained GOLD parent-path suppression or override in `curation/`, then teach the second GOLD pass in `src/habitatmech/seed.py` to consult it before adding `parent_habitats`. |

## Recommended Edits

1. Add a maintained `curation/` table that suppresses the generated GOLD edge
   from child path
   `Environmental > Aquatic > Freshwater > Glacier > Cryoconite hole` to
   parent path `Environmental > Aquatic > Freshwater > Glacier`.
2. Update the second GOLD parent-path pass in `src/habitatmech/seed.py` so it
   skips curated suppressions before calling
   `store.concepts[child_id].parents.add(parent_id)`.
3. Regenerate the corpus and confirm that
   `data/habitats/aquatic/cryoconite_hole.yaml` still grounds exactly to
   `ENVO:03000039` and lists only `ENVO:03000048` as a parent.

## Follow-up Checks

1. Run `just seed`, then `just seed-canary ENVO:03000039`, and verify the only
   `cryoconite_hole.yaml` parent change is removal of
   `habitatmech:GOLD.6faa98a0aa`.
2. Run `just validate data/habitats/aquatic/cryoconite_hole.yaml`.
3. Run `just validate-all data/habitats/aquatic/cryoconite_hole.yaml`.
4. Run `just validate-causal-all`.
5. Run `just verify-corpus --max-diffs 1`.
6. Repeat ignored-inclusive searches for `ENVO:03000039`,
   `gold.ecosystem:7968`,
   `Environmental > Aquatic > Freshwater > Glacier > Cryoconite hole`,
   and `cryoconite_hole` over maintained raw, curation, generated record,
   research, history, report, and config paths to ensure no other maintained
   owner needs a parallel update.

## Additional Notes

The related `Environmental > Aquatic > Freshwater > Ice > Cryoconite` GOLD
record is separate from this exact cryoconite-hole target. Its MIxS triad rows
name `ENVO:03000039` as a local-scale term and `ENVO:03000038`
`cryoconite deposit` as a medium-scale term; those rows are evidence for that
Cryoconite leaf, not for broadening or narrowing the already exact
`ENVO:03000039` target reviewed here.
