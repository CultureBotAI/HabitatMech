# Remediation review: felidae_cat

- Review: 20261108T154502Z-felidae_cat-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-08T15:35:00Z
- Finished UTC: 2026-11-08T15:45:02Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Replaced the bare host label 'Felidae-Cat' in exact_synonym of curation/term_requests.tsv for habitatmech:BACDIVE.e6b73de092 ('felid-associated environment') with 'cat-associated environment&#124;feline host environment' and added a guarded exclusion row in curation/definition_source_label_exclusions.tsv (#2319) so automatic retention of the displaced host label is omitted from synonyms (SOURCE_SYNONYM_EXCLUDED) while preserving verbatim BacDive source_attestations, NCBITaxon:9681 xref, parent ENVO:01001002, and native REVIEWED/UNGROUNDED status. No unresolved predecessor finding remains in this target scope.

## Scope And Provenance

Full current target assessment and explicit disposition of every baseline finding on data/habitats/host_associated/felidae_cat.yaml after bounded Cycle 7 Stage 5 remediation.

Selection: One of seven repaired targets from the fecal__0d8696a2-through-fin cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8e2744f4c33769669e5e9a66a4ae9e27a9642590.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:BACDIVE.e6b73de092 | data/habitats/host_associated/felidae_cat.yaml | generated | felid-associated environment |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:BACDIVE.e6b73de092 | Completed 2026-11-08T15:42:12Z. No issues found against src/habitatmech/schema/habitatmech.yaml. |
| validate-strict | passed | True | habitatmech:BACDIVE.e6b73de092 | Completed 2026-11-08T15:42:18Z. 24 checked, 0 failed; target passed closed-schema validation. |
| validate-history | passed | True | habitatmech:BACDIVE.e6b73de092 | Completed 2026-11-08T15:42:25Z. No issues found; 872 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | habitatmech:BACDIVE.e6b73de092 | Completed 2026-11-08T15:42:30Z. 14 inventory files and 2 GOLD export files verified. |
| verify-corpus | passed | True | habitatmech:BACDIVE.e6b73de092 | Completed 2026-11-08T15:42:40Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | habitatmech:BACDIVE.e6b73de092 | Completed 2026-11-08T15:42:45Z. 93 causal-graph curations and target records validated. |
| term-requests-check | passed | True | habitatmech:BACDIVE.e6b73de092 | Completed 2026-11-08T15:42:50Z. term-request table is current (674 terms). |
| validate-products | passed | True | habitatmech:BACDIVE.e6b73de092 | Completed 2026-11-08T15:42:55Z. 24 records, 0 label drift findings. |
| pytest counterfactual review repairs | passed | True | habitatmech:BACDIVE.e6b73de092 | Completed 2026-11-08T15:43:00Z. 2 passed; exact 7-record counterfactual diff verified. |
| curation-floor | passed | True | habitatmech:BACDIVE.e6b73de092 | Completed 2026-11-08T15:43:05Z. Floor satisfied across all 13 metrics. |
| render-check | passed | True | habitatmech:BACDIVE.e6b73de092 | Completed 2026-11-08T15:44:50Z. rendered 3209 habitat pages, 753 redirect stubs, 8 categories, 699 term requests; pages/ is in step with the corpus. |

## Scientific And Domain Assessments

### Native validity and reproduction after bounded remediation

schema: supported. Targets: habitatmech:BACDIVE.e6b73de092.

Individual schema, strict 24-target validation, 872 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 93 causal overlays, 674 term requests, curation floor, site parity, and counterfactual regression tests passed.

### Identity, definition, hierarchy and aliases

identity: supported. Targets: habitatmech:BACDIVE.e6b73de092.

habitatmech:BACDIVE.e6b73de092: felid-associated environment; UNGROUNDED/REVIEWED; parents ["ENVO:01001002"]. Replaced the bare host label 'Felidae-Cat' in exact_synonym of curation/term_requests.tsv for habitatmech:BACDIVE.e6b73de092 ('felid-associated environment') with 'cat-associated environment&#124;feline host environment' and added a guarded exclusion row in curation/definition_source_label_exclusions.tsv (#2319) so automatic retention of the displaced host label is omitted from synonyms (SOURCE_SYNONYM_EXCLUDED) while preserving verbatim BacDive source_attestations, NCBITaxon:9681 xref, parent ENVO:01001002, and native REVIEWED/UNGROUNDED status. No unresolved predecessor finding remains in this target scope.

### Source counts and retained ranking

quantity: supported. Targets: habitatmech:BACDIVE.e6b73de092.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"source": "BACDIVE", "count": 95, "unit": "STRAIN"}]. Zero counts are omitted; unrelated parent counts are not combined.

### Predecessor finding reconciliation

representation: supported. Targets: habitatmech:BACDIVE.e6b73de092.

Every predecessor finding preserves its stable issue_key and exact lineage. All predecessor findings in this target scope are resolved.

### Parameters, mechanisms and native status

completeness: supported. Targets: habitatmech:BACDIVE.e6b73de092.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only review does not mutate generated records.

## Findings

### F1: Felid-associated environment asserts host-taxon label 'Felidae-Cat' as an exact synonym

major / resolved / confirmed; issue key: felidae-cat-host-name-exact-synonym.

Replace 'Felidae-Cat' in exact_synonym of curation/term_requests.tsv row 46 for habitatmech:BACDIVE.e6b73de092 (e.g. with 'cat-associated environment&#124;feline host environment') and add a guarded exclusion row in curation/definition_source_label_exclusions.tsv (source_label 'Felidae-Cat', requested_label 'felid-associated environment') so automatic retention of the displaced BacDive host label 'Felidae-Cat' as an EXACT_SYNONYM is omitted from synonyms (SOURCE_SYNONYM_EXCLUDED) while preserving verbatim source_attestations.

Disposition: Replaced bare host label 'Felidae-Cat' in exact_synonym of curation/term_requests.tsv for habitatmech:BACDIVE.e6b73de092 with 'cat-associated environment&#124;feline host environment' and added a guarded exclusion row in curation/definition_source_label_exclusions.tsv (#2319) so automatic retention of the displaced host label is omitted from synonyms (SOURCE_SYNONYM_EXCLUDED) while preserving verbatim BacDive source_attestations.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/felidae_cat.yaml; Entire YAML | supports | {"identifier": "habitatmech:BACDIVE.e6b73de092", "label": "felid-associated environment", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED", "parent_habitats": ["ENVO:01001002"], "xrefs": ["NCBITaxon:9681"], "synonyms": [{"synonym_text": "cat-associated environment", "synonym_type": "EXACT_SYNONYM", "source": "HabitatMech curation"}, {"synonym_text": "feline host environment", "synonym_type": "EXACT_SYNONYM", "source": "HabitatMech curation"}], "source_attestations": [{"source": "BACDIVE", "source_id": "bacdive.isolation_source:felidae-cat", "source_label": "Felidae-Cat", "assertion_count": 95, "assertion_unit": "STRAIN", "notes": "Upstream mapping targets a non-habitat ontology (NCBITaxon:9681); kept as an xref."}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by BACDIVE. Grounding: UNGROUNDED."}, {"timestamp": "2026-08-26T00:00:00Z", "curator": "claude-opus-5", "action": "CONFIRM_UNGROUNDED", "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. NCBITaxon:9681 'Felidae' kept as an xref. Host-taxon reversal (#114) reaching the last members of its own family (#194): this was NOT_APPLICABLE, which asserts the source concept is not a habitat. An organism acting as a host IS a habitat, and the corpus already says so for bovine, caprine, equid, leporid and suid, all minted with ENVO:01001002 'animal-associated environment' as parent and the organism term as an xref. Never curated on the question at all: the NOT_APPLICABLE was the seeder's automatic bacdive_non_habitat_target route firing on an NCBITaxon target, and #114's sweep did not reach this row. The taxon term is not the identity - a family is a class of organisms, not a place - so it stays an xref (#99) and the concept keeps its minted identity with a term request. Category HOST_ASSOCIATED: the host is living. (source concept habitatmech:BACDIVE.e6b73de092)"}, {"timestamp": "2026-11-08T00:00:00Z", "curator": "antigravity", "action": "DEFINED", "changes": "Defined as 'felid-associated environment' under ENVO:01001002 'animal-associated environment'. Definition follows the established &lt;clade&gt;-associated environment family for BacDive host buckets, whose naming rule the corpus already fixes: a -inae source label yields -ine (Bovinae-Cow,-Cattle -&gt; bovine) and a -idae source label yields -id (Equidae-Horse -&gt; equid, Leporidae-Rabbit/Hare -&gt; leporid, Suidae-Pig,Swine -&gt; suid). No deep-research run was commissioned: the genus, the wording pattern and the near-miss reasoning are already settled by those five siblings and by NCBITaxon, so a billed report would add nothing this slice turns on. Worded like the equid sibling for the same reason as the canid row: NCBITaxon:9681 'Felidae' is wider than the domestic cat the source label names. Review https://github.com/CultureBotAI/HabitatMech/issues/2319 : replaced bare host label Felidae-Cat in exact_synonym with cat-associated environment&#124;feline host environment and guarded fallback exclusion in curation/definition_source_label_exclusions.tsv."}, {"timestamp": "2026-11-08T00:00:00Z", "curator": "antigravity", "action": "SOURCE_SYNONYM_EXCLUDED", "changes": "Omitted automatic retention of displaced source label 'Felidae-Cat' when defining habitatmech:BACDIVE.e6b73de092 as 'felid-associated environment'. Verbatim source attestations are preserved. Review https://github.com/CultureBotAI/HabitatMech/issues/2319 : The displaced label names the determining hosts (Felidae-Cat), not their associated environment. Suppress exact-alias fallback; preserve verbatim source provenance, definition, genus and native status."}]} |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon and life-stage organism terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=habitatmech:BACDIVE.e6b73de092, grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["ENVO:01001002"], xrefs=["NCBITaxon:9681"]. |
| ESIB1 | data/habitats/host_associated/canidae_dog.yaml; Entire YAML | supports | Sibling BacDive host-bucket record habitatmech:BACDIVE.6e1687d7d0 (canid-associated environment) where displaced host-taxon label 'Canidae-Dog' was omitted from exact synonyms via curation/definition_source_label_exclusions.tsv (#2197). |
| ESIB2 | data/habitats/host_associated/equidae_horse.yaml; Entire YAML | supports | Sibling BacDive host-bucket record habitatmech:BACDIVE.7d4c0576bf (equid-associated environment) where displaced host-taxon label 'Equidae-Horse' was omitted from exact synonyms via curation/definition_source_label_exclusions.tsv (#2286). |
| EBACDIVE | data/raw/bacdive_isolation_sources.tsv; TSV rows 73 | supports | [{"data": {"bacdive_id": "bacdive.isolation_source:felidae-cat", "label": "Felidae-Cat", "source_slug": "felidae-cat", "strain_count": "95", "taxon_count": "59"}, "row": 73}] |
| EGROUND | data/raw/isolation_source_groundings.tsv; TSV rows 111 | supports | [{"data": {"confidence": "medium", "curator": "ols4_auto", "mapping_justification": "semapv:LexicalMatching", "object_id": "NCBITaxon:9681", "object_label": "Felidae", "object_source": "NCBITaxon", "predicate_id": "skos:closeMatch", "source_dataset": "bacdive", "subject_label": "Felidae-Cat", "subject_label_normalized": "felidae cat", "verified_date": "2026-05-01"}, "row": 111}] |
| EONT | data/raw/ontology_terms.tsv; TSV rows 8491,10767 | supports | [{"data": {"definition": "An environmental system determined by an animal.", "deprecated": "", "directly_referenced": "TRUE", "label": "animal-associated environment", "label_only": "FALSE", "ontology": "ENVO", "synonyms": "Metazoan-associated environment&#124;animal environment", "term_id": "ENVO:01001002"}, "row": 8491}, {"data": {"definition": "", "deprecated": "", "directly_referenced": "TRUE", "label": "Felidae", "label_only": "TRUE", "ontology": "NCBITaxon", "synonyms": "", "term_id": "NCBITaxon:9681"}, "row": 10767}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 6797,6992,6996,7704 | supports | [{"data": {"object": "ENVO:01001000", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001002"}, "row": 6797}, {"data": {"object": "ENVO:01001002", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001176"}, "row": 6992}, {"data": {"object": "ENVO:01001002", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001179"}, "row": 6996}, {"data": {"object": "ENVO:01001002", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001829"}, "row": 7704}] |
| EDEC | curation/decisions.tsv; TSV line 1835 | supports | [[1835, "habitatmech:BACDIVE.e6b73de092\tCONFIRM_UNGROUNDED\tNCBITaxon:9681\tFelidae\t\tclaude-opus-5\t2026-08-26\tHost-taxon reversal (#114) reaching the last members of its own family (#194): this was NOT_APPLICABLE, which asserts the source concept is not a habitat. An organism acting as a host IS a habitat, and the corpus already says so for bovine, caprine, equid, leporid and suid, all minted with ENVO:01001002 'animal-associated environment' as parent and the organism term as an xref. Never curated on the question at all: the NOT_APPLICABLE was the seeder's automatic bacdive_non_habitat_target route firing on an NCBITaxon target, and #114's sweep did not reach this row. The taxon term is not the identity - a family is a class of organisms, not a place - so it stays an xref (#99) and the concept keeps its minted identity with a term request. Category HOST_ASSOCIATED: the host is living.\tITEM\tHOST_ASSOCIATED\txref"]] |
| ETR | curation/term_requests.tsv; TSV line 46 | supports | [[46, "habitatmech:BACDIVE.e6b73de092\tfelid-associated environment\tENVO:01001002\tanimal-associated environment\tAn animal-associated environment which is determined by a cat or other felid.\tcat-associated environment&#124;feline host environment\tantigravity\t2026-11-08\tDefinition follows the established &lt;clade&gt;-associated environment family for BacDive host buckets, whose naming rule the corpus already fixes: a -inae source label yields -ine (Bovinae-Cow,-Cattle -&gt; bovine) and a -idae source label yields -id (Equidae-Horse -&gt; equid, Leporidae-Rabbit/Hare -&gt; leporid, Suidae-Pig,Swine -&gt; suid). No deep-research run was commissioned: the genus, the wording pattern and the near-miss reasoning are already settled by those five siblings and by NCBITaxon, so a billed report would add nothing this slice turns on. Worded like the equid sibling for the same reason as the canid row: NCBITaxon:9681 'Felidae' is wider than the domestic cat the source label names. Review https://github.com/CultureBotAI/HabitatMech/issues/2319 : replaced bare host label Felidae-Cat in exact_synonym with cat-associated environment&#124;feline host environment and guarded fallback exclusion in curation/definition_source_label_exclusions.tsv.\tADD"]] |
| EP1 | data/habitats/other/animal_associated_environment.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": "An environmental system determined by an animal.", "grounding_status": "EXACT", "identifier": "ENVO:01001002", "label": "animal-associated environment", "mapping_status": "SEEDED", "parent_habitats": ["ENVO:01001000"], "source_attestations": [{"notes": "Physicochemical parameter bands from kg-microbe's environment table.", "source": "ENVIRONMENTS_TABLE", "source_id": "host_animal", "source_label": "host_animal"}, {"assertion_count": 144, "assertion_unit": "TAXON", "source": "MADIN", "source_id": "ENVO:01001002", "source_label": "animal-associated environment"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'felidae_cat&#124;habitatmech:BACDIVE.e6b73de092' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal located Stage 4 predecessor bundle 20261108T114919Z-felidae_cat-record (linked via EPREV and related_reviews) and checked related cohort and ancestor reviews for reconciliation. |
| ESYNS | curation/definition_source_label_exclusions.tsv; TSV line 2 | supports | [[2, "habitatmech:BACDIVE.e6b73de092\tFelidae-Cat\tfelid-associated environment\tantigravity\t2026-11-08\tReview https://github.com/CultureBotAI/HabitatMech/issues/2319 : The displaced label names the determining hosts (Felidae-Cat), not their associated environment. Suppress exact-alias fallback; preserve verbatim source provenance, definition, genus and native status."]] |
| EPREV | reviews/structured/20261108T114919Z-felidae_cat-record/review.yaml; Every immutable Stage 4 baseline finding | supports | Exact predecessor keys and findings reconciled; original inspected source scope preserved. |
| ETEST | tests/test_fecal_0d8696a2_to_fin_review_repairs.py; Complete full-corpus counterfactual regression suite | supports | Exactly seven records differ from the counterfactual baseline across Issues #2318 and #2319. |
| EHIST_G2 | history/other/definition_source_label_exclusions/2026-11-08T153510Z-antigravity-231901.yaml; Complete curation session history event | supports | Authorized curation event for Issue #2319 recorded and validated. |

## Limits And Additional Notes

- Only the stated primary evidence and current ontology/taxonomy authorities were independently inspected; original specimen-level support for every source-bin member is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism or characteristic presence. Parent observations are not inherited by children.
- Configured label correspondence skipped 2,088 no-adapter pairs; this is not whole-corpus identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in this pre-save observation.
- iModulonDB is not applicable: the target has no gene, regulator or expression-module assertion. No paid research or scientific-status promotion was performed.
- Saved against working-tree repairs atop main commit 8e2744f4c33769669e5e9a66a4ae9e27a9642590; all earlier saved bundles in reviews/structured/ remain byte-identical.
- Reconciles predecessor bundle 20261108T114919Z-felidae_cat-record with exact issue_key and previous_occurrences lineage.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261108T154502Z-felidae_cat-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: felidae_cat'
started_at: '2026-11-08T15:35:00Z'
finished_at: '2026-11-08T15:45:02Z'
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
summary: Replaced the bare host label 'Felidae-Cat' in exact_synonym of curation/term_requests.tsv
  for habitatmech:BACDIVE.e6b73de092 ('felid-associated environment') with 'cat-associated
  environment|feline host environment' and added a guarded exclusion row in curation/definition_source_label_exclusions.tsv
  (#2319) so automatic retention of the displaced host label is omitted from synonyms
  (SOURCE_SYNONYM_EXCLUDED) while preserving verbatim BacDive source_attestations,
  NCBITaxon:9681 xref, parent ENVO:01001002, and native REVIEWED/UNGROUNDED status.
  No unresolved predecessor finding remains in this target scope.
source:
  git_revision: 8e2744f4c33769669e5e9a66a4ae9e27a9642590
  state: working_tree
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
  - path: data/habitats/host_associated/canidae_dog.yaml
    sha256: 87552b6a21a0c1b436ff9e38322f21fa5c657e3c23eb4b0aaf56e62b32c03172
    role: context
  - path: data/habitats/host_associated/equidae_horse.yaml
    sha256: ae6e646baf0a68a68a1c29c09e7202810fc6a0c656dd1d23f6742adef673cd2f
    role: context
  - path: data/habitats/host_associated/felidae_cat.yaml
    sha256: daf5f03c2f0b7d4b212d5fea484cd29724e0d0d2e45431deffb8aab8e8211667
    role: target
  - path: data/habitats/other/animal_associated_environment.yaml
    sha256: a1cf41f43f9bece44dfb3e5d6ab0ca86858df67b88ee25d6ada260cccac69e16
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
  - path: history/other/definition_source_label_exclusions/2026-11-08T153510Z-antigravity-231901.yaml
    sha256: e28d82abe703f19ad589f62f7e93ca573a8ebb71bfab13030a83059e974d2126
    role: context
  - path: history/other/gold_parent_exclusions/2026-11-08T153500Z-antigravity-231801.yaml
    sha256: 0238f5404c80e4c6e0f01acbaf496cb3a6a304632fe3c51122e348ea0e39c919
    role: context
  - path: reviews/structured/20261108T114919Z-felidae_cat-record/review.yaml
    sha256: b7eed05671f6ff23b060078283adcea2d7a85c5e49cb0d322020ab3c9dfac989
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
    role: context
  - path: src/habitatmech/seed.py
    sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
    role: context
  - path: tests/test_fecal_0d8696a2_to_fin_review_repairs.py
    sha256: db50d90f8a6296e1914051aa62fe928ab03d264f44cc8cbfb1c822f9f9ec650c
    role: context
targets:
- target_id: habitatmech:BACDIVE.e6b73de092
  path: data/habitats/host_associated/felidae_cat.yaml
  label: felid-associated environment
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
    finding on data/habitats/host_associated/felidae_cat.yaml after bounded Cycle
    7 Stage 5 remediation.
  selection: One of seven repaired targets from the fecal__0d8696a2-through-fin cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:BACDIVE.e6b73de092
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
    --target-class HabitatRecord data/habitats/host_associated/felidae_cat.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.e6b73de092
  summary: Completed 2026-11-08T15:42:12Z. No issues found against src/habitatmech/schema/habitatmech.yaml.
  scope_note: Individual schema; strict command covers the 24 named cohort targets;
    other documented gates have full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/habitats/host_associated/fecal__0d8696a2.yaml
    data/habitats/host_associated/fecal__0e10427f.yaml data/habitats/host_associated/fecal__69dad039.yaml
    data/habitats/host_associated/fecal__89494a72.yaml data/habitats/host_associated/fecal__c047ee1e.yaml
    data/habitats/host_associated/fecal__ceae17b6.yaml data/habitats/host_associated/fecal__d12909cd.yaml
    data/habitats/host_associated/fecal__e9f04eec.yaml data/habitats/host_associated/feces.yaml
    data/habitats/host_associated/felidae_cat.yaml data/habitats/host_associated/female_reproductive_system.yaml
    data/habitats/host_associated/fetal_tissue.yaml data/habitats/host_associated/fetal_tissue__610eb0c8.yaml
    data/habitats/host_associated/fetus.yaml data/habitats/host_associated/fetus__250e9844.yaml
    data/habitats/host_associated/fiber.yaml data/habitats/host_associated/fibroblast.yaml
    data/habitats/host_associated/fibrocartilage.yaml data/habitats/host_associated/fibrocartilage__9cc92423.yaml
    data/habitats/host_associated/fibroma.yaml data/habitats/host_associated/filament.yaml
    data/habitats/host_associated/filiform_warts.yaml data/habitats/host_associated/filter_chamber.yaml
    data/habitats/host_associated/fin.yaml --out .temp/c7s4_24_strict.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.e6b73de092
  summary: Completed 2026-11-08T15:42:18Z. 24 checked, 0 failed; target passed closed-schema
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
  - habitatmech:BACDIVE.e6b73de092
  summary: Completed 2026-11-08T15:42:25Z. No issues found; 872 history record(s)
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
  - habitatmech:BACDIVE.e6b73de092
  summary: Completed 2026-11-08T15:42:30Z. 14 inventory files and 2 GOLD export files
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
  - habitatmech:BACDIVE.e6b73de092
  summary: 'Completed 2026-11-08T15:42:40Z. expected 3209 records, found 3209 on disk;
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
  - habitatmech:BACDIVE.e6b73de092
  summary: Completed 2026-11-08T15:42:45Z. 93 causal-graph curations and target records
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
  - habitatmech:BACDIVE.e6b73de092
  summary: Completed 2026-11-08T15:42:50Z. term-request table is current (674 terms).
  scope_note: Full-corpus term-request table currency check.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.e6b73de092
  summary: Completed 2026-11-08T15:42:55Z. 24 records, 0 label drift findings.
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
- check_id: C9
  name: pytest counterfactual review repairs
  status: passed
  required: true
  command: .venv/bin/python -m pytest tests/test_fecal_0d8696a2_to_fin_review_repairs.py
    -q --no-cov
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.e6b73de092
  summary: Completed 2026-11-08T15:43:00Z. 2 passed; exact 7-record counterfactual
    diff verified.
  scope_note: 'Full-corpus counterfactual regression test for Issues #2318 and #2319.'
- check_id: C10
  name: curation-floor
  status: passed
  required: true
  command: .venv/bin/python scripts/check_curation_floor.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.e6b73de092
  summary: Completed 2026-11-08T15:43:05Z. Floor satisfied across all 13 metrics.
  scope_note: Full-corpus curation floor ratchets.
- check_id: C11
  name: render-check
  status: passed
  required: true
  command: .venv/bin/python scripts/render_pages.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.e6b73de092
  summary: Completed 2026-11-08T15:44:50Z. rendered 3209 habitat pages, 753 redirect
    stubs, 8 categories, 699 term requests; pages/ is in step with the corpus.
  scope_note: Full-corpus static site parity check.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/felidae_cat.yaml
  locator: Entire YAML
  accessed_at: '2026-11-08T15:45:02Z'
  support: supports
  summary: '{"identifier": "habitatmech:BACDIVE.e6b73de092", "label": "felid-associated
    environment", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED",
    "parent_habitats": ["ENVO:01001002"], "xrefs": ["NCBITaxon:9681"], "synonyms":
    [{"synonym_text": "cat-associated environment", "synonym_type": "EXACT_SYNONYM",
    "source": "HabitatMech curation"}, {"synonym_text": "feline host environment",
    "synonym_type": "EXACT_SYNONYM", "source": "HabitatMech curation"}], "source_attestations":
    [{"source": "BACDIVE", "source_id": "bacdive.isolation_source:felidae-cat", "source_label":
    "Felidae-Cat", "assertion_count": 95, "assertion_unit": "STRAIN", "notes": "Upstream
    mapping targets a non-habitat ontology (NCBITaxon:9681); kept as an xref."}],
    "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources",
    "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories;
    attested by BACDIVE. Grounding: UNGROUNDED."}, {"timestamp": "2026-08-26T00:00:00Z",
    "curator": "claude-opus-5", "action": "CONFIRM_UNGROUNDED", "changes": "Confirmed
    UNGROUNDED: no ontology term fits this concept. NCBITaxon:9681 ''Felidae'' kept
    as an xref. Host-taxon reversal (#114) reaching the last members of its own family
    (#194): this was NOT_APPLICABLE, which asserts the source concept is not a habitat.
    An organism acting as a host IS a habitat, and the corpus already says so for
    bovine, caprine, equid, leporid and suid, all minted with ENVO:01001002 ''animal-associated
    environment'' as parent and the organism term as an xref. Never curated on the
    question at all: the NOT_APPLICABLE was the seeder''s automatic bacdive_non_habitat_target
    route firing on an NCBITaxon target, and #114''s sweep did not reach this row.
    The taxon term is not the identity - a family is a class of organisms, not a place
    - so it stays an xref (#99) and the concept keeps its minted identity with a term
    request. Category HOST_ASSOCIATED: the host is living. (source concept habitatmech:BACDIVE.e6b73de092)"},
    {"timestamp": "2026-11-08T00:00:00Z", "curator": "antigravity", "action": "DEFINED",
    "changes": "Defined as ''felid-associated environment'' under ENVO:01001002 ''animal-associated
    environment''. Definition follows the established <clade>-associated environment
    family for BacDive host buckets, whose naming rule the corpus already fixes: a
    -inae source label yields -ine (Bovinae-Cow,-Cattle -> bovine) and a -idae source
    label yields -id (Equidae-Horse -> equid, Leporidae-Rabbit/Hare -> leporid, Suidae-Pig,Swine
    -> suid). No deep-research run was commissioned: the genus, the wording pattern
    and the near-miss reasoning are already settled by those five siblings and by
    NCBITaxon, so a billed report would add nothing this slice turns on. Worded like
    the equid sibling for the same reason as the canid row: NCBITaxon:9681 ''Felidae''
    is wider than the domestic cat the source label names. Review https://github.com/CultureBotAI/HabitatMech/issues/2319
    : replaced bare host label Felidae-Cat in exact_synonym with cat-associated environment|feline
    host environment and guarded fallback exclusion in curation/definition_source_label_exclusions.tsv."},
    {"timestamp": "2026-11-08T00:00:00Z", "curator": "antigravity", "action": "SOURCE_SYNONYM_EXCLUDED",
    "changes": "Omitted automatic retention of displaced source label ''Felidae-Cat''
    when defining habitatmech:BACDIVE.e6b73de092 as ''felid-associated environment''.
    Verbatim source attestations are preserved. Review https://github.com/CultureBotAI/HabitatMech/issues/2319
    : The displaced label names the determining hosts (Felidae-Cat), not their associated
    environment. Suppress exact-alias fallback; preserve verbatim source provenance,
    definition, genus and native status."}]}'
  snapshot_sha256: daf5f03c2f0b7d4b212d5fea484cd29724e0d0d2e45431deffb8aab8e8211667
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-08T15:45:02Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon and life-stage
    organism terms cannot substitute for associated environments; parent_habitats
    must be strictly broader across all contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-08T15:45:02Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-08T15:45:02Z'
  support: supports
  summary: Seed generator produces identifier=habitatmech:BACDIVE.e6b73de092, grounding_status=UNGROUNDED,
    mapping_status=REVIEWED, parent_habitats=["ENVO:01001002"], xrefs=["NCBITaxon:9681"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: ESIB1
  kind: record_content
  reference: data/habitats/host_associated/canidae_dog.yaml
  locator: Entire YAML
  accessed_at: '2026-11-08T15:45:02Z'
  support: supports
  summary: Sibling BacDive host-bucket record habitatmech:BACDIVE.6e1687d7d0 (canid-associated
    environment) where displaced host-taxon label 'Canidae-Dog' was omitted from exact
    synonyms via curation/definition_source_label_exclusions.tsv (#2197).
  snapshot_sha256: 87552b6a21a0c1b436ff9e38322f21fa5c657e3c23eb4b0aaf56e62b32c03172
- evidence_id: ESIB2
  kind: record_content
  reference: data/habitats/host_associated/equidae_horse.yaml
  locator: Entire YAML
  accessed_at: '2026-11-08T15:45:02Z'
  support: supports
  summary: Sibling BacDive host-bucket record habitatmech:BACDIVE.7d4c0576bf (equid-associated
    environment) where displaced host-taxon label 'Equidae-Horse' was omitted from
    exact synonyms via curation/definition_source_label_exclusions.tsv (#2286).
  snapshot_sha256: ae6e646baf0a68a68a1c29c09e7202810fc6a0c656dd1d23f6742adef673cd2f
- evidence_id: EBACDIVE
  kind: database
  reference: data/raw/bacdive_isolation_sources.tsv
  locator: TSV rows 73
  accessed_at: '2026-11-08T15:45:02Z'
  support: supports
  summary: '[{"data": {"bacdive_id": "bacdive.isolation_source:felidae-cat", "label":
    "Felidae-Cat", "source_slug": "felidae-cat", "strain_count": "95", "taxon_count":
    "59"}, "row": 73}]'
  snapshot_sha256: fb1645dd899a43130be9cf38b0e8b27ffbaa0175306917bff20e20ee225875fc
- evidence_id: EGROUND
  kind: database
  reference: data/raw/isolation_source_groundings.tsv
  locator: TSV rows 111
  accessed_at: '2026-11-08T15:45:02Z'
  support: supports
  summary: '[{"data": {"confidence": "medium", "curator": "ols4_auto", "mapping_justification":
    "semapv:LexicalMatching", "object_id": "NCBITaxon:9681", "object_label": "Felidae",
    "object_source": "NCBITaxon", "predicate_id": "skos:closeMatch", "source_dataset":
    "bacdive", "subject_label": "Felidae-Cat", "subject_label_normalized": "felidae
    cat", "verified_date": "2026-05-01"}, "row": 111}]'
  snapshot_sha256: ab6a997359aab961c40928f9b13e06adb6dc43124fa3de821819570dd87f43b8
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 8491,10767
  accessed_at: '2026-11-08T15:45:02Z'
  support: supports
  summary: '[{"data": {"definition": "An environmental system determined by an animal.",
    "deprecated": "", "directly_referenced": "TRUE", "label": "animal-associated environment",
    "label_only": "FALSE", "ontology": "ENVO", "synonyms": "Metazoan-associated environment|animal
    environment", "term_id": "ENVO:01001002"}, "row": 8491}, {"data": {"definition":
    "", "deprecated": "", "directly_referenced": "TRUE", "label": "Felidae", "label_only":
    "TRUE", "ontology": "NCBITaxon", "synonyms": "", "term_id": "NCBITaxon:9681"},
    "row": 10767}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 6797,6992,6996,7704
  accessed_at: '2026-11-08T15:45:02Z'
  support: supports
  summary: '[{"data": {"object": "ENVO:01001000", "predicate": "rdfs:subClassOf",
    "subject": "ENVO:01001002"}, "row": 6797}, {"data": {"object": "ENVO:01001002",
    "predicate": "rdfs:subClassOf", "subject": "ENVO:01001176"}, "row": 6992}, {"data":
    {"object": "ENVO:01001002", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001179"},
    "row": 6996}, {"data": {"object": "ENVO:01001002", "predicate": "rdfs:subClassOf",
    "subject": "ENVO:01001829"}, "row": 7704}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EDEC
  kind: database
  reference: curation/decisions.tsv
  locator: TSV line 1835
  accessed_at: '2026-11-08T15:45:02Z'
  support: supports
  summary: '[[1835, "habitatmech:BACDIVE.e6b73de092\tCONFIRM_UNGROUNDED\tNCBITaxon:9681\tFelidae\t\tclaude-opus-5\t2026-08-26\tHost-taxon
    reversal (#114) reaching the last members of its own family (#194): this was NOT_APPLICABLE,
    which asserts the source concept is not a habitat. An organism acting as a host
    IS a habitat, and the corpus already says so for bovine, caprine, equid, leporid
    and suid, all minted with ENVO:01001002 ''animal-associated environment'' as parent
    and the organism term as an xref. Never curated on the question at all: the NOT_APPLICABLE
    was the seeder''s automatic bacdive_non_habitat_target route firing on an NCBITaxon
    target, and #114''s sweep did not reach this row. The taxon term is not the identity
    - a family is a class of organisms, not a place - so it stays an xref (#99) and
    the concept keeps its minted identity with a term request. Category HOST_ASSOCIATED:
    the host is living.\tITEM\tHOST_ASSOCIATED\txref"]]'
  snapshot_sha256: d3bf0a3ca3570e8f318898db92f800a1e13220f64112fe5c1ce1edc9181c3ae2
- evidence_id: ETR
  kind: database
  reference: curation/term_requests.tsv
  locator: TSV line 46
  accessed_at: '2026-11-08T15:45:02Z'
  support: supports
  summary: '[[46, "habitatmech:BACDIVE.e6b73de092\tfelid-associated environment\tENVO:01001002\tanimal-associated
    environment\tAn animal-associated environment which is determined by a cat or
    other felid.\tcat-associated environment|feline host environment\tantigravity\t2026-11-08\tDefinition
    follows the established <clade>-associated environment family for BacDive host
    buckets, whose naming rule the corpus already fixes: a -inae source label yields
    -ine (Bovinae-Cow,-Cattle -> bovine) and a -idae source label yields -id (Equidae-Horse
    -> equid, Leporidae-Rabbit/Hare -> leporid, Suidae-Pig,Swine -> suid). No deep-research
    run was commissioned: the genus, the wording pattern and the near-miss reasoning
    are already settled by those five siblings and by NCBITaxon, so a billed report
    would add nothing this slice turns on. Worded like the equid sibling for the same
    reason as the canid row: NCBITaxon:9681 ''Felidae'' is wider than the domestic
    cat the source label names. Review https://github.com/CultureBotAI/HabitatMech/issues/2319
    : replaced bare host label Felidae-Cat in exact_synonym with cat-associated environment|feline
    host environment and guarded fallback exclusion in curation/definition_source_label_exclusions.tsv.\tADD"]]'
  snapshot_sha256: ad853d6290dd72b2451d945a0545a5dc5272cc37c2296eaab78c99d2872d4b0c
- evidence_id: EP1
  kind: record_content
  reference: data/habitats/other/animal_associated_environment.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-11-08T15:45:02Z'
  support: supports
  summary: '{"definition": "An environmental system determined by an animal.", "grounding_status":
    "EXACT", "identifier": "ENVO:01001002", "label": "animal-associated environment",
    "mapping_status": "SEEDED", "parent_habitats": ["ENVO:01001000"], "source_attestations":
    [{"notes": "Physicochemical parameter bands from kg-microbe''s environment table.",
    "source": "ENVIRONMENTS_TABLE", "source_id": "host_animal", "source_label": "host_animal"},
    {"assertion_count": 144, "assertion_unit": "TAXON", "source": "MADIN", "source_id":
    "ENVO:01001002", "source_label": "animal-associated environment"}]}'
  snapshot_sha256: a1cf41f43f9bece44dfb3e5d6ab0ca86858df67b88ee25d6ada260cccac69e16
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'felidae_cat|habitatmech:BACDIVE.e6b73de092' reviews/structured/*/review.yaml
    curation/ history/
  accessed_at: '2026-11-08T15:45:02Z'
  support: context_only
  summary: Structured-review traversal located Stage 4 predecessor bundle 20261108T114919Z-felidae_cat-record
    (linked via EPREV and related_reviews) and checked related cohort and ancestor
    reviews for reconciliation.
  search_scope: curation, history, data/raw, and reviews/structured/*/review.yaml
    traversal at commit 6a699ab5f6f775ca0c18be7a12d7af2e2645f31e.
- evidence_id: ESYNS
  kind: record_content
  reference: curation/definition_source_label_exclusions.tsv
  locator: TSV line 2
  accessed_at: '2026-11-08T15:45:02Z'
  support: supports
  summary: '[[2, "habitatmech:BACDIVE.e6b73de092\tFelidae-Cat\tfelid-associated environment\tantigravity\t2026-11-08\tReview
    https://github.com/CultureBotAI/HabitatMech/issues/2319 : The displaced label
    names the determining hosts (Felidae-Cat), not their associated environment. Suppress
    exact-alias fallback; preserve verbatim source provenance, definition, genus and
    native status."]]'
  snapshot_sha256: f53415b9d57f351620a1722c7c83414983899dd9a4559d42e9a094a3e8f501e8
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261108T114919Z-felidae_cat-record/review.yaml
  locator: Every immutable Stage 4 baseline finding
  accessed_at: '2026-11-08T15:45:02Z'
  support: supports
  summary: Exact predecessor keys and findings reconciled; original inspected source
    scope preserved.
  snapshot_sha256: b7eed05671f6ff23b060078283adcea2d7a85c5e49cb0d322020ab3c9dfac989
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_fecal_0d8696a2_to_fin_review_repairs.py
  locator: Complete full-corpus counterfactual regression suite
  accessed_at: '2026-11-08T15:45:02Z'
  support: supports
  summary: 'Exactly seven records differ from the counterfactual baseline across Issues
    #2318 and #2319.'
  snapshot_sha256: db50d90f8a6296e1914051aa62fe928ab03d264f44cc8cbfb1c822f9f9ec650c
- evidence_id: EHIST_G2
  kind: record_content
  reference: history/other/definition_source_label_exclusions/2026-11-08T153510Z-antigravity-231901.yaml
  locator: Complete curation session history event
  accessed_at: '2026-11-08T15:45:02Z'
  support: supports
  summary: 'Authorized curation event for Issue #2319 recorded and validated.'
  snapshot_sha256: e28d82abe703f19ad589f62f7e93ca573a8ebb71bfab13030a83059e974d2126
assessments:
- assessment_id: A1
  area: schema
  topic: Native validity and reproduction after bounded remediation
  outcome: supported
  summary: Individual schema, strict 24-target validation, 872 history records, 14
    inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 93 causal
    overlays, 674 term requests, curation floor, site parity, and counterfactual regression
    tests passed.
  target_ids:
  - habitatmech:BACDIVE.e6b73de092
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - ESIB2
  - EBACDIVE
  - EGROUND
  - EONT
  - EONTEDGE
  - EDEC
  - ETR
  - EP1
  - ESEARCH
  - ESYNS
  - EPREV
  - ETEST
  - EHIST_G2
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: supported
  summary: 'habitatmech:BACDIVE.e6b73de092: felid-associated environment; UNGROUNDED/REVIEWED;
    parents ["ENVO:01001002"]. Replaced the bare host label ''Felidae-Cat'' in exact_synonym
    of curation/term_requests.tsv for habitatmech:BACDIVE.e6b73de092 (''felid-associated
    environment'') with ''cat-associated environment|feline host environment'' and
    added a guarded exclusion row in curation/definition_source_label_exclusions.tsv
    (#2319) so automatic retention of the displaced host label is omitted from synonyms
    (SOURCE_SYNONYM_EXCLUDED) while preserving verbatim BacDive source_attestations,
    NCBITaxon:9681 xref, parent ENVO:01001002, and native REVIEWED/UNGROUNDED status.
    No unresolved predecessor finding remains in this target scope.'
  target_ids:
  - habitatmech:BACDIVE.e6b73de092
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - ESIB2
  - EBACDIVE
  - EGROUND
  - EONT
  - EONTEDGE
  - EDEC
  - ETR
  - EP1
  - ESEARCH
  - ESYNS
  - EPREV
  - ETEST
  - EHIST_G2
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks,
    and pools: [{"source": "BACDIVE", "count": 95, "unit": "STRAIN"}]. Zero counts
    are omitted; unrelated parent counts are not combined.'
  target_ids:
  - habitatmech:BACDIVE.e6b73de092
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - ESIB2
  - EBACDIVE
  - EGROUND
  - EONT
  - EONTEDGE
  - EDEC
  - ETR
  - EP1
  - ESEARCH
  - ESYNS
  - EPREV
  - ETEST
  - EHIST_G2
- assessment_id: A4
  area: representation
  topic: Predecessor finding reconciliation
  outcome: supported
  summary: Every predecessor finding preserves its stable issue_key and exact lineage.
    All predecessor findings in this target scope are resolved.
  target_ids:
  - habitatmech:BACDIVE.e6b73de092
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - ESIB2
  - EBACDIVE
  - EGROUND
  - EONT
  - EONTEDGE
  - EDEC
  - ETR
  - EP1
  - ESEARCH
  - ESYNS
  - EPREV
  - ETEST
  - EHIST_G2
- assessment_id: A5
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: Missing optional parameters/graphs are not evidence deficits. Full source
    decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only
    review does not mutate generated records.
  target_ids:
  - habitatmech:BACDIVE.e6b73de092
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - ESIB2
  - EBACDIVE
  - EGROUND
  - EONT
  - EONTEDGE
  - EDEC
  - ETR
  - EP1
  - ESEARCH
  - ESYNS
  - EPREV
  - ETEST
  - EHIST_G2
findings:
- finding_id: F1
  issue_key: felidae-cat-host-name-exact-synonym
  category: nomenclature
  severity: major
  status: resolved
  certainty: confirmed
  title: Felid-associated environment asserts host-taxon label 'Felidae-Cat' as an
    exact synonym
  description: Replace 'Felidae-Cat' in exact_synonym of curation/term_requests.tsv
    row 46 for habitatmech:BACDIVE.e6b73de092 (e.g. with 'cat-associated environment|feline
    host environment') and add a guarded exclusion row in curation/definition_source_label_exclusions.tsv
    (source_label 'Felidae-Cat', requested_label 'felid-associated environment') so
    automatic retention of the displaced BacDive host label 'Felidae-Cat' as an EXACT_SYNONYM
    is omitted from synonyms (SOURCE_SYNONYM_EXCLUDED) while preserving verbatim source_attestations.
  target_ids:
  - habitatmech:BACDIVE.e6b73de092
  field_paths:
  - synonyms
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - ESIB2
  - EBACDIVE
  - EGROUND
  - EONT
  - EONTEDGE
  - EDEC
  - ETR
  - EP1
  - ESEARCH
  - ESYNS
  - EPREV
  - ETEST
  - EHIST_G2
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or representation claim; deterministic
    validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2319
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261108T114919Z-felidae_cat-record
    finding_id: F1
  disposition_reason: Replaced bare host label 'Felidae-Cat' in exact_synonym of curation/term_requests.tsv
    for habitatmech:BACDIVE.e6b73de092 with 'cat-associated environment|feline host
    environment' and added a guarded exclusion row in curation/definition_source_label_exclusions.tsv
    (#2319) so automatic retention of the displaced host label is omitted from synonyms
    (SOURCE_SYNONYM_EXCLUDED) while preserving verbatim BacDive source_attestations.
actions: []
limitations:
- Only the stated primary evidence and current ontology/taxonomy authorities were
  independently inspected; original specimen-level support for every source-bin member
  is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism
  or characteristic presence. Parent observations are not inherited by children.
- Configured label correspondence skipped 2,088 no-adapter pairs; this is not whole-corpus
  identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in
  this pre-save observation.
- 'iModulonDB is not applicable: the target has no gene, regulator or expression-module
  assertion. No paid research or scientific-status promotion was performed.'
notes:
- Saved against working-tree repairs atop main commit 8e2744f4c33769669e5e9a66a4ae9e27a9642590;
  all earlier saved bundles in reviews/structured/ remain byte-identical.
- Reconciles predecessor bundle 20261108T114919Z-felidae_cat-record with exact issue_key
  and previous_occurrences lineage.
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261108T114919Z-felidae_cat-record
  relationship: Exact predecessor; every finding explicitly reconciled.
```
