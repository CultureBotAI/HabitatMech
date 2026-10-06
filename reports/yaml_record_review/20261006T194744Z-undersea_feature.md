# YAML Record Review: undersea feature

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/undersea_feature.yaml`
- Started UTC: 2026-10-06T19:44:33Z
- Finished UTC: 2026-10-06T19:47:44Z
- Verdict: needs curation

## Target

Read the complete generated HabitatRecord at baseline
`de3b61e4a6610b56a775a21e0bd78a5e8b31feec`: ENVO:00000104, undersea feature,
AQUATIC, EXACT/SEEDED. It contains an ENVO definition, 184 synonym entries
(69 ENVO exact and 115 PREGO related), one parent, one PREGO attestation,
25 associated taxa and one seed event. The target is a broad marine
hydrographic feature, not one particular landform or its surrounding water.

## Validation

- `UV_CACHE_DIR=build/uv-cache just validate data/habitats/aquatic/undersea_feature.yaml`:
  pass, no issues.
- `UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/aquatic/undersea_feature.yaml`:
  one file, zero errors; refreshed only the ignored validator diagnostic.
- Executed `seed.build_corpus()` and `seed.build_document()` and asserted
  equality of the entire parsed document: pass, one contributing concept,
  zero ITEM-reviewed sources, all 25 taxa and the seed event reproduced.
- Parsed current official ENVO RDF/XML at revision
  `a2455d1a77e46bb8a664d65a157166b539269042`: target and parent are active;
  their labels, definitions and named superclass assertions were inspected.
- Fresh NCBI Taxonomy efetch resolved all 25 requested IDs, including one
  merged alias. An explicit assertion verified all 24 nonempty YAML names
  against current scientific names. Resolved ranks: four species, 21 strains.
- The immediately preceding full local QC passed all 13 gates: 496 tests,
  three skips, two dependency warnings; 3,206 closed-schema records, 107
  histories, 32 causal overlays, provenance, corpus, site and term requests.
  Local OAK and all 18 vendored-file comparisons also passed. The
  [successful merge-group QC](https://github.com/CultureBotAI/HabitatMech/actions/runs/37520007274)
  ran on this exact baseline commit/tree. These full-corpus receipts are
  reused, not represented as another full QC run for this individual review.
  A fresh scoped git comparison confirmed scientific inputs, code, docs,
  tests and generated products are unchanged from the prior validated tree.
- Rendered page text was inspected, including the missing taxon name and
  weaker associated-taxa wording. No browser visual QA was performed.

## Identity and Grounding

The [official ENVO snapshot](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
agrees with the maintained target ID, label, definition and immediate
ENVO:00000012 hydrographic-feature parent. The generated parent retains
ENVO:00000000 geographical feature. The target's placement below a marine
water surface describes its location; it does not make the feature a kind of
water material or marine water body. AQUATIC is a defensible coarse category.

Executed `apply_decision` on the actual `prego_self_grounded` resolution:
the identifier remains ENVO:00000104, EXACT, no mapping predicate, no added
parents/xrefs, `reviewed=False`, and no decision. The addressable source mint
is `habitatmech:PREGO.439d34b645`. EXACT denotes source self identity, not an
ecological quality guarantee. SEEDED accurately reflects no item-level
curation. `PATHS.tsv:486` pins the record filename.

Official ENVO declares no exact or broad synonyms for this target: 59 are
narrow and ten related. Examples of narrow assertions include undersea bank,
undersea fan and shelf edge. The related set is ocean floor feature, seafloor
feature, sill, spur, subsea feature, terrace, tongue (seafloor), underwater
feature, valley and valleys. All 69 ENVO entries are currently emitted exact.
Do not turn this broad identity into one of its lexical examples or invent
subclass records merely from synonym annotations. The independently sourced
PREGO entries must retain their separate, weaker provenance.

## Evidence

All 14 raw TSV inventories were scanned structurally for exact field or
pipe-list membership of the target ID, mint and label/variant. Physical file
locators are distinguished from logical rows containing quoted newlines.

| Input | Verified contribution |
| --- | --- |
| `prego_habitats.tsv:191` | 97 distinct taxa, 97 direct-flagged input assertions, maximum score 3, annotated_genomes_isolates channel; lexical variants including the canonical name |
| `prego_habitat_taxa.tsv:3895-3919` | All 25 emitted entries, score 3, ranks 1-25, direct flags TRUE, genome/isolate channel, no corroborating source; rank-two label is empty in the maintained input |
| `ontology_terms.tsv:6697` | Canonical definition and 69 flattened synonym strings; this is logical TSV row 6691 including header |
| `ontology_subclass_edges.tsv:4734` | Target's hydrographic-feature superclass |
| `ontology_subclass_edges.tsv:4822,5696` | Two narrower ontology classes point to the target; these are not additional target attestations |

The extractor keeps the best score per habitat/taxon, then orders by score,
direct flag and identifier before retaining 25. Every displayed score and
flag ties here, so the displayed rank does not discriminate ecological
specificity. TAXON is not an isolate, sample, abundance or experimental count.
The direct-assertion total counts input edges and need not equal distinct taxa
in general, despite equality in this snapshot.

The inspected [PREGO primary paper, section 2.3](https://imbbc.hcmr.gr/wp-content/uploads/2022/03/2022-Zafeiropoulos-Micro-12.pdf)
describes tagged JGI genome metadata and BioProject-linked abstract mining
within this channel. It assigns BioProject-derived associations confidence
three and the other described genome sources four. This makes the channel
an annotation-based association source, not independent proof of characteristic
presence or direct culture from every named environment. A score of three
alone does not identify the original source record; these 25 assertions
cannot all be attributed to specific BioProjects without their evidence keys.
No source score was treated as a probability.

[NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037355)
resolves the unlabeled NCBITaxon:1037355 to NCBITaxon:879969,
Macellibacteroides fermentans. The structured efetch response lists 1037355
under `AkaTaxIds`. Thus this is a resolvable merged identifier and missing
display name, not a deleted organism or proof of a false habitat association.
The other 24 IDs resolve unchanged with exact current name agreement.
The complete 97-member pool was not recovered, so duplicate canonical taxa
or an erroneous pool count are not asserted.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden` covered curation, history,
research, conf, docs, src, tests, PATHS, RETIRED and the research manifest
using the ID, source mint, label, slug and both old/current taxon IDs.
The only relevant hits were PATHS and an unrelated Seaweed research report's
discussion of the ontology hierarchy. No target-owned decision, definition,
causal overlay or research report was found in those maintained surfaces;
bytecode was excluded. The all-inventory scan found no parameter, GOLD,
BacDive or Madin contribution for this target.

An ignored-inclusive filename/path search in the configured kg-microbe
`data/` tree found no PREGO dump under the searched lower/upper-case source
patterns. The original full graph and individual genome/abstract evidence
keys were not reconstructed. PREGO's public page failed to load in the fresh
web check. The author-institution paper PDF and official NCBI response were
available; source-access failure is not ecological negative evidence.

Empty parameters, literature evidence, graphs, discussion and dataset fields
are not defects by themselves. The broad feature class does not justify
universal depth, oxygen, temperature, salinity, microbial functions or a
characteristic community. iModulonDB is not applicable: there is no gene,
protein, regulator, pathway or transcriptomic-module assertion to check.

## Findings

1. **Major: ontology synonym scopes are inflated to exact.** All 59 narrow
   and ten related ENVO assertions become EXACT_SYNONYM. Owner:
   `extract.py:_load_tsv_ontology`, governed ontology inventory representation
   and `seed.py:ConceptStore.get`, which unconditionally promotes the flat
   pipe at lines 413-414. Existing [#1249](https://github.com/CultureBotAI/HabitatMech/issues/1249)
   was checked read-only and remains open. This is one systemic record
   finding, not 69 independently counted findings.
2. **Minor: a resolvable merged taxon remains unlabeled.** Rank two retains
   NCBITaxon:1037355 and no name, although NCBI resolves it to the named
   canonical taxon above. Owner: upstream taxonomy normalization,
   `extract.py:_load_taxon_labels` and the governed PREGO taxon inventory.
   The loader only looks up exact IDs; generated YAML/pages are not the fix.

Totals: zero blockers, one major finding, one minor finding. Original
association evidence remains unresolved, without a false-association verdict.

## Recommended Edits

1. Recover and preserve typed ontology synonym assertions reproducibly, then
   regenerate. Include narrow and related examples from this target plus
   genuinely exact controls elsewhere; preserve PREGO provenance. Do not
   globally downgrade all ontology synonyms or patch generated YAML.
2. Refresh taxon resolution and labels through the maintained source contract,
   preserving the historical source identifier. If canonical IDs are adopted,
   deduplicate the full pool before reranking/recounting, not just the top 25.
   Add merged-ID and canonical-convergence regressions. Do not claim the
   current pool count is wrong without testing the full pool.
3. Recover original genome/abstract evidence keys before making a stronger
   isolation, characteristic-presence or ecological-specificity assertion.

## Follow-up Checks

For future curation, compare against a pinned typed ontology and NCBI alias
mapping; inspect dry seed and a forced canary. Run provenance, open/strict
schema, labels, history, exact corpus reproduction, site, term requests and
full QC. Compare semantic-map input hashes: scope-only changes may be text
neutral, but a new taxon label or other selected-text change needs its actual
impact checked before deciding whether the map/site must be rebuilt.

## Additional Notes

Only this new timestamped report was authored for the target. No scientific
input, record, page, history, old report or GitHub item was modified. Earlier
unpublished Undersea feature checks were not counted as a completed review;
the full target and necessary target checks were repeated at this baseline.
The ignored-inclusive starting census found 1,060 reviewed current records
out of 3,206. Full-corpus completion and SSSOM/KGX readiness are not claimed.
