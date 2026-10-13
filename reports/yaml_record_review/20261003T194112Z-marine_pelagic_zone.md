# YAML Record Review: marine pelagic zone

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/marine_pelagic_zone.yaml`
- Started UTC: 2026-10-03T19:39:46Z
- Finished UTC: 2026-10-03T19:41:12Z
- Verdict: needs curation

## Target

Read the complete generated HabitatRecord, `ENVO:00000208`, marine pelagic
zone, AQUATIC, EXACT, REVIEWED. GOLD and PREGO keys independently compute
to `habitatmech:GOLD.e089065baa` and `habitatmech:PREGO.47b019f5af`.
`data/habitats/PATHS.tsv:520` pins the filename.

## Validation

- `just validate data/habitats/aquatic/marine_pelagic_zone.yaml`: pass.
- `just validate-strict data/habitats/aquatic/marine_pelagic_zone.yaml`:
  one file, zero errors.
- Fresh full `just qc` was still running tests at review finish. Lint,
  documentation and provenance passed; later gates were not yet complete.
- Inspected current official ENVO target, parent and contextual triad terms;
  OWL fetched and byte-verified this batch, SHA-256
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
- All 25 current NCBI IDs resolve directly. All 24 supplied names match;
  the one optional blank name is faithfully retained. Structured comparison
  passed for each displayed PREGO row.
- OAK correspondence is deferred to required CI; it does not establish
  source-parent scope or ecological membership.

## Identity and Grounding

ID, label and definition match `data/raw/ontology_terms.tsv:6798` and
[official ENVO](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl).
`data/raw/ontology_subclass_edges.tsv:4841` and current OWL support
`ENVO:01000295` marine layer. That layer is part of a marine water body,
not a subclass of the whole body. The extra `ENVO:00001999` parent comes
from GOLD's Marine context through the second `ingest_gold` pass.

`curation/decisions.tsv:1245` and `:1437` are ITEM REVIEW decisions for
the two source keys. The generated histories faithfully explain REVIEWED;
this does not make the extra parent scientifically valid. The full marine
path and PREGO identifier support the exact identity merge. GOLD's source
label and PREGO's three related synonyms remain separately attributed.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:14` records nodes 3771/4021 and 4,877
organisms, with zero tree-level study/biosample counts. The YAML preserves
the first node, two-node note and ORGANISM count/unit.

Exact-path scans covered all 2,562 ecosystem rows, 1,040 bulk-count rows,
1,587 triad rows and 4,587 study rows:

- `data/raw/gold_path_biosamples.tsv:67`: node 4021, 525 bulk samples.
- `data/raw/gold_path_triads.tsv:641-643`: 296 API samples across 15
  studies. Broad marine biome has share 0.75/13 agreeing studies; local
  marine pelagic zone 0.58/nine; medium sea water 0.88/13. Distinct term
  counts are three, six and five respectively.
- Nineteen exact bulk study memberships occur at `data/raw/gold_studies.tsv`
  lines 994, 1030, 1039, 1162, 1240, 1344, 1375, 1829, 2255, 2562,
  2601, 2637, 2936, 3150, 3230, 4320, 4447, 4482 and 4494. Their
  identifiers and exact path memberships were inspected; live study
  contents were not independently read.

Bulk and API inventories are different snapshots, not interchangeable
counts. The local triad supports the zone interpretation without promoting
the broad biome or sampled water material to identity or a new is-a parent.

`data/raw/prego_habitats.tsv:266` gives 29 taxa, 29 direct assertions,
score 4 and annotated_genomes_isolates|environmental_samples. All 25
displayed entries at `data/raw/prego_habitat_taxa.tsv:4240-4264` match
IDs, optional names, scores, ranks 1-25 and pool 29. Each is direct TRUE
with no corroboration. The first two rows use annotated_genomes_isolates;
the other 23 use environmental_samples. The aggregate's two channels
must not be assigned to every displayed row. Four candidates remain unshown.

[NCBI Taxonomy efetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=110663,1123059,134561,1394,266940,28122,34085,36987,379066,411477,411485,428125,435805,445336,457427,498761,537937,562,56780,57043,583355,585501,595452,595453,641112)
confirms the displayed IDs and names without alias redirects. The blank
name for 36987 resolves to Coptotermes formosanus; that optional omission
does not break the identifier. None is marked is_characteristic. Original
genome/sample associations were not inspected, so this verifies source
projection and taxonomy, not characteristic ecology or every unusual
association's biological basis. GOLD organisms and PREGO taxa were not summed.

## Completeness

Ignored-inclusive ID, source-key, label and stem searches covered curation,
history, raw inventories, PATHS, research and individual reports. Both ITEM
decisions exist; no target term request, causal overlay, dedicated history
or prior individual target report was found. Child-record reports and
plankton research mentions are context, not this target's prior review or
independent scientific evidence.

Optional measurements, evidence, graphs, discussions and datasets are absent
and must not be invented from generic pelagic biology. iModulonDB is not
applicable: no gene, regulator, expression dataset or mechanism claim.

## Findings

Blockers: 0. Major: 1. Minor: 0.

**Major M1: zone classified as a whole marine water body.** Preserve the
true marine-layer parent while suppressing the unsupported GOLD contribution
to `ENVO:00001999`. Owners: governed source-specific parent handling in
`curation/` and `src/habitatmech/seed.py`, coordinated with draft #1218.
Tracked in [#1288](https://github.com/CultureBotAI/HabitatMech/issues/1288).

## Recommended Edits

Add only the narrow source-parent exclusion and regression. Preserve identity,
both source attestations, decisions, reviewed status and supported ancestry.
Append curation history for the actual change; do not hand-edit generated
YAML, remove a source, or conflate part-of with is-a.

## Follow-up Checks

Dry seed, inspect a canary, validate schema/history/OAK, reproduce the corpus,
regenerate affected map/site products and run full QC. #1217 remains the
supported-runtime regeneration dependency. Complete local QC and required CI
before report merge; report publication does not fix this scientific issue.

## Additional Notes

All 453 returned open/closed issues and their comments were searched before
filing #1288. No scientific input, generated record, page, status or history
changed; no other record is counted as reviewed here.
