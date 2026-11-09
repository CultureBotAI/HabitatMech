# Remediation review: fin

- Review: 20261108T154507Z-fin-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-08T15:35:00Z
- Finished UTC: 2026-11-08T15:45:07Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Removed the guarded GOLD whole-organ context-parent contribution habitatmech:GOLD.92e3c832eb (fish Skin) for source concept habitatmech:GOLD.8634ec53de ('Host-associated &gt; Fish &gt; Integumentary system &gt; Skin &gt; Fin') via curation/gold_parent_exclusions.tsv (#2318), preserving broader ontology parent UBERON:0000026 (appendage). Identity (UBERON:0008897, 'fin'), native SEEDED/EXACT status, and source observations are preserved. No unresolved predecessor finding remains in this target scope.

## Scope And Provenance

Full current target assessment and explicit disposition of every baseline finding on data/habitats/host_associated/fin.yaml after bounded Cycle 7 Stage 5 remediation.

Selection: One of seven repaired targets from the fecal__0d8696a2-through-fin cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8e2744f4c33769669e5e9a66a4ae9e27a9642590.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| UBERON:0008897 | data/habitats/host_associated/fin.yaml | generated | fin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | UBERON:0008897 | Completed 2026-11-08T15:42:12Z. No issues found against src/habitatmech/schema/habitatmech.yaml. |
| validate-strict | passed | True | UBERON:0008897 | Completed 2026-11-08T15:42:18Z. 24 checked, 0 failed; target passed closed-schema validation. |
| validate-history | passed | True | UBERON:0008897 | Completed 2026-11-08T15:42:25Z. No issues found; 872 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | UBERON:0008897 | Completed 2026-11-08T15:42:30Z. 14 inventory files and 2 GOLD export files verified. |
| verify-corpus | passed | True | UBERON:0008897 | Completed 2026-11-08T15:42:40Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | UBERON:0008897 | Completed 2026-11-08T15:42:45Z. 93 causal-graph curations and target records validated. |
| term-requests-check | passed | True | UBERON:0008897 | Completed 2026-11-08T15:42:50Z. term-request table is current (674 terms). |
| validate-products | passed | True | UBERON:0008897 | Completed 2026-11-08T15:42:55Z. 24 records, 0 label drift findings. |
| pytest counterfactual review repairs | passed | True | UBERON:0008897 | Completed 2026-11-08T15:43:00Z. 2 passed; exact 7-record counterfactual diff verified. |
| curation-floor | passed | True | UBERON:0008897 | Completed 2026-11-08T15:43:05Z. Floor satisfied across all 13 metrics. |
| render-check | passed | True | UBERON:0008897 | Completed 2026-11-08T15:44:50Z. rendered 3209 habitat pages, 753 redirect stubs, 8 categories, 699 term requests; pages/ is in step with the corpus. |

## Scientific And Domain Assessments

### Native validity and reproduction after bounded remediation

schema: supported. Targets: UBERON:0008897.

Individual schema, strict 24-target validation, 872 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 93 causal overlays, 674 term requests, curation floor, site parity, and counterfactual regression tests passed.

### Identity, definition, hierarchy and aliases

identity: supported. Targets: UBERON:0008897.

UBERON:0008897: fin; EXACT/SEEDED; parents ["UBERON:0000026"]. Removed the guarded GOLD whole-organ context-parent contribution habitatmech:GOLD.92e3c832eb (fish Skin) for source concept habitatmech:GOLD.8634ec53de ('Host-associated &gt; Fish &gt; Integumentary system &gt; Skin &gt; Fin') via curation/gold_parent_exclusions.tsv (#2318), preserving broader ontology parent UBERON:0000026 (appendage). Identity (UBERON:0008897, 'fin'), native SEEDED/EXACT status, and source observations are preserved. No unresolved predecessor finding remains in this target scope.

### Source counts and retained ranking

quantity: supported. Targets: UBERON:0008897.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"source": "GOLD", "count": null, "unit": null}]. Zero counts are omitted; unrelated parent counts are not combined.

### Predecessor finding reconciliation

representation: supported. Targets: UBERON:0008897.

Every predecessor finding preserves its stable issue_key and exact lineage. All predecessor findings in this target scope are resolved.

### Parameters, mechanisms and native status

completeness: supported. Targets: UBERON:0008897.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce SEEDED / EXACT; this read-only review does not mutate generated records.

## Findings

### F1: Fin retains piscine Skin GOLD parent as a superclass

major / resolved / confirmed; issue key: fin-context-parent.

Add an exclusion row in curation/gold_parent_exclusions.tsv for source identifier habitatmech:GOLD.e0bc7cc171 on GOLD path 'Host-associated &gt; Fish &gt; Integumentary system &gt; Skin &gt; Fin' (exact target UBERON:0008897) excluding parent_id habitatmech:GOLD.92e3c832eb (Skin), preserving ontology parent UBERON:0000026 (appendage) and matching sibling feather (#2304).

Disposition: Excluded only the guarded GOLD whole-organ context-parent contribution habitatmech:GOLD.92e3c832eb (fish Skin) for source concept habitatmech:GOLD.8634ec53de in curation/gold_parent_exclusions.tsv (#2318), preserving broader ontology parent UBERON:0000026 (appendage).

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/fin.yaml; Entire YAML | supports | {"identifier": "UBERON:0008897", "label": "fin", "grounding_status": "EXACT", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0000026"], "xrefs": [], "synonyms": [{"synonym_text": "fins", "synonym_type": "EXACT_SYNONYM", "source": "UBERON"}], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6922", "source_label": "Fin", "source_path": "Host-associated &gt; Fish &gt; Integumentary system &gt; Skin &gt; Fin", "mapping_predicate": "skos:exactMatch"}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: EXACT."}, {"timestamp": "2026-11-08T00:00:00Z", "curator": "antigravity", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.92e3c832eb for habitatmech:GOLD.8634ec53de (Host-associated &gt; Fish &gt; Integumentary system &gt; Skin &gt; Fin). Review https://github.com/CultureBotAI/HabitatMech/issues/2318 : Feces and earthworm casts are egested digestive waste material, not subtypes of the digestive tract or of the human, mammalian, or avian large intestine organ; a fish fin is a locomotory appendage, not a subtype of the whole fish skin organ. Exclude only exact guarded GOLD source-path contributions, preserving independent genera and all source observations. Exact target UBERON:0008897. Shared mapping endpoints #1398 remain separate."}]} |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon and life-stage organism terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=UBERON:0008897, grounding_status=EXACT, mapping_status=SEEDED, parent_habitats=["UBERON:0000026"], xrefs=[]. |
| ESIB1 | data/habitats/host_associated/feather.yaml; Entire YAML | supports | Sibling integumentary appendage record BTO:0000447 (feather) where whole-organ Skin GOLD parent was excluded via curation/gold_parent_exclusions.tsv (#2304). |
| EGOLD | data/raw/gold_ecosystem_paths.tsv; TSV rows 1940 | supports | [{"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Fish &gt; Integumentary system &gt; Skin &gt; Fin", "depth": "5", "ecosystem": "Host-associated", "ecosystem_category": "Fish", "ecosystem_subtype": "Skin", "ecosystem_type": "Integumentary system", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:6922", "leaf_label": "Fin", "organism_count": "0", "specific_ecosystem": "Fin", "study_count": "0", "total_assertions": "0"}, "row": 1940}] |
| EONT | data/raw/ontology_terms.tsv; TSV rows 12877,13365 | supports | [{"data": {"definition": "Major subdivision of an organism that protrudes from the body[DOS, CARO].", "deprecated": "", "directly_referenced": "FALSE", "label": "appendage", "label_only": "FALSE", "ontology": "UBERON", "synonyms": "appendages&#124;extremitaet&#124;extremity&#124;limbs/digits/tail", "term_id": "UBERON:0000026"}, "row": 12877}, {"data": {"definition": "An external projection of an aquatic animal as a fish used in propelling or guiding the body[BTO].", "deprecated": "", "directly_referenced": "FALSE", "label": "fin", "label_only": "FALSE", "ontology": "UBERON", "synonyms": "fins", "term_id": "UBERON:0008897"}, "row": 13365}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 10989,11488,11655,11670 | supports | [{"data": {"object": "UBERON:0000475", "predicate": "rdfs:subClassOf", "subject": "UBERON:0000026"}, "row": 10989}, {"data": {"object": "UBERON:0000026", "predicate": "rdfs:subClassOf", "subject": "UBERON:0004708"}, "row": 11488}, {"data": {"object": "UBERON:0000026", "predicate": "rdfs:subClassOf", "subject": "UBERON:0008897"}, "row": 11655}, {"data": {"object": "UBERON:0000026", "predicate": "rdfs:subClassOf", "subject": "UBERON:0009719"}, "row": 11670}] |
| EP2 | data/habitats/host_associated/skin__9a5d285e.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": null, "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.92e3c832eb", "label": "Skin", "mapping_status": "SEEDED", "parent_habitats": ["BTO:0001253", "habitatmech:GOLD.d980919c41"], "source_attestations": [{"assertion_count": 52, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:narrowMatch", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:6919", "source_label": "Skin", "source_path": "Host-associated &gt; Fish &gt; Integumentary system &gt; Skin"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'fin&#124;UBERON:0008897' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal located Stage 4 predecessor bundle 20261108T114933Z-fin-record (linked via EPREV and related_reviews) and checked related cohort and ancestor reviews for reconciliation. |
| EPARENTS | curation/gold_parent_exclusions.tsv; TSV line 6 | supports | [[6, "habitatmech:GOLD.8634ec53de\tHost-associated &gt; Fish &gt; Integumentary system &gt; Skin &gt; Fin\thabitatmech:GOLD.92e3c832eb\tantigravity\t2026-11-08\tReview https://github.com/CultureBotAI/HabitatMech/issues/2318 : Feces and earthworm casts are egested digestive waste material, not subtypes of the digestive tract or of the human, mammalian, or avian large intestine organ; a fish fin is a locomotory appendage, not a subtype of the whole fish skin organ. Exclude only exact guarded GOLD source-path contributions, preserving independent genera and all source observations. Exact target UBERON:0008897. Shared mapping endpoints #1398 remain separate."]] |
| EPREV | reviews/structured/20261108T114933Z-fin-record/review.yaml; Every immutable Stage 4 baseline finding | supports | Exact predecessor keys and findings reconciled; original inspected source scope preserved. |
| ETEST | tests/test_fecal_0d8696a2_to_fin_review_repairs.py; Complete full-corpus counterfactual regression suite | supports | Exactly seven records differ from the counterfactual baseline across Issues #2318 and #2319. |
| EHIST_G1 | history/other/gold_parent_exclusions/2026-11-08T153500Z-antigravity-231801.yaml; Complete curation session history event | supports | Authorized curation event for Issue #2318 recorded and validated. |

## Limits And Additional Notes

- Only the stated primary evidence and current ontology/taxonomy authorities were independently inspected; original specimen-level support for every source-bin member is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism or characteristic presence. Parent observations are not inherited by children.
- Configured label correspondence skipped 2,088 no-adapter pairs; this is not whole-corpus identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in this pre-save observation.
- iModulonDB is not applicable: the target has no gene, regulator or expression-module assertion. No paid research or scientific-status promotion was performed.
- Saved against working-tree repairs atop main commit 8e2744f4c33769669e5e9a66a4ae9e27a9642590; all earlier saved bundles in reviews/structured/ remain byte-identical.
- Reconciles predecessor bundle 20261108T114933Z-fin-record with exact issue_key and previous_occurrences lineage.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261108T154507Z-fin-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: fin'
started_at: '2026-11-08T15:35:00Z'
finished_at: '2026-11-08T15:45:07Z'
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
summary: Removed the guarded GOLD whole-organ context-parent contribution habitatmech:GOLD.92e3c832eb
  (fish Skin) for source concept habitatmech:GOLD.8634ec53de ('Host-associated > Fish
  > Integumentary system > Skin > Fin') via curation/gold_parent_exclusions.tsv (#2318),
  preserving broader ontology parent UBERON:0000026 (appendage). Identity (UBERON:0008897,
  'fin'), native SEEDED/EXACT status, and source observations are preserved. No unresolved
  predecessor finding remains in this target scope.
source:
  git_revision: 8e2744f4c33769669e5e9a66a4ae9e27a9642590
  state: working_tree
  inputs:
  - path: curation/decisions.tsv
    sha256: d3bf0a3ca3570e8f318898db92f800a1e13220f64112fe5c1ce1edc9181c3ae2
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: f53415b9d57f351620a1722c7c83414983899dd9a4559d42e9a094a3e8f501e8
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: f004c15e7d206d673bdd9e6d051f6fce93c8a06ebe4db6026149d4d00c49cc9e
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: c1207270bb0ae2031e42de6cb8220b20f98886f65e40d48793bfd7e9d757d83a
    role: context
  - path: curation/term_requests.tsv
    sha256: ad853d6290dd72b2451d945a0545a5dc5272cc37c2296eaab78c99d2872d4b0c
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/host_associated/feather.yaml
    sha256: 3f4cc8e939f689b41c9f84474dd6af35acaec98855baeab7e38a7423af16a460
    role: context
  - path: data/habitats/host_associated/fin.yaml
    sha256: 64af3b171425e86bccb2f2ded0308c8fca835228377ba86a43eeb33baad1de8e
    role: target
  - path: data/habitats/host_associated/skin__9a5d285e.yaml
    sha256: edc7b8f13b76bc7d0cc3692eb5f59d4c9e678fa86e3074cd21457a5d7293c5bb
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
  - path: history/other/definition_source_label_exclusions/2026-11-08T153510Z-antigravity-231901.yaml
    sha256: e28d82abe703f19ad589f62f7e93ca573a8ebb71bfab13030a83059e974d2126
    role: context
  - path: history/other/gold_parent_exclusions/2026-11-08T153500Z-antigravity-231801.yaml
    sha256: 0238f5404c80e4c6e0f01acbaf496cb3a6a304632fe3c51122e348ea0e39c919
    role: context
  - path: reviews/structured/20261108T114933Z-fin-record/review.yaml
    sha256: ffb7aa1e17e0fa65947b1e572feb9eb9cbc850e63b0068a1a7bb41fe31382280
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
    role: context
  - path: src/habitatmech/seed.py
    sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
    role: context
  - path: tests/test_fecal_0d8696a2_to_fin_review_repairs.py
    sha256: db50d90f8a6296e1914051aa62fe928ab03d264f44cc8cbfb1c822f9f9ec650c
    role: context
targets:
- target_id: UBERON:0008897
  path: data/habitats/host_associated/fin.yaml
  label: fin
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
    finding on data/habitats/host_associated/fin.yaml after bounded Cycle 7 Stage
    5 remediation.
  selection: One of seven repaired targets from the fecal__0d8696a2-through-fin cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - UBERON:0008897
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
    --target-class HabitatRecord data/habitats/host_associated/fin.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0008897
  summary: Completed 2026-11-08T15:42:12Z. No issues found against src/habitatmech/schema/habitatmech.yaml.
  scope_note: Individual schema; strict command covers the 24 named cohort targets;
    other documented gates have full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/habitats/host_associated/fecal__0d8696a2.yaml
    data/habitats/host_associated/fecal__0e10427f.yaml data/habitats/host_associated/fecal__69dad039.yaml
    data/habitats/host_associated/fecal__89494a72.yaml data/habitats/host_associated/fecal__c047ee1e.yaml
    data/habitats/host_associated/fecal__ceae17b6.yaml data/habitats/host_associated/fecal__d12909cd.yaml
    data/habitats/host_associated/fecal__e9f04eec.yaml data/habitats/host_associated/feces.yaml
    data/habitats/host_associated/felidae_cat.yaml data/habitats/host_associated/female_reproductive_system.yaml
    data/habitats/host_associated/fetal_tissue.yaml data/habitats/host_associated/fetal_tissue__610eb0c8.yaml
    data/habitats/host_associated/fetus.yaml data/habitats/host_associated/fetus__250e9844.yaml
    data/habitats/host_associated/fiber.yaml data/habitats/host_associated/fibroblast.yaml
    data/habitats/host_associated/fibrocartilage.yaml data/habitats/host_associated/fibrocartilage__9cc92423.yaml
    data/habitats/host_associated/fibroma.yaml data/habitats/host_associated/filament.yaml
    data/habitats/host_associated/filiform_warts.yaml data/habitats/host_associated/filter_chamber.yaml
    data/habitats/host_associated/fin.yaml --out .temp/c7s4_24_strict.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0008897
  summary: Completed 2026-11-08T15:42:18Z. 24 checked, 0 failed; target passed closed-schema
    validation.
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
  - UBERON:0008897
  summary: Completed 2026-11-08T15:42:25Z. No issues found; 872 history record(s)
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
  - UBERON:0008897
  summary: Completed 2026-11-08T15:42:30Z. 14 inventory files and 2 GOLD export files
    verified.
  scope_note: Full-corpus raw inventory provenance verification.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: .venv/bin/python scripts/verify_corpus.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0008897
  summary: 'Completed 2026-11-08T15:42:40Z. expected 3209 records, found 3209 on disk;
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
  - UBERON:0008897
  summary: Completed 2026-11-08T15:42:45Z. 93 causal-graph curations and target records
    validated.
  scope_note: Full-corpus causal-graph overlay validation.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: .venv/bin/python scripts/build_term_requests.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0008897
  summary: Completed 2026-11-08T15:42:50Z. term-request table is current (674 terms).
  scope_note: Full-corpus term-request table currency check.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0008897
  summary: Completed 2026-11-08T15:42:55Z. 24 records, 0 label drift findings.
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
- check_id: C9
  name: pytest counterfactual review repairs
  status: passed
  required: true
  command: .venv/bin/python -m pytest tests/test_fecal_0d8696a2_to_fin_review_repairs.py
    -q --no-cov
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0008897
  summary: Completed 2026-11-08T15:43:00Z. 2 passed; exact 7-record counterfactual
    diff verified.
  scope_note: 'Full-corpus counterfactual regression test for Issues #2318 and #2319.'
- check_id: C10
  name: curation-floor
  status: passed
  required: true
  command: .venv/bin/python scripts/check_curation_floor.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0008897
  summary: Completed 2026-11-08T15:43:05Z. Floor satisfied across all 13 metrics.
  scope_note: Full-corpus curation floor ratchets.
- check_id: C11
  name: render-check
  status: passed
  required: true
  command: .venv/bin/python scripts/render_pages.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0008897
  summary: Completed 2026-11-08T15:44:50Z. rendered 3209 habitat pages, 753 redirect
    stubs, 8 categories, 699 term requests; pages/ is in step with the corpus.
  scope_note: Full-corpus static site parity check.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/fin.yaml
  locator: Entire YAML
  accessed_at: '2026-11-08T15:45:07Z'
  support: supports
  summary: '{"identifier": "UBERON:0008897", "label": "fin", "grounding_status": "EXACT",
    "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0000026"], "xrefs": [],
    "synonyms": [{"synonym_text": "fins", "synonym_type": "EXACT_SYNONYM", "source":
    "UBERON"}], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6922",
    "source_label": "Fin", "source_path": "Host-associated > Fish > Integumentary
    system > Skin > Fin", "mapping_predicate": "skos:exactMatch"}], "curation_history":
    [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action":
    "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested
    by GOLD. Grounding: EXACT."}, {"timestamp": "2026-11-08T00:00:00Z", "curator":
    "antigravity", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path
    parent contribution habitatmech:GOLD.92e3c832eb for habitatmech:GOLD.8634ec53de
    (Host-associated > Fish > Integumentary system > Skin > Fin). Review https://github.com/CultureBotAI/HabitatMech/issues/2318
    : Feces and earthworm casts are egested digestive waste material, not subtypes
    of the digestive tract or of the human, mammalian, or avian large intestine organ;
    a fish fin is a locomotory appendage, not a subtype of the whole fish skin organ.
    Exclude only exact guarded GOLD source-path contributions, preserving independent
    genera and all source observations. Exact target UBERON:0008897. Shared mapping
    endpoints #1398 remain separate."}]}'
  snapshot_sha256: 64af3b171425e86bccb2f2ded0308c8fca835228377ba86a43eeb33baad1de8e
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-08T15:45:07Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon and life-stage
    organism terms cannot substitute for associated environments; parent_habitats
    must be strictly broader across all contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-08T15:45:07Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-08T15:45:07Z'
  support: supports
  summary: Seed generator produces identifier=UBERON:0008897, grounding_status=EXACT,
    mapping_status=SEEDED, parent_habitats=["UBERON:0000026"], xrefs=[].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: ESIB1
  kind: record_content
  reference: data/habitats/host_associated/feather.yaml
  locator: Entire YAML
  accessed_at: '2026-11-08T15:45:07Z'
  support: supports
  summary: Sibling integumentary appendage record BTO:0000447 (feather) where whole-organ
    Skin GOLD parent was excluded via curation/gold_parent_exclusions.tsv (#2304).
  snapshot_sha256: 3f4cc8e939f689b41c9f84474dd6af35acaec98855baeab7e38a7423af16a460
- evidence_id: EGOLD
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV rows 1940
  accessed_at: '2026-11-08T15:45:07Z'
  support: supports
  summary: '[{"data": {"biosample_count": "0", "canonical_path": "Host-associated
    > Fish > Integumentary system > Skin > Fin", "depth": "5", "ecosystem": "Host-associated",
    "ecosystem_category": "Fish", "ecosystem_subtype": "Skin", "ecosystem_type": "Integumentary
    system", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:6922", "leaf_label":
    "Fin", "organism_count": "0", "specific_ecosystem": "Fin", "study_count": "0",
    "total_assertions": "0"}, "row": 1940}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 12877,13365
  accessed_at: '2026-11-08T15:45:07Z'
  support: supports
  summary: '[{"data": {"definition": "Major subdivision of an organism that protrudes
    from the body[DOS, CARO].", "deprecated": "", "directly_referenced": "FALSE",
    "label": "appendage", "label_only": "FALSE", "ontology": "UBERON", "synonyms":
    "appendages|extremitaet|extremity|limbs/digits/tail", "term_id": "UBERON:0000026"},
    "row": 12877}, {"data": {"definition": "An external projection of an aquatic animal
    as a fish used in propelling or guiding the body[BTO].", "deprecated": "", "directly_referenced":
    "FALSE", "label": "fin", "label_only": "FALSE", "ontology": "UBERON", "synonyms":
    "fins", "term_id": "UBERON:0008897"}, "row": 13365}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 10989,11488,11655,11670
  accessed_at: '2026-11-08T15:45:07Z'
  support: supports
  summary: '[{"data": {"object": "UBERON:0000475", "predicate": "rdfs:subClassOf",
    "subject": "UBERON:0000026"}, "row": 10989}, {"data": {"object": "UBERON:0000026",
    "predicate": "rdfs:subClassOf", "subject": "UBERON:0004708"}, "row": 11488}, {"data":
    {"object": "UBERON:0000026", "predicate": "rdfs:subClassOf", "subject": "UBERON:0008897"},
    "row": 11655}, {"data": {"object": "UBERON:0000026", "predicate": "rdfs:subClassOf",
    "subject": "UBERON:0009719"}, "row": 11670}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EP2
  kind: record_content
  reference: data/habitats/host_associated/skin__9a5d285e.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-11-08T15:45:07Z'
  support: supports
  summary: '{"definition": null, "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.92e3c832eb",
    "label": "Skin", "mapping_status": "SEEDED", "parent_habitats": ["BTO:0001253",
    "habitatmech:GOLD.d980919c41"], "source_attestations": [{"assertion_count": 52,
    "assertion_unit": "ORGANISM", "mapping_predicate": "skos:narrowMatch", "notes":
    "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.",
    "source": "GOLD", "source_id": "gold.ecosystem:6919", "source_label": "Skin",
    "source_path": "Host-associated > Fish > Integumentary system > Skin"}]}'
  snapshot_sha256: edc7b8f13b76bc7d0cc3692eb5f59d4c9e678fa86e3074cd21457a5d7293c5bb
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'fin|UBERON:0008897' reviews/structured/*/review.yaml curation/
    history/
  accessed_at: '2026-11-08T15:45:07Z'
  support: context_only
  summary: Structured-review traversal located Stage 4 predecessor bundle 20261108T114933Z-fin-record
    (linked via EPREV and related_reviews) and checked related cohort and ancestor
    reviews for reconciliation.
  search_scope: curation, history, data/raw, and reviews/structured/*/review.yaml
    traversal at commit 6a699ab5f6f775ca0c18be7a12d7af2e2645f31e.
- evidence_id: EPARENTS
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: TSV line 6
  accessed_at: '2026-11-08T15:45:07Z'
  support: supports
  summary: '[[6, "habitatmech:GOLD.8634ec53de\tHost-associated > Fish > Integumentary
    system > Skin > Fin\thabitatmech:GOLD.92e3c832eb\tantigravity\t2026-11-08\tReview
    https://github.com/CultureBotAI/HabitatMech/issues/2318 : Feces and earthworm
    casts are egested digestive waste material, not subtypes of the digestive tract
    or of the human, mammalian, or avian large intestine organ; a fish fin is a locomotory
    appendage, not a subtype of the whole fish skin organ. Exclude only exact guarded
    GOLD source-path contributions, preserving independent genera and all source observations.
    Exact target UBERON:0008897. Shared mapping endpoints #1398 remain separate."]]'
  snapshot_sha256: f004c15e7d206d673bdd9e6d051f6fce93c8a06ebe4db6026149d4d00c49cc9e
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261108T114933Z-fin-record/review.yaml
  locator: Every immutable Stage 4 baseline finding
  accessed_at: '2026-11-08T15:45:07Z'
  support: supports
  summary: Exact predecessor keys and findings reconciled; original inspected source
    scope preserved.
  snapshot_sha256: ffb7aa1e17e0fa65947b1e572feb9eb9cbc850e63b0068a1a7bb41fe31382280
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_fecal_0d8696a2_to_fin_review_repairs.py
  locator: Complete full-corpus counterfactual regression suite
  accessed_at: '2026-11-08T15:45:07Z'
  support: supports
  summary: 'Exactly seven records differ from the counterfactual baseline across Issues
    #2318 and #2319.'
  snapshot_sha256: db50d90f8a6296e1914051aa62fe928ab03d264f44cc8cbfb1c822f9f9ec650c
- evidence_id: EHIST_G1
  kind: record_content
  reference: history/other/gold_parent_exclusions/2026-11-08T153500Z-antigravity-231801.yaml
  locator: Complete curation session history event
  accessed_at: '2026-11-08T15:45:07Z'
  support: supports
  summary: 'Authorized curation event for Issue #2318 recorded and validated.'
  snapshot_sha256: 0238f5404c80e4c6e0f01acbaf496cb3a6a304632fe3c51122e348ea0e39c919
assessments:
- assessment_id: A1
  area: schema
  topic: Native validity and reproduction after bounded remediation
  outcome: supported
  summary: Individual schema, strict 24-target validation, 872 history records, 14
    inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 93 causal
    overlays, 674 term requests, curation floor, site parity, and counterfactual regression
    tests passed.
  target_ids:
  - UBERON:0008897
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EGOLD
  - EONT
  - EONTEDGE
  - EP2
  - ESEARCH
  - EPARENTS
  - EPREV
  - ETEST
  - EHIST_G1
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: supported
  summary: 'UBERON:0008897: fin; EXACT/SEEDED; parents ["UBERON:0000026"]. Removed
    the guarded GOLD whole-organ context-parent contribution habitatmech:GOLD.92e3c832eb
    (fish Skin) for source concept habitatmech:GOLD.8634ec53de (''Host-associated
    > Fish > Integumentary system > Skin > Fin'') via curation/gold_parent_exclusions.tsv
    (#2318), preserving broader ontology parent UBERON:0000026 (appendage). Identity
    (UBERON:0008897, ''fin''), native SEEDED/EXACT status, and source observations
    are preserved. No unresolved predecessor finding remains in this target scope.'
  target_ids:
  - UBERON:0008897
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EGOLD
  - EONT
  - EONTEDGE
  - EP2
  - ESEARCH
  - EPARENTS
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
  - UBERON:0008897
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EGOLD
  - EONT
  - EONTEDGE
  - EP2
  - ESEARCH
  - EPARENTS
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
  - UBERON:0008897
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EGOLD
  - EONT
  - EONTEDGE
  - EP2
  - ESEARCH
  - EPARENTS
  - EPREV
  - ETEST
  - EHIST_G1
- assessment_id: A5
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: Missing optional parameters/graphs are not evidence deficits. Full source
    decisions and executed routes reproduce SEEDED / EXACT; this read-only review
    does not mutate generated records.
  target_ids:
  - UBERON:0008897
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EGOLD
  - EONT
  - EONTEDGE
  - EP2
  - ESEARCH
  - EPARENTS
  - EPREV
  - ETEST
  - EHIST_G1
findings:
- finding_id: F1
  issue_key: fin-context-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Fin retains piscine Skin GOLD parent as a superclass
  description: Add an exclusion row in curation/gold_parent_exclusions.tsv for source
    identifier habitatmech:GOLD.e0bc7cc171 on GOLD path 'Host-associated > Fish >
    Integumentary system > Skin > Fin' (exact target UBERON:0008897) excluding parent_id
    habitatmech:GOLD.92e3c832eb (Skin), preserving ontology parent UBERON:0000026
    (appendage) and matching sibling feather (#2304).
  target_ids:
  - UBERON:0008897
  field_paths:
  - parent_habitats
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EGOLD
  - EONT
  - EONTEDGE
  - EP2
  - ESEARCH
  - EPARENTS
  - EPREV
  - ETEST
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
  - https://github.com/CultureBotAI/HabitatMech/issues/2318
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261108T114933Z-fin-record
    finding_id: F1
  disposition_reason: Excluded only the guarded GOLD whole-organ context-parent contribution
    habitatmech:GOLD.92e3c832eb (fish Skin) for source concept habitatmech:GOLD.8634ec53de
    in curation/gold_parent_exclusions.tsv (#2318), preserving broader ontology parent
    UBERON:0000026 (appendage).
actions: []
limitations:
- Only the stated primary evidence and current ontology/taxonomy authorities were
  independently inspected; original specimen-level support for every source-bin member
  is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism
  or characteristic presence. Parent observations are not inherited by children.
- Configured label correspondence skipped 2,088 no-adapter pairs; this is not whole-corpus
  identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in
  this pre-save observation.
- 'iModulonDB is not applicable: the target has no gene, regulator or expression-module
  assertion. No paid research or scientific-status promotion was performed.'
notes:
- Saved against working-tree repairs atop main commit 8e2744f4c33769669e5e9a66a4ae9e27a9642590;
  all earlier saved bundles in reviews/structured/ remain byte-identical.
- Reconciles predecessor bundle 20261108T114933Z-fin-record with exact issue_key and
  previous_occurrences lineage.
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261108T114933Z-fin-record
  relationship: Exact predecessor; every finding explicitly reconciled.
```
