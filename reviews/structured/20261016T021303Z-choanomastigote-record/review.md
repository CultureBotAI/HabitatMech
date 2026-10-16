# Record review: choanomastigote (BTO:0003434)

- Review: 20261016T021303Z-choanomastigote-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-16T02:01:22Z
- Finished UTC: 2026-10-16T02:13:03Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

BTO defines a Crithidia developmental form and places it under trypanosomoid form. PREGO instead supplies choanoflagellate-related aliases and Algoriphagus machipongonensis. Current NCBI recognizes Algoriphagus sp. PR1 as an alias; the primary PR1 abstract names Salpingoeca rosetta as its predator. This is a different eukaryotic context from Crithidia. Recover original pair and dictionary evidence before retargeting the source, deleting an association, or deciding a host-associated environment identity.

## Scope And Provenance

Full field-by-field review of this one generated record.

Selection: Next 24 unreviewed identifiers in deterministic path order from ignored-inclusive 3209-record census; this bundle assesses exactly one, not a proxy sample.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 5fef9bb871a510550a3f70c45118805ac7c8d9a8.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0003434 | data/habitats/host_associated/choanomastigote.yaml | generated | choanomastigote |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0003434 | Finished 2026-10-16T02:02:28Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/choanomastigote.yaml |
| validate-strict | passed | True | BTO:0003434 | Finished 2026-10-16T02:04:22Z. uv run python scripts/validate_strict.py data/habitats/host_associated/cervical_cancer.yaml data/habitats/host_associated/cervical_neck_nodes.yaml data/habitats/host_associated/cervix.yaml data/habitats/host_associated/cervix__0de03fa8.yaml data/habitats/host_associated/chago_k_1_cell.yaml data/habitats/host_associated/cho.yaml data/habitats/host_associated/choanomastigote.yaml data/habitats/host_associated/cholesteatoma_tissue.yaml data/habitats/host_associated/chorionic_villi.yaml data/habitats/host_associated/chorionic_villi__9af464db.yaml data/habitats/host_associated/chyme.yaml data/habitats/host_associated/chyme__0bfd2730.yaml data/habitats/host_associated/cibarium_preoral_cavity.yaml data/habitats/host_associated/ciliates.yaml data/habitats/host_associated/ciliates__df51eda4.yaml data/habitats/host_associated/ciliophora.yaml data/habitats/host_associated/circulatory_system.yaml data/habitats/host_associated/circulatory_system__241de4de.yaml data/habitats/host_associated/circulatory_system__5b3debaf.yaml data/habitats/host_associated/circulatory_system__745592ee.yaml data/habitats/host_associated/circulatory_system__7e4ecb0e.yaml data/habitats/host_associated/circulatory_system__90d88932.yaml data/habitats/host_associated/circulatory_system__e49da8a0.yaml data/habitats/host_associated/circulatory_system__f5b69d9c.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | BTO:0003434 | Finished 2026-10-16T02:04:39Z. No issues found<br>830 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | BTO:0003434 | Finished 2026-10-16T02:04:40Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | BTO:0003434 | Finished 2026-10-16T02:05:09Z. expected 3209 records, found 3209 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | BTO:0003434 | Finished 2026-10-16T02:05:15Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | BTO:0003434 | Finished 2026-10-16T02:05:44Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | BTO:0003434 | Finished 2026-10-16T02:07:01Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1173<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2063<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-base hosted QC | passed | True | BTO:0003434 | Verified 2026-10-16T01:59:09Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38835150071 |
| Standalone citation validator applicability | not_applicable | False | BTO:0003434 | No standalone citation checker documented for evidence-free generated targets. Stable references checked with native gates/current authorities; causal validation ran globally. |

## Scientific And Domain Assessments

### Identity, definition, aliases, source scope and hierarchy

identity: concern. Targets: BTO:0003434.

BTO defines a Crithidia developmental form and places it under trypanosomoid form. PREGO instead supplies choanoflagellate-related aliases and Algoriphagus machipongonensis. Current NCBI recognizes Algoriphagus sp. PR1 as an alias; the primary PR1 abstract names Salpingoeca rosetta as its predator. This is a different eukaryotic context from Crithidia. Recover original pair and dictionary evidence before retargeting the source, deleting an association, or deciding a host-associated environment identity.

### Counts, units, ranks and candidate pools

quantity: supported. Targets: BTO:0003434.

Frozen source rows reproduce every emitted count/unit and displayed taxon score/rank/pool. Zero tree counts are omitted; supplemental biosamples, triads and study membership are nonadditive. {"assertions": [{"source": "PREGO", "count": 1, "unit": "TAXON", "row": {"row": 639, "data": {"prego_id": "BTO:0003434", "ontology": "BTO", "biolink_category": "biolink:GrossAnatomicalStructure", "taxon_count": "1", "direct_assertion_count": "1", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms": "choanoflagellate&#124;choanoflagellates&#124;choanomastigote&#124;choanomastigotes&#124;collared flagellate&#124;collared flagellate s"}}}], "taxa": [{"id": "NCBITaxon:388413", "source": "PREGO", "label": "Algoriphagus machipongonensis", "current_id": "388413", "current_name": "Algoriphagus machipongonensis", "rank": "species", "direct_match": true, "recognized_alias": true, "other_names": ["Algoriphagus sp. PR1", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            "], "source_row": {"row": 2780, "data": {"prego_id": "BTO:0003434", "rank": "1", "taxon_id": "NCBITaxon:388413", "taxon_label": "Algoriphagus machipongonensis", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}}]}

### Native status and optional evidence

completeness: supported. Targets: BTO:0003434.

Executed native resolution reproduces EXACT/SEEDED. No environmental parameters, causal graphs, discussions, datasets or characteristic-presence claims are asserted. Missing optional fields do not authorize invented content. Parent mechanisms are not inherited.

### Native checks and reproducibility

schema: supported. Targets: BTO:0003434.

All 31 baseline commands passed: target schema, strict cohort, 830 histories, provenance, exact 3209-record reproduction, 32 causal overlays, 110 term requests and configured label checks. Hosted QC matches the exact base. Deterministic validity is not scientific approval.

## Findings

### F1: Recover original pair and dictionary evidence before interpreting localization

major / open / provisional; issue key: choanomastigote-prego-identity-evidence.

BTO defines a Crithidia developmental form and places it under trypanosomoid form. PREGO instead supplies choanoflagellate-related aliases and Algoriphagus machipongonensis. Current NCBI recognizes Algoriphagus sp. PR1 as an alias; the primary PR1 abstract names Salpingoeca rosetta as its predator. This is a different eukaryotic context from Crithidia. Recover original pair and dictionary evidence before retargeting the source, deleting an association, or deciding a host-associated environment identity. Recover manifest-matching pair and alias provenance; distinguish source association from direct localization. Preserve current counts and taxa pending that assessment.

## Recommended Actions And Acceptance Checks

### ACT1

BTO defines a Crithidia developmental form and places it under trypanosomoid form. PREGO instead supplies choanoflagellate-related aliases and Algoriphagus machipongonensis. Current NCBI recognizes Algoriphagus sp. PR1 as an alias; the primary PR1 abstract names Salpingoeca rosetta as its predator. This is a different eukaryotic context from Crithidia. Recover original pair and dictionary evidence before retargeting the source, deleting an association, or deciding a host-associated environment identity. Recover manifest-matching pair and alias provenance; distinguish source association from direct localization. Preserve current counts and taxa pending that assessment. No repair is performed by this review.

- Regress the exact claim, preserving independent valid genera, raw provenance and source counts/units. Change native status or mappings only when supported by the authorized ITEM assessment; never decrement source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/choanomastigote.yaml; Full target YAML | supports | All fields and entire generated history read. |
| ERULE | docs/CURATION.md; Identity, parents, evidence and native status | supports | All parent contributions must be strictly broader. Optional absence and native SEEDED status are not inherently defects. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; HabitatRecord, SourceAttestation, TaxonAssociation | supports | Source mapping endpoints are source-to-record. Associations are not characteristic presence. |
| ESEED | src/habitatmech/seed.py; Executed native source resolution and complete document reproduction | supports | [{"mint": "habitatmech:PREGO.400eb17f65", "automatic": {"identifier": "BTO:0003434", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "BTO:0003434", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}}] |
| EEXTRACT | src/habitatmech/extract.py; Source projections and count/rank/score interpretation | supports | Exact source rows reproduce source-specific units, maximum scores and ranks. Frozen PREGO projection lacks original pair citation links. |
| ET5 | data/raw/prego_habitat_taxa.tsv; Physical TSV rows 2780 | supports | [{"row": 2780, "data": {"prego_id": "BTO:0003434", "rank": "1", "taxon_id": "NCBITaxon:388413", "taxon_label": "Algoriphagus machipongonensis", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}] |
| ET6 | data/raw/prego_habitats.tsv; Physical TSV rows 639 | supports | [{"row": 639, "data": {"prego_id": "BTO:0003434", "ontology": "BTO", "biolink_category": "biolink:GrossAnatomicalStructure", "taxon_count": "1", "direct_assertion_count": "1", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms": "choanoflagellate&#124;choanoflagellates&#124;choanomastigote&#124;choanomastigotes&#124;collared flagellate&#124;collared flagellate s"}}] |
| ET7 | data/raw/ontology_subclass_edges.tsv; Physical TSV rows 69,2398 | supports | [{"row": 69, "data": {"subject": "BTO:0000092", "predicate": "rdfs:subClassOf", "object": "BTO:0002503"}}, {"row": 2398, "data": {"subject": "BTO:0003434", "predicate": "rdfs:subClassOf", "object": "BTO:0000092"}}] |
| ET8 | data/raw/ontology_terms.tsv; Physical TSV rows 94,3434 | supports | [{"row": 94, "data": {"term_id": "BTO:0000092", "ontology": "BTO", "label": "trypanosomoid form", "definition": "Any of a genus (Trypanosoma) of parasitic flagellate protozoans that infest the blood of various vertebrates including humans, are usually transmitted by the bite of an insect, and include some that cause serious disease (as sleeping sickness).", "synonyms": "", "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}}, {"row": 3434, "data": {"term_id": "BTO:0003434", "ontology": "BTO", "label": "choanomastigote", "definition": "A term, in the series used to describe developmental stages of the parasitic flagellates, denoting the barleycorn form of the flagellate in the genus Crithidia characterised by a collarlike extension surrounding the anterior and through which the single flagellum emerges.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}] |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000092/graph; BTO_0000092-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000092", "target": "http://purl.obolibrary.org/obo/BTO_0002503", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000092; BTO_0000092.json | context_only | Current term identity, active status and definition: {"obo_id": "BTO:0000092", "label": "trypanosomoid form", "is_obsolete": false, "description": ["Any of a genus (Trypanosoma) of parasitic flagellate protozoans that infest the blood of various vertebrates including humans, are usually transmitted by the bite of an insect, and include some that cause serious disease (as sleeping sickness)."]} |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0003434/graph; BTO_0003434-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0003434", "target": "http://purl.obolibrary.org/obo/BTO_0000092", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0003434; BTO_0003434.json | context_only | Current term identity, active status and definition: {"obo_id": "BTO:0003434", "label": "choanomastigote", "is_obsolete": false, "description": ["A term, in the series used to describe developmental stages of the parasitic flagellates, denoting the barleycorn form of the flagellate in the genus Crithidia characterised by a collarlike extension surrounding the anterior and through which the single flagellum emerges."]} |
| EX5 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML; PMC8879827.xml | context_only | PREGO methods identify association channels and score-three BioProject-associated abstract mining. Source channel and score are not proof of direct habitat localization or characteristic presence. The original extraction route of either particular pair remains unresolved. |
| EX6 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PMCID%3APMC3067637&amp;format=json&amp;resultType=core; abstract-PMC3067637.json | context_only | PMID:21183675; DOI:10.1128/JB.01421-10. Primary abstract inspected: Algoriphagus PR1 interacts with its choanoflagellate predator Salpingoeca rosetta. This is not Crithidia developmental-stage evidence. Full-text XML failed and direct PMC returned a browser challenge. |
| EX7 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=388413,582419&amp;retmode=xml; taxonomy.xml | context_only | Current NCBI identities and source-label comparisons: [{"id": "NCBITaxon:388413", "source": "PREGO", "label": "Algoriphagus machipongonensis", "current_id": "388413", "current_name": "Algoriphagus machipongonensis", "rank": "species", "direct_match": true, "recognized_alias": true}] |
| ESEARCH | Maintained inputs and review archive; rg --no-ignore --hidden -l -F -e BTO:0003434 -e choanomastigote -e choanomastigote -e habitatmech:PREGO.400eb17f65 curation history research reports data/raw build reviews | context_only | Exact TSV rows parsed separately; broad label matches are leads, not all read. No earlier formal structured target observation. |
| EAVAIL | Configured kg-microbe checkout; find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe -type f -ipath '*prego*' | context_only | No PREGO-named files found in this checkout. Original pair exports remain unavailable here, not proven absent globally. |

## Limits And Additional Notes

- Source counts, score channels and ranks do not establish prevalence, viability or characteristic presence. Original specimen-level and pair-level evidence has not been reconstructed exhaustively.
- Configured label validation skipped 2063 no-adapter pairs; displayed target TaxIds were resolved separately with current NCBI.
- Exact-base full QC is verified hosted evidence for unchanged scientific inputs, not a new local full-QC run or validation of these new review bundles.
- iModulonDB is not applicable: target claims do not assert genes, regulators or expression modules. No paid research or native status promotion.
- Original PREGO pair exports are unavailable in the configured checkout; association and ambiguous RELATED aliases are retained pending evidence, not deleted based on a competing origin.
- Native working-tree capture retained; input hashes additionally compared with exact base blobs 5fef9bb871a510550a3f70c45118805ac7c8d9a8.
- No previous structured target observation found in ignored-inclusive archive traversal. Historical prose is not a formal predecessor or automatic disposition.
- This immutable observation does not itself perform curation. Separately authorized PR remediation must retain its findings and lineage.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T021303Z-choanomastigote-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: choanomastigote (BTO:0003434)'
started_at: '2026-10-16T02:01:22Z'
finished_at: '2026-10-16T02:13:03Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent assessed sources and target; not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: BTO defines a Crithidia developmental form and places it under trypanosomoid
  form. PREGO instead supplies choanoflagellate-related aliases and Algoriphagus machipongonensis.
  Current NCBI recognizes Algoriphagus sp. PR1 as an alias; the primary PR1 abstract
  names Salpingoeca rosetta as its predator. This is a different eukaryotic context
  from Crithidia. Recover original pair and dictionary evidence before retargeting
  the source, deleting an association, or deciding a host-associated environment identity.
source:
  git_revision: 5fef9bb871a510550a3f70c45118805ac7c8d9a8
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
    sha256: e5cb2e09f72dd4b18e069c0e2576e25e13e56c9991f4eb5ae47416345e247578
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 37dc4b40642d19e7b5c3262f368d12daa82e03115e7731a2326ae88785ceff5b
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 7b7e21d2fa3350efb85fc3cf79725465c09adba8b4fe100b004813deb8a2eed7
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: a56f07a45fb743fb7b0e61f83ef70fa5ed61a3c892cfaf36e3428967c548dc5e
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: bc7a13d922c179cd9bcd4d37b348bc90a39b08a4dafba7af4ed0039ad99621c3
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: ee559f7b45b4af2d72a078c45d1a3b676785d34305f286e9738f95771dbaccfd
    role: context
  - path: data/habitats/RETIRED.tsv
    sha256: 747e6a5612dc0b7ed881b9fb323fd57ab3c75794d9ee5ebb9d59b2be57dbf8cd
    role: context
  - path: data/habitats/host_associated/choanomastigote.yaml
    sha256: 86706d881f53ab0ed4fc1142e8b222717e90515ad4bccf5e7533eade4d33e789
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
targets:
- target_id: BTO:0003434
  path: data/habitats/host_associated/choanomastigote.yaml
  label: choanomastigote
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
  description: Full field-by-field review of this one generated record.
  selection: Next 24 unreviewed identifiers in deterministic path order from ignored-inclusive
    3209-record census; this bundle assesses exactly one, not a proxy sample.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - BTO:0003434
  exclusions:
  - target: Other records, original source specimens, SSSOM/KGX
    reason: Parent context does not expand target scope; exports and individual specimens
      are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/choanomastigote.yaml
  exit_code: 0
  target_ids:
  - BTO:0003434
  summary: "Finished 2026-10-16T02:02:28Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/choanomastigote.yaml"
  scope_note: Individual schema; strict covers all 24 targets; other gates have documented
    full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/cervical_cancer.yaml data/habitats/host_associated/cervical_neck_nodes.yaml
    data/habitats/host_associated/cervix.yaml data/habitats/host_associated/cervix__0de03fa8.yaml
    data/habitats/host_associated/chago_k_1_cell.yaml data/habitats/host_associated/cho.yaml
    data/habitats/host_associated/choanomastigote.yaml data/habitats/host_associated/cholesteatoma_tissue.yaml
    data/habitats/host_associated/chorionic_villi.yaml data/habitats/host_associated/chorionic_villi__9af464db.yaml
    data/habitats/host_associated/chyme.yaml data/habitats/host_associated/chyme__0bfd2730.yaml
    data/habitats/host_associated/cibarium_preoral_cavity.yaml data/habitats/host_associated/ciliates.yaml
    data/habitats/host_associated/ciliates__df51eda4.yaml data/habitats/host_associated/ciliophora.yaml
    data/habitats/host_associated/circulatory_system.yaml data/habitats/host_associated/circulatory_system__241de4de.yaml
    data/habitats/host_associated/circulatory_system__5b3debaf.yaml data/habitats/host_associated/circulatory_system__745592ee.yaml
    data/habitats/host_associated/circulatory_system__7e4ecb0e.yaml data/habitats/host_associated/circulatory_system__90d88932.yaml
    data/habitats/host_associated/circulatory_system__e49da8a0.yaml data/habitats/host_associated/circulatory_system__f5b69d9c.yaml
  exit_code: 0
  target_ids:
  - BTO:0003434
  summary: "Finished 2026-10-16T02:04:22Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/cervical_cancer.yaml data/habitats/host_associated/cervical_neck_nodes.yaml\
    \ data/habitats/host_associated/cervix.yaml data/habitats/host_associated/cervix__0de03fa8.yaml\
    \ data/habitats/host_associated/chago_k_1_cell.yaml data/habitats/host_associated/cho.yaml\
    \ data/habitats/host_associated/choanomastigote.yaml data/habitats/host_associated/cholesteatoma_tissue.yaml\
    \ data/habitats/host_associated/chorionic_villi.yaml data/habitats/host_associated/chorionic_villi__9af464db.yaml\
    \ data/habitats/host_associated/chyme.yaml data/habitats/host_associated/chyme__0bfd2730.yaml\
    \ data/habitats/host_associated/cibarium_preoral_cavity.yaml data/habitats/host_associated/ciliates.yaml\
    \ data/habitats/host_associated/ciliates__df51eda4.yaml data/habitats/host_associated/ciliophora.yaml\
    \ data/habitats/host_associated/circulatory_system.yaml data/habitats/host_associated/circulatory_system__241de4de.yaml\
    \ data/habitats/host_associated/circulatory_system__5b3debaf.yaml data/habitats/host_associated/circulatory_system__745592ee.yaml\
    \ data/habitats/host_associated/circulatory_system__7e4ecb0e.yaml data/habitats/host_associated/circulatory_system__90d88932.yaml\
    \ data/habitats/host_associated/circulatory_system__e49da8a0.yaml data/habitats/host_associated/circulatory_system__f5b69d9c.yaml\n\
    Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      24\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Individual schema; strict covers all 24 targets; other gates have documented
    full-corpus scope.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - BTO:0003434
  summary: 'Finished 2026-10-16T02:04:39Z. No issues found

    830 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Individual schema; strict covers all 24 targets; other gates have documented
    full-corpus scope.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - BTO:0003434
  summary: "Finished 2026-10-16T02:04:40Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Individual schema; strict covers all 24 targets; other gates have documented
    full-corpus scope.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - BTO:0003434
  summary: "Finished 2026-10-16T02:05:09Z. expected 3209 records, found 3209 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Individual schema; strict covers all 24 targets; other gates have documented
    full-corpus scope.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - BTO:0003434
  summary: "Finished 2026-10-16T02:05:15Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Individual schema; strict covers all 24 targets; other gates have documented
    full-corpus scope.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - BTO:0003434
  summary: "Finished 2026-10-16T02:05:44Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Individual schema; strict covers all 24 targets; other gates have documented
    full-corpus scope.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - BTO:0003434
  summary: "Finished 2026-10-16T02:07:01Z. id↔label correspondence summary:\n    \
    \      OK_CANONICAL: 1173\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2063\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Individual schema; strict covers all 24 targets; other gates have documented
    full-corpus scope.
- check_id: CCI
  name: Exact-base hosted QC
  status: passed
  required: true
  command: gh run view 38835150071 --repo CultureBotAI/HabitatMech --json headSha,conclusion,url,jobs
  exit_code: 0
  target_ids:
  - BTO:0003434
  summary: Verified 2026-10-16T01:59:09Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38835150071
  scope_note: Unchanged scientific-input baseline only; new output bundles require
    separate validation.
- check_id: CREF
  name: Standalone citation validator applicability
  status: not_applicable
  required: false
  target_ids:
  - BTO:0003434
  summary: No standalone citation checker documented for evidence-free generated targets.
    Stable references checked with native gates/current authorities; causal validation
    ran globally.
  scope_note: No invented command or exit code.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/choanomastigote.yaml
  locator: Full target YAML
  accessed_at: '2026-10-16T02:13:03Z'
  support: supports
  summary: All fields and entire generated history read.
  snapshot_sha256: 86706d881f53ab0ed4fc1142e8b222717e90515ad4bccf5e7533eade4d33e789
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, parents, evidence and native status
  accessed_at: '2026-10-16T02:13:03Z'
  support: supports
  summary: All parent contributions must be strictly broader. Optional absence and
    native SEEDED status are not inherently defects.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: HabitatRecord, SourceAttestation, TaxonAssociation
  accessed_at: '2026-10-16T02:13:03Z'
  support: supports
  summary: Source mapping endpoints are source-to-record. Associations are not characteristic
    presence.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native source resolution and complete document reproduction
  accessed_at: '2026-10-16T02:13:03Z'
  support: supports
  summary: '[{"mint": "habitatmech:PREGO.400eb17f65", "automatic": {"identifier":
    "BTO:0003434", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded",
    "category": null, "reviewed": false, "decision": null}, "final": {"identifier":
    "BTO:0003434", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded",
    "category": null, "reviewed": false, "decision": null}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: Source projections and count/rank/score interpretation
  accessed_at: '2026-10-16T02:13:03Z'
  support: supports
  summary: Exact source rows reproduce source-specific units, maximum scores and ranks.
    Frozen PREGO projection lacks original pair citation links.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/prego_habitat_taxa.tsv
  locator: Physical TSV rows 2780
  accessed_at: '2026-10-16T02:13:03Z'
  support: supports
  summary: '[{"row": 2780, "data": {"prego_id": "BTO:0003434", "rank": "1", "taxon_id":
    "NCBITaxon:388413", "taxon_label": "Algoriphagus machipongonensis", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}]'
  snapshot_sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
- evidence_id: ET6
  kind: database
  reference: data/raw/prego_habitats.tsv
  locator: Physical TSV rows 639
  accessed_at: '2026-10-16T02:13:03Z'
  support: supports
  summary: '[{"row": 639, "data": {"prego_id": "BTO:0003434", "ontology": "BTO", "biolink_category":
    "biolink:GrossAnatomicalStructure", "taxon_count": "1", "direct_assertion_count":
    "1", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms":
    "choanoflagellate|choanoflagellates|choanomastigote|choanomastigotes|collared
    flagellate|collared flagellate s"}}]'
  snapshot_sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
- evidence_id: ET7
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: Physical TSV rows 69,2398
  accessed_at: '2026-10-16T02:13:03Z'
  support: supports
  summary: '[{"row": 69, "data": {"subject": "BTO:0000092", "predicate": "rdfs:subClassOf",
    "object": "BTO:0002503"}}, {"row": 2398, "data": {"subject": "BTO:0003434", "predicate":
    "rdfs:subClassOf", "object": "BTO:0000092"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET8
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 94,3434
  accessed_at: '2026-10-16T02:13:03Z'
  support: supports
  summary: '[{"row": 94, "data": {"term_id": "BTO:0000092", "ontology": "BTO", "label":
    "trypanosomoid form", "definition": "Any of a genus (Trypanosoma) of parasitic
    flagellate protozoans that infest the blood of various vertebrates including humans,
    are usually transmitted by the bite of an insect, and include some that cause
    serious disease (as sleeping sickness).", "synonyms": "", "deprecated": "", "directly_referenced":
    "FALSE", "label_only": "FALSE"}}, {"row": 3434, "data": {"term_id": "BTO:0003434",
    "ontology": "BTO", "label": "choanomastigote", "definition": "A term, in the series
    used to describe developmental stages of the parasitic flagellates, denoting the
    barleycorn form of the flagellate in the genus Crithidia characterised by a collarlike
    extension surrounding the anterior and through which the single flagellum emerges.",
    "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only":
    "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EX1
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000092/graph
  locator: BTO_0000092-graph.json
  accessed_at: '2026-10-16T02:01:40Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000092",
    "target": "http://purl.obolibrary.org/obo/BTO_0002503", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: 2159bc0504144031decf448328a23f8b51943588d8846bf38294a89a06cefbf6
- evidence_id: EX2
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000092
  locator: BTO_0000092.json
  accessed_at: '2026-10-16T02:01:40Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "BTO:0000092",
    "label": "trypanosomoid form", "is_obsolete": false, "description": ["Any of a
    genus (Trypanosoma) of parasitic flagellate protozoans that infest the blood of
    various vertebrates including humans, are usually transmitted by the bite of an
    insect, and include some that cause serious disease (as sleeping sickness)."]}'
  snapshot_sha256: 9af9c1b644e8b5884ca44bdc5f2630bdaf22291755e7d838dd4b670cc216be5e
- evidence_id: EX3
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0003434/graph
  locator: BTO_0003434-graph.json
  accessed_at: '2026-10-16T02:01:45Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0003434",
    "target": "http://purl.obolibrary.org/obo/BTO_0000092", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: 9e15740a46485002466d3e9f2ccb20ee187a6f59871c10dbb24e1fea9006e1a2
- evidence_id: EX4
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0003434
  locator: BTO_0003434.json
  accessed_at: '2026-10-16T02:01:44Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "BTO:0003434",
    "label": "choanomastigote", "is_obsolete": false, "description": ["A term, in
    the series used to describe developmental stages of the parasitic flagellates,
    denoting the barleycorn form of the flagellate in the genus Crithidia characterised
    by a collarlike extension surrounding the anterior and through which the single
    flagellum emerges."]}'
  snapshot_sha256: 602ac274c1866dc6fd4ac8d7ac595a1da84ab46859ab6ff0c626415258b57368
- evidence_id: EX5
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML
  locator: PMC8879827.xml
  accessed_at: '2026-10-16T02:08:54Z'
  support: context_only
  summary: PREGO methods identify association channels and score-three BioProject-associated
    abstract mining. Source channel and score are not proof of direct habitat localization
    or characteristic presence. The original extraction route of either particular
    pair remains unresolved.
  snapshot_sha256: 375f0fde4d07bb823cb9106aa4567bc0ef03c2866af0b2a7740b543f50687c25
- evidence_id: EX6
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PMCID%3APMC3067637&format=json&resultType=core
  locator: abstract-PMC3067637.json
  accessed_at: '2026-10-16T02:10:52Z'
  support: context_only
  summary: 'PMID:21183675; DOI:10.1128/JB.01421-10. Primary abstract inspected: Algoriphagus
    PR1 interacts with its choanoflagellate predator Salpingoeca rosetta. This is
    not Crithidia developmental-stage evidence. Full-text XML failed and direct PMC
    returned a browser challenge.'
  snapshot_sha256: 94952758af30605bf1e3beb4db632fa6b2f4f7602bff6dfe4ac34f07cf7c7100
- evidence_id: EX7
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=388413,582419&retmode=xml
  locator: taxonomy.xml
  accessed_at: '2026-10-16T02:02:06Z'
  support: context_only
  summary: 'Current NCBI identities and source-label comparisons: [{"id": "NCBITaxon:388413",
    "source": "PREGO", "label": "Algoriphagus machipongonensis", "current_id": "388413",
    "current_name": "Algoriphagus machipongonensis", "rank": "species", "direct_match":
    true, "recognized_alias": true}]'
  snapshot_sha256: 04127d6ebd0c4531ff9c54591764b8dc79970b2f5c8fc9b782c7e7f6d85dcc0a
- evidence_id: ESEARCH
  kind: search
  reference: Maintained inputs and review archive
  locator: rg --no-ignore --hidden -l -F -e BTO:0003434 -e choanomastigote -e choanomastigote
    -e habitatmech:PREGO.400eb17f65 curation history research reports data/raw build
    reviews
  accessed_at: '2026-10-16T02:00:57Z'
  support: context_only
  summary: Exact TSV rows parsed separately; broad label matches are leads, not all
    read. No earlier formal structured target observation.
  search_scope: curation, history, research, reports, data/raw, build and reviews
    including hidden/ignored content; full structured YAML traversal.
- evidence_id: EAVAIL
  kind: search
  reference: Configured kg-microbe checkout
  locator: find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe
    -type f -ipath '*prego*'
  accessed_at: '2026-10-16T02:09:00Z'
  support: context_only
  summary: No PREGO-named files found in this checkout. Original pair exports remain
    unavailable here, not proven absent globally.
  search_scope: find across the configured checkout including hidden/ignored files.
assessments:
- assessment_id: A1
  area: identity
  topic: Identity, definition, aliases, source scope and hierarchy
  outcome: concern
  summary: BTO defines a Crithidia developmental form and places it under trypanosomoid
    form. PREGO instead supplies choanoflagellate-related aliases and Algoriphagus
    machipongonensis. Current NCBI recognizes Algoriphagus sp. PR1 as an alias; the
    primary PR1 abstract names Salpingoeca rosetta as its predator. This is a different
    eukaryotic context from Crithidia. Recover original pair and dictionary evidence
    before retargeting the source, deleting an association, or deciding a host-associated
    environment identity.
  target_ids:
  - BTO:0003434
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EEXTRACT
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
- assessment_id: A2
  area: quantity
  topic: Counts, units, ranks and candidate pools
  outcome: supported
  summary: 'Frozen source rows reproduce every emitted count/unit and displayed taxon
    score/rank/pool. Zero tree counts are omitted; supplemental biosamples, triads
    and study membership are nonadditive. {"assertions": [{"source": "PREGO", "count":
    1, "unit": "TAXON", "row": {"row": 639, "data": {"prego_id": "BTO:0003434", "ontology":
    "BTO", "biolink_category": "biolink:GrossAnatomicalStructure", "taxon_count":
    "1", "direct_assertion_count": "1", "max_prego_score": "3", "channels": "annotated_genomes_isolates",
    "prego_synonyms": "choanoflagellate|choanoflagellates|choanomastigote|choanomastigotes|collared
    flagellate|collared flagellate s"}}}], "taxa": [{"id": "NCBITaxon:388413", "source":
    "PREGO", "label": "Algoriphagus machipongonensis", "current_id": "388413", "current_name":
    "Algoriphagus machipongonensis", "rank": "species", "direct_match": true, "recognized_alias":
    true, "other_names": ["Algoriphagus sp. PR1", "\n            ", "\n            ",
    "\n            ", "\n            ", "\n            ", "\n            ", "\n            ",
    "\n            "], "source_row": {"row": 2780, "data": {"prego_id": "BTO:0003434",
    "rank": "1", "taxon_id": "NCBITaxon:388413", "taxon_label": "Algoriphagus machipongonensis",
    "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates",
    "corroborated_by": ""}}}]}'
  target_ids:
  - BTO:0003434
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
- assessment_id: A3
  area: completeness
  topic: Native status and optional evidence
  outcome: supported
  summary: Executed native resolution reproduces EXACT/SEEDED. No environmental parameters,
    causal graphs, discussions, datasets or characteristic-presence claims are asserted.
    Missing optional fields do not authorize invented content. Parent mechanisms are
    not inherited.
  target_ids:
  - BTO:0003434
  evidence_ids:
  - E1
  - ESCHEMA
  - ESEED
- assessment_id: A4
  area: schema
  topic: Native checks and reproducibility
  outcome: supported
  summary: 'All 31 baseline commands passed: target schema, strict cohort, 830 histories,
    provenance, exact 3209-record reproduction, 32 causal overlays, 110 term requests
    and configured label checks. Hosted QC matches the exact base. Deterministic validity
    is not scientific approval.'
  target_ids:
  - BTO:0003434
  evidence_ids:
  - E1
  - ERULE
findings:
- finding_id: F1
  issue_key: choanomastigote-prego-identity-evidence
  category: evidence
  severity: major
  status: open
  certainty: provisional
  title: Recover original pair and dictionary evidence before interpreting localization
  description: BTO defines a Crithidia developmental form and places it under trypanosomoid
    form. PREGO instead supplies choanoflagellate-related aliases and Algoriphagus
    machipongonensis. Current NCBI recognizes Algoriphagus sp. PR1 as an alias; the
    primary PR1 abstract names Salpingoeca rosetta as its predator. This is a different
    eukaryotic context from Crithidia. Recover original pair and dictionary evidence
    before retargeting the source, deleting an association, or deciding a host-associated
    environment identity. Recover manifest-matching pair and alias provenance; distinguish
    source association from direct localization. Preserve current counts and taxa
    pending that assessment.
  target_ids:
  - BTO:0003434
  field_paths:
  - characteristic_taxa
  - synonyms
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EEXTRACT
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
  - EAVAIL
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/MANIFEST.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported hierarchy, mapping or source-evidence
    semantics; correct deterministic reproduction does not establish scientific support.
  external_issues: []
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - BTO:0003434
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/MANIFEST.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  description: BTO defines a Crithidia developmental form and places it under trypanosomoid
    form. PREGO instead supplies choanoflagellate-related aliases and Algoriphagus
    machipongonensis. Current NCBI recognizes Algoriphagus sp. PR1 as an alias; the
    primary PR1 abstract names Salpingoeca rosetta as its predator. This is a different
    eukaryotic context from Crithidia. Recover original pair and dictionary evidence
    before retargeting the source, deleting an association, or deciding a host-associated
    environment identity. Recover manifest-matching pair and alias provenance; distinguish
    source association from direct localization. Preserve current counts and taxa
    pending that assessment. No repair is performed by this review.
  generator: Controlled source refresh when required, then just seed, guarded just
    seed-canary, just seed-apply, and dependent term-request/map/site/redirect regeneration.
  acceptance_checks:
  - Regress the exact claim, preserving independent valid genera, raw provenance and
    source counts/units. Change native status or mappings only when supported by the
    authorized ITEM assessment; never decrement source totals by hand.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
limitations:
- Source counts, score channels and ranks do not establish prevalence, viability or
  characteristic presence. Original specimen-level and pair-level evidence has not
  been reconstructed exhaustively.
- Configured label validation skipped 2063 no-adapter pairs; displayed target TaxIds
  were resolved separately with current NCBI.
- Exact-base full QC is verified hosted evidence for unchanged scientific inputs,
  not a new local full-QC run or validation of these new review bundles.
- 'iModulonDB is not applicable: target claims do not assert genes, regulators or
  expression modules. No paid research or native status promotion.'
- Original PREGO pair exports are unavailable in the configured checkout; association
  and ambiguous RELATED aliases are retained pending evidence, not deleted based on
  a competing origin.
notes:
- Native working-tree capture retained; input hashes additionally compared with exact
  base blobs 5fef9bb871a510550a3f70c45118805ac7c8d9a8.
- No previous structured target observation found in ignored-inclusive archive traversal.
  Historical prose is not a formal predecessor or automatic disposition.
- This immutable observation does not itself perform curation. Separately authorized
  PR remediation must retain its findings and lineage.
tags:
- individual-scientific-review
- host-associated
```
