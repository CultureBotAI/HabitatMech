# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/host_associated/cephalochordata.yaml
- Started UTC: 2026-09-27T20:10:00Z
- Finished UTC: 2026-09-27T20:35:42Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/host_associated/cephalochordata.yaml` |
| Identifier | `habitatmech:GOLD.46c43fd62c` |
| Label | `Cephalochordata` |
| Category | `HOST_ASSOCIATED` |
| Grounding | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Maintained path lock | `data/habitats/PATHS.tsv:1822` maps `habitatmech:GOLD.46c43fd62c` to `cephalochordata` |
| Source path | `Host-associated > Cephalochordata` |
| Maintained status | Generated from the GOLD raw inventory and source-path hierarchy |

The complete generated YAML was read before judging the record. It is a compact
GOLD-only class-level-swept record with one source attestation, one broader
ENVO parent, and generated history for `CONFIRM_UNGROUNDED` plus
`SEEDED_FROM_SOURCES`.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/cephalochordata.yaml` | Pass; LinkML reported no issues. |
| `just validate-strict data/habitats/host_associated/cephalochordata.yaml` | Pass; 1 file scanned, 0 files with errors. |
| `just validate-causal-all` | Pass; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Pass; the generated term-request table is current with 109 terms. |
| `just validate-history` | Pass; 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus` | Pass; expected 3,206 records, found 3,206, with 0 missing, 0 extra, and 0 differing. |
| `just worklist --status all --out /tmp/habitatmech-cephalochordata-worklist.tsv` | Attempted; it was still running after more than 60 seconds with no output and was terminated with SIGTERM. |
| `just report --out /tmp/habitatmech-cephalochordata-report.tsv` | Attempted; it printed the corpus summary, including 3,206 records, 953 `UNGROUNDED`, 686 `REVIEWED`, zero risky unreviewed groundings, and zero class-level sweeps contradicted by the current slice, then stalled for more than 60 seconds and was terminated with SIGTERM. |

No record-specific reference validator exists beyond `just verify-corpus`,
`just validate-history`, and `just term-requests-check`; those corpus checks
cover generated-record drift, append-only history shape, and generated term
request synchronization for this target.

## Identity and Grounding

| Claim | Evidence | Review |
|---|---|---|
| `habitatmech:GOLD.46c43fd62c` is the minted identifier for `Host-associated > Cephalochordata`. | `data/raw/gold_ecosystem_paths.tsv:510` is the exact GOLD source-path row with four GOLD node IDs, 11 organism assertions, zero bulk studies, zero bulk biosamples, and node IDs `gold.ecosystem:4958\|gold.ecosystem:5171\|gold.ecosystem:5172\|gold.ecosystem:5173`. | Supported exactly. |
| The stable filename is `cephalochordata`. | `data/habitats/PATHS.tsv:1822` pins the target identifier to this slug. | Supported exactly. |
| The generated GOLD attestation has `source_id: gold.ecosystem:4958`, `assertion_count: 11`, `assertion_unit: ORGANISM`, and a duplicate-node note. | The generated values match `data/raw/gold_ecosystem_paths.tsv:510`, whose node list begins with `gold.ecosystem:4958` and contains four nodes. The separate GOLD API side table records two biosamples for exact ecosystem path `5173` in `data/raw/gold_path_biosamples.tsv:915`; those are not part of the organism assertion count and are correctly not summed into the record. | Supported exactly. |
| `ENVO:01001000` is a broader host-associated parent. | `data/raw/ontology_terms.tsv:8495` verifies `ENVO:01001000` as `environmental system determined by an organism`, synonym `host-associated environment`. The GOLD path is under `Host-associated` and then narrows the host determinant to the cephalochordate clade. | Supported as a strictly broader parent. |
| The current `UNGROUNDED` status is only class-level reviewed. | `curation/decisions.tsv:474` has `CONFIRM_UNGROUNDED` at `review_depth: CLASS` and explicitly says whether the concept is a habitat was not assessed, so this is not yet a term-request candidate. The generated `curation_history` preserves that limitation. | Reproducible, but incomplete for this individual GOLD path. |

The record denotes a cephalochordate-associated host environment, not the
taxon `Cephalochordata` alone. That host context makes the GOLD concept a real
habitat candidate, but the current label still comes directly from the source
taxonomic slot and there is no item-level curator row defining the habitat
identity as distinct from the host organism.

## Evidence

The source attestation is supported by the GOLD inventory row:

| Source row | Relevant value |
|---|---|
| `data/raw/gold_ecosystem_paths.tsv:510` | Exact path `Host-associated > Cephalochordata`; four GOLD node IDs; 11 organism assertions; zero bulk studies; zero bulk biosamples; 11 total assertions. |
| `data/raw/gold_path_biosamples.tsv:915` | The GOLD API side table records 2 biosamples for exact ecosystem path `5173`. |
| `data/raw/gold_studies.tsv:3045` | Study `Gs0150218` lists the exact target path along with amphibian, fish, and reptile digestive and respiratory-system paths. |

The immediate GOLD children are also reproducible from the inventory:

| Source row | Relevant value |
|---|---|
| `data/raw/gold_ecosystem_paths.tsv:1909` | `Host-associated > Cephalochordata > Digestive system`; one GOLD node ID and zero source assertions. |
| `data/raw/gold_ecosystem_paths.tsv:1912` | `Host-associated > Cephalochordata > Lancelets`; three GOLD node IDs and zero source assertions. |

Exact hidden/ignored-inclusive searches over `data/raw/gold_path_triads.tsv`
and `data/raw/environment_parameters.tsv` found no MIxS triad or environmental
parameter row for the exact `Host-associated > Cephalochordata` path. The
grandchild `Host-associated > Cephalochordata > Digestive system > Intestine >
Fecal` path has four API biosamples and appears in study `Gs0134283`, but those
rows attach to the fecal descendant rather than to this parent record.

## Completeness

- The record has no definition, xrefs, environmental parameters,
  characteristic taxa, evidence objects, causal graphs, discussions, datasets,
  item-level curation history, or item-level maintained decision row of its
  own.
- Exact hidden/ignored-inclusive searches for `habitatmech:GOLD.46c43fd62c`,
  `GOLD.46c43fd62c`, `gold.ecosystem:4958`, `gold.ecosystem:5173`,
  `cephalochordata`, `Cephalochordata`, and `Host-associated >
  Cephalochordata` across `curation`, `conf`, `history`, `research`,
  `reports/yaml_record_review`, selected `data/raw` GOLD tables, and
  `data/habitats/PATHS.tsv` found no target-specific term request, excluded
  term request, causal overlay, history record, label-correspondence residual,
  deep-research report, or prior exact YAML review.
- An ignored-inclusive search of `data/raw/ontology_terms.tsv` for
  cephalochordate, lancelet, `Branchiostoma`, and amphioxus strings found only
  the anatomical near misses `BTO:0001768` `notochord` and `BTO:0003173`
  `endostyle`; neither is an exact habitat identity for this GOLD
  host-associated path.

The absence of optional causal graphs, characteristic taxa, and environmental
parameters is not itself a defect for a sparse GOLD host-clade parent. The
material gap is that the class-level negative grounding decision has not been
promoted into an item-level habitat review or term request.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| HM-CEPHALOCHORDATA-001 | Major | `habitatmech:GOLD.46c43fd62c` is still a `SEEDED`, class-level `UNGROUNDED` host-taxon record even though the GOLD path denotes a cephalochordate-associated host environment. The existing `ENVO:01001000` parent is strictly broader and no vendored ontology term was found by an ignored-inclusive local search, but no curator has item-reviewed the individual source path, decided that the taxonomic label should remain a minted habitat rather than `NOT_APPLICABLE`, or requested an exact cephalochordate-associated environment term. | `curation/decisions.tsv`, then `curation/term_requests.tsv` and `history/` if the concept remains minted. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Item-review `habitatmech:GOLD.46c43fd62c` in `curation/decisions.tsv`
   against the exact `Host-associated > Cephalochordata` source path,
   `ENVO:01001000` `environmental system determined by an organism`, the GOLD
   child paths, and any exact cephalochordate host-associated term available in
   the current ontology slice.
2. If the review confirms the current minted identity, keep
   `ENVO:01001000` as a broader parent and add an authored
   `curation/term_requests.tsv` row for a cephalochordate-associated
   environment.
3. Scaffold a new append-only `history/` entry for the decision and any term
   request change.
4. Regenerate from the maintained inputs with `just seed` and a canary for
   `habitatmech:GOLD.46c43fd62c`; never patch
   `data/habitats/host_associated/cephalochordata.yaml` by hand.

## Follow-up Checks

| Check | Purpose |
|---|---|
| `just seed` | Preview the regenerated corpus after maintained curation edits. |
| `just seed-canary habitatmech:GOLD.46c43fd62c` | Rebuild and validate only the Cephalochordata record before a wider apply. |
| `just validate data/habitats/host_associated/cephalochordata.yaml` | Revalidate the corrected generated record. |
| `just validate-strict data/habitats/host_associated/cephalochordata.yaml` | Confirm the corrected generated record remains closed-schema valid. |
| `just verify-corpus` | Prove the committed generated YAML still reproduces from `data/raw/` and curation inputs. |
| `just term-requests-check` | Prove any generated ENVO term-request table is current. |
| `just validate-history` | Validate the new append-only curation history. |
| `just render` and `just qc` | Refresh and verify generated pages, redirects, tests, schema checks, and corpus reports after the curation change. |

## Additional Notes

- `Host-associated > Cephalochordata > Lancelets` is source-hierarchical child
  context. It is not evidence that the bare `Cephalochordata` label names a
  microbial habitat by itself.
- The exact GOLD study row, `Gs0150218`, groups this target with amphibian,
  fish, and reptile digestive and respiratory-system paths. That side table
  helps trace source provenance but is not a definition and does not prove an
  exact ontology identity.
