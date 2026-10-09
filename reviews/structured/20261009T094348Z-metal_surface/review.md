# Metal surface: subway location is incorrectly asserted as a superclass

- Review: 20261009T094348Z-metal_surface
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-09T09:36:47Z
- Finished UTC: 2026-10-09T09:43:48Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Reviewed the complete subway Metal surface record. One confirmed major hierarchy finding: its sole parent denotes the enclosing subway environment, not a broader kind of metal surface. Existing issue282 already tracks this exact source concept. The mint, GOLD node/path, ungrounded seeded lifecycle and zero-organism omission reproduce. Later1022biosamples are separate provenance, not missing organism assertions. A read-only counterfactual demonstrates a target-only source-parent exclusion; no maintained input or generated record was changed.

## Scope And Provenance

Whole metal_surface.yaml and its sole source contribution; complete current Subway parent definition and provenance; related surface corrections only as implementation context.

Selection: PATHS.tsv:1522, habitatmech:GOLD.2082ed6ba7, node5462 and exact depth5 Subway &gt; Metal surface path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 966ccfe5a59b8d741f942f5d6924b4949d897430.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.2082ed6ba7 | data/habitats/engineered/metal_surface.yaml | generated | Metal surface |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current target and context capture | passed | True | habitatmech:GOLD.2082ed6ba7 | 45 inputs captured at966ccfe5a. Added exclusion-helper capture preserves all44earlier hashes. Target was read in full before assessment. |
| Target LinkML validation | passed | True | habitatmech:GOLD.2082ed6ba7 | No issues found. |
| Target closed-schema validation | passed | True | habitatmech:GOLD.2082ed6ba7 | One file, zero errors. |
| Fourteen-inventory exact-field scan | passed | True | habitatmech:GOLD.2082ed6ba7 | Exact path has zero aggregate organism counters, separately1022biosamples and studyGs0118444 across12paths. No direct target triad, taxon or parameter row. |
| Complete source resolution and reproduction | passed | True | habitatmech:GOLD.2082ed6ba7 | Default gold_unmatched retained by CLASS CONFIRM_UNGROUNDED; one source, zero reviewed. Full document equals disk. Parent ITEM decision rejects subway-train identity. Broad candidate printout was truncated; separate complete exact-match scan supplies absence evidence. |
| Complete committed-slice candidate scan | passed | False | habitatmech:GOLD.2082ed6ba7 | No exact metal-surface label or synonym in the entire committed ontology TSV. Metallic material and surface layer are neighboring concepts, not adopted identities or automatically added parents. No global absence claim. |
| Ignored-inclusive owner and prior-review search | passed | True | habitatmech:GOLD.2082ed6ba7 | Only the exact CLASS decision and path lock were found for the target in these roots. No target definition, exclusion, native history or earlier individual review found within the stated bounds. |
| Current GOLD source-node classification | passed | False | habitatmech:GOLD.2082ed6ba7 | Workbook row186 confirms node5462 and the full exact path. Non-fatal default-style warning only. |
| Initial issue read | failed | False | habitatmech:GOLD.2082ed6ba7 | Sandbox network connection failed; permitted public issue read subsequently succeeded. |
| Existing issue cross-check | passed | False | habitatmech:GOLD.2082ed6ba7 | Issue282 is OPEN and explicitly lists Metal surface/GOLD.2082ed6ba7/node5462 among six affected leaves. No new GitHub issue or mutation. |
| In-memory proposed repair isolation | passed | True | habitatmech:GOLD.2082ed6ba7 | Across3208documents, only this target changes. Sole source-context parent is removed and SOURCE_PARENT_EXCLUDED audit appended; every other target field and all other records remain equal. No file write or enacted curation. |
| Full corpus reproduction | passed | True | habitatmech:GOLD.2082ed6ba7 | 3208 expected and found; zero missing, extra or differing records. Shared unchanged-input check from this review session. |
| Native curation history | passed | True | habitatmech:GOLD.2082ed6ba7 | 217 histories valid. Shared unchanged-input check from this review session. |
| Raw inventory provenance | passed | True | habitatmech:GOLD.2082ed6ba7 | 14 committed inventories and two GOLD sources current. Shared unchanged-input check from this review session. |
| Parent, status and reference regressions | passed | True | habitatmech:GOLD.2082ed6ba7 | 6 passed, 33 deselected; deterministic integrity is not scientific proof. Shared unchanged-input check from this review session. |
| Exact-baseline full quality-gate receipt | passed | True | habitatmech:GOLD.2082ed6ba7 | Freshly queried successful run at captured 966ccfe5a: 639 passed, 3 skipped, four dedicated contract tests, 217 histories, 3208 records and all native gates. No fresh local full-QC run claimed. Shared unchanged-input check from this review session. |
| Exact-baseline ontology label receipt | passed | True | habitatmech:GOLD.2082ed6ba7 | Completed SUCCESS at captured revision; configured ontology coverage and exceptions are not proof of source semantics. Shared unchanged-input check from this review session. |
| Scientific-input equivalence | passed | True | habitatmech:GOLD.2082ed6ba7 | No differences from the checked base; only new review artifacts are written. Shared unchanged-input check from this review session. |
| Original study/member and material detail | unavailable | False | habitatmech:GOLD.2082ed6ba7 | GOLD node page was inaccessible; Gs0118444 rendered an error shell. Original metal composition, finish, coating and sample-level crosswalk were not recovered. |
| Molecular and causal adapters | not_applicable | False | habitatmech:GOLD.2082ed6ba7 | No target gene, regulator, transcriptomic or causal assertion and no target overlay found in the ignored-inclusive search. iModulonDB is not applicable. |

## Scientific And Domain Assessments

### Subway-associated metal surface

identity: supported. Targets: habitatmech:GOLD.2082ed6ba7.

Mint, source path, node, label and engineered category agree on a surface-associated source bin. No metal alloy, coating, object, station or cleaning regime is asserted.

### Retained source identity

grounding: supported. Targets: habitatmech:GOLD.2082ed6ba7.

The source remains minted and UNGROUNDED rather than claiming a nearby bulk-metal or transit-system term. CLASS status is honestly reflected by SEEDED and is not itself a major defect.

### Location incorrectly treated as superclass

graph: concern. Targets: habitatmech:GOLD.2082ed6ba7.

The sole parent denotes the enclosing subway environment. Being sampled on a metal surface within that environment supplies location context, not a strict broader class. This is the major finding.

### Different inventory units

quantity: supported. Targets: habitatmech:GOLD.2082ed6ba7.

Zero-organism omission and the later1022biosamples are compatible because they measure different source units and snapshots. Study-wide metadata cannot be assigned exclusively to the metal subset.

### Class-level decision and generated audit

consistency: supported. Targets: habitatmech:GOLD.2082ed6ba7.

One CLASS-confirmed source yields SEEDED, preserving the confirmation and seed history. A hierarchy-only fix need not promote identity review status.

### No unsupported optional enrichment

completeness: supported. Targets: habitatmech:GOLD.2082ed6ba7.

No target-specific taxon, parameter or triad rows in the complete direct raw scan. Missing alloy composition or original-study access is a limitation, not a license to populate mechanisms or characteristic taxa.

### Guarded source-only exclusion

ownership: supported. Targets: habitatmech:GOLD.2082ed6ba7.

Existing maintained exclusion table can remove this source contribution without changing the mint, raw provenance or unrelated records; verified by an in-memory counterfactual.

### Deterministic correctness versus semantics

schema: supported. Targets: habitatmech:GOLD.2082ed6ba7.

Target shape and source reproduction pass. The defect resides in the scientific meaning of an otherwise reproducible edge.

## Findings

### F1: Metal surface is falsely made a kind of the enclosing subway environment

major / open / confirmed; issue key: gold-2082ed6ba7-subway-context-parent.

parent_habitats asserts habitatmech:GOLD.961229841c as a strictly broader class of this localized metal surface. The maintained parent definition denotes an environment bounded by whole transit structures, and the source path locates the surface inside it. This is a location contribution, not an is-a genus; no independent ontology or target-definition evidence supplies the edge. Existing issue282 already identifies this exact source concept.

## Recommended Actions And Acceptance Checks

### A1

In a separately authorized curation change, add the guarded exclusion for sourceGOLD.2082ed6ba7, exact Engineered &gt; Built environment &gt; City &gt; Subway &gt; Metal surface path, and parentGOLD.961229841c. Use the existing table; do not redefine Subway, add an unsupported replacement genus, or fabricate a term-request definition merely to suppress this edge.

- Whole-corpus before/after comparison changes only the target parent list and appended SOURCE_PARENT_EXCLUDED event for this fix. Preserve all other record fields and earlier events.
- Keep source node5462, full path, mint, source label, count/unit omissions, absent mapping predicate and UNGROUNDED/SEEDED identity lifecycle. Preserve1022BIOSAMPLE provenance separately; do not transfer study-wide biology.
- Add a regression mirroring the proven in-memory isolation; stale source path or changed parent must be rejected. Do not alter siblings by inference.
- Append native curation history only during the authorized fix and pass schema/strict, corpus, provenance, history, configured labels, fullQC and applicable generated-site/map checks.
- Record any resolution in a new linked immutable review. Close only the metal-surface portion of issue282; other leaves require their own evidence and verification.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/habitats/engineered/metal_surface.yaml; Whole record, sole parent and two history events | supports | Source-specific Metal surface under Subway, UNGROUNDED/SEEDED; no count/unit or mapping predicate emitted; no authored definition or biological claim. |
| source | data/raw/gold_ecosystem_paths.tsv; Row1256, exact path, depth5 and node5462 | supports | One node; all organism/study/biosample/total counters zero in this aggregate. Source path identifies the localized material surface, not the whole enclosing transit environment. |
| samples | data/raw/gold_path_biosamples.tsv; Row33; gold_studies.tsv:1093; complete exact-field scan of14TSVs | supports | 1022BIOSAMPLE observations for the exact path in the later source inventory. Gs0118444 spans12paths, including other subway surfaces and unrelated source categories. Neither1022 nor the whole study is an organism count or metal-specific biological characterization. |
| parent | curation/term_requests.tsv; Row75; full current subway.yaml; parent decision1577 | refutes | Maintained parent defines the environment bounded by stations, tunnels, trains and other enclosed transit structures. A localized metal surface in this environment is not a subtype of that enclosing system. The parent itself rejects subway-train identity and replaces the earlier City context edge. |
| resolution | src/habitatmech/seed.py; Full-index resolution and whole build_document equality; target decision280 | supports | CLASS confirmation preserves minted identity with no exact mapping predicate, zero reviewed contributors and SEEDED status. The sole bad parent is introduced by GOLD prefix hierarchy, not an ontology subclass or target definition. |
| gold | https://gold.jgi.doe.gov/download?mode=ecosystempaths; site data row186; exact5462/Engineered/Built environment/City/Subway/Metal surface | supports | Current public classification confirms the historical node/path spelling. Workbook84174bytes, SHA2563933e5f0664915c1bbfa00212e17d013da360fb33dd52e509254050813135396; it does not characterize the specimens. |
| study | https://link.springer.com/article/10.1186/s40168-019-0772-9; Gohli et al.; inspected abstract and Methods, especially Surface sampling lines107-120 | supports | The study distinguishes station air from localized kiosk, railing and bench surfaces. This supports surface-versus-enclosing-environment semantics, not a metal composition assignment or a GOLD study crosswalk. No taxa, effects, sample numbers or figure claims are transferred. |
| issue | https://github.com/CultureBotAI/HabitatMech/issues/282; Fresh all-field issue read; OPEN; exact Metal surface entry | supports | Existing issue already identifies this source-context hierarchy defect. Its older suggested term-request approach predates the maintained guarded-exclusion mechanism; no new definition is required solely to remove the false edge. Other affected leaves remain outside this review. |
| precedent | curation/gold_parent_exclusions.tsv; Rows28 and54; tests/test_gold_parent_exclusions.py:558-636; exclusion helper | context_only | Existing concrete and bench exclusions show the guarded input owner and isolation pattern. This target's independent source/parent semantics establish its finding; sibling fixes alone are not evidence that all surfaces should change. |
| counterfactual | src/habitatmech/curate/gold_parent_exclusions.py; Read-only mock of load_gold_parent_exclusions during full-corpus builds | supports | Adding only the exact metal-source/path/subway-parent triple in memory changes one record's parent list and appended audit event. No scientific curation was written. |
| candidates | data/raw/ontology_terms.tsv; Complete exact normalized label/synonym scan and bounded candidate projection | context_only | No exact metal surface match in this slice. ENVO:01001069 metallic material describes bulk material; ENVO:00010504 surface layer is a possible genus for future assessment, not the subway-qualified identity. Anthropogenic environment is also broader, not an exact surface match. |
| scope | curation; Exact ignored-inclusive target identifier, node, label and slug search | context_only | No target-specific definition, exclusion, native session history, causal overlay or earlier individual report was recovered within the named roots. Neighboring report excerpts were context, not whole-record reassessments. |
| unavailable | https://gold.jgi.doe.gov/study?id=Gs0118444; Inspected rendered error shell; ecosystem5462 browser retrieval failed | unknown | Study/member details remain unavailable; no inference of invalid IDs or ecological absence follows. DOI resolver and PMC retrieval also failed, but the original publisher's methods were accessible. |
| gates | https://github.com/CultureBotAI/HabitatMech/actions/runs/37910149298; Exact966ccfe5a baseline and label run37910149233; fresh local shared checks | supports | Deterministic gates pass while retaining the semantic parent defect. Passing validation does not make source context an is-a relation. |

## Limits And Additional Notes

- One exact target reviewed; full3208-record completion remains unproven.
- Original source specimens and Gs0118444 metadata are unavailable. No study crosswalk, metal alloy, coating, treatment, taxa, health effect or causal mechanism is endorsed.
- The source is a surface-associated habitat bin; surface layer, bulk metal and anthropogenic environment remain candidate distinctions, not automatic replacement identities. No global ontology absence claim.
- Parent and sibling material is contextual; their whole-record findings and the remaining portions of issue282 are not closed.
- Current fullQC/label receipts at the exact unchanged base and shared fresh local checks were reused; no fresh local fullQC. Three native tests are skipped.
- No scientific-input change, native status/history mutation, GitHub mutation, publication or SSSOM/KGX readiness assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261009T094348Z-metal_surface
kind: record
repository: CultureBotAI/HabitatMech
title: 'Metal surface: subway location is incorrectly asserted as a superclass'
started_at: '2026-10-09T09:36:47Z'
finished_at: '2026-10-09T09:43:48Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent continuing the corpus review; fresh target assessment
    and in-memory reproduction, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Reviewed the complete subway Metal surface record. One confirmed major hierarchy
  finding: its sole parent denotes the enclosing subway environment, not a broader
  kind of metal surface. Existing issue282 already tracks this exact source concept.
  The mint, GOLD node/path, ungrounded seeded lifecycle and zero-organism omission
  reproduce. Later1022biosamples are separate provenance, not missing organism assertions.
  A read-only counterfactual demonstrates a target-only source-parent exclusion; no
  maintained input or generated record was changed.'
source:
  git_revision: 966ccfe5a59b8d741f942f5d6924b4949d897430
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
  - path: curation/decisions.tsv
    sha256: 0602cca13e6495da256a6f1cfd5897462f73f9739a729447862017d93c148efd
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: cc4da2e7e5e8750e6c023683014aa37a909230280f231eec5be7c71795340312
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: c741b54ba1c39872afaf090422d274a123e308f15eba480639c702eddab60a3d
    role: context
  - path: curation/term_requests.tsv
    sha256: 3efdac153ccd40f518458a9dc5360e09dd660c3a42fbd06bfc57f3b2f707ece7
    role: context
  - path: curation/term_requests/envo_robot_template.tsv
    sha256: 6968010617eb36a4e326b04f629fe7b4242efd47a5656f4d8ffec3242b1e9b9f
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
  - path: data/habitats/engineered/metal_surface.yaml
    sha256: 54505befa6500b37f4159f4ddf2814854546b80404fd187834e9b3358313b7c7
    role: target
  - path: data/habitats/engineered/subway.yaml
    sha256: 7f918d820e1959b3e94d4634dc328ddb65adf8aaa500fc1293f846a65f25d133
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
  - path: history/mappings/subway/2026-09-10T022534Z-claude-code-8e3889.yaml
    sha256: cbe67f3552b5b7d1d2f1b5a2d71cebca7addbec398bf1eeb0b8a0f0baaae395b
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20261007T055028Z-bench_surface.md
    sha256: 7ca5e2c7dc8f31f406fa6abb2bd30806b61994e7a44ded36ef238bbb0277cd1e
    role: context
  - path: reports/yaml_record_review/20261008T031853Z-concrete_surface.md
    sha256: f6034c488990c23e118a3b03d0ec7c38d016afb5afb6fc7d84ba2be87fc375fd
    role: context
  - path: research/habitats/engineered/subway-habitatmech-gold-961229841c-deep-research-claude_code.md
    sha256: 5e8316af2431a1d65e94bfdedd55e9cdb7d8b2024899dfa74882f17282f16139
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/habitatmech/curate/gold_parent_exclusions.py
    sha256: 044d8277509a9b1f6e4f2d7ea1fb82319b41e09ffef7788738a0f4ed0d0b63af
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 52d2a22309a1f4a10728a663560bb4d918346c292221fd34139b99b4159d3fe5
    role: context
  - path: src/habitatmech/seed.py
    sha256: 92adf631fa099120a497ff7001473e659347d23ac9b418f04cd341ddad5d2a89
    role: context
  - path: tests/test_gold_parent_exclusions.py
    sha256: c561499386bd092f37f5901ad2ca985c1bd620211113800762ed432554c39f38
    role: context
targets:
- target_id: habitatmech:GOLD.2082ed6ba7
  path: data/habitats/engineered/metal_surface.yaml
  label: Metal surface
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Exact GOLD.2082ed6ba7 source concept grounding and item review.
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Guarded source-only context-parent exclusion if warranted.
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Source-specific definition, true genus and label if justified.
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Exact subway metal-surface path, node and counts.
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Generated mapping, source hierarchy, lifecycle and parent exclusion application.
scope:
  description: Whole metal_surface.yaml and its sole source contribution; complete
    current Subway parent definition and provenance; related surface corrections only
    as implementation context.
  selection: PATHS.tsv:1522, habitatmech:GOLD.2082ed6ba7, node5462 and exact depth5
    Subway > Metal surface path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.2082ed6ba7
  exclusions:
  - target: Subway parent and five sibling surface records
    reason: No new whole-record verdict or closure for these records; issue282 is
      broader than this finding.
checks:
- check_id: capture
  name: Current target and context capture
  status: passed
  required: true
  summary: 45 inputs captured at966ccfe5a. Added exclusion-helper capture preserves
    all44earlier hashes. Target was read in full before assessment.
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
  command: env UV_CACHE_DIR=build/uv-cache uv run python scripts/record_review.py
    inspect --targets /private/tmp/habitatmech-metal-surface-targets-20261009T093647Z.json
    --input CLAUDE.md --input justfile --input docs/CURATION.md --input docs/HARMONIZATION.md
    --input docs/RESEARCH.md --input docs/record-review-profile.md --input docs/record-reviews.md
    --input .claude/skills/review-yaml-record/SKILL.md --input .claude/skills/curate-yaml-record/references/review-checklist.md
    --input schema/record_review.yaml --input src/habitatmech/schema/habitatmech.yaml
    --input src/habitatmech/seed.py --input curation/decisions.tsv --input curation/gold_parent_exclusions.tsv
    --input curation/term_requests.tsv --input curation/term_requests_excluded.tsv
    --input data/habitats/PATHS.tsv --input data/habitats/RETIRED.tsv --input data/raw/ontology_terms.tsv
    --input data/raw/ontology_subclass_edges.tsv --input data/raw/isolation_source_groundings.tsv
    --input data/raw/gold_ecosystem_paths.tsv --input data/raw/gold_path_biosamples.tsv
    --input data/raw/gold_path_triads.tsv --input data/raw/gold_studies.tsv --input
    data/raw/prego_habitats.tsv --input data/raw/prego_habitat_taxa.tsv --input data/raw/bacdive_isolation_sources.tsv
    --input data/raw/bacdive_source_taxa.tsv --input data/raw/madin_habitats.tsv --input
    data/raw/madin_habitat_taxa.tsv --input data/raw/environment_parameters.tsv --input
    data/raw/MANIFEST.yaml --input data/raw/GOLD_MANIFEST.yaml --input research/habitats/engineered/subway-habitatmech-gold-961229841c-deep-research-claude_code.md
    --input tests/test_gold_parent_exclusions.py --input curation/term_requests/envo_robot_template.tsv
    --input reports/yaml_record_review/20261008T031853Z-concrete_surface.md --input
    history/mappings/subway/2026-09-10T022534Z-claude-code-8e3889.yaml --input reports/yaml_record_review/20261007T055028Z-bench_surface.md
    --input curation/definition_source_label_exclusions.tsv --input conf/id_label_targets.yaml
    --input data/habitats/engineered/subway.yaml --input src/habitatmech/curate/gold_parent_exclusions.py
  exit_code: 0
- check_id: schema
  name: Target LinkML validation
  status: passed
  required: true
  summary: No issues found.
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
  command: env UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/metal_surface.yaml
  exit_code: 0
- check_id: strict
  name: Target closed-schema validation
  status: passed
  required: true
  summary: One file, zero errors.
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
  command: env UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/metal_surface.yaml
  exit_code: 0
- check_id: raw
  name: Fourteen-inventory exact-field scan
  status: passed
  required: true
  summary: Exact path has zero aggregate organism counters, separately1022biosamples
    and studyGs0118444 across12paths. No direct target triad, taxon or parameter row.
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
  command: "env UV_CACHE_DIR=build/uv-cache uv run python - <<'PY'\nfrom pathlib import\
    \ Path\nimport csv,json\nneedles={'habitatmech:GOLD.2082ed6ba7','Engineered >\
    \ Built environment > City > Subway > Metal surface','gold.ecosystem:5462'}\n\
    for path in sorted(Path('data/raw').glob('*.tsv')):\n    hits=[]\n    with path.open()\
    \ as h:\n        for n,row in enumerate(csv.DictReader(h,delimiter='\\t'),2):\n\
    \            values=[v for x in row.values() for v in (x if isinstance(x,list)\
    \ else [x]) if v]\n            if any(v in needles or needles.intersection(v.split('|'))\
    \ for v in values):hits.append({'line':n,'row':row})\n    print(path.name,json.dumps(hits))\n\
    PY"
  exit_code: 0
- check_id: route
  name: Complete source resolution and reproduction
  status: passed
  required: true
  summary: Default gold_unmatched retained by CLASS CONFIRM_UNGROUNDED; one source,
    zero reviewed. Full document equals disk. Parent ITEM decision rejects subway-train
    identity. Broad candidate printout was truncated; separate complete exact-match
    scan supplies absence evidence.
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
  command: "env UV_CACHE_DIR=build/uv-cache uv run python - <<'PY'\nfrom habitatmech\
    \ import seed as s\nfrom dataclasses import asdict\nfrom pathlib import Path\n\
    import json,yaml\nrows=s.read_tsv('gold_ecosystem_paths.tsv'); ont=s.OntologyIndex(s.read_tsv('ontology_terms.tsv'),s.read_tsv('ontology_subclass_edges.tsv'));d=s.load_decisions(s.DECISIONS_PATH);mapping={}\n\
    for row in s.read_tsv('isolation_source_groundings.tsv'):\n    for key in (s.norm_label(row['subject_label']),s.norm_label(row['subject_label_normalized'])):\n\
    \        if key:mapping.setdefault(key,row)\nfor path in ['Engineered > Built\
    \ environment > City > Subway > Metal surface','Engineered > Built environment\
    \ > City > Subway']:\n    row=next(r for r in rows if r['canonical_path']==path);\
    \ ident=s.mint('GOLD',path)\n    auto=s.resolve_gold(row,ont,mapping,s.leaf_claimants(rows),s.composed_claimants(rows))\n\
    \    print(json.dumps({'path':path,'mint':ident,'automatic':asdict(auto),'final':asdict(s.apply_decision(auto,ident,d))}))\n\
    c=next(c for c in s.build_corpus().concepts if c.identifier=='habitatmech:GOLD.2082ed6ba7')\n\
    assert s.build_document(c)==yaml.safe_load(Path('data/habitats/engineered/metal_surface.yaml').read_text())\n\
    print('Whole document equal; sources',c.source_concepts,'reviewed',c.reviewed_sources)\n\
    for ident,row in ont.terms.items():\n    if any(word in row['label'].lower() for\
    \ word in ['metal','surface']):print('CANDIDATE',ident,json.dumps(row))\nPY"
  exit_code: 0
- check_id: candidates
  name: Complete committed-slice candidate scan
  status: passed
  required: false
  summary: No exact metal-surface label or synonym in the entire committed ontology
    TSV. Metallic material and surface layer are neighboring concepts, not adopted
    identities or automatically added parents. No global absence claim.
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
  command: "env UV_CACHE_DIR=build/uv-cache uv run python - <<'PY'\nimport csv,json\n\
    from habitatmech.seed import norm_label\nwith open('data/raw/ontology_terms.tsv')\
    \ as h:\n    rows=list(csv.DictReader(h,delimiter='\\t'))\nexact=[r for r in rows\
    \ if any(norm_label(v)=='metal surface' for v in [r['label'],*r['synonyms'].split('|')])]\n\
    print('Exact metal-surface label/synonym matches in complete committed slice:',json.dumps(exact))\n\
    for r in rows:\n    if r['label'] in {'metallic material','surface layer','anthropogenic\
    \ environment'}:print(json.dumps(r))\nPY"
  exit_code: 0
- check_id: search
  name: Ignored-inclusive owner and prior-review search
  status: passed
  required: true
  summary: Only the exact CLASS decision and path lock were found for the target in
    these roots. No target definition, exclusion, native history or earlier individual
    review found within the stated bounds.
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
  command: rg --no-ignore --hidden -n -i 'GOLD.2082ed6ba7|metal_surface|metal surface|gold.ecosystem:5462'
    curation history research conf tests docs reviews reports/yaml_record_review data/habitats/PATHS.tsv
    data/habitats/RETIRED.tsv
  exit_code: 0
- check_id: gold
  name: Current GOLD source-node classification
  status: passed
  required: false
  summary: Workbook row186 confirms node5462 and the full exact path. Non-fatal default-style
    warning only.
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
  command: "env UV_CACHE_DIR=build/uv-cache uv run python - <<'PY'\nimport urllib.request,io,hashlib\n\
    from openpyxl import load_workbook\nu='https://gold.jgi.doe.gov/download?mode=ecosystempaths';b=urllib.request.urlopen(u,timeout=45).read();w=load_workbook(io.BytesIO(b),read_only=True,data_only=True);s=w['site\
    \ data'];s.reset_dimensions()\nprint('WORKBOOK',len(b),hashlib.sha256(b).hexdigest())\n\
    for n,r in enumerate(s.iter_rows(values_only=True),1):\n    if 'Metal surface'\
    \ in r:print(n,r)\nPY"
  exit_code: 0
- check_id: issue_initial
  name: Initial issue read
  status: failed
  required: false
  summary: Sandbox network connection failed; permitted public issue read subsequently
    succeeded.
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
  command: gh issue view 282 --json number,title,state,body,url
  exit_code: 1
- check_id: issue
  name: Existing issue cross-check
  status: passed
  required: false
  summary: Issue282 is OPEN and explicitly lists Metal surface/GOLD.2082ed6ba7/node5462
    among six affected leaves. No new GitHub issue or mutation.
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
  command: gh issue view 282 --json number,title,state,body,url
  exit_code: 0
- check_id: counterfactual
  name: In-memory proposed repair isolation
  status: passed
  required: true
  summary: Across3208documents, only this target changes. Sole source-context parent
    is removed and SOURCE_PARENT_EXCLUDED audit appended; every other target field
    and all other records remain equal. No file write or enacted curation.
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
  command: "env UV_CACHE_DIR=build/uv-cache uv run python - <<'PY'\nfrom dataclasses\
    \ import replace\nfrom unittest.mock import patch\nfrom habitatmech import seed\
    \ as s\nidentifier='habitatmech:GOLD.2082ed6ba7';parent='habitatmech:GOLD.961229841c';path='Engineered\
    \ > Built environment > City > Subway > Metal surface'\nbefore={c.identifier:s.build_document(c)\
    \ for c in s.build_corpus().concepts}\nexclusions=s.load_gold_parent_exclusions(s.GOLD_PARENT_EXCLUSIONS_PATH)\n\
    assert identifier not in exclusions\nexclusions[identifier]=replace(exclusions['habitatmech:GOLD.d4694eed69'],identifier=identifier,source_path=path,date='2026-10-09',curator='codex-gpt-5',notes='Read-only\
    \ counterfactual: a localized metal surface is not a kind of its enclosing subway\
    \ environment. No curation is written.')\nwith patch.object(s,'load_gold_parent_exclusions',return_value=exclusions):\n\
    \    after={c.identifier:s.build_document(c) for c in s.build_corpus().concepts}\n\
    assert before.keys()==after.keys()\nchanged={k for k in before if before[k]!=after[k]};assert\
    \ changed=={identifier},changed\nold,new=before[identifier],after[identifier]\n\
    assert old['parent_habitats']==[parent] and 'parent_habitats' not in new\nassert\
    \ new['curation_history'][:-1]==old['curation_history']\nassert new['curation_history'][-1]['action']=='SOURCE_PARENT_EXCLUDED'\n\
    for field in (old.keys()|new.keys())-{'parent_habitats','curation_history'}:assert\
    \ old.get(field)==new.get(field),field\nprint('In-memory only:',len(before),'documents;',changed,'alone\
    \ changes. Only parent_habitats and appended SOURCE_PARENT_EXCLUDED audit differ.\
    \ No file written.')\nPY"
  exit_code: 0
- check_id: corpus
  name: Full corpus reproduction
  status: passed
  required: true
  summary: 3208 expected and found; zero missing, extra or differing records. Shared
    unchanged-input check from this review session.
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
  command: env UV_CACHE_DIR=build/uv-cache just verify-corpus
  exit_code: 0
- check_id: history
  name: Native curation history
  status: passed
  required: true
  summary: 217 histories valid. Shared unchanged-input check from this review session.
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
  command: env UV_CACHE_DIR=build/uv-cache just validate-history
  exit_code: 0
- check_id: provenance
  name: Raw inventory provenance
  status: passed
  required: true
  summary: 14 committed inventories and two GOLD sources current. Shared unchanged-input
    check from this review session.
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
  command: env UV_CACHE_DIR=build/uv-cache just provenance-check
  exit_code: 0
- check_id: integrity
  name: Parent, status and reference regressions
  status: passed
  required: true
  summary: 6 passed, 33 deselected; deterministic integrity is not scientific proof.
    Shared unchanged-input check from this review session.
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
  command: env UV_CACHE_DIR=build/uv-cache uv run pytest -q tests/test_corpus_integrity.py
    -k 'parent or reviewed_records or history or causal_edges_reference'
  exit_code: 0
- check_id: ci_qc
  name: Exact-baseline full quality-gate receipt
  status: passed
  required: true
  summary: 'Freshly queried successful run at captured 966ccfe5a: 639 passed, 3 skipped,
    four dedicated contract tests, 217 histories, 3208 records and all native gates.
    No fresh local full-QC run claimed. Shared unchanged-input check from this review
    session.'
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
  command: gh run view 37910149298 --log | rg 'passed|skipped|history record|files
    scanned|corpus reproduces|All HabitatMech quality gates'
  exit_code: 0
- check_id: ci_labels
  name: Exact-baseline ontology label receipt
  status: passed
  required: true
  summary: Completed SUCCESS at captured revision; configured ontology coverage and
    exceptions are not proof of source semantics. Shared unchanged-input check from
    this review session.
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
  command: gh run view 37910149233 --json status,conclusion,headSha,url
  exit_code: 0
- check_id: unchanged
  name: Scientific-input equivalence
  status: passed
  required: true
  summary: No differences from the checked base; only new review artifacts are written.
    Shared unchanged-input check from this review session.
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
  command: git diff --exit-code 966ccfe5a59b8d741f942f5d6924b4949d897430 -- data curation
    src scripts tests docs conf schema CLAUDE.md justfile
  exit_code: 0
- check_id: source_detail
  name: Original study/member and material detail
  status: unavailable
  required: false
  summary: GOLD node page was inaccessible; Gs0118444 rendered an error shell. Original
    metal composition, finish, coating and sample-level crosswalk were not recovered.
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
- check_id: molecular
  name: Molecular and causal adapters
  status: not_applicable
  required: false
  summary: No target gene, regulator, transcriptomic or causal assertion and no target
    overlay found in the ignored-inclusive search. iModulonDB is not applicable.
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
evidence:
- evidence_id: record
  kind: record_content
  reference: data/habitats/engineered/metal_surface.yaml
  locator: Whole record, sole parent and two history events
  accessed_at: '2026-10-09T09:42:03Z'
  support: supports
  summary: Source-specific Metal surface under Subway, UNGROUNDED/SEEDED; no count/unit
    or mapping predicate emitted; no authored definition or biological claim.
- evidence_id: source
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Row1256, exact path, depth5 and node5462
  accessed_at: '2026-10-09T09:42:03Z'
  support: supports
  summary: One node; all organism/study/biosample/total counters zero in this aggregate.
    Source path identifies the localized material surface, not the whole enclosing
    transit environment.
- evidence_id: samples
  kind: database
  reference: data/raw/gold_path_biosamples.tsv
  locator: Row33; gold_studies.tsv:1093; complete exact-field scan of14TSVs
  accessed_at: '2026-10-09T09:42:03Z'
  support: supports
  summary: 1022BIOSAMPLE observations for the exact path in the later source inventory.
    Gs0118444 spans12paths, including other subway surfaces and unrelated source categories.
    Neither1022 nor the whole study is an organism count or metal-specific biological
    characterization.
- evidence_id: parent
  kind: record_content
  reference: curation/term_requests.tsv
  locator: Row75; full current subway.yaml; parent decision1577
  accessed_at: '2026-10-09T09:42:03Z'
  support: refutes
  summary: Maintained parent defines the environment bounded by stations, tunnels,
    trains and other enclosed transit structures. A localized metal surface in this
    environment is not a subtype of that enclosing system. The parent itself rejects
    subway-train identity and replaces the earlier City context edge.
- evidence_id: resolution
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Full-index resolution and whole build_document equality; target decision280
  accessed_at: '2026-10-09T09:42:03Z'
  support: supports
  summary: CLASS confirmation preserves minted identity with no exact mapping predicate,
    zero reviewed contributors and SEEDED status. The sole bad parent is introduced
    by GOLD prefix hierarchy, not an ontology subclass or target definition.
- evidence_id: gold
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=ecosystempaths
  locator: site data row186; exact5462/Engineered/Built environment/City/Subway/Metal
    surface
  accessed_at: '2026-10-09T09:42:03Z'
  support: supports
  summary: Current public classification confirms the historical node/path spelling.
    Workbook84174bytes, SHA2563933e5f0664915c1bbfa00212e17d013da360fb33dd52e509254050813135396;
    it does not characterize the specimens.
- evidence_id: study
  kind: primary_source
  reference: https://link.springer.com/article/10.1186/s40168-019-0772-9
  locator: Gohli et al.; inspected abstract and Methods, especially Surface sampling
    lines107-120
  accessed_at: '2026-10-09T09:42:03Z'
  support: supports
  summary: The study distinguishes station air from localized kiosk, railing and bench
    surfaces. This supports surface-versus-enclosing-environment semantics, not a
    metal composition assignment or a GOLD study crosswalk. No taxa, effects, sample
    numbers or figure claims are transferred.
- evidence_id: issue
  kind: prior_review
  reference: https://github.com/CultureBotAI/HabitatMech/issues/282
  locator: Fresh all-field issue read; OPEN; exact Metal surface entry
  accessed_at: '2026-10-09T09:42:03Z'
  support: supports
  summary: Existing issue already identifies this source-context hierarchy defect.
    Its older suggested term-request approach predates the maintained guarded-exclusion
    mechanism; no new definition is required solely to remove the false edge. Other
    affected leaves remain outside this review.
- evidence_id: precedent
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: Rows28 and54; tests/test_gold_parent_exclusions.py:558-636; exclusion helper
  accessed_at: '2026-10-09T09:42:03Z'
  support: context_only
  summary: Existing concrete and bench exclusions show the guarded input owner and
    isolation pattern. This target's independent source/parent semantics establish
    its finding; sibling fixes alone are not evidence that all surfaces should change.
- evidence_id: counterfactual
  kind: validation
  reference: src/habitatmech/curate/gold_parent_exclusions.py
  locator: Read-only mock of load_gold_parent_exclusions during full-corpus builds
  accessed_at: '2026-10-09T09:42:03Z'
  support: supports
  summary: Adding only the exact metal-source/path/subway-parent triple in memory
    changes one record's parent list and appended audit event. No scientific curation
    was written.
- evidence_id: candidates
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Complete exact normalized label/synonym scan and bounded candidate projection
  accessed_at: '2026-10-09T09:42:03Z'
  support: context_only
  summary: No exact metal surface match in this slice. ENVO:01001069 metallic material
    describes bulk material; ENVO:00010504 surface layer is a possible genus for future
    assessment, not the subway-qualified identity. Anthropogenic environment is also
    broader, not an exact surface match.
- evidence_id: scope
  kind: search
  reference: curation
  locator: Exact ignored-inclusive target identifier, node, label and slug search
  accessed_at: '2026-10-09T09:42:03Z'
  support: context_only
  summary: No target-specific definition, exclusion, native session history, causal
    overlay or earlier individual report was recovered within the named roots. Neighboring
    report excerpts were context, not whole-record reassessments.
  search_scope: rg --no-ignore --hidden across curation, history, research, conf,
    tests, docs, reviews, reports/yaml_record_review and PATHS/RETIRED, querying GOLD.2082ed6ba7,
    metal_surface, Metal surface and gold.ecosystem:5462. All ignored and hidden files
    in these bounds included. Separate parent-ID search found the two sibling reports
    and Subway curation.
- evidence_id: unavailable
  kind: database
  reference: https://gold.jgi.doe.gov/study?id=Gs0118444
  locator: Inspected rendered error shell; ecosystem5462 browser retrieval failed
  accessed_at: '2026-10-09T09:42:03Z'
  support: unknown
  summary: Study/member details remain unavailable; no inference of invalid IDs or
    ecological absence follows. DOI resolver and PMC retrieval also failed, but the
    original publisher's methods were accessible.
- evidence_id: gates
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/37910149298
  locator: Exact966ccfe5a baseline and label run37910149233; fresh local shared checks
  accessed_at: '2026-10-09T09:42:03Z'
  support: supports
  summary: Deterministic gates pass while retaining the semantic parent defect. Passing
    validation does not make source context an is-a relation.
assessments:
- assessment_id: identity
  area: identity
  topic: Subway-associated metal surface
  outcome: supported
  summary: Mint, source path, node, label and engineered category agree on a surface-associated
    source bin. No metal alloy, coating, object, station or cleaning regime is asserted.
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
  evidence_ids:
  - record
  - source
  - gold
- assessment_id: grounding
  area: grounding
  topic: Retained source identity
  outcome: supported
  summary: The source remains minted and UNGROUNDED rather than claiming a nearby
    bulk-metal or transit-system term. CLASS status is honestly reflected by SEEDED
    and is not itself a major defect.
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
  evidence_ids:
  - resolution
  - candidates
- assessment_id: hierarchy
  area: graph
  topic: Location incorrectly treated as superclass
  outcome: concern
  summary: The sole parent denotes the enclosing subway environment. Being sampled
    on a metal surface within that environment supplies location context, not a strict
    broader class. This is the major finding.
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
  evidence_ids:
  - record
  - parent
  - source
  - study
  - issue
- assessment_id: counts
  area: quantity
  topic: Different inventory units
  outcome: supported
  summary: Zero-organism omission and the later1022biosamples are compatible because
    they measure different source units and snapshots. Study-wide metadata cannot
    be assigned exclusively to the metal subset.
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
  evidence_ids:
  - source
  - samples
- assessment_id: lifecycle
  area: consistency
  topic: Class-level decision and generated audit
  outcome: supported
  summary: One CLASS-confirmed source yields SEEDED, preserving the confirmation and
    seed history. A hierarchy-only fix need not promote identity review status.
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
  evidence_ids:
  - record
  - resolution
- assessment_id: completeness
  area: completeness
  topic: No unsupported optional enrichment
  outcome: supported
  summary: No target-specific taxon, parameter or triad rows in the complete direct
    raw scan. Missing alloy composition or original-study access is a limitation,
    not a license to populate mechanisms or characteristic taxa.
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
  evidence_ids:
  - samples
  - unavailable
  - scope
- assessment_id: repair
  area: ownership
  topic: Guarded source-only exclusion
  outcome: supported
  summary: Existing maintained exclusion table can remove this source contribution
    without changing the mint, raw provenance or unrelated records; verified by an
    in-memory counterfactual.
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
  evidence_ids:
  - precedent
  - counterfactual
- assessment_id: validation
  area: schema
  topic: Deterministic correctness versus semantics
  outcome: supported
  summary: Target shape and source reproduction pass. The defect resides in the scientific
    meaning of an otherwise reproducible edge.
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
  evidence_ids:
  - gates
  - resolution
findings:
- finding_id: F1
  issue_key: gold-2082ed6ba7-subway-context-parent
  category: graph
  severity: major
  status: open
  certainty: confirmed
  title: Metal surface is falsely made a kind of the enclosing subway environment
  description: parent_habitats asserts habitatmech:GOLD.961229841c as a strictly broader
    class of this localized metal surface. The maintained parent definition denotes
    an environment bounded by whole transit structures, and the source path locates
    the surface inside it. This is a location contribution, not an is-a genus; no
    independent ontology or target-definition evidence supplies the edge. Existing
    issue282 already identifies this exact source concept.
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
  field_paths:
  - parent_habitats
  evidence_ids:
  - record
  - parent
  - source
  - study
  - resolution
  - issue
  - counterfactual
  rule_id: 'CLAUDE.md semantic invariant: parent_habitats means strictly broader for
    every contributing route'
  native_severity: major
  normalization_reason: Confirmed false hierarchy edge affects scientific graph meaning,
    not style or missing optional fields. Target identity itself remains the intended
    source bin.
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Guarded source-only context-parent exclusion if warranted.
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Generated mapping, source hierarchy, lifecycle and parent exclusion application.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/282
actions:
- action_id: A1
  description: In a separately authorized curation change, add the guarded exclusion
    for sourceGOLD.2082ed6ba7, exact Engineered > Built environment > City > Subway
    > Metal surface path, and parentGOLD.961229841c. Use the existing table; do not
    redefine Subway, add an unsupported replacement genus, or fabricate a term-request
    definition merely to suppress this edge.
  finding_ids:
  - F1
  target_ids:
  - habitatmech:GOLD.2082ed6ba7
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Guarded source-only context-parent exclusion if warranted.
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Generated mapping, source hierarchy, lifecycle and parent exclusion application.
  generator: Dry seed, inspected target canary, then validated generation through
    the existing seeder; no generation performed by this review.
  acceptance_checks:
  - Whole-corpus before/after comparison changes only the target parent list and appended
    SOURCE_PARENT_EXCLUDED event for this fix. Preserve all other record fields and
    earlier events.
  - Keep source node5462, full path, mint, source label, count/unit omissions, absent
    mapping predicate and UNGROUNDED/SEEDED identity lifecycle. Preserve1022BIOSAMPLE
    provenance separately; do not transfer study-wide biology.
  - Add a regression mirroring the proven in-memory isolation; stale source path or
    changed parent must be rejected. Do not alter siblings by inference.
  - Append native curation history only during the authorized fix and pass schema/strict,
    corpus, provenance, history, configured labels, fullQC and applicable generated-site/map
    checks.
  - Record any resolution in a new linked immutable review. Close only the metal-surface
    portion of issue282; other leaves require their own evidence and verification.
limitations:
- One exact target reviewed; full3208-record completion remains unproven.
- Original source specimens and Gs0118444 metadata are unavailable. No study crosswalk,
  metal alloy, coating, treatment, taxa, health effect or causal mechanism is endorsed.
- The source is a surface-associated habitat bin; surface layer, bulk metal and anthropogenic
  environment remain candidate distinctions, not automatic replacement identities.
  No global ontology absence claim.
- Parent and sibling material is contextual; their whole-record findings and the remaining
  portions of issue282 are not closed.
- Current fullQC/label receipts at the exact unchanged base and shared fresh local
  checks were reused; no fresh local fullQC. Three native tests are skipped.
- No scientific-input change, native status/history mutation, GitHub mutation, publication
  or SSSOM/KGX readiness assessment.
tags:
- habitat
- engineered
- metal-surface
- GOLD
- source-parent
```
