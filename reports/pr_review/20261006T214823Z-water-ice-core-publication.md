# PR Review: Water Ice Core

- PR: https://github.com/CultureBotAI/HabitatMech/pull/1589
- Scientific baseline: `aedc7665228b0881f87b2b67384c6d4cc2c54ed8`
- Initial report commit: `575bf9d4a4867cccd33ca696a58a1cfd757dd7f4`
- Correction/build commit: `d1d7f619862e32f73ae5ecbbadfa876c83c04c06`
- Reviewer: Codex, separate adversarial pass; no independent-agent review claimed.

## Scope

Publish `reports/yaml_record_review/20261006T212917Z-water_ice_core.md`
unchanged as a baseline judgement, then correct its established source-parent
defect. The unfinished watercourse investigation is excluded. This publication
does not claim that all findings in the original report are fixed.

The pass re-read the complete record and report, maintained exclusion contract,
synonym ingestion/emission code, correction diff, regression and session history.
It challenged context versus is-a, independent-parent preservation, accidental
identity promotion, source units, fabricated evidence, generated-output freshness
and overstatement of validation. Ignored-inclusive searches of curation, history,
tests and PR audits found no existing target-owned exclusion. GitHub's all-state
water-ice-core issue search returned no match before #1590 was filed.

## Findings and Disposition

1. **Major, #1590: saline-lake context emitted as a superclass.** Corrected
   with one guarded source-mint/path/expected-parent row in
   `curation/gold_parent_exclusions.tsv`. A drilled ice mass is not a kind of
   the whole lake. The independent ENVO:01000293 ice-mass parent remains.
2. **Existing major, #1249: broad ontology synonyms emitted as exact.** Added
   the independently verified two-string witness to the existing issue.
   The governed typed-ontology ingestion change remains open; this PR does
   not patch generated aliases or close the shared issue. Preserve the
   separately sourced GOLD label when repairing it.

No additional blocking publication defect was established in this bounded pass.
The GOLD path does not prove the multi-year snow-accumulation definition. That
source-identity question remains unresolved, not a third established finding
or grounds to invent a replacement identity. Preserving CLOSE/REVIEWED records
existing provenance; it is not a new endorsement of the old identity decision.

## Evidence and Preservation

Independently retrieved and parsed current official ENVO revision
`a2455d1a77e46bb8a664d65a157166b539269042`, 106,817 triples. All three IDs
are active. ENVO:01001530 denotes drilled ice with the stated accumulation
history and has ENVO:01000293 as its named superclass; ENVO:00000019 denotes
a whole saline lake. Both `ice core` and `ice sample` have broad scope, with
no exact, narrow or related assertions on this target. The report's earlier
inspected PubMed abstract/captions remain its literature basis; a fresh web
request was rate-limited, and no new full-paper inspection is claimed.

`test_water_ice_core_exclusion_changes_only_context_parent_and_audit` builds
the complete corpus with and without only the new exclusion. Membership is
identical and exactly ENVO:01001530 changes. The test preserves every other
field and old event, including CLOSE/REVIEWED, skos:closeMatch, source node
7982, the complete path and absent assertion count/unit. It checks the
retained parent and the appended event's action, curator and date.

Session history was scaffolded with explicit actor `codex-gpt-5`, model
`gpt-5` and tool `codex`, targeting the maintained exclusion table. No prior
report or committed history was rewritten. No raw inventory, dependency,
schema, extraction rule or unrelated record was edited.

## Generated Products

Complete before/after adapter exports contain 3,206 records. Only water ice
core changes, by removing `broader habitat: saline lake`.

- Before JSONL SHA-256: `aa2ed67aaa262ced0e3073b8d5e9cfba09cb826f352fefc14f28b814287887db`
- After JSONL SHA-256: `984bf9d8ee5811ee22a8ab0a9ceb9fbd05459872d6a309ed734171bcbcf70c81`

The unchanged locked Linux runtime completed
[build 37535978764](https://github.com/CultureBotAI/HabitatMech/actions/runs/37535978764).
Its target canary encoded one vector, then reused that vector on repeat.
A separate 32-record projection canary passed. The full embedding pass reused
all 3,206 vectors, and actual PaCMAP rebuilt the complete projection. Locally
exported full inputs are byte-identical to the downloaded CI inputs; the
artifact and imported bundle both passed verification with the vector cache.

New immutable generation:
`6f9c86711f9f3c67d8697990400329db83d24a1ffd16e4e3ed5acfe232fb8293`.
Old generations are retained. The temporary read-only, branch-scoped workflow
is removed from the final diff. No fabricated coordinates or checksum-only
freshness patch was used. An initial local import used the wrong directory;
the renderer rejected the missing bundle before publication. The actual
bundle was then imported, verified again and rendering restarted.

## Validation and Merge Conditions

Completed before this audit was written:

- Dry seed and forced exact canary; generated YAML inspected in full.
- All 29 focused parent-exclusion tests passed.
- Target open and closed schema validation, zero errors.
- Exact corpus reproduction: 3,206 expected/found, no missing/extra/differing records.
- All 110 history records valid.
- OAK labels: 1,178 canonical, one synonym, five accepted exceptions,
  2,055 no-adapter skips; no failing correspondence.
- Real map canaries, full projection and local artifact/cache/input verification.
- No whitespace errors; original individual report remains byte-identical.

Fresh full `just qc` and site rendering were still running at audit creation.
Merge requires their successful completion plus final-head and merge-queue
checks; exact completion receipts will be recorded on the PR. No admin bypass
or self-approval is part of this workflow. Browser visual QA was not performed.

## Remaining Scope

An ignored-inclusive filesystem census finds 1,066 review files covering
1,065 distinct current records, leaving 2,141 of 3,206 records unreviewed.
The all-record review remains unfinished. Shared synonym scope (#1249),
source-mapping endpoint semantics (#1398), and original sample-level identity
evidence remain outstanding. This publication does not certify SSSOM or KGX
compatibility with current kg-microbe modeling.
