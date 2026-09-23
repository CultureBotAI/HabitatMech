# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/engineered/algae_cultivation_tank.yaml`
- Started UTC: `2026-09-23T21:32:00Z`
- Finished UTC: `2026-09-23T21:41:39Z`
- Verdict: `needs curation`

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/engineered/algae_cultivation_tank.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.5d882de599` |
| Label | `Algae cultivation tank` |
| Definition source | Not set |
| Category | `ENGINEERED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |

This is a generated record owned by upstream inputs, not by hand edits under
`data/habitats/`. Its path is pinned by `data/habitats/PATHS.tsv`, which maps
`habitatmech:GOLD.5d882de599` to `algae_cultivation_tank`.

## Validation

| Check | Result |
|---|---|
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-algae_cultivation_tank.md' -print` | Passed; no prior exact report was present. |
| `find curation/causal_graphs -maxdepth 1 -type f -name '*algae_cultivation_tank*' -print` | Passed; no candidate causal overlay was present. |
| `rg --no-ignore --hidden -n -e "habitatmech:GOLD\.5d882de599" -e "GOLD\.5d882de599" curation/causal_graphs data/habitats reports research src tests conf -g '!data/text_map/**' -g '!pages/**' -g '!build/**'` | Passed; only the generated YAML and `PATHS.tsv` referenced the identifier, and no maintained causal overlay referenced it. Ignored and hidden files were included. |
| `just validate data/habitats/engineered/algae_cultivation_tank.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/habitats/engineered/algae_cultivation_tank.yaml` | Passed; 1 file scanned, 0 files with errors, and 0 total error rows. |
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
`habitatmech:GOLD.5d882de599`, label `Algae cultivation tank`, with path
`Engineered > WWTP > Effluent > Algae cultivation tank`. In
`data/raw/gold_ecosystem_paths.tsv`, the canonical path is a depth-4 GOLD leaf
covering two upstream node IDs, `gold.ecosystem:7772` and
`gold.ecosystem:7773`.

The only decision row for this concept is still the 2026-08-12 class-level
`CONFIRM_UNGROUNDED` sweep row. That row checked lexical absence in the
vendored ontology slice but explicitly did not assess whether the source
concept is a habitat. The generated `mapping_status: SEEDED` is therefore
correct: there is no item-level curation row, no HabitatMech-authored
definition, and no term-request row for `habitatmech:GOLD.5d882de599`.

The vendored slice has near misses but not an exact label match for this GOLD
leaf. `ENVO:03600047` `raceway pond` is defined as a pond constructed for
algae cultivation and already lines up with GOLD's separate
`Engineered > Artificial ecosystem > Aquaculture > Algae raceway pond` path.
`ENVO:03600077` `photobioreactor` is broader only if item review confirms the
WWTP effluent tank denotes a light-driven algal bioreactor. The generic
`ENVO:00002123` `bioreactor` term is also a plausible broader-term candidate
for a future minted definition, but the record needs source review before a
curator picks a genus.

## Evidence

The GOLD source attestation preserves the `data/raw/gold_ecosystem_paths.tsv`
source label and source path. Its `source_id` is `gold.ecosystem:7772`, which
is the first of the two GOLD node IDs collapsed into this canonical path; the
generated note correctly points to `data/raw/gold_ecosystem_paths.tsv` for the
full ID set.

The GOLD API-derived side inventories add context that is not yet asserted on
the generated record: `data/raw/gold_studies.tsv` has one study for the same
path, and `data/raw/gold_path_biosamples.tsv` has 16 biosamples for the second
collapsed node ID, `7773`. No `data/raw/gold_path_triads.tsv` row was found for
`Engineered > WWTP > Effluent > Algae cultivation tank`, so the record
correctly has no generated `environmental_parameters`.

The record has no `definition`, `definition_source`, authored synonyms,
`characteristic_taxa`, causal graph, claim-level evidence block, discussion
item, or dataset usage. No maintained input currently asserts those fields.

## Completeness

The record is structurally reproducible but not complete enough for a reviewed
state:

- It has no item-level decision for its only source concept.
- Its class-level sweep row intentionally did not establish whether the GOLD
  concept denotes a microbial habitat, a treatment unit, or wastewater effluent
  inside a treatment unit.
- It still lacks a HabitatMech definition that chooses the intended physical
  scope and a defensible broader genus.
- It inherits the GOLD path parent `Engineered > WWTP > Effluent`, generated as
  `habitatmech:GOLD.827b5dbbef`, even though the source leaf names a tank and
  a tank is not a strict subclass of effluent.

Bounded, ignored-inclusive exact searches for
`habitatmech:GOLD.5d882de599`, `gold.ecosystem:7772`,
`gold.ecosystem:7773`, `Algae cultivation tank`, and the canonical GOLD path
across curation inputs, raw inputs, `PATHS.tsv`, history, reports, research,
source, tests, and configuration found the class-level decision, GOLD raw rows,
the `PATHS.tsv` slug row, the generated target record, and a host-associated
algae research-report cross-reference. Generated `data/text_map/`, `pages/`,
and `build/` files were excluded; ignored and hidden files were included.

## Findings

### Major

| Finding | Evidence | Maintained owner |
|---|---|---|
| The record publishes `Effluent` as a broader habitat of `Algae cultivation tank`, but the source leaf does not name a kind of effluent. | `src/habitatmech/seed.py` derives the parent edge from GOLD's source path, so `data/habitats/engineered/algae_cultivation_tank.yaml` inherits `habitatmech:GOLD.827b5dbbef` from `Engineered > WWTP > Effluent`. In `parent_habitats`, that edge asserts an `is-a` relation; an algae cultivation tank is a managed treatment vessel containing effluent, not a subclass of the effluent material. The parent concept is itself only class-sweep reviewed. | `curation/decisions.tsv`; `curation/term_requests.tsv` |

## Recommended Edits

1. Add an item-level curation row for
   `habitatmech:GOLD.5d882de599` in `curation/decisions.tsv` after reviewing
   the GOLD source concept. Keep the record minted if no exact vendored term
   names the tank scope.
2. If the source concept is confirmed as a real habitat lacking an exact
   vendored term, add a `curation/term_requests.tsv` row that defines the tank
   scope, selects a defensible genus such as `ENVO:00002123` `bioreactor` or
   `ENVO:03600077` `photobioreactor`, and uses `parent_mode=REPLACE` to drop
   the inherited `Effluent` parent.

## Follow-up Checks

- Run `just term-requests-check` if a term-request row is added.
- Run `just seed`, `just seed-canary habitatmech:GOLD.5d882de599`, inspect
  `data/habitats/engineered/algae_cultivation_tank.yaml`, then run
  `just seed-apply --force`.
- Run `just validate-strict data/habitats/engineered/algae_cultivation_tank.yaml`
  to prove the regenerated record still satisfies the closed LinkML schema.
- Run `just verify-corpus --max-diffs 1` to prove the generated corpus has no
  unexpected drift.
- Run `just validate-history` after writing the required append-only history
  record for the future curation session.

## Additional Notes

`data/raw/gold_ecosystem_paths.tsv` also has the parent
`Engineered > WWTP > Effluent` as its own depth-3 path with three collapsed
GOLD node IDs and zero organism, study, biosample, or total assertion counts.
`data/raw/gold_path_biosamples.tsv` records 23 biosamples against the third of
those node IDs, but no item-level decision has yet resolved the generic
`Effluent` source concept either.
