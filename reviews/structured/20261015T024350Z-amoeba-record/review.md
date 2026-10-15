# Record review: amoeba (BTO:0005312)

- Review: 20261015T024350Z-amoeba-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T02:25:03Z
- Finished UTC: 2026-10-15T02:43:50Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One blocker: whole-organism BTO identity is used for the habitat. Seven strain associations, source counts and ranks are faithfully copied and taxonomically valid. A matching laboratory predation study raises an unresolved scope question, but does not justify a second classified finding or deletion of the associations.

## Scope And Provenance

Full individual scientific review of this one resolved generated record, including all contributing source concepts.

Selection: Exact PATHS/identifier resolution in the next unreviewed host-associated cohort; this is not a sample extrapolated to the corpus.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 45c39c0ae63d7825c13b586b8e99e68a396af394.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0005312 | data/habitats/host_associated/amoeba.yaml | generated | amoeba |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0005312 | Actual command passed; started 2026-10-15T02:24:55Z, finished 2026-10-15T02:24:59Z. |
| validate-strict | passed | True | BTO:0005312 | Actual command passed; started 2026-10-15T02:25:03Z, finished 2026-10-15T02:25:14Z. |
| validate-history | passed | True | BTO:0005312 | Actual command passed; started 2026-10-15T02:25:14Z, finished 2026-10-15T02:25:32Z. |
| provenance-check | passed | True | BTO:0005312 | Actual command passed; started 2026-10-15T02:25:32Z, finished 2026-10-15T02:25:33Z. |
| verify-corpus | passed | True | BTO:0005312 | Actual command passed; started 2026-10-15T02:25:33Z, finished 2026-10-15T02:25:59Z. |
| validate-causal-all | passed | True | BTO:0005312 | Actual command passed; started 2026-10-15T02:25:59Z, finished 2026-10-15T02:26:07Z. |
| term-requests-check | passed | True | BTO:0005312 | Actual command passed; started 2026-10-15T02:26:07Z, finished 2026-10-15T02:26:37Z. |
| validate-products | passed | True | BTO:0005312 | Actual command passed; started 2026-10-15T02:26:37Z, finished 2026-10-15T02:28:49Z. |
| iModulonDB applicability | not_applicable | False | BTO:0005312 | No gene/regulator/expression claim in this record; no adapter query was appropriate. |
| Original PREGO pair provenance recovery | unavailable | False | BTO:0005312 | Current frozen TSVs and independent literature can be assessed, but the original pair evidence URLs/member records were not recovered. No pair is removed or declared false on that basis. |

## Scientific And Domain Assessments

### Native validation and generated reproducibility

schema: supported. Targets: BTO:0005312.

Target schema and nine-record strict validation passed. Current 3,208-record corpus reproduces exactly; 726 session histories, 32 graphs and 110 term requests validate. These are structural gates, not biological approval.

### Optional parameters, causal graphs and evidence placement

completeness: not_applicable. Targets: BTO:0005312.

The target contains no environmental parameter, causal graph, dataset or discussion claim. Missing optional slots alone are not findings; no mechanism or characteristic-presence claim is inferred.

### Source counts, taxon identities and ranking

quantity: supported. Targets: BTO:0005312.

The frozen PREGO row has 7 distinct TAXON associations and 7 direct assertions; all 7 displayed taxa are retained with score 3, ranks 1 through 7, candidate_pool 7 and annotated_genomes_isolates channel. No corroborated_by or is_characteristic claim is present. Equal-score order does not establish ecological prominence.

### Source spelling and native status

provenance: supported. Targets: BTO:0005312.

PREGO lexical variants remain RELATED_SYNONYM, not exact ontology equivalences. No target ITEM decision is present in the inspected maintained decisions; EXACT/SEEDED is the deterministic self-grounding state, not a curator sign-off.

### Whole amoeboid organism versus associated habitat

identity: concern. Targets: BTO:0005312.

The BTO identifier, copied definition and protozoan-form parent denote an organism. They cannot serve as exact identity and strict superclass of an associated-environment HabitatRecord.

### Assay versus reported occurrence

evidence: unknown. Targets: BTO:0005312.

Current NCBI verifies all seven strain names and identifiers. The matching primary paper establishes an experimental interaction, but is not proven to be the original PREGO evidence. This does not establish natural colonization, characteristic presence, universal absence, or false source associations.

## Findings

### F1: Whole amoeba identity is used for a habitat

blocker / open / confirmed; issue key: HM-AMOEBA-001.

BTO:0005312 and its BTO:0002503 superclass denote organisms. Keep a genuine host habitat minted and explicitly environment-defined if source evidence supports that reading. Do not equate the informal amoeba grouping with the distinct Amoebozoa clade or delete source associations because original citations are unavailable.

## Recommended Actions And Acceptance Checks

### ACT1

Resolve habitatmech:PREGO.28ae816444 at ITEM depth, distinguishing a living amoeboid host environment from assay apparatus or non-habitat metadata. Retain source provenance and organism context appropriately; do not force SAME_AS to Amoebozoa.

- A corrected habitat identity and its strict parents must denote environments, not whole protozoans; preserve the seven source taxa unless separately evidenced pair-scope correction is authorized.
- Preserve exact source IDs, paths, counts and units; compare affected descendants and unrelated records, not only the target label.
- Append a new session history for any separately authorized curation; never rewrite saved reviews or previous session records.
- Run schema/strict, history, provenance, exact corpus reproduction, causal, term-request and configured label gates, then just qc.
- Check actual semantic-input changes and regenerate map/site/redirect products through supported tooling when required; save an immutable successor with exact finding lineage.

### ACT2

Continue existing investigation #1321 by recovering each original PREGO pair evidence URL and source version. Any qualification or exclusion is conditional on those inspected contexts; no second major/minor finding is established here.

- Distinguish laboratory exposure from original reported-from evidence without claiming either false occurrence or resident/endosymbiotic status from the present paper.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/amoeba.yaml; Entire YAML, including source attestations, synonyms and curation_history | supports | Complete target read; exact identifier, source provenance, grounding, status, parents and optional slots inspected. |
| E2 | docs/CURATION.md; Hosts, anatomy and taxa; decision depth; source-parent and source-label exclusions | supports | A host organism is distinct from its associated environment; anatomical parts may ground normally. Every parent is strictly broader. NOT_APPLICABLE requires evidence about the source concept, not merely an organism-valued match. |
| E3 | src/habitatmech/seed.py; PREGO self-grounding; resolve_gold; source-parent contribution; apply_curated_definitions; generated curation events | supports | Maintained producer explains source-to-record identity, all-source ITEM status, parent contributions and generated history; deterministic reproduction does not certify semantics. |
| E4 | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, assertion_count/unit; characteristic_taxa and is_characteristic | supports | Mapping predicate compares source to record identifier. TAXON and ORGANISM are different units; source-associated taxa are not automatically characteristic. |
| ESEARCH | HabitatMech local ignored-inclusive search; rg --no-ignore --hidden -l -F -e 'Amniotic fluid' -e 'Amniotic sac' -e BTO:0000025 -e BTO:0000062 -e BTO:0000068 -e BTO:0005312 -e amastigote -e 'amniotic cavity' -e 'amniotic fluid' -e amniotic_cavity -e amniotic_fluid -e amniotic_fluid__8d4e7d01 -e amniotic_fluid__ff65cb2e -e amniotic_sac -e amniotic_sac__37392cb1 -e amoeba -e amoebozoa__291e8086 -e 'amoebozoan-associated environment' -e habitatmech:GOLD.1341e74d35 -e habitatmech:GOLD.433d96f0dd -e habitatmech:GOLD.6a7bcba80d -e habitatmech:GOLD.73051a70cb -e habitatmech:GOLD.8a86b174ba -e habitatmech:GOLD.e29c7e3964 -e habitatmech:PREGO.28ae816444 -e habitatmech:PREGO.35c4c18829 -e habitatmech:PREGO.d55bca41f4 -e habitatmech:PREGO.f914cf5ea0 curation history research reports data/raw build reviews | context_only | Search returned 6,494 matching files with exit 0 and no stderr. Exact targets, source mints and source-path table rows were resolved separately; no global absence is inferred. |
| C1E | just validate data/habitats/host_associated/amoeba.yaml; 2026-10-15T02:24:55Z through 2026-10-15T02:24:59Z | supports | No issues found uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/amoeba.yaml |
| C2E | just validate-strict data/habitats/host_associated/amastigote.yaml data/habitats/host_associated/amniotic_cavity.yaml data/habitats/host_associated/amniotic_fluid.yaml data/habitats/host_associated/amniotic_fluid__8d4e7d01.yaml data/habitats/host_associated/amniotic_fluid__ff65cb2e.yaml data/habitats/host_associated/amniotic_sac.yaml data/habitats/host_associated/amniotic_sac__37392cb1.yaml data/habitats/host_associated/amoeba.yaml data/habitats/host_associated/amoebozoa__291e8086.yaml; 2026-10-15T02:25:03Z through 2026-10-15T02:25:14Z | supports | uv run python scripts/validate_strict.py data/habitats/host_associated/amastigote.yaml data/habitats/host_associated/amniotic_cavity.yaml data/habitats/host_associated/amniotic_fluid.yaml data/habitats/host_associated/amniotic_fluid__8d4e7d01.yaml data/habitats/host_associated/amniotic_fluid__ff65cb2e.yaml data/habitats/host_associated/amniotic_sac.yaml data/habitats/host_associated/amniotic_sac__37392cb1.yaml data/habitats/host_associated/amoeba.yaml data/habitats/host_associated/amoebozoa__291e8086.yaml<br>Validating 9 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      9<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| C3E | just validate-history; 2026-10-15T02:25:14Z through 2026-10-15T02:25:32Z | supports | No issues found<br>726 history record(s) valid against src/habitatmech/schema/history.yaml |
| C4E | just provenance-check; 2026-10-15T02:25:32Z through 2026-10-15T02:25:33Z | supports | provenance current: 14 committed inventories, 2 GOLD sources uv run python scripts/check_provenance.py |
| C5E | just verify-corpus; 2026-10-15T02:25:33Z through 2026-10-15T02:25:59Z | supports | expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ uv run python scripts/verify_corpus.py |
| C6E | just validate-causal-all; 2026-10-15T02:25:59Z through 2026-10-15T02:26:07Z | supports | validated 32 causal-graph curation file(s) with 32 graph(s) uv run python scripts/validate_causal_graph_curations.py |
| C7E | just term-requests-check; 2026-10-15T02:26:07Z through 2026-10-15T02:26:37Z | supports | term-request table is current (110 terms) uv run python scripts/build_term_requests.py --check |
| C8E | just validate-products; 2026-10-15T02:26:37Z through 2026-10-15T02:28:49Z | supports | id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond. uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| ELEGACY | reports/yaml_record_review/20261004T001804Z-amoeba.md; Complete historical ad hoc report | context_only | Historical review was read as a lead. Current source evidence and current maintained owners control this verdict; old validator counts and implementation availability are not reused. |
| EPREGO | data/raw/prego_habitats.tsv; Rows 361 | supports | {"biolink_category": "biolink:GrossAnatomicalStructure", "channels": "annotated_genomes_isolates", "direct_assertion_count": "7", "max_prego_score": "3", "ontology": "BTO", "prego_id": "BTO:0005312", "prego_synonyms": "amoeba&#124;amoebal&#124;amoebas", "taxon_count": "7"} |
| ETAXAROWS | data/raw/prego_habitat_taxa.tsv; Rows 2925, 2926, 2927, 2928, 2929, 2930, 2931 | supports | {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0005312", "prego_score": "3", "rank": "1", "taxon_id": "NCBITaxon:1408271", "taxon_label": "Pseudomonas aeruginosa LES400"}; {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0005312", "prego_score": "3", "rank": "2", "taxon_id": "NCBITaxon:1408272", "taxon_label": "Pseudomonas aeruginosa LES431"}; {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0005312", "prego_score": "3", "rank": "3", "taxon_id": "NCBITaxon:1408273", "taxon_label": "Pseudomonas aeruginosa LESB65"}; {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0005312", "prego_score": "3", "rank": "4", "taxon_id": "NCBITaxon:1408274", "taxon_label": "Pseudomonas aeruginosa LESlike1"}; {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0005312", "prego_score": "3", "rank": "5", "taxon_id": "NCBITaxon:1408275", "taxon_label": "Pseudomonas aeruginosa LESlike4"}; {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0005312", "prego_score": "3", "rank": "6", "taxon_id": "NCBITaxon:1408276", "taxon_label": "Pseudomonas aeruginosa LESlike5"}; {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0005312", "prego_score": "3", "rank": "7", "taxon_id": "NCBITaxon:1408277", "taxon_label": "Pseudomonas aeruginosa LESlike7"} |
| ESLICE | data/raw/ontology_terms.tsv; Rows 5311 | supports | {"definition": "Any of various one-celled aquatic or parasitic protozoans of the genus amoeba or related genera, having no definite form and consisting of a mass of protoplasm containing one or more nuclei surrounded by a flexible outer membrane. It moves by means of pseudopods.", "deprecated": "", "directly_referenced": "TRUE", "label": "amoeba", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0005312"} |
| EONTO | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0005312; label, description, obsolete flag | supports | Current OLS identity/label and definition agree with the source term; ontology meaning is assessed separately from habitat eligibility. |
| EGRAPH | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0005312/graph; nodes and typed edges | supports | Typed ontology edges distinguish subclass from containment and part_of; only genuine broader habitats belong in parent_habitats. |
| ETAXON | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1408271,1408272,1408273,1408274,1408275,1408276,1408277,2098,353153,554915; Top-level Taxon entries for NCBITaxon:1408271, NCBITaxon:1408272, NCBITaxon:1408273, NCBITaxon:1408274, NCBITaxon:1408275, NCBITaxon:1408276, NCBITaxon:1408277 | supports | NCBI canonical identities and ranks inspected for every displayed target taxon; historical Mycoplasma hominis nomenclature reconciled where applicable. |
| EEXTRACT | src/habitatmech/extract.py; extract_prego, lines 338-437 | supports | Retains best score/direct/channel per habitat-taxon pair, orders score then direct flag then taxon ID, and keeps top-N pairs. Pair evidence URLs and publication/member context are not retained in these TSV fields. |
| EUPSEARCH | Configured local kg-microbe checkout; find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe -ipath '*prego*' -type f | context_only | find completed with exit 0, no matching files and no stderr; this confirms only the bounded local payload availability limitation. |
| EPARENT | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0002503; label and definition | supports | The direct superclass explicitly denotes an individual protozoan, not its associated environment. |
| EPAPER | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3914812/fullTextXML; PMID24505294; DOI10.1371/journal.pone.0087611; introduction, Table1, predation assay methods and Figure7 | context_only | Jeukens et al. study the same seven LES strains as human clinical isolates and test their interaction with Dictyostelium in a bacterial-lawn predation assay. This paper is an assay-scope warning, not a recovered original PREGO citation. |
| EIDENTITY | https://github.com/CultureBotAI/HabitatMech/issues/1320; Issue body and relevant comments; state OPEN | context_only | Existing open identity repair remains supported by current ontology and record content. |
| EINVESTIGATION | https://github.com/CultureBotAI/HabitatMech/issues/1321; Issue body and relevant comments; state OPEN | context_only | Open investigation seeks original pair context; it does not establish that the seven associations are false. |
| ECORRECTION | https://github.com/CultureBotAI/HabitatMech/issues/1322; Issue body and relevant comments; state CLOSED | context_only | Closed review-correction issue explicitly removed unsupported major severity from the assay-versus-occurrence concern. This review preserves that distinction. |

## Limits And Additional Notes

- This completed observation does not promote native mapping_status, curate a record, close an issue, or certify the unreviewed corpus.
- Configured id-label validation passed but skips 2,061 no-adapter pairs. Canonical correspondence is not proof of biological identity, source membership or relation direction.
- The full just qc suite was not rerun for these review-only additions. Native record checks are recorded in this review; immutable-bundle validation and the append-only archive check are separate publication verification.
- No paid research was used. iModulonDB is not applicable because this target has no gene, regulator or expression claim; contextual genomic papers are not imported as mechanisms.
- Original PREGO pair-level evidence/member payload is unavailable in the retained inventories. An ignored-inclusive find of the configured kg-microbe checkout found no files with prego in their path; this is a bounded availability result, not proof the evidence does not exist elsewhere.
- All target fields were read. Source input hashes were captured before assessment and rechecked unchanged during supplemental inspection at 2026-10-15T02:37:32Z.
- The ignored-inclusive native review search found no earlier structured observation targeting this identifier. Historical Markdown is retained as evidence, not fabricated previous_occurrences.
- This review assesses the exact recorded main revision, whose captured inputs were each verified against git show blobs and still match the working tree. External responses are identified by retrieval URL, access time and SHA-256, not silently vendored into domain inputs.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T024350Z-amoeba-record
kind: record
repository: CultureBotAI/HabitatMech
title: 'Record review: amoeba (BTO:0005312)'
started_at: '2026-10-15T02:25:03Z'
finished_at: '2026-10-15T02:43:50Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Continuing review agent. Complete target and maintained inputs
    were independently reassessed from historical leads, but this is not independent
    human or second-agent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'One blocker: whole-organism BTO identity is used for the habitat. Seven
  strain associations, source counts and ranks are faithfully copied and taxonomically
  valid. A matching laboratory predation study raises an unresolved scope question,
  but does not justify a second classified finding or deletion of the associations.'
source:
  git_revision: 45c39c0ae63d7825c13b586b8e99e68a396af394
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
    sha256: d9c76d275d61b7fef860179b6d0472e54e15b2b027022d7a125a19f03881fd8e
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 505e6efc536392c9f6ce77fd4a70284392166269713189ff53e40367256d2899
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 41d223485ac848fcb5a724dc308caba88e922ae89c972ca9f92565ff3b753f32
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: 144e48a101aa072a96cd08f88a9a66ecd14122d788c54b95ac8ad7d934f720bc
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: 034aee0bcf71e9c813d20450bc93d7f3f6070cab0ddebfe6f3f39911e7c6b0e1
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: b0135af0aa4deed0f3824a2f491d5a742c1b7de4775c533f283761d22e805821
    role: context
  - path: data/habitats/host_associated/amastigote.yaml
    sha256: 6d3d3c8374415178937a2419506cdfb0582ea4c08d07cb5215f74902d08f97f4
    role: context
  - path: data/habitats/host_associated/amniotic_cavity.yaml
    sha256: 869a370aa694df7ce5798419d2056d8096e764e6391e786c16f537d299b2ce0d
    role: context
  - path: data/habitats/host_associated/amniotic_fluid.yaml
    sha256: 0d11095a2414faa717c2aa11ee3cf33ad2afd1239bcdefcad8ebd0de4b0861f3
    role: context
  - path: data/habitats/host_associated/amniotic_fluid__8d4e7d01.yaml
    sha256: 9add117b1972de6df3d191ecca89627e67baccba58696f834ee6e68b4b882ff8
    role: context
  - path: data/habitats/host_associated/amniotic_fluid__ff65cb2e.yaml
    sha256: 320bb4a3d5dd9bb434b328892c818fd2f4a2d5bb50e1c9377c544766b32ef10d
    role: context
  - path: data/habitats/host_associated/amniotic_sac.yaml
    sha256: 014ec22a262fbf857f84e72a8082e5496ccc75f80aeb8f471faffd7a04db20c5
    role: context
  - path: data/habitats/host_associated/amniotic_sac__37392cb1.yaml
    sha256: efebe500871039e24dfad94951f1e6db0ab141ecf0841b0d1aee55414541167c
    role: context
  - path: data/habitats/host_associated/amoeba.yaml
    sha256: b992fbfdaa3229fd2f0709ebe4e87bb2db6060587e0272f68713d58a82d64010
    role: target
  - path: data/habitats/host_associated/amoebozoa__291e8086.yaml
    sha256: 1c975174212a2b64de76f87e960fde508a5dcd1161ba7d26fac3f6cba14910fc
    role: context
  - path: data/habitats/host_associated/environmental_system_determined_by_an_organism.yaml
    sha256: d3b79ef9436a87fbce8e6b204b0113e170fa758e4a66efb592543bf934c67270
    role: context
  - path: data/habitats/host_associated/fetal_tissue__610eb0c8.yaml
    sha256: 9b3cf56fdaa5e4afcf82f5c20eca9e0c7216bd28b9e4ec82caded85ea2d79aae
    role: context
  - path: data/habitats/host_associated/fetus.yaml
    sha256: cda704d0cd49b4dbd5fa4e7bf2c6e6e0e4f8ee23c52ffcaa639c16c4e441c247
    role: context
  - path: data/habitats/host_associated/fetus__250e9844.yaml
    sha256: 1de36aaf5d6ba77a218d90b8733c18252b8935c2bf9a855c1bd24c8890d7a60d
    role: context
  - path: data/habitats/host_associated/protists.yaml
    sha256: 36cc3b7d0ac6b3e67e4522db0b9661bb38d978f0ae2907ea8a6f073c3c3a7047
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
  - path: history/mappings/amoebozoa/2026-09-08T080050Z-claude-code-ca3c8d.yaml
    sha256: 028d9dab9c5d62a38d2030b44b87e5c4baafbdceda4501f468c92dbba66210a0
    role: context
  - path: history/mappings/amoebozoa/2026-09-10T103332Z-claude-code-3f93ba.yaml
    sha256: 325141765eb7997da2c21c81872bc18594b8dd3643473d357c389468928fdd9b
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20261002T103738Z-amniotic_cavity.md
    sha256: bbe3e1d3ab7a4bf7e5b7722f01ab9179803e59c68abcc93044effe40536303e5
    role: context
  - path: reports/yaml_record_review/20261002T113212Z-amastigote.md
    sha256: 01652170d30fd71918e37cb570101096da4d7b82b84c670c2288e244d94abf5c
    role: context
  - path: reports/yaml_record_review/20261002T120005Z-amniotic_fluid.md
    sha256: d774ec3f26ddded413799970accdd21bb29c3484281a175e7cef261180e3b92f
    role: context
  - path: reports/yaml_record_review/20261004T000226Z-amniotic_fluid__8d4e7d01.md
    sha256: fdb5a4e46d03825e3bc0e98d1ad633d7e6b71d2e049aafb75ab11f27265b3929
    role: context
  - path: reports/yaml_record_review/20261004T000448Z-amniotic_fluid__ff65cb2e.md
    sha256: e6a14e0359f875cd0144b067bc34290751b97eb3ea0a7c5a1d805ba1dd126054
    role: context
  - path: reports/yaml_record_review/20261004T000806Z-amniotic_sac.md
    sha256: 867834ed1d6829ab2e9b38a7256f427bfc2093978a020d5bff2caa31ed8f2bc5
    role: context
  - path: reports/yaml_record_review/20261004T001013Z-amniotic_sac__37392cb1.md
    sha256: 0d5a42a3ba45fbf136d89402379af9e549341372206ffbe9f73b5d8828df71a5
    role: context
  - path: reports/yaml_record_review/20261004T001804Z-amoeba.md
    sha256: 0e9c926afad7674377690db5aa55959888eddfe621e9538d53f7c5e3860d3670
    role: context
  - path: reports/yaml_record_review/20261004T004156Z-amoebozoa__291e8086.md
    sha256: bdf2dd5b74838c394d6b9ac87e5dafc9fe3fb92eb735d4b9f01a63a6a9ba8127
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/aggregate_gold_triads.py
    sha256: 0e25179dbecd7c73cbedd99a0ae44e56e4992afb9e1ec02d2411439f643b8e54
    role: context
  - path: scripts/extract_gold_biosamples.py
    sha256: b6a2773c86fe718e1ca0b1d7b32709f0eee491ac813655e310aa0817c0fec31b
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
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
- target_id: BTO:0005312
  path: data/habitats/host_associated/amoeba.yaml
  label: amoeba
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained curation input or implementation; never patch generated habitat
      YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained curation input or implementation; never patch generated habitat
      YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained curation input or implementation; never patch generated habitat
      YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained curation input or implementation; never patch generated habitat
      YAML
scope:
  description: Full individual scientific review of this one resolved generated record,
    including all contributing source concepts.
  selection: Exact PATHS/identifier resolution in the next unreviewed host-associated
    cohort; this is not a sample extrapolated to the corpus.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - BTO:0005312
  exclusions:
  - target: Other HabitatMech records and SSSOM/KGX products
    reason: Referenced parents and neighboring concepts are inspected only as dependencies,
      not certified as complete individual reviews or export conformance.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/amoeba.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0005312
  evidence_ids:
  - C1E
  summary: Actual command passed; started 2026-10-15T02:24:55Z, finished 2026-10-15T02:24:59Z.
  scope_note: Target-only schema; the strict command names nine targets. History,
    provenance, corpus, causal, term requests and label correspondence use their documented
    wider scopes.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/amastigote.yaml data/habitats/host_associated/amniotic_cavity.yaml
    data/habitats/host_associated/amniotic_fluid.yaml data/habitats/host_associated/amniotic_fluid__8d4e7d01.yaml
    data/habitats/host_associated/amniotic_fluid__ff65cb2e.yaml data/habitats/host_associated/amniotic_sac.yaml
    data/habitats/host_associated/amniotic_sac__37392cb1.yaml data/habitats/host_associated/amoeba.yaml
    data/habitats/host_associated/amoebozoa__291e8086.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0005312
  evidence_ids:
  - C2E
  summary: Actual command passed; started 2026-10-15T02:25:03Z, finished 2026-10-15T02:25:14Z.
  scope_note: Target-only schema; the strict command names nine targets. History,
    provenance, corpus, causal, term requests and label correspondence use their documented
    wider scopes.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0005312
  evidence_ids:
  - C3E
  summary: Actual command passed; started 2026-10-15T02:25:14Z, finished 2026-10-15T02:25:32Z.
  scope_note: Target-only schema; the strict command names nine targets. History,
    provenance, corpus, causal, term requests and label correspondence use their documented
    wider scopes.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0005312
  evidence_ids:
  - C4E
  summary: Actual command passed; started 2026-10-15T02:25:32Z, finished 2026-10-15T02:25:33Z.
  scope_note: Target-only schema; the strict command names nine targets. History,
    provenance, corpus, causal, term requests and label correspondence use their documented
    wider scopes.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0005312
  evidence_ids:
  - C5E
  summary: Actual command passed; started 2026-10-15T02:25:33Z, finished 2026-10-15T02:25:59Z.
  scope_note: Target-only schema; the strict command names nine targets. History,
    provenance, corpus, causal, term requests and label correspondence use their documented
    wider scopes.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0005312
  evidence_ids:
  - C6E
  summary: Actual command passed; started 2026-10-15T02:25:59Z, finished 2026-10-15T02:26:07Z.
  scope_note: Target-only schema; the strict command names nine targets. History,
    provenance, corpus, causal, term requests and label correspondence use their documented
    wider scopes.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0005312
  evidence_ids:
  - C7E
  summary: Actual command passed; started 2026-10-15T02:26:07Z, finished 2026-10-15T02:26:37Z.
  scope_note: Target-only schema; the strict command names nine targets. History,
    provenance, corpus, causal, term requests and label correspondence use their documented
    wider scopes.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0005312
  evidence_ids:
  - C8E
  summary: Actual command passed; started 2026-10-15T02:26:37Z, finished 2026-10-15T02:28:49Z.
  scope_note: Target-only schema; the strict command names nine targets. History,
    provenance, corpus, causal, term requests and label correspondence use their documented
    wider scopes.
- check_id: CIMOD
  name: iModulonDB applicability
  status: not_applicable
  required: false
  summary: No gene/regulator/expression claim in this record; no adapter query was
    appropriate.
  target_ids:
  - BTO:0005312
  evidence_ids:
  - E1
- check_id: CORIGINAL
  name: Original PREGO pair provenance recovery
  status: unavailable
  required: false
  summary: Current frozen TSVs and independent literature can be assessed, but the
    original pair evidence URLs/member records were not recovered. No pair is removed
    or declared false on that basis.
  target_ids:
  - BTO:0005312
  evidence_ids:
  - EEXTRACT
  - ETAXAROWS
  - EUPSEARCH
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/amoeba.yaml
  locator: Entire YAML, including source attestations, synonyms and curation_history
  accessed_at: '2026-10-15T02:43:50Z'
  support: supports
  summary: Complete target read; exact identifier, source provenance, grounding, status,
    parents and optional slots inspected.
  snapshot_sha256: b992fbfdaa3229fd2f0709ebe4e87bb2db6060587e0272f68713d58a82d64010
- evidence_id: E2
  kind: authority
  reference: docs/CURATION.md
  locator: Hosts, anatomy and taxa; decision depth; source-parent and source-label
    exclusions
  accessed_at: '2026-10-15T02:43:50Z'
  support: supports
  summary: A host organism is distinct from its associated environment; anatomical
    parts may ground normally. Every parent is strictly broader. NOT_APPLICABLE requires
    evidence about the source concept, not merely an organism-valued match.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: E3
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: PREGO self-grounding; resolve_gold; source-parent contribution; apply_curated_definitions;
    generated curation events
  accessed_at: '2026-10-15T02:43:50Z'
  support: supports
  summary: Maintained producer explains source-to-record identity, all-source ITEM
    status, parent contributions and generated history; deterministic reproduction
    does not certify semantics.
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: E4
  kind: record_content
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, assertion_count/unit; characteristic_taxa
    and is_characteristic
  accessed_at: '2026-10-15T02:43:50Z'
  support: supports
  summary: Mapping predicate compares source to record identifier. TAXON and ORGANISM
    are different units; source-associated taxa are not automatically characteristic.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEARCH
  kind: search
  reference: HabitatMech local ignored-inclusive search
  locator: rg --no-ignore --hidden -l -F -e 'Amniotic fluid' -e 'Amniotic sac' -e
    BTO:0000025 -e BTO:0000062 -e BTO:0000068 -e BTO:0005312 -e amastigote -e 'amniotic
    cavity' -e 'amniotic fluid' -e amniotic_cavity -e amniotic_fluid -e amniotic_fluid__8d4e7d01
    -e amniotic_fluid__ff65cb2e -e amniotic_sac -e amniotic_sac__37392cb1 -e amoeba
    -e amoebozoa__291e8086 -e 'amoebozoan-associated environment' -e habitatmech:GOLD.1341e74d35
    -e habitatmech:GOLD.433d96f0dd -e habitatmech:GOLD.6a7bcba80d -e habitatmech:GOLD.73051a70cb
    -e habitatmech:GOLD.8a86b174ba -e habitatmech:GOLD.e29c7e3964 -e habitatmech:PREGO.28ae816444
    -e habitatmech:PREGO.35c4c18829 -e habitatmech:PREGO.d55bca41f4 -e habitatmech:PREGO.f914cf5ea0
    curation history research reports data/raw build reviews
  accessed_at: '2026-10-15T02:25:06Z'
  support: context_only
  summary: Search returned 6,494 matching files with exit 0 and no stderr. Exact targets,
    source mints and source-path table rows were resolved separately; no global absence
    is inferred.
  search_scope: Ignored and hidden files included under curation, history, research,
    reports, data/raw, build and reviews. Complete TSV parsing and native review traversal
    supplement these text hits; outside repositories are not covered by this search.
- evidence_id: C1E
  kind: validation
  reference: just validate data/habitats/host_associated/amoeba.yaml
  locator: 2026-10-15T02:24:55Z through 2026-10-15T02:24:59Z
  accessed_at: '2026-10-15T02:24:59Z'
  support: supports
  summary: No issues found uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml
    --target-class HabitatRecord data/habitats/host_associated/amoeba.yaml
- evidence_id: C2E
  kind: validation
  reference: just validate-strict data/habitats/host_associated/amastigote.yaml data/habitats/host_associated/amniotic_cavity.yaml
    data/habitats/host_associated/amniotic_fluid.yaml data/habitats/host_associated/amniotic_fluid__8d4e7d01.yaml
    data/habitats/host_associated/amniotic_fluid__ff65cb2e.yaml data/habitats/host_associated/amniotic_sac.yaml
    data/habitats/host_associated/amniotic_sac__37392cb1.yaml data/habitats/host_associated/amoeba.yaml
    data/habitats/host_associated/amoebozoa__291e8086.yaml
  locator: 2026-10-15T02:25:03Z through 2026-10-15T02:25:14Z
  accessed_at: '2026-10-15T02:25:14Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/habitats/host_associated/amastigote.yaml\
    \ data/habitats/host_associated/amniotic_cavity.yaml data/habitats/host_associated/amniotic_fluid.yaml\
    \ data/habitats/host_associated/amniotic_fluid__8d4e7d01.yaml data/habitats/host_associated/amniotic_fluid__ff65cb2e.yaml\
    \ data/habitats/host_associated/amniotic_sac.yaml data/habitats/host_associated/amniotic_sac__37392cb1.yaml\
    \ data/habitats/host_associated/amoeba.yaml data/habitats/host_associated/amoebozoa__291e8086.yaml\n\
    Validating 9 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      9\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
- evidence_id: C3E
  kind: validation
  reference: just validate-history
  locator: 2026-10-15T02:25:14Z through 2026-10-15T02:25:32Z
  accessed_at: '2026-10-15T02:25:32Z'
  support: supports
  summary: 'No issues found

    726 history record(s) valid against src/habitatmech/schema/history.yaml'
- evidence_id: C4E
  kind: validation
  reference: just provenance-check
  locator: 2026-10-15T02:25:32Z through 2026-10-15T02:25:33Z
  accessed_at: '2026-10-15T02:25:33Z'
  support: supports
  summary: 'provenance current: 14 committed inventories, 2 GOLD sources uv run python
    scripts/check_provenance.py'
- evidence_id: C5E
  kind: validation
  reference: just verify-corpus
  locator: 2026-10-15T02:25:33Z through 2026-10-15T02:25:59Z
  accessed_at: '2026-10-15T02:25:59Z'
  support: supports
  summary: "expected 3208 records, found 3208 on disk\n  missing:   0\n  extra:  \
    \   0\n  differing: 0\n\ncorpus reproduces exactly from data/raw/ uv run python\
    \ scripts/verify_corpus.py"
- evidence_id: C6E
  kind: validation
  reference: just validate-causal-all
  locator: 2026-10-15T02:25:59Z through 2026-10-15T02:26:07Z
  accessed_at: '2026-10-15T02:26:07Z'
  support: supports
  summary: validated 32 causal-graph curation file(s) with 32 graph(s) uv run python
    scripts/validate_causal_graph_curations.py
- evidence_id: C7E
  kind: validation
  reference: just term-requests-check
  locator: 2026-10-15T02:26:07Z through 2026-10-15T02:26:37Z
  accessed_at: '2026-10-15T02:26:37Z'
  support: supports
  summary: term-request table is current (110 terms) uv run python scripts/build_term_requests.py
    --check
- evidence_id: C8E
  kind: validation
  reference: just validate-products
  locator: 2026-10-15T02:26:37Z through 2026-10-15T02:28:49Z
  accessed_at: '2026-10-15T02:28:49Z'
  support: supports
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 1174\n     \
    \       OK_SYNONYM: 1\n          OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2061\n\
    \n✅ All id↔label pairs correspond. uv run python scripts/validate_id_label_correspondence.py\
    \ -c conf/id_label_targets.yaml"
- evidence_id: ELEGACY
  kind: prior_review
  reference: reports/yaml_record_review/20261004T001804Z-amoeba.md
  locator: Complete historical ad hoc report
  accessed_at: '2026-10-15T02:43:50Z'
  support: context_only
  summary: Historical review was read as a lead. Current source evidence and current
    maintained owners control this verdict; old validator counts and implementation
    availability are not reused.
  snapshot_sha256: 0e9c926afad7674377690db5aa55959888eddfe621e9538d53f7c5e3860d3670
- evidence_id: EPREGO
  kind: database
  reference: data/raw/prego_habitats.tsv
  locator: Rows 361
  accessed_at: '2026-10-15T02:43:50Z'
  support: supports
  summary: '{"biolink_category": "biolink:GrossAnatomicalStructure", "channels": "annotated_genomes_isolates",
    "direct_assertion_count": "7", "max_prego_score": "3", "ontology": "BTO", "prego_id":
    "BTO:0005312", "prego_synonyms": "amoeba|amoebal|amoebas", "taxon_count": "7"}'
  snapshot_sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
- evidence_id: ETAXAROWS
  kind: database
  reference: data/raw/prego_habitat_taxa.tsv
  locator: Rows 2925, 2926, 2927, 2928, 2929, 2930, 2931
  accessed_at: '2026-10-15T02:43:50Z'
  support: supports
  summary: '{"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "BTO:0005312", "prego_score": "3", "rank": "1", "taxon_id":
    "NCBITaxon:1408271", "taxon_label": "Pseudomonas aeruginosa LES400"}; {"channels":
    "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "BTO:0005312", "prego_score": "3", "rank": "2", "taxon_id": "NCBITaxon:1408272",
    "taxon_label": "Pseudomonas aeruginosa LES431"}; {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0005312", "prego_score":
    "3", "rank": "3", "taxon_id": "NCBITaxon:1408273", "taxon_label": "Pseudomonas
    aeruginosa LESB65"}; {"channels": "annotated_genomes_isolates", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "BTO:0005312", "prego_score": "3", "rank":
    "4", "taxon_id": "NCBITaxon:1408274", "taxon_label": "Pseudomonas aeruginosa LESlike1"};
    {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "BTO:0005312", "prego_score": "3", "rank": "5", "taxon_id":
    "NCBITaxon:1408275", "taxon_label": "Pseudomonas aeruginosa LESlike4"}; {"channels":
    "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "BTO:0005312", "prego_score": "3", "rank": "6", "taxon_id": "NCBITaxon:1408276",
    "taxon_label": "Pseudomonas aeruginosa LESlike5"}; {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0005312", "prego_score":
    "3", "rank": "7", "taxon_id": "NCBITaxon:1408277", "taxon_label": "Pseudomonas
    aeruginosa LESlike7"}'
  snapshot_sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
- evidence_id: ESLICE
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Rows 5311
  accessed_at: '2026-10-15T02:43:50Z'
  support: supports
  summary: '{"definition": "Any of various one-celled aquatic or parasitic protozoans
    of the genus amoeba or related genera, having no definite form and consisting
    of a mass of protoplasm containing one or more nuclei surrounded by a flexible
    outer membrane. It moves by means of pseudopods.", "deprecated": "", "directly_referenced":
    "TRUE", "label": "amoeba", "label_only": "FALSE", "ontology": "BTO", "synonyms":
    "", "term_id": "BTO:0005312"}'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTO
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0005312
  locator: label, description, obsolete flag
  accessed_at: '2026-10-15T02:27:36Z'
  support: supports
  summary: Current OLS identity/label and definition agree with the source term; ontology
    meaning is assessed separately from habitat eligibility.
  snapshot_sha256: d17ea9cd5c48421ce64bd72b0c39b6dd9e2555444d5bbd7ed11a43e8f2180f75
- evidence_id: EGRAPH
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0005312/graph
  locator: nodes and typed edges
  accessed_at: '2026-10-15T02:35:06Z'
  support: supports
  summary: Typed ontology edges distinguish subclass from containment and part_of;
    only genuine broader habitats belong in parent_habitats.
  snapshot_sha256: 9d76d8baaa9da3501ba139cb2d95f92aed874d04171c6ce9dd7ffe8590aad762
- evidence_id: ETAXON
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1408271,1408272,1408273,1408274,1408275,1408276,1408277,2098,353153,554915
  locator: Top-level Taxon entries for NCBITaxon:1408271, NCBITaxon:1408272, NCBITaxon:1408273,
    NCBITaxon:1408274, NCBITaxon:1408275, NCBITaxon:1408276, NCBITaxon:1408277
  accessed_at: '2026-10-15T02:27:41Z'
  support: supports
  summary: NCBI canonical identities and ranks inspected for every displayed target
    taxon; historical Mycoplasma hominis nomenclature reconciled where applicable.
  snapshot_sha256: 9c177420cf4d21729c2b5f604220caff180ce97ca3f438e7638e76fe1b57d314
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: extract_prego, lines 338-437
  accessed_at: '2026-10-15T02:43:50Z'
  support: supports
  summary: Retains best score/direct/channel per habitat-taxon pair, orders score
    then direct flag then taxon ID, and keeps top-N pairs. Pair evidence URLs and
    publication/member context are not retained in these TSV fields.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: EUPSEARCH
  kind: search
  reference: Configured local kg-microbe checkout
  locator: find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe
    -ipath '*prego*' -type f
  accessed_at: '2026-10-15T02:43:30Z'
  support: context_only
  summary: find completed with exit 0, no matching files and no stderr; this confirms
    only the bounded local payload availability limitation.
  search_scope: All files beneath the configured checkout, including ignored and hidden
    paths, whose paths contain prego. No claim about remote sources or alternate checkouts.
- evidence_id: EPARENT
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0002503
  locator: label and definition
  accessed_at: '2026-10-15T02:27:36Z'
  support: supports
  summary: The direct superclass explicitly denotes an individual protozoan, not its
    associated environment.
  snapshot_sha256: 28781ce5955bd77e3e843797f6de241786719e9fdea282d93164e5cac62f9c4f
- evidence_id: EPAPER
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3914812/fullTextXML
  locator: PMID24505294; DOI10.1371/journal.pone.0087611; introduction, Table1, predation
    assay methods and Figure7
  accessed_at: '2026-10-15T02:27:43Z'
  support: context_only
  summary: Jeukens et al. study the same seven LES strains as human clinical isolates
    and test their interaction with Dictyostelium in a bacterial-lawn predation assay.
    This paper is an assay-scope warning, not a recovered original PREGO citation.
  snapshot_sha256: 6f32c6909cb550ef989f31262ca8854477193b3813ced46cc6fd3827af944634
- evidence_id: EIDENTITY
  kind: prior_review
  reference: https://github.com/CultureBotAI/HabitatMech/issues/1320
  locator: Issue body and relevant comments; state OPEN
  accessed_at: '2026-10-15T02:35:09Z'
  support: context_only
  summary: Existing open identity repair remains supported by current ontology and
    record content.
- evidence_id: EINVESTIGATION
  kind: prior_review
  reference: https://github.com/CultureBotAI/HabitatMech/issues/1321
  locator: Issue body and relevant comments; state OPEN
  accessed_at: '2026-10-15T02:35:10Z'
  support: context_only
  summary: Open investigation seeks original pair context; it does not establish that
    the seven associations are false.
- evidence_id: ECORRECTION
  kind: prior_review
  reference: https://github.com/CultureBotAI/HabitatMech/issues/1322
  locator: Issue body and relevant comments; state CLOSED
  accessed_at: '2026-10-15T02:35:10Z'
  support: context_only
  summary: Closed review-correction issue explicitly removed unsupported major severity
    from the assay-versus-occurrence concern. This review preserves that distinction.
assessments:
- assessment_id: A1
  area: schema
  topic: Native validation and generated reproducibility
  outcome: supported
  summary: Target schema and nine-record strict validation passed. Current 3,208-record
    corpus reproduces exactly; 726 session histories, 32 graphs and 110 term requests
    validate. These are structural gates, not biological approval.
  target_ids:
  - BTO:0005312
  evidence_ids:
  - C1E
  - C2E
  - C3E
  - C4E
  - C5E
  - C6E
  - C7E
  - C8E
- assessment_id: A2
  area: completeness
  topic: Optional parameters, causal graphs and evidence placement
  outcome: not_applicable
  summary: The target contains no environmental parameter, causal graph, dataset or
    discussion claim. Missing optional slots alone are not findings; no mechanism
    or characteristic-presence claim is inferred.
  target_ids:
  - BTO:0005312
  evidence_ids:
  - E1
  - ESEARCH
- assessment_id: A3
  area: quantity
  topic: Source counts, taxon identities and ranking
  outcome: supported
  summary: The frozen PREGO row has 7 distinct TAXON associations and 7 direct assertions;
    all 7 displayed taxa are retained with score 3, ranks 1 through 7, candidate_pool
    7 and annotated_genomes_isolates channel. No corroborated_by or is_characteristic
    claim is present. Equal-score order does not establish ecological prominence.
  target_ids:
  - BTO:0005312
  evidence_ids:
  - EPREGO
  - ETAXAROWS
  - ETAXON
  - E4
  - EEXTRACT
  metrics:
  - name: Retained source taxa
    value: 7
    unit: distinct PREGO TAXON identifiers
    definition: Displayed taxon associations divided by the frozen PREGO candidate
      pool; not prevalence or abundance.
    denominator: 7
  dimensions:
  - name: source-curation-key
    value: habitatmech:PREGO.28ae816444
    definition: Minted PREGO key for an ITEM decision; not the current self-grounded
      BTO record ID.
    evidence_ids:
    - EPREGO
    - E3
  - name: evidence-channel
    value: annotated_genomes_isolates
    definition: Upstream channel label, not independent proof of sampled habitat occurrence.
    evidence_ids:
    - EPREGO
    - ETAXAROWS
- assessment_id: A4
  area: provenance
  topic: Source spelling and native status
  outcome: supported
  summary: PREGO lexical variants remain RELATED_SYNONYM, not exact ontology equivalences.
    No target ITEM decision is present in the inspected maintained decisions; EXACT/SEEDED
    is the deterministic self-grounding state, not a curator sign-off.
  target_ids:
  - BTO:0005312
  evidence_ids:
  - E1
  - EPREGO
  - E3
  - ESEARCH
- assessment_id: A5
  area: identity
  topic: Whole amoeboid organism versus associated habitat
  outcome: concern
  summary: The BTO identifier, copied definition and protozoan-form parent denote
    an organism. They cannot serve as exact identity and strict superclass of an associated-environment
    HabitatRecord.
  target_ids:
  - BTO:0005312
  evidence_ids:
  - EONTO
  - EGRAPH
  - EPARENT
  - E2
- assessment_id: A6
  area: evidence
  topic: Assay versus reported occurrence
  outcome: unknown
  summary: Current NCBI verifies all seven strain names and identifiers. The matching
    primary paper establishes an experimental interaction, but is not proven to be
    the original PREGO evidence. This does not establish natural colonization, characteristic
    presence, universal absence, or false source associations.
  target_ids:
  - BTO:0005312
  evidence_ids:
  - EPAPER
  - ETAXON
  - ETAXAROWS
  - EINVESTIGATION
  - ECORRECTION
findings:
- finding_id: F1
  issue_key: HM-AMOEBA-001
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Whole amoeba identity is used for a habitat
  description: BTO:0005312 and its BTO:0002503 superclass denote organisms. Keep a
    genuine host habitat minted and explicitly environment-defined if source evidence
    supports that reading. Do not equate the informal amoeba grouping with the distinct
    Amoebozoa clade or delete source associations because original citations are unavailable.
  target_ids:
  - BTO:0005312
  field_paths:
  - identifier
  - definition
  - grounding_status
  - parent_habitats
  evidence_ids:
  - E1
  - EONTO
  - EPARENT
  - E2
  rule_id: 'docs/CURATION.md: semantic habitat and strictly-broader hierarchy rules'
  native_severity: blocker
  normalization_reason: Native severity agrees with the shared record-review rubric.
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained curation input or implementation; never patch generated habitat
      YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained curation input or implementation; never patch generated habitat
      YAML
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1320
actions:
- action_id: ACT1
  description: Resolve habitatmech:PREGO.28ae816444 at ITEM depth, distinguishing
    a living amoeboid host environment from assay apparatus or non-habitat metadata.
    Retain source provenance and organism context appropriately; do not force SAME_AS
    to Amoebozoa.
  finding_ids:
  - F1
  target_ids:
  - BTO:0005312
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained curation input or implementation; never patch generated habitat
      YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained curation input or implementation; never patch generated habitat
      YAML
  acceptance_checks:
  - A corrected habitat identity and its strict parents must denote environments,
    not whole protozoans; preserve the seven source taxa unless separately evidenced
    pair-scope correction is authorized.
  - Preserve exact source IDs, paths, counts and units; compare affected descendants
    and unrelated records, not only the target label.
  - Append a new session history for any separately authorized curation; never rewrite
    saved reviews or previous session records.
  - Run schema/strict, history, provenance, exact corpus reproduction, causal, term-request
    and configured label gates, then just qc.
  - Check actual semantic-input changes and regenerate map/site/redirect products
    through supported tooling when required; save an immutable successor with exact
    finding lineage.
  generator: just seed; inspect the affected just seed-canary output before authorized
    regeneration
- action_id: ACT2
  description: 'Continue existing investigation #1321 by recovering each original
    PREGO pair evidence URL and source version. Any qualification or exclusion is
    conditional on those inspected contexts; no second major/minor finding is established
    here.'
  finding_ids: []
  target_ids:
  - BTO:0005312
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained curation input or implementation; never patch generated habitat
      YAML
  acceptance_checks:
  - Distinguish laboratory exposure from original reported-from evidence without claiming
    either false occurrence or resident/endosymbiotic status from the present paper.
  generator: just seed; inspect the affected just seed-canary output before authorized
    regeneration
limitations:
- This completed observation does not promote native mapping_status, curate a record,
  close an issue, or certify the unreviewed corpus.
- Configured id-label validation passed but skips 2,061 no-adapter pairs. Canonical
  correspondence is not proof of biological identity, source membership or relation
  direction.
- The full just qc suite was not rerun for these review-only additions. Native record
  checks are recorded in this review; immutable-bundle validation and the append-only
  archive check are separate publication verification.
- No paid research was used. iModulonDB is not applicable because this target has
  no gene, regulator or expression claim; contextual genomic papers are not imported
  as mechanisms.
- Original PREGO pair-level evidence/member payload is unavailable in the retained
  inventories. An ignored-inclusive find of the configured kg-microbe checkout found
  no files with prego in their path; this is a bounded availability result, not proof
  the evidence does not exist elsewhere.
notes:
- All target fields were read. Source input hashes were captured before assessment
  and rechecked unchanged during supplemental inspection at 2026-10-15T02:37:32Z.
- The ignored-inclusive native review search found no earlier structured observation
  targeting this identifier. Historical Markdown is retained as evidence, not fabricated
  previous_occurrences.
- This review assesses the exact recorded main revision, whose captured inputs were
  each verified against git show blobs and still match the working tree. External
  responses are identified by retrieval URL, access time and SHA-256, not silently
  vendored into domain inputs.
tags:
- individual-scientific-review
- host-associated
- read-only
```
