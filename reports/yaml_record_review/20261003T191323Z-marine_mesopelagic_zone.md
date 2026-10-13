# YAML Record Review: marine mesopelagic zone

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/marine_mesopelagic_zone.yaml`
- Started UTC: 2026-10-03T19:11:32Z
- Finished UTC: 2026-10-03T19:13:23Z
- Verdict: needs curation

## Target

Read the entire generated HabitatRecord, `ENVO:00000213`, marine mesopelagic
zone, AQUATIC, EXACT, REVIEWED. GOLD source key
`habitatmech:GOLD.76bc4edc73` and PREGO key `habitatmech:PREGO.33f83f4f4c`
feed the record. `data/habitats/PATHS.tsv:524` pins the stem.

## Validation

- `just validate data/habitats/aquatic/marine_mesopelagic_zone.yaml`: pass.
- `just validate-strict data/habitats/aquatic/marine_mesopelagic_zone.yaml`:
  one file, zero errors.
- Fresh full `just qc` had passed tests (455 passed, 3 skipped, 2 warnings),
  history (83), strict corpus (3,206), overlays (32), curation floor, exact
  reproduction, generated site, redirects and term requests. Its final
  corpus report was still active at review finish; no terminal full-QC
  result had yet been observed.
- Inspected current official ENVO identity, parents and contextual biome;
  OWL fetched and byte-verified this batch, SHA-256
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
- All four displayed NCBI IDs resolve directly, without aliases, and all
  names match. Structured CSV/YAML comparison confirms their source rows.
- OAK correspondence is deferred to required CI; it does not establish
  source-parent scope or original ecological evidence.

## Identity and Grounding

ID, label and full definition match `data/raw/ontology_terms.tsv:6803` and
[official ENVO](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl).
`data/raw/ontology_subclass_edges.tsv:4846` supports `ENVO:00000210` marine
aphotic zone as the named superclass. `ENVO:00001999` marine water body is
an extra GOLD-derived parent: a water-column zone is not the whole lentic
water body. Preserve the ontology axiom while removing that source-context
is-a claim.

`curation/decisions.tsv:702` is an ITEM GROUND/EXACT decision for Marine >
Mesopelagic; `:1420` is the PREGO ITEM REVIEW. Both source identities agree
with the target, and their histories explain REVIEWED. This review does
not promote status or reinterpret the separate organism and taxon counts.

ENVO uses a thermal lower boundary and a photosynthesis-based aphotic
definition. The inspected
[NOAA mesopelagic transcript](https://oceantoday.noaa.gov/fullmoon-mysteriesofthemesopelagic/)
uses approximately 200-1,000 m, while
[NOAA's light-zone description](https://oceanservice.noaa.gov/facts/light_travel.html)
calls that range dysphotic and reserves aphotic for deeper water. These
conventions are not interchangeable. Preserve this difference rather than
silently replacing the current ontology parent/definition, adding universal
depth measurements, or declaring the whole-waterbody parent valid.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:339` records nodes 5332/5333, 34 organisms
and zero tree-level study/biosample counts. The first node, two-node note and
34 ORGANISM assertions are correctly projected. The GOLD source label is
retained as an exact synonym within its path; PREGO's three alternate strings
are independently related synonyms.

Structured exact-path scans covered 2,562 ecosystem rows, 1,040 bulk-count
rows, 1,587 triad rows and 4,587 study rows. The supporting rows are:

- `data/raw/gold_path_biosamples.tsv:227`: node 5333, 104 bulk samples.
- `data/raw/gold_path_triads.tsv:581-583`: 104 API samples across eight
  studies. Broad `ENVO:01000036` oceanic mesopelagic zone biome has share
  1.00/eight agreeing studies; local `ENVO:00000213` has share 0.99/seven
  agreeing studies and two distinct local terms; medium `ENVO:00002149`
  sea water has share 1.00/eight agreeing studies.
- `data/raw/gold_studies.tsv` exact memberships: Gs0121483 (1344), Gs0121717
  (1379), Gs0133511 (1994), Gs0141831 (2251), Gs0145237 (2920), Gs0145253
  (2936), Gs0150723 (3535), Gs0151931 (3583). Their total path counts are
  respectively 4, 4, 10, 4, 4, 3, 3 and 1. Live study contents were not read.

The local annotation supports the zone interpretation; the offshore biome
and sampled water remain different claim roles. Neither becomes an exact
replacement identity or additional parent merely by appearing in the triad.
Bulk/API counts and organism assertions were not summed.

`data/raw/prego_habitats.tsv:416` gives four taxa/direct assertions, maximum
score 4 and annotated_genomes_isolates. All four candidates at
`data/raw/prego_habitat_taxa.tsv:4303-4306` are displayed. IDs, names, scores,
ranks 1-4 and pool 4 agree; direct flags are TRUE and corroboration absent.
No row is marked is_characteristic.

[NCBI efetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=939306,939316,939324,939346)
confirms the four SCGC alpha-proteobacterium identifiers and displayed
strain-like names. The original genome/sample associations were not inspected;
valid taxonomy and faithful projection are not proof of characteristic ecology.

## Completeness

Ignored-inclusive ID, source-key, label, stem and full-path searches covered
curation, history, raw inventories, PATHS, research and individual reports.
The two decisions are present, but no target term request, causal overlay,
dedicated history or prior individual target report was found. Research
mentions were leads, not independent biological evidence.

Optional measurements, evidence objects, graphs, discussions and datasets
are absent and cannot be filled from general water-column biology. iModulonDB
is not applicable: no gene, regulator, expression dataset or mechanism claim.

## Findings

Blockers: 0. Major: 1. Minor: 0.

**Major M1: water-column zone inherits a whole-waterbody parent.** The
GOLD parent-path contribution to `ENVO:00001999` is not a strict is-a
relation. Owners: governed source-specific parent handling in `curation/`
and `src/habitatmech/seed.py`, coordinated with draft #1218. Tracked in
[#1285](https://github.com/CultureBotAI/HabitatMech/issues/1285).

## Recommended Edits

Exclude only the unsupported GOLD parent contribution. Retain
`ENVO:00000210`, exact identity, both ITEM decisions, source attestations,
taxa and derived REVIEWED status. Add a targeted regression and append
curation history for an actual input change; never hand-edit generated YAML.
Treat the differing ENVO/NOAA boundary conventions as a separate upstream
scope question, not an automatic local replacement rule.

## Follow-up Checks

Dry seed and inspect a canary, validate schema/history/OAK, reproduce the
corpus and regenerate affected semantic-map/site products. Respect #1217's
supported-runtime blocker; do not bypass freshness checks. Complete full
local QC and all required CI before publishing the report.

## Additional Notes

All 451 returned open/closed issues and comments were searched before filing
#1285. No scientific input, generated record, page, status or history changed.
The parent defect is independent of the supported identity merge and source
counts; fixing it should not discard either source.
