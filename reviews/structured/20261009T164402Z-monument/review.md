# Record review: built heritage structure (monument)

- Review: 20261009T164402Z-monument
- Repository: culturebotai/HabitatMech
- Started UTC: 2026-10-09T16:21:14Z
- Finished UTC: 2026-10-09T16:44:02Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The curated built-heritage interpretation is positively supported by actual GOLD marble-associated organisms and primary isolation papers. Human construction/Built Environment are defensible broader contexts; constructed monument remains an overlapping xref, not an exact identity or universal genus. This bounded pass does not close the broader Monument/Stone issue #275.

## Scope And Provenance

One complete generated record and its claim-relevant maintained inputs; broader corpus review remains incomplete.

Selection: Next engineered filename lead without an individual structured target review, resolved by exact path and identifier. Historical filename inventories were selection aids, not current-coverage proof.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base c1398ac6e126d0298832bead8f77437c40112ca3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.a8b8ee2424 | data/habitats/engineered/monument.yaml | generated | built heritage structure |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.a8b8ee2424 | uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/engineered/monument.yaml<br>No issues found |
| validate-strict | passed | True | habitatmech:GOLD.a8b8ee2424 | uv run python scripts/validate_strict.py data/habitats/engineered/monument.yaml<br>Validating 1 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| Authoritative full QC | passed | True | habitatmech:GOLD.a8b8ee2424 | All HabitatMech quality gates passed; 647 passed, 3 skipped; 222 history records; 3208 schema-valid and exactly reproduced records; 32 causal overlays; 252 redirects; 109 term requests. |
| ID-label correspondence | passed | True | habitatmech:GOLD.a8b8ee2424 | 1178 OK_CANONICAL, 1 OK_SYNONYM, 5 OK_EXCEPTION, 2057 SKIPPED_NO_ADAPTER; all supported id-label pairs correspond. Unsupported adapters are not scientific passes. |
| Full target document and mint reproduction | passed | False | habitatmech:GOLD.a8b8ee2424 | All four complete build_document outputs equal disk; minted identifiers reproduce exact GOLD paths. One source each; Monument 1 ITEM-reviewed source/one definition; other three zero ITEM-reviewed sources. No applicable GOLD parent exclusions. |
| Structured expression evidence | not_applicable | False | habitatmech:GOLD.a8b8ee2424 | No expression, gene, locus or regulator claim in this target; no adapter query was required. |

## Scientific And Domain Assessments

### Built heritage habitat, definition and synonym scope

identity: supported. Targets: habitatmech:GOLD.a8b8ee2424.

Physical built-mineral habitat identity has positive source and primary-literature support. The authored definition and source-context alias Monument are defensible in this engineered path; do not treat the alias as every natural or constructed monument in unrestricted vocabulary.

### Parents, xref and ITEM-derived status

grounding: supported. Targets: habitatmech:GOLD.a8b8ee2424.

ENVO:00000070 and mesh:D000076624 are broader construction/environment contexts. ENVO:00000359 would be a false natural-site identity. ENVO:02000132 imposes memorial function and remains an overlap xref. The single ITEM-reviewed source plus definition legitimately yields REVIEWED without exact ontology grounding.

### Generalization and retained backlog

scope: unknown. Targets: habitatmech:GOLD.a8b8ee2424.

Inspected instances support but do not prove conservation, subaerial exposure and mineral fabric for every historical GOLD member. The current scope is curator-authored; issue #275 and the separately reviewed Interior wall scope are not closed.

### Source units, generation and status boundaries

provenance: supported. Targets: habitatmech:GOLD.a8b8ee2424.

Engineered &gt; Built environment &gt; Monument; gold.ecosystem:7125; nodes 7125/7142/7143; two ORGANISM assertions; no exact frozen BioSample, study or triad row. Complete build_document comparison and exact-path mint reproduction passed. One source contributes; no cross-source equivalence or unlike-unit sum is asserted.

### Parameters, taxa, mechanisms and evidence placement

completeness: not_applicable. Targets: habitatmech:GOLD.a8b8ee2424.

No environmental parameters, characteristic taxa, causal graphs, evidence blocks, datasets or discussion claims occur in this target. Empty optional fields are not automatically defects. No gene/locus/regulator/transcriptomics claim makes iModulonDB applicable. Literature examples inform identity only and are not imported as class-wide biology.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/habitats/engineered/monument.yaml; Entire generated HabitatRecord and parent records | supports | Engineered &gt; Built environment &gt; Monument; gold.ecosystem:7125; nodes 7125/7142/7143; two ORGANISM assertions; no exact frozen BioSample, study or triad row. |
| inventory | data/raw/gold_ecosystem_paths.tsv; row 776; decisions.tsv row 1576; term_requests.tsv row 77 | supports | The exact path has two ORGANISM assertions and three collapsed nodes. An ITEM decision rejects natural monument, retains constructed monument as xref, and the term request supplies the built-heritage definition under human construction in ADD mode. |
| workbook | https://gold.jgi.doe.gov/download?mode=site_excel; Organism Go0027725/Go0143274; Biosample Gb0341668-Gb0341670; Study Gs0156876 | supports | The newer export has DSM12652 from a marble statue and DSM46842 from monument marble, plus three marble-surface samples at Saint Demetrios in Thessalonica. These positively support built mineral heritage scope; matching the frozen count of two does not establish identical original membership. |
| isolates | https://pubmed.ncbi.nlm.nih.gov/29458502/; Abstract; DOI:10.1099/ijsem.0.002646; DSM46842 = BMG862 | supports | The type isolate came from monument marble at Bulla Regia, supporting one inspected GOLD organism's habitat. It does not establish universal heritage-class conditions. |
| statue | https://pubmed.ncbi.nlm.nih.gov/10758857/; Abstract; DOI:10.1099/00207713-50-2-529; DSM12652 = BC361 | supports | The type isolate originated on a marble statue surface. Historical Marmoricola naming is not a habitat identity change; current taxonomy was not imported into this record. |
| heritage | https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0163287; Abstract and sampling methods; DOI:10.1371/journal.pone.0163287 | supports | Microbial sampling on preserved brick, stone pillars and marble carvings supplies independent examples of built mineral heritage surfaces beyond a solely memorial-function scope. These are not asserted to be GOLD members. |
| ontology | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A02000132; Current definitions for ENVO:02000132, ENVO:00000359 and ENVO:00000070; compared with frozen ontology rows | supports | Constructed monument requires memorial function; natural monument is a protected natural environment; human construction requires deliberate assembly. These distinguish the rejected lexical match, overlapping xref and broader construction genus. |
| mesh | https://meshb.nlm.nih.gov/record/ui?ui=D000076624; 2026 Built Environment descriptor | supports | The descriptor covers man-made physical environmental elements, consistent with constructed heritage. It is not independently checked by the OAK label gate. |
| unesco | https://whc.unesco.org/en/conventiontext/; Article 1 | context_only | Architectural and archaeological works can be cultural monuments; the class is not restricted to commemorative function. This does not certify each GOLD sample's designation. |
| prior | https://github.com/CultureBotAI/HabitatMech/issues/275; Open Monument and Stone modeling issue | context_only | This bounded review supports the currently chosen Monument representation, but does not resolve the separate Stone target or close the combined issue. |
| absence | data/raw/ and curation/; Exact identifier, full source path and source accession matching | context_only | All 14 raw TSVs and top-level curation TSVs were parsed with exact-field and pipe-member comparisons. Hidden/ignored-aware searches covered target/context files and review selection; optional empty fields were checked against full records. |
| checks | just qc; Baseline working tree at c1398ac6e126d0298832bead8f77437c40112ca3 | supports | All HabitatMech quality gates passed; 647 passed, 3 skipped; 222 history records; 3208 schema-valid and exactly reproduced records; 32 causal overlays; 252 redirects; 109 term requests. |

## Limits And Additional Notes

- The full set of 22 model-generated dossier citations was not revalidated; only claim-relevant primary papers and authorities were inspected.
- The current public workbook differs from the frozen export. Three newer monument biosamples do not justify rewriting the historical two-ORGANISM count.
- NCBI SAMN10363428 and SAMN12292099 resolve the type-strain accessions but omit isolation-source fields; habitat corroboration comes from GOLD and the primary isolation papers, not those missing fields.
- No accession/PMID was supplied for the three newer monument Biosamples in the inspected project rows; their public GOLD metadata is database evidence, not independent publication proof.
- Schema, reproduction and label gates are deterministic checks, not proof of scientific completeness. Full QC skipped three tests; label checks contain configured exceptions and unsupported adapters.
- No paid research was run; existing model-generated research and historical reviews were treated as leads, not independent primary authority.
- Initial native inspect preceded assessment. Additional discovered context inputs were captured later only after comparing every original hash and the unchanged Git base; no hashes were silently refreshed.
- Frozen August inventories and the later public GOLD workbook are deliberately separate snapshots. Optional fields, source identifiers, mapping/status histories and generated ownership were assessed without editing scientific inputs.
- Auxiliary exploratory TSV/header probes initially failed and were corrected; all reported native checks completed with their stated results.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261009T164402Z-monument
kind: record
repository: culturebotai/HabitatMech
title: 'Record review: built heritage structure (monument)'
started_at: '2026-10-09T16:21:14Z'
finished_at: '2026-10-09T16:44:02Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent family has contributed repository curation and publication
    work; this is a separate evidence-review pass, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'The curated built-heritage interpretation is positively supported by actual
  GOLD marble-associated organisms and primary isolation papers. Human construction/Built
  Environment are defensible broader contexts; constructed monument remains an overlapping
  xref, not an exact identity or universal genus. This bounded pass does not close
  the broader Monument/Stone issue #275.'
source:
  git_revision: c1398ac6e126d0298832bead8f77437c40112ca3
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
    sha256: e1238e20fe1cc3d7bdce19354b9ea0f2ab949dba171b692238d321e741541191
    role: context
  - path: curation/term_requests.tsv
    sha256: 9977e384b79128d6e89c85f28e35c77d29644d503dea6d53c12628599e33f7f3
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: b59b9e800a918135e3915145d4d8098bb48dcea36a312b3004c594a57d221ae9
    role: context
  - path: data/habitats/engineered/built_environment.yaml
    sha256: df6de674d7d48a98b7d1d43a0a5c67a696550f00e1fb787ec71a3569acc47021
    role: context
  - path: data/habitats/engineered/human_construction.yaml
    sha256: cb18d75802047037b046072cb47805a8f2db1123b99cd346e690ad6e4065a3ea
    role: context
  - path: data/habitats/engineered/interior_wall.yaml
    sha256: dadb6cc869ac608e350515081d96f88d8223e3feb915251c50bda6e26f570b26
    role: context
  - path: data/habitats/engineered/monument.yaml
    sha256: acc4140b716b4d858917796dbb49837cdd0d8375d6f13de8bac50497bc304e7f
    role: target
  - path: data/habitats/engineered/stone.yaml
    sha256: 416b23ae32970801cb998c4d2705a08d98d77c88a57ad0c2b86d30db94a78337
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
  - path: history/mappings/monument/2026-09-10T034959Z-claude-code-4263cf.yaml
    sha256: 3f6062c0edd75245f3b62ab93e7317f62c00b1c302288da5e867e0d0bca6ff98
    role: context
  - path: history/mappings/monument/2026-09-10T035006Z-claude-code-d7c4c9.yaml
    sha256: 3825cc72de0f849e77910d579b245a478aef8a2d88556db65512a3c1d945a302
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20261009T005726Z-interior_wall.md
    sha256: 117f92c4e29f0c198df86d5f500fe8f0050d28b5c87931157891a6a35d661281
    role: context
  - path: research/habitats/engineered/monument-habitatmech-gold-a8b8ee2424-deep-research-claude_code.md
    sha256: de66fa4ff898b7ea0bf345b89d88cce25a8629a8a176c9c52782162382b24f16
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/extract_gold_biosamples.py
    sha256: b6a2773c86fe718e1ca0b1d7b32709f0eee491ac813655e310aa0817c0fec31b
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
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
  description: One complete generated record and its claim-relevant maintained inputs;
    broader corpus review remains incomplete.
  selection: Next engineered filename lead without an individual structured target
    review, resolved by exact path and identifier. Historical filename inventories
    were selection aids, not current-coverage proof.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.a8b8ee2424
  exclusions:
  - target: Other 3207 corpus records
    reason: Context records are not individually certified by this one-record review.
targets:
- target_id: habitatmech:GOLD.a8b8ee2424
  path: data/habitats/engineered/monument.yaml
  label: built heritage structure
  record_class: HabitatRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained source or curation owner relevant to identity and hierarchy
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained source or curation owner relevant to identity and hierarchy
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained source or curation owner relevant to identity and hierarchy
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Maintained source or curation owner relevant to identity and hierarchy
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Maintained source or curation owner relevant to identity and hierarchy
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_subclass_edges.tsv
    role: Maintained source or curation owner relevant to identity and hierarchy
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Deterministic source-to-record generator
checks:
- check_id: schema-0
  name: validate
  status: passed
  required: true
  summary: 'uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class
    HabitatRecord data/habitats/engineered/monument.yaml

    No issues found'
  target_ids:
  - habitatmech:GOLD.a8b8ee2424
  command: env UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/monument.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: schema-1
  name: validate-strict
  status: passed
  required: true
  summary: "uv run python scripts/validate_strict.py data/habitats/engineered/monument.yaml\n\
    Validating 1 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  target_ids:
  - habitatmech:GOLD.a8b8ee2424
  command: env UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/monument.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: qc
  name: Authoritative full QC
  status: passed
  required: true
  summary: All HabitatMech quality gates passed; 647 passed, 3 skipped; 222 history
    records; 3208 schema-valid and exactly reproduced records; 32 causal overlays;
    252 redirects; 109 term requests.
  target_ids:
  - habitatmech:GOLD.a8b8ee2424
  command: env UV_CACHE_DIR=build/uv-cache just qc
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - checks
- check_id: labels
  name: ID-label correspondence
  status: passed
  required: true
  summary: 1178 OK_CANONICAL, 1 OK_SYNONYM, 5 OK_EXCEPTION, 2057 SKIPPED_NO_ADAPTER;
    all supported id-label pairs correspond. Unsupported adapters are not scientific
    passes.
  target_ids:
  - habitatmech:GOLD.a8b8ee2424
  command: env UV_CACHE_DIR=build/uv-cache just validate-products
  exit_code: 0
  expected_exit_code: 0
  scope_note: Configured identity/causal-node pairs only; excludes source attestations,
    parent relationship semantics and characteristic taxa. Minted/MeSH prefixes lack
    adapters.
- check_id: reproduce
  name: Full target document and mint reproduction
  status: passed
  required: false
  summary: All four complete build_document outputs equal disk; minted identifiers
    reproduce exact GOLD paths. One source each; Monument 1 ITEM-reviewed source/one
    definition; other three zero ITEM-reviewed sources. No applicable GOLD parent
    exclusions.
  target_ids:
  - habitatmech:GOLD.a8b8ee2424
  exit_code: 0
  expected_exit_code: 0
- check_id: imodulondb
  name: Structured expression evidence
  status: not_applicable
  required: false
  summary: No expression, gene, locus or regulator claim in this target; no adapter
    query was required.
  target_ids:
  - habitatmech:GOLD.a8b8ee2424
evidence:
- evidence_id: record
  kind: record_content
  reference: data/habitats/engineered/monument.yaml
  locator: Entire generated HabitatRecord and parent records
  accessed_at: '2026-10-09T16:44:02Z'
  support: supports
  summary: Engineered > Built environment > Monument; gold.ecosystem:7125; nodes 7125/7142/7143;
    two ORGANISM assertions; no exact frozen BioSample, study or triad row.
- evidence_id: inventory
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: row 776; decisions.tsv row 1576; term_requests.tsv row 77
  accessed_at: '2026-10-09T16:44:02Z'
  support: supports
  summary: The exact path has two ORGANISM assertions and three collapsed nodes. An
    ITEM decision rejects natural monument, retains constructed monument as xref,
    and the term request supplies the built-heritage definition under human construction
    in ADD mode.
- evidence_id: workbook
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=site_excel
  locator: Organism Go0027725/Go0143274; Biosample Gb0341668-Gb0341670; Study Gs0156876
  accessed_at: '2026-10-09T16:44:02Z'
  support: supports
  summary: The newer export has DSM12652 from a marble statue and DSM46842 from monument
    marble, plus three marble-surface samples at Saint Demetrios in Thessalonica.
    These positively support built mineral heritage scope; matching the frozen count
    of two does not establish identical original membership.
  snapshot_sha256: 5f48b2f50fb2a9257754960a0f0e12dc6e8fa121e97c3e9f4497249e5fe6e439
- evidence_id: isolates
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/29458502/
  locator: Abstract; DOI:10.1099/ijsem.0.002646; DSM46842 = BMG862
  accessed_at: '2026-10-09T16:44:02Z'
  support: supports
  summary: The type isolate came from monument marble at Bulla Regia, supporting one
    inspected GOLD organism's habitat. It does not establish universal heritage-class
    conditions.
- evidence_id: statue
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/10758857/
  locator: Abstract; DOI:10.1099/00207713-50-2-529; DSM12652 = BC361
  accessed_at: '2026-10-09T16:44:02Z'
  support: supports
  summary: The type isolate originated on a marble statue surface. Historical Marmoricola
    naming is not a habitat identity change; current taxonomy was not imported into
    this record.
- evidence_id: heritage
  kind: primary_source
  reference: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0163287
  locator: Abstract and sampling methods; DOI:10.1371/journal.pone.0163287
  accessed_at: '2026-10-09T16:44:02Z'
  support: supports
  summary: Microbial sampling on preserved brick, stone pillars and marble carvings
    supplies independent examples of built mineral heritage surfaces beyond a solely
    memorial-function scope. These are not asserted to be GOLD members.
- evidence_id: ontology
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A02000132
  locator: Current definitions for ENVO:02000132, ENVO:00000359 and ENVO:00000070;
    compared with frozen ontology rows
  accessed_at: '2026-10-09T16:44:02Z'
  support: supports
  summary: Constructed monument requires memorial function; natural monument is a
    protected natural environment; human construction requires deliberate assembly.
    These distinguish the rejected lexical match, overlapping xref and broader construction
    genus.
- evidence_id: mesh
  kind: authority
  reference: https://meshb.nlm.nih.gov/record/ui?ui=D000076624
  locator: 2026 Built Environment descriptor
  accessed_at: '2026-10-09T16:44:02Z'
  support: supports
  summary: The descriptor covers man-made physical environmental elements, consistent
    with constructed heritage. It is not independently checked by the OAK label gate.
- evidence_id: unesco
  kind: authority
  reference: https://whc.unesco.org/en/conventiontext/
  locator: Article 1
  accessed_at: '2026-10-09T16:44:02Z'
  support: context_only
  summary: Architectural and archaeological works can be cultural monuments; the class
    is not restricted to commemorative function. This does not certify each GOLD sample's
    designation.
- evidence_id: prior
  kind: prior_review
  reference: https://github.com/CultureBotAI/HabitatMech/issues/275
  locator: Open Monument and Stone modeling issue
  accessed_at: '2026-10-09T16:44:02Z'
  support: context_only
  summary: This bounded review supports the currently chosen Monument representation,
    but does not resolve the separate Stone target or close the combined issue.
- evidence_id: absence
  kind: search
  reference: data/raw/ and curation/
  locator: Exact identifier, full source path and source accession matching
  accessed_at: '2026-10-09T16:44:02Z'
  support: context_only
  summary: All 14 raw TSVs and top-level curation TSVs were parsed with exact-field
    and pipe-member comparisons. Hidden/ignored-aware searches covered target/context
    files and review selection; optional empty fields were checked against full records.
  search_scope: Ignored files included via pathlib traversal and rg --no-ignore --hidden;
    bounded to repository inventories, curation surfaces, records, legacy reports
    and reviews. No universal internet absence is claimed.
- evidence_id: checks
  kind: validation
  reference: just qc
  locator: Baseline working tree at c1398ac6e126d0298832bead8f77437c40112ca3
  accessed_at: '2026-10-09T16:44:02Z'
  support: supports
  summary: All HabitatMech quality gates passed; 647 passed, 3 skipped; 222 history
    records; 3208 schema-valid and exactly reproduced records; 32 causal overlays;
    252 redirects; 109 term requests.
assessments:
- assessment_id: identity
  area: identity
  topic: Built heritage habitat, definition and synonym scope
  outcome: supported
  summary: Physical built-mineral habitat identity has positive source and primary-literature
    support. The authored definition and source-context alias Monument are defensible
    in this engineered path; do not treat the alias as every natural or constructed
    monument in unrestricted vocabulary.
  target_ids:
  - habitatmech:GOLD.a8b8ee2424
  evidence_ids:
  - record
  - inventory
  - workbook
  - isolates
  - statue
  - heritage
- assessment_id: grounding
  area: grounding
  topic: Parents, xref and ITEM-derived status
  outcome: supported
  summary: ENVO:00000070 and mesh:D000076624 are broader construction/environment
    contexts. ENVO:00000359 would be a false natural-site identity. ENVO:02000132
    imposes memorial function and remains an overlap xref. The single ITEM-reviewed
    source plus definition legitimately yields REVIEWED without exact ontology grounding.
  target_ids:
  - habitatmech:GOLD.a8b8ee2424
  evidence_ids:
  - record
  - inventory
  - ontology
  - mesh
  - unesco
- assessment_id: scope
  area: scope
  topic: Generalization and retained backlog
  outcome: unknown
  summary: 'Inspected instances support but do not prove conservation, subaerial exposure
    and mineral fabric for every historical GOLD member. The current scope is curator-authored;
    issue #275 and the separately reviewed Interior wall scope are not closed.'
  target_ids:
  - habitatmech:GOLD.a8b8ee2424
  evidence_ids:
  - workbook
  - heritage
  - prior
- assessment_id: provenance
  area: provenance
  topic: Source units, generation and status boundaries
  outcome: supported
  summary: Engineered > Built environment > Monument; gold.ecosystem:7125; nodes 7125/7142/7143;
    two ORGANISM assertions; no exact frozen BioSample, study or triad row. Complete
    build_document comparison and exact-path mint reproduction passed. One source
    contributes; no cross-source equivalence or unlike-unit sum is asserted.
  target_ids:
  - habitatmech:GOLD.a8b8ee2424
  evidence_ids:
  - record
  - inventory
  - checks
- assessment_id: optional
  area: completeness
  topic: Parameters, taxa, mechanisms and evidence placement
  outcome: not_applicable
  summary: No environmental parameters, characteristic taxa, causal graphs, evidence
    blocks, datasets or discussion claims occur in this target. Empty optional fields
    are not automatically defects. No gene/locus/regulator/transcriptomics claim makes
    iModulonDB applicable. Literature examples inform identity only and are not imported
    as class-wide biology.
  target_ids:
  - habitatmech:GOLD.a8b8ee2424
  evidence_ids:
  - record
  - absence
findings: []
actions: []
limitations:
- The full set of 22 model-generated dossier citations was not revalidated; only claim-relevant
  primary papers and authorities were inspected.
- The current public workbook differs from the frozen export. Three newer monument
  biosamples do not justify rewriting the historical two-ORGANISM count.
- NCBI SAMN10363428 and SAMN12292099 resolve the type-strain accessions but omit isolation-source
  fields; habitat corroboration comes from GOLD and the primary isolation papers,
  not those missing fields.
- No accession/PMID was supplied for the three newer monument Biosamples in the inspected
  project rows; their public GOLD metadata is database evidence, not independent publication
  proof.
- Schema, reproduction and label gates are deterministic checks, not proof of scientific
  completeness. Full QC skipped three tests; label checks contain configured exceptions
  and unsupported adapters.
- No paid research was run; existing model-generated research and historical reviews
  were treated as leads, not independent primary authority.
notes:
- Initial native inspect preceded assessment. Additional discovered context inputs
  were captured later only after comparing every original hash and the unchanged Git
  base; no hashes were silently refreshed.
- Frozen August inventories and the later public GOLD workbook are deliberately separate
  snapshots. Optional fields, source identifiers, mapping/status histories and generated
  ownership were assessed without editing scientific inputs.
- Auxiliary exploratory TSV/header probes initially failed and were corrected; all
  reported native checks completed with their stated results.
tags:
- record-review
- engineered
- source-scope
```
