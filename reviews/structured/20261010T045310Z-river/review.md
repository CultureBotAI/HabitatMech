# Scientific record review: river

- Review: 20261010T045310Z-river
- Repository: culturebotai/HabitatMech
- Started UTC: 2026-10-10T04:34:40Z
- Finished UTC: 2026-10-10T04:53:10Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

River identity, stream genus and the separate GOLD CLOSE/PREGO association provenance are supported. One confirmed major finding remains: the source-path wastewater contribution is not a strict parent of a river feature. PREGO includes nonmicrobial taxa and two merged taxon IDs; these are explicitly qualified source associations, not automatically false edges or characteristic microbiota.

## Scope And Provenance

Scientific review of one resolved generated HabitatRecord and every emitted claim type.

Selection: Next individual target in the ongoing 3208-record review goal; this bundle certifies no other record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 52fa450b6cc0a9770482a574396cfe73d8dd2ba5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| ENVO:00000022 | data/habitats/engineered/river.yaml | generated | river |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native validate | passed | True | ENVO:00000022 | Executed 2026-10-10T04:35:12.478010+00:00 to 2026-10-10T04:35:14.669546+00:00. No issues found |
| Native validate-strict | passed | True | ENVO:00000022 | Executed 2026-10-10T04:35:22.767207+00:00 to 2026-10-10T04:35:27.509292+00:00.  |
| Native verify-corpus | passed | True | ENVO:00000022 | Executed 2026-10-10T04:35:27.510036+00:00 to 2026-10-10T04:35:40.737310+00:00. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ |
| Native validate-products | passed | True | ENVO:00000022 | Executed 2026-10-10T04:35:40.738259+00:00 to 2026-10-10T04:36:23.940534+00:00. id↔label correspondence summary:<br>          OK_CANONICAL: 1178<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2057<br><br>✅ All id↔label pairs correspond. |
| Native review-check | passed | True | ENVO:00000022 | Executed 2026-10-10T04:36:23.941225+00:00 to 2026-10-10T04:39:13.062429+00:00. {<br>  "repository": "culturebotai/HabitatMech",<br>  "valid_reviews": 101,<br>  "coverage": "declared_scopes_only"<br>}<br>....                                                                     [100%]<br>4 passed in 89.56s (0:01:29) |
| Exact-base full QC in CI | passed | True | ENVO:00000022 | Run metadata confirms exact head 52fa450b6cc0a9770482a574396cfe73d8dd2ba5 and success. Full QC: 657 passed, 3 skipped; 3208 validated and reproducing; all gates passed at 2026-10-10T04:30:23Z. Inspected CI evidence, not a fresh local full-QC execution. |
| Fresh native captures and complete local source trace | passed | True | ENVO:00000022 | Original capture preceded assessment. All 14 raw TSVs, seven root curation TSVs and PATHS were fully parsed. Entire target equals seed.build_document; contributor/status/parent attribution was inspected separately from scientific evidence. |
| Additional inspected inputs and original-hash preservation | passed | True | ENVO:00000022 | Native inspect added bounded search-hit overlays and, for river water, the legacy review. All original captured hashes and the Git base were preserved. 56 inputs for this target; all 202 prior review files unchanged. Ignored-inclusive structured inventory confirms 81 distinct completed targets in 101 bundles before this batch. |
| Complete dated workbook source census | passed | True | ENVO:00000022 | Both reused workbook SHA256 values freshly verified; all 244951 Biosample, 532019 Organism, 636914 SequencingProject and 63806 Study rows scanned, including headers. Classification has 2422 rows. Exact paths, then exact sample/organism IDs, determine joins. This is not a fresh download or the original frozen member roster. |
| Scientific baseline unchanged | passed | True | ENVO:00000022 | All maintained and generated scientific inputs remain unchanged. |
| Causal and expression applicability | not_applicable | False | ENVO:00000022 | No overlay targets this record; generic river/restroom hits belong to ENVO:00002019 and ENVO:00000073. No emitted causal, gene, regulator or expression claims require a target-specific graph check or iModulonDB adapter. |
| PREGO supporting-document retrieval | unavailable | False | ENVO:00000022 | Attempt returned curl 60, expired TLS certificate. No insecure bypass was used. Exact supporting-document inspection is unavailable; the local association inventory, primary methods and selected independent evidence remain inspectable. |

## Scientific And Domain Assessments

### Habitat identity and grounding scope

identity: supported. Targets: ENVO:00000022.

ENVO:00000022 denotes a flowing watercourse, not wastewater material. GOLD Engineered &gt; Wastewater &gt; River is ITEM-grounded CLOSE as a wastewater-receiving river; PREGO supplies the generic ENVO identity. EXACT aggregate status does not change the GOLD predicate. ENGINEERED is a source-priority heuristic, not proof that every instance of the merged ontology class is artificial or polluted.

### Strict parents versus context

grounding: concern. Targets: ENVO:00000022.

ENVO:00000023 stream is a genuine genus. ENVO:00002001 waste water denotes anthropogenically affected water material, not the receiving watercourse. Receiving or containing wastewater cannot establish the emitted river is-a wastewater edge. Its owner is the exact GOLD source-parent contribution keyed by habitatmech:GOLD.33a923764f, not the independent ENVO subclass.

### Microbial habitat support and claim placement

evidence: supported. Targets: ENVO:00000022.

PMID:23315724 compares benthic bacterial communities in wastewater-receiving rivers, supporting river-associated microbiota while keeping sediment, effluent and receiving ecosystem distinct. It does not corroborate all PREGO taxa. NCBI resolves all 25 emitted identifiers, including 110539 as an alias of 39687 and 115561 as an alias of 44935. Four entries have Metazoa lineage (10090, 10116, 104791, 105949), so the list cannot be described as exclusively microbial. The native taxon slot permits reported associations, and no is_characteristic flag is emitted; taxonomy alone does not justify deletion.

### Source extent, units, taxa and status

provenance: unknown. Targets: ENVO:00000022.

GOLD data row 1414 has nodes 5545&#124;5546 and zero organisms. PREGO habitat row 72 records 1143 TAXON associations, 1225 direct edge assertions and max score 4 across two channels. The 25 emitted ranks all score 4; tie ordering is deterministic, not abundance. Two contributing concepts have ITEM decisions (rows 382 and 1480), so REVIEWED reproduces. Later classification/bulk exact-path matches are absent; natural freshwater River and its later samples belong to another GOLD concept and are not transferred.

### Optional enrichment and audit boundaries

completeness: supported. Targets: ENVO:00000022.

No target causal graph, environmental parameter, discussion or dataset claim is emitted. Optional absence is not itself a defect. 2 contributing source concept(s), 2 ITEM-reviewed; generated status and source history reproduce. Parent parameters, taxa and graphs are not inherited, and this review does not promote native status.

### Validation is distinct from scientific approval

schema: supported. Targets: ENVO:00000022.

Fresh local native/schema, corpus, label and review checks passed. Exact-base CI QC passed. Required execution evidence does not resolve scientific uncertainty, and adapter-free label rows and skipped CI tests remain disclosed.

## Findings

### F1: Exclude the wastewater context parent from river

major / open / confirmed; issue key: gold-33a923764f-river-wastewater-context-parent.

The immediate GOLD path contributes ENVO:00002001 as if a river were a kind of wastewater. The reviewed source decision itself describes a river receiving wastewater. Watercourse identity is distinct from contained or incoming water material; exclude only that source-parent contribution.

## Recommended Actions And Acceptance Checks

### ACT1

The immediate GOLD path contributes ENVO:00002001 as if a river were a kind of wastewater. The reviewed source decision itself describes a river receiving wastewater. Watercourse identity is distinct from contained or incoming water material; exclude only that source-parent contribution.

- Add a guarded exclusion for habitatmech:GOLD.33a923764f, exact path Engineered &gt; Wastewater &gt; River, expected parent ENVO:00002001.
- Retain ontology parent ENVO:00000023, both source attestations, the GOLD CLOSE predicate, PREGO counts/scores/taxa and existing ITEM status.
- Regenerate through the native writer and verify that only the unsupported parent contribution and its required history/artifacts change.
- Append native curation history and focused regression tests for an authorized correction; preserve unrelated inputs and prior immutable reviews.
- Run affected schema/strict gates, corpus reproduction, applicable provenance/label gates and full QC.
- Save a linked immutable successor with the same issue key before closing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/engineered/river.yaml; Entire target YAML, all fields and generated history | supports | Full target read and source captured before assessment. Parent identity fields were inspected as context, not separately certified records. |
| E2 | data/raw/; Exact raw/curation data-row locators in Source extent assessment; data rows exclude header/comments | supports | Full structured parses trace identity, parents, source IDs/units, status and ranked taxa through the maintained source tables and seeder. Source reproducibility is not ecological validation. |
| R0 | docs/CURATION.md; Semantic invariants, decision depth and guarded GOLD parent exclusions; docs/HARMONIZATION.md and native checklist also read | supports | parent_habitats means strictly broader. Source context, taxonomy, MIxS roles and observed associations do not automatically establish identity, genus or characteristic presence. |
| E3 | curation/causal_graphs/; Ignored-inclusive rg over target identifiers, case-insensitive labels and slugs; full filesystem parse of reviews/structured | supports | No matching target overlay. Generic river/restroom text hits were resolved by overlay identifiers to different targets. No prior completed native review for these six targets; one river-water legacy report is explicitly retained. This is not an absence claim about all research or external databases. |
| V1 | https://github.com/CultureBotAI/HabitatMech/actions/runs/38023675552; Exact baseline metadata/log plus fresh local checks | supports | Schema, strict, corpus reproduction, ID-label and native-review gates passed locally. Full QC passed on the exact unchanged baseline in CI with three tests skipped. Label results: 1178 canonical, one synonym, five exceptions, 2057 without adapter. No general SSSOM/KGX readiness conclusion follows. |
| W1 | https://gold.jgi.doe.gov/download?mode=site_excel; Dated reused export; exact path census and exact ID joins; classification workbook at https://gold.jgi.doe.gov/download?mode=ecosystempaths | supports | Bulk SHA256 5f48b2f50fb2a9257754960a0f0e12dc6e8fa121e97c3e9f4497249e5fe6e439 (238974789 bytes); classification SHA256 3933e5f0664915c1bbfa00212e17d013da360fb33dd52e509254050813135396 (84174 bytes). Complete scans of all four bulk sheets and classification were performed for this batch; counts/selected locators are in the assessment. This later snapshot does not establish historical member identity. |
| T1 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=10090,10116,101510,1027,103,104097,1045010,104791,1053,1057,1058,105949,1061,106370,1076,108028,1082,1085,109902,109966,110479,110500,110539,114615,115561&amp;retmode=xml; Every emitted taxon ID, scientific name, rank, lineage and AkaTaxIds | supports | All emitted identifiers resolve directly or through explicit merged-ID aliases, and every supplied label matches. Taxonomic validity is not ecological or exclusively microbial evidence. |
| P0 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8879827/; Methods 2.3-2.4, Appendix C.1/C.3; PMID:35208748; DOI:10.3390/microorganisms10020293 | supports | PREGO combines annotated-genome metadata/text and sample co-occurrence using channel-specific scores. Scores and rank are not abundance, prevalence or proof of colonization; biological source scope still needs checking. |
| O1 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO:00000022; Active term labels, definitions and obsolescence for ENVO:00000022, ENVO:00000023, ENVO:00002001 | supports | The active river/stream definitions describe watercourses; waste water is an affected material, supporting a feature-versus-material distinction. |
| P1 | https://pubmed.ncbi.nlm.nih.gov/23315724/; Abstract; DOI:10.1128/AEM.03527-12 | supports | Field sampling compares river sediment microbiota around effluent inputs. This is positive bounded habitat evidence, not exact PREGO source validation. |

## Limits And Additional Notes

- Exact PREGO backing sample links are unavailable due to expired TLS. No ecological verification of all 1143 associations or exclusively microbial interpretation is claimed; merged taxon aliases are recorded without inventing invalid identifiers.
- Original frozen source membership is not reconstructed. Dated workbook bytes were reused and freshly checked; new source accesses are observations at review time, not changes to the frozen inventory.
- Full QC evidence is the inspected exact-base CI run, with three skipped tests; it is not a newly executed local full-QC run.
- Only the new review pair is written. This observation does not curate records, change scientific status or products, mutate GitHub, or establish whole-corpus or SSSOM/KGX readiness.
- Access timestamps mark completed inspection of source text or previously fetched bytes, not publication or fresh-download dates.
- Native inspect preceded assessment; later-added context was captured through inspect while preserving all earlier hashes. Legacy reports are contextual evidence, not native terminal dispositions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T045310Z-river
kind: record
repository: culturebotai/HabitatMech
title: 'Scientific record review: river'
started_at: '2026-10-10T04:34:40Z'
finished_at: '2026-10-10T04:53:10Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same continuing agent inspected the full record and its source
    claims; no independent reviewer approval is claimed.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'River identity, stream genus and the separate GOLD CLOSE/PREGO association
  provenance are supported. One confirmed major finding remains: the source-path wastewater
  contribution is not a strict parent of a river feature. PREGO includes nonmicrobial
  taxa and two merged taxon IDs; these are explicitly qualified source associations,
  not automatically false edges or characteristic microbiota.'
source:
  git_revision: 52fa450b6cc0a9770482a574396cfe73d8dd2ba5
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
    role: context
  - path: data/habitats/engineered/river.yaml
    sha256: 23adeede1c15dee36d63397b4995772e0ad1f96c065095c793b2a73ebb485fa8
    role: target
  - path: data/habitats/engineered/river_water.yaml
    sha256: 98bcdca83cba01d1d965ec21d76becfaf8776c26930cd770cc682138d542b803
    role: context
  - path: data/habitats/engineered/road.yaml
    sha256: 2b532c6a6d8ba2fe1fce692f5344eebdf49d6c88f0cf34140965f9008c976e87
    role: context
  - path: data/habitats/engineered/room_surface.yaml
    sha256: 7865923178f532bca96aa27016cb16b552be718dea8ea72114f3c81ad28c5ede
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
  - path: reviews/structured/20261010T040432Z-railway/review.md
    sha256: 558ad0e675ad1b987f4e958d6bb575044721b87f5202228644c216e525317b65
    role: context
  - path: reviews/structured/20261010T040432Z-railway/review.yaml
    sha256: 7fab5018b7d7fc31bac188f190a430f35ee51822a5cc637521b7759591c13d80
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
  description: Scientific review of one resolved generated HabitatRecord and every
    emitted claim type.
  selection: Next individual target in the ongoing 3208-record review goal; this bundle
    certifies no other record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - ENVO:00000022
  exclusions:
  - target: Other habitat records and complete external database membership
    reason: Parent identity and selected later source members provide context, not
      separately completed target reviews.
targets:
- target_id: ENVO:00000022
  path: data/habitats/engineered/river.yaml
  label: river
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
checks:
- check_id: C1
  name: Native validate
  command: just validate data/habitats/engineered/river.yaml
  summary: Executed 2026-10-10T04:35:12.478010+00:00 to 2026-10-10T04:35:14.669546+00:00.
    No issues found
  status: passed
  required: true
  target_ids:
  - ENVO:00000022
  exit_code: 0
- check_id: C2
  name: Native validate-strict
  command: just validate-strict data/habitats/engineered/research_nuclear_reactor.yaml
    data/habitats/engineered/rice_straw.yaml data/habitats/engineered/river.yaml data/habitats/engineered/river_water.yaml
    data/habitats/engineered/road.yaml data/habitats/engineered/room_surface.yaml
  summary: 'Executed 2026-10-10T04:35:22.767207+00:00 to 2026-10-10T04:35:27.509292+00:00. '
  status: passed
  required: true
  target_ids:
  - ENVO:00000022
  exit_code: 0
- check_id: C3
  name: Native verify-corpus
  command: just verify-corpus
  summary: "Executed 2026-10-10T04:35:27.510036+00:00 to 2026-10-10T04:35:40.737310+00:00.\
    \ expected 3208 records, found 3208 on disk\n  missing:   0\n  extra:     0\n\
    \  differing: 0\n\ncorpus reproduces exactly from data/raw/"
  status: passed
  required: true
  target_ids:
  - ENVO:00000022
  exit_code: 0
- check_id: C4
  name: Native validate-products
  command: just validate-products
  summary: "Executed 2026-10-10T04:35:40.738259+00:00 to 2026-10-10T04:36:23.940534+00:00.\
    \ id↔label correspondence summary:\n          OK_CANONICAL: 1178\n           \
    \ OK_SYNONYM: 1\n          OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2057\n\n✅\
    \ All id↔label pairs correspond."
  status: passed
  required: true
  target_ids:
  - ENVO:00000022
  exit_code: 0
- check_id: C5
  name: Native review-check
  command: just review-check
  summary: "Executed 2026-10-10T04:36:23.941225+00:00 to 2026-10-10T04:39:13.062429+00:00.\
    \ {\n  \"repository\": \"culturebotai/HabitatMech\",\n  \"valid_reviews\": 101,\n\
    \  \"coverage\": \"declared_scopes_only\"\n}\n....                           \
    \                                          [100%]\n4 passed in 89.56s (0:01:29)"
  status: passed
  required: true
  target_ids:
  - ENVO:00000022
  exit_code: 0
- check_id: C6
  name: Exact-base full QC in CI
  command: gh run view 38023675552 --log | rg '[0-9]+ passed|All HabitatMech quality
    gates|history records|files scanned|differing'
  summary: 'Run metadata confirms exact head 52fa450b6cc0a9770482a574396cfe73d8dd2ba5
    and success. Full QC: 657 passed, 3 skipped; 3208 validated and reproducing; all
    gates passed at 2026-10-10T04:30:23Z. Inspected CI evidence, not a fresh local
    full-QC execution.'
  status: passed
  required: true
  target_ids:
  - ENVO:00000022
  exit_code: 0
- check_id: C7
  name: Fresh native captures and complete local source trace
  command: uv run python /private/tmp/habitatmech-review-x-prepare.py
  summary: Original capture preceded assessment. All 14 raw TSVs, seven root curation
    TSVs and PATHS were fully parsed. Entire target equals seed.build_document; contributor/status/parent
    attribution was inspected separately from scientific evidence.
  status: passed
  required: true
  target_ids:
  - ENVO:00000022
  exit_code: 0
- check_id: C8
  name: Additional inspected inputs and original-hash preservation
  command: .venv/bin/python /private/tmp/habitatmech-review-x-recheck.py
  summary: Native inspect added bounded search-hit overlays and, for river water,
    the legacy review. All original captured hashes and the Git base were preserved.
    56 inputs for this target; all 202 prior review files unchanged. Ignored-inclusive
    structured inventory confirms 81 distinct completed targets in 101 bundles before
    this batch.
  status: passed
  required: true
  target_ids:
  - ENVO:00000022
  exit_code: 0
- check_id: C9
  name: Complete dated workbook source census
  command: .venv/bin/python /private/tmp/habitatmech-review-x-workbook.py
  summary: Both reused workbook SHA256 values freshly verified; all 244951 Biosample,
    532019 Organism, 636914 SequencingProject and 63806 Study rows scanned, including
    headers. Classification has 2422 rows. Exact paths, then exact sample/organism
    IDs, determine joins. This is not a fresh download or the original frozen member
    roster.
  status: passed
  required: true
  target_ids:
  - ENVO:00000022
  exit_code: 0
- check_id: C10
  name: Scientific baseline unchanged
  command: git diff --exit-code 52fa450b6cc0a9770482a574396cfe73d8dd2ba5 -- data src
    curation history scripts docs conf .claude justfile schema
  summary: All maintained and generated scientific inputs remain unchanged.
  status: passed
  required: true
  target_ids:
  - ENVO:00000022
  exit_code: 0
- check_id: C11
  name: Causal and expression applicability
  summary: No overlay targets this record; generic river/restroom hits belong to ENVO:00002019
    and ENVO:00000073. No emitted causal, gene, regulator or expression claims require
    a target-specific graph check or iModulonDB adapter.
  status: not_applicable
  required: false
  target_ids:
  - ENVO:00000022
- check_id: C12
  name: PREGO supporting-document retrieval
  command: curl -fSsL --max-time 45 https://prego.hcmr.gr/
  summary: Attempt returned curl 60, expired TLS certificate. No insecure bypass was
    used. Exact supporting-document inspection is unavailable; the local association
    inventory, primary methods and selected independent evidence remain inspectable.
  status: unavailable
  required: false
  target_ids:
  - ENVO:00000022
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/engineered/river.yaml
  locator: Entire target YAML, all fields and generated history
  accessed_at: '2026-10-10T04:53:10Z'
  support: supports
  summary: Full target read and source captured before assessment. Parent identity
    fields were inspected as context, not separately certified records.
- evidence_id: E2
  kind: database
  reference: data/raw/
  locator: Exact raw/curation data-row locators in Source extent assessment; data
    rows exclude header/comments
  accessed_at: '2026-10-10T04:53:10Z'
  support: supports
  summary: Full structured parses trace identity, parents, source IDs/units, status
    and ranked taxa through the maintained source tables and seeder. Source reproducibility
    is not ecological validation.
- evidence_id: R0
  kind: authority
  reference: docs/CURATION.md
  locator: Semantic invariants, decision depth and guarded GOLD parent exclusions;
    docs/HARMONIZATION.md and native checklist also read
  accessed_at: '2026-10-10T04:53:10Z'
  support: supports
  summary: parent_habitats means strictly broader. Source context, taxonomy, MIxS
    roles and observed associations do not automatically establish identity, genus
    or characteristic presence.
- evidence_id: E3
  kind: search
  reference: curation/causal_graphs/
  locator: Ignored-inclusive rg over target identifiers, case-insensitive labels and
    slugs; full filesystem parse of reviews/structured
  accessed_at: '2026-10-10T04:53:10Z'
  support: supports
  summary: No matching target overlay. Generic river/restroom text hits were resolved
    by overlay identifiers to different targets. No prior completed native review
    for these six targets; one river-water legacy report is explicitly retained. This
    is not an absence claim about all research or external databases.
  search_scope: Ignored-inclusive rg over target identifiers, case-insensitive labels
    and slugs; full filesystem parse of reviews/structured; No matching target overlay.
    Generic river/restroom text hits were resolved by overlay identifiers to different
    targets. No prior completed native review for these six targets; one river-water
    legacy report is explicitly retained. This is not an absence claim about all research
    or external databases.
- evidence_id: V1
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38023675552
  locator: Exact baseline metadata/log plus fresh local checks
  accessed_at: '2026-10-10T04:53:10Z'
  support: supports
  summary: 'Schema, strict, corpus reproduction, ID-label and native-review gates
    passed locally. Full QC passed on the exact unchanged baseline in CI with three
    tests skipped. Label results: 1178 canonical, one synonym, five exceptions, 2057
    without adapter. No general SSSOM/KGX readiness conclusion follows.'
- evidence_id: W1
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=site_excel
  locator: Dated reused export; exact path census and exact ID joins; classification
    workbook at https://gold.jgi.doe.gov/download?mode=ecosystempaths
  accessed_at: '2026-10-10T04:53:10Z'
  support: supports
  summary: Bulk SHA256 5f48b2f50fb2a9257754960a0f0e12dc6e8fa121e97c3e9f4497249e5fe6e439
    (238974789 bytes); classification SHA256 3933e5f0664915c1bbfa00212e17d013da360fb33dd52e509254050813135396
    (84174 bytes). Complete scans of all four bulk sheets and classification were
    performed for this batch; counts/selected locators are in the assessment. This
    later snapshot does not establish historical member identity.
- evidence_id: T1
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=10090,10116,101510,1027,103,104097,1045010,104791,1053,1057,1058,105949,1061,106370,1076,108028,1082,1085,109902,109966,110479,110500,110539,114615,115561&retmode=xml
  locator: Every emitted taxon ID, scientific name, rank, lineage and AkaTaxIds
  accessed_at: '2026-10-10T04:53:10Z'
  support: supports
  summary: All emitted identifiers resolve directly or through explicit merged-ID
    aliases, and every supplied label matches. Taxonomic validity is not ecological
    or exclusively microbial evidence.
- evidence_id: P0
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC8879827/
  locator: Methods 2.3-2.4, Appendix C.1/C.3; PMID:35208748; DOI:10.3390/microorganisms10020293
  accessed_at: '2026-10-10T04:53:10Z'
  support: supports
  summary: PREGO combines annotated-genome metadata/text and sample co-occurrence
    using channel-specific scores. Scores and rank are not abundance, prevalence or
    proof of colonization; biological source scope still needs checking.
- evidence_id: O1
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO:00000022
  locator: Active term labels, definitions and obsolescence for ENVO:00000022, ENVO:00000023,
    ENVO:00002001
  accessed_at: '2026-10-10T04:53:10Z'
  support: supports
  summary: The active river/stream definitions describe watercourses; waste water
    is an affected material, supporting a feature-versus-material distinction.
- evidence_id: P1
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/23315724/
  locator: Abstract; DOI:10.1128/AEM.03527-12
  accessed_at: '2026-10-10T04:53:10Z'
  support: supports
  summary: Field sampling compares river sediment microbiota around effluent inputs.
    This is positive bounded habitat evidence, not exact PREGO source validation.
assessments:
- assessment_id: A1
  area: identity
  topic: Habitat identity and grounding scope
  outcome: supported
  summary: ENVO:00000022 denotes a flowing watercourse, not wastewater material. GOLD
    Engineered > Wastewater > River is ITEM-grounded CLOSE as a wastewater-receiving
    river; PREGO supplies the generic ENVO identity. EXACT aggregate status does not
    change the GOLD predicate. ENGINEERED is a source-priority heuristic, not proof
    that every instance of the merged ontology class is artificial or polluted.
  target_ids:
  - ENVO:00000022
  evidence_ids:
  - E1
  - E2
  - O1
  - R0
- assessment_id: A2
  area: grounding
  topic: Strict parents versus context
  outcome: concern
  summary: ENVO:00000023 stream is a genuine genus. ENVO:00002001 waste water denotes
    anthropogenically affected water material, not the receiving watercourse. Receiving
    or containing wastewater cannot establish the emitted river is-a wastewater edge.
    Its owner is the exact GOLD source-parent contribution keyed by habitatmech:GOLD.33a923764f,
    not the independent ENVO subclass.
  target_ids:
  - ENVO:00000022
  evidence_ids:
  - E1
  - E2
  - O1
  - R0
- assessment_id: A3
  area: evidence
  topic: Microbial habitat support and claim placement
  outcome: supported
  summary: PMID:23315724 compares benthic bacterial communities in wastewater-receiving
    rivers, supporting river-associated microbiota while keeping sediment, effluent
    and receiving ecosystem distinct. It does not corroborate all PREGO taxa. NCBI
    resolves all 25 emitted identifiers, including 110539 as an alias of 39687 and
    115561 as an alias of 44935. Four entries have Metazoa lineage (10090, 10116,
    104791, 105949), so the list cannot be described as exclusively microbial. The
    native taxon slot permits reported associations, and no is_characteristic flag
    is emitted; taxonomy alone does not justify deletion.
  target_ids:
  - ENVO:00000022
  evidence_ids:
  - E1
  - E2
  - T1
  - P1
  - P0
  - R0
- assessment_id: A4
  area: provenance
  topic: Source extent, units, taxa and status
  outcome: unknown
  summary: GOLD data row 1414 has nodes 5545|5546 and zero organisms. PREGO habitat
    row 72 records 1143 TAXON associations, 1225 direct edge assertions and max score
    4 across two channels. The 25 emitted ranks all score 4; tie ordering is deterministic,
    not abundance. Two contributing concepts have ITEM decisions (rows 382 and 1480),
    so REVIEWED reproduces. Later classification/bulk exact-path matches are absent;
    natural freshwater River and its later samples belong to another GOLD concept
    and are not transferred.
  target_ids:
  - ENVO:00000022
  evidence_ids:
  - E1
  - E2
  - R0
  - W1
  - P0
  - T1
- assessment_id: A5
  area: completeness
  topic: Optional enrichment and audit boundaries
  outcome: supported
  summary: No target causal graph, environmental parameter, discussion or dataset
    claim is emitted. Optional absence is not itself a defect. 2 contributing source
    concept(s), 2 ITEM-reviewed; generated status and source history reproduce. Parent
    parameters, taxa and graphs are not inherited, and this review does not promote
    native status.
  target_ids:
  - ENVO:00000022
  evidence_ids:
  - E1
  - E2
  - E3
  - R0
- assessment_id: A6
  area: schema
  topic: Validation is distinct from scientific approval
  outcome: supported
  summary: Fresh local native/schema, corpus, label and review checks passed. Exact-base
    CI QC passed. Required execution evidence does not resolve scientific uncertainty,
    and adapter-free label rows and skipped CI tests remain disclosed.
  target_ids:
  - ENVO:00000022
  evidence_ids:
  - V1
findings:
- issue_key: gold-33a923764f-river-wastewater-context-parent
  severity: major
  certainty: confirmed
  category: grounding
  title: Exclude the wastewater context parent from river
  description: The immediate GOLD path contributes ENVO:00002001 as if a river were
    a kind of wastewater. The reviewed source decision itself describes a river receiving
    wastewater. Watercourse identity is distinct from contained or incoming water
    material; exclude only that source-parent contribution.
  field_paths:
  - parent_habitats
  evidence_ids:
  - E1
  - E2
  - O1
  - R0
  finding_id: F1
  status: open
  target_ids:
  - ENVO:00000022
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or source transformation; generated habitat YAML is read-only
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or source transformation; generated habitat YAML is read-only
  native_severity: major
  rule_id: Native strict-parent, source-equivalence and scoped-provenance rules
  normalization_reason: False strict parents and unresolved material identity are
    major; bounded source-substrate provenance discrepancies without a proved false
    identity are minor. Certainty is recorded separately from severity.
actions:
- action_id: ACT1
  description: The immediate GOLD path contributes ENVO:00002001 as if a river were
    a kind of wastewater. The reviewed source decision itself describes a river receiving
    wastewater. Watercourse identity is distinct from contained or incoming water
    material; exclude only that source-parent contribution.
  finding_ids:
  - F1
  target_ids:
  - ENVO:00000022
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or source transformation; generated habitat YAML is read-only
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or source transformation; generated habitat YAML is read-only
  generator: 'Only after supported maintained-input curation: just seed; inspect just
    seed-canary <identifier>; guarded seed-apply and just render as applicable.'
  acceptance_checks:
  - Add a guarded exclusion for habitatmech:GOLD.33a923764f, exact path Engineered
    > Wastewater > River, expected parent ENVO:00002001.
  - Retain ontology parent ENVO:00000023, both source attestations, the GOLD CLOSE
    predicate, PREGO counts/scores/taxa and existing ITEM status.
  - Regenerate through the native writer and verify that only the unsupported parent
    contribution and its required history/artifacts change.
  - Append native curation history and focused regression tests for an authorized
    correction; preserve unrelated inputs and prior immutable reviews.
  - Run affected schema/strict gates, corpus reproduction, applicable provenance/label
    gates and full QC.
  - Save a linked immutable successor with the same issue key before closing this
    finding.
limitations:
- Exact PREGO backing sample links are unavailable due to expired TLS. No ecological
  verification of all 1143 associations or exclusively microbial interpretation is
  claimed; merged taxon aliases are recorded without inventing invalid identifiers.
- Original frozen source membership is not reconstructed. Dated workbook bytes were
  reused and freshly checked; new source accesses are observations at review time,
  not changes to the frozen inventory.
- Full QC evidence is the inspected exact-base CI run, with three skipped tests; it
  is not a newly executed local full-QC run.
- Only the new review pair is written. This observation does not curate records, change
  scientific status or products, mutate GitHub, or establish whole-corpus or SSSOM/KGX
  readiness.
notes:
- Access timestamps mark completed inspection of source text or previously fetched
  bytes, not publication or fresh-download dates.
- Native inspect preceded assessment; later-added context was captured through inspect
  while preserving all earlier hashes. Legacy reports are contextual evidence, not
  native terminal dispositions.
tags:
- habitatmech
- engineered
- scientific-record-review
```
