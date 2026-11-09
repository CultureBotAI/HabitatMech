# Remediation review: extracellular

- Review: 20261107T050007Z-extracellular-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-07T04:55:00Z
- Finished UTC: 2026-11-07T05:00:07Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Updated curation/term_requests.tsv and curation/term_requests/envo_robot_template.tsv for habitatmech:GOLD.0a69f87c03 to parent_id ENVO:01001055 (environment associated with an animal part or small animal) with parent_mode REPLACE (#2304), replacing whole-structure parent UBERON:3010636 (egg capsule). Identity (habitatmech:GOLD.0a69f87c03, 'annelid egg capsule albuminous fluid'), native REVIEWED/UNGROUNDED status, and source observations are preserved. No unresolved predecessor finding remains in this target scope.

## Scope And Provenance

Full current target assessment and explicit disposition of every baseline finding on data/habitats/host_associated/extracellular.yaml after bounded Cycle 6 Stage 5 remediation.

Selection: One of twenty-two repaired targets from the excretory_system__22ee753c-through-fecal cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 30fbe25f4c539ad6266dae7680d21e451caf6e40.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.0a69f87c03 | data/habitats/host_associated/extracellular.yaml | generated | annelid egg capsule albuminous fluid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.0a69f87c03 | Completed 2026-11-07T04:58:12Z. No issues found. |
| validate-strict | passed | True | habitatmech:GOLD.0a69f87c03 | Completed 2026-11-07T04:58:18Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | habitatmech:GOLD.0a69f87c03 | Completed 2026-11-07T04:59:00Z. No issues found; 868 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | habitatmech:GOLD.0a69f87c03 | Completed 2026-11-07T04:59:05Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | habitatmech:GOLD.0a69f87c03 | Completed 2026-11-07T04:59:10Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | habitatmech:GOLD.0a69f87c03 | Completed 2026-11-07T04:59:12Z. validated 83 causal-graph curation file(s) with 83 graph(s). |
| term-requests-check | passed | True | habitatmech:GOLD.0a69f87c03 | Completed 2026-11-07T04:59:15Z. term-request table is current (671 terms). |
| validate-products | passed | True | habitatmech:GOLD.0a69f87c03 | Completed 2026-11-07T04:59:20Z. OK_CANONICAL: 1203, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2084. All id&lt;-&gt;label pairs correspond. |
| pytest counterfactual review repairs | passed | True | habitatmech:GOLD.0a69f87c03 | Completed 2026-11-07T04:59:30Z. 2 passed; exact 22-record counterfactual diff verified. |
| curation-floor | passed | True | habitatmech:GOLD.0a69f87c03 | Completed 2026-11-07T04:59:35Z. Floor satisfied across all 13 metrics. |
| render-check | passed | True | habitatmech:GOLD.0a69f87c03 | Completed 2026-11-07T04:59:50Z. rendered 3209 habitat pages, 750 redirect stubs, 8 categories, 696 term requests; pages/ is in step with the corpus. |

## Scientific And Domain Assessments

### Native validity and reproduction after bounded remediation

schema: supported. Targets: habitatmech:GOLD.0a69f87c03.

Individual schema, strict 24-target validation, 868 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 83 causal overlays, 671 term requests, curation floor, site parity, and counterfactual regression tests passed.

### Identity, definition, hierarchy and aliases

identity: supported. Targets: habitatmech:GOLD.0a69f87c03.

habitatmech:GOLD.0a69f87c03: annelid egg capsule albuminous fluid; UNGROUNDED/REVIEWED; parents ["ENVO:01001055"]. Updated curation/term_requests.tsv and curation/term_requests/envo_robot_template.tsv for habitatmech:GOLD.0a69f87c03 to parent_id ENVO:01001055 (environment associated with an animal part or small animal) with parent_mode REPLACE (#2304), replacing whole-structure parent UBERON:3010636 (egg capsule). Identity (habitatmech:GOLD.0a69f87c03, 'annelid egg capsule albuminous fluid'), native REVIEWED/UNGROUNDED status, and source observations are preserved. No unresolved predecessor finding remains in this target scope.

### Source counts and retained ranking

quantity: supported. Targets: habitatmech:GOLD.0a69f87c03.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"source": "GOLD", "count": null, "unit": null}]. Zero counts are omitted; unrelated parent counts are not combined.

### Predecessor finding reconciliation

representation: supported. Targets: habitatmech:GOLD.0a69f87c03.

Every predecessor finding preserves its stable issue_key and exact lineage. All predecessor findings in this target scope are resolved.

### Parameters, mechanisms and native status

completeness: supported. Targets: habitatmech:GOLD.0a69f87c03.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only review does not mutate generated records.

## Findings

### F1: Annelid egg capsule albuminous fluid asserts protective membrane UBERON:3010636 (egg capsule) as a superclass

major / resolved / confirmed; issue key: extracellular-context-parent.

Update curation/term_requests.tsv row 478 for habitatmech:GOLD.0a69f87c03 ('annelid egg capsule albuminous fluid') to use parent_id ENVO:01001055 (environment associated with an animal part or small animal) with parent_mode REPLACE (and update the definition genus accordingly), matching sibling extracellular__3f7afaf4 (habitatmech:GOLD.6c8238add0).

Disposition: Updated curation/term_requests.tsv and curation/term_requests/envo_robot_template.tsv for habitatmech:GOLD.0a69f87c03 to parent_id ENVO:01001055 (environment associated with an animal part or small animal) with parent_mode REPLACE (#2304), replacing whole-structure parent UBERON:3010636 (egg capsule).

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/extracellular.yaml; Entire YAML | supports | {"identifier": "habitatmech:GOLD.0a69f87c03", "label": "annelid egg capsule albuminous fluid", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED", "parent_habitats": ["ENVO:01001055"], "synonyms": [{"synonym_text": "earthworm cocoon extracellular fluid", "synonym_type": "EXACT_SYNONYM", "source": "HabitatMech curation"}], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:4332", "source_label": "Extracellular", "source_path": "Host-associated &gt; Annelida &gt; Reproductive system &gt; Egg capsule &gt; Extracellular"}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED."}, {"timestamp": "2026-10-17T00:00:00Z", "curator": "antigravity", "action": "CONFIRM_UNGROUNDED", "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. ITEM curation: GOLD 'Host-associated &gt; Annelida &gt; Reproductive system &gt; Egg capsule &gt; Extracellular' denotes the extracellular fluid compartment inside an annelid egg capsule/cocoon (PMID 18480259; DOI:10.1128/AEM.00126-08). Path: Host-associated &gt; Annelida &gt; Reproductive system &gt; Egg capsule &gt; Extracellular (source concept habitatmech:GOLD.0a69f87c03)"}, {"timestamp": "2026-10-17T00:00:00Z", "curator": "antigravity", "action": "DEFINED", "changes": "Defined as 'annelid egg capsule albuminous fluid' under ENVO:01001055 'environment associated with an animal part or small animal'. ITEM curation: GOLD 'Host-associated &gt; Annelida &gt; Reproductive system &gt; Egg capsule &gt; Extracellular' denotes the extracellular fluid compartment inside an annelid egg capsule/cocoon (PMID 18480259; DOI:10.1128/AEM.00126-08). Path: Host-associated &gt; Annelida &gt; Reproductive system &gt; Egg capsule &gt; Extracellular; parent_mode REPLACE under ENVO:01001055 excludes protective capsule parent Egg capsule (https://github.com/CultureBotAI/HabitatMech/issues/2304)."}, {"timestamp": "2026-10-17T00:00:00Z", "curator": "antigravity", "action": "SOURCE_SYNONYM_EXCLUDED", "changes": "Omitted automatic retention of displaced source label 'Extracellular' when defining habitatmech:GOLD.0a69f87c03 as 'annelid egg capsule albuminous fluid'. Verbatim source attestations are preserved. Displaced GOLD source label 'Extracellular' in path 'Host-associated &gt; Annelida &gt; Reproductive system &gt; Egg capsule &gt; Extracellular' is context-dependent, ambiguous, or names a host/disease/process rather than the defined habitat 'annelid egg capsule albuminous fluid'; suppress automatic exact-synonym retention while preserving verbatim source provenance."}]} |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=habitatmech:GOLD.0a69f87c03, grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["ENVO:01001055"]. |
| ESIB1 | data/habitats/host_associated/extracellular__3f7afaf4.yaml; Entire YAML | supports | Sibling GOLD Extracellular record habitatmech:GOLD.6c8238add0 (molluscan gill extracellular environment) defined under ENVO:01001055 (environment associated with an animal part or small animal) with parent_mode REPLACE in curation/term_requests.tsv. |
| EGOLD | data/raw/gold_ecosystem_paths.tsv; TSV rows 1751 | supports | [{"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Annelida &gt; Reproductive system &gt; Egg capsule &gt; Extracellular", "depth": "5", "ecosystem": "Host-associated", "ecosystem_category": "Annelida", "ecosystem_subtype": "Egg capsule", "ecosystem_type": "Reproductive system", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:4332", "leaf_label": "Extracellular", "organism_count": "0", "specific_ecosystem": "Extracellular", "study_count": "0", "total_assertions": "0"}, "row": 1751}] |
| EGROUND | data/raw/isolation_source_groundings.tsv; TSV rows 108 | supports | [{"data": {"confidence": "high", "curator": "kg_review_promote", "mapping_justification": "semapv:ManualMappingCuration", "object_id": "GO:0005615", "object_label": "extracellular space", "object_source": "GO", "predicate_id": "skos:exactMatch", "source_dataset": "bacdive", "subject_label": "Extracellular", "subject_label_normalized": "extracellular", "verified_date": "2026-05-02"}, "row": 108}] |
| EONT | data/raw/ontology_terms.tsv; TSV rows 8544,13523 | supports | [{"data": {"definition": "An environmental system determined by part of a living or dead animal, or a whole small animal.", "deprecated": "", "directly_referenced": "FALSE", "label": "environment associated with an animal part or small animal", "label_only": "FALSE", "ontology": "ENVO", "synonyms": "", "term_id": "ENVO:01001055"}, "row": 8544}, {"data": {"definition": "Protective membranes that surround amphibian embryos.", "deprecated": "", "directly_referenced": "FALSE", "label": "egg capsule", "label_only": "FALSE", "ontology": "UBERON", "synonyms": "", "term_id": "UBERON:3010636"}, "row": 13523}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 6861,6993,7705,11847,11848 | supports | [{"data": {"object": "ENVO:01001110", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001055"}, "row": 6861}, {"data": {"object": "ENVO:01001055", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001176"}, "row": 6993}, {"data": {"object": "ENVO:01001055", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001829"}, "row": 7705}, {"data": {"object": "UBERON:0000476", "predicate": "rdfs:subClassOf", "subject": "UBERON:3010636"}, "row": 11847}, {"data": {"object": "UBERON:0000478", "predicate": "rdfs:subClassOf", "subject": "UBERON:3010636"}, "row": 11848}] |
| EDEC | curation/decisions.tsv; TSV line 174 | supports | [[174, "habitatmech:GOLD.0a69f87c03\tCONFIRM_UNGROUNDED\t\t\t\tantigravity\t2026-10-17\tITEM curation: GOLD 'Host-associated &gt; Annelida &gt; Reproductive system &gt; Egg capsule &gt; Extracellular' denotes the extracellular fluid compartment inside an annelid egg capsule/cocoon (PMID 18480259; DOI:10.1128/AEM.00126-08). Path: Host-associated &gt; Annelida &gt; Reproductive system &gt; Egg capsule &gt; Extracellular\tITEM\t\t"]] |
| ETR | curation/term_requests.tsv; TSV line 478 | supports | [[478, "habitatmech:GOLD.0a69f87c03\tannelid egg capsule albuminous fluid\tENVO:01001055\tenvironment associated with an animal part or small animal\tAn environment associated with an animal part or small animal consisting of the extracellular nutritive albuminous fluid inside an annelid cocoon (such as an earthworm or leech egg capsule), where vertically transmitted bacterial symbionts proliferate before colonizing developing embryos.\tearthworm cocoon extracellular fluid\tantigravity\t2026-10-17\tITEM curation: GOLD 'Host-associated &gt; Annelida &gt; Reproductive system &gt; Egg capsule &gt; Extracellular' denotes the extracellular fluid compartment inside an annelid egg capsule/cocoon (PMID 18480259; DOI:10.1128/AEM.00126-08). Path: Host-associated &gt; Annelida &gt; Reproductive system &gt; Egg capsule &gt; Extracellular; parent_mode REPLACE under ENVO:01001055 excludes protective capsule parent Egg capsule (https://github.com/CultureBotAI/HabitatMech/issues/2304).\tREPLACE"]] |
| ELE | curation/definition_source_label_exclusions.tsv; TSV rows 249 | supports | [{"data": {"curator": "antigravity", "date": "2026-10-17", "identifier": "habitatmech:GOLD.0a69f87c03", "notes": "Displaced GOLD source label 'Extracellular' in path 'Host-associated &gt; Annelida &gt; Reproductive system &gt; Egg capsule &gt; Extracellular' is context-dependent, ambiguous, or names a host/disease/process rather than the defined habitat 'annelid egg capsule albuminous fluid'; suppress automatic exact-synonym retention while preserving verbatim source provenance.", "requested_label": "annelid egg capsule albuminous fluid", "source_label": "Extracellular"}, "row": 249}] |
| EP1 | data/habitats/host_associated/egg_capsule.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": "Protective membranes that surround amphibian embryos.", "grounding_status": "EXACT", "identifier": "UBERON:3010636", "label": "egg capsule", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0000476", "UBERON:0000478"], "source_attestations": [{"mapping_predicate": "skos:exactMatch", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:3892", "source_label": "Egg capsule", "source_path": "Host-associated &gt; Annelida &gt; Reproductive system &gt; Egg capsule"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'extracellular&#124;habitatmech:GOLD.0a69f87c03' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal located Stage 4 predecessor bundle 20261106T194817Z-extracellular-record (linked via EPREV and related_reviews) and checked related cohort and ancestor reviews for reconciliation. |
| EPREV | reviews/structured/20261106T194817Z-extracellular-record/review.yaml; Every immutable Stage 4 baseline finding | supports | Exact predecessor keys and findings reconciled; original inspected source scope preserved. |
| ETEST | tests/test_excretory_system_22ee753c_to_fecal_review_repairs.py; Complete full-corpus counterfactual regression suite | supports | Exactly twenty-two records differ from the counterfactual baseline across Issues #2304 and #2305. |
| EHIST_G1 | history/other/gold_parent_exclusions/2026-11-07T045500Z-antigravity-230401.yaml; Complete curation session history event | supports | Authorized curation event for Issue #2304 recorded and validated. |

## Limits And Additional Notes

- Only the stated primary evidence and current ontology/taxonomy authorities were independently inspected; original specimen-level support for every source-bin member is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism or characteristic presence. Parent observations are not inherited by children.
- Configured label correspondence skipped 2,084 no-adapter pairs; this is not whole-corpus identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in this pre-save observation.
- iModulonDB is not applicable: the target has no gene, regulator or expression-module assertion. No paid research or scientific-status promotion was performed.
- Saved against working-tree repairs atop main commit 30fbe25f4c539ad6266dae7680d21e451caf6e40; all earlier saved bundles in reviews/structured/ remain byte-identical.
- Reconciles predecessor bundle 20261106T194817Z-extracellular-record with exact issue_key and previous_occurrences lineage.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261107T050007Z-extracellular-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: extracellular'
started_at: '2026-11-07T04:55:00Z'
finished_at: '2026-11-07T05:00:07Z'
reviewer:
  identity: antigravity
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Same agent inspected the full target and source evidence; not
    independent human or second-agent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Updated curation/term_requests.tsv and curation/term_requests/envo_robot_template.tsv
  for habitatmech:GOLD.0a69f87c03 to parent_id ENVO:01001055 (environment associated
  with an animal part or small animal) with parent_mode REPLACE (#2304), replacing
  whole-structure parent UBERON:3010636 (egg capsule). Identity (habitatmech:GOLD.0a69f87c03,
  'annelid egg capsule albuminous fluid'), native REVIEWED/UNGROUNDED status, and
  source observations are preserved. No unresolved predecessor finding remains in
  this target scope.
source:
  git_revision: 30fbe25f4c539ad6266dae7680d21e451caf6e40
  state: working_tree
  inputs:
  - path: curation/decisions.tsv
    sha256: 7e0e28eeca775e7795d3f72384794f392fcf287f7f972fa57042234a64d3ce40
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 596d59ab03fafa4c1fcdcb6446c87b7c72c04305e9d516047e661060710e86d4
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 913f1ece5224bbed33b736f78cc8e1244155e91f390fe8e790d6f91a24b3b796
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: c1207270bb0ae2031e42de6cb8220b20f98886f65e40d48793bfd7e9d757d83a
    role: context
  - path: curation/term_requests.tsv
    sha256: f86df360f54cb00d3062ae27a9196828113219c06cfd9cfc9830a0e08603d069
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/host_associated/egg_capsule.yaml
    sha256: 7986a368cd50dd2bc20d7c8dc66ab0e6a954a7a4b9a5c5f672ce2f59a9089e8d
    role: context
  - path: data/habitats/host_associated/extracellular.yaml
    sha256: 95012e93e796bb1a19eddc307da317ef7e07cb14c18d9cdefb982fb9962247ed
    role: target
  - path: data/habitats/host_associated/extracellular__3f7afaf4.yaml
    sha256: e5017a4c3736700b024f6af281f1933b438ee68199d1c81e85a9d7d59266d838
    role: context
  - path: data/raw/bacdive_isolation_sources.tsv
    sha256: fb1645dd899a43130be9cf38b0e8b27ffbaa0175306917bff20e20ee225875fc
    role: context
  - path: data/raw/gold_ecosystem_paths.tsv
    sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
    role: context
  - path: data/raw/isolation_source_groundings.tsv
    sha256: ab6a997359aab961c40928f9b13e06adb6dc43124fa3de821819570dd87f43b8
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
  - path: history/other/definition_source_label_exclusions/2026-11-07T045510Z-antigravity-230501.yaml
    sha256: 16115355944b03d6e09142bca848ee5d52d3ab9332e2367433aebb6177da314c
    role: context
  - path: history/other/gold_parent_exclusions/2026-11-07T045500Z-antigravity-230401.yaml
    sha256: d55f782e57e1c75b9485ba0c5e39260dfcbaed7532af9a7fc30c3316874efac9
    role: context
  - path: reviews/structured/20261106T194817Z-extracellular-record/review.yaml
    sha256: 46602629be3bc2dfd9c57ff8846950a6d8213177e485b0d60ee4bfb067c002cf
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
    role: context
  - path: src/habitatmech/seed.py
    sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
    role: context
  - path: tests/test_excretory_system_22ee753c_to_fecal_review_repairs.py
    sha256: 90bb097e6a2311fbaf0a2afadc4ca7642581bab11e5dd3d582ea5cd149c066f6
    role: context
targets:
- target_id: habitatmech:GOLD.0a69f87c03
  path: data/habitats/host_associated/extracellular.yaml
  label: annelid egg capsule albuminous fluid
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
    path: curation/term_requests_excluded.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
scope:
  description: Full current target assessment and explicit disposition of every baseline
    finding on data/habitats/host_associated/extracellular.yaml after bounded Cycle
    6 Stage 5 remediation.
  selection: One of twenty-two repaired targets from the excretory_system__22ee753c-through-fecal
    cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.0a69f87c03
  exclusions:
  - target: Other habitat records and SSSOM/KGX products
    reason: Direct parents and siblings inform hierarchy/synonym interpretation but
      are not additional completed reviews; exports are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: .venv/bin/python -m linkml.validator.cli -s src/habitatmech/schema/habitatmech.yaml
    --target-class HabitatRecord data/habitats/host_associated/extracellular.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.0a69f87c03
  summary: Completed 2026-11-07T04:58:12Z. No issues found.
  scope_note: Individual schema; strict command covers the 24 named cohort targets;
    other documented gates have full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/habitats/host_associated/excretory_system__22ee753c.yaml
    data/habitats/host_associated/excretory_system__37f93bb9.yaml data/habitats/host_associated/exoskeleton.yaml
    data/habitats/host_associated/external_genitalia.yaml data/habitats/host_associated/external_organs.yaml
    data/habitats/host_associated/external_organs__aed6edb3.yaml data/habitats/host_associated/external_soft_tissue_zone.yaml
    data/habitats/host_associated/extracellular.yaml data/habitats/host_associated/extracellular__3f7afaf4.yaml
    data/habitats/host_associated/extracellular_symbionts.yaml data/habitats/host_associated/eye.yaml
    data/habitats/host_associated/eye__59a4c665.yaml data/habitats/host_associated/eye__810dedbb.yaml
    data/habitats/host_associated/eye_ciliary_body.yaml data/habitats/host_associated/eye_ciliary_body__832768c5.yaml
    data/habitats/host_associated/eye_vitreous_chamber.yaml data/habitats/host_associated/eye_vitreous_chamber__b4eddfc1.yaml
    data/habitats/host_associated/fallopian_tubes.yaml data/habitats/host_associated/fallopian_tubes__c41e0038.yaml
    data/habitats/host_associated/fascia.yaml data/habitats/host_associated/fascia__1f6c9c1a.yaml
    data/habitats/host_associated/fat_body.yaml data/habitats/host_associated/feather.yaml
    data/habitats/host_associated/fecal.yaml --out /tmp/c6s4_24_strict.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.0a69f87c03
  summary: 'Completed 2026-11-07T04:58:18Z. Validated 24 files; files with ERROR:
    0; total ERROR rows: 0.'
  scope_note: Closed-schema strict validation across all 24 cohort target files (and
    3,209 full-corpus files).
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_history.py history
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.0a69f87c03
  summary: Completed 2026-11-07T04:59:00Z. No issues found; 868 history record(s)
    valid against src/habitatmech/schema/history.yaml.
  scope_note: Full-corpus curation history validation.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: .venv/bin/python scripts/check_provenance.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.0a69f87c03
  summary: 'Completed 2026-11-07T04:59:05Z. provenance current: 14 committed inventories,
    2 GOLD sources.'
  scope_note: Full-corpus raw inventory provenance verification.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: .venv/bin/python scripts/verify_corpus.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.0a69f87c03
  summary: 'Completed 2026-11-07T04:59:10Z. expected 3209 records, found 3209 on disk;
    missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/.'
  scope_note: Full-corpus deterministic reproduction from raw inventories and curation
    tables.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_causal_graph_curations.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.0a69f87c03
  summary: Completed 2026-11-07T04:59:12Z. validated 83 causal-graph curation file(s)
    with 83 graph(s).
  scope_note: Full-corpus causal-graph overlay validation.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: .venv/bin/python scripts/build_term_requests.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.0a69f87c03
  summary: Completed 2026-11-07T04:59:15Z. term-request table is current (671 terms).
  scope_note: Full-corpus term-request table currency check.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.0a69f87c03
  summary: 'Completed 2026-11-07T04:59:20Z. OK_CANONICAL: 1203, OK_SYNONYM: 1, OK_EXCEPTION:
    5, SKIPPED_NO_ADAPTER: 2084. All id<->label pairs correspond.'
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
- check_id: C9
  name: pytest counterfactual review repairs
  status: passed
  required: true
  command: .venv/bin/python -m pytest tests/test_excretory_system_22ee753c_to_fecal_review_repairs.py
    -q --no-cov
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.0a69f87c03
  summary: Completed 2026-11-07T04:59:30Z. 2 passed; exact 22-record counterfactual
    diff verified.
  scope_note: 'Full-corpus counterfactual regression test for Issues #2304 and #2305.'
- check_id: C10
  name: curation-floor
  status: passed
  required: true
  command: .venv/bin/python scripts/check_curation_floor.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.0a69f87c03
  summary: Completed 2026-11-07T04:59:35Z. Floor satisfied across all 13 metrics.
  scope_note: Full-corpus curation floor ratchets.
- check_id: C11
  name: render-check
  status: passed
  required: true
  command: .venv/bin/python scripts/render_pages.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.0a69f87c03
  summary: Completed 2026-11-07T04:59:50Z. rendered 3209 habitat pages, 750 redirect
    stubs, 8 categories, 696 term requests; pages/ is in step with the corpus.
  scope_note: Full-corpus static site parity check.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/extracellular.yaml
  locator: Entire YAML
  accessed_at: '2026-11-07T05:00:07Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.0a69f87c03", "label": "annelid egg capsule
    albuminous fluid", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED",
    "parent_habitats": ["ENVO:01001055"], "synonyms": [{"synonym_text": "earthworm
    cocoon extracellular fluid", "synonym_type": "EXACT_SYNONYM", "source": "HabitatMech
    curation"}], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:4332",
    "source_label": "Extracellular", "source_path": "Host-associated > Annelida >
    Reproductive system > Egg capsule > Extracellular"}], "curation_history": [{"timestamp":
    "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES",
    "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED."},
    {"timestamp": "2026-10-17T00:00:00Z", "curator": "antigravity", "action": "CONFIRM_UNGROUNDED",
    "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. ITEM curation:
    GOLD ''Host-associated > Annelida > Reproductive system > Egg capsule > Extracellular''
    denotes the extracellular fluid compartment inside an annelid egg capsule/cocoon
    (PMID 18480259; DOI:10.1128/AEM.00126-08). Path: Host-associated > Annelida >
    Reproductive system > Egg capsule > Extracellular (source concept habitatmech:GOLD.0a69f87c03)"},
    {"timestamp": "2026-10-17T00:00:00Z", "curator": "antigravity", "action": "DEFINED",
    "changes": "Defined as ''annelid egg capsule albuminous fluid'' under ENVO:01001055
    ''environment associated with an animal part or small animal''. ITEM curation:
    GOLD ''Host-associated > Annelida > Reproductive system > Egg capsule > Extracellular''
    denotes the extracellular fluid compartment inside an annelid egg capsule/cocoon
    (PMID 18480259; DOI:10.1128/AEM.00126-08). Path: Host-associated > Annelida >
    Reproductive system > Egg capsule > Extracellular; parent_mode REPLACE under ENVO:01001055
    excludes protective capsule parent Egg capsule (https://github.com/CultureBotAI/HabitatMech/issues/2304)."},
    {"timestamp": "2026-10-17T00:00:00Z", "curator": "antigravity", "action": "SOURCE_SYNONYM_EXCLUDED",
    "changes": "Omitted automatic retention of displaced source label ''Extracellular''
    when defining habitatmech:GOLD.0a69f87c03 as ''annelid egg capsule albuminous
    fluid''. Verbatim source attestations are preserved. Displaced GOLD source label
    ''Extracellular'' in path ''Host-associated > Annelida > Reproductive system >
    Egg capsule > Extracellular'' is context-dependent, ambiguous, or names a host/disease/process
    rather than the defined habitat ''annelid egg capsule albuminous fluid''; suppress
    automatic exact-synonym retention while preserving verbatim source provenance."}]}'
  snapshot_sha256: 95012e93e796bb1a19eddc307da317ef7e07cb14c18d9cdefb982fb9962247ed
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-07T05:00:07Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon terms cannot substitute
    for associated environments; parent_habitats must be strictly broader across all
    contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-07T05:00:07Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-07T05:00:07Z'
  support: supports
  summary: Seed generator produces identifier=habitatmech:GOLD.0a69f87c03, grounding_status=UNGROUNDED,
    mapping_status=REVIEWED, parent_habitats=["ENVO:01001055"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: ESIB1
  kind: record_content
  reference: data/habitats/host_associated/extracellular__3f7afaf4.yaml
  locator: Entire YAML
  accessed_at: '2026-11-07T05:00:07Z'
  support: supports
  summary: Sibling GOLD Extracellular record habitatmech:GOLD.6c8238add0 (molluscan
    gill extracellular environment) defined under ENVO:01001055 (environment associated
    with an animal part or small animal) with parent_mode REPLACE in curation/term_requests.tsv.
  snapshot_sha256: e5017a4c3736700b024f6af281f1933b438ee68199d1c81e85a9d7d59266d838
- evidence_id: EGOLD
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV rows 1751
  accessed_at: '2026-11-07T05:00:07Z'
  support: supports
  summary: '[{"data": {"biosample_count": "0", "canonical_path": "Host-associated
    > Annelida > Reproductive system > Egg capsule > Extracellular", "depth": "5",
    "ecosystem": "Host-associated", "ecosystem_category": "Annelida", "ecosystem_subtype":
    "Egg capsule", "ecosystem_type": "Reproductive system", "gold_node_count": "1",
    "gold_node_ids": "gold.ecosystem:4332", "leaf_label": "Extracellular", "organism_count":
    "0", "specific_ecosystem": "Extracellular", "study_count": "0", "total_assertions":
    "0"}, "row": 1751}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: EGROUND
  kind: database
  reference: data/raw/isolation_source_groundings.tsv
  locator: TSV rows 108
  accessed_at: '2026-11-07T05:00:07Z'
  support: supports
  summary: '[{"data": {"confidence": "high", "curator": "kg_review_promote", "mapping_justification":
    "semapv:ManualMappingCuration", "object_id": "GO:0005615", "object_label": "extracellular
    space", "object_source": "GO", "predicate_id": "skos:exactMatch", "source_dataset":
    "bacdive", "subject_label": "Extracellular", "subject_label_normalized": "extracellular",
    "verified_date": "2026-05-02"}, "row": 108}]'
  snapshot_sha256: ab6a997359aab961c40928f9b13e06adb6dc43124fa3de821819570dd87f43b8
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 8544,13523
  accessed_at: '2026-11-07T05:00:07Z'
  support: supports
  summary: '[{"data": {"definition": "An environmental system determined by part of
    a living or dead animal, or a whole small animal.", "deprecated": "", "directly_referenced":
    "FALSE", "label": "environment associated with an animal part or small animal",
    "label_only": "FALSE", "ontology": "ENVO", "synonyms": "", "term_id": "ENVO:01001055"},
    "row": 8544}, {"data": {"definition": "Protective membranes that surround amphibian
    embryos.", "deprecated": "", "directly_referenced": "FALSE", "label": "egg capsule",
    "label_only": "FALSE", "ontology": "UBERON", "synonyms": "", "term_id": "UBERON:3010636"},
    "row": 13523}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 6861,6993,7705,11847,11848
  accessed_at: '2026-11-07T05:00:07Z'
  support: supports
  summary: '[{"data": {"object": "ENVO:01001110", "predicate": "rdfs:subClassOf",
    "subject": "ENVO:01001055"}, "row": 6861}, {"data": {"object": "ENVO:01001055",
    "predicate": "rdfs:subClassOf", "subject": "ENVO:01001176"}, "row": 6993}, {"data":
    {"object": "ENVO:01001055", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001829"},
    "row": 7705}, {"data": {"object": "UBERON:0000476", "predicate": "rdfs:subClassOf",
    "subject": "UBERON:3010636"}, "row": 11847}, {"data": {"object": "UBERON:0000478",
    "predicate": "rdfs:subClassOf", "subject": "UBERON:3010636"}, "row": 11848}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EDEC
  kind: database
  reference: curation/decisions.tsv
  locator: TSV line 174
  accessed_at: '2026-11-07T05:00:07Z'
  support: supports
  summary: '[[174, "habitatmech:GOLD.0a69f87c03\tCONFIRM_UNGROUNDED\t\t\t\tantigravity\t2026-10-17\tITEM
    curation: GOLD ''Host-associated > Annelida > Reproductive system > Egg capsule
    > Extracellular'' denotes the extracellular fluid compartment inside an annelid
    egg capsule/cocoon (PMID 18480259; DOI:10.1128/AEM.00126-08). Path: Host-associated
    > Annelida > Reproductive system > Egg capsule > Extracellular\tITEM\t\t"]]'
  snapshot_sha256: 7e0e28eeca775e7795d3f72384794f392fcf287f7f972fa57042234a64d3ce40
- evidence_id: ETR
  kind: database
  reference: curation/term_requests.tsv
  locator: TSV line 478
  accessed_at: '2026-11-07T05:00:07Z'
  support: supports
  summary: '[[478, "habitatmech:GOLD.0a69f87c03\tannelid egg capsule albuminous fluid\tENVO:01001055\tenvironment
    associated with an animal part or small animal\tAn environment associated with
    an animal part or small animal consisting of the extracellular nutritive albuminous
    fluid inside an annelid cocoon (such as an earthworm or leech egg capsule), where
    vertically transmitted bacterial symbionts proliferate before colonizing developing
    embryos.\tearthworm cocoon extracellular fluid\tantigravity\t2026-10-17\tITEM
    curation: GOLD ''Host-associated > Annelida > Reproductive system > Egg capsule
    > Extracellular'' denotes the extracellular fluid compartment inside an annelid
    egg capsule/cocoon (PMID 18480259; DOI:10.1128/AEM.00126-08). Path: Host-associated
    > Annelida > Reproductive system > Egg capsule > Extracellular; parent_mode REPLACE
    under ENVO:01001055 excludes protective capsule parent Egg capsule (https://github.com/CultureBotAI/HabitatMech/issues/2304).\tREPLACE"]]'
  snapshot_sha256: f86df360f54cb00d3062ae27a9196828113219c06cfd9cfc9830a0e08603d069
- evidence_id: ELE
  kind: database
  reference: curation/definition_source_label_exclusions.tsv
  locator: TSV rows 249
  accessed_at: '2026-11-07T05:00:07Z'
  support: supports
  summary: '[{"data": {"curator": "antigravity", "date": "2026-10-17", "identifier":
    "habitatmech:GOLD.0a69f87c03", "notes": "Displaced GOLD source label ''Extracellular''
    in path ''Host-associated > Annelida > Reproductive system > Egg capsule > Extracellular''
    is context-dependent, ambiguous, or names a host/disease/process rather than the
    defined habitat ''annelid egg capsule albuminous fluid''; suppress automatic exact-synonym
    retention while preserving verbatim source provenance.", "requested_label": "annelid
    egg capsule albuminous fluid", "source_label": "Extracellular"}, "row": 249}]'
  snapshot_sha256: 596d59ab03fafa4c1fcdcb6446c87b7c72c04305e9d516047e661060710e86d4
- evidence_id: EP1
  kind: record_content
  reference: data/habitats/host_associated/egg_capsule.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-11-07T05:00:07Z'
  support: supports
  summary: '{"definition": "Protective membranes that surround amphibian embryos.",
    "grounding_status": "EXACT", "identifier": "UBERON:3010636", "label": "egg capsule",
    "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0000476", "UBERON:0000478"],
    "source_attestations": [{"mapping_predicate": "skos:exactMatch", "notes": "2 GOLD
    ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.",
    "source": "GOLD", "source_id": "gold.ecosystem:3892", "source_label": "Egg capsule",
    "source_path": "Host-associated > Annelida > Reproductive system > Egg capsule"}]}'
  snapshot_sha256: 7986a368cd50dd2bc20d7c8dc66ab0e6a954a7a4b9a5c5f672ce2f59a9089e8d
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'extracellular|habitatmech:GOLD.0a69f87c03' reviews/structured/*/review.yaml
    curation/ history/
  accessed_at: '2026-11-07T05:00:07Z'
  support: context_only
  summary: Structured-review traversal located Stage 4 predecessor bundle 20261106T194817Z-extracellular-record
    (linked via EPREV and related_reviews) and checked related cohort and ancestor
    reviews for reconciliation.
  search_scope: curation, history, data/raw, and reviews/structured/*/review.yaml
    traversal at commit 30fbe25f4c539ad6266dae7680d21e451caf6e40.
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261106T194817Z-extracellular-record/review.yaml
  locator: Every immutable Stage 4 baseline finding
  accessed_at: '2026-11-07T05:00:07Z'
  support: supports
  summary: Exact predecessor keys and findings reconciled; original inspected source
    scope preserved.
  snapshot_sha256: 46602629be3bc2dfd9c57ff8846950a6d8213177e485b0d60ee4bfb067c002cf
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_excretory_system_22ee753c_to_fecal_review_repairs.py
  locator: Complete full-corpus counterfactual regression suite
  accessed_at: '2026-11-07T05:00:07Z'
  support: supports
  summary: 'Exactly twenty-two records differ from the counterfactual baseline across
    Issues #2304 and #2305.'
  snapshot_sha256: 90bb097e6a2311fbaf0a2afadc4ca7642581bab11e5dd3d582ea5cd149c066f6
- evidence_id: EHIST_G1
  kind: record_content
  reference: history/other/gold_parent_exclusions/2026-11-07T045500Z-antigravity-230401.yaml
  locator: Complete curation session history event
  accessed_at: '2026-11-07T05:00:07Z'
  support: supports
  summary: 'Authorized curation event for Issue #2304 recorded and validated.'
  snapshot_sha256: d55f782e57e1c75b9485ba0c5e39260dfcbaed7532af9a7fc30c3316874efac9
assessments:
- assessment_id: A1
  area: schema
  topic: Native validity and reproduction after bounded remediation
  outcome: supported
  summary: Individual schema, strict 24-target validation, 868 history records, 14
    inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 83 causal
    overlays, 671 term requests, curation floor, site parity, and counterfactual regression
    tests passed.
  target_ids:
  - habitatmech:GOLD.0a69f87c03
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EGOLD
  - EGROUND
  - EONT
  - EONTEDGE
  - EDEC
  - ETR
  - ELE
  - EP1
  - ESEARCH
  - EPREV
  - ETEST
  - EHIST_G1
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: supported
  summary: 'habitatmech:GOLD.0a69f87c03: annelid egg capsule albuminous fluid; UNGROUNDED/REVIEWED;
    parents ["ENVO:01001055"]. Updated curation/term_requests.tsv and curation/term_requests/envo_robot_template.tsv
    for habitatmech:GOLD.0a69f87c03 to parent_id ENVO:01001055 (environment associated
    with an animal part or small animal) with parent_mode REPLACE (#2304), replacing
    whole-structure parent UBERON:3010636 (egg capsule). Identity (habitatmech:GOLD.0a69f87c03,
    ''annelid egg capsule albuminous fluid''), native REVIEWED/UNGROUNDED status,
    and source observations are preserved. No unresolved predecessor finding remains
    in this target scope.'
  target_ids:
  - habitatmech:GOLD.0a69f87c03
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EGOLD
  - EGROUND
  - EONT
  - EONTEDGE
  - EDEC
  - ETR
  - ELE
  - EP1
  - ESEARCH
  - EPREV
  - ETEST
  - EHIST_G1
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks,
    and pools: [{"source": "GOLD", "count": null, "unit": null}]. Zero counts are
    omitted; unrelated parent counts are not combined.'
  target_ids:
  - habitatmech:GOLD.0a69f87c03
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EGOLD
  - EGROUND
  - EONT
  - EONTEDGE
  - EDEC
  - ETR
  - ELE
  - EP1
  - ESEARCH
  - EPREV
  - ETEST
  - EHIST_G1
- assessment_id: A4
  area: representation
  topic: Predecessor finding reconciliation
  outcome: supported
  summary: Every predecessor finding preserves its stable issue_key and exact lineage.
    All predecessor findings in this target scope are resolved.
  target_ids:
  - habitatmech:GOLD.0a69f87c03
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EGOLD
  - EGROUND
  - EONT
  - EONTEDGE
  - EDEC
  - ETR
  - ELE
  - EP1
  - ESEARCH
  - EPREV
  - ETEST
  - EHIST_G1
- assessment_id: A5
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: Missing optional parameters/graphs are not evidence deficits. Full source
    decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only
    review does not mutate generated records.
  target_ids:
  - habitatmech:GOLD.0a69f87c03
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EGOLD
  - EGROUND
  - EONT
  - EONTEDGE
  - EDEC
  - ETR
  - ELE
  - EP1
  - ESEARCH
  - EPREV
  - ETEST
  - EHIST_G1
findings:
- finding_id: F1
  issue_key: extracellular-context-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Annelid egg capsule albuminous fluid asserts protective membrane UBERON:3010636
    (egg capsule) as a superclass
  description: Update curation/term_requests.tsv row 478 for habitatmech:GOLD.0a69f87c03
    ('annelid egg capsule albuminous fluid') to use parent_id ENVO:01001055 (environment
    associated with an animal part or small animal) with parent_mode REPLACE (and
    update the definition genus accordingly), matching sibling extracellular__3f7afaf4
    (habitatmech:GOLD.6c8238add0).
  target_ids:
  - habitatmech:GOLD.0a69f87c03
  field_paths:
  - definition
  - parent_habitats
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EGOLD
  - EGROUND
  - EONT
  - EONTEDGE
  - EDEC
  - ETR
  - ELE
  - EP1
  - ESEARCH
  - EPREV
  - ETEST
  - EHIST_G1
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or representation claim; deterministic
    validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2304
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261106T194817Z-extracellular-record
    finding_id: F1
  disposition_reason: Updated curation/term_requests.tsv and curation/term_requests/envo_robot_template.tsv
    for habitatmech:GOLD.0a69f87c03 to parent_id ENVO:01001055 (environment associated
    with an animal part or small animal) with parent_mode REPLACE (#2304), replacing
    whole-structure parent UBERON:3010636 (egg capsule).
actions: []
limitations:
- Only the stated primary evidence and current ontology/taxonomy authorities were
  independently inspected; original specimen-level support for every source-bin member
  is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism
  or characteristic presence. Parent observations are not inherited by children.
- Configured label correspondence skipped 2,084 no-adapter pairs; this is not whole-corpus
  identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in
  this pre-save observation.
- 'iModulonDB is not applicable: the target has no gene, regulator or expression-module
  assertion. No paid research or scientific-status promotion was performed.'
notes:
- Saved against working-tree repairs atop main commit 30fbe25f4c539ad6266dae7680d21e451caf6e40;
  all earlier saved bundles in reviews/structured/ remain byte-identical.
- Reconciles predecessor bundle 20261106T194817Z-extracellular-record with exact issue_key
  and previous_occurrences lineage.
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261106T194817Z-extracellular-record
  relationship: Exact predecessor; every finding explicitly reconciled.
```
