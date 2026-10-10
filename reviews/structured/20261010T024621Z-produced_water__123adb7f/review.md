# Scientific record review: Produced water (produced_water__123adb7f)

- Review: 20261010T024621Z-produced_water__123adb7f
- Repository: culturebotai/HabitatMech
- Started UTC: 2026-10-10T02:31:35Z
- Finished UTC: 2026-10-10T02:46:21Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The source path is reproducible and plausibly describes a microbial treatment environment, but the water label and apparatus parent leave a material-versus-treatment-system ambiguity. A provisional major finding requires source-level adjudication before either retaining the apparatus genus or excluding it. This is not an automatic correction based on a label.

## Scope And Provenance

Read-only scientific review of exactly one resolved generated HabitatRecord and all its contributing source claims.

Selection: Next individually resolved target in the continuing complete-corpus review; the 3208-record objective is unchanged, not replaced by this six-target working sequence.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 2e30ed4df3b727ed4080b58603805a988b4b19f3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.df1d688f27 | data/habitats/engineered/produced_water__123adb7f.yaml | generated | Produced water |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native validate | passed | True | habitatmech:GOLD.df1d688f27 | Executed 2026-10-10T02:32:53.416314+00:00 to 2026-10-10T02:32:56.277867+00:00, exit 0. No issues found |
| Native validate-strict | passed | True | habitatmech:GOLD.df1d688f27 | Executed 2026-10-10T02:33:07.305687+00:00 to 2026-10-10T02:33:12.126028+00:00, exit 0.  Six-record closed-schema validation reported zero errors. |
| Native verify-corpus | passed | True | habitatmech:GOLD.df1d688f27 | Executed 2026-10-10T02:33:12.126726+00:00 to 2026-10-10T02:33:26.893271+00:00, exit 0. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ |
| Native validate-products | passed | True | habitatmech:GOLD.df1d688f27 | Executed 2026-10-10T02:33:26.893850+00:00 to 2026-10-10T02:34:11.792770+00:00, exit 0. id↔label correspondence summary:<br>          OK_CANONICAL: 1178<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2057<br><br>✅ All id↔label pairs correspond. |
| Native review-check | passed | True | habitatmech:GOLD.df1d688f27 | Executed 2026-10-10T02:34:11.793358+00:00 to 2026-10-10T02:36:36.946542+00:00, exit 0. {<br>  "repository": "culturebotai/HabitatMech",<br>  "valid_reviews": 88,<br>  "coverage": "declared_scopes_only"<br>}<br>....                                                                     [100%]<br>4 passed in 69.73s (0:01:09) |
| Full exact-base QC | passed | True | habitatmech:GOLD.df1d688f27 | Completed CI at the captured Git base: 656 passed, 3 skipped, all native QC gates passed; run head and conclusion also fetched through gh run view --json. Three skipped tests remain disclosed. |
| Whole-target source trace | passed | True | habitatmech:GOLD.df1d688f27 | All six generated documents equal seed.build_document. All raw/root-curation tables and path mappings parsed; current input hashes freshly verified unchanged. |
| Dated workbook census revalidation | passed | True | habitatmech:GOLD.df1d688f27 | Both hashes match the complete earlier census from /private/tmp/habitatmech-review-t-workbook.py, whose parser was inspected. This turn reuses the dated census; it does not claim a fresh bulk download/scan. |
| Exact ontology and selected external records | passed | False | habitatmech:GOLD.df1d688f27 | Eight accession/project XML responses and six OLS term responses retrieved with exit 0. Relevant evidence is separately scoped per target; no whole-roster external verification claimed. |
| Scientific baseline unchanged | passed | True | habitatmech:GOLD.df1d688f27 | Exit 0. All 52 captured repository inputs independently SHA256-checked before authoring. |
| Causal and expression applicability | not_applicable | False | habitatmech:GOLD.df1d688f27 | Target has no causal edges, causal overlay, genes, regulators or transcriptomic claims. iModulonDB and target-specific causal validation are not applicable; complete baseline QC covers all maintained overlays. |
| Original frozen member reconstruction | unavailable | False | habitatmech:GOLD.df1d688f27 | Original source-member workbook/dumps unavailable within the bounded ignored-inclusive search. Later source members do not reconstruct historical membership. |

## Scientific And Domain Assessments

### Source concept, ontology kind and strictly broader hierarchy

identity: concern. Targets: habitatmech:GOLD.df1d688f27.

The sole parent ENVO:03600010 denotes a membrane bioreactor apparatus. Under a water-material interpretation it is not broader than produced water. However, node 5505 is an intermediate source context with descendant 5506 Sludge, so it could instead classify a produced-water-treating MBR environment. There is no source-authored definition or direct member proving which extent was intended. Do not conflate this target with the Mine water or Petroleum reservoir produced-water records, nor import their members. ENVO:00002194 oil field production water is a candidate to investigate only after material identity is resolved.

### Frozen attestations, counts, generated status and histories

provenance: supported. Targets: habitatmech:GOLD.df1d688f27.

Exact source data row 1193, path Engineered &gt; Bioreactor &gt; MBR (Membrane bioreactor) &gt; Produced water, nodes gold.ecosystem:5505, organism_count=0. Decision data row 1234 is CLASS CONFIRM_UNGROUNDED. Full target equals seed.build_document; one source contributor, zero ITEM-reviewed contributors, no direct ontology parent and no exact mapping predicate. UNGROUNDED/SEEDED is correctly retained. Zero count and unit are omitted; this is not biological absence.

### Microbial habitat support without claim inflation

evidence: supported. Targets: habitatmech:GOLD.df1d688f27.

The primary MBR experiment distinguishes produced water from oil/gas wells, the reactor treating it and its microbial biomass. It supports a microbial treatment environment and the material/apparatus distinction, but is illustrative rather than an exact GOLD 5505 member. Salinity responses and community changes from that experiment are not universal target properties.

### Exact source member extent and MIxS-role boundaries

scope: unknown. Targets: habitatmech:GOLD.df1d688f27.

No exact-path Biosample, Organism or SequencingProject members in the complete October snapshot. Classification row 109 retains the longer path ending Produced water &gt; Sludge (5506); no terminal 5505 row occurs in the complete 2422-row classification sheet. That leaf-path export does not establish retirement of the intermediate context. Source occurrence does not make every member characteristic or make broad/local/medium roles interchangeable. No target MIxS parameter row is promoted to identity.

### Optional fields, evidence placement and ownership

completeness: supported. Targets: habitatmech:GOLD.df1d688f27.

All target content and history read. No authored definition, taxa, parameter, mechanism, discussion or dataset claim is emitted. Missing optional enrichment and CLASS status alone are not findings. No target causal overlay was found in ignored-inclusive search. Fixes belong to named maintained sources or overlays, never generated habitats/pages. Parent-record taxa and other produced-water paths were not inherited as target claims.

### Deterministic validity versus scientific evidence

schema: supported. Targets: habitatmech:GOLD.df1d688f27.

Target LinkML, six-target strict, corpus reproduction, ID-label and native review gates passed locally at unchanged inputs. Full native QC was verified in exact-base CI. Deterministic success does not settle the scientific findings or unresolved source extent.

## Findings

### F1: Produced-water material and produced-water treatment system remain conflated

major / open / provisional; issue key: gold-df1d688f27-material-versus-mbr-scope.

Resolve the intended extent of GOLD node 5505, including its Sludge descendant, from original membership or source documentation. If the target denotes water material, suppress only the ENVO:03600010 source-context contribution using the guarded GOLD parent exclusion. If it denotes a treatment-system class, support a qualified label/definition rather than deleting a valid apparatus parent. Do not invent a definition solely to remove the edge.

## Recommended Actions And Acceptance Checks

### ACT1

Resolve the intended extent of GOLD node 5505, including its Sludge descendant, from original membership or source documentation. If the target denotes water material, suppress only the ENVO:03600010 source-context contribution using the guarded GOLD parent exclusion. If it denotes a treatment-system class, support a qualified label/definition rather than deleting a valid apparatus parent. Do not invent a definition solely to remove the edge.

- Resolve only the exact source concept, retain verbatim path, source IDs, source-specific count units and conservative scientific status unless item-level evidence supports change.
- Document source conflicts and the actual adjudicating evidence; a missing field or label similarity alone cannot justify an identity, parent or member change.
- Preserve immutable reviews and append native history for maintained-input curation; add focused regression tests.
- Run applicable provenance, schema, strict, label correspondence, corpus reproduction and full QC/site/map gates after any authorized curation.
- Save an immutable successor with this stable issue key and exact predecessor reference before closing the finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/engineered/produced_water__123adb7f.yaml; Entire target YAML including history; entire immediate parent YAML | supports | The sole parent ENVO:03600010 denotes a membrane bioreactor apparatus. Under a water-material interpretation it is not broader than produced water. However, node 5505 is an intermediate source context with descendant 5506 Sludge, so it could instead classify a produced-water-treating MBR environment. There is no source-authored definition or direct member proving which extent was intended. Do not conflate this target with the Mine water or Petroleum reservoir produced-water records, nor import their members. ENVO:00002194 oil field production water is a candidate to investigate only after material identity is resolved. |
| E2 | data/raw/gold_ecosystem_paths.tsv; Data row 1193; curation/decisions.tsv data row 1234; full generated-document trace | supports | Exact source data row 1193, path Engineered &gt; Bioreactor &gt; MBR (Membrane bioreactor) &gt; Produced water, nodes gold.ecosystem:5505, organism_count=0. Decision data row 1234 is CLASS CONFIRM_UNGROUNDED. Full target equals seed.build_document; one source contributor, zero ITEM-reviewed contributors, no direct ontology parent and no exact mapping predicate. UNGROUNDED/SEEDED is correctly retained. Zero count and unit are omitted; this is not biological absence. |
| E3 | https://gold.jgi.doe.gov/download?mode=site_excel; Dated October 9 workbook; exact-path four-sheet census and source accession joins | partial | No exact-path Biosample, Organism or SequencingProject members in the complete October snapshot. Classification row 109 retains the longer path ending Produced water &gt; Sludge (5506); no terminal 5505 row occurs in the complete 2422-row classification sheet. That leaf-path export does not establish retirement of the intermediate context. Reused census on a freshly SHA256-verified source, not a new download or a new full-workbook scan. Complete rows including headers: Biosample 244951, Organism 532019, SequencingProject 636914, Study 63806. |
| E4 | curation; history; reviews/structured; reports/yaml_record_review; research/habitats; data/raw; build; /private/tmp; configured kg-microbe/data; Bounded ignored-inclusive target/source searches and complete structured source-table parses | context_only | No target-specific causal overlay was found. Earlier legacy reports or other-record references are leads, not new scientific review or predecessor findings for this target. No earlier native completed scientific target review was found by full structured bundle parsing. Original GOLD node/edge dumps and the August workbook were not recovered in the explicitly bounded source search. This is not machine-wide absence. |
| E5 | https://gold.jgi.doe.gov/download?mode=ecosystempaths; Complete 2422-row classification sheet; exact paths and all Produced water rows inspected | supports | No exact terminal path; row 109 is descendant 5506 with Sludge. Node 5505 remains in the frozen source inventory and as a contextual prefix, not proven obsolete. |
| R1 | https://gold.jgi.doe.gov/ecosystem_classification; Five-level classification explanation | supports | GOLD paths describe source surroundings and specific environmental features. Each contextual level requires scientific interpretation before being used as a strictly broader ontology parent. |
| V1 | https://github.com/CultureBotAI/HabitatMech/actions/runs/38016425124; Completed QC at exact unchanged base 2e30ed4df3b727ed4080b58603805a988b4b19f3; logs and run metadata inspected | supports | CI executed authoritative QC successfully: 656 passed, 3 skipped; 3208 strict-valid records, exact corpus reproduction, and all HabitatMech quality gates passed. This is verified CI execution at the same scientific base, not a new local full-QC run. |
| S1 | https://pubmed.ncbi.nlm.nih.gov/30235594/; PMID:30235594; DOI:10.1016/j.scitotenv.2018.07.386; complete abstract via Europe PMC core API | supports | Real produced water was treated in an MBR; the fluid, apparatus and biomass are distinct. No exact source membership or universal composition was established. |
| O1 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO:03600010; Active label, definition and obsolete flag; ENVO:00002194 also inspected | supports | The parent is a bioreactor with a membrane, not a water material. Oil field production water is active but lacks a textual definition in the inspected response; label proximity alone does not establish a mapping. |

## Limits And Additional Notes

- No exact direct source member or historical roster was recovered. Descendant Sludge context prevents a confident unconditional parent exclusion. The primary experiment is abstract-only and not linked to this source bin.
- Original frozen membership reconstruction is unavailable; later workbook evidence is a dated reused snapshot. Required deterministic checks passed in their documented scope, with full QC verified in exact-base CI and three tests skipped there.
- This review writes only a new immutable YAML/Markdown pair. No scientific source, generated record, history, page, GitHub issue or mapping status is changed. It makes no SSSOM/KGX readiness claim.
- Actual review began at 02:31:35Z, paused for publication-state verification, and resumed at 02:39:26Z without a scientific-input change. Access timestamps denote completed inspection, not download/publication dates.
- All 52 initial captured repository hashes remain unchanged. The October source snapshots were freshly SHA256-verified; the complete earlier census and parser were reused. Searches included ignored/hidden files within explicit bounds.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T024621Z-produced_water__123adb7f
kind: record
repository: culturebotai/HabitatMech
title: 'Scientific record review: Produced water (produced_water__123adb7f)'
started_at: '2026-10-10T02:31:35Z'
finished_at: '2026-10-10T02:46:21Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same continuing agent inspected source records, evidence and
    generated claims; no independent human or second-agent approval is claimed.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: The source path is reproducible and plausibly describes a microbial treatment
  environment, but the water label and apparatus parent leave a material-versus-treatment-system
  ambiguity. A provisional major finding requires source-level adjudication before
  either retaining the apparatus genus or excluding it. This is not an automatic correction
  based on a label.
source:
  git_revision: 2e30ed4df3b727ed4080b58603805a988b4b19f3
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
    sha256: 0da28df896b99166eff4fc193444df1d3e50afc66861b7ac91f7fe1f741cdcd1
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
  - path: data/habitats/engineered/industrial_waste_material.yaml
    sha256: 0d57cbfda093a70c21d801ea59f10959e09670e6c211a2ce4554296cf1132f85
    role: context
  - path: data/habitats/engineered/industrial_wastewater.yaml
    sha256: 07698df721a169cd55c2d1ce80027df8c8a3140536ba99eee312272887ce8768
    role: context
  - path: data/habitats/engineered/membrane_bioreactor.yaml
    sha256: 89d8964bce58cdeac9c2d3cc6db41e3cab4ef5ef6a6f2e312deaf115306c77fe
    role: context
  - path: data/habitats/engineered/mine_water.yaml
    sha256: c285eed1f2bc078931182954bb1f290d8e0a7c05cc5940fbac9509503ef6b38c
    role: context
  - path: data/habitats/engineered/nutrient_rich.yaml
    sha256: e722d3b49b5dbb4dfde7e2112c47a8752d2e33803ce612c33890d7cf1dbf08c7
    role: context
  - path: data/habitats/engineered/produced_water__123adb7f.yaml
    sha256: c6fb2b744303f124538e3047148380c739a366f45787e07a8cb385e1899a7a87
    role: target
  - path: data/habitats/engineered/produced_water__4b7c7f10.yaml
    sha256: 4b37e393fae66ff1930d74f03c7c3ff495ce4317baea2a907efc2afa4182e4b5
    role: context
  - path: data/habitats/engineered/produced_water__58649b5f.yaml
    sha256: 3ea34c87a81c1e9a227bcccce2888a26f5db7ed4b4fd7fb25f122c578b1b56ad
    role: context
  - path: data/habitats/engineered/pulp_and_paper_wastewater.yaml
    sha256: 2c6b31dc0f6d04cf05618f1b54b08ba6a0ee1fffb14e24c48011b072a3bf693a
    role: context
  - path: data/habitats/engineered/r2a_agar.yaml
    sha256: 53384072a3f8547c68d59a2d7ecb40bc654f68bda9ed19ab83252e084de6da5b
    role: context
  - path: data/habitats/engineered/radioactive_waste.yaml
    sha256: c1d6093e3d810ceb4c4b277c83909fc968f8fa84c2f511f82eba4e2f936a5d43
    role: context
  - path: data/habitats/terrestrial/oil_reservoir.yaml
    sha256: 091dd4b2be2cf7a26ad7c42451a8b60b1214aecab56bd3b7ac9219082aea1d9a
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
  description: Read-only scientific review of exactly one resolved generated HabitatRecord
    and all its contributing source claims.
  selection: Next individually resolved target in the continuing complete-corpus review;
    the 3208-record objective is unchanged, not replaced by this six-target working
    sequence.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.df1d688f27
  exclusions:
  - target: Other corpus records and full source-database validation
    reason: Parents/siblings and selected later source members are context. This review
      does not certify all records, every sample accession or all-record goal completion.
targets:
- target_id: habitatmech:GOLD.df1d688f27
  path: data/habitats/engineered/produced_water__123adb7f.yaml
  label: Produced water
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: source-concept grounding and review depth
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: authored definition and genus
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: guarded source-context parent exclusions
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: frozen GOLD source IDs, paths and counts
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: generated identity, parents, status and attestations
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: source inventory transformations
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: stable slug mapping
  - repository: culturebotai/HabitatMech
    path: data/raw/gold_path_biosamples.tsv
    role: source-submitted sample/path counts, not validated sample substrate identity
  - repository: culturebotai/HabitatMech
    path: data/raw/gold_studies.tsv
    role: study-to-source-path associations, not member-level substrate evidence
  - repository: culturebotai/HabitatMech
    path: scripts/extract_gold_biosamples.py
    role: reproducible source-path sample and study inventory extraction
checks:
- check_id: C1
  name: Native validate
  status: passed
  required: true
  summary: Executed 2026-10-10T02:32:53.416314+00:00 to 2026-10-10T02:32:56.277867+00:00,
    exit 0. No issues found
  target_ids:
  - habitatmech:GOLD.df1d688f27
  command: just validate data/habitats/engineered/produced_water__123adb7f.yaml
  exit_code: 0
- check_id: C2
  name: Native validate-strict
  status: passed
  required: true
  summary: Executed 2026-10-10T02:33:07.305687+00:00 to 2026-10-10T02:33:12.126028+00:00,
    exit 0.  Six-record closed-schema validation reported zero errors.
  target_ids:
  - habitatmech:GOLD.df1d688f27
  command: just validate-strict data/habitats/engineered/produced_water__123adb7f.yaml
    data/habitats/engineered/produced_water__4b7c7f10.yaml data/habitats/engineered/produced_water__58649b5f.yaml
    data/habitats/engineered/pulp_and_paper_wastewater.yaml data/habitats/engineered/r2a_agar.yaml
    data/habitats/engineered/radioactive_waste.yaml
  exit_code: 0
- check_id: C3
  name: Native verify-corpus
  status: passed
  required: true
  summary: "Executed 2026-10-10T02:33:12.126726+00:00 to 2026-10-10T02:33:26.893271+00:00,\
    \ exit 0. expected 3208 records, found 3208 on disk\n  missing:   0\n  extra:\
    \     0\n  differing: 0\n\ncorpus reproduces exactly from data/raw/"
  target_ids:
  - habitatmech:GOLD.df1d688f27
  command: just verify-corpus
  exit_code: 0
- check_id: C4
  name: Native validate-products
  status: passed
  required: true
  summary: "Executed 2026-10-10T02:33:26.893850+00:00 to 2026-10-10T02:34:11.792770+00:00,\
    \ exit 0. id↔label correspondence summary:\n          OK_CANONICAL: 1178\n   \
    \         OK_SYNONYM: 1\n          OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2057\n\
    \n✅ All id↔label pairs correspond."
  target_ids:
  - habitatmech:GOLD.df1d688f27
  command: just validate-products
  exit_code: 0
- check_id: C5
  name: Native review-check
  status: passed
  required: true
  summary: "Executed 2026-10-10T02:34:11.793358+00:00 to 2026-10-10T02:36:36.946542+00:00,\
    \ exit 0. {\n  \"repository\": \"culturebotai/HabitatMech\",\n  \"valid_reviews\"\
    : 88,\n  \"coverage\": \"declared_scopes_only\"\n}\n....                     \
    \                                                [100%]\n4 passed in 69.73s (0:01:09)"
  target_ids:
  - habitatmech:GOLD.df1d688f27
  command: just review-check
  exit_code: 0
- check_id: C7
  name: Full exact-base QC
  status: passed
  required: true
  summary: 'Completed CI at the captured Git base: 656 passed, 3 skipped, all native
    QC gates passed; run head and conclusion also fetched through gh run view --json.
    Three skipped tests remain disclosed.'
  target_ids:
  - habitatmech:GOLD.df1d688f27
  command: gh run view 38016425124 --log | rg '[0-9]+ passed|All HabitatMech quality
    gates|history records|files scanned|term-request table|differing'
  exit_code: 0
- check_id: C8
  name: Whole-target source trace
  status: passed
  required: true
  summary: All six generated documents equal seed.build_document. All raw/root-curation
    tables and path mappings parsed; current input hashes freshly verified unchanged.
  target_ids:
  - habitatmech:GOLD.df1d688f27
  command: uv run python /private/tmp/habitatmech-review-u-local.py
  exit_code: 0
- check_id: C9
  name: Dated workbook census revalidation
  status: passed
  required: true
  summary: Both hashes match the complete earlier census from /private/tmp/habitatmech-review-t-workbook.py,
    whose parser was inspected. This turn reuses the dated census; it does not claim
    a fresh bulk download/scan.
  target_ids:
  - habitatmech:GOLD.df1d688f27
  command: shasum -a 256 /private/tmp/habitatmech-20261009h-goldData.xlsx /private/tmp/habitatmech-review-n-ecosystems.xlsx
  exit_code: 0
- check_id: C10
  name: Exact ontology and selected external records
  status: passed
  required: false
  summary: Eight accession/project XML responses and six OLS term responses retrieved
    with exit 0. Relevant evidence is separately scoped per target; no whole-roster
    external verification claimed.
  target_ids:
  - habitatmech:GOLD.df1d688f27
  command: uv run python /private/tmp/habitatmech-review-u-external.py
  exit_code: 0
- check_id: C11
  name: Scientific baseline unchanged
  status: passed
  required: true
  summary: Exit 0. All 52 captured repository inputs independently SHA256-checked
    before authoring.
  target_ids:
  - habitatmech:GOLD.df1d688f27
  command: git diff --exit-code 2e30ed4df3b727ed4080b58603805a988b4b19f3 -- data src
    curation history scripts docs conf .claude justfile schema
  exit_code: 0
- check_id: C12
  name: Causal and expression applicability
  status: not_applicable
  required: false
  summary: Target has no causal edges, causal overlay, genes, regulators or transcriptomic
    claims. iModulonDB and target-specific causal validation are not applicable; complete
    baseline QC covers all maintained overlays.
  target_ids:
  - habitatmech:GOLD.df1d688f27
- check_id: C13
  name: Original frozen member reconstruction
  status: unavailable
  required: false
  summary: Original source-member workbook/dumps unavailable within the bounded ignored-inclusive
    search. Later source members do not reconstruct historical membership.
  target_ids:
  - habitatmech:GOLD.df1d688f27
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/engineered/produced_water__123adb7f.yaml
  locator: Entire target YAML including history; entire immediate parent YAML
  accessed_at: '2026-10-10T02:46:21Z'
  support: supports
  summary: The sole parent ENVO:03600010 denotes a membrane bioreactor apparatus.
    Under a water-material interpretation it is not broader than produced water. However,
    node 5505 is an intermediate source context with descendant 5506 Sludge, so it
    could instead classify a produced-water-treating MBR environment. There is no
    source-authored definition or direct member proving which extent was intended.
    Do not conflate this target with the Mine water or Petroleum reservoir produced-water
    records, nor import their members. ENVO:00002194 oil field production water is
    a candidate to investigate only after material identity is resolved.
- evidence_id: E2
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Data row 1193; curation/decisions.tsv data row 1234; full generated-document
    trace
  accessed_at: '2026-10-10T02:46:21Z'
  support: supports
  summary: Exact source data row 1193, path Engineered > Bioreactor > MBR (Membrane
    bioreactor) > Produced water, nodes gold.ecosystem:5505, organism_count=0. Decision
    data row 1234 is CLASS CONFIRM_UNGROUNDED. Full target equals seed.build_document;
    one source contributor, zero ITEM-reviewed contributors, no direct ontology parent
    and no exact mapping predicate. UNGROUNDED/SEEDED is correctly retained. Zero
    count and unit are omitted; this is not biological absence.
- evidence_id: E3
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=site_excel
  locator: Dated October 9 workbook; exact-path four-sheet census and source accession
    joins
  accessed_at: '2026-10-10T02:46:21Z'
  support: partial
  summary: 'No exact-path Biosample, Organism or SequencingProject members in the
    complete October snapshot. Classification row 109 retains the longer path ending
    Produced water > Sludge (5506); no terminal 5505 row occurs in the complete 2422-row
    classification sheet. That leaf-path export does not establish retirement of the
    intermediate context. Reused census on a freshly SHA256-verified source, not a
    new download or a new full-workbook scan. Complete rows including headers: Biosample
    244951, Organism 532019, SequencingProject 636914, Study 63806.'
  snapshot_sha256: 5f48b2f50fb2a9257754960a0f0e12dc6e8fa121e97c3e9f4497249e5fe6e439
- evidence_id: E4
  kind: search
  reference: curation; history; reviews/structured; reports/yaml_record_review; research/habitats;
    data/raw; build; /private/tmp; configured kg-microbe/data
  locator: Bounded ignored-inclusive target/source searches and complete structured
    source-table parses
  accessed_at: '2026-10-10T02:46:21Z'
  support: context_only
  summary: No target-specific causal overlay was found. Earlier legacy reports or
    other-record references are leads, not new scientific review or predecessor findings
    for this target. No earlier native completed scientific target review was found
    by full structured bundle parsing. Original GOLD node/edge dumps and the August
    workbook were not recovered in the explicitly bounded source search. This is not
    machine-wide absence.
  search_scope: rg --no-ignore --hidden -l for all six IDs, labels and slugs in curation/causal_graphs,
    history, reviews/structured, reports/yaml_record_review, research/habitats; all
    14 raw TSVs, seven root curation TSVs and PATHS.tsv parsed without ignore filtering.
    find data/raw build /private/tmp -maxdepth 2 for goldData, GOLD nodes/edges and
    PREGO files; recursive find in configured kg-microbe/data for those names. Current
    source workbook found; original frozen workbook/dumps not found in these bounds.
- evidence_id: E5
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=ecosystempaths
  locator: Complete 2422-row classification sheet; exact paths and all Produced water
    rows inspected
  accessed_at: '2026-10-10T02:46:21Z'
  support: supports
  summary: No exact terminal path; row 109 is descendant 5506 with Sludge. Node 5505
    remains in the frozen source inventory and as a contextual prefix, not proven
    obsolete.
  snapshot_sha256: 3933e5f0664915c1bbfa00212e17d013da360fb33dd52e509254050813135396
- evidence_id: R1
  kind: authority
  reference: https://gold.jgi.doe.gov/ecosystem_classification
  locator: Five-level classification explanation
  accessed_at: '2026-10-10T02:46:21Z'
  support: supports
  summary: GOLD paths describe source surroundings and specific environmental features.
    Each contextual level requires scientific interpretation before being used as
    a strictly broader ontology parent.
- evidence_id: V1
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38016425124
  locator: Completed QC at exact unchanged base 2e30ed4df3b727ed4080b58603805a988b4b19f3;
    logs and run metadata inspected
  accessed_at: '2026-10-10T02:46:21Z'
  support: supports
  summary: 'CI executed authoritative QC successfully: 656 passed, 3 skipped; 3208
    strict-valid records, exact corpus reproduction, and all HabitatMech quality gates
    passed. This is verified CI execution at the same scientific base, not a new local
    full-QC run.'
- evidence_id: S1
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/30235594/
  locator: PMID:30235594; DOI:10.1016/j.scitotenv.2018.07.386; complete abstract via
    Europe PMC core API
  accessed_at: '2026-10-10T02:46:21Z'
  support: supports
  summary: Real produced water was treated in an MBR; the fluid, apparatus and biomass
    are distinct. No exact source membership or universal composition was established.
- evidence_id: O1
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO:03600010
  locator: Active label, definition and obsolete flag; ENVO:00002194 also inspected
  accessed_at: '2026-10-10T02:46:21Z'
  support: supports
  summary: The parent is a bioreactor with a membrane, not a water material. Oil field
    production water is active but lacks a textual definition in the inspected response;
    label proximity alone does not establish a mapping.
assessments:
- assessment_id: A1
  area: identity
  topic: Source concept, ontology kind and strictly broader hierarchy
  outcome: concern
  summary: The sole parent ENVO:03600010 denotes a membrane bioreactor apparatus.
    Under a water-material interpretation it is not broader than produced water. However,
    node 5505 is an intermediate source context with descendant 5506 Sludge, so it
    could instead classify a produced-water-treating MBR environment. There is no
    source-authored definition or direct member proving which extent was intended.
    Do not conflate this target with the Mine water or Petroleum reservoir produced-water
    records, nor import their members. ENVO:00002194 oil field production water is
    a candidate to investigate only after material identity is resolved.
  target_ids:
  - habitatmech:GOLD.df1d688f27
  evidence_ids:
  - E1
  - E2
  - E5
  - R1
  - S1
  - O1
- assessment_id: A2
  area: provenance
  topic: Frozen attestations, counts, generated status and histories
  outcome: supported
  summary: Exact source data row 1193, path Engineered > Bioreactor > MBR (Membrane
    bioreactor) > Produced water, nodes gold.ecosystem:5505, organism_count=0. Decision
    data row 1234 is CLASS CONFIRM_UNGROUNDED. Full target equals seed.build_document;
    one source contributor, zero ITEM-reviewed contributors, no direct ontology parent
    and no exact mapping predicate. UNGROUNDED/SEEDED is correctly retained. Zero
    count and unit are omitted; this is not biological absence.
  target_ids:
  - habitatmech:GOLD.df1d688f27
  evidence_ids:
  - E1
  - E2
  dimensions:
  - name: native_status
    value: UNGROUNDED / SEEDED; CLASS-level lexical decision
    definition: Generator status, not scientific certification or habitat denial.
    evidence_ids:
    - E1
    - E2
  - name: frozen_organism_count
    value: '0'
    definition: Frozen source ORGANISM count; zero count/unit omitted; not a later
      BIOSAMPLE or species count.
    evidence_ids:
    - E2
- assessment_id: A3
  area: evidence
  topic: Microbial habitat support without claim inflation
  outcome: supported
  summary: The primary MBR experiment distinguishes produced water from oil/gas wells,
    the reactor treating it and its microbial biomass. It supports a microbial treatment
    environment and the material/apparatus distinction, but is illustrative rather
    than an exact GOLD 5505 member. Salinity responses and community changes from
    that experiment are not universal target properties.
  target_ids:
  - habitatmech:GOLD.df1d688f27
  evidence_ids:
  - E1
  - E3
  - S1
  - O1
- assessment_id: A4
  area: scope
  topic: Exact source member extent and MIxS-role boundaries
  outcome: unknown
  summary: No exact-path Biosample, Organism or SequencingProject members in the complete
    October snapshot. Classification row 109 retains the longer path ending Produced
    water > Sludge (5506); no terminal 5505 row occurs in the complete 2422-row classification
    sheet. That leaf-path export does not establish retirement of the intermediate
    context. Source occurrence does not make every member characteristic or make broad/local/medium
    roles interchangeable. No target MIxS parameter row is promoted to identity.
  target_ids:
  - habitatmech:GOLD.df1d688f27
  evidence_ids:
  - E2
  - E3
  - E5
  - S1
  - O1
- assessment_id: A5
  area: completeness
  topic: Optional fields, evidence placement and ownership
  outcome: supported
  summary: All target content and history read. No authored definition, taxa, parameter,
    mechanism, discussion or dataset claim is emitted. Missing optional enrichment
    and CLASS status alone are not findings. No target causal overlay was found in
    ignored-inclusive search. Fixes belong to named maintained sources or overlays,
    never generated habitats/pages. Parent-record taxa and other produced-water paths
    were not inherited as target claims.
  target_ids:
  - habitatmech:GOLD.df1d688f27
  evidence_ids:
  - E1
  - E2
  - E4
- assessment_id: A6
  area: schema
  topic: Deterministic validity versus scientific evidence
  outcome: supported
  summary: Target LinkML, six-target strict, corpus reproduction, ID-label and native
    review gates passed locally at unchanged inputs. Full native QC was verified in
    exact-base CI. Deterministic success does not settle the scientific findings or
    unresolved source extent.
  target_ids:
  - habitatmech:GOLD.df1d688f27
  evidence_ids:
  - E1
  - V1
findings:
- finding_id: F1
  issue_key: gold-df1d688f27-material-versus-mbr-scope
  severity: major
  certainty: provisional
  category: identity
  status: open
  title: Produced-water material and produced-water treatment system remain conflated
  description: Resolve the intended extent of GOLD node 5505, including its Sludge
    descendant, from original membership or source documentation. If the target denotes
    water material, suppress only the ENVO:03600010 source-context contribution using
    the guarded GOLD parent exclusion. If it denotes a treatment-system class, support
    a qualified label/definition rather than deleting a valid apparatus parent. Do
    not invent a definition solely to remove the edge.
  normalization_reason: The two plausible readings differ in ontological kind and
    validity of the sole parent, so the uncertainty affects the graph materially.
    The false material-to-apparatus relation is conditional, not claimed conclusively
    from the sparse source bin.
  native_severity: major
  rule_id: 'HabitatRecord checklist: strict broader parents, source scope, sampled
    material versus context and claim-level evidence; docs/CURATION.md'
  target_ids:
  - habitatmech:GOLD.df1d688f27
  field_paths:
  - label
  - parent_habitats
  evidence_ids:
  - E1
  - E2
  - E3
  - E5
  - R1
  - S1
  - O1
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: source-concept grounding and review depth
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: authored definition and genus
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: guarded source-context parent exclusions
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: generated identity, parents, status and attestations
actions:
- action_id: ACT1
  description: Resolve the intended extent of GOLD node 5505, including its Sludge
    descendant, from original membership or source documentation. If the target denotes
    water material, suppress only the ENVO:03600010 source-context contribution using
    the guarded GOLD parent exclusion. If it denotes a treatment-system class, support
    a qualified label/definition rather than deleting a valid apparatus parent. Do
    not invent a definition solely to remove the edge.
  finding_ids:
  - F1
  target_ids:
  - habitatmech:GOLD.df1d688f27
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: source-concept grounding and review depth
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: authored definition and genus
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: guarded source-context parent exclusions
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: generated identity, parents, status and attestations
  generator: 'Only during separately authorized curation: governed maintained-input
    change, just seed, inspect just seed-canary <identifier>, guarded regeneration
    and just render as applicable.'
  acceptance_checks:
  - Resolve only the exact source concept, retain verbatim path, source IDs, source-specific
    count units and conservative scientific status unless item-level evidence supports
    change.
  - Document source conflicts and the actual adjudicating evidence; a missing field
    or label similarity alone cannot justify an identity, parent or member change.
  - Preserve immutable reviews and append native history for maintained-input curation;
    add focused regression tests.
  - Run applicable provenance, schema, strict, label correspondence, corpus reproduction
    and full QC/site/map gates after any authorized curation.
  - Save an immutable successor with this stable issue key and exact predecessor reference
    before closing the finding.
limitations:
- No exact direct source member or historical roster was recovered. Descendant Sludge
  context prevents a confident unconditional parent exclusion. The primary experiment
  is abstract-only and not linked to this source bin.
- Original frozen membership reconstruction is unavailable; later workbook evidence
  is a dated reused snapshot. Required deterministic checks passed in their documented
  scope, with full QC verified in exact-base CI and three tests skipped there.
- This review writes only a new immutable YAML/Markdown pair. No scientific source,
  generated record, history, page, GitHub issue or mapping status is changed. It makes
  no SSSOM/KGX readiness claim.
notes:
- Actual review began at 02:31:35Z, paused for publication-state verification, and
  resumed at 02:39:26Z without a scientific-input change. Access timestamps denote
  completed inspection, not download/publication dates.
- All 52 initial captured repository hashes remain unchanged. The October source snapshots
  were freshly SHA256-verified; the complete earlier census and parser were reused.
  Searches included ignored/hidden files within explicit bounds.
tags:
- habitatmech
- engineered
- scientific-record-review
```
