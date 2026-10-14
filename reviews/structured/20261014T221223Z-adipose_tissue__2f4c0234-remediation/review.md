# Remediation review: Adipose tissue

- Review: 20261014T221223Z-adipose_tissue__2f4c0234-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-14T22:06:15Z
- Finished UTC: 2026-10-14T22:12:23Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

A guarded exclusion removes only the host-specific GOLD integumentary-system parent. The distinct native adipose identity, UBERON:0001013 tissue genus, NARROW/SEEDED state, verbatim source path/node IDs and count/unit omission or value are unchanged.

## Scope And Provenance

Focused remediation of exact prior findings after rereading the complete current target and its diff. Identity migrations also retain the former source-mapping target, not all uses of its ontology class.

Selection: Explicit successor to 20261014T214821Z-adipose_tissue__2f4c0234
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 0142b731d3f4d4e503fb16711eb8ba9ef7c06b6f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.7d70febb4c | data/habitats/host_associated/adipose_tissue__2f4c0234.yaml | generated | Adipose tissue |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native validate | passed | True | habitatmech:GOLD.7d70febb4c | Executed 2026-10-14T22:04:47Z to 2026-10-14T22:04:51Z. No issues found |
| Native validate-strict | passed | True | habitatmech:GOLD.7d70febb4c | Executed 2026-10-14T22:05:12Z to 2026-10-14T22:05:22Z. files scanned:      12<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| Native validate-history | passed | True | habitatmech:GOLD.7d70febb4c | Executed 2026-10-14T22:05:22Z to 2026-10-14T22:05:38Z. No issues found<br>718 history record(s) valid against src/habitatmech/schema/history.yaml |
| Native provenance-check | passed | True | habitatmech:GOLD.7d70febb4c | Executed 2026-10-14T22:05:38Z to 2026-10-14T22:05:39Z. provenance current: 14 committed inventories, 2 GOLD sources |
| Native verify-corpus | passed | True | habitatmech:GOLD.7d70febb4c | Executed 2026-10-14T22:05:39Z to 2026-10-14T22:06:16Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ |
| Native validate-causal-all | passed | True | habitatmech:GOLD.7d70febb4c | Executed 2026-10-14T22:06:16Z to 2026-10-14T22:06:31Z. validated 32 causal-graph curation file(s) with 32 graph(s) |
| Native term-requests-check | passed | True | habitatmech:GOLD.7d70febb4c | Executed 2026-10-14T22:06:31Z to 2026-10-14T22:07:38Z. term-request table is current (110 terms) |
| Native validate-products | passed | True | habitatmech:GOLD.7d70febb4c | Executed 2026-10-14T22:07:38Z to 2026-10-14T22:09:16Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond. |
| Focused regressions | passed | True | habitatmech:GOLD.7d70febb4c | Executed 2026-10-14T22:09:16Z to 2026-10-14T22:11:33Z. ........................................................................ [ 93%]<br>.....                                                                    [100%]<br>77 passed in 135.48s (0:02:15) |
| Repository lint | passed | True | habitatmech:GOLD.7d70febb4c | Executed 2026-10-14T22:11:33Z to 2026-10-14T22:11:34Z. All checks passed! |
| Branch-wide whitespace | passed | True | habitatmech:GOLD.7d70febb4c | Executed 2026-10-14T22:11:34Z to 2026-10-14T22:11:34Z. |
| Original source-member recovery | unavailable | False | habitatmech:GOLD.7d70febb4c | Original GOLD specimen joins and PREGO pair references remain unrecovered. The correction does not certify occurrence or prevalence. |
| Final publication gates | unavailable | False | habitatmech:GOLD.7d70febb4c | Final immutable archive, generated map/site and protected final-head QC remain mandatory before merge, not predeclared successful. |

## Scientific And Domain Assessments

### Maintained-input correction and preserved source scope

grounding: supported. Targets: habitatmech:GOLD.7d70febb4c.

A guarded exclusion removes only the host-specific GOLD integumentary-system parent. The distinct native adipose identity, UBERON:0001013 tissue genus, NARROW/SEEDED state, verbatim source path/node IDs and count/unit omission or value are unchanged.

### Native decision status and scientific uncertainty

consistency: supported. Targets: habitatmech:GOLD.7d70febb4c.

Native status is SEEDED/NARROW. Only adult gets a new ITEM review; adenoid replaces an existing ITEM mapping. Other source statuses remain unchanged. Source-member uncertainty is not certified by deterministic validation.

## Findings

### F1: Adipose tissue is not an integumentary system

major / resolved / confirmed; issue key: adipose_tissue__2f4c0234-source-context-parent.

Pre-fix observation: The source parent habitatmech:GOLD.968051b240 denotes the host-scoped integumentary system. Its position in the GOLD hierarchy gives anatomical context, not a strictly broader tissue genus.

Disposition: A guarded exclusion removes only the host-specific GOLD integumentary-system parent. The distinct native adipose identity, UBERON:0001013 tissue genus, NARROW/SEEDED state, verbatim source path/node IDs and count/unit omission or value are unchanged.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| PREVIOUS | reviews/structured/20261014T214821Z-adipose_tissue__2f4c0234/review.yaml | supports | Immutable pre-fix claim-specific primary evidence and access limits; same-agent predecessor, not independent approval. |
| PATCH | curation/decisions.tsv; curation/gold_parent_exclusions.tsv; curation/term_requests.tsv; curation/definition_source_label_exclusions.tsv; data/habitats/host_associated/adipose_tissue__2f4c0234.yaml | supports | A guarded exclusion removes only the host-specific GOLD integumentary-system parent. The distinct native adipose identity, UBERON:0001013 tissue genus, NARROW/SEEDED state, verbatim source path/node IDs and count/unit omission or value are unchanged. Current parents: ['UBERON:0001013']. |
| TESTS | tests/test_adipose_and_stage_repairs.py | supports | Full-corpus counterfactual reconstructs former inputs and proves exactly seven changed source records, preserved unrelated claims, two precise identity replacements, six parent-contribution exclusions and unchanged source counts/taxa. Adenoma remains unchanged. |

## Limits And Additional Notes

- Same-agent remediation assessment, not independent approval.
- Original source-member and PREGO pair-level references remain unavailable; no whole-corpus or SSSOM/KGX readiness certification.
- Final archive, map/site and protected publication QC are pending at this immutable observation.
- Fresh native inspection after committing the maintained fixes; captured inputs checked against the declared Git tree.
- Original saved history/reviews and raw ontology inventories remain unchanged.
- Development regression run initially had 1 failed and 76 passed: the new test fixture reversed the human and mammalian adrenal source-mint expectations. Native seed.mint confirmed the actual source keys; the curation rows were already correct. The fixture was corrected and the focused counterfactual then passed (1 passed in 9.79s), followed by the full recorded regression rerun.
- An initial diff-whitespace check reported trailing empty TSV columns on the updated adenoid decision. Making its default parent relation explicit removed the whitespace without changing mapping behavior; the final diff check is recorded separately.
- Preserve this off-main input base with an annotated provenance tag before squash and branch deletion.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T221223Z-adipose_tissue__2f4c0234-remediation
kind: record
repository: CultureBotAI/HabitatMech
title: 'Remediation review: Adipose tissue'
started_at: '2026-10-14T22:06:15Z'
finished_at: '2026-10-14T22:12:23Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same-agent scientific assessment and later adversarial pass,
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
scientific_review: true
verdict: pass_with_limitations
summary: A guarded exclusion removes only the host-specific GOLD integumentary-system
  parent. The distinct native adipose identity, UBERON:0001013 tissue genus, NARROW/SEEDED
  state, verbatim source path/node IDs and count/unit omission or value are unchanged.
source:
  git_revision: 0142b731d3f4d4e503fb16711eb8ba9ef7c06b6f
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
  - path: conf/id_label_targets.yaml
    sha256: e100d84aabccaeb00c1a60246142b3cafcec009dbfba58f5cc319c35adddb633
    role: context
  - path: conf/record_review.yaml
    sha256: c2f5d0eb4c5744f5fe354c92184ddab144dc2688dba952b032b4f3d597bc08d6
    role: context
  - path: curation/decisions.tsv
    sha256: 3072cbab4fc5f9241e595a681b0f9095ae0942c9dba6502fb01afc52fe67d919
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 505e6efc536392c9f6ce77fd4a70284392166269713189ff53e40367256d2899
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 77240ee178c7374a1d872a4226cd7c05916097b9b1d78679ae921666feead297
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: 11f153cc7f19333dc89a9019ef59c33b210bbebb44dd4e84b11166be3dd3927f
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: 8d4ce33422cf749d02b43d734fdcbefeb5dd04b79ef8574cc361548a112da0b8
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: b0135af0aa4deed0f3824a2f491d5a742c1b7de4775c533f283761d22e805821
    role: context
  - path: data/habitats/host_associated/acute_lymphoblastic_leukemia_cell.yaml
    sha256: 00aa44197c12be59d28acd8d9006d0c468f36e8b7dec42595326d2dabf017d81
    role: context
  - path: data/habitats/host_associated/adenoid.yaml
    sha256: e0c16df46b4d76579a50d8e1683490f5106d6e2bd9f8f4f0603156cff3439656
    role: context
  - path: data/habitats/host_associated/adenoma.yaml
    sha256: 3cf9c9c96c98f6a5db085bd3a9e265900e81c0d1f7dafd7e19af8e90c9f5cda1
    role: context
  - path: data/habitats/host_associated/adipose_tissue.yaml
    sha256: 864bdf2a2f2a5a1e99716a7ea9c354a0d2cec4833c183458f526f54ed313329e
    role: context
  - path: data/habitats/host_associated/adipose_tissue__28f7c202.yaml
    sha256: d0b81f121493473d19c8773313fb18981a58c977d8d72036960afccb6b87e437
    role: context
  - path: data/habitats/host_associated/adipose_tissue__2f4c0234.yaml
    sha256: cbc20999a6b69b3922add4d2cfa56ef51c6fdd0b04ec6e0cf4af39806c0a80da
    role: target
  - path: data/habitats/host_associated/adipose_tissue__3dd3b646.yaml
    sha256: 39390ddb0de7165207737e509b101baab763d7e91fda333c6bb56260cb6e4e8d
    role: context
  - path: data/habitats/host_associated/adipose_tissue__9969df64.yaml
    sha256: 57eee21dc1fa3c08e87f51beda1fb01150d69713f4c5fb84b7493a8372f1cf0f
    role: context
  - path: data/habitats/host_associated/adrenal_gland.yaml
    sha256: 7180a6d479ca9862d7d659f09d73c72f4c6da6b264911d258fb14e39f7e9457d
    role: context
  - path: data/habitats/host_associated/adult.yaml
    sha256: 91c41fc8a4d72c43682756d0e29562fbf92e27e198d386fc5847a6c8961e4e04
    role: context
  - path: data/habitats/host_associated/aerial_part.yaml
    sha256: eb7b4c5a03c7b5c5c5f0af47e97a50cf4f0a185affb57f30aee21c6432c3c71a
    role: context
  - path: data/habitats/host_associated/aerial_root.yaml
    sha256: 6a5f29f9b0077c138c2021f72060b6b1cf8e7462c4071c36cdf697b9dca86978
    role: context
  - path: data/habitats/host_associated/benign_tumor.yaml
    sha256: 3e0b774986a5090329828796dfdc55d7405135ecbc27ff8c9c638cf47863d63e
    role: context
  - path: data/habitats/host_associated/connective_tissue.yaml
    sha256: a9bdb03f9861db9efde176fa4d7eaa4daedce57096e99bf6064de8ce62b556e9
    role: context
  - path: data/habitats/host_associated/endocrine_gland.yaml
    sha256: 7bad2c064b51f831c15818a6c641d7db5984605f2d54d6553ce737a824081dcc
    role: context
  - path: data/habitats/host_associated/endocrine_gland__8c35903c.yaml
    sha256: 514315aea57ac6555d13e02dac2548b4f829f1b060d347f65f372fde8a7eb9f5
    role: context
  - path: data/habitats/host_associated/integumentary_system__2442c03e.yaml
    sha256: 6b9641cba433804d7f4535dda313f84aefd1805f7f36a79c71e0e93dabd78afc
    role: context
  - path: data/habitats/host_associated/integumentary_system__489a751e.yaml
    sha256: ca8dd250782441d72f1bc981dd1e9402553363456897b21c7cbbd2133b50ed8a
    role: context
  - path: data/habitats/host_associated/integumentary_system__bd82bc93.yaml
    sha256: 4e26a3fb52d1b0aab9ddecc1c357935e2394b6a2af1764f67afc244ddd824be5
    role: context
  - path: data/habitats/host_associated/integumentary_system__e212bc7d.yaml
    sha256: 17169f5334109254c2d5f87a04cadfe86f0a74ded9dceac8d608e0cdf2abf93e
    role: context
  - path: data/habitats/host_associated/lymphoid_tissue.yaml
    sha256: 4fe04531289bdcca53a59810a84bfbc3308297b75b1cc1a2eb87aedac523dd64
    role: context
  - path: data/habitats/host_associated/root.yaml
    sha256: bff8dbd6b887c04f59cf573e8a201cd30f49bc2c51e6e92d5fb72747cc55df25
    role: context
  - path: data/habitats/host_associated/root__722ce44f.yaml
    sha256: eed2322864dbb77748a875551a9c8b42a7db2ffd35e246c9e4fa5f586ff736e5
    role: context
  - path: data/habitats/host_associated/tonsil.yaml
    sha256: a7b94d7d9e01995eb25e5e17f05d89516e2637ce750da05bf58e39232e2d6b8e
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
  - path: docs/CURATION.md
    sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
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
  - path: history/mappings/adipose_tissue__2f4c0234/2026-10-14T220115Z-codex-gpt-5-f23276.yaml
    sha256: 015334c7ec35589b3660fa24540e59b8b6ed43bcf9159cfc914689b270169cd5
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260923T051638Z-acute_lymphoblastic_leukemia_cell.md
    sha256: 8a9e0d858e0d17a6bd0b0f4f4de9c6252683bf6391d8556960136cead84fa5e0
    role: context
  - path: reports/yaml_record_review/20260923T053455Z-adenoid.md
    sha256: 792e800776371c11f981e4f5d33342c542413ba86d6bdf3bdff72d2c68dac8a4
    role: context
  - path: reports/yaml_record_review/20260923T055611Z-adenoma.md
    sha256: 6b2d1f1081e5b790771803b6495c608eccce79a899c2a9a29bc1153e1c17c6a9
    role: context
  - path: reports/yaml_record_review/20260923T061621Z-adipose_tissue.md
    sha256: cb87ecd387e6d053e5fca96e902cdf2cdb9c457d82fd438dfcbdac75361521a3
    role: context
  - path: reports/yaml_record_review/20260923T063701Z-adipose_tissue__28f7c202.md
    sha256: 9dc2e8e0a07eeb052eacb37502451fa14cf80b72ec58270e8bf21c4a374836c0
    role: context
  - path: reports/yaml_record_review/20260923T065349Z-adipose_tissue__2f4c0234.md
    sha256: 0da01abaa79b7812f2acfdcaa4150561a3174b70e8fc35d228b7198d490ca7e1
    role: context
  - path: reports/yaml_record_review/20260923T154927Z-adipose_tissue__3dd3b646.md
    sha256: b83483ed390e3e1f87f7bdb76388e516d99cb0f1a235eb58462eb43bd036c51a
    role: context
  - path: reports/yaml_record_review/20260923T161138Z-adipose_tissue__9969df64.md
    sha256: 482bb8e1957f09645964a094b3751692c630ecfb7c4f50919cd943841020d51b
    role: context
  - path: reports/yaml_record_review/20260923T163309Z-adrenal_gland.md
    sha256: be09f641d0cd6d2787e50fc93ff9f628df60e10ba960b892b4d8fbd63b52e69d
    role: context
  - path: reports/yaml_record_review/20260923T165051Z-adult.md
    sha256: 73ec6bd6dbea8969afce52b8ad941dced86297d4698340af6c7f3ceac45a5033
    role: context
  - path: reports/yaml_record_review/20260923T170759Z-aerial_part.md
    sha256: eab52834eb277777c15176f2b65ed71cb919167054bbc624c0a0df2f422e24b8
    role: context
  - path: reports/yaml_record_review/20260923T172735Z-aerial_root.md
    sha256: 9eb877777b9cfd926036011d637b1b857a83ed98196f97819d575215ef317324
    role: context
  - path: reviews/structured/20261014T214821Z-adipose_tissue__2f4c0234/review.md
    sha256: b842dd0c16908692fe14cf7a2f62b2fd9995a94c15b18ddbfb65742fbf099678
    role: context
  - path: reviews/structured/20261014T214821Z-adipose_tissue__2f4c0234/review.yaml
    sha256: 9d7b237f33ecfd77308dc4d6e9fed5b5c4a56c7c5c7ecc78d4d8c959fab2e1fc
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/habitatmech/curate/decisions.py
    sha256: f33d3e9dc95bb428e63e640d48d4074cf15e90ea666603fb16fb651d591e3f02
    role: context
  - path: src/habitatmech/curate/definitions.py
    sha256: decd02eea029e884ab1a8bbb51dd870edb5544906b3ddd39598147b27ce572c9
    role: context
  - path: src/habitatmech/curate/external_xrefs.py
    sha256: 8b90ec049887d3aa67e31cce7f7a04d7300421c6fedb833cc66e5d5f5f181694
    role: context
  - path: src/habitatmech/curate/gold_parent_exclusions.py
    sha256: 044d8277509a9b1f6e4f2d7ea1fb82319b41e09ffef7788738a0f4ed0d0b63af
    role: context
  - path: src/habitatmech/curate/record_annotation_corrections.py
    sha256: 15bad3d40fd95e2acc72d3ff3c74289c15fb8a1775adc523b3575c3ea8487033
    role: context
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
    role: context
  - path: src/habitatmech/seed.py
    sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
    role: context
  - path: tests/test_adipose_and_stage_repairs.py
    sha256: 288a8ceb703685d59b3ab369327cdfc4d5101354fb679c5a9b1286998616a8cd
    role: context
targets:
- target_id: habitatmech:GOLD.7d70febb4c
  path: data/habitats/host_associated/adipose_tissue__2f4c0234.yaml
  label: Adipose tissue
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/external_xrefs.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/redirects_retracted.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests_excluded.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/bacdive_isolation_sources.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/bacdive_source_taxa.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/environment_parameters.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_path_biosamples.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_path_triads.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_studies.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/isolation_source_groundings.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/madin_habitat_taxa.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/madin_habitats.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_subclass_edges.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitat_taxa.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitats.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained source, curation input, or generator; target YAML is read-only
scope:
  description: Focused remediation of exact prior findings after rereading the complete
    current target and its diff. Identity migrations also retain the former source-mapping
    target, not all uses of its ontology class.
  selection: Explicit successor to 20261014T214821Z-adipose_tissue__2f4c0234
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.7d70febb4c
checks:
- check_id: FIX5
  name: Native validate
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/adipose_tissue__2f4c0234.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.7d70febb4c
  summary: Executed 2026-10-14T22:04:47Z to 2026-10-14T22:04:51Z. No issues found
  scope_note: Schema exact target; strict twelve; focused regressions and documented
    full-corpus gates. Final publication/archive QC is separate.
- check_id: FIX12
  name: Native validate-strict
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/acute_lymphoblastic_leukemia_cell.yaml data/habitats/host_associated/adenoid.yaml
    data/habitats/host_associated/adenoma.yaml data/habitats/host_associated/adipose_tissue.yaml
    data/habitats/host_associated/adipose_tissue__28f7c202.yaml data/habitats/host_associated/adipose_tissue__2f4c0234.yaml
    data/habitats/host_associated/adipose_tissue__3dd3b646.yaml data/habitats/host_associated/adipose_tissue__9969df64.yaml
    data/habitats/host_associated/adrenal_gland.yaml data/habitats/host_associated/adult.yaml
    data/habitats/host_associated/aerial_part.yaml data/habitats/host_associated/aerial_root.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.7d70febb4c
  summary: "Executed 2026-10-14T22:05:12Z to 2026-10-14T22:05:22Z. files scanned:\
    \      12\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:          \
    \      reports/instance_validation_failures.tsv"
  scope_note: Schema exact target; strict twelve; focused regressions and documented
    full-corpus gates. Final publication/archive QC is separate.
- check_id: FIX13
  name: Native validate-history
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.7d70febb4c
  summary: 'Executed 2026-10-14T22:05:22Z to 2026-10-14T22:05:38Z. No issues found

    718 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Schema exact target; strict twelve; focused regressions and documented
    full-corpus gates. Final publication/archive QC is separate.
- check_id: FIX14
  name: Native provenance-check
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.7d70febb4c
  summary: 'Executed 2026-10-14T22:05:38Z to 2026-10-14T22:05:39Z. provenance current:
    14 committed inventories, 2 GOLD sources'
  scope_note: Schema exact target; strict twelve; focused regressions and documented
    full-corpus gates. Final publication/archive QC is separate.
- check_id: FIX15
  name: Native verify-corpus
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.7d70febb4c
  summary: "Executed 2026-10-14T22:05:39Z to 2026-10-14T22:06:16Z. expected 3208 records,\
    \ found 3208 on disk\n  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus\
    \ reproduces exactly from data/raw/"
  scope_note: Schema exact target; strict twelve; focused regressions and documented
    full-corpus gates. Final publication/archive QC is separate.
- check_id: FIX16
  name: Native validate-causal-all
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.7d70febb4c
  summary: Executed 2026-10-14T22:06:16Z to 2026-10-14T22:06:31Z. validated 32 causal-graph
    curation file(s) with 32 graph(s)
  scope_note: Schema exact target; strict twelve; focused regressions and documented
    full-corpus gates. Final publication/archive QC is separate.
- check_id: FIX17
  name: Native term-requests-check
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.7d70febb4c
  summary: Executed 2026-10-14T22:06:31Z to 2026-10-14T22:07:38Z. term-request table
    is current (110 terms)
  scope_note: Schema exact target; strict twelve; focused regressions and documented
    full-corpus gates. Final publication/archive QC is separate.
- check_id: FIX18
  name: Native validate-products
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.7d70febb4c
  summary: "Executed 2026-10-14T22:07:38Z to 2026-10-14T22:09:16Z. id↔label correspondence\
    \ summary:\n          OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n        \
    \  OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond."
  scope_note: Schema exact target; strict twelve; focused regressions and documented
    full-corpus gates. Final publication/archive QC is separate.
- check_id: FIX19
  name: Focused regressions
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_adipose_and_stage_repairs.py tests/test_gold_parent_exclusions.py
    tests/test_definition_source_label_exclusions.py
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.7d70febb4c
  summary: 'Executed 2026-10-14T22:09:16Z to 2026-10-14T22:11:33Z. ........................................................................
    [ 93%]

    .....                                                                    [100%]

    77 passed in 135.48s (0:02:15)'
  scope_note: Schema exact target; strict twelve; focused regressions and documented
    full-corpus gates. Final publication/archive QC is separate.
- check_id: FIX20
  name: Repository lint
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m ruff check .
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.7d70febb4c
  summary: Executed 2026-10-14T22:11:33Z to 2026-10-14T22:11:34Z. All checks passed!
  scope_note: Schema exact target; strict twelve; focused regressions and documented
    full-corpus gates. Final publication/archive QC is separate.
- check_id: FIX21
  name: Branch-wide whitespace
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache git diff --check 22120cf5ce86a96fbd23524bfcd7a00ed08b3106
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.7d70febb4c
  summary: Executed 2026-10-14T22:11:34Z to 2026-10-14T22:11:34Z.
  scope_note: Schema exact target; strict twelve; focused regressions and documented
    full-corpus gates. Final publication/archive QC is separate.
- check_id: MEMBERS
  name: Original source-member recovery
  required: false
  status: unavailable
  target_ids:
  - habitatmech:GOLD.7d70febb4c
  summary: Original GOLD specimen joins and PREGO pair references remain unrecovered.
    The correction does not certify occurrence or prevalence.
- check_id: PUBLICATION
  name: Final publication gates
  required: false
  status: unavailable
  target_ids:
  - habitatmech:GOLD.7d70febb4c
  summary: Final immutable archive, generated map/site and protected final-head QC
    remain mandatory before merge, not predeclared successful.
evidence:
- evidence_id: PREVIOUS
  kind: prior_review
  reference: reviews/structured/20261014T214821Z-adipose_tissue__2f4c0234/review.yaml
  summary: Immutable pre-fix claim-specific primary evidence and access limits; same-agent
    predecessor, not independent approval.
  accessed_at: '2026-10-14T22:12:23Z'
  support: supports
- evidence_id: PATCH
  kind: record_content
  reference: curation/decisions.tsv; curation/gold_parent_exclusions.tsv; curation/term_requests.tsv;
    curation/definition_source_label_exclusions.tsv; data/habitats/host_associated/adipose_tissue__2f4c0234.yaml
  summary: 'A guarded exclusion removes only the host-specific GOLD integumentary-system
    parent. The distinct native adipose identity, UBERON:0001013 tissue genus, NARROW/SEEDED
    state, verbatim source path/node IDs and count/unit omission or value are unchanged.
    Current parents: [''UBERON:0001013''].'
  accessed_at: '2026-10-14T22:12:23Z'
  support: supports
- evidence_id: TESTS
  kind: validation
  reference: tests/test_adipose_and_stage_repairs.py
  summary: Full-corpus counterfactual reconstructs former inputs and proves exactly
    seven changed source records, preserved unrelated claims, two precise identity
    replacements, six parent-contribution exclusions and unchanged source counts/taxa.
    Adenoma remains unchanged.
  accessed_at: '2026-10-14T22:12:23Z'
  support: supports
assessments:
- assessment_id: REPAIR
  area: grounding
  topic: Maintained-input correction and preserved source scope
  outcome: supported
  target_ids:
  - habitatmech:GOLD.7d70febb4c
  evidence_ids:
  - PREVIOUS
  - PATCH
  - TESTS
  summary: A guarded exclusion removes only the host-specific GOLD integumentary-system
    parent. The distinct native adipose identity, UBERON:0001013 tissue genus, NARROW/SEEDED
    state, verbatim source path/node IDs and count/unit omission or value are unchanged.
- assessment_id: STATUS
  area: consistency
  topic: Native decision status and scientific uncertainty
  outcome: supported
  target_ids:
  - habitatmech:GOLD.7d70febb4c
  evidence_ids:
  - PREVIOUS
  - PATCH
  summary: Native status is SEEDED/NARROW. Only adult gets a new ITEM review; adenoid
    replaces an existing ITEM mapping. Other source statuses remain unchanged. Source-member
    uncertainty is not certified by deterministic validation.
  dimensions:
  - name: mapping_status
    value: SEEDED
    definition: Native generated status, independent of review verdict
    evidence_ids:
    - PATCH
  - name: grounding_status
    value: NARROW
    definition: Native generated status, independent of review verdict
    evidence_ids:
    - PATCH
findings:
- finding_id: F1
  issue_key: adipose_tissue__2f4c0234-source-context-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Adipose tissue is not an integumentary system
  description: 'Pre-fix observation: The source parent habitatmech:GOLD.968051b240
    denotes the host-scoped integumentary system. Its position in the GOLD hierarchy
    gives anatomical context, not a strictly broader tissue genus.'
  target_ids:
  - habitatmech:GOLD.7d70febb4c
  field_paths:
  - parent_habitats
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  evidence_ids:
  - PREVIOUS
  - PATCH
  - TESTS
  rule_id: HM-IDENTITY-STRICT-GENUS-SOURCE-SCOPE
  native_severity: major
  normalization_reason: Materially unsupported scope, hierarchy or source disposition
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261014T214821Z-adipose_tissue__2f4c0234
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2137
  disposition_reason: A guarded exclusion removes only the host-specific GOLD integumentary-system
    parent. The distinct native adipose identity, UBERON:0001013 tissue genus, NARROW/SEEDED
    state, verbatim source path/node IDs and count/unit omission or value are unchanged.
actions: []
limitations:
- Same-agent remediation assessment, not independent approval.
- Original source-member and PREGO pair-level references remain unavailable; no whole-corpus
  or SSSOM/KGX readiness certification.
- Final archive, map/site and protected publication QC are pending at this immutable
  observation.
notes:
- Fresh native inspection after committing the maintained fixes; captured inputs checked
  against the declared Git tree.
- Original saved history/reviews and raw ontology inventories remain unchanged.
- 'Development regression run initially had 1 failed and 76 passed: the new test fixture
  reversed the human and mammalian adrenal source-mint expectations. Native seed.mint
  confirmed the actual source keys; the curation rows were already correct. The fixture
  was corrected and the focused counterfactual then passed (1 passed in 9.79s), followed
  by the full recorded regression rerun.'
- An initial diff-whitespace check reported trailing empty TSV columns on the updated
  adenoid decision. Making its default parent relation explicit removed the whitespace
  without changing mapping behavior; the final diff check is recorded separately.
- Preserve this off-main input base with an annotated provenance tag before squash
  and branch deletion.
tags:
- habitatmech
- record-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261014T214821Z-adipose_tissue__2f4c0234
  relationship: Exact remediation successor retaining all predecessor finding targets
```
