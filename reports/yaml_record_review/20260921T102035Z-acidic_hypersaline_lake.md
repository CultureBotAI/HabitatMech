# YAML Record Review: Acidic hypersaline lake

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/aquatic/acidic_hypersaline_lake.yaml
- Started UTC: 2026-09-21T10:20:35Z
- Finished UTC: 2026-09-21T10:20:35Z
- Verdict: needs curation

## Target

The target is the generated `HabitatRecord` at `data/habitats/aquatic/acidic_hypersaline_lake.yaml`.

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.2a6cc2b868` |
| Label | `Acidic hypersaline lake` |
| Category | `AQUATIC` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Source concept | collapsed GOLD nodes `gold.ecosystem:7986` and `gold.ecosystem:7987` |
| Source path | `Environmental > Aquatic > Acidic > Acidic hypersaline lake` |
| Locked stem | `acidic_hypersaline_lake` in `data/habitats/PATHS.tsv` |

This review covers the single GOLD source concept represented by `habitatmech:GOLD.2a6cc2b868`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/acidic_hypersaline_lake.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/aquatic/acidic_hypersaline_lake.yaml --quiet` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; 3,206 expected records, 3,206 records on disk, 0 missing, 0 extra, 0 differing. |
| Reference validator | Not checked: this record has no DOI/PMID/URL `EvidenceItem`, no causal-edge evidence, and no target-specific `curation/causal_graphs/` overlay. |

## Identity and Grounding

The record denotes the GOLD source concept at `Environmental > Aquatic > Acidic > Acidic hypersaline lake`. `data/raw/gold_ecosystem_paths.tsv` has an exact row for that path with leaf `Acidic hypersaline lake`, depth 4, `gold_node_count=2`, `organism_count=1`, `total_assertions=1`, and nodes `gold.ecosystem:7986|gold.ecosystem:7987`.

The current `UNGROUNDED` value follows from a `CONFIRM_UNGROUNDED` row in `curation/decisions.tsv`, but the row is only a class-level lexical no-match sweep. The row explicitly says habitathood was not assessed and the source is not yet a term-request candidate. That is consistent with `mapping_status: SEEDED`, but it also means no curator has inspected whether this source path is a real acidic hypersaline-lake habitat or which narrower-than-ENVO identity it should carry.

The vendored ontology slice has `ENVO:01001020` `hypersaline lake`, defined as a lake primarily composed of water with dissolved salts above the concentration of ocean water. That term is broader than GOLD's acid-specific leaf because it lacks the acidity constraint. Ignored and hidden searches over `data`, `curation`, `research`, and `reports`, excluding only generated `data/text_map/` cache files, found no exact `acidic hypersaline` ontology term, term request, decision rationale, research report, or previous target review.

The generated parent is unsound. `parent_habitats` points to `habitatmech:GOLD.90a084a03e`, the GOLD `Environmental > Aquatic > Acidic` parent, but that parent is item-reviewed `NOT_APPLICABLE` because it denotes a pH band qualifying the aquatic parent rather than a habitat.

## Evidence

| Claim | Evidence | Assessment |
|---|---|---|
| The source concept and filename are resolved correctly. | `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.2a6cc2b868` to `acidic_hypersaline_lake`; the exact GOLD source path hashes to that identifier and appears in the target YAML. | Supported. |
| The GOLD source attestation preserves the collapsed source concept. | `data/raw/gold_ecosystem_paths.tsv` lists two GOLD node IDs for the exact path and the YAML names the first, `gold.ecosystem:7986`, with a note that two IDs share the path. | Supported. |
| `assertion_count: 1` is a GOLD organism count. | The exact raw ecosystem-path row has `organism_count=1` and `total_assertions=1`. | Supported. |
| The exact source path has additional MIxS, biosample, or study context. | Exact ignored and hidden searches for the full source path in `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`, and `data/raw/gold_studies.tsv` found no row for the exact path. | Not supported by current committed raw tables. |
| Existing causal evidence belongs to this target. | The only `*hypersaline*` causal overlay found was `curation/causal_graphs/hypersaline_water.yaml`, targeting `ENVO:00002012` `hypersaline water`. | Not supported for this target-specific minted GOLD lake concept. |

The child GOLD concepts under the same path are present on disk:

- `data/habitats/aquatic/sediment__7e21c5d8.yaml` for `Environmental > Aquatic > Acidic > Acidic hypersaline lake > Sediment`
- `data/habitats/aquatic/microbial_mat__54ad7767.yaml` for `Environmental > Aquatic > Acidic > Acidic hypersaline lake > Microbial mat`

Those child records show the source path is used as a generated hierarchy bridge. They are not independent evidence that the parent source has been item-reviewed.

## Completeness

The generated record preserves all current raw GOLD source facts: identifier, label, path, first source node ID, the collapsed-node note, and the one GOLD organism assertion.

Material curation remains incomplete:

- The class-level `curation/decisions.tsv` row must be replaced with an item-level decision that decides the source path, not just the lexical label.
- A reviewed broader parent should be selected if the concept is retained as a real habitat. `ENVO:01001020` `hypersaline lake` is the apparent near parent in the vendored slice; `habitatmech:GOLD.90a084a03e` is not a habitat.
- A term request should be considered if item review confirms an acidic hypersaline lake is a real habitat and no existing ontology class is exact.
- The child sediment and microbial-mat branches should be rechecked after parent repair so they keep a true acidic-hypersaline-lake context when the source parent is promoted, redirected, or given a new term.

No environmental parameters, characteristic taxa, causal graph, discussions, or datasets are currently supported for this sparse GOLD-only record.

## Findings

| ID | Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| `HM-ACIDIC-HYPERSALINE-LAKE-001` | Major | The source concept still needs item-level curation. `mapping_status: SEEDED` is correct because the only maintained decision is a `CLASS`-depth lexical no-match sweep; that sweep did not assess whether `Environmental > Aquatic > Acidic > Acidic hypersaline lake` denotes a real habitat, whether it should attach `ENVO:01001020` `hypersaline lake` as a broader parent, or whether it needs a novel acidic-hypersaline-lake term. | `curation/decisions.tsv` row `habitatmech:GOLD.2a6cc2b868` has `review_depth=CLASS` and says habitathood was not assessed; `data/raw/ontology_terms.tsv` contains a broader `ENVO:01001020` `hypersaline lake` term but no exact acidic-hypersaline term was found with an ignored/hidden search. | `curation/decisions.tsv`; possibly `curation/term_requests.tsv` after item review. |
| `HM-ACIDIC-HYPERSALINE-LAKE-002` | Major | `parent_habitats` points to a reviewed non-habitat pH band. The generated parent `habitatmech:GOLD.90a084a03e` is the GOLD `Acidic` source node, which is item-reviewed `NOT_APPLICABLE`. A pH quality is not a strict broader habitat for an acidic hypersaline lake. | The target YAML lists `habitatmech:GOLD.90a084a03e`; that parent's decision row says `Acidic` is a pH band qualifying the parent node and belongs in environmental parameters; `docs/CURATION.md` says `parent_habitats` is an is-a claim. | `src/habitatmech/seed.py`, or a maintained parent-edge override consumed by the seeder. |

## Recommended Edits

1. Replace the class-depth `CONFIRM_UNGROUNDED` row for `habitatmech:GOLD.2a6cc2b868` in `curation/decisions.tsv` with an item-depth decision. If the source is retained as a distinct real habitat, use `GROUND_AS_PARENT` with `ENVO:01001020` `hypersaline lake` unless item review finds a better exact term.
2. If no exact ontology term exists after item review, add a `curation/term_requests.tsv` row for a new acidic hypersaline lake term using `ENVO:01001020` as the genus.
3. Fix the maintained GOLD parent-path generation so this target no longer inherits the item-rejected `Environmental > Aquatic > Acidic` pH-band node as a strict parent.
4. Re-evaluate `sediment__7e21c5d8.yaml` and `microbial_mat__54ad7767.yaml` after the parent concept is repaired, because both children currently point to this sparse, class-reviewed bridge.

No direct edit should be made to `data/habitats/aquatic/acidic_hypersaline_lake.yaml`.

## Follow-up Checks

| Edit | Narrowest proving check |
|---|---|
| Add the item-level decision for `habitatmech:GOLD.2a6cc2b868`. | Re-read the exact `curation/decisions.tsv` row and confirm `review_depth=ITEM` with an inspected source-path rationale. |
| Add or reject an acidic-hypersaline-lake term request. | Rebuild with `just term-requests`, then run `just term-requests-check`. |
| Regenerate this canary. | Run `just seed-canary habitatmech:GOLD.2a6cc2b868` and inspect `data/habitats/aquatic/acidic_hypersaline_lake.yaml`. |
| Preserve valid child context. | Run `just seed-canary habitatmech:GOLD.9eaa63ad72 habitatmech:GOLD.9b3b1cd806` and confirm the sediment and microbial-mat children no longer rely on a false pH-band parent. |
| Validate the regenerated corpus. | Run `just validate data/habitats/aquatic/acidic_hypersaline_lake.yaml`, `just validate-strict data/habitats/aquatic/acidic_hypersaline_lake.yaml --quiet`, `just validate-history`, `just verify-corpus --max-diffs 1`, and `just render-check`. |
| Verify downstream products. | Rebuild KGX and SSSOM products and confirm exported hierarchy edges no longer assert `habitatmech:GOLD.2a6cc2b868` as a child of `habitatmech:GOLD.90a084a03e`. |

## Additional Notes

This review intentionally leaves generated YAML unchanged. The current record is reproducible and schema-valid; the problem is that the reproducible maintained inputs are still too weak to publish a reviewed acidic-hypersaline-lake model.
