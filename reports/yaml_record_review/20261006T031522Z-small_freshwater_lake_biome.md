# YAML Record Review: Small Freshwater Lake Biome

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/small_freshwater_lake_biome.yaml`
- Started UTC: 2026-10-06T03:14:32Z (final verification pass; continued earlier individual review)
- Finished UTC: 2026-10-06T03:15:22Z
- Verdict: pass with minor issues

## Target

Read the complete generated `HabitatRecord`: `ENVO:00000892`, small freshwater
lake biome, `AQUATIC`, `EXACT`, `SEEDED`. `PATHS.tsv:604` identifies this
record, not lake, lake water, or large freshwater lake biome. It contains an
ENVO definition, three PREGO related synonyms, one parent, one PREGO source
attestation, 25 observational taxon associations and one seed history event.
The maintained inputs, generated YAML, pages and history were not edited.

## Validation

- `just validate data/habitats/aquatic/small_freshwater_lake_biome.yaml`:
  passed, no issues.
- `just validate-strict data/habitats/aquatic/small_freshwater_lake_biome.yaml`:
  passed, one file, zero errors.
- Actual `build_corpus` / `build_document` comparison reproduced the entire
  loaded document, including 25 taxa and the single history event. The
  concept has one source and zero reviewed sources.
- `just verify-corpus`: 3,206 expected and found; zero missing, extra or
  differing documents. `just validate-history`: all 90 records valid.
- Current official OLS verifies the two habitat identifiers, names,
  definitions and active status. Typed official ENVO OWL independently
  supports the asserted superclass and the small-biome ambiguity comment.
- Current NCBI EFetch resolves all 25 retained identifiers: 24 directly and
  one through an explicit merged alias. All 23 stored names match current
  scientific names. The two missing names are detailed below.
- Full current-code CI is reused, not represented as a new local full-QC
  run: merge-group QC [37405331753](https://github.com/CultureBotAI/HabitatMech/actions/runs/37405331753)
  passed with 463 tests, three skipped and two warnings, 90 valid histories,
  exact corpus reproduction and all gates. Baseline main-push QC
  [37406717753](https://github.com/CultureBotAI/HabitatMech/actions/runs/37406717753)
  also completed successfully on `5eb94ad1e72f5c05bf857c3a18247910242779c3`.
  Baseline head label run 37402245135 passed with zero flagged; its target
  configuration explicitly excludes `characteristic_taxa`, so this is not
  taxonomy verification. No separate reference validator is exposed for
  this record, which has no EvidenceItems or causal edges.

## Identity and Grounding

The source already uses `ENVO:00000892`. The actual default and applied
resolutions agree: `prego_self_grounded`, `EXACT`, contributes grounding,
no mapping predicate, extra parent or reviewed decision. The decision key
is `habitatmech:PREGO.03c4ec33c5`. An absent source-self mapping predicate is
correct here, not an incomplete exact mapping.

The definition and sole parent `ENVO:01000252`, freshwater lake biome,
agree with ENVO. The typed snapshot places the parent under freshwater
biome and supplies a lake part restriction. Do not conflate the biome with
the physical lake or a sample of its water.
[Small freshwater lake biome](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000892),
[freshwater lake biome](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000252).

The typed OWL comment explicitly treats "small" as ambiguous and discusses
future replacement of this WWF-derived class. Current OLS still reports it
active; the comment is not an obsolescence assertion. The inspected WWF
page describes smaller lentic ecosystems selected for freshwater biodiversity
and explicitly labels its classification historical. Neither source supplies
a universal area/depth threshold. This is an upstream scope caveat, not
evidence that this faithful source-self record has the wrong identity.
[Official ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl),
[historical WWF small-lake ecosystems](https://www.worldwildlife.org/biomes/small-lake-ecosystems).

All three names, Small lake, Small lake biome and Small lakes, are PREGO
`RELATED_SYNONYM` entries. The inspected ontology term has no synonym
assertions to flatten. The broader surface names are not asserted exact.

## Evidence

`data/raw/ontology_terms.tsv:7158` contains the canonical definition and
`ontology_subclass_edges.tsv:5254` the named parent.
`prego_habitats.tsv:149` supplies 203 distinct source taxon IDs, 203 direct
assertions, maximum score 4 and only `environmental_samples`. These are
different count concepts even though they coincide here. The record
correctly emits 203 with unit `TAXON`, not 203 samples or isolates.

`prego_habitat_taxa.tsv:5263-5287` contains all 25 retained pairs. Each has
score 4, `direct_flag` TRUE and only `environmental_samples`; retained ranks
are 1-25. The generated `candidate_pool` of 203 comes separately from
`prego_habitats.tsv:149` (`taxon_count`) via `src/habitatmech/seed.py:1101`,
not from the pair table. The extractor sorts by descending score,
directness, then lexical taxon ID, and caps the list at 25. These displayed
ties are not an abundance or ecological-dominance ranking. No retained
association is marked `is_characteristic` or independently corroborated.

The inspected original PREGO paper describes environmental associations
from taxonomic profiles co-occurring with sample metadata. It supports the
channel's methodology, not independent validation of these exact 203 pairs.
Neither its methods nor a source direct flag establishes a universal
characteristic community or a causal mechanism.
[PREGO methods, sections 2.1 and 2.4, DOI 10.3390/microorganisms10020293](https://imbbc.hcmr.gr/wp-content/uploads/2022/03/2022-Zafeiropoulos-Micro-12.pdf).

| Stored identifier | Current NCBI result | Scope |
|---|---|---|
| NCBITaxon:108943 | NCBITaxon:640397, Protoparmeliopsis muralis | 108943 explicitly appears in AkaTaxIds; merged, not broken. |
| NCBITaxon:120749 | Neglectella solitaria | Same current identifier; missing display name. |

[Official NCBI check](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=108943,120749&retmode=xml).
The full 25-ID EFetch comparison also verified every present name, including
Paenibacillus polymyxa at rank 25. Taxonomic identity does not verify lake
occurrence. Fungal or algal lineage alone does not invalidate an upstream
association or justify replacing it with a guessed bacterium.

## Completeness

Ignored-inclusive exact identifier, source-key, label and stem searches
covered curation, history, research, configuration, documentation, source,
tests, prior reports and the path registries. The current census found no
prior individual report for this target. All 14 raw TSV inventories were
scanned for exact identifier matches, including overflow fields. Matches
were confined to ontology terms, ontology subclass edges and the two PREGO
inventories. No exact GOLD, BacDive, Madin, grounding or parameter row was
found in that bounded scan. Optional measurements, mechanisms, evidence
items and iModulonDB queries are not required for this observational record;
no gene, regulator or expression dataset is asserted.

The configured upstream PREGO node/edge inputs could not be reconstructed:
the probe failed because the configured `data/transformed/prego/nodes.tsv`
was missing. An ignored-inclusive search under the configured kg-microbe
checkout found no PREGO paths. A broader KG-Microbe-root search had permission
errors in other directories and is not exhaustive. No alternative input was
verified against the manifest hashes. Therefore this review verifies the
committed counts and top-25 rows, not the complete 203-member upstream pool,
sample crosswalk, or possible canonical-ID collisions in that pool.

The current rendered habitat page was inspected in full. It labels the list
Associated taxa, explains source-count units and retained-rank limitations,
and does not equate SEEDED with human review. The two missing names render
as bare identifiers. This is not a missing generated page.

## Findings

1. **Minor: two missing taxon names, including one merged source ID.**
   The current official identities are given above. This is reference and
   display maintenance, not a broken habitat identifier, false occurrence
   finding, or schema failure. Owner: versioned kg-microbe PREGO/NCBI inputs
   and `_load_taxon_labels` in `src/habitatmech/extract.py:650`, whose exact-ID
   lookup does not itself recover historical aliases. The existing
   [issue #1257](https://github.com/CultureBotAI/HabitatMech/issues/1257)
   already names both identifiers and owns this correction.

Zero blockers, zero major findings, one minor finding. Upstream ambiguity
and unavailable full-source reconstruction are disclosed limitations, not
additional invented failures.

## Recommended Edits

Refresh names and alias handling through governed, versioned source inputs;
preserve the original source identifier and evidence provenance. Inspect
the entire 203-member source pool for canonical collisions before changing
IDs, counts, ranks or selection. Do not patch the generated YAML or quietly
promote these associations to characteristic presence. Append this target
as an additional witness to #1257 rather than filing a duplicate root cause.

## Follow-up Checks

Test merged-ID provenance, optional names, full-source collision handling
and preservation of per-pair scores/channels and target-specific pool counts.
Re-extract governed inventories, canary the seed, append curation history,
verify provenance and exact corpus reproduction, and run full QC.

An actual in-memory `semantic_text` probe shows adding the two names adds
two observed-taxon lines. Changing only the unlabeled alias ID leaves that
text unchanged. Thus label recovery needs supported map/site regeneration
under #1217; do not assume the isolated ID-only edit has the same text
effect. Preserve protected draft #1218 and runtime pins. The OAK label gate
does not replace the explicit NCBI checks.

## Additional Notes

This is a read-only scientific review. No source correction, history event,
status promotion or regenerated scientific artifact is included. Full
all-state issue pagination inspected 628 issue titles/bodies; #1257's full
body and five comments were read. That issue covers these exact identifiers
already; no exact small-biome witness was present there. Other report hits
for 1089439 are substring near misses, not this taxon.

The typed official ENVO snapshot used here was
`/private/tmp/habitatmech-review-envo-20261004.owl`, SHA-256
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`;
current OLS was checked separately. The PREGO homepage timed out and MDPI
returned HTTP 429; the institution-hosted original paper supplied inspected
methods and DOI metadata instead. Neither access failure was treated as
proof that PREGO or a scientific association no longer exists.
