# Record review: BCP-1 cell (BTO:0002728)

- Review: 20261015T093741Z-bcp_1_cell-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T09:23:48Z
- Finished UTC: 2026-10-15T09:37:41Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

BTO correctly identifies the EBV-negative primary-effusion-lymphoma cell line. Rhodococcus strain BCP1 is a distinct bacterial entity with environmental isolation evidence. The retained species association needs original pair-level context to distinguish a name collision from real cell-line occurrence; the exact extraction error is not established.

## Scope And Provenance

Scientific review of one exact target at bcf6c369a27a5bf1dd9a0156f12f0a61352ff78d.

Selection: Next twenty unreviewed records in corpus path order; this bundle assesses exactly one of their resolved identifiers.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base bcf6c369a27a5bf1dd9a0156f12f0a61352ff78d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0002728 | data/habitats/host_associated/bcp_1_cell.yaml | generated | BCP-1 cell |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0002728 | Completed 2026-10-15T09:24:41Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/bcp_1_cell.yaml |
| validate-strict | passed | True | BTO:0002728 | Completed 2026-10-15T09:25:01Z. uv run python scripts/validate_strict.py data/habitats/host_associated/attached_keratinized_gingiva.yaml data/habitats/host_associated/attached_keratinized_gingiva__a8c3d27a.yaml data/habitats/host_associated/auditory_hearing_system.yaml data/habitats/host_associated/auditory_hearing_system__8fefc879.yaml data/habitats/host_associated/aural.yaml data/habitats/host_associated/autopod_pad.yaml data/habitats/host_associated/autotrophic_anf.yaml data/habitats/host_associated/axilla.yaml data/habitats/host_associated/b_lymphocyte.yaml data/habitats/host_associated/b_lymphocyte_cell_line.yaml data/habitats/host_associated/bacteria.yaml data/habitats/host_associated/bacteria__7bc807fd.yaml data/habitats/host_associated/bacteroid.yaml data/habitats/host_associated/bark.yaml data/habitats/host_associated/bark__5b1d3b9d.yaml data/habitats/host_associated/bartholin_abscess.yaml data/habitats/host_associated/basal_cell_carcinoma.yaml data/habitats/host_associated/bcp_1_cell.yaml data/habitats/host_associated/beaker_s_popliteal_cyst.yaml data/habitats/host_associated/benign_tumor.yaml<br>Validating 20 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      20<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | BTO:0002728 | Completed 2026-10-15T09:25:13Z. No issues found<br>777 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | BTO:0002728 | Completed 2026-10-15T09:25:14Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | BTO:0002728 | Completed 2026-10-15T09:25:35Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | BTO:0002728 | Completed 2026-10-15T09:25:40Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | BTO:0002728 | Completed 2026-10-15T09:26:00Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | BTO:0002728 | Completed 2026-10-15T09:26:58Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-revision baseline full QC | passed | True | BTO:0002728 | Required full native QC and structured-review contract succeeded at the exact captured revision; status checked 2026-10-15T09:25:51Z. https://github.com/CultureBotAI/HabitatMech/actions/runs/38709434919 |

## Scientific And Domain Assessments

### Native validators and reproduction

schema: supported. Targets: BTO:0002728.

Individual schema, twenty-target strict validation, 777 history records, 14 inventories/two GOLD sources, 3,208-record reproduction, 32 overlays and 110 term requests passed. This establishes deterministic fidelity, not scientific validity.

### Identity, definition, hierarchy and synonym scope

identity: concern. Targets: BTO:0002728.

BTO correctly identifies the EBV-negative primary-effusion-lymphoma cell line. Rhodococcus strain BCP1 is a distinct bacterial entity with environmental isolation evidence. The retained species association needs original pair-level context to distinguish a name collision from real cell-line occurrence; the exact extraction error is not established.

### Counts, units and ranking provenance

quantity: supported. Targets: BTO:0002728.

Exact source rows reproduce [{"source": "PREGO", "count": 1, "unit": "TAXON"}]. Every displayed taxon ID/name resolves in NCBI; ranks and pools reproduce the exact habitat-keyed rows. Tied PREGO score/direct flags are ordered by taxon ID, not abundance. Zero tree counts do not imply microbial absence or erase different bulk counts.

### Source status and optional claims

completeness: supported. Targets: BTO:0002728.

Full routes reproduce EXACT/SEEDED. Optional parameter, mechanism and characteristic-presence claims are not asserted and are not required quotas. Source parent counts, triad annotations and adjacent records are not inherited observations.

## Findings

### F1: Retained evidence does not establish cell-site occurrence

major / open / provisional; issue key: bcp-1-cell-prego-occurrence-scope.

Recover the manifest-matching PREGO pair evidence and distinguish occurrence/localization from disease, assay, or name context. BTO correctly identifies the EBV-negative primary-effusion-lymphoma cell line. Rhodococcus strain BCP1 is a distinct bacterial entity with environmental isolation evidence. The retained species association needs original pair-level context to distinguish a name collision from real cell-line occurrence; the exact extraction error is not established. Preserve raw totals and source provenance; any qualified association pool needs an explicit maintained contract, not hand deletion from generated YAML.

## Recommended Actions And Acceptance Checks

### ACT1

Recover the manifest-matching PREGO pair evidence and distinguish occurrence/localization from disease, assay, or name context. BTO correctly identifies the EBV-negative primary-effusion-lymphoma cell line. Rhodococcus strain BCP1 is a distinct bacterial entity with environmental isolation evidence. The retained species association needs original pair-level context to distinguish a name collision from real cell-line occurrence; the exact extraction error is not established. Preserve raw totals and source provenance; any qualified association pool needs an explicit maintained contract, not hand deletion from generated YAML. No repair is performed by this review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history. Do not change source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/bcp_1_cell.yaml; Entire YAML | supports | Read the complete target including source path, fields, taxonomy and generated history. |
| ERULE | docs/CURATION.md; Host identity, broader parents and maintained ownership | supports | Whole organisms cannot identify associated environments; parent_habitats requires strictly broader habitat meaning. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation, parent_habitats, xrefs and CharacteristicTaxon | supports | Source-to-record mapping endpoints, broader habitat relations and observed versus characteristic presence are distinct. |
| ESEED | src/habitatmech/seed.py; Native executed resolution route | supports | Executed native route and final decision: [{"source": "PREGO", "mint": "habitatmech:PREGO.1e308112da", "automatic": {"identifier": "BTO:0002728", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "BTO:0002728", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}}] |
| EEXTRACT | src/habitatmech/extract.py; extract_prego | supports | Projection deduplicates pairs, preserves best score/channel, uses score/directness/taxon-ID order and retains a full distinct-taxon pool. Original pair citations are not emitted into this committed projection. |
| ET5 | data/raw/prego_habitat_taxa.tsv; TSV physical rows 2662 | supports | [{"row": 2662, "data": {"prego_id": "BTO:0002728", "rank": "1", "taxon_id": "NCBITaxon:191292", "taxon_label": "Rhodococcus aetherivorans", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}] |
| ET6 | data/raw/prego_habitats.tsv; TSV physical rows 630 | supports | [{"row": 630, "data": {"prego_id": "BTO:0002728", "ontology": "BTO", "biolink_category": "biolink:GrossAnatomicalStructure", "taxon_count": "1", "direct_assertion_count": "1", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms": "BCP-1 cell"}}] |
| ET7 | data/raw/ontology_subclass_edges.tsv; TSV physical rows 1893,1902 | supports | [{"row": 1893, "data": {"subject": "BTO:0002719", "predicate": "rdfs:subClassOf", "object": "BTO:0001518"}}, {"row": 1902, "data": {"subject": "BTO:0002728", "predicate": "rdfs:subClassOf", "object": "BTO:0002719"}}] |
| ET8 | data/raw/ontology_terms.tsv; TSV physical rows 2719,2728 | supports | [{"row": 2719, "data": {"term_id": "BTO:0002719", "ontology": "BTO", "label": "primary effusion lymphoma cell line", "definition": "Primary effusion lymphoma (PEL) is a peculiar type of B cell non-Hodgkin lymphoma (NHL) that has been recently recognized as an individual clinico-pathologic category based on the consistent infection of the tumor clone by human herpesvirus type-8 (HHV-8) and the distinctiveness of its clinical and biologic features. Although immunogenotypic studies have confirmed that PEL belongs in all cases to the B cell lineage, the overwhelming majority of cases exhibit a non-B, non-T (ie indeterminate) phenotype, lacking expression of surface immunoglobulins and common B cell associated antigens.", "synonyms": "", "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}}, {"row": 2728, "data": {"term_id": "BTO:0002728", "ontology": "BTO", "label": "BCP-1 cell", "definition": "EBV negative PEL cell line.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}] |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0002719/graph; Canonical term identity, definition and explicit relation types | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0002719", "target": "http://purl.obolibrary.org/obo/BTO_0001518", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0002719; Canonical term identity, definition and explicit relation types | supports | BTO:0002719 primary effusion lymphoma cell line; inspected definition and typed scope. ["Primary effusion lymphoma (PEL) is a peculiar type of B cell non-Hodgkin lymphoma (NHL) that has been recently recognized as an individual clinico-pathologic category based on the consistent infection of the tumor clone by human herpesvirus type-8 (HHV-8) and the distinctiveness of its clinical and biologic features. Although immunogenotypic studies have confirmed that PEL belongs in all cases to the B cell lineage, the overwhelming majority of cases exhibit a non-B, non-T (ie indeterminate) phenotype, lacking expression of surface immunoglobulins and common B cell associated antigens."] |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0002728/graph; Canonical term identity, definition and explicit relation types | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0002728", "target": "http://purl.obolibrary.org/obo/BTO_0002719", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0002728; Canonical term identity, definition and explicit relation types | supports | BTO:0002728 BCP-1 cell; inspected definition and typed scope. ["EBV negative PEL cell line."] |
| EX5 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4591350/fullTextXML; Introduction: source consortium; genome sequencing methods | supports | DOI:10.1371/journal.pone.0139467. Rhodococcus sp. BCP1 was selected from an aerobic butane-utilizing consortium and is DSM44980. This bacterial strain is not the human BCP-1 cell line; the paper does not establish the retained species-to-cell-line association. |
| EX6 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML; Section 2.3: BioProject-associated abstracts | supports | PMID:35208748; DOI:10.3390/microorganisms10020293. The annotated-genomes channel includes text-mined associations from abstracts linked to genome-sequencing BioProjects, assigned score three of five. That channel is not exclusively direct isolation-site evidence. |
| EX7 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=NZ_CM002177.1&amp;rettype=gb&amp;retmode=xml&amp;seq_start=1&amp;seq_stop=1; NZ_CM002177.1 source qualifiers; one-base request bounds payload | supports | The current GenBank source identifies Rhodococcus aetherivorans strain BCP1, taxon:191292, isolated from chlorinated-solvent-contaminated sediment in Italy. This agrees with environmental strain context, not BCP-1 human cell-line identity. |
| EX8 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1133849,114615,1245469,1359,191292,2,375177,438753,592205&amp;retmode=xml; TaxId, ScientificName, Rank, Lineage and aliases | supports | [{"id": "NCBITaxon:191292", "label": "Rhodococcus aetherivorans", "current_id": "191292", "current_name": "Rhodococcus aetherivorans", "current_rank": "species", "lineage": "cellular organisms; Bacteria; Bacillati; Actinomycetota; Actinomycetes; Mycobacteriales; Nocardiaceae; Rhodococcus"}] |
| ESEARCH | Local records and maintained inputs; rg --no-ignore --hidden -l -F -e BTO:0002728 -e 'BCP-1 cell' -e bcp_1_cell -e habitatmech:PREGO.1e308112da curation history research reports data/raw build reviews | context_only | Identifier, label, slug and minted-source search includes hidden and ignored files; parsed structured archive traversal found no target predecessor. Broad text hits are not treated as exact source associations. |
| ELEGACY | reports/yaml_record_review/20261004T112152Z-bcp_1_cell.md; Historical target review, especially findings and evidence leads | supports | Historical assessment was consulted for source and issue leads; current findings are independently reassessed against the captured inputs and stated authorities. It is not structured predecessor lineage. |
| EPREGOSEARCH | Configured upstream kg-microbe checkout; find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe -type f -path '*/prego/*' -name '*.tsv' | context_only | No PREGO TSV payload found by the successful filesystem traversal of the configured checkout, including ignored files. Frozen HabitatMech projections remain available; absence elsewhere is not asserted. |

## Limits And Additional Notes

- Source counts, PREGO scores and rank are not prevalence, viability, mechanism or characteristic presence. Every historical specimen has not been independently reidentified.
- Configured label correspondence skipped 2,061 pairs without adapters; it is not full identifier or semantic certification.
- Baseline full QC is exact-revision CI evidence, not a new local full-QC execution. The post-save archive gate is subsequent and is not claimed passed inside this observation.
- Only stated source passages were assessed. Historical reports provide leads, not independent approval; optional empty fields do not create automatic deficiencies.
- iModulonDB is not applicable because the target asserts no gene, regulator or expression module. No paid research, curation, native-status promotion or GitHub mutation was performed.
- Original PREGO pair citations were unavailable in the configured checkout. Primary comparison sources establish bounded interpretations, not a reconstruction of the unobserved upstream extraction or proof of biological absence.
- Fresh captures were made at current main after the previous publication; earlier scratch captures were not refreshed or reused as provenance.
- All captured bytes match both current files and the exact Git revision. The extractor has a separate native supplemental capture.
- Ignored-inclusive traversal found no structured predecessor targeting this identifier. Legacy Markdown observations are contextual; no earlier structured finding is silently closed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T093741Z-bcp_1_cell-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: BCP-1 cell (BTO:0002728)'
started_at: '2026-10-15T09:23:48Z'
finished_at: '2026-10-15T09:37:41Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent performed evidence inspection; not independent human
    or second-agent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: BTO correctly identifies the EBV-negative primary-effusion-lymphoma cell
  line. Rhodococcus strain BCP1 is a distinct bacterial entity with environmental
  isolation evidence. The retained species association needs original pair-level context
  to distinguish a name collision from real cell-line occurrence; the exact extraction
  error is not established.
source:
  git_revision: bcf6c369a27a5bf1dd9a0156f12f0a61352ff78d
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
    sha256: ee710783b625e34dcfa822afab0008e4bfe6b2daf3224b5f804fe569dccb26fb
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 5a794902f1338c3206cb43900e310ef7d573fcbff61da4a01d77bb43b6677c48
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: 6af1d1e372e4400f3caf58808eeb508d3436c2ee1ae7a897c4a23e434093d455
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: 70656ba3c46b4d72fd44cb0ef83322c2c4591edbc3501a9fb7d1497aaeab67a6
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
  - path: data/habitats/host_associated/bcp_1_cell.yaml
    sha256: fa39844d3778e701aed222ea61756bb23c62b525f9092f66446d3e1c4b56c91a
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
  - path: reports/yaml_record_review/20261004T112152Z-bcp_1_cell.md
    sha256: 269f2aa0ec749cc346f2f869cc1a6b6fc3190ee36179000bd0e0608c783c5a31
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
- target_id: BTO:0002728
  path: data/habitats/host_associated/bcp_1_cell.yaml
  label: BCP-1 cell
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
  description: Scientific review of one exact target at bcf6c369a27a5bf1dd9a0156f12f0a61352ff78d.
  selection: Next twenty unreviewed records in corpus path order; this bundle assesses
    exactly one of their resolved identifiers.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - BTO:0002728
  exclusions:
  - target: Other records, exports and parent-record reviews
    reason: Parent context informs this review but is not counted as additional reviewed
      coverage; SSSOM/KGX readiness is not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/bcp_1_cell.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0002728
  summary: "Completed 2026-10-15T09:24:41Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/bcp_1_cell.yaml"
  scope_note: Individual schema; strict validation names all twenty targets; other
    native gates have documented full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/attached_keratinized_gingiva.yaml data/habitats/host_associated/attached_keratinized_gingiva__a8c3d27a.yaml
    data/habitats/host_associated/auditory_hearing_system.yaml data/habitats/host_associated/auditory_hearing_system__8fefc879.yaml
    data/habitats/host_associated/aural.yaml data/habitats/host_associated/autopod_pad.yaml
    data/habitats/host_associated/autotrophic_anf.yaml data/habitats/host_associated/axilla.yaml
    data/habitats/host_associated/b_lymphocyte.yaml data/habitats/host_associated/b_lymphocyte_cell_line.yaml
    data/habitats/host_associated/bacteria.yaml data/habitats/host_associated/bacteria__7bc807fd.yaml
    data/habitats/host_associated/bacteroid.yaml data/habitats/host_associated/bark.yaml
    data/habitats/host_associated/bark__5b1d3b9d.yaml data/habitats/host_associated/bartholin_abscess.yaml
    data/habitats/host_associated/basal_cell_carcinoma.yaml data/habitats/host_associated/bcp_1_cell.yaml
    data/habitats/host_associated/beaker_s_popliteal_cyst.yaml data/habitats/host_associated/benign_tumor.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0002728
  summary: "Completed 2026-10-15T09:25:01Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/attached_keratinized_gingiva.yaml data/habitats/host_associated/attached_keratinized_gingiva__a8c3d27a.yaml\
    \ data/habitats/host_associated/auditory_hearing_system.yaml data/habitats/host_associated/auditory_hearing_system__8fefc879.yaml\
    \ data/habitats/host_associated/aural.yaml data/habitats/host_associated/autopod_pad.yaml\
    \ data/habitats/host_associated/autotrophic_anf.yaml data/habitats/host_associated/axilla.yaml\
    \ data/habitats/host_associated/b_lymphocyte.yaml data/habitats/host_associated/b_lymphocyte_cell_line.yaml\
    \ data/habitats/host_associated/bacteria.yaml data/habitats/host_associated/bacteria__7bc807fd.yaml\
    \ data/habitats/host_associated/bacteroid.yaml data/habitats/host_associated/bark.yaml\
    \ data/habitats/host_associated/bark__5b1d3b9d.yaml data/habitats/host_associated/bartholin_abscess.yaml\
    \ data/habitats/host_associated/basal_cell_carcinoma.yaml data/habitats/host_associated/bcp_1_cell.yaml\
    \ data/habitats/host_associated/beaker_s_popliteal_cyst.yaml data/habitats/host_associated/benign_tumor.yaml\n\
    Validating 20 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      20\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Individual schema; strict validation names all twenty targets; other
    native gates have documented full-corpus scope.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0002728
  summary: 'Completed 2026-10-15T09:25:13Z. No issues found

    777 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Individual schema; strict validation names all twenty targets; other
    native gates have documented full-corpus scope.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0002728
  summary: "Completed 2026-10-15T09:25:14Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Individual schema; strict validation names all twenty targets; other
    native gates have documented full-corpus scope.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0002728
  summary: "Completed 2026-10-15T09:25:35Z. expected 3208 records, found 3208 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Individual schema; strict validation names all twenty targets; other
    native gates have documented full-corpus scope.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0002728
  summary: "Completed 2026-10-15T09:25:40Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Individual schema; strict validation names all twenty targets; other
    native gates have documented full-corpus scope.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0002728
  summary: "Completed 2026-10-15T09:26:00Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Individual schema; strict validation names all twenty targets; other
    native gates have documented full-corpus scope.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0002728
  summary: "Completed 2026-10-15T09:26:58Z. id↔label correspondence summary:\n   \
    \       OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Individual schema; strict validation names all twenty targets; other
    native gates have documented full-corpus scope.
- check_id: CCI
  name: Exact-revision baseline full QC
  status: passed
  required: true
  command: gh run view 38709434919 --json status,conclusion,headSha,url,jobs
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0002728
  summary: Required full native QC and structured-review contract succeeded at the
    exact captured revision; status checked 2026-10-15T09:25:51Z. https://github.com/CultureBotAI/HabitatMech/actions/runs/38709434919
  scope_note: Remote baseline execution; newly saved review outputs require their
    own archive check.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/bcp_1_cell.yaml
  locator: Entire YAML
  accessed_at: '2026-10-15T09:37:41Z'
  support: supports
  summary: Read the complete target including source path, fields, taxonomy and generated
    history.
  snapshot_sha256: fa39844d3778e701aed222ea61756bb23c62b525f9092f66446d3e1c4b56c91a
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, broader parents and maintained ownership
  accessed_at: '2026-10-15T09:37:41Z'
  support: supports
  summary: Whole organisms cannot identify associated environments; parent_habitats
    requires strictly broader habitat meaning.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation, parent_habitats, xrefs and CharacteristicTaxon
  accessed_at: '2026-10-15T09:37:41Z'
  support: supports
  summary: Source-to-record mapping endpoints, broader habitat relations and observed
    versus characteristic presence are distinct.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Native executed resolution route
  accessed_at: '2026-10-15T09:37:41Z'
  support: supports
  summary: 'Executed native route and final decision: [{"source": "PREGO", "mint":
    "habitatmech:PREGO.1e308112da", "automatic": {"identifier": "BTO:0002728", "grounding_status":
    "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents":
    [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed":
    false, "decision": null}, "final": {"identifier": "BTO:0002728", "grounding_status":
    "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents":
    [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed":
    false, "decision": null}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: extract_prego
  accessed_at: '2026-10-15T09:37:41Z'
  support: supports
  summary: Projection deduplicates pairs, preserves best score/channel, uses score/directness/taxon-ID
    order and retains a full distinct-taxon pool. Original pair citations are not
    emitted into this committed projection.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/prego_habitat_taxa.tsv
  locator: TSV physical rows 2662
  accessed_at: '2026-10-15T09:37:41Z'
  support: supports
  summary: '[{"row": 2662, "data": {"prego_id": "BTO:0002728", "rank": "1", "taxon_id":
    "NCBITaxon:191292", "taxon_label": "Rhodococcus aetherivorans", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}]'
  snapshot_sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
- evidence_id: ET6
  kind: database
  reference: data/raw/prego_habitats.tsv
  locator: TSV physical rows 630
  accessed_at: '2026-10-15T09:37:41Z'
  support: supports
  summary: '[{"row": 630, "data": {"prego_id": "BTO:0002728", "ontology": "BTO", "biolink_category":
    "biolink:GrossAnatomicalStructure", "taxon_count": "1", "direct_assertion_count":
    "1", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms":
    "BCP-1 cell"}}]'
  snapshot_sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
- evidence_id: ET7
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV physical rows 1893,1902
  accessed_at: '2026-10-15T09:37:41Z'
  support: supports
  summary: '[{"row": 1893, "data": {"subject": "BTO:0002719", "predicate": "rdfs:subClassOf",
    "object": "BTO:0001518"}}, {"row": 1902, "data": {"subject": "BTO:0002728", "predicate":
    "rdfs:subClassOf", "object": "BTO:0002719"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET8
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV physical rows 2719,2728
  accessed_at: '2026-10-15T09:37:41Z'
  support: supports
  summary: '[{"row": 2719, "data": {"term_id": "BTO:0002719", "ontology": "BTO", "label":
    "primary effusion lymphoma cell line", "definition": "Primary effusion lymphoma
    (PEL) is a peculiar type of B cell non-Hodgkin lymphoma (NHL) that has been recently
    recognized as an individual clinico-pathologic category based on the consistent
    infection of the tumor clone by human herpesvirus type-8 (HHV-8) and the distinctiveness
    of its clinical and biologic features. Although immunogenotypic studies have confirmed
    that PEL belongs in all cases to the B cell lineage, the overwhelming majority
    of cases exhibit a non-B, non-T (ie indeterminate) phenotype, lacking expression
    of surface immunoglobulins and common B cell associated antigens.", "synonyms":
    "", "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}},
    {"row": 2728, "data": {"term_id": "BTO:0002728", "ontology": "BTO", "label": "BCP-1
    cell", "definition": "EBV negative PEL cell line.", "synonyms": "", "deprecated":
    "", "directly_referenced": "TRUE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EX1
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0002719/graph
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:31Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0002719",
    "target": "http://purl.obolibrary.org/obo/BTO_0001518", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: 113da71afe84f6980d2e3a2236192793996d2e61312ec7b5c7dcf85a643f039a
- evidence_id: EX2
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0002719
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:30Z'
  support: supports
  summary: BTO:0002719 primary effusion lymphoma cell line; inspected definition and
    typed scope. ["Primary effusion lymphoma (PEL) is a peculiar type of B cell non-Hodgkin
    lymphoma (NHL) that has been recently recognized as an individual clinico-pathologic
    category based on the consistent infection of the tumor clone by human herpesvirus
    type-8 (HHV-8) and the distinctiveness of its clinical and biologic features.
    Although immunogenotypic studies have confirmed that PEL belongs in all cases
    to the B cell lineage, the overwhelming majority of cases exhibit a non-B, non-T
    (ie indeterminate) phenotype, lacking expression of surface immunoglobulins and
    common B cell associated antigens."]
  snapshot_sha256: 92a92ad92618f5cfc29e0a30cd486bba0d4695efc0d073c23a71282a7a678593
- evidence_id: EX3
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0002728/graph
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:32Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0002728",
    "target": "http://purl.obolibrary.org/obo/BTO_0002719", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: 7421f96e560bcad0af71be761da7a9854496176d270d00acfaf905fa0ca7c9d9
- evidence_id: EX4
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0002728
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:31Z'
  support: supports
  summary: BTO:0002728 BCP-1 cell; inspected definition and typed scope. ["EBV negative
    PEL cell line."]
  snapshot_sha256: c2e23b89c9cd5b25db157710b6fa44bcd66f4881ccee97fd962b6277b7ced22f
- evidence_id: EX5
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4591350/fullTextXML
  locator: 'Introduction: source consortium; genome sequencing methods'
  accessed_at: '2026-10-15T09:27:09Z'
  support: supports
  summary: DOI:10.1371/journal.pone.0139467. Rhodococcus sp. BCP1 was selected from
    an aerobic butane-utilizing consortium and is DSM44980. This bacterial strain
    is not the human BCP-1 cell line; the paper does not establish the retained species-to-cell-line
    association.
  snapshot_sha256: d0598a16278c5a1dc20a012a8c44f113e3a76100ce97cd512dda0c74334c7dce
- evidence_id: EX6
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML
  locator: 'Section 2.3: BioProject-associated abstracts'
  accessed_at: '2026-10-15T09:30:17Z'
  support: supports
  summary: PMID:35208748; DOI:10.3390/microorganisms10020293. The annotated-genomes
    channel includes text-mined associations from abstracts linked to genome-sequencing
    BioProjects, assigned score three of five. That channel is not exclusively direct
    isolation-site evidence.
  snapshot_sha256: 375f0fde4d07bb823cb9106aa4567bc0ef03c2866af0b2a7740b543f50687c25
- evidence_id: EX7
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NZ_CM002177.1&rettype=gb&retmode=xml&seq_start=1&seq_stop=1
  locator: NZ_CM002177.1 source qualifiers; one-base request bounds payload
  accessed_at: '2026-10-15T09:27:34Z'
  support: supports
  summary: The current GenBank source identifies Rhodococcus aetherivorans strain
    BCP1, taxon:191292, isolated from chlorinated-solvent-contaminated sediment in
    Italy. This agrees with environmental strain context, not BCP-1 human cell-line
    identity.
  snapshot_sha256: 163c5a188bab46b85acbcbca9ffaf89f861a545c91a247078d1f5687638f050c
- evidence_id: EX8
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1133849,114615,1245469,1359,191292,2,375177,438753,592205&retmode=xml
  locator: TaxId, ScientificName, Rank, Lineage and aliases
  accessed_at: '2026-10-15T09:26:01Z'
  support: supports
  summary: '[{"id": "NCBITaxon:191292", "label": "Rhodococcus aetherivorans", "current_id":
    "191292", "current_name": "Rhodococcus aetherivorans", "current_rank": "species",
    "lineage": "cellular organisms; Bacteria; Bacillati; Actinomycetota; Actinomycetes;
    Mycobacteriales; Nocardiaceae; Rhodococcus"}]'
  snapshot_sha256: bc5ad6493aa78574a052359add560693971d71c2e08ddbf4357d39c37e8f7b0b
- evidence_id: ESEARCH
  kind: search
  reference: Local records and maintained inputs
  locator: rg --no-ignore --hidden -l -F -e BTO:0002728 -e 'BCP-1 cell' -e bcp_1_cell
    -e habitatmech:PREGO.1e308112da curation history research reports data/raw build
    reviews
  accessed_at: '2026-10-15T09:24:07Z'
  support: context_only
  summary: Identifier, label, slug and minted-source search includes hidden and ignored
    files; parsed structured archive traversal found no target predecessor. Broad
    text hits are not treated as exact source associations.
  search_scope: curation, history, research, reports, data/raw, build and reviews;
    filesystem traversal of every structured review.yaml independent of gitignore.
- evidence_id: ELEGACY
  kind: record_content
  reference: reports/yaml_record_review/20261004T112152Z-bcp_1_cell.md
  locator: Historical target review, especially findings and evidence leads
  accessed_at: '2026-10-15T09:37:41Z'
  support: supports
  summary: Historical assessment was consulted for source and issue leads; current
    findings are independently reassessed against the captured inputs and stated authorities.
    It is not structured predecessor lineage.
  snapshot_sha256: 269f2aa0ec749cc346f2f869cc1a6b6fc3190ee36179000bd0e0608c783c5a31
- evidence_id: EPREGOSEARCH
  kind: search
  reference: Configured upstream kg-microbe checkout
  locator: find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe
    -type f -path '*/prego/*' -name '*.tsv'
  accessed_at: '2026-10-15T09:25:51Z'
  support: context_only
  summary: No PREGO TSV payload found by the successful filesystem traversal of the
    configured checkout, including ignored files. Frozen HabitatMech projections remain
    available; absence elsewhere is not asserted.
  search_scope: All files under /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe
    matching */prego/*.tsv, independent of gitignore.
assessments:
- assessment_id: A1
  area: schema
  topic: Native validators and reproduction
  outcome: supported
  summary: Individual schema, twenty-target strict validation, 777 history records,
    14 inventories/two GOLD sources, 3,208-record reproduction, 32 overlays and 110
    term requests passed. This establishes deterministic fidelity, not scientific
    validity.
  target_ids:
  - BTO:0002728
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and synonym scope
  outcome: concern
  summary: BTO correctly identifies the EBV-negative primary-effusion-lymphoma cell
    line. Rhodococcus strain BCP1 is a distinct bacterial entity with environmental
    isolation evidence. The retained species association needs original pair-level
    context to distinguish a name collision from real cell-line occurrence; the exact
    extraction error is not established.
  target_ids:
  - BTO:0002728
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
  topic: Counts, units and ranking provenance
  outcome: supported
  summary: 'Exact source rows reproduce [{"source": "PREGO", "count": 1, "unit": "TAXON"}].
    Every displayed taxon ID/name resolves in NCBI; ranks and pools reproduce the
    exact habitat-keyed rows. Tied PREGO score/direct flags are ordered by taxon ID,
    not abundance. Zero tree counts do not imply microbial absence or erase different
    bulk counts.'
  target_ids:
  - BTO:0002728
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
  topic: Source status and optional claims
  outcome: supported
  summary: Full routes reproduce EXACT/SEEDED. Optional parameter, mechanism and characteristic-presence
    claims are not asserted and are not required quotas. Source parent counts, triad
    annotations and adjacent records are not inherited observations.
  target_ids:
  - BTO:0002728
  evidence_ids:
  - E1
  - ESEED
  - ESCHEMA
findings:
- finding_id: F1
  issue_key: bcp-1-cell-prego-occurrence-scope
  category: evidence
  severity: major
  status: open
  certainty: provisional
  title: Retained evidence does not establish cell-site occurrence
  description: Recover the manifest-matching PREGO pair evidence and distinguish occurrence/localization
    from disease, assay, or name context. BTO correctly identifies the EBV-negative
    primary-effusion-lymphoma cell line. Rhodococcus strain BCP1 is a distinct bacterial
    entity with environmental isolation evidence. The retained species association
    needs original pair-level context to distinguish a name collision from real cell-line
    occurrence; the exact extraction error is not established. Preserve raw totals
    and source provenance; any qualified association pool needs an explicit maintained
    contract, not hand deletion from generated YAML.
  target_ids:
  - BTO:0002728
  field_paths:
  - characteristic_taxa
  - source_attestations
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
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1374
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - BTO:0002728
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
  description: Recover the manifest-matching PREGO pair evidence and distinguish occurrence/localization
    from disease, assay, or name context. BTO correctly identifies the EBV-negative
    primary-effusion-lymphoma cell line. Rhodococcus strain BCP1 is a distinct bacterial
    entity with environmental isolation evidence. The retained species association
    needs original pair-level context to distinguish a name collision from real cell-line
    occurrence; the exact extraction error is not established. Preserve raw totals
    and source provenance; any qualified association pool needs an explicit maintained
    contract, not hand deletion from generated YAML. No repair is performed by this
    review.
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
- Source counts, PREGO scores and rank are not prevalence, viability, mechanism or
  characteristic presence. Every historical specimen has not been independently reidentified.
- Configured label correspondence skipped 2,061 pairs without adapters; it is not
  full identifier or semantic certification.
- Baseline full QC is exact-revision CI evidence, not a new local full-QC execution.
  The post-save archive gate is subsequent and is not claimed passed inside this observation.
- Only stated source passages were assessed. Historical reports provide leads, not
  independent approval; optional empty fields do not create automatic deficiencies.
- iModulonDB is not applicable because the target asserts no gene, regulator or expression
  module. No paid research, curation, native-status promotion or GitHub mutation was
  performed.
- Original PREGO pair citations were unavailable in the configured checkout. Primary
  comparison sources establish bounded interpretations, not a reconstruction of the
  unobserved upstream extraction or proof of biological absence.
notes:
- Fresh captures were made at current main after the previous publication; earlier
  scratch captures were not refreshed or reused as provenance.
- All captured bytes match both current files and the exact Git revision. The extractor
  has a separate native supplemental capture.
- Ignored-inclusive traversal found no structured predecessor targeting this identifier.
  Legacy Markdown observations are contextual; no earlier structured finding is silently
  closed.
tags:
- individual-scientific-review
- host-associated
```
