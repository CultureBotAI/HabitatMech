# Scoped hierarchy resolution: Pond scum

- Review: 20261010T020508Z-pond_scum-followup
- Repository: culturebotai/HabitatMech
- Started UTC: 2026-10-10T01:52:36.495529Z
- Finished UTC: 2026-10-10T02:05:08Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The enclosing algae raceway pond is no longer asserted as a genus of scum. The exact aquaculture/raceway source path and GOLD node 8140 remain. Minted identity, zero-count omission, UNGROUNDED and CLASS/SEEDED state are unchanged; no replacement genus, definition or organism claim is introduced.

## Scope And Provenance

Resolve the exact parent finding and verify preservation of every other target claim.

Selection: Explicit successor to 20261010T011542Z-pond_scum F1, not a new coverage target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base b4396b5610e6af19a1627623158abc1917f19d81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.6e0470a1d8 | data/habitats/engineered/pond_scum.yaml | generated | Pond scum |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Target schema | passed | True | habitatmech:GOLD.6e0470a1d8 | No issues found; exit 0. |
| Strict target validation | passed | True | habitatmech:GOLD.6e0470a1d8 | One file; zero errors. |
| Corpus reproduction | passed | True | habitatmech:GOLD.6e0470a1d8 | 3208 expected/found; zero missing, extra or differing. |
| Scoped regression and publication provenance | passed | True | habitatmech:GOLD.6e0470a1d8 | 3 passed in 59.57s; the new whole-corpus curation regression also passed separately in 6.97s. |
| History validation | passed | True | habitatmech:GOLD.6e0470a1d8 | All 232 history records validate. |
| Label correspondence | passed | True | habitatmech:GOLD.6e0470a1d8 | 1178 canonical, 1 synonym, 5 accepted exceptions; 2057 no-adapter skips. No new identity was grounded. |
| Complete authoritative quality gate in exact-product CI | passed | True | habitatmech:GOLD.6e0470a1d8 | 656 passed, 3 skipped in 469.45s (0:07:49); all HabitatMech quality gates passed. The CI workflow executes scripts/run_qc.py, the same authoritative runner as just qc; this records actual CI results rather than a local execution claim. |
| Exact-product CI | passed | True | habitatmech:GOLD.6e0470a1d8 | Completed success at b4396b5610e6af19a1627623158abc1917f19d81; the same authoritative gate is verified independently of local execution. |
| Downloaded semantic map | passed | True | habitatmech:GOLD.6e0470a1d8 | Complete input identity, profile, cache and finite map bundle verified; all 3208 records retained. |
| Generated site | passed | True | habitatmech:GOLD.6e0470a1d8 | 3208 habitat pages, 252 redirects, eight categories and 114 term-request pages match the corpus. |
| Initial review immutability | passed | True | habitatmech:GOLD.6e0470a1d8 | 87 bundles validated before this successor; all 174 existing files also verified against a separate SHA256 manifest. |
| Durable review base | passed | True | habitatmech:GOLD.6e0470a1d8 | Annotated tag 3cfb5a4cbb7cd0cbc85f738adf2e9280a4df5201 peels to the exact reviewed product commit. |
| Premature artifact check | failed | False | habitatmech:GOLD.6e0470a1d8 | First attempt ran before the download completed and exited 1 for missing current.json. The completed download was subsequently checked successfully in C9; no guard was bypassed. |

## Scientific And Domain Assessments

### Material versus container hierarchy

grounding: supported. Targets: habitatmech:GOLD.6e0470a1d8.

The enclosing algae raceway pond is no longer asserted as a genus of scum. The exact aquaculture/raceway source path and GOLD node 8140 remain. Minted identity, zero-count omission, UNGROUNDED and CLASS/SEEDED state are unchanged; no replacement genus, definition or organism claim is introduced.

### Source, count and status preservation

provenance: supported. Targets: habitatmech:GOLD.6e0470a1d8.

Exact GOLD provenance, zero-count omission, all previous events and native status remain. Only the guarded exclusion event and separate session history are added.

### Products and native gates

consistency: supported. Targets: habitatmech:GOLD.6e0470a1d8.

The corpus reproduces and the refreshed map, pages, checks and review-base provenance pass.

## Findings

### F1: Scum material is not a subtype of its enclosing algae raceway pond

major / resolved / confirmed; issue key: gold-6e0470a1d8-raceway-context-parent.

The sole GOLD parent contribution habitatmech:GOLD.e474187df8 expresses collection/container context rather than a strictly broader class of scum. Suppress only this exact contribution through curation/gold_parent_exclusions.tsv after authorized curation; retain the original source path and minted habitat. Do not replace the identity with ENVO:03600047 or invent a definition solely to remove the edge.

Disposition: The enclosing algae raceway pond is no longer asserted as a genus of scum. The exact aquaculture/raceway source path and GOLD node 8140 remain. Minted identity, zero-count omission, UNGROUNDED and CLASS/SEEDED state are unchanged; no replacement genus, definition or organism claim is introduced.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/engineered/pond_scum.yaml; Full regenerated YAML and exact original-base diff | supports | The enclosing algae raceway pond is no longer asserted as a genus of scum. The exact aquaculture/raceway source path and GOLD node 8140 remain. Minted identity, zero-count omission, UNGROUNDED and CLASS/SEEDED state are unchanged; no replacement genus, definition or organism claim is introduced. Every other field and prior event is unchanged. |
| E2 | curation/gold_parent_exclusions.tsv; Exact habitatmech:GOLD.6e0470a1d8 row, source path and expected parent guard | supports | The maintained exclusion suppresses only this immediate GOLD context contribution. The source material and its enclosing constructed pond have different scope. No independent genus or other source is removed. |
| E3 | reviews/structured/20261010T011542Z-pond_scum/review.yaml; F1 and its AMNH, current-ontology and source-path evidence | supports | Retains the original scientific observation. The AMNH sampling transcript and current ENVO:03600047 constructed-pond definition were also reinspected during this publication session. Illustrative material/container evidence does not reconstruct this exact GOLD member roster. |
| E4 | tests/test_pond_scum_parent_curation.py; Complete before/after corpus and semantic-text comparison | supports | Only the pond-scum record and its semantic text change. All other records, source claims, status fields and earlier events are preserved. The scoped regression and publication tests passed. |
| E5 | https://github.com/CultureBotAI/HabitatMech/actions/runs/38014525767; Locked Linux rebuild at 453688a2e6cc367b2e42953f699ecaaf97aac644 | supports | One changed text encoded, repeat reuse verified, full embed reused all 3208 vectors. The downloaded inputs exactly match fresh local SHA256 8f9e85067b19e1fd5a17e7605b78a7133ad372c1c5f45bc6b6f6371c26e0b195. Bundle verification passes with 3208 unique finite points and unchanged encoder/projection settings. |
| E6 | https://github.com/CultureBotAI/HabitatMech/actions/runs/38014818143; Successful exact-product CI; job metadata and complete-gate log inspected | supports | CI QC: 656 passed, 3 skipped in 469.45s (0:07:49); all quality gates passed, including 232 history records, 3208 strict-valid and exactly reproduced records, generated site and backlog products. The native authoritative runner completed at 2026-10-10T02:02:49Z. This is completed CI execution, not a completed local full-QC claim. Deterministic checks do not certify full-corpus scientific completeness. |
| E7 | history/mappings/pond_scum/2026-10-10T014705Z-codex-gpt-5-f6e88e.yaml; Session actor, issue and evidence-backed event | supports | One new append-only session records codex-gpt-5, model gpt-5, tool codex and issue #1840; all 232 history records validate. The generated target separately retains its prior events. |

## Limits And Additional Notes

- Original August source members and a source-authored scum definition remain unavailable as documented in the initial review. This successor does not claim a new exhaustive membership search.
- No replacement genus, exact ontology identity, characteristic-taxon or causal claim is established. The record remains UNGROUNDED and SEEDED, not newly ITEM-reviewed.
- This is a scoped self-reviewed correction, not independent scientific sign-off or full-corpus certification. Three full-suite tests remain skipped. Four other batch findings remain open as issues #1841-#1844. The duplicate local full-QC run was still in progress at this observation; required full-gate evidence comes from the successful exact-product CI run, not an assumed local result.
- The first artifact check preceded download completion and was rerun successfully. History scaffolding required the configured CLAW path and access to the existing uv cache. The unchanged locked Linux environment supplied map products; no paid research provider was used.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T020508Z-pond_scum-followup
kind: record
repository: culturebotai/HabitatMech
title: 'Scoped hierarchy resolution: Pond scum'
started_at: '2026-10-10T01:52:36.495529Z'
finished_at: '2026-10-10T02:05:08Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same continuing agent inspected the target and primary evidence;
    no independent second-agent or human approval claimed.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The enclosing algae raceway pond is no longer asserted as a genus of scum.
  The exact aquaculture/raceway source path and GOLD node 8140 remain. Minted identity,
  zero-count omission, UNGROUNDED and CLASS/SEEDED state are unchanged; no replacement
  genus, definition or organism claim is introduced.
source:
  git_revision: b4396b5610e6af19a1627623158abc1917f19d81
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
  - path: conf/sources.yaml
    sha256: a8e069f9278068b57fa234f43e03c8d893f857827b83fd10cfa92d6815aed642
    role: context
  - path: curation/decisions.tsv
    sha256: 200a0185b77586aaea6bffd2b1e837fb671eb26e8f7f4d2cb05db658f9036972
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 2d41fc93db4939122b3909f2a412b84b679703948b10d9f02e12021442f71407
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 0da28df896b99166eff4fc193444df1d3e50afc66861b7ac91f7fe1f741cdcd1
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: 9977e384b79128d6e89c85f28e35c77d29644d503dea6d53c12628599e33f7f3
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: b59b9e800a918135e3915145d4d8098bb48dcea36a312b3004c594a57d221ae9
    role: context
  - path: data/habitats/engineered/algae_raceway_pond.yaml
    sha256: da0a058100de66d14600405da09f1b52433c287ae5be16ad7db99f7db158d498
    role: context
  - path: data/habitats/engineered/animal_waste_material.yaml
    sha256: 2ad8d7faa1132d2403bc1d7596521fb659304ff5013b808249bc1fe5b35404c6
    role: context
  - path: data/habitats/engineered/built_environment.yaml
    sha256: df6de674d7d48a98b7d1d43a0a5c67a696550f00e1fb787ec71a3569acc47021
    role: context
  - path: data/habitats/engineered/drugs_supplements.yaml
    sha256: 9c3c8c406932e6ca70dde612b0d06eca33752d837247169d94a174714589bf33
    role: context
  - path: data/habitats/engineered/industrial_wastewater.yaml
    sha256: 07698df721a169cd55c2d1ce80027df8c8a3140536ba99eee312272887ce8768
    role: context
  - path: data/habitats/engineered/meat_poultry_processing_plant.yaml
    sha256: 5214e20505e29115a647ff3feb08ecdaf3436b214cebce771ac3381aa70a4445
    role: context
  - path: data/habitats/engineered/pond_scum.yaml
    sha256: d88060eee35354095237f263c95ec7ab30c362d56ef2d503a548730c0bd76b36
    role: target
  - path: data/habitats/engineered/poultry_confinement_building.yaml
    sha256: 874a2a199447f2ea5b1e1c9b8ea94bf6b19a047e799f51a5d19830162d5061a4
    role: context
  - path: data/habitats/engineered/poultry_farm.yaml
    sha256: 93dd2c4e144d112c39469e169c80d3da6bde7bd23310ac03ad4be9556cd76940
    role: context
  - path: data/habitats/engineered/poultry_litter.yaml
    sha256: 5c22c29b2f019d5b4003a2cfa50f7171b1131f6e7413d9e8b112811db41d38b6
    role: context
  - path: data/habitats/engineered/poultry_processing_wastewater.yaml
    sha256: d5dcb3c9f5b5d9175fe2ef909bcffb284f44184a506d8b1bcc4ace20652ca2c2
    role: context
  - path: data/habitats/engineered/probiotics.yaml
    sha256: cb84cbee3bee82b1ec1a823c21647c9ac69f3bb2f803db69f5990189b0552b09
    role: context
  - path: data/habitats/other/animal_litter.yaml
    sha256: ab90548229d5dd304b65b3c91f8c04c4efd847ba38876c79e42c0dd09dc4630f
    role: context
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
  - path: data/text_map/141910442a3dbfde26202297db6ef20ce6f3e275ade8e2624f2b9a0189f8bb0f/manifest.json
    sha256: a0ee8d42bb74e2333f31cc92cc8376d23512b9d2718fe7cdc001ebd794ef8c84
    role: context
  - path: data/text_map/141910442a3dbfde26202297db6ef20ce6f3e275ade8e2624f2b9a0189f8bb0f/points.json
    sha256: d9272efb856c139cb1b30ce59ce67fcd10e1493ebf0fb487d59caf00d0f1a3d9
    role: context
  - path: data/text_map/current.json
    sha256: 2f588d168603c043316fb7c0a530b209848bbcd799e69ce276532297f896af16
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
  - path: history/mappings/pond_scum/2026-10-10T014705Z-codex-gpt-5-f6e88e.yaml
    sha256: 537a96e50409071ed84f86d6ff3af428123c1f469538cd5c17f0d7c09f88881e
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: pages/habitats/pond-scum-habitatmech-gold-6e0470a1d8.html
    sha256: e9fa0c192b7709008fe90ec2b6367fdb07eb33825346da023afa0f2d711566ef
    role: context
  - path: reviews/structured/20261009T080101Z-meat_poultry_processing_plant/review.yaml
    sha256: 4e0a7376b1bd8dd6cf50b921a7b31ba398c1f31dbaf04ecff27a25559c4dcc62
    role: context
  - path: reviews/structured/20261010T011542Z-pond_scum/review.yaml
    sha256: 17601d45673dfe53775588744a30b2c4fa1d7e25afc86020b20f67655c226a11
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/extract_gold_biosamples.py
    sha256: b6a2773c86fe718e1ca0b1d7b32709f0eee491ac813655e310aa0817c0fec31b
    role: context
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 52d2a22309a1f4a10728a663560bb4d918346c292221fd34139b99b4159d3fe5
    role: context
  - path: src/habitatmech/seed.py
    sha256: 92adf631fa099120a497ff7001473e659347d23ac9b418f04cd341ddad5d2a89
    role: context
  - path: tests/test_pond_scum_parent_curation.py
    sha256: 09457669d063afd3393001d2cc7d255b3ddf9bf29429b993add164632167f4ef
    role: context
  - path: tests/test_record_review_publication.py
    sha256: 3a04daba5cf0244be57d4fd80824d372511f6105f06146d0a159f9fe0e7e69c0
    role: context
scope:
  description: Resolve the exact parent finding and verify preservation of every other
    target claim.
  selection: Explicit successor to 20261010T011542Z-pond_scum F1, not a new coverage
    target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.6e0470a1d8
  exclusions:
  - target: New source-member census, new exact grounding and other habitats
    reason: The scope is the correction and unchanged-claim verification.
targets:
- target_id: habitatmech:GOLD.6e0470a1d8
  path: data/habitats/engineered/pond_scum.yaml
  label: Pond scum
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: source-concept grounding and review depth
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: authored definition and genus
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: guarded source-context parent exclusions
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: frozen GOLD source IDs, paths and counts
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: generated identity, parents, status and attestations
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: source inventory transformations
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: stable slug mapping
checks:
- check_id: C1
  name: Target schema
  command: just validate data/habitats/engineered/pond_scum.yaml
  status: passed
  required: true
  exit_code: 0
  summary: No issues found; exit 0.
  target_ids:
  - habitatmech:GOLD.6e0470a1d8
- check_id: C2
  name: Strict target validation
  command: just validate-strict data/habitats/engineered/pond_scum.yaml
  status: passed
  required: true
  exit_code: 0
  summary: One file; zero errors.
  target_ids:
  - habitatmech:GOLD.6e0470a1d8
- check_id: C3
  name: Corpus reproduction
  command: just verify-corpus
  status: passed
  required: true
  exit_code: 0
  summary: 3208 expected/found; zero missing, extra or differing.
  target_ids:
  - habitatmech:GOLD.6e0470a1d8
- check_id: C4
  name: Scoped regression and publication provenance
  command: uv run pytest -q tests/test_pond_scum_parent_curation.py tests/test_record_review_publication.py
  status: passed
  required: true
  exit_code: 0
  summary: 3 passed in 59.57s; the new whole-corpus curation regression also passed
    separately in 6.97s.
  target_ids:
  - habitatmech:GOLD.6e0470a1d8
- check_id: C5
  name: History validation
  command: just validate-history
  status: passed
  required: true
  exit_code: 0
  summary: All 232 history records validate.
  target_ids:
  - habitatmech:GOLD.6e0470a1d8
- check_id: C6
  name: Label correspondence
  command: just validate-products
  status: passed
  required: true
  exit_code: 0
  summary: 1178 canonical, 1 synonym, 5 accepted exceptions; 2057 no-adapter skips.
    No new identity was grounded.
  target_ids:
  - habitatmech:GOLD.6e0470a1d8
- check_id: C7
  name: Complete authoritative quality gate in exact-product CI
  command: gh run view 38014818143 --log | rg 'passed,|All HabitatMech quality gates|history
    record\(s\)|files scanned:|differing:|pages/ is in step'
  status: passed
  required: true
  exit_code: 0
  summary: 656 passed, 3 skipped in 469.45s (0:07:49); all HabitatMech quality gates
    passed. The CI workflow executes scripts/run_qc.py, the same authoritative runner
    as just qc; this records actual CI results rather than a local execution claim.
  target_ids:
  - habitatmech:GOLD.6e0470a1d8
- check_id: C8
  name: Exact-product CI
  command: gh run view 38014818143 --json status,conclusion,headSha,url
  status: passed
  required: true
  exit_code: 0
  summary: Completed success at b4396b5610e6af19a1627623158abc1917f19d81; the same
    authoritative gate is verified independently of local execution.
  target_ids:
  - habitatmech:GOLD.6e0470a1d8
- check_id: C9
  name: Downloaded semantic map
  command: uv run python scripts/embedding_pipeline.py check --output build/pr1839-map-download/data/text_map
    --input build/text-map/pr1839-inputs.jsonl --cache build/pr1839-map-download/build/text-map/vectors.sqlite
  status: passed
  required: true
  exit_code: 0
  summary: Complete input identity, profile, cache and finite map bundle verified;
    all 3208 records retained.
  target_ids:
  - habitatmech:GOLD.6e0470a1d8
- check_id: C10
  name: Generated site
  command: just render-check
  status: passed
  required: true
  exit_code: 0
  summary: 3208 habitat pages, 252 redirects, eight categories and 114 term-request
    pages match the corpus.
  target_ids:
  - habitatmech:GOLD.6e0470a1d8
- check_id: C11
  name: Initial review immutability
  command: uv run python scripts/record_review.py check --base 3d606e0925fd933182595bd81fd5cfea9cc18f0b
  status: passed
  required: true
  exit_code: 0
  summary: 87 bundles validated before this successor; all 174 existing files also
    verified against a separate SHA256 manifest.
  target_ids:
  - habitatmech:GOLD.6e0470a1d8
- check_id: C12
  name: Durable review base
  command: git ls-remote --tags origin 'refs/tags/record-review-base/b4396b5610e6af19a1627623158abc1917f19d81*'
  status: passed
  required: true
  exit_code: 0
  summary: Annotated tag 3cfb5a4cbb7cd0cbc85f738adf2e9280a4df5201 peels to the exact
    reviewed product commit.
  target_ids:
  - habitatmech:GOLD.6e0470a1d8
- check_id: C13
  name: Premature artifact check
  command: uv run python scripts/embedding_pipeline.py check --output build/pr1839-map-download/data/text_map
    --input build/text-map/pr1839-inputs.jsonl --cache build/pr1839-map-download/build/text-map/vectors.sqlite
  status: failed
  required: false
  exit_code: 1
  summary: First attempt ran before the download completed and exited 1 for missing
    current.json. The completed download was subsequently checked successfully in
    C9; no guard was bypassed.
  target_ids:
  - habitatmech:GOLD.6e0470a1d8
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/engineered/pond_scum.yaml
  locator: Full regenerated YAML and exact original-base diff
  accessed_at: '2026-10-10T02:05:08Z'
  support: supports
  summary: The enclosing algae raceway pond is no longer asserted as a genus of scum.
    The exact aquaculture/raceway source path and GOLD node 8140 remain. Minted identity,
    zero-count omission, UNGROUNDED and CLASS/SEEDED state are unchanged; no replacement
    genus, definition or organism claim is introduced. Every other field and prior
    event is unchanged.
- evidence_id: E2
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: Exact habitatmech:GOLD.6e0470a1d8 row, source path and expected parent
    guard
  accessed_at: '2026-10-10T02:05:08Z'
  support: supports
  summary: The maintained exclusion suppresses only this immediate GOLD context contribution.
    The source material and its enclosing constructed pond have different scope. No
    independent genus or other source is removed.
- evidence_id: E3
  kind: prior_review
  reference: reviews/structured/20261010T011542Z-pond_scum/review.yaml
  locator: F1 and its AMNH, current-ontology and source-path evidence
  accessed_at: '2026-10-10T02:05:08Z'
  support: supports
  summary: Retains the original scientific observation. The AMNH sampling transcript
    and current ENVO:03600047 constructed-pond definition were also reinspected during
    this publication session. Illustrative material/container evidence does not reconstruct
    this exact GOLD member roster.
- evidence_id: E4
  kind: validation
  reference: tests/test_pond_scum_parent_curation.py
  locator: Complete before/after corpus and semantic-text comparison
  accessed_at: '2026-10-10T02:05:08Z'
  support: supports
  summary: Only the pond-scum record and its semantic text change. All other records,
    source claims, status fields and earlier events are preserved. The scoped regression
    and publication tests passed.
- evidence_id: E5
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38014525767
  locator: Locked Linux rebuild at 453688a2e6cc367b2e42953f699ecaaf97aac644
  accessed_at: '2026-10-10T02:05:08Z'
  support: supports
  summary: One changed text encoded, repeat reuse verified, full embed reused all
    3208 vectors. The downloaded inputs exactly match fresh local SHA256 8f9e85067b19e1fd5a17e7605b78a7133ad372c1c5f45bc6b6f6371c26e0b195.
    Bundle verification passes with 3208 unique finite points and unchanged encoder/projection
    settings.
- evidence_id: E6
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38014818143
  locator: Successful exact-product CI; job metadata and complete-gate log inspected
  accessed_at: '2026-10-10T02:05:08Z'
  support: supports
  summary: 'CI QC: 656 passed, 3 skipped in 469.45s (0:07:49); all quality gates passed,
    including 232 history records, 3208 strict-valid and exactly reproduced records,
    generated site and backlog products. The native authoritative runner completed
    at 2026-10-10T02:02:49Z. This is completed CI execution, not a completed local
    full-QC claim. Deterministic checks do not certify full-corpus scientific completeness.'
- evidence_id: E7
  kind: record_content
  reference: history/mappings/pond_scum/2026-10-10T014705Z-codex-gpt-5-f6e88e.yaml
  locator: Session actor, issue and evidence-backed event
  accessed_at: '2026-10-10T02:05:08Z'
  support: supports
  summary: 'One new append-only session records codex-gpt-5, model gpt-5, tool codex
    and issue #1840; all 232 history records validate. The generated target separately
    retains its prior events.'
assessments:
- assessment_id: A1
  area: grounding
  topic: Material versus container hierarchy
  outcome: supported
  summary: The enclosing algae raceway pond is no longer asserted as a genus of scum.
    The exact aquaculture/raceway source path and GOLD node 8140 remain. Minted identity,
    zero-count omission, UNGROUNDED and CLASS/SEEDED state are unchanged; no replacement
    genus, definition or organism claim is introduced.
  target_ids:
  - habitatmech:GOLD.6e0470a1d8
  evidence_ids:
  - E1
  - E2
  - E3
- assessment_id: A2
  area: provenance
  topic: Source, count and status preservation
  outcome: supported
  summary: Exact GOLD provenance, zero-count omission, all previous events and native
    status remain. Only the guarded exclusion event and separate session history are
    added.
  target_ids:
  - habitatmech:GOLD.6e0470a1d8
  evidence_ids:
  - E1
  - E2
  - E4
  - E7
- assessment_id: A3
  area: consistency
  topic: Products and native gates
  outcome: supported
  summary: The corpus reproduces and the refreshed map, pages, checks and review-base
    provenance pass.
  target_ids:
  - habitatmech:GOLD.6e0470a1d8
  evidence_ids:
  - E4
  - E5
  - E6
findings:
- finding_id: F1
  issue_key: gold-6e0470a1d8-raceway-context-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Scum material is not a subtype of its enclosing algae raceway pond
  description: The sole GOLD parent contribution habitatmech:GOLD.e474187df8 expresses
    collection/container context rather than a strictly broader class of scum. Suppress
    only this exact contribution through curation/gold_parent_exclusions.tsv after
    authorized curation; retain the original source path and minted habitat. Do not
    replace the identity with ENVO:03600047 or invent a definition solely to remove
    the edge.
  target_ids:
  - habitatmech:GOLD.6e0470a1d8
  field_paths:
  - parent_habitats
  evidence_ids:
  - E1
  - E2
  - E3
  - E4
  - E6
  rule_id: 'Native checklist: source scope, strictly broader parents and evidence
    strength; docs/CURATION.md'
  native_severity: major
  normalization_reason: The full target and parent plus direct material/container
    observations establish a false is-a interpretation, which materially changes graph
    semantics.
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: source-concept grounding and review depth
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: guarded source-context parent exclusions
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: generated identity, parents, status and attestations
  previous_occurrences:
  - repository: culturebotai/HabitatMech
    review_id: 20261010T011542Z-pond_scum
    finding_id: F1
  disposition_reason: The enclosing algae raceway pond is no longer asserted as a
    genus of scum. The exact aquaculture/raceway source path and GOLD node 8140 remain.
    Minted identity, zero-count omission, UNGROUNDED and CLASS/SEEDED state are unchanged;
    no replacement genus, definition or organism claim is introduced.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1840
actions: []
limitations:
- Original August source members and a source-authored scum definition remain unavailable
  as documented in the initial review. This successor does not claim a new exhaustive
  membership search.
- No replacement genus, exact ontology identity, characteristic-taxon or causal claim
  is established. The record remains UNGROUNDED and SEEDED, not newly ITEM-reviewed.
- 'This is a scoped self-reviewed correction, not independent scientific sign-off
  or full-corpus certification. Three full-suite tests remain skipped. Four other
  batch findings remain open as issues #1841-#1844. The duplicate local full-QC run
  was still in progress at this observation; required full-gate evidence comes from
  the successful exact-product CI run, not an assumed local result.'
- The first artifact check preceded download completion and was rerun successfully.
  History scaffolding required the configured CLAW path and access to the existing
  uv cache. The unchanged locked Linux environment supplied map products; no paid
  research provider was used.
related_reviews:
- repository: culturebotai/HabitatMech
  review_id: 20261010T011542Z-pond_scum
  relationship: Explicitly resolves F1; preserves the immutable initial observation
links:
- https://github.com/CultureBotAI/HabitatMech/issues/1840
- https://github.com/CultureBotAI/HabitatMech/pull/1839
tags:
- habitatmech
- hierarchy
- followup
```
