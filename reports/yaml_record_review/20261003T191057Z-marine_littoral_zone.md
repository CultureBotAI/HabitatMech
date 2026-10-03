# YAML Record Review: marine littoral zone

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/marine_littoral_zone.yaml`
- Started UTC: 2026-10-03T19:09:09Z
- Finished UTC: 2026-10-03T19:10:57Z
- Verdict: needs curation

## Target

Read the entire generated HabitatRecord, `ENVO:01000125`, marine littoral
zone, AQUATIC, EXACT, SEEDED. Sole source: GOLD Environmental > Aquatic >
Marine > Littoral zone, computed key `habitatmech:GOLD.2a3e25f443`.
`data/habitats/PATHS.tsv:778` pins the stem. Only a deterministic seed event
is present; there is no ITEM decision for this source concept.

## Validation

- `just validate data/habitats/aquatic/marine_littoral_zone.yaml`: pass.
- `just validate-strict data/habitats/aquatic/marine_littoral_zone.yaml`:
  one file, zero errors.
- Fresh full `just qc` remained active at review finish. Tests passed:
  455 passed, 3 skipped, 2 warnings. History (83), strict corpus (3,206),
  overlays (32), curation floor and exact reproduction passed. Generated-site
  and later gates were not yet confirmed complete.
- Inspected current official ENVO target and parents; OWL was fetched and
  byte-verified this batch, SHA-256
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
- No displayed taxon IDs require resolution. OAK correspondence is deferred
  to required CI; it does not verify source-parent scope or spelling.

## Identity and Grounding

ID, canonical label and full definition match
`data/raw/ontology_terms.tsv:7631` and
[official ENVO](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl).
`data/raw/ontology_subclass_edges.tsv:5775` and current OWL support
`ENVO:01000407` littoral zone as the named superclass. This marine zone has
an intertidal part but is not identical to intertidal zone.

The extra `ENVO:00001999` marine-waterbody parent comes from GOLD's Marine
context in the second `ingest_gold` pass. The target includes the spray
region above high tide; it is a shore-associated zone, not a whole lentic
marine water body. Source hierarchy is not sufficient evidence for is-a.

The inherited definition also contains coninental rather than continental.
The same spelling occurs in current ENVO; this is upstream wording, not a
local serializer error. The approximate geographic extent must not be changed
silently while repairing the spelling.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:715` records nodes 7907 and 7909, three
organisms, and zero tree-level study/biosample counts. The YAML faithfully
shows node 7907, the two-node note, and 3 ORGANISM assertions. GOLD's
Littoral zone synonym remains source-attributed within its marine path;
it is not evidence that every nonmarine littoral zone has this identity.

Structured exact-path scans covered all 1,040 bulk-count rows, 1,587 triad
rows and 4,587 study rows. None matches the target path. The child Neritic
zone/Coastal water has separate evidence: seven organisms, 48 bulk samples
and one committed study membership. Those are not the parent's counts.
Other child paths likewise do not justify adding measurements, taxa or
independent-source corroboration to this record.

Identity resolution is compatible with the full Marine > Littoral zone
path and current ENVO label. SEEDED appropriately distinguishes this lexical
resolution from an ITEM review. No curator-endorsed source equivalence is
implied by the report's checks.

## Completeness

Ignored-inclusive searches for ID, source key, label, stem and full path
covered curation, history, raw inventories, PATHS, research and individual
reports. No target ITEM decision, term request, causal overlay, dedicated
history or prior individual target review was found. Child decisions and
contextual mentions in other reports were not counted as this review.

Optional parameters, taxa, evidence, graphs, discussions and datasets are
absent and must not be invented from generic littoral biology. iModulonDB is
not applicable: no gene, regulator, expression dataset or mechanism is claimed.

## Findings

Blockers: 0. Major: 1. Minor: 1.

1. **Major M1: zone classified as a whole marine water body.** Suppress the
   unsupported GOLD parent contribution while retaining the true littoral
   superclass and all source provenance. Owners: governed source-specific
   controls in `curation/` and `src/habitatmech/seed.py`, coordinated with
   draft #1218. Tracked in
   [#1283](https://github.com/CultureBotAI/HabitatMech/issues/1283).
2. **Minor m1: upstream definition typo.** Correct coninental through ENVO
   and the governed ontology refresh, not by hand-editing generated YAML.
   Owners: upstream definition, ontology inventory and extraction. Tracked in
   [#1284](https://github.com/CultureBotAI/HabitatMech/issues/1284).

## Recommended Edits

Add the narrow source-parent exclusion/regression and append curation history
when that input is changed. Preserve `ENVO:01000407`, exact identity, both
GOLD nodes, source label and count/unit. Coordinate the separate typo repair
with the upstream source; it must not redefine the zone or alter child counts.

## Follow-up Checks

Dry seed, inspect a canary, validate schema/history/OAK and reproduce the
corpus. Regenerate affected semantic map/site products and run full QC.
The supported-runtime map blocker #1217 remains relevant to publication of
scientific changes. Complete local QC and all required CI for this report PR.

## Additional Notes

All 449 returned open/closed issues and comments were searched before filing.
#1254 concerns a different child intertidal-to-whole-littoral relation; it
does not resolve this record's zone-to-waterbody edge. No scientific input,
generated record, page, status or history changed.
