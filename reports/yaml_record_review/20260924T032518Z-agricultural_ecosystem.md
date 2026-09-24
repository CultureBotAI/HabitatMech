# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/terrestrial/agricultural_ecosystem.yaml
- Started UTC: 2026-09-24T03:20:48Z
- Finished UTC: 2026-09-24T03:25:18Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/terrestrial/agricultural_ecosystem.yaml` |
| Class | `HabitatRecord` |
| Identifier | `ENVO:00000077` |
| Label | `agricultural ecosystem` |
| Category | `TERRESTRIAL` |
| Grounding status | `EXACT` |
| Mapping status | `REVIEWED` |
| Maintained owner | Generated from `data/raw/gold_ecosystem_paths.tsv`, `data/raw/prego_habitats.tsv`, `data/raw/prego_habitat_taxa.tsv`, the vendored ontology slice, and `curation/decisions.tsv`; `data/habitats/` is generated and remains read-only |

This generated record merges two reviewed source concepts onto `ENVO:00000077`:

| Source concept | Deterministic key | Maintained input | Decision |
|---|---|---|---|
| GOLD `Environmental > Terrestrial > Soil > Agricultural land` | `habitatmech:GOLD.a0c9778ffa`, from `sha1("GOLD:Environmental > Terrestrial > Soil > Agricultural land")[:10]` | `data/raw/gold_ecosystem_paths.tsv` row for `gold.ecosystem:5860\|gold.ecosystem:7674` | `curation/decisions.tsv` item-level `REVIEW` |
| PREGO `ENVO:00000077` | `habitatmech:PREGO.68f4ab3447`, from `sha1("PREGO:ENVO:00000077")[:10]` | `data/raw/prego_habitats.tsv` row for `ENVO:00000077` | `curation/decisions.tsv` item-level `REVIEW` |

`data/habitats/PATHS.tsv` pins `ENVO:00000077` to the stable `agricultural_ecosystem` file stem.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/terrestrial/agricultural_ecosystem.yaml` | Passed: `No issues found` |
| `just validate-strict data/habitats/terrestrial/agricultural_ecosystem.yaml` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| Target causal overlay validator | Not applicable: exact ignored/hidden-inclusive searches found no `curation/causal_graphs/` overlay for `agricultural_ecosystem`, `ENVO:00000077`, `habitatmech:GOLD.a0c9778ffa`, or `habitatmech:PREGO.68f4ab3447` |
| `just validate-causal-all` | Passed: 32 causal-graph curation files with 32 graphs |
| Reference validator | Not applicable: this record has no claim-level `EvidenceItem` references and no causal overlay with literature-backed edges |
| `just term-requests-check` | Passed: term-request table is current with 109 terms |
| `just validate-history` | Passed: no issues found; 77 history records valid against `src/habitatmech/schema/history.yaml` |
| `just verify-corpus --max-diffs 1` | Passed: expected 3,206 records, found 3,206, 0 missing, 0 extra, 0 differing |
| `just worklist --limit 2000` | Passed: 0 ungrounded records still undecided, 1,810 decisions on file |
| `just report` | Passed: corpus report completed for 3,206 records |
| `git diff --check` | Passed |

## Identity and Grounding

The PREGO side is an exact self-grounding. `data/raw/prego_habitats.tsv` keys the source row by `ENVO:00000077`, and `ingest_prego()` uses that CURIE directly as the default identifier while still minting `habitatmech:PREGO.68f4ab3447` as the curation decision key. The row carries 31 PREGO taxa, 31 direct assertions, maximum PREGO score `4`, and the evidence channels `annotated_genomes_isolates|environmental_samples`; the generated source attestation preserves those values as `assertion_count: 31`, `assertion_unit: TAXON`, `score: 4.0`, and the same channel pipe.

The GOLD side is a close synonym grounding. The committed GOLD path row is:

```text
Environmental > Terrestrial > Soil > Agricultural land
```

with two GOLD ecosystem node ids, 138 organism assertions, and canonical source id `gold.ecosystem:5860`; the generated attestation preserves the first node id, the 138 `ORGANISM` count, the full source path, and the note that two GOLD ecosystem node ids share the path.

Both source concepts have `ITEM`-level `REVIEW` rows dated `2026-08-13` in `curation/decisions.tsv`, so the generated `mapping_status: REVIEWED` is mechanically supported. Exact ignored/hidden-inclusive searches for `habitatmech:GOLD.a0c9778ffa`, `habitatmech:PREGO.68f4ab3447`, `ENVO:00000077`, and `agricultural_ecosystem` covered `curation/`, `history/`, `research/`, `data/raw/`, `data/habitats/PATHS.tsv`, and `reports/yaml_record_review/`; they found the two decision rows, raw GOLD/PREGO rows, the path pin, and no prior exact YAML review report before this file was written.

The ontology identity itself is internally consistent: `data/raw/ontology_terms.tsv` has `ENVO:00000077` with label `agricultural ecosystem` and exact ENVO synonyms including `agricultural land`, and `data/raw/ontology_subclass_edges.tsv` makes it a subclass of `ENVO:01001828` `anthropised ecosystem`.

The generated hierarchy is not fully sound. `ENVO:01001828` is the direct ontology parent and is broader than the record. `ENVO:00001998` `soil`, however, is not an ENVO parent of `agricultural ecosystem`; it is imported by the GOLD parent-path second pass because the reviewed GOLD source path sits under `Environmental > Terrestrial > Soil`. That parent is true of GOLD's soil-scoped submission path, but it is not broader than the merged ontology/PREGO record, which also includes farms, barns, dairies, feedlots, stockyards, corrals, and similar non-soil agricultural ecosystem senses from the ENVO and PREGO synonym sets.

## Evidence

Supported claims:

| Claim | Maintained evidence | Assessment |
|---|---|---|
| `identifier: ENVO:00000077`, label `agricultural ecosystem`, and `EXACT` grounding from PREGO | `data/raw/prego_habitats.tsv` row for `ENVO:00000077`; `src/habitatmech/seed.py` self-grounds PREGO rows by default | Supported |
| GOLD attestation for `Environmental > Terrestrial > Soil > Agricultural land` | `data/raw/gold_ecosystem_paths.tsv` row with node ids `gold.ecosystem:5860\|gold.ecosystem:7674` and 138 organism assertions | Supported |
| PREGO attestation count, score, and channels | `data/raw/prego_habitats.tsv` row with `taxon_count=31`, `direct_assertion_count=31`, `max_prego_score=4`, and channels `annotated_genomes_isolates|environmental_samples` | Supported |
| Twenty-five generated PREGO taxon rows | Top 25 rows for `ENVO:00000077` in `data/raw/prego_habitat_taxa.tsv`; rank 20 has an empty upstream label and therefore correctly omits optional `taxon_label` | Supported as observed PREGO associations; no row is upgraded with `is_characteristic: true` |
| ENVO exact synonyms and PREGO related synonyms | `data/raw/ontology_terms.tsv` and `data/raw/prego_habitats.tsv` | Supported as source labels/lexical variants, including PREGO's stemmed or pluralized variants |

Unsupported or over-scoped claims:

- The `ENVO:00001998` parent over-scopes one GOLD path's soil context to the merged `ENVO:00000077` record. `parent_habitats` asserts a strict broader-than relationship, but `soil` is a material, while `agricultural ecosystem` is an ecosystem covering soil and non-soil agricultural facilities and lands.

The record has no authored definition, claim-level evidence, environmental parameters, causal graph, discussion links, datasets, external xrefs, or quality flags. No current maintained source row claims those fields for this record.

## Completeness

The record is complete for the current raw GOLD and PREGO inputs:

| Slot | Status |
|---|---|
| Definition | Empty because the vendored `ENVO:00000077` row has no definition |
| GOLD source attestation | Complete for the one raw canonical path row and two collapsed GOLD node ids |
| PREGO source attestation | Complete for count, source score, and evidence channels |
| PREGO characteristic taxa | Complete for the 25 committed top-ranked PREGO rows; `candidate_pool: 31` preserves the larger upstream candidate count |
| Causal graphs | None expected; ignored/hidden-inclusive searches found no target overlay |
| Research and history | No target-specific artifact found; ignored/hidden-inclusive searches found only the path lock plus one unrelated sheep/goat research note mentioning `ENVO:00000077` as a non-host setting |

Exact ignored/hidden-inclusive searches for `Agricultural land` and `ENVO:00000077` in `data/raw/bacdive_isolation_sources.tsv`, `data/raw/isolation_source_groundings.tsv`, `data/raw/environment_parameters.tsv`, `data/raw/madin_habitats.tsv`, and curation xref/redirect tables found no BacDive, Madin, environment-parameter, or external-xref contribution that should have appeared in this generated record.

## Findings

**Blocker**

None found.

**Major**

- `parent_habitats` contains `ENVO:00001998` `soil`, which is a false parent for the merged `ENVO:00000077` `agricultural ecosystem` record. The parent is introduced by the GOLD parent-path linker in `src/habitatmech/seed.py` after `Environmental > Terrestrial > Soil > Agricultural land` has already been merged into the broader ENVO/PREGO agricultural ecosystem concept. Future curation should either split the GOLD soil-scoped source concept from `ENVO:00000077` with an item-level `curation/decisions.tsv` decision, or teach the GOLD parent-path pass to suppress a parent when merging a source path into a broader ontology record would make that path context false for the merged identity.

**Minor**

None found.

## Recommended Edits

1. Fix the false `soil` parent at the maintained input or generator layer, not in `data/habitats/terrestrial/agricultural_ecosystem.yaml`.
2. If curators decide the GOLD source concept is narrower than `ENVO:00000077`, update the existing `curation/decisions.tsv` row for `habitatmech:GOLD.a0c9778ffa` from `REVIEW` to an item-level `GROUND_AS_PARENT` decision and record the correct strictly broader target.
3. If curators keep the GOLD source concept merged with `ENVO:00000077`, update `src/habitatmech/seed.py` so the second-pass GOLD parent-path link does not attach `ENVO:00001998` to this merged ontology/PREGO record.
4. Regenerate from maintained inputs with `just seed`, canary the affected identifier, run the appropriate `just seed-apply --force` pass, and confirm the regenerated `agricultural_ecosystem.yaml` retains `ENVO:01001828` while dropping the false `ENVO:00001998` parent.

## Follow-up Checks

Re-run the same focused validation set after the hierarchy fix:

| Scope | Command |
|---|---|
| Target schema | `just validate data/habitats/terrestrial/agricultural_ecosystem.yaml` |
| Closed-schema validation | `just validate-strict data/habitats/terrestrial/agricultural_ecosystem.yaml` |
| Causal overlays | `just validate-causal-all` |
| Term-request exports | `just term-requests-check` |
| History | `just validate-history` |
| Corpus reproduction | `just verify-corpus --max-diffs 1` |
| Worklist/report sanity | `just worklist --limit 2000` and `just report` |
| Diff hygiene | `git diff --check` |

Manual follow-up should verify that:

- `parent_habitats` contains only strictly broader habitat terms after the GOLD path parent is recomputed.
- `habitatmech:GOLD.a0c9778ffa` still has an item-level decision and a source attestation in exactly one regenerated record.
- `habitatmech:PREGO.68f4ab3447` remains reviewed and continues to support the PREGO attestation for `ENVO:00000077`.

## Additional Notes

- Exact report pre-existence was checked with `find reports/yaml_record_review -maxdepth 1 -type f -name '*-agricultural_ecosystem.md' -print`; ignored files were included by `find`, and no prior exact report was found.
- The GOLD MIxS triad rows for `Environmental > Terrestrial > Soil > Agricultural land` are consistent with the problem: current GOLD samples mostly use `ENVO:00000446` `terrestrial biome` as broad scale, `ENVO:00000114` `agricultural field` as local scale, and `ENVO:00002259` `agricultural soil` as medium. They support treating the submitted path as soil in an agricultural land context, not as proof that `soil` is broader than the whole ENVO/PREGO `agricultural ecosystem` record.
