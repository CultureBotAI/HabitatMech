# Record review: alveolus

- Review: 20261015T005601Z-alveolus-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T00:44:12Z
- Finished UTC: 2026-10-15T00:56:01Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

BTO:0000060 denotes the thin-walled pulmonary gas-exchange sac. The source variants air sac and air sacs remain related, not exact. PREGO supplies two score-three taxon associations and no characteristic-status assertion; both current NCBI strain identities resolve. The exact IMT2125 and chi7122 source project is avian-pathogenic E. coli. It reports chi7122 mutant inoculation into turkey air sacs and recovery from lung/liver, not demonstrated residence in mammalian pulmonary alveoli. An air-sac homonym or tissue-scope error is plausible; unavailable original PREGO pair references prevent a definitive rejection.

## Scope And Provenance

One complete generated record and all contributing source concepts; referenced parents are bounded context checks.

Selection: Next exact unreviewed identifier in the full-corpus inventory; one separate individual review, not a sampled category verdict.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base b09f0b8718528ce9b5853f3a809d2e1846499f99.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0000060 | data/habitats/host_associated/alveolus.yaml | generated | alveolus |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0000060 | Executed 2026-10-15T00:45:06Z to 2026-10-15T00:45:14Z. Exact target passes LinkML validation. |
| validate-strict | passed | True | BTO:0000060 | Executed 2026-10-15T00:45:14Z to 2026-10-15T00:45:31Z. Nine enumerated targets pass closed-schema validation with zero errors. |
| validate-history | passed | True | BTO:0000060 | Executed 2026-10-15T00:45:32Z to 2026-10-15T00:45:56Z. All 718 native history records validate. |
| provenance-check | passed | True | BTO:0000060 | Executed 2026-10-15T00:45:56Z to 2026-10-15T00:45:58Z. Fourteen committed inventories and two GOLD sources match their manifests. |
| verify-corpus | passed | True | BTO:0000060 | Executed 2026-10-15T00:45:58Z to 2026-10-15T00:47:11Z. All 3208 records reproduce exactly: zero missing, extra or differing. |
| validate-causal-all | passed | True | BTO:0000060 | Executed 2026-10-15T00:47:11Z to 2026-10-15T00:47:32Z. All 32 overlays and 32 causal graphs validate; this target has no graph. |
| term-requests-check | passed | True | BTO:0000060 | Executed 2026-10-15T00:47:32Z to 2026-10-15T00:48:41Z. The generated 110-term request table is current. |
| validate-products | passed | True | BTO:0000060 | Executed 2026-10-15T00:48:41Z to 2026-10-15T00:51:02Z. 1174 canonical labels, one synonym and five configured exceptions pass; 2061 identifiers without adapters are skipped. |
| Exact source and taxonomy comparison | passed | True | BTO:0000060 | Read-only structured audit checked 54 retained taxon rows, all target source rows, both actual alveoli resolution routes, the pinned Madin pool and retained workbook hashes. Completed 2026-10-15T00:47:57Z. |
| Original frozen upstream member/pair recovery | unavailable | False | BTO:0000060 | Ignored-inclusive find over the configured kg-microbe data/ and kg_microbe/ trees returned no PREGO-, Madin- or goldData-named files. Original member-level inputs and PREGO pair references were not recovered there; this is not global absence. Pinned transformations, committed inventories and later source exports do not substitute for the missing original payload. |
| iModulonDB and molecular adapters | not_applicable | False | BTO:0000060 | The target asserts no gene, regulator, expression module or molecular mechanism requiring these adapters. |

## Scientific And Domain Assessments

### Complete identity and source grounding

identity: supported. Targets: BTO:0000060.

BTO:0000060 denotes the thin-walled pulmonary gas-exchange sac. The source variants air sac and air sacs remain related, not exact. PREGO supplies two score-three taxon associations and no characteristic-status assertion; both current NCBI strain identities resolve.

### Anatomical, synonym and occurrence claim scope

scope: concern. Targets: BTO:0000060.

The exact IMT2125 and chi7122 source project is avian-pathogenic E. coli. It reports chi7122 mutant inoculation into turkey air sacs and recovery from lung/liver, not demonstrated residence in mammalian pulmonary alveoli. An air-sac homonym or tissue-scope error is plausible; unavailable original PREGO pair references prevent a definitive rejection.

### Counts, ranks, statuses and generated audit

provenance: supported. Targets: BTO:0000060.

The displayed fields reproduce their maintained inputs. Counts retain source-specific units; max scores and display ranking are not prevalence, confidence probabilities or taxonomy ranks. No source unit is combined with another.

### Optional enrichment and evidence limits

completeness: supported. Targets: BTO:0000060.

No causal graph or parameter ranges are asserted in the complete target. Optional absence is not a defect or evidence of ecological absence. Research hypotheses and parent biology were not imported. Scientific concerns are recorded separately rather than concealed by deterministic success.

## Findings

### F1: Avian air-sac context may be misread as pulmonary-alveolus occurrence

major / open / provisional; issue key: bto-0000060-prego-avian-air-sac-scope.

The exact IMT2125 and chi7122 source project is avian-pathogenic E. coli. It reports chi7122 mutant inoculation into turkey air sacs and recovery from lung/liver, not demonstrated residence in mammalian pulmonary alveoli. An air-sac homonym or tissue-scope error is plausible; unavailable original PREGO pair references prevent a definitive rejection.

## Recommended Actions And Acceptance Checks

### A1

Recover both original PREGO pair references and separate avian air-sac inoculation, whole-lung recovery and true alveolar localization. Preserve supported observations with the correct anatomical relation through maintained association inputs. Do not merge with the avian air-sac record or relabel taxa based solely on this suspected homonym.

- Resolve source scope and relation endpoints with inspected primary or original source evidence; retain explicit uncertainty until then.
- Make any separately authorized correction in maintained inputs, append native history, run just seed and inspect affected just seed-canary output before regeneration.
- Add focused regressions for the supported and rejected scopes; run strict/schema, provenance, history, corpus reproduction, causal, term-request and configured label gates, followed by just qc.
- Inspect actual downstream mappings and generated pages/redirects after any identity or relation change; deterministic record checks do not certify SSSOM/KGX compatibility.
- Save an immutable successor with these exact finding identities; do not rewrite this observation or promote scientific status by review alone.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/habitats/host_associated/alveolus.yaml; Complete YAML at b09f0b8718528ce9b5853f3a809d2e1846499f99 | supports | BTO:0000060 denotes the thin-walled pulmonary gas-exchange sac. The source variants air sac and air sacs remain related, not exact. PREGO supplies two score-three taxon associations and no characteristic-status assertion; both current NCBI strain identities resolve. The exact IMT2125 and chi7122 source project is avian-pathogenic E. coli. It reports chi7122 mutant inoculation into turkey air sacs and recovery from lung/liver, not demonstrated residence in mammalian pulmonary alveoli. An air-sac homonym or tissue-scope error is plausible; unavailable original PREGO pair references prevent a definitive rejection. |
| raw | data/raw/; data/habitats/PATHS.tsv; data/raw/prego_habitat_taxa.tsv: rows 33,34; data/raw/prego_habitats.tsv: rows 467; data/raw/ontology_terms.tsv: rows 62,13188 | supports | Exact source identifiers, nodes/paths, source counts/units, retained taxon fields and ontology rows were compared with the entire generated record. Structured source details: {"source_rows": [], "taxa": [{"current_taxonomy": {"canonical": "1204724", "label": "Escherichia coli IMT2125", "lineage": "cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Enterobacterales; Enterobacteriaceae; Escherichia; Escherichia coli; Escherichia coli O78:H9", "rank": "strain"}, "source": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0000060", "prego_score": "3", "rank": "1", "taxon_id": "NCBITaxon:1204724", "taxon_label": "Escherichia coli IMT2125"}}, {"current_taxonomy": {"canonical": "475609", "label": "Escherichia coli chi7122", "lineage": "cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Enterobacterales; Enterobacteriaceae; Escherichia; Escherichia coli", "rank": "strain"}, "source": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0000060", "prego_score": "3", "rank": "2", "taxon_id": "NCBITaxon:475609", "taxon_label": "Escherichia coli chi7122"}}]} |
| owners | curation/decisions.tsv; curation/term_requests.tsv; curation/gold_parent_exclusions.tsv; curation/record_annotation_corrections.tsv; Exact source mints habitatmech:PREGO.e88a5ce5ba; row locations in raw evidence | supports | All contributing decisions and definition rows were inspected. ITEM depth, not a saved review, controls REVIEWED. Owner rows: {} |
| rules | docs/CURATION.md; docs/HARMONIZATION.md; src/habitatmech/schema/habitatmech.yaml; src/habitatmech/seed.py; src/habitatmech/extract.py; Native checklist, source-to-record predicate contract, strict parents, source-unit counts and taxon ranking | supports | Parent_habitats asserts strictly broader classes, not anatomical containment. Source association is not characteristic prevalence. PREGO retains best scores, direct flags and channel unions, sorting by score/direct flag/ID; taxonomy ranks differ from displayed source rank. |
| legacy | reports/yaml_record_review/20261002T110502Z-alveolus.md; Historical ad hoc target reports, findings and evidence leads | supports | Legacy reports were rechecked against current files and inspected primary evidence. Their stable finding keys are retained when applicable; they are not native structured predecessors, and no previous_occurrences is fabricated. |
| search | curation/; history/; research/; reports/; data/raw/; build/; reviews/; Identifier, label, slug and source-mint search using rg --no-ignore --hidden -l -F | supports | Ignored files were included. The current nine-target search exited 0 with 6837 matching files. Exact matching tables and native review census were then parsed. No prior native individual bundle was found for these nine IDs; related mentions and legacy reports are not counted as completed individual coverage. |
| taxonomy | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=102127,104269,1044,1087449,1121011,1122135,1122191,1128113,113355,1137780,1141221,1142394,1154763,1156985,1158132,1158134,1170562,1204724,1219065,1219071,1236544,1263,1265,1279017,1304,1314,1347420,1380,1408286,1433126,1437605,1485,152297,1679001,171549,1842533,1842534,1842535,1842536,185761,186802,186803,1869227,2,214092,28211,31979,33042,475609,541000,629395,766,830,84107; All 2 displayed taxon IDs; ScientificName, Rank, Lineage and AkaTaxIds | supports | Every displayed identifier resolves directly or via an explicit alias. Current names/ranks are retained in the raw audit evidence; name equivalence is not evidence of habitat occurrence. |
| prego_transform | https://raw.githubusercontent.com/Knowledge-Graph-Hub/kg-microbe/7698351a54b48f2e917635fdf51cd0a6b323135d/kg_microbe/transform_utils/prego/prego.py; Pinned kg-microbe 7698351a54b48f2e917635fdf51cd0a6b323135d, lines 874-888; HabitatMech extract.py lines 337-435 | supports | The upstream BTO/taxon route emits tissue-to-taxon location_of edges. The retained local inventory preserves scores/channels but not pair-level source references. Direct flag and score do not independently prove tissue localization. |
| ontology | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000060; Active pulmonary definition | supports | The target is a gas-exchanging pulmonary alveolus. |
| avian | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0009060; Bird-specific air-sac definition | supports | Avian air sacs are anatomically distinct from pulmonary alveoli. |
| project | https://www.ncbi.nlm.nih.gov/bioproject/PRJEB51; NCBI project description, IMT2125/chi7122 and intra-airsac turkey experiment | supports | The project explicitly identifies both APEC strains and the turkey inoculation model. It does not provide the missing original PREGO pair evidence. |
| apec | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3900561/fullTextXML; Figure 3 caption, Table 1 and sequence-comparison methods | supports | The paper lists IMT2125 NZ_HE964769 and chi7122 NZ_HE962388.1 among APEC genomes; no universal pulmonary occurrence is inferred. |

## Limits And Additional Notes

- This review assesses exact committed input bytes at b09f0b8718528ce9b5853f3a809d2e1846499f99, also verified unchanged on disk at drafting. It does not change curation, history, generated products or GitHub.
- Configured label correspondence skips identifiers without adapters; the actual result below must not be read as full identifier or biological validation.
- Original upstream payloads remain unavailable in the bounded configured-checkout search. Selected primary witnesses do not establish ecological support for every source member.
- No SSSOM/KGX product audit or compatibility certification was performed. No paid research was run.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T005601Z-alveolus-record
kind: record
repository: CultureBotAI/HabitatMech
title: 'Record review: alveolus'
started_at: '2026-10-15T00:44:12Z'
finished_at: '2026-10-15T00:56:01Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Continuing review agent; current claims and historical leads
    were reassessed against primary evidence. No independent approval is claimed.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: BTO:0000060 denotes the thin-walled pulmonary gas-exchange sac. The source
  variants air sac and air sacs remain related, not exact. PREGO supplies two score-three
  taxon associations and no characteristic-status assertion; both current NCBI strain
  identities resolve. The exact IMT2125 and chi7122 source project is avian-pathogenic
  E. coli. It reports chi7122 mutant inoculation into turkey air sacs and recovery
  from lung/liver, not demonstrated residence in mammalian pulmonary alveoli. An air-sac
  homonym or tissue-scope error is plausible; unavailable original PREGO pair references
  prevent a definitive rejection.
source:
  git_revision: b09f0b8718528ce9b5853f3a809d2e1846499f99
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
    sha256: 3072cbab4fc5f9241e595a681b0f9095ae0942c9dba6502fb01afc52fe67d919
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 505e6efc536392c9f6ce77fd4a70284392166269713189ff53e40367256d2899
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 77240ee178c7374a1d872a4226cd7c05916097b9b1d78679ae921666feead297
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: 11f153cc7f19333dc89a9019ef59c33b210bbebb44dd4e84b11166be3dd3927f
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: 8d4ce33422cf749d02b43d734fdcbefeb5dd04b79ef8574cc361548a112da0b8
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: b0135af0aa4deed0f3824a2f491d5a742c1b7de4775c533f283761d22e805821
    role: context
  - path: data/habitats/host_associated/alveolus.yaml
    sha256: 1dc7c8ae39283e173d7eb89fb1c727451578b0449f511722eefd2230524fcacb
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
  - path: reports/yaml_record_review/20261002T110502Z-alveolus.md
    sha256: e8e030cd8db744ff3b7d8bccf2b0378e877966c35b3bfed0c6f94d38d7ae59b3
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/habitatmech/curate/decisions.py
    sha256: f33d3e9dc95bb428e63e640d48d4074cf15e90ea666603fb16fb651d591e3f02
    role: context
  - path: src/habitatmech/curate/definitions.py
    sha256: decd02eea029e884ab1a8bbb51dd870edb5544906b3ddd39598147b27ce572c9
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
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
    role: context
  - path: src/habitatmech/seed.py
    sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
    role: context
targets:
- target_id: BTO:0000060
  path: data/habitats/host_associated/alveolus.yaml
  label: alveolus
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitat_taxa.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained source, curation input, or generator; target YAML is read-only
scope:
  description: One complete generated record and all contributing source concepts;
    referenced parents are bounded context checks.
  selection: Next exact unreviewed identifier in the full-corpus inventory; one separate
    individual review, not a sampled category verdict.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - BTO:0000060
checks:
- check_id: C8
  name: validate
  status: passed
  required: true
  target_ids:
  - BTO:0000060
  exit_code: 0
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/alveolus.yaml
  summary: Executed 2026-10-15T00:45:06Z to 2026-10-15T00:45:14Z. Exact target passes
    LinkML validation.
- check_id: C9
  name: validate-strict
  status: passed
  required: true
  target_ids:
  - BTO:0000060
  exit_code: 0
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/air_breathing_organ.yaml data/habitats/host_associated/air_sac.yaml
    data/habitats/host_associated/air_sacs__d20658f1.yaml data/habitats/host_associated/algae.yaml
    data/habitats/host_associated/alimentary_canal.yaml data/habitats/host_associated/alveolar_bone.yaml
    data/habitats/host_associated/alveoli.yaml data/habitats/host_associated/alveoli__5d35ddee.yaml
    data/habitats/host_associated/alveolus.yaml
  summary: Executed 2026-10-15T00:45:14Z to 2026-10-15T00:45:31Z. Nine enumerated
    targets pass closed-schema validation with zero errors.
- check_id: C10
  name: validate-history
  status: passed
  required: true
  target_ids:
  - BTO:0000060
  exit_code: 0
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  summary: Executed 2026-10-15T00:45:32Z to 2026-10-15T00:45:56Z. All 718 native history
    records validate.
- check_id: C11
  name: provenance-check
  status: passed
  required: true
  target_ids:
  - BTO:0000060
  exit_code: 0
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  summary: Executed 2026-10-15T00:45:56Z to 2026-10-15T00:45:58Z. Fourteen committed
    inventories and two GOLD sources match their manifests.
- check_id: C12
  name: verify-corpus
  status: passed
  required: true
  target_ids:
  - BTO:0000060
  exit_code: 0
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  summary: 'Executed 2026-10-15T00:45:58Z to 2026-10-15T00:47:11Z. All 3208 records
    reproduce exactly: zero missing, extra or differing.'
- check_id: C13
  name: validate-causal-all
  status: passed
  required: true
  target_ids:
  - BTO:0000060
  exit_code: 0
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  summary: Executed 2026-10-15T00:47:11Z to 2026-10-15T00:47:32Z. All 32 overlays
    and 32 causal graphs validate; this target has no graph.
- check_id: C14
  name: term-requests-check
  status: passed
  required: true
  target_ids:
  - BTO:0000060
  exit_code: 0
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  summary: Executed 2026-10-15T00:47:32Z to 2026-10-15T00:48:41Z. The generated 110-term
    request table is current.
- check_id: C15
  name: validate-products
  status: passed
  required: true
  target_ids:
  - BTO:0000060
  exit_code: 0
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  summary: Executed 2026-10-15T00:48:41Z to 2026-10-15T00:51:02Z. 1174 canonical labels,
    one synonym and five configured exceptions pass; 2061 identifiers without adapters
    are skipped.
- check_id: structured_audit
  name: Exact source and taxonomy comparison
  status: passed
  required: true
  target_ids:
  - BTO:0000060
  exit_code: 0
  command: .venv/bin/python /private/tmp/habitatmech-review-bz-work.py audit
  summary: Read-only structured audit checked 54 retained taxon rows, all target source
    rows, both actual alveoli resolution routes, the pinned Madin pool and retained
    workbook hashes. Completed 2026-10-15T00:47:57Z.
- check_id: original_payload
  name: Original frozen upstream member/pair recovery
  status: unavailable
  required: false
  target_ids:
  - BTO:0000060
  summary: Ignored-inclusive find over the configured kg-microbe data/ and kg_microbe/
    trees returned no PREGO-, Madin- or goldData-named files. Original member-level
    inputs and PREGO pair references were not recovered there; this is not global
    absence. Pinned transformations, committed inventories and later source exports
    do not substitute for the missing original payload.
- check_id: molecular
  name: iModulonDB and molecular adapters
  status: not_applicable
  required: false
  target_ids:
  - BTO:0000060
  summary: The target asserts no gene, regulator, expression module or molecular mechanism
    requiring these adapters.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/habitats/host_associated/alveolus.yaml
  locator: Complete YAML at b09f0b8718528ce9b5853f3a809d2e1846499f99
  summary: BTO:0000060 denotes the thin-walled pulmonary gas-exchange sac. The source
    variants air sac and air sacs remain related, not exact. PREGO supplies two score-three
    taxon associations and no characteristic-status assertion; both current NCBI strain
    identities resolve. The exact IMT2125 and chi7122 source project is avian-pathogenic
    E. coli. It reports chi7122 mutant inoculation into turkey air sacs and recovery
    from lung/liver, not demonstrated residence in mammalian pulmonary alveoli. An
    air-sac homonym or tissue-scope error is plausible; unavailable original PREGO
    pair references prevent a definitive rejection.
  support: supports
  accessed_at: '2026-10-15T00:56:01Z'
- evidence_id: raw
  kind: record_content
  reference: data/raw/; data/habitats/PATHS.tsv
  locator: 'data/raw/prego_habitat_taxa.tsv: rows 33,34; data/raw/prego_habitats.tsv:
    rows 467; data/raw/ontology_terms.tsv: rows 62,13188'
  summary: 'Exact source identifiers, nodes/paths, source counts/units, retained taxon
    fields and ontology rows were compared with the entire generated record. Structured
    source details: {"source_rows": [], "taxa": [{"current_taxonomy": {"canonical":
    "1204724", "label": "Escherichia coli IMT2125", "lineage": "cellular organisms;
    Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Enterobacterales;
    Enterobacteriaceae; Escherichia; Escherichia coli; Escherichia coli O78:H9", "rank":
    "strain"}, "source": {"channels": "annotated_genomes_isolates", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "BTO:0000060", "prego_score": "3", "rank":
    "1", "taxon_id": "NCBITaxon:1204724", "taxon_label": "Escherichia coli IMT2125"}},
    {"current_taxonomy": {"canonical": "475609", "label": "Escherichia coli chi7122",
    "lineage": "cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
    Enterobacterales; Enterobacteriaceae; Escherichia; Escherichia coli", "rank":
    "strain"}, "source": {"channels": "annotated_genomes_isolates", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "BTO:0000060", "prego_score": "3", "rank":
    "2", "taxon_id": "NCBITaxon:475609", "taxon_label": "Escherichia coli chi7122"}}]}'
  support: supports
  accessed_at: '2026-10-15T00:56:01Z'
- evidence_id: owners
  kind: record_content
  reference: curation/decisions.tsv; curation/term_requests.tsv; curation/gold_parent_exclusions.tsv;
    curation/record_annotation_corrections.tsv
  locator: Exact source mints habitatmech:PREGO.e88a5ce5ba; row locations in raw evidence
  summary: 'All contributing decisions and definition rows were inspected. ITEM depth,
    not a saved review, controls REVIEWED. Owner rows: {}'
  support: supports
  accessed_at: '2026-10-15T00:56:01Z'
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md; docs/HARMONIZATION.md; src/habitatmech/schema/habitatmech.yaml;
    src/habitatmech/seed.py; src/habitatmech/extract.py
  locator: Native checklist, source-to-record predicate contract, strict parents,
    source-unit counts and taxon ranking
  summary: Parent_habitats asserts strictly broader classes, not anatomical containment.
    Source association is not characteristic prevalence. PREGO retains best scores,
    direct flags and channel unions, sorting by score/direct flag/ID; taxonomy ranks
    differ from displayed source rank.
  support: supports
  accessed_at: '2026-10-15T00:56:01Z'
- evidence_id: legacy
  kind: prior_review
  reference: reports/yaml_record_review/20261002T110502Z-alveolus.md
  locator: Historical ad hoc target reports, findings and evidence leads
  summary: Legacy reports were rechecked against current files and inspected primary
    evidence. Their stable finding keys are retained when applicable; they are not
    native structured predecessors, and no previous_occurrences is fabricated.
  support: supports
  accessed_at: '2026-10-15T00:56:01Z'
- evidence_id: search
  kind: search
  reference: curation/; history/; research/; reports/; data/raw/; build/; reviews/
  locator: Identifier, label, slug and source-mint search using rg --no-ignore --hidden
    -l -F
  summary: Ignored files were included. The current nine-target search exited 0 with
    6837 matching files. Exact matching tables and native review census were then
    parsed. No prior native individual bundle was found for these nine IDs; related
    mentions and legacy reports are not counted as completed individual coverage.
  support: supports
  accessed_at: '2026-10-15T00:56:01Z'
  search_scope: curation/; history/; research/; reports/; data/raw/; build/; reviews/;
    ignored and hidden files included; exact identifier, label, slug and source-mint
    strings; results refined by structured table and review parsing.
- evidence_id: taxonomy
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=102127,104269,1044,1087449,1121011,1122135,1122191,1128113,113355,1137780,1141221,1142394,1154763,1156985,1158132,1158134,1170562,1204724,1219065,1219071,1236544,1263,1265,1279017,1304,1314,1347420,1380,1408286,1433126,1437605,1485,152297,1679001,171549,1842533,1842534,1842535,1842536,185761,186802,186803,1869227,2,214092,28211,31979,33042,475609,541000,629395,766,830,84107
  locator: All 2 displayed taxon IDs; ScientificName, Rank, Lineage and AkaTaxIds
  summary: Every displayed identifier resolves directly or via an explicit alias.
    Current names/ranks are retained in the raw audit evidence; name equivalence is
    not evidence of habitat occurrence.
  support: supports
  accessed_at: '2026-10-14T23:43:53Z'
  snapshot_sha256: 847965140998633d95fde21a1f24a9615a400e89edb6093af10a6a2209620697
- evidence_id: prego_transform
  kind: database
  reference: https://raw.githubusercontent.com/Knowledge-Graph-Hub/kg-microbe/7698351a54b48f2e917635fdf51cd0a6b323135d/kg_microbe/transform_utils/prego/prego.py
  locator: Pinned kg-microbe 7698351a54b48f2e917635fdf51cd0a6b323135d, lines 874-888;
    HabitatMech extract.py lines 337-435
  summary: The upstream BTO/taxon route emits tissue-to-taxon location_of edges. The
    retained local inventory preserves scores/channels but not pair-level source references.
    Direct flag and score do not independently prove tissue localization.
  support: supports
  accessed_at: '2026-10-15T00:45:16Z'
  snapshot_sha256: f516be3f28db9d9e4a3a49b46db9f06b42b5d9d0e857e2e5ee76ce0245a0fda8
- evidence_id: ontology
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000060
  locator: Active pulmonary definition
  summary: The target is a gas-exchanging pulmonary alveolus.
  support: supports
  accessed_at: '2026-10-14T23:43:39Z'
  snapshot_sha256: c0b82591770cf374c8cd4a834c557305930c25a86a71e2984d705535119e9909
- evidence_id: avian
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0009060
  locator: Bird-specific air-sac definition
  summary: Avian air sacs are anatomically distinct from pulmonary alveoli.
  support: supports
  accessed_at: '2026-10-14T23:43:47Z'
  snapshot_sha256: 4157f34baee4b76ac57fa331ebcfb57fdb60229ab16ef5edd58cc9f4b4d86606
- evidence_id: project
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/bioproject/PRJEB51
  locator: NCBI project description, IMT2125/chi7122 and intra-airsac turkey experiment
  summary: The project explicitly identifies both APEC strains and the turkey inoculation
    model. It does not provide the missing original PREGO pair evidence.
  support: supports
  accessed_at: '2026-10-15T00:45:15Z'
  snapshot_sha256: 8c37dbdf474037364784254ac06602f16777ce38bfe5c586fe7288a0471705d3
- evidence_id: apec
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3900561/fullTextXML
  locator: Figure 3 caption, Table 1 and sequence-comparison methods
  summary: The paper lists IMT2125 NZ_HE964769 and chi7122 NZ_HE962388.1 among APEC
    genomes; no universal pulmonary occurrence is inferred.
  support: supports
  accessed_at: '2026-10-15T00:44:16Z'
  snapshot_sha256: a3eb4b026349d98a9415f410e2680f22c2dbc6c7da03bf5c975b3cdb9f0d866c
assessments:
- assessment_id: identity
  area: identity
  topic: Complete identity and source grounding
  outcome: supported
  target_ids:
  - BTO:0000060
  evidence_ids:
  - record
  - raw
  - owners
  summary: BTO:0000060 denotes the thin-walled pulmonary gas-exchange sac. The source
    variants air sac and air sacs remain related, not exact. PREGO supplies two score-three
    taxon associations and no characteristic-status assertion; both current NCBI strain
    identities resolve.
- assessment_id: scientific_scope
  area: scope
  topic: Anatomical, synonym and occurrence claim scope
  outcome: concern
  target_ids:
  - BTO:0000060
  evidence_ids:
  - record
  - rules
  - ontology
  - avian
  - project
  - apec
  summary: The exact IMT2125 and chi7122 source project is avian-pathogenic E. coli.
    It reports chi7122 mutant inoculation into turkey air sacs and recovery from lung/liver,
    not demonstrated residence in mammalian pulmonary alveoli. An air-sac homonym
    or tissue-scope error is plausible; unavailable original PREGO pair references
    prevent a definitive rejection.
- assessment_id: source_fidelity
  area: provenance
  topic: Counts, ranks, statuses and generated audit
  outcome: supported
  target_ids:
  - BTO:0000060
  evidence_ids:
  - raw
  - owners
  - rules
  summary: The displayed fields reproduce their maintained inputs. Counts retain source-specific
    units; max scores and display ranking are not prevalence, confidence probabilities
    or taxonomy ranks. No source unit is combined with another.
- assessment_id: optional
  area: completeness
  topic: Optional enrichment and evidence limits
  outcome: supported
  target_ids:
  - BTO:0000060
  evidence_ids:
  - record
  - search
  - rules
  summary: No causal graph or parameter ranges are asserted in the complete target.
    Optional absence is not a defect or evidence of ecological absence. Research hypotheses
    and parent biology were not imported. Scientific concerns are recorded separately
    rather than concealed by deterministic success.
findings:
- issue_key: bto-0000060-prego-avian-air-sac-scope
  category: scope
  severity: major
  status: open
  certainty: provisional
  title: Avian air-sac context may be misread as pulmonary-alveolus occurrence
  description: The exact IMT2125 and chi7122 source project is avian-pathogenic E.
    coli. It reports chi7122 mutant inoculation into turkey air sacs and recovery
    from lung/liver, not demonstrated residence in mammalian pulmonary alveoli. An
    air-sac homonym or tissue-scope error is plausible; unavailable original PREGO
    pair references prevent a definitive rejection.
  field_paths:
  - characteristic_taxa
  evidence_ids:
  - record
  - raw
  - taxonomy
  - ontology
  - avian
  - project
  - apec
  - prego_transform
  rule_id: HabitatMech:claim-scope-and-strict-broader-identity
  native_severity: major
  normalization_reason: The finding changes the scientific interpretation of an anatomical
    relation, identity or occurrence claim, rather than style. Provisional findings
    require original source evidence before correction.
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitat_taxa.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained source, curation input, or generator; target YAML is read-only
  finding_id: F1
  target_ids:
  - BTO:0000060
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - BTO:0000060
  description: Recover both original PREGO pair references and separate avian air-sac
    inoculation, whole-lung recovery and true alveolar localization. Preserve supported
    observations with the correct anatomical relation through maintained association
    inputs. Do not merge with the avian air-sac record or relabel taxa based solely
    on this suspected homonym.
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitat_taxa.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained source, curation input, or generator; target YAML is read-only
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Resolve source scope and relation endpoints with inspected primary or original
    source evidence; retain explicit uncertainty until then.
  - Make any separately authorized correction in maintained inputs, append native
    history, run just seed and inspect affected just seed-canary output before regeneration.
  - Add focused regressions for the supported and rejected scopes; run strict/schema,
    provenance, history, corpus reproduction, causal, term-request and configured
    label gates, followed by just qc.
  - Inspect actual downstream mappings and generated pages/redirects after any identity
    or relation change; deterministic record checks do not certify SSSOM/KGX compatibility.
  - Save an immutable successor with these exact finding identities; do not rewrite
    this observation or promote scientific status by review alone.
limitations:
- This review assesses exact committed input bytes at b09f0b8718528ce9b5853f3a809d2e1846499f99,
  also verified unchanged on disk at drafting. It does not change curation, history,
  generated products or GitHub.
- Configured label correspondence skips identifiers without adapters; the actual result
  below must not be read as full identifier or biological validation.
- Original upstream payloads remain unavailable in the bounded configured-checkout
  search. Selected primary witnesses do not establish ecological support for every
  source member.
- No SSSOM/KGX product audit or compatibility certification was performed. No paid
  research was run.
```
