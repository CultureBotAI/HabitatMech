# YAML Record Review: oligotrophic water

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/oligotrophic_water.yaml`
- Started UTC: 2026-10-04T22:44:54Z
- Finished UTC: 2026-10-04T22:47:50Z
- Verdict: pass

## Target

Entire generated HabitatRecord ENVO:00002223, oligotrophic water,
AQUATIC/EXACT/SEEDED. The record has an ENVO definition/source, one PREGO
related plural synonym, one ontology parent, one 318-TAXON PREGO attestation,
25 retained taxon associations and one seed-history event. Parameters,
xrefs, evidence, graphs, discussions and datasets are absent.
PATHS.tsv:682 pins oligotrophic_water.

This is nutrient-poor water material, not a waterbody, a particular oligotrophic
lake/ocean zone or an assertion that every listed taxon is an obligate oligotroph.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/oligotrophic_water.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/oligotrophic_water.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Shared fresh batch PASS: 1,179 canonical, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | Shared PASS: 953 ungrounded records, 1,810 decisions. |
| `just qc` | Fresh local batch run remains active in tests beyond 93%; lint, documentation and raw provenance passed. No terminal result claimed. |
| Source/reference checks | Full target, actual PREGO decision route/full-field reproduction, all 14 raw tables, all 25 taxon-row comparisons, fresh NCBI Taxonomy for all IDs, current typed ENVO/OLS and entire page/semantic text. |

Full construction reproduces every target field with one source and zero
reviewed sources, including all 25 taxon rows and the single history event.
No individual ecological association was independently re-established from
original experiments; that limit is not hidden by schema or reproduction success.

## Identity and Grounding

Current [ENVO:00002223 oligotrophic water](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002223)
is active and agrees with the record's label and nutrient-poor-water definition.
Its named parent is current [ENVO:00002006 liquid water](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002006),
an environmental material. The committed term and subclass evidence are
physical ontology_terms.tsv:7300 and ontology_subclass_edges.tsv:5413.
No false source-context parent is present. Neither term specifies a universal
numeric nutrient threshold or restricts this material to fresh or marine water.

The actual source key is habitatmech:PREGO.29514450ca. Executing
prego_self_grounded plus current decision application keeps ENVO:00002223,
EXACT, reviewed=False and no mapping predicate. No maintained decision applies.
The source already uses the record's ontology ID, so predicate omission is
consistent with the attestation contract, not the #1398 minted-parent defect.
EXACT identifies the vocabulary alignment; SEEDED honestly leaves ecological
and curator endorsement separate.

The source inventory supplies oligotrophic water and oligotrophic waters.
The canonical label is not duplicated, and the plural survives conservatively
as RELATED_SYNONYM with PREGO provenance. No current ENVO synonym scope was
flattened into exactness, so no #1249 finding is supported. The historical
curation/samples/exact-20260814.tsv:21 ok sample is not an ITEM decision or
proof that these associations have been individually curated.

## Evidence

Physical prego_habitats.tsv:117 reports 318 distinct taxon identifiers,
318 direct assertions, maximum score 1.33315 and environmental_samples as
the source channel. These are separate aggregate fields, not 318 specimens,
independent experiments, species or demonstrated oligotrophs. The attestation
faithfully uses the taxon count and TAXON unit.

All 25 retained raw rows at prego_habitat_taxa.tsv:6306-6330 were compared
field by field. IDs, labels, scores and consecutive ranks 1-25 match; every
candidate_pool is 318. Scores range from 1.33315 to 1.27726. All retained
raw rows have direct_flag TRUE, environmental_samples and empty corroboration.
No emitted row sets is_characteristic or claims cross-source corroboration.

The inspected extractor keeps the maximum score per habitat/taxon pair,
combines channels and truncates the score-ranked list while retaining the
full pool count. The seeder copies the retained provenance without converting
scores into probabilities or biological effect sizes. The top 25 are not
the entire 318-member inventory, and direct_flag is not a synonym for
independently proven characteristic occurrence.

Fresh [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=644107,314262,556484,246200,388399,313598,228405,351016,2850,583355,313594,237727,216432,290400,313590,756272,394221,443152,243090,398720,768066,313596,688270,384765,391624&retmode=xml)
returned all 25 requested IDs directly, with all 25 labels matching current
scientific names. Several historical aliases were present, but none required
an ID redirect or label repair. The retained set contains species and strain
taxa; Phaeodactylum tricornutum and its CCAP 1055/1 strain are distinct nested
taxonomic entries, not two independent species. Their eukaryotic lineage is
not a reason to delete valid source associations from a microbial-habitat record.

Taxonomy resolution proves identifiers and labels, not oligotrophic ecology.
The [PREGO site](https://prego.hcmr.gr/) request timed out. The committed
aggregate/top-taxon rows contain no per-association primary-study accession
to inspect, and those experiments were not reconstructed or fabricated.
No gene/regulator/expression assertion makes iModulonDB applicable here.

The exact-ID scan covered all 14 raw tables. Only the PREGO rows and ontology
term/subclass rows match; no GOLD, BacDive, MADIN or environmental-parameter
contribution feeds this target. The full generated page explicitly describes
the taxa as reported associations, weaker than characteristic presence, and
shows rank/pool plus the unreviewed warning. The semantic text likewise uses
observed-taxon lines, not characteristic-trait assertions.

## Completeness

Ignored-inclusive ID, minted key, label/plural/stem and filename searches
covered curation, conf, history, research, reports, all raw inventories,
PATHS and RETIRED. They found the historical sample row and expected source/
ontology/path rows, but no ITEM decision, target definition request, overlay,
dedicated research, session history, retirement or earlier individual review.

The inherited definition and true material genus suffice for present identity.
Optional empty measurements and mechanisms are appropriate; no numeric nutrient
cutoff, salinity, geographic range, organism requirement or causal graph should
be added merely to enrich the record. SEEDED must remain distinct from this
read-only report's bounded pass.

## Findings

None found in the checked identity, ontology hierarchy, source projection,
taxonomic references, synonym provenance or status/history derivation.

Counts: zero blockers, zero major, zero minor. This pass does not certify
all 318 underlying ecological associations or downstream SSSOM/KGX products.

## Recommended Edits

No supported correction is required by this audit. Preserve the ontology
identity/genus, PREGO source ID, all count/score/channel/rank/pool semantics,
all retained taxa and the honest unreviewed status. Do not promote taxa to
characteristic without claim-level evidence or collapse species/strain IDs
merely because their names overlap.

If future evidence supports an ITEM endorsement, use the exact PREGO source
key in curation/decisions.tsv and append new history; an old sample-table ok
entry or this report is not a substitute. Source changes belong in governed
upstream extraction/inventories, never manually in the generated YAML.

## Follow-up Checks

For a future change, canary ENVO:00002223, compare every retained taxon and
aggregate field, run ordinary/strict/products/history/provenance checks,
exact reproduction, generated-site checks and full QC. Verify original
association evidence before ecological endorsement. Recompute actual
semantic inputs for any proposed correction; no change was needed or
simulated as a repair in this audit. Preserve protected #1218/runtime pins.

## Additional Notes

All-state exact-ID/label issue search returned no matching issue. No new
scientific issue is warranted by this bounded pass. Official typed ENVO OWL
SHA-256: `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No scientific input, generated output, old report/history, paid research or
GitHub item changed during this individual review.
