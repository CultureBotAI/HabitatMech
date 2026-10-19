---
name: add-record
description: "Add, mint, un-merge, or define a HabitatMech microbial habitat record using web search, scientific literature, ontology lookups, and authoritative curation tables without hand-editing generated YAML."
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Edit, Write
metadata:
  category: curation
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Add a HabitatMech microbial habitat record

Use this skill when asked to add, mint, split, or define microbial habitat
records in HabitatMech using web search, primary scientific literature, and
ontology evidence. Follow the complete workflow in
[../add-yaml-record/SKILL.md](../add-yaml-record/SKILL.md).

## Quick reference

1. **Never hand-edit `data/habitats/` or `pages/`.** All records are emitted by
   `src/habitatmech/seed.py` from `data/raw/*.tsv` and `curation/*.tsv`.
2. **Un-merge conflated source concepts** in `curation/decisions.tsv`
   (`CONFIRM_UNGROUNDED` or `GROUND_AS_PARENT` at `review_depth: ITEM`) to mint
   standalone YAML records in `data/habitats/<category>/<slug>.yaml`.
3. **Author native HabitatMech microbial habitat definitions** in
   `curation/term_requests.tsv` (`definition_source: HabitatMech`) with a
   verified ontology genus (`proposed_parent_id` in `data/raw/ontology_terms.tsv`),
   explicit `parent_mode` (`ADD` or `REPLACE`), and literature-backed
   genus-differentia definitions ending in `.`.
4. **Exclude ambiguous renamed source labels** in
   `curation/definition_source_label_exclusions.tsv` and context-only GOLD
   parents in `curation/gold_parent_exclusions.tsv` when needed.
5. **Regenerate and verify** with `scripts/seed_from_sources.py --apply --force --prune`,
   `scripts/build_term_requests.py`, `scripts/build_redirects.py`,
   `scripts/render_pages.py`, `scripts/check_docs.py --write`, and
   `scripts/run_qc.py`.
