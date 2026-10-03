# YAML Record Review: marine reef biome

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/marine_reef_biome.yaml`
- Started UTC: 2026-10-03T19:47:11Z
- Finished UTC: 2026-10-03T19:48:32Z
- Verdict: pass with minor issues

## Target

Read the entire generated HabitatRecord, `ENVO:01000029`, marine reef biome,
AQUATIC, EXACT, SEEDED. PREGO is the only source; computed key
`habitatmech:PREGO.e73691319d`. `data/habitats/PATHS.tsv:762` pins the
filename. The lone seed event is not an ITEM review.

## Validation

- `just validate data/habitats/aquatic/marine_reef_biome.yaml`: pass.
- `just validate-strict data/habitats/aquatic/marine_reef_biome.yaml`:
  one file, zero errors.
- Fresh full `just qc` passed tests (455 passed, 3 skipped, 2 warnings),
  history (83), strict corpus (3,206), overlays (32), curation floor, exact
  reproduction, generated site, redirects and term requests. Its final
  corpus report was still running at review finish; no terminal full-QC
  result had yet been observed.
- Inspected target and parent in current official ENVO OWL, fetched and
  byte-verified this batch, SHA-256
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
- Queried current NCBI again for this record: 24 direct IDs and one alias
  redirect; all 24 supplied names match. Each own-source raw row was compared
  independently with the YAML.
- OAK correspondence is deferred to required CI; its scope does not cover
  the PREGO taxon alias or original ecological associations.

## Identity and Grounding

ID, label, definition and sole named parent `ENVO:01000024` marine benthic
biome agree with `data/raw/ontology_terms.tsv:7540`,
`data/raw/ontology_subclass_edges.tsv:5670` and
[official ENVO](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl).
The target is a biome, not the reef feature `ENVO:01000143` or a reef-building
host organism. The ontology's part-of/determined-by restrictions involving
the feature are not exact-identity or is-a statements. The two PREGO aliases
remain related.

The current definition explicitly describes reefs rising near the water
surface. [NOAA's deep-sea coral tutorial](https://oceanservice.noaa.gov/education/tutorial_corals/media/supp_coral05b.html)
describes a reef at depth, so an unrestricted all-depth reading is not
justified by this definition. Preserve that upstream scope boundary; faithful
copying alone is not an endorsement of the term for every reef ecosystem.
No unsupported replacement identity or local definition rewrite follows.

## Evidence

`data/raw/prego_habitats.tsv:180` reports 112 taxa, 112 direct assertions,
maximum score 4 and environmental_samples. The YAML's TAXON aggregate,
score and channel agree. All 25 rows at
`data/raw/prego_habitat_taxa.tsv:7430-7454` match IDs, optional names,
score 4, ranks 1-25 and pool 112. Each direct flag is TRUE, channel is
environmental_samples and corroboration is empty. None is marked
is_characteristic; 87 other candidates were not individually reviewed.

[NCBI Taxonomy efetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=102,1026,103810,104268,104270,1044,107401,1080,111770,114404,119542,1217908,133924,143224,150120,158080,161528,168275,172371,173737,184914,188906,188908,197222,200617)
directly resolves 24 IDs and confirms their supplied scientific names. Rank
16 uses 158080 with no optional label in either raw input or YAML. The
response resolves it to 141390 Chromohalobacter israelensis and includes
158080 in AkaTaxIds, consistent with the separately inspected single-ID
response. This is a resolvable legacy alias, not a broken reference.

Structured comparison confirms that the reef-feature record has an identical
displayed taxon vector. The two PREGO concept rows are not independent
corroboration and do not establish equivalence of feature and biome. Original
environmental-sample evidence was not inspected, including whether its usage
respects the near-surface scope. Taxonomy/source projection is the verified
claim, not characteristic ecology.

`data/raw/gold_path_triads.tsv:1232`, `:1238`, `:1241` and `:1331` use
the target as broad scale for green algae, mixed algae turf, red algae and
coral tissue. These are host-sampling contexts, not additional attestations
for this PREGO-only biome. Their counts are not added to the TAXON aggregate.

## Completeness

Ignored-inclusive searches covered ID, source key, label and stem in curation,
history, raw inventories, PATHS, research and individual reports. No target
ITEM decision, term request, causal overlay, dedicated history or prior
individual target report was found. Earlier reef/coral discussions are leads,
not independent evidence or prior completed reviews of this target.

Optional parameters, evidence, graphs, discussions and datasets are absent
and should not be invented. iModulonDB is not applicable: no gene, regulator,
expression dataset or mechanism claim is present. SEEDED is consistent with
the maintained inputs.

## Findings

Blockers: 0. Major: 0. Minor: 1.

**Minor m1: retained taxon alias.** The rank-16 PREGO row uses 158080
instead of current canonical ID 141390. Owner: governed PREGO/taxonomy inputs
and `src/habitatmech/extract.py`, not generated YAML. The independently
confirmed biome occurrence was added to existing
[#1244](https://github.com/CultureBotAI/HabitatMech/issues/1244).

## Recommended Edits

Resolve the alias through a versioned taxonomy refresh while preserving the
source ID and observational provenance. Keep ranks, scores and pool size;
test canonical/alias deduplication without merging feature and biome records.
Seek upstream ontology scope clarification before applying this near-surface
biome definition to all deep reefs; do not rewrite it locally by assumption.

## Follow-up Checks

Validate the alias against pinned taxonomy inputs, refresh source manifests,
canary and inspect the target, validate schema/history/labels, reproduce corpus
and regenerate affected semantic-map/site products. Respect #1217's supported
runtime dependency. Complete full QC and required CI before report merge;
publishing the report does not close #1244.

## Additional Notes

The preceding complete issue search covered all 455 returned open/closed
issues and their comments; #1244 already names this exact alias. No duplicate
implementation issue was created. Known findings in the marine-benthic record
do not invalidate this target's genuine ontology-derived benthic parent.
No scientific input, generated record, page, status or history changed.
