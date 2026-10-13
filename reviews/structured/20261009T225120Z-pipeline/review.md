# Scientific record review: Pipeline

- Review: 20261009T225120Z-pipeline
- Repository: culturebotai/HabitatMech
- Started UTC: 2026-10-09T22:30:06Z
- Finished UTC: 2026-10-09T22:51:20Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

A pipeline-associated microbial habitat context is directly supported. Built environment (mesh:D000076624) includes human-made infrastructure and remains a defensible setting-level parent. ENVO:03600014 pipeline network is a candidate with different granularity, not a proven exact substitute. Enriched fluids do not establish that the source concept means fluid alone; retain the minted unresolved identity rather than forcing an equivalence.

## Scope And Provenance

One entire generated habitat record and its maintained provenance; source members examined to test this class's claims.

Selection: Exact identifier/path from the next six engineered records in the continuing 3208-record goal. Each bundle assesses exactly one target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 00d3d47eaaa603c89e08ae1dbe750063137b4809.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.edec297c39 | data/habitats/engineered/pipeline.yaml | generated | Pipeline |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Target schema | passed | True | habitatmech:GOLD.edec297c39 | Terminal exit 0: no issues found. |
| Closed-schema target cohort | passed | True | habitatmech:GOLD.edec297c39 | Six files, zero error files/rows. |
| Authoritative baseline QC | passed | True | habitatmech:GOLD.edec297c39 | Terminal exit 0: all HabitatMech quality gates passed. 652 tests passed, 3 skipped; 227 history records, 3208 strict-valid/reproduced records, 32 causal overlays, generated site, 252 redirects and term-request checks passed. |
| Ontology identifier/label correspondence | passed | True | habitatmech:GOLD.edec297c39 | 1178 canonical, 1 synonym, 5 exceptions; 2057 no-adapter skips. This is not validation of minted identity. |
| Native review infrastructure | passed | True | habitatmech:GOLD.edec297c39 | 64 existing bundles valid; 4 contract tests passed in 63.81s, before saving this observation. |
| Local source trace and complete target reproduction | passed | True | habitatmech:GOLD.edec297c39 | Exit 0; all six full documents equal their seed.build_document results; 14 raw tables and maintained rows parsed. |
| Current exact-path membership census | passed | True | habitatmech:GOLD.edec297c39 | Exit 0; complete workbook sheets, member/project/study joins and source hashes checked. Analysis output is temporary; durable source URL/hash and accession locators are retained here. |
| Target causal and iModulon applicability | not_applicable | False | habitatmech:GOLD.edec297c39 | No target overlay, gene, regulator, protein or expression-module assertion. Project titles are provenance context, not transcriptomic interpretation. |
| Original upstream re-extraction | unavailable | False | habitatmech:GOLD.edec297c39 | Original August workbook and KGX node/edge sources were unavailable in the bounded ignored-inclusive search. Current export does not reconstruct historical membership. |

## Scientific And Domain Assessments

### Habitat identity, grounding and strict hierarchy

identity: supported. Targets: habitatmech:GOLD.edec297c39.

A pipeline-associated microbial habitat context is directly supported. Built environment (mesh:D000076624) includes human-made infrastructure and remains a defensible setting-level parent. ENVO:03600014 pipeline network is a candidate with different granularity, not a proven exact substitute. Enriched fluids do not establish that the source concept means fluid alone; retain the minted unresolved identity rather than forcing an equivalence.

### Frozen and later source quantities

provenance: supported. Targets: habitatmech:GOLD.edec297c39.

GOLD ecosystem data row 1274, decision row 1312; nodes 4663&#124;4664&#124;4665, zero original assertions. Supplemental table has 3 BIOSAMPLE at row 817 and Gs0111382 at study row 629. CLASS-level decision correctly leaves UNGROUNDED/SEEDED. Later source counts are observations from a different snapshot; project counts are not added to organism or Biosample counts.

### Optional biology, triads and status

completeness: supported. Targets: habitatmech:GOLD.edec297c39.

No unsupported parameters, characteristic taxa or causal mechanisms were added to fill optional slots. No target exact triad was borrowed from descendants. CLASS/SEEDED is not itself an error; REVIEWED, when present, describes ITEM coverage rather than universal scientific approval.

### Validation and input ownership

schema: supported. Targets: habitatmech:GOLD.edec297c39.

Required native gates passed. Scientific concerns remain independent of schema and corpus reproduction. Corrections must use maintained curation/source inputs and validated generation, not hand-edited habitat or page files.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/engineered/pipeline.yaml; Entire YAML including all history events | supports | Full record read, source concepts resolved and all current fields traced. No target causal graph, environmental parameter, characteristic taxon, experimental evidence, discussion or dataset claims are present. |
| E2 | data/raw/gold_ecosystem_paths.tsv; Exact canonical paths; row numbers below are 1-based data rows excluding comments/headers | supports | GOLD ecosystem data row 1274, decision row 1312; nodes 4663&#124;4664&#124;4665, zero original assertions. Supplemental table has 3 BIOSAMPLE at row 817 and Gs0111382 at study row 629. CLASS-level decision correctly leaves UNGROUNDED/SEEDED. Entire target reproduces from seed.build_document. Complete 14 raw TSVs and seven curation TSVs plus PATHS were parsed; no exact target triad was attached or borrowed from descendants. |
| E3 | https://gold.jgi.doe.gov/download?mode=site_excel; Complete exact-path Biosample/Organism scan, all corresponding SequencingProject and Study joins | partial | Oct 9 public workbook, hash rechecked. Sheets scanned in full (including headers): Biosample 244951, Organism 532019, SequencingProject 636914, Study 63806. 3 exact Biosamples, 0 Organism, 3 linked projects. Gb0197312/Gb0197313/Gb0197314 (rows 57577-57579) are lab-enriched produced-water microbial communities from pipeline fluids in Medicine Hat. Gp0349329/30/31 link to Gs0111382. The broader study spans eight source paths; only the three exact-path members count here. |
| E4 | data/raw; curation; build; /private/tmp; Exact identifiers, labels, slugs, paths and original GOLD source filenames | context_only | Ignored-inclusive searches and complete structured TSV parsing establish bounded absences of target overlays and maintained rows. Original August GOLD workbook and node/edge dumps were not recovered under data/raw, build and /private/tmp; this is not a machine-wide absence claim. |
| E5 | https://gold.jgi.doe.gov/download?mode=ecosystempaths; Exact terminal path, not descendant matches | supports | Current classification workbook retains the reviewed path(s). Descendants were distinguished from exact terminal membership. |
| O1 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO:03600014; Active pipeline network definition and editorial scope note | context_only | The ontology term denotes a constructed pipe system transporting liquid or gas. It flags inside/outside sample context; exact identity to this broad source path has not been established. |
| O2 | https://id.nlm.nih.gov/mesh/M000622402.json; Preferred concept of mesh:D000076624 (descriptor JSON also inspected) | supports | Built Environment includes human-made physical environment and infrastructure. This supports the retained infrastructure reading, not an automatic identity for its sampled contents. |

## Limits And Additional Notes

- The original frozen upstream membership was not reconstructed. The later GOLD public workbook must not replace historical counts or establish the same members by matching totals.
- Exact-path occurrence supports provenance, not universal phenotype, characteristic presence or a mechanistic claim.
- Optional live GOLD study pages were inaccessible (HTTP 403); official downloadable workbook and primary/authority endpoints were used. NCBI web rendering failed for some project pages; official XML was inspected, with one transient 429 before successful PRJNA657700 retry.
- No independent scientific sign-off or native status promotion is implied. Legacy reports are historical context, not automatically migrated native reviews.
- Input capture was extended from 45 to 53 files after additional full-table inspection; all prior hashes and Git revision were verified unchanged. No silent snapshot refresh.
- Review-only observation at the captured baseline. The user separately authorized publication and issue fixes; subsequent curation does not rewrite this bundle.
- Evidence accessed_at marks completion of the inspection interval recorded by started_at/finished_at, not an asserted HTTP request timestamp for each source.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261009T225120Z-pipeline
kind: record
repository: culturebotai/HabitatMech
title: 'Scientific record review: Pipeline'
started_at: '2026-10-09T22:30:06Z'
finished_at: '2026-10-09T22:51:20Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same ongoing agent performed evidence inspection and assessment;
    no independent human or second-agent scientific sign-off is claimed.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: A pipeline-associated microbial habitat context is directly supported. Built
  environment (mesh:D000076624) includes human-made infrastructure and remains a defensible
  setting-level parent. ENVO:03600014 pipeline network is a candidate with different
  granularity, not a proven exact substitute. Enriched fluids do not establish that
  the source concept means fluid alone; retain the minted unresolved identity rather
  than forcing an equivalence.
source:
  git_revision: 00d3d47eaaa603c89e08ae1dbe750063137b4809
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
    sha256: 0602cca13e6495da256a6f1cfd5897462f73f9739a729447862017d93c148efd
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 2d41fc93db4939122b3909f2a412b84b679703948b10d9f02e12021442f71407
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: d2d11825934fa9088365c249ddae6c718bf8232846add057bcb7d099a2c0c090
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
  - path: data/habitats/engineered/aquaculture.yaml
    sha256: 82bda18b49783b27434b6d10b64e097e7699ac0ceb613fc41c86b24e913547e3
    role: context
  - path: data/habitats/engineered/artificial_ecosystem.yaml
    sha256: 721350810f5b9c5c33a03ce8133bdfee22605458fef414c87390469695964317
    role: context
  - path: data/habitats/engineered/bioreactor.yaml
    sha256: c0a5f4d06130d949810c29b15f5874b4e9673b23dc188161d699412c2bea0c02
    role: context
  - path: data/habitats/engineered/built_environment.yaml
    sha256: df6de674d7d48a98b7d1d43a0a5c67a696550f00e1fb787ec71a3569acc47021
    role: context
  - path: data/habitats/engineered/material.yaml
    sha256: 01b2767b0983a3ed85de20b759119f14102b6c1333dad051466e7b94667ffa02
    role: context
  - path: data/habitats/engineered/nutrient_poor.yaml
    sha256: 90a2b50a7029a19e1d507f102cd01eed7decd739ba962ca306a29ee96160a1d1
    role: context
  - path: data/habitats/engineered/pipeline.yaml
    sha256: c4833032fbf0dc5082a0e901aa83c22313e2a59cdbfa8dee6d38911536a949a4
    role: target
  - path: data/habitats/engineered/simulated_communities_microbial_mixture.yaml
    sha256: f4108a8dfedd597c339102eba44bea265e7171638201ddc2f8ed1695865a6adc
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
  - path: reports/yaml_record_review/20260924T173320Z-aquaculture.md
    sha256: 8ac09f788ecb5cd673e00ae76b48a53743f3fdcc6fb88799950a647b16f24586
    role: context
  - path: reports/yaml_record_review/20260925T015321Z-photobioreactor.md
    sha256: 37a83847ad01cb6021578999e480949200770484718e4f46399156661f8a3c21
    role: context
  - path: reports/yaml_record_review/20260925T054406Z-nutrient_poor.md
    sha256: 33ab8561e5157f01c906ff7d4c758f69eda9037191ba061266acf07e772165eb
    role: context
  - path: reports/yaml_record_review/20260925T060448Z-pine_litter_on_sand.md
    sha256: 948a348378efe97f541c29be7bafd206c7775882b5a520290b955e964b54a0f2
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
scope:
  description: One entire generated habitat record and its maintained provenance;
    source members examined to test this class's claims.
  selection: Exact identifier/path from the next six engineered records in the continuing
    3208-record goal. Each bundle assesses exactly one target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.edec297c39
  exclusions:
  - target: Other records, descendant source paths and all-record completion
    reason: Context only; neither their biological validity nor total corpus completion
      is asserted.
targets:
- target_id: habitatmech:GOLD.edec297c39
  path: data/habitats/engineered/pipeline.yaml
  label: Pipeline
  kind: generated
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: source-concept grounding and review depth
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: frozen GOLD paths, node IDs and assertion counts
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: guarded context-only source-parent exclusions
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: generated identity, parents, attestations and native status
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: stable generated slug ownership
checks:
- check_id: C1
  name: Target schema
  command: just validate data/habitats/engineered/pipeline.yaml
  status: passed
  required: true
  exit_code: 0
  summary: 'Terminal exit 0: no issues found.'
  target_ids:
  - habitatmech:GOLD.edec297c39
- check_id: C2
  name: Closed-schema target cohort
  command: just validate-strict data/habitats/engineered/photobioreactor.yaml data/habitats/engineered/pine_litter_on_sand.yaml
    data/habitats/engineered/pipeline.yaml data/habitats/engineered/plant_growth_chamber.yaml
    data/habitats/engineered/plant_nodule.yaml data/habitats/engineered/plastic.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Six files, zero error files/rows.
  target_ids:
  - habitatmech:GOLD.edec297c39
- check_id: C3
  name: Authoritative baseline QC
  command: just qc
  status: passed
  required: true
  exit_code: 0
  summary: 'Terminal exit 0: all HabitatMech quality gates passed. 652 tests passed,
    3 skipped; 227 history records, 3208 strict-valid/reproduced records, 32 causal
    overlays, generated site, 252 redirects and term-request checks passed.'
  target_ids:
  - habitatmech:GOLD.edec297c39
- check_id: C4
  name: Ontology identifier/label correspondence
  command: just validate-products
  status: passed
  required: true
  exit_code: 0
  summary: 1178 canonical, 1 synonym, 5 exceptions; 2057 no-adapter skips. This is
    not validation of minted identity.
  target_ids:
  - habitatmech:GOLD.edec297c39
- check_id: C5
  name: Native review infrastructure
  command: just review-check
  status: passed
  required: true
  exit_code: 0
  summary: 64 existing bundles valid; 4 contract tests passed in 63.81s, before saving
    this observation.
  target_ids:
  - habitatmech:GOLD.edec297c39
- check_id: C6
  name: Local source trace and complete target reproduction
  command: uv run python /private/tmp/habitatmech-review-q-local.py
  status: passed
  required: true
  exit_code: 0
  summary: Exit 0; all six full documents equal their seed.build_document results;
    14 raw tables and maintained rows parsed.
  target_ids:
  - habitatmech:GOLD.edec297c39
- check_id: C7
  name: Current exact-path membership census
  command: uv run python /private/tmp/habitatmech-review-q-workbook.py
  status: passed
  required: true
  exit_code: 0
  summary: Exit 0; complete workbook sheets, member/project/study joins and source
    hashes checked. Analysis output is temporary; durable source URL/hash and accession
    locators are retained here.
  target_ids:
  - habitatmech:GOLD.edec297c39
- check_id: C8
  name: Target causal and iModulon applicability
  status: not_applicable
  required: false
  summary: No target overlay, gene, regulator, protein or expression-module assertion.
    Project titles are provenance context, not transcriptomic interpretation.
  target_ids:
  - habitatmech:GOLD.edec297c39
- check_id: C9
  name: Original upstream re-extraction
  status: unavailable
  required: false
  summary: Original August workbook and KGX node/edge sources were unavailable in
    the bounded ignored-inclusive search. Current export does not reconstruct historical
    membership.
  target_ids:
  - habitatmech:GOLD.edec297c39
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/engineered/pipeline.yaml
  locator: Entire YAML including all history events
  accessed_at: '2026-10-09T22:51:20Z'
  support: supports
  summary: Full record read, source concepts resolved and all current fields traced.
    No target causal graph, environmental parameter, characteristic taxon, experimental
    evidence, discussion or dataset claims are present.
- evidence_id: E2
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Exact canonical paths; row numbers below are 1-based data rows excluding
    comments/headers
  accessed_at: '2026-10-09T22:51:20Z'
  support: supports
  summary: GOLD ecosystem data row 1274, decision row 1312; nodes 4663|4664|4665,
    zero original assertions. Supplemental table has 3 BIOSAMPLE at row 817 and Gs0111382
    at study row 629. CLASS-level decision correctly leaves UNGROUNDED/SEEDED. Entire
    target reproduces from seed.build_document. Complete 14 raw TSVs and seven curation
    TSVs plus PATHS were parsed; no exact target triad was attached or borrowed from
    descendants.
- evidence_id: E3
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=site_excel
  locator: Complete exact-path Biosample/Organism scan, all corresponding SequencingProject
    and Study joins
  accessed_at: '2026-10-09T22:51:20Z'
  support: partial
  summary: 'Oct 9 public workbook, hash rechecked. Sheets scanned in full (including
    headers): Biosample 244951, Organism 532019, SequencingProject 636914, Study 63806.
    3 exact Biosamples, 0 Organism, 3 linked projects. Gb0197312/Gb0197313/Gb0197314
    (rows 57577-57579) are lab-enriched produced-water microbial communities from
    pipeline fluids in Medicine Hat. Gp0349329/30/31 link to Gs0111382. The broader
    study spans eight source paths; only the three exact-path members count here.'
  snapshot_sha256: 5f48b2f50fb2a9257754960a0f0e12dc6e8fa121e97c3e9f4497249e5fe6e439
- evidence_id: E4
  kind: search
  reference: data/raw; curation; build; /private/tmp
  locator: Exact identifiers, labels, slugs, paths and original GOLD source filenames
  accessed_at: '2026-10-09T22:51:20Z'
  support: context_only
  summary: Ignored-inclusive searches and complete structured TSV parsing establish
    bounded absences of target overlays and maintained rows. Original August GOLD
    workbook and node/edge dumps were not recovered under data/raw, build and /private/tmp;
    this is not a machine-wide absence claim.
  search_scope: rg --no-ignore --hidden and full structured TSV parses, including
    ignored files in the named trees; no machine-wide negative assertion.
- evidence_id: E5
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=ecosystempaths
  locator: Exact terminal path, not descendant matches
  accessed_at: '2026-10-09T22:51:20Z'
  support: supports
  summary: Current classification workbook retains the reviewed path(s). Descendants
    were distinguished from exact terminal membership.
  snapshot_sha256: 3933e5f0664915c1bbfa00212e17d013da360fb33dd52e509254050813135396
- evidence_id: O1
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO:03600014
  locator: Active pipeline network definition and editorial scope note
  accessed_at: '2026-10-09T22:51:20Z'
  support: context_only
  summary: The ontology term denotes a constructed pipe system transporting liquid
    or gas. It flags inside/outside sample context; exact identity to this broad source
    path has not been established.
- evidence_id: O2
  kind: authority
  reference: https://id.nlm.nih.gov/mesh/M000622402.json
  locator: Preferred concept of mesh:D000076624 (descriptor JSON also inspected)
  accessed_at: '2026-10-09T22:51:20Z'
  support: supports
  summary: Built Environment includes human-made physical environment and infrastructure.
    This supports the retained infrastructure reading, not an automatic identity for
    its sampled contents.
assessments:
- assessment_id: A1
  area: identity
  topic: Habitat identity, grounding and strict hierarchy
  outcome: supported
  summary: A pipeline-associated microbial habitat context is directly supported.
    Built environment (mesh:D000076624) includes human-made infrastructure and remains
    a defensible setting-level parent. ENVO:03600014 pipeline network is a candidate
    with different granularity, not a proven exact substitute. Enriched fluids do
    not establish that the source concept means fluid alone; retain the minted unresolved
    identity rather than forcing an equivalence.
  target_ids:
  - habitatmech:GOLD.edec297c39
  evidence_ids:
  - E1
  - E2
  - E3
  - E5
  - O1
  - O2
- assessment_id: A2
  area: provenance
  topic: Frozen and later source quantities
  outcome: supported
  summary: GOLD ecosystem data row 1274, decision row 1312; nodes 4663|4664|4665,
    zero original assertions. Supplemental table has 3 BIOSAMPLE at row 817 and Gs0111382
    at study row 629. CLASS-level decision correctly leaves UNGROUNDED/SEEDED. Later
    source counts are observations from a different snapshot; project counts are not
    added to organism or Biosample counts.
  target_ids:
  - habitatmech:GOLD.edec297c39
  evidence_ids:
  - E1
  - E2
  - E3
  - E5
- assessment_id: A3
  area: completeness
  topic: Optional biology, triads and status
  outcome: supported
  summary: No unsupported parameters, characteristic taxa or causal mechanisms were
    added to fill optional slots. No target exact triad was borrowed from descendants.
    CLASS/SEEDED is not itself an error; REVIEWED, when present, describes ITEM coverage
    rather than universal scientific approval.
  target_ids:
  - habitatmech:GOLD.edec297c39
  evidence_ids:
  - E1
  - E2
  - E4
- assessment_id: A4
  area: schema
  topic: Validation and input ownership
  outcome: supported
  summary: Required native gates passed. Scientific concerns remain independent of
    schema and corpus reproduction. Corrections must use maintained curation/source
    inputs and validated generation, not hand-edited habitat or page files.
  target_ids:
  - habitatmech:GOLD.edec297c39
  evidence_ids:
  - E1
  - E2
findings: []
actions: []
limitations:
- The original frozen upstream membership was not reconstructed. The later GOLD public
  workbook must not replace historical counts or establish the same members by matching
  totals.
- Exact-path occurrence supports provenance, not universal phenotype, characteristic
  presence or a mechanistic claim.
- Optional live GOLD study pages were inaccessible (HTTP 403); official downloadable
  workbook and primary/authority endpoints were used. NCBI web rendering failed for
  some project pages; official XML was inspected, with one transient 429 before successful
  PRJNA657700 retry.
- No independent scientific sign-off or native status promotion is implied. Legacy
  reports are historical context, not automatically migrated native reviews.
notes:
- Input capture was extended from 45 to 53 files after additional full-table inspection;
  all prior hashes and Git revision were verified unchanged. No silent snapshot refresh.
- Review-only observation at the captured baseline. The user separately authorized
  publication and issue fixes; subsequent curation does not rewrite this bundle.
- Evidence accessed_at marks completion of the inspection interval recorded by started_at/finished_at,
  not an asserted HTTP request timestamp for each source.
tags:
- engineered
- gold
- scientific-review
```
