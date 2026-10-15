# Record review: CACO-2 cell (BTO:0000195)

- Review: 20261015T193031Z-caco_2_cell-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T19:05:40Z
- Finished UTC: 2026-10-15T19:30:31Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The BTO identity is a human colon-adenocarcinoma-derived cell line, not an intact colon or a diagnosis. Its cell-line superclass is supported. A primary study directly assays B. longum CECT7347 adhesion to Caco-2 cultures, supporting experimental association rather than natural isolation. All four PREGO rows reproduce the source, but not every original pair has been independently traced. Assay exposure alone is not a demonstrated defect under the association schema.

## Scope And Provenance

Full field-by-field scientific assessment of this exact target at a073f8e821a7c095f35501982930cc5a156835c0.

Selection: One of the next 24 path-ordered unreviewed identifiers in an ignored-inclusive 3208-record census. This bundle reviews one identifier, not a sample standing for other targets.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base a073f8e821a7c095f35501982930cc5a156835c0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0000195 | data/habitats/host_associated/caco_2_cell.yaml | generated | CACO-2 cell |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0000195 | Finished 2026-10-15T19:09:29Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/caco_2_cell.yaml |
| validate-strict | passed | True | BTO:0000195 | Finished 2026-10-15T19:10:07Z. uv run python scripts/validate_strict.py data/habitats/host_associated/brown_algae.yaml data/habitats/host_associated/bryophytes.yaml data/habitats/host_associated/bryozoa.yaml data/habitats/host_associated/bryozoans.yaml data/habitats/host_associated/buccal_mucosa.yaml data/habitats/host_associated/buccal_mucosa__62ec5bff.yaml data/habitats/host_associated/buccal_mucosa__a90386db.yaml data/habitats/host_associated/buffy_coat.yaml data/habitats/host_associated/bulb.yaml data/habitats/host_associated/bursa_of_fabricius.yaml data/habitats/host_associated/c1_glandular_saccules.yaml data/habitats/host_associated/c2.yaml data/habitats/host_associated/c3.yaml data/habitats/host_associated/caco_2_cell.yaml data/habitats/host_associated/caeca.yaml data/habitats/host_associated/caeca__67ed138d.yaml data/habitats/host_associated/caeca_bacteriome.yaml data/habitats/host_associated/canidae_dog.yaml data/habitats/host_associated/canthus.yaml data/habitats/host_associated/canthus__f4c2e1df.yaml data/habitats/host_associated/capillary.yaml data/habitats/host_associated/caprinae_sheep_goat.yaml data/habitats/host_associated/carapace.yaml data/habitats/host_associated/carcass.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | BTO:0000195 | Finished 2026-10-15T19:10:18Z. No issues found<br>816 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | BTO:0000195 | Finished 2026-10-15T19:10:19Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | BTO:0000195 | Finished 2026-10-15T19:10:38Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | BTO:0000195 | Finished 2026-10-15T19:10:44Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | BTO:0000195 | Finished 2026-10-15T19:11:04Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | BTO:0000195 | Finished 2026-10-15T19:12:07Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-baseline full QC | passed | True | BTO:0000195 | Verified 2026-10-15T19:04:33Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38786529592 |

## Scientific And Domain Assessments

### Identity, definition, category and broader ancestry

identity: supported. Targets: BTO:0000195.

The BTO identity is a human colon-adenocarcinoma-derived cell line, not an intact colon or a diagnosis. Its cell-line superclass is supported. A primary study directly assays B. longum CECT7347 adhesion to Caco-2 cultures, supporting experimental association rather than natural isolation. All four PREGO rows reproduce the source, but not every original pair has been independently traced. Assay exposure alone is not a demonstrated defect under the association schema.

### Source counts, units, ranks, pools and channels

quantity: supported. Targets: BTO:0000195.

Every attestation and displayed taxon was compared with its exact frozen source row. [{"source": "PREGO", "count": 4, "unit": "TAXON"}]. Side-table biosamples and study memberships are separate from tree ORGANISM counts; zero-count omission is not biological absence.

### Biological support and limits

evidence: supported. Targets: BTO:0000195.

The BTO identity is a human colon-adenocarcinoma-derived cell line, not an intact colon or a diagnosis. Its cell-line superclass is supported. A primary study directly assays B. longum CECT7347 adhesion to Caco-2 cultures, supporting experimental association rather than natural isolation. All four PREGO rows reproduce the source, but not every original pair has been independently traced. Assay exposure alone is not a demonstrated defect under the association schema.

### Curation status, parameters, mechanisms and optional content

completeness: supported. Targets: BTO:0000195.

Executed routes reproduce EXACT/SEEDED. No target environmental parameters, causal edges, discussions/datasets or is_characteristic=true assertions are present. Parent-record mechanisms are not inherited. Optional absence and SEEDED status alone are not defects.

### Native deterministic gates

schema: supported. Targets: BTO:0000195.

Ordinary and strict schema, 816 curation histories, provenance, exact 3208-record reproduction, 32 causal overlays, term requests, configured labels and exact-base QC passed. Deterministic fidelity does not establish biological correctness.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/caco_2_cell.yaml; Entire target YAML | supports | All fields, displayed taxa and complete curation history read. |
| ERULE | docs/CURATION.md; Identity, hierarchy and source-evidence rules | supports | All parent contributions must be strictly broader; host identity is not environment identity. Source occurrences are not automatically characteristic. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; HabitatRecord, SourceAttestation, TaxonAssociation and category enums | supports | Source-to-record mapping endpoints; reported associations versus characteristic assertions; category scope and optional fields. |
| ESEED | src/habitatmech/seed.py; Executed resolution routes, parent accumulation, prefix category and overrides | supports | Exact emitted target reproduction established. Routes: [{"mint": "habitatmech:PREGO.c98b337dc1", "automatic": {"identifier": "BTO:0000195", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "BTO:0000195", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}}] |
| EEXTRACT | src/habitatmech/extract.py; Inventory projection | supports | Counts/units and taxon ranks/scores preserve source meanings. PREGO projections omit original pair-level citation links. |
| ET5 | data/raw/prego_habitat_taxa.tsv; Physical TSV rows 259,260,261,262 | supports | [{"row": 259, "data": {"prego_id": "BTO:0000195", "rank": "1", "taxon_id": "NCBITaxon:1205679", "taxon_label": "Bifidobacterium longum subsp. longum CECT 7347", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 260, "data": {"prego_id": "BTO:0000195", "rank": "2", "taxon_id": "NCBITaxon:1392869", "taxon_label": "Escherichia coli K1", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 261, "data": {"prego_id": "BTO:0000195", "rank": "3", "taxon_id": "NCBITaxon:1580", "taxon_label": "Levilactobacillus brevis", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 262, "data": {"prego_id": "BTO:0000195", "rank": "4", "taxon_id": "NCBITaxon:557433", "taxon_label": "Limosilactobacillus reuteri subsp. reuteri JCM 1112", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}] |
| ET6 | data/raw/prego_habitats.tsv; Physical TSV rows 401 | supports | [{"row": 401, "data": {"prego_id": "BTO:0000195", "ontology": "BTO", "biolink_category": "biolink:GrossAnatomicalStructure", "taxon_count": "4", "direct_assertion_count": "4", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms": "CACO-2 cell&#124;caco2&#124;caco2 cell line&#124;caco2 cell lines&#124;caco2 cells"}}] |
| ET7 | data/raw/ontology_subclass_edges.tsv; Physical TSV rows 141,1294 | supports | [{"row": 141, "data": {"subject": "BTO:0000195", "predicate": "rdfs:subClassOf", "object": "BTO:0001913"}}, {"row": 1294, "data": {"subject": "BTO:0001913", "predicate": "rdfs:subClassOf", "object": "BTO:0000797"}}] |
| ET8 | data/raw/ontology_terms.tsv; Physical TSV rows 197,1913 | supports | [{"row": 197, "data": {"term_id": "BTO:0000195", "ontology": "BTO", "label": "CACO-2 cell", "definition": "Human colon adenocarcinoma cell line, established from the primary colon tumor (adenocarcinoma) of a 72-year-old Caucasian man in 1974.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}, {"row": 1913, "data": {"term_id": "BTO:0001913", "ontology": "BTO", "label": "colonic adenocarcinoma cell line", "definition": "", "synonyms": "", "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}}] |
| ELEGACY | reports/yaml_record_review/20261002T225923Z-caco_2_cell.md; Findings and recommended edits; historical review lead | supports | The earlier major finding was solely absence of a native ITEM REVIEW decision. SEEDED accurately reports that state and is not a scientific error by itself. This qualified review does not create the missing native decision or claim all source pairs independently verified. |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000195/graph; BTO_0000195-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000195", "target": "http://purl.obolibrary.org/obo/BTO_0001913", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000195; BTO_0000195.json | context_only | Current authoritative identity, active status and definition: {"obo_id": "BTO:0000195", "label": "CACO-2 cell", "is_obsolete": false, "description": ["Human colon adenocarcinoma cell line, established from the primary colon tumor (adenocarcinoma) of a 72-year-old Caucasian man in 1974."]} |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001913/graph; BTO_0001913-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0001913", "target": "http://purl.obolibrary.org/obo/BTO_0000797", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001913; BTO_0001913.json | context_only | Current authoritative identity, active status and definition: {"obo_id": "BTO:0001913", "label": "colonic adenocarcinoma cell line", "is_obsolete": false, "description": []} |
| EX5 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML; PMC8879827.xml | context_only | Primary methods section 2.3, PMID:35208748, DOI:10.3390/microorganisms10020293. BioProject-assigned taxa are associated with entities mined from linked abstracts at score three. This source channel does not certify natural isolation, viability, prevalence or characteristic presence. |
| EX6 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22Dietary%20glycosaminoglycans%22&amp;format=json&amp;resultType=core&amp;pageSize=10; paper-caco-cect.json | context_only | Primary abstract PMID:20637226, DOI:10.1016/j.ijbiomac.2010.06.015. Adhesion of B. longum CECT7347 and other named bacteria to mucin and Caco-2 cultures was assayed. This directly supports experimental association for that strain, not original isolation from the cell line or the remaining three PREGO pair citations. |
| EX7 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=100469,1015,108028,1085628,1159213,1163745,1205679,131109,131112,1329,1330043,1334,1392869,1417985,155085,1580,1661,170187,1719,184914,1872627,1962667,197,2,206,243265,243273,28080,28091,28121,28188,283734,28450,28898,29419,317010,326522,33,34,35,38,388919,398527,52770,54,554290,557433,56,562,590061,694433,71864,722,731,753,754,759,75985,760,82806,83456,83462,85336,85401,90240,99807&amp;retmode=xml; taxonomy.xml | context_only | Current NCBI TaxIds, names and source-label comparison: [{"id": "NCBITaxon:1205679", "source": "PREGO", "label": "Bifidobacterium longum subsp. longum CECT 7347", "current_id": "1205679", "current_name": "Bifidobacterium longum subsp. longum CECT 7347", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1392869", "source": "PREGO", "label": "Escherichia coli K1", "current_id": "1392869", "current_name": "Escherichia coli K1", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1580", "source": "PREGO", "label": "Levilactobacillus brevis", "current_id": "1580", "current_name": "Levilactobacillus brevis", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:557433", "source": "PREGO", "label": "Limosilactobacillus reuteri subsp. reuteri JCM 1112", "current_id": "557433", "current_name": "Limosilactobacillus reuteri subsp. reuteri JCM 1112 = DSM 20016", "rank": "strain", "direct_match": false, "recognized_alias": false}]. For taxon557433, current NCBI adds the equivalent DSM20016 strain designation; the retained JCM1112 label is not a wrong identifier. |
| ESEARCH | Maintained inputs and local structured archive; rg --no-ignore --hidden -l -F -e BTO:0000195 -e 'CACO-2 cell' -e caco_2_cell -e habitatmech:PREGO.c98b337dc1 curation history research reports data/raw build reviews | context_only | Exact source/curation rows were parsed separately. No formal target predecessor was found; not every broad label match was inspected. |
| EAVAIL | Configured kg-microbe checkout; find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe -type f -path '*/prego/*' -name '*.tsv' | context_only | No prego-directory TSV files were found in this checkout. Original pair-level citation exports remain unavailable; this is not a global absence claim. |

## Limits And Additional Notes

- Original specimens and every pair-level source citation have not been independently reidentified. Source counts and ranks are not prevalence, viability, or characteristic presence.
- The configured label gate skips 2061 no-adapter pairs. Displayed taxon identities were separately checked against current NCBI Taxonomy, not certified by that label gate.
- Full QC evidence is a successful remote run at the exact unchanged scientific input base, not a new local full-QC execution. New review files require a post-save native archive check.
- iModulonDB is not applicable to these target claims: no gene, regulator, transcriptomic module or causal mechanism is asserted. No paid research was used.
- Original PREGO pair exports are unavailable in the configured checkout. Primary examples do not prove the provenance or truth of every retained pair. Score three remains the source score, not measured localization confidence.
- The CECT7347 adhesion study is positive evidence for one pair only. Current NCBI expands the JCM1112 name with DSM20016; no incorrect TaxId is inferred from the shorter frozen label.
- Current input hashes were checked against both working bytes and exact tracked base blobs; source.state git_commit explicitly describes that revision.
- Ignored-inclusive searches and the parsed structured archive found no previous structured observation targeting this identifier. Broad label matches are leads, not formal lineage or automatic scientific findings.
- Read-only scientific review: no habitat curation, generation, history/status promotion or GitHub mutation is performed.
- The earlier major finding was solely absence of a native ITEM REVIEW decision. SEEDED accurately reports that state and is not a scientific error by itself. This qualified review does not create the missing native decision or claim all source pairs independently verified.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T193031Z-caco_2_cell-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: CACO-2 cell (BTO:0000195)'
started_at: '2026-10-15T19:05:40Z'
finished_at: '2026-10-15T19:30:31Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent assesses the record and sources; not independent
    reviewer approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The BTO identity is a human colon-adenocarcinoma-derived cell line, not an
  intact colon or a diagnosis. Its cell-line superclass is supported. A primary study
  directly assays B. longum CECT7347 adhesion to Caco-2 cultures, supporting experimental
  association rather than natural isolation. All four PREGO rows reproduce the source,
  but not every original pair has been independently traced. Assay exposure alone
  is not a demonstrated defect under the association schema.
source:
  git_revision: a073f8e821a7c095f35501982930cc5a156835c0
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
    sha256: 196d393819145d33f30f7706fd9c5369ed05847d2ccbd9b977a759556ca293fd
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 9344f0bbbad1423ff0e47204ad49bc27ffaf4b5e63841e77e09cc01877b91f54
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: a56f07a45fb743fb7b0e61f83ef70fa5ed61a3c892cfaf36e3428967c548dc5e
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: da5dcc7d49a3441bd9ff25d95ff204ba4e8716cf062271338ee2795ca16a5ce4
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
  - path: data/habitats/host_associated/caco_2_cell.yaml
    sha256: a909a98a4b4f90fc49bbe783b4378ef136f1019932727effba1797103e165808
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
  - path: reports/yaml_record_review/20261002T225923Z-caco_2_cell.md
    sha256: 48d2119ad56a5ad82deb9d2cc918a76f9f6abc3741a8ebbf8d6a517e4ac014ff
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
- target_id: BTO:0000195
  path: data/habitats/host_associated/caco_2_cell.yaml
  label: CACO-2 cell
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
  description: Full field-by-field scientific assessment of this exact target at a073f8e821a7c095f35501982930cc5a156835c0.
  selection: One of the next 24 path-ordered unreviewed identifiers in an ignored-inclusive
    3208-record census. This bundle reviews one identifier, not a sample standing
    for other targets.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - BTO:0000195
  exclusions:
  - target: Other habitats and SSSOM/KGX products
    reason: Parent context is not additional record coverage. Export conformance and
      original individual specimens are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/caco_2_cell.yaml
  exit_code: 0
  target_ids:
  - BTO:0000195
  summary: "Finished 2026-10-15T19:09:29Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/caco_2_cell.yaml"
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/brown_algae.yaml data/habitats/host_associated/bryophytes.yaml
    data/habitats/host_associated/bryozoa.yaml data/habitats/host_associated/bryozoans.yaml
    data/habitats/host_associated/buccal_mucosa.yaml data/habitats/host_associated/buccal_mucosa__62ec5bff.yaml
    data/habitats/host_associated/buccal_mucosa__a90386db.yaml data/habitats/host_associated/buffy_coat.yaml
    data/habitats/host_associated/bulb.yaml data/habitats/host_associated/bursa_of_fabricius.yaml
    data/habitats/host_associated/c1_glandular_saccules.yaml data/habitats/host_associated/c2.yaml
    data/habitats/host_associated/c3.yaml data/habitats/host_associated/caco_2_cell.yaml
    data/habitats/host_associated/caeca.yaml data/habitats/host_associated/caeca__67ed138d.yaml
    data/habitats/host_associated/caeca_bacteriome.yaml data/habitats/host_associated/canidae_dog.yaml
    data/habitats/host_associated/canthus.yaml data/habitats/host_associated/canthus__f4c2e1df.yaml
    data/habitats/host_associated/capillary.yaml data/habitats/host_associated/caprinae_sheep_goat.yaml
    data/habitats/host_associated/carapace.yaml data/habitats/host_associated/carcass.yaml
  exit_code: 0
  target_ids:
  - BTO:0000195
  summary: "Finished 2026-10-15T19:10:07Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/brown_algae.yaml data/habitats/host_associated/bryophytes.yaml\
    \ data/habitats/host_associated/bryozoa.yaml data/habitats/host_associated/bryozoans.yaml\
    \ data/habitats/host_associated/buccal_mucosa.yaml data/habitats/host_associated/buccal_mucosa__62ec5bff.yaml\
    \ data/habitats/host_associated/buccal_mucosa__a90386db.yaml data/habitats/host_associated/buffy_coat.yaml\
    \ data/habitats/host_associated/bulb.yaml data/habitats/host_associated/bursa_of_fabricius.yaml\
    \ data/habitats/host_associated/c1_glandular_saccules.yaml data/habitats/host_associated/c2.yaml\
    \ data/habitats/host_associated/c3.yaml data/habitats/host_associated/caco_2_cell.yaml\
    \ data/habitats/host_associated/caeca.yaml data/habitats/host_associated/caeca__67ed138d.yaml\
    \ data/habitats/host_associated/caeca_bacteriome.yaml data/habitats/host_associated/canidae_dog.yaml\
    \ data/habitats/host_associated/canthus.yaml data/habitats/host_associated/canthus__f4c2e1df.yaml\
    \ data/habitats/host_associated/capillary.yaml data/habitats/host_associated/caprinae_sheep_goat.yaml\
    \ data/habitats/host_associated/carapace.yaml data/habitats/host_associated/carcass.yaml\n\
    Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      24\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - BTO:0000195
  summary: 'Finished 2026-10-15T19:10:18Z. No issues found

    816 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - BTO:0000195
  summary: "Finished 2026-10-15T19:10:19Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - BTO:0000195
  summary: "Finished 2026-10-15T19:10:38Z. expected 3208 records, found 3208 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - BTO:0000195
  summary: "Finished 2026-10-15T19:10:44Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - BTO:0000195
  summary: "Finished 2026-10-15T19:11:04Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - BTO:0000195
  summary: "Finished 2026-10-15T19:12:07Z. id↔label correspondence summary:\n    \
    \      OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: CCI
  name: Exact-baseline full QC
  status: passed
  required: true
  command: gh run view 38786529592 --json status,conclusion,headSha,url,jobs
  exit_code: 0
  target_ids:
  - BTO:0000195
  summary: Verified 2026-10-15T19:04:33Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38786529592
  scope_note: Unchanged scientific input baseline; these new review files are outside
    that remote run.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/caco_2_cell.yaml
  locator: Entire target YAML
  accessed_at: '2026-10-15T19:30:30Z'
  support: supports
  summary: All fields, displayed taxa and complete curation history read.
  snapshot_sha256: a909a98a4b4f90fc49bbe783b4378ef136f1019932727effba1797103e165808
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, hierarchy and source-evidence rules
  accessed_at: '2026-10-15T19:30:30Z'
  support: supports
  summary: All parent contributions must be strictly broader; host identity is not
    environment identity. Source occurrences are not automatically characteristic.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: HabitatRecord, SourceAttestation, TaxonAssociation and category enums
  accessed_at: '2026-10-15T19:30:30Z'
  support: supports
  summary: Source-to-record mapping endpoints; reported associations versus characteristic
    assertions; category scope and optional fields.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed resolution routes, parent accumulation, prefix category and overrides
  accessed_at: '2026-10-15T19:30:30Z'
  support: supports
  summary: 'Exact emitted target reproduction established. Routes: [{"mint": "habitatmech:PREGO.c98b337dc1",
    "automatic": {"identifier": "BTO:0000195", "grounding_status": "EXACT", "mapping_predicate":
    null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route":
    "prego_self_grounded", "category": null, "reviewed": false, "decision": null},
    "final": {"identifier": "BTO:0000195", "grounding_status": "EXACT", "mapping_predicate":
    null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route":
    "prego_self_grounded", "category": null, "reviewed": false, "decision": null}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: Inventory projection
  accessed_at: '2026-10-15T19:30:30Z'
  support: supports
  summary: Counts/units and taxon ranks/scores preserve source meanings. PREGO projections
    omit original pair-level citation links.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/prego_habitat_taxa.tsv
  locator: Physical TSV rows 259,260,261,262
  accessed_at: '2026-10-15T19:30:30Z'
  support: supports
  summary: '[{"row": 259, "data": {"prego_id": "BTO:0000195", "rank": "1", "taxon_id":
    "NCBITaxon:1205679", "taxon_label": "Bifidobacterium longum subsp. longum CECT
    7347", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates",
    "corroborated_by": ""}}, {"row": 260, "data": {"prego_id": "BTO:0000195", "rank":
    "2", "taxon_id": "NCBITaxon:1392869", "taxon_label": "Escherichia coli K1", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 261, "data": {"prego_id": "BTO:0000195", "rank": "3", "taxon_id":
    "NCBITaxon:1580", "taxon_label": "Levilactobacillus brevis", "prego_score": "3",
    "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 262, "data": {"prego_id": "BTO:0000195", "rank": "4", "taxon_id":
    "NCBITaxon:557433", "taxon_label": "Limosilactobacillus reuteri subsp. reuteri
    JCM 1112", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates",
    "corroborated_by": ""}}]'
  snapshot_sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
- evidence_id: ET6
  kind: database
  reference: data/raw/prego_habitats.tsv
  locator: Physical TSV rows 401
  accessed_at: '2026-10-15T19:30:30Z'
  support: supports
  summary: '[{"row": 401, "data": {"prego_id": "BTO:0000195", "ontology": "BTO", "biolink_category":
    "biolink:GrossAnatomicalStructure", "taxon_count": "4", "direct_assertion_count":
    "4", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms":
    "CACO-2 cell|caco2|caco2 cell line|caco2 cell lines|caco2 cells"}}]'
  snapshot_sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
- evidence_id: ET7
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: Physical TSV rows 141,1294
  accessed_at: '2026-10-15T19:30:30Z'
  support: supports
  summary: '[{"row": 141, "data": {"subject": "BTO:0000195", "predicate": "rdfs:subClassOf",
    "object": "BTO:0001913"}}, {"row": 1294, "data": {"subject": "BTO:0001913", "predicate":
    "rdfs:subClassOf", "object": "BTO:0000797"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET8
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 197,1913
  accessed_at: '2026-10-15T19:30:30Z'
  support: supports
  summary: '[{"row": 197, "data": {"term_id": "BTO:0000195", "ontology": "BTO", "label":
    "CACO-2 cell", "definition": "Human colon adenocarcinoma cell line, established
    from the primary colon tumor (adenocarcinoma) of a 72-year-old Caucasian man in
    1974.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only":
    "FALSE"}}, {"row": 1913, "data": {"term_id": "BTO:0001913", "ontology": "BTO",
    "label": "colonic adenocarcinoma cell line", "definition": "", "synonyms": "",
    "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: ELEGACY
  kind: record_content
  reference: reports/yaml_record_review/20261002T225923Z-caco_2_cell.md
  locator: Findings and recommended edits; historical review lead
  accessed_at: '2026-10-15T19:30:30Z'
  support: supports
  summary: The earlier major finding was solely absence of a native ITEM REVIEW decision.
    SEEDED accurately reports that state and is not a scientific error by itself.
    This qualified review does not create the missing native decision or claim all
    source pairs independently verified.
  snapshot_sha256: 48d2119ad56a5ad82deb9d2cc918a76f9f6abc3741a8ebbf8d6a517e4ac014ff
- evidence_id: EX1
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000195/graph
  locator: BTO_0000195-graph.json
  accessed_at: '2026-10-15T19:05:52Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000195",
    "target": "http://purl.obolibrary.org/obo/BTO_0001913", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: 83e5b611b812a523d263831d5ceff5187f342064f236aad1a29fa4ec8c4e4984
- evidence_id: EX2
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000195
  locator: BTO_0000195.json
  accessed_at: '2026-10-15T19:05:51Z'
  support: context_only
  summary: 'Current authoritative identity, active status and definition: {"obo_id":
    "BTO:0000195", "label": "CACO-2 cell", "is_obsolete": false, "description": ["Human
    colon adenocarcinoma cell line, established from the primary colon tumor (adenocarcinoma)
    of a 72-year-old Caucasian man in 1974."]}'
  snapshot_sha256: 8f2ca1ce8b7c38cebf1a8891bcf2c382625e89a73b6f732e809eeb43d1930ece
- evidence_id: EX3
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001913/graph
  locator: BTO_0001913-graph.json
  accessed_at: '2026-10-15T19:06:02Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0001913",
    "target": "http://purl.obolibrary.org/obo/BTO_0000797", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: 5fd76fad54b7199923ecb13cfdd6a59477febd52c920bc0317f2fc418d5e3ec5
- evidence_id: EX4
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001913
  locator: BTO_0001913.json
  accessed_at: '2026-10-15T19:06:01Z'
  support: context_only
  summary: 'Current authoritative identity, active status and definition: {"obo_id":
    "BTO:0001913", "label": "colonic adenocarcinoma cell line", "is_obsolete": false,
    "description": []}'
  snapshot_sha256: 5c320b99622a8944345ef3a2aa0815ac1dad0fa5b198979fdf595db80faa7a22
- evidence_id: EX5
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML
  locator: PMC8879827.xml
  accessed_at: '2026-10-15T19:19:06Z'
  support: context_only
  summary: Primary methods section 2.3, PMID:35208748, DOI:10.3390/microorganisms10020293.
    BioProject-assigned taxa are associated with entities mined from linked abstracts
    at score three. This source channel does not certify natural isolation, viability,
    prevalence or characteristic presence.
  snapshot_sha256: 375f0fde4d07bb823cb9106aa4567bc0ef03c2866af0b2a7740b543f50687c25
- evidence_id: EX6
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22Dietary%20glycosaminoglycans%22&format=json&resultType=core&pageSize=10
  locator: paper-caco-cect.json
  accessed_at: '2026-10-15T19:19:13Z'
  support: context_only
  summary: Primary abstract PMID:20637226, DOI:10.1016/j.ijbiomac.2010.06.015. Adhesion
    of B. longum CECT7347 and other named bacteria to mucin and Caco-2 cultures was
    assayed. This directly supports experimental association for that strain, not
    original isolation from the cell line or the remaining three PREGO pair citations.
  snapshot_sha256: fffbacde29dfa88fd9f21fbcb3f4c22014d9ced1fd35005c5124cc6b93ceb1f1
- evidence_id: EX7
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=100469,1015,108028,1085628,1159213,1163745,1205679,131109,131112,1329,1330043,1334,1392869,1417985,155085,1580,1661,170187,1719,184914,1872627,1962667,197,2,206,243265,243273,28080,28091,28121,28188,283734,28450,28898,29419,317010,326522,33,34,35,38,388919,398527,52770,54,554290,557433,56,562,590061,694433,71864,722,731,753,754,759,75985,760,82806,83456,83462,85336,85401,90240,99807&retmode=xml
  locator: taxonomy.xml
  accessed_at: '2026-10-15T19:06:42Z'
  support: context_only
  summary: 'Current NCBI TaxIds, names and source-label comparison: [{"id": "NCBITaxon:1205679",
    "source": "PREGO", "label": "Bifidobacterium longum subsp. longum CECT 7347",
    "current_id": "1205679", "current_name": "Bifidobacterium longum subsp. longum
    CECT 7347", "rank": "strain", "direct_match": true, "recognized_alias": true},
    {"id": "NCBITaxon:1392869", "source": "PREGO", "label": "Escherichia coli K1",
    "current_id": "1392869", "current_name": "Escherichia coli K1", "rank": "strain",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1580", "source":
    "PREGO", "label": "Levilactobacillus brevis", "current_id": "1580", "current_name":
    "Levilactobacillus brevis", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:557433", "source": "PREGO", "label": "Limosilactobacillus
    reuteri subsp. reuteri JCM 1112", "current_id": "557433", "current_name": "Limosilactobacillus
    reuteri subsp. reuteri JCM 1112 = DSM 20016", "rank": "strain", "direct_match":
    false, "recognized_alias": false}]. For taxon557433, current NCBI adds the equivalent
    DSM20016 strain designation; the retained JCM1112 label is not a wrong identifier.'
  snapshot_sha256: ea5036b7cc5c9bf152840fae0a470b8f6cb17f89633967069648541712ecf8b2
- evidence_id: ESEARCH
  kind: search
  reference: Maintained inputs and local structured archive
  locator: rg --no-ignore --hidden -l -F -e BTO:0000195 -e 'CACO-2 cell' -e caco_2_cell
    -e habitatmech:PREGO.c98b337dc1 curation history research reports data/raw build
    reviews
  accessed_at: '2026-10-15T19:05:55Z'
  support: context_only
  summary: Exact source/curation rows were parsed separately. No formal target predecessor
    was found; not every broad label match was inspected.
  search_scope: curation, history, research, reports, data/raw, build and reviews;
    ignored and hidden files included; every structured review.yaml was parsed.
- evidence_id: EAVAIL
  kind: search
  reference: Configured kg-microbe checkout
  locator: find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe
    -type f -path '*/prego/*' -name '*.tsv'
  accessed_at: '2026-10-15T19:19:24Z'
  support: context_only
  summary: No prego-directory TSV files were found in this checkout. Original pair-level
    citation exports remain unavailable; this is not a global absence claim.
  search_scope: find across the configured checkout, including ignored and hidden
    files.
assessments:
- assessment_id: A1
  area: identity
  topic: Identity, definition, category and broader ancestry
  outcome: supported
  summary: The BTO identity is a human colon-adenocarcinoma-derived cell line, not
    an intact colon or a diagnosis. Its cell-line superclass is supported. A primary
    study directly assays B. longum CECT7347 adhesion to Caco-2 cultures, supporting
    experimental association rather than natural isolation. All four PREGO rows reproduce
    the source, but not every original pair has been independently traced. Assay exposure
    alone is not a demonstrated defect under the association schema.
  target_ids:
  - BTO:0000195
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
  dimensions:
  - name: native_status
    value: EXACT/SEEDED
    definition: Generated grounding and curation status; distinct from this scientific
      review verdict.
    evidence_ids:
    - E1
    - ESEED
- assessment_id: A2
  area: quantity
  topic: Source counts, units, ranks, pools and channels
  outcome: supported
  summary: 'Every attestation and displayed taxon was compared with its exact frozen
    source row. [{"source": "PREGO", "count": 4, "unit": "TAXON"}]. Side-table biosamples
    and study memberships are separate from tree ORGANISM counts; zero-count omission
    is not biological absence.'
  target_ids:
  - BTO:0000195
  evidence_ids:
  - E1
  - EEXTRACT
  - ESEED
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  dimensions:
  - name: source_assertion_units
    value: '[{"source": "PREGO", "count": 4, "unit": "TAXON"}]'
    definition: Frozen source counts with their noninterchangeable units; omitted
      zero GOLD counts are verified in the raw row.
    evidence_ids:
    - E1
    - EEXTRACT
    - ESEED
- assessment_id: A3
  area: evidence
  topic: Biological support and limits
  outcome: supported
  summary: The BTO identity is a human colon-adenocarcinoma-derived cell line, not
    an intact colon or a diagnosis. Its cell-line superclass is supported. A primary
    study directly assays B. longum CECT7347 adhesion to Caco-2 cultures, supporting
    experimental association rather than natural isolation. All four PREGO rows reproduce
    the source, but not every original pair has been independently traced. Assay exposure
    alone is not a demonstrated defect under the association schema.
  target_ids:
  - BTO:0000195
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
- assessment_id: A4
  area: completeness
  topic: Curation status, parameters, mechanisms and optional content
  outcome: supported
  summary: Executed routes reproduce EXACT/SEEDED. No target environmental parameters,
    causal edges, discussions/datasets or is_characteristic=true assertions are present.
    Parent-record mechanisms are not inherited. Optional absence and SEEDED status
    alone are not defects.
  target_ids:
  - BTO:0000195
  evidence_ids:
  - E1
  - ERULE
  - ESEED
- assessment_id: A5
  area: schema
  topic: Native deterministic gates
  outcome: supported
  summary: Ordinary and strict schema, 816 curation histories, provenance, exact 3208-record
    reproduction, 32 causal overlays, term requests, configured labels and exact-base
    QC passed. Deterministic fidelity does not establish biological correctness.
  target_ids:
  - BTO:0000195
  evidence_ids:
  - E1
  - ERULE
findings: []
actions: []
limitations:
- Original specimens and every pair-level source citation have not been independently
  reidentified. Source counts and ranks are not prevalence, viability, or characteristic
  presence.
- The configured label gate skips 2061 no-adapter pairs. Displayed taxon identities
  were separately checked against current NCBI Taxonomy, not certified by that label
  gate.
- Full QC evidence is a successful remote run at the exact unchanged scientific input
  base, not a new local full-QC execution. New review files require a post-save native
  archive check.
- 'iModulonDB is not applicable to these target claims: no gene, regulator, transcriptomic
  module or causal mechanism is asserted. No paid research was used.'
- Original PREGO pair exports are unavailable in the configured checkout. Primary
  examples do not prove the provenance or truth of every retained pair. Score three
  remains the source score, not measured localization confidence.
- The CECT7347 adhesion study is positive evidence for one pair only. Current NCBI
  expands the JCM1112 name with DSM20016; no incorrect TaxId is inferred from the
  shorter frozen label.
notes:
- Current input hashes were checked against both working bytes and exact tracked base
  blobs; source.state git_commit explicitly describes that revision.
- Ignored-inclusive searches and the parsed structured archive found no previous structured
  observation targeting this identifier. Broad label matches are leads, not formal
  lineage or automatic scientific findings.
- 'Read-only scientific review: no habitat curation, generation, history/status promotion
  or GitHub mutation is performed.'
- The earlier major finding was solely absence of a native ITEM REVIEW decision. SEEDED
  accurately reports that state and is not a scientific error by itself. This qualified
  review does not create the missing native decision or claim all source pairs independently
  verified.
tags:
- individual-scientific-review
- host-associated
```
