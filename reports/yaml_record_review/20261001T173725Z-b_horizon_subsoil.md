# YAML Record Review: B horizon/Subsoil

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/terrestrial/b_horizon_subsoil.yaml`
- Started UTC: `2026-10-01T17:37:25Z`
- Finished UTC: `2026-10-01T17:37:25Z`
- Verdict: needs curation

## Target

Reviewed the complete generated `HabitatRecord` for the GOLD temperate-forest
soil B-horizon path:

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.711a362a45` |
| Label | `B horizon/Subsoil` |
| Path | `data/habitats/terrestrial/b_horizon_subsoil.yaml` |
| Stable slug | `b_horizon_subsoil` |
| Class | `HabitatRecord` |
| Category | `TERRESTRIAL` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Source | `GOLD` |
| Source ID | `gold.ecosystem:6010` |
| Source path | `Environmental > Terrestrial > Soil > Temperate forest > B horizon/Subsoil` |

The record is generated from committed inputs. `data/habitats/PATHS.tsv:2125`
pins `habitatmech:GOLD.711a362a45` to `b_horizon_subsoil`, and future
item-level decisions belong in `curation/decisions.tsv`, not as hand edits to
the generated YAML or rendered page.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/terrestrial/b_horizon_subsoil.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/terrestrial/b_horizon_subsoil.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, and 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; 3206 expected records, 3206 found on disk, 0 missing, 0 extra, and 0 differing. |
| `just worklist --status all --out /tmp/habitatmech-record-review-worklist.tsv` | Passed; wrote 953 ungrounded rows. The target appears at line 410 as a zero-assertion class-swept GOLD record. |
| `just report --out /tmp/habitatmech-record-review-report.tsv` | Passed; the target appears at line 2125 as `UNGROUNDED`, `SEEDED`, GOLD-only, one source, zero assertions, one parent, zero environmental parameters, zero characteristic taxa, and zero causal graphs. |
| `just render-check` | Passed; rendered 3206 habitat pages, 231 redirect stubs, 8 categories, and 123 term requests to a temporary site and confirmed `pages/` is in step with the corpus. |

No target-specific causal overlay exists, so there was no narrower
`just validate-causal curation/causal_graphs/<slug>.yaml` command to run.

## Identity and Grounding

The generated source identity is exact. `data/raw/gold_ecosystem_paths.tsv:1694`
has one row for `Environmental > Terrestrial > Soil > Temperate forest >
B horizon/Subsoil`, with leaf label `B horizon/Subsoil`, depth 5, one GOLD
ecosystem node ID, zero organism assertions, zero study assertions, zero
biosample assertions, zero total assertions, and source ID
`gold.ecosystem:6010`.

The exact node also appears in separate GOLD side-table inventories:
`data/raw/gold_path_biosamples.tsv:615` records 11 biosamples for ecosystem path
6010, and `data/raw/gold_studies.tsv:4213` records study `Gs0159116` as a
two-path study covering this target and
`Environmental > Terrestrial > Soil > Agricultural land`. Those side tables
show that GOLD has exact Temperate B-horizon/Subsoil source usage, but they do
not decide which ontology term, if any, should identify the slash leaf.

The target currently has only a class-level `CONFIRM_UNGROUNDED` decision at
`curation/decisions.tsv:673`. That decision is reproducible but intentionally
incomplete: it says no term in the then-vendored slice matched this label by
any search route, but it also says whether the concept is a habitat was not
assessed.

The record's only generated parent is `ENVO:01001805` `temperate forest`.
That term is present in the vendored slice at
`data/raw/ontology_terms.tsv:9298` and its generated GOLD page comes from the
source-path parent `Environmental > Terrestrial > Soil > Temperate forest`.
Unlike the equivalent boreal-forest parent, however, that parent is still only
an automatic exact match: `data/habitats/terrestrial/temperate_forest.yaml`
has `mapping_status: SEEDED`, and exact ignored/hidden-inclusive searches for
`habitatmech:GOLD.fa541933af`, `gold.ecosystem:6004`,
`gold.ecosystem:7665`, and the parent source path found no item-level decision
or prior review row.

The vendored ENVO slice has a general `soil horizon` term and a `mineral
horizon` child, but it does not name a B horizon directly. Exact
ignored/hidden-inclusive searches found three parallel GOLD
`B horizon/Subsoil` forest-soil rows, all zero-assertion in
`data/raw/gold_ecosystem_paths.tsv` and all still backed only by class-level
`CONFIRM_UNGROUNDED` rows:

| GOLD path | Source concept | Decision |
|---|---:|---|
| `Environmental > Terrestrial > Soil > Boreal forest/Taiga > B horizon/Subsoil` | `habitatmech:GOLD.fd21f91e1f` | `curation/decisions.tsv:1387` |
| `Environmental > Terrestrial > Soil > Temperate forest > B horizon/Subsoil` | `habitatmech:GOLD.711a362a45` | `curation/decisions.tsv:673` |
| `Environmental > Terrestrial > Soil > Tropical forest > B horizon/Subsoil` | `habitatmech:GOLD.8f75400740` | `curation/decisions.tsv:834` |

## Evidence

The record has no authored definition, synonyms, xrefs, environmental
parameters, characteristic taxa, record-level evidence, causal graphs,
discussions, or datasets. There are no claim-level citations to audit.

| Claim | Nearest maintained support | Review |
|---|---|---|
| The source attestation preserves GOLD node `6010`, the source label, and the full source path. | `data/raw/gold_ecosystem_paths.tsv:1694` | Supported exactly. |
| No direct source assertion count is emitted in the generated record. | `data/raw/gold_ecosystem_paths.tsv:1694` has zero organism, study, biosample, and total assertions for this exact path. | Supported for the current ecosystem-path projection. The independent `gold_path_biosamples.tsv` and `gold_studies.tsv` side tables show exact raw GOLD activity for the same node but are not emitted into `source_attestations`. |
| No GOLD triad side table supplies exact-path evidence. | Ignored/hidden-inclusive exact searches for the target source path found `data/raw/gold_ecosystem_paths.tsv:1694`, `data/raw/gold_path_biosamples.tsv:615`, and `data/raw/gold_studies.tsv:4213`, but no `data/raw/gold_path_triads.tsv` row for the exact path. | Supported. |
| Parent `ENVO:01001805` preserves the GOLD Temperate forest source-path parent. | `data/raw/gold_ecosystem_paths.tsv:727` records `Environmental > Terrestrial > Soil > Temperate forest`; `data/raw/ontology_terms.tsv:9298` names `ENVO:01001805` as `temperate forest`; `data/habitats/terrestrial/temperate_forest.yaml` is the generated exact record for that parent. | Supported as a source-path parent. This does not decide the B-horizon leaf, and the parent still lacks item-level review. |
| The rendered page mirrors the YAML. | `pages/habitats/b-horizon-subsoil-habitatmech-gold-711a362a45.html` | Supported; it shows the same identifier, category, `UNGROUNDED` grounding, `SEEDED` mapping, GOLD source path, missing assertion count, broader `ENVO:01001805` habitat, and class-level curation event. |

Ignored/hidden-inclusive exact searches found no target-specific term request,
causal graph overlay, append-only history record, deep-research report, or
prior exact YAML review whose filename is `*-b_horizon_subsoil.md`.

## Completeness

The record is complete for its generated GOLD projection, but it is not
complete as item-level HabitatMech curation.

The empty optional slots are currently appropriate: no maintained source input
supplies a definition, physicochemical parameters, characteristic taxa,
claim-level evidence, a causal graph, discussions, or datasets for this exact
source path.

The substantive gap is the item-level interpretation of `B horizon/Subsoil`.
GOLD uses the same slash label for boreal, temperate, and tropical forest soil
leaves, but the generated records are currently three ungrounded minted
concepts distinguished only by forest parent. A curator still needs to decide
whether the leaf denotes the B horizon specifically, subsoil more generally,
or a composite source category that should be grounded to an existing ENVO
soil-horizon term, represented by a novel term, or merged across the
forest-biome variants.

## Findings

| Severity | Finding | Owner |
|---|---|---|
| Major | `habitatmech:GOLD.711a362a45` is still only class-reviewed. The live record is a GOLD Temperate forest `B horizon/Subsoil` leaf whose current state has not been read against the exact GOLD path, its 11 exact-path biosamples, study `Gs0159116`, the existing `ENVO:03600011` `mineral horizon` / `ENVO:03600030` `soil horizon` branch, or the parallel boreal and tropical forest `B horizon/Subsoil` rows. | Replace the class-depth `curation/decisions.tsv` row with an item-level decision; audit the tropical sibling `habitatmech:GOLD.8f75400740` with the same criterion; if the Temperate row remains minted, define the intended temperate-forest B-horizon/subsoil environment under a defensible soil-horizon parent and regenerate the target. |
| Minor | The only generated parent, `ENVO:01001805` `temperate forest`, is source-supported but also still automatic. The parent record is an exact label match for `Environmental > Terrestrial > Soil > Temperate forest`, yet no item-level `REVIEW` row exists for its GOLD source concept, so the target depends on a seeder-grounded broader context while its B-horizon leaf remains unresolved. | Add an item-level `REVIEW` decision for the Temperate forest source concept in `curation/decisions.tsv` and regenerate the parent and any child records that inherit it. |

## Recommended Edits

1. Replace the `curation/decisions.tsv` row for
   `habitatmech:GOLD.711a362a45` with an item-level decision that decides
   whether the temperate-forest `B horizon/Subsoil` GOLD path should stay
   minted, should merge with an existing soil-horizon record, or should become
   `NOT_APPLICABLE`.
2. Audit sibling record `habitatmech:GOLD.8f75400740` so the boreal,
   temperate, and tropical forest `B horizon/Subsoil` records get consistent
   grounding and merge behavior.
3. Add an item-level `REVIEW` decision for the GOLD
   `Environmental > Terrestrial > Soil > Temperate forest` source concept so
   the generated `ENVO:01001805` parent no longer depends only on lexical exact
   matching.
4. If the target stays minted, add a `curation/term_requests.tsv` row that
   defines the intended temperate-forest B-horizon/subsoil environment and
   records whether `ENVO:03600011` `mineral horizon`, `ENVO:03600030`
   `soil horizon`, or both should be retained as broader parents.

## Follow-up Checks

After item-level curation, run:

1. `just seed`
2. `just seed-canary habitatmech:GOLD.711a362a45`
3. `just render`
4. `just validate data/habitats/terrestrial/b_horizon_subsoil.yaml`
5. `just validate-strict data/habitats/terrestrial/b_horizon_subsoil.yaml`
6. `just validate-causal-all`
7. `just validate-history`
8. `just term-requests-check`
9. `just verify-corpus --max-diffs 1`
10. `just render-check`
11. `git diff --check`

## Additional Notes

- Exact ignored/hidden-inclusive searches covered maintained curation inputs,
  causal overlays, `history`, prior YAML review reports, `research`,
  `data/raw`, generated habitat YAML, exact generated habitat pages, `docs`,
  `conf`, `.claude`, `CLAUDE.md`, and `justfile`. They excluded `.git`,
  `.venv`, `pages/text-map`, and `data/text_map` to avoid irrelevant Git
  internals, installed dependencies, and very large generated JSON text-map
  lines.
- The pre-report `find reports/yaml_record_review -maxdepth 1 -type f -name
  '*b_horizon_subsoil.md' -print` check returned no previous exact report for
  this generated stem. `find` included ignored files under the searched
  directory.
- `find` checks under `curation/causal_graphs`, `history`, and `research`
  found no exact slug-named causal overlay, append-only history record, or raw
  research report. `find` included ignored files under the searched
  directories.
- iModulonDB structured source checks were not applicable because the target
  names a GOLD terrestrial soil inventory category, not a gene, locus tag,
  regulator, protein, pathway, stress-response term, or transcriptomics
  dataset.
