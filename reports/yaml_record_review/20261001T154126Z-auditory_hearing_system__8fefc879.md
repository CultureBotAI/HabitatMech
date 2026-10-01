# YAML Record Review: Auditory/Hearing system

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/host_associated/auditory_hearing_system__8fefc879.yaml`
- Started UTC: `2026-10-01T15:41:26Z`
- Finished UTC: `2026-10-01T15:41:26Z`
- Verdict: needs curation

## Target

Reviewed the complete generated `HabitatRecord` for the GOLD Mammals: Human
auditory-system path:

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.b842078e17` |
| Label | `Auditory/Hearing system` |
| Path | `data/habitats/host_associated/auditory_hearing_system__8fefc879.yaml` |
| Stable slug | `auditory_hearing_system__8fefc879` |
| Class | `HabitatRecord` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Source | `GOLD` |
| Source ID | `gold.ecosystem:6267` |
| Source path | `Host-associated > Mammals: Human > Auditory/Hearing system` |

The record is generated from committed inputs. `data/habitats/PATHS.tsv:2642`
pins `habitatmech:GOLD.b842078e17` to
`auditory_hearing_system__8fefc879`, and future item-level decisions belong in
`curation/decisions.tsv`, not as hand edits to the generated YAML or rendered
page.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/auditory_hearing_system__8fefc879.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/host_associated/auditory_hearing_system__8fefc879.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, and 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; 3206 expected records, 3206 found on disk, 0 missing, 0 extra, and 0 differing. |
| `just worklist --status all --out /tmp/habitatmech-record-review-next-worklist.tsv` | Passed; wrote 953 ungrounded rows. The target appears at line 406 as a zero-assertion class-swept GOLD record. |
| `just report --out /tmp/habitatmech-record-review-next-report.tsv` | Passed; the target appears at line 2642 as `UNGROUNDED`, `SEEDED`, GOLD-only, one source, zero assertions, one parent, zero environmental parameters, zero characteristic taxa, and zero causal graphs. |
| `just render-check` | Passed; rendered 3206 habitat pages, 231 redirect stubs, 8 categories, and 123 term requests to a temporary site and confirmed `pages/` is in step with the corpus. |

No target-specific causal overlay exists, so there was no narrower
`just validate-causal curation/causal_graphs/<slug>.yaml` command to run.

## Identity and Grounding

The generated source identity is exact. `data/raw/gold_ecosystem_paths.tsv:2149`
has one row for `Host-associated > Mammals: Human > Auditory/Hearing system`,
with leaf label `Auditory/Hearing system`, depth 3, three GOLD ecosystem node
IDs, zero organism assertions, zero study assertions, zero biosample
assertions, zero total assertions, and source IDs
`gold.ecosystem:6267|gold.ecosystem:7050|gold.ecosystem:7051`.

The target currently has only a class-level `CONFIRM_UNGROUNDED` decision at
`curation/decisions.tsv:1037`. That decision is reproducible but intentionally
incomplete: it says no term in the then-vendored slice matched this label by
any search route, but it also says whether the concept is a habitat was not
assessed.

The exact GOLD path is a human host auditory/hearing branch, not an anatomical
`ear` record. `UBERON:0001690` is vendored as `ear` with `auditory apparatus`
as a synonym at `data/raw/ontology_terms.tsv:13054`, but the human
`Host-associated > Mammals: Human > Auditory/Hearing system > Ear` child is the
record already generated as exact `UBERON:0001690` at
`data/habitats/host_associated/ear.yaml`. A curator should decide whether the
parent auditory/hearing system is a source grouping that should stay minted
under `habitatmech:GOLD.cd0b0940e5`, should keep `UBERON:0001690` as a related
anatomy term, or should receive some other item-level treatment.

The generated parent `habitatmech:GOLD.cd0b0940e5` preserves the GOLD
`Host-associated > Mammals: Human` source hierarchy. That parent is already
item-reviewed as a human-associated environment with a term request at
`curation/term_requests.tsv:4`, so this target's unresolved status is local to
the auditory/hearing branch.

## Evidence

The record has no authored definition, synonyms, xrefs, environmental
parameters, characteristic taxa, record-level evidence, causal graphs,
discussions, or datasets. There are no claim-level citations to audit.

| Claim | Nearest maintained support | Review |
|---|---|---|
| The source attestation preserves GOLD node `6267`, the source label, and the full source path. | `data/raw/gold_ecosystem_paths.tsv:2149` | Supported exactly. GOLD collapses `gold.ecosystem:6267|gold.ecosystem:7050|gold.ecosystem:7051` into one canonical path and the generated attestation reports the first node ID with a shared-node note. |
| No direct source assertion count is emitted. | `data/raw/gold_ecosystem_paths.tsv:2149` has zero organism, study, biosample, and total assertions for this exact path. | Supported. |
| Parent `habitatmech:GOLD.cd0b0940e5` preserves GOLD source-path hierarchy. | `data/raw/gold_ecosystem_paths.tsv:2` is the `Host-associated > Mammals: Human` parent path, `data/habitats/PATHS.tsv:2794` pins it to `mammals_human`, and `curation/decisions.tsv:1132` plus `curation/term_requests.tsv:4` support its item-reviewed minted identity. | Supported as source hierarchy. |
| No GOLD biosample, study, or triad side table supplies extra exact-path evidence. | An ignored/hidden-inclusive exact search for `Host-associated > Mammals: Human > Auditory/Hearing system\t` found only `data/raw/gold_ecosystem_paths.tsv:2149`. | Supported. |
| The rendered page mirrors the YAML. | `pages/habitats/auditory-hearing-system-habitatmech-gold-b842078e17.html` | Supported; it shows the same identifier, category, `UNGROUNDED` grounding, `SEEDED` mapping, GOLD source path, missing assertion count, broader habitat, and class-level curation event. |

Ignored/hidden-inclusive exact searches found no target-specific term request,
causal graph overlay, append-only history record, or prior exact YAML review
whose `Record` line names
`data/habitats/host_associated/auditory_hearing_system__8fefc879.yaml`.

## Completeness

The record is complete for its generated GOLD projection, but it is not
complete as item-level HabitatMech curation.

The empty optional slots are currently appropriate: no maintained source input
or exact GOLD side table supplies a definition, physicochemical parameters,
characteristic taxa, claim-level evidence, a causal graph, discussions, or
datasets for this exact zero-assertion source path.

The substantive gap is the class-depth decision. The direct human auditory
children range from zero-assertion grouping leaves such as `Inner ear` and
`Middle ear > Eustachian tube` to the 55-assertion `Middle ear` child, the
16-assertion `Middle ear > Effusion` child, and the exact nine-assertion
`UBERON:0001690` `Ear` child. The parent record still needs an item-level
decision that states whether the branch itself denotes a valid human
host-associated environment, whether any ontology anatomy should be retained as
a parent or xref, and whether a novel-term definition is needed.

## Findings

| Severity | Finding | Owner |
|---|---|---|
| Major | `habitatmech:GOLD.b842078e17` is still only class-reviewed. The live record is a `SEEDED`, undefined, `UNGROUNDED` Human auditory-system category whose sole decision explicitly did not assess whether the source concept is a habitat, whether `UBERON:0001690` should be treated as the exact `Ear` child only or also retained as a broader/related anatomy term, or whether an ENVO-style term should be requested for this host sub-environment. | Replace the class-depth `curation/decisions.tsv` row with an item-level decision; if the source concept remains minted, add a definition in `curation/term_requests.tsv` under the tightest defensible genus, then regenerate the target. |

## Recommended Edits

1. Replace the `curation/decisions.tsv` row for
   `habitatmech:GOLD.b842078e17` with an item-level decision that decides
   whether the Human `Auditory/Hearing system` GOLD path should stay minted,
   should be merged, or should be marked non-applicable.
2. If it stays minted, add a `curation/term_requests.tsv` row that defines the
   intended human auditory/hearing-system environment and records whether
   `UBERON:0001690` is a broader parent, an xref, or only the exact generated
   `Ear` child.
3. Regenerate with `just seed` and
   `just seed-canary habitatmech:GOLD.b842078e17`; inspect
   `data/habitats/host_associated/auditory_hearing_system__8fefc879.yaml`
   before a full `just seed-apply --force`.

## Follow-up Checks

After item-level curation, run:

1. `just seed`
2. `just seed-canary habitatmech:GOLD.b842078e17`
3. `just render`
4. `just validate data/habitats/host_associated/auditory_hearing_system__8fefc879.yaml`
5. `just validate-strict data/habitats/host_associated/auditory_hearing_system__8fefc879.yaml`
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
- The search for the exact target source path under GOLD side tables found only
  `data/raw/gold_ecosystem_paths.tsv:2149` and no exact GOLD biosample, study,
  or triad side-table row.
- The same-label Mammals `Auditory/Hearing system` record has already been
  reviewed separately by its own source concept,
  `habitatmech:GOLD.81aa9dc62f`.
- iModulonDB structured source checks were not applicable because the target
  names a GOLD anatomical habitat category, not a gene, locus tag, regulator,
  protein, pathway, stress-response term, or transcriptomics dataset.
