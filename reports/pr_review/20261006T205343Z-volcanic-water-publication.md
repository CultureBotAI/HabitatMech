# PR Review: Volcanic and Water Body

- PR: https://github.com/CultureBotAI/HabitatMech/pull/1586
- Scientific baseline: `85e321c7c943461d35b10c37cd633c4d6f4ea917`
- Initial report commit: `0397277e16b692bc55742cea60fec560c7574df3`
- Implementation/build commit: `b3f11867e28815a042fcfdc80effdf0b3b2adae6`
- Reviewer: Codex, separate adversarial pass; no independent-agent review claimed.

## Scope

Publish the completed individual reports
`reports/yaml_record_review/20261006T203103Z-volcanic.md` and
`reports/yaml_record_review/20261006T203513Z-water_body.md`, preserving their
baseline verdicts and original text. Correct only the established Volcanic
source-parent defect. The unfinished water ice core investigation is excluded.

The pass re-read both complete YAML records and reports, the maintained
exclusion contract, the extraction/seeding synonym path, implementation diff,
regression and session history. It challenged source-context versus is-a,
independent-parent retention, units, review status, scope of evidence, stale
generated outputs, and overstatement of validation or product readiness.
Ignored-inclusive curation/history/test searches found no prior target-owned
Volcanic exclusion in those surfaces. GitHub's all-state volcanic issue search
returned no match before #1587 was filed; the shared scope defect already has
an issue and was not duplicated.

## Findings and Disposition

1. **Major, #1587: unsupported marine-water-body parent.** The immediate
   Marine source context supplied ENVO:00001999, but the volcanic feature
   is not a kind of its surrounding water body. Corrected by one guarded
   mint/path/expected-parent row in `curation/gold_parent_exclusions.tsv`.
   The independently contributed ENVO:00000094 parent is retained.
2. **Minor, #1588: misleading default session actor name.** The scaffold
   retained `claude-code` as the actor name in
   `history/mappings/volcanic/2026-10-06T204819Z-claude-code-aaa828.yaml`,
   despite correct `gpt-5` model and `codex` tool fields. Corrected through
   `history/mappings/volcanic/2026-10-06T205026Z-codex-gpt-5-4a23c7.yaml`,
   explicitly attributing the session to `codex-gpt-5`. The original record,
   timestamp and scientific statements are preserved, not rewritten.
3. **Existing major, #1249: water-body broad synonym emitted as exact.**
   Added the verified mixed-scope witness to the existing issue. This PR does
   not implement the governed typed-ontology ingestion contract and must not
   close that issue. The four genuine ENVO exact synonyms and seven separate
   PREGO related assertions are preservation controls, not grounds for a
   blanket downgrade. The water-body YAML remains unchanged.

No additional blocking finding was established in this bounded pass. The
original reports' two major record findings are distinct from the publication
provenance finding; tracking a finding is not the same as fixing it.

## Evidence and Preservation

The publication pass independently parsed official ENVO revision
`a2455d1a77e46bb8a664d65a157166b539269042` (106,817 triples). Both Volcanic
parents are active; ENVO:00001999 denotes a lentic marine water body, while
ENVO:00000094 denotes a volcano-associated physical feature. ENVO:00000063
has four exact synonyms and broad `hydrographic feature`, as the report says.
The inspected [NOAA volcanic pillow-mound account](https://oceanexplorer.noaa.gov/education/hydrothermal-vents-volcanoes/)
supports the physical-feature distinction, not an exact GOLD study crosswalk
or a universal microbial community.

`test_volcanic_exclusion_changes_only_context_parent_and_audit` builds the
whole corpus with and without only this exclusion. Membership is identical
and exactly one document changes. All other fields and old history are
equal: NARROW/SEEDED, skos:narrowMatch, 107 ORGANISM assertions, source path,
first node 3772 and two-node collapse note remain. The raw row separately
retains nodes 3772 and 4022. No ITEM identity decision was invented, and the
source-mapping endpoint issue #1398 is not solved by this correction.

## Generated Products

Full adapter comparisons cover all 3,206 records. Only Volcanic's semantic
text changes, by removing `broader habitat: marine water body`.

- Before JSONL SHA-256: `c66b09dd08c597c2bc2be8358cd0785b30e454858db374392966edf275a2ae45`
- After JSONL SHA-256: `aa2ed67aaa262ced0e3073b8d5e9cfba09cb826f352fefc14f28b814287887db`

The pinned Torch 2.14.0 runtime has no Intel macOS wheel. No dependency or
encoder contract was relaxed. A branch-scoped, read-only temporary workflow
used the existing locked Linux environment and prior verified cache:
[successful build 37529321455](https://github.com/CultureBotAI/HabitatMech/actions/runs/37529321455).
Its changed-record canary encoded one vector, then reused that vector without
encoding. A separate 32-record projection canary passed; the full embedding
pass reused all 3,206 entries, and actual PaCMAP regenerated the complete map.
The downloaded bundle passed local verification against independently
exported current inputs and its vector cache before import.

New immutable generation:
`6ba48e48fe26d1438bd148c972046de92c0b40ec4c7fd8c845d52aaf79430ee9`.
The temporary workflow is removed from the final PR diff. Old generations
remain intact. No checksum-only freshness patch or fabricated coordinates
were used. Site outputs are generated by the renderer, not hand-edited.

## Validation and Merge Conditions

Completed before this audit was written:

- Dry seed and forced exact canary, with the written YAML inspected.
- All 28 focused parent-exclusion tests.
- Target open schema and closed schema, zero errors.
- Exact corpus reproduction: 3,206 expected/found, zero missing/extra/differing.
- All 109 history records valid, including the attribution correction.
- OAK labels: 1,178 canonical, one synonym, five accepted exceptions;
  2,055 no-adapter skips, with no failing correspondence.
- Real map canary, full projection, local artifact/cache/input verification.

Full fresh `just qc` and site rendering were still running at audit creation;
their completion is not claimed here. Merge requires their successful
completion and successful final-head/merge-queue checks, with exact head and
check receipts recorded on the PR. No admin bypass or self-approval is part
of this workflow. Browser visual QA was not performed.

## Remaining Scope

An ignored-inclusive filesystem census finds 1,065 review files covering
1,064 distinct current records, with 2,142 of 3,206 records still unreviewed.
The all-record review remains unfinished. Water-body synonym scope (#1249),
source-mapping/SSSOM/KGX contract work (#1398), and original sample-level
provenance limitations remain explicit. This publication does not certify
SSSOM or KGX compatibility with current kg-microbe modeling.
