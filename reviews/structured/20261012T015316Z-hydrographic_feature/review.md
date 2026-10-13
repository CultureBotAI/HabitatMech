# Scientific record review: hydrographic_feature

- Review: 20261012T015316Z-hydrographic_feature
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-12T01:35:44.699592Z
- Finished UTC: 2026-10-12T01:53:16.410488Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The PREGO record names the broad ENVO geographic feature associated with water, not a particular river or water material. Its geographic-feature genus is supported. Official fluvial feature is related rather than exact; several PREGO lexical variants are malformed. Scores around 1.8 rank associations from a 1427-taxon pool and are not occurrence probabilities.

## Scope And Provenance

Entire exact generated record, all contributors and individual asserted mechanism edges, with bounded source-context assessment.

Selection: Next forty records without a completed individual scientific review in stable repository-relative path order: estuary variants through hydrothermal fluid. Full individual observations, not a category-wide pass. Starting observation coverage608/3208 is not clean current-input coverage.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 51e0d6e3e3429b8cf601667b9097daba848f5326.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| ENVO:00000012 | data/habitats/aquatic/hydrographic_feature.yaml | generated | hydrographic feature |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native gate on captured scientific inputs | passed | True | ENVO:00000012 | Actual success from 2026-10-12T01:38:40.243463Z to 2026-10-12T01:38:42.914558Z. Native scope retained. |
| Native gate on captured scientific inputs | passed | True | ENVO:00000012 | Actual success from 2026-10-12T01:38:45.606215Z to 2026-10-12T01:38:54.204186Z. Native scope retained. |
| Native gate on captured scientific inputs | passed | True | ENVO:00000012 | Actual success from 2026-10-12T01:38:54.205107Z to 2026-10-12T01:39:22.495898Z. Native scope retained. |
| Native gate on captured scientific inputs | passed | True | ENVO:00000012 | Actual success from 2026-10-12T01:39:22.510128Z to 2026-10-12T01:40:40.416231Z. Native scope retained. |
| Native gate on captured scientific inputs | passed | True | ENVO:00000012 | Actual success from 2026-10-12T01:40:40.417502Z to 2026-10-12T01:40:49.459346Z. Native scope retained. |
| Native gate on captured scientific inputs | passed | True | ENVO:00000012 | Actual success from 2026-10-12T01:40:49.460754Z to 2026-10-12T01:40:54.753371Z. Native scope retained. |
| Native gate on captured scientific inputs | passed | True | ENVO:00000012 | Actual success from 2026-10-12T01:40:54.754493Z to 2026-10-12T01:41:21.741599Z. Native scope retained. |
| Native gate on captured scientific inputs | passed | True | ENVO:00000012 | Actual success from 2026-10-12T01:41:21.742805Z to 2026-10-12T01:41:22.498024Z. Native scope retained. |
| Native gate on captured scientific inputs | passed | True | ENVO:00000012 | Actual success from 2026-10-12T01:37:32.943507Z to 2026-10-12T01:37:35.068708Z. All three required merge-group workflows passed at the exact captured base; authoritative QC passed 856 tests with 3 skipped. Newly saved review bundles require their own integrity check. Exact-base CI receipt; these new review bundles were not part of that CI run. |
| Complete target reconstruction | passed | False | ENVO:00000012 | All40 complete documents matched; captured input hashes verified again before authoring. |
| Original assertion membership | unavailable | False | ENVO:00000012 | Bounded ignored-inclusive searches did not recover the complete original assertion inputs. Later exports supply context only. |
| Structured expression applicability | not_applicable | False | ENVO:00000012 | No organism/dataset-specific gene, regulator or expression-module assertion in this habitat record; database absence is not negative habitat evidence. |

## Scientific And Domain Assessments

### Exact identity, definition and source intent

identity: supported. Targets: ENVO:00000012.

The PREGO record names the broad ENVO geographic feature associated with water, not a particular river or water material. Its geographic-feature genus is supported. Official fluvial feature is related rather than exact; several PREGO lexical variants are malformed. Scores around 1.8 rank associations from a 1427-taxon pool and are not occurrence probabilities.

### All parent contributions and mapping scope

grounding: supported. Targets: ENVO:00000012.

The PREGO record names the broad ENVO geographic feature associated with water, not a particular river or water material. Its geographic-feature genus is supported. Official fluvial feature is related rather than exact; several PREGO lexical variants are malformed. Scores around 1.8 rank associations from a 1427-taxon pool and are not occurrence probabilities. Ontology, GOLD path, ambiguous-leaf and authored-genus contributions were distinguished.

### Source units, decision ownership and native lifecycle

provenance: supported. Targets: ENVO:00000012.

Complete reconstruction preserves 1 source concepts and 0 ITEM-reviewed contributors. Attestations=[{"source": "PREGO", "source_id": "ENVO:00000012", "source_label": "hydrographic feature", "assertion_count": 1427, "assertion_unit": "TAXON", "score": 1.81611, "evidence_channels": "environmental_samples"}]. Unlike units are not summed; omitted direct counts do not imply ecological absence. This review does not change native status.

### Association versus characteristic presence

evidence: supported. Targets: ENVO:00000012.

All emitted taxon IDs resolve, including merged identifiers and historical spellings. Full reconstruction preserves source pools, ranks, scores and corroborations; displayed taxa are selected associations, not exhaustive occurrence evidence. No is_characteristic assertion is present. A source score is not a probability or habitat abundance.

### Optional slots and evidence boundaries

completeness: supported. Targets: ENVO:00000012.

Missing optional definitions or datasets alone do not establish defects. No causal graph is asserted in this exact record; ignored-inclusive overlay search and the causal corpus gate were checked. Habitat associations without named gene/regulator or transcriptome claims do not justify an iModulon query.

## Findings

### F1: Non-exact ontology synonyms are promoted to exact

major / open / confirmed; issue key: envo-00000012-ontology-synonym-scope.

fluvial feature: RELATED, not EXACT. The PREGO record names the broad ENVO geographic feature associated with water, not a particular river or water material. Its geographic-feature genus is supported. Official fluvial feature is related rather than exact; several PREGO lexical variants are malformed. Scores around 1.8 rank associations from a 1427-taxon pool and are not occurrence probabilities.

### F2: Malformed inherited lexical variants are retained

minor / open / confirmed; issue key: envo-00000012-malformed-source-alias.

OVERFALLSs, overfallses, overfallsic and tidal ripp/ripps are source lexical artifacts, not alternative habitat identities.

## Recommended Actions And Acceptance Checks

### A1

Resolve shared1249 through governed typed-synonym ingestion and consumer tests; retain genuine exact names and PREGO related aliases instead of globally downgrading all synonyms.

- Change only maintained inputs after source-level assessment; preserve independent true parents, identities, source counts/units and lifecycle.
- Append required history, add focused regressions, inspect a seed canary and regenerate affected products without hand-editing records or pages.
- Pass schema, strict, product-label, corpus reproduction, causal/history, review-integrity and full QC; save a linked successor for every finding disposition.

### A2

Trace and correct the exact lexical artifacts through source handling while preserving valid aliases, source identity and scoring.

- Change only maintained inputs after source-level assessment; preserve independent true parents, identities, source counts/units and lifecycle.
- Append required history, add focused regressions, inspect a seed canary and regenerate affected products without hand-editing records or pages.
- Pass schema, strict, product-label, corpus reproduction, causal/history, review-integrity and full QC; save a linked successor for every finding disposition.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R | data/habitats/aquatic/hydrographic_feature.yaml; Entire captured YAML read, including provenance, parameters, taxa, graphs and generated history | supports | The PREGO record names the broad ENVO geographic feature associated with water, not a particular river or water material. Its geographic-feature genus is supported. Official fluvial feature is related rather than exact; several PREGO lexical variants are malformed. Scores around 1.8 rank associations from a 1427-taxon pool and are not occurrence probabilities. |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; src/habitatmech/schema/habitatmech.yaml | supports | Applied exact identity, strict-parent, MIxS-role, source unit/score and ITEM lifecycle contracts. STATE is a cellular value, not the process establishing it. Evidence is assessed at edge scope. |
| RAW | data/raw; curation/decisions.tsv; curation/term_requests.tsv; curation/gold_parent_exclusions.tsv; Exact logical TSV rows; header is row1; unrelated neighbor matches excluded | supports | {"data/raw/ontology_subclass_edges.tsv": [{"data": {"object": "ENVO:00000000", "predicate": "rdfs:subClassOf", "subject": "ENVO:00000012"}, "logical_row": 4639}], "data/raw/ontology_terms.tsv": [{"data": {"definition": "A geographical feature associated with water.", "deprecated": "", "directly_referenced": "TRUE", "label": "hydrographic feature", "label_only": "FALSE", "ontology": "ENVO", "synonyms": "fluvial feature", "term_id": "ENVO:00000012"}, "logical_row": 6604}], "data/raw/prego_habitat_taxa.tsv": [{"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.81611", "rank": "1", "taxon_id": "NCBITaxon:207954", "taxon_label": "Neptuniibacter caesariensis"}, "logical_row": 3138}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.79016", "rank": "2", "taxon_id": "NCBITaxon:313594", "taxon_label": "Polaribacter irgensii 23-P"}, "logical_row": 3139}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.7893", "rank": "3", "taxon_id": "NCBITaxon:314277", "taxon_label": "Marinomonas sp. MED121"}, "logical_row": 3140}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.78824", "rank": "4", "taxon_id": "NCBITaxon:357804", "taxon_label": "Psychromonas ingrahamii 37"}, "logical_row": 3141}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.78491", "rank": "5", "taxon_id": "NCBITaxon:290400", "taxon_label": "Jannaschia sp. CCS1"}, "logical_row": 3142}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.77955", "rank": "6", "taxon_id": "NCBITaxon:398580", "taxon_label": "Dinoroseobacter shibae DFL 12 = DSM 16493"}, "logical_row": 3143}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.77609", "rank": "7", "taxon_id": "NCBITaxon:313598", "taxon_label": "Polaribacter sp. MED152"}, "logical_row": 3144}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.76834", "rank": "8", "taxon_id": "NCBITaxon:318586", "taxon_label": "Paracoccus denitrificans PD1222"}, "logical_row": 3145}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.76422", "rank": "9", "taxon_id": "NCBITaxon:400668", "taxon_label": "Marinomonas sp. MWYL1"}, "logical_row": 3146}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.76409", "rank": "10", "taxon_id": "NCBITaxon:349521", "taxon_label": "Hahella chejuensis KCTC 2396"}, "logical_row": 3147}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.76091", "rank": "11", "taxon_id": "NCBITaxon:391626", "taxon_label": "Octadecabacter antarcticus 307"}, "logical_row": 3148}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.76001", "rank": "12", "taxon_id": "NCBITaxon:439495", "taxon_label": "Pseudovibrio sp. JE062"}, "logical_row": 3149}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.75992", "rank": "13", "taxon_id": "NCBITaxon:314271", "taxon_label": "Maritimibacter alkaliphilus HTCC2654"}, "logical_row": 3150}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.75992", "rank": "14", "taxon_id": "NCBITaxon:371731", "taxon_label": "Rhodobacter ferrooxidans"}, "logical_row": 3151}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.75859", "rank": "15", "taxon_id": "NCBITaxon:313603", "taxon_label": "Maribacter sp. HTCC2170"}, "logical_row": 3152}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.75772", "rank": "16", "taxon_id": "NCBITaxon:388399", "taxon_label": "Sagittula stellata E-37"}, "logical_row": 3153}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.74946", "rank": "17", "taxon_id": "NCBITaxon:342610", "taxon_label": ""}, "logical_row": 3154}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.74897", "rank": "18", "taxon_id": "NCBITaxon:391624", "taxon_label": "Sulfitobacter indolifex HEL-45"}, "logical_row": 3155}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.7477", "rank": "19", "taxon_id": "NCBITaxon:167879", "taxon_label": "Colwellia psychrerythraea 34H"}, "logical_row": 3156}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.74749", "rank": "20", "taxon_id": "NCBITaxon:314256", "taxon_label": "Oceanicola granulosus HTCC2516"}, "logical_row": 3157}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.74613", "rank": "21", "taxon_id": "NCBITaxon:207949", "taxon_label": "Bermanella marisrubri"}, "logical_row": 3158}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.74491", "rank": "22", "taxon_id": "NCBITaxon:290398", "taxon_label": "Chromohalobacter israelensis DSM 3043"}, "logical_row": 3159}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.74352", "rank": "23", "taxon_id": "NCBITaxon:376686", "taxon_label": "Flavobacterium johnsoniae UW101"}, "logical_row": 3160}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.74312", "rank": "24", "taxon_id": "NCBITaxon:411684", "taxon_label": "Hoeflea phototrophica DFL-43"}, "logical_row": 3161}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.7424", "rank": "25", "taxon_id": "NCBITaxon:396588", "taxon_label": "Thioalkalivibrio sulfidiphilus HL-EbGr7"}, "logical_row": 3162}], "data/raw/prego_habitats.tsv": [{"data": {"biolink_category": "biolink:OntologyClass", "channels": "environmental_samples", "direct_assertion_count": "1427", "max_prego_score": "1.81611", "ontology": "ENVO", "prego_id": "ENVO:00000012", "prego_synonyms": "OVERFALLS&#124;OVERFALLSs&#124;eddy&#124;fluvial feature&#124;fluvial features&#124;hydrographic feature&#124;hydrographic features&#124;marine feature&#124;marine features&#124;overfallses&#124;overfallsic&#124;tidal ripp&#124;tidal ripps", "taxon_count": "1427"}, "logical_row": 60}]} |
| CODE | src/habitatmech/seed.py; Executed complete-document reconstruction; all40 matched captured records | supports | {"reviewed_sources": 0, "routes": [{"actual": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:00000012", "mapping_predicate": null, "reviewed": false, "route": "prego_self_grounded"}, "automatic": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:00000012", "mapping_predicate": null, "reviewed": false, "route": "prego_self_grounded"}, "minted": "habitatmech:PREGO.79534379c9", "source": "PREGO", "source_id": "ENVO:00000012"}], "source_concepts": 1} |
| ONT | https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl; Official OWL fetched11-Oct; identity, deprecated/replacement metadata, typed synonyms and direct axioms; no snapshot refresh | supports | {"ENVO:00000000": {"definitions": ["An astrononmical body part which delimited by physical discontinuities with its surroundings."], "deprecated": [], "equivalents": [], "labels": ["geographic feature"], "parents": ["http://purl.obolibrary.org/obo/ENVO_01000813"], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": ["macroscopic spatial feature"], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:00000012": {"definitions": ["A geographical feature associated with water."], "deprecated": [], "equivalents": [], "labels": ["hydrographic feature"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00000000", "http://purl.obolibrary.org/obo/RO_0002577", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/BFO_0000050"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_00000063"]}, {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002507"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_00000063"]}], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": ["fluvial feature"]}}} |
| PARENT | data/habitats/other/geographic_feature.yaml; Ancestor context is not full-record review coverage of ancestors | supports | {"ENVO:00000000": {"definition": "An astrononmical body part which delimited by physical discontinuities with its surroundings.", "grounding_status": "EXACT", "label": "geographic feature", "parent_habitats": ["ENVO:01000813"]}} |
| TAX0 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=100%2C100038%2C1001240%2C1003%2C1004304%2C1005%2C1007511%2C1008%2C1012%2C1017018%2C102%2C102232%2C1026%2C102822%2C103%2C103690%2C103810%2C104176%2C1042%2C104245%2C104336%2C1045010%2C1045317%2C1046938%2C1046985%2C1046987%2C1046989%2C1046996%2C1047003%2C1047010%2C1052802%2C1052803%2C1052804%2C1052805%2C1052806%2C1052810%2C1052811%2C1052812%2C1052813%2C1052814%2C1052828%2C1052829%2C1052830%2C1052831%2C1052832%2C1052833%2C1052838%2C1052839%2C1052841%2C1054498%2C1056495%2C1056810%2C105850%2C1061%2C106111%2C1063%2C106592%2C1069080%2C1069082%2C1074%2C107400%2C1076%2C107633%2C107635%2C107636%2C107637%2C1076412%2C1077942%2C1077976%2C1079%2C1081640%2C1082345%2C108619%2C1089433%2C1094%2C1096091%2C1100720%2C1100721%2C1104324%2C1104571%2C1104575%2C1104576%2C1104577%2C1104580%2C1104607%2C1104609%2C1104610%2C1104614%2C1104615%2C1111728%2C1112%2C1112272%2C111780%2C1120989%2C1121004%2C1121032%2C1121104%2C1121124%2C1121256%2C1121259%2C1121270%2C1121279%2C1121291%2C1121302%2C1121319%2C1121383%2C1121406%2C1121412%2C1121428%2C1121435%2C1121441%2C1121448%2C1121462%2C1121466%2C1121861%2C1121881%2C1121895%2C1121898%2C1121902%2C1121903%2C1121948%2C1122133%2C1122221%2C1122222%2C1122603%2C1122607%2C1122612%2C1122970%2C1122999%2C1123031%2C1123057%2C1123072%2C1123253%2C1123368%2C1123369%2C1123372%2C1123374%2C1123375%2C114707%2C120213%2C127458%2C1302614%2C148219%2C1495%2C1543%2C155042%2C167879%2C169679%2C1869227%2C1876&amp;retmode=xml; NCBI TaxId, ScientificName, Rank, AkaTaxIds and OtherNames | supports | The two chunks resolve all234 requested cohort IDs. This target=[{"current_id": "207954", "current_name": "Neptuniibacter caesariensis", "frozen_label": "Neptuniibacter caesariensis", "id": "207954", "rank": "species"}, {"current_id": "313594", "current_name": "Polaribacter irgensii 23-P", "frozen_label": "Polaribacter irgensii 23-P", "id": "313594", "rank": "strain"}, {"current_id": "314277", "current_name": "Marinomonas sp. MED121", "frozen_label": "Marinomonas sp. MED121", "id": "314277", "rank": "species"}, {"current_id": "357804", "current_name": "Psychromonas ingrahamii 37", "frozen_label": "Psychromonas ingrahamii 37", "id": "357804", "rank": "strain"}, {"current_id": "290400", "current_name": "Jannaschia sp. CCS1", "frozen_label": "Jannaschia sp. CCS1", "id": "290400", "rank": "species"}, {"current_id": "398580", "current_name": "Dinoroseobacter shibae DFL 12 = DSM 16493", "frozen_label": "Dinoroseobacter shibae DFL 12 = DSM 16493", "id": "398580", "rank": "strain"}, {"current_id": "313598", "current_name": "Polaribacter sp. MED152", "frozen_label": "Polaribacter sp. MED152", "id": "313598", "rank": "species"}, {"current_id": "318586", "current_name": "Paracoccus denitrificans PD1222", "frozen_label": "Paracoccus denitrificans PD1222", "id": "318586", "rank": "strain"}, {"current_id": "400668", "current_name": "Marinomonas sp. MWYL1", "frozen_label": "Marinomonas sp. MWYL1", "id": "400668", "rank": "species"}, {"current_id": "349521", "current_name": "Hahella chejuensis KCTC 2396", "frozen_label": "Hahella chejuensis KCTC 2396", "id": "349521", "rank": "strain"}, {"current_id": "391626", "current_name": "Octadecabacter antarcticus 307", "frozen_label": "Octadecabacter antarcticus 307", "id": "391626", "rank": "strain"}, {"current_id": "439495", "current_name": "Pseudovibrio sp. JE062", "frozen_label": "Pseudovibrio sp. JE062", "id": "439495", "rank": "species"}, {"current_id": "314271", "current_name": "Maritimibacter alkaliphilus HTCC2654", "frozen_label": "Maritimibacter alkaliphilus HTCC2654", "id": "314271", "rank": "strain"}, {"current_id": "371731", "current_name": "Rhodobacter ferrooxidans", "frozen_label": "Rhodobacter ferrooxidans", "id": "371731", "rank": "species"}, {"current_id": "313603", "current_name": "Maribacter sp. HTCC2170", "frozen_label": "Maribacter sp. HTCC2170", "id": "313603", "rank": "species"}, {"current_id": "388399", "current_name": "Sagittula stellata E-37", "frozen_label": "Sagittula stellata E-37", "id": "388399", "rank": "strain"}, {"current_id": "3042615", "current_name": "Paraglaciecola sp. T6c", "frozen_label": null, "id": "342610", "rank": "species"}, {"current_id": "391624", "current_name": "Sulfitobacter indolifex HEL-45", "frozen_label": "Sulfitobacter indolifex HEL-45", "id": "391624", "rank": "strain"}, {"current_id": "167879", "current_name": "Colwellia psychrerythraea 34H", "frozen_label": "Colwellia psychrerythraea 34H", "id": "167879", "rank": "strain"}, {"current_id": "314256", "current_name": "Oceanicola granulosus HTCC2516", "frozen_label": "Oceanicola granulosus HTCC2516", "id": "314256", "rank": "strain"}, {"current_id": "207949", "current_name": "Bermanella marisrubri", "frozen_label": "Bermanella marisrubri", "id": "207949", "rank": "species"}, {"current_id": "290398", "current_name": "Chromohalobacter israelensis DSM 3043", "frozen_label": "Chromohalobacter israelensis DSM 3043", "id": "290398", "rank": "strain"}, {"current_id": "376686", "current_name": "Flavobacterium johnsoniae UW101", "frozen_label": "Flavobacterium johnsoniae UW101", "id": "376686", "rank": "strain"}, {"current_id": "411684", "current_name": "Hoeflea phototrophica DFL-43", "frozen_label": "Hoeflea phototrophica DFL-43", "id": "411684", "rank": "strain"}, {"current_id": "396588", "current_name": "Thioalkalivibrio sulfidiphilus HL-EbGr7", "frozen_label": "Thioalkalivibrio sulfidiphilus HL-EbGr7", "id": "396588", "rank": "strain"}]. Frozen labels may be historical aliases; resolution does not establish occurrence. |
| TAX1 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1890675%2C1919273%2C1934978%2C1934979%2C1934980%2C1934981%2C1934982%2C1934983%2C1934984%2C1934985%2C1934986%2C1934987%2C1934988%2C1934989%2C1934990%2C1934991%2C1934992%2C1934993%2C1934994%2C1934995%2C1934996%2C1934997%2C1934998%2C1934999%2C1935000%2C1935001%2C207949%2C207954%2C231024%2C232537%2C237491%2C237497%2C238209%2C239%2C2527775%2C253%2C256%2C290398%2C290400%2C2930037%2C294%2C303%2C306%2C31234%2C313594%2C313598%2C313603%2C314256%2C314271%2C314277%2C317619%2C318586%2C33953%2C34003%2C34012%2C34073%2C34085%2C342610%2C349521%2C357804%2C358%2C36987%2C371731%2C376686%2C381845%2C388399%2C391624%2C391626%2C396588%2C398580%2C39946%2C400668%2C40324%2C404941%2C409%2C411684%2C41211%2C427%2C439495%2C562%2C582402%2C65%2C665118%2C685&amp;retmode=xml; NCBI TaxId, ScientificName, Rank, AkaTaxIds and OtherNames | supports | The two chunks resolve all234 requested cohort IDs. This target=[{"current_id": "207954", "current_name": "Neptuniibacter caesariensis", "frozen_label": "Neptuniibacter caesariensis", "id": "207954", "rank": "species"}, {"current_id": "313594", "current_name": "Polaribacter irgensii 23-P", "frozen_label": "Polaribacter irgensii 23-P", "id": "313594", "rank": "strain"}, {"current_id": "314277", "current_name": "Marinomonas sp. MED121", "frozen_label": "Marinomonas sp. MED121", "id": "314277", "rank": "species"}, {"current_id": "357804", "current_name": "Psychromonas ingrahamii 37", "frozen_label": "Psychromonas ingrahamii 37", "id": "357804", "rank": "strain"}, {"current_id": "290400", "current_name": "Jannaschia sp. CCS1", "frozen_label": "Jannaschia sp. CCS1", "id": "290400", "rank": "species"}, {"current_id": "398580", "current_name": "Dinoroseobacter shibae DFL 12 = DSM 16493", "frozen_label": "Dinoroseobacter shibae DFL 12 = DSM 16493", "id": "398580", "rank": "strain"}, {"current_id": "313598", "current_name": "Polaribacter sp. MED152", "frozen_label": "Polaribacter sp. MED152", "id": "313598", "rank": "species"}, {"current_id": "318586", "current_name": "Paracoccus denitrificans PD1222", "frozen_label": "Paracoccus denitrificans PD1222", "id": "318586", "rank": "strain"}, {"current_id": "400668", "current_name": "Marinomonas sp. MWYL1", "frozen_label": "Marinomonas sp. MWYL1", "id": "400668", "rank": "species"}, {"current_id": "349521", "current_name": "Hahella chejuensis KCTC 2396", "frozen_label": "Hahella chejuensis KCTC 2396", "id": "349521", "rank": "strain"}, {"current_id": "391626", "current_name": "Octadecabacter antarcticus 307", "frozen_label": "Octadecabacter antarcticus 307", "id": "391626", "rank": "strain"}, {"current_id": "439495", "current_name": "Pseudovibrio sp. JE062", "frozen_label": "Pseudovibrio sp. JE062", "id": "439495", "rank": "species"}, {"current_id": "314271", "current_name": "Maritimibacter alkaliphilus HTCC2654", "frozen_label": "Maritimibacter alkaliphilus HTCC2654", "id": "314271", "rank": "strain"}, {"current_id": "371731", "current_name": "Rhodobacter ferrooxidans", "frozen_label": "Rhodobacter ferrooxidans", "id": "371731", "rank": "species"}, {"current_id": "313603", "current_name": "Maribacter sp. HTCC2170", "frozen_label": "Maribacter sp. HTCC2170", "id": "313603", "rank": "species"}, {"current_id": "388399", "current_name": "Sagittula stellata E-37", "frozen_label": "Sagittula stellata E-37", "id": "388399", "rank": "strain"}, {"current_id": "3042615", "current_name": "Paraglaciecola sp. T6c", "frozen_label": null, "id": "342610", "rank": "species"}, {"current_id": "391624", "current_name": "Sulfitobacter indolifex HEL-45", "frozen_label": "Sulfitobacter indolifex HEL-45", "id": "391624", "rank": "strain"}, {"current_id": "167879", "current_name": "Colwellia psychrerythraea 34H", "frozen_label": "Colwellia psychrerythraea 34H", "id": "167879", "rank": "strain"}, {"current_id": "314256", "current_name": "Oceanicola granulosus HTCC2516", "frozen_label": "Oceanicola granulosus HTCC2516", "id": "314256", "rank": "strain"}, {"current_id": "207949", "current_name": "Bermanella marisrubri", "frozen_label": "Bermanella marisrubri", "id": "207949", "rank": "species"}, {"current_id": "290398", "current_name": "Chromohalobacter israelensis DSM 3043", "frozen_label": "Chromohalobacter israelensis DSM 3043", "id": "290398", "rank": "strain"}, {"current_id": "376686", "current_name": "Flavobacterium johnsoniae UW101", "frozen_label": "Flavobacterium johnsoniae UW101", "id": "376686", "rank": "strain"}, {"current_id": "411684", "current_name": "Hoeflea phototrophica DFL-43", "frozen_label": "Hoeflea phototrophica DFL-43", "id": "411684", "rank": "strain"}, {"current_id": "396588", "current_name": "Thioalkalivibrio sulfidiphilus HL-EbGr7", "frozen_label": "Thioalkalivibrio sulfidiphilus HL-EbGr7", "id": "396588", "rank": "strain"}]. Frozen labels may be historical aliases; resolution does not establish occurrence. |
| SEARCH | curation; history; research; reports; reviews; data/raw; data/habitats; conf; Bounded ignored-inclusive searches; no global absence claim | supports | Identifier, label, slug and exact source-path searches included ignored/hidden files in these roots; coverage used Path.rglob. No earlier structured observation of this target found. Legacy reports were indexed, not uniformly rereviewed. Original membership search={"configured_root": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe", "root_exists": true, "exact_paths": [{"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_nodes.tsv", "exists": false, "expected_sha256": "c13c21bdd04619c75ce16e63b05e51577b0cefec5b61765d383313f654ab3fae"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_edges.tsv", "exists": false, "expected_sha256": "54982c25de9d2c820eeebc1452aeac0b034595921d04d55b810bf1d2b1e127e0"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/nodes.tsv", "exists": false, "expected_sha256": "a2a2f9acae230636dd866347d173a32c9f025c04a377060087a4be65781628f3"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/edges.tsv", "exists": false, "expected_sha256": "ab6208bff4854db7c1a736d53d0aa04269a682ab15a1ce6f37c6d731000281d7"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/nodes.tsv", "exists": false, "expected_sha256": "020de3afc71495571ddb05000c83a58d009272f53735b5f7c9326c1293e0415c"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/edges.tsv", "exists": false, "expected_sha256": "8863ee3197a36915865fa4833df39d10c3f8f69b64bafbb746b9cd731308a0aa"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/nodes.tsv", "exists": false, "expected_sha256": "cc5941cd677831e8e207da018dca763cd009bb1f9310b21cb4d45892316e006d"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/edges.tsv", "exists": false, "expected_sha256": "fd333634eaaa3cfe57a35cdca2f4c5b8cf0662851c1df58914d3e999d62a650e"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/environments.csv", "exists": false, "expected_sha256": "99299fe635159712f95568783ad3b484230fb31781262f1f6f8bd84db4bc3048"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/mappings/isolation_source_to_ontology.tsv", "exists": false, "expected_sha256": "2dea3d1bb20c72a04b6f64a67e2bb2bdc4f3649b809c5935390239be2791ef1f"}], "traversal": [{"command": ["rg", "--files", "--no-ignore", "--hidden", "data"], "exit_code": 0, "matches": [], "stderr": ""}, {"command": ["rg", "--files", "--no-ignore", "--hidden", "build"], "exit_code": 0, "matches": [], "stderr": ""}, {"command": ["rg", "--files", "--no-ignore", "--hidden", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data"], "exit_code": 0, "matches": [], "stderr": ""}]} |
| ISSUES | https://github.com/CultureBotAI/HabitatMech/issues; GitHub CLI census and relevant issue bodies | supports | Read-only all-state959-issue title/body census checked for overlaps, including shared1249 and1398 and prior hot-spring correction1238. Prior issue closure is not primary scientific evidence. Comments were not exhaustively crawled. |

## Limits And Additional Notes

- Completed scientific assessment is not a clean-corpus verdict or proof of every original occurrence.
- Only first3 exact BioSample/Organism descriptions per sheet were individually interpreted; all other matches and study joins were indexed, not individually assessed.
- The later GOLD export/classification are not reconstructed August membership; original assertion inputs were not fully recovered. No ontology, taxonomy or source snapshot was refreshed.
- Same-agent review, not independent approval. Native status and curation/history inputs are unchanged.
- SSSOM/KGX conformance with current kg-microbe modeling was not audited; shared mapping-endpoint issue1398 remains unresolved.
- Whole-corpus review remains incomplete; ancestor context and indexing add no record coverage. Product-label gate retains2057 SKIPPED_NO_ADAPTER targets and5 accepted exceptions; it does not certify scientific identity.
- New immutable observation only; no source curation, native status promotion or GitHub mutation.
- No earlier structured target observation found; legacy reports remain historical and are not silently retired.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T015316Z-hydrographic_feature
kind: record
repository: CultureBotAI/HabitatMech
title: 'Scientific record review: hydrographic_feature'
started_at: '2026-10-12T01:35:44.699592Z'
finished_at: '2026-10-12T01:53:16.410488Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Agent has participated in repository curation; this is not independent
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: The PREGO record names the broad ENVO geographic feature associated with
  water, not a particular river or water material. Its geographic-feature genus is
  supported. Official fluvial feature is related rather than exact; several PREGO
  lexical variants are malformed. Scores around 1.8 rank associations from a 1427-taxon
  pool and are not occurrence probabilities.
source:
  git_revision: 51e0d6e3e3429b8cf601667b9097daba848f5326
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 4544b5d2c11fbbb3a46cd8a65f7e664363df78c1000c590aab533219f9eec59b
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: d429c8bb74f521df9a77a90b216a44fc6959ee28efb1fa17a93582536caa8bce
    role: context
  - path: CLAUDE.md
    sha256: 98d95f910ff5160bc5b2ff572766785519dacdba487700bebaa6dbf96d071fd9
    role: context
  - path: conf/id_label_targets.yaml
    sha256: e100d84aabccaeb00c1a60246142b3cafcec009dbfba58f5cc319c35adddb633
    role: context
  - path: conf/record_review.yaml
    sha256: c2f5d0eb4c5744f5fe354c92184ddab144dc2688dba952b032b4f3d597bc08d6
    role: context
  - path: conf/sources.yaml
    sha256: a8e069f9278068b57fa234f43e03c8d893f857827b83fd10cfa92d6815aed642
    role: context
  - path: curation/decisions.tsv
    sha256: 7cbec6d310b1aac248defdbe657e68c0cc1e848981230d2279e63f474c6f4c96
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 2d41fc93db4939122b3909f2a412b84b679703948b10d9f02e12021442f71407
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 08f2092516f33ec1d38c0e7a8d78c5e997445d649ba167caaf4acc05e80d73e5
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: 3f2ce04805defe5ff65dc20988cc72bc94d4636b3140eb1311017866bdc0ea0a
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: b59b9e800a918135e3915145d4d8098bb48dcea36a312b3004c594a57d221ae9
    role: context
  - path: data/habitats/aquatic/hydrographic_feature.yaml
    sha256: 62216f89c234b9c46e9e4e3cf3afde0fce06ed5b742ea62aef1003be9e43108c
    role: target
  - path: data/habitats/other/geographic_feature.yaml
    sha256: 9466c0d6a5445ce3e809e2993f76b50e8fa7c91d12a01103ac8bae349475c274
    role: context
  - path: data/raw/GOLD_MANIFEST.yaml
    sha256: 99ec487ae02d512cfb75440685f927abe907effe52cb755feb095631e8841489
    role: context
  - path: data/raw/MANIFEST.yaml
    sha256: 4657672d429be35e551ceef4a1204ab0a8120558ce63e2a2b74188eee94b8480
    role: context
  - path: data/raw/bacdive_isolation_sources.tsv
    sha256: fb1645dd899a43130be9cf38b0e8b27ffbaa0175306917bff20e20ee225875fc
    role: context
  - path: data/raw/bacdive_source_taxa.tsv
    sha256: 08471c12f887882e2a6af8f078166b1f59ed7e2b24eb7edbe43a7fc77dfbad44
    role: context
  - path: data/raw/environment_parameters.tsv
    sha256: a75d0f565d8ee2498188ff98b17d0ab325ae4f782601bf4414eff6e86c13e0f9
    role: context
  - path: data/raw/gold_ecosystem_paths.tsv
    sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
    role: context
  - path: data/raw/gold_path_biosamples.tsv
    sha256: 97cd7c8d0e731d07a85db6986dbcf9e49096a3c7988bd90a855599f492fe619e
    role: context
  - path: data/raw/gold_path_triads.tsv
    sha256: b1717bd8fc4fdcd6a1a132f4eb32df3638b01ddf7d78f9a5797f110ee2b1e8d6
    role: context
  - path: data/raw/gold_studies.tsv
    sha256: fa7aaa46f288d10c453bb723e6cf486cde646a003559414b5523cc3883a84c8c
    role: context
  - path: data/raw/isolation_source_groundings.tsv
    sha256: ab6a997359aab961c40928f9b13e06adb6dc43124fa3de821819570dd87f43b8
    role: context
  - path: data/raw/madin_habitat_taxa.tsv
    sha256: d30854cfcffca0405914d04071ac47053938d354d5df250125843131b7c91fd7
    role: context
  - path: data/raw/madin_habitats.tsv
    sha256: 2ae1756f40242600365c49bfbdada4bce5fc8b86630426bb34892f055e5a5c93
    role: context
  - path: data/raw/ontology_subclass_edges.tsv
    sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
    role: context
  - path: data/raw/ontology_terms.tsv
    sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
    role: context
  - path: data/raw/prego_habitat_taxa.tsv
    sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
    role: context
  - path: data/raw/prego_habitats.tsv
    sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
    role: context
  - path: docs/CURATION.md
    sha256: 36df8306394c06c352b73e0bf7b47a2858784cedac7389a24d0b78f593ece646
    role: context
  - path: docs/HARMONIZATION.md
    sha256: ee39d3cd29115ee14f5e7386169c76c47d471ebdc2502c008c49d30fb44918f1
    role: context
  - path: docs/RESEARCH.md
    sha256: 82c5471890d310bf8fd33141d5596f847bfc1eb6091c2db6f485388435e067af
    role: context
  - path: docs/record-review-profile.md
    sha256: f7aa39ee762d94f1902d9f08f328cb897bc543e4e226057eb4770d24bfcc6eb5
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260921T120140Z-algal_bloom.md
    sha256: 7a193dfbdb28961f8d24165b4ed0792ce1d0e25688f7e5a55078e2a29bfb8b86
    role: context
  - path: reports/yaml_record_review/20260921T185521Z-bar.md
    sha256: 0142f8a7ebfadb28c1e34f5e95a8a1bdde318bd3d458c736de72bc19f4240649
    role: context
  - path: reports/yaml_record_review/20260927T110611Z-cyanobacterial_bloom.md
    sha256: 7935dd51e683c05a173b82247b7864cead5d8a2876e7f23e52e81079f46b1090
    role: context
  - path: reports/yaml_record_review/20261003T121205Z-hydrographic_feature.md
    sha256: d9dc7bf7608b28e79704d7d94d6dbbd883868713bcdefa86dab4c8d83bc91592
    role: context
  - path: reports/yaml_record_review/20261003T143846Z-inlet.md
    sha256: d4a245a43dae88035594855de3011332a80cd4c3dafd9b5cf76c705c4bf081ea
    role: context
  - path: reports/yaml_record_review/20261006T000757Z-sediment__f9571146.md
    sha256: 6942b8d878c25d56aeb3b68e682fea999c3369fa246e0c548e503c441afd9634
    role: context
  - path: reports/yaml_record_review/20261006T194744Z-undersea_feature.md
    sha256: bb2a71f7d7ffc603998ecb51731a74b581430b5fab037a2f8ae5c5692c7e28f7
    role: context
  - path: reports/yaml_record_review/20261006T203513Z-water_body.md
    sha256: e1782a9f39419e88d385ea0454128bb20f2ccc51413a107b98b94c35332da6f0
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/extract_gold_biosamples.py
    sha256: b6a2773c86fe718e1ca0b1d7b32709f0eee491ac813655e310aa0817c0fec31b
    role: context
  - path: scripts/extract_source_inventory.py
    sha256: 4bf5391d25ff48a2d81eb3821af6582de063fd0391440973d309dfd93016490c
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
    role: context
  - path: src/habitatmech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/habitatmech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/habitatmech/seed.py
    sha256: 4adf105e23d75c3563a516a0c160623d1065df7fcb2f31b7a0a0a8303d0401be
    role: context
targets:
- target_id: ENVO:00000012
  path: data/habitats/aquatic/hydrographic_feature.yaml
  label: hydrographic feature
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Source-specific identity and lifecycle decisions
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Authored definitions and genus
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Guarded source context-parent exclusions
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Pinned ontology labels, definitions and synonyms
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_subclass_edges.tsv
    role: Pinned ontology hierarchy
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Harmonization and generated record construction
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitats.tsv
    role: Frozen PREGO source inventory
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitat_taxa.tsv
    role: Frozen PREGO source inventory
scope:
  description: Entire exact generated record, all contributors and individual asserted
    mechanism edges, with bounded source-context assessment.
  selection: 'Next forty records without a completed individual scientific review
    in stable repository-relative path order: estuary variants through hydrothermal
    fluid. Full individual observations, not a category-wide pass. Starting observation
    coverage608/3208 is not clean current-input coverage.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - ENVO:00000012
  exclusions:
  - target: Other3207 current records
    reason: Context reads are not their full scientific review.
checks:
- check_id: C0
  name: Native gate on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00000012
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=51e0d6e3e3429b8cf601667b9097daba848f5326
    just validate data/habitats/aquatic/hydrographic_feature.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success from 2026-10-12T01:38:40.243463Z to 2026-10-12T01:38:42.914558Z.
    Native scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C1
  name: Native gate on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00000012
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=51e0d6e3e3429b8cf601667b9097daba848f5326
    just validate-strict data/habitats/aquatic/estuary__5f780975.yaml data/habitats/aquatic/estuary__bae88a25.yaml
    data/habitats/aquatic/estuary_microbial_mat.yaml data/habitats/aquatic/estuary_sediment.yaml
    data/habitats/aquatic/eutrophic_water.yaml data/habitats/aquatic/fen__a3c5fc09.yaml
    data/habitats/aquatic/filtered_water.yaml data/habitats/aquatic/fjord.yaml data/habitats/aquatic/floodplain__7ad4b08f.yaml
    data/habitats/aquatic/floodplain__98d09203.yaml data/habitats/aquatic/floodplain_lake.yaml
    data/habitats/aquatic/formation_fluid.yaml data/habitats/aquatic/fossil.yaml data/habitats/aquatic/fracking_water__af948aea.yaml
    data/habitats/aquatic/fresh_water.yaml data/habitats/aquatic/freshwater.yaml data/habitats/aquatic/freshwater_biome.yaml
    data/habitats/aquatic/freshwater_ice.yaml data/habitats/aquatic/freshwater_lake.yaml
    data/habitats/aquatic/freshwater_lake_biome.yaml data/habitats/aquatic/freshwater_river.yaml
    data/habitats/aquatic/geothermal_pool_hot_lake.yaml data/habitats/aquatic/glacial_lake.yaml
    data/habitats/aquatic/glacier__0eab88a6.yaml data/habitats/aquatic/glacier__efa45690.yaml
    data/habitats/aquatic/glacier_meltwater.yaml data/habitats/aquatic/glacier_stream.yaml
    data/habitats/aquatic/groundwater.yaml data/habitats/aquatic/groundwater__25377149.yaml
    data/habitats/aquatic/groundwater__585f08d9.yaml data/habitats/aquatic/gulf.yaml
    data/habitats/aquatic/hadalpelagic.yaml data/habitats/aquatic/hadopelagic_zone_ocean_trenches.yaml
    data/habitats/aquatic/harbor.yaml data/habitats/aquatic/harbor__5962cec6.yaml
    data/habitats/aquatic/hot_42_90c.yaml data/habitats/aquatic/hot_spring.yaml data/habitats/aquatic/hydrocarbon__a75cc82e.yaml
    data/habitats/aquatic/hydrographic_feature.yaml data/habitats/aquatic/hydrothermal_fluid.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success from 2026-10-12T01:38:45.606215Z to 2026-10-12T01:38:54.204186Z.
    Native scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C2
  name: Native gate on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00000012
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=51e0d6e3e3429b8cf601667b9097daba848f5326
    just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success from 2026-10-12T01:38:54.205107Z to 2026-10-12T01:39:22.495898Z.
    Native scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C3
  name: Native gate on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00000012
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=51e0d6e3e3429b8cf601667b9097daba848f5326
    just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success from 2026-10-12T01:39:22.510128Z to 2026-10-12T01:40:40.416231Z.
    Native scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C4
  name: Native gate on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00000012
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=51e0d6e3e3429b8cf601667b9097daba848f5326
    just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success from 2026-10-12T01:40:40.417502Z to 2026-10-12T01:40:49.459346Z.
    Native scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C5
  name: Native gate on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00000012
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=51e0d6e3e3429b8cf601667b9097daba848f5326
    just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success from 2026-10-12T01:40:49.460754Z to 2026-10-12T01:40:54.753371Z.
    Native scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C6
  name: Native gate on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00000012
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=51e0d6e3e3429b8cf601667b9097daba848f5326
    just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success from 2026-10-12T01:40:54.754493Z to 2026-10-12T01:41:21.741599Z.
    Native scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C7
  name: Native gate on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00000012
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=51e0d6e3e3429b8cf601667b9097daba848f5326
    just provenance-check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success from 2026-10-12T01:41:21.742805Z to 2026-10-12T01:41:22.498024Z.
    Native scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C8
  name: Native gate on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00000012
  command: gh run view 38191340510 --repo CultureBotAI/HabitatMech --log
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success from 2026-10-12T01:37:32.943507Z to 2026-10-12T01:37:35.068708Z.
    All three required merge-group workflows passed at the exact captured base; authoritative
    QC passed 856 tests with 3 skipped. Newly saved review bundles require their own
    integrity check. Exact-base CI receipt; these new review bundles were not part
    of that CI run.
  evidence_ids:
  - R
  - RULES
- check_id: REPRO
  name: Complete target reconstruction
  required: false
  status: passed
  target_ids:
  - ENVO:00000012
  command: .venv/bin/python /private/tmp/habitatmech-review-ba-evidence.py
  exit_code: 0
  summary: All40 complete documents matched; captured input hashes verified again
    before authoring.
  evidence_ids:
  - RAW
  - CODE
- check_id: ORIGINAL
  name: Original assertion membership
  required: false
  status: unavailable
  target_ids:
  - ENVO:00000012
  summary: Bounded ignored-inclusive searches did not recover the complete original
    assertion inputs. Later exports supply context only.
  evidence_ids:
  - SEARCH
- check_id: IMODULON
  name: Structured expression applicability
  required: false
  status: not_applicable
  target_ids:
  - ENVO:00000012
  summary: No organism/dataset-specific gene, regulator or expression-module assertion
    in this habitat record; database absence is not negative habitat evidence.
  evidence_ids:
  - R
  - RULES
evidence:
- evidence_id: R
  kind: record_content
  reference: data/habitats/aquatic/hydrographic_feature.yaml
  summary: The PREGO record names the broad ENVO geographic feature associated with
    water, not a particular river or water material. Its geographic-feature genus
    is supported. Official fluvial feature is related rather than exact; several PREGO
    lexical variants are malformed. Scores around 1.8 rank associations from a 1427-taxon
    pool and are not occurrence probabilities.
  accessed_at: '2026-10-12T01:53:16.410488Z'
  support: supports
  locator: Entire captured YAML read, including provenance, parameters, taxa, graphs
    and generated history
- evidence_id: RULES
  kind: record_content
  reference: docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; src/habitatmech/schema/habitatmech.yaml
  summary: Applied exact identity, strict-parent, MIxS-role, source unit/score and
    ITEM lifecycle contracts. STATE is a cellular value, not the process establishing
    it. Evidence is assessed at edge scope.
  accessed_at: '2026-10-12T01:53:16.410488Z'
  support: supports
- evidence_id: RAW
  kind: database
  reference: data/raw; curation/decisions.tsv; curation/term_requests.tsv; curation/gold_parent_exclusions.tsv
  summary: '{"data/raw/ontology_subclass_edges.tsv": [{"data": {"object": "ENVO:00000000",
    "predicate": "rdfs:subClassOf", "subject": "ENVO:00000012"}, "logical_row": 4639}],
    "data/raw/ontology_terms.tsv": [{"data": {"definition": "A geographical feature
    associated with water.", "deprecated": "", "directly_referenced": "TRUE", "label":
    "hydrographic feature", "label_only": "FALSE", "ontology": "ENVO", "synonyms":
    "fluvial feature", "term_id": "ENVO:00000012"}, "logical_row": 6604}], "data/raw/prego_habitat_taxa.tsv":
    [{"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.81611", "rank": "1", "taxon_id":
    "NCBITaxon:207954", "taxon_label": "Neptuniibacter caesariensis"}, "logical_row":
    3138}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.79016", "rank": "2", "taxon_id":
    "NCBITaxon:313594", "taxon_label": "Polaribacter irgensii 23-P"}, "logical_row":
    3139}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.7893", "rank": "3", "taxon_id":
    "NCBITaxon:314277", "taxon_label": "Marinomonas sp. MED121"}, "logical_row": 3140},
    {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.78824", "rank": "4", "taxon_id":
    "NCBITaxon:357804", "taxon_label": "Psychromonas ingrahamii 37"}, "logical_row":
    3141}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.78491", "rank": "5", "taxon_id":
    "NCBITaxon:290400", "taxon_label": "Jannaschia sp. CCS1"}, "logical_row": 3142},
    {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.77955", "rank": "6", "taxon_id":
    "NCBITaxon:398580", "taxon_label": "Dinoroseobacter shibae DFL 12 = DSM 16493"},
    "logical_row": 3143}, {"data": {"channels": "environmental_samples", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.77609",
    "rank": "7", "taxon_id": "NCBITaxon:313598", "taxon_label": "Polaribacter sp.
    MED152"}, "logical_row": 3144}, {"data": {"channels": "environmental_samples",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score":
    "1.76834", "rank": "8", "taxon_id": "NCBITaxon:318586", "taxon_label": "Paracoccus
    denitrificans PD1222"}, "logical_row": 3145}, {"data": {"channels": "environmental_samples",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score":
    "1.76422", "rank": "9", "taxon_id": "NCBITaxon:400668", "taxon_label": "Marinomonas
    sp. MWYL1"}, "logical_row": 3146}, {"data": {"channels": "environmental_samples",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score":
    "1.76409", "rank": "10", "taxon_id": "NCBITaxon:349521", "taxon_label": "Hahella
    chejuensis KCTC 2396"}, "logical_row": 3147}, {"data": {"channels": "environmental_samples",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score":
    "1.76091", "rank": "11", "taxon_id": "NCBITaxon:391626", "taxon_label": "Octadecabacter
    antarcticus 307"}, "logical_row": 3148}, {"data": {"channels": "environmental_samples",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score":
    "1.76001", "rank": "12", "taxon_id": "NCBITaxon:439495", "taxon_label": "Pseudovibrio
    sp. JE062"}, "logical_row": 3149}, {"data": {"channels": "environmental_samples",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score":
    "1.75992", "rank": "13", "taxon_id": "NCBITaxon:314271", "taxon_label": "Maritimibacter
    alkaliphilus HTCC2654"}, "logical_row": 3150}, {"data": {"channels": "environmental_samples",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score":
    "1.75992", "rank": "14", "taxon_id": "NCBITaxon:371731", "taxon_label": "Rhodobacter
    ferrooxidans"}, "logical_row": 3151}, {"data": {"channels": "environmental_samples",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score":
    "1.75859", "rank": "15", "taxon_id": "NCBITaxon:313603", "taxon_label": "Maribacter
    sp. HTCC2170"}, "logical_row": 3152}, {"data": {"channels": "environmental_samples",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score":
    "1.75772", "rank": "16", "taxon_id": "NCBITaxon:388399", "taxon_label": "Sagittula
    stellata E-37"}, "logical_row": 3153}, {"data": {"channels": "environmental_samples",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000012", "prego_score":
    "1.74946", "rank": "17", "taxon_id": "NCBITaxon:342610", "taxon_label": ""}, "logical_row":
    3154}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.74897", "rank": "18", "taxon_id":
    "NCBITaxon:391624", "taxon_label": "Sulfitobacter indolifex HEL-45"}, "logical_row":
    3155}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.7477", "rank": "19", "taxon_id":
    "NCBITaxon:167879", "taxon_label": "Colwellia psychrerythraea 34H"}, "logical_row":
    3156}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.74749", "rank": "20", "taxon_id":
    "NCBITaxon:314256", "taxon_label": "Oceanicola granulosus HTCC2516"}, "logical_row":
    3157}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.74613", "rank": "21", "taxon_id":
    "NCBITaxon:207949", "taxon_label": "Bermanella marisrubri"}, "logical_row": 3158},
    {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.74491", "rank": "22", "taxon_id":
    "NCBITaxon:290398", "taxon_label": "Chromohalobacter israelensis DSM 3043"}, "logical_row":
    3159}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.74352", "rank": "23", "taxon_id":
    "NCBITaxon:376686", "taxon_label": "Flavobacterium johnsoniae UW101"}, "logical_row":
    3160}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.74312", "rank": "24", "taxon_id":
    "NCBITaxon:411684", "taxon_label": "Hoeflea phototrophica DFL-43"}, "logical_row":
    3161}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "ENVO:00000012", "prego_score": "1.7424", "rank": "25", "taxon_id":
    "NCBITaxon:396588", "taxon_label": "Thioalkalivibrio sulfidiphilus HL-EbGr7"},
    "logical_row": 3162}], "data/raw/prego_habitats.tsv": [{"data": {"biolink_category":
    "biolink:OntologyClass", "channels": "environmental_samples", "direct_assertion_count":
    "1427", "max_prego_score": "1.81611", "ontology": "ENVO", "prego_id": "ENVO:00000012",
    "prego_synonyms": "OVERFALLS|OVERFALLSs|eddy|fluvial feature|fluvial features|hydrographic
    feature|hydrographic features|marine feature|marine features|overfallses|overfallsic|tidal
    ripp|tidal ripps", "taxon_count": "1427"}, "logical_row": 60}]}'
  accessed_at: '2026-10-12T01:53:16.410488Z'
  support: supports
  locator: Exact logical TSV rows; header is row1; unrelated neighbor matches excluded
- evidence_id: CODE
  kind: record_content
  reference: src/habitatmech/seed.py
  summary: '{"reviewed_sources": 0, "routes": [{"actual": {"category": null, "contributes_grounding":
    true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status":
    "EXACT", "identifier": "ENVO:00000012", "mapping_predicate": null, "reviewed":
    false, "route": "prego_self_grounded"}, "automatic": {"category": null, "contributes_grounding":
    true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status":
    "EXACT", "identifier": "ENVO:00000012", "mapping_predicate": null, "reviewed":
    false, "route": "prego_self_grounded"}, "minted": "habitatmech:PREGO.79534379c9",
    "source": "PREGO", "source_id": "ENVO:00000012"}], "source_concepts": 1}'
  accessed_at: '2026-10-12T01:53:16.410488Z'
  support: supports
  locator: Executed complete-document reconstruction; all40 matched captured records
- evidence_id: ONT
  kind: authority
  reference: https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl
  summary: '{"ENVO:00000000": {"definitions": ["An astrononmical body part which delimited
    by physical discontinuities with its surroundings."], "deprecated": [], "equivalents":
    [], "labels": ["geographic feature"], "parents": ["http://purl.obolibrary.org/obo/ENVO_01000813"],
    "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": ["macroscopic
    spatial feature"], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:00000012":
    {"definitions": ["A geographical feature associated with water."], "deprecated":
    [], "equivalents": [], "labels": ["hydrographic feature"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00000000",
    "http://purl.obolibrary.org/obo/RO_0002577", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty":
    ["http://purl.obolibrary.org/obo/BFO_0000050"], "http://www.w3.org/2002/07/owl#someValuesFrom":
    ["http://purl.obolibrary.org/obo/ENVO_00000063"]}, {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty":
    ["http://purl.obolibrary.org/obo/RO_0002507"], "http://www.w3.org/2002/07/owl#someValuesFrom":
    ["http://purl.obolibrary.org/obo/ENVO_00000063"]}], "replacements": [], "synonyms":
    {"hasBroadSynonym": [], "hasExactSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym":
    ["fluvial feature"]}}}'
  accessed_at: '2026-10-11T13:21:47.927208Z'
  support: supports
  locator: Official OWL fetched11-Oct; identity, deprecated/replacement metadata,
    typed synonyms and direct axioms; no snapshot refresh
  snapshot_sha256: a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c
- evidence_id: PARENT
  kind: record_content
  reference: data/habitats/other/geographic_feature.yaml
  summary: '{"ENVO:00000000": {"definition": "An astrononmical body part which delimited
    by physical discontinuities with its surroundings.", "grounding_status": "EXACT",
    "label": "geographic feature", "parent_habitats": ["ENVO:01000813"]}}'
  accessed_at: '2026-10-12T01:53:16.410488Z'
  support: supports
  locator: Ancestor context is not full-record review coverage of ancestors
- evidence_id: TAX0
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=100%2C100038%2C1001240%2C1003%2C1004304%2C1005%2C1007511%2C1008%2C1012%2C1017018%2C102%2C102232%2C1026%2C102822%2C103%2C103690%2C103810%2C104176%2C1042%2C104245%2C104336%2C1045010%2C1045317%2C1046938%2C1046985%2C1046987%2C1046989%2C1046996%2C1047003%2C1047010%2C1052802%2C1052803%2C1052804%2C1052805%2C1052806%2C1052810%2C1052811%2C1052812%2C1052813%2C1052814%2C1052828%2C1052829%2C1052830%2C1052831%2C1052832%2C1052833%2C1052838%2C1052839%2C1052841%2C1054498%2C1056495%2C1056810%2C105850%2C1061%2C106111%2C1063%2C106592%2C1069080%2C1069082%2C1074%2C107400%2C1076%2C107633%2C107635%2C107636%2C107637%2C1076412%2C1077942%2C1077976%2C1079%2C1081640%2C1082345%2C108619%2C1089433%2C1094%2C1096091%2C1100720%2C1100721%2C1104324%2C1104571%2C1104575%2C1104576%2C1104577%2C1104580%2C1104607%2C1104609%2C1104610%2C1104614%2C1104615%2C1111728%2C1112%2C1112272%2C111780%2C1120989%2C1121004%2C1121032%2C1121104%2C1121124%2C1121256%2C1121259%2C1121270%2C1121279%2C1121291%2C1121302%2C1121319%2C1121383%2C1121406%2C1121412%2C1121428%2C1121435%2C1121441%2C1121448%2C1121462%2C1121466%2C1121861%2C1121881%2C1121895%2C1121898%2C1121902%2C1121903%2C1121948%2C1122133%2C1122221%2C1122222%2C1122603%2C1122607%2C1122612%2C1122970%2C1122999%2C1123031%2C1123057%2C1123072%2C1123253%2C1123368%2C1123369%2C1123372%2C1123374%2C1123375%2C114707%2C120213%2C127458%2C1302614%2C148219%2C1495%2C1543%2C155042%2C167879%2C169679%2C1869227%2C1876&retmode=xml
  summary: 'The two chunks resolve all234 requested cohort IDs. This target=[{"current_id":
    "207954", "current_name": "Neptuniibacter caesariensis", "frozen_label": "Neptuniibacter
    caesariensis", "id": "207954", "rank": "species"}, {"current_id": "313594", "current_name":
    "Polaribacter irgensii 23-P", "frozen_label": "Polaribacter irgensii 23-P", "id":
    "313594", "rank": "strain"}, {"current_id": "314277", "current_name": "Marinomonas
    sp. MED121", "frozen_label": "Marinomonas sp. MED121", "id": "314277", "rank":
    "species"}, {"current_id": "357804", "current_name": "Psychromonas ingrahamii
    37", "frozen_label": "Psychromonas ingrahamii 37", "id": "357804", "rank": "strain"},
    {"current_id": "290400", "current_name": "Jannaschia sp. CCS1", "frozen_label":
    "Jannaschia sp. CCS1", "id": "290400", "rank": "species"}, {"current_id": "398580",
    "current_name": "Dinoroseobacter shibae DFL 12 = DSM 16493", "frozen_label": "Dinoroseobacter
    shibae DFL 12 = DSM 16493", "id": "398580", "rank": "strain"}, {"current_id":
    "313598", "current_name": "Polaribacter sp. MED152", "frozen_label": "Polaribacter
    sp. MED152", "id": "313598", "rank": "species"}, {"current_id": "318586", "current_name":
    "Paracoccus denitrificans PD1222", "frozen_label": "Paracoccus denitrificans PD1222",
    "id": "318586", "rank": "strain"}, {"current_id": "400668", "current_name": "Marinomonas
    sp. MWYL1", "frozen_label": "Marinomonas sp. MWYL1", "id": "400668", "rank": "species"},
    {"current_id": "349521", "current_name": "Hahella chejuensis KCTC 2396", "frozen_label":
    "Hahella chejuensis KCTC 2396", "id": "349521", "rank": "strain"}, {"current_id":
    "391626", "current_name": "Octadecabacter antarcticus 307", "frozen_label": "Octadecabacter
    antarcticus 307", "id": "391626", "rank": "strain"}, {"current_id": "439495",
    "current_name": "Pseudovibrio sp. JE062", "frozen_label": "Pseudovibrio sp. JE062",
    "id": "439495", "rank": "species"}, {"current_id": "314271", "current_name": "Maritimibacter
    alkaliphilus HTCC2654", "frozen_label": "Maritimibacter alkaliphilus HTCC2654",
    "id": "314271", "rank": "strain"}, {"current_id": "371731", "current_name": "Rhodobacter
    ferrooxidans", "frozen_label": "Rhodobacter ferrooxidans", "id": "371731", "rank":
    "species"}, {"current_id": "313603", "current_name": "Maribacter sp. HTCC2170",
    "frozen_label": "Maribacter sp. HTCC2170", "id": "313603", "rank": "species"},
    {"current_id": "388399", "current_name": "Sagittula stellata E-37", "frozen_label":
    "Sagittula stellata E-37", "id": "388399", "rank": "strain"}, {"current_id": "3042615",
    "current_name": "Paraglaciecola sp. T6c", "frozen_label": null, "id": "342610",
    "rank": "species"}, {"current_id": "391624", "current_name": "Sulfitobacter indolifex
    HEL-45", "frozen_label": "Sulfitobacter indolifex HEL-45", "id": "391624", "rank":
    "strain"}, {"current_id": "167879", "current_name": "Colwellia psychrerythraea
    34H", "frozen_label": "Colwellia psychrerythraea 34H", "id": "167879", "rank":
    "strain"}, {"current_id": "314256", "current_name": "Oceanicola granulosus HTCC2516",
    "frozen_label": "Oceanicola granulosus HTCC2516", "id": "314256", "rank": "strain"},
    {"current_id": "207949", "current_name": "Bermanella marisrubri", "frozen_label":
    "Bermanella marisrubri", "id": "207949", "rank": "species"}, {"current_id": "290398",
    "current_name": "Chromohalobacter israelensis DSM 3043", "frozen_label": "Chromohalobacter
    israelensis DSM 3043", "id": "290398", "rank": "strain"}, {"current_id": "376686",
    "current_name": "Flavobacterium johnsoniae UW101", "frozen_label": "Flavobacterium
    johnsoniae UW101", "id": "376686", "rank": "strain"}, {"current_id": "411684",
    "current_name": "Hoeflea phototrophica DFL-43", "frozen_label": "Hoeflea phototrophica
    DFL-43", "id": "411684", "rank": "strain"}, {"current_id": "396588", "current_name":
    "Thioalkalivibrio sulfidiphilus HL-EbGr7", "frozen_label": "Thioalkalivibrio sulfidiphilus
    HL-EbGr7", "id": "396588", "rank": "strain"}]. Frozen labels may be historical
    aliases; resolution does not establish occurrence.'
  accessed_at: '2026-10-12T01:37:19.254663Z'
  support: supports
  locator: NCBI TaxId, ScientificName, Rank, AkaTaxIds and OtherNames
  snapshot_sha256: f6051ddbd355c412a484fa78a19e85857a099890755571feea232d85276cf8c3
- evidence_id: TAX1
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1890675%2C1919273%2C1934978%2C1934979%2C1934980%2C1934981%2C1934982%2C1934983%2C1934984%2C1934985%2C1934986%2C1934987%2C1934988%2C1934989%2C1934990%2C1934991%2C1934992%2C1934993%2C1934994%2C1934995%2C1934996%2C1934997%2C1934998%2C1934999%2C1935000%2C1935001%2C207949%2C207954%2C231024%2C232537%2C237491%2C237497%2C238209%2C239%2C2527775%2C253%2C256%2C290398%2C290400%2C2930037%2C294%2C303%2C306%2C31234%2C313594%2C313598%2C313603%2C314256%2C314271%2C314277%2C317619%2C318586%2C33953%2C34003%2C34012%2C34073%2C34085%2C342610%2C349521%2C357804%2C358%2C36987%2C371731%2C376686%2C381845%2C388399%2C391624%2C391626%2C396588%2C398580%2C39946%2C400668%2C40324%2C404941%2C409%2C411684%2C41211%2C427%2C439495%2C562%2C582402%2C65%2C665118%2C685&retmode=xml
  summary: 'The two chunks resolve all234 requested cohort IDs. This target=[{"current_id":
    "207954", "current_name": "Neptuniibacter caesariensis", "frozen_label": "Neptuniibacter
    caesariensis", "id": "207954", "rank": "species"}, {"current_id": "313594", "current_name":
    "Polaribacter irgensii 23-P", "frozen_label": "Polaribacter irgensii 23-P", "id":
    "313594", "rank": "strain"}, {"current_id": "314277", "current_name": "Marinomonas
    sp. MED121", "frozen_label": "Marinomonas sp. MED121", "id": "314277", "rank":
    "species"}, {"current_id": "357804", "current_name": "Psychromonas ingrahamii
    37", "frozen_label": "Psychromonas ingrahamii 37", "id": "357804", "rank": "strain"},
    {"current_id": "290400", "current_name": "Jannaschia sp. CCS1", "frozen_label":
    "Jannaschia sp. CCS1", "id": "290400", "rank": "species"}, {"current_id": "398580",
    "current_name": "Dinoroseobacter shibae DFL 12 = DSM 16493", "frozen_label": "Dinoroseobacter
    shibae DFL 12 = DSM 16493", "id": "398580", "rank": "strain"}, {"current_id":
    "313598", "current_name": "Polaribacter sp. MED152", "frozen_label": "Polaribacter
    sp. MED152", "id": "313598", "rank": "species"}, {"current_id": "318586", "current_name":
    "Paracoccus denitrificans PD1222", "frozen_label": "Paracoccus denitrificans PD1222",
    "id": "318586", "rank": "strain"}, {"current_id": "400668", "current_name": "Marinomonas
    sp. MWYL1", "frozen_label": "Marinomonas sp. MWYL1", "id": "400668", "rank": "species"},
    {"current_id": "349521", "current_name": "Hahella chejuensis KCTC 2396", "frozen_label":
    "Hahella chejuensis KCTC 2396", "id": "349521", "rank": "strain"}, {"current_id":
    "391626", "current_name": "Octadecabacter antarcticus 307", "frozen_label": "Octadecabacter
    antarcticus 307", "id": "391626", "rank": "strain"}, {"current_id": "439495",
    "current_name": "Pseudovibrio sp. JE062", "frozen_label": "Pseudovibrio sp. JE062",
    "id": "439495", "rank": "species"}, {"current_id": "314271", "current_name": "Maritimibacter
    alkaliphilus HTCC2654", "frozen_label": "Maritimibacter alkaliphilus HTCC2654",
    "id": "314271", "rank": "strain"}, {"current_id": "371731", "current_name": "Rhodobacter
    ferrooxidans", "frozen_label": "Rhodobacter ferrooxidans", "id": "371731", "rank":
    "species"}, {"current_id": "313603", "current_name": "Maribacter sp. HTCC2170",
    "frozen_label": "Maribacter sp. HTCC2170", "id": "313603", "rank": "species"},
    {"current_id": "388399", "current_name": "Sagittula stellata E-37", "frozen_label":
    "Sagittula stellata E-37", "id": "388399", "rank": "strain"}, {"current_id": "3042615",
    "current_name": "Paraglaciecola sp. T6c", "frozen_label": null, "id": "342610",
    "rank": "species"}, {"current_id": "391624", "current_name": "Sulfitobacter indolifex
    HEL-45", "frozen_label": "Sulfitobacter indolifex HEL-45", "id": "391624", "rank":
    "strain"}, {"current_id": "167879", "current_name": "Colwellia psychrerythraea
    34H", "frozen_label": "Colwellia psychrerythraea 34H", "id": "167879", "rank":
    "strain"}, {"current_id": "314256", "current_name": "Oceanicola granulosus HTCC2516",
    "frozen_label": "Oceanicola granulosus HTCC2516", "id": "314256", "rank": "strain"},
    {"current_id": "207949", "current_name": "Bermanella marisrubri", "frozen_label":
    "Bermanella marisrubri", "id": "207949", "rank": "species"}, {"current_id": "290398",
    "current_name": "Chromohalobacter israelensis DSM 3043", "frozen_label": "Chromohalobacter
    israelensis DSM 3043", "id": "290398", "rank": "strain"}, {"current_id": "376686",
    "current_name": "Flavobacterium johnsoniae UW101", "frozen_label": "Flavobacterium
    johnsoniae UW101", "id": "376686", "rank": "strain"}, {"current_id": "411684",
    "current_name": "Hoeflea phototrophica DFL-43", "frozen_label": "Hoeflea phototrophica
    DFL-43", "id": "411684", "rank": "strain"}, {"current_id": "396588", "current_name":
    "Thioalkalivibrio sulfidiphilus HL-EbGr7", "frozen_label": "Thioalkalivibrio sulfidiphilus
    HL-EbGr7", "id": "396588", "rank": "strain"}]. Frozen labels may be historical
    aliases; resolution does not establish occurrence.'
  accessed_at: '2026-10-12T01:37:21.106280Z'
  support: supports
  locator: NCBI TaxId, ScientificName, Rank, AkaTaxIds and OtherNames
  snapshot_sha256: 3d4ba70a3bd80a91ef05ee66474dbf2646354a5d71a6c82ab2145c37e536b61a
- evidence_id: SEARCH
  kind: search
  reference: curation; history; research; reports; reviews; data/raw; data/habitats;
    conf
  summary: 'Identifier, label, slug and exact source-path searches included ignored/hidden
    files in these roots; coverage used Path.rglob. No earlier structured observation
    of this target found. Legacy reports were indexed, not uniformly rereviewed. Original
    membership search={"configured_root": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe",
    "root_exists": true, "exact_paths": [{"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_nodes.tsv",
    "exists": false, "expected_sha256": "c13c21bdd04619c75ce16e63b05e51577b0cefec5b61765d383313f654ab3fae"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_edges.tsv",
    "exists": false, "expected_sha256": "54982c25de9d2c820eeebc1452aeac0b034595921d04d55b810bf1d2b1e127e0"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/nodes.tsv",
    "exists": false, "expected_sha256": "a2a2f9acae230636dd866347d173a32c9f025c04a377060087a4be65781628f3"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/edges.tsv",
    "exists": false, "expected_sha256": "ab6208bff4854db7c1a736d53d0aa04269a682ab15a1ce6f37c6d731000281d7"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/nodes.tsv",
    "exists": false, "expected_sha256": "020de3afc71495571ddb05000c83a58d009272f53735b5f7c9326c1293e0415c"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/edges.tsv",
    "exists": false, "expected_sha256": "8863ee3197a36915865fa4833df39d10c3f8f69b64bafbb746b9cd731308a0aa"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/nodes.tsv",
    "exists": false, "expected_sha256": "cc5941cd677831e8e207da018dca763cd009bb1f9310b21cb4d45892316e006d"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/edges.tsv",
    "exists": false, "expected_sha256": "fd333634eaaa3cfe57a35cdca2f4c5b8cf0662851c1df58914d3e999d62a650e"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/environments.csv",
    "exists": false, "expected_sha256": "99299fe635159712f95568783ad3b484230fb31781262f1f6f8bd84db4bc3048"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/mappings/isolation_source_to_ontology.tsv",
    "exists": false, "expected_sha256": "2dea3d1bb20c72a04b6f64a67e2bb2bdc4f3649b809c5935390239be2791ef1f"}],
    "traversal": [{"command": ["rg", "--files", "--no-ignore", "--hidden", "data"],
    "exit_code": 0, "matches": [], "stderr": ""}, {"command": ["rg", "--files", "--no-ignore",
    "--hidden", "build"], "exit_code": 0, "matches": [], "stderr": ""}, {"command":
    ["rg", "--files", "--no-ignore", "--hidden", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data"],
    "exit_code": 0, "matches": [], "stderr": ""}]}'
  accessed_at: '2026-10-12T01:53:16.410488Z'
  support: supports
  locator: Bounded ignored-inclusive searches; no global absence claim
  search_scope: 'Identifier, label, slug and exact source-path searches included ignored/hidden
    files in these roots; coverage used Path.rglob. No earlier structured observation
    of this target found. Legacy reports were indexed, not uniformly rereviewed. Original
    membership search={"configured_root": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe",
    "root_exists": true, "exact_paths": [{"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_nodes.tsv",
    "exists": false, "expected_sha256": "c13c21bdd04619c75ce16e63b05e51577b0cefec5b61765d383313f654ab3fae"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_edges.tsv",
    "exists": false, "expected_sha256": "54982c25de9d2c820eeebc1452aeac0b034595921d04d55b810bf1d2b1e127e0"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/nodes.tsv",
    "exists": false, "expected_sha256": "a2a2f9acae230636dd866347d173a32c9f025c04a377060087a4be65781628f3"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/edges.tsv",
    "exists": false, "expected_sha256": "ab6208bff4854db7c1a736d53d0aa04269a682ab15a1ce6f37c6d731000281d7"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/nodes.tsv",
    "exists": false, "expected_sha256": "020de3afc71495571ddb05000c83a58d009272f53735b5f7c9326c1293e0415c"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/edges.tsv",
    "exists": false, "expected_sha256": "8863ee3197a36915865fa4833df39d10c3f8f69b64bafbb746b9cd731308a0aa"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/nodes.tsv",
    "exists": false, "expected_sha256": "cc5941cd677831e8e207da018dca763cd009bb1f9310b21cb4d45892316e006d"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/edges.tsv",
    "exists": false, "expected_sha256": "fd333634eaaa3cfe57a35cdca2f4c5b8cf0662851c1df58914d3e999d62a650e"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/environments.csv",
    "exists": false, "expected_sha256": "99299fe635159712f95568783ad3b484230fb31781262f1f6f8bd84db4bc3048"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/mappings/isolation_source_to_ontology.tsv",
    "exists": false, "expected_sha256": "2dea3d1bb20c72a04b6f64a67e2bb2bdc4f3649b809c5935390239be2791ef1f"}],
    "traversal": [{"command": ["rg", "--files", "--no-ignore", "--hidden", "data"],
    "exit_code": 0, "matches": [], "stderr": ""}, {"command": ["rg", "--files", "--no-ignore",
    "--hidden", "build"], "exit_code": 0, "matches": [], "stderr": ""}, {"command":
    ["rg", "--files", "--no-ignore", "--hidden", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data"],
    "exit_code": 0, "matches": [], "stderr": ""}]}'
- evidence_id: ISSUES
  kind: database
  reference: https://github.com/CultureBotAI/HabitatMech/issues
  summary: Read-only all-state959-issue title/body census checked for overlaps, including
    shared1249 and1398 and prior hot-spring correction1238. Prior issue closure is
    not primary scientific evidence. Comments were not exhaustively crawled.
  accessed_at: '2026-10-12T01:53:16.410488Z'
  support: supports
  locator: GitHub CLI census and relevant issue bodies
assessments:
- assessment_id: IDENTITY
  area: identity
  topic: Exact identity, definition and source intent
  outcome: supported
  summary: The PREGO record names the broad ENVO geographic feature associated with
    water, not a particular river or water material. Its geographic-feature genus
    is supported. Official fluvial feature is related rather than exact; several PREGO
    lexical variants are malformed. Scores around 1.8 rank associations from a 1427-taxon
    pool and are not occurrence probabilities.
  target_ids:
  - ENVO:00000012
  evidence_ids:
  - R
  - RAW
  - ONT
  - PARENT
- assessment_id: HIERARCHY
  area: grounding
  topic: All parent contributions and mapping scope
  outcome: supported
  summary: The PREGO record names the broad ENVO geographic feature associated with
    water, not a particular river or water material. Its geographic-feature genus
    is supported. Official fluvial feature is related rather than exact; several PREGO
    lexical variants are malformed. Scores around 1.8 rank associations from a 1427-taxon
    pool and are not occurrence probabilities. Ontology, GOLD path, ambiguous-leaf
    and authored-genus contributions were distinguished.
  target_ids:
  - ENVO:00000012
  evidence_ids:
  - R
  - RAW
  - CODE
  - ONT
  - PARENT
- assessment_id: PROVENANCE
  area: provenance
  topic: Source units, decision ownership and native lifecycle
  outcome: supported
  summary: 'Complete reconstruction preserves 1 source concepts and 0 ITEM-reviewed
    contributors. Attestations=[{"source": "PREGO", "source_id": "ENVO:00000012",
    "source_label": "hydrographic feature", "assertion_count": 1427, "assertion_unit":
    "TAXON", "score": 1.81611, "evidence_channels": "environmental_samples"}]. Unlike
    units are not summed; omitted direct counts do not imply ecological absence. This
    review does not change native status.'
  target_ids:
  - ENVO:00000012
  evidence_ids:
  - R
  - RAW
  - CODE
  - RULES
- assessment_id: TAXA
  area: evidence
  topic: Association versus characteristic presence
  outcome: supported
  summary: All emitted taxon IDs resolve, including merged identifiers and historical
    spellings. Full reconstruction preserves source pools, ranks, scores and corroborations;
    displayed taxa are selected associations, not exhaustive occurrence evidence.
    No is_characteristic assertion is present. A source score is not a probability
    or habitat abundance.
  target_ids:
  - ENVO:00000012
  evidence_ids:
  - R
  - RAW
  - TAX0
  - TAX1
  - RULES
- assessment_id: COMPLETENESS
  area: completeness
  topic: Optional slots and evidence boundaries
  outcome: supported
  summary: Missing optional definitions or datasets alone do not establish defects.
    No causal graph is asserted in this exact record; ignored-inclusive overlay search
    and the causal corpus gate were checked. Habitat associations without named gene/regulator
    or transcriptome claims do not justify an iModulon query.
  target_ids:
  - ENVO:00000012
  evidence_ids:
  - R
  - RAW
  - RULES
  - SEARCH
findings:
- finding_id: F1
  issue_key: envo-00000012-ontology-synonym-scope
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Non-exact ontology synonyms are promoted to exact
  description: 'fluvial feature: RELATED, not EXACT. The PREGO record names the broad
    ENVO geographic feature associated with water, not a particular river or water
    material. Its geographic-feature genus is supported. Official fluvial feature
    is related rather than exact; several PREGO lexical variants are malformed. Scores
    around 1.8 rank associations from a 1427-taxon pool and are not occurrence probabilities.'
  target_ids:
  - ENVO:00000012
  field_paths:
  - synonyms
  evidence_ids:
  - R
  - RAW
  - ONT
  - CODE
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Typed ontology synonym ingestion
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Governed ontology source
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Scope preservation
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: major
  normalization_reason: Material hierarchy, identity, scope or comparison-contract
    concern.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1249
- finding_id: F2
  issue_key: envo-00000012-malformed-source-alias
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Malformed inherited lexical variants are retained
  description: OVERFALLSs, overfallses, overfallsic and tidal ripp/ripps are source
    lexical artifacts, not alternative habitat identities.
  target_ids:
  - ENVO:00000012
  field_paths:
  - synonyms
  evidence_ids:
  - R
  - RAW
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitats.tsv
    role: Trace exact source variants
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Governed lexical ingestion
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: minor
  normalization_reason: Bounded lexical or explanatory wording defect; core identity
    or mechanism remains supported.
actions:
- action_id: A1
  description: Resolve shared1249 through governed typed-synonym ingestion and consumer
    tests; retain genuine exact names and PREGO related aliases instead of globally
    downgrading all synonyms.
  finding_ids:
  - F1
  target_ids:
  - ENVO:00000012
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Typed ontology synonym ingestion
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Governed ontology source
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Scope preservation
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Change only maintained inputs after source-level assessment; preserve independent
    true parents, identities, source counts/units and lifecycle.
  - Append required history, add focused regressions, inspect a seed canary and regenerate
    affected products without hand-editing records or pages.
  - Pass schema, strict, product-label, corpus reproduction, causal/history, review-integrity
    and full QC; save a linked successor for every finding disposition.
- action_id: A2
  description: Trace and correct the exact lexical artifacts through source handling
    while preserving valid aliases, source identity and scoring.
  finding_ids:
  - F2
  target_ids:
  - ENVO:00000012
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitats.tsv
    role: Trace exact source variants
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Governed lexical ingestion
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Change only maintained inputs after source-level assessment; preserve independent
    true parents, identities, source counts/units and lifecycle.
  - Append required history, add focused regressions, inspect a seed canary and regenerate
    affected products without hand-editing records or pages.
  - Pass schema, strict, product-label, corpus reproduction, causal/history, review-integrity
    and full QC; save a linked successor for every finding disposition.
limitations:
- Completed scientific assessment is not a clean-corpus verdict or proof of every
  original occurrence.
- Only first3 exact BioSample/Organism descriptions per sheet were individually interpreted;
  all other matches and study joins were indexed, not individually assessed.
- The later GOLD export/classification are not reconstructed August membership; original
  assertion inputs were not fully recovered. No ontology, taxonomy or source snapshot
  was refreshed.
- Same-agent review, not independent approval. Native status and curation/history
  inputs are unchanged.
- SSSOM/KGX conformance with current kg-microbe modeling was not audited; shared mapping-endpoint
  issue1398 remains unresolved.
- Whole-corpus review remains incomplete; ancestor context and indexing add no record
  coverage. Product-label gate retains2057 SKIPPED_NO_ADAPTER targets and5 accepted
  exceptions; it does not certify scientific identity.
notes:
- New immutable observation only; no source curation, native status promotion or GitHub
  mutation.
- No earlier structured target observation found; legacy reports remain historical
  and are not silently retired.
tags:
- habitatmech
- aquatic
- record-review
- scientific-review
```
