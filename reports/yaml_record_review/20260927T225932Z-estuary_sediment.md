# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/aquatic/estuary_sediment.yaml`
- Started UTC: 2026-09-27T22:59:32Z
- Finished UTC: 2026-09-27T22:59:32Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.4849010f40` |
| Label | `Estuary: Sediment` |
| Category | `AQUATIC` |
| Grounding status | `NARROW` |
| Mapping status | `REVIEWED` |
| Generated path | `data/habitats/aquatic/estuary_sediment.yaml` |
| GOLD path | `Environmental > Aquatic > Marine > Intertidal zone > Estuary: Sediment` |

The target is a generated GOLD-only record for estuarine sediment. It has one
source attestation, two generated parents, no definition, no xrefs, no
environmental parameters, no characteristic taxa, no record-level evidence, no
causal graphs, no discussions, and no datasets.

The record is correctly kept under its minted `habitatmech:GOLD.4849010f40`
identifier rather than grounded to `ENVO:00000045` `estuary`: the GOLD leaf
denotes a sediment material in an estuarine context, not the estuary itself.
Its `REVIEWED` status comes from the item-level `GROUND_AS_PARENT` row in
`curation/decisions.tsv`.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/aquatic/estuary_sediment.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/aquatic/estuary_sediment.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the generated term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records validated against the vendored history schema. |
| `just verify-corpus` | Passed; 3206 records were expected, 3206 were found, and `data/habitats/` reproduced exactly from `data/raw/`. |
| `just worklist --status all --out /tmp/habitatmech-estuary-sediment-worklist.tsv` | Passed; wrote 953 rows to `/tmp/habitatmech-estuary-sediment-worklist.tsv`. |
| `just report --out /tmp/habitatmech-estuary-sediment-report.tsv` | Passed; wrote `/tmp/habitatmech-estuary-sediment-report.tsv` and listed this target with 1 `GOLD` source, 36 source assertions, 2 parents, and 0 populated optional claim collections. |

No required validator was skipped. The target has no causal graph, no
`EvidenceItem` references, and no dataset references for a narrower
record-local reference validator to inspect.

The strict validator left `reports/instance_validation_failures.tsv`
unchanged.

## Identity and Grounding

The generated identifier, label, category, GOLD attestation, and curation
history agree with the committed source inventory and decision row:

- `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.4849010f40` to
  `estuary_sediment`.
- `data/raw/gold_ecosystem_paths.tsv` has an exact aggregate row for
  `Environmental > Aquatic > Marine > Intertidal zone > Estuary: Sediment`.
- `curation/decisions.tsv` has an item-level `GROUND_AS_PARENT` row for
  `habitatmech:GOLD.4849010f40`.

The exact GOLD ecosystem-path row has:

| Column | Value |
|---|---|
| `canonical_path` | `Environmental > Aquatic > Marine > Intertidal zone > Estuary: Sediment` |
| `ecosystem` | `Environmental` |
| `ecosystem_category` | `Aquatic` |
| `ecosystem_type` | `Marine` |
| `ecosystem_subtype` | `Intertidal zone` |
| `specific_ecosystem` | `Estuary: Sediment` |
| `leaf_label` | `Estuary: Sediment` |
| `depth` | `5` |
| `gold_node_count` | `1` |
| `organism_count` | `36` |
| `study_count` | `0` |
| `biosample_count` | `0` |
| `total_assertions` | `36` |
| `gold_node_ids` | `gold.ecosystem:7872` |

The minted identity is appropriate because no exact ontology term for
estuarine sediment is present in the vendored slice. Exact
hidden/ignored-inclusive searches over `data/raw`, `curation`, `history`,
`research`, `reports`, `data/habitats`, and `conf` found no term request,
deep-research report, history record, causal overlay, or prior exact YAML
review for `habitatmech:GOLD.4849010f40`, `gold.ecosystem:7872`,
`estuary_sediment`, or the exact source path.

The current `curation/decisions.tsv` row selected the wrong broader object:
`ENVO:00000045` `estuary` is the local-scale site for the sediment, not its
material genus. `data/raw/gold_path_triads.tsv` reinforces this distinction for
the exact path: `ENVO:01000020` `estuarine biome` is the broad-scale term in
all seven supporting studies, `ENVO:00000045` `estuary` is the local-scale term
in six studies, and `ENVO:00002007` `sediment` is the medium term in all seven
studies.

The second parent, `habitatmech:GOLD.115edc36f8`, is GOLD's
`Environmental > Aquatic > Marine > Intertidal zone` source-path parent. That
classification edge is useful context, but it is not a strict `is_a` edge:
estuarine sediment is located in an intertidal setting, not a subtype of the
intertidal zone record.

## Evidence

| YAML claim | Maintained evidence | Review |
|---|---|---|
| `identifier: habitatmech:GOLD.4849010f40` | `data/habitats/PATHS.tsv` pins the minted identifier to `estuary_sediment`; `docs/HARMONIZATION.md` documents that minted GOLD identifiers are content hashes of canonical paths. | Supported. |
| `label: Estuary: Sediment` | The exact `data/raw/gold_ecosystem_paths.tsv` row has `leaf_label` `Estuary: Sediment`. | Supported. |
| `habitat_category: AQUATIC` | The GOLD source path starts with `Environmental > Aquatic`. | Supported. |
| `grounding_status: NARROW` | The item-level `GROUND_AS_PARENT` decision keeps the minted identity and produces a `skos:narrowMatch` source mapping. The source concept is narrower than a broader material term. | Supported in principle, but the maintained decision uses `ENVO:00000045` instead of `ENVO:00002007`. |
| `mapping_status: REVIEWED` | The exact `curation/decisions.tsv` row has `review_depth=ITEM`; `src/habitatmech/seed.py` emits `REVIEWED` only when every source concept feeding a record has been reviewed. | Supported. |
| `parent_habitats: ENVO:00000045` | `curation/decisions.tsv` attaches `ENVO:00000045` as the `GROUND_AS_PARENT` object; `data/raw/ontology_terms.tsv` labels that term `estuary`. | Unsupported as a parent. The decision note itself says estuarine sediment is found in an estuary, not the estuary, and the GOLD triad rows classify `estuary` as local scale rather than medium. |
| `parent_habitats: habitatmech:GOLD.115edc36f8` | The edge is generated from GOLD's immediate parent path, `Environmental > Aquatic > Marine > Intertidal zone`. | Unsupported as a parent. `Intertidal zone` is source-path context for the material, not its genus. |
| GOLD `source_attestations` fields | The exact `data/raw/gold_ecosystem_paths.tsv` row has one node, `gold.ecosystem:7872`, and 36 organism assertions. | Supported. |

The target record has no optional curator-authored scientific claims to inspect
beyond hierarchy: no definition, xrefs, environmental parameters,
characteristic taxa, record-level evidence, causal graphs, discussions, or
datasets are present.

## Completeness

Exact hidden/ignored-inclusive searches for `habitatmech:GOLD.4849010f40`,
`gold.ecosystem:7872`, `Environmental > Aquatic > Marine > Intertidal zone >
Estuary: Sediment`, and `estuary_sediment` covered `data/raw`, `curation`,
`history`, `research`, `reports`, generated habitat YAML, and `conf`. They
found:

- the generated target;
- the `data/habitats/PATHS.tsv` row;
- the exact `data/raw/gold_ecosystem_paths.tsv` row;
- the exact `data/raw/gold_path_triads.tsv` broad, local, and medium rows;
- seven `data/raw/gold_studies.tsv` rows that include the exact GOLD path;
- one `data/raw/gold_path_biosamples.tsv` row with 129 biosamples for the
  exact path;
- the maintained item-level `curation/decisions.tsv` row.

Those searches found no target-owned `history` record, target-specific
`curation/causal_graphs/` overlay, maintained `curation/term_requests.tsv` row,
committed deep-research report, label-correspondence residual, or prior exact
YAML review report.

A related exact hidden/ignored-inclusive search found a second GOLD source
concept, `habitatmech:GOLD.aed863b800`, with `label: Estuarine sediment` and
source path `Environmental > Aquatic > Freshwater > Lake > Estuarine sediment`.
It is currently a separate `SEEDED` record under
`data/habitats/aquatic/estuarine_sediment.yaml`, with five GOLD organism
assertions and only a class-level `CONFIRM_UNGROUNDED` row in
`curation/decisions.tsv`. That near-duplicate source needs item-level merge
review before the split can be accepted as deliberate.

The empty optional slots are acceptable for the current maintained inputs. No
term request, causal overlay, or source-inventory row currently provides a
definition, causal graph, environmental parameter, characteristic taxon,
discussion, or dataset for this exact record.

## Findings

| ID | Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| HM-ESTUARY-SEDIMENT-001 | Major | `ENVO:00000045` `estuary` is recorded as a parent even though the reviewed concept denotes sediment, not an estuary. | The target lists `ENVO:00000045` in `parent_habitats`, and its `GROUND_AS_PARENT` decision attaches that term as the broader object. The decision note says "Estuarine sediment is a kind of thing found in an estuary, not the estuary", and the GOLD MIxS rows put `ENVO:00000045` in the `local` slot while putting `ENVO:00002007` `sediment` in `medium` with `share=1.00` across seven studies. | `curation/decisions.tsv`. |
| HM-ESTUARY-SEDIMENT-002 | Major | The inherited `habitatmech:GOLD.115edc36f8` `Intertidal zone` parent is a source-path context, not a strict broader habitat. | The target lists `habitatmech:GOLD.115edc36f8` in `parent_habitats`; that parent is the GOLD path `Environmental > Aquatic > Marine > Intertidal zone`. The exact target path's GOLD triads distinguish estuarine biome, estuary, and sediment as broad/local/medium context terms instead of treating `Intertidal zone` as the sediment material genus. | New maintained source-path parent-edge override in `curation/`, plus `src/habitatmech/seed.py` support for suppressing one inherited GOLD parent edge. |
| HM-ESTUARY-SEDIMENT-003 | Major | `Estuary: Sediment` has not been item-reviewed against the separate `Estuarine sediment` GOLD concept. | `data/habitats/aquatic/estuarine_sediment.yaml` represents `habitatmech:GOLD.aed863b800`, `Environmental > Aquatic > Freshwater > Lake > Estuarine sediment`, as a separate ungrounded record with five GOLD organism assertions. Its only maintained decision is the 2026-08-12 class-level sweep row, so no item-level row explains why two equivalently named estuarine-sediment materials should remain split or be joined with `SAME_AS`. | `curation/decisions.tsv`. |

No blockers or minor findings were found.

## Recommended Edits

| Priority | Edit | Owner | Follow-up validator |
|---:|---|---|---|
| 1 | Update the `habitatmech:GOLD.4849010f40` decision row so `object_id` is `ENVO:00002007`, `object_label` is `sediment`, and `decision` remains `GROUND_AS_PARENT` with `grounding_status=NARROW` and `review_depth=ITEM`. | `curation/decisions.tsv` | `just seed`, `just seed-canary habitatmech:GOLD.4849010f40`, then inspect `data/habitats/aquatic/estuary_sediment.yaml` for the `ENVO:00002007` parent. |
| 2 | Add a maintained parent-edge override that suppresses only `Environmental > Aquatic > Marine > Intertidal zone -> Environmental > Aquatic > Marine > Intertidal zone > Estuary: Sediment`, then teach the GOLD parent pass in `src/habitatmech/seed.py` to honor it. | New curation input plus `src/habitatmech/seed.py` | `just seed`, `just seed-canary habitatmech:GOLD.4849010f40`, then inspect the regenerated target to confirm `habitatmech:GOLD.115edc36f8` is gone. |
| 3 | Item-review `habitatmech:GOLD.aed863b800` against `habitatmech:GOLD.4849010f40` and add a `SAME_AS` decision if the two GOLD rows are the same estuarine-sediment material. | `curation/decisions.tsv` | `just seed`, `just seed-canary habitatmech:GOLD.aed863b800`, `just verify-corpus`. |
| 4 | Add an append-only curation session history record for the future hierarchy and merge-boundary curation. | `history/` | `just validate-history`. |

## Follow-up Checks

- After updating the maintained curation inputs, run `just seed` and the
  relevant `just seed-canary <IDENTIFIER>` calls.
- Confirm the regenerated `data/habitats/aquatic/estuary_sediment.yaml` keeps
  `identifier: habitatmech:GOLD.4849010f40`, `grounding_status: NARROW`, and
  `mapping_status: REVIEWED`.
- Confirm the regenerated target keeps the GOLD `gold.ecosystem:7872`
  attestation and replaces the false `ENVO:00000045` parent with
  `ENVO:00002007`.
- Confirm the regenerated target drops `habitatmech:GOLD.115edc36f8` once the
  source-path parent-edge override exists.
- Confirm future item review either keeps `habitatmech:GOLD.aed863b800`
  separate with explicit evidence or folds it into the estuarine-sediment
  survivor through `SAME_AS`.
- Re-run `just validate data/habitats/aquatic/estuary_sediment.yaml`.
- Re-run `just validate-strict data/habitats/aquatic/estuary_sediment.yaml`.
- Re-run `just term-requests-check`, `just validate-history`,
  `just validate-causal-all`, `just verify-corpus`, and `just report`.

## Additional Notes

All absence checks in this review used hidden/ignored-inclusive `rg
--no-ignore --hidden` over bounded maintained-input, raw, generated-record,
research, history, configuration, and review-report paths.

The current source-path-parent defect is another instance of GOLD
classification context being emitted as `parent_habitats`; similar false edges
have already been reported for path-qualified sediment materials and for the
`coral reef` record.
