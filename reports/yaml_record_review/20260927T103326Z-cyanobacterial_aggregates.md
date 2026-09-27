# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/aquatic/cyanobacterial_aggregates.yaml`
- Started UTC: `2026-09-27T10:33:26Z`
- Finished UTC: `2026-09-27T10:33:26Z`
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/aquatic/cyanobacterial_aggregates.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.9b43a12f0c` |
| Label | `Cyanobacterial aggregates` |
| Category | `AQUATIC` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Source provenance | One GOLD source concept, `gold.ecosystem:8088` |
| Generated status | Generated from `data/raw/`, the vendored ontology slice, `curation/decisions.tsv`, and `src/habitatmech/seed.py`; `data/habitats/PATHS.tsv` pins `habitatmech:GOLD.9b43a12f0c` to `cyanobacterial_aggregates` |

The complete generated record was read before making this judgment. It
contains the HabitatMech GOLD identifier, generated label, one generated GOLD
source-path `parent_habitats` edge, one GOLD source attestation, a class-level
`CONFIRM_UNGROUNDED` curation-history event, and the seeder history event. It
has no definition, synonyms, xrefs, environmental parameters, characteristic
taxa, evidence, causal graphs, discussions, external datasets, or quality
flags.

Before this report was written, ignored-inclusive exact searches over
`data/raw`, `data/habitats`, `curation`, `history`, `research`, `reports`, and
`conf` for `habitatmech:GOLD.9b43a12f0c`, `gold.ecosystem:8088`, the exact
GOLD path, `cyanobacterial_aggregates`, and related `cyanobacterial` labels
found the path lock, the class-level grounding decision, the expected raw GOLD
rows, the generated target record, and the related but distinct
`cyanobacterial_bloom` record. A `find` under `curation/causal_graphs` found
no `*cyanobacter*` or `*cyanobacterial*` causal overlay, a `find` under
`research/habitats` found no `*cyanobacter*` or `*cyanobacterial*` research
report, and a `find` under `reports/yaml_record_review` found no pre-existing
`*cyanobacterial_aggregates*` YAML-record review report. Those
`rg --no-ignore --hidden` and `find` checks included ignored files.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/cyanobacterial_aggregates.yaml` | Passed; LinkML reported no issues. |
| `just validate-all data/habitats/aquatic/cyanobacterial_aggregates.yaml --out /tmp/habitatmech-cyanobacterial-aggregates-validate-all.tsv` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just validate-strict data/habitats/aquatic/cyanobacterial_aggregates.yaml --quiet --out /tmp/habitatmech-cyanobacterial-aggregates-validate-strict.tsv` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs were valid. |
| `just validate-history` | Passed; 77 history records were valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; the corpus has the expected 3206 records and reproduces exactly from `data/raw/`. |
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist-cyanobacterial-aggregates.tsv` | Passed; wrote 953 ungrounded rows and reported 1810 decisions on file. |
| `just report` | Passed; emitted the corpus diagnostic report for 3206 records, including 468 `AQUATIC` records, 2520 `SEEDED` records, 1060 `EXACT` records, and 953 `UNGROUNDED` records. |
| Focused reference validator | Not checked: an ignored-inclusive exact `rg` search of `justfile`, `.claude`, `docs`, `scripts`, `src`, and `tests` found no `validate-references` command, and this target has no `evidence` entries to dereference. |

## Identity and Grounding

The GOLD source identity is supported. `data/raw/gold_ecosystem_paths.tsv`
contains exactly
`Environmental > Aquatic > Freshwater > Lake > Cyanobacterial aggregates` with
leaf label `Cyanobacterial aggregates`, depth 5, one GOLD node, six organism
assertions, and `gold.ecosystem:8088`. The generated source attestation
preserves that GOLD node, label, path, assertion count, and `ORGANISM` unit.

The committed raw GOLD inputs add 32 direct biosamples and two GOLD studies for
the exact path. They do not add a MIxS triad row for the exact path, so there
is no source-specific local, medium, or broad-scale ontology assertion to
compare against the generated identity.

The ungrounded identity is plausible. The maintained class-level
`CONFIRM_UNGROUNDED` decision records that no term in the vendored slice
matched the label by any search route. A fresh ignored-inclusive search found
no exact cyanobacterial-aggregate ontology term; the nearby
`ENVO:03600071` `cyanobacterial bloom` names a water-discoloration feature
caused by rapid cyanobacterial multiplication and is not the same concept as
GOLD's `Cyanobacterial aggregates` leaf.

The generated GOLD source-path parent is not supported. `ENVO:00000021`
denotes `freshwater lake`, and the target's GOLD source path only says that
`Cyanobacterial aggregates` sit under GOLD's `Lake` path. A cyanobacterial
aggregate may be located in a freshwater lake, but it is not a freshwater lake.
`src/habitatmech/seed.py` adds this edge unconditionally in its second GOLD
pass by resolving every child path to the concept of its parent path and then
calling `store.concepts[child_id].parents.add(parent_id)`.

## Evidence

The record has no claim-level `evidence` objects or curator-authored mechanism
claims. Its generated source-attestation, grounding, and hierarchy claims trace
to maintained raw, decision, and ontology inputs:

| Claim | Nearest support | Assessment |
|---|---|---|
| The HabitatRecord denotes `habitatmech:GOLD.9b43a12f0c` `Cyanobacterial aggregates`. | `curation/decisions.tsv` carries a class-level `CONFIRM_UNGROUNDED` decision for that identifier; `data/habitats/PATHS.tsv` pins that identifier to the generated slug. | Supported as a HabitatMech-minted ungrounded source concept. |
| The source concept is GOLD `gold.ecosystem:8088` `Cyanobacterial aggregates` under `Environmental > Aquatic > Freshwater > Lake`. | `data/raw/gold_ecosystem_paths.tsv:606` carries that exact collapsed GOLD path and node. | Supported exactly. |
| The record has six GOLD organism assertions. | `data/raw/gold_ecosystem_paths.tsv:606` reports six organism assertions, zero study assertions, zero biosample assertions, and six total assertions for the exact path. | Supported exactly. |
| `ENVO:00000021` is a broader parent. | Generated by `src/habitatmech/seed.py` from the GOLD parent path `Environmental > Aquatic > Freshwater > Lake`. | Unsupported as an is-a parent; see `HM-CYANOBACTERIAL-AGGREGATES-001`. |

## Completeness

The GOLD source attestation is complete for the currently committed aggregate
GOLD source inventory. The separate biosample and study inventories contain 32
biosamples and two studies for the exact path, but those are not fields on
this generated `SourceAttestation`.

The class-level `UNGROUNDED` decision is correctly reflected from maintained
curation, and the fresh search found no already-vendored ontology replacement.
No target-specific `ITEM` decision has assessed whether the concept is a
habitat at all, so this remains a seeded GOLD concept rather than a reviewed
term request.

The hierarchy is incomplete because GOLD path context is being emitted as an
`is-a` edge even where the source tree has modeled location rather than
subtyping. The record should stop claiming that a cyanobacterial aggregate is a
kind of `freshwater lake`.

## Findings

| ID | Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| HM-CYANOBACTERIAL-AGGREGATES-001 | Major | `parent_habitats` includes false parent `ENVO:00000021` `freshwater lake`. | The target's GOLD source path is `Environmental > Aquatic > Freshwater > Lake > Cyanobacterial aggregates`; the parent path resolves to the reviewed `ENVO:00000021` `freshwater lake` record; and `src/habitatmech/seed.py` unconditionally adds resolved GOLD parent paths as `parent_habitats`. The target leaf denotes cyanobacterial aggregates reported in the lake branch, not a lake subtype. | Add a maintained GOLD parent-path suppression or override in `curation/`, then teach the second GOLD pass in `src/habitatmech/seed.py` to consult it before adding `parent_habitats`. |

## Recommended Edits

1. Add a maintained `curation/` table that suppresses the generated GOLD edge
   from child path
   `Environmental > Aquatic > Freshwater > Lake > Cyanobacterial aggregates`
   to parent path `Environmental > Aquatic > Freshwater > Lake`.
2. Update the second GOLD parent-path pass in `src/habitatmech/seed.py` so it
   skips curated suppressions before calling
   `store.concepts[child_id].parents.add(parent_id)`.
3. Regenerate the corpus and confirm that
   `data/habitats/aquatic/cyanobacterial_aggregates.yaml` keeps the supported
   GOLD source attestation and drops `ENVO:00000021` from `parent_habitats`.

## Follow-up Checks

1. Run `just seed`, then
   `just seed-canary habitatmech:GOLD.9b43a12f0c`, and verify the only
   `cyanobacterial_aggregates.yaml` parent change is removal of
   `ENVO:00000021`.
2. Run `just validate data/habitats/aquatic/cyanobacterial_aggregates.yaml`.
3. Run `just validate-all data/habitats/aquatic/cyanobacterial_aggregates.yaml`.
4. Run `just validate-causal-all`.
5. Run `just verify-corpus --max-diffs 1`.
6. Repeat ignored-inclusive searches for `habitatmech:GOLD.9b43a12f0c`,
   `gold.ecosystem:8088`,
   `Environmental > Aquatic > Freshwater > Lake > Cyanobacterial aggregates`,
   and `cyanobacterial_aggregates` over maintained raw, curation, generated
   record, research, history, report, and config paths to ensure no other
   maintained owner needs a parallel update.

## Additional Notes

The existing `Environmental > Aquatic > Freshwater > Lake > Cyanobacterial bloom`
GOLD record is separate from this exact cyanobacterial-aggregate target. Its
record is already grounded to `ENVO:03600071` `cyanobacterial bloom`, while
this target has no exact vendored ontology class and no MIxS triad row pointing
to one.
