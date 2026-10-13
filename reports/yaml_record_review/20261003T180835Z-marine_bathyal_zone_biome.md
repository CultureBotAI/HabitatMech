# YAML Record Review: marine bathyal zone biome

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/marine_bathyal_zone_biome.yaml`
- Started UTC: 2026-10-03T18:06:28Z
- Finished UTC: 2026-10-03T18:08:35Z
- Verdict: pass

## Target

Read the entire generated HabitatRecord, `ENVO:01000026`, marine bathyal zone
biome, AQUATIC, EXACT, SEEDED. PREGO is the sole source; its computed decision
key is `habitatmech:PREGO.66ac02ed40`. `PATHS.tsv:761` pins the stem. The
single seed event does not establish ITEM curation.

## Validation

- `just validate data/habitats/aquatic/marine_bathyal_zone_biome.yaml`: pass.
- `just validate-strict data/habitats/aquatic/marine_bathyal_zone_biome.yaml`:
  one file, zero errors.
- Fresh full `just qc` was still active at review finish. Tests passed:
  455 passed, 3 skipped, 2 warnings. History (83), strict corpus (3,206),
  overlays (32), curation floor and exact corpus reproduction also passed;
  generated-site and later gates were not yet confirmed complete.
- Inspected current official ENVO OWL, fetched and byte-verified this batch,
  SHA-256 `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
- Both displayed NCBITaxon IDs resolved directly in current NCBI efetch,
  without alias redirects. The one supplied scientific name matched.
- OAK identity validation is deferred to required CI. Taxon labels and
  synonym scopes are outside that configured gate.

## Identity and Grounding

ID, label, full definition and sole parent match
[official ENVO](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl),
`ontology_terms.tsv:7537` and `ontology_subclass_edges.tsv:5667`. This is a
benthic biome at approximately 200-3,000 m, generally associated with the
continental slope, not the bathypelagic water column. The source does not
assert a rigid universal depth boundary beyond the quoted ontology wording.

`ENVO:01000024` marine benthic biome is genuinely broader. Its current
ontology definition and full maintained record were read for context. The
parent record has other source assertions requiring its own review; reading
it here neither endorses all those assertions nor counts as another completed
target review. The separate GOLD Bathypelagic/Bathyal zone source mentioned in
an earlier report must not be merged here merely because part of its slash
label resembles this biome.

## Evidence

`prego_habitats.tsv:524` gives two distinct taxa, two direct assertions,
maximum score 4 and the environmental-samples channel. The YAML faithfully
retains a TAXON count. It is not a count of cultures or independent studies.

Both retained rows at `prego_habitat_taxa.tsv:7428-7429` were checked with
structured CSV/YAML parsing: IDs, score 4, ranks 1-2, pool 2, direct flags TRUE,
channel and absent corroboration agree. All candidates are displayed, and
neither is marked `is_characteristic`.

Current [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/taxonomy) resolves
`NCBITaxon:777` directly to the displayed Coxiella burnetii. The unnamed
`NCBITaxon:36987` resolves directly to Coptotermes formosanus; its inspected
lineage includes Metazoa and Insecta. It is not an unidentified microbial
species and must not receive a guessed microbial replacement. The missing
optional YAML label faithfully reflects the blank committed raw field;
`_load_taxon_labels` only fills names found in the upstream taxonomy table.

The ecological basis for that nonmicrobial association remains unverified.
PREGO's score/direct flag is source metadata, not independently inspected
evidence that this organism inhabits a deep marine biome. No primary sample
record behind the association was inspected, so this report neither endorses
that ecological interpretation nor declares the source assertion false. The
present schema permits observational taxa and does not require a microbial
filter or a label. Source projection alone is the supported claim.

PREGO's canonical label plus three alternate strings are projected as related
synonyms. The morphological variant `marine bathyal zonous` remains explicitly
source-attributed, not a canonical or exact ontology label.

## Completeness

Ignored-inclusive ID, source-key, label and stem searches covered curation,
raw inventories, PATHS, history, research and individual reports. No target
ITEM decision, authored definition, overlay, dedicated history or prior
individual target review was found. Earlier mentions compare another GOLD
source to this term. SEEDED correctly reflects the absence of ITEM review.

Optional measurements, causal graphs, evidence, discussions and datasets
must not be filled from generic deep-sea biology. The omitted optional taxon
label is not alone a schema or provenance error. iModulonDB is not applicable:
there is no gene, regulator, expression dataset or mechanism claim, and a
module match would not settle a source habitat association.

## Findings

None verified for the current identity and explicitly source-attributed
projection. Blockers: 0. Major: 0. Minor: 0. This bounded pass does not verify
the ecology of Coptotermes formosanus or promote either displayed taxon to a
characteristic member of the biome.

## Recommended Edits

No immediate record edit is justified by the inspected evidence. Before any
stronger ecological use, trace the original PREGO environmental-sample evidence
for 36987 and 777. A supported name enrichment belongs to the governed source
taxonomy inputs and `src/habitatmech/extract.py`, not generated YAML. Any
source-association correction needs the original evidence and an auditable
input policy; do not delete an unusual association based only on plausibility.

## Follow-up Checks

Complete QC and required network identity checks before report merge. Any
future source refresh must preserve IDs, ranks, scores, channel, candidate
pool and observational status, then canary, validate provenance/schema/history,
verify corpus, compare semantic-map inputs and regenerate affected products.

## Additional Notes

All 443 returned open/closed issues and comments were searched for 36987,
Coptotermes and missing-label issues. #1244 concerns actual redirects and
changed names in other records; neither condition was found here. No duplicate
alias issue was created for a valid stable ID with an optional blank label.
No scientific input, generated record, page or curation history changed.
