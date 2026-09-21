# YAML Record Review: Composting facility

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/air/composting_facility.yaml
- Started UTC: 2026-09-21T05:17:30Z
- Finished UTC: 2026-09-21T05:23:48Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/air/composting_facility.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.228c68bdf2` |
| Label | `Composting facility` |
| Category | `AIR` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Maintained status | generated from `data/raw/`, `curation/decisions.tsv`, and `data/habitats/PATHS.tsv` |

The generated record is a compact GOLD-only placeholder:

- GOLD supplies one `Environmental > Air > Indoor Air > Composting facility`
  source attestation with one `ORGANISM` assertion.
- The parent `habitatmech:GOLD.40979f5751` comes from the preceding GOLD path
  step, `Indoor Air`.
- A class-level curation decision rejected automatic lexical grounding but did
  not assess the source concept as an individual habitat.
- No definition, authored term request, item-level grounding decision, taxa,
  environmental parameters, evidence, causal graphs, discussions, datasets,
  synonyms, or xrefs are present.

## Validation

| Check | Result |
|---|---|
| `.venv/bin/python -c "from linkml.validator.cli import cli; cli()" --schema src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/air/composting_facility.yaml` | Passed; no LinkML issues. |
| `.venv/bin/python scripts/validate_strict.py data/habitats/air/composting_facility.yaml --quiet` | Passed; 1 file scanned, 0 files with errors, 0 total error rows. |
| `.venv/bin/python scripts/build_term_requests.py --check` | Passed; term-request table is current at 109 terms. |
| `.venv/bin/python scripts/verify_corpus.py --max-diffs 1` | Passed; 3,206 expected records, 3,206 found, no missing/extra/differing records. |
| `.venv/bin/python scripts/validate_history.py` | Passed; 77 history records valid against `src/habitatmech/schema/history.yaml`. |
| Reference validator | Not checked: this record has no DOI/PMID/URL `EvidenceItem` or causal-edge evidence, and no dedicated `research/habitats/air/` report for `habitatmech:GOLD.228c68bdf2` requiring `scripts/check_report_citations.py` exists. |

## Identity and Grounding

| Claim | Evidence | Assessment |
|---|---|---|
| The record denotes the GOLD `Environmental > Air > Indoor Air > Composting facility` source concept. | `data/raw/gold_ecosystem_paths.tsv` has exactly that canonical path, leaf `Composting facility`, depth `4`, `gold_node_count=2`, `organism_count=1`, `total_assertions=1`, and node IDs `gold.ecosystem:7107\|gold.ecosystem:7108`. | Supported exactly. |
| The stable file stem is `composting_facility`. | `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.228c68bdf2` to `composting_facility`. | Supported exactly. |
| The source path justifies the broad AIR category and the `indoor_air` parent. | The raw GOLD path is under `Environmental > Air > Indoor Air`; `data/habitats/PATHS.tsv` maps the parent identifier `habitatmech:GOLD.40979f5751` to `indoor_air`. `curation/decisions.tsv` and `curation/term_requests.tsv` show that the `indoor air` parent has item-level review and an authored term request under `ENVO:00002005` `air`. | Supported if the leaf means composting-facility air rather than the facility building, compost pile, or some other source artifact. |
| `grounding_status: UNGROUNDED` is generated from a class-level no-match sweep. | `curation/decisions.tsv` has `habitatmech:GOLD.228c68bdf2` as `CONFIRM_UNGROUNDED` with `review_depth=CLASS` and no object ID. Its note says no vendored-slice term matched the label by any search route and explicitly says whether the concept is a habitat was not assessed. | Mechanically supported but incomplete for item-level curation. |
| `mapping_status: SEEDED` is correct. | The only curation row for `habitatmech:GOLD.228c68bdf2` has `review_depth=CLASS`; `docs/CURATION.md` states that only item-level decisions promote a merged record to `REVIEWED`. | Supported exactly. |

## Evidence

No claim-level literature evidence was present. The record has no
characteristic taxon rows and no causal graph, so there are no taxon
associations, causal edges, or snippets to audit.

## Completeness

- The record is schema-valid and reproducible, but not item-curated.
- Empty `characteristic_taxa`, `evidence`, `environmental_parameters`,
  `causal_graphs`, `discussions`, `datasets`, `synonyms`, and `xrefs` are
  technically acceptable: no maintained input currently supplies them for this
  record.
- `data/raw/gold_path_triads.tsv`, `data/raw/environment_parameters.tsv`, and
  `curation/term_requests.tsv` have no row for
  `Environmental > Air > Indoor Air > Composting facility`,
  `habitatmech:GOLD.228c68bdf2`, or `gold.ecosystem:7107`.
- Ignored/hidden-inclusive exact searches covered `data`, `curation`,
  `research`, `docs`, `src`, `.claude`, and `reports`, excluding only generated
  text-map, cache, and build trees, for `habitatmech:GOLD.228c68bdf2`,
  `gold.ecosystem:7107`, `Composting facility`, and `composting_facility`. They
  found the target, its `PATHS.tsv` row, the raw GOLD path, the class-level
  decision row, adjacent research reports mentioning GOLD `Indoor Air`
  children, and one adjacent prior YAML review; they found no item-level
  decision, term-request row, causal overlay, or dedicated research report for
  this target.
- A bounded `find curation/causal_graphs -maxdepth 1 -type f -name '*compost*'`
  search found `curation/causal_graphs/compost.yaml`, but that overlay targets
  `ENVO:00002170` `compost`, not `habitatmech:GOLD.228c68bdf2`.
- A bounded `find research/habitats -maxdepth 3 -type f -name '*compost*'`
  search found no candidate dedicated research report.
- A bounded `find reports/yaml_record_review -maxdepth 1` search and an exact
  ignored/hidden-inclusive `rg` search under `reports/yaml_record_review/`
  found no prior review for `data/habitats/air/composting_facility.yaml` or
  `habitatmech:GOLD.228c68bdf2`.

## Findings

### Major

| ID | Finding | Evidence | Maintained owner |
|---|---|---|---|
| `HM-COMPOSTING-FACILITY-001` | The source concept still needs item-level curation. The generated record treats `Composting facility` as an AIR habitat under `indoor air`, but its only curation row is a `CLASS`-depth lexical no-match sweep that explicitly did not assess whether the concept is a habitat. | `curation/decisions.tsv` row `habitatmech:GOLD.228c68bdf2` has `review_depth=CLASS` and the note "Whether the concept is a habitat at all was NOT assessed, so this is not yet a term-request candidate." | `curation/decisions.tsv`, with a possible follow-on `curation/term_requests.tsv` row if item review confirms GOLD means composting-facility air and no ontology term fits. |

## Recommended Edits

1. Item-review `habitatmech:GOLD.228c68bdf2` in
   `curation/decisions.tsv`. Resolve whether the GOLD child under
   `Environmental > Air > Indoor Air` denotes composting-facility air, the
   composting facility building, a compost pile or compost material, or another
   source artifact.
2. If the concept is real composting-facility air and no vendored ontology term
   fits, add a `curation/term_requests.tsv` row with an authored definition and
   a vendored ontology genus. Use default `ADD` parent mode to retain
   `habitatmech:GOLD.40979f5751` `indoor air` when item review confirms that
   inherited source parent is true.
3. Regenerate a single-record canary for `habitatmech:GOLD.228c68bdf2`, inspect
   `data/habitats/air/composting_facility.yaml`, and confirm that the generated
   `grounding_status`, `mapping_status`, definition, parent, source
   attestation, and curation history all follow from the maintained rows.

## Follow-up Checks

- `.venv/bin/python scripts/seed_from_sources.py`
- `.venv/bin/python scripts/seed_from_sources.py --apply --only habitatmech:GOLD.228c68bdf2`
- `.venv/bin/python -c "from linkml.validator.cli import cli; cli()" --schema src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/air/composting_facility.yaml`
- `.venv/bin/python scripts/validate_strict.py data/habitats/air/composting_facility.yaml --quiet`
- `.venv/bin/python scripts/build_term_requests.py --check`
- `.venv/bin/python scripts/verify_corpus.py --max-diffs 1`

## Additional Notes

- `research/habitats/air/indoor-air-habitatmech-gold-40979f5751-deep-research-claude_code.md`
  discusses the GOLD `Cattle barn`, `Poultry farm`, `Composting facility`,
  `Dust`, and `Air scrubber` children under `Indoor Air`, but that report is
  evidence for the parent `Indoor Air` definition rather than an item-level
  composting-facility-air review.
- Committed `Dust`, `Air scrubber`, and `Environmental` research reports also
  mention the GOLD `Composting facility` child as an `Indoor Air` sibling or
  count, but none of them inspect `Composting facility` as their target.
- `curation/causal_graphs/compost.yaml` backs the generated `ENVO:00002170`
  `compost` record. It is not maintained input for the GOLD composting-facility
  record.
