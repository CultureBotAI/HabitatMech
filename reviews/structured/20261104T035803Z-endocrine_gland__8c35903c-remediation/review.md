# Remediation review: endocrine_gland__8c35903c

- Review: 20261104T035803Z-endocrine_gland__8c35903c-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-04T03:55:00Z
- Finished UTC: 2026-11-04T03:58:03Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Removed the guarded GOLD context-parent contribution habitatmech:GOLD.d63e165267 (Endocrine system) via curation/gold_parent_exclusions.tsv (#2285), preserving broader ontology parent UBERON:0002368 (endocrine gland). Identity (habitatmech:GOLD.c26b92ece6), native status, and source observations are preserved. The global NARROW source-attestation endpoint finding (#1398) remains explicitly open.

## Scope And Provenance

Full current target assessment and explicit disposition of every baseline finding on data/habitats/host_associated/endocrine_gland__8c35903c.yaml after bounded Cycle 4 Stage 5 remediation.

Selection: One of nine repaired targets from the empyema_drain-through-epibionts cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 95a1eb1b6a5b18b8a5c3b135222b1118f7506ef0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.c26b92ece6 | data/habitats/host_associated/endocrine_gland__8c35903c.yaml | generated | Endocrine gland |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.c26b92ece6 | Completed 2026-11-01T06:08:08Z. No issues found. |
| validate-strict | passed | True | habitatmech:GOLD.c26b92ece6 | Completed 2026-11-01T06:08:14Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | habitatmech:GOLD.c26b92ece6 | Completed 2026-11-04T03:57:00Z. No issues found; 860 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | habitatmech:GOLD.c26b92ece6 | Completed 2026-11-01T06:08:25Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | habitatmech:GOLD.c26b92ece6 | Completed 2026-11-04T03:57:10Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | habitatmech:GOLD.c26b92ece6 | Completed 2026-11-01T06:08:45Z. validated 63 causal-graph curation file(s) with 63 graph(s). |
| term-requests-check | passed | True | habitatmech:GOLD.c26b92ece6 | Completed 2026-11-04T03:57:15Z. term-request table is current (671 terms). |
| validate-products | passed | True | habitatmech:GOLD.c26b92ece6 | Completed 2026-11-01T06:11:06Z. OK_CANONICAL: 1196, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2071. All id&lt;-&gt;label pairs correspond. |
| pytest counterfactual review repairs | passed | True | habitatmech:GOLD.c26b92ece6 | Completed 2026-11-04T03:58:00Z. 2 passed; exact 9-record counterfactual diff verified. |
| curation-floor | passed | True | habitatmech:GOLD.c26b92ece6 | Completed 2026-11-04T03:58:05Z. Floor satisfied across all 13 metrics. |
| render-check | passed | True | habitatmech:GOLD.c26b92ece6 | Completed 2026-11-04T03:58:30Z. rendered 3209 habitat pages, 750 redirect stubs, 8 categories, 696 term requests; pages/ is in step with the corpus. |

## Scientific And Domain Assessments

### Native validity and reproduction after bounded remediation

schema: supported. Targets: habitatmech:GOLD.c26b92ece6.

Individual schema, strict 24-target validation, 860 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 58 causal overlays, 671 term requests, curation floor, site parity, and counterfactual regression tests passed.

### Identity, definition, hierarchy and aliases

identity: concern. Targets: habitatmech:GOLD.c26b92ece6.

habitatmech:GOLD.c26b92ece6: Endocrine gland; NARROW/SEEDED; parents ["UBERON:0002368"]. Removed the guarded GOLD context-parent contribution habitatmech:GOLD.d63e165267 (Endocrine system) via curation/gold_parent_exclusions.tsv (#2285), preserving broader ontology parent UBERON:0002368 (endocrine gland). Identity (habitatmech:GOLD.c26b92ece6), native status, and source observations are preserved. The global NARROW source-attestation endpoint finding (#1398) remains explicitly open.

### Source counts and retained ranking

quantity: supported. Targets: habitatmech:GOLD.c26b92ece6.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"source": "GOLD", "count": null, "unit": null}]. Zero counts are omitted; unrelated parent counts are not combined.

### Predecessor finding reconciliation

representation: concern. Targets: habitatmech:GOLD.c26b92ece6.

Every predecessor finding preserves its stable issue_key and exact lineage. F1 is resolved under #2285; F2 remains open under corpus-wide issue #1398.

### Parameters, mechanisms and native status

completeness: supported. Targets: habitatmech:GOLD.c26b92ece6.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce SEEDED / NARROW; this read-only review does not mutate generated records.

## Findings

### F1: Human endocrine gland retains human Endocrine system GOLD parent as a superclass

major / resolved / confirmed; issue key: endocrine-gland--8c35903c-context-parent.

Add an exclusion row in curation/gold_parent_exclusions.tsv for habitatmech:GOLD.c26b92ece6 on GOLD path 'Host-associated &gt; Mammals: Human &gt; Endocrine system &gt; Endocrine gland' excluding parent_id habitatmech:GOLD.d63e165267, preserving ontology parent UBERON:0002368 (endocrine gland).

Disposition: Excluded only the guarded GOLD whole-system context-parent contribution habitatmech:GOLD.d63e165267 (Endocrine system) in curation/gold_parent_exclusions.tsv (#2285), preserving broader ontology parent UBERON:0002368 (endocrine gland).

### F2: Narrow mapping predicate points to a minted source-path record

major / open / confirmed; issue key: endocrine-gland--8c35903c-mapping-endpoint-contract.

Reconcile narrow-match source-attestation output with the endpoint contract tracked in Issue #1398 for habitatmech:GOLD.c26b92ece6 (Host-associated &gt; Mammals: Human &gt; Endocrine system &gt; Endocrine gland) and its broader ontology parent UBERON:0002368 (endocrine gland).

Disposition: The retained NARROW source/record endpoint mismatch (#1398) is unchanged; a guarded GOLD context-parent exclusion does not alter the global SourceAttestation.mapping_predicate endpoint contract.

## Recommended Actions And Acceptance Checks

### ACT2

Reconcile narrow-match source-attestation output with the endpoint contract tracked in Issue #1398 for habitatmech:GOLD.c26b92ece6 (Host-associated &gt; Mammals: Human &gt; Endocrine system &gt; Endocrine gland) and its broader ontology parent UBERON:0002368 (endocrine gland). No repair is performed by this read-only review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/endocrine_gland__8c35903c.yaml; Entire YAML | supports | {"identifier": "habitatmech:GOLD.c26b92ece6", "label": "Endocrine gland", "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0002368"], "synonyms": [], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6547", "source_label": "Endocrine gland", "source_path": "Host-associated &gt; Mammals: Human &gt; Endocrine system &gt; Endocrine gland", "mapping_predicate": "skos:narrowMatch", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NARROW."}, {"timestamp": "2026-11-04T00:00:00Z", "curator": "antigravity", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.d63e165267 for habitatmech:GOLD.c26b92ece6 (Host-associated &gt; Mammals: Human &gt; Endocrine system &gt; Endocrine gland). Review https://github.com/CultureBotAI/HabitatMech/issues/2285 : Endocrine gland is an organ part of the endocrine system, not a subtype of the entire mammalian or human endocrine system; human endometrial polyp is a benign uterine mucosal lesion, not a subtype of the cnidarian body-form homonym BTO:0006350 (polyp); endometrium is the inner mucosal lining of the uterus, not the entire human uterus; fruit endophyte environment is an internal fruit tissue habitat, not a subtype of the external fruit surface (carposphere); root endophyte environment is an internal root tissue habitat, not a subtype of the external root surface (rhizoplane). Exclude only exact guarded GOLD source-path contributions, preserving independent genera and all source observations. Exact target habitatmech:GOLD.c26b92ece6. Shared mapping endpoints #1398 remain separate."}]} |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=habitatmech:GOLD.c26b92ece6, grounding_status=NARROW, mapping_status=SEEDED, parent_habitats=["UBERON:0002368"]. |
| EGOLD | data/raw/gold_ecosystem_paths.tsv; TSV rows 2239 | supports | [{"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Mammals: Human &gt; Endocrine system &gt; Endocrine gland", "depth": "4", "ecosystem": "Host-associated", "ecosystem_category": "Mammals: Human", "ecosystem_subtype": "Endocrine gland", "ecosystem_type": "Endocrine system", "gold_node_count": "2", "gold_node_ids": "gold.ecosystem:6547&#124;gold.ecosystem:7059", "leaf_label": "Endocrine gland", "organism_count": "0", "specific_ecosystem": "", "study_count": "0", "total_assertions": "0"}, "row": 2239}] |
| EONT | data/raw/ontology_terms.tsv; TSV rows 13142 | supports | [{"data": {"definition": "Endocrine glands are glands of the endocrine system that secrete their products directly into the circulatory system rather than through a duct.[WP, modified].", "deprecated": "", "directly_referenced": "FALSE", "label": "endocrine gland", "label_only": "FALSE", "ontology": "UBERON", "synonyms": "ductless gland&#124;glandula endocrina&#124;glandulae endocrinae", "term_id": "UBERON:0002368"}, "row": 13142}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 11167,11294,11368,11369,11585 | supports | [{"data": {"object": "UBERON:0002368", "predicate": "rdfs:subClassOf", "subject": "UBERON:0001132"}, "row": 11167}, {"data": {"object": "UBERON:0002368", "predicate": "rdfs:subClassOf", "subject": "UBERON:0002046"}, "row": 11294}, {"data": {"object": "UBERON:0002530", "predicate": "rdfs:subClassOf", "subject": "UBERON:0002368"}, "row": 11368}, {"data": {"object": "UBERON:0002368", "predicate": "rdfs:subClassOf", "subject": "UBERON:0002370"}, "row": 11369}, {"data": {"object": "UBERON:0002368", "predicate": "rdfs:subClassOf", "subject": "UBERON:0006925"}, "row": 11585}] |
| EP2 | data/habitats/host_associated/endocrine_system__fc8977b8.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": null, "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.d63e165267", "label": "Endocrine system", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0000949", "habitatmech:GOLD.cd0b0940e5"], "source_attestations": [{"mapping_predicate": "skos:narrowMatch", "notes": "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:6546", "source_label": "Endocrine system", "source_path": "Host-associated &gt; Mammals: Human &gt; Endocrine system"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'endocrine_gland__8c35903c&#124;habitatmech:GOLD.c26b92ece6' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal verified no prior target review bundle exists for this record; curation and history tables were inspected for all matching rows. |
| EPREV | reviews/structured/20261101T061212Z-endocrine_gland__8c35903c-record/review.yaml; Every immutable Stage 4 baseline finding | supports | Exact predecessor keys and findings reconciled; original inspected source scope preserved. |
| ETEST | tests/test_empyema_drain_to_epibionts_review_repairs.py; Complete full-corpus counterfactual regression suite | supports | Exactly nine records differ from the counterfactual baseline across Issues #2285 and #2286. |
| EPARENTS | curation/gold_parent_exclusions.tsv; TSV line 3 | supports | [[3, "habitatmech:GOLD.c26b92ece6\tHost-associated &gt; Mammals: Human &gt; Endocrine system &gt; Endocrine gland\thabitatmech:GOLD.d63e165267\tantigravity\t2026-11-04\tReview https://github.com/CultureBotAI/HabitatMech/issues/2285 : Endocrine gland is an organ part of the endocrine system, not a subtype of the entire mammalian or human endocrine system; human endometrial polyp is a benign uterine mucosal lesion, not a subtype of the cnidarian body-form homonym BTO:0006350 (polyp); endometrium is the inner mucosal lining of the uterus, not the entire human uterus; fruit endophyte environment is an internal fruit tissue habitat, not a subtype of the external fruit surface (carposphere); root endophyte environment is an internal root tissue habitat, not a subtype of the external root surface (rhizoplane). Exclude only exact guarded GOLD source-path contributions, preserving independent genera and all source observations. Exact target habitatmech:GOLD.c26b92ece6. Shared mapping endpoints #1398 remain separate."]] |
| EHIST_G1 | history/other/gold_parent_exclusions/2026-11-04T034500Z-antigravity-228501.yaml; Complete curation session history event | supports | Authorized curation event for Issue #2285 recorded and validated. |

## Limits And Additional Notes

- Only the stated primary evidence and current ontology/taxonomy authorities were independently inspected; original specimen-level support for every source-bin member is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism or characteristic presence. Parent observations are not inherited by children.
- Configured label correspondence skipped 2,071 no-adapter pairs; this is not whole-corpus identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in this pre-save observation.
- iModulonDB is not applicable: the target has no gene, regulator or expression-module assertion. No paid research or scientific-status promotion was performed.
- Saved against working-tree repairs atop main commit 95a1eb1b6a5b18b8a5c3b135222b1118f7506ef0; all earlier saved bundles in reviews/structured/ remain byte-identical.
- Reconciles predecessor bundle 20261101T061212Z-endocrine_gland__8c35903c-record with exact issue_key and previous_occurrences lineage.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T035803Z-endocrine_gland__8c35903c-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: endocrine_gland__8c35903c'
started_at: '2026-11-04T03:55:00Z'
finished_at: '2026-11-04T03:58:03Z'
reviewer:
  identity: antigravity
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Same agent inspected the full target and source evidence; not
    independent human or second-agent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: Removed the guarded GOLD context-parent contribution habitatmech:GOLD.d63e165267
  (Endocrine system) via curation/gold_parent_exclusions.tsv (#2285), preserving broader
  ontology parent UBERON:0002368 (endocrine gland). Identity (habitatmech:GOLD.c26b92ece6),
  native status, and source observations are preserved. The global NARROW source-attestation
  endpoint finding (#1398) remains explicitly open.
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
  - path: data/habitats/host_associated/endocrine_gland__8c35903c.yaml
    sha256: da28faac60d131fe910ed82de7588966932b2423f188b5c95549731b67e0070f
    role: target
  - path: data/habitats/host_associated/endocrine_system__fc8977b8.yaml
    sha256: d6b61f33e6a697e1b706ee63c485500da4a152c568c728eddc5817cb5edb010c
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
  - path: history/other/definition_source_label_exclusions/2026-11-04T034510Z-antigravity-228601.yaml
    sha256: 257872174c2e52bee3c842c011d691a7cbe702307a33f69531dcbda7c1141333
    role: context
  - path: history/other/gold_parent_exclusions/2026-11-04T034500Z-antigravity-228501.yaml
    sha256: 01cc85edae358f0b99fb26bb0127c93f997cb24f5b87fecb2a496604eb00f230
    role: context
  - path: reviews/structured/20261101T061212Z-endocrine_gland__8c35903c-record/review.yaml
    sha256: 1419256ca7d02beb118dde2eaf31e45165892d6a3f925d142291efe5cecb45c2
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
- target_id: habitatmech:GOLD.c26b92ece6
  path: data/habitats/host_associated/endocrine_gland__8c35903c.yaml
  label: Endocrine gland
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
    finding on data/habitats/host_associated/endocrine_gland__8c35903c.yaml after
    bounded Cycle 4 Stage 5 remediation.
  selection: One of nine repaired targets from the empyema_drain-through-epibionts
    cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.c26b92ece6
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
    --target-class HabitatRecord data/habitats/host_associated/endocrine_gland__8c35903c.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.c26b92ece6
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
  - habitatmech:GOLD.c26b92ece6
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
  - habitatmech:GOLD.c26b92ece6
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
  - habitatmech:GOLD.c26b92ece6
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
  - habitatmech:GOLD.c26b92ece6
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
  - habitatmech:GOLD.c26b92ece6
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
  - habitatmech:GOLD.c26b92ece6
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
  - habitatmech:GOLD.c26b92ece6
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
  - habitatmech:GOLD.c26b92ece6
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
  - habitatmech:GOLD.c26b92ece6
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
  - habitatmech:GOLD.c26b92ece6
  summary: Completed 2026-11-04T03:58:30Z. rendered 3209 habitat pages, 750 redirect
    stubs, 8 categories, 696 term requests; pages/ is in step with the corpus.
  scope_note: Full-corpus static site parity check.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/endocrine_gland__8c35903c.yaml
  locator: Entire YAML
  accessed_at: '2026-11-04T03:58:03Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.c26b92ece6", "label": "Endocrine gland",
    "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0002368"],
    "synonyms": [], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6547",
    "source_label": "Endocrine gland", "source_path": "Host-associated > Mammals:
    Human > Endocrine system > Endocrine gland", "mapping_predicate": "skos:narrowMatch",
    "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}],
    "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources",
    "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories;
    attested by GOLD. Grounding: NARROW."}, {"timestamp": "2026-11-04T00:00:00Z",
    "curator": "antigravity", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded
    GOLD source-path parent contribution habitatmech:GOLD.d63e165267 for habitatmech:GOLD.c26b92ece6
    (Host-associated > Mammals: Human > Endocrine system > Endocrine gland). Review
    https://github.com/CultureBotAI/HabitatMech/issues/2285 : Endocrine gland is an
    organ part of the endocrine system, not a subtype of the entire mammalian or human
    endocrine system; human endometrial polyp is a benign uterine mucosal lesion,
    not a subtype of the cnidarian body-form homonym BTO:0006350 (polyp); endometrium
    is the inner mucosal lining of the uterus, not the entire human uterus; fruit
    endophyte environment is an internal fruit tissue habitat, not a subtype of the
    external fruit surface (carposphere); root endophyte environment is an internal
    root tissue habitat, not a subtype of the external root surface (rhizoplane).
    Exclude only exact guarded GOLD source-path contributions, preserving independent
    genera and all source observations. Exact target habitatmech:GOLD.c26b92ece6.
    Shared mapping endpoints #1398 remain separate."}]}'
  snapshot_sha256: da28faac60d131fe910ed82de7588966932b2423f188b5c95549731b67e0070f
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-04T03:58:03Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon terms cannot substitute
    for associated environments; parent_habitats must be strictly broader across all
    contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-04T03:58:03Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-04T03:58:03Z'
  support: supports
  summary: Seed generator produces identifier=habitatmech:GOLD.c26b92ece6, grounding_status=NARROW,
    mapping_status=SEEDED, parent_habitats=["UBERON:0002368"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EGOLD
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV rows 2239
  accessed_at: '2026-11-04T03:58:03Z'
  support: supports
  summary: '[{"data": {"biosample_count": "0", "canonical_path": "Host-associated
    > Mammals: Human > Endocrine system > Endocrine gland", "depth": "4", "ecosystem":
    "Host-associated", "ecosystem_category": "Mammals: Human", "ecosystem_subtype":
    "Endocrine gland", "ecosystem_type": "Endocrine system", "gold_node_count": "2",
    "gold_node_ids": "gold.ecosystem:6547|gold.ecosystem:7059", "leaf_label": "Endocrine
    gland", "organism_count": "0", "specific_ecosystem": "", "study_count": "0", "total_assertions":
    "0"}, "row": 2239}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 13142
  accessed_at: '2026-11-04T03:58:03Z'
  support: supports
  summary: '[{"data": {"definition": "Endocrine glands are glands of the endocrine
    system that secrete their products directly into the circulatory system rather
    than through a duct.[WP, modified].", "deprecated": "", "directly_referenced":
    "FALSE", "label": "endocrine gland", "label_only": "FALSE", "ontology": "UBERON",
    "synonyms": "ductless gland|glandula endocrina|glandulae endocrinae", "term_id":
    "UBERON:0002368"}, "row": 13142}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 11167,11294,11368,11369,11585
  accessed_at: '2026-11-04T03:58:03Z'
  support: supports
  summary: '[{"data": {"object": "UBERON:0002368", "predicate": "rdfs:subClassOf",
    "subject": "UBERON:0001132"}, "row": 11167}, {"data": {"object": "UBERON:0002368",
    "predicate": "rdfs:subClassOf", "subject": "UBERON:0002046"}, "row": 11294}, {"data":
    {"object": "UBERON:0002530", "predicate": "rdfs:subClassOf", "subject": "UBERON:0002368"},
    "row": 11368}, {"data": {"object": "UBERON:0002368", "predicate": "rdfs:subClassOf",
    "subject": "UBERON:0002370"}, "row": 11369}, {"data": {"object": "UBERON:0002368",
    "predicate": "rdfs:subClassOf", "subject": "UBERON:0006925"}, "row": 11585}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EP2
  kind: record_content
  reference: data/habitats/host_associated/endocrine_system__fc8977b8.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-11-04T03:58:03Z'
  support: supports
  summary: '{"definition": null, "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.d63e165267",
    "label": "Endocrine system", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0000949",
    "habitatmech:GOLD.cd0b0940e5"], "source_attestations": [{"mapping_predicate":
    "skos:narrowMatch", "notes": "3 GOLD ecosystem node ids share this path; first
    shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id":
    "gold.ecosystem:6546", "source_label": "Endocrine system", "source_path": "Host-associated
    > Mammals: Human > Endocrine system"}]}'
  snapshot_sha256: d6b61f33e6a697e1b706ee63c485500da4a152c568c728eddc5817cb5edb010c
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'endocrine_gland__8c35903c|habitatmech:GOLD.c26b92ece6' reviews/structured/*/review.yaml
    curation/ history/
  accessed_at: '2026-11-04T03:58:03Z'
  support: context_only
  summary: Structured-review traversal verified no prior target review bundle exists
    for this record; curation and history tables were inspected for all matching rows.
  search_scope: curation, history, data/raw, and reviews/structured/*/review.yaml
    traversal at commit ad20de05c38d4fadf667b5c579eef50496b31b02.
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261101T061212Z-endocrine_gland__8c35903c-record/review.yaml
  locator: Every immutable Stage 4 baseline finding
  accessed_at: '2026-11-04T03:58:03Z'
  support: supports
  summary: Exact predecessor keys and findings reconciled; original inspected source
    scope preserved.
  snapshot_sha256: 1419256ca7d02beb118dde2eaf31e45165892d6a3f925d142291efe5cecb45c2
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_empyema_drain_to_epibionts_review_repairs.py
  locator: Complete full-corpus counterfactual regression suite
  accessed_at: '2026-11-04T03:58:03Z'
  support: supports
  summary: 'Exactly nine records differ from the counterfactual baseline across Issues
    #2285 and #2286.'
  snapshot_sha256: bbd37dbb824e90efe994ab4a44b01b16d9ed4a5b039fb66aa902192a4752036c
- evidence_id: EPARENTS
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: TSV line 3
  accessed_at: '2026-11-04T03:58:03Z'
  support: supports
  summary: '[[3, "habitatmech:GOLD.c26b92ece6\tHost-associated > Mammals: Human >
    Endocrine system > Endocrine gland\thabitatmech:GOLD.d63e165267\tantigravity\t2026-11-04\tReview
    https://github.com/CultureBotAI/HabitatMech/issues/2285 : Endocrine gland is an
    organ part of the endocrine system, not a subtype of the entire mammalian or human
    endocrine system; human endometrial polyp is a benign uterine mucosal lesion,
    not a subtype of the cnidarian body-form homonym BTO:0006350 (polyp); endometrium
    is the inner mucosal lining of the uterus, not the entire human uterus; fruit
    endophyte environment is an internal fruit tissue habitat, not a subtype of the
    external fruit surface (carposphere); root endophyte environment is an internal
    root tissue habitat, not a subtype of the external root surface (rhizoplane).
    Exclude only exact guarded GOLD source-path contributions, preserving independent
    genera and all source observations. Exact target habitatmech:GOLD.c26b92ece6.
    Shared mapping endpoints #1398 remain separate."]]'
  snapshot_sha256: ec8f7b5cf7b804e31663653e482be907b0333a8be807259eec024fcb7acfeb94
- evidence_id: EHIST_G1
  kind: record_content
  reference: history/other/gold_parent_exclusions/2026-11-04T034500Z-antigravity-228501.yaml
  locator: Complete curation session history event
  accessed_at: '2026-11-04T03:58:03Z'
  support: supports
  summary: 'Authorized curation event for Issue #2285 recorded and validated.'
  snapshot_sha256: 01cc85edae358f0b99fb26bb0127c93f997cb24f5b87fecb2a496604eb00f230
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
  - habitatmech:GOLD.c26b92ece6
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EP2
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST_G1
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: concern
  summary: 'habitatmech:GOLD.c26b92ece6: Endocrine gland; NARROW/SEEDED; parents ["UBERON:0002368"].
    Removed the guarded GOLD context-parent contribution habitatmech:GOLD.d63e165267
    (Endocrine system) via curation/gold_parent_exclusions.tsv (#2285), preserving
    broader ontology parent UBERON:0002368 (endocrine gland). Identity (habitatmech:GOLD.c26b92ece6),
    native status, and source observations are preserved. The global NARROW source-attestation
    endpoint finding (#1398) remains explicitly open.'
  target_ids:
  - habitatmech:GOLD.c26b92ece6
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EP2
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST_G1
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks,
    and pools: [{"source": "GOLD", "count": null, "unit": null}]. Zero counts are
    omitted; unrelated parent counts are not combined.'
  target_ids:
  - habitatmech:GOLD.c26b92ece6
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EP2
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST_G1
- assessment_id: A4
  area: representation
  topic: Predecessor finding reconciliation
  outcome: concern
  summary: 'Every predecessor finding preserves its stable issue_key and exact lineage.
    F1 is resolved under #2285; F2 remains open under corpus-wide issue #1398.'
  target_ids:
  - habitatmech:GOLD.c26b92ece6
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EP2
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST_G1
- assessment_id: A5
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: Missing optional parameters/graphs are not evidence deficits. Full source
    decisions and executed routes reproduce SEEDED / NARROW; this read-only review
    does not mutate generated records.
  target_ids:
  - habitatmech:GOLD.c26b92ece6
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EP2
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST_G1
findings:
- finding_id: F1
  issue_key: endocrine-gland--8c35903c-context-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Human endocrine gland retains human Endocrine system GOLD parent as a superclass
  description: 'Add an exclusion row in curation/gold_parent_exclusions.tsv for habitatmech:GOLD.c26b92ece6
    on GOLD path ''Host-associated > Mammals: Human > Endocrine system > Endocrine
    gland'' excluding parent_id habitatmech:GOLD.d63e165267, preserving ontology parent
    UBERON:0002368 (endocrine gland).'
  target_ids:
  - habitatmech:GOLD.c26b92ece6
  field_paths:
  - parent_habitats
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EP2
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST_G1
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or representation claim; deterministic
    validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2285
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261101T061212Z-endocrine_gland__8c35903c-record
    finding_id: F1
  disposition_reason: Excluded only the guarded GOLD whole-system context-parent contribution
    habitatmech:GOLD.d63e165267 (Endocrine system) in curation/gold_parent_exclusions.tsv
    (#2285), preserving broader ontology parent UBERON:0002368 (endocrine gland).
- finding_id: F2
  issue_key: endocrine-gland--8c35903c-mapping-endpoint-contract
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Narrow mapping predicate points to a minted source-path record
  description: 'Reconcile narrow-match source-attestation output with the endpoint
    contract tracked in Issue #1398 for habitatmech:GOLD.c26b92ece6 (Host-associated
    > Mammals: Human > Endocrine system > Endocrine gland) and its broader ontology
    parent UBERON:0002368 (endocrine gland).'
  target_ids:
  - habitatmech:GOLD.c26b92ece6
  field_paths:
  - identifier
  - grounding_status
  - parent_habitats
  - source_attestations[0].mapping_predicate
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EP2
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST_G1
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: docs/CURATION.md
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or representation claim; deterministic
    validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261101T061212Z-endocrine_gland__8c35903c-record
    finding_id: F2
  disposition_reason: The retained NARROW source/record endpoint mismatch (#1398)
    is unchanged; a guarded GOLD context-parent exclusion does not alter the global
    SourceAttestation.mapping_predicate endpoint contract.
actions:
- action_id: ACT2
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.c26b92ece6
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: docs/CURATION.md
    role: Maintained input or generator; never patch generated habitat YAML
  description: 'Reconcile narrow-match source-attestation output with the endpoint
    contract tracked in Issue #1398 for habitatmech:GOLD.c26b92ece6 (Host-associated
    > Mammals: Human > Endocrine system > Endocrine gland) and its broader ontology
    parent UBERON:0002368 (endocrine gland). No repair is performed by this read-only
    review.'
  generator: Controlled source/curation update in Stage 5, then just seed, guarded
    just seed-canary, just seed-apply, and dependent term-request/map/site/redirect
    regeneration.
  acceptance_checks:
  - Regress the exact reported claim and preserve independently valid identifiers,
    source counts/units, raw provenance, native status and history.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
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
- Reconciles predecessor bundle 20261101T061212Z-endocrine_gland__8c35903c-record
  with exact issue_key and previous_occurrences lineage.
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261101T061212Z-endocrine_gland__8c35903c-record
  relationship: Exact predecessor; every finding explicitly reconciled.
```
