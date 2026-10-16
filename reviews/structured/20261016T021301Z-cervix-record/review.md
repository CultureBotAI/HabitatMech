# Record review: Cervix (habitatmech:GOLD.c15e1115f3)

- Review: 20261016T021301Z-cervix-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-16T02:00:43Z
- Finished UTC: 2026-10-16T02:13:01Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The human source is a host-scoped uterine cervix, with a valid generic cervix genus. Current Uberon explicitly relates cervix to uterus by part_of; whole human uterus is not a strictly broader class. Preserve 28 ORGANISM assertions separately from 127 supplemental biosamples and three study memberships, and do not equate the mucus medium with the anatomical site.

## Scope And Provenance

Full field-by-field review of this one generated record.

Selection: Next 24 unreviewed identifiers in deterministic path order from ignored-inclusive 3209-record census; this bundle assesses exactly one, not a proxy sample.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 5fef9bb871a510550a3f70c45118805ac7c8d9a8.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.c15e1115f3 | data/habitats/host_associated/cervix.yaml | generated | Cervix |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.c15e1115f3 | Finished 2026-10-16T02:01:44Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/cervix.yaml |
| validate-strict | passed | True | habitatmech:GOLD.c15e1115f3 | Finished 2026-10-16T02:04:22Z. uv run python scripts/validate_strict.py data/habitats/host_associated/cervical_cancer.yaml data/habitats/host_associated/cervical_neck_nodes.yaml data/habitats/host_associated/cervix.yaml data/habitats/host_associated/cervix__0de03fa8.yaml data/habitats/host_associated/chago_k_1_cell.yaml data/habitats/host_associated/cho.yaml data/habitats/host_associated/choanomastigote.yaml data/habitats/host_associated/cholesteatoma_tissue.yaml data/habitats/host_associated/chorionic_villi.yaml data/habitats/host_associated/chorionic_villi__9af464db.yaml data/habitats/host_associated/chyme.yaml data/habitats/host_associated/chyme__0bfd2730.yaml data/habitats/host_associated/cibarium_preoral_cavity.yaml data/habitats/host_associated/ciliates.yaml data/habitats/host_associated/ciliates__df51eda4.yaml data/habitats/host_associated/ciliophora.yaml data/habitats/host_associated/circulatory_system.yaml data/habitats/host_associated/circulatory_system__241de4de.yaml data/habitats/host_associated/circulatory_system__5b3debaf.yaml data/habitats/host_associated/circulatory_system__745592ee.yaml data/habitats/host_associated/circulatory_system__7e4ecb0e.yaml data/habitats/host_associated/circulatory_system__90d88932.yaml data/habitats/host_associated/circulatory_system__e49da8a0.yaml data/habitats/host_associated/circulatory_system__f5b69d9c.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | habitatmech:GOLD.c15e1115f3 | Finished 2026-10-16T02:04:39Z. No issues found<br>830 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | habitatmech:GOLD.c15e1115f3 | Finished 2026-10-16T02:04:40Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | habitatmech:GOLD.c15e1115f3 | Finished 2026-10-16T02:05:09Z. expected 3209 records, found 3209 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | habitatmech:GOLD.c15e1115f3 | Finished 2026-10-16T02:05:15Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | habitatmech:GOLD.c15e1115f3 | Finished 2026-10-16T02:05:44Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | habitatmech:GOLD.c15e1115f3 | Finished 2026-10-16T02:07:01Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1173<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2063<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-base hosted QC | passed | True | habitatmech:GOLD.c15e1115f3 | Verified 2026-10-16T01:59:09Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38835150071 |
| Standalone citation validator applicability | not_applicable | False | habitatmech:GOLD.c15e1115f3 | No standalone citation checker documented for evidence-free generated targets. Stable references checked with native gates/current authorities; causal validation ran globally. |

## Scientific And Domain Assessments

### Identity, definition, aliases, source scope and hierarchy

identity: concern. Targets: habitatmech:GOLD.c15e1115f3.

The human source is a host-scoped uterine cervix, with a valid generic cervix genus. Current Uberon explicitly relates cervix to uterus by part_of; whole human uterus is not a strictly broader class. Preserve 28 ORGANISM assertions separately from 127 supplemental biosamples and three study memberships, and do not equate the mucus medium with the anatomical site.

### Counts, units, ranks and candidate pools

quantity: supported. Targets: habitatmech:GOLD.c15e1115f3.

Frozen source rows reproduce every emitted count/unit and displayed taxon score/rank/pool. Zero tree counts are omitted; supplemental biosamples, triads and study membership are nonadditive. {"assertions": [{"source": "GOLD", "count": 28, "unit": "ORGANISM", "row": {"row": 363, "data": {"canonical_path": "Host-associated &gt; Mammals: Human &gt; Reproductive system &gt; Uterus &gt; Cervix", "ecosystem": "Host-associated", "ecosystem_category": "Mammals: Human", "ecosystem_type": "Reproductive system", "ecosystem_subtype": "Uterus", "specific_ecosystem": "Cervix", "leaf_label": "Cervix", "depth": "5", "gold_node_count": "1", "organism_count": "28", "study_count": "0", "biosample_count": "0", "total_assertions": "28", "gold_node_ids": "gold.ecosystem:6126"}}}], "taxa": []}

### Native status and optional evidence

completeness: supported. Targets: habitatmech:GOLD.c15e1115f3.

Executed native resolution reproduces NARROW/SEEDED. No environmental parameters, causal graphs, discussions, datasets or characteristic-presence claims are asserted. Missing optional fields do not authorize invented content. Parent mechanisms are not inherited.

### Native checks and reproducibility

schema: supported. Targets: habitatmech:GOLD.c15e1115f3.

All 31 baseline commands passed: target schema, strict cohort, 830 histories, provenance, exact 3209-record reproduction, 32 causal overlays, 110 term requests and configured label checks. Hosted QC matches the exact base. Deterministic validity is not scientific approval.

## Findings

### F1: Source context is not a broader habitat class

major / open / confirmed; issue key: cervix-context-parent.

The human source is a host-scoped uterine cervix, with a valid generic cervix genus. Current Uberon explicitly relates cervix to uterus by part_of; whole human uterus is not a strictly broader class. Preserve 28 ORGANISM assertions separately from 127 supplemental biosamples and three study memberships, and do not equate the mucus medium with the anatomical site. Exclude only the exact GOLD source path contribution to habitatmech:GOLD.f736cbfbc5, preserving independently valid parents and all source provenance.

### F2: Mapping uses an undeclared ontology-parent endpoint

major / open / confirmed; issue key: cervix-mapping-endpoint-contract.

The executed route keeps the source mint but emits narrowMatch relative to its ontology parent; SourceAttestation instead declares source-to-record endpoints. Reconcile schema, producer and actual consumers under #1398. This is not a formal SKOS self-link prohibition, not solved by a blind predicate reversal, and not an SSSOM/KGX certification.

## Recommended Actions And Acceptance Checks

### ACT1

The human source is a host-scoped uterine cervix, with a valid generic cervix genus. Current Uberon explicitly relates cervix to uterus by part_of; whole human uterus is not a strictly broader class. Preserve 28 ORGANISM assertions separately from 127 supplemental biosamples and three study memberships, and do not equate the mucus medium with the anatomical site. Exclude only the exact GOLD source path contribution to habitatmech:GOLD.f736cbfbc5, preserving independently valid parents and all source provenance. No repair is performed by this review.

- Regress the exact claim, preserving independent valid genera, raw provenance and source counts/units. Change native status or mappings only when supported by the authorized ITEM assessment; never decrement source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

### ACT2

The executed route keeps the source mint but emits narrowMatch relative to its ontology parent; SourceAttestation instead declares source-to-record endpoints. Reconcile schema, producer and actual consumers under #1398. This is not a formal SKOS self-link prohibition, not solved by a blind predicate reversal, and not an SSSOM/KGX certification. No repair is performed by this review.

- Regress the exact claim, preserving independent valid genera, raw provenance and source counts/units. Change native status or mappings only when supported by the authorized ITEM assessment; never decrement source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/cervix.yaml; Full target YAML | supports | All fields and entire generated history read. |
| ERULE | docs/CURATION.md; Identity, parents, evidence and native status | supports | All parent contributions must be strictly broader. Optional absence and native SEEDED status are not inherently defects. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; HabitatRecord, SourceAttestation, TaxonAssociation | supports | Source mapping endpoints are source-to-record. Associations are not characteristic presence. |
| ESEED | src/habitatmech/seed.py; Executed native source resolution and complete document reproduction | supports | [{"mint": "habitatmech:GOLD.c15e1115f3", "automatic": {"identifier": "habitatmech:GOLD.c15e1115f3", "grounding_status": "NARROW", "mapping_predicate": "skos:narrowMatch", "contributes_grounding": true, "extra_parents": ["UBERON:0000002"], "extra_xrefs": [], "route": "gold_narrower_than_leaf_match", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "habitatmech:GOLD.c15e1115f3", "grounding_status": "NARROW", "mapping_predicate": "skos:narrowMatch", "contributes_grounding": true, "extra_parents": ["UBERON:0000002"], "extra_xrefs": [], "route": "gold_narrower_than_leaf_match", "category": null, "reviewed": false, "decision": null}}] |
| EEXTRACT | src/habitatmech/extract.py; Source projections and count/rank/score interpretation | supports | Exact source rows reproduce source-specific units, maximum scores and ranks. Frozen PREGO projection lacks original pair citation links. |
| ET5 | data/raw/gold_ecosystem_paths.tsv; Physical TSV rows 363 | supports | [{"row": 363, "data": {"canonical_path": "Host-associated &gt; Mammals: Human &gt; Reproductive system &gt; Uterus &gt; Cervix", "ecosystem": "Host-associated", "ecosystem_category": "Mammals: Human", "ecosystem_type": "Reproductive system", "ecosystem_subtype": "Uterus", "specific_ecosystem": "Cervix", "leaf_label": "Cervix", "depth": "5", "gold_node_count": "1", "organism_count": "28", "study_count": "0", "biosample_count": "0", "total_assertions": "28", "gold_node_ids": "gold.ecosystem:6126"}}] |
| ET6 | data/raw/gold_path_triads.tsv; Physical TSV rows 1493,1494,1495 | supports | [{"row": 1493, "data": {"canonical_path": "Host-associated &gt; Mammals: Human &gt; Reproductive system &gt; Uterus &gt; Cervix", "slot": "broad", "samples": "1", "studies": "1", "distinct_terms": "1", "top_term": "ENVO:01001000", "top_label": "environmental system determined by an organism", "top_share": "1.00", "studies_agreeing": "1"}}, {"row": 1494, "data": {"canonical_path": "Host-associated &gt; Mammals: Human &gt; Reproductive system &gt; Uterus &gt; Cervix", "slot": "local", "samples": "1", "studies": "1", "distinct_terms": "1", "top_term": "UBERON:0000002", "top_label": "uterine cervix", "top_share": "1.00", "studies_agreeing": "1"}}, {"row": 1495, "data": {"canonical_path": "Host-associated &gt; Mammals: Human &gt; Reproductive system &gt; Uterus &gt; Cervix", "slot": "medium", "samples": "1", "studies": "1", "distinct_terms": "1", "top_term": "UBERON:0000316", "top_label": "cervical mucus", "top_share": "1.00", "studies_agreeing": "1"}}] |
| ET7 | data/raw/gold_path_biosamples.tsv; Physical TSV rows 198 | supports | [{"row": 198, "data": {"canonical_path": "Host-associated &gt; Mammals: Human &gt; Reproductive system &gt; Uterus &gt; Cervix", "ecosystem_path_id": "6126", "biosample_count": "127"}}] |
| ET8 | data/raw/gold_studies.tsv; Physical TSV rows 2262,3310,3623 | supports | [{"row": 2262, "data": {"study_gold_id": "Gs0141904", "path_count": "2", "paths": "Host-associated &gt; Mammals: Human &gt; Reproductive system &gt; Fallopian tubes&#124;Host-associated &gt; Mammals: Human &gt; Reproductive system &gt; Uterus &gt; Cervix"}}, {"row": 3310, "data": {"study_gold_id": "Gs0150493", "path_count": "1", "paths": "Host-associated &gt; Mammals: Human &gt; Reproductive system &gt; Uterus &gt; Cervix"}}, {"row": 3623, "data": {"study_gold_id": "Gs0153705", "path_count": "1", "paths": "Host-associated &gt; Mammals: Human &gt; Reproductive system &gt; Uterus &gt; Cervix"}}] |
| ET9 | data/raw/ontology_subclass_edges.tsv; Physical TSV rows 10974,10975 | supports | [{"row": 10974, "data": {"subject": "UBERON:0000002", "predicate": "rdfs:subClassOf", "object": "UBERON:0001560"}}, {"row": 10975, "data": {"subject": "UBERON:0000002", "predicate": "rdfs:subClassOf", "object": "UBERON:0005156"}}] |
| ET10 | data/raw/ontology_terms.tsv; Physical TSV rows 12869 | supports | [{"row": 12869, "data": {"term_id": "UBERON:0000002", "ontology": "UBERON", "label": "uterine cervix", "definition": "Lower, narrow portion of the uterus where it joins with the top end of the vagina.", "synonyms": "canalis cervicis uteri&#124;caudal segment of uterus&#124;cervical canal&#124;cervical canal of uterus&#124;cervix&#124;cervix of uterus&#124;cervix uteri&#124;neck of uterus&#124;uterine cervix", "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}}] |
| EP11 | data/habitats/host_associated/uterus__a0e26d9f.yaml; Immediate parent, context only | supports | {"identifier": "habitatmech:GOLD.f736cbfbc5", "label": "Uterus", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0000995", "habitatmech:GOLD.abc827a582"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6125", "source_label": "Uterus", "source_path": "Host-associated &gt; Mammals: Human &gt; Reproductive system &gt; Uterus", "mapping_predicate": "skos:narrowMatch", "assertion_count": 1, "assertion_unit": "ORGANISM", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NARROW."}]} |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000002/graph; UBERON_0000002-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0000002", "target": "http://purl.obolibrary.org/obo/UBERON_0001560", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000002", "target": "http://purl.obolibrary.org/obo/UBERON_0005156", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000002", "target": "http://purl.obolibrary.org/obo/UBERON_0000995", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000002", "target": "http://purl.obolibrary.org/obo/UBERON_0000996", "uri": "http://purl.obolibrary.org/obo/RO_0002150", "label": "continuous with"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000002; UBERON_0000002.json | context_only | Current term identity, active status and definition: {"obo_id": "UBERON:0000002", "label": "uterine cervix", "is_obsolete": false, "description": ["Lower, narrow portion of the uterus where it joins with the top end of the vagina."]} |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000995/graph; UBERON_0000995-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0000995", "target": "http://purl.obolibrary.org/obo/UBERON_0013515", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000995", "target": "http://purl.obolibrary.org/obo/NCBITaxon_32525", "uri": "http://purl.obolibrary.org/obo/RO_0002162", "label": "in taxon"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000995", "target": "http://purl.obolibrary.org/obo/UBERON_0000922", "uri": "http://purl.obolibrary.org/obo/RO_0002202", "label": "develops from"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000995", "target": "http://purl.obolibrary.org/obo/UBERON_0004175", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000995", "target": "http://purl.obolibrary.org/obo/UBERON_0005795", "uri": "http://purl.obolibrary.org/obo/RO_0002202", "label": "develops from"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000995; UBERON_0000995.json | context_only | Current term identity, active status and definition: {"obo_id": "UBERON:0000995", "label": "uterus", "is_obsolete": false, "description": ["The female muscular organ of gestation in which the developing embryo or fetus is nourished until birth."]} |
| ESEARCH | Maintained inputs and review archive; rg --no-ignore --hidden -l -F -e habitatmech:GOLD.c15e1115f3 -e Cervix -e cervix -e habitatmech:GOLD.c15e1115f3 curation history research reports data/raw build reviews | context_only | Exact TSV rows parsed separately; broad label matches are leads, not all read. No earlier formal structured target observation. |

## Limits And Additional Notes

- Source counts, score channels and ranks do not establish prevalence, viability or characteristic presence. Original specimen-level and pair-level evidence has not been reconstructed exhaustively.
- Configured label validation skipped 2063 no-adapter pairs; displayed target TaxIds were resolved separately with current NCBI.
- Exact-base full QC is verified hosted evidence for unchanged scientific inputs, not a new local full-QC run or validation of these new review bundles.
- iModulonDB is not applicable: target claims do not assert genes, regulators or expression modules. No paid research or native status promotion.
- Native working-tree capture retained; input hashes additionally compared with exact base blobs 5fef9bb871a510550a3f70c45118805ac7c8d9a8.
- No previous structured target observation found in ignored-inclusive archive traversal. Historical prose is not a formal predecessor or automatic disposition.
- This immutable observation does not itself perform curation. Separately authorized PR remediation must retain its findings and lineage.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T021301Z-cervix-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: Cervix (habitatmech:GOLD.c15e1115f3)'
started_at: '2026-10-16T02:00:43Z'
finished_at: '2026-10-16T02:13:01Z'
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
summary: The human source is a host-scoped uterine cervix, with a valid generic cervix
  genus. Current Uberon explicitly relates cervix to uterus by part_of; whole human
  uterus is not a strictly broader class. Preserve 28 ORGANISM assertions separately
  from 127 supplemental biosamples and three study memberships, and do not equate
  the mucus medium with the anatomical site.
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
  - path: data/habitats/host_associated/cervix.yaml
    sha256: f03862d21b02598c47ed276a036dd006cb7de62f85efac8c8f2450179d83cd3c
    role: target
  - path: data/habitats/host_associated/uterus__a0e26d9f.yaml
    sha256: 6053e7077e3b8d1aab73f8a13ad5eb37571bf5467ddf0d24df9a20345f4a246a
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
- target_id: habitatmech:GOLD.c15e1115f3
  path: data/habitats/host_associated/cervix.yaml
  label: Cervix
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
  - habitatmech:GOLD.c15e1115f3
  exclusions:
  - target: Other records, original source specimens, SSSOM/KGX
    reason: Parent context does not expand target scope; exports and individual specimens
      are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/cervix.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.c15e1115f3
  summary: "Finished 2026-10-16T02:01:44Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/cervix.yaml"
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
  - habitatmech:GOLD.c15e1115f3
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
  - habitatmech:GOLD.c15e1115f3
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
  - habitatmech:GOLD.c15e1115f3
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
  - habitatmech:GOLD.c15e1115f3
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
  - habitatmech:GOLD.c15e1115f3
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
  - habitatmech:GOLD.c15e1115f3
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
  - habitatmech:GOLD.c15e1115f3
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
  - habitatmech:GOLD.c15e1115f3
  summary: Verified 2026-10-16T01:59:09Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38835150071
  scope_note: Unchanged scientific-input baseline only; new output bundles require
    separate validation.
- check_id: CREF
  name: Standalone citation validator applicability
  status: not_applicable
  required: false
  target_ids:
  - habitatmech:GOLD.c15e1115f3
  summary: No standalone citation checker documented for evidence-free generated targets.
    Stable references checked with native gates/current authorities; causal validation
    ran globally.
  scope_note: No invented command or exit code.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/cervix.yaml
  locator: Full target YAML
  accessed_at: '2026-10-16T02:13:00Z'
  support: supports
  summary: All fields and entire generated history read.
  snapshot_sha256: f03862d21b02598c47ed276a036dd006cb7de62f85efac8c8f2450179d83cd3c
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, parents, evidence and native status
  accessed_at: '2026-10-16T02:13:00Z'
  support: supports
  summary: All parent contributions must be strictly broader. Optional absence and
    native SEEDED status are not inherently defects.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: HabitatRecord, SourceAttestation, TaxonAssociation
  accessed_at: '2026-10-16T02:13:00Z'
  support: supports
  summary: Source mapping endpoints are source-to-record. Associations are not characteristic
    presence.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native source resolution and complete document reproduction
  accessed_at: '2026-10-16T02:13:00Z'
  support: supports
  summary: '[{"mint": "habitatmech:GOLD.c15e1115f3", "automatic": {"identifier": "habitatmech:GOLD.c15e1115f3",
    "grounding_status": "NARROW", "mapping_predicate": "skos:narrowMatch", "contributes_grounding":
    true, "extra_parents": ["UBERON:0000002"], "extra_xrefs": [], "route": "gold_narrower_than_leaf_match",
    "category": null, "reviewed": false, "decision": null}, "final": {"identifier":
    "habitatmech:GOLD.c15e1115f3", "grounding_status": "NARROW", "mapping_predicate":
    "skos:narrowMatch", "contributes_grounding": true, "extra_parents": ["UBERON:0000002"],
    "extra_xrefs": [], "route": "gold_narrower_than_leaf_match", "category": null,
    "reviewed": false, "decision": null}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: Source projections and count/rank/score interpretation
  accessed_at: '2026-10-16T02:13:00Z'
  support: supports
  summary: Exact source rows reproduce source-specific units, maximum scores and ranks.
    Frozen PREGO projection lacks original pair citation links.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Physical TSV rows 363
  accessed_at: '2026-10-16T02:13:00Z'
  support: supports
  summary: '[{"row": 363, "data": {"canonical_path": "Host-associated > Mammals: Human
    > Reproductive system > Uterus > Cervix", "ecosystem": "Host-associated", "ecosystem_category":
    "Mammals: Human", "ecosystem_type": "Reproductive system", "ecosystem_subtype":
    "Uterus", "specific_ecosystem": "Cervix", "leaf_label": "Cervix", "depth": "5",
    "gold_node_count": "1", "organism_count": "28", "study_count": "0", "biosample_count":
    "0", "total_assertions": "28", "gold_node_ids": "gold.ecosystem:6126"}}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: ET6
  kind: database
  reference: data/raw/gold_path_triads.tsv
  locator: Physical TSV rows 1493,1494,1495
  accessed_at: '2026-10-16T02:13:00Z'
  support: supports
  summary: '[{"row": 1493, "data": {"canonical_path": "Host-associated > Mammals:
    Human > Reproductive system > Uterus > Cervix", "slot": "broad", "samples": "1",
    "studies": "1", "distinct_terms": "1", "top_term": "ENVO:01001000", "top_label":
    "environmental system determined by an organism", "top_share": "1.00", "studies_agreeing":
    "1"}}, {"row": 1494, "data": {"canonical_path": "Host-associated > Mammals: Human
    > Reproductive system > Uterus > Cervix", "slot": "local", "samples": "1", "studies":
    "1", "distinct_terms": "1", "top_term": "UBERON:0000002", "top_label": "uterine
    cervix", "top_share": "1.00", "studies_agreeing": "1"}}, {"row": 1495, "data":
    {"canonical_path": "Host-associated > Mammals: Human > Reproductive system > Uterus
    > Cervix", "slot": "medium", "samples": "1", "studies": "1", "distinct_terms":
    "1", "top_term": "UBERON:0000316", "top_label": "cervical mucus", "top_share":
    "1.00", "studies_agreeing": "1"}}]'
  snapshot_sha256: b1717bd8fc4fdcd6a1a132f4eb32df3638b01ddf7d78f9a5797f110ee2b1e8d6
- evidence_id: ET7
  kind: database
  reference: data/raw/gold_path_biosamples.tsv
  locator: Physical TSV rows 198
  accessed_at: '2026-10-16T02:13:00Z'
  support: supports
  summary: '[{"row": 198, "data": {"canonical_path": "Host-associated > Mammals: Human
    > Reproductive system > Uterus > Cervix", "ecosystem_path_id": "6126", "biosample_count":
    "127"}}]'
  snapshot_sha256: 97cd7c8d0e731d07a85db6986dbcf9e49096a3c7988bd90a855599f492fe619e
- evidence_id: ET8
  kind: database
  reference: data/raw/gold_studies.tsv
  locator: Physical TSV rows 2262,3310,3623
  accessed_at: '2026-10-16T02:13:00Z'
  support: supports
  summary: '[{"row": 2262, "data": {"study_gold_id": "Gs0141904", "path_count": "2",
    "paths": "Host-associated > Mammals: Human > Reproductive system > Fallopian tubes|Host-associated
    > Mammals: Human > Reproductive system > Uterus > Cervix"}}, {"row": 3310, "data":
    {"study_gold_id": "Gs0150493", "path_count": "1", "paths": "Host-associated >
    Mammals: Human > Reproductive system > Uterus > Cervix"}}, {"row": 3623, "data":
    {"study_gold_id": "Gs0153705", "path_count": "1", "paths": "Host-associated >
    Mammals: Human > Reproductive system > Uterus > Cervix"}}]'
  snapshot_sha256: fa7aaa46f288d10c453bb723e6cf486cde646a003559414b5523cc3883a84c8c
- evidence_id: ET9
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: Physical TSV rows 10974,10975
  accessed_at: '2026-10-16T02:13:00Z'
  support: supports
  summary: '[{"row": 10974, "data": {"subject": "UBERON:0000002", "predicate": "rdfs:subClassOf",
    "object": "UBERON:0001560"}}, {"row": 10975, "data": {"subject": "UBERON:0000002",
    "predicate": "rdfs:subClassOf", "object": "UBERON:0005156"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET10
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 12869
  accessed_at: '2026-10-16T02:13:00Z'
  support: supports
  summary: '[{"row": 12869, "data": {"term_id": "UBERON:0000002", "ontology": "UBERON",
    "label": "uterine cervix", "definition": "Lower, narrow portion of the uterus
    where it joins with the top end of the vagina.", "synonyms": "canalis cervicis
    uteri|caudal segment of uterus|cervical canal|cervical canal of uterus|cervix|cervix
    of uterus|cervix uteri|neck of uterus|uterine cervix", "deprecated": "", "directly_referenced":
    "FALSE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EP11
  kind: record_content
  reference: data/habitats/host_associated/uterus__a0e26d9f.yaml
  locator: Immediate parent, context only
  accessed_at: '2026-10-16T02:13:00Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.f736cbfbc5", "label": "Uterus", "habitat_category":
    "HOST_ASSOCIATED", "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats":
    ["UBERON:0000995", "habitatmech:GOLD.abc827a582"], "source_attestations": [{"source":
    "GOLD", "source_id": "gold.ecosystem:6125", "source_label": "Uterus", "source_path":
    "Host-associated > Mammals: Human > Reproductive system > Uterus", "mapping_predicate":
    "skos:narrowMatch", "assertion_count": 1, "assertion_unit": "ORGANISM", "notes":
    "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}],
    "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources",
    "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories;
    attested by GOLD. Grounding: NARROW."}]}'
  snapshot_sha256: 6053e7077e3b8d1aab73f8a13ad5eb37571bf5467ddf0d24df9a20345f4a246a
- evidence_id: EX1
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000002/graph
  locator: UBERON_0000002-graph.json
  accessed_at: '2026-10-16T02:01:54Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0000002",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001560", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000002",
    "target": "http://purl.obolibrary.org/obo/UBERON_0005156", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000002",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000995", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000002",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000996", "uri": "http://purl.obolibrary.org/obo/RO_0002150",
    "label": "continuous with"}]'
  snapshot_sha256: d0828a5769039e8f1ab890673d29f9243ba67032f2ff1c1663ee1314fe3a356b
- evidence_id: EX2
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000002
  locator: UBERON_0000002.json
  accessed_at: '2026-10-16T02:01:54Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "UBERON:0000002",
    "label": "uterine cervix", "is_obsolete": false, "description": ["Lower, narrow
    portion of the uterus where it joins with the top end of the vagina."]}'
  snapshot_sha256: bf4eedc3d978556acdc7e7042c9617f7bbf8a848828de893fa098e507e734d5c
- evidence_id: EX3
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000995/graph
  locator: UBERON_0000995-graph.json
  accessed_at: '2026-10-16T02:02:00Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0000995",
    "target": "http://purl.obolibrary.org/obo/UBERON_0013515", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000995",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_32525", "uri": "http://purl.obolibrary.org/obo/RO_0002162",
    "label": "in taxon"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000995",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000922", "uri": "http://purl.obolibrary.org/obo/RO_0002202",
    "label": "develops from"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000995",
    "target": "http://purl.obolibrary.org/obo/UBERON_0004175", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000995",
    "target": "http://purl.obolibrary.org/obo/UBERON_0005795", "uri": "http://purl.obolibrary.org/obo/RO_0002202",
    "label": "develops from"}]'
  snapshot_sha256: 935144d2148f7a000eabbdfd443544c2860ec821d12a21f721559f8d2df3fc66
- evidence_id: EX4
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000995
  locator: UBERON_0000995.json
  accessed_at: '2026-10-16T02:01:59Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "UBERON:0000995",
    "label": "uterus", "is_obsolete": false, "description": ["The female muscular
    organ of gestation in which the developing embryo or fetus is nourished until
    birth."]}'
  snapshot_sha256: c958d0c579b97f45178811829d2a0f2af236879009c6ab1910a65f8dc573ef0e
- evidence_id: ESEARCH
  kind: search
  reference: Maintained inputs and review archive
  locator: rg --no-ignore --hidden -l -F -e habitatmech:GOLD.c15e1115f3 -e Cervix
    -e cervix -e habitatmech:GOLD.c15e1115f3 curation history research reports data/raw
    build reviews
  accessed_at: '2026-10-16T02:00:57Z'
  support: context_only
  summary: Exact TSV rows parsed separately; broad label matches are leads, not all
    read. No earlier formal structured target observation.
  search_scope: curation, history, research, reports, data/raw, build and reviews
    including hidden/ignored content; full structured YAML traversal.
assessments:
- assessment_id: A1
  area: identity
  topic: Identity, definition, aliases, source scope and hierarchy
  outcome: concern
  summary: The human source is a host-scoped uterine cervix, with a valid generic
    cervix genus. Current Uberon explicitly relates cervix to uterus by part_of; whole
    human uterus is not a strictly broader class. Preserve 28 ORGANISM assertions
    separately from 127 supplemental biosamples and three study memberships, and do
    not equate the mucus medium with the anatomical site.
  target_ids:
  - habitatmech:GOLD.c15e1115f3
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
  - ET9
  - ET10
  - EP11
  - EX1
  - EX2
  - EX3
  - EX4
- assessment_id: A2
  area: quantity
  topic: Counts, units, ranks and candidate pools
  outcome: supported
  summary: 'Frozen source rows reproduce every emitted count/unit and displayed taxon
    score/rank/pool. Zero tree counts are omitted; supplemental biosamples, triads
    and study membership are nonadditive. {"assertions": [{"source": "GOLD", "count":
    28, "unit": "ORGANISM", "row": {"row": 363, "data": {"canonical_path": "Host-associated
    > Mammals: Human > Reproductive system > Uterus > Cervix", "ecosystem": "Host-associated",
    "ecosystem_category": "Mammals: Human", "ecosystem_type": "Reproductive system",
    "ecosystem_subtype": "Uterus", "specific_ecosystem": "Cervix", "leaf_label": "Cervix",
    "depth": "5", "gold_node_count": "1", "organism_count": "28", "study_count": "0",
    "biosample_count": "0", "total_assertions": "28", "gold_node_ids": "gold.ecosystem:6126"}}}],
    "taxa": []}'
  target_ids:
  - habitatmech:GOLD.c15e1115f3
  evidence_ids:
  - E1
  - EEXTRACT
  - ESEED
  - EX1
  - EX2
  - EX3
  - EX4
- assessment_id: A3
  area: completeness
  topic: Native status and optional evidence
  outcome: supported
  summary: Executed native resolution reproduces NARROW/SEEDED. No environmental parameters,
    causal graphs, discussions, datasets or characteristic-presence claims are asserted.
    Missing optional fields do not authorize invented content. Parent mechanisms are
    not inherited.
  target_ids:
  - habitatmech:GOLD.c15e1115f3
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
  - habitatmech:GOLD.c15e1115f3
  evidence_ids:
  - E1
  - ERULE
findings:
- finding_id: F1
  issue_key: cervix-context-parent
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Source context is not a broader habitat class
  description: The human source is a host-scoped uterine cervix, with a valid generic
    cervix genus. Current Uberon explicitly relates cervix to uterus by part_of; whole
    human uterus is not a strictly broader class. Preserve 28 ORGANISM assertions
    separately from 127 supplemental biosamples and three study memberships, and do
    not equate the mucus medium with the anatomical site. Exclude only the exact GOLD
    source path contribution to habitatmech:GOLD.f736cbfbc5, preserving independently
    valid parents and all source provenance.
  target_ids:
  - habitatmech:GOLD.c15e1115f3
  field_paths:
  - parent_habitats
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
  - ET9
  - ET10
  - EP11
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
  issue_key: cervix-mapping-endpoint-contract
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Mapping uses an undeclared ontology-parent endpoint
  description: 'The executed route keeps the source mint but emits narrowMatch relative
    to its ontology parent; SourceAttestation instead declares source-to-record endpoints.
    Reconcile schema, producer and actual consumers under #1398. This is not a formal
    SKOS self-link prohibition, not solved by a blind predicate reversal, and not
    an SSSOM/KGX certification.'
  target_ids:
  - habitatmech:GOLD.c15e1115f3
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
  - ET8
  - ET9
  - ET10
  - EP11
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
  - habitatmech:GOLD.c15e1115f3
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: The human source is a host-scoped uterine cervix, with a valid generic
    cervix genus. Current Uberon explicitly relates cervix to uterus by part_of; whole
    human uterus is not a strictly broader class. Preserve 28 ORGANISM assertions
    separately from 127 supplemental biosamples and three study memberships, and do
    not equate the mucus medium with the anatomical site. Exclude only the exact GOLD
    source path contribution to habitatmech:GOLD.f736cbfbc5, preserving independently
    valid parents and all source provenance. No repair is performed by this review.
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
  - habitatmech:GOLD.c15e1115f3
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  description: 'The executed route keeps the source mint but emits narrowMatch relative
    to its ontology parent; SourceAttestation instead declares source-to-record endpoints.
    Reconcile schema, producer and actual consumers under #1398. This is not a formal
    SKOS self-link prohibition, not solved by a blind predicate reversal, and not
    an SSSOM/KGX certification. No repair is performed by this review.'
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
