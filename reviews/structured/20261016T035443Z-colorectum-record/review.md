# Record review: colorectum (BTO:0001613)

- Review: 20261016T035443Z-colorectum-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-16T03:35:55Z
- Finished UTC: 2026-10-16T03:54:43Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

BTO:0001613 denotes colon and rectum considered together. Its sole PREGO taxon, F. nucleatum CC53, has positive exact-strain context: the primary colorectal-carcinoma study explicitly identifies CC53 as its tumor isolate and assays it in culture. This supports colorectal tissue association, not universal healthy-colorectum residence, prevalence, or a causal cancer claim. Preserve the one TAXON count, score three, source identity and current name.

## Scope And Provenance

Full field-by-field assessment of this one resolved generated record.

Selection: One of the next 24 unreviewed records selected in deterministic path order from the ignored-inclusive 3209-record census. This bundle assesses exactly one target, not a proxy sample.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 67cde35918d7361de3a1164fb22756cba5d20e30.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0001613 | data/habitats/host_associated/colorectum.yaml | generated | colorectum |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0001613 | Finished 2026-10-16T03:36:24Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/colorectum.yaml |
| validate-strict | passed | True | BTO:0001613 | Finished 2026-10-16T03:36:32Z. uv run python scripts/validate_strict.py data/habitats/host_associated/clasper.yaml data/habitats/host_associated/claw.yaml data/habitats/host_associated/cloaca.yaml data/habitats/host_associated/cloaca__f527d4ff.yaml data/habitats/host_associated/cnidarian_associated_environment.yaml data/habitats/host_associated/cob.yaml data/habitats/host_associated/cocoon.yaml data/habitats/host_associated/coelom.yaml data/habitats/host_associated/coelom__d65ea80b.yaml data/habitats/host_associated/colon.yaml data/habitats/host_associated/colon__a0dd5461.yaml data/habitats/host_associated/colon__ff534087.yaml data/habitats/host_associated/colon_cancer.yaml data/habitats/host_associated/colon_mucosa.yaml data/habitats/host_associated/colon_mucosa__7a8e4588.yaml data/habitats/host_associated/colon_mucosa__b687aead.yaml data/habitats/host_associated/colon_mucosa__de31f03f.yaml data/habitats/host_associated/colonic.yaml data/habitats/host_associated/colonic_cancer_cell.yaml data/habitats/host_associated/colonic_epithelium.yaml data/habitats/host_associated/colonic_mucosa.yaml data/habitats/host_associated/colorectal_polyps.yaml data/habitats/host_associated/colorectum.yaml data/habitats/host_associated/colostrum.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | BTO:0001613 | Finished 2026-10-16T03:36:40Z. No issues found<br>831 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | BTO:0001613 | Finished 2026-10-16T03:36:40Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | BTO:0001613 | Finished 2026-10-16T03:37:54Z. expected 3209 records, found 3209 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | BTO:0001613 | Finished 2026-10-16T03:38:04Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | BTO:0001613 | Finished 2026-10-16T03:38:23Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | BTO:0001613 | Finished 2026-10-16T03:39:05Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1173<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2063<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-base hosted native QC | passed | True | BTO:0001613 | Verified 2026-10-16T03:43:47Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38843593114 |
| Displayed candidate-pool correspondence | passed | False | BTO:0001613 | Finished 2026-10-16T03:54:30Z. All 60 displayed candidate pools equal exact source taxon totals. |
| Standalone citation validation applicability | not_applicable | False | BTO:0001613 | No standalone citation checker is documented for these evidence-free generated targets. Stable references were checked with native gates and current authorities; causal validation ran globally. |

## Scientific And Domain Assessments

### Identity, grounding, aliases and strictly broader hierarchy

identity: supported. Targets: BTO:0001613.

BTO:0001613 denotes colon and rectum considered together. Its sole PREGO taxon, F. nucleatum CC53, has positive exact-strain context: the primary colorectal-carcinoma study explicitly identifies CC53 as its tumor isolate and assays it in culture. This supports colorectal tissue association, not universal healthy-colorectum residence, prevalence, or a causal cancer claim. Preserve the one TAXON count, score three, source identity and current name.

### Native source units, ranks, scores and candidate pools

quantity: supported. Targets: BTO:0001613.

Exact source rows reproduce every emitted count/unit and displayed taxon rank/score/pool. Zero tree counts are omitted; supplemental biosamples, study memberships and triads are nonadditive. {"assertions": [{"source": "PREGO", "count": 1, "unit": "TAXON", "row": {"row": 605, "data": {"prego_id": "BTO:0001613", "ontology": "BTO", "biolink_category": "biolink:GrossAnatomicalStructure", "taxon_count": "1", "direct_assertion_count": "1", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms": "colorecta&#124;colorectal&#124;colorectum&#124;colorectums"}}}], "taxa": [{"id": "NCBITaxon:1297579", "source": "PREGO", "label": "Fusobacterium nucleatum CC53", "current_id": "1297579", "current_name": "Fusobacterium nucleatum CC53", "rank": "strain", "direct_match": true, "recognized_alias": true, "other_names": [], "source_row": {"row": 2405, "data": {"prego_id": "BTO:0001613", "rank": "1", "taxon_id": "NCBITaxon:1297579", "taxon_label": "Fusobacterium nucleatum CC53", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}}]}

### Association evidence and claim scope

evidence: supported. Targets: BTO:0001613.

Current ontology/TaxId identities and source attestations were verified. BTO:0001613 denotes colon and rectum considered together. Its sole PREGO taxon, F. nucleatum CC53, has positive exact-strain context: the primary colorectal-carcinoma study explicitly identifies CC53 as its tumor isolate and assays it in culture. This supports colorectal tissue association, not universal healthy-colorectum residence, prevalence, or a causal cancer claim. Preserve the one TAXON count, score three, source identity and current name. Individual papers support only the stated scope; original source pairs were not exhaustively reconstructed.

### Native lifecycle, optional content and mechanism limits

completeness: supported. Targets: BTO:0001613.

Executed native routes reproduce EXACT/SEEDED. Required content is present. No optional environmental parameters, causal graph, discussion, dataset or characteristic-presence claim is fabricated. Missing ITEM status alone is not a defect; no status or history promotion is performed.

### Native validation and reproducibility

schema: supported. Targets: BTO:0001613.

31 baseline commands passed: target schema, cohort strict, 831 histories, source provenance, exact 3209-record reproduction, 32 causal overlays, 110 term requests and configured labels. Exact-base hosted QC passed. Deterministic validity is not scientific approval.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/colorectum.yaml; Entire generated target YAML | supports | All fields, source attestations, displayed taxa, aliases and complete generated history read. |
| ERULE | docs/CURATION.md; Identity, evidence and strictly broader parents | supports | All parent contributions must be strictly broader; source context, anatomy, host and diagnosis are distinct. Optional absence is not a required-field defect. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation and GroundingStatusEnum | supports | The mapping contract compares source concept to record identifier; source-is-record omits the predicate. Native status and association rules are preserved. |
| ESEED | src/habitatmech/seed.py; Executed source routes and entire document reproduction | supports | [{"mint": "habitatmech:PREGO.cbfe86fae7", "automatic": {"identifier": "BTO:0001613", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "BTO:0001613", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}}] |
| EEXTRACT | src/habitatmech/extract.py; Source counts, source-strain-taxon join and PREGO scoring/ranking | supports | Inspected native projections. Original BacDive source-strain join and PREGO pair citation evidence are not retained in the compact per-habitat taxon tables. |
| ET5 | data/raw/prego_habitat_taxa.tsv; Physical TSV rows 2405 | supports | [{"row": 2405, "data": {"prego_id": "BTO:0001613", "rank": "1", "taxon_id": "NCBITaxon:1297579", "taxon_label": "Fusobacterium nucleatum CC53", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}] |
| ET6 | data/raw/prego_habitats.tsv; Physical TSV rows 605 | supports | [{"row": 605, "data": {"prego_id": "BTO:0001613", "ontology": "BTO", "biolink_category": "biolink:GrossAnatomicalStructure", "taxon_count": "1", "direct_assertion_count": "1", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms": "colorecta&#124;colorectal&#124;colorectum&#124;colorectums"}}] |
| ET7 | data/raw/ontology_terms.tsv; Physical TSV rows 1613 | supports | [{"row": 1613, "data": {"term_id": "BTO:0001613", "ontology": "BTO", "label": "colorectum", "definition": "The colon and rectum considered as a unit.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}] |
| EX8 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001613/graph; BTO_0001613-graph.json | context_only | Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0001613", "target": "http://purl.obolibrary.org/obo/BTO_0000648", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX9 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001613; BTO_0001613.json | context_only | Current identity, active status, definition and typed synonyms: {"obo_id": "BTO:0001613", "label": "colorectum", "is_obsolete": false, "description": ["The colon and rectum considered as a unit."], "obo_synonym": null, "annotation": {"has_obo_namespace": ["BrendaTissueOBO"], "id": ["BTO:0001613"]}} |
| EX10 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3971631/fullTextXML; PMC3971631.xml | context_only | PMID:24450771; DOI:10.1186/2049-2618-1-16. Introduction and co-aggregation methods/results inspected: exact CC53 is described as a colorectal-tumor isolate from the authors' earlier study. Positive tissue association, not universal prevalence or cancer causation. |
| EX11 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML; PMC8879827.xml | context_only | PMID:35208748; DOI:10.3390/microorganisms10020293. Methods and scoring appendix inspected: channels have different evidence and scoring; score-three BioProject associations can derive from abstract mining. This does not identify the extraction route of any particular retained pair. |
| EX12 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=102234,1027273,1048357,1069963,1074311,1110509,1117,1120968,1120983,1121027,1150864,1173995,119852,1216969,1224163,1234143,1234144,1245026,1263,1280004,1292046,1297579,1342794,1342818,1348114,1385512,1401264,141693,1449351,1452538,1453497,1479025,1481923,1485,1578,1590,171549,171550,171552,186802,186803,189330,248039,31979,33038,33042,375288,384676,411459,411460,444103,51514,541000,560080,572511,816,830,838,85831,872&amp;retmode=xml; taxonomy.xml | context_only | Current exact TaxId resolutions, including merged IDs and labels: [{"id": "NCBITaxon:1297579", "source": "PREGO", "label": "Fusobacterium nucleatum CC53", "current_id": "1297579", "current_name": "Fusobacterium nucleatum CC53", "rank": "strain", "direct_match": true, "recognized_alias": true}] |
| ESEARCH | Local source/curation/review corpus; rg --no-ignore --hidden -l -F -e BTO:0001613 -e colorectum -e colorectum -e habitatmech:PREGO.cbfe86fae7 curation history research reports data/raw build reviews | context_only | Source rows were parsed by exact keys; broad name hits were leads, not all inspected. No formal structured target predecessor. |
| EAVAIL | Configured kg-microbe checkout; find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe -type f '(' -ipath '*prego*' -o -ipath '*bacdive*' ')' | context_only | Search found BacDive notebooks and Git metadata, but no manifest-matching BacDive/PREGO transformed node/edge exports. No claim of global absence. |

## Limits And Additional Notes

- Original specimen-level evidence and every pair-level citation were not exhaustively reconstructed. Source associations, counts, ranks and scores are not prevalence, viability or characteristic presence.
- Configured label validation skips 2063 no-adapter pairs; target TaxIds were separately resolved with current NCBI.
- Exact-base hosted QC covers unchanged scientific inputs, not a new local full-QC execution or these new review files. Each new bundle requires native validation/save and the subsequent archive check.
- iModulonDB is not applicable: no gene, regulator or expression-module claim is asserted. Cited experiments are used only for identity and context, not imported causal mechanisms.
- Original source-strain or PREGO pair exports were unavailable in the configured checkout; no uncertain association is removed or source count rewritten.
- Captured working_tree provenance is retained. All local input hashes were additionally checked against exact base 67cde35918d7361de3a1164fb22756cba5d20e30.
- Read-only review: no source, curation, generated record, status or history edit; no GitHub mutation or paid research.
- Ignored-inclusive structured archive traversal found no previous structured target review. Legacy prose is contextual evidence, not formal predecessor lineage or issue closure.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T035443Z-colorectum-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: colorectum (BTO:0001613)'
started_at: '2026-10-16T03:35:55Z'
finished_at: '2026-10-16T03:54:43Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent assessed all evidence and target; not independent
    reviewer approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'BTO:0001613 denotes colon and rectum considered together. Its sole PREGO
  taxon, F. nucleatum CC53, has positive exact-strain context: the primary colorectal-carcinoma
  study explicitly identifies CC53 as its tumor isolate and assays it in culture.
  This supports colorectal tissue association, not universal healthy-colorectum residence,
  prevalence, or a causal cancer claim. Preserve the one TAXON count, score three,
  source identity and current name.'
source:
  git_revision: 67cde35918d7361de3a1164fb22756cba5d20e30
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
    sha256: e5cb2e09f72dd4b18e069c0e2576e25e13e56c9991f4eb5ae47416345e247578
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 37dc4b40642d19e7b5c3262f368d12daa82e03115e7731a2326ae88785ceff5b
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 04ba048af6f93b69c127bc3d47e2403dbe153452c75f9e26939188fc5daa52d7
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: a56f07a45fb743fb7b0e61f83ef70fa5ed61a3c892cfaf36e3428967c548dc5e
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: bc7a13d922c179cd9bcd4d37b348bc90a39b08a4dafba7af4ed0039ad99621c3
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: ee559f7b45b4af2d72a078c45d1a3b676785d34305f286e9738f95771dbaccfd
    role: context
  - path: data/habitats/RETIRED.tsv
    sha256: 747e6a5612dc0b7ed881b9fb323fd57ab3c75794d9ee5ebb9d59b2be57dbf8cd
    role: context
  - path: data/habitats/host_associated/colorectum.yaml
    sha256: 3cfee37f15d47c5c81e1a54022698faa322ec4f921b5533578ea912bd6297276
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
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
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
- target_id: BTO:0001613
  path: data/habitats/host_associated/colorectum.yaml
  label: colorectum
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
  description: Full field-by-field assessment of this one resolved generated record.
  selection: One of the next 24 unreviewed records selected in deterministic path
    order from the ignored-inclusive 3209-record census. This bundle assesses exactly
    one target, not a proxy sample.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - BTO:0001613
  exclusions:
  - target: Other records, individual source specimens and SSSOM/KGX products
    reason: Parent context is not additional review coverage; original specimens and
      exports are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/colorectum.yaml
  exit_code: 0
  target_ids:
  - BTO:0001613
  summary: "Finished 2026-10-16T03:36:24Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/colorectum.yaml"
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/clasper.yaml data/habitats/host_associated/claw.yaml
    data/habitats/host_associated/cloaca.yaml data/habitats/host_associated/cloaca__f527d4ff.yaml
    data/habitats/host_associated/cnidarian_associated_environment.yaml data/habitats/host_associated/cob.yaml
    data/habitats/host_associated/cocoon.yaml data/habitats/host_associated/coelom.yaml
    data/habitats/host_associated/coelom__d65ea80b.yaml data/habitats/host_associated/colon.yaml
    data/habitats/host_associated/colon__a0dd5461.yaml data/habitats/host_associated/colon__ff534087.yaml
    data/habitats/host_associated/colon_cancer.yaml data/habitats/host_associated/colon_mucosa.yaml
    data/habitats/host_associated/colon_mucosa__7a8e4588.yaml data/habitats/host_associated/colon_mucosa__b687aead.yaml
    data/habitats/host_associated/colon_mucosa__de31f03f.yaml data/habitats/host_associated/colonic.yaml
    data/habitats/host_associated/colonic_cancer_cell.yaml data/habitats/host_associated/colonic_epithelium.yaml
    data/habitats/host_associated/colonic_mucosa.yaml data/habitats/host_associated/colorectal_polyps.yaml
    data/habitats/host_associated/colorectum.yaml data/habitats/host_associated/colostrum.yaml
  exit_code: 0
  target_ids:
  - BTO:0001613
  summary: "Finished 2026-10-16T03:36:32Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/clasper.yaml data/habitats/host_associated/claw.yaml\
    \ data/habitats/host_associated/cloaca.yaml data/habitats/host_associated/cloaca__f527d4ff.yaml\
    \ data/habitats/host_associated/cnidarian_associated_environment.yaml data/habitats/host_associated/cob.yaml\
    \ data/habitats/host_associated/cocoon.yaml data/habitats/host_associated/coelom.yaml\
    \ data/habitats/host_associated/coelom__d65ea80b.yaml data/habitats/host_associated/colon.yaml\
    \ data/habitats/host_associated/colon__a0dd5461.yaml data/habitats/host_associated/colon__ff534087.yaml\
    \ data/habitats/host_associated/colon_cancer.yaml data/habitats/host_associated/colon_mucosa.yaml\
    \ data/habitats/host_associated/colon_mucosa__7a8e4588.yaml data/habitats/host_associated/colon_mucosa__b687aead.yaml\
    \ data/habitats/host_associated/colon_mucosa__de31f03f.yaml data/habitats/host_associated/colonic.yaml\
    \ data/habitats/host_associated/colonic_cancer_cell.yaml data/habitats/host_associated/colonic_epithelium.yaml\
    \ data/habitats/host_associated/colonic_mucosa.yaml data/habitats/host_associated/colorectal_polyps.yaml\
    \ data/habitats/host_associated/colorectum.yaml data/habitats/host_associated/colostrum.yaml\n\
    Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      24\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - BTO:0001613
  summary: 'Finished 2026-10-16T03:36:40Z. No issues found

    831 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - BTO:0001613
  summary: "Finished 2026-10-16T03:36:40Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - BTO:0001613
  summary: "Finished 2026-10-16T03:37:54Z. expected 3209 records, found 3209 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - BTO:0001613
  summary: "Finished 2026-10-16T03:38:04Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - BTO:0001613
  summary: "Finished 2026-10-16T03:38:23Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - BTO:0001613
  summary: "Finished 2026-10-16T03:39:05Z. id↔label correspondence summary:\n    \
    \      OK_CANONICAL: 1173\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2063\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: CCI
  name: Exact-base hosted native QC
  status: passed
  required: true
  command: gh run view 38843593114 --repo CultureBotAI/HabitatMech --json headSha,conclusion,url,jobs
  exit_code: 0
  target_ids:
  - BTO:0001613
  summary: Verified 2026-10-16T03:43:47Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38843593114
  scope_note: Unchanged scientific-input base only. Not a claim that the new output
    bundles were part of the earlier run.
- check_id: CPOOL
  name: Displayed candidate-pool correspondence
  status: passed
  required: false
  command: .venv/bin/python /private/tmp/habitatmech-review-cq-author.py pool_check
  exit_code: 0
  target_ids:
  - BTO:0001613
  summary: Finished 2026-10-16T03:54:30Z. All 60 displayed candidate pools equal exact
    source taxon totals.
  scope_note: Supplemental mechanical cross-check of all 60 displayed taxon entries;
    not a replacement for native validators or scientific evidence.
- check_id: CREF
  name: Standalone citation validation applicability
  status: not_applicable
  required: false
  target_ids:
  - BTO:0001613
  summary: No standalone citation checker is documented for these evidence-free generated
    targets. Stable references were checked with native gates and current authorities;
    causal validation ran globally.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/colorectum.yaml
  locator: Entire generated target YAML
  accessed_at: '2026-10-16T03:54:43Z'
  support: supports
  summary: All fields, source attestations, displayed taxa, aliases and complete generated
    history read.
  snapshot_sha256: 3cfee37f15d47c5c81e1a54022698faa322ec4f921b5533578ea912bd6297276
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, evidence and strictly broader parents
  accessed_at: '2026-10-16T03:54:43Z'
  support: supports
  summary: All parent contributions must be strictly broader; source context, anatomy,
    host and diagnosis are distinct. Optional absence is not a required-field defect.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation and GroundingStatusEnum
  accessed_at: '2026-10-16T03:54:43Z'
  support: supports
  summary: The mapping contract compares source concept to record identifier; source-is-record
    omits the predicate. Native status and association rules are preserved.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed source routes and entire document reproduction
  accessed_at: '2026-10-16T03:54:43Z'
  support: supports
  summary: '[{"mint": "habitatmech:PREGO.cbfe86fae7", "automatic": {"identifier":
    "BTO:0001613", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded",
    "category": null, "reviewed": false, "decision": null}, "final": {"identifier":
    "BTO:0001613", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded",
    "category": null, "reviewed": false, "decision": null}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: Source counts, source-strain-taxon join and PREGO scoring/ranking
  accessed_at: '2026-10-16T03:54:43Z'
  support: supports
  summary: Inspected native projections. Original BacDive source-strain join and PREGO
    pair citation evidence are not retained in the compact per-habitat taxon tables.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/prego_habitat_taxa.tsv
  locator: Physical TSV rows 2405
  accessed_at: '2026-10-16T03:54:43Z'
  support: supports
  summary: '[{"row": 2405, "data": {"prego_id": "BTO:0001613", "rank": "1", "taxon_id":
    "NCBITaxon:1297579", "taxon_label": "Fusobacterium nucleatum CC53", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}]'
  snapshot_sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
- evidence_id: ET6
  kind: database
  reference: data/raw/prego_habitats.tsv
  locator: Physical TSV rows 605
  accessed_at: '2026-10-16T03:54:43Z'
  support: supports
  summary: '[{"row": 605, "data": {"prego_id": "BTO:0001613", "ontology": "BTO", "biolink_category":
    "biolink:GrossAnatomicalStructure", "taxon_count": "1", "direct_assertion_count":
    "1", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms":
    "colorecta|colorectal|colorectum|colorectums"}}]'
  snapshot_sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
- evidence_id: ET7
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 1613
  accessed_at: '2026-10-16T03:54:43Z'
  support: supports
  summary: '[{"row": 1613, "data": {"term_id": "BTO:0001613", "ontology": "BTO", "label":
    "colorectum", "definition": "The colon and rectum considered as a unit.", "synonyms":
    "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EX8
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001613/graph
  locator: BTO_0001613-graph.json
  accessed_at: '2026-10-16T03:36:55Z'
  support: context_only
  summary: 'Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0001613",
    "target": "http://purl.obolibrary.org/obo/BTO_0000648", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 4995dd9cccf0e3affc43204a52ecf588234bb928184ed94177af43d147c7fb74
- evidence_id: EX9
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001613
  locator: BTO_0001613.json
  accessed_at: '2026-10-16T03:36:54Z'
  support: context_only
  summary: 'Current identity, active status, definition and typed synonyms: {"obo_id":
    "BTO:0001613", "label": "colorectum", "is_obsolete": false, "description": ["The
    colon and rectum considered as a unit."], "obo_synonym": null, "annotation": {"has_obo_namespace":
    ["BrendaTissueOBO"], "id": ["BTO:0001613"]}}'
  snapshot_sha256: 37722da3624694c9f95898969cb2230d7f8f55ff4d9f7ae0dfe73da13806f66c
- evidence_id: EX10
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3971631/fullTextXML
  locator: PMC3971631.xml
  accessed_at: '2026-10-16T03:46:27Z'
  support: context_only
  summary: 'PMID:24450771; DOI:10.1186/2049-2618-1-16. Introduction and co-aggregation
    methods/results inspected: exact CC53 is described as a colorectal-tumor isolate
    from the authors'' earlier study. Positive tissue association, not universal prevalence
    or cancer causation.'
  snapshot_sha256: 606880af66331df91e33d61ccd066bb97c64e11d7bf572d184ad92e0ecba856b
- evidence_id: EX11
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML
  locator: PMC8879827.xml
  accessed_at: '2026-10-16T03:52:56Z'
  support: context_only
  summary: 'PMID:35208748; DOI:10.3390/microorganisms10020293. Methods and scoring
    appendix inspected: channels have different evidence and scoring; score-three
    BioProject associations can derive from abstract mining. This does not identify
    the extraction route of any particular retained pair.'
  snapshot_sha256: 375f0fde4d07bb823cb9106aa4567bc0ef03c2866af0b2a7740b543f50687c25
- evidence_id: EX12
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=102234,1027273,1048357,1069963,1074311,1110509,1117,1120968,1120983,1121027,1150864,1173995,119852,1216969,1224163,1234143,1234144,1245026,1263,1280004,1292046,1297579,1342794,1342818,1348114,1385512,1401264,141693,1449351,1452538,1453497,1479025,1481923,1485,1578,1590,171549,171550,171552,186802,186803,189330,248039,31979,33038,33042,375288,384676,411459,411460,444103,51514,541000,560080,572511,816,830,838,85831,872&retmode=xml
  locator: taxonomy.xml
  accessed_at: '2026-10-16T03:37:40Z'
  support: context_only
  summary: 'Current exact TaxId resolutions, including merged IDs and labels: [{"id":
    "NCBITaxon:1297579", "source": "PREGO", "label": "Fusobacterium nucleatum CC53",
    "current_id": "1297579", "current_name": "Fusobacterium nucleatum CC53", "rank":
    "strain", "direct_match": true, "recognized_alias": true}]'
  snapshot_sha256: 8cc30a816c5940897a93cd10094f921f070f1378c3dab63db865fd736db4f15b
- evidence_id: ESEARCH
  kind: search
  reference: Local source/curation/review corpus
  locator: rg --no-ignore --hidden -l -F -e BTO:0001613 -e colorectum -e colorectum
    -e habitatmech:PREGO.cbfe86fae7 curation history research reports data/raw build
    reviews
  accessed_at: '2026-10-16T03:36:40Z'
  support: context_only
  summary: Source rows were parsed by exact keys; broad name hits were leads, not
    all inspected. No formal structured target predecessor.
  search_scope: curation, history, research, reports, data/raw, build and reviews
    including hidden/ignored files; structured YAML archive parsed independently of
    gitignore.
- evidence_id: EAVAIL
  kind: search
  reference: Configured kg-microbe checkout
  locator: find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe
    -type f '(' -ipath '*prego*' -o -ipath '*bacdive*' ')'
  accessed_at: '2026-10-16T03:46:37Z'
  support: context_only
  summary: Search found BacDive notebooks and Git metadata, but no manifest-matching
    BacDive/PREGO transformed node/edge exports. No claim of global absence.
  search_scope: find across the configured checkout, including hidden and ignored
    files.
assessments:
- assessment_id: A1
  area: identity
  topic: Identity, grounding, aliases and strictly broader hierarchy
  outcome: supported
  summary: 'BTO:0001613 denotes colon and rectum considered together. Its sole PREGO
    taxon, F. nucleatum CC53, has positive exact-strain context: the primary colorectal-carcinoma
    study explicitly identifies CC53 as its tumor isolate and assays it in culture.
    This supports colorectal tissue association, not universal healthy-colorectum
    residence, prevalence, or a causal cancer claim. Preserve the one TAXON count,
    score three, source identity and current name.'
  target_ids:
  - BTO:0001613
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EEXTRACT
  - ET5
  - ET6
  - ET7
  - EX8
  - EX9
  - EX10
  - EX11
  - EX12
- assessment_id: A2
  area: quantity
  topic: Native source units, ranks, scores and candidate pools
  outcome: supported
  summary: 'Exact source rows reproduce every emitted count/unit and displayed taxon
    rank/score/pool. Zero tree counts are omitted; supplemental biosamples, study
    memberships and triads are nonadditive. {"assertions": [{"source": "PREGO", "count":
    1, "unit": "TAXON", "row": {"row": 605, "data": {"prego_id": "BTO:0001613", "ontology":
    "BTO", "biolink_category": "biolink:GrossAnatomicalStructure", "taxon_count":
    "1", "direct_assertion_count": "1", "max_prego_score": "3", "channels": "annotated_genomes_isolates",
    "prego_synonyms": "colorecta|colorectal|colorectum|colorectums"}}}], "taxa": [{"id":
    "NCBITaxon:1297579", "source": "PREGO", "label": "Fusobacterium nucleatum CC53",
    "current_id": "1297579", "current_name": "Fusobacterium nucleatum CC53", "rank":
    "strain", "direct_match": true, "recognized_alias": true, "other_names": [], "source_row":
    {"row": 2405, "data": {"prego_id": "BTO:0001613", "rank": "1", "taxon_id": "NCBITaxon:1297579",
    "taxon_label": "Fusobacterium nucleatum CC53", "prego_score": "3", "direct_flag":
    "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}}]}'
  target_ids:
  - BTO:0001613
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EEXTRACT
  - ET5
  - ET6
  - ET7
  - EX8
  - EX9
  - EX10
  - EX11
  - EX12
- assessment_id: A3
  area: evidence
  topic: Association evidence and claim scope
  outcome: supported
  summary: 'Current ontology/TaxId identities and source attestations were verified.
    BTO:0001613 denotes colon and rectum considered together. Its sole PREGO taxon,
    F. nucleatum CC53, has positive exact-strain context: the primary colorectal-carcinoma
    study explicitly identifies CC53 as its tumor isolate and assays it in culture.
    This supports colorectal tissue association, not universal healthy-colorectum
    residence, prevalence, or a causal cancer claim. Preserve the one TAXON count,
    score three, source identity and current name. Individual papers support only
    the stated scope; original source pairs were not exhaustively reconstructed.'
  target_ids:
  - BTO:0001613
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EEXTRACT
  - ET5
  - ET6
  - ET7
  - EX8
  - EX9
  - EX10
  - EX11
  - EX12
- assessment_id: A4
  area: completeness
  topic: Native lifecycle, optional content and mechanism limits
  outcome: supported
  summary: Executed native routes reproduce EXACT/SEEDED. Required content is present.
    No optional environmental parameters, causal graph, discussion, dataset or characteristic-presence
    claim is fabricated. Missing ITEM status alone is not a defect; no status or history
    promotion is performed.
  target_ids:
  - BTO:0001613
  evidence_ids:
  - E1
  - ESCHEMA
  - ESEED
- assessment_id: A5
  area: schema
  topic: Native validation and reproducibility
  outcome: supported
  summary: '31 baseline commands passed: target schema, cohort strict, 831 histories,
    source provenance, exact 3209-record reproduction, 32 causal overlays, 110 term
    requests and configured labels. Exact-base hosted QC passed. Deterministic validity
    is not scientific approval.'
  target_ids:
  - BTO:0001613
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
findings: []
actions: []
limitations:
- Original specimen-level evidence and every pair-level citation were not exhaustively
  reconstructed. Source associations, counts, ranks and scores are not prevalence,
  viability or characteristic presence.
- Configured label validation skips 2063 no-adapter pairs; target TaxIds were separately
  resolved with current NCBI.
- Exact-base hosted QC covers unchanged scientific inputs, not a new local full-QC
  execution or these new review files. Each new bundle requires native validation/save
  and the subsequent archive check.
- 'iModulonDB is not applicable: no gene, regulator or expression-module claim is
  asserted. Cited experiments are used only for identity and context, not imported
  causal mechanisms.'
- Original source-strain or PREGO pair exports were unavailable in the configured
  checkout; no uncertain association is removed or source count rewritten.
notes:
- Captured working_tree provenance is retained. All local input hashes were additionally
  checked against exact base 67cde35918d7361de3a1164fb22756cba5d20e30.
- 'Read-only review: no source, curation, generated record, status or history edit;
  no GitHub mutation or paid research.'
- Ignored-inclusive structured archive traversal found no previous structured target
  review. Legacy prose is contextual evidence, not formal predecessor lineage or issue
  closure.
tags:
- individual-scientific-review
- host-associated
```
