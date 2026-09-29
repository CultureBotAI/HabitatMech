# YAML Record Review: Oropharynx

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/oropharynx__eecf4d0a.yaml`
- Started UTC: 2026-09-29T13:40:32Z
- Finished UTC: 2026-09-29T13:40:49Z
- Verdict: pass with minor issues

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.d5eff0efa2` |
| Label | Oropharynx |
| Definition source | None |
| Habitat category | `HOST_ASSOCIATED` |
| Grounding status | `NARROW` |
| Mapping status | `SEEDED` |
| Maintained owner | Generated from `data/raw/gold_ecosystem_paths.tsv`; future item review belongs in `curation/decisions.tsv` |

The target is a generated GOLD record for
`Host-associated > Birds > Digestive system > Pharynx/Throat > Oropharynx`.
It is intentionally distinct from the PREGO `BTO:0005257` `oropharynx` record
and from the mammalian GOLD Oropharynx source records.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/oropharynx__eecf4d0a.yaml` | Passed with `No issues found`. |
| `just validate-strict data/habitats/host_associated/oropharynx__eecf4d0a.yaml` | Passed; 1 file scanned, 0 files with errors, 0 total error rows. |
| `just validate-causal-all` | Passed; validated 32 causal-graph curation files with 32 graphs. |
| `just validate-history` | Passed; `No issues found`, 77 history records valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; generated term-request table is current with 109 terms. |
| `just verify-corpus` | Passed; expected 3,206 records, found 3,206 on disk, with 0 missing, 0 extra, and 0 differing records. |
| `just report --ungrounded-top 0 --out /tmp/habitatmech-report-oropharynx.tsv` | Passed and wrote `/tmp/habitatmech-report-oropharynx.tsv`. |
| `just worklist --limit 40 --status all --out /tmp/habitatmech-worklist-oropharynx.tsv` | Passed and wrote `/tmp/habitatmech-worklist-oropharynx.tsv`. |

## Identity and Grounding

The record denotes the Birds GOLD `Oropharynx` child under
`Digestive system > Pharynx/Throat`, not the unqualified UBERON or BTO
oropharynx class:

| Check | Evidence | Result |
|---|---|---|
| Generated identifier | The first 10 SHA1 characters of `GOLD:Host-associated > Birds > Digestive system > Pharynx/Throat > Oropharynx` are `d5eff0efa2`, and `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.d5eff0efa2` to `oropharynx__eecf4d0a`. | Supported. |
| Source identity | `data/raw/gold_ecosystem_paths.tsv` has exactly this Birds source path with one node, `gold.ecosystem:7496`, and zero organism, study, biosample, or total assertions. | Supported. |
| Broader anatomical term | `data/raw/ontology_terms.tsv` vendors `UBERON:0001729` with label `oropharynx` and defines it as the portion of the pharynx between the soft palate and upper edge of the epiglottis. | Supported. |
| Source parent | The previous GOLD path level, `Pharynx/Throat`, was generated as `UBERON:0000341` `throat` and is a strictly broader parent for the Oropharynx leaf. | Supported. |
| Narrow grounding | The generated record uses `grounding_status: NARROW` and `skos:narrowMatch`, keeping the Birds source-path concept minted while linking it to general UBERON `oropharynx`. | Supported as a generated ambiguous-leaf fallback pending item-level review. |
| Mapping status | Hidden/ignored-inclusive searches found no `curation/decisions.tsv` row or history record for `habitatmech:GOLD.d5eff0efa2`; `mapping_status: SEEDED` is therefore correct. | Supported. |

The two other GOLD Oropharynx rows are different maintained source concepts:

| Generated source concept | Canonical path | Raw GOLD nodes | Total assertions |
|---|---|---:|---:|
| `habitatmech:GOLD.0fe2a08dac` | `Host-associated > Mammals: Human > Digestive system > Pharynx/Throat > Oropharynx` | `gold.ecosystem:6100` | 159 |
| `habitatmech:GOLD.ad6b97c4a4` | `Host-associated > Mammals > Respiratory system > Pharynx/Throat > Oropharynx` | `gold.ecosystem:6378` | 11 |

## Evidence

No publication or causal-mechanism evidence is required for this source-derived
zero-assertion GOLD leaf. The material evidence for this record is the GOLD path
inventory and the generated narrow match against a broader vendored UBERON term.

Supported evidence:

- The `source_attestations` entry preserves `source_id`,
  `source_label`, `source_path`, and `mapping_predicate` for
  `gold.ecosystem:7496`.
- The Birds GOLD row has `total_assertions: 0`, so the generated record
  correctly omits `assertion_count` and `assertion_unit`.
- An ignored-file-inclusive exact search of
  `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`,
  `data/raw/gold_studies.tsv`, and `data/raw/gold_ecosystem_paths.tsv` for
  `gold.ecosystem:7496` and the full Birds Oropharynx source path found only
  the `gold_ecosystem_paths.tsv` row. The absence of environmental parameters,
  characteristic taxa, biosample provenance, and study provenance on this
  generated record is therefore supported by the committed raw inventories.
- `data/raw/ontology_terms.tsv` also vendors `BTO:0005257` with label
  `oropharynx`; the PREGO record using that ID is separate and does not feed
  this GOLD source-path-scoped record.

Unsupported or over-scoped claims: None found.

## Completeness

The record is complete for a seeded NARROW GOLD record except for item-level
curation review:

- The minted identifier, GOLD source attestation, UBERON parent, source-path
  parent, and seeded curation-history event all trace to committed source rows
  or generated parent records.
- No `environmental_parameters`, `characteristic_taxa`, `causal_graphs`,
  `evidence`, or `discussions` fields are present; none are implied by the
  Birds source row feeding this record.
- An ignored-file-inclusive exact search across `curation/decisions.tsv`,
  `history`, `data/habitats/PATHS.tsv`,
  `reports/yaml_record_review`, `research/habitats`,
  `curation/causal_graphs`, `conf`, and the relevant `data/raw` GOLD side
  tables found the generated path row and source inventory row, but no
  maintained curation decision, history entry, causal overlay, research report,
  or prior YAML review for this record.
- Before this report was written, a `find` search, which included ignored files
  under `reports/yaml_record_review`, `research/habitats`, `history`, and
  `curation/causal_graphs`, found no Oropharynx-named artifact that would add a
  narrower evidence obligation for this Birds GOLD record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Minor | The Birds GOLD Oropharynx source concept has not received item-level grounding review. | Exact hidden/ignored-inclusive searches for `habitatmech:GOLD.d5eff0efa2`, `gold.ecosystem:7496`, the path-locked slug, and the full GOLD source path found no maintained decision or history record for this source concept, and the generated record remains `mapping_status: SEEDED`. The current `UBERON:0001729` parent itself is supported by the full GOLD path and the vendored ontology row. | `curation/decisions.tsv` |

## Recommended Edits

1. Add an item-level `REVIEW` or `GROUND_AS_PARENT` row in
   `curation/decisions.tsv` for `habitatmech:GOLD.d5eff0efa2` that preserves
   target `UBERON:0001729`, label `oropharynx`, `grounding_status: NARROW`, and
   `review_depth: ITEM`. The notes should state that the source is the Birds
   `Digestive system > Pharynx/Throat > Oropharynx` source-path concept and is
   therefore narrower than the unqualified UBERON anatomy term.

## Follow-up Checks

After adding the item-level decision:

1. Run `just seed`.
2. Run `just seed-canary habitatmech:GOLD.d5eff0efa2`.
3. Run `just seed-apply --force`.
4. Re-run `just validate data/habitats/host_associated/oropharynx__eecf4d0a.yaml`.
5. Re-run `just validate-strict data/habitats/host_associated/oropharynx__eecf4d0a.yaml`.
6. Re-run `just verify-corpus`.

## Additional Notes

- iModulonDB is not applicable: this record names a host anatomical microbial
  habitat, not a gene, regulator, protein, pathway, stress response, trait, or
  transcriptomics dataset.
- The Mammals and Mammals: Human Oropharynx GOLD siblings carry upstream GOLD
  assertions and are different HabitatMech records. Their studies, biosamples,
  and one Mammals MIxS triad row do not apply to this zero-assertion Birds
  Oropharynx source path.
