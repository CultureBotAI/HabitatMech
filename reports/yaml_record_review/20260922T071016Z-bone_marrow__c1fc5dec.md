# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/bone_marrow__c1fc5dec.yaml`
- Started UTC: 2026-09-22T07:10:16Z
- Finished UTC: 2026-09-22T07:10:16Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.ef3ff31a67` |
| Label | `Bone marrow` |
| Class | `HabitatRecord` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `NARROW` |
| Mapping status | `SEEDED` |
| Maintained owner | Generated from the GOLD ecosystem-path inventory plus the vendored ontology slice; future item-level review belongs in `curation/decisions.tsv`, future authored definitions belong in `curation/term_requests.tsv`, and future mechanism evidence belongs in `curation/causal_graphs/*.yaml` |
| Locked slug | `data/habitats/PATHS.tsv:3061` maps `habitatmech:GOLD.ef3ff31a67` to `bone_marrow__c1fc5dec` |

This is the minted GOLD record for `Host-associated > Mammals: Human > Skeletal system > Bone > Bone marrow`. The GOLD path scopes the `Bone marrow` leaf to the human skeletal-system bone branch and keeps it narrower than the generic UBERON `bone marrow` term.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/bone_marrow__c1fc5dec.yaml` | Pass; `linkml-validate` reported `No issues found` |
| `just validate-strict data/habitats/host_associated/bone_marrow__c1fc5dec.yaml` | Pass; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate-causal-all` | Pass; 32 causal-graph curation files with 32 graphs validated |
| `just term-requests-check` | Pass; term-request table is current with 109 terms |
| `just validate-history` | Pass; 77 history records are valid against `src/habitatmech/schema/history.yaml` |
| `just verify-corpus --max-diffs 1` | Pass; expected 3206 records, found 3206, with 0 missing, 0 extra, 0 differing |
| `git diff --check` | Pass; no whitespace or patch errors after this report was staged |

## Identity and Grounding

The minted identity and broader parents are supported by the GOLD inventory, the path lock, and the vendored ontology slice:

- `data/habitats/PATHS.tsv:3061` pins `habitatmech:GOLD.ef3ff31a67` to slug `bone_marrow__c1fc5dec`, matching the reviewed YAML path.
- `data/raw/gold_ecosystem_paths.tsv:1092` is the exact raw GOLD path `Host-associated > Mammals: Human > Skeletal system > Bone > Bone marrow`, gives leaf label `Bone marrow`, records depth `5`, aggregates one GOLD ecosystem node, records 1 organism assertion, and names `gold.ecosystem:5314` as the upstream node.
- `data/raw/ontology_terms.tsv:13150` defines `UBERON:0002371` with canonical label `bone marrow`, definition `The soft tissue that fills the cavities of bones.`, synonyms `medulla of bone|medulla ossea|medulla ossium|medullary bone`, `directly_referenced: FALSE`, and `label_only: FALSE`.
- `data/raw/gold_ecosystem_paths.tsv:361` is the immediate GOLD parent path `Host-associated > Mammals: Human > Skeletal system > Bone`, and `data/habitats/PATHS.tsv:2044` pins its generated identifier `habitatmech:GOLD.67f49f8b15` to `bone__234001be`.
- The target and parent source-concept hashes match the seeder's `sha1(f"{source}:{key}")[:10]` route: `GOLD:Host-associated > Mammals: Human > Skeletal system > Bone > Bone marrow` hashes to `ef3ff31a67`, and `GOLD:Host-associated > Mammals: Human > Skeletal system > Bone` hashes to `67f49f8b15`.

`grounding_status: NARROW` is consistent with the path context: the source concept is human skeletal-system bone marrow and should not be merged into the generic UBERON `bone marrow` identity. Keeping the GOLD path as a minted child while attaching `UBERON:0002371` as a broader term preserves both the source path and the anatomical parent. `mapping_status: SEEDED` is expected because exact ignored/hidden-inclusive searches found no item-level `curation/decisions.tsv` row for `habitatmech:GOLD.ef3ff31a67`.

## Evidence

Every generated scientific claim in this record is source-derived:

| Claim | Nearest source | Review |
|---|---|---|
| Minted identifier and locked filename | `data/habitats/PATHS.tsv:3061` | Supported exactly |
| GOLD `source_id: gold.ecosystem:5314`, `source_label: Bone marrow`, full source path, and 1-organism attestation | `data/raw/gold_ecosystem_paths.tsv:1092` | Supported exactly |
| Broader UBERON `bone marrow` parent | `data/raw/ontology_terms.tsv:13150` | Supported as a broader term for the human GOLD path, not as an exact identity |
| Broader GOLD human `Bone` parent | `data/raw/gold_ecosystem_paths.tsv:361`, `data/habitats/PATHS.tsv:2044`, and `data/habitats/host_associated/bone__234001be.yaml` | Supported exactly |

The record has no definition, synonyms, xrefs, environmental parameters, characteristic taxa, record-level evidence, causal graphs, discussion links, or datasets. Exact raw side-table lookups found no rows for the exact target path in `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`, or `data/raw/gold_studies.tsv`.

## Completeness

No consequential slot is underfilled for the maintained inputs that feed this record:

- The sole `source_attestations` entry captures the complete target GOLD path, exact upstream node id, organism assertion count, and `ORGANISM` unit.
- Both `parent_habitats` values are expected: `UBERON:0002371` records the matched broader ontology term, and `habitatmech:GOLD.67f49f8b15` records the next broader GOLD path.
- The record has no environmental parameter because the committed GOLD triad table has no exact row for `Host-associated > Mammals: Human > Skeletal system > Bone > Bone marrow`.
- `mapping_status` stays `SEEDED` because no item-level curation decision exists for `habitatmech:GOLD.ef3ff31a67`.

Ignored/hidden-inclusive exact searches covered `curation`, `history`, `research`, `reports`, `data/raw`, `data/habitats/PATHS.tsv`, the generated target, and the generated GOLD parent. They found the expected GOLD and UBERON rows, pinned slugs, the reviewed parent report for the immediate GOLD parent, and no maintained target decision row, term request, history record, causal-graph overlay, target-specific research report, raw biosample side-table row, raw study side-table row, raw triad row, or prior exact YAML review report for `habitatmech:GOLD.ef3ff31a67`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the same focused validation set if a future curation change adds an item-level decision, authored definition, or causal graph overlay for this human bone-marrow record:

- `just validate data/habitats/host_associated/bone_marrow__c1fc5dec.yaml`
- `just validate-strict data/habitats/host_associated/bone_marrow__c1fc5dec.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `git diff --check`

If future curation signs off the exact GOLD path, add the maintained item-level row to `curation/decisions.tsv`, run `just seed`, preview `just seed-canary habitatmech:GOLD.ef3ff31a67`, and rerun the corpus-level checks after regeneration.

## Additional Notes

- `find reports/yaml_record_review -name '*bone_marrow__c1fc5dec*' -print` found no pre-existing exact review report for this record before this file was written.
- `find curation history research reports \( -name '*bone_marrow__c1fc5dec*' -o -name '*ef3ff31a67*' -o -name '*5314*' \) -print` found no maintained target-specific decision, history, research, report, or causal overlay artifacts before this file was written.
- The exact target path has no matching rows in `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`, or `data/raw/gold_studies.tsv`.
