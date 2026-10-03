# YAML Record Review: hydrothermal fluid

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/hydrothermal_fluid.yaml`
- Started UTC: 2026-10-03T12:12:51Z
- Finished UTC: 2026-10-03T12:22:53Z
- Verdict: pass

## Target

The complete generated `HabitatRecord` was read: `ENVO:01000134`, hydrothermal
fluid, `AQUATIC`, `EXACT`, `SEEDED`. It contains an ENVO definition, one PREGO
plural synonym, the leachate parent, one PREGO attestation, 25 source-associated
taxa, and one seed-history event. `PATHS.tsv:781` locks the stem; the source
key recomputes to `habitatmech:PREGO.e843d390ae`.

## Validation

- `just validate data/habitats/aquatic/hydrothermal_fluid.yaml`: pass.
- `just validate-strict data/habitats/aquatic/hydrothermal_fluid.yaml`:
  one record, zero errors.
- Structured comparison of every complete taxon dictionary against the PREGO
  inventory: all 25 match, including names, ranks, scores, and pool sizes.
- Live OLS verified both ontology terms, their definitions, non-obsolete
  status, and the direct parent. NCBI EFetch returned all 25 IDs unchanged;
  every source name matched a current name or alias.
- Baseline `just qc`: all gates passed; 451 tests passed, three skipped,
  two dependency warnings; 3,206 records reproduce and validate, with current
  site/redirects. OAK label correspondence is a separate CI gate.
- No literature citation, gene, pathway, or causal edge is asserted on this
  record; a literature-reference or iModulonDB check is not applicable.

## Identity and Grounding

The PREGO ID, canonical label, ontology definition, and exact grounding agree.
This is the material flowing from a vent, not the vent structure, a plume, or
a thermophilic-sediment class. The current definition describes heated water
that acquired dissolved material through crustal percolation.
[Hydrothermal fluid](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000134).

`ENVO:00002141` leachate is a supported broader material class: it covers
liquid produced by water percolating through permeable material.
The vendored edge at `data/raw/ontology_subclass_edges.tsv:5784` and live OLS
agree. This is not a water-body/constituent conflation.
[Leachate](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002141).

No target ITEM decision was found, so `SEEDED` is correct. This review does
not promote the generated mapping status.

## Evidence

| Claim | Inspected support and limits |
|---|---|
| Definition and hierarchy | `ontology_terms.tsv:7640` supplies the exact hydrothermal-fluid definition; row 7237 supplies leachate. Both match current ontology records. |
| Source attestation | `prego_habitats.tsv:188` has 99 taxa, a separate 99 direct-assertion count, score 3, and `annotated_genomes_isolates`. The generated count remains TAXON. |
| Plural synonym | The same PREGO row contains `hydrothermal fluids`, correctly emitted as a related source synonym rather than an additional ENVO exact synonym. |
| All 25 taxon entries | `prego_habitat_taxa.tsv:7722-7746` supplies the selected rank-1-to-25 entries. Every score is 3; rank is the source order, not demonstrated abundance or physiological preference. |
| Taxon identity | All 25 current taxonomy records resolved and matched the supplied names/aliases. These observations do not establish characteristic status, in situ activity, or a common metabolism for all listed taxa. |

The sampled list is only 25 of the source's 99 candidates. It correctly makes
no `is_characteristic` claim. Names such as Archaeoglobus sp. JdFR-22 do not
authorize a new metabolic edge without separate organism-specific evidence.

## Completeness

No measured temperature, metal concentration, pressure, or salinity is provided;
the definition does not justify inventing numeric parameter ranges. No optional
mechanism, discussion, or dataset field needs to be filled for this seed record.

Hidden/ignored-inclusive ID/label/stem searches covered curation, history,
research, configuration, ontology and PREGO inventories, and the path lock.
No target-specific decision, term request, research report, or session history
was found. The maintained `hydrothermal_vent.yaml` overlay mentions this fluid
as a node but targets another record; it is not a missing overlay to copy here.
Exact report-header coverage, including ignored files, found no prior individual
review of this record.

## Findings

None found. Zero blockers, major findings, or minor findings. The verdict is
limited to the represented source associations and ontology claims; it does
not independently validate each underlying genome's ecological annotation.

## Recommended Edits

None required. Preserve the material identity, ontology-derived leachate parent,
source count/unit and channel, and non-characteristic interpretation of taxa.

## Follow-up Checks

At a future source refresh, recheck the exact PREGO row and all selected taxa,
then run inventory provenance checks, focused strict validation, and
`just verify-corpus`. New quantitative or causal claims would require their own
inspected source evidence and maintained curation inputs. Run normal map/site
freshness and full QC gates if any semantic fields are subsequently changed.

## Additional Notes

The record is a valid seeded association aggregate, not an ITEM-curated
mechanism dossier. No corpus, generated product, decision, or history was edited.
