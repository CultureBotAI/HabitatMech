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

# Everything CI runs, in the order that fails cheapest-first
qc: lint test validate-all report
