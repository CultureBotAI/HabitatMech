---
name: add-yaml-record
description: "Add, mint, un-merge, or author a HabitatMech microbial habitat record using web search, scientific literature, ontology lookups, and authoritative curation inputs without hand-editing generated YAML."
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Edit, Write
metadata:
  category: curation
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Add or author a HabitatMech microbial habitat record

Add a standalone generated YAML habitat record (`data/habitats/<category>/<slug>.yaml`),
author a native HabitatMech microbial habitat definition (`curation/term_requests.tsv`),
or ground an uncurated habitat concept through HabitatMech's seeder-first
architecture, backed by inspected primary scientific literature and verified
ontology slices.

## Architectural contract

1. **Seeder-first reproduction (`just verify-corpus`).** Never create or edit a
   file under `data/habitats/` or `pages/` by hand. Every habitat record is
   deterministically emitted by `src/habitatmech/seed.py` from the sha-locked
   source inventories in `data/raw/*.tsv` plus the authoritative curation inputs
   in `curation/`.
2. **Inventory provenance lock (`just provenance-check`).** The raw source
   inventories (`data/raw/gold_paths.tsv`, `data/raw/bacdive_tags.tsv`,
   `data/raw/prego_terms.tsv`, `data/raw/madin_isolation_sources.tsv`,
   `data/raw/environments_table.tsv`, and `data/raw/ontology_terms.tsv`) are
   sha256- and row-count-locked in `data/raw/MANIFEST.yaml` and
   `data/raw/GOLD_MANIFEST.yaml`. Every minted habitat record must trace to at
   least one source concept (`^habitatmech:(GOLD|BACDIVE|PREGO|MADIN|ENVIRONMENTS_TABLE)\.[0-9a-f]{10}$`).
3. **Three authoritative ways to add or define a microbial habitat in HabitatMech:**
   - **Mechanism A — Un-merge a conflated source concept into a standalone minted YAML record (`curation/decisions.tsv`).**
     When a source concept was merged into a broader or cross-domain ontology
     record (via lexical matching or a prior `GROUND` decision), changing its
     row in `curation/decisions.tsv` to `CONFIRM_UNGROUNDED` or
     `GROUND_AS_PARENT` (at `review_depth: ITEM`) mints a new standalone YAML
     record under `data/habitats/<category>/<slug>.yaml` and registers its slug
     in `data/habitats/PATHS.tsv` on regeneration.
   - **Mechanism B — Author a native HabitatMech microbial habitat definition (`curation/term_requests.tsv` + `curation/decisions.tsv`).**
     HabitatMech supersedes ENVO for microbial habitats that lack an ontology
     class. For any `CONFIRM_UNGROUNDED` (`review_depth: ITEM`) record, adding
     a row in `curation/term_requests.tsv` supplies its canonical `label`,
     Aristotelian genus-differentia `definition` (`definition_source: HabitatMech`),
     strictly broader `parent_habitats` (`parent_mode: ADD` or `REPLACE`), and
     curated synonyms (`exact_synonyms`, `narrow_synonyms`, `broad_synonyms`),
     while compiling `curation/term_requests/envo_robot_template.tsv`.
   - **Mechanism C — Ground an uncurated or `CLASS`-swept habitat to a distinct ontology identity (`curation/decisions.tsv`) or enrich its causal graph (`curation/causal_graphs/<slug>.yaml`).**
     When a source concept has an exact identity in `data/raw/ontology_terms.tsv`
     that was left ungrounded or `CLASS`-swept, setting `decision: GROUND` with
     `review_depth: ITEM` resolves it to that ontology term (creating a new
     ontology-keyed YAML record if no other concept already claimed that CURIE).
     Literature-backed ecological mechanisms are added as overlays in
     `curation/causal_graphs/<slug>.yaml`.

## Workflow

### Step 1. Discover candidates and inspect existing state

Use `just worklist`, `just report`, or targeted searches across
`curation/decisions.tsv`, `curation/term_requests.tsv`,
`curation/term_requests_excluded.tsv`, and `data/habitats/PATHS.tsv` to identify:

- Ungrounded source concepts at `review_depth: CLASS` or `ITEM` that lack a
  curated HabitatMech definition in `curation/term_requests.tsv`;
- Source concepts conflated under a broader, homonymous, or cross-host ontology
  record that should be split into standalone minted records; or
- Source concepts whose exact or broader ontology target exists in
  `data/raw/ontology_terms.tsv`.

Before changing any record, check:

```bash
rg --no-ignore --hidden "<identifier-or-slug>" curation/ reports/ reviews/ history/
```

Respect prior review dispositions in `reports/yaml_record_review/` and
`reviews/structured/`, and never regress existing curation-floor invariants
(`scripts/check_curation_floor.py`).

### Step 2. Perform web, literature, and ontology research

1. **Inspect primary source context.** Read the full GOLD 5-tuple path,
   MIxS triad slots (`env_broad_scale`, `env_local_scale`, `env_medium`),
   sample assertions, BacDive keywords, PREGO text-mined/metadata channels, or
   Madin isolation sources feeding the concept.
2. **Verify ontology candidates against `data/raw/ontology_terms.tsv`.**
   - A `GROUND` or `GROUND_AS_PARENT` target must exist in
     `data/raw/ontology_terms.tsv` with `label_only != TRUE`.
   - Confirm the target is not a whole organism/taxon (`ORGANISM_TERMS` or
     `ORGANISM_ROOTS` in `src/habitatmech/seed.py`), biological process
     (`ENVO:02500000` subtree), quality (`PATO:*`), chemical (`CHEBI:*`), or
     disease (`MONDO:*`, `DOID:*`).
   - External ontology terms not in `data/raw/ontology_terms.tsv` may only be
     attached as `relation: xref` alongside `CONFIRM_UNGROUNDED` or
     `NOT_APPLICABLE`, with their exact canonical label registered in
     `curation/external_xrefs.tsv`.
3. **Search primary scientific literature and authoritative references.**
   Use `WebSearch` and `WebFetch` (PubMed/PMC, DOI resolution, OLS/Ontobee,
   peer-reviewed microbial ecology literature) to establish:
   - What physical, chemical, anatomical, or engineered environment the source
     concept denotes;
   - Its strictly broader habitat genus (for `GROUND_AS_PARENT` or
     `proposed_parent_id` in `curation/term_requests.tsv`);
   - The distinguishing physicochemical, structural, or host-context
     differentia that separate it from sibling habitats; and
   - Verified PMIDs/DOIs when authoring causal graphs (`curation/causal_graphs/<slug>.yaml`)
     or citing evidence in curation notes.

### Step 3. Update authoritative curation tables

#### A. `curation/decisions.tsv`

Columns:
`identifier`, `decision`, `object_id`, `object_label`, `grounding_status`,
`curator`, `date`, `notes`, `review_depth`, `category`, `relation`

- Always use `review_depth: ITEM` when curating an individual concept.
- Use `GROUND` (`grounding_status: EXACT`, `relation: exact`) only when the
  ontology class is coterminous with the microbial habitat concept.
- Use `GROUND_AS_PARENT` (`grounding_status: NARROW`, `relation: parent`) when
  the ontology class is strictly broader than the source concept.
- Use `CONFIRM_UNGROUNDED` (`grounding_status: UNGROUNDED`) when no ontology
  class in the slice captures the exact identity (optionally pairing with
  `relation: xref` to a host taxon, substrate, or external term).
- In `notes`, include `Path: <exact source_path>` (for GOLD paths), name every
  referenced ontology ID with its exact canonical label from
  `data/raw/ontology_terms.tsv`, and explain the scientific rationale.

#### B. `curation/term_requests.tsv`

Columns:
`identifier`, `requested_label`, `parent_class`, `parent_label`, `definition`,
`exact_synonym`, `curator`, `date`, `notes`, `parent_mode`

Rules enforced by `src/habitatmech/seed.py`, `scripts/build_term_requests.py`,
and `tests/test_term_requests.py`:

- Every row must correspond to an active record with `grounding_status == UNGROUNDED`
  and `mapping_status == REVIEWED` (`decision == CONFIRM_UNGROUNDED` and
  `review_depth == ITEM`).
- `parent_class` and `parent_label` must match an entry in
  `data/raw/ontology_terms.tsv` with `label_only != TRUE`.
- `parent_mode` must be `ADD` (default; retains valid source-derived parents and
  adds the ontology genus) or `REPLACE` (used only when item-level review proves
  every inherited source parent is false for the concept, documented in `notes`).
  When keeping a valid GOLD parent while excluding a false context-only GOLD
  parent on an ontology-grounded or ungrounded concept, use
  `curation/gold_parent_exclusions.tsv`.
- `requested_label` must be lowercase (except proper nouns/acronyms), unique
  across all rows in `curation/term_requests.tsv`, and distinct from the
  `parent_label`.
- If `requested_label` renames an ambiguous `source_label` that is not a valid
  synonym of the defined habitat, add an opt-out row to
  `curation/definition_source_label_exclusions.tsv` rather than letting the old
  ambiguous label remain as a synonym.
- `definition` must be a single Aristotelian genus-differentia sentence
  (`A <parent_label> that ...` or `An ...`) ending with a period (`.`).
- `exact_synonym` (`|`-delimited) must not duplicate `requested_label`,
  `parent_label`, or broader/host-only labels.
- If an `ITEM`-reviewed `CONFIRM_UNGROUNDED` concept is intentionally unsuitable
  for a single habitat definition (for example, a compound/disjunctive source
  bin or an underspecified administrative bucket), record it in
  `curation/term_requests_excluded.tsv` with `identifier`, `label`, and
  `why_not_a_term_request`.

#### C. `curation/causal_graphs/<slug>.yaml` (when adding mechanistic evidence)

- Validate every causal graph overlay with `just validate-causal curation/causal_graphs/<slug>.yaml`.
- Every edge must carry real, inspected `evidence` (`reference` as `PMID:...` or
  `DOI:...`, `supports: SUPPORT`, verbatim `snippet`, and `notes`).

### Step 4. Canary, regenerate, and verify

Always canary a single record before running a full corpus apply:

```bash
.venv/bin/python scripts/seed_from_sources.py --only <IDENTIFIER>
.venv/bin/python scripts/seed_from_sources.py --only <IDENTIFIER> --apply --force
```

Inspect the emitted YAML in `data/habitats/<category>/<slug>.yaml`. Then
regenerate the full corpus and derived artifacts:

```bash
.venv/bin/python scripts/seed_from_sources.py --apply --force --prune
.venv/bin/python scripts/build_term_requests.py
.venv/bin/python scripts/build_redirects.py
.venv/bin/python scripts/render_pages.py
.venv/bin/python scripts/check_docs.py --write
```

Record an append-only session log under `history/` (validated by
`.venv/bin/python scripts/validate_history.py`) and run the complete offline
quality gate suite:

```bash
.venv/bin/python scripts/run_qc.py
```
