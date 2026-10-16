# Record review: Compact bone (habitatmech:GOLD.92256d7035)

- Review: 20261016T054403Z-compact_bone-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-16T05:13:49Z
- Finished UTC: 2026-10-16T05:44:03Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The human compact-bone source can retain generic compact bone tissue as a broader class. Its source Bone parent is itself defined through BTO as hard connective tissue, not a whole skeletal organ; no part/whole exclusion is justified. Preserve both genera, source mint and zero-count semantics. The separate narrow mapping endpoint contract remains inconsistent.

## Scope And Provenance

Full field-by-field assessment of this one resolved generated target.

Selection: One of the next 24 unreviewed targets in deterministic path order from the ignored-inclusive 3209-record census. This bundle is not a proxy sample.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 13cddc722250dcad4327e5f9fad0a12fe7c08268.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.92256d7035 | data/habitats/host_associated/compact_bone.yaml | generated | Compact bone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.92256d7035 | Finished 2026-10-16T05:15:45Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/compact_bone.yaml |
| validate-strict | passed | True | habitatmech:GOLD.92256d7035 | Finished 2026-10-16T05:17:09Z. uv run python scripts/validate_strict.py data/habitats/host_associated/column.yaml data/habitats/host_associated/common_warts.yaml data/habitats/host_associated/compact_bone.yaml data/habitats/host_associated/compact_bone__c00eaa73.yaml data/habitats/host_associated/conjunctiva.yaml data/habitats/host_associated/conjunctiva__482ca0a7.yaml data/habitats/host_associated/conjunctiva__6e913f9c.yaml data/habitats/host_associated/connective_tissue.yaml data/habitats/host_associated/connective_tissue__85a5a212.yaml data/habitats/host_associated/connective_tissue__b37fb9b6.yaml data/habitats/host_associated/coprolite.yaml data/habitats/host_associated/coral.yaml data/habitats/host_associated/corn_silk.yaml data/habitats/host_associated/cornea.yaml data/habitats/host_associated/cornea__2a9b9367.yaml data/habitats/host_associated/cornea__f146d32e.yaml data/habitats/host_associated/cortex.yaml data/habitats/host_associated/crop.yaml data/habitats/host_associated/crop__310374d9.yaml data/habitats/host_associated/crop__3de61c58.yaml data/habitats/host_associated/crop__a03dd0e3.yaml data/habitats/host_associated/crop__d566c329.yaml data/habitats/host_associated/crop_content.yaml data/habitats/host_associated/crown_gall.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | habitatmech:GOLD.92256d7035 | Finished 2026-10-16T05:17:16Z. No issues found<br>834 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | habitatmech:GOLD.92256d7035 | Finished 2026-10-16T05:17:16Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | habitatmech:GOLD.92256d7035 | Finished 2026-10-16T05:17:32Z. expected 3209 records, found 3209 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | habitatmech:GOLD.92256d7035 | Finished 2026-10-16T05:17:36Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | habitatmech:GOLD.92256d7035 | Finished 2026-10-16T05:17:53Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | habitatmech:GOLD.92256d7035 | Finished 2026-10-16T05:18:37Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1173<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2063<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-base hosted native QC | passed | True | habitatmech:GOLD.92256d7035 | Verified 2026-10-16T05:19:04Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38852350960 |
| Candidate-pool correspondence | passed | False | habitatmech:GOLD.92256d7035 | Finished 2026-10-16T05:42:35Z. All 67 displayed candidate pools equal exact source taxon totals. |
| Standalone citation validation applicability | not_applicable | False | habitatmech:GOLD.92256d7035 | No standalone citation validator is documented for these generated targets without evidence objects. Current authorities verify stable references; full-corpus causal validation ran. |

## Scientific And Domain Assessments

### Identity, grounding, aliases and strict hierarchy

identity: concern. Targets: habitatmech:GOLD.92256d7035.

The human compact-bone source can retain generic compact bone tissue as a broader class. Its source Bone parent is itself defined through BTO as hard connective tissue, not a whole skeletal organ; no part/whole exclusion is justified. Preserve both genera, source mint and zero-count semantics. The separate narrow mapping endpoint contract remains inconsistent.

### Counts, units, taxon ranks, scores and candidate pools

quantity: supported. Targets: habitatmech:GOLD.92256d7035.

Exact source rows reproduce emitted counts/units and displayed ranks/scores/pools. Zero tree counts are omitted; supplemental biosamples, study memberships and triads are nonadditive. {"assertions": [{"source": "GOLD", "count": 0, "unit": "ORGANISM", "row": {"row": 2440, "data": {"canonical_path": "Host-associated &gt; Mammals: Human &gt; Skeletal system &gt; Bone &gt; Compact bone", "ecosystem": "Host-associated", "ecosystem_category": "Mammals: Human", "ecosystem_type": "Skeletal system", "ecosystem_subtype": "Bone", "specific_ecosystem": "Compact bone", "leaf_label": "Compact bone", "depth": "5", "gold_node_count": "1", "organism_count": "0", "study_count": "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids": "gold.ecosystem:6579"}}}], "taxa": []}

### Association support and source limits

evidence: supported. Targets: habitatmech:GOLD.92256d7035.

The human compact-bone source can retain generic compact bone tissue as a broader class. Its source Bone parent is itself defined through BTO as hard connective tissue, not a whole skeletal organ; no part/whole exclusion is justified. Preserve both genera, source mint and zero-count semantics. The separate narrow mapping endpoint contract remains inconsistent. Each cited source supports only its stated scope; original source pairs were not exhaustively reconstructed.

### Native lifecycle and optional content

completeness: supported. Targets: habitatmech:GOLD.92256d7035.

Executed routes reproduce NARROW/SEEDED. Required fields are present; absent optional parameters, causal graphs, discussions and datasets are not fabricated. No scientific status promotion follows from this review.

### Native gates and exact reproduction

schema: supported. Targets: habitatmech:GOLD.92256d7035.

31 baseline commands passed: individual schemas, 24-target strict validation, 834 histories, provenance, exact 3209-record reproduction, 32 causal overlays, 110 term requests and configured labels. Exact-base hosted QC passed; deterministic validity is not scientific approval.

## Findings

### F1: Mapping uses an undeclared ontology-parent endpoint

major / open / confirmed; issue key: compact-bone-mapping-endpoint-contract.

The executed narrower-than-leaf route retains the source mint but emits narrowMatch relative to an ontology parent, whereas the schema endpoint is the record identifier. Reconcile producer, schema and consumers under #1398. This is not a formal SKOS self-link prohibition or a request for a blind predicate reversal.

## Recommended Actions And Acceptance Checks

### ACT1

The executed narrower-than-leaf route retains the source mint but emits narrowMatch relative to an ontology parent, whereas the schema endpoint is the record identifier. Reconcile producer, schema and consumers under #1398. This is not a formal SKOS self-link prohibition or a request for a blind predicate reversal. Proposed work only; no repair or status promotion is performed by this review.

- Regress the exact target claim and preserve valid genera, identifiers, source counts/units and taxon associations. Recover original evidence before deleting a provisional pair; do not decrement frozen totals by hand.
- Record authorized curation history; require schema, strict, provenance, history, label, corpus, site and full QC gates.
- Save an immutable successor with the same issue key and exact predecessor finding identity.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/compact_bone.yaml; Entire generated target YAML | supports | All fields, source attestations, displayed taxa, aliases and generated history read. |
| ERULE | docs/CURATION.md; Identity, strict parents and evidence scope | supports | All parent contributions must be strictly broader; source context, host, anatomy and diagnosis are distinct. Missing optional content or ITEM status alone is not a defect. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation and native statuses | supports | Mapping contract compares source concept to record identifier; source-is-record omits the predicate. Native count units and status gates retained. |
| ESEED | src/habitatmech/seed.py; Executed source routes and target reproduction | supports | [{"mint": "habitatmech:GOLD.92256d7035", "automatic": {"identifier": "habitatmech:GOLD.92256d7035", "grounding_status": "NARROW", "mapping_predicate": "skos:narrowMatch", "contributes_grounding": true, "extra_parents": ["UBERON:0001439"], "extra_xrefs": [], "route": "gold_narrower_than_leaf_match", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "habitatmech:GOLD.92256d7035", "grounding_status": "NARROW", "mapping_predicate": "skos:narrowMatch", "contributes_grounding": true, "extra_parents": ["UBERON:0001439"], "extra_xrefs": [], "route": "gold_narrower_than_leaf_match", "category": null, "reviewed": false, "decision": null}}] |
| EEXTRACT | src/habitatmech/extract.py; PREGO source projections | supports | Compact per-habitat tables preserve associations but do not retain original pair citations/dictionary provenance. |
| ET5 | data/raw/gold_ecosystem_paths.tsv; Physical TSV rows 2440 | supports | [{"row": 2440, "data": {"canonical_path": "Host-associated &gt; Mammals: Human &gt; Skeletal system &gt; Bone &gt; Compact bone", "ecosystem": "Host-associated", "ecosystem_category": "Mammals: Human", "ecosystem_type": "Skeletal system", "ecosystem_subtype": "Bone", "specific_ecosystem": "Compact bone", "leaf_label": "Compact bone", "depth": "5", "gold_node_count": "1", "organism_count": "0", "study_count": "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids": "gold.ecosystem:6579"}}] |
| ET6 | data/raw/ontology_subclass_edges.tsv; Physical TSV rows 11199 | supports | [{"row": 11199, "data": {"subject": "UBERON:0001439", "predicate": "rdfs:subClassOf", "object": "UBERON:0002481"}}] |
| ET7 | data/raw/ontology_terms.tsv; Physical TSV rows 13036 | supports | [{"row": 13036, "data": {"term_id": "UBERON:0001439", "ontology": "UBERON", "label": "compact bone tissue", "definition": "The outer layers of solid, hard bone that covers spongy bone; consists of parallel osteons containing mineral deposits and interstitial lamellae.", "synonyms": "bony cortex&#124;compact bone&#124;compact bone tissue&#124;cortical bone&#124;cortical bone tissue&#124;cortical region of bone&#124;substantia compacta&#124;substantia compacta (pars ossea)&#124;substantia corticalis", "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}}] |
| EP8 | data/habitats/host_associated/bone__234001be.yaml; Full immediate parent record, context only | supports | {"identifier": "habitatmech:GOLD.67f49f8b15", "label": "Bone", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats": ["BTO:0000140"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:5249", "source_label": "Bone", "source_path": "Host-associated &gt; Mammals: Human &gt; Skeletal system &gt; Bone", "mapping_predicate": "skos:narrowMatch", "assertion_count": 29, "assertion_unit": "ORGANISM", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NARROW."}, {"timestamp": "2026-10-15T00:00:00Z", "curator": "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.ea67ca30cb for habitatmech:GOLD.67f49f8b15 (Host-associated &gt; Mammals: Human &gt; Skeletal system &gt; Bone). Review https://github.com/CultureBotAI/HabitatMech/issues/2186. Bone is part of a skeletal system, not a subtype of the whole skeletal system. Exclude only this exact source-path/expected-parent contribution; preserve independent ontology genera, source observations and native status."}]} |
| EX9 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000140/graph; BTO_0000140-graph.json | context_only | Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000140", "target": "http://purl.obolibrary.org/obo/BTO_0000421", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/BTO_0000140", "target": "http://purl.obolibrary.org/obo/BTO_0001486", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX10 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000140; BTO_0000140.json | context_only | Current identity, definition, active status and typed synonyms: {"obo_id": "BTO:0000140", "label": "bone", "is_obsolete": false, "description": ["The hard form of connective tissue that constitutes the majority of the skeleton of most vertebrates; it consists of an organic component (the cells and matrix) and an inorganic, or mineral, component; the matrix contains a framework of collagenous fibers and is impregnated with the mineral component, chiefly calcium phosphate (85 per cent) and calcium carbonate (10 per cent), which imparts the quality of rigidity to bone."], "obo_synonym": null} |
| EX11 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001439/graph; UBERON_0001439-graph.json | context_only | Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001439", "target": "http://purl.obolibrary.org/obo/UBERON_0002481", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001439", "target": "http://purl.obolibrary.org/obo/UBERON_0002482", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX12 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001439; UBERON_0001439.json | context_only | Current identity, definition, active status and typed synonyms: {"obo_id": "UBERON:0001439", "label": "compact bone tissue", "is_obsolete": false, "description": ["MP distinguishes compact/cortical bone. in other AOs they are syns", "The outer layers of solid, hard bone that covers spongy bone; consists of parallel osteons containing mineral deposits and interstitial lamellae."], "obo_synonym": [{"name": "bony cortex", "scope": "hasExactSynonym", "type": null, "xrefs": [{"database": "HP", "id": "0002753", "description": null, "url": "http://purl.obolibrary.org/obo/HP_0002753"}]}, {"name": "compact bone", "scope": "hasExactSynonym", "type": null, "xrefs": [{"database": "MA", "id": "0001461", "description": null, "url": "http://www.informatics.jax.org/searches/AMA.cgi?id=MA:0001461"}]}, {"name": "substantia compacta", "scope": "hasExactSynonym", "type": "latin term", "xrefs": [{"database": "FMA", "id": "24018", "description": null, "url": "http://purl.org/sig/ont/fma/24018"}, {"database": "FMA", "id": "TA", "description": null, "url": null}]}, {"name": "substantia corticalis", "scope": "hasExactSynonym", "type": "latin term", "xrefs": [{"database": "FMA", "id": "24018", "description": null, "url": "http://purl.org/sig/ont/fma/24018"}, {"database": "FMA", "id": "TA", "description": null, "url": null}]}]} |
| ESEARCH | Local source and review corpus; rg --no-ignore --hidden -l -F -e habitatmech:GOLD.92256d7035 -e 'Compact bone' -e compact_bone -e habitatmech:GOLD.92256d7035 curation history research reports data/raw build reviews | context_only | Exact source keys and structured archive parsed independently; broad name hits are leads, not all inspected. No formal target predecessor. |

## Limits And Additional Notes

- Original specimen-level evidence and all pair-level citations were not exhaustively reconstructed. Native association counts, taxon ranks and scores do not establish prevalence, viability or characteristic presence.
- Configured label validation skips 2063 no-adapter pairs. Exact target TaxIds were separately resolved; frozen taxon labels are not universally current.
- Exact-base hosted QC covers unchanged scientific inputs, not a fresh local full-QC execution or these new review outputs. Native validate/save and subsequent archive/final-head gates are separate.
- iModulonDB is not applicable: no gene, regulator or expression-module claim is asserted. No new causal mechanism is imported.
- All captured local input hashes were independently checked against exact base 13cddc722250dcad4327e5f9fad0a12fe7c08268.
- This baseline observation changes no scientific input. Separately authorized PR remediation follows; no status promotion is conferred by review validation.
- Ignored-inclusive structured archive traversal found no formal previous target review. Legacy reports are context, not predecessor lineage.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T054403Z-compact_bone-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: Compact bone (habitatmech:GOLD.92256d7035)'
started_at: '2026-10-16T05:13:49Z'
finished_at: '2026-10-16T05:44:03Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Parent agent integrates evidence and separate-agent source/hierarchy
    cross-checks; not independent human approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: The human compact-bone source can retain generic compact bone tissue as a
  broader class. Its source Bone parent is itself defined through BTO as hard connective
  tissue, not a whole skeletal organ; no part/whole exclusion is justified. Preserve
  both genera, source mint and zero-count semantics. The separate narrow mapping endpoint
  contract remains inconsistent.
source:
  git_revision: 13cddc722250dcad4327e5f9fad0a12fe7c08268
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
    sha256: 5d3af0a0505a61cda5e088e2c4b7922b740b7423fbca957d49aa8261b5584b37
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 37dc4b40642d19e7b5c3262f368d12daa82e03115e7731a2326ae88785ceff5b
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 29671974bab045cad2620da3ad89d176f8a2f5ca2612ad3c8761d82fd3f1ea81
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: c1207270bb0ae2031e42de6cb8220b20f98886f65e40d48793bfd7e9d757d83a
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
  - path: data/habitats/host_associated/bone__234001be.yaml
    sha256: c6d0f96926a82855fac759ecb36e58b00ca1d6458db41db4265b272d890f2d5a
    role: context
  - path: data/habitats/host_associated/compact_bone.yaml
    sha256: b300f21fc8175f0891962c709b2f19425c3462837daea0fa81aef2d02fca26a1
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
- target_id: habitatmech:GOLD.92256d7035
  path: data/habitats/host_associated/compact_bone.yaml
  label: Compact bone
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
  description: Full field-by-field assessment of this one resolved generated target.
  selection: One of the next 24 unreviewed targets in deterministic path order from
    the ignored-inclusive 3209-record census. This bundle is not a proxy sample.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.92256d7035
  exclusions:
  - target: Other records, original specimens and SSSOM/KGX products
    reason: Parents are contextual evidence, not additional review coverage; original
      specimens and exports are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/compact_bone.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.92256d7035
  summary: "Finished 2026-10-16T05:15:45Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/compact_bone.yaml"
  scope_note: Individual schema; strict covers 24 targets; other native commands retain
    full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/column.yaml data/habitats/host_associated/common_warts.yaml
    data/habitats/host_associated/compact_bone.yaml data/habitats/host_associated/compact_bone__c00eaa73.yaml
    data/habitats/host_associated/conjunctiva.yaml data/habitats/host_associated/conjunctiva__482ca0a7.yaml
    data/habitats/host_associated/conjunctiva__6e913f9c.yaml data/habitats/host_associated/connective_tissue.yaml
    data/habitats/host_associated/connective_tissue__85a5a212.yaml data/habitats/host_associated/connective_tissue__b37fb9b6.yaml
    data/habitats/host_associated/coprolite.yaml data/habitats/host_associated/coral.yaml
    data/habitats/host_associated/corn_silk.yaml data/habitats/host_associated/cornea.yaml
    data/habitats/host_associated/cornea__2a9b9367.yaml data/habitats/host_associated/cornea__f146d32e.yaml
    data/habitats/host_associated/cortex.yaml data/habitats/host_associated/crop.yaml
    data/habitats/host_associated/crop__310374d9.yaml data/habitats/host_associated/crop__3de61c58.yaml
    data/habitats/host_associated/crop__a03dd0e3.yaml data/habitats/host_associated/crop__d566c329.yaml
    data/habitats/host_associated/crop_content.yaml data/habitats/host_associated/crown_gall.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.92256d7035
  summary: "Finished 2026-10-16T05:17:09Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/column.yaml data/habitats/host_associated/common_warts.yaml\
    \ data/habitats/host_associated/compact_bone.yaml data/habitats/host_associated/compact_bone__c00eaa73.yaml\
    \ data/habitats/host_associated/conjunctiva.yaml data/habitats/host_associated/conjunctiva__482ca0a7.yaml\
    \ data/habitats/host_associated/conjunctiva__6e913f9c.yaml data/habitats/host_associated/connective_tissue.yaml\
    \ data/habitats/host_associated/connective_tissue__85a5a212.yaml data/habitats/host_associated/connective_tissue__b37fb9b6.yaml\
    \ data/habitats/host_associated/coprolite.yaml data/habitats/host_associated/coral.yaml\
    \ data/habitats/host_associated/corn_silk.yaml data/habitats/host_associated/cornea.yaml\
    \ data/habitats/host_associated/cornea__2a9b9367.yaml data/habitats/host_associated/cornea__f146d32e.yaml\
    \ data/habitats/host_associated/cortex.yaml data/habitats/host_associated/crop.yaml\
    \ data/habitats/host_associated/crop__310374d9.yaml data/habitats/host_associated/crop__3de61c58.yaml\
    \ data/habitats/host_associated/crop__a03dd0e3.yaml data/habitats/host_associated/crop__d566c329.yaml\
    \ data/habitats/host_associated/crop_content.yaml data/habitats/host_associated/crown_gall.yaml\n\
    Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      24\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Individual schema; strict covers 24 targets; other native commands retain
    full-corpus scope.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.92256d7035
  summary: 'Finished 2026-10-16T05:17:16Z. No issues found

    834 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Individual schema; strict covers 24 targets; other native commands retain
    full-corpus scope.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.92256d7035
  summary: "Finished 2026-10-16T05:17:16Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Individual schema; strict covers 24 targets; other native commands retain
    full-corpus scope.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.92256d7035
  summary: "Finished 2026-10-16T05:17:32Z. expected 3209 records, found 3209 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Individual schema; strict covers 24 targets; other native commands retain
    full-corpus scope.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.92256d7035
  summary: "Finished 2026-10-16T05:17:36Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Individual schema; strict covers 24 targets; other native commands retain
    full-corpus scope.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.92256d7035
  summary: "Finished 2026-10-16T05:17:53Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Individual schema; strict covers 24 targets; other native commands retain
    full-corpus scope.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.92256d7035
  summary: "Finished 2026-10-16T05:18:37Z. id↔label correspondence summary:\n    \
    \      OK_CANONICAL: 1173\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2063\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Individual schema; strict covers 24 targets; other native commands retain
    full-corpus scope.
- check_id: CCI
  name: Exact-base hosted native QC
  status: passed
  required: true
  command: gh run view 38852350960 --repo CultureBotAI/HabitatMech --json headSha,conclusion,url,jobs
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.92256d7035
  summary: Verified 2026-10-16T05:19:04Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38852350960
  scope_note: Unchanged scientific-input base; not new review-output validation.
- check_id: CPOOL
  name: Candidate-pool correspondence
  status: passed
  required: false
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python3
    /private/tmp/habitatmech-review-cr-author.py pool_check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.92256d7035
  summary: Finished 2026-10-16T05:42:35Z. All 67 displayed candidate pools equal exact
    source taxon totals.
  scope_note: Supplemental exact source-total check, not a replacement for native
    validators or scientific evidence.
- check_id: CREF
  name: Standalone citation validation applicability
  status: not_applicable
  required: false
  target_ids:
  - habitatmech:GOLD.92256d7035
  summary: No standalone citation validator is documented for these generated targets
    without evidence objects. Current authorities verify stable references; full-corpus
    causal validation ran.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/compact_bone.yaml
  locator: Entire generated target YAML
  accessed_at: '2026-10-16T05:44:03Z'
  support: supports
  summary: All fields, source attestations, displayed taxa, aliases and generated
    history read.
  snapshot_sha256: b300f21fc8175f0891962c709b2f19425c3462837daea0fa81aef2d02fca26a1
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, strict parents and evidence scope
  accessed_at: '2026-10-16T05:44:03Z'
  support: supports
  summary: All parent contributions must be strictly broader; source context, host,
    anatomy and diagnosis are distinct. Missing optional content or ITEM status alone
    is not a defect.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation and native statuses
  accessed_at: '2026-10-16T05:44:03Z'
  support: supports
  summary: Mapping contract compares source concept to record identifier; source-is-record
    omits the predicate. Native count units and status gates retained.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed source routes and target reproduction
  accessed_at: '2026-10-16T05:44:03Z'
  support: supports
  summary: '[{"mint": "habitatmech:GOLD.92256d7035", "automatic": {"identifier": "habitatmech:GOLD.92256d7035",
    "grounding_status": "NARROW", "mapping_predicate": "skos:narrowMatch", "contributes_grounding":
    true, "extra_parents": ["UBERON:0001439"], "extra_xrefs": [], "route": "gold_narrower_than_leaf_match",
    "category": null, "reviewed": false, "decision": null}, "final": {"identifier":
    "habitatmech:GOLD.92256d7035", "grounding_status": "NARROW", "mapping_predicate":
    "skos:narrowMatch", "contributes_grounding": true, "extra_parents": ["UBERON:0001439"],
    "extra_xrefs": [], "route": "gold_narrower_than_leaf_match", "category": null,
    "reviewed": false, "decision": null}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: PREGO source projections
  accessed_at: '2026-10-16T05:44:03Z'
  support: supports
  summary: Compact per-habitat tables preserve associations but do not retain original
    pair citations/dictionary provenance.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Physical TSV rows 2440
  accessed_at: '2026-10-16T05:44:03Z'
  support: supports
  summary: '[{"row": 2440, "data": {"canonical_path": "Host-associated > Mammals:
    Human > Skeletal system > Bone > Compact bone", "ecosystem": "Host-associated",
    "ecosystem_category": "Mammals: Human", "ecosystem_type": "Skeletal system", "ecosystem_subtype":
    "Bone", "specific_ecosystem": "Compact bone", "leaf_label": "Compact bone", "depth":
    "5", "gold_node_count": "1", "organism_count": "0", "study_count": "0", "biosample_count":
    "0", "total_assertions": "0", "gold_node_ids": "gold.ecosystem:6579"}}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: ET6
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: Physical TSV rows 11199
  accessed_at: '2026-10-16T05:44:03Z'
  support: supports
  summary: '[{"row": 11199, "data": {"subject": "UBERON:0001439", "predicate": "rdfs:subClassOf",
    "object": "UBERON:0002481"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET7
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 13036
  accessed_at: '2026-10-16T05:44:03Z'
  support: supports
  summary: '[{"row": 13036, "data": {"term_id": "UBERON:0001439", "ontology": "UBERON",
    "label": "compact bone tissue", "definition": "The outer layers of solid, hard
    bone that covers spongy bone; consists of parallel osteons containing mineral
    deposits and interstitial lamellae.", "synonyms": "bony cortex|compact bone|compact
    bone tissue|cortical bone|cortical bone tissue|cortical region of bone|substantia
    compacta|substantia compacta (pars ossea)|substantia corticalis", "deprecated":
    "", "directly_referenced": "FALSE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EP8
  kind: record_content
  reference: data/habitats/host_associated/bone__234001be.yaml
  locator: Full immediate parent record, context only
  accessed_at: '2026-10-16T05:44:03Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.67f49f8b15", "label": "Bone", "habitat_category":
    "HOST_ASSOCIATED", "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats":
    ["BTO:0000140"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:5249",
    "source_label": "Bone", "source_path": "Host-associated > Mammals: Human > Skeletal
    system > Bone", "mapping_predicate": "skos:narrowMatch", "assertion_count": 29,
    "assertion_unit": "ORGANISM", "notes": "2 GOLD ecosystem node ids share this path;
    first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp":
    "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES",
    "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NARROW."},
    {"timestamp": "2026-10-15T00:00:00Z", "curator": "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED",
    "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.ea67ca30cb
    for habitatmech:GOLD.67f49f8b15 (Host-associated > Mammals: Human > Skeletal system
    > Bone). Review https://github.com/CultureBotAI/HabitatMech/issues/2186. Bone
    is part of a skeletal system, not a subtype of the whole skeletal system. Exclude
    only this exact source-path/expected-parent contribution; preserve independent
    ontology genera, source observations and native status."}]}'
  snapshot_sha256: c6d0f96926a82855fac759ecb36e58b00ca1d6458db41db4265b272d890f2d5a
- evidence_id: EX9
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000140/graph
  locator: BTO_0000140-graph.json
  accessed_at: '2026-10-16T05:15:20Z'
  support: context_only
  summary: 'Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000140",
    "target": "http://purl.obolibrary.org/obo/BTO_0000421", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/BTO_0000140",
    "target": "http://purl.obolibrary.org/obo/BTO_0001486", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 14ec2b72ca358eed8ca91634929743f2dfff7491c094c0eeab5491e982c7ca35
- evidence_id: EX10
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000140
  locator: BTO_0000140.json
  accessed_at: '2026-10-16T05:15:19Z'
  support: context_only
  summary: 'Current identity, definition, active status and typed synonyms: {"obo_id":
    "BTO:0000140", "label": "bone", "is_obsolete": false, "description": ["The hard
    form of connective tissue that constitutes the majority of the skeleton of most
    vertebrates; it consists of an organic component (the cells and matrix) and an
    inorganic, or mineral, component; the matrix contains a framework of collagenous
    fibers and is impregnated with the mineral component, chiefly calcium phosphate
    (85 per cent) and calcium carbonate (10 per cent), which imparts the quality of
    rigidity to bone."], "obo_synonym": null}'
  snapshot_sha256: 75f23eb9636f74b74c10224f169aab677ce7cdba087ca4d5e51fba9a875cff6f
- evidence_id: EX11
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001439/graph
  locator: UBERON_0001439-graph.json
  accessed_at: '2026-10-16T05:16:13Z'
  support: context_only
  summary: 'Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001439",
    "target": "http://purl.obolibrary.org/obo/UBERON_0002481", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001439",
    "target": "http://purl.obolibrary.org/obo/UBERON_0002482", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 8347006ab532e05d99833b203efa29d7a1d572b16babaab6a7d5db8646b440b8
- evidence_id: EX12
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001439
  locator: UBERON_0001439.json
  accessed_at: '2026-10-16T05:16:13Z'
  support: context_only
  summary: 'Current identity, definition, active status and typed synonyms: {"obo_id":
    "UBERON:0001439", "label": "compact bone tissue", "is_obsolete": false, "description":
    ["MP distinguishes compact/cortical bone. in other AOs they are syns", "The outer
    layers of solid, hard bone that covers spongy bone; consists of parallel osteons
    containing mineral deposits and interstitial lamellae."], "obo_synonym": [{"name":
    "bony cortex", "scope": "hasExactSynonym", "type": null, "xrefs": [{"database":
    "HP", "id": "0002753", "description": null, "url": "http://purl.obolibrary.org/obo/HP_0002753"}]},
    {"name": "compact bone", "scope": "hasExactSynonym", "type": null, "xrefs": [{"database":
    "MA", "id": "0001461", "description": null, "url": "http://www.informatics.jax.org/searches/AMA.cgi?id=MA:0001461"}]},
    {"name": "substantia compacta", "scope": "hasExactSynonym", "type": "latin term",
    "xrefs": [{"database": "FMA", "id": "24018", "description": null, "url": "http://purl.org/sig/ont/fma/24018"},
    {"database": "FMA", "id": "TA", "description": null, "url": null}]}, {"name":
    "substantia corticalis", "scope": "hasExactSynonym", "type": "latin term", "xrefs":
    [{"database": "FMA", "id": "24018", "description": null, "url": "http://purl.org/sig/ont/fma/24018"},
    {"database": "FMA", "id": "TA", "description": null, "url": null}]}]}'
  snapshot_sha256: a9809483e633c64aac8a8ff5403aea2dd8b9482dd3238f94d999c8da0bc6d7b2
- evidence_id: ESEARCH
  kind: search
  reference: Local source and review corpus
  locator: rg --no-ignore --hidden -l -F -e habitatmech:GOLD.92256d7035 -e 'Compact
    bone' -e compact_bone -e habitatmech:GOLD.92256d7035 curation history research
    reports data/raw build reviews
  accessed_at: '2026-10-16T05:15:46Z'
  support: context_only
  summary: Exact source keys and structured archive parsed independently; broad name
    hits are leads, not all inspected. No formal target predecessor.
  search_scope: curation, history, research, reports, data/raw, build and reviews
    including hidden/ignored files; independent structured YAML traversal.
assessments:
- assessment_id: A1
  area: identity
  topic: Identity, grounding, aliases and strict hierarchy
  outcome: concern
  summary: The human compact-bone source can retain generic compact bone tissue as
    a broader class. Its source Bone parent is itself defined through BTO as hard
    connective tissue, not a whole skeletal organ; no part/whole exclusion is justified.
    Preserve both genera, source mint and zero-count semantics. The separate narrow
    mapping endpoint contract remains inconsistent.
  target_ids:
  - habitatmech:GOLD.92256d7035
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EEXTRACT
  - ET5
  - ET6
  - ET7
  - EP8
  - EX9
  - EX10
  - EX11
  - EX12
- assessment_id: A2
  area: quantity
  topic: Counts, units, taxon ranks, scores and candidate pools
  outcome: supported
  summary: 'Exact source rows reproduce emitted counts/units and displayed ranks/scores/pools.
    Zero tree counts are omitted; supplemental biosamples, study memberships and triads
    are nonadditive. {"assertions": [{"source": "GOLD", "count": 0, "unit": "ORGANISM",
    "row": {"row": 2440, "data": {"canonical_path": "Host-associated > Mammals: Human
    > Skeletal system > Bone > Compact bone", "ecosystem": "Host-associated", "ecosystem_category":
    "Mammals: Human", "ecosystem_type": "Skeletal system", "ecosystem_subtype": "Bone",
    "specific_ecosystem": "Compact bone", "leaf_label": "Compact bone", "depth": "5",
    "gold_node_count": "1", "organism_count": "0", "study_count": "0", "biosample_count":
    "0", "total_assertions": "0", "gold_node_ids": "gold.ecosystem:6579"}}}], "taxa":
    []}'
  target_ids:
  - habitatmech:GOLD.92256d7035
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EEXTRACT
  - ET5
  - ET6
  - ET7
  - EP8
  - EX9
  - EX10
  - EX11
  - EX12
- assessment_id: A3
  area: evidence
  topic: Association support and source limits
  outcome: supported
  summary: The human compact-bone source can retain generic compact bone tissue as
    a broader class. Its source Bone parent is itself defined through BTO as hard
    connective tissue, not a whole skeletal organ; no part/whole exclusion is justified.
    Preserve both genera, source mint and zero-count semantics. The separate narrow
    mapping endpoint contract remains inconsistent. Each cited source supports only
    its stated scope; original source pairs were not exhaustively reconstructed.
  target_ids:
  - habitatmech:GOLD.92256d7035
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EEXTRACT
  - ET5
  - ET6
  - ET7
  - EP8
  - EX9
  - EX10
  - EX11
  - EX12
- assessment_id: A4
  area: completeness
  topic: Native lifecycle and optional content
  outcome: supported
  summary: Executed routes reproduce NARROW/SEEDED. Required fields are present; absent
    optional parameters, causal graphs, discussions and datasets are not fabricated.
    No scientific status promotion follows from this review.
  target_ids:
  - habitatmech:GOLD.92256d7035
  evidence_ids:
  - E1
  - ESCHEMA
  - ESEED
- assessment_id: A5
  area: schema
  topic: Native gates and exact reproduction
  outcome: supported
  summary: '31 baseline commands passed: individual schemas, 24-target strict validation,
    834 histories, provenance, exact 3209-record reproduction, 32 causal overlays,
    110 term requests and configured labels. Exact-base hosted QC passed; deterministic
    validity is not scientific approval.'
  target_ids:
  - habitatmech:GOLD.92256d7035
  evidence_ids:
  - E1
  - ESCHEMA
  - ERULE
findings:
- finding_id: F1
  issue_key: compact-bone-mapping-endpoint-contract
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Mapping uses an undeclared ontology-parent endpoint
  description: 'The executed narrower-than-leaf route retains the source mint but
    emits narrowMatch relative to an ontology parent, whereas the schema endpoint
    is the record identifier. Reconcile producer, schema and consumers under #1398.
    This is not a formal SKOS self-link prohibition or a request for a blind predicate
    reversal.'
  target_ids:
  - habitatmech:GOLD.92256d7035
  field_paths:
  - source_attestations[0].mapping_predicate
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EEXTRACT
  - ET5
  - ET6
  - ET7
  - EP8
  - EX9
  - EX10
  - EX11
  - EX12
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never hand-edit generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; never hand-edit generated habitat YAML
  rule_id: docs/CURATION.md and native field-by-field review checklist
  native_severity: major
  normalization_reason: Material hierarchy, grounding, representation or pair-evidence
    mismatch. Source reproduction alone does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - habitatmech:GOLD.92256d7035
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never hand-edit generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; never hand-edit generated habitat YAML
  description: 'The executed narrower-than-leaf route retains the source mint but
    emits narrowMatch relative to an ontology parent, whereas the schema endpoint
    is the record identifier. Reconcile producer, schema and consumers under #1398.
    This is not a formal SKOS self-link prohibition or a request for a blind predicate
    reversal. Proposed work only; no repair or status promotion is performed by this
    review.'
  generator: Controlled source/input correction, just seed, inspected just seed-canary,
    guarded just seed-apply, and dependent term-request/map/site/redirect regeneration
    where required.
  acceptance_checks:
  - Regress the exact target claim and preserve valid genera, identifiers, source
    counts/units and taxon associations. Recover original evidence before deleting
    a provisional pair; do not decrement frozen totals by hand.
  - Record authorized curation history; require schema, strict, provenance, history,
    label, corpus, site and full QC gates.
  - Save an immutable successor with the same issue key and exact predecessor finding
    identity.
limitations:
- Original specimen-level evidence and all pair-level citations were not exhaustively
  reconstructed. Native association counts, taxon ranks and scores do not establish
  prevalence, viability or characteristic presence.
- Configured label validation skips 2063 no-adapter pairs. Exact target TaxIds were
  separately resolved; frozen taxon labels are not universally current.
- Exact-base hosted QC covers unchanged scientific inputs, not a fresh local full-QC
  execution or these new review outputs. Native validate/save and subsequent archive/final-head
  gates are separate.
- 'iModulonDB is not applicable: no gene, regulator or expression-module claim is
  asserted. No new causal mechanism is imported.'
notes:
- All captured local input hashes were independently checked against exact base 13cddc722250dcad4327e5f9fad0a12fe7c08268.
- This baseline observation changes no scientific input. Separately authorized PR
  remediation follows; no status promotion is conferred by review validation.
- Ignored-inclusive structured archive traversal found no formal previous target review.
  Legacy reports are context, not predecessor lineage.
tags:
- individual-scientific-review
- host-associated
```
