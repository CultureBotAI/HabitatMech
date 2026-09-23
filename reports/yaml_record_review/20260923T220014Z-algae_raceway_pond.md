# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/engineered/algae_raceway_pond.yaml`
- Started UTC: `2026-09-23T21:57:04Z`
- Finished UTC: `2026-09-23T22:00:14Z`
- Verdict: `needs curation`

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/engineered/algae_raceway_pond.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.e474187df8` |
| Label | `Algae raceway pond` |
| Definition source | Not set |
| Category | `ENGINEERED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |

This is a generated record owned by upstream inputs, not by hand edits under
`data/habitats/`. Its path is pinned by `data/habitats/PATHS.tsv`, which maps
`habitatmech:GOLD.e474187df8` to `algae_raceway_pond`.

## Validation

| Check | Result |
|---|---|
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-algae_raceway_pond.md' -print` | Passed; no prior exact report was present. |
| `find curation/causal_graphs -maxdepth 1 -type f -name '*algae_raceway_pond*' -print` | Passed; no candidate causal overlay was present. |
| `rg --no-ignore --hidden -n --fixed-strings ... curation data/raw data/habitats reports research src tests conf -g '!data/text_map/**' -g '!pages/**' -g '!build/**'` | Passed; bounded exact searches found the class-level decision, GOLD raw rows, the `PATHS.tsv` slug row, the generated target and child records, prior report/research cross-references, and the matching vendored ENVO term. Ignored and hidden files were included. |
| `just validate data/habitats/engineered/algae_raceway_pond.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/habitats/engineered/algae_raceway_pond.yaml` | Passed; 1 file scanned, 0 files with errors, and 0 total error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| Focused causal-graph validation | Not applicable; the record has no maintained overlay under `curation/causal_graphs/`. |
| Reference validator | Not applicable; the record has no DOI, PMID, URL, causal-edge evidence, dataset, or discussion references to check. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just validate-history` | Passed; no issues found and 77 history records validated. |
| `just verify-corpus --max-diffs 1` | Passed; 3,206 expected records, 3,206 on disk, 0 missing, 0 extra, and 0 differing. |
| `just worklist --limit 2000` | Passed; the command reported 0 ungrounded records still undecided and 1,810 decisions on file. |
| `just report` | Passed; the corpus report completed for 3,206 records. |
| `git diff --check` | Passed before report creation. |

## Identity and Grounding

The GOLD source concept is represented by the generated minted identifier
`habitatmech:GOLD.e474187df8`, label `Algae raceway pond`, with path
`Engineered > Artificial ecosystem > Aquaculture > Algae raceway pond`. In
`data/raw/gold_ecosystem_paths.tsv`, the canonical path is a depth-4 GOLD leaf
covering two upstream node IDs, `gold.ecosystem:7993` and
`gold.ecosystem:7994`.

The only decision row for this concept is still the 2026-08-12 class-level
`CONFIRM_UNGROUNDED` sweep row. That row checked lexical absence in the
vendored ontology slice but explicitly did not assess whether the source
concept is a habitat. The generated `mapping_status: SEEDED` is therefore
correct for the maintained inputs, but the generated `grounding_status:
UNGROUNDED` is now stale at the record level.

`data/raw/ontology_terms.tsv` already contains `ENVO:03600047` `raceway pond`,
defined as a pond constructed by humans for algae cultivation, with `algal
pond` as a synonym. That definition exactly matches GOLD's `Algae raceway
pond` leaf, and the vendored subclass slice keeps the ENVO term beneath both
`ENVO:00000033` and `ENVO:00000070`. GOLD's MIxS triads corroborate the match:
`data/raw/gold_path_triads.tsv` maps four biosamples from one study for this
source path to local term `ENVO:03600047`.

## Evidence

The GOLD source attestation preserves the `data/raw/gold_ecosystem_paths.tsv`
source label and source path. Its `source_id` is `gold.ecosystem:7993`, which
is the first of the two GOLD node IDs collapsed into this canonical path; the
generated note correctly points to `data/raw/gold_ecosystem_paths.tsv` for the
full ID set.

The GOLD API-derived side inventories add context that is not yet asserted on
the generated record. `data/raw/gold_studies.tsv` lists study `Gs0126276`
against the same path, `data/raw/gold_path_biosamples.tsv` lists four
biosamples for `gold.ecosystem:7994`, and `data/raw/gold_path_triads.tsv`
summarizes those four samples as agreeing on `ENVO:03600047` as the local MIxS
term.

The record has no `definition`, `definition_source`, authored synonyms,
`environmental_parameters`, `characteristic_taxa`, causal graph, claim-level
evidence block, discussion item, or dataset usage. No maintained input
currently asserts those fields.

## Completeness

The record is structurally reproducible but not complete enough for a reviewed
state:

- It has no item-level grounding decision for its only source concept.
- It still carries an ungrounded minted identifier even though the vendored
  ENVO slice has an exact class for the leaf habitat.
- Its only current curation decision is a class-level lexical sweep that did
  not read the individual source concept.
- Generated child records for GOLD `Pond scum` and `Sediment` inherit the
  minted `habitatmech:GOLD.e474187df8` parent until this parent is grounded and
  regenerated.

Bounded, ignored-inclusive exact searches for
`habitatmech:GOLD.e474187df8`, `GOLD.e474187df8`,
`gold.ecosystem:7993`, `gold.ecosystem:7994`,
`Algae raceway pond`, `algae_raceway_pond`, `ENVO:03600047`, and
`raceway pond` across curation inputs, raw inputs, `PATHS.tsv`, generated YAML,
reports, research, source, tests, and configuration found the
class-level decision, GOLD raw rows, matching ontology rows, the `PATHS.tsv`
slug row, the generated target and child records, a prior review-report
cross-reference, and host-associated algae research-report cross-references.
Generated `data/text_map/`, `pages/`, and `build/` files were excluded;
ignored and hidden files were included.

## Findings

### Major

| Finding | Evidence | Maintained owner |
|---|---|---|
| The record remains `UNGROUNDED` and minted even though a vendored exact term exists. | `data/habitats/engineered/algae_raceway_pond.yaml` is generated from the 2026-08-12 class-level `CONFIRM_UNGROUNDED` row for `habitatmech:GOLD.e474187df8`. `data/raw/ontology_terms.tsv` already has `ENVO:03600047` `raceway pond`, defined as a pond constructed for algae cultivation, and GOLD's local MIxS triad for `Engineered > Artificial ecosystem > Aquaculture > Algae raceway pond` also points to `ENVO:03600047`. | `curation/decisions.tsv` |

## Recommended Edits

1. Add an item-level `GROUND` decision for `habitatmech:GOLD.e474187df8` in
   `curation/decisions.tsv` that maps the GOLD source concept to
   `ENVO:03600047` `raceway pond` with `EXACT`.
2. Regenerate seeded records so the reviewed output uses the ENVO identifier
   and no longer publishes a minted, ungrounded `Algae raceway pond` class.

## Follow-up Checks

- Run `just seed`.
- Run `just seed-canary ENVO:03600047` and inspect the generated raceway-pond
  record plus GOLD `Pond scum` and `Sediment` children for expected parent
  updates.
- Run `just seed-apply --force`.
- Run `just validate-strict` against the regenerated raceway-pond record to
  prove it still satisfies the closed LinkML schema.
- Run `just verify-corpus --max-diffs 1` to prove the generated corpus has no
  unexpected drift.
- Run `just validate-history` after writing the required append-only history
  record for the future curation session.

## Additional Notes

The raw ontology slice already places `ENVO:03600047` beneath `ENVO:00000033`
and `ENVO:00000070`. A future grounding pass can therefore use the existing
vendored ontology parentage for `raceway pond` instead of adding a HabitatMech
term request.
