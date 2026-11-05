# Remediation review: excretory_system

- Review: 20261105T152514Z-excretory_system-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-05T15:20:00Z
- Finished UTC: 2026-11-05T15:25:14Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Removed the guarded GOLD whole-host context-parent contribution habitatmech:GOLD.0ef2e24505 (insect-associated environment) via curation/gold_parent_exclusions.tsv (#2295), preserving broader ontology parent UBERON:0001008 (renal system). Identity (habitatmech:GOLD.3a0549cbd8), native REVIEWED/NARROW status, and source observations are preserved. The global NARROW source-attestation endpoint finding (#1398) remains explicitly open.

## Scope And Provenance

Full current target assessment and explicit disposition of every baseline finding on data/habitats/host_associated/excretory_system.yaml after bounded Cycle 5 Stage 5 remediation.

Selection: One of fourteen repaired targets from the epicuticular_wax-through-excretory_system cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f0c857592f79534eeb3701824a58eb7b5fcefef3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.3a0549cbd8 | data/habitats/host_associated/excretory_system.yaml | generated | Excretory system |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.3a0549cbd8 | Completed 2026-11-05T04:42:18Z. No issues found. |
| validate-strict | passed | True | habitatmech:GOLD.3a0549cbd8 | Completed 2026-11-05T04:55:15Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | habitatmech:GOLD.3a0549cbd8 | Completed 2026-11-05T15:24:00Z. No issues found; 864 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | habitatmech:GOLD.3a0549cbd8 | Completed 2026-11-05T04:40:25Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | habitatmech:GOLD.3a0549cbd8 | Completed 2026-11-05T15:24:10Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | habitatmech:GOLD.3a0549cbd8 | Completed 2026-11-05T04:40:29Z. validated 73 causal-graph curation file(s) with 73 graph(s). |
| term-requests-check | passed | True | habitatmech:GOLD.3a0549cbd8 | Completed 2026-11-05T15:24:15Z. term-request table is current (671 terms). |
| validate-products | passed | True | habitatmech:GOLD.3a0549cbd8 | Completed 2026-11-05T04:43:01Z. OK_CANONICAL: 1200, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2077. All id&lt;-&gt;label pairs correspond. |
| pytest counterfactual review repairs | passed | True | habitatmech:GOLD.3a0549cbd8 | Completed 2026-11-05T15:24:30Z. 2 passed; exact 14-record counterfactual diff verified. |
| curation-floor | passed | True | habitatmech:GOLD.3a0549cbd8 | Completed 2026-11-05T15:24:35Z. Floor satisfied across all 13 metrics. |
| render-check | passed | True | habitatmech:GOLD.3a0549cbd8 | Completed 2026-11-05T15:24:50Z. rendered 3209 habitat pages, 750 redirect stubs, 8 categories, 696 term requests; pages/ is in step with the corpus. |

## Scientific And Domain Assessments

### Native validity and reproduction after bounded remediation

schema: supported. Targets: habitatmech:GOLD.3a0549cbd8.

Individual schema, strict 24-target validation, 864 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 73 causal overlays, 671 term requests, curation floor, site parity, and counterfactual regression tests passed.

### Identity, definition, hierarchy and aliases

identity: concern. Targets: habitatmech:GOLD.3a0549cbd8.

habitatmech:GOLD.3a0549cbd8: Excretory system; NARROW/SEEDED; parents ["UBERON:8450002"]. Removed the guarded GOLD whole-host context-parent contribution habitatmech:GOLD.0ef2e24505 (insect-associated environment) via curation/gold_parent_exclusions.tsv (#2295), preserving broader ontology parent UBERON:0001008 (renal system). Identity (habitatmech:GOLD.3a0549cbd8), native REVIEWED/NARROW status, and source observations are preserved. The global NARROW source-attestation endpoint finding (#1398) remains explicitly open.

### Source counts and retained ranking

quantity: supported. Targets: habitatmech:GOLD.3a0549cbd8.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"source": "GOLD", "count": null, "unit": null}]. Zero counts are omitted; unrelated parent counts are not combined.

### Predecessor finding reconciliation

representation: concern. Targets: habitatmech:GOLD.3a0549cbd8.

Every predecessor finding preserves its stable issue_key and exact lineage. F1 is resolved under #2295; F2 remains open under corpus-wide issue #1398.

### Parameters, mechanisms and native status

completeness: supported. Targets: habitatmech:GOLD.3a0549cbd8.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce SEEDED / NARROW; this read-only review does not mutate generated records.

## Findings

### F1: Insect Excretory system retains whole-host insect-associated environment GOLD parent as a superclass

major / resolved / confirmed; issue key: excretory-system-context-parent.

Add an exclusion row in curation/gold_parent_exclusions.tsv for source identifier habitatmech:GOLD.3a0549cbd8 on GOLD path 'Host-associated &gt; Arthropoda: Insects &gt; Excretory system' (exact target habitatmech:GOLD.3a0549cbd8) excluding parent_id habitatmech:GOLD.dba2a83b95 (insect-associated environment), preserving broader ontology parent UBERON:8450002 (excretory system).

Disposition: Excluded only the guarded GOLD whole-host context-parent contribution habitatmech:GOLD.0ef2e24505 (insect-associated environment) in curation/gold_parent_exclusions.tsv (#2295), preserving broader ontology parent UBERON:0001008 (renal system).

### F2: Narrow mapping predicate points to a minted source-path record

major / open / confirmed; issue key: excretory-system-mapping-endpoint-contract.

Reconcile narrow-match source-attestation output with the endpoint contract tracked in Issue #1398 for habitatmech:GOLD.3a0549cbd8 (Host-associated &gt; Arthropoda: Insects &gt; Excretory system) and its broader ontology parent UBERON:8450002 (excretory system).

Disposition: The retained NARROW source/record endpoint mismatch (#1398) is unchanged; a guarded GOLD context-parent exclusion does not alter the global SourceAttestation.mapping_predicate endpoint contract.

## Recommended Actions And Acceptance Checks

### ACT2

Reconcile narrow-match source-attestation output with the endpoint contract tracked in Issue #1398 for habitatmech:GOLD.3a0549cbd8 (Host-associated &gt; Arthropoda: Insects &gt; Excretory system) and its broader ontology parent UBERON:8450002 (excretory system). No repair is performed by this read-only review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/excretory_system.yaml; Entire YAML | supports | {"identifier": "habitatmech:GOLD.3a0549cbd8", "label": "Excretory system", "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:8450002"], "synonyms": [], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:7184", "source_label": "Excretory system", "source_path": "Host-associated &gt; Arthropoda: Insects &gt; Excretory system", "mapping_predicate": "skos:narrowMatch", "notes": "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NARROW."}, {"timestamp": "2026-11-05T00:00:00Z", "curator": "antigravity", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.dba2a83b95 for habitatmech:GOLD.3a0549cbd8 (Host-associated &gt; Arthropoda: Insects &gt; Excretory system). Review https://github.com/CultureBotAI/HabitatMech/issues/2295 : Epicuticular wax is the outer cuticular wax layer on a leaf surface, not a subtype of the whole leaf organ (PO:0025034); epithelial lining fluid is the respiratory mucosal surface liquid, not the entire human respiratory system; erythrocyte is a circulating red blood cell, not the entire human blood tissue; esophageal ulcer is a mucosal lesion/disease concept, not a subtype of the anatomical human esophagus; crustacean, piscine, avian, human and mammalian esophagus are tubular digestive organs, not subtypes of the entire foregut or digestive system; ethmoid bone is a cranial bone, not the human-scoped bone assemblage; mammalian and human Eustachian tube are pharyngotympanic tubes, not subtypes of the middle ear cavity; insect excretory system is an organ system, not a subtype of the whole insect-associated environment. Exclude only exact guarded GOLD source-path contributions, preserving independent genera and all source observations. Exact target habitatmech:GOLD.3a0549cbd8. Shared mapping endpoints #1398 remain separate."}]} |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=habitatmech:GOLD.3a0549cbd8, grounding_status=NARROW, mapping_status=SEEDED, parent_habitats=["UBERON:8450002"]. |
| EGOLD | data/raw/gold_ecosystem_paths.tsv; TSV rows 1817 | supports | [{"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Arthropoda: Insects &gt; Excretory system", "depth": "3", "ecosystem": "Host-associated", "ecosystem_category": "Arthropoda: Insects", "ecosystem_subtype": "", "ecosystem_type": "Excretory system", "gold_node_count": "3", "gold_node_ids": "gold.ecosystem:7184&#124;gold.ecosystem:7363&#124;gold.ecosystem:7364", "leaf_label": "Excretory system", "organism_count": "0", "specific_ecosystem": "", "study_count": "0", "total_assertions": "0"}, "row": 1817}] |
| EONT | data/raw/ontology_terms.tsv; TSV rows 13546 | supports | [{"data": {"definition": "An anatomical system that eliminates waste products that arise as a result of metabolic activity.", "deprecated": "", "directly_referenced": "FALSE", "label": "excretory system", "label_only": "FALSE", "ontology": "UBERON", "synonyms": "", "term_id": "UBERON:8450002"}, "row": 13546}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 11134,11878 | supports | [{"data": {"object": "UBERON:8450002", "predicate": "rdfs:subClassOf", "subject": "UBERON:0001008"}, "row": 11134}, {"data": {"object": "UBERON:0000467", "predicate": "rdfs:subClassOf", "subject": "UBERON:8450002"}, "row": 11878}] |
| EP2 | data/habitats/host_associated/arthropoda_insects.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": "An environmental system determined by an insect.", "grounding_status": "UNGROUNDED", "identifier": "habitatmech:GOLD.dba2a83b95", "label": "insect-associated environment", "mapping_status": "REVIEWED", "parent_habitats": ["ENVO:01001000", "ENVO:01001002"], "source_attestations": [{"assertion_count": 1833, "assertion_unit": "ORGANISM", "notes": "4 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:7073", "source_label": "Arthropoda: Insects", "source_path": "Host-associated &gt; Arthropoda: Insects"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'excretory_system&#124;habitatmech:GOLD.3a0549cbd8' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal verified no prior target review bundle exists for this record; curation and history tables were inspected for all matching rows. |
| EPREV | reviews/structured/20261105T051533Z-excretory_system-record/review.yaml; Every immutable Stage 4 baseline finding | supports | Exact predecessor keys and findings reconciled; original inspected source scope preserved. |
| ETEST | tests/test_epicuticular_wax_to_excretory_system_review_repairs.py; Complete full-corpus counterfactual regression suite | supports | Exactly fourteen records differ from the counterfactual baseline across Issues #2295 and #2296. |
| EPARENTS | curation/gold_parent_exclusions.tsv; TSV line 14 | supports | [[14, "habitatmech:GOLD.3a0549cbd8\tHost-associated &gt; Arthropoda: Insects &gt; Excretory system\thabitatmech:GOLD.dba2a83b95\tantigravity\t2026-11-05\tReview https://github.com/CultureBotAI/HabitatMech/issues/2295 : Epicuticular wax is the outer cuticular wax layer on a leaf surface, not a subtype of the whole leaf organ (PO:0025034); epithelial lining fluid is the respiratory mucosal surface liquid, not the entire human respiratory system; erythrocyte is a circulating red blood cell, not the entire human blood tissue; esophageal ulcer is a mucosal lesion/disease concept, not a subtype of the anatomical human esophagus; crustacean, piscine, avian, human and mammalian esophagus are tubular digestive organs, not subtypes of the entire foregut or digestive system; ethmoid bone is a cranial bone, not the human-scoped bone assemblage; mammalian and human Eustachian tube are pharyngotympanic tubes, not subtypes of the middle ear cavity; insect excretory system is an organ system, not a subtype of the whole insect-associated environment. Exclude only exact guarded GOLD source-path contributions, preserving independent genera and all source observations. Exact target habitatmech:GOLD.3a0549cbd8. Shared mapping endpoints #1398 remain separate."]] |
| EHIST_G1 | history/other/gold_parent_exclusions/2026-11-05T151500Z-antigravity-229501.yaml; Complete curation session history event | supports | Authorized curation event for Issue #2295 recorded and validated. |

## Limits And Additional Notes

- Only the stated primary evidence and current ontology/taxonomy authorities were independently inspected; original specimen-level support for every source-bin member is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism or characteristic presence. Parent observations are not inherited by children.
- Configured label correspondence skipped 2,077 no-adapter pairs; this is not whole-corpus identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in this pre-save observation.
- iModulonDB is not applicable: the target has no gene, regulator or expression-module assertion. No paid research or scientific-status promotion was performed.
- Saved against working-tree repairs atop main commit f0c857592f79534eeb3701824a58eb7b5fcefef3; all earlier saved bundles in reviews/structured/ remain byte-identical.
- Reconciles predecessor bundle 20261105T051533Z-excretory_system-record with exact issue_key and previous_occurrences lineage.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T152514Z-excretory_system-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: excretory_system'
started_at: '2026-11-05T15:20:00Z'
finished_at: '2026-11-05T15:25:14Z'
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
summary: Removed the guarded GOLD whole-host context-parent contribution habitatmech:GOLD.0ef2e24505
  (insect-associated environment) via curation/gold_parent_exclusions.tsv (#2295),
  preserving broader ontology parent UBERON:0001008 (renal system). Identity (habitatmech:GOLD.3a0549cbd8),
  native REVIEWED/NARROW status, and source observations are preserved. The global
  NARROW source-attestation endpoint finding (#1398) remains explicitly open.
source:
  git_revision: f0c857592f79534eeb3701824a58eb7b5fcefef3
  state: working_tree
  inputs:
  - path: curation/decisions.tsv
    sha256: e39c962e767c655c22d6b1b5cf1cc392be3af21c2514e9c70d4c6105782d5650
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 725655426fded7f138d9a3e4e7a47eb1165f9a6a6a0d16cd242c07fcebfa0f8c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: c1efdfa9188346f3292250e42e9f2315d2d49d8c6235e07733efda22039a5c1c
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: c1207270bb0ae2031e42de6cb8220b20f98886f65e40d48793bfd7e9d757d83a
    role: context
  - path: curation/term_requests.tsv
    sha256: 72d7573cdee85f7cd54d27e2c864654b1f3b1121444c28b8d65e901edff9b053
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/host_associated/arthropoda_insects.yaml
    sha256: 7ccd793f67de18d846d25fad8906f7ad0bef91872ae3a68c60532ebdde7e0c80
    role: context
  - path: data/habitats/host_associated/excretory_system.yaml
    sha256: 6f0d6c6b89b978e25cf87809f5f877300a5662b7f3c2d313461f702b804b9e32
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
  - path: history/other/definition_source_label_exclusions/2026-11-05T151510Z-antigravity-229601.yaml
    sha256: b9af84e90e318d221396ff09e6ae4e926e74bdbfc692ae6cc1a9334c8429abe7
    role: context
  - path: history/other/gold_parent_exclusions/2026-11-05T151500Z-antigravity-229501.yaml
    sha256: 55bcac9e6231000d583bef7c9bff80f24c0a32b3e1c3ede0322550656637c0ec
    role: context
  - path: reviews/structured/20261105T051533Z-excretory_system-record/review.yaml
    sha256: b1b07b969cca45dd179dcd3cce453e425f7a466540c1086d72996a71d688e8da
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
    role: context
  - path: src/habitatmech/seed.py
    sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
    role: context
  - path: tests/test_epicuticular_wax_to_excretory_system_review_repairs.py
    sha256: 49996201e6fc34bd32f03bad90354d16c9efedb37f518d1020daf68a99e25afe
    role: context
targets:
- target_id: habitatmech:GOLD.3a0549cbd8
  path: data/habitats/host_associated/excretory_system.yaml
  label: Excretory system
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
    finding on data/habitats/host_associated/excretory_system.yaml after bounded Cycle
    5 Stage 5 remediation.
  selection: One of fourteen repaired targets from the epicuticular_wax-through-excretory_system
    cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.3a0549cbd8
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
    --target-class HabitatRecord data/habitats/host_associated/excretory_system.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.3a0549cbd8
  summary: Completed 2026-11-05T04:42:18Z. No issues found.
  scope_note: Individual schema; strict command covers the 24 named cohort targets;
    other documented gates have full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/habitats/host_associated/epicuticular_wax.yaml
    data/habitats/host_associated/epidermal_cell.yaml data/habitats/host_associated/epidermis.yaml
    data/habitats/host_associated/epidermoid.yaml data/habitats/host_associated/epiphytes.yaml
    data/habitats/host_associated/epiphytes__ec31dd8e.yaml data/habitats/host_associated/epithelial_cell.yaml
    data/habitats/host_associated/epithelial_lining_fluid.yaml data/habitats/host_associated/epithelium.yaml
    data/habitats/host_associated/equidae_horse.yaml data/habitats/host_associated/erythrocyte.yaml
    data/habitats/host_associated/erythroleukemia_cell_line.yaml data/habitats/host_associated/esophageal_ulcer.yaml
    data/habitats/host_associated/esophagus.yaml data/habitats/host_associated/esophagus__25614af3.yaml
    data/habitats/host_associated/esophagus__2ce9b1a3.yaml data/habitats/host_associated/esophagus__d8421c5e.yaml
    data/habitats/host_associated/esophagus__e0ae9e65.yaml data/habitats/host_associated/esophagus__e4629951.yaml
    data/habitats/host_associated/ethmoid_bone.yaml data/habitats/host_associated/eustachian_tube.yaml
    data/habitats/host_associated/eustachian_tube__a8583033.yaml data/habitats/host_associated/excavata.yaml
    data/habitats/host_associated/excretory_system.yaml --out /tmp/c5s4_24_strict.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.3a0549cbd8
  summary: 'Completed 2026-11-05T04:55:15Z. Validated 24 files; files with ERROR:
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
  - habitatmech:GOLD.3a0549cbd8
  summary: Completed 2026-11-05T15:24:00Z. No issues found; 864 history record(s)
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
  - habitatmech:GOLD.3a0549cbd8
  summary: 'Completed 2026-11-05T04:40:25Z. provenance current: 14 committed inventories,
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
  - habitatmech:GOLD.3a0549cbd8
  summary: 'Completed 2026-11-05T15:24:10Z. expected 3209 records, found 3209 on disk;
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
  - habitatmech:GOLD.3a0549cbd8
  summary: Completed 2026-11-05T04:40:29Z. validated 73 causal-graph curation file(s)
    with 73 graph(s).
  scope_note: Full-corpus causal-graph overlay validation.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: .venv/bin/python scripts/build_term_requests.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.3a0549cbd8
  summary: Completed 2026-11-05T15:24:15Z. term-request table is current (671 terms).
  scope_note: Full-corpus term-request table currency check.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.3a0549cbd8
  summary: 'Completed 2026-11-05T04:43:01Z. OK_CANONICAL: 1200, OK_SYNONYM: 1, OK_EXCEPTION:
    5, SKIPPED_NO_ADAPTER: 2077. All id<->label pairs correspond.'
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
- check_id: C9
  name: pytest counterfactual review repairs
  status: passed
  required: true
  command: .venv/bin/python -m pytest tests/test_epicuticular_wax_to_excretory_system_review_repairs.py
    -q --no-cov
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.3a0549cbd8
  summary: Completed 2026-11-05T15:24:30Z. 2 passed; exact 14-record counterfactual
    diff verified.
  scope_note: 'Full-corpus counterfactual regression test for Issues #2295 and #2296.'
- check_id: C10
  name: curation-floor
  status: passed
  required: true
  command: .venv/bin/python scripts/check_curation_floor.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.3a0549cbd8
  summary: Completed 2026-11-05T15:24:35Z. Floor satisfied across all 13 metrics.
  scope_note: Full-corpus curation floor ratchets.
- check_id: C11
  name: render-check
  status: passed
  required: true
  command: .venv/bin/python scripts/render_pages.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.3a0549cbd8
  summary: Completed 2026-11-05T15:24:50Z. rendered 3209 habitat pages, 750 redirect
    stubs, 8 categories, 696 term requests; pages/ is in step with the corpus.
  scope_note: Full-corpus static site parity check.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/excretory_system.yaml
  locator: Entire YAML
  accessed_at: '2026-11-05T15:25:14Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.3a0549cbd8", "label": "Excretory system",
    "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:8450002"],
    "synonyms": [], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:7184",
    "source_label": "Excretory system", "source_path": "Host-associated > Arthropoda:
    Insects > Excretory system", "mapping_predicate": "skos:narrowMatch", "notes":
    "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}],
    "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources",
    "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories;
    attested by GOLD. Grounding: NARROW."}, {"timestamp": "2026-11-05T00:00:00Z",
    "curator": "antigravity", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded
    GOLD source-path parent contribution habitatmech:GOLD.dba2a83b95 for habitatmech:GOLD.3a0549cbd8
    (Host-associated > Arthropoda: Insects > Excretory system). Review https://github.com/CultureBotAI/HabitatMech/issues/2295
    : Epicuticular wax is the outer cuticular wax layer on a leaf surface, not a subtype
    of the whole leaf organ (PO:0025034); epithelial lining fluid is the respiratory
    mucosal surface liquid, not the entire human respiratory system; erythrocyte is
    a circulating red blood cell, not the entire human blood tissue; esophageal ulcer
    is a mucosal lesion/disease concept, not a subtype of the anatomical human esophagus;
    crustacean, piscine, avian, human and mammalian esophagus are tubular digestive
    organs, not subtypes of the entire foregut or digestive system; ethmoid bone is
    a cranial bone, not the human-scoped bone assemblage; mammalian and human Eustachian
    tube are pharyngotympanic tubes, not subtypes of the middle ear cavity; insect
    excretory system is an organ system, not a subtype of the whole insect-associated
    environment. Exclude only exact guarded GOLD source-path contributions, preserving
    independent genera and all source observations. Exact target habitatmech:GOLD.3a0549cbd8.
    Shared mapping endpoints #1398 remain separate."}]}'
  snapshot_sha256: 6f0d6c6b89b978e25cf87809f5f877300a5662b7f3c2d313461f702b804b9e32
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-05T15:25:14Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon terms cannot substitute
    for associated environments; parent_habitats must be strictly broader across all
    contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-05T15:25:14Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-05T15:25:14Z'
  support: supports
  summary: Seed generator produces identifier=habitatmech:GOLD.3a0549cbd8, grounding_status=NARROW,
    mapping_status=SEEDED, parent_habitats=["UBERON:8450002"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EGOLD
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV rows 1817
  accessed_at: '2026-11-05T15:25:14Z'
  support: supports
  summary: '[{"data": {"biosample_count": "0", "canonical_path": "Host-associated
    > Arthropoda: Insects > Excretory system", "depth": "3", "ecosystem": "Host-associated",
    "ecosystem_category": "Arthropoda: Insects", "ecosystem_subtype": "", "ecosystem_type":
    "Excretory system", "gold_node_count": "3", "gold_node_ids": "gold.ecosystem:7184|gold.ecosystem:7363|gold.ecosystem:7364",
    "leaf_label": "Excretory system", "organism_count": "0", "specific_ecosystem":
    "", "study_count": "0", "total_assertions": "0"}, "row": 1817}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 13546
  accessed_at: '2026-11-05T15:25:14Z'
  support: supports
  summary: '[{"data": {"definition": "An anatomical system that eliminates waste products
    that arise as a result of metabolic activity.", "deprecated": "", "directly_referenced":
    "FALSE", "label": "excretory system", "label_only": "FALSE", "ontology": "UBERON",
    "synonyms": "", "term_id": "UBERON:8450002"}, "row": 13546}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 11134,11878
  accessed_at: '2026-11-05T15:25:14Z'
  support: supports
  summary: '[{"data": {"object": "UBERON:8450002", "predicate": "rdfs:subClassOf",
    "subject": "UBERON:0001008"}, "row": 11134}, {"data": {"object": "UBERON:0000467",
    "predicate": "rdfs:subClassOf", "subject": "UBERON:8450002"}, "row": 11878}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EP2
  kind: record_content
  reference: data/habitats/host_associated/arthropoda_insects.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-11-05T15:25:14Z'
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
  locator: grep -rn -E 'excretory_system|habitatmech:GOLD.3a0549cbd8' reviews/structured/*/review.yaml
    curation/ history/
  accessed_at: '2026-11-05T15:25:14Z'
  support: context_only
  summary: Structured-review traversal verified no prior target review bundle exists
    for this record; curation and history tables were inspected for all matching rows.
  search_scope: curation, history, data/raw, and reviews/structured/*/review.yaml
    traversal at commit 215b23c90244e634e64f88fa2c1a2a3bb011880a.
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261105T051533Z-excretory_system-record/review.yaml
  locator: Every immutable Stage 4 baseline finding
  accessed_at: '2026-11-05T15:25:14Z'
  support: supports
  summary: Exact predecessor keys and findings reconciled; original inspected source
    scope preserved.
  snapshot_sha256: b1b07b969cca45dd179dcd3cce453e425f7a466540c1086d72996a71d688e8da
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_epicuticular_wax_to_excretory_system_review_repairs.py
  locator: Complete full-corpus counterfactual regression suite
  accessed_at: '2026-11-05T15:25:14Z'
  support: supports
  summary: 'Exactly fourteen records differ from the counterfactual baseline across
    Issues #2295 and #2296.'
  snapshot_sha256: 49996201e6fc34bd32f03bad90354d16c9efedb37f518d1020daf68a99e25afe
- evidence_id: EPARENTS
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: TSV line 14
  accessed_at: '2026-11-05T15:25:14Z'
  support: supports
  summary: '[[14, "habitatmech:GOLD.3a0549cbd8\tHost-associated > Arthropoda: Insects
    > Excretory system\thabitatmech:GOLD.dba2a83b95\tantigravity\t2026-11-05\tReview
    https://github.com/CultureBotAI/HabitatMech/issues/2295 : Epicuticular wax is
    the outer cuticular wax layer on a leaf surface, not a subtype of the whole leaf
    organ (PO:0025034); epithelial lining fluid is the respiratory mucosal surface
    liquid, not the entire human respiratory system; erythrocyte is a circulating
    red blood cell, not the entire human blood tissue; esophageal ulcer is a mucosal
    lesion/disease concept, not a subtype of the anatomical human esophagus; crustacean,
    piscine, avian, human and mammalian esophagus are tubular digestive organs, not
    subtypes of the entire foregut or digestive system; ethmoid bone is a cranial
    bone, not the human-scoped bone assemblage; mammalian and human Eustachian tube
    are pharyngotympanic tubes, not subtypes of the middle ear cavity; insect excretory
    system is an organ system, not a subtype of the whole insect-associated environment.
    Exclude only exact guarded GOLD source-path contributions, preserving independent
    genera and all source observations. Exact target habitatmech:GOLD.3a0549cbd8.
    Shared mapping endpoints #1398 remain separate."]]'
  snapshot_sha256: c1efdfa9188346f3292250e42e9f2315d2d49d8c6235e07733efda22039a5c1c
- evidence_id: EHIST_G1
  kind: record_content
  reference: history/other/gold_parent_exclusions/2026-11-05T151500Z-antigravity-229501.yaml
  locator: Complete curation session history event
  accessed_at: '2026-11-05T15:25:14Z'
  support: supports
  summary: 'Authorized curation event for Issue #2295 recorded and validated.'
  snapshot_sha256: 55bcac9e6231000d583bef7c9bff80f24c0a32b3e1c3ede0322550656637c0ec
assessments:
- assessment_id: A1
  area: schema
  topic: Native validity and reproduction after bounded remediation
  outcome: supported
  summary: Individual schema, strict 24-target validation, 864 history records, 14
    inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 73 causal
    overlays, 671 term requests, curation floor, site parity, and counterfactual regression
    tests passed.
  target_ids:
  - habitatmech:GOLD.3a0549cbd8
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
  summary: 'habitatmech:GOLD.3a0549cbd8: Excretory system; NARROW/SEEDED; parents
    ["UBERON:8450002"]. Removed the guarded GOLD whole-host context-parent contribution
    habitatmech:GOLD.0ef2e24505 (insect-associated environment) via curation/gold_parent_exclusions.tsv
    (#2295), preserving broader ontology parent UBERON:0001008 (renal system). Identity
    (habitatmech:GOLD.3a0549cbd8), native REVIEWED/NARROW status, and source observations
    are preserved. The global NARROW source-attestation endpoint finding (#1398) remains
    explicitly open.'
  target_ids:
  - habitatmech:GOLD.3a0549cbd8
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
  - habitatmech:GOLD.3a0549cbd8
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
    F1 is resolved under #2295; F2 remains open under corpus-wide issue #1398.'
  target_ids:
  - habitatmech:GOLD.3a0549cbd8
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
  - habitatmech:GOLD.3a0549cbd8
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
  issue_key: excretory-system-context-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Insect Excretory system retains whole-host insect-associated environment
    GOLD parent as a superclass
  description: 'Add an exclusion row in curation/gold_parent_exclusions.tsv for source
    identifier habitatmech:GOLD.3a0549cbd8 on GOLD path ''Host-associated > Arthropoda:
    Insects > Excretory system'' (exact target habitatmech:GOLD.3a0549cbd8) excluding
    parent_id habitatmech:GOLD.dba2a83b95 (insect-associated environment), preserving
    broader ontology parent UBERON:8450002 (excretory system).'
  target_ids:
  - habitatmech:GOLD.3a0549cbd8
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
  - https://github.com/CultureBotAI/HabitatMech/issues/2295
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261105T051533Z-excretory_system-record
    finding_id: F1
  disposition_reason: Excluded only the guarded GOLD whole-host context-parent contribution
    habitatmech:GOLD.0ef2e24505 (insect-associated environment) in curation/gold_parent_exclusions.tsv
    (#2295), preserving broader ontology parent UBERON:0001008 (renal system).
- finding_id: F2
  issue_key: excretory-system-mapping-endpoint-contract
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Narrow mapping predicate points to a minted source-path record
  description: 'Reconcile narrow-match source-attestation output with the endpoint
    contract tracked in Issue #1398 for habitatmech:GOLD.3a0549cbd8 (Host-associated
    > Arthropoda: Insects > Excretory system) and its broader ontology parent UBERON:8450002
    (excretory system).'
  target_ids:
  - habitatmech:GOLD.3a0549cbd8
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
    review_id: 20261105T051533Z-excretory_system-record
    finding_id: F2
  disposition_reason: The retained NARROW source/record endpoint mismatch (#1398)
    is unchanged; a guarded GOLD context-parent exclusion does not alter the global
    SourceAttestation.mapping_predicate endpoint contract.
actions:
- action_id: ACT2
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.3a0549cbd8
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
    contract tracked in Issue #1398 for habitatmech:GOLD.3a0549cbd8 (Host-associated
    > Arthropoda: Insects > Excretory system) and its broader ontology parent UBERON:8450002
    (excretory system). No repair is performed by this read-only review.'
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
- Configured label correspondence skipped 2,077 no-adapter pairs; this is not whole-corpus
  identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in
  this pre-save observation.
- 'iModulonDB is not applicable: the target has no gene, regulator or expression-module
  assertion. No paid research or scientific-status promotion was performed.'
notes:
- Saved against working-tree repairs atop main commit f0c857592f79534eeb3701824a58eb7b5fcefef3;
  all earlier saved bundles in reviews/structured/ remain byte-identical.
- Reconciles predecessor bundle 20261105T051533Z-excretory_system-record with exact
  issue_key and previous_occurrences lineage.
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261105T051533Z-excretory_system-record
  relationship: Exact predecessor; every finding explicitly reconciled.
```
