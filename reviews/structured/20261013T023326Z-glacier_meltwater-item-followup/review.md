# Glacier meltwater ITEM grounding and preserved source scope

- Review: 20261013T023326Z-glacier_meltwater-item-followup
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-13T02:09:30.598027Z
- Finished UTC: 2026-10-13T02:33:26.238637Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

This review assesses the captured scientific files at pinned commit 01ae8d08f5a8d337371399078b6d0c18a40df645. Every captured blob was also verified byte-identical on current head 348085582b0090404a73c122376b8045e6050c41 after map/site regeneration. Reassessed the entire glacier-specific source after integrating PR1218 with main. The ITEM GROUND_AS_PARENT decision retains habitatmech:GOLD.f3dc60ff11 and adds ENVO:01000722 as a strictly broader meltwater genus. The current official ENVO definition spans snow and several ice sources, while the GOLD label specifies glacier origin. Frozen medium annotation covers six samples from one study Gs0118069, not six independent studies; broad freshwater-lake biome and local glacial-lake slots remain context. The direct GOLD occurrence inventory has zero counts, so the attestation correctly omits positive counts rather than importing the separate bulk/API counts. The separate Glacier &gt; Meltwater record ENVO:01000722 retains node7297 and its one ORGANISM assertion. The existing ENVO:01001511 frozen-precursor exclusion and all444 exclusion rows remain byte-identical to main. Native NARROW/REVIEWED is derived from the new ITEM decision, not this review. The generated active decision history is regenerated; old committed session histories and immutable reviews are not rewritten. The shared attestation comparison-endpoint contract remains unresolved under #1398; this review does not certify SSSOM/KGX conformance.

## Scope And Provenance

Entire exact glacier-meltwater record and its sole source concept; bounded curation follow-up.

Selection: Explicit remaining scientific scope in PR1218; no new distinct-record coverage.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 01ae8d08f5a8d337371399078b6d0c18a40df645.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.f3dc60ff11 | data/habitats/aquatic/glacier_meltwater.yaml | generated | Glacier meltwater |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native post-correction gate | passed | True | habitatmech:GOLD.f3dc60ff11 | Actual success from 2026-10-13T02:11:15.117890+00:00 to 2026-10-13T02:12:11.751759+00:00. Scientific scope remains one target. |
| Native post-correction gate | passed | True | habitatmech:GOLD.f3dc60ff11 | Actual success from 2026-10-13T02:07:54.478180+00:00 to 2026-10-13T02:07:59.049500+00:00. Scientific scope remains one target. |
| Native post-correction gate | passed | True | habitatmech:GOLD.f3dc60ff11 | Actual success from 2026-10-13T02:07:59.050451+00:00 to 2026-10-13T02:08:10.568140+00:00. Scientific scope remains one target. |
| Native post-correction gate | passed | True | habitatmech:GOLD.f3dc60ff11 | Actual success from 2026-10-13T02:08:10.569120+00:00 to 2026-10-13T02:09:49.514758+00:00. Scientific scope remains one target. |
| Native post-correction gate | passed | True | habitatmech:GOLD.f3dc60ff11 | Actual success from 2026-10-13T02:09:49.516177+00:00 to 2026-10-13T02:10:00.046475+00:00. Scientific scope remains one target. |
| Native post-correction gate | passed | True | habitatmech:GOLD.f3dc60ff11 | Actual success from 2026-10-13T02:10:00.047246+00:00 to 2026-10-13T02:10:00.898990+00:00. Scientific scope remains one target. |
| Native post-correction gate | passed | True | habitatmech:GOLD.f3dc60ff11 | Actual success from 2026-10-13T02:10:00.899837+00:00 to 2026-10-13T02:10:22.775641+00:00. Scientific scope remains one target. |
| Native post-correction gate | passed | True | habitatmech:GOLD.f3dc60ff11 | Actual success from 2026-10-13T02:10:22.776432+00:00 to 2026-10-13T02:10:29.162380+00:00. Scientific scope remains one target. |
| Native post-correction gate | passed | True | habitatmech:GOLD.f3dc60ff11 | Actual success from 2026-10-13T02:10:29.163275+00:00 to 2026-10-13T02:10:58.864928+00:00. Scientific scope remains one target. |
| Native post-correction gate | passed | True | habitatmech:GOLD.f3dc60ff11 | Actual success from 2026-10-13T02:10:58.866342+00:00 to 2026-10-13T02:10:59.300405+00:00. Scientific scope remains one target. |
| Native post-correction gate | passed | True | habitatmech:GOLD.f3dc60ff11 | Actual success from 2026-10-13T02:10:59.301236+00:00 to 2026-10-13T02:10:59.793415+00:00. Scientific scope remains one target. |
| Corrected-input hosted authoritative QC | passed | True | habitatmech:GOLD.f3dc60ff11 | Exact-head authoritative hosted QC passed: 1060 tests, 3 skipped, and all native quality gates. Captured scientific inputs were hash-rechecked unchanged; new review files require final-head CI. |

## Scientific And Domain Assessments

### Glacier-specific identity, broader meltwater genus and frozen precursor

grounding: supported. Targets: habitatmech:GOLD.f3dc60ff11.

This review assesses the captured scientific files at pinned commit 01ae8d08f5a8d337371399078b6d0c18a40df645. Every captured blob was also verified byte-identical on current head 348085582b0090404a73c122376b8045e6050c41 after map/site regeneration. Reassessed the entire glacier-specific source after integrating PR1218 with main. The ITEM GROUND_AS_PARENT decision retains habitatmech:GOLD.f3dc60ff11 and adds ENVO:01000722 as a strictly broader meltwater genus. The current official ENVO definition spans snow and several ice sources, while the GOLD label specifies glacier origin. Frozen medium annotation covers six samples from one study Gs0118069, not six independent studies; broad freshwater-lake biome and local glacial-lake slots remain context. The direct GOLD occurrence inventory has zero counts, so the attestation correctly omits positive counts rather than importing the separate bulk/API counts. The separate Glacier &gt; Meltwater record ENVO:01000722 retains node7297 and its one ORGANISM assertion. The existing ENVO:01001511 frozen-precursor exclusion and all444 exclusion rows remain byte-identical to main. Native NARROW/REVIEWED is derived from the new ITEM decision, not this review. The generated active decision history is regenerated; old committed session histories and immutable reviews are not rewritten. The shared attestation comparison-endpoint contract remains unresolved under #1398; this review does not certify SSSOM/KGX conformance.

### Frozen counters, triad roles and independent study denominator

provenance: supported. Targets: habitatmech:GOLD.f3dc60ff11.

The sole source node7784 and exact five-level path remain. Six medium-annotated samples arise from one study; zero direct counts, separate bulk/API counts and omitted display counts are not interchangeable. No taxa, parameters, causal graphs or universal ecological measurements are invented.

### Attestation comparison-object contract

grounding: concern. Targets: habitatmech:GOLD.f3dc60ff11.

The schema defines mapping_predicate from source_id to this record identifier, while the actual narrow route retains the source mint and compares it to a broader ontology parent. This is a representation-contract mismatch, not a claim of formal SKOS inconsistency. SSSOM/KGX readiness is not established.

## Findings

### F1: A source setting or material is emitted as a strict superclass

major / resolved / confirmed; issue key: habitatmech-gold.f3dc60ff11-context-parent.

The former GOLD freshwater-ice superclass remains excluded; the separate new meltwater genus does not reintroduce the precursor edge.

Disposition: Reconfirmed the earlier resolved context-parent disposition: the maintained exclusion is unchanged and a whole-corpus regression retains independent parents. This review assesses the captured scientific files at pinned commit 01ae8d08f5a8d337371399078b6d0c18a40df645. Every captured blob was also verified byte-identical on current head 348085582b0090404a73c122376b8045e6050c41 after map/site regeneration. Reassessed the entire glacier-specific source after integrating PR1218 with main. The ITEM GROUND_AS_PARENT decision retains habitatmech:GOLD.f3dc60ff11 and adds ENVO:01000722 as a strictly broader meltwater genus. The current official ENVO definition spans snow and several ice sources, while the GOLD label specifies glacier origin. Frozen medium annotation covers six samples from one study Gs0118069, not six independent studies; broad freshwater-lake biome and local glacial-lake slots remain context. The direct GOLD occurrence inventory has zero counts, so the attestation correctly omits positive counts rather than importing the separate bulk/API counts. The separate Glacier &gt; Meltwater record ENVO:01000722 retains node7297 and its one ORGANISM assertion. The existing ENVO:01001511 frozen-precursor exclusion and all444 exclusion rows remain byte-identical to main. Native NARROW/REVIEWED is derived from the new ITEM decision, not this review. The generated active decision history is regenerated; old committed session histories and immutable reviews are not rewritten. The shared attestation comparison-endpoint contract remains unresolved under #1398; this review does not certify SSSOM/KGX conformance.

### F2: NARROW comparison endpoint is ambiguous under the attestation contract

major / open / confirmed; issue key: habitatmech-gold.f3dc60ff11-mapping-endpoint-contract.

The schema defines mapping_predicate from source_id to this record identifier, while the actual narrow route retains the source mint and compares it to a broader ontology parent. This is a representation-contract mismatch, not a claim of formal SKOS inconsistency. SSSOM/KGX readiness is not established.

## Recommended Actions And Acceptance Checks

### A1

Resolve source-to-record versus source-to-ontology-parent comparison semantics with seeder and downstream export regressions; a predicate-only replacement is insufficient.

- Reassess the exact source and preserve independent valid genera, source IDs, counts/units and omitted counts.
- Change maintained owners with append-only curation history; do not rewrite generated records or saved reviews.
- Add focused regressions; inspect guarded canaries and pass strict schema, labels, history, provenance, reproduction and QC.
- Use a linked successor review for any disposition; this assessment records proposed work, not an executed repair.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| PRIOR | reviews/structured/20261012T025310Z-glacier_meltwater-followup/review.yaml | supports | Exact predecessor and original review read in full; the precursor exclusion was resolved previously, while optional genus curation was explicitly outside that earlier scope. |
| CURRENT | data/habitats/aquatic/glacier_meltwater.yaml; curation/decisions.tsv:1349; data/raw/gold_ecosystem_paths.tsv:1472; data/raw/gold_path_biosamples.tsv:728; data/raw/gold_path_triads.tsv:305-307; data/raw/gold_studies.tsv:1057 | supports | This review assesses the captured scientific files at pinned commit 01ae8d08f5a8d337371399078b6d0c18a40df645. Every captured blob was also verified byte-identical on current head 348085582b0090404a73c122376b8045e6050c41 after map/site regeneration. Reassessed the entire glacier-specific source after integrating PR1218 with main. The ITEM GROUND_AS_PARENT decision retains habitatmech:GOLD.f3dc60ff11 and adds ENVO:01000722 as a strictly broader meltwater genus. The current official ENVO definition spans snow and several ice sources, while the GOLD label specifies glacier origin. Frozen medium annotation covers six samples from one study Gs0118069, not six independent studies; broad freshwater-lake biome and local glacial-lake slots remain context. The direct GOLD occurrence inventory has zero counts, so the attestation correctly omits positive counts rather than importing the separate bulk/API counts. The separate Glacier &gt; Meltwater record ENVO:01000722 retains node7297 and its one ORGANISM assertion. The existing ENVO:01001511 frozen-precursor exclusion and all444 exclusion rows remain byte-identical to main. Native NARROW/REVIEWED is derived from the new ITEM decision, not this review. The generated active decision history is regenerated; old committed session histories and immutable reviews are not rewritten. The shared attestation comparison-endpoint contract remains unresolved under #1398; this review does not certify SSSOM/KGX conformance. |
| ENVO | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000722 | supports | Current official OLS JSON inspected: active ENVO:01000722, canonical label meltwater, definition explicitly includes water from glacial ice alongside snow and other ice sources. Matches frozen ontology_terms row8217 and liquid-water subclass edge row6492; supports a broader genus, not exact identity. |
| CONTRACT | src/habitatmech/schema/habitatmech.yaml:317; src/habitatmech/seed.py:595; https://github.com/CultureBotAI/HabitatMech/issues/1398 | supports | Schema says mapping_predicate relates the source to this record identifier and is absent when the record is the source concept. The curated parent route instead preserves the mint and emits skos:narrowMatch for its comparison with the broader ontology parent. The comparison object is not explicit in the attestation. This is a representation ambiguity, not a claim of formal SKOS inconsistency. |
| CHECKS | tests/test_glacier_meltwater_grounding.py; tests/test_fourth_aquatic_review_fixes.py; https://github.com/CultureBotAI/HabitatMech/actions/runs/38335796983 | supports | Sixty-nine focused exclusion/curation-floor tests passed; a later 33-test genus/earlier-cohort suite passed after correcting the reproduced stale expectation tracked in #2034. Native post-correction gates and corrected-input hosted QC passed. Generated map uses the unchanged pinned runtime, verified changed-record inference and repeat reuse, all3208 points, zero omissions. New review integrity and final-head checks remain separate publication gates. |

## Limits And Additional Notes

- Same-agent adversarial review, not independent approval.
- The original occurrence membership limitations in the predecessor remain. Ignored-inclusive searches covered reviews/structured, curation, history, research, conf, reports/yaml_record_review and data/raw for the exact source ID, slug and label; no new original membership evidence was established.
- The live GOLD study page returned a request error; no claim of fresh authenticated GOLD API membership verification is made. Frozen inventories support the bounded denominator.
- iModulonDB is not applicable: no gene, regulator, strain-specific expression module or transcriptomic claim occurs in this record.
- Ontology-label validation retains configured no-adapter skips and accepted exceptions. SSSOM/KGX conformance remains uncertified under #1398.
- This review resolves no unrelated #1220 or corpus-wide scientific finding. Optional definitions and organism/parameter examples are not inferred from a habitat name.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T023326Z-glacier_meltwater-item-followup
kind: record
repository: CultureBotAI/HabitatMech
title: Glacier meltwater ITEM grounding and preserved source scope
started_at: '2026-10-13T02:09:30.598027Z'
finished_at: '2026-10-13T02:33:26.238637Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Same agent authored curation and adversarial reassessment; not
    independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'This review assesses the captured scientific files at pinned commit 01ae8d08f5a8d337371399078b6d0c18a40df645.
  Every captured blob was also verified byte-identical on current head 348085582b0090404a73c122376b8045e6050c41
  after map/site regeneration. Reassessed the entire glacier-specific source after
  integrating PR1218 with main. The ITEM GROUND_AS_PARENT decision retains habitatmech:GOLD.f3dc60ff11
  and adds ENVO:01000722 as a strictly broader meltwater genus. The current official
  ENVO definition spans snow and several ice sources, while the GOLD label specifies
  glacier origin. Frozen medium annotation covers six samples from one study Gs0118069,
  not six independent studies; broad freshwater-lake biome and local glacial-lake
  slots remain context. The direct GOLD occurrence inventory has zero counts, so the
  attestation correctly omits positive counts rather than importing the separate bulk/API
  counts. The separate Glacier > Meltwater record ENVO:01000722 retains node7297 and
  its one ORGANISM assertion. The existing ENVO:01001511 frozen-precursor exclusion
  and all444 exclusion rows remain byte-identical to main. Native NARROW/REVIEWED
  is derived from the new ITEM decision, not this review. The generated active decision
  history is regenerated; old committed session histories and immutable reviews are
  not rewritten. The shared attestation comparison-endpoint contract remains unresolved
  under #1398; this review does not certify SSSOM/KGX conformance.'
source:
  git_revision: 01ae8d08f5a8d337371399078b6d0c18a40df645
  state: git_commit
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 4544b5d2c11fbbb3a46cd8a65f7e664363df78c1000c590aab533219f9eec59b
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: d429c8bb74f521df9a77a90b216a44fc6959ee28efb1fa17a93582536caa8bce
    role: context
  - path: CLAUDE.md
    sha256: 98d95f910ff5160bc5b2ff572766785519dacdba487700bebaa6dbf96d071fd9
    role: context
  - path: curation/decisions.tsv
    sha256: eb82cec48508912622b452ae78bb1ad199c93cb0591ce534bb8f25273da4e220
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: c7017ce7889ebfce889eb6f2c6a6c12510428be4b8a4370e2e4e165231e1af25
    role: context
  - path: curation/term_requests.tsv
    sha256: 331a7d9eb8a8909fc37402c0a776838979a8065644504d5c4f2a1c39bce5c24d
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: b59b9e800a918135e3915145d4d8098bb48dcea36a312b3004c594a57d221ae9
    role: context
  - path: data/habitats/aquatic/freshwater_ice.yaml
    sha256: 1b72924519135c1a5c864fe9653c42e401cb923c3a4dcbf90d5f8044ee843b06
    role: context
  - path: data/habitats/aquatic/glacier_meltwater.yaml
    sha256: c336889d26d9fb31a1938bd2a2fdfb607d797c3ccdefcaae8677751d01111828
    role: target
  - path: data/habitats/aquatic/meltwater.yaml
    sha256: e14ab751da93d929738709f395eb9ad007bb39e443033a47448d59fa4bd3da55
    role: context
  - path: data/raw/gold_ecosystem_paths.tsv
    sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
    role: context
  - path: data/raw/gold_path_biosamples.tsv
    sha256: 97cd7c8d0e731d07a85db6986dbcf9e49096a3c7988bd90a855599f492fe619e
    role: context
  - path: data/raw/gold_path_triads.tsv
    sha256: b1717bd8fc4fdcd6a1a132f4eb32df3638b01ddf7d78f9a5797f110ee2b1e8d6
    role: context
  - path: data/raw/gold_studies.tsv
    sha256: fa7aaa46f288d10c453bb723e6cf486cde646a003559414b5523cc3883a84c8c
    role: context
  - path: data/raw/ontology_subclass_edges.tsv
    sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
    role: context
  - path: data/raw/ontology_terms.tsv
    sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
    role: context
  - path: docs/CURATION.md
    sha256: 36df8306394c06c352b73e0bf7b47a2858784cedac7389a24d0b78f593ece646
    role: context
  - path: docs/HARMONIZATION.md
    sha256: ee39d3cd29115ee14f5e7386169c76c47d471ebdc2502c008c49d30fb44918f1
    role: context
  - path: docs/RESEARCH.md
    sha256: 82c5471890d310bf8fd33141d5596f847bfc1eb6091c2db6f485388435e067af
    role: context
  - path: docs/record-review-profile.md
    sha256: 105b3c8e10f43ce689b05d3089d3a8be1d713a98dd6806e11be37ebd85b10590
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/mappings/glacier_meltwater/2026-10-03T095306Z-codex-fd45bd.yaml
    sha256: 6701348b75653edbd81b3178fa0e8a3534d30668ddbf3f227d97dab4ed242040
    role: context
  - path: history/mappings/glacier_meltwater/2026-10-12T022359Z-codex-gpt-5-52f1f3.yaml
    sha256: df2621a8a7f96b930243c836b0d9904340a8717d3c8c9793459d4b872c91557e
    role: context
  - path: history/mappings/glacier_meltwater/2026-10-13T020352Z-codex-gpt-5-cb66a0.yaml
    sha256: f02401ba70eace5f4e47f79a9aa506d3cc0b4ad1ff9fd72ac9f984cdd645ccca
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reviews/structured/20261012T015233Z-glacier_meltwater/review.yaml
    sha256: bf1a8fc9857d15e7931a69af2a9ce86538239e3c230053b90cdfbec7483bed32
    role: context
  - path: reviews/structured/20261012T025310Z-glacier_meltwater-followup/review.yaml
    sha256: a8f0b4246b46aa596ed91a9a8327e3491943ff225d04286d1aad621db2ccfa6b
    role: context
  - path: src/habitatmech/curate/decisions.py
    sha256: f33d3e9dc95bb428e63e640d48d4074cf15e90ea666603fb16fb651d591e3f02
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
    role: context
  - path: src/habitatmech/seed.py
    sha256: 4adf105e23d75c3563a516a0c160623d1065df7fcb2f31b7a0a0a8303d0401be
    role: context
  - path: tests/test_fourth_aquatic_review_fixes.py
    sha256: 0bcb26d4264c75a4f34e5940f22b7afe45ae1b3cf533cd8ae4b6248fa3df68e6
    role: context
  - path: tests/test_glacier_meltwater_grounding.py
    sha256: 6f2c9a4e846daa5717d60f16921fe4459e71d7daf5e0c911b27ec9d4511dcc0e
    role: context
targets:
- target_id: habitatmech:GOLD.f3dc60ff11
  path: data/habitats/aquatic/glacier_meltwater.yaml
  label: Glacier meltwater
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Source-specific identity and lifecycle decisions
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Authored definitions and genus
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Guarded source context-parent exclusions
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Pinned ontology labels, definitions and synonyms
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_subclass_edges.tsv
    role: Pinned ontology hierarchy
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Harmonization and generated record construction
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Frozen GOLD source inventory
scope:
  description: Entire exact glacier-meltwater record and its sole source concept;
    bounded curation follow-up.
  selection: Explicit remaining scientific scope in PR1218; no new distinct-record
    coverage.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.f3dc60ff11
checks:
- check_id: C0
  name: Native post-correction gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.f3dc60ff11
  command: just render
  exit_code: 0
  evidence_ids:
  - CHECKS
  summary: Actual success from 2026-10-13T02:11:15.117890+00:00 to 2026-10-13T02:12:11.751759+00:00.
    Scientific scope remains one target.
- check_id: C1
  name: Native post-correction gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.f3dc60ff11
  command: just validate data/habitats/aquatic/glacier_meltwater.yaml
  exit_code: 0
  evidence_ids:
  - CHECKS
  summary: Actual success from 2026-10-13T02:07:54.478180+00:00 to 2026-10-13T02:07:59.049500+00:00.
    Scientific scope remains one target.
- check_id: C2
  name: Native post-correction gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.f3dc60ff11
  command: just validate-strict data/habitats/aquatic/glacier_meltwater.yaml
  exit_code: 0
  evidence_ids:
  - CHECKS
  summary: Actual success from 2026-10-13T02:07:59.050451+00:00 to 2026-10-13T02:08:10.568140+00:00.
    Scientific scope remains one target.
- check_id: C3
  name: Native post-correction gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.f3dc60ff11
  command: just validate-products
  exit_code: 0
  evidence_ids:
  - CHECKS
  summary: Actual success from 2026-10-13T02:08:10.569120+00:00 to 2026-10-13T02:09:49.514758+00:00.
    Scientific scope remains one target.
- check_id: C4
  name: Native post-correction gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.f3dc60ff11
  command: just validate-history
  exit_code: 0
  evidence_ids:
  - CHECKS
  summary: Actual success from 2026-10-13T02:09:49.516177+00:00 to 2026-10-13T02:10:00.046475+00:00.
    Scientific scope remains one target.
- check_id: C5
  name: Native post-correction gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.f3dc60ff11
  command: just provenance-check
  exit_code: 0
  evidence_ids:
  - CHECKS
  summary: Actual success from 2026-10-13T02:10:00.047246+00:00 to 2026-10-13T02:10:00.898990+00:00.
    Scientific scope remains one target.
- check_id: C6
  name: Native post-correction gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.f3dc60ff11
  command: just verify-corpus
  exit_code: 0
  evidence_ids:
  - CHECKS
  summary: Actual success from 2026-10-13T02:10:00.899837+00:00 to 2026-10-13T02:10:22.775641+00:00.
    Scientific scope remains one target.
- check_id: C7
  name: Native post-correction gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.f3dc60ff11
  command: just validate-causal-all
  exit_code: 0
  evidence_ids:
  - CHECKS
  summary: Actual success from 2026-10-13T02:10:22.776432+00:00 to 2026-10-13T02:10:29.162380+00:00.
    Scientific scope remains one target.
- check_id: C8
  name: Native post-correction gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.f3dc60ff11
  command: just term-requests-check
  exit_code: 0
  evidence_ids:
  - CHECKS
  summary: Actual success from 2026-10-13T02:10:29.163275+00:00 to 2026-10-13T02:10:58.864928+00:00.
    Scientific scope remains one target.
- check_id: C9
  name: Native post-correction gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.f3dc60ff11
  command: uv run ruff check .
  exit_code: 0
  evidence_ids:
  - CHECKS
  summary: Actual success from 2026-10-13T02:10:58.866342+00:00 to 2026-10-13T02:10:59.300405+00:00.
    Scientific scope remains one target.
- check_id: C10
  name: Native post-correction gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.f3dc60ff11
  command: git diff --check 679a57e04cd2581aec2cfbd1cdc5a78f09ec8a4a
  exit_code: 0
  evidence_ids:
  - CHECKS
  summary: Actual success from 2026-10-13T02:10:59.301236+00:00 to 2026-10-13T02:10:59.793415+00:00.
    Scientific scope remains one target.
- check_id: QC
  name: Corrected-input hosted authoritative QC
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.f3dc60ff11
  command: gh run view 38335796983 --log
  exit_code: 0
  evidence_ids:
  - CHECKS
  summary: 'Exact-head authoritative hosted QC passed: 1060 tests, 3 skipped, and
    all native quality gates. Captured scientific inputs were hash-rechecked unchanged;
    new review files require final-head CI.'
evidence:
- evidence_id: PRIOR
  kind: prior_review
  reference: reviews/structured/20261012T025310Z-glacier_meltwater-followup/review.yaml
  accessed_at: '2026-10-13T02:33:26.238159Z'
  support: supports
  summary: Exact predecessor and original review read in full; the precursor exclusion
    was resolved previously, while optional genus curation was explicitly outside
    that earlier scope.
- evidence_id: CURRENT
  kind: record_content
  reference: data/habitats/aquatic/glacier_meltwater.yaml; curation/decisions.tsv:1349;
    data/raw/gold_ecosystem_paths.tsv:1472; data/raw/gold_path_biosamples.tsv:728;
    data/raw/gold_path_triads.tsv:305-307; data/raw/gold_studies.tsv:1057
  accessed_at: '2026-10-13T02:33:26.238159Z'
  support: supports
  summary: 'This review assesses the captured scientific files at pinned commit 01ae8d08f5a8d337371399078b6d0c18a40df645.
    Every captured blob was also verified byte-identical on current head 348085582b0090404a73c122376b8045e6050c41
    after map/site regeneration. Reassessed the entire glacier-specific source after
    integrating PR1218 with main. The ITEM GROUND_AS_PARENT decision retains habitatmech:GOLD.f3dc60ff11
    and adds ENVO:01000722 as a strictly broader meltwater genus. The current official
    ENVO definition spans snow and several ice sources, while the GOLD label specifies
    glacier origin. Frozen medium annotation covers six samples from one study Gs0118069,
    not six independent studies; broad freshwater-lake biome and local glacial-lake
    slots remain context. The direct GOLD occurrence inventory has zero counts, so
    the attestation correctly omits positive counts rather than importing the separate
    bulk/API counts. The separate Glacier > Meltwater record ENVO:01000722 retains
    node7297 and its one ORGANISM assertion. The existing ENVO:01001511 frozen-precursor
    exclusion and all444 exclusion rows remain byte-identical to main. Native NARROW/REVIEWED
    is derived from the new ITEM decision, not this review. The generated active decision
    history is regenerated; old committed session histories and immutable reviews
    are not rewritten. The shared attestation comparison-endpoint contract remains
    unresolved under #1398; this review does not certify SSSOM/KGX conformance.'
- evidence_id: ENVO
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000722
  accessed_at: '2026-10-13T02:33:26.238159Z'
  support: supports
  summary: 'Current official OLS JSON inspected: active ENVO:01000722, canonical label
    meltwater, definition explicitly includes water from glacial ice alongside snow
    and other ice sources. Matches frozen ontology_terms row8217 and liquid-water
    subclass edge row6492; supports a broader genus, not exact identity.'
- evidence_id: CONTRACT
  kind: record_content
  reference: src/habitatmech/schema/habitatmech.yaml:317; src/habitatmech/seed.py:595;
    https://github.com/CultureBotAI/HabitatMech/issues/1398
  accessed_at: '2026-10-13T02:33:26.238159Z'
  support: supports
  summary: Schema says mapping_predicate relates the source to this record identifier
    and is absent when the record is the source concept. The curated parent route
    instead preserves the mint and emits skos:narrowMatch for its comparison with
    the broader ontology parent. The comparison object is not explicit in the attestation.
    This is a representation ambiguity, not a claim of formal SKOS inconsistency.
- evidence_id: CHECKS
  kind: record_content
  reference: tests/test_glacier_meltwater_grounding.py; tests/test_fourth_aquatic_review_fixes.py;
    https://github.com/CultureBotAI/HabitatMech/actions/runs/38335796983
  accessed_at: '2026-10-13T02:33:26.238159Z'
  support: supports
  summary: 'Sixty-nine focused exclusion/curation-floor tests passed; a later 33-test
    genus/earlier-cohort suite passed after correcting the reproduced stale expectation
    tracked in #2034. Native post-correction gates and corrected-input hosted QC passed.
    Generated map uses the unchanged pinned runtime, verified changed-record inference
    and repeat reuse, all3208 points, zero omissions. New review integrity and final-head
    checks remain separate publication gates.'
assessments:
- assessment_id: GENUS
  area: grounding
  topic: Glacier-specific identity, broader meltwater genus and frozen precursor
  outcome: supported
  target_ids:
  - habitatmech:GOLD.f3dc60ff11
  evidence_ids:
  - CURRENT
  - ENVO
  - PRIOR
  summary: 'This review assesses the captured scientific files at pinned commit 01ae8d08f5a8d337371399078b6d0c18a40df645.
    Every captured blob was also verified byte-identical on current head 348085582b0090404a73c122376b8045e6050c41
    after map/site regeneration. Reassessed the entire glacier-specific source after
    integrating PR1218 with main. The ITEM GROUND_AS_PARENT decision retains habitatmech:GOLD.f3dc60ff11
    and adds ENVO:01000722 as a strictly broader meltwater genus. The current official
    ENVO definition spans snow and several ice sources, while the GOLD label specifies
    glacier origin. Frozen medium annotation covers six samples from one study Gs0118069,
    not six independent studies; broad freshwater-lake biome and local glacial-lake
    slots remain context. The direct GOLD occurrence inventory has zero counts, so
    the attestation correctly omits positive counts rather than importing the separate
    bulk/API counts. The separate Glacier > Meltwater record ENVO:01000722 retains
    node7297 and its one ORGANISM assertion. The existing ENVO:01001511 frozen-precursor
    exclusion and all444 exclusion rows remain byte-identical to main. Native NARROW/REVIEWED
    is derived from the new ITEM decision, not this review. The generated active decision
    history is regenerated; old committed session histories and immutable reviews
    are not rewritten. The shared attestation comparison-endpoint contract remains
    unresolved under #1398; this review does not certify SSSOM/KGX conformance.'
- assessment_id: SOURCES
  area: provenance
  topic: Frozen counters, triad roles and independent study denominator
  outcome: supported
  target_ids:
  - habitatmech:GOLD.f3dc60ff11
  evidence_ids:
  - CURRENT
  - CHECKS
  summary: The sole source node7784 and exact five-level path remain. Six medium-annotated
    samples arise from one study; zero direct counts, separate bulk/API counts and
    omitted display counts are not interchangeable. No taxa, parameters, causal graphs
    or universal ecological measurements are invented.
- assessment_id: ENDPOINT
  area: grounding
  topic: Attestation comparison-object contract
  outcome: concern
  target_ids:
  - habitatmech:GOLD.f3dc60ff11
  evidence_ids:
  - CONTRACT
  summary: The schema defines mapping_predicate from source_id to this record identifier,
    while the actual narrow route retains the source mint and compares it to a broader
    ontology parent. This is a representation-contract mismatch, not a claim of formal
    SKOS inconsistency. SSSOM/KGX readiness is not established.
findings:
- finding_id: F1
  issue_key: habitatmech-gold.f3dc60ff11-context-parent
  category: scope
  severity: major
  status: resolved
  certainty: confirmed
  title: A source setting or material is emitted as a strict superclass
  description: The former GOLD freshwater-ice superclass remains excluded; the separate
    new meltwater genus does not reintroduce the precursor edge.
  target_ids:
  - habitatmech:GOLD.f3dc60ff11
  field_paths:
  - parent_habitats
  evidence_ids:
  - PRIOR
  - CURRENT
  - CHECKS
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Exact source-path and expected-parent guards
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: major
  normalization_reason: Material hierarchy, identity, scope or comparison-contract
    concern.
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261012T025310Z-glacier_meltwater-followup
    finding_id: F1
  disposition_reason: 'Reconfirmed the earlier resolved context-parent disposition:
    the maintained exclusion is unchanged and a whole-corpus regression retains independent
    parents. This review assesses the captured scientific files at pinned commit 01ae8d08f5a8d337371399078b6d0c18a40df645.
    Every captured blob was also verified byte-identical on current head 348085582b0090404a73c122376b8045e6050c41
    after map/site regeneration. Reassessed the entire glacier-specific source after
    integrating PR1218 with main. The ITEM GROUND_AS_PARENT decision retains habitatmech:GOLD.f3dc60ff11
    and adds ENVO:01000722 as a strictly broader meltwater genus. The current official
    ENVO definition spans snow and several ice sources, while the GOLD label specifies
    glacier origin. Frozen medium annotation covers six samples from one study Gs0118069,
    not six independent studies; broad freshwater-lake biome and local glacial-lake
    slots remain context. The direct GOLD occurrence inventory has zero counts, so
    the attestation correctly omits positive counts rather than importing the separate
    bulk/API counts. The separate Glacier > Meltwater record ENVO:01000722 retains
    node7297 and its one ORGANISM assertion. The existing ENVO:01001511 frozen-precursor
    exclusion and all444 exclusion rows remain byte-identical to main. Native NARROW/REVIEWED
    is derived from the new ITEM decision, not this review. The generated active decision
    history is regenerated; old committed session histories and immutable reviews
    are not rewritten. The shared attestation comparison-endpoint contract remains
    unresolved under #1398; this review does not certify SSSOM/KGX conformance.'
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1994
- finding_id: F2
  issue_key: habitatmech-gold.f3dc60ff11-mapping-endpoint-contract
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: NARROW comparison endpoint is ambiguous under the attestation contract
  description: The schema defines mapping_predicate from source_id to this record
    identifier, while the actual narrow route retains the source mint and compares
    it to a broader ontology parent. This is a representation-contract mismatch, not
    a claim of formal SKOS inconsistency. SSSOM/KGX readiness is not established.
  target_ids:
  - habitatmech:GOLD.f3dc60ff11
  field_paths:
  - source_attestations.mapping_predicate
  evidence_ids:
  - CURRENT
  - CONTRACT
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained owner of the exact finding; never patch generated YAML
  rule_id: docs/CURATION.md; docs/record-review-profile.md
  native_severity: major
  normalization_reason: Material claim or representation mismatch.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
actions:
- action_id: A1
  description: Resolve source-to-record versus source-to-ontology-parent comparison
    semantics with seeder and downstream export regressions; a predicate-only replacement
    is insufficient.
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.f3dc60ff11
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained owner of the exact finding; never patch generated YAML
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Reassess the exact source and preserve independent valid genera, source IDs, counts/units
    and omitted counts.
  - Change maintained owners with append-only curation history; do not rewrite generated
    records or saved reviews.
  - Add focused regressions; inspect guarded canaries and pass strict schema, labels,
    history, provenance, reproduction and QC.
  - Use a linked successor review for any disposition; this assessment records proposed
    work, not an executed repair.
limitations:
- Same-agent adversarial review, not independent approval.
- The original occurrence membership limitations in the predecessor remain. Ignored-inclusive
  searches covered reviews/structured, curation, history, research, conf, reports/yaml_record_review
  and data/raw for the exact source ID, slug and label; no new original membership
  evidence was established.
- The live GOLD study page returned a request error; no claim of fresh authenticated
  GOLD API membership verification is made. Frozen inventories support the bounded
  denominator.
- 'iModulonDB is not applicable: no gene, regulator, strain-specific expression module
  or transcriptomic claim occurs in this record.'
- 'Ontology-label validation retains configured no-adapter skips and accepted exceptions.
  SSSOM/KGX conformance remains uncertified under #1398.'
- 'This review resolves no unrelated #1220 or corpus-wide scientific finding. Optional
  definitions and organism/parameter examples are not inferred from a habitat name.'
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261012T025310Z-glacier_meltwater-followup
  relationship: Reconfirms the resolved precursor exclusion and assesses the separately
    curated genus and endpoint contract
tags:
- habitatmech
- record-review
- followup
```
