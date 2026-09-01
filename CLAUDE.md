# CLAUDE.md

Operational guidance for Claude Code and other editing agents in this repository.

## Repository purpose

HabitatMech is a LinkML knowledge base of microbial habitats harmonized from
JGI GOLD, BacDive, PREGO and Madin et al. One generated YAML record lives under
`data/habitats/<category>/<slug>.yaml` for each resolved habitat. The committed
inventories in `data/raw/` are the reproducible inputs.

Read these before changing domain behavior:

- [README.md](README.md) — public model and generated current statistics.
- [docs/HARMONIZATION.md](docs/HARMONIZATION.md) — identity, merging and seeding design.
- [docs/CURATION.md](docs/CURATION.md) — decision semantics and habitat rules.
- [docs/RESEARCH.md](docs/RESEARCH.md) — model-assisted definition research.

Sibling repositories use similar conventions: TraitMech, CultureMech,
MediaIngredientMech and CommunityMech. The upstream pattern is
monarch-initiative/dismech.

## Authoritative commands

```bash
just qc                # every local and CI quality gate
just report            # current corpus, grounding and curation statistics
just test              # unit and corpus-integrity tests
just validate-all      # closed-schema validation of every record
just verify-corpus     # prove data/habitats reproduces from its inputs
just render            # regenerate the committed site under pages/
just docs-stats        # refresh the generated README statistics block
```

`just qc` is authoritative. It runs lint, documentation consistency, tests,
closed-schema validation, corpus reproduction, generated-site, redirect and
term-request checks, then the corpus report. CI invokes the same runner.

For an upstream refresh:

```bash
just extract-inventory-dry
just extract-inventory
just seed
just seed-canary ENVO:00001998
just seed-apply --force
just seed-apply --force --prune  # only when stale category files should be removed
```

## Generated-file boundaries

**Never hand-edit a habitat record.** `data/habitats/` is generated from the
committed inventories plus curation decisions. Put source harmonization changes
in the extractor or seeder and curator decisions in `curation/decisions.tsv`.
`just verify-corpus` rejects drift.

**Never write a record except through `write_validated_habitat`.** It performs
closed-schema validation before writing. Every mutation must also append a
`CurationEvent` with
`habitatmech.curate.curation_event.record_curation_event`.

**Re-emitting an unchanged record must be byte-identical.** Preserve the YAML
emission contract enforced by `tests/test_write_validated.py`; do not loosen the
test to accommodate a new serializer shape.

**Edit site templates, not `pages/`.** Change `src/habitatmech/templates/`, run
`just render`, and commit the regenerated pages. `pages/` is published and
checked byte-for-byte.

**Do not edit `src/habitatmech/schema/mech_shared.yaml` here.** It is vendored
byte-identically across the Mech repositories and sha-pinned by the schema tests.

## Safe corpus workflow

**Canary before a bulk write.** Run `just seed`, then `just seed-canary
<IDENTIFIER>`. Inspect the written file, not only the exit code, before a full
`seed-apply`.

**Never rename a record file directly.** Change the identifier-to-slug entry in
`data/habitats/PATHS.tsv` and re-seed. Slugs are corpus-wide and the integrity
tests reject duplicates and path disagreement.

**Treat extractor drift as evidence to inspect.** Re-extraction compares
upstream bytes with `data/raw/MANIFEST.yaml`. Investigate a mismatch before using
`--allow-drift`; a different upstream checkout can reproduce a consistently
wrong corpus just as faithfully as a correct one.

`data/raw/GOLD_MANIFEST.yaml` separately covers inventories derived from the
GOLD bulk export and API. Run `just provenance-check` after changing any raw
inventory; large sources and credentials remain uncommitted.

**Resolve a merge by class, never in bulk.** A merge into a curation branch
conflicts in two kinds of file at once, and they take opposite treatments.
Generated artifacts — `README.md`, `pages/`, `data/habitats/`, `RETIRED.tsv`,
`curation/term_requests/` — take either side and are then *regenerated*; hand
merging an output is meaningless. Curation inputs — `curation/decisions.tsv`,
`term_requests.tsv`, `term_requests_excluded.tsv`, `redirects_retracted.tsv` —
carry rows that exist nowhere else and must be resolved by hand, then staged
immediately. Never run a blanket `git checkout --ours/--theirs` across a mixed
conflict set: it reaches the inputs too, and an input that loses rows still
reproduces a corpus that is internally consistent, in step with its site, and
green under `just qc` (#219). `just curation-floor` is the check that catches it.

**Retired URLs require a post-commit pass.** A deleted working-tree page is not
visible to the history-based redirect builder until committed. The sequence is:

1. seed and commit the corpus change;
2. run `just redirects` and `just render`;
3. commit the redirect and site updates.

Do not prune on partial `--only` or `--limit` runs.

**Retracting a published redirect needs a decision row, not a deletion.** The
builder reads the committed map, so a row deleted from the working tree comes
straight back. Record it in `curation/redirects_retracted.tsv` with a curator
and a reason, then rebuild. See [docs/CURATION.md](docs/CURATION.md).

## Semantic invariants

Read the module docstring in `src/habitatmech/seed.py` before changing a
grounding route.

- Ambiguous GOLD leaves do not all claim the same ontology identity. Only the
  defensible claimant grounds directly; narrower paths keep minted identities
  and the ontology term as a broader parent.
- An empty BacDive upstream mapping is a curator decision and remains
  `UNGROUNDED`; do not replace it with a weaker lexical guess.
- A mapping to a quality, chemical, disease, process or procedure is not a
  habitat identity. Preserve relevant links as xrefs and use
  `NOT_APPLICABLE` only when the source concept itself is not a habitat.
- `parent_habitats` means strictly broader. A related term that is not broader
  belongs in an xref relation. Four things contribute a parent — ontology
  subclass parents, the GOLD parent-path link, the ambiguous-leaf rule, and the
  genus of a curated definition in `curation/term_requests.tsv` — so
  `decisions.tsv` is not the whole audit trail for a parent claim. The
  strictly-broader rule binds all four.
- A host organism is a microbial habitat, but its taxon or whole-organism term
  is not the habitat identity. Keep the source concept minted, use the organism
  term as an xref, and request an associated-environment term where appropriate.
  Anatomical host parts such as gut, skin and blood ground normally.
- MIxS environmental-triad slots have different roles: broad scale is an
  ecosystem, local scale may be an anatomical site, and medium is the sampled
  material. Do not adopt a triad term as identity merely because it is present.
- `assertion_count` is interpretable only with `assertion_unit`; counts from
  different sources use different units and must not be summed.
- Multi-term environmental-parameter rows are not attached to a record for only
  one component.
- Every causal-graph edge needs real cited evidence.

## Curation and research

Curation decisions are keyed by the minted identifier of one source concept.
Every grounding target and claimed label is checked against the vendored
ontology slice. A multi-source record becomes `REVIEWED` only when every source
concept feeding it has an item-level decision. See
[docs/CURATION.md](docs/CURATION.md) for the decision table and examples.

Deep-research reports under `research/habitats/` are evidence for a curator,
never automatic record input. Canary a paid run and read the report before any
batch. See [docs/RESEARCH.md](docs/RESEARCH.md).

## Git workflow

Branch before the first edit. Open a PR for every change, including docs-only
changes. Review the diff as a separate adversarial pass and file findings as
issues. Do not merge without explicit approval. Delete branches after merge.
