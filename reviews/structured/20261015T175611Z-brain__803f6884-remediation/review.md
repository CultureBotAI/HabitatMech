# Remediation review: Brain (habitatmech:GOLD.6bdd76cda3)

- Review: 20261015T175611Z-brain__803f6884-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T17:25:38Z
- Finished UTC: 2026-10-15T17:56:11Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Removed only the exact GOLD context-parent contribution habitatmech:GOLD.ca321f1251. Current independent parents: UBERON:0000955. All source IDs, counts/units, taxa, mapping predicates, native status and previous events are preserved. Unresolved predecessor findings remain explicitly open or deferred below.

## Scope And Provenance

Full current target re-read and scoped disposition of every exact predecessor finding.

Selection: One of seventeen repaired targets within the twenty-four-record bovine/brain/breast/bronchial cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base c062438003a4cb4b49d56c4a055771a981a17ccf.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.6bdd76cda3 | data/habitats/host_associated/brain__803f6884.yaml | generated | Brain |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate data/habitats/host_associated/brain__803f6884.yaml | passed | True | habitatmech:GOLD.6bdd76cda3 | Executed 2026-10-15T17:18:04Z through 2026-10-15T17:18:11Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/brain__803f6884.yaml |
| just validate-strict data/habitats/host_associated/bovinae_cow_cattle.yaml data/habitats/host_associated/bowens_disease_squamous_cell_carcinoma_in_situ.yaml data/habitats/host_associated/brain.yaml data/habitats/host_associated/brain__7bf4166c.yaml data/habitats/host_associated/brain__803f6884.yaml data/habitats/host_associated/brain__b2bb2ba8.yaml data/habitats/host_associated/brain__e9ca95b7.yaml data/habitats/host_associated/brain__f0593337.yaml data/habitats/host_associated/brain_cell_line.yaml data/habitats/host_associated/brain_stem.yaml data/habitats/host_associated/breast.yaml data/habitats/host_associated/breast_abscess.yaml data/habitats/host_associated/breast_cancer.yaml data/habitats/host_associated/breast_cancer_ductal.yaml data/habitats/host_associated/breast_cancer_lobular.yaml data/habitats/host_associated/breast_cyst.yaml data/habitats/host_associated/breviatea.yaml data/habitats/host_associated/bronchi.yaml data/habitats/host_associated/bronchi__3fb23b44.yaml data/habitats/host_associated/bronchi__c8c64428.yaml data/habitats/host_associated/bronchial_epithelial_cell.yaml data/habitats/host_associated/bronchiole.yaml data/habitats/host_associated/bronchoalveolar_lavage_fluid.yaml data/habitats/host_associated/bronchus.yaml | passed | True | habitatmech:GOLD.6bdd76cda3 | Executed 2026-10-15T17:19:44Z through 2026-10-15T17:19:53Z. uv run python scripts/validate_strict.py data/habitats/host_associated/bovinae_cow_cattle.yaml data/habitats/host_associated/bowens_disease_squamous_cell_carcinoma_in_situ.yaml data/habitats/host_associated/brain.yaml data/habitats/host_associated/brain__7bf4166c.yaml data/habitats/host_associated/brain__803f6884.yaml data/habitats/host_associated/brain__b2bb2ba8.yaml data/habitats/host_associated/brain__e9ca95b7.yaml data/habitats/host_associated/brain__f0593337.yaml data/habitats/host_associated/brain_cell_line.yaml data/habitats/host_associated/brain_stem.yaml data/habitats/host_associated/breast.yaml data/habitats/host_associated/breast_abscess.yaml data/habitats/host_associated/breast_cancer.yaml data/habitats/host_associated/breast_cancer_ductal.yaml data/habitats/host_associated/breast_cancer_lobular.yaml data/habitats/host_associated/breast_cyst.yaml data/habitats/host_associated/breviatea.yaml data/habitats/host_associated/bronchi.yaml data/habitats/host_associated/bronchi__3fb23b44.yaml data/habitats/host_associated/bronchi__c8c64428.yaml data/habitats/host_associated/bronchial_epithelial_cell.yaml data/habitats/host_associated/bronchiole.yaml data/habitats/host_associated/bronchoalveolar_lavage_fluid.yaml data/habitats/host_associated/bronchus.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| just validate-history | passed | True | habitatmech:GOLD.6bdd76cda3 | Executed 2026-10-15T17:19:53Z through 2026-10-15T17:20:06Z. No issues found<br>816 history record(s) valid against src/habitatmech/schema/history.yaml |
| just provenance-check | passed | True | habitatmech:GOLD.6bdd76cda3 | Executed 2026-10-15T17:20:06Z through 2026-10-15T17:20:06Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| just verify-corpus | passed | True | habitatmech:GOLD.6bdd76cda3 | Executed 2026-10-15T17:20:06Z through 2026-10-15T17:20:29Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| just validate-causal-all | passed | True | habitatmech:GOLD.6bdd76cda3 | Executed 2026-10-15T17:20:29Z through 2026-10-15T17:20:34Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| just term-requests-check | passed | True | habitatmech:GOLD.6bdd76cda3 | Executed 2026-10-15T17:20:34Z through 2026-10-15T17:20:59Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| just validate-products | passed | True | habitatmech:GOLD.6bdd76cda3 | Executed 2026-10-15T17:20:59Z through 2026-10-15T17:22:02Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python -m pytest -q tests/test_brain_breast_bronchial_review_repairs.py | passed | True | habitatmech:GOLD.6bdd76cda3 | Executed 2026-10-15T17:22:02Z through 2026-10-15T17:22:11Z. ..                                                                       [100%]<br>2 passed in 7.51s |
| git diff --check 50dbf8b388bf32ca58708f7993e83120310f7cea | passed | True | habitatmech:GOLD.6bdd76cda3 | Executed 2026-10-15T17:22:11Z through 2026-10-15T17:22:11Z.  |
| Exact-revision full QC and structured archive contract | passed | True | habitatmech:GOLD.6bdd76cda3 | Verified 2026-10-15T17:54:42Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38777236046 |

## Scientific And Domain Assessments

### Correction and source preservation

consistency: supported. Targets: habitatmech:GOLD.6bdd76cda3.

Removed only the exact GOLD context-parent contribution habitatmech:GOLD.ca321f1251. Current independent parents: UBERON:0000955. All source IDs, counts/units, taxa, mapping predicates, native status and previous events are preserved. Unresolved predecessor findings remain explicitly open or deferred below.

### Current source identity and definitions

identity: supported. Targets: habitatmech:GOLD.6bdd76cda3.

The regenerated target remains Brain (habitatmech:GOLD.6bdd76cda3), with unchanged NARROW/SEEDED status and 1 source attestation(s). The retained identity and source meaning remain supported by the linked predecessor evidence; this correction asserts no new definition, merge or source localization.

### Remaining scoped findings

representation: concern. Targets: habitatmech:GOLD.6bdd76cda3.

Unresolved findings retain their exact issue keys and target scopes; a repaired parent does not certify other claims.

## Findings

### F1: Containing anatomy is not a broader habitat class

major / resolved / confirmed; issue key: brain--803f6884-context-parent.

The predecessor claim is corrected through the guarded maintained input. Removed only the exact GOLD context-parent contribution habitatmech:GOLD.ca321f1251. Current independent parents: UBERON:0000955. The original observation remains immutable; no unrelated finding is closed.

Disposition: Removed only the exact GOLD context-parent contribution habitatmech:GOLD.ca321f1251. Current independent parents: UBERON:0000955. Full-corpus preservation regression and exact-revision native QC passed.

### F2: Narrow predicate uses an undeclared ontology-parent endpoint

major / open / confirmed; issue key: brain--803f6884-mapping-endpoint-contract.

Reassessed after the parent/alias repair; this finding is not resolved. Actual resolution retains the GOLD source mint but emits narrowMatch relative to the generic ontology parent. The SourceAttestation contract instead describes source-to-record identity. Reconcile producer/schema/consumers under #1398 without merging host-specific concepts or merely swapping predicates. This is not a claim that SKOS forbids self-links, and downstream SSSOM/KGX conformance has not been tested.

## Recommended Actions And Acceptance Checks

### ACT2

Actual resolution retains the GOLD source mint but emits narrowMatch relative to the generic ontology parent. The SourceAttestation contract instead describes source-to-record identity. Reconcile producer/schema/consumers under #1398 without merging host-specific concepts or merely swapping predicates. This is not a claim that SKOS forbids self-links, and downstream SSSOM/KGX conformance has not been tested. No repair is performed by this review.

- Regress the exact reported claim and preserve independent identifiers, counts/units and raw provenance. Change identity, native status or mapping only when separately supported by the scoped item assessment; never change source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000955/graph; UBERON_0000955-graph.json | context_only | Typed outgoing ontology relations, not an untyped ancestor list: [{"source": "http://purl.obolibrary.org/obo/UBERON_0000955", "target": "http://purl.obolibrary.org/obo/UBERON_0000062", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000955", "target": "http://purl.obolibrary.org/obo/UBERON_0004121", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000955", "target": "http://purl.obolibrary.org/obo/CL_0002319", "uri": "http://purl.obolibrary.org/obo/RO_0002473", "label": "composed primarily of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000955", "target": "http://purl.obolibrary.org/obo/UBERON_0000066", "uri": "http://purl.obolibrary.org/obo/RO_0002492", "label": "existence ends during"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000955", "target": "http://purl.obolibrary.org/obo/UBERON_0000468", "uri": "http://purl.obolibrary.org/obo/BSPO_0000123", "label": "in anterior side of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000955", "target": "http://purl.obolibrary.org/obo/UBERON_0001016", "uri": "http://purl.obolibrary.org/obo/RO_0002433", "label": "contributes to morphology of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000955", "target": "http://purl.obolibrary.org/obo/UBERON_0001017", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000955", "target": "http://purl.obolibrary.org/obo/UBERON_0002346", "uri": "http://purl.obolibrary.org/obo/RO_0002202", "label": "develops from"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000955", "target": "http://purl.obolibrary.org/obo/UBERON_0006238", "uri": "http://purl.obolibrary.org/obo/RO_0002202", "label": "develops from"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000955; UBERON_0000955.json | context_only | Current term identity, active status and definition: {"obo_id": "UBERON:0000955", "label": "brain", "is_obsolete": false, "description": ["The brain is the center of the nervous system in all vertebrate, and most invertebrate, animals. Some primitive animals such as jellyfish and starfish have a decentralized nervous system without a brain, while sponges lack any nervous system at all. In vertebrates, the brain is located in the head, protected by the skull and close to the primary sensory apparatus of vision, hearing, balance, taste, and smell[WP]."]} |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001016/graph; UBERON_0001016-graph.json | context_only | Typed outgoing ontology relations, not an untyped ancestor list: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001016", "target": "http://purl.obolibrary.org/obo/UBERON_0000467", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001016", "target": "http://purl.obolibrary.org/obo/CL_0000540", "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001016", "target": "http://purl.obolibrary.org/obo/CL_0002319", "uri": "http://purl.obolibrary.org/obo/RO_0002473", "label": "composed primarily of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001016", "target": "http://purl.obolibrary.org/obo/GO_0050877", "uri": "http://purl.obolibrary.org/obo/RO_0002215", "label": "capable of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001016", "target": "http://purl.obolibrary.org/obo/NCBITaxon_6072", "uri": "http://purl.obolibrary.org/obo/RO_0002162", "label": "in taxon"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001016", "target": "http://purl.obolibrary.org/obo/UBERON_0000066", "uri": "http://purl.obolibrary.org/obo/RO_0002492", "label": "existence ends during"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001016", "target": "http://purl.obolibrary.org/obo/UBERON_0000922", "uri": "http://purl.obolibrary.org/obo/RO_0002202", "label": "develops from"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001016", "target": "http://purl.obolibrary.org/obo/UBERON_0016880", "uri": "http://purl.obolibrary.org/obo/RO_0002202", "label": "develops from"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001016; UBERON_0001016.json | context_only | Current term identity, active status and definition: {"obo_id": "UBERON:0001016", "label": "nervous system", "is_obsolete": false, "description": ["The nervous system is an organ system containing predominantly neuron and glial cells. In bilaterally symmetrical organism, it is arranged in a network of tree-like structures connected to a central body. The main functions of the nervous system are to regulate and control body functions, and to receive sensory input, process this information, and generate behavior [CUMBO]."]} |
| EAFTER | data/habitats/host_associated/brain__803f6884.yaml; Entire regenerated target | supports | {"identifier": "habitatmech:GOLD.6bdd76cda3", "label": "Brain", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0000955"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:3675", "source_label": "Brain", "source_path": "Host-associated &gt; Mammals &gt; Nervous system &gt; Brain", "mapping_predicate": "skos:narrowMatch", "assertion_count": 94, "assertion_unit": "ORGANISM", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NARROW."}, {"timestamp": "2026-10-15T00:00:00Z", "curator": "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.ca321f1251 for habitatmech:GOLD.6bdd76cda3 (Host-associated &gt; Mammals &gt; Nervous system &gt; Brain). Review https://github.com/CultureBotAI/HabitatMech/issues/2190 : A component, cell or lesion is not a subtype of its whole containing organ or system. Exclude only this exact GOLD contribution; retain independent genera, source observations and native status. This does not settle source-material scope or mapping endpoint #1398."}]} |
| EPREV | reviews/structured/20261015T165554Z-brain__803f6884-record/review.yaml; Exact predecessor and all findings | supports | Original observation retained unchanged; every finding is reconciled with identical affected-target scope. |
| ETEST | tests/test_brain_breast_bronchial_review_repairs.py; Full-corpus counterfactual and public URL rendering | supports | Regression proves exactly seventeen records change, only by sixteen parent removals, one alias removal and one appended event each. All 3208 identities and every unrelated record are preserved. |
| ERULE | docs/CURATION.md; Strict hierarchy, host identity and source provenance | supports | Containing anatomy and disease classification are not broader habitat ancestry. Hosts and their environment are distinct identities. |
| EINPUT | curation/gold_parent_exclusions.tsv; Exact keyed rows 4 | supports | [[4, "habitatmech:GOLD.6bdd76cda3\tHost-associated &gt; Mammals &gt; Nervous system &gt; Brain\thabitatmech:GOLD.ca321f1251\tcodex-gpt-5\t2026-10-15\tReview https://github.com/CultureBotAI/HabitatMech/issues/2190 : A component, cell or lesion is not a subtype of its whole containing organ or system. Exclude only this exact GOLD contribution; retain independent genera, source observations and native status. This does not settle source-material scope or mapping endpoint #1398."]] |
| EHISTORY | src/habitatmech/seed.py; build_document and _decision_summary | supports | Current decision notes are projected into their generated historical events; changing the note would replace prior content. Existing notes and history remain unchanged; #2192 requires a history-preserving owner. |

## Limits And Additional Notes

- Same-agent self-review, not independent approval. Primary-source and specimen-level limitations of the linked predecessor remain; no new universal taxon, prevalence or mechanism claim is made.
- Shared mapping endpoint #1398 and kg-microbe SSSOM/KGX conformity are not resolved. Current record status is not scientific sign-off.
- Configured label gate retains 2061 no-adapter skips. iModulonDB is not applicable because no gene/module assertion is added.
- Final-head checks must validate this new immutable successor; the recorded full QC covers the exact repaired scientific inputs.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T175611Z-brain__803f6884-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: Brain (habitatmech:GOLD.6bdd76cda3)'
started_at: '2026-10-15T17:25:38Z'
finished_at: '2026-10-15T17:56:11Z'
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
summary: 'Removed only the exact GOLD context-parent contribution habitatmech:GOLD.ca321f1251.
  Current independent parents: UBERON:0000955. All source IDs, counts/units, taxa,
  mapping predicates, native status and previous events are preserved. Unresolved
  predecessor findings remain explicitly open or deferred below.'
source:
  git_revision: c062438003a4cb4b49d56c4a055771a981a17ccf
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
  - path: data/habitats/host_associated/brain__803f6884.yaml
    sha256: 8d5fa58f157e2ba714aa0be381b0a53483b13770ffc6870ce7cae3538aaaf8f8
    role: target
  - path: data/habitats/host_associated/nervous_system__e978605d.yaml
    sha256: 0e9890f72769ad29326a4f6e24d03cf2e97312e24526ed1acdf93c4fd252face
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
  - path: history/mappings/bovinae_cow_cattle/2026-10-15T171621Z-codex-gpt-5-ac1f26.yaml
    sha256: 4d5e740d53c2b10b6d2770551660119020f8614a2a2d9b02bc4ba116e64240d0
    role: context
  - path: history/mappings/brain_breast_bronchial_review/2026-10-15T171620Z-codex-gpt-5-c7d641.yaml
    sha256: 40227be7cbd12e7c2d33e5e36c77bcf664cc34bf6fd58724c313cb28c36b1741
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260922T083615Z-brain__803f6884.md
    sha256: 1ed2327e7c762b580a751c52d37504a2038ef5edaaeb138b4a229c738542a0c8
    role: context
  - path: reviews/structured/20261015T165554Z-brain__803f6884-record/review.yaml
    sha256: 8ef6f9ee4ebcf76078084fded86576afb5c4d33f5783e72559c11630f9e9f958
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
  - path: tests/test_brain_breast_bronchial_review_repairs.py
    sha256: fe5445f7ec0133992669f7e5f1aea80d24d34ddda774308f4c74f46022985dca
    role: context
targets:
- target_id: habitatmech:GOLD.6bdd76cda3
  path: data/habitats/host_associated/brain__803f6884.yaml
  label: Brain
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
  description: Full current target re-read and scoped disposition of every exact predecessor
    finding.
  selection: One of seventeen repaired targets within the twenty-four-record bovine/brain/breast/bronchial
    cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.6bdd76cda3
  exclusions:
  - target: Other targets and SSSOM/KGX compatibility
    reason: 'This observation does not close source-evidence gaps, shared mapping
      contract #1398 or current kg-microbe compatibility questions.'
checks:
- check_id: C3
  name: just validate data/habitats/host_associated/brain__803f6884.yaml
  status: passed
  required: true
  command: just validate data/habitats/host_associated/brain__803f6884.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.6bdd76cda3
  summary: "Executed 2026-10-15T17:18:04Z through 2026-10-15T17:18:11Z. No issues\
    \ found\n uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class\
    \ HabitatRecord data/habitats/host_associated/brain__803f6884.yaml"
  scope_note: Ordinary schema for seventeen corrected targets, strict for all 24,
    focused regression and documented full-corpus native gates.
- check_id: C17
  name: just validate-strict data/habitats/host_associated/bovinae_cow_cattle.yaml
    data/habitats/host_associated/bowens_disease_squamous_cell_carcinoma_in_situ.yaml
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
  status: passed
  required: true
  command: just validate-strict data/habitats/host_associated/bovinae_cow_cattle.yaml
    data/habitats/host_associated/bowens_disease_squamous_cell_carcinoma_in_situ.yaml
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
  - habitatmech:GOLD.6bdd76cda3
  summary: "Executed 2026-10-15T17:19:44Z through 2026-10-15T17:19:53Z. uv run python\
    \ scripts/validate_strict.py data/habitats/host_associated/bovinae_cow_cattle.yaml\
    \ data/habitats/host_associated/bowens_disease_squamous_cell_carcinoma_in_situ.yaml\
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
  scope_note: Ordinary schema for seventeen corrected targets, strict for all 24,
    focused regression and documented full-corpus native gates.
- check_id: C18
  name: just validate-history
  status: passed
  required: true
  command: just validate-history
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.6bdd76cda3
  summary: 'Executed 2026-10-15T17:19:53Z through 2026-10-15T17:20:06Z. No issues
    found

    816 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Ordinary schema for seventeen corrected targets, strict for all 24,
    focused regression and documented full-corpus native gates.
- check_id: C19
  name: just provenance-check
  status: passed
  required: true
  command: just provenance-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.6bdd76cda3
  summary: "Executed 2026-10-15T17:20:06Z through 2026-10-15T17:20:06Z. provenance\
    \ current: 14 committed inventories, 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Ordinary schema for seventeen corrected targets, strict for all 24,
    focused regression and documented full-corpus native gates.
- check_id: C20
  name: just verify-corpus
  status: passed
  required: true
  command: just verify-corpus
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.6bdd76cda3
  summary: "Executed 2026-10-15T17:20:06Z through 2026-10-15T17:20:29Z. expected 3208\
    \ records, found 3208 on disk\n  missing:   0\n  extra:     0\n  differing: 0\n\
    \ncorpus reproduces exactly from data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Ordinary schema for seventeen corrected targets, strict for all 24,
    focused regression and documented full-corpus native gates.
- check_id: C21
  name: just validate-causal-all
  status: passed
  required: true
  command: just validate-causal-all
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.6bdd76cda3
  summary: "Executed 2026-10-15T17:20:29Z through 2026-10-15T17:20:34Z. validated\
    \ 32 causal-graph curation file(s) with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Ordinary schema for seventeen corrected targets, strict for all 24,
    focused regression and documented full-corpus native gates.
- check_id: C22
  name: just term-requests-check
  status: passed
  required: true
  command: just term-requests-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.6bdd76cda3
  summary: "Executed 2026-10-15T17:20:34Z through 2026-10-15T17:20:59Z. term-request\
    \ table is current (110 terms)\n uv run python scripts/build_term_requests.py\
    \ --check"
  scope_note: Ordinary schema for seventeen corrected targets, strict for all 24,
    focused regression and documented full-corpus native gates.
- check_id: C23
  name: just validate-products
  status: passed
  required: true
  command: just validate-products
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.6bdd76cda3
  summary: "Executed 2026-10-15T17:20:59Z through 2026-10-15T17:22:02Z. id↔label correspondence\
    \ summary:\n          OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n        \
    \  OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n\
    \ uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Ordinary schema for seventeen corrected targets, strict for all 24,
    focused regression and documented full-corpus native gates.
- check_id: C24
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_brain_breast_bronchial_review_repairs.py
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_brain_breast_bronchial_review_repairs.py
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.6bdd76cda3
  summary: 'Executed 2026-10-15T17:22:02Z through 2026-10-15T17:22:11Z. ..                                                                       [100%]

    2 passed in 7.51s'
  scope_note: Ordinary schema for seventeen corrected targets, strict for all 24,
    focused regression and documented full-corpus native gates.
- check_id: C25
  name: git diff --check 50dbf8b388bf32ca58708f7993e83120310f7cea
  status: passed
  required: true
  command: git diff --check 50dbf8b388bf32ca58708f7993e83120310f7cea
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.6bdd76cda3
  summary: 'Executed 2026-10-15T17:22:11Z through 2026-10-15T17:22:11Z. '
  scope_note: Ordinary schema for seventeen corrected targets, strict for all 24,
    focused regression and documented full-corpus native gates.
- check_id: CCI
  name: Exact-revision full QC and structured archive contract
  status: passed
  required: true
  command: gh run view 38777236046 --json status,conclusion,headSha,url,jobs
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.6bdd76cda3
  summary: Verified 2026-10-15T17:54:42Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38777236046
  scope_note: Authoritative CI full QC passed at exact captured scientific input revision;
    final-head validation must also check this new successor before merge.
evidence:
- evidence_id: EX1
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000955/graph
  locator: UBERON_0000955-graph.json
  accessed_at: '2026-10-15T16:34:23Z'
  support: context_only
  summary: 'Typed outgoing ontology relations, not an untyped ancestor list: [{"source":
    "http://purl.obolibrary.org/obo/UBERON_0000955", "target": "http://purl.obolibrary.org/obo/UBERON_0000062",
    "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"},
    {"source": "http://purl.obolibrary.org/obo/UBERON_0000955", "target": "http://purl.obolibrary.org/obo/UBERON_0004121",
    "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"},
    {"source": "http://purl.obolibrary.org/obo/UBERON_0000955", "target": "http://purl.obolibrary.org/obo/CL_0002319",
    "uri": "http://purl.obolibrary.org/obo/RO_0002473", "label": "composed primarily
    of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000955", "target": "http://purl.obolibrary.org/obo/UBERON_0000066",
    "uri": "http://purl.obolibrary.org/obo/RO_0002492", "label": "existence ends during"},
    {"source": "http://purl.obolibrary.org/obo/UBERON_0000955", "target": "http://purl.obolibrary.org/obo/UBERON_0000468",
    "uri": "http://purl.obolibrary.org/obo/BSPO_0000123", "label": "in anterior side
    of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000955", "target": "http://purl.obolibrary.org/obo/UBERON_0001016",
    "uri": "http://purl.obolibrary.org/obo/RO_0002433", "label": "contributes to morphology
    of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000955", "target": "http://purl.obolibrary.org/obo/UBERON_0001017",
    "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source":
    "http://purl.obolibrary.org/obo/UBERON_0000955", "target": "http://purl.obolibrary.org/obo/UBERON_0002346",
    "uri": "http://purl.obolibrary.org/obo/RO_0002202", "label": "develops from"},
    {"source": "http://purl.obolibrary.org/obo/UBERON_0000955", "target": "http://purl.obolibrary.org/obo/UBERON_0006238",
    "uri": "http://purl.obolibrary.org/obo/RO_0002202", "label": "develops from"}]'
  snapshot_sha256: 093422d631ddc78467b92a3c797d93003e3cbc8781cc8f47dd4d99a1d96d9ae6
- evidence_id: EX2
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000955
  locator: UBERON_0000955.json
  accessed_at: '2026-10-15T16:34:22Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "UBERON:0000955",
    "label": "brain", "is_obsolete": false, "description": ["The brain is the center
    of the nervous system in all vertebrate, and most invertebrate, animals. Some
    primitive animals such as jellyfish and starfish have a decentralized nervous
    system without a brain, while sponges lack any nervous system at all. In vertebrates,
    the brain is located in the head, protected by the skull and close to the primary
    sensory apparatus of vision, hearing, balance, taste, and smell[WP]."]}'
  snapshot_sha256: 9083451a13b7e45058362501bb03fd93944d7aa79ffc0248bc2cf8b1520b9652
- evidence_id: EX3
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001016/graph
  locator: UBERON_0001016-graph.json
  accessed_at: '2026-10-15T16:34:26Z'
  support: context_only
  summary: 'Typed outgoing ontology relations, not an untyped ancestor list: [{"source":
    "http://purl.obolibrary.org/obo/UBERON_0001016", "target": "http://purl.obolibrary.org/obo/UBERON_0000467",
    "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"},
    {"source": "http://purl.obolibrary.org/obo/UBERON_0001016", "target": "http://purl.obolibrary.org/obo/CL_0000540",
    "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}, {"source":
    "http://purl.obolibrary.org/obo/UBERON_0001016", "target": "http://purl.obolibrary.org/obo/CL_0002319",
    "uri": "http://purl.obolibrary.org/obo/RO_0002473", "label": "composed primarily
    of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001016", "target": "http://purl.obolibrary.org/obo/GO_0050877",
    "uri": "http://purl.obolibrary.org/obo/RO_0002215", "label": "capable of"}, {"source":
    "http://purl.obolibrary.org/obo/UBERON_0001016", "target": "http://purl.obolibrary.org/obo/NCBITaxon_6072",
    "uri": "http://purl.obolibrary.org/obo/RO_0002162", "label": "in taxon"}, {"source":
    "http://purl.obolibrary.org/obo/UBERON_0001016", "target": "http://purl.obolibrary.org/obo/UBERON_0000066",
    "uri": "http://purl.obolibrary.org/obo/RO_0002492", "label": "existence ends during"},
    {"source": "http://purl.obolibrary.org/obo/UBERON_0001016", "target": "http://purl.obolibrary.org/obo/UBERON_0000922",
    "uri": "http://purl.obolibrary.org/obo/RO_0002202", "label": "develops from"},
    {"source": "http://purl.obolibrary.org/obo/UBERON_0001016", "target": "http://purl.obolibrary.org/obo/UBERON_0016880",
    "uri": "http://purl.obolibrary.org/obo/RO_0002202", "label": "develops from"}]'
  snapshot_sha256: 95234704cbe48ae48782b557f33291f2094de860ac11578fe32e65daaa916a46
- evidence_id: EX4
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001016
  locator: UBERON_0001016.json
  accessed_at: '2026-10-15T16:34:26Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "UBERON:0001016",
    "label": "nervous system", "is_obsolete": false, "description": ["The nervous
    system is an organ system containing predominantly neuron and glial cells. In
    bilaterally symmetrical organism, it is arranged in a network of tree-like structures
    connected to a central body. The main functions of the nervous system are to regulate
    and control body functions, and to receive sensory input, process this information,
    and generate behavior [CUMBO]."]}'
  snapshot_sha256: 99bfc901274c22f8db92d6ff295597688ec0d4e17fbb4d50a3c6fe03a23c8599
- evidence_id: EAFTER
  kind: record_content
  reference: data/habitats/host_associated/brain__803f6884.yaml
  locator: Entire regenerated target
  accessed_at: '2026-10-15T17:56:11Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.6bdd76cda3", "label": "Brain", "habitat_category":
    "HOST_ASSOCIATED", "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats":
    ["UBERON:0000955"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:3675",
    "source_label": "Brain", "source_path": "Host-associated > Mammals > Nervous system
    > Brain", "mapping_predicate": "skos:narrowMatch", "assertion_count": 94, "assertion_unit":
    "ORGANISM", "notes": "2 GOLD ecosystem node ids share this path; first shown.
    See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp":
    "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES",
    "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NARROW."},
    {"timestamp": "2026-10-15T00:00:00Z", "curator": "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED",
    "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.ca321f1251
    for habitatmech:GOLD.6bdd76cda3 (Host-associated > Mammals > Nervous system >
    Brain). Review https://github.com/CultureBotAI/HabitatMech/issues/2190 : A component,
    cell or lesion is not a subtype of its whole containing organ or system. Exclude
    only this exact GOLD contribution; retain independent genera, source observations
    and native status. This does not settle source-material scope or mapping endpoint
    #1398."}]}'
  snapshot_sha256: 8d5fa58f157e2ba714aa0be381b0a53483b13770ffc6870ce7cae3538aaaf8f8
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261015T165554Z-brain__803f6884-record/review.yaml
  locator: Exact predecessor and all findings
  accessed_at: '2026-10-15T17:56:11Z'
  support: supports
  summary: Original observation retained unchanged; every finding is reconciled with
    identical affected-target scope.
  snapshot_sha256: 8ef6f9ee4ebcf76078084fded86576afb5c4d33f5783e72559c11630f9e9f958
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_brain_breast_bronchial_review_repairs.py
  locator: Full-corpus counterfactual and public URL rendering
  accessed_at: '2026-10-15T17:56:11Z'
  support: supports
  summary: Regression proves exactly seventeen records change, only by sixteen parent
    removals, one alias removal and one appended event each. All 3208 identities and
    every unrelated record are preserved.
  snapshot_sha256: fe5445f7ec0133992669f7e5f1aea80d24d34ddda774308f4c74f46022985dca
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Strict hierarchy, host identity and source provenance
  accessed_at: '2026-10-15T17:56:11Z'
  support: supports
  summary: Containing anatomy and disease classification are not broader habitat ancestry.
    Hosts and their environment are distinct identities.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: EINPUT
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: Exact keyed rows 4
  accessed_at: '2026-10-15T17:56:11Z'
  support: supports
  summary: '[[4, "habitatmech:GOLD.6bdd76cda3\tHost-associated > Mammals > Nervous
    system > Brain\thabitatmech:GOLD.ca321f1251\tcodex-gpt-5\t2026-10-15\tReview https://github.com/CultureBotAI/HabitatMech/issues/2190
    : A component, cell or lesion is not a subtype of its whole containing organ or
    system. Exclude only this exact GOLD contribution; retain independent genera,
    source observations and native status. This does not settle source-material scope
    or mapping endpoint #1398."]]'
  snapshot_sha256: 9344f0bbbad1423ff0e47204ad49bc27ffaf4b5e63841e77e09cc01877b91f54
- evidence_id: EHISTORY
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: build_document and _decision_summary
  accessed_at: '2026-10-15T17:56:11Z'
  support: supports
  summary: 'Current decision notes are projected into their generated historical events;
    changing the note would replace prior content. Existing notes and history remain
    unchanged; #2192 requires a history-preserving owner.'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
assessments:
- assessment_id: A1
  area: consistency
  topic: Correction and source preservation
  outcome: supported
  summary: 'Removed only the exact GOLD context-parent contribution habitatmech:GOLD.ca321f1251.
    Current independent parents: UBERON:0000955. All source IDs, counts/units, taxa,
    mapping predicates, native status and previous events are preserved. Unresolved
    predecessor findings remain explicitly open or deferred below.'
  target_ids:
  - habitatmech:GOLD.6bdd76cda3
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EX4
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EINPUT
  - EHISTORY
- assessment_id: A2
  area: identity
  topic: Current source identity and definitions
  outcome: supported
  summary: The regenerated target remains Brain (habitatmech:GOLD.6bdd76cda3), with
    unchanged NARROW/SEEDED status and 1 source attestation(s). The retained identity
    and source meaning remain supported by the linked predecessor evidence; this correction
    asserts no new definition, merge or source localization.
  target_ids:
  - habitatmech:GOLD.6bdd76cda3
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EX4
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EINPUT
  - EHISTORY
- assessment_id: A3
  area: representation
  topic: Remaining scoped findings
  outcome: concern
  summary: Unresolved findings retain their exact issue keys and target scopes; a
    repaired parent does not certify other claims.
  target_ids:
  - habitatmech:GOLD.6bdd76cda3
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EX4
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EINPUT
  - EHISTORY
findings:
- finding_id: F1
  issue_key: brain--803f6884-context-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Containing anatomy is not a broader habitat class
  description: 'The predecessor claim is corrected through the guarded maintained
    input. Removed only the exact GOLD context-parent contribution habitatmech:GOLD.ca321f1251.
    Current independent parents: UBERON:0000955. The original observation remains
    immutable; no unrelated finding is closed.'
  target_ids:
  - habitatmech:GOLD.6bdd76cda3
  field_paths:
  - parent_habitats
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EX4
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EINPUT
  - EHISTORY
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or source-evidence claim;
    deterministic validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2190
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261015T165554Z-brain__803f6884-record
    finding_id: F1
  disposition_reason: 'Removed only the exact GOLD context-parent contribution habitatmech:GOLD.ca321f1251.
    Current independent parents: UBERON:0000955. Full-corpus preservation regression
    and exact-revision native QC passed.'
- finding_id: F2
  issue_key: brain--803f6884-mapping-endpoint-contract
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Narrow predicate uses an undeclared ontology-parent endpoint
  description: 'Reassessed after the parent/alias repair; this finding is not resolved.
    Actual resolution retains the GOLD source mint but emits narrowMatch relative
    to the generic ontology parent. The SourceAttestation contract instead describes
    source-to-record identity. Reconcile producer/schema/consumers under #1398 without
    merging host-specific concepts or merely swapping predicates. This is not a claim
    that SKOS forbids self-links, and downstream SSSOM/KGX conformance has not been
    tested.'
  target_ids:
  - habitatmech:GOLD.6bdd76cda3
  field_paths:
  - source_attestations[0].mapping_predicate
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EX4
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EINPUT
  - EHISTORY
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
    review_id: 20261015T165554Z-brain__803f6884-record
    finding_id: F2
actions:
- action_id: ACT2
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.6bdd76cda3
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  description: 'Actual resolution retains the GOLD source mint but emits narrowMatch
    relative to the generic ontology parent. The SourceAttestation contract instead
    describes source-to-record identity. Reconcile producer/schema/consumers under
    #1398 without merging host-specific concepts or merely swapping predicates. This
    is not a claim that SKOS forbids self-links, and downstream SSSOM/KGX conformance
    has not been tested. No repair is performed by this review.'
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
- Same-agent self-review, not independent approval. Primary-source and specimen-level
  limitations of the linked predecessor remain; no new universal taxon, prevalence
  or mechanism claim is made.
- 'Shared mapping endpoint #1398 and kg-microbe SSSOM/KGX conformity are not resolved.
  Current record status is not scientific sign-off.'
- Configured label gate retains 2061 no-adapter skips. iModulonDB is not applicable
  because no gene/module assertion is added.
- Final-head checks must validate this new immutable successor; the recorded full
  QC covers the exact repaired scientific inputs.
notes: []
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261015T165554Z-brain__803f6884-record
  relationship: Exact predecessor; every original finding is explicitly reconciled.
```
