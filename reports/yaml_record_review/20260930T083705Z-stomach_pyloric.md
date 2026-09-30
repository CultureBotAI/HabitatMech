# YAML Record Review: Stomach: Pyloric

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/stomach_pyloric.yaml`
- Started UTC: 2026-09-30T08:37:05Z
- Finished UTC: 2026-09-30T08:37:05Z
- Verdict: pass

## Target

Reviewed one generated `HabitatRecord`:

| Field | Value |
|---|---|
| Path | `data/habitats/host_associated/stomach_pyloric.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.15506702ab` |
| Label | `Stomach: Pyloric` |
| Category | `HOST_ASSOCIATED` |
| `grounding_status` | `NARROW` |
| `mapping_status` | `REVIEWED` |
| Generated? | Yes; owned by `data/raw/`, `curation/decisions.tsv`, and `data/habitats/PATHS.tsv` |

This record is the GOLD Fish foregut pyloric-stomach concept:

| Source | Source identity | Maintained input |
|---|---|---|
| GOLD | `gold.ecosystem:7533`, `Host-associated > Fish > Digestive system > Foregut > Stomach: Pyloric` | `data/raw/gold_ecosystem_paths.tsv` |

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/stomach_pyloric.yaml` | Pass; LinkML reported no issues. |
| `just validate-strict data/habitats/host_associated/stomach_pyloric.yaml` | Pass; 1 file scanned, 0 files with errors, 0 error rows. |
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
| Minted identity | Supported. Row 1925 of `data/raw/gold_ecosystem_paths.tsv` has `gold.ecosystem:7533` for `Host-associated > Fish > Digestive system > Foregut > Stomach: Pyloric`, with leaf label `Stomach: Pyloric`, depth 5, one GOLD node, and zero organism, study, or biosample assertions. |
| Item-level decision | Supported. `curation/decisions.tsv:215` keys `habitatmech:GOLD.15506702ab` to an `ITEM`-depth `GROUND_AS_PARENT` decision for `UBERON:0000945` `stomach`, preserving a minted identity with `grounding_status: NARROW`. |
| UBERON stomach parent | Supported. `UBERON:0000945` is labeled `stomach` in `data/raw/ontology_terms.tsv` and defines an expanded region of the vertebrate alimentary tract; it is broader than a Fish foregut pyloric-stomach subregion. |
| Fish Foregut parent | Supported. GOLD directly places `Stomach: Pyloric` under `Host-associated > Fish > Digestive system > Foregut`, and `habitatmech:GOLD.52f22e84ee` maps to `foregut__6bc8c43a` in `data/habitats/PATHS.tsv`. |
| Pyloric false friends | Correctly avoided. The ignored/hidden-inclusive ontology searches found `BTO:0002121` and `UBERON:0008246` `pyloric stomach` exact-label candidates, but both are starfish structures; `BTO:0001146` `pyloric region`, `BTO:0002984` `antropyloric mucosa`, and `BTO:0004110` `pyloric mucosa` are narrower region or mucosa terms, not the full GOLD Fish pyloric-stomach habitat concept. |
| `mapping_status: REVIEWED` | Supported. The sole source concept has an item-level decision, so the generated single-source GOLD record is reviewed. |

The exact negative searches used `rg --fixed-strings --no-ignore --hidden`, `rg --ignore-case --no-ignore --hidden`, and `find` across `data/raw`, `data/habitats`, `curation`, `history`, `research`, `reports/yaml_record_review`, `docs`, `src`, `conf`, `.claude`, `CLAUDE.md`, `justfile`, and the freshly written `/tmp/habitat_worklist.tsv`. They found the expected GOLD raw row, generated record, `PATHS.tsv` lock row, item-level decision, Fish Foregut parent, vertebrate stomach parent, generic PREGO-backed `BTO:0001307` stomach record, starfish-specific BTO/UBERON `pyloric stomach` candidates, BTO `pyloric region` and `pyloric mucosa` near misses, the separate Fish `Pyloric ceca` worklist row, and earlier sibling-report mentions. They found no pre-existing YAML review report for `habitatmech:GOLD.15506702ab`, no source-owned count or path conflict, no `curation/term_requests.tsv` definition for this already-reviewed minted record, and no causal-graph, discussion, dataset, or separate `history/` session record for this source concept.

## Evidence

The record contains generated GOLD provenance and one generated curation-history event from the maintained decision row; it has no curator-authored record-level `evidence` items, environmental parameters, characteristic taxa, datasets, discussions, or causal graphs.

| Generated claim | Evidence review |
|---|---|
| GOLD `source_attestations` entry | Exact. The generated `source_id`, `source_label`, `source_path`, and omitted assertion counts match the row for `gold.ecosystem:7533`; the raw row has zero organism, study, and biosample counts. |
| `UBERON:0000945` as a broader parent | Exact. `curation/decisions.tsv:215` uses `GROUND_AS_PARENT`, and `src/habitatmech/seed.py` translates that decision into an extra parent while keeping the minted identifier. |
| Fish Foregut as a broader parent | Exact. The GOLD source path places `Stomach: Pyloric` directly below `Foregut`; the generated record carries the matching Fish Foregut minted identifier as a source-path parent. |
| Reviewed curation history | Exact. The generated first `curation_history` entry restates the 2026-08-12 `GROUND_AS_PARENT` decision for `habitatmech:GOLD.15506702ab`; the 2026-08-16 entry records source seeding. |

There are no taxon associations to overstate: the sole GOLD row has `0` organism, study, and biosample assertions, and the generated target accordingly has no `characteristic_taxa` entries.

No iModulonDB adapter check was applicable. The record names a host anatomical habitat path, not a gene, locus, regulator, transcriptomics dataset, pathway, or stress-response claim.

## Completeness

The record is complete for its current maintained inputs.

- Its single GOLD source concept has item-level review, so `mapping_status: REVIEWED` is justified.
- The exact ignored/hidden-inclusive searches above did not find a maintained definition, causal-graph overlay, dataset, discussion, or environmental-parameter input to project into this record.
- A separate `history/` session record was not found for the 2026-08-12 decision, but `history/README.md` documents history presence as advisory while validity is blocking; the generated record-level curation history is present and valid.
- The freshly generated worklist did not place Pyloric Stomach among its 953 unresolved rows because this target is `NARROW` and item-reviewed, not `UNGROUNDED`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No immediate follow-up is required. If future curation adds a Fish pyloric-stomach definition, causal graph, or stricter parent, rerun:

1. `just validate data/habitats/host_associated/stomach_pyloric.yaml`
2. `just validate-strict data/habitats/host_associated/stomach_pyloric.yaml`
3. `just validate-history`
4. `just term-requests-check`
5. `just validate-causal-all`
6. `just verify-corpus --max-diffs 1`
7. `just worklist --status all --out /tmp/habitat_worklist.tsv`
8. `just report`
9. `git diff --check`

## Additional Notes

The Fish `Stomach: Cardiac` and `Stomach: Fundic` sibling records have equivalent 2026-08-12 item-level decisions that keep those GOLD `Stomach: X` labels minted and attach `UBERON:0000945` as a broader stomach parent. Those are consistent siblings, not duplicate inputs for this Pyloric Stomach source concept.
