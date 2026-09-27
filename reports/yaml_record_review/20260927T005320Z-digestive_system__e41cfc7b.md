# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/host_associated/digestive_system__e41cfc7b.yaml
- Started UTC: 2026-09-27T00:49:20Z
- Finished UTC: 2026-09-27T00:53:20Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/host_associated/digestive_system__e41cfc7b.yaml` |
| Identifier | `habitatmech:GOLD.bcbf6eec9b` |
| Label | `Digestive system` |
| Category | `HOST_ASSOCIATED` |
| Grounding | `NARROW` |
| Mapping status | `SEEDED` |
| Maintained path lock | `data/habitats/PATHS.tsv:2673` maps `habitatmech:GOLD.bcbf6eec9b` to `digestive_system__e41cfc7b` |
| Source path | `Host-associated > Amphibia > Digestive system` |
| Maintained status | Generated from the GOLD raw inventory and source-path hierarchy |

The complete generated YAML was read before judging the record. It is a compact
GOLD-only record with one source attestation, two generated parents, and only
the generated `SEEDED_FROM_SOURCES` history event.

## Validation

| Command | Result |
|---|---|
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist.tsv` | Pass; wrote 953 ungrounded rows with 1,810 decisions on file. |
| `just report` | Pass; reported 3,206 records, 953 `UNGROUNDED`, 686 `REVIEWED`, zero risky unreviewed groundings, and zero class-level sweeps contradicted by the current slice. |
| `just validate data/habitats/host_associated/digestive_system__e41cfc7b.yaml` | Pass; LinkML reported no issues. |
| `just validate-strict data/habitats/host_associated/digestive_system__e41cfc7b.yaml` | Pass; 1 file scanned, 0 files with errors. |
| `just validate-causal-all` | Pass; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Pass; 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus` | Pass; expected 3,206 records, found 3,206, with 0 missing, 0 extra, and 0 differing. |
| `just term-requests-check` | Pass; the generated term-request table is current with 109 terms. |

No record-specific reference validator exists beyond `just verify-corpus`,
`just validate-history`, and `just term-requests-check`; those corpus checks
cover generated-record drift, append-only history shape, and generated term
request synchronization for this target.

## Identity and Grounding

| Claim | Evidence | Review |
|---|---|---|
| `habitatmech:GOLD.bcbf6eec9b` is the minted identifier for `Host-associated > Amphibia > Digestive system`. | `data/raw/gold_ecosystem_paths.tsv:1008` is the exact GOLD source-path row with three GOLD node IDs, one GOLD organism assertion, zero bulk studies, zero bulk biosamples, and node IDs `gold.ecosystem:3559|gold.ecosystem:3638|gold.ecosystem:4083`. | Supported exactly. |
| The stable filename is `digestive_system__e41cfc7b`. | `data/habitats/PATHS.tsv:2673` pins the target identifier to this slug. | Supported exactly. |
| The generated GOLD attestation has `source_id: gold.ecosystem:3559`, `mapping_predicate: skos:narrowMatch`, `assertion_count: 1`, `assertion_unit: ORGANISM`, and a duplicate-node note. | The generated values match `data/raw/gold_ecosystem_paths.tsv:1008`, whose node list begins with `gold.ecosystem:3559` and contains three nodes. | Supported exactly. |
| `UBERON:0001007` is a broader anatomical parent. | `data/raw/ontology_terms.tsv:12989` verifies `UBERON:0001007` as `digestive system`. The GOLD path constrains the target to Amphibia, while the same bare `Digestive system` leaf is reused under Annelida, arthropods, Birds, Cephalochordata, Fish, Mammals, Mollusca, Nematoda, and Reptilia. | Plausible and reproducible as `NARROW`; still unreviewed for this exact amphibian source path. |
| `habitatmech:GOLD.0cd585a031` is the immediate source-path parent. | `data/habitats/host_associated/amphibia.yaml` is the item-reviewed parent record; `curation/decisions.tsv:1606` keeps the `Amphibia` taxon as an `xref`, and `curation/term_requests.tsv:23` defines `amphibian-associated environment` under `ENVO:01001002`. | Supported exactly. |

The record denotes an amphibian digestive-system habitat, not the generic
anatomical structure alone. The generated `NARROW` grounding prevents the
record from merging with other host-clade `Digestive system` records through
`UBERON:0001007`, but no maintained item-level decision currently records that
the clade-specific minted identity is correct for this path.

## Evidence

The source attestation is supported by the GOLD inventory row:

| Source row | Relevant value |
|---|---|
| `data/raw/gold_ecosystem_paths.tsv:1008` | Exact path `Host-associated > Amphibia > Digestive system`; three GOLD node IDs; one organism assertion; zero bulk studies; zero bulk biosamples; one total assertion. |
| `data/raw/gold_path_biosamples.tsv:656` | The GOLD API side table records 9 biosamples for exact ecosystem path `4083`. |
| `data/raw/gold_studies.tsv:3045` | Study `Gs0150218` lists the exact target path along with 11 amphibian, cephalochordate, fish, and reptile host-system paths. |

Exact hidden/ignored-inclusive searches over `data/raw/gold_path_triads.tsv`
and `data/raw/environment_parameters.tsv` found no MIxS triad or environmental
parameter row for the exact `Host-associated > Amphibia > Digestive system`
path. The Amphibia child paths `Digestive system > Biliary tract > Liver` and
`Digestive system > Intestine > Fecal` do have contextual side-table rows, but
those do not attach to this parent digestive-system record.

## Completeness

- The record has no definition, xrefs, environmental parameters,
  characteristic taxa, evidence objects, causal graphs, discussions, datasets,
  item-level curation history, or item-level maintained decision row of its
  own.
- Exact hidden/ignored-inclusive searches for `habitatmech:GOLD.bcbf6eec9b`,
  `GOLD.bcbf6eec9b`, `gold.ecosystem:3559`, `gold.ecosystem:3638`,
  `gold.ecosystem:4083`, `digestive_system__e41cfc7b`, and `Host-associated >
  Amphibia > Digestive system` across `history`, `curation/causal_graphs`,
  `curation/samples`, `reports/yaml_record_review`,
  `reports/habitat_research_manifest.tsv`, `curation/term_requests.tsv`,
  `curation/term_requests/`, `research/habitats`, and `conf` found no
  target-specific history record, causal overlay, advisory sample row, prior
  exact YAML review, research-manifest row, term request, deep-research report,
  label-correspondence residual, or decision-row entry.
- Before this report was written, an ignored-independent `find` search found no
  prior `*digestive*` review report under `reports/yaml_record_review`. The
  review-time `find` search over `curation/causal_graphs` found no `*digestive*`
  causal overlay.

The absence of optional causal graphs, characteristic taxa, and environmental
parameters is not itself a defect for a sparse GOLD parent node. The material
gap is that the generated `NARROW` identity has never been item-reviewed or
defined.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| HM-AMPH-DIGESTIVE-001 | Major | `habitatmech:GOLD.bcbf6eec9b` still exposes a clade-specific `Digestive system` source path as a seeded record without an item-level grounding decision or definition. The generic `UBERON:0001007` parent is broader and the item-reviewed `amphibian-associated environment` parent is supported, but no curator row records why this exact GOLD path should remain minted, whether `UBERON:0001007` is only a parent, or whether the label should be defined as an amphibian digestive-system habitat rather than the reusable bare GOLD leaf. | `curation/decisions.tsv`, then `curation/term_requests.tsv` and `history/` if the concept remains minted. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Item-review `habitatmech:GOLD.bcbf6eec9b` in `curation/decisions.tsv`
   against the exact `Host-associated > Amphibia > Digestive system` source
   path, `UBERON:0001007` `digestive system`, the item-reviewed
   `amphibian-associated environment` parent, and the sibling host-clade
   `Digestive system` records.
2. If the item review confirms the current minted `NARROW` identity, use
   `GROUND_AS_PARENT` to retain `UBERON:0001007` as a broader parent rather
   than merging this path into generic digestive system.
3. If no exact ontology term exists, add an authored row to
   `curation/term_requests.tsv` for an amphibian digestive-system habitat; use
   `ADD` unless curation proves that one of the generated parents is not
   strictly broader.
4. Scaffold a new append-only `history/` entry for the decision and any term
   request change.
5. Regenerate from the maintained inputs with `just seed` and a canary for
   `habitatmech:GOLD.bcbf6eec9b`; never patch
   `data/habitats/host_associated/digestive_system__e41cfc7b.yaml` by hand.

## Follow-up Checks

| Check | Purpose |
|---|---|
| `just seed` | Preview the regenerated corpus after maintained curation edits. |
| `just seed-canary habitatmech:GOLD.bcbf6eec9b` | Rebuild and validate only the Amphibia digestive-system record before a wider apply. |
| `just validate data/habitats/host_associated/digestive_system__e41cfc7b.yaml` | Revalidate the corrected generated record. |
| `just validate-strict data/habitats/host_associated/digestive_system__e41cfc7b.yaml` | Confirm the corrected generated record remains closed-schema valid. |
| `just verify-corpus` | Prove the committed generated YAML still reproduces from `data/raw/` and curation inputs. |
| `just term-requests-check` | Prove any generated ENVO term-request table is current. |
| `just validate-history` | Validate the new append-only curation history. |
| `just render` and `just qc` | Refresh and verify generated pages, redirects, tests, schema checks, and corpus reports after the curation change. |

## Additional Notes

- `reports/habitat_research_manifest.tsv:265` records a successful parent-level
  Amphibia deep-research report for `habitatmech:GOLD.0cd585a031`; that report
  supports treating amphibians as microbial hosts but does not inspect the
  `Host-associated > Amphibia > Digestive system` child.
- The exact GOLD study row, `Gs0150218`, groups this target with amphibian
  liver and respiratory-system paths plus cephalochordate, fish, and reptile
  host-system paths. That side table is useful context for future curation, but
  it is not a definition and does not prove an exact ontology identity.
