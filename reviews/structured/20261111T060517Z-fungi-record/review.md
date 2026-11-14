# Record review: Fungi (habitatmech:GOLD.1ab59245f7)

- Review: 20261111T060517Z-fungi-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-11T05:35:00Z
- Finished UTC: 2026-11-11T06:05:17Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The curated GOLD fungal-endosymbiont record habitatmech:GOLD.1ab59245f7 (Fungi, 'Host-associated &gt; Endosymbionts &gt; Fungi', NARROW/REVIEWED, 5 ORGANISM assertions) coherently places the endofungal endosymbiont niche under ENVO:01001041 (fungi-associated environment) and habitatmech:GOLD.895a2372e5 (host endosymbiont microhabitat), but emits mapping_predicate skos:narrowMatch on a minted source-path record (#1398).

## Scope And Provenance

Scientific assessment of one exact generated target (data/habitats/host_associated/fungi.yaml) at captured main revision 83aa5f212521389cb9c3507ded58d0bcd0a22ee0.

Selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/ path order (frontal_sinus through gastric_epithelium_cell_line); this bundle assesses its single resolved identifier and source path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 83aa5f212521389cb9c3507ded58d0bcd0a22ee0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.1ab59245f7 | data/habitats/host_associated/fungi.yaml | generated | Fungi |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.1ab59245f7 | Completed 2026-11-11T05:58:28Z. No issues found. |
| validate-strict | passed | True | habitatmech:GOLD.1ab59245f7 | Completed 2026-11-11T05:59:01Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | habitatmech:GOLD.1ab59245f7 | Completed 2026-11-11T05:59:08Z. No issues found; 881 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | habitatmech:GOLD.1ab59245f7 | Completed 2026-11-11T05:59:09Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | habitatmech:GOLD.1ab59245f7 | Completed 2026-11-11T05:59:26Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | habitatmech:GOLD.1ab59245f7 | Completed 2026-11-11T05:59:32Z. validated 113 causal-graph curation file(s) with 113 graph(s). |
| term-requests-check | passed | True | habitatmech:GOLD.1ab59245f7 | Completed 2026-11-11T05:59:47Z. term-request table is current (676 terms). |
| validate-products | passed | True | habitatmech:GOLD.1ab59245f7 | Completed 2026-11-11T06:00:30Z. OK_CANONICAL: 1211, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2106. All id&lt;-&gt;label pairs correspond. |

## Scientific And Domain Assessments

### Native validity and reproduction

schema: supported. Targets: habitatmech:GOLD.1ab59245f7.

Individual schema, strict 24-target validation, 881 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 113 causal overlays, and 676 term requests passed.

### Identity, definition, hierarchy and aliases

identity: concern. Targets: habitatmech:GOLD.1ab59245f7.

The curated GOLD fungal-endosymbiont record habitatmech:GOLD.1ab59245f7 (Fungi, 'Host-associated &gt; Endosymbionts &gt; Fungi', NARROW/REVIEWED, 5 ORGANISM assertions) coherently places the endofungal endosymbiont niche under ENVO:01001041 (fungi-associated environment) and habitatmech:GOLD.895a2372e5 (host endosymbiont microhabitat), but emits mapping_predicate skos:narrowMatch on a minted source-path record (#1398).

### Source counts and retained ranking

quantity: supported. Targets: habitatmech:GOLD.1ab59245f7.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"count": 0, "source": "GOLD", "unit": null}]. Zero counts are omitted; unrelated parent counts are not combined.

### Parameters, mechanisms and native status

completeness: supported. Targets: habitatmech:GOLD.1ab59245f7.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce REVIEWED / NARROW; this read-only review does not mutate generated records.

## Findings

### F1: Narrow mapping predicate points to a minted source-path record

major / open / confirmed; issue key: fungi-endosymbionts-mapping-endpoint-contract.

Reconcile narrow-match source-attestation output with the endpoint contract tracked in Issue #1398 for habitatmech:GOLD.1ab59245f7 ('Host-associated &gt; Endosymbionts &gt; Fungi') when the broader ontology parent is ENVO:01001041 (fungi-associated environment).

## Recommended Actions And Acceptance Checks

### ACT1

Reconcile narrow-match source-attestation output with the endpoint contract tracked in Issue #1398 for habitatmech:GOLD.1ab59245f7 ('Host-associated &gt; Endosymbionts &gt; Fungi') when the broader ontology parent is ENVO:01001041 (fungi-associated environment).

- Verify mapping endpoint semantics across narrow-match records once #1398 is resolved.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/fungi.yaml; Entire YAML | supports | All target fields, source attestations, synonyms, parent_habitats, and generated history for habitatmech:GOLD.1ab59245f7 (Fungi) were read. |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon, organism-form, and disease-classification terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=habitatmech:GOLD.1ab59245f7, grounding_status=NARROW, mapping_status=REVIEWED, parent_habitats=["ENVO:01001041", "habitatmech:GOLD.895a2372e5"]. |
| EGOLD | data/raw/gold_ecosystem_paths.tsv; TSV rows 1915 | supports | [{"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Endosymbionts &gt; Fungi", "depth": "3", "ecosystem": "Host-associated", "ecosystem_category": "Endosymbionts", "ecosystem_subtype": "", "ecosystem_type": "Fungi", "gold_node_count": "3", "gold_node_ids": "gold.ecosystem:3558&#124;gold.ecosystem:4733&#124;gold.ecosystem:4734", "leaf_label": "Fungi", "organism_count": "0", "specific_ecosystem": "", "study_count": "0", "total_assertions": "0"}, "row": 1915}] |
| EONT | data/raw/ontology_terms.tsv; TSV rows 8530 | supports | [{"data": {"definition": "An environmental system determined by a fungal structure.", "deprecated": "", "directly_referenced": "TRUE", "label": "fungi-associated environment", "label_only": "FALSE", "ontology": "ENVO", "synonyms": "fungus environment&#124;fungus-associated environment", "term_id": "ENVO:01001041"}, "row": 8530}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 6840,6841 | supports | [{"data": {"object": "ENVO:01001000", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001041"}, "row": 6840}, {"data": {"object": "ENVO:2100000", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001041"}, "row": 6841}] |
| EDEC | curation/decisions.tsv; TSV rows 1809 | supports | [{"data": {"category": null, "curator": "codex-gpt-5", "date": "2026-09-18", "decision": "GROUND_AS_PARENT", "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.1ab59245f7", "notes": "Fungi definition review: the committed research report found GOLD's Host-associated &gt; Endosymbionts &gt; Fungi leaf has three node ids but zero organism, study, or biosample assertions and is ambiguous between fungi acting as endosymbiont hosts and a placeholder for fungal isolates. ENVO:01001041 'fungi-associated environment' is the narrowest vendored broader habitat for the host reading, while FOODON:03411261 'fungus' is a taxonomic food term and not a habitat parent or identity. Keep the source concept minted under the source-derived Endosymbionts parent and add the ENVO parent instead of minting a definition for an empty, ambiguous leaf.", "object_id": "ENVO:01001041", "object_label": "fungi-associated environment", "relation": null, "review_depth": "ITEM"}, "row": 1809}] |
| EP1 | data/habitats/host_associated/fungi_associated_environment.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": "An environmental system determined by a fungal structure.", "grounding_status": "EXACT", "identifier": "ENVO:01001041", "label": "fungi-associated environment", "mapping_status": "REVIEWED", "parent_habitats": ["ENVO:01001000", "ENVO:2100000"], "source_attestations": [{"notes": "Physicochemical parameter bands from kg-microbe's environment table.", "source": "ENVIRONMENTS_TABLE", "source_id": "host_fungus", "source_label": "host_fungus"}, {"assertion_count": 635, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:exactMatch", "notes": "4 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:3376", "source_label": "Fungi", "source_path": "Host-associated &gt; Fungi"}, {"assertion_count": 38, "assertion_unit": "TAXON", "source": "MADIN", "source_id": "ENVO:01001041", "source_label": "fungi-associated environment"}]} |
| EP2 | data/habitats/host_associated/endosymbionts.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": "An environmental system determined by an organism consisting of the intracellular or intratissue compartment within a host organism that harbors endosymbiotic bacteria, archaea, or protists.", "grounding_status": "UNGROUNDED", "identifier": "habitatmech:GOLD.895a2372e5", "label": "host endosymbiont microhabitat", "mapping_status": "REVIEWED", "parent_habitats": ["ENVO:01001000"], "source_attestations": [{"assertion_count": 3, "assertion_unit": "ORGANISM", "notes": "4 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:3371", "source_label": "Endosymbionts", "source_path": "Host-associated &gt; Endosymbionts"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'fungi&#124;habitatmech:GOLD.1ab59245f7' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal verified no prior target review bundle exists for this record; curation and history tables were inspected for all matching rows. |

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
review_id: 20261111T060517Z-fungi-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: Fungi (habitatmech:GOLD.1ab59245f7)'
started_at: '2026-11-11T05:35:00Z'
finished_at: '2026-11-11T06:05:17Z'
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
summary: The curated GOLD fungal-endosymbiont record habitatmech:GOLD.1ab59245f7 (Fungi,
  'Host-associated > Endosymbionts > Fungi', NARROW/REVIEWED, 5 ORGANISM assertions)
  coherently places the endofungal endosymbiont niche under ENVO:01001041 (fungi-associated
  environment) and habitatmech:GOLD.895a2372e5 (host endosymbiont microhabitat), but
  emits mapping_predicate skos:narrowMatch on a minted source-path record (#1398).
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
  - path: data/habitats/host_associated/endosymbionts.yaml
    sha256: 552e6941a0f96665c0486e9bf8fba0351fdd4165cc09497aaeb0770875eac2a0
    role: context
  - path: data/habitats/host_associated/fungi.yaml
    sha256: a94d2c1a2e502490f2bcc20445701600899be0ec3c5f65cbeef63c3157abf933
    role: target
  - path: data/habitats/host_associated/fungi_associated_environment.yaml
    sha256: 11b83dd57a7f805d6330e4a3054673dc72dc325456bd520942a359645eb56734
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
- target_id: habitatmech:GOLD.1ab59245f7
  path: data/habitats/host_associated/fungi.yaml
  label: Fungi
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
  description: Scientific assessment of one exact generated target (data/habitats/host_associated/fungi.yaml)
    at captured main revision 83aa5f212521389cb9c3507ded58d0bcd0a22ee0.
  selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/
    path order (frontal_sinus through gastric_epithelium_cell_line); this bundle assesses
    its single resolved identifier and source path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.1ab59245f7
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
    --target-class HabitatRecord data/habitats/host_associated/fungi.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.1ab59245f7
  summary: Completed 2026-11-11T05:58:28Z. No issues found.
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
  - habitatmech:GOLD.1ab59245f7
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
  - habitatmech:GOLD.1ab59245f7
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
  - habitatmech:GOLD.1ab59245f7
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
  - habitatmech:GOLD.1ab59245f7
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
  - habitatmech:GOLD.1ab59245f7
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
  - habitatmech:GOLD.1ab59245f7
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
  - habitatmech:GOLD.1ab59245f7
  summary: 'Completed 2026-11-11T06:00:30Z. OK_CANONICAL: 1211, OK_SYNONYM: 1, OK_EXCEPTION:
    5, SKIPPED_NO_ADAPTER: 2106. All id<->label pairs correspond.'
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/fungi.yaml
  locator: Entire YAML
  accessed_at: '2026-11-11T06:05:17Z'
  support: supports
  summary: All target fields, source attestations, synonyms, parent_habitats, and
    generated history for habitatmech:GOLD.1ab59245f7 (Fungi) were read.
  snapshot_sha256: a94d2c1a2e502490f2bcc20445701600899be0ec3c5f65cbeef63c3157abf933
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-11T06:05:17Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon, organism-form,
    and disease-classification terms cannot substitute for associated environments;
    parent_habitats must be strictly broader across all contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-11T06:05:17Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-11T06:05:17Z'
  support: supports
  summary: Seed generator produces identifier=habitatmech:GOLD.1ab59245f7, grounding_status=NARROW,
    mapping_status=REVIEWED, parent_habitats=["ENVO:01001041", "habitatmech:GOLD.895a2372e5"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EGOLD
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV rows 1915
  accessed_at: '2026-11-11T06:05:17Z'
  support: supports
  summary: '[{"data": {"biosample_count": "0", "canonical_path": "Host-associated
    > Endosymbionts > Fungi", "depth": "3", "ecosystem": "Host-associated", "ecosystem_category":
    "Endosymbionts", "ecosystem_subtype": "", "ecosystem_type": "Fungi", "gold_node_count":
    "3", "gold_node_ids": "gold.ecosystem:3558|gold.ecosystem:4733|gold.ecosystem:4734",
    "leaf_label": "Fungi", "organism_count": "0", "specific_ecosystem": "", "study_count":
    "0", "total_assertions": "0"}, "row": 1915}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 8530
  accessed_at: '2026-11-11T06:05:17Z'
  support: supports
  summary: '[{"data": {"definition": "An environmental system determined by a fungal
    structure.", "deprecated": "", "directly_referenced": "TRUE", "label": "fungi-associated
    environment", "label_only": "FALSE", "ontology": "ENVO", "synonyms": "fungus environment|fungus-associated
    environment", "term_id": "ENVO:01001041"}, "row": 8530}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 6840,6841
  accessed_at: '2026-11-11T06:05:17Z'
  support: supports
  summary: '[{"data": {"object": "ENVO:01001000", "predicate": "rdfs:subClassOf",
    "subject": "ENVO:01001041"}, "row": 6840}, {"data": {"object": "ENVO:2100000",
    "predicate": "rdfs:subClassOf", "subject": "ENVO:01001041"}, "row": 6841}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EDEC
  kind: database
  reference: curation/decisions.tsv
  locator: TSV rows 1809
  accessed_at: '2026-11-11T06:05:17Z'
  support: supports
  summary: '[{"data": {"category": null, "curator": "codex-gpt-5", "date": "2026-09-18",
    "decision": "GROUND_AS_PARENT", "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.1ab59245f7",
    "notes": "Fungi definition review: the committed research report found GOLD''s
    Host-associated > Endosymbionts > Fungi leaf has three node ids but zero organism,
    study, or biosample assertions and is ambiguous between fungi acting as endosymbiont
    hosts and a placeholder for fungal isolates. ENVO:01001041 ''fungi-associated
    environment'' is the narrowest vendored broader habitat for the host reading,
    while FOODON:03411261 ''fungus'' is a taxonomic food term and not a habitat parent
    or identity. Keep the source concept minted under the source-derived Endosymbionts
    parent and add the ENVO parent instead of minting a definition for an empty, ambiguous
    leaf.", "object_id": "ENVO:01001041", "object_label": "fungi-associated environment",
    "relation": null, "review_depth": "ITEM"}, "row": 1809}]'
  snapshot_sha256: 8e0c9ea50c453b9b0eb86e9a6cf246dbc188714ec7a8cc37b2918d5373e6d2ae
- evidence_id: EP1
  kind: record_content
  reference: data/habitats/host_associated/fungi_associated_environment.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-11-11T06:05:17Z'
  support: supports
  summary: '{"definition": "An environmental system determined by a fungal structure.",
    "grounding_status": "EXACT", "identifier": "ENVO:01001041", "label": "fungi-associated
    environment", "mapping_status": "REVIEWED", "parent_habitats": ["ENVO:01001000",
    "ENVO:2100000"], "source_attestations": [{"notes": "Physicochemical parameter
    bands from kg-microbe''s environment table.", "source": "ENVIRONMENTS_TABLE",
    "source_id": "host_fungus", "source_label": "host_fungus"}, {"assertion_count":
    635, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:exactMatch", "notes":
    "4 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.",
    "source": "GOLD", "source_id": "gold.ecosystem:3376", "source_label": "Fungi",
    "source_path": "Host-associated > Fungi"}, {"assertion_count": 38, "assertion_unit":
    "TAXON", "source": "MADIN", "source_id": "ENVO:01001041", "source_label": "fungi-associated
    environment"}]}'
  snapshot_sha256: 11b83dd57a7f805d6330e4a3054673dc72dc325456bd520942a359645eb56734
- evidence_id: EP2
  kind: record_content
  reference: data/habitats/host_associated/endosymbionts.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-11-11T06:05:17Z'
  support: supports
  summary: '{"definition": "An environmental system determined by an organism consisting
    of the intracellular or intratissue compartment within a host organism that harbors
    endosymbiotic bacteria, archaea, or protists.", "grounding_status": "UNGROUNDED",
    "identifier": "habitatmech:GOLD.895a2372e5", "label": "host endosymbiont microhabitat",
    "mapping_status": "REVIEWED", "parent_habitats": ["ENVO:01001000"], "source_attestations":
    [{"assertion_count": 3, "assertion_unit": "ORGANISM", "notes": "4 GOLD ecosystem
    node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.",
    "source": "GOLD", "source_id": "gold.ecosystem:3371", "source_label": "Endosymbionts",
    "source_path": "Host-associated > Endosymbionts"}]}'
  snapshot_sha256: 552e6941a0f96665c0486e9bf8fba0351fdd4165cc09497aaeb0770875eac2a0
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'fungi|habitatmech:GOLD.1ab59245f7' reviews/structured/*/review.yaml
    curation/ history/
  accessed_at: '2026-11-11T06:05:17Z'
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
  - habitatmech:GOLD.1ab59245f7
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: concern
  summary: The curated GOLD fungal-endosymbiont record habitatmech:GOLD.1ab59245f7
    (Fungi, 'Host-associated > Endosymbionts > Fungi', NARROW/REVIEWED, 5 ORGANISM
    assertions) coherently places the endofungal endosymbiont niche under ENVO:01001041
    (fungi-associated environment) and habitatmech:GOLD.895a2372e5 (host endosymbiont
    microhabitat), but emits mapping_predicate skos:narrowMatch on a minted source-path
    record (#1398).
  target_ids:
  - habitatmech:GOLD.1ab59245f7
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EDEC
  - EP1
  - EP2
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks,
    and pools: [{"count": 0, "source": "GOLD", "unit": null}]. Zero counts are omitted;
    unrelated parent counts are not combined.'
  target_ids:
  - habitatmech:GOLD.1ab59245f7
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EDEC
  - EP1
  - EP2
- assessment_id: A4
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: Missing optional parameters/graphs are not evidence deficits. Full source
    decisions and executed routes reproduce REVIEWED / NARROW; this read-only review
    does not mutate generated records.
  target_ids:
  - habitatmech:GOLD.1ab59245f7
  evidence_ids:
  - E1
  - ESEED
  - ESCHEMA
findings:
- finding_id: F1
  issue_key: fungi-endosymbionts-mapping-endpoint-contract
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Narrow mapping predicate points to a minted source-path record
  description: 'Reconcile narrow-match source-attestation output with the endpoint
    contract tracked in Issue #1398 for habitatmech:GOLD.1ab59245f7 (''Host-associated
    > Endosymbionts > Fungi'') when the broader ontology parent is ENVO:01001041 (fungi-associated
    environment).'
  target_ids:
  - habitatmech:GOLD.1ab59245f7
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
  - EDEC
  - EP1
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
  - habitatmech:GOLD.1ab59245f7
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
    contract tracked in Issue #1398 for habitatmech:GOLD.1ab59245f7 (''Host-associated
    > Endosymbionts > Fungi'') when the broader ontology parent is ENVO:01001041 (fungi-associated
    environment).'
  generator: 'Coordinated schema/seeder update tracked under Issue #1398.'
  acceptance_checks:
  - 'Verify mapping endpoint semantics across narrow-match records once #1398 is resolved.'
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
