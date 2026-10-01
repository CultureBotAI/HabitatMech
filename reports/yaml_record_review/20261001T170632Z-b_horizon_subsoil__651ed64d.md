# YAML Record Review: B horizon/Subsoil

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/terrestrial/b_horizon_subsoil__651ed64d.yaml`
- Started UTC: `2026-10-01T17:06:32Z`
- Finished UTC: `2026-10-01T17:06:32Z`
- Verdict: needs curation

## Target

Reviewed the complete generated `HabitatRecord` for the GOLD boreal-forest
soil B-horizon path:

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.fd21f91e1f` |
| Label | `B horizon/Subsoil` |
| Path | `data/habitats/terrestrial/b_horizon_subsoil__651ed64d.yaml` |
| Stable slug | `b_horizon_subsoil__651ed64d` |
| Class | `HabitatRecord` |
| Category | `TERRESTRIAL` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Source | `GOLD` |
| Source ID | `gold.ecosystem:6031` |
| Source path | `Environmental > Terrestrial > Soil > Boreal forest/Taiga > B horizon/Subsoil` |

The record is generated from committed inputs. `data/habitats/PATHS.tsv:3174`
pins `habitatmech:GOLD.fd21f91e1f` to
`b_horizon_subsoil__651ed64d`, and future item-level decisions belong in
`curation/decisions.tsv`, not as hand edits to the generated YAML or rendered
page.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/terrestrial/b_horizon_subsoil__651ed64d.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/terrestrial/b_horizon_subsoil__651ed64d.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, and 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; 3206 expected records, 3206 found on disk, 0 missing, 0 extra, and 0 differing. |
| `just worklist --status all --out /tmp/habitatmech-record-review-worklist.tsv` | Passed; wrote 953 ungrounded rows. The target appears at line 409 as a zero-assertion class-swept GOLD record. |
| `just report --out /tmp/habitatmech-record-review-report.tsv` | Passed; the target appears at line 3174 as `UNGROUNDED`, `SEEDED`, GOLD-only, one source, zero assertions, one parent, zero environmental parameters, zero characteristic taxa, and zero causal graphs. |
| `just render-check` | Passed; rendered 3206 habitat pages, 231 redirect stubs, 8 categories, and 123 term requests to a temporary site and confirmed `pages/` is in step with the corpus. |

No target-specific causal overlay exists, so there was no narrower
`just validate-causal curation/causal_graphs/<slug>.yaml` command to run.

## Identity and Grounding

The generated source identity is exact. `data/raw/gold_ecosystem_paths.tsv:1632`
has one row for `Environmental > Terrestrial > Soil > Boreal forest/Taiga >
B horizon/Subsoil`, with leaf label `B horizon/Subsoil`, depth 5, one GOLD
ecosystem node ID, zero organism assertions, zero study assertions, zero
biosample assertions, zero total assertions, and source ID
`gold.ecosystem:6031`.

The target currently has only a class-level `CONFIRM_UNGROUNDED` decision at
`curation/decisions.tsv:1387`. That decision is reproducible but
intentionally incomplete: it says no term in the then-vendored slice matched
this label by any search route, but it also says whether the concept is a
habitat was not assessed.

The record's only generated parent is `ENVO:01000250` `subpolar coniferous
forest biome`. That parent is the item-reviewed grounding for the GOLD
`Environmental > Terrestrial > Soil > Boreal forest/Taiga` source-path parent,
recorded in `curation/decisions.tsv:954`; the unresolved part of this row is
therefore the slash leaf `B horizon/Subsoil`, not the boreal-forest context.

The vendored ENVO slice has a general `soil horizon` term and a `mineral
horizon` child, but it does not name a B horizon directly. GOLD carries two
other zero-assertion, class-swept `B horizon/Subsoil` rows under temperate and
tropical forest soil. Those three rows should be read together because a
decision to merge, ground narrowly, define a new B-horizon habitat, or reject
the slash label applies across the forest-biome variants.

## Evidence

The record has no authored definition, synonyms, xrefs, environmental
parameters, characteristic taxa, record-level evidence, causal graphs,
discussions, or datasets. There are no claim-level citations to audit.

| Claim | Nearest maintained support | Review |
|---|---|---|
| The source attestation preserves GOLD node `6031`, the source label, and the full source path. | `data/raw/gold_ecosystem_paths.tsv:1632` | Supported exactly. |
| No direct source assertion count is emitted. | `data/raw/gold_ecosystem_paths.tsv:1632` has zero organism, study, biosample, and total assertions for this exact path. | Supported. |
| No GOLD biosample, study, or triad side table supplies extra exact-path evidence. | An ignored/hidden-inclusive exact search for `Environmental > Terrestrial > Soil > Boreal forest/Taiga > B horizon/Subsoil\t` found only `data/raw/gold_ecosystem_paths.tsv:1632`. | Supported. |
| Parent `ENVO:01000250` preserves the reviewed GOLD boreal-forest source-path parent. | `data/raw/gold_ecosystem_paths.tsv:723` records `Environmental > Terrestrial > Soil > Boreal forest/Taiga`; `curation/decisions.tsv:954` grounds that source concept to `ENVO:01000250`; `data/raw/ontology_terms.tsv:7755` names `ENVO:01000250` as `subpolar coniferous forest biome` with `boreal forest` and `taiga` synonyms. | Supported. The parent does not decide the B-horizon leaf. |
| The rendered page mirrors the YAML. | `pages/habitats/b-horizon-subsoil-habitatmech-gold-fd21f91e1f.html` | Supported; it shows the same identifier, category, `UNGROUNDED` grounding, `SEEDED` mapping, GOLD source path, missing assertion count, broader `ENVO:01000250` habitat, and class-level curation event. |

Ignored/hidden-inclusive exact searches found no target-specific term request,
causal graph overlay, append-only history record, or prior exact YAML review
whose `Record` line names
`data/habitats/terrestrial/b_horizon_subsoil__651ed64d.yaml`.

## Completeness

The record is complete for its generated GOLD projection, but it is not
complete as item-level HabitatMech curation.

The empty optional slots are currently appropriate: no maintained source input
or exact GOLD side table supplies a definition, physicochemical parameters,
characteristic taxa, claim-level evidence, a causal graph, discussions, or
datasets for this exact zero-assertion source path.

The substantive gap is the item-level interpretation of `B horizon/Subsoil`.
GOLD uses the slash label for boreal, temperate, and tropical forest soil
leaves, but the generated records are currently three ungrounded minted
concepts distinguished only by forest-biome parent. A curator still needs to
decide whether the leaf denotes the B horizon specifically, subsoil more
generally, or a composite source category that should be grounded to an
existing ENVO soil-horizon term, represented by a novel term, or merged across
the forest-biome variants.

## Findings

| Severity | Finding | Owner |
|---|---|---|
| Major | `habitatmech:GOLD.fd21f91e1f` is still only class-reviewed. The live record is a zero-assertion GOLD boreal-forest `B horizon/Subsoil` leaf whose only item-reviewed parent is the broader `ENVO:01000250` biome, and the class sweep explicitly did not decide whether the slash leaf should be treated as a B horizon, as subsoil, or as a forest-specific soil horizon that needs a new definition. This leaves three parallel forest `B horizon/Subsoil` records unresolved as separate minted habitats. | Replace the class-depth `curation/decisions.tsv` row with an item-level decision; audit the temperate and tropical `B horizon/Subsoil` rows with the same criterion; if the boreal row remains minted, define the intended boreal B-horizon/subsoil environment under a defensible soil-horizon parent and regenerate the target. |

## Recommended Edits

1. Replace the `curation/decisions.tsv` row for
   `habitatmech:GOLD.fd21f91e1f` with an item-level decision that decides
   whether the boreal `B horizon/Subsoil` GOLD path should stay minted, should
   merge with an existing soil-horizon record, or should become
   `NOT_APPLICABLE`.
2. Audit sibling records `habitatmech:GOLD.711a362a45` and
   `habitatmech:GOLD.8f75400740` so the temperate, tropical, and boreal forest
   `B horizon/Subsoil` records get consistent grounding and merge behavior.
3. If the target stays minted, add a `curation/term_requests.tsv` row that
   defines the intended forest B-horizon/subsoil environment and records
   whether `ENVO:03600011` `mineral horizon`, `ENVO:03600030` `soil horizon`,
   or both should be retained as broader parents.

## Follow-up Checks

After item-level curation, run:

1. `just seed`
2. `just seed-canary habitatmech:GOLD.fd21f91e1f`
3. `just render`
4. `just validate data/habitats/terrestrial/b_horizon_subsoil__651ed64d.yaml`
5. `just validate-strict data/habitats/terrestrial/b_horizon_subsoil__651ed64d.yaml`
6. `just validate-causal-all`
7. `just validate-history`
8. `just term-requests-check`
9. `just verify-corpus --max-diffs 1`
10. `just render-check`
11. `git diff --check`

## Additional Notes

- Exact ignored/hidden-inclusive searches covered maintained curation inputs,
  causal overlays, `history`, prior YAML review reports, `data/raw`, generated
  habitat YAML, and exact generated habitat pages. They excluded `.git`,
  `pages/text-map`, and `data/text_map` to avoid irrelevant Git internals and
  very large generated JSON text-map lines.
- The search for the exact target source path under GOLD side tables found
  only `data/raw/gold_ecosystem_paths.tsv:1632` and no exact GOLD biosample,
  study, or triad side-table row.
- iModulonDB structured source checks were not applicable because the target
  names a GOLD terrestrial soil inventory category, not a gene, locus tag,
  regulator, protein, pathway, stress-response term, or transcriptomics
  dataset.
