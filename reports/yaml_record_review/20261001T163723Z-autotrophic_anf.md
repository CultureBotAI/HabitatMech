# YAML Record Review: Autotrophic (ANF)

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/host_associated/autotrophic_anf.yaml`
- Started UTC: `2026-10-01T16:37:23Z`
- Finished UTC: `2026-10-01T16:37:23Z`
- Verdict: needs curation

## Target

Reviewed the complete generated `HabitatRecord` for the GOLD
nanoflagellate ANF path:

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.052d6c8006` |
| Label | `Autotrophic (ANF)` |
| Path | `data/habitats/host_associated/autotrophic_anf.yaml` |
| Stable slug | `autotrophic_anf` |
| Class | `HabitatRecord` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Source | `GOLD` |
| Source ID | `gold.ecosystem:7729` |
| Source path | `Host-associated > Protists > Nanoflagellates > Autotrophic (ANF)` |

The record is generated from committed inputs. `data/habitats/PATHS.tsv:1304`
pins `habitatmech:GOLD.052d6c8006` to `autotrophic_anf`, and future
item-level decisions belong in `curation/decisions.tsv`, not as hand edits to
the generated YAML or rendered page.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/autotrophic_anf.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/host_associated/autotrophic_anf.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, and 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; 3206 expected records, 3206 found on disk, 0 missing, 0 extra, and 0 differing. |
| `just worklist --status all --out /tmp/habitatmech-record-review-worklist.tsv` | Passed; wrote 953 ungrounded rows. The target appears at line 408 as a zero-assertion class-swept GOLD record. |
| `just report --out /tmp/habitatmech-record-review-report.tsv` | Passed; the target appears at line 1304 as `UNGROUNDED`, `SEEDED`, GOLD-only, one source, zero assertions, one parent, zero environmental parameters, zero characteristic taxa, and zero causal graphs. |

No target-specific causal overlay exists, so there was no narrower
`just validate-causal curation/causal_graphs/<slug>.yaml` command to run.

## Identity and Grounding

The generated source identity is exact. `data/raw/gold_ecosystem_paths.tsv:2541`
has one row for `Host-associated > Protists > Nanoflagellates > Autotrophic
(ANF)`, with leaf label `Autotrophic (ANF)`, depth 4, two GOLD ecosystem node
IDs, zero organism assertions, zero study assertions, zero biosample assertions,
zero total assertions, and source IDs `gold.ecosystem:7729|gold.ecosystem:7730`.

The target currently has only a class-level `CONFIRM_UNGROUNDED` decision at
`curation/decisions.tsv:126`. That decision is reproducible but intentionally
incomplete: it says no term in the then-vendored slice matched this label by
any search route, but it also says whether the concept is a habitat was not
assessed.

The record's only generated parent is `habitatmech:GOLD.d366a6d2a2`, the
generated source-path parent for `Host-associated > Protists >
Nanoflagellates`. That parent is also `UNGROUNDED`, `SEEDED`, and only
class-swept at `curation/decisions.tsv:1166`.

The ontology candidates ranked for this row support the class sweep. BTO names
`BTO:0002258` as `autotroph` with definition `An autotrophic organism`, and
`BTO:0002259` as `autotrophic cell`; both name organisms or cells rather than
the environment associated with those organisms. The sibling leaves
`Heterotrophic (HNF)` and `Mixotrophic (MNF)` have the same generated shape:
each is a zero-assertion, class-swept GOLD child of `Nanoflagellates` with no
definition, no evidence slots, and no characteristic taxa.

## Evidence

The record has no authored definition, synonyms, xrefs, environmental
parameters, characteristic taxa, record-level evidence, causal graphs,
discussions, or datasets. There are no claim-level citations to audit.

| Claim | Nearest maintained support | Review |
|---|---|---|
| The source attestation preserves GOLD node `7729`, the source label, and the full source path. | `data/raw/gold_ecosystem_paths.tsv:2541` | Supported exactly. GOLD collapses `gold.ecosystem:7729|gold.ecosystem:7730` into one canonical path and the generated attestation reports the first node ID with a shared-node note. |
| No direct source assertion count is emitted. | `data/raw/gold_ecosystem_paths.tsv:2541` has zero organism, study, biosample, and total assertions for this exact path. | Supported. |
| No GOLD biosample, study, or triad side table supplies extra exact-path evidence. | An ignored/hidden-inclusive exact search for `Host-associated > Protists > Nanoflagellates > Autotrophic (ANF)\t` found only `data/raw/gold_ecosystem_paths.tsv:2541`. | Supported. |
| Parent `habitatmech:GOLD.d366a6d2a2` preserves GOLD source-path hierarchy. | `data/raw/gold_ecosystem_paths.tsv:2540` is the `Host-associated > Protists > Nanoflagellates` parent path, and `data/habitats/PATHS.tsv:2850` pins it to `nanoflagellates`. | Supported as source hierarchy. Not supported as item-level habitat curation because the parent is also only class-swept. |
| The rendered page mirrors the YAML. | `pages/habitats/autotrophic-anf-habitatmech-gold-052d6c8006.html` | Supported; it shows the same identifier, category, `UNGROUNDED` grounding, `SEEDED` mapping, GOLD source path, missing assertion count, broader `Nanoflagellates` habitat, and class-level curation event. |

Ignored/hidden-inclusive exact searches found no target-specific term request,
causal graph overlay, append-only history record, or prior exact YAML review
whose `Record` line names
`data/habitats/host_associated/autotrophic_anf.yaml`.

## Completeness

The record is complete for its generated GOLD projection, but it is not
complete as item-level HabitatMech curation.

The empty optional slots are currently appropriate: no maintained source input
or exact GOLD side table supplies a definition, physicochemical parameters,
characteristic taxa, claim-level evidence, a causal graph, discussions, or
datasets for this exact zero-assertion source path.

The substantive gap is semantic, not generative. `Autotrophic (ANF)` is a
trophic descriptor in a nanoflagellate organism branch, and the obvious
ontology candidates are organism or cell terms. A curator still needs to state
whether GOLD's ANF, HNF, and MNF leaves denote host-associated environments
associated with those nanoflagellate groups, source inventory categories that
should be merged into the `Nanoflagellates` parent, or organism/trophic-mode
bins that should become `NOT_APPLICABLE`.

## Findings

| Severity | Finding | Owner |
|---|---|---|
| Major | `habitatmech:GOLD.052d6c8006` is still only class-reviewed even though its label does not name a habitat. The live record is a zero-assertion GOLD `Autotrophic (ANF)` nanoflagellate leaf whose only parent is the class-swept `Nanoflagellates` record, and the ranked ontology candidates name an autotrophic organism or cell rather than an environment. This leaves the target without an item-level decision on whether the GOLD ANF/HNF/MNF leaves should be minted as host-associated environments, merged into the nanoflagellate branch parent, or marked `NOT_APPLICABLE` because they represent trophic organism bins rather than habitats. | Replace the class-depth `curation/decisions.tsv` row with an item-level decision; audit the `Nanoflagellates`, `Heterotrophic (HNF)`, and `Mixotrophic (MNF)` sibling records as one branch; if the ANF row remains minted, define the intended host-associated nanoflagellate environment and keep BTO organism/cell terms out of the habitat identity. |

## Recommended Edits

1. Replace the `curation/decisions.tsv` row for
   `habitatmech:GOLD.052d6c8006` with an item-level decision that decides
   whether `Autotrophic (ANF)` should stay minted, should merge into
   `habitatmech:GOLD.d366a6d2a2`, or should become `NOT_APPLICABLE`.
2. Audit the source-path sibling records `habitatmech:GOLD.1e8f6911f5`
   (`Heterotrophic (HNF)`) and `habitatmech:GOLD.c9a52231f1` (`Mixotrophic
   (MNF)`) with the same criterion so the three nanoflagellate trophic leaves
   receive consistent decisions.
3. If the target stays minted, add a `curation/term_requests.tsv` row that
   defines the intended autotrophic-nanoflagellate-associated host environment
   and regenerate with `just seed` and
   `just seed-canary habitatmech:GOLD.052d6c8006`.

## Follow-up Checks

After item-level curation, run:

1. `just seed`
2. `just seed-canary habitatmech:GOLD.052d6c8006`
3. `just render`
4. `just validate data/habitats/host_associated/autotrophic_anf.yaml`
5. `just validate-strict data/habitats/host_associated/autotrophic_anf.yaml`
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
  only `data/raw/gold_ecosystem_paths.tsv:2541` and no exact GOLD biosample,
  study, or triad side-table row.
- iModulonDB structured source checks were not applicable because the target
  names a GOLD host-associated protist inventory category, not a gene, locus
  tag, regulator, protein, pathway, stress-response term, or transcriptomics
  dataset.
