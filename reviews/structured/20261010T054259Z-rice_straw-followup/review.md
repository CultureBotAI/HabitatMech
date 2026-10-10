# Scoped publication follow-up: rice straw

- Review: 20261010T054259Z-rice_straw-followup
- Repository: culturebotai/HabitatMech
- Started UTC: 2026-10-10T05:29:38Z
- Finished UTC: 2026-10-10T05:42:59Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Resolved the later cohort substrate ambiguity without changing the habitat record: PRJNA669350 is explicitly the metagenomic dataset of soil microcosms amended with rice straw, not a pure-straw swab cohort. Soil is the sampled matrix and straw the amendment/carbon source. The separate frozen one-ORGANISM assertion remains unchanged; the later source-context grouping is not promoted to a direct straw-material observation.

## Scope And Provenance

Reassess the exact prior finding and preservation of other target claims.

Selection: Explicit successor, not a newly covered record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 34bbe5635c8c9731f2a99dd86611b7b5c6fa42ca.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| ENVO:00003870 | data/habitats/engineered/rice_straw.yaml | generated | rice straw |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Target LinkML | passed | True | ENVO:00003870 | Executed in this publication session: No issues found. |
| Strict target validation | passed | True | ENVO:00003870 | Zero errors; one rice-straw file or the three corrected targets as shown by command. |
| Reproduction | passed | True | ENVO:00003870 | 3208 expected and found; zero missing, extra or differing. |
| Focused regression | passed | True | ENVO:00003870 | 49 passed in 75.14s; test formatting-only change is AST-equivalent and the full suite also passes in V1. |
| Session history | passed | True | ENVO:00003870 | 236 valid history records. |
| Ontology labels | passed | True | ENVO:00003870 | 1178 canonical, one synonym, five accepted exceptions; 2057 rows without adapters remain disclosed. |
| Generated site | passed | True | ENVO:00003870 | 3208 habitat pages, 252 redirects, eight categories and 114 term requests match the corpus. |
| Map input and cache verification | passed | True | ENVO:00003870 | Complete source-bound map and cache verified; separate cmp and finite-point checks also passed. |
| Authoritative exact-product CI | passed | True | ENVO:00003870 | All native gates passed on 34bbe5635c8c9731f2a99dd86611b7b5c6fa42ca; 658 passed, 3 skipped in 333.56s (0:05:33). CI, not a claimed local full-QC run. |
| Earlier saved observations unchanged | passed | True | ENVO:00003870 | All original and earlier saved review bundles remain byte-identical. |
| Capture preservation | passed | True | ENVO:00003870 | Native inspect preceded follow-up assessment. Product-base recapture verifies every prior scientific input hash; only AST-equivalent test formatting is explicitly accepted. Map manifest added through inspect. |
| Causal and expression claims | not_applicable | False | ENVO:00003870 | No new causal, gene, regulator, expression or mechanism claim is introduced; a paper containing such analyses does not make those claims part of this record. |

## Scientific And Domain Assessments

### Scoped finding disposition

provenance: supported. Targets: ENVO:00003870.

Resolved the later cohort substrate ambiguity without changing the habitat record: PRJNA669350 is explicitly the metagenomic dataset of soil microcosms amended with rice straw, not a pure-straw swab cohort. Soil is the sampled matrix and straw the amendment/carbon source. The separate frozen one-ORGANISM assertion remains unchanged; the later source-context grouping is not promoted to a direct straw-material observation.

### Preserved records and generated products

consistency: supported. Targets: ENVO:00003870.

No identity, status, taxon, mechanism or source-count promotion. Native gates and generated products pass.

### Unresolved scientific boundaries

identity: unknown. Targets: ENVO:00003870.

Original source-membership limitations remain. River-water source scope (#1858), PREGO road provenance (#1859) and ontology synonym scope (#1249) are not settled by this publication.

## Findings

### F1: Resolve soil versus straw sampling in the later GOLD cohort

minor / resolved / provisional; issue key: gold-rice-straw-metagenome-soil-substrate-provenance.

The exact joined accessions SAMN16448803 and SAMN16448829 place rice straw in the host field and soil in isolation_source. GOLD labels these members decomposed rice straw. This is a real metadata discrepancy, but not yet proof of misclassification: attached straw communities, surrounding soil and experiment context must be distinguished. The isolated NRRL B-2194 evidence remains independently supportive.

Disposition: Resolved the later cohort substrate ambiguity without changing the habitat record: PRJNA669350 is explicitly the metagenomic dataset of soil microcosms amended with rice straw, not a pure-straw swab cohort. Soil is the sampled matrix and straw the amendment/carbon source. The separate frozen one-ORGANISM assertion remains unchanged; the later source-context grouping is not promoted to a direct straw-material observation.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/engineered/rice_straw.yaml; Complete target and baseline field-by-field comparison | supports | Resolved the later cohort substrate ambiguity without changing the habitat record: PRJNA669350 is explicitly the metagenomic dataset of soil microcosms amended with rice straw, not a pure-straw swab cohort. Soil is the sampled matrix and straw the amendment/carbon source. The separate frozen one-ORGANISM assertion remains unchanged; the later source-context grouping is not promoted to a direct straw-material observation. |
| E2 | docs/CURATION.md; Strict-parent, source-unit and generated-ownership rules | supports | Source context is not strict subsumption. Later biosample cohorts do not replace frozen ORGANISM attestations. Curation must preserve independently supported claims and scientific status. |
| E3 | reviews/structured/20261010T045310Z-rice_straw/review.yaml; Original findings, evidence, limitations and exact stable issue keys | supports | The original bundle remains immutable. This scoped successor resolves only the named concern and does not repeat an exhaustive scientific review of every external source. |
| V1 | https://github.com/CultureBotAI/HabitatMech/actions/runs/38027990307; Exact product commit metadata and completed authoritative QC log | supports | Verified successful scripts/run_qc.py execution on 34bbe5635c8c9731f2a99dd86611b7b5c6fa42ca: 658 passed, 3 skipped in 333.56s (0:05:33). This is CI evidence, not a fresh local full-QC execution. |
| V2 | tests/test_river_room_parent_curation.py; Whole-corpus counterfactual exclusion comparison | supports | 49 focused exclusion tests passed. Only three intended documents and their semantic text change across all 3208 records. Every other target field is unchanged; AST-equivalent import spacing was subsequently corrected. |
| V3 | https://github.com/CultureBotAI/HabitatMech/actions/runs/38027642651; Locked Linux build plus local input/cache/bundle verification | supports | Three vectors encoded; repeated canary reused all three; full embedding reused all 3208. Linux/local inputs byte-match SHA256 aaff03e9344abf2a141f7c6e000efa4848740c620edb72a3ab0c09b093306c52. All 3208 plotted identifiers are unique with finite coordinates; no records omitted. Encoder and projection settings unchanged. |
| P1 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8028251/; PMID:33827695; DOI:10.1186/s40168-021-01032-x; Methods: labeled-straw microcosms/DNA-SIP and shotgun sequencing of heavy fractions | supports | Methods identify 24 soil samples from two soils amended with rice straw; extracted soil DNA was fractionated and heavy fractions sequenced. The following sequencing section explicitly links these metagenomes to PRJNA669350. This explains the matrix/amendment distinction without asserting pure-straw sampling. |
| S1 | https://www.ebi.ac.uk/ena/browser/api/xml/PRJNA669350; Reinspected project XML, exact accession and source context | supports | Project concerns bacterial functional lineages in straw decomposition. The paper supplies the sampling matrix missing from this abbreviated project description. No new member census is claimed. |

## Limits And Additional Notes

- Scoped self-review, not independent approval or exhaustive re-review of all external evidence.
- No whole-corpus scientific approval or SSSOM/KGX readiness conclusion follows.
- Full-QC evidence is verified exact-product CI, with three skipped tests, not a fresh local full-QC execution.
- All scientific source tables and identity decisions remain unchanged; preserved claims are not newly endorsed beyond the stated scope.
- Earlier captures were explicitly checked before recapturing at the completed product commit; the one test-only formatting change has an identical Python AST. Earlier immutable bundles were not rewritten.
- The first correction-commit CI failed solely on import spacing; this was fixed and the successful V1 run covers the complete corrected product.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T054259Z-rice_straw-followup
kind: record
repository: culturebotai/HabitatMech
title: 'Scoped publication follow-up: rice straw'
started_at: '2026-10-10T05:29:38Z'
finished_at: '2026-10-10T05:42:59Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same continuing agent inspected the full record and its source
    claims; no independent reviewer approval is claimed.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Resolved the later cohort substrate ambiguity without changing the habitat
  record: PRJNA669350 is explicitly the metagenomic dataset of soil microcosms amended
  with rice straw, not a pure-straw swab cohort. Soil is the sampled matrix and straw
  the amendment/carbon source. The separate frozen one-ORGANISM assertion remains
  unchanged; the later source-context grouping is not promoted to a direct straw-material
  observation.'
source:
  git_revision: 34bbe5635c8c9731f2a99dd86611b7b5c6fa42ca
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
  - path: curation/causal_graphs/brackish_water.yaml
    sha256: b9d58082a53bef1143a3868918cfed7f6d74ba7e2330648069733d9ea2c76508
    role: context
  - path: curation/causal_graphs/building.yaml
    sha256: 9e9360775fdda554b285d7ecfb9b1729bf389b8241376a410eca60bd672eb235
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
    sha256: 09f728b498eb096296a2f50c8eb4af55b0af24c224740273b8a9c0202bdbb33c
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
  - path: data/habitats/aquatic/stream.yaml
    sha256: cef44d9573f0969784d2794c2b4d5424a496b7e972427cd5f999827412cbb097
    role: context
  - path: data/habitats/engineered/brown_waste.yaml
    sha256: 176b59732b3e345bb5045061977295c90882fcd00b3cbeb0b9933cc287391dc5
    role: context
  - path: data/habitats/engineered/built_environment.yaml
    sha256: df6de674d7d48a98b7d1d43a0a5c67a696550f00e1fb787ec71a3569acc47021
    role: context
  - path: data/habitats/engineered/hospital_bedroom.yaml
    sha256: aa42863b19a182a8011a5b44a1cbef560c3085c02b52dbd5f31fdc9516fa6953
    role: context
  - path: data/habitats/engineered/mesocosm.yaml
    sha256: e1011359d5f5291a401b1ad1b7e0dd33928453543481b1104474d7c69160a9e8
    role: context
  - path: data/habitats/engineered/research_nuclear_reactor.yaml
    sha256: 2efb65b3b767573e97e0f5765c3d09db036377b5eb2d1b0f0eba09b0c03fab71
    role: context
  - path: data/habitats/engineered/rice_straw.yaml
    sha256: faed0bc1ba7e85d92aaa0ce1f77ad876f17aed4ee05ff166969ce765c9b97f16
    role: target
  - path: data/habitats/engineered/river.yaml
    sha256: bdb5de8744c9084d7774a713d7daca3a89c14d112f8c6459acbce80efc6cb219
    role: context
  - path: data/habitats/engineered/river_water.yaml
    sha256: 54711e2906b85b77a98e396a04dcde7c55a0eb93afbf9c92a751dedfc77115b6
    role: context
  - path: data/habitats/engineered/road.yaml
    sha256: 2b532c6a6d8ba2fe1fce692f5344eebdf49d6c88f0cf34140965f9008c976e87
    role: context
  - path: data/habitats/engineered/room_surface.yaml
    sha256: c423c3841ff81602a76ce52093a46f59810cf6dcc8373ef33fec627d785fd35a
    role: context
  - path: data/habitats/engineered/waste_water.yaml
    sha256: 774c88de3169fb8ae95ea05deb748f21e036a35d0b21734c81c228493ec96056
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
  - path: data/text_map/8c15133429d1fd81fb394a00be0542d55f5cdb8c24c1dbc3923edbcb582faba8/manifest.json
    sha256: 1629a4ee439c63e960b17172b9ce56c03aec79cdfe3fee34e60eadad8b3b6ef4
    role: context
  - path: data/text_map/current.json
    sha256: ffac51fb17c83d5843a5f35ca7dc8c024291dd8c83b45cc3b01423a4c0d04c44
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
  - path: history/mappings/river/2026-10-10T052811Z-codex-gpt-5-f5d017.yaml
    sha256: c32b9ce8e4a3752c6c832101ff30013cfe633febeb1a90ef623a28759585a58b
    role: context
  - path: history/mappings/river_water/2026-10-10T052812Z-codex-gpt-5-3d6036.yaml
    sha256: 763812b4d774be17d031f4c23ccad339f4df34d1fa055598d0f51cc90af455f7
    role: context
  - path: history/mappings/room_surface/2026-10-10T052813Z-codex-gpt-5-a1da50.yaml
    sha256: b581c48d56de149bab0a450c8211fcc451eef14f0587c982571679b1a155b1e5
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reviews/structured/20261010T040432Z-railway/review.md
    sha256: 558ad0e675ad1b987f4e958d6bb575044721b87f5202228644c216e525317b65
    role: context
  - path: reviews/structured/20261010T040432Z-railway/review.yaml
    sha256: 7fab5018b7d7fc31bac188f190a430f35ee51822a5cc637521b7759591c13d80
    role: context
  - path: reviews/structured/20261010T045310Z-rice_straw/review.md
    sha256: 4d0e325215ffa35638e568af65ee8ca74c1a67037ed1312609e39646fcc01b8d
    role: context
  - path: reviews/structured/20261010T045310Z-rice_straw/review.yaml
    sha256: 0c3598b2f7134038147c93af1995902a1c37f99691cee44fd747000ef01b8d33
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
  - path: tests/test_river_room_parent_curation.py
    sha256: 16f2ca657c6e98c51634e237ce356ada7f653c4944f0f581212dfaf495aa9a69
    role: context
targets:
- target_id: ENVO:00003870
  path: data/habitats/engineered/rice_straw.yaml
  label: rice straw
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/decisions.tsv
    role: source identity and item-level review decisions
  - repository: culturebotai/HabitatMech
    path: curation/term_requests.tsv
    role: authored label/definition and genus
  - repository: culturebotai/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: guarded GOLD context-parent exclusions
  - repository: culturebotai/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: frozen GOLD source paths and organism counts
  - repository: culturebotai/HabitatMech
    path: data/raw/gold_path_biosamples.tsv
    role: later source-classified BIOSAMPLE counts
  - repository: culturebotai/HabitatMech
    path: data/raw/gold_studies.tsv
    role: study/path relationships
  - repository: culturebotai/HabitatMech
    path: scripts/extract_gold_biosamples.py
    role: source sample/study extraction
  - repository: culturebotai/HabitatMech
    path: data/raw/prego_habitats.tsv
    role: PREGO habitat and taxon count summary
  - repository: culturebotai/HabitatMech
    path: data/raw/prego_habitat_taxa.tsv
    role: ranked taxon association scores and channels
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: generated records
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/extract.py
    role: source inventory extraction
  - repository: culturebotai/HabitatMech
    path: data/habitats/PATHS.tsv
    role: stable identifier-to-slug mapping
scope:
  description: Reassess the exact prior finding and preservation of other target claims.
  selection: Explicit successor, not a newly covered record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - ENVO:00003870
  exclusions:
  - target: New complete source census and unrelated habitat curation
    reason: Bounded publication follow-up.
checks:
- check_id: C1
  name: Target LinkML
  command: just validate data/habitats/engineered/rice_straw.yaml
  status: passed
  required: true
  exit_code: 0
  summary: 'Executed in this publication session: No issues found.'
  target_ids:
  - ENVO:00003870
- check_id: C2
  name: Strict target validation
  command: uv run python scripts/validate_strict.py data/habitats/engineered/rice_straw.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Zero errors; one rice-straw file or the three corrected targets as shown
    by command.
  target_ids:
  - ENVO:00003870
- check_id: C3
  name: Reproduction
  command: just verify-corpus
  status: passed
  required: true
  exit_code: 0
  summary: 3208 expected and found; zero missing, extra or differing.
  target_ids:
  - ENVO:00003870
- check_id: C4
  name: Focused regression
  command: uv run pytest -q tests/test_river_room_parent_curation.py tests/test_gold_parent_exclusions.py
  status: passed
  required: true
  exit_code: 0
  summary: 49 passed in 75.14s; test formatting-only change is AST-equivalent and
    the full suite also passes in V1.
  target_ids:
  - ENVO:00003870
- check_id: C5
  name: Session history
  command: just validate-history
  status: passed
  required: true
  exit_code: 0
  summary: 236 valid history records.
  target_ids:
  - ENVO:00003870
- check_id: C6
  name: Ontology labels
  command: just validate-products
  status: passed
  required: true
  exit_code: 0
  summary: 1178 canonical, one synonym, five accepted exceptions; 2057 rows without
    adapters remain disclosed.
  target_ids:
  - ENVO:00003870
- check_id: C7
  name: Generated site
  command: just render-check
  status: passed
  required: true
  exit_code: 0
  summary: 3208 habitat pages, 252 redirects, eight categories and 114 term requests
    match the corpus.
  target_ids:
  - ENVO:00003870
- check_id: C8
  name: Map input and cache verification
  command: uv run python scripts/embedding_pipeline.py check --output build/pr1854-map-download/data/text_map
    --input build/text-map/pr1854-inputs.jsonl --cache build/pr1854-map-download/build/text-map/vectors.sqlite
  status: passed
  required: true
  exit_code: 0
  summary: Complete source-bound map and cache verified; separate cmp and finite-point
    checks also passed.
  target_ids:
  - ENVO:00003870
- check_id: C9
  name: Authoritative exact-product CI
  command: gh run view 38027990307 --log
  status: passed
  required: true
  exit_code: 0
  summary: All native gates passed on 34bbe5635c8c9731f2a99dd86611b7b5c6fa42ca; 658
    passed, 3 skipped in 333.56s (0:05:33). CI, not a claimed local full-QC run.
  target_ids:
  - ENVO:00003870
- check_id: C10
  name: Earlier saved observations unchanged
  command: git diff bd20d0459 --exit-code -- reviews/structured
  status: passed
  required: true
  exit_code: 0
  summary: All original and earlier saved review bundles remain byte-identical.
  target_ids:
  - ENVO:00003870
- check_id: C11
  name: Capture preservation
  command: uv run python /private/tmp/habitatmech-pr1854-capture.py
  status: passed
  required: true
  exit_code: 0
  summary: Native inspect preceded follow-up assessment. Product-base recapture verifies
    every prior scientific input hash; only AST-equivalent test formatting is explicitly
    accepted. Map manifest added through inspect.
  target_ids:
  - ENVO:00003870
- check_id: C12
  name: Causal and expression claims
  status: not_applicable
  required: false
  target_ids:
  - ENVO:00003870
  summary: No new causal, gene, regulator, expression or mechanism claim is introduced;
    a paper containing such analyses does not make those claims part of this record.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/engineered/rice_straw.yaml
  locator: Complete target and baseline field-by-field comparison
  accessed_at: '2026-10-10T05:42:59Z'
  support: supports
  summary: 'Resolved the later cohort substrate ambiguity without changing the habitat
    record: PRJNA669350 is explicitly the metagenomic dataset of soil microcosms amended
    with rice straw, not a pure-straw swab cohort. Soil is the sampled matrix and
    straw the amendment/carbon source. The separate frozen one-ORGANISM assertion
    remains unchanged; the later source-context grouping is not promoted to a direct
    straw-material observation.'
- evidence_id: E2
  kind: authority
  reference: docs/CURATION.md
  locator: Strict-parent, source-unit and generated-ownership rules
  accessed_at: '2026-10-10T05:42:59Z'
  support: supports
  summary: Source context is not strict subsumption. Later biosample cohorts do not
    replace frozen ORGANISM attestations. Curation must preserve independently supported
    claims and scientific status.
- evidence_id: E3
  kind: prior_review
  reference: reviews/structured/20261010T045310Z-rice_straw/review.yaml
  locator: Original findings, evidence, limitations and exact stable issue keys
  accessed_at: '2026-10-10T05:42:59Z'
  support: supports
  summary: The original bundle remains immutable. This scoped successor resolves only
    the named concern and does not repeat an exhaustive scientific review of every
    external source.
- evidence_id: V1
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38027990307
  locator: Exact product commit metadata and completed authoritative QC log
  accessed_at: '2026-10-10T05:42:59Z'
  support: supports
  summary: 'Verified successful scripts/run_qc.py execution on 34bbe5635c8c9731f2a99dd86611b7b5c6fa42ca:
    658 passed, 3 skipped in 333.56s (0:05:33). This is CI evidence, not a fresh local
    full-QC execution.'
- evidence_id: V2
  kind: validation
  reference: tests/test_river_room_parent_curation.py
  locator: Whole-corpus counterfactual exclusion comparison
  accessed_at: '2026-10-10T05:42:59Z'
  support: supports
  summary: 49 focused exclusion tests passed. Only three intended documents and their
    semantic text change across all 3208 records. Every other target field is unchanged;
    AST-equivalent import spacing was subsequently corrected.
- evidence_id: V3
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38027642651
  locator: Locked Linux build plus local input/cache/bundle verification
  accessed_at: '2026-10-10T05:42:59Z'
  support: supports
  summary: Three vectors encoded; repeated canary reused all three; full embedding
    reused all 3208. Linux/local inputs byte-match SHA256 aaff03e9344abf2a141f7c6e000efa4848740c620edb72a3ab0c09b093306c52.
    All 3208 plotted identifiers are unique with finite coordinates; no records omitted.
    Encoder and projection settings unchanged.
- evidence_id: P1
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC8028251/
  locator: 'PMID:33827695; DOI:10.1186/s40168-021-01032-x; Methods: labeled-straw
    microcosms/DNA-SIP and shotgun sequencing of heavy fractions'
  accessed_at: '2026-10-10T05:42:59Z'
  support: supports
  summary: Methods identify 24 soil samples from two soils amended with rice straw;
    extracted soil DNA was fractionated and heavy fractions sequenced. The following
    sequencing section explicitly links these metagenomes to PRJNA669350. This explains
    the matrix/amendment distinction without asserting pure-straw sampling.
- evidence_id: S1
  kind: database
  reference: https://www.ebi.ac.uk/ena/browser/api/xml/PRJNA669350
  locator: Reinspected project XML, exact accession and source context
  accessed_at: '2026-10-10T05:42:59Z'
  support: supports
  summary: Project concerns bacterial functional lineages in straw decomposition.
    The paper supplies the sampling matrix missing from this abbreviated project description.
    No new member census is claimed.
assessments:
- assessment_id: A1
  area: provenance
  topic: Scoped finding disposition
  outcome: supported
  summary: 'Resolved the later cohort substrate ambiguity without changing the habitat
    record: PRJNA669350 is explicitly the metagenomic dataset of soil microcosms amended
    with rice straw, not a pure-straw swab cohort. Soil is the sampled matrix and
    straw the amendment/carbon source. The separate frozen one-ORGANISM assertion
    remains unchanged; the later source-context grouping is not promoted to a direct
    straw-material observation.'
  target_ids:
  - ENVO:00003870
  evidence_ids:
  - E1
  - E2
  - E3
  - P1
- assessment_id: A2
  area: consistency
  topic: Preserved records and generated products
  outcome: supported
  summary: No identity, status, taxon, mechanism or source-count promotion. Native
    gates and generated products pass.
  target_ids:
  - ENVO:00003870
  evidence_ids:
  - V1
  - V2
  - V3
- assessment_id: A3
  area: identity
  topic: Unresolved scientific boundaries
  outcome: unknown
  summary: Original source-membership limitations remain. River-water source scope
    (#1858), PREGO road provenance (#1859) and ontology synonym scope (#1249) are
    not settled by this publication.
  target_ids:
  - ENVO:00003870
  evidence_ids:
  - E3
findings:
- issue_key: gold-rice-straw-metagenome-soil-substrate-provenance
  severity: minor
  certainty: provisional
  category: provenance
  title: Resolve soil versus straw sampling in the later GOLD cohort
  description: 'The exact joined accessions SAMN16448803 and SAMN16448829 place rice
    straw in the host field and soil in isolation_source. GOLD labels these members
    decomposed rice straw. This is a real metadata discrepancy, but not yet proof
    of misclassification: attached straw communities, surrounding soil and experiment
    context must be distinguished. The isolated NRRL B-2194 evidence remains independently
    supportive.'
  field_paths:
  - source_attestations
  evidence_ids:
  - E1
  - E2
  - E3
  - P1
  - V1
  - V2
  finding_id: F1
  status: resolved
  target_ids:
  - ENVO:00003870
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: data/raw/gold_path_biosamples.tsv
    role: Maintained input or source transformation; generated habitat YAML is read-only
  - repository: culturebotai/HabitatMech
    path: data/raw/gold_studies.tsv
    role: Maintained input or source transformation; generated habitat YAML is read-only
  - repository: culturebotai/HabitatMech
    path: scripts/extract_gold_biosamples.py
    role: Maintained input or source transformation; generated habitat YAML is read-only
  native_severity: minor
  rule_id: Native strict-parent, source-equivalence and scoped-provenance rules
  normalization_reason: False strict parents and unresolved material identity are
    major; bounded source-substrate provenance discrepancies without a proved false
    identity are minor. Certainty is recorded separately from severity.
  previous_occurrences:
  - repository: culturebotai/HabitatMech
    review_id: 20261010T045310Z-rice_straw
    finding_id: F1
  disposition_reason: 'Resolved the later cohort substrate ambiguity without changing
    the habitat record: PRJNA669350 is explicitly the metagenomic dataset of soil
    microcosms amended with rice straw, not a pure-straw swab cohort. Soil is the
    sampled matrix and straw the amendment/carbon source. The separate frozen one-ORGANISM
    assertion remains unchanged; the later source-context grouping is not promoted
    to a direct straw-material observation.'
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1855
actions: []
limitations:
- Scoped self-review, not independent approval or exhaustive re-review of all external
  evidence.
- No whole-corpus scientific approval or SSSOM/KGX readiness conclusion follows.
- Full-QC evidence is verified exact-product CI, with three skipped tests, not a fresh
  local full-QC execution.
- All scientific source tables and identity decisions remain unchanged; preserved
  claims are not newly endorsed beyond the stated scope.
notes:
- Earlier captures were explicitly checked before recapturing at the completed product
  commit; the one test-only formatting change has an identical Python AST. Earlier
  immutable bundles were not rewritten.
- The first correction-commit CI failed solely on import spacing; this was fixed and
  the successful V1 run covers the complete corrected product.
related_reviews:
- repository: culturebotai/HabitatMech
  review_id: 20261010T045310Z-rice_straw
  relationship: Resolves F1 only; any additional original finding remains explicit.
links:
- https://github.com/CultureBotAI/HabitatMech/issues/1855
- https://github.com/CultureBotAI/HabitatMech/pull/1854
tags:
- habitatmech
- followup
- publication-review
```
