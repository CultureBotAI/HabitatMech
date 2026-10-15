# Record review: brain (BTO:0000142)

- Review: 20261015T165553Z-brain-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T16:29:31Z
- Finished UTC: 2026-10-15T16:55:53Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

BTO brain identity includes vertebrate and comparable invertebrate nervous centers. Forty PREGO TAXON associations and 25 displayed rows reproduce their source. The primary canine genome study and exact sequence metadata distinguish PG14 throat, UF31/UF33 vaginal origins, and UFG1/UFG4 brain origins. Recover the original pair evidence before endorsing brain localization for the first three; do not delete the two positively supported brain isolates or infer biological absence. Unlabeled taxon 12455 resolves to Borna disease virus.

## Scope And Provenance

Full field-by-field scientific review of this one exact target at 50dbf8b388bf32ca58708f7993e83120310f7cea.

Selection: One of the next 24 path-ordered unreviewed targets in an ignored-inclusive 3208-record census. This bundle assesses only this identifier, not a cohort sample.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 50dbf8b388bf32ca58708f7993e83120310f7cea.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0000142 | data/habitats/host_associated/brain.yaml | generated | brain |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0000142 | Completed 2026-10-15T16:33:35Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/brain.yaml |
| validate-strict | passed | True | BTO:0000142 | Completed 2026-10-15T16:35:27Z. uv run python scripts/validate_strict.py data/habitats/host_associated/bovinae_cow_cattle.yaml data/habitats/host_associated/bowens_disease_squamous_cell_carcinoma_in_situ.yaml data/habitats/host_associated/brain.yaml data/habitats/host_associated/brain__7bf4166c.yaml data/habitats/host_associated/brain__803f6884.yaml data/habitats/host_associated/brain__b2bb2ba8.yaml data/habitats/host_associated/brain__e9ca95b7.yaml data/habitats/host_associated/brain__f0593337.yaml data/habitats/host_associated/brain_cell_line.yaml data/habitats/host_associated/brain_stem.yaml data/habitats/host_associated/breast.yaml data/habitats/host_associated/breast_abscess.yaml data/habitats/host_associated/breast_cancer.yaml data/habitats/host_associated/breast_cancer_ductal.yaml data/habitats/host_associated/breast_cancer_lobular.yaml data/habitats/host_associated/breast_cyst.yaml data/habitats/host_associated/breviatea.yaml data/habitats/host_associated/bronchi.yaml data/habitats/host_associated/bronchi__3fb23b44.yaml data/habitats/host_associated/bronchi__c8c64428.yaml data/habitats/host_associated/bronchial_epithelial_cell.yaml data/habitats/host_associated/bronchiole.yaml data/habitats/host_associated/bronchoalveolar_lavage_fluid.yaml data/habitats/host_associated/bronchus.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | BTO:0000142 | Completed 2026-10-15T16:35:39Z. No issues found<br>814 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | BTO:0000142 | Completed 2026-10-15T16:35:39Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | BTO:0000142 | Completed 2026-10-15T16:36:01Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | BTO:0000142 | Completed 2026-10-15T16:36:06Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | BTO:0000142 | Completed 2026-10-15T16:36:35Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | BTO:0000142 | Completed 2026-10-15T16:37:38Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-baseline full QC | passed | True | BTO:0000142 | Verified 2026-10-15T16:29:56Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38764995320 |

## Scientific And Domain Assessments

### Identity, definition, hierarchy and aliases

identity: supported. Targets: BTO:0000142.

BTO brain identity includes vertebrate and comparable invertebrate nervous centers. Forty PREGO TAXON associations and 25 displayed rows reproduce their source. The primary canine genome study and exact sequence metadata distinguish PG14 throat, UF31/UF33 vaginal origins, and UFG1/UFG4 brain origins. Recover the original pair evidence before endorsing brain localization for the first three; do not delete the two positively supported brain isolates or infer biological absence. Unlabeled taxon 12455 resolves to Borna disease virus.

### Frozen counts, units, ranks, channels and scores

quantity: supported. Targets: BTO:0000142.

Every source assertion and displayed taxon was checked against its exact raw row. [{"source": "PREGO", "count": 40, "unit": "TAXON"}]. Side-table biosample/study counts are not added to tree ORGANISM counts. Zero-count omission is not biological absence.

### Scientific support and scope limits

evidence: concern. Targets: BTO:0000142.

BTO brain identity includes vertebrate and comparable invertebrate nervous centers. Forty PREGO TAXON associations and 25 displayed rows reproduce their source. The primary canine genome study and exact sequence metadata distinguish PG14 throat, UF31/UF33 vaginal origins, and UFG1/UFG4 brain origins. Recover the original pair evidence before endorsing brain localization for the first three; do not delete the two positively supported brain isolates or infer biological absence. Unlabeled taxon 12455 resolves to Borna disease virus.

### Status, optional content, triads and mechanisms

completeness: supported. Targets: BTO:0000142.

Actual routes reproduce EXACT/SEEDED. No environmental-parameter, causal-edge, discussion/dataset or is_characteristic=true assertion is present in this target. Optional absence and SEEDED status alone are not defects. Scientific review does not promote native status.

### Native deterministic validation

schema: supported. Targets: BTO:0000142.

Ordinary and strict schemas, 814 history records, provenance, 3208-record reproduction, 32 causal overlays, term-request checks, configured labels and exact-base full QC passed. These establish fidelity, not biological truth.

## Findings

### F1: Original pair evidence is needed for anatomical localization

major / open / provisional; issue key: brain-prego-pair-scope.

BTO brain identity includes vertebrate and comparable invertebrate nervous centers. Forty PREGO TAXON associations and 25 displayed rows reproduce their source. The primary canine genome study and exact sequence metadata distinguish PG14 throat, UF31/UF33 vaginal origins, and UFG1/UFG4 brain origins. Recover the original pair evidence before endorsing brain localization for the first three; do not delete the two positively supported brain isolates or infer biological absence. Unlabeled taxon 12455 resolves to Borna disease virus. Recover manifest-matching citations and distinguish original isolation from experimental exposure or paper co-mention. Correct or qualify only demonstrated mismatches through governed source/extractor handling; do not hand-delete taxa or decrement counts.

## Recommended Actions And Acceptance Checks

### ACT1

BTO brain identity includes vertebrate and comparable invertebrate nervous centers. Forty PREGO TAXON associations and 25 displayed rows reproduce their source. The primary canine genome study and exact sequence metadata distinguish PG14 throat, UF31/UF33 vaginal origins, and UFG1/UFG4 brain origins. Recover the original pair evidence before endorsing brain localization for the first three; do not delete the two positively supported brain isolates or infer biological absence. Unlabeled taxon 12455 resolves to Borna disease virus. Recover manifest-matching citations and distinguish original isolation from experimental exposure or paper co-mention. Correct or qualify only demonstrated mismatches through governed source/extractor handling; do not hand-delete taxa or decrement counts. No repair is performed by this review.

- Regress the exact reported claim and preserve independent identifiers, counts/units and raw provenance. Change identity, native status or mapping only when separately supported by the scoped item assessment; never change source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/brain.yaml; Entire target YAML | supports | Entire record read: identity, definition, parents, source attestations, every displayed taxon and complete history. |
| ERULE | docs/CURATION.md; Host, anatomy, hierarchy, disposition and evidence rules | supports | Parent_habitats means strictly broader; source occurrence does not establish characteristic presence. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; HabitatRecord and SourceAttestation slots | supports | Typed identity, broader habitat and source-to-record mapping semantics; optional fields are not mandatory. |
| ESEED | src/habitatmech/seed.py; Executed build_corpus/apply_decision routes and parent accumulation | supports | Full target equality was verified against actual generated document. Exact source routes: [{"mint": "habitatmech:PREGO.b16b4521f0", "automatic": {"identifier": "BTO:0000142", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "BTO:0000142", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}}] |
| EEXTRACT | src/habitatmech/extract.py; Frozen inventory projection | supports | Source counts and taxon ranks/scores preserve source units; PREGO projections do not retain original pair-level citations. |
| ET5 | data/raw/prego_habitat_taxa.tsv; Physical TSV rows 163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187 | supports | [{"row": 163, "data": {"prego_id": "BTO:0000142", "rank": "1", "taxon_id": "NCBITaxon:12455", "taxon_label": "", "prego_score": "4", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 164, "data": {"prego_id": "BTO:0000142", "rank": "2", "taxon_id": "NCBITaxon:147802", "taxon_label": "Lactobacillus iners", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 165, "data": {"prego_id": "BTO:0000142", "rank": "3", "taxon_id": "NCBITaxon:1578", "taxon_label": "Lactobacillus", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 166, "data": {"prego_id": "BTO:0000142", "rank": "4", "taxon_id": "NCBITaxon:1601", "taxon_label": "Ligilactobacillus agilis", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 167, "data": {"prego_id": "BTO:0000142", "rank": "5", "taxon_id": "NCBITaxon:168808", "taxon_label": "Sneathia", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 168, "data": {"prego_id": "BTO:0000142", "rank": "6", "taxon_id": "NCBITaxon:2701", "taxon_label": "Gardnerella", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 169, "data": {"prego_id": "BTO:0000142", "rank": "7", "taxon_id": "NCBITaxon:82135", "taxon_label": "Fannyhessea vaginae", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 170, "data": {"prego_id": "BTO:0000142", "rank": "8", "taxon_id": "NCBITaxon:838", "taxon_label": "Prevotella", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 171, "data": {"prego_id": "BTO:0000142", "rank": "9", "taxon_id": "NCBITaxon:84107", "taxon_label": "Coriobacteriaceae", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 172, "data": {"prego_id": "BTO:0000142", "rank": "10", "taxon_id": "NCBITaxon:1117644", "taxon_label": "Mycoplasmopsis canis PG 14", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 173, "data": {"prego_id": "BTO:0000142", "rank": "11", "taxon_id": "NCBITaxon:1131452", "taxon_label": "Mycoplasmopsis canis UF31", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 174, "data": {"prego_id": "BTO:0000142", "rank": "12", "taxon_id": "NCBITaxon:1131453", "taxon_label": "Mycoplasmopsis canis UF33", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 175, "data": {"prego_id": "BTO:0000142", "rank": "13", "taxon_id": "NCBITaxon:1131454", "taxon_label": "Mycoplasmopsis canis UFG1", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 176, "data": {"prego_id": "BTO:0000142", "rank": "14", "taxon_id": "NCBITaxon:1131455", "taxon_label": "Mycoplasmopsis canis UFG4", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 177, "data": {"prego_id": "BTO:0000142", "rank": "15", "taxon_id": "NCBITaxon:1133849", "taxon_label": "Nocardia brasiliensis ATCC 700358", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 178, "data": {"prego_id": "BTO:0000142", "rank": "16", "taxon_id": "NCBITaxon:1177117", "taxon_label": "Vreelandella stevensii S18214", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 179, "data": {"prego_id": "BTO:0000142", "rank": "17", "taxon_id": "NCBITaxon:1189613", "taxon_label": "Staphylococcus massiliensis CCUG 55927", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 180, "data": {"prego_id": "BTO:0000142", "rank": "18", "taxon_id": "NCBITaxon:1214102", "taxon_label": "Mycolicibacterium fortuitum subsp. fortuitum DSM 46621 = ATCC 6841 = JCM 6387", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 181, "data": {"prego_id": "BTO:0000142", "rank": "19", "taxon_id": "NCBITaxon:1328", "taxon_label": "Streptococcus anginosus", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 182, "data": {"prego_id": "BTO:0000142", "rank": "20", "taxon_id": "NCBITaxon:1348", "taxon_label": "Streptococcus parauberis", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 183, "data": {"prego_id": "BTO:0000142", "rank": "21", "taxon_id": "NCBITaxon:1392869", "taxon_label": "Escherichia coli K1", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 184, "data": {"prego_id": "BTO:0000142", "rank": "22", "taxon_id": "NCBITaxon:1639", "taxon_label": "Listeria monocytogenes", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 185, "data": {"prego_id": "BTO:0000142", "rank": "23", "taxon_id": "NCBITaxon:1680", "taxon_label": "Bifidobacterium adolescentis", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 186, "data": {"prego_id": "BTO:0000142", "rank": "24", "taxon_id": "NCBITaxon:1683", "taxon_label": "Bifidobacterium angulatum", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 187, "data": {"prego_id": "BTO:0000142", "rank": "25", "taxon_id": "NCBITaxon:169963", "taxon_label": "Listeria monocytogenes EGD-e", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}] |
| ET6 | data/raw/prego_habitats.tsv; Physical TSV rows 239 | supports | [{"row": 239, "data": {"prego_id": "BTO:0000142", "ontology": "BTO", "biolink_category": "biolink:GrossAnatomicalStructure", "taxon_count": "40", "direct_assertion_count": "40", "max_prego_score": "4", "channels": "annotated_genomes_isolates&#124;environmental_samples", "prego_synonyms": "brain&#124;brains&#124;encephalon&#124;encephalonal&#124;encephalons"}}] |
| ET7 | data/raw/isolation_source_groundings.tsv; Physical TSV rows 51 | supports | [{"row": 51, "data": {"subject_label": "Brain", "subject_label_normalized": "brain", "object_id": "UBERON:0000955", "object_label": "brain", "object_source": "UBERON", "predicate_id": "skos:exactMatch", "confidence": "high", "mapping_justification": "semapv:LexicalMatching", "curator": "ols4_auto", "source_dataset": "bacdive", "verified_date": "2026-05-01"}}] |
| ET8 | data/raw/ontology_terms.tsv; Physical TSV rows 144 | supports | [{"row": 144, "data": {"term_id": "BTO:0000142", "ontology": "BTO", "label": "brain", "definition": "1: The portion of the vertebrate central nervous system that constitutes the organ of thought and neural coordination, includes all the higher nervous centers receiving stimuli from the sense organs and interpreting and correlating them to formulate the motor impulses, is made up of neurons and supporting and nutritive structures, is enclosed within the skull, and is continuous with the spinal cord through the foramen magnum. Also named encephalon. 2: A nervous center in invertebrates comparable in position and function to the vertebrate brain.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}] |
| ELEGACY | reports/yaml_record_review/20260922T080023Z-brain.md; Findings and recommended edits; historical lead | supports | Legacy conclusions were compared with current target and primary evidence. No formal predecessor or automatic native-status requirement is inferred. |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000142/graph; BTO_0000142-graph.json | context_only | Typed outgoing ontology relations, not an untyped ancestor list: [{"source": "http://purl.obolibrary.org/obo/BTO_0000142", "target": "http://purl.obolibrary.org/obo/BTO_0000227", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/BTO_0000142", "target": "http://purl.obolibrary.org/obo/BTO_0000282", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000142; BTO_0000142.json | context_only | Current term identity, active status and definition: {"obo_id": "BTO:0000142", "label": "brain", "is_obsolete": false, "description": ["1: The portion of the vertebrate central nervous system that constitutes the organ of thought and neural coordination, includes all the higher nervous centers receiving stimuli from the sense organs and interpreting and correlating them to formulate the motor impulses, is made up of neurons and supporting and nutritive structures, is enclosed within the skull, and is continuous with the spinal cord through the foramen magnum. Also named encephalon. 2: A nervous center in invertebrates comparable in position and function to the vertebrate brain."]} |
| EX3 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3416566/?report=xml; PMC3416566.html | context_only | Primary genome announcement, first paragraph and accession context inspected, DOI:10.1128/JB.00664-12, PMID:22815452. The paragraph assigns PG14 to throat, UF31/UF33 to genital tract and UFG1/UFG4 to brain. Not assumed to be the unrecovered PREGO pair citation. |
| EX4 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4907131/?report=xml; PMC4907131.html | context_only | Primary methods, Mycoplasma strains and cultivation, DOI:10.1128/IAI.01440-15, PMID:27045036: PG14 originated from normal-dog throat; UF31/UF33 from vaginal swabs of dogs without meningoencephalitis; UFG strains from frozen brains of necrotizing meningoencephalitis cases. Laboratory exposures do not change original sampling sites. |
| EX5 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML; PMC8879827.xml | context_only | PREGO methods section 2.3, DOI:10.3390/microorganisms10020293, PMID:35208748: BioProject assigned taxa are associated with entities mined from linked abstracts at confidence three. The channel is not independently verified strain localization or ecological prevalence. |
| EX6 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=419704315&amp;rettype=gb&amp;retmode=xml&amp;seq_start=1&amp;seq_stop=1; nuccore-1117644.xml | context_only | Exact sequence accession NZ_AJFQ00000000.1 source qualifiers: {"organism": "Mycoplasmopsis canis PG 14", "mol_type": "genomic DNA", "strain": "PG 14", "isolation_source": "throat", "host": "Canis lupus familiaris", "culture_collection": "ATCC:19525", "type_material": "type strain of Mycoplasma canis", "db_xref": "taxon:1117644", "geo_loc_name": "United Kingdom: England", "collection_date": "1951", "note": "type strain of Mycoplasma canis"} |
| EX7 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=384938297&amp;rettype=gb&amp;retmode=xml&amp;seq_start=1&amp;seq_stop=1; nuccore-1131452.xml | context_only | Exact sequence accession NZ_AJFR00000000.1 source qualifiers: {"organism": "Mycoplasmopsis canis UF31", "mol_type": "genomic DNA", "strain": "UF31", "isolation_source": "vagina of a dog", "host": "Canis lupus familiaris", "db_xref": "taxon:1131452", "geo_loc_name": "USA: FL", "collection_date": "1992"} |
| EX8 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=419704962&amp;rettype=gb&amp;retmode=xml&amp;seq_start=1&amp;seq_stop=1; nuccore-1131453.xml | context_only | Exact sequence accession NZ_AJFS00000000.1 source qualifiers: {"organism": "Mycoplasmopsis canis UF33", "mol_type": "genomic DNA", "strain": "UF33", "isolation_source": "vagina of a dog", "host": "Canis lupus familiaris", "db_xref": "taxon:1131453", "geo_loc_name": "USA: FL", "collection_date": "1992"} |
| EX9 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=419705607&amp;rettype=gb&amp;retmode=xml&amp;seq_start=1&amp;seq_stop=1; nuccore-1131454.xml | context_only | Exact sequence accession NZ_AJFT00000000.1 source qualifiers: {"organism": "Mycoplasmopsis canis UFG1", "mol_type": "genomic DNA", "strain": "UFG1", "isolation_source": "brain of a dog", "host": "Canis lupus familiaris", "db_xref": "taxon:1131454", "geo_loc_name": "USA: FL", "collection_date": "2009"} |
| EX10 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=419706256&amp;rettype=gb&amp;retmode=xml&amp;seq_start=1&amp;seq_stop=1; nuccore-1131455.xml | context_only | Exact sequence accession NZ_AJFU00000000.1 source qualifiers: {"organism": "Mycoplasmopsis canis UFG4", "mol_type": "genomic DNA", "strain": "UFG4", "isolation_source": "brain of a dog", "host": "Canis lupus familiaris", "db_xref": "taxon:1131455", "geo_loc_name": "USA: FL", "collection_date": "2009"} |
| EX11 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1117644,1122164,1131452,1131453,1131454,1131455,1133849,1141647,1157946,1162284,1162288,1177117,1189613,1193128,1199187,1206729,1214102,1220554,1226751,12455,1271862,1328,1329,1329902,1334,1348,1392869,147802,153721,1578,1590,1601,161879,1639,1658,1661,1679,1680,1682,1683,168808,169963,1718,1724,1796,1802,1817,184914,1886,1962118,197,198,2,205913,206,2074,2081794,222805,238,2701,28026,28087,286804,287,32002,32020,33,341199,36808,391904,439842,476,47885,480035,484020,51665,524884,653940,678,720,72407,731,747,756689,76759,82135,82348,83655,838,84107,912594,985762&amp;retmode=xml; taxonomy.xml | context_only | All displayed IDs resolve in current NCBI Taxonomy. Preferred names and source labels were compared, without treating recognized historical aliases as wrong identities: [{"id": "NCBITaxon:12455", "source": "PREGO", "label": null, "current_id": "12455", "current_name": "Borna disease virus", "rank": "species", "direct_match": false, "recognized_alias": false}, {"id": "NCBITaxon:147802", "source": "PREGO", "label": "Lactobacillus iners", "current_id": "147802", "current_name": "Lactobacillus iners", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1578", "source": "PREGO", "label": "Lactobacillus", "current_id": "1578", "current_name": "Lactobacillus", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1601", "source": "PREGO", "label": "Ligilactobacillus agilis", "current_id": "1601", "current_name": "Ligilactobacillus agilis", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:168808", "source": "PREGO", "label": "Sneathia", "current_id": "168808", "current_name": "Sneathia", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:2701", "source": "PREGO", "label": "Gardnerella", "current_id": "2701", "current_name": "Gardnerella", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:82135", "source": "PREGO", "label": "Fannyhessea vaginae", "current_id": "82135", "current_name": "Fannyhessea vaginae", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:838", "source": "PREGO", "label": "Prevotella", "current_id": "838", "current_name": "Prevotella", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:84107", "source": "PREGO", "label": "Coriobacteriaceae", "current_id": "84107", "current_name": "Coriobacteriaceae", "rank": "family", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1117644", "source": "PREGO", "label": "Mycoplasmopsis canis PG 14", "current_id": "1117644", "current_name": "Mycoplasmopsis canis PG 14", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1131452", "source": "PREGO", "label": "Mycoplasmopsis canis UF31", "current_id": "1131452", "current_name": "Mycoplasmopsis canis UF31", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1131453", "source": "PREGO", "label": "Mycoplasmopsis canis UF33", "current_id": "1131453", "current_name": "Mycoplasmopsis canis UF33", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1131454", "source": "PREGO", "label": "Mycoplasmopsis canis UFG1", "current_id": "1131454", "current_name": "Mycoplasmopsis canis UFG1", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1131455", "source": "PREGO", "label": "Mycoplasmopsis canis UFG4", "current_id": "1131455", "current_name": "Mycoplasmopsis canis UFG4", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1133849", "source": "PREGO", "label": "Nocardia brasiliensis ATCC 700358", "current_id": "1133849", "current_name": "Nocardia brasiliensis ATCC 700358", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1177117", "source": "PREGO", "label": "Vreelandella stevensii S18214", "current_id": "1177117", "current_name": "Vreelandella stevensii S18214", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1189613", "source": "PREGO", "label": "Staphylococcus massiliensis CCUG 55927", "current_id": "1189613", "current_name": "Staphylococcus massiliensis CCUG 55927", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1214102", "source": "PREGO", "label": "Mycolicibacterium fortuitum subsp. fortuitum DSM 46621 = ATCC 6841 = JCM 6387", "current_id": "1214102", "current_name": "Mycolicibacterium fortuitum subsp. fortuitum DSM 46621 = ATCC 6841 = JCM 6387", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1328", "source": "PREGO", "label": "Streptococcus anginosus", "current_id": "1328", "current_name": "Streptococcus anginosus", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1348", "source": "PREGO", "label": "Streptococcus parauberis", "current_id": "1348", "current_name": "Streptococcus parauberis", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1392869", "source": "PREGO", "label": "Escherichia coli K1", "current_id": "1392869", "current_name": "Escherichia coli K1", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1639", "source": "PREGO", "label": "Listeria monocytogenes", "current_id": "1639", "current_name": "Listeria monocytogenes", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1680", "source": "PREGO", "label": "Bifidobacterium adolescentis", "current_id": "1680", "current_name": "Bifidobacterium adolescentis", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1683", "source": "PREGO", "label": "Bifidobacterium angulatum", "current_id": "1683", "current_name": "Bifidobacterium angulatum", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:169963", "source": "PREGO", "label": "Listeria monocytogenes EGD-e", "current_id": "169963", "current_name": "Listeria monocytogenes EGD-e", "rank": "strain", "direct_match": true, "recognized_alias": true}] |
| ESEARCH | Local maintained inputs and structured archive; rg --no-ignore --hidden -l -F -e BTO:0000142 -e brain -e brain -e habitatmech:PREGO.b16b4521f0 curation history research reports data/raw build reviews | context_only | Exact source/curation rows were parsed separately from broad textual matches. No previous structured target observation was found; not every broad label match was inspected. |
| EAVAIL | Configured kg-microbe checkout; find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe -type f -path '*/prego/*' -name '*.tsv' | context_only | No prego-directory TSVs found within this checkout. Original pair citations could not be inspected; this is not a global absence claim. |

## Limits And Additional Notes

- Historical specimens and every original association have not been independently reidentified. Counts, scores and ranked rows are not prevalence, viability, characteristic presence or mechanism.
- The label gate skips 2061 no-adapter pairs and does not certify taxon labels. Every displayed taxon ID was separately resolved through current NCBI Taxonomy.
- Full QC evidence is a successful remote run at the exact unchanged input baseline, not a new local full-QC execution. These new review bundles require their native post-save archive check.
- iModulonDB is not applicable: no gene, regulator, transcriptomic module or causal mechanism is asserted. No paid research was used.
- Original PREGO pair exports are unavailable in the configured checkout. Inspected primary publications and sequence qualifiers cannot reconstruct every pair or establish the cause of extraction errors.
- Input hashes match both current working bytes and exact tracked base blobs; source.state git_commit describes that historical revision without silently refreshing inputs.
- Ignored-inclusive searches and parsed structured archive found no previous structured observation targeting this exact identifier. Legacy findings were inspected as leads, not adopted automatically or assigned false structured lineage.
- Review-only: no habitat curation, regeneration, status promotion, history mutation or GitHub mutation is performed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T165553Z-brain-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: brain (BTO:0000142)'
started_at: '2026-10-15T16:29:31Z'
finished_at: '2026-10-15T16:55:53Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent assesses the target and evidence; not independent
    reviewer approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: BTO brain identity includes vertebrate and comparable invertebrate nervous
  centers. Forty PREGO TAXON associations and 25 displayed rows reproduce their source.
  The primary canine genome study and exact sequence metadata distinguish PG14 throat,
  UF31/UF33 vaginal origins, and UFG1/UFG4 brain origins. Recover the original pair
  evidence before endorsing brain localization for the first three; do not delete
  the two positively supported brain isolates or infer biological absence. Unlabeled
  taxon 12455 resolves to Borna disease virus.
source:
  git_revision: 50dbf8b388bf32ca58708f7993e83120310f7cea
  state: git_commit
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
    sha256: b01c55614780f2eba62e1dc7b47f30d40fb783fe388e75761ca2639769b9c5de
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 6d5cbfd0f5ad911fbb074ee8ec253625d1fa13d94117759b1f25a1cd2e6576bc
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 903fc125adcd84df9fa99a4fae71b30d4a3541efc48eeff3cd49b94e866a5056
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: a56f07a45fb743fb7b0e61f83ef70fa5ed61a3c892cfaf36e3428967c548dc5e
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: dfde49f64273cb94b4162170a5542c94880fa36015ccaac6edfa248820492a23
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: b0135af0aa4deed0f3824a2f491d5a742c1b7de4775c533f283761d22e805821
    role: context
  - path: data/habitats/RETIRED.tsv
    sha256: a2a0496837ea75e487d7fc5d35317a890262a941d8fffe9babcd39f2f332c6db
    role: context
  - path: data/habitats/host_associated/brain.yaml
    sha256: 3ea25ba8dffadcea004046b2fc05043df90853829b5c3f6c85ab63685d320539
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
    sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
    role: context
  - path: docs/HARMONIZATION.md
    sha256: ee39d3cd29115ee14f5e7386169c76c47d471ebdc2502c008c49d30fb44918f1
    role: context
  - path: docs/RESEARCH.md
    sha256: 82c5471890d310bf8fd33141d5596f847bfc1eb6091c2db6f485388435e067af
    role: context
  - path: docs/record-review-profile.md
    sha256: 105b3c8e10f43ce689b05d3089d3a8be1d713a98dd6806e11be37ebd85b10590
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260922T080023Z-brain.md
    sha256: de38c5ce31447183a1052ebe06d6056de2657845936998c6927683ac4fa70124
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/habitatmech/curate/__init__.py
    sha256: d9837c29dc61d8c9245fdb471a68a109cea31b131cdbc0c4d51d23a8d013ce12
    role: context
  - path: src/habitatmech/curate/causal_graphs.py
    sha256: d1884374263ed7926292c52a58742c614e75628d78ff50fe688e6abc0ddf9c1c
    role: context
  - path: src/habitatmech/curate/curation_event.py
    sha256: 08c774d309fe988c468097518d346f07a653b283cb9b9b51c7fe79fa0af785a9
    role: context
  - path: src/habitatmech/curate/decisions.py
    sha256: f33d3e9dc95bb428e63e640d48d4074cf15e90ea666603fb16fb651d591e3f02
    role: context
  - path: src/habitatmech/curate/definition_source_label_exclusions.py
    sha256: 0c13e83fe17613e8b9f5b346d1259104172f8c1de42f911625579b903707625d
    role: context
  - path: src/habitatmech/curate/definitions.py
    sha256: decd02eea029e884ab1a8bbb51dd870edb5544906b3ddd39598147b27ce572c9
    role: context
  - path: src/habitatmech/curate/external_xrefs.py
    sha256: 8b90ec049887d3aa67e31cce7f7a04d7300421c6fedb833cc66e5d5f5f181694
    role: context
  - path: src/habitatmech/curate/gold_parent_exclusions.py
    sha256: 044d8277509a9b1f6e4f2d7ea1fb82319b41e09ffef7788738a0f4ed0d0b63af
    role: context
  - path: src/habitatmech/curate/record_annotation_corrections.py
    sha256: 15bad3d40fd95e2acc72d3ff3c74289c15fb8a1775adc523b3575c3ea8487033
    role: context
  - path: src/habitatmech/labels.py
    sha256: eb6986c3a9c7d5a3e4651b639351f1f2d3e12d74c4bfaa92899205a1f9df0977
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
    sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
    role: context
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
    role: context
targets:
- target_id: BTO:0000142
  path: data/habitats/host_associated/brain.yaml
  label: brain
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
scope:
  description: Full field-by-field scientific review of this one exact target at 50dbf8b388bf32ca58708f7993e83120310f7cea.
  selection: One of the next 24 path-ordered unreviewed targets in an ignored-inclusive
    3208-record census. This bundle assesses only this identifier, not a cohort sample.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - BTO:0000142
  exclusions:
  - target: Other records and SSSOM/KGX products
    reason: Parent context is not additional coverage. Export compatibility and original
      individual source specimens are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/brain.yaml
  exit_code: 0
  target_ids:
  - BTO:0000142
  summary: "Completed 2026-10-15T16:33:35Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/brain.yaml"
  scope_note: Ordinary schema for this target; strict for all 24 selected targets;
    remaining checks use documented full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/bovinae_cow_cattle.yaml data/habitats/host_associated/bowens_disease_squamous_cell_carcinoma_in_situ.yaml
    data/habitats/host_associated/brain.yaml data/habitats/host_associated/brain__7bf4166c.yaml
    data/habitats/host_associated/brain__803f6884.yaml data/habitats/host_associated/brain__b2bb2ba8.yaml
    data/habitats/host_associated/brain__e9ca95b7.yaml data/habitats/host_associated/brain__f0593337.yaml
    data/habitats/host_associated/brain_cell_line.yaml data/habitats/host_associated/brain_stem.yaml
    data/habitats/host_associated/breast.yaml data/habitats/host_associated/breast_abscess.yaml
    data/habitats/host_associated/breast_cancer.yaml data/habitats/host_associated/breast_cancer_ductal.yaml
    data/habitats/host_associated/breast_cancer_lobular.yaml data/habitats/host_associated/breast_cyst.yaml
    data/habitats/host_associated/breviatea.yaml data/habitats/host_associated/bronchi.yaml
    data/habitats/host_associated/bronchi__3fb23b44.yaml data/habitats/host_associated/bronchi__c8c64428.yaml
    data/habitats/host_associated/bronchial_epithelial_cell.yaml data/habitats/host_associated/bronchiole.yaml
    data/habitats/host_associated/bronchoalveolar_lavage_fluid.yaml data/habitats/host_associated/bronchus.yaml
  exit_code: 0
  target_ids:
  - BTO:0000142
  summary: "Completed 2026-10-15T16:35:27Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/bovinae_cow_cattle.yaml data/habitats/host_associated/bowens_disease_squamous_cell_carcinoma_in_situ.yaml\
    \ data/habitats/host_associated/brain.yaml data/habitats/host_associated/brain__7bf4166c.yaml\
    \ data/habitats/host_associated/brain__803f6884.yaml data/habitats/host_associated/brain__b2bb2ba8.yaml\
    \ data/habitats/host_associated/brain__e9ca95b7.yaml data/habitats/host_associated/brain__f0593337.yaml\
    \ data/habitats/host_associated/brain_cell_line.yaml data/habitats/host_associated/brain_stem.yaml\
    \ data/habitats/host_associated/breast.yaml data/habitats/host_associated/breast_abscess.yaml\
    \ data/habitats/host_associated/breast_cancer.yaml data/habitats/host_associated/breast_cancer_ductal.yaml\
    \ data/habitats/host_associated/breast_cancer_lobular.yaml data/habitats/host_associated/breast_cyst.yaml\
    \ data/habitats/host_associated/breviatea.yaml data/habitats/host_associated/bronchi.yaml\
    \ data/habitats/host_associated/bronchi__3fb23b44.yaml data/habitats/host_associated/bronchi__c8c64428.yaml\
    \ data/habitats/host_associated/bronchial_epithelial_cell.yaml data/habitats/host_associated/bronchiole.yaml\
    \ data/habitats/host_associated/bronchoalveolar_lavage_fluid.yaml data/habitats/host_associated/bronchus.yaml\n\
    Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      24\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Ordinary schema for this target; strict for all 24 selected targets;
    remaining checks use documented full-corpus scope.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - BTO:0000142
  summary: 'Completed 2026-10-15T16:35:39Z. No issues found

    814 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Ordinary schema for this target; strict for all 24 selected targets;
    remaining checks use documented full-corpus scope.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - BTO:0000142
  summary: "Completed 2026-10-15T16:35:39Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Ordinary schema for this target; strict for all 24 selected targets;
    remaining checks use documented full-corpus scope.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - BTO:0000142
  summary: "Completed 2026-10-15T16:36:01Z. expected 3208 records, found 3208 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Ordinary schema for this target; strict for all 24 selected targets;
    remaining checks use documented full-corpus scope.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - BTO:0000142
  summary: "Completed 2026-10-15T16:36:06Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Ordinary schema for this target; strict for all 24 selected targets;
    remaining checks use documented full-corpus scope.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - BTO:0000142
  summary: "Completed 2026-10-15T16:36:35Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Ordinary schema for this target; strict for all 24 selected targets;
    remaining checks use documented full-corpus scope.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - BTO:0000142
  summary: "Completed 2026-10-15T16:37:38Z. id↔label correspondence summary:\n   \
    \       OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Ordinary schema for this target; strict for all 24 selected targets;
    remaining checks use documented full-corpus scope.
- check_id: CCI
  name: Exact-baseline full QC
  status: passed
  required: true
  command: gh run view 38764995320 --json status,conclusion,headSha,url,jobs
  exit_code: 0
  target_ids:
  - BTO:0000142
  summary: Verified 2026-10-15T16:29:56Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38764995320
  scope_note: Exact unchanged scientific input baseline; new review files are outside
    that remote run.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/brain.yaml
  locator: Entire target YAML
  accessed_at: '2026-10-15T16:55:52Z'
  support: supports
  summary: 'Entire record read: identity, definition, parents, source attestations,
    every displayed taxon and complete history.'
  snapshot_sha256: 3ea25ba8dffadcea004046b2fc05043df90853829b5c3f6c85ab63685d320539
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host, anatomy, hierarchy, disposition and evidence rules
  accessed_at: '2026-10-15T16:55:52Z'
  support: supports
  summary: Parent_habitats means strictly broader; source occurrence does not establish
    characteristic presence.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: HabitatRecord and SourceAttestation slots
  accessed_at: '2026-10-15T16:55:52Z'
  support: supports
  summary: Typed identity, broader habitat and source-to-record mapping semantics;
    optional fields are not mandatory.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed build_corpus/apply_decision routes and parent accumulation
  accessed_at: '2026-10-15T16:55:52Z'
  support: supports
  summary: 'Full target equality was verified against actual generated document. Exact
    source routes: [{"mint": "habitatmech:PREGO.b16b4521f0", "automatic": {"identifier":
    "BTO:0000142", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded",
    "category": null, "reviewed": false, "decision": null}, "final": {"identifier":
    "BTO:0000142", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded",
    "category": null, "reviewed": false, "decision": null}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: Frozen inventory projection
  accessed_at: '2026-10-15T16:55:52Z'
  support: supports
  summary: Source counts and taxon ranks/scores preserve source units; PREGO projections
    do not retain original pair-level citations.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/prego_habitat_taxa.tsv
  locator: Physical TSV rows 163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187
  accessed_at: '2026-10-15T16:55:52Z'
  support: supports
  summary: '[{"row": 163, "data": {"prego_id": "BTO:0000142", "rank": "1", "taxon_id":
    "NCBITaxon:12455", "taxon_label": "", "prego_score": "4", "direct_flag": "TRUE",
    "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 164,
    "data": {"prego_id": "BTO:0000142", "rank": "2", "taxon_id": "NCBITaxon:147802",
    "taxon_label": "Lactobacillus iners", "prego_score": "4", "direct_flag": "TRUE",
    "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 165, "data":
    {"prego_id": "BTO:0000142", "rank": "3", "taxon_id": "NCBITaxon:1578", "taxon_label":
    "Lactobacillus", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples",
    "corroborated_by": ""}}, {"row": 166, "data": {"prego_id": "BTO:0000142", "rank":
    "4", "taxon_id": "NCBITaxon:1601", "taxon_label": "Ligilactobacillus agilis",
    "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples",
    "corroborated_by": ""}}, {"row": 167, "data": {"prego_id": "BTO:0000142", "rank":
    "5", "taxon_id": "NCBITaxon:168808", "taxon_label": "Sneathia", "prego_score":
    "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}, {"row": 168, "data": {"prego_id": "BTO:0000142", "rank": "6", "taxon_id":
    "NCBITaxon:2701", "taxon_label": "Gardnerella", "prego_score": "4", "direct_flag":
    "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row":
    169, "data": {"prego_id": "BTO:0000142", "rank": "7", "taxon_id": "NCBITaxon:82135",
    "taxon_label": "Fannyhessea vaginae", "prego_score": "4", "direct_flag": "TRUE",
    "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 170, "data":
    {"prego_id": "BTO:0000142", "rank": "8", "taxon_id": "NCBITaxon:838", "taxon_label":
    "Prevotella", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples",
    "corroborated_by": ""}}, {"row": 171, "data": {"prego_id": "BTO:0000142", "rank":
    "9", "taxon_id": "NCBITaxon:84107", "taxon_label": "Coriobacteriaceae", "prego_score":
    "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}, {"row": 172, "data": {"prego_id": "BTO:0000142", "rank": "10", "taxon_id":
    "NCBITaxon:1117644", "taxon_label": "Mycoplasmopsis canis PG 14", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 173, "data": {"prego_id": "BTO:0000142", "rank": "11", "taxon_id":
    "NCBITaxon:1131452", "taxon_label": "Mycoplasmopsis canis UF31", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 174, "data": {"prego_id": "BTO:0000142", "rank": "12", "taxon_id":
    "NCBITaxon:1131453", "taxon_label": "Mycoplasmopsis canis UF33", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 175, "data": {"prego_id": "BTO:0000142", "rank": "13", "taxon_id":
    "NCBITaxon:1131454", "taxon_label": "Mycoplasmopsis canis UFG1", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 176, "data": {"prego_id": "BTO:0000142", "rank": "14", "taxon_id":
    "NCBITaxon:1131455", "taxon_label": "Mycoplasmopsis canis UFG4", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 177, "data": {"prego_id": "BTO:0000142", "rank": "15", "taxon_id":
    "NCBITaxon:1133849", "taxon_label": "Nocardia brasiliensis ATCC 700358", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 178, "data": {"prego_id": "BTO:0000142", "rank": "16", "taxon_id":
    "NCBITaxon:1177117", "taxon_label": "Vreelandella stevensii S18214", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 179, "data": {"prego_id": "BTO:0000142", "rank": "17", "taxon_id":
    "NCBITaxon:1189613", "taxon_label": "Staphylococcus massiliensis CCUG 55927",
    "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates",
    "corroborated_by": ""}}, {"row": 180, "data": {"prego_id": "BTO:0000142", "rank":
    "18", "taxon_id": "NCBITaxon:1214102", "taxon_label": "Mycolicibacterium fortuitum
    subsp. fortuitum DSM 46621 = ATCC 6841 = JCM 6387", "prego_score": "3", "direct_flag":
    "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row":
    181, "data": {"prego_id": "BTO:0000142", "rank": "19", "taxon_id": "NCBITaxon:1328",
    "taxon_label": "Streptococcus anginosus", "prego_score": "3", "direct_flag": "TRUE",
    "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 182,
    "data": {"prego_id": "BTO:0000142", "rank": "20", "taxon_id": "NCBITaxon:1348",
    "taxon_label": "Streptococcus parauberis", "prego_score": "3", "direct_flag":
    "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row":
    183, "data": {"prego_id": "BTO:0000142", "rank": "21", "taxon_id": "NCBITaxon:1392869",
    "taxon_label": "Escherichia coli K1", "prego_score": "3", "direct_flag": "TRUE",
    "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 184,
    "data": {"prego_id": "BTO:0000142", "rank": "22", "taxon_id": "NCBITaxon:1639",
    "taxon_label": "Listeria monocytogenes", "prego_score": "3", "direct_flag": "TRUE",
    "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 185,
    "data": {"prego_id": "BTO:0000142", "rank": "23", "taxon_id": "NCBITaxon:1680",
    "taxon_label": "Bifidobacterium adolescentis", "prego_score": "3", "direct_flag":
    "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row":
    186, "data": {"prego_id": "BTO:0000142", "rank": "24", "taxon_id": "NCBITaxon:1683",
    "taxon_label": "Bifidobacterium angulatum", "prego_score": "3", "direct_flag":
    "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row":
    187, "data": {"prego_id": "BTO:0000142", "rank": "25", "taxon_id": "NCBITaxon:169963",
    "taxon_label": "Listeria monocytogenes EGD-e", "prego_score": "3", "direct_flag":
    "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}]'
  snapshot_sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
- evidence_id: ET6
  kind: database
  reference: data/raw/prego_habitats.tsv
  locator: Physical TSV rows 239
  accessed_at: '2026-10-15T16:55:52Z'
  support: supports
  summary: '[{"row": 239, "data": {"prego_id": "BTO:0000142", "ontology": "BTO", "biolink_category":
    "biolink:GrossAnatomicalStructure", "taxon_count": "40", "direct_assertion_count":
    "40", "max_prego_score": "4", "channels": "annotated_genomes_isolates|environmental_samples",
    "prego_synonyms": "brain|brains|encephalon|encephalonal|encephalons"}}]'
  snapshot_sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
- evidence_id: ET7
  kind: database
  reference: data/raw/isolation_source_groundings.tsv
  locator: Physical TSV rows 51
  accessed_at: '2026-10-15T16:55:52Z'
  support: supports
  summary: '[{"row": 51, "data": {"subject_label": "Brain", "subject_label_normalized":
    "brain", "object_id": "UBERON:0000955", "object_label": "brain", "object_source":
    "UBERON", "predicate_id": "skos:exactMatch", "confidence": "high", "mapping_justification":
    "semapv:LexicalMatching", "curator": "ols4_auto", "source_dataset": "bacdive",
    "verified_date": "2026-05-01"}}]'
  snapshot_sha256: ab6a997359aab961c40928f9b13e06adb6dc43124fa3de821819570dd87f43b8
- evidence_id: ET8
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 144
  accessed_at: '2026-10-15T16:55:52Z'
  support: supports
  summary: '[{"row": 144, "data": {"term_id": "BTO:0000142", "ontology": "BTO", "label":
    "brain", "definition": "1: The portion of the vertebrate central nervous system
    that constitutes the organ of thought and neural coordination, includes all the
    higher nervous centers receiving stimuli from the sense organs and interpreting
    and correlating them to formulate the motor impulses, is made up of neurons and
    supporting and nutritive structures, is enclosed within the skull, and is continuous
    with the spinal cord through the foramen magnum. Also named encephalon. 2: A nervous
    center in invertebrates comparable in position and function to the vertebrate
    brain.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only":
    "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: ELEGACY
  kind: record_content
  reference: reports/yaml_record_review/20260922T080023Z-brain.md
  locator: Findings and recommended edits; historical lead
  accessed_at: '2026-10-15T16:55:52Z'
  support: supports
  summary: Legacy conclusions were compared with current target and primary evidence.
    No formal predecessor or automatic native-status requirement is inferred.
  snapshot_sha256: de38c5ce31447183a1052ebe06d6056de2657845936998c6927683ac4fa70124
- evidence_id: EX1
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000142/graph
  locator: BTO_0000142-graph.json
  accessed_at: '2026-10-15T16:34:05Z'
  support: context_only
  summary: 'Typed outgoing ontology relations, not an untyped ancestor list: [{"source":
    "http://purl.obolibrary.org/obo/BTO_0000142", "target": "http://purl.obolibrary.org/obo/BTO_0000227",
    "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source":
    "http://purl.obolibrary.org/obo/BTO_0000142", "target": "http://purl.obolibrary.org/obo/BTO_0000282",
    "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}]'
  snapshot_sha256: 073e9aa6ee245e8c72f0921bd2a78ff6292e2bee59374f38136effa4b6806aa5
- evidence_id: EX2
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000142
  locator: BTO_0000142.json
  accessed_at: '2026-10-15T16:34:04Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "BTO:0000142",
    "label": "brain", "is_obsolete": false, "description": ["1: The portion of the
    vertebrate central nervous system that constitutes the organ of thought and neural
    coordination, includes all the higher nervous centers receiving stimuli from the
    sense organs and interpreting and correlating them to formulate the motor impulses,
    is made up of neurons and supporting and nutritive structures, is enclosed within
    the skull, and is continuous with the spinal cord through the foramen magnum.
    Also named encephalon. 2: A nervous center in invertebrates comparable in position
    and function to the vertebrate brain."]}'
  snapshot_sha256: a2a22da2dc24e1aaed55d855c982ec9e70a2aa5906c37889dd54d372355c7f46
- evidence_id: EX3
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3416566/?report=xml
  locator: PMC3416566.html
  accessed_at: '2026-10-15T16:47:03Z'
  support: context_only
  summary: Primary genome announcement, first paragraph and accession context inspected,
    DOI:10.1128/JB.00664-12, PMID:22815452. The paragraph assigns PG14 to throat,
    UF31/UF33 to genital tract and UFG1/UFG4 to brain. Not assumed to be the unrecovered
    PREGO pair citation.
  snapshot_sha256: 4fa0951072cda487b35d7b97dbd7dbdff6b865f3b846d175d1a268deaea442c7
- evidence_id: EX4
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4907131/?report=xml
  locator: PMC4907131.html
  accessed_at: '2026-10-15T16:47:03Z'
  support: context_only
  summary: 'Primary methods, Mycoplasma strains and cultivation, DOI:10.1128/IAI.01440-15,
    PMID:27045036: PG14 originated from normal-dog throat; UF31/UF33 from vaginal
    swabs of dogs without meningoencephalitis; UFG strains from frozen brains of necrotizing
    meningoencephalitis cases. Laboratory exposures do not change original sampling
    sites.'
  snapshot_sha256: 5c01b95fb494bb4178024fe67742cbe27a622d7d828f4534274988ba17328a5c
- evidence_id: EX5
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML
  locator: PMC8879827.xml
  accessed_at: '2026-10-15T16:44:01Z'
  support: context_only
  summary: 'PREGO methods section 2.3, DOI:10.3390/microorganisms10020293, PMID:35208748:
    BioProject assigned taxa are associated with entities mined from linked abstracts
    at confidence three. The channel is not independently verified strain localization
    or ecological prevalence.'
  snapshot_sha256: 375f0fde4d07bb823cb9106aa4567bc0ef03c2866af0b2a7740b543f50687c25
- evidence_id: EX6
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=419704315&rettype=gb&retmode=xml&seq_start=1&seq_stop=1
  locator: nuccore-1117644.xml
  accessed_at: '2026-10-15T16:47:03Z'
  support: context_only
  summary: 'Exact sequence accession NZ_AJFQ00000000.1 source qualifiers: {"organism":
    "Mycoplasmopsis canis PG 14", "mol_type": "genomic DNA", "strain": "PG 14", "isolation_source":
    "throat", "host": "Canis lupus familiaris", "culture_collection": "ATCC:19525",
    "type_material": "type strain of Mycoplasma canis", "db_xref": "taxon:1117644",
    "geo_loc_name": "United Kingdom: England", "collection_date": "1951", "note":
    "type strain of Mycoplasma canis"}'
  snapshot_sha256: c136a052560e45c9cc3d98981dc146342b4691f1ae499a01fabc5f505db38201
- evidence_id: EX7
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=384938297&rettype=gb&retmode=xml&seq_start=1&seq_stop=1
  locator: nuccore-1131452.xml
  accessed_at: '2026-10-15T16:48:01Z'
  support: context_only
  summary: 'Exact sequence accession NZ_AJFR00000000.1 source qualifiers: {"organism":
    "Mycoplasmopsis canis UF31", "mol_type": "genomic DNA", "strain": "UF31", "isolation_source":
    "vagina of a dog", "host": "Canis lupus familiaris", "db_xref": "taxon:1131452",
    "geo_loc_name": "USA: FL", "collection_date": "1992"}'
  snapshot_sha256: fd39b8f02bab21da864bb973f1d0ab73622ac2d8cfb4e7f25f2f6ab63cbd88c0
- evidence_id: EX8
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=419704962&rettype=gb&retmode=xml&seq_start=1&seq_stop=1
  locator: nuccore-1131453.xml
  accessed_at: '2026-10-15T16:48:03Z'
  support: context_only
  summary: 'Exact sequence accession NZ_AJFS00000000.1 source qualifiers: {"organism":
    "Mycoplasmopsis canis UF33", "mol_type": "genomic DNA", "strain": "UF33", "isolation_source":
    "vagina of a dog", "host": "Canis lupus familiaris", "db_xref": "taxon:1131453",
    "geo_loc_name": "USA: FL", "collection_date": "1992"}'
  snapshot_sha256: 9fff801b583656c9f8c9188201e2b3f1f2745803a1756a413b7fe62a55713c6f
- evidence_id: EX9
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=419705607&rettype=gb&retmode=xml&seq_start=1&seq_stop=1
  locator: nuccore-1131454.xml
  accessed_at: '2026-10-15T16:48:06Z'
  support: context_only
  summary: 'Exact sequence accession NZ_AJFT00000000.1 source qualifiers: {"organism":
    "Mycoplasmopsis canis UFG1", "mol_type": "genomic DNA", "strain": "UFG1", "isolation_source":
    "brain of a dog", "host": "Canis lupus familiaris", "db_xref": "taxon:1131454",
    "geo_loc_name": "USA: FL", "collection_date": "2009"}'
  snapshot_sha256: f7fcf5e434c9d226d1c5180c37acf090e8511e5ff635ace932ff3fd0f90e0b34
- evidence_id: EX10
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=419706256&rettype=gb&retmode=xml&seq_start=1&seq_stop=1
  locator: nuccore-1131455.xml
  accessed_at: '2026-10-15T16:48:09Z'
  support: context_only
  summary: 'Exact sequence accession NZ_AJFU00000000.1 source qualifiers: {"organism":
    "Mycoplasmopsis canis UFG4", "mol_type": "genomic DNA", "strain": "UFG4", "isolation_source":
    "brain of a dog", "host": "Canis lupus familiaris", "db_xref": "taxon:1131455",
    "geo_loc_name": "USA: FL", "collection_date": "2009"}'
  snapshot_sha256: 102b13d846831f049a02bf05813ab2ef6c32135e309d95365b800c3c85174d67
- evidence_id: EX11
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1117644,1122164,1131452,1131453,1131454,1131455,1133849,1141647,1157946,1162284,1162288,1177117,1189613,1193128,1199187,1206729,1214102,1220554,1226751,12455,1271862,1328,1329,1329902,1334,1348,1392869,147802,153721,1578,1590,1601,161879,1639,1658,1661,1679,1680,1682,1683,168808,169963,1718,1724,1796,1802,1817,184914,1886,1962118,197,198,2,205913,206,2074,2081794,222805,238,2701,28026,28087,286804,287,32002,32020,33,341199,36808,391904,439842,476,47885,480035,484020,51665,524884,653940,678,720,72407,731,747,756689,76759,82135,82348,83655,838,84107,912594,985762&retmode=xml
  locator: taxonomy.xml
  accessed_at: '2026-10-15T16:34:33Z'
  support: context_only
  summary: 'All displayed IDs resolve in current NCBI Taxonomy. Preferred names and
    source labels were compared, without treating recognized historical aliases as
    wrong identities: [{"id": "NCBITaxon:12455", "source": "PREGO", "label": null,
    "current_id": "12455", "current_name": "Borna disease virus", "rank": "species",
    "direct_match": false, "recognized_alias": false}, {"id": "NCBITaxon:147802",
    "source": "PREGO", "label": "Lactobacillus iners", "current_id": "147802", "current_name":
    "Lactobacillus iners", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:1578", "source": "PREGO", "label": "Lactobacillus", "current_id":
    "1578", "current_name": "Lactobacillus", "rank": "genus", "direct_match": true,
    "recognized_alias": true}, {"id": "NCBITaxon:1601", "source": "PREGO", "label":
    "Ligilactobacillus agilis", "current_id": "1601", "current_name": "Ligilactobacillus
    agilis", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id":
    "NCBITaxon:168808", "source": "PREGO", "label": "Sneathia", "current_id": "168808",
    "current_name": "Sneathia", "rank": "genus", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:2701", "source": "PREGO", "label": "Gardnerella", "current_id":
    "2701", "current_name": "Gardnerella", "rank": "genus", "direct_match": true,
    "recognized_alias": true}, {"id": "NCBITaxon:82135", "source": "PREGO", "label":
    "Fannyhessea vaginae", "current_id": "82135", "current_name": "Fannyhessea vaginae",
    "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:838",
    "source": "PREGO", "label": "Prevotella", "current_id": "838", "current_name":
    "Prevotella", "rank": "genus", "direct_match": true, "recognized_alias": true},
    {"id": "NCBITaxon:84107", "source": "PREGO", "label": "Coriobacteriaceae", "current_id":
    "84107", "current_name": "Coriobacteriaceae", "rank": "family", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:1117644", "source": "PREGO",
    "label": "Mycoplasmopsis canis PG 14", "current_id": "1117644", "current_name":
    "Mycoplasmopsis canis PG 14", "rank": "strain", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:1131452", "source": "PREGO", "label": "Mycoplasmopsis
    canis UF31", "current_id": "1131452", "current_name": "Mycoplasmopsis canis UF31",
    "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1131453",
    "source": "PREGO", "label": "Mycoplasmopsis canis UF33", "current_id": "1131453",
    "current_name": "Mycoplasmopsis canis UF33", "rank": "strain", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:1131454", "source": "PREGO",
    "label": "Mycoplasmopsis canis UFG1", "current_id": "1131454", "current_name":
    "Mycoplasmopsis canis UFG1", "rank": "strain", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:1131455", "source": "PREGO", "label": "Mycoplasmopsis
    canis UFG4", "current_id": "1131455", "current_name": "Mycoplasmopsis canis UFG4",
    "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1133849",
    "source": "PREGO", "label": "Nocardia brasiliensis ATCC 700358", "current_id":
    "1133849", "current_name": "Nocardia brasiliensis ATCC 700358", "rank": "strain",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1177117", "source":
    "PREGO", "label": "Vreelandella stevensii S18214", "current_id": "1177117", "current_name":
    "Vreelandella stevensii S18214", "rank": "strain", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:1189613", "source": "PREGO", "label": "Staphylococcus
    massiliensis CCUG 55927", "current_id": "1189613", "current_name": "Staphylococcus
    massiliensis CCUG 55927", "rank": "strain", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:1214102", "source": "PREGO", "label": "Mycolicibacterium
    fortuitum subsp. fortuitum DSM 46621 = ATCC 6841 = JCM 6387", "current_id": "1214102",
    "current_name": "Mycolicibacterium fortuitum subsp. fortuitum DSM 46621 = ATCC
    6841 = JCM 6387", "rank": "strain", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:1328", "source": "PREGO", "label": "Streptococcus anginosus",
    "current_id": "1328", "current_name": "Streptococcus anginosus", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1348", "source":
    "PREGO", "label": "Streptococcus parauberis", "current_id": "1348", "current_name":
    "Streptococcus parauberis", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:1392869", "source": "PREGO", "label": "Escherichia coli
    K1", "current_id": "1392869", "current_name": "Escherichia coli K1", "rank": "strain",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1639", "source":
    "PREGO", "label": "Listeria monocytogenes", "current_id": "1639", "current_name":
    "Listeria monocytogenes", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:1680", "source": "PREGO", "label": "Bifidobacterium adolescentis",
    "current_id": "1680", "current_name": "Bifidobacterium adolescentis", "rank":
    "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1683",
    "source": "PREGO", "label": "Bifidobacterium angulatum", "current_id": "1683",
    "current_name": "Bifidobacterium angulatum", "rank": "species", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:169963", "source": "PREGO",
    "label": "Listeria monocytogenes EGD-e", "current_id": "169963", "current_name":
    "Listeria monocytogenes EGD-e", "rank": "strain", "direct_match": true, "recognized_alias":
    true}]'
  snapshot_sha256: 249c661a92762c2362c9b3b8c3a0606ef71a9369fb2600df89f8ed7f06ace644
- evidence_id: ESEARCH
  kind: search
  reference: Local maintained inputs and structured archive
  locator: rg --no-ignore --hidden -l -F -e BTO:0000142 -e brain -e brain -e habitatmech:PREGO.b16b4521f0
    curation history research reports data/raw build reviews
  accessed_at: '2026-10-15T16:33:57Z'
  support: context_only
  summary: Exact source/curation rows were parsed separately from broad textual matches.
    No previous structured target observation was found; not every broad label match
    was inspected.
  search_scope: curation, history, research, reports, data/raw, build and reviews;
    ignored and hidden files included, with all structured review.yaml files parsed.
- evidence_id: EAVAIL
  kind: search
  reference: Configured kg-microbe checkout
  locator: find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe
    -type f -path '*/prego/*' -name '*.tsv'
  accessed_at: '2026-10-15T16:48:02Z'
  support: context_only
  summary: No prego-directory TSVs found within this checkout. Original pair citations
    could not be inspected; this is not a global absence claim.
  search_scope: find across the configured checkout including ignored and hidden files.
assessments:
- assessment_id: A1
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: supported
  summary: BTO brain identity includes vertebrate and comparable invertebrate nervous
    centers. Forty PREGO TAXON associations and 25 displayed rows reproduce their
    source. The primary canine genome study and exact sequence metadata distinguish
    PG14 throat, UF31/UF33 vaginal origins, and UFG1/UFG4 brain origins. Recover the
    original pair evidence before endorsing brain localization for the first three;
    do not delete the two positively supported brain isolates or infer biological
    absence. Unlabeled taxon 12455 resolves to Borna disease virus.
  target_ids:
  - BTO:0000142
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EX9
  - EX10
  - EX11
- assessment_id: A2
  area: quantity
  topic: Frozen counts, units, ranks, channels and scores
  outcome: supported
  summary: 'Every source assertion and displayed taxon was checked against its exact
    raw row. [{"source": "PREGO", "count": 40, "unit": "TAXON"}]. Side-table biosample/study
    counts are not added to tree ORGANISM counts. Zero-count omission is not biological
    absence.'
  target_ids:
  - BTO:0000142
  evidence_ids:
  - E1
  - ESEED
  - EEXTRACT
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EX9
  - EX10
  - EX11
- assessment_id: A3
  area: evidence
  topic: Scientific support and scope limits
  outcome: concern
  summary: BTO brain identity includes vertebrate and comparable invertebrate nervous
    centers. Forty PREGO TAXON associations and 25 displayed rows reproduce their
    source. The primary canine genome study and exact sequence metadata distinguish
    PG14 throat, UF31/UF33 vaginal origins, and UFG1/UFG4 brain origins. Recover the
    original pair evidence before endorsing brain localization for the first three;
    do not delete the two positively supported brain isolates or infer biological
    absence. Unlabeled taxon 12455 resolves to Borna disease virus.
  target_ids:
  - BTO:0000142
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EX9
  - EX10
  - EX11
- assessment_id: A4
  area: completeness
  topic: Status, optional content, triads and mechanisms
  outcome: supported
  summary: Actual routes reproduce EXACT/SEEDED. No environmental-parameter, causal-edge,
    discussion/dataset or is_characteristic=true assertion is present in this target.
    Optional absence and SEEDED status alone are not defects. Scientific review does
    not promote native status.
  target_ids:
  - BTO:0000142
  evidence_ids:
  - E1
  - ERULE
  - ESEED
- assessment_id: A5
  area: schema
  topic: Native deterministic validation
  outcome: supported
  summary: Ordinary and strict schemas, 814 history records, provenance, 3208-record
    reproduction, 32 causal overlays, term-request checks, configured labels and exact-base
    full QC passed. These establish fidelity, not biological truth.
  target_ids:
  - BTO:0000142
  evidence_ids:
  - E1
  - ERULE
findings:
- finding_id: F1
  issue_key: brain-prego-pair-scope
  category: evidence
  severity: major
  status: open
  certainty: provisional
  title: Original pair evidence is needed for anatomical localization
  description: BTO brain identity includes vertebrate and comparable invertebrate
    nervous centers. Forty PREGO TAXON associations and 25 displayed rows reproduce
    their source. The primary canine genome study and exact sequence metadata distinguish
    PG14 throat, UF31/UF33 vaginal origins, and UFG1/UFG4 brain origins. Recover the
    original pair evidence before endorsing brain localization for the first three;
    do not delete the two positively supported brain isolates or infer biological
    absence. Unlabeled taxon 12455 resolves to Borna disease virus. Recover manifest-matching
    citations and distinguish original isolation from experimental exposure or paper
    co-mention. Correct or qualify only demonstrated mismatches through governed source/extractor
    handling; do not hand-delete taxa or decrement counts.
  target_ids:
  - BTO:0000142
  field_paths:
  - characteristic_taxa
  - source_attestations
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EX9
  - EX10
  - EX11
  - EAVAIL
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/MANIFEST.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or source-evidence claim;
    deterministic validity does not establish scientific support.
  external_issues: []
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - BTO:0000142
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/MANIFEST.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  description: BTO brain identity includes vertebrate and comparable invertebrate
    nervous centers. Forty PREGO TAXON associations and 25 displayed rows reproduce
    their source. The primary canine genome study and exact sequence metadata distinguish
    PG14 throat, UF31/UF33 vaginal origins, and UFG1/UFG4 brain origins. Recover the
    original pair evidence before endorsing brain localization for the first three;
    do not delete the two positively supported brain isolates or infer biological
    absence. Unlabeled taxon 12455 resolves to Borna disease virus. Recover manifest-matching
    citations and distinguish original isolation from experimental exposure or paper
    co-mention. Correct or qualify only demonstrated mismatches through governed source/extractor
    handling; do not hand-delete taxa or decrement counts. No repair is performed
    by this review.
  generator: Controlled source refresh when required, then just seed, guarded just
    seed-canary, just seed-apply, and dependent term-request/map/site/redirect regeneration.
  acceptance_checks:
  - Regress the exact reported claim and preserve independent identifiers, counts/units
    and raw provenance. Change identity, native status or mapping only when separately
    supported by the scoped item assessment; never change source totals by hand.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
limitations:
- Historical specimens and every original association have not been independently
  reidentified. Counts, scores and ranked rows are not prevalence, viability, characteristic
  presence or mechanism.
- The label gate skips 2061 no-adapter pairs and does not certify taxon labels. Every
  displayed taxon ID was separately resolved through current NCBI Taxonomy.
- Full QC evidence is a successful remote run at the exact unchanged input baseline,
  not a new local full-QC execution. These new review bundles require their native
  post-save archive check.
- 'iModulonDB is not applicable: no gene, regulator, transcriptomic module or causal
  mechanism is asserted. No paid research was used.'
- Original PREGO pair exports are unavailable in the configured checkout. Inspected
  primary publications and sequence qualifiers cannot reconstruct every pair or establish
  the cause of extraction errors.
notes:
- Input hashes match both current working bytes and exact tracked base blobs; source.state
  git_commit describes that historical revision without silently refreshing inputs.
- Ignored-inclusive searches and parsed structured archive found no previous structured
  observation targeting this exact identifier. Legacy findings were inspected as leads,
  not adopted automatically or assigned false structured lineage.
- 'Review-only: no habitat curation, regeneration, status promotion, history mutation
  or GitHub mutation is performed.'
tags:
- individual-scientific-review
- host-associated
```
