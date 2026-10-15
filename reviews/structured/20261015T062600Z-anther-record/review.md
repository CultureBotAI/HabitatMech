# Record review: anther (BTO:0000079)

- Review: 20261015T062600Z-anther-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T06:06:36Z
- Finished UTC: 2026-10-15T06:26:00Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The BTO pollen-bearing organ identity and PREGO observational associations are coherent. The two taxa and score 3.0 are source association metadata, not evidence of prevalence or characteristic presence.

## Scope And Provenance

Individual scientific assessment of the exact generated target at the captured main revision.

Selection: Resolved identifier and source path in the next sixteen unreviewed records in corpus path order; this document assesses only its single target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base d255ab29c86291d2166fcf22219c10a9edb136c9.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0000079 | data/habitats/host_associated/anther.yaml | generated | anther |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0000079 | Actual exit 0 at 2026-10-15T06:06:38Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/anther.yaml |
| validate-strict | passed | True | BTO:0000079 | Actual exit 0 at 2026-10-15T06:07:14Z. uv run python scripts/validate_strict.py data/habitats/host_associated/anterior_nares.yaml data/habitats/host_associated/anterior_nares__14fc5dcc.yaml data/habitats/host_associated/anther.yaml data/habitats/host_associated/anthosphere.yaml data/habitats/host_associated/antler.yaml data/habitats/host_associated/aortic_valve.yaml data/habitats/host_associated/apocrine_sweat_gland.yaml data/habitats/host_associated/apoeccrine_sweat_glands.yaml data/habitats/host_associated/appendix.yaml data/habitats/host_associated/appendix__8f7f5041.yaml data/habitats/host_associated/appendix_abscess.yaml data/habitats/host_associated/appressorium.yaml data/habitats/host_associated/aquatic_mammal.yaml data/habitats/host_associated/aquatic_plant.yaml data/habitats/host_associated/aqueous_humor_of_eyeball.yaml data/habitats/host_associated/area_of_moss_dominated_vegetation.yaml<br>Validating 16 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      16<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | BTO:0000079 | Actual exit 0 at 2026-10-15T06:07:22Z. No issues found<br>746 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | BTO:0000079 | Actual exit 0 at 2026-10-15T06:07:23Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | BTO:0000079 | Actual exit 0 at 2026-10-15T06:07:39Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | BTO:0000079 | Actual exit 0 at 2026-10-15T06:07:43Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | BTO:0000079 | Actual exit 0 at 2026-10-15T06:08:00Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | BTO:0000079 | Actual exit 0 at 2026-10-15T06:08:42Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |

## Scientific And Domain Assessments

### Native structural and reproduction checks

schema: supported. Targets: BTO:0000079.

Recorded gates passed: schema, strict sixteen-target validation, 746 history records, exact 3,208-record reproduction, 32 causal graphs and 110 term requests. These are not scientific proof.

### Habitat identity and full source scope

identity: supported. Targets: BTO:0000079.

The BTO pollen-bearing organ identity and PREGO observational associations are coherent. The two taxa and score 3.0 are source association metadata, not evidence of prevalence or characteristic presence.

### Source counts, units and retained taxon observations

quantity: supported. Targets: BTO:0000079.

Exact contributing source rows, emitted counts/units, taxon labels/ranks and source scores were compared. [{"source": "PREGO", "count": 2, "unit": "TAXON"}]. 2 retained taxon IDs match current NCBI names. Zero counts are omitted, and later bulk biosamples/studies are not added to frozen ORGANISM counts. Source pools are not prevalence denominators.

### Parameters, causal claims and optional evidence

completeness: not_applicable. Targets: BTO:0000079.

No target causal graph, environmental-parameter, mechanism or characteristic-presence assertion requires expansion. No absent optional field is populated for coverage. Parent-record mechanisms are not inherited as evidence for this target.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/anther.yaml; Entire YAML | supports | All target fields and generated history were read. |
| ERULE | docs/CURATION.md; Hosts, anatomy, strict broader hierarchy and input ownership | supports | Anatomy may identify a microbial site; host taxa are not environment identities; every parent must be strictly broader. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate and taxon fields | supports | Mapping endpoint is the emitted record; association metrics and characteristic flags are separate. |
| ESEED | src/habitatmech/seed.py; resolve_gold, resolve_bacdive, ingest_prego, apply_decision and apply_curated_definitions | supports | All contributing native resolution routes executed with complete claimant and mapping pools; final identifier/status/predicate agree: [{"automatic": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "BTO:0000079", "mapping_predicate": null, "reviewed": false, "route": "prego_self_grounded"}, "final": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "BTO:0000079", "mapping_predicate": null, "reviewed": false, "route": "prego_self_grounded"}, "mint": "habitatmech:PREGO.6e4ee2b9dd", "source": "PREGO"}] |
| ET4 | data/raw/prego_habitat_taxa.tsv; TSV rows 37,38 | supports | [{"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0000079", "prego_score": "3", "rank": "1", "taxon_id": "NCBITaxon:1423", "taxon_label": "Bacillus subtilis"}, "row": 37}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0000079", "prego_score": "3", "rank": "2", "taxon_id": "NCBITaxon:269621", "taxon_label": "Microbotryum intermedium"}, "row": 38}] |
| ET5 | data/raw/prego_habitats.tsv; TSV rows 468 | supports | [{"data": {"biolink_category": "biolink:GrossAnatomicalStructure", "channels": "annotated_genomes_isolates", "direct_assertion_count": "2", "max_prego_score": "3", "ontology": "BTO", "prego_id": "BTO:0000079", "prego_synonyms": "anther&#124;anthers", "taxon_count": "2"}, "row": 468}] |
| ET6 | data/raw/ontology_terms.tsv; TSV rows 81 | supports | [{"data": {"definition": "The male reproductive organ enclosing and containing the pollen grains.", "deprecated": "", "directly_referenced": "TRUE", "label": "anther", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0000079"}, "row": 81}] |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000079; Target term or typed outgoing relations; primary abstract; exact strain identity and isolation-source fields as described | supports | Active authoritative BTO:0000079 anther; definition and typed scope compared with the frozen source and local parent meaning. Obsolete=False. |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000079/graph; Target term or typed outgoing relations; primary abstract; exact strain identity and isolation-source fields as described | supports | Inspected typed outgoing relations: [{"label": "part of", "source": "http://purl.obolibrary.org/obo/BTO_0000079", "target": "http://purl.obolibrary.org/obo/BTO_0001559", "uri": "http://purl.obolibrary.org/obo/BFO_0000050"}]. Partonomy and connectivity remain distinct from subclassing. |
| EX3 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1006155,1042321,1044,1071679,108028,109472,1114878,1121336,1121355,1121467,1122146,1122599,1123255,1130046,1176176,1176177,119224,1206817,1210932,1216006,1235440,1260928,1278303,1278307,1278309,1278310,1278312,1302685,1302687,1302689,1302690,1307457,131112,1324766,1336234,1346,137733,138563,1387353,1411316,1423,1436133,1460882,1490222,156892,1577474,157842,1612308,1619308,1619309,1619310,1799789,1834927,1843580,1843581,184914,1862160,1869227,1871086,1872412,1872627,1872635,1873466,1965234,2108,269621,269666,33,34,395087,409,420952,420953,53344,53364,83456&amp;retmode=xml; Target term or typed outgoing relations; primary abstract; exact strain identity and isolation-source fields as described | supports | All 2 retained taxon IDs resolve directly with matching preferred names: [{"direct_name_match": true, "id": "NCBITaxon:1423", "label": "Bacillus subtilis", "rank": "species"}, {"direct_name_match": true, "id": "NCBITaxon:269621", "label": "Microbotryum intermedium", "rank": "species"}] |
| ESEARCH | Local scientific-input and saved-review traversal; rg --no-ignore --hidden -l -F -e BTO:0000079 -e anther -e anther -e habitatmech:PREGO.6e4ee2b9dd curation history research reports data/raw build reviews | context_only | Ignored-inclusive source ID/label/slug search plus exact parsed table matches and complete structured-target traversal. No structured predecessor targets this record. |

## Limits And Additional Notes

- Frozen source-bin membership is not a complete audit of original specimens. Only the exact external source witnesses described here were independently inspected.
- Taxon associations are observational. PREGO score and BacDive strain counts do not prove prevalence, mechanism or characteristic presence.
- The configured label gate skipped 2,061 no-adapter pairs. Ontology semantics and retained taxon identities were separately assessed.
- The full archive and just qc are publication gates to run after saving; these pre-fix observations do not claim their future results.
- Historical reports and history prose are search leads, not independent approval. Historical neighboring claims and every legacy citation were not re-reviewed.
- iModulonDB is not applicable: these targets assert no gene, regulator or transcriptomic mechanism. No paid research was used.
- All captured local input bytes were rechecked unchanged against the working tree and exact Git blobs.
- Ignored-inclusive structured archive traversal found no earlier structured review targeting this record. Historical reports and GitHub issues are retained as contextual leads.
- This is a pre-fix observation; separately authorized curation requires new successor observations.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T062600Z-anther-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: anther (BTO:0000079)'
started_at: '2026-10-15T06:06:36Z'
finished_at: '2026-10-15T06:26:00Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent assessed full records and primary evidence. This
    is not independent human or second-agent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The BTO pollen-bearing organ identity and PREGO observational associations
  are coherent. The two taxa and score 3.0 are source association metadata, not evidence
  of prevalence or characteristic presence.
source:
  git_revision: d255ab29c86291d2166fcf22219c10a9edb136c9
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
  - path: conf/sources.yaml
    sha256: a8e069f9278068b57fa234f43e03c8d893f857827b83fd10cfa92d6815aed642
    role: context
  - path: curation/decisions.tsv
    sha256: ca42d86b6040df1c0c6e6ed36573bb51975a5e8daade262113bce547f1b6fd8b
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: a3e2880134344406dd3239ee041076df64c76407d311b71a16f2382c4146a177
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 761c1c1c60358c6c24e4d797637a12bdde6f8541e568914b404bffd1e0dd57ec
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: ea37676f1a16dd05fbfbb6c394b3f14b42ea93b763fb257043b817a4f10d3612
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: 2144d43ab4e106ff820da87c348f673d16cb8ea30d5a565f12e156af598f85ad
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: b0135af0aa4deed0f3824a2f491d5a742c1b7de4775c533f283761d22e805821
    role: context
  - path: data/habitats/RETIRED.tsv
    sha256: a2a0496837ea75e487d7fc5d35317a890262a941d8fffe9babcd39f2f332c6db
    role: context
  - path: data/habitats/host_associated/anther.yaml
    sha256: ed3ba78b8ea1952d82f0b4e1bcde48d0deda1a7a51f65a451666a999fcced11b
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
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20261002T123249Z-anther.md
    sha256: eff055e62db1189a6d7f1720b136606365e919e2e5b0dfb9649eb59983c6d1a7
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/habitatmech/curate/__init__.py
    sha256: d9837c29dc61d8c9245fdb471a68a109cea31b131cdbc0c4d51d23a8d013ce12
    role: context
  - path: src/habitatmech/curate/causal_graphs.py
    sha256: d1884374263ed7926292c52a58742c614e75628d78ff50fe688e6abc0ddf9c1c
    role: context
  - path: src/habitatmech/curate/curation_event.py
    sha256: 08c774d309fe988c468097518d346f07a653b283cb9b9b51c7fe79fa0af785a9
    role: context
  - path: src/habitatmech/curate/decisions.py
    sha256: f33d3e9dc95bb428e63e640d48d4074cf15e90ea666603fb16fb651d591e3f02
    role: context
  - path: src/habitatmech/curate/definition_source_label_exclusions.py
    sha256: 0c13e83fe17613e8b9f5b346d1259104172f8c1de42f911625579b903707625d
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
  - path: src/habitatmech/labels.py
    sha256: eb6986c3a9c7d5a3e4651b639351f1f2d3e12d74c4bfaa92899205a1f9df0977
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
    role: context
  - path: src/habitatmech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/habitatmech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/habitatmech/seed.py
    sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
    role: context
targets:
- target_id: BTO:0000079
  path: data/habitats/host_associated/anther.yaml
  label: anther
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
scope:
  description: Individual scientific assessment of the exact generated target at the
    captured main revision.
  selection: Resolved identifier and source path in the next sixteen unreviewed records
    in corpus path order; this document assesses only its single target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - BTO:0000079
  exclusions:
  - target: Other habitats and SSSOM/KGX products
    reason: Direct parents are contextual dependencies, not additional completed reviews;
      no export compatibility certification.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/anther.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000079
  summary: "Actual exit 0 at 2026-10-15T06:06:38Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/anther.yaml"
  scope_note: Individual schema; strict command covers sixteen targets; other named
    native gates have whole-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/anterior_nares.yaml data/habitats/host_associated/anterior_nares__14fc5dcc.yaml
    data/habitats/host_associated/anther.yaml data/habitats/host_associated/anthosphere.yaml
    data/habitats/host_associated/antler.yaml data/habitats/host_associated/aortic_valve.yaml
    data/habitats/host_associated/apocrine_sweat_gland.yaml data/habitats/host_associated/apoeccrine_sweat_glands.yaml
    data/habitats/host_associated/appendix.yaml data/habitats/host_associated/appendix__8f7f5041.yaml
    data/habitats/host_associated/appendix_abscess.yaml data/habitats/host_associated/appressorium.yaml
    data/habitats/host_associated/aquatic_mammal.yaml data/habitats/host_associated/aquatic_plant.yaml
    data/habitats/host_associated/aqueous_humor_of_eyeball.yaml data/habitats/host_associated/area_of_moss_dominated_vegetation.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000079
  summary: "Actual exit 0 at 2026-10-15T06:07:14Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/anterior_nares.yaml data/habitats/host_associated/anterior_nares__14fc5dcc.yaml\
    \ data/habitats/host_associated/anther.yaml data/habitats/host_associated/anthosphere.yaml\
    \ data/habitats/host_associated/antler.yaml data/habitats/host_associated/aortic_valve.yaml\
    \ data/habitats/host_associated/apocrine_sweat_gland.yaml data/habitats/host_associated/apoeccrine_sweat_glands.yaml\
    \ data/habitats/host_associated/appendix.yaml data/habitats/host_associated/appendix__8f7f5041.yaml\
    \ data/habitats/host_associated/appendix_abscess.yaml data/habitats/host_associated/appressorium.yaml\
    \ data/habitats/host_associated/aquatic_mammal.yaml data/habitats/host_associated/aquatic_plant.yaml\
    \ data/habitats/host_associated/aqueous_humor_of_eyeball.yaml data/habitats/host_associated/area_of_moss_dominated_vegetation.yaml\n\
    Validating 16 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      16\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Individual schema; strict command covers sixteen targets; other named
    native gates have whole-corpus scope.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000079
  summary: 'Actual exit 0 at 2026-10-15T06:07:22Z. No issues found

    746 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Individual schema; strict command covers sixteen targets; other named
    native gates have whole-corpus scope.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000079
  summary: "Actual exit 0 at 2026-10-15T06:07:23Z. provenance current: 14 committed\
    \ inventories, 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Individual schema; strict command covers sixteen targets; other named
    native gates have whole-corpus scope.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000079
  summary: "Actual exit 0 at 2026-10-15T06:07:39Z. expected 3208 records, found 3208\
    \ on disk\n  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces\
    \ exactly from data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Individual schema; strict command covers sixteen targets; other named
    native gates have whole-corpus scope.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000079
  summary: "Actual exit 0 at 2026-10-15T06:07:43Z. validated 32 causal-graph curation\
    \ file(s) with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Individual schema; strict command covers sixteen targets; other named
    native gates have whole-corpus scope.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000079
  summary: "Actual exit 0 at 2026-10-15T06:08:00Z. term-request table is current (110\
    \ terms)\n uv run python scripts/build_term_requests.py --check"
  scope_note: Individual schema; strict command covers sixteen targets; other named
    native gates have whole-corpus scope.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000079
  summary: "Actual exit 0 at 2026-10-15T06:08:42Z. id↔label correspondence summary:\n\
    \          OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Individual schema; strict command covers sixteen targets; other named
    native gates have whole-corpus scope.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/anther.yaml
  locator: Entire YAML
  accessed_at: '2026-10-15T06:26:00Z'
  support: supports
  summary: All target fields and generated history were read.
  snapshot_sha256: ed3ba78b8ea1952d82f0b4e1bcde48d0deda1a7a51f65a451666a999fcced11b
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Hosts, anatomy, strict broader hierarchy and input ownership
  accessed_at: '2026-10-15T06:26:00Z'
  support: supports
  summary: Anatomy may identify a microbial site; host taxa are not environment identities;
    every parent must be strictly broader.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate and taxon fields
  accessed_at: '2026-10-15T06:26:00Z'
  support: supports
  summary: Mapping endpoint is the emitted record; association metrics and characteristic
    flags are separate.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: resolve_gold, resolve_bacdive, ingest_prego, apply_decision and apply_curated_definitions
  accessed_at: '2026-10-15T06:26:00Z'
  support: supports
  summary: 'All contributing native resolution routes executed with complete claimant
    and mapping pools; final identifier/status/predicate agree: [{"automatic": {"category":
    null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs":
    [], "grounding_status": "EXACT", "identifier": "BTO:0000079", "mapping_predicate":
    null, "reviewed": false, "route": "prego_self_grounded"}, "final": {"category":
    null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs":
    [], "grounding_status": "EXACT", "identifier": "BTO:0000079", "mapping_predicate":
    null, "reviewed": false, "route": "prego_self_grounded"}, "mint": "habitatmech:PREGO.6e4ee2b9dd",
    "source": "PREGO"}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: ET4
  kind: database
  reference: data/raw/prego_habitat_taxa.tsv
  locator: TSV rows 37,38
  accessed_at: '2026-10-15T06:26:00Z'
  support: supports
  summary: '[{"data": {"channels": "annotated_genomes_isolates", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "BTO:0000079", "prego_score": "3", "rank":
    "1", "taxon_id": "NCBITaxon:1423", "taxon_label": "Bacillus subtilis"}, "row":
    37}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "",
    "direct_flag": "TRUE", "prego_id": "BTO:0000079", "prego_score": "3", "rank":
    "2", "taxon_id": "NCBITaxon:269621", "taxon_label": "Microbotryum intermedium"},
    "row": 38}]'
  snapshot_sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
- evidence_id: ET5
  kind: database
  reference: data/raw/prego_habitats.tsv
  locator: TSV rows 468
  accessed_at: '2026-10-15T06:26:00Z'
  support: supports
  summary: '[{"data": {"biolink_category": "biolink:GrossAnatomicalStructure", "channels":
    "annotated_genomes_isolates", "direct_assertion_count": "2", "max_prego_score":
    "3", "ontology": "BTO", "prego_id": "BTO:0000079", "prego_synonyms": "anther|anthers",
    "taxon_count": "2"}, "row": 468}]'
  snapshot_sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
- evidence_id: ET6
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 81
  accessed_at: '2026-10-15T06:26:00Z'
  support: supports
  summary: '[{"data": {"definition": "The male reproductive organ enclosing and containing
    the pollen grains.", "deprecated": "", "directly_referenced": "TRUE", "label":
    "anther", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id":
    "BTO:0000079"}, "row": 81}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EX1
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000079
  locator: Target term or typed outgoing relations; primary abstract; exact strain
    identity and isolation-source fields as described
  accessed_at: '2026-10-15T06:17:49Z'
  support: supports
  summary: Active authoritative BTO:0000079 anther; definition and typed scope compared
    with the frozen source and local parent meaning. Obsolete=False.
  snapshot_sha256: 084aec3ab54460cc3f3daae7fed388b0fce7eba3278c58ddd6f7c753e0517b63
- evidence_id: EX2
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000079/graph
  locator: Target term or typed outgoing relations; primary abstract; exact strain
    identity and isolation-source fields as described
  accessed_at: '2026-10-15T06:17:50Z'
  support: supports
  summary: 'Inspected typed outgoing relations: [{"label": "part of", "source": "http://purl.obolibrary.org/obo/BTO_0000079",
    "target": "http://purl.obolibrary.org/obo/BTO_0001559", "uri": "http://purl.obolibrary.org/obo/BFO_0000050"}].
    Partonomy and connectivity remain distinct from subclassing.'
  snapshot_sha256: 186e644a347b974565cadc9790aee27012a7af739915af95528efa890dabe7c6
- evidence_id: EX3
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1006155,1042321,1044,1071679,108028,109472,1114878,1121336,1121355,1121467,1122146,1122599,1123255,1130046,1176176,1176177,119224,1206817,1210932,1216006,1235440,1260928,1278303,1278307,1278309,1278310,1278312,1302685,1302687,1302689,1302690,1307457,131112,1324766,1336234,1346,137733,138563,1387353,1411316,1423,1436133,1460882,1490222,156892,1577474,157842,1612308,1619308,1619309,1619310,1799789,1834927,1843580,1843581,184914,1862160,1869227,1871086,1872412,1872627,1872635,1873466,1965234,2108,269621,269666,33,34,395087,409,420952,420953,53344,53364,83456&retmode=xml
  locator: Target term or typed outgoing relations; primary abstract; exact strain
    identity and isolation-source fields as described
  accessed_at: '2026-10-15T06:19:30Z'
  support: supports
  summary: 'All 2 retained taxon IDs resolve directly with matching preferred names:
    [{"direct_name_match": true, "id": "NCBITaxon:1423", "label": "Bacillus subtilis",
    "rank": "species"}, {"direct_name_match": true, "id": "NCBITaxon:269621", "label":
    "Microbotryum intermedium", "rank": "species"}]'
  snapshot_sha256: 74da4de2673092fd0e7d34e23be448eb9bd1ff410a532286c0fbfd597d0fc88e
- evidence_id: ESEARCH
  kind: search
  reference: Local scientific-input and saved-review traversal
  locator: rg --no-ignore --hidden -l -F -e BTO:0000079 -e anther -e anther -e habitatmech:PREGO.6e4ee2b9dd
    curation history research reports data/raw build reviews
  accessed_at: '2026-10-15T06:17:29Z'
  support: context_only
  summary: Ignored-inclusive source ID/label/slug search plus exact parsed table matches
    and complete structured-target traversal. No structured predecessor targets this
    record.
  search_scope: Hidden and ignored files included under curation, history, research,
    reports, data/raw, build and reviews; all structured review.yaml files traversed
    irrespective of gitignore. Not a global absence or original-member claim.
assessments:
- assessment_id: A1
  area: schema
  topic: Native structural and reproduction checks
  outcome: supported
  summary: 'Recorded gates passed: schema, strict sixteen-target validation, 746 history
    records, exact 3,208-record reproduction, 32 causal graphs and 110 term requests.
    These are not scientific proof.'
  target_ids:
  - BTO:0000079
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Habitat identity and full source scope
  outcome: supported
  summary: The BTO pollen-bearing organ identity and PREGO observational associations
    are coherent. The two taxa and score 3.0 are source association metadata, not
    evidence of prevalence or characteristic presence.
  target_ids:
  - BTO:0000079
  evidence_ids:
  - E1
  - ERULE
  - ESEED
  - EX1
  - EX2
  - EX3
- assessment_id: A3
  area: quantity
  topic: Source counts, units and retained taxon observations
  outcome: supported
  summary: 'Exact contributing source rows, emitted counts/units, taxon labels/ranks
    and source scores were compared. [{"source": "PREGO", "count": 2, "unit": "TAXON"}].
    2 retained taxon IDs match current NCBI names. Zero counts are omitted, and later
    bulk biosamples/studies are not added to frozen ORGANISM counts. Source pools
    are not prevalence denominators.'
  target_ids:
  - BTO:0000079
  evidence_ids:
  - E1
  - ESEED
  - ESEARCH
  - EX1
  - EX2
  - EX3
- assessment_id: A4
  area: completeness
  topic: Parameters, causal claims and optional evidence
  outcome: not_applicable
  summary: No target causal graph, environmental-parameter, mechanism or characteristic-presence
    assertion requires expansion. No absent optional field is populated for coverage.
    Parent-record mechanisms are not inherited as evidence for this target.
  target_ids:
  - BTO:0000079
  evidence_ids:
  - E1
findings: []
actions: []
limitations:
- Frozen source-bin membership is not a complete audit of original specimens. Only
  the exact external source witnesses described here were independently inspected.
- Taxon associations are observational. PREGO score and BacDive strain counts do not
  prove prevalence, mechanism or characteristic presence.
- The configured label gate skipped 2,061 no-adapter pairs. Ontology semantics and
  retained taxon identities were separately assessed.
- The full archive and just qc are publication gates to run after saving; these pre-fix
  observations do not claim their future results.
- Historical reports and history prose are search leads, not independent approval.
  Historical neighboring claims and every legacy citation were not re-reviewed.
- 'iModulonDB is not applicable: these targets assert no gene, regulator or transcriptomic
  mechanism. No paid research was used.'
notes:
- All captured local input bytes were rechecked unchanged against the working tree
  and exact Git blobs.
- Ignored-inclusive structured archive traversal found no earlier structured review
  targeting this record. Historical reports and GitHub issues are retained as contextual
  leads.
- This is a pre-fix observation; separately authorized curation requires new successor
  observations.
tags:
- individual-scientific-review
- host-associated
```
