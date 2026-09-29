# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/terrestrial/agricultural_soil.yaml`
- Started UTC: 2026-09-29T03:32:17Z
- Finished UTC: 2026-09-29T03:32:17Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `HabitatRecord` |
| Identifier | `ENVO:00002259` |
| Label | `agricultural soil` |
| Category | `TERRESTRIAL` |
| Grounding | `EXACT` |
| Mapping | `SEEDED` |
| Sources | `ENVIRONMENTS_TABLE`, `GOLD`, `MADIN`, `PREGO` |
| Generated path | `data/habitats/terrestrial/agricultural_soil.yaml` |
| Stable slug | `agricultural_soil` |
| Causal overlay | `curation/causal_graphs/agricultural_soil.yaml` |
| Maintained owner | The only unsupported assertion is inherited from the reviewed GOLD source concept `habitatmech:GOLD.842c30e44d` in `curation/decisions.tsv`. |

Reviewed the complete generated record at
`data/habitats/terrestrial/agricultural_soil.yaml`, plus its maintained causal
overlay at `curation/causal_graphs/agricultural_soil.yaml`.

`data/habitats/PATHS.tsv` maps the ontology identifier `ENVO:00002259` to the
stable `agricultural_soil` slug.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/habitats/terrestrial/agricultural_soil.yaml` | Pass: LinkML reported `No issues found`. |
| `just validate-strict data/habitats/terrestrial/agricultural_soil.yaml` | Pass: scanned 1 file with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| `just validate-causal curation/causal_graphs/agricultural_soil.yaml` | Pass: LinkML reported `No issues found`. |
| `just validate-causal-all` | Pass: validated 32 causal-graph curation files with 32 graphs. |
| `just term-requests-check` | Pass: the term-request table is current with 109 terms. |
| `just validate-history` | Pass: 77 history records were valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Pass: expected 3,206 records, found 3,206 on disk, and the corpus reproduces exactly from `data/raw/`. |
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist-agricultural-soil.tsv` | Pass: wrote 953 total `UNGROUNDED` rows across all decision states with 1,810 decisions on file. |
| `just report --out /tmp/habitatmech-report-agricultural-soil.tsv` | Pass: completed the corpus report for 3,206 records. |
| `git diff --check` | Pass before writing this report. |

## Identity and Grounding

The generic ENVO identity is well supported by three of the four contributing
source surfaces.

- The vendored ontology slice defines `ENVO:00002259` `agricultural soil` as
  `Soil which is part of an ecosystem used for agricultural activities.`
- `data/raw/environment_parameters.tsv:645-654` has ten exact
  `soil_agricultural` rows mapped to `ENVO:00002259` with the expected
  agricultural-soil label.
- `data/raw/madin_habitats.tsv:35` maps MADIN `ENVO:00002259` to the same
  agricultural-soil label with 117 taxon assertions.
- `data/raw/prego_habitats.tsv:45` maps PREGO `ENVO:00002259` to the same ENVO
  class, carries 1,767 taxon assertions, and preserves the plural synonym
  `agricultural soils`.

The GOLD contribution is narrower than this identity. The reviewed GOLD source
concept is `habitatmech:GOLD.842c30e44d`, which mints from the exact path
`Environmental > Terrestrial > Soil > Loam > Agricultural soil`.
`curation/decisions.tsv:784` currently `REVIEW`s the seeder's exact grounding
of that path to generic `ENVO:00002259`, but the GOLD source path constrains
the node to agricultural soil under a loam parent.

The false broadened merge has a visible parent-side effect. The ontology slice
has parallel `rdfs:subClassOf` edges from `ENVO:00002258` `loam` to
`ENVO:00001998` `soil` and from `ENVO:00002259` `agricultural soil` to
`ENVO:00001998`; it does not assert `agricultural soil` as a subclass of
`loam`. The generated record nevertheless has both `ENVO:00001998` and
`ENVO:00002258` under `parent_habitats` because the second GOLD ingest pass
copies the resolved identifier of each source path's immediate parent into the
child record.

The curated causal graph is traceable. The generated
`agricultural_nitrogen_nitrification_loss` graph matches
`curation/causal_graphs/agricultural_soil.yaml` and carries the intended
evidence references, `PMID:31543867`, `PMID:29398704`, and `PMID:22936929`, on
the generated edge-level evidence blocks.

## Evidence

Supported:

- `data/raw/ontology_terms.tsv:7335` supplies the ENVO label and definition.
- The ENVIRONMENTS_TABLE attestation and all ten generated
  `environmental_parameters` rows reproduce the committed `soil_agricultural`
  rows in `data/raw/environment_parameters.tsv`.
- The PREGO source attestation reproduces the `ENVO:00002259` summary row with
  1,767 taxon assertions, score `3.0`, and the
  `annotated_genomes_isolates|environmental_samples` channel string.
- The generated PREGO `characteristic_taxa` block keeps ranks 1-25 from the
  contiguous `data/raw/prego_habitat_taxa.tsv` rows for `ENVO:00002259`.
- The MADIN source attestation reproduces the `ENVO:00002259` source row with
  117 taxon assertions.
- The generated MADIN `characteristic_taxa` block keeps the first 25 MADIN
  rows for `ENVO:00002259`; the first 14 are correctly marked as corroborated
  by PREGO in `data/raw/madin_habitat_taxa.tsv`.
- The GOLD source attestation reproduces
  `data/raw/gold_ecosystem_paths.tsv:236`: source ID `gold.ecosystem:4244`,
  exact source path `Environmental > Terrestrial > Soil > Loam > Agricultural
  soil`, and 77 direct organism assertions.
- The exact GOLD path has side-channel support in
  `data/raw/gold_path_biosamples.tsv:423`, three study rows in
  `data/raw/gold_studies.tsv`, and a three-slot MIxS triad block in
  `data/raw/gold_path_triads.tsv:1040-1042`.
- The curated overlay's `curation_history` records the 2026-09-04
  agricultural nitrification graph addition, and the generated record carries
  the same graph and graph-level history entry.

Unsupported or over-scoped:

- The reviewed GOLD `Environmental > Terrestrial > Soil > Loam > Agricultural
  soil` source path is not exact to the broader ENVO class for any agricultural
  soil.
- The generated `ENVO:00002258` `loam` parent applies to the narrower GOLD
  source path, not to the generic ENVO agricultural-soil record that also
  absorbs ENVIRONMENTS_TABLE, MADIN, and PREGO attestations.

## Completeness

`find reports/yaml_record_review -maxdepth 1 -type f -name
'*agricultural_soil.md' -print` found no prior top-level YAML report for this
file stem. `find` is not filtered by `.gitignore`.

Exact ignored/hidden-inclusive searches found:

- no prior top-level report, append-only history record, or research report for
  `habitatmech:GOLD.842c30e44d` or the exact GOLD path
  `Environmental > Terrestrial > Soil > Loam > Agricultural soil`;
- no previous top-level report for `ENVO:00002259` or the `agricultural_soil`
  slug;
- the maintained PREGO and GOLD `REVIEW` rows in `curation/decisions.tsv`;
- no maintained decision row for the exact
  `habitatmech:ENVIRONMENTS_TABLE.d7b81423f4` or
  `habitatmech:MADIN.c57efd458e` source keys; and
- prior agricultural-land reports that mention `ENVO:00002259` only as MIxS
  medium-slot evidence for separate GOLD agricultural-land records.

The causal-graph search found only the maintained overlay and the generated
copy in this record for `agricultural_nitrogen_nitrification_loss` and its
three PMID references.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The GOLD source concept under `Loam` is reviewed as exact to generic `agricultural soil`, which leaks `ENVO:00002258` `loam` onto the merged ENVO record as a strict parent. | `curation/decisions.tsv:784` `REVIEW`s `habitatmech:GOLD.842c30e44d`; that source concept is `Environmental > Terrestrial > Soil > Loam > Agricultural soil`, not all agricultural soil. The vendored ontology gives `ENVO:00002258` and `ENVO:00002259` as sibling subclasses of `ENVO:00001998` `soil`, while the generated record publishes both `soil` and `loam` as parents for the generic ENVO record. | Replace the GOLD `REVIEW` row in `curation/decisions.tsv` with a decision that keeps the loam-specific GOLD concept minted under true broader parents, such as `GROUND_AS_PARENT` to `ENVO:00002259` with the source-path `Loam` parent retained on the minted child. |

No blocker findings found.

No minor findings found.

## Recommended Edits

1. Replace the `habitatmech:GOLD.842c30e44d` `REVIEW` row in
   `curation/decisions.tsv` with an `ITEM` decision that treats the GOLD source
   as narrower than generic `ENVO:00002259`.
2. Seed a canary for `habitatmech:GOLD.842c30e44d` and confirm the GOLD source
   no longer merges directly into `ENVO:00002259`.
3. Confirm `data/habitats/terrestrial/agricultural_soil.yaml` keeps the
   ENVIRONMENTS_TABLE, MADIN, PREGO, environmental-parameter,
   characteristic-taxon, and causal-graph content while dropping
   `ENVO:00002258` from `parent_habitats`.
4. Confirm the new minted GOLD child keeps `gold.ecosystem:4244`, the exact
   `Environmental > Terrestrial > Soil > Loam > Agricultural soil` source path,
   77 organism assertions, and true broader parents for loam and agricultural
   soil.
5. Record the decision edit in an append-only mapping history file with
   `just new-history`, then re-seed with `just seed`,
   `just seed-canary habitatmech:GOLD.842c30e44d`, and
   `just seed-apply --force`.

## Follow-up Checks

| Edit | Proof |
| --- | --- |
| Re-decide the loam-specific GOLD source | `rg --no-ignore --hidden -n '^habitatmech:GOLD\\.842c30e44d\\b' curation/decisions.tsv` should show an `ITEM` decision whose note explicitly rejects exact identity to all agricultural soil. |
| Preserve the broad ENVO record | Inspect `data/habitats/terrestrial/agricultural_soil.yaml` after `just seed-canary ENVO:00002259`; it should keep `ENVIRONMENTS_TABLE`, `MADIN`, and `PREGO` attestations, ten environmental parameters, 50 characteristic taxa, and the `agricultural_nitrogen_nitrification_loss` graph. |
| Remove the false loam parent | The same canary should keep `ENVO:00001998` in `parent_habitats` and should not emit `ENVO:00002258` on the generic ENVO agricultural-soil record. |
| Preserve the loam-specific GOLD evidence | A canary for `habitatmech:GOLD.842c30e44d` should carry `source_id: gold.ecosystem:4244`, `source_path: Environmental > Terrestrial > Soil > Loam > Agricultural soil`, and `assertion_count: 77`. |
| Keep the generated corpus reproducible | Run `just verify-corpus --max-diffs 1`, `just validate data/habitats/terrestrial/agricultural_soil.yaml`, `just validate-strict data/habitats/terrestrial/agricultural_soil.yaml`, `just validate-causal-all`, `just term-requests-check`, `just validate-history`, `just report`, `just worklist --status all`, and `git diff --check`. |

## Additional Notes

The exact absence searches above included ignored and hidden files. They were
bounded to the committed raw tables and maintained curation surfaces that could
plausibly own this target.

The `Loam > Agricultural soil` defect is a specific instance of a broader
hazard with source-path parents on ontology-grounded GOLD records. When a
narrow source concept merges into a broader ontology record, copying the GOLD
source parent onto the resolved ontology identifier can convert source context
into a false universal parent edge.
