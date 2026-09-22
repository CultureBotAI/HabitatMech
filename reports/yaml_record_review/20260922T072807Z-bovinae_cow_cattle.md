# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/bovinae_cow_cattle.yaml`
- Started UTC: 2026-09-22T07:28:07Z
- Finished UTC: 2026-09-22T07:28:07Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `habitatmech:BACDIVE.a4a67c4a7f` |
| Label | `bovine-associated environment` |
| Class | `HabitatRecord` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `REVIEWED` |
| Maintained owner | Generated from the BacDive isolation-source inventory, the `curation/decisions.tsv` item decision, and the authored `curation/term_requests.tsv` novel-term request |
| Locked slug | `data/habitats/PATHS.tsv:1230` maps `habitatmech:BACDIVE.a4a67c4a7f` to `bovinae_cow_cattle` |

This is the reviewed BacDive record for `Bovinae-Cow,-Cattle`. The record keeps the source concept as a novel host-associated habitat under `ENVO:01001002` instead of grounding it to the upstream `NCBITaxon:9903` close match, because the taxon names the determining host organism rather than the microbial habitat.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/bovinae_cow_cattle.yaml` | Pass; `linkml-validate` reported `No issues found` |
| `just validate-strict data/habitats/host_associated/bovinae_cow_cattle.yaml` | Pass; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate-causal-all` | Pass; 32 causal-graph curation files with 32 graphs validated |
| `just term-requests-check` | Pass; term-request table is current with 109 terms |
| `just validate-history` | Pass; 77 history records are valid against `src/habitatmech/schema/history.yaml` |
| `just verify-corpus --max-diffs 1` | Pass; expected 3206 records, found 3206, with 0 missing, 0 extra, 0 differing |
| `git diff --check` | Pass; no whitespace or patch errors after this report was staged |

## Identity and Grounding

The minted identity, authored term, and reviewed ungrounded status are supported by maintained curation and the BacDive inventory:

- `data/habitats/PATHS.tsv:1230` pins `habitatmech:BACDIVE.a4a67c4a7f` to slug `bovinae_cow_cattle`, matching the reviewed YAML path.
- `BACDIVE:bacdive.isolation_source:bovinae-cow,-cattle` hashes to the minted suffix `a4a67c4a7f`, matching the record identifier.
- `data/raw/bacdive_isolation_sources.tsv:25` records source id `bacdive.isolation_source:bovinae-cow,-cattle`, source label `Bovinae-Cow,-Cattle`, normalized label `bovinae-cow,-cattle`, 619 strain assertions, and a 336-taxon candidate pool.
- `data/raw/isolation_source_groundings.tsv:49` maps the upstream source label to `NCBITaxon:9903` `Bos` as a medium-confidence `skos:closeMatch`, and the generated source-attestation note correctly records that this non-habitat partial mapping is not carried onto the record.
- `curation/decisions.tsv:1590` is the item-level `CONFIRM_UNGROUNDED` row for `habitatmech:BACDIVE.a4a67c4a7f`; it assigns `HOST_ASSOCIATED` and explicitly keeps the host organism concept as a habitat while rejecting the host taxon as the identity.
- `curation/term_requests.tsv:18` authors the requested label `bovine-associated environment`, broader term `ENVO:01001002` `animal-associated environment`, definition `An animal-associated environment which is determined by a bovine.`, exact synonym `Bovinae-Cow,-Cattle`, and `ADD` action.
- `data/raw/ontology_terms.tsv:8497` defines `ENVO:01001002` as `animal-associated environment` with definition `An environmental system determined by an animal.`, synonyms `Metazoan-associated environment|animal environment`, `directly_referenced: TRUE`, and `label_only: FALSE`.
- `reports/habitat_research_manifest.tsv:17` points the target identifier to `research/habitats/other/bovinae-cow-cattle-habitatmech-bacdive-a4a67c4a7f-deep-research-claude_code.md`; that report supports the animal-associated genus, records that `NCBITaxon:27592` and `NCBITaxon:9913` are organism classes rather than places, and argues for a cattle or bovine associated environment term under the broader animal-associated environment.

`grounding_status: UNGROUNDED` is correct for a source concept that has no exact vendored environment term, and `mapping_status: REVIEWED` is correct because the item-level decision has already been curated. `HOST_ASSOCIATED` is likewise maintained: the decision row moved this domestic-mammal host out of the seeder default and onto the same host-associated branch as other records under `ENVO:01001002`.

## Evidence

Every generated scientific claim in this record is source-derived or maintained:

| Claim | Nearest source | Review |
|---|---|---|
| Minted identifier and locked filename | `data/habitats/PATHS.tsv:1230` plus the BacDive source-key hash | Supported exactly |
| `label`, `definition`, exact synonym, `parent_habitats: ENVO:01001002`, and `mapping_status: REVIEWED` | `curation/term_requests.tsv:18`, `curation/term_requests/envo_robot_template.tsv:15`, and `curation/decisions.tsv:1590` | Supported exactly |
| `habitat_category: HOST_ASSOCIATED` and `grounding_status: UNGROUNDED` | `curation/decisions.tsv:1590` | Supported exactly |
| BacDive `source_id`, `source_label`, 619-strain attestation, and 336-taxon candidate pool | `data/raw/bacdive_isolation_sources.tsv:25` | Supported exactly |
| Deliberate omission of the upstream taxon grounding | `data/raw/isolation_source_groundings.tsv:49` and `curation/decisions.tsv:1590` | Supported; `NCBITaxon:9903` is a host taxon close match, not a habitat identity |
| Top 25 `characteristic_taxa` rows, ranks, taxon labels, and association counts | `data/raw/bacdive_source_taxa.tsv:346-370` | Supported exactly |
| Authored term rationale | `research/habitats/other/bovinae-cow-cattle-habitatmech-bacdive-a4a67c4a7f-deep-research-claude_code.md` | Supported by the committed report linked from `reports/habitat_research_manifest.tsv:17` |

The record has no xrefs, environmental parameters, record-level evidence, causal graphs, discussion links, or datasets. Their absence is consistent with the curated decision to avoid emitting the non-habitat NCBITaxon close match and with exact ignored/hidden-inclusive searches that found no maintained causal overlay or dataset row for `habitatmech:BACDIVE.a4a67c4a7f`.

## Completeness

No consequential slot is underfilled for the maintained inputs that feed this record:

- The `source_attestations` entry captures the complete BacDive source id, label, assertion count, `STRAIN` unit, and the curation note explaining why the upstream taxon close match is not emitted.
- The authored definition, exact synonym, direct `ENVO:01001002` parent, and `REVIEWED` status all trace to `curation/term_requests.tsv:18`.
- The `HOST_ASSOCIATED` category and reviewed ungrounded status trace to the item-level curation decision rather than to the raw BacDive inventory alone.
- The top-25 characteristic taxa are complete for the generated cutoff and retain the raw rank order from `data/raw/bacdive_source_taxa.tsv:346-370`; the shared `candidate_pool: 336` value is supported by `data/raw/bacdive_isolation_sources.tsv:25`.

Ignored/hidden-inclusive exact searches covered `curation`, `history`, `research`, `reports`, `data/raw`, `data/habitats/PATHS.tsv`, and the generated target. They found the expected decision row, term-request row, ENVO robot-template row, research report, research manifest row, raw BacDive source row, raw upstream-grounding row, raw top-taxa rows, path lock, and generated YAML, and no prior exact YAML review report for `bovinae_cow_cattle`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the same focused validation set if future curation changes the BacDive decision, the authored term request, the upstream taxon-grounding note, or the characteristic-taxon rollup for this bovine host record:

- `just validate data/habitats/host_associated/bovinae_cow_cattle.yaml`
- `just validate-strict data/habitats/host_associated/bovinae_cow_cattle.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `git diff --check`

If future curation adds a bovine host xref, keep it out of `parent_habitats` and verify that the generated source-attestation note still prevents `NCBITaxon:9903` from being treated as a habitat identity.

## Additional Notes

- `find reports/yaml_record_review -name '*bovinae_cow_cattle*' -print` found no pre-existing exact review report for this record before this file was written.
- `find curation history research reports \( -name '*bovinae_cow_cattle*' -o -name '*a4a67c4a7f*' -o -name '*bovinae*' -o -name '*cattle*' \) -print` found the expected deep-research report and one unrelated `cattle_barn` YAML review, but no prior exact YAML review or target-specific causal overlay before this file was written.
- Exact ignored/hidden-inclusive content searches for `habitatmech:BACDIVE.a4a67c4a7f`, `bacdive.isolation_source:bovinae-cow,-cattle`, and `Bovinae-Cow,-Cattle` found the maintained target curation, research, raw, generated, and manifest rows cited above, plus non-target sibling host reports and term-request rationales that mention the BacDive label as background context.
