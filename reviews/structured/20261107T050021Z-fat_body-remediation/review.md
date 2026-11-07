# Remediation review: fat_body

- Review: 20261107T050021Z-fat_body-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-07T04:55:00Z
- Finished UTC: 2026-11-07T05:00:21Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Removed the guarded GOLD whole-host context-parent contribution habitatmech:GOLD.dba2a83b95 (insect-associated environment) for source concept habitatmech:GOLD.e63b1e075e via curation/gold_parent_exclusions.tsv (#2304), preserving broader ontology parent BTO:0001487 (adipose tissue). Identity (BTO:0000442, 'fat body'), native SEEDED/EXACT status, and source observations are preserved. No unresolved predecessor finding remains in this target scope.

## Scope And Provenance

Full current target assessment and explicit disposition of every baseline finding on data/habitats/host_associated/fat_body.yaml after bounded Cycle 6 Stage 5 remediation.

Selection: One of twenty-two repaired targets from the excretory_system__22ee753c-through-fecal cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 30fbe25f4c539ad6266dae7680d21e451caf6e40.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0000442 | data/habitats/host_associated/fat_body.yaml | generated | fat body |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0000442 | Completed 2026-11-07T04:58:12Z. No issues found. |
| validate-strict | passed | True | BTO:0000442 | Completed 2026-11-07T04:58:18Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | BTO:0000442 | Completed 2026-11-07T04:59:00Z. No issues found; 868 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | BTO:0000442 | Completed 2026-11-07T04:59:05Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | BTO:0000442 | Completed 2026-11-07T04:59:10Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | BTO:0000442 | Completed 2026-11-07T04:59:12Z. validated 83 causal-graph curation file(s) with 83 graph(s). |
| term-requests-check | passed | True | BTO:0000442 | Completed 2026-11-07T04:59:15Z. term-request table is current (671 terms). |
| validate-products | passed | True | BTO:0000442 | Completed 2026-11-07T04:59:20Z. OK_CANONICAL: 1203, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2084. All id&lt;-&gt;label pairs correspond. |
| pytest counterfactual review repairs | passed | True | BTO:0000442 | Completed 2026-11-07T04:59:30Z. 2 passed; exact 22-record counterfactual diff verified. |
| curation-floor | passed | True | BTO:0000442 | Completed 2026-11-07T04:59:35Z. Floor satisfied across all 13 metrics. |
| render-check | passed | True | BTO:0000442 | Completed 2026-11-07T04:59:50Z. rendered 3209 habitat pages, 750 redirect stubs, 8 categories, 696 term requests; pages/ is in step with the corpus. |

## Scientific And Domain Assessments

### Native validity and reproduction after bounded remediation

schema: supported. Targets: BTO:0000442.

Individual schema, strict 24-target validation, 868 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 83 causal overlays, 671 term requests, curation floor, site parity, and counterfactual regression tests passed.

### Identity, definition, hierarchy and aliases

identity: supported. Targets: BTO:0000442.

BTO:0000442: fat body; EXACT/SEEDED; parents ["BTO:0001487"]. Removed the guarded GOLD whole-host context-parent contribution habitatmech:GOLD.dba2a83b95 (insect-associated environment) for source concept habitatmech:GOLD.e63b1e075e via curation/gold_parent_exclusions.tsv (#2304), preserving broader ontology parent BTO:0001487 (adipose tissue). Identity (BTO:0000442, 'fat body'), native SEEDED/EXACT status, and source observations are preserved. No unresolved predecessor finding remains in this target scope.

### Source counts and retained ranking

quantity: supported. Targets: BTO:0000442.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"source": "GOLD", "count": 2, "unit": "ORGANISM"}]. Zero counts are omitted; unrelated parent counts are not combined.

### Predecessor finding reconciliation

representation: supported. Targets: BTO:0000442.

Every predecessor finding preserves its stable issue_key and exact lineage. All predecessor findings in this target scope are resolved.

### Parameters, mechanisms and native status

completeness: supported. Targets: BTO:0000442.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce SEEDED / EXACT; this read-only review does not mutate generated records.

## Findings

### F1: Fat body retains whole-host insect-associated environment GOLD parent as a superclass

major / resolved / confirmed; issue key: fat-body-context-parent.

Add an exclusion row in curation/gold_parent_exclusions.tsv for source identifier habitatmech:GOLD.e63b1e075e on GOLD path 'Host-associated &gt; Arthropoda: Insects &gt; Fat body' (exact target BTO:0000442) excluding parent_id habitatmech:GOLD.dba2a83b95 (insect-associated environment), preserving ontology parent BTO:0001487 (adipose tissue).

Disposition: Excluded only the guarded GOLD whole-host context-parent contribution habitatmech:GOLD.dba2a83b95 (insect-associated environment) for source concept habitatmech:GOLD.e63b1e075e in curation/gold_parent_exclusions.tsv (#2304), preserving broader ontology parent BTO:0001487 (adipose tissue).

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/fat_body.yaml; Entire YAML | supports | {"identifier": "BTO:0000442", "label": "fat body", "grounding_status": "EXACT", "mapping_status": "SEEDED", "parent_habitats": ["BTO:0001487"], "synonyms": [], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:7093", "source_label": "Fat body", "source_path": "Host-associated &gt; Arthropoda: Insects &gt; Fat body", "mapping_predicate": "skos:exactMatch", "assertion_count": 2, "assertion_unit": "ORGANISM", "notes": "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: EXACT."}, {"timestamp": "2026-11-06T00:00:00Z", "curator": "antigravity", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.dba2a83b95 for habitatmech:GOLD.e63b1e075e (Host-associated &gt; Arthropoda: Insects &gt; Fat body). Review https://github.com/CultureBotAI/HabitatMech/issues/2304 : Crustacean and annelid excretory system are organ systems, not subtypes of the whole crustacean- or annelid-associated host environment; external genitalia is an anatomical reproductive organ structure, not a subtype of the entire mammalian or human reproductive system; external soft tissue zone is a soft-tissue anatomical region, not a subtype of the mammalian Multiple systems GOLD classification bucket; mammalian, piscine, and human eye are sense organs and ciliary body and vitreous chamber are intraocular structures/compartments, not subtypes of the entire visual system; human and mammalian fallopian tube are oviductal reproductive organs, not subtypes of the entire reproductive system; mammalian and human fascia are connective tissue sheets, not subtypes of the host-scoped connective tissue assemblage; insect fat body is an adipose organ/tissue, not a subtype of the whole insect-associated environment; feather is an avian epidermal appendage, not a subtype of the whole avian skin organ. Exclude only exact guarded GOLD source-path contributions, preserving independent genera and all source observations. Exact target BTO:0000442. Shared mapping endpoints #1398 remain separate."}]} |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=BTO:0000442, grounding_status=EXACT, mapping_status=SEEDED, parent_habitats=["BTO:0001487"]. |
| EGOLD | data/raw/gold_ecosystem_paths.tsv; TSV rows 836 | supports | [{"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Arthropoda: Insects &gt; Fat body", "depth": "3", "ecosystem": "Host-associated", "ecosystem_category": "Arthropoda: Insects", "ecosystem_subtype": "", "ecosystem_type": "Fat body", "gold_node_count": "3", "gold_node_ids": "gold.ecosystem:7093&#124;gold.ecosystem:7094&#124;gold.ecosystem:7095", "leaf_label": "Fat body", "organism_count": "2", "specific_ecosystem": "", "study_count": "0", "total_assertions": "2"}, "row": 836}] |
| EONT | data/raw/ontology_terms.tsv; TSV rows 443,1487 | supports | [{"data": {"definition": "A fatty tissue especially of nearly mature insect larvae that serves as a food reserve.", "deprecated": "", "directly_referenced": "FALSE", "label": "fat body", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0000442"}, "row": 443}, {"data": {"definition": "Connective tissue in which fat is stored and which has the cells distended by droplets of fat.", "deprecated": "", "directly_referenced": "TRUE", "label": "adipose tissue", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0001487"}, "row": 1487}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 110,287,288,1001,1016,2853,2854,2855,4153,4155 | supports | [{"data": {"object": "BTO:0001487", "predicate": "rdfs:subClassOf", "subject": "BTO:0000156"}, "row": 110}, {"data": {"object": "BTO:0001487", "predicate": "rdfs:subClassOf", "subject": "BTO:0000442"}, "row": 287}, {"data": {"object": "BTO:0001487", "predicate": "rdfs:subClassOf", "subject": "BTO:0000444"}, "row": 288}, {"data": {"object": "BTO:0001487", "predicate": "rdfs:subClassOf", "subject": "BTO:0001456"}, "row": 1001}, {"data": {"object": "BTO:0000421", "predicate": "rdfs:subClassOf", "subject": "BTO:0001487"}, "row": 1016}, {"data": {"object": "BTO:0001487", "predicate": "rdfs:subClassOf", "subject": "BTO:0004041"}, "row": 2853}, {"data": {"object": "BTO:0001487", "predicate": "rdfs:subClassOf", "subject": "BTO:0004042"}, "row": 2854}, {"data": {"object": "BTO:0001487", "predicate": "rdfs:subClassOf", "subject": "BTO:0004043"}, "row": 2855}, {"data": {"object": "BTO:0001487", "predicate": "rdfs:subClassOf", "subject": "BTO:0005943"}, "row": 4153}, {"data": {"object": "BTO:0001487", "predicate": "rdfs:subClassOf", "subject": "BTO:0005945"}, "row": 4155}] |
| EP1 | data/habitats/host_associated/adipose_tissue.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": "Connective tissue in which fat is stored and which has the cells distended by droplets of fat.", "grounding_status": "EXACT", "identifier": "BTO:0001487", "label": "adipose tissue", "mapping_status": "SEEDED", "parent_habitats": ["BTO:0000421"], "source_attestations": [{"assertion_count": 29, "assertion_unit": "TAXON", "evidence_channels": "environmental_samples", "score": 1.45999, "source": "PREGO", "source_id": "BTO:0001487", "source_label": "adipose tissue"}]} |
| EP2 | data/habitats/host_associated/arthropoda_insects.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": "An environmental system determined by an insect.", "grounding_status": "UNGROUNDED", "identifier": "habitatmech:GOLD.dba2a83b95", "label": "insect-associated environment", "mapping_status": "REVIEWED", "parent_habitats": ["ENVO:01001000", "ENVO:01001002"], "source_attestations": [{"assertion_count": 1833, "assertion_unit": "ORGANISM", "notes": "4 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:7073", "source_label": "Arthropoda: Insects", "source_path": "Host-associated &gt; Arthropoda: Insects"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'fat_body&#124;BTO:0000442' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal located Stage 4 predecessor bundle 20261106T194831Z-fat_body-record (linked via EPREV and related_reviews) and checked related cohort and ancestor reviews for reconciliation. |
| EPREV | reviews/structured/20261106T194831Z-fat_body-record/review.yaml; Every immutable Stage 4 baseline finding | supports | Exact predecessor keys and findings reconciled; original inspected source scope preserved. |
| ETEST | tests/test_excretory_system_22ee753c_to_fecal_review_repairs.py; Complete full-corpus counterfactual regression suite | supports | Exactly twenty-two records differ from the counterfactual baseline across Issues #2304 and #2305. |
| EPARENTS | curation/gold_parent_exclusions.tsv; TSV line 18 | supports | [[18, "habitatmech:GOLD.e63b1e075e\tHost-associated &gt; Arthropoda: Insects &gt; Fat body\thabitatmech:GOLD.dba2a83b95\tantigravity\t2026-11-06\tReview https://github.com/CultureBotAI/HabitatMech/issues/2304 : Crustacean and annelid excretory system are organ systems, not subtypes of the whole crustacean- or annelid-associated host environment; external genitalia is an anatomical reproductive organ structure, not a subtype of the entire mammalian or human reproductive system; external soft tissue zone is a soft-tissue anatomical region, not a subtype of the mammalian Multiple systems GOLD classification bucket; mammalian, piscine, and human eye are sense organs and ciliary body and vitreous chamber are intraocular structures/compartments, not subtypes of the entire visual system; human and mammalian fallopian tube are oviductal reproductive organs, not subtypes of the entire reproductive system; mammalian and human fascia are connective tissue sheets, not subtypes of the host-scoped connective tissue assemblage; insect fat body is an adipose organ/tissue, not a subtype of the whole insect-associated environment; feather is an avian epidermal appendage, not a subtype of the whole avian skin organ. Exclude only exact guarded GOLD source-path contributions, preserving independent genera and all source observations. Exact target BTO:0000442. Shared mapping endpoints #1398 remain separate."]] |
| EHIST_G1 | history/other/gold_parent_exclusions/2026-11-07T045500Z-antigravity-230401.yaml; Complete curation session history event | supports | Authorized curation event for Issue #2304 recorded and validated. |

## Limits And Additional Notes

- Only the stated primary evidence and current ontology/taxonomy authorities were independently inspected; original specimen-level support for every source-bin member is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism or characteristic presence. Parent observations are not inherited by children.
- Configured label correspondence skipped 2,084 no-adapter pairs; this is not whole-corpus identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in this pre-save observation.
- iModulonDB is not applicable: the target has no gene, regulator or expression-module assertion. No paid research or scientific-status promotion was performed.
- Saved against working-tree repairs atop main commit 30fbe25f4c539ad6266dae7680d21e451caf6e40; all earlier saved bundles in reviews/structured/ remain byte-identical.
- Reconciles predecessor bundle 20261106T194831Z-fat_body-record with exact issue_key and previous_occurrences lineage.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261107T050021Z-fat_body-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: fat_body'
started_at: '2026-11-07T04:55:00Z'
finished_at: '2026-11-07T05:00:21Z'
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
summary: Removed the guarded GOLD whole-host context-parent contribution habitatmech:GOLD.dba2a83b95
  (insect-associated environment) for source concept habitatmech:GOLD.e63b1e075e via
  curation/gold_parent_exclusions.tsv (#2304), preserving broader ontology parent
  BTO:0001487 (adipose tissue). Identity (BTO:0000442, 'fat body'), native SEEDED/EXACT
  status, and source observations are preserved. No unresolved predecessor finding
  remains in this target scope.
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
  - path: data/habitats/host_associated/adipose_tissue.yaml
    sha256: 864bdf2a2f2a5a1e99716a7ea9c354a0d2cec4833c183458f526f54ed313329e
    role: context
  - path: data/habitats/host_associated/arthropoda_insects.yaml
    sha256: 7ccd793f67de18d846d25fad8906f7ad0bef91872ae3a68c60532ebdde7e0c80
    role: context
  - path: data/habitats/host_associated/fat_body.yaml
    sha256: ff1e1543ee5e0e72f6478b24b4c20b3aa3cb16898d50be71e983535033a8c541
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
  - path: history/other/definition_source_label_exclusions/2026-11-07T045510Z-antigravity-230501.yaml
    sha256: 16115355944b03d6e09142bca848ee5d52d3ab9332e2367433aebb6177da314c
    role: context
  - path: history/other/gold_parent_exclusions/2026-11-07T045500Z-antigravity-230401.yaml
    sha256: d55f782e57e1c75b9485ba0c5e39260dfcbaed7532af9a7fc30c3316874efac9
    role: context
  - path: reviews/structured/20261106T194831Z-fat_body-record/review.yaml
    sha256: d63b405f3862773fb856f02275b5a21bc1696453e5d287854a6e467ba3f1988d
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
- target_id: BTO:0000442
  path: data/habitats/host_associated/fat_body.yaml
  label: fat body
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
    finding on data/habitats/host_associated/fat_body.yaml after bounded Cycle 6 Stage
    5 remediation.
  selection: One of twenty-two repaired targets from the excretory_system__22ee753c-through-fecal
    cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - BTO:0000442
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
    --target-class HabitatRecord data/habitats/host_associated/fat_body.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000442
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
  - BTO:0000442
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
  - BTO:0000442
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
  - BTO:0000442
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
  - BTO:0000442
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
  - BTO:0000442
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
  - BTO:0000442
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
  - BTO:0000442
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
  - BTO:0000442
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
  - BTO:0000442
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
  - BTO:0000442
  summary: Completed 2026-11-07T04:59:50Z. rendered 3209 habitat pages, 750 redirect
    stubs, 8 categories, 696 term requests; pages/ is in step with the corpus.
  scope_note: Full-corpus static site parity check.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/fat_body.yaml
  locator: Entire YAML
  accessed_at: '2026-11-07T05:00:21Z'
  support: supports
  summary: '{"identifier": "BTO:0000442", "label": "fat body", "grounding_status":
    "EXACT", "mapping_status": "SEEDED", "parent_habitats": ["BTO:0001487"], "synonyms":
    [], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:7093",
    "source_label": "Fat body", "source_path": "Host-associated > Arthropoda: Insects
    > Fat body", "mapping_predicate": "skos:exactMatch", "assertion_count": 2, "assertion_unit":
    "ORGANISM", "notes": "3 GOLD ecosystem node ids share this path; first shown.
    See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp":
    "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES",
    "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: EXACT."},
    {"timestamp": "2026-11-06T00:00:00Z", "curator": "antigravity", "action": "SOURCE_PARENT_EXCLUDED",
    "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.dba2a83b95
    for habitatmech:GOLD.e63b1e075e (Host-associated > Arthropoda: Insects > Fat body).
    Review https://github.com/CultureBotAI/HabitatMech/issues/2304 : Crustacean and
    annelid excretory system are organ systems, not subtypes of the whole crustacean-
    or annelid-associated host environment; external genitalia is an anatomical reproductive
    organ structure, not a subtype of the entire mammalian or human reproductive system;
    external soft tissue zone is a soft-tissue anatomical region, not a subtype of
    the mammalian Multiple systems GOLD classification bucket; mammalian, piscine,
    and human eye are sense organs and ciliary body and vitreous chamber are intraocular
    structures/compartments, not subtypes of the entire visual system; human and mammalian
    fallopian tube are oviductal reproductive organs, not subtypes of the entire reproductive
    system; mammalian and human fascia are connective tissue sheets, not subtypes
    of the host-scoped connective tissue assemblage; insect fat body is an adipose
    organ/tissue, not a subtype of the whole insect-associated environment; feather
    is an avian epidermal appendage, not a subtype of the whole avian skin organ.
    Exclude only exact guarded GOLD source-path contributions, preserving independent
    genera and all source observations. Exact target BTO:0000442. Shared mapping endpoints
    #1398 remain separate."}]}'
  snapshot_sha256: ff1e1543ee5e0e72f6478b24b4c20b3aa3cb16898d50be71e983535033a8c541
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-07T05:00:21Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon terms cannot substitute
    for associated environments; parent_habitats must be strictly broader across all
    contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-07T05:00:21Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-07T05:00:21Z'
  support: supports
  summary: Seed generator produces identifier=BTO:0000442, grounding_status=EXACT,
    mapping_status=SEEDED, parent_habitats=["BTO:0001487"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EGOLD
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV rows 836
  accessed_at: '2026-11-07T05:00:21Z'
  support: supports
  summary: '[{"data": {"biosample_count": "0", "canonical_path": "Host-associated
    > Arthropoda: Insects > Fat body", "depth": "3", "ecosystem": "Host-associated",
    "ecosystem_category": "Arthropoda: Insects", "ecosystem_subtype": "", "ecosystem_type":
    "Fat body", "gold_node_count": "3", "gold_node_ids": "gold.ecosystem:7093|gold.ecosystem:7094|gold.ecosystem:7095",
    "leaf_label": "Fat body", "organism_count": "2", "specific_ecosystem": "", "study_count":
    "0", "total_assertions": "2"}, "row": 836}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 443,1487
  accessed_at: '2026-11-07T05:00:21Z'
  support: supports
  summary: '[{"data": {"definition": "A fatty tissue especially of nearly mature insect
    larvae that serves as a food reserve.", "deprecated": "", "directly_referenced":
    "FALSE", "label": "fat body", "label_only": "FALSE", "ontology": "BTO", "synonyms":
    "", "term_id": "BTO:0000442"}, "row": 443}, {"data": {"definition": "Connective
    tissue in which fat is stored and which has the cells distended by droplets of
    fat.", "deprecated": "", "directly_referenced": "TRUE", "label": "adipose tissue",
    "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0001487"},
    "row": 1487}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 110,287,288,1001,1016,2853,2854,2855,4153,4155
  accessed_at: '2026-11-07T05:00:21Z'
  support: supports
  summary: '[{"data": {"object": "BTO:0001487", "predicate": "rdfs:subClassOf", "subject":
    "BTO:0000156"}, "row": 110}, {"data": {"object": "BTO:0001487", "predicate": "rdfs:subClassOf",
    "subject": "BTO:0000442"}, "row": 287}, {"data": {"object": "BTO:0001487", "predicate":
    "rdfs:subClassOf", "subject": "BTO:0000444"}, "row": 288}, {"data": {"object":
    "BTO:0001487", "predicate": "rdfs:subClassOf", "subject": "BTO:0001456"}, "row":
    1001}, {"data": {"object": "BTO:0000421", "predicate": "rdfs:subClassOf", "subject":
    "BTO:0001487"}, "row": 1016}, {"data": {"object": "BTO:0001487", "predicate":
    "rdfs:subClassOf", "subject": "BTO:0004041"}, "row": 2853}, {"data": {"object":
    "BTO:0001487", "predicate": "rdfs:subClassOf", "subject": "BTO:0004042"}, "row":
    2854}, {"data": {"object": "BTO:0001487", "predicate": "rdfs:subClassOf", "subject":
    "BTO:0004043"}, "row": 2855}, {"data": {"object": "BTO:0001487", "predicate":
    "rdfs:subClassOf", "subject": "BTO:0005943"}, "row": 4153}, {"data": {"object":
    "BTO:0001487", "predicate": "rdfs:subClassOf", "subject": "BTO:0005945"}, "row":
    4155}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EP1
  kind: record_content
  reference: data/habitats/host_associated/adipose_tissue.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-11-07T05:00:21Z'
  support: supports
  summary: '{"definition": "Connective tissue in which fat is stored and which has
    the cells distended by droplets of fat.", "grounding_status": "EXACT", "identifier":
    "BTO:0001487", "label": "adipose tissue", "mapping_status": "SEEDED", "parent_habitats":
    ["BTO:0000421"], "source_attestations": [{"assertion_count": 29, "assertion_unit":
    "TAXON", "evidence_channels": "environmental_samples", "score": 1.45999, "source":
    "PREGO", "source_id": "BTO:0001487", "source_label": "adipose tissue"}]}'
  snapshot_sha256: 864bdf2a2f2a5a1e99716a7ea9c354a0d2cec4833c183458f526f54ed313329e
- evidence_id: EP2
  kind: record_content
  reference: data/habitats/host_associated/arthropoda_insects.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-11-07T05:00:21Z'
  support: supports
  summary: '{"definition": "An environmental system determined by an insect.", "grounding_status":
    "UNGROUNDED", "identifier": "habitatmech:GOLD.dba2a83b95", "label": "insect-associated
    environment", "mapping_status": "REVIEWED", "parent_habitats": ["ENVO:01001000",
    "ENVO:01001002"], "source_attestations": [{"assertion_count": 1833, "assertion_unit":
    "ORGANISM", "notes": "4 GOLD ecosystem node ids share this path; first shown.
    See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:7073",
    "source_label": "Arthropoda: Insects", "source_path": "Host-associated > Arthropoda:
    Insects"}]}'
  snapshot_sha256: 7ccd793f67de18d846d25fad8906f7ad0bef91872ae3a68c60532ebdde7e0c80
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'fat_body|BTO:0000442' reviews/structured/*/review.yaml curation/
    history/
  accessed_at: '2026-11-07T05:00:21Z'
  support: context_only
  summary: Structured-review traversal located Stage 4 predecessor bundle 20261106T194831Z-fat_body-record
    (linked via EPREV and related_reviews) and checked related cohort and ancestor
    reviews for reconciliation.
  search_scope: curation, history, data/raw, and reviews/structured/*/review.yaml
    traversal at commit 30fbe25f4c539ad6266dae7680d21e451caf6e40.
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261106T194831Z-fat_body-record/review.yaml
  locator: Every immutable Stage 4 baseline finding
  accessed_at: '2026-11-07T05:00:21Z'
  support: supports
  summary: Exact predecessor keys and findings reconciled; original inspected source
    scope preserved.
  snapshot_sha256: d63b405f3862773fb856f02275b5a21bc1696453e5d287854a6e467ba3f1988d
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_excretory_system_22ee753c_to_fecal_review_repairs.py
  locator: Complete full-corpus counterfactual regression suite
  accessed_at: '2026-11-07T05:00:21Z'
  support: supports
  summary: 'Exactly twenty-two records differ from the counterfactual baseline across
    Issues #2304 and #2305.'
  snapshot_sha256: 90bb097e6a2311fbaf0a2afadc4ca7642581bab11e5dd3d582ea5cd149c066f6
- evidence_id: EPARENTS
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: TSV line 18
  accessed_at: '2026-11-07T05:00:21Z'
  support: supports
  summary: '[[18, "habitatmech:GOLD.e63b1e075e\tHost-associated > Arthropoda: Insects
    > Fat body\thabitatmech:GOLD.dba2a83b95\tantigravity\t2026-11-06\tReview https://github.com/CultureBotAI/HabitatMech/issues/2304
    : Crustacean and annelid excretory system are organ systems, not subtypes of the
    whole crustacean- or annelid-associated host environment; external genitalia is
    an anatomical reproductive organ structure, not a subtype of the entire mammalian
    or human reproductive system; external soft tissue zone is a soft-tissue anatomical
    region, not a subtype of the mammalian Multiple systems GOLD classification bucket;
    mammalian, piscine, and human eye are sense organs and ciliary body and vitreous
    chamber are intraocular structures/compartments, not subtypes of the entire visual
    system; human and mammalian fallopian tube are oviductal reproductive organs,
    not subtypes of the entire reproductive system; mammalian and human fascia are
    connective tissue sheets, not subtypes of the host-scoped connective tissue assemblage;
    insect fat body is an adipose organ/tissue, not a subtype of the whole insect-associated
    environment; feather is an avian epidermal appendage, not a subtype of the whole
    avian skin organ. Exclude only exact guarded GOLD source-path contributions, preserving
    independent genera and all source observations. Exact target BTO:0000442. Shared
    mapping endpoints #1398 remain separate."]]'
  snapshot_sha256: 913f1ece5224bbed33b736f78cc8e1244155e91f390fe8e790d6f91a24b3b796
- evidence_id: EHIST_G1
  kind: record_content
  reference: history/other/gold_parent_exclusions/2026-11-07T045500Z-antigravity-230401.yaml
  locator: Complete curation session history event
  accessed_at: '2026-11-07T05:00:21Z'
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
  - BTO:0000442
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EP1
  - EP2
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST_G1
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: supported
  summary: 'BTO:0000442: fat body; EXACT/SEEDED; parents ["BTO:0001487"]. Removed
    the guarded GOLD whole-host context-parent contribution habitatmech:GOLD.dba2a83b95
    (insect-associated environment) for source concept habitatmech:GOLD.e63b1e075e
    via curation/gold_parent_exclusions.tsv (#2304), preserving broader ontology parent
    BTO:0001487 (adipose tissue). Identity (BTO:0000442, ''fat body''), native SEEDED/EXACT
    status, and source observations are preserved. No unresolved predecessor finding
    remains in this target scope.'
  target_ids:
  - BTO:0000442
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EP1
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
    and pools: [{"source": "GOLD", "count": 2, "unit": "ORGANISM"}]. Zero counts are
    omitted; unrelated parent counts are not combined.'
  target_ids:
  - BTO:0000442
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EP1
  - EP2
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST_G1
- assessment_id: A4
  area: representation
  topic: Predecessor finding reconciliation
  outcome: supported
  summary: Every predecessor finding preserves its stable issue_key and exact lineage.
    All predecessor findings in this target scope are resolved.
  target_ids:
  - BTO:0000442
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EP1
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
    decisions and executed routes reproduce SEEDED / EXACT; this read-only review
    does not mutate generated records.
  target_ids:
  - BTO:0000442
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EP1
  - EP2
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST_G1
findings:
- finding_id: F1
  issue_key: fat-body-context-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Fat body retains whole-host insect-associated environment GOLD parent as
    a superclass
  description: 'Add an exclusion row in curation/gold_parent_exclusions.tsv for source
    identifier habitatmech:GOLD.e63b1e075e on GOLD path ''Host-associated > Arthropoda:
    Insects > Fat body'' (exact target BTO:0000442) excluding parent_id habitatmech:GOLD.dba2a83b95
    (insect-associated environment), preserving ontology parent BTO:0001487 (adipose
    tissue).'
  target_ids:
  - BTO:0000442
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
  - EP1
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
  - https://github.com/CultureBotAI/HabitatMech/issues/2304
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261106T194831Z-fat_body-record
    finding_id: F1
  disposition_reason: Excluded only the guarded GOLD whole-host context-parent contribution
    habitatmech:GOLD.dba2a83b95 (insect-associated environment) for source concept
    habitatmech:GOLD.e63b1e075e in curation/gold_parent_exclusions.tsv (#2304), preserving
    broader ontology parent BTO:0001487 (adipose tissue).
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
- Reconciles predecessor bundle 20261106T194831Z-fat_body-record with exact issue_key
  and previous_occurrences lineage.
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261106T194831Z-fat_body-record
  relationship: Exact predecessor; every finding explicitly reconciled.
```
