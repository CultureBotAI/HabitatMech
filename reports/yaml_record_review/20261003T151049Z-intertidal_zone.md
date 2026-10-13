# YAML Record Review: Intertidal zone

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/intertidal_zone.yaml`
- Started UTC: 2026-10-03T15:07:27Z
- Finished UTC: 2026-10-03T15:10:49Z
- Verdict: needs curation

## Target

Read the complete generated `HabitatRecord`, `ENVO:00000316`, intertidal zone,
`AQUATIC`, `EXACT`, `SEEDED`: ontology definition, ten synonym entries, one
parent, one PREGO attestation, 25 ranked associations and a seed event.
`PATHS.tsv:553` distinguishes this generic ontology record from three
path-qualified GOLD records. No GOLD count belongs to this target.

## Validation

- `just validate data/habitats/aquatic/intertidal_zone.yaml`: pass.
- `just validate-strict data/habitats/aquatic/intertidal_zone.yaml`: pass,
  zero errors.
- Minting PREGO's CURIE reproduces `habitatmech:PREGO.1e1d841752`.
- All 25 emitted IDs, labels, scores and ranks match the committed PREGO rows;
  candidate-pool values match the separate 53-taxon aggregate.
- NCBI taxonomy efetch resolves every displayed ID without an alias redirect;
  all 25 scientific names match. Strain/species ranks were not confused with
  the PREGO ranking field.
- Current OLS verifies the target and its direct parent. Official ENVO OWL
  was parsed as XML to verify all three synonym scopes.
- Full QC and network label correspondence passed on exact baseline
  `c72f4366a2889af57f75bb988d7b4dbedbd13655`, runs
  [37131516302](https://github.com/CultureBotAI/HabitatMech/actions/runs/37131516302)
  and 37131516268. Fresh local full QC is running, not claimed complete.

## Identity and Grounding

PREGO uses the ENVO identity itself. Its definition describes the shore area
alternately exposed and submerged by tides. The direct parent
`ENVO:01001201` marine environmental zone is a genuine broader geographic
zone, not liquid water. The current OLS definition and parent agree with
the committed ontology rows. `SEEDED` is honest: no target ITEM decision
was found. NOAA independently supports the tidal boundary, but its example
communities and subzones were not imported as universal record properties.
[ENVO target](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000316),
[marine environmental zone](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001201),
[NOAA](https://oceanservice.noaa.gov/facts/intertidal-zone.html).

The official ENVO OWL explicitly types `IntertidalZone` as exact, `coastal
zone` as broad, and `littoral zone` as related. OLS's flat `synonyms` list
contains all three, but its `obo_synonym` response contains only the exact
entry. That partial scoped response is not evidence that the other spellings
are absent or exact. The XML annotations settle their actual scopes.
ENVO separately defines littoral zone (`ENVO:01000407`) across sea, lake and
river shores; marine littoral zone (`ENVO:01000125`) includes a wider
cross-shore extent and has the intertidal zone as a part, not an equivalent.
[Official ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl).

## Evidence

`prego_habitats.tsv:220` gives 53 distinct taxa, maximum score 4 and channel
`annotated_genomes_isolates`. Its separate direct-assertion counter is 54;
the record correctly uses 53 with unit `TAXON`, not 54 organisms or samples.
The source label is ontology-derived by the seeder, while the synonym pipe
supplies seven distinct non-label PREGO related entries.

`prego_habitat_taxa.tsv:4588-4612` contains the 25 displayed associations,
all score 4, direct flag true, ranks 1-25, and the same channel. The
extractor's top-25 cap explains the difference from the candidate pool of
53; the other 28 identities are not recoverable from these retained rows.
Associations and scores do not establish universal or characteristic
presence. No organism-specific mechanism, measured parameter or citation
is asserted by this record.

## Completeness

Ignored-inclusive ID, minted source-ID, label and stem searches covered
curation, history, configuration, research, raw inputs and prior reports.
No target ITEM decision, authored definition, causal overlay, session history
or prior exact-target review was found. Broader research mentions and reviews
of GOLD descendants are leads, not reviews of this record. The structured
iModulonDB adapter returned 28 datasets; none matches the displayed
organisms/strains. In particular, Synechococcus elongatus is not WH 8016.
No module query was applicable; dataset absence is not negative evidence.

## Findings

1. **Major: broad and related ontology synonyms are promoted to exact.**
   ENVO's broad `coastal zone` and related `littoral zone` both become
   `EXACT_SYNONYM`. The untyped pipe in `data/raw/ontology_terms.tsv:6905`
   loses the distinction, and `ConceptStore.get` in `src/habitatmech/seed.py`
   unconditionally assigns exact scope. Owners: the governed ontology
   extraction contract in `src/habitatmech/extract.py` and seeder emission.

Zero blockers, one major finding, zero minor findings.

## Recommended Edits

Extend #1249 with this mixed-scope witness. Preserve exact `IntertidalZone`,
restore broad/related scopes from authoritative source assertions, and keep
PREGO's independent related entries. Do not infer scope from either a flat
synonym list or absence in OLS's partial scoped list. Retain the definition,
true parent, 53-TAXON aggregate and all 25 stored association rows.

## Follow-up Checks

Add regression coverage for exact/broad/related entries in one ontology term,
including unannotated synonyms omitted by the OLS scoped projection. Rebuild
the governed inventory and generated records, append history and pass
provenance, strict schema, label, corpus and full QC. Compare semantic-map
inputs: scope-only changes do not change the unique synonym spellings used
by the adapter, so map regeneration depends on the actual input diff.

## Additional Notes

The OBO download matched Git blob `98ec7d2b3161c7b8f4dd3c4c331a24c4a80e8565`,
but fastobo rejected an unrelated escaped-URL stanza. The official OWL XML
fallback succeeded; no failed parse was treated as evidence of absence.
Only this new review report was written; no corpus curation was performed.
