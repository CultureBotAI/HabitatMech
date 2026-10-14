# Scientific record review: Transient pool

- Review: 20261014T044034Z-transient_pool
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-14T04:26:49.055542Z
- Finished UTC: 2026-10-14T04:40:34.481078Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The freshwater transient-pool source retains its minted identity without the old liquid-fresh-water parent. Both collapsed nodes, zero-count omission and CLASS/SEEDED provenance reproduce. Water-body versus periodically filled basin remains a bounded definition question, not a reason to guess an exact term.

## Scope And Provenance

One entire generated HabitatRecord and all contributing source concepts; parent records are bounded hierarchy context, not additional review targets.

Selection: Next eight uncovered aquatic paths in stable path order; this bundle assesses exactly one target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base db6301fe65eb3f419dfb2338f029ca2c269cdbef.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.d39a2ed099 | data/habitats/aquatic/transient_pool.yaml | generated | Transient pool |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native validation | passed | True | habitatmech:GOLD.d39a2ed099 | Actual exit 0 from 2026-10-14T04:29:24.782010Z to 2026-10-14T04:29:30.569152Z; record-specific or corpus-wide scope retained. |
| Native validation | passed | True | habitatmech:GOLD.d39a2ed099 | Actual exit 0 from 2026-10-14T04:29:30.570138Z to 2026-10-14T04:29:41.569723Z; record-specific or corpus-wide scope retained. |
| Native validation | passed | True | habitatmech:GOLD.d39a2ed099 | Actual exit 0 from 2026-10-14T04:29:41.570709Z to 2026-10-14T04:29:58.524103Z; record-specific or corpus-wide scope retained. |
| Native validation | passed | True | habitatmech:GOLD.d39a2ed099 | Actual exit 0 from 2026-10-14T04:29:58.525052Z to 2026-10-14T04:29:59.690953Z; record-specific or corpus-wide scope retained. |
| Native validation | passed | True | habitatmech:GOLD.d39a2ed099 | Actual exit 0 from 2026-10-14T04:29:59.691992Z to 2026-10-14T04:30:56.467533Z; record-specific or corpus-wide scope retained. |
| Native validation | passed | True | habitatmech:GOLD.d39a2ed099 | Actual exit 0 from 2026-10-14T04:30:56.468642Z to 2026-10-14T04:31:07.015136Z; record-specific or corpus-wide scope retained. |
| Native validation | passed | True | habitatmech:GOLD.d39a2ed099 | Actual exit 0 from 2026-10-14T04:31:07.016135Z to 2026-10-14T04:31:55.507763Z; record-specific or corpus-wide scope retained. |
| Native ontology label correspondence | passed | True | habitatmech:GOLD.d39a2ed099 | Executed during this assessment: 1178 canonical, 1 synonym, 5 accepted exceptions, 2057 configured no-adapter skips. The gate does not assess occurrence, source labels or NCBI pairs; those are separately scoped. |
| Complete target-document equality and captured hash checks | passed | True | habitatmech:GOLD.d39a2ed099 | Compared native build_corpus/build_document with each complete target and rechecked captured hashes; this is a diagnostic complement to the native whole-corpus reproduction gate. |
| Exact-base authoritative hosted QC | passed | True | habitatmech:GOLD.d39a2ed099 | Verified successful authoritative CI on the exact unchanged scientific-input base; not a new local full-QC run or validation of these newly saved bundles. |
| Expression-module adapter | not_applicable | False | habitatmech:GOLD.d39a2ed099 | No gene, regulator, protein or expression-module assertion occurs in this target. iModulonDB is not applicable; non-use is not negative evidence. |

## Scientific And Domain Assessments

### Exact entity and strictly broader hierarchy

identity: supported. Targets: habitatmech:GOLD.d39a2ed099.

GOLD8268/8269 denotes the freshwater transient-pool source. A water body or its intermittently filled depression is not ENVO:00002011 water material, and exclusion row 146 already suppresses that context contribution. CLASS row 1169 preserves UNGROUNDED/SEEDED; neither this review nor the exclusion creates ITEM status. The separate Microbial mat child has also had its pool-context edge excluded; its remaining endpoint question is not a target finding.

### Source units, membership, MIxS roles and status

provenance: supported. Targets: habitatmech:GOLD.d39a2ed099.

gold_ecosystem_paths row 1498 contains two collapsed nodes and zero direct counters. The first node and collapse note are retained without a fabricated count/unit. The current terminal-path workbook confirms8269, not the historical internal node 8268; the latter is checked only against the frozen inventory. The bounded structured inventory search found no target-specific bulk biosample, triad or study row.

### Bounded scientific support and optional content

evidence: supported. Targets: habitatmech:GOLD.d39a2ed099.

EPA's seasonal-pool manual distinguishes periodically wet and dry habitats from the water material filling them. It supports the excluded material edge, but does not equate every GOLD transient pool with a seasonal vernal basin or specify a universal hydroperiod, size, taxa or substrate. The undefined basin-versus-water-body scope remains explicit; no unsupported definition, genus, environmental measurement or mechanism is invented.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| RECORD | data/habitats/aquatic/transient_pool.yaml | supports | Entire YAML inspected, including all sources, associations and historical events. The freshwater transient-pool source retains its minted identity without the old liquid-fresh-water parent. Both collapsed nodes, zero-count omission and CLASS/SEEDED provenance reproduce. Water-body versus periodically filled basin remains a bounded definition question, not a reason to guess an exact term. |
| RAW | data/raw/gold_ecosystem_paths.tsv:1498; curation/gold_parent_exclusions.tsv:146; curation/decisions.tsv:1169 | supports | gold_ecosystem_paths row 1498 contains two collapsed nodes and zero direct counters. The first node and collapse note are retained without a fabricated count/unit. The current terminal-path workbook confirms8269, not the historical internal node 8268; the latter is checked only against the frozen inventory. The bounded structured inventory search found no target-specific bulk biosample, triad or study row. |
| OWNERS | curation/decisions.tsv; curation/gold_parent_exclusions.tsv; curation/term_requests.tsv; src/habitatmech/seed.py; src/habitatmech/extract.py | supports | Inspected maintained rows and source construction, ontology-synonym promotion, source counts, ranking and lifecycle. Full build_corpus/build_document equality passed for this record; every captured input hash was rechecked unchanged. Reproduction is not scientific approval. |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; docs/record-review-profile.md; src/habitatmech/schema/habitatmech.yaml | supports | Applied the native record rubric: entity identity, strictly broader genus, typed synonyms, source/count units, MIxS roles, taxon association versus characteristic presence, and ITEM versus CLASS lifecycle. |
| SEARCH | curation; history; research; conf; reviews/structured; reports/yaml_record_review; data/raw | supports | Bounded rg --no-ignore --hidden searches used exact identifier, source IDs/mints, label and slug. Structured TSV and recursive review inventories are also gitignore-independent. Legacy reports were read as leads and compared against current maintained changes; no legacy finding is silently retired by this new observation. Original source membership matrices were not reconstructed, and no global absence claim is made. |
| ENVO | https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl; Named classes ENVO:00002011 | supports | Official current envo.owl file commit a2455d1a77e46bb8a664d65a157166b539269042, SHA256 a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c. Inspected active class definitions against the assessments, named parents and typed synonyms. Relevant labels and scoped aliases: {"ENVO:00002011": {"label": "fresh water", "synonyms": {"hasExactSynonym": ["freshwater"], "hasBroadSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": ["sweet water"]}, "parents": ["http://purl.obolibrary.org/obo/ENVO_00002006"]}} |
| BASE_QC | https://github.com/CultureBotAI/HabitatMech/actions/runs/38341318428 | supports | Fresh gh run view confirmed success on exact unchanged base db6301fe65eb3f419dfb2338f029ca2c269cdbef. Its actual log records 1060 tests passed, 3 skipped and all native quality gates. This existing run checks the captured scientific inputs, not the new review files; full QC was not rerun locally for review-only additions. |
| GOLD | https://gold.jgi.doe.gov/download?mode=ecosystempaths; Workbook row656 | supports | Fresh complete workbook parsed with incorrect worksheet dimensions reset;2422 rows including header. Exact path row: ["8269", "Environmental", "Aquatic", "Freshwater", "Transient pool", "Unclassified"]. SHA256 f13652be516a0f1482bf0abbb44d7d8e9acb17c5d401cd7e0474af949b447611. A terminal-path listing verifies this vocabulary row, not every collapsed historical internal node, sample count or ecological property. |
| GOLD_SCOPE | https://gold.jgi.doe.gov/ecosystem_classification; Classification purpose and five-level descriptions | context_only | GOLD describes sample surroundings using a sample-driven classification. Source path depth alone does not establish a strict ontology subclass or exact habitat equivalence. |
| EPA | https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P1002R0O.TXT; EPA/903/B-05/001, abstract and introduction | context_only | The manual treats periodic inundation/drying as habitat properties, not identity with fresh-water material. Regional seasonal-pool criteria do not establish every transient-pool class boundary. |

## Limits And Additional Notes

- Same-agent review, not independent approval or full-corpus certification.
- Original upstream source membership matrices and study-to-sample crosswalks were not reconstructed. Frozen source counters reproduce; live taxonomy verifies identity, not occurrence. Public GOLD terminal paths do not independently verify every historical internal node.
- Native label validation retains 5 configured accepted exceptions and 2057 no-adapter skips; these are not scientific approvals.
- Parent records are inspected for relevant hierarchy/interpretation only. Their unrelated taxa, parameters and causal evidence are not inherited or re-reviewed here.
- Legacy reports are historical leads, not structured disposition lineage. Corrected hierarchy findings are described as current state without silently closing old findings.
- PMC browser challenge and intermittent publisher HTML errors were encountered; primary-paper PDFs or publisher/institutional text were inspected instead. GOLD resources URL was inaccessible; the classification page and workbook were accessible.
- No habitat, decision, source, history, scientific status, generated page or map is changed. Browser visual QA and SSSOM/KGX conformance are outside this record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T044034Z-transient_pool
kind: record
repository: CultureBotAI/HabitatMech
title: 'Scientific record review: Transient pool'
started_at: '2026-10-14T04:26:49.055542Z'
finished_at: '2026-10-14T04:40:34.481078Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Same agent participated in repository work; this is not independent
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
scientific_review: true
verdict: pass_with_limitations
summary: The freshwater transient-pool source retains its minted identity without
  the old liquid-fresh-water parent. Both collapsed nodes, zero-count omission and
  CLASS/SEEDED provenance reproduce. Water-body versus periodically filled basin remains
  a bounded definition question, not a reason to guess an exact term.
source:
  git_revision: db6301fe65eb3f419dfb2338f029ca2c269cdbef
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
    sha256: eb82cec48508912622b452ae78bb1ad199c93cb0591ce534bb8f25273da4e220
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 2d41fc93db4939122b3909f2a412b84b679703948b10d9f02e12021442f71407
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: c7017ce7889ebfce889eb6f2c6a6c12510428be4b8a4370e2e4e165231e1af25
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: 331a7d9eb8a8909fc37402c0a776838979a8065644504d5c4f2a1c39bce5c24d
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: b59b9e800a918135e3915145d4d8098bb48dcea36a312b3004c594a57d221ae9
    role: context
  - path: data/habitats/aquatic/fresh_water.yaml
    sha256: 99bd93c6173c2ccf7b59645a131ae41c88c45246b45265034a8275053b3745b7
    role: context
  - path: data/habitats/aquatic/hot_42_90c.yaml
    sha256: 3e065fa083097833b536fdd2172e5eba3b92d9fbfd27801530cb3dd3025f25e7
    role: context
  - path: data/habitats/aquatic/hot_spring.yaml
    sha256: ffee4f6aa076c707582be0110182034054f2fc53c481d18bcc866254080e2ad4
    role: context
  - path: data/habitats/aquatic/intertidal_zone__2f295854.yaml
    sha256: e1539f56318f217f73b976e738d5fd560935e613a5cfd7a954eaaa3f0ccb53f2
    role: context
  - path: data/habitats/aquatic/microbial_mat__2020a793.yaml
    sha256: 527a3d31661b1b6d7e4892eede7ec18ca327f1b5bb07536cc7101b2a48c235b1
    role: context
  - path: data/habitats/aquatic/microbialites__a38bc21d.yaml
    sha256: db0f4de03cb1b4555d87f4085f319fa9e8d7f2228f963bc482bf5ec9588a972b
    role: context
  - path: data/habitats/aquatic/near_boiling_90c__f7b76591.yaml
    sha256: 289ecf5ddd0e6989c0f62b2d467e9a1ccf6eb8b0fbe3706277ed8af8b7fabe0f
    role: context
  - path: data/habitats/aquatic/transient_pool.yaml
    sha256: f539a42b963df2767d657afc035c09ed10722c87bae008b6abe4860e6a3f87e2
    role: target
  - path: data/habitats/aquatic/warm_34_42c.yaml
    sha256: 04b990970bc30486accf32ec76eddc261f5f738d31296265e70a3d350a816625
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
    sha256: 105b3c8e10f43ce689b05d3089d3a8be1d713a98dd6806e11be37ebd85b10590
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/mappings/thalassic/2026-10-06T172112Z-claude-code-3c90c3.yaml
    sha256: b5ab5b115c4e7832f5c8f7ba402dc681b7ddd3dd39832d1c325815fb1050bdea
    role: context
  - path: history/mappings/thrombolites/2026-10-06T172127Z-claude-code-8f8722.yaml
    sha256: a4b965be126acc17504f89ab930126bb518f64162215138e42d59a2a4a92f252
    role: context
  - path: history/mappings/transient_pool/2026-10-06T183149Z-codex-gpt-5-00b35f.yaml
    sha256: b632d9ad96f91a96f80b7fccdb7a26442a880426efb98493b2bfacc2639e8156
    role: context
  - path: history/other/thalassic_thrombolites_actor_correction/2026-10-06T172327Z-codex-gpt-5-76d614.yaml
    sha256: 8dad97f34fdf44f976be30e563b73c14e82e085737bb020ad8756abe303e83c9
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20261006T181259Z-transient_pool.md
    sha256: dd92b5ef9f9d99e3d60d7c53b63b281c75d89002707a342bdbba1c486fa46005
    role: context
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
    role: context
  - path: src/habitatmech/seed.py
    sha256: 4adf105e23d75c3563a516a0c160623d1065df7fcb2f31b7a0a0a8303d0401be
    role: context
targets:
- target_id: habitatmech:GOLD.d39a2ed099
  path: data/habitats/aquatic/transient_pool.yaml
  label: Transient pool
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Grounding and ITEM review
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Authored definition and genus
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Exact source context-parent exclusions
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Pinned ontology term assertions
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_subclass_edges.tsv
    role: Pinned ontology hierarchy
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Record generation and source harmonization
scope:
  description: One entire generated HabitatRecord and all contributing source concepts;
    parent records are bounded hierarchy context, not additional review targets.
  selection: Next eight uncovered aquatic paths in stable path order; this bundle
    assesses exactly one target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.d39a2ed099
checks:
- check_id: C0
  name: Native validation
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.d39a2ed099
  command: just validate data/habitats/aquatic/transient_pool.yaml
  exit_code: 0
  summary: Actual exit 0 from 2026-10-14T04:29:24.782010Z to 2026-10-14T04:29:30.569152Z;
    record-specific or corpus-wide scope retained.
- check_id: C1
  name: Native validation
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.d39a2ed099
  command: just validate-strict data/habitats/aquatic/transient_pool.yaml
  exit_code: 0
  summary: Actual exit 0 from 2026-10-14T04:29:30.570138Z to 2026-10-14T04:29:41.569723Z;
    record-specific or corpus-wide scope retained.
- check_id: C2
  name: Native validation
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.d39a2ed099
  command: just validate-history
  exit_code: 0
  summary: Actual exit 0 from 2026-10-14T04:29:41.570709Z to 2026-10-14T04:29:58.524103Z;
    record-specific or corpus-wide scope retained.
- check_id: C3
  name: Native validation
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.d39a2ed099
  command: just provenance-check
  exit_code: 0
  summary: Actual exit 0 from 2026-10-14T04:29:58.525052Z to 2026-10-14T04:29:59.690953Z;
    record-specific or corpus-wide scope retained.
- check_id: C4
  name: Native validation
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.d39a2ed099
  command: just verify-corpus
  exit_code: 0
  summary: Actual exit 0 from 2026-10-14T04:29:59.691992Z to 2026-10-14T04:30:56.467533Z;
    record-specific or corpus-wide scope retained.
- check_id: C5
  name: Native validation
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.d39a2ed099
  command: just validate-causal-all
  exit_code: 0
  summary: Actual exit 0 from 2026-10-14T04:30:56.468642Z to 2026-10-14T04:31:07.015136Z;
    record-specific or corpus-wide scope retained.
- check_id: C6
  name: Native validation
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.d39a2ed099
  command: just term-requests-check
  exit_code: 0
  summary: Actual exit 0 from 2026-10-14T04:31:07.016135Z to 2026-10-14T04:31:55.507763Z;
    record-specific or corpus-wide scope retained.
- check_id: LABELS
  name: Native ontology label correspondence
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.d39a2ed099
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  summary: 'Executed during this assessment: 1178 canonical, 1 synonym, 5 accepted
    exceptions, 2057 configured no-adapter skips. The gate does not assess occurrence,
    source labels or NCBI pairs; those are separately scoped.'
- check_id: REPRO
  name: Complete target-document equality and captured hash checks
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.d39a2ed099
  command: .venv/bin/python /private/tmp/habitatmech-review-bk.py crosscheck
  exit_code: 0
  summary: Compared native build_corpus/build_document with each complete target and
    rechecked captured hashes; this is a diagnostic complement to the native whole-corpus
    reproduction gate.
- check_id: QC
  name: Exact-base authoritative hosted QC
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.d39a2ed099
  command: gh run view 38341318428 --json headSha,conclusion,status,url,jobs
  exit_code: 0
  evidence_ids:
  - BASE_QC
  summary: Verified successful authoritative CI on the exact unchanged scientific-input
    base; not a new local full-QC run or validation of these newly saved bundles.
- check_id: IMOD
  name: Expression-module adapter
  required: false
  status: not_applicable
  target_ids:
  - habitatmech:GOLD.d39a2ed099
  summary: No gene, regulator, protein or expression-module assertion occurs in this
    target. iModulonDB is not applicable; non-use is not negative evidence.
evidence:
- evidence_id: RECORD
  kind: record_content
  reference: data/habitats/aquatic/transient_pool.yaml
  accessed_at: '2026-10-14T04:40:34.480722Z'
  support: supports
  summary: Entire YAML inspected, including all sources, associations and historical
    events. The freshwater transient-pool source retains its minted identity without
    the old liquid-fresh-water parent. Both collapsed nodes, zero-count omission and
    CLASS/SEEDED provenance reproduce. Water-body versus periodically filled basin
    remains a bounded definition question, not a reason to guess an exact term.
- evidence_id: RAW
  kind: record_content
  reference: data/raw/gold_ecosystem_paths.tsv:1498; curation/gold_parent_exclusions.tsv:146;
    curation/decisions.tsv:1169
  accessed_at: '2026-10-14T04:40:34.480722Z'
  support: supports
  summary: gold_ecosystem_paths row 1498 contains two collapsed nodes and zero direct
    counters. The first node and collapse note are retained without a fabricated count/unit.
    The current terminal-path workbook confirms8269, not the historical internal node
    8268; the latter is checked only against the frozen inventory. The bounded structured
    inventory search found no target-specific bulk biosample, triad or study row.
- evidence_id: OWNERS
  kind: record_content
  reference: curation/decisions.tsv; curation/gold_parent_exclusions.tsv; curation/term_requests.tsv;
    src/habitatmech/seed.py; src/habitatmech/extract.py
  accessed_at: '2026-10-14T04:40:34.480722Z'
  support: supports
  summary: Inspected maintained rows and source construction, ontology-synonym promotion,
    source counts, ranking and lifecycle. Full build_corpus/build_document equality
    passed for this record; every captured input hash was rechecked unchanged. Reproduction
    is not scientific approval.
- evidence_id: RULES
  kind: record_content
  reference: docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; docs/record-review-profile.md;
    src/habitatmech/schema/habitatmech.yaml
  accessed_at: '2026-10-14T04:40:34.480722Z'
  support: supports
  summary: 'Applied the native record rubric: entity identity, strictly broader genus,
    typed synonyms, source/count units, MIxS roles, taxon association versus characteristic
    presence, and ITEM versus CLASS lifecycle.'
- evidence_id: SEARCH
  kind: record_content
  reference: curation; history; research; conf; reviews/structured; reports/yaml_record_review;
    data/raw
  accessed_at: '2026-10-14T04:26:16.197845Z'
  support: supports
  summary: Bounded rg --no-ignore --hidden searches used exact identifier, source
    IDs/mints, label and slug. Structured TSV and recursive review inventories are
    also gitignore-independent. Legacy reports were read as leads and compared against
    current maintained changes; no legacy finding is silently retired by this new
    observation. Original source membership matrices were not reconstructed, and no
    global absence claim is made.
- evidence_id: ENVO
  kind: database
  reference: https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl
  accessed_at: '2026-10-14T04:28:47.463855Z'
  locator: Named classes ENVO:00002011
  support: supports
  summary: 'Official current envo.owl file commit a2455d1a77e46bb8a664d65a157166b539269042,
    SHA256 a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c. Inspected
    active class definitions against the assessments, named parents and typed synonyms.
    Relevant labels and scoped aliases: {"ENVO:00002011": {"label": "fresh water",
    "synonyms": {"hasExactSynonym": ["freshwater"], "hasBroadSynonym": [], "hasNarrowSynonym":
    [], "hasRelatedSynonym": ["sweet water"]}, "parents": ["http://purl.obolibrary.org/obo/ENVO_00002006"]}}'
- evidence_id: BASE_QC
  kind: record_content
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38341318428
  accessed_at: '2026-10-14T04:40:34.480722Z'
  support: supports
  summary: Fresh gh run view confirmed success on exact unchanged base db6301fe65eb3f419dfb2338f029ca2c269cdbef.
    Its actual log records 1060 tests passed, 3 skipped and all native quality gates.
    This existing run checks the captured scientific inputs, not the new review files;
    full QC was not rerun locally for review-only additions.
- evidence_id: GOLD
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=ecosystempaths
  accessed_at: '2026-10-14T04:31:31.245568Z'
  locator: Workbook row656
  support: supports
  summary: 'Fresh complete workbook parsed with incorrect worksheet dimensions reset;2422
    rows including header. Exact path row: ["8269", "Environmental", "Aquatic", "Freshwater",
    "Transient pool", "Unclassified"]. SHA256 f13652be516a0f1482bf0abbb44d7d8e9acb17c5d401cd7e0474af949b447611.
    A terminal-path listing verifies this vocabulary row, not every collapsed historical
    internal node, sample count or ecological property.'
- evidence_id: GOLD_SCOPE
  kind: database
  reference: https://gold.jgi.doe.gov/ecosystem_classification
  accessed_at: '2026-10-14T04:40:34.480722Z'
  support: context_only
  locator: Classification purpose and five-level descriptions
  summary: GOLD describes sample surroundings using a sample-driven classification.
    Source path depth alone does not establish a strict ontology subclass or exact
    habitat equivalence.
- evidence_id: EPA
  kind: database
  reference: https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P1002R0O.TXT
  locator: EPA/903/B-05/001, abstract and introduction
  accessed_at: '2026-10-14T04:40:34.480722Z'
  support: context_only
  summary: The manual treats periodic inundation/drying as habitat properties, not
    identity with fresh-water material. Regional seasonal-pool criteria do not establish
    every transient-pool class boundary.
assessments:
- assessment_id: IDENTITY
  area: identity
  topic: Exact entity and strictly broader hierarchy
  outcome: supported
  target_ids:
  - habitatmech:GOLD.d39a2ed099
  evidence_ids:
  - RECORD
  - RAW
  - RULES
  - ENVO
  summary: GOLD8268/8269 denotes the freshwater transient-pool source. A water body
    or its intermittently filled depression is not ENVO:00002011 water material, and
    exclusion row 146 already suppresses that context contribution. CLASS row 1169
    preserves UNGROUNDED/SEEDED; neither this review nor the exclusion creates ITEM
    status. The separate Microbial mat child has also had its pool-context edge excluded;
    its remaining endpoint question is not a target finding.
- assessment_id: SOURCES
  area: provenance
  topic: Source units, membership, MIxS roles and status
  outcome: supported
  target_ids:
  - habitatmech:GOLD.d39a2ed099
  evidence_ids:
  - RAW
  - OWNERS
  - SEARCH
  summary: gold_ecosystem_paths row 1498 contains two collapsed nodes and zero direct
    counters. The first node and collapse note are retained without a fabricated count/unit.
    The current terminal-path workbook confirms8269, not the historical internal node
    8268; the latter is checked only against the frozen inventory. The bounded structured
    inventory search found no target-specific bulk biosample, triad or study row.
- assessment_id: SCIENCE
  area: evidence
  topic: Bounded scientific support and optional content
  outcome: supported
  target_ids:
  - habitatmech:GOLD.d39a2ed099
  evidence_ids:
  - RECORD
  - RAW
  - ENVO
  - EPA
  summary: EPA's seasonal-pool manual distinguishes periodically wet and dry habitats
    from the water material filling them. It supports the excluded material edge,
    but does not equate every GOLD transient pool with a seasonal vernal basin or
    specify a universal hydroperiod, size, taxa or substrate. The undefined basin-versus-water-body
    scope remains explicit; no unsupported definition, genus, environmental measurement
    or mechanism is invented.
findings: []
actions: []
limitations:
- Same-agent review, not independent approval or full-corpus certification.
- Original upstream source membership matrices and study-to-sample crosswalks were
  not reconstructed. Frozen source counters reproduce; live taxonomy verifies identity,
  not occurrence. Public GOLD terminal paths do not independently verify every historical
  internal node.
- Native label validation retains 5 configured accepted exceptions and 2057 no-adapter
  skips; these are not scientific approvals.
- Parent records are inspected for relevant hierarchy/interpretation only. Their unrelated
  taxa, parameters and causal evidence are not inherited or re-reviewed here.
- Legacy reports are historical leads, not structured disposition lineage. Corrected
  hierarchy findings are described as current state without silently closing old findings.
- PMC browser challenge and intermittent publisher HTML errors were encountered; primary-paper
  PDFs or publisher/institutional text were inspected instead. GOLD resources URL
  was inaccessible; the classification page and workbook were accessible.
- No habitat, decision, source, history, scientific status, generated page or map
  is changed. Browser visual QA and SSSOM/KGX conformance are outside this record
  review.
tags:
- habitatmech
- record-review
- aquatic
```
