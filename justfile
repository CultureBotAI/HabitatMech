# HabitatMech — microbial habitat knowledge base harmonized from GOLD/BacDive/PREGO

set positional-arguments := true

schema := "src/habitatmech/schema/habitatmech.yaml"
habitats := "data/habitats"

default:
    @just --list --unsorted

# Install package + dev tools
install:
    uv sync --extra dev

# Generate Pydantic classes from the LinkML schema
gen-schema:
    uv run gen-pydantic {{schema}} > src/habitatmech/schema/habitatmech_dataclasses.py

# Re-extract the data/raw/ inventories from a local kg-microbe checkout.
# Only needed when kg-microbe's sources change — the inventories are committed,
# so seeding, validation and tests all run without kg-microbe present.
# Set KG_MICROBE_ROOT or edit conf/sources.yaml to point at the checkout.
extract-inventory *args:
    uv run python scripts/extract_source_inventory.py {{args}}

# Show what extraction would produce, without writing (free check before the real run)
extract-inventory-dry:
    uv run python scripts/extract_source_inventory.py --dry-run

# Dry-run the seed: harmonize the inventories and report the concept counts
# that WOULD be written, per category and grounding status. No files touched.
seed:
    uv run python scripts/seed_from_sources.py

# Seed exactly one record end to end and validate it — the canary to run
# before any bulk write. `just seed-canary ENVO:00000019`
seed-canary *args:
    uv run python scripts/seed_from_sources.py --apply --only "$@"

# Write every habitat record under data/habitats/<category>/<slug>.yaml.
# Run `just seed` and `just seed-canary` first.
seed-apply *args:
    uv run python scripts/seed_from_sources.py --apply {{args}}

# Validate a single habitat YAML against the schema
validate file:
    uv run linkml-validate -s {{schema}} --target-class HabitatRecord {{file}}

# Validate every record. Delegates to validate-strict (closed mode: unknown
# fields are errors, not silently accepted as they are in linkml-validate's
# default open mode).
validate-all *args:
    @just validate-strict {{args}}

# Strict in-process validation in closed mode. Emits
# reports/instance_validation_failures.tsv and exits 1 on any ERROR.
validate-strict *args:
    uv run python scripts/validate_strict.py {{args}}

# The curation backlog, ranked by upstream assertion volume, with the minted
# identifier each decision must key on and lexically-near candidate terms.
# Suggestions are a starting point, never an answer — anything written into
# curation/decisions.tsv is re-verified against the ontology slice at seed time.
worklist *args:
    uv run python scripts/curation_worklist.py {{args}}

# Verify data/habitats/ is exactly what data/raw/ produces. Schema validation
# checks each record's shape but not its content, so without this a hand-edited
# or drifted record passes every other check.
verify-corpus *args:
    uv run python scripts/verify_corpus.py {{args}}

# Render the browsable site under pages/ from the corpus. Committed and served
# from the branch root, so it can go stale exactly as records can; `--check`
# fails when it has.
render *args:
    uv run python scripts/render_pages.py {{args}}

# Draw a reproducible sample of a grounding population, to estimate its error
# rate when the slice is too big to read and too uniform to screen.
# `just sample --grounding EXACT --size 40 --found 2`
sample *args:
    uv run python scripts/sample_groundings.py {{args}}

# Rebuild data/habitats/RETIRED.tsv — the map from record URLs curation has
# retired to the records that absorbed them. A record page is named after its
# label and identifier, so improving either moves the URL; the map is what keeps
# the old address resolving instead of 404ing.
redirects *args:
    uv run python scripts/build_redirects.py {{args}}

# Fail if RETIRED.tsv is out of date with git history
redirects-check:
    uv run python scripts/build_redirects.py --check

# Corpus report: records per category, grounding-status breakdown, source
# coverage, and the multi-source corroboration counts.
report *args:
    uv run python scripts/habitat_report.py {{args}}

# Run the test suite
test *args:
    uv run pytest {{args}}

# Lint
lint *args:
    uv run ruff check {{args}} .

# Auto-fix lint findings
lint-fix:
    uv run ruff check --fix .

# The authoritative quality gate used both locally and in CI.
qc:
    uv run python scripts/run_qc.py

# Refresh the generated current-corpus block in README.md.
docs-stats:
    uv run python scripts/check_docs.py --write

# Fail if README.md's current-corpus block is out of step with the corpus.
docs-check:
    uv run python scripts/check_docs.py --check

# Verify every committed raw TSV is covered by a manifest and matches it.
provenance-check:
    uv run python scripts/check_provenance.py

# Fail if pages/ is out of step with the corpus
render-check:
    uv run python scripts/render_pages.py --check

# Which novel terms still need a definition, ranked by upstream volume
research-worklist:
    uv run python -c "import sys; sys.path.insert(0,'scripts'); \
    from research_habitat import undefined_novel_terms; \
    w=undefined_novel_terms(); print(f'{len(w)} novel terms need a definition'); \
    [print(f'{v:7d}  {l[:34]:34s} {i}') for v,l,i in w[:25]]"

# Free check: print the provider command for one record without calling it
research-dry IDENTIFIER:
    uv run python scripts/research_habitat.py --identifier {{IDENTIFIER}} --dry-run

# Research ONE novel term. Costs a real provider call and takes ~10 minutes.
# Run this before any batch and read the result: the first canary failed in 8
# seconds because the cborg route wanted a model the key does not expose.
research IDENTIFIER *args:
    uv run python scripts/research_habitat.py --identifier {{IDENTIFIER}} {{args}}

# Rebuild the ENVO batch term-request table from curation/term_requests.tsv
term-requests:
    uv run python scripts/build_term_requests.py

# Fail if the committed term-request table is out of step with the corpus
term-requests-check:
    uv run python scripts/build_term_requests.py --check
