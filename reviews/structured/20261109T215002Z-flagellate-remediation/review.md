# Remediation review: flagellate

- Review: 20261109T215002Z-flagellate-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-09T21:40:00Z
- Finished UTC: 2026-11-09T21:50:02Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Un-grounded PREGO source concept habitatmech:PREGO.ce9c3a92e9 (BTO:0000464 'flagellate') from organismal form term BTO:0000464 ('flagellate') via an ITEM-level CONFIRM_UNGROUNDED decision (target_id=BTO:0000464, relation=xref) in curation/decisions.tsv, defined 'flagellate-associated environment' under ENVO:01001000 ('environmental system determined by an organism', parent_mode REPLACE) in curation/term_requests.tsv, and excluded automatic retention of displaced source label 'flagellate' in curation/definition_source_label_exclusions.tsv (#2334). This removes non-habitat BTO parents BTO:0000720 (plant form) and BTO:0002503 (protozoan form) from parent_habitats, keeps BTO:0000464 as a contextual xref, promotes status to REVIEWED/UNGROUNDED, and preserves all 9 retained PREGO characteristic taxa (9 TAXON assertions). Both predecessor findings (F1 and F2) are resolved.

## Scope And Provenance

Full current target assessment and explicit disposition of every baseline finding on data/habitats/host_associated/flagellate.yaml after bounded Cycle 8 Stage 5 remediation.

Selection: One of thirteen repaired targets from the finger-through-free_living_state cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c82566b001f676eb0d3c9cc6c905f85a99b8bde.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:PREGO.ce9c3a92e9 | data/habitats/host_associated/flagellate.yaml | generated | flagellate-associated environment |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:PREGO.ce9c3a92e9 | Completed 2026-11-09T21:48:00Z. No issues found against src/habitatmech/schema/habitatmech.yaml. |
| validate-strict | passed | True | habitatmech:PREGO.ce9c3a92e9 | Completed 2026-11-09T21:48:05Z. 24 checked, 0 failed; target passed closed-schema validation. |
| validate-history | passed | True | habitatmech:PREGO.ce9c3a92e9 | Completed 2026-11-09T21:48:10Z. No issues found; 879 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | habitatmech:PREGO.ce9c3a92e9 | Completed 2026-11-09T21:48:15Z. 14 inventory files and 2 GOLD export files verified. |
| verify-corpus | passed | True | habitatmech:PREGO.ce9c3a92e9 | Completed 2026-11-09T21:48:25Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | habitatmech:PREGO.ce9c3a92e9 | Completed 2026-11-09T21:48:30Z. 103 causal-graph curations and target records validated. |
| term-requests-check | passed | True | habitatmech:PREGO.ce9c3a92e9 | Completed 2026-11-09T21:48:35Z. term-request table is current (676 terms). |
| validate-products | passed | True | habitatmech:PREGO.ce9c3a92e9 | Completed 2026-11-09T21:48:45Z. 24 records, 0 label drift findings. |
| pytest counterfactual review repairs | passed | True | habitatmech:PREGO.ce9c3a92e9 | Completed 2026-11-09T21:49:00Z. 2 passed; exact 13-record counterfactual diff verified. |
| curation-floor | passed | True | habitatmech:PREGO.ce9c3a92e9 | Completed 2026-11-09T21:49:05Z. Floor satisfied across all 13 metrics. |
| render-check | passed | True | habitatmech:PREGO.ce9c3a92e9 | Completed 2026-11-09T21:49:30Z. rendered 3209 habitat pages, 757 redirect stubs, 8 categories, 701 term requests; pages/ is in step with the corpus. |

## Scientific And Domain Assessments

### Native validity and reproduction after bounded remediation

schema: supported. Targets: habitatmech:PREGO.ce9c3a92e9.

Individual schema, strict 24-target validation, 879 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 103 causal overlays, 676 term requests, curation floor, site parity, and counterfactual regression tests passed.

### Identity, definition, hierarchy and aliases

identity: supported. Targets: habitatmech:PREGO.ce9c3a92e9.

habitatmech:PREGO.ce9c3a92e9: flagellate-associated environment; UNGROUNDED/REVIEWED; parents ["ENVO:01001000"]. Un-grounded PREGO source concept habitatmech:PREGO.ce9c3a92e9 (BTO:0000464 'flagellate') from organismal form term BTO:0000464 ('flagellate') via an ITEM-level CONFIRM_UNGROUNDED decision (target_id=BTO:0000464, relation=xref) in curation/decisions.tsv, defined 'flagellate-associated environment' under ENVO:01001000 ('environmental system determined by an organism', parent_mode REPLACE) in curation/term_requests.tsv, and excluded automatic retention of displaced source label 'flagellate' in curation/definition_source_label_exclusions.tsv (#2334). This removes non-habitat BTO parents BTO:0000720 (plant form) and BTO:0002503 (protozoan form) from parent_habitats, keeps BTO:0000464 as a contextual xref, promotes status to REVIEWED/UNGROUNDED, and preserves all 9 retained PREGO characteristic taxa (9 TAXON assertions). Both predecessor findings (F1 and F2) are resolved.

### Source counts and retained ranking

quantity: supported. Targets: habitatmech:PREGO.ce9c3a92e9.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"count": 9, "source": "PREGO", "unit": "TAXON"}]. Zero counts are omitted; unrelated parent counts are not combined.

### Predecessor finding reconciliation

representation: supported. Targets: habitatmech:PREGO.ce9c3a92e9.

Every predecessor finding preserves its stable issue_key and exact lineage. All predecessor findings in this target scope are resolved.

### Parameters, mechanisms and native status

completeness: supported. Targets: habitatmech:PREGO.ce9c3a92e9.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only review does not mutate generated records.

## Findings

### F1: Organism-form class BTO:0000464 (flagellate) is used as the habitat identity

blocker / resolved / confirmed; issue key: flagellate-organism-form-identity.

Under docs/CURATION.md, whole-organism and morphological organism-form classes cannot serve as habitat identity. Add an ITEM-level CONFIRM_UNGROUNDED row in curation/decisions.tsv for habitatmech:PREGO.ce9c3a92e9 with object_id=BTO:0000464, object_label=flagellate, relation=xref, category=HOST_ASSOCIATED; author a curated definition for 'flagellate-associated environment' ('An environmental system determined by a flagellate protozoan or alga.') under ENVO:01001000 (environmental system determined by an organism) with parent_mode=REPLACE in curation/term_requests.tsv; exclude bare source label 'flagellate' in curation/definition_source_label_exclusions.tsv; and update data/habitats/PATHS.tsv.

Disposition: Added ITEM-level CONFIRM_UNGROUNDED decision for habitatmech:PREGO.ce9c3a92e9 (target_id=BTO:0000464 'flagellate', relation=xref) in curation/decisions.tsv, defined 'flagellate-associated environment' under ENVO:01001000 ('environmental system determined by an organism', parent_mode REPLACE) in curation/term_requests.tsv, and added a guarded source-label exclusion in curation/definition_source_label_exclusions.tsv (#2334).

### F2: Organism-form classes BTO:0000720 (plant form) and BTO:0002503 (protozoan form) are asserted in parent_habitats

major / resolved / confirmed; issue key: flagellate-organism-form-parents.

BTO:0000720 (plant form) and BTO:0002503 (protozoan form) are morphological organism-form classes imported from BTO:0000464 rather than strictly broader microbial habitat superclasses. Resolving F1 by ungrounding habitatmech:PREGO.ce9c3a92e9 and defining 'flagellate-associated environment' under ENVO:01001000 with parent_mode=REPLACE removes both organism-form parents.

Disposition: Resolved by un-grounding habitatmech:PREGO.ce9c3a92e9 from BTO:0000464 and defining it under ENVO:01001000 ('environmental system determined by an organism', parent_mode REPLACE) in curation/term_requests.tsv (#2334), removing organism-form subclass parents BTO:0000720 (plant form) and BTO:0002503 (protozoan form) from parent_habitats.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/flagellate.yaml; Entire YAML | supports | {"identifier": "habitatmech:PREGO.ce9c3a92e9", "label": "flagellate-associated environment", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED", "definition": "An environmental system determined by a flagellate protozoan or alga.", "parent_habitats": ["ENVO:01001000"], "xrefs": ["BTO:0000464"], "synonyms": [{"synonym_text": "flagellate host environment", "synonym_type": "EXACT_SYNONYM", "source": "HabitatMech curation"}, {"synonym_text": "flagellates", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}], "source_attestations": [{"source": "PREGO", "source_id": "BTO:0000464", "source_label": "flagellate", "assertion_count": 9, "assertion_unit": "TAXON", "score": 3.0, "evidence_channels": "annotated_genomes_isolates"}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by PREGO. Grounding: UNGROUNDED."}, {"timestamp": "2026-11-09T00:00:00Z", "curator": "antigravity", "action": "CONFIRM_UNGROUNDED", "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. BTO:0000464 'flagellate' kept as an xref. ITEM organism-form review #2334: PREGO BTO:0000464 ('flagellate', 'A flagellate protozoan or alga.') names a morphological organism form rather than a microbial habitat identity, and its BTO subclass parents BTO:0000720 ('plant form') and BTO:0002503 ('protozoan form') are organism-form classifications rather than habitat superclasses. Keep the stable source mint habitatmech:PREGO.ce9c3a92e9 in HOST_ASSOCIATED with BTO:0000464 preserved as a contextual xref, and define 'flagellate-associated environment' under ENVO:01001000 ('environmental system determined by an organism'). https://purl.obolibrary.org/obo/BTO_0000464 https://purl.obolibrary.org/obo/ENVO_01001000 (source concept habitatmech:PREGO.ce9c3a92e9)"}, {"timestamp": "2026-11-09T00:00:00Z", "curator": "antigravity", "action": "DEFINED", "changes": "Defined as 'flagellate-associated environment' under ENVO:01001000 'environmental system determined by an organism'. Review #2334: define the organism-determined environmental system associated with a flagellate protozoan or alga under ENVO:01001000 ('environmental system determined by an organism') with parent_mode REPLACE, keeping BTO:0000464 ('flagellate') as a contextual xref and suppressing automatic retention of the bare organism-form source label 'flagellate' as an exact synonym. https://purl.obolibrary.org/obo/BTO_0000464 https://purl.obolibrary.org/obo/ENVO_01001000"}, {"timestamp": "2026-11-09T00:00:00Z", "curator": "antigravity", "action": "SOURCE_SYNONYM_EXCLUDED", "changes": "Omitted automatic retention of displaced source label 'flagellate' when defining habitatmech:PREGO.ce9c3a92e9 as 'flagellate-associated environment'. Verbatim source attestations are preserved. Review #2334: 'flagellate' names the organism form (BTO:0000464), not the environment associated with it. Suppress automatic retention of the displaced source label while preserving verbatim PREGO provenance and related source aliases."}]} |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon, organism-form, and subcellular organelle terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=habitatmech:PREGO.ce9c3a92e9, grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["ENVO:01001000"], xrefs=["BTO:0000464"]. |
| ESIB1 | data/habitats/host_associated/adult.yaml; Entire YAML | supports | {"identifier": "habitatmech:PREGO.57e0a5faae", "label": "adult-associated environment", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED", "definition": "An environmental system determined by a living organism that has reached its adult stage.", "parent_habitats": ["ENVO:01001000"], "xrefs": ["BTO:0001043"], "synonyms": [{"synonym_text": "adult stage", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "adult stages", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "adults", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}]} |
| EPREGO | data/raw/prego_habitats.tsv; TSV rows 340 | supports | [{"data": {"biolink_category": "biolink:GrossAnatomicalStructure", "channels": "annotated_genomes_isolates", "direct_assertion_count": "9", "max_prego_score": "3", "ontology": "BTO", "prego_id": "BTO:0000464", "prego_synonyms": "flagellate&#124;flagellates", "taxon_count": "9"}, "row": 340}] |
| EPREGOTAXA | data/raw/prego_habitat_taxa.tsv; TSV rows 647,648,649,650,651,652,653,654,655 | supports | 9 PREGO taxon-association rows for BTO:0000464. |
| EONT | data/raw/ontology_terms.tsv; TSV rows 465,721,2503 | supports | [{"data": {"definition": "A flagellate protozoan or alga.", "deprecated": "", "directly_referenced": "TRUE", "label": "flagellate", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0000464"}, "row": 465}, {"data": {"definition": "", "deprecated": "", "directly_referenced": "FALSE", "label": "plant form", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0000720"}, "row": 721}, {"data": {"definition": "Any individual of the Protozoa.", "deprecated": "", "directly_referenced": "FALSE", "label": "protozoan form", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0002503"}, "row": 2503}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 69,112,195,305,306,327,336,462,475,488,682,715,728,792,836 | supports | [{"data": {"object": "BTO:0002503", "predicate": "rdfs:subClassOf", "subject": "BTO:0000092"}, "row": 69}, {"data": {"object": "BTO:0000720", "predicate": "rdfs:subClassOf", "subject": "BTO:0000159"}, "row": 112}, {"data": {"object": "BTO:0000720", "predicate": "rdfs:subClassOf", "subject": "BTO:0000285"}, "row": 195}, {"data": {"object": "BTO:0000720", "predicate": "rdfs:subClassOf", "subject": "BTO:0000464"}, "row": 305}, {"data": {"object": "BTO:0002503", "predicate": "rdfs:subClassOf", "subject": "BTO:0000464"}, "row": 306}, {"data": {"object": "BTO:0000720", "predicate": "rdfs:subClassOf", "subject": "BTO:0000495"}, "row": 327}, {"data": {"object": "BTO:0000720", "predicate": "rdfs:subClassOf", "subject": "BTO:0000514"}, "row": 336}, {"data": {"object": "BTO:0001461", "predicate": "rdfs:subClassOf", "subject": "BTO:0000720"}, "row": 462}, {"data": {"object": "BTO:0000720", "predicate": "rdfs:subClassOf", "subject": "BTO:0000735"}, "row": 475}, {"data": {"object": "BTO:0002503", "predicate": "rdfs:subClassOf", "subject": "BTO:0000749"}, "row": 488}, {"data": {"object": "BTO:0000720", "predicate": "rdfs:subClassOf", "subject": "BTO:0001010"}, "row": 682}, {"data": {"object": "BTO:0000720", "predicate": "rdfs:subClassOf", "subject": "BTO:0001064"}, "row": 715}, {"data": {"object": "BTO:0000720", "predicate": "rdfs:subClassOf", "subject": "BTO:0001084"}, "row": 728}, {"data": {"object": "BTO:0000720", "predicate": "rdfs:subClassOf", "subject": "BTO:0001171"}, "row": 792}, {"data": {"object": "BTO:0000720", "predicate": "rdfs:subClassOf", "subject": "BTO:0001228"}, "row": 836}] |
| ESEARCH | Local input and review traversal; grep -rn -E 'flagellate&#124;BTO:0000464' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal located Stage 4 predecessor bundle 20261109T181012Z-flagellate-record (linked via EPREV and related_reviews) and checked related cohort and ancestor reviews for reconciliation. |
| ETR | curation/term_requests.tsv; TSV line 677 | supports | [[677, "habitatmech:PREGO.ce9c3a92e9\tflagellate-associated environment\tENVO:01001000\tenvironmental system determined by an organism\tAn environmental system determined by a flagellate protozoan or alga.\tflagellate host environment\tantigravity\t2026-11-09\tReview #2334: define the organism-determined environmental system associated with a flagellate protozoan or alga under ENVO:01001000 ('environmental system determined by an organism') with parent_mode REPLACE, keeping BTO:0000464 ('flagellate') as a contextual xref and suppressing automatic retention of the bare organism-form source label 'flagellate' as an exact synonym. https://purl.obolibrary.org/obo/BTO_0000464 https://purl.obolibrary.org/obo/ENVO_01001000\tREPLACE"]] |
| EDEC | curation/decisions.tsv; TSV line 1843 | supports | [[1843, "habitatmech:PREGO.ce9c3a92e9\tCONFIRM_UNGROUNDED\tBTO:0000464\tflagellate\t\tantigravity\t2026-11-09\tITEM organism-form review #2334: PREGO BTO:0000464 ('flagellate', 'A flagellate protozoan or alga.') names a morphological organism form rather than a microbial habitat identity, and its BTO subclass parents BTO:0000720 ('plant form') and BTO:0002503 ('protozoan form') are organism-form classifications rather than habitat superclasses. Keep the stable source mint habitatmech:PREGO.ce9c3a92e9 in HOST_ASSOCIATED with BTO:0000464 preserved as a contextual xref, and define 'flagellate-associated environment' under ENVO:01001000 ('environmental system determined by an organism'). https://purl.obolibrary.org/obo/BTO_0000464 https://purl.obolibrary.org/obo/ENVO_01001000\tITEM\tHOST_ASSOCIATED\txref"]] |
| ESYNS | curation/definition_source_label_exclusions.tsv; TSV line 3 | supports | [[3, "habitatmech:PREGO.ce9c3a92e9\tflagellate\tflagellate-associated environment\tantigravity\t2026-11-09\tReview #2334: 'flagellate' names the organism form (BTO:0000464), not the environment associated with it. Suppress automatic retention of the displaced source label while preserving verbatim PREGO provenance and related source aliases."]] |
| EPREV | reviews/structured/20261109T181012Z-flagellate-record/review.yaml; Every immutable Stage 4 baseline finding | supports | Exact predecessor keys and findings reconciled; original inspected source scope preserved. |
| ETEST | tests/test_finger_to_free_living_state_review_repairs.py; Complete full-corpus counterfactual regression suite | supports | Exactly thirteen records differ from the counterfactual baseline across Issues #2334, #2335, and #2336. |
| EHIST_G1 | history/other/decisions/2026-11-09T214500Z-antigravity-233401.yaml; Complete curation session history event | supports | Authorized curation event for Issue #2334 recorded and validated. |

## Limits And Additional Notes

- Only the cited repository inputs, ontology terms, and source inventories were inspected; original specimen-level support for every upstream source assertion was not exhaustively reconstructed.
- Source counts, PREGO scores, and ranks are not prevalence, viability, mechanism, or characteristic presence.
- Configured label correspondence skipped 2,094 no-adapter pairs; this is not whole-corpus identifier certification.
- Read-only review: no curation table, generated habitat YAML, status, or history record was modified.
- Saved against working-tree repairs atop main commit 7c82566b001f676eb0d3c9cc6c905f85a99b8bde; all earlier saved bundles in reviews/structured/ remain byte-identical.
- Reconciles predecessor bundle 20261109T181012Z-flagellate-record with exact issue_key and previous_occurrences lineage.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T215002Z-flagellate-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: flagellate'
started_at: '2026-11-09T21:40:00Z'
finished_at: '2026-11-09T21:50:02Z'
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
summary: Un-grounded PREGO source concept habitatmech:PREGO.ce9c3a92e9 (BTO:0000464
  'flagellate') from organismal form term BTO:0000464 ('flagellate') via an ITEM-level
  CONFIRM_UNGROUNDED decision (target_id=BTO:0000464, relation=xref) in curation/decisions.tsv,
  defined 'flagellate-associated environment' under ENVO:01001000 ('environmental
  system determined by an organism', parent_mode REPLACE) in curation/term_requests.tsv,
  and excluded automatic retention of displaced source label 'flagellate' in curation/definition_source_label_exclusions.tsv
  (#2334). This removes non-habitat BTO parents BTO:0000720 (plant form) and BTO:0002503
  (protozoan form) from parent_habitats, keeps BTO:0000464 as a contextual xref, promotes
  status to REVIEWED/UNGROUNDED, and preserves all 9 retained PREGO characteristic
  taxa (9 TAXON assertions). Both predecessor findings (F1 and F2) are resolved.
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
  - path: reviews/structured/20261109T181012Z-flagellate-record/review.yaml
    sha256: 9d6910f015cf9010378bbd9038ccc96b3cd7d1af2196856049460ed706d4852b
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
- target_id: habitatmech:PREGO.ce9c3a92e9
  path: data/habitats/host_associated/flagellate.yaml
  label: flagellate-associated environment
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
    finding on data/habitats/host_associated/flagellate.yaml after bounded Cycle 8
    Stage 5 remediation.
  selection: One of thirteen repaired targets from the finger-through-free_living_state
    cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:PREGO.ce9c3a92e9
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
    --target-class HabitatRecord data/habitats/host_associated/flagellate.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:PREGO.ce9c3a92e9
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
  - habitatmech:PREGO.ce9c3a92e9
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
  - habitatmech:PREGO.ce9c3a92e9
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
  - habitatmech:PREGO.ce9c3a92e9
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
  - habitatmech:PREGO.ce9c3a92e9
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
  - habitatmech:PREGO.ce9c3a92e9
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
  - habitatmech:PREGO.ce9c3a92e9
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
  - habitatmech:PREGO.ce9c3a92e9
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
  - habitatmech:PREGO.ce9c3a92e9
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
  - habitatmech:PREGO.ce9c3a92e9
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
  - habitatmech:PREGO.ce9c3a92e9
  summary: Completed 2026-11-09T21:49:30Z. rendered 3209 habitat pages, 757 redirect
    stubs, 8 categories, 701 term requests; pages/ is in step with the corpus.
  scope_note: Full-corpus static site parity check.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/flagellate.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T21:50:02Z'
  support: supports
  summary: '{"identifier": "habitatmech:PREGO.ce9c3a92e9", "label": "flagellate-associated
    environment", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED",
    "definition": "An environmental system determined by a flagellate protozoan or
    alga.", "parent_habitats": ["ENVO:01001000"], "xrefs": ["BTO:0000464"], "synonyms":
    [{"synonym_text": "flagellate host environment", "synonym_type": "EXACT_SYNONYM",
    "source": "HabitatMech curation"}, {"synonym_text": "flagellates", "synonym_type":
    "RELATED_SYNONYM", "source": "PREGO"}], "source_attestations": [{"source": "PREGO",
    "source_id": "BTO:0000464", "source_label": "flagellate", "assertion_count": 9,
    "assertion_unit": "TAXON", "score": 3.0, "evidence_channels": "annotated_genomes_isolates"}],
    "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources",
    "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories;
    attested by PREGO. Grounding: UNGROUNDED."}, {"timestamp": "2026-11-09T00:00:00Z",
    "curator": "antigravity", "action": "CONFIRM_UNGROUNDED", "changes": "Confirmed
    UNGROUNDED: no ontology term fits this concept. BTO:0000464 ''flagellate'' kept
    as an xref. ITEM organism-form review #2334: PREGO BTO:0000464 (''flagellate'',
    ''A flagellate protozoan or alga.'') names a morphological organism form rather
    than a microbial habitat identity, and its BTO subclass parents BTO:0000720 (''plant
    form'') and BTO:0002503 (''protozoan form'') are organism-form classifications
    rather than habitat superclasses. Keep the stable source mint habitatmech:PREGO.ce9c3a92e9
    in HOST_ASSOCIATED with BTO:0000464 preserved as a contextual xref, and define
    ''flagellate-associated environment'' under ENVO:01001000 (''environmental system
    determined by an organism''). https://purl.obolibrary.org/obo/BTO_0000464 https://purl.obolibrary.org/obo/ENVO_01001000
    (source concept habitatmech:PREGO.ce9c3a92e9)"}, {"timestamp": "2026-11-09T00:00:00Z",
    "curator": "antigravity", "action": "DEFINED", "changes": "Defined as ''flagellate-associated
    environment'' under ENVO:01001000 ''environmental system determined by an organism''.
    Review #2334: define the organism-determined environmental system associated with
    a flagellate protozoan or alga under ENVO:01001000 (''environmental system determined
    by an organism'') with parent_mode REPLACE, keeping BTO:0000464 (''flagellate'')
    as a contextual xref and suppressing automatic retention of the bare organism-form
    source label ''flagellate'' as an exact synonym. https://purl.obolibrary.org/obo/BTO_0000464
    https://purl.obolibrary.org/obo/ENVO_01001000"}, {"timestamp": "2026-11-09T00:00:00Z",
    "curator": "antigravity", "action": "SOURCE_SYNONYM_EXCLUDED", "changes": "Omitted
    automatic retention of displaced source label ''flagellate'' when defining habitatmech:PREGO.ce9c3a92e9
    as ''flagellate-associated environment''. Verbatim source attestations are preserved.
    Review #2334: ''flagellate'' names the organism form (BTO:0000464), not the environment
    associated with it. Suppress automatic retention of the displaced source label
    while preserving verbatim PREGO provenance and related source aliases."}]}'
  snapshot_sha256: d0d8a90198899c9c97024913bd9932e4789230c7d11407363f7af15a79a1dcdc
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-09T21:50:02Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon, organism-form,
    and subcellular organelle terms cannot substitute for associated environments;
    parent_habitats must be strictly broader across all contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-09T21:50:02Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-09T21:50:02Z'
  support: supports
  summary: Seed generator produces identifier=habitatmech:PREGO.ce9c3a92e9, grounding_status=UNGROUNDED,
    mapping_status=REVIEWED, parent_habitats=["ENVO:01001000"], xrefs=["BTO:0000464"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: ESIB1
  kind: record_content
  reference: data/habitats/host_associated/adult.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T21:50:02Z'
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
  locator: TSV rows 340
  accessed_at: '2026-11-09T21:50:02Z'
  support: supports
  summary: '[{"data": {"biolink_category": "biolink:GrossAnatomicalStructure", "channels":
    "annotated_genomes_isolates", "direct_assertion_count": "9", "max_prego_score":
    "3", "ontology": "BTO", "prego_id": "BTO:0000464", "prego_synonyms": "flagellate|flagellates",
    "taxon_count": "9"}, "row": 340}]'
  snapshot_sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
- evidence_id: EPREGOTAXA
  kind: database
  reference: data/raw/prego_habitat_taxa.tsv
  locator: TSV rows 647,648,649,650,651,652,653,654,655
  accessed_at: '2026-11-09T21:50:02Z'
  support: supports
  summary: 9 PREGO taxon-association rows for BTO:0000464.
  snapshot_sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 465,721,2503
  accessed_at: '2026-11-09T21:50:02Z'
  support: supports
  summary: '[{"data": {"definition": "A flagellate protozoan or alga.", "deprecated":
    "", "directly_referenced": "TRUE", "label": "flagellate", "label_only": "FALSE",
    "ontology": "BTO", "synonyms": "", "term_id": "BTO:0000464"}, "row": 465}, {"data":
    {"definition": "", "deprecated": "", "directly_referenced": "FALSE", "label":
    "plant form", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id":
    "BTO:0000720"}, "row": 721}, {"data": {"definition": "Any individual of the Protozoa.",
    "deprecated": "", "directly_referenced": "FALSE", "label": "protozoan form", "label_only":
    "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0002503"}, "row":
    2503}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 69,112,195,305,306,327,336,462,475,488,682,715,728,792,836
  accessed_at: '2026-11-09T21:50:02Z'
  support: supports
  summary: '[{"data": {"object": "BTO:0002503", "predicate": "rdfs:subClassOf", "subject":
    "BTO:0000092"}, "row": 69}, {"data": {"object": "BTO:0000720", "predicate": "rdfs:subClassOf",
    "subject": "BTO:0000159"}, "row": 112}, {"data": {"object": "BTO:0000720", "predicate":
    "rdfs:subClassOf", "subject": "BTO:0000285"}, "row": 195}, {"data": {"object":
    "BTO:0000720", "predicate": "rdfs:subClassOf", "subject": "BTO:0000464"}, "row":
    305}, {"data": {"object": "BTO:0002503", "predicate": "rdfs:subClassOf", "subject":
    "BTO:0000464"}, "row": 306}, {"data": {"object": "BTO:0000720", "predicate": "rdfs:subClassOf",
    "subject": "BTO:0000495"}, "row": 327}, {"data": {"object": "BTO:0000720", "predicate":
    "rdfs:subClassOf", "subject": "BTO:0000514"}, "row": 336}, {"data": {"object":
    "BTO:0001461", "predicate": "rdfs:subClassOf", "subject": "BTO:0000720"}, "row":
    462}, {"data": {"object": "BTO:0000720", "predicate": "rdfs:subClassOf", "subject":
    "BTO:0000735"}, "row": 475}, {"data": {"object": "BTO:0002503", "predicate": "rdfs:subClassOf",
    "subject": "BTO:0000749"}, "row": 488}, {"data": {"object": "BTO:0000720", "predicate":
    "rdfs:subClassOf", "subject": "BTO:0001010"}, "row": 682}, {"data": {"object":
    "BTO:0000720", "predicate": "rdfs:subClassOf", "subject": "BTO:0001064"}, "row":
    715}, {"data": {"object": "BTO:0000720", "predicate": "rdfs:subClassOf", "subject":
    "BTO:0001084"}, "row": 728}, {"data": {"object": "BTO:0000720", "predicate": "rdfs:subClassOf",
    "subject": "BTO:0001171"}, "row": 792}, {"data": {"object": "BTO:0000720", "predicate":
    "rdfs:subClassOf", "subject": "BTO:0001228"}, "row": 836}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'flagellate|BTO:0000464' reviews/structured/*/review.yaml curation/
    history/
  accessed_at: '2026-11-09T21:50:02Z'
  support: context_only
  summary: Structured-review traversal located Stage 4 predecessor bundle 20261109T181012Z-flagellate-record
    (linked via EPREV and related_reviews) and checked related cohort and ancestor
    reviews for reconciliation.
  search_scope: curation, history, data/raw, and reviews/structured/*/review.yaml
    traversal at commit 7c82566b001f676eb0d3c9cc6c905f85a99b8bde.
- evidence_id: ETR
  kind: record_content
  reference: curation/term_requests.tsv
  locator: TSV line 677
  accessed_at: '2026-11-09T21:50:02Z'
  support: supports
  summary: '[[677, "habitatmech:PREGO.ce9c3a92e9\tflagellate-associated environment\tENVO:01001000\tenvironmental
    system determined by an organism\tAn environmental system determined by a flagellate
    protozoan or alga.\tflagellate host environment\tantigravity\t2026-11-09\tReview
    #2334: define the organism-determined environmental system associated with a flagellate
    protozoan or alga under ENVO:01001000 (''environmental system determined by an
    organism'') with parent_mode REPLACE, keeping BTO:0000464 (''flagellate'') as
    a contextual xref and suppressing automatic retention of the bare organism-form
    source label ''flagellate'' as an exact synonym. https://purl.obolibrary.org/obo/BTO_0000464
    https://purl.obolibrary.org/obo/ENVO_01001000\tREPLACE"]]'
  snapshot_sha256: 3703ae74d7565abdfb5a1fab47718b05c4fd02447b4ed60bbeb3bde65e1d8792
- evidence_id: EDEC
  kind: record_content
  reference: curation/decisions.tsv
  locator: TSV line 1843
  accessed_at: '2026-11-09T21:50:02Z'
  support: supports
  summary: '[[1843, "habitatmech:PREGO.ce9c3a92e9\tCONFIRM_UNGROUNDED\tBTO:0000464\tflagellate\t\tantigravity\t2026-11-09\tITEM
    organism-form review #2334: PREGO BTO:0000464 (''flagellate'', ''A flagellate
    protozoan or alga.'') names a morphological organism form rather than a microbial
    habitat identity, and its BTO subclass parents BTO:0000720 (''plant form'') and
    BTO:0002503 (''protozoan form'') are organism-form classifications rather than
    habitat superclasses. Keep the stable source mint habitatmech:PREGO.ce9c3a92e9
    in HOST_ASSOCIATED with BTO:0000464 preserved as a contextual xref, and define
    ''flagellate-associated environment'' under ENVO:01001000 (''environmental system
    determined by an organism''). https://purl.obolibrary.org/obo/BTO_0000464 https://purl.obolibrary.org/obo/ENVO_01001000\tITEM\tHOST_ASSOCIATED\txref"]]'
  snapshot_sha256: 8e0c9ea50c453b9b0eb86e9a6cf246dbc188714ec7a8cc37b2918d5373e6d2ae
- evidence_id: ESYNS
  kind: record_content
  reference: curation/definition_source_label_exclusions.tsv
  locator: TSV line 3
  accessed_at: '2026-11-09T21:50:02Z'
  support: supports
  summary: '[[3, "habitatmech:PREGO.ce9c3a92e9\tflagellate\tflagellate-associated
    environment\tantigravity\t2026-11-09\tReview #2334: ''flagellate'' names the organism
    form (BTO:0000464), not the environment associated with it. Suppress automatic
    retention of the displaced source label while preserving verbatim PREGO provenance
    and related source aliases."]]'
  snapshot_sha256: 84e5214713a21033312eb9c512fe38f44865662f934a4e679d45e827b16ff780
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261109T181012Z-flagellate-record/review.yaml
  locator: Every immutable Stage 4 baseline finding
  accessed_at: '2026-11-09T21:50:02Z'
  support: supports
  summary: Exact predecessor keys and findings reconciled; original inspected source
    scope preserved.
  snapshot_sha256: 9d6910f015cf9010378bbd9038ccc96b3cd7d1af2196856049460ed706d4852b
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_finger_to_free_living_state_review_repairs.py
  locator: Complete full-corpus counterfactual regression suite
  accessed_at: '2026-11-09T21:50:02Z'
  support: supports
  summary: 'Exactly thirteen records differ from the counterfactual baseline across
    Issues #2334, #2335, and #2336.'
  snapshot_sha256: 495a506d77d0f3c2484e16b510c233a7c8b108ae96cba6b6346252c3a9d01bdb
- evidence_id: EHIST_G1
  kind: record_content
  reference: history/other/decisions/2026-11-09T214500Z-antigravity-233401.yaml
  locator: Complete curation session history event
  accessed_at: '2026-11-09T21:50:02Z'
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
  - habitatmech:PREGO.ce9c3a92e9
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
  - ESEARCH
  - ETR
  - EDEC
  - ESYNS
  - EPREV
  - ETEST
  - EHIST_G1
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: supported
  summary: 'habitatmech:PREGO.ce9c3a92e9: flagellate-associated environment; UNGROUNDED/REVIEWED;
    parents ["ENVO:01001000"]. Un-grounded PREGO source concept habitatmech:PREGO.ce9c3a92e9
    (BTO:0000464 ''flagellate'') from organismal form term BTO:0000464 (''flagellate'')
    via an ITEM-level CONFIRM_UNGROUNDED decision (target_id=BTO:0000464, relation=xref)
    in curation/decisions.tsv, defined ''flagellate-associated environment'' under
    ENVO:01001000 (''environmental system determined by an organism'', parent_mode
    REPLACE) in curation/term_requests.tsv, and excluded automatic retention of displaced
    source label ''flagellate'' in curation/definition_source_label_exclusions.tsv
    (#2334). This removes non-habitat BTO parents BTO:0000720 (plant form) and BTO:0002503
    (protozoan form) from parent_habitats, keeps BTO:0000464 as a contextual xref,
    promotes status to REVIEWED/UNGROUNDED, and preserves all 9 retained PREGO characteristic
    taxa (9 TAXON assertions). Both predecessor findings (F1 and F2) are resolved.'
  target_ids:
  - habitatmech:PREGO.ce9c3a92e9
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
  - ESEARCH
  - ETR
  - EDEC
  - ESYNS
  - EPREV
  - ETEST
  - EHIST_G1
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks,
    and pools: [{"count": 9, "source": "PREGO", "unit": "TAXON"}]. Zero counts are
    omitted; unrelated parent counts are not combined.'
  target_ids:
  - habitatmech:PREGO.ce9c3a92e9
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
  - ESEARCH
  - ETR
  - EDEC
  - ESYNS
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
  - habitatmech:PREGO.ce9c3a92e9
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
  - ESEARCH
  - ETR
  - EDEC
  - ESYNS
  - EPREV
  - ETEST
  - EHIST_G1
- assessment_id: A5
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: Missing optional parameters/graphs are not evidence deficits. Full source
    decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only
    review does not mutate generated records.
  target_ids:
  - habitatmech:PREGO.ce9c3a92e9
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
  - ESEARCH
  - ETR
  - EDEC
  - ESYNS
  - EPREV
  - ETEST
  - EHIST_G1
findings:
- finding_id: F1
  issue_key: flagellate-organism-form-identity
  category: identity
  severity: blocker
  status: resolved
  certainty: confirmed
  title: Organism-form class BTO:0000464 (flagellate) is used as the habitat identity
  description: Under docs/CURATION.md, whole-organism and morphological organism-form
    classes cannot serve as habitat identity. Add an ITEM-level CONFIRM_UNGROUNDED
    row in curation/decisions.tsv for habitatmech:PREGO.ce9c3a92e9 with object_id=BTO:0000464,
    object_label=flagellate, relation=xref, category=HOST_ASSOCIATED; author a curated
    definition for 'flagellate-associated environment' ('An environmental system determined
    by a flagellate protozoan or alga.') under ENVO:01001000 (environmental system
    determined by an organism) with parent_mode=REPLACE in curation/term_requests.tsv;
    exclude bare source label 'flagellate' in curation/definition_source_label_exclusions.tsv;
    and update data/habitats/PATHS.tsv.
  target_ids:
  - habitatmech:PREGO.ce9c3a92e9
  field_paths:
  - identifier
  - label
  - definition
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
  - ESEARCH
  - ETR
  - EDEC
  - ESYNS
  - EPREV
  - ETEST
  - EHIST_G1
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
  normalization_reason: Whole-organism or organism-form identity is adopted as the
    habitat identity, contradicting the native host/environment rule.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2334
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261109T181012Z-flagellate-record
    finding_id: F1
  disposition_reason: Added ITEM-level CONFIRM_UNGROUNDED decision for habitatmech:PREGO.ce9c3a92e9
    (target_id=BTO:0000464 'flagellate', relation=xref) in curation/decisions.tsv,
    defined 'flagellate-associated environment' under ENVO:01001000 ('environmental
    system determined by an organism', parent_mode REPLACE) in curation/term_requests.tsv,
    and added a guarded source-label exclusion in curation/definition_source_label_exclusions.tsv
    (#2334).
- finding_id: F2
  issue_key: flagellate-organism-form-parents
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Organism-form classes BTO:0000720 (plant form) and BTO:0002503 (protozoan
    form) are asserted in parent_habitats
  description: BTO:0000720 (plant form) and BTO:0002503 (protozoan form) are morphological
    organism-form classes imported from BTO:0000464 rather than strictly broader microbial
    habitat superclasses. Resolving F1 by ungrounding habitatmech:PREGO.ce9c3a92e9
    and defining 'flagellate-associated environment' under ENVO:01001000 with parent_mode=REPLACE
    removes both organism-form parents.
  target_ids:
  - habitatmech:PREGO.ce9c3a92e9
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
  - ESEARCH
  - ETR
  - EDEC
  - ESYNS
  - EPREV
  - ETEST
  - EHIST_G1
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
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2334
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261109T181012Z-flagellate-record
    finding_id: F2
  disposition_reason: Resolved by un-grounding habitatmech:PREGO.ce9c3a92e9 from BTO:0000464
    and defining it under ENVO:01001000 ('environmental system determined by an organism',
    parent_mode REPLACE) in curation/term_requests.tsv (#2334), removing organism-form
    subclass parents BTO:0000720 (plant form) and BTO:0002503 (protozoan form) from
    parent_habitats.
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
- Reconciles predecessor bundle 20261109T181012Z-flagellate-record with exact issue_key
  and previous_occurrences lineage.
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261109T181012Z-flagellate-record
  relationship: Exact predecessor; every finding explicitly reconciled.
```
