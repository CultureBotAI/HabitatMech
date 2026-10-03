# YAML Record Review: marine oligotrophic desert

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/marine_oligotrophic_desert.yaml`
- Started UTC: 2026-10-03T19:37:20Z
- Finished UTC: 2026-10-03T19:39:14Z
- Verdict: pass

## Target

Read the complete generated HabitatRecord, `ENVO:01000073`, marine
oligotrophic desert, AQUATIC, EXACT, SEEDED. PREGO is the sole source;
computed key `habitatmech:PREGO.74afff3700`.
`data/habitats/PATHS.tsv:773` pins the filename. Only the seed event is
present, not an ITEM review.

## Validation

- `just validate data/habitats/aquatic/marine_oligotrophic_desert.yaml`:
  pass.
- `just validate-strict data/habitats/aquatic/marine_oligotrophic_desert.yaml`:
  one file, zero errors.
- Fresh full `just qc` was still running tests at review finish. Lint,
  documentation and raw provenance passed; later gates were not yet complete.
- Inspected target and parent in current official ENVO OWL, fetched and
  byte-verified this batch, SHA-256
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
- Current NCBI efetch resolved all 25 displayed IDs directly. All 21 supplied
  scientific names match; four optional labels are blank in both inputs and
  output. Structured CSV/YAML comparison passed for every retained row.
- OAK correspondence is deferred to required CI; it does not verify ecology.

## Identity and Grounding

ID, label, full definition and sole parent agree with
`data/raw/ontology_terms.tsv:7580`,
`data/raw/ontology_subclass_edges.tsv:5712` and
[official ENVO](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl).
`ENVO:01000686` is marine water mass. The target denotes nutrient-poor marine
water, not a terrestrial desert, an organism, or a biome identity inferred
from the word desert. Its source-attributed plural synonym is RELATED_SYNONYM.

The current ontology has additional part-of/composition restrictions; these
are not silently promoted to is-a parents. No GOLD context contributes an
extra whole-waterbody parent to this PREGO-only record.

## Evidence

`data/raw/prego_habitats.tsv:199` gives 81 distinct taxa, 81 direct assertions,
maximum score 1.25361 and environmental_samples. The YAML's TAXON aggregate,
score and channel match. The two equal counts represent different quantities
and should not be treated as interchangeable in general.

All displayed entries at `data/raw/prego_habitat_taxa.tsv:7604-7628` match
the raw IDs, optional labels, scores, ranks 1-25 and pool 81. Direct flags
are TRUE, channels are environmental_samples and corroboration is empty.
None is marked is_characteristic. The other 56 candidates were not reviewed.

[NCBI Taxonomy efetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=3068,313595,583355,1774373,756272,243090,391625,378806,240016,313606,7955,225937,575540,530564,502025,216432,314230,443152,504472,344747,3055,518766,313603,45351,264462)
returns all IDs without alias redirects. The supplied names, including
Allostigmatella aurantiaca DW4/3-1 and Rubinisphaera brasiliensis DSM 5305,
match. The four source blanks resolve to Volvox carteri f. nagariensis,
Danio rerio, Chlamydomonas reinhardtii and Nematostella vectensis. Optional
blank labels are not evidence of broken identifiers or permission to invent
microbial labels.

Original sample evidence was not independently inspected. Neither valid
taxonomy nor faithful PREGO projection establishes characteristic ecology;
an unusual association alone is also insufficient grounds for deletion.

## Completeness

Ignored-inclusive searches covered the ID, source key, label and stem in
curation, history, raw inventories, PATHS, research and individual reports.
No target ITEM decision, term request, causal overlay, dedicated history or
prior individual target report was found. SEEDED is consistent with that.

Optional measurements, evidence objects, graphs, discussions and datasets
are absent. The definition supports low nutrient concentrations but does not
justify invented quantitative thresholds or universal oxygen measurements.
iModulonDB is not applicable: no gene, regulator, expression dataset or
mechanistic claim is present.

## Findings

None verified for identity and source-attributed projection. Blockers: 0.
Major: 0. Minor: 0. This bounded pass does not verify the original ecological
basis of the displayed associations.

## Recommended Edits

No immediate record correction is justified. Trace original PREGO sample
assertions before stronger ecological use; supported changes belong in
governed source inputs/extraction, not generated YAML. Preserve ranks,
scores, pool size and observational status in any future refresh.

## Follow-up Checks

Complete full local QC and required CI before report merge. Any future source
change needs provenance checks, canary inspection, schema/history/OAK
validation, corpus reproduction and regenerated affected map/site products.

## Additional Notes

An initial ad hoc comparison used an incorrect raw-column name and stopped
before fetching NCBI. After reading the TSV headers, the corrected comparison
completed successfully. No scientific input, generated record, page, status or
history changed; no other record is counted as reviewed here.
