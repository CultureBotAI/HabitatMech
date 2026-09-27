# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/coastal_sea_water.yaml`
- Started UTC: 2026-09-27T03:36:00Z
- Finished UTC: 2026-09-27T03:47:49Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `ENVO:00002150` |
| Label | `coastal sea water` |
| Class | `HabitatRecord` |
| Category | `AQUATIC` |
| Generated or maintained | Generated from `data/raw/`, `curation/decisions.tsv`, and `data/habitats/PATHS.tsv`; do not hand-edit |
| Current grounding | `EXACT` |
| Current mapping | `REVIEWED` |

The target resolves exactly one generated YAML file and one slug:
`data/habitats/aquatic/coastal_sea_water.yaml`. `data/habitats/PATHS.tsv`
pins `ENVO:00002150` to `coastal_sea_water`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/coastal_sea_water.yaml` | Pass: LinkML reported `No issues found`. |
| `just validate-all data/habitats/aquatic/coastal_sea_water.yaml` | Pass: 1 file scanned, 0 files with errors, 0 error rows. |
| `just validate-strict data/habitats/aquatic/coastal_sea_water.yaml --quiet` | Pass: 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just validate-causal-all` | Pass: 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Pass: committed term-request table is current with 109 terms. |
| `just validate-history` | Pass: 77 history records valid against `src/habitatmech/schema/history.yaml`. |
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist.tsv` | Pass: regenerated a 953-row ungrounded worklist outside the repository. |
| `just verify-corpus --max-diffs 1` | Pass: 3,206 expected records, 3,206 found, 0 missing, 0 extra, 0 differing. |
| `just report` | Pass: completed the corpus diagnostic report without surfacing a global issue for this target. |

No documented validator was skipped.

## Identity and Grounding

The record identity is correct. `data/raw/ontology_terms.tsv` contains
`ENVO:00002150` `coastal sea water` with the definition copied into the record,
and `data/raw/ontology_subclass_edges.tsv` makes it a direct subclass of
`ENVO:00002149` `sea water`. `data/raw/prego_habitats.tsv` contributes the
same ontology identifier with 812 PREGO taxon assertions, score 4.0, and the
`annotated_genomes_isolates|environmental_samples` evidence channels;
`curation/decisions.tsv` has an item-level `REVIEW` row endorsing that PREGO
self-grounding.

The three GOLD paths that merge into the ENVO record all have item-level
`CLOSE` decisions:

| Source concept | GOLD path | Raw support | Decision |
|---|---|---|---|
| `habitatmech:GOLD.1a3d0aff0c` | `Environmental > Aquatic > Marine > Coastal` | Two GOLD node IDs, 1,718 organism assertions, 4,109 GOLD API biosamples, 106 exact GOLD studies, and a MIxS medium triad whose top term is `ENVO:00002150` across 2,011 samples and 64 studies. | `GROUND` to `ENVO:00002150` with `CLOSE`: the GOLD node is the coastal zone and ENVO names the water material. |
| `habitatmech:GOLD.89754b31f3` | `Environmental > Aquatic > Marine > Neritic zone/Coastal water` | Two GOLD node IDs, 68 organism assertions, 247 GOLD API biosamples, 15 exact GOLD studies, and MIxS triads whose local and medium terms are `ENVO:00000206` `marine neritic zone` and `ENVO:00002149` `sea water`. | `GROUND` to `ENVO:00002150` with `CLOSE`: the neritic zone is the region and ENVO names the water material. |
| `habitatmech:GOLD.ad324e6267` | `Environmental > Aquatic > Marine > Littoral zone > Neritic zone/Coastal water` | One GOLD node ID, seven organism assertions, 48 GOLD API biosamples, one exact GOLD study, and MIxS triads whose local and medium terms are `ENVO:00000206` `marine neritic zone` and `ENVO:00002149` `sea water`. | `GROUND` to `ENVO:00002150` with `CLOSE`: the neritic zone is the region and ENVO names the water material. |

Those `CLOSE` decisions are faithful source attestations, but two inherited
parents are not strict broader classes of the merged ENVO water-material
record:

- `ENVO:00001999` `marine water body` comes from the common GOLD parent
  `Environmental > Aquatic > Marine`; it denotes a body, not the sea-water
  material in the body.
- `ENVO:01000125` `marine littoral zone` comes from the exact GOLD parent
  `Environmental > Aquatic > Marine > Littoral zone`; it denotes a zone, not
  the coastal water material within a zone.

`ENVO:00002149` `sea water` is the only valid current broader parent.

## Evidence

The ENVO definition, ENVO synonyms, PREGO related synonyms, PREGO source
attestation, and all 25 generated PREGO taxon rows are copied from the vendored
ontology and `data/raw/prego_*` source rows.

The GOLD source attestations are copied from `data/raw/gold_ecosystem_paths.tsv`
and agree with their maintained decision rows. The source IDs
`gold.ecosystem:3780`, `gold.ecosystem:3781`, and `gold.ecosystem:7912` are the
first node IDs for their exact GOLD paths, the organism assertion counts match
the collapsed GOLD inventory, and the two multi-node paths correctly carry the
generated note explaining that the first GOLD node ID is shown.

The generated GOLD synonyms are over-scoped. `src/habitatmech/seed.py`
currently adds every GOLD leaf label as an `EXACT_SYNONYM` before curation
decisions turn the same source concepts into `skos:closeMatch` attestations.
Here that makes `Coastal` and `Neritic zone/Coastal water` exact synonyms for
`coastal sea water`, even though all three item-level decisions explicitly say
the GOLD nodes denote a zone or region and only closely match ENVO's water
material.

## Completeness

The record has no curator-authored `evidence`, `causal_graphs`, `discussions`,
or `datasets`; those slots are correctly empty for the current maintained
inputs.

Exact hidden- and ignored-file-inclusive searches of
`reports/yaml_record_review`, `research/habitats`, `curation/causal_graphs`,
`history`, `curation/term_requests.tsv`, `curation/term_requests_excluded.tsv`,
`curation/external_xrefs.tsv`, `conf/id_label_targets.yaml`, and
`reports/habitat_research_manifest.tsv` found no prior review, no target-owned
research report, no causal overlay, no history entry, no term request,
no term-request exclusion, no external xref, and no id-label target row for
`data/habitats/aquatic/coastal_sea_water.yaml`, `coastal_sea_water`,
`habitatmech:GOLD.1a3d0aff0c`, `habitatmech:GOLD.89754b31f3`,
`habitatmech:GOLD.ad324e6267`, or `habitatmech:PREGO.0da0bcd805`.

The earlier Brine review already found the same source-path-parent failure from
the child side: `Environmental > Aquatic > Marine > Coastal > Brine` inherits
`ENVO:00002150` from the `Coastal` path even though coastal brine is not a kind
of coastal sea water. The same generator behavior gives `coastal sea water`
body and zone parents in this record.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| HM-COASTAL-SEA-WATER-001 | Major | `parent_habitats` says `coastal sea water` is a subclass of both `ENVO:00001999` `marine water body` and `ENVO:01000125` `marine littoral zone`. The ENVO ontology only places `ENVO:00002150` under `ENVO:00002149` `sea water`; the extra generated parents come from close-matched GOLD path contexts and turn "found under this body or zone in GOLD" into a false is-a edge from a water material to a body or zone. | Add a maintained parent-edge override or equivalent source-path relation table, then make `src/habitatmech/seed.py` consult it before adding inherited GOLD parent paths as `parent_habitats`. |
| HM-COASTAL-SEA-WATER-002 | Major | `Coastal` and `Neritic zone/Coastal water` are emitted as `EXACT_SYNONYM` rows even though the item-level GOLD decisions only ground those source concepts with `CLOSE`. This loses the curated distinction that the GOLD concepts denote zones or regions while the ENVO record denotes a water material. | `src/habitatmech/seed.py` |

No blocker findings.

No minor findings.

## Recommended Edits

1. Add a maintained override for the false source-path parent edges that make
   `ENVO:00002150` inherit `ENVO:00001999` and `ENVO:01000125`, or add an
   equivalent seeder rule that only inherits a GOLD parent path when the
   resolved parent is truly broader than the resolved child record.
2. Update GOLD synonym generation in `src/habitatmech/seed.py` so leaf labels
   from `skos:closeMatch` source attestations are not emitted as
   `EXACT_SYNONYM` values. Either suppress those close labels as synonyms or
   emit them at a weaker scope that preserves the `CLOSE` decision.
3. Run the dry-run `just seed`, regenerate the target with
   `just seed-canary ENVO:00002150 --force`, and inspect the target before any
   wider `just seed-apply --force` run.

## Follow-up Checks

- `just seed`
- `just seed-canary ENVO:00002150 --force`
- `just validate data/habitats/aquatic/coastal_sea_water.yaml`
- `just validate-strict data/habitats/aquatic/coastal_sea_water.yaml --quiet`
- `just verify-corpus --max-diffs 1`
- `just report`
- `git diff --check`

After regeneration, re-read `data/habitats/aquatic/coastal_sea_water.yaml` and
confirm that:

- `parent_habitats` keeps `ENVO:00002149` and drops `ENVO:00001999` and
  `ENVO:01000125`;
- GOLD source attestations still carry `skos:closeMatch`;
- close GOLD source labels are no longer exact synonyms of `coastal sea water`;
  and
- the record remains `EXACT` and `REVIEWED`.

## Additional Notes

This was a read-only YAML review. It did not edit generated habitat YAML, append
curation history, promote review status, create an issue, or run paid
definition research.

The generated HTML page was not used as evidence; all assertions above were
traced to maintained TSV inputs, source inventory rows, the vendored ontology
slice, `src/habitatmech/seed.py`, or the generated target YAML.
