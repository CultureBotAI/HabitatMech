# PR Review: Watercourse and Wells

- PR: https://github.com/CultureBotAI/HabitatMech/pull/1591
- Scientific baseline: `b3675b02c0274f44e12d3ecca2b167ee10cdebe8`
- Baseline report commit: `7c230b64305c201da00199565a594e2e98513f3b`
- Correction/build commit: `4a4e6b22ace82a2995204b1f35b1fb33594a49e1`
- Reviewer: Codex, separate adversarial pass; no independent-agent approval claimed.

## Scope

Publish the three completed individual reviews for watercourse, well and well
biofilm unchanged. The unfinished well-sediment investigation is excluded.
This publication corrects established local hierarchy and provenance defects;
it does not claim that every finding in the original reports is fixed.

The pass re-read all three complete records and reports, the maintained
curation contracts, source extraction and synonym emission behavior, the
historical watercourse record, the correction diff, regression and session
history. It challenged context versus is-a, independent parent retention,
unintended identity/review promotion, source-unit preservation, alias merging,
historical attribution, evidence scope and generated-product freshness.

Ignored-inclusive searches of curation, history, tests and previous PR audits
found no target-owned well exclusions before editing. GitHub all-state title
searches for well/watercourse and a taxon-57 search found no matching issue
before filing the new findings. Existing shared synonym scope was deduplicated
against #1249, which remains open.

## Findings and Disposition

1. **Major, #1592: well has a groundwater-context superclass.** One guarded
   source-mint/path/expected-parent row excludes only that contribution.
   The independent ENVO:00000002 anthropogenic-feature parent is retained.
2. **Major, #1592: well biofilm has a groundwater-context superclass.** A
   second guarded row removes only the water-context edge. The qualified
   mint remains; no definition, genus or review-state promotion is guessed.
3. **Minor, #1593: the watercourse note attributes the prior record to GOLD.**
   Corrected the single maintained word to PREGO. Complete YAML at the parent
   of `8fc4c81ad1430ad6ea720bc9480ffa6c6859bd41` has only PREGO as attestor.
   The original decision actor/date remain; a new Codex session records this
   correction. Generated event text changes, not committed session history.
4. **Existing major, #1249: watercourse ontology synonyms lose their scope.**
   Added the independently verified witness to the shared issue. Current
   ENVO has 27 narrow and 10 related assertions across 36 spellings, including
   both scopes for `narrows`; none is exact. Typed ingestion and separately
   sourced PREGO aliases still require the governed shared repair.
5. **Major, #1594: taxon alias 57 lacks its current identifier and label.**
   Current NCBI resolves it to 3409587, Polyangium sp. (in: bacteria).
   Normalization belongs before full-source aggregation, ranking, pool counts
   and corroboration, not in generated YAML or a top-25-only substitution.
   No original BacDive/NCBITaxon dump matched an ignored-inclusive filename
   search of the configured kg-microbe data directory. Source recovery and
   governed extraction remain open; NCBITaxon:56 must remain distinct.

No additional blocking defect in the bounded corrections was established.
River-Creek coextension with watercourse and the general-well versus qualified
GOLD identity remain unresolved source-scope questions. Removing the false
biofilm parent does not complete its future genus/definition curation.

## Evidence and Preservation

Independently retrieved and parsed current official ENVO revision
`a2455d1a77e46bb8a664d65a157166b539269042`, 106,817 triples. Well,
anthropogenic geographic feature, groundwater, biofilm and watercourse are
active. Their definitions distinguish a constructed feature and a matrix-bound
microbial aggregation from underground water. The freshly inspected
[USGS account](https://www.usgs.gov/water-science-school/science/aquifers-and-groundwater)
likewise distinguishes drilled holes from water occupying rock pores. This is
entity-type evidence, not a sample-level crosswalk or universal chemistry.
The current [NCBI alias page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=57)
was also inspected; the individual report contains the all-28-taxon XML check.

`test_well_context_and_watercourse_note_corrections_have_exact_scope` builds
the complete corpus with and without exactly these input changes. Membership
is identical and only the three intended records change. It preserves every
non-parent/non-event field for the wells, the independent ontology parent,
all old events, source nodes 8262/5960, paths, one ORGANISM assertion and the
biofilm's omitted count/unit/predicate. Both remain SEEDED. For watercourse,
only one event's GOLD-to-PREGO wording changes; all scientific fields and the
original event actor/date are identical.

Three append-only histories were scaffolded with explicit actor `codex-gpt-5`,
model `gpt-5` and tool `codex`, targeting the maintained input tables. No raw
inventory, schema, dependency, source transform, prior report or committed
session-history record was changed. Trailing tabs in the modified decision
row are its two intentionally empty TSV columns; all other diff whitespace
checks pass, as does the whole diff with blank-at-EOL checking disabled.

## Generated Products

Both full semantic exports contain 3,206 records. Exactly well and well biofilm
lose `broader habitat: Groundwater`; watercourse semantic text is unchanged.

- Before JSONL SHA-256: `984bf9d8ee5811ee22a8ab0a9ceb9fbd05459872d6a309ed734171bcbcf70c81`
- After JSONL SHA-256: `85784c9872d121cc93f5d62d7c81d8bc3652795a4490dd1d3dbd96af2130b428`

The unchanged locked Linux runtime completed
[build 37541800708](https://github.com/CultureBotAI/HabitatMech/actions/runs/37541800708).
Its two-record canary encoded two vectors and reused both on repeat. A
32-record projection canary passed; full embedding reused all 3,206 vectors,
and actual PaCMAP rebuilt the complete map. Local and downloaded full inputs
are byte-identical. Both the artifact and imported bundle passed local checks
against the real vector cache. No coordinates or freshness hashes were forged.

New immutable generation:
`dafb8402c84176f752bd48d2fda330f7364ce4176c59cd1e032af70b7b599179`.
Prior generations remain. The temporary branch-scoped, read-only workflow
is removed from the final diff. Site rendering was still running when this
audit was authored; merge requires its completion and full validation.

## Validation and Merge Conditions

Completed before this audit was written:

- Dry seed and all three forced exact canaries; complete changed records inspected.
- All 30 focused regression and source-parent tests passed.
- All three open/closed schema validations passed, zero errors.
- Exact corpus reproduction: 3,206 expected/found, no missing/extra/differing files.
- All 113 session histories valid; lint passed.
- OAK correspondence: 1,178 canonical, one synonym, five accepted exceptions,
  2,055 no-adapter skips and no failing pairs.
- Real map canaries, full projection and local input/cache/bundle verification.
- Baseline reports remain byte-identical to their initial publication commit.

Full `just qc`, final site verification, final-head CI and merge-queue checks
remain mandatory. Exact completion receipts will be posted to the PR. No
admin bypass or self-approval is used. Browser visual QA was not performed.

## Remaining Scope

Ignored-inclusive filesystem census: 1,069 reports cover 1,068 distinct current
records, leaving 2,138 of 3,206 records unreviewed. The all-record review is
not complete. #1249 and #1594 remain open, as does source-mapping endpoint
issue #1398 (freshly checked). This PR does not certify SSSOM or KGX readiness
against current kg-microbe modeling.
