# YAML Record Review: Intestine: Anterior

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/intestine_anterior.yaml`
- Started UTC: 2026-09-30T09:47:55Z
- Finished UTC: 2026-09-30T09:47:55Z
- Verdict: pass

## Target

Reviewed one generated `HabitatRecord`:

| Field | Value |
|---|---|
| Path | `data/habitats/host_associated/intestine_anterior.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.c2a1b0b268` |
| Label | `Intestine: Anterior` |
| Category | `HOST_ASSOCIATED` |
| `grounding_status` | `NARROW` |
| `mapping_status` | `REVIEWED` |
| Generated? | Yes; owned by `data/raw/`, `curation/decisions.tsv`, and `data/habitats/PATHS.tsv` |

This target is the reviewed, minted GOLD Fish anterior-intestine source concept:

| Source | Source identity | Maintained input |
|---|---|---|
| GOLD | `gold.ecosystem:7534` / `gold.ecosystem:7535`, `Host-associated > Fish > Digestive system > Intestine: Anterior` | `data/raw/gold_ecosystem_paths.tsv` |

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/intestine_anterior.yaml` | Pass; LinkML reported no issues. |
| `just validate-strict data/habitats/host_associated/intestine_anterior.yaml` | Pass; 1 file scanned, 0 files with errors, 0 error rows. |
| `just validate-causal-all` | Pass; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Pass; 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Pass; the committed term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Pass; 3,206 expected records, 3,206 on disk, 0 missing, 0 extra, 0 differing. |
| `just worklist --status all --out /tmp/habitat_worklist.tsv` | Pass; wrote 953 unresolved worklist rows. |
| `just report` | Pass; reported 3,206 records, 686 `REVIEWED` records, 1,060 `EXACT` records, and 0 risky groundings not yet reviewed. |
| `git diff --check` | Pass before writing this report. |

## Identity and Grounding

The identity and grounding are sound.

| Claim | Review |
|---|---|
| Minted identity | Supported. Row 1928 of `data/raw/gold_ecosystem_paths.tsv` has the full path `Host-associated > Fish > Digestive system > Intestine: Anterior`, leaf label `Intestine: Anterior`, depth 4, two collapsed GOLD node IDs, and zero organism, study, or biosample assertions. |
| Item-level decision | Supported. `curation/decisions.tsv:1089` keys `habitatmech:GOLD.c2a1b0b268` to an `ITEM`-depth `GROUND_AS_PARENT` decision for `UBERON:0000160` `intestine`, preserving a minted Fish anterior-intestine identity with `grounding_status: NARROW`. |
| UBERON intestine parent | Supported. `UBERON:0000160` is the vendored `intestine` term and defines the alimentary-canal segment from stomach to anus. The Fish `Intestine: Anterior` source concept is narrower than that generic anatomy class. |
| Fish Digestive system parent | Supported. GOLD places `Intestine: Anterior` directly under `Host-associated > Fish > Digestive system`; `data/habitats/PATHS.tsv` maps that parent to `habitatmech:GOLD.8a68d0f6f5`, whose generated record carries the exact GOLD parent path. |
| `mapping_status: REVIEWED` | Supported. The sole collapsed GOLD source concept has the item-level `GROUND_AS_PARENT` decision above, and a single-source GOLD record becomes reviewed when its one source concept is reviewed. |

The exact negative searches used `rg --fixed-strings --no-ignore --hidden`,
`rg --no-ignore --hidden`, and `find` across `data/raw`, `data/habitats`,
`curation`, `history`, `research`, `reports/yaml_record_review`, `docs`, `src`,
`conf`, `.claude`, `CLAUDE.md`, `justfile`, and the freshly written
`/tmp/habitat_worklist.tsv`. They found the expected GOLD raw row, item-level
decision, generated record, `PATHS.tsv` row, UBERON parent, and Fish Digestive
system parent. They found no exact worklist row for `habitatmech:GOLD.c2a1b0b268`,
no maintained definition, no target causal-graph overlay, no separate
`history/` session record, no source-specific environmental triad, no
source-owned assertion count for the two Fish `Intestine: Anterior` GOLD nodes,
and no previous YAML review report for `intestine_anterior`.

## Evidence

The record contains generated GOLD provenance, generated and curated broader
parents, and generated curation-history events from the maintained decision row
and source seed. It has no ontology definition, synonyms, curator-authored
record-level evidence items, environmental parameters, characteristic taxa,
datasets, discussions, or causal graphs.

| Generated claim | Evidence review |
|---|---|
| GOLD `source_attestations` entry | Exact. `data/raw/gold_ecosystem_paths.tsv:1928` is the sole maintained source row for `gold.ecosystem:7534|gold.ecosystem:7535` and has no organism, study, biosample, or environmental-parameter assertion counts to project. |
| `UBERON:0000160` as a broader parent | Exact. The 2026-08-12 `GROUND_AS_PARENT` decision selects `UBERON:0000160` as a broader anatomy parent rather than the identity, and the vendored ontology row labels that target `intestine`. |
| Fish Digestive system as a broader parent | Exact. The GOLD source path places `Intestine: Anterior` one level below the Fish Digestive system source concept, and the generated parent record `digestive_system__4f205b4d.yaml` carries `habitatmech:GOLD.8a68d0f6f5`. |
| UBERON anterior-intestine near misses | Correctly not used. `UBERON:0000945` `stomach` and `UBERON:0002108` `small intestine` both carry `anterior intestine` as a synonym, but neither exactly denotes the Fish-specific GOLD `Intestine: Anterior` path. |
| Reviewed curation history | Exact. The generated first `curation_history` entry restates the 2026-08-12 item-level `GROUND_AS_PARENT` decision, and the 2026-08-16 seed entry records source seeding. |

There are no taxon associations to overstate: the collapsed GOLD row has `0`
organism, study, and biosample assertions, and the generated target accordingly
has no `characteristic_taxa` entries.

No iModulonDB adapter check was applicable. The record names a host anatomical
habitat path, not a gene, locus, regulator, transcriptomics dataset, pathway,
or stress-response claim.

## Completeness

The record is complete for its current maintained inputs.

- The item-level `GROUND_AS_PARENT` decision reviews the sole collapsed GOLD source concept, so `mapping_status: REVIEWED` is justified.
- The minted identity is the correct generated representation for a Fish anterior-intestine concept that is narrower than generic `UBERON:0000160` intestine.
- The exact ignored/hidden-inclusive searches above found no maintained definition, target-specific causal-graph overlay, dataset, discussion, environmental-parameter input, or exact worklist row to project into the record.
- The exact GOLD source row has no organism, study, or biosample assertions, so the absence of assertion counts and characteristic taxa is expected.
- A separate `history/` session record was not found for the 2026-08-12 decision, but `history/README.md` documents history presence as advisory while validity is blocking; the generated record-level curation history is present and valid.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No immediate follow-up is required. If future curation adds a Fish
`Intestine: Anterior` mechanism graph or authored definition, rerun:

1. `just validate data/habitats/host_associated/intestine_anterior.yaml`
2. `just validate-strict data/habitats/host_associated/intestine_anterior.yaml`
3. `just validate-history`
4. `just term-requests-check`
5. `just validate-causal-all`
6. `just verify-corpus --max-diffs 1`
7. `just worklist --status all --out /tmp/habitat_worklist.tsv`
8. `just report`
9. `git diff --check`

## Additional Notes

The reviewed Air-breathing organ child keeps `Intestine: Anterior` as its
source-path parent. That child is still unresolved in the all-status worklist,
but its ungrounded state does not undermine this parent record's identity,
broader UBERON intestine parent, or item-level reviewed status.
