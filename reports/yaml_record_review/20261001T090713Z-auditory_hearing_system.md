# YAML Record Review: Auditory/Hearing system

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/host_associated/auditory_hearing_system.yaml`
- Started UTC: `2026-10-01T09:07:13Z`
- Finished UTC: `2026-10-01T09:07:13Z`
- Verdict: needs curation

## Target

Reviewed the complete generated `HabitatRecord` for the GOLD Mammals
`Auditory/Hearing system` path:

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.81aa9dc62f` |
| Label | `Auditory/Hearing system` |
| Path | `data/habitats/host_associated/auditory_hearing_system.yaml` |
| Stable slug | `auditory_hearing_system` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Source | `GOLD` |
| Source ID | `gold.ecosystem:6404` |
| Source path | `Host-associated > Mammals > Auditory/Hearing system` |

The record is generated from committed inputs. Its path is pinned by
`data/habitats/PATHS.tsv:2249`; future identity, grounding, definition, or
hierarchy repairs should be made in `curation/decisions.tsv`,
`curation/term_requests.tsv`, or the raw source inventory and then regenerated,
not hand-edited in `data/habitats/`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/auditory_hearing_system.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/host_associated/auditory_hearing_system.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, and 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; 3206 expected records, 3206 found on disk, 0 missing, 0 extra, and 0 differing. |
| `just worklist --status all --out /tmp/habitatmech-auditory-hearing-system-worklist.tsv` | Passed; wrote 953 ungrounded rows. The target appears at line 405 as a zero-assertion class-swept GOLD record, and the same-label Mammals: Human sibling appears separately at line 406. |
| `just report --out /tmp/habitatmech-auditory-hearing-system-report.tsv` | Passed; the target appears at line 2249 as `UNGROUNDED`, `SEEDED`, GOLD-only, one source, zero assertions, one parent, zero environmental parameters, zero characteristic taxa, and zero causal graphs. |
| `git diff --check` | Passed after this report was added. |

No target-specific causal overlay exists, so there was no narrower
`just validate-causal curation/causal_graphs/<slug>.yaml` command to run.

## Identity and Grounding

The generated source identity is exact. `data/raw/gold_ecosystem_paths.tsv:1983`
has one canonical row for
`Host-associated > Mammals > Auditory/Hearing system`, with leaf label
`Auditory/Hearing system`, depth 3, one GOLD node, zero organism assertions,
zero study assertions, zero biosample assertions, zero total assertions, and
node ID `gold.ecosystem:6404`.

The label is not unique by itself. GOLD also has a distinct
`Host-associated > Mammals: Human > Auditory/Hearing system` concept at
`data/raw/gold_ecosystem_paths.tsv:2149`; it is generated as
`habitatmech:GOLD.b842078e17` at
`data/habitats/host_associated/auditory_hearing_system__8fefc879.yaml`.
That sibling was inspected only to disambiguate the bare label.

The current `UNGROUNDED` status follows only from a class-level lexical sweep.
`curation/decisions.tsv:766` says no term in the vendored slice matched the
label by any sweep route and explicitly says the sweep did not assess whether
the source concept is a habitat. That is enough to explain
`mapping_status: SEEDED`; it is not enough to confirm that this should remain
undefined and ungrounded.

The generated parent is supported. `Host-associated > Mammals` is the immediate
GOLD parent path for the target, and `data/raw/gold_ecosystem_paths.tsv:9`
resolves that parent to the reviewed `mammal-associated environment` record,
`habitatmech:GOLD.e889967f4f`. The target is not claiming to be a specific
anatomical `ear`; it is a mammal-host auditory/hearing branch whose direct GOLD
children include Mammals `Inner ear`, `Middle ear`, and `Outer ear` paths.

`UBERON:0001690` is an important near miss, not an automatic replacement.
The vendored slice labels it `ear` and records `auditory apparatus` as a
synonym, and the Human GOLD child path
`Host-associated > Mammals: Human > Auditory/Hearing system > Ear` already
grounds exactly to `UBERON:0001690`. A curator should explicitly decide whether
the Mammals `Auditory/Hearing system` category is merely an auditory-system
grouping, should get `UBERON:0001690` as a broader parent, or should be
collapsed only after accounting for the same-branch exact `Ear` child.

## Evidence

The record has no authored definition, synonyms, xrefs, environmental
parameters, characteristic taxa, record-level evidence, causal graphs,
discussions, or datasets. There are no claim-level citations to audit.

| Claim | Nearest maintained support | Review |
|---|---|---|
| The source attestation preserves GOLD node `6404`, the source label, and the full source path. | `data/raw/gold_ecosystem_paths.tsv:1983` | Supported exactly. |
| No `assertion_count` should be emitted for this GOLD attestation. | The exact raw row reports `organism_count`, `study_count`, `biosample_count`, and `total_assertions` as zero. An ignored/hidden-inclusive exact search for the full source path found no row in `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`, or `data/raw/gold_studies.tsv`. | Supported. |
| The only generated parent is `habitatmech:GOLD.e889967f4f`. | GOLD places the target directly under `Host-associated > Mammals`; `data/habitats/PATHS.tsv:3021` pins `habitatmech:GOLD.e889967f4f` to `mammals`, and the generated `mammals.yaml` record is defined as `mammal-associated environment`. | Supported. |
| The rendered page mirrors the YAML. | `pages/habitats/auditory-hearing-system-habitatmech-gold-81aa9dc62f.html` | Supported; the page shows the same ID, label, `HOST_ASSOCIATED` category, `UNGROUNDED` grounding, `SEEDED` mapping, GOLD source path, missing assertion count, broader mammal-associated parent, and class-level curation event. |

Ignored/hidden-inclusive exact searches found no target-specific maintained
term request, target-specific causal graph overlay, append-only history record,
deep-research report, or prior exact YAML review for
`habitatmech:GOLD.81aa9dc62f`, `gold.ecosystem:6404`, the
`auditory_hearing_system.yaml` slug, or the exact GOLD source path.

## Completeness

The record is complete for its generated zero-assertion GOLD projection, but
not for item-level HabitatMech curation.

The empty optional slots are currently appropriate: no maintained input or GOLD
side table supplies physicochemical parameters, characteristic taxa,
claim-level evidence, a causal graph, discussions, or datasets for this exact
source path.

The substantive gap is the same one named by the class-level decision. The
source path is a real host-associated GOLD category with direct anatomical
children, but nobody has made an item-level decision about the habitat identity
or authored a definition that explains what a mammalian
auditory/hearing-system environment is and how it differs from the exact
`UBERON:0001690` ear child already present in the human branch.

## Findings

| Severity | Finding | Owner |
|---|---|---|
| Major | `habitatmech:GOLD.81aa9dc62f` is still only class-reviewed. The live record is a `SEEDED`, undefined, `UNGROUNDED` Mammals auditory-system category whose sole decision explicitly did not assess whether the source concept is a habitat, whether `UBERON:0001690` should be retained as a broader ear/anatomy parent or a near-miss xref, or whether an ENVO-style term should be requested for this host sub-environment. | Replace the class-depth row with an item-level decision in `curation/decisions.tsv`; if the source concept remains minted, add a definition in `curation/term_requests.tsv` under the tightest defensible genus, then regenerate the target. |

## Recommended Edits

1. In `curation/decisions.tsv`, add item-level review for
   `habitatmech:GOLD.81aa9dc62f` that decides whether the Mammals
   `Auditory/Hearing system` path should stay minted, should keep
   `UBERON:0001690` as a broader parent or an xref, or should make a different
   relationship claim.
2. If the source concept remains a minted `UNGROUNDED` habitat, add a
   definition to `curation/term_requests.tsv`, using `ADD` unless item review
   proves the inherited `mammal-associated environment` parent is false.
3. Regenerate with `just seed` and
   `just seed-canary habitatmech:GOLD.81aa9dc62f`; inspect
   `data/habitats/host_associated/auditory_hearing_system.yaml` before a full
   `just seed-apply --force`.

## Follow-up Checks

After item-level curation, run:

1. `just validate data/habitats/host_associated/auditory_hearing_system.yaml`
2. `just validate-strict data/habitats/host_associated/auditory_hearing_system.yaml`
3. `just validate-causal-all`
4. `just validate-history`
5. `just term-requests-check`
6. `just verify-corpus --max-diffs 1`
7. `just render`
8. Inspect `pages/habitats/auditory-hearing-system-habitatmech-gold-81aa9dc62f.html`
9. `git diff --check`

## Additional Notes

- Exact ignored/hidden-inclusive searches covered `curation`, `history`,
  `research`, `reports`, `data/raw`, `data/habitats`, generated habitat pages,
  and `build/text-map`. They excluded `.git`, `pages/text-map`, and
  `data/text_map` to avoid irrelevant Git internals and very large generated
  JSON text-map lines.
- The search for the exact target source path under `data/raw` found only the
  `gold_ecosystem_paths.tsv` row and no direct GOLD biosample, study, or triad
  side-table row.
- The same-label Mammals: Human `Auditory/Hearing system` record is also
  zero-assertion and class-swept. It should be reviewed separately by its own
  source concept, `habitatmech:GOLD.b842078e17`.
- iModulonDB structured source checks were not applicable because the target
  names a GOLD anatomical habitat category, not a gene, locus tag, regulator,
  protein, pathway, stress-response term, or transcriptomics dataset.
