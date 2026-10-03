# YAML Record Review: marine photic zone

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/marine_photic_zone.yaml`
- Started UTC: 2026-10-03T19:42:02Z
- Finished UTC: 2026-10-03T19:43:47Z
- Verdict: needs curation

## Target

Read the complete generated HabitatRecord, `ENVO:00000209`, marine photic
zone, AQUATIC, EXACT, REVIEWED. Independently computed source keys are
`habitatmech:GOLD.7d154f5642` and `habitatmech:PREGO.ecfad8372c`.
`data/habitats/PATHS.tsv:521` pins the filename.

## Validation

- `just validate data/habitats/aquatic/marine_photic_zone.yaml`: pass.
- `just validate-strict data/habitats/aquatic/marine_photic_zone.yaml`:
  one file, zero errors.
- Fresh full `just qc` was still running tests at review finish. Lint,
  documentation and provenance passed; later gates were not yet complete.
- Inspected current official ENVO target, its claimed parents, neritic
  contrast and offshore epipelagic biome; OWL fetched and byte-verified this
  batch, SHA-256
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
- All 25 current NCBI IDs resolve directly; all 24 supplied names match.
  The one optional blank label and every retained raw rank/score agree.
- OAK correspondence is deferred to required CI; labels alone do not prove
  hierarchy or source equivalence.

## Identity and Grounding

The canonical ID, label and definition match
`data/raw/ontology_terms.tsv:6799` and
[official ENVO](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl).
`data/raw/ontology_subclass_edges.tsv:4842` supports `ENVO:01000295`
marine layer. ENVO explicitly types PhoticZone and epipelagic zone as exact
synonyms; the independently sourced PREGO variants remain related. The
synonym-scope defect found in other records is not established here.

`curation/decisions.tsv:740` grounds GOLD Marine > Oceanic > Photic zone
exactly at ITEM depth; `:1516` is the PREGO ITEM REVIEW. The generated
histories and REVIEWED status faithfully reflect those decisions.

However, the generic ENVO/PREGO light-defined class inherits `ENVO:00000207`
oceanic zone from GOLD's path. That parent specifically excludes water over a
continental shelf. Marine photic zone does not have that horizontal
restriction; marine neritic zone is the contrasting shelf class. This is a
source-only constraint becoming universal generic ancestry.

[NOAA NCEI's photic-depth application](https://www.ncei.noaa.gov/waf/data-atlas-waf/products/html/environmentalPlates/CMECS_PhoticQualityLayerGuidance.htm)
describes euphotic depth in coastal and Gulf waters, varying with optical
conditions and sometimes reaching the bottom. This provides positive coastal
context, not merely an absent OWL edge. [NOAA's light-zone overview](https://oceanservice.noaa.gov/facts/light_travel.html)
uses an approximate upper-200-m convention; it does not justify adding a
universal depth measurement or an off-shelf boundary.

The GOLD exact-versus-narrow scope therefore needs reassessment. The present
review does not automatically split it or declare its Oceanic qualifier
irrelevant. Keep the generic PREGO identity distinct from that unresolved
source-specific equivalence question. An offshore biome is not a replacement
identity for a generic water-column zone.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:382` has one node, 4004, and 25 organisms,
with zero tree-level study/biosample counts. The 25 ORGANISM attestation and
lack of a multi-node note are correct.

Exact-path scans covered all 2,562 ecosystem rows, 1,040 bulk-count rows,
1,587 triad rows and 4,587 study rows:

- `data/raw/gold_path_biosamples.tsv:123`: 247 bulk samples for node 4004.
- `data/raw/gold_path_triads.tsv:629-631`: 211 API samples across 23
  studies. Broad marine biome has share 0.99/22 agreeing studies; local
  marine photic zone 0.52/17; medium sea water 0.63/20. Distinct term counts
  are two, two and three, respectively.
- Twenty-six bulk study memberships were inspected at `data/raw/gold_studies.tsv`
  lines 43, 53, 113, 239, 244, 267, 269, 294, 324, 333, 663, 698, 804,
  821, 981, 1155, 1255, 1402, 1444, 1543, 1795, 2028, 2310, 2312,
  4518 and 4520. Live study contents were not independently read.

The API and bulk inventories are different snapshots. A study's other path
memberships do not prove that a single sample is simultaneously coastal and
offshore. Triad roles remain separate; local label agreement does not settle
the exact-versus-narrow mapping or validate the generic offshore parent.
The abyssopelagic path's separate photic annotation is not target evidence.

`data/raw/prego_habitats.tsv:53` gives 1,607 taxa and 1,607 direct assertions,
maximum score 4 and both annotated_genomes_isolates/environmental_samples.
All 25 displayed entries at `data/raw/prego_habitat_taxa.tsv:4265-4289`
match IDs, optional names, scores, ranks 1-25 and pool 1,607. Direct flags
are TRUE and corroboration is empty. The first five use the genome/isolate
channel; the other 20 use environmental_samples. The remaining 1,582
candidates were not individually reviewed.

[NCBI Taxonomy efetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=110662,316279,59920,74546,74547,89184,86104,320388,372461,302409,332415,880447,880,198804,224915,515618,36870,340047,203907,264,357244,35845,293614,257363,205920)
confirms all IDs without alias redirects and all supplied names. The blank
35845 label resolves to Acetabularia acetabulum. None is marked
is_characteristic. Original genome/sample associations were not inspected;
taxonomy and source projection neither establish characteristic photic
ecology nor justify deleting unusual associations on name plausibility.
GOLD organisms and PREGO taxa were not summed.

## Completeness

Ignored-inclusive ID, source-key, label and stem searches covered curation,
history, raw inventories, PATHS, research and individual reports. Both ITEM
decisions exist; no target term request, causal overlay, dedicated history
or prior individual target report was found. Earlier epipelagic/abyssopelagic
reports are leads about other targets, not authoritative proof of this
record's scope or completed reviews of this target.

Optional measurements, evidence, graphs, discussions and datasets are absent
and must not be invented. iModulonDB is not applicable: no gene, regulator,
expression dataset or mechanism claim is present.

## Findings

Blockers: 0. Major: 1. Minor: 0.

**Major M1: source-only offshore restriction becomes generic ancestry.**
`ENVO:00000207` is not a universal superclass of the light-defined photic
zone. Reassess the GOLD decision's specificity and prevent its contextual
constraint from altering the generic ENVO/PREGO class. Owners: maintained
source decisions and/or scoped GOLD parent generation in `curation/` and
`src/habitatmech/seed.py`. Tracked in
[#1289](https://github.com/CultureBotAI/HabitatMech/issues/1289).

## Recommended Edits

Resolve exact-versus-narrow GOLD scope with item-level evidence; do not
automatically split merely to remove a parent. Retain PREGO identity, genuine
exact synonyms, separate source attributions and true marine-layer ancestry.
Use a narrowly governed source control, targeted regressions and append-only
history for the actual curation change; never hand-edit generated YAML.

## Follow-up Checks

Canary the resolved decision and inspect identity, attestations and parent
sets. Validate provenance/schema/history/OAK, reproduce corpus, regenerate
affected map/site products and run full QC. Do not bypass #1217's runtime
dependency or the separate draft #1218. Complete local QC and required CI
before report merge; report publication does not fix the scientific finding.

## Additional Notes

All 454 returned open/closed issues and comments were searched before filing
#1289. #1273 is the analogous aphotic-zone issue, not this target. No
scientific input, generated record, page, status or history changed.
