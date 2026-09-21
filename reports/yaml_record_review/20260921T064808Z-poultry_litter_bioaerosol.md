# YAML Record Review: Poultry litter bioaerosol

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/air/poultry_litter_bioaerosol.yaml
- Started UTC: 2026-09-21T06:48:08Z
- Finished UTC: 2026-09-21T06:48:20Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/air/poultry_litter_bioaerosol.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.6c54e5b602` |
| Label | `Poultry litter bioaerosol` |
| Category | `AIR` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Maintained status | generated from `data/raw/`, `curation/decisions.tsv`, and `data/habitats/PATHS.tsv` |

The generated record is a compact GOLD-only placeholder:

- GOLD supplies one `Environmental > Air > Indoor Air > Poultry farm > Poultry
  litter bioaerosol` source attestation.
- The parent `habitatmech:GOLD.8a960b7130` comes from the preceding GOLD path
  step, `Poultry farm`.
- GOLD's MIxS triad inventory separately reports 15 biosamples on this path
  with `ENVO:00000077` `agricultural feature` as broad scale,
  `ENVO:00002192` `poultry litter` as local scale, and `ENVO:00002005` `air`
  as medium.
- A class-level curation decision rejected automatic lexical grounding but did
  not assess the source concept as an individual habitat.
- No definition, authored term request, item-level grounding decision, taxa,
  environmental parameters, evidence, causal graphs, discussions, datasets,
  synonyms, or xrefs are present.

## Validation

| Check | Result |
|---|---|
| `.venv/bin/python -c "from linkml.validator.cli import cli; cli()" --schema src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/air/poultry_litter_bioaerosol.yaml` | Passed; no LinkML issues. |
| `.venv/bin/python scripts/validate_strict.py data/habitats/air/poultry_litter_bioaerosol.yaml --quiet` | Passed; 1 file scanned, 0 files with errors, 0 total error rows. |
| `.venv/bin/python scripts/build_term_requests.py --check` | Passed; term-request table is current at 109 terms. |
| `.venv/bin/python scripts/verify_corpus.py --max-diffs 1` | Passed; 3,206 expected records, 3,206 found, no missing/extra/differing records. |
| `.venv/bin/python scripts/validate_history.py` | Passed; 77 history records valid against `src/habitatmech/schema/history.yaml`. |
| Reference validator | Not checked: this record has no DOI/PMID/URL `EvidenceItem` or causal-edge evidence, and no dedicated `research/habitats/air/` report for `habitatmech:GOLD.6c54e5b602` requiring `scripts/check_report_citations.py` exists. |

## Identity and Grounding

| Claim | Evidence | Assessment |
|---|---|---|
| The record denotes the GOLD `Environmental > Air > Indoor Air > Poultry farm > Poultry litter bioaerosol` source concept. | `data/raw/gold_ecosystem_paths.tsv` has exactly that canonical path, leaf `Poultry litter bioaerosol`, depth `5`, `gold_node_count=1`, `organism_count=0`, `total_assertions=0`, and node ID `gold.ecosystem:6884`. `data/raw/gold_path_biosamples.tsv` has 15 biosamples for the same source path and GOLD node. | Supported exactly. |
| The stable file stem is `poultry_litter_bioaerosol`. | `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.6c54e5b602` to `poultry_litter_bioaerosol`. | Supported exactly. |
| The source path justifies the broad AIR category and the `poultry_farm__064a62e0` parent. | The raw GOLD path is under `Environmental > Air > Indoor Air > Poultry farm`; `data/habitats/PATHS.tsv` maps the parent identifier `habitatmech:GOLD.8a960b7130` to `poultry_farm__064a62e0`. The raw GOLD triads for this child put `air` in the MIxS medium slot and `poultry litter` in the local-scale slot for 15 biosamples. | Supported if the leaf means aerosolized material in poultry-farm air rather than a poultry-litter sample artifact or another source artifact. |
| `grounding_status: UNGROUNDED` is generated from a class-level no-match sweep. | `curation/decisions.tsv` has `habitatmech:GOLD.6c54e5b602` as `CONFIRM_UNGROUNDED` with `review_depth=CLASS` and no object ID. Its note says no vendored-slice term matched the label by any search route and explicitly says whether the concept is a habitat was not assessed. | Mechanically supported but incomplete for item-level curation. |
| `mapping_status: SEEDED` is correct. | The only curation row for `habitatmech:GOLD.6c54e5b602` has `review_depth=CLASS`; `docs/CURATION.md` states that only item-level decisions promote a merged record to `REVIEWED`. | Supported exactly. |

## Evidence

No claim-level literature evidence was present. The record has no
characteristic taxon rows and no causal graph, so there are no taxon
associations, causal edges, or snippets to audit.

The raw GOLD MIxS triads are source-context rows, not literature evidence or a
curated definition. They support the review hypothesis that this path was used
for air samples local to poultry litter, but they do not replace an item-level
habitat decision.

## Completeness

- The record is schema-valid and reproducible, but not item-curated.
- Empty `characteristic_taxa`, `evidence`, `environmental_parameters`,
  `causal_graphs`, `discussions`, `datasets`, `synonyms`, and `xrefs` are
  technically acceptable: no maintained input currently supplies them for this
  record.
- `data/raw/environment_parameters.tsv` has no row for
  `Environmental > Air > Indoor Air > Poultry farm > Poultry litter bioaerosol`.
- `curation/term_requests.tsv`,
  `curation/term_requests/envo_robot_template.tsv`, and
  `reports/habitat_research_manifest.tsv` have no row for
  `habitatmech:GOLD.6c54e5b602`.
- Ignored/hidden-inclusive exact searches covered `data/raw`,
  `data/habitats/air`, `curation`, `research/habitats`,
  `reports/habitat_research_manifest.tsv`, and `reports/yaml_record_review`,
  excluding only generated text-map, cache, and build trees, for
  `habitatmech:GOLD.6c54e5b602`, `gold.ecosystem:6884`,
  `Poultry litter bioaerosol`, and `poultry_litter_bioaerosol`. They found the
  target, the raw GOLD path, raw GOLD biosamples and triads, the class-level
  decision row, adjacent research reports mentioning GOLD `Indoor Air`
  children, and the parent `Poultry farm` YAML review; they found no item-level
  decision, term-request row, causal overlay, research manifest entry, or
  dedicated research report for this target.
- A bounded `find curation/causal_graphs -maxdepth 1 -type f -name '*poultry*'`
  search found no candidate causal overlay.
- A bounded `find research/habitats -type f -name '*poultry*'` search found no
  candidate dedicated research report.
- A bounded `find reports/yaml_record_review -maxdepth 1` search and an exact
  ignored/hidden-inclusive `rg` search under `reports/yaml_record_review/`
  found no prior review for
  `data/habitats/air/poultry_litter_bioaerosol.yaml` or
  `habitatmech:GOLD.6c54e5b602`; the existing parent `Poultry farm` review
  mentions this child but does not audit it.

## Findings

### Major

| ID | Finding | Evidence | Maintained owner |
|---|---|---|---|
| `HM-POULTRY-LITTER-BIOAEROSOL-001` | The source concept still needs item-level curation. The generated record treats `Poultry litter bioaerosol` as an AIR habitat under `Poultry farm`, but its only curation row is a `CLASS`-depth lexical no-match sweep that explicitly did not assess whether the concept is a habitat. | `curation/decisions.tsv` row `habitatmech:GOLD.6c54e5b602` has `review_depth=CLASS` and the note "Whether the concept is a habitat at all was NOT assessed, so this is not yet a term-request candidate." | `curation/decisions.tsv`, with a possible follow-on `curation/term_requests.tsv` row if item review confirms GOLD means poultry-litter bioaerosol and no ontology term fits. |

## Recommended Edits

1. Item-review `habitatmech:GOLD.6c54e5b602` in
   `curation/decisions.tsv`. Resolve whether the GOLD child under
   `Environmental > Air > Indoor Air > Poultry farm` denotes aerosolized
   poultry litter in air, a poultry-litter material sample, or another source
   artifact; account for the sibling parent `habitatmech:GOLD.8a960b7130`
   remaining at `CLASS` review depth.
2. If the concept is real poultry-litter bioaerosol and no vendored ontology
   term fits, add a `curation/term_requests.tsv` row with an authored
   definition and a vendored ontology genus. Use default `ADD` parent mode to
   retain `habitatmech:GOLD.8a960b7130` `Poultry farm` only if item review
   confirms that inherited source parent is true.
3. Regenerate a single-record canary for `habitatmech:GOLD.6c54e5b602`, inspect
   `data/habitats/air/poultry_litter_bioaerosol.yaml`, and confirm that the
   generated `grounding_status`, `mapping_status`, definition, parent, source
   attestation, and curation history all follow from the maintained rows.

## Follow-up Checks

- `.venv/bin/python scripts/seed_from_sources.py`
- `.venv/bin/python scripts/seed_from_sources.py --apply --only habitatmech:GOLD.6c54e5b602`
- `.venv/bin/python -c "from linkml.validator.cli import cli; cli()" --schema src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/air/poultry_litter_bioaerosol.yaml`
- `.venv/bin/python scripts/validate_strict.py data/habitats/air/poultry_litter_bioaerosol.yaml --quiet`
- `.venv/bin/python scripts/build_term_requests.py --check`
- `.venv/bin/python scripts/verify_corpus.py --max-diffs 1`

## Additional Notes

- `research/habitats/engineered/air-scrubber-habitatmech-gold-ebf95a8a4a-deep-research-claude_code.md`
  and
  `research/habitats/engineered/dust-habitatmech-gold-398aeb6c37-deep-research-claude_code.md`
  mention `Poultry litter bioaerosol` as an `Indoor Air` sibling while
  reasoning about different GOLD children. They are not item-level reviews of
  `habitatmech:GOLD.6c54e5b602`.
- `data/raw/gold_studies.tsv` shows one study listing both
  `Environmental > Air > Indoor Air > Poultry farm` and
  `Environmental > Air > Indoor Air > Poultry farm > Poultry litter bioaerosol`.
  That shared study link makes parent/child item review worth doing together.
