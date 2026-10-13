# Engineered Mine water: source identity preserved; industrial-wastewater genus needs scope reconciliation

- Review: 20261009T143453Z-engineered-mine-water
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-09T14:16:56Z
- Finished UTC: 2026-10-09T14:34:53Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Full one-record review preserves the exact source identity, counts and native lifecycle, but records one provisional major concern: the automatic industrial-wastewater parent may overstate the scope of a heterogeneous GOLD category. Current GOLD crosswalks, exact submitted samples and primary abstracts support the concern, not a definitive source reclassification. Original frozen member-level evidence and category intent remain unresolved; no scientific input or generated output is changed.

## Scope And Provenance

Entire generated engineered Mine water record, sole source concept, immediate parent context, maintained source/decision route, all current exact-path sample/organism contexts and bounded primary-source cross-checks.

Selection: Continuation of the engineered-record review sequence; resolved target is habitatmech:GOLD.6a0644fced, not the similarly labelled groundwater sibling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 016bfc2de4301e13930d5701a03c016cc150295f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.6a0644fced | data/habitats/engineered/mine_water.yaml | generated | Mine water |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Exact pre-assessment input capture | passed | True | habitatmech:GOLD.6a0644fced | Captured 41 inputs at 016bfc2de4301e13930d5701a03c016cc150295f before scientific assessment. |
| Target LinkML validation | passed | True | habitatmech:GOLD.6a0644fced | No issues found. |
| Target closed-schema validation | passed | True | habitatmech:GOLD.6a0644fced | One file, zero errors. |
| All 14 committed raw TSV exact-field scan | passed | True | habitatmech:GOLD.6a0644fced | Recovered path, separate biosample inventory and six study rows. No exact target-path triad, parameter, BacDive, PREGO or Madin row in these tables; bounded absence only. |
| Actual seeder route and complete target reconstruction | passed | True | habitatmech:GOLD.6a0644fced | gold_unmatched becomes curated_confirm_ungrounded_from_gold_unmatched; one contributing source, zero ITEM-reviewed sources. Parent path resolves by gold_leaf_label to ENVO:01000964. Whole generated document equals the target. |
| Exact corpus reproduction | passed | True | habitatmech:GOLD.6a0644fced | 3,208 expected and present; zero missing, extra or differing records. |
| Native append-only history validation | passed | True | habitatmech:GOLD.6a0644fced | 220 valid history records. |
| Frozen inventory manifests | passed | True | habitatmech:GOLD.6a0644fced | All 14 inventories and two GOLD-source manifests current. |
| Focused existing corpus-integrity regressions | passed | True | habitatmech:GOLD.6a0644fced | 6 passed, 33 deselected in 24.55 seconds. |
| Current public GOLD exact-path scan | passed | False | habitatmech:GOLD.6a0644fced | Completed scan: 70 biosamples, nine organisms, 85 linked sequencing projects and 13 study IDs. Initial stdout was truncated; the separate contact-free replay below supplied the complete compact crosswalk. |
| Complete contact-free GOLD sample/project/study replay | passed | False | habitatmech:GOLD.6a0644fced | Inspected all 70 sample names/sites, 85 project crosswalk rows and all 13 study names/descriptions. Six studies have exact-path biosamples (1+5+15+5+14+30); seven are organism-only. All 70 biosample and nine organism IDs join to projects. |
| Initial sandbox OLS request | failed | False | habitatmech:GOLD.6a0644fced | DNS failure; no ontology response obtained in this attempt. The separately recorded authorized retry succeeded. |
| Current official ontology identities and bounded candidate search | passed | True | habitatmech:GOLD.6a0644fced | Authorized retry inspected industrial wastewater, mine drainage, acid mine drainage and gold mine drainage; all active. Search returned 26 hits, first 20 inspected only. |
| Initial primary abstract and full-text attempt | failed | False | habitatmech:GOLD.6a0644fced | Read PMID 12807207 and PMID 10049886 abstracts. PMC91167 fullTextXML returned HTTP 500 and exited 1; subsequent requested abstracts did not execute in this call. |
| Remaining primary abstracts and PMC metadata retry | passed | False | habitatmech:GOLD.6a0644fced | Read PMID 11491320 and PMID 22115438 abstracts. NCBI PMC91167 XML was metadata only despite the diagnostic print label FULLTEXT; it supplied no body/methods. |
| Explicit metadata-versus-full-text check | passed | False | habitatmech:GOLD.6a0644fced | PMC91167 efetch response contains one article, zero sections and no body. Correct identity metadata does not certify a full-text inspection. |
| Exact public sample metadata cross-check | passed | False | habitatmech:GOLD.6a0644fced | All three exact sample accessions resolved: sediment in a mine-tailing pool; thiosulfate-fed enrichment from a mine-wastewater reservoir; DSM 15120 isolated from subsurface hot aquifer water. |
| Optional web fetch routes | unavailable | False | habitatmech:GOLD.6a0644fced | Web opens of exact OLS endpoints were unavailable. PMC pages yielded reCAPTCHA only. Official structured OLS and abstract APIs succeeded independently; no full-text methods claimed. |
| Captured hashes and exact base-tree equality | passed | True | habitatmech:GOLD.6a0644fced | All 41 captured SHA-256 values still match, and every input equals its bytes at the original Git base. |
| Fresh exact-baseline full-QC receipt | passed | True | habitatmech:GOLD.6a0644fced | Completed success at exact base 016bfc2de4301e13930d5701a03c016cc150295f. Actual logs inspected during preceding publication showed 646 passed, three skipped (422.98 seconds), plus all native QC gates. Reused because scientific inputs are byte-identical; this is not a fresh local full-QC run. |
| Fresh exact-baseline ontology-label receipt | passed | True | habitatmech:GOLD.6a0644fced | Completed success at exact same base. No new global ontology download or full local validate-products run; target parent and candidate term definitions were additionally inspected live. |
| Target causal-overlay and molecular applicability | not_applicable | False | habitatmech:GOLD.6a0644fced | No causal graph, causal overlay, genes, regulators, proteins, expression datasets or characteristic-taxon claims on this target. Target-specific causal and iModulonDB assessment not applicable, not negative biological evidence. |

## Scientific And Domain Assessments

### Exact source identity versus a single physical-material class

identity: concern. Targets: habitatmech:GOLD.6a0644fced.

Mint and path are correct and the category contains actual microbial habitat observations. Current usage spans water materials, sampled solids, enrichment cultures and deep aquifer sources; the precise class denoted by the frozen source category remains unresolved. This is not evidence to mark the entire target NOT_APPLICABLE.

### Conservative ungrounded identity and near candidates

grounding: supported. Targets: habitatmech:GOLD.6a0644fced.

No supported exact replacement is established. Retain the minted identity and UNGROUNDED status pending source interpretation; mine drainage adds an outflow condition, acid mine drainage adds acidity, and gold mine drainage adds a mining qualifier not universal across the category.

### Strict industrial-wastewater parent

graph: concern. Targets: habitatmech:GOLD.6a0644fced.

The parent is an automatic path projection, not an independently ITEM-endorsed genus. Submitted sample metadata and primary abstracts raise a material-versus-setting and natural-water-versus-wastewater concern. They do not alone prove the frozen category's intended scope or justify an automatic parent exclusion.

### Source counts, units and snapshot separation

quantity: supported. Targets: habitatmech:GOLD.6a0644fced.

14 ORGANISM occurrences over two collapsed KGX ecosystem nodes reproduce exactly. The separate 70-biosample inventory and current 9-organism/85-project crosswalk have different versions and units; they neither replace nor sum with 14. Matching biosample totals do not prove identical historical membership.

### CLASS decision, SEEDED status and generated history

consistency: supported. Targets: habitatmech:GOLD.6a0644fced.

One CLASS decision and zero ITEM-reviewed contributing concepts correctly retain SEEDED. This review neither promotes scientific status nor appends a curation event. Missing optional fields and prior CLASS depth are not separate major findings.

### Definition and novel-term readiness

completeness: unknown. Targets: habitatmech:GOLD.6a0644fced.

No authored target definition or novel-term request was recovered in the ignored-inclusive maintained-input search. Optional omission is not itself a defect. Scope must be resolved before choosing a genus, requesting a term or merging the groundwater sibling.

### Environmental parameters, triad roles and culture conditions

scope: not_applicable. Targets: habitatmech:GOLD.6a0644fced.

Target asserts no parameters or triad. No exact target-path row in the committed parameter/triad tables; this is not a statement that all source samples lack environmental metadata. Culture optima and acidity from individual studies are not universal habitat properties.

### Taxa and mechanisms

evidence: not_applicable. Targets: habitatmech:GOLD.6a0644fced.

No target taxon associations or causal edges to validate. Current organism records identify source contexts only; no characteristic taxa, phylogenetic assertion or mechanistic claims were inferred. iModulonDB is not applicable.

### Generated ownership and deterministic gates

ownership: supported. Targets: habitatmech:GOLD.6a0644fced.

Whole-document reproduction, source/hash checks, schema and native gates pass. Any eventual fix belongs to maintained decisions and guarded parent exclusions or a supported definition, followed by native canary/regeneration/history and semantic product checks; never to generated YAML or pages.

## Findings

### F1: Reconcile the strict industrial-wastewater genus with mixed GOLD source usage

major / open / provisional; issue key: mine-water-industrial-wastewater-source-scope.

The sole parent_habitats edge asserts that this whole source-defined class is industrial wastewater. It comes from the GOLD path rather than a source-specific scientific endorsement. Current exact-path source usages include independently verified sediment, an enrichment culture, and a deep hot-aquifer isolate, alongside clear wastewater samples. These distinctions materially challenge a universal material identity, while not proving the upstream category wrong: sampling material may be inside a wastewater setting, and current membership is not the frozen KGX membership. Resolve the original category intent and member context before endorsing, replacing or excluding the parent. Do not infer that deep water was uncontaminated, that all members are mine drainage, or that the complete category is not a habitat.

## Recommended Actions And Acceptance Checks

### A1

Recover the original GOLD category meaning and frozen organism-level sources; distinguish wastewater material, sampled setting, natural water, enrichment and upstream annotation error. Then make an evidence-backed ITEM decision and only those guarded hierarchy/definition changes the evidence warrants.

- Document the exact historical source/path/node membership or its remaining recovery limit; keep 14 ORGANISM occurrences distinct from current organisms, biosamples and project counts.
- Explain why ENVO:01000964 is strictly broader for the exact source concept, or support an exact-path gold_parent_exclusions.tsv row without suppressing independent ontology/curator parents. No exclusion solely because current sample material differs from a setting label.
- Explicitly assess mine drainage and the distinct groundwater Mine water concept without an unsupported exact merge, universal acidity/gold-mining qualifier, arbitrary split, or NOT_APPLICABLE decision.
- If scientific inputs change: append native history; add exact-source/edge regression coverage; dry-seed, force a target canary and inspect the entire output before guarded full regeneration. Do not hand-edit generated records or prune partial runs.
- Run target strict/schema, provenance/history, exact corpus reproduction, live label correspondence for any grounding change, genuine site/semantic-map/product refresh required by native change scope, and full just qc. Save a new linked immutable review retaining this issue_key and previous occurrence for any scientific disposition.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/habitats/engineered/mine_water.yaml; Entire file; PATHS.tsv physical line 2062 | supports | Minted Mine water, ENGINEERED, UNGROUNDED, SEEDED; sole parent ENVO:01000964; one GOLD attestation with 14 ORGANISM occurrences and two collapsed nodes; CLASS history plus seed history. No authored definition, taxa, parameters, xrefs or causal graph. |
| frozen | data/raw/gold_ecosystem_paths.tsv; Logical row 475, exact canonical path; data/raw/gold_path_biosamples.tsv logical row 300; gold_studies.tsv logical rows 1258,1508,1706,1933,2289,4541 | supports | Engineered &gt; Wastewater &gt; Industrial wastewater &gt; Mine water collapses nodes 3839 and 4270, preserving first-node attestation 3839 and 14 ORGANISM occurrences. Separate bulk inventory has 70 biosamples on 4270 and six study IDs. Zero study/biosample counters in the older KGX-derived row are not evidence that no samples exist. |
| decision | curation/decisions.tsv; Physical line 630, habitatmech:GOLD.6a0644fced | supports | CONFIRM_UNGROUNDED at CLASS depth explicitly leaves habitat meaning unassessed. It does not endorse a strict parent or promote mapping_status to REVIEWED. |
| generation | src/habitatmech/seed.py; resolve_gold and ingest_gold; actual route/reconstruction check; src/habitatmech/extract.py lines 123-242 | supports | The immediate GOLD path parent supplies ENVO:01000964 via the parent's automatic gold_leaf_label route. Count extraction aggregates Go occurs_in edges by collapsed source path; it is not a count of current public-workbook unique organisms. Exact source mint and complete target reconstruction agree. |
| rules | docs/CURATION.md; Decision model; curated definitions and hierarchy; CLAUDE.md semantic invariants; native checklist | supports | All parent contributions must express a strict broader class, not a sampled setting. Source association and native validation alone cannot certify identity. Optional fields and CLASS status alone are not major findings. |
| parent | data/habitats/engineered/industrial_wastewater.yaml; Entire context record, ENVO:01000964 | context_only | Parent describes industrially produced wastewater with non-fecal chemical contaminants. Its existence and automatic exact grounding do not prove every descendant path has the same material scope. This is not a complete scientific review of the parent. |
| bulk | https://gold.jgi.doe.gov/download?mode=site_excel; Oct 9 public workbook, 238974789 bytes; sheets 2-5; exact path and source IDs 4270 / Go0000121,Go0006917,Go0013366,Go0035556,Go0037571,Go0044073,Go0047507,Go0050683,Go0509422 | partial | Current exact-path membership is 70 biosamples and nine organisms, joined through 85 sequencing projects to 13 studies. Biosample study counts: Gs0121252=1, Gs0128962=5, Gs0132928=15, Gs0133347=5, Gs0141931=14, Gs0164315=30. Source metadata includes drainage/runoff, tailings waters, sediment, enrichments, natural deep aquifer/fissure water and treatment-bed isolates. This is newer contextual evidence, not the frozen KGX membership or the August GOLD_MANIFEST snapshot. |
| bulk-contexts | https://gold.jgi.doe.gov/download?mode=site_excel; Exact-path sample and organism rows; compact crosswalk checks | partial | All 70 sample names/sites and all nine organism contexts were inspected. Gs0132928 contains three thiosulfate enrichments plus runoff/reservoir/discharge samples; Gs0133347 contains five sediment samples; only 14 exact-path samples are used from multipath Gs0141931. Go0013366 is DSM 15120 from a hot aquifer; Go0006917 is SA-01 from deep groundwater; Go0047507 and Go0050683 are treatment-bed fungal isolates. These are source usages, not characteristic taxa or proof that upstream classification is correct. |
| envo-industrial | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01000964; ENVO:01000964 industrial wastewater; identifier, label, definition, obsolete flag and synonyms inspected | context_only | Current active definition requires wastewater produced by industrial activity and containing non-fecal chemical contaminants. GOLD ancestry is not independent support for universal satisfaction of that definition. |
| envo-drainage | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_00001996; ENVO:00001996 mine drainage; identifier, label, definition, obsolete flag and synonyms inspected | context_only | Active outflow-of-water-from-mine concept. Related acid/metalliferous synonyms are not exact synonyms; source waters need not all be outflow features. |
| envo-acid | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_00001997; ENVO:00001997 acid mine drainage; identifier, label, definition, obsolete flag and synonyms inspected | context_only | Active mine-drainage concept requiring acidic pH. A subset of source samples labelled AMD does not establish universal acidity. |
| envo-gold | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_00002112; ENVO:00002112 gold mine drainage; identifier, label, definition, obsolete flag and synonyms inspected | context_only | Active gold-mining-qualified drainage concept. The target includes non-gold mining and other material contexts; it is not an exact substitute. |
| ols-search | https://www.ebi.ac.uk/ols4/api/search?q=mine+water&amp;ontology=envo&amp;rows=20&amp;type=class; First 20 of 26 hits | context_only | No exact identity is established by this bounded tokenized search. Near mine-drainage candidates were read directly rather than discarded for label mismatch. |
| primary-aquifer | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12807207+AND+SRC%3AMED&amp;format=json&amp;resultType=core; PMID:12807207; DOI:10.1099/ijs.0.02506-0; bibliographic identity and complete abstract | partial | Takai et al. 2003 abstract reports isolation from subsurface hot aquifer water in a Japanese gold mine. Type-strain aliases include DSM 15120, linking the paper to GOLD Go0013366. Supports collection context only, not absence of industrial contamination or a universal habitat definition. |
| primary-thermus-isolation | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10049886+AND+SRC%3AMED&amp;format=json&amp;resultType=core; PMID:10049886; DOI:10.1128/aem.65.3.1214-1221.1999; bibliographic identity and complete abstract | partial | Kieft et al. 1999 abstract reports SA-01 isolated from groundwater 3.2 km deep in a South African gold mine. Matches GOLD Go0006917 strain context; full article methods were not recovered. |
| primary-alkaliphilus | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11491320+AND+SRC%3AMED&amp;format=json&amp;resultType=core; PMID:11491320; DOI:10.1099/00207713-51-4-1245; bibliographic identity and complete abstract | partial | Takai et al. 2001 abstract reports isolation from a containment dam 3.2 km deep in a South African gold mine, SAGM1=ATCC 700919, matching Go0044073. The workbook's 32 km string is not propagated; depth is not a target field. |
| primary-thermus-genome | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22115438+AND+SRC%3AMED&amp;format=json&amp;resultType=core; PMID:22115438; DOI:10.1186/1471-2164-12-577; bibliographic identity and complete abstract | partial | Gounder et al. 2011 abstract identifies SA-01's fissure-water source at 3.2 km depth. Corroborates bounded collection context; no genomic mechanism, culture optimum or phenotype is transferred to the habitat. |
| ena-sediment | https://www.ebi.ac.uk/ena/browser/api/xml/SAMEA3904894; Exact sample accession, title and complete sample attributes | partial | GOLD Gp0289437/Gb0181570/Gs0133347 crosswalk resolves to a primary submitted sample with sediment material and mine-tailing-pool biome/feature. Demonstrates material-versus-setting distinction for this sample, not the entire category. |
| ena-enrichment | https://www.ebi.ac.uk/ena/browser/api/xml/SAMN06612095; Exact sample accession, title and complete sample attributes | partial | GOLD Gp0272781/Gb0165115/Gs0132928 resolves to enrichment 3 from oxidation-reservoir shore water; isolation text retains mine wastewater. The enrichment can retain source context without becoming evidence that all members are natural waters. |
| ena-aquifer | https://www.ebi.ac.uk/ena/browser/api/xml/SAMN02769639; Exact sample accession, title and complete sample attributes | partial | GOLD Gp0013366/Go0013366/Gs0015051 resolves to DSM 15120 with Japanese subsurface hot-aquifer-water isolation source. Independently corroborates the strain/source link; metadata does not establish industrial contamination absent or present. |
| search-local | curation/; history/; research/; reports/; reviews/; data/habitats/PATHS.tsv; Ignored-inclusive exact identifier/path/slug search and filename search | context_only | Recovered target decision/path, a child Sediment sample review, and the distinct groundwater Mine water historical report. No target-specific engineered Mine water report, overlay or novel definition recovered within these bounded roots. |
| sibling | reports/yaml_record_review/20260926T173701Z-mine_water__20810f85.md; Entire historical review, distinct habitatmech:GOLD.943d5cba70 | context_only | The groundwater sibling is not this engineered target. Its 206 biosamples, triad and proposed genus cannot be transferred. Its CLASS-based major rationale is not adopted here. No finding in that separate review is closed. |
| validation | https://github.com/CultureBotAI/HabitatMech/actions/runs/37941486985; Exact-base completed-success receipt; fresh target/corpus/history/reference/provenance checks | supports | Structural reproducibility and native lifecycle checks pass. They do not establish scientific parent scope or independent scientific approval. |

## Limits And Additional Notes

- This is a completed scoped assessment with an unresolved provisional finding, not scientific approval of the record or completion of the 3,208-record corpus objective.
- Current Oct 9 GOLD workbook is not the frozen kg-microbe input or the Aug 20 GOLD_MANIFEST snapshot (SHA-256 6797471982570ed145f81aef966c1ff5398dc4d35287a01faefaf80ac5311fea). The original 14 occurrence memberships were not recovered.
- All 70 current sample contexts, nine organism contexts and 85 GOLD project links were inspected, but only three external sample accessions and four primary abstracts were independently cross-checked. Other source-provided BioProjects, BioSamples and publication IDs are context metadata, not independently validated claims.
- Primary isolation/genome abstracts support reported source context only. Europe PMC full-text retrieval failed; PMC web routes yielded reCAPTCHA; NCBI efetch supplied metadata without a body. No full methods, industrial-contamination absence, or universal habitat physiology is claimed.
- OLS candidate search inspected only its first 20 of 26 hits. Existing near terms are discussed directly; no exhaustive ontology term-absence conclusion or novel-term readiness is asserted.
- Full native QC and whole-corpus label checks are reused from verified exact-base CI receipts because all scientific inputs are unchanged. Fresh focused/schema/provenance/history/reproduction checks are recorded separately; receipt reuse is not a fresh local full QC run.
- Source category heterogeneity can reflect material-versus-setting roles or upstream annotation mistakes, not necessarily a genuinely heterogeneous intended class. The parent concern therefore remains provisional; no automatic curation is authorized by the report itself.
- Evidence accessed_at timestamps mark final inspection of the captured local inputs and retrieved responses during report construction on Oct 9. Public source retrievals occurred earlier the same session; no historical retrieval timestamp is invented.
- No generated record, curation input, history entry, source inventory, page, product or previous immutable review was changed. Public study contact fields are irrelevant and are not retained.
- No finding in a sibling review or existing GitHub issue is closed by this new observation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261009T143453Z-engineered-mine-water
kind: record
repository: CultureBotAI/HabitatMech
title: 'Engineered Mine water: source identity preserved; industrial-wastewater genus
  needs scope reconciliation'
started_at: '2026-10-09T14:16:56Z'
finished_at: '2026-10-09T14:34:53Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent continuing the corpus review; not independent scientific
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Full one-record review preserves the exact source identity, counts and native
  lifecycle, but records one provisional major concern: the automatic industrial-wastewater
  parent may overstate the scope of a heterogeneous GOLD category. Current GOLD crosswalks,
  exact submitted samples and primary abstracts support the concern, not a definitive
  source reclassification. Original frozen member-level evidence and category intent
  remain unresolved; no scientific input or generated output is changed.'
source:
  git_revision: 016bfc2de4301e13930d5701a03c016cc150295f
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
  - path: conf/record_review.yaml
    sha256: c2f5d0eb4c5744f5fe354c92184ddab144dc2688dba952b032b4f3d597bc08d6
    role: context
  - path: conf/sources.yaml
    sha256: a8e069f9278068b57fa234f43e03c8d893f857827b83fd10cfa92d6815aed642
    role: context
  - path: curation/decisions.tsv
    sha256: 0602cca13e6495da256a6f1cfd5897462f73f9739a729447862017d93c148efd
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 9d2324647d0a0ddeccc2f7836811872e112af208bb1b8f7decb332c00f17d12b
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
  - path: data/habitats/RETIRED.tsv
    sha256: 41beffc45aabdf304de633c21200b375d7f01d1cb2e036d4a026961d545a35e5
    role: context
  - path: data/habitats/engineered/industrial_wastewater.yaml
    sha256: 07698df721a169cd55c2d1ce80027df8c8a3140536ba99eee312272887ce8768
    role: context
  - path: data/habitats/engineered/mine_water.yaml
    sha256: c285eed1f2bc078931182954bb1f290d8e0a7c05cc5940fbac9509503ef6b38c
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
  - path: reports/yaml_record_review/20260926T173701Z-mine_water__20810f85.md
    sha256: 27d5a4bd2403e9d7780d97a382d93441af29afa94d6e27d7c2566aafd648e9b6
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
targets:
- target_id: habitatmech:GOLD.6a0644fced
  path: data/habitats/engineered/mine_water.yaml
  label: Mine water
  kind: generated
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Exact GOLD.6a0644fced decision row
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Source-specific parent exclusions
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Any supported novel definition and genus
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Frozen GOLD path and count
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Generated record and hierarchy
scope:
  description: Entire generated engineered Mine water record, sole source concept,
    immediate parent context, maintained source/decision route, all current exact-path
    sample/organism contexts and bounded primary-source cross-checks.
  selection: Continuation of the engineered-record review sequence; resolved target
    is habitatmech:GOLD.6a0644fced, not the similarly labelled groundwater sibling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.6a0644fced
  exclusions:
  - target: Other 3,207 records, including groundwater Mine water and industrial wastewater
    reason: Context reads are not whole-record scientific review or disposition of
      their findings.
  - target: Frozen KGX per-organism source statements and all external study/sample
      publications
    reason: Frozen 14-occurrence membership was not reconstructed. Current workbook
      crosswalk is complete for its exact path, but external validation is limited
      to three submitted samples and four primary abstracts.
checks:
- check_id: capture
  name: Exact pre-assessment input capture
  status: passed
  required: true
  summary: Captured 41 inputs at 016bfc2de4301e13930d5701a03c016cc150295f before scientific
    assessment.
  target_ids:
  - habitatmech:GOLD.6a0644fced
  command: env UV_CACHE_DIR=build/uv-cache uv run python scripts/record_review.py
    inspect --targets /private/tmp/habitatmech-20261009j-mine-water-targets.json --input
    .claude/skills/curate-yaml-record/references/review-checklist.md --input .claude/skills/review-yaml-record/SKILL.md
    --input CLAUDE.md --input conf/record_review.yaml --input conf/sources.yaml --input
    curation/decisions.tsv --input curation/gold_parent_exclusions.tsv --input curation/term_requests.tsv
    --input curation/term_requests_excluded.tsv --input data/habitats/PATHS.tsv --input
    data/habitats/RETIRED.tsv --input data/raw/GOLD_MANIFEST.yaml --input data/raw/MANIFEST.yaml
    --input data/raw/bacdive_isolation_sources.tsv --input data/raw/bacdive_source_taxa.tsv
    --input data/raw/environment_parameters.tsv --input data/raw/gold_ecosystem_paths.tsv
    --input data/raw/gold_path_biosamples.tsv --input data/raw/gold_path_triads.tsv
    --input data/raw/gold_studies.tsv --input data/raw/isolation_source_groundings.tsv
    --input data/raw/madin_habitat_taxa.tsv --input data/raw/madin_habitats.tsv --input
    data/raw/ontology_subclass_edges.tsv --input data/raw/ontology_terms.tsv --input
    data/raw/prego_habitat_taxa.tsv --input data/raw/prego_habitats.tsv --input docs/CURATION.md
    --input docs/HARMONIZATION.md --input docs/RESEARCH.md --input docs/record-review-profile.md
    --input docs/record-reviews.md --input justfile --input schema/record_review.yaml
    --input src/habitatmech/extract.py --input src/habitatmech/schema/habitatmech.yaml
    --input src/habitatmech/seed.py --input data/habitats/engineered/industrial_wastewater.yaml
    --input reports/yaml_record_review/20260926T173701Z-mine_water__20810f85.md --input
    scripts/extract_gold_biosamples.py
  exit_code: 0
- check_id: schema
  name: Target LinkML validation
  status: passed
  required: true
  summary: No issues found.
  target_ids:
  - habitatmech:GOLD.6a0644fced
  command: env UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/mine_water.yaml
  exit_code: 0
- check_id: strict
  name: Target closed-schema validation
  status: passed
  required: true
  summary: One file, zero errors.
  target_ids:
  - habitatmech:GOLD.6a0644fced
  command: env UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/mine_water.yaml
  exit_code: 0
- check_id: raw
  name: All 14 committed raw TSV exact-field scan
  status: passed
  required: true
  summary: Recovered path, separate biosample inventory and six study rows. No exact
    target-path triad, parameter, BacDive, PREGO or Madin row in these tables; bounded
    absence only.
  target_ids:
  - habitatmech:GOLD.6a0644fced
  command: "env UV_CACHE_DIR=build/uv-cache uv run python - <<'PY'\nfrom pathlib import\
    \ Path\nimport csv,json\npath='Engineered > Wastewater > Industrial wastewater\
    \ > Mine water'\nwith Path('data/raw/gold_ecosystem_paths.tsv').open() as f:\n\
    \    src=next(r for r in csv.DictReader(f,delimiter='\\t') if r['canonical_path']==path)\n\
    needles={path,'habitatmech:GOLD.6a0644fced',*src['gold_node_ids'].split('|')}\n\
    for p in sorted(Path('data/raw').glob('*.tsv')):\n    matches=[]\n    with p.open()\
    \ as f:\n        for n,row in enumerate(csv.DictReader(f,delimiter='\\t'),2):\n\
    \            vals=[v for x in row.values() for v in (x if isinstance(x,list) else\
    \ [x]) if v]\n            if any(v in needles or needles.intersection(v.split('|'))\
    \ for v in vals):\n                matches.append({'logical_row':n,'row':row})\n\
    \    print(p.name,json.dumps(matches))\nPY"
  exit_code: 0
- check_id: route
  name: Actual seeder route and complete target reconstruction
  status: passed
  required: true
  summary: gold_unmatched becomes curated_confirm_ungrounded_from_gold_unmatched;
    one contributing source, zero ITEM-reviewed sources. Parent path resolves by gold_leaf_label
    to ENVO:01000964. Whole generated document equals the target.
  target_ids:
  - habitatmech:GOLD.6a0644fced
  command: "env UV_CACHE_DIR=build/uv-cache uv run python - <<'PY'\nfrom habitatmech\
    \ import seed as s\nfrom pathlib import Path\nfrom dataclasses import asdict\n\
    import json,yaml\nrows=s.read_tsv('gold_ecosystem_paths.tsv');ont=s.OntologyIndex(s.read_tsv('ontology_terms.tsv'),s.read_tsv('ontology_subclass_edges.tsv'));decisions=s.load_decisions(s.DECISIONS_PATH)\n\
    mapping={}\nfor r in s.read_tsv('isolation_source_groundings.tsv'):\n    for text\
    \ in [r['subject_label'],r['subject_label_normalized']]:\n        if s.norm_label(text):mapping.setdefault(s.norm_label(text),r)\n\
    for path in ['Engineered > Wastewater > Industrial wastewater > Mine water','Engineered\
    \ > Wastewater > Industrial wastewater']:\n    row=next(r for r in rows if r['canonical_path']==path);ident=s.mint('GOLD',path)\n\
    \    auto=s.resolve_gold(row,ont,mapping,s.leaf_claimants(rows),s.composed_claimants(rows))\n\
    \    print('ROUTE',json.dumps({'path':path,'mint':ident,'automatic':asdict(auto),'final':asdict(s.apply_decision(auto,ident,decisions))}))\n\
    c=next(c for c in s.build_corpus().concepts if c.identifier=='habitatmech:GOLD.6a0644fced')\n\
    assert s.build_document(c)==yaml.safe_load(Path('data/habitats/engineered/mine_water.yaml').read_text())\n\
    print('WHOLE_DOCUMENT_EQUAL',c.source_concepts,c.reviewed_sources)\nPY"
  exit_code: 0
- check_id: corpus
  name: Exact corpus reproduction
  status: passed
  required: true
  summary: 3,208 expected and present; zero missing, extra or differing records.
  target_ids:
  - habitatmech:GOLD.6a0644fced
  command: env UV_CACHE_DIR=build/uv-cache just verify-corpus
  exit_code: 0
- check_id: history
  name: Native append-only history validation
  status: passed
  required: true
  summary: 220 valid history records.
  target_ids:
  - habitatmech:GOLD.6a0644fced
  command: env UV_CACHE_DIR=build/uv-cache just validate-history
  exit_code: 0
- check_id: provenance
  name: Frozen inventory manifests
  status: passed
  required: true
  summary: All 14 inventories and two GOLD-source manifests current.
  target_ids:
  - habitatmech:GOLD.6a0644fced
  command: env UV_CACHE_DIR=build/uv-cache just provenance-check
  exit_code: 0
- check_id: references
  name: Focused existing corpus-integrity regressions
  status: passed
  required: true
  summary: 6 passed, 33 deselected in 24.55 seconds.
  target_ids:
  - habitatmech:GOLD.6a0644fced
  command: env UV_CACHE_DIR=build/uv-cache uv run pytest -q tests/test_corpus_integrity.py
    -k 'parent or reviewed_records or history or causal_edges_reference'
  exit_code: 0
- check_id: bulk-original
  name: Current public GOLD exact-path scan
  status: passed
  required: false
  summary: 'Completed scan: 70 biosamples, nine organisms, 85 linked sequencing projects
    and 13 study IDs. Initial stdout was truncated; the separate contact-free replay
    below supplied the complete compact crosswalk.'
  target_ids:
  - habitatmech:GOLD.6a0644fced
  command: "env UV_CACHE_DIR=build/uv-cache uv run python -u - <<'PY'\nfrom pathlib\
    \ import Path\nimport collections,hashlib,json,zipfile\nfrom scripts.extract_gold_biosamples\
    \ import rows\np=Path('/private/tmp/habitatmech-20261009h-goldData.xlsx')\nwith\
    \ p.open('rb') as f:\n    assert hashlib.file_digest(f,'sha256').hexdigest()=='5f48b2f50fb2a9257754960a0f0e12dc6e8fa121e97c3e9f4497249e5fe6e439'\n\
    path='Engineered > Wastewater > Industrial wastewater > Mine water'\nbs={};org={};links=[]\n\
    with zipfile.ZipFile(p) as z:\n    for sheet,prefix,start,dest in [('sheet3','BIOSAMPLE',10,bs),('sheet4','ORGANISM',26,org)]:\n\
    \        for n,c in enumerate(rows(z,f'xl/worksheets/{sheet}.xml')):\n       \
    \     if n==0:\n                h=c;continue\n            this=' > '.join(v for\
    \ v in c[start:start+5] if v and v!='Unclassified')\n            if this==path:\n\
    \                row=dict(zip(h,c));dest[c[0]]=row\n                keep=[k for\
    \ k in row if any(t in k for t in ('GOLD ID','NAME','COLLECTION SITE','ECOSYSTEM','ISOLATION\
    \ PUBMED','HABITAT'))]\n                print(prefix,json.dumps({k:row[k] for\
    \ k in keep}),flush=True)\n        print('SCANNED',sheet,n+1,'MATCHES',len(dest),flush=True)\n\
    \    for n,c in enumerate(rows(z,'xl/worksheets/sheet5.xml')):\n        if n==0:h=c;continue\n\
    \        row=dict(zip(h,c))\n        if row.get('BIOSAMPLE GOLD ID') in bs or\
    \ row.get('ORGANISM GOLD ID') in org:\n            keys=['PROJECT GOLD ID','PROJECT\
    \ NAME','STUDY GOLD ID','ORGANISM GOLD ID','BIOSAMPLE GOLD ID','NCBI BIOPROJECT\
    \ ACCESSION','NCBI BIOSAMPLE ACCESSION','SRA EXPERIMENT IDS','PROJECT GENOME PUBLICATION\
    \ PUBMED ID','PROJECT OTHER PUBLICATION PUBMED ID']\n            links.append({k:row.get(k,'')\
    \ for k in keys})\n    print('SCANNED_PROJECTS',n+1)\n    studies={r['STUDY GOLD\
    \ ID'] for r in links if r['STUDY GOLD ID']}\n    for n,c in enumerate(rows(z,'xl/worksheets/sheet2.xml')):\n\
    \        if n==0:h=c;continue\n        if c and c[0] in studies:\n           \
    \ print('STUDY',json.dumps(dict(zip(h,c))))\nprint('LINKS',json.dumps(links))\n\
    print('SUMMARY',json.dumps({'biosamples':len(bs),'organisms':len(org),'projects':len(links),'studies':sorted(studies),'biosamples_without_project':sorted(set(bs)-{r['BIOSAMPLE\
    \ GOLD ID'] for r in links}),'organisms_without_project':sorted(set(org)-{r['ORGANISM\
    \ GOLD ID'] for r in links})}))\nPY"
  exit_code: 0
- check_id: bulk-compact
  name: Complete contact-free GOLD sample/project/study replay
  status: passed
  required: false
  summary: Inspected all 70 sample names/sites, 85 project crosswalk rows and all
    13 study names/descriptions. Six studies have exact-path biosamples (1+5+15+5+14+30);
    seven are organism-only. All 70 biosample and nine organism IDs join to projects.
  target_ids:
  - habitatmech:GOLD.6a0644fced
  command: "env UV_CACHE_DIR=build/uv-cache uv run python -u - <<'PY'\nimport collections,json,zipfile\n\
    from lxml import etree as E\nNS='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'\n\
    path='Engineered > Wastewater > Industrial wastewater > Mine water'\ndef sheet(z,name):\n\
    \    with z.open('xl/worksheets/'+name+'.xml') as f:\n        for _,elem in E.iterparse(f,events=('end',),tag=NS+'row'):\n\
    \            out=[]\n            for c in elem.findall(NS+'c'):\n            \
    \    t=c.find(NS+'is/'+NS+'t');v=c.find(NS+'v')\n                out.append((t.text\
    \ if t is not None else v.text if v is not None else '') or '')\n            yield\
    \ out\n            elem.clear()\n            while elem.getprevious() is not None:del\
    \ elem.getparent()[0]\nbs={};org={'Go0000121','Go0006917','Go0013366','Go0035556','Go0037571','Go0044073','Go0047507','Go0050683','Go0509422'};links=[]\n\
    with zipfile.ZipFile('/private/tmp/habitatmech-20261009h-goldData.xlsx') as z:\n\
    \    for n,c in enumerate(sheet(z,'sheet3')):\n        if n and ' > '.join(x for\
    \ x in c[10:15] if x and x!='Unclassified')==path:\n            bs[c[0]]={'name':c[1],'site':c[4],'path_id':c[9]}\n\
    \    print('BIOSAMPLE_SCAN',n+1,len(bs))\n    for n,c in enumerate(sheet(z,'sheet5')):\n\
    \        if n==0:h=c;continue\n        r=dict(zip(h,c))\n        if r.get('BIOSAMPLE\
    \ GOLD ID') in bs or r.get('ORGANISM GOLD ID') in org:\n            keys=['PROJECT\
    \ GOLD ID','STUDY GOLD ID','ORGANISM GOLD ID','BIOSAMPLE GOLD ID','NCBI BIOPROJECT\
    \ ACCESSION','NCBI BIOSAMPLE ACCESSION','PROJECT GENOME PUBLICATION PUBMED ID']\n\
    \            links.append({k:r.get(k,'') for k in keys})\n    print('PROJECT_SCAN',n+1,len(links))\n\
    \    groups=collections.defaultdict(list)\n    for r in links:groups[r['STUDY\
    \ GOLD ID']].append(r)\n    for n,c in enumerate(sheet(z,'sheet2')):\n       \
    \ if n and c[0] in groups:print('STUDY_TEXT',json.dumps({'id':c[0],'name':c[1],'description':c[2]}))\n\
    for sid,rs in sorted(groups.items()):\n    ids=sorted({r['BIOSAMPLE GOLD ID']\
    \ for r in rs if r['BIOSAMPLE GOLD ID']})\n    organisms=sorted({r['ORGANISM GOLD\
    \ ID'] for r in rs if r['ORGANISM GOLD ID']})\n    print('GROUP',json.dumps({'study':sid,'biosamples':ids,'organisms':organisms,'projects':len(rs),'collection_contexts':sorted({bs[b]['site']\
    \ for b in ids}),'public_projects':sorted({r['NCBI BIOPROJECT ACCESSION'] for\
    \ r in rs if r['NCBI BIOPROJECT ACCESSION']})}))\n    print('CROSSWALK',json.dumps([[r[k]\
    \ for k in ['PROJECT GOLD ID','ORGANISM GOLD ID','BIOSAMPLE GOLD ID','NCBI BIOSAMPLE\
    \ ACCESSION','PROJECT GENOME PUBLICATION PUBMED ID']] for r in rs]))\nprint('ALL70_NAMES',json.dumps(bs))\n\
    assert set(bs)=={r['BIOSAMPLE GOLD ID'] for r in links if r['BIOSAMPLE GOLD ID']}\n\
    assert org=={r['ORGANISM GOLD ID'] for r in links if r['ORGANISM GOLD ID']}\n\
    print('COMPLETE_CROSSWALK',len(bs),len(org),len(links),len(groups))\nPY"
  exit_code: 0
- check_id: ols-initial
  name: Initial sandbox OLS request
  status: failed
  required: false
  summary: DNS failure; no ontology response obtained in this attempt. The separately
    recorded authorized retry succeeded.
  target_ids:
  - habitatmech:GOLD.6a0644fced
  command: "env UV_CACHE_DIR=build/uv-cache uv run python -u - <<'PY'\nimport hashlib,json,urllib.parse,urllib.request\n\
    for ident in ['ENVO_01000964','ENVO_00001996','ENVO_00001997','ENVO_00002112']:\n\
    \    url='https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?'+urllib.parse.urlencode({'iri':'http://purl.obolibrary.org/obo/'+ident})\n\
    \    b=urllib.request.urlopen(url,timeout=45).read();j=json.loads(b)\n    print('TERM',url,len(b),hashlib.sha256(b).hexdigest(),json.dumps(j))\n\
    url='https://www.ebi.ac.uk/ols4/api/search?'+urllib.parse.urlencode({'q':'mine\
    \ water','ontology':'envo','rows':20,'type':'class'})\nb=urllib.request.urlopen(url,timeout=45).read();j=json.loads(b)\n\
    print('SEARCH',url,len(b),hashlib.sha256(b).hexdigest(),json.dumps(j))\nPY"
  exit_code: 1
- check_id: ols
  name: Current official ontology identities and bounded candidate search
  status: passed
  required: true
  summary: Authorized retry inspected industrial wastewater, mine drainage, acid mine
    drainage and gold mine drainage; all active. Search returned 26 hits, first 20
    inspected only.
  target_ids:
  - habitatmech:GOLD.6a0644fced
  command: "env UV_CACHE_DIR=build/uv-cache uv run python -u - <<'PY'\nimport hashlib,json,urllib.parse,urllib.request\n\
    for ident in ['ENVO_01000964','ENVO_00001996','ENVO_00001997','ENVO_00002112']:\n\
    \    url='https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?'+urllib.parse.urlencode({'iri':'http://purl.obolibrary.org/obo/'+ident})\n\
    \    b=urllib.request.urlopen(url,timeout=45).read();j=json.loads(b)\n    print('TERM',url,len(b),hashlib.sha256(b).hexdigest(),json.dumps(j))\n\
    url='https://www.ebi.ac.uk/ols4/api/search?'+urllib.parse.urlencode({'q':'mine\
    \ water','ontology':'envo','rows':20,'type':'class'})\nb=urllib.request.urlopen(url,timeout=45).read();j=json.loads(b)\n\
    print('SEARCH',url,len(b),hashlib.sha256(b).hexdigest(),json.dumps(j))\nPY"
  exit_code: 0
- check_id: primary-initial
  name: Initial primary abstract and full-text attempt
  status: failed
  required: false
  summary: Read PMID 12807207 and PMID 10049886 abstracts. PMC91167 fullTextXML returned
    HTTP 500 and exited 1; subsequent requested abstracts did not execute in this
    call.
  target_ids:
  - habitatmech:GOLD.6a0644fced
  command: "env UV_CACHE_DIR=build/uv-cache uv run python -u - <<'PY'\nimport urllib.request,urllib.parse,json,hashlib,xml.etree.ElementTree\
    \ as ET\nfor pmid in ['12807207','10049886','11491320','22115438']:\n    url='https://www.ebi.ac.uk/europepmc/webservices/rest/search?'+urllib.parse.urlencode({'query':'EXT_ID:'+pmid+'\
    \ AND SRC:MED','format':'json','resultType':'core'})\n    b=urllib.request.urlopen(url,timeout=45).read();j=json.loads(b)\n\
    \    print('PAPER',pmid,len(b),hashlib.sha256(b).hexdigest())\n    for r in j['resultList']['result']:\n\
    \        print(json.dumps({k:r.get(k) for k in ['id','pmcid','doi','title','authorString','pubYear','abstractText']}))\n\
    \        if pmid=='10049886' and r.get('pmcid'):\n            url='https://www.ebi.ac.uk/europepmc/webservices/rest/'+r['pmcid']+'/fullTextXML'\n\
    \            x=urllib.request.urlopen(url,timeout=45).read();root=ET.fromstring(x)\n\
    \            print('FULLTEXT',url,len(x),hashlib.sha256(x).hexdigest())\n    \
    \        for sec in root.findall('.//sec'):\n                title=sec.findtext('title','')\n\
    \                if any(t in title.lower() for t in ('site','sample','water','geochem')):\n\
    \                    print('SECTION',title,' '.join(sec.itertext())[:18000])\n\
    PY"
  exit_code: 1
- check_id: primary-retry
  name: Remaining primary abstracts and PMC metadata retry
  status: passed
  required: false
  summary: Read PMID 11491320 and PMID 22115438 abstracts. NCBI PMC91167 XML was metadata
    only despite the diagnostic print label FULLTEXT; it supplied no body/methods.
  target_ids:
  - habitatmech:GOLD.6a0644fced
  command: "env UV_CACHE_DIR=build/uv-cache uv run python -u - <<'PY'\nimport urllib.request,urllib.parse,json,hashlib,xml.etree.ElementTree\
    \ as ET\nfor pmid in ['11491320','22115438']:\n    url='https://www.ebi.ac.uk/europepmc/webservices/rest/search?'+urllib.parse.urlencode({'query':'EXT_ID:'+pmid+'\
    \ AND SRC:MED','format':'json','resultType':'core'})\n    b=urllib.request.urlopen(url,timeout=45).read();j=json.loads(b)\n\
    \    print('PAPER',pmid,len(b),hashlib.sha256(b).hexdigest())\n    for r in j['resultList']['result']:\n\
    \        print(json.dumps({k:r.get(k) for k in ['id','pmcid','doi','title','authorString','pubYear','abstractText']}))\n\
    url='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=91167'\n\
    b=urllib.request.urlopen(url,timeout=60).read();root=ET.fromstring(b)\nprint('FULLTEXT',url,len(b),hashlib.sha256(b).hexdigest())\n\
    for sec in root.findall('.//sec'):\n    title=sec.findtext('title','')\n    if\
    \ any(t in title.lower() for t in ('site','sample','water','geochem')):\n    \
    \    print('SECTION',title,' '.join(sec.itertext())[:18000])\nPY"
  exit_code: 0
- check_id: pmc-body
  name: Explicit metadata-versus-full-text check
  status: passed
  required: false
  summary: PMC91167 efetch response contains one article, zero sections and no body.
    Correct identity metadata does not certify a full-text inspection.
  target_ids:
  - habitatmech:GOLD.6a0644fced
  command: 'env UV_CACHE_DIR=build/uv-cache uv run python - <<''PY''

    import urllib.request,xml.etree.ElementTree as ET

    u=''https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=91167''

    r=ET.fromstring(urllib.request.urlopen(u,timeout=45).read())

    print(''ROOT'',r.tag,''ARTICLES'',len(r.findall(''.//article'')),''SECTIONS'',len(r.findall(''.//sec'')))

    print(''ARTICLE_IDS'',[(x.attrib,x.text) for x in r.findall(''.//article-id'')])

    print(''BODY'','' ''.join(r.find(''.//body'').itertext()) if r.find(''.//body'')
    is not None else ''No body'')

    print(''TITLES'',[x.text for x in r.findall(''.//article-title'')])

    PY'
  exit_code: 0
- check_id: ena
  name: Exact public sample metadata cross-check
  status: passed
  required: false
  summary: 'All three exact sample accessions resolved: sediment in a mine-tailing
    pool; thiosulfate-fed enrichment from a mine-wastewater reservoir; DSM 15120 isolated
    from subsurface hot aquifer water.'
  target_ids:
  - habitatmech:GOLD.6a0644fced
  command: "env UV_CACHE_DIR=build/uv-cache uv run python - <<'PY'\nimport hashlib,\
    \ urllib.request, xml.etree.ElementTree as E\nfor accession in ['SAMEA3904894','SAMN06612095','SAMN02769639']:\n\
    \    url='https://www.ebi.ac.uk/ena/browser/api/xml/'+accession\n    data=urllib.request.urlopen(url,timeout=45).read()\n\
    \    root=E.fromstring(data)\n    print(accession,url,len(data),hashlib.sha256(data).hexdigest())\n\
    \    for sample in root.findall('.//SAMPLE'):\n        print('TITLE',sample.findtext('TITLE'))\n\
    \        for attr in sample.findall('.//SAMPLE_ATTRIBUTE'):\n            print(attr.findtext('TAG'),':',attr.findtext('VALUE'))\n\
    PY"
  exit_code: 0
- check_id: web-routes
  name: Optional web fetch routes
  status: unavailable
  required: false
  summary: Web opens of exact OLS endpoints were unavailable. PMC pages yielded reCAPTCHA
    only. Official structured OLS and abstract APIs succeeded independently; no full-text
    methods claimed.
  target_ids:
  - habitatmech:GOLD.6a0644fced
- check_id: unchanged
  name: Captured hashes and exact base-tree equality
  status: passed
  required: true
  summary: All 41 captured SHA-256 values still match, and every input equals its
    bytes at the original Git base.
  target_ids:
  - habitatmech:GOLD.6a0644fced
  command: "env UV_CACHE_DIR=build/uv-cache uv run python - <<'PY'\nimport hashlib,json,subprocess\n\
    from pathlib import Path\ninputs=json.loads(\"[{\\\"path\\\":\\\".claude/skills/curate-yaml-record/references/review-checklist.md\\\
    \",\\\"sha256\\\":\\\"4544b5d2c11fbbb3a46cd8a65f7e664363df78c1000c590aab533219f9eec59b\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\".claude/skills/review-yaml-record/SKILL.md\\\
    \",\\\"sha256\\\":\\\"d429c8bb74f521df9a77a90b216a44fc6959ee28efb1fa17a93582536caa8bce\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"CLAUDE.md\\\",\\\"sha256\\\"\
    :\\\"98d95f910ff5160bc5b2ff572766785519dacdba487700bebaa6dbf96d071fd9\\\",\\\"\
    role\\\":\\\"context\\\"},{\\\"path\\\":\\\"conf/record_review.yaml\\\",\\\"sha256\\\
    \":\\\"c2f5d0eb4c5744f5fe354c92184ddab144dc2688dba952b032b4f3d597bc08d6\\\",\\\
    \"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"conf/sources.yaml\\\",\\\"sha256\\\
    \":\\\"a8e069f9278068b57fa234f43e03c8d893f857827b83fd10cfa92d6815aed642\\\",\\\
    \"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"curation/decisions.tsv\\\",\\\"\
    sha256\\\":\\\"0602cca13e6495da256a6f1cfd5897462f73f9739a729447862017d93c148efd\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"curation/gold_parent_exclusions.tsv\\\
    \",\\\"sha256\\\":\\\"9d2324647d0a0ddeccc2f7836811872e112af208bb1b8f7decb332c00f17d12b\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"curation/term_requests.tsv\\\
    \",\\\"sha256\\\":\\\"9977e384b79128d6e89c85f28e35c77d29644d503dea6d53c12628599e33f7f3\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"curation/term_requests_excluded.tsv\\\
    \",\\\"sha256\\\":\\\"36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"data/habitats/PATHS.tsv\\\"\
    ,\\\"sha256\\\":\\\"b59b9e800a918135e3915145d4d8098bb48dcea36a312b3004c594a57d221ae9\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"data/habitats/RETIRED.tsv\\\
    \",\\\"sha256\\\":\\\"41beffc45aabdf304de633c21200b375d7f01d1cb2e036d4a026961d545a35e5\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"data/habitats/engineered/industrial_wastewater.yaml\\\
    \",\\\"sha256\\\":\\\"07698df721a169cd55c2d1ce80027df8c8a3140536ba99eee312272887ce8768\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"data/habitats/engineered/mine_water.yaml\\\
    \",\\\"sha256\\\":\\\"c285eed1f2bc078931182954bb1f290d8e0a7c05cc5940fbac9509503ef6b38c\\\
    \",\\\"role\\\":\\\"target\\\"},{\\\"path\\\":\\\"data/raw/GOLD_MANIFEST.yaml\\\
    \",\\\"sha256\\\":\\\"99ec487ae02d512cfb75440685f927abe907effe52cb755feb095631e8841489\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"data/raw/MANIFEST.yaml\\\"\
    ,\\\"sha256\\\":\\\"4657672d429be35e551ceef4a1204ab0a8120558ce63e2a2b74188eee94b8480\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"data/raw/bacdive_isolation_sources.tsv\\\
    \",\\\"sha256\\\":\\\"fb1645dd899a43130be9cf38b0e8b27ffbaa0175306917bff20e20ee225875fc\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"data/raw/bacdive_source_taxa.tsv\\\
    \",\\\"sha256\\\":\\\"08471c12f887882e2a6af8f078166b1f59ed7e2b24eb7edbe43a7fc77dfbad44\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"data/raw/environment_parameters.tsv\\\
    \",\\\"sha256\\\":\\\"a75d0f565d8ee2498188ff98b17d0ab325ae4f782601bf4414eff6e86c13e0f9\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"data/raw/gold_ecosystem_paths.tsv\\\
    \",\\\"sha256\\\":\\\"5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"data/raw/gold_path_biosamples.tsv\\\
    \",\\\"sha256\\\":\\\"97cd7c8d0e731d07a85db6986dbcf9e49096a3c7988bd90a855599f492fe619e\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"data/raw/gold_path_triads.tsv\\\
    \",\\\"sha256\\\":\\\"b1717bd8fc4fdcd6a1a132f4eb32df3638b01ddf7d78f9a5797f110ee2b1e8d6\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"data/raw/gold_studies.tsv\\\
    \",\\\"sha256\\\":\\\"fa7aaa46f288d10c453bb723e6cf486cde646a003559414b5523cc3883a84c8c\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"data/raw/isolation_source_groundings.tsv\\\
    \",\\\"sha256\\\":\\\"ab6a997359aab961c40928f9b13e06adb6dc43124fa3de821819570dd87f43b8\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"data/raw/madin_habitat_taxa.tsv\\\
    \",\\\"sha256\\\":\\\"d30854cfcffca0405914d04071ac47053938d354d5df250125843131b7c91fd7\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"data/raw/madin_habitats.tsv\\\
    \",\\\"sha256\\\":\\\"2ae1756f40242600365c49bfbdada4bce5fc8b86630426bb34892f055e5a5c93\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"data/raw/ontology_subclass_edges.tsv\\\
    \",\\\"sha256\\\":\\\"b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"data/raw/ontology_terms.tsv\\\
    \",\\\"sha256\\\":\\\"7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"data/raw/prego_habitat_taxa.tsv\\\
    \",\\\"sha256\\\":\\\"26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"data/raw/prego_habitats.tsv\\\
    \",\\\"sha256\\\":\\\"07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"docs/CURATION.md\\\",\\\"sha256\\\
    \":\\\"36df8306394c06c352b73e0bf7b47a2858784cedac7389a24d0b78f593ece646\\\",\\\
    \"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"docs/HARMONIZATION.md\\\",\\\"sha256\\\
    \":\\\"ee39d3cd29115ee14f5e7386169c76c47d471ebdc2502c008c49d30fb44918f1\\\",\\\
    \"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"docs/RESEARCH.md\\\",\\\"sha256\\\
    \":\\\"82c5471890d310bf8fd33141d5596f847bfc1eb6091c2db6f485388435e067af\\\",\\\
    \"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"docs/record-review-profile.md\\\"\
    ,\\\"sha256\\\":\\\"f7aa39ee762d94f1902d9f08f328cb897bc543e4e226057eb4770d24bfcc6eb5\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"docs/record-reviews.md\\\"\
    ,\\\"sha256\\\":\\\"452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"justfile\\\",\\\"sha256\\\"\
    :\\\"e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14\\\",\\\"\
    role\\\":\\\"context\\\"},{\\\"path\\\":\\\"reports/yaml_record_review/20260926T173701Z-mine_water__20810f85.md\\\
    \",\\\"sha256\\\":\\\"27d5a4bd2403e9d7780d97a382d93441af29afa94d6e27d7c2566aafd648e9b6\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"schema/record_review.yaml\\\
    \",\\\"sha256\\\":\\\"229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"scripts/extract_gold_biosamples.py\\\
    \",\\\"sha256\\\":\\\"b6a2773c86fe718e1ca0b1d7b32709f0eee491ac813655e310aa0817c0fec31b\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"src/habitatmech/extract.py\\\
    \",\\\"sha256\\\":\\\"4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"src/habitatmech/schema/habitatmech.yaml\\\
    \",\\\"sha256\\\":\\\"52d2a22309a1f4a10728a663560bb4d918346c292221fd34139b99b4159d3fe5\\\
    \",\\\"role\\\":\\\"context\\\"},{\\\"path\\\":\\\"src/habitatmech/seed.py\\\"\
    ,\\\"sha256\\\":\\\"92adf631fa099120a497ff7001473e659347d23ac9b418f04cd341ddad5d2a89\\\
    \",\\\"role\\\":\\\"context\\\"}]\")\nfor item in inputs:\n    b=Path(item['path']).read_bytes()\n\
    \    assert hashlib.sha256(b).hexdigest()==item['sha256'],item['path']\n    assert\
    \ b==subprocess.check_output(['git','show','016bfc2de4301e13930d5701a03c016cc150295f:'+item['path']]),item['path']\n\
    print('UNCHANGED_CAPTURE_AND_BASE',len(inputs),'016bfc2de4301e13930d5701a03c016cc150295f')\n\
    PY"
  exit_code: 0
- check_id: baseline-qc
  name: Fresh exact-baseline full-QC receipt
  status: passed
  required: true
  summary: Completed success at exact base 016bfc2de4301e13930d5701a03c016cc150295f.
    Actual logs inspected during preceding publication showed 646 passed, three skipped
    (422.98 seconds), plus all native QC gates. Reused because scientific inputs are
    byte-identical; this is not a fresh local full-QC run.
  target_ids:
  - habitatmech:GOLD.6a0644fced
  command: gh run view 37941486985 --json status,conclusion,headSha,url
  exit_code: 0
- check_id: baseline-labels
  name: Fresh exact-baseline ontology-label receipt
  status: passed
  required: true
  summary: Completed success at exact same base. No new global ontology download or
    full local validate-products run; target parent and candidate term definitions
    were additionally inspected live.
  target_ids:
  - habitatmech:GOLD.6a0644fced
  command: gh run view 37941486962 --json status,conclusion,headSha,url
  exit_code: 0
- check_id: causal
  name: Target causal-overlay and molecular applicability
  status: not_applicable
  required: false
  summary: No causal graph, causal overlay, genes, regulators, proteins, expression
    datasets or characteristic-taxon claims on this target. Target-specific causal
    and iModulonDB assessment not applicable, not negative biological evidence.
  target_ids:
  - habitatmech:GOLD.6a0644fced
evidence:
- evidence_id: record
  kind: record_content
  reference: data/habitats/engineered/mine_water.yaml
  locator: Entire file; PATHS.tsv physical line 2062
  accessed_at: '2026-10-09T14:34:53Z'
  support: supports
  summary: Minted Mine water, ENGINEERED, UNGROUNDED, SEEDED; sole parent ENVO:01000964;
    one GOLD attestation with 14 ORGANISM occurrences and two collapsed nodes; CLASS
    history plus seed history. No authored definition, taxa, parameters, xrefs or
    causal graph.
  snapshot_sha256: c285eed1f2bc078931182954bb1f290d8e0a7c05cc5940fbac9509503ef6b38c
- evidence_id: frozen
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Logical row 475, exact canonical path; data/raw/gold_path_biosamples.tsv
    logical row 300; gold_studies.tsv logical rows 1258,1508,1706,1933,2289,4541
  accessed_at: '2026-10-09T14:34:53Z'
  support: supports
  summary: Engineered > Wastewater > Industrial wastewater > Mine water collapses
    nodes 3839 and 4270, preserving first-node attestation 3839 and 14 ORGANISM occurrences.
    Separate bulk inventory has 70 biosamples on 4270 and six study IDs. Zero study/biosample
    counters in the older KGX-derived row are not evidence that no samples exist.
- evidence_id: decision
  kind: record_content
  reference: curation/decisions.tsv
  locator: Physical line 630, habitatmech:GOLD.6a0644fced
  accessed_at: '2026-10-09T14:34:53Z'
  support: supports
  summary: CONFIRM_UNGROUNDED at CLASS depth explicitly leaves habitat meaning unassessed.
    It does not endorse a strict parent or promote mapping_status to REVIEWED.
- evidence_id: generation
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: resolve_gold and ingest_gold; actual route/reconstruction check; src/habitatmech/extract.py
    lines 123-242
  accessed_at: '2026-10-09T14:34:53Z'
  support: supports
  summary: The immediate GOLD path parent supplies ENVO:01000964 via the parent's
    automatic gold_leaf_label route. Count extraction aggregates Go occurs_in edges
    by collapsed source path; it is not a count of current public-workbook unique
    organisms. Exact source mint and complete target reconstruction agree.
- evidence_id: rules
  kind: authority
  reference: docs/CURATION.md
  locator: Decision model; curated definitions and hierarchy; CLAUDE.md semantic invariants;
    native checklist
  accessed_at: '2026-10-09T14:34:53Z'
  support: supports
  summary: All parent contributions must express a strict broader class, not a sampled
    setting. Source association and native validation alone cannot certify identity.
    Optional fields and CLASS status alone are not major findings.
- evidence_id: parent
  kind: record_content
  reference: data/habitats/engineered/industrial_wastewater.yaml
  locator: Entire context record, ENVO:01000964
  accessed_at: '2026-10-09T14:34:53Z'
  support: context_only
  summary: Parent describes industrially produced wastewater with non-fecal chemical
    contaminants. Its existence and automatic exact grounding do not prove every descendant
    path has the same material scope. This is not a complete scientific review of
    the parent.
- evidence_id: bulk
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=site_excel
  locator: Oct 9 public workbook, 238974789 bytes; sheets 2-5; exact path and source
    IDs 4270 / Go0000121,Go0006917,Go0013366,Go0035556,Go0037571,Go0044073,Go0047507,Go0050683,Go0509422
  accessed_at: '2026-10-09T14:34:53Z'
  support: partial
  summary: 'Current exact-path membership is 70 biosamples and nine organisms, joined
    through 85 sequencing projects to 13 studies. Biosample study counts: Gs0121252=1,
    Gs0128962=5, Gs0132928=15, Gs0133347=5, Gs0141931=14, Gs0164315=30. Source metadata
    includes drainage/runoff, tailings waters, sediment, enrichments, natural deep
    aquifer/fissure water and treatment-bed isolates. This is newer contextual evidence,
    not the frozen KGX membership or the August GOLD_MANIFEST snapshot.'
  snapshot_sha256: 5f48b2f50fb2a9257754960a0f0e12dc6e8fa121e97c3e9f4497249e5fe6e439
- evidence_id: bulk-contexts
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=site_excel
  locator: Exact-path sample and organism rows; compact crosswalk checks
  accessed_at: '2026-10-09T14:34:53Z'
  support: partial
  summary: All 70 sample names/sites and all nine organism contexts were inspected.
    Gs0132928 contains three thiosulfate enrichments plus runoff/reservoir/discharge
    samples; Gs0133347 contains five sediment samples; only 14 exact-path samples
    are used from multipath Gs0141931. Go0013366 is DSM 15120 from a hot aquifer;
    Go0006917 is SA-01 from deep groundwater; Go0047507 and Go0050683 are treatment-bed
    fungal isolates. These are source usages, not characteristic taxa or proof that
    upstream classification is correct.
- evidence_id: envo-industrial
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01000964
  locator: ENVO:01000964 industrial wastewater; identifier, label, definition, obsolete
    flag and synonyms inspected
  accessed_at: '2026-10-09T14:34:53Z'
  support: context_only
  summary: Current active definition requires wastewater produced by industrial activity
    and containing non-fecal chemical contaminants. GOLD ancestry is not independent
    support for universal satisfaction of that definition.
  snapshot_sha256: e609beb090dee1884cb6fe465807aa17b3d8670094c7081afab060c827a94a95
- evidence_id: envo-drainage
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_00001996
  locator: ENVO:00001996 mine drainage; identifier, label, definition, obsolete flag
    and synonyms inspected
  accessed_at: '2026-10-09T14:34:53Z'
  support: context_only
  summary: Active outflow-of-water-from-mine concept. Related acid/metalliferous synonyms
    are not exact synonyms; source waters need not all be outflow features.
  snapshot_sha256: 4931f69b3c9b63a0bb71dbe8cbf5c1b613952aed7c26a5b788755cc6f43b9b2a
- evidence_id: envo-acid
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_00001997
  locator: ENVO:00001997 acid mine drainage; identifier, label, definition, obsolete
    flag and synonyms inspected
  accessed_at: '2026-10-09T14:34:53Z'
  support: context_only
  summary: Active mine-drainage concept requiring acidic pH. A subset of source samples
    labelled AMD does not establish universal acidity.
  snapshot_sha256: 8c8414401c14f99c8a65e27d7aa414b4a7516466803b7998bf72711c241d6d67
- evidence_id: envo-gold
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_00002112
  locator: ENVO:00002112 gold mine drainage; identifier, label, definition, obsolete
    flag and synonyms inspected
  accessed_at: '2026-10-09T14:34:53Z'
  support: context_only
  summary: Active gold-mining-qualified drainage concept. The target includes non-gold
    mining and other material contexts; it is not an exact substitute.
  snapshot_sha256: eaff9c4552919b1565b8e7282cdd4814cb0e8dc01f0178fe501cfb40a332f554
- evidence_id: ols-search
  kind: search
  reference: https://www.ebi.ac.uk/ols4/api/search?q=mine+water&ontology=envo&rows=20&type=class
  locator: First 20 of 26 hits
  accessed_at: '2026-10-09T14:34:53Z'
  support: context_only
  summary: No exact identity is established by this bounded tokenized search. Near
    mine-drainage candidates were read directly rather than discarded for label mismatch.
  snapshot_sha256: 779e08968afaa6ac4361a38d8f3bb5b73e074f47f6ec43c5c682c249768e2c79
  search_scope: Official ENVO class search for mine water, rows=20; not all 26 hits
    or all ontologies. No exhaustive term-absence claim.
- evidence_id: primary-aquifer
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12807207+AND+SRC%3AMED&format=json&resultType=core
  locator: PMID:12807207; DOI:10.1099/ijs.0.02506-0; bibliographic identity and complete
    abstract
  accessed_at: '2026-10-09T14:34:53Z'
  support: partial
  summary: Takai et al. 2003 abstract reports isolation from subsurface hot aquifer
    water in a Japanese gold mine. Type-strain aliases include DSM 15120, linking
    the paper to GOLD Go0013366. Supports collection context only, not absence of
    industrial contamination or a universal habitat definition.
  snapshot_sha256: a93a2534229f22463e2c67d6d980fa1a73a0444012c053ac29e7599af02c9244
- evidence_id: primary-thermus-isolation
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10049886+AND+SRC%3AMED&format=json&resultType=core
  locator: PMID:10049886; DOI:10.1128/aem.65.3.1214-1221.1999; bibliographic identity
    and complete abstract
  accessed_at: '2026-10-09T14:34:53Z'
  support: partial
  summary: Kieft et al. 1999 abstract reports SA-01 isolated from groundwater 3.2
    km deep in a South African gold mine. Matches GOLD Go0006917 strain context; full
    article methods were not recovered.
  snapshot_sha256: ce42344eab80902e35dc3894624affedbdd52628deb6c3b6cbe82c0d5bba93b8
- evidence_id: primary-alkaliphilus
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11491320+AND+SRC%3AMED&format=json&resultType=core
  locator: PMID:11491320; DOI:10.1099/00207713-51-4-1245; bibliographic identity and
    complete abstract
  accessed_at: '2026-10-09T14:34:53Z'
  support: partial
  summary: Takai et al. 2001 abstract reports isolation from a containment dam 3.2
    km deep in a South African gold mine, SAGM1=ATCC 700919, matching Go0044073. The
    workbook's 32 km string is not propagated; depth is not a target field.
  snapshot_sha256: addbf9855f9d02b6d42fdb5fe3156f59b8534082518f522ee7e0c5fb49f4309d
- evidence_id: primary-thermus-genome
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22115438+AND+SRC%3AMED&format=json&resultType=core
  locator: PMID:22115438; DOI:10.1186/1471-2164-12-577; bibliographic identity and
    complete abstract
  accessed_at: '2026-10-09T14:34:53Z'
  support: partial
  summary: Gounder et al. 2011 abstract identifies SA-01's fissure-water source at
    3.2 km depth. Corroborates bounded collection context; no genomic mechanism, culture
    optimum or phenotype is transferred to the habitat.
  snapshot_sha256: f5179bd396465f32eada3f3081ec61a5620bf923408ef12a21938f2a056222f3
- evidence_id: ena-sediment
  kind: database
  reference: https://www.ebi.ac.uk/ena/browser/api/xml/SAMEA3904894
  locator: Exact sample accession, title and complete sample attributes
  accessed_at: '2026-10-09T14:34:53Z'
  support: partial
  summary: GOLD Gp0289437/Gb0181570/Gs0133347 crosswalk resolves to a primary submitted
    sample with sediment material and mine-tailing-pool biome/feature. Demonstrates
    material-versus-setting distinction for this sample, not the entire category.
  snapshot_sha256: 9a00c16718bc59c5ee0660a115b6c57d22ecb88831a5a21b45a5098f916c2f76
- evidence_id: ena-enrichment
  kind: database
  reference: https://www.ebi.ac.uk/ena/browser/api/xml/SAMN06612095
  locator: Exact sample accession, title and complete sample attributes
  accessed_at: '2026-10-09T14:34:53Z'
  support: partial
  summary: GOLD Gp0272781/Gb0165115/Gs0132928 resolves to enrichment 3 from oxidation-reservoir
    shore water; isolation text retains mine wastewater. The enrichment can retain
    source context without becoming evidence that all members are natural waters.
  snapshot_sha256: 9c941a3b83d9d2e13521c7a5b4480746dd1dc710b0202337036211c688a49457
- evidence_id: ena-aquifer
  kind: database
  reference: https://www.ebi.ac.uk/ena/browser/api/xml/SAMN02769639
  locator: Exact sample accession, title and complete sample attributes
  accessed_at: '2026-10-09T14:34:53Z'
  support: partial
  summary: GOLD Gp0013366/Go0013366/Gs0015051 resolves to DSM 15120 with Japanese
    subsurface hot-aquifer-water isolation source. Independently corroborates the
    strain/source link; metadata does not establish industrial contamination absent
    or present.
  snapshot_sha256: 359a0d11a9db86d0afcfd84eca561ee6b200c42b704fdec24c30eea27008c1ed
- evidence_id: search-local
  kind: search
  reference: curation/; history/; research/; reports/; reviews/; data/habitats/PATHS.tsv
  locator: Ignored-inclusive exact identifier/path/slug search and filename search
  accessed_at: '2026-10-09T14:34:53Z'
  support: context_only
  summary: Recovered target decision/path, a child Sediment sample review, and the
    distinct groundwater Mine water historical report. No target-specific engineered
    Mine water report, overlay or novel definition recovered within these bounded
    roots.
  search_scope: rg --no-ignore --hidden -n 'GOLD\.6a0644fced|gold.ecosystem:3839|/mine_water\.yaml|Engineered
    > Wastewater > Industrial wastewater > Mine water' curation history research reports
    reviews data/habitats/PATHS.tsv; rg --no-ignore --hidden --files reports research
    reviews curation -g '*mine_water*' -g '*mine-water*'. Ignored files included.
    Not a claim of absence outside these roots.
- evidence_id: sibling
  kind: prior_review
  reference: reports/yaml_record_review/20260926T173701Z-mine_water__20810f85.md
  locator: Entire historical review, distinct habitatmech:GOLD.943d5cba70
  accessed_at: '2026-10-09T14:34:53Z'
  support: context_only
  summary: The groundwater sibling is not this engineered target. Its 206 biosamples,
    triad and proposed genus cannot be transferred. Its CLASS-based major rationale
    is not adopted here. No finding in that separate review is closed.
- evidence_id: validation
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/37941486985
  locator: Exact-base completed-success receipt; fresh target/corpus/history/reference/provenance
    checks
  accessed_at: '2026-10-09T14:34:53Z'
  support: supports
  summary: Structural reproducibility and native lifecycle checks pass. They do not
    establish scientific parent scope or independent scientific approval.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact source identity versus a single physical-material class
  outcome: concern
  summary: Mint and path are correct and the category contains actual microbial habitat
    observations. Current usage spans water materials, sampled solids, enrichment
    cultures and deep aquifer sources; the precise class denoted by the frozen source
    category remains unresolved. This is not evidence to mark the entire target NOT_APPLICABLE.
  target_ids:
  - habitatmech:GOLD.6a0644fced
  evidence_ids:
  - record
  - frozen
  - bulk
  - bulk-contexts
  - ena-sediment
  - ena-enrichment
  - ena-aquifer
- assessment_id: grounding
  area: grounding
  topic: Conservative ungrounded identity and near candidates
  outcome: supported
  summary: No supported exact replacement is established. Retain the minted identity
    and UNGROUNDED status pending source interpretation; mine drainage adds an outflow
    condition, acid mine drainage adds acidity, and gold mine drainage adds a mining
    qualifier not universal across the category.
  target_ids:
  - habitatmech:GOLD.6a0644fced
  evidence_ids:
  - decision
  - envo-drainage
  - envo-acid
  - envo-gold
  - bulk
- assessment_id: parent-scope
  area: graph
  topic: Strict industrial-wastewater parent
  outcome: concern
  summary: The parent is an automatic path projection, not an independently ITEM-endorsed
    genus. Submitted sample metadata and primary abstracts raise a material-versus-setting
    and natural-water-versus-wastewater concern. They do not alone prove the frozen
    category's intended scope or justify an automatic parent exclusion.
  target_ids:
  - habitatmech:GOLD.6a0644fced
  evidence_ids:
  - generation
  - parent
  - rules
  - envo-industrial
  - primary-aquifer
  - primary-thermus-isolation
  - ena-sediment
  - ena-enrichment
  - ena-aquifer
- assessment_id: attestations
  area: quantity
  topic: Source counts, units and snapshot separation
  outcome: supported
  summary: 14 ORGANISM occurrences over two collapsed KGX ecosystem nodes reproduce
    exactly. The separate 70-biosample inventory and current 9-organism/85-project
    crosswalk have different versions and units; they neither replace nor sum with
    14. Matching biosample totals do not prove identical historical membership.
  target_ids:
  - habitatmech:GOLD.6a0644fced
  evidence_ids:
  - record
  - frozen
  - generation
  - bulk
- assessment_id: native-status
  area: consistency
  topic: CLASS decision, SEEDED status and generated history
  outcome: supported
  summary: One CLASS decision and zero ITEM-reviewed contributing concepts correctly
    retain SEEDED. This review neither promotes scientific status nor appends a curation
    event. Missing optional fields and prior CLASS depth are not separate major findings.
  target_ids:
  - habitatmech:GOLD.6a0644fced
  evidence_ids:
  - record
  - decision
  - generation
  - rules
- assessment_id: definition
  area: completeness
  topic: Definition and novel-term readiness
  outcome: unknown
  summary: No authored target definition or novel-term request was recovered in the
    ignored-inclusive maintained-input search. Optional omission is not itself a defect.
    Scope must be resolved before choosing a genus, requesting a term or merging the
    groundwater sibling.
  target_ids:
  - habitatmech:GOLD.6a0644fced
  evidence_ids:
  - record
  - search-local
  - sibling
  - rules
- assessment_id: parameters
  area: scope
  topic: Environmental parameters, triad roles and culture conditions
  outcome: not_applicable
  summary: Target asserts no parameters or triad. No exact target-path row in the
    committed parameter/triad tables; this is not a statement that all source samples
    lack environmental metadata. Culture optima and acidity from individual studies
    are not universal habitat properties.
  target_ids:
  - habitatmech:GOLD.6a0644fced
  evidence_ids:
  - record
  - frozen
  - bulk
  - primary-aquifer
- assessment_id: taxa
  area: evidence
  topic: Taxa and mechanisms
  outcome: not_applicable
  summary: No target taxon associations or causal edges to validate. Current organism
    records identify source contexts only; no characteristic taxa, phylogenetic assertion
    or mechanistic claims were inferred. iModulonDB is not applicable.
  target_ids:
  - habitatmech:GOLD.6a0644fced
  evidence_ids:
  - record
  - bulk-contexts
- assessment_id: validation-ownership
  area: ownership
  topic: Generated ownership and deterministic gates
  outcome: supported
  summary: Whole-document reproduction, source/hash checks, schema and native gates
    pass. Any eventual fix belongs to maintained decisions and guarded parent exclusions
    or a supported definition, followed by native canary/regeneration/history and
    semantic product checks; never to generated YAML or pages.
  target_ids:
  - habitatmech:GOLD.6a0644fced
  evidence_ids:
  - generation
  - rules
  - validation
findings:
- finding_id: F1
  issue_key: mine-water-industrial-wastewater-source-scope
  category: scope
  severity: major
  status: open
  certainty: provisional
  title: Reconcile the strict industrial-wastewater genus with mixed GOLD source usage
  description: 'The sole parent_habitats edge asserts that this whole source-defined
    class is industrial wastewater. It comes from the GOLD path rather than a source-specific
    scientific endorsement. Current exact-path source usages include independently
    verified sediment, an enrichment culture, and a deep hot-aquifer isolate, alongside
    clear wastewater samples. These distinctions materially challenge a universal
    material identity, while not proving the upstream category wrong: sampling material
    may be inside a wastewater setting, and current membership is not the frozen KGX
    membership. Resolve the original category intent and member context before endorsing,
    replacing or excluding the parent. Do not infer that deep water was uncontaminated,
    that all members are mine drainage, or that the complete category is not a habitat.'
  target_ids:
  - habitatmech:GOLD.6a0644fced
  field_paths:
  - parent_habitats[0]
  - source_attestations[0].source_path
  evidence_ids:
  - record
  - generation
  - rules
  - envo-industrial
  - bulk
  - primary-aquifer
  - primary-thermus-isolation
  - ena-sediment
  - ena-enrichment
  - ena-aquifer
  rule_id: docs/CURATION.md#decision-model
  native_severity: major
  normalization_reason: An unresolved universal genus can materially inflate habitat
    identity/scope. Certainty remains provisional because source intent and frozen
    membership are incomplete; this is not a confirmed false is-a or a finding merely
    about missing optional fields.
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Exact GOLD.6a0644fced decision row
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Source-specific parent exclusions
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Any supported novel definition and genus
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Frozen GOLD path and count
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Generated record and hierarchy
actions:
- action_id: A1
  description: Recover the original GOLD category meaning and frozen organism-level
    sources; distinguish wastewater material, sampled setting, natural water, enrichment
    and upstream annotation error. Then make an evidence-backed ITEM decision and
    only those guarded hierarchy/definition changes the evidence warrants.
  finding_ids:
  - F1
  target_ids:
  - habitatmech:GOLD.6a0644fced
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Exact GOLD.6a0644fced decision row
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Source-specific parent exclusions
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Any supported novel definition and genus
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Frozen GOLD path and count
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Generated record and hierarchy
  generator: src/habitatmech/seed.py via just seed, just seed-canary habitatmech:GOLD.6a0644fced
    --force, then guarded regeneration only if inputs change
  acceptance_checks:
  - Document the exact historical source/path/node membership or its remaining recovery
    limit; keep 14 ORGANISM occurrences distinct from current organisms, biosamples
    and project counts.
  - Explain why ENVO:01000964 is strictly broader for the exact source concept, or
    support an exact-path gold_parent_exclusions.tsv row without suppressing independent
    ontology/curator parents. No exclusion solely because current sample material
    differs from a setting label.
  - Explicitly assess mine drainage and the distinct groundwater Mine water concept
    without an unsupported exact merge, universal acidity/gold-mining qualifier, arbitrary
    split, or NOT_APPLICABLE decision.
  - 'If scientific inputs change: append native history; add exact-source/edge regression
    coverage; dry-seed, force a target canary and inspect the entire output before
    guarded full regeneration. Do not hand-edit generated records or prune partial
    runs.'
  - Run target strict/schema, provenance/history, exact corpus reproduction, live
    label correspondence for any grounding change, genuine site/semantic-map/product
    refresh required by native change scope, and full just qc. Save a new linked immutable
    review retaining this issue_key and previous occurrence for any scientific disposition.
limitations:
- This is a completed scoped assessment with an unresolved provisional finding, not
  scientific approval of the record or completion of the 3,208-record corpus objective.
- Current Oct 9 GOLD workbook is not the frozen kg-microbe input or the Aug 20 GOLD_MANIFEST
  snapshot (SHA-256 6797471982570ed145f81aef966c1ff5398dc4d35287a01faefaf80ac5311fea).
  The original 14 occurrence memberships were not recovered.
- All 70 current sample contexts, nine organism contexts and 85 GOLD project links
  were inspected, but only three external sample accessions and four primary abstracts
  were independently cross-checked. Other source-provided BioProjects, BioSamples
  and publication IDs are context metadata, not independently validated claims.
- Primary isolation/genome abstracts support reported source context only. Europe
  PMC full-text retrieval failed; PMC web routes yielded reCAPTCHA; NCBI efetch supplied
  metadata without a body. No full methods, industrial-contamination absence, or universal
  habitat physiology is claimed.
- OLS candidate search inspected only its first 20 of 26 hits. Existing near terms
  are discussed directly; no exhaustive ontology term-absence conclusion or novel-term
  readiness is asserted.
- Full native QC and whole-corpus label checks are reused from verified exact-base
  CI receipts because all scientific inputs are unchanged. Fresh focused/schema/provenance/history/reproduction
  checks are recorded separately; receipt reuse is not a fresh local full QC run.
- Source category heterogeneity can reflect material-versus-setting roles or upstream
  annotation mistakes, not necessarily a genuinely heterogeneous intended class. The
  parent concern therefore remains provisional; no automatic curation is authorized
  by the report itself.
notes:
- Evidence accessed_at timestamps mark final inspection of the captured local inputs
  and retrieved responses during report construction on Oct 9. Public source retrievals
  occurred earlier the same session; no historical retrieval timestamp is invented.
- No generated record, curation input, history entry, source inventory, page, product
  or previous immutable review was changed. Public study contact fields are irrelevant
  and are not retained.
- No finding in a sibling review or existing GitHub issue is closed by this new observation.
tags:
- record-review
- engineered
- gold
- mine-water
- source-scope
```
