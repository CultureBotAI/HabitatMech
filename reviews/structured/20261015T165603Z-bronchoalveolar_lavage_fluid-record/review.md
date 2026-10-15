# Record review: bronchoalveolar lavage fluid (BTO:0000155)

- Review: 20261015T165603Z-bronchoalveolar_lavage_fluid-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T16:30:51Z
- Finished UTC: 2026-10-15T16:56:03Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The BTO label denotes recovered lavage fluid, but its imported definition describes the collection technique. Current BTO repeats this entity-type conflict. Primary genome analysis explicitly identifies M24 and M154 as lavage-fluid isolates, supporting a sample-material interpretation. The fix must preserve valid source associations and use PREGO mint habitatmech:PREGO.bdc9910582 for any item decision; SEEDED status alone is not the defect.

## Scope And Provenance

Full field-by-field scientific review of this one exact target at 50dbf8b388bf32ca58708f7993e83120310f7cea.

Selection: One of the next 24 path-ordered unreviewed targets in an ignored-inclusive 3208-record census. This bundle assesses only this identifier, not a cohort sample.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 50dbf8b388bf32ca58708f7993e83120310f7cea.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0000155 | data/habitats/host_associated/bronchoalveolar_lavage_fluid.yaml | generated | bronchoalveolar lavage fluid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0000155 | Completed 2026-10-15T16:35:14Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/bronchoalveolar_lavage_fluid.yaml |
| validate-strict | passed | True | BTO:0000155 | Completed 2026-10-15T16:35:27Z. uv run python scripts/validate_strict.py data/habitats/host_associated/bovinae_cow_cattle.yaml data/habitats/host_associated/bowens_disease_squamous_cell_carcinoma_in_situ.yaml data/habitats/host_associated/brain.yaml data/habitats/host_associated/brain__7bf4166c.yaml data/habitats/host_associated/brain__803f6884.yaml data/habitats/host_associated/brain__b2bb2ba8.yaml data/habitats/host_associated/brain__e9ca95b7.yaml data/habitats/host_associated/brain__f0593337.yaml data/habitats/host_associated/brain_cell_line.yaml data/habitats/host_associated/brain_stem.yaml data/habitats/host_associated/breast.yaml data/habitats/host_associated/breast_abscess.yaml data/habitats/host_associated/breast_cancer.yaml data/habitats/host_associated/breast_cancer_ductal.yaml data/habitats/host_associated/breast_cancer_lobular.yaml data/habitats/host_associated/breast_cyst.yaml data/habitats/host_associated/breviatea.yaml data/habitats/host_associated/bronchi.yaml data/habitats/host_associated/bronchi__3fb23b44.yaml data/habitats/host_associated/bronchi__c8c64428.yaml data/habitats/host_associated/bronchial_epithelial_cell.yaml data/habitats/host_associated/bronchiole.yaml data/habitats/host_associated/bronchoalveolar_lavage_fluid.yaml data/habitats/host_associated/bronchus.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | BTO:0000155 | Completed 2026-10-15T16:35:39Z. No issues found<br>814 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | BTO:0000155 | Completed 2026-10-15T16:35:39Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | BTO:0000155 | Completed 2026-10-15T16:36:01Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | BTO:0000155 | Completed 2026-10-15T16:36:06Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | BTO:0000155 | Completed 2026-10-15T16:36:35Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | BTO:0000155 | Completed 2026-10-15T16:37:38Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-baseline full QC | passed | True | BTO:0000155 | Verified 2026-10-15T16:29:56Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38764995320 |

## Scientific And Domain Assessments

### Identity, definition, hierarchy and aliases

identity: concern. Targets: BTO:0000155.

The BTO label denotes recovered lavage fluid, but its imported definition describes the collection technique. Current BTO repeats this entity-type conflict. Primary genome analysis explicitly identifies M24 and M154 as lavage-fluid isolates, supporting a sample-material interpretation. The fix must preserve valid source associations and use PREGO mint habitatmech:PREGO.bdc9910582 for any item decision; SEEDED status alone is not the defect.

### Frozen counts, units, ranks, channels and scores

quantity: supported. Targets: BTO:0000155.

Every source assertion and displayed taxon was checked against its exact raw row. [{"source": "PREGO", "count": 10, "unit": "TAXON"}]. Side-table biosample/study counts are not added to tree ORGANISM counts. Zero-count omission is not biological absence.

### Scientific support and scope limits

evidence: supported. Targets: BTO:0000155.

The BTO label denotes recovered lavage fluid, but its imported definition describes the collection technique. Current BTO repeats this entity-type conflict. Primary genome analysis explicitly identifies M24 and M154 as lavage-fluid isolates, supporting a sample-material interpretation. The fix must preserve valid source associations and use PREGO mint habitatmech:PREGO.bdc9910582 for any item decision; SEEDED status alone is not the defect.

### Status, optional content, triads and mechanisms

completeness: supported. Targets: BTO:0000155.

Actual routes reproduce EXACT/SEEDED. No environmental-parameter, causal-edge, discussion/dataset or is_characteristic=true assertion is present in this target. Optional absence and SEEDED status alone are not defects. Scientific review does not promote native status.

### Native deterministic validation

schema: supported. Targets: BTO:0000155.

Ordinary and strict schemas, 814 history records, provenance, 3208-record reproduction, 32 causal overlays, term-request checks, configured labels and exact-base full QC passed. These establish fidelity, not biological truth.

## Findings

### F1: Imported ontology definition conflicts with the represented entity

major / open / confirmed; issue key: bronchoalveolar-lavage-fluid-ontology-definition-scope.

The BTO label denotes recovered lavage fluid, but its imported definition describes the collection technique. Current BTO repeats this entity-type conflict. Primary genome analysis explicitly identifies M24 and M154 as lavage-fluid isolates, supporting a sample-material interpretation. The fix must preserve valid source associations and use PREGO mint habitatmech:PREGO.bdc9910582 for any item decision; SEEDED status alone is not the defect. Reconcile label, definition and typed ontology relations against the intended source meaning. Prefer an upstream BTO correction followed by a controlled ontology-inventory refresh with manifests; a local override would require a new guarded, tested owner because record_annotation_corrections currently permits only synonym_type and taxon_label. A PREGO REVIEW row alone cannot repair the inherited definition. Do not patch generated YAML or force a definition onto an ontology ID through native-term requests.

## Recommended Actions And Acceptance Checks

### ACT1

The BTO label denotes recovered lavage fluid, but its imported definition describes the collection technique. Current BTO repeats this entity-type conflict. Primary genome analysis explicitly identifies M24 and M154 as lavage-fluid isolates, supporting a sample-material interpretation. The fix must preserve valid source associations and use PREGO mint habitatmech:PREGO.bdc9910582 for any item decision; SEEDED status alone is not the defect. Reconcile label, definition and typed ontology relations against the intended source meaning. Prefer an upstream BTO correction followed by a controlled ontology-inventory refresh with manifests; a local override would require a new guarded, tested owner because record_annotation_corrections currently permits only synonym_type and taxon_label. A PREGO REVIEW row alone cannot repair the inherited definition. Do not patch generated YAML or force a definition onto an ontology ID through native-term requests. No repair is performed by this review.

- Regress the exact reported claim and preserve independent identifiers, counts/units and raw provenance. Change identity, native status or mapping only when separately supported by the scoped item assessment; never change source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/bronchoalveolar_lavage_fluid.yaml; Entire target YAML | supports | Entire record read: identity, definition, parents, source attestations, every displayed taxon and complete history. |
| ERULE | docs/CURATION.md; Host, anatomy, hierarchy, disposition and evidence rules | supports | Parent_habitats means strictly broader; source occurrence does not establish characteristic presence. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; HabitatRecord and SourceAttestation slots | supports | Typed identity, broader habitat and source-to-record mapping semantics; optional fields are not mandatory. |
| ESEED | src/habitatmech/seed.py; Executed build_corpus/apply_decision routes and parent accumulation | supports | Full target equality was verified against actual generated document. Exact source routes: [{"mint": "habitatmech:PREGO.bdc9910582", "automatic": {"identifier": "BTO:0000155", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "BTO:0000155", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}}] |
| EEXTRACT | src/habitatmech/extract.py; Frozen inventory projection | supports | Source counts and taxon ranks/scores preserve source units; PREGO projections do not retain original pair-level citations. |
| ET5 | data/raw/prego_habitat_taxa.tsv; Physical TSV rows 203,204,205,206,207,208,209,210,211,212 | supports | [{"row": 203, "data": {"prego_id": "BTO:0000155", "rank": "1", "taxon_id": "NCBITaxon:1162284", "taxon_label": "Mycobacteroides abscessus M24", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 204, "data": {"prego_id": "BTO:0000155", "rank": "2", "taxon_id": "NCBITaxon:1162288", "taxon_label": "Mycobacteroides abscessus M154", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 205, "data": {"prego_id": "BTO:0000155", "rank": "3", "taxon_id": "NCBITaxon:1220554", "taxon_label": "Actinomadura chibensis NBRC 106107", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 206, "data": {"prego_id": "BTO:0000155", "rank": "4", "taxon_id": "NCBITaxon:1718", "taxon_label": "Corynebacterium glutamicum", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 207, "data": {"prego_id": "BTO:0000155", "rank": "5", "taxon_id": "NCBITaxon:287", "taxon_label": "Pseudomonas aeruginosa", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 208, "data": {"prego_id": "BTO:0000155", "rank": "6", "taxon_id": "NCBITaxon:32002", "taxon_label": "Achromobacter denitrificans", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 209, "data": {"prego_id": "BTO:0000155", "rank": "7", "taxon_id": "NCBITaxon:47885", "taxon_label": "Pseudomonas oryzihabitans", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 210, "data": {"prego_id": "BTO:0000155", "rank": "8", "taxon_id": "NCBITaxon:51665", "taxon_label": "Aerococcus urinaeequi", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 211, "data": {"prego_id": "BTO:0000155", "rank": "9", "taxon_id": "NCBITaxon:76759", "taxon_label": "Pseudomonas monteilii", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 212, "data": {"prego_id": "BTO:0000155", "rank": "10", "taxon_id": "NCBITaxon:83655", "taxon_label": "Leclercia adecarboxylata", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}] |
| ET6 | data/raw/prego_habitats.tsv; Physical TSV rows 333 | supports | [{"row": 333, "data": {"prego_id": "BTO:0000155", "ontology": "BTO", "biolink_category": "biolink:GrossAnatomicalStructure", "taxon_count": "10", "direct_assertion_count": "10", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms": "BAL cell&#124;BAL cells&#124;bronchioalveolar lavage&#124;bronchioalveolar lavage s&#124;bronchioalveolar lavages&#124;bronchoalveolar lavage fluid&#124;bronchoalveolar lavage fluids"}}] |
| ET7 | data/raw/ontology_terms.tsv; Physical TSV rows 157 | supports | [{"row": 157, "data": {"term_id": "BTO:0000155", "ontology": "BTO", "label": "bronchoalveolar lavage fluid", "definition": "A technique by which cells and fluid from bronchioles and lung alveoli are removed for diagnosis of disease or evaluation of treatment. A bronchoscope is wedged into a bronchus and sterile saline is pumped in and then removed along with the fluid and cells to be analyzed.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}] |
| ELEGACY | reports/yaml_record_review/20260922T140450Z-bronchoalveolar_lavage_fluid.md; Findings and recommended edits; historical lead | supports | Legacy conclusions were compared with current target and primary evidence. No formal predecessor or automatic native-status requirement is inferred. |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000155/graph; BTO_0000155-graph.json | context_only | Typed outgoing ontology relations, not an untyped ancestor list: [{"source": "http://purl.obolibrary.org/obo/BTO_0000155", "target": "http://purl.obolibrary.org/obo/BTO_0000136", "uri": "http://purl.obolibrary.org/obo/BFO_0000054", "label": "realized in"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000155; BTO_0000155.json | context_only | Current term identity, active status and definition: {"obo_id": "BTO:0000155", "label": "bronchoalveolar lavage fluid", "is_obsolete": false, "description": ["A technique by which cells and fluid from bronchioles and lung alveoli are removed for diagnosis of disease or evaluation of treatment. A bronchoscope is wedged into a bronchus and sterile saline is pumped in and then removed along with the fluid and cells to be analyzed."]} |
| EX3 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4035080/fullTextXML; PMC4035080.xml | context_only | Primary genome analysis Table 1, DOI:10.1186/1471-2164-15-359, PMID:24886480: M154 and M24 are listed as bronchoalveolar-lavage-fluid isolates. Published strain naming differs by subspecies grouping; the table does not prove all ten PREGO pairs or transform collection procedure into sample material. |
| EX4 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML; PMC8879827.xml | context_only | PREGO methods section 2.3, DOI:10.3390/microorganisms10020293, PMID:35208748: BioProject assigned taxa are associated with entities mined from linked abstracts at confidence three. The channel is not independently verified strain localization or ecological prevalence. |
| EX5 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1117644,1122164,1131452,1131453,1131454,1131455,1133849,1141647,1157946,1162284,1162288,1177117,1189613,1193128,1199187,1206729,1214102,1220554,1226751,12455,1271862,1328,1329,1329902,1334,1348,1392869,147802,153721,1578,1590,1601,161879,1639,1658,1661,1679,1680,1682,1683,168808,169963,1718,1724,1796,1802,1817,184914,1886,1962118,197,198,2,205913,206,2074,2081794,222805,238,2701,28026,28087,286804,287,32002,32020,33,341199,36808,391904,439842,476,47885,480035,484020,51665,524884,653940,678,720,72407,731,747,756689,76759,82135,82348,83655,838,84107,912594,985762&amp;retmode=xml; taxonomy.xml | context_only | All displayed IDs resolve in current NCBI Taxonomy. Preferred names and source labels were compared, without treating recognized historical aliases as wrong identities: [{"id": "NCBITaxon:1162284", "source": "PREGO", "label": "Mycobacteroides abscessus M24", "current_id": "1162284", "current_name": "Mycobacteroides abscessus M24", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1162288", "source": "PREGO", "label": "Mycobacteroides abscessus M154", "current_id": "1162288", "current_name": "Mycobacteroides abscessus M154", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1220554", "source": "PREGO", "label": "Actinomadura chibensis NBRC 106107", "current_id": "1220554", "current_name": "Actinomadura chibensis NBRC 106107", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1718", "source": "PREGO", "label": "Corynebacterium glutamicum", "current_id": "1718", "current_name": "Corynebacterium glutamicum", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:287", "source": "PREGO", "label": "Pseudomonas aeruginosa", "current_id": "287", "current_name": "Pseudomonas aeruginosa", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:32002", "source": "PREGO", "label": "Achromobacter denitrificans", "current_id": "32002", "current_name": "Achromobacter denitrificans", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:47885", "source": "PREGO", "label": "Pseudomonas oryzihabitans", "current_id": "47885", "current_name": "Pseudomonas oryzihabitans", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:51665", "source": "PREGO", "label": "Aerococcus urinaeequi", "current_id": "51665", "current_name": "Aerococcus urinaeequi", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:76759", "source": "PREGO", "label": "Pseudomonas monteilii", "current_id": "76759", "current_name": "Pseudomonas monteilii", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:83655", "source": "PREGO", "label": "Leclercia adecarboxylata", "current_id": "83655", "current_name": "Leclercia adecarboxylata", "rank": "species", "direct_match": true, "recognized_alias": true}] |
| ESEARCH | Local maintained inputs and structured archive; rg --no-ignore --hidden -l -F -e BTO:0000155 -e 'bronchoalveolar lavage fluid' -e bronchoalveolar_lavage_fluid -e habitatmech:PREGO.bdc9910582 curation history research reports data/raw build reviews | context_only | Exact source/curation rows were parsed separately from broad textual matches. No previous structured target observation was found; not every broad label match was inspected. |
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
review_id: 20261015T165603Z-bronchoalveolar_lavage_fluid-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: bronchoalveolar lavage fluid (BTO:0000155)'
started_at: '2026-10-15T16:30:51Z'
finished_at: '2026-10-15T16:56:03Z'
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
summary: The BTO label denotes recovered lavage fluid, but its imported definition
  describes the collection technique. Current BTO repeats this entity-type conflict.
  Primary genome analysis explicitly identifies M24 and M154 as lavage-fluid isolates,
  supporting a sample-material interpretation. The fix must preserve valid source
  associations and use PREGO mint habitatmech:PREGO.bdc9910582 for any item decision;
  SEEDED status alone is not the defect.
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
  - path: data/habitats/host_associated/bronchoalveolar_lavage_fluid.yaml
    sha256: 61d6e2b8feaea077b5e8d70a93fbd37c8a281b709534ed01e09a15109a99c701
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
  - path: reports/yaml_record_review/20260922T140450Z-bronchoalveolar_lavage_fluid.md
    sha256: 4f835abd9ee44fefae6740fc355121949582fd6a7983c1f2e471461870ab8274
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
- target_id: BTO:0000155
  path: data/habitats/host_associated/bronchoalveolar_lavage_fluid.yaml
  label: bronchoalveolar lavage fluid
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
  - BTO:0000155
  exclusions:
  - target: Other records and SSSOM/KGX products
    reason: Parent context is not additional coverage. Export compatibility and original
      individual source specimens are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/bronchoalveolar_lavage_fluid.yaml
  exit_code: 0
  target_ids:
  - BTO:0000155
  summary: "Completed 2026-10-15T16:35:14Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/bronchoalveolar_lavage_fluid.yaml"
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
  - BTO:0000155
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
  - BTO:0000155
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
  - BTO:0000155
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
  - BTO:0000155
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
  - BTO:0000155
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
  - BTO:0000155
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
  - BTO:0000155
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
  - BTO:0000155
  summary: Verified 2026-10-15T16:29:56Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38764995320
  scope_note: Exact unchanged scientific input baseline; new review files are outside
    that remote run.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/bronchoalveolar_lavage_fluid.yaml
  locator: Entire target YAML
  accessed_at: '2026-10-15T16:56:03Z'
  support: supports
  summary: 'Entire record read: identity, definition, parents, source attestations,
    every displayed taxon and complete history.'
  snapshot_sha256: 61d6e2b8feaea077b5e8d70a93fbd37c8a281b709534ed01e09a15109a99c701
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host, anatomy, hierarchy, disposition and evidence rules
  accessed_at: '2026-10-15T16:56:03Z'
  support: supports
  summary: Parent_habitats means strictly broader; source occurrence does not establish
    characteristic presence.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: HabitatRecord and SourceAttestation slots
  accessed_at: '2026-10-15T16:56:03Z'
  support: supports
  summary: Typed identity, broader habitat and source-to-record mapping semantics;
    optional fields are not mandatory.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed build_corpus/apply_decision routes and parent accumulation
  accessed_at: '2026-10-15T16:56:03Z'
  support: supports
  summary: 'Full target equality was verified against actual generated document. Exact
    source routes: [{"mint": "habitatmech:PREGO.bdc9910582", "automatic": {"identifier":
    "BTO:0000155", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded",
    "category": null, "reviewed": false, "decision": null}, "final": {"identifier":
    "BTO:0000155", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded",
    "category": null, "reviewed": false, "decision": null}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: Frozen inventory projection
  accessed_at: '2026-10-15T16:56:03Z'
  support: supports
  summary: Source counts and taxon ranks/scores preserve source units; PREGO projections
    do not retain original pair-level citations.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/prego_habitat_taxa.tsv
  locator: Physical TSV rows 203,204,205,206,207,208,209,210,211,212
  accessed_at: '2026-10-15T16:56:03Z'
  support: supports
  summary: '[{"row": 203, "data": {"prego_id": "BTO:0000155", "rank": "1", "taxon_id":
    "NCBITaxon:1162284", "taxon_label": "Mycobacteroides abscessus M24", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 204, "data": {"prego_id": "BTO:0000155", "rank": "2", "taxon_id":
    "NCBITaxon:1162288", "taxon_label": "Mycobacteroides abscessus M154", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 205, "data": {"prego_id": "BTO:0000155", "rank": "3", "taxon_id":
    "NCBITaxon:1220554", "taxon_label": "Actinomadura chibensis NBRC 106107", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 206, "data": {"prego_id": "BTO:0000155", "rank": "4", "taxon_id":
    "NCBITaxon:1718", "taxon_label": "Corynebacterium glutamicum", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 207, "data": {"prego_id": "BTO:0000155", "rank": "5", "taxon_id":
    "NCBITaxon:287", "taxon_label": "Pseudomonas aeruginosa", "prego_score": "3",
    "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 208, "data": {"prego_id": "BTO:0000155", "rank": "6", "taxon_id":
    "NCBITaxon:32002", "taxon_label": "Achromobacter denitrificans", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 209, "data": {"prego_id": "BTO:0000155", "rank": "7", "taxon_id":
    "NCBITaxon:47885", "taxon_label": "Pseudomonas oryzihabitans", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 210, "data": {"prego_id": "BTO:0000155", "rank": "8", "taxon_id":
    "NCBITaxon:51665", "taxon_label": "Aerococcus urinaeequi", "prego_score": "3",
    "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 211, "data": {"prego_id": "BTO:0000155", "rank": "9", "taxon_id":
    "NCBITaxon:76759", "taxon_label": "Pseudomonas monteilii", "prego_score": "3",
    "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 212, "data": {"prego_id": "BTO:0000155", "rank": "10", "taxon_id":
    "NCBITaxon:83655", "taxon_label": "Leclercia adecarboxylata", "prego_score": "3",
    "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}]'
  snapshot_sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
- evidence_id: ET6
  kind: database
  reference: data/raw/prego_habitats.tsv
  locator: Physical TSV rows 333
  accessed_at: '2026-10-15T16:56:03Z'
  support: supports
  summary: '[{"row": 333, "data": {"prego_id": "BTO:0000155", "ontology": "BTO", "biolink_category":
    "biolink:GrossAnatomicalStructure", "taxon_count": "10", "direct_assertion_count":
    "10", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms":
    "BAL cell|BAL cells|bronchioalveolar lavage|bronchioalveolar lavage s|bronchioalveolar
    lavages|bronchoalveolar lavage fluid|bronchoalveolar lavage fluids"}}]'
  snapshot_sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
- evidence_id: ET7
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 157
  accessed_at: '2026-10-15T16:56:03Z'
  support: supports
  summary: '[{"row": 157, "data": {"term_id": "BTO:0000155", "ontology": "BTO", "label":
    "bronchoalveolar lavage fluid", "definition": "A technique by which cells and
    fluid from bronchioles and lung alveoli are removed for diagnosis of disease or
    evaluation of treatment. A bronchoscope is wedged into a bronchus and sterile
    saline is pumped in and then removed along with the fluid and cells to be analyzed.",
    "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only":
    "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: ELEGACY
  kind: record_content
  reference: reports/yaml_record_review/20260922T140450Z-bronchoalveolar_lavage_fluid.md
  locator: Findings and recommended edits; historical lead
  accessed_at: '2026-10-15T16:56:03Z'
  support: supports
  summary: Legacy conclusions were compared with current target and primary evidence.
    No formal predecessor or automatic native-status requirement is inferred.
  snapshot_sha256: 4f835abd9ee44fefae6740fc355121949582fd6a7983c1f2e471461870ab8274
- evidence_id: EX1
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000155/graph
  locator: BTO_0000155-graph.json
  accessed_at: '2026-10-15T16:34:09Z'
  support: context_only
  summary: 'Typed outgoing ontology relations, not an untyped ancestor list: [{"source":
    "http://purl.obolibrary.org/obo/BTO_0000155", "target": "http://purl.obolibrary.org/obo/BTO_0000136",
    "uri": "http://purl.obolibrary.org/obo/BFO_0000054", "label": "realized in"}]'
  snapshot_sha256: acd56d975c8abda0f90bd83214e7de54d5f7ecccf958a8fba2b77cdcf17b5634
- evidence_id: EX2
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000155
  locator: BTO_0000155.json
  accessed_at: '2026-10-15T16:34:08Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "BTO:0000155",
    "label": "bronchoalveolar lavage fluid", "is_obsolete": false, "description":
    ["A technique by which cells and fluid from bronchioles and lung alveoli are removed
    for diagnosis of disease or evaluation of treatment. A bronchoscope is wedged
    into a bronchus and sterile saline is pumped in and then removed along with the
    fluid and cells to be analyzed."]}'
  snapshot_sha256: f05f0d51360eba411171e95f4ad3a9de9518320ae80428706ad593ecb0d45099
- evidence_id: EX3
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4035080/fullTextXML
  locator: PMC4035080.xml
  accessed_at: '2026-10-15T16:43:59Z'
  support: context_only
  summary: 'Primary genome analysis Table 1, DOI:10.1186/1471-2164-15-359, PMID:24886480:
    M154 and M24 are listed as bronchoalveolar-lavage-fluid isolates. Published strain
    naming differs by subspecies grouping; the table does not prove all ten PREGO
    pairs or transform collection procedure into sample material.'
  snapshot_sha256: 40d1cfa6007b2ddee8ca5a15908a7dc2a3940c4a1aad78340430c4f95c8975d6
- evidence_id: EX4
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
- evidence_id: EX5
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1117644,1122164,1131452,1131453,1131454,1131455,1133849,1141647,1157946,1162284,1162288,1177117,1189613,1193128,1199187,1206729,1214102,1220554,1226751,12455,1271862,1328,1329,1329902,1334,1348,1392869,147802,153721,1578,1590,1601,161879,1639,1658,1661,1679,1680,1682,1683,168808,169963,1718,1724,1796,1802,1817,184914,1886,1962118,197,198,2,205913,206,2074,2081794,222805,238,2701,28026,28087,286804,287,32002,32020,33,341199,36808,391904,439842,476,47885,480035,484020,51665,524884,653940,678,720,72407,731,747,756689,76759,82135,82348,83655,838,84107,912594,985762&retmode=xml
  locator: taxonomy.xml
  accessed_at: '2026-10-15T16:34:33Z'
  support: context_only
  summary: 'All displayed IDs resolve in current NCBI Taxonomy. Preferred names and
    source labels were compared, without treating recognized historical aliases as
    wrong identities: [{"id": "NCBITaxon:1162284", "source": "PREGO", "label": "Mycobacteroides
    abscessus M24", "current_id": "1162284", "current_name": "Mycobacteroides abscessus
    M24", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id":
    "NCBITaxon:1162288", "source": "PREGO", "label": "Mycobacteroides abscessus M154",
    "current_id": "1162288", "current_name": "Mycobacteroides abscessus M154", "rank":
    "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1220554",
    "source": "PREGO", "label": "Actinomadura chibensis NBRC 106107", "current_id":
    "1220554", "current_name": "Actinomadura chibensis NBRC 106107", "rank": "strain",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1718", "source":
    "PREGO", "label": "Corynebacterium glutamicum", "current_id": "1718", "current_name":
    "Corynebacterium glutamicum", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:287", "source": "PREGO", "label": "Pseudomonas aeruginosa",
    "current_id": "287", "current_name": "Pseudomonas aeruginosa", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:32002", "source":
    "PREGO", "label": "Achromobacter denitrificans", "current_id": "32002", "current_name":
    "Achromobacter denitrificans", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:47885", "source": "PREGO", "label": "Pseudomonas oryzihabitans",
    "current_id": "47885", "current_name": "Pseudomonas oryzihabitans", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:51665", "source":
    "PREGO", "label": "Aerococcus urinaeequi", "current_id": "51665", "current_name":
    "Aerococcus urinaeequi", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:76759", "source": "PREGO", "label": "Pseudomonas monteilii",
    "current_id": "76759", "current_name": "Pseudomonas monteilii", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:83655", "source":
    "PREGO", "label": "Leclercia adecarboxylata", "current_id": "83655", "current_name":
    "Leclercia adecarboxylata", "rank": "species", "direct_match": true, "recognized_alias":
    true}]'
  snapshot_sha256: 249c661a92762c2362c9b3b8c3a0606ef71a9369fb2600df89f8ed7f06ace644
- evidence_id: ESEARCH
  kind: search
  reference: Local maintained inputs and structured archive
  locator: rg --no-ignore --hidden -l -F -e BTO:0000155 -e 'bronchoalveolar lavage
    fluid' -e bronchoalveolar_lavage_fluid -e habitatmech:PREGO.bdc9910582 curation
    history research reports data/raw build reviews
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
  outcome: concern
  summary: The BTO label denotes recovered lavage fluid, but its imported definition
    describes the collection technique. Current BTO repeats this entity-type conflict.
    Primary genome analysis explicitly identifies M24 and M154 as lavage-fluid isolates,
    supporting a sample-material interpretation. The fix must preserve valid source
    associations and use PREGO mint habitatmech:PREGO.bdc9910582 for any item decision;
    SEEDED status alone is not the defect.
  target_ids:
  - BTO:0000155
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
- assessment_id: A2
  area: quantity
  topic: Frozen counts, units, ranks, channels and scores
  outcome: supported
  summary: 'Every source assertion and displayed taxon was checked against its exact
    raw row. [{"source": "PREGO", "count": 10, "unit": "TAXON"}]. Side-table biosample/study
    counts are not added to tree ORGANISM counts. Zero-count omission is not biological
    absence.'
  target_ids:
  - BTO:0000155
  evidence_ids:
  - E1
  - ESEED
  - EEXTRACT
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
- assessment_id: A3
  area: evidence
  topic: Scientific support and scope limits
  outcome: supported
  summary: The BTO label denotes recovered lavage fluid, but its imported definition
    describes the collection technique. Current BTO repeats this entity-type conflict.
    Primary genome analysis explicitly identifies M24 and M154 as lavage-fluid isolates,
    supporting a sample-material interpretation. The fix must preserve valid source
    associations and use PREGO mint habitatmech:PREGO.bdc9910582 for any item decision;
    SEEDED status alone is not the defect.
  target_ids:
  - BTO:0000155
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
- assessment_id: A4
  area: completeness
  topic: Status, optional content, triads and mechanisms
  outcome: supported
  summary: Actual routes reproduce EXACT/SEEDED. No environmental-parameter, causal-edge,
    discussion/dataset or is_characteristic=true assertion is present in this target.
    Optional absence and SEEDED status alone are not defects. Scientific review does
    not promote native status.
  target_ids:
  - BTO:0000155
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
  - BTO:0000155
  evidence_ids:
  - E1
  - ERULE
findings:
- finding_id: F1
  issue_key: bronchoalveolar-lavage-fluid-ontology-definition-scope
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Imported ontology definition conflicts with the represented entity
  description: The BTO label denotes recovered lavage fluid, but its imported definition
    describes the collection technique. Current BTO repeats this entity-type conflict.
    Primary genome analysis explicitly identifies M24 and M154 as lavage-fluid isolates,
    supporting a sample-material interpretation. The fix must preserve valid source
    associations and use PREGO mint habitatmech:PREGO.bdc9910582 for any item decision;
    SEEDED status alone is not the defect. Reconcile label, definition and typed ontology
    relations against the intended source meaning. Prefer an upstream BTO correction
    followed by a controlled ontology-inventory refresh with manifests; a local override
    would require a new guarded, tested owner because record_annotation_corrections
    currently permits only synonym_type and taxon_label. A PREGO REVIEW row alone
    cannot repair the inherited definition. Do not patch generated YAML or force a
    definition onto an ontology ID through native-term requests.
  target_ids:
  - BTO:0000155
  field_paths:
  - definition
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_subclass_edges.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/MANIFEST.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
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
  - BTO:0000155
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_subclass_edges.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/MANIFEST.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: The BTO label denotes recovered lavage fluid, but its imported definition
    describes the collection technique. Current BTO repeats this entity-type conflict.
    Primary genome analysis explicitly identifies M24 and M154 as lavage-fluid isolates,
    supporting a sample-material interpretation. The fix must preserve valid source
    associations and use PREGO mint habitatmech:PREGO.bdc9910582 for any item decision;
    SEEDED status alone is not the defect. Reconcile label, definition and typed ontology
    relations against the intended source meaning. Prefer an upstream BTO correction
    followed by a controlled ontology-inventory refresh with manifests; a local override
    would require a new guarded, tested owner because record_annotation_corrections
    currently permits only synonym_type and taxon_label. A PREGO REVIEW row alone
    cannot repair the inherited definition. Do not patch generated YAML or force a
    definition onto an ontology ID through native-term requests. No repair is performed
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
