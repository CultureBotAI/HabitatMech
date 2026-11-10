# Remediation review: flagellum

- Review: 20261109T215003Z-flagellum-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-09T21:40:00Z
- Finished UTC: 2026-11-09T21:50:03Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reclassified PREGO source concept habitatmech:PREGO.267811fd7a (BTO:0002292 'flagellum') via an ITEM-level NOT_APPLICABLE decision (target_id=BTO:0002292 'flagellum', relation=xref) in curation/decisions.tsv (#2334). This replaces cellular organelle identity BTO:0002292 with minted identifier habitatmech:PREGO.267811fd7a (REVIEWED/NOT_APPLICABLE), removes organismal form parent BTO:0000464 (flagellate) from parent_habitats, preserves BTO:0002292 as a contextual xref, and retains all 140 PREGO TAXON assertions and 25 retained characteristic_taxa rows. Both predecessor findings (F1 and F2) are resolved.

## Scope And Provenance

Full current target assessment and explicit disposition of every baseline finding on data/habitats/host_associated/flagellum.yaml after bounded Cycle 8 Stage 5 remediation.

Selection: One of thirteen repaired targets from the finger-through-free_living_state cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c82566b001f676eb0d3c9cc6c905f85a99b8bde.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:PREGO.267811fd7a | data/habitats/host_associated/flagellum.yaml | generated | flagella |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:PREGO.267811fd7a | Completed 2026-11-09T21:48:00Z. No issues found against src/habitatmech/schema/habitatmech.yaml. |
| validate-strict | passed | True | habitatmech:PREGO.267811fd7a | Completed 2026-11-09T21:48:05Z. 24 checked, 0 failed; target passed closed-schema validation. |
| validate-history | passed | True | habitatmech:PREGO.267811fd7a | Completed 2026-11-09T21:48:10Z. No issues found; 879 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | habitatmech:PREGO.267811fd7a | Completed 2026-11-09T21:48:15Z. 14 inventory files and 2 GOLD export files verified. |
| verify-corpus | passed | True | habitatmech:PREGO.267811fd7a | Completed 2026-11-09T21:48:25Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | habitatmech:PREGO.267811fd7a | Completed 2026-11-09T21:48:30Z. 103 causal-graph curations and target records validated. |
| term-requests-check | passed | True | habitatmech:PREGO.267811fd7a | Completed 2026-11-09T21:48:35Z. term-request table is current (676 terms). |
| validate-products | passed | True | habitatmech:PREGO.267811fd7a | Completed 2026-11-09T21:48:45Z. 24 records, 0 label drift findings. |
| pytest counterfactual review repairs | passed | True | habitatmech:PREGO.267811fd7a | Completed 2026-11-09T21:49:00Z. 2 passed; exact 13-record counterfactual diff verified. |
| curation-floor | passed | True | habitatmech:PREGO.267811fd7a | Completed 2026-11-09T21:49:05Z. Floor satisfied across all 13 metrics. |
| render-check | passed | True | habitatmech:PREGO.267811fd7a | Completed 2026-11-09T21:49:30Z. rendered 3209 habitat pages, 757 redirect stubs, 8 categories, 701 term requests; pages/ is in step with the corpus. |

## Scientific And Domain Assessments

### Native validity and reproduction after bounded remediation

schema: supported. Targets: habitatmech:PREGO.267811fd7a.

Individual schema, strict 24-target validation, 879 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 103 causal overlays, 676 term requests, curation floor, site parity, and counterfactual regression tests passed.

### Identity, definition, hierarchy and aliases

identity: supported. Targets: habitatmech:PREGO.267811fd7a.

habitatmech:PREGO.267811fd7a: flagella; NOT_APPLICABLE/REVIEWED; parents []. Reclassified PREGO source concept habitatmech:PREGO.267811fd7a (BTO:0002292 'flagellum') via an ITEM-level NOT_APPLICABLE decision (target_id=BTO:0002292 'flagellum', relation=xref) in curation/decisions.tsv (#2334). This replaces cellular organelle identity BTO:0002292 with minted identifier habitatmech:PREGO.267811fd7a (REVIEWED/NOT_APPLICABLE), removes organismal form parent BTO:0000464 (flagellate) from parent_habitats, preserves BTO:0002292 as a contextual xref, and retains all 140 PREGO TAXON assertions and 25 retained characteristic_taxa rows. Both predecessor findings (F1 and F2) are resolved.

### Source counts and retained ranking

quantity: supported. Targets: habitatmech:PREGO.267811fd7a.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"count": 140, "source": "PREGO", "unit": "TAXON"}]. Zero counts are omitted; unrelated parent counts are not combined.

### Predecessor finding reconciliation

representation: supported. Targets: habitatmech:PREGO.267811fd7a.

Every predecessor finding preserves its stable issue_key and exact lineage. All predecessor findings in this target scope are resolved.

### Parameters, mechanisms and native status

completeness: supported. Targets: habitatmech:PREGO.267811fd7a.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce REVIEWED / NOT_APPLICABLE; this read-only review does not mutate generated records.

## Findings

### F1: Subcellular motility organelle BTO:0002292 (flagellum) is used as a host-associated habitat identity

blocker / resolved / confirmed; issue key: flagellum-cellular-organelle-identity.

PREGO row 166 (BTO:0002292, biolink:GrossAnatomicalStructure, 140 TAXON assertions across flagellated bacteria such as Escherichia coli, Salmonella enterica, and Bacillus) maps genome/isolate mentions of bacterial and eukaryotic motility flagella to BTO:0002292 ('Long, slender, threadlike, whiplike extension of certain cells or unicellular organisms used mainly for movements (others for signal transduction)...'). Under docs/CURATION.md, a subcellular motility organelle/component of the cell is not a microbial habitat identity. Add an ITEM-level NOT_APPLICABLE row in curation/decisions.tsv for habitatmech:PREGO.267811fd7a (object_id=BTO:0002292, object_label=flagellum, category=HOST_ASSOCIATED), preserving BTO:0002292 as an xref and retaining all 140 PREGO taxon rows on the minted concept, and update data/habitats/PATHS.tsv.

Disposition: Added ITEM-level NOT_APPLICABLE decision for habitatmech:PREGO.267811fd7a (target_id=BTO:0002292 'flagellum', relation=xref) in curation/decisions.tsv (#2334), reclassifying the cellular motility organelle bin as REVIEWED/NOT_APPLICABLE with BTO:0002292 preserved as a contextual xref.

### F2: Cellular appendage BTO:0002292 (flagellum) asserts whole-organism form BTO:0000464 (flagellate) in parent_habitats

major / resolved / confirmed; issue key: flagellum-organism-form-parent.

BTO:0002292 (flagellum) imports BTO:0000464 (flagellate, 'A flagellate protozoan or alga.') in parent_habitats from data/raw/ontology_subclass_edges.tsv row 1584. A cellular motility appendage is a component (part_of) of a flagellated cell, not a subtype (is_a) of a whole flagellate protozoan or alga. Resolving F1 in curation/decisions.tsv (NOT_APPLICABLE on habitatmech:PREGO.267811fd7a) removes the imported BTO:0000464 parent.

Disposition: Resolved by reclassifying habitatmech:PREGO.267811fd7a as NOT_APPLICABLE in curation/decisions.tsv (#2334), removing the BTO:0002292 -&gt; BTO:0000464 subclass edge from parent_habitats.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/flagellum.yaml; Entire YAML | supports | {"identifier": "habitatmech:PREGO.267811fd7a", "label": "flagella", "grounding_status": "NOT_APPLICABLE", "mapping_status": "REVIEWED", "xrefs": ["BTO:0002292"], "synonyms": [{"synonym_text": "flagellal", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "flagellum", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "flagellums", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}], "source_attestations": [{"source": "PREGO", "source_id": "BTO:0002292", "source_label": "flagellum", "assertion_count": 140, "assertion_unit": "TAXON", "score": 3.0, "evidence_channels": "annotated_genomes_isolates"}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by PREGO. Grounding: NOT_APPLICABLE."}, {"timestamp": "2026-11-09T00:00:00Z", "curator": "antigravity", "action": "NOT_APPLICABLE", "changes": "Marked NOT_APPLICABLE: the source concept does not denote a habitat. BTO:0002292 kept as an xref. ITEM cellular-organelle review #2334: PREGO BTO:0002292 ('flagellum', 'Long, slender, threadlike, whiplike extension of certain cells or unicellular organisms used mainly for movements...') denotes a subcellular motility appendage of flagellated microbes and cells (attested across 140 flagellated bacterial taxa such as Escherichia coli, Salmonella enterica, and Bacillus) rather than an external microbial habitat or host anatomical site, and its BTO subclass parent BTO:0000464 ('flagellate') is a whole-organism form. Mark NOT_APPLICABLE on the minted concept habitatmech:PREGO.267811fd7a in HOST_ASSOCIATED while preserving BTO:0002292 as an xref and retaining all 140 PREGO taxon rows. https://purl.obolibrary.org/obo/BTO_0002292 (source concept habitatmech:PREGO.267811fd7a)"}]} |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon, organism-form, and subcellular organelle terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=habitatmech:PREGO.267811fd7a, grounding_status=NOT_APPLICABLE, mapping_status=REVIEWED, parent_habitats=[], xrefs=["BTO:0002292"]. |
| ESIB1 | data/habitats/host_associated/adult.yaml; Entire YAML | supports | {"identifier": "habitatmech:PREGO.57e0a5faae", "label": "adult-associated environment", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED", "definition": "An environmental system determined by a living organism that has reached its adult stage.", "parent_habitats": ["ENVO:01001000"], "xrefs": ["BTO:0001043"], "synonyms": [{"synonym_text": "adult stage", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "adult stages", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "adults", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}]} |
| EPREGO | data/raw/prego_habitats.tsv; TSV rows 166 | supports | [{"data": {"biolink_category": "biolink:GrossAnatomicalStructure", "channels": "annotated_genomes_isolates", "direct_assertion_count": "140", "max_prego_score": "3", "ontology": "BTO", "prego_id": "BTO:0002292", "prego_synonyms": "flagella&#124;flagellal&#124;flagellum&#124;flagellums", "taxon_count": "140"}, "row": 166}] |
| EPREGOTAXA | data/raw/prego_habitat_taxa.tsv; TSV rows 2598,2599,2600,2601,2602,2603,2604,2605,2606,2607,2608,2609,2610,2611,2612,2613,2614,2615,2616,2617,2618,2619,2620,2621,2622 | supports | 25 PREGO taxon-association rows for BTO:0002292. |
| EONT | data/raw/ontology_terms.tsv; TSV rows 465,2292 | supports | [{"data": {"definition": "A flagellate protozoan or alga.", "deprecated": "", "directly_referenced": "TRUE", "label": "flagellate", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0000464"}, "row": 465}, {"data": {"definition": "Long, slender, threadlike, whiplike extension of certain cells or unicellular organisms used mainly for movements (others for signal transduction). In bacteria, the flagella are helical filaments made up of the protein, flagellin, and rotate like screws. In eukaryotes, such as in cells of animals, plants and protists, they are made up of microtubules surrounded by the plasma membrane and enable the cells to move in a whip-like fashion. Some flagella are not used for movement but in sensation and signal transduction by various cell types, e.g. rod photoreceptor cells of the eye, olfactory receptor neurons of the nose, kinocilium in cochlea of the ear.", "deprecated": "", "directly_referenced": "TRUE", "label": "flagellum", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0002292"}, "row": 2292}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 305,306,1584 | supports | [{"data": {"object": "BTO:0000720", "predicate": "rdfs:subClassOf", "subject": "BTO:0000464"}, "row": 305}, {"data": {"object": "BTO:0002503", "predicate": "rdfs:subClassOf", "subject": "BTO:0000464"}, "row": 306}, {"data": {"object": "BTO:0000464", "predicate": "rdfs:subClassOf", "subject": "BTO:0002292"}, "row": 1584}] |
| EP1 | data/habitats/host_associated/flagellate.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"identifier": "habitatmech:PREGO.ce9c3a92e9", "label": "flagellate-associated environment", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED", "definition": "An environmental system determined by a flagellate protozoan or alga.", "parent_habitats": ["ENVO:01001000"], "xrefs": ["BTO:0000464"], "synonyms": [{"synonym_text": "flagellate host environment", "synonym_type": "EXACT_SYNONYM", "source": "HabitatMech curation"}, {"synonym_text": "flagellates", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'flagellum&#124;BTO:0002292' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal located Stage 4 predecessor bundle 20261109T181013Z-flagellum-record (linked via EPREV and related_reviews) and checked related cohort and ancestor reviews for reconciliation. |
| EDEC | curation/decisions.tsv; TSV line 1844 | supports | [[1844, "habitatmech:PREGO.267811fd7a\tNOT_APPLICABLE\tBTO:0002292\tflagellum\t\tantigravity\t2026-11-09\tITEM cellular-organelle review #2334: PREGO BTO:0002292 ('flagellum', 'Long, slender, threadlike, whiplike extension of certain cells or unicellular organisms used mainly for movements...') denotes a subcellular motility appendage of flagellated microbes and cells (attested across 140 flagellated bacterial taxa such as Escherichia coli, Salmonella enterica, and Bacillus) rather than an external microbial habitat or host anatomical site, and its BTO subclass parent BTO:0000464 ('flagellate') is a whole-organism form. Mark NOT_APPLICABLE on the minted concept habitatmech:PREGO.267811fd7a in HOST_ASSOCIATED while preserving BTO:0002292 as an xref and retaining all 140 PREGO taxon rows. https://purl.obolibrary.org/obo/BTO_0002292\tITEM\tHOST_ASSOCIATED\txref"]] |
| EPREV | reviews/structured/20261109T181013Z-flagellum-record/review.yaml; Every immutable Stage 4 baseline finding | supports | Exact predecessor keys and findings reconciled; original inspected source scope preserved. |
| ETEST | tests/test_finger_to_free_living_state_review_repairs.py; Complete full-corpus counterfactual regression suite | supports | Exactly thirteen records differ from the counterfactual baseline across Issues #2334, #2335, and #2336. |
| EHIST_G1 | history/other/decisions/2026-11-09T214500Z-antigravity-233401.yaml; Complete curation session history event | supports | Authorized curation event for Issue #2334 recorded and validated. |

## Limits And Additional Notes

- Only the cited repository inputs, ontology terms, and source inventories were inspected; original specimen-level support for every upstream source assertion was not exhaustively reconstructed.
- Source counts, PREGO scores, and ranks are not prevalence, viability, mechanism, or characteristic presence.
- Configured label correspondence skipped 2,094 no-adapter pairs; this is not whole-corpus identifier certification.
- Read-only review: no curation table, generated habitat YAML, status, or history record was modified.
- Saved against working-tree repairs atop main commit 7c82566b001f676eb0d3c9cc6c905f85a99b8bde; all earlier saved bundles in reviews/structured/ remain byte-identical.
- Reconciles predecessor bundle 20261109T181013Z-flagellum-record with exact issue_key and previous_occurrences lineage.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T215003Z-flagellum-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: flagellum'
started_at: '2026-11-09T21:40:00Z'
finished_at: '2026-11-09T21:50:03Z'
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
summary: Reclassified PREGO source concept habitatmech:PREGO.267811fd7a (BTO:0002292
  'flagellum') via an ITEM-level NOT_APPLICABLE decision (target_id=BTO:0002292 'flagellum',
  relation=xref) in curation/decisions.tsv (#2334). This replaces cellular organelle
  identity BTO:0002292 with minted identifier habitatmech:PREGO.267811fd7a (REVIEWED/NOT_APPLICABLE),
  removes organismal form parent BTO:0000464 (flagellate) from parent_habitats, preserves
  BTO:0002292 as a contextual xref, and retains all 140 PREGO TAXON assertions and
  25 retained characteristic_taxa rows. Both predecessor findings (F1 and F2) are
  resolved.
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
  - path: data/habitats/host_associated/adult.yaml
    sha256: 91c41fc8a4d72c43682756d0e29562fbf92e27e198d386fc5847a6c8961e4e04
    role: context
  - path: data/habitats/host_associated/flagellate.yaml
    sha256: d0d8a90198899c9c97024913bd9932e4789230c7d11407363f7af15a79a1dcdc
    role: context
  - path: data/habitats/host_associated/flagellum.yaml
    sha256: 728aa864450dc96b6f6f58fac79aad57a83397520dbe1f2e09a16be5b552eb0f
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
  - path: history/other/decisions/2026-11-09T214500Z-antigravity-233401.yaml
    sha256: b6347253e029b5d760e3e10bc1c927efc02c51fd69114bd920a11681c35f7ff2
    role: context
  - path: reviews/structured/20261109T181013Z-flagellum-record/review.yaml
    sha256: 3128ed937f6a3b14fac8dc19283cfbea1702e41c411940cf12c4b7615d656cc0
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
- target_id: habitatmech:PREGO.267811fd7a
  path: data/habitats/host_associated/flagellum.yaml
  label: flagella
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
    finding on data/habitats/host_associated/flagellum.yaml after bounded Cycle 8
    Stage 5 remediation.
  selection: One of thirteen repaired targets from the finger-through-free_living_state
    cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:PREGO.267811fd7a
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
    --target-class HabitatRecord data/habitats/host_associated/flagellum.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:PREGO.267811fd7a
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
  - habitatmech:PREGO.267811fd7a
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
  - habitatmech:PREGO.267811fd7a
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
  - habitatmech:PREGO.267811fd7a
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
  - habitatmech:PREGO.267811fd7a
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
  - habitatmech:PREGO.267811fd7a
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
  - habitatmech:PREGO.267811fd7a
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
  - habitatmech:PREGO.267811fd7a
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
  - habitatmech:PREGO.267811fd7a
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
  - habitatmech:PREGO.267811fd7a
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
  - habitatmech:PREGO.267811fd7a
  summary: Completed 2026-11-09T21:49:30Z. rendered 3209 habitat pages, 757 redirect
    stubs, 8 categories, 701 term requests; pages/ is in step with the corpus.
  scope_note: Full-corpus static site parity check.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/flagellum.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T21:50:03Z'
  support: supports
  summary: '{"identifier": "habitatmech:PREGO.267811fd7a", "label": "flagella", "grounding_status":
    "NOT_APPLICABLE", "mapping_status": "REVIEWED", "xrefs": ["BTO:0002292"], "synonyms":
    [{"synonym_text": "flagellal", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"},
    {"synonym_text": "flagellum", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"},
    {"synonym_text": "flagellums", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}],
    "source_attestations": [{"source": "PREGO", "source_id": "BTO:0002292", "source_label":
    "flagellum", "assertion_count": 140, "assertion_unit": "TAXON", "score": 3.0,
    "evidence_channels": "annotated_genomes_isolates"}], "curation_history": [{"timestamp":
    "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES",
    "changes": "Seeded from data/raw/ inventories; attested by PREGO. Grounding: NOT_APPLICABLE."},
    {"timestamp": "2026-11-09T00:00:00Z", "curator": "antigravity", "action": "NOT_APPLICABLE",
    "changes": "Marked NOT_APPLICABLE: the source concept does not denote a habitat.
    BTO:0002292 kept as an xref. ITEM cellular-organelle review #2334: PREGO BTO:0002292
    (''flagellum'', ''Long, slender, threadlike, whiplike extension of certain cells
    or unicellular organisms used mainly for movements...'') denotes a subcellular
    motility appendage of flagellated microbes and cells (attested across 140 flagellated
    bacterial taxa such as Escherichia coli, Salmonella enterica, and Bacillus) rather
    than an external microbial habitat or host anatomical site, and its BTO subclass
    parent BTO:0000464 (''flagellate'') is a whole-organism form. Mark NOT_APPLICABLE
    on the minted concept habitatmech:PREGO.267811fd7a in HOST_ASSOCIATED while preserving
    BTO:0002292 as an xref and retaining all 140 PREGO taxon rows. https://purl.obolibrary.org/obo/BTO_0002292
    (source concept habitatmech:PREGO.267811fd7a)"}]}'
  snapshot_sha256: 728aa864450dc96b6f6f58fac79aad57a83397520dbe1f2e09a16be5b552eb0f
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-09T21:50:03Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon, organism-form,
    and subcellular organelle terms cannot substitute for associated environments;
    parent_habitats must be strictly broader across all contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-09T21:50:03Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-09T21:50:03Z'
  support: supports
  summary: Seed generator produces identifier=habitatmech:PREGO.267811fd7a, grounding_status=NOT_APPLICABLE,
    mapping_status=REVIEWED, parent_habitats=[], xrefs=["BTO:0002292"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: ESIB1
  kind: record_content
  reference: data/habitats/host_associated/adult.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T21:50:03Z'
  support: supports
  summary: '{"identifier": "habitatmech:PREGO.57e0a5faae", "label": "adult-associated
    environment", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED",
    "definition": "An environmental system determined by a living organism that has
    reached its adult stage.", "parent_habitats": ["ENVO:01001000"], "xrefs": ["BTO:0001043"],
    "synonyms": [{"synonym_text": "adult stage", "synonym_type": "RELATED_SYNONYM",
    "source": "PREGO"}, {"synonym_text": "adult stages", "synonym_type": "RELATED_SYNONYM",
    "source": "PREGO"}, {"synonym_text": "adults", "synonym_type": "RELATED_SYNONYM",
    "source": "PREGO"}]}'
  snapshot_sha256: 91c41fc8a4d72c43682756d0e29562fbf92e27e198d386fc5847a6c8961e4e04
- evidence_id: EPREGO
  kind: database
  reference: data/raw/prego_habitats.tsv
  locator: TSV rows 166
  accessed_at: '2026-11-09T21:50:03Z'
  support: supports
  summary: '[{"data": {"biolink_category": "biolink:GrossAnatomicalStructure", "channels":
    "annotated_genomes_isolates", "direct_assertion_count": "140", "max_prego_score":
    "3", "ontology": "BTO", "prego_id": "BTO:0002292", "prego_synonyms": "flagella|flagellal|flagellum|flagellums",
    "taxon_count": "140"}, "row": 166}]'
  snapshot_sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
- evidence_id: EPREGOTAXA
  kind: database
  reference: data/raw/prego_habitat_taxa.tsv
  locator: TSV rows 2598,2599,2600,2601,2602,2603,2604,2605,2606,2607,2608,2609,2610,2611,2612,2613,2614,2615,2616,2617,2618,2619,2620,2621,2622
  accessed_at: '2026-11-09T21:50:03Z'
  support: supports
  summary: 25 PREGO taxon-association rows for BTO:0002292.
  snapshot_sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 465,2292
  accessed_at: '2026-11-09T21:50:03Z'
  support: supports
  summary: '[{"data": {"definition": "A flagellate protozoan or alga.", "deprecated":
    "", "directly_referenced": "TRUE", "label": "flagellate", "label_only": "FALSE",
    "ontology": "BTO", "synonyms": "", "term_id": "BTO:0000464"}, "row": 465}, {"data":
    {"definition": "Long, slender, threadlike, whiplike extension of certain cells
    or unicellular organisms used mainly for movements (others for signal transduction).
    In bacteria, the flagella are helical filaments made up of the protein, flagellin,
    and rotate like screws. In eukaryotes, such as in cells of animals, plants and
    protists, they are made up of microtubules surrounded by the plasma membrane and
    enable the cells to move in a whip-like fashion. Some flagella are not used for
    movement but in sensation and signal transduction by various cell types, e.g.
    rod photoreceptor cells of the eye, olfactory receptor neurons of the nose, kinocilium
    in cochlea of the ear.", "deprecated": "", "directly_referenced": "TRUE", "label":
    "flagellum", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id":
    "BTO:0002292"}, "row": 2292}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 305,306,1584
  accessed_at: '2026-11-09T21:50:03Z'
  support: supports
  summary: '[{"data": {"object": "BTO:0000720", "predicate": "rdfs:subClassOf", "subject":
    "BTO:0000464"}, "row": 305}, {"data": {"object": "BTO:0002503", "predicate": "rdfs:subClassOf",
    "subject": "BTO:0000464"}, "row": 306}, {"data": {"object": "BTO:0000464", "predicate":
    "rdfs:subClassOf", "subject": "BTO:0002292"}, "row": 1584}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EP1
  kind: record_content
  reference: data/habitats/host_associated/flagellate.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-11-09T21:50:03Z'
  support: supports
  summary: '{"identifier": "habitatmech:PREGO.ce9c3a92e9", "label": "flagellate-associated
    environment", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED",
    "definition": "An environmental system determined by a flagellate protozoan or
    alga.", "parent_habitats": ["ENVO:01001000"], "xrefs": ["BTO:0000464"], "synonyms":
    [{"synonym_text": "flagellate host environment", "synonym_type": "EXACT_SYNONYM",
    "source": "HabitatMech curation"}, {"synonym_text": "flagellates", "synonym_type":
    "RELATED_SYNONYM", "source": "PREGO"}]}'
  snapshot_sha256: d0d8a90198899c9c97024913bd9932e4789230c7d11407363f7af15a79a1dcdc
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'flagellum|BTO:0002292' reviews/structured/*/review.yaml curation/
    history/
  accessed_at: '2026-11-09T21:50:03Z'
  support: context_only
  summary: Structured-review traversal located Stage 4 predecessor bundle 20261109T181013Z-flagellum-record
    (linked via EPREV and related_reviews) and checked related cohort and ancestor
    reviews for reconciliation.
  search_scope: curation, history, data/raw, and reviews/structured/*/review.yaml
    traversal at commit 7c82566b001f676eb0d3c9cc6c905f85a99b8bde.
- evidence_id: EDEC
  kind: record_content
  reference: curation/decisions.tsv
  locator: TSV line 1844
  accessed_at: '2026-11-09T21:50:03Z'
  support: supports
  summary: '[[1844, "habitatmech:PREGO.267811fd7a\tNOT_APPLICABLE\tBTO:0002292\tflagellum\t\tantigravity\t2026-11-09\tITEM
    cellular-organelle review #2334: PREGO BTO:0002292 (''flagellum'', ''Long, slender,
    threadlike, whiplike extension of certain cells or unicellular organisms used
    mainly for movements...'') denotes a subcellular motility appendage of flagellated
    microbes and cells (attested across 140 flagellated bacterial taxa such as Escherichia
    coli, Salmonella enterica, and Bacillus) rather than an external microbial habitat
    or host anatomical site, and its BTO subclass parent BTO:0000464 (''flagellate'')
    is a whole-organism form. Mark NOT_APPLICABLE on the minted concept habitatmech:PREGO.267811fd7a
    in HOST_ASSOCIATED while preserving BTO:0002292 as an xref and retaining all 140
    PREGO taxon rows. https://purl.obolibrary.org/obo/BTO_0002292\tITEM\tHOST_ASSOCIATED\txref"]]'
  snapshot_sha256: 8e0c9ea50c453b9b0eb86e9a6cf246dbc188714ec7a8cc37b2918d5373e6d2ae
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261109T181013Z-flagellum-record/review.yaml
  locator: Every immutable Stage 4 baseline finding
  accessed_at: '2026-11-09T21:50:03Z'
  support: supports
  summary: Exact predecessor keys and findings reconciled; original inspected source
    scope preserved.
  snapshot_sha256: 3128ed937f6a3b14fac8dc19283cfbea1702e41c411940cf12c4b7615d656cc0
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_finger_to_free_living_state_review_repairs.py
  locator: Complete full-corpus counterfactual regression suite
  accessed_at: '2026-11-09T21:50:03Z'
  support: supports
  summary: 'Exactly thirteen records differ from the counterfactual baseline across
    Issues #2334, #2335, and #2336.'
  snapshot_sha256: 495a506d77d0f3c2484e16b510c233a7c8b108ae96cba6b6346252c3a9d01bdb
- evidence_id: EHIST_G1
  kind: record_content
  reference: history/other/decisions/2026-11-09T214500Z-antigravity-233401.yaml
  locator: Complete curation session history event
  accessed_at: '2026-11-09T21:50:03Z'
  support: supports
  summary: 'Authorized curation event for Issue #2334 recorded and validated.'
  snapshot_sha256: b6347253e029b5d760e3e10bc1c927efc02c51fd69114bd920a11681c35f7ff2
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
  - habitatmech:PREGO.267811fd7a
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EPREGO
  - EPREGOTAXA
  - EONT
  - EONTEDGE
  - EP1
  - ESEARCH
  - EDEC
  - EPREV
  - ETEST
  - EHIST_G1
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: supported
  summary: 'habitatmech:PREGO.267811fd7a: flagella; NOT_APPLICABLE/REVIEWED; parents
    []. Reclassified PREGO source concept habitatmech:PREGO.267811fd7a (BTO:0002292
    ''flagellum'') via an ITEM-level NOT_APPLICABLE decision (target_id=BTO:0002292
    ''flagellum'', relation=xref) in curation/decisions.tsv (#2334). This replaces
    cellular organelle identity BTO:0002292 with minted identifier habitatmech:PREGO.267811fd7a
    (REVIEWED/NOT_APPLICABLE), removes organismal form parent BTO:0000464 (flagellate)
    from parent_habitats, preserves BTO:0002292 as a contextual xref, and retains
    all 140 PREGO TAXON assertions and 25 retained characteristic_taxa rows. Both
    predecessor findings (F1 and F2) are resolved.'
  target_ids:
  - habitatmech:PREGO.267811fd7a
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EPREGO
  - EPREGOTAXA
  - EONT
  - EONTEDGE
  - EP1
  - ESEARCH
  - EDEC
  - EPREV
  - ETEST
  - EHIST_G1
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks,
    and pools: [{"count": 140, "source": "PREGO", "unit": "TAXON"}]. Zero counts are
    omitted; unrelated parent counts are not combined.'
  target_ids:
  - habitatmech:PREGO.267811fd7a
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EPREGO
  - EPREGOTAXA
  - EONT
  - EONTEDGE
  - EP1
  - ESEARCH
  - EDEC
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
  - habitatmech:PREGO.267811fd7a
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EPREGO
  - EPREGOTAXA
  - EONT
  - EONTEDGE
  - EP1
  - ESEARCH
  - EDEC
  - EPREV
  - ETEST
  - EHIST_G1
- assessment_id: A5
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: Missing optional parameters/graphs are not evidence deficits. Full source
    decisions and executed routes reproduce REVIEWED / NOT_APPLICABLE; this read-only
    review does not mutate generated records.
  target_ids:
  - habitatmech:PREGO.267811fd7a
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EPREGO
  - EPREGOTAXA
  - EONT
  - EONTEDGE
  - EP1
  - ESEARCH
  - EDEC
  - EPREV
  - ETEST
  - EHIST_G1
findings:
- finding_id: F1
  issue_key: flagellum-cellular-organelle-identity
  category: identity
  severity: blocker
  status: resolved
  certainty: confirmed
  title: Subcellular motility organelle BTO:0002292 (flagellum) is used as a host-associated
    habitat identity
  description: PREGO row 166 (BTO:0002292, biolink:GrossAnatomicalStructure, 140 TAXON
    assertions across flagellated bacteria such as Escherichia coli, Salmonella enterica,
    and Bacillus) maps genome/isolate mentions of bacterial and eukaryotic motility
    flagella to BTO:0002292 ('Long, slender, threadlike, whiplike extension of certain
    cells or unicellular organisms used mainly for movements (others for signal transduction)...').
    Under docs/CURATION.md, a subcellular motility organelle/component of the cell
    is not a microbial habitat identity. Add an ITEM-level NOT_APPLICABLE row in curation/decisions.tsv
    for habitatmech:PREGO.267811fd7a (object_id=BTO:0002292, object_label=flagellum,
    category=HOST_ASSOCIATED), preserving BTO:0002292 as an xref and retaining all
    140 PREGO taxon rows on the minted concept, and update data/habitats/PATHS.tsv.
  target_ids:
  - habitatmech:PREGO.267811fd7a
  field_paths:
  - identifier
  - grounding_status
  - mapping_status
  - parent_habitats
  - xrefs
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EPREGO
  - EPREGOTAXA
  - EONT
  - EONTEDGE
  - EP1
  - ESEARCH
  - EDEC
  - EPREV
  - ETEST
  - EHIST_G1
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: blocker
  normalization_reason: Subcellular organelle/component identity is adopted as a microbial
    habitat identity, contradicting docs/CURATION.md.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2334
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261109T181013Z-flagellum-record
    finding_id: F1
  disposition_reason: Added ITEM-level NOT_APPLICABLE decision for habitatmech:PREGO.267811fd7a
    (target_id=BTO:0002292 'flagellum', relation=xref) in curation/decisions.tsv (#2334),
    reclassifying the cellular motility organelle bin as REVIEWED/NOT_APPLICABLE with
    BTO:0002292 preserved as a contextual xref.
- finding_id: F2
  issue_key: flagellum-organism-form-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Cellular appendage BTO:0002292 (flagellum) asserts whole-organism form BTO:0000464
    (flagellate) in parent_habitats
  description: BTO:0002292 (flagellum) imports BTO:0000464 (flagellate, 'A flagellate
    protozoan or alga.') in parent_habitats from data/raw/ontology_subclass_edges.tsv
    row 1584. A cellular motility appendage is a component (part_of) of a flagellated
    cell, not a subtype (is_a) of a whole flagellate protozoan or alga. Resolving
    F1 in curation/decisions.tsv (NOT_APPLICABLE on habitatmech:PREGO.267811fd7a)
    removes the imported BTO:0000464 parent.
  target_ids:
  - habitatmech:PREGO.267811fd7a
  field_paths:
  - parent_habitats
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EPREGO
  - EPREGOTAXA
  - EONT
  - EONTEDGE
  - EP1
  - ESEARCH
  - EDEC
  - EPREV
  - ETEST
  - EHIST_G1
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_subclass_edges.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or representation claim; deterministic
    validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2334
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261109T181013Z-flagellum-record
    finding_id: F2
  disposition_reason: Resolved by reclassifying habitatmech:PREGO.267811fd7a as NOT_APPLICABLE
    in curation/decisions.tsv (#2334), removing the BTO:0002292 -> BTO:0000464 subclass
    edge from parent_habitats.
actions: []
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
- Reconciles predecessor bundle 20261109T181013Z-flagellum-record with exact issue_key
  and previous_occurrences lineage.
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261109T181013Z-flagellum-record
  relationship: Exact predecessor; every finding explicitly reconciled.
```
