# Record review: BHK-21 cell (BTO:0000120)

- Review: 20261015T110623Z-bhk_21_cell-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T10:49:53Z
- Finished UTC: 2026-10-15T11:06:23Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

BTO identifies the clone-13 BHK-21 cell line and its BHK-cell superclass. The exact NZ-RLO1 association requires pair-level support: the linked genome publication used EPC cells, whereas the inspected BHK-21 growth report concerns genetically distinct NZ-RLO2. This is not proof that NZ-RLO1 never occurs in BHK-21.

## Scope And Provenance

Scientific assessment of one exact target at captured revision 405ef4c51cf7aa4d0d2203aaf392ed5d773a7e87.

Selection: Next twenty unreviewed records in corpus path order; this document assesses one resolved identifier.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 405ef4c51cf7aa4d0d2203aaf392ed5d773a7e87.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0000120 | data/habitats/host_associated/bhk_21_cell.yaml | generated | BHK-21 cell |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0000120 | Completed 2026-10-15T10:50:20Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/bhk_21_cell.yaml |
| validate-strict | passed | True | BTO:0000120 | Completed 2026-10-15T10:52:03Z. uv run python scripts/validate_strict.py data/habitats/host_associated/benign_tumor_tissue.yaml data/habitats/host_associated/bhk.yaml data/habitats/host_associated/bhk_21_cell.yaml data/habitats/host_associated/bile.yaml data/habitats/host_associated/bile__22fc0a7b.yaml data/habitats/host_associated/bile__57dd7796.yaml data/habitats/host_associated/bile__612af0df.yaml data/habitats/host_associated/bile__deca6de5.yaml data/habitats/host_associated/bile_duct.yaml data/habitats/host_associated/biliary_tract.yaml data/habitats/host_associated/biliary_tract__076692f7.yaml data/habitats/host_associated/biliary_tract__7bf9e820.yaml data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml data/habitats/host_associated/biliary_tract__d5e0bd1d.yaml data/habitats/host_associated/biliary_tract__e6019127.yaml data/habitats/host_associated/biocrust.yaml data/habitats/host_associated/biofilm.yaml data/habitats/host_associated/biofilm__465616a5.yaml data/habitats/host_associated/birds.yaml data/habitats/host_associated/bivalves.yaml<br>Validating 20 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      20<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | BTO:0000120 | Completed 2026-10-15T10:52:45Z. No issues found<br>789 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | BTO:0000120 | Completed 2026-10-15T10:52:46Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | BTO:0000120 | Completed 2026-10-15T10:53:13Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | BTO:0000120 | Completed 2026-10-15T10:53:20Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | BTO:0000120 | Completed 2026-10-15T10:53:50Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | BTO:0000120 | Completed 2026-10-15T10:55:12Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Baseline full native QC | passed | True | BTO:0000120 | Exact-revision full QC and structured review contract succeeded; verified 2026-10-15T11:05:49Z. https://github.com/CultureBotAI/HabitatMech/actions/runs/38722329263 |

## Scientific And Domain Assessments

### Native validity and reproduction

schema: supported. Targets: BTO:0000120.

Individual schema, twenty-target strict validation, 789 history records, 14 inventories/two GOLD sources, 3,208-record reproduction, 32 overlays and 110 term requests passed. These are deterministic rather than scientific certification.

### Identity, hierarchy and alias scope

identity: concern. Targets: BTO:0000120.

BTO identifies the clone-13 BHK-21 cell line and its BHK-cell superclass. The exact NZ-RLO1 association requires pair-level support: the linked genome publication used EPC cells, whereas the inspected BHK-21 growth report concerns genetically distinct NZ-RLO2. This is not proof that NZ-RLO1 never occurs in BHK-21.

### Counts, units and ranking

quantity: supported. Targets: BTO:0000120.

Exact source rows reproduce [{"source": "PREGO", "count": 1, "unit": "TAXON"}]. All 1 retained taxon IDs were resolved against current NCBI identities, including the explicit alias noted for bile. Zero-count omissions are not biological absence; unlike counts are not summed.

### Native status and optional assertions

completeness: supported. Targets: BTO:0000120.

Executed routes reproduce EXACT/SEEDED. No causal or characteristic-presence claim is asserted; missing optional fields are not automatic deficiencies.

## Findings

### F1: NZ-RLO1 association lacks support in the inspected cell-line sources

major / open / provisional; issue key: bhk-21-cell-nzrlo-pair-support.

Trace the original PREGO evidence for taxon 1810840. GenBank links NZ-RLO1 to the EPC-based genome announcement; the BHK-21 growth abstract concerns NZ-RLO2. Preserve this strain distinction without asserting absence from every other experiment. Correct or qualify only after recovery of pair evidence through a governed source contract; never manually decrement source totals.

## Recommended Actions And Acceptance Checks

### ACT1

Trace the original PREGO evidence for taxon 1810840. GenBank links NZ-RLO1 to the EPC-based genome announcement; the BHK-21 growth abstract concerns NZ-RLO2. Preserve this strain distinction without asserting absence from every other experiment. Correct or qualify only after recovery of pair evidence through a governed source contract; never manually decrement source totals. No repair is performed by this review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history. Do not change source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/bhk_21_cell.yaml; Entire YAML | supports | Complete target read, including source paths, fields, taxa and history. |
| ERULE | docs/CURATION.md; Habitat identity, strictly broader parents and owner boundaries | supports | Whole hosts differ from associated environments; context and part-of links must not be asserted as broader habitat classes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation, parent_habitats, xrefs and CharacteristicTaxon | supports | Mapping endpoints, broader parents and reported versus characteristic presence are distinct. |
| ESEED | src/habitatmech/seed.py; Executed native routes | supports | Resolution results: [{"source": "PREGO", "mint": "habitatmech:PREGO.7353a649d9", "automatic": {"identifier": "BTO:0000120", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "BTO:0000120", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}}] |
| EEXTRACT | src/habitatmech/extract.py; extract_prego | supports | Distinct pairs, maximum scores/channels, score/directness/ID ordering and full taxon pool are retained; original pair citations are not emitted. |
| ET5 | data/raw/prego_habitat_taxa.tsv; TSV physical rows 83 | supports | [{"row": 83, "data": {"prego_id": "BTO:0000120", "rank": "1", "taxon_id": "NCBITaxon:1810840", "taxon_label": "Piscirickettsiaceae bacterium NZ-RLO1", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}] |
| ET6 | data/raw/prego_habitats.tsv; TSV physical rows 532 | supports | [{"row": 532, "data": {"prego_id": "BTO:0000120", "ontology": "BTO", "biolink_category": "biolink:GrossAnatomicalStructure", "taxon_count": "1", "direct_assertion_count": "1", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms": "BHK-21 cell&#124;BHK-21/C13 cell&#124;baby hamster kidney cell&#124;baby hamster kidney cells&#124;bhk21&#124;bhk21 cell line&#124;bhk21 cell lines&#124;bhk21 cells"}}] |
| ET7 | data/raw/ontology_subclass_edges.tsv; TSV physical rows 90,762 | supports | [{"row": 90, "data": {"subject": "BTO:0000120", "predicate": "rdfs:subClassOf", "object": "BTO:0001131"}}, {"row": 762, "data": {"subject": "BTO:0001131", "predicate": "rdfs:subClassOf", "object": "BTO:0000067"}}] |
| ET8 | data/raw/ontology_terms.tsv; TSV physical rows 122,1132 | supports | [{"row": 122, "data": {"term_id": "BTO:0000120", "ontology": "BTO", "label": "BHK-21 cell", "definition": "Syrian hamster kidney BHK-21 is a subclone (clone 13) of the parental line established from the kidneys of five unsexed, one-day-old hamsters in 1961; cells can be used for virus replication studies.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}, {"row": 1132, "data": {"term_id": "BTO:0001131", "ontology": "BTO", "label": "BHK cell", "definition": "Baby hamster kidney cell line.", "synonyms": "", "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}}] |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000120/graph; Current identity, definition and typed relations | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0000120", "target": "http://purl.obolibrary.org/obo/BTO_0001131", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000120; Current identity, definition and typed relations | supports | BTO:0000120 BHK-21 cell; inspected definition: ["Syrian hamster kidney BHK-21 is a subclone (clone 13) of the parental line established from the kidneys of five unsexed, one-day-old hamsters in 1961; cells can be used for virus replication studies."] |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001131/graph; Current identity, definition and typed relations | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0001131", "target": "http://purl.obolibrary.org/obo/BTO_0000067", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001131; Current identity, definition and typed relations | supports | BTO:0001131 BHK cell; inspected definition: ["Baby hamster kidney cell line."] |
| EX5 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4929508/fullTextXML; Genome announcement: isolation and accession paragraph | supports | PMID:27365345; DOI:10.1128/genomeA.00503-16. The NZ-RLO isolate from Chinook-salmon kidney was grown in EPC cells and subsequently on blood cysteine heart agar. The paper identifies WGS accession LVCQ00000000; BHK-21 is not the described isolation cell line. |
| EX6 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=LVCQ01000068&amp;rettype=gb&amp;retmode=xml&amp;seq_start=1&amp;seq_stop=1; LVCQ01000068.1 source qualifiers, comment and cited publication | supports | The one-base source-feature request links LVCQ01000068.1 to strain NZ-RLO1, taxon:1810840, Chinook-salmon host and PMID:27365345. Its comment records the 2018 rename from NZ-RLO to NZ-RLO1. It supplies identity linkage, not proof of every culture association. |
| EX7 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:29806079%20AND%20SRC:MED&amp;format=json&amp;resultType=core; Primary abstract and identifier metadata | supports | PMID:29806079; DOI:10.1111/jfd.12817. NZ-RLO2 grew in BHK-21 and other cell lines; the abstract explicitly distinguishes it genetically from NZ-RLO1. This does not exclude a different NZ-RLO1 experiment. |
| EX8 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1000561,1110546,1123317,1177117,1191475,1233262,1236904,1238993,1257037,1257038,1257039,1257040,1257041,1257042,1280,1283,1292046,1321369,1367494,137591,1392869,1408271,1408272,1408273,1408274,1810840,257758,282199,440512,470&amp;retmode=xml; Exact TaxId, aliases, ScientificName, rank and lineage | supports | [{"id": "NCBITaxon:1810840", "label": "Piscirickettsiaceae bacterium NZ-RLO1", "current_id": "1810840", "current_name": "Piscirickettsiaceae bacterium NZ-RLO1", "current_rank": "species", "lineage": "cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Thiotrichales; Piscirickettsiaceae; unclassified Piscirickettsiaceae"}] |
| ESEARCH | Local maintained inputs and archive; rg --no-ignore --hidden -l -F -e BTO:0000120 -e 'BHK-21 cell' -e bhk_21_cell -e habitatmech:PREGO.7353a649d9 curation history research reports data/raw build reviews | context_only | Ignored-inclusive identifier/label/slug traversal plus exact TSV parsing found the stated source rows and no structured predecessor. |
| EPREGOSEARCH | Configured kg-microbe checkout; find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe -type f -path '*/prego/*' -name '*.tsv' | context_only | No PREGO TSV payload was found in this configured checkout; frozen HabitatMech projections remain available. This is not an upstream or global absence claim. |

## Limits And Additional Notes

- Only the identified source passages were assessed; every historical specimen or PREGO pair has not been independently verified.
- Counts, score and rank are not prevalence, viability, mechanism or characteristic presence. Parent observations are not inherited.
- Configured label correspondence skipped 2,061 pairs without adapters; this is not whole-corpus semantic certification.
- Exact-revision baseline full QC is remote evidence, not a new local QC execution. Post-save archive validation is a subsequent gate.
- iModulonDB is not applicable because no gene, regulator or expression module is asserted. No paid research or scientific-status promotion was performed.
- Original PREGO pair evidence is unavailable in the configured checkout. Publication comparisons do not reconstruct every source pair or establish its extraction cause.
- All captured local bytes were rechecked against the working tree and the captured Git tree before saving.
- Ignored-inclusive archive traversal found no structured predecessor. Legacy observations are contextual leads, not independent approval or structured lineage.
- This observation precedes any separately authorized curation/publication and does not claim a repair.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T110623Z-bhk_21_cell-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: BHK-21 cell (BTO:0000120)'
started_at: '2026-10-15T10:49:53Z'
finished_at: '2026-10-15T11:06:23Z'
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
summary: 'BTO identifies the clone-13 BHK-21 cell line and its BHK-cell superclass.
  The exact NZ-RLO1 association requires pair-level support: the linked genome publication
  used EPC cells, whereas the inspected BHK-21 growth report concerns genetically
  distinct NZ-RLO2. This is not proof that NZ-RLO1 never occurs in BHK-21.'
source:
  git_revision: 405ef4c51cf7aa4d0d2203aaf392ed5d773a7e87
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
    sha256: e54999803277611372ffbad02a795423dc527822d7e900515f27f8824e6b7367
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 6dc8428e469ce29d5d091ec282d39445d07f11eb090e874de1efbe587a080782
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: 5c9bd23cb0f681e2880ff13d606b0bf4d47d12fbcf73154260da1d795b801cbe
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: b303b863e16eb805932c8e8fe831cdb82b17518d63a8b3ab0f62fef675cd24cc
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
  - path: data/habitats/host_associated/bhk_21_cell.yaml
    sha256: 1e9fc776ac6d0fb4ce3713d07c111f27d79ca50b87233a459cc3e2b95ba9a559
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
- target_id: BTO:0000120
  path: data/habitats/host_associated/bhk_21_cell.yaml
  label: BHK-21 cell
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
  description: Scientific assessment of one exact target at captured revision 405ef4c51cf7aa4d0d2203aaf392ed5d773a7e87.
  selection: Next twenty unreviewed records in corpus path order; this document assesses
    one resolved identifier.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - BTO:0000120
  exclusions:
  - target: Other records and SSSOM/KGX products
    reason: Parent context informs hierarchy but is not an additional completed review;
      exports are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/bhk_21_cell.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000120
  summary: "Completed 2026-10-15T10:50:20Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/bhk_21_cell.yaml"
  scope_note: Individual schema, strict validation of twenty targets, other gates
    full-corpus as documented.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/benign_tumor_tissue.yaml data/habitats/host_associated/bhk.yaml
    data/habitats/host_associated/bhk_21_cell.yaml data/habitats/host_associated/bile.yaml
    data/habitats/host_associated/bile__22fc0a7b.yaml data/habitats/host_associated/bile__57dd7796.yaml
    data/habitats/host_associated/bile__612af0df.yaml data/habitats/host_associated/bile__deca6de5.yaml
    data/habitats/host_associated/bile_duct.yaml data/habitats/host_associated/biliary_tract.yaml
    data/habitats/host_associated/biliary_tract__076692f7.yaml data/habitats/host_associated/biliary_tract__7bf9e820.yaml
    data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml data/habitats/host_associated/biliary_tract__d5e0bd1d.yaml
    data/habitats/host_associated/biliary_tract__e6019127.yaml data/habitats/host_associated/biocrust.yaml
    data/habitats/host_associated/biofilm.yaml data/habitats/host_associated/biofilm__465616a5.yaml
    data/habitats/host_associated/birds.yaml data/habitats/host_associated/bivalves.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000120
  summary: "Completed 2026-10-15T10:52:03Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/benign_tumor_tissue.yaml data/habitats/host_associated/bhk.yaml\
    \ data/habitats/host_associated/bhk_21_cell.yaml data/habitats/host_associated/bile.yaml\
    \ data/habitats/host_associated/bile__22fc0a7b.yaml data/habitats/host_associated/bile__57dd7796.yaml\
    \ data/habitats/host_associated/bile__612af0df.yaml data/habitats/host_associated/bile__deca6de5.yaml\
    \ data/habitats/host_associated/bile_duct.yaml data/habitats/host_associated/biliary_tract.yaml\
    \ data/habitats/host_associated/biliary_tract__076692f7.yaml data/habitats/host_associated/biliary_tract__7bf9e820.yaml\
    \ data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml data/habitats/host_associated/biliary_tract__d5e0bd1d.yaml\
    \ data/habitats/host_associated/biliary_tract__e6019127.yaml data/habitats/host_associated/biocrust.yaml\
    \ data/habitats/host_associated/biofilm.yaml data/habitats/host_associated/biofilm__465616a5.yaml\
    \ data/habitats/host_associated/birds.yaml data/habitats/host_associated/bivalves.yaml\n\
    Validating 20 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      20\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Individual schema, strict validation of twenty targets, other gates
    full-corpus as documented.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000120
  summary: 'Completed 2026-10-15T10:52:45Z. No issues found

    789 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Individual schema, strict validation of twenty targets, other gates
    full-corpus as documented.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000120
  summary: "Completed 2026-10-15T10:52:46Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Individual schema, strict validation of twenty targets, other gates
    full-corpus as documented.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000120
  summary: "Completed 2026-10-15T10:53:13Z. expected 3208 records, found 3208 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Individual schema, strict validation of twenty targets, other gates
    full-corpus as documented.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000120
  summary: "Completed 2026-10-15T10:53:20Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Individual schema, strict validation of twenty targets, other gates
    full-corpus as documented.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000120
  summary: "Completed 2026-10-15T10:53:50Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Individual schema, strict validation of twenty targets, other gates
    full-corpus as documented.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000120
  summary: "Completed 2026-10-15T10:55:12Z. id↔label correspondence summary:\n   \
    \       OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Individual schema, strict validation of twenty targets, other gates
    full-corpus as documented.
- check_id: CCI
  name: Baseline full native QC
  status: passed
  required: true
  command: gh run view 38722329263 --json status,conclusion,headSha,url,jobs
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000120
  summary: Exact-revision full QC and structured review contract succeeded; verified
    2026-10-15T11:05:49Z. https://github.com/CultureBotAI/HabitatMech/actions/runs/38722329263
  scope_note: Remote baseline, not a new local QC execution.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/bhk_21_cell.yaml
  locator: Entire YAML
  accessed_at: '2026-10-15T11:06:22Z'
  support: supports
  summary: Complete target read, including source paths, fields, taxa and history.
  snapshot_sha256: 1e9fc776ac6d0fb4ce3713d07c111f27d79ca50b87233a459cc3e2b95ba9a559
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Habitat identity, strictly broader parents and owner boundaries
  accessed_at: '2026-10-15T11:06:22Z'
  support: supports
  summary: Whole hosts differ from associated environments; context and part-of links
    must not be asserted as broader habitat classes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation, parent_habitats, xrefs and CharacteristicTaxon
  accessed_at: '2026-10-15T11:06:22Z'
  support: supports
  summary: Mapping endpoints, broader parents and reported versus characteristic presence
    are distinct.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native routes
  accessed_at: '2026-10-15T11:06:22Z'
  support: supports
  summary: 'Resolution results: [{"source": "PREGO", "mint": "habitatmech:PREGO.7353a649d9",
    "automatic": {"identifier": "BTO:0000120", "grounding_status": "EXACT", "mapping_predicate":
    null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route":
    "prego_self_grounded", "category": null, "reviewed": false, "decision": null},
    "final": {"identifier": "BTO:0000120", "grounding_status": "EXACT", "mapping_predicate":
    null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route":
    "prego_self_grounded", "category": null, "reviewed": false, "decision": null}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: extract_prego
  accessed_at: '2026-10-15T11:06:22Z'
  support: supports
  summary: Distinct pairs, maximum scores/channels, score/directness/ID ordering and
    full taxon pool are retained; original pair citations are not emitted.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/prego_habitat_taxa.tsv
  locator: TSV physical rows 83
  accessed_at: '2026-10-15T11:06:22Z'
  support: supports
  summary: '[{"row": 83, "data": {"prego_id": "BTO:0000120", "rank": "1", "taxon_id":
    "NCBITaxon:1810840", "taxon_label": "Piscirickettsiaceae bacterium NZ-RLO1", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}]'
  snapshot_sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
- evidence_id: ET6
  kind: database
  reference: data/raw/prego_habitats.tsv
  locator: TSV physical rows 532
  accessed_at: '2026-10-15T11:06:22Z'
  support: supports
  summary: '[{"row": 532, "data": {"prego_id": "BTO:0000120", "ontology": "BTO", "biolink_category":
    "biolink:GrossAnatomicalStructure", "taxon_count": "1", "direct_assertion_count":
    "1", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms":
    "BHK-21 cell|BHK-21/C13 cell|baby hamster kidney cell|baby hamster kidney cells|bhk21|bhk21
    cell line|bhk21 cell lines|bhk21 cells"}}]'
  snapshot_sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
- evidence_id: ET7
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV physical rows 90,762
  accessed_at: '2026-10-15T11:06:22Z'
  support: supports
  summary: '[{"row": 90, "data": {"subject": "BTO:0000120", "predicate": "rdfs:subClassOf",
    "object": "BTO:0001131"}}, {"row": 762, "data": {"subject": "BTO:0001131", "predicate":
    "rdfs:subClassOf", "object": "BTO:0000067"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET8
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV physical rows 122,1132
  accessed_at: '2026-10-15T11:06:22Z'
  support: supports
  summary: '[{"row": 122, "data": {"term_id": "BTO:0000120", "ontology": "BTO", "label":
    "BHK-21 cell", "definition": "Syrian hamster kidney BHK-21 is a subclone (clone
    13) of the parental line established from the kidneys of five unsexed, one-day-old
    hamsters in 1961; cells can be used for virus replication studies.", "synonyms":
    "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}},
    {"row": 1132, "data": {"term_id": "BTO:0001131", "ontology": "BTO", "label": "BHK
    cell", "definition": "Baby hamster kidney cell line.", "synonyms": "", "deprecated":
    "", "directly_referenced": "FALSE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EX1
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000120/graph
  locator: Current identity, definition and typed relations
  accessed_at: '2026-10-15T10:52:16Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0000120",
    "target": "http://purl.obolibrary.org/obo/BTO_0001131", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: 171879b2325ecdffcd8fbd005f07635fffc018c1908ea4b52c68693debb84cb1
- evidence_id: EX2
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000120
  locator: Current identity, definition and typed relations
  accessed_at: '2026-10-15T10:52:15Z'
  support: supports
  summary: 'BTO:0000120 BHK-21 cell; inspected definition: ["Syrian hamster kidney
    BHK-21 is a subclone (clone 13) of the parental line established from the kidneys
    of five unsexed, one-day-old hamsters in 1961; cells can be used for virus replication
    studies."]'
  snapshot_sha256: 5ca5f8de3e75eddb771dd8c516774d24a4af74ed7e9e3fccbc2be2c60a0619c7
- evidence_id: EX3
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001131/graph
  locator: Current identity, definition and typed relations
  accessed_at: '2026-10-15T10:52:25Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0001131",
    "target": "http://purl.obolibrary.org/obo/BTO_0000067", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: d3bca2845574b7a885ecb4aa814dcfbb36e114e6aad9dad996dcd25534463a0a
- evidence_id: EX4
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001131
  locator: Current identity, definition and typed relations
  accessed_at: '2026-10-15T10:52:24Z'
  support: supports
  summary: 'BTO:0001131 BHK cell; inspected definition: ["Baby hamster kidney cell
    line."]'
  snapshot_sha256: 8dc776213eecd00de354b58a8e9a97db13f08b4659d0915bc5869fda0990b452
- evidence_id: EX5
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4929508/fullTextXML
  locator: 'Genome announcement: isolation and accession paragraph'
  accessed_at: '2026-10-15T10:56:37Z'
  support: supports
  summary: PMID:27365345; DOI:10.1128/genomeA.00503-16. The NZ-RLO isolate from Chinook-salmon
    kidney was grown in EPC cells and subsequently on blood cysteine heart agar. The
    paper identifies WGS accession LVCQ00000000; BHK-21 is not the described isolation
    cell line.
  snapshot_sha256: 95323c0d8dc463f685a0836f26060428f26d703e1d22668a28af229b03d32f15
- evidence_id: EX6
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=LVCQ01000068&rettype=gb&retmode=xml&seq_start=1&seq_stop=1
  locator: LVCQ01000068.1 source qualifiers, comment and cited publication
  accessed_at: '2026-10-15T10:56:47Z'
  support: supports
  summary: The one-base source-feature request links LVCQ01000068.1 to strain NZ-RLO1,
    taxon:1810840, Chinook-salmon host and PMID:27365345. Its comment records the
    2018 rename from NZ-RLO to NZ-RLO1. It supplies identity linkage, not proof of
    every culture association.
  snapshot_sha256: 21365769482f6aad8d0d29c6eff295956e44cb094c9f5f49e83f80ab800f83e6
- evidence_id: EX7
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:29806079%20AND%20SRC:MED&format=json&resultType=core
  locator: Primary abstract and identifier metadata
  accessed_at: '2026-10-15T10:55:32Z'
  support: supports
  summary: PMID:29806079; DOI:10.1111/jfd.12817. NZ-RLO2 grew in BHK-21 and other
    cell lines; the abstract explicitly distinguishes it genetically from NZ-RLO1.
    This does not exclude a different NZ-RLO1 experiment.
  snapshot_sha256: f5bc5bdc69640e802b474aef66c6b431c287a3565824e77bb3259134430c08b4
- evidence_id: EX8
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1000561,1110546,1123317,1177117,1191475,1233262,1236904,1238993,1257037,1257038,1257039,1257040,1257041,1257042,1280,1283,1292046,1321369,1367494,137591,1392869,1408271,1408272,1408273,1408274,1810840,257758,282199,440512,470&retmode=xml
  locator: Exact TaxId, aliases, ScientificName, rank and lineage
  accessed_at: '2026-10-15T10:52:57Z'
  support: supports
  summary: '[{"id": "NCBITaxon:1810840", "label": "Piscirickettsiaceae bacterium NZ-RLO1",
    "current_id": "1810840", "current_name": "Piscirickettsiaceae bacterium NZ-RLO1",
    "current_rank": "species", "lineage": "cellular organisms; Bacteria; Pseudomonadati;
    Pseudomonadota; Gammaproteobacteria; Thiotrichales; Piscirickettsiaceae; unclassified
    Piscirickettsiaceae"}]'
  snapshot_sha256: c0e0525844dde33d0c1309b8876344c9404ef26c8769b279c3b5aae5f5a2a5df
- evidence_id: ESEARCH
  kind: search
  reference: Local maintained inputs and archive
  locator: rg --no-ignore --hidden -l -F -e BTO:0000120 -e 'BHK-21 cell' -e bhk_21_cell
    -e habitatmech:PREGO.7353a649d9 curation history research reports data/raw build
    reviews
  accessed_at: '2026-10-15T10:51:11Z'
  support: context_only
  summary: Ignored-inclusive identifier/label/slug traversal plus exact TSV parsing
    found the stated source rows and no structured predecessor.
  search_scope: curation, history, research, reports, data/raw, build and reviews;
    all structured review.yaml files traversed independently of gitignore.
- evidence_id: EPREGOSEARCH
  kind: search
  reference: Configured kg-microbe checkout
  locator: find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe
    -type f -path '*/prego/*' -name '*.tsv'
  accessed_at: '2026-10-15T10:51:19Z'
  support: context_only
  summary: No PREGO TSV payload was found in this configured checkout; frozen HabitatMech
    projections remain available. This is not an upstream or global absence claim.
  search_scope: All prego-directory TSV files under the configured checkout, including
    ignored and hidden files.
assessments:
- assessment_id: A1
  area: schema
  topic: Native validity and reproduction
  outcome: supported
  summary: Individual schema, twenty-target strict validation, 789 history records,
    14 inventories/two GOLD sources, 3,208-record reproduction, 32 overlays and 110
    term requests passed. These are deterministic rather than scientific certification.
  target_ids:
  - BTO:0000120
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Identity, hierarchy and alias scope
  outcome: concern
  summary: 'BTO identifies the clone-13 BHK-21 cell line and its BHK-cell superclass.
    The exact NZ-RLO1 association requires pair-level support: the linked genome publication
    used EPC cells, whereas the inspected BHK-21 growth report concerns genetically
    distinct NZ-RLO2. This is not proof that NZ-RLO1 never occurs in BHK-21.'
  target_ids:
  - BTO:0000120
  evidence_ids:
  - E1
  - ERULE
  - ESEED
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
- assessment_id: A3
  area: quantity
  topic: Counts, units and ranking
  outcome: supported
  summary: 'Exact source rows reproduce [{"source": "PREGO", "count": 1, "unit": "TAXON"}].
    All 1 retained taxon IDs were resolved against current NCBI identities, including
    the explicit alias noted for bile. Zero-count omissions are not biological absence;
    unlike counts are not summed.'
  target_ids:
  - BTO:0000120
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
- assessment_id: A4
  area: completeness
  topic: Native status and optional assertions
  outcome: supported
  summary: Executed routes reproduce EXACT/SEEDED. No causal or characteristic-presence
    claim is asserted; missing optional fields are not automatic deficiencies.
  target_ids:
  - BTO:0000120
  evidence_ids:
  - E1
  - ESEED
  - ESCHEMA
findings:
- finding_id: F1
  issue_key: bhk-21-cell-nzrlo-pair-support
  category: evidence
  severity: major
  status: open
  certainty: provisional
  title: NZ-RLO1 association lacks support in the inspected cell-line sources
  description: Trace the original PREGO evidence for taxon 1810840. GenBank links
    NZ-RLO1 to the EPC-based genome announcement; the BHK-21 growth abstract concerns
    NZ-RLO2. Preserve this strain distinction without asserting absence from every
    other experiment. Correct or qualify only after recovery of pair evidence through
    a governed source contract; never manually decrement source totals.
  target_ids:
  - BTO:0000120
  field_paths:
  - characteristic_taxa
  evidence_ids:
  - E1
  - ERULE
  - ESEED
  - ESCHEMA
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
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
  - BTO:0000120
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/MANIFEST.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  description: Trace the original PREGO evidence for taxon 1810840. GenBank links
    NZ-RLO1 to the EPC-based genome announcement; the BHK-21 growth abstract concerns
    NZ-RLO2. Preserve this strain distinction without asserting absence from every
    other experiment. Correct or qualify only after recovery of pair evidence through
    a governed source contract; never manually decrement source totals. No repair
    is performed by this review.
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
- Only the identified source passages were assessed; every historical specimen or
  PREGO pair has not been independently verified.
- Counts, score and rank are not prevalence, viability, mechanism or characteristic
  presence. Parent observations are not inherited.
- Configured label correspondence skipped 2,061 pairs without adapters; this is not
  whole-corpus semantic certification.
- Exact-revision baseline full QC is remote evidence, not a new local QC execution.
  Post-save archive validation is a subsequent gate.
- iModulonDB is not applicable because no gene, regulator or expression module is
  asserted. No paid research or scientific-status promotion was performed.
- Original PREGO pair evidence is unavailable in the configured checkout. Publication
  comparisons do not reconstruct every source pair or establish its extraction cause.
notes:
- All captured local bytes were rechecked against the working tree and the captured
  Git tree before saving.
- Ignored-inclusive archive traversal found no structured predecessor. Legacy observations
  are contextual leads, not independent approval or structured lineage.
- This observation precedes any separately authorized curation/publication and does
  not claim a repair.
tags:
- individual-scientific-review
- host-associated
```
