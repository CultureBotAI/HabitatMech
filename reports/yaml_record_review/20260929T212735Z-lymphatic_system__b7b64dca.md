# YAML Record Review: Lymphatic system

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/lymphatic_system__b7b64dca.yaml`
- Started UTC: 2026-09-29T21:20:00Z
- Finished UTC: 2026-09-29T21:27:35Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Record | `data/habitats/host_associated/lymphatic_system__b7b64dca.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.f65007e88e` |
| Label | `Lymphatic system` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `NARROW` |
| Mapping status | `SEEDED` |
| Maintained/generated | generated from committed source inventories by `scripts/seed_from_sources.py` |
| Source attestation | `GOLD`, `gold.ecosystem:5133`, `Host-associated > Birds > Lymphatic system`, `skos:narrowMatch` |

The target is the generated, seeded, GOLD-only Birds/Lymphatic system source concept. It is distinct from other generated records with the same display label, including the Mammals Lymphatic system record `habitatmech:GOLD.be39fe9a0e`; `data/habitats/PATHS.tsv` pins the bird record `habitatmech:GOLD.f65007e88e` to `lymphatic_system__b7b64dca`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/lymphatic_system__b7b64dca.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/habitats/host_associated/lymphatic_system__b7b64dca.yaml` | Passed; 1 file scanned, 0 files with errors, 0 error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; 3206 records expected, 3206 found, 0 missing, 0 extra, 0 differing. |
| `just report --ungrounded-top 0 --out /private/var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/habitatmech-report-bird-lymphatic-system.tsv` | Passed; wrote the TSV snapshot and reported `habitatmech:GOLD.f65007e88e` as `NARROW`, `SEEDED`, 1 source, 0 assertions, no definition, 2 parents, 0 parameters, 0 taxa, and 0 causal graphs. |
| `just worklist --limit 40 --status all --out /private/var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/habitatmech-worklist-bird-lymphatic-system.tsv` | Passed; wrote 953 ungrounded backlog rows. The bird Lymphatic system record is narrow-grounded and therefore not a ranked ungrounded item. |
| `git diff --check` | Passed after writing this report. |

## Identity and Grounding

The source identity is internally consistent. `data/raw/gold_ecosystem_paths.tsv` contains the canonical GOLD row `Host-associated > Birds > Lymphatic system`, leaf label `Lymphatic system`, depth 3, three GOLD node IDs, and source IDs `gold.ecosystem:5133`, `gold.ecosystem:7472`, and `gold.ecosystem:7473`; the generated source attestation uses the first node ID and records that three GOLD ecosystem node IDs share this path.

The `NARROW` grounding is appropriate for an unreviewed source path whose closest ontology term is the generic vertebrate `UBERON:0002465` `lymphoid system`. The vendored UBERON row defines the lymphatic system in vertebrates and lists `lymphatic system` as an exact synonym, while the GOLD concept adds the bird host context. The bird source concept is therefore narrower than UBERON's anatomy class instead of exactly identical to it.

Both parents are justified:

| Parent | Support |
|---|---|
| `UBERON:0002465` | `data/raw/ontology_terms.tsv` defines `UBERON:0002465` `lymphoid system` and lists `lymphatic system` as an exact synonym. |
| `habitatmech:GOLD.47e603cf4f` | The GOLD source path sits directly under `Host-associated > Birds`, which is generated as `bird-associated environment`. |

## Evidence

The record has no curator-authored causal graphs, characteristic taxa, environmental parameters, authored definition, or record-level evidence, so there are no claim-level citations to audit.

The zero assertion total is supported by the raw GOLD path inventory. The `Host-associated > Birds > Lymphatic system` row reports `organism_count = 0`, `study_count = 0`, `biosample_count = 0`, and `total_assertions = 0`. Exact gitignore-independent searches for `gold.ecosystem:5133`, `gold.ecosystem:7472`, and `gold.ecosystem:7473` found no rows in `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`, or `data/raw/gold_studies.tsv`, matching the empty optional slots in the YAML.

The rendered page `pages/habitats/lymphatic-system-habitatmech-gold-f65007e88e.html` reflects the same identifier, category, `NARROW` grounding, `SEEDED` mapping status, GOLD source path, and two broader parents as the generated YAML.

## Completeness

The generated record is complete for the maintained inputs currently available:

- The minted identifier, GOLD label, source ID, and source path are present.
- The broad UBERON lymphoid-system parent is present.
- The source-path parent to `bird-associated environment` is present.
- `data/habitats/PATHS.tsv` pins `habitatmech:GOLD.f65007e88e` to the stable `lymphatic_system__b7b64dca` slug.
- Empty `definition`, `characteristic_taxa`, `environmental_parameters`, `evidence`, and `causal_graphs` slots are appropriate because no curated definition, GOLD side-table row, raw biosample/study/triad row, or causal-graph overlay currently feeds this generated record.
- iModulonDB was not applicable; this anatomical habitat record names no gene, locus, regulator, transcriptomic dataset, or strain-level expression claim.

Gitignore-independent searches found no preexisting review for `habitatmech:GOLD.f65007e88e` or its GOLD node IDs under `reports/yaml_record_review`, and no Lymphatic-system-specific maintained decision, research, history, or causal-graph artifact for the exact bird minted ID, node IDs, or GOLD source path under `curation`, `history`, or `research`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No corrective follow-up is needed. If this record changes later, the narrow checks are:

- `just validate data/habitats/host_associated/lymphatic_system__b7b64dca.yaml`
- `just validate-strict data/habitats/host_associated/lymphatic_system__b7b64dca.yaml`
- `just verify-corpus --max-diffs 1`
- `just report --ungrounded-top 0`

## Additional Notes

Absence and de-duplication searches were gitignore-independent:

- `rg --no-ignore --hidden` for `YAML Record Review: Lymphatic system`, `habitatmech:GOLD.f65007e88e`, `gold.ecosystem:5133`, `gold.ecosystem:7472`, `gold.ecosystem:7473`, and the exact GOLD source path under `reports/yaml_record_review` found no prior review report for this record.
- `rg --no-ignore --hidden` for `habitatmech:GOLD.f65007e88e`, the three GOLD node IDs, and the exact GOLD source path under `curation`, `history`, and `research` found no exact maintained decision, research report, history record, or causal-graph overlay.
- `rg --no-ignore --hidden` for the three GOLD node IDs under `data/raw` found only the `data/raw/gold_ecosystem_paths.tsv` source row; the raw GOLD side tables contain no direct rows for this zero-assertion source path.
- `rg --no-ignore --hidden` for `habitatmech:GOLD.f65007e88e` found the expected generated YAML, `data/habitats/PATHS.tsv` stable slug row, rendered page, and child-parent references from generated Spleen and Bursa of Fabricius records.
