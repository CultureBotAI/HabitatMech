# Record review: Cartilage (habitatmech:GOLD.e1b5f9301d)

- Review: 20261015T212548Z-cartilage__bd8c407c-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T21:13:32Z
- Finished UTC: 2026-10-15T21:25:48Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Fish cartilage has a defensible generic cartilage genus and distinct host-scoped mint. Cartilage tissue is not the complete fish skeletal system. A prior favorable hierarchy assessment conflated source-path containment with is-a. The emitted narrow predicate also has the separate endpoint-contract defect; neither issue requires merging this record into mammalian cartilage.

## Scope And Provenance

Full field-by-field scientific assessment of this exact target at 62952fb7cdf223af9d1ffbf1cc2f556b22f7ee6b.

Selection: One of the next 24 path-ordered unreviewed identifiers in the ignored-inclusive 3208-record census. This bundle assesses one exact identifier, not a proxy sample.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 62952fb7cdf223af9d1ffbf1cc2f556b22f7ee6b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.e1b5f9301d | data/habitats/host_associated/cartilage__bd8c407c.yaml | generated | Cartilage |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.e1b5f9301d | Finished 2026-10-15T21:13:35Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/cartilage__bd8c407c.yaml |
| validate-strict | passed | True | habitatmech:GOLD.e1b5f9301d | Finished 2026-10-15T21:15:16Z. uv run python scripts/validate_strict.py data/habitats/host_associated/carcinoid.yaml data/habitats/host_associated/carcinoma.yaml data/habitats/host_associated/carcinoma_cell.yaml data/habitats/host_associated/carcinosarcoma.yaml data/habitats/host_associated/cardiac_atrium.yaml data/habitats/host_associated/cardiac_septum.yaml data/habitats/host_associated/cardiac_skeleton.yaml data/habitats/host_associated/cardiac_stomach.yaml data/habitats/host_associated/cardiovascular_system.yaml data/habitats/host_associated/carposphere.yaml data/habitats/host_associated/cartilage.yaml data/habitats/host_associated/cartilage__bd8c407c.yaml data/habitats/host_associated/cartilage__c54322c6.yaml data/habitats/host_associated/caryopsis.yaml data/habitats/host_associated/caski.yaml data/habitats/host_associated/catarrh.yaml data/habitats/host_associated/catarrh__1e78e51c.yaml data/habitats/host_associated/caulosphere.yaml data/habitats/host_associated/ceca.yaml data/habitats/host_associated/ceca__2f9665ca.yaml data/habitats/host_associated/ceca__d15faa5d.yaml data/habitats/host_associated/cecotropes_night_fecs.yaml data/habitats/host_associated/cecum.yaml data/habitats/host_associated/cecum__79e270ae.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | habitatmech:GOLD.e1b5f9301d | Finished 2026-10-15T21:15:30Z. No issues found<br>824 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | habitatmech:GOLD.e1b5f9301d | Finished 2026-10-15T21:15:32Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | habitatmech:GOLD.e1b5f9301d | Finished 2026-10-15T21:16:11Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | habitatmech:GOLD.e1b5f9301d | Finished 2026-10-15T21:16:19Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | habitatmech:GOLD.e1b5f9301d | Finished 2026-10-15T21:16:50Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | habitatmech:GOLD.e1b5f9301d | Finished 2026-10-15T21:17:56Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-baseline native QC | passed | True | habitatmech:GOLD.e1b5f9301d | Verified 2026-10-15T21:13:04Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38805081742 |

## Scientific And Domain Assessments

### Identity, definition, category and ancestry

identity: concern. Targets: habitatmech:GOLD.e1b5f9301d.

Fish cartilage has a defensible generic cartilage genus and distinct host-scoped mint. Cartilage tissue is not the complete fish skeletal system. A prior favorable hierarchy assessment conflated source-path containment with is-a. The emitted narrow predicate also has the separate endpoint-contract defect; neither issue requires merging this record into mammalian cartilage.

### Frozen source counts, units, ranks, channels and pool

quantity: supported. Targets: habitatmech:GOLD.e1b5f9301d.

Exact source rows reproduce all emitted counts and displayed taxon rows. [{"source": "GOLD", "count": 0, "unit": "ORGANISM"}]. Zero GOLD counts are omitted; supplemental biosamples and study memberships are not added to tree ORGANISM counts.

### Biological support and bounded uncertainty

evidence: supported. Targets: habitatmech:GOLD.e1b5f9301d.

Fish cartilage has a defensible generic cartilage genus and distinct host-scoped mint. Cartilage tissue is not the complete fish skeletal system. A prior favorable hierarchy assessment conflated source-path containment with is-a. The emitted narrow predicate also has the separate endpoint-contract defect; neither issue requires merging this record into mammalian cartilage.

### Native status, optional fields and mechanisms

completeness: supported. Targets: habitatmech:GOLD.e1b5f9301d.

Executed resolution reproduces NARROW/SEEDED. No target environmental parameters, causal graphs, discussions, datasets or is_characteristic=true claims are present. Optional absence and SEEDED status alone do not warrant findings; parent mechanisms are not inherited.

### Deterministic validity and source fidelity

schema: supported. Targets: habitatmech:GOLD.e1b5f9301d.

Ordinary/strict target validation, 824 histories, source provenance, exact 3208-record reproduction, 32 causal overlays, 110 term requests, configured labels and exact-base remote QC passed. These are not substitutes for scientific identity assessment.

## Findings

### F1: Containing anatomy is emitted as a broader habitat class

major / open / confirmed; issue key: cartilage--bd8c407c-context-parent.

Exclude only the exact GOLD source-path/expected-parent contribution habitatmech:GOLD.b1f5d69111. Fish cartilage has a defensible generic cartilage genus and distinct host-scoped mint. Cartilage tissue is not the complete fish skeletal system. A prior favorable hierarchy assessment conflated source-path containment with is-a. The emitted narrow predicate also has the separate endpoint-contract defect; neither issue requires merging this record into mammalian cartilage. Preserve independent valid ontology genera and raw source paths.

### F2: Narrow predicate uses an undeclared ontology-parent endpoint

major / open / confirmed; issue key: cartilage--bd8c407c-mapping-endpoint-contract.

Resolution retains the GOLD source mint but emits narrowMatch relative to its ontology parent. SourceAttestation declares a source-to-record relation. Reconcile producer, schema and downstream consumers under #1398 without merging host-specific concepts or blindly reversing predicates. This is not a claim that SKOS prohibits self-links and does not certify SSSOM/KGX conformance.

## Recommended Actions And Acceptance Checks

### ACT1

Exclude only the exact GOLD source-path/expected-parent contribution habitatmech:GOLD.b1f5d69111. Fish cartilage has a defensible generic cartilage genus and distinct host-scoped mint. Cartilage tissue is not the complete fish skeletal system. A prior favorable hierarchy assessment conflated source-path containment with is-a. The emitted narrow predicate also has the separate endpoint-contract defect; neither issue requires merging this record into mammalian cartilage. Preserve independent valid ontology genera and raw source paths. No repair is performed by this review.

- Regress the exact claim, preserving independent valid genera, raw provenance and source counts/units. Change native status or mappings only when supported by the authorized ITEM assessment; never decrement source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

### ACT2

Resolution retains the GOLD source mint but emits narrowMatch relative to its ontology parent. SourceAttestation declares a source-to-record relation. Reconcile producer, schema and downstream consumers under #1398 without merging host-specific concepts or blindly reversing predicates. This is not a claim that SKOS prohibits self-links and does not certify SSSOM/KGX conformance. No repair is performed by this review.

- Regress the exact claim, preserving independent valid genera, raw provenance and source counts/units. Change native status or mappings only when supported by the authorized ITEM assessment; never decrement source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/cartilage__bd8c407c.yaml; Entire target YAML | supports | All fields, displayed taxa, source attestations and complete generated history read. |
| ERULE | docs/CURATION.md; Identity, strictly broader hierarchy and source evidence rules | supports | All parent contributions must be strictly broader. Disease, organism, sampled material and habitat meanings are distinct. Optional absence is not automatically a defect. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; HabitatRecord, SourceAttestation, TaxonAssociation and category semantics | supports | Source mapping endpoints are source-to-record. Reported associations do not imply characteristic presence. Native category and optional-field contracts retained. |
| ESEED | src/habitatmech/seed.py; Executed source resolution and full generated-document reproduction | supports | [{"mint": "habitatmech:GOLD.e1b5f9301d", "automatic": {"identifier": "habitatmech:GOLD.e1b5f9301d", "grounding_status": "NARROW", "mapping_predicate": "skos:narrowMatch", "contributes_grounding": true, "extra_parents": ["BTO:0000206"], "extra_xrefs": [], "route": "gold_narrower_than_leaf_match", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "habitatmech:GOLD.e1b5f9301d", "grounding_status": "NARROW", "mapping_predicate": "skos:narrowMatch", "contributes_grounding": true, "extra_parents": ["BTO:0000206"], "extra_xrefs": [], "route": "gold_narrower_than_leaf_match", "category": null, "reviewed": false, "decision": null}}] |
| EEXTRACT | src/habitatmech/extract.py; Source projections, taxon ranking and counts | supports | Frozen counts/units, maximum scores, channels, candidate pools and top taxon rows were traced to exact source rows. Original PREGO pair citation links are not retained in this projection. |
| ET5 | data/raw/gold_ecosystem_paths.tsv; Physical TSV rows 1965 | supports | [{"row": 1965, "data": {"canonical_path": "Host-associated &gt; Fish &gt; Skeletal system &gt; Cartilage", "ecosystem": "Host-associated", "ecosystem_category": "Fish", "ecosystem_type": "Skeletal system", "ecosystem_subtype": "Cartilage", "specific_ecosystem": "", "leaf_label": "Cartilage", "depth": "4", "gold_node_count": "2", "organism_count": "0", "study_count": "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids": "gold.ecosystem:7567&#124;gold.ecosystem:7568"}}] |
| ET6 | data/raw/ontology_subclass_edges.tsv; Physical TSV rows 147 | supports | [{"row": 147, "data": {"subject": "BTO:0000206", "predicate": "rdfs:subClassOf", "object": "BTO:0000421"}}] |
| ET7 | data/raw/ontology_terms.tsv; Physical TSV rows 208 | supports | [{"row": 208, "data": {"term_id": "BTO:0000206", "ontology": "BTO", "label": "cartilage", "definition": "A specialized, fibrous connective tissue, forming most of the temporary skeleton of the embryo, providing a model in which most of the bones develop, and constituting an important part of the growth mechanism of the organism. It exists in several types, the most important of which are hyaline cartilage, elastic cartilage, and fibrocartilage. Also used as a general term to designate a mass of such tissue in a particular site in the body.", "synonyms": "", "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}}] |
| EP8 | data/habitats/host_associated/skeletal_system__a462a5a5.yaml; Entire immediate parent record; context only | supports | {"identifier": "habitatmech:GOLD.b1f5d69111", "label": "Skeletal system", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0001434", "habitatmech:GOLD.3d529a667e"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:7562", "source_label": "Skeletal system", "source_path": "Host-associated &gt; Fish &gt; Skeletal system", "mapping_predicate": "skos:narrowMatch", "notes": "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NARROW."}]} |
| ELEGACY | reports/yaml_record_review/20261001T003944Z-cartilage__bd8c407c.md; Findings and proposed edits; historical lead | supports | The earlier pass accepted the source skeletal-system parent as broader. That confuses containment with is-a. Its native status and raw counts remain correctly reproduced. |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000206/graph; BTO_0000206-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000206", "target": "http://purl.obolibrary.org/obo/BTO_0000421", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/BTO_0000206", "target": "http://purl.obolibrary.org/obo/BTO_0001486", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000206; BTO_0000206.json | context_only | Current term identity, active status and definition: {"obo_id": "BTO:0000206", "label": "cartilage", "is_obsolete": false, "description": ["A specialized, fibrous connective tissue, forming most of the temporary skeleton of the embryo, providing a model in which most of the bones develop, and constituting an important part of the growth mechanism of the organism. It exists in several types, the most important of which are hyaline cartilage, elastic cartilage, and fibrocartilage. Also used as a general term to designate a mass of such tissue in a particular site in the body."]} |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001434/graph; UBERON_0001434-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001434", "target": "http://purl.obolibrary.org/obo/UBERON_0011216", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001434", "target": "http://purl.obolibrary.org/obo/UBERON_0000066", "uri": "http://purl.obolibrary.org/obo/RO_0002492", "label": "existence ends during"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001434", "target": "http://purl.obolibrary.org/obo/UBERON_0002204", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001434", "target": "http://purl.obolibrary.org/obo/UBERON_0004288", "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001434", "target": "http://purl.obolibrary.org/obo/UBERON_0004770", "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001434; UBERON_0001434.json | context_only | Current term identity, active status and definition: {"obo_id": "UBERON:0001434", "label": "skeletal system", "is_obsolete": false, "description": ["Anatomical system that is a multi-element, multi-tissue anatomical cluster that consists of the skeleton and the articular system."]} |
| ESEARCH | Local maintained inputs and structured archive; rg --no-ignore --hidden -l -F -e habitatmech:GOLD.e1b5f9301d -e Cartilage -e cartilage__bd8c407c -e habitatmech:GOLD.e1b5f9301d curation history research reports data/raw build reviews | context_only | Exact source rows were parsed separately; no formal structured target predecessor was found. Broad label matches were treated as leads, not all read. |

## Limits And Additional Notes

- Individual source specimens and all original pair-level citations have not been independently reconstructed. Counts, ranks and source scores are not prevalence or characteristic presence.
- Configured label validation skips 2061 no-adapter pairs. Displayed TaxIds were separately checked against current NCBI Taxonomy.
- Full QC evidence is a successful remote run at the exact unchanged scientific input base, not a new local full-QC execution. These new bundles require their own post-save archive check.
- iModulonDB is not applicable to target claims: no gene, regulator, expression module or causal mechanism is asserted. Papers mentioning genes are used only for source context. No paid research was used.
- All captured local inputs were compared with both current bytes and exact Git-base blobs. The review explicitly assesses that committed revision.
- Ignored-inclusive archive search found no previous structured observation targeting this identifier. Legacy prose is a lead, not formal predecessor lineage or automatic closure.
- Read-only review: no curation, generation, native status/history promotion or GitHub mutation.
- The earlier pass accepted the source skeletal-system parent as broader. That confuses containment with is-a. Its native status and raw counts remain correctly reproduced.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T212548Z-cartilage__bd8c407c-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: Cartilage (habitatmech:GOLD.e1b5f9301d)'
started_at: '2026-10-15T21:13:32Z'
finished_at: '2026-10-15T21:25:48Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent assesses target and evidence; not independent reviewer
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: Fish cartilage has a defensible generic cartilage genus and distinct host-scoped
  mint. Cartilage tissue is not the complete fish skeletal system. A prior favorable
  hierarchy assessment conflated source-path containment with is-a. The emitted narrow
  predicate also has the separate endpoint-contract defect; neither issue requires
  merging this record into mammalian cartilage.
source:
  git_revision: 62952fb7cdf223af9d1ffbf1cc2f556b22f7ee6b
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
    sha256: 490d3478aadc1dc3c4f04770d06db02fead4964d2e40ff339bfa389d46a5918a
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 37dc4b40642d19e7b5c3262f368d12daa82e03115e7731a2326ae88785ceff5b
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 12be4a7eccfcc6a9b9ef89fc1cb009e8f5e9ab87005bd6eb7ba93c910abf8f6d
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
    sha256: b0135af0aa4deed0f3824a2f491d5a742c1b7de4775c533f283761d22e805821
    role: context
  - path: data/habitats/RETIRED.tsv
    sha256: a2a0496837ea75e487d7fc5d35317a890262a941d8fffe9babcd39f2f332c6db
    role: context
  - path: data/habitats/host_associated/cartilage__bd8c407c.yaml
    sha256: 8d941ed44d0e4621bd7259d4090faa3aff1fb4d1b41343a1f4581f43842c2fea
    role: target
  - path: data/habitats/host_associated/skeletal_system__a462a5a5.yaml
    sha256: 1704508e1f52a0eef7624b8a50ec4f8ff9d1041f23dddd6039405a1a527b7400
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
  - path: reports/yaml_record_review/20261001T003944Z-cartilage__bd8c407c.md
    sha256: 4d2f773549c4cfeed5317e07c1e48748dc060a9152542d88a834ad6b0fdd190a
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
- target_id: habitatmech:GOLD.e1b5f9301d
  path: data/habitats/host_associated/cartilage__bd8c407c.yaml
  label: Cartilage
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
  description: Full field-by-field scientific assessment of this exact target at 62952fb7cdf223af9d1ffbf1cc2f556b22f7ee6b.
  selection: One of the next 24 path-ordered unreviewed identifiers in the ignored-inclusive
    3208-record census. This bundle assesses one exact identifier, not a proxy sample.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.e1b5f9301d
  exclusions:
  - target: Other records and SSSOM/KGX products
    reason: Parent context and source witnesses do not add reviewed identifiers. Export
      conformance and individual source specimens are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/cartilage__bd8c407c.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.e1b5f9301d
  summary: "Finished 2026-10-15T21:13:35Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/cartilage__bd8c407c.yaml"
  scope_note: Ordinary schema for this target; strict check covers all 24 named targets;
    other documented checks have full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/carcinoid.yaml data/habitats/host_associated/carcinoma.yaml
    data/habitats/host_associated/carcinoma_cell.yaml data/habitats/host_associated/carcinosarcoma.yaml
    data/habitats/host_associated/cardiac_atrium.yaml data/habitats/host_associated/cardiac_septum.yaml
    data/habitats/host_associated/cardiac_skeleton.yaml data/habitats/host_associated/cardiac_stomach.yaml
    data/habitats/host_associated/cardiovascular_system.yaml data/habitats/host_associated/carposphere.yaml
    data/habitats/host_associated/cartilage.yaml data/habitats/host_associated/cartilage__bd8c407c.yaml
    data/habitats/host_associated/cartilage__c54322c6.yaml data/habitats/host_associated/caryopsis.yaml
    data/habitats/host_associated/caski.yaml data/habitats/host_associated/catarrh.yaml
    data/habitats/host_associated/catarrh__1e78e51c.yaml data/habitats/host_associated/caulosphere.yaml
    data/habitats/host_associated/ceca.yaml data/habitats/host_associated/ceca__2f9665ca.yaml
    data/habitats/host_associated/ceca__d15faa5d.yaml data/habitats/host_associated/cecotropes_night_fecs.yaml
    data/habitats/host_associated/cecum.yaml data/habitats/host_associated/cecum__79e270ae.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.e1b5f9301d
  summary: "Finished 2026-10-15T21:15:16Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/carcinoid.yaml data/habitats/host_associated/carcinoma.yaml\
    \ data/habitats/host_associated/carcinoma_cell.yaml data/habitats/host_associated/carcinosarcoma.yaml\
    \ data/habitats/host_associated/cardiac_atrium.yaml data/habitats/host_associated/cardiac_septum.yaml\
    \ data/habitats/host_associated/cardiac_skeleton.yaml data/habitats/host_associated/cardiac_stomach.yaml\
    \ data/habitats/host_associated/cardiovascular_system.yaml data/habitats/host_associated/carposphere.yaml\
    \ data/habitats/host_associated/cartilage.yaml data/habitats/host_associated/cartilage__bd8c407c.yaml\
    \ data/habitats/host_associated/cartilage__c54322c6.yaml data/habitats/host_associated/caryopsis.yaml\
    \ data/habitats/host_associated/caski.yaml data/habitats/host_associated/catarrh.yaml\
    \ data/habitats/host_associated/catarrh__1e78e51c.yaml data/habitats/host_associated/caulosphere.yaml\
    \ data/habitats/host_associated/ceca.yaml data/habitats/host_associated/ceca__2f9665ca.yaml\
    \ data/habitats/host_associated/ceca__d15faa5d.yaml data/habitats/host_associated/cecotropes_night_fecs.yaml\
    \ data/habitats/host_associated/cecum.yaml data/habitats/host_associated/cecum__79e270ae.yaml\n\
    Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      24\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Ordinary schema for this target; strict check covers all 24 named targets;
    other documented checks have full-corpus scope.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.e1b5f9301d
  summary: 'Finished 2026-10-15T21:15:30Z. No issues found

    824 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Ordinary schema for this target; strict check covers all 24 named targets;
    other documented checks have full-corpus scope.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.e1b5f9301d
  summary: "Finished 2026-10-15T21:15:32Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Ordinary schema for this target; strict check covers all 24 named targets;
    other documented checks have full-corpus scope.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.e1b5f9301d
  summary: "Finished 2026-10-15T21:16:11Z. expected 3208 records, found 3208 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Ordinary schema for this target; strict check covers all 24 named targets;
    other documented checks have full-corpus scope.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.e1b5f9301d
  summary: "Finished 2026-10-15T21:16:19Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Ordinary schema for this target; strict check covers all 24 named targets;
    other documented checks have full-corpus scope.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.e1b5f9301d
  summary: "Finished 2026-10-15T21:16:50Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Ordinary schema for this target; strict check covers all 24 named targets;
    other documented checks have full-corpus scope.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.e1b5f9301d
  summary: "Finished 2026-10-15T21:17:56Z. id↔label correspondence summary:\n    \
    \      OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Ordinary schema for this target; strict check covers all 24 named targets;
    other documented checks have full-corpus scope.
- check_id: CCI
  name: Exact-baseline native QC
  status: passed
  required: true
  command: gh run view 38805081742 --json status,conclusion,headSha,url,jobs
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.e1b5f9301d
  summary: Verified 2026-10-15T21:13:04Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38805081742
  scope_note: Unchanged committed scientific-input baseline. New output bundles are
    outside this remote execution.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/cartilage__bd8c407c.yaml
  locator: Entire target YAML
  accessed_at: '2026-10-15T21:25:47Z'
  support: supports
  summary: All fields, displayed taxa, source attestations and complete generated
    history read.
  snapshot_sha256: 8d941ed44d0e4621bd7259d4090faa3aff1fb4d1b41343a1f4581f43842c2fea
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, strictly broader hierarchy and source evidence rules
  accessed_at: '2026-10-15T21:25:47Z'
  support: supports
  summary: All parent contributions must be strictly broader. Disease, organism, sampled
    material and habitat meanings are distinct. Optional absence is not automatically
    a defect.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: HabitatRecord, SourceAttestation, TaxonAssociation and category semantics
  accessed_at: '2026-10-15T21:25:47Z'
  support: supports
  summary: Source mapping endpoints are source-to-record. Reported associations do
    not imply characteristic presence. Native category and optional-field contracts
    retained.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed source resolution and full generated-document reproduction
  accessed_at: '2026-10-15T21:25:47Z'
  support: supports
  summary: '[{"mint": "habitatmech:GOLD.e1b5f9301d", "automatic": {"identifier": "habitatmech:GOLD.e1b5f9301d",
    "grounding_status": "NARROW", "mapping_predicate": "skos:narrowMatch", "contributes_grounding":
    true, "extra_parents": ["BTO:0000206"], "extra_xrefs": [], "route": "gold_narrower_than_leaf_match",
    "category": null, "reviewed": false, "decision": null}, "final": {"identifier":
    "habitatmech:GOLD.e1b5f9301d", "grounding_status": "NARROW", "mapping_predicate":
    "skos:narrowMatch", "contributes_grounding": true, "extra_parents": ["BTO:0000206"],
    "extra_xrefs": [], "route": "gold_narrower_than_leaf_match", "category": null,
    "reviewed": false, "decision": null}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: Source projections, taxon ranking and counts
  accessed_at: '2026-10-15T21:25:47Z'
  support: supports
  summary: Frozen counts/units, maximum scores, channels, candidate pools and top
    taxon rows were traced to exact source rows. Original PREGO pair citation links
    are not retained in this projection.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Physical TSV rows 1965
  accessed_at: '2026-10-15T21:25:47Z'
  support: supports
  summary: '[{"row": 1965, "data": {"canonical_path": "Host-associated > Fish > Skeletal
    system > Cartilage", "ecosystem": "Host-associated", "ecosystem_category": "Fish",
    "ecosystem_type": "Skeletal system", "ecosystem_subtype": "Cartilage", "specific_ecosystem":
    "", "leaf_label": "Cartilage", "depth": "4", "gold_node_count": "2", "organism_count":
    "0", "study_count": "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids":
    "gold.ecosystem:7567|gold.ecosystem:7568"}}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: ET6
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: Physical TSV rows 147
  accessed_at: '2026-10-15T21:25:47Z'
  support: supports
  summary: '[{"row": 147, "data": {"subject": "BTO:0000206", "predicate": "rdfs:subClassOf",
    "object": "BTO:0000421"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET7
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 208
  accessed_at: '2026-10-15T21:25:47Z'
  support: supports
  summary: '[{"row": 208, "data": {"term_id": "BTO:0000206", "ontology": "BTO", "label":
    "cartilage", "definition": "A specialized, fibrous connective tissue, forming
    most of the temporary skeleton of the embryo, providing a model in which most
    of the bones develop, and constituting an important part of the growth mechanism
    of the organism. It exists in several types, the most important of which are hyaline
    cartilage, elastic cartilage, and fibrocartilage. Also used as a general term
    to designate a mass of such tissue in a particular site in the body.", "synonyms":
    "", "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EP8
  kind: record_content
  reference: data/habitats/host_associated/skeletal_system__a462a5a5.yaml
  locator: Entire immediate parent record; context only
  accessed_at: '2026-10-15T21:25:47Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.b1f5d69111", "label": "Skeletal system",
    "habitat_category": "HOST_ASSOCIATED", "grounding_status": "NARROW", "mapping_status":
    "SEEDED", "parent_habitats": ["UBERON:0001434", "habitatmech:GOLD.3d529a667e"],
    "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:7562",
    "source_label": "Skeletal system", "source_path": "Host-associated > Fish > Skeletal
    system", "mapping_predicate": "skos:narrowMatch", "notes": "3 GOLD ecosystem node
    ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history":
    [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action":
    "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested
    by GOLD. Grounding: NARROW."}]}'
  snapshot_sha256: 1704508e1f52a0eef7624b8a50ec4f8ff9d1041f23dddd6039405a1a527b7400
- evidence_id: ELEGACY
  kind: record_content
  reference: reports/yaml_record_review/20261001T003944Z-cartilage__bd8c407c.md
  locator: Findings and proposed edits; historical lead
  accessed_at: '2026-10-15T21:25:47Z'
  support: supports
  summary: The earlier pass accepted the source skeletal-system parent as broader.
    That confuses containment with is-a. Its native status and raw counts remain correctly
    reproduced.
  snapshot_sha256: 4d2f773549c4cfeed5317e07c1e48748dc060a9152542d88a834ad6b0fdd190a
- evidence_id: EX1
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000206/graph
  locator: BTO_0000206-graph.json
  accessed_at: '2026-10-15T21:13:55Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000206",
    "target": "http://purl.obolibrary.org/obo/BTO_0000421", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/BTO_0000206",
    "target": "http://purl.obolibrary.org/obo/BTO_0001486", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: f2ba10bee29166bbda373c7ca74fb1fdfdd4dad60c3f31add0bce0e9d47998c5
- evidence_id: EX2
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000206
  locator: BTO_0000206.json
  accessed_at: '2026-10-15T21:13:54Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "BTO:0000206",
    "label": "cartilage", "is_obsolete": false, "description": ["A specialized, fibrous
    connective tissue, forming most of the temporary skeleton of the embryo, providing
    a model in which most of the bones develop, and constituting an important part
    of the growth mechanism of the organism. It exists in several types, the most
    important of which are hyaline cartilage, elastic cartilage, and fibrocartilage.
    Also used as a general term to designate a mass of such tissue in a particular
    site in the body."]}'
  snapshot_sha256: 248cea02b76e48ca6fedbb5d45d6554218d3b13ca9685ad515e84bc5031e2917
- evidence_id: EX3
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001434/graph
  locator: UBERON_0001434-graph.json
  accessed_at: '2026-10-15T21:14:13Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001434",
    "target": "http://purl.obolibrary.org/obo/UBERON_0011216", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001434",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000066", "uri": "http://purl.obolibrary.org/obo/RO_0002492",
    "label": "existence ends during"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001434",
    "target": "http://purl.obolibrary.org/obo/UBERON_0002204", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001434",
    "target": "http://purl.obolibrary.org/obo/UBERON_0004288", "uri": "http://purl.obolibrary.org/obo/BFO_0000051",
    "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001434",
    "target": "http://purl.obolibrary.org/obo/UBERON_0004770", "uri": "http://purl.obolibrary.org/obo/BFO_0000051",
    "label": "has part"}]'
  snapshot_sha256: ecbcf4134ad9733794246b12ecba04ef8a390ad1ec184baf4f7f0a60e5eaa71b
- evidence_id: EX4
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001434
  locator: UBERON_0001434.json
  accessed_at: '2026-10-15T21:14:12Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "UBERON:0001434",
    "label": "skeletal system", "is_obsolete": false, "description": ["Anatomical
    system that is a multi-element, multi-tissue anatomical cluster that consists
    of the skeleton and the articular system."]}'
  snapshot_sha256: 0965f957490fb66ad6f4744d8fe4694bf133e2f156a67805e485800bc53e616e
- evidence_id: ESEARCH
  kind: search
  reference: Local maintained inputs and structured archive
  locator: rg --no-ignore --hidden -l -F -e habitatmech:GOLD.e1b5f9301d -e Cartilage
    -e cartilage__bd8c407c -e habitatmech:GOLD.e1b5f9301d curation history research
    reports data/raw build reviews
  accessed_at: '2026-10-15T21:13:37Z'
  support: context_only
  summary: Exact source rows were parsed separately; no formal structured target predecessor
    was found. Broad label matches were treated as leads, not all read.
  search_scope: curation, history, research, reports, data/raw, build and reviews;
    hidden/ignored content included, with structured review.yaml parsing independent
    of gitignore.
assessments:
- assessment_id: A1
  area: identity
  topic: Identity, definition, category and ancestry
  outcome: concern
  summary: Fish cartilage has a defensible generic cartilage genus and distinct host-scoped
    mint. Cartilage tissue is not the complete fish skeletal system. A prior favorable
    hierarchy assessment conflated source-path containment with is-a. The emitted
    narrow predicate also has the separate endpoint-contract defect; neither issue
    requires merging this record into mammalian cartilage.
  target_ids:
  - habitatmech:GOLD.e1b5f9301d
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - EP8
  - EX1
  - EX2
  - EX3
  - EX4
  dimensions:
  - name: native_status
    value: NARROW/SEEDED
    definition: Generated grounding and curation status, distinct from scientific
      review verdict.
    evidence_ids:
    - E1
    - ESEED
- assessment_id: A2
  area: quantity
  topic: Frozen source counts, units, ranks, channels and pool
  outcome: supported
  summary: 'Exact source rows reproduce all emitted counts and displayed taxon rows.
    [{"source": "GOLD", "count": 0, "unit": "ORGANISM"}]. Zero GOLD counts are omitted;
    supplemental biosamples and study memberships are not added to tree ORGANISM counts.'
  target_ids:
  - habitatmech:GOLD.e1b5f9301d
  evidence_ids:
  - E1
  - EEXTRACT
  - ESEED
  - EX1
  - EX2
  - EX3
  - EX4
  dimensions:
  - name: source_assertion_units
    value: '[{"source": "GOLD", "count": 0, "unit": "ORGANISM"}]'
    definition: Frozen counts with noninterchangeable source units; zero GOLD counts
      are verified in raw rows.
    evidence_ids:
    - E1
    - EEXTRACT
- assessment_id: A3
  area: evidence
  topic: Biological support and bounded uncertainty
  outcome: supported
  summary: Fish cartilage has a defensible generic cartilage genus and distinct host-scoped
    mint. Cartilage tissue is not the complete fish skeletal system. A prior favorable
    hierarchy assessment conflated source-path containment with is-a. The emitted
    narrow predicate also has the separate endpoint-contract defect; neither issue
    requires merging this record into mammalian cartilage.
  target_ids:
  - habitatmech:GOLD.e1b5f9301d
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - EP8
  - EX1
  - EX2
  - EX3
  - EX4
- assessment_id: A4
  area: completeness
  topic: Native status, optional fields and mechanisms
  outcome: supported
  summary: Executed resolution reproduces NARROW/SEEDED. No target environmental parameters,
    causal graphs, discussions, datasets or is_characteristic=true claims are present.
    Optional absence and SEEDED status alone do not warrant findings; parent mechanisms
    are not inherited.
  target_ids:
  - habitatmech:GOLD.e1b5f9301d
  evidence_ids:
  - E1
  - ESCHEMA
  - ESEED
- assessment_id: A5
  area: schema
  topic: Deterministic validity and source fidelity
  outcome: supported
  summary: Ordinary/strict target validation, 824 histories, source provenance, exact
    3208-record reproduction, 32 causal overlays, 110 term requests, configured labels
    and exact-base remote QC passed. These are not substitutes for scientific identity
    assessment.
  target_ids:
  - habitatmech:GOLD.e1b5f9301d
  evidence_ids:
  - E1
  - ERULE
findings:
- finding_id: F1
  issue_key: cartilage--bd8c407c-context-parent
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Containing anatomy is emitted as a broader habitat class
  description: Exclude only the exact GOLD source-path/expected-parent contribution
    habitatmech:GOLD.b1f5d69111. Fish cartilage has a defensible generic cartilage
    genus and distinct host-scoped mint. Cartilage tissue is not the complete fish
    skeletal system. A prior favorable hierarchy assessment conflated source-path
    containment with is-a. The emitted narrow predicate also has the separate endpoint-contract
    defect; neither issue requires merging this record into mammalian cartilage. Preserve
    independent valid ontology genera and raw source paths.
  target_ids:
  - habitatmech:GOLD.e1b5f9301d
  field_paths:
  - parent_habitats
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - EP8
  - EX1
  - EX2
  - EX3
  - EX4
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported hierarchy, mapping or source-evidence
    semantics; correct deterministic reproduction does not establish scientific support.
  external_issues: []
- finding_id: F2
  issue_key: cartilage--bd8c407c-mapping-endpoint-contract
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Narrow predicate uses an undeclared ontology-parent endpoint
  description: 'Resolution retains the GOLD source mint but emits narrowMatch relative
    to its ontology parent. SourceAttestation declares a source-to-record relation.
    Reconcile producer, schema and downstream consumers under #1398 without merging
    host-specific concepts or blindly reversing predicates. This is not a claim that
    SKOS prohibits self-links and does not certify SSSOM/KGX conformance.'
  target_ids:
  - habitatmech:GOLD.e1b5f9301d
  field_paths:
  - source_attestations[0].mapping_predicate
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - EP8
  - EX1
  - EX2
  - EX3
  - EX4
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported hierarchy, mapping or source-evidence
    semantics; correct deterministic reproduction does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - habitatmech:GOLD.e1b5f9301d
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: Exclude only the exact GOLD source-path/expected-parent contribution
    habitatmech:GOLD.b1f5d69111. Fish cartilage has a defensible generic cartilage
    genus and distinct host-scoped mint. Cartilage tissue is not the complete fish
    skeletal system. A prior favorable hierarchy assessment conflated source-path
    containment with is-a. The emitted narrow predicate also has the separate endpoint-contract
    defect; neither issue requires merging this record into mammalian cartilage. Preserve
    independent valid ontology genera and raw source paths. No repair is performed
    by this review.
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
- action_id: ACT2
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.e1b5f9301d
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  description: 'Resolution retains the GOLD source mint but emits narrowMatch relative
    to its ontology parent. SourceAttestation declares a source-to-record relation.
    Reconcile producer, schema and downstream consumers under #1398 without merging
    host-specific concepts or blindly reversing predicates. This is not a claim that
    SKOS prohibits self-links and does not certify SSSOM/KGX conformance. No repair
    is performed by this review.'
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
- Individual source specimens and all original pair-level citations have not been
  independently reconstructed. Counts, ranks and source scores are not prevalence
  or characteristic presence.
- Configured label validation skips 2061 no-adapter pairs. Displayed TaxIds were separately
  checked against current NCBI Taxonomy.
- Full QC evidence is a successful remote run at the exact unchanged scientific input
  base, not a new local full-QC execution. These new bundles require their own post-save
  archive check.
- 'iModulonDB is not applicable to target claims: no gene, regulator, expression module
  or causal mechanism is asserted. Papers mentioning genes are used only for source
  context. No paid research was used.'
notes:
- All captured local inputs were compared with both current bytes and exact Git-base
  blobs. The review explicitly assesses that committed revision.
- Ignored-inclusive archive search found no previous structured observation targeting
  this identifier. Legacy prose is a lead, not formal predecessor lineage or automatic
  closure.
- 'Read-only review: no curation, generation, native status/history promotion or GitHub
  mutation.'
- The earlier pass accepted the source skeletal-system parent as broader. That confuses
  containment with is-a. Its native status and raw counts remain correctly reproduced.
tags:
- individual-scientific-review
- host-associated
```
