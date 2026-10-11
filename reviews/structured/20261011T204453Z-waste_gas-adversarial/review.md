# Adversarial correction: waste-gas association scope

- Review: 20261011T204453Z-waste_gas-adversarial
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-11T20:43:53.089213Z
- Finished UTC: 2026-10-11T20:44:53.141937Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Adversarial correction of predecessor F1: the unchanged record already identifies the BacDive attestations as waste-gas biofilter cohorts in its DEFINED history, from curation/term_requests.tsv. The schema defines source assertions and taxon associations, not direct gas-phase sampling, and no taxon asserts is_characteristic. BacDive11867 is therefore consistent with the qualified association rather than proof of a wrong gas-material identity. The definition and ENVO:01000797 genus remain defensible. Retain only a minor, provisional association-level provenance question because the original twenty strain assertions were not recovered. Do not rewrite the gas definition, delete taxa or relabel the entire source bin on this evidence.

## Scope And Provenance

Reassessment of the full unchanged waste-gas record, correcting the predecessor interpretation of source-association scope.

Selection: Linked adversarial successor; no new distinct-record coverage.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6e131fdf701d16afc5cdd22cef5aabbdfaed17a2.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:BACDIVE.3eec8fcfc4 | data/habitats/engineered/waste_gas.yaml | generated | waste gas |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native validation | passed | True | habitatmech:BACDIVE.3eec8fcfc4 | Actual check started 2026-10-11T20:44:47.446969Z; finished 2026-10-11T20:44:49.620525Z.  |
| Native validation | passed | True | habitatmech:BACDIVE.3eec8fcfc4 | Actual check started 2026-10-11T20:44:49.621070Z; finished 2026-10-11T20:44:53.141032Z.  |
| Exact captured-base required CI | passed | True | habitatmech:BACDIVE.3eec8fcfc4 | Actual check started 2026-10-11T20:27:27.310650+00:00; finished 2026-10-11T20:41:36.562878+00:00. Authoritative full QC on exact head 6e131fdf701d16afc5cdd22cef5aabbdfaed17a2 passed783 tests with3 skipped; all required workflows succeeded. https://github.com/CultureBotAI/HabitatMech/actions/runs/38172269357 |

## Scientific And Domain Assessments

### Gas material and valid genus

identity: supported. Targets: habitatmech:BACDIVE.3eec8fcfc4.

The defined anthropogenic gaseous effluent and ENVO:01000797 genus remain supported. Biofilter contextual associations do not turn this gas-material class into the biofilter bed. No exact ontology identity or status promotion is inferred.

### Actual assertion semantics and existing qualification

evidence: supported. Targets: habitatmech:BACDIVE.3eec8fcfc4.

Adversarial correction of predecessor F1: the unchanged record already identifies the BacDive attestations as waste-gas biofilter cohorts in its DEFINED history, from curation/term_requests.tsv. The schema defines source assertions and taxon associations, not direct gas-phase sampling, and no taxon asserts is_characteristic. BacDive11867 is therefore consistent with the qualified association rather than proof of a wrong gas-material identity. The definition and ENVO:01000797 genus remain defensible. Retain only a minor, provisional association-level provenance question because the original twenty strain assertions were not recovered. Do not rewrite the gas definition, delete taxa or relabel the entire source bin on this evidence.

### Frozen aggregate counts and missing member-level traceability

provenance: concern. Targets: habitatmech:BACDIVE.3eec8fcfc4.

All twenty STRAIN assertions and seventeen aggregate taxon rows reproduce unchanged. Original assertion-level membership remains unrecovered; the predecessor documents the bounded ignored-inclusive source search. This observation adds no broader absence claim.

### Unchanged remaining field review

completeness: supported. Targets: habitatmech:BACDIVE.3eec8fcfc4.

All fields, lifecycle and history were re-read. Prior full-record ontology/taxon identifier checks remain applicable to identical values. No environmental parameter, causal graph or characteristic taxon claim is present in this exact file. No gene or transcriptomic claim makes iModulonDB applicable; no optional field is invented.

## Findings

### F1: Frozen waste-gas association contexts remain incompletely traceable

minor / open / provisional; issue key: habitatmech-bacdive.3eec8fcfc4-gas-biofilter-association-scope.

The gas/biofilter boundary is already explicitly qualified and the schema permits the retained source associations. The unrecovered original twenty strain assertions prevent a per-association check of exact sampling context. More accessible pair-level provenance may help consumers, but the inspected witness does not establish a material identity error or warrant deleting retained associations.

## Recommended Actions And Acceptance Checks

### A1

Keep #1964 as a bounded provenance investigation. Recover original assertion-level source evidence before changing pair context. Do not equate source association with direct gas sampling, rename the gas class, delete taxa or change frozen counts based on one later strain witness.

- Recover the original source revision and verify exact strain membership, not a later replacement export.
- Document actual gas versus biofilter context per recovered assertion; preserve legitimate source associations and all source units.
- Only make an evidence-backed maintained-input or transform change, with native history, canary reproduction and validation when a record change is authorized.
- Save a linked successor; the review correction itself does not resolve the remaining provenance uncertainty.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| PRIOR | reviews/structured/20261011T195952Z-waste_gas/review.yaml | partial | Full predecessor assessment retained as historical evidence. Its major/confirmed F1 overstates direct-sampling semantics; its frozen reproduction, identifier checks and original membership limits remain relevant. |
| CURRENT | data/habitats/engineered/waste_gas.yaml | supports | Full unchanged record re-read, including all seventeen taxon associations and explicit gas-stream/biofilter-bed qualification in DEFINED history. Twenty STRAIN assertions, valid gas-material genus, UNGROUNDED/REVIEWED lifecycle and no characteristic taxon promotion. |
| OWNER | curation/term_requests.tsv:62; curation/decisions.tsv:1565 | supports | Exact BACDIVE.3eec8fcfc4 maintained rows already identify the Engineered &gt; Waste &gt; Waste gas concept, qualify biofilter cohorts, and distinguish the gas material from the biofilter bed. |
| SCHEMA | src/habitatmech/schema/habitatmech.yaml:289-327,389-451 | supports | SourceAttestation counts upstream links; CharacteristicTaxon means association. Neither entails direct gas-phase isolation. The stronger characteristic claim requires an explicit flag and supporting reference. |
| RAW | data/raw/bacdive_isolation_sources.tsv:116; data/raw/bacdive_source_taxa.tsv:2982-2998 | supports | Ignored-inclusive exact-key search and complete matched-row inspection confirm twenty frozen strains and seventeen source taxon rows. These aggregate rows do not identify all original strain members or their sampling contexts. |
| BACDIVE | https://bacdive.dsmz.de/strain/11867 | supports | Reopened official strain page: 905/1, DSM19730, NCBITaxon:469551 is assigned to Engineered &gt; Waste &gt; Waste gas and described as isolated from a treatment biofilter. This later witness supports contextual association; it does not establish all frozen strain memberships or gas-phase sampling. |

## Limits And Additional Notes

- The baseline review is retained immutable; this successor supersedes only its F1 severity, certainty and rationale.
- Original twenty-strain membership remains unrecovered. Current BacDive evidence is a context witness, not a replacement frozen dataset.
- PubMed web reopening returned no abstract text in this pass; the predecessor inspected abstract evidence is not upgraded to full-text support.
- Same-agent adversarial review, not independent approval. Full QC applies to the captured input commit; this new bundle still requires review-integrity and final-head checks.
- SSSOM/KGX current kg-microbe compatibility remains unverified. No new distinct-record coverage or whole-corpus pass is claimed.
- Review artifact defect tracked in #1969; source-provenance question remains open in #1964.
- No habitat record, maintained curation row, generated page or scientific lifecycle is changed by this correction.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T204453Z-waste_gas-adversarial
kind: record
repository: CultureBotAI/HabitatMech
title: 'Adversarial correction: waste-gas association scope'
started_at: '2026-10-11T20:43:53.089213Z'
finished_at: '2026-10-11T20:44:53.141937Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Continuing agent has participated in HabitatMech curation and
    earlier reviews; this is not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Adversarial correction of predecessor F1: the unchanged record already identifies
  the BacDive attestations as waste-gas biofilter cohorts in its DEFINED history,
  from curation/term_requests.tsv. The schema defines source assertions and taxon
  associations, not direct gas-phase sampling, and no taxon asserts is_characteristic.
  BacDive11867 is therefore consistent with the qualified association rather than
  proof of a wrong gas-material identity. The definition and ENVO:01000797 genus remain
  defensible. Retain only a minor, provisional association-level provenance question
  because the original twenty strain assertions were not recovered. Do not rewrite
  the gas definition, delete taxa or relabel the entire source bin on this evidence.'
source:
  git_revision: 6e131fdf701d16afc5cdd22cef5aabbdfaed17a2
  state: working_tree
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
  - path: conf/id_label_targets.yaml
    sha256: e100d84aabccaeb00c1a60246142b3cafcec009dbfba58f5cc319c35adddb633
    role: context
  - path: conf/record_review.yaml
    sha256: c2f5d0eb4c5744f5fe354c92184ddab144dc2688dba952b032b4f3d597bc08d6
    role: context
  - path: conf/sources.yaml
    sha256: a8e069f9278068b57fa234f43e03c8d893f857827b83fd10cfa92d6815aed642
    role: context
  - path: curation/decisions.tsv
    sha256: 7cbec6d310b1aac248defdbe657e68c0cc1e848981230d2279e63f474c6f4c96
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 2d41fc93db4939122b3909f2a412b84b679703948b10d9f02e12021442f71407
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 53522d2fbe1cfa6c6a350a46170de9b80b1fa138dfcf4e9ddb0b5851f29d1c88
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: 3f2ce04805defe5ff65dc20988cc72bc94d4636b3140eb1311017866bdc0ea0a
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: b59b9e800a918135e3915145d4d8098bb48dcea36a312b3004c594a57d221ae9
    role: context
  - path: data/habitats/engineered/waste_gas.yaml
    sha256: e50a50cb3974a53395923f22c41435a8a981df7abb1f0730fcc7108cc02ee027
    role: target
  - path: data/raw/GOLD_MANIFEST.yaml
    sha256: 99ec487ae02d512cfb75440685f927abe907effe52cb755feb095631e8841489
    role: context
  - path: data/raw/MANIFEST.yaml
    sha256: 4657672d429be35e551ceef4a1204ab0a8120558ce63e2a2b74188eee94b8480
    role: context
  - path: data/raw/bacdive_isolation_sources.tsv
    sha256: fb1645dd899a43130be9cf38b0e8b27ffbaa0175306917bff20e20ee225875fc
    role: context
  - path: data/raw/bacdive_source_taxa.tsv
    sha256: 08471c12f887882e2a6af8f078166b1f59ed7e2b24eb7edbe43a7fc77dfbad44
    role: context
  - path: data/raw/environment_parameters.tsv
    sha256: a75d0f565d8ee2498188ff98b17d0ab325ae4f782601bf4414eff6e86c13e0f9
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
    sha256: 36df8306394c06c352b73e0bf7b47a2858784cedac7389a24d0b78f593ece646
    role: context
  - path: docs/HARMONIZATION.md
    sha256: ee39d3cd29115ee14f5e7386169c76c47d471ebdc2502c008c49d30fb44918f1
    role: context
  - path: docs/RESEARCH.md
    sha256: 82c5471890d310bf8fd33141d5596f847bfc1eb6091c2db6f485388435e067af
    role: context
  - path: docs/record-review-profile.md
    sha256: f7aa39ee762d94f1902d9f08f328cb897bc543e4e226057eb4770d24bfcc6eb5
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: research/habitats/other/waste-gas-habitatmech-bacdive-3eec8fcfc4-deep-research-claude_code.md
    sha256: 7cb0023d6b84d6907fd8ace8dff73969415ce3d0b7cfbfbddaa17130ae4f3690
    role: context
  - path: reviews/structured/20261011T195952Z-waste_gas/review.yaml
    sha256: b35a4691d3a2f018d2136b0ec836edf46fab47734f617a635c27eafd2a76ed06
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/extract_gold_biosamples.py
    sha256: b6a2773c86fe718e1ca0b1d7b32709f0eee491ac813655e310aa0817c0fec31b
    role: context
  - path: scripts/extract_source_inventory.py
    sha256: 4bf5391d25ff48a2d81eb3821af6582de063fd0391440973d309dfd93016490c
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
    role: context
  - path: src/habitatmech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/habitatmech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/habitatmech/seed.py
    sha256: 4adf105e23d75c3563a516a0c160623d1065df7fcb2f31b7a0a0a8303d0401be
    role: context
targets:
- target_id: habitatmech:BACDIVE.3eec8fcfc4
  path: data/habitats/engineered/waste_gas.yaml
  label: waste gas
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Per-source grounding and native review-depth decisions
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Exact GOLD context-parent contribution decisions
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Curated definition, genus and lexical scope
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Pinned ontology identity, labels, synonyms and definitions
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_subclass_edges.tsv
    role: Pinned ontology hierarchy
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Source harmonization and generated output
  - repository: CultureBotAI/HabitatMech
    path: data/raw/bacdive_isolation_sources.tsv
    role: Frozen isolation-source vocabulary
  - repository: CultureBotAI/HabitatMech
    path: data/raw/isolation_source_groundings.tsv
    role: Upstream grounding decisions
  - repository: CultureBotAI/HabitatMech
    path: data/raw/bacdive_source_taxa.tsv
    role: Frozen strain-derived taxon assertions
scope:
  description: Reassessment of the full unchanged waste-gas record, correcting the
    predecessor interpretation of source-association scope.
  selection: Linked adversarial successor; no new distinct-record coverage.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:BACDIVE.3eec8fcfc4
checks:
- check_id: C0
  name: Native validation
  required: true
  status: passed
  target_ids:
  - habitatmech:BACDIVE.3eec8fcfc4
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just validate
    data/habitats/engineered/waste_gas.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: 'Actual check started 2026-10-11T20:44:47.446969Z; finished 2026-10-11T20:44:49.620525Z. '
- check_id: C1
  name: Native validation
  required: true
  status: passed
  target_ids:
  - habitatmech:BACDIVE.3eec8fcfc4
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just validate-strict
    data/habitats/engineered/waste_gas.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: 'Actual check started 2026-10-11T20:44:49.621070Z; finished 2026-10-11T20:44:53.141032Z. '
- check_id: C2
  name: Exact captured-base required CI
  required: true
  status: passed
  target_ids:
  - habitatmech:BACDIVE.3eec8fcfc4
  command: gh pr checks codex/record-reviews-20261011p --watch --interval 30
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual check started 2026-10-11T20:27:27.310650+00:00; finished 2026-10-11T20:41:36.562878+00:00.
    Authoritative full QC on exact head 6e131fdf701d16afc5cdd22cef5aabbdfaed17a2 passed783
    tests with3 skipped; all required workflows succeeded. https://github.com/CultureBotAI/HabitatMech/actions/runs/38172269357
evidence:
- evidence_id: PRIOR
  kind: prior_review
  reference: reviews/structured/20261011T195952Z-waste_gas/review.yaml
  accessed_at: '2026-10-11T20:43:53.089213Z'
  support: partial
  summary: Full predecessor assessment retained as historical evidence. Its major/confirmed
    F1 overstates direct-sampling semantics; its frozen reproduction, identifier checks
    and original membership limits remain relevant.
- evidence_id: CURRENT
  kind: record_content
  reference: data/habitats/engineered/waste_gas.yaml
  accessed_at: '2026-10-11T20:44:53.141937Z'
  support: supports
  summary: Full unchanged record re-read, including all seventeen taxon associations
    and explicit gas-stream/biofilter-bed qualification in DEFINED history. Twenty
    STRAIN assertions, valid gas-material genus, UNGROUNDED/REVIEWED lifecycle and
    no characteristic taxon promotion.
- evidence_id: OWNER
  kind: record_content
  reference: curation/term_requests.tsv:62; curation/decisions.tsv:1565
  accessed_at: '2026-10-11T20:44:53.141937Z'
  support: supports
  summary: Exact BACDIVE.3eec8fcfc4 maintained rows already identify the Engineered
    > Waste > Waste gas concept, qualify biofilter cohorts, and distinguish the gas
    material from the biofilter bed.
- evidence_id: SCHEMA
  kind: record_content
  reference: src/habitatmech/schema/habitatmech.yaml:289-327,389-451
  accessed_at: '2026-10-11T20:44:53.141937Z'
  support: supports
  summary: SourceAttestation counts upstream links; CharacteristicTaxon means association.
    Neither entails direct gas-phase isolation. The stronger characteristic claim
    requires an explicit flag and supporting reference.
- evidence_id: RAW
  kind: record_content
  reference: data/raw/bacdive_isolation_sources.tsv:116; data/raw/bacdive_source_taxa.tsv:2982-2998
  accessed_at: '2026-10-11T20:44:53.141937Z'
  support: supports
  summary: Ignored-inclusive exact-key search and complete matched-row inspection
    confirm twenty frozen strains and seventeen source taxon rows. These aggregate
    rows do not identify all original strain members or their sampling contexts.
- evidence_id: BACDIVE
  kind: database
  reference: https://bacdive.dsmz.de/strain/11867
  accessed_at: '2026-10-11T20:44:53.141937Z'
  support: supports
  summary: 'Reopened official strain page: 905/1, DSM19730, NCBITaxon:469551 is assigned
    to Engineered > Waste > Waste gas and described as isolated from a treatment biofilter.
    This later witness supports contextual association; it does not establish all
    frozen strain memberships or gas-phase sampling.'
assessments:
- assessment_id: IDENTITY
  area: identity
  topic: Gas material and valid genus
  outcome: supported
  target_ids:
  - habitatmech:BACDIVE.3eec8fcfc4
  evidence_ids:
  - CURRENT
  - OWNER
  - PRIOR
  summary: The defined anthropogenic gaseous effluent and ENVO:01000797 genus remain
    supported. Biofilter contextual associations do not turn this gas-material class
    into the biofilter bed. No exact ontology identity or status promotion is inferred.
- assessment_id: ASSOCIATIONS
  area: evidence
  topic: Actual assertion semantics and existing qualification
  outcome: supported
  target_ids:
  - habitatmech:BACDIVE.3eec8fcfc4
  evidence_ids:
  - CURRENT
  - OWNER
  - SCHEMA
  - BACDIVE
  summary: 'Adversarial correction of predecessor F1: the unchanged record already
    identifies the BacDive attestations as waste-gas biofilter cohorts in its DEFINED
    history, from curation/term_requests.tsv. The schema defines source assertions
    and taxon associations, not direct gas-phase sampling, and no taxon asserts is_characteristic.
    BacDive11867 is therefore consistent with the qualified association rather than
    proof of a wrong gas-material identity. The definition and ENVO:01000797 genus
    remain defensible. Retain only a minor, provisional association-level provenance
    question because the original twenty strain assertions were not recovered. Do
    not rewrite the gas definition, delete taxa or relabel the entire source bin on
    this evidence.'
- assessment_id: PROVENANCE
  area: provenance
  topic: Frozen aggregate counts and missing member-level traceability
  outcome: concern
  target_ids:
  - habitatmech:BACDIVE.3eec8fcfc4
  evidence_ids:
  - RAW
  - PRIOR
  - CURRENT
  summary: All twenty STRAIN assertions and seventeen aggregate taxon rows reproduce
    unchanged. Original assertion-level membership remains unrecovered; the predecessor
    documents the bounded ignored-inclusive source search. This observation adds no
    broader absence claim.
- assessment_id: COMPLETENESS
  area: completeness
  topic: Unchanged remaining field review
  outcome: supported
  target_ids:
  - habitatmech:BACDIVE.3eec8fcfc4
  evidence_ids:
  - PRIOR
  - CURRENT
  summary: All fields, lifecycle and history were re-read. Prior full-record ontology/taxon
    identifier checks remain applicable to identical values. No environmental parameter,
    causal graph or characteristic taxon claim is present in this exact file. No gene
    or transcriptomic claim makes iModulonDB applicable; no optional field is invented.
findings:
- finding_id: F1
  issue_key: habitatmech-bacdive.3eec8fcfc4-gas-biofilter-association-scope
  category: scope
  severity: minor
  status: open
  certainty: provisional
  title: Frozen waste-gas association contexts remain incompletely traceable
  description: The gas/biofilter boundary is already explicitly qualified and the
    schema permits the retained source associations. The unrecovered original twenty
    strain assertions prevent a per-association check of exact sampling context. More
    accessible pair-level provenance may help consumers, but the inspected witness
    does not establish a material identity error or warrant deleting retained associations.
  target_ids:
  - habitatmech:BACDIVE.3eec8fcfc4
  field_paths:
  - source_attestations
  - characteristic_taxa
  evidence_ids:
  - PRIOR
  - CURRENT
  - OWNER
  - SCHEMA
  - RAW
  - BACDIVE
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: data/raw/bacdive_source_taxa.tsv
    role: Frozen source-association evidence, not a manual rewrite target
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Future source-context presentation, only if supported by recovered evidence
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: minor
  normalization_reason: Non-blocking provenance uncertainty, not a confirmed unsupported
    identity or direct-isolation assertion.
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261011T195952Z-waste_gas
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1964
actions:
- action_id: A1
  description: 'Keep #1964 as a bounded provenance investigation. Recover original
    assertion-level source evidence before changing pair context. Do not equate source
    association with direct gas sampling, rename the gas class, delete taxa or change
    frozen counts based on one later strain witness.'
  finding_ids:
  - F1
  target_ids:
  - habitatmech:BACDIVE.3eec8fcfc4
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: data/raw/bacdive_source_taxa.tsv
    role: Frozen source-association evidence, not a manual rewrite target
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Future source-context presentation, only if supported by recovered evidence
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Recover the original source revision and verify exact strain membership, not a
    later replacement export.
  - Document actual gas versus biofilter context per recovered assertion; preserve
    legitimate source associations and all source units.
  - Only make an evidence-backed maintained-input or transform change, with native
    history, canary reproduction and validation when a record change is authorized.
  - Save a linked successor; the review correction itself does not resolve the remaining
    provenance uncertainty.
limitations:
- The baseline review is retained immutable; this successor supersedes only its F1
  severity, certainty and rationale.
- Original twenty-strain membership remains unrecovered. Current BacDive evidence
  is a context witness, not a replacement frozen dataset.
- PubMed web reopening returned no abstract text in this pass; the predecessor inspected
  abstract evidence is not upgraded to full-text support.
- Same-agent adversarial review, not independent approval. Full QC applies to the
  captured input commit; this new bundle still requires review-integrity and final-head
  checks.
- SSSOM/KGX current kg-microbe compatibility remains unverified. No new distinct-record
  coverage or whole-corpus pass is claimed.
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261011T195952Z-waste_gas
  relationship: Corrects overstatement of F1 while retaining the same association-scope
    issue key
notes:
- 'Review artifact defect tracked in #1969; source-provenance question remains open
  in #1964.'
- No habitat record, maintained curation row, generated page or scientific lifecycle
  is changed by this correction.
tags:
- habitatmech
- record-review
- adversarial-correction
```
