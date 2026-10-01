# YAML Record Review: Beaker's/Popliteal cyst

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/host_associated/beaker_s_popliteal_cyst.yaml`
- Started UTC: `2026-10-01T18:40:51Z`
- Finished UTC: `2026-10-01T18:40:51Z`
- Verdict: needs curation

## Target

Reviewed the complete generated `HabitatRecord` for the GOLD human
joint-capsule cyst path:

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.1a8c452712` |
| Label | `Beaker's/Popliteal cyst` |
| Path | `data/habitats/host_associated/beaker_s_popliteal_cyst.yaml` |
| Stable slug | `beaker_s_popliteal_cyst` |
| Class | `HabitatRecord` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Parent habitat | `habitatmech:GOLD.e7296678c2` |
| Source | `GOLD` |
| Source ID | `gold.ecosystem:7003` |
| Source path | `Host-associated > Mammals: Human > Skeletal system > Joint capsule > Beaker's/Popliteal cyst` |

The record is generated from committed inputs. `data/habitats/PATHS.tsv:1476`
pins `habitatmech:GOLD.1a8c452712` to `beaker_s_popliteal_cyst`,
and future item-level decisions belong in `curation/decisions.tsv`, not as hand
edits to the generated YAML or rendered page.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/beaker_s_popliteal_cyst.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/host_associated/beaker_s_popliteal_cyst.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, and 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; 3206 expected records, 3206 found on disk, 0 missing, 0 extra, and 0 differing. |
| `just worklist --status all --out /tmp/habitatmech-record-review-worklist.tsv` | Passed; wrote 953 ungrounded rows. The target appears at line 414 as a zero-assertion class-swept GOLD record. |
| `just report --out /tmp/habitatmech-record-review-report.tsv` | Passed; the target appears at line 1476 as `UNGROUNDED`, `SEEDED`, GOLD-only, one source, zero assertions, one parent, zero environmental parameters, zero characteristic taxa, and zero causal graphs. |
| `just render-check` | Passed; rendered 3206 habitat pages, 231 redirect stubs, 8 categories, and 123 term requests to a temporary site and confirmed `pages/` is in step with the corpus. |

No target-specific causal overlay exists, so there was no narrower
`just validate-causal curation/causal_graphs/beaker_s_popliteal_cyst.yaml`
command to run.

## Identity and Grounding

The generated source identity is exact. `data/raw/gold_ecosystem_paths.tsv:2453`
has one row for `Host-associated > Mammals: Human > Skeletal system > Joint
capsule > Beaker's/Popliteal cyst`, with leaf label
`Beaker's/Popliteal cyst`, depth 5, one GOLD ecosystem node ID, zero organism
assertions, zero study assertions, zero biosample assertions, zero total
assertions, and source ID `gold.ecosystem:7003`.

The target currently has only a class-level `CONFIRM_UNGROUNDED` decision at
`curation/decisions.tsv:244`. That row only records a lexical negative result:
no term in the then-vendored slice matched the label by any class-sweep search
route, and whether the concept is a habitat was explicitly not assessed.
`curation/samples/class_swept_unscreened-20260814.tsv:8` later sampled the row
as a real habitat, but it is still a sampled class-screen verdict, not an
item-level review of the exact source path against candidate ontology terms or
possible parent relationships.

The record's only generated parent is `habitatmech:GOLD.e7296678c2` `Joint
capsule`. That parent is generated from
`data/raw/gold_ecosystem_paths.tsv:2452`, the exact GOLD source-path prefix
`Host-associated > Mammals: Human > Skeletal system > Joint capsule`, and it is
itself still only automatic:
`data/habitats/host_associated/joint_capsule__3bc01568.yaml` has
`mapping_status: SEEDED` and a seeded `skos:narrowMatch` parent link to
`UBERON:0001484` `articular capsule`.
`data/raw/ontology_terms.tsv:13047` confirms `UBERON:0001484` is the vendored
term whose synonyms include `joint capsule`.

Focused ignored/hidden-inclusive searches of the vendored slice and maintained
curation inputs found no exact `Baker's cyst`, `Beaker's cyst`, or `popliteal
cyst` ontology term or term request. The relevant maintained hits were limited
to the GOLD target row, the generated target record, and the sampled
class-sweep row; apparent ontology string hits were unrelated `bakery` terms,
PREGO beaker-cell synonyms for `goblet cell`, and a BTO definition mentioning
the popliteal space.

## Evidence

The record has no authored definition, synonyms, xrefs, environmental
parameters, characteristic taxa, record-level evidence, causal graphs,
discussions, or datasets. There are no claim-level citations to audit.

| Claim | Nearest maintained support | Review |
|---|---|---|
| The source attestation preserves GOLD node `7003`, the source label, and the full source path. | `data/raw/gold_ecosystem_paths.tsv:2453` | Supported exactly. |
| No direct source assertion count is emitted in the generated record. | `data/raw/gold_ecosystem_paths.tsv:2453` has zero organism, study, biosample, and total assertions for this exact path. | Supported. |
| No GOLD biosample, study, or MIxS triad side table supplies extra exact-path evidence. | An ignored/hidden-inclusive exact search for `Host-associated > Mammals: Human > Skeletal system > Joint capsule > Beaker's/Popliteal cyst\t` under `data/raw/` found only `data/raw/gold_ecosystem_paths.tsv:2453`. | Supported. |
| Parent `habitatmech:GOLD.e7296678c2` preserves the GOLD human Joint capsule source-path parent. | `data/raw/gold_ecosystem_paths.tsv:2452` records `Host-associated > Mammals: Human > Skeletal system > Joint capsule`; `data/raw/ontology_terms.tsv:13047` names `UBERON:0001484` as `articular capsule` with `joint capsule` as a synonym; `data/habitats/host_associated/joint_capsule__3bc01568.yaml` is the generated NARROW record for that parent path. | Supported as a source-path parent. This does not decide the Beaker's/Popliteal cyst leaf, and the parent still lacks item-level review. |
| The rendered page mirrors the YAML. | `pages/habitats/beaker-s-popliteal-cyst-habitatmech-gold-1a8c452712.html` | Supported; it shows the same identifier, category, `UNGROUNDED` grounding, `SEEDED` mapping, GOLD source path, missing assertion count, broader `habitatmech:GOLD.e7296678c2` habitat, and class-level curation event. |

Ignored/hidden-inclusive exact searches found no target-specific term request,
causal graph overlay, append-only history record, deep-research report, or
prior exact YAML review whose `Record` line names
`data/habitats/host_associated/beaker_s_popliteal_cyst.yaml`.

## Completeness

The record is complete for its generated GOLD projection, but it is not
complete as item-level HabitatMech curation.

The empty optional slots are currently appropriate: no maintained source input
or exact GOLD side table supplies a definition, physicochemical parameters,
characteristic taxa, claim-level evidence, a causal graph, discussions, or
datasets for this exact source path.

The unresolved curation question is the exact identity of the GOLD slash label.
The maintained GOLD source uses `Beaker's/Popliteal cyst`, the vendored slice
does not contain a cyst-specific ontology identity, and the source path places
the leaf under human `Joint capsule`. A curator still needs to decide whether
the leaf denotes a joint-capsule cyst habitat that should remain minted with a
spelling-preserving GOLD synonym, whether it should become a more general
popliteal-cyst environment under a reviewed joint parent, or whether the parent
relationship should be treated as related anatomical context rather than a
strictly broader habitat.

## Findings

| Severity | Finding | Owner |
|---|---|---|
| Major | `habitatmech:GOLD.1a8c452712` is still only class-reviewed. The live record is a zero-assertion GOLD `Beaker's/Popliteal cyst` leaf under the human Joint capsule path, and its current state has not been read at item level against the exact GOLD path, the likely spelling issue in the source label, the sampled class-screen verdict, or the existing `UBERON:0001484` joint-capsule context. | Replace the class-depth `curation/decisions.tsv` row with an item-level decision; decide whether the source concept stays minted, becomes `NOT_APPLICABLE`, or gains a reviewed relation to an existing anatomy term; if it stays minted, define the intended popliteal-cyst environment in `curation/term_requests.tsv` and retain the GOLD spelling only as source provenance. |
| Minor | The only generated parent, `habitatmech:GOLD.e7296678c2` `Joint capsule`, is source-supported but still automatic. The parent is a human GOLD path with a seeded broader link to `UBERON:0001484` `articular capsule`; no item-level `REVIEW` row exists for the parent source concept, so the target depends on an unreviewed broader context while the cyst leaf remains unresolved. | Add an item-level `REVIEW` or grounding decision for the human Joint capsule source concept in `curation/decisions.tsv` and regenerate the parent and any child records that inherit it. |

## Recommended Edits

1. Replace the `curation/decisions.tsv` row for
   `habitatmech:GOLD.1a8c452712` with an item-level decision that decides
   whether the human `Beaker's/Popliteal cyst` GOLD path should stay minted,
   should use an existing anatomical broader term or xref, or should become
   `NOT_APPLICABLE`.
2. If the target stays minted, add a `curation/term_requests.tsv` row that
   defines the intended popliteal-cyst host environment, records the corrected
   canonical label, and states whether the human `Joint capsule` source-path
   parent remains a strict broader habitat or should be replaced by a reviewed
   ontology genus.
3. Add an item-level decision for the human
   `Host-associated > Mammals: Human > Skeletal system > Joint capsule` GOLD
   source concept so the generated `habitatmech:GOLD.e7296678c2` parent no
   longer depends only on the seeder's NARROW lexical match.

## Follow-up Checks

After item-level curation, run:

1. `just seed`
2. `just seed-canary habitatmech:GOLD.1a8c452712`
3. `just render`
4. `just validate data/habitats/host_associated/beaker_s_popliteal_cyst.yaml`
5. `just validate-strict data/habitats/host_associated/beaker_s_popliteal_cyst.yaml`
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
  '*beaker*' -print` check returned no previous exact report for this generated
  stem. `find` included ignored files under the searched directory.
- `find` checks under `curation/causal_graphs`, `history`, and `research`
  found no exact slug-named causal overlay, append-only history record, or raw
  research report. `find` included ignored files under the searched
  directories.
- iModulonDB structured source checks were not applicable because the target
  names a GOLD human anatomical lesion inventory category, not a gene, locus
  tag, regulator, protein, pathway, stress-response term, or transcriptomics
  dataset.
