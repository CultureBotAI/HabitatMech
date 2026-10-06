# YAML Record Review: Small River Biome

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/small_river_biome.yaml`
- Started UTC: 2026-10-06T03:46:59Z
- Finished UTC: 2026-10-06T03:49:38Z
- Verdict: pass

## Target

Read the complete generated `HabitatRecord`: `ENVO:00000890`, small river
biome, `AQUATIC`, `EXACT`, `SEEDED`. `PATHS.tsv:602` identifies this target,
not a river-water material, individual river, or large river biome. It has
an ENVO definition, four PREGO related synonyms, one parent, one source
attestation, 25 observational taxon associations and one seed event.

## Validation

- `just validate data/habitats/aquatic/small_river_biome.yaml`: passed.
- `just validate-strict data/habitats/aquatic/small_river_biome.yaml`:
  one file, zero errors.
- Actual `build_corpus` / `build_document` comparison reproduced the whole
  document, not just selected fields: one source, zero reviewed sources,
  25 taxa and one history event.
- Fresh `just verify-corpus`: 3,206 expected/found; zero missing, extra or
  differing files. Fresh `just validate-history`: all 90 histories valid.
- Current OLS and typed official ENVO OWL verify both habitat identifiers,
  definitions, labels and hierarchy. Current NCBI EFetch returns all 25
  retained IDs directly; every stored scientific name matches.
- Unchanged-input full-CI baseline: main-push QC
  [37409623564](https://github.com/CultureBotAI/HabitatMech/actions/runs/37409623564)
  is successful at `d9b5df4330fead0bc521c4efaf7d0e91e5f70f0b`.
  The inspected preceding merge-group QC
  [37408965551](https://github.com/CultureBotAI/HabitatMech/actions/runs/37408965551)
  passed 463 tests, three skipped, two warnings, 90 histories, exact corpus
  reproduction and all gates. This is reused CI, not a new local full-QC run.
  Its label and vendored-sync checks also passed. OAK deliberately excludes
  source taxon labels; the NCBI check is independent of that gate. No separate
  reference validator applies to this record, which has no EvidenceItems or
  causal edges.

## Identity and Grounding

PREGO already asserts the ENVO identity. The source decision key is
`habitatmech:PREGO.dac1bc9a31`. Actual default and applied resolutions agree:
`prego_self_grounded`, `EXACT`, contributes grounding, no mapping predicate,
extra parent or reviewed decision. Source-self identity does not require an
invented mapping predicate or imply that a curator endorsed the record.

The definition and named parent `ENVO:01000253`, freshwater river biome,
match ENVO. The parent's freshwater-biome superclass and freshwater-river
part restriction do not make the biome synonymous with river water.
[Small river biome](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000890),
[freshwater river biome](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000253).

The typed OWL comment explicitly calls the size adjective ambiguous and
anticipates a less ambiguous replacement, but current OLS reports the term
active. The linked WWF page is explicitly historical and describes freshwater
biota examples, not a universal river-size threshold or microbial community.
Do not manufacture a numeric cutoff, replacement ID or obsolescence decision.
[Official ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl),
[WWF small river ecosystems](https://www.worldwildlife.org/biomes/small-river-ecosystems).

The raw PREGO synonym pipe has five entries. `Concept.add_synonym` suppresses
Small river biome because it normalizes to the canonical label; the other
four retain PREGO provenance and related scope. In particular, rivers is
broader wording and riverses is unusual, but neither is asserted canonical
or exact. Faithful source-spelling retention is not an ontology synonym-scope
inflation finding. No ENVO synonym assertion is present for this term.

## Evidence

`data/raw/ontology_terms.tsv:7156` supplies the definition and
`ontology_subclass_edges.tsv:5252` the parent. `prego_habitats.tsv:57` supplies
1,473 distinct source taxon IDs, a separate 1,494 direct-assertion count,
maximum score 4 and only `environmental_samples`. The record correctly emits
1,473 with unit `TAXON`, not 1,494 samples, organisms, or retained rows.

`prego_habitat_taxa.tsv:5213-5237` supplies the 25 displayed IDs, labels,
scores, ranks, direct flags and channels. All have score 4, direct flag TRUE,
environmental_samples only and no corroboration. The generated pool of 1,473
comes separately from `prego_habitats.tsv:57` (`taxon_count`), copied by
`ingest_prego` in `src/habitatmech/seed.py:1101`; the pair table has no
candidate-pool field. The extractor orders score, directness and lexical ID
before retaining 25. These displayed ties do not establish abundance or
ecological dominance; the other 1,448 identities are outside the stored slice.

The inspected original PREGO methods describe environmental associations
from taxonomic profiles co-occurring with sample metadata. They support the
channel's method, not independent verification of this target's exact pairs.
[PREGO, section 2.4, DOI 10.3390/microorganisms10020293](https://imbbc.hcmr.gr/wp-content/uploads/2022/03/2022-Zafeiropoulos-Micro-12.pdf).
All 25 current taxon IDs and names resolve directly, including the four
strain-level entries and Haloquadratum walsbyi. That verifies identity, not
freshwater occurrence. A familiar marine or host-associated name alone does
not prove a false environmental association. No entry is `is_characteristic`.
[NCBI EFetch, all retained IDs](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1026,104176,1044,109263,128,1396,1423814,143223,1502,1510,173,224438,2369,237727,238,241368,262076,266940,28122,28251,293091,301375,313596,314260,34003&retmode=xml).

## Completeness

Ignored-inclusive identifier, source-key, label, stem and riverses searches
covered curation, history, research, configuration, documentation, source,
tests, prior reports and path registries. No exact-target maintained decision,
definition, overlay, history session or prior individual report was found.
The large-river-biome report was read as a lead, not reused as target evidence.
The exact identifier was also scanned across all 14 raw TSVs, including
overflow values; matches occurred only in the four inventories cited above.
Optional parameters and mechanisms are not required by this observational
record. No gene, regulator or expression dataset is asserted; iModulonDB is
not applicable, not negative evidence.

An ignored-inclusive search under the configured kg-microbe checkout found
no PREGO input paths. The full 1,473-member source graph, sample crosswalk and
full-pool identity/collision behavior were not reconstructed. This limits
independent occurrence verification, not the passing reproduction of the
committed inventories. No upstream graph hash match is claimed.

The complete rendered page and actual semantic text were inspected. The
page uses Associated taxa, warns about retained rank and per-source count
units, and does not equate SEEDED with human review. All 25 names are present.

## Findings

None found within the inspected record and source scope: zero blockers,
zero major findings, zero minor findings. Upstream size ambiguity and the
unavailable full-source reconstruction are explicit limitations, not proof
of a wrong identity or missing required field.

## Recommended Edits

No scientific edit is established. Retain the true freshwater-river-biome
parent and observational status. Any future alias normalization must use a
versioned PREGO input/policy with provenance, not a generated-YAML patch.
Revisit size scope only against an inspected ontology revision or explicit
item-level evidence; do not substitute a broader river material.

## Follow-up Checks

For any later source refresh, compare pair-level fields separately from the
habitat-summary denominator, inspect the whole candidate pool, preserve
original IDs/provenance, and check ranks/selection after canonicalization.
Run provenance, canary/reproduction, history, schema and full QC gates.
If text-bearing fields change, evaluate actual semantic text and regenerate
map/site products through the governed workflow; preserve #1218/runtime pins.

## Additional Notes

All-state pagination searched 629 GitHub issue titles/bodies for the exact
target/source key and riverses; no matches were returned. This is not a
claim that all issue comments were searched. No issue was manufactured for
a passing target, and no scientific input, history or generated product was
edited. Typed OWL snapshot SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
