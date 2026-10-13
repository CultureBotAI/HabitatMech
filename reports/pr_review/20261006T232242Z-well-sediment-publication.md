# PR Review: Well Sediment

- PR: https://github.com/CultureBotAI/HabitatMech/pull/1595
- Scientific baseline: `c663762cac4c4c7dd0570be7a73cbfa21407aeeb`
- Baseline report commit: `a0a0d569af219090682bf0fa224d19b65cf67577`
- Correction/build commit: `fabf92945c10045129849640f955552eb9604434`
- Reviewer: Codex, separate adversarial pass; no independent-agent approval claimed.

## Scope

Publish the completed well-sediment individual review unchanged and correct its
unsupported source-context parent. The unfinished wetland-area investigation
is not part of this PR. The review challenged material versus water identity,
source contribution versus accumulated parents, status promotion, count units,
historical attribution, exact change scope and generated-product freshness.

The pass read the complete target and immediate-parent records, individual
report, maintained curation contracts, exclusion loader and source-parent
application, schema, regression tests, session and correction diff. An
ignored-inclusive search of curation, history, tests and prior PR audits found
only the target's existing CLASS decision, not a target exclusion. An all-state
GitHub exact-phrase search found no well-sediment issue before filing #1596.

## Finding and Disposition

**Major, #1596: well sediment incorrectly inherits groundwater context.**
The qualified sediment source habitatmech:GOLD.71a5958fdc is not a type of
habitatmech:GOLD.22a80cbd14, the groundwater source in its path. Added one row
to `curation/gold_parent_exclusions.tsv`, guarded by the exact source mint,
complete path and expected resolved parent. It removes only that contribution.

Freshly retrieved and parsed the official typed ENVO revision
`a2455d1a77e46bb8a664d65a157166b539269042`, with 106,817 triples. Sediment,
groundwater, well and aquifer are active. Their definitions distinguish
deposited particulate material, pore-space water, a constructed hole and a
water-bearing geological layer. The committed exact-path GOLD triad at
`gold_path_triads.tsv:212` through line 214 distinguishes aquifer, well and
sediment in broad/local/medium roles. This supports excluding water as a
superclass; one triad-annotated sample/study does not establish detailed
sample composition or independent replication.

No other blocking defect was established in the bounded correction. No
replacement genus, definition or exact grounding is asserted. Generic sediment
remains a future broader-term candidate. The original study-to-BioSample
crosswalk remains unrecovered, as documented in the individual review; the
publication pass did not obtain a new successful live GOLD study response.

## Preservation and Regression

`test_well_sediment_context_exclusion_has_exact_scope` builds the complete
corpus with and without only the new exclusion. Membership is identical and
only well sediment changes: its sole parent is removed and one deterministic
SOURCE_PARENT_EXCLUDED event is appended. Every other field and all previous
events are equal. Explicit assertions preserve GOLD5959, the full path, one
ORGANISM assertion, omitted mapping predicate, UNGROUNDED grounding and
CLASS/SEEDED identity-review provenance. The exclusion does not endorse the
CLASS sweep as an individual identity review.

The existing mechanism tests cover stale path/parent/mint rejection and
independent ontology, curator and other-source parent preservation. All 31
focused tests passed. No source transform, schema, dependency, raw inventory,
decision row or prior report/history was edited. The new session was scaffolded
with explicit actor codex-gpt-5, model gpt-5 and tool codex, targeting the input
table and linking #1596 and this PR.

## Generated Products

Both full semantic exports contain 3,206 records. Exactly well sediment loses
`broader habitat: Groundwater`; no other semantic row changes.

- Before JSONL SHA-256: `85784c9872d121cc93f5d62d7c81d8bc3652795a4490dd1d3dbd96af2130b428`
- After JSONL SHA-256: `97bc537396f79302cb1cb14617dfe211534b5e00e98778154acb4e88d715ed25`

The unchanged locked Linux runtime completed
[build 37545958410](https://github.com/CultureBotAI/HabitatMech/actions/runs/37545958410).
Its one-record canary encoded one vector and reused it on repeat. A 32-record
projection canary passed. Full embedding reused all 3,206 vectors, then actual
PaCMAP rebuilt the full map. Local and downloaded inputs are byte-identical;
the downloaded bundle passed local validation against the real vector cache.

Imported immutable generation:
`68072fafdc9ba7be5fbc622d3812c9cc91bdfa4b363c030f5a348771753efda0`.
Prior generations remain. No coordinates or freshness receipts were forged.
The temporary branch-scoped, read-only workflow was removed from the final
working-tree diff. Site rendering and imported-bundle validation were running
when this audit was authored; completion is required before publication.

## Validation and Merge Conditions

Completed before this audit was written:

- Dry seed and exact forced canary; complete generated target inspected.
- All 31 focused tests passed, including full-corpus before/after regression.
- Exact corpus: 3,206 expected/found, zero missing, extra or differing records.
- Target open/closed schema and new append-only session validation passed.
- Lint, raw provenance (14 inventories, two GOLD sources) and curation floor passed.
- OAK: 1,178 canonical, one synonym, five accepted exceptions and 2,055
  no-adapter skips; no failing ID-label pair.
- Real map canaries/full projection, input equality and downloaded-bundle/cache checks passed.
- Individual review remains byte-identical to its baseline report commit.

Full `just qc`, final site verification, final-head CI and native merge-queue
checks remain mandatory. Exact completion receipts will be posted to the PR.
No admin bypass or self-approval is used. Browser visual QA was not performed.

## Remaining Scope

Ignored-inclusive filesystem census: 1,070 reports cover 1,069 distinct current
records, leaving 2,137 of 3,206 records unreviewed. The all-record goal remains
unfinished. #1398 was freshly verified open: this publication does not certify
SSSOM/KGX source-endpoint modeling or current kg-microbe compatibility.
