# Scoped publication follow-up: Sand microcosm

- Review: 20261010T073223Z-sand_microcosm-followup
- Repository: culturebotai/HabitatMech
- Started UTC: 2026-10-10T06:55:39Z
- Finished UTC: 2026-10-10T07:32:23Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Resolved the missing broader grounding with an ITEM GROUND_AS_PARENT decision to ENVO:01000621 microcosm. Retained the mint and artificial-ecosystem parent, distinguishing experimental system from river context and sand material. NARROW/REVIEWED is generator-derived. The separate emitted source-mapping endpoint mismatch remains open under #1398; this is not an overall clean mapping verdict.

## Scope And Provenance

Verify the named scientific correction and preserve other record claims; explicitly inspect changed mapping semantics.

Selection: Successor to the exact prior individual review; not newly covered scientific-record count.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 45f4455ecbd528303690b4dad66bf17edf32b692.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.14789d9032 | data/habitats/engineered/sand_microcosm.yaml | generated | Sand microcosm |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Target LinkML | passed | True | habitatmech:GOLD.14789d9032 | No issues found; fresh local execution. |
| Strict target validation | passed | True | habitatmech:GOLD.14789d9032 | Six files validated; zero errors. |
| Focused curation regressions | passed | True | habitatmech:GOLD.14789d9032 | 50 passed in 104.59s. |
| Exact corpus reproduction | passed | True | habitatmech:GOLD.14789d9032 | 3208 expected/found; zero missing, extra or differing. |
| Ontology labels | passed | True | habitatmech:GOLD.14789d9032 | 1178 canonical, one synonym and five exceptions; 2057 rows without adapters remain outside the automated gate. |
| Session history | passed | True | habitatmech:GOLD.14789d9032 | 244 valid append-only session records; actual actor attribution checked. |
| Authoritative local QC | passed | True | habitatmech:GOLD.14789d9032 | 660 passed, 3 skipped in 964.33s (0:16:04); all quality gates passed. |
| Generated site | passed | True | habitatmech:GOLD.14789d9032 | uv run python scripts/render_pages.py --check<br>rendered 3208 habitat pages, 252 redirect stubs, 8 categories, 114 term requests -&gt; /var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/tmpwuxnlan3/site<br>pages/ is in step with the corpus |
| Semantic-map artifact/cache | passed | True | habitatmech:GOLD.14789d9032 | Complete source-bound artifact passed; exact local/remote inputs and 3208 finite unique points separately verified. |
| Immutable predecessors | passed | True | habitatmech:GOLD.14789d9032 | Native inspect preceded follow-up assessment. Recapture verifies every previous input hash or the exact PMID-to-PubMed-URL correction in two notes/records via structured CSV/YAML comparison. No other captured input changed. All 236 prior review files are byte-identical. |
| Causal and expression-source applicability | not_applicable | False | habitatmech:GOLD.14789d9032 | No new causal mechanism, gene, regulator or expression-module claim is introduced. Contextual papers do not import such claims into the record. |

## Scientific And Domain Assessments

### Disposition of the reviewed correction

grounding: supported. Targets: habitatmech:GOLD.14789d9032.

Resolved the missing broader grounding with an ITEM GROUND_AS_PARENT decision to ENVO:01000621 microcosm. Retained the mint and artificial-ecosystem parent, distinguishing experimental system from river context and sand material. NARROW/REVIEWED is generator-derived. The separate emitted source-mapping endpoint mismatch remains open under #1398; this is not an overall clean mapping verdict.

### Preservation and generated products

consistency: supported. Targets: habitatmech:GOLD.14789d9032.

Only the six intended records change; four exclusions preserve every non-parent/history claim. The two ITEM decisions derive native status/history, retaining source identities and all source counts. The semantic map and pages are regenerated and verified.

### Remaining uncertainty and contract boundaries

grounding: concern. Targets: habitatmech:GOLD.14789d9032.

The emitted narrowMatch endpoint mismatch remains F2/#1398.

## Findings

### F1: Add the evidence-supported broader microcosm relation

major / resolved / confirmed; issue key: gold-14789d9032-sand-microcosm-missing-broader-grounding.

The CLASS-only decision retains UNGROUNDED despite a supported strictly broader microcosm concept. Exact BioSample context and the ENVO definition support a NARROW parent relation while preserving the source-specific mint.

Disposition: Resolved the missing broader grounding with an ITEM GROUND_AS_PARENT decision to ENVO:01000621 microcosm. Retained the mint and artificial-ecosystem parent, distinguishing experimental system from river context and sand material. NARROW/REVIEWED is generator-derived. The separate emitted source-mapping endpoint mismatch remains open under #1398; this is not an overall clean mapping verdict.

### F2: Retained source identity still receives a parent-comparison predicate

major / open / confirmed; issue key: gold-14789d9032-mapping-endpoint-contract.

The curated narrower-than-microcosm placement is scientifically supported, but its generated narrowMatch field uses the wrong documented comparison endpoints. SourceAttestation declares source-to-record identity; the actual decision compares the minted record to ENVO:01000621. This is another witness of shared issue #1398, not a predicate-direction swap or a claimed formal SKOS inconsistency.

## Recommended Actions And Acceptance Checks

### ACT2

Resolve the shared #1398 endpoint contract without removing the supported microcosm genus or merging the qualified mint into it.

- Specify source-to-record versus record-to-ontology-parent endpoints explicitly across schema and actual consumers.
- Cover minted, exact and broader/narrower routes with endpoint-aware tests, including this witness.
- Audit actual SSSOM/KGX triples against current kg-microbe modeling before claiming compatibility.
- Regenerate governed products, append curation history and pass full QC in the shared-contract correction.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/engineered/sand_microcosm.yaml; Complete regenerated YAML and field-by-field comparison with 486d97f799fe3df7d8933b6c9a5dab69e48f7f59 | supports | Resolved the missing broader grounding with an ITEM GROUND_AS_PARENT decision to ENVO:01000621 microcosm. Retained the mint and artificial-ecosystem parent, distinguishing experimental system from river context and sand material. NARROW/REVIEWED is generator-derived. The separate emitted source-mapping endpoint mismatch remains open under #1398; this is not an overall clean mapping verdict. |
| E2 | docs/CURATION.md; Strictly broader parents, source identity, decision and review-depth rules | supports | Source context is not subsumption; keep exact identity separate from broader placement. NOT_APPLICABLE concerns the source concept itself. Status is derived from maintained ITEM decisions, not from saving a review. |
| E3 | reviews/structured/20261010T063411Z-sand_microcosm/review.yaml; Original F1, inspected evidence and limitations; prior immutable YAML/Markdown pair | context_only | This successor resolves only the original finding. Original source-membership, optional-content and evidence limitations remain. This is not a fresh exhaustive literature or source-member census. |
| M1 | curation/decisions.tsv; Exact source-ID row and append-only history/mappings/sand_microcosm/ | supports | The maintained row records the verified source scope, actual agent, date, issue and evidence. Guarded seeding reproduces the intended correction without manual generated-record edits. |
| V1 | scripts/run_qc.py; Fresh local just qc execution; session gate-6 log | supports | All authoritative quality gates passed: 660 passed, 3 skipped in 964.33s (0:16:04). Includes provenance, tests, history, strict schema, causal overlays, curation floor, exact corpus reproduction and generated-site/redirect/term-request checks. |
| V2 | tests/test_sand_and_seating_review_fixes.py; Two full-corpus before/after tests plus existing guarded-exclusion regressions | supports | 50 focused tests passed. Four exclusions affect only parent/history fields of four documents; two ITEM decisions affect only their two resolved records. Source IDs, paths, unlike count units and unrelated claims are preserved. |
| V3 | https://github.com/CultureBotAI/HabitatMech/actions/runs/38032549518; Successful locked Linux map build, local exact input comparison, source-bound cache/bundle check and finite-point check | supports | Five changed texts encoded; the repeated canary reused all five and the full pass reused all 3208. Local and remote inputs byte-match SHA256 21f001aa3d07c2e510c906aa2160f5d91cceefc3e9d46bf72e350bc26bf153c0. All 3208 plotted identifiers are unique with finite coordinates, with unchanged encoder/projection settings. |
| P1 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&amp;id=SAMN06343863,SAMN14510915&amp;retmode=xml; Reinspected exact BioSample XML: GOLD classification, local context, medium, accessions and project links | supports | Both examples are GOLD-classified Sand microcosm. SAMN06343863 distinguishes river broad context, microcosm local context and sand medium; SAMN14510915 describes methanol-treated sandy-soil material. Neither establishes an exact generic sand or river identity. |
| O1 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO:01000621; Same-day OLS response reinspected: active ID, canonical label and description | supports | The controlled artificial ecosystem within a vivarium is a supported broader system genus for the sand-specific source concept, not its exact identity. |
| E4 | src/habitatmech/seed.py; _decided GROUND_AS_PARENT branch; SourceAttestation.mapping_predicate schema lines 317-322; actual regenerated attestation | supports | The route compares the retained mint with a broader ontology parent but emits narrowMatch into a field documented as source-to-record, with omission for retained source identity. The actual output reproduces existing issue #1398. |
| G1 | https://github.com/CultureBotAI/HabitatMech/issues/1398; Current OPEN issue body and added PR1861 witness comment | supports | Shared endpoint-contract defect remains unresolved; this is not a formal assertion that SKOS forbids hierarchical self-links or evidence of downstream product readiness. |

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
review_id: 20261010T073223Z-sand_microcosm-followup
kind: record
repository: culturebotai/HabitatMech
title: 'Scoped publication follow-up: Sand microcosm'
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
verdict: needs_curation
scientific_review: true
summary: 'Resolved the missing broader grounding with an ITEM GROUND_AS_PARENT decision
  to ENVO:01000621 microcosm. Retained the mint and artificial-ecosystem parent, distinguishing
  experimental system from river context and sand material. NARROW/REVIEWED is generator-derived.
  The separate emitted source-mapping endpoint mismatch remains open under #1398;
  this is not an overall clean mapping verdict.'
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
  - path: data/habitats/engineered/sand_microcosm.yaml
    sha256: 0460daceb44a2a4fe2f2f35384dbde5b58ac70e69677b151046ef31454106f85
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
  - path: history/mappings/sand_microcosm/2026-10-10T065303Z-codex-gpt-5-21c2f9.yaml
    sha256: af35b1c6a11cf7edfcd2c66fe8984bab8525f3d7fae35b20f0474d2e854bdf25
    role: context
  - path: history/mappings/sand_microcosm/2026-10-10T070915Z-codex-gpt-5-023ed6.yaml
    sha256: f3fa1ee223f386efb0491a5606efaa158fc69878fc44f533278413230cf8cbd2
    role: context
  - path: reviews/structured/20261010T063411Z-sand_microcosm/review.md
    sha256: b5205af48c6f45f75f8b7bbc9aaf0f1e32b1dccdbabca2539ac17971c5f6d2ad
    role: context
  - path: reviews/structured/20261010T063411Z-sand_microcosm/review.yaml
    sha256: 3bc07311fc6f6fb9bfb218e1cede749ffa2bfa7bc474a7de367a234f7b747220
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
- target_id: habitatmech:GOLD.14789d9032
  path: data/habitats/engineered/sand_microcosm.yaml
  label: Sand microcosm
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
  - habitatmech:GOLD.14789d9032
  exclusions:
  - target: Unchanged source membership and unrelated records
    reason: No new full source census or comprehensive literature re-review is claimed.
checks:
- check_id: C1
  name: Target LinkML
  command: just validate data/habitats/engineered/sand_microcosm.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.14789d9032
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
  - habitatmech:GOLD.14789d9032
  summary: Six files validated; zero errors.
- check_id: C3
  name: Focused curation regressions
  command: uv run pytest -q tests/test_sand_and_seating_review_fixes.py tests/test_gold_parent_exclusions.py
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.14789d9032
  summary: 50 passed in 104.59s.
- check_id: C4
  name: Exact corpus reproduction
  command: just verify-corpus
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.14789d9032
  summary: 3208 expected/found; zero missing, extra or differing.
- check_id: C5
  name: Ontology labels
  command: just validate-products
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.14789d9032
  summary: 1178 canonical, one synonym and five exceptions; 2057 rows without adapters
    remain outside the automated gate.
- check_id: C6
  name: Session history
  command: just validate-history
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.14789d9032
  summary: 244 valid append-only session records; actual actor attribution checked.
- check_id: C7
  name: Authoritative local QC
  command: just qc
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.14789d9032
  summary: 660 passed, 3 skipped in 964.33s (0:16:04); all quality gates passed.
- check_id: C8
  name: Generated site
  command: just render-check
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.14789d9032
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
  - habitatmech:GOLD.14789d9032
  summary: Complete source-bound artifact passed; exact local/remote inputs and 3208
    finite unique points separately verified.
- check_id: C10
  name: Immutable predecessors
  command: uv run python /private/tmp/habitatmech-pr1861-capture.py
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.14789d9032
  summary: Native inspect preceded follow-up assessment. Recapture verifies every
    previous input hash or the exact PMID-to-PubMed-URL correction in two notes/records
    via structured CSV/YAML comparison. No other captured input changed. All 236 prior
    review files are byte-identical.
- check_id: C11
  name: Causal and expression-source applicability
  status: not_applicable
  required: false
  target_ids:
  - habitatmech:GOLD.14789d9032
  summary: No new causal mechanism, gene, regulator or expression-module claim is
    introduced. Contextual papers do not import such claims into the record.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/engineered/sand_microcosm.yaml
  locator: Complete regenerated YAML and field-by-field comparison with 486d97f799fe3df7d8933b6c9a5dab69e48f7f59
  accessed_at: '2026-10-10T07:32:23Z'
  support: supports
  summary: 'Resolved the missing broader grounding with an ITEM GROUND_AS_PARENT decision
    to ENVO:01000621 microcosm. Retained the mint and artificial-ecosystem parent,
    distinguishing experimental system from river context and sand material. NARROW/REVIEWED
    is generator-derived. The separate emitted source-mapping endpoint mismatch remains
    open under #1398; this is not an overall clean mapping verdict.'
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
  reference: reviews/structured/20261010T063411Z-sand_microcosm/review.yaml
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
  locator: Exact source-ID row and append-only history/mappings/sand_microcosm/
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
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=SAMN06343863,SAMN14510915&retmode=xml
  locator: 'Reinspected exact BioSample XML: GOLD classification, local context, medium,
    accessions and project links'
  accessed_at: '2026-10-10T07:32:23Z'
  support: supports
  summary: Both examples are GOLD-classified Sand microcosm. SAMN06343863 distinguishes
    river broad context, microcosm local context and sand medium; SAMN14510915 describes
    methanol-treated sandy-soil material. Neither establishes an exact generic sand
    or river identity.
- evidence_id: O1
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO:01000621
  locator: 'Same-day OLS response reinspected: active ID, canonical label and description'
  accessed_at: '2026-10-10T07:32:23Z'
  support: supports
  summary: The controlled artificial ecosystem within a vivarium is a supported broader
    system genus for the sand-specific source concept, not its exact identity.
- evidence_id: E4
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: _decided GROUND_AS_PARENT branch; SourceAttestation.mapping_predicate schema
    lines 317-322; actual regenerated attestation
  accessed_at: '2026-10-10T07:32:23Z'
  support: supports
  summary: 'The route compares the retained mint with a broader ontology parent but
    emits narrowMatch into a field documented as source-to-record, with omission for
    retained source identity. The actual output reproduces existing issue #1398.'
- evidence_id: G1
  kind: database
  reference: https://github.com/CultureBotAI/HabitatMech/issues/1398
  locator: Current OPEN issue body and added PR1861 witness comment
  accessed_at: '2026-10-10T07:32:23Z'
  support: supports
  summary: Shared endpoint-contract defect remains unresolved; this is not a formal
    assertion that SKOS forbids hierarchical self-links or evidence of downstream
    product readiness.
assessments:
- assessment_id: A1
  area: grounding
  topic: Disposition of the reviewed correction
  outcome: supported
  summary: 'Resolved the missing broader grounding with an ITEM GROUND_AS_PARENT decision
    to ENVO:01000621 microcosm. Retained the mint and artificial-ecosystem parent,
    distinguishing experimental system from river context and sand material. NARROW/REVIEWED
    is generator-derived. The separate emitted source-mapping endpoint mismatch remains
    open under #1398; this is not an overall clean mapping verdict.'
  target_ids:
  - habitatmech:GOLD.14789d9032
  evidence_ids:
  - E1
  - E2
  - E3
  - M1
  - P1
  - O1
- assessment_id: A2
  area: consistency
  topic: Preservation and generated products
  outcome: supported
  summary: Only the six intended records change; four exclusions preserve every non-parent/history
    claim. The two ITEM decisions derive native status/history, retaining source identities
    and all source counts. The semantic map and pages are regenerated and verified.
  target_ids:
  - habitatmech:GOLD.14789d9032
  evidence_ids:
  - E1
  - M1
  - V1
  - V2
  - V3
- assessment_id: A3
  area: grounding
  topic: Remaining uncertainty and contract boundaries
  outcome: concern
  summary: The emitted narrowMatch endpoint mismatch remains F2/#1398.
  target_ids:
  - habitatmech:GOLD.14789d9032
  evidence_ids:
  - E1
  - E4
  - G1
findings:
- finding_id: F1
  issue_key: gold-14789d9032-sand-microcosm-missing-broader-grounding
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Add the evidence-supported broader microcosm relation
  description: The CLASS-only decision retains UNGROUNDED despite a supported strictly
    broader microcosm concept. Exact BioSample context and the ENVO definition support
    a NARROW parent relation while preserving the source-specific mint.
  target_ids:
  - habitatmech:GOLD.14789d9032
  field_paths:
  - grounding_status
  - parent_habitats
  evidence_ids:
  - E1
  - E2
  - E3
  - M1
  - P1
  - O1
  - V1
  - V2
  rule_id: HabitatMech:strictly-broader-parents
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
  disposition_reason: 'Resolved the missing broader grounding with an ITEM GROUND_AS_PARENT
    decision to ENVO:01000621 microcosm. Retained the mint and artificial-ecosystem
    parent, distinguishing experimental system from river context and sand material.
    NARROW/REVIEWED is generator-derived. The separate emitted source-mapping endpoint
    mismatch remains open under #1398; this is not an overall clean mapping verdict.'
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1863
  previous_occurrences:
  - repository: culturebotai/HabitatMech
    review_id: 20261010T063411Z-sand_microcosm
    finding_id: F1
- finding_id: F2
  issue_key: gold-14789d9032-mapping-endpoint-contract
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Retained source identity still receives a parent-comparison predicate
  description: 'The curated narrower-than-microcosm placement is scientifically supported,
    but its generated narrowMatch field uses the wrong documented comparison endpoints.
    SourceAttestation declares source-to-record identity; the actual decision compares
    the minted record to ENVO:01000621. This is another witness of shared issue #1398,
    not a predicate-direction swap or a claimed formal SKOS inconsistency.'
  target_ids:
  - habitatmech:GOLD.14789d9032
  field_paths:
  - source_attestations[0].mapping_predicate
  evidence_ids:
  - E1
  - E4
  - G1
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: Shared mapping endpoint contract and emitted predicates
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Shared mapping endpoint contract and emitted predicates
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
  rule_id: HabitatMech:source-attestation-endpoints
  native_severity: major
  normalization_reason: The published mapping field compares different endpoints than
    its schema contract. Shared generator repair is required.
actions:
- action_id: ACT2
  description: 'Resolve the shared #1398 endpoint contract without removing the supported
    microcosm genus or merging the qualified mint into it.'
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.14789d9032
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: Shared mapping endpoint contract and emitted predicates
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Shared mapping endpoint contract and emitted predicates
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Specify source-to-record versus record-to-ontology-parent endpoints explicitly
    across schema and actual consumers.
  - Cover minted, exact and broader/narrower routes with endpoint-aware tests, including
    this witness.
  - Audit actual SSSOM/KGX triples against current kg-microbe modeling before claiming
    compatibility.
  - Regenerate governed products, append curation history and pass full QC in the
    shared-contract correction.
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
  review_id: 20261010T063411Z-sand_microcosm
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
- https://github.com/CultureBotAI/HabitatMech/issues/1863
- https://github.com/CultureBotAI/HabitatMech/pull/1861
tags:
- habitatmech
- followup
- publication-review
```
