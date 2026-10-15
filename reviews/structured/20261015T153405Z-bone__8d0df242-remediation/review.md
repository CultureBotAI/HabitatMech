# Remediation review: Bone (habitatmech:GOLD.28cfbd7dee)

- Review: 20261015T153405Z-bone__8d0df242-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T15:16:38Z
- Finished UTC: 2026-10-15T15:34:05Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Resolved the exact context-parent finding by removing only habitatmech:GOLD.092eae5cd7. Remaining parents are BTO:0000140. All source identities, counts, units, taxa, mapping predicates and NARROW/SEEDED status are unchanged. The retained-mint mapping-endpoint finding remains open under #1398.

## Scope And Provenance

Full current target re-read and disposition of each exact predecessor finding.

Selection: One of thirteen parent-edge corrections in the twenty-one-record blood/bone publication cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 073e706698b1f36f64561c13aebece4349765bad.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.28cfbd7dee | data/habitats/host_associated/bone__8d0df242.yaml | generated | Bone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate data/habitats/host_associated/bone__8d0df242.yaml | passed | True | habitatmech:GOLD.28cfbd7dee | Executed 2026-10-15T15:09:09Z through 2026-10-15T15:09:13Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/bone__8d0df242.yaml |
| just validate-strict data/habitats/host_associated/blood.yaml data/habitats/host_associated/blood__070ce7aa.yaml data/habitats/host_associated/blood__5ca8064f.yaml data/habitats/host_associated/blood__5ef3f2f4.yaml data/habitats/host_associated/blood__c1b484fe.yaml data/habitats/host_associated/blood__d6f5ae05.yaml data/habitats/host_associated/blood_plasma.yaml data/habitats/host_associated/blood_plasma__00b70c6a.yaml data/habitats/host_associated/blood_serum.yaml data/habitats/host_associated/blood_vessel.yaml data/habitats/host_associated/bone.yaml data/habitats/host_associated/bone__169c3d9e.yaml data/habitats/host_associated/bone__234001be.yaml data/habitats/host_associated/bone__71064238.yaml data/habitats/host_associated/bone__8430e16e.yaml data/habitats/host_associated/bone__8d0df242.yaml data/habitats/host_associated/bone__b47efce2.yaml data/habitats/host_associated/bone_element.yaml data/habitats/host_associated/bone_marrow.yaml data/habitats/host_associated/bone_marrow__9387f1a6.yaml data/habitats/host_associated/bone_marrow__c1fc5dec.yaml | passed | True | habitatmech:GOLD.28cfbd7dee | Executed 2026-10-15T15:09:28Z through 2026-10-15T15:09:39Z. uv run python scripts/validate_strict.py data/habitats/host_associated/blood.yaml data/habitats/host_associated/blood__070ce7aa.yaml data/habitats/host_associated/blood__5ca8064f.yaml data/habitats/host_associated/blood__5ef3f2f4.yaml data/habitats/host_associated/blood__c1b484fe.yaml data/habitats/host_associated/blood__d6f5ae05.yaml data/habitats/host_associated/blood_plasma.yaml data/habitats/host_associated/blood_plasma__00b70c6a.yaml data/habitats/host_associated/blood_serum.yaml data/habitats/host_associated/blood_vessel.yaml data/habitats/host_associated/bone.yaml data/habitats/host_associated/bone__169c3d9e.yaml data/habitats/host_associated/bone__234001be.yaml data/habitats/host_associated/bone__71064238.yaml data/habitats/host_associated/bone__8430e16e.yaml data/habitats/host_associated/bone__8d0df242.yaml data/habitats/host_associated/bone__b47efce2.yaml data/habitats/host_associated/bone_element.yaml data/habitats/host_associated/bone_marrow.yaml data/habitats/host_associated/bone_marrow__9387f1a6.yaml data/habitats/host_associated/bone_marrow__c1fc5dec.yaml<br>Validating 21 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      21<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| just validate-history | passed | True | habitatmech:GOLD.28cfbd7dee | Executed 2026-10-15T15:09:39Z through 2026-10-15T15:09:49Z. No issues found<br>814 history record(s) valid against src/habitatmech/schema/history.yaml |
| just provenance-check | passed | True | habitatmech:GOLD.28cfbd7dee | Executed 2026-10-15T15:09:49Z through 2026-10-15T15:09:50Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| just verify-corpus | passed | True | habitatmech:GOLD.28cfbd7dee | Executed 2026-10-15T15:09:50Z through 2026-10-15T15:10:10Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| just validate-causal-all | passed | True | habitatmech:GOLD.28cfbd7dee | Executed 2026-10-15T15:10:10Z through 2026-10-15T15:10:15Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| just term-requests-check | passed | True | habitatmech:GOLD.28cfbd7dee | Executed 2026-10-15T15:10:15Z through 2026-10-15T15:10:37Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| just validate-products | passed | True | habitatmech:GOLD.28cfbd7dee | Executed 2026-10-15T15:10:37Z through 2026-10-15T15:11:53Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python -m pytest -q tests/test_blood_bone_review_repairs.py | passed | True | habitatmech:GOLD.28cfbd7dee | Executed 2026-10-15T15:11:54Z through 2026-10-15T15:12:03Z. ..                                                                       [100%]<br>2 passed in 8.36s |
| git diff --check b558fd561286d1fe3ba133784776f7be1f9f49fb | passed | True | habitatmech:GOLD.28cfbd7dee | Executed 2026-10-15T15:12:03Z through 2026-10-15T15:12:04Z.  |
| Exact-revision full QC and structured archive contract | passed | True | habitatmech:GOLD.28cfbd7dee | Full native QC succeeded at captured input revision 073e706698b1f36f64561c13aebece4349765bad; verified 2026-10-15T15:32:39Z. https://github.com/CultureBotAI/HabitatMech/actions/runs/38758835048 |

## Scientific And Domain Assessments

### Scoped correction and preservation

consistency: supported. Targets: habitatmech:GOLD.28cfbd7dee.

Resolved the exact context-parent finding by removing only habitatmech:GOLD.092eae5cd7. Remaining parents are BTO:0000140. All source identities, counts, units, taxa, mapping predicates and NARROW/SEEDED status are unchanged. The retained-mint mapping-endpoint finding remains open under #1398.

### Retained identity and true genera

identity: supported. Targets: habitatmech:GOLD.28cfbd7dee.

Full target and typed authority evidence were reassessed. The same site identity and source semantics remain; containing-anatomy edges are removed without replacing them with unsupported claims.

### Remaining mapping contract

representation: concern. Targets: habitatmech:GOLD.28cfbd7dee.

The target narrowMatch witness remains open under #1398.

## Findings

### F1: Containing anatomy is not a broader habitat class

major / resolved / confirmed; issue key: bone--8d0df242-context-parent.

The predecessor reported unsupported context parents habitatmech:GOLD.092eae5cd7. These contributions are now excluded. The retained parents are BTO:0000140. The complete original observation remains available in the linked immutable predecessor; its historical issue-state wording is not a claim about current issue status.

Disposition: Exact source-path and expected-parent exclusions remove only the unsupported context contributions. Independent ontology ancestry, identities, source observations, mapping predicates and native status remain unchanged; focused counterfactual and exact-revision full QC passed.

### F2: Narrow predicate uses an undeclared ontology-parent endpoint

major / open / confirmed; issue key: bone--8d0df242-mapping-endpoint-contract.

Reassessed after the parent repair: the source mint and narrowMatch output are unchanged. The original source-to-record versus record-to-ontology-parent contract finding remains open under #1398. Parent repair does not resolve or approve SSSOM/KGX mapping semantics.

## Recommended Actions And Acceptance Checks

### ACT2

The executed gold_narrower_than_leaf_match route retains the source mint yet emits narrowMatch relative to an ontology parent, while SourceAttestation describes a source-to-record mapping. Reconcile producer, schema and consumers under #1398; do not relabel an anatomically valid broader parent as an exact source identity, and do not claim SKOS formally forbids self-links. No repair is performed by this review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history. Do not change source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000140/graph; BTO_0000140-graph.json | context_only | Typed outgoing relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0000140", "target": "http://purl.obolibrary.org/obo/BTO_0000421", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/BTO_0000140", "target": "http://purl.obolibrary.org/obo/BTO_0001486", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000140; BTO_0000140.json | context_only | Inspected current ID, label, active status and definition for scope; {"obo_id": "BTO:0000140", "label": "bone", "is_obsolete": false} |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001434/graph; UBERON_0001434-graph.json | context_only | Typed outgoing relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001434", "target": "http://purl.obolibrary.org/obo/UBERON_0011216", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001434", "target": "http://purl.obolibrary.org/obo/UBERON_0000066", "uri": "http://purl.obolibrary.org/obo/RO_0002492", "label": "existence ends during"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001434", "target": "http://purl.obolibrary.org/obo/UBERON_0002204", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001434", "target": "http://purl.obolibrary.org/obo/UBERON_0004288", "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001434", "target": "http://purl.obolibrary.org/obo/UBERON_0004770", "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001434; UBERON_0001434.json | context_only | Inspected current ID, label, active status and definition for scope; {"obo_id": "UBERON:0001434", "label": "skeletal system", "is_obsolete": false} |
| EAFTER | data/habitats/host_associated/bone__8d0df242.yaml; Entire regenerated target | supports | {"identifier": "habitatmech:GOLD.28cfbd7dee", "label": "Bone", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats": ["BTO:0000140"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6373", "source_label": "Bone", "source_path": "Host-associated &gt; Mammals &gt; Skeletal system &gt; Bone", "mapping_predicate": "skos:narrowMatch", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NARROW."}, {"timestamp": "2026-10-15T00:00:00Z", "curator": "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.092eae5cd7 for habitatmech:GOLD.28cfbd7dee (Host-associated &gt; Mammals &gt; Skeletal system &gt; Bone). Review https://github.com/CultureBotAI/HabitatMech/issues/2186. Bone is part of a skeletal system, not a subtype of the whole skeletal system. Exclude only this exact source-path/expected-parent contribution; preserve independent ontology genera, source observations and native status."}]} |
| EPREV | reviews/structured/20261015T145139Z-bone__8d0df242-record/review.yaml; Exact predecessor, all findings | supports | The original observation is retained unchanged; current findings explicitly reconcile it. |
| ETEST | tests/test_blood_bone_review_repairs.py; Exact exclusions, actual URL rendering and full-corpus counterfactual | supports | Regression proves that removing the sixteen exclusions changes exactly thirteen records, solely in parent lists and appended exclusion history. Raw source assertions and all unrelated records remain identical. |
| ERULE | docs/CURATION.md; Strict ancestry | supports | A containing anatomical structure is not a broader habitat class. |
| EINPUT | curation/gold_parent_exclusions.tsv; Exact keyed rows 3 | supports | [[3, "habitatmech:GOLD.28cfbd7dee\tHost-associated &gt; Mammals &gt; Skeletal system &gt; Bone\thabitatmech:GOLD.092eae5cd7\tcodex-gpt-5\t2026-10-15\tReview https://github.com/CultureBotAI/HabitatMech/issues/2186. Bone is part of a skeletal system, not a subtype of the whole skeletal system. Exclude only this exact source-path/expected-parent contribution; preserve independent ontology genera, source observations and native status."]] |

## Limits And Additional Notes

- Same-agent review, not independent approval. The original specimen/pair-level evidence limitations remain; only supported context-parent findings are repaired.
- Shared mapping contract #1398 remains open; this review does not certify current kg-microbe SSSOM/KGX conformance.
- Configured label correspondence retains 2,061 no-adapter skips. No causal or characteristic-presence claim is added. iModulonDB is not applicable.
- Final-head validation of this new successor is a subsequent publication gate; full QC at the exact scientific input revision has passed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T153405Z-bone__8d0df242-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: Bone (habitatmech:GOLD.28cfbd7dee)'
started_at: '2026-10-15T15:16:38Z'
finished_at: '2026-10-15T15:34:05Z'
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
summary: 'Resolved the exact context-parent finding by removing only habitatmech:GOLD.092eae5cd7.
  Remaining parents are BTO:0000140. All source identities, counts, units, taxa, mapping
  predicates and NARROW/SEEDED status are unchanged. The retained-mint mapping-endpoint
  finding remains open under #1398.'
source:
  git_revision: 073e706698b1f36f64561c13aebece4349765bad
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
  - path: data/habitats/host_associated/bone__8d0df242.yaml
    sha256: a1d77056f4700b90e5310da75ac58796fd48fa350608756b9cd59d959b273484
    role: target
  - path: data/habitats/host_associated/skeletal_system__e5059bff.yaml
    sha256: e9e371b0df559a96f2074c2a9ca2ee74a4fe473f19d5d3436732d7079c97f61e
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
  - path: history/mappings/blood_bone_review/2026-10-15T150651Z-codex-gpt-5-902c84.yaml
    sha256: 9a13ca33ce519181d8120e03c84c081572cb4407db4d835e065da99cf46e6fc1
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260922T041554Z-bone__8d0df242.md
    sha256: 7ecc29835e05ba2fff837043e3d8dc1dd1414e8de570e0549e99b07bf7273415
    role: context
  - path: reviews/structured/20261015T145139Z-bone__8d0df242-record/review.yaml
    sha256: af877c43d19c6b252e5b8293cc1ff15c7b21664ea3d10324a4245682139c35bc
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
  - path: tests/test_blood_bone_review_repairs.py
    sha256: 80b9d073ace3ec124366cee4906976775038b3c35833b1adad2a709c1dc3a2ee
    role: context
targets:
- target_id: habitatmech:GOLD.28cfbd7dee
  path: data/habitats/host_associated/bone__8d0df242.yaml
  label: Bone
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
  description: Full current target re-read and disposition of each exact predecessor
    finding.
  selection: One of thirteen parent-edge corrections in the twenty-one-record blood/bone
    publication cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.28cfbd7dee
  exclusions:
  - target: Other records and SSSOM/KGX contract
    reason: 'Shared #1398 remains unresolved; other original cohort findings are not
      closed by this observation.'
checks:
- check_id: C8
  name: just validate data/habitats/host_associated/bone__8d0df242.yaml
  status: passed
  required: true
  command: just validate data/habitats/host_associated/bone__8d0df242.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.28cfbd7dee
  summary: "Executed 2026-10-15T15:09:09Z through 2026-10-15T15:09:13Z. No issues\
    \ found\n uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class\
    \ HabitatRecord data/habitats/host_associated/bone__8d0df242.yaml"
  scope_note: Ordinary schema for thirteen changed targets, strict for all 21, focused
    regression and full-corpus native gates.
- check_id: C13
  name: just validate-strict data/habitats/host_associated/blood.yaml data/habitats/host_associated/blood__070ce7aa.yaml
    data/habitats/host_associated/blood__5ca8064f.yaml data/habitats/host_associated/blood__5ef3f2f4.yaml
    data/habitats/host_associated/blood__c1b484fe.yaml data/habitats/host_associated/blood__d6f5ae05.yaml
    data/habitats/host_associated/blood_plasma.yaml data/habitats/host_associated/blood_plasma__00b70c6a.yaml
    data/habitats/host_associated/blood_serum.yaml data/habitats/host_associated/blood_vessel.yaml
    data/habitats/host_associated/bone.yaml data/habitats/host_associated/bone__169c3d9e.yaml
    data/habitats/host_associated/bone__234001be.yaml data/habitats/host_associated/bone__71064238.yaml
    data/habitats/host_associated/bone__8430e16e.yaml data/habitats/host_associated/bone__8d0df242.yaml
    data/habitats/host_associated/bone__b47efce2.yaml data/habitats/host_associated/bone_element.yaml
    data/habitats/host_associated/bone_marrow.yaml data/habitats/host_associated/bone_marrow__9387f1a6.yaml
    data/habitats/host_associated/bone_marrow__c1fc5dec.yaml
  status: passed
  required: true
  command: just validate-strict data/habitats/host_associated/blood.yaml data/habitats/host_associated/blood__070ce7aa.yaml
    data/habitats/host_associated/blood__5ca8064f.yaml data/habitats/host_associated/blood__5ef3f2f4.yaml
    data/habitats/host_associated/blood__c1b484fe.yaml data/habitats/host_associated/blood__d6f5ae05.yaml
    data/habitats/host_associated/blood_plasma.yaml data/habitats/host_associated/blood_plasma__00b70c6a.yaml
    data/habitats/host_associated/blood_serum.yaml data/habitats/host_associated/blood_vessel.yaml
    data/habitats/host_associated/bone.yaml data/habitats/host_associated/bone__169c3d9e.yaml
    data/habitats/host_associated/bone__234001be.yaml data/habitats/host_associated/bone__71064238.yaml
    data/habitats/host_associated/bone__8430e16e.yaml data/habitats/host_associated/bone__8d0df242.yaml
    data/habitats/host_associated/bone__b47efce2.yaml data/habitats/host_associated/bone_element.yaml
    data/habitats/host_associated/bone_marrow.yaml data/habitats/host_associated/bone_marrow__9387f1a6.yaml
    data/habitats/host_associated/bone_marrow__c1fc5dec.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.28cfbd7dee
  summary: "Executed 2026-10-15T15:09:28Z through 2026-10-15T15:09:39Z. uv run python\
    \ scripts/validate_strict.py data/habitats/host_associated/blood.yaml data/habitats/host_associated/blood__070ce7aa.yaml\
    \ data/habitats/host_associated/blood__5ca8064f.yaml data/habitats/host_associated/blood__5ef3f2f4.yaml\
    \ data/habitats/host_associated/blood__c1b484fe.yaml data/habitats/host_associated/blood__d6f5ae05.yaml\
    \ data/habitats/host_associated/blood_plasma.yaml data/habitats/host_associated/blood_plasma__00b70c6a.yaml\
    \ data/habitats/host_associated/blood_serum.yaml data/habitats/host_associated/blood_vessel.yaml\
    \ data/habitats/host_associated/bone.yaml data/habitats/host_associated/bone__169c3d9e.yaml\
    \ data/habitats/host_associated/bone__234001be.yaml data/habitats/host_associated/bone__71064238.yaml\
    \ data/habitats/host_associated/bone__8430e16e.yaml data/habitats/host_associated/bone__8d0df242.yaml\
    \ data/habitats/host_associated/bone__b47efce2.yaml data/habitats/host_associated/bone_element.yaml\
    \ data/habitats/host_associated/bone_marrow.yaml data/habitats/host_associated/bone_marrow__9387f1a6.yaml\
    \ data/habitats/host_associated/bone_marrow__c1fc5dec.yaml\nValidating 21 files\
    \ with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      21\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Ordinary schema for thirteen changed targets, strict for all 21, focused
    regression and full-corpus native gates.
- check_id: C14
  name: just validate-history
  status: passed
  required: true
  command: just validate-history
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.28cfbd7dee
  summary: 'Executed 2026-10-15T15:09:39Z through 2026-10-15T15:09:49Z. No issues
    found

    814 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Ordinary schema for thirteen changed targets, strict for all 21, focused
    regression and full-corpus native gates.
- check_id: C15
  name: just provenance-check
  status: passed
  required: true
  command: just provenance-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.28cfbd7dee
  summary: "Executed 2026-10-15T15:09:49Z through 2026-10-15T15:09:50Z. provenance\
    \ current: 14 committed inventories, 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Ordinary schema for thirteen changed targets, strict for all 21, focused
    regression and full-corpus native gates.
- check_id: C16
  name: just verify-corpus
  status: passed
  required: true
  command: just verify-corpus
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.28cfbd7dee
  summary: "Executed 2026-10-15T15:09:50Z through 2026-10-15T15:10:10Z. expected 3208\
    \ records, found 3208 on disk\n  missing:   0\n  extra:     0\n  differing: 0\n\
    \ncorpus reproduces exactly from data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Ordinary schema for thirteen changed targets, strict for all 21, focused
    regression and full-corpus native gates.
- check_id: C17
  name: just validate-causal-all
  status: passed
  required: true
  command: just validate-causal-all
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.28cfbd7dee
  summary: "Executed 2026-10-15T15:10:10Z through 2026-10-15T15:10:15Z. validated\
    \ 32 causal-graph curation file(s) with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Ordinary schema for thirteen changed targets, strict for all 21, focused
    regression and full-corpus native gates.
- check_id: C18
  name: just term-requests-check
  status: passed
  required: true
  command: just term-requests-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.28cfbd7dee
  summary: "Executed 2026-10-15T15:10:15Z through 2026-10-15T15:10:37Z. term-request\
    \ table is current (110 terms)\n uv run python scripts/build_term_requests.py\
    \ --check"
  scope_note: Ordinary schema for thirteen changed targets, strict for all 21, focused
    regression and full-corpus native gates.
- check_id: C19
  name: just validate-products
  status: passed
  required: true
  command: just validate-products
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.28cfbd7dee
  summary: "Executed 2026-10-15T15:10:37Z through 2026-10-15T15:11:53Z. id↔label correspondence\
    \ summary:\n          OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n        \
    \  OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n\
    \ uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Ordinary schema for thirteen changed targets, strict for all 21, focused
    regression and full-corpus native gates.
- check_id: C20
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_blood_bone_review_repairs.py
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_blood_bone_review_repairs.py
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.28cfbd7dee
  summary: 'Executed 2026-10-15T15:11:54Z through 2026-10-15T15:12:03Z. ..                                                                       [100%]

    2 passed in 8.36s'
  scope_note: Ordinary schema for thirteen changed targets, strict for all 21, focused
    regression and full-corpus native gates.
- check_id: C21
  name: git diff --check b558fd561286d1fe3ba133784776f7be1f9f49fb
  status: passed
  required: true
  command: git diff --check b558fd561286d1fe3ba133784776f7be1f9f49fb
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.28cfbd7dee
  summary: 'Executed 2026-10-15T15:12:03Z through 2026-10-15T15:12:04Z. '
  scope_note: Ordinary schema for thirteen changed targets, strict for all 21, focused
    regression and full-corpus native gates.
- check_id: CCI
  name: Exact-revision full QC and structured archive contract
  status: passed
  required: true
  command: gh run view 38758835048 --json status,conclusion,headSha,url,jobs
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.28cfbd7dee
  summary: Full native QC succeeded at captured input revision 073e706698b1f36f64561c13aebece4349765bad;
    verified 2026-10-15T15:32:39Z. https://github.com/CultureBotAI/HabitatMech/actions/runs/38758835048
  scope_note: This new immutable successor also requires final-head validation before
    merge.
evidence:
- evidence_id: EX1
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000140/graph
  locator: BTO_0000140-graph.json
  accessed_at: '2026-10-15T14:36:17Z'
  support: context_only
  summary: 'Typed outgoing relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0000140",
    "target": "http://purl.obolibrary.org/obo/BTO_0000421", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/BTO_0000140",
    "target": "http://purl.obolibrary.org/obo/BTO_0001486", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 14ec2b72ca358eed8ca91634929743f2dfff7491c094c0eeab5491e982c7ca35
- evidence_id: EX2
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000140
  locator: BTO_0000140.json
  accessed_at: '2026-10-15T14:36:16Z'
  support: context_only
  summary: 'Inspected current ID, label, active status and definition for scope; {"obo_id":
    "BTO:0000140", "label": "bone", "is_obsolete": false}'
  snapshot_sha256: 75f23eb9636f74b74c10224f169aab677ce7cdba087ca4d5e51fba9a875cff6f
- evidence_id: EX3
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001434/graph
  locator: UBERON_0001434-graph.json
  accessed_at: '2026-10-15T14:36:28Z'
  support: context_only
  summary: 'Typed outgoing relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001434",
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
  accessed_at: '2026-10-15T14:36:27Z'
  support: context_only
  summary: 'Inspected current ID, label, active status and definition for scope; {"obo_id":
    "UBERON:0001434", "label": "skeletal system", "is_obsolete": false}'
  snapshot_sha256: 0965f957490fb66ad6f4744d8fe4694bf133e2f156a67805e485800bc53e616e
- evidence_id: EAFTER
  kind: record_content
  reference: data/habitats/host_associated/bone__8d0df242.yaml
  locator: Entire regenerated target
  accessed_at: '2026-10-15T15:34:05Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.28cfbd7dee", "label": "Bone", "habitat_category":
    "HOST_ASSOCIATED", "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats":
    ["BTO:0000140"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6373",
    "source_label": "Bone", "source_path": "Host-associated > Mammals > Skeletal system
    > Bone", "mapping_predicate": "skos:narrowMatch", "notes": "2 GOLD ecosystem node
    ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history":
    [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action":
    "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested
    by GOLD. Grounding: NARROW."}, {"timestamp": "2026-10-15T00:00:00Z", "curator":
    "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path
    parent contribution habitatmech:GOLD.092eae5cd7 for habitatmech:GOLD.28cfbd7dee
    (Host-associated > Mammals > Skeletal system > Bone). Review https://github.com/CultureBotAI/HabitatMech/issues/2186.
    Bone is part of a skeletal system, not a subtype of the whole skeletal system.
    Exclude only this exact source-path/expected-parent contribution; preserve independent
    ontology genera, source observations and native status."}]}'
  snapshot_sha256: a1d77056f4700b90e5310da75ac58796fd48fa350608756b9cd59d959b273484
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261015T145139Z-bone__8d0df242-record/review.yaml
  locator: Exact predecessor, all findings
  accessed_at: '2026-10-15T15:34:05Z'
  support: supports
  summary: The original observation is retained unchanged; current findings explicitly
    reconcile it.
  snapshot_sha256: af877c43d19c6b252e5b8293cc1ff15c7b21664ea3d10324a4245682139c35bc
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_blood_bone_review_repairs.py
  locator: Exact exclusions, actual URL rendering and full-corpus counterfactual
  accessed_at: '2026-10-15T15:34:05Z'
  support: supports
  summary: Regression proves that removing the sixteen exclusions changes exactly
    thirteen records, solely in parent lists and appended exclusion history. Raw source
    assertions and all unrelated records remain identical.
  snapshot_sha256: 80b9d073ace3ec124366cee4906976775038b3c35833b1adad2a709c1dc3a2ee
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Strict ancestry
  accessed_at: '2026-10-15T15:34:05Z'
  support: supports
  summary: A containing anatomical structure is not a broader habitat class.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: EINPUT
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: Exact keyed rows 3
  accessed_at: '2026-10-15T15:34:05Z'
  support: supports
  summary: '[[3, "habitatmech:GOLD.28cfbd7dee\tHost-associated > Mammals > Skeletal
    system > Bone\thabitatmech:GOLD.092eae5cd7\tcodex-gpt-5\t2026-10-15\tReview https://github.com/CultureBotAI/HabitatMech/issues/2186.
    Bone is part of a skeletal system, not a subtype of the whole skeletal system.
    Exclude only this exact source-path/expected-parent contribution; preserve independent
    ontology genera, source observations and native status."]]'
  snapshot_sha256: 903fc125adcd84df9fa99a4fae71b30d4a3541efc48eeff3cd49b94e866a5056
assessments:
- assessment_id: A1
  area: consistency
  topic: Scoped correction and preservation
  outcome: supported
  summary: 'Resolved the exact context-parent finding by removing only habitatmech:GOLD.092eae5cd7.
    Remaining parents are BTO:0000140. All source identities, counts, units, taxa,
    mapping predicates and NARROW/SEEDED status are unchanged. The retained-mint mapping-endpoint
    finding remains open under #1398.'
  target_ids:
  - habitatmech:GOLD.28cfbd7dee
  evidence_ids:
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EINPUT
  - EX1
  - EX2
  - EX3
  - EX4
- assessment_id: A2
  area: identity
  topic: Retained identity and true genera
  outcome: supported
  summary: Full target and typed authority evidence were reassessed. The same site
    identity and source semantics remain; containing-anatomy edges are removed without
    replacing them with unsupported claims.
  target_ids:
  - habitatmech:GOLD.28cfbd7dee
  evidence_ids:
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EINPUT
  - EX1
  - EX2
  - EX3
  - EX4
- assessment_id: A3
  area: representation
  topic: Remaining mapping contract
  outcome: concern
  summary: 'The target narrowMatch witness remains open under #1398.'
  target_ids:
  - habitatmech:GOLD.28cfbd7dee
  evidence_ids:
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EINPUT
  - EX1
  - EX2
  - EX3
  - EX4
findings:
- finding_id: F1
  issue_key: bone--8d0df242-context-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Containing anatomy is not a broader habitat class
  description: The predecessor reported unsupported context parents habitatmech:GOLD.092eae5cd7.
    These contributions are now excluded. The retained parents are BTO:0000140. The
    complete original observation remains available in the linked immutable predecessor;
    its historical issue-state wording is not a claim about current issue status.
  target_ids:
  - habitatmech:GOLD.28cfbd7dee
  field_paths:
  - parent_habitats
  evidence_ids:
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EINPUT
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
  normalization_reason: Materially unsupported semantic or source-evidence claim;
    deterministic validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2186
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261015T145139Z-bone__8d0df242-record
    finding_id: F1
  disposition_reason: Exact source-path and expected-parent exclusions remove only
    the unsupported context contributions. Independent ontology ancestry, identities,
    source observations, mapping predicates and native status remain unchanged; focused
    counterfactual and exact-revision full QC passed.
- finding_id: F2
  issue_key: bone--8d0df242-mapping-endpoint-contract
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Narrow predicate uses an undeclared ontology-parent endpoint
  description: 'Reassessed after the parent repair: the source mint and narrowMatch
    output are unchanged. The original source-to-record versus record-to-ontology-parent
    contract finding remains open under #1398. Parent repair does not resolve or approve
    SSSOM/KGX mapping semantics.'
  target_ids:
  - habitatmech:GOLD.28cfbd7dee
  field_paths:
  - source_attestations[0].mapping_predicate
  evidence_ids:
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EINPUT
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
  normalization_reason: Materially unsupported semantic or source-evidence claim;
    deterministic validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261015T145139Z-bone__8d0df242-record
    finding_id: F2
actions:
- action_id: ACT2
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.28cfbd7dee
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  description: 'The executed gold_narrower_than_leaf_match route retains the source
    mint yet emits narrowMatch relative to an ontology parent, while SourceAttestation
    describes a source-to-record mapping. Reconcile producer, schema and consumers
    under #1398; do not relabel an anatomically valid broader parent as an exact source
    identity, and do not claim SKOS formally forbids self-links. No repair is performed
    by this review.'
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
- Same-agent review, not independent approval. The original specimen/pair-level evidence
  limitations remain; only supported context-parent findings are repaired.
- 'Shared mapping contract #1398 remains open; this review does not certify current
  kg-microbe SSSOM/KGX conformance.'
- Configured label correspondence retains 2,061 no-adapter skips. No causal or characteristic-presence
  claim is added. iModulonDB is not applicable.
- Final-head validation of this new successor is a subsequent publication gate; full
  QC at the exact scientific input revision has passed.
notes: []
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261015T145139Z-bone__8d0df242-record
  relationship: Exact predecessor; every original finding is reconciled with unchanged
    affected-target scope.
```
