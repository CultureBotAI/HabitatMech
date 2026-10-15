# Record review: B-lymphocyte (BTO:0000776)

- Review: 20261015T093737Z-b_lymphocyte-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T09:23:21Z
- Finished UTC: 2026-10-15T09:37:37Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The B-cell identity and lymphocyte superclass are sound, and all three PREGO names/counts/ranks reproduce. Reported-from scope is not established by the retained channel alone: B38 has gastric-biopsy/lymphoma context, HUJEG-1 has culture/mycetoma context, and an independent Lactococcus study measures immune responses. Original pair evidence remains necessary.

## Scope And Provenance

Scientific review of one exact target at bcf6c369a27a5bf1dd9a0156f12f0a61352ff78d.

Selection: Next twenty unreviewed records in corpus path order; this bundle assesses exactly one of their resolved identifiers.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base bcf6c369a27a5bf1dd9a0156f12f0a61352ff78d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0000776 | data/habitats/host_associated/b_lymphocyte.yaml | generated | B-lymphocyte |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0000776 | Completed 2026-10-15T09:23:50Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/b_lymphocyte.yaml |
| validate-strict | passed | True | BTO:0000776 | Completed 2026-10-15T09:25:01Z. uv run python scripts/validate_strict.py data/habitats/host_associated/attached_keratinized_gingiva.yaml data/habitats/host_associated/attached_keratinized_gingiva__a8c3d27a.yaml data/habitats/host_associated/auditory_hearing_system.yaml data/habitats/host_associated/auditory_hearing_system__8fefc879.yaml data/habitats/host_associated/aural.yaml data/habitats/host_associated/autopod_pad.yaml data/habitats/host_associated/autotrophic_anf.yaml data/habitats/host_associated/axilla.yaml data/habitats/host_associated/b_lymphocyte.yaml data/habitats/host_associated/b_lymphocyte_cell_line.yaml data/habitats/host_associated/bacteria.yaml data/habitats/host_associated/bacteria__7bc807fd.yaml data/habitats/host_associated/bacteroid.yaml data/habitats/host_associated/bark.yaml data/habitats/host_associated/bark__5b1d3b9d.yaml data/habitats/host_associated/bartholin_abscess.yaml data/habitats/host_associated/basal_cell_carcinoma.yaml data/habitats/host_associated/bcp_1_cell.yaml data/habitats/host_associated/beaker_s_popliteal_cyst.yaml data/habitats/host_associated/benign_tumor.yaml<br>Validating 20 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      20<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | BTO:0000776 | Completed 2026-10-15T09:25:13Z. No issues found<br>777 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | BTO:0000776 | Completed 2026-10-15T09:25:14Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | BTO:0000776 | Completed 2026-10-15T09:25:35Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | BTO:0000776 | Completed 2026-10-15T09:25:40Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | BTO:0000776 | Completed 2026-10-15T09:26:00Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | BTO:0000776 | Completed 2026-10-15T09:26:58Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-revision baseline full QC | passed | True | BTO:0000776 | Required full native QC and structured-review contract succeeded at the exact captured revision; status checked 2026-10-15T09:25:51Z. https://github.com/CultureBotAI/HabitatMech/actions/runs/38709434919 |

## Scientific And Domain Assessments

### Native validators and reproduction

schema: supported. Targets: BTO:0000776.

Individual schema, twenty-target strict validation, 777 history records, 14 inventories/two GOLD sources, 3,208-record reproduction, 32 overlays and 110 term requests passed. This establishes deterministic fidelity, not scientific validity.

### Identity, definition, hierarchy and synonym scope

identity: concern. Targets: BTO:0000776.

The B-cell identity and lymphocyte superclass are sound, and all three PREGO names/counts/ranks reproduce. Reported-from scope is not established by the retained channel alone: B38 has gastric-biopsy/lymphoma context, HUJEG-1 has culture/mycetoma context, and an independent Lactococcus study measures immune responses. Original pair evidence remains necessary.

### Counts, units and ranking provenance

quantity: supported. Targets: BTO:0000776.

Exact source rows reproduce [{"source": "PREGO", "count": 3, "unit": "TAXON"}]. Every displayed taxon ID/name resolves in NCBI; ranks and pools reproduce the exact habitat-keyed rows. Tied PREGO score/direct flags are ordered by taxon ID, not abundance. Zero tree counts do not imply microbial absence or erase different bulk counts.

### Source status and optional claims

completeness: supported. Targets: BTO:0000776.

Full routes reproduce EXACT/SEEDED. Optional parameter, mechanism and characteristic-presence claims are not asserted and are not required quotas. Source parent counts, triad annotations and adjacent records are not inherited observations.

## Findings

### F1: Retained evidence does not establish cell-site occurrence

major / open / provisional; issue key: b-lymphocyte-prego-occurrence-scope.

Recover the manifest-matching PREGO pair evidence and distinguish occurrence/localization from disease, assay, or name context. The B-cell identity and lymphocyte superclass are sound, and all three PREGO names/counts/ranks reproduce. Reported-from scope is not established by the retained channel alone: B38 has gastric-biopsy/lymphoma context, HUJEG-1 has culture/mycetoma context, and an independent Lactococcus study measures immune responses. Original pair evidence remains necessary. Preserve raw totals and source provenance; any qualified association pool needs an explicit maintained contract, not hand deletion from generated YAML.

## Recommended Actions And Acceptance Checks

### ACT1

Recover the manifest-matching PREGO pair evidence and distinguish occurrence/localization from disease, assay, or name context. The B-cell identity and lymphocyte superclass are sound, and all three PREGO names/counts/ranks reproduce. Reported-from scope is not established by the retained channel alone: B38 has gastric-biopsy/lymphoma context, HUJEG-1 has culture/mycetoma context, and an independent Lactococcus study measures immune responses. Original pair evidence remains necessary. Preserve raw totals and source provenance; any qualified association pool needs an explicit maintained contract, not hand deletion from generated YAML. No repair is performed by this review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history. Do not change source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/b_lymphocyte.yaml; Entire YAML | supports | Read the complete target including source path, fields, taxonomy and generated history. |
| ERULE | docs/CURATION.md; Host identity, broader parents and maintained ownership | supports | Whole organisms cannot identify associated environments; parent_habitats requires strictly broader habitat meaning. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation, parent_habitats, xrefs and CharacteristicTaxon | supports | Source-to-record mapping endpoints, broader habitat relations and observed versus characteristic presence are distinct. |
| ESEED | src/habitatmech/seed.py; Native executed resolution route | supports | Executed native route and final decision: [{"source": "PREGO", "mint": "habitatmech:PREGO.cafee0000f", "automatic": {"identifier": "BTO:0000776", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "BTO:0000776", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}}] |
| EEXTRACT | src/habitatmech/extract.py; extract_prego | supports | Projection deduplicates pairs, preserves best score/channel, uses score/directness/taxon-ID order and retains a full distinct-taxon pool. Original pair citations are not emitted into this committed projection. |
| ET5 | data/raw/prego_habitat_taxa.tsv; TSV physical rows 1284,1285,1286 | supports | [{"row": 1284, "data": {"prego_id": "BTO:0000776", "rank": "1", "taxon_id": "NCBITaxon:1133849", "taxon_label": "Nocardia brasiliensis ATCC 700358", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 1285, "data": {"prego_id": "BTO:0000776", "rank": "2", "taxon_id": "NCBITaxon:1359", "taxon_label": "Lactococcus cremoris", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 1286, "data": {"prego_id": "BTO:0000776", "rank": "3", "taxon_id": "NCBITaxon:592205", "taxon_label": "Helicobacter pylori B38", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}] |
| ET6 | data/raw/prego_habitats.tsv; TSV physical rows 437 | supports | [{"row": 437, "data": {"prego_id": "BTO:0000776", "ontology": "BTO", "biolink_category": "biolink:GrossAnatomicalStructure", "taxon_count": "3", "direct_assertion_count": "3", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms": "B cell&#124;B cells&#124;B-cell&#124;B-cells&#124;B-lymphocyte&#124;B-lymphocytes"}}] |
| ET7 | data/raw/ontology_subclass_edges.tsv; TSV physical rows 508,509,510 | supports | [{"row": 508, "data": {"subject": "BTO:0000775", "predicate": "rdfs:subClassOf", "object": "BTO:0000751"}}, {"row": 509, "data": {"subject": "BTO:0000775", "predicate": "rdfs:subClassOf", "object": "BTO:0001096"}}, {"row": 510, "data": {"subject": "BTO:0000776", "predicate": "rdfs:subClassOf", "object": "BTO:0000775"}}] |
| ET8 | data/raw/ontology_terms.tsv; TSV physical rows 776,777 | supports | [{"row": 776, "data": {"term_id": "BTO:0000775", "ontology": "BTO", "label": "lymphocyte", "definition": "Any of the colorless weakly motile cells originating from stem cells and differentiating in lymphoid tissue (as of the thymus or bone marrow) that are the typical cellular elements of lymph, include the cellular mediators of immunity, and constitute 20 to 30 percent of the white blood cells of normal human blood.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}, {"row": 777, "data": {"term_id": "BTO:0000776", "ontology": "BTO", "label": "B-lymphocyte", "definition": "Any of the lymphocytes that have antibody molecules on the surface and comprise the antibody-secreting plasma cells when mature.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}] |
| EP9 | data/habitats/host_associated/lymphocyte.yaml; Direct parent scope, not an additional target review | supports | {"identifier": "BTO:0000775", "label": "lymphocyte", "definition": "Any of the colorless weakly motile cells originating from stem cells and differentiating in lymphoid tissue (as of the thymus or bone marrow) that are the typical cellular elements of lymph, include the cellular mediators of immunity, and constitute 20 to 30 percent of the white blood cells of normal human blood.", "grounding_status": "EXACT", "parent_habitats": ["BTO:0000751", "BTO:0001096"], "source_attestations": [{"source": "PREGO", "source_id": "BTO:0000775", "source_label": "lymphocyte", "assertion_count": 7, "assertion_unit": "TAXON", "score": 3.0, "evidence_channels": "annotated_genomes_isolates"}]} |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000751/graph; Canonical term identity, definition and explicit relation types | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0000751", "target": "http://purl.obolibrary.org/obo/BTO_0000574", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000751; Canonical term identity, definition and explicit relation types | supports | BTO:0000751 leukocyte; inspected definition and typed scope. ["Any of the blood cells that are colorless, lack hemoglobin, contain a nucleus, and include the lymphocytes, monocytes, neutrophils, eosinophils, and basophils."] |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000775/graph; Canonical term identity, definition and explicit relation types | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0000775", "target": "http://purl.obolibrary.org/obo/BTO_0000751", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/BTO_0000775", "target": "http://purl.obolibrary.org/obo/BTO_0001096", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000775; Canonical term identity, definition and explicit relation types | supports | BTO:0000775 lymphocyte; inspected definition and typed scope. ["Any of the colorless weakly motile cells originating from stem cells and differentiating in lymphoid tissue (as of the thymus or bone marrow) that are the typical cellular elements of lymph, include the cellular mediators of immunity, and constitute 20 to 30 percent of the white blood cells of normal human blood."] |
| EX5 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000776/graph; Canonical term identity, definition and explicit relation types | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0000776", "target": "http://purl.obolibrary.org/obo/BTO_0000775", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX6 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000776; Canonical term identity, definition and explicit relation types | supports | BTO:0000776 B-lymphocyte; inspected definition and typed scope. ["Any of the lymphocytes that have antibody molecules on the surface and comprise the antibody-secreting plasma cells when mature."] |
| EX7 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001096/graph; Canonical term identity, definition and explicit relation types | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0001096", "target": "http://purl.obolibrary.org/obo/BTO_0000753", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX8 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001096; Canonical term identity, definition and explicit relation types | supports | BTO:0001096 lymphoid cell; inspected definition and typed scope. ["Any of the cells responsible for the production of immunity mediated by cells or antibodies and including lymphocytes, lymphoblasts, and plasma cells. Cells derived from stem cells of the lymphoid lineage: large and small lymphocytes, plasma cells."] |
| EX9 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10159052/fullTextXML; Methods and results: bacterial strains and splenic IgM-positive cells | supports | PMID:37153602; DOI:10.3389/fimmu.2023.1178462. Aquatic-origin L. cremoris WA2-67 strains were added to trout splenocyte cultures to test immune effects. B-cell survival or proliferation after exposure does not establish bacterial residence. This is a strain-scoped contrast, not the original PREGO citation or a species-wide absence finding. |
| EX10 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3091627/fullTextXML; Results: B38; Methods: bacterial strains and DNA | supports | PMID:20537153; DOI:10.1186/1471-2164-11-368. B38 belongs to gastric B-cell MALT-lymphoma patient isolates; isolation involved biopsy homogenization and culture. Patient disease context does not demonstrate B-lymphocyte residence. This is not identified as the original PREGO pair citation. |
| EX11 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3510171/fullTextXML; Methods: intracellular viable recovery; Results and Figure 2 | supports | PMID:23209805; DOI:10.1371/journal.pone.0050667. Imaging and recovery after extracellular killing support viable intracellular Salmonella in primary human B cells and replication in Ramos cells, with different replication outcomes. This positive control establishes bounded site eligibility, not any of the displayed PREGO pairs. |
| EX12 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3670865/fullTextXML; Introduction and Methods: genome sequencing | supports | PMID:23755230; DOI:10.1371/journal.pone.0065425. HUJEG-1 is ATCC 700358, and sequencing used a colony-purified stock. The inspected strain context concerns soil, mycetoma and pathogenesis, not demonstrated B-cell localization. Gene predictions are not imported as habitat mechanisms. |
| EX13 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML; Section 2.3: BioProject-associated abstracts | supports | PMID:35208748; DOI:10.3390/microorganisms10020293. The annotated-genomes channel includes text-mined associations from abstracts linked to genome-sequencing BioProjects, assigned score three of five. That channel is not exclusively direct isolation-site evidence. |
| EX14 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1133849,114615,1245469,1359,191292,2,375177,438753,592205&amp;retmode=xml; TaxId, ScientificName, Rank, Lineage and aliases | supports | [{"id": "NCBITaxon:1133849", "label": "Nocardia brasiliensis ATCC 700358", "current_id": "1133849", "current_name": "Nocardia brasiliensis ATCC 700358", "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Bacillati; Actinomycetota; Actinomycetes; Mycobacteriales; Nocardiaceae; Nocardia; Nocardia brasiliensis"}, {"id": "NCBITaxon:1359", "label": "Lactococcus cremoris", "current_id": "1359", "current_name": "Lactococcus cremoris", "current_rank": "species", "lineage": "cellular organisms; Bacteria; Bacillati; Bacillota; Bacilli; Lactobacillales; Streptococcaceae; Lactococcus"}, {"id": "NCBITaxon:592205", "label": "Helicobacter pylori B38", "current_id": "592205", "current_name": "Helicobacter pylori B38", "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Pseudomonadati; Campylobacterota; Epsilonproteobacteria; Campylobacterales; Helicobacteraceae; Helicobacter; Helicobacter pylori"}] |
| ESEARCH | Local records and maintained inputs; rg --no-ignore --hidden -l -F -e BTO:0000776 -e B-lymphocyte -e b_lymphocyte -e habitatmech:PREGO.cafee0000f curation history research reports data/raw build reviews | context_only | Identifier, label, slug and minted-source search includes hidden and ignored files; parsed structured archive traversal found no target predecessor. Broad text hits are not treated as exact source associations. |
| ELEGACY | reports/yaml_record_review/20261004T091951Z-b_lymphocyte.md; Historical target review, especially findings and evidence leads | supports | Historical assessment was consulted for source and issue leads; current findings are independently reassessed against the captured inputs and stated authorities. It is not structured predecessor lineage. |
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
review_id: 20261015T093737Z-b_lymphocyte-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: B-lymphocyte (BTO:0000776)'
started_at: '2026-10-15T09:23:21Z'
finished_at: '2026-10-15T09:37:37Z'
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
summary: 'The B-cell identity and lymphocyte superclass are sound, and all three PREGO
  names/counts/ranks reproduce. Reported-from scope is not established by the retained
  channel alone: B38 has gastric-biopsy/lymphoma context, HUJEG-1 has culture/mycetoma
  context, and an independent Lactococcus study measures immune responses. Original
  pair evidence remains necessary.'
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
  - path: data/habitats/host_associated/b_lymphocyte.yaml
    sha256: 312d72ea9440b9972c46943790a0ccda553a3951da589fcdc44a680b858be0df
    role: target
  - path: data/habitats/host_associated/lymphocyte.yaml
    sha256: 0a8c568a0e1cb6f8abe8efa2f2b6bfe16869e056b420a4dbfa8879d3753f232a
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
  - path: reports/yaml_record_review/20261004T091951Z-b_lymphocyte.md
    sha256: 1c76c18e8697e96cd015f290c79c7ed53c99abdfba82d17348d38b6424c88515
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
- target_id: BTO:0000776
  path: data/habitats/host_associated/b_lymphocyte.yaml
  label: B-lymphocyte
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
  - BTO:0000776
  exclusions:
  - target: Other records, exports and parent-record reviews
    reason: Parent context informs this review but is not counted as additional reviewed
      coverage; SSSOM/KGX readiness is not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/b_lymphocyte.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000776
  summary: "Completed 2026-10-15T09:23:50Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/b_lymphocyte.yaml"
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
  - BTO:0000776
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
  - BTO:0000776
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
  - BTO:0000776
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
  - BTO:0000776
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
  - BTO:0000776
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
  - BTO:0000776
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
  - BTO:0000776
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
  - BTO:0000776
  summary: Required full native QC and structured-review contract succeeded at the
    exact captured revision; status checked 2026-10-15T09:25:51Z. https://github.com/CultureBotAI/HabitatMech/actions/runs/38709434919
  scope_note: Remote baseline execution; newly saved review outputs require their
    own archive check.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/b_lymphocyte.yaml
  locator: Entire YAML
  accessed_at: '2026-10-15T09:37:37Z'
  support: supports
  summary: Read the complete target including source path, fields, taxonomy and generated
    history.
  snapshot_sha256: 312d72ea9440b9972c46943790a0ccda553a3951da589fcdc44a680b858be0df
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, broader parents and maintained ownership
  accessed_at: '2026-10-15T09:37:37Z'
  support: supports
  summary: Whole organisms cannot identify associated environments; parent_habitats
    requires strictly broader habitat meaning.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation, parent_habitats, xrefs and CharacteristicTaxon
  accessed_at: '2026-10-15T09:37:37Z'
  support: supports
  summary: Source-to-record mapping endpoints, broader habitat relations and observed
    versus characteristic presence are distinct.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Native executed resolution route
  accessed_at: '2026-10-15T09:37:37Z'
  support: supports
  summary: 'Executed native route and final decision: [{"source": "PREGO", "mint":
    "habitatmech:PREGO.cafee0000f", "automatic": {"identifier": "BTO:0000776", "grounding_status":
    "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents":
    [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed":
    false, "decision": null}, "final": {"identifier": "BTO:0000776", "grounding_status":
    "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents":
    [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed":
    false, "decision": null}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: extract_prego
  accessed_at: '2026-10-15T09:37:37Z'
  support: supports
  summary: Projection deduplicates pairs, preserves best score/channel, uses score/directness/taxon-ID
    order and retains a full distinct-taxon pool. Original pair citations are not
    emitted into this committed projection.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/prego_habitat_taxa.tsv
  locator: TSV physical rows 1284,1285,1286
  accessed_at: '2026-10-15T09:37:37Z'
  support: supports
  summary: '[{"row": 1284, "data": {"prego_id": "BTO:0000776", "rank": "1", "taxon_id":
    "NCBITaxon:1133849", "taxon_label": "Nocardia brasiliensis ATCC 700358", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 1285, "data": {"prego_id": "BTO:0000776", "rank": "2", "taxon_id":
    "NCBITaxon:1359", "taxon_label": "Lactococcus cremoris", "prego_score": "3", "direct_flag":
    "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row":
    1286, "data": {"prego_id": "BTO:0000776", "rank": "3", "taxon_id": "NCBITaxon:592205",
    "taxon_label": "Helicobacter pylori B38", "prego_score": "3", "direct_flag": "TRUE",
    "channels": "annotated_genomes_isolates", "corroborated_by": ""}}]'
  snapshot_sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
- evidence_id: ET6
  kind: database
  reference: data/raw/prego_habitats.tsv
  locator: TSV physical rows 437
  accessed_at: '2026-10-15T09:37:37Z'
  support: supports
  summary: '[{"row": 437, "data": {"prego_id": "BTO:0000776", "ontology": "BTO", "biolink_category":
    "biolink:GrossAnatomicalStructure", "taxon_count": "3", "direct_assertion_count":
    "3", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms":
    "B cell|B cells|B-cell|B-cells|B-lymphocyte|B-lymphocytes"}}]'
  snapshot_sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
- evidence_id: ET7
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV physical rows 508,509,510
  accessed_at: '2026-10-15T09:37:37Z'
  support: supports
  summary: '[{"row": 508, "data": {"subject": "BTO:0000775", "predicate": "rdfs:subClassOf",
    "object": "BTO:0000751"}}, {"row": 509, "data": {"subject": "BTO:0000775", "predicate":
    "rdfs:subClassOf", "object": "BTO:0001096"}}, {"row": 510, "data": {"subject":
    "BTO:0000776", "predicate": "rdfs:subClassOf", "object": "BTO:0000775"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET8
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV physical rows 776,777
  accessed_at: '2026-10-15T09:37:37Z'
  support: supports
  summary: '[{"row": 776, "data": {"term_id": "BTO:0000775", "ontology": "BTO", "label":
    "lymphocyte", "definition": "Any of the colorless weakly motile cells originating
    from stem cells and differentiating in lymphoid tissue (as of the thymus or bone
    marrow) that are the typical cellular elements of lymph, include the cellular
    mediators of immunity, and constitute 20 to 30 percent of the white blood cells
    of normal human blood.", "synonyms": "", "deprecated": "", "directly_referenced":
    "TRUE", "label_only": "FALSE"}}, {"row": 777, "data": {"term_id": "BTO:0000776",
    "ontology": "BTO", "label": "B-lymphocyte", "definition": "Any of the lymphocytes
    that have antibody molecules on the surface and comprise the antibody-secreting
    plasma cells when mature.", "synonyms": "", "deprecated": "", "directly_referenced":
    "TRUE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EP9
  kind: record_content
  reference: data/habitats/host_associated/lymphocyte.yaml
  locator: Direct parent scope, not an additional target review
  accessed_at: '2026-10-15T09:37:37Z'
  support: supports
  summary: '{"identifier": "BTO:0000775", "label": "lymphocyte", "definition": "Any
    of the colorless weakly motile cells originating from stem cells and differentiating
    in lymphoid tissue (as of the thymus or bone marrow) that are the typical cellular
    elements of lymph, include the cellular mediators of immunity, and constitute
    20 to 30 percent of the white blood cells of normal human blood.", "grounding_status":
    "EXACT", "parent_habitats": ["BTO:0000751", "BTO:0001096"], "source_attestations":
    [{"source": "PREGO", "source_id": "BTO:0000775", "source_label": "lymphocyte",
    "assertion_count": 7, "assertion_unit": "TAXON", "score": 3.0, "evidence_channels":
    "annotated_genomes_isolates"}]}'
  snapshot_sha256: 0a8c568a0e1cb6f8abe8efa2f2b6bfe16869e056b420a4dbfa8879d3753f232a
- evidence_id: EX1
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000751/graph
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:19Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0000751",
    "target": "http://purl.obolibrary.org/obo/BTO_0000574", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: 1db250cef56fb17437d2fc7a8e62757f639f52dc6c36919dcb8cbe33580302ea
- evidence_id: EX2
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000751
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:19Z'
  support: supports
  summary: BTO:0000751 leukocyte; inspected definition and typed scope. ["Any of the
    blood cells that are colorless, lack hemoglobin, contain a nucleus, and include
    the lymphocytes, monocytes, neutrophils, eosinophils, and basophils."]
  snapshot_sha256: dc3f8532e9dfec57d9d998dd62a80401a810c5861ea07ae731a75c3a5c26adfb
- evidence_id: EX3
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000775/graph
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:21Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0000775",
    "target": "http://purl.obolibrary.org/obo/BTO_0000751", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/BTO_0000775",
    "target": "http://purl.obolibrary.org/obo/BTO_0001096", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: 01675353e8781be8145e5d5c6f5cab18972510b14408415e411c0a3b9b04ae7d
- evidence_id: EX4
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000775
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:20Z'
  support: supports
  summary: BTO:0000775 lymphocyte; inspected definition and typed scope. ["Any of
    the colorless weakly motile cells originating from stem cells and differentiating
    in lymphoid tissue (as of the thymus or bone marrow) that are the typical cellular
    elements of lymph, include the cellular mediators of immunity, and constitute
    20 to 30 percent of the white blood cells of normal human blood."]
  snapshot_sha256: a3e1e00e7678e82db6dc498ad7b6e393ca0878227dbab125ac5a63a5ff099dd9
- evidence_id: EX5
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000776/graph
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:22Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0000776",
    "target": "http://purl.obolibrary.org/obo/BTO_0000775", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: 6fcc058fc0c551acee88d020c367fb31f09e997d64ad308e8f13f67fce32a92f
- evidence_id: EX6
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000776
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:22Z'
  support: supports
  summary: BTO:0000776 B-lymphocyte; inspected definition and typed scope. ["Any of
    the lymphocytes that have antibody molecules on the surface and comprise the antibody-secreting
    plasma cells when mature."]
  snapshot_sha256: 5b10cc92340d79e7ba798f9e5fb53ec2fa6cd7f5793088c5c64757570a20b0ac
- evidence_id: EX7
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001096/graph
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:24Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0001096",
    "target": "http://purl.obolibrary.org/obo/BTO_0000753", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: c22026d56973b51bc65f948d4b2929b0298fa5d26b44ffa82ae379217b35d10a
- evidence_id: EX8
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001096
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:23Z'
  support: supports
  summary: 'BTO:0001096 lymphoid cell; inspected definition and typed scope. ["Any
    of the cells responsible for the production of immunity mediated by cells or antibodies
    and including lymphocytes, lymphoblasts, and plasma cells. Cells derived from
    stem cells of the lymphoid lineage: large and small lymphocytes, plasma cells."]'
  snapshot_sha256: 788c4fef9b21d66dfa545faaec2f9e1fe762286dc3a1a8c297f8f33f774b4f52
- evidence_id: EX9
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10159052/fullTextXML
  locator: 'Methods and results: bacterial strains and splenic IgM-positive cells'
  accessed_at: '2026-10-15T09:30:21Z'
  support: supports
  summary: PMID:37153602; DOI:10.3389/fimmu.2023.1178462. Aquatic-origin L. cremoris
    WA2-67 strains were added to trout splenocyte cultures to test immune effects.
    B-cell survival or proliferation after exposure does not establish bacterial residence.
    This is a strain-scoped contrast, not the original PREGO citation or a species-wide
    absence finding.
  snapshot_sha256: 33f9d2fe828510a20741510fff549494e8de3bd38e9205d392307c91e00bf2ee
- evidence_id: EX10
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3091627/fullTextXML
  locator: 'Results: B38; Methods: bacterial strains and DNA'
  accessed_at: '2026-10-15T09:27:18Z'
  support: supports
  summary: PMID:20537153; DOI:10.1186/1471-2164-11-368. B38 belongs to gastric B-cell
    MALT-lymphoma patient isolates; isolation involved biopsy homogenization and culture.
    Patient disease context does not demonstrate B-lymphocyte residence. This is not
    identified as the original PREGO pair citation.
  snapshot_sha256: 4d9fa8ee03046bbb4ea7a85a81968a622d50a67283cbc0976730e319461fcc6e
- evidence_id: EX11
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3510171/fullTextXML
  locator: 'Methods: intracellular viable recovery; Results and Figure 2'
  accessed_at: '2026-10-15T09:30:20Z'
  support: supports
  summary: PMID:23209805; DOI:10.1371/journal.pone.0050667. Imaging and recovery after
    extracellular killing support viable intracellular Salmonella in primary human
    B cells and replication in Ramos cells, with different replication outcomes. This
    positive control establishes bounded site eligibility, not any of the displayed
    PREGO pairs.
  snapshot_sha256: 430f7f7332da3ca172e3308b15f7a4e66c6ce96f80bc9313a9016de79d58ed36
- evidence_id: EX12
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3670865/fullTextXML
  locator: 'Introduction and Methods: genome sequencing'
  accessed_at: '2026-10-15T09:28:30Z'
  support: supports
  summary: PMID:23755230; DOI:10.1371/journal.pone.0065425. HUJEG-1 is ATCC 700358,
    and sequencing used a colony-purified stock. The inspected strain context concerns
    soil, mycetoma and pathogenesis, not demonstrated B-cell localization. Gene predictions
    are not imported as habitat mechanisms.
  snapshot_sha256: 1338e530dafe2b37445b6ac55deaf2fecb993913423ea681c77694bd4647b734
- evidence_id: EX13
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
- evidence_id: EX14
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1133849,114615,1245469,1359,191292,2,375177,438753,592205&retmode=xml
  locator: TaxId, ScientificName, Rank, Lineage and aliases
  accessed_at: '2026-10-15T09:26:01Z'
  support: supports
  summary: '[{"id": "NCBITaxon:1133849", "label": "Nocardia brasiliensis ATCC 700358",
    "current_id": "1133849", "current_name": "Nocardia brasiliensis ATCC 700358",
    "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Bacillati;
    Actinomycetota; Actinomycetes; Mycobacteriales; Nocardiaceae; Nocardia; Nocardia
    brasiliensis"}, {"id": "NCBITaxon:1359", "label": "Lactococcus cremoris", "current_id":
    "1359", "current_name": "Lactococcus cremoris", "current_rank": "species", "lineage":
    "cellular organisms; Bacteria; Bacillati; Bacillota; Bacilli; Lactobacillales;
    Streptococcaceae; Lactococcus"}, {"id": "NCBITaxon:592205", "label": "Helicobacter
    pylori B38", "current_id": "592205", "current_name": "Helicobacter pylori B38",
    "current_rank": "strain", "lineage": "cellular organisms; Bacteria; Pseudomonadati;
    Campylobacterota; Epsilonproteobacteria; Campylobacterales; Helicobacteraceae;
    Helicobacter; Helicobacter pylori"}]'
  snapshot_sha256: bc5ad6493aa78574a052359add560693971d71c2e08ddbf4357d39c37e8f7b0b
- evidence_id: ESEARCH
  kind: search
  reference: Local records and maintained inputs
  locator: rg --no-ignore --hidden -l -F -e BTO:0000776 -e B-lymphocyte -e b_lymphocyte
    -e habitatmech:PREGO.cafee0000f curation history research reports data/raw build
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
  reference: reports/yaml_record_review/20261004T091951Z-b_lymphocyte.md
  locator: Historical target review, especially findings and evidence leads
  accessed_at: '2026-10-15T09:37:37Z'
  support: supports
  summary: Historical assessment was consulted for source and issue leads; current
    findings are independently reassessed against the captured inputs and stated authorities.
    It is not structured predecessor lineage.
  snapshot_sha256: 1c76c18e8697e96cd015f290c79c7ed53c99abdfba82d17348d38b6424c88515
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
  - BTO:0000776
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and synonym scope
  outcome: concern
  summary: 'The B-cell identity and lymphocyte superclass are sound, and all three
    PREGO names/counts/ranks reproduce. Reported-from scope is not established by
    the retained channel alone: B38 has gastric-biopsy/lymphoma context, HUJEG-1 has
    culture/mycetoma context, and an independent Lactococcus study measures immune
    responses. Original pair evidence remains necessary.'
  target_ids:
  - BTO:0000776
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
  - EX9
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
- assessment_id: A3
  area: quantity
  topic: Counts, units and ranking provenance
  outcome: supported
  summary: 'Exact source rows reproduce [{"source": "PREGO", "count": 3, "unit": "TAXON"}].
    Every displayed taxon ID/name resolves in NCBI; ranks and pools reproduce the
    exact habitat-keyed rows. Tied PREGO score/direct flags are ordered by taxon ID,
    not abundance. Zero tree counts do not imply microbial absence or erase different
    bulk counts.'
  target_ids:
  - BTO:0000776
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
  - EX12
  - EX13
  - EX14
- assessment_id: A4
  area: completeness
  topic: Source status and optional claims
  outcome: supported
  summary: Full routes reproduce EXACT/SEEDED. Optional parameter, mechanism and characteristic-presence
    claims are not asserted and are not required quotas. Source parent counts, triad
    annotations and adjacent records are not inherited observations.
  target_ids:
  - BTO:0000776
  evidence_ids:
  - E1
  - ESEED
  - ESCHEMA
findings:
- finding_id: F1
  issue_key: b-lymphocyte-prego-occurrence-scope
  category: evidence
  severity: major
  status: open
  certainty: provisional
  title: Retained evidence does not establish cell-site occurrence
  description: 'Recover the manifest-matching PREGO pair evidence and distinguish
    occurrence/localization from disease, assay, or name context. The B-cell identity
    and lymphocyte superclass are sound, and all three PREGO names/counts/ranks reproduce.
    Reported-from scope is not established by the retained channel alone: B38 has
    gastric-biopsy/lymphoma context, HUJEG-1 has culture/mycetoma context, and an
    independent Lactococcus study measures immune responses. Original pair evidence
    remains necessary. Preserve raw totals and source provenance; any qualified association
    pool needs an explicit maintained contract, not hand deletion from generated YAML.'
  target_ids:
  - BTO:0000776
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
  - EX9
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
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
  - https://github.com/CultureBotAI/HabitatMech/issues/1367
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - BTO:0000776
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
  description: 'Recover the manifest-matching PREGO pair evidence and distinguish
    occurrence/localization from disease, assay, or name context. The B-cell identity
    and lymphocyte superclass are sound, and all three PREGO names/counts/ranks reproduce.
    Reported-from scope is not established by the retained channel alone: B38 has
    gastric-biopsy/lymphoma context, HUJEG-1 has culture/mycetoma context, and an
    independent Lactococcus study measures immune responses. Original pair evidence
    remains necessary. Preserve raw totals and source provenance; any qualified association
    pool needs an explicit maintained contract, not hand deletion from generated YAML.
    No repair is performed by this review.'
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
