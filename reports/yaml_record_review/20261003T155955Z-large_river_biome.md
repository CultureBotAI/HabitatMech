# YAML Record Review: Large river biome

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/large_river_biome.yaml`
- Started UTC: 2026-10-03T15:58:19Z
- Finished UTC: 2026-10-03T15:59:55Z
- Verdict: pass with minor issues

## Target

Read the complete generated `HabitatRecord`, `ENVO:00000887`, large river
biome, `AQUATIC`, `EXACT`, `SEEDED`: definition, four PREGO related synonyms,
one parent, one attestation, 25 ranked taxa and a seed event. `PATHS.tsv:601`
fixes this biome target. The PREGO source mints to `habitatmech:PREGO.6b163ed9ec`.

## Validation

- `just validate data/habitats/aquatic/large_river_biome.yaml`: pass.
- `just validate-strict data/habitats/aquatic/large_river_biome.yaml`: pass,
  zero errors.
- All 25 retained IDs, stored labels, scores and ranks match the source;
  every pool matches the 1,775-taxon aggregate.
- Current NCBI efetch resolves all 25 IDs directly and all 22 existing names
  match, including the bracketed Acidovorax name and Pseudomonas fluorescens
  PF5. No name was changed from memory or a similarly named strain.
- Official ENVO OWL verifies the target, definition and true direct parent.
  Exact baseline `d1b6aa47b` passed full QC 37133815658 and labels 37133815698.
  Fresh local full QC remains running, not claimed complete.

## Identity and Grounding

PREGO already uses the ontology identity. `ENVO:01000253` freshwater river
biome is a broader ecosystem class; its definition and water-body part
restriction do not turn the biome into river water. The target's definition
and direct named subclass edge reproduce current ENVO.
[Official ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl).

ENVO explicitly notes that large is ambiguous and anticipates replacement,
but supplies neither a replacement ID nor a numerical threshold. The linked
WWF page was inspected: it gives historical river-fauna examples and warns
that the biome pages are no longer updated. It supports the historical
ecosystem context, not a current universal size criterion, a microbial
assemblage or an identity change to one particular river.
[WWF large river ecosystems](https://www.worldwildlife.org/biomes/large-river-ecosystems).

The four PREGO spellings are Large river, Large rivers, rivers and riverses.
The last is unusual, but it is present in the source synonym pipe and remains
related, not canonical or exact. `ingest_prego` in `src/habitatmech/seed.py`
preserves those source spellings. This is not the ontology-scope inflation
tracked in #1249; do not manufacture an exact-grounding finding from it.

## Evidence

`prego_habitats.tsv:44` gives 1,775 distinct taxa, 1,775 direct assertions,
maximum score 2.5246 and `environmental_samples`. The generated aggregate is
correctly `TAXON`. The retained rows at `prego_habitat_taxa.tsv:5188-5212`
are all direct in that channel, with ranks 1-25 and scores decreasing from
2.5246 to 2.42302. The other 1,750 identities are outside the stored top-25
slice. Equal aggregate counters do not imply equal units, prevalence or
characteristic presence.

Three IDs have no stored name, although their current references resolve:

| ID | Current scientific name | Taxonomic context |
|---|---|---|
| NCBITaxon:610380 | Harpegnathos saltator | Insecta; species |
| NCBITaxon:3055 | Chlamydomonas reinhardtii | Chlorophyta; species |
| NCBITaxon:39947 | Oryza sativa Japonica Group | Plant group; no-rank entry |

[NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=610380,3055,39947).
The record's ranking field is not taxonomic rank. None of the displayed
entries asserts `is_characteristic`. A plant or insect source association
needs source inspection before stronger ecological interpretation or removal;
the schema does not promise an exclusively bacterial community.

## Completeness

Ignored-inclusive ontology/source-ID, label and stem searches covered
curation, history, research, configuration, reports, raw inputs and path
locks. No target ITEM decision, authored definition, causal overlay,
session history or prior exact-target report was found. The structured
28-dataset iModulonDB catalog has no matching taxa/strains. Datasets for
other Pseudomonas species are not evidence for these strains. No gene/module
query applies; missing optional parameters and mechanisms are not defects.

## Findings

1. **Minor: three resolvable taxon labels are missing.** Owners: governed
   PREGO/NCBI inventories and `_load_taxon_labels` in
   `src/habitatmech/extract.py:650-665`. This is optional-name maintenance,
   not a broken reference, merged-ID case or established false association.

Zero blockers, zero major findings, one minor finding.

## Recommended Edits

Add these three names to #1257's shared governed taxonomy refresh. Preserve
all 25 IDs and scores, ranks, the 1,775 pool and source provenance. Keep the
true freshwater-river-biome parent. Any treatment of PREGO's unusual spelling
must preserve its source provenance and use an explicit normalization policy,
not a silent generated-YAML edit. Do not invent a size threshold.

## Follow-up Checks

Test optional-name loading and unchanged association metadata, canary after
input refresh, append history, verify provenance and corpus, and rebuild
changed semantic-map/site inputs before full QC (#1217). OAK excludes source
taxa, so a correspondence pass is not taxonomy-name completeness. Revisit
identity only against an inspected upstream replacement or ITEM evidence.

## Additional Notes

Official OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
The inspected WWF page is explicitly historical. No universal river fauna,
microbial mechanism, minimum discharge or minimum area was inferred from it.
Only this review report was written; no corpus curation was performed.
