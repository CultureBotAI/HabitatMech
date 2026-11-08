# Native EdgeMech assertion adapter

The package module `habitatmech.edge_curation` exports immutable Git-committed
`curation/decisions.tsv` rows as canonical native assertions. It preserves complete
selected rows, file hashes, source positions, source commit and native scope.
No generated records are edited and no independent scientific review or KG
occurrence approval is created.

Exact organism/taxon source observations, aggregate-to-row evidence bindings and reviewed SKOS projections are not supplied by the native decision table. A complete eligible-overlap result must report this scope limitation; zero matched native predicates is not evidence of no biological overlap.

The optional shared contract source is pinned at CLAW commit
`1b5391d083ba85ac94e5279c3cba25ac4fde243c`. Use an explicit checkout of that
revision on PYTHONPATH alongside this repository's src directory, and run
`scripts/adhoc/check_edge_contract_pin_20261107.py --claw-root PATH`.
The dedicated CI integration tier makes a missing shared dependency an error
with `REQUIRE_EDGE_CONTRACT=1`; ordinary native tests may skip this optional
integration when CLAW is absent.

Run one real unit first through the same module, shell and environment:

```bash
python -m habitatmech.edge_curation --root . --source-commit FULL_NATIVE_COMMIT --positions 1 --output build/edge-curation/canary
```

Verify the persisted assertions.jsonl and manifest.json, counts and hashes.
Then replace `--positions 1` with `--all` and select a new output directory for
the complete declared native surface. Output streams into a staging directory;
the destination is reserved exclusively and the manifest is published last
after the payload is complete. Files and directories are synced; consumers
ignore incomplete destinations without a manifest.
Existing destinations are never overwritten. Keep analytical outputs in
ignored build/; there is no per-row GitHub record or Pages publication.
