# YAML Record Review: Artesian spring

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/aquatic/artesian_spring.yaml
- Started UTC: 2026-09-21T17:50:06Z
- Finished UTC: 2026-09-21T17:50:06Z
- Verdict: needs curation

## Target

The target is the generated `HabitatRecord` at `data/habitats/aquatic/artesian_spring.yaml`.

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.19b5876c23` |
| Label | `Artesian spring` |
| Category | `AQUATIC` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Source concepts | GOLD `gold.ecosystem:7660` |
| Locked stem | `artesian_spring` in `data/habitats/PATHS.tsv` |

This review covers GOLD `Environmental > Aquatic > Artesian spring`, a GOLD level-3 ecosystem-type concept emitted as one HabitatMech-minted record.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/artesian_spring.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/aquatic/artesian_spring.yaml --quiet` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; 3,206 expected records, 3,206 records on disk, 0 missing, 0 extra, 0 differing. |
| Reference validator | Not checked: the generated record has no DOI/PMID/URL `EvidenceItem`, no causal-edge evidence, and no curated causal overlay. |

## Identity and Grounding

| Claim | Evidence | Assessment |
|---|---|---|
| The generated record denotes the GOLD `Artesian spring` source concept. | `data/raw/gold_ecosystem_paths.tsv` has canonical path `Environmental > Aquatic > Artesian spring`, leaf `Artesian spring`, depth `3`, three GOLD node IDs `gold.ecosystem:7660\|gold.ecosystem:7661\|gold.ecosystem:7662`, `organism_count=1`, and `total_assertions=1`. | Supported exactly. |
| The locked generated identifier is stable. | `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.19b5876c23` to stem `artesian_spring`; the identifier is the SHA1-based minted key for GOLD path `Environmental > Aquatic > Artesian spring`. | Supported exactly. |
| The record has not been item-reviewed yet. | `curation/decisions.tsv` has one row for `habitatmech:GOLD.19b5876c23`, but its `review_depth` is `CLASS`, and the note explicitly says the class-level sweep did not assess whether the concept is a habitat. The generated history carries the same `[CLASS-level]` limitation. | Needs curation; an exact grounding absence and term-request candidate require an item-level review of this source path and candidate broader terms. |
| The vendored ontology slice has a broader spring term but no exact artesian-spring term. | A hidden/ignored-inclusive search for `artesian` across `data/raw`, `curation`, `history`, `research/habitats`, and prior `reports/yaml_record_review` found GOLD rows and contextual prose but no `data/raw/ontology_terms.tsv` label or synonym containing `artesian`; `data/raw/ontology_terms.tsv` has `ENVO:00000027` `spring`, defined as a surface landform where groundwater or steam flows out of the ground. | Supports keeping the concept minted and using `ENVO:00000027` as the likely maintained parent after item review. |
| The generated `ENVO:00002030` parent is inherited from the GOLD source path. | `data/raw/gold_ecosystem_paths.tsv` has parent path `Environmental > Aquatic`, which resolves to `ENVO:00002030` `aquatic biome`; `data/habitats/PATHS.tsv` maps `ENVO:00002030` to `aquatic_biome`, and the target record lists `ENVO:00002030` in `parent_habitats`. | Mechanically supported but biologically over-scoped; an artesian spring is a spring landform, not a biome with ecological climax communities. |

## Evidence

The generated record has no record-level `evidence` entries and no `causal_graphs`.

| Claim | Evidence | Assessment |
|---|---|---|
| The GOLD source attestation preserves the source path and first source ID. | `data/raw/gold_ecosystem_paths.tsv` has `gold.ecosystem:7660\|gold.ecosystem:7661\|gold.ecosystem:7662` on `Environmental > Aquatic > Artesian spring`; the generated `source_attestations` entry names `gold.ecosystem:7660` and notes that three GOLD ecosystem node IDs share this path. | Supported exactly. |
| The generated GOLD assertion count is source-local. | The canonical GOLD row reports `organism_count=1`, which matches the generated `assertion_count: 1` and `assertion_unit: ORGANISM`. | Supported exactly. |
| The direct child `Acidic` row is correctly item-reviewed as a non-habitat qualifier. | `curation/decisions.tsv` records `habitatmech:GOLD.8ee6ff626d` as `NOT_APPLICABLE` at `ITEM` depth and explains that GOLD `Environmental > Aquatic > Artesian spring > Acidic` is a pH band qualifying the parent node, not a habitat in its own right. | Supported; the open issue is that this non-habitat node still remains in the generated parent chain for `Environmental > Aquatic > Artesian spring > Acidic > Sediment`, as already recorded by `HM-ACIDIC-001`. |

## Completeness

- The generated record is complete enough for a class-swept source concept: it has its stable HabitatMech identifier, the GOLD source attestation, the generated class-sweep event, and the generated seed event.
- The record correctly omits record-level evidence, causal graphs, characteristic taxa, and environmental parameters because there is no maintained target-specific curation row, term request, or causal overlay yet.
- The target is not complete enough for a defended `UNGROUNDED` curation state because the sole decision is a class-level lexical no-match sweep, not an item-level check of artesian springs against ENVO `spring`, `freshwater spring`, `groundwater`, or related near misses.
- The immediate hierarchy is incomplete: `parent_habitats` currently asserts that an artesian spring is an aquatic biome and does not assert the stricter spring genus available as `ENVO:00000027`.
- Hidden/ignored-inclusive exact searches covered `data/raw`, `data/habitats/PATHS.tsv`, `curation`, `history`, `curation/causal_graphs`, `reports/yaml_record_review`, and `research/habitats` for `habitatmech:GOLD.19b5876c23`, `gold.ecosystem:7660`, `artesian_spring`, `Artesian spring`, and `Environmental > Aquatic > Artesian spring`. They found the raw GOLD row, the locked slug, the class-sweep decision, child-path raw rows, and contextual mentions in the prior `acidic` reviews; they found no target-specific term request, causal overlay, history record, research report, or prior YAML review for `artesian_spring`.

## Findings

| ID | Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| `HM-ARTESIAN-SPRING-001` | Major | `Artesian spring` is still only class-reviewed. The current `CONFIRM_UNGROUNDED` row records a lexical no-match cohort, explicitly says it did not assess whether the concept is a habitat, and therefore cannot defend the final `UNGROUNDED` state or a future ENVO term request. | `curation/decisions.tsv` row `habitatmech:GOLD.19b5876c23` has `review_depth=CLASS`; `docs/HARMONIZATION.md` states that class decisions do not establish whether the concept is a real habitat and do not promote a record to `REVIEWED`; the record remains `mapping_status: SEEDED`. | Replace the class-sweep row with an item-depth `curation/decisions.tsv` row for `habitatmech:GOLD.19b5876c23` after checking the GOLD path against available spring and groundwater terms. |
| `HM-ARTESIAN-SPRING-002` | Major | The record inherits a false `ENVO:00002030` `aquatic biome` parent from the GOLD `Environmental > Aquatic` path. An artesian spring is a spring landform and should be narrower than `ENVO:00000027` `spring`, not a biome determined by ecological climax communities adapted to life in or on water. | `data/habitats/aquatic/artesian_spring.yaml` lists `ENVO:00002030`; `data/raw/ontology_terms.tsv` defines `ENVO:00002030` as `aquatic biome` and `ENVO:00000027` as `spring`; the hidden/ignored-inclusive `artesian` search found no exact vendored term for artesian spring. | Add a `curation/term_requests.tsv` row for `habitatmech:GOLD.19b5876c23` that uses `ENVO:00000027` as the authored parent and `parent_mode=REPLACE` to drop the false inherited biome parent. |

No blocker or minor findings found.

## Recommended Edits

1. Replace the class-sweep decision in `curation/decisions.tsv` for `habitatmech:GOLD.19b5876c23` with an item-level decision that confirms GOLD `Environmental > Aquatic > Artesian spring` is a real spring habitat with no exact term in the current vendored ENVO slice.
2. Add a curated definition and hierarchy row in `curation/term_requests.tsv` for `habitatmech:GOLD.19b5876c23`, with `parent_class` set to `ENVO:00000027`, `parent_label` set to `spring`, and `parent_mode=REPLACE` so regeneration drops the false inherited `ENVO:00002030` parent.
3. Regenerate `data/habitats/aquatic/artesian_spring.yaml` with `just seed-canary habitatmech:GOLD.19b5876c23` and inspect the generated target before any wider seed run.
4. Re-check `data/habitats/aquatic/acidic.yaml` and `data/habitats/aquatic/sediment__4ec76487.yaml` after the earlier non-habitat hierarchy bug is fixed, because `Acidic` should become an environmental parameter on the artesian-sediment child instead of remaining a parent node.

## Follow-up Checks

| Edit | Narrowest proving check |
|---|---|
| Promote the source path from class sweep to item review. | Re-read the new `curation/decisions.tsv` row and confirm it keys `habitatmech:GOLD.19b5876c23`, uses `review_depth=ITEM`, and cites the inspected GOLD path and spring near-miss terms. |
| Suppress the false aquatic-biome parent edge. | Re-read the new `curation/term_requests.tsv` row, run `just seed-canary habitatmech:GOLD.19b5876c23`, and confirm `data/habitats/aquatic/artesian_spring.yaml` keeps the GOLD source attestation, drops `ENVO:00002030`, and gains `ENVO:00000027`. |
| Validate the regenerated record and corpus. | `just validate data/habitats/aquatic/artesian_spring.yaml`, `just validate-strict data/habitats/aquatic/artesian_spring.yaml --quiet`, `just validate-history`, `just term-requests-check`, and `just verify-corpus --max-diffs 1`. |
| Prevent downstream non-habitat parent leakage. | After a seed run, inspect `data/habitats/aquatic/sediment__4ec76487.yaml` and confirm the GOLD `Acidic` qualifier no longer appears in `parent_habitats`. |

## Additional Notes

- GOLD also lists `Environmental > Aquatic > Artesian spring > Acidic` and `Environmental > Aquatic > Artesian spring > Acidic > Sediment`; the existing `20260921T090914Z-acidic.md` review already found that the reviewed `Acidic` pH band still incorrectly participates in generated habitat hierarchy.
- `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`, and `data/raw/gold_studies.tsv` contain rows for the child `Environmental > Aquatic > Artesian spring > Acidic > Sediment` path but no direct rows for the parent `Environmental > Aquatic > Artesian spring` path. The generated `assertion_count: 1` comes from `gold_ecosystem_paths.tsv` organism count, not from those child-path biosamples.
