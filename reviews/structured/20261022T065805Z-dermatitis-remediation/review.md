# Remediation review: dermatitis

- Review: 20261022T065805Z-dermatitis-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-22T06:40:00Z
- Finished UTC: 2026-10-22T06:58:05Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Removed the guarded GOLD context-parent contribution (#2255). Identity, native status, broader ontology parents, and source observations are preserved. No unresolved predecessor finding remains in this target scope.

## Scope And Provenance

Full current target assessment and explicit disposition of every baseline finding on data/habitats/host_associated/dermatitis.yaml after bounded Stage 5 remediation.

Selection: One of twelve repaired targets from the dental_plaque__8396e8ec-through-digestive_system__780e5b67 cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 2ec3d103f44a563f8cc4562f33e82d364039fa81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.25fd1f31a1 | data/habitats/host_associated/dermatitis.yaml | generated | mammalian dermatitis skin lesion |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.25fd1f31a1 | Completed 2026-10-22T01:41:53Z. No issues found. |
| validate-strict | passed | True | habitatmech:GOLD.25fd1f31a1 | Completed 2026-10-22T01:41:15Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | habitatmech:GOLD.25fd1f31a1 | Completed 2026-10-22T06:45:00Z. No issues found; 845 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | habitatmech:GOLD.25fd1f31a1 | Completed 2026-10-22T01:25:16Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | habitatmech:GOLD.25fd1f31a1 | Completed 2026-10-22T06:45:10Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | habitatmech:GOLD.25fd1f31a1 | Completed 2026-10-22T01:25:56Z. validated 33 causal-graph curation file(s) with 33 graph(s). |
| term-requests-check | passed | True | habitatmech:GOLD.25fd1f31a1 | Completed 2026-10-22T06:45:15Z. term-request table is current (625 terms). |
| validate-products | passed | True | habitatmech:GOLD.25fd1f31a1 | Completed 2026-10-22T01:28:18Z. OK_CANONICAL: 1174, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2063. All id&lt;-&gt;label pairs correspond. |
| Baseline full native QC in CI | passed | True | habitatmech:GOLD.25fd1f31a1 | Authoritative Build and test quality gate and label-correspondence succeeded on the exact working-tree base revision 2ec3d103f44a563f8cc4562f33e82d364039fa81; verified at 2026-10-22T06:22:00Z. https://github.com/CultureBotAI/HabitatMech/actions/runs/39686464212 |
| pytest counterfactual review repairs | passed | True | habitatmech:GOLD.25fd1f31a1 | Completed 2026-10-22T06:46:00Z. 2 passed; exact 12-record counterfactual diff verified. |
| curation-floor | passed | True | habitatmech:GOLD.25fd1f31a1 | Completed 2026-10-22T06:46:05Z. Floor satisfied across all 13 metrics. |
| render-check | passed | True | habitatmech:GOLD.25fd1f31a1 | Completed 2026-10-22T06:46:30Z. rendered 3209 habitat pages, 259 redirect stubs, 8 categories, 135 term requests; pages/ is in step with the corpus. |

## Scientific And Domain Assessments

### Native validity and reproduction after bounded remediation

schema: supported. Targets: habitatmech:GOLD.25fd1f31a1.

Individual schema, strict 24-target validation, 845 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 33 causal overlays, 625 term requests, curation floor, site parity, and counterfactual regression tests passed.

### Identity, definition, hierarchy and aliases

identity: supported. Targets: habitatmech:GOLD.25fd1f31a1.

habitatmech:GOLD.25fd1f31a1: mammalian dermatitis skin lesion; UNGROUNDED/REVIEWED; parents ["ENVO:2100003"]. Excluded only the false GOLD context-parent contribution habitatmech:GOLD.c896f9520f (#2255).

### Source counts and retained ranking

quantity: supported. Targets: habitatmech:GOLD.25fd1f31a1.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"source": "GOLD", "count": null, "unit": null}]. Zero counts are omitted; unrelated parent counts are not combined.

### Predecessor finding reconciliation

representation: supported. Targets: habitatmech:GOLD.25fd1f31a1.

Every predecessor finding preserves its stable issue_key and exact lineage. F1 is resolved under #2255; no open findings remain.

### Parameters, mechanisms and native status

completeness: supported. Targets: habitatmech:GOLD.25fd1f31a1.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only review does not mutate generated records.

## Findings

### F1: Whole mammalian skin is asserted as a superclass of mammalian dermatitis skin lesion

major / resolved / confirmed; issue key: dermatitis-context-parent.

Exclude only the guarded GOLD source-path parent contribution habitatmech:GOLD.c896f9520f (Skin in Host-associated &gt; Mammals &gt; Integumentary system &gt; Skin &gt; Dermatitis) from dermatitis.yaml while preserving the curated parent ENVO:2100003 (skin environment), UNGROUNDED/REVIEWED status, and GOLD source attestation (total_assertions: 0).

Disposition: Excluded only the guarded GOLD source-context contribution habitatmech:GOLD.c896f9520f in curation/gold_parent_exclusions.tsv (#2255). Independent valid parents, status, and all source observations remain intact.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/dermatitis.yaml; Entire YAML | supports | {"identifier": "habitatmech:GOLD.25fd1f31a1", "label": "mammalian dermatitis skin lesion", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED", "parent_habitats": ["ENVO:2100003"], "synonyms": [{"synonym_text": "dermatitic mammalian skin", "synonym_type": "EXACT_SYNONYM", "source": "HabitatMech curation"}], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6414", "source_label": "Dermatitis", "source_path": "Host-associated &gt; Mammals &gt; Integumentary system &gt; Skin &gt; Dermatitis"}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED."}, {"timestamp": "2026-10-17T00:00:00Z", "curator": "antigravity", "action": "CONFIRM_UNGROUNDED", "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. Defined mammalian dermatitis skin lesion under ENVO:2100003 'skin environment'; supported by mammalian and canine dermatitis skin microbiome studies (PMID 27512056). (source concept habitatmech:GOLD.25fd1f31a1)"}, {"timestamp": "2026-10-17T00:00:00Z", "curator": "antigravity", "action": "DEFINED", "changes": "Defined as 'mammalian dermatitis skin lesion' under ENVO:2100003 'skin environment'. Defined mammalian dermatitis skin lesion under ENVO:2100003 'skin environment'; supported by mammalian and canine dermatitis skin microbiome studies (PMID 27512056)."}, {"timestamp": "2026-10-17T00:00:00Z", "curator": "antigravity", "action": "SOURCE_SYNONYM_EXCLUDED", "changes": "Omitted automatic retention of displaced source label 'Dermatitis' when defining habitatmech:GOLD.25fd1f31a1 as 'mammalian dermatitis skin lesion'. Verbatim source attestations are preserved. Displaced GOLD source label 'Dermatitis' in path 'Host-associated &gt; Mammals &gt; Integumentary system &gt; Skin &gt; Dermatitis' is context-dependent, ambiguous, or names a host/disease/process rather than the defined habitat 'mammalian dermatitis skin lesion'; suppress automatic exact-synonym retention while preserving verbatim source provenance."}, {"timestamp": "2026-10-22T00:00:00Z", "curator": "antigravity", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.c896f9520f for habitatmech:GOLD.25fd1f31a1 (Host-associated &gt; Mammals &gt; Integumentary system &gt; Skin &gt; Dermatitis). Review https://github.com/CultureBotAI/HabitatMech/issues/2255 : Dental plaque is a tooth-surface biofilm deposit, not the entire mammalian oral cavity; post-mortem dentin is calcified tooth tissue, not an entire skeletonized remains assemblage; dentition is a tooth assemblage, not the whole oral cavity; dermal papilla and dermis are skin layers/structures and dermatitis and diabetic foot ulcer are cutaneous lesions/conditions, not subtypes of the whole skin organ; descending colon is a colonic segment, not the entire large intestine; diaphragm is a muscular partition, not the entire respiratory system. Exclude only exact guarded GOLD source-path contributions, preserving independent genera and all source observations. Exact target habitatmech:GOLD.25fd1f31a1. Shared mapping endpoints #1398 remain separate."}]} |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, not-applicable disease bins, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=habitatmech:GOLD.25fd1f31a1, grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["ENVO:2100003"]. |
| EGOLD | data/raw/gold_ecosystem_paths.tsv; TSV rows 2070 | supports | [{"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Mammals &gt; Integumentary system &gt; Skin &gt; Dermatitis", "depth": "5", "ecosystem": "Host-associated", "ecosystem_category": "Mammals", "ecosystem_subtype": "Skin", "ecosystem_type": "Integumentary system", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:6414", "leaf_label": "Dermatitis", "organism_count": "0", "specific_ecosystem": "Dermatitis", "study_count": "0", "total_assertions": "0"}, "row": 2070}] |
| EONT | data/raw/ontology_terms.tsv; TSV rows 10376 | supports | [{"data": {"definition": "An environment determined by an area or zone of skin tissue.", "deprecated": "", "directly_referenced": "TRUE", "label": "skin environment", "label_only": "FALSE", "ontology": "ENVO", "synonyms": "", "term_id": "ENVO:2100003"}, "row": 10376}] |
| EDEC | curation/decisions.tsv; TSV rows 330 | supports | [{"data": {"category": "", "curator": "antigravity", "date": "2026-10-17", "decision": "CONFIRM_UNGROUNDED", "grounding_status": "", "identifier": "habitatmech:GOLD.25fd1f31a1", "notes": "Defined mammalian dermatitis skin lesion under ENVO:2100003 'skin environment'; supported by mammalian and canine dermatitis skin microbiome studies (PMID 27512056).", "object_id": "", "object_label": "", "relation": "", "review_depth": "ITEM"}, "row": 330}] |
| ETR | curation/term_requests.tsv; TSV rows 571 | supports | [{"data": {"curator": "antigravity", "date": "2026-10-17", "definition": "A skin environment on a mammalian host affected by epidermal and dermal inflammation (dermatitis), often exhibiting barrier disruption and Staphylococcus or Malassezia overgrowth.", "exact_synonym": "dermatitic mammalian skin", "identifier": "habitatmech:GOLD.25fd1f31a1", "notes": "Defined mammalian dermatitis skin lesion under ENVO:2100003 'skin environment'; supported by mammalian and canine dermatitis skin microbiome studies (PMID 27512056).", "parent_class": "ENVO:2100003", "parent_label": "skin environment", "parent_mode": "ADD", "requested_label": "mammalian dermatitis skin lesion"}, "row": 571}] |
| EP1 | data/habitats/other/skin_environment.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": "An environment determined by an area or zone of skin tissue.", "grounding_status": "EXACT", "identifier": "ENVO:2100003", "label": "skin environment", "mapping_status": "REVIEWED", "parent_habitats": ["ENVO:2100004"], "source_attestations": [{"notes": "Physicochemical parameter bands from kg-microbe's environment table.", "source": "ENVIRONMENTS_TABLE", "source_id": "host_animal_endotherm_surface", "source_label": "host_animal_endotherm_surface"}, {"assertion_count": 372, "assertion_unit": "TAXON", "source": "MADIN", "source_id": "ENVO:2100003", "source_label": "skin environment"}, {"assertion_count": 39, "assertion_unit": "TAXON", "evidence_channels": "environmental_samples", "score": 4.0, "source": "PREGO", "source_id": "ENVO:2100003", "source_label": "skin environment"}]} |
| EP2 | data/habitats/host_associated/skin__120842b3.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": null, "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.c896f9520f", "label": "Skin", "mapping_status": "SEEDED", "parent_habitats": ["BTO:0001253", "habitatmech:GOLD.56e0776270"], "source_attestations": [{"assertion_count": 121, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:narrowMatch", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:6383", "source_label": "Skin", "source_path": "Host-associated &gt; Mammals &gt; Integumentary system &gt; Skin"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'dermatitis&#124;habitatmech:GOLD.25fd1f31a1' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal verified no prior target review bundle exists for this record; curation and history tables were inspected for all matching rows. |
| EPREV | reviews/structured/20261022T014517Z-dermatitis-record/review.yaml; Every immutable Stage 4 baseline finding | supports | Exact predecessor keys and findings reconciled; original inspected source scope preserved. |
| ETEST | tests/test_dental_to_diaphragm_review_repairs.py; Complete full-corpus counterfactual regression suite | supports | Exactly twelve records differ from the counterfactual baseline: eleven guarded GOLD context-parent removals (#2255) and one bare host-clade exact-alias exclusion (#2256). |
| EPARENTS | curation/gold_parent_exclusions.tsv; TSV line 6 | supports | [[6, "habitatmech:GOLD.25fd1f31a1\tHost-associated &gt; Mammals &gt; Integumentary system &gt; Skin &gt; Dermatitis\thabitatmech:GOLD.c896f9520f\tantigravity\t2026-10-22\tReview https://github.com/CultureBotAI/HabitatMech/issues/2255 : Dental plaque is a tooth-surface biofilm deposit, not the entire mammalian oral cavity; post-mortem dentin is calcified tooth tissue, not an entire skeletonized remains assemblage; dentition is a tooth assemblage, not the whole oral cavity; dermal papilla and dermis are skin layers/structures and dermatitis and diabetic foot ulcer are cutaneous lesions/conditions, not subtypes of the whole skin organ; descending colon is a colonic segment, not the entire large intestine; diaphragm is a muscular partition, not the entire respiratory system. Exclude only exact guarded GOLD source-path contributions, preserving independent genera and all source observations. Exact target habitatmech:GOLD.25fd1f31a1. Shared mapping endpoints #1398 remain separate."]] |
| EHIST | history/other/gold_parent_exclusions/2026-10-22T063700Z-antigravity-225501.yaml; Complete curation session history event | supports | Authorized curation event for Issue #2255 recorded and validated. |

## Limits And Additional Notes

- Only the stated primary evidence and current ontology/taxonomy authorities were independently inspected; original specimen-level support for every source-bin member is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism or characteristic presence. Parent observations are not inherited by children.
- Configured label correspondence skipped 2,063 no-adapter pairs; this is not whole-corpus identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in this pre-save observation. Baseline full QC is separately identified as CI evidence.
- iModulonDB is not applicable: the target has no gene, regulator or expression-module assertion. No paid research or scientific-status promotion was performed.
- Saved against working-tree repairs atop main commit 2ec3d103f44a563f8cc4562f33e82d364039fa81; all earlier saved bundles in reviews/structured/ remain byte-identical.
- Reconciles predecessor bundle 20261022T014517Z-dermatitis-record with exact issue_key and previous_occurrences lineage.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T065805Z-dermatitis-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: dermatitis'
started_at: '2026-10-22T06:40:00Z'
finished_at: '2026-10-22T06:58:05Z'
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
summary: Removed the guarded GOLD context-parent contribution (#2255). Identity, native
  status, broader ontology parents, and source observations are preserved. No unresolved
  predecessor finding remains in this target scope.
source:
  git_revision: 2ec3d103f44a563f8cc4562f33e82d364039fa81
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 4544b5d2c11fbbb3a46cd8a65f7e664363df78c1000c590aab533219f9eec59b
    role: context
  - path: .claude/skills/review-yaml-category/SKILL.md
    sha256: 4a43388a0a8863b06c66cef795db0b9cc12c1507af727f2f672fd97f18309e0e
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: d429c8bb74f521df9a77a90b216a44fc6959ee28efb1fa17a93582536caa8bce
    role: context
  - path: CLAUDE.md
    sha256: bcd9e1c631a4ec7313b7662e2b17fcd9504eed19385577c728440ca78fc55efb
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
    sha256: 704cd3ef46ced8aff6bd8b7f2ce15edfa7c75f3612ce3dc270dd365fd48d1c9c
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: fbcc0deac2c94eadaa3629647605a09deed534460300386bb097cd013ac90c96
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 391fd3abe12d609d5d15fc8cff56d87c0278a4056c1231a251253227e9da1cb9
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: c1207270bb0ae2031e42de6cb8220b20f98886f65e40d48793bfd7e9d757d83a
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: e020f95fc67252b97da96abe39c7b1228ec161055cd0221499e2d12a33cf9aa0
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: ee559f7b45b4af2d72a078c45d1a3b676785d34305f286e9738f95771dbaccfd
    role: context
  - path: data/habitats/RETIRED.tsv
    sha256: 8215d18f466445cc7aa6348601f0a76380c8fc41ecef537ec24b60af35698ff0
    role: context
  - path: data/habitats/host_associated/dermatitis.yaml
    sha256: d1e0d7b857e2fa4c1a892cb36b7b3b687ef462696565f7af229d0ed74217df45
    role: target
  - path: data/habitats/host_associated/skin__120842b3.yaml
    sha256: d289ced090fe833fd08c77a79df5c013044dfada3603d6eb839c8da7cb9216ff
    role: context
  - path: data/habitats/other/skin_environment.yaml
    sha256: 84954c26e7b843c6a8b103f9db89d12b28eac1e8360f6ad4d28e65d026bb34ac
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
  - path: history/other/definition_source_label_exclusions/2026-10-22T063710Z-antigravity-225601.yaml
    sha256: 473b98692d4e7067042014a59dc192e330765b61adde491247e5f71547f3cfb3
    role: context
  - path: history/other/gold_parent_exclusions/2026-10-22T063700Z-antigravity-225501.yaml
    sha256: 237789a50d728b2c30e35190ba4ef7d30047fc212a21e67885f1e3e037343045
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reviews/structured/20261022T014517Z-dermatitis-record/review.yaml
    sha256: 6855d0accb024b1876da07f7bf43a57f8e6db97bf59208f3fc75ec1acd112cf5
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
  - path: tests/test_dental_to_diaphragm_review_repairs.py
    sha256: 63b86fb79148e60c7bdde0ac5c861fc7bc8a800d99a9608f1105aad2ad919451
    role: context
targets:
- target_id: habitatmech:GOLD.25fd1f31a1
  path: data/habitats/host_associated/dermatitis.yaml
  label: mammalian dermatitis skin lesion
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
    finding on data/habitats/host_associated/dermatitis.yaml after bounded Stage 5
    remediation.
  selection: One of twelve repaired targets from the dental_plaque__8396e8ec-through-digestive_system__780e5b67
    cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.25fd1f31a1
  exclusions:
  - target: Other habitat records and SSSOM/KGX products
    reason: Direct parents inform hierarchy interpretation but are not additional
      completed reviews; exports are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: .venv/bin/python -m linkml.validator.cli -s src/habitatmech/schema/habitatmech.yaml
    --target-class HabitatRecord data/habitats/host_associated/dermatitis.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.25fd1f31a1
  summary: Completed 2026-10-22T01:41:53Z. No issues found.
  scope_note: Individual schema; strict command covers the 24 named cohort targets;
    other documented gates have full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/habitats/host_associated/dental_plaque__8396e8ec.yaml
    data/habitats/host_associated/dental_plaque__df2cbc31.yaml data/habitats/host_associated/dental_pulp.yaml
    data/habitats/host_associated/dentin.yaml data/habitats/host_associated/dentin__be69daef.yaml
    data/habitats/host_associated/dentition.yaml data/habitats/host_associated/dermal_papilla.yaml
    data/habitats/host_associated/dermatitis.yaml data/habitats/host_associated/dermatitis__d991f62d.yaml
    data/habitats/host_associated/dermis.yaml data/habitats/host_associated/dermoid.yaml
    data/habitats/host_associated/descending_colon.yaml data/habitats/host_associated/diabetic_foot_ulcer_dfu.yaml
    data/habitats/host_associated/diabetic_foot_ulcer_dfu__cf26bdc0.yaml data/habitats/host_associated/diaphragm.yaml
    data/habitats/host_associated/diaphragm__3c058609.yaml data/habitats/host_associated/diaphragm__fbd202d9.yaml
    data/habitats/host_associated/diatoms.yaml data/habitats/host_associated/diffuse_large_b_cell_lymphoma.yaml
    data/habitats/host_associated/digestive_system.yaml data/habitats/host_associated/digestive_system__2589c8ce.yaml
    data/habitats/host_associated/digestive_system__46d403bb.yaml data/habitats/host_associated/digestive_system__4f205b4d.yaml
    data/habitats/host_associated/digestive_system__780e5b67.yaml --out /tmp/stage4_24_strict.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.25fd1f31a1
  summary: 'Completed 2026-10-22T01:41:15Z. Validated 24 files; files with ERROR:
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
  - habitatmech:GOLD.25fd1f31a1
  summary: Completed 2026-10-22T06:45:00Z. No issues found; 845 history record(s)
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
  - habitatmech:GOLD.25fd1f31a1
  summary: 'Completed 2026-10-22T01:25:16Z. provenance current: 14 committed inventories,
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
  - habitatmech:GOLD.25fd1f31a1
  summary: 'Completed 2026-10-22T06:45:10Z. expected 3209 records, found 3209 on disk;
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
  - habitatmech:GOLD.25fd1f31a1
  summary: Completed 2026-10-22T01:25:56Z. validated 33 causal-graph curation file(s)
    with 33 graph(s).
  scope_note: Full-corpus causal-graph overlay validation.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: .venv/bin/python scripts/build_term_requests.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.25fd1f31a1
  summary: Completed 2026-10-22T06:45:15Z. term-request table is current (625 terms).
  scope_note: Full-corpus term-request table currency check.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.25fd1f31a1
  summary: 'Completed 2026-10-22T01:28:18Z. OK_CANONICAL: 1174, OK_SYNONYM: 1, OK_EXCEPTION:
    5, SKIPPED_NO_ADAPTER: 2063. All id<->label pairs correspond.'
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
- check_id: CCI
  name: Baseline full native QC in CI
  status: passed
  required: true
  command: gh run view 39686464212 --json status,conclusion,headSha,url
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.25fd1f31a1
  summary: Authoritative Build and test quality gate and label-correspondence succeeded
    on the exact working-tree base revision 2ec3d103f44a563f8cc4562f33e82d364039fa81;
    verified at 2026-10-22T06:22:00Z. https://github.com/CultureBotAI/HabitatMech/actions/runs/39686464212
  scope_note: Verified remote baseline execution on exact git revision.
- check_id: C9
  name: pytest counterfactual review repairs
  status: passed
  required: true
  command: .venv/bin/python -m pytest tests/test_dental_to_diaphragm_review_repairs.py
    -q --no-cov
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.25fd1f31a1
  summary: Completed 2026-10-22T06:46:00Z. 2 passed; exact 12-record counterfactual
    diff verified.
  scope_note: 'Full-corpus counterfactual regression test for Issues #2255 and #2256.'
- check_id: C10
  name: curation-floor
  status: passed
  required: true
  command: .venv/bin/python scripts/check_curation_floor.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.25fd1f31a1
  summary: Completed 2026-10-22T06:46:05Z. Floor satisfied across all 13 metrics.
  scope_note: Full-corpus curation floor ratchets.
- check_id: C11
  name: render-check
  status: passed
  required: true
  command: .venv/bin/python scripts/render_pages.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.25fd1f31a1
  summary: Completed 2026-10-22T06:46:30Z. rendered 3209 habitat pages, 259 redirect
    stubs, 8 categories, 135 term requests; pages/ is in step with the corpus.
  scope_note: Full-corpus static site parity check.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/dermatitis.yaml
  locator: Entire YAML
  accessed_at: '2026-10-22T06:58:05Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.25fd1f31a1", "label": "mammalian dermatitis
    skin lesion", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED",
    "parent_habitats": ["ENVO:2100003"], "synonyms": [{"synonym_text": "dermatitic
    mammalian skin", "synonym_type": "EXACT_SYNONYM", "source": "HabitatMech curation"}],
    "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6414",
    "source_label": "Dermatitis", "source_path": "Host-associated > Mammals > Integumentary
    system > Skin > Dermatitis"}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z",
    "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded
    from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED."}, {"timestamp":
    "2026-10-17T00:00:00Z", "curator": "antigravity", "action": "CONFIRM_UNGROUNDED",
    "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. Defined
    mammalian dermatitis skin lesion under ENVO:2100003 ''skin environment''; supported
    by mammalian and canine dermatitis skin microbiome studies (PMID 27512056). (source
    concept habitatmech:GOLD.25fd1f31a1)"}, {"timestamp": "2026-10-17T00:00:00Z",
    "curator": "antigravity", "action": "DEFINED", "changes": "Defined as ''mammalian
    dermatitis skin lesion'' under ENVO:2100003 ''skin environment''. Defined mammalian
    dermatitis skin lesion under ENVO:2100003 ''skin environment''; supported by mammalian
    and canine dermatitis skin microbiome studies (PMID 27512056)."}, {"timestamp":
    "2026-10-17T00:00:00Z", "curator": "antigravity", "action": "SOURCE_SYNONYM_EXCLUDED",
    "changes": "Omitted automatic retention of displaced source label ''Dermatitis''
    when defining habitatmech:GOLD.25fd1f31a1 as ''mammalian dermatitis skin lesion''.
    Verbatim source attestations are preserved. Displaced GOLD source label ''Dermatitis''
    in path ''Host-associated > Mammals > Integumentary system > Skin > Dermatitis''
    is context-dependent, ambiguous, or names a host/disease/process rather than the
    defined habitat ''mammalian dermatitis skin lesion''; suppress automatic exact-synonym
    retention while preserving verbatim source provenance."}, {"timestamp": "2026-10-22T00:00:00Z",
    "curator": "antigravity", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded
    GOLD source-path parent contribution habitatmech:GOLD.c896f9520f for habitatmech:GOLD.25fd1f31a1
    (Host-associated > Mammals > Integumentary system > Skin > Dermatitis). Review
    https://github.com/CultureBotAI/HabitatMech/issues/2255 : Dental plaque is a tooth-surface
    biofilm deposit, not the entire mammalian oral cavity; post-mortem dentin is calcified
    tooth tissue, not an entire skeletonized remains assemblage; dentition is a tooth
    assemblage, not the whole oral cavity; dermal papilla and dermis are skin layers/structures
    and dermatitis and diabetic foot ulcer are cutaneous lesions/conditions, not subtypes
    of the whole skin organ; descending colon is a colonic segment, not the entire
    large intestine; diaphragm is a muscular partition, not the entire respiratory
    system. Exclude only exact guarded GOLD source-path contributions, preserving
    independent genera and all source observations. Exact target habitatmech:GOLD.25fd1f31a1.
    Shared mapping endpoints #1398 remain separate."}]}'
  snapshot_sha256: d1e0d7b857e2fa4c1a892cb36b7b3b687ef462696565f7af229d0ed74217df45
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, not-applicable disease bins, and
    source ownership
  accessed_at: '2026-10-22T06:58:05Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon terms cannot substitute
    for associated environments; parent_habitats must be strictly broader across all
    contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-10-22T06:58:05Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-10-22T06:58:05Z'
  support: supports
  summary: Seed generator produces identifier=habitatmech:GOLD.25fd1f31a1, grounding_status=UNGROUNDED,
    mapping_status=REVIEWED, parent_habitats=["ENVO:2100003"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EGOLD
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV rows 2070
  accessed_at: '2026-10-22T06:58:05Z'
  support: supports
  summary: '[{"data": {"biosample_count": "0", "canonical_path": "Host-associated
    > Mammals > Integumentary system > Skin > Dermatitis", "depth": "5", "ecosystem":
    "Host-associated", "ecosystem_category": "Mammals", "ecosystem_subtype": "Skin",
    "ecosystem_type": "Integumentary system", "gold_node_count": "1", "gold_node_ids":
    "gold.ecosystem:6414", "leaf_label": "Dermatitis", "organism_count": "0", "specific_ecosystem":
    "Dermatitis", "study_count": "0", "total_assertions": "0"}, "row": 2070}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 10376
  accessed_at: '2026-10-22T06:58:05Z'
  support: supports
  summary: '[{"data": {"definition": "An environment determined by an area or zone
    of skin tissue.", "deprecated": "", "directly_referenced": "TRUE", "label": "skin
    environment", "label_only": "FALSE", "ontology": "ENVO", "synonyms": "", "term_id":
    "ENVO:2100003"}, "row": 10376}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EDEC
  kind: database
  reference: curation/decisions.tsv
  locator: TSV rows 330
  accessed_at: '2026-10-22T06:58:05Z'
  support: supports
  summary: '[{"data": {"category": "", "curator": "antigravity", "date": "2026-10-17",
    "decision": "CONFIRM_UNGROUNDED", "grounding_status": "", "identifier": "habitatmech:GOLD.25fd1f31a1",
    "notes": "Defined mammalian dermatitis skin lesion under ENVO:2100003 ''skin environment'';
    supported by mammalian and canine dermatitis skin microbiome studies (PMID 27512056).",
    "object_id": "", "object_label": "", "relation": "", "review_depth": "ITEM"},
    "row": 330}]'
  snapshot_sha256: 704cd3ef46ced8aff6bd8b7f2ce15edfa7c75f3612ce3dc270dd365fd48d1c9c
- evidence_id: ETR
  kind: database
  reference: curation/term_requests.tsv
  locator: TSV rows 571
  accessed_at: '2026-10-22T06:58:05Z'
  support: supports
  summary: '[{"data": {"curator": "antigravity", "date": "2026-10-17", "definition":
    "A skin environment on a mammalian host affected by epidermal and dermal inflammation
    (dermatitis), often exhibiting barrier disruption and Staphylococcus or Malassezia
    overgrowth.", "exact_synonym": "dermatitic mammalian skin", "identifier": "habitatmech:GOLD.25fd1f31a1",
    "notes": "Defined mammalian dermatitis skin lesion under ENVO:2100003 ''skin environment'';
    supported by mammalian and canine dermatitis skin microbiome studies (PMID 27512056).",
    "parent_class": "ENVO:2100003", "parent_label": "skin environment", "parent_mode":
    "ADD", "requested_label": "mammalian dermatitis skin lesion"}, "row": 571}]'
  snapshot_sha256: e020f95fc67252b97da96abe39c7b1228ec161055cd0221499e2d12a33cf9aa0
- evidence_id: EP1
  kind: record_content
  reference: data/habitats/other/skin_environment.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-10-22T06:58:05Z'
  support: supports
  summary: '{"definition": "An environment determined by an area or zone of skin tissue.",
    "grounding_status": "EXACT", "identifier": "ENVO:2100003", "label": "skin environment",
    "mapping_status": "REVIEWED", "parent_habitats": ["ENVO:2100004"], "source_attestations":
    [{"notes": "Physicochemical parameter bands from kg-microbe''s environment table.",
    "source": "ENVIRONMENTS_TABLE", "source_id": "host_animal_endotherm_surface",
    "source_label": "host_animal_endotherm_surface"}, {"assertion_count": 372, "assertion_unit":
    "TAXON", "source": "MADIN", "source_id": "ENVO:2100003", "source_label": "skin
    environment"}, {"assertion_count": 39, "assertion_unit": "TAXON", "evidence_channels":
    "environmental_samples", "score": 4.0, "source": "PREGO", "source_id": "ENVO:2100003",
    "source_label": "skin environment"}]}'
  snapshot_sha256: 84954c26e7b843c6a8b103f9db89d12b28eac1e8360f6ad4d28e65d026bb34ac
- evidence_id: EP2
  kind: record_content
  reference: data/habitats/host_associated/skin__120842b3.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-10-22T06:58:05Z'
  support: supports
  summary: '{"definition": null, "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.c896f9520f",
    "label": "Skin", "mapping_status": "SEEDED", "parent_habitats": ["BTO:0001253",
    "habitatmech:GOLD.56e0776270"], "source_attestations": [{"assertion_count": 121,
    "assertion_unit": "ORGANISM", "mapping_predicate": "skos:narrowMatch", "notes":
    "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.",
    "source": "GOLD", "source_id": "gold.ecosystem:6383", "source_label": "Skin",
    "source_path": "Host-associated > Mammals > Integumentary system > Skin"}]}'
  snapshot_sha256: d289ced090fe833fd08c77a79df5c013044dfada3603d6eb839c8da7cb9216ff
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'dermatitis|habitatmech:GOLD.25fd1f31a1' reviews/structured/*/review.yaml
    curation/ history/
  accessed_at: '2026-10-22T06:58:05Z'
  support: context_only
  summary: Structured-review traversal verified no prior target review bundle exists
    for this record; curation and history tables were inspected for all matching rows.
  search_scope: curation, history, data/raw, and reviews/structured/*/review.yaml
    traversal at commit 56904acf1cf24914a262495568ecd63a67f5d9c7.
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261022T014517Z-dermatitis-record/review.yaml
  locator: Every immutable Stage 4 baseline finding
  accessed_at: '2026-10-22T06:58:05Z'
  support: supports
  summary: Exact predecessor keys and findings reconciled; original inspected source
    scope preserved.
  snapshot_sha256: 6855d0accb024b1876da07f7bf43a57f8e6db97bf59208f3fc75ec1acd112cf5
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_dental_to_diaphragm_review_repairs.py
  locator: Complete full-corpus counterfactual regression suite
  accessed_at: '2026-10-22T06:58:05Z'
  support: supports
  summary: 'Exactly twelve records differ from the counterfactual baseline: eleven
    guarded GOLD context-parent removals (#2255) and one bare host-clade exact-alias
    exclusion (#2256).'
  snapshot_sha256: 63b86fb79148e60c7bdde0ac5c861fc7bc8a800d99a9608f1105aad2ad919451
- evidence_id: EPARENTS
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: TSV line 6
  accessed_at: '2026-10-22T06:58:05Z'
  support: supports
  summary: '[[6, "habitatmech:GOLD.25fd1f31a1\tHost-associated > Mammals > Integumentary
    system > Skin > Dermatitis\thabitatmech:GOLD.c896f9520f\tantigravity\t2026-10-22\tReview
    https://github.com/CultureBotAI/HabitatMech/issues/2255 : Dental plaque is a tooth-surface
    biofilm deposit, not the entire mammalian oral cavity; post-mortem dentin is calcified
    tooth tissue, not an entire skeletonized remains assemblage; dentition is a tooth
    assemblage, not the whole oral cavity; dermal papilla and dermis are skin layers/structures
    and dermatitis and diabetic foot ulcer are cutaneous lesions/conditions, not subtypes
    of the whole skin organ; descending colon is a colonic segment, not the entire
    large intestine; diaphragm is a muscular partition, not the entire respiratory
    system. Exclude only exact guarded GOLD source-path contributions, preserving
    independent genera and all source observations. Exact target habitatmech:GOLD.25fd1f31a1.
    Shared mapping endpoints #1398 remain separate."]]'
  snapshot_sha256: 391fd3abe12d609d5d15fc8cff56d87c0278a4056c1231a251253227e9da1cb9
- evidence_id: EHIST
  kind: record_content
  reference: history/other/gold_parent_exclusions/2026-10-22T063700Z-antigravity-225501.yaml
  locator: Complete curation session history event
  accessed_at: '2026-10-22T06:58:05Z'
  support: supports
  summary: 'Authorized curation event for Issue #2255 recorded and validated.'
  snapshot_sha256: 237789a50d728b2c30e35190ba4ef7d30047fc212a21e67885f1e3e037343045
assessments:
- assessment_id: A1
  area: schema
  topic: Native validity and reproduction after bounded remediation
  outcome: supported
  summary: Individual schema, strict 24-target validation, 845 history records, 14
    inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 33 causal
    overlays, 625 term requests, curation floor, site parity, and counterfactual regression
    tests passed.
  target_ids:
  - habitatmech:GOLD.25fd1f31a1
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EDEC
  - ETR
  - EP1
  - EP2
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: supported
  summary: 'habitatmech:GOLD.25fd1f31a1: mammalian dermatitis skin lesion; UNGROUNDED/REVIEWED;
    parents ["ENVO:2100003"]. Excluded only the false GOLD context-parent contribution
    habitatmech:GOLD.c896f9520f (#2255).'
  target_ids:
  - habitatmech:GOLD.25fd1f31a1
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EDEC
  - ETR
  - EP1
  - EP2
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks,
    and pools: [{"source": "GOLD", "count": null, "unit": null}]. Zero counts are
    omitted; unrelated parent counts are not combined.'
  target_ids:
  - habitatmech:GOLD.25fd1f31a1
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EDEC
  - ETR
  - EP1
  - EP2
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST
- assessment_id: A4
  area: representation
  topic: Predecessor finding reconciliation
  outcome: supported
  summary: 'Every predecessor finding preserves its stable issue_key and exact lineage.
    F1 is resolved under #2255; no open findings remain.'
  target_ids:
  - habitatmech:GOLD.25fd1f31a1
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EDEC
  - ETR
  - EP1
  - EP2
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST
- assessment_id: A5
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: Missing optional parameters/graphs are not evidence deficits. Full source
    decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only
    review does not mutate generated records.
  target_ids:
  - habitatmech:GOLD.25fd1f31a1
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EDEC
  - ETR
  - EP1
  - EP2
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST
findings:
- finding_id: F1
  issue_key: dermatitis-context-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Whole mammalian skin is asserted as a superclass of mammalian dermatitis
    skin lesion
  description: 'Exclude only the guarded GOLD source-path parent contribution habitatmech:GOLD.c896f9520f
    (Skin in Host-associated > Mammals > Integumentary system > Skin > Dermatitis)
    from dermatitis.yaml while preserving the curated parent ENVO:2100003 (skin environment),
    UNGROUNDED/REVIEWED status, and GOLD source attestation (total_assertions: 0).'
  target_ids:
  - habitatmech:GOLD.25fd1f31a1
  field_paths:
  - parent_habitats
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EDEC
  - ETR
  - EP1
  - EP2
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or representation claim; deterministic
    validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2255
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261022T014517Z-dermatitis-record
    finding_id: F1
  disposition_reason: Excluded only the guarded GOLD source-context contribution habitatmech:GOLD.c896f9520f
    in curation/gold_parent_exclusions.tsv (#2255). Independent valid parents, status,
    and all source observations remain intact.
actions: []
limitations:
- Only the stated primary evidence and current ontology/taxonomy authorities were
  independently inspected; original specimen-level support for every source-bin member
  is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism
  or characteristic presence. Parent observations are not inherited by children.
- Configured label correspondence skipped 2,063 no-adapter pairs; this is not whole-corpus
  identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in
  this pre-save observation. Baseline full QC is separately identified as CI evidence.
- 'iModulonDB is not applicable: the target has no gene, regulator or expression-module
  assertion. No paid research or scientific-status promotion was performed.'
notes:
- Saved against working-tree repairs atop main commit 2ec3d103f44a563f8cc4562f33e82d364039fa81;
  all earlier saved bundles in reviews/structured/ remain byte-identical.
- Reconciles predecessor bundle 20261022T014517Z-dermatitis-record with exact issue_key
  and previous_occurrences lineage.
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261022T014517Z-dermatitis-record
  relationship: Exact predecessor; every finding explicitly reconciled.
```
