# Record review: apocrine sweat gland (BTO:0001458)

- Review: 20261015T062602Z-apocrine_sweat_gland-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T06:06:45Z
- Finished UTC: 2026-10-15T06:26:02Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The BTO apocrine sweat-gland identity and both gland superclasses are supported. The separate GOLD integumentary-system contribution is an invalid whole-system superclass.

## Scope And Provenance

Individual scientific assessment of the exact generated target at the captured main revision.

Selection: Resolved identifier and source path in the next sixteen unreviewed records in corpus path order; this document assesses only its single target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base d255ab29c86291d2166fcf22219c10a9edb136c9.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0001458 | data/habitats/host_associated/apocrine_sweat_gland.yaml | generated | apocrine sweat gland |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0001458 | Actual exit 0 at 2026-10-15T06:06:46Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/apocrine_sweat_gland.yaml |
| validate-strict | passed | True | BTO:0001458 | Actual exit 0 at 2026-10-15T06:07:14Z. uv run python scripts/validate_strict.py data/habitats/host_associated/anterior_nares.yaml data/habitats/host_associated/anterior_nares__14fc5dcc.yaml data/habitats/host_associated/anther.yaml data/habitats/host_associated/anthosphere.yaml data/habitats/host_associated/antler.yaml data/habitats/host_associated/aortic_valve.yaml data/habitats/host_associated/apocrine_sweat_gland.yaml data/habitats/host_associated/apoeccrine_sweat_glands.yaml data/habitats/host_associated/appendix.yaml data/habitats/host_associated/appendix__8f7f5041.yaml data/habitats/host_associated/appendix_abscess.yaml data/habitats/host_associated/appressorium.yaml data/habitats/host_associated/aquatic_mammal.yaml data/habitats/host_associated/aquatic_plant.yaml data/habitats/host_associated/aqueous_humor_of_eyeball.yaml data/habitats/host_associated/area_of_moss_dominated_vegetation.yaml<br>Validating 16 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      16<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | BTO:0001458 | Actual exit 0 at 2026-10-15T06:07:22Z. No issues found<br>746 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | BTO:0001458 | Actual exit 0 at 2026-10-15T06:07:23Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | BTO:0001458 | Actual exit 0 at 2026-10-15T06:07:39Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | BTO:0001458 | Actual exit 0 at 2026-10-15T06:07:43Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | BTO:0001458 | Actual exit 0 at 2026-10-15T06:08:00Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | BTO:0001458 | Actual exit 0 at 2026-10-15T06:08:42Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |

## Scientific And Domain Assessments

### Native structural and reproduction checks

schema: supported. Targets: BTO:0001458.

Recorded gates passed: schema, strict sixteen-target validation, 746 history records, exact 3,208-record reproduction, 32 causal graphs and 110 term requests. These are not scientific proof.

### Habitat identity and full source scope

identity: concern. Targets: BTO:0001458.

The BTO apocrine sweat-gland identity and both gland superclasses are supported. The separate GOLD integumentary-system contribution is an invalid whole-system superclass.

### Source counts, units and retained taxon observations

quantity: supported. Targets: BTO:0001458.

Exact contributing source rows, emitted counts/units, taxon labels/ranks and source scores were compared. [{"source": "GOLD", "count": 0, "unit": "ORGANISM"}]. 0 retained taxon IDs match current NCBI names. Zero counts are omitted, and later bulk biosamples/studies are not added to frozen ORGANISM counts. Source pools are not prevalence denominators.

### Parameters, causal claims and optional evidence

completeness: not_applicable. Targets: BTO:0001458.

No target causal graph, environmental-parameter, mechanism or characteristic-presence assertion requires expansion. No absent optional field is populated for coverage. Parent-record mechanisms are not inherited as evidence for this target.

## Findings

### F1: Source context is asserted as a broader habitat

major / open / confirmed; issue key: apocrine-sweat-gland-source-parent.

A sweat gland is not a whole integumentary system. Both BTO gland superclasses remain valid. Exclude only the immediate GOLD contribution habitatmech:GOLD.dc86c8917c with exact source-path and expected-parent guards; preserve independent parents and verbatim source provenance.

## Recommended Actions And Acceptance Checks

### ACT1

A sweat gland is not a whole integumentary system. Both BTO gland superclasses remain valid. Exclude only the immediate GOLD contribution habitatmech:GOLD.dc86c8917c with exact source-path and expected-parent guards; preserve independent parents and verbatim source provenance. Use maintained owners, not generated YAML edits.

- Regress the exact target and preserve independently valid source identities, counts/units, taxa, status and parents.
- Append session history; run strict schema, history, provenance, reproduction, configured label and full QC gates.
- Save a successor with exact finding lineage; do not rewrite this observation or claim broader export conformance.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/apocrine_sweat_gland.yaml; Entire YAML | supports | All target fields and generated history were read. |
| ERULE | docs/CURATION.md; Hosts, anatomy, strict broader hierarchy and input ownership | supports | Anatomy may identify a microbial site; host taxa are not environment identities; every parent must be strictly broader. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate and taxon fields | supports | Mapping endpoint is the emitted record; association metrics and characteristic flags are separate. |
| ESEED | src/habitatmech/seed.py; resolve_gold, resolve_bacdive, ingest_prego, apply_decision and apply_curated_definitions | supports | All contributing native resolution routes executed with complete claimant and mapping pools; final identifier/status/predicate agree: [{"automatic": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "UNGROUNDED", "identifier": "habitatmech:GOLD.f3c6dc4883", "mapping_predicate": null, "reviewed": false, "route": "gold_unmatched"}, "final": {"category": null, "contributes_grounding": true, "decision": {"category": "", "curator": "claude-opus-5", "date": "2026-08-12", "decision": "GROUND", "grounding_status": "EXACT", "identifier": "habitatmech:GOLD.f3c6dc4883", "notes": "Leaf label equals the BTO label exactly and no other source concept claims it. Path: Host-associated &gt; Mammals: Human &gt; Integumentary system &gt; Apocrine sweat glands", "object_id": "BTO:0001458", "object_label": "apocrine sweat gland", "relation": "parent", "review_depth": "ITEM"}, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "BTO:0001458", "mapping_predicate": "skos:exactMatch", "reviewed": true, "route": "curated_ground_from_gold_unmatched"}, "mint": "habitatmech:GOLD.f3c6dc4883", "source": "GOLD"}] |
| ET4 | data/raw/gold_ecosystem_paths.tsv; TSV rows 2254 | supports | [{"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Mammals: Human &gt; Integumentary system &gt; Apocrine sweat glands", "depth": "4", "ecosystem": "Host-associated", "ecosystem_category": "Mammals: Human", "ecosystem_subtype": "Apocrine sweat glands", "ecosystem_type": "Integumentary system", "gold_node_count": "2", "gold_node_ids": "gold.ecosystem:6863&#124;gold.ecosystem:6867", "leaf_label": "Apocrine sweat glands", "organism_count": "0", "specific_ecosystem": "", "study_count": "0", "total_assertions": "0"}, "row": 2254}] |
| ET5 | data/raw/ontology_subclass_edges.tsv; TSV rows 784,911,912,1002,1003 | supports | [{"data": {"object": "BTO:0000522", "predicate": "rdfs:subClassOf", "subject": "BTO:0001162"}, "row": 784}, {"data": {"object": "BTO:0000431", "predicate": "rdfs:subClassOf", "subject": "BTO:0001331"}, "row": 911}, {"data": {"object": "BTO:0000765", "predicate": "rdfs:subClassOf", "subject": "BTO:0001331"}, "row": 912}, {"data": {"object": "BTO:0001162", "predicate": "rdfs:subClassOf", "subject": "BTO:0001458"}, "row": 1002}, {"data": {"object": "BTO:0001331", "predicate": "rdfs:subClassOf", "subject": "BTO:0001458"}, "row": 1003}] |
| ET6 | data/raw/ontology_terms.tsv; TSV rows 1163,1332,1458 | supports | [{"data": {"definition": "A gland whose discharged secretion contains part of the secreting cells.", "deprecated": "", "directly_referenced": "FALSE", "label": "apocrine gland", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0001162"}, "row": 1163}, {"data": {"definition": "A simple tubular gland of the skin that secretes perspiration, is widely distributed in nearly all parts of the human skin, and consists typically of an epithelial tube extending spirally from a minute pore on the surface of the skin into the dermis or subcutaneous tissues where it ends in a convoluted tuft.", "deprecated": "", "directly_referenced": "FALSE", "label": "sweat gland", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0001331"}, "row": 1332}, {"data": {"definition": "A type of large, branched, specialized sudoriferous gland (glandula sudorifera) that empties into the upper portion of a hair follicle instead of directly onto the skin surface; found only on certain areas of the body, such as around the anus and in the axilla; after puberty they produce a viscous secretion that is acted on by bacteria to produce a characteristic acrid odor.", "deprecated": "", "directly_referenced": "TRUE", "label": "apocrine sweat gland", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0001458"}, "row": 1458}] |
| ET7 | curation/decisions.tsv; TSV rows 1355 | supports | [{"data": {"category": "", "curator": "claude-opus-5", "date": "2026-08-12", "decision": "GROUND", "grounding_status": "EXACT", "identifier": "habitatmech:GOLD.f3c6dc4883", "notes": "Leaf label equals the BTO label exactly and no other source concept claims it. Path: Host-associated &gt; Mammals: Human &gt; Integumentary system &gt; Apocrine sweat glands", "object_id": "BTO:0001458", "object_label": "apocrine sweat gland", "relation": "", "review_depth": "ITEM"}, "row": 1355}] |
| EP8 | data/habitats/host_associated/integumentary_system__2442c03e.yaml; Direct-parent identity, definition, parent and source fields | supports | Inspected parent meaning: {"grounding_status": "NARROW", "identifier": "habitatmech:GOLD.dc86c8917c", "label": "Integumentary system", "parent_habitats": ["UBERON:0002416", "habitatmech:GOLD.cd0b0940e5"], "source_attestations": [{"mapping_predicate": "skos:narrowMatch", "notes": "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:6113", "source_label": "Integumentary system", "source_path": "Host-associated &gt; Mammals: Human &gt; Integumentary system"}]} |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001458; Target term or typed outgoing relations; primary abstract; exact strain identity and isolation-source fields as described | supports | Active authoritative BTO:0001458 apocrine sweat gland; definition and typed scope compared with the frozen source and local parent meaning. Obsolete=False. |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001458/graph; Target term or typed outgoing relations; primary abstract; exact strain identity and isolation-source fields as described | supports | Inspected typed outgoing relations: [{"label": "subClassOf", "source": "http://purl.obolibrary.org/obo/BTO_0001458", "target": "http://purl.obolibrary.org/obo/BTO_0001162", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf"}, {"label": "subClassOf", "source": "http://purl.obolibrary.org/obo/BTO_0001458", "target": "http://purl.obolibrary.org/obo/BTO_0001331", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf"}]. Partonomy and connectivity remain distinct from subclassing. |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001162; Target term or typed outgoing relations; primary abstract; exact strain identity and isolation-source fields as described | supports | Active authoritative BTO:0001162 apocrine gland; definition and typed scope compared with the frozen source and local parent meaning. Obsolete=False. |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001331; Target term or typed outgoing relations; primary abstract; exact strain identity and isolation-source fields as described | supports | Active authoritative BTO:0001331 sweat gland; definition and typed scope compared with the frozen source and local parent meaning. Obsolete=False. |
| EX5 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002416; Target term or typed outgoing relations; primary abstract; exact strain identity and isolation-source fields as described | supports | Active authoritative UBERON:0002416 integumental system; definition and typed scope compared with the frozen source and local parent meaning. Obsolete=False. |
| ESEARCH | Local scientific-input and saved-review traversal; rg --no-ignore --hidden -l -F -e BTO:0001458 -e 'apocrine sweat gland' -e apocrine_sweat_gland -e habitatmech:GOLD.f3c6dc4883 curation history research reports data/raw build reviews | context_only | Ignored-inclusive source ID/label/slug search plus exact parsed table matches and complete structured-target traversal. No structured predecessor targets this record. |

## Limits And Additional Notes

- Frozen source-bin membership is not a complete audit of original specimens. Only the exact external source witnesses described here were independently inspected.
- Taxon associations are observational. PREGO score and BacDive strain counts do not prove prevalence, mechanism or characteristic presence.
- The configured label gate skipped 2,061 no-adapter pairs. Ontology semantics and retained taxon identities were separately assessed.
- The full archive and just qc are publication gates to run after saving; these pre-fix observations do not claim their future results.
- Historical reports and history prose are search leads, not independent approval. Historical neighboring claims and every legacy citation were not re-reviewed.
- iModulonDB is not applicable: these targets assert no gene, regulator or transcriptomic mechanism. No paid research was used.
- All captured local input bytes were rechecked unchanged against the working tree and exact Git blobs.
- Ignored-inclusive structured archive traversal found no earlier structured review targeting this record. Historical reports and GitHub issues are retained as contextual leads.
- This is a pre-fix observation; separately authorized curation requires new successor observations.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T062602Z-apocrine_sweat_gland-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: apocrine sweat gland (BTO:0001458)'
started_at: '2026-10-15T06:06:45Z'
finished_at: '2026-10-15T06:26:02Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent assessed full records and primary evidence. This
    is not independent human or second-agent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: The BTO apocrine sweat-gland identity and both gland superclasses are supported.
  The separate GOLD integumentary-system contribution is an invalid whole-system superclass.
source:
  git_revision: d255ab29c86291d2166fcf22219c10a9edb136c9
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
    sha256: a3e2880134344406dd3239ee041076df64c76407d311b71a16f2382c4146a177
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 761c1c1c60358c6c24e4d797637a12bdde6f8541e568914b404bffd1e0dd57ec
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: ea37676f1a16dd05fbfbb6c394b3f14b42ea93b763fb257043b817a4f10d3612
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: 2144d43ab4e106ff820da87c348f673d16cb8ea30d5a565f12e156af598f85ad
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
  - path: data/habitats/host_associated/apocrine_sweat_gland.yaml
    sha256: 34fca3014974aea71b3163312e34ae64415ee2441e4a2373e677f3b73245795a
    role: target
  - path: data/habitats/host_associated/integumentary_system__2442c03e.yaml
    sha256: 6b9641cba433804d7f4535dda313f84aefd1805f7f36a79c71e0e93dabd78afc
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
  - path: reports/yaml_record_review/20261004T025438Z-apocrine_sweat_gland.md
    sha256: d391baac026f128bd044b20324d952fef505f7616c6e97ff314acfa69d7e121c
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
targets:
- target_id: BTO:0001458
  path: data/habitats/host_associated/apocrine_sweat_gland.yaml
  label: apocrine sweat gland
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
  description: Individual scientific assessment of the exact generated target at the
    captured main revision.
  selection: Resolved identifier and source path in the next sixteen unreviewed records
    in corpus path order; this document assesses only its single target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - BTO:0001458
  exclusions:
  - target: Other habitats and SSSOM/KGX products
    reason: Direct parents are contextual dependencies, not additional completed reviews;
      no export compatibility certification.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/apocrine_sweat_gland.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0001458
  summary: "Actual exit 0 at 2026-10-15T06:06:46Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/apocrine_sweat_gland.yaml"
  scope_note: Individual schema; strict command covers sixteen targets; other named
    native gates have whole-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/anterior_nares.yaml data/habitats/host_associated/anterior_nares__14fc5dcc.yaml
    data/habitats/host_associated/anther.yaml data/habitats/host_associated/anthosphere.yaml
    data/habitats/host_associated/antler.yaml data/habitats/host_associated/aortic_valve.yaml
    data/habitats/host_associated/apocrine_sweat_gland.yaml data/habitats/host_associated/apoeccrine_sweat_glands.yaml
    data/habitats/host_associated/appendix.yaml data/habitats/host_associated/appendix__8f7f5041.yaml
    data/habitats/host_associated/appendix_abscess.yaml data/habitats/host_associated/appressorium.yaml
    data/habitats/host_associated/aquatic_mammal.yaml data/habitats/host_associated/aquatic_plant.yaml
    data/habitats/host_associated/aqueous_humor_of_eyeball.yaml data/habitats/host_associated/area_of_moss_dominated_vegetation.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0001458
  summary: "Actual exit 0 at 2026-10-15T06:07:14Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/anterior_nares.yaml data/habitats/host_associated/anterior_nares__14fc5dcc.yaml\
    \ data/habitats/host_associated/anther.yaml data/habitats/host_associated/anthosphere.yaml\
    \ data/habitats/host_associated/antler.yaml data/habitats/host_associated/aortic_valve.yaml\
    \ data/habitats/host_associated/apocrine_sweat_gland.yaml data/habitats/host_associated/apoeccrine_sweat_glands.yaml\
    \ data/habitats/host_associated/appendix.yaml data/habitats/host_associated/appendix__8f7f5041.yaml\
    \ data/habitats/host_associated/appendix_abscess.yaml data/habitats/host_associated/appressorium.yaml\
    \ data/habitats/host_associated/aquatic_mammal.yaml data/habitats/host_associated/aquatic_plant.yaml\
    \ data/habitats/host_associated/aqueous_humor_of_eyeball.yaml data/habitats/host_associated/area_of_moss_dominated_vegetation.yaml\n\
    Validating 16 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      16\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Individual schema; strict command covers sixteen targets; other named
    native gates have whole-corpus scope.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0001458
  summary: 'Actual exit 0 at 2026-10-15T06:07:22Z. No issues found

    746 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Individual schema; strict command covers sixteen targets; other named
    native gates have whole-corpus scope.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0001458
  summary: "Actual exit 0 at 2026-10-15T06:07:23Z. provenance current: 14 committed\
    \ inventories, 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Individual schema; strict command covers sixteen targets; other named
    native gates have whole-corpus scope.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0001458
  summary: "Actual exit 0 at 2026-10-15T06:07:39Z. expected 3208 records, found 3208\
    \ on disk\n  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces\
    \ exactly from data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Individual schema; strict command covers sixteen targets; other named
    native gates have whole-corpus scope.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0001458
  summary: "Actual exit 0 at 2026-10-15T06:07:43Z. validated 32 causal-graph curation\
    \ file(s) with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Individual schema; strict command covers sixteen targets; other named
    native gates have whole-corpus scope.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0001458
  summary: "Actual exit 0 at 2026-10-15T06:08:00Z. term-request table is current (110\
    \ terms)\n uv run python scripts/build_term_requests.py --check"
  scope_note: Individual schema; strict command covers sixteen targets; other named
    native gates have whole-corpus scope.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0001458
  summary: "Actual exit 0 at 2026-10-15T06:08:42Z. id↔label correspondence summary:\n\
    \          OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Individual schema; strict command covers sixteen targets; other named
    native gates have whole-corpus scope.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/apocrine_sweat_gland.yaml
  locator: Entire YAML
  accessed_at: '2026-10-15T06:26:02Z'
  support: supports
  summary: All target fields and generated history were read.
  snapshot_sha256: 34fca3014974aea71b3163312e34ae64415ee2441e4a2373e677f3b73245795a
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Hosts, anatomy, strict broader hierarchy and input ownership
  accessed_at: '2026-10-15T06:26:02Z'
  support: supports
  summary: Anatomy may identify a microbial site; host taxa are not environment identities;
    every parent must be strictly broader.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate and taxon fields
  accessed_at: '2026-10-15T06:26:02Z'
  support: supports
  summary: Mapping endpoint is the emitted record; association metrics and characteristic
    flags are separate.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: resolve_gold, resolve_bacdive, ingest_prego, apply_decision and apply_curated_definitions
  accessed_at: '2026-10-15T06:26:02Z'
  support: supports
  summary: 'All contributing native resolution routes executed with complete claimant
    and mapping pools; final identifier/status/predicate agree: [{"automatic": {"category":
    null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs":
    [], "grounding_status": "UNGROUNDED", "identifier": "habitatmech:GOLD.f3c6dc4883",
    "mapping_predicate": null, "reviewed": false, "route": "gold_unmatched"}, "final":
    {"category": null, "contributes_grounding": true, "decision": {"category": "",
    "curator": "claude-opus-5", "date": "2026-08-12", "decision": "GROUND", "grounding_status":
    "EXACT", "identifier": "habitatmech:GOLD.f3c6dc4883", "notes": "Leaf label equals
    the BTO label exactly and no other source concept claims it. Path: Host-associated
    > Mammals: Human > Integumentary system > Apocrine sweat glands", "object_id":
    "BTO:0001458", "object_label": "apocrine sweat gland", "relation": "parent", "review_depth":
    "ITEM"}, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT",
    "identifier": "BTO:0001458", "mapping_predicate": "skos:exactMatch", "reviewed":
    true, "route": "curated_ground_from_gold_unmatched"}, "mint": "habitatmech:GOLD.f3c6dc4883",
    "source": "GOLD"}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: ET4
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV rows 2254
  accessed_at: '2026-10-15T06:26:02Z'
  support: supports
  summary: '[{"data": {"biosample_count": "0", "canonical_path": "Host-associated
    > Mammals: Human > Integumentary system > Apocrine sweat glands", "depth": "4",
    "ecosystem": "Host-associated", "ecosystem_category": "Mammals: Human", "ecosystem_subtype":
    "Apocrine sweat glands", "ecosystem_type": "Integumentary system", "gold_node_count":
    "2", "gold_node_ids": "gold.ecosystem:6863|gold.ecosystem:6867", "leaf_label":
    "Apocrine sweat glands", "organism_count": "0", "specific_ecosystem": "", "study_count":
    "0", "total_assertions": "0"}, "row": 2254}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: ET5
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 784,911,912,1002,1003
  accessed_at: '2026-10-15T06:26:02Z'
  support: supports
  summary: '[{"data": {"object": "BTO:0000522", "predicate": "rdfs:subClassOf", "subject":
    "BTO:0001162"}, "row": 784}, {"data": {"object": "BTO:0000431", "predicate": "rdfs:subClassOf",
    "subject": "BTO:0001331"}, "row": 911}, {"data": {"object": "BTO:0000765", "predicate":
    "rdfs:subClassOf", "subject": "BTO:0001331"}, "row": 912}, {"data": {"object":
    "BTO:0001162", "predicate": "rdfs:subClassOf", "subject": "BTO:0001458"}, "row":
    1002}, {"data": {"object": "BTO:0001331", "predicate": "rdfs:subClassOf", "subject":
    "BTO:0001458"}, "row": 1003}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET6
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 1163,1332,1458
  accessed_at: '2026-10-15T06:26:02Z'
  support: supports
  summary: '[{"data": {"definition": "A gland whose discharged secretion contains
    part of the secreting cells.", "deprecated": "", "directly_referenced": "FALSE",
    "label": "apocrine gland", "label_only": "FALSE", "ontology": "BTO", "synonyms":
    "", "term_id": "BTO:0001162"}, "row": 1163}, {"data": {"definition": "A simple
    tubular gland of the skin that secretes perspiration, is widely distributed in
    nearly all parts of the human skin, and consists typically of an epithelial tube
    extending spirally from a minute pore on the surface of the skin into the dermis
    or subcutaneous tissues where it ends in a convoluted tuft.", "deprecated": "",
    "directly_referenced": "FALSE", "label": "sweat gland", "label_only": "FALSE",
    "ontology": "BTO", "synonyms": "", "term_id": "BTO:0001331"}, "row": 1332}, {"data":
    {"definition": "A type of large, branched, specialized sudoriferous gland (glandula
    sudorifera) that empties into the upper portion of a hair follicle instead of
    directly onto the skin surface; found only on certain areas of the body, such
    as around the anus and in the axilla; after puberty they produce a viscous secretion
    that is acted on by bacteria to produce a characteristic acrid odor.", "deprecated":
    "", "directly_referenced": "TRUE", "label": "apocrine sweat gland", "label_only":
    "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0001458"}, "row":
    1458}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: ET7
  kind: database
  reference: curation/decisions.tsv
  locator: TSV rows 1355
  accessed_at: '2026-10-15T06:26:02Z'
  support: supports
  summary: '[{"data": {"category": "", "curator": "claude-opus-5", "date": "2026-08-12",
    "decision": "GROUND", "grounding_status": "EXACT", "identifier": "habitatmech:GOLD.f3c6dc4883",
    "notes": "Leaf label equals the BTO label exactly and no other source concept
    claims it. Path: Host-associated > Mammals: Human > Integumentary system > Apocrine
    sweat glands", "object_id": "BTO:0001458", "object_label": "apocrine sweat gland",
    "relation": "", "review_depth": "ITEM"}, "row": 1355}]'
  snapshot_sha256: ca42d86b6040df1c0c6e6ed36573bb51975a5e8daade262113bce547f1b6fd8b
- evidence_id: EP8
  kind: record_content
  reference: data/habitats/host_associated/integumentary_system__2442c03e.yaml
  locator: Direct-parent identity, definition, parent and source fields
  accessed_at: '2026-10-15T06:26:02Z'
  support: supports
  summary: 'Inspected parent meaning: {"grounding_status": "NARROW", "identifier":
    "habitatmech:GOLD.dc86c8917c", "label": "Integumentary system", "parent_habitats":
    ["UBERON:0002416", "habitatmech:GOLD.cd0b0940e5"], "source_attestations": [{"mapping_predicate":
    "skos:narrowMatch", "notes": "3 GOLD ecosystem node ids share this path; first
    shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id":
    "gold.ecosystem:6113", "source_label": "Integumentary system", "source_path":
    "Host-associated > Mammals: Human > Integumentary system"}]}'
  snapshot_sha256: 6b9641cba433804d7f4535dda313f84aefd1805f7f36a79c71e0e93dabd78afc
- evidence_id: EX1
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001458
  locator: Target term or typed outgoing relations; primary abstract; exact strain
    identity and isolation-source fields as described
  accessed_at: '2026-10-15T06:17:55Z'
  support: supports
  summary: Active authoritative BTO:0001458 apocrine sweat gland; definition and typed
    scope compared with the frozen source and local parent meaning. Obsolete=False.
  snapshot_sha256: 67dfe7863cd687818f61b686a8a654ca3a5bf4019c4febd59174b55d68ba2722
- evidence_id: EX2
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001458/graph
  locator: Target term or typed outgoing relations; primary abstract; exact strain
    identity and isolation-source fields as described
  accessed_at: '2026-10-15T06:17:56Z'
  support: supports
  summary: 'Inspected typed outgoing relations: [{"label": "subClassOf", "source":
    "http://purl.obolibrary.org/obo/BTO_0001458", "target": "http://purl.obolibrary.org/obo/BTO_0001162",
    "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf"}, {"label": "subClassOf",
    "source": "http://purl.obolibrary.org/obo/BTO_0001458", "target": "http://purl.obolibrary.org/obo/BTO_0001331",
    "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf"}]. Partonomy and connectivity
    remain distinct from subclassing.'
  snapshot_sha256: 9c559be220deb01317232244aa665f0b87d248dd24fc79e7d382a047c808b2b7
- evidence_id: EX3
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001162
  locator: Target term or typed outgoing relations; primary abstract; exact strain
    identity and isolation-source fields as described
  accessed_at: '2026-10-15T06:17:52Z'
  support: supports
  summary: Active authoritative BTO:0001162 apocrine gland; definition and typed scope
    compared with the frozen source and local parent meaning. Obsolete=False.
  snapshot_sha256: aa364e8f51109cb705f918eaf82a5bcac430a5f6c75091e31858188bca948688
- evidence_id: EX4
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001331
  locator: Target term or typed outgoing relations; primary abstract; exact strain
    identity and isolation-source fields as described
  accessed_at: '2026-10-15T06:17:54Z'
  support: supports
  summary: Active authoritative BTO:0001331 sweat gland; definition and typed scope
    compared with the frozen source and local parent meaning. Obsolete=False.
  snapshot_sha256: 1083ade599d9e63b26f2b9e14471ae6e2194b8ea7affaac0a3cc9d24f895bced
- evidence_id: EX5
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002416
  locator: Target term or typed outgoing relations; primary abstract; exact strain
    identity and isolation-source fields as described
  accessed_at: '2026-10-15T06:21:07Z'
  support: supports
  summary: Active authoritative UBERON:0002416 integumental system; definition and
    typed scope compared with the frozen source and local parent meaning. Obsolete=False.
  snapshot_sha256: b99dd38824896b19176431aaa2cc09f4b344a5fa22c303ec9193f3c9f1694d8a
- evidence_id: ESEARCH
  kind: search
  reference: Local scientific-input and saved-review traversal
  locator: rg --no-ignore --hidden -l -F -e BTO:0001458 -e 'apocrine sweat gland'
    -e apocrine_sweat_gland -e habitatmech:GOLD.f3c6dc4883 curation history research
    reports data/raw build reviews
  accessed_at: '2026-10-15T06:17:29Z'
  support: context_only
  summary: Ignored-inclusive source ID/label/slug search plus exact parsed table matches
    and complete structured-target traversal. No structured predecessor targets this
    record.
  search_scope: Hidden and ignored files included under curation, history, research,
    reports, data/raw, build and reviews; all structured review.yaml files traversed
    irrespective of gitignore. Not a global absence or original-member claim.
assessments:
- assessment_id: A1
  area: schema
  topic: Native structural and reproduction checks
  outcome: supported
  summary: 'Recorded gates passed: schema, strict sixteen-target validation, 746 history
    records, exact 3,208-record reproduction, 32 causal graphs and 110 term requests.
    These are not scientific proof.'
  target_ids:
  - BTO:0001458
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Habitat identity and full source scope
  outcome: concern
  summary: The BTO apocrine sweat-gland identity and both gland superclasses are supported.
    The separate GOLD integumentary-system contribution is an invalid whole-system
    superclass.
  target_ids:
  - BTO:0001458
  evidence_ids:
  - E1
  - ERULE
  - ESEED
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
- assessment_id: A3
  area: quantity
  topic: Source counts, units and retained taxon observations
  outcome: supported
  summary: 'Exact contributing source rows, emitted counts/units, taxon labels/ranks
    and source scores were compared. [{"source": "GOLD", "count": 0, "unit": "ORGANISM"}].
    0 retained taxon IDs match current NCBI names. Zero counts are omitted, and later
    bulk biosamples/studies are not added to frozen ORGANISM counts. Source pools
    are not prevalence denominators.'
  target_ids:
  - BTO:0001458
  evidence_ids:
  - E1
  - ESEED
  - ESEARCH
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
- assessment_id: A4
  area: completeness
  topic: Parameters, causal claims and optional evidence
  outcome: not_applicable
  summary: No target causal graph, environmental-parameter, mechanism or characteristic-presence
    assertion requires expansion. No absent optional field is populated for coverage.
    Parent-record mechanisms are not inherited as evidence for this target.
  target_ids:
  - BTO:0001458
  evidence_ids:
  - E1
findings:
- finding_id: F1
  issue_key: apocrine-sweat-gland-source-parent
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Source context is asserted as a broader habitat
  description: A sweat gland is not a whole integumentary system. Both BTO gland superclasses
    remain valid. Exclude only the immediate GOLD contribution habitatmech:GOLD.dc86c8917c
    with exact source-path and expected-parent guards; preserve independent parents
    and verbatim source provenance.
  target_ids:
  - BTO:0001458
  field_paths:
  - parent_habitats
  evidence_ids:
  - E1
  - ERULE
  - ESEED
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained curation input or generator
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Material semantic claim unsupported by the inspected source
    scope; deterministic validity is insufficient.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1337
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - BTO:0001458
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained curation input or generator
  description: A sweat gland is not a whole integumentary system. Both BTO gland superclasses
    remain valid. Exclude only the immediate GOLD contribution habitatmech:GOLD.dc86c8917c
    with exact source-path and expected-parent guards; preserve independent parents
    and verbatim source provenance. Use maintained owners, not generated YAML edits.
  generator: just seed; inspect just seed-canary; just seed-apply; supported semantic
    map, term-request, site and redirect regeneration when inputs change
  acceptance_checks:
  - Regress the exact target and preserve independently valid source identities, counts/units,
    taxa, status and parents.
  - Append session history; run strict schema, history, provenance, reproduction,
    configured label and full QC gates.
  - Save a successor with exact finding lineage; do not rewrite this observation or
    claim broader export conformance.
limitations:
- Frozen source-bin membership is not a complete audit of original specimens. Only
  the exact external source witnesses described here were independently inspected.
- Taxon associations are observational. PREGO score and BacDive strain counts do not
  prove prevalence, mechanism or characteristic presence.
- The configured label gate skipped 2,061 no-adapter pairs. Ontology semantics and
  retained taxon identities were separately assessed.
- The full archive and just qc are publication gates to run after saving; these pre-fix
  observations do not claim their future results.
- Historical reports and history prose are search leads, not independent approval.
  Historical neighboring claims and every legacy citation were not re-reviewed.
- 'iModulonDB is not applicable: these targets assert no gene, regulator or transcriptomic
  mechanism. No paid research was used.'
notes:
- All captured local input bytes were rechecked unchanged against the working tree
  and exact Git blobs.
- Ignored-inclusive structured archive traversal found no earlier structured review
  targeting this record. Historical reports and GitHub issues are retained as contextual
  leads.
- This is a pre-fix observation; separately authorized curation requires new successor
  observations.
tags:
- individual-scientific-review
- host-associated
```
