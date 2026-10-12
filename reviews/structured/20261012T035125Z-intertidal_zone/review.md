# Scientific record review: intertidal_zone

- Review: 20261012T035125Z-intertidal_zone
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-12T03:33:35.063495Z
- Finished UTC: 2026-10-12T03:51:25.648123Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

ENVO:00000316 denotes the region between tidal marks and has the supported marine-environmental-zone genus. PREGO supplies 53 TAXON candidates with 25 displayed associations. Official IntertidalZone is exact, whereas littoral zone is related and coastal zone broad; their ingestion must preserve these scopes.

## Scope And Provenance

Entire exact generated record, all contributors and individual asserted mechanism edges, with bounded source-context assessment.

Selection: Next forty records without a completed individual scientific review in stable repository-relative path order: hydrothermal plume through marginal sea biome. Full individual observations, not a category-wide pass. Starting observation coverage648/3208 is not clean current-input coverage.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 0cdeb733c38557948747ac46dbf98651279f8bd1.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| ENVO:00000316 | data/habitats/aquatic/intertidal_zone.yaml | generated | intertidal zone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native gate on captured scientific inputs | passed | True | ENVO:00000316 | Actual success from 2026-10-12T03:35:48.904082Z to 2026-10-12T03:35:52.188981Z. Native scope retained. |
| Native gate on captured scientific inputs | passed | True | ENVO:00000316 | Actual success from 2026-10-12T03:37:03.419277Z to 2026-10-12T03:37:12.395795Z. Native scope retained. |
| Native gate on captured scientific inputs | passed | True | ENVO:00000316 | Actual success from 2026-10-12T03:37:12.396779Z to 2026-10-12T03:37:31.652184Z. Native scope retained. |
| Native gate on captured scientific inputs | passed | True | ENVO:00000316 | Actual success from 2026-10-12T03:37:31.653951Z to 2026-10-12T03:38:23.419150Z. Native scope retained. |
| Native gate on captured scientific inputs | passed | True | ENVO:00000316 | Actual success from 2026-10-12T03:38:23.420244Z to 2026-10-12T03:38:32.031101Z. Native scope retained. |
| Native gate on captured scientific inputs | passed | True | ENVO:00000316 | Actual success from 2026-10-12T03:38:32.032463Z to 2026-10-12T03:38:37.476375Z. Native scope retained. |
| Native gate on captured scientific inputs | passed | True | ENVO:00000316 | Actual success from 2026-10-12T03:38:37.477529Z to 2026-10-12T03:39:03.951019Z. Native scope retained. |
| Native gate on captured scientific inputs | passed | True | ENVO:00000316 | Actual success from 2026-10-12T03:39:03.953076Z to 2026-10-12T03:39:05.157446Z. Native scope retained. |
| Native gate on captured scientific inputs | passed | True | ENVO:00000316 | Actual success from 2026-10-12T03:36:13.751706Z to 2026-10-12T03:36:15.983252Z. All three required merge-group workflows passed at the exact captured base; authoritative QC passed 886 tests with 3 skipped. Newly saved review bundles require their own integrity check. Exact-base CI receipt; these new review bundles were not part of that CI run. |
| Complete target reconstruction | passed | False | ENVO:00000316 | All40 complete documents matched; captured input hashes verified again before authoring. |
| Original assertion membership | unavailable | False | ENVO:00000316 | Bounded ignored-inclusive searches did not recover the complete original assertion inputs. Later exports supply context only. |
| Structured expression applicability | not_applicable | False | ENVO:00000316 | Successful dataset inventory was inspected for graphs; no matching claim-specific strain/gene or expression-module assertion is present. Generic pathway/stress vocabulary alone cannot certify natural habitat occurrence or causation. No component hit was asserted, so no summarize call applies. |

## Scientific And Domain Assessments

### Exact identity, definition and source intent

identity: supported. Targets: ENVO:00000316.

ENVO:00000316 denotes the region between tidal marks and has the supported marine-environmental-zone genus. PREGO supplies 53 TAXON candidates with 25 displayed associations. Official IntertidalZone is exact, whereas littoral zone is related and coastal zone broad; their ingestion must preserve these scopes.

### All parent contributions and mapping scope

grounding: supported. Targets: ENVO:00000316.

ENVO:00000316 denotes the region between tidal marks and has the supported marine-environmental-zone genus. PREGO supplies 53 TAXON candidates with 25 displayed associations. Official IntertidalZone is exact, whereas littoral zone is related and coastal zone broad; their ingestion must preserve these scopes. Ontology, GOLD path, ambiguous-leaf and authored-genus contributions were distinguished.

### Source units, decision ownership and native lifecycle

provenance: supported. Targets: ENVO:00000316.

Complete reconstruction preserves 1 source concepts and 0 ITEM-reviewed contributors. Attestations=[{"source": "PREGO", "source_id": "ENVO:00000316", "source_label": "intertidal zone", "assertion_count": 53, "assertion_unit": "TAXON", "score": 4.0, "evidence_channels": "annotated_genomes_isolates"}]. Unlike units are not summed; omitted direct counts do not imply ecological absence. This review does not change native status.

### Association versus characteristic presence

evidence: supported. Targets: ENVO:00000316.

All emitted taxon IDs resolve, including merged identifiers. Historical spellings were checked; unresolved row-specific name scope is recorded separately. Full reconstruction preserves source pools, ranks, scores and corroborations; displayed taxa are selected associations, not exhaustive occurrence evidence. No is_characteristic assertion is present. A source score is not a probability or habitat abundance.

### Optional slots and evidence boundaries

completeness: supported. Targets: ENVO:00000316.

Missing optional definitions or datasets alone do not establish defects. No causal graph is asserted in this exact record; ignored-inclusive overlay search and the causal corpus gate were checked. Habitat associations without named gene/regulator or transcriptome claims do not justify an iModulon query.

## Findings

### F1: Non-exact ontology synonyms are promoted to exact

major / open / confirmed; issue key: envo-00000316-ontology-synonym-scope.

littoral zone is RELATED and coastal zone BROAD; IntertidalZone remains EXACT. ENVO:00000316 denotes the region between tidal marks and has the supported marine-environmental-zone genus. PREGO supplies 53 TAXON candidates with 25 displayed associations. Official IntertidalZone is exact, whereas littoral zone is related and coastal zone broad; their ingestion must preserve these scopes.

## Recommended Actions And Acceptance Checks

### A1

Resolve shared1249 through governed typed-synonym ingestion and consumer tests; retain genuine exact names and PREGO related aliases instead of globally downgrading all synonyms.

- Change only maintained inputs after source-level assessment; preserve independent true parents, identities, source counts/units and lifecycle.
- Append required history, add focused regressions, inspect a seed canary and regenerate affected products without hand-editing records or pages.
- Pass schema, strict, product-label, corpus reproduction, causal/history, review-integrity and full QC; save a linked successor for every finding disposition.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R | data/habitats/aquatic/intertidal_zone.yaml; Entire captured YAML read, including provenance, parameters, taxa, graphs and generated history | supports | ENVO:00000316 denotes the region between tidal marks and has the supported marine-environmental-zone genus. PREGO supplies 53 TAXON candidates with 25 displayed associations. Official IntertidalZone is exact, whereas littoral zone is related and coastal zone broad; their ingestion must preserve these scopes. |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; src/habitatmech/schema/habitatmech.yaml | supports | Applied exact identity, strict-parent, MIxS-role, source unit/score and ITEM lifecycle contracts. STATE is a cellular value, not the process establishing it. Evidence is assessed at edge scope. |
| RAW | data/raw; curation/decisions.tsv; curation/term_requests.tsv; curation/gold_parent_exclusions.tsv; Exact logical TSV rows; header is row1; unrelated neighbor matches excluded | supports | {"data/raw/ontology_subclass_edges.tsv": [{"data": {"object": "ENVO:01001201", "predicate": "rdfs:subClassOf", "subject": "ENVO:00000316"}, "logical_row": 4959}], "data/raw/ontology_terms.tsv": [{"data": {"definition": "The area of the foreshore and seabed that is exposed to the air at low tide and submerged at high tide, i.e., the area between tide marks.", "deprecated": "", "directly_referenced": "TRUE", "label": "intertidal zone", "label_only": "FALSE", "ontology": "ENVO", "synonyms": "IntertidalZone&#124;coastal zone&#124;littoral zone", "term_id": "ENVO:00000316"}, "logical_row": 6899}], "data/raw/prego_habitat_taxa.tsv": [{"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank": "1", "taxon_id": "NCBITaxon:1040984", "taxon_label": "Mesorhizobium sp. WSM1293"}, "logical_row": 4588}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank": "2", "taxon_id": "NCBITaxon:1048", "taxon_label": "Marichromatium gracile"}, "logical_row": 4589}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank": "3", "taxon_id": "NCBITaxon:1120965", "taxon_label": "Algoriphagus mannitolivorans DSM 15301"}, "logical_row": 4590}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank": "4", "taxon_id": "NCBITaxon:1121014", "taxon_label": "Arenimonas donghaensis DSM 18148 = HO3-R19"}, "logical_row": 4591}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank": "5", "taxon_id": "NCBITaxon:1121403", "taxon_label": "Desulfogranum japonicum DSM 18378"}, "logical_row": 4592}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank": "6", "taxon_id": "NCBITaxon:1121416", "taxon_label": "Desulfopila aestuarii DSM 18488"}, "logical_row": 4593}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank": "7", "taxon_id": "NCBITaxon:1121938", "taxon_label": "Halobacillus kuroshimensis DSM 18393"}, "logical_row": 4594}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank": "8", "taxon_id": "NCBITaxon:1122176", "taxon_label": "Lewinella cohaerens DSM 23179"}, "logical_row": 4595}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank": "9", "taxon_id": "NCBITaxon:1122197", "taxon_label": "Marinobacter daepoensis DSM 16072"}, "logical_row": 4596}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank": "10", "taxon_id": "NCBITaxon:1122599", "taxon_label": "Neptunomonas japonica DSM 18939"}, "logical_row": 4597}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank": "11", "taxon_id": "NCBITaxon:1123000", "taxon_label": "Propionigenium maris DSM 9537"}, "logical_row": 4598}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank": "12", "taxon_id": "NCBITaxon:1123503", "taxon_label": "Woodsholea maritima DSM 17123"}, "logical_row": 4599}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank": "13", "taxon_id": "NCBITaxon:1123509", "taxon_label": "Zooshikella ganghwensis DSM 15267"}, "logical_row": 4600}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank": "14", "taxon_id": "NCBITaxon:1123515", "taxon_label": "Thiomicrorhabdus chilensis DSM 12352"}, "logical_row": 4601}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank": "15", "taxon_id": "NCBITaxon:1123517", "taxon_label": "Thiomicrospira pelophila DSM 1534"}, "logical_row": 4602}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank": "16", "taxon_id": "NCBITaxon:1278307", "taxon_label": "Psychromonas ossibalaenae ATCC BAA-1528"}, "logical_row": 4603}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank": "17", "taxon_id": "NCBITaxon:1397696", "taxon_label": "Exiguobacterium marinum DSM 16307"}, "logical_row": 4604}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank": "18", "taxon_id": "NCBITaxon:1408433", "taxon_label": "Crocinitomix catalasitica ATCC 23190"}, "logical_row": 4605}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank": "19", "taxon_id": "NCBITaxon:1442586", "taxon_label": "Winogradskyella wandonensis"}, "logical_row": 4606}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank": "20", "taxon_id": "NCBITaxon:150", "taxon_label": "Spirochaeta isovalerica"}, "logical_row": 4607}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank": "21", "taxon_id": "NCBITaxon:163908", "taxon_label": "Anabaena sp. PCC 7108"}, "logical_row": 4608}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank": "22", "taxon_id": "NCBITaxon:166318", "taxon_label": "Synechococcus sp. WH 8016"}, "logical_row": 4609}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank": "23", "taxon_id": "NCBITaxon:203122", "taxon_label": "Saccharophagus degradans 2-40"}, "logical_row": 4610}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank": "24", "taxon_id": "NCBITaxon:226505", "taxon_label": "Algoriphagus halophilus"}, "logical_row": 4611}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank": "25", "taxon_id": "NCBITaxon:285258", "taxon_label": "Tenacibaculum lutimaris"}, "logical_row": 4612}], "data/raw/prego_habitats.tsv": [{"data": {"biolink_category": "biolink:OntologyClass", "channels": "annotated_genomes_isolates", "direct_assertion_count": "54", "max_prego_score": "4", "ontology": "ENVO", "prego_id": "ENVO:00000316", "prego_synonyms": "intertidal&#124;intertidal zone&#124;intertidalic&#124;intertidals&#124;littoral&#124;littoral zone&#124;littoralic&#124;littorals", "taxon_count": "53"}, "logical_row": 220}]} |
| CODE | src/habitatmech/seed.py; Executed complete-document reconstruction; all40 matched captured records | supports | {"reviewed_sources": 0, "routes": [{"actual": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:00000316", "mapping_predicate": null, "reviewed": false, "route": "prego_self_grounded"}, "automatic": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:00000316", "mapping_predicate": null, "reviewed": false, "route": "prego_self_grounded"}, "minted": "habitatmech:PREGO.1e1d841752", "source": "PREGO", "source_id": "ENVO:00000316"}], "source_concepts": 1} |
| ONT | https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl; Official OWL fetched11-Oct; identity, deprecated/replacement metadata, typed synonyms and direct axioms; no snapshot refresh | supports | {"ENVO:00000316": {"definitions": ["The area of the foreshore and seabed that is exposed to the air at low tide and submerged at high tide, i.e., the area between tide marks."], "deprecated": [], "equivalents": [], "labels": ["intertidal zone"], "parents": ["http://purl.obolibrary.org/obo/ENVO_01001201", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/BFO_0000050"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_00000304"]}, {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002131"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_01001468"]}], "replacements": [], "synonyms": {"hasBroadSynonym": ["coastal zone"], "hasExactSynonym": ["IntertidalZone"], "hasNarrowSynonym": [], "hasRelatedSynonym": ["littoral zone"]}}, "ENVO:01001201": {"definitions": ["An astronomical body part which is part of a marine environment."], "deprecated": [], "equivalents": [], "labels": ["marine environmental zone"], "parents": ["http://purl.obolibrary.org/obo/ENVO_01000813", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/BFO_0000050"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_01000320"]}], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}} |
| PARENT | data/raw/ontology_terms.tsv; Ancestor context is not full-record review coverage of ancestors | supports | {} |
| TAX0 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=100038%2C1007122%2C1007124%2C1009420%2C1009695%2C1026%2C1027249%2C103%2C1033802%2C1033806%2C1033810%2C1034944%2C1036674%2C103810%2C1040984%2C1041152%2C104176%2C104245%2C1045010%2C1048%2C1048380%2C1048396%2C1058%2C106111%2C1063%2C106370%2C106592%2C1069%2C1069073%2C1069081%2C1069083%2C1071078%2C1071079%2C1074%2C107400%2C107401%2C1076695%2C107820%2C108003%2C1082479%2C1085%2C1087%2C108901%2C108943%2C109263%2C1096246%2C109635%2C110101%2C1101193%2C110933%2C1114856%2C111805%2C1118153%2C1120797%2C1120956%2C1120961%2C1120963%2C1120965%2C1120983%2C1120998%2C1121007%2C1121014%2C1121087%2C1121264%2C1121266%2C1121301%2C1121317%2C1121324%2C1121390%2C1121392%2C1121403%2C1121416%2C1121451%2C1121459%2C1121463%2C1121911%2C1121912%2C1121931%2C1121938%2C1121940%2C1122135%2C1122137%2C1122176%2C1122195%2C1122197%2C1122226%2C112235%2C112248%2C1122599%2C1123000%2C1123053%2C1123251%2C1123270%2C1123325%2C1123349%2C1123350%2C1123371%2C1123380%2C1123503%2C1123509%2C1123515%2C1123517%2C1125975%2C1131812%2C114497%2C114628%2C114707%2C114712%2C114715%2C115553%2C117681%2C1188994%2C120749%2C1214577%2C121845%2C1218948%2C1265%2C126740%2C1270%2C127458%2C127520%2C1278307%2C128%2C1280%2C129817%2C130049%2C13035%2C1303716%2C1334019%2C1341154%2C1358%2C13684%2C137510%2C1380347%2C139239%2C1397696%2C1402%2C1408%2C1408433%2C1409%2C1424653%2C1436140%2C1442586%2C147%2C1478%2C1495045%2C149712%2C150%2C1505%2C152&amp;retmode=xml; NCBI TaxId, ScientificName, Rank, AkaTaxIds and OtherNames | supports | The two chunks resolve all252 requested cohort IDs. This target=[{"current_id": "1040984", "current_name": "Mesorhizobium sp. WSM1293", "frozen_label": "Mesorhizobium sp. WSM1293", "id": "1040984", "rank": "species"}, {"current_id": "1048", "current_name": "Marichromatium gracile", "frozen_label": "Marichromatium gracile", "id": "1048", "rank": "species"}, {"current_id": "1120965", "current_name": "Algoriphagus mannitolivorans DSM 15301", "frozen_label": "Algoriphagus mannitolivorans DSM 15301", "id": "1120965", "rank": "strain"}, {"current_id": "1121014", "current_name": "Arenimonas donghaensis DSM 18148 = HO3-R19", "frozen_label": "Arenimonas donghaensis DSM 18148 = HO3-R19", "id": "1121014", "rank": "strain"}, {"current_id": "1121403", "current_name": "Desulfogranum japonicum DSM 18378", "frozen_label": "Desulfogranum japonicum DSM 18378", "id": "1121403", "rank": "strain"}, {"current_id": "1121416", "current_name": "Desulfopila aestuarii DSM 18488", "frozen_label": "Desulfopila aestuarii DSM 18488", "id": "1121416", "rank": "strain"}, {"current_id": "1121938", "current_name": "Halobacillus kuroshimensis DSM 18393", "frozen_label": "Halobacillus kuroshimensis DSM 18393", "id": "1121938", "rank": "strain"}, {"current_id": "1122176", "current_name": "Lewinella cohaerens DSM 23179", "frozen_label": "Lewinella cohaerens DSM 23179", "id": "1122176", "rank": "strain"}, {"current_id": "1122197", "current_name": "Marinobacter daepoensis DSM 16072", "frozen_label": "Marinobacter daepoensis DSM 16072", "id": "1122197", "rank": "strain"}, {"current_id": "1122599", "current_name": "Neptunomonas japonica DSM 18939", "frozen_label": "Neptunomonas japonica DSM 18939", "id": "1122599", "rank": "strain"}, {"current_id": "1123000", "current_name": "Propionigenium maris DSM 9537", "frozen_label": "Propionigenium maris DSM 9537", "id": "1123000", "rank": "strain"}, {"current_id": "1123503", "current_name": "Woodsholea maritima DSM 17123", "frozen_label": "Woodsholea maritima DSM 17123", "id": "1123503", "rank": "strain"}, {"current_id": "1123509", "current_name": "Zooshikella ganghwensis DSM 15267", "frozen_label": "Zooshikella ganghwensis DSM 15267", "id": "1123509", "rank": "strain"}, {"current_id": "1123515", "current_name": "Thiomicrorhabdus chilensis DSM 12352", "frozen_label": "Thiomicrorhabdus chilensis DSM 12352", "id": "1123515", "rank": "strain"}, {"current_id": "1123517", "current_name": "Thiomicrospira pelophila DSM 1534", "frozen_label": "Thiomicrospira pelophila DSM 1534", "id": "1123517", "rank": "strain"}, {"current_id": "1278307", "current_name": "Psychromonas ossibalaenae ATCC BAA-1528", "frozen_label": "Psychromonas ossibalaenae ATCC BAA-1528", "id": "1278307", "rank": "strain"}, {"current_id": "1397696", "current_name": "Exiguobacterium marinum DSM 16307", "frozen_label": "Exiguobacterium marinum DSM 16307", "id": "1397696", "rank": "strain"}, {"current_id": "1408433", "current_name": "Crocinitomix catalasitica ATCC 23190", "frozen_label": "Crocinitomix catalasitica ATCC 23190", "id": "1408433", "rank": "strain"}, {"current_id": "1442586", "current_name": "Winogradskyella wandonensis", "frozen_label": "Winogradskyella wandonensis", "id": "1442586", "rank": "species"}, {"current_id": "150", "current_name": "Spirochaeta isovalerica", "frozen_label": "Spirochaeta isovalerica", "id": "150", "rank": "species"}, {"current_id": "163908", "current_name": "Anabaena sp. PCC 7108", "frozen_label": "Anabaena sp. PCC 7108", "id": "163908", "rank": "species"}, {"current_id": "166318", "current_name": "Synechococcus sp. WH 8016", "frozen_label": "Synechococcus sp. WH 8016", "id": "166318", "rank": "species"}, {"current_id": "203122", "current_name": "Saccharophagus degradans 2-40", "frozen_label": "Saccharophagus degradans 2-40", "id": "203122", "rank": "strain"}, {"current_id": "226505", "current_name": "Algoriphagus halophilus", "frozen_label": "Algoriphagus halophilus", "id": "226505", "rank": "species"}, {"current_id": "285258", "current_name": "Tenacibaculum lutimaris", "frozen_label": "Tenacibaculum lutimaris", "id": "285258", "rank": "species"}]. Frozen labels may be historical aliases; resolution does not establish occurrence. |
| TAX1 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1525%2C153026%2C153500%2C1537%2C1537524%2C153911%2C154510%2C1549639%2C155715%2C156%2C158080%2C158751%2C159087%2C161156%2C1639%2C163908%2C166318%2C1684%2C168471%2C172045%2C172371%2C173%2C1732%2C1734049%2C173764%2C1768%2C185294%2C198703%2C202747%2C203122%2C204773%2C205922%2C206665%2C210512%2C213224%2C223786%2C226505%2C230105%2C232721%2C240166%2C240167%2C240169%2C244366%2C259564%2C2663692%2C267990%2C279714%2C2850%2C285091%2C285258%2C285271%2C286698%2C287%2C292%2C292415%2C293%2C300%2C304%2C3055%2C312153%2C313606%2C314229%2C316%2C31910%2C332175%2C358%2C365044%2C371731%2C375286%2C375451%2C398578%2C39947%2C40214%2C405436%2C42256%2C431041%2C441157%2C452638%2C47885%2C48547%2C521674%2C535289%2C548%2C550984%2C562%2C563045%2C572546%2C573060%2C573064%2C59919%2C610380%2C643561%2C645472%2C655438%2C666681%2C679926%2C693972%2C710696%2C74152%2C746360%2C926690%2C935948&amp;retmode=xml; NCBI TaxId, ScientificName, Rank, AkaTaxIds and OtherNames | supports | The two chunks resolve all252 requested cohort IDs. This target=[{"current_id": "1040984", "current_name": "Mesorhizobium sp. WSM1293", "frozen_label": "Mesorhizobium sp. WSM1293", "id": "1040984", "rank": "species"}, {"current_id": "1048", "current_name": "Marichromatium gracile", "frozen_label": "Marichromatium gracile", "id": "1048", "rank": "species"}, {"current_id": "1120965", "current_name": "Algoriphagus mannitolivorans DSM 15301", "frozen_label": "Algoriphagus mannitolivorans DSM 15301", "id": "1120965", "rank": "strain"}, {"current_id": "1121014", "current_name": "Arenimonas donghaensis DSM 18148 = HO3-R19", "frozen_label": "Arenimonas donghaensis DSM 18148 = HO3-R19", "id": "1121014", "rank": "strain"}, {"current_id": "1121403", "current_name": "Desulfogranum japonicum DSM 18378", "frozen_label": "Desulfogranum japonicum DSM 18378", "id": "1121403", "rank": "strain"}, {"current_id": "1121416", "current_name": "Desulfopila aestuarii DSM 18488", "frozen_label": "Desulfopila aestuarii DSM 18488", "id": "1121416", "rank": "strain"}, {"current_id": "1121938", "current_name": "Halobacillus kuroshimensis DSM 18393", "frozen_label": "Halobacillus kuroshimensis DSM 18393", "id": "1121938", "rank": "strain"}, {"current_id": "1122176", "current_name": "Lewinella cohaerens DSM 23179", "frozen_label": "Lewinella cohaerens DSM 23179", "id": "1122176", "rank": "strain"}, {"current_id": "1122197", "current_name": "Marinobacter daepoensis DSM 16072", "frozen_label": "Marinobacter daepoensis DSM 16072", "id": "1122197", "rank": "strain"}, {"current_id": "1122599", "current_name": "Neptunomonas japonica DSM 18939", "frozen_label": "Neptunomonas japonica DSM 18939", "id": "1122599", "rank": "strain"}, {"current_id": "1123000", "current_name": "Propionigenium maris DSM 9537", "frozen_label": "Propionigenium maris DSM 9537", "id": "1123000", "rank": "strain"}, {"current_id": "1123503", "current_name": "Woodsholea maritima DSM 17123", "frozen_label": "Woodsholea maritima DSM 17123", "id": "1123503", "rank": "strain"}, {"current_id": "1123509", "current_name": "Zooshikella ganghwensis DSM 15267", "frozen_label": "Zooshikella ganghwensis DSM 15267", "id": "1123509", "rank": "strain"}, {"current_id": "1123515", "current_name": "Thiomicrorhabdus chilensis DSM 12352", "frozen_label": "Thiomicrorhabdus chilensis DSM 12352", "id": "1123515", "rank": "strain"}, {"current_id": "1123517", "current_name": "Thiomicrospira pelophila DSM 1534", "frozen_label": "Thiomicrospira pelophila DSM 1534", "id": "1123517", "rank": "strain"}, {"current_id": "1278307", "current_name": "Psychromonas ossibalaenae ATCC BAA-1528", "frozen_label": "Psychromonas ossibalaenae ATCC BAA-1528", "id": "1278307", "rank": "strain"}, {"current_id": "1397696", "current_name": "Exiguobacterium marinum DSM 16307", "frozen_label": "Exiguobacterium marinum DSM 16307", "id": "1397696", "rank": "strain"}, {"current_id": "1408433", "current_name": "Crocinitomix catalasitica ATCC 23190", "frozen_label": "Crocinitomix catalasitica ATCC 23190", "id": "1408433", "rank": "strain"}, {"current_id": "1442586", "current_name": "Winogradskyella wandonensis", "frozen_label": "Winogradskyella wandonensis", "id": "1442586", "rank": "species"}, {"current_id": "150", "current_name": "Spirochaeta isovalerica", "frozen_label": "Spirochaeta isovalerica", "id": "150", "rank": "species"}, {"current_id": "163908", "current_name": "Anabaena sp. PCC 7108", "frozen_label": "Anabaena sp. PCC 7108", "id": "163908", "rank": "species"}, {"current_id": "166318", "current_name": "Synechococcus sp. WH 8016", "frozen_label": "Synechococcus sp. WH 8016", "id": "166318", "rank": "species"}, {"current_id": "203122", "current_name": "Saccharophagus degradans 2-40", "frozen_label": "Saccharophagus degradans 2-40", "id": "203122", "rank": "strain"}, {"current_id": "226505", "current_name": "Algoriphagus halophilus", "frozen_label": "Algoriphagus halophilus", "id": "226505", "rank": "species"}, {"current_id": "285258", "current_name": "Tenacibaculum lutimaris", "frozen_label": "Tenacibaculum lutimaris", "id": "285258", "rank": "species"}]. Frozen labels may be historical aliases; resolution does not establish occurrence. |
| SEARCH | curation; history; research; reports; reviews; data/raw; data/habitats; conf; Bounded ignored-inclusive searches; no global absence claim | supports | Identifier, label, slug and exact source-path searches included ignored/hidden files in these roots; coverage used Path.rglob. No earlier structured observation of this target found. Legacy reports were indexed, not uniformly rereviewed. Original membership search={"configured_root": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe", "root_exists": true, "exact_paths": [{"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_nodes.tsv", "exists": false, "expected_sha256": "c13c21bdd04619c75ce16e63b05e51577b0cefec5b61765d383313f654ab3fae"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_edges.tsv", "exists": false, "expected_sha256": "54982c25de9d2c820eeebc1452aeac0b034595921d04d55b810bf1d2b1e127e0"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/nodes.tsv", "exists": false, "expected_sha256": "a2a2f9acae230636dd866347d173a32c9f025c04a377060087a4be65781628f3"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/edges.tsv", "exists": false, "expected_sha256": "ab6208bff4854db7c1a736d53d0aa04269a682ab15a1ce6f37c6d731000281d7"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/nodes.tsv", "exists": false, "expected_sha256": "020de3afc71495571ddb05000c83a58d009272f53735b5f7c9326c1293e0415c"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/edges.tsv", "exists": false, "expected_sha256": "8863ee3197a36915865fa4833df39d10c3f8f69b64bafbb746b9cd731308a0aa"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/nodes.tsv", "exists": false, "expected_sha256": "cc5941cd677831e8e207da018dca763cd009bb1f9310b21cb4d45892316e006d"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/edges.tsv", "exists": false, "expected_sha256": "fd333634eaaa3cfe57a35cdca2f4c5b8cf0662851c1df58914d3e999d62a650e"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/environments.csv", "exists": false, "expected_sha256": "99299fe635159712f95568783ad3b484230fb31781262f1f6f8bd84db4bc3048"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/mappings/isolation_source_to_ontology.tsv", "exists": false, "expected_sha256": "2dea3d1bb20c72a04b6f64a67e2bb2bdc4f3649b809c5935390239be2791ef1f"}], "traversal": [{"command": ["rg", "--files", "--no-ignore", "--hidden", "data"], "exit_code": 0, "matches": [], "stderr": ""}, {"command": ["rg", "--files", "--no-ignore", "--hidden", "build"], "exit_code": 0, "matches": [], "stderr": ""}, {"command": ["rg", "--files", "--no-ignore", "--hidden", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data"], "exit_code": 0, "matches": [], "stderr": ""}]} |
| ISSUES | https://github.com/CultureBotAI/HabitatMech/issues; GitHub CLI census and relevant issue bodies | supports | Read-only all-state964-issue title/body census checked for overlaps, including shared1249 and1398 and prior vent1239 and hypersaline1243 corrections. Prior issue closure is not primary scientific evidence. Comments were not exhaustively crawled. |

## Limits And Additional Notes

- Completed scientific assessment is not a clean-corpus verdict or proof of every original occurrence.
- Only first3 exact BioSample/Organism descriptions per sheet were individually interpreted; all other matches and study joins were indexed, not individually assessed.
- The later GOLD export/classification are not reconstructed August membership; original assertion inputs were not fully recovered. No ontology, taxonomy or source snapshot was refreshed.
- Same-agent review, not independent approval. Native status and curation/history inputs are unchanged.
- SSSOM/KGX conformance with current kg-microbe modeling was not audited; shared mapping-endpoint issue1398 remains unresolved.
- Whole-corpus review remains incomplete; ancestor context and indexing add no record coverage. Product-label checks retain documented no-adapter skips and accepted exceptions; they do not certify scientific identity.
- Initial immutable observation precedes separately authorized publication and curation; this observation itself changes no source record or native status.
- No earlier structured target observation found; legacy reports remain historical and are not silently retired.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T035125Z-intertidal_zone
kind: record
repository: CultureBotAI/HabitatMech
title: 'Scientific record review: intertidal_zone'
started_at: '2026-10-12T03:33:35.063495Z'
finished_at: '2026-10-12T03:51:25.648123Z'
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
summary: ENVO:00000316 denotes the region between tidal marks and has the supported
  marine-environmental-zone genus. PREGO supplies 53 TAXON candidates with 25 displayed
  associations. Official IntertidalZone is exact, whereas littoral zone is related
  and coastal zone broad; their ingestion must preserve these scopes.
source:
  git_revision: 0cdeb733c38557948747ac46dbf98651279f8bd1
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
    sha256: 2fd5aec7ac1710ede2405849e78dd0423c253d72b43676230f72b9905bae99dd
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 2d41fc93db4939122b3909f2a412b84b679703948b10d9f02e12021442f71407
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 6be3d043f1730c9098ade51833e311b5b5a14cfddbb83ef3af0e9713f4a52198
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
  - path: data/habitats/aquatic/intertidal_zone.yaml
    sha256: a1ebb321cfde461806414dcde6110e277127793a4fd4016887508291b4de57a2
    role: target
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
  - path: history/mappings/intertidal_zone/2026-10-06T183132Z-codex-gpt-5-6d1f29.yaml
    sha256: cadcd14a51a3621fa4d993bf027706e0e5e6d06a5b26d0ddecbcc24da6e26171
    role: context
  - path: history/mappings/subterranean_estuary/2026-10-06T122100Z-claude-code-e6ea40.yaml
    sha256: 337dedcf3b31e744fa2679f1dafa3a4c7342ac238e8f98b01241143aa498a38b
    role: context
  - path: history/mappings/thrombolites/2026-10-06T172127Z-claude-code-8f8722.yaml
    sha256: a4b965be126acc17504f89ab930126bb518f64162215138e42d59a2a4a92f252
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260927T073130Z-coral_reef.md
    sha256: 3b608b9c3fd7558216f7c92449dcfb34349f0a32503e01284208af9b181de52b
    role: context
  - path: reports/yaml_record_review/20261002T051030Z-estuary__bae88a25.md
    sha256: 37b9333abff759c2fa44f57b56e49cc214a3de57f15a4dd1caabf31d5518f932
    role: context
  - path: reports/yaml_record_review/20261003T151049Z-intertidal_zone.md
    sha256: 91799deb3d6a4eb30b7f8577095f1c785b76f854a11603fd51fdace1efbe7e18
    role: context
  - path: reports/yaml_record_review/20261003T151340Z-intertidal_zone__2f295854.md
    sha256: 8deb917e036da4baa06b6c53e9cd5f62a3ed2840653cc9f71999700e0061697a
    role: context
  - path: reports/yaml_record_review/20261003T151529Z-intertidal_zone__3d85893c.md
    sha256: ad555a5ebb87528070acf24cf5b361715e51e7e0f055b28cb9094f413b9863b8
    role: context
  - path: reports/yaml_record_review/20261004T183719Z-microbialites__2dd0659e.md
    sha256: b35f23a13be596950c956ceefe7e18f52f52ddac8e89d9c91857f7e4f4280e4a
    role: context
  - path: reports/yaml_record_review/20261004T220108Z-oil_contaminated.md
    sha256: a09a270810ba529be8aefc626d1a68ab660acc4e68e1368b864b61e588b404b3
    role: context
  - path: reports/yaml_record_review/20261004T221603Z-oil_contaminated_sediment__b1bb8113.md
    sha256: a0d108b2ae0d45369c8fe098567c3cc7bd37a472345b4b749afbd7641add9f2f
    role: context
  - path: reports/yaml_record_review/20261005T063232Z-salt_marsh__34fd781c.md
    sha256: 7e9e9653449edde30b731f171a37c8922e5497add98074ad94573691719277ab
    role: context
  - path: reports/yaml_record_review/20261005T063632Z-salt_marsh_sediment.md
    sha256: fd20cff2809b310ab37c39375fe6cbb3ce9f25b4f255721ce7dfa67b81505fdf
    role: context
  - path: reports/yaml_record_review/20261005T064509Z-salt_pond_sediment.md
    sha256: df8d37cfbcd3cc9711e3f1dcee48df4620e26d44fb2d736b042af9da47da3fe0
    role: context
  - path: reports/yaml_record_review/20261005T074020Z-sea_grass_bed.md
    sha256: 9fb4444c754ce1e1723ebf070091b4bf00d64b4ec644c03043940b8ac80bfbf0
    role: context
  - path: reports/yaml_record_review/20261005T085456Z-seagrass_bed_sediment.md
    sha256: 8850312900721ef09c463e31ecf7e13f5d4ddee5a9598e65f4a3684d3095b637
    role: context
  - path: reports/yaml_record_review/20261005T111751Z-sediment__2b3ec834.md
    sha256: e6ca42f5ff00b317c307e491da24aa1d9114ed72e5f33e9b1a27ee4190773471
    role: context
  - path: reports/yaml_record_review/20261006T061154Z-solar_salterns.md
    sha256: 8a034ec9fc14975e53a4fc1ab2f69e58f7e1801cb6a2a2ad7ea7e80b009b1fbd
    role: context
  - path: reports/yaml_record_review/20261006T065215Z-solar_salterns_sediment.md
    sha256: 26ef83437a1838f13e340d3703b9bfd3a57ad0fac4ed3ba4bc003b30278173ff
    role: context
  - path: reports/yaml_record_review/20261006T114536Z-subterranean_estuary.md
    sha256: 4b431e0ab82eb1e3cd57f5e89fb5d8b6d1d326a64866f5fedc0707ed4ced98c7
    role: context
  - path: reports/yaml_record_review/20261006T170416Z-thrombolites.md
    sha256: 3f48e8b00bb5d6092748109a6f0129de65d601323f19d117d7cd1a49a37d083f
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
- target_id: ENVO:00000316
  path: data/habitats/aquatic/intertidal_zone.yaml
  label: intertidal zone
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
    in stable repository-relative path order: hydrothermal plume through marginal
    sea biome. Full individual observations, not a category-wide pass. Starting observation
    coverage648/3208 is not clean current-input coverage.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - ENVO:00000316
  exclusions:
  - target: Other3207 current records
    reason: Context reads are not their full scientific review.
checks:
- check_id: C0
  name: Native gate on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00000316
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=0cdeb733c38557948747ac46dbf98651279f8bd1
    just validate data/habitats/aquatic/intertidal_zone.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success from 2026-10-12T03:35:48.904082Z to 2026-10-12T03:35:52.188981Z.
    Native scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C1
  name: Native gate on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00000316
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=0cdeb733c38557948747ac46dbf98651279f8bd1
    just validate-strict data/habitats/aquatic/hydrothermal_plume.yaml data/habitats/aquatic/hydrothermal_vent.yaml
    data/habitats/aquatic/hypersaline_lake.yaml data/habitats/aquatic/hypersaline_soda_lake.yaml
    data/habitats/aquatic/hypersaline_spring.yaml data/habitats/aquatic/hypersaline_water.yaml
    data/habitats/aquatic/hypersaline_water_environment.yaml data/habitats/aquatic/hypolimnion.yaml
    data/habitats/aquatic/hypolimnion__78bbb31f.yaml data/habitats/aquatic/hypolimnion__d888743c.yaml
    data/habitats/aquatic/hypoxic_zone.yaml data/habitats/aquatic/ice.yaml data/habitats/aquatic/ice_accretions.yaml
    data/habitats/aquatic/ice_shelf.yaml data/habitats/aquatic/inlet.yaml data/habitats/aquatic/insect_burrows.yaml
    data/habitats/aquatic/intertidal_zone.yaml data/habitats/aquatic/intertidal_zone__2f295854.yaml
    data/habitats/aquatic/intertidal_zone__3d85893c.yaml data/habitats/aquatic/kettle.yaml
    data/habitats/aquatic/lake.yaml data/habitats/aquatic/lake__335782f4.yaml data/habitats/aquatic/lake_biofilm.yaml
    data/habitats/aquatic/lake_inlet.yaml data/habitats/aquatic/large_freshwater_lake_biome.yaml
    data/habitats/aquatic/large_river_biome.yaml data/habitats/aquatic/leachate.yaml
    data/habitats/aquatic/lentic_water_body.yaml data/habitats/aquatic/liftoff_microbial_mat.yaml
    data/habitats/aquatic/limnetic_zone.yaml data/habitats/aquatic/liquid_water.yaml
    data/habitats/aquatic/littoral_zone.yaml data/habitats/aquatic/littoral_zone__9f547c9b.yaml
    data/habitats/aquatic/lotic_water_body.yaml data/habitats/aquatic/low_tide_zone.yaml
    data/habitats/aquatic/mangrove_area.yaml data/habitats/aquatic/mangrove_sediment.yaml
    data/habitats/aquatic/mangrove_soil.yaml data/habitats/aquatic/mangrove_swamp.yaml
    data/habitats/aquatic/marginal_sea_biome.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success from 2026-10-12T03:37:03.419277Z to 2026-10-12T03:37:12.395795Z.
    Native scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C2
  name: Native gate on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00000316
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=0cdeb733c38557948747ac46dbf98651279f8bd1
    just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success from 2026-10-12T03:37:12.396779Z to 2026-10-12T03:37:31.652184Z.
    Native scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C3
  name: Native gate on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00000316
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=0cdeb733c38557948747ac46dbf98651279f8bd1
    just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success from 2026-10-12T03:37:31.653951Z to 2026-10-12T03:38:23.419150Z.
    Native scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C4
  name: Native gate on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00000316
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=0cdeb733c38557948747ac46dbf98651279f8bd1
    just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success from 2026-10-12T03:38:23.420244Z to 2026-10-12T03:38:32.031101Z.
    Native scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C5
  name: Native gate on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00000316
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=0cdeb733c38557948747ac46dbf98651279f8bd1
    just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success from 2026-10-12T03:38:32.032463Z to 2026-10-12T03:38:37.476375Z.
    Native scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C6
  name: Native gate on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00000316
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=0cdeb733c38557948747ac46dbf98651279f8bd1
    just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success from 2026-10-12T03:38:37.477529Z to 2026-10-12T03:39:03.951019Z.
    Native scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C7
  name: Native gate on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00000316
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=0cdeb733c38557948747ac46dbf98651279f8bd1
    just provenance-check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success from 2026-10-12T03:39:03.953076Z to 2026-10-12T03:39:05.157446Z.
    Native scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C8
  name: Native gate on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00000316
  command: gh run view 38198936724 --repo CultureBotAI/HabitatMech --log
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success from 2026-10-12T03:36:13.751706Z to 2026-10-12T03:36:15.983252Z.
    All three required merge-group workflows passed at the exact captured base; authoritative
    QC passed 886 tests with 3 skipped. Newly saved review bundles require their own
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
  - ENVO:00000316
  command: .venv/bin/python /private/tmp/habitatmech-review-bb-evidence.py
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
  - ENVO:00000316
  summary: Bounded ignored-inclusive searches did not recover the complete original
    assertion inputs. Later exports supply context only.
  evidence_ids:
  - SEARCH
- check_id: IMODULON
  name: Structured expression applicability
  required: false
  status: not_applicable
  target_ids:
  - ENVO:00000316
  summary: Successful dataset inventory was inspected for graphs; no matching claim-specific
    strain/gene or expression-module assertion is present. Generic pathway/stress
    vocabulary alone cannot certify natural habitat occurrence or causation. No component
    hit was asserted, so no summarize call applies.
  evidence_ids:
  - R
  - RULES
evidence:
- evidence_id: R
  kind: record_content
  reference: data/habitats/aquatic/intertidal_zone.yaml
  summary: ENVO:00000316 denotes the region between tidal marks and has the supported
    marine-environmental-zone genus. PREGO supplies 53 TAXON candidates with 25 displayed
    associations. Official IntertidalZone is exact, whereas littoral zone is related
    and coastal zone broad; their ingestion must preserve these scopes.
  accessed_at: '2026-10-12T03:49:08.350315Z'
  support: supports
  locator: Entire captured YAML read, including provenance, parameters, taxa, graphs
    and generated history
- evidence_id: RULES
  kind: record_content
  reference: docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; src/habitatmech/schema/habitatmech.yaml
  summary: Applied exact identity, strict-parent, MIxS-role, source unit/score and
    ITEM lifecycle contracts. STATE is a cellular value, not the process establishing
    it. Evidence is assessed at edge scope.
  accessed_at: '2026-10-12T03:49:08.350315Z'
  support: supports
- evidence_id: RAW
  kind: database
  reference: data/raw; curation/decisions.tsv; curation/term_requests.tsv; curation/gold_parent_exclusions.tsv
  summary: '{"data/raw/ontology_subclass_edges.tsv": [{"data": {"object": "ENVO:01001201",
    "predicate": "rdfs:subClassOf", "subject": "ENVO:00000316"}, "logical_row": 4959}],
    "data/raw/ontology_terms.tsv": [{"data": {"definition": "The area of the foreshore
    and seabed that is exposed to the air at low tide and submerged at high tide,
    i.e., the area between tide marks.", "deprecated": "", "directly_referenced":
    "TRUE", "label": "intertidal zone", "label_only": "FALSE", "ontology": "ENVO",
    "synonyms": "IntertidalZone|coastal zone|littoral zone", "term_id": "ENVO:00000316"},
    "logical_row": 6899}], "data/raw/prego_habitat_taxa.tsv": [{"data": {"channels":
    "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:00000316", "prego_score": "4", "rank": "1", "taxon_id": "NCBITaxon:1040984",
    "taxon_label": "Mesorhizobium sp. WSM1293"}, "logical_row": 4588}, {"data": {"channels":
    "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:00000316", "prego_score": "4", "rank": "2", "taxon_id": "NCBITaxon:1048",
    "taxon_label": "Marichromatium gracile"}, "logical_row": 4589}, {"data": {"channels":
    "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:00000316", "prego_score": "4", "rank": "3", "taxon_id": "NCBITaxon:1120965",
    "taxon_label": "Algoriphagus mannitolivorans DSM 15301"}, "logical_row": 4590},
    {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank": "4", "taxon_id":
    "NCBITaxon:1121014", "taxon_label": "Arenimonas donghaensis DSM 18148 = HO3-R19"},
    "logical_row": 4591}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank":
    "5", "taxon_id": "NCBITaxon:1121403", "taxon_label": "Desulfogranum japonicum
    DSM 18378"}, "logical_row": 4592}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score":
    "4", "rank": "6", "taxon_id": "NCBITaxon:1121416", "taxon_label": "Desulfopila
    aestuarii DSM 18488"}, "logical_row": 4593}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score":
    "4", "rank": "7", "taxon_id": "NCBITaxon:1121938", "taxon_label": "Halobacillus
    kuroshimensis DSM 18393"}, "logical_row": 4594}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score":
    "4", "rank": "8", "taxon_id": "NCBITaxon:1122176", "taxon_label": "Lewinella cohaerens
    DSM 23179"}, "logical_row": 4595}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score":
    "4", "rank": "9", "taxon_id": "NCBITaxon:1122197", "taxon_label": "Marinobacter
    daepoensis DSM 16072"}, "logical_row": 4596}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score":
    "4", "rank": "10", "taxon_id": "NCBITaxon:1122599", "taxon_label": "Neptunomonas
    japonica DSM 18939"}, "logical_row": 4597}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score":
    "4", "rank": "11", "taxon_id": "NCBITaxon:1123000", "taxon_label": "Propionigenium
    maris DSM 9537"}, "logical_row": 4598}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score":
    "4", "rank": "12", "taxon_id": "NCBITaxon:1123503", "taxon_label": "Woodsholea
    maritima DSM 17123"}, "logical_row": 4599}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score":
    "4", "rank": "13", "taxon_id": "NCBITaxon:1123509", "taxon_label": "Zooshikella
    ganghwensis DSM 15267"}, "logical_row": 4600}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score":
    "4", "rank": "14", "taxon_id": "NCBITaxon:1123515", "taxon_label": "Thiomicrorhabdus
    chilensis DSM 12352"}, "logical_row": 4601}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score":
    "4", "rank": "15", "taxon_id": "NCBITaxon:1123517", "taxon_label": "Thiomicrospira
    pelophila DSM 1534"}, "logical_row": 4602}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score":
    "4", "rank": "16", "taxon_id": "NCBITaxon:1278307", "taxon_label": "Psychromonas
    ossibalaenae ATCC BAA-1528"}, "logical_row": 4603}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score":
    "4", "rank": "17", "taxon_id": "NCBITaxon:1397696", "taxon_label": "Exiguobacterium
    marinum DSM 16307"}, "logical_row": 4604}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score":
    "4", "rank": "18", "taxon_id": "NCBITaxon:1408433", "taxon_label": "Crocinitomix
    catalasitica ATCC 23190"}, "logical_row": 4605}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score":
    "4", "rank": "19", "taxon_id": "NCBITaxon:1442586", "taxon_label": "Winogradskyella
    wandonensis"}, "logical_row": 4606}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score":
    "4", "rank": "20", "taxon_id": "NCBITaxon:150", "taxon_label": "Spirochaeta isovalerica"},
    "logical_row": 4607}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank":
    "21", "taxon_id": "NCBITaxon:163908", "taxon_label": "Anabaena sp. PCC 7108"},
    "logical_row": 4608}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank":
    "22", "taxon_id": "NCBITaxon:166318", "taxon_label": "Synechococcus sp. WH 8016"},
    "logical_row": 4609}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score": "4", "rank":
    "23", "taxon_id": "NCBITaxon:203122", "taxon_label": "Saccharophagus degradans
    2-40"}, "logical_row": 4610}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score":
    "4", "rank": "24", "taxon_id": "NCBITaxon:226505", "taxon_label": "Algoriphagus
    halophilus"}, "logical_row": 4611}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00000316", "prego_score":
    "4", "rank": "25", "taxon_id": "NCBITaxon:285258", "taxon_label": "Tenacibaculum
    lutimaris"}, "logical_row": 4612}], "data/raw/prego_habitats.tsv": [{"data": {"biolink_category":
    "biolink:OntologyClass", "channels": "annotated_genomes_isolates", "direct_assertion_count":
    "54", "max_prego_score": "4", "ontology": "ENVO", "prego_id": "ENVO:00000316",
    "prego_synonyms": "intertidal|intertidal zone|intertidalic|intertidals|littoral|littoral
    zone|littoralic|littorals", "taxon_count": "53"}, "logical_row": 220}]}'
  accessed_at: '2026-10-12T03:49:08.350315Z'
  support: supports
  locator: Exact logical TSV rows; header is row1; unrelated neighbor matches excluded
- evidence_id: CODE
  kind: record_content
  reference: src/habitatmech/seed.py
  summary: '{"reviewed_sources": 0, "routes": [{"actual": {"category": null, "contributes_grounding":
    true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status":
    "EXACT", "identifier": "ENVO:00000316", "mapping_predicate": null, "reviewed":
    false, "route": "prego_self_grounded"}, "automatic": {"category": null, "contributes_grounding":
    true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status":
    "EXACT", "identifier": "ENVO:00000316", "mapping_predicate": null, "reviewed":
    false, "route": "prego_self_grounded"}, "minted": "habitatmech:PREGO.1e1d841752",
    "source": "PREGO", "source_id": "ENVO:00000316"}], "source_concepts": 1}'
  accessed_at: '2026-10-12T03:49:08.350315Z'
  support: supports
  locator: Executed complete-document reconstruction; all40 matched captured records
- evidence_id: ONT
  kind: authority
  reference: https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl
  summary: '{"ENVO:00000316": {"definitions": ["The area of the foreshore and seabed
    that is exposed to the air at low tide and submerged at high tide, i.e., the area
    between tide marks."], "deprecated": [], "equivalents": [], "labels": ["intertidal
    zone"], "parents": ["http://purl.obolibrary.org/obo/ENVO_01001201", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty":
    ["http://purl.obolibrary.org/obo/BFO_0000050"], "http://www.w3.org/2002/07/owl#someValuesFrom":
    ["http://purl.obolibrary.org/obo/ENVO_00000304"]}, {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty":
    ["http://purl.obolibrary.org/obo/RO_0002131"], "http://www.w3.org/2002/07/owl#someValuesFrom":
    ["http://purl.obolibrary.org/obo/ENVO_01001468"]}], "replacements": [], "synonyms":
    {"hasBroadSynonym": ["coastal zone"], "hasExactSynonym": ["IntertidalZone"], "hasNarrowSynonym":
    [], "hasRelatedSynonym": ["littoral zone"]}}, "ENVO:01001201": {"definitions":
    ["An astronomical body part which is part of a marine environment."], "deprecated":
    [], "equivalents": [], "labels": ["marine environmental zone"], "parents": ["http://purl.obolibrary.org/obo/ENVO_01000813",
    {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"],
    "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/BFO_0000050"],
    "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_01000320"]}],
    "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": [],
    "hasNarrowSynonym": [], "hasRelatedSynonym": []}}}'
  accessed_at: '2026-10-11T13:21:47.927208Z'
  support: supports
  locator: Official OWL fetched11-Oct; identity, deprecated/replacement metadata,
    typed synonyms and direct axioms; no snapshot refresh
  snapshot_sha256: a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c
- evidence_id: PARENT
  kind: record_content
  reference: data/raw/ontology_terms.tsv
  summary: '{}'
  accessed_at: '2026-10-12T03:49:08.350315Z'
  support: supports
  locator: Ancestor context is not full-record review coverage of ancestors
- evidence_id: TAX0
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=100038%2C1007122%2C1007124%2C1009420%2C1009695%2C1026%2C1027249%2C103%2C1033802%2C1033806%2C1033810%2C1034944%2C1036674%2C103810%2C1040984%2C1041152%2C104176%2C104245%2C1045010%2C1048%2C1048380%2C1048396%2C1058%2C106111%2C1063%2C106370%2C106592%2C1069%2C1069073%2C1069081%2C1069083%2C1071078%2C1071079%2C1074%2C107400%2C107401%2C1076695%2C107820%2C108003%2C1082479%2C1085%2C1087%2C108901%2C108943%2C109263%2C1096246%2C109635%2C110101%2C1101193%2C110933%2C1114856%2C111805%2C1118153%2C1120797%2C1120956%2C1120961%2C1120963%2C1120965%2C1120983%2C1120998%2C1121007%2C1121014%2C1121087%2C1121264%2C1121266%2C1121301%2C1121317%2C1121324%2C1121390%2C1121392%2C1121403%2C1121416%2C1121451%2C1121459%2C1121463%2C1121911%2C1121912%2C1121931%2C1121938%2C1121940%2C1122135%2C1122137%2C1122176%2C1122195%2C1122197%2C1122226%2C112235%2C112248%2C1122599%2C1123000%2C1123053%2C1123251%2C1123270%2C1123325%2C1123349%2C1123350%2C1123371%2C1123380%2C1123503%2C1123509%2C1123515%2C1123517%2C1125975%2C1131812%2C114497%2C114628%2C114707%2C114712%2C114715%2C115553%2C117681%2C1188994%2C120749%2C1214577%2C121845%2C1218948%2C1265%2C126740%2C1270%2C127458%2C127520%2C1278307%2C128%2C1280%2C129817%2C130049%2C13035%2C1303716%2C1334019%2C1341154%2C1358%2C13684%2C137510%2C1380347%2C139239%2C1397696%2C1402%2C1408%2C1408433%2C1409%2C1424653%2C1436140%2C1442586%2C147%2C1478%2C1495045%2C149712%2C150%2C1505%2C152&retmode=xml
  summary: 'The two chunks resolve all252 requested cohort IDs. This target=[{"current_id":
    "1040984", "current_name": "Mesorhizobium sp. WSM1293", "frozen_label": "Mesorhizobium
    sp. WSM1293", "id": "1040984", "rank": "species"}, {"current_id": "1048", "current_name":
    "Marichromatium gracile", "frozen_label": "Marichromatium gracile", "id": "1048",
    "rank": "species"}, {"current_id": "1120965", "current_name": "Algoriphagus mannitolivorans
    DSM 15301", "frozen_label": "Algoriphagus mannitolivorans DSM 15301", "id": "1120965",
    "rank": "strain"}, {"current_id": "1121014", "current_name": "Arenimonas donghaensis
    DSM 18148 = HO3-R19", "frozen_label": "Arenimonas donghaensis DSM 18148 = HO3-R19",
    "id": "1121014", "rank": "strain"}, {"current_id": "1121403", "current_name":
    "Desulfogranum japonicum DSM 18378", "frozen_label": "Desulfogranum japonicum
    DSM 18378", "id": "1121403", "rank": "strain"}, {"current_id": "1121416", "current_name":
    "Desulfopila aestuarii DSM 18488", "frozen_label": "Desulfopila aestuarii DSM
    18488", "id": "1121416", "rank": "strain"}, {"current_id": "1121938", "current_name":
    "Halobacillus kuroshimensis DSM 18393", "frozen_label": "Halobacillus kuroshimensis
    DSM 18393", "id": "1121938", "rank": "strain"}, {"current_id": "1122176", "current_name":
    "Lewinella cohaerens DSM 23179", "frozen_label": "Lewinella cohaerens DSM 23179",
    "id": "1122176", "rank": "strain"}, {"current_id": "1122197", "current_name":
    "Marinobacter daepoensis DSM 16072", "frozen_label": "Marinobacter daepoensis
    DSM 16072", "id": "1122197", "rank": "strain"}, {"current_id": "1122599", "current_name":
    "Neptunomonas japonica DSM 18939", "frozen_label": "Neptunomonas japonica DSM
    18939", "id": "1122599", "rank": "strain"}, {"current_id": "1123000", "current_name":
    "Propionigenium maris DSM 9537", "frozen_label": "Propionigenium maris DSM 9537",
    "id": "1123000", "rank": "strain"}, {"current_id": "1123503", "current_name":
    "Woodsholea maritima DSM 17123", "frozen_label": "Woodsholea maritima DSM 17123",
    "id": "1123503", "rank": "strain"}, {"current_id": "1123509", "current_name":
    "Zooshikella ganghwensis DSM 15267", "frozen_label": "Zooshikella ganghwensis
    DSM 15267", "id": "1123509", "rank": "strain"}, {"current_id": "1123515", "current_name":
    "Thiomicrorhabdus chilensis DSM 12352", "frozen_label": "Thiomicrorhabdus chilensis
    DSM 12352", "id": "1123515", "rank": "strain"}, {"current_id": "1123517", "current_name":
    "Thiomicrospira pelophila DSM 1534", "frozen_label": "Thiomicrospira pelophila
    DSM 1534", "id": "1123517", "rank": "strain"}, {"current_id": "1278307", "current_name":
    "Psychromonas ossibalaenae ATCC BAA-1528", "frozen_label": "Psychromonas ossibalaenae
    ATCC BAA-1528", "id": "1278307", "rank": "strain"}, {"current_id": "1397696",
    "current_name": "Exiguobacterium marinum DSM 16307", "frozen_label": "Exiguobacterium
    marinum DSM 16307", "id": "1397696", "rank": "strain"}, {"current_id": "1408433",
    "current_name": "Crocinitomix catalasitica ATCC 23190", "frozen_label": "Crocinitomix
    catalasitica ATCC 23190", "id": "1408433", "rank": "strain"}, {"current_id": "1442586",
    "current_name": "Winogradskyella wandonensis", "frozen_label": "Winogradskyella
    wandonensis", "id": "1442586", "rank": "species"}, {"current_id": "150", "current_name":
    "Spirochaeta isovalerica", "frozen_label": "Spirochaeta isovalerica", "id": "150",
    "rank": "species"}, {"current_id": "163908", "current_name": "Anabaena sp. PCC
    7108", "frozen_label": "Anabaena sp. PCC 7108", "id": "163908", "rank": "species"},
    {"current_id": "166318", "current_name": "Synechococcus sp. WH 8016", "frozen_label":
    "Synechococcus sp. WH 8016", "id": "166318", "rank": "species"}, {"current_id":
    "203122", "current_name": "Saccharophagus degradans 2-40", "frozen_label": "Saccharophagus
    degradans 2-40", "id": "203122", "rank": "strain"}, {"current_id": "226505", "current_name":
    "Algoriphagus halophilus", "frozen_label": "Algoriphagus halophilus", "id": "226505",
    "rank": "species"}, {"current_id": "285258", "current_name": "Tenacibaculum lutimaris",
    "frozen_label": "Tenacibaculum lutimaris", "id": "285258", "rank": "species"}].
    Frozen labels may be historical aliases; resolution does not establish occurrence.'
  accessed_at: '2026-10-12T03:35:53.303178Z'
  support: supports
  locator: NCBI TaxId, ScientificName, Rank, AkaTaxIds and OtherNames
  snapshot_sha256: 303bd04b2066e24f3cee950081b5f4287c36659b223347ff9c3a5088e7dac099
- evidence_id: TAX1
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1525%2C153026%2C153500%2C1537%2C1537524%2C153911%2C154510%2C1549639%2C155715%2C156%2C158080%2C158751%2C159087%2C161156%2C1639%2C163908%2C166318%2C1684%2C168471%2C172045%2C172371%2C173%2C1732%2C1734049%2C173764%2C1768%2C185294%2C198703%2C202747%2C203122%2C204773%2C205922%2C206665%2C210512%2C213224%2C223786%2C226505%2C230105%2C232721%2C240166%2C240167%2C240169%2C244366%2C259564%2C2663692%2C267990%2C279714%2C2850%2C285091%2C285258%2C285271%2C286698%2C287%2C292%2C292415%2C293%2C300%2C304%2C3055%2C312153%2C313606%2C314229%2C316%2C31910%2C332175%2C358%2C365044%2C371731%2C375286%2C375451%2C398578%2C39947%2C40214%2C405436%2C42256%2C431041%2C441157%2C452638%2C47885%2C48547%2C521674%2C535289%2C548%2C550984%2C562%2C563045%2C572546%2C573060%2C573064%2C59919%2C610380%2C643561%2C645472%2C655438%2C666681%2C679926%2C693972%2C710696%2C74152%2C746360%2C926690%2C935948&retmode=xml
  summary: 'The two chunks resolve all252 requested cohort IDs. This target=[{"current_id":
    "1040984", "current_name": "Mesorhizobium sp. WSM1293", "frozen_label": "Mesorhizobium
    sp. WSM1293", "id": "1040984", "rank": "species"}, {"current_id": "1048", "current_name":
    "Marichromatium gracile", "frozen_label": "Marichromatium gracile", "id": "1048",
    "rank": "species"}, {"current_id": "1120965", "current_name": "Algoriphagus mannitolivorans
    DSM 15301", "frozen_label": "Algoriphagus mannitolivorans DSM 15301", "id": "1120965",
    "rank": "strain"}, {"current_id": "1121014", "current_name": "Arenimonas donghaensis
    DSM 18148 = HO3-R19", "frozen_label": "Arenimonas donghaensis DSM 18148 = HO3-R19",
    "id": "1121014", "rank": "strain"}, {"current_id": "1121403", "current_name":
    "Desulfogranum japonicum DSM 18378", "frozen_label": "Desulfogranum japonicum
    DSM 18378", "id": "1121403", "rank": "strain"}, {"current_id": "1121416", "current_name":
    "Desulfopila aestuarii DSM 18488", "frozen_label": "Desulfopila aestuarii DSM
    18488", "id": "1121416", "rank": "strain"}, {"current_id": "1121938", "current_name":
    "Halobacillus kuroshimensis DSM 18393", "frozen_label": "Halobacillus kuroshimensis
    DSM 18393", "id": "1121938", "rank": "strain"}, {"current_id": "1122176", "current_name":
    "Lewinella cohaerens DSM 23179", "frozen_label": "Lewinella cohaerens DSM 23179",
    "id": "1122176", "rank": "strain"}, {"current_id": "1122197", "current_name":
    "Marinobacter daepoensis DSM 16072", "frozen_label": "Marinobacter daepoensis
    DSM 16072", "id": "1122197", "rank": "strain"}, {"current_id": "1122599", "current_name":
    "Neptunomonas japonica DSM 18939", "frozen_label": "Neptunomonas japonica DSM
    18939", "id": "1122599", "rank": "strain"}, {"current_id": "1123000", "current_name":
    "Propionigenium maris DSM 9537", "frozen_label": "Propionigenium maris DSM 9537",
    "id": "1123000", "rank": "strain"}, {"current_id": "1123503", "current_name":
    "Woodsholea maritima DSM 17123", "frozen_label": "Woodsholea maritima DSM 17123",
    "id": "1123503", "rank": "strain"}, {"current_id": "1123509", "current_name":
    "Zooshikella ganghwensis DSM 15267", "frozen_label": "Zooshikella ganghwensis
    DSM 15267", "id": "1123509", "rank": "strain"}, {"current_id": "1123515", "current_name":
    "Thiomicrorhabdus chilensis DSM 12352", "frozen_label": "Thiomicrorhabdus chilensis
    DSM 12352", "id": "1123515", "rank": "strain"}, {"current_id": "1123517", "current_name":
    "Thiomicrospira pelophila DSM 1534", "frozen_label": "Thiomicrospira pelophila
    DSM 1534", "id": "1123517", "rank": "strain"}, {"current_id": "1278307", "current_name":
    "Psychromonas ossibalaenae ATCC BAA-1528", "frozen_label": "Psychromonas ossibalaenae
    ATCC BAA-1528", "id": "1278307", "rank": "strain"}, {"current_id": "1397696",
    "current_name": "Exiguobacterium marinum DSM 16307", "frozen_label": "Exiguobacterium
    marinum DSM 16307", "id": "1397696", "rank": "strain"}, {"current_id": "1408433",
    "current_name": "Crocinitomix catalasitica ATCC 23190", "frozen_label": "Crocinitomix
    catalasitica ATCC 23190", "id": "1408433", "rank": "strain"}, {"current_id": "1442586",
    "current_name": "Winogradskyella wandonensis", "frozen_label": "Winogradskyella
    wandonensis", "id": "1442586", "rank": "species"}, {"current_id": "150", "current_name":
    "Spirochaeta isovalerica", "frozen_label": "Spirochaeta isovalerica", "id": "150",
    "rank": "species"}, {"current_id": "163908", "current_name": "Anabaena sp. PCC
    7108", "frozen_label": "Anabaena sp. PCC 7108", "id": "163908", "rank": "species"},
    {"current_id": "166318", "current_name": "Synechococcus sp. WH 8016", "frozen_label":
    "Synechococcus sp. WH 8016", "id": "166318", "rank": "species"}, {"current_id":
    "203122", "current_name": "Saccharophagus degradans 2-40", "frozen_label": "Saccharophagus
    degradans 2-40", "id": "203122", "rank": "strain"}, {"current_id": "226505", "current_name":
    "Algoriphagus halophilus", "frozen_label": "Algoriphagus halophilus", "id": "226505",
    "rank": "species"}, {"current_id": "285258", "current_name": "Tenacibaculum lutimaris",
    "frozen_label": "Tenacibaculum lutimaris", "id": "285258", "rank": "species"}].
    Frozen labels may be historical aliases; resolution does not establish occurrence.'
  accessed_at: '2026-10-12T03:35:55.008639Z'
  support: supports
  locator: NCBI TaxId, ScientificName, Rank, AkaTaxIds and OtherNames
  snapshot_sha256: 32f9be6ba0a3c4293275bbcad64427709376c99cf52c494909dbc6f97598d6c5
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
  accessed_at: '2026-10-12T03:49:08.350315Z'
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
  summary: Read-only all-state964-issue title/body census checked for overlaps, including
    shared1249 and1398 and prior vent1239 and hypersaline1243 corrections. Prior issue
    closure is not primary scientific evidence. Comments were not exhaustively crawled.
  accessed_at: '2026-10-12T03:49:08.350315Z'
  support: supports
  locator: GitHub CLI census and relevant issue bodies
assessments:
- assessment_id: IDENTITY
  area: identity
  topic: Exact identity, definition and source intent
  outcome: supported
  summary: ENVO:00000316 denotes the region between tidal marks and has the supported
    marine-environmental-zone genus. PREGO supplies 53 TAXON candidates with 25 displayed
    associations. Official IntertidalZone is exact, whereas littoral zone is related
    and coastal zone broad; their ingestion must preserve these scopes.
  target_ids:
  - ENVO:00000316
  evidence_ids:
  - R
  - RAW
  - ONT
  - PARENT
- assessment_id: HIERARCHY
  area: grounding
  topic: All parent contributions and mapping scope
  outcome: supported
  summary: ENVO:00000316 denotes the region between tidal marks and has the supported
    marine-environmental-zone genus. PREGO supplies 53 TAXON candidates with 25 displayed
    associations. Official IntertidalZone is exact, whereas littoral zone is related
    and coastal zone broad; their ingestion must preserve these scopes. Ontology,
    GOLD path, ambiguous-leaf and authored-genus contributions were distinguished.
  target_ids:
  - ENVO:00000316
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
    contributors. Attestations=[{"source": "PREGO", "source_id": "ENVO:00000316",
    "source_label": "intertidal zone", "assertion_count": 53, "assertion_unit": "TAXON",
    "score": 4.0, "evidence_channels": "annotated_genomes_isolates"}]. Unlike units
    are not summed; omitted direct counts do not imply ecological absence. This review
    does not change native status.'
  target_ids:
  - ENVO:00000316
  evidence_ids:
  - R
  - RAW
  - CODE
  - RULES
- assessment_id: TAXA
  area: evidence
  topic: Association versus characteristic presence
  outcome: supported
  summary: All emitted taxon IDs resolve, including merged identifiers. Historical
    spellings were checked; unresolved row-specific name scope is recorded separately.
    Full reconstruction preserves source pools, ranks, scores and corroborations;
    displayed taxa are selected associations, not exhaustive occurrence evidence.
    No is_characteristic assertion is present. A source score is not a probability
    or habitat abundance.
  target_ids:
  - ENVO:00000316
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
  - ENVO:00000316
  evidence_ids:
  - R
  - RAW
  - RULES
  - SEARCH
findings:
- finding_id: F1
  issue_key: envo-00000316-ontology-synonym-scope
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Non-exact ontology synonyms are promoted to exact
  description: littoral zone is RELATED and coastal zone BROAD; IntertidalZone remains
    EXACT. ENVO:00000316 denotes the region between tidal marks and has the supported
    marine-environmental-zone genus. PREGO supplies 53 TAXON candidates with 25 displayed
    associations. Official IntertidalZone is exact, whereas littoral zone is related
    and coastal zone broad; their ingestion must preserve these scopes.
  target_ids:
  - ENVO:00000316
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
actions:
- action_id: A1
  description: Resolve shared1249 through governed typed-synonym ingestion and consumer
    tests; retain genuine exact names and PREGO related aliases instead of globally
    downgrading all synonyms.
  finding_ids:
  - F1
  target_ids:
  - ENVO:00000316
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
  coverage. Product-label checks retain documented no-adapter skips and accepted exceptions;
  they do not certify scientific identity.
notes:
- Initial immutable observation precedes separately authorized publication and curation;
  this observation itself changes no source record or native status.
- No earlier structured target observation found; legacy reports remain historical
  and are not silently retired.
tags:
- habitatmech
- aquatic
- record-review
- scientific-review
```
