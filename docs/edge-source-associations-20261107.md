# Native source-association expansion

This advances [#2311](https://github.com/CultureBotAI/HabitatMech/issues/2311)
with complete exports of the committed BacDive, PREGO and Madin selected
association inventories. It does not supply the missing exact association
reviews or authorize a KG predicate projection. The issue remains open for
that scientific evidence and projection work.

`habitatmech.edge_observations` reads immutable source commit
`3b232e8a50ac434e4c1131edc43fb39ba0af10e3` and uses shared contract commit
`1b5391d083ba85ac94e5279c3cba25ac4fde243c` (CLAW PR #962). The existing native
decision exporter and its `full-verified` artifacts remain unchanged.

Each new assertion binds the complete selected source row, exact source owner
row, source-file hashes, native manifest, schema, curation/harmonization rules
and extractor. Source concepts remain unprojected. The native slot predicate
`habitatmech:characteristic_taxa` is transported with explicit association-only
scope: characteristicness, habitat preference, growth, negative observations
and causality are not inferred. All new assertions are **unassessed**.

BacDive counts retain STRAIN units while owner candidate pools count taxa.
PREGO scores, ranking, direct flags and channels remain lexical source values.
Madin's corroboration-first selected subset has no invented score or ranking.
The native inventories can omit upstream candidates; a selected-inventory
export is not a census of the original upstream sources. Original primary
source bytes have not been fetched or reverified, and BacDive aggregate counts
do not identify the contributing individual strains.

## Validation and publication

The independent read-only review found no blocking issue. Mandatory native
contract tests passed: **28 tests**, including lossless owner/source binding,
review isolation, real serial/spawn byte identity, worker failure without
publication, malformed unselected inputs and valid-line reorder/duplication
rejection. Ruff passed. The previously reviewed durable manifest-last
publisher is unchanged.

All three free full-source preflights passed. Each surface then used one real
source-row canary with four workers. Persisted JSONL and manifest hashes,
nonzero sizes, one-row counters and unassessed status were checked independently
before full exports. Full exports used the same module, nonlogin Bash shell,
Python environment, source pin and four-worker mode. Every generated envelope
was validated; exact persisted bytes and ordered membership were reconciled
before atomic manifest publication. These checks establish transport and
persistence, not biological approval or current KG occurrence compatibility.

## Persisted receipts

Paths are relative to this worktree's
`build/edge-curation-20261107/observations-v1/`. Existing destinations are never
overwritten. Every output reports zero independent scientific reviews and zero
approved KG occurrences.

| Directory | Rows | JSONL bytes | Manifest SHA-256 |
| --- | ---: | ---: | --- |
| `bacdive-canary` | 1 | 5,869 | `155742a8f807502c20bfad000fbb4190d0435b0b05fc3363af73c03dab1ee846` |
| `prego-canary` | 1 | 5,998 | `d3f2e4eedf9bada324283120fcb3cb6ffd1878eded4ccbbbfeb2e8138f19e302` |
| `madin-canary` | 1 | 5,697 | `0da75e6cf1a4102f1df4f33640eac6bc4dfb1ffc8d3c7a80d5271d3737697c5f` |
| `bacdive-full` | 3,081 | 18,250,331 | `56ec544212a597670bbaa10e876dce0abd8771172319afb3686affc55e02cd81` |
| `prego-full` | 8,807 | 52,830,916 | `2955d0c6b5e2d7435c419303d86a9d2208cebd00bf4cc4c7551c1d135479af14` |
| `madin-full` | 1,378 | 7,883,998 | `dadf1f1f6a0a6eaf2ff6150d833c83d4c1bfb70bb70ed9504ed5604937ef91a3` |

| Directory | Assertions SHA-256 |
| --- | --- |
| `bacdive-canary` | `4e082f8e1451bf8655e83c89e4929828a259c08a6dad06493117079831da85a0` |
| `prego-canary` | `7c22bf831d96c766ab8a4436ecbaa05161dc26bf9a166bea1f590decf038b426` |
| `madin-canary` | `35de382cf11224b7ece6daed7177fef3bfc18711eee8028e265a5c723ad07ca7` |
| `bacdive-full` | `ce6818181deb7338c985706c5c93f81b6510ac95125c4364914cc84e3dfd3ba1` |
| `prego-full` | `84e603a585f8c7bf36b380cd47360ea55144bdd7b8c70a49252b9037b970965a` |
| `madin-full` | `4613ce2182fc61b632a3f965fc86d3a694a2925f319948a594a2dd0b21cc8f4f` |

## Reproduction

Use a fresh destination and the exact CLAW source pin above on `PYTHONPATH`.
The actual Python executable was the adjacent
`culturebotai-claw-edgemech-20261107/.venv/bin/python`; source paths were this
worktree's `src` and the detached
`culturebotai-claw-edgemech-contract-1b5391d/src`. No provider or credentials are
required. The module itself is the retained launcher and provenance source.

```bash
python -m habitatmech.edge_observations --root . \
  --source-commit 3b232e8a50ac434e4c1131edc43fb39ba0af10e3 \
  --surface bacdive --workers 4 --all --plan \
  --output build/edge-curation-20261107/observations-v1/bacdive-full
```

For each surface (`bacdive`, `prego`, `madin`), run `--positions 1` to a new
canary destination, inspect persisted files, then use `--all` without `--plan`
to a new full destination. The recorded outputs above already exist; choose
new versioned paths when repeating validation.
