# Record review: Eye (habitatmech:GOLD.7f217d034e)

- Review: 20261106T194821Z-eye__59a4c665-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-06T19:35:00Z
- Finished UTC: 2026-11-06T19:48:21Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The minted GOLD record habitatmech:GOLD.7f217d034e (Eye in Host-associated &gt; Fish &gt; Visual system &gt; Eye, NARROW/SEEDED, 1 ORGANISM assertion) is placed under UBERON:0000970 (eye), but retains the whole-organ-system piscine Visual system GOLD parent habitatmech:GOLD.5a41405bc3 as a superclass and exhibits the #1398 narrow-match mapping_predicate representation contract defect.

## Scope And Provenance

Scientific assessment of one exact generated target (data/habitats/host_associated/eye__59a4c665.yaml) at captured main revision 355eb4a23118506c83a76cf22c6332d04decffec.

Selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/ path order (excretory_system__22ee753c through fecal); this bundle assesses its single resolved identifier and source path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 355eb4a23118506c83a76cf22c6332d04decffec.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.7f217d034e | data/habitats/host_associated/eye__59a4c665.yaml | generated | Eye |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.7f217d034e | Completed 2026-11-06T19:45:12Z. No issues found. |
| validate-strict | passed | True | habitatmech:GOLD.7f217d034e | Completed 2026-11-06T19:45:18Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | habitatmech:GOLD.7f217d034e | Completed 2026-11-06T19:45:25Z. No issues found; 866 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | habitatmech:GOLD.7f217d034e | Completed 2026-11-06T19:45:28Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | habitatmech:GOLD.7f217d034e | Completed 2026-11-06T19:45:55Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | habitatmech:GOLD.7f217d034e | Completed 2026-11-06T19:46:02Z. validated 83 causal-graph curation file(s) with 83 graph(s). |
| term-requests-check | passed | True | habitatmech:GOLD.7f217d034e | Completed 2026-11-06T19:46:05Z. term-request table is current (671 terms). |
| validate-products | passed | True | habitatmech:GOLD.7f217d034e | Completed 2026-11-06T19:47:55Z. OK_CANONICAL: 1203, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2084. All id&lt;-&gt;label pairs correspond. |

## Scientific And Domain Assessments

### Native validity and reproduction

schema: supported. Targets: habitatmech:GOLD.7f217d034e.

Individual schema, strict 24-target validation, 866 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 83 causal overlays, and 671 term requests passed.

### Identity, definition, hierarchy and aliases

identity: concern. Targets: habitatmech:GOLD.7f217d034e.

The piscine eye (under UBERON:0000970, eye) is an anatomical sensory organ (part_of the visual system), not a subtype (is_a) of the piscine Visual system (habitatmech:GOLD.5a41405bc3), and the record carries mapping_predicate skos:narrowMatch while its emitted identifier is the minted source concept (#1398).

### Source counts and retained ranking

quantity: supported. Targets: habitatmech:GOLD.7f217d034e.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"source": "GOLD", "count": 1, "unit": "ORGANISM"}]. Zero counts are omitted; unrelated parent counts are not combined.

### Parameters, mechanisms and native status

completeness: supported. Targets: habitatmech:GOLD.7f217d034e.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce SEEDED / NARROW; this read-only review does not mutate generated records.

## Findings

### F1: Piscine Eye retains piscine Visual system GOLD parent as a superclass

major / open / confirmed; issue key: eye--59a4c665-context-parent.

Add an exclusion row in curation/gold_parent_exclusions.tsv for source identifier habitatmech:GOLD.7f217d034e on GOLD path 'Host-associated &gt; Fish &gt; Visual system &gt; Eye' (exact target habitatmech:GOLD.7f217d034e) excluding parent_id habitatmech:GOLD.5a41405bc3 (Visual system), preserving broader ontology parent UBERON:0000970 (eye).

### F2: Narrow mapping predicate points to a minted source-path record

major / open / confirmed; issue key: eye--59a4c665-mapping-endpoint-contract.

Reconcile narrow-match source-attestation output with the endpoint contract tracked in Issue #1398 for habitatmech:GOLD.7f217d034e (Host-associated &gt; Fish &gt; Visual system &gt; Eye) and its broader ontology parent UBERON:0000970 (eye).

## Recommended Actions And Acceptance Checks

### ACT1

Add an exclusion row in curation/gold_parent_exclusions.tsv for source identifier habitatmech:GOLD.7f217d034e on GOLD path 'Host-associated &gt; Fish &gt; Visual system &gt; Eye' (exact target habitatmech:GOLD.7f217d034e) excluding parent_id habitatmech:GOLD.5a41405bc3 (Visual system), preserving broader ontology parent UBERON:0000970 (eye). No repair is performed by this read-only review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

### ACT2

Reconcile narrow-match source-attestation output with the endpoint contract tracked in Issue #1398 for habitatmech:GOLD.7f217d034e (Host-associated &gt; Fish &gt; Visual system &gt; Eye) and its broader ontology parent UBERON:0000970 (eye). No repair is performed by this read-only review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/eye__59a4c665.yaml; Entire YAML | supports | All target fields, source attestations, synonyms, parent_habitats, and generated history for habitatmech:GOLD.7f217d034e (Eye) were read. |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=habitatmech:GOLD.7f217d034e, grounding_status=NARROW, mapping_status=SEEDED, parent_habitats=["UBERON:0000970", "habitatmech:GOLD.5a41405bc3"]. |
| EGOLD | data/raw/gold_ecosystem_paths.tsv; TSV rows 1041 | supports | [{"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Fish &gt; Visual system &gt; Eye", "depth": "4", "ecosystem": "Host-associated", "ecosystem_category": "Fish", "ecosystem_subtype": "Eye", "ecosystem_type": "Visual system", "gold_node_count": "2", "gold_node_ids": "gold.ecosystem:6930&#124;gold.ecosystem:6931", "leaf_label": "Eye", "organism_count": "1", "specific_ecosystem": "", "study_count": "0", "total_assertions": "1"}, "row": 1041}] |
| EGROUND | data/raw/isolation_source_groundings.tsv; TSV rows 109 | supports | [{"data": {"confidence": "high", "curator": "ols4_auto", "mapping_justification": "semapv:LexicalMatching", "object_id": "UBERON:0000970", "object_label": "eye", "object_source": "UBERON", "predicate_id": "skos:exactMatch", "source_dataset": "bacdive", "subject_label": "Eye", "subject_label_normalized": "eye", "verified_date": "2026-05-01"}, "row": 109}] |
| EONT | data/raw/ontology_terms.tsv; TSV rows 12965 | supports | [{"data": {"definition": "An organ that detects light.", "deprecated": "", "directly_referenced": "TRUE", "label": "eye", "label_only": "FALSE", "ontology": "UBERON", "synonyms": "light-detecting organ&#124;visual apparatus", "term_id": "UBERON:0000970"}, "row": 12965}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 10995,11105 | supports | [{"data": {"object": "UBERON:0000970", "predicate": "rdfs:subClassOf", "subject": "UBERON:0000047"}, "row": 10995}, {"data": {"object": "UBERON:0000020", "predicate": "rdfs:subClassOf", "subject": "UBERON:0000970"}, "row": 11105}] |
| EP2 | data/habitats/host_associated/visual_system__23837b48.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": null, "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.5a41405bc3", "label": "Visual system", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0002104", "habitatmech:GOLD.3d529a667e"], "source_attestations": [{"mapping_predicate": "skos:narrowMatch", "source": "GOLD", "source_id": "gold.ecosystem:6929", "source_label": "Visual system", "source_path": "Host-associated &gt; Fish &gt; Visual system"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'eye__59a4c665&#124;habitatmech:GOLD.7f217d034e' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal verified no prior target review bundle exists for this record; curation and history tables were inspected for all matching rows. |

## Limits And Additional Notes

- Only the stated primary evidence and current ontology/taxonomy authorities were independently inspected; original specimen-level support for every source-bin member is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism or characteristic presence. Parent observations are not inherited by children.
- Configured label correspondence skipped 2,084 no-adapter pairs; this is not whole-corpus identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in this pre-save observation.
- iModulonDB is not applicable: the target has no gene, regulator or expression-module assertion. No paid research or scientific-status promotion was performed.
- All included input bytes match both the clean working tree and exact captured Git revision 355eb4a23118506c83a76cf22c6332d04decffec.
- Structured archive traversal found no earlier structured review targeting this record. No existing bundle is superseded or closed.
- This read-only Stage-4 review proposes maintained-owner actions and preserves open findings for Stage 5 grouped remediation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T194821Z-eye__59a4c665-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: Eye (habitatmech:GOLD.7f217d034e)'
started_at: '2026-11-06T19:35:00Z'
finished_at: '2026-11-06T19:48:21Z'
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
summary: 'The minted GOLD record habitatmech:GOLD.7f217d034e (Eye in Host-associated
  > Fish > Visual system > Eye, NARROW/SEEDED, 1 ORGANISM assertion) is placed under
  UBERON:0000970 (eye), but retains the whole-organ-system piscine Visual system GOLD
  parent habitatmech:GOLD.5a41405bc3 as a superclass and exhibits the #1398 narrow-match
  mapping_predicate representation contract defect.'
source:
  git_revision: 355eb4a23118506c83a76cf22c6332d04decffec
  state: git_commit
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
  - path: data/habitats/host_associated/eye__59a4c665.yaml
    sha256: b42052577506c7eb15f571e243c6bb8d4ac73ab7525d65721857a7409a13299f
    role: target
  - path: data/habitats/host_associated/visual_system__23837b48.yaml
    sha256: 8e917e9e3d06c0e830a6331a6970f114fdc4585ee99ed6f22eefcfab38865ace
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
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
    role: context
  - path: src/habitatmech/seed.py
    sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
    role: context
targets:
- target_id: habitatmech:GOLD.7f217d034e
  path: data/habitats/host_associated/eye__59a4c665.yaml
  label: Eye
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
  description: Scientific assessment of one exact generated target (data/habitats/host_associated/eye__59a4c665.yaml)
    at captured main revision 355eb4a23118506c83a76cf22c6332d04decffec.
  selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/
    path order (excretory_system__22ee753c through fecal); this bundle assesses its
    single resolved identifier and source path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.7f217d034e
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
    --target-class HabitatRecord data/habitats/host_associated/eye__59a4c665.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.7f217d034e
  summary: Completed 2026-11-06T19:45:12Z. No issues found.
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
  - habitatmech:GOLD.7f217d034e
  summary: 'Completed 2026-11-06T19:45:18Z. Validated 24 files; files with ERROR:
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
  - habitatmech:GOLD.7f217d034e
  summary: Completed 2026-11-06T19:45:25Z. No issues found; 866 history record(s)
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
  - habitatmech:GOLD.7f217d034e
  summary: 'Completed 2026-11-06T19:45:28Z. provenance current: 14 committed inventories,
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
  - habitatmech:GOLD.7f217d034e
  summary: 'Completed 2026-11-06T19:45:55Z. expected 3209 records, found 3209 on disk;
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
  - habitatmech:GOLD.7f217d034e
  summary: Completed 2026-11-06T19:46:02Z. validated 83 causal-graph curation file(s)
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
  - habitatmech:GOLD.7f217d034e
  summary: Completed 2026-11-06T19:46:05Z. term-request table is current (671 terms).
  scope_note: Full-corpus term-request table currency check.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.7f217d034e
  summary: 'Completed 2026-11-06T19:47:55Z. OK_CANONICAL: 1203, OK_SYNONYM: 1, OK_EXCEPTION:
    5, SKIPPED_NO_ADAPTER: 2084. All id<->label pairs correspond.'
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/eye__59a4c665.yaml
  locator: Entire YAML
  accessed_at: '2026-11-06T19:48:21Z'
  support: supports
  summary: All target fields, source attestations, synonyms, parent_habitats, and
    generated history for habitatmech:GOLD.7f217d034e (Eye) were read.
  snapshot_sha256: b42052577506c7eb15f571e243c6bb8d4ac73ab7525d65721857a7409a13299f
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-06T19:48:21Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon terms cannot substitute
    for associated environments; parent_habitats must be strictly broader across all
    contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-06T19:48:21Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-06T19:48:21Z'
  support: supports
  summary: Seed generator produces identifier=habitatmech:GOLD.7f217d034e, grounding_status=NARROW,
    mapping_status=SEEDED, parent_habitats=["UBERON:0000970", "habitatmech:GOLD.5a41405bc3"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EGOLD
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV rows 1041
  accessed_at: '2026-11-06T19:48:21Z'
  support: supports
  summary: '[{"data": {"biosample_count": "0", "canonical_path": "Host-associated
    > Fish > Visual system > Eye", "depth": "4", "ecosystem": "Host-associated", "ecosystem_category":
    "Fish", "ecosystem_subtype": "Eye", "ecosystem_type": "Visual system", "gold_node_count":
    "2", "gold_node_ids": "gold.ecosystem:6930|gold.ecosystem:6931", "leaf_label":
    "Eye", "organism_count": "1", "specific_ecosystem": "", "study_count": "0", "total_assertions":
    "1"}, "row": 1041}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: EGROUND
  kind: database
  reference: data/raw/isolation_source_groundings.tsv
  locator: TSV rows 109
  accessed_at: '2026-11-06T19:48:21Z'
  support: supports
  summary: '[{"data": {"confidence": "high", "curator": "ols4_auto", "mapping_justification":
    "semapv:LexicalMatching", "object_id": "UBERON:0000970", "object_label": "eye",
    "object_source": "UBERON", "predicate_id": "skos:exactMatch", "source_dataset":
    "bacdive", "subject_label": "Eye", "subject_label_normalized": "eye", "verified_date":
    "2026-05-01"}, "row": 109}]'
  snapshot_sha256: ab6a997359aab961c40928f9b13e06adb6dc43124fa3de821819570dd87f43b8
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 12965
  accessed_at: '2026-11-06T19:48:21Z'
  support: supports
  summary: '[{"data": {"definition": "An organ that detects light.", "deprecated":
    "", "directly_referenced": "TRUE", "label": "eye", "label_only": "FALSE", "ontology":
    "UBERON", "synonyms": "light-detecting organ|visual apparatus", "term_id": "UBERON:0000970"},
    "row": 12965}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 10995,11105
  accessed_at: '2026-11-06T19:48:21Z'
  support: supports
  summary: '[{"data": {"object": "UBERON:0000970", "predicate": "rdfs:subClassOf",
    "subject": "UBERON:0000047"}, "row": 10995}, {"data": {"object": "UBERON:0000020",
    "predicate": "rdfs:subClassOf", "subject": "UBERON:0000970"}, "row": 11105}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EP2
  kind: record_content
  reference: data/habitats/host_associated/visual_system__23837b48.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-11-06T19:48:21Z'
  support: supports
  summary: '{"definition": null, "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.5a41405bc3",
    "label": "Visual system", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0002104",
    "habitatmech:GOLD.3d529a667e"], "source_attestations": [{"mapping_predicate":
    "skos:narrowMatch", "source": "GOLD", "source_id": "gold.ecosystem:6929", "source_label":
    "Visual system", "source_path": "Host-associated > Fish > Visual system"}]}'
  snapshot_sha256: 8e917e9e3d06c0e830a6331a6970f114fdc4585ee99ed6f22eefcfab38865ace
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'eye__59a4c665|habitatmech:GOLD.7f217d034e' reviews/structured/*/review.yaml
    curation/ history/
  accessed_at: '2026-11-06T19:48:21Z'
  support: context_only
  summary: Structured-review traversal verified no prior target review bundle exists
    for this record; curation and history tables were inspected for all matching rows.
  search_scope: curation, history, data/raw, and reviews/structured/*/review.yaml
    traversal at commit 355eb4a23118506c83a76cf22c6332d04decffec.
assessments:
- assessment_id: A1
  area: schema
  topic: Native validity and reproduction
  outcome: supported
  summary: Individual schema, strict 24-target validation, 866 history records, 14
    inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 83 causal
    overlays, and 671 term requests passed.
  target_ids:
  - habitatmech:GOLD.7f217d034e
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: concern
  summary: The piscine eye (under UBERON:0000970, eye) is an anatomical sensory organ
    (part_of the visual system), not a subtype (is_a) of the piscine Visual system
    (habitatmech:GOLD.5a41405bc3), and the record carries mapping_predicate skos:narrowMatch
    while its emitted identifier is the minted source concept (#1398).
  target_ids:
  - habitatmech:GOLD.7f217d034e
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EGROUND
  - EONT
  - EONTEDGE
  - EP2
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks,
    and pools: [{"source": "GOLD", "count": 1, "unit": "ORGANISM"}]. Zero counts are
    omitted; unrelated parent counts are not combined.'
  target_ids:
  - habitatmech:GOLD.7f217d034e
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EGROUND
  - EONT
  - EONTEDGE
  - EP2
- assessment_id: A4
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: Missing optional parameters/graphs are not evidence deficits. Full source
    decisions and executed routes reproduce SEEDED / NARROW; this read-only review
    does not mutate generated records.
  target_ids:
  - habitatmech:GOLD.7f217d034e
  evidence_ids:
  - E1
  - ESEED
  - ESCHEMA
findings:
- finding_id: F1
  issue_key: eye--59a4c665-context-parent
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Piscine Eye retains piscine Visual system GOLD parent as a superclass
  description: Add an exclusion row in curation/gold_parent_exclusions.tsv for source
    identifier habitatmech:GOLD.7f217d034e on GOLD path 'Host-associated > Fish >
    Visual system > Eye' (exact target habitatmech:GOLD.7f217d034e) excluding parent_id
    habitatmech:GOLD.5a41405bc3 (Visual system), preserving broader ontology parent
    UBERON:0000970 (eye).
  target_ids:
  - habitatmech:GOLD.7f217d034e
  field_paths:
  - parent_habitats
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EGROUND
  - EONT
  - EONTEDGE
  - EP2
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or representation claim; deterministic
    validity does not establish scientific support.
  external_issues: []
- finding_id: F2
  issue_key: eye--59a4c665-mapping-endpoint-contract
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Narrow mapping predicate points to a minted source-path record
  description: 'Reconcile narrow-match source-attestation output with the endpoint
    contract tracked in Issue #1398 for habitatmech:GOLD.7f217d034e (Host-associated
    > Fish > Visual system > Eye) and its broader ontology parent UBERON:0000970 (eye).'
  target_ids:
  - habitatmech:GOLD.7f217d034e
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
  - EGROUND
  - EONT
  - EONTEDGE
  - EP2
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
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - habitatmech:GOLD.7f217d034e
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: Add an exclusion row in curation/gold_parent_exclusions.tsv for source
    identifier habitatmech:GOLD.7f217d034e on GOLD path 'Host-associated > Fish >
    Visual system > Eye' (exact target habitatmech:GOLD.7f217d034e) excluding parent_id
    habitatmech:GOLD.5a41405bc3 (Visual system), preserving broader ontology parent
    UBERON:0000970 (eye). No repair is performed by this read-only review.
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
- action_id: ACT2
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.7f217d034e
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
    contract tracked in Issue #1398 for habitatmech:GOLD.7f217d034e (Host-associated
    > Fish > Visual system > Eye) and its broader ontology parent UBERON:0000970 (eye).
    No repair is performed by this read-only review.'
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
- Configured label correspondence skipped 2,084 no-adapter pairs; this is not whole-corpus
  identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in
  this pre-save observation.
- 'iModulonDB is not applicable: the target has no gene, regulator or expression-module
  assertion. No paid research or scientific-status promotion was performed.'
notes:
- All included input bytes match both the clean working tree and exact captured Git
  revision 355eb4a23118506c83a76cf22c6332d04decffec.
- Structured archive traversal found no earlier structured review targeting this record.
  No existing bundle is superseded or closed.
- This read-only Stage-4 review proposes maintained-owner actions and preserves open
  findings for Stage 5 grouped remediation.
tags:
- individual-scientific-review
- host-associated
```
