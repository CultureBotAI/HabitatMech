# YAML Record Review: Epipelagic/Euphotic zone

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/epipelagic_euphotic_zone.yaml`
- Started UTC: 2026-10-02T02:13:00Z
- Finished UTC: 2026-10-02T02:25:31Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.b88a94c4f7` |
| Label | `Epipelagic/Euphotic zone` |
| File | `data/habitats/aquatic/epipelagic_euphotic_zone.yaml` |
| Category | `AQUATIC` |
| Grounding | `UNGROUNDED` |
| Mapping | `SEEDED` |
| Source | GOLD `gold.ecosystem:7897` |
| Source path | `Environmental > Aquatic > Marine > Pelagic zone > Epipelagic/Euphotic zone` |
| Generated status | Generated from `data/raw/*` inventories plus `curation/decisions.tsv`; `data/habitats/` is read-only generated output. |

The full generated YAML was read. The record is a single-source GOLD record with:

- one inherited parent, `ENVO:00000208`;
- one GOLD source attestation with 8 `ORGANISM` assertions;
- one class-level `CONFIRM_UNGROUNDED` curation event;
- no definition, synonyms, environmental parameters, characteristic taxa, evidence items, causal graphs, discussions, or datasets.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/epipelagic_euphotic_zone.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/aquatic/epipelagic_euphotic_zone.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus` | Passed; expected 3,206 records, found 3,206 on disk, 0 missing, 0 extra, 0 differing. |
| `just report` | Passed; the corpus report still ranks this record among class-level swept ungrounded records. |
| `just worklist --status all --out /tmp/habitatmech-worklist.tsv` | Passed; the target row reports `ENVO:00000209=epipelagic zone` as a candidate for `habitatmech:GOLD.b88a94c4f7`. |

`iModulonDB` was not applicable: the record names no gene, locus tag, regulator, pathway, stress response, trait, or transcriptomics dataset.

## Identity and Grounding

The GOLD identity is supported. `data/raw/gold_ecosystem_paths.tsv` has the exact canonical path with `gold.ecosystem:7897`, leaf label `Epipelagic/Euphotic zone`, and 8 organism assertions. `data/raw/gold_path_biosamples.tsv` independently lists the same canonical path and node id with 302 biosamples.

The current `UNGROUNDED` status is not supported by the vendored ontology slice. `data/raw/ontology_terms.tsv` has:

| CURIE | Label | Definition | Exact synonym |
|---|---|---|---|
| `ENVO:00000209` | `marine photic zone` | `The zone of an ocean from the surface to where photosynthesis can occur, due to the penetration of light.` | `epipelagic zone` |

That term is the exact identity for a marine `Epipelagic/Euphotic zone` source concept. The same exact grounding already exists for the sibling GOLD source concept `habitatmech:GOLD.7d154f5642`: `curation/decisions.tsv` item-grounds `Environmental > Aquatic > Marine > Oceanic > Photic zone` to `ENVO:00000209` `marine photic zone`, and `data/habitats/aquatic/marine_photic_zone.yaml` is the reviewed generated record for that target.

`ENVO:00000208` `marine pelagic zone` is a valid broader parent for the current GOLD concept. The source path explicitly places `Epipelagic/Euphotic zone` under `Environmental > Aquatic > Marine > Pelagic zone`, and `ENVO:00000208` is the record generated for that parent path.

Ignored files were included in the exact searches with `rg --no-ignore --hidden`. Searches over `curation/decisions.tsv`, `curation/term_requests.tsv`, `curation/causal_graphs`, `history`, `research`, `reports/yaml_record_review`, `data/raw/gold_ecosystem_paths.tsv`, `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`, `data/raw/gold_studies.tsv`, `data/habitats/PATHS.tsv`, `data/habitats/aquatic`, `src`, `pages/habitats`, `pages/category`, and rendered `pages/*.html` found the current class-level decision, the GOLD inventory rows, generated rendered pages, the pinned slug, and prior review notes, but no maintained item-level decision, term request, causal overlay, or research report for `habitatmech:GOLD.b88a94c4f7`.

## Evidence

| Claim | Evidence checked | Assessment |
|---|---|---|
| The record denotes GOLD `gold.ecosystem:7897`, `Environmental > Aquatic > Marine > Pelagic zone > Epipelagic/Euphotic zone`. | `data/raw/gold_ecosystem_paths.tsv` contains exactly that collapsed path and node id. | Supported. |
| The GOLD attestation has 8 organism assertions. | The same `gold_ecosystem_paths.tsv` row reports `organism_count` and `total_assertions` as 8. | Supported. |
| The record has 302 GOLD biosamples on that path. | `data/raw/gold_path_biosamples.tsv` reports 302 biosamples for path id `7897`. | Supported as source context; this is not the YAML `assertion_count`, which intentionally stores organisms. |
| No GOLD MIxS triad row is attached to this exact path. | Ignored-inclusive exact search of `data/raw/gold_path_triads.tsv` for `Environmental > Aquatic > Marine > Pelagic zone > Epipelagic/Euphotic zone` found no rows. | Supported. The nearby triad rows for `Marine > Oceanic > Photic zone` and `Marine > Pelagic zone > Abyssopelagic/Abyssal zone` do not belong to this exact record. |
| The concept is a real habitat with no fitting ontology identity. | `data/raw/ontology_terms.tsv` has `ENVO:00000209` `marine photic zone` with exact synonym `epipelagic zone`, and `just worklist --status all` proposes that term for this record. | Not supported. This source needs item-level exact grounding. |
| `ENVO:01000035` `oceanic epipelagic zone biome` or `ENVO:01000042` `neritic epipelagic zone biome` would be a better identity. | The GOLD path is `Marine > Pelagic zone > Epipelagic/Euphotic zone`, not `Marine > Oceanic > Epipelagic` or `Marine > Neritic ...`. | Not supported. These are near misses for offshore and continental-shelf epipelagic biomes, respectively. |

## Completeness

The record is incomplete at the identity-curation layer. The class-level negative decision in `curation/decisions.tsv` predates the current item-level candidate evidence and leaves a valid exact ENVO target unused.

The empty optional scientific fields are otherwise acceptable for a seeded single-source GOLD record. There is no maintained definition, environmental-parameter row, PREGO taxon matrix, causal-graph overlay, or literature evidence object for this source concept. Exact ignored-inclusive searches over the maintained curation, research, and GOLD inventory surfaces found no missing dedicated input for those fields.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | `habitatmech:GOLD.b88a94c4f7` remains `UNGROUNDED` under a stale class-level `CONFIRM_UNGROUNDED` decision even though the vendored ontology slice has an exact identity term: `ENVO:00000209` `marine photic zone`, exact synonym `epipelagic zone`. The class-level note in `curation/decisions.tsv` row 1040 says no vendored term matched this label by any sweep route; the current worklist contradicts that with `ENVO:00000209=epipelagic zone`, and `curation/decisions.tsv` already uses the same term as the exact item-level identity for the analogous GOLD marine photic-zone source. | `curation/decisions.tsv` |

No blocker findings.

No minor findings.

## Recommended Edits

1. Update the `curation/decisions.tsv` row for `habitatmech:GOLD.b88a94c4f7` from class-level `CONFIRM_UNGROUNDED` to an `ITEM`-depth `GROUND` decision targeting `ENVO:00000209` `marine photic zone` with relation `EXACT`.
2. Rerun `just seed`, `just seed-canary ENVO:00000209`, inspect `data/habitats/aquatic/marine_photic_zone.yaml`, then run the appropriate full `seed-apply` so the GOLD `Epipelagic/Euphotic zone` source attestation merges into the reviewed `ENVO:00000209` record.
3. Confirm the regenerated corpus drops the minted `habitatmech:GOLD.b88a94c4f7` record, removes the active `data/habitats/PATHS.tsv` row for that minted identifier, and retains a strictly broader parent set on `marine_photic_zone.yaml`.

## Follow-up Checks

- `just validate data/habitats/aquatic/marine_photic_zone.yaml`
- `just validate-strict data/habitats/aquatic/marine_photic_zone.yaml`
- `just verify-corpus`
- `just render`
- `just qc`
- `git diff --check`
- Manual: inspect the regenerated `data/habitats/aquatic/marine_photic_zone.yaml` and confirm it has the added `GOLD` attestation for `Environmental > Aquatic > Marine > Pelagic zone > Epipelagic/Euphotic zone`.
- Manual: search for `habitatmech:GOLD.b88a94c4f7` with `rg --no-ignore --hidden` after regeneration to verify no stale active `PATHS.tsv`, generated record, or rendered page entry remains.

## Additional Notes

The previous `reports/yaml_record_review/20261002T014625Z-epipelagic.md` review flagged this record as a likely sibling needing the same `ENVO:00000209` item review. This pass read `data/habitats/aquatic/epipelagic_euphotic_zone.yaml` itself and confirmed the sibling diagnosis for the generated GOLD record rather than relying on that report as evidence.

The invalid exploratory commands `just report --record habitatmech:GOLD.b88a94c4f7` and `just worklist habitatmech:GOLD.b88a94c4f7` were rejected because those recipes do not expose per-record filters. Their supported corpus forms, `just report` and `just worklist --status all --out /tmp/habitatmech-worklist.tsv`, both ran successfully.
