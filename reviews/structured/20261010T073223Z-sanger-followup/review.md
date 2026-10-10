# Scoped publication follow-up: Sanger

- Review: 20261010T073223Z-sanger-followup
- Repository: culturebotai/HabitatMech
- Started UTC: 2026-10-10T06:55:39Z
- Finished UTC: 2026-10-10T07:32:23Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Resolved the computational read-mixture identity with an ITEM NOT_APPLICABLE decision. The exact Modeled &gt; Simulated communities (sequence read mixture) &gt; Sanger path and the linked 113-isolate-genome benchmark establish a sequence-data artifact, not a physical habitat. The citable mint, source grouping, nodes, complete path and count omission remain; no sibling is reclassified.

## Scope And Provenance

Verify the named scientific correction and preserve other record claims; explicitly inspect changed mapping semantics.

Selection: Successor to the exact prior individual review; not newly covered scientific-record count.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 45f4455ecbd528303690b4dad66bf17edf32b692.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.68f3852be5 | data/habitats/engineered/sanger.yaml | generated | Sanger |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Target LinkML | passed | True | habitatmech:GOLD.68f3852be5 | No issues found; fresh local execution. |
| Strict target validation | passed | True | habitatmech:GOLD.68f3852be5 | Six files validated; zero errors. |
| Focused curation regressions | passed | True | habitatmech:GOLD.68f3852be5 | 50 passed in 104.59s. |
| Exact corpus reproduction | passed | True | habitatmech:GOLD.68f3852be5 | 3208 expected/found; zero missing, extra or differing. |
| Ontology labels | passed | True | habitatmech:GOLD.68f3852be5 | 1178 canonical, one synonym and five exceptions; 2057 rows without adapters remain outside the automated gate. |
| Session history | passed | True | habitatmech:GOLD.68f3852be5 | 244 valid append-only session records; actual actor attribution checked. |
| Authoritative local QC | passed | True | habitatmech:GOLD.68f3852be5 | 660 passed, 3 skipped in 964.33s (0:16:04); all quality gates passed. |
| Generated site | passed | True | habitatmech:GOLD.68f3852be5 | uv run python scripts/render_pages.py --check<br>rendered 3208 habitat pages, 252 redirect stubs, 8 categories, 114 term requests -&gt; /var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/tmpwuxnlan3/site<br>pages/ is in step with the corpus |
| Semantic-map artifact/cache | passed | True | habitatmech:GOLD.68f3852be5 | Complete source-bound artifact passed; exact local/remote inputs and 3208 finite unique points separately verified. |
| Immutable predecessors | passed | True | habitatmech:GOLD.68f3852be5 | Native inspect preceded follow-up assessment. Recapture verifies every previous input hash or the exact PMID-to-PubMed-URL correction in two notes/records via structured CSV/YAML comparison. No other captured input changed. All 236 prior review files are byte-identical. |
| Causal and expression-source applicability | not_applicable | False | habitatmech:GOLD.68f3852be5 | No new causal mechanism, gene, regulator or expression-module claim is introduced. Contextual papers do not import such claims into the record. |

## Scientific And Domain Assessments

### Disposition of the reviewed correction

identity: supported. Targets: habitatmech:GOLD.68f3852be5.

Resolved the computational read-mixture identity with an ITEM NOT_APPLICABLE decision. The exact Modeled &gt; Simulated communities (sequence read mixture) &gt; Sanger path and the linked 113-isolate-genome benchmark establish a sequence-data artifact, not a physical habitat. The citable mint, source grouping, nodes, complete path and count omission remain; no sibling is reclassified.

### Preservation and generated products

consistency: supported. Targets: habitatmech:GOLD.68f3852be5.

Only the six intended records change; four exclusions preserve every non-parent/history claim. The two ITEM decisions derive native status/history, retaining source identities and all source counts. The semantic map and pages are regenerated and verified.

### Remaining uncertainty and contract boundaries

provenance: unknown. Targets: habitatmech:GOLD.68f3852be5.

Original bounded source-membership and evidence limitations remain. Preserving a claim is not a new independent confirmation of all its ecology.

## Findings

### F1: Classify the Sanger sequence-read bin as non-habitat

major / resolved / confirmed; issue key: gold-68f3852be5-sanger-sequence-artifact-not-habitat.

The record is still CLASS/UNGROUNDED, while the exact source path and joined primary benchmark establish an in-silico read-mixture concept. It must not be treated as a missing environmental ontology identity or a habitat term-request candidate.

Disposition: Resolved the computational read-mixture identity with an ITEM NOT_APPLICABLE decision. The exact Modeled &gt; Simulated communities (sequence read mixture) &gt; Sanger path and the linked 113-isolate-genome benchmark establish a sequence-data artifact, not a physical habitat. The citable mint, source grouping, nodes, complete path and count omission remain; no sibling is reclassified.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/engineered/sanger.yaml; Complete regenerated YAML and field-by-field comparison with 486d97f799fe3df7d8933b6c9a5dab69e48f7f59 | supports | Resolved the computational read-mixture identity with an ITEM NOT_APPLICABLE decision. The exact Modeled &gt; Simulated communities (sequence read mixture) &gt; Sanger path and the linked 113-isolate-genome benchmark establish a sequence-data artifact, not a physical habitat. The citable mint, source grouping, nodes, complete path and count omission remain; no sibling is reclassified. |
| E2 | docs/CURATION.md; Strictly broader parents, source identity, decision and review-depth rules | supports | Source context is not subsumption; keep exact identity separate from broader placement. NOT_APPLICABLE concerns the source concept itself. Status is derived from maintained ITEM decisions, not from saving a review. |
| E3 | reviews/structured/20261010T063411Z-sanger/review.yaml; Original F1, inspected evidence and limitations; prior immutable YAML/Markdown pair | context_only | This successor resolves only the original finding. Original source-membership, optional-content and evidence limitations remain. This is not a fresh exhaustive literature or source-member census. |
| M1 | curation/decisions.tsv; Exact source-ID row and append-only history/mappings/sanger/ | supports | The maintained row records the verified source scope, actual agent, date, issue and evidence. Guarded seeding reproduces the intended correction without manual generated-record edits. |
| V1 | scripts/run_qc.py; Fresh local just qc execution; session gate-6 log | supports | All authoritative quality gates passed: 660 passed, 3 skipped in 964.33s (0:16:04). Includes provenance, tests, history, strict schema, causal overlays, curation floor, exact corpus reproduction and generated-site/redirect/term-request checks. |
| V2 | tests/test_sand_and_seating_review_fixes.py; Two full-corpus before/after tests plus existing guarded-exclusion regressions | supports | 50 focused tests passed. Four exclusions affect only parent/history fields of four documents; two ITEM decisions affect only their two resolved records. Source IDs, paths, unlike count units and unrelated claims are preserved. |
| V3 | https://github.com/CultureBotAI/HabitatMech/actions/runs/38032549518; Successful locked Linux map build, local exact input comparison, source-bound cache/bundle check and finite-point check | supports | Five changed texts encoded; the repeated canary reused all five and the full pass reused all 3208. Local and remote inputs byte-match SHA256 21f001aa3d07c2e510c906aa2160f5d91cceefc3e9d46bf72e350bc26bf153c0. All 3208 plotted identifiers are unique with finite coordinates, with unchanged encoder/projection settings. |
| P1 | https://www.nature.com/articles/nmeth1043; Primary abstract, DOI:10.1038/nmeth1043; PMID:17468765 | supports | The authors construct three simulated metagenomes by combining sequencing reads from 113 isolate genomes. This supports a computational artifact interpretation of the exact sequence-read-mixture source path, not a physical mock community. |

## Limits And Additional Notes

- Scoped self-review, not independent approval or an exhaustive new source census.
- Three skipped tests and 2057 label rows without adapters remain outside automated verification.
- No corpus-wide scientific approval or SSSOM/KGX compatibility conclusion follows; shared issue #1398 remains open.
- Generated decision events reflect current maintained decisions. Superseded CLASS decisions remain in Git and immutable predecessor reviews; append-only session history records this curation.
- Initial CI 38032874915 found two valid PMID citations misclassified as ontology identifiers by the existing decision-note guard (issue #1868). The known-failed local QC run was stopped. Citation spelling was corrected to exact PubMed URLs without weakening the guard; the targeted failing test and both scoped regressions then passed (3 tests). New correction history was appended. Semantic inputs remained byte-identical; the final local full QC recorded here is a fresh rerun after that fix.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T073223Z-sanger-followup
kind: record
repository: culturebotai/HabitatMech
title: 'Scoped publication follow-up: Sanger'
started_at: '2026-10-10T06:55:39Z'
finished_at: '2026-10-10T07:32:23Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same continuing agent independently checks source claims within
    this session; no separate reviewer or human approval is claimed.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Resolved the computational read-mixture identity with an ITEM NOT_APPLICABLE
  decision. The exact Modeled > Simulated communities (sequence read mixture) > Sanger
  path and the linked 113-isolate-genome benchmark establish a sequence-data artifact,
  not a physical habitat. The citable mint, source grouping, nodes, complete path
  and count omission remain; no sibling is reclassified.
source:
  git_revision: 45f4455ecbd528303690b4dad66bf17edf32b692
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/SKILL.md
    sha256: c279e6d24969c0c9f0cf4f486bfde70a118762b4af3b706f20eb152710a15dd9
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: d429c8bb74f521df9a77a90b216a44fc6959ee28efb1fa17a93582536caa8bce
    role: context
  - path: CLAUDE.md
    sha256: 98d95f910ff5160bc5b2ff572766785519dacdba487700bebaa6dbf96d071fd9
    role: context
  - path: curation/decisions.tsv
    sha256: 46811ec0aae5819874fb46a998b4f745580739234017cebb43ce2f6b23ead5c7
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 443e2452852be844f238efe513fd584fb8ad6421b3c344066e08686e6c4d670c
    role: context
  - path: curation/term_requests.tsv
    sha256: 9977e384b79128d6e89c85f28e35c77d29644d503dea6d53c12628599e33f7f3
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: b59b9e800a918135e3915145d4d8098bb48dcea36a312b3004c594a57d221ae9
    role: context
  - path: data/habitats/engineered/sanger.yaml
    sha256: b2c2441b4f033b1f232add483eabb8a24e6a73b8330f83d0f4da6394e8732699
    role: target
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
  - path: data/raw/ontology_subclass_edges.tsv
    sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
    role: context
  - path: data/raw/ontology_terms.tsv
    sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
    role: context
  - path: docs/CURATION.md
    sha256: 36df8306394c06c352b73e0bf7b47a2858784cedac7389a24d0b78f593ece646
    role: context
  - path: docs/HARMONIZATION.md
    sha256: ee39d3cd29115ee14f5e7386169c76c47d471ebdc2502c008c49d30fb44918f1
    role: context
  - path: docs/record-review-profile.md
    sha256: f7aa39ee762d94f1902d9f08f328cb897bc543e4e226057eb4770d24bfcc6eb5
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/mappings/sanger/2026-10-10T065305Z-codex-gpt-5-a4d7a5.yaml
    sha256: 5152520b510858441a606aec48c4c5ee170b2daca4518b71744cfffa37e99653
    role: context
  - path: history/mappings/sanger/2026-10-10T070923Z-codex-gpt-5-969ac8.yaml
    sha256: b5f00e4b522dc9f36710e4459969ecd39b6ce9653d20bd767de5da744c0aa1bc
    role: context
  - path: reviews/structured/20261010T063411Z-sanger/review.md
    sha256: 815f3888e755df53cc7c9d33d7d214f29c8b70477e5a43af1cf60842b4199f2f
    role: context
  - path: reviews/structured/20261010T063411Z-sanger/review.yaml
    sha256: c579938ba773356b2f0c854f70381f61713072fbdb6de20da31306773873d202
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 52d2a22309a1f4a10728a663560bb4d918346c292221fd34139b99b4159d3fe5
    role: context
  - path: src/habitatmech/seed.py
    sha256: 92adf631fa099120a497ff7001473e659347d23ac9b418f04cd341ddad5d2a89
    role: context
  - path: tests/test_sand_and_seating_review_fixes.py
    sha256: 8e74a4c1a52b42cdd915b201a8c80a754a0a578e47d5c271b9cb6844b919ab6a
    role: context
targets:
- target_id: habitatmech:GOLD.68f3852be5
  path: data/habitats/engineered/sanger.yaml
  label: Sanger
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
scope:
  description: Verify the named scientific correction and preserve other record claims;
    explicitly inspect changed mapping semantics.
  selection: Successor to the exact prior individual review; not newly covered scientific-record
    count.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.68f3852be5
  exclusions:
  - target: Unchanged source membership and unrelated records
    reason: No new full source census or comprehensive literature re-review is claimed.
checks:
- check_id: C1
  name: Target LinkML
  command: just validate data/habitats/engineered/sanger.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.68f3852be5
  summary: No issues found; fresh local execution.
- check_id: C2
  name: Strict target validation
  command: just validate-strict data/habitats/engineered/sand_filter.yaml data/habitats/engineered/sand_microcosm.yaml
    data/habitats/engineered/sandstone.yaml data/habitats/engineered/sanger.yaml data/habitats/engineered/seat_surface.yaml
    data/habitats/engineered/seat_surface__a1cb78f8.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.68f3852be5
  summary: Six files validated; zero errors.
- check_id: C3
  name: Focused curation regressions
  command: uv run pytest -q tests/test_sand_and_seating_review_fixes.py tests/test_gold_parent_exclusions.py
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.68f3852be5
  summary: 50 passed in 104.59s.
- check_id: C4
  name: Exact corpus reproduction
  command: just verify-corpus
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.68f3852be5
  summary: 3208 expected/found; zero missing, extra or differing.
- check_id: C5
  name: Ontology labels
  command: just validate-products
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.68f3852be5
  summary: 1178 canonical, one synonym and five exceptions; 2057 rows without adapters
    remain outside the automated gate.
- check_id: C6
  name: Session history
  command: just validate-history
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.68f3852be5
  summary: 244 valid append-only session records; actual actor attribution checked.
- check_id: C7
  name: Authoritative local QC
  command: just qc
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.68f3852be5
  summary: 660 passed, 3 skipped in 964.33s (0:16:04); all quality gates passed.
- check_id: C8
  name: Generated site
  command: just render-check
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.68f3852be5
  summary: 'uv run python scripts/render_pages.py --check

    rendered 3208 habitat pages, 252 redirect stubs, 8 categories, 114 term requests
    -> /var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/tmpwuxnlan3/site

    pages/ is in step with the corpus'
- check_id: C9
  name: Semantic-map artifact/cache
  command: uv run python scripts/embedding_pipeline.py check --output build/pr1861-map-download/data/text_map
    --input build/text-map/pr1861-inputs.jsonl --cache build/pr1861-map-download/build/text-map/vectors.sqlite
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.68f3852be5
  summary: Complete source-bound artifact passed; exact local/remote inputs and 3208
    finite unique points separately verified.
- check_id: C10
  name: Immutable predecessors
  command: uv run python /private/tmp/habitatmech-pr1861-capture.py
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.68f3852be5
  summary: Native inspect preceded follow-up assessment. Recapture verifies every
    previous input hash or the exact PMID-to-PubMed-URL correction in two notes/records
    via structured CSV/YAML comparison. No other captured input changed. All 236 prior
    review files are byte-identical.
- check_id: C11
  name: Causal and expression-source applicability
  status: not_applicable
  required: false
  target_ids:
  - habitatmech:GOLD.68f3852be5
  summary: No new causal mechanism, gene, regulator or expression-module claim is
    introduced. Contextual papers do not import such claims into the record.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/engineered/sanger.yaml
  locator: Complete regenerated YAML and field-by-field comparison with 486d97f799fe3df7d8933b6c9a5dab69e48f7f59
  accessed_at: '2026-10-10T07:32:23Z'
  support: supports
  summary: Resolved the computational read-mixture identity with an ITEM NOT_APPLICABLE
    decision. The exact Modeled > Simulated communities (sequence read mixture) >
    Sanger path and the linked 113-isolate-genome benchmark establish a sequence-data
    artifact, not a physical habitat. The citable mint, source grouping, nodes, complete
    path and count omission remain; no sibling is reclassified.
- evidence_id: E2
  kind: authority
  reference: docs/CURATION.md
  locator: Strictly broader parents, source identity, decision and review-depth rules
  accessed_at: '2026-10-10T07:32:23Z'
  support: supports
  summary: Source context is not subsumption; keep exact identity separate from broader
    placement. NOT_APPLICABLE concerns the source concept itself. Status is derived
    from maintained ITEM decisions, not from saving a review.
- evidence_id: E3
  kind: prior_review
  reference: reviews/structured/20261010T063411Z-sanger/review.yaml
  locator: Original F1, inspected evidence and limitations; prior immutable YAML/Markdown
    pair
  accessed_at: '2026-10-10T07:32:23Z'
  support: context_only
  summary: This successor resolves only the original finding. Original source-membership,
    optional-content and evidence limitations remain. This is not a fresh exhaustive
    literature or source-member census.
- evidence_id: M1
  kind: record_content
  reference: curation/decisions.tsv
  locator: Exact source-ID row and append-only history/mappings/sanger/
  accessed_at: '2026-10-10T07:32:23Z'
  support: supports
  summary: The maintained row records the verified source scope, actual agent, date,
    issue and evidence. Guarded seeding reproduces the intended correction without
    manual generated-record edits.
- evidence_id: V1
  kind: validation
  reference: scripts/run_qc.py
  locator: Fresh local just qc execution; session gate-6 log
  accessed_at: '2026-10-10T07:32:23Z'
  support: supports
  summary: 'All authoritative quality gates passed: 660 passed, 3 skipped in 964.33s
    (0:16:04). Includes provenance, tests, history, strict schema, causal overlays,
    curation floor, exact corpus reproduction and generated-site/redirect/term-request
    checks.'
- evidence_id: V2
  kind: validation
  reference: tests/test_sand_and_seating_review_fixes.py
  locator: Two full-corpus before/after tests plus existing guarded-exclusion regressions
  accessed_at: '2026-10-10T07:32:23Z'
  support: supports
  summary: 50 focused tests passed. Four exclusions affect only parent/history fields
    of four documents; two ITEM decisions affect only their two resolved records.
    Source IDs, paths, unlike count units and unrelated claims are preserved.
- evidence_id: V3
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38032549518
  locator: Successful locked Linux map build, local exact input comparison, source-bound
    cache/bundle check and finite-point check
  accessed_at: '2026-10-10T07:32:23Z'
  support: supports
  summary: Five changed texts encoded; the repeated canary reused all five and the
    full pass reused all 3208. Local and remote inputs byte-match SHA256 21f001aa3d07c2e510c906aa2160f5d91cceefc3e9d46bf72e350bc26bf153c0.
    All 3208 plotted identifiers are unique with finite coordinates, with unchanged
    encoder/projection settings.
- evidence_id: P1
  kind: primary_source
  reference: https://www.nature.com/articles/nmeth1043
  locator: Primary abstract, DOI:10.1038/nmeth1043; PMID:17468765
  accessed_at: '2026-10-10T07:32:23Z'
  support: supports
  summary: The authors construct three simulated metagenomes by combining sequencing
    reads from 113 isolate genomes. This supports a computational artifact interpretation
    of the exact sequence-read-mixture source path, not a physical mock community.
assessments:
- assessment_id: A1
  area: identity
  topic: Disposition of the reviewed correction
  outcome: supported
  summary: Resolved the computational read-mixture identity with an ITEM NOT_APPLICABLE
    decision. The exact Modeled > Simulated communities (sequence read mixture) >
    Sanger path and the linked 113-isolate-genome benchmark establish a sequence-data
    artifact, not a physical habitat. The citable mint, source grouping, nodes, complete
    path and count omission remain; no sibling is reclassified.
  target_ids:
  - habitatmech:GOLD.68f3852be5
  evidence_ids:
  - E1
  - E2
  - E3
  - M1
  - P1
- assessment_id: A2
  area: consistency
  topic: Preservation and generated products
  outcome: supported
  summary: Only the six intended records change; four exclusions preserve every non-parent/history
    claim. The two ITEM decisions derive native status/history, retaining source identities
    and all source counts. The semantic map and pages are regenerated and verified.
  target_ids:
  - habitatmech:GOLD.68f3852be5
  evidence_ids:
  - E1
  - M1
  - V1
  - V2
  - V3
- assessment_id: A3
  area: provenance
  topic: Remaining uncertainty and contract boundaries
  outcome: unknown
  summary: Original bounded source-membership and evidence limitations remain. Preserving
    a claim is not a new independent confirmation of all its ecology.
  target_ids:
  - habitatmech:GOLD.68f3852be5
  evidence_ids:
  - E3
findings:
- finding_id: F1
  issue_key: gold-68f3852be5-sanger-sequence-artifact-not-habitat
  category: identity
  severity: major
  status: resolved
  certainty: confirmed
  title: Classify the Sanger sequence-read bin as non-habitat
  description: The record is still CLASS/UNGROUNDED, while the exact source path and
    joined primary benchmark establish an in-silico read-mixture concept. It must
    not be treated as a missing environmental ontology identity or a habitat term-request
    candidate.
  target_ids:
  - habitatmech:GOLD.68f3852be5
  field_paths:
  - grounding_status
  - mapping_status
  - curation_history
  evidence_ids:
  - E1
  - E2
  - E3
  - M1
  - P1
  - V1
  - V2
  rule_id: HabitatMech:non-habitat-artifacts
  native_severity: major
  normalization_reason: Material entity-type or hierarchy error, or missing supported
    ontology relationship; target and source record are resolved, so not classified
    as an ambiguous-target blocker.
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; generated habitat YAML is read-only
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated habitat YAML is read-only
  disposition_reason: Resolved the computational read-mixture identity with an ITEM
    NOT_APPLICABLE decision. The exact Modeled > Simulated communities (sequence read
    mixture) > Sanger path and the linked 113-isolate-genome benchmark establish a
    sequence-data artifact, not a physical habitat. The citable mint, source grouping,
    nodes, complete path and count omission remain; no sibling is reclassified.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1865
  previous_occurrences:
  - repository: culturebotai/HabitatMech
    review_id: 20261010T063411Z-sanger
    finding_id: F1
actions: []
limitations:
- Scoped self-review, not independent approval or an exhaustive new source census.
- Three skipped tests and 2057 label rows without adapters remain outside automated
  verification.
- 'No corpus-wide scientific approval or SSSOM/KGX compatibility conclusion follows;
  shared issue #1398 remains open.'
- Generated decision events reflect current maintained decisions. Superseded CLASS
  decisions remain in Git and immutable predecessor reviews; append-only session history
  records this curation.
related_reviews:
- repository: culturebotai/HabitatMech
  review_id: 20261010T063411Z-sanger
  relationship: Resolves the original F1; retains distinct new or pre-existing contract
    limitations explicitly.
notes:
- 'Initial CI 38032874915 found two valid PMID citations misclassified as ontology
  identifiers by the existing decision-note guard (issue #1868). The known-failed
  local QC run was stopped. Citation spelling was corrected to exact PubMed URLs without
  weakening the guard; the targeted failing test and both scoped regressions then
  passed (3 tests). New correction history was appended. Semantic inputs remained
  byte-identical; the final local full QC recorded here is a fresh rerun after that
  fix.'
links:
- https://github.com/CultureBotAI/HabitatMech/issues/1865
- https://github.com/CultureBotAI/HabitatMech/pull/1861
tags:
- habitatmech
- followup
- publication-review
```
