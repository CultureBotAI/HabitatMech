# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/bowens_disease_squamous_cell_carcinoma_in_situ.yaml`
- Started UTC: 2026-09-22T07:44:39Z
- Finished UTC: 2026-09-22T07:44:39Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.acd58e051d` |
| Label | `Bowens disease/Squamous cell carcinoma in situ` |
| Class | `HabitatRecord` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `NOT_APPLICABLE` |
| Mapping status | `REVIEWED` |
| Maintained owner | Generated from the GOLD ecosystem-path inventory plus the item-level `curation/decisions.tsv` review; generated YAML remains read-only |
| Locked slug | `data/habitats/PATHS.tsv:2555` maps `habitatmech:GOLD.acd58e051d` to `bowens_disease_squamous_cell_carcinoma_in_situ` |

This is the reviewed GOLD record for `Host-associated > Mammals: Human > Malignant tumor > Carcinoma > Bowens disease/Squamous cell carcinoma in situ`. It intentionally remains `NOT_APPLICABLE`: the source label names a disease or diagnosis category, not a habitat identity.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/bowens_disease_squamous_cell_carcinoma_in_situ.yaml` | Pass; `linkml-validate` reported `No issues found` |
| `just validate-strict data/habitats/host_associated/bowens_disease_squamous_cell_carcinoma_in_situ.yaml` | Pass; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate-causal-all` | Pass; 32 causal-graph curation files with 32 graphs validated |
| `just term-requests-check` | Pass; term-request table is current with 109 terms |
| `just validate-history` | Pass; 77 history records are valid against `src/habitatmech/schema/history.yaml` |
| `just verify-corpus --max-diffs 1` | Pass; expected 3206 records, found 3206, with 0 missing, 0 extra, 0 differing |
| `git diff --check` | Pass; no whitespace or patch errors after this report was staged |

## Identity and Grounding

The minted identity, reviewed disposition, and GOLD parent are supported by the GOLD inventory, path lock, and maintained decision table:

- `data/habitats/PATHS.tsv:2555` pins `habitatmech:GOLD.acd58e051d` to slug `bowens_disease_squamous_cell_carcinoma_in_situ`, matching the reviewed YAML path.
- `GOLD:Host-associated > Mammals: Human > Malignant tumor > Carcinoma > Bowens disease/Squamous cell carcinoma in situ` hashes to `acd58e051d`, matching the record identifier.
- `data/raw/gold_ecosystem_paths.tsv:2326` is the exact raw GOLD path, gives leaf label `Bowens disease/Squamous cell carcinoma in situ`, records depth `5`, aggregates one GOLD ecosystem node, names `gold.ecosystem:6196`, and carries 0 organism, study, biosample, and total assertions.
- `curation/decisions.tsv:977` is the item-level `NOT_APPLICABLE` row for `habitatmech:GOLD.acd58e051d`; it records that `Bowens disease/Squamous cell carcinoma in situ` names a disease, intervention, sampling artifact, or no-value filler rather than a place.
- `data/raw/gold_ecosystem_paths.tsv:2323` is the immediate GOLD parent path `Host-associated > Mammals: Human > Malignant tumor > Carcinoma`, and `data/habitats/PATHS.tsv:2445` pins its generated identifier `habitatmech:GOLD.9bb307824f` to `carcinoma`.
- `curation/decisions.tsv:901` independently reviews the immediate GOLD `Carcinoma` parent as `NOT_APPLICABLE` for the same disease-category reason.

`grounding_status: NOT_APPLICABLE` and `mapping_status: REVIEWED` are expected because the item-level curation row has already pulled this disease leaf out of the class-level sweep and decided it individually. Keeping the generated `habitatmech:GOLD.9bb307824f` parent preserves the original GOLD hierarchy while both records remain reviewed as non-habitats.

## Evidence

Every generated scientific claim in this record is source-derived or maintained:

| Claim | Nearest source | Review |
|---|---|---|
| Minted identifier and locked filename | `data/habitats/PATHS.tsv:2555` plus the GOLD source-path hash | Supported exactly |
| GOLD `source_id: gold.ecosystem:6196`, `source_label`, and full source path | `data/raw/gold_ecosystem_paths.tsv:2326` | Supported exactly |
| Reviewed `NOT_APPLICABLE` disposition | `curation/decisions.tsv:977` | Supported exactly |
| Broader generated GOLD `Carcinoma` parent | `data/raw/gold_ecosystem_paths.tsv:2323`, `data/habitats/PATHS.tsv:2445`, `curation/decisions.tsv:901`, and `data/habitats/host_associated/carcinoma.yaml` | Supported exactly |

The record has no definition, synonyms, xrefs, environmental parameters, characteristic taxa, record-level evidence, causal graphs, discussion links, assertion count, assertion unit, or datasets. Those absences are consistent with the reviewed `NOT_APPLICABLE` decision and with the exact raw GOLD path row having zero organism assertions. Exact side-table lookups found `data/raw/gold_path_biosamples.tsv:928`, which records 2 biosamples for ecosystem path `6196`, and `data/raw/gold_studies.tsv:3157`, a multi-path study set that includes the exact target path; they found no exact target row in `data/raw/gold_path_triads.tsv`.

## Completeness

No consequential slot is underfilled for the maintained inputs that feed this record:

- The sole `source_attestations` entry captures the complete target GOLD path and exact upstream node id.
- No `assertion_count` is emitted because `data/raw/gold_ecosystem_paths.tsv:2326` records 0 organism assertions for the canonical GOLD path.
- `parent_habitats` correctly points to the immediate minted GOLD parent, `habitatmech:GOLD.9bb307824f`.
- `mapping_status` stays `REVIEWED` because `curation/decisions.tsv:977` is an item-level target decision.

Ignored/hidden-inclusive exact searches covered `curation`, `history`, `research`, `reports`, `data/raw`, `data/habitats/PATHS.tsv`, the generated target, and the generated GOLD parent. They found the expected target and parent decisions, GOLD rows, pinned slugs, exact raw biosample and study side-table context, and no maintained term request, history record, causal-graph overlay, target-specific research report, or prior exact YAML review report for `habitatmech:GOLD.acd58e051d`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the same focused validation set if a future curation change reopens this disease leaf or one of its carcinoma siblings:

- `just validate data/habitats/host_associated/bowens_disease_squamous_cell_carcinoma_in_situ.yaml`
- `just validate-strict data/habitats/host_associated/bowens_disease_squamous_cell_carcinoma_in_situ.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `git diff --check`

If future evidence interprets this GOLD leaf as a sampled anatomical site instead of a diagnosis bucket, replace the `NOT_APPLICABLE` decision first, regenerate with `just seed`, preview `just seed-canary habitatmech:GOLD.acd58e051d`, and rerun the corpus-level checks.

## Additional Notes

- `find reports/yaml_record_review -name '*bowens_disease_squamous_cell_carcinoma_in_situ*' -print` found no pre-existing exact review report for this record before this file was written.
- `find curation history research reports \( -name '*bowens_disease_squamous_cell_carcinoma_in_situ*' -o -name '*acd58e051d*' -o -name '*bowens*' -o -name '*squamous*' \) -print` found no maintained target-specific history, research, report, or causal overlay artifacts before this file was written.
- Exact ignored/hidden-inclusive content searches for `habitatmech:GOLD.acd58e051d`, `gold.ecosystem:6196`, and `Bowens disease/Squamous cell carcinoma in situ` found the maintained decision, raw rows, path lock, and generated YAML cited above.
