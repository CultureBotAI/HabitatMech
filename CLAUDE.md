# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this repo is

A LinkML knowledge base of microbial habitats, harmonized from three source
vocabularies (JGI GOLD ecosystem paths, BacDive isolation sources, PREGO habitat
associations) onto ontology-grounded records. One YAML per habitat under
`data/habitats/<category>/<slug>.yaml`. See [README.md](README.md) for the
model and the current corpus numbers.

Sibling repos with the same conventions: TraitMech, CultureMech,
MediaIngredientMech, CommunityMech. Upstream pattern: monarch-initiative/dismech.

## Commands

```bash
just report            # corpus stats: grounding, categories, curation backlog
just validate-all      # closed-mode schema validation of every record
just verify-corpus     # check data/habitats/ is what data/raw/ produces
just test              # unit + corpus-integrity tests
just lint              # ruff
just render            # regenerate the browsable site under pages/
just qc                # lint + test + validate-all + verify-corpus + render-check + report
```

Re-seeding (only when upstream data changes):

```bash
just extract-inventory-dry     # free check: what extraction would produce
just extract-inventory         # refresh data/raw/ from a kg-microbe checkout
just seed                      # dry-run harmonization report, no writes
just seed-canary ENVO:00001998 # ONE record, end to end
just seed-apply --force        # rewrite the corpus
just seed-apply --force --prune  # ...and delete files left behind by a category move
```

## Rules that matter here

**Never write a record except through `write_validated_habitat`.** It runs
closed-schema validation and refuses to write on failure. A bare
`path.write_text(yaml.safe_dump(...))` bypasses the gate and will get caught by
`tests/test_write_validated.py` — after the bad data is already committed.

**Re-emitting any record must be byte-identical.** `test_write_validated.py`
enforces this over the whole corpus. It is what keeps a one-field bulk edit to a
one-field diff instead of 3,299 reflowed files. If you hand-edit a record into a
shape `safe_dump` would not emit, reformat it through the helper — do not
loosen the test.

**Re-extraction refuses when an upstream input has changed.** The extractor
compares each input's sha256 against `data/raw/MANIFEST.yaml` and stops before
reading anything if any differ, naming them. That is not paranoia: seven of the
eight inputs are *untracked* working-tree files in the kg-microbe checkout, so
its commit says nothing about their content, and a checkout sitting on a
different branch once swapped 16 mapping rows back to their pre-fix values and
reverted a merged PR with nothing failing — `verify-corpus` passes either way,
because the corpus faithfully reproduces from the newly-wrong `data/raw/`. Look
at what changed, then `--allow-drift` to take it, or `--mappings PATH` with
`--mappings-from` to pin the table while the checkout sits elsewhere (#72).

**A re-seed that retires a record needs a second pass.**
`data/habitats/RETIRED.tsv` maps URLs curation has retired to the records that
absorbed them, and `just redirects` rebuilds it from git history — so a page
deleted in the working tree is invisible to it until the deletion is committed.
The order is: `just seed-apply` → commit → `just redirects` → `just render` →
commit. CI runs `build_redirects.py --check` and fails if you skip it, which is
the point: a skipped pass means a published record URL now 404s (#54).

**`pages/` is generated too.** It is committed and served from the branch root,
so it goes stale exactly as records can. `just render` regenerates it and
`just render-check` (in CI) fails when it has drifted. Edit
`src/habitatmech/templates/`, never `pages/`.

**Never hand-edit a record.** `data/habitats/` is generated from `data/raw/`;
`just verify-corpus` compares them byte-for-byte and CI runs it. A change
that belongs in the corpus belongs in the seeder, or it is lost on the next
re-seed. (Once curation starts and records legitimately diverge, this gate
narrows to the seeder-owned fields — see issue #14.)

**Append a `CurationEvent` on every mutation**, via
`habitatmech.curate.curation_event.record_curation_event`.

**Canary before any bulk run.** `just seed-canary <IDENTIFIER>` writes exactly
one record. Verify the file is on disk and its content is right — not just the
exit code — before `seed-apply`.

**Never rename a record file directly.** `data/habitats/PATHS.tsv` pins each
identifier's slug; the seeder recreates the file under the pinned name, so a
hand rename leaves two files claiming one identifier. To rename, edit the slug
in `PATHS.tsv` and re-seed — that makes the rename an explicit, reviewable
one-line diff. `tests/test_corpus_integrity.py` fails on any disagreement.

**`mech_shared.yaml` is vendored byte-identical across the Mech repos.** Do not
edit this copy. `tests/test_schema.py` pins its sha256; changing it means
changing it upstream and re-vendoring everywhere, then updating the pin.

## Grounding: what not to "fix"

Several behaviours look like bugs and are deliberate. Read
`scripts/seed_from_sources.py`'s module docstring before changing any of them.

- **Ambiguous GOLD leaves are not grounded to the matched term.** When several
  paths end in "Sediment", only the shallowest claims `ENVO:00002007`; the rest
  get minted ids with `NARROW` grounding and the term as a parent. Grounding
  them all to the same term would merge marine, freshwater, and hot-spring
  sediment into one record with mixed attestations. Ties at the shallowest
  depth are left unclaimed on purpose — there is no principled winner.
- **BacDive sources with an empty upstream mapping stay UNGROUNDED.** That
  empty cell is a kg-microbe curator's decision, recorded with a reason. Do not
  re-ground it with a weaker lexical method.
- **Non-habitat mapping targets are `NOT_APPLICABLE`, not adopted.** "Acidic"
  maps to `PATO:0001429`; a quality is a property of a habitat, not a habitat.
  The link is kept as an xref.
- **Multi-term rows in the environment parameter table are skipped.**
  `sediment_marine_cold` is ENVO sediment *plus* PATO cold; attaching its
  parameters to plain sediment would misattribute them.
- **`assertion_count` is meaningless without `assertion_unit`.** GOLD counts
  organisms, BacDive strains, PREGO taxa. Never sum them across sources.

## Deep research

`just research <identifier>` runs deep-research-client against one novel term and
writes a report under `research/habitats/`. **The report is an input to a
curator, not a record.** Nothing reads it automatically, for the same reason
`data/raw/` is separate from `data/habitats/`: a model's prose is evidence to
weigh, and a definition written straight from an unread report is exactly the
plausible-sounding unverifiable claim `tests/test_decisions.py` exists to catch.

**Canary before any batch, and read the result.** A run costs money and takes
about ten minutes. The first canary here failed in 8 seconds because the
`cborg` route asks for `o3-deep-research-2025-06-26` and the CBORG key exposes
1,084 models with no deep-research model among them; the default is
`claude_code`, which needs no extra credential and whose defaults are read-only.

**Do not reach the client with `uv run --python 3.12`.** It requires Python
3.12 while this project still supports 3.10, and `uv run --python` tears down
and recreates the project's `.venv` as a side effect. The default launcher is an
isolated `uvx`, and `--client-command` takes the whole launcher as one string.

## Curation

**Curation is never a hand-edit to a record.** Records are generated and
`just verify-corpus` gates that they reproduce from `data/raw/`, so an edit is
silently reverted by the next re-seed. Decisions go in `curation/decisions.tsv`,
which the seeder reads as an input: `GROUND` / `GROUND_AS_PARENT` /
`NOT_APPLICABLE` / `CONFIRM_UNGROUNDED` / `REVIEW`, each keyed on the **minted
identifier of one source concept** (`just worklist` prints the key to use).

**`parent_habitats` means *broader*, so do not attach a term there unless it
is.** A term that is related to a concept but neither its identity nor broader
than it goes in the `relation` column as `xref` instead of the default
`parent`. This is not a formality: ENVO's *anthropogenic contamination feature*
asserts an anthropogenic origin and geographic feature-hood that BacDive's
474-strain "Contamination" category never claims, so both grounding it and
parenting it publish the same over-claim, one as identity and one as an is-a
(#99). `relation: xref` keeps the link upstream saw without this repo asserting
one.

**A host's PARTS ground to the anatomy term; the WHOLE host organism does not.**
This is the line that decides every organism-as-habitat case, and getting it
wrong twice is what #114 and #112 cost. `gut`, `skin`, `lung` and `blood` are
parts, and grounding a habitat to them is right and routine. `Mollusca`,
`Porifera`, `larva`, `pupa` and `embryo` are the whole organism — as a clade or
at a life stage — and those keep their own minted identity, carry the organism
term as `relation: xref`, and want an `<X>-associated environment` term instead.
A `cocoon` is a structure an insect builds rather than the insect, so it grounds
normally. Applying the rule to the term's ontology rather than to what it
denotes is the mistake: UBERON holds both `skin of body` and `larva`.

**An organism acting as a host IS a habitat; the taxon term is not.** These are
two different claims and conflating them cost 4,920 assertions. "A host taxon is
not a habitat" was recorded on 24 records — Mollusca, Porifera, Fungi, Bovinae,
Protozoa — as `NOT_APPLICABLE`, while the identical concept was treated as a
habitat for Sponge, Nematoda, Reptilia, Mammals and Birds. `Host-associated >
Porifera` was NOT_APPLICABLE while its own child `Porifera > Sponge` was a term
request (#114).

A host is where the microbe lives, and ENVO models exactly this at
plant-associated, animal-associated and fungi-associated environment. What is
not a place is the *taxon term* — a phylum is a class of organisms. So the
taxon goes in `relation: xref` and the concept keeps its own identity as a
term-request candidate. `NOT_APPLICABLE` says the concept is not a habitat,
which is a stronger and different claim: reserve it for diseases, qualities,
processes and procedures. `tests/test_decisions.py` fails on a NOT_APPLICABLE
whose target is an organism term.

**A note's claims are checked too.** `notes` is the only record of *why* a
decision was made and is most of what an LLM-assisted pass produces, so a
plausible-sounding citation is as hard to spot as a plausible-looking CURIE was
before #39. `tests/test_decisions.py` verifies the three claims a note can make
against the repo: a `Path:` must match the concept's own canonical path, any
term id must exist in the vendored slice, and a label quoted next to an id must
be that term's label (#51).

Every `GROUND` names both the target CURIE and the label it expects, and the
seed fails unless the term exists in the vendored slice *and* the label matches.
Do not weaken that check — it is the only thing standing between an
LLM-assisted curation pass and a plausible-looking wrong term ID in the corpus.
If a target is not in the slice, vendor the ontology (see #10); do not remove
the check.

A merged record reaches `REVIEWED` only when **every** source concept feeding it
is decided. A partially-curated record staying `SEEDED` is the rule working, not
a bug — `just worklist` and the report show which co-attestor is missing.

`mapping_status: SEEDED` means machine-generated and unreviewed — currently
3,229 of 3,284 records.

When adding `causal_graphs`, every edge needs `evidence` with a real citation.
That is enforced by the schema and re-checked corpus-wide in
`tests/test_corpus_integrity.py`, because mechanism claims are the one thing in
this repo that no upstream source vouches for.

`just report` ends with the ungrounded records ranked by upstream assertion
volume. That is the curation backlog, highest-yield first.

## Git workflow

Branch before the first edit, open a PR for every change including docs-only
ones, review the diff as a separate adversarial pass, file findings as issues,
and delete the branch after merge. Do not merge without explicit approval.
