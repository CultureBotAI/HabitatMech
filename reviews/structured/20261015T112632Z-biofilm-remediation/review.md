# Remediation review: biofilm (BTO:0002690)

- Review: 20261015T112632Z-biofilm-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T11:25:01Z
- Finished UTC: 2026-10-15T11:26:32Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The report field locator is corrected to habitat_category. The complete record is unchanged; the original major category-overrestriction finding remains open with exact predecessor lineage.

## Scope And Provenance

Full current target re-read with every predecessor finding reassessed.

Selection: One of fifteen repaired records or the unchanged biofilm target receiving a report-locator correction in this twenty-record PR cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 4ec4413155f6113135317c787f37e36cb91304c6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0002690 | data/habitats/host_associated/biofilm.yaml | generated | biofilm |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate-strict data/habitats/host_associated/benign_tumor_tissue.yaml data/habitats/host_associated/bhk.yaml data/habitats/host_associated/bhk_21_cell.yaml data/habitats/host_associated/bile.yaml data/habitats/host_associated/bile__22fc0a7b.yaml data/habitats/host_associated/bile__57dd7796.yaml data/habitats/host_associated/bile__612af0df.yaml data/habitats/host_associated/bile__deca6de5.yaml data/habitats/host_associated/bile_duct.yaml data/habitats/host_associated/biliary_tract.yaml data/habitats/host_associated/biliary_tract__076692f7.yaml data/habitats/host_associated/biliary_tract__7bf9e820.yaml data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml data/habitats/host_associated/biliary_tract__d5e0bd1d.yaml data/habitats/host_associated/biliary_tract__e6019127.yaml data/habitats/host_associated/biocrust.yaml data/habitats/host_associated/biofilm.yaml data/habitats/host_associated/biofilm__465616a5.yaml data/habitats/host_associated/birds.yaml data/habitats/host_associated/bivalves.yaml | passed | True | BTO:0002690 | Actual execution 2026-10-15T11:22:32Z through 2026-10-15T11:22:42Z. uv run python scripts/validate_strict.py data/habitats/host_associated/benign_tumor_tissue.yaml data/habitats/host_associated/bhk.yaml data/habitats/host_associated/bhk_21_cell.yaml data/habitats/host_associated/bile.yaml data/habitats/host_associated/bile__22fc0a7b.yaml data/habitats/host_associated/bile__57dd7796.yaml data/habitats/host_associated/bile__612af0df.yaml data/habitats/host_associated/bile__deca6de5.yaml data/habitats/host_associated/bile_duct.yaml data/habitats/host_associated/biliary_tract.yaml data/habitats/host_associated/biliary_tract__076692f7.yaml data/habitats/host_associated/biliary_tract__7bf9e820.yaml data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml data/habitats/host_associated/biliary_tract__d5e0bd1d.yaml data/habitats/host_associated/biliary_tract__e6019127.yaml data/habitats/host_associated/biocrust.yaml data/habitats/host_associated/biofilm.yaml data/habitats/host_associated/biofilm__465616a5.yaml data/habitats/host_associated/birds.yaml data/habitats/host_associated/bivalves.yaml<br>Validating 20 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      20<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| just validate-history | passed | True | BTO:0002690 | Actual execution 2026-10-15T11:22:42Z through 2026-10-15T11:22:54Z. No issues found<br>807 history record(s) valid against src/habitatmech/schema/history.yaml |
| just provenance-check | passed | True | BTO:0002690 | Actual execution 2026-10-15T11:22:54Z through 2026-10-15T11:22:55Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| just verify-corpus | passed | True | BTO:0002690 | Actual execution 2026-10-15T11:22:55Z through 2026-10-15T11:23:17Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| just validate-causal-all | passed | True | BTO:0002690 | Actual execution 2026-10-15T11:23:17Z through 2026-10-15T11:23:24Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| just term-requests-check | passed | True | BTO:0002690 | Actual execution 2026-10-15T11:23:24Z through 2026-10-15T11:23:49Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| just validate-products | passed | True | BTO:0002690 | Actual execution 2026-10-15T11:23:49Z through 2026-10-15T11:25:27Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python -m pytest -q tests/test_biliary_bivalve_review_repairs.py | passed | True | BTO:0002690 | Actual execution 2026-10-15T11:25:27Z through 2026-10-15T11:25:37Z. .                                                                        [100%]<br>1 passed in 9.01s |
| git diff --check 405ef4c51cf7aa4d0d2203aaf392ed5d773a7e87 | passed | True | BTO:0002690 | Actual execution 2026-10-15T11:25:37Z through 2026-10-15T11:25:38Z.  |

## Scientific And Domain Assessments

### Exact correction and whole-record preservation

consistency: supported. Targets: BTO:0002690.

The whole-corpus counterfactual and complete current YAML demonstrate bounded hierarchy/synonym changes, preserved source metadata and status, and repeatable generation.

### Retained scientific support

evidence: supported. Targets: BTO:0002690.

The target was rechecked against retained typed ontology and bounded primary evidence. No new characteristic-presence, prevalence or mechanism claim is added.

### Unresolved findings

representation: concern. Targets: BTO:0002690.

Generic biofilm is restricted to host-associated category

## Findings

### F1: Generic biofilm is restricted to host-associated category

major / open / confirmed; issue key: biofilm-host-category-overrestriction.

Replace the BTO-prefix category fallback for this exact PREGO source with a justified ITEM override, preserving the generic physical-film identity and source observations. Pipes and host devices in the definition show that HOST_ASSOCIATED is not universal. OTHER is a candidate, not an instruction to rewrite unrelated BTO categories.

Disposition: Only the review field locator is corrected from category to habitat_category. The actual generic-biofilm category and source observations remain unchanged; scientific finding #1385 remains open.

## Recommended Actions And Acceptance Checks

### ACT1

Replace the BTO-prefix category fallback for this exact PREGO source with a justified ITEM override, preserving the generic physical-film identity and source observations. Pipes and host devices in the definition show that HOST_ASSOCIATED is not universal. OTHER is a candidate, not an instruction to rewrite unrelated BTO categories. No repair is performed by this review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history. Do not change source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000284/graph; Current identity, definition and typed relations | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0000284", "target": "http://purl.obolibrary.org/obo/BTO_0000000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000284; Current identity, definition and typed relations | supports | BTO:0000284 organism form; inspected definition: [] |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0002690/graph; Current identity, definition and typed relations | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0002690", "target": "http://purl.obolibrary.org/obo/BTO_0000284", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0002690; Current identity, definition and typed relations | supports | BTO:0002690 biofilm; inspected definition: ["A thin usually resistant layer of microorganisms (as bacteria) that form on and coat various surfaces (as of water pipes and catheters)."] |
| EX5 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3608642/fullTextXML; Methods: sample collection and combined single-cell genomes | supports | PMID:23555659; DOI:10.1371/journal.pone.0059361. Dsb1-5 combines single-cell datasets from subgingival paper-point and curette samples in healthy and periodontitis subjects. This supports oral-biofilm context at the named dataset scope; predicted genes are not direct mechanism evidence. |
| EX6 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:23412845%20AND%20SRC:MED&amp;format=json&amp;resultType=core; Primary abstract only | supports | PMID:23412845; DOI:10.1099/mic.0.064782-0. UAB PO1 and M129 formed quantitatively and qualitatively different biofilms. This supports strain-bounded biofilm formation, not all strains or the complete 188-taxon pool. Full-text retrieval failed and is not claimed. |
| EX7 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1000561,1110546,1123317,1177117,1191475,1233262,1236904,1238993,1257037,1257038,1257039,1257040,1257041,1257042,1280,1283,1292046,1321369,1367494,137591,1392869,1408271,1408272,1408273,1408274,1810840,257758,282199,440512,470&amp;retmode=xml; Exact TaxId, aliases, ScientificName, rank and lineage | supports | [{"id": "NCBITaxon:1000561", "label": "Pseudomonas aeruginosa AES-1R", "current_id": "1000561", "current_name": "Pseudomonas aeruginosa AES-1R", "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Pseudomonadales; Pseudomonadaceae; Pseudomonas; Pseudomonas aeruginosa group; Pseudomonas aeruginosa"}, {"id": "NCBITaxon:1110546", "label": "Veillonella tobetsuensis", "current_id": "1110546", "current_name": "Veillonella tobetsuensis", "current_rank": "species", "lineage": "cellular organisms; Bacteria; Bacillati; Bacillota; Negativicutes; Veillonellales; Veillonellaceae; Veillonella"}, {"id": "NCBITaxon:1123317", "label": "Streptococcus sobrinus DSM 20742 = ATCC 33478", "current_id": "1123317", "current_name": "Streptococcus sobrinus DSM 20742 = ATCC 33478", "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Bacillati; Bacillota; Bacilli; Lactobacillales; Streptococcaceae; Streptococcus; Streptococcus sobrinus"}, {"id": "NCBITaxon:1177117", "label": "Vreelandella stevensii S18214", "current_id": "1177117", "current_name": "Vreelandella stevensii S18214", "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Oceanospirillales; Halomonadaceae; Vreelandella; Vreelandella stevensii"}, {"id": "NCBITaxon:1191475", "label": "Pseudomonas aeruginosa PAO579", "current_id": "1191475", "current_name": "Pseudomonas aeruginosa PAO579", "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Pseudomonadales; Pseudomonadaceae; Pseudomonas; Pseudomonas aeruginosa group; Pseudomonas aeruginosa"}, {"id": "NCBITaxon:1233262", "label": "Mycoplasmoides pneumoniae PO1", "current_id": "1233262", "current_name": "Mycoplasmoides pneumoniae PO1", "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Bacillati; Mycoplasmatota; Mycoplasmoidales; Mycoplasmoidaceae; Mycoplasmoides; Mycoplasmoides pneumoniae"}, {"id": "NCBITaxon:1236904", "label": "Mycoplasmoides pneumoniae PI 1428", "current_id": "1236904", "current_name": "Mycoplasmoides pneumoniae PI 1428", "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Bacillati; Mycoplasmatota; Mycoplasmoidales; Mycoplasmoidaceae; Mycoplasmoides; Mycoplasmoides pneumoniae"}, {"id": "NCBITaxon:1238993", "label": "Mycoplasmoides pneumoniae M129-B7", "current_id": "1238993", "current_name": "Mycoplasmoides pneumoniae M129-B7", "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Bacillati; Mycoplasmatota; Mycoplasmoidales; Mycoplasmoidaceae; Mycoplasmoides; Mycoplasmoides pneumoniae"}, {"id": "NCBITaxon:1257037", "label": "Streptococcus mutans 5DC8", "current_id": "1257037", "current_name": "Streptococcus mutans 5DC8", "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Bacillati; Bacillota; Bacilli; Lactobacillales; Streptococcaceae; Streptococcus; Streptococcus mutans"}, {"id": "NCBITaxon:1257038", "label": "Streptococcus mutans KK21", "current_id": "1257038", "current_name": "Streptococcus mutans KK21", "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Bacillati; Bacillota; Bacilli; Lactobacillales; Streptococcaceae; Streptococcus; Streptococcus mutans"}, {"id": "NCBITaxon:1257039", "label": "Streptococcus mutans KK23", "current_id": "1257039", "current_name": "Streptococcus mutans KK23", "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Bacillati; Bacillota; Bacilli; Lactobacillales; Streptococcaceae; Streptococcus; Streptococcus mutans"}, {"id": "NCBITaxon:1257040", "label": "Streptococcus mutans AC4446", "current_id": "1257040", "current_name": "Streptococcus mutans AC4446", "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Bacillati; Bacillota; Bacilli; Lactobacillales; Streptococcaceae; Streptococcus; Streptococcus mutans"}, {"id": "NCBITaxon:1257041", "label": "Streptococcus mutans ATCC 25175", "current_id": "1257041", "current_name": "Streptococcus mutans ATCC 25175", "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Bacillati; Bacillota; Bacilli; Lactobacillales; Streptococcaceae; Streptococcus; Streptococcus mutans"}, {"id": "NCBITaxon:1257042", "label": "Streptococcus mutans NCTC 11060", "current_id": "1257042", "current_name": "Streptococcus mutans NCTC 11060", "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Bacillati; Bacillota; Bacilli; Lactobacillales; Streptococcaceae; Streptococcus; Streptococcus mutans"}, {"id": "NCBITaxon:1280", "label": "Staphylococcus aureus", "current_id": "1280", "current_name": "Staphylococcus aureus", "current_rank": "species", "lineage": "cellular organisms; Bacteria; Bacillati; Bacillota; Bacilli; Caryophanales; Staphylococcaceae; Staphylococcus"}, {"id": "NCBITaxon:1283", "label": "Staphylococcus haemolyticus", "current_id": "1283", "current_name": "Staphylococcus haemolyticus", "current_rank": "species", "lineage": "cellular organisms; Bacteria; Bacillati; Bacillota; Bacilli; Caryophanales; Staphylococcaceae; Staphylococcus"}, {"id": "NCBITaxon:1292046", "label": "Desulfobulbus sp. oral taxon 041 str. Dsb1-5", "current_id": "1292046", "current_name": "Desulfobulbus sp. oral taxon 041 str. Dsb1-5", "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Pseudomonadati; Thermodesulfobacteriota; Desulfobulbia; Desulfobulbales; Desulfobulbaceae; Desulfobulbus; unclassified Desulfobulbus; Desulfobulbus sp. oral taxon 041"}, {"id": "NCBITaxon:1321369", "label": "Staphylococcus aureus Bmb9393", "current_id": "1321369", "current_name": "Staphylococcus aureus Bmb9393", "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Bacillati; Bacillota; Bacilli; Caryophanales; Staphylococcaceae; Staphylococcus; Staphylococcus aureus"}, {"id": "NCBITaxon:1367494", "label": "Pseudomonas aeruginosa PAO1-VE13", "current_id": "1367494", "current_name": "Pseudomonas aeruginosa PAO1-VE13", "current_rank": "no rank", "lineage": "cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Pseudomonadales; Pseudomonadaceae; Pseudomonas; Pseudomonas aeruginosa group; Pseudomonas aeruginosa; Pseudomonas aeruginosa PAO1"}, {"id": "NCBITaxon:137591", "label": "Weissella cibaria", "current_id": "137591", "current_name": "Weissella cibaria", "current_rank": "species", "lineage": "cellular organisms; Bacteria; Bacillati; Bacillota; Bacilli; Lactobacillales; Lactobacillaceae; Weissella"}, {"id": "NCBITaxon:1392869", "label": "Escherichia coli K1", "current_id": "1392869", "current_name": "Escherichia coli K1", "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Enterobacterales; Enterobacteriaceae; Escherichia; Escherichia coli"}, {"id": "NCBITaxon:1408271", "label": "Pseudomonas aeruginosa LES400", "current_id": "1408271", "current_name": "Pseudomonas aeruginosa LES400", "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Pseudomonadales; Pseudomonadaceae; Pseudomonas; Pseudomonas aeruginosa group; Pseudomonas aeruginosa"}, {"id": "NCBITaxon:1408272", "label": "Pseudomonas aeruginosa LES431", "current_id": "1408272", "current_name": "Pseudomonas aeruginosa LES431", "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Pseudomonadales; Pseudomonadaceae; Pseudomonas; Pseudomonas aeruginosa group; Pseudomonas aeruginosa"}, {"id": "NCBITaxon:1408273", "label": "Pseudomonas aeruginosa LESB65", "current_id": "1408273", "current_name": "Pseudomonas aeruginosa LESB65", "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Pseudomonadales; Pseudomonadaceae; Pseudomonas; Pseudomonas aeruginosa group; Pseudomonas aeruginosa"}, {"id": "NCBITaxon:1408274", "label": "Pseudomonas aeruginosa LESlike1", "current_id": "1408274", "current_name": "Pseudomonas aeruginosa LESlike1", "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Pseudomonadales; Pseudomonadaceae; Pseudomonas; Pseudomonas aeruginosa group; Pseudomonas aeruginosa"}] |
| EAFTER | data/habitats/host_associated/biofilm.yaml; Entire current YAML | supports | Complete post-fix record inspected: {"identifier": "BTO:0002690", "label": "biofilm", "definition": "A thin usually resistant layer of microorganisms (as bacteria) that form on and coat various surfaces (as of water pipes and catheters).", "definition_source": "BTO", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "EXACT", "mapping_status": "SEEDED", "synonyms": [{"synonym_text": "biofilms", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}], "parent_habitats": ["BTO:0000284"], "source_attestations": [{"source": "PREGO", "source_id": "BTO:0002690", "source_label": "biofilm", "assertion_count": 188, "assertion_unit": "TAXON", "score": 3.0, "evidence_channels": "annotated_genomes_isolates&#124;environmental_samples"}], "characteristic_taxa": [{"taxon_id": "NCBITaxon:1000561", "source": "PREGO", "taxon_label": "Pseudomonas aeruginosa AES-1R", "score": 3.0, "rank": 1, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1110546", "source": "PREGO", "taxon_label": "Veillonella tobetsuensis", "score": 3.0, "rank": 2, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1123317", "source": "PREGO", "taxon_label": "Streptococcus sobrinus DSM 20742 = ATCC 33478", "score": 3.0, "rank": 3, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1177117", "source": "PREGO", "taxon_label": "Vreelandella stevensii S18214", "score": 3.0, "rank": 4, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1191475", "source": "PREGO", "taxon_label": "Pseudomonas aeruginosa PAO579", "score": 3.0, "rank": 5, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1233262", "source": "PREGO", "taxon_label": "Mycoplasmoides pneumoniae PO1", "score": 3.0, "rank": 6, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1236904", "source": "PREGO", "taxon_label": "Mycoplasmoides pneumoniae PI 1428", "score": 3.0, "rank": 7, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1238993", "source": "PREGO", "taxon_label": "Mycoplasmoides pneumoniae M129-B7", "score": 3.0, "rank": 8, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1257037", "source": "PREGO", "taxon_label": "Streptococcus mutans 5DC8", "score": 3.0, "rank": 9, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1257038", "source": "PREGO", "taxon_label": "Streptococcus mutans KK21", "score": 3.0, "rank": 10, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1257039", "source": "PREGO", "taxon_label": "Streptococcus mutans KK23", "score": 3.0, "rank": 11, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1257040", "source": "PREGO", "taxon_label": "Streptococcus mutans AC4446", "score": 3.0, "rank": 12, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1257041", "source": "PREGO", "taxon_label": "Streptococcus mutans ATCC 25175", "score": 3.0, "rank": 13, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1257042", "source": "PREGO", "taxon_label": "Streptococcus mutans NCTC 11060", "score": 3.0, "rank": 14, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1280", "source": "PREGO", "taxon_label": "Staphylococcus aureus", "score": 3.0, "rank": 15, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1283", "source": "PREGO", "taxon_label": "Staphylococcus haemolyticus", "score": 3.0, "rank": 16, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1292046", "source": "PREGO", "taxon_label": "Desulfobulbus sp. oral taxon 041 str. Dsb1-5", "score": 3.0, "rank": 17, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1321369", "source": "PREGO", "taxon_label": "Staphylococcus aureus Bmb9393", "score": 3.0, "rank": 18, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1367494", "source": "PREGO", "taxon_label": "Pseudomonas aeruginosa PAO1-VE13", "score": 3.0, "rank": 19, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:137591", "source": "PREGO", "taxon_label": "Weissella cibaria", "score": 3.0, "rank": 20, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1392869", "source": "PREGO", "taxon_label": "Escherichia coli K1", "score": 3.0, "rank": 21, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1408271", "source": "PREGO", "taxon_label": "Pseudomonas aeruginosa LES400", "score": 3.0, "rank": 22, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1408272", "source": "PREGO", "taxon_label": "Pseudomonas aeruginosa LES431", "score": 3.0, "rank": 23, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1408273", "source": "PREGO", "taxon_label": "Pseudomonas aeruginosa LESB65", "score": 3.0, "rank": 24, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1408274", "source": "PREGO", "taxon_label": "Pseudomonas aeruginosa LESlike1", "score": 3.0, "rank": 25, "candidate_pool": 188}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by PREGO. Grounding: EXACT."}]} |
| EPREV | reviews/structured/20261015T110633Z-biofilm-record/review.yaml; Exact predecessor and all findings | supports | Immutable original scientific observation retained unchanged. |
| ETEST | tests/test_biliary_bivalve_review_repairs.py; Whole-corpus counterfactual | supports | Restoring only prior rules changes exactly fifteen records. Identity, definitions, source observations/counts/units, taxa, native statuses, valid parents and prior history are preserved; regeneration is repeatable. |

## Limits And Additional Notes

- Same-agent review is not independent approval. Review does not promote native scientific status.
- Original source-member and source-precision limitations from the predecessor remain; preserved assertions are not independently confirmed specimens.
- Final full QC, archive integrity and real semantic-map/site publication are subsequent gates, not claimed completed in this observation.
- Configured label correspondence retains documented no-adapter skips; this is not global identifier or semantic certification.
- Shared mapping endpoints #1398 and typed ontology extraction #1249 remain open. iModulonDB is not applicable; no gene/expression assertion is made.
- Report-only correction under https://github.com/CultureBotAI/HabitatMech/issues/2178: the native field is habitat_category, not category. The immutable predecessor remains intact; correcting its locator does not close the scientific finding.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T112632Z-biofilm-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: biofilm (BTO:0002690)'
started_at: '2026-10-15T11:25:01Z'
finished_at: '2026-10-15T11:26:32Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent inspected target and evidence; not independent human
    or second-agent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: The report field locator is corrected to habitat_category. The complete record
  is unchanged; the original major category-overrestriction finding remains open with
  exact predecessor lineage.
source:
  git_revision: 4ec4413155f6113135317c787f37e36cb91304c6
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
    sha256: ca42d86b6040df1c0c6e6ed36573bb51975a5e8daade262113bce547f1b6fd8b
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 574399bd8a3d5b0cd9280126eefa878decc2d6d44e46742c5bc6a42a994b3b14
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: a3dcff92a2317bb47ce8ace1064faa7c0611b2ce9f805348a245ec1a9b268157
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: 2f94ea4d12f8b40ae688d2099ed7f201056996abf750f9d842a09e0fd383ab55
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
  - path: data/habitats/host_associated/biofilm.yaml
    sha256: 62608951fa02a03e4173953042727a167eeed7ed02a7f7d07b350b55dd5bd01c
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
  - path: reports/yaml_record_review/20261004T131814Z-biofilm.md
    sha256: 065c5a788ec8d0b370e48826d1f609d42fd5c8e0c8f155c8a0a7d0cea7feb07e
    role: context
  - path: reviews/structured/20261015T110633Z-biofilm-record/review.yaml
    sha256: 69375ce4d5c522f1badccfb0c9d79d7a1bef036bd77e08acd07291f998760d1e
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
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
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
  - path: tests/test_biliary_bivalve_review_repairs.py
    sha256: 1412766b81259472012db4a0b75b171a12d854357f7c6d2d79289dcbcb1882d0
    role: context
targets:
- target_id: BTO:0002690
  path: data/habitats/host_associated/biofilm.yaml
  label: biofilm
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
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
scope:
  description: Full current target re-read with every predecessor finding reassessed.
  selection: One of fifteen repaired records or the unchanged biofilm target receiving
    a report-locator correction in this twenty-record PR cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - BTO:0002690
  exclusions:
  - target: Global mapping, source contracts and other records
    reason: Only exact hierarchy/synonym witnesses are repaired; SSSOM/KGX readiness
      is not certified.
checks:
- check_id: C1
  name: just validate-strict data/habitats/host_associated/benign_tumor_tissue.yaml
    data/habitats/host_associated/bhk.yaml data/habitats/host_associated/bhk_21_cell.yaml
    data/habitats/host_associated/bile.yaml data/habitats/host_associated/bile__22fc0a7b.yaml
    data/habitats/host_associated/bile__57dd7796.yaml data/habitats/host_associated/bile__612af0df.yaml
    data/habitats/host_associated/bile__deca6de5.yaml data/habitats/host_associated/bile_duct.yaml
    data/habitats/host_associated/biliary_tract.yaml data/habitats/host_associated/biliary_tract__076692f7.yaml
    data/habitats/host_associated/biliary_tract__7bf9e820.yaml data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml
    data/habitats/host_associated/biliary_tract__d5e0bd1d.yaml data/habitats/host_associated/biliary_tract__e6019127.yaml
    data/habitats/host_associated/biocrust.yaml data/habitats/host_associated/biofilm.yaml
    data/habitats/host_associated/biofilm__465616a5.yaml data/habitats/host_associated/birds.yaml
    data/habitats/host_associated/bivalves.yaml
  status: passed
  required: true
  command: just validate-strict data/habitats/host_associated/benign_tumor_tissue.yaml
    data/habitats/host_associated/bhk.yaml data/habitats/host_associated/bhk_21_cell.yaml
    data/habitats/host_associated/bile.yaml data/habitats/host_associated/bile__22fc0a7b.yaml
    data/habitats/host_associated/bile__57dd7796.yaml data/habitats/host_associated/bile__612af0df.yaml
    data/habitats/host_associated/bile__deca6de5.yaml data/habitats/host_associated/bile_duct.yaml
    data/habitats/host_associated/biliary_tract.yaml data/habitats/host_associated/biliary_tract__076692f7.yaml
    data/habitats/host_associated/biliary_tract__7bf9e820.yaml data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml
    data/habitats/host_associated/biliary_tract__d5e0bd1d.yaml data/habitats/host_associated/biliary_tract__e6019127.yaml
    data/habitats/host_associated/biocrust.yaml data/habitats/host_associated/biofilm.yaml
    data/habitats/host_associated/biofilm__465616a5.yaml data/habitats/host_associated/birds.yaml
    data/habitats/host_associated/bivalves.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0002690
  summary: "Actual execution 2026-10-15T11:22:32Z through 2026-10-15T11:22:42Z. uv\
    \ run python scripts/validate_strict.py data/habitats/host_associated/benign_tumor_tissue.yaml\
    \ data/habitats/host_associated/bhk.yaml data/habitats/host_associated/bhk_21_cell.yaml\
    \ data/habitats/host_associated/bile.yaml data/habitats/host_associated/bile__22fc0a7b.yaml\
    \ data/habitats/host_associated/bile__57dd7796.yaml data/habitats/host_associated/bile__612af0df.yaml\
    \ data/habitats/host_associated/bile__deca6de5.yaml data/habitats/host_associated/bile_duct.yaml\
    \ data/habitats/host_associated/biliary_tract.yaml data/habitats/host_associated/biliary_tract__076692f7.yaml\
    \ data/habitats/host_associated/biliary_tract__7bf9e820.yaml data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml\
    \ data/habitats/host_associated/biliary_tract__d5e0bd1d.yaml data/habitats/host_associated/biliary_tract__e6019127.yaml\
    \ data/habitats/host_associated/biocrust.yaml data/habitats/host_associated/biofilm.yaml\
    \ data/habitats/host_associated/biofilm__465616a5.yaml data/habitats/host_associated/birds.yaml\
    \ data/habitats/host_associated/bivalves.yaml\nValidating 20 files with 15 workers;\
    \ schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      20\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Strict validation covers twenty targets; other documented gates full
    corpus except focused pytest.
- check_id: C2
  name: just validate-history
  status: passed
  required: true
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0002690
  summary: 'Actual execution 2026-10-15T11:22:42Z through 2026-10-15T11:22:54Z. No
    issues found

    807 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Strict validation covers twenty targets; other documented gates full
    corpus except focused pytest.
- check_id: C3
  name: just provenance-check
  status: passed
  required: true
  command: just provenance-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0002690
  summary: "Actual execution 2026-10-15T11:22:54Z through 2026-10-15T11:22:55Z. provenance\
    \ current: 14 committed inventories, 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Strict validation covers twenty targets; other documented gates full
    corpus except focused pytest.
- check_id: C4
  name: just verify-corpus
  status: passed
  required: true
  command: just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0002690
  summary: "Actual execution 2026-10-15T11:22:55Z through 2026-10-15T11:23:17Z. expected\
    \ 3208 records, found 3208 on disk\n  missing:   0\n  extra:     0\n  differing:\
    \ 0\n\ncorpus reproduces exactly from data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Strict validation covers twenty targets; other documented gates full
    corpus except focused pytest.
- check_id: C5
  name: just validate-causal-all
  status: passed
  required: true
  command: just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0002690
  summary: "Actual execution 2026-10-15T11:23:17Z through 2026-10-15T11:23:24Z. validated\
    \ 32 causal-graph curation file(s) with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Strict validation covers twenty targets; other documented gates full
    corpus except focused pytest.
- check_id: C6
  name: just term-requests-check
  status: passed
  required: true
  command: just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0002690
  summary: "Actual execution 2026-10-15T11:23:24Z through 2026-10-15T11:23:49Z. term-request\
    \ table is current (110 terms)\n uv run python scripts/build_term_requests.py\
    \ --check"
  scope_note: Strict validation covers twenty targets; other documented gates full
    corpus except focused pytest.
- check_id: C7
  name: just validate-products
  status: passed
  required: true
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0002690
  summary: "Actual execution 2026-10-15T11:23:49Z through 2026-10-15T11:25:27Z. id↔label\
    \ correspondence summary:\n          OK_CANONICAL: 1174\n            OK_SYNONYM:\
    \ 1\n          OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label\
    \ pairs correspond.\n uv run python scripts/validate_id_label_correspondence.py\
    \ -c conf/id_label_targets.yaml"
  scope_note: Strict validation covers twenty targets; other documented gates full
    corpus except focused pytest.
- check_id: C8
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_biliary_bivalve_review_repairs.py
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_biliary_bivalve_review_repairs.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0002690
  summary: 'Actual execution 2026-10-15T11:25:27Z through 2026-10-15T11:25:37Z. .                                                                        [100%]

    1 passed in 9.01s'
  scope_note: Strict validation covers twenty targets; other documented gates full
    corpus except focused pytest.
- check_id: C9
  name: git diff --check 405ef4c51cf7aa4d0d2203aaf392ed5d773a7e87
  status: passed
  required: true
  command: git diff --check 405ef4c51cf7aa4d0d2203aaf392ed5d773a7e87
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0002690
  summary: 'Actual execution 2026-10-15T11:25:37Z through 2026-10-15T11:25:38Z. '
  scope_note: Strict validation covers twenty targets; other documented gates full
    corpus except focused pytest.
evidence:
- evidence_id: EX1
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000284/graph
  locator: Current identity, definition and typed relations
  accessed_at: '2026-10-15T10:52:21Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0000284",
    "target": "http://purl.obolibrary.org/obo/BTO_0000000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: d8667ccebbf1ef06a4dfb8fc90b7e8fd16d9475a22121ec59f2cf35c6c7c5968
- evidence_id: EX2
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000284
  locator: Current identity, definition and typed relations
  accessed_at: '2026-10-15T10:52:20Z'
  support: supports
  summary: 'BTO:0000284 organism form; inspected definition: []'
  snapshot_sha256: 305fb4df3b8081b3645a0a98f1f5abe7014f5e0b0458732189ba37fdd5b961f8
- evidence_id: EX3
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0002690/graph
  locator: Current identity, definition and typed relations
  accessed_at: '2026-10-15T10:52:27Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0002690",
    "target": "http://purl.obolibrary.org/obo/BTO_0000284", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: 6a27ae937b0eea2e18eed3dfdefeb23236ddf0c383d7ece2afa696a6ea91fa77
- evidence_id: EX4
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0002690
  locator: Current identity, definition and typed relations
  accessed_at: '2026-10-15T10:52:26Z'
  support: supports
  summary: 'BTO:0002690 biofilm; inspected definition: ["A thin usually resistant
    layer of microorganisms (as bacteria) that form on and coat various surfaces (as
    of water pipes and catheters)."]'
  snapshot_sha256: 480ca8386eecb2d96a2a1caeef26bff28dc92d818d44e3c8979be993fe2db45e
- evidence_id: EX5
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3608642/fullTextXML
  locator: 'Methods: sample collection and combined single-cell genomes'
  accessed_at: '2026-10-15T10:53:39Z'
  support: supports
  summary: PMID:23555659; DOI:10.1371/journal.pone.0059361. Dsb1-5 combines single-cell
    datasets from subgingival paper-point and curette samples in healthy and periodontitis
    subjects. This supports oral-biofilm context at the named dataset scope; predicted
    genes are not direct mechanism evidence.
  snapshot_sha256: 83eff02d5f8561fd1f6ec0e3f479d8544232273aad77c586a383306212d0cfeb
- evidence_id: EX6
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:23412845%20AND%20SRC:MED&format=json&resultType=core
  locator: Primary abstract only
  accessed_at: '2026-10-15T10:55:33Z'
  support: supports
  summary: PMID:23412845; DOI:10.1099/mic.0.064782-0. UAB PO1 and M129 formed quantitatively
    and qualitatively different biofilms. This supports strain-bounded biofilm formation,
    not all strains or the complete 188-taxon pool. Full-text retrieval failed and
    is not claimed.
  snapshot_sha256: 46c375430741c0775f189c02dfacdfe276bafa4aa39299849b3784ff164d2c25
- evidence_id: EX7
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1000561,1110546,1123317,1177117,1191475,1233262,1236904,1238993,1257037,1257038,1257039,1257040,1257041,1257042,1280,1283,1292046,1321369,1367494,137591,1392869,1408271,1408272,1408273,1408274,1810840,257758,282199,440512,470&retmode=xml
  locator: Exact TaxId, aliases, ScientificName, rank and lineage
  accessed_at: '2026-10-15T10:52:57Z'
  support: supports
  summary: '[{"id": "NCBITaxon:1000561", "label": "Pseudomonas aeruginosa AES-1R",
    "current_id": "1000561", "current_name": "Pseudomonas aeruginosa AES-1R", "current_rank":
    "strain", "lineage": "cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota;
    Gammaproteobacteria; Pseudomonadales; Pseudomonadaceae; Pseudomonas; Pseudomonas
    aeruginosa group; Pseudomonas aeruginosa"}, {"id": "NCBITaxon:1110546", "label":
    "Veillonella tobetsuensis", "current_id": "1110546", "current_name": "Veillonella
    tobetsuensis", "current_rank": "species", "lineage": "cellular organisms; Bacteria;
    Bacillati; Bacillota; Negativicutes; Veillonellales; Veillonellaceae; Veillonella"},
    {"id": "NCBITaxon:1123317", "label": "Streptococcus sobrinus DSM 20742 = ATCC
    33478", "current_id": "1123317", "current_name": "Streptococcus sobrinus DSM 20742
    = ATCC 33478", "current_rank": "strain", "lineage": "cellular organisms; Bacteria;
    Bacillati; Bacillota; Bacilli; Lactobacillales; Streptococcaceae; Streptococcus;
    Streptococcus sobrinus"}, {"id": "NCBITaxon:1177117", "label": "Vreelandella stevensii
    S18214", "current_id": "1177117", "current_name": "Vreelandella stevensii S18214",
    "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Pseudomonadati;
    Pseudomonadota; Gammaproteobacteria; Oceanospirillales; Halomonadaceae; Vreelandella;
    Vreelandella stevensii"}, {"id": "NCBITaxon:1191475", "label": "Pseudomonas aeruginosa
    PAO579", "current_id": "1191475", "current_name": "Pseudomonas aeruginosa PAO579",
    "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Pseudomonadati;
    Pseudomonadota; Gammaproteobacteria; Pseudomonadales; Pseudomonadaceae; Pseudomonas;
    Pseudomonas aeruginosa group; Pseudomonas aeruginosa"}, {"id": "NCBITaxon:1233262",
    "label": "Mycoplasmoides pneumoniae PO1", "current_id": "1233262", "current_name":
    "Mycoplasmoides pneumoniae PO1", "current_rank": "strain", "lineage": "cellular
    organisms; Bacteria; Bacillati; Mycoplasmatota; Mycoplasmoidales; Mycoplasmoidaceae;
    Mycoplasmoides; Mycoplasmoides pneumoniae"}, {"id": "NCBITaxon:1236904", "label":
    "Mycoplasmoides pneumoniae PI 1428", "current_id": "1236904", "current_name":
    "Mycoplasmoides pneumoniae PI 1428", "current_rank": "strain", "lineage": "cellular
    organisms; Bacteria; Bacillati; Mycoplasmatota; Mycoplasmoidales; Mycoplasmoidaceae;
    Mycoplasmoides; Mycoplasmoides pneumoniae"}, {"id": "NCBITaxon:1238993", "label":
    "Mycoplasmoides pneumoniae M129-B7", "current_id": "1238993", "current_name":
    "Mycoplasmoides pneumoniae M129-B7", "current_rank": "strain", "lineage": "cellular
    organisms; Bacteria; Bacillati; Mycoplasmatota; Mycoplasmoidales; Mycoplasmoidaceae;
    Mycoplasmoides; Mycoplasmoides pneumoniae"}, {"id": "NCBITaxon:1257037", "label":
    "Streptococcus mutans 5DC8", "current_id": "1257037", "current_name": "Streptococcus
    mutans 5DC8", "current_rank": "strain", "lineage": "cellular organisms; Bacteria;
    Bacillati; Bacillota; Bacilli; Lactobacillales; Streptococcaceae; Streptococcus;
    Streptococcus mutans"}, {"id": "NCBITaxon:1257038", "label": "Streptococcus mutans
    KK21", "current_id": "1257038", "current_name": "Streptococcus mutans KK21", "current_rank":
    "strain", "lineage": "cellular organisms; Bacteria; Bacillati; Bacillota; Bacilli;
    Lactobacillales; Streptococcaceae; Streptococcus; Streptococcus mutans"}, {"id":
    "NCBITaxon:1257039", "label": "Streptococcus mutans KK23", "current_id": "1257039",
    "current_name": "Streptococcus mutans KK23", "current_rank": "strain", "lineage":
    "cellular organisms; Bacteria; Bacillati; Bacillota; Bacilli; Lactobacillales;
    Streptococcaceae; Streptococcus; Streptococcus mutans"}, {"id": "NCBITaxon:1257040",
    "label": "Streptococcus mutans AC4446", "current_id": "1257040", "current_name":
    "Streptococcus mutans AC4446", "current_rank": "strain", "lineage": "cellular
    organisms; Bacteria; Bacillati; Bacillota; Bacilli; Lactobacillales; Streptococcaceae;
    Streptococcus; Streptococcus mutans"}, {"id": "NCBITaxon:1257041", "label": "Streptococcus
    mutans ATCC 25175", "current_id": "1257041", "current_name": "Streptococcus mutans
    ATCC 25175", "current_rank": "strain", "lineage": "cellular organisms; Bacteria;
    Bacillati; Bacillota; Bacilli; Lactobacillales; Streptococcaceae; Streptococcus;
    Streptococcus mutans"}, {"id": "NCBITaxon:1257042", "label": "Streptococcus mutans
    NCTC 11060", "current_id": "1257042", "current_name": "Streptococcus mutans NCTC
    11060", "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Bacillati;
    Bacillota; Bacilli; Lactobacillales; Streptococcaceae; Streptococcus; Streptococcus
    mutans"}, {"id": "NCBITaxon:1280", "label": "Staphylococcus aureus", "current_id":
    "1280", "current_name": "Staphylococcus aureus", "current_rank": "species", "lineage":
    "cellular organisms; Bacteria; Bacillati; Bacillota; Bacilli; Caryophanales; Staphylococcaceae;
    Staphylococcus"}, {"id": "NCBITaxon:1283", "label": "Staphylococcus haemolyticus",
    "current_id": "1283", "current_name": "Staphylococcus haemolyticus", "current_rank":
    "species", "lineage": "cellular organisms; Bacteria; Bacillati; Bacillota; Bacilli;
    Caryophanales; Staphylococcaceae; Staphylococcus"}, {"id": "NCBITaxon:1292046",
    "label": "Desulfobulbus sp. oral taxon 041 str. Dsb1-5", "current_id": "1292046",
    "current_name": "Desulfobulbus sp. oral taxon 041 str. Dsb1-5", "current_rank":
    "strain", "lineage": "cellular organisms; Bacteria; Pseudomonadati; Thermodesulfobacteriota;
    Desulfobulbia; Desulfobulbales; Desulfobulbaceae; Desulfobulbus; unclassified
    Desulfobulbus; Desulfobulbus sp. oral taxon 041"}, {"id": "NCBITaxon:1321369",
    "label": "Staphylococcus aureus Bmb9393", "current_id": "1321369", "current_name":
    "Staphylococcus aureus Bmb9393", "current_rank": "strain", "lineage": "cellular
    organisms; Bacteria; Bacillati; Bacillota; Bacilli; Caryophanales; Staphylococcaceae;
    Staphylococcus; Staphylococcus aureus"}, {"id": "NCBITaxon:1367494", "label":
    "Pseudomonas aeruginosa PAO1-VE13", "current_id": "1367494", "current_name": "Pseudomonas
    aeruginosa PAO1-VE13", "current_rank": "no rank", "lineage": "cellular organisms;
    Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Pseudomonadales;
    Pseudomonadaceae; Pseudomonas; Pseudomonas aeruginosa group; Pseudomonas aeruginosa;
    Pseudomonas aeruginosa PAO1"}, {"id": "NCBITaxon:137591", "label": "Weissella
    cibaria", "current_id": "137591", "current_name": "Weissella cibaria", "current_rank":
    "species", "lineage": "cellular organisms; Bacteria; Bacillati; Bacillota; Bacilli;
    Lactobacillales; Lactobacillaceae; Weissella"}, {"id": "NCBITaxon:1392869", "label":
    "Escherichia coli K1", "current_id": "1392869", "current_name": "Escherichia coli
    K1", "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Pseudomonadati;
    Pseudomonadota; Gammaproteobacteria; Enterobacterales; Enterobacteriaceae; Escherichia;
    Escherichia coli"}, {"id": "NCBITaxon:1408271", "label": "Pseudomonas aeruginosa
    LES400", "current_id": "1408271", "current_name": "Pseudomonas aeruginosa LES400",
    "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Pseudomonadati;
    Pseudomonadota; Gammaproteobacteria; Pseudomonadales; Pseudomonadaceae; Pseudomonas;
    Pseudomonas aeruginosa group; Pseudomonas aeruginosa"}, {"id": "NCBITaxon:1408272",
    "label": "Pseudomonas aeruginosa LES431", "current_id": "1408272", "current_name":
    "Pseudomonas aeruginosa LES431", "current_rank": "strain", "lineage": "cellular
    organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Pseudomonadales;
    Pseudomonadaceae; Pseudomonas; Pseudomonas aeruginosa group; Pseudomonas aeruginosa"},
    {"id": "NCBITaxon:1408273", "label": "Pseudomonas aeruginosa LESB65", "current_id":
    "1408273", "current_name": "Pseudomonas aeruginosa LESB65", "current_rank": "strain",
    "lineage": "cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
    Pseudomonadales; Pseudomonadaceae; Pseudomonas; Pseudomonas aeruginosa group;
    Pseudomonas aeruginosa"}, {"id": "NCBITaxon:1408274", "label": "Pseudomonas aeruginosa
    LESlike1", "current_id": "1408274", "current_name": "Pseudomonas aeruginosa LESlike1",
    "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Pseudomonadati;
    Pseudomonadota; Gammaproteobacteria; Pseudomonadales; Pseudomonadaceae; Pseudomonas;
    Pseudomonas aeruginosa group; Pseudomonas aeruginosa"}]'
  snapshot_sha256: c0e0525844dde33d0c1309b8876344c9404ef26c8769b279c3b5aae5f5a2a5df
- evidence_id: EAFTER
  kind: record_content
  reference: data/habitats/host_associated/biofilm.yaml
  locator: Entire current YAML
  accessed_at: '2026-10-15T11:26:32Z'
  support: supports
  summary: 'Complete post-fix record inspected: {"identifier": "BTO:0002690", "label":
    "biofilm", "definition": "A thin usually resistant layer of microorganisms (as
    bacteria) that form on and coat various surfaces (as of water pipes and catheters).",
    "definition_source": "BTO", "habitat_category": "HOST_ASSOCIATED", "grounding_status":
    "EXACT", "mapping_status": "SEEDED", "synonyms": [{"synonym_text": "biofilms",
    "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}], "parent_habitats": ["BTO:0000284"],
    "source_attestations": [{"source": "PREGO", "source_id": "BTO:0002690", "source_label":
    "biofilm", "assertion_count": 188, "assertion_unit": "TAXON", "score": 3.0, "evidence_channels":
    "annotated_genomes_isolates|environmental_samples"}], "characteristic_taxa": [{"taxon_id":
    "NCBITaxon:1000561", "source": "PREGO", "taxon_label": "Pseudomonas aeruginosa
    AES-1R", "score": 3.0, "rank": 1, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1110546",
    "source": "PREGO", "taxon_label": "Veillonella tobetsuensis", "score": 3.0, "rank":
    2, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1123317", "source": "PREGO",
    "taxon_label": "Streptococcus sobrinus DSM 20742 = ATCC 33478", "score": 3.0,
    "rank": 3, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1177117", "source":
    "PREGO", "taxon_label": "Vreelandella stevensii S18214", "score": 3.0, "rank":
    4, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1191475", "source": "PREGO",
    "taxon_label": "Pseudomonas aeruginosa PAO579", "score": 3.0, "rank": 5, "candidate_pool":
    188}, {"taxon_id": "NCBITaxon:1233262", "source": "PREGO", "taxon_label": "Mycoplasmoides
    pneumoniae PO1", "score": 3.0, "rank": 6, "candidate_pool": 188}, {"taxon_id":
    "NCBITaxon:1236904", "source": "PREGO", "taxon_label": "Mycoplasmoides pneumoniae
    PI 1428", "score": 3.0, "rank": 7, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1238993",
    "source": "PREGO", "taxon_label": "Mycoplasmoides pneumoniae M129-B7", "score":
    3.0, "rank": 8, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1257037", "source":
    "PREGO", "taxon_label": "Streptococcus mutans 5DC8", "score": 3.0, "rank": 9,
    "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1257038", "source": "PREGO", "taxon_label":
    "Streptococcus mutans KK21", "score": 3.0, "rank": 10, "candidate_pool": 188},
    {"taxon_id": "NCBITaxon:1257039", "source": "PREGO", "taxon_label": "Streptococcus
    mutans KK23", "score": 3.0, "rank": 11, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1257040",
    "source": "PREGO", "taxon_label": "Streptococcus mutans AC4446", "score": 3.0,
    "rank": 12, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1257041", "source":
    "PREGO", "taxon_label": "Streptococcus mutans ATCC 25175", "score": 3.0, "rank":
    13, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1257042", "source": "PREGO",
    "taxon_label": "Streptococcus mutans NCTC 11060", "score": 3.0, "rank": 14, "candidate_pool":
    188}, {"taxon_id": "NCBITaxon:1280", "source": "PREGO", "taxon_label": "Staphylococcus
    aureus", "score": 3.0, "rank": 15, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1283",
    "source": "PREGO", "taxon_label": "Staphylococcus haemolyticus", "score": 3.0,
    "rank": 16, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1292046", "source":
    "PREGO", "taxon_label": "Desulfobulbus sp. oral taxon 041 str. Dsb1-5", "score":
    3.0, "rank": 17, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1321369", "source":
    "PREGO", "taxon_label": "Staphylococcus aureus Bmb9393", "score": 3.0, "rank":
    18, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1367494", "source": "PREGO",
    "taxon_label": "Pseudomonas aeruginosa PAO1-VE13", "score": 3.0, "rank": 19, "candidate_pool":
    188}, {"taxon_id": "NCBITaxon:137591", "source": "PREGO", "taxon_label": "Weissella
    cibaria", "score": 3.0, "rank": 20, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1392869",
    "source": "PREGO", "taxon_label": "Escherichia coli K1", "score": 3.0, "rank":
    21, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1408271", "source": "PREGO",
    "taxon_label": "Pseudomonas aeruginosa LES400", "score": 3.0, "rank": 22, "candidate_pool":
    188}, {"taxon_id": "NCBITaxon:1408272", "source": "PREGO", "taxon_label": "Pseudomonas
    aeruginosa LES431", "score": 3.0, "rank": 23, "candidate_pool": 188}, {"taxon_id":
    "NCBITaxon:1408273", "source": "PREGO", "taxon_label": "Pseudomonas aeruginosa
    LESB65", "score": 3.0, "rank": 24, "candidate_pool": 188}, {"taxon_id": "NCBITaxon:1408274",
    "source": "PREGO", "taxon_label": "Pseudomonas aeruginosa LESlike1", "score":
    3.0, "rank": 25, "candidate_pool": 188}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z",
    "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded
    from data/raw/ inventories; attested by PREGO. Grounding: EXACT."}]}'
  snapshot_sha256: 62608951fa02a03e4173953042727a167eeed7ed02a7f7d07b350b55dd5bd01c
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261015T110633Z-biofilm-record/review.yaml
  locator: Exact predecessor and all findings
  accessed_at: '2026-10-15T11:26:32Z'
  support: supports
  summary: Immutable original scientific observation retained unchanged.
  snapshot_sha256: 69375ce4d5c522f1badccfb0c9d79d7a1bef036bd77e08acd07291f998760d1e
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_biliary_bivalve_review_repairs.py
  locator: Whole-corpus counterfactual
  accessed_at: '2026-10-15T11:26:32Z'
  support: supports
  summary: Restoring only prior rules changes exactly fifteen records. Identity, definitions,
    source observations/counts/units, taxa, native statuses, valid parents and prior
    history are preserved; regeneration is repeatable.
  snapshot_sha256: 1412766b81259472012db4a0b75b171a12d854357f7c6d2d79289dcbcb1882d0
assessments:
- assessment_id: A1
  area: consistency
  topic: Exact correction and whole-record preservation
  outcome: supported
  summary: The whole-corpus counterfactual and complete current YAML demonstrate bounded
    hierarchy/synonym changes, preserved source metadata and status, and repeatable
    generation.
  target_ids:
  - BTO:0002690
  evidence_ids:
  - EAFTER
  - EPREV
  - ETEST
- assessment_id: A2
  area: evidence
  topic: Retained scientific support
  outcome: supported
  summary: The target was rechecked against retained typed ontology and bounded primary
    evidence. No new characteristic-presence, prevalence or mechanism claim is added.
  target_ids:
  - BTO:0002690
  evidence_ids:
  - EAFTER
  - EPREV
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
- assessment_id: A3
  area: representation
  topic: Unresolved findings
  outcome: concern
  summary: Generic biofilm is restricted to host-associated category
  target_ids:
  - BTO:0002690
  evidence_ids:
  - EAFTER
  - EPREV
findings:
- finding_id: F1
  issue_key: biofilm-host-category-overrestriction
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Generic biofilm is restricted to host-associated category
  description: Replace the BTO-prefix category fallback for this exact PREGO source
    with a justified ITEM override, preserving the generic physical-film identity
    and source observations. Pipes and host devices in the definition show that HOST_ASSOCIATED
    is not universal. OTHER is a candidate, not an instruction to rewrite unrelated
    BTO categories.
  target_ids:
  - BTO:0002690
  field_paths:
  - habitat_category
  evidence_ids:
  - EAFTER
  - EPREV
  - ETEST
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or source-evidence claim;
    deterministic validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1385
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261015T110633Z-biofilm-record
    finding_id: F1
  disposition_reason: 'Only the review field locator is corrected from category to
    habitat_category. The actual generic-biofilm category and source observations
    remain unchanged; scientific finding #1385 remains open.'
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - BTO:0002690
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: Replace the BTO-prefix category fallback for this exact PREGO source
    with a justified ITEM override, preserving the generic physical-film identity
    and source observations. Pipes and host devices in the definition show that HOST_ASSOCIATED
    is not universal. OTHER is a candidate, not an instruction to rewrite unrelated
    BTO categories. No repair is performed by this review.
  generator: Controlled source refresh when required, then just seed, guarded just
    seed-canary, just seed-apply, and dependent term-request/map/site/redirect regeneration.
  acceptance_checks:
  - Regress the exact reported claim and preserve independently valid identifiers,
    source counts/units, raw provenance, native status and history. Do not change
    source totals by hand.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
limitations:
- Same-agent review is not independent approval. Review does not promote native scientific
  status.
- Original source-member and source-precision limitations from the predecessor remain;
  preserved assertions are not independently confirmed specimens.
- Final full QC, archive integrity and real semantic-map/site publication are subsequent
  gates, not claimed completed in this observation.
- Configured label correspondence retains documented no-adapter skips; this is not
  global identifier or semantic certification.
- 'Shared mapping endpoints #1398 and typed ontology extraction #1249 remain open.
  iModulonDB is not applicable; no gene/expression assertion is made.'
notes:
- 'Report-only correction under https://github.com/CultureBotAI/HabitatMech/issues/2178:
  the native field is habitat_category, not category. The immutable predecessor remains
  intact; correcting its locator does not close the scientific finding.'
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261015T110633Z-biofilm-record
  relationship: Exact predecessor; every original finding identity and lineage retained.
```
