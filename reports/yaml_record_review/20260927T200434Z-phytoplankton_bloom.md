# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/phytoplankton_bloom.yaml`
- Started UTC: 2026-09-27T19:57:00Z
- Finished UTC: 2026-09-27T20:04:34Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.46309b7794` |
| Label | `Phytoplankton bloom` |
| Class | `HabitatRecord` |
| Category | `AQUATIC` |
| Generated or maintained | Generated from `data/raw/`, `curation/decisions.tsv`, and `data/habitats/PATHS.tsv`; do not hand-edit |
| Current grounding | `UNGROUNDED` |
| Current mapping | `SEEDED` |

The target resolves to exactly one generated YAML file and one pinned slug:
`data/habitats/aquatic/phytoplankton_bloom.yaml`. `data/habitats/PATHS.tsv`
maps `habitatmech:GOLD.46309b7794` to `phytoplankton_bloom`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/phytoplankton_bloom.yaml` | Pass: LinkML reported `No issues found`. |
| `just validate-strict data/habitats/aquatic/phytoplankton_bloom.yaml` | Pass: 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just validate-causal-all` | Pass: 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Pass: committed term-request table is current with 109 terms. |
| `just validate-history` | Pass: 77 history records valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus` | Pass: 3,206 expected records, 3,206 found, 0 missing, 0 extra, 0 differing. |
| `just worklist --status all --out /tmp/habitatmech-phytoplankton-bloom-worklist.tsv` | Attempted twice; both runs hung before creating the requested `/tmp` TSV and were terminated with SIGTERM. |
| `just report --out /tmp/habitatmech-phytoplankton-bloom-report.tsv` | Attempted twice; both runs printed the corpus summary through `=== 15 novel label(s) held by records from different sources ===`, then hung before listing that section or writing the requested `/tmp` TSV. Both runs were terminated with SIGTERM. |

All documented validators that completed were clean. No `curation_worklist.py` or
`habitat_report.py` processes were left running after the hung diagnostics were
terminated.

## Identity and Grounding

The record identity is reproducible. `data/raw/gold_ecosystem_paths.tsv` has one
exact path for `Environmental > Aquatic > Marine > Coastal > Phytoplankton
bloom`; the raw row records one GOLD node, `gold.ecosystem:5825`, one organism
assertion, zero exact-path study assertions, zero exact-path GOLD API biosample
assertions, and one total assertion. `data/habitats/PATHS.tsv` pins the minted
source concept to the current `phytoplankton_bloom` slug.

The existing generated parent `ENVO:00002150` is copied from the GOLD parent
path `Environmental > Aquatic > Marine > Coastal`, not from evidence for the
exact `Phytoplankton bloom` leaf. The exact bloom path has no rows in
`data/raw/gold_path_triads.tsv`, `data/raw/gold_path_biosamples.tsv`, or
`data/raw/gold_studies.tsv`. The `Coastal` parent path does have MIxS support
for a coastal-water context: 2,011 samples across 64 studies point to
`ENVO:00000447` `marine biome`, `ENVO:02000049` `coastal water body`, and
`ENVO:00002150` `coastal sea water` as broad, local, and medium triads.

`coastal sea water` is therefore context for the GOLD path, but it is not the
bloom's genus. A phytoplankton bloom is a rapid accumulation of phytoplankton in
water, not a kind of the water material itself.

The `UNGROUNDED` status is also now too weak. `data/raw/ontology_terms.tsv`
contains both `ENVO:2000004` `algal bloom` and its subclass `ENVO:01000057`
`marine algal bloom`; `data/raw/ontology_subclass_edges.tsv` records
`ENVO:01000057 rdfs:subClassOf ENVO:2000004`. The GOLD source path supplies
the missing context that this is a marine coastal phytoplankton bloom. That
source concept should remain minted so the coastal restriction is preserved,
but `ENVO:01000057` is a valid broader parent.

## Evidence

Supported:

| Claim | Evidence |
|---|---|
| The record is the generated GOLD concept for the coastal marine phytoplankton-bloom path. | `data/raw/gold_ecosystem_paths.tsv` row 944 and `data/habitats/PATHS.tsv` row 1820 agree on the canonical path, `gold.ecosystem:5825`, `habitatmech:GOLD.46309b7794`, and `phytoplankton_bloom`. |
| The source is GOLD-only with one organism assertion. | The exact raw GOLD ecosystem row has `organism_count=1`, `study_count=0`, `biosample_count=0`, and `total_assertions=1`; the YAML stores `assertion_count: 1` with `assertion_unit: ORGANISM`. |
| Exact-path MIxS, GOLD biosample, and GOLD study support are absent. | Exact hidden- and ignored-file-inclusive `rg` searches for `Environmental > Aquatic > Marine > Coastal > Phytoplankton bloom` and `gold.ecosystem:5825` across `data/raw/*.tsv` found only `data/raw/gold_ecosystem_paths.tsv`. |
| A bloom parent exists in the vendored ontology slice. | `data/raw/ontology_terms.tsv` contains `ENVO:01000057` `marine algal bloom`, and `data/raw/ontology_subclass_edges.tsv` places it below `ENVO:2000004` `algal bloom`. |
| The existing `coastal sea water` parent is inherited from path context. | The immediate GOLD parent path `Environmental > Aquatic > Marine > Coastal` has medium-scale MIxS evidence for `ENVO:00002150`; the exact `Phytoplankton bloom` path has no triad rows. |

Unsupported or stale:

| Claim | Issue |
|---|---|
| No ontology term fits `Phytoplankton bloom`. | That claim came from a class-level sweep over the leaf label. Once the full GOLD path is read, `ENVO:01000057` `marine algal bloom` is an existing broader class for a coastal marine phytoplankton bloom. |
| `ENVO:00002150` `coastal sea water` is a strict broader `parent_habitats` class. | Coastal sea water is the water material in which a bloom can occur. The bloom itself is a feature/state in the water column, not a subtype of the material. |

## Completeness

The record has no curator-authored definition, evidence, causal graphs,
discussions, datasets, environmental parameters, or characteristic taxa. Those
slots are expected for the current generated GOLD-only record.

The only maintained curation row for the target is the 2026-08-12
`CONFIRM_UNGROUNDED` row in `curation/decisions.tsv`; its note explicitly says
the class-level sweep did not assess whether the source concept was a habitat
or a term-request candidate. There is no row for this target in
`curation/term_requests.tsv`, `curation/term_requests_excluded.tsv`,
`curation/external_xrefs.tsv`, or `curation/redirects_retracted.tsv`.

Exact hidden- and ignored-file-inclusive searches of
`reports/yaml_record_review`, `research`, `curation`, `history`, `conf`, and
`data/habitats/PATHS.tsv` found no prior review, no target-owned deep-research
report, no causal overlay, no history entry, no term request, no term-request
exclusion, no external xref, and no id-label target for
`data/habitats/aquatic/phytoplankton_bloom.yaml`,
`habitatmech:GOLD.46309b7794`, `gold.ecosystem:5825`, or the exact GOLD source
path.

Several unrelated deep-research reports mention `Phytoplankton bloom`,
`ENVO:2000004`, or `ENVO:01000057` only as adjacent non-matches for seaweed,
algae-as-host, and standing-plankton records. They correctly treat algal
blooms as distinct water-column features and do not curate this GOLD
phytoplankton-bloom record.

The prior `algal_bloom` YAML review already found the analogous freshwater
case: GOLD's `Environmental > Aquatic > Freshwater > Lake > Algal bloom` path
should stay minted under `ENVO:2000005` `freshwater algal bloom`, rather than
being merged into generic `ENVO:2000004` or inheriting a false
`ENVO:00000021` freshwater-lake parent. The same modeling pattern applies
here, with `ENVO:01000057` as the marine bloom genus and `ENVO:00002150` as
location context to exclude from `parent_habitats`.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| HM-PHYTOPLANKTON-BLOOM-001 | Major | The record remains `UNGROUNDED` under a class-level "no ontology term fits" decision even though the vendored slice contains `ENVO:01000057` `marine algal bloom` under `ENVO:2000004` `algal bloom`. The source label alone is underspecified, but the full GOLD path says this is an aquatic marine coastal bloom; a minted coastal phytoplankton-bloom class can be grounded as narrower than `ENVO:01000057`. | Replace or override the class-level `CONFIRM_UNGROUNDED` row with an item-level decision for `habitatmech:GOLD.46309b7794` that records `ENVO:01000057` as the valid broader class. |
| HM-PHYTOPLANKTON-BLOOM-002 | Major | `parent_habitats` currently asserts `ENVO:00002150` `coastal sea water`, turning the water material where the bloom occurs into an is-a parent of the bloom. The exact GOLD path has no MIxS triad evidence; the `coastal sea water` term comes from the parent `Coastal` path and is contextual, not taxonomic. | Add a `curation/term_requests.tsv` row for the minted coastal phytoplankton-bloom term with `parent_class=ENVO:01000057` and `parent_mode=REPLACE`, or add an equivalent maintained parent override that prevents inherited `Coastal` water context from becoming a bloom parent. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Add item-level curation for `habitatmech:GOLD.46309b7794` that keeps the
   GOLD concept minted and records `ENVO:01000057` `marine algal bloom` as the
   reviewed broader parent.
2. Add a term request for a coastal phytoplankton-bloom class under
   `ENVO:01000057` with `parent_mode=REPLACE`; use the GOLD source label
   `Phytoplankton bloom` as an exact synonym rather than as the full primary
   label.
3. Regenerate with `just seed`, canary
   `habitatmech:GOLD.46309b7794`, and confirm
   `data/habitats/aquatic/phytoplankton_bloom.yaml` keeps the minted identity,
   gains a HabitatMech definition, switches to a reviewed narrow grounding
   under `ENVO:01000057`, and drops `ENVO:00002150` from
   `parent_habitats`.
4. Add an append-only history record for the curation edit, including the raw
   GOLD row, absence of exact-path MIxS rows, the ENVO algal-bloom terms, and
   the prior freshwater `algal_bloom` precedent.

## Follow-up Checks

- `just seed`
- `just seed-canary habitatmech:GOLD.46309b7794 --force`
- `just term-requests`
- `just seed-apply --force`
- `just validate data/habitats/aquatic/phytoplankton_bloom.yaml`
- `just validate-strict data/habitats/aquatic/phytoplankton_bloom.yaml --quiet`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `git diff --check`

After regeneration, re-read the target YAML and confirm:

- `identifier` remains `habitatmech:GOLD.46309b7794`;
- `label` is the requested coastal phytoplankton-bloom label;
- `definition_source` is `HabitatMech`;
- `grounding_status` is no longer `UNGROUNDED`;
- `parent_habitats` contains `ENVO:01000057` and no longer contains
  `ENVO:00002150`; and
- the source attestation still preserves `gold.ecosystem:5825`, the exact GOLD
  source path, and one organism assertion.

## Additional Notes

This was a read-only YAML review. It did not edit generated habitat YAML,
append curation history, promote review status, create an issue, or run paid
definition research.

The generated HTML page was not used as evidence; all assertions above were
traced to maintained TSV inputs, source inventory rows, the vendored ontology
slice, curation TSVs, prior YAML review reports, or the generated target YAML.

All absence searches described above included hidden and ignored files.
