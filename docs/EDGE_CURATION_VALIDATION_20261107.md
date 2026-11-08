This adds a native EdgeMech adapter for HabitatMech's authoritative curation
decision table. Complete rows, source positions, source commit and native
review depth remain bound to immutable file hashes. Explicit ITEM decisions
retain their native action predicate; no SKOS or biological edge projection is
invented. Other native states remain unassessed.

The shared source pin is CLAW `1b5391d083ba85ac94e5279c3cba25ac4fde243c`
(prerequisite CLAW PR #953). A dedicated integration workflow verifies that
pin and requires the feature tests. This implements the HabitatMech slice of
[CLAW #767](https://github.com/CultureBotAI/culturebotai-claw/issues/767).

Validation on 2026-11-07:

- 16 focused tests passed in mandatory shared-contract mode, including
  valid-row reversal/duplication during the real exporter readback, exclusive
  publication collision, interrupted publication and directory sync checks.
- Ruff passed for the new adapter, publisher, tests and pin checker.
- A real position-11 canary and full export used the same module launcher,
  pinned environment and publication path, reading native commit
  `3b232e8a50ac434e4c1131edc43fb39ba0af10e3`.
- The full table contains 1,831 assertions: 424 inherit review of the exact
  native ITEM decision; 1,407 remain unassessed curation states. Zero new
  scientific reviews or KG occurrence approvals were produced.
- Exact persisted bytes, ordered assertion identity/source-position
  membership and status counters were reconciled before manifest-last
  publication. Files and directories were synced and artifacts checked on disk.

| Export under `build/edge-curation-20261107/` | Rows | JSONL bytes | Manifest SHA256 | JSONL SHA256 |
|---|---:|---:|---|---|
| `canary-verified` | 1 | 6,594 | `a185f7d0b0948b3e2e42713279f0c2bc6880bf49b55818b2eecf4b06525b701d` | `01276eacaf2767d5121816e740920df0c297b6110dbba469fc6571816133b2d1` |
| `full-verified` | 1,831 | 7,911,812 | `484e037facef2e3f4edff792c5acfd52ac932a46b4af321f8526aca40e17d4c4` | `fed100eeadd35bf114167c5ba07bad67c3493e6fc6c629cec917a70143867e56` |

Run `python -m habitatmech.edge_curation --root . --source-commit COMMIT`
with `--positions 11` or `--all` and a new `--output` directory to reproduce.
The analytical payloads stay outside Git; the retained module and pin checker
provide the implementation and environment provenance.

Independent read-only review filed #2312 for the persisted verification gap.
The repaired implementation and mutation tests passed independent reinspection;
the corrected canary was independently checked on disk. Fixes #2312.
The shared publication repairs also cover the failure modes recorded in
MediaIngredientMech #1145 and #1146.

Issue #2311 remains open for exact organism/taxon observations, native evidence
ancestry and reviewed cross-schema projections. Counts, characteristic taxa,
preferences and causal mechanisms are explicitly outside this adapter's
curation-decision surface; no overlap conclusion may erase that limitation.
