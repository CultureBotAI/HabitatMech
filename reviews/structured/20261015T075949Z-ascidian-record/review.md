# Record review: ascidian (BTO:0000090)

- Review: 20261015T075949Z-ascidian-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T07:35:01Z
- Finished UTC: 2026-10-15T07:59:49Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Blocker: PREGO self-grounding adopts a whole Ascidiacea organism identity as a habitat. The host and its associated environment must remain distinct. The three retained taxa include a host organism, not three demonstrated microbial inhabitants.

## Scope And Provenance

Scientific assessment of one exact generated target at captured main revision 23486ff2e685b41d486f25aad4719fd5b1549e4e.

Selection: Next twenty unreviewed records in corpus path order were selected; this document assesses only its single resolved identifier and source path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 23486ff2e685b41d486f25aad4719fd5b1549e4e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0000090 | data/habitats/host_associated/ascidian.yaml | generated | ascidian |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0000090 | Completed 2026-10-15T07:37:32Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/ascidian.yaml |
| validate-strict | passed | True | BTO:0000090 | Completed 2026-10-15T07:38:15Z. uv run python scripts/validate_strict.py data/habitats/host_associated/arm_nodes.yaml data/habitats/host_associated/armpit_nodes.yaml data/habitats/host_associated/arterial.yaml data/habitats/host_associated/arterial_blood.yaml data/habitats/host_associated/arterial_ulcer.yaml data/habitats/host_associated/arthropoda_chelicerates.yaml data/habitats/host_associated/arthropoda_crustaceans.yaml data/habitats/host_associated/arthropoda_insects.yaml data/habitats/host_associated/arthropoda_myriapoda.yaml data/habitats/host_associated/articular_cartilage.yaml data/habitats/host_associated/articular_cartilage__2ad5f85b.yaml data/habitats/host_associated/ascending_colon.yaml data/habitats/host_associated/ascidian.yaml data/habitats/host_associated/ascidians.yaml data/habitats/host_associated/ascites.yaml data/habitats/host_associated/ascites__06c98a68.yaml data/habitats/host_associated/ascites__13be9a4c.yaml data/habitats/host_associated/ascites__f2c36f2c.yaml data/habitats/host_associated/atherosclerotic_plaque.yaml data/habitats/host_associated/athlete_s_foot.yaml<br>Validating 20 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      20<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | BTO:0000090 | Completed 2026-10-15T07:38:28Z. No issues found<br>759 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | BTO:0000090 | Completed 2026-10-15T07:38:29Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | BTO:0000090 | Completed 2026-10-15T07:38:55Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | BTO:0000090 | Completed 2026-10-15T07:39:04Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | BTO:0000090 | Completed 2026-10-15T07:39:37Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | BTO:0000090 | Completed 2026-10-15T07:41:13Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Baseline full native QC in CI | passed | True | BTO:0000090 | Authoritative quality gate and structured-review contract succeeded on the exact captured revision; status verified at 2026-10-15T07:57:35Z. https://github.com/CultureBotAI/HabitatMech/actions/runs/38698835390 |

## Scientific And Domain Assessments

### Native validity and reproduction

schema: supported. Targets: BTO:0000090.

Individual schema, strict twenty-target validation, 759 history records, 14 inventory/two GOLD provenance sources, exact 3,208-record reproduction, 32 causal overlays and 110 term requests passed. These deterministic checks do not prove scientific claims.

### Identity, definition, hierarchy and aliases

identity: concern. Targets: BTO:0000090.

Blocker: PREGO self-grounding adopts a whole Ascidiacea organism identity as a habitat. The host and its associated environment must remain distinct. The three retained taxa include a host organism, not three demonstrated microbial inhabitants.

### Source counts and retained ranking

quantity: supported. Targets: BTO:0000090.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks and pools: [{"source": "PREGO", "count": 3, "unit": "TAXON"}]. Zero counts are omitted; unrelated parent, bulk and study counts are not added. 3 retained taxon IDs were resolved against NCBI, including explicit aliases where noted.

### Parameters, mechanisms and native status

completeness: supported. Targets: BTO:0000090.

No causal edge or characteristic-presence claim is asserted. Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce SEEDED / EXACT; this review does not promote them.

## Findings

### F1: Whole ascidian organism is adopted as habitat identity

blocker / open / confirmed; issue key: ascidian-whole-host-identity.

Replace PREGO self-grounding with an evidence-backed decision for habitatmech:PREGO.fce17c8a5c that preserves a minted associated-environment identity and keeps BTO organism meaning only as context. Audit the three associations before any merge into the GOLD ascidian environment. NCBITaxon:7719 is Ciona intestinalis, a host taxon allowed as an association but not evidence of a microbial inhabitant; Endozoicomonas type-strain pen-shell origin does not prove species-level absence from ascidians.

## Recommended Actions And Acceptance Checks

### ACT1

Replace PREGO self-grounding with an evidence-backed decision for habitatmech:PREGO.fce17c8a5c that preserves a minted associated-environment identity and keeps BTO organism meaning only as context. Audit the three associations before any merge into the GOLD ascidian environment. NCBITaxon:7719 is Ciona intestinalis, a host taxon allowed as an association but not evidence of a microbial inhabitant; Endozoicomonas type-strain pen-shell origin does not prove species-level absence from ascidians. No repair is performed by this review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history. Do not change source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/ascidian.yaml; Entire YAML | supports | All target fields, source attestations, taxonomy entries and generated history were read. |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon terms cannot substitute for associated environments; parent_habitats must be strictly broader. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; reported association is weaker than characteristic presence. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Complete native context was used for source resolution; resulting identifier/status/predicate agree with the target: [{"automatic": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "BTO:0000090", "mapping_predicate": null, "reviewed": false, "route": "prego_self_grounded"}, "final": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "BTO:0000090", "mapping_predicate": null, "reviewed": false, "route": "prego_self_grounded"}, "mint": "habitatmech:PREGO.fce17c8a5c", "source": "PREGO"}] |
| ET4 | data/raw/prego_habitat_taxa.tsv; TSV rows 72,73,74 | supports | [{"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0000090", "prego_score": "3", "rank": "1", "taxon_id": "NCBITaxon:1290553", "taxon_label": "Halocynthiibacter namhaensis"}, "row": 72}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0000090", "prego_score": "3", "rank": "2", "taxon_id": "NCBITaxon:1333660", "taxon_label": "Endozoicomonas atrinae"}, "row": 73}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0000090", "prego_score": "3", "rank": "3", "taxon_id": "NCBITaxon:7719", "taxon_label": ""}, "row": 74}] |
| ET5 | data/raw/prego_habitats.tsv; TSV rows 425 | supports | [{"data": {"biolink_category": "biolink:GrossAnatomicalStructure", "channels": "annotated_genomes_isolates", "direct_assertion_count": "3", "max_prego_score": "3", "ontology": "BTO", "prego_id": "BTO:0000090", "prego_synonyms": "ascidian&#124;ascidianic&#124;ascidians&#124;sea squirt&#124;sea squirts", "taxon_count": "3"}, "row": 425}] |
| ET6 | data/raw/ontology_subclass_edges.tsv; TSV rows 68,194 | supports | [{"data": {"object": "BTO:0000284", "predicate": "rdfs:subClassOf", "subject": "BTO:0000090"}, "row": 68}, {"data": {"object": "BTO:0000000", "predicate": "rdfs:subClassOf", "subject": "BTO:0000284"}, "row": 194}] |
| ET7 | data/raw/ontology_terms.tsv; TSV rows 92,286 | supports | [{"data": {"definition": "Any of a class (Ascidiacea) of solitary or colonial sessile tunicates that have an oral and an atrial siphon.", "deprecated": "", "directly_referenced": "TRUE", "label": "ascidian", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0000090"}, "row": 92}, {"data": {"definition": "", "deprecated": "", "directly_referenced": "FALSE", "label": "organism form", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0000284"}, "row": 286}] |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000090/graph; Authoritative term label, definition, typed synonyms and outgoing relations | supports | Typed outgoing edges, retaining subclass/part-of distinction: [{"label": "subClassOf", "source": "http://purl.obolibrary.org/obo/BTO_0000090", "target": "http://purl.obolibrary.org/obo/BTO_0000284", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000090; Authoritative term label, definition, typed synonyms and outgoing relations | supports | Current BTO:0000090 ascidian; inspected definition and typed scope against the local record. |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000284/graph; Authoritative term label, definition, typed synonyms and outgoing relations | supports | Typed outgoing edges, retaining subclass/part-of distinction: [{"label": "subClassOf", "source": "http://purl.obolibrary.org/obo/BTO_0000284", "target": "http://purl.obolibrary.org/obo/BTO_0000000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000284; Authoritative term label, definition, typed synonyms and outgoing relations | supports | Current BTO:0000284 organism form; inspected definition and typed scope against the local record. |
| EX5 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002/graph; Authoritative term label, definition, typed synonyms and outgoing relations | supports | Typed outgoing edges, retaining subclass/part-of distinction: [{"label": "subClassOf", "source": "http://purl.obolibrary.org/obo/ENVO_01001002", "target": "http://purl.obolibrary.org/obo/ENVO_01001000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf"}, {"label": "part of", "source": "http://purl.obolibrary.org/obo/ENVO_01001002", "target": "http://purl.obolibrary.org/obo/NCBITaxon_33208", "uri": "http://purl.obolibrary.org/obo/BFO_0000050"}] |
| EX6 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002; Authoritative term label, definition, typed synonyms and outgoing relations | supports | Current ENVO:01001002 animal-associated environment; inspected definition and typed scope against the local record. |
| EX7 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3A%22Endozoicomonas%20atrinae%22&amp;format=json&amp;resultType=core&amp;pageSize=20; Primary publication abstract and identifier metadata | supports | Endozoicomonas atrinae WP70 was isolated from the gut of Atrina pectinata, a pen shell. This type-strain origin does not prove the species never occurs with ascidians; the original PREGO pair needs its own context. PMID:24733175; DOI:10.1099/ijs.0.060780-0. |
| EX8 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3A%22Halocynthiibacter%20namhaensis%22&amp;format=json&amp;resultType=core&amp;pageSize=20; Primary publication abstract and identifier metadata | supports | Halocynthiibacter namhaensis RA2-3 was isolated from Halocynthia roretzi. This supports a sea-squirt association at the named strain and species scope. PMID:24573327; DOI:10.1007/s10482-014-0142-3. |
| EX9 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1096995,1096996,1096997,1231058,1290553,1333660,169215,1716,1747,1869227,2,281915,32008,32033,335058,35493,356,374,401472,41294,41295,48736,504481,50709,563835,629395,6656,75682,75787,7719,80840,80864,82115,85413&amp;retmode=xml; Exact requested TaxId, AkaTaxIds, ScientificName, Rank and Lineage | supports | NCBI identities and lineages: [{"current_id": "1290553", "current_name": "Halocynthiibacter namhaensis", "current_rank": "species", "id": "NCBITaxon:1290553", "label": "Halocynthiibacter namhaensis", "lineage": "cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Alphaproteobacteria; Rhodobacterales; Paracoccaceae; Halocynthiibacter"}, {"current_id": "1333660", "current_name": "Endozoicomonas atrinae", "current_rank": "species", "id": "NCBITaxon:1333660", "label": "Endozoicomonas atrinae", "lineage": "cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Oceanospirillales; Endozoicomonadaceae; Endozoicomonas"}, {"current_id": "7719", "current_name": "Ciona intestinalis", "current_rank": "species", "id": "NCBITaxon:7719", "label": null, "lineage": "cellular organisms; Eukaryota; Opisthokonta; Metazoa; Eumetazoa; Bilateria; Deuterostomia; Chordata; Tunicata; Ascidiacea; Phlebobranchia; Cionidae; Ciona"}] |
| ESEARCH | Local input and review traversal; rg --no-ignore --hidden -l -F -e BTO:0000090 -e ascidian -e ascidian -e habitatmech:PREGO.fce17c8a5c curation history research reports data/raw build reviews | context_only | Identifier/label/slug search covered hidden and ignored inputs; complete structured-YAML traversal found no target predecessor. Exact parsed TSV matches separately scope source associations. |
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
review_id: 20261015T075949Z-ascidian-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: ascidian (BTO:0000090)'
started_at: '2026-10-15T07:35:01Z'
finished_at: '2026-10-15T07:59:49Z'
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
summary: 'Blocker: PREGO self-grounding adopts a whole Ascidiacea organism identity
  as a habitat. The host and its associated environment must remain distinct. The
  three retained taxa include a host organism, not three demonstrated microbial inhabitants.'
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
  - path: data/habitats/host_associated/ascidian.yaml
    sha256: 57443d4018e4700ea97f7d03c05632b8ba95435057b9a6c836b6074538c6a33d
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
  - path: reports/yaml_record_review/20261002T151517Z-ascidian.md
    sha256: 37be0df5cda337ef75efcec7b79a817f3b863c26c772fe7db4e504fe9ba2519d
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
- target_id: BTO:0000090
  path: data/habitats/host_associated/ascidian.yaml
  label: ascidian
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
  - BTO:0000090
  exclusions:
  - target: Other habitat records and SSSOM/KGX products
    reason: Direct parents inform hierarchy interpretation but are not additional
      completed reviews; exports are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/ascidian.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000090
  summary: "Completed 2026-10-15T07:37:32Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/ascidian.yaml"
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
  - BTO:0000090
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
  - BTO:0000090
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
  - BTO:0000090
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
  - BTO:0000090
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
  - BTO:0000090
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
  - BTO:0000090
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
  - BTO:0000090
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
  - BTO:0000090
  summary: Authoritative quality gate and structured-review contract succeeded on
    the exact captured revision; status verified at 2026-10-15T07:57:35Z. https://github.com/CultureBotAI/HabitatMech/actions/runs/38698835390
  scope_note: Verified remote baseline execution, not a new local full-QC run. New
    output bundles require a separate post-save archive check.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/ascidian.yaml
  locator: Entire YAML
  accessed_at: '2026-10-15T07:59:49Z'
  support: supports
  summary: All target fields, source attestations, taxonomy entries and generated
    history were read.
  snapshot_sha256: 57443d4018e4700ea97f7d03c05632b8ba95435057b9a6c836b6074538c6a33d
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy and source ownership
  accessed_at: '2026-10-15T07:59:49Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon terms cannot substitute
    for associated environments; parent_habitats must be strictly broader.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-10-15T07:59:49Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; reported association is weaker than characteristic presence.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-10-15T07:59:49Z'
  support: supports
  summary: 'Complete native context was used for source resolution; resulting identifier/status/predicate
    agree with the target: [{"automatic": {"category": null, "contributes_grounding":
    true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status":
    "EXACT", "identifier": "BTO:0000090", "mapping_predicate": null, "reviewed": false,
    "route": "prego_self_grounded"}, "final": {"category": null, "contributes_grounding":
    true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status":
    "EXACT", "identifier": "BTO:0000090", "mapping_predicate": null, "reviewed": false,
    "route": "prego_self_grounded"}, "mint": "habitatmech:PREGO.fce17c8a5c", "source":
    "PREGO"}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: ET4
  kind: database
  reference: data/raw/prego_habitat_taxa.tsv
  locator: TSV rows 72,73,74
  accessed_at: '2026-10-15T07:59:49Z'
  support: supports
  summary: '[{"data": {"channels": "annotated_genomes_isolates", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "BTO:0000090", "prego_score": "3", "rank":
    "1", "taxon_id": "NCBITaxon:1290553", "taxon_label": "Halocynthiibacter namhaensis"},
    "row": 72}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "BTO:0000090", "prego_score": "3", "rank":
    "2", "taxon_id": "NCBITaxon:1333660", "taxon_label": "Endozoicomonas atrinae"},
    "row": 73}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "BTO:0000090", "prego_score": "3", "rank":
    "3", "taxon_id": "NCBITaxon:7719", "taxon_label": ""}, "row": 74}]'
  snapshot_sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
- evidence_id: ET5
  kind: database
  reference: data/raw/prego_habitats.tsv
  locator: TSV rows 425
  accessed_at: '2026-10-15T07:59:49Z'
  support: supports
  summary: '[{"data": {"biolink_category": "biolink:GrossAnatomicalStructure", "channels":
    "annotated_genomes_isolates", "direct_assertion_count": "3", "max_prego_score":
    "3", "ontology": "BTO", "prego_id": "BTO:0000090", "prego_synonyms": "ascidian|ascidianic|ascidians|sea
    squirt|sea squirts", "taxon_count": "3"}, "row": 425}]'
  snapshot_sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
- evidence_id: ET6
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 68,194
  accessed_at: '2026-10-15T07:59:49Z'
  support: supports
  summary: '[{"data": {"object": "BTO:0000284", "predicate": "rdfs:subClassOf", "subject":
    "BTO:0000090"}, "row": 68}, {"data": {"object": "BTO:0000000", "predicate": "rdfs:subClassOf",
    "subject": "BTO:0000284"}, "row": 194}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET7
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 92,286
  accessed_at: '2026-10-15T07:59:49Z'
  support: supports
  summary: '[{"data": {"definition": "Any of a class (Ascidiacea) of solitary or colonial
    sessile tunicates that have an oral and an atrial siphon.", "deprecated": "",
    "directly_referenced": "TRUE", "label": "ascidian", "label_only": "FALSE", "ontology":
    "BTO", "synonyms": "", "term_id": "BTO:0000090"}, "row": 92}, {"data": {"definition":
    "", "deprecated": "", "directly_referenced": "FALSE", "label": "organism form",
    "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0000284"},
    "row": 286}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EX1
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000090/graph
  locator: Authoritative term label, definition, typed synonyms and outgoing relations
  accessed_at: '2026-10-15T07:39:11Z'
  support: supports
  summary: 'Typed outgoing edges, retaining subclass/part-of distinction: [{"label":
    "subClassOf", "source": "http://purl.obolibrary.org/obo/BTO_0000090", "target":
    "http://purl.obolibrary.org/obo/BTO_0000284", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf"}]'
  snapshot_sha256: 7c0c1a2fdc09f363fa12a417b049ed1fd7d771695f91237b34ab27254acfc127
- evidence_id: EX2
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000090
  locator: Authoritative term label, definition, typed synonyms and outgoing relations
  accessed_at: '2026-10-15T07:39:10Z'
  support: supports
  summary: Current BTO:0000090 ascidian; inspected definition and typed scope against
    the local record.
  snapshot_sha256: 22fcd309752acbbb4b5de2b05a4c8d804554e41b30aad31f5b91009b7ca9e8bd
- evidence_id: EX3
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000284/graph
  locator: Authoritative term label, definition, typed synonyms and outgoing relations
  accessed_at: '2026-10-15T07:40:42Z'
  support: supports
  summary: 'Typed outgoing edges, retaining subclass/part-of distinction: [{"label":
    "subClassOf", "source": "http://purl.obolibrary.org/obo/BTO_0000284", "target":
    "http://purl.obolibrary.org/obo/BTO_0000000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf"}]'
  snapshot_sha256: d8667ccebbf1ef06a4dfb8fc90b7e8fd16d9475a22121ec59f2cf35c6c7c5968
- evidence_id: EX4
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000284
  locator: Authoritative term label, definition, typed synonyms and outgoing relations
  accessed_at: '2026-10-15T07:40:41Z'
  support: supports
  summary: Current BTO:0000284 organism form; inspected definition and typed scope
    against the local record.
  snapshot_sha256: 305fb4df3b8081b3645a0a98f1f5abe7014f5e0b0458732189ba37fdd5b961f8
- evidence_id: EX5
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002/graph
  locator: Authoritative term label, definition, typed synonyms and outgoing relations
  accessed_at: '2026-10-15T07:39:26Z'
  support: supports
  summary: 'Typed outgoing edges, retaining subclass/part-of distinction: [{"label":
    "subClassOf", "source": "http://purl.obolibrary.org/obo/ENVO_01001002", "target":
    "http://purl.obolibrary.org/obo/ENVO_01001000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf"},
    {"label": "part of", "source": "http://purl.obolibrary.org/obo/ENVO_01001002",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_33208", "uri": "http://purl.obolibrary.org/obo/BFO_0000050"}]'
  snapshot_sha256: 882375d994d0dea7166097328c56e0e22362848e68aba0125d1b128a24ebf1b0
- evidence_id: EX6
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002
  locator: Authoritative term label, definition, typed synonyms and outgoing relations
  accessed_at: '2026-10-15T07:39:25Z'
  support: supports
  summary: Current ENVO:01001002 animal-associated environment; inspected definition
    and typed scope against the local record.
  snapshot_sha256: c3c90d5e91cc85727658222c907f7747f34861ad80bf1ceac5ce209f7e170907
- evidence_id: EX7
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3A%22Endozoicomonas%20atrinae%22&format=json&resultType=core&pageSize=20
  locator: Primary publication abstract and identifier metadata
  accessed_at: '2026-10-15T07:39:22Z'
  support: supports
  summary: Endozoicomonas atrinae WP70 was isolated from the gut of Atrina pectinata,
    a pen shell. This type-strain origin does not prove the species never occurs with
    ascidians; the original PREGO pair needs its own context. PMID:24733175; DOI:10.1099/ijs.0.060780-0.
  snapshot_sha256: 8984facf73b0ce6fb3c58dfe74c04707a7cf595912bba663115dbbe7d585e1a0
- evidence_id: EX8
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3A%22Halocynthiibacter%20namhaensis%22&format=json&resultType=core&pageSize=20
  locator: Primary publication abstract and identifier metadata
  accessed_at: '2026-10-15T07:39:21Z'
  support: supports
  summary: Halocynthiibacter namhaensis RA2-3 was isolated from Halocynthia roretzi.
    This supports a sea-squirt association at the named strain and species scope.
    PMID:24573327; DOI:10.1007/s10482-014-0142-3.
  snapshot_sha256: a5694e5b01802e5821d03695d386d52d517f922a2c0047e4fa4a4fc0dd921bc8
- evidence_id: EX9
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1096995,1096996,1096997,1231058,1290553,1333660,169215,1716,1747,1869227,2,281915,32008,32033,335058,35493,356,374,401472,41294,41295,48736,504481,50709,563835,629395,6656,75682,75787,7719,80840,80864,82115,85413&retmode=xml
  locator: Exact requested TaxId, AkaTaxIds, ScientificName, Rank and Lineage
  accessed_at: '2026-10-15T07:39:50Z'
  support: supports
  summary: 'NCBI identities and lineages: [{"current_id": "1290553", "current_name":
    "Halocynthiibacter namhaensis", "current_rank": "species", "id": "NCBITaxon:1290553",
    "label": "Halocynthiibacter namhaensis", "lineage": "cellular organisms; Bacteria;
    Pseudomonadati; Pseudomonadota; Alphaproteobacteria; Rhodobacterales; Paracoccaceae;
    Halocynthiibacter"}, {"current_id": "1333660", "current_name": "Endozoicomonas
    atrinae", "current_rank": "species", "id": "NCBITaxon:1333660", "label": "Endozoicomonas
    atrinae", "lineage": "cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota;
    Gammaproteobacteria; Oceanospirillales; Endozoicomonadaceae; Endozoicomonas"},
    {"current_id": "7719", "current_name": "Ciona intestinalis", "current_rank": "species",
    "id": "NCBITaxon:7719", "label": null, "lineage": "cellular organisms; Eukaryota;
    Opisthokonta; Metazoa; Eumetazoa; Bilateria; Deuterostomia; Chordata; Tunicata;
    Ascidiacea; Phlebobranchia; Cionidae; Ciona"}]'
  snapshot_sha256: aea844aa11500f9f43af1b5e0ea2843bd4ef46fd593071067c25e7a85917dcac
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: rg --no-ignore --hidden -l -F -e BTO:0000090 -e ascidian -e ascidian -e
    habitatmech:PREGO.fce17c8a5c curation history research reports data/raw build
    reviews
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
  accessed_at: '2026-10-15T07:59:49Z'
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
  - BTO:0000090
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: concern
  summary: 'Blocker: PREGO self-grounding adopts a whole Ascidiacea organism identity
    as a habitat. The host and its associated environment must remain distinct. The
    three retained taxa include a host organism, not three demonstrated microbial
    inhabitants.'
  target_ids:
  - BTO:0000090
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
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks and
    pools: [{"source": "PREGO", "count": 3, "unit": "TAXON"}]. Zero counts are omitted;
    unrelated parent, bulk and study counts are not added. 3 retained taxon IDs were
    resolved against NCBI, including explicit aliases where noted.'
  target_ids:
  - BTO:0000090
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
- assessment_id: A4
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: No causal edge or characteristic-presence claim is asserted. Missing optional
    parameters/graphs are not evidence deficits. Full source decisions and executed
    routes reproduce SEEDED / EXACT; this review does not promote them.
  target_ids:
  - BTO:0000090
  evidence_ids:
  - E1
  - ESEED
  - ESCHEMA
findings:
- finding_id: F1
  issue_key: ascidian-whole-host-identity
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Whole ascidian organism is adopted as habitat identity
  description: Replace PREGO self-grounding with an evidence-backed decision for habitatmech:PREGO.fce17c8a5c
    that preserves a minted associated-environment identity and keeps BTO organism
    meaning only as context. Audit the three associations before any merge into the
    GOLD ascidian environment. NCBITaxon:7719 is Ciona intestinalis, a host taxon
    allowed as an association but not evidence of a microbial inhabitant; Endozoicomonas
    type-strain pen-shell origin does not prove species-level absence from ascidians.
  target_ids:
  - BTO:0000090
  field_paths:
  - identifier
  - definition
  - parent_habitats
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
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: blocker
  normalization_reason: Whole-organism identity is adopted as the habitat identity,
    contradicting the native host/environment rule.
  external_issues: []
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - BTO:0000090
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  description: Replace PREGO self-grounding with an evidence-backed decision for habitatmech:PREGO.fce17c8a5c
    that preserves a minted associated-environment identity and keeps BTO organism
    meaning only as context. Audit the three associations before any merge into the
    GOLD ascidian environment. NCBITaxon:7719 is Ciona intestinalis, a host taxon
    allowed as an association but not evidence of a microbial inhabitant; Endozoicomonas
    type-strain pen-shell origin does not prove species-level absence from ascidians.
    No repair is performed by this review.
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
