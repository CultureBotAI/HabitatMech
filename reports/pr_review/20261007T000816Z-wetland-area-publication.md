# PR Review: Wetland Area

- PR: https://github.com/CultureBotAI/HabitatMech/pull/1597
- Scientific baseline: `bedfc0e45b4425f1fd76f0039b701cbc630231cb`
- Review-report commit: `7e64015b04d47bba20a490b0f188040856c9879f`
- Correction/build commit: `ffcc2c70d55c16ef596369788fde1f23cd4fc005`
- Reviewer: Codex, separate adversarial pass; no independent-agent approval claimed.

## Scope and Method

Publish the completed wetland-area individual review unchanged and correct its
three unsupported source-context parents. The unfinished whale-fall review is
not included. Read the complete baseline target, individual report, maintained
curation contracts, exclusion loader/application, history emission, synonym
ingestion, mechanism tests, new regression, session and generated-record diff.
Challenge entity-type distinctions, source-specific suppression versus global
parent removal, merge scope, counts, provenance, historical attribution and
generated-product freshness.

Ignored-inclusive searches of curation, history and tests for all three source
mints found their existing ITEM decisions but no target-owned exclusions.
The existing swamp exclusion is child-owned and must remain intact. GitHub's
all-state wetland-title search found other child-edge issues, not this defect.
Filed #1598; reused the existing shared synonym-scope issue #1249.

## Findings and Disposition

1. **Major, #1598: three GOLD contexts are false superclasses.** Added exact
   mint/path/resolved-parent exclusions for GOLD.5f6044871d to ENVO:00001998
   soil, GOLD.92ce88cda1 to ENVO:00001999 marine water body, and
   GOLD.a981586d10 to ENVO:00002011 fresh water. A vegetated geographic area
   is not a kind of these materials or the whole water body. Retain the
   independently supported ENVO:01001305 vegetated-area parent.
2. **Major, #1249: ENVO synonym scope remains inflated.** Fresh official ENVO
   types WetlandRegion as RELATED; the generated ENVO assertion is EXACT.
   PREGO separately asserts it as RELATED. The current `(text, type)` key
   omits source, so a typed-scope repair must preserve both provenances when
   they converge. Added this witness and collision risk to #1249. The shared
   governed extraction/ingestion repair is not implemented by this bounded
   hierarchy PR and the issue remains open. No local raw-data or generated
   synonym patch substitutes for that repair.

Freshly fetched and parsed official typed ENVO revision
`a2455d1a77e46bb8a664d65a157166b539269042` (106,817 triples), checking the
active target, all four parents, definitions and synonym scopes. The target's
only named parent is vegetated area. Freshly read
[EPA's ecological description](https://www.epa.gov/wetlands/what-wetland),
which distinguishes wetland areas from their water and soils and includes
coastal, inland and seasonal settings. No legal interpretation is made.

No further defect in the bounded correction was established. These exclusions
do not prove coextensiveness of the three qualified GOLD bins with the generic
area. Original sample crosswalks and the complete PREGO pool remain unresolved
as documented in the individual review. No source-bin split, universal
parameter, characteristic-taxon flag or mechanism claim is invented.

## Preservation and Regression

`test_wetland_area_context_exclusions_have_exact_scope` builds all 3,206 records
with and without only the three new exclusions. Membership is identical and
exactly ENVO:00000043 changes. Its parents change from four to the independent
vegetated-area genus and three SOURCE_PARENT_EXCLUDED events are appended.
Every other field and all prior events remain equal. Explicit checks preserve
four attestations, the three GOLD organism counts (3, 61, 29), PREGO's 50-TAXON
count, exact GOLD predicates, absent PREGO predicate, 25 taxa and EXACT/REVIEWED
state. Swamp's prior area-parent exclusion is explicitly protected; every
other child record is unchanged in the full-corpus comparison.

Existing mechanism tests cover stale mint/path/parent rejection and retention
of independently supported ontology, curator and other-source parents. All
32 focused tests passed. No schema, runtime, dependency, raw inventory,
decision row or prior report/history was edited. The new session targets the
input table and attributes the work to codex-gpt-5, model gpt-5, tool codex.

## Generated Products

Both semantic exports contain 3,206 records; only wetland area's row changes,
losing the three unsupported broader-habitat lines.

- Before JSONL SHA-256: `97bc537396f79302cb1cb14617dfe211534b5e00e98778154acb4e88d715ed25`
- After JSONL SHA-256: `9662ba781a3f97222814ea346fb191ddec51f09e842bfc05e1a3e58434be4e4e`

The unchanged locked Linux runtime passed
[build 37550011911](https://github.com/CultureBotAI/HabitatMech/actions/runs/37550011911).
The changed-record canary encoded one vector and reused it on repeat. The
32-record projection canary passed. The full embed reused all 3,206 vectors,
then actual PaCMAP rebuilt the full map. Downloaded inputs are byte-identical
to the local export. Both downloaded and imported bundles passed local
validation against the downloaded real vector cache.

New immutable generation:
`d9ed54cf976224e2a6f44619e5141012b826ad2336ad7831b414535759e4dc50`.
Prior generations remain. No coordinates or freshness receipts were forged.
The temporary read-only branch-scoped workflow is removed from the final diff.
An initial local artifact check ran before download completion and found no
files; after terminal successful download the actual checks above passed.

## Validation and Publication Gates

Completed before this audit was written: dry seed, forced canary, generated
diff inspection, 32 focused tests, exact corpus reproduction (3,206 records,
zero missing/extra/differing), target open/closed schema, session validation,
lint, provenance (14 inventories and two GOLD sources), curation floor and
OAK (1,178 canonical, one synonym, five accepted exceptions, 2,055 no-adapter
skips, no failing pairs). The individual report is byte-identical to its
report commit. The initial history-scaffold invocation used an ambiguous
actor flag and wrote nothing; the corrected explicit flags produced the
validated session.

Site regeneration and full local QC are in progress at audit creation.
Final-head CI, exact-tree merge-queue checks and post-merge integrity remain
required. Completion receipts will be posted on the PR; no admin bypass or
self-approval is used. Browser visual QA was not performed.

## Remaining Scope

Fresh ignored-inclusive Path.rglob census: 1,071 reports cover 1,070 distinct
current records; 2,136 of 3,206 remain unreviewed, with no unparsed reports.
The all-record review is unfinished. #1398 was freshly verified open; this PR
does not certify SSSOM/KGX endpoint modeling or current kg-microbe compatibility.
