# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/terrestrial/fluvial_sediment.yaml`
- Started UTC: 2026-09-28T00:56:12Z
- Finished UTC: 2026-09-28T00:56:12Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.49273d9a48` |
| Label | `Fluvial sediment` |
| Category | `TERRESTRIAL` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Generated path | `data/habitats/terrestrial/fluvial_sediment.yaml` |
| GOLD path | `Environmental > Terrestrial > Soil > Floodplain > Fluvial sediment` |

The target is a class-swept GOLD record for fluvial sediment in a terrestrial
floodplain-soil context. It has one GOLD source attestation, one generated
GOLD source-path parent, no definition, no xrefs, no environmental parameters,
no characteristic taxa, no record-level evidence, no causal graphs, no
discussions, and no datasets.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/terrestrial/fluvial_sediment.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/terrestrial/fluvial_sediment.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the generated term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records validated against the vendored history schema. |
| `just verify-corpus` | Passed; 3206 records were expected, 3206 were found, and `data/habitats/` reproduced exactly from `data/raw/`. |
| `just worklist --status all --out /tmp/habitatmech-fluvial-sediment-worklist.tsv` | Passed; wrote 953 rows to `/tmp/habitatmech-fluvial-sediment-worklist.tsv` and listed this target at row 553 with alluvial, colloidal, lake, and clay sediment candidates. |
| `just report --out /tmp/habitatmech-fluvial-sediment-report.tsv` | Passed; wrote `/tmp/habitatmech-fluvial-sediment-report.tsv` and listed this target with 1 `GOLD` source, 0 source assertions, 1 parent, and 0 populated optional claim collections. |

No required validator was skipped. The target has no causal graph, no
`EvidenceItem` references, and no dataset references for a narrower
record-local reference validator to inspect.

The strict validator left `reports/instance_validation_failures.tsv`
unchanged.

## Identity and Grounding

The generated identifier, label, terrestrial category, GOLD attestation, path
lock, and class-swept `SEEDED` status agree with the committed source
inventory:

- `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.49273d9a48` to
  `fluvial_sediment`.
- `data/raw/gold_ecosystem_paths.tsv` has an exact aggregate row for
  `Environmental > Terrestrial > Soil > Floodplain > Fluvial sediment`.
- `curation/decisions.tsv` has a `CLASS`-depth `CONFIRM_UNGROUNDED` row for
  `habitatmech:GOLD.49273d9a48`; per `docs/HARMONIZATION.md`, `CLASS`
  decisions do not promote records to `REVIEWED`.

The exact GOLD ecosystem-path row has:

| Column | Value |
|---|---|
| `canonical_path` | `Environmental > Terrestrial > Soil > Floodplain > Fluvial sediment` |
| `ecosystem` | `Environmental` |
| `ecosystem_category` | `Terrestrial` |
| `ecosystem_type` | `Soil` |
| `ecosystem_subtype` | `Floodplain` |
| `specific_ecosystem` | `Fluvial sediment` |
| `leaf_label` | `Fluvial sediment` |
| `depth` | `5` |
| `gold_node_count` | `1` |
| `organism_count` | `0` |
| `study_count` | `0` |
| `biosample_count` | `0` |
| `total_assertions` | `0` |
| `gold_node_ids` | `gold.ecosystem:8089` |

The committed side tables contain additional exact-path evidence that is not
summarized by the aggregate organism count:

| Source table | Exact-path row |
|---|---|
| `data/raw/gold_path_biosamples.tsv` | `ecosystem_path_id` 8089 with 4 biosamples. |
| `data/raw/gold_studies.tsv` | GOLD study `Gs0161472`, whose only path is this target. |
| `data/raw/gold_path_triads.tsv` | One exact-path MIxS triad: broad `ENVO:00000446` `terrestrial biome`, local `ENVO:00000255` `flood plain`, and medium `ENVO:00002007` `sediment`, each observed in 1 sample and 1 study with top share 1.00. |

The current `UNGROUNDED` grounding is not an item-level judgment and is too weak
for this target. `ENVO:00002007` `sediment` is vendored and is a true broader
material for the GOLD medium slot. `ENVO:01001203` `alluvial sediment` is also
vendored, is a subclass of `sediment`, and should be examined as a candidate
exact grounding or tighter parent: ENVO defines it as sediment transported by
flowing water and redeposited in a non-marine setting, which is close to the
GOLD `Fluvial sediment` leaf in a floodplain path.

The generated parent edge to `habitatmech:GOLD.07fe1c5b62` is not sound as a
strict broader habitat. That parent is GOLD's
`Environmental > Terrestrial > Soil > Floodplain` source concept. Floodplain is
the MIxS local-scale context for this row, not the material genus of fluvial
sediment.

## Evidence

| YAML claim | Maintained evidence | Review |
|---|---|---|
| `identifier: habitatmech:GOLD.49273d9a48` | `data/habitats/PATHS.tsv` pins the minted GOLD identifier to `fluvial_sediment`; the minted identifier follows from the exact canonical path. | Supported. |
| `label: Fluvial sediment` | The exact `data/raw/gold_ecosystem_paths.tsv` row has `leaf_label` `Fluvial sediment`. | Supported as the source label. |
| `habitat_category: TERRESTRIAL` | The GOLD source path starts with `Environmental > Terrestrial`, and the MIxS broad slot names `ENVO:00000446` `terrestrial biome`. | Supported. |
| `grounding_status: UNGROUNDED` | `curation/decisions.tsv` has a class-level `CONFIRM_UNGROUNDED` row stating no lexical route matched the label. | Weak. `CLASS` depth did not assess this path, and exact side-table evidence plus worklist candidates show this target deserves item-level review against at least `ENVO:01001203` `alluvial sediment` and `ENVO:00002007` `sediment`. |
| `mapping_status: SEEDED` | The only target-specific decision is `review_depth: CLASS`. | Supported. Class-level sweeps deliberately do not count as `REVIEWED`. |
| `parent_habitats: habitatmech:GOLD.07fe1c5b62` | GOLD's immediate parent path is `Environmental > Terrestrial > Soil > Floodplain`, generated as a terrestrial-soil `Floodplain` source-path record. | Unsupported as a habitat parent. Floodplain is local context, not a strict broader sediment material. |
| GOLD `source_attestations` fields | The exact `data/raw/gold_ecosystem_paths.tsv` row has one node, `gold.ecosystem:8089`, and no organism assertions. | Supported. |

The reviewed YAML does not carry the exact-path GOLD side-table rows. That is a
current model limitation rather than a hand-editable omission on this record:
the source attestation is emitted from `data/raw/gold_ecosystem_paths.tsv`, while
the `gold_path_biosamples`, `gold_studies`, and `gold_path_triads` tables are
report/worklist evidence for a curator.

## Completeness

Exact hidden/ignored-inclusive searches for `habitatmech:GOLD.49273d9a48`,
`49273d9a48`, `gold.ecosystem:8089`, `fluvial_sediment`,
`Fluvial sediment`, and
`Environmental > Terrestrial > Soil > Floodplain > Fluvial sediment` covered
`data/habitats`, `data/raw`, `curation`, `history`, `research`, `reports`,
`conf`, `src`, `tests`, `docs`, the `justfile`, and `README.md`. They found:

- the generated target;
- the `data/habitats/PATHS.tsv` row;
- the `CLASS`-depth `curation/decisions.tsv` row;
- the exact `data/raw/gold_ecosystem_paths.tsv` row;
- one exact `data/raw/gold_path_biosamples.tsv` row;
- one exact `data/raw/gold_studies.tsv` row;
- the three exact `data/raw/gold_path_triads.tsv` rows.

Follow-up hidden/ignored-inclusive searches for the GOLD parent path and
vendored ENVO candidate rows found:

- the generated GOLD `Floodplain` source-path parent;
- the relevant vendored ENVO rows for `flood plain`, `terrestrial biome`,
  `sediment`, and `alluvial sediment`.

The target-term search found no target-specific item-level decision, term
request, history record, causal overlay, habitat research report, or prior
exact YAML review report for this exact target.

No characteristic taxa, environmental parameters, causal graphs, discussions,
or datasets are expected on this single-source class-swept GOLD leaf.

## Findings

### Blocker

None found.

### Major

| ID | Finding | Maintained owner |
|---|---|---|
| M1 | The current source concept remains class-swept `UNGROUNDED`, but the exact GOLD path has MIxS evidence naming `ENVO:00002007` `sediment` as the sampled medium, and `ENVO:01001203` `alluvial sediment` is a vendored subclass of sediment whose definition is close to fluvial sediment in a terrestrial floodplain setting. The target needs an item-level decision instead of the mechanical `CLASS` row. | Replace or supersede the row for `habitatmech:GOLD.49273d9a48` in `curation/decisions.tsv` with an `ITEM`-depth decision, likely `GROUND` to `ENVO:01001203` if alluvial sediment is accepted as exact, or `GROUND_AS_PARENT` to the tightest confirmed broader sediment term. |
| M2 | `parent_habitats` keeps the GOLD source-path locality as an `is_a` edge: `data/habitats/terrestrial/fluvial_sediment.yaml` says fluvial sediment is a kind of `Floodplain` (`habitatmech:GOLD.07fe1c5b62`). The GOLD and MIxS evidence treat flood plain as local context; the material parent is sediment. | Maintained GOLD path-parent suppression consumed by `src/habitatmech/seed.py`; if curation keeps this target under a minted identifier, a curated definition in `curation/term_requests.tsv` should use `parent_mode: REPLACE` to remove the inherited floodplain edge. |

### Minor

None found.

## Recommended Edits

1. Add an item-level `curation/decisions.tsv` row for
   `habitatmech:GOLD.49273d9a48`.
2. Test `ENVO:01001203` `alluvial sediment` as an exact grounding target. If it
   is too narrow or otherwise semantically wrong, keep the minted identity and
   ground it as a child of `ENVO:00002007` `sediment` or a tighter confirmed
   sediment term.
3. Suppress `habitatmech:GOLD.07fe1c5b62` as an inherited source-path parent;
   preserve flood plain as context rather than as an `is_a` parent.
4. Regenerate with:

```bash
just seed
just seed-canary habitatmech:GOLD.49273d9a48
just seed-apply --force
```

No hand edit is recommended for `data/habitats/terrestrial/fluvial_sediment.yaml`.

## Follow-up Checks

After the future curation edit:

1. Re-read the regenerated record and confirm the grounding target is either
   the verified alluvial-sediment identity or a NARROW child of a sediment
   term.
2. Confirm it no longer lists `habitatmech:GOLD.07fe1c5b62` as a
   `parent_habitats` entry.
3. Confirm the GOLD source attestation for `gold.ecosystem:8089` is preserved.
4. Run:

```bash
just validate data/habitats/terrestrial/fluvial_sediment.yaml
just validate-strict data/habitats/terrestrial/fluvial_sediment.yaml
just validate-causal-all
just verify-corpus
just term-requests-check
just validate-history
```

## Additional Notes

This review intentionally makes no generated YAML, page, decision, or term
request edits. The YAML faithfully records the current seeded result; the
remaining curation task is to turn the class-level placeholder into a genuine
item-level decision and maintain the stricter hierarchy for this fluvial
sediment material.
