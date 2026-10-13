# Scientific record review: swamp ecosystem

- Review: 20261013T024744Z-swamp_ecosystem
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-13T02:18:39.408226Z
- Finished UTC: 2026-10-13T02:47:44.328188Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The three-source swamp ecosystem record retains the true wetland-ecosystem genus and the corrected area-context exclusion. Its heterogeneous counts and 26 associations reproduce, and taxon identifiers/names resolve. Two ontology aliases have unsupported exact scope: wetland is broad and cienaga related in current ENVO (#1249).

## Scope And Provenance

One entire generated habitat and every contributing source concept.

Selection: Next four aquatic paths without completed individual structured scientific reviews, in stable path order; this bundle assesses only this target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 348085582b0090404a73c122376b8045e6050c41.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| ENVO:00000233 | data/habitats/aquatic/swamp_ecosystem.yaml | generated | swamp ecosystem |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native validation | passed | True | ENVO:00000233 | Actual success 2026-10-13T02:19:00.022099+00:00 to 2026-10-13T02:19:03.503720+00:00. The command retains its record-specific or corpus-wide scope. |
| Native validation | passed | True | ENVO:00000233 | Actual success 2026-10-13T02:19:03.504533+00:00 to 2026-10-13T02:19:10.367960+00:00. The command retains its record-specific or corpus-wide scope. |
| Native validation | passed | True | ENVO:00000233 | Actual success 2026-10-13T02:08:10.569120+00:00 to 2026-10-13T02:09:49.514758+00:00. The command retains its record-specific or corpus-wide scope. |
| Native validation | passed | True | ENVO:00000233 | Actual success 2026-10-13T02:09:49.516177+00:00 to 2026-10-13T02:10:00.046475+00:00. The command retains its record-specific or corpus-wide scope. |
| Native validation | passed | True | ENVO:00000233 | Actual success 2026-10-13T02:10:00.047246+00:00 to 2026-10-13T02:10:00.898990+00:00. The command retains its record-specific or corpus-wide scope. |
| Native validation | passed | True | ENVO:00000233 | Actual success 2026-10-13T02:10:00.899837+00:00 to 2026-10-13T02:10:22.775641+00:00. The command retains its record-specific or corpus-wide scope. |
| Native validation | passed | True | ENVO:00000233 | Actual success 2026-10-13T02:10:22.776432+00:00 to 2026-10-13T02:10:29.162380+00:00. The command retains its record-specific or corpus-wide scope. |
| Native validation | passed | True | ENVO:00000233 | Actual success 2026-10-13T02:10:29.163275+00:00 to 2026-10-13T02:10:58.864928+00:00. The command retains its record-specific or corpus-wide scope. |
| Exact-input hosted authoritative QC | passed | True | ENVO:00000233 | Exact-head authoritative hosted QC passed: 1060 tests, 3 skipped, and all native quality gates. New review files are not covered by this pre-save run. |
| Claim-specific expression module | not_applicable | False | ENVO:00000233 | No gene, regulator or strain-specific transcriptomic claim occurs in this habitat record; iModulonDB is not applicable and non-use is not negative evidence. |

## Scientific And Domain Assessments

### Exact identity and strictly broader hierarchy

identity: supported. Targets: ENVO:00000233.

ENVO:00000233 is an ecosystem with ENVO:01001209 wetland ecosystem as its true genus, not a subclass of the overlapping wetland area ENVO:00000043. The exact GOLD source guard row154 remains effective. Three ITEM REVIEW decisions account for REVIEWED, while BacDive and GOLD still carry closeMatch and PREGO self-identifies. The current ontology definition is faithfully reproduced; EPA uses a woody-vegetation criterion and allows seasonal standing water, so equivalent scope across all vocabulary usages is not fully established. This disagreement is retained as a limitation, not silently rewritten or upgraded to exact source equivalence.

### Source counters, triad roles and review lifecycle

provenance: supported. Targets: ENVO:00000233.

BacDive index row59 reports 171 STRAIN and 149 distinct taxa; GOLD row565 reports 8 ORGANISM; PREGO row675 reports 1 TAXON with score 4 and its isolate channel. These units are not additive. Separate GOLD bulk row792 reports 4 biosamples; triad rows431-433 describe 1 sample from 1 study with lake-biome, freshwater-lake and lake-water roles. Those contextual slots are not replacement identity or genus. The two exact path memberships at study rows844/3363 are not the triad study denominator. The original merged-source membership matrices were not independently re-extracted.

### Bounded taxon evidence and optional scientific content

evidence: supported. Targets: ENVO:00000233.

The one PREGO association and 25 BacDive associations reproduce, including rank/count/pool and the PREGO Trichococcus palustris corroboration flag. All 26 current NCBI identifiers and stored names agree. DSMZ 9172 independently records strain Z-7189 from a swamp near Abramtsevo; this supports that bounded species association, not all 171 strains, every swamp or a characteristic taxon claim. Taxa include broad ranks and named strains; candidate_pool 149 is not the number of associations displayed. No environmental measurement or mechanism graph is supplied.

### Broad and related swamp aliases are promoted to exact equivalence

grounding: concern. Targets: ENVO:00000233.

Current official ENVO/OLS types wetland as BROAD and cienaga as RELATED; both are generated as EXACT_SYNONYM. The frozen ontology_terms row6816 has an untyped synonym pipe, and ConceptStore.get promotes each spelling to exact. The earlier BacDive/GOLD source-synonym correction does not repair these independent ontology assertions. True exact Swamp and swamp aliases should remain exact.

## Findings

### F1: Broad and related swamp aliases are promoted to exact equivalence

major / open / confirmed; issue key: envo-00000233-synonym-scope.

Current official ENVO/OLS types wetland as BROAD and cienaga as RELATED; both are generated as EXACT_SYNONYM. The frozen ontology_terms row6816 has an untyped synonym pipe, and ConceptStore.get promotes each spelling to exact. The earlier BacDive/GOLD source-synonym correction does not repair these independent ontology assertions. True exact Swamp and swamp aliases should remain exact.

## Recommended Actions And Acceptance Checks

### A1

Preserve typed ontology synonym assertions through the governed source inventory and generator; treat unknown scope conservatively rather than as exact.

- Regenerate wetland as BROAD and cienaga as RELATED while retaining verified exact Swamp/swamp, PREGO related aliases and source-specific GOLD/BacDive related aliases.
- Test multiple scopes for one spelling, unknown scope, and actual typed exact/broad/narrow/related inputs; do not globally downgrade every alias.
- Refresh the source contract and provenance through native extraction, not manual generated YAML or checksum edits.
- Append required curation history, regenerate through native writers, and pass schema, labels, provenance, exact reproduction, site and full QC. Preserve prior immutable reviews and use a linked successor to change this disposition.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| RECORD | data/habitats/aquatic/swamp_ecosystem.yaml | supports | Entire YAML inspected, including each source, taxon and historical event. The three-source swamp ecosystem record retains the true wetland-ecosystem genus and the corrected area-context exclusion. Its heterogeneous counts and 26 associations reproduce, and taxon identifiers/names resolve. Two ontology aliases have unsupported exact scope: wetland is broad and cienaga related in current ENVO (#1249). |
| RAW | data/raw/gold_ecosystem_paths.tsv:565; data/raw/prego_habitat_taxa.tsv:4359; data/raw/prego_habitats.tsv:675; data/raw/gold_path_triads.tsv:431,432,433; data/raw/gold_path_biosamples.tsv:792; data/raw/gold_studies.tsv:844,3363; data/raw/bacdive_source_taxa.tsv:3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048; data/raw/bacdive_isolation_sources.tsv:59; data/raw/ontology_subclass_edges.tsv:4865; data/raw/ontology_terms.tsv:6816; curation/gold_parent_exclusions.tsv:154; curation/decisions.tsv:20,186,1465 | supports | BacDive index row59 reports 171 STRAIN and 149 distinct taxa; GOLD row565 reports 8 ORGANISM; PREGO row675 reports 1 TAXON with score 4 and its isolate channel. These units are not additive. Separate GOLD bulk row792 reports 4 biosamples; triad rows431-433 describe 1 sample from 1 study with lake-biome, freshwater-lake and lake-water roles. Those contextual slots are not replacement identity or genus. The two exact path memberships at study rows844/3363 are not the triad study denominator. The original merged-source membership matrices were not independently re-extracted. |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; docs/record-review-profile.md; src/habitatmech/schema/habitatmech.yaml | supports | Applied strict-genus, source-comparison, typed-synonym, MIxS-role, source-unit, association-versus-characteristic and ITEM lifecycle rules. Native optional fields are not mandatory scientific inventions. |
| CODE | src/habitatmech/seed.py:427; src/habitatmech/seed.py:804; src/habitatmech/schema/habitatmech.yaml:317; src/habitatmech/extract.py:338; src/habitatmech/extract.py:835 | supports | Inspected source and synonym routes plus PREGO ranking semantics. Exact full-document reconstruction from build_corpus/build_document matched this record, with captured input hashes rechecked unchanged. Reproduction establishes implementation provenance, not scientific correctness. |
| SEARCH | curation; history; research; conf; reviews/structured; reports/yaml_record_review; data/raw | supports | Bounded ignored/hidden-inclusive searches used target ID, source mint, label and slug. Existing legacy report and later maintained fixes were inspected; legacy prose is not a new structured disposition. No earlier completed individual structured review of this exact target was present in the coverage inventory. Original source membership was not independently rebuilt; no global absence claim is made. |
| QC | https://github.com/CultureBotAI/HabitatMech/actions/runs/38335796983 | supports | Exact-head authoritative hosted QC passed: 1060 tests, 3 skipped, and all native quality gates. This exact captured scientific-input head was checked; these new immutable reviews require separate integrity and final-head CI. |
| ONT0 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000233 | supports | Active ENVO:00000233 swamp ecosystem. Description inspected against the stored definition and the identity assessment above. Named parents from the official linked response: [["ENVO:01001209", "wetland ecosystem"]]. Relevant typed synonym assertions: [["Swamp", "hasExactSynonym"], ["cienaga", "hasRelatedSynonym"], ["swamp", "hasExactSynonym"], ["wetland", "hasBroadSynonym"]]. |
| ONT1 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001209 | supports | Active ENVO:01001209 wetland ecosystem. Description inspected against the stored definition and the identity assessment above. Named parents from the official linked response: [["ENVO:01001110", "ecosystem"]]. Relevant typed synonym assertions: []. |
| ONT2 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000043 | supports | Active ENVO:00000043 wetland area. Description inspected against the stored definition and the identity assessment above. Named parents from the official linked response: [["ENVO:01001305", "vegetated area"]]. Relevant typed synonym assertions: []. |
| EPA | https://www.epa.gov/wetlands/classification-and-types-wetlands; Description of Swamps; Forested Swamps; Shrub Swamps | context_only | The official ecological classification emphasizes woody vegetation and permits standing water during only some parts of a year. This differs from the ontology definition requiring permanent inundation; the scope conflict is retained without replacing the source definition. |
| DSMZ | https://www.dsmz.de/collection/catalogue/details/culture/DSM-9172; Identity, strain designation and isolated-from fields | context_only | DSM9172 is Trichococcus palustris strain Z-7189, isolated from a swamp near Abramtsevo. This supports one bounded occurrence rather than habitat-wide characteristic presence or validation of all source counts. |
| TAXA | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;retmode=xml&amp;id=2,54,56,103,173,1066,1069,1082,1267,1399,1406,1464,1476,1495,1537,1855,13690,83428,83453,104245,106592,111805,112248,114707,114715,117681,129817,134561,139056,140314,150053,158899,162209,180282,184914,193108,204470,382514,1069475,1108595,1117702,1117703,1118379,1121022,1121291,1121343,1122133,1122612,1122928,1122946,1123043 | supports | The one PREGO association and 25 BacDive associations reproduce, including rank/count/pool and the PREGO Trichococcus palustris corroboration flag. All 26 current NCBI identifiers and stored names agree. DSMZ 9172 independently records strain Z-7189 from a swamp near Abramtsevo; this supports that bounded species association, not all 171 strains, every swamp or a characteristic taxon claim. Taxa include broad ranks and named strains; candidate_pool 149 is not the number of associations displayed. No environmental measurement or mechanism graph is supplied. |

## Limits And Additional Notes

- Same-agent review, not independent approval or whole-corpus certification.
- Source occurrence and association membership was not independently rebuilt from original upstream matrices; frozen counters reproduce but do not establish characteristic presence. Live ontology and taxonomy resolution do not validate habitat occurrence.
- Ontology-label validation retains configured no-adapter skips and accepted exceptions; those skips are not scientific approval.
- Legacy reports are historical leads, not structured finding lineage; earlier corrections are not newly performed or silently reopened by this review.
- The assessment changes no habitat, decision, scientific status, history, generated site or map. Optional parameters, definitions and mechanisms are not invented.
- SSSOM/KGX compatibility was not audited. Shared endpoint issue #1398 and typed synonym issue #1249 remain open where applicable.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T024744Z-swamp_ecosystem
kind: record
repository: CultureBotAI/HabitatMech
title: 'Scientific record review: swamp ecosystem'
started_at: '2026-10-13T02:18:39.408226Z'
finished_at: '2026-10-13T02:47:44.328188Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Agent participated in repository work; this is not independent
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
scientific_review: true
verdict: needs_curation
summary: 'The three-source swamp ecosystem record retains the true wetland-ecosystem
  genus and the corrected area-context exclusion. Its heterogeneous counts and 26
  associations reproduce, and taxon identifiers/names resolve. Two ontology aliases
  have unsupported exact scope: wetland is broad and cienaga related in current ENVO
  (#1249).'
source:
  git_revision: 348085582b0090404a73c122376b8045e6050c41
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
  - path: data/habitats/aquatic/swamp_ecosystem.yaml
    sha256: 1c6cc6186199917308c789a59ec167a8ac72d95b06cc05577f08b301c993f576
    role: target
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
  - path: history/mappings/swamp_ecosystem/2026-10-06T155006Z-codex-gpt-5-15e0f2.yaml
    sha256: 321a486476bd8f90bc38d64e3d272cc688d22d9fe906b462893efc092a705957
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20261006T153106Z-swamp_ecosystem.md
    sha256: 4ac30191655473b40d2f2b1828e76fa1affc5031fdfd0cd6fd79fae3690826d9
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
- target_id: ENVO:00000233
  path: data/habitats/aquatic/swamp_ecosystem.yaml
  label: swamp ecosystem
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Source identity and ITEM review decisions
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Exact source context-parent exclusions
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Definitions and genus
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Pinned ontology definitions and synonyms
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_subclass_edges.tsv
    role: Pinned ontology hierarchy
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Source harmonization and generated record construction
scope:
  description: One entire generated habitat and every contributing source concept.
  selection: Next four aquatic paths without completed individual structured scientific
    reviews, in stable path order; this bundle assesses only this target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - ENVO:00000233
checks:
- check_id: C0
  name: Native validation
  required: true
  status: passed
  target_ids:
  - ENVO:00000233
  command: just validate data/habitats/aquatic/swamp_ecosystem.yaml
  exit_code: 0
  evidence_ids:
  - QC
  summary: Actual success 2026-10-13T02:19:00.022099+00:00 to 2026-10-13T02:19:03.503720+00:00.
    The command retains its record-specific or corpus-wide scope.
- check_id: C1
  name: Native validation
  required: true
  status: passed
  target_ids:
  - ENVO:00000233
  command: just validate-strict data/habitats/aquatic/swamp_ecosystem.yaml
  exit_code: 0
  evidence_ids:
  - QC
  summary: Actual success 2026-10-13T02:19:03.504533+00:00 to 2026-10-13T02:19:10.367960+00:00.
    The command retains its record-specific or corpus-wide scope.
- check_id: C2
  name: Native validation
  required: true
  status: passed
  target_ids:
  - ENVO:00000233
  command: just validate-products
  exit_code: 0
  evidence_ids:
  - QC
  summary: Actual success 2026-10-13T02:08:10.569120+00:00 to 2026-10-13T02:09:49.514758+00:00.
    The command retains its record-specific or corpus-wide scope.
- check_id: C3
  name: Native validation
  required: true
  status: passed
  target_ids:
  - ENVO:00000233
  command: just validate-history
  exit_code: 0
  evidence_ids:
  - QC
  summary: Actual success 2026-10-13T02:09:49.516177+00:00 to 2026-10-13T02:10:00.046475+00:00.
    The command retains its record-specific or corpus-wide scope.
- check_id: C4
  name: Native validation
  required: true
  status: passed
  target_ids:
  - ENVO:00000233
  command: just provenance-check
  exit_code: 0
  evidence_ids:
  - QC
  summary: Actual success 2026-10-13T02:10:00.047246+00:00 to 2026-10-13T02:10:00.898990+00:00.
    The command retains its record-specific or corpus-wide scope.
- check_id: C5
  name: Native validation
  required: true
  status: passed
  target_ids:
  - ENVO:00000233
  command: just verify-corpus
  exit_code: 0
  evidence_ids:
  - QC
  summary: Actual success 2026-10-13T02:10:00.899837+00:00 to 2026-10-13T02:10:22.775641+00:00.
    The command retains its record-specific or corpus-wide scope.
- check_id: C6
  name: Native validation
  required: true
  status: passed
  target_ids:
  - ENVO:00000233
  command: just validate-causal-all
  exit_code: 0
  evidence_ids:
  - QC
  summary: Actual success 2026-10-13T02:10:22.776432+00:00 to 2026-10-13T02:10:29.162380+00:00.
    The command retains its record-specific or corpus-wide scope.
- check_id: C7
  name: Native validation
  required: true
  status: passed
  target_ids:
  - ENVO:00000233
  command: just term-requests-check
  exit_code: 0
  evidence_ids:
  - QC
  summary: Actual success 2026-10-13T02:10:29.163275+00:00 to 2026-10-13T02:10:58.864928+00:00.
    The command retains its record-specific or corpus-wide scope.
- check_id: CI
  name: Exact-input hosted authoritative QC
  required: true
  status: passed
  target_ids:
  - ENVO:00000233
  command: gh run view 38335796983 --log
  exit_code: 0
  evidence_ids:
  - QC
  summary: 'Exact-head authoritative hosted QC passed: 1060 tests, 3 skipped, and
    all native quality gates. New review files are not covered by this pre-save run.'
- check_id: IMOD
  name: Claim-specific expression module
  required: false
  status: not_applicable
  target_ids:
  - ENVO:00000233
  summary: No gene, regulator or strain-specific transcriptomic claim occurs in this
    habitat record; iModulonDB is not applicable and non-use is not negative evidence.
evidence:
- evidence_id: RECORD
  kind: record_content
  reference: data/habitats/aquatic/swamp_ecosystem.yaml
  accessed_at: '2026-10-13T02:47:44.327903Z'
  support: supports
  summary: 'Entire YAML inspected, including each source, taxon and historical event.
    The three-source swamp ecosystem record retains the true wetland-ecosystem genus
    and the corrected area-context exclusion. Its heterogeneous counts and 26 associations
    reproduce, and taxon identifiers/names resolve. Two ontology aliases have unsupported
    exact scope: wetland is broad and cienaga related in current ENVO (#1249).'
- evidence_id: RAW
  kind: record_content
  reference: data/raw/gold_ecosystem_paths.tsv:565; data/raw/prego_habitat_taxa.tsv:4359;
    data/raw/prego_habitats.tsv:675; data/raw/gold_path_triads.tsv:431,432,433; data/raw/gold_path_biosamples.tsv:792;
    data/raw/gold_studies.tsv:844,3363; data/raw/bacdive_source_taxa.tsv:3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048;
    data/raw/bacdive_isolation_sources.tsv:59; data/raw/ontology_subclass_edges.tsv:4865;
    data/raw/ontology_terms.tsv:6816; curation/gold_parent_exclusions.tsv:154; curation/decisions.tsv:20,186,1465
  accessed_at: '2026-10-13T02:47:44.327903Z'
  support: supports
  summary: BacDive index row59 reports 171 STRAIN and 149 distinct taxa; GOLD row565
    reports 8 ORGANISM; PREGO row675 reports 1 TAXON with score 4 and its isolate
    channel. These units are not additive. Separate GOLD bulk row792 reports 4 biosamples;
    triad rows431-433 describe 1 sample from 1 study with lake-biome, freshwater-lake
    and lake-water roles. Those contextual slots are not replacement identity or genus.
    The two exact path memberships at study rows844/3363 are not the triad study denominator.
    The original merged-source membership matrices were not independently re-extracted.
- evidence_id: RULES
  kind: record_content
  reference: docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; docs/record-review-profile.md;
    src/habitatmech/schema/habitatmech.yaml
  accessed_at: '2026-10-13T02:47:44.327903Z'
  support: supports
  summary: Applied strict-genus, source-comparison, typed-synonym, MIxS-role, source-unit,
    association-versus-characteristic and ITEM lifecycle rules. Native optional fields
    are not mandatory scientific inventions.
- evidence_id: CODE
  kind: record_content
  reference: src/habitatmech/seed.py:427; src/habitatmech/seed.py:804; src/habitatmech/schema/habitatmech.yaml:317;
    src/habitatmech/extract.py:338; src/habitatmech/extract.py:835
  accessed_at: '2026-10-13T02:47:44.327903Z'
  support: supports
  summary: Inspected source and synonym routes plus PREGO ranking semantics. Exact
    full-document reconstruction from build_corpus/build_document matched this record,
    with captured input hashes rechecked unchanged. Reproduction establishes implementation
    provenance, not scientific correctness.
- evidence_id: SEARCH
  kind: record_content
  reference: curation; history; research; conf; reviews/structured; reports/yaml_record_review;
    data/raw
  accessed_at: '2026-10-13T02:47:44.327903Z'
  support: supports
  summary: Bounded ignored/hidden-inclusive searches used target ID, source mint,
    label and slug. Existing legacy report and later maintained fixes were inspected;
    legacy prose is not a new structured disposition. No earlier completed individual
    structured review of this exact target was present in the coverage inventory.
    Original source membership was not independently rebuilt; no global absence claim
    is made.
- evidence_id: QC
  kind: record_content
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38335796983
  accessed_at: '2026-10-13T02:47:44.327903Z'
  support: supports
  summary: 'Exact-head authoritative hosted QC passed: 1060 tests, 3 skipped, and
    all native quality gates. This exact captured scientific-input head was checked;
    these new immutable reviews require separate integrity and final-head CI.'
- evidence_id: ONT0
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000233
  accessed_at: '2026-10-13T02:20:21.559753Z'
  support: supports
  summary: 'Active ENVO:00000233 swamp ecosystem. Description inspected against the
    stored definition and the identity assessment above. Named parents from the official
    linked response: [["ENVO:01001209", "wetland ecosystem"]]. Relevant typed synonym
    assertions: [["Swamp", "hasExactSynonym"], ["cienaga", "hasRelatedSynonym"], ["swamp",
    "hasExactSynonym"], ["wetland", "hasBroadSynonym"]].'
- evidence_id: ONT1
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001209
  accessed_at: '2026-10-13T02:20:24.432892Z'
  support: supports
  summary: 'Active ENVO:01001209 wetland ecosystem. Description inspected against
    the stored definition and the identity assessment above. Named parents from the
    official linked response: [["ENVO:01001110", "ecosystem"]]. Relevant typed synonym
    assertions: [].'
- evidence_id: ONT2
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000043
  accessed_at: '2026-10-13T02:20:28.917015Z'
  support: supports
  summary: 'Active ENVO:00000043 wetland area. Description inspected against the stored
    definition and the identity assessment above. Named parents from the official
    linked response: [["ENVO:01001305", "vegetated area"]]. Relevant typed synonym
    assertions: [].'
- evidence_id: EPA
  kind: database
  reference: https://www.epa.gov/wetlands/classification-and-types-wetlands
  locator: Description of Swamps; Forested Swamps; Shrub Swamps
  accessed_at: '2026-10-13T02:31:36Z'
  support: context_only
  summary: The official ecological classification emphasizes woody vegetation and
    permits standing water during only some parts of a year. This differs from the
    ontology definition requiring permanent inundation; the scope conflict is retained
    without replacing the source definition.
- evidence_id: DSMZ
  kind: database
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-9172
  locator: Identity, strain designation and isolated-from fields
  accessed_at: '2026-10-13T02:31:36Z'
  support: context_only
  summary: DSM9172 is Trichococcus palustris strain Z-7189, isolated from a swamp
    near Abramtsevo. This supports one bounded occurrence rather than habitat-wide
    characteristic presence or validation of all source counts.
- evidence_id: TAXA
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&retmode=xml&id=2,54,56,103,173,1066,1069,1082,1267,1399,1406,1464,1476,1495,1537,1855,13690,83428,83453,104245,106592,111805,112248,114707,114715,117681,129817,134561,139056,140314,150053,158899,162209,180282,184914,193108,204470,382514,1069475,1108595,1117702,1117703,1118379,1121022,1121291,1121343,1122133,1122612,1122928,1122946,1123043
  accessed_at: '2026-10-13T02:20:30.323071Z'
  support: supports
  summary: The one PREGO association and 25 BacDive associations reproduce, including
    rank/count/pool and the PREGO Trichococcus palustris corroboration flag. All 26
    current NCBI identifiers and stored names agree. DSMZ 9172 independently records
    strain Z-7189 from a swamp near Abramtsevo; this supports that bounded species
    association, not all 171 strains, every swamp or a characteristic taxon claim.
    Taxa include broad ranks and named strains; candidate_pool 149 is not the number
    of associations displayed. No environmental measurement or mechanism graph is
    supplied.
assessments:
- assessment_id: IDENTITY
  area: identity
  topic: Exact identity and strictly broader hierarchy
  outcome: supported
  target_ids:
  - ENVO:00000233
  evidence_ids:
  - RECORD
  - RAW
  - RULES
  - ONT0
  - ONT1
  - ONT2
  summary: ENVO:00000233 is an ecosystem with ENVO:01001209 wetland ecosystem as its
    true genus, not a subclass of the overlapping wetland area ENVO:00000043. The
    exact GOLD source guard row154 remains effective. Three ITEM REVIEW decisions
    account for REVIEWED, while BacDive and GOLD still carry closeMatch and PREGO
    self-identifies. The current ontology definition is faithfully reproduced; EPA
    uses a woody-vegetation criterion and allows seasonal standing water, so equivalent
    scope across all vocabulary usages is not fully established. This disagreement
    is retained as a limitation, not silently rewritten or upgraded to exact source
    equivalence.
- assessment_id: PROVENANCE
  area: provenance
  topic: Source counters, triad roles and review lifecycle
  outcome: supported
  target_ids:
  - ENVO:00000233
  evidence_ids:
  - RECORD
  - RAW
  - CODE
  summary: BacDive index row59 reports 171 STRAIN and 149 distinct taxa; GOLD row565
    reports 8 ORGANISM; PREGO row675 reports 1 TAXON with score 4 and its isolate
    channel. These units are not additive. Separate GOLD bulk row792 reports 4 biosamples;
    triad rows431-433 describe 1 sample from 1 study with lake-biome, freshwater-lake
    and lake-water roles. Those contextual slots are not replacement identity or genus.
    The two exact path memberships at study rows844/3363 are not the triad study denominator.
    The original merged-source membership matrices were not independently re-extracted.
- assessment_id: ASSOCIATIONS
  area: evidence
  topic: Bounded taxon evidence and optional scientific content
  outcome: supported
  target_ids:
  - ENVO:00000233
  evidence_ids:
  - RECORD
  - RAW
  - CODE
  - TAXA
  - EPA
  - DSMZ
  summary: The one PREGO association and 25 BacDive associations reproduce, including
    rank/count/pool and the PREGO Trichococcus palustris corroboration flag. All 26
    current NCBI identifiers and stored names agree. DSMZ 9172 independently records
    strain Z-7189 from a swamp near Abramtsevo; this supports that bounded species
    association, not all 171 strains, every swamp or a characteristic taxon claim.
    Taxa include broad ranks and named strains; candidate_pool 149 is not the number
    of associations displayed. No environmental measurement or mechanism graph is
    supplied.
- assessment_id: CONTRACT
  area: grounding
  topic: Broad and related swamp aliases are promoted to exact equivalence
  outcome: concern
  target_ids:
  - ENVO:00000233
  evidence_ids:
  - RECORD
  - RAW
  - CODE
  - ONT0
  summary: Current official ENVO/OLS types wetland as BROAD and cienaga as RELATED;
    both are generated as EXACT_SYNONYM. The frozen ontology_terms row6816 has an
    untyped synonym pipe, and ConceptStore.get promotes each spelling to exact. The
    earlier BacDive/GOLD source-synonym correction does not repair these independent
    ontology assertions. True exact Swamp and swamp aliases should remain exact.
findings:
- finding_id: F1
  issue_key: envo-00000233-synonym-scope
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Broad and related swamp aliases are promoted to exact equivalence
  description: Current official ENVO/OLS types wetland as BROAD and cienaga as RELATED;
    both are generated as EXACT_SYNONYM. The frozen ontology_terms row6816 has an
    untyped synonym pipe, and ConceptStore.get promotes each spelling to exact. The
    earlier BacDive/GOLD source-synonym correction does not repair these independent
    ontology assertions. True exact Swamp and swamp aliases should remain exact.
  target_ids:
  - ENVO:00000233
  field_paths:
  - synonyms
  evidence_ids:
  - RECORD
  - RAW
  - RULES
  - CODE
  - ONT0
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained representation owner; generated YAML remains read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained representation owner; generated YAML remains read-only
  rule_id: docs/CURATION.md; docs/record-review-profile.md
  native_severity: major
  normalization_reason: Material representation or semantic-scope mismatch, not stylistic
    wording.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1249
actions:
- action_id: A1
  description: Preserve typed ontology synonym assertions through the governed source
    inventory and generator; treat unknown scope conservatively rather than as exact.
  finding_ids:
  - F1
  target_ids:
  - ENVO:00000233
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained representation owner; generated YAML remains read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained representation owner; generated YAML remains read-only
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Regenerate wetland as BROAD and cienaga as RELATED while retaining verified exact
    Swamp/swamp, PREGO related aliases and source-specific GOLD/BacDive related aliases.
  - Test multiple scopes for one spelling, unknown scope, and actual typed exact/broad/narrow/related
    inputs; do not globally downgrade every alias.
  - Refresh the source contract and provenance through native extraction, not manual
    generated YAML or checksum edits.
  - Append required curation history, regenerate through native writers, and pass
    schema, labels, provenance, exact reproduction, site and full QC. Preserve prior
    immutable reviews and use a linked successor to change this disposition.
limitations:
- Same-agent review, not independent approval or whole-corpus certification.
- Source occurrence and association membership was not independently rebuilt from
  original upstream matrices; frozen counters reproduce but do not establish characteristic
  presence. Live ontology and taxonomy resolution do not validate habitat occurrence.
- Ontology-label validation retains configured no-adapter skips and accepted exceptions;
  those skips are not scientific approval.
- Legacy reports are historical leads, not structured finding lineage; earlier corrections
  are not newly performed or silently reopened by this review.
- The assessment changes no habitat, decision, scientific status, history, generated
  site or map. Optional parameters, definitions and mechanisms are not invented.
- 'SSSOM/KGX compatibility was not audited. Shared endpoint issue #1398 and typed
  synonym issue #1249 remain open where applicable.'
tags:
- habitatmech
- record-review
- aquatic
```
