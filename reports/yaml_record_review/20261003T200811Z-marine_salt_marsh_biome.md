# YAML Record Review: marine salt marsh biome

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/marine_salt_marsh_biome.yaml`
- Started UTC: 2026-10-03T20:05:29Z
- Finished UTC: 2026-10-03T20:08:11Z
- Verdict: pass with minor issues

## Target

Read the complete generated HabitatRecord for `ENVO:01000022`, marine salt
marsh biome: AQUATIC, EXACT, REVIEWED, with BACDIVE and PREGO attestations,
50 displayed observational taxa, and three generated history events.
`data/habitats/PATHS.tsv:759` pins its current stem. No generated file was edited.

## Validation

- `just validate data/habitats/aquatic/marine_salt_marsh_biome.yaml`: passed.
- `just validate-strict data/habitats/aquatic/marine_salt_marsh_biome.yaml`:
  one file, zero errors.
- Fresh `just qc` is running. Lint, documentation and raw provenance passed;
  the test stage has not completed at report finish. Corpus reproduction,
  history, overlays and generated products are not yet verified by this run.
- Current ENVO class and parent were inspected directly; all 50 displayed
  taxon references were queried against current NCBI Taxonomy.
- The full OAK gate remains required in CI. Its configured scope excludes
  source attestations and characteristic-taxon labels; it does not establish
  the ecological truth of a PREGO association.

## Identity and Grounding

`data/raw/ontology_terms.tsv:7533` and current official ENVO agree on the
identifier, label and definition. The definition describes a marine intertidal
biome with salt-tolerant herbaceous vegetation, not the plants, sediment or
whole marine water body. Its one named parent, `ENVO:00000447` marine biome,
matches `ontology_subclass_edges.tsv:5663` and current OWL.

[NOAA's salt-marsh account](https://oceanservice.noaa.gov/facts/saltmarsh.html)
supports the tidal coastal-wetland interpretation and nutrient-processing
context. It does not independently prove every general ecological statement
in the ontology definition or every listed taxon association.

The BacDive mapping is **closeMatch**, not exactMatch:
`isolation_source_groundings.tsv:272` maps Salt-marsh to this term with medium
confidence and lexical-matching provenance. The attestation retains that
predicate. The record's EXACT status also reflects PREGO's direct ontology
identity and must not be read as upgrading the BacDive assertion. The
source-label synonym is emitted as EXACT_SYNONYM; it is not an ENVO axiom or
additional evidence overriding the explicitly weaker mapping predicate.

ITEM REVIEW decisions at `curation/decisions.tsv:92,1452` cover
`habitatmech:BACDIVE.efbaf083f7` and `habitatmech:PREGO.5b16eb64c7`.
The two review events and final seeding event faithfully explain REVIEWED.
No independently established identity error was found in this bounded audit.

## Evidence

- `bacdive_isolation_sources.tsv:98`: 41 strains and 26 taxa. The record
  preserves the 41 STRAIN assertions and BacDive source ID and spelling.
- `prego_habitats.tsv:178`: 121 taxa, 121 direct assertions, maximum score 4,
  environmental-samples channel. The record preserves the TAXON unit, score
  and channel. Do not add these counts to the BacDive strain count.
- All 25 PREGO rows at `prego_habitat_taxa.tsv:7378-7402` match displayed IDs,
  names or optional blanks, scores, ranks 1-25 and pool 121. All are direct
  environmental-samples assertions; none carries corroboration in that table.
- All 25 BacDive rows at `bacdive_source_taxa.tsv:2400-2424` match displayed
  IDs, names, strain counts, ranks 1-25 and pool 26. Rank 24,
  `NCBITaxon:48729` Rhabdochromatium marinum, alone carries PREGO corroboration.
  `extract.py:1409-1483` computes this against full source sets before
  truncation. Its absence from the displayed PREGO top 25 is not a
  contradiction. The original full PREGO assertion was not independently read.
- Current [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=163248)
  explicitly resolves the unlabeled PREGO rank-10 ID `163248` to `996992`,
  Lophiotrema vagabundum, with the former in AkaTaxIds. The other 49 IDs resolve
  directly and all 49 supplied names match, including the generic source name
  `bacterium` and the strain-level names. Name resolution is not ecology proof.
- GOLD triad rows 557 and 560 use this biome as broad-scale context for
  intertidal salt marsh and salt-marsh sediment. These are distinct source
  concepts, not additional attestations or counts to insert into this record.

## Completeness

The 96 undisplayed PREGO taxa and one undisplayed BacDive taxon were not
individually reviewed. No taxa are promoted to `is_characteristic`.
Original study-level associations and the full-source corroboration claim
remain outside the evidence inspected here.

Ignored-inclusive searches by identifier, label, stem and both source keys
covered curation, history, research, prior record reports and PATHS. They found
the two ITEM decisions but no matching term request, causal overlay, separate
authored history or prior target report. Structured scans included all 770
environment-parameter rows and 58 Madin habitats, with no exact target match.
Empty parameters, evidence, graphs, discussions and datasets therefore are
not automatically defects; no unsupported mechanism has been invented.

## Findings

1. **Minor - HM-SALT-MARSH-001:** PREGO retains the resolvable legacy taxon ID
   `NCBITaxon:163248`. The optional blank label is faithfully copied, not a
   schema error. Current NCBI supplies canonical `NCBITaxon:996992` and its
   name. Owner: governed taxonomy inputs and `src/habitatmech/extract.py`, not
   generated YAML. Tracked in [#1292](https://github.com/CultureBotAI/HabitatMech/issues/1292).

No blocker or major finding was established.

## Recommended Edits

Resolve aliases through versioned NCBI inputs while preserving original source
IDs/names as provenance. Test replacement/alias coexistence before any
deduplication. Preserve rank, score, pool, source channels, corroboration and
observational status. Do not infer characteristic membership from an alias
refresh or from a high PREGO score.

## Follow-up Checks

Canary the affected extractor/seeder outputs; verify manifests and corpus
reproduction; re-query old and replacement taxon IDs; inspect corroboration
against the original full inputs. Regenerate affected map/site products in the
supported runtime tracked by #1217 and run full QC and required OAK checks.
The review report does not fix or close #1292.

## Additional Notes

Current official [ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl)
was fetched on 2026-10-03, SHA256
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
The browser rejected its size; the complete downloaded XML was inspected.
All 456 existing open/closed issues and returned comments were searched before
filing #1292. iModulonDB was not applicable: this record has no strain-specific
gene, regulator or expression-module claim. No paid research was used.

An exploratory cross-table scan initially stopped on an unrelated extra-field
row in `gold_path_biosamples.tsv:395`; it was rerun with explicit string-field
handling. No target conclusion relies on that malformed row or on the failed
scan. Original record and source inventory bytes remain unchanged.
