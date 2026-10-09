# oil or gas pipeline network: source, identity and hierarchy review

- Review: 20261009T185455Z-oil_gas_pipeline
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-09T18:33:49Z
- Finished UTC: 2026-10-09T18:54:55Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified pass: the authored pipeline-network definition, broad genus, oil-only xref and native REVIEWED status are supported. The frozen single organism was not recovered in the later workbook, leaving the commodity versus industry-sector interpretation limited.

## Scope And Provenance

Entire single generated record and all contributing source concepts; related records are context only.

Selection: Exact path/ID selection from six next engineered filename leads in the ongoing 3208-record corpus review. Each is saved as a separate one-record judgement; this is not full-corpus sign-off.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a3ab5a95c34e00900b1a53b571518cea4df20599.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.74bb711f82 | data/habitats/engineered/oil_gas_pipeline.yaml | generated | oil or gas pipeline network |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Schema | passed | True | habitatmech:GOLD.74bb711f82 | No issues found. |
| Closed schema | passed | True | habitatmech:GOLD.74bb711f82 | One file, zero errors. |
| Full native quality gates | passed | True | habitatmech:GOLD.74bb711f82 | 648 passed,3 skipped; all native gates passed; fresh run at captured base. |
| Ontology labels | passed | True | habitatmech:GOLD.74bb711f82 | 1178 canonical,1 synonym,5 exceptions,2057 no-adapter skips; no claim of semantic validation. |
| Existing structured bundles | passed | True | habitatmech:GOLD.74bb711f82 | 42 valid existing reviews before saving these observations. |
| Captured input stability and full-document reproduction | passed | True | habitatmech:GOLD.74bb711f82 | All original50 captured hashes rechecked unchanged before expanded54-input native capture. In-memory full build_document equality confirmed for this target; source revision unchanged. |
| Target causal-overlay and expression-module checks | not_applicable | False | habitatmech:GOLD.74bb711f82 | No target causal overlay or gene/expression claim; full QC still exercises repository-wide causal/reference gates. |

## Scientific And Domain Assessments

### Physical habitat and source identity

identity: supported. Targets: habitatmech:GOLD.74bb711f82.

Manufactured networks carrying oil/gas are physical microbial habitat contexts, distinct from the transport procedure, crude oil chemical or a particular pipeline sample. The authored commodity interpretation is supported as a plausible reading, not proven from the missing original member.

### Exact identity versus broader/xref scope

grounding: supported. Targets: habitatmech:GOLD.74bb711f82.

ENVO:03600014 covers pipeline networks transporting liquids/gases. ENVO:03600012 is oil-only and additionally specifies consumer destination, so xref rather than exact identity is appropriate. Petroleum-products/gas breadth is curator-authored; alternative industry-sector usage remains a source-scope limitation.

### All parent contribution routes

graph: supported. Targets: habitatmech:GOLD.74bb711f82.

Both the ontology pipeline-network genus and minted generic Pipeline source are broader under the authored commodity interpretation. ADD retains the independent source parent. Neither gathering/production lines nor the primary paper justify a consumer-only restriction.

### Attestation counts, source versions and triad roles

quantity: supported. Targets: habitatmech:GOLD.74bb711f82.

Frozen node IDs, collapse notes and source count/unit rendering agree with inventory. Current BioSample/Organism counts are not added to frozen ORGANISM counts, treated as independent replicates, or transferred to characteristic taxa. gold_ecosystem_paths data row 895; decisions row 696 ITEM CONFIRM_UNGROUNDED with xref ENVO:03600012; term_requests row 71 ADD genus ENVO:03600014; PATHS row 2152. Exact path Engineered &gt; Built environment &gt; Pipeline &gt; Oil/Gas pipeline. No exact frozen sample, study or triad contribution.

### Native status and history

provenance: supported. Targets: habitatmech:GOLD.74bb711f82.

gold_unmatched -&gt; curated_confirm_ungrounded_from_gold_unmatched. One source and one ITEM-reviewed source; authored ADD definition contributes the ontology genus, while GOLD contributes minted Pipeline. Native REVIEWED is derived correctly; UNGROUNDED with a genus is not itself a narrow-match endpoint defect. Saving this review does not alter mapping status or any scientific input.

### Optional parameters, taxa, evidence, causal graphs and datasets

completeness: supported. Targets: habitatmech:GOLD.74bb711f82.

No target biological or mechanism claims are inferred from optional empty slots. Exact-key inventory scan found no target-owned environmental-parameter or taxon contribution; refinery triads have distinct scale/medium roles and are not identity evidence. Do not import study examples or infer characteristic organisms from source occurrence.

### Structured expression-module checks

evidence: not_applicable. Targets: habitatmech:GOLD.74bb711f82.

No gene, regulator, protein or transcriptomic dataset assertion in this target triggers an iModulonDB check. Its absence is not negative habitat evidence.

### Native gates and scientific limits

schema: supported. Targets: habitatmech:GOLD.74bb711f82.

All required native checks ran successfully. Mechanical validity does not adjudicate scope, ontology identity or source semantics; label skips are explicit.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/engineered/oil_gas_pipeline.yaml; Entire generated file and immediate parent files | supports | ENGINEERED / UNGROUNDED / REVIEWED. Definition authored by HabitatMech with EXACT_SYNONYM Oil/Gas pipeline and oil and gas pipeline. Parents ENVO:03600014 and minted Pipeline habitatmech:GOLD.edec297c39; xref ENVO:03600012. One GOLD source, 1 ORGANISM, nodes 8072/8073. Three history events read; no optional taxa/parameters/graphs/evidence/datasets. |
| E2 | data/raw/gold_ecosystem_paths.tsv; Exact path, node keys and related frozen inventory/decision rows | supports | gold_ecosystem_paths data row 895; decisions row 696 ITEM CONFIRM_UNGROUNDED with xref ENVO:03600012; term_requests row 71 ADD genus ENVO:03600014; PATHS row 2152. Exact path Engineered &gt; Built environment &gt; Pipeline &gt; Oil/Gas pipeline. No exact frozen sample, study or triad contribution. |
| E3 | src/habitatmech/seed.py; resolve_gold, apply_decision, apply_curated_definitions, GOLD parent pass and in-memory build_corpus/build_document | supports | gold_unmatched -&gt; curated_confirm_ungrounded_from_gold_unmatched. One source and one ITEM-reviewed source; authored ADD definition contributes the ontology genus, while GOLD contributes minted Pipeline. Native REVIEWED is derived correctly; UNGROUNDED with a genus is not itself a narrow-match endpoint defect. |
| E4 | https://gold.jgi.doe.gov/download?mode=site_excel; Complete streamed Biosample, Organism, SequencingProject and Study sheets | partial | No exact-path BioSample or Organism rows in the complete later workbook; the frozen 1 ORGANISM is retained and not explained away. No exact historical member identity recovered. Scanned 244951/532019/636914/63806 rows respectively, including headers. Public Oct9 snapshot is later than frozen inputs. |
| E5 | https://gold.jgi.doe.gov/download?mode=ecosystempaths; Complete sheet census after resetting misleading A1:A1 dimensions, 2422 rows | context_only | site data row 219, GOLD8073 retains the exact Oil/Gas pipeline path. Current path retention is not proof of original members. |
| E6 | curation/; history/; research/; reports/; reviews/; data/raw/; Ignored-inclusive Path.rglob traversal plus structured inventory scans | context_only | Identifier/label/slug scan covered 43 curation, 224 history, 121 research, 1274 report and 84 structured-review files. Matches include pipeline research/history and other-source sediment/sludge context; all 14 raw TSVs were parsed for exact fields and pipe-token keys. No target-owned causal overlay or extra definition was found except the pipeline term request. Context mentions are not new target coverage. |
| E7 | build/review-20261009n-qc.log; Fresh full QC at captured base, focused validators and fresh label validation | supports | QC exited0: 648 passed,3 skipped; all native gates passed, including exact 3208-record reproduction, history, reference/corpus tests and generated site. Each target separately passed schema and strict validation. validate-products:1178 canonical,1 synonym,5 exceptions,2057 no-adapter skips. Minted/MeSH skips do not certify parent semantics. |
| E8 | CLAUDE.md; Semantic invariants; docs/CURATION.md; schema HabitatRecord/SourceAttestation | supports | Every parent must be strictly broader, from any contribution route. Source counters retain their units; optional absence is not negative evidence. Generated ownership and ITEM-derived mapping status are preserved. Review is not native status promotion. |
| S1 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO:03600014; Active ENVO:03600014 and ENVO:03600012 labels, descriptions and parent APIs | supports | Pipeline network denotes a human construction conveying liquids or gases through pipes. Oil pipeline network is oil-specific with a consumer-destination constraint. Current terms agree with the frozen slice. |
| S2 | https://www.phmsa.dot.gov/sites/phmsa.dot.gov/files/2020-06/Gathering%20Pipelines%20FAQs.pdf; Page 1, Question 1; historical terminology only | supports | Gathering lines carry gases/liquids from source toward processing, refinery or transmission. This terminology example is not adopted as current legal guidance. |
| S3 | https://doi.org/10.3389/fmicb.2017.00099; PMC5281625 fullTextXML, Field Sample Collection; PMID 28197141 | supports | Pigging debris was collected from two Norwegian-sector North Sea production pipelines, with early/late cleaning-run samples. Supports physical pipeline-associated material; no universal corrosion mechanism, growth regime, taxon or gene claim is transferred. |
| S4 | research/habitats/engineered/oil-gas-pipeline-habitatmech-gold-74bb711f82-deep-research-claude_code.md; Definition alternatives plus two dated mapping history files | supports | Research is a lead, not independent evidence. It explicitly distinguishes commodity from industry-sector interpretations; subsequent ITEM decision and ADD definition chose commodity scope. Previously corrected pipeline-term absence is not reopened. |

## Limits And Additional Notes

- Original GOLD node/edge and August bulk-export membership were not recovered in the bounded source-file search. The later public workbook is not a replacement for frozen provenance.
- All ontology/candidate and source searches are bounded. Missing source examples and optional fields do not establish biological absence or justify invented definitions.
- Three tests are skipped in native QC; label validation skips2057 no-adapter labels, including minted/MeSH scope. These deterministic checks do not certify scientific grounding.
- Read-only observation captured and saved before separately authorized correction/publication. Actions are proposals, not claims of completed fixes.
- No paid research, source refresh, native status promotion or universal physiology/taxon/mechanism assertion.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261009T185455Z-oil_gas_pipeline
kind: record
repository: CultureBotAI/HabitatMech
title: 'oil or gas pipeline network: source, identity and hierarchy review'
started_at: '2026-10-09T18:33:49Z'
finished_at: '2026-10-09T18:54:55Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent continuing the scientific review and authorized publication;
    no independent scientific approval claimed.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Qualified pass: the authored pipeline-network definition, broad genus, oil-only
  xref and native REVIEWED status are supported. The frozen single organism was not
  recovered in the later workbook, leaving the commodity versus industry-sector interpretation
  limited.'
source:
  git_revision: a3ab5a95c34e00900b1a53b571518cea4df20599
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
    sha256: cc4da2e7e5e8750e6c023683014aa37a909230280f231eec5be7c71795340312
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 2b7f7bb6977a9d7a1b19856962bb63cf0a7f53ab435b3fb7100bffdfddfba3c5
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
  - path: data/habitats/engineered/built_environment.yaml
    sha256: df6de674d7d48a98b7d1d43a0a5c67a696550f00e1fb787ec71a3569acc47021
    role: context
  - path: data/habitats/engineered/engineered_product__d2d22ac0.yaml
    sha256: bd11c704d1f5b049fdddfdf5ce98d7bfe68d53480de20707feefab541d162bbf
    role: context
  - path: data/habitats/engineered/oil_contaminated_sediment.yaml
    sha256: a17541198edee77179f0f1bd913f126b730e4d7594f40d5e9d6ff145dc79481e
    role: context
  - path: data/habitats/engineered/oil_gas_pipeline.yaml
    sha256: d2e24936c5edf9135504f6b9db40713a4326cc1ca7d14e14a306e767d8a90750
    role: target
  - path: data/habitats/engineered/oil_refinery.yaml
    sha256: 76cbfb1bceec08f47f788a602e075bb741b73b9bdbe7771891cf96d6574fdf35
    role: context
  - path: data/habitats/engineered/oil_sludge.yaml
    sha256: 5a90a5a027fbc0f904ef707f13362482ce3290808307dbab7752a2eb5d78a9e5
    role: context
  - path: data/habitats/engineered/optical_instruments.yaml
    sha256: 4cdc5830cffbd2b9fcb16491a8d27596314f96a004b73fe2f183617c49a69981
    role: context
  - path: data/habitats/engineered/optical_lens.yaml
    sha256: 5cad1470101f5ee168ef18a9e019a1514b4ba0269a0c7d4bc2ee614700900706
    role: context
  - path: data/habitats/engineered/petrochemical.yaml
    sha256: b1ae13932d6d5faa80c1d44c1faea5058af8580983702d98d6225eb1a3ab959f
    role: context
  - path: data/habitats/engineered/pipeline.yaml
    sha256: c4833032fbf0dc5082a0e901aa83c22313e2a59cdbfa8dee6d38911536a949a4
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
  - path: history/mappings/oil_gas_pipeline/2026-09-09T024715Z-claude-code-0b52e7.yaml
    sha256: 77c8bc77e8634838e6a622320e5913f02aa1843cf2ecb51d6f19a5e773cd0d58
    role: context
  - path: history/mappings/oil_gas_pipeline/2026-09-09T024716Z-claude-code-a9452f.yaml
    sha256: 8f4976fa945668c58b98828693ca9ce6cdf9a9eb7d18d9753aa7f208e89267fa
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: research/habitats/engineered/oil-gas-pipeline-habitatmech-gold-74bb711f82-deep-research-claude_code.md
    sha256: 002c81942e77b8e2179486afef17f48c4222597ddc0d040b290dfc4b003e3add
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/extract_gold_biosamples.py
    sha256: b6a2773c86fe718e1ca0b1d7b32709f0eee491ac813655e310aa0817c0fec31b
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 52d2a22309a1f4a10728a663560bb4d918346c292221fd34139b99b4159d3fe5
    role: context
  - path: src/habitatmech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/habitatmech/seed.py
    sha256: 92adf631fa099120a497ff7001473e659347d23ac9b418f04cd341ddad5d2a89
    role: context
scope:
  description: Entire single generated record and all contributing source concepts;
    related records are context only.
  selection: Exact path/ID selection from six next engineered filename leads in the
    ongoing 3208-record corpus review. Each is saved as a separate one-record judgement;
    this is not full-corpus sign-off.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.74bb711f82
  exclusions:
  - target: All other HabitatMech records
    reason: Immediate parents, same-label sources and research examples inform this
      target only.
targets:
- target_id: habitatmech:GOLD.74bb711f82
  path: data/habitats/engineered/oil_gas_pipeline.yaml
  label: oil or gas pipeline network
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained source, decision, definition or generator owner
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained source, decision, definition or generator owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained source, decision, definition or generator owner
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Maintained source, decision, definition or generator owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained source, decision, definition or generator owner
checks:
- check_id: C1
  name: Schema
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.74bb711f82
  command: env UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/oil_gas_pipeline.yaml
  exit_code: 0
  summary: No issues found.
- check_id: C2
  name: Closed schema
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.74bb711f82
  command: env UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/oil_gas_pipeline.yaml
  exit_code: 0
  summary: One file, zero errors.
- check_id: C3
  name: Full native quality gates
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.74bb711f82
  command: env UV_CACHE_DIR=build/uv-cache just qc > build/review-20261009n-qc.log
    2>&1
  exit_code: 0
  summary: 648 passed,3 skipped; all native gates passed; fresh run at captured base.
- check_id: C4
  name: Ontology labels
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.74bb711f82
  command: env UV_CACHE_DIR=build/uv-cache just validate-products
  exit_code: 0
  summary: 1178 canonical,1 synonym,5 exceptions,2057 no-adapter skips; no claim of
    semantic validation.
- check_id: C5
  name: Existing structured bundles
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.74bb711f82
  command: env UV_CACHE_DIR=build/uv-cache uv run python scripts/record_review.py
    check
  exit_code: 0
  summary: 42 valid existing reviews before saving these observations.
- check_id: C6
  name: Captured input stability and full-document reproduction
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.74bb711f82
  exit_code: 0
  summary: All original50 captured hashes rechecked unchanged before expanded54-input
    native capture. In-memory full build_document equality confirmed for this target;
    source revision unchanged.
- check_id: C7
  name: Target causal-overlay and expression-module checks
  status: not_applicable
  required: false
  target_ids:
  - habitatmech:GOLD.74bb711f82
  summary: No target causal overlay or gene/expression claim; full QC still exercises
    repository-wide causal/reference gates.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/engineered/oil_gas_pipeline.yaml
  locator: Entire generated file and immediate parent files
  accessed_at: '2026-10-09T18:54:55Z'
  support: supports
  summary: ENGINEERED / UNGROUNDED / REVIEWED. Definition authored by HabitatMech
    with EXACT_SYNONYM Oil/Gas pipeline and oil and gas pipeline. Parents ENVO:03600014
    and minted Pipeline habitatmech:GOLD.edec297c39; xref ENVO:03600012. One GOLD
    source, 1 ORGANISM, nodes 8072/8073. Three history events read; no optional taxa/parameters/graphs/evidence/datasets.
- evidence_id: E2
  kind: record_content
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Exact path, node keys and related frozen inventory/decision rows
  accessed_at: '2026-10-09T18:54:55Z'
  support: supports
  summary: gold_ecosystem_paths data row 895; decisions row 696 ITEM CONFIRM_UNGROUNDED
    with xref ENVO:03600012; term_requests row 71 ADD genus ENVO:03600014; PATHS row
    2152. Exact path Engineered > Built environment > Pipeline > Oil/Gas pipeline.
    No exact frozen sample, study or triad contribution.
- evidence_id: E3
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: resolve_gold, apply_decision, apply_curated_definitions, GOLD parent pass
    and in-memory build_corpus/build_document
  accessed_at: '2026-10-09T18:54:55Z'
  support: supports
  summary: gold_unmatched -> curated_confirm_ungrounded_from_gold_unmatched. One source
    and one ITEM-reviewed source; authored ADD definition contributes the ontology
    genus, while GOLD contributes minted Pipeline. Native REVIEWED is derived correctly;
    UNGROUNDED with a genus is not itself a narrow-match endpoint defect.
- evidence_id: E4
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=site_excel
  locator: Complete streamed Biosample, Organism, SequencingProject and Study sheets
  accessed_at: '2026-10-09T18:54:55Z'
  support: partial
  summary: No exact-path BioSample or Organism rows in the complete later workbook;
    the frozen 1 ORGANISM is retained and not explained away. No exact historical
    member identity recovered. Scanned 244951/532019/636914/63806 rows respectively,
    including headers. Public Oct9 snapshot is later than frozen inputs.
  snapshot_sha256: 5f48b2f50fb2a9257754960a0f0e12dc6e8fa121e97c3e9f4497249e5fe6e439
- evidence_id: E5
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=ecosystempaths
  locator: Complete sheet census after resetting misleading A1:A1 dimensions, 2422
    rows
  accessed_at: '2026-10-09T18:54:55Z'
  support: context_only
  summary: site data row 219, GOLD8073 retains the exact Oil/Gas pipeline path. Current
    path retention is not proof of original members.
  snapshot_sha256: 3933e5f0664915c1bbfa00212e17d013da360fb33dd52e509254050813135396
- evidence_id: E6
  kind: search
  reference: curation/; history/; research/; reports/; reviews/; data/raw/
  locator: Ignored-inclusive Path.rglob traversal plus structured inventory scans
  accessed_at: '2026-10-09T18:54:55Z'
  support: context_only
  summary: Identifier/label/slug scan covered 43 curation, 224 history, 121 research,
    1274 report and 84 structured-review files. Matches include pipeline research/history
    and other-source sediment/sludge context; all 14 raw TSVs were parsed for exact
    fields and pipe-token keys. No target-owned causal overlay or extra definition
    was found except the pipeline term request. Context mentions are not new target
    coverage.
  search_scope: No gitignore filtering. All files under the five named roots were
    traversed; exact structured keys also scanned in all 14 raw and seven top-level
    curation TSVs plus PATHS. Expected GOLD_nodes.tsv/GOLD_edges.tsv/goldData.xlsx/triad
    JSON filenames separately searched under build, data/raw and local kg-microbe/data;
    unavailable there, not globally absent.
- evidence_id: E7
  kind: validation
  reference: build/review-20261009n-qc.log
  locator: Fresh full QC at captured base, focused validators and fresh label validation
  accessed_at: '2026-10-09T18:54:55Z'
  support: supports
  summary: 'QC exited0: 648 passed,3 skipped; all native gates passed, including exact
    3208-record reproduction, history, reference/corpus tests and generated site.
    Each target separately passed schema and strict validation. validate-products:1178
    canonical,1 synonym,5 exceptions,2057 no-adapter skips. Minted/MeSH skips do not
    certify parent semantics.'
- evidence_id: E8
  kind: record_content
  reference: CLAUDE.md
  locator: Semantic invariants; docs/CURATION.md; schema HabitatRecord/SourceAttestation
  accessed_at: '2026-10-09T18:54:55Z'
  support: supports
  summary: Every parent must be strictly broader, from any contribution route. Source
    counters retain their units; optional absence is not negative evidence. Generated
    ownership and ITEM-derived mapping status are preserved. Review is not native
    status promotion.
- evidence_id: S1
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO:03600014
  locator: Active ENVO:03600014 and ENVO:03600012 labels, descriptions and parent
    APIs
  accessed_at: '2026-10-09T18:54:55Z'
  support: supports
  summary: Pipeline network denotes a human construction conveying liquids or gases
    through pipes. Oil pipeline network is oil-specific with a consumer-destination
    constraint. Current terms agree with the frozen slice.
- evidence_id: S2
  kind: authority
  reference: https://www.phmsa.dot.gov/sites/phmsa.dot.gov/files/2020-06/Gathering%20Pipelines%20FAQs.pdf
  locator: Page 1, Question 1; historical terminology only
  accessed_at: '2026-10-09T18:54:55Z'
  support: supports
  summary: Gathering lines carry gases/liquids from source toward processing, refinery
    or transmission. This terminology example is not adopted as current legal guidance.
- evidence_id: S3
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2017.00099
  locator: PMC5281625 fullTextXML, Field Sample Collection; PMID 28197141
  accessed_at: '2026-10-09T18:54:55Z'
  support: supports
  summary: Pigging debris was collected from two Norwegian-sector North Sea production
    pipelines, with early/late cleaning-run samples. Supports physical pipeline-associated
    material; no universal corrosion mechanism, growth regime, taxon or gene claim
    is transferred.
- evidence_id: S4
  kind: record_content
  reference: research/habitats/engineered/oil-gas-pipeline-habitatmech-gold-74bb711f82-deep-research-claude_code.md
  locator: Definition alternatives plus two dated mapping history files
  accessed_at: '2026-10-09T18:54:55Z'
  support: supports
  summary: Research is a lead, not independent evidence. It explicitly distinguishes
    commodity from industry-sector interpretations; subsequent ITEM decision and ADD
    definition chose commodity scope. Previously corrected pipeline-term absence is
    not reopened.
assessments:
- assessment_id: A1
  area: identity
  topic: Physical habitat and source identity
  outcome: supported
  summary: Manufactured networks carrying oil/gas are physical microbial habitat contexts,
    distinct from the transport procedure, crude oil chemical or a particular pipeline
    sample. The authored commodity interpretation is supported as a plausible reading,
    not proven from the missing original member.
  target_ids:
  - habitatmech:GOLD.74bb711f82
  evidence_ids:
  - E1
  - E2
  - E4
  - S1
  - S2
  - S3
  - S4
- assessment_id: A2
  area: grounding
  topic: Exact identity versus broader/xref scope
  outcome: supported
  summary: ENVO:03600014 covers pipeline networks transporting liquids/gases. ENVO:03600012
    is oil-only and additionally specifies consumer destination, so xref rather than
    exact identity is appropriate. Petroleum-products/gas breadth is curator-authored;
    alternative industry-sector usage remains a source-scope limitation.
  target_ids:
  - habitatmech:GOLD.74bb711f82
  evidence_ids:
  - E1
  - E2
  - E3
  - S1
  - S2
  - S3
  - S4
- assessment_id: A3
  area: graph
  topic: All parent contribution routes
  outcome: supported
  summary: Both the ontology pipeline-network genus and minted generic Pipeline source
    are broader under the authored commodity interpretation. ADD retains the independent
    source parent. Neither gathering/production lines nor the primary paper justify
    a consumer-only restriction.
  target_ids:
  - habitatmech:GOLD.74bb711f82
  evidence_ids:
  - E1
  - E3
  - E8
  - S1
  - S2
  - S3
  - S4
- assessment_id: A4
  area: quantity
  topic: Attestation counts, source versions and triad roles
  outcome: supported
  summary: Frozen node IDs, collapse notes and source count/unit rendering agree with
    inventory. Current BioSample/Organism counts are not added to frozen ORGANISM
    counts, treated as independent replicates, or transferred to characteristic taxa.
    gold_ecosystem_paths data row 895; decisions row 696 ITEM CONFIRM_UNGROUNDED with
    xref ENVO:03600012; term_requests row 71 ADD genus ENVO:03600014; PATHS row 2152.
    Exact path Engineered > Built environment > Pipeline > Oil/Gas pipeline. No exact
    frozen sample, study or triad contribution.
  target_ids:
  - habitatmech:GOLD.74bb711f82
  evidence_ids:
  - E1
  - E2
  - E4
  - E5
- assessment_id: A5
  area: provenance
  topic: Native status and history
  outcome: supported
  summary: gold_unmatched -> curated_confirm_ungrounded_from_gold_unmatched. One source
    and one ITEM-reviewed source; authored ADD definition contributes the ontology
    genus, while GOLD contributes minted Pipeline. Native REVIEWED is derived correctly;
    UNGROUNDED with a genus is not itself a narrow-match endpoint defect. Saving this
    review does not alter mapping status or any scientific input.
  target_ids:
  - habitatmech:GOLD.74bb711f82
  evidence_ids:
  - E1
  - E2
  - E3
- assessment_id: A6
  area: completeness
  topic: Optional parameters, taxa, evidence, causal graphs and datasets
  outcome: supported
  summary: No target biological or mechanism claims are inferred from optional empty
    slots. Exact-key inventory scan found no target-owned environmental-parameter
    or taxon contribution; refinery triads have distinct scale/medium roles and are
    not identity evidence. Do not import study examples or infer characteristic organisms
    from source occurrence.
  target_ids:
  - habitatmech:GOLD.74bb711f82
  evidence_ids:
  - E1
  - E2
  - E6
  - E8
- assessment_id: A7
  area: evidence
  topic: Structured expression-module checks
  outcome: not_applicable
  summary: No gene, regulator, protein or transcriptomic dataset assertion in this
    target triggers an iModulonDB check. Its absence is not negative habitat evidence.
  target_ids:
  - habitatmech:GOLD.74bb711f82
  evidence_ids:
  - E1
- assessment_id: A8
  area: schema
  topic: Native gates and scientific limits
  outcome: supported
  summary: All required native checks ran successfully. Mechanical validity does not
    adjudicate scope, ontology identity or source semantics; label skips are explicit.
  target_ids:
  - habitatmech:GOLD.74bb711f82
  evidence_ids:
  - E7
findings: []
actions: []
limitations:
- Original GOLD node/edge and August bulk-export membership were not recovered in
  the bounded source-file search. The later public workbook is not a replacement for
  frozen provenance.
- All ontology/candidate and source searches are bounded. Missing source examples
  and optional fields do not establish biological absence or justify invented definitions.
- Three tests are skipped in native QC; label validation skips2057 no-adapter labels,
  including minted/MeSH scope. These deterministic checks do not certify scientific
  grounding.
notes:
- Read-only observation captured and saved before separately authorized correction/publication.
  Actions are proposals, not claims of completed fixes.
- No paid research, source refresh, native status promotion or universal physiology/taxon/mechanism
  assertion.
tags:
- habitat
- engineered
- gold
- record-review
```
