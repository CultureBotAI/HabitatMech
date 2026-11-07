# Record review: fish feces (habitatmech:GOLD.227b8ef4a5)

- Review: 20261106T194833Z-fecal-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-06T19:35:00Z
- Finished UTC: 2026-11-06T19:48:33Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The minted GOLD record habitatmech:GOLD.227b8ef4a5 (fish feces in Host-associated &gt; Fish &gt; Digestive system &gt; Intestine &gt; Fecal, UNGROUNDED/REVIEWED, 9 ORGANISM assertions) is coherently defined under UBERON:0001988 (feces) with parent_mode REPLACE to exclude anatomical Intestine and displaced source label 'Fecal' omitted from synonyms (SOURCE_SYNONYM_EXCLUDED).

## Scope And Provenance

Scientific assessment of one exact generated target (data/habitats/host_associated/fecal.yaml) at captured main revision 355eb4a23118506c83a76cf22c6332d04decffec.

Selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/ path order (excretory_system__22ee753c through fecal); this bundle assesses its single resolved identifier and source path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 355eb4a23118506c83a76cf22c6332d04decffec.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.227b8ef4a5 | data/habitats/host_associated/fecal.yaml | generated | fish feces |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.227b8ef4a5 | Completed 2026-11-06T19:45:12Z. No issues found. |
| validate-strict | passed | True | habitatmech:GOLD.227b8ef4a5 | Completed 2026-11-06T19:45:18Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | habitatmech:GOLD.227b8ef4a5 | Completed 2026-11-06T19:45:25Z. No issues found; 866 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | habitatmech:GOLD.227b8ef4a5 | Completed 2026-11-06T19:45:28Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | habitatmech:GOLD.227b8ef4a5 | Completed 2026-11-06T19:45:55Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | habitatmech:GOLD.227b8ef4a5 | Completed 2026-11-06T19:46:02Z. validated 83 causal-graph curation file(s) with 83 graph(s). |
| term-requests-check | passed | True | habitatmech:GOLD.227b8ef4a5 | Completed 2026-11-06T19:46:05Z. term-request table is current (671 terms). |
| validate-products | passed | True | habitatmech:GOLD.227b8ef4a5 | Completed 2026-11-06T19:47:55Z. OK_CANONICAL: 1203, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2084. All id&lt;-&gt;label pairs correspond. |

## Scientific And Domain Assessments

### Native validity and reproduction

schema: supported. Targets: habitatmech:GOLD.227b8ef4a5.

Individual schema, strict 24-target validation, 866 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 83 causal overlays, and 671 term requests passed.

### Identity, definition, hierarchy and aliases

identity: supported. Targets: habitatmech:GOLD.227b8ef4a5.

The record defines fish feces under UBERON:0001988 (feces) with parent_mode REPLACE to exclude anatomical piscine Intestine (habitatmech:GOLD.79a0f12101), retains curated exact synonyms ('fish fecal material', 'piscine feces'), and omits displaced GOLD source label 'Fecal' from synonyms (SOURCE_SYNONYM_EXCLUDED) via curation/definition_source_label_exclusions.tsv.

### Source counts and retained ranking

quantity: supported. Targets: habitatmech:GOLD.227b8ef4a5.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"source": "GOLD", "count": 9, "unit": "ORGANISM"}]. Zero counts are omitted; unrelated parent counts are not combined.

### Parameters, mechanisms and native status

completeness: supported. Targets: habitatmech:GOLD.227b8ef4a5.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only review does not mutate generated records.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/fecal.yaml; Entire YAML | supports | All target fields, source attestations, synonyms, parent_habitats, and generated history for habitatmech:GOLD.227b8ef4a5 (fish feces) were read. |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=habitatmech:GOLD.227b8ef4a5, grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["UBERON:0001988"]. |
| EGOLD | data/raw/gold_ecosystem_paths.tsv; TSV rows 552 | supports | [{"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Fish &gt; Digestive system &gt; Intestine &gt; Fecal", "depth": "5", "ecosystem": "Host-associated", "ecosystem_category": "Fish", "ecosystem_subtype": "Intestine", "ecosystem_type": "Digestive system", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:4968", "leaf_label": "Fecal", "organism_count": "9", "specific_ecosystem": "Fecal", "study_count": "0", "total_assertions": "9"}, "row": 552}] |
| EONT | data/raw/ontology_terms.tsv; TSV rows 13092 | supports | [{"data": {"definition": "Portion of semisolid bodily waste discharged through the anus[MW,modified].", "deprecated": "", "directly_referenced": "TRUE", "label": "feces", "label_only": "FALSE", "ontology": "UBERON", "synonyms": "cow dung&#124;cow pat&#124;droppings&#124;dung&#124;excrement&#124;excreta&#124;faeces&#124;fecal material&#124;fecal matter&#124;fewmet&#124;frass&#124;guano&#124;ordure&#124;piece of shit&#124;portion of dung&#124;portion of excrement&#124;portion of faeces&#124;portion of fecal material&#124;portion of fecal matter&#124;portion of feces&#124;portion of guano&#124;portion of scat&#124;portionem cacas&#124;scat&#124;spoor&#124;spraint&#124;stool", "term_id": "UBERON:0001988"}, "row": 13092}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 11287,11594 | supports | [{"data": {"object": "UBERON:0000174", "predicate": "rdfs:subClassOf", "subject": "UBERON:0001988"}, "row": 11287}, {"data": {"object": "UBERON:0001988", "predicate": "rdfs:subClassOf", "subject": "UBERON:0007109"}, "row": 11594}] |
| EDEC | curation/decisions.tsv; TSV rows 310 | supports | [{"data": {"category": "", "curator": "antigravity", "date": "2026-10-17", "decision": "CONFIRM_UNGROUNDED", "grounding_status": "", "identifier": "habitatmech:GOLD.227b8ef4a5", "notes": "ITEM curation: GOLD 'Host-associated &gt; Fish &gt; Digestive system &gt; Intestine &gt; Fecal' denotes fish fecal material rather than the intestine organ. Define under UBERON:0001988 (feces) with parent_mode REPLACE and exclude bare 'Fecal' (PMID 26696324; DOI:10.3389/fmicb.2015.01362). Path: Host-associated &gt; Fish &gt; Digestive system &gt; Intestine &gt; Fecal", "object_id": "", "object_label": "", "relation": "", "review_depth": "ITEM"}, "row": 310}] |
| ETR | curation/term_requests.tsv; TSV rows 177 | supports | [{"data": {"curator": "antigravity", "date": "2026-10-17", "definition": "A feces excreted from the intestine of a fish that contains undigested feed, mucus, and intestinal microorganisms.", "exact_synonym": "fish fecal material&#124;piscine feces", "identifier": "habitatmech:GOLD.227b8ef4a5", "notes": "ITEM curation: GOLD 'Host-associated &gt; Fish &gt; Digestive system &gt; Intestine &gt; Fecal' denotes fish fecal material rather than the intestine organ. Define under UBERON:0001988 (feces) with parent_mode REPLACE and exclude bare 'Fecal' (PMID 26696324; DOI:10.3389/fmicb.2015.01362). Path: Host-associated &gt; Fish &gt; Digestive system &gt; Intestine &gt; Fecal", "parent_class": "UBERON:0001988", "parent_label": "feces", "parent_mode": "REPLACE", "requested_label": "fish feces"}, "row": 177}] |
| ELE | curation/definition_source_label_exclusions.tsv; TSV rows 71 | supports | [{"data": {"curator": "antigravity", "date": "2026-10-17", "identifier": "habitatmech:GOLD.227b8ef4a5", "notes": "Displaced GOLD source label 'Fecal' in path 'Host-associated &gt; Fish &gt; Digestive system &gt; Intestine &gt; Fecal' is context-dependent, ambiguous, or names a host/disease/process rather than the defined habitat 'fish feces'; suppress automatic exact-synonym retention while preserving verbatim source provenance.", "requested_label": "fish feces", "source_label": "Fecal"}, "row": 71}] |
| EP1 | data/habitats/host_associated/feces.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": "Portion of semisolid bodily waste discharged through the anus[MW,modified].", "grounding_status": "EXACT", "identifier": "UBERON:0001988", "label": "feces", "mapping_status": "REVIEWED", "parent_habitats": ["ENVO:00002276", "UBERON:0000174", "UBERON:0001555", "habitatmech:GOLD.5b0aa7456c", "habitatmech:GOLD.6bda0871e2", "habitatmech:GOLD.b091b80314"], "source_attestations": [{"assertion_count": 2421, "assertion_unit": "STRAIN", "mapping_predicate": "skos:exactMatch", "source": "BACDIVE", "source_id": "bacdive.isolation_source:feces-stool", "source_label": "Feces-Stool"}, {"assertion_count": 13744, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:exactMatch", "source": "GOLD", "source_id": "gold.ecosystem:3920", "source_label": "Fecal", "source_path": "Host-associated &gt; Mammals: Human &gt; Digestive system &gt; Large intestine &gt; Fecal"}, {"assertion_count": 4785, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:exactMatch", "source": "GOLD", "source_id": "gold.ecosystem:4104", "source_label": "Fecal", "source_path": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Fecal"}, {"assertion_count": 1229, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:exactMatch", "source": "GOLD", "source_id": "gold.ecosystem:4957", "source_label": "Fecal", "source_path": "Host-associated &gt; Birds &gt; Digestive system &gt; Large intestine &gt; Fecal"}, {"assertion_count": 2, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:broadMatch", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:6471", "source_label": "Guano", "source_path": "Engineered &gt; Solid waste &gt; Animal waste &gt; Guano"}, {"assertion_count": 3, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:closeMatch", "source": "GOLD", "source_id": "gold.ecosystem:8175", "source_label": "Cast", "source_path": "Host-associated &gt; Annelida &gt; Digestive system &gt; Digestive tube &gt; Cast"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'fecal&#124;habitatmech:GOLD.227b8ef4a5' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal verified no prior target review bundle exists for this record; curation and history tables were inspected for all matching rows. |

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
review_id: 20261106T194833Z-fecal-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: fish feces (habitatmech:GOLD.227b8ef4a5)'
started_at: '2026-11-06T19:35:00Z'
finished_at: '2026-11-06T19:48:33Z'
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
summary: The minted GOLD record habitatmech:GOLD.227b8ef4a5 (fish feces in Host-associated
  > Fish > Digestive system > Intestine > Fecal, UNGROUNDED/REVIEWED, 9 ORGANISM assertions)
  is coherently defined under UBERON:0001988 (feces) with parent_mode REPLACE to exclude
  anatomical Intestine and displaced source label 'Fecal' omitted from synonyms (SOURCE_SYNONYM_EXCLUDED).
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
  - path: data/habitats/host_associated/fecal.yaml
    sha256: df3138e9f2794a49535d3df6c5b9a04006f755ac2cf9296e2027bc7714766a37
    role: target
  - path: data/habitats/host_associated/feces.yaml
    sha256: 8fc3ef983646fb278130da29b370d5448ac99af2762f66746aad06d187d3fddb
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
- target_id: habitatmech:GOLD.227b8ef4a5
  path: data/habitats/host_associated/fecal.yaml
  label: fish feces
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
  description: Scientific assessment of one exact generated target (data/habitats/host_associated/fecal.yaml)
    at captured main revision 355eb4a23118506c83a76cf22c6332d04decffec.
  selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/
    path order (excretory_system__22ee753c through fecal); this bundle assesses its
    single resolved identifier and source path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.227b8ef4a5
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
    --target-class HabitatRecord data/habitats/host_associated/fecal.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.227b8ef4a5
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
  - habitatmech:GOLD.227b8ef4a5
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
  - habitatmech:GOLD.227b8ef4a5
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
  - habitatmech:GOLD.227b8ef4a5
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
  - habitatmech:GOLD.227b8ef4a5
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
  - habitatmech:GOLD.227b8ef4a5
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
  - habitatmech:GOLD.227b8ef4a5
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
  - habitatmech:GOLD.227b8ef4a5
  summary: 'Completed 2026-11-06T19:47:55Z. OK_CANONICAL: 1203, OK_SYNONYM: 1, OK_EXCEPTION:
    5, SKIPPED_NO_ADAPTER: 2084. All id<->label pairs correspond.'
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/fecal.yaml
  locator: Entire YAML
  accessed_at: '2026-11-06T19:48:33Z'
  support: supports
  summary: All target fields, source attestations, synonyms, parent_habitats, and
    generated history for habitatmech:GOLD.227b8ef4a5 (fish feces) were read.
  snapshot_sha256: df3138e9f2794a49535d3df6c5b9a04006f755ac2cf9296e2027bc7714766a37
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-06T19:48:33Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon terms cannot substitute
    for associated environments; parent_habitats must be strictly broader across all
    contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-06T19:48:33Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-06T19:48:33Z'
  support: supports
  summary: Seed generator produces identifier=habitatmech:GOLD.227b8ef4a5, grounding_status=UNGROUNDED,
    mapping_status=REVIEWED, parent_habitats=["UBERON:0001988"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EGOLD
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV rows 552
  accessed_at: '2026-11-06T19:48:33Z'
  support: supports
  summary: '[{"data": {"biosample_count": "0", "canonical_path": "Host-associated
    > Fish > Digestive system > Intestine > Fecal", "depth": "5", "ecosystem": "Host-associated",
    "ecosystem_category": "Fish", "ecosystem_subtype": "Intestine", "ecosystem_type":
    "Digestive system", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:4968",
    "leaf_label": "Fecal", "organism_count": "9", "specific_ecosystem": "Fecal", "study_count":
    "0", "total_assertions": "9"}, "row": 552}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 13092
  accessed_at: '2026-11-06T19:48:33Z'
  support: supports
  summary: '[{"data": {"definition": "Portion of semisolid bodily waste discharged
    through the anus[MW,modified].", "deprecated": "", "directly_referenced": "TRUE",
    "label": "feces", "label_only": "FALSE", "ontology": "UBERON", "synonyms": "cow
    dung|cow pat|droppings|dung|excrement|excreta|faeces|fecal material|fecal matter|fewmet|frass|guano|ordure|piece
    of shit|portion of dung|portion of excrement|portion of faeces|portion of fecal
    material|portion of fecal matter|portion of feces|portion of guano|portion of
    scat|portionem cacas|scat|spoor|spraint|stool", "term_id": "UBERON:0001988"},
    "row": 13092}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 11287,11594
  accessed_at: '2026-11-06T19:48:33Z'
  support: supports
  summary: '[{"data": {"object": "UBERON:0000174", "predicate": "rdfs:subClassOf",
    "subject": "UBERON:0001988"}, "row": 11287}, {"data": {"object": "UBERON:0001988",
    "predicate": "rdfs:subClassOf", "subject": "UBERON:0007109"}, "row": 11594}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EDEC
  kind: database
  reference: curation/decisions.tsv
  locator: TSV rows 310
  accessed_at: '2026-11-06T19:48:33Z'
  support: supports
  summary: '[{"data": {"category": "", "curator": "antigravity", "date": "2026-10-17",
    "decision": "CONFIRM_UNGROUNDED", "grounding_status": "", "identifier": "habitatmech:GOLD.227b8ef4a5",
    "notes": "ITEM curation: GOLD ''Host-associated > Fish > Digestive system > Intestine
    > Fecal'' denotes fish fecal material rather than the intestine organ. Define
    under UBERON:0001988 (feces) with parent_mode REPLACE and exclude bare ''Fecal''
    (PMID 26696324; DOI:10.3389/fmicb.2015.01362). Path: Host-associated > Fish >
    Digestive system > Intestine > Fecal", "object_id": "", "object_label": "", "relation":
    "", "review_depth": "ITEM"}, "row": 310}]'
  snapshot_sha256: e39c962e767c655c22d6b1b5cf1cc392be3af21c2514e9c70d4c6105782d5650
- evidence_id: ETR
  kind: database
  reference: curation/term_requests.tsv
  locator: TSV rows 177
  accessed_at: '2026-11-06T19:48:33Z'
  support: supports
  summary: '[{"data": {"curator": "antigravity", "date": "2026-10-17", "definition":
    "A feces excreted from the intestine of a fish that contains undigested feed,
    mucus, and intestinal microorganisms.", "exact_synonym": "fish fecal material|piscine
    feces", "identifier": "habitatmech:GOLD.227b8ef4a5", "notes": "ITEM curation:
    GOLD ''Host-associated > Fish > Digestive system > Intestine > Fecal'' denotes
    fish fecal material rather than the intestine organ. Define under UBERON:0001988
    (feces) with parent_mode REPLACE and exclude bare ''Fecal'' (PMID 26696324; DOI:10.3389/fmicb.2015.01362).
    Path: Host-associated > Fish > Digestive system > Intestine > Fecal", "parent_class":
    "UBERON:0001988", "parent_label": "feces", "parent_mode": "REPLACE", "requested_label":
    "fish feces"}, "row": 177}]'
  snapshot_sha256: 72d7573cdee85f7cd54d27e2c864654b1f3b1121444c28b8d65e901edff9b053
- evidence_id: ELE
  kind: database
  reference: curation/definition_source_label_exclusions.tsv
  locator: TSV rows 71
  accessed_at: '2026-11-06T19:48:33Z'
  support: supports
  summary: '[{"data": {"curator": "antigravity", "date": "2026-10-17", "identifier":
    "habitatmech:GOLD.227b8ef4a5", "notes": "Displaced GOLD source label ''Fecal''
    in path ''Host-associated > Fish > Digestive system > Intestine > Fecal'' is context-dependent,
    ambiguous, or names a host/disease/process rather than the defined habitat ''fish
    feces''; suppress automatic exact-synonym retention while preserving verbatim
    source provenance.", "requested_label": "fish feces", "source_label": "Fecal"},
    "row": 71}]'
  snapshot_sha256: 725655426fded7f138d9a3e4e7a47eb1165f9a6a6a0d16cd242c07fcebfa0f8c
- evidence_id: EP1
  kind: record_content
  reference: data/habitats/host_associated/feces.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-11-06T19:48:33Z'
  support: supports
  summary: '{"definition": "Portion of semisolid bodily waste discharged through the
    anus[MW,modified].", "grounding_status": "EXACT", "identifier": "UBERON:0001988",
    "label": "feces", "mapping_status": "REVIEWED", "parent_habitats": ["ENVO:00002276",
    "UBERON:0000174", "UBERON:0001555", "habitatmech:GOLD.5b0aa7456c", "habitatmech:GOLD.6bda0871e2",
    "habitatmech:GOLD.b091b80314"], "source_attestations": [{"assertion_count": 2421,
    "assertion_unit": "STRAIN", "mapping_predicate": "skos:exactMatch", "source":
    "BACDIVE", "source_id": "bacdive.isolation_source:feces-stool", "source_label":
    "Feces-Stool"}, {"assertion_count": 13744, "assertion_unit": "ORGANISM", "mapping_predicate":
    "skos:exactMatch", "source": "GOLD", "source_id": "gold.ecosystem:3920", "source_label":
    "Fecal", "source_path": "Host-associated > Mammals: Human > Digestive system >
    Large intestine > Fecal"}, {"assertion_count": 4785, "assertion_unit": "ORGANISM",
    "mapping_predicate": "skos:exactMatch", "source": "GOLD", "source_id": "gold.ecosystem:4104",
    "source_label": "Fecal", "source_path": "Host-associated > Mammals > Digestive
    system > Large intestine > Fecal"}, {"assertion_count": 1229, "assertion_unit":
    "ORGANISM", "mapping_predicate": "skos:exactMatch", "source": "GOLD", "source_id":
    "gold.ecosystem:4957", "source_label": "Fecal", "source_path": "Host-associated
    > Birds > Digestive system > Large intestine > Fecal"}, {"assertion_count": 2,
    "assertion_unit": "ORGANISM", "mapping_predicate": "skos:broadMatch", "notes":
    "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.",
    "source": "GOLD", "source_id": "gold.ecosystem:6471", "source_label": "Guano",
    "source_path": "Engineered > Solid waste > Animal waste > Guano"}, {"assertion_count":
    3, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:closeMatch", "source":
    "GOLD", "source_id": "gold.ecosystem:8175", "source_label": "Cast", "source_path":
    "Host-associated > Annelida > Digestive system > Digestive tube > Cast"}]}'
  snapshot_sha256: 8fc3ef983646fb278130da29b370d5448ac99af2762f66746aad06d187d3fddb
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'fecal|habitatmech:GOLD.227b8ef4a5' reviews/structured/*/review.yaml
    curation/ history/
  accessed_at: '2026-11-06T19:48:33Z'
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
  - habitatmech:GOLD.227b8ef4a5
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: supported
  summary: The record defines fish feces under UBERON:0001988 (feces) with parent_mode
    REPLACE to exclude anatomical piscine Intestine (habitatmech:GOLD.79a0f12101),
    retains curated exact synonyms ('fish fecal material', 'piscine feces'), and omits
    displaced GOLD source label 'Fecal' from synonyms (SOURCE_SYNONYM_EXCLUDED) via
    curation/definition_source_label_exclusions.tsv.
  target_ids:
  - habitatmech:GOLD.227b8ef4a5
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
  - ELE
  - EP1
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks,
    and pools: [{"source": "GOLD", "count": 9, "unit": "ORGANISM"}]. Zero counts are
    omitted; unrelated parent counts are not combined.'
  target_ids:
  - habitatmech:GOLD.227b8ef4a5
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
  - ELE
  - EP1
- assessment_id: A4
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: Missing optional parameters/graphs are not evidence deficits. Full source
    decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only
    review does not mutate generated records.
  target_ids:
  - habitatmech:GOLD.227b8ef4a5
  evidence_ids:
  - E1
  - ESEED
  - ESCHEMA
findings: []
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
