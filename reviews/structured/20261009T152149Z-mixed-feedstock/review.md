# Mixed feedstock: source, identity and hierarchy review

- Review: 20261009T152149Z-mixed-feedstock
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-09T15:02:39Z
- Finished UTC: 2026-10-09T15:21:49Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The source-qualified mixed solid-waste feedstock record is coherent at SEEDED scope, with no demonstrated material defect. Keep the minted identity and broad Solid Waste parent; missing exact sample membership and an authored definition limit further identity or recipe claims.

## Scope And Provenance

Full field-by-field scientific review of exactly one generated record; related records and source samples are context only.

Selection: Exact ID, path and source-path disambiguation in the continuing 3208-record corpus review. This is one complete record, not a corpus-wide pass.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 14d99404e9da3170d3d099aedc2855d4e8c4081e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.f655f67ca2 | data/habitats/engineered/mixed_feedstock.yaml | generated | Mixed feedstock |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Schema | passed | True | habitatmech:GOLD.f655f67ca2 | No issues found. |
| Closed schema | passed | True | habitatmech:GOLD.f655f67ca2 | Four exact targets, zero errors. |
| Corpus reproduction | passed | True | habitatmech:GOLD.f655f67ca2 | 3208 expected and present; zero missing, extra or differing. |
| History | passed | True | habitatmech:GOLD.f655f67ca2 | 220 history records valid. |
| Source provenance | passed | True | habitatmech:GOLD.f655f67ca2 | 14 committed inventories and two GOLD sources current. |
| Focused integrity | passed | True | habitatmech:GOLD.f655f67ca2 | Six passed, 33 deselected. |
| Exact-base QC receipt | passed | True | habitatmech:GOLD.f655f67ca2 | Completed success at captured base; reused receipt, not a new full run. |
| Exact-base ontology-label receipt | passed | True | habitatmech:GOLD.f655f67ca2 | Completed success at captured base; reused receipt, no new OAK run. |
| Capture recheck | passed | True | habitatmech:GOLD.f655f67ca2 | Fresh SHA-256 comparison rechecked all 42 captured local inputs; none changed. HEAD remains the inspected base. |
| Causal overlay and iModulonDB applicability | not_applicable | False | habitatmech:GOLD.f655f67ca2 | No overlay, causal edge or structured gene/dataset claim in this target. |

## Scientific And Domain Assessments

### Qualified source identity

identity: supported. Targets: habitatmech:GOLD.f655f67ca2.

The full path qualifies Mixed feedstock as mixed solid-waste feedstock, not every possible feedstock, a completed compost product or the composting process. Its mint and single source node agree. A mixed waste material can supply a microbial habitat; no particular composition, processing stage or commercial product is claimed.

### Mint, decision route and exact-identity restraint

grounding: supported. Targets: habitatmech:GOLD.f655f67ca2.

UNGROUNDED preserves the source-qualified mint and supplies no self-mapping predicate. Actual automatic and curated routes reproduce the full record. A broad or related candidate must not silently replace this identity; a CLASS lexical sweep is not an individual scientific sign-off.

### Strictly broader parent contribution

graph: supported. Targets: habitatmech:GOLD.f655f67ca2.

The immediate GOLD parent resolves through gold_mapping_table to mesh:D062611 Solid Waste. NLM confirms the active descriptor and waste-material scope. Under the retained waste-qualified source meaning, this is a defensible broader material class, not exact identity. Lack of direct samples limits independent confirmation of category membership but is not itself proof of a false parent.

### Source counters and units

quantity: supported. Targets: habitatmech:GOLD.f655f67ca2.

The frozen KGX-derived zero counters correctly omit count/unit; 1 node(s) support no collapse note. The separate 0 current BIOSAMPLE observations are not organisms, taxa, independent replicates or a live replacement for the frozen attestation.

### Lifecycle and generated ownership

provenance: supported. Targets: habitatmech:GOLD.f655f67ca2.

Both native events agree with the CLASS decision and seed. No ITEM identity review, authored definition or source merge is invented. Inputs and native generator own any correction; saving this review does not promote SEEDED.

### Definition, taxa, parameters, evidence, graphs and datasets

completeness: supported. Targets: habitatmech:GOLD.f655f67ca2.

The sparse target makes no unsupported optional biological claims. Exact-key scans found no target-specific triad, taxon or environmental-parameter row. No defined ingredient mixture, causal mechanism or characteristic organism is warranted by source counts or parent/descendant data. Missing optional fields are limitations, not automatic defects.

### Structured expression-module cross-check

evidence: not_applicable. Targets: habitatmech:GOLD.f655f67ca2.

No target gene, regulator, protein, named organism/dataset or transcriptomic assertion requires an iModulonDB adapter. Absence from that resource is not negative evidence.

### Native validation versus scientific validity

schema: supported. Targets: habitatmech:GOLD.f655f67ca2.

Fresh schema, strict, corpus, history and focused reference/lifecycle checks pass. Base QC and label CI receipts are reused with unchanged captured inputs. Deterministic validity does not settle the scientific hierarchy finding.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/engineered/mixed_feedstock.yaml; Complete file; PATHS entry; immediate parent complete file | supports | ENGINEERED / UNGROUNDED / SEEDED; sole parent mesh:D062611; one GOLD attestation; no definition, synonyms, xrefs, parameters, taxa, evidence, graph, discussion or dataset claims. Both existing history events inspected. The full path qualifies Mixed feedstock as mixed solid-waste feedstock, not every possible feedstock, a completed compost product or the composting process. Its mint and single source node agree. A mixed waste material can supply a microbial habitat; no particular composition, processing stage or commercial product is claimed. |
| E2 | data/raw/gold_ecosystem_paths.tsv; Logical data row 1373; exact path Engineered &gt; Solid waste &gt; Mixed feedstock | supports | First node 7696, 1 collapsed node(s): 7696. All frozen organism/study/biosample/total counters zero. Count and unit omission is correct, not proof of no microbes. A one-node source needs no collapse note. |
| E3 | curation/decisions.tsv; Physical line 1358; habitatmech:GOLD.f655f67ca2 | supports | CONFIRM_UNGROUNDED, CLASS, claude-opus-5, 2026-08-12. Actual automatic route gold_unmatched becomes curated_confirm_ungrounded_from_gold_unmatched. Fresh build_corpus/build_document equals every target field: one source, zero ITEM-reviewed sources. SEEDED is accurate; this review is not an ITEM decision. |
| E4 | data/raw/; All 14 committed TSV inventories, exact canonical path, target ID and every collapsed node key | supports | No exact-path gold_path_biosamples row. No exact-path study row. No exact-path triad row or target taxa/parameters from the other inventories. This structured all-field scan excludes descendant-path borrowing. |
| E5 | https://gold.jgi.doe.gov/download?mode=site_excel; Oct 9 public workbook; Biosample/Organism/Sequencing Project/Study sheets, exact path and joins | supports | The complete current workbook scan found zero exact-path biosamples, organisms or project joins. This is bounded exact-path absence, not absence of microbial use or of descendant samples. The prior Composting and Commercial compost reports concern longer paths; their 32 biosamples/31 triads cannot be transferred to this record. Scanned 244951 Biosample rows including header, 532019 Organism rows including header and 636914 Project rows including header. All 108 exact-match biosamples across the four separately reviewed targets join to projects; only this target informs its verdict. |
| E6 | https://gold.jgi.doe.gov/ecosystem_classification; Five-level classification introduction and level descriptions | context_only | GOLD organizes the surroundings/features of collected samples and periodically revises paths. The classification does not establish that each adjacency is a strict is-a relation. |
| E7 | curation/; research/; reports/yaml_record_review/; reviews/; history/; Identifier, label, slug, exact source-path searches | context_only | Ignored-inclusive searches recover the CLASS decisions and historical context mentions, but no earlier individual report, ITEM identity decision, authored definition or causal overlay for this target in those roots. |
| E8 | https://github.com/CultureBotAI/HabitatMech/actions/runs/37947649422; Base 14d99404e9da3170d3d099aedc2855d4e8c4081e | supports | Fresh gh run view confirms completed success on the exact review base. This reuses the completed base full-QC receipt, not a new full-QC invocation for this target. Fresh local checks verify 3208/3208 exact records, 220 valid histories, strict schema and six focused integrity tests. |
| E9 | https://github.com/CultureBotAI/HabitatMech/actions/runs/37947649601; Base 14d99404e9da3170d3d099aedc2855d4e8c4081e | supports | Fresh gh run view confirms completed label-correspondence success on this exact base. No grounding or label changed during this observation; no claim of running OAK anew. |
| E10 | CLAUDE.md; Semantic invariants; docs/CURATION.md, Excluding a GOLD context parent | supports | Every parent contribution must be strictly broader. Exact-path guarded exclusions remove only a GOLD context contribution; they preserve grounding/status and append an exclusion event. Generated records/pages must never be hand-edited. |
| E11 | https://meshb.nlm.nih.gov/record/ui?ui=D062611; Solid Waste, Unique ID and Scope Note | supports | NLM MeSH 2026 confirms D062611 Solid Waste and a discarded-material scope including refuse/sludge, not generic feedstocks. This supports the source-qualified material genus, not a particular recipe or sample membership. |
| E12 | reports/yaml_record_review/20261008T014409Z-composting__614642ae.md; Whole report; commercial_compost report through parent discussion | context_only | Descendant process/product ambiguity remains separate. No descendant observations, counts or findings are promoted into this target; those prior reviews do not establish a defect of Mixed feedstock itself. |

## Limits And Additional Notes

- The current GOLD workbook is 238974789 bytes and differs from the frozen August GOLD_MANIFEST source (222850238 bytes, SHA-256 6797471982570ed145f81aef966c1ff5398dc4d35287a01faefaf80ac5311fea). Matching totals do not prove identical historical membership; no source inventory was refreshed.
- Optional fields are unfilled and scientific status stays SEEDED. This observation is not a term proposal, species-level ecological claim, mechanism review or corpus-wide sign-off.
- Current ontology candidate inspection and local ignored-inclusive term searches are bounded, not an exhaustive proof that no fitting ontology term exists.
- Network attempts initially failed in the restricted shell; official OLS and NCBI structured requests succeeded after network approval. Browser access to NCBI pages was unavailable; fetched XML is the inspected evidence.
- No exact direct sample or study recovered in the named inventory/workbook bounds. The positive assessment is limited to the sparse, explicitly waste-qualified source concept; mixture composition and sampling stage remain unknown.
- Read-only observation saved before any separately authorized issue fix. Proposed actions are not recorded as executed.
- No paid research, external contact, source refresh or native identity/status promotion.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261009T152149Z-mixed-feedstock
kind: record
repository: CultureBotAI/HabitatMech
title: 'Mixed feedstock: source, identity and hierarchy review'
started_at: '2026-10-09T15:02:39Z'
finished_at: '2026-10-09T15:21:49Z'
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
summary: The source-qualified mixed solid-waste feedstock record is coherent at SEEDED
  scope, with no demonstrated material defect. Keep the minted identity and broad
  Solid Waste parent; missing exact sample membership and an authored definition limit
  further identity or recipe claims.
source:
  git_revision: 14d99404e9da3170d3d099aedc2855d4e8c4081e
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
    sha256: 9d2324647d0a0ddeccc2f7836811872e112af208bb1b8f7decb332c00f17d12b
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
  - path: data/habitats/engineered/mixed_feedstock.yaml
    sha256: c74cecd0173bf9f8a7866aef18165574a89fd2540f12ea8b7ea676b2215442f3
    role: target
  - path: data/habitats/engineered/solid_waste.yaml
    sha256: 4cd78657634aca99d98863d643419c7deb56b8835d9f47d144d08247457736d4
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
  - path: reports/yaml_record_review/20261007T214652Z-commercial_compost.md
    sha256: 88029b8570ac8a93e335714c44056d9de1a2c7b14a9ce3d51cbbae4f5f2b0634
    role: context
  - path: reports/yaml_record_review/20261008T014409Z-composting__614642ae.md
    sha256: 579e27703b15d6e28c7b371c217e6389b484a426791d964cab5b03722008706a
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
  description: Full field-by-field scientific review of exactly one generated record;
    related records and source samples are context only.
  selection: Exact ID, path and source-path disambiguation in the continuing 3208-record
    corpus review. This is one complete record, not a corpus-wide pass.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.f655f67ca2
  exclusions:
  - target: All other HabitatMech records
    reason: Parents and historical descendant reviews were read for context, not counted
      as additional target reviews.
targets:
- target_id: habitatmech:GOLD.f655f67ca2
  path: data/habitats/engineered/mixed_feedstock.yaml
  label: Mixed feedstock
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
  - habitatmech:GOLD.f655f67ca2
  command: env UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/mixed_feedstock.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: No issues found.
- check_id: C2
  name: Closed schema
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.f655f67ca2
  command: env UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/mixed_alcohol_bioreactor.yaml
    data/habitats/engineered/mixed_feedstock.yaml data/habitats/engineered/mixed_liquor.yaml
    data/habitats/engineered/mixed_liquor__ef7a87e7.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Four exact targets, zero errors.
- check_id: C3
  name: Corpus reproduction
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.f655f67ca2
  command: env UV_CACHE_DIR=build/uv-cache just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  summary: 3208 expected and present; zero missing, extra or differing.
- check_id: C4
  name: History
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.f655f67ca2
  command: env UV_CACHE_DIR=build/uv-cache just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: 220 history records valid.
- check_id: C5
  name: Source provenance
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.f655f67ca2
  command: env UV_CACHE_DIR=build/uv-cache just provenance-check
  exit_code: 0
  expected_exit_code: 0
  summary: 14 committed inventories and two GOLD sources current.
- check_id: C6
  name: Focused integrity
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.f655f67ca2
  command: env UV_CACHE_DIR=build/uv-cache uv run pytest -q tests/test_corpus_integrity.py
    -k 'parent or reviewed_records or history or causal_edges_reference'
  exit_code: 0
  expected_exit_code: 0
  summary: Six passed, 33 deselected.
- check_id: C7
  name: Exact-base QC receipt
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.f655f67ca2
  command: gh run view 37947649422 --json status,conclusion,headSha,url
  exit_code: 0
  expected_exit_code: 0
  summary: Completed success at captured base; reused receipt, not a new full run.
- check_id: C8
  name: Exact-base ontology-label receipt
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.f655f67ca2
  command: gh run view 37947649601 --json status,conclusion,headSha,url
  exit_code: 0
  expected_exit_code: 0
  summary: Completed success at captured base; reused receipt, no new OAK run.
- check_id: C9
  name: Capture recheck
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.f655f67ca2
  exit_code: 0
  summary: Fresh SHA-256 comparison rechecked all 42 captured local inputs; none changed.
    HEAD remains the inspected base.
- check_id: C10
  name: Causal overlay and iModulonDB applicability
  status: not_applicable
  required: false
  target_ids:
  - habitatmech:GOLD.f655f67ca2
  summary: No overlay, causal edge or structured gene/dataset claim in this target.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/engineered/mixed_feedstock.yaml
  locator: Complete file; PATHS entry; immediate parent complete file
  accessed_at: '2026-10-09T15:21:49Z'
  support: supports
  summary: ENGINEERED / UNGROUNDED / SEEDED; sole parent mesh:D062611; one GOLD attestation;
    no definition, synonyms, xrefs, parameters, taxa, evidence, graph, discussion
    or dataset claims. Both existing history events inspected. The full path qualifies
    Mixed feedstock as mixed solid-waste feedstock, not every possible feedstock,
    a completed compost product or the composting process. Its mint and single source
    node agree. A mixed waste material can supply a microbial habitat; no particular
    composition, processing stage or commercial product is claimed.
- evidence_id: E2
  kind: record_content
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Logical data row 1373; exact path Engineered > Solid waste > Mixed feedstock
  accessed_at: '2026-10-09T15:21:49Z'
  support: supports
  summary: 'First node 7696, 1 collapsed node(s): 7696. All frozen organism/study/biosample/total
    counters zero. Count and unit omission is correct, not proof of no microbes. A
    one-node source needs no collapse note.'
- evidence_id: E3
  kind: record_content
  reference: curation/decisions.tsv
  locator: Physical line 1358; habitatmech:GOLD.f655f67ca2
  accessed_at: '2026-10-09T15:21:49Z'
  support: supports
  summary: 'CONFIRM_UNGROUNDED, CLASS, claude-opus-5, 2026-08-12. Actual automatic
    route gold_unmatched becomes curated_confirm_ungrounded_from_gold_unmatched. Fresh
    build_corpus/build_document equals every target field: one source, zero ITEM-reviewed
    sources. SEEDED is accurate; this review is not an ITEM decision.'
- evidence_id: E4
  kind: record_content
  reference: data/raw/
  locator: All 14 committed TSV inventories, exact canonical path, target ID and every
    collapsed node key
  accessed_at: '2026-10-09T15:21:49Z'
  support: supports
  summary: No exact-path gold_path_biosamples row. No exact-path study row. No exact-path
    triad row or target taxa/parameters from the other inventories. This structured
    all-field scan excludes descendant-path borrowing.
  search_scope: All 14 physical TSV files parsed with csv.DictReader; exact field
    or pipe-member matching, including overflow values. No ignored-file filter.
- evidence_id: E5
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=site_excel
  locator: Oct 9 public workbook; Biosample/Organism/Sequencing Project/Study sheets,
    exact path and joins
  accessed_at: '2026-10-09T15:21:49Z'
  support: supports
  summary: The complete current workbook scan found zero exact-path biosamples, organisms
    or project joins. This is bounded exact-path absence, not absence of microbial
    use or of descendant samples. The prior Composting and Commercial compost reports
    concern longer paths; their 32 biosamples/31 triads cannot be transferred to this
    record. Scanned 244951 Biosample rows including header, 532019 Organism rows including
    header and 636914 Project rows including header. All 108 exact-match biosamples
    across the four separately reviewed targets join to projects; only this target
    informs its verdict.
  snapshot_sha256: 5f48b2f50fb2a9257754960a0f0e12dc6e8fa121e97c3e9f4497249e5fe6e439
- evidence_id: E6
  kind: authority
  reference: https://gold.jgi.doe.gov/ecosystem_classification
  locator: Five-level classification introduction and level descriptions
  accessed_at: '2026-10-09T15:21:49Z'
  support: context_only
  summary: GOLD organizes the surroundings/features of collected samples and periodically
    revises paths. The classification does not establish that each adjacency is a
    strict is-a relation.
- evidence_id: E7
  kind: search
  reference: curation/; research/; reports/yaml_record_review/; reviews/; history/
  locator: Identifier, label, slug, exact source-path searches
  accessed_at: '2026-10-09T15:21:49Z'
  support: context_only
  summary: Ignored-inclusive searches recover the CLASS decisions and historical context
    mentions, but no earlier individual report, ITEM identity decision, authored definition
    or causal overlay for this target in those roots.
  search_scope: rg --no-ignore --hidden; all four exact IDs, slugs and labels and
    the target source paths, plus structured inventory scan. Bounded repository roots,
    not global absence.
- evidence_id: E8
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/37947649422
  locator: Base 14d99404e9da3170d3d099aedc2855d4e8c4081e
  accessed_at: '2026-10-09T15:21:49Z'
  support: supports
  summary: Fresh gh run view confirms completed success on the exact review base.
    This reuses the completed base full-QC receipt, not a new full-QC invocation for
    this target. Fresh local checks verify 3208/3208 exact records, 220 valid histories,
    strict schema and six focused integrity tests.
- evidence_id: E9
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/37947649601
  locator: Base 14d99404e9da3170d3d099aedc2855d4e8c4081e
  accessed_at: '2026-10-09T15:21:49Z'
  support: supports
  summary: Fresh gh run view confirms completed label-correspondence success on this
    exact base. No grounding or label changed during this observation; no claim of
    running OAK anew.
- evidence_id: E10
  kind: record_content
  reference: CLAUDE.md
  locator: Semantic invariants; docs/CURATION.md, Excluding a GOLD context parent
  accessed_at: '2026-10-09T15:21:49Z'
  support: supports
  summary: Every parent contribution must be strictly broader. Exact-path guarded
    exclusions remove only a GOLD context contribution; they preserve grounding/status
    and append an exclusion event. Generated records/pages must never be hand-edited.
- evidence_id: E11
  kind: authority
  reference: https://meshb.nlm.nih.gov/record/ui?ui=D062611
  locator: Solid Waste, Unique ID and Scope Note
  accessed_at: '2026-10-09T15:21:49Z'
  support: supports
  summary: NLM MeSH 2026 confirms D062611 Solid Waste and a discarded-material scope
    including refuse/sludge, not generic feedstocks. This supports the source-qualified
    material genus, not a particular recipe or sample membership.
- evidence_id: E12
  kind: prior_review
  reference: reports/yaml_record_review/20261008T014409Z-composting__614642ae.md
  locator: Whole report; commercial_compost report through parent discussion
  accessed_at: '2026-10-09T15:21:49Z'
  support: context_only
  summary: Descendant process/product ambiguity remains separate. No descendant observations,
    counts or findings are promoted into this target; those prior reviews do not establish
    a defect of Mixed feedstock itself.
assessments:
- assessment_id: A1
  area: identity
  topic: Qualified source identity
  outcome: supported
  summary: The full path qualifies Mixed feedstock as mixed solid-waste feedstock,
    not every possible feedstock, a completed compost product or the composting process.
    Its mint and single source node agree. A mixed waste material can supply a microbial
    habitat; no particular composition, processing stage or commercial product is
    claimed.
  target_ids:
  - habitatmech:GOLD.f655f67ca2
  evidence_ids:
  - E1
  - E2
  - E5
- assessment_id: A2
  area: grounding
  topic: Mint, decision route and exact-identity restraint
  outcome: supported
  summary: UNGROUNDED preserves the source-qualified mint and supplies no self-mapping
    predicate. Actual automatic and curated routes reproduce the full record. A broad
    or related candidate must not silently replace this identity; a CLASS lexical
    sweep is not an individual scientific sign-off.
  target_ids:
  - habitatmech:GOLD.f655f67ca2
  evidence_ids:
  - E1
  - E3
- assessment_id: A3
  area: graph
  topic: Strictly broader parent contribution
  outcome: supported
  summary: The immediate GOLD parent resolves through gold_mapping_table to mesh:D062611
    Solid Waste. NLM confirms the active descriptor and waste-material scope. Under
    the retained waste-qualified source meaning, this is a defensible broader material
    class, not exact identity. Lack of direct samples limits independent confirmation
    of category membership but is not itself proof of a false parent.
  target_ids:
  - habitatmech:GOLD.f655f67ca2
  evidence_ids:
  - E1
  - E3
  - E6
  - E10
  - E11
- assessment_id: A4
  area: quantity
  topic: Source counters and units
  outcome: supported
  summary: The frozen KGX-derived zero counters correctly omit count/unit; 1 node(s)
    support no collapse note. The separate 0 current BIOSAMPLE observations are not
    organisms, taxa, independent replicates or a live replacement for the frozen attestation.
  target_ids:
  - habitatmech:GOLD.f655f67ca2
  evidence_ids:
  - E2
  - E4
  - E5
- assessment_id: A5
  area: provenance
  topic: Lifecycle and generated ownership
  outcome: supported
  summary: Both native events agree with the CLASS decision and seed. No ITEM identity
    review, authored definition or source merge is invented. Inputs and native generator
    own any correction; saving this review does not promote SEEDED.
  target_ids:
  - habitatmech:GOLD.f655f67ca2
  evidence_ids:
  - E1
  - E3
  - E7
  - E10
- assessment_id: A6
  area: completeness
  topic: Definition, taxa, parameters, evidence, graphs and datasets
  outcome: supported
  summary: The sparse target makes no unsupported optional biological claims. Exact-key
    scans found no target-specific triad, taxon or environmental-parameter row. No
    defined ingredient mixture, causal mechanism or characteristic organism is warranted
    by source counts or parent/descendant data. Missing optional fields are limitations,
    not automatic defects.
  target_ids:
  - habitatmech:GOLD.f655f67ca2
  evidence_ids:
  - E1
  - E4
  - E7
- assessment_id: A7
  area: evidence
  topic: Structured expression-module cross-check
  outcome: not_applicable
  summary: No target gene, regulator, protein, named organism/dataset or transcriptomic
    assertion requires an iModulonDB adapter. Absence from that resource is not negative
    evidence.
  target_ids:
  - habitatmech:GOLD.f655f67ca2
  evidence_ids:
  - E1
- assessment_id: A8
  area: schema
  topic: Native validation versus scientific validity
  outcome: supported
  summary: Fresh schema, strict, corpus, history and focused reference/lifecycle checks
    pass. Base QC and label CI receipts are reused with unchanged captured inputs.
    Deterministic validity does not settle the scientific hierarchy finding.
  target_ids:
  - habitatmech:GOLD.f655f67ca2
  evidence_ids:
  - E8
  - E9
findings: []
actions: []
limitations:
- The current GOLD workbook is 238974789 bytes and differs from the frozen August
  GOLD_MANIFEST source (222850238 bytes, SHA-256 6797471982570ed145f81aef966c1ff5398dc4d35287a01faefaf80ac5311fea).
  Matching totals do not prove identical historical membership; no source inventory
  was refreshed.
- Optional fields are unfilled and scientific status stays SEEDED. This observation
  is not a term proposal, species-level ecological claim, mechanism review or corpus-wide
  sign-off.
- Current ontology candidate inspection and local ignored-inclusive term searches
  are bounded, not an exhaustive proof that no fitting ontology term exists.
- Network attempts initially failed in the restricted shell; official OLS and NCBI
  structured requests succeeded after network approval. Browser access to NCBI pages
  was unavailable; fetched XML is the inspected evidence.
- No exact direct sample or study recovered in the named inventory/workbook bounds.
  The positive assessment is limited to the sparse, explicitly waste-qualified source
  concept; mixture composition and sampling stage remain unknown.
notes:
- Read-only observation saved before any separately authorized issue fix. Proposed
  actions are not recorded as executed.
- No paid research, external contact, source refresh or native identity/status promotion.
tags:
- habitat
- engineered
- gold
- record-review
```
