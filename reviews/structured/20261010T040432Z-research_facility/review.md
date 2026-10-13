# Scientific record review: research facility

- Review: 20261010T040432Z-research_facility
- Repository: culturebotai/HabitatMech
- Started UTC: 2026-10-10T03:54:22Z
- Finished UTC: 2026-10-10T04:04:32Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The active ENVO facility identity and human-construction parent agree with the record. PREGO source channel, 339-taxon pool, 25 emitted ranks and all taxon labels reproduce. A primary facility study supports microbial habitat plausibility, not the exact PREGO roster. Qualified pass with source-link limitations and no corrective finding.

## Scope And Provenance

Scientific review of one resolved generated HabitatRecord and its contributing claims.

Selection: Next individual target in the continuing 3208-record goal; publication does not imply whole-corpus completion.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f749c54812886458d7b5a09796055c54180ab78e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| ENVO:00000469 | data/habitats/engineered/research_facility.yaml | generated | research facility |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native validate | passed | True | ENVO:00000469 | Executed 2026-10-10T03:55:00.181753+00:00 to 2026-10-10T03:55:02.530586+00:00; exit 0. No issues found |
| Native validate-strict | passed | True | ENVO:00000469 | Executed 2026-10-10T03:55:02.531340+00:00 to 2026-10-10T03:55:08.640591+00:00; exit 0.  |
| Native verify-corpus | passed | True | ENVO:00000469 | Executed 2026-10-10T03:55:08.641251+00:00 to 2026-10-10T03:55:23.798702+00:00; exit 0. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ |
| Native validate-products | passed | True | ENVO:00000469 | Executed 2026-10-10T03:55:23.799371+00:00 to 2026-10-10T03:56:06.256283+00:00; exit 0. id↔label correspondence summary:<br>          OK_CANONICAL: 1178<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2057<br><br>✅ All id↔label pairs correspond. |
| Native review-check | passed | True | ENVO:00000469 | Executed 2026-10-10T03:56:06.257046+00:00 to 2026-10-10T03:58:56.767389+00:00; exit 0. {<br>  "repository": "culturebotai/HabitatMech",<br>  "valid_reviews": 95,<br>  "coverage": "declared_scopes_only"<br>}<br>....                                                                     [100%]<br>4 passed in 87.75s (0:01:27) |
| Exact-base full QC in CI | passed | True | ENVO:00000469 | Run metadata verifies f749c54812886458d7b5a09796055c54180ab78e and success. Full QC: 657 passed, 3 skipped, 3208 validated and reproducing; all gates passed at 2026-10-10T03:50:03Z. This is inspected CI evidence, not a new local full-QC execution. |
| Fresh native capture and source trace | passed | True | ENVO:00000469 | Six target captures each hash 53 inputs. Full documents equal seed.build_document; all 14 raw TSVs, seven root curation TSVs and PATHS parsed without ignore filtering. One contributor and zero ITEM-reviewed contributors per target. Captured hashes rechecked before authoring. |
| Dated workbook hashes | passed | True | ENVO:00000469 | Fresh SHA256 verification matches the prior complete census. Parser and selected joined rows reread. No new bulk download or census is claimed. |
| Scientific baseline unchanged | passed | True | ENVO:00000469 | No maintained/generated scientific inputs changed during assessment. |
| Causal overlay and expression applicability | not_applicable | False | ENVO:00000469 | These targets emit no causal edges, genes, regulators or transcriptomic claims. Ignored-inclusive search found no matching causal overlay; iModulonDB and target-specific causal validation are not applicable. |
| PREGO supporting links | unavailable | False | ENVO:00000469 | The retrieval attempt returned curl 60: expired TLS certificate prevented secure access to backing links. Initial sandbox DNS failures were retried successfully for ENA, OLS and NCBI with authorized network access; PREGO TLS failure remained. The scientific supporting-link check could not execute. |

## Scientific And Domain Assessments

### Identity and strict hierarchy

identity: supported. Targets: ENVO:00000469.

ENVO:00000469 denotes a facility for scientific research or measurement, including temporary facilities in different settings. ENVO:00000070 human construction is an appropriate broader class. Research facilities is a PREGO related synonym, not a separately merged source concept. A laboratory facility can be narrower; its GOLD triad usage does not redefine this PREGO identity.

### Microbial support and source scope

evidence: supported. Targets: ENVO:00000469.

PMID:34861887 reports microbial sampling of a spacecraft assembly facility, including culture and sequence-based methods. It provides an example of facility-associated microbiota, not confirmation of all emitted PREGO taxa or universal viability. NCBI resolves all 25 emitted identifiers/names, including four strain-rank entries. Ecological expectations about food-associated species are not sufficient to reject these source associations.

### Source units, scores, extent and status

provenance: unknown. Targets: ENVO:00000469.

PREGO data row 114 reports 339 TAXON associations and maximum score 1.75033 from environmental_samples. The 25 emitted records retain ranks 1-25, pool 339 and scores 1.75033 down to 1.36219, without is_characteristic flags. PREGO describes metadata-based co-occurrence with channel-specific scoring, not prevalence or abundance. Missing original sample links limit ecological verification, not reproducibility of the maintained inventory.

### Claim placement and optional enrichment

completeness: supported. Targets: ENVO:00000469.

No target causal graph, environmental parameter, discussion or dataset claim is emitted. Optional absent fields, CLASS decisions and SEEDED state alone are not defects. One source contributes and zero are ITEM-reviewed; no scientific status is promoted. Parent taxa, parameters and graphs are not inherited as target claims.

### Validation versus scientific certification

schema: supported. Targets: ENVO:00000469.

Fresh native target/schema, corpus, label and review checks pass. Exact unchanged baseline passed full CI QC. The assessment retains source limitations; validator success does not settle identity or provenance questions.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/engineered/research_facility.yaml; Entire target YAML including history and all optional fields | supports | Full target read; captured with native inspect before assessment. Parent identity fields and all contributing source/decision rows examined; no full scientific certification of parent records is claimed. |
| E2 | data/raw/; Exact source rows and curation rows identified in assessments; data-row numbering excludes header/comments | supports | All raw and root curation TSVs plus PATHS parsed. Full generated document matches the seeder; count, score, parent and status meanings evaluated separately from deterministic equality. |
| E3 | curation/causal_graphs/; rg --no-ignore --hidden over curation/causal_graphs, research/habitats and history; identifiers, labels, slugs | supports | Ignored files included. No target causal overlay matched. Related material, subway and reptile research reports are leads only. Bounded find through configured kg-microbe/data to depth 3 and /private/tmp to depth 1 found no PREGO dumps; this is not a whole-filesystem absence claim. |
| V1 | https://github.com/CultureBotAI/HabitatMech/actions/runs/38021322406; Exact-base run metadata/log and fresh local gate receipts | supports | Required schema, strict, corpus, label and native-review gates passed locally; baseline full QC passed in CI with three skipped tests. ID-label gate: 1178 canonical, 1 synonym, 5 exceptions, 2057 without adapter. Deterministic success is not scientific approval. |
| T1 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=164393,153496,185294,903522,28038,880633,1553,438,1530,1701,1494,115778,765118,1254,442,1534,104102,33954,1615,1599,320497,231024,889932,322009,1580&amp;retmode=xml; Every emitted taxon ID and scientific name | supports | Fresh NCBI response confirms target taxon identifiers and labels; taxonomic validity does not establish ecological association. |
| P2 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8879827/; Methods 2.3-2.4 and Appendix C.1/C.3; PMID:35208748, DOI:10.3390/microorganisms10020293 | supports | PREGO derives associations from metadata/text or sample co-occurrence. Its channel-specific scores are not abundance or proof of a characteristic taxon. |
| O1 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO:00000469; Active definition; ENVO:00000070 also inspected | supports | Research facility and its broader construction class remain active and match the target meaning. |
| P1 | https://pubmed.ncbi.nlm.nih.gov/34861887/; Abstract; DOI:10.1186/s40168-021-01159-x | supports | A primary spacecraft-assembly-facility study characterizes microbial samples using culture and molecular methods. It is a positive facility example, not exact PREGO source-member support. |

## Limits And Additional Notes

- PREGO backing sample links are unavailable because HTTPS certificate validation failed. No independent validation of all 339 source associations is claimed.
- Original frozen source membership is not reconstructed. Later workbook evidence is dated and reused; full QC is inspected exact-base CI evidence, with three tests skipped.
- This observation writes only its immutable review pair. It does not change generated scientific records, curation status or products, and makes no SSSOM/KGX readiness claim.
- Access timestamps denote completed inspection of source text or reused cached evidence, not publication or download dates. Native inspect preceded assessment; all 53 captured hashes remained unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T040432Z-research_facility
kind: record
repository: culturebotai/HabitatMech
title: 'Scientific record review: research facility'
started_at: '2026-10-10T03:54:22Z'
finished_at: '2026-10-10T04:04:32Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same continuing agent assessed source and generated claims;
    no independent human or second-agent approval is claimed.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The active ENVO facility identity and human-construction parent agree with
  the record. PREGO source channel, 339-taxon pool, 25 emitted ranks and all taxon
  labels reproduce. A primary facility study supports microbial habitat plausibility,
  not the exact PREGO roster. Qualified pass with source-link limitations and no corrective
  finding.
source:
  git_revision: f749c54812886458d7b5a09796055c54180ab78e
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
  - path: data/habitats/engineered/animal_cage.yaml
    sha256: 82712b7be271d6729c1f1053add0c5d9491ef8cfd4fffcce7d9dd2bff010c72c
    role: context
  - path: data/habitats/engineered/chemical_product.yaml
    sha256: d5039d8e0f3f8c77680371d162d7934f5ada70d63130e5a1b4bcab154bb77b1f
    role: context
  - path: data/habitats/engineered/human_construction.yaml
    sha256: cb18d75802047037b046072cb47805a8f2db1123b99cd346e690ad6e4065a3ea
    role: context
  - path: data/habitats/engineered/influent.yaml
    sha256: 5040657ce6cf92c03a2e172301c565de09ca6e850a3ac5f0cc2fa5e26bc82b10
    role: context
  - path: data/habitats/engineered/railway.yaml
    sha256: af6f402568c66c00b2a810888f05492062d79076a745cc879e44a7b361b0a2eb
    role: context
  - path: data/habitats/engineered/raw_wastewater.yaml
    sha256: 3a1395e27037fd2afa3421b2ccdabc7725f774a8e17f6fc713d33e72932b4a63
    role: context
  - path: data/habitats/engineered/reagent_blank.yaml
    sha256: 3c3676402b35bb99ac4b63c959692e6a86aa9e0bb0cb8183b5f2d5bc7ec4ba97
    role: context
  - path: data/habitats/engineered/reclaimed_recycled_wastewater.yaml
    sha256: fc9722654e63ae555b14ff6925210bbb19b51e84030dd6e750054558642fb0e8
    role: context
  - path: data/habitats/engineered/reptile_cage.yaml
    sha256: 1389ad0e17e24bd302944c3cd01f2f4be283b1a99841ecfa17e55b01d21d63ee
    role: context
  - path: data/habitats/engineered/research_facility.yaml
    sha256: 506dd0b31a4299e62764461725a2e69718b3a7963b7e7069aa8e1af5a2714575
    role: target
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
  - path: reviews/structured/20261009T201157Z-pcr_blank_control/review.md
    sha256: 8923db1e9f9d5044a375eb319e6c262d4d2c74f1ac925d0a49dd816ce976edf4
    role: context
  - path: reviews/structured/20261009T201157Z-pcr_blank_control/review.yaml
    sha256: c159bdee3b1e0517ba1ac5dd08ad6e0815a8a8903bc708a73bff78de2c6b5b16
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
  description: Scientific review of one resolved generated HabitatRecord and its contributing
    claims.
  selection: Next individual target in the continuing 3208-record goal; publication
    does not imply whole-corpus completion.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - ENVO:00000469
  exclusions:
  - target: Other records and full external database membership
    reason: Parents and selected later source members are context, not separately
      certified targets.
targets:
- target_id: ENVO:00000469
  path: data/habitats/engineered/research_facility.yaml
  label: research facility
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
  status: passed
  required: true
  command: just validate data/habitats/engineered/research_facility.yaml
  exit_code: 0
  target_ids:
  - ENVO:00000469
  summary: Executed 2026-10-10T03:55:00.181753+00:00 to 2026-10-10T03:55:02.530586+00:00;
    exit 0. No issues found
- check_id: C2
  name: Native validate-strict
  status: passed
  required: true
  command: just validate-strict data/habitats/engineered/railway.yaml data/habitats/engineered/raw_wastewater.yaml
    data/habitats/engineered/reagent_blank.yaml data/habitats/engineered/reclaimed_recycled_wastewater.yaml
    data/habitats/engineered/reptile_cage.yaml data/habitats/engineered/research_facility.yaml
  exit_code: 0
  target_ids:
  - ENVO:00000469
  summary: 'Executed 2026-10-10T03:55:02.531340+00:00 to 2026-10-10T03:55:08.640591+00:00;
    exit 0. '
- check_id: C3
  name: Native verify-corpus
  status: passed
  required: true
  command: just verify-corpus
  exit_code: 0
  target_ids:
  - ENVO:00000469
  summary: "Executed 2026-10-10T03:55:08.641251+00:00 to 2026-10-10T03:55:23.798702+00:00;\
    \ exit 0. expected 3208 records, found 3208 on disk\n  missing:   0\n  extra:\
    \     0\n  differing: 0\n\ncorpus reproduces exactly from data/raw/"
- check_id: C4
  name: Native validate-products
  status: passed
  required: true
  command: just validate-products
  exit_code: 0
  target_ids:
  - ENVO:00000469
  summary: "Executed 2026-10-10T03:55:23.799371+00:00 to 2026-10-10T03:56:06.256283+00:00;\
    \ exit 0. id↔label correspondence summary:\n          OK_CANONICAL: 1178\n   \
    \         OK_SYNONYM: 1\n          OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2057\n\
    \n✅ All id↔label pairs correspond."
- check_id: C5
  name: Native review-check
  status: passed
  required: true
  command: just review-check
  exit_code: 0
  target_ids:
  - ENVO:00000469
  summary: "Executed 2026-10-10T03:56:06.257046+00:00 to 2026-10-10T03:58:56.767389+00:00;\
    \ exit 0. {\n  \"repository\": \"culturebotai/HabitatMech\",\n  \"valid_reviews\"\
    : 95,\n  \"coverage\": \"declared_scopes_only\"\n}\n....                     \
    \                                                [100%]\n4 passed in 87.75s (0:01:27)"
- check_id: C6
  name: Exact-base full QC in CI
  status: passed
  required: true
  command: gh run view 38021322406 --log | rg '[0-9]+ passed|All HabitatMech quality
    gates|history records|files scanned|differing'
  exit_code: 0
  target_ids:
  - ENVO:00000469
  summary: 'Run metadata verifies f749c54812886458d7b5a09796055c54180ab78e and success.
    Full QC: 657 passed, 3 skipped, 3208 validated and reproducing; all gates passed
    at 2026-10-10T03:50:03Z. This is inspected CI evidence, not a new local full-QC
    execution.'
- check_id: C7
  name: Fresh native capture and source trace
  status: passed
  required: true
  command: uv run python /private/tmp/habitatmech-review-w-prepare.py
  exit_code: 0
  target_ids:
  - ENVO:00000469
  summary: Six target captures each hash 53 inputs. Full documents equal seed.build_document;
    all 14 raw TSVs, seven root curation TSVs and PATHS parsed without ignore filtering.
    One contributor and zero ITEM-reviewed contributors per target. Captured hashes
    rechecked before authoring.
- check_id: C8
  name: Dated workbook hashes
  status: passed
  required: true
  command: shasum -a 256 /private/tmp/habitatmech-20261009h-goldData.xlsx /private/tmp/habitatmech-review-n-ecosystems.xlsx
    /private/tmp/habitatmech-review-v-workbook-result.json
  exit_code: 0
  target_ids:
  - ENVO:00000469
  summary: Fresh SHA256 verification matches the prior complete census. Parser and
    selected joined rows reread. No new bulk download or census is claimed.
- check_id: C9
  name: Scientific baseline unchanged
  status: passed
  required: true
  command: git diff --exit-code f749c54812886458d7b5a09796055c54180ab78e -- data src
    curation history scripts docs conf .claude justfile schema
  exit_code: 0
  target_ids:
  - ENVO:00000469
  summary: No maintained/generated scientific inputs changed during assessment.
- check_id: C10
  name: Causal overlay and expression applicability
  status: not_applicable
  required: false
  target_ids:
  - ENVO:00000469
  summary: These targets emit no causal edges, genes, regulators or transcriptomic
    claims. Ignored-inclusive search found no matching causal overlay; iModulonDB
    and target-specific causal validation are not applicable.
- check_id: C11
  name: PREGO supporting links
  status: unavailable
  required: false
  target_ids:
  - ENVO:00000469
  command: curl -fSsL --max-time 45 https://prego.hcmr.gr/
  summary: 'The retrieval attempt returned curl 60: expired TLS certificate prevented
    secure access to backing links. Initial sandbox DNS failures were retried successfully
    for ENA, OLS and NCBI with authorized network access; PREGO TLS failure remained.
    The scientific supporting-link check could not execute.'
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/engineered/research_facility.yaml
  locator: Entire target YAML including history and all optional fields
  accessed_at: '2026-10-10T04:04:32Z'
  support: supports
  summary: Full target read; captured with native inspect before assessment. Parent
    identity fields and all contributing source/decision rows examined; no full scientific
    certification of parent records is claimed.
- evidence_id: E2
  kind: database
  reference: data/raw/
  locator: Exact source rows and curation rows identified in assessments; data-row
    numbering excludes header/comments
  accessed_at: '2026-10-10T04:04:32Z'
  support: supports
  summary: All raw and root curation TSVs plus PATHS parsed. Full generated document
    matches the seeder; count, score, parent and status meanings evaluated separately
    from deterministic equality.
- evidence_id: E3
  kind: search
  reference: curation/causal_graphs/
  locator: rg --no-ignore --hidden over curation/causal_graphs, research/habitats
    and history; identifiers, labels, slugs
  accessed_at: '2026-10-10T04:04:32Z'
  support: supports
  summary: Ignored files included. No target causal overlay matched. Related material,
    subway and reptile research reports are leads only. Bounded find through configured
    kg-microbe/data to depth 3 and /private/tmp to depth 1 found no PREGO dumps; this
    is not a whole-filesystem absence claim.
  search_scope: rg --no-ignore --hidden over curation/causal_graphs, research/habitats
    and history; identifiers, labels, slugs; Ignored files included. No target causal
    overlay matched. Related material, subway and reptile research reports are leads
    only. Bounded find through configured kg-microbe/data to depth 3 and /private/tmp
    to depth 1 found no PREGO dumps; this is not a whole-filesystem absence claim.
- evidence_id: V1
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38021322406
  locator: Exact-base run metadata/log and fresh local gate receipts
  accessed_at: '2026-10-10T04:04:32Z'
  support: supports
  summary: 'Required schema, strict, corpus, label and native-review gates passed
    locally; baseline full QC passed in CI with three skipped tests. ID-label gate:
    1178 canonical, 1 synonym, 5 exceptions, 2057 without adapter. Deterministic success
    is not scientific approval.'
- evidence_id: T1
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=164393,153496,185294,903522,28038,880633,1553,438,1530,1701,1494,115778,765118,1254,442,1534,104102,33954,1615,1599,320497,231024,889932,322009,1580&retmode=xml
  locator: Every emitted taxon ID and scientific name
  accessed_at: '2026-10-10T04:04:32Z'
  support: supports
  summary: Fresh NCBI response confirms target taxon identifiers and labels; taxonomic
    validity does not establish ecological association.
- evidence_id: P2
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC8879827/
  locator: Methods 2.3-2.4 and Appendix C.1/C.3; PMID:35208748, DOI:10.3390/microorganisms10020293
  accessed_at: '2026-10-10T04:04:32Z'
  support: supports
  summary: PREGO derives associations from metadata/text or sample co-occurrence.
    Its channel-specific scores are not abundance or proof of a characteristic taxon.
- evidence_id: O1
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO:00000469
  locator: Active definition; ENVO:00000070 also inspected
  accessed_at: '2026-10-10T04:04:32Z'
  support: supports
  summary: Research facility and its broader construction class remain active and
    match the target meaning.
- evidence_id: P1
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/34861887/
  locator: Abstract; DOI:10.1186/s40168-021-01159-x
  accessed_at: '2026-10-10T04:04:32Z'
  support: supports
  summary: A primary spacecraft-assembly-facility study characterizes microbial samples
    using culture and molecular methods. It is a positive facility example, not exact
    PREGO source-member support.
assessments:
- assessment_id: A1
  area: identity
  topic: Identity and strict hierarchy
  outcome: supported
  summary: ENVO:00000469 denotes a facility for scientific research or measurement,
    including temporary facilities in different settings. ENVO:00000070 human construction
    is an appropriate broader class. Research facilities is a PREGO related synonym,
    not a separately merged source concept. A laboratory facility can be narrower;
    its GOLD triad usage does not redefine this PREGO identity.
  target_ids:
  - ENVO:00000469
  evidence_ids:
  - E1
  - E2
  - E3
  - V1
  - T1
  - P2
  - O1
  - P1
- assessment_id: A2
  area: evidence
  topic: Microbial support and source scope
  outcome: supported
  summary: PMID:34861887 reports microbial sampling of a spacecraft assembly facility,
    including culture and sequence-based methods. It provides an example of facility-associated
    microbiota, not confirmation of all emitted PREGO taxa or universal viability.
    NCBI resolves all 25 emitted identifiers/names, including four strain-rank entries.
    Ecological expectations about food-associated species are not sufficient to reject
    these source associations.
  target_ids:
  - ENVO:00000469
  evidence_ids:
  - E1
  - E2
  - E3
  - V1
  - T1
  - P2
  - O1
  - P1
- assessment_id: A3
  area: provenance
  topic: Source units, scores, extent and status
  outcome: unknown
  summary: PREGO data row 114 reports 339 TAXON associations and maximum score 1.75033
    from environmental_samples. The 25 emitted records retain ranks 1-25, pool 339
    and scores 1.75033 down to 1.36219, without is_characteristic flags. PREGO describes
    metadata-based co-occurrence with channel-specific scoring, not prevalence or
    abundance. Missing original sample links limit ecological verification, not reproducibility
    of the maintained inventory.
  target_ids:
  - ENVO:00000469
  evidence_ids:
  - E1
  - E2
  - E3
  - V1
  - T1
  - P2
  - O1
  - P1
- assessment_id: A4
  area: completeness
  topic: Claim placement and optional enrichment
  outcome: supported
  summary: No target causal graph, environmental parameter, discussion or dataset
    claim is emitted. Optional absent fields, CLASS decisions and SEEDED state alone
    are not defects. One source contributes and zero are ITEM-reviewed; no scientific
    status is promoted. Parent taxa, parameters and graphs are not inherited as target
    claims.
  target_ids:
  - ENVO:00000469
  evidence_ids:
  - E1
  - E2
  - E3
- assessment_id: A5
  area: schema
  topic: Validation versus scientific certification
  outcome: supported
  summary: Fresh native target/schema, corpus, label and review checks pass. Exact
    unchanged baseline passed full CI QC. The assessment retains source limitations;
    validator success does not settle identity or provenance questions.
  target_ids:
  - ENVO:00000469
  evidence_ids:
  - V1
findings: []
actions: []
limitations:
- PREGO backing sample links are unavailable because HTTPS certificate validation
  failed. No independent validation of all 339 source associations is claimed.
- Original frozen source membership is not reconstructed. Later workbook evidence
  is dated and reused; full QC is inspected exact-base CI evidence, with three tests
  skipped.
- This observation writes only its immutable review pair. It does not change generated
  scientific records, curation status or products, and makes no SSSOM/KGX readiness
  claim.
notes:
- Access timestamps denote completed inspection of source text or reused cached evidence,
  not publication or download dates. Native inspect preceded assessment; all 53 captured
  hashes remained unchanged.
tags:
- habitatmech
- engineered
- scientific-record-review
```
