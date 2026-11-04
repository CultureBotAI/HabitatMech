# Remediation review: empyema_drain

- Review: 20261104T035801Z-empyema_drain-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-04T03:55:00Z
- Finished UTC: 2026-11-04T03:58:01Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Removed the bare medical-device alias 'Empyema drain' from exact_synonym in curation/term_requests.tsv (retaining 'empyema chest drain fluid') and added a guarded exclusion row in curation/definition_source_label_exclusions.tsv so 'Empyema drain' is scoped as RELATED_SYNONYM from GOLD (#2286). Identity (habitatmech:GOLD.1ce5b3ff1a, 'pleural empyema drainage fluid'), native status, hierarchy, and source observations are preserved. No unresolved predecessor finding remains in this target scope.

## Scope And Provenance

Full current target assessment and explicit disposition of every baseline finding on data/habitats/host_associated/empyema_drain.yaml after bounded Cycle 4 Stage 5 remediation.

Selection: One of nine repaired targets from the empyema_drain-through-epibionts cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 95a1eb1b6a5b18b8a5c3b135222b1118f7506ef0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.1ce5b3ff1a | data/habitats/host_associated/empyema_drain.yaml | generated | pleural empyema drainage fluid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.1ce5b3ff1a | Completed 2026-11-01T06:08:08Z. No issues found. |
| validate-strict | passed | True | habitatmech:GOLD.1ce5b3ff1a | Completed 2026-11-01T06:08:14Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | habitatmech:GOLD.1ce5b3ff1a | Completed 2026-11-04T03:57:00Z. No issues found; 860 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | habitatmech:GOLD.1ce5b3ff1a | Completed 2026-11-01T06:08:25Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | habitatmech:GOLD.1ce5b3ff1a | Completed 2026-11-04T03:57:10Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | habitatmech:GOLD.1ce5b3ff1a | Completed 2026-11-01T06:08:45Z. validated 63 causal-graph curation file(s) with 63 graph(s). |
| term-requests-check | passed | True | habitatmech:GOLD.1ce5b3ff1a | Completed 2026-11-04T03:57:15Z. term-request table is current (671 terms). |
| validate-products | passed | True | habitatmech:GOLD.1ce5b3ff1a | Completed 2026-11-01T06:11:06Z. OK_CANONICAL: 1196, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2071. All id&lt;-&gt;label pairs correspond. |
| pytest counterfactual review repairs | passed | True | habitatmech:GOLD.1ce5b3ff1a | Completed 2026-11-04T03:58:00Z. 2 passed; exact 9-record counterfactual diff verified. |
| curation-floor | passed | True | habitatmech:GOLD.1ce5b3ff1a | Completed 2026-11-04T03:58:05Z. Floor satisfied across all 13 metrics. |
| render-check | passed | True | habitatmech:GOLD.1ce5b3ff1a | Completed 2026-11-04T03:58:30Z. rendered 3209 habitat pages, 750 redirect stubs, 8 categories, 696 term requests; pages/ is in step with the corpus. |

## Scientific And Domain Assessments

### Native validity and reproduction after bounded remediation

schema: supported. Targets: habitatmech:GOLD.1ce5b3ff1a.

Individual schema, strict 24-target validation, 860 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 58 causal overlays, 671 term requests, curation floor, site parity, and counterfactual regression tests passed.

### Identity, definition, hierarchy and aliases

identity: supported. Targets: habitatmech:GOLD.1ce5b3ff1a.

habitatmech:GOLD.1ce5b3ff1a: pleural empyema drainage fluid; UNGROUNDED/REVIEWED; parents ["UBERON:0006314"]. Removed the bare medical-device alias 'Empyema drain' from exact_synonym in curation/term_requests.tsv (retaining 'empyema chest drain fluid') and added a guarded exclusion row in curation/definition_source_label_exclusions.tsv so 'Empyema drain' is scoped as RELATED_SYNONYM from GOLD (#2286). Identity (habitatmech:GOLD.1ce5b3ff1a, 'pleural empyema drainage fluid'), native status, hierarchy, and source observations are preserved. No unresolved predecessor finding remains in this target scope.

### Source counts and retained ranking

quantity: supported. Targets: habitatmech:GOLD.1ce5b3ff1a.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"source": "GOLD", "count": 1, "unit": "ORGANISM"}]. Zero counts are omitted; unrelated parent counts are not combined.

### Predecessor finding reconciliation

representation: supported. Targets: habitatmech:GOLD.1ce5b3ff1a.

Every predecessor finding preserves its stable issue_key and exact lineage. All predecessor findings in this target scope are resolved.

### Parameters, mechanisms and native status

completeness: supported. Targets: habitatmech:GOLD.1ce5b3ff1a.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only review does not mutate generated records.

## Findings

### F1: Bare device/procedure label 'Empyema drain' is asserted as an exact drainage-fluid synonym

major / resolved / confirmed; issue key: empyema-drain-device-name-exact-synonym.

Remove bare 'Empyema drain' from exact_synonym in curation/term_requests.tsv for habitatmech:GOLD.1ce5b3ff1a (keeping 'empyema chest drain fluid') and add a guarded row in curation/definition_source_label_exclusions.tsv so 'Empyema drain' is scoped as RELATED_SYNONYM from GOLD rather than EXACT_SYNONYM.

Disposition: Removed bare 'Empyema drain' from exact_synonym in curation/term_requests.tsv (retaining 'empyema chest drain fluid') and added a guarded row in curation/definition_source_label_exclusions.tsv (#2286) so 'Empyema drain' is emitted as RELATED_SYNONYM from GOLD.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/empyema_drain.yaml; Entire YAML | supports | {"identifier": "habitatmech:GOLD.1ce5b3ff1a", "label": "pleural empyema drainage fluid", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED", "parent_habitats": ["UBERON:0006314"], "synonyms": [{"synonym_text": "empyema chest drain fluid", "synonym_type": "EXACT_SYNONYM", "source": "HabitatMech curation"}], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6303", "source_label": "Empyema drain", "source_path": "Host-associated &gt; Mammals: Human &gt; Respiratory system &gt; Pleural space/cavity &gt; Empyema drain", "assertion_count": 1, "assertion_unit": "ORGANISM"}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED."}, {"timestamp": "2026-10-17T00:00:00Z", "curator": "antigravity", "action": "CONFIRM_UNGROUNDED", "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. ITEM curation: GOLD 'Host-associated &gt; Mammals: Human &gt; Respiratory system &gt; Pleural space/cavity &gt; Empyema drain' denotes purulent fluid drained from a pleural empyema rather than the pleural cavity organ (UBERON:0002402). Define under UBERON:0006314 (bodily fluid) with parent_mode REPLACE (PMID 31558513; DOI:10.1128/JCM.00856-19). Path: Host-associated &gt; Mammals: Human &gt; Respiratory system &gt; Pleural space/cavity &gt; Empyema drain (source concept habitatmech:GOLD.1ce5b3ff1a)"}, {"timestamp": "2026-11-04T00:00:00Z", "curator": "antigravity", "action": "DEFINED", "changes": "Defined as 'pleural empyema drainage fluid' under UBERON:0006314 'bodily fluid'. ITEM curation https://github.com/CultureBotAI/HabitatMech/issues/2286 : GOLD 'Host-associated &gt; Mammals: Human &gt; Respiratory system &gt; Pleural space/cavity &gt; Empyema drain' denotes purulent fluid drained from a pleural empyema rather than the pleural cavity organ (UBERON:0002402) or the physical drain tube/device. Define under UBERON:0006314 (bodily fluid) with parent_mode REPLACE and exclude device-ambiguous 'Empyema drain' (PMID 31558513; DOI:10.1128/JCM.00856-19). Path: Host-associated &gt; Mammals: Human &gt; Respiratory system &gt; Pleural space/cavity &gt; Empyema drain"}, {"timestamp": "2026-11-04T00:00:00Z", "curator": "antigravity", "action": "SOURCE_SYNONYM_EXCLUDED", "changes": "Omitted automatic retention of displaced source label 'Empyema drain' when defining habitatmech:GOLD.1ce5b3ff1a as 'pleural empyema drainage fluid'. Verbatim source attestations are preserved. Review https://github.com/CultureBotAI/HabitatMech/issues/2286 : The displaced label Empyema drain is ambiguous between the physical chest drain device/catheter and the purulent pleural exudate outside Host-associated &gt; Mammals: Human &gt; Respiratory system &gt; Pleural space/cavity &gt; Empyema drain. Remove only the device-ambiguous exact alias and suppress exact-alias fallback; preserve verbatim source provenance, definition, empyema chest drain fluid synonym, genera and native status."}]} |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=habitatmech:GOLD.1ce5b3ff1a, grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["UBERON:0006314"]. |
| EGOLD | data/raw/gold_ecosystem_paths.tsv; TSV rows 1090 | supports | [{"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Mammals: Human &gt; Respiratory system &gt; Pleural space/cavity &gt; Empyema drain", "depth": "5", "ecosystem": "Host-associated", "ecosystem_category": "Mammals: Human", "ecosystem_subtype": "Pleural space/cavity", "ecosystem_type": "Respiratory system", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:6303", "leaf_label": "Empyema drain", "organism_count": "1", "specific_ecosystem": "Empyema drain", "study_count": "0", "total_assertions": "1"}, "row": 1090}] |
| EONT | data/raw/ontology_terms.tsv; TSV rows 13288 | supports | [{"data": {"definition": "Liquid components of living organisms. includes fluids that are excreted or secreted from the body as well as body water that normally is not.", "deprecated": "", "directly_referenced": "FALSE", "label": "bodily fluid", "label_only": "FALSE", "ontology": "UBERON", "synonyms": "body fluid&#124;fluid", "term_id": "UBERON:0006314"}, "row": 13288}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 7005,11038,11080,11083,11158,11250,11275,11283,11559,11630,11632,11832 | supports | [{"data": {"object": "UBERON:0006314", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001188"}, "row": 7005}, {"data": {"object": "UBERON:0006314", "predicate": "rdfs:subClassOf", "subject": "UBERON:0000179"}, "row": 11038}, {"data": {"object": "UBERON:0006314", "predicate": "rdfs:subClassOf", "subject": "UBERON:0000910"}, "row": 11080}, {"data": {"object": "UBERON:0006314", "predicate": "rdfs:subClassOf", "subject": "UBERON:0000912"}, "row": 11083}, {"data": {"object": "UBERON:0006314", "predicate": "rdfs:subClassOf", "subject": "UBERON:0001089"}, "row": 11158}, {"data": {"object": "UBERON:0006314", "predicate": "rdfs:subClassOf", "subject": "UBERON:0001796"}, "row": 11250}, {"data": {"object": "UBERON:0006314", "predicate": "rdfs:subClassOf", "subject": "UBERON:0001913"}, "row": 11275}, {"data": {"object": "UBERON:0006314", "predicate": "rdfs:subClassOf", "subject": "UBERON:0001970"}, "row": 11283}, {"data": {"object": "UBERON:0000463", "predicate": "rdfs:subClassOf", "subject": "UBERON:0006314"}, "row": 11559}, {"data": {"object": "UBERON:0006314", "predicate": "rdfs:subClassOf", "subject": "UBERON:0007779"}, "row": 11630}, {"data": {"object": "UBERON:0006314", "predicate": "rdfs:subClassOf", "subject": "UBERON:0007794"}, "row": 11632}, {"data": {"object": "UBERON:0006314", "predicate": "rdfs:subClassOf", "subject": "UBERON:0035963"}, "row": 11832}] |
| EDEC | curation/decisions.tsv; TSV line 278 | supports | [[278, "habitatmech:GOLD.1ce5b3ff1a\tCONFIRM_UNGROUNDED\t\t\t\tantigravity\t2026-10-17\tITEM curation: GOLD 'Host-associated &gt; Mammals: Human &gt; Respiratory system &gt; Pleural space/cavity &gt; Empyema drain' denotes purulent fluid drained from a pleural empyema rather than the pleural cavity organ (UBERON:0002402). Define under UBERON:0006314 (bodily fluid) with parent_mode REPLACE (PMID 31558513; DOI:10.1128/JCM.00856-19). Path: Host-associated &gt; Mammals: Human &gt; Respiratory system &gt; Pleural space/cavity &gt; Empyema drain\tITEM\t\t"]] |
| ETR | curation/term_requests.tsv; TSV line 236 | supports | [[236, "habitatmech:GOLD.1ce5b3ff1a\tpleural empyema drainage fluid\tUBERON:0006314\tbodily fluid\tA bodily fluid consisting of purulent pleural exudate drained from a human pleural cavity affected by empyema.\tempyema chest drain fluid\tantigravity\t2026-11-04\tITEM curation https://github.com/CultureBotAI/HabitatMech/issues/2286 : GOLD 'Host-associated &gt; Mammals: Human &gt; Respiratory system &gt; Pleural space/cavity &gt; Empyema drain' denotes purulent fluid drained from a pleural empyema rather than the pleural cavity organ (UBERON:0002402) or the physical drain tube/device. Define under UBERON:0006314 (bodily fluid) with parent_mode REPLACE and exclude device-ambiguous 'Empyema drain' (PMID 31558513; DOI:10.1128/JCM.00856-19). Path: Host-associated &gt; Mammals: Human &gt; Respiratory system &gt; Pleural space/cavity &gt; Empyema drain\tREPLACE"]] |
| ESEARCH | Local input and review traversal; grep -rn -E 'empyema_drain&#124;habitatmech:GOLD.1ce5b3ff1a' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal verified no prior target review bundle exists for this record; curation and history tables were inspected for all matching rows. |
| EPREV | reviews/structured/20261101T061210Z-empyema_drain-record/review.yaml; Every immutable Stage 4 baseline finding | supports | Exact predecessor keys and findings reconciled; original inspected source scope preserved. |
| ETEST | tests/test_empyema_drain_to_epibionts_review_repairs.py; Complete full-corpus counterfactual regression suite | supports | Exactly nine records differ from the counterfactual baseline across Issues #2285 and #2286. |
| ESYNS | curation/definition_source_label_exclusions.tsv; TSV line 2 | supports | [[2, "habitatmech:GOLD.1ce5b3ff1a\tEmpyema drain\tpleural empyema drainage fluid\tantigravity\t2026-11-04\tReview https://github.com/CultureBotAI/HabitatMech/issues/2286 : The displaced label Empyema drain is ambiguous between the physical chest drain device/catheter and the purulent pleural exudate outside Host-associated &gt; Mammals: Human &gt; Respiratory system &gt; Pleural space/cavity &gt; Empyema drain. Remove only the device-ambiguous exact alias and suppress exact-alias fallback; preserve verbatim source provenance, definition, empyema chest drain fluid synonym, genera and native status."]] |
| EHIST_G2 | history/other/definition_source_label_exclusions/2026-11-04T034510Z-antigravity-228601.yaml; Complete curation session history event | supports | Authorized curation event for Issue #2286 recorded and validated. |

## Limits And Additional Notes

- Only the stated primary evidence and current ontology/taxonomy authorities were independently inspected; original specimen-level support for every source-bin member is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism or characteristic presence. Parent observations are not inherited by children.
- Configured label correspondence skipped 2,071 no-adapter pairs; this is not whole-corpus identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in this pre-save observation.
- iModulonDB is not applicable: the target has no gene, regulator or expression-module assertion. No paid research or scientific-status promotion was performed.
- Saved against working-tree repairs atop main commit 95a1eb1b6a5b18b8a5c3b135222b1118f7506ef0; all earlier saved bundles in reviews/structured/ remain byte-identical.
- Reconciles predecessor bundle 20261101T061210Z-empyema_drain-record with exact issue_key and previous_occurrences lineage.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T035801Z-empyema_drain-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: empyema_drain'
started_at: '2026-11-04T03:55:00Z'
finished_at: '2026-11-04T03:58:01Z'
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
summary: Removed the bare medical-device alias 'Empyema drain' from exact_synonym
  in curation/term_requests.tsv (retaining 'empyema chest drain fluid') and added
  a guarded exclusion row in curation/definition_source_label_exclusions.tsv so 'Empyema
  drain' is scoped as RELATED_SYNONYM from GOLD (#2286). Identity (habitatmech:GOLD.1ce5b3ff1a,
  'pleural empyema drainage fluid'), native status, hierarchy, and source observations
  are preserved. No unresolved predecessor finding remains in this target scope.
source:
  git_revision: 95a1eb1b6a5b18b8a5c3b135222b1118f7506ef0
  state: working_tree
  inputs:
  - path: curation/decisions.tsv
    sha256: 7e55e782625f544f2d3e4e5c9e5ed5d82c04d477ee606c894bc26cb55f8a949e
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 454bc07fdc75b4abdced785be5334e75d2955ea691fedb1122bf474b68cd73de
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: ec8f7b5cf7b804e31663653e482be907b0333a8be807259eec024fcb7acfeb94
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: c1207270bb0ae2031e42de6cb8220b20f98886f65e40d48793bfd7e9d757d83a
    role: context
  - path: curation/term_requests.tsv
    sha256: d2ca8bb2a88649eef54ff812b40641a02f2ab39145168d65617503309ea9127c
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/host_associated/empyema_drain.yaml
    sha256: a8d070d444e85b5a3c54d7c1ef8a92c1f1ac3ed7b7b89238d85844d0ff45ec16
    role: target
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
  - path: history/other/definition_source_label_exclusions/2026-11-04T034510Z-antigravity-228601.yaml
    sha256: 257872174c2e52bee3c842c011d691a7cbe702307a33f69531dcbda7c1141333
    role: context
  - path: history/other/gold_parent_exclusions/2026-11-04T034500Z-antigravity-228501.yaml
    sha256: 01cc85edae358f0b99fb26bb0127c93f997cb24f5b87fecb2a496604eb00f230
    role: context
  - path: reviews/structured/20261101T061210Z-empyema_drain-record/review.yaml
    sha256: cd97df27b9176fc05d56a8f271ac86880a2b2bf541955653651355fb4a293a75
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
    role: context
  - path: src/habitatmech/seed.py
    sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
    role: context
  - path: tests/test_empyema_drain_to_epibionts_review_repairs.py
    sha256: bbd37dbb824e90efe994ab4a44b01b16d9ed4a5b039fb66aa902192a4752036c
    role: context
targets:
- target_id: habitatmech:GOLD.1ce5b3ff1a
  path: data/habitats/host_associated/empyema_drain.yaml
  label: pleural empyema drainage fluid
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
    finding on data/habitats/host_associated/empyema_drain.yaml after bounded Cycle
    4 Stage 5 remediation.
  selection: One of nine repaired targets from the empyema_drain-through-epibionts
    cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.1ce5b3ff1a
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
    --target-class HabitatRecord data/habitats/host_associated/empyema_drain.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.1ce5b3ff1a
  summary: Completed 2026-11-01T06:08:08Z. No issues found.
  scope_note: Individual schema; strict command covers the 24 named cohort targets;
    other documented gates have full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/habitats/host_associated/empyema_drain.yaml
    data/habitats/host_associated/endocrine_gland.yaml data/habitats/host_associated/endocrine_gland__8c35903c.yaml
    data/habitats/host_associated/endocrine_system.yaml data/habitats/host_associated/endocrine_system__a22b6ca6.yaml
    data/habitats/host_associated/endocrine_system__e2d3d7a6.yaml data/habitats/host_associated/endocrine_system__fc8977b8.yaml
    data/habitats/host_associated/endometrial_uterine.yaml data/habitats/host_associated/endometrium.yaml
    data/habitats/host_associated/endophytes.yaml data/habitats/host_associated/endophytes__ca9aaedf.yaml
    data/habitats/host_associated/endophytes__fae60ba7.yaml data/habitats/host_associated/endosphere.yaml
    data/habitats/host_associated/endosphere__005f8afe.yaml data/habitats/host_associated/endosphere__eb0d56da.yaml
    data/habitats/host_associated/endosphere__fd8c8a61.yaml data/habitats/host_associated/endosymbionts.yaml
    data/habitats/host_associated/endosymbionts__38198b44.yaml data/habitats/host_associated/endothelial_cell.yaml
    data/habitats/host_associated/endothelial_progenitor_cell.yaml data/habitats/host_associated/enterocyte.yaml
    data/habitats/host_associated/environmental_system_determined_by_an_organism.yaml
    data/habitats/host_associated/eosinophil.yaml data/habitats/host_associated/epibionts.yaml
    --out /tmp/c4s4_24_strict.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.1ce5b3ff1a
  summary: 'Completed 2026-11-01T06:08:14Z. Validated 24 files; files with ERROR:
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
  - habitatmech:GOLD.1ce5b3ff1a
  summary: Completed 2026-11-04T03:57:00Z. No issues found; 860 history record(s)
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
  - habitatmech:GOLD.1ce5b3ff1a
  summary: 'Completed 2026-11-01T06:08:25Z. provenance current: 14 committed inventories,
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
  - habitatmech:GOLD.1ce5b3ff1a
  summary: 'Completed 2026-11-04T03:57:10Z. expected 3209 records, found 3209 on disk;
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
  - habitatmech:GOLD.1ce5b3ff1a
  summary: Completed 2026-11-01T06:08:45Z. validated 63 causal-graph curation file(s)
    with 63 graph(s).
  scope_note: Full-corpus causal-graph overlay validation.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: .venv/bin/python scripts/build_term_requests.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.1ce5b3ff1a
  summary: Completed 2026-11-04T03:57:15Z. term-request table is current (671 terms).
  scope_note: Full-corpus term-request table currency check.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.1ce5b3ff1a
  summary: 'Completed 2026-11-01T06:11:06Z. OK_CANONICAL: 1196, OK_SYNONYM: 1, OK_EXCEPTION:
    5, SKIPPED_NO_ADAPTER: 2071. All id<->label pairs correspond.'
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
- check_id: C9
  name: pytest counterfactual review repairs
  status: passed
  required: true
  command: .venv/bin/python -m pytest tests/test_empyema_drain_to_epibionts_review_repairs.py
    -q --no-cov
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.1ce5b3ff1a
  summary: Completed 2026-11-04T03:58:00Z. 2 passed; exact 9-record counterfactual
    diff verified.
  scope_note: 'Full-corpus counterfactual regression test for Issues #2285 and #2286.'
- check_id: C10
  name: curation-floor
  status: passed
  required: true
  command: .venv/bin/python scripts/check_curation_floor.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.1ce5b3ff1a
  summary: Completed 2026-11-04T03:58:05Z. Floor satisfied across all 13 metrics.
  scope_note: Full-corpus curation floor ratchets.
- check_id: C11
  name: render-check
  status: passed
  required: true
  command: .venv/bin/python scripts/render_pages.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.1ce5b3ff1a
  summary: Completed 2026-11-04T03:58:30Z. rendered 3209 habitat pages, 750 redirect
    stubs, 8 categories, 696 term requests; pages/ is in step with the corpus.
  scope_note: Full-corpus static site parity check.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/empyema_drain.yaml
  locator: Entire YAML
  accessed_at: '2026-11-04T03:58:01Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.1ce5b3ff1a", "label": "pleural empyema
    drainage fluid", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED",
    "parent_habitats": ["UBERON:0006314"], "synonyms": [{"synonym_text": "empyema
    chest drain fluid", "synonym_type": "EXACT_SYNONYM", "source": "HabitatMech curation"}],
    "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6303",
    "source_label": "Empyema drain", "source_path": "Host-associated > Mammals: Human
    > Respiratory system > Pleural space/cavity > Empyema drain", "assertion_count":
    1, "assertion_unit": "ORGANISM"}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z",
    "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded
    from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED."}, {"timestamp":
    "2026-10-17T00:00:00Z", "curator": "antigravity", "action": "CONFIRM_UNGROUNDED",
    "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. ITEM curation:
    GOLD ''Host-associated > Mammals: Human > Respiratory system > Pleural space/cavity
    > Empyema drain'' denotes purulent fluid drained from a pleural empyema rather
    than the pleural cavity organ (UBERON:0002402). Define under UBERON:0006314 (bodily
    fluid) with parent_mode REPLACE (PMID 31558513; DOI:10.1128/JCM.00856-19). Path:
    Host-associated > Mammals: Human > Respiratory system > Pleural space/cavity >
    Empyema drain (source concept habitatmech:GOLD.1ce5b3ff1a)"}, {"timestamp": "2026-11-04T00:00:00Z",
    "curator": "antigravity", "action": "DEFINED", "changes": "Defined as ''pleural
    empyema drainage fluid'' under UBERON:0006314 ''bodily fluid''. ITEM curation
    https://github.com/CultureBotAI/HabitatMech/issues/2286 : GOLD ''Host-associated
    > Mammals: Human > Respiratory system > Pleural space/cavity > Empyema drain''
    denotes purulent fluid drained from a pleural empyema rather than the pleural
    cavity organ (UBERON:0002402) or the physical drain tube/device. Define under
    UBERON:0006314 (bodily fluid) with parent_mode REPLACE and exclude device-ambiguous
    ''Empyema drain'' (PMID 31558513; DOI:10.1128/JCM.00856-19). Path: Host-associated
    > Mammals: Human > Respiratory system > Pleural space/cavity > Empyema drain"},
    {"timestamp": "2026-11-04T00:00:00Z", "curator": "antigravity", "action": "SOURCE_SYNONYM_EXCLUDED",
    "changes": "Omitted automatic retention of displaced source label ''Empyema drain''
    when defining habitatmech:GOLD.1ce5b3ff1a as ''pleural empyema drainage fluid''.
    Verbatim source attestations are preserved. Review https://github.com/CultureBotAI/HabitatMech/issues/2286
    : The displaced label Empyema drain is ambiguous between the physical chest drain
    device/catheter and the purulent pleural exudate outside Host-associated > Mammals:
    Human > Respiratory system > Pleural space/cavity > Empyema drain. Remove only
    the device-ambiguous exact alias and suppress exact-alias fallback; preserve verbatim
    source provenance, definition, empyema chest drain fluid synonym, genera and native
    status."}]}'
  snapshot_sha256: a8d070d444e85b5a3c54d7c1ef8a92c1f1ac3ed7b7b89238d85844d0ff45ec16
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-04T03:58:01Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon terms cannot substitute
    for associated environments; parent_habitats must be strictly broader across all
    contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-04T03:58:01Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-04T03:58:01Z'
  support: supports
  summary: Seed generator produces identifier=habitatmech:GOLD.1ce5b3ff1a, grounding_status=UNGROUNDED,
    mapping_status=REVIEWED, parent_habitats=["UBERON:0006314"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EGOLD
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV rows 1090
  accessed_at: '2026-11-04T03:58:01Z'
  support: supports
  summary: '[{"data": {"biosample_count": "0", "canonical_path": "Host-associated
    > Mammals: Human > Respiratory system > Pleural space/cavity > Empyema drain",
    "depth": "5", "ecosystem": "Host-associated", "ecosystem_category": "Mammals:
    Human", "ecosystem_subtype": "Pleural space/cavity", "ecosystem_type": "Respiratory
    system", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:6303", "leaf_label":
    "Empyema drain", "organism_count": "1", "specific_ecosystem": "Empyema drain",
    "study_count": "0", "total_assertions": "1"}, "row": 1090}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 13288
  accessed_at: '2026-11-04T03:58:01Z'
  support: supports
  summary: '[{"data": {"definition": "Liquid components of living organisms. includes
    fluids that are excreted or secreted from the body as well as body water that
    normally is not.", "deprecated": "", "directly_referenced": "FALSE", "label":
    "bodily fluid", "label_only": "FALSE", "ontology": "UBERON", "synonyms": "body
    fluid|fluid", "term_id": "UBERON:0006314"}, "row": 13288}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 7005,11038,11080,11083,11158,11250,11275,11283,11559,11630,11632,11832
  accessed_at: '2026-11-04T03:58:01Z'
  support: supports
  summary: '[{"data": {"object": "UBERON:0006314", "predicate": "rdfs:subClassOf",
    "subject": "ENVO:01001188"}, "row": 7005}, {"data": {"object": "UBERON:0006314",
    "predicate": "rdfs:subClassOf", "subject": "UBERON:0000179"}, "row": 11038}, {"data":
    {"object": "UBERON:0006314", "predicate": "rdfs:subClassOf", "subject": "UBERON:0000910"},
    "row": 11080}, {"data": {"object": "UBERON:0006314", "predicate": "rdfs:subClassOf",
    "subject": "UBERON:0000912"}, "row": 11083}, {"data": {"object": "UBERON:0006314",
    "predicate": "rdfs:subClassOf", "subject": "UBERON:0001089"}, "row": 11158}, {"data":
    {"object": "UBERON:0006314", "predicate": "rdfs:subClassOf", "subject": "UBERON:0001796"},
    "row": 11250}, {"data": {"object": "UBERON:0006314", "predicate": "rdfs:subClassOf",
    "subject": "UBERON:0001913"}, "row": 11275}, {"data": {"object": "UBERON:0006314",
    "predicate": "rdfs:subClassOf", "subject": "UBERON:0001970"}, "row": 11283}, {"data":
    {"object": "UBERON:0000463", "predicate": "rdfs:subClassOf", "subject": "UBERON:0006314"},
    "row": 11559}, {"data": {"object": "UBERON:0006314", "predicate": "rdfs:subClassOf",
    "subject": "UBERON:0007779"}, "row": 11630}, {"data": {"object": "UBERON:0006314",
    "predicate": "rdfs:subClassOf", "subject": "UBERON:0007794"}, "row": 11632}, {"data":
    {"object": "UBERON:0006314", "predicate": "rdfs:subClassOf", "subject": "UBERON:0035963"},
    "row": 11832}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EDEC
  kind: database
  reference: curation/decisions.tsv
  locator: TSV line 278
  accessed_at: '2026-11-04T03:58:01Z'
  support: supports
  summary: '[[278, "habitatmech:GOLD.1ce5b3ff1a\tCONFIRM_UNGROUNDED\t\t\t\tantigravity\t2026-10-17\tITEM
    curation: GOLD ''Host-associated > Mammals: Human > Respiratory system > Pleural
    space/cavity > Empyema drain'' denotes purulent fluid drained from a pleural empyema
    rather than the pleural cavity organ (UBERON:0002402). Define under UBERON:0006314
    (bodily fluid) with parent_mode REPLACE (PMID 31558513; DOI:10.1128/JCM.00856-19).
    Path: Host-associated > Mammals: Human > Respiratory system > Pleural space/cavity
    > Empyema drain\tITEM\t\t"]]'
  snapshot_sha256: 7e55e782625f544f2d3e4e5c9e5ed5d82c04d477ee606c894bc26cb55f8a949e
- evidence_id: ETR
  kind: database
  reference: curation/term_requests.tsv
  locator: TSV line 236
  accessed_at: '2026-11-04T03:58:01Z'
  support: supports
  summary: '[[236, "habitatmech:GOLD.1ce5b3ff1a\tpleural empyema drainage fluid\tUBERON:0006314\tbodily
    fluid\tA bodily fluid consisting of purulent pleural exudate drained from a human
    pleural cavity affected by empyema.\tempyema chest drain fluid\tantigravity\t2026-11-04\tITEM
    curation https://github.com/CultureBotAI/HabitatMech/issues/2286 : GOLD ''Host-associated
    > Mammals: Human > Respiratory system > Pleural space/cavity > Empyema drain''
    denotes purulent fluid drained from a pleural empyema rather than the pleural
    cavity organ (UBERON:0002402) or the physical drain tube/device. Define under
    UBERON:0006314 (bodily fluid) with parent_mode REPLACE and exclude device-ambiguous
    ''Empyema drain'' (PMID 31558513; DOI:10.1128/JCM.00856-19). Path: Host-associated
    > Mammals: Human > Respiratory system > Pleural space/cavity > Empyema drain\tREPLACE"]]'
  snapshot_sha256: d2ca8bb2a88649eef54ff812b40641a02f2ab39145168d65617503309ea9127c
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'empyema_drain|habitatmech:GOLD.1ce5b3ff1a' reviews/structured/*/review.yaml
    curation/ history/
  accessed_at: '2026-11-04T03:58:01Z'
  support: context_only
  summary: Structured-review traversal verified no prior target review bundle exists
    for this record; curation and history tables were inspected for all matching rows.
  search_scope: curation, history, data/raw, and reviews/structured/*/review.yaml
    traversal at commit ad20de05c38d4fadf667b5c579eef50496b31b02.
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261101T061210Z-empyema_drain-record/review.yaml
  locator: Every immutable Stage 4 baseline finding
  accessed_at: '2026-11-04T03:58:01Z'
  support: supports
  summary: Exact predecessor keys and findings reconciled; original inspected source
    scope preserved.
  snapshot_sha256: cd97df27b9176fc05d56a8f271ac86880a2b2bf541955653651355fb4a293a75
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_empyema_drain_to_epibionts_review_repairs.py
  locator: Complete full-corpus counterfactual regression suite
  accessed_at: '2026-11-04T03:58:01Z'
  support: supports
  summary: 'Exactly nine records differ from the counterfactual baseline across Issues
    #2285 and #2286.'
  snapshot_sha256: bbd37dbb824e90efe994ab4a44b01b16d9ed4a5b039fb66aa902192a4752036c
- evidence_id: ESYNS
  kind: record_content
  reference: curation/definition_source_label_exclusions.tsv
  locator: TSV line 2
  accessed_at: '2026-11-04T03:58:01Z'
  support: supports
  summary: '[[2, "habitatmech:GOLD.1ce5b3ff1a\tEmpyema drain\tpleural empyema drainage
    fluid\tantigravity\t2026-11-04\tReview https://github.com/CultureBotAI/HabitatMech/issues/2286
    : The displaced label Empyema drain is ambiguous between the physical chest drain
    device/catheter and the purulent pleural exudate outside Host-associated > Mammals:
    Human > Respiratory system > Pleural space/cavity > Empyema drain. Remove only
    the device-ambiguous exact alias and suppress exact-alias fallback; preserve verbatim
    source provenance, definition, empyema chest drain fluid synonym, genera and native
    status."]]'
  snapshot_sha256: 454bc07fdc75b4abdced785be5334e75d2955ea691fedb1122bf474b68cd73de
- evidence_id: EHIST_G2
  kind: record_content
  reference: history/other/definition_source_label_exclusions/2026-11-04T034510Z-antigravity-228601.yaml
  locator: Complete curation session history event
  accessed_at: '2026-11-04T03:58:01Z'
  support: supports
  summary: 'Authorized curation event for Issue #2286 recorded and validated.'
  snapshot_sha256: 257872174c2e52bee3c842c011d691a7cbe702307a33f69531dcbda7c1141333
assessments:
- assessment_id: A1
  area: schema
  topic: Native validity and reproduction after bounded remediation
  outcome: supported
  summary: Individual schema, strict 24-target validation, 860 history records, 14
    inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 58 causal
    overlays, 671 term requests, curation floor, site parity, and counterfactual regression
    tests passed.
  target_ids:
  - habitatmech:GOLD.1ce5b3ff1a
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EDEC
  - ETR
  - ESEARCH
  - EPREV
  - ETEST
  - ESYNS
  - EHIST_G2
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: supported
  summary: 'habitatmech:GOLD.1ce5b3ff1a: pleural empyema drainage fluid; UNGROUNDED/REVIEWED;
    parents ["UBERON:0006314"]. Removed the bare medical-device alias ''Empyema drain''
    from exact_synonym in curation/term_requests.tsv (retaining ''empyema chest drain
    fluid'') and added a guarded exclusion row in curation/definition_source_label_exclusions.tsv
    so ''Empyema drain'' is scoped as RELATED_SYNONYM from GOLD (#2286). Identity
    (habitatmech:GOLD.1ce5b3ff1a, ''pleural empyema drainage fluid''), native status,
    hierarchy, and source observations are preserved. No unresolved predecessor finding
    remains in this target scope.'
  target_ids:
  - habitatmech:GOLD.1ce5b3ff1a
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EDEC
  - ETR
  - ESEARCH
  - EPREV
  - ETEST
  - ESYNS
  - EHIST_G2
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks,
    and pools: [{"source": "GOLD", "count": 1, "unit": "ORGANISM"}]. Zero counts are
    omitted; unrelated parent counts are not combined.'
  target_ids:
  - habitatmech:GOLD.1ce5b3ff1a
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EDEC
  - ETR
  - ESEARCH
  - EPREV
  - ETEST
  - ESYNS
  - EHIST_G2
- assessment_id: A4
  area: representation
  topic: Predecessor finding reconciliation
  outcome: supported
  summary: Every predecessor finding preserves its stable issue_key and exact lineage.
    All predecessor findings in this target scope are resolved.
  target_ids:
  - habitatmech:GOLD.1ce5b3ff1a
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EDEC
  - ETR
  - ESEARCH
  - EPREV
  - ETEST
  - ESYNS
  - EHIST_G2
- assessment_id: A5
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: Missing optional parameters/graphs are not evidence deficits. Full source
    decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only
    review does not mutate generated records.
  target_ids:
  - habitatmech:GOLD.1ce5b3ff1a
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EDEC
  - ETR
  - ESEARCH
  - EPREV
  - ETEST
  - ESYNS
  - EHIST_G2
findings:
- finding_id: F1
  issue_key: empyema-drain-device-name-exact-synonym
  category: nomenclature
  severity: major
  status: resolved
  certainty: confirmed
  title: Bare device/procedure label 'Empyema drain' is asserted as an exact drainage-fluid
    synonym
  description: Remove bare 'Empyema drain' from exact_synonym in curation/term_requests.tsv
    for habitatmech:GOLD.1ce5b3ff1a (keeping 'empyema chest drain fluid') and add
    a guarded row in curation/definition_source_label_exclusions.tsv so 'Empyema drain'
    is scoped as RELATED_SYNONYM from GOLD rather than EXACT_SYNONYM.
  target_ids:
  - habitatmech:GOLD.1ce5b3ff1a
  field_paths:
  - synonyms
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EDEC
  - ETR
  - ESEARCH
  - EPREV
  - ETEST
  - ESYNS
  - EHIST_G2
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or representation claim; deterministic
    validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2286
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261101T061210Z-empyema_drain-record
    finding_id: F1
  disposition_reason: Removed bare 'Empyema drain' from exact_synonym in curation/term_requests.tsv
    (retaining 'empyema chest drain fluid') and added a guarded row in curation/definition_source_label_exclusions.tsv
    (#2286) so 'Empyema drain' is emitted as RELATED_SYNONYM from GOLD.
actions: []
limitations:
- Only the stated primary evidence and current ontology/taxonomy authorities were
  independently inspected; original specimen-level support for every source-bin member
  is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism
  or characteristic presence. Parent observations are not inherited by children.
- Configured label correspondence skipped 2,071 no-adapter pairs; this is not whole-corpus
  identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in
  this pre-save observation.
- 'iModulonDB is not applicable: the target has no gene, regulator or expression-module
  assertion. No paid research or scientific-status promotion was performed.'
notes:
- Saved against working-tree repairs atop main commit 95a1eb1b6a5b18b8a5c3b135222b1118f7506ef0;
  all earlier saved bundles in reviews/structured/ remain byte-identical.
- Reconciles predecessor bundle 20261101T061210Z-empyema_drain-record with exact issue_key
  and previous_occurrences lineage.
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261101T061210Z-empyema_drain-record
  relationship: Exact predecessor; every finding explicitly reconciled.
```
