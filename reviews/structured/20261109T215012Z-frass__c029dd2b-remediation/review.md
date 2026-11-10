# Remediation review: frass__c029dd2b

- Review: 20261109T215012Z-frass__c029dd2b-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-09T21:40:00Z
- Finished UTC: 2026-11-09T21:50:12Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Removed the guarded GOLD anatomical-container Hindgut context-parent contribution habitatmech:GOLD.50722c7871 ('Host-associated &gt; Arthropoda: Insects &gt; Digestive system &gt; Hindgut') for source concept habitatmech:GOLD.67f3cde908 ('Host-associated &gt; Arthropoda: Insects &gt; Digestive system &gt; Hindgut &gt; Frass') via curation/gold_parent_exclusions.tsv (#2335), preserving broader excreta parent ENVO:00002003 (fecal material). Identity (habitatmech:GOLD.67f3cde908), native SEEDED/NARROW status, and the verbatim GOLD path attestation (0 ORGANISM assertions) are preserved. Predecessor finding F1 is resolved; the global NARROW source-attestation endpoint finding F2 (#1398) remains explicitly open.

## Scope And Provenance

Full current target assessment and explicit disposition of every baseline finding on data/habitats/host_associated/frass__c029dd2b.yaml after bounded Cycle 8 Stage 5 remediation.

Selection: One of thirteen repaired targets from the finger-through-free_living_state cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c82566b001f676eb0d3c9cc6c905f85a99b8bde.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.67f3cde908 | data/habitats/host_associated/frass__c029dd2b.yaml | generated | Frass |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.67f3cde908 | Completed 2026-11-09T21:48:00Z. No issues found against src/habitatmech/schema/habitatmech.yaml. |
| validate-strict | passed | True | habitatmech:GOLD.67f3cde908 | Completed 2026-11-09T21:48:05Z. 24 checked, 0 failed; target passed closed-schema validation. |
| validate-history | passed | True | habitatmech:GOLD.67f3cde908 | Completed 2026-11-09T21:48:10Z. No issues found; 879 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | habitatmech:GOLD.67f3cde908 | Completed 2026-11-09T21:48:15Z. 14 inventory files and 2 GOLD export files verified. |
| verify-corpus | passed | True | habitatmech:GOLD.67f3cde908 | Completed 2026-11-09T21:48:25Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | habitatmech:GOLD.67f3cde908 | Completed 2026-11-09T21:48:30Z. 103 causal-graph curations and target records validated. |
| term-requests-check | passed | True | habitatmech:GOLD.67f3cde908 | Completed 2026-11-09T21:48:35Z. term-request table is current (676 terms). |
| validate-products | passed | True | habitatmech:GOLD.67f3cde908 | Completed 2026-11-09T21:48:45Z. 24 records, 0 label drift findings. |
| pytest counterfactual review repairs | passed | True | habitatmech:GOLD.67f3cde908 | Completed 2026-11-09T21:49:00Z. 2 passed; exact 13-record counterfactual diff verified. |
| curation-floor | passed | True | habitatmech:GOLD.67f3cde908 | Completed 2026-11-09T21:49:05Z. Floor satisfied across all 13 metrics. |
| render-check | passed | True | habitatmech:GOLD.67f3cde908 | Completed 2026-11-09T21:49:30Z. rendered 3209 habitat pages, 757 redirect stubs, 8 categories, 701 term requests; pages/ is in step with the corpus. |

## Scientific And Domain Assessments

### Native validity and reproduction after bounded remediation

schema: supported. Targets: habitatmech:GOLD.67f3cde908.

Individual schema, strict 24-target validation, 879 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 103 causal overlays, 676 term requests, curation floor, site parity, and counterfactual regression tests passed.

### Identity, definition, hierarchy and aliases

identity: concern. Targets: habitatmech:GOLD.67f3cde908.

habitatmech:GOLD.67f3cde908: Frass; NARROW/SEEDED; parents ["ENVO:00002003"]. Removed the guarded GOLD anatomical-container Hindgut context-parent contribution habitatmech:GOLD.50722c7871 ('Host-associated &gt; Arthropoda: Insects &gt; Digestive system &gt; Hindgut') for source concept habitatmech:GOLD.67f3cde908 ('Host-associated &gt; Arthropoda: Insects &gt; Digestive system &gt; Hindgut &gt; Frass') via curation/gold_parent_exclusions.tsv (#2335), preserving broader excreta parent ENVO:00002003 (fecal material). Identity (habitatmech:GOLD.67f3cde908), native SEEDED/NARROW status, and the verbatim GOLD path attestation (0 ORGANISM assertions) are preserved. Predecessor finding F1 is resolved; the global NARROW source-attestation endpoint finding F2 (#1398) remains explicitly open.

### Source counts and retained ranking

quantity: supported. Targets: habitatmech:GOLD.67f3cde908.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"count": 0, "source": "GOLD", "unit": null}]. Zero counts are omitted; unrelated parent counts are not combined.

### Predecessor finding reconciliation

representation: concern. Targets: habitatmech:GOLD.67f3cde908.

Every predecessor finding preserves its stable issue_key and exact lineage. F1 is resolved under #2335; F2 remains open under corpus-wide issue #1398.

### Parameters, mechanisms and native status

completeness: supported. Targets: habitatmech:GOLD.67f3cde908.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce SEEDED / NARROW; this read-only review does not mutate generated records.

## Findings

### F1: Insect Frass (habitatmech:GOLD.67f3cde908) asserts anatomical organ habitatmech:GOLD.50722c7871 (Hindgut) as a broader habitat parent

major / resolved / confirmed; issue key: frass--c029dd2b-context-parent.

Insect frass (excreta) is egested digestive waste material (a subtype of ENVO:00002003 fecal material), not an anatomical subtype (is_a) of the Hindgut organ ('Host-associated &gt; Arthropoda: Insects &gt; Digestive system &gt; Hindgut', habitatmech:GOLD.50722c7871). Add a guarded exclusion row in curation/gold_parent_exclusions.tsv for habitatmech:GOLD.67f3cde908 ('Host-associated &gt; Arthropoda: Insects &gt; Digestive system &gt; Hindgut &gt; Frass') excluding expected_parent_id=habitatmech:GOLD.50722c7871 while retaining ENVO:00002003 (fecal material).

Disposition: Excluded only the guarded GOLD anatomical-container Hindgut context-parent contribution habitatmech:GOLD.50722c7871 (Hindgut) for habitatmech:GOLD.67f3cde908 in curation/gold_parent_exclusions.tsv (#2335), preserving broader excreta parent ENVO:00002003 (fecal material).

### F2: Narrow mapping predicate points to a minted source-path record

major / open / confirmed; issue key: frass--c029dd2b-mapping-endpoint-contract.

Reconcile narrow-match source-attestation output with the endpoint contract tracked in Issue #1398 for habitatmech:GOLD.67f3cde908 ('Host-associated &gt; Arthropoda: Insects &gt; Digestive system &gt; Hindgut &gt; Frass') when the broader ontology target is ENVO:00002003 (fecal material).

Disposition: The retained NARROW source/record endpoint mismatch (#1398) is unchanged; a guarded GOLD context-parent exclusion does not alter the global SourceAttestation.mapping_predicate endpoint contract.

## Recommended Actions And Acceptance Checks

### ACT2

Reconcile narrow-match source-attestation output with the endpoint contract tracked in Issue #1398 for habitatmech:GOLD.67f3cde908 ('Host-associated &gt; Arthropoda: Insects &gt; Digestive system &gt; Hindgut &gt; Frass') when the broader ontology target is ENVO:00002003 (fecal material).

- Verify mapping endpoint semantics across ambiguous-leaf narrow-match records once #1398 is resolved.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/frass__c029dd2b.yaml; Entire YAML | supports | {"identifier": "habitatmech:GOLD.67f3cde908", "label": "Frass", "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats": ["ENVO:00002003"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:7395", "source_label": "Frass", "source_path": "Host-associated &gt; Arthropoda: Insects &gt; Digestive system &gt; Hindgut &gt; Frass", "mapping_predicate": "skos:narrowMatch"}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NARROW."}, {"timestamp": "2026-11-09T00:00:00Z", "curator": "antigravity", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.50722c7871 for habitatmech:GOLD.67f3cde908 (Host-associated &gt; Arthropoda: Insects &gt; Digestive system &gt; Hindgut &gt; Frass). Review https://github.com/CultureBotAI/HabitatMech/issues/2335 : Piscine, mammalian, insect, myriapod, and crustacean foregut are anterior digestive-tract subdivisions (part_of), not subtypes (is_a) of the whole host-scoped digestive system; mammalian forestomach (BTO:0000480) is an anterior stomach compartment (part_of), not a subtype of the whole mammalian stomach; insect larval and hindgut frass are egested fecal waste materials (ENVO:00002003), not anatomical subtypes of the gut or hindgut organ. Exclude only exact guarded GOLD source-path contributions, preserving independent genera and all source observations. Exact target habitatmech:GOLD.67f3cde908. Shared mapping endpoints #1398 remain separate."}]} |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon, organism-form, and subcellular organelle terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=habitatmech:GOLD.67f3cde908, grounding_status=NARROW, mapping_status=SEEDED, parent_habitats=["ENVO:00002003"], xrefs=[]. |
| EGOLD | data/raw/gold_ecosystem_paths.tsv; TSV rows 1802 | supports | [{"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Arthropoda: Insects &gt; Digestive system &gt; Hindgut &gt; Frass", "depth": "5", "ecosystem": "Host-associated", "ecosystem_category": "Arthropoda: Insects", "ecosystem_subtype": "Hindgut", "ecosystem_type": "Digestive system", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:7395", "leaf_label": "Frass", "organism_count": "0", "specific_ecosystem": "Frass", "study_count": "0", "total_assertions": "0"}, "row": 1802}] |
| EONT | data/raw/ontology_terms.tsv; TSV rows 7161 | supports | [{"data": {"definition": "An excreta material which is composed primarily of feces, an excreta consisting of waste products expelled from an animal's digestive tract through the anus (or cloaca) during defecation.", "deprecated": "", "directly_referenced": "FALSE", "label": "fecal material", "label_only": "FALSE", "ontology": "ENVO", "synonyms": "droppings&#124;faeces material&#124;feces material&#124;frass&#124;pellet", "term_id": "ENVO:00002003"}, "row": 7161}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 5265 | supports | [{"data": {"object": "ENVO:02000022", "predicate": "rdfs:subClassOf", "subject": "ENVO:00002003"}, "row": 5265}] |
| EP2 | data/habitats/host_associated/hindgut__f414b618.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"identifier": "habitatmech:GOLD.50722c7871", "label": "Hindgut", "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0001046", "habitatmech:GOLD.d7cff86ce8"]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'frass__c029dd2b&#124;habitatmech:GOLD.67f3cde908' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal located Stage 4 predecessor bundle 20261109T181032Z-frass__c029dd2b-record (linked via EPREV and related_reviews) and checked related cohort and ancestor reviews for reconciliation. |
| EPARENTS | curation/gold_parent_exclusions.tsv; TSV line 9 | supports | [[9, "habitatmech:GOLD.67f3cde908\tHost-associated &gt; Arthropoda: Insects &gt; Digestive system &gt; Hindgut &gt; Frass\thabitatmech:GOLD.50722c7871\tantigravity\t2026-11-09\tReview https://github.com/CultureBotAI/HabitatMech/issues/2335 : Piscine, mammalian, insect, myriapod, and crustacean foregut are anterior digestive-tract subdivisions (part_of), not subtypes (is_a) of the whole host-scoped digestive system; mammalian forestomach (BTO:0000480) is an anterior stomach compartment (part_of), not a subtype of the whole mammalian stomach; insect larval and hindgut frass are egested fecal waste materials (ENVO:00002003), not anatomical subtypes of the gut or hindgut organ. Exclude only exact guarded GOLD source-path contributions, preserving independent genera and all source observations. Exact target habitatmech:GOLD.67f3cde908. Shared mapping endpoints #1398 remain separate."]] |
| EPREV | reviews/structured/20261109T181032Z-frass__c029dd2b-record/review.yaml; Every immutable Stage 4 baseline finding | supports | Exact predecessor keys and findings reconciled; original inspected source scope preserved. |
| ETEST | tests/test_finger_to_free_living_state_review_repairs.py; Complete full-corpus counterfactual regression suite | supports | Exactly thirteen records differ from the counterfactual baseline across Issues #2334, #2335, and #2336. |
| EHIST_G2 | history/other/gold_parent_exclusions/2026-11-09T214510Z-antigravity-233501.yaml; Complete curation session history event | supports | Authorized curation event for Issue #2335 recorded and validated. |

## Limits And Additional Notes

- Only the cited repository inputs, ontology terms, and source inventories were inspected; original specimen-level support for every upstream source assertion was not exhaustively reconstructed.
- Source counts, PREGO scores, and ranks are not prevalence, viability, mechanism, or characteristic presence.
- Configured label correspondence skipped 2,094 no-adapter pairs; this is not whole-corpus identifier certification.
- Read-only review: no curation table, generated habitat YAML, status, or history record was modified.
- Saved against working-tree repairs atop main commit 7c82566b001f676eb0d3c9cc6c905f85a99b8bde; all earlier saved bundles in reviews/structured/ remain byte-identical.
- Reconciles predecessor bundle 20261109T181032Z-frass__c029dd2b-record with exact issue_key and previous_occurrences lineage.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T215012Z-frass__c029dd2b-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: frass__c029dd2b'
started_at: '2026-11-09T21:40:00Z'
finished_at: '2026-11-09T21:50:12Z'
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
summary: 'Removed the guarded GOLD anatomical-container Hindgut context-parent contribution
  habitatmech:GOLD.50722c7871 (''Host-associated > Arthropoda: Insects > Digestive
  system > Hindgut'') for source concept habitatmech:GOLD.67f3cde908 (''Host-associated
  > Arthropoda: Insects > Digestive system > Hindgut > Frass'') via curation/gold_parent_exclusions.tsv
  (#2335), preserving broader excreta parent ENVO:00002003 (fecal material). Identity
  (habitatmech:GOLD.67f3cde908), native SEEDED/NARROW status, and the verbatim GOLD
  path attestation (0 ORGANISM assertions) are preserved. Predecessor finding F1 is
  resolved; the global NARROW source-attestation endpoint finding F2 (#1398) remains
  explicitly open.'
source:
  git_revision: 7c82566b001f676eb0d3c9cc6c905f85a99b8bde
  state: working_tree
  inputs:
  - path: curation/decisions.tsv
    sha256: 8e0c9ea50c453b9b0eb86e9a6cf246dbc188714ec7a8cc37b2918d5373e6d2ae
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 84e5214713a21033312eb9c512fe38f44865662f934a4e679d45e827b16ff780
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 21c90040f7616f5ecc103716597d65b899f433eee24e880ac3f2fd802ff624c6
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: c1207270bb0ae2031e42de6cb8220b20f98886f65e40d48793bfd7e9d757d83a
    role: context
  - path: curation/term_requests.tsv
    sha256: 3703ae74d7565abdfb5a1fab47718b05c4fd02447b4ed60bbeb3bde65e1d8792
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: 779e0cf7e829e3ec74b5a898b6ed70d54d930b7da726c1611225902c00915388
    role: context
  - path: data/habitats/host_associated/frass__c029dd2b.yaml
    sha256: 2123796310cbaa733b6274a2ebdc88a966d5c4433c1038dfd859391263c93aaf
    role: target
  - path: data/habitats/host_associated/hindgut__f414b618.yaml
    sha256: d9e6476df58f7b510f568e8c374b1f6173570da79653f246e76f023b0cb5fd0e
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
  - path: history/other/gold_parent_exclusions/2026-11-09T214510Z-antigravity-233501.yaml
    sha256: f380b100705f7c7ba6f050c75996b1c13daf8d61cccb656dbd323034751b959a
    role: context
  - path: reviews/structured/20261109T181032Z-frass__c029dd2b-record/review.yaml
    sha256: 3b60df150b1a3ddc8aeadb036b17a895800925d6b263933c3ce0dd753657b733
    role: context
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
    role: context
  - path: src/habitatmech/seed.py
    sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
    role: context
  - path: tests/test_finger_to_free_living_state_review_repairs.py
    sha256: 495a506d77d0f3c2484e16b510c233a7c8b108ae96cba6b6346252c3a9d01bdb
    role: context
targets:
- target_id: habitatmech:GOLD.67f3cde908
  path: data/habitats/host_associated/frass__c029dd2b.yaml
  label: Frass
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
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
scope:
  description: Full current target assessment and explicit disposition of every baseline
    finding on data/habitats/host_associated/frass__c029dd2b.yaml after bounded Cycle
    8 Stage 5 remediation.
  selection: One of thirteen repaired targets from the finger-through-free_living_state
    cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.67f3cde908
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
    --target-class HabitatRecord data/habitats/host_associated/frass__c029dd2b.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.67f3cde908
  summary: Completed 2026-11-09T21:48:00Z. No issues found against src/habitatmech/schema/habitatmech.yaml.
  scope_note: Individual schema; strict command covers the 24 named cohort targets;
    other documented gates have full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/habitats/host_associated/finger.yaml
    data/habitats/host_associated/fingernail.yaml data/habitats/host_associated/fish.yaml
    data/habitats/host_associated/fistula.yaml data/habitats/host_associated/flagellate.yaml
    data/habitats/host_associated/flagellum.yaml data/habitats/host_associated/flea.yaml
    data/habitats/host_associated/flesh.yaml data/habitats/host_associated/floc.yaml
    data/habitats/host_associated/flower.yaml data/habitats/host_associated/Flower_head.yaml
    data/habitats/host_associated/fluid.yaml data/habitats/host_associated/fluid__8fb24b60.yaml
    data/habitats/host_associated/fly.yaml data/habitats/host_associated/fomite.yaml
    data/habitats/host_associated/foot.yaml data/habitats/host_associated/foregut.yaml
    data/habitats/host_associated/foregut__6bc8c43a.yaml data/habitats/host_associated/foregut__c14450a8.yaml
    data/habitats/host_associated/foregut__ce63e8ab.yaml data/habitats/host_associated/foregut__d14a54ae.yaml
    data/habitats/host_associated/foregut__ee6a8f74.yaml data/habitats/host_associated/foreleg.yaml
    data/habitats/host_associated/forestomach.yaml --out .temp/c8s4_24_strict.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.67f3cde908
  summary: Completed 2026-11-09T21:48:05Z. 24 checked, 0 failed; target passed closed-schema
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
  - habitatmech:GOLD.67f3cde908
  summary: Completed 2026-11-09T21:48:10Z. No issues found; 879 history record(s)
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
  - habitatmech:GOLD.67f3cde908
  summary: Completed 2026-11-09T21:48:15Z. 14 inventory files and 2 GOLD export files
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
  - habitatmech:GOLD.67f3cde908
  summary: 'Completed 2026-11-09T21:48:25Z. expected 3209 records, found 3209 on disk;
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
  - habitatmech:GOLD.67f3cde908
  summary: Completed 2026-11-09T21:48:30Z. 103 causal-graph curations and target records
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
  - habitatmech:GOLD.67f3cde908
  summary: Completed 2026-11-09T21:48:35Z. term-request table is current (676 terms).
  scope_note: Full-corpus term-request table currency check.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.67f3cde908
  summary: Completed 2026-11-09T21:48:45Z. 24 records, 0 label drift findings.
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
- check_id: C9
  name: pytest counterfactual review repairs
  status: passed
  required: true
  command: .venv/bin/python -m pytest tests/test_finger_to_free_living_state_review_repairs.py
    -q --no-cov
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.67f3cde908
  summary: Completed 2026-11-09T21:49:00Z. 2 passed; exact 13-record counterfactual
    diff verified.
  scope_note: 'Full-corpus counterfactual regression test for Issues #2334, #2335,
    and #2336.'
- check_id: C10
  name: curation-floor
  status: passed
  required: true
  command: .venv/bin/python scripts/check_curation_floor.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.67f3cde908
  summary: Completed 2026-11-09T21:49:05Z. Floor satisfied across all 13 metrics.
  scope_note: Full-corpus curation floor ratchets.
- check_id: C11
  name: render-check
  status: passed
  required: true
  command: .venv/bin/python scripts/render_pages.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.67f3cde908
  summary: Completed 2026-11-09T21:49:30Z. rendered 3209 habitat pages, 757 redirect
    stubs, 8 categories, 701 term requests; pages/ is in step with the corpus.
  scope_note: Full-corpus static site parity check.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/frass__c029dd2b.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T21:50:12Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.67f3cde908", "label": "Frass", "grounding_status":
    "NARROW", "mapping_status": "SEEDED", "parent_habitats": ["ENVO:00002003"], "source_attestations":
    [{"source": "GOLD", "source_id": "gold.ecosystem:7395", "source_label": "Frass",
    "source_path": "Host-associated > Arthropoda: Insects > Digestive system > Hindgut
    > Frass", "mapping_predicate": "skos:narrowMatch"}], "curation_history": [{"timestamp":
    "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES",
    "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NARROW."},
    {"timestamp": "2026-11-09T00:00:00Z", "curator": "antigravity", "action": "SOURCE_PARENT_EXCLUDED",
    "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.50722c7871
    for habitatmech:GOLD.67f3cde908 (Host-associated > Arthropoda: Insects > Digestive
    system > Hindgut > Frass). Review https://github.com/CultureBotAI/HabitatMech/issues/2335
    : Piscine, mammalian, insect, myriapod, and crustacean foregut are anterior digestive-tract
    subdivisions (part_of), not subtypes (is_a) of the whole host-scoped digestive
    system; mammalian forestomach (BTO:0000480) is an anterior stomach compartment
    (part_of), not a subtype of the whole mammalian stomach; insect larval and hindgut
    frass are egested fecal waste materials (ENVO:00002003), not anatomical subtypes
    of the gut or hindgut organ. Exclude only exact guarded GOLD source-path contributions,
    preserving independent genera and all source observations. Exact target habitatmech:GOLD.67f3cde908.
    Shared mapping endpoints #1398 remain separate."}]}'
  snapshot_sha256: 2123796310cbaa733b6274a2ebdc88a966d5c4433c1038dfd859391263c93aaf
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-09T21:50:12Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon, organism-form,
    and subcellular organelle terms cannot substitute for associated environments;
    parent_habitats must be strictly broader across all contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-09T21:50:12Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-09T21:50:12Z'
  support: supports
  summary: Seed generator produces identifier=habitatmech:GOLD.67f3cde908, grounding_status=NARROW,
    mapping_status=SEEDED, parent_habitats=["ENVO:00002003"], xrefs=[].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EGOLD
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV rows 1802
  accessed_at: '2026-11-09T21:50:12Z'
  support: supports
  summary: '[{"data": {"biosample_count": "0", "canonical_path": "Host-associated
    > Arthropoda: Insects > Digestive system > Hindgut > Frass", "depth": "5", "ecosystem":
    "Host-associated", "ecosystem_category": "Arthropoda: Insects", "ecosystem_subtype":
    "Hindgut", "ecosystem_type": "Digestive system", "gold_node_count": "1", "gold_node_ids":
    "gold.ecosystem:7395", "leaf_label": "Frass", "organism_count": "0", "specific_ecosystem":
    "Frass", "study_count": "0", "total_assertions": "0"}, "row": 1802}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 7161
  accessed_at: '2026-11-09T21:50:12Z'
  support: supports
  summary: '[{"data": {"definition": "An excreta material which is composed primarily
    of feces, an excreta consisting of waste products expelled from an animal''s digestive
    tract through the anus (or cloaca) during defecation.", "deprecated": "", "directly_referenced":
    "FALSE", "label": "fecal material", "label_only": "FALSE", "ontology": "ENVO",
    "synonyms": "droppings|faeces material|feces material|frass|pellet", "term_id":
    "ENVO:00002003"}, "row": 7161}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 5265
  accessed_at: '2026-11-09T21:50:12Z'
  support: supports
  summary: '[{"data": {"object": "ENVO:02000022", "predicate": "rdfs:subClassOf",
    "subject": "ENVO:00002003"}, "row": 5265}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EP2
  kind: record_content
  reference: data/habitats/host_associated/hindgut__f414b618.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-11-09T21:50:12Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.50722c7871", "label": "Hindgut", "grounding_status":
    "NARROW", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0001046", "habitatmech:GOLD.d7cff86ce8"]}'
  snapshot_sha256: d9e6476df58f7b510f568e8c374b1f6173570da79653f246e76f023b0cb5fd0e
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'frass__c029dd2b|habitatmech:GOLD.67f3cde908' reviews/structured/*/review.yaml
    curation/ history/
  accessed_at: '2026-11-09T21:50:12Z'
  support: context_only
  summary: Structured-review traversal located Stage 4 predecessor bundle 20261109T181032Z-frass__c029dd2b-record
    (linked via EPREV and related_reviews) and checked related cohort and ancestor
    reviews for reconciliation.
  search_scope: curation, history, data/raw, and reviews/structured/*/review.yaml
    traversal at commit 7c82566b001f676eb0d3c9cc6c905f85a99b8bde.
- evidence_id: EPARENTS
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: TSV line 9
  accessed_at: '2026-11-09T21:50:12Z'
  support: supports
  summary: '[[9, "habitatmech:GOLD.67f3cde908\tHost-associated > Arthropoda: Insects
    > Digestive system > Hindgut > Frass\thabitatmech:GOLD.50722c7871\tantigravity\t2026-11-09\tReview
    https://github.com/CultureBotAI/HabitatMech/issues/2335 : Piscine, mammalian,
    insect, myriapod, and crustacean foregut are anterior digestive-tract subdivisions
    (part_of), not subtypes (is_a) of the whole host-scoped digestive system; mammalian
    forestomach (BTO:0000480) is an anterior stomach compartment (part_of), not a
    subtype of the whole mammalian stomach; insect larval and hindgut frass are egested
    fecal waste materials (ENVO:00002003), not anatomical subtypes of the gut or hindgut
    organ. Exclude only exact guarded GOLD source-path contributions, preserving independent
    genera and all source observations. Exact target habitatmech:GOLD.67f3cde908.
    Shared mapping endpoints #1398 remain separate."]]'
  snapshot_sha256: 21c90040f7616f5ecc103716597d65b899f433eee24e880ac3f2fd802ff624c6
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261109T181032Z-frass__c029dd2b-record/review.yaml
  locator: Every immutable Stage 4 baseline finding
  accessed_at: '2026-11-09T21:50:12Z'
  support: supports
  summary: Exact predecessor keys and findings reconciled; original inspected source
    scope preserved.
  snapshot_sha256: 3b60df150b1a3ddc8aeadb036b17a895800925d6b263933c3ce0dd753657b733
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_finger_to_free_living_state_review_repairs.py
  locator: Complete full-corpus counterfactual regression suite
  accessed_at: '2026-11-09T21:50:12Z'
  support: supports
  summary: 'Exactly thirteen records differ from the counterfactual baseline across
    Issues #2334, #2335, and #2336.'
  snapshot_sha256: 495a506d77d0f3c2484e16b510c233a7c8b108ae96cba6b6346252c3a9d01bdb
- evidence_id: EHIST_G2
  kind: record_content
  reference: history/other/gold_parent_exclusions/2026-11-09T214510Z-antigravity-233501.yaml
  locator: Complete curation session history event
  accessed_at: '2026-11-09T21:50:12Z'
  support: supports
  summary: 'Authorized curation event for Issue #2335 recorded and validated.'
  snapshot_sha256: f380b100705f7c7ba6f050c75996b1c13daf8d61cccb656dbd323034751b959a
assessments:
- assessment_id: A1
  area: schema
  topic: Native validity and reproduction after bounded remediation
  outcome: supported
  summary: Individual schema, strict 24-target validation, 879 history records, 14
    inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 103 causal
    overlays, 676 term requests, curation floor, site parity, and counterfactual regression
    tests passed.
  target_ids:
  - habitatmech:GOLD.67f3cde908
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
  - EPARENTS
  - EPREV
  - ETEST
  - EHIST_G2
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: concern
  summary: 'habitatmech:GOLD.67f3cde908: Frass; NARROW/SEEDED; parents ["ENVO:00002003"].
    Removed the guarded GOLD anatomical-container Hindgut context-parent contribution
    habitatmech:GOLD.50722c7871 (''Host-associated > Arthropoda: Insects > Digestive
    system > Hindgut'') for source concept habitatmech:GOLD.67f3cde908 (''Host-associated
    > Arthropoda: Insects > Digestive system > Hindgut > Frass'') via curation/gold_parent_exclusions.tsv
    (#2335), preserving broader excreta parent ENVO:00002003 (fecal material). Identity
    (habitatmech:GOLD.67f3cde908), native SEEDED/NARROW status, and the verbatim GOLD
    path attestation (0 ORGANISM assertions) are preserved. Predecessor finding F1
    is resolved; the global NARROW source-attestation endpoint finding F2 (#1398)
    remains explicitly open.'
  target_ids:
  - habitatmech:GOLD.67f3cde908
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
  - EPARENTS
  - EPREV
  - ETEST
  - EHIST_G2
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks,
    and pools: [{"count": 0, "source": "GOLD", "unit": null}]. Zero counts are omitted;
    unrelated parent counts are not combined.'
  target_ids:
  - habitatmech:GOLD.67f3cde908
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
  - EPARENTS
  - EPREV
  - ETEST
  - EHIST_G2
- assessment_id: A4
  area: representation
  topic: Predecessor finding reconciliation
  outcome: concern
  summary: 'Every predecessor finding preserves its stable issue_key and exact lineage.
    F1 is resolved under #2335; F2 remains open under corpus-wide issue #1398.'
  target_ids:
  - habitatmech:GOLD.67f3cde908
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
  - EPARENTS
  - EPREV
  - ETEST
  - EHIST_G2
- assessment_id: A5
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: Missing optional parameters/graphs are not evidence deficits. Full source
    decisions and executed routes reproduce SEEDED / NARROW; this read-only review
    does not mutate generated records.
  target_ids:
  - habitatmech:GOLD.67f3cde908
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
  - EPARENTS
  - EPREV
  - ETEST
  - EHIST_G2
findings:
- finding_id: F1
  issue_key: frass--c029dd2b-context-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Insect Frass (habitatmech:GOLD.67f3cde908) asserts anatomical organ habitatmech:GOLD.50722c7871
    (Hindgut) as a broader habitat parent
  description: 'Insect frass (excreta) is egested digestive waste material (a subtype
    of ENVO:00002003 fecal material), not an anatomical subtype (is_a) of the Hindgut
    organ (''Host-associated > Arthropoda: Insects > Digestive system > Hindgut'',
    habitatmech:GOLD.50722c7871). Add a guarded exclusion row in curation/gold_parent_exclusions.tsv
    for habitatmech:GOLD.67f3cde908 (''Host-associated > Arthropoda: Insects > Digestive
    system > Hindgut > Frass'') excluding expected_parent_id=habitatmech:GOLD.50722c7871
    while retaining ENVO:00002003 (fecal material).'
  target_ids:
  - habitatmech:GOLD.67f3cde908
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
  - EPARENTS
  - EPREV
  - ETEST
  - EHIST_G2
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or representation claim; deterministic
    validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2335
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261109T181032Z-frass__c029dd2b-record
    finding_id: F1
  disposition_reason: Excluded only the guarded GOLD anatomical-container Hindgut
    context-parent contribution habitatmech:GOLD.50722c7871 (Hindgut) for habitatmech:GOLD.67f3cde908
    in curation/gold_parent_exclusions.tsv (#2335), preserving broader excreta parent
    ENVO:00002003 (fecal material).
- finding_id: F2
  issue_key: frass--c029dd2b-mapping-endpoint-contract
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Narrow mapping predicate points to a minted source-path record
  description: 'Reconcile narrow-match source-attestation output with the endpoint
    contract tracked in Issue #1398 for habitatmech:GOLD.67f3cde908 (''Host-associated
    > Arthropoda: Insects > Digestive system > Hindgut > Frass'') when the broader
    ontology target is ENVO:00002003 (fecal material).'
  target_ids:
  - habitatmech:GOLD.67f3cde908
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
  - EPARENTS
  - EPREV
  - ETEST
  - EHIST_G2
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
    review_id: 20261109T181032Z-frass__c029dd2b-record
    finding_id: F2
  disposition_reason: The retained NARROW source/record endpoint mismatch (#1398)
    is unchanged; a guarded GOLD context-parent exclusion does not alter the global
    SourceAttestation.mapping_predicate endpoint contract.
actions:
- action_id: ACT2
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.67f3cde908
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
    contract tracked in Issue #1398 for habitatmech:GOLD.67f3cde908 (''Host-associated
    > Arthropoda: Insects > Digestive system > Hindgut > Frass'') when the broader
    ontology target is ENVO:00002003 (fecal material).'
  generator: 'Coordinated schema/seeder update tracked under Issue #1398.'
  acceptance_checks:
  - 'Verify mapping endpoint semantics across ambiguous-leaf narrow-match records
    once #1398 is resolved.'
limitations:
- Only the cited repository inputs, ontology terms, and source inventories were inspected;
  original specimen-level support for every upstream source assertion was not exhaustively
  reconstructed.
- Source counts, PREGO scores, and ranks are not prevalence, viability, mechanism,
  or characteristic presence.
- Configured label correspondence skipped 2,094 no-adapter pairs; this is not whole-corpus
  identifier certification.
- 'Read-only review: no curation table, generated habitat YAML, status, or history
  record was modified.'
notes:
- Saved against working-tree repairs atop main commit 7c82566b001f676eb0d3c9cc6c905f85a99b8bde;
  all earlier saved bundles in reviews/structured/ remain byte-identical.
- Reconciles predecessor bundle 20261109T181032Z-frass__c029dd2b-record with exact
  issue_key and previous_occurrences lineage.
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261109T181032Z-frass__c029dd2b-record
  relationship: Exact predecessor; every finding explicitly reconciled.
```
