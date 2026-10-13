# YAML Record Review: marine cold seep biome

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/marine_cold_seep_biome.yaml`
- Started UTC: 2026-10-03T19:03:22Z
- Finished UTC: 2026-10-03T19:04:21Z
- Verdict: pass

## Target

Read the entire generated HabitatRecord, `ENVO:01000127`, marine cold seep
biome, AQUATIC, EXACT, SEEDED. PREGO is the sole source; its computed key is
`habitatmech:PREGO.3bcdbfe42a`. `data/habitats/PATHS.tsv:779` pins the stem.
Only the deterministic seed event is present, not an ITEM review.

## Validation

- `just validate data/habitats/aquatic/marine_cold_seep_biome.yaml`: pass.
- `just validate-strict data/habitats/aquatic/marine_cold_seep_biome.yaml`:
  one file, zero errors.
- Fresh full `just qc` was still active at review finish; lint, documentation
  and raw provenance passed. Later checks were not yet confirmed complete.
- Inspected the target, marine-benthic parent and cold-seep feature in current
  official ENVO OWL, fetched and byte-verified this batch, SHA-256
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
- All 17 current NCBI IDs resolve directly without aliases; names match.
  Structured comparison verified every retained PREGO row.
- Required CI will run OAK correspondence; it does not independently verify
  source-taxon ecology.

## Identity and Grounding

ID, label, definition and sole named parent `ENVO:01000024` agree with
`data/raw/ontology_terms.tsv:7633`,
`data/raw/ontology_subclass_edges.tsv:5777` and
[official ENVO](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl).
The biome has a cold-seep feature (`ENVO:01000263`); it is not identical to
that feature. The feature must not be substituted for the biome identity or
promoted from a part relation to an is-a parent. PREGO's two alternate strings
are related synonyms, with no stronger ontology synonym claim.

## Evidence

`data/raw/prego_habitats.tsv:303` reports 17 distinct taxa, 17 direct
assertions, maximum score 1.41893 and environmental_samples. The YAML's
TAXON count and channel agree. All 17 candidate rows at
`data/raw/prego_habitat_taxa.tsv:7704-7720` are displayed. IDs, names, scores,
ranks 1-17 and pool 17 agree individually; raw direct flags are TRUE and
corroboration is absent. None is marked is_characteristic.

[NCBI efetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=563043,110163,523849,2264,46539,119394,758583,442956,212050,688066,2423,29292,53953,129958,28223,703612,126741)
confirms all displayed IDs/names, including 703612 Bacillus spizizenii ATCC
6633 = JCM 2499. These checks establish source projection and valid taxonomy,
not characteristic ecology. The original environmental-sample evidence was
not inspected; names associated with thermal environments are not, by
themselves, grounds to delete a source assertion or replace the biome with a
hydrothermal-vent identity.

The target also appears as a GOLD broad-scale term in
`data/raw/gold_path_triads.tsv:134`, `:458` and `:461`, including distinct
Cold seeps and Cold seeps > Sediment paths. Those contextual rows are not
additional source attestations for this PREGO record, and their counts must
not be added to the 17-TAXON aggregate. The earlier cold_seep review is about
the feature, not this biome, and was used only as a lead.

## Completeness

Ignored-inclusive searches for ID, source key, label and stem covered
curation, history, raw inventories, PATHS, research and individual reports.
No target ITEM decision, authored definition, causal overlay, dedicated
history or prior individual target review was found. SEEDED is appropriate.
The target has no optional measurements, evidence, graphs, discussions or
datasets; generic seep biology does not justify filling these fields.

iModulonDB is not applicable: no gene, regulator, expression dataset or
mechanistic claim is made. No other target is counted as reviewed here.

## Findings

None verified for this identity and source-attributed projection. Blockers:
0. Major: 0. Minor: 0. This bounded pass does not establish the original
ecological basis of the 17 PREGO associations.

## Recommended Edits

No immediate record edit is justified by the inspected evidence. Before
stronger ecological use, trace the original PREGO sample assertions. Any
supported correction belongs in governed source inputs and extraction, not
generated YAML. Do not merge the feature, biome and sediment merely because
they share a broad-scale annotation.

## Follow-up Checks

Complete full local QC and required CI before report merge. A later source
refresh must preserve rank, score, pool, provenance and observational status;
then canary, validate provenance/schema/history/labels, verify corpus and
regenerate affected map/site products through the normal guarded workflow.

## Additional Notes

Known parent-record findings #1279/#1280 do not invalidate this target's
genuine direct marine-benthic parent, nor does this pass endorse all claims
in that parent record. No scientific input, generated record, page, status
or history was changed.
