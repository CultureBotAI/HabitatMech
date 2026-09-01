# Model-assisted habitat research

Research reports help curators define novel habitat concepts. They are not
trusted inputs to the seeder and are never applied to records automatically.

## Workflow

```bash
just research-worklist
just research-dry <IDENTIFIER>
just research <IDENTIFIER>
```

The dry run prints the provider command without making a paid call. Run one
real canary, read the complete result, and verify its citations before starting
a batch. A typical call can take several minutes and may incur provider cost.

Reports are written beneath `research/habitats/`. The durable batch manifest at
`reports/habitat_research_manifest.tsv` records what was attempted, elapsed time,
output size and failures, because reproducing that history would require paying
for the calls again.

Definitions, broader terms and citations from a report require curator review
and an explicit curation decision. Plausible prose is not evidence by itself.
Use `scripts/check_report_citations.py` as a screen, then inspect the underlying
sources.

## Client isolation

The research client requires Python 3.12 or newer while HabitatMech supports an
older project floor. The default launcher therefore uses an isolated `uvx`
environment. Do not invoke it with `uv run --python 3.12`, which can recreate
the project virtual environment. `--client-command` accepts the complete
launcher as one string.

The default `claude_code` route needs no additional repository credential and
runs read-only. Provider-specific credentials belong in the environment and
must never be committed.

Native Codex and OpenScientist are documented in
`docs/DEEP_RESEARCH_PROVIDERS.md`. Use `--provider codex` for the native,
schema-validated Codex lane and `--provider openscientist` for the isolated
deep-research-client lane. Run `just deep-research-canary <provider>` before a
real one-record canary.

## Troubleshooting history

The original CBORG canary failed immediately because that route requested
`o3-deep-research-2025-06-26` while the available model catalog exposed no
deep-research model. This is an environment/provider mismatch, not a corpus
failure. Re-run `just research-dry`, inspect the current provider configuration,
and canary again rather than changing record-generation code.
