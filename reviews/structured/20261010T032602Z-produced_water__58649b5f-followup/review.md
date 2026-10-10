# Scoped hierarchy resolution: petroleum produced water

- Review: 20261010T032602Z-produced_water__58649b5f-followup
- Repository: culturebotai/HabitatMech
- Started UTC: 2026-10-10T03:08:59Z
- Finished UTC: 2026-10-10T03:26:02Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Produced-water material is no longer asserted to be a subtype of an oil-reservoir landform. Only the guarded immediate GOLD source-parent contribution is excluded. The minted identity, node 7639, full petroleum-reservoir source path, one ORGANISM assertion, UNGROUNDED/CLASS/SEEDED state and all prior events are preserved. No new identity, genus, definition or biological claim is asserted.

## Scope And Provenance

Resolve the exact parent defect and verify preservation of all other target claims.

Selection: Explicit successor to the petroleum produced-water F1; not a new coverage target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7faca5a8c6d6a140f1163f923baf314d2cce279a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.bfd6bfa0f1 | data/habitats/engineered/produced_water__58649b5f.yaml | generated | Produced water |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Target LinkML | passed | True | habitatmech:GOLD.bfd6bfa0f1 | No issues found; unchanged corrected target. |
| Target strict schema | passed | True | habitatmech:GOLD.bfd6bfa0f1 | One file, zero errors. |
| Corpus reproduction | passed | True | habitatmech:GOLD.bfd6bfa0f1 | 3208 expected/found, zero missing/extra/differing. |
| Regression and publication provenance | passed | True | habitatmech:GOLD.bfd6bfa0f1 | 51 passed in 112.77s. New test separately passed in 9.86s. |
| History | passed | True | habitatmech:GOLD.bfd6bfa0f1 | 233 history records valid. |
| Ontology labels | passed | True | habitatmech:GOLD.bfd6bfa0f1 | 1178 canonical, 1 synonym, 5 accepted exceptions; 2057 no-adapter skips. No identity grounding added. |
| Authoritative exact-product CI | passed | True | habitatmech:GOLD.bfd6bfa0f1 | The same scripts/run_qc.py runner used by just qc completed successfully at 2026-10-10T03:22:45Z on 7faca5a8c6d6a140f1163f923baf314d2cce279a. 657 passed, 3 skipped in 481.19s (0:08:01); all native gates passed. Run metadata independently confirms completed success. |
| Map input/cache/bundle verification | passed | True | habitatmech:GOLD.bfd6bfa0f1 | Full input identity, pinned encoder, checksums, complete map and cache passed. Separate cmp confirmed identical Linux/local inputs; finite-point check retained all 3208 records. |
| Generated site | passed | True | habitatmech:GOLD.bfd6bfa0f1 | 3208 habitat pages, 252 redirects, eight categories and 114 term requests match generated inputs. |
| Original reviews preserved | passed | True | habitatmech:GOLD.bfd6bfa0f1 | 94 native reviews passed before this successor; all 188 saved files separately byte-compared with 34b698602 and every one of the six initial captures matched its main-base input hashes. |
| Retained publication base | passed | True | habitatmech:GOLD.bfd6bfa0f1 | Remote annotated provenance tag peels to the exact product/capture commit 7faca5a8c6d6a140f1163f923baf314d2cce279a. |
| Local model environment | failed | False | habitatmech:GOLD.bfd6bfa0f1 | Exited 2: pinned Torch has no macOS x86_64 wheel. The unchanged locked Linux workflow completed the required rebuild; downloaded products passed C8. No dependency guard was weakened. |

## Scientific And Domain Assessments

### Material versus landform

grounding: supported. Targets: habitatmech:GOLD.bfd6bfa0f1.

Produced-water material is no longer asserted to be a subtype of an oil-reservoir landform. Only the guarded immediate GOLD source-parent contribution is excluded. The minted identity, node 7639, full petroleum-reservoir source path, one ORGANISM assertion, UNGROUNDED/CLASS/SEEDED state and all prior events are preserved. No new identity, genus, definition or biological claim is asserted.

### Preserved claims and history

provenance: supported. Targets: habitatmech:GOLD.bfd6bfa0f1.

Exact source identifiers, path, one-ORGANISM unit/count, status and earlier events are unchanged. No parent taxa or other produced-water samples are inherited.

### Generated products and gates

consistency: supported. Targets: habitatmech:GOLD.bfd6bfa0f1.

Corpus reproduction, complete map, pages, native QC and durable base provenance passed.

## Findings

### F1: Produced-water material is not a subtype of its reservoir landform

major / resolved / confirmed; issue key: gold-bfd6bfa0f1-reservoir-context-parent.

Suppress only the exact source-path contribution of ENVO:00002185 through curation/gold_parent_exclusions.tsv. Preserve node 7639, the full source path, minted identity, one ORGANISM assertion and independent valid parents. Investigate any new material grounding separately with item-level evidence; do not merge produced-water siblings or transfer the reservoir parent's taxa.

Disposition: Produced-water material is no longer asserted to be a subtype of an oil-reservoir landform. Only the guarded immediate GOLD source-parent contribution is excluded. The minted identity, node 7639, full petroleum-reservoir source path, one ORGANISM assertion, UNGROUNDED/CLASS/SEEDED state and all prior events are preserved. No new identity, genus, definition or biological claim is asserted.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/engineered/produced_water__58649b5f.yaml; Full regenerated YAML and original-main comparison | supports | Produced-water material is no longer asserted to be a subtype of an oil-reservoir landform. Only the guarded immediate GOLD source-parent contribution is excluded. The minted identity, node 7639, full petroleum-reservoir source path, one ORGANISM assertion, UNGROUNDED/CLASS/SEEDED state and all prior events are preserved. No new identity, genus, definition or biological claim is asserted. |
| E2 | curation/gold_parent_exclusions.tsv; Exact habitatmech:GOLD.bfd6bfa0f1 row and guarded path/parent | supports | Suppresses ENVO:00002185 only for the petroleum-reservoir produced-water source. Other source paths, independent parents and all source inventory bytes are unchanged. |
| E3 | https://www.dsmz.de/collection/catalogue/details/culture/DSM-22707; DSM 22707 PEH A isolation source, location and sampling date, reinspected in this publication session | supports | The catalogue identifies the isolation material as petroleum-reservoir produced water from Kuparuk, Alaska, sampled 2008-01-24. This supports a sampled fluid, not a reservoir-landform identity; it does not reconstruct the original frozen GOLD roster. |
| E4 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO:00002185; Current API response: label, complete definition and obsolete flag | supports | The active oil-reservoir term denotes a subsurface hydrocarbon-bearing landform. Source origin is not a broader class of the sampled water material. |
| E5 | reviews/structured/20261010T024621Z-produced_water__58649b5f/review.yaml; Exact F1 and scoped source-membership limitations | supports | Retains the original scientific observation and stable issue key. This successor resolves only the parent defect, not the original frozen membership or a candidate exact water grounding. |
| E6 | tests/test_produced_water_parent_curation.py; Whole-corpus before/after document and semantic-text comparison | supports | Only this record and its semantic text change. Every other claim and record is unchanged. The focused regression passed alone and with 50 exclusion/publication tests. |
| E7 | https://github.com/CultureBotAI/HabitatMech/actions/runs/38019701934; Successful exact-product CI; run metadata and complete-gate log inspected | supports | The authoritative scripts/run_qc.py runner completed successfully on publication commit 7faca5a8c6d6a140f1163f923baf314d2cce279a at 2026-10-10T03:22:45Z. 657 passed, 3 skipped in 481.19s (0:08:01); all native gates passed. This is verified CI execution, not a completed local full-QC claim. |
| E8 | https://github.com/CultureBotAI/HabitatMech/actions/runs/38019413965; Successful locked Linux rebuild, downloaded artifact and local input/cache/bundle verification | supports | One changed-record vector encoded; repeated canary reused it; full embedding reused all 3208. Downloaded inputs byte-match local SHA256 f101d9a5c0ad2eed77c2aea5c533f42896d843c546c5eb53ae83547b26bca76f. All 3208 points are unique and finite, with none omitted. Encoder/projection settings unchanged. |
| E9 | history/mappings/produced_water__58649b5f/2026-10-10T030643Z-codex-gpt-5-88ca03.yaml; Complete append-only session record | supports | Records the actual agent, issue #1848, supporting evidence, preserved claims and preflight checks. All 233 session-history records validate. |

## Limits And Additional Notes

- Original frozen member identity and a source-authored definition remain unresolved as documented in the initial review. This successor does not claim a new exhaustive source census.
- No exact replacement ontology identity or new genus is established. Native status remains UNGROUNDED/SEEDED with the prior CLASS decision; resolving this hierarchy finding is not ITEM identity approval.
- Self-reviewed scoped correction, not independent approval, all-corpus scientific review, or SSSOM/KGX readiness. The four other findings remain open in #1846, #1847, #1849 and #1850. Three full-suite tests are skipped.
- The duplicate local full-QC run is still in progress at this observation. Required full-gate evidence comes from inspected successful exact-product CI, not an assumed local result.
- Local model environment unavailable on macOS x86_64; validated locked Linux build used without changing dependency pins. Optional environment failure is preserved in C12.
- The initial save was correctly rejected because HEAD advanced while generated products were committed. A new native inspection at the complete product commit verified all 59 captured input hashes unchanged. The target, correction, regression and product diff were reassessed without changing scientific claims. This new validated observation retains the actual original review start; no saved bundle was overwritten.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T032602Z-produced_water__58649b5f-followup
kind: record
repository: culturebotai/HabitatMech
title: 'Scoped hierarchy resolution: petroleum produced water'
started_at: '2026-10-10T03:08:59Z'
finished_at: '2026-10-10T03:26:02Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same continuing agent inspected source records, evidence and
    generated claims; no independent human or second-agent approval is claimed.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Produced-water material is no longer asserted to be a subtype of an oil-reservoir
  landform. Only the guarded immediate GOLD source-parent contribution is excluded.
  The minted identity, node 7639, full petroleum-reservoir source path, one ORGANISM
  assertion, UNGROUNDED/CLASS/SEEDED state and all prior events are preserved. No
  new identity, genus, definition or biological claim is asserted.
source:
  git_revision: 7faca5a8c6d6a140f1163f923baf314d2cce279a
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
  - path: conf/text_map.yaml
    sha256: b35f851c06a367b1bb121744c26bf82963d9e4885a7afb4cadbc59120f47ab75
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
    sha256: 68c45b6528747cdc39d067f5032e3898a7f0109ba0bde739c0e4f821b8afaf1e
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
  - path: data/habitats/engineered/industrial_waste_material.yaml
    sha256: 0d57cbfda093a70c21d801ea59f10959e09670e6c211a2ce4554296cf1132f85
    role: context
  - path: data/habitats/engineered/industrial_wastewater.yaml
    sha256: 07698df721a169cd55c2d1ce80027df8c8a3140536ba99eee312272887ce8768
    role: context
  - path: data/habitats/engineered/membrane_bioreactor.yaml
    sha256: 89d8964bce58cdeac9c2d3cc6db41e3cab4ef5ef6a6f2e312deaf115306c77fe
    role: context
  - path: data/habitats/engineered/mine_water.yaml
    sha256: c285eed1f2bc078931182954bb1f290d8e0a7c05cc5940fbac9509503ef6b38c
    role: context
  - path: data/habitats/engineered/nutrient_rich.yaml
    sha256: e722d3b49b5dbb4dfde7e2112c47a8752d2e33803ce612c33890d7cf1dbf08c7
    role: context
  - path: data/habitats/engineered/produced_water__123adb7f.yaml
    sha256: c6fb2b744303f124538e3047148380c739a366f45787e07a8cb385e1899a7a87
    role: context
  - path: data/habitats/engineered/produced_water__4b7c7f10.yaml
    sha256: 4b37e393fae66ff1930d74f03c7c3ff495ce4317baea2a907efc2afa4182e4b5
    role: context
  - path: data/habitats/engineered/produced_water__58649b5f.yaml
    sha256: aae821a2930b740ad36e0588e4b066bb396f04e5386412e42b29fadeb38763ce
    role: target
  - path: data/habitats/engineered/pulp_and_paper_wastewater.yaml
    sha256: 2c6b31dc0f6d04cf05618f1b54b08ba6a0ee1fffb14e24c48011b072a3bf693a
    role: context
  - path: data/habitats/engineered/r2a_agar.yaml
    sha256: 53384072a3f8547c68d59a2d7ecb40bc654f68bda9ed19ab83252e084de6da5b
    role: context
  - path: data/habitats/engineered/radioactive_waste.yaml
    sha256: c1d6093e3d810ceb4c4b277c83909fc968f8fa84c2f511f82eba4e2f936a5d43
    role: context
  - path: data/habitats/terrestrial/oil_reservoir.yaml
    sha256: 091dd4b2be2cf7a26ad7c42451a8b60b1214aecab56bd3b7ac9219082aea1d9a
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
  - path: data/text_map/a56d320c9e562fab87b2e29d1ce81a4104d1f3f68b70f9719876ac73b2966f61/manifest.json
    sha256: f7c531fe37956c40cd7904f074451508f09be76c75419ed4db0eeff69b5234e5
    role: context
  - path: data/text_map/current.json
    sha256: 148b82161ed27a88b7ae0a1d242ed0946826c60fd178ef4cbe2270f0b5811473
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
  - path: history/mappings/produced_water__58649b5f/2026-10-10T030643Z-codex-gpt-5-88ca03.yaml
    sha256: 7e86655313e8c58e379b591fb4a9a789770584f9f30255b7f5b6127975df7fa1
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reviews/structured/20261010T024621Z-produced_water__58649b5f/review.md
    sha256: a4d82d71e41fb362ed4934694338e7d34cd0bdb677386dfed0adc1b2f7fde599
    role: context
  - path: reviews/structured/20261010T024621Z-produced_water__58649b5f/review.yaml
    sha256: dd2b7ad03d2698e79a757beda343441c71093bf1d690885cc35b9a36adf493e7
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
  - path: tests/test_produced_water_parent_curation.py
    sha256: 3b393fe4308e09eb3a20cb41f74537b7469e6443898c632d54f463c72167040c
    role: context
scope:
  description: Resolve the exact parent defect and verify preservation of all other
    target claims.
  selection: Explicit successor to the petroleum produced-water F1; not a new coverage
    target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.bfd6bfa0f1
  exclusions:
  - target: New member census, exact groundwater identity and other habitats
    reason: Limited to this source-context hierarchy correction.
targets:
- target_id: habitatmech:GOLD.bfd6bfa0f1
  path: data/habitats/engineered/produced_water__58649b5f.yaml
  label: Produced water
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
  - repository: culturebotai/HabitatMech
    path: data/raw/gold_path_biosamples.tsv
    role: source-submitted sample/path counts, not validated sample substrate identity
  - repository: culturebotai/HabitatMech
    path: data/raw/gold_studies.tsv
    role: study-to-source-path associations, not member-level substrate evidence
  - repository: culturebotai/HabitatMech
    path: scripts/extract_gold_biosamples.py
    role: reproducible source-path sample and study inventory extraction
checks:
- check_id: C1
  name: Target LinkML
  command: just validate data/habitats/engineered/produced_water__58649b5f.yaml
  status: passed
  required: true
  exit_code: 0
  summary: No issues found; unchanged corrected target.
  target_ids:
  - habitatmech:GOLD.bfd6bfa0f1
- check_id: C2
  name: Target strict schema
  command: just validate-strict data/habitats/engineered/produced_water__58649b5f.yaml
  status: passed
  required: true
  exit_code: 0
  summary: One file, zero errors.
  target_ids:
  - habitatmech:GOLD.bfd6bfa0f1
- check_id: C3
  name: Corpus reproduction
  command: just verify-corpus
  status: passed
  required: true
  exit_code: 0
  summary: 3208 expected/found, zero missing/extra/differing.
  target_ids:
  - habitatmech:GOLD.bfd6bfa0f1
- check_id: C4
  name: Regression and publication provenance
  command: uv run pytest -q tests/test_gold_parent_exclusions.py tests/test_produced_water_parent_curation.py
    tests/test_record_review_publication.py
  status: passed
  required: true
  exit_code: 0
  summary: 51 passed in 112.77s. New test separately passed in 9.86s.
  target_ids:
  - habitatmech:GOLD.bfd6bfa0f1
- check_id: C5
  name: History
  command: just validate-history
  status: passed
  required: true
  exit_code: 0
  summary: 233 history records valid.
  target_ids:
  - habitatmech:GOLD.bfd6bfa0f1
- check_id: C6
  name: Ontology labels
  command: just validate-products
  status: passed
  required: true
  exit_code: 0
  summary: 1178 canonical, 1 synonym, 5 accepted exceptions; 2057 no-adapter skips.
    No identity grounding added.
  target_ids:
  - habitatmech:GOLD.bfd6bfa0f1
- check_id: C7
  name: Authoritative exact-product CI
  command: gh run view 38019701934 --log
  status: passed
  required: true
  exit_code: 0
  summary: The same scripts/run_qc.py runner used by just qc completed successfully
    at 2026-10-10T03:22:45Z on 7faca5a8c6d6a140f1163f923baf314d2cce279a. 657 passed,
    3 skipped in 481.19s (0:08:01); all native gates passed. Run metadata independently
    confirms completed success.
  target_ids:
  - habitatmech:GOLD.bfd6bfa0f1
- check_id: C8
  name: Map input/cache/bundle verification
  command: uv run python scripts/embedding_pipeline.py check --output build/pr1845-map-download/data/text_map
    --input build/text-map/pr1845-inputs.jsonl --cache build/pr1845-map-download/build/text-map/vectors.sqlite
  status: passed
  required: true
  exit_code: 0
  summary: Full input identity, pinned encoder, checksums, complete map and cache
    passed. Separate cmp confirmed identical Linux/local inputs; finite-point check
    retained all 3208 records.
  target_ids:
  - habitatmech:GOLD.bfd6bfa0f1
- check_id: C9
  name: Generated site
  command: just render-check
  status: passed
  required: true
  exit_code: 0
  summary: 3208 habitat pages, 252 redirects, eight categories and 114 term requests
    match generated inputs.
  target_ids:
  - habitatmech:GOLD.bfd6bfa0f1
- check_id: C10
  name: Original reviews preserved
  command: uv run python scripts/record_review.py check
  status: passed
  required: true
  exit_code: 0
  summary: 94 native reviews passed before this successor; all 188 saved files separately
    byte-compared with 34b698602 and every one of the six initial captures matched
    its main-base input hashes.
  target_ids:
  - habitatmech:GOLD.bfd6bfa0f1
- check_id: C11
  name: Retained publication base
  command: git ls-remote --tags origin 'refs/tags/record-review-base/7faca5a8c6d6a140f1163f923baf314d2cce279a*'
  status: passed
  required: true
  exit_code: 0
  summary: Remote annotated provenance tag peels to the exact product/capture commit
    7faca5a8c6d6a140f1163f923baf314d2cce279a.
  target_ids:
  - habitatmech:GOLD.bfd6bfa0f1
- check_id: C12
  name: Local model environment
  command: uv run --locked --project conf/embedding-runtime python scripts/embedding_pipeline.py
    inspect --input build/text-map/pr1845-inputs.jsonl
  status: failed
  required: false
  exit_code: 2
  summary: 'Exited 2: pinned Torch has no macOS x86_64 wheel. The unchanged locked
    Linux workflow completed the required rebuild; downloaded products passed C8.
    No dependency guard was weakened.'
  target_ids:
  - habitatmech:GOLD.bfd6bfa0f1
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/engineered/produced_water__58649b5f.yaml
  locator: Full regenerated YAML and original-main comparison
  accessed_at: '2026-10-10T03:26:02Z'
  support: supports
  summary: Produced-water material is no longer asserted to be a subtype of an oil-reservoir
    landform. Only the guarded immediate GOLD source-parent contribution is excluded.
    The minted identity, node 7639, full petroleum-reservoir source path, one ORGANISM
    assertion, UNGROUNDED/CLASS/SEEDED state and all prior events are preserved. No
    new identity, genus, definition or biological claim is asserted.
- evidence_id: E2
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: Exact habitatmech:GOLD.bfd6bfa0f1 row and guarded path/parent
  accessed_at: '2026-10-10T03:26:02Z'
  support: supports
  summary: Suppresses ENVO:00002185 only for the petroleum-reservoir produced-water
    source. Other source paths, independent parents and all source inventory bytes
    are unchanged.
- evidence_id: E3
  kind: authority
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-22707
  locator: DSM 22707 PEH A isolation source, location and sampling date, reinspected
    in this publication session
  accessed_at: '2026-10-10T03:26:02Z'
  support: supports
  summary: The catalogue identifies the isolation material as petroleum-reservoir
    produced water from Kuparuk, Alaska, sampled 2008-01-24. This supports a sampled
    fluid, not a reservoir-landform identity; it does not reconstruct the original
    frozen GOLD roster.
- evidence_id: E4
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO:00002185
  locator: 'Current API response: label, complete definition and obsolete flag'
  accessed_at: '2026-10-10T03:26:02Z'
  support: supports
  summary: The active oil-reservoir term denotes a subsurface hydrocarbon-bearing
    landform. Source origin is not a broader class of the sampled water material.
- evidence_id: E5
  kind: prior_review
  reference: reviews/structured/20261010T024621Z-produced_water__58649b5f/review.yaml
  locator: Exact F1 and scoped source-membership limitations
  accessed_at: '2026-10-10T03:26:02Z'
  support: supports
  summary: Retains the original scientific observation and stable issue key. This
    successor resolves only the parent defect, not the original frozen membership
    or a candidate exact water grounding.
- evidence_id: E6
  kind: validation
  reference: tests/test_produced_water_parent_curation.py
  locator: Whole-corpus before/after document and semantic-text comparison
  accessed_at: '2026-10-10T03:26:02Z'
  support: supports
  summary: Only this record and its semantic text change. Every other claim and record
    is unchanged. The focused regression passed alone and with 50 exclusion/publication
    tests.
- evidence_id: E7
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38019701934
  locator: Successful exact-product CI; run metadata and complete-gate log inspected
  accessed_at: '2026-10-10T03:26:02Z'
  support: supports
  summary: The authoritative scripts/run_qc.py runner completed successfully on publication
    commit 7faca5a8c6d6a140f1163f923baf314d2cce279a at 2026-10-10T03:22:45Z. 657 passed,
    3 skipped in 481.19s (0:08:01); all native gates passed. This is verified CI execution,
    not a completed local full-QC claim.
- evidence_id: E8
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38019413965
  locator: Successful locked Linux rebuild, downloaded artifact and local input/cache/bundle
    verification
  accessed_at: '2026-10-10T03:26:02Z'
  support: supports
  summary: One changed-record vector encoded; repeated canary reused it; full embedding
    reused all 3208. Downloaded inputs byte-match local SHA256 f101d9a5c0ad2eed77c2aea5c533f42896d843c546c5eb53ae83547b26bca76f.
    All 3208 points are unique and finite, with none omitted. Encoder/projection settings
    unchanged.
- evidence_id: E9
  kind: record_content
  reference: history/mappings/produced_water__58649b5f/2026-10-10T030643Z-codex-gpt-5-88ca03.yaml
  locator: Complete append-only session record
  accessed_at: '2026-10-10T03:26:02Z'
  support: supports
  summary: 'Records the actual agent, issue #1848, supporting evidence, preserved
    claims and preflight checks. All 233 session-history records validate.'
assessments:
- assessment_id: A1
  area: grounding
  topic: Material versus landform
  outcome: supported
  summary: Produced-water material is no longer asserted to be a subtype of an oil-reservoir
    landform. Only the guarded immediate GOLD source-parent contribution is excluded.
    The minted identity, node 7639, full petroleum-reservoir source path, one ORGANISM
    assertion, UNGROUNDED/CLASS/SEEDED state and all prior events are preserved. No
    new identity, genus, definition or biological claim is asserted.
  target_ids:
  - habitatmech:GOLD.bfd6bfa0f1
  evidence_ids:
  - E1
  - E2
  - E3
  - E4
- assessment_id: A2
  area: provenance
  topic: Preserved claims and history
  outcome: supported
  summary: Exact source identifiers, path, one-ORGANISM unit/count, status and earlier
    events are unchanged. No parent taxa or other produced-water samples are inherited.
  target_ids:
  - habitatmech:GOLD.bfd6bfa0f1
  evidence_ids:
  - E1
  - E2
  - E5
  - E6
  - E9
- assessment_id: A3
  area: consistency
  topic: Generated products and gates
  outcome: supported
  summary: Corpus reproduction, complete map, pages, native QC and durable base provenance
    passed.
  target_ids:
  - habitatmech:GOLD.bfd6bfa0f1
  evidence_ids:
  - E6
  - E7
  - E8
findings:
- finding_id: F1
  issue_key: gold-bfd6bfa0f1-reservoir-context-parent
  severity: major
  certainty: confirmed
  category: grounding
  status: resolved
  title: Produced-water material is not a subtype of its reservoir landform
  description: Suppress only the exact source-path contribution of ENVO:00002185 through
    curation/gold_parent_exclusions.tsv. Preserve node 7639, the full source path,
    minted identity, one ORGANISM assertion and independent valid parents. Investigate
    any new material grounding separately with item-level evidence; do not merge produced-water
    siblings or transfer the reservoir parent's taxa.
  normalization_reason: The exact current isolate provenance and active ontology definition
    establish a material-versus-landform error in the sole strict parent, which materially
    changes graph meaning.
  native_severity: major
  rule_id: 'HabitatRecord checklist: strict broader parents, source scope, sampled
    material versus context and claim-level evidence; docs/CURATION.md'
  target_ids:
  - habitatmech:GOLD.bfd6bfa0f1
  field_paths:
  - parent_habitats
  evidence_ids:
  - E1
  - E2
  - E3
  - E4
  - E6
  - E7
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: guarded source-context parent exclusions
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: generated identity, parents, status and attestations
  previous_occurrences:
  - repository: culturebotai/HabitatMech
    review_id: 20261010T024621Z-produced_water__58649b5f
    finding_id: F1
  disposition_reason: Produced-water material is no longer asserted to be a subtype
    of an oil-reservoir landform. Only the guarded immediate GOLD source-parent contribution
    is excluded. The minted identity, node 7639, full petroleum-reservoir source path,
    one ORGANISM assertion, UNGROUNDED/CLASS/SEEDED state and all prior events are
    preserved. No new identity, genus, definition or biological claim is asserted.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1848
actions: []
limitations:
- Original frozen member identity and a source-authored definition remain unresolved
  as documented in the initial review. This successor does not claim a new exhaustive
  source census.
- No exact replacement ontology identity or new genus is established. Native status
  remains UNGROUNDED/SEEDED with the prior CLASS decision; resolving this hierarchy
  finding is not ITEM identity approval.
- 'Self-reviewed scoped correction, not independent approval, all-corpus scientific
  review, or SSSOM/KGX readiness. The four other findings remain open in #1846, #1847,
  #1849 and #1850. Three full-suite tests are skipped.'
- The duplicate local full-QC run is still in progress at this observation. Required
  full-gate evidence comes from inspected successful exact-product CI, not an assumed
  local result.
- Local model environment unavailable on macOS x86_64; validated locked Linux build
  used without changing dependency pins. Optional environment failure is preserved
  in C12.
related_reviews:
- repository: culturebotai/HabitatMech
  review_id: 20261010T024621Z-produced_water__58649b5f
  relationship: Explicitly resolves F1 while preserving the initial observation
links:
- https://github.com/CultureBotAI/HabitatMech/issues/1848
- https://github.com/CultureBotAI/HabitatMech/pull/1845
notes:
- The initial save was correctly rejected because HEAD advanced while generated products
  were committed. A new native inspection at the complete product commit verified
  all 59 captured input hashes unchanged. The target, correction, regression and product
  diff were reassessed without changing scientific claims. This new validated observation
  retains the actual original review start; no saved bundle was overwritten.
tags:
- habitatmech
- hierarchy
- followup
```
