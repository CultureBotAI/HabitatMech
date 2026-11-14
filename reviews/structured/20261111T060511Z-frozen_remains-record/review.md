# Record review: frozen avian remains (habitatmech:GOLD.112979e260)

- Review: 20261111T060511Z-frozen_remains-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-11T05:35:00Z
- Finished UTC: 2026-11-11T06:05:11Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The curated GOLD frozen-remains record habitatmech:GOLD.112979e260 (frozen avian remains, 'Host-associated &gt; Birds &gt; Remains &gt; Frozen remains', UNGROUNDED/REVIEWED) is coherently defined under ENVO:00002033 (carcass) with parent_mode REPLACE and source-label exclusion for bare 'Frozen remains'.

## Scope And Provenance

Scientific assessment of one exact generated target (data/habitats/host_associated/frozen_remains.yaml) at captured main revision 83aa5f212521389cb9c3507ded58d0bcd0a22ee0.

Selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/ path order (frontal_sinus through gastric_epithelium_cell_line); this bundle assesses its single resolved identifier and source path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 83aa5f212521389cb9c3507ded58d0bcd0a22ee0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.112979e260 | data/habitats/host_associated/frozen_remains.yaml | generated | frozen avian remains |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.112979e260 | Completed 2026-11-11T05:58:18Z. No issues found. |
| validate-strict | passed | True | habitatmech:GOLD.112979e260 | Completed 2026-11-11T05:59:01Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | habitatmech:GOLD.112979e260 | Completed 2026-11-11T05:59:08Z. No issues found; 881 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | habitatmech:GOLD.112979e260 | Completed 2026-11-11T05:59:09Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | habitatmech:GOLD.112979e260 | Completed 2026-11-11T05:59:26Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | habitatmech:GOLD.112979e260 | Completed 2026-11-11T05:59:32Z. validated 113 causal-graph curation file(s) with 113 graph(s). |
| term-requests-check | passed | True | habitatmech:GOLD.112979e260 | Completed 2026-11-11T05:59:47Z. term-request table is current (676 terms). |
| validate-products | passed | True | habitatmech:GOLD.112979e260 | Completed 2026-11-11T06:00:30Z. OK_CANONICAL: 1211, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2106. All id&lt;-&gt;label pairs correspond. |

## Scientific And Domain Assessments

### Native validity and reproduction

schema: supported. Targets: habitatmech:GOLD.112979e260.

Individual schema, strict 24-target validation, 881 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 113 causal overlays, and 676 term requests passed.

### Identity, definition, hierarchy and aliases

identity: supported. Targets: habitatmech:GOLD.112979e260.

The curated GOLD frozen-remains record habitatmech:GOLD.112979e260 (frozen avian remains, 'Host-associated &gt; Birds &gt; Remains &gt; Frozen remains', UNGROUNDED/REVIEWED) is coherently defined under ENVO:00002033 (carcass) with parent_mode REPLACE and source-label exclusion for bare 'Frozen remains'.

### Source counts and retained ranking

quantity: supported. Targets: habitatmech:GOLD.112979e260.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"count": 0, "source": "GOLD", "unit": null}]. Zero counts are omitted; unrelated parent counts are not combined.

### Parameters, mechanisms and native status

completeness: supported. Targets: habitatmech:GOLD.112979e260.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only review does not mutate generated records.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/frozen_remains.yaml; Entire YAML | supports | All target fields, source attestations, synonyms, parent_habitats, and generated history for habitatmech:GOLD.112979e260 (frozen avian remains) were read. |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon, organism-form, and disease-classification terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=habitatmech:GOLD.112979e260, grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["ENVO:00002033"]. |
| EGOLD | data/raw/gold_ecosystem_paths.tsv; TSV rows 1897 | supports | [{"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Birds &gt; Remains &gt; Frozen remains", "depth": "4", "ecosystem": "Host-associated", "ecosystem_category": "Birds", "ecosystem_subtype": "Frozen remains", "ecosystem_type": "Remains", "gold_node_count": "2", "gold_node_ids": "gold.ecosystem:7508&#124;gold.ecosystem:7509", "leaf_label": "Frozen remains", "organism_count": "0", "specific_ecosystem": "", "study_count": "0", "total_assertions": "0"}, "row": 1897}] |
| EONT | data/raw/ontology_terms.tsv; TSV rows 7177 | supports | [{"data": {"definition": "The dead body of an animal.", "deprecated": "", "directly_referenced": "TRUE", "label": "carcass", "label_only": "FALSE", "ontology": "ENVO", "synonyms": "corpse", "term_id": "ENVO:00002033"}, "row": 7177}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 5283,5790 | supports | [{"data": {"object": "ENVO:01001814", "predicate": "rdfs:subClassOf", "subject": "ENVO:00002033"}, "row": 5283}, {"data": {"object": "ENVO:00002033", "predicate": "rdfs:subClassOf", "subject": "ENVO:01000139"}, "row": 5790}] |
| EDEC | curation/decisions.tsv; TSV rows 208 | supports | [{"data": {"category": "", "curator": "antigravity", "date": "2026-10-17", "decision": "CONFIRM_UNGROUNDED", "grounding_status": "", "identifier": "habitatmech:GOLD.112979e260", "notes": "Defined frozen avian remains under ENVO:00002033 'carcass'; supported by permafrost and frozen vertebrate remains microbiology (PMID 26659141).", "object_id": "", "object_label": "", "relation": "", "review_depth": "ITEM"}, "row": 208}] |
| ETREQ | curation/term_requests.tsv; TSV rows 565 | supports | [{"data": {"curator": "antigravity", "date": "2026-10-17", "definition": "A carcass of a bird preserved at subfreezing temperatures in ice, permafrost, or cold storage, retaining cryotolerant and post-mortem microorganisms.", "exact_synonym": "frozen bird carcass", "identifier": "habitatmech:GOLD.112979e260", "notes": "Defined frozen avian remains under ENVO:00002033 'carcass'; supported by permafrost and frozen vertebrate remains microbiology (PMID 26659141).", "parent_class": "ENVO:00002033", "parent_label": "carcass", "parent_mode": "REPLACE", "requested_label": "frozen avian remains"}, "row": 565}] |
| EDEFEXCL | curation/definition_source_label_exclusions.tsv; TSV rows 318 | supports | [{"data": {"curator": "antigravity", "date": "2026-10-17", "identifier": "habitatmech:GOLD.112979e260", "notes": "Displaced GOLD source label 'Frozen remains' in path 'Host-associated &gt; Birds &gt; Remains &gt; Frozen remains' is context-dependent, ambiguous, or names a host/disease/process rather than the defined habitat 'frozen avian remains'; suppress automatic exact-synonym retention while preserving verbatim source provenance.", "requested_label": "frozen avian remains", "source_label": "Frozen remains"}, "row": 318}] |
| EP1 | data/habitats/other/carcass__24623a85.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": "The dead body of an animal.", "grounding_status": "EXACT", "identifier": "ENVO:00002033", "label": "carcass", "mapping_status": "REVIEWED", "parent_habitats": ["ENVO:01001814"], "source_attestations": [{"assertion_count": 60, "assertion_unit": "STRAIN", "mapping_predicate": "skos:closeMatch", "source": "BACDIVE", "source_id": "bacdive.isolation_source:decomposing-animal", "source_label": "Decomposing-animal"}, {"assertion_count": 1, "assertion_unit": "TAXON", "evidence_channels": "annotated_genomes_isolates", "score": 3.0, "source": "PREGO", "source_id": "ENVO:00002033", "source_label": "carcass"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'frozen_remains&#124;habitatmech:GOLD.112979e260' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal verified no prior target review bundle exists for this record; curation and history tables were inspected for all matching rows. |

## Limits And Additional Notes

- Only the cited repository inputs, ontology terms, and source inventories were inspected; original specimen-level support for every upstream source assertion was not exhaustively reconstructed.
- Source counts, PREGO scores, and ranks are not prevalence, viability, mechanism, or characteristic presence.
- Configured label correspondence skipped 2,106 no-adapter pairs; this is not whole-corpus identifier certification.
- Read-only review: no curation table, generated habitat YAML, status, or history record was modified.
- All target and context inputs were captured at clean git commit 83aa5f212521389cb9c3507ded58d0bcd0a22ee0.
- Structured-review archive traversal confirmed no prior target review bundle exists for this record.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261111T060511Z-frozen_remains-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: frozen avian remains (habitatmech:GOLD.112979e260)'
started_at: '2026-11-11T05:35:00Z'
finished_at: '2026-11-11T06:05:11Z'
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
summary: The curated GOLD frozen-remains record habitatmech:GOLD.112979e260 (frozen
  avian remains, 'Host-associated > Birds > Remains > Frozen remains', UNGROUNDED/REVIEWED)
  is coherently defined under ENVO:00002033 (carcass) with parent_mode REPLACE and
  source-label exclusion for bare 'Frozen remains'.
source:
  git_revision: 83aa5f212521389cb9c3507ded58d0bcd0a22ee0
  state: git_commit
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
  - path: data/habitats/host_associated/frozen_remains.yaml
    sha256: 84ac3b30e18b8b0175ad85c9703920c043980ba2d87e1c5c3f0efdb5400dd8cd
    role: target
  - path: data/habitats/other/carcass__24623a85.yaml
    sha256: 9cce81df5671b106fb73e3dd58815969461bcf2c9d363d211ef1fe6c53eb6dfc
    role: context
  - path: data/raw/bacdive_isolation_sources.tsv
    sha256: fb1645dd899a43130be9cf38b0e8b27ffbaa0175306917bff20e20ee225875fc
    role: context
  - path: data/raw/environment_parameters.tsv
    sha256: a75d0f565d8ee2498188ff98b17d0ab325ae4f782601bf4414eff6e86c13e0f9
    role: context
  - path: data/raw/gold_ecosystem_paths.tsv
    sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
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
- target_id: habitatmech:GOLD.112979e260
  path: data/habitats/host_associated/frozen_remains.yaml
  label: frozen avian remains
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
  description: Scientific assessment of one exact generated target (data/habitats/host_associated/frozen_remains.yaml)
    at captured main revision 83aa5f212521389cb9c3507ded58d0bcd0a22ee0.
  selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/
    path order (frontal_sinus through gastric_epithelium_cell_line); this bundle assesses
    its single resolved identifier and source path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.112979e260
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
    --target-class HabitatRecord data/habitats/host_associated/frozen_remains.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.112979e260
  summary: Completed 2026-11-11T05:58:18Z. No issues found.
  scope_note: Individual schema; strict command covers the 24 named cohort targets;
    other documented gates have full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/habitats/host_associated/frontal_sinus.yaml
    data/habitats/host_associated/frozen_remains.yaml data/habitats/host_associated/frozen_remains__584db35c.yaml
    data/habitats/host_associated/frozen_remains__aa25d597.yaml data/habitats/host_associated/fruit.yaml
    data/habitats/host_associated/fruit_juice.yaml data/habitats/host_associated/fruiting_body.yaml
    data/habitats/host_associated/fungi.yaml data/habitats/host_associated/fungi_associated_environment.yaml
    data/habitats/host_associated/g_cell.yaml data/habitats/host_associated/gall_bladder.yaml
    data/habitats/host_associated/gallbladder.yaml data/habitats/host_associated/gallbladder__d157697c.yaml
    data/habitats/host_associated/gallbladder_stones.yaml data/habitats/host_associated/gallbladder_stones__a31ee838.yaml
    data/habitats/host_associated/galls.yaml data/habitats/host_associated/gametophyte.yaml
    data/habitats/host_associated/ganglion.yaml data/habitats/host_associated/gaster.yaml
    data/habitats/host_associated/gastric_caeca.yaml data/habitats/host_associated/gastric_caeca__12108999.yaml
    data/habitats/host_associated/gastric_carcinoma.yaml data/habitats/host_associated/gastric_epithelium.yaml
    data/habitats/host_associated/gastric_epithelium_cell_line.yaml --out .temp/c9s4_24_strict.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.112979e260
  summary: 'Completed 2026-11-11T05:59:01Z. Validated 24 files; files with ERROR:
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
  - habitatmech:GOLD.112979e260
  summary: Completed 2026-11-11T05:59:08Z. No issues found; 881 history record(s)
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
  - habitatmech:GOLD.112979e260
  summary: 'Completed 2026-11-11T05:59:09Z. provenance current: 14 committed inventories,
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
  - habitatmech:GOLD.112979e260
  summary: 'Completed 2026-11-11T05:59:26Z. expected 3209 records, found 3209 on disk;
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
  - habitatmech:GOLD.112979e260
  summary: Completed 2026-11-11T05:59:32Z. validated 113 causal-graph curation file(s)
    with 113 graph(s).
  scope_note: Full-corpus causal-graph overlay validation.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: .venv/bin/python scripts/build_term_requests.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.112979e260
  summary: Completed 2026-11-11T05:59:47Z. term-request table is current (676 terms).
  scope_note: Full-corpus term-request table currency check.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.112979e260
  summary: 'Completed 2026-11-11T06:00:30Z. OK_CANONICAL: 1211, OK_SYNONYM: 1, OK_EXCEPTION:
    5, SKIPPED_NO_ADAPTER: 2106. All id<->label pairs correspond.'
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/frozen_remains.yaml
  locator: Entire YAML
  accessed_at: '2026-11-11T06:05:11Z'
  support: supports
  summary: All target fields, source attestations, synonyms, parent_habitats, and
    generated history for habitatmech:GOLD.112979e260 (frozen avian remains) were
    read.
  snapshot_sha256: 84ac3b30e18b8b0175ad85c9703920c043980ba2d87e1c5c3f0efdb5400dd8cd
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-11T06:05:11Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon, organism-form,
    and disease-classification terms cannot substitute for associated environments;
    parent_habitats must be strictly broader across all contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-11T06:05:11Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-11T06:05:11Z'
  support: supports
  summary: Seed generator produces identifier=habitatmech:GOLD.112979e260, grounding_status=UNGROUNDED,
    mapping_status=REVIEWED, parent_habitats=["ENVO:00002033"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EGOLD
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV rows 1897
  accessed_at: '2026-11-11T06:05:11Z'
  support: supports
  summary: '[{"data": {"biosample_count": "0", "canonical_path": "Host-associated
    > Birds > Remains > Frozen remains", "depth": "4", "ecosystem": "Host-associated",
    "ecosystem_category": "Birds", "ecosystem_subtype": "Frozen remains", "ecosystem_type":
    "Remains", "gold_node_count": "2", "gold_node_ids": "gold.ecosystem:7508|gold.ecosystem:7509",
    "leaf_label": "Frozen remains", "organism_count": "0", "specific_ecosystem": "",
    "study_count": "0", "total_assertions": "0"}, "row": 1897}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 7177
  accessed_at: '2026-11-11T06:05:11Z'
  support: supports
  summary: '[{"data": {"definition": "The dead body of an animal.", "deprecated":
    "", "directly_referenced": "TRUE", "label": "carcass", "label_only": "FALSE",
    "ontology": "ENVO", "synonyms": "corpse", "term_id": "ENVO:00002033"}, "row":
    7177}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 5283,5790
  accessed_at: '2026-11-11T06:05:11Z'
  support: supports
  summary: '[{"data": {"object": "ENVO:01001814", "predicate": "rdfs:subClassOf",
    "subject": "ENVO:00002033"}, "row": 5283}, {"data": {"object": "ENVO:00002033",
    "predicate": "rdfs:subClassOf", "subject": "ENVO:01000139"}, "row": 5790}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EDEC
  kind: database
  reference: curation/decisions.tsv
  locator: TSV rows 208
  accessed_at: '2026-11-11T06:05:11Z'
  support: supports
  summary: '[{"data": {"category": "", "curator": "antigravity", "date": "2026-10-17",
    "decision": "CONFIRM_UNGROUNDED", "grounding_status": "", "identifier": "habitatmech:GOLD.112979e260",
    "notes": "Defined frozen avian remains under ENVO:00002033 ''carcass''; supported
    by permafrost and frozen vertebrate remains microbiology (PMID 26659141).", "object_id":
    "", "object_label": "", "relation": "", "review_depth": "ITEM"}, "row": 208}]'
  snapshot_sha256: 8e0c9ea50c453b9b0eb86e9a6cf246dbc188714ec7a8cc37b2918d5373e6d2ae
- evidence_id: ETREQ
  kind: database
  reference: curation/term_requests.tsv
  locator: TSV rows 565
  accessed_at: '2026-11-11T06:05:11Z'
  support: supports
  summary: '[{"data": {"curator": "antigravity", "date": "2026-10-17", "definition":
    "A carcass of a bird preserved at subfreezing temperatures in ice, permafrost,
    or cold storage, retaining cryotolerant and post-mortem microorganisms.", "exact_synonym":
    "frozen bird carcass", "identifier": "habitatmech:GOLD.112979e260", "notes": "Defined
    frozen avian remains under ENVO:00002033 ''carcass''; supported by permafrost
    and frozen vertebrate remains microbiology (PMID 26659141).", "parent_class":
    "ENVO:00002033", "parent_label": "carcass", "parent_mode": "REPLACE", "requested_label":
    "frozen avian remains"}, "row": 565}]'
  snapshot_sha256: 3703ae74d7565abdfb5a1fab47718b05c4fd02447b4ed60bbeb3bde65e1d8792
- evidence_id: EDEFEXCL
  kind: database
  reference: curation/definition_source_label_exclusions.tsv
  locator: TSV rows 318
  accessed_at: '2026-11-11T06:05:11Z'
  support: supports
  summary: '[{"data": {"curator": "antigravity", "date": "2026-10-17", "identifier":
    "habitatmech:GOLD.112979e260", "notes": "Displaced GOLD source label ''Frozen
    remains'' in path ''Host-associated > Birds > Remains > Frozen remains'' is context-dependent,
    ambiguous, or names a host/disease/process rather than the defined habitat ''frozen
    avian remains''; suppress automatic exact-synonym retention while preserving verbatim
    source provenance.", "requested_label": "frozen avian remains", "source_label":
    "Frozen remains"}, "row": 318}]'
  snapshot_sha256: 84e5214713a21033312eb9c512fe38f44865662f934a4e679d45e827b16ff780
- evidence_id: EP1
  kind: record_content
  reference: data/habitats/other/carcass__24623a85.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-11-11T06:05:11Z'
  support: supports
  summary: '{"definition": "The dead body of an animal.", "grounding_status": "EXACT",
    "identifier": "ENVO:00002033", "label": "carcass", "mapping_status": "REVIEWED",
    "parent_habitats": ["ENVO:01001814"], "source_attestations": [{"assertion_count":
    60, "assertion_unit": "STRAIN", "mapping_predicate": "skos:closeMatch", "source":
    "BACDIVE", "source_id": "bacdive.isolation_source:decomposing-animal", "source_label":
    "Decomposing-animal"}, {"assertion_count": 1, "assertion_unit": "TAXON", "evidence_channels":
    "annotated_genomes_isolates", "score": 3.0, "source": "PREGO", "source_id": "ENVO:00002033",
    "source_label": "carcass"}]}'
  snapshot_sha256: 9cce81df5671b106fb73e3dd58815969461bcf2c9d363d211ef1fe6c53eb6dfc
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'frozen_remains|habitatmech:GOLD.112979e260' reviews/structured/*/review.yaml
    curation/ history/
  accessed_at: '2026-11-11T06:05:11Z'
  support: context_only
  summary: Structured-review traversal verified no prior target review bundle exists
    for this record; curation and history tables were inspected for all matching rows.
  search_scope: curation, history, data/raw, and reviews/structured/*/review.yaml
    traversal at commit 83aa5f212521389cb9c3507ded58d0bcd0a22ee0.
assessments:
- assessment_id: A1
  area: schema
  topic: Native validity and reproduction
  outcome: supported
  summary: Individual schema, strict 24-target validation, 881 history records, 14
    inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 113 causal
    overlays, and 676 term requests passed.
  target_ids:
  - habitatmech:GOLD.112979e260
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: supported
  summary: The curated GOLD frozen-remains record habitatmech:GOLD.112979e260 (frozen
    avian remains, 'Host-associated > Birds > Remains > Frozen remains', UNGROUNDED/REVIEWED)
    is coherently defined under ENVO:00002033 (carcass) with parent_mode REPLACE and
    source-label exclusion for bare 'Frozen remains'.
  target_ids:
  - habitatmech:GOLD.112979e260
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EDEC
  - ETREQ
  - EDEFEXCL
  - EP1
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks,
    and pools: [{"count": 0, "source": "GOLD", "unit": null}]. Zero counts are omitted;
    unrelated parent counts are not combined.'
  target_ids:
  - habitatmech:GOLD.112979e260
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EDEC
  - ETREQ
  - EDEFEXCL
  - EP1
- assessment_id: A4
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: Missing optional parameters/graphs are not evidence deficits. Full source
    decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only
    review does not mutate generated records.
  target_ids:
  - habitatmech:GOLD.112979e260
  evidence_ids:
  - E1
  - ESEED
  - ESCHEMA
findings: []
actions: []
limitations:
- Only the cited repository inputs, ontology terms, and source inventories were inspected;
  original specimen-level support for every upstream source assertion was not exhaustively
  reconstructed.
- Source counts, PREGO scores, and ranks are not prevalence, viability, mechanism,
  or characteristic presence.
- Configured label correspondence skipped 2,106 no-adapter pairs; this is not whole-corpus
  identifier certification.
- 'Read-only review: no curation table, generated habitat YAML, status, or history
  record was modified.'
notes:
- All target and context inputs were captured at clean git commit 83aa5f212521389cb9c3507ded58d0bcd0a22ee0.
- Structured-review archive traversal confirmed no prior target review bundle exists
  for this record.
tags:
- individual-scientific-review
- host-associated
```
