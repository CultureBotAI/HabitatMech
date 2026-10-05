# YAML Record Review: Saline Evaporation Pond

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/saline_evaporation_pond.yaml`
- Started UTC: 2026-10-05T03:10:00Z
- Finished UTC: 2026-10-05T03:17:42Z
- Verdict: needs curation

## Target

Entire generated HabitatRecord ENVO:00000055, saline evaporation pond,
AQUATIC/EXACT/REVIEWED: ENVO definition, 14 source-typed synonym entries,
two parents, GOLD and PREGO attestations, eight PREGO taxa and three history
events. PATHS.tsv:461 pins the filename. Parameters, xrefs, record-level
evidence, graphs, discussions and datasets are absent.

GOLD node 7709 denotes Environmental > Aquatic > Marine > Intertidal zone >
Salt pond. It contributes ten ORGANISM assertions and skos:closeMatch.
PREGO contributes its ENVO:00000055 node, eight TAXON assertions, score 3
and annotated_genomes_isolates. Unlike counts are not summed. Salt pond
sediment and non-marine salt-crystallizer source cohorts are not this source.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/saline_evaporation_pond.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/saline_evaporation_pond.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Shared fresh PASS: 1,179 canonical, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | Shared PASS: 953 ungrounded records, 1,810 decisions. |
| `just qc` | Fresh run reached terminal PASS during this review: 457 tests passed, three skipped, two warnings; 90 valid history records; zero missing/extra/different corpus records; site, redirects and term requests passed. |
| Source/reference checks | Whole-document reproduction, executed source and parent routes, all 14 raw inventories for exact GOLD source keys, typed ENVO/current OLS, eight current NCBI identifiers, original abstracts and culture-collection entries, whole contextual parent and rendered page. |

Full generated-document equality passed with two source concepts and two
ITEM-reviewed sources, including all eight taxa and three history events.
The QC log is /private/tmp/habitatmech-sabkha-saline-qc-20261005.log.
No new scientific input or generated artifact was written.

## Identity and Grounding

Active [ENVO:00000055](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000055)
denotes a shallow artificial pond for producing salt by evaporating seawater.
The definition matches ontology_terms.tsv:6649. Its true ontology parent,
active [ENVO:00000033 pond](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000033),
is reproduced from ontology_subclass_edges.tsv:4683 and must remain.

GOLD minting gives habitatmech:GOLD.dc339d2180; the actual gold_leaf_synonym
CLOSE/skos:closeMatch result is endorsed by ITEM REVIEW at decisions.tsv:1220.
PREGO's habitatmech:PREGO.2a96f3bb8b has ITEM REVIEW at row 1418. Its
self-grounded ENVO identity supplies the aggregate EXACT state; that state
does not mean GOLD itself has an exact mapping. Both August 13 reviews and
the August 16 seed event are faithfully generated. This GOLD source and
target have distinct identifiers: the retained-minted endpoint defect in
#1398 is not reproduced by this closeMatch attestation.

Typed official ENVO distinguishes the following assertions:

| ENVO spelling | Typed source scope | Generated scope |
| --- | --- | --- |
| lake | broad | exact |
| salt evaporation pond | exact | exact |
| salt pond | related | exact |
| salt ponds | related | exact |
| saltern | related | exact |

The untyped ontology inventory and seed.py:406-407 inflate four scopes.
The genuine exact assertion must not be downgraded as a shortcut. PREGO's
eight related aliases and GOLD's separately sourced label alias are distinct
assertions; this typed-ENVO finding does not justify changing them globally.

The other parent, habitatmech:GOLD.115edc36f8, is the marine Intertidal zone
source. Its complete YAML and prior review were read as context, not as a
new individual target. Actual gold_narrower_than_leaf_match retains that
minted parent. seed.py:898-907 then contributes it to the merged pond class.
[NOAA](https://oceanservice.noaa.gov/facts/intertidal-zone.html) describes
the intertidal zone by shore position and tidal exposure. A seawater-fed
artificial evaporation pond is not thereby a kind of that zone, and this
ENVO class has no universal between-tidal-marks restriction. The GOLD path
can preserve one source's setting without making it a superclass for every
merged pond. The parent's own outgoing waterbody problem is separate.

## Evidence

Physical gold_ecosystem_paths.tsv:522 contains one depth-five node with ten
organisms and zero study/biosample counters. All 14 raw inventories were
scanned for this exact GOLD path/node: only the tree row matched. No exact
GOLD bulk-sample, complete-triad, study or parameter contribution was found.
Current official GOLD node 7709 returned 404; retirement was not established.

prego_habitats.tsv:353 records eight taxa, eight direct assertions and score
3. prego_habitat_taxa.tsv:3566-3573 supplies the eight rows below, each with
direct_flag TRUE, score 3, rank 1-8, candidate pool eight and no imported
corroboration. These reproduce exactly. Current NCBI EFetch resolves all
eight IDs to the record's exact labels: six are strain-ranked and the two
Candidatus/Kushneria entries are species-ranked. The rank difference is not
a habitat-specificity ranking.

| Taxon ID and generated label | Inspected source support and limits |
| --- | --- |
| NCBITaxon:1121463, Desulfobaculum senezii DSM 8436 | [JCM 16814](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=16814) explicitly equates DSM 8436/CVL and gives the Chula Vista solar saltern as source. |
| NCBITaxon:1121942, Modicisalibacter ilicicola DSM 19980 | Original abstract, [PMID:19244445](https://pubmed.ncbi.nlm.nih.gov/19244445/), DOI:10.1099/ijs.0.003509-0, links SP8 to DSM 19980 and saline water from Santa Pola solar salterns. The [DSM entry](https://www.dsmz.de/collection/catalogue/details/culture/DSM-19980) independently retains that source under Halomonas ilicicola. |
| NCBITaxon:1123236, Salinimonas chungwhensis DSM 16280 | Inspected [original publisher abstract](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.63279-0), DOI:10.1099/ijs.0.63279-0, links BH030046 to DSM 16280 and a Korean solar saltern. |
| NCBITaxon:1385511, Pontibacillus marinus BH030004 = DSM 16465 | Original abstract, [PMID:15879229](https://pubmed.ncbi.nlm.nih.gov/15879229/), DOI:10.1099/ijs.0.63489-0, explicitly links the strain aliases and Korean solar-saltern isolation. It does not establish water-column-only occurrence. |
| NCBITaxon:184067, Kushneria indalinina | Original abstract, [PMID:17267982](https://pubmed.ncbi.nlm.nih.gov/17267982/), DOI:10.1099/ijs.0.64702-0, describes type strain CG2.1 from Cabo de Gata solar saltern. NCBI associates this type with the current species name; one strain's occurrence is not universality across species members. |
| NCBITaxon:257501, Candidatus Chlorotrichoides halophilum | NCBI retains Chlorothrix halophila among the names. Original [PMID:14655000](https://pubmed.ncbi.nlm.nih.gov/14655000/), DOI:10.1007/s00203-003-0615-7, concerns enriched hypersaline-mat material; inspected [PMID:17369303](https://pubmed.ncbi.nlm.nih.gov/17369303/), DOI:10.1128/JB.01711-06, specifies Guerrero Negro. The inspected abstracts alone do not recover the precise pond/sample annotation underlying PREGO. |
| NCBITaxon:290398, Chromohalobacter israelensis DSM 3043 | [DSM 3043](https://www.dsmz.de/collection/catalogue/details/culture/DSM-3043) links 1H11 to a Bonaire solar salt facility, using the older C. salexigens name. [LPSN](https://lpsn.dsmz.de/species/chromohalobacter-salexigens) treats salexigens as a later heterotypic synonym of israelensis; do not revert the current NCBI label merely to match the older catalogue heading. |
| NCBITaxon:469382, Halogeometricum borinquense DSM 11551 | [DSM 11551](https://www.dsmz.de/collection/catalogue/details/culture/DSM-11551) links PR3 to Puerto Rican solar salterns, consistent with the current NCBI strain identity. |

Taxonomic opinions need not be synchronized across databases. For example,
[LPSN](https://lpsn.dsmz.de/species/salinimonas-chungwhensis) prefers the
homotypic Alteromonas combination while NCBI retains Salinimonas; DSM 19980
uses Halomonas while NCBI uses Modicisalibacter. These are not evidence that
the record points to a different isolate. Preserve identifier provenance.

The sources support bounded saltern/mat occurrences, not characteristic
abundance, identical sampling media or the recovered PREGO accession chain.
No is_characteristic flag is set; schema and rendered page correctly say
associated/reported-from. Do not convert culture optima to general pond
salinity, temperature or pH. No gene/regulator/expression claim makes
iModulonDB applicable. Enrichment-source uncertainty is recorded above,
not promoted to a proven false taxon association.

## Completeness

Ignored-inclusive ID, source-key/path, label and filename searches covered
curation, conf, history, research, individual reports, raw inventories,
PATHS and RETIRED. Both ITEM decisions were found, but no exact-target
definition overlay, xref row, causal overlay, dedicated research/session
history, retirement or prior individual review was found. Generic pond
and microbial-mat reports and non-marine research are context only.

The ENVO ID also occurs as a local-scale modal triad term for different
salt-crystallizer-pond and mat paths at gold_path_triads.tsv:741,744. Those
63- and 12-sample cohorts are not additional observations for GOLD 7709.
Likewise Salt pond sediment's bulk/study rows do not fill this target's gaps.
Empty optional mechanisms, discussions and datasets are not defects.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | Four typed broad/related ENVO aliases are inflated to exact synonyms; salt evaporation pond itself is correctly exact. | Typed ontology source/extraction contract and src/habitatmech/seed.py:406-407; existing #1249. |
| Major | A source-specific intertidal-zone setting is emitted as a strict superclass of the generic saline evaporation pond class. | Exact-source parent control for GOLD.dc339d2180 in src/habitatmech/seed.py:898-907; preserve its attestation and real ENVO pond parent. |

Zero blockers, two major findings, zero minor. No wrong stable taxon ID,
characteristic-taxon overclaim or additional #1398 witness is established.

## Recommended Edits

1. Recover typed scopes through #1249's governed source contract; preserve
   verified exact, separately sourced and PREGO-related assertions.
2. Suppress only the unsupported GOLD source-parent contribution to this
   merged class. Keep ENVO identity, pond superclass, definition, both source
   attestations, ten ORGANISM/eight TAXON counts and eight taxa. Do not replace
   all inherited parents or exact-merge separate sediment/material records.
3. Retain the bounded taxon provenance caveats. Recover PREGO sample/genome
   annotations before adding corroboration, specificity or experimental
   habitat parameters. No automatic taxon deletion is justified here.

## Follow-up Checks

Dry seed and inspect `just seed-canary ENVO:00000055 --force`. Regress typed
synonym distinctions, false-zone suppression, true-pond retention, two-source
ITEM accounting and unchanged counts/taxon IDs. Append required curation
history, regenerate with guarded writers and pass ordinary/strict/products,
provenance/history, exact corpus reproduction, site and full QC.

Actual full-context zone-parent removal changes semantic text, whereas
predicate-only omission is neutral; neither probe changed files. A real
hierarchy correction needs the genuine #1217 map/site refresh while keeping
protected draft #1218 and runtime pins isolated. SSSOM/KGX exports were not
executed or certified compatible by this review.

## Additional Notes

All-state exact ontology/source-ID and saline-evaporation searches returned
generic-pond issue #1427, not this child's intertidal edge. Existing #1249
owns synonym scope. #1398 was read and distinguished from this close mapping.
No GitHub item was mutated during the individual review.

Some browser PubMed/PMC pages returned challenges. NCBI API retrieval of the
inspected abstracts succeeded; an initial batch hit HTTP 429 after its first
three records, then the remaining requested abstracts were retrieved in a
later call. Full articles and the precise PREGO annotation chain were not
inspected. DSM 19980 was read with the standard HTML parser after browser
access failed. No paid research or dependency installation was used.

Typed official ENVO OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
