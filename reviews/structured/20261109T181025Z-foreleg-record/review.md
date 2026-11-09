# Record review: foreleg (BTO:0006514)

- Review: 20261109T181025Z-foreleg-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-09T18:08:00Z
- Finished UTC: 2026-11-09T18:10:25Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The GOLD-attested record BTO:0006514 (foreleg, 'A front leg.', EXACT/REVIEWED) grounds GOLD path 'Host-associated &gt; Mammals &gt; Lymphatic system &gt; Lymph nodes &gt; Forelegs' (habitatmech:GOLD.80220dc4d4) to the whole front limb BTO:0006514 rather than a mammalian forelimb lymph node (parallel to hind_legs.yaml habitatmech:GOLD.ca4882ca81), causing BTO:0006514 to assert both BTO:0000721 (leg) and UBERON:0000029 (lymph node) in parent_habitats.

## Scope And Provenance

Scientific assessment of one exact generated target (data/habitats/host_associated/foreleg.yaml) at captured main revision 19d3ccb65e6b5128b9b0a5ae39cb509bf3f2bf39.

Selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/ path order (finger through free_living_state); this bundle assesses its single resolved identifier and source path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 19d3ccb65e6b5128b9b0a5ae39cb509bf3f2bf39.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0006514 | data/habitats/host_associated/foreleg.yaml | generated | foreleg |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0006514 | Completed 2026-11-09T18:08:48Z. No issues found. |
| validate-strict | passed | True | BTO:0006514 | Completed 2026-11-09T18:08:54Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | BTO:0006514 | Completed 2026-11-09T18:09:00Z. No issues found; 876 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | BTO:0006514 | Completed 2026-11-09T18:09:01Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | BTO:0006514 | Completed 2026-11-09T18:09:16Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | BTO:0006514 | Completed 2026-11-09T18:09:22Z. validated 103 causal-graph curation file(s) with 103 graph(s). |
| term-requests-check | passed | True | BTO:0006514 | Completed 2026-11-09T18:09:36Z. term-request table is current (674 terms). |
| validate-products | passed | True | BTO:0006514 | Completed 2026-11-09T18:10:17Z. OK_CANONICAL: 1213, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2094. All id&lt;-&gt;label pairs correspond. |

## Scientific And Domain Assessments

### Native validity and reproduction

schema: supported. Targets: BTO:0006514.

Individual schema, strict 24-target validation, 876 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 103 causal overlays, and 674 term requests passed.

### Identity, definition, hierarchy and aliases

identity: concern. Targets: BTO:0006514.

The GOLD-attested record BTO:0006514 (foreleg, 'A front leg.', EXACT/REVIEWED) grounds GOLD path 'Host-associated &gt; Mammals &gt; Lymphatic system &gt; Lymph nodes &gt; Forelegs' (habitatmech:GOLD.80220dc4d4) to the whole front limb BTO:0006514 rather than a mammalian forelimb lymph node (parallel to hind_legs.yaml habitatmech:GOLD.ca4882ca81), causing BTO:0006514 to assert both BTO:0000721 (leg) and UBERON:0000029 (lymph node) in parent_habitats.

### Source counts and retained ranking

quantity: supported. Targets: BTO:0006514.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"count": 0, "source": "GOLD", "unit": null}]. Zero counts are omitted; unrelated parent counts are not combined.

### Parameters, mechanisms and native status

completeness: supported. Targets: BTO:0006514.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce REVIEWED / EXACT; this read-only review does not mutate generated records.

## Findings

### F1: Mammalian forelimb lymph node path is grounded to whole limb BTO:0006514 (foreleg)

blocker / open / confirmed; issue key: foreleg-lymph-node-identity.

GOLD path 'Host-associated &gt; Mammals &gt; Lymphatic system &gt; Lymph nodes &gt; Forelegs' (habitatmech:GOLD.80220dc4d4) denotes a lymph node of the mammalian forelimb (such as the axillary or superficial cervical lymph node, parallel to already-curated sibling hind_legs.yaml habitatmech:GOLD.ca4882ca81 'mammalian hindlimb lymph node'), not the entire front leg (BTO:0006514 foreleg, 'A front leg.'). Replace the GROUND decision on habitatmech:GOLD.80220dc4d4 in curation/decisions.tsv with CONFIRM_UNGROUNDED (object_id=UBERON:0000029, object_label=lymph node, relation=parent), author a curated definition for 'mammalian forelimb lymph node' under UBERON:0000029 in curation/term_requests.tsv, exclude displaced source label 'Forelegs' in curation/definition_source_label_exclusions.tsv, and update data/habitats/PATHS.tsv.

### F2: Grounding forelimb lymph node to BTO:0006514 (foreleg) asserts UBERON:0000029 (lymph node) as a parent of foreleg

major / open / confirmed; issue key: foreleg-lymph-node-parent-collision.

Because habitatmech:GOLD.80220dc4d4 ('Host-associated &gt; Mammals &gt; Lymphatic system &gt; Lymph nodes &gt; Forelegs') is grounded to BTO:0006514 (foreleg), the generated record combines BTO subclass parent BTO:0000721 (leg) with GOLD path parent UBERON:0000029 (lymph node), falsely asserting that a foreleg is a subtype of lymph node. Resolving F1 by ungrounding habitatmech:GOLD.80220dc4d4 to 'mammalian forelimb lymph node' under UBERON:0000029 eliminates this parent collision.

## Recommended Actions And Acceptance Checks

### ACT1

GOLD path 'Host-associated &gt; Mammals &gt; Lymphatic system &gt; Lymph nodes &gt; Forelegs' (habitatmech:GOLD.80220dc4d4) denotes a lymph node of the mammalian forelimb (such as the axillary or superficial cervical lymph node, parallel to already-curated sibling hind_legs.yaml habitatmech:GOLD.ca4882ca81 'mammalian hindlimb lymph node'), not the entire front leg (BTO:0006514 foreleg, 'A front leg.'). Replace the GROUND decision on habitatmech:GOLD.80220dc4d4 in curation/decisions.tsv with CONFIRM_UNGROUNDED (object_id=UBERON:0000029, object_label=lymph node, relation=parent), author a curated definition for 'mammalian forelimb lymph node' under UBERON:0000029 in curation/term_requests.tsv, exclude displaced source label 'Forelegs' in curation/definition_source_label_exclusions.tsv, and update data/habitats/PATHS.tsv.

- Verify data/habitats/host_associated/foreleg.yaml resolves to habitatmech:GOLD.80220dc4d4 (mammalian forelimb lymph node) with parent_habitats=['UBERON:0000029'] and without BTO:0000721 or bare 'Forelegs' exact_synonym.
- Run just qc and just validate-products.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/foreleg.yaml; Entire YAML | supports | All target fields, source attestations, synonyms, parent_habitats, and generated history for BTO:0006514 (foreleg) were read. |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon, organism-form, and subcellular organelle terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=BTO:0006514, grounding_status=EXACT, mapping_status=REVIEWED, parent_habitats=["BTO:0000721", "UBERON:0000029"]. |
| ESIB1 | data/habitats/host_associated/hind_legs.yaml; Entire YAML | supports | Already-curated sibling GOLD lymph-node record habitatmech:GOLD.ca4882ca81 (mammalian hindlimb lymph node, 'Host-associated &gt; Mammals &gt; Lymphatic system &gt; Lymph nodes &gt; Hind legs') ungrounded under UBERON:0000029 (lymph node). |
| EGOLD | data/raw/gold_ecosystem_paths.tsv; TSV rows 2076 | supports | [{"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Mammals &gt; Lymphatic system &gt; Lymph nodes &gt; Forelegs", "depth": "5", "ecosystem": "Host-associated", "ecosystem_category": "Mammals", "ecosystem_subtype": "Lymph nodes", "ecosystem_type": "Lymphatic system", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:6764", "leaf_label": "Forelegs", "organism_count": "0", "specific_ecosystem": "Forelegs", "study_count": "0", "total_assertions": "0"}, "row": 2076}] |
| EONT | data/raw/ontology_terms.tsv; TSV rows 722,6513,12878 | supports | [{"data": {"definition": "A limb of an animal used especially for supporting the body and for walking.", "deprecated": "", "directly_referenced": "FALSE", "label": "leg", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0000721"}, "row": 722}, {"data": {"definition": "A front leg.", "deprecated": "", "directly_referenced": "TRUE", "label": "foreleg", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0006514"}, "row": 6513}, {"data": {"definition": "Any of the rounded masses of lymphoid tissue that are surrounded by a capsule of connective tissue, are distributed along the lymphatic vessels, and contain numerous lymphocytes which filter the flow of lymph.", "deprecated": "", "directly_referenced": "TRUE", "label": "lymph node", "label_only": "FALSE", "ontology": "UBERON", "synonyms": "lymph gland&#124;nodus lymphaticus", "term_id": "UBERON:0000029"}, "row": 12878}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 463,464,4556,4557,10990 | supports | [{"data": {"object": "BTO:0001729", "predicate": "rdfs:subClassOf", "subject": "BTO:0000721"}, "row": 463}, {"data": {"object": "BTO:0002345", "predicate": "rdfs:subClassOf", "subject": "BTO:0000721"}, "row": 464}, {"data": {"object": "BTO:0000721", "predicate": "rdfs:subClassOf", "subject": "BTO:0006514"}, "row": 4556}, {"data": {"object": "BTO:0000721", "predicate": "rdfs:subClassOf", "subject": "BTO:0006515"}, "row": 4557}, {"data": {"object": "UBERON:0005057", "predicate": "rdfs:subClassOf", "subject": "UBERON:0000029"}, "row": 10990}] |
| EDEC | curation/decisions.tsv; TSV rows 776 | supports | [{"data": {"category": "", "curator": "claude-opus-5", "date": "2026-08-12", "decision": "GROUND", "grounding_status": "EXACT", "identifier": "habitatmech:GOLD.80220dc4d4", "notes": "Leaf label equals the BTO label exactly and no other source concept claims it. Path: Host-associated &gt; Mammals &gt; Lymphatic system &gt; Lymph nodes &gt; Forelegs", "object_id": "BTO:0006514", "object_label": "foreleg", "relation": "", "review_depth": "ITEM"}, "row": 776}] |
| EP2 | data/habitats/host_associated/lymph_node__7af26c8b.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": "Any of the rounded masses of lymphoid tissue that are surrounded by a capsule of connective tissue, are distributed along the lymphatic vessels, and contain numerous lymphocytes which filter the flow of lymph.", "grounding_status": "EXACT", "identifier": "UBERON:0000029", "label": "lymph node", "mapping_status": "REVIEWED", "parent_habitats": ["UBERON:0005057", "habitatmech:GOLD.a792be9b27", "habitatmech:GOLD.be39fe9a0e"], "source_attestations": [{"assertion_count": 129, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:exactMatch", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:3677", "source_label": "Lymph nodes", "source_path": "Host-associated &gt; Mammals &gt; Lymphatic system &gt; Lymph nodes"}, {"assertion_count": 25, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:exactMatch", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:3694", "source_label": "Lymph nodes", "source_path": "Host-associated &gt; Mammals: Human &gt; Lymphatic system &gt; Lymph nodes"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'foreleg&#124;BTO:0006514' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal verified no prior target review bundle exists for this record; curation and history tables were inspected for all matching rows. |

## Limits And Additional Notes

- Only the cited repository inputs, ontology terms, and source inventories were inspected; original specimen-level support for every upstream source assertion was not exhaustively reconstructed.
- Source counts, PREGO scores, and ranks are not prevalence, viability, mechanism, or characteristic presence.
- Configured label correspondence skipped 2,094 no-adapter pairs; this is not whole-corpus identifier certification.
- Read-only review: no curation table, generated habitat YAML, status, or history record was modified.
- All target and context inputs were captured at clean git commit 19d3ccb65e6b5128b9b0a5ae39cb509bf3f2bf39.
- Structured-review archive traversal confirmed no prior target review bundle exists for this record.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T181025Z-foreleg-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: foreleg (BTO:0006514)'
started_at: '2026-11-09T18:08:00Z'
finished_at: '2026-11-09T18:10:25Z'
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
summary: The GOLD-attested record BTO:0006514 (foreleg, 'A front leg.', EXACT/REVIEWED)
  grounds GOLD path 'Host-associated > Mammals > Lymphatic system > Lymph nodes >
  Forelegs' (habitatmech:GOLD.80220dc4d4) to the whole front limb BTO:0006514 rather
  than a mammalian forelimb lymph node (parallel to hind_legs.yaml habitatmech:GOLD.ca4882ca81),
  causing BTO:0006514 to assert both BTO:0000721 (leg) and UBERON:0000029 (lymph node)
  in parent_habitats.
source:
  git_revision: 19d3ccb65e6b5128b9b0a5ae39cb509bf3f2bf39
  state: git_commit
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
  - path: data/habitats/PATHS.tsv
    sha256: ee559f7b45b4af2d72a078c45d1a3b676785d34305f286e9738f95771dbaccfd
    role: context
  - path: data/habitats/host_associated/foreleg.yaml
    sha256: f1e0b2a6ac736a093fcfd5f854ea35fd3b2480f77e5192db26bf357decd22625
    role: target
  - path: data/habitats/host_associated/hind_legs.yaml
    sha256: 92f64b32540428e126f0d371ed83553b36e4f1429458c855dfde6753ccc7d088
    role: context
  - path: data/habitats/host_associated/lymph_node__7af26c8b.yaml
    sha256: 2ad5c08889ffa33811bb6d9e2cf48891e13376d441f51fdacac76aa2456288b7
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
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
    role: context
  - path: src/habitatmech/seed.py
    sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
    role: context
targets:
- target_id: BTO:0006514
  path: data/habitats/host_associated/foreleg.yaml
  label: foreleg
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
  description: Scientific assessment of one exact generated target (data/habitats/host_associated/foreleg.yaml)
    at captured main revision 19d3ccb65e6b5128b9b0a5ae39cb509bf3f2bf39.
  selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/
    path order (finger through free_living_state); this bundle assesses its single
    resolved identifier and source path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - BTO:0006514
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
    --target-class HabitatRecord data/habitats/host_associated/foreleg.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0006514
  summary: Completed 2026-11-09T18:08:48Z. No issues found.
  scope_note: Individual schema; strict command covers the 24 named cohort targets;
    other documented gates have full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/habitats/host_associated/finger.yaml
    data/habitats/host_associated/fish.yaml data/habitats/host_associated/flagellate.yaml
    data/habitats/host_associated/flagellum.yaml data/habitats/host_associated/flat_warts.yaml
    data/habitats/host_associated/flower.yaml data/habitats/host_associated/foot.yaml
    data/habitats/host_associated/foraminifera.yaml data/habitats/host_associated/forearm.yaml
    data/habitats/host_associated/foregut.yaml data/habitats/host_associated/foregut__6bc8c43a.yaml
    data/habitats/host_associated/foregut__c14450a8.yaml data/habitats/host_associated/foregut__ce63e8ab.yaml
    data/habitats/host_associated/foregut__d14a54ae.yaml data/habitats/host_associated/foregut__ee6a8f74.yaml
    data/habitats/host_associated/foreleg.yaml data/habitats/host_associated/forestomach.yaml
    data/habitats/host_associated/fossilized_remains.yaml data/habitats/host_associated/fossilized_remains__19772eb4.yaml
    data/habitats/host_associated/fossilized_remains__8b01c49f.yaml data/habitats/host_associated/fossilized_remains__eec3c6e8.yaml
    data/habitats/host_associated/frass.yaml data/habitats/host_associated/frass__c029dd2b.yaml
    data/habitats/host_associated/free_living_state.yaml --out .temp/c8s4_24_strict.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0006514
  summary: 'Completed 2026-11-09T18:08:54Z. Validated 24 files; files with ERROR:
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
  - BTO:0006514
  summary: Completed 2026-11-09T18:09:00Z. No issues found; 876 history record(s)
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
  - BTO:0006514
  summary: 'Completed 2026-11-09T18:09:01Z. provenance current: 14 committed inventories,
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
  - BTO:0006514
  summary: 'Completed 2026-11-09T18:09:16Z. expected 3209 records, found 3209 on disk;
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
  - BTO:0006514
  summary: Completed 2026-11-09T18:09:22Z. validated 103 causal-graph curation file(s)
    with 103 graph(s).
  scope_note: Full-corpus causal-graph overlay validation.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: .venv/bin/python scripts/build_term_requests.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0006514
  summary: Completed 2026-11-09T18:09:36Z. term-request table is current (674 terms).
  scope_note: Full-corpus term-request table currency check.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0006514
  summary: 'Completed 2026-11-09T18:10:17Z. OK_CANONICAL: 1213, OK_SYNONYM: 1, OK_EXCEPTION:
    5, SKIPPED_NO_ADAPTER: 2094. All id<->label pairs correspond.'
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/foreleg.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T18:10:25Z'
  support: supports
  summary: All target fields, source attestations, synonyms, parent_habitats, and
    generated history for BTO:0006514 (foreleg) were read.
  snapshot_sha256: f1e0b2a6ac736a093fcfd5f854ea35fd3b2480f77e5192db26bf357decd22625
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-09T18:10:25Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon, organism-form,
    and subcellular organelle terms cannot substitute for associated environments;
    parent_habitats must be strictly broader across all contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-09T18:10:25Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-09T18:10:25Z'
  support: supports
  summary: Seed generator produces identifier=BTO:0006514, grounding_status=EXACT,
    mapping_status=REVIEWED, parent_habitats=["BTO:0000721", "UBERON:0000029"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: ESIB1
  kind: record_content
  reference: data/habitats/host_associated/hind_legs.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T18:10:25Z'
  support: supports
  summary: Already-curated sibling GOLD lymph-node record habitatmech:GOLD.ca4882ca81
    (mammalian hindlimb lymph node, 'Host-associated > Mammals > Lymphatic system
    > Lymph nodes > Hind legs') ungrounded under UBERON:0000029 (lymph node).
  snapshot_sha256: 92f64b32540428e126f0d371ed83553b36e4f1429458c855dfde6753ccc7d088
- evidence_id: EGOLD
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV rows 2076
  accessed_at: '2026-11-09T18:10:25Z'
  support: supports
  summary: '[{"data": {"biosample_count": "0", "canonical_path": "Host-associated
    > Mammals > Lymphatic system > Lymph nodes > Forelegs", "depth": "5", "ecosystem":
    "Host-associated", "ecosystem_category": "Mammals", "ecosystem_subtype": "Lymph
    nodes", "ecosystem_type": "Lymphatic system", "gold_node_count": "1", "gold_node_ids":
    "gold.ecosystem:6764", "leaf_label": "Forelegs", "organism_count": "0", "specific_ecosystem":
    "Forelegs", "study_count": "0", "total_assertions": "0"}, "row": 2076}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 722,6513,12878
  accessed_at: '2026-11-09T18:10:25Z'
  support: supports
  summary: '[{"data": {"definition": "A limb of an animal used especially for supporting
    the body and for walking.", "deprecated": "", "directly_referenced": "FALSE",
    "label": "leg", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id":
    "BTO:0000721"}, "row": 722}, {"data": {"definition": "A front leg.", "deprecated":
    "", "directly_referenced": "TRUE", "label": "foreleg", "label_only": "FALSE",
    "ontology": "BTO", "synonyms": "", "term_id": "BTO:0006514"}, "row": 6513}, {"data":
    {"definition": "Any of the rounded masses of lymphoid tissue that are surrounded
    by a capsule of connective tissue, are distributed along the lymphatic vessels,
    and contain numerous lymphocytes which filter the flow of lymph.", "deprecated":
    "", "directly_referenced": "TRUE", "label": "lymph node", "label_only": "FALSE",
    "ontology": "UBERON", "synonyms": "lymph gland|nodus lymphaticus", "term_id":
    "UBERON:0000029"}, "row": 12878}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 463,464,4556,4557,10990
  accessed_at: '2026-11-09T18:10:25Z'
  support: supports
  summary: '[{"data": {"object": "BTO:0001729", "predicate": "rdfs:subClassOf", "subject":
    "BTO:0000721"}, "row": 463}, {"data": {"object": "BTO:0002345", "predicate": "rdfs:subClassOf",
    "subject": "BTO:0000721"}, "row": 464}, {"data": {"object": "BTO:0000721", "predicate":
    "rdfs:subClassOf", "subject": "BTO:0006514"}, "row": 4556}, {"data": {"object":
    "BTO:0000721", "predicate": "rdfs:subClassOf", "subject": "BTO:0006515"}, "row":
    4557}, {"data": {"object": "UBERON:0005057", "predicate": "rdfs:subClassOf", "subject":
    "UBERON:0000029"}, "row": 10990}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EDEC
  kind: database
  reference: curation/decisions.tsv
  locator: TSV rows 776
  accessed_at: '2026-11-09T18:10:25Z'
  support: supports
  summary: '[{"data": {"category": "", "curator": "claude-opus-5", "date": "2026-08-12",
    "decision": "GROUND", "grounding_status": "EXACT", "identifier": "habitatmech:GOLD.80220dc4d4",
    "notes": "Leaf label equals the BTO label exactly and no other source concept
    claims it. Path: Host-associated > Mammals > Lymphatic system > Lymph nodes >
    Forelegs", "object_id": "BTO:0006514", "object_label": "foreleg", "relation":
    "", "review_depth": "ITEM"}, "row": 776}]'
  snapshot_sha256: d3bf0a3ca3570e8f318898db92f800a1e13220f64112fe5c1ce1edc9181c3ae2
- evidence_id: EP2
  kind: record_content
  reference: data/habitats/host_associated/lymph_node__7af26c8b.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-11-09T18:10:25Z'
  support: supports
  summary: '{"definition": "Any of the rounded masses of lymphoid tissue that are
    surrounded by a capsule of connective tissue, are distributed along the lymphatic
    vessels, and contain numerous lymphocytes which filter the flow of lymph.", "grounding_status":
    "EXACT", "identifier": "UBERON:0000029", "label": "lymph node", "mapping_status":
    "REVIEWED", "parent_habitats": ["UBERON:0005057", "habitatmech:GOLD.a792be9b27",
    "habitatmech:GOLD.be39fe9a0e"], "source_attestations": [{"assertion_count": 129,
    "assertion_unit": "ORGANISM", "mapping_predicate": "skos:exactMatch", "notes":
    "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.",
    "source": "GOLD", "source_id": "gold.ecosystem:3677", "source_label": "Lymph nodes",
    "source_path": "Host-associated > Mammals > Lymphatic system > Lymph nodes"},
    {"assertion_count": 25, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:exactMatch",
    "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.",
    "source": "GOLD", "source_id": "gold.ecosystem:3694", "source_label": "Lymph nodes",
    "source_path": "Host-associated > Mammals: Human > Lymphatic system > Lymph nodes"}]}'
  snapshot_sha256: 2ad5c08889ffa33811bb6d9e2cf48891e13376d441f51fdacac76aa2456288b7
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'foreleg|BTO:0006514' reviews/structured/*/review.yaml curation/
    history/
  accessed_at: '2026-11-09T18:10:25Z'
  support: context_only
  summary: Structured-review traversal verified no prior target review bundle exists
    for this record; curation and history tables were inspected for all matching rows.
  search_scope: curation, history, data/raw, and reviews/structured/*/review.yaml
    traversal at commit 19d3ccb65e6b5128b9b0a5ae39cb509bf3f2bf39.
assessments:
- assessment_id: A1
  area: schema
  topic: Native validity and reproduction
  outcome: supported
  summary: Individual schema, strict 24-target validation, 876 history records, 14
    inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 103 causal
    overlays, and 674 term requests passed.
  target_ids:
  - BTO:0006514
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: concern
  summary: The GOLD-attested record BTO:0006514 (foreleg, 'A front leg.', EXACT/REVIEWED)
    grounds GOLD path 'Host-associated > Mammals > Lymphatic system > Lymph nodes
    > Forelegs' (habitatmech:GOLD.80220dc4d4) to the whole front limb BTO:0006514
    rather than a mammalian forelimb lymph node (parallel to hind_legs.yaml habitatmech:GOLD.ca4882ca81),
    causing BTO:0006514 to assert both BTO:0000721 (leg) and UBERON:0000029 (lymph
    node) in parent_habitats.
  target_ids:
  - BTO:0006514
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EGOLD
  - EONT
  - EONTEDGE
  - EDEC
  - EP2
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks,
    and pools: [{"count": 0, "source": "GOLD", "unit": null}]. Zero counts are omitted;
    unrelated parent counts are not combined.'
  target_ids:
  - BTO:0006514
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EGOLD
  - EONT
  - EONTEDGE
  - EDEC
  - EP2
- assessment_id: A4
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: Missing optional parameters/graphs are not evidence deficits. Full source
    decisions and executed routes reproduce REVIEWED / EXACT; this read-only review
    does not mutate generated records.
  target_ids:
  - BTO:0006514
  evidence_ids:
  - E1
  - ESEED
  - ESCHEMA
findings:
- finding_id: F1
  issue_key: foreleg-lymph-node-identity
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Mammalian forelimb lymph node path is grounded to whole limb BTO:0006514
    (foreleg)
  description: GOLD path 'Host-associated > Mammals > Lymphatic system > Lymph nodes
    > Forelegs' (habitatmech:GOLD.80220dc4d4) denotes a lymph node of the mammalian
    forelimb (such as the axillary or superficial cervical lymph node, parallel to
    already-curated sibling hind_legs.yaml habitatmech:GOLD.ca4882ca81 'mammalian
    hindlimb lymph node'), not the entire front leg (BTO:0006514 foreleg, 'A front
    leg.'). Replace the GROUND decision on habitatmech:GOLD.80220dc4d4 in curation/decisions.tsv
    with CONFIRM_UNGROUNDED (object_id=UBERON:0000029, object_label=lymph node, relation=parent),
    author a curated definition for 'mammalian forelimb lymph node' under UBERON:0000029
    in curation/term_requests.tsv, exclude displaced source label 'Forelegs' in curation/definition_source_label_exclusions.tsv,
    and update data/habitats/PATHS.tsv.
  target_ids:
  - BTO:0006514
  field_paths:
  - identifier
  - label
  - definition
  - grounding_status
  - parent_habitats
  - source_attestations
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EGOLD
  - EONT
  - EONTEDGE
  - EDEC
  - EP2
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: blocker
  normalization_reason: Source path denoting a forelimb lymph node is grounded to
    the whole forelimb anatomical class BTO:0006514.
  external_issues: []
- finding_id: F2
  issue_key: foreleg-lymph-node-parent-collision
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Grounding forelimb lymph node to BTO:0006514 (foreleg) asserts UBERON:0000029
    (lymph node) as a parent of foreleg
  description: Because habitatmech:GOLD.80220dc4d4 ('Host-associated > Mammals > Lymphatic
    system > Lymph nodes > Forelegs') is grounded to BTO:0006514 (foreleg), the generated
    record combines BTO subclass parent BTO:0000721 (leg) with GOLD path parent UBERON:0000029
    (lymph node), falsely asserting that a foreleg is a subtype of lymph node. Resolving
    F1 by ungrounding habitatmech:GOLD.80220dc4d4 to 'mammalian forelimb lymph node'
    under UBERON:0000029 eliminates this parent collision.
  target_ids:
  - BTO:0006514
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
  - EDEC
  - EP2
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or representation claim; deterministic
    validity does not establish scientific support.
  external_issues: []
actions:
- action_id: ACT1
  finding_ids:
  - F1
  - F2
  target_ids:
  - BTO:0006514
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: GOLD path 'Host-associated > Mammals > Lymphatic system > Lymph nodes
    > Forelegs' (habitatmech:GOLD.80220dc4d4) denotes a lymph node of the mammalian
    forelimb (such as the axillary or superficial cervical lymph node, parallel to
    already-curated sibling hind_legs.yaml habitatmech:GOLD.ca4882ca81 'mammalian
    hindlimb lymph node'), not the entire front leg (BTO:0006514 foreleg, 'A front
    leg.'). Replace the GROUND decision on habitatmech:GOLD.80220dc4d4 in curation/decisions.tsv
    with CONFIRM_UNGROUNDED (object_id=UBERON:0000029, object_label=lymph node, relation=parent),
    author a curated definition for 'mammalian forelimb lymph node' under UBERON:0000029
    in curation/term_requests.tsv, exclude displaced source label 'Forelegs' in curation/definition_source_label_exclusions.tsv,
    and update data/habitats/PATHS.tsv.
  generator: Update curation/decisions.tsv, curation/term_requests.tsv, curation/definition_source_label_exclusions.tsv,
    and data/habitats/PATHS.tsv, then run just seed, just seed-canary, just seed-apply,
    just term-requests, just redirects, and just render.
  acceptance_checks:
  - Verify data/habitats/host_associated/foreleg.yaml resolves to habitatmech:GOLD.80220dc4d4
    (mammalian forelimb lymph node) with parent_habitats=['UBERON:0000029'] and without
    BTO:0000721 or bare 'Forelegs' exact_synonym.
  - Run just qc and just validate-products.
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
- All target and context inputs were captured at clean git commit 19d3ccb65e6b5128b9b0a5ae39cb509bf3f2bf39.
- Structured-review archive traversal confirmed no prior target review bundle exists
  for this record.
tags:
- individual-scientific-review
- host-associated
```
