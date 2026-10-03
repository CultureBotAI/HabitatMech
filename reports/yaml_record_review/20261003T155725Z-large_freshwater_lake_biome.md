# YAML Record Review: Large freshwater lake biome

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/large_freshwater_lake_biome.yaml`
- Started UTC: 2026-10-03T15:55:58Z
- Finished UTC: 2026-10-03T15:57:25Z
- Verdict: pass with minor issues

## Target

Read the complete generated `HabitatRecord`, `ENVO:00000891`, large freshwater
lake biome, `AQUATIC`, `EXACT`, `SEEDED`: ontology definition, three PREGO
related synonyms, one parent, one attestation, 25 ranked taxa and a seed
event. `PATHS.tsv:603` identifies the biome, not a bare lake water body.
The PREGO source key mints to `habitatmech:PREGO.8cb296bcba`.

## Validation

- `just validate data/habitats/aquatic/large_freshwater_lake_biome.yaml`: pass.
- `just validate-strict data/habitats/aquatic/large_freshwater_lake_biome.yaml`:
  pass, zero errors.
- All 25 stored association IDs, available names, ranks and scores match
  committed PREGO input; each pool is 1,617.
- Fresh NCBI efetch resolves all 25 IDs without alias redirects and verifies
  all 22 present names, including Paraclostridium sordellii (NCBITaxon:1505).
- Official ENVO OWL XML verifies the target and direct parent. Exact baseline
  `d1b6aa47b` passed full QC 37133815658 and labels 37133815698; fresh local
  full QC is still running, not claimed complete.

## Identity and Grounding

The ontology defines a freshwater biome determined by a large lake and places
it under `ENVO:01000252` freshwater lake biome. That is a true broader biome,
not the lake's water material or the lake itself. PREGO already uses the ENVO
identity. Its three shorter spellings, Large lake, Large lake biome and Large
lakes, remain related synonyms; they are not exact equivalences between a
water body and an ecological system.
[Official ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl).

The current OWL comment explicitly calls large ambiguous and anticipates a
less ambiguous class; it does not supply a replacement or area threshold.
The inspected FEOW Major Habitat Types page describes lake-dominated
ecoregions, including associated rivers and wetlands. It supports retaining
the ecosystem/water-body distinction, not copying every FEOW member into
this ENVO class or asserting a universal lake size. FEOW's own grouping also
includes inland seas, so its scope is not an automatic exact replacement
for a freshwater-only ontology class.
[FEOW habitat types](https://www.feow.org/global-maps/major-habitat-types).

## Evidence

`prego_habitats.tsv:50` records 1,617 distinct taxa, 1,643 direct assertions,
maximum score 4 and channel `environmental_samples`. The generated count
correctly uses `TAXON`; the larger assertion count is not a competing taxon
pool. `prego_habitat_taxa.tsv:5238-5262` retains 25 rows, all direct and
score 4, ranked 1-25 in that channel. The other 1,592 taxon identities are
not stored in this top-25 inventory.

Three labels are missing, although all corresponding IDs resolve directly:
`NCBITaxon:121845` Diaphorina citri, `NCBITaxon:154510` Coleochaete
sieminskiana and `NCBITaxon:155715` Raphidonema nivale. This repeats the
same inventory-label gap seen in lake inlet, but the aggregate and ranks
were independently checked for this target.
[NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=121845,154510,155715).
No taxon is marked characteristic. Mixed lineages or a high PREGO score do
not justify claiming a universal microbial community, nor removing a source
association without examining its evidence.

## Completeness

Ignored-inclusive term/source-ID, label and stem searches covered curation,
history, research, configuration, reports, raw inputs and path locks. No
target ITEM decision, authored definition, causal overlay, session history
or prior exact-target report was found. The structured 28-dataset iModulonDB
catalog inspected in this review sequence has no matching taxa/strains;
no module query applies and absence is not negative evidence. Optional
measurements and mechanisms need not be filled to make a complete review.

## Findings

1. **Minor: three current taxon names are absent from the retained source
   rows.** Owner: governed PREGO/NCBI inventories and `_load_taxon_labels`
   in `src/habitatmech/extract.py:650-665`. This is optional-label reference
   maintenance, not a broken identifier or demonstrated false association.

Zero blockers, zero major findings, one minor finding. The ontology's stated
size ambiguity is retained as an interpretation limit, not silently repaired.

## Recommended Edits

Extend #1257's shared taxonomy refresh with this target, preserving its
1,617-taxon pool, 25 association rows, ranks/scores and source provenance.
Keep the true biome parent and related synonym scopes. Monitor any future
upstream ENVO replacement; do not invent a numeric cutoff or re-ground this
biome to a lake material term.

## Follow-up Checks

Canary after a versioned taxonomy input refresh, verify association metadata
and optional-name behavior, append history, and pass provenance, strict,
corpus, history and full QC. Label changes require comparing and rebuilding
semantic-map/site input through the governed runtime (#1217). The OAK
correspondence gate excludes source taxa, so it cannot prove this fix.

## Additional Notes

The legacy WWF URL in the ontology comment redirected to a page the web tool
could not inspect; no scientific claim relies on its uninspected contents.
The FEOW page was opened and read. Official OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
Only this review report was written; no corpus curation was performed.
