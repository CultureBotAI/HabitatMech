# Remediation review: eggs__79d5874d

- Review: 20261031T082507Z-eggs__79d5874d-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-31T08:20:00Z
- Finished UTC: 2026-10-31T08:25:07Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Removed the containing envelope GOLD parent habitatmech:GOLD.d23207689e (insect ootheca) by setting parent_mode=REPLACE in curation/term_requests.tsv and adding a guarded row in curation/gold_parent_exclusions.tsv (#2276). Identity, native status, broader parent BTO:0000369 (egg), and source observations are preserved. No unresolved predecessor finding remains.

## Scope And Provenance

Full current target assessment and explicit disposition of every baseline finding on data/habitats/host_associated/eggs__79d5874d.yaml after bounded Cycle 3 Stage 5 remediation.

Selection: One of eleven repaired targets from the ear_discharge-through-empyema cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 73f5de1ffa3a7ab7e7bfb0e60149aef034c51aa0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.7b8cf8839b | data/habitats/host_associated/eggs__79d5874d.yaml | generated | insect egg |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.7b8cf8839b | Completed 2026-10-26T08:25:36Z. No issues found. |
| validate-strict | passed | True | habitatmech:GOLD.7b8cf8839b | Completed 2026-10-26T08:25:42Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | habitatmech:GOLD.7b8cf8839b | Completed 2026-10-31T08:22:00Z. No issues found; 854 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | habitatmech:GOLD.7b8cf8839b | Completed 2026-10-26T08:25:49Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | habitatmech:GOLD.7b8cf8839b | Completed 2026-10-31T08:22:10Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | habitatmech:GOLD.7b8cf8839b | Completed 2026-10-26T08:26:07Z. validated 53 causal-graph curation file(s) with 53 graph(s). |
| term-requests-check | passed | True | habitatmech:GOLD.7b8cf8839b | Completed 2026-10-31T08:22:15Z. term-request table is current (663 terms). |
| validate-products | passed | True | habitatmech:GOLD.7b8cf8839b | Completed 2026-10-26T08:27:01Z. OK_CANONICAL: 1194, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2063. All id&lt;-&gt;label pairs correspond. |
| pytest counterfactual review repairs | passed | True | habitatmech:GOLD.7b8cf8839b | Completed 2026-10-31T08:23:00Z. 2 passed; exact 11-record counterfactual diff verified. |
| curation-floor | passed | True | habitatmech:GOLD.7b8cf8839b | Completed 2026-10-31T08:23:05Z. Floor satisfied across all 13 metrics. |
| render-check | passed | True | habitatmech:GOLD.7b8cf8839b | Completed 2026-10-31T08:23:30Z. rendered 3209 habitat pages, 743 redirect stubs, 8 categories, 688 term requests; pages/ is in step with the corpus. |

## Scientific And Domain Assessments

### Native validity and reproduction after bounded remediation

schema: supported. Targets: habitatmech:GOLD.7b8cf8839b.

Individual schema, strict 24-target validation, 854 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 53 causal overlays, 663 term requests, curation floor, site parity, and counterfactual regression tests passed.

### Identity, definition, hierarchy and aliases

identity: supported. Targets: habitatmech:GOLD.7b8cf8839b.

habitatmech:GOLD.7b8cf8839b: insect egg; UNGROUNDED/REVIEWED; parents ["BTO:0000369"]. Removed the containing envelope GOLD parent habitatmech:GOLD.d23207689e (insect ootheca) by setting parent_mode=REPLACE in curation/term_requests.tsv and adding a guarded row in curation/gold_parent_exclusions.tsv (#2276). Identity, native status, broader parent BTO:0000369 (egg), and source observations are preserved. No unresolved predecessor finding remains.

### Source counts and retained ranking

quantity: supported. Targets: habitatmech:GOLD.7b8cf8839b.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"source": "GOLD", "count": 19, "unit": "ORGANISM"}]. Zero counts are omitted; unrelated parent counts are not combined.

### Predecessor finding reconciliation

representation: supported. Targets: habitatmech:GOLD.7b8cf8839b.

Every predecessor finding preserves its stable issue_key and exact lineage; all predecessor findings in this target scope are resolved.

### Parameters, mechanisms and native status

completeness: supported. Targets: habitatmech:GOLD.7b8cf8839b.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only review does not mutate generated records.

## Findings

### F1: Insect egg retains containing insect ootheca GOLD parent as a superclass

major / resolved / confirmed; issue key: eggs--79d5874d-context-parent.

Change parent_mode to REPLACE in curation/term_requests.tsv (or add an exclusion row in curation/gold_parent_exclusions.tsv) for habitatmech:GOLD.7b8cf8839b on GOLD path 'Host-associated &gt; Arthropoda: Insects &gt; Ootheca/Egg mass &gt; Eggs' so containing envelope habitatmech:GOLD.d23207689e (insect ootheca) is excluded while preserving BTO:0000369 (egg).

Disposition: Set parent_mode=REPLACE in curation/term_requests.tsv and added a guarded row in curation/gold_parent_exclusions.tsv excluding containing envelope habitatmech:GOLD.d23207689e (insect ootheca) (#2276), preserving BTO:0000369 (egg).

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/eggs__79d5874d.yaml; Entire YAML | supports | {"identifier": "habitatmech:GOLD.7b8cf8839b", "label": "insect egg", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED", "parent_habitats": ["BTO:0000369"], "synonyms": [{"synonym_text": "insect ova", "synonym_type": "EXACT_SYNONYM", "source": "HabitatMech curation"}], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:7140", "source_label": "Eggs", "source_path": "Host-associated &gt; Arthropoda: Insects &gt; Ootheca/Egg mass &gt; Eggs", "assertion_count": 19, "assertion_unit": "ORGANISM", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED."}, {"timestamp": "2026-10-17T00:00:00Z", "curator": "antigravity", "action": "CONFIRM_UNGROUNDED", "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. ITEM curation: GOLD 'Host-associated &gt; Arthropoda: Insects &gt; Ootheca/Egg mass &gt; Eggs' denotes insect eggs within an egg mass or ootheca. Define under BTO:0000369 (egg) and exclude bare 'Eggs' (PMID 25085349; DOI:10.1038/ismej.2014.129). Path: Host-associated &gt; Arthropoda: Insects &gt; Ootheca/Egg mass &gt; Eggs (source concept habitatmech:GOLD.7b8cf8839b)"}, {"timestamp": "2026-10-17T00:00:00Z", "curator": "antigravity", "action": "DEFINED", "changes": "Defined as 'insect egg' under BTO:0000369 'egg'. ITEM curation: GOLD 'Host-associated &gt; Arthropoda: Insects &gt; Ootheca/Egg mass &gt; Eggs' denotes insect eggs within an egg mass or ootheca. Define under BTO:0000369 (egg) with parent_mode REPLACE to exclude containing ootheca parent habitatmech:GOLD.d23207689e and exclude bare 'Eggs' (PMID 25085349; DOI:10.1038/ismej.2014.129). Path: Host-associated &gt; Arthropoda: Insects &gt; Ootheca/Egg mass &gt; Eggs"}, {"timestamp": "2026-10-17T00:00:00Z", "curator": "antigravity", "action": "SOURCE_SYNONYM_EXCLUDED", "changes": "Omitted automatic retention of displaced source label 'Eggs' when defining habitatmech:GOLD.7b8cf8839b as 'insect egg'. Verbatim source attestations are preserved. Displaced GOLD source label 'Eggs' in path 'Host-associated &gt; Arthropoda: Insects &gt; Ootheca/Egg mass &gt; Eggs' is context-dependent, ambiguous, or names a host/disease/process rather than the defined habitat 'insect egg'; suppress automatic exact-synonym retention while preserving verbatim source provenance."}, {"timestamp": "2026-10-31T00:00:00Z", "curator": "antigravity", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.d23207689e for habitatmech:GOLD.7b8cf8839b (Host-associated &gt; Arthropoda: Insects &gt; Ootheca/Egg mass &gt; Eggs). Review https://github.com/CultureBotAI/HabitatMech/issues/2276 : Eccrine sweat gland is an exocrine skin appendage, not the entire human integumentary system; eczematous skin lesion is a cutaneous lesion, not the whole skin organ; middle ear effusion is a fluid accumulation, not the middle ear cavity/organ; egg capsule is a secreted reproductive capsule, not the entire annelid reproductive system; insect egg is a reproductive unit, not an entire ootheca/egg mass; elastic cartilage is a cartilage tissue type, not the entire skeletal cartilage assemblage; pleural empyema exudate is a purulent exudate, not the pleural cavity. Exclude only exact guarded GOLD source-path contributions, preserving independent genera and all source observations. Exact target habitatmech:GOLD.7b8cf8839b. Shared mapping endpoints #1398 remain separate."}]} |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=habitatmech:GOLD.7b8cf8839b, grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["BTO:0000369"]. |
| EGOLD | data/raw/gold_ecosystem_paths.tsv; TSV rows 426 | supports | [{"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Arthropoda: Insects &gt; Ootheca/Egg mass &gt; Eggs", "depth": "4", "ecosystem": "Host-associated", "ecosystem_category": "Arthropoda: Insects", "ecosystem_subtype": "Eggs", "ecosystem_type": "Ootheca/Egg mass", "gold_node_count": "2", "gold_node_ids": "gold.ecosystem:7140&#124;gold.ecosystem:7141", "leaf_label": "Eggs", "organism_count": "19", "specific_ecosystem": "", "study_count": "0", "total_assertions": "19"}, "row": 426}] |
| EONT | data/raw/ontology_terms.tsv; TSV rows 371 | supports | [{"data": {"definition": "The hard-shelled reproductive body produced by a bird and especially by the common domestic chicken; also: its contents used as food.", "deprecated": "", "directly_referenced": "FALSE", "label": "egg", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0000369"}, "row": 371}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 802 | supports | [{"data": {"object": "BTO:0000369", "predicate": "rdfs:subClassOf", "subject": "BTO:0001187"}, "row": 802}] |
| EDEC | curation/decisions.tsv; TSV rows 750 | supports | [{"data": {"category": "", "curator": "antigravity", "date": "2026-10-17", "decision": "CONFIRM_UNGROUNDED", "grounding_status": "", "identifier": "habitatmech:GOLD.7b8cf8839b", "notes": "ITEM curation: GOLD 'Host-associated &gt; Arthropoda: Insects &gt; Ootheca/Egg mass &gt; Eggs' denotes insect eggs within an egg mass or ootheca. Define under BTO:0000369 (egg) and exclude bare 'Eggs' (PMID 25085349; DOI:10.1038/ismej.2014.129). Path: Host-associated &gt; Arthropoda: Insects &gt; Ootheca/Egg mass &gt; Eggs", "object_id": "", "object_label": "", "relation": "", "review_depth": "ITEM"}, "row": 750}] |
| ETR | curation/term_requests.tsv; TSV line 167 | supports | [[167, "habitatmech:GOLD.7b8cf8839b\tinsect egg\tBTO:0000369\tegg\tAn egg produced by an insect and deposited singly or within an ootheca or egg mass, whose chorion surface and interior harbor vertically transmitted or protective microorganisms.\tinsect ova\tantigravity\t2026-10-17\tITEM curation: GOLD 'Host-associated &gt; Arthropoda: Insects &gt; Ootheca/Egg mass &gt; Eggs' denotes insect eggs within an egg mass or ootheca. Define under BTO:0000369 (egg) with parent_mode REPLACE to exclude containing ootheca parent habitatmech:GOLD.d23207689e and exclude bare 'Eggs' (PMID 25085349; DOI:10.1038/ismej.2014.129). Path: Host-associated &gt; Arthropoda: Insects &gt; Ootheca/Egg mass &gt; Eggs\tREPLACE"]] |
| ELE | curation/definition_source_label_exclusions.tsv; TSV rows 58 | supports | [{"data": {"curator": "antigravity", "date": "2026-10-17", "identifier": "habitatmech:GOLD.7b8cf8839b", "notes": "Displaced GOLD source label 'Eggs' in path 'Host-associated &gt; Arthropoda: Insects &gt; Ootheca/Egg mass &gt; Eggs' is context-dependent, ambiguous, or names a host/disease/process rather than the defined habitat 'insect egg'; suppress automatic exact-synonym retention while preserving verbatim source provenance.", "requested_label": "insect egg", "source_label": "Eggs"}, "row": 58}] |
| EP2 | data/habitats/host_associated/ootheca_egg_mass.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": "An egg capsule or frothy proteinaceous egg mass secreted by female insects (such as cockroaches, mantises, or beetles) that encloses and protects a clutch of eggs and transmits maternal symbionts.", "grounding_status": "UNGROUNDED", "identifier": "habitatmech:GOLD.d23207689e", "label": "insect ootheca", "mapping_status": "REVIEWED", "parent_habitats": ["UBERON:3010636", "habitatmech:GOLD.dba2a83b95"], "source_attestations": [{"notes": "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:7139", "source_label": "Ootheca/Egg mass", "source_path": "Host-associated &gt; Arthropoda: Insects &gt; Ootheca/Egg mass"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'eggs__79d5874d&#124;habitatmech:GOLD.7b8cf8839b' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal verified no prior target review bundle exists for this record; curation and history tables were inspected for all matching rows. |
| EPREV | reviews/structured/20261026T083022Z-eggs__79d5874d-record/review.yaml; Every immutable Stage 4 baseline finding | supports | Exact predecessor keys and findings reconciled; original inspected source scope preserved. |
| ETEST | tests/test_ear_discharge_to_empyema_review_repairs.py; Complete full-corpus counterfactual regression suite | supports | Exactly eleven records differ from the counterfactual baseline across Issues #2276 and #2277. |
| EPARENTS | curation/gold_parent_exclusions.tsv; TSV line 7 | supports | [[7, "habitatmech:GOLD.7b8cf8839b\tHost-associated &gt; Arthropoda: Insects &gt; Ootheca/Egg mass &gt; Eggs\thabitatmech:GOLD.d23207689e\tantigravity\t2026-10-31\tReview https://github.com/CultureBotAI/HabitatMech/issues/2276 : Eccrine sweat gland is an exocrine skin appendage, not the entire human integumentary system; eczematous skin lesion is a cutaneous lesion, not the whole skin organ; middle ear effusion is a fluid accumulation, not the middle ear cavity/organ; egg capsule is a secreted reproductive capsule, not the entire annelid reproductive system; insect egg is a reproductive unit, not an entire ootheca/egg mass; elastic cartilage is a cartilage tissue type, not the entire skeletal cartilage assemblage; pleural empyema exudate is a purulent exudate, not the pleural cavity. Exclude only exact guarded GOLD source-path contributions, preserving independent genera and all source observations. Exact target habitatmech:GOLD.7b8cf8839b. Shared mapping endpoints #1398 remain separate."]] |
| EHIST_G1 | history/other/gold_parent_exclusions/2026-10-31T081500Z-antigravity-227601.yaml; Complete curation session history event | supports | Authorized curation event for Issue #2276 recorded and validated. |

## Limits And Additional Notes

- Only the stated primary evidence and current ontology/taxonomy authorities were independently inspected; original specimen-level support for every source-bin member is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism or characteristic presence. Parent observations are not inherited by children.
- Configured label correspondence skipped 2,063 no-adapter pairs; this is not whole-corpus identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in this pre-save observation.
- iModulonDB is not applicable: the target has no gene, regulator or expression-module assertion. No paid research or scientific-status promotion was performed.
- Saved against working-tree repairs atop main commit 73f5de1ffa3a7ab7e7bfb0e60149aef034c51aa0; all earlier saved bundles in reviews/structured/ remain byte-identical.
- Reconciles predecessor bundle 20261026T083022Z-eggs__79d5874d-record with exact issue_key and previous_occurrences lineage.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261031T082507Z-eggs__79d5874d-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: eggs__79d5874d'
started_at: '2026-10-31T08:20:00Z'
finished_at: '2026-10-31T08:25:07Z'
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
summary: Removed the containing envelope GOLD parent habitatmech:GOLD.d23207689e (insect
  ootheca) by setting parent_mode=REPLACE in curation/term_requests.tsv and adding
  a guarded row in curation/gold_parent_exclusions.tsv (#2276). Identity, native status,
  broader parent BTO:0000369 (egg), and source observations are preserved. No unresolved
  predecessor finding remains.
source:
  git_revision: 73f5de1ffa3a7ab7e7bfb0e60149aef034c51aa0
  state: working_tree
  inputs:
  - path: curation/decisions.tsv
    sha256: dea9f54c4f37043299ec911820c1ca9f552a913881bd8ceefef18b6140ed5031
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: f6d6e83963d272c057f795d8a5518e2d117b4a431c75c08b501eed13d170efa1
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 12380d3ee22e773ff067d372204f74165cf5cfa77973ad9565162bbcd383a797
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: c1207270bb0ae2031e42de6cb8220b20f98886f65e40d48793bfd7e9d757d83a
    role: context
  - path: curation/term_requests.tsv
    sha256: 76e2e5b58191022cd20054836efccdbec3f4aee24903c73c68519908af4943d0
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/host_associated/eggs__79d5874d.yaml
    sha256: 5e5dd19ada08ef38272c5e8c093d4fedf0582312568705b6b3ab47ac7cca303b
    role: target
  - path: data/habitats/host_associated/ootheca_egg_mass.yaml
    sha256: 8be7b9ee75956f2c6b51be9df6ddde8f85e60e2587066df12fd99875de069e95
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
  - path: history/other/definition_source_label_exclusions/2026-10-31T081510Z-antigravity-227701.yaml
    sha256: f25a4321c5b99cb3e6486d2be3e42cfc6a9762f7500163d90fd2957a3a6cda57
    role: context
  - path: history/other/gold_parent_exclusions/2026-10-31T081500Z-antigravity-227601.yaml
    sha256: 604c2de8bb4c0383bddd0bd8234b0153757b30db8ec49d35d02db80437caa136
    role: context
  - path: reviews/structured/20261026T083022Z-eggs__79d5874d-record/review.yaml
    sha256: 5c97276d46f422376328ca991d2e97a235ab6a16f5f20f97e8c9413fd4aed7b4
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
    role: context
  - path: src/habitatmech/seed.py
    sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
    role: context
  - path: tests/test_ear_discharge_to_empyema_review_repairs.py
    sha256: e6ee4c56690b2018f4f02e84d445c93c30c79a319c93461ccb5674e1f51d26c8
    role: context
targets:
- target_id: habitatmech:GOLD.7b8cf8839b
  path: data/habitats/host_associated/eggs__79d5874d.yaml
  label: insect egg
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
    finding on data/habitats/host_associated/eggs__79d5874d.yaml after bounded Cycle
    3 Stage 5 remediation.
  selection: One of eleven repaired targets from the ear_discharge-through-empyema
    cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.7b8cf8839b
  exclusions:
  - target: Other habitat records and SSSOM/KGX products
    reason: Direct parents inform hierarchy interpretation but are not additional
      completed reviews; exports are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: .venv/bin/python -m linkml.validator.cli -s src/habitatmech/schema/habitatmech.yaml
    --target-class HabitatRecord data/habitats/host_associated/eggs__79d5874d.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.7b8cf8839b
  summary: Completed 2026-10-26T08:25:36Z. No issues found.
  scope_note: Individual schema; strict command covers the 24 named cohort targets;
    other documented gates have full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/habitats/host_associated/ear_discharge.yaml
    data/habitats/host_associated/ear_discharge__c59c71e2.yaml data/habitats/host_associated/eccrine_sweat_gland.yaml
    data/habitats/host_associated/echinodermata.yaml data/habitats/host_associated/ectosymbionts.yaml
    data/habitats/host_associated/ectosymbionts__7a42a232.yaml data/habitats/host_associated/eczema.yaml
    data/habitats/host_associated/effusion.yaml data/habitats/host_associated/effusion__ef80da5d.yaml
    data/habitats/host_associated/egg.yaml data/habitats/host_associated/egg_capsule.yaml
    data/habitats/host_associated/eggs.yaml data/habitats/host_associated/eggs__79d5874d.yaml
    data/habitats/host_associated/elastic__846c7f5c.yaml data/habitats/host_associated/elastic_cartilage_tissue.yaml
    data/habitats/host_associated/electric_organ.yaml data/habitats/host_associated/elementary_body.yaml
    data/habitats/host_associated/embryo.yaml data/habitats/host_associated/embryo__3df16fcc.yaml
    data/habitats/host_associated/embryo__74685e7d.yaml data/habitats/host_associated/embryo__e76df6f3.yaml
    data/habitats/host_associated/embryonic_cell_line.yaml data/habitats/host_associated/embryonic_stem_cell.yaml
    data/habitats/host_associated/empyema.yaml --out /tmp/c3s4_24_strict.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.7b8cf8839b
  summary: 'Completed 2026-10-26T08:25:42Z. Validated 24 files; files with ERROR:
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
  - habitatmech:GOLD.7b8cf8839b
  summary: Completed 2026-10-31T08:22:00Z. No issues found; 854 history record(s)
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
  - habitatmech:GOLD.7b8cf8839b
  summary: 'Completed 2026-10-26T08:25:49Z. provenance current: 14 committed inventories,
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
  - habitatmech:GOLD.7b8cf8839b
  summary: 'Completed 2026-10-31T08:22:10Z. expected 3209 records, found 3209 on disk;
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
  - habitatmech:GOLD.7b8cf8839b
  summary: Completed 2026-10-26T08:26:07Z. validated 53 causal-graph curation file(s)
    with 53 graph(s).
  scope_note: Full-corpus causal-graph overlay validation.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: .venv/bin/python scripts/build_term_requests.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.7b8cf8839b
  summary: Completed 2026-10-31T08:22:15Z. term-request table is current (663 terms).
  scope_note: Full-corpus term-request table currency check.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.7b8cf8839b
  summary: 'Completed 2026-10-26T08:27:01Z. OK_CANONICAL: 1194, OK_SYNONYM: 1, OK_EXCEPTION:
    5, SKIPPED_NO_ADAPTER: 2063. All id<->label pairs correspond.'
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
- check_id: C9
  name: pytest counterfactual review repairs
  status: passed
  required: true
  command: .venv/bin/python -m pytest tests/test_ear_discharge_to_empyema_review_repairs.py
    -q --no-cov
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.7b8cf8839b
  summary: Completed 2026-10-31T08:23:00Z. 2 passed; exact 11-record counterfactual
    diff verified.
  scope_note: 'Full-corpus counterfactual regression test for Issues #2276 and #2277.'
- check_id: C10
  name: curation-floor
  status: passed
  required: true
  command: .venv/bin/python scripts/check_curation_floor.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.7b8cf8839b
  summary: Completed 2026-10-31T08:23:05Z. Floor satisfied across all 13 metrics.
  scope_note: Full-corpus curation floor ratchets.
- check_id: C11
  name: render-check
  status: passed
  required: true
  command: .venv/bin/python scripts/render_pages.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.7b8cf8839b
  summary: Completed 2026-10-31T08:23:30Z. rendered 3209 habitat pages, 743 redirect
    stubs, 8 categories, 688 term requests; pages/ is in step with the corpus.
  scope_note: Full-corpus static site parity check.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/eggs__79d5874d.yaml
  locator: Entire YAML
  accessed_at: '2026-10-31T08:25:07Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.7b8cf8839b", "label": "insect egg", "grounding_status":
    "UNGROUNDED", "mapping_status": "REVIEWED", "parent_habitats": ["BTO:0000369"],
    "synonyms": [{"synonym_text": "insect ova", "synonym_type": "EXACT_SYNONYM", "source":
    "HabitatMech curation"}], "source_attestations": [{"source": "GOLD", "source_id":
    "gold.ecosystem:7140", "source_label": "Eggs", "source_path": "Host-associated
    > Arthropoda: Insects > Ootheca/Egg mass > Eggs", "assertion_count": 19, "assertion_unit":
    "ORGANISM", "notes": "2 GOLD ecosystem node ids share this path; first shown.
    See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp":
    "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES",
    "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED."},
    {"timestamp": "2026-10-17T00:00:00Z", "curator": "antigravity", "action": "CONFIRM_UNGROUNDED",
    "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. ITEM curation:
    GOLD ''Host-associated > Arthropoda: Insects > Ootheca/Egg mass > Eggs'' denotes
    insect eggs within an egg mass or ootheca. Define under BTO:0000369 (egg) and
    exclude bare ''Eggs'' (PMID 25085349; DOI:10.1038/ismej.2014.129). Path: Host-associated
    > Arthropoda: Insects > Ootheca/Egg mass > Eggs (source concept habitatmech:GOLD.7b8cf8839b)"},
    {"timestamp": "2026-10-17T00:00:00Z", "curator": "antigravity", "action": "DEFINED",
    "changes": "Defined as ''insect egg'' under BTO:0000369 ''egg''. ITEM curation:
    GOLD ''Host-associated > Arthropoda: Insects > Ootheca/Egg mass > Eggs'' denotes
    insect eggs within an egg mass or ootheca. Define under BTO:0000369 (egg) with
    parent_mode REPLACE to exclude containing ootheca parent habitatmech:GOLD.d23207689e
    and exclude bare ''Eggs'' (PMID 25085349; DOI:10.1038/ismej.2014.129). Path: Host-associated
    > Arthropoda: Insects > Ootheca/Egg mass > Eggs"}, {"timestamp": "2026-10-17T00:00:00Z",
    "curator": "antigravity", "action": "SOURCE_SYNONYM_EXCLUDED", "changes": "Omitted
    automatic retention of displaced source label ''Eggs'' when defining habitatmech:GOLD.7b8cf8839b
    as ''insect egg''. Verbatim source attestations are preserved. Displaced GOLD
    source label ''Eggs'' in path ''Host-associated > Arthropoda: Insects > Ootheca/Egg
    mass > Eggs'' is context-dependent, ambiguous, or names a host/disease/process
    rather than the defined habitat ''insect egg''; suppress automatic exact-synonym
    retention while preserving verbatim source provenance."}, {"timestamp": "2026-10-31T00:00:00Z",
    "curator": "antigravity", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded
    GOLD source-path parent contribution habitatmech:GOLD.d23207689e for habitatmech:GOLD.7b8cf8839b
    (Host-associated > Arthropoda: Insects > Ootheca/Egg mass > Eggs). Review https://github.com/CultureBotAI/HabitatMech/issues/2276
    : Eccrine sweat gland is an exocrine skin appendage, not the entire human integumentary
    system; eczematous skin lesion is a cutaneous lesion, not the whole skin organ;
    middle ear effusion is a fluid accumulation, not the middle ear cavity/organ;
    egg capsule is a secreted reproductive capsule, not the entire annelid reproductive
    system; insect egg is a reproductive unit, not an entire ootheca/egg mass; elastic
    cartilage is a cartilage tissue type, not the entire skeletal cartilage assemblage;
    pleural empyema exudate is a purulent exudate, not the pleural cavity. Exclude
    only exact guarded GOLD source-path contributions, preserving independent genera
    and all source observations. Exact target habitatmech:GOLD.7b8cf8839b. Shared
    mapping endpoints #1398 remain separate."}]}'
  snapshot_sha256: 5e5dd19ada08ef38272c5e8c093d4fedf0582312568705b6b3ab47ac7cca303b
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-10-31T08:25:07Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon terms cannot substitute
    for associated environments; parent_habitats must be strictly broader across all
    contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-10-31T08:25:07Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-10-31T08:25:07Z'
  support: supports
  summary: Seed generator produces identifier=habitatmech:GOLD.7b8cf8839b, grounding_status=UNGROUNDED,
    mapping_status=REVIEWED, parent_habitats=["BTO:0000369"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EGOLD
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV rows 426
  accessed_at: '2026-10-31T08:25:07Z'
  support: supports
  summary: '[{"data": {"biosample_count": "0", "canonical_path": "Host-associated
    > Arthropoda: Insects > Ootheca/Egg mass > Eggs", "depth": "4", "ecosystem": "Host-associated",
    "ecosystem_category": "Arthropoda: Insects", "ecosystem_subtype": "Eggs", "ecosystem_type":
    "Ootheca/Egg mass", "gold_node_count": "2", "gold_node_ids": "gold.ecosystem:7140|gold.ecosystem:7141",
    "leaf_label": "Eggs", "organism_count": "19", "specific_ecosystem": "", "study_count":
    "0", "total_assertions": "19"}, "row": 426}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 371
  accessed_at: '2026-10-31T08:25:07Z'
  support: supports
  summary: '[{"data": {"definition": "The hard-shelled reproductive body produced
    by a bird and especially by the common domestic chicken; also: its contents used
    as food.", "deprecated": "", "directly_referenced": "FALSE", "label": "egg", "label_only":
    "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0000369"}, "row":
    371}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 802
  accessed_at: '2026-10-31T08:25:07Z'
  support: supports
  summary: '[{"data": {"object": "BTO:0000369", "predicate": "rdfs:subClassOf", "subject":
    "BTO:0001187"}, "row": 802}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EDEC
  kind: database
  reference: curation/decisions.tsv
  locator: TSV rows 750
  accessed_at: '2026-10-31T08:25:07Z'
  support: supports
  summary: '[{"data": {"category": "", "curator": "antigravity", "date": "2026-10-17",
    "decision": "CONFIRM_UNGROUNDED", "grounding_status": "", "identifier": "habitatmech:GOLD.7b8cf8839b",
    "notes": "ITEM curation: GOLD ''Host-associated > Arthropoda: Insects > Ootheca/Egg
    mass > Eggs'' denotes insect eggs within an egg mass or ootheca. Define under
    BTO:0000369 (egg) and exclude bare ''Eggs'' (PMID 25085349; DOI:10.1038/ismej.2014.129).
    Path: Host-associated > Arthropoda: Insects > Ootheca/Egg mass > Eggs", "object_id":
    "", "object_label": "", "relation": "", "review_depth": "ITEM"}, "row": 750}]'
  snapshot_sha256: dea9f54c4f37043299ec911820c1ca9f552a913881bd8ceefef18b6140ed5031
- evidence_id: ETR
  kind: database
  reference: curation/term_requests.tsv
  locator: TSV line 167
  accessed_at: '2026-10-31T08:25:07Z'
  support: supports
  summary: '[[167, "habitatmech:GOLD.7b8cf8839b\tinsect egg\tBTO:0000369\tegg\tAn
    egg produced by an insect and deposited singly or within an ootheca or egg mass,
    whose chorion surface and interior harbor vertically transmitted or protective
    microorganisms.\tinsect ova\tantigravity\t2026-10-17\tITEM curation: GOLD ''Host-associated
    > Arthropoda: Insects > Ootheca/Egg mass > Eggs'' denotes insect eggs within an
    egg mass or ootheca. Define under BTO:0000369 (egg) with parent_mode REPLACE to
    exclude containing ootheca parent habitatmech:GOLD.d23207689e and exclude bare
    ''Eggs'' (PMID 25085349; DOI:10.1038/ismej.2014.129). Path: Host-associated >
    Arthropoda: Insects > Ootheca/Egg mass > Eggs\tREPLACE"]]'
  snapshot_sha256: 76e2e5b58191022cd20054836efccdbec3f4aee24903c73c68519908af4943d0
- evidence_id: ELE
  kind: database
  reference: curation/definition_source_label_exclusions.tsv
  locator: TSV rows 58
  accessed_at: '2026-10-31T08:25:07Z'
  support: supports
  summary: '[{"data": {"curator": "antigravity", "date": "2026-10-17", "identifier":
    "habitatmech:GOLD.7b8cf8839b", "notes": "Displaced GOLD source label ''Eggs''
    in path ''Host-associated > Arthropoda: Insects > Ootheca/Egg mass > Eggs'' is
    context-dependent, ambiguous, or names a host/disease/process rather than the
    defined habitat ''insect egg''; suppress automatic exact-synonym retention while
    preserving verbatim source provenance.", "requested_label": "insect egg", "source_label":
    "Eggs"}, "row": 58}]'
  snapshot_sha256: f6d6e83963d272c057f795d8a5518e2d117b4a431c75c08b501eed13d170efa1
- evidence_id: EP2
  kind: record_content
  reference: data/habitats/host_associated/ootheca_egg_mass.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-10-31T08:25:07Z'
  support: supports
  summary: '{"definition": "An egg capsule or frothy proteinaceous egg mass secreted
    by female insects (such as cockroaches, mantises, or beetles) that encloses and
    protects a clutch of eggs and transmits maternal symbionts.", "grounding_status":
    "UNGROUNDED", "identifier": "habitatmech:GOLD.d23207689e", "label": "insect ootheca",
    "mapping_status": "REVIEWED", "parent_habitats": ["UBERON:3010636", "habitatmech:GOLD.dba2a83b95"],
    "source_attestations": [{"notes": "3 GOLD ecosystem node ids share this path;
    first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id":
    "gold.ecosystem:7139", "source_label": "Ootheca/Egg mass", "source_path": "Host-associated
    > Arthropoda: Insects > Ootheca/Egg mass"}]}'
  snapshot_sha256: 8be7b9ee75956f2c6b51be9df6ddde8f85e60e2587066df12fd99875de069e95
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'eggs__79d5874d|habitatmech:GOLD.7b8cf8839b' reviews/structured/*/review.yaml
    curation/ history/
  accessed_at: '2026-10-31T08:25:07Z'
  support: context_only
  summary: Structured-review traversal verified no prior target review bundle exists
    for this record; curation and history tables were inspected for all matching rows.
  search_scope: curation, history, data/raw, and reviews/structured/*/review.yaml
    traversal at commit 1a40d0958114e6e3facd148ccec6197fa4dd679c.
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261026T083022Z-eggs__79d5874d-record/review.yaml
  locator: Every immutable Stage 4 baseline finding
  accessed_at: '2026-10-31T08:25:07Z'
  support: supports
  summary: Exact predecessor keys and findings reconciled; original inspected source
    scope preserved.
  snapshot_sha256: 5c97276d46f422376328ca991d2e97a235ab6a16f5f20f97e8c9413fd4aed7b4
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_ear_discharge_to_empyema_review_repairs.py
  locator: Complete full-corpus counterfactual regression suite
  accessed_at: '2026-10-31T08:25:07Z'
  support: supports
  summary: 'Exactly eleven records differ from the counterfactual baseline across
    Issues #2276 and #2277.'
  snapshot_sha256: e6ee4c56690b2018f4f02e84d445c93c30c79a319c93461ccb5674e1f51d26c8
- evidence_id: EPARENTS
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: TSV line 7
  accessed_at: '2026-10-31T08:25:07Z'
  support: supports
  summary: '[[7, "habitatmech:GOLD.7b8cf8839b\tHost-associated > Arthropoda: Insects
    > Ootheca/Egg mass > Eggs\thabitatmech:GOLD.d23207689e\tantigravity\t2026-10-31\tReview
    https://github.com/CultureBotAI/HabitatMech/issues/2276 : Eccrine sweat gland
    is an exocrine skin appendage, not the entire human integumentary system; eczematous
    skin lesion is a cutaneous lesion, not the whole skin organ; middle ear effusion
    is a fluid accumulation, not the middle ear cavity/organ; egg capsule is a secreted
    reproductive capsule, not the entire annelid reproductive system; insect egg is
    a reproductive unit, not an entire ootheca/egg mass; elastic cartilage is a cartilage
    tissue type, not the entire skeletal cartilage assemblage; pleural empyema exudate
    is a purulent exudate, not the pleural cavity. Exclude only exact guarded GOLD
    source-path contributions, preserving independent genera and all source observations.
    Exact target habitatmech:GOLD.7b8cf8839b. Shared mapping endpoints #1398 remain
    separate."]]'
  snapshot_sha256: 12380d3ee22e773ff067d372204f74165cf5cfa77973ad9565162bbcd383a797
- evidence_id: EHIST_G1
  kind: record_content
  reference: history/other/gold_parent_exclusions/2026-10-31T081500Z-antigravity-227601.yaml
  locator: Complete curation session history event
  accessed_at: '2026-10-31T08:25:07Z'
  support: supports
  summary: 'Authorized curation event for Issue #2276 recorded and validated.'
  snapshot_sha256: 604c2de8bb4c0383bddd0bd8234b0153757b30db8ec49d35d02db80437caa136
assessments:
- assessment_id: A1
  area: schema
  topic: Native validity and reproduction after bounded remediation
  outcome: supported
  summary: Individual schema, strict 24-target validation, 854 history records, 14
    inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 53 causal
    overlays, 663 term requests, curation floor, site parity, and counterfactual regression
    tests passed.
  target_ids:
  - habitatmech:GOLD.7b8cf8839b
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
  - EP2
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST_G1
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: supported
  summary: 'habitatmech:GOLD.7b8cf8839b: insect egg; UNGROUNDED/REVIEWED; parents
    ["BTO:0000369"]. Removed the containing envelope GOLD parent habitatmech:GOLD.d23207689e
    (insect ootheca) by setting parent_mode=REPLACE in curation/term_requests.tsv
    and adding a guarded row in curation/gold_parent_exclusions.tsv (#2276). Identity,
    native status, broader parent BTO:0000369 (egg), and source observations are preserved.
    No unresolved predecessor finding remains.'
  target_ids:
  - habitatmech:GOLD.7b8cf8839b
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
    and pools: [{"source": "GOLD", "count": 19, "unit": "ORGANISM"}]. Zero counts
    are omitted; unrelated parent counts are not combined.'
  target_ids:
  - habitatmech:GOLD.7b8cf8839b
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
  - EP2
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST_G1
- assessment_id: A4
  area: representation
  topic: Predecessor finding reconciliation
  outcome: supported
  summary: Every predecessor finding preserves its stable issue_key and exact lineage;
    all predecessor findings in this target scope are resolved.
  target_ids:
  - habitatmech:GOLD.7b8cf8839b
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
    decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only
    review does not mutate generated records.
  target_ids:
  - habitatmech:GOLD.7b8cf8839b
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
  - EP2
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST_G1
findings:
- finding_id: F1
  issue_key: eggs--79d5874d-context-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Insect egg retains containing insect ootheca GOLD parent as a superclass
  description: 'Change parent_mode to REPLACE in curation/term_requests.tsv (or add
    an exclusion row in curation/gold_parent_exclusions.tsv) for habitatmech:GOLD.7b8cf8839b
    on GOLD path ''Host-associated > Arthropoda: Insects > Ootheca/Egg mass > Eggs''
    so containing envelope habitatmech:GOLD.d23207689e (insect ootheca) is excluded
    while preserving BTO:0000369 (egg).'
  target_ids:
  - habitatmech:GOLD.7b8cf8839b
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
  - EDEC
  - ETR
  - ELE
  - EP2
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST_G1
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or representation claim; deterministic
    validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2276
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261026T083022Z-eggs__79d5874d-record
    finding_id: F1
  disposition_reason: Set parent_mode=REPLACE in curation/term_requests.tsv and added
    a guarded row in curation/gold_parent_exclusions.tsv excluding containing envelope
    habitatmech:GOLD.d23207689e (insect ootheca) (#2276), preserving BTO:0000369 (egg).
actions: []
limitations:
- Only the stated primary evidence and current ontology/taxonomy authorities were
  independently inspected; original specimen-level support for every source-bin member
  is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism
  or characteristic presence. Parent observations are not inherited by children.
- Configured label correspondence skipped 2,063 no-adapter pairs; this is not whole-corpus
  identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in
  this pre-save observation.
- 'iModulonDB is not applicable: the target has no gene, regulator or expression-module
  assertion. No paid research or scientific-status promotion was performed.'
notes:
- Saved against working-tree repairs atop main commit 73f5de1ffa3a7ab7e7bfb0e60149aef034c51aa0;
  all earlier saved bundles in reviews/structured/ remain byte-identical.
- Reconciles predecessor bundle 20261026T083022Z-eggs__79d5874d-record with exact
  issue_key and previous_occurrences lineage.
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261026T083022Z-eggs__79d5874d-record
  relationship: Exact predecessor; every finding explicitly reconciled.
```
