# Mixed liquor (MBR): resolved source-context hierarchy finding

- Review: 20261009T154958Z-mixed-liquor-mbr-resolved
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-09T15:29:42Z
- Finished UTC: 2026-10-09T15:49:58Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

At retained commit 7ac0db3290acfb634b501ba38e7362ff2b3bf10c, the confirmed false parent is corrected through a guarded exclusion. The complete historical generated record is rechecked and every captured input is byte-identical to current product commit 564b79a8360155f6d98ca1eefe3c1f8f565fafa4. This successor resolves only F1; original scientific claims, seeded status and remaining evidence limits are preserved.

## Scope And Provenance

Historical full-record assessment of the correction committed at 7ac0db3290acfb634b501ba38e7362ff2b3bf10c, with a scoped F1 disposition. Both complete target blobs were re-read there; all 44 captured hashes match that retained commit and the current product tree. External evidence is retained from the original observation, not newly collected.

Selection: Exact original target ID/path; inspect captured the post-fix inputs before this assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 7ac0db3290acfb634b501ba38e7362ff2b3bf10c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.904cce6b84 | data/habitats/engineered/mixed_liquor.yaml | generated | Mixed liquor (MBR) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Schema | passed | True | habitatmech:GOLD.904cce6b84 | No issues found. |
| Closed schema | passed | True | habitatmech:GOLD.904cce6b84 | Two exact files, zero errors. |
| Corpus | passed | True | habitatmech:GOLD.904cce6b84 | 3208 expected/present, zero missing, extra or differing. |
| History | passed | True | habitatmech:GOLD.904cce6b84 | 222 histories valid. |
| Isolation and guarded exclusions | passed | True | habitatmech:GOLD.904cce6b84 | 49 passed in 69.29 seconds. |
| Render | passed | True | habitatmech:GOLD.904cce6b84 | 3208 habitat pages, 252 redirects, eight categories and 114 term requests rendered after a verified map refresh. |
| Map source/vector validation | passed | True | habitatmech:GOLD.904cce6b84 | Full local input identity and cache vectors match the generated 3208-point bundle. |
| Publication provenance | passed | True | habitatmech:GOLD.904cce6b84 | Two passed in 12.13 seconds. Exact off-main base retained under an annotated tag and verified peeled on origin. |
| Ontology labels | passed | True | habitatmech:GOLD.904cce6b84 | Success on exact product commit; no identity or label changes. |
| Full local quality gate | passed | True | habitatmech:GOLD.904cce6b84 | All HabitatMech quality gates passed; 647 tests passed, three skipped in 632.57 seconds. This is the completed rerun after map regeneration, not the interrupted earlier run. |
| Full CI quality gate | passed | True | habitatmech:GOLD.904cce6b84 | Completed success on product commit 564b79a8360155f6d98ca1eefe3c1f8f565fafa4; actual gate log inspected. |

## Scientific And Domain Assessments

### Retained qualified identity and source units

identity: supported. Targets: habitatmech:GOLD.904cce6b84.

Mint, full GOLD path, distinct same-label identity and collapsed source-node note remain supported by the original scientific review. Zero frozen counters still omit count/unit; separate biosamples are not organisms or independent environmental replicates.

### Corrected context-only parent

graph: supported. Targets: habitatmech:GOLD.904cce6b84.

The exact material-to-equipment/facility relation is gone. No unsupported replacement relation is asserted, and whole-corpus comparison proves the parent record and all other records remain unchanged.

### Grounding and lifecycle restraint

grounding: supported. Targets: habitatmech:GOLD.904cce6b84.

UNGROUNDED/SEEDED and the prior CLASS decision remain appropriate to their provenance. Hierarchy review is not a new ITEM identity judgment or a basis for REVIEWED promotion.

### Definition, parameters, taxa, mechanisms, discussion and datasets

completeness: supported. Targets: habitatmech:GOLD.904cce6b84.

All original optional-field absences and evidence limits are preserved. No parent taxa, source study conditions, SIP metrics, recipe or causal claim are imported. Neither material genus nor sibling equivalence is forced.

### Maintained-input and generated-product consistency

ownership: supported. Targets: habitatmech:GOLD.904cce6b84.

The exclusion table owns the correction; native canary writes and page generation produce the outputs. Append-only history and review lineage are retained. No raw source, seeder or ontology label change is needed.

### Expression-module applicability

evidence: not_applicable. Targets: habitatmech:GOLD.904cce6b84.

No gene/regulator/protein or named transcriptomics dataset claim requires iModulonDB; its absence is not negative evidence.

### Complete native verification

schema: supported. Targets: habitatmech:GOLD.904cce6b84.

Both target schemas, full corpus reproduction, full local QC, exact product-commit CI and ontology labels pass. Map and page changes are required consequences of the two removed parent labels, not new biological claims.

## Findings

### F1: Mixed-liquor material is not a type of its containing equipment or facility

major / resolved / confirmed; issue key: mixed-liquor-mbr-material-to-apparatus-parent.

The exact source-parent contribution ENVO:03600010 has been excluded. This resolves only the original material-to-apparatus/facility subsumption defect. No identity merge, substitute genus, new ecological condition or ITEM status follows.

Disposition: Source semantics establish the material/equipment distinction; the guarded maintained row and regenerated output implement the bounded correction. Whole-corpus differential testing confirms that unrelated claims and records remain intact.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/engineered/mixed_liquor.yaml; Complete regenerated record and diff from 14d99404e9da3170d3d099aedc2855d4e8c4081e | supports | The unsupported sole parent ENVO:03600010 is removed. Identity, label, category, source attestation including path and 2-node note, count/unit/predicate omissions, UNGROUNDED/SEEDED and both prior events are unchanged. One deterministic SOURCE_PARENT_EXCLUDED event is appended; no replacement parent or definition is asserted. |
| E2 | curation/gold_parent_exclusions.tsv; habitatmech:GOLD.904cce6b84; Engineered &gt; Bioreactor &gt; MBR (Membrane bioreactor) &gt; Mixed liquor; expected parent ENVO:03600010 | supports | The exact source-concept/path/parent row records codex-gpt-5, 2026-10-09, primary-source rationale and issue #1800. This excludes only the immediate GOLD contribution; the parent record and unrelated sources are unchanged. |
| E3 | reviews/structured/20261009T152149Z-mixed-liquor-mbr/review.yaml; Complete original observation; F1 and E1-E14 | supports | Retains the one-record scientific review, exact GOLD crosswalk and NCBI inspection, current ontology verification, EPA material-versus-equipment distinction, original access limits, and stable finding key. This successor rechecks the implemented relationship correction; it does not pretend to repeat every external request or close unrelated identity questions. |
| E4 | tests/test_mixed_liquor_parents.py; Whole-corpus differential regression | supports | With and without these two exclusions, all 3208 concept IDs remain identical and only the two intended records differ. The regression asserts only parent removal and one audit event, unchanged remaining fields, retained mint/path/node notes, status and count/unit/predicate omissions. Together with shared exclusion tests, 49 cases pass. |
| E5 | history/mappings/mixed_liquor/2026-10-09T152516Z-codex-gpt-5-71c5fe.yaml; Full session provenance | supports | Append-only session record attributes this hierarchy-only edit to codex-gpt-5/gpt-5/codex and issue #1800. Its details honestly distinguish checks underway at creation from later completed results. Both new histories and all 222 total histories validate. |
| E6 | https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=9100NX8X.txt; Section III Definitions, as inspected in original observation | supports | Inspected EPA terminology distinguishes mixed-liquor material from the treatment equipment containing it. It supports removing the false is-a relation, not a universal treatment condition or exact sludge identity. |
| E7 | https://github.com/CultureBotAI/HabitatMech/actions/runs/37952082716; Build head 7ac0db3290acfb634b501ba38e7362ff2b3bf10c; canary and full receipts | supports | Real pinned Linux BGE/PaCMAP build encoded two changed records, reused both on repeat, validated a 32-record projection canary, reused all 3208 vectors on the full pass and generated all 3208 finite points. Local full-input/vector verification passes. Only these two records' parent-label text changed; the temporary workflow is removed. |
| E8 | https://github.com/CultureBotAI/HabitatMech/actions/runs/37952670267; Head 564b79a8360155f6d98ca1eefe3c1f8f565fafa4 | supports | Required ontology-label workflow completed successfully on the product commit. No identity/label was changed by the hierarchy correction. |
| E9 | https://github.com/CultureBotAI/HabitatMech/actions/runs/37952670630; Product commit 564b79a8360155f6d98ca1eefe3c1f8f565fafa4; full gate logs | supports | CI passes all native gates, with 647 tests passed and three skipped (424.54 seconds). Fresh local just qc also exits zero: 647 passed/three skipped (632.57 seconds), 222 histories, 3208 closed-schema/exact records, 32 overlays, curation floor, current site, redirects and term requests. No scientific input changed after the captured correction. |

## Limits And Additional Notes

- This is a same-agent follow-up, not independent approval. Source identity remains CLASS/SEEDED, without a newly authored definition or established exact ontology match.
- The original external-source bounds remain: the current GOLD workbook is not the frozen August source, and matched counts do not prove historical membership. No live-count refresh or source classification rewrite is performed.
- GOLD supplies MBR context; the three exact NCBI submissions have sparse location/isolation fields and distinct HS50/HS5/HS0 titles. No treatment or sampling-condition equivalence is inferred.
- Local render initially failed as intended on stale map inputs; full QC was stopped during tests before rebuilding (exit130), not reported as a pass. The pinned torch runtime has no Intel macOS wheel; actual model inference/projection ran in the established temporary Linux workflow, then artifacts were validated locally.
- No corpus-wide scientific completion, SSSOM/KGX readiness, sibling merge or novel-term approval is implied.
- HEAD advanced for product-only changes after the original inspect. Rather than recapture or replace hashes, this observation explicitly reviews the committed correction at its original 7ac0db3290acfb634b501ba38e7362ff2b3bf10c base (source.state git_commit). Fresh historical blob hashing verified all 44 original input digests and exact equality to the current tree; full target blobs were re-read. The exact annotated record-review-base tag is verified on origin.
- The prior immutable finding is resolved only by this explicit linked observation. The GitHub issue closes on merge, not merely on saving this review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261009T154958Z-mixed-liquor-mbr-resolved
kind: record
repository: CultureBotAI/HabitatMech
title: 'Mixed liquor (MBR): resolved source-context hierarchy finding'
started_at: '2026-10-09T15:29:42Z'
finished_at: '2026-10-09T15:49:58Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent continuing the corpus review and authorized publication;
    not independent scientific approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: At retained commit 7ac0db3290acfb634b501ba38e7362ff2b3bf10c, the confirmed
  false parent is corrected through a guarded exclusion. The complete historical generated
  record is rechecked and every captured input is byte-identical to current product
  commit 564b79a8360155f6d98ca1eefe3c1f8f565fafa4. This successor resolves only F1;
  original scientific claims, seeded status and remaining evidence limits are preserved.
source:
  git_revision: 7ac0db3290acfb634b501ba38e7362ff2b3bf10c
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
  - path: conf/record_review.yaml
    sha256: c2f5d0eb4c5744f5fe354c92184ddab144dc2688dba952b032b4f3d597bc08d6
    role: context
  - path: conf/sources.yaml
    sha256: a8e069f9278068b57fa234f43e03c8d893f857827b83fd10cfa92d6815aed642
    role: context
  - path: curation/decisions.tsv
    sha256: 0602cca13e6495da256a6f1cfd5897462f73f9739a729447862017d93c148efd
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: e1238e20fe1cc3d7bdce19354b9ea0f2ab949dba171b692238d321e741541191
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
  - path: data/habitats/RETIRED.tsv
    sha256: 41beffc45aabdf304de633c21200b375d7f01d1cb2e036d4a026961d545a35e5
    role: context
  - path: data/habitats/engineered/membrane_bioreactor.yaml
    sha256: 89d8964bce58cdeac9c2d3cc6db41e3cab4ef5ef6a6f2e312deaf115306c77fe
    role: context
  - path: data/habitats/engineered/mixed_liquor.yaml
    sha256: 936b93a5044c512a3703e36c06944ec42937bfd8e5a275e60579debd370e6d8a
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
  - path: history/mappings/mixed_liquor/2026-10-09T152516Z-codex-gpt-5-71c5fe.yaml
    sha256: 431191aa7b7fef9e8b945c2a8bcf50c35e0adc8d4d908c1753f3f2ce3b62d64b
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reviews/structured/20261009T152149Z-mixed-liquor-mbr/review.md
    sha256: 01f9fd0853ee435689bfcb3debef1c721fbc34e72d7113a0348d20ec1313a44f
    role: context
  - path: reviews/structured/20261009T152149Z-mixed-liquor-mbr/review.yaml
    sha256: 22206fde69166eeafa1e208b8506fbdb58db7d4c0ef15245a8ad1bc3e9a9d2a5
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
  - path: tests/test_mixed_liquor_parents.py
    sha256: 8c16a5e955e82432e4bd3deb5d2cae6c8443c73750ccd9d6f8ff2c7a0ba32e6d
    role: context
scope:
  description: Historical full-record assessment of the correction committed at 7ac0db3290acfb634b501ba38e7362ff2b3bf10c,
    with a scoped F1 disposition. Both complete target blobs were re-read there; all
    44 captured hashes match that retained commit and the current product tree. External
    evidence is retained from the original observation, not newly collected.
  selection: Exact original target ID/path; inspect captured the post-fix inputs before
    this assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.904cce6b84
  exclusions:
  - target: The same-label Mixed liquor sibling and all other records
    reason: Shared regression covers collateral changes; this document reviews and
      dispositions only its one named target.
targets:
- target_id: habitatmech:GOLD.904cce6b84
  path: data/habitats/engineered/mixed_liquor.yaml
  label: Mixed liquor (MBR)
  kind: generated
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Source-specific ITEM grounding/scope decision
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Guarded source-context parent exclusion
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Supported novel definition and genus
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Frozen path/node/count inventory
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Generated record, hierarchy and lifecycle
checks:
- check_id: C1
  name: Schema
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.904cce6b84
  command: env UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/mixed_liquor.yaml
  exit_code: 0
  summary: No issues found.
- check_id: C2
  name: Closed schema
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.904cce6b84
  command: env UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/mixed_liquor.yaml
    data/habitats/engineered/mixed_liquor__ef7a87e7.yaml
  exit_code: 0
  summary: Two exact files, zero errors.
- check_id: C3
  name: Corpus
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.904cce6b84
  command: env UV_CACHE_DIR=build/uv-cache just verify-corpus
  exit_code: 0
  summary: 3208 expected/present, zero missing, extra or differing.
- check_id: C4
  name: History
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.904cce6b84
  command: env UV_CACHE_DIR=build/uv-cache just validate-history
  exit_code: 0
  summary: 222 histories valid.
- check_id: C5
  name: Isolation and guarded exclusions
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.904cce6b84
  command: env UV_CACHE_DIR=build/uv-cache uv run pytest -q tests/test_mixed_liquor_parents.py
    tests/test_gold_parent_exclusions.py
  exit_code: 0
  summary: 49 passed in 69.29 seconds.
- check_id: C6
  name: Render
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.904cce6b84
  command: env UV_CACHE_DIR=build/uv-cache just render
  exit_code: 0
  summary: 3208 habitat pages, 252 redirects, eight categories and 114 term requests
    rendered after a verified map refresh.
- check_id: C7
  name: Map source/vector validation
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.904cce6b84
  command: env UV_CACHE_DIR=build/uv-cache uv run python scripts/embedding_pipeline.py
    check --output build/pr1802-map-download/data/text_map --input build/text-map/pr1802-inputs.jsonl
    --cache build/pr1802-map-download/build/text-map/vectors.sqlite
  exit_code: 0
  summary: Full local input identity and cache vectors match the generated 3208-point
    bundle.
- check_id: C8
  name: Publication provenance
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.904cce6b84
  command: env UV_CACHE_DIR=build/uv-cache uv run pytest -q tests/test_record_review_publication.py
  exit_code: 0
  summary: Two passed in 12.13 seconds. Exact off-main base retained under an annotated
    tag and verified peeled on origin.
  scope_note: Regression invocation before saving this successor; exact retained base
    also verified manually on origin. Publication checks are rerun after saving.
- check_id: C9
  name: Ontology labels
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.904cce6b84
  command: gh run view 37952670267 --json status,conclusion,headSha
  exit_code: 0
  summary: Success on exact product commit; no identity or label changes.
- check_id: C10
  name: Full local quality gate
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.904cce6b84
  command: env UV_CACHE_DIR=build/uv-cache just qc
  exit_code: 0
  summary: All HabitatMech quality gates passed; 647 tests passed, three skipped in
    632.57 seconds. This is the completed rerun after map regeneration, not the interrupted
    earlier run.
  evidence_ids:
  - E9
- check_id: C11
  name: Full CI quality gate
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.904cce6b84
  command: gh run view 37952670630 --json status,conclusion,headSha,url
  exit_code: 0
  summary: Completed success on product commit 564b79a8360155f6d98ca1eefe3c1f8f565fafa4;
    actual gate log inspected.
  evidence_ids:
  - E9
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/engineered/mixed_liquor.yaml
  locator: Complete regenerated record and diff from 14d99404e9da3170d3d099aedc2855d4e8c4081e
  accessed_at: '2026-10-09T15:29:42Z'
  support: supports
  summary: The unsupported sole parent ENVO:03600010 is removed. Identity, label,
    category, source attestation including path and 2-node note, count/unit/predicate
    omissions, UNGROUNDED/SEEDED and both prior events are unchanged. One deterministic
    SOURCE_PARENT_EXCLUDED event is appended; no replacement parent or definition
    is asserted.
- evidence_id: E2
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: habitatmech:GOLD.904cce6b84; Engineered > Bioreactor > MBR (Membrane bioreactor)
    > Mixed liquor; expected parent ENVO:03600010
  accessed_at: '2026-10-09T15:29:42Z'
  support: supports
  summary: 'The exact source-concept/path/parent row records codex-gpt-5, 2026-10-09,
    primary-source rationale and issue #1800. This excludes only the immediate GOLD
    contribution; the parent record and unrelated sources are unchanged.'
- evidence_id: E3
  kind: prior_review
  reference: reviews/structured/20261009T152149Z-mixed-liquor-mbr/review.yaml
  locator: Complete original observation; F1 and E1-E14
  accessed_at: '2026-10-09T15:29:42Z'
  support: supports
  summary: Retains the one-record scientific review, exact GOLD crosswalk and NCBI
    inspection, current ontology verification, EPA material-versus-equipment distinction,
    original access limits, and stable finding key. This successor rechecks the implemented
    relationship correction; it does not pretend to repeat every external request
    or close unrelated identity questions.
- evidence_id: E4
  kind: record_content
  reference: tests/test_mixed_liquor_parents.py
  locator: Whole-corpus differential regression
  accessed_at: '2026-10-09T15:29:42Z'
  support: supports
  summary: With and without these two exclusions, all 3208 concept IDs remain identical
    and only the two intended records differ. The regression asserts only parent removal
    and one audit event, unchanged remaining fields, retained mint/path/node notes,
    status and count/unit/predicate omissions. Together with shared exclusion tests,
    49 cases pass.
- evidence_id: E5
  kind: record_content
  reference: history/mappings/mixed_liquor/2026-10-09T152516Z-codex-gpt-5-71c5fe.yaml
  locator: Full session provenance
  accessed_at: '2026-10-09T15:29:42Z'
  support: supports
  summary: 'Append-only session record attributes this hierarchy-only edit to codex-gpt-5/gpt-5/codex
    and issue #1800. Its details honestly distinguish checks underway at creation
    from later completed results. Both new histories and all 222 total histories validate.'
- evidence_id: E6
  kind: authority
  reference: https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=9100NX8X.txt
  locator: Section III Definitions, as inspected in original observation
  accessed_at: '2026-10-09T15:21:49Z'
  support: supports
  summary: Inspected EPA terminology distinguishes mixed-liquor material from the
    treatment equipment containing it. It supports removing the false is-a relation,
    not a universal treatment condition or exact sludge identity.
- evidence_id: E7
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/37952082716
  locator: Build head 7ac0db3290acfb634b501ba38e7362ff2b3bf10c; canary and full receipts
  accessed_at: '2026-10-09T15:47:52Z'
  support: supports
  summary: Real pinned Linux BGE/PaCMAP build encoded two changed records, reused
    both on repeat, validated a 32-record projection canary, reused all 3208 vectors
    on the full pass and generated all 3208 finite points. Local full-input/vector
    verification passes. Only these two records' parent-label text changed; the temporary
    workflow is removed.
- evidence_id: E8
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/37952670267
  locator: Head 564b79a8360155f6d98ca1eefe3c1f8f565fafa4
  accessed_at: '2026-10-09T15:47:52Z'
  support: supports
  summary: Required ontology-label workflow completed successfully on the product
    commit. No identity/label was changed by the hierarchy correction.
- evidence_id: E9
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/37952670630
  locator: Product commit 564b79a8360155f6d98ca1eefe3c1f8f565fafa4; full gate logs
  accessed_at: '2026-10-09T15:47:52Z'
  support: supports
  summary: 'CI passes all native gates, with 647 tests passed and three skipped (424.54
    seconds). Fresh local just qc also exits zero: 647 passed/three skipped (632.57
    seconds), 222 histories, 3208 closed-schema/exact records, 32 overlays, curation
    floor, current site, redirects and term requests. No scientific input changed
    after the captured correction.'
assessments:
- assessment_id: A1
  area: identity
  topic: Retained qualified identity and source units
  outcome: supported
  target_ids:
  - habitatmech:GOLD.904cce6b84
  summary: Mint, full GOLD path, distinct same-label identity and collapsed source-node
    note remain supported by the original scientific review. Zero frozen counters
    still omit count/unit; separate biosamples are not organisms or independent environmental
    replicates.
  evidence_ids:
  - E1
  - E3
- assessment_id: A2
  area: graph
  topic: Corrected context-only parent
  outcome: supported
  target_ids:
  - habitatmech:GOLD.904cce6b84
  summary: The exact material-to-equipment/facility relation is gone. No unsupported
    replacement relation is asserted, and whole-corpus comparison proves the parent
    record and all other records remain unchanged.
  evidence_ids:
  - E1
  - E2
  - E4
  - E6
- assessment_id: A3
  area: grounding
  topic: Grounding and lifecycle restraint
  outcome: supported
  target_ids:
  - habitatmech:GOLD.904cce6b84
  summary: UNGROUNDED/SEEDED and the prior CLASS decision remain appropriate to their
    provenance. Hierarchy review is not a new ITEM identity judgment or a basis for
    REVIEWED promotion.
  evidence_ids:
  - E1
  - E3
  - E5
- assessment_id: A4
  area: completeness
  topic: Definition, parameters, taxa, mechanisms, discussion and datasets
  outcome: supported
  target_ids:
  - habitatmech:GOLD.904cce6b84
  summary: All original optional-field absences and evidence limits are preserved.
    No parent taxa, source study conditions, SIP metrics, recipe or causal claim are
    imported. Neither material genus nor sibling equivalence is forced.
  evidence_ids:
  - E1
  - E3
- assessment_id: A5
  area: ownership
  topic: Maintained-input and generated-product consistency
  outcome: supported
  target_ids:
  - habitatmech:GOLD.904cce6b84
  summary: The exclusion table owns the correction; native canary writes and page
    generation produce the outputs. Append-only history and review lineage are retained.
    No raw source, seeder or ontology label change is needed.
  evidence_ids:
  - E2
  - E4
  - E5
  - E7
- assessment_id: A6
  area: evidence
  topic: Expression-module applicability
  outcome: not_applicable
  target_ids:
  - habitatmech:GOLD.904cce6b84
  evidence_ids:
  - E1
  - E3
  summary: No gene/regulator/protein or named transcriptomics dataset claim requires
    iModulonDB; its absence is not negative evidence.
- assessment_id: A7
  area: schema
  topic: Complete native verification
  outcome: supported
  target_ids:
  - habitatmech:GOLD.904cce6b84
  evidence_ids:
  - E4
  - E7
  - E8
  - E9
  summary: Both target schemas, full corpus reproduction, full local QC, exact product-commit
    CI and ontology labels pass. Map and page changes are required consequences of
    the two removed parent labels, not new biological claims.
findings:
- finding_id: F1
  issue_key: mixed-liquor-mbr-material-to-apparatus-parent
  category: graph
  severity: major
  status: resolved
  certainty: confirmed
  title: Mixed-liquor material is not a type of its containing equipment or facility
  description: The exact source-parent contribution ENVO:03600010 has been excluded.
    This resolves only the original material-to-apparatus/facility subsumption defect.
    No identity merge, substitute genus, new ecological condition or ITEM status follows.
  target_ids:
  - habitatmech:GOLD.904cce6b84
  field_paths:
  - parent_habitats
  evidence_ids:
  - E1
  - E2
  - E3
  - E4
  - E6
  rule_id: CLAUDE.md/semantic-invariants/strictly-broader
  native_severity: major
  normalization_reason: Materially unsupported habitat subsumption affects downstream
    graph interpretation; YAML identity and critical references remain valid, so this
    is not a blocker.
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Source-specific ITEM grounding/scope decision
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Guarded source-context parent exclusion
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Supported novel definition and genus
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1800
  disposition_reason: Source semantics establish the material/equipment distinction;
    the guarded maintained row and regenerated output implement the bounded correction.
    Whole-corpus differential testing confirms that unrelated claims and records remain
    intact.
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261009T152149Z-mixed-liquor-mbr
    finding_id: F1
actions: []
limitations:
- This is a same-agent follow-up, not independent approval. Source identity remains
  CLASS/SEEDED, without a newly authored definition or established exact ontology
  match.
- 'The original external-source bounds remain: the current GOLD workbook is not the
  frozen August source, and matched counts do not prove historical membership. No
  live-count refresh or source classification rewrite is performed.'
- GOLD supplies MBR context; the three exact NCBI submissions have sparse location/isolation
  fields and distinct HS50/HS5/HS0 titles. No treatment or sampling-condition equivalence
  is inferred.
- Local render initially failed as intended on stale map inputs; full QC was stopped
  during tests before rebuilding (exit130), not reported as a pass. The pinned torch
  runtime has no Intel macOS wheel; actual model inference/projection ran in the established
  temporary Linux workflow, then artifacts were validated locally.
- No corpus-wide scientific completion, SSSOM/KGX readiness, sibling merge or novel-term
  approval is implied.
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261009T152149Z-mixed-liquor-mbr
  relationship: Resolves only F1 after maintained-input correction; retains original
    scientific limitations.
links:
- https://github.com/CultureBotAI/HabitatMech/pull/1802
- https://github.com/CultureBotAI/HabitatMech/issues/1800
tags:
- habitat
- engineered
- gold
- finding-disposition
notes:
- HEAD advanced for product-only changes after the original inspect. Rather than recapture
  or replace hashes, this observation explicitly reviews the committed correction
  at its original 7ac0db3290acfb634b501ba38e7362ff2b3bf10c base (source.state git_commit).
  Fresh historical blob hashing verified all 44 original input digests and exact equality
  to the current tree; full target blobs were re-read. The exact annotated record-review-base
  tag is verified on origin.
- The prior immutable finding is resolved only by this explicit linked observation.
  The GitHub issue closes on merge, not merely on saving this review.
```
