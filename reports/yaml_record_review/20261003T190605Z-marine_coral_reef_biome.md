# YAML Record Review: marine coral reef biome

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/marine_coral_reef_biome.yaml`
- Started UTC: 2026-10-03T19:04:57Z
- Finished UTC: 2026-10-03T19:06:05Z
- Verdict: pass

## Target

Read the entire generated HabitatRecord, `ENVO:01000049`, marine coral reef
biome, AQUATIC, EXACT, SEEDED. Its only source is PREGO, computed source key
`habitatmech:PREGO.6e75680d3f`. `data/habitats/PATHS.tsv:770` pins the stem.
The single deterministic seed event is not an ITEM review.

## Validation

- `just validate data/habitats/aquatic/marine_coral_reef_biome.yaml`: pass.
- `just validate-strict data/habitats/aquatic/marine_coral_reef_biome.yaml`:
  one file, zero errors.
- Fresh full `just qc` was still running tests at review finish. Lint,
  documentation and provenance passed; later gates were not yet complete.
- Inspected target, parent and tropical subclass in official ENVO OWL,
  fetched and byte-verified this batch, SHA-256
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
- All 25 current NCBI IDs resolved directly without aliases. Structured
  CSV/YAML comparison verified every retained raw taxon value.
- Required OAK correspondence remains a CI gate; it does not establish
  taxon ecology or coverage of every reef type by this ontology class.

## Identity and Grounding

ID, label, full definition and parent `ENVO:01000029` marine reef biome
match `data/raw/ontology_terms.tsv:7558`,
`data/raw/ontology_subclass_edges.tsv:5689` and
[official ENVO](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl).
`ENVO:01000854` is the tropical subclass, not an interchangeable identifier.
Neither a reef feature nor a coral host-associated environment is the same
identity as this biome. The two PREGO alternate strings remain related.

The ontology's parent definition places reefs near the water surface, and
the target describes wave-resistant construction with symbiont-assisted
growth. This is narrower than an unrestricted reading of the label.
[NOAA's coral-reef overview](https://www.noaa.gov/education/resource-collections/marine-life/coral-reef-ecosystems)
distinguishes shallow symbiotic systems from deep-water reefs; its
[deep-sea tutorial](https://oceanservice.noaa.gov/education/tutorial_corals/media/supp_coral05b.html)
explicitly describes a deep reef whose corals lack zooxanthellae. Thus the
current term must not silently be generalized to all deep coral habitats.
This is an upstream scope boundary to preserve, not proof that HabitatMech
mis-copied the ontology or that this PREGO identifier should be replaced.

## Evidence

`data/raw/prego_habitats.tsv:99` gives 500 distinct taxa, 500 direct
assertions, maximum score 2.43853 and environmental_samples. The YAML's
TAXON aggregate agrees. All 25 displayed rows at
`data/raw/prego_habitat_taxa.tsv:7550-7574` match IDs, blank names, scores,
ranks 1-25 and pool 500. Each raw direct flag is TRUE, the channel is
environmental_samples and corroboration is absent. None is marked
is_characteristic; the other 475 candidates were not individually reviewed.

The primary
[NCBI efetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=46745,48499,214988,3068,247026,7070,610380,639602,6334,7209,104421,6087,7425,8090,7029,6669,13686,69293,7668,6238,45351,7719,39947,46687,46704)
resolved every ID. Examples include 46745 Galaxea fascicularis, 639602
Trissopathes pseudotristicha, 6087 Hydra vulgaris and 39947 Oryza sativa
Japonica Group. Optional blank source labels are faithfully retained; they
are not permission to guess microbial names. The original sample evidence
was not inspected, so an unusual association is neither independently
endorsed nor declared false here. Taxonomy/source projection is the verified
claim, not characteristic membership or compliance with the shallow scope.

The biome also appears as a broad-scale GOLD term at
`data/raw/gold_path_triads.tsv:527`, `:1328` and `:1568`. Reef, host-surface
and sponge-tissue sampling contexts must remain separate from the target's
PREGO attestation. Their sample/study counts were not added to its TAXON
count, and broad-scale context does not establish host or feature identity.

## Completeness

Ignored-inclusive ID, source-key, label and stem searches covered curation,
history, raw inventories, PATHS, research and individual reports. No target
ITEM decision, authored definition, causal overlay, dedicated history or
prior individual target report was found. SEEDED is consistent with this.
Prior coral-feature/host reports and research were leads only.

Optional measurements, evidence, causal graphs, discussions and datasets
are absent; generic reef biology cannot fill them. iModulonDB is not
applicable: no gene, regulator, expression dataset or mechanism is claimed.

## Findings

None verified for the current ontology identity and source projection.
Blockers: 0. Major: 0. Minor: 0. This bounded pass does not endorse an
all-depth interpretation of the ontology label or verify the ecological
basis of the 25 PREGO associations.

## Recommended Edits

No immediate generated-record correction is justified. Before expanding
the term to all coral-reef habitats, seek upstream ENVO scope clarification
using both shallow and deep reef evidence, then refresh governed ontology
inputs if the class changes. Do not silently rewrite the ENVO definition
locally or replace this identity with the tropical subclass.

Trace original PREGO evidence before stronger habitat-membership use or any
source-association correction. Name enrichment belongs in governed taxonomy
inputs/extraction and must preserve original provenance.

## Follow-up Checks

Complete full QC and required CI before report merge. Any later ontology or
source refresh needs provenance validation, canary inspection, schema/history
and OAK checks, corpus reproduction and regenerated affected map/site products.
Review identity changes and source associations separately.

## Additional Notes

No scientific input, generated record, page, status or history changed.
Current ENVO and NOAA describe different scope boundaries; neither source
was discarded merely to produce a simpler verdict.
