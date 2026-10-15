# Record review: ascites (BTO:0000091)

- Review: 20261015T075950Z-ascites-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T07:35:09Z
- Finished UTC: 2026-10-15T07:59:50Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

BTO fluid-accumulation meaning can support a sampled material context, but two exact Acinetobacter strain associations lack ascites support in their primary genome study. That study assigns BJAB07104 to blood, BJAB0715 to cerebrospinal fluid, and only BJAB0868 to ascites. Independent positive controls support other retained associations.

## Scope And Provenance

Scientific assessment of one exact generated target at captured main revision 23486ff2e685b41d486f25aad4719fd5b1549e4e.

Selection: Next twenty unreviewed records in corpus path order were selected; this document assesses only its single resolved identifier and source path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 23486ff2e685b41d486f25aad4719fd5b1549e4e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0000091 | data/habitats/host_associated/ascites.yaml | generated | ascites |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0000091 | Completed 2026-10-15T07:37:42Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/ascites.yaml |
| validate-strict | passed | True | BTO:0000091 | Completed 2026-10-15T07:38:15Z. uv run python scripts/validate_strict.py data/habitats/host_associated/arm_nodes.yaml data/habitats/host_associated/armpit_nodes.yaml data/habitats/host_associated/arterial.yaml data/habitats/host_associated/arterial_blood.yaml data/habitats/host_associated/arterial_ulcer.yaml data/habitats/host_associated/arthropoda_chelicerates.yaml data/habitats/host_associated/arthropoda_crustaceans.yaml data/habitats/host_associated/arthropoda_insects.yaml data/habitats/host_associated/arthropoda_myriapoda.yaml data/habitats/host_associated/articular_cartilage.yaml data/habitats/host_associated/articular_cartilage__2ad5f85b.yaml data/habitats/host_associated/ascending_colon.yaml data/habitats/host_associated/ascidian.yaml data/habitats/host_associated/ascidians.yaml data/habitats/host_associated/ascites.yaml data/habitats/host_associated/ascites__06c98a68.yaml data/habitats/host_associated/ascites__13be9a4c.yaml data/habitats/host_associated/ascites__f2c36f2c.yaml data/habitats/host_associated/atherosclerotic_plaque.yaml data/habitats/host_associated/athlete_s_foot.yaml<br>Validating 20 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      20<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | BTO:0000091 | Completed 2026-10-15T07:38:28Z. No issues found<br>759 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | BTO:0000091 | Completed 2026-10-15T07:38:29Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | BTO:0000091 | Completed 2026-10-15T07:38:55Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | BTO:0000091 | Completed 2026-10-15T07:39:04Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | BTO:0000091 | Completed 2026-10-15T07:39:37Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | BTO:0000091 | Completed 2026-10-15T07:41:13Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Baseline full native QC in CI | passed | True | BTO:0000091 | Authoritative quality gate and structured-review contract succeeded on the exact captured revision; status verified at 2026-10-15T07:57:35Z. https://github.com/CultureBotAI/HabitatMech/actions/runs/38698835390 |

## Scientific And Domain Assessments

### Native validity and reproduction

schema: supported. Targets: BTO:0000091.

Individual schema, strict twenty-target validation, 759 history records, 14 inventory/two GOLD provenance sources, exact 3,208-record reproduction, 32 causal overlays and 110 term requests passed. These deterministic checks do not prove scientific claims.

### Identity, definition, hierarchy and aliases

identity: concern. Targets: BTO:0000091.

BTO fluid-accumulation meaning can support a sampled material context, but two exact Acinetobacter strain associations lack ascites support in their primary genome study. That study assigns BJAB07104 to blood, BJAB0715 to cerebrospinal fluid, and only BJAB0868 to ascites. Independent positive controls support other retained associations.

### Source counts and retained ranking

quantity: supported. Targets: BTO:0000091.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks and pools: [{"source": "PREGO", "count": 5, "unit": "TAXON"}]. Zero counts are omitted; unrelated parent, bulk and study counts are not added. 5 retained taxon IDs were resolved against NCBI, including explicit aliases where noted.

### Parameters, mechanisms and native status

completeness: supported. Targets: BTO:0000091.

No causal edge or characteristic-presence claim is asserted. Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce SEEDED / EXACT; this review does not promote them.

## Findings

### F1: Two exact strain associations lack ascites support in the genome study

major / open / confirmed; issue key: ascites-strain-isolation-site-mismatch.

BJAB07104/NCBITaxon:1096995/CP003846.1 is blood-derived and BJAB0715/1096996/CP003847.1 is cerebrospinal-fluid-derived in the inspected primary methods. BJAB0868/1096997/CP003849.1 is the ascites isolate and must remain a supported control. Recover the original PREGO pair evidence and correct or qualify unsupported site assignments through a governed source contract; do not infer the exact upstream error, absence of every possible later occurrence, or manually decrement the pool. Preserve the separately supported Vibrio E0666 and Corynebacterium species associations.

## Recommended Actions And Acceptance Checks

### ACT1

BJAB07104/NCBITaxon:1096995/CP003846.1 is blood-derived and BJAB0715/1096996/CP003847.1 is cerebrospinal-fluid-derived in the inspected primary methods. BJAB0868/1096997/CP003849.1 is the ascites isolate and must remain a supported control. Recover the original PREGO pair evidence and correct or qualify unsupported site assignments through a governed source contract; do not infer the exact upstream error, absence of every possible later occurrence, or manually decrement the pool. Preserve the separately supported Vibrio E0666 and Corynebacterium species associations. No repair is performed by this review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history. Do not change source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/ascites.yaml; Entire YAML | supports | All target fields, source attestations, taxonomy entries and generated history were read. |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon terms cannot substitute for associated environments; parent_habitats must be strictly broader. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; reported association is weaker than characteristic presence. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Complete native context was used for source resolution; resulting identifier/status/predicate agree with the target: [{"automatic": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "BTO:0000091", "mapping_predicate": null, "reviewed": false, "route": "prego_self_grounded"}, "final": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "BTO:0000091", "mapping_predicate": null, "reviewed": false, "route": "prego_self_grounded"}, "mint": "habitatmech:PREGO.e885ed7c65", "source": "PREGO"}] |
| ET4 | data/raw/prego_habitat_taxa.tsv; TSV rows 75,76,77,78,79 | supports | [{"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0000091", "prego_score": "3", "rank": "1", "taxon_id": "NCBITaxon:1096995", "taxon_label": "Acinetobacter baumannii BJAB07104"}, "row": 75}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0000091", "prego_score": "3", "rank": "2", "taxon_id": "NCBITaxon:1096996", "taxon_label": "Acinetobacter baumannii BJAB0715"}, "row": 76}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0000091", "prego_score": "3", "rank": "3", "taxon_id": "NCBITaxon:1096997", "taxon_label": "Acinetobacter baumannii BJAB0868"}, "row": 77}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0000091", "prego_score": "3", "rank": "4", "taxon_id": "NCBITaxon:1231058", "taxon_label": "Vibrio diabolicus E0666"}, "row": 78}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0000091", "prego_score": "3", "rank": "5", "taxon_id": "NCBITaxon:401472", "taxon_label": "Corynebacterium ureicelerivorans"}, "row": 79}] |
| ET5 | data/raw/prego_habitats.tsv; TSV rows 385 | supports | [{"data": {"biolink_category": "biolink:GrossAnatomicalStructure", "channels": "annotated_genomes_isolates", "direct_assertion_count": "5", "max_prego_score": "3", "ontology": "BTO", "prego_id": "BTO:0000091", "prego_synonyms": "ascites&#124;ascites fluid&#124;ascites fluids&#124;asciteses&#124;ascitic fluid&#124;ascitic fluids", "taxon_count": "5"}, "row": 385}] |
| ET6 | data/raw/ontology_terms.tsv; TSV rows 93 | supports | [{"data": {"definition": "Accumulation of serous fluid in the spaces between tissues and organs in the cavity of the abdomen.", "deprecated": "", "directly_referenced": "TRUE", "label": "ascites", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0000091"}, "row": 93}] |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000091/graph; Authoritative term label, definition, typed synonyms and outgoing relations | supports | Typed outgoing edges, retaining subclass/part-of distinction: [{"label": "part of", "source": "http://purl.obolibrary.org/obo/BTO_0000091", "target": "http://purl.obolibrary.org/obo/BTO_0000020", "uri": "http://purl.obolibrary.org/obo/BFO_0000050"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000091; Authoritative term label, definition, typed synonyms and outgoing relations | supports | Current BTO:0000091 ascites; inspected definition and typed scope against the local record. |
| EX3 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=CP003846.1&amp;rettype=gb&amp;retmode=xml&amp;seq_start=1&amp;seq_stop=1; GBSeq source feature, strain and db_xref; first-base interval requested only to bound payload | supports | CP003846.1 source qualifiers [["organism", "Acinetobacter baumannii BJAB07104"], ["mol_type", "genomic DNA"], ["strain", "BJAB07104"], ["db_xref", "taxon:1096995"]]. These source features establish accession/strain/taxon identity, not isolation site; isolation site is supported by the primary paper. |
| EX4 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=CP003847.1&amp;rettype=gb&amp;retmode=xml&amp;seq_start=1&amp;seq_stop=1; GBSeq source feature, strain and db_xref; first-base interval requested only to bound payload | supports | CP003847.1 source qualifiers [["organism", "Acinetobacter baumannii BJAB0715"], ["mol_type", "genomic DNA"], ["strain", "BJAB0715"], ["db_xref", "taxon:1096996"]]. These source features establish accession/strain/taxon identity, not isolation site; isolation site is supported by the primary paper. |
| EX5 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=CP003849.1&amp;rettype=gb&amp;retmode=xml&amp;seq_start=1&amp;seq_stop=1; GBSeq source feature, strain and db_xref; first-base interval requested only to bound payload | supports | CP003849.1 source qualifiers [["organism", "Acinetobacter baumannii BJAB0868"], ["mol_type", "genomic DNA"], ["strain", "BJAB0868"], ["db_xref", "taxon:1096997"]]. These source features establish accession/strain/taxon identity, not isolation site; isolation site is supported by the primary paper. |
| EX6 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3691203/fullTextXML; Results: General features; Materials and Methods: Bacterial strains; strain-linked accession paragraph | supports | Methods assign BJAB07104 to blood, BJAB0715 to cerebrospinal fluid and BJAB0868 to ascites. The strain-linked accession paragraph assigns CP003846, CP003847 and CP003849 respectively; GenBank confirms these identity links. The final Data Availability sentence lists the latter two accessions in inconsistent order, so it is not used as the strain map. This confirms the publication-level mismatch, not the unobserved PREGO extraction mechanism. |
| EX7 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:19089476%20AND%20SRC:MED&amp;format=json&amp;resultType=core; Primary publication abstract and identifier metadata | supports | Fifteen Corynebacterium ureicelerivorans isolates from six patients included one patient with ascitic-fluid infection. Species-level ascites support remains valid despite other blood-derived isolates. PMID:19089476; DOI:10.1007/s10096-008-0677-1. |
| EX8 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:23826102%20AND%20SRC:MED&amp;format=json&amp;resultType=core; Primary publication abstract and identifier metadata | supports | The primary abstract distinguishes BJAB07104 blood, BJAB0715 spinal fluid and BJAB0868 ascites. The full methods and strain-linked accession paragraph corroborate these exact isolation contexts. PMID:23826102; DOI:10.1371/journal.pone.0066584. |
| EX9 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1096995,1096996,1096997,1231058,1290553,1333660,169215,1716,1747,1869227,2,281915,32008,32033,335058,35493,356,374,401472,41294,41295,48736,504481,50709,563835,629395,6656,75682,75787,7719,80840,80864,82115,85413&amp;retmode=xml; Exact requested TaxId, AkaTaxIds, ScientificName, Rank and Lineage | supports | NCBI identities and lineages: [{"current_id": "1096995", "current_name": "Acinetobacter baumannii BJAB07104", "current_rank": "strain", "id": "NCBITaxon:1096995", "label": "Acinetobacter baumannii BJAB07104", "lineage": "cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Moraxellales; Moraxellaceae; Acinetobacter; Acinetobacter calcoaceticus/baumannii complex; Acinetobacter baumannii"}, {"current_id": "1096996", "current_name": "Acinetobacter baumannii BJAB0715", "current_rank": "strain", "id": "NCBITaxon:1096996", "label": "Acinetobacter baumannii BJAB0715", "lineage": "cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Moraxellales; Moraxellaceae; Acinetobacter; Acinetobacter calcoaceticus/baumannii complex; Acinetobacter baumannii"}, {"current_id": "1096997", "current_name": "Acinetobacter baumannii BJAB0868", "current_rank": "strain", "id": "NCBITaxon:1096997", "label": "Acinetobacter baumannii BJAB0868", "lineage": "cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Moraxellales; Moraxellaceae; Acinetobacter; Acinetobacter calcoaceticus/baumannii complex; Acinetobacter baumannii"}, {"current_id": "1231058", "current_name": "Vibrio diabolicus E0666", "current_rank": "strain", "id": "NCBITaxon:1231058", "label": "Vibrio diabolicus E0666", "lineage": "cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Vibrionales; Vibrionaceae; Vibrio; Vibrio harveyi group; Vibrio diabolicus subgroup; Vibrio diabolicus"}, {"current_id": "401472", "current_name": "Corynebacterium ureicelerivorans", "current_rank": "species", "id": "NCBITaxon:401472", "label": "Corynebacterium ureicelerivorans", "lineage": "cellular organisms; Bacteria; Bacillati; Actinomycetota; Actinomycetes; Mycobacteriales; Corynebacteriaceae; Corynebacterium"}] |
| EX10 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1128/genomeA.00686-13&amp;format=json&amp;resultType=core; Primary publication abstract and identifier metadata | supports | E0666, published under Vibrio alginolyticus and now named Vibrio diabolicus, was isolated from Epinephelus coioides ascites. This is an exact strain positive control, not support for unrelated GOLD nodes. PMID:23990586; DOI:10.1128/genomea.00686-13. |
| ESEARCH | Local input and review traversal; rg --no-ignore --hidden -l -F -e BTO:0000091 -e ascites -e ascites -e habitatmech:PREGO.e885ed7c65 curation history research reports data/raw build reviews | context_only | Identifier/label/slug search covered hidden and ignored inputs; complete structured-YAML traversal found no target predecessor. Exact parsed TSV matches separately scope source associations. |
| EEXTRACT | src/habitatmech/extract.py; extract_prego | supports | The extractor deduplicates habitat/taxon pairs, keeps maximum source score, combines channels, sorts by score/direct flag/ID and retains top taxa with the full distinct-taxon pool. It does not retain specimen-level proof in the committed projection. |
| EAVAIL | Configured kg-microbe source checkout; find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe -type f -path '*/prego/*' -name '*.tsv' | context_only | No PREGO TSV files found in the configured checkout; expected transformed/prego/nodes.tsv and edges.tsv cannot be inspected here. This is bounded local availability, not evidence that upstream data do not exist. |

## Limits And Additional Notes

- Only the stated primary evidence and current ontology/taxonomy authorities were independently inspected; original specimen-level support for every source-bin member is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism or characteristic presence. Parent observations are not inherited by children.
- Configured label correspondence skipped 2,061 no-adapter pairs; this is not whole-corpus identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in this pre-save observation. Baseline full QC is separately identified as CI evidence.
- Legacy reports and historical rationale are contextual leads, not independent approval; historical incidental references were not exhaustively re-reviewed.
- iModulonDB is not applicable: the target has no gene, regulator or expression-module assertion. No paid research or scientific-status promotion was performed.
- Original manifest-named PREGO exports are unavailable in the configured checkout after ignored-inclusive search; publication witnesses do not reconstruct every original PREGO pair or extraction cause.
- Original captured hashes were rechecked unchanged, and the extractor was captured separately before assessing its PREGO contract. All included bytes match both the working tree and exact captured Git revision.
- Ignored-inclusive structured archive traversal found no earlier structured review targeting this record. No existing bundle is superseded or closed.
- This read-only review proposes maintained-owner actions but performs no curation or GitHub mutation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T075950Z-ascites-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: ascites (BTO:0000091)'
started_at: '2026-10-15T07:35:09Z'
finished_at: '2026-10-15T07:59:50Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent inspected the full target and source evidence; not
    independent human or second-agent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: BTO fluid-accumulation meaning can support a sampled material context, but
  two exact Acinetobacter strain associations lack ascites support in their primary
  genome study. That study assigns BJAB07104 to blood, BJAB0715 to cerebrospinal fluid,
  and only BJAB0868 to ascites. Independent positive controls support other retained
  associations.
source:
  git_revision: 23486ff2e685b41d486f25aad4719fd5b1549e4e
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
    sha256: 899c716d42cc7b2ddf9b78c7f2ba3838f5ec613faae838f87c586fc28bafc442
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 4fc09b29ddff99e935fc7a6eeb3ded377ad5cd0210c3664ba11b8a92d08bbd19
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: ea37676f1a16dd05fbfbb6c394b3f14b42ea93b763fb257043b817a4f10d3612
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: a87b2918b082a8661f85dc1a2fa24f59ec65717d11edf07e5cc1cb3f0834a0fe
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
  - path: data/habitats/host_associated/ascites.yaml
    sha256: 8de5555685a84ddd304e9ac72e22495a03714e8646a0cebe36fa67e241a92925
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
  - path: reports/yaml_record_review/20261002T154347Z-ascites.md
    sha256: 2d1001415f59816ad7e5db0ba47702fac17c106f3f15e456cbc373f1b42c8ef3
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
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
    role: context
targets:
- target_id: BTO:0000091
  path: data/habitats/host_associated/ascites.yaml
  label: ascites
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
  description: Scientific assessment of one exact generated target at captured main
    revision 23486ff2e685b41d486f25aad4719fd5b1549e4e.
  selection: Next twenty unreviewed records in corpus path order were selected; this
    document assesses only its single resolved identifier and source path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - BTO:0000091
  exclusions:
  - target: Other habitat records and SSSOM/KGX products
    reason: Direct parents inform hierarchy interpretation but are not additional
      completed reviews; exports are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/ascites.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000091
  summary: "Completed 2026-10-15T07:37:42Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/ascites.yaml"
  scope_note: Individual schema; strict command covers twenty named targets; other
    documented gates have full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/arm_nodes.yaml data/habitats/host_associated/armpit_nodes.yaml
    data/habitats/host_associated/arterial.yaml data/habitats/host_associated/arterial_blood.yaml
    data/habitats/host_associated/arterial_ulcer.yaml data/habitats/host_associated/arthropoda_chelicerates.yaml
    data/habitats/host_associated/arthropoda_crustaceans.yaml data/habitats/host_associated/arthropoda_insects.yaml
    data/habitats/host_associated/arthropoda_myriapoda.yaml data/habitats/host_associated/articular_cartilage.yaml
    data/habitats/host_associated/articular_cartilage__2ad5f85b.yaml data/habitats/host_associated/ascending_colon.yaml
    data/habitats/host_associated/ascidian.yaml data/habitats/host_associated/ascidians.yaml
    data/habitats/host_associated/ascites.yaml data/habitats/host_associated/ascites__06c98a68.yaml
    data/habitats/host_associated/ascites__13be9a4c.yaml data/habitats/host_associated/ascites__f2c36f2c.yaml
    data/habitats/host_associated/atherosclerotic_plaque.yaml data/habitats/host_associated/athlete_s_foot.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000091
  summary: "Completed 2026-10-15T07:38:15Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/arm_nodes.yaml data/habitats/host_associated/armpit_nodes.yaml\
    \ data/habitats/host_associated/arterial.yaml data/habitats/host_associated/arterial_blood.yaml\
    \ data/habitats/host_associated/arterial_ulcer.yaml data/habitats/host_associated/arthropoda_chelicerates.yaml\
    \ data/habitats/host_associated/arthropoda_crustaceans.yaml data/habitats/host_associated/arthropoda_insects.yaml\
    \ data/habitats/host_associated/arthropoda_myriapoda.yaml data/habitats/host_associated/articular_cartilage.yaml\
    \ data/habitats/host_associated/articular_cartilage__2ad5f85b.yaml data/habitats/host_associated/ascending_colon.yaml\
    \ data/habitats/host_associated/ascidian.yaml data/habitats/host_associated/ascidians.yaml\
    \ data/habitats/host_associated/ascites.yaml data/habitats/host_associated/ascites__06c98a68.yaml\
    \ data/habitats/host_associated/ascites__13be9a4c.yaml data/habitats/host_associated/ascites__f2c36f2c.yaml\
    \ data/habitats/host_associated/atherosclerotic_plaque.yaml data/habitats/host_associated/athlete_s_foot.yaml\n\
    Validating 20 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      20\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Individual schema; strict command covers twenty named targets; other
    documented gates have full-corpus scope.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000091
  summary: 'Completed 2026-10-15T07:38:28Z. No issues found

    759 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Individual schema; strict command covers twenty named targets; other
    documented gates have full-corpus scope.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000091
  summary: "Completed 2026-10-15T07:38:29Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Individual schema; strict command covers twenty named targets; other
    documented gates have full-corpus scope.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000091
  summary: "Completed 2026-10-15T07:38:55Z. expected 3208 records, found 3208 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Individual schema; strict command covers twenty named targets; other
    documented gates have full-corpus scope.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000091
  summary: "Completed 2026-10-15T07:39:04Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Individual schema; strict command covers twenty named targets; other
    documented gates have full-corpus scope.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000091
  summary: "Completed 2026-10-15T07:39:37Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Individual schema; strict command covers twenty named targets; other
    documented gates have full-corpus scope.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000091
  summary: "Completed 2026-10-15T07:41:13Z. id↔label correspondence summary:\n   \
    \       OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Individual schema; strict command covers twenty named targets; other
    documented gates have full-corpus scope.
- check_id: CCI
  name: Baseline full native QC in CI
  status: passed
  required: true
  command: gh run view 38698835390 --json status,conclusion,headSha,url,jobs
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000091
  summary: Authoritative quality gate and structured-review contract succeeded on
    the exact captured revision; status verified at 2026-10-15T07:57:35Z. https://github.com/CultureBotAI/HabitatMech/actions/runs/38698835390
  scope_note: Verified remote baseline execution, not a new local full-QC run. New
    output bundles require a separate post-save archive check.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/ascites.yaml
  locator: Entire YAML
  accessed_at: '2026-10-15T07:59:50Z'
  support: supports
  summary: All target fields, source attestations, taxonomy entries and generated
    history were read.
  snapshot_sha256: 8de5555685a84ddd304e9ac72e22495a03714e8646a0cebe36fa67e241a92925
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy and source ownership
  accessed_at: '2026-10-15T07:59:50Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon terms cannot substitute
    for associated environments; parent_habitats must be strictly broader.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-10-15T07:59:50Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; reported association is weaker than characteristic presence.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-10-15T07:59:50Z'
  support: supports
  summary: 'Complete native context was used for source resolution; resulting identifier/status/predicate
    agree with the target: [{"automatic": {"category": null, "contributes_grounding":
    true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status":
    "EXACT", "identifier": "BTO:0000091", "mapping_predicate": null, "reviewed": false,
    "route": "prego_self_grounded"}, "final": {"category": null, "contributes_grounding":
    true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status":
    "EXACT", "identifier": "BTO:0000091", "mapping_predicate": null, "reviewed": false,
    "route": "prego_self_grounded"}, "mint": "habitatmech:PREGO.e885ed7c65", "source":
    "PREGO"}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: ET4
  kind: database
  reference: data/raw/prego_habitat_taxa.tsv
  locator: TSV rows 75,76,77,78,79
  accessed_at: '2026-10-15T07:59:50Z'
  support: supports
  summary: '[{"data": {"channels": "annotated_genomes_isolates", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "BTO:0000091", "prego_score": "3", "rank":
    "1", "taxon_id": "NCBITaxon:1096995", "taxon_label": "Acinetobacter baumannii
    BJAB07104"}, "row": 75}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "BTO:0000091", "prego_score": "3", "rank":
    "2", "taxon_id": "NCBITaxon:1096996", "taxon_label": "Acinetobacter baumannii
    BJAB0715"}, "row": 76}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "BTO:0000091", "prego_score": "3", "rank":
    "3", "taxon_id": "NCBITaxon:1096997", "taxon_label": "Acinetobacter baumannii
    BJAB0868"}, "row": 77}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "BTO:0000091", "prego_score": "3", "rank":
    "4", "taxon_id": "NCBITaxon:1231058", "taxon_label": "Vibrio diabolicus E0666"},
    "row": 78}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "BTO:0000091", "prego_score": "3", "rank":
    "5", "taxon_id": "NCBITaxon:401472", "taxon_label": "Corynebacterium ureicelerivorans"},
    "row": 79}]'
  snapshot_sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
- evidence_id: ET5
  kind: database
  reference: data/raw/prego_habitats.tsv
  locator: TSV rows 385
  accessed_at: '2026-10-15T07:59:50Z'
  support: supports
  summary: '[{"data": {"biolink_category": "biolink:GrossAnatomicalStructure", "channels":
    "annotated_genomes_isolates", "direct_assertion_count": "5", "max_prego_score":
    "3", "ontology": "BTO", "prego_id": "BTO:0000091", "prego_synonyms": "ascites|ascites
    fluid|ascites fluids|asciteses|ascitic fluid|ascitic fluids", "taxon_count": "5"},
    "row": 385}]'
  snapshot_sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
- evidence_id: ET6
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 93
  accessed_at: '2026-10-15T07:59:50Z'
  support: supports
  summary: '[{"data": {"definition": "Accumulation of serous fluid in the spaces between
    tissues and organs in the cavity of the abdomen.", "deprecated": "", "directly_referenced":
    "TRUE", "label": "ascites", "label_only": "FALSE", "ontology": "BTO", "synonyms":
    "", "term_id": "BTO:0000091"}, "row": 93}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EX1
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000091/graph
  locator: Authoritative term label, definition, typed synonyms and outgoing relations
  accessed_at: '2026-10-15T07:40:39Z'
  support: supports
  summary: 'Typed outgoing edges, retaining subclass/part-of distinction: [{"label":
    "part of", "source": "http://purl.obolibrary.org/obo/BTO_0000091", "target": "http://purl.obolibrary.org/obo/BTO_0000020",
    "uri": "http://purl.obolibrary.org/obo/BFO_0000050"}]'
  snapshot_sha256: 414ef3ff8bcf08ebc0652980da161a9072bb26faf10a4ad81d45b546f75eb5fb
- evidence_id: EX2
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000091
  locator: Authoritative term label, definition, typed synonyms and outgoing relations
  accessed_at: '2026-10-15T07:39:11Z'
  support: supports
  summary: Current BTO:0000091 ascites; inspected definition and typed scope against
    the local record.
  snapshot_sha256: b896a28635610349ffc758d5bb4e24d612c8087d06b2503d89e1c49f030e480b
- evidence_id: EX3
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=CP003846.1&rettype=gb&retmode=xml&seq_start=1&seq_stop=1
  locator: GBSeq source feature, strain and db_xref; first-base interval requested
    only to bound payload
  accessed_at: '2026-10-15T07:49:16Z'
  support: supports
  summary: CP003846.1 source qualifiers [["organism", "Acinetobacter baumannii BJAB07104"],
    ["mol_type", "genomic DNA"], ["strain", "BJAB07104"], ["db_xref", "taxon:1096995"]].
    These source features establish accession/strain/taxon identity, not isolation
    site; isolation site is supported by the primary paper.
  snapshot_sha256: bee48352f7e038825e957ae3f937b89aff0ab7d2efd4792254ce479fc070b609
- evidence_id: EX4
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=CP003847.1&rettype=gb&retmode=xml&seq_start=1&seq_stop=1
  locator: GBSeq source feature, strain and db_xref; first-base interval requested
    only to bound payload
  accessed_at: '2026-10-15T07:49:16Z'
  support: supports
  summary: CP003847.1 source qualifiers [["organism", "Acinetobacter baumannii BJAB0715"],
    ["mol_type", "genomic DNA"], ["strain", "BJAB0715"], ["db_xref", "taxon:1096996"]].
    These source features establish accession/strain/taxon identity, not isolation
    site; isolation site is supported by the primary paper.
  snapshot_sha256: 71ed4f7d05090c9420dac6505dd0f4e9be773fc142d4c83b55bb3f699388b208
- evidence_id: EX5
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=CP003849.1&rettype=gb&retmode=xml&seq_start=1&seq_stop=1
  locator: GBSeq source feature, strain and db_xref; first-base interval requested
    only to bound payload
  accessed_at: '2026-10-15T07:49:17Z'
  support: supports
  summary: CP003849.1 source qualifiers [["organism", "Acinetobacter baumannii BJAB0868"],
    ["mol_type", "genomic DNA"], ["strain", "BJAB0868"], ["db_xref", "taxon:1096997"]].
    These source features establish accession/strain/taxon identity, not isolation
    site; isolation site is supported by the primary paper.
  snapshot_sha256: 8e680858df4f49a281dd74f1c75d7c7019d0c25bfa81e231c9fcdc25c1070500
- evidence_id: EX6
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3691203/fullTextXML
  locator: 'Results: General features; Materials and Methods: Bacterial strains; strain-linked
    accession paragraph'
  accessed_at: '2026-10-15T07:49:14Z'
  support: supports
  summary: Methods assign BJAB07104 to blood, BJAB0715 to cerebrospinal fluid and
    BJAB0868 to ascites. The strain-linked accession paragraph assigns CP003846, CP003847
    and CP003849 respectively; GenBank confirms these identity links. The final Data
    Availability sentence lists the latter two accessions in inconsistent order, so
    it is not used as the strain map. This confirms the publication-level mismatch,
    not the unobserved PREGO extraction mechanism.
  snapshot_sha256: a97139cf0649b10a9f44328952c8181d211c0bd0c6d4b7041856a3af7c3a5fef
- evidence_id: EX7
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:19089476%20AND%20SRC:MED&format=json&resultType=core
  locator: Primary publication abstract and identifier metadata
  accessed_at: '2026-10-15T07:49:13Z'
  support: supports
  summary: Fifteen Corynebacterium ureicelerivorans isolates from six patients included
    one patient with ascitic-fluid infection. Species-level ascites support remains
    valid despite other blood-derived isolates. PMID:19089476; DOI:10.1007/s10096-008-0677-1.
  snapshot_sha256: 0d499f7299c351e4c7b2ea79f4ffef3252061e079c8bf33eafea864a8d8b0518
- evidence_id: EX8
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:23826102%20AND%20SRC:MED&format=json&resultType=core
  locator: Primary publication abstract and identifier metadata
  accessed_at: '2026-10-15T07:49:12Z'
  support: supports
  summary: The primary abstract distinguishes BJAB07104 blood, BJAB0715 spinal fluid
    and BJAB0868 ascites. The full methods and strain-linked accession paragraph corroborate
    these exact isolation contexts. PMID:23826102; DOI:10.1371/journal.pone.0066584.
  snapshot_sha256: f09ef05816e2914b23337890b10ccf1e51fd6b986bd53b6e998bcc81b7db3722
- evidence_id: EX9
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1096995,1096996,1096997,1231058,1290553,1333660,169215,1716,1747,1869227,2,281915,32008,32033,335058,35493,356,374,401472,41294,41295,48736,504481,50709,563835,629395,6656,75682,75787,7719,80840,80864,82115,85413&retmode=xml
  locator: Exact requested TaxId, AkaTaxIds, ScientificName, Rank and Lineage
  accessed_at: '2026-10-15T07:39:50Z'
  support: supports
  summary: 'NCBI identities and lineages: [{"current_id": "1096995", "current_name":
    "Acinetobacter baumannii BJAB07104", "current_rank": "strain", "id": "NCBITaxon:1096995",
    "label": "Acinetobacter baumannii BJAB07104", "lineage": "cellular organisms;
    Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Moraxellales; Moraxellaceae;
    Acinetobacter; Acinetobacter calcoaceticus/baumannii complex; Acinetobacter baumannii"},
    {"current_id": "1096996", "current_name": "Acinetobacter baumannii BJAB0715",
    "current_rank": "strain", "id": "NCBITaxon:1096996", "label": "Acinetobacter baumannii
    BJAB0715", "lineage": "cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota;
    Gammaproteobacteria; Moraxellales; Moraxellaceae; Acinetobacter; Acinetobacter
    calcoaceticus/baumannii complex; Acinetobacter baumannii"}, {"current_id": "1096997",
    "current_name": "Acinetobacter baumannii BJAB0868", "current_rank": "strain",
    "id": "NCBITaxon:1096997", "label": "Acinetobacter baumannii BJAB0868", "lineage":
    "cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
    Moraxellales; Moraxellaceae; Acinetobacter; Acinetobacter calcoaceticus/baumannii
    complex; Acinetobacter baumannii"}, {"current_id": "1231058", "current_name":
    "Vibrio diabolicus E0666", "current_rank": "strain", "id": "NCBITaxon:1231058",
    "label": "Vibrio diabolicus E0666", "lineage": "cellular organisms; Bacteria;
    Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Vibrionales; Vibrionaceae;
    Vibrio; Vibrio harveyi group; Vibrio diabolicus subgroup; Vibrio diabolicus"},
    {"current_id": "401472", "current_name": "Corynebacterium ureicelerivorans", "current_rank":
    "species", "id": "NCBITaxon:401472", "label": "Corynebacterium ureicelerivorans",
    "lineage": "cellular organisms; Bacteria; Bacillati; Actinomycetota; Actinomycetes;
    Mycobacteriales; Corynebacteriaceae; Corynebacterium"}]'
  snapshot_sha256: aea844aa11500f9f43af1b5e0ea2843bd4ef46fd593071067c25e7a85917dcac
- evidence_id: EX10
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1128/genomeA.00686-13&format=json&resultType=core
  locator: Primary publication abstract and identifier metadata
  accessed_at: '2026-10-15T07:49:15Z'
  support: supports
  summary: E0666, published under Vibrio alginolyticus and now named Vibrio diabolicus,
    was isolated from Epinephelus coioides ascites. This is an exact strain positive
    control, not support for unrelated GOLD nodes. PMID:23990586; DOI:10.1128/genomea.00686-13.
  snapshot_sha256: a265df14151206f8cd54461f734fd6abd2d7d55c43efe8dfc0c14694ce19e252
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: rg --no-ignore --hidden -l -F -e BTO:0000091 -e ascites -e ascites -e habitatmech:PREGO.e885ed7c65
    curation history research reports data/raw build reviews
  accessed_at: '2026-10-15T07:36:12Z'
  support: context_only
  summary: Identifier/label/slug search covered hidden and ignored inputs; complete
    structured-YAML traversal found no target predecessor. Exact parsed TSV matches
    separately scope source associations.
  search_scope: curation, history, research, reports, data/raw, build and reviews,
    including hidden/ignored files; structured review.yaml traversal independent of
    gitignore. Not a global absence claim.
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: extract_prego
  accessed_at: '2026-10-15T07:59:50Z'
  support: supports
  summary: The extractor deduplicates habitat/taxon pairs, keeps maximum source score,
    combines channels, sorts by score/direct flag/ID and retains top taxa with the
    full distinct-taxon pool. It does not retain specimen-level proof in the committed
    projection.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: EAVAIL
  kind: search
  reference: Configured kg-microbe source checkout
  locator: find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe
    -type f -path '*/prego/*' -name '*.tsv'
  accessed_at: '2026-10-15T07:50:46Z'
  support: context_only
  summary: No PREGO TSV files found in the configured checkout; expected transformed/prego/nodes.tsv
    and edges.tsv cannot be inspected here. This is bounded local availability, not
    evidence that upstream data do not exist.
  search_scope: find traversed the configured kg-microbe checkout including hidden
    and ignored files, selecting all prego-directory TSVs.
assessments:
- assessment_id: A1
  area: schema
  topic: Native validity and reproduction
  outcome: supported
  summary: Individual schema, strict twenty-target validation, 759 history records,
    14 inventory/two GOLD provenance sources, exact 3,208-record reproduction, 32
    causal overlays and 110 term requests passed. These deterministic checks do not
    prove scientific claims.
  target_ids:
  - BTO:0000091
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: concern
  summary: BTO fluid-accumulation meaning can support a sampled material context,
    but two exact Acinetobacter strain associations lack ascites support in their
    primary genome study. That study assigns BJAB07104 to blood, BJAB0715 to cerebrospinal
    fluid, and only BJAB0868 to ascites. Independent positive controls support other
    retained associations.
  target_ids:
  - BTO:0000091
  evidence_ids:
  - E1
  - ERULE
  - ESEED
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EX9
  - EX10
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks and
    pools: [{"source": "PREGO", "count": 5, "unit": "TAXON"}]. Zero counts are omitted;
    unrelated parent, bulk and study counts are not added. 5 retained taxon IDs were
    resolved against NCBI, including explicit aliases where noted.'
  target_ids:
  - BTO:0000091
  evidence_ids:
  - E1
  - ESEED
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EX9
  - EX10
- assessment_id: A4
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: No causal edge or characteristic-presence claim is asserted. Missing optional
    parameters/graphs are not evidence deficits. Full source decisions and executed
    routes reproduce SEEDED / EXACT; this review does not promote them.
  target_ids:
  - BTO:0000091
  evidence_ids:
  - E1
  - ESEED
  - ESCHEMA
findings:
- finding_id: F1
  issue_key: ascites-strain-isolation-site-mismatch
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Two exact strain associations lack ascites support in the genome study
  description: BJAB07104/NCBITaxon:1096995/CP003846.1 is blood-derived and BJAB0715/1096996/CP003847.1
    is cerebrospinal-fluid-derived in the inspected primary methods. BJAB0868/1096997/CP003849.1
    is the ascites isolate and must remain a supported control. Recover the original
    PREGO pair evidence and correct or qualify unsupported site assignments through
    a governed source contract; do not infer the exact upstream error, absence of
    every possible later occurrence, or manually decrement the pool. Preserve the
    separately supported Vibrio E0666 and Corynebacterium species associations.
  target_ids:
  - BTO:0000091
  field_paths:
  - characteristic_taxa
  evidence_ids:
  - E1
  - ERULE
  - ESEED
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EX9
  - EX10
  - EEXTRACT
  - EAVAIL
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or source-evidence claim;
    deterministic validity does not establish scientific support.
  external_issues: []
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - BTO:0000091
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  description: BJAB07104/NCBITaxon:1096995/CP003846.1 is blood-derived and BJAB0715/1096996/CP003847.1
    is cerebrospinal-fluid-derived in the inspected primary methods. BJAB0868/1096997/CP003849.1
    is the ascites isolate and must remain a supported control. Recover the original
    PREGO pair evidence and correct or qualify unsupported site assignments through
    a governed source contract; do not infer the exact upstream error, absence of
    every possible later occurrence, or manually decrement the pool. Preserve the
    separately supported Vibrio E0666 and Corynebacterium species associations. No
    repair is performed by this review.
  generator: Controlled source refresh when required, then just seed, guarded just
    seed-canary, just seed-apply, and dependent term-request/map/site/redirect regeneration.
  acceptance_checks:
  - Regress the exact reported claim and preserve independently valid identifiers,
    source counts/units, raw provenance, native status and history. Do not change
    source totals by hand.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
limitations:
- Only the stated primary evidence and current ontology/taxonomy authorities were
  independently inspected; original specimen-level support for every source-bin member
  is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism
  or characteristic presence. Parent observations are not inherited by children.
- Configured label correspondence skipped 2,061 no-adapter pairs; this is not whole-corpus
  identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in
  this pre-save observation. Baseline full QC is separately identified as CI evidence.
- Legacy reports and historical rationale are contextual leads, not independent approval;
  historical incidental references were not exhaustively re-reviewed.
- 'iModulonDB is not applicable: the target has no gene, regulator or expression-module
  assertion. No paid research or scientific-status promotion was performed.'
- Original manifest-named PREGO exports are unavailable in the configured checkout
  after ignored-inclusive search; publication witnesses do not reconstruct every original
  PREGO pair or extraction cause.
notes:
- Original captured hashes were rechecked unchanged, and the extractor was captured
  separately before assessing its PREGO contract. All included bytes match both the
  working tree and exact captured Git revision.
- Ignored-inclusive structured archive traversal found no earlier structured review
  targeting this record. No existing bundle is superseded or closed.
- This read-only review proposes maintained-owner actions but performs no curation
  or GitHub mutation.
tags:
- individual-scientific-review
- host-associated
```
