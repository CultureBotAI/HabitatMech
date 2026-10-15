# Record review: amniotic fluid (BTO:0000068)

- Review: 20261015T024347Z-amniotic_fluid-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T02:24:39Z
- Finished UTC: 2026-10-15T02:43:47Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified pass: exact anatomical identity, source attestation, typed-related synonyms and the single Metamycoplasma hominis association are coherent. Independent primary evidence supports infection-associated occurrence. Original PREGO pair provenance remains unavailable; no normal-microbiome or characteristic-presence claim is made.

## Scope And Provenance

Full individual scientific review of this one resolved generated record, including all contributing source concepts.

Selection: Exact PATHS/identifier resolution in the next unreviewed host-associated cohort; this is not a sample extrapolated to the corpus.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 45c39c0ae63d7825c13b586b8e99e68a396af394.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0000068 | data/habitats/host_associated/amniotic_fluid.yaml | generated | amniotic fluid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0000068 | Actual command passed; started 2026-10-15T02:24:33Z, finished 2026-10-15T02:24:37Z. |
| validate-strict | passed | True | BTO:0000068 | Actual command passed; started 2026-10-15T02:25:03Z, finished 2026-10-15T02:25:14Z. |
| validate-history | passed | True | BTO:0000068 | Actual command passed; started 2026-10-15T02:25:14Z, finished 2026-10-15T02:25:32Z. |
| provenance-check | passed | True | BTO:0000068 | Actual command passed; started 2026-10-15T02:25:32Z, finished 2026-10-15T02:25:33Z. |
| verify-corpus | passed | True | BTO:0000068 | Actual command passed; started 2026-10-15T02:25:33Z, finished 2026-10-15T02:25:59Z. |
| validate-causal-all | passed | True | BTO:0000068 | Actual command passed; started 2026-10-15T02:25:59Z, finished 2026-10-15T02:26:07Z. |
| term-requests-check | passed | True | BTO:0000068 | Actual command passed; started 2026-10-15T02:26:07Z, finished 2026-10-15T02:26:37Z. |
| validate-products | passed | True | BTO:0000068 | Actual command passed; started 2026-10-15T02:26:37Z, finished 2026-10-15T02:28:49Z. |
| iModulonDB applicability | not_applicable | False | BTO:0000068 | No gene/regulator/expression claim in this record; no adapter query was appropriate. |
| Original PREGO pair provenance recovery | unavailable | False | BTO:0000068 | Current frozen TSVs and independent literature can be assessed, but the original pair evidence URLs/member records were not recovered. No pair is removed or declared false on that basis. |

## Scientific And Domain Assessments

### Native validation and generated reproducibility

schema: supported. Targets: BTO:0000068.

Target schema and nine-record strict validation passed. Current 3,208-record corpus reproduces exactly; 726 session histories, 32 graphs and 110 term requests validate. These are structural gates, not biological approval.

### Optional parameters, causal graphs and evidence placement

completeness: not_applicable. Targets: BTO:0000068.

The target contains no environmental parameter, causal graph, dataset or discussion claim. Missing optional slots alone are not findings; no mechanism or characteristic-presence claim is inferred.

### Source counts, taxon identities and ranking

quantity: supported. Targets: BTO:0000068.

The frozen PREGO row has one distinct TAXON association and one direct assertion; the displayed taxon retains score 3, rank 1, candidate_pool 1 and annotated_genomes_isolates channel. No corroborated_by or is_characteristic claim is present. Equal-score order does not establish ecological prominence.

### Source spelling and native status

provenance: supported. Targets: BTO:0000068.

PREGO lexical variants remain RELATED_SYNONYM, not exact ontology equivalences. No target ITEM decision is present in the inspected maintained decisions; EXACT/SEEDED is the deterministic self-grounding state, not a curator sign-off.

### Anatomical compartment or body fluid

identity: supported. Targets: BTO:0000068.

Exact BTO identity, canonical label and definition agree with the current authority and frozen source. The cavity is a space within the amnion; fluid is its liquid content. They are neither the enclosing membrane nor the whole fetus. Anatomical host sites are eligible habitats under the native rules.

### No invented subclass from containment

graph: supported. Targets: BTO:0000068.

No parent_habitats is emitted. The frozen subclass table and current typed BTO graph do not provide a direct broader habitat class for this term; part_of/contained_in relations are not silently converted to is-a. Separate GOLD sac and fluid paths do not feed this BTO record.

### Occurrence support versus characteristic microbiome

evidence: supported. Targets: BTO:0000068.

NCBITaxon:2098 is currently Metamycoplasma hominis; the historical Mycoplasma name in the primary study is consistent. Source-reported association is biologically supported in infection context, without promoting is_characteristic or inferring normal prenatal colonization.

### Original pair citation

provenance: unknown. Targets: BTO:0000068.

The independent paper is not proven to be the original PREGO evidence. That limits provenance confidence, but no current assertion is demonstrated false and optional citation absence alone is not a classified defect.

### Source definition versus measured parameters

scope: supported. Targets: BTO:0000068.

The developmental description and 500-1500 mL term-volume wording are copied BTO definition prose. They are not target measurements, a universal all-species range, or evidence of microbial presence. No environmental parameter is generated from them.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### ACT1

As a bounded provenance follow-up, recover the original PREGO evidence for this exact source pair and retain sample/infection context. No corrective domain edit is established by the present review.

- Match BTO:0000068 with NCBITaxon:2098 in the pinned source release before attributing the independent paper; do not infer normal flora, merge cavity with fluid, or automatically promote REVIEWED.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/amniotic_fluid.yaml; Entire YAML, including source attestations, synonyms and curation_history | supports | Complete target read; exact identifier, source provenance, grounding, status, parents and optional slots inspected. |
| E2 | docs/CURATION.md; Hosts, anatomy and taxa; decision depth; source-parent and source-label exclusions | supports | A host organism is distinct from its associated environment; anatomical parts may ground normally. Every parent is strictly broader. NOT_APPLICABLE requires evidence about the source concept, not merely an organism-valued match. |
| E3 | src/habitatmech/seed.py; PREGO self-grounding; resolve_gold; source-parent contribution; apply_curated_definitions; generated curation events | supports | Maintained producer explains source-to-record identity, all-source ITEM status, parent contributions and generated history; deterministic reproduction does not certify semantics. |
| E4 | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, assertion_count/unit; characteristic_taxa and is_characteristic | supports | Mapping predicate compares source to record identifier. TAXON and ORGANISM are different units; source-associated taxa are not automatically characteristic. |
| ESEARCH | HabitatMech local ignored-inclusive search; rg --no-ignore --hidden -l -F -e 'Amniotic fluid' -e 'Amniotic sac' -e BTO:0000025 -e BTO:0000062 -e BTO:0000068 -e BTO:0005312 -e amastigote -e 'amniotic cavity' -e 'amniotic fluid' -e amniotic_cavity -e amniotic_fluid -e amniotic_fluid__8d4e7d01 -e amniotic_fluid__ff65cb2e -e amniotic_sac -e amniotic_sac__37392cb1 -e amoeba -e amoebozoa__291e8086 -e 'amoebozoan-associated environment' -e habitatmech:GOLD.1341e74d35 -e habitatmech:GOLD.433d96f0dd -e habitatmech:GOLD.6a7bcba80d -e habitatmech:GOLD.73051a70cb -e habitatmech:GOLD.8a86b174ba -e habitatmech:GOLD.e29c7e3964 -e habitatmech:PREGO.28ae816444 -e habitatmech:PREGO.35c4c18829 -e habitatmech:PREGO.d55bca41f4 -e habitatmech:PREGO.f914cf5ea0 curation history research reports data/raw build reviews | context_only | Search returned 6,494 matching files with exit 0 and no stderr. Exact targets, source mints and source-path table rows were resolved separately; no global absence is inferred. |
| C1E | just validate data/habitats/host_associated/amniotic_fluid.yaml; 2026-10-15T02:24:33Z through 2026-10-15T02:24:37Z | supports | No issues found uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/amniotic_fluid.yaml |
| C2E | just validate-strict data/habitats/host_associated/amastigote.yaml data/habitats/host_associated/amniotic_cavity.yaml data/habitats/host_associated/amniotic_fluid.yaml data/habitats/host_associated/amniotic_fluid__8d4e7d01.yaml data/habitats/host_associated/amniotic_fluid__ff65cb2e.yaml data/habitats/host_associated/amniotic_sac.yaml data/habitats/host_associated/amniotic_sac__37392cb1.yaml data/habitats/host_associated/amoeba.yaml data/habitats/host_associated/amoebozoa__291e8086.yaml; 2026-10-15T02:25:03Z through 2026-10-15T02:25:14Z | supports | uv run python scripts/validate_strict.py data/habitats/host_associated/amastigote.yaml data/habitats/host_associated/amniotic_cavity.yaml data/habitats/host_associated/amniotic_fluid.yaml data/habitats/host_associated/amniotic_fluid__8d4e7d01.yaml data/habitats/host_associated/amniotic_fluid__ff65cb2e.yaml data/habitats/host_associated/amniotic_sac.yaml data/habitats/host_associated/amniotic_sac__37392cb1.yaml data/habitats/host_associated/amoeba.yaml data/habitats/host_associated/amoebozoa__291e8086.yaml<br>Validating 9 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      9<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| C3E | just validate-history; 2026-10-15T02:25:14Z through 2026-10-15T02:25:32Z | supports | No issues found<br>726 history record(s) valid against src/habitatmech/schema/history.yaml |
| C4E | just provenance-check; 2026-10-15T02:25:32Z through 2026-10-15T02:25:33Z | supports | provenance current: 14 committed inventories, 2 GOLD sources uv run python scripts/check_provenance.py |
| C5E | just verify-corpus; 2026-10-15T02:25:33Z through 2026-10-15T02:25:59Z | supports | expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ uv run python scripts/verify_corpus.py |
| C6E | just validate-causal-all; 2026-10-15T02:25:59Z through 2026-10-15T02:26:07Z | supports | validated 32 causal-graph curation file(s) with 32 graph(s) uv run python scripts/validate_causal_graph_curations.py |
| C7E | just term-requests-check; 2026-10-15T02:26:07Z through 2026-10-15T02:26:37Z | supports | term-request table is current (110 terms) uv run python scripts/build_term_requests.py --check |
| C8E | just validate-products; 2026-10-15T02:26:37Z through 2026-10-15T02:28:49Z | supports | id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond. uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| ELEGACY | reports/yaml_record_review/20261002T120005Z-amniotic_fluid.md; Complete historical ad hoc report | context_only | Historical review was read as a lead. Current source evidence and current maintained owners control this verdict; old validator counts and implementation availability are not reused. |
| EPREGO | data/raw/prego_habitats.tsv; Rows 529 | supports | {"biolink_category": "biolink:GrossAnatomicalStructure", "channels": "annotated_genomes_isolates", "direct_assertion_count": "1", "max_prego_score": "3", "ontology": "BTO", "prego_id": "BTO:0000068", "prego_synonyms": "acqua amnii&#124;acqua amniis&#124;amniotic fluid&#124;amniotic fluids&#124;liquor amnii&#124;liquor amniis", "taxon_count": "1"} |
| ETAXAROWS | data/raw/prego_habitat_taxa.tsv; Rows 36 | supports | {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0000068", "prego_score": "3", "rank": "1", "taxon_id": "NCBITaxon:2098", "taxon_label": "Metamycoplasma hominis"} |
| ESLICE | data/raw/ontology_terms.tsv; Rows 70 | supports | {"definition": "Fluid within the amniotic cavity produced by the amnion during the early embryonic period, and later by the lungs and kidneys; at first crystal clear, it later becomes cloudy. It protects the embryo and fetus from injury. The amount at term normally varies from 500 to 1500 mL.", "deprecated": "", "directly_referenced": "TRUE", "label": "amniotic fluid", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0000068"} |
| EONTO | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000068; label, description, obsolete flag | supports | Current OLS identity/label and definition agree with the source term; ontology meaning is assessed separately from habitat eligibility. |
| EGRAPH | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000068/graph; nodes and typed edges | supports | Typed ontology edges distinguish subclass from containment and part_of; only genuine broader habitats belong in parent_habitats. |
| ETAXON | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1408271,1408272,1408273,1408274,1408275,1408276,1408277,2098,353153,554915; Top-level Taxon entries for NCBITaxon:2098 | supports | NCBI canonical identities and ranks inspected for every displayed target taxon; historical Mycoplasma hominis nomenclature reconciled where applicable. |
| EEXTRACT | src/habitatmech/extract.py; extract_prego, lines 338-437 | supports | Retains best score/direct/channel per habitat-taxon pair, orders score then direct flag then taxon ID, and keeps top-N pairs. Pair evidence URLs and publication/member context are not retained in these TSV fields. |
| EUPSEARCH | Configured local kg-microbe checkout; find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe -ipath '*prego*' -type f | context_only | find completed with exit 0, no matching files and no stderr; this confirms only the bounded local payload availability limitation. |
| EPAPER | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:25637842%20AND%20SRC:MED&amp;format=json&amp;resultType=core; PMID25637842; DOI10.1016/j.ajog.2015.01.032; primary abstract study design | partial | Allen-Daniels et al. report two M. hominis amniotic-fluid isolates and one placental isolate from preterm pregnancies. This independently supports infection-associated occurrence in the compartment, not a normal resident microbiome or the identity of PREGO original pairs. |
| ENEIGHBOR | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000173; label, description and cross references | supports | Current cross-ontology definition supports the cavity/fluid distinction; it does not authorize a source merge. |

## Limits And Additional Notes

- This completed observation does not promote native mapping_status, curate a record, close an issue, or certify the unreviewed corpus.
- Configured id-label validation passed but skips 2,061 no-adapter pairs. Canonical correspondence is not proof of biological identity, source membership or relation direction.
- The full just qc suite was not rerun for these review-only additions. Native record checks are recorded in this review; immutable-bundle validation and the append-only archive check are separate publication verification.
- No paid research was used. iModulonDB is not applicable because this target has no gene, regulator or expression claim; contextual genomic papers are not imported as mechanisms.
- Original PREGO pair-level evidence/member payload is unavailable in the retained inventories. An ignored-inclusive find of the configured kg-microbe checkout found no files with prego in their path; this is a bounded availability result, not proof the evidence does not exist elsewhere.
- The primary study was inspected through its full abstract/metadata; the Europe PMC fullTextXML request for PMC4457590 returned HTTP500. It is not represented as a successful full-text read.
- All target fields were read. Source input hashes were captured before assessment and rechecked unchanged during supplemental inspection at 2026-10-15T02:36:59Z.
- The ignored-inclusive native review search found no earlier structured observation targeting this identifier. Historical Markdown is retained as evidence, not fabricated previous_occurrences.
- This review assesses the exact recorded main revision, whose captured inputs were each verified against git show blobs and still match the working tree. External responses are identified by retrieval URL, access time and SHA-256, not silently vendored into domain inputs.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T024347Z-amniotic_fluid-record
kind: record
repository: CultureBotAI/HabitatMech
title: 'Record review: amniotic fluid (BTO:0000068)'
started_at: '2026-10-15T02:24:39Z'
finished_at: '2026-10-15T02:43:47Z'
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
verdict: pass_with_limitations
scientific_review: true
summary: 'Qualified pass: exact anatomical identity, source attestation, typed-related
  synonyms and the single Metamycoplasma hominis association are coherent. Independent
  primary evidence supports infection-associated occurrence. Original PREGO pair provenance
  remains unavailable; no normal-microbiome or characteristic-presence claim is made.'
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
    role: target
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
    role: context
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
- target_id: BTO:0000068
  path: data/habitats/host_associated/amniotic_fluid.yaml
  label: amniotic fluid
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
  - BTO:0000068
  exclusions:
  - target: Other HabitatMech records and SSSOM/KGX products
    reason: Referenced parents and neighboring concepts are inspected only as dependencies,
      not certified as complete individual reviews or export conformance.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/amniotic_fluid.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000068
  evidence_ids:
  - C1E
  summary: Actual command passed; started 2026-10-15T02:24:33Z, finished 2026-10-15T02:24:37Z.
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
  - BTO:0000068
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
  - BTO:0000068
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
  - BTO:0000068
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
  - BTO:0000068
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
  - BTO:0000068
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
  - BTO:0000068
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
  - BTO:0000068
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
  - BTO:0000068
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
  - BTO:0000068
  evidence_ids:
  - EEXTRACT
  - ETAXAROWS
  - EUPSEARCH
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/amniotic_fluid.yaml
  locator: Entire YAML, including source attestations, synonyms and curation_history
  accessed_at: '2026-10-15T02:43:47Z'
  support: supports
  summary: Complete target read; exact identifier, source provenance, grounding, status,
    parents and optional slots inspected.
  snapshot_sha256: 0d11095a2414faa717c2aa11ee3cf33ad2afd1239bcdefcad8ebd0de4b0861f3
- evidence_id: E2
  kind: authority
  reference: docs/CURATION.md
  locator: Hosts, anatomy and taxa; decision depth; source-parent and source-label
    exclusions
  accessed_at: '2026-10-15T02:43:47Z'
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
  accessed_at: '2026-10-15T02:43:47Z'
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
  accessed_at: '2026-10-15T02:43:47Z'
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
  reference: just validate data/habitats/host_associated/amniotic_fluid.yaml
  locator: 2026-10-15T02:24:33Z through 2026-10-15T02:24:37Z
  accessed_at: '2026-10-15T02:24:37Z'
  support: supports
  summary: No issues found uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml
    --target-class HabitatRecord data/habitats/host_associated/amniotic_fluid.yaml
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
  reference: reports/yaml_record_review/20261002T120005Z-amniotic_fluid.md
  locator: Complete historical ad hoc report
  accessed_at: '2026-10-15T02:43:47Z'
  support: context_only
  summary: Historical review was read as a lead. Current source evidence and current
    maintained owners control this verdict; old validator counts and implementation
    availability are not reused.
  snapshot_sha256: d774ec3f26ddded413799970accdd21bb29c3484281a175e7cef261180e3b92f
- evidence_id: EPREGO
  kind: database
  reference: data/raw/prego_habitats.tsv
  locator: Rows 529
  accessed_at: '2026-10-15T02:43:47Z'
  support: supports
  summary: '{"biolink_category": "biolink:GrossAnatomicalStructure", "channels": "annotated_genomes_isolates",
    "direct_assertion_count": "1", "max_prego_score": "3", "ontology": "BTO", "prego_id":
    "BTO:0000068", "prego_synonyms": "acqua amnii|acqua amniis|amniotic fluid|amniotic
    fluids|liquor amnii|liquor amniis", "taxon_count": "1"}'
  snapshot_sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
- evidence_id: ETAXAROWS
  kind: database
  reference: data/raw/prego_habitat_taxa.tsv
  locator: Rows 36
  accessed_at: '2026-10-15T02:43:47Z'
  support: supports
  summary: '{"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "BTO:0000068", "prego_score": "3", "rank": "1", "taxon_id":
    "NCBITaxon:2098", "taxon_label": "Metamycoplasma hominis"}'
  snapshot_sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
- evidence_id: ESLICE
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Rows 70
  accessed_at: '2026-10-15T02:43:47Z'
  support: supports
  summary: '{"definition": "Fluid within the amniotic cavity produced by the amnion
    during the early embryonic period, and later by the lungs and kidneys; at first
    crystal clear, it later becomes cloudy. It protects the embryo and fetus from
    injury. The amount at term normally varies from 500 to 1500 mL.", "deprecated":
    "", "directly_referenced": "TRUE", "label": "amniotic fluid", "label_only": "FALSE",
    "ontology": "BTO", "synonyms": "", "term_id": "BTO:0000068"}'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTO
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000068
  locator: label, description, obsolete flag
  accessed_at: '2026-10-15T02:27:34Z'
  support: supports
  summary: Current OLS identity/label and definition agree with the source term; ontology
    meaning is assessed separately from habitat eligibility.
  snapshot_sha256: ace2d77df847bd27d3c22cec3eaea9a969eeb03f6b61861815895466e1dcf1c8
- evidence_id: EGRAPH
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000068/graph
  locator: nodes and typed edges
  accessed_at: '2026-10-15T02:35:05Z'
  support: supports
  summary: Typed ontology edges distinguish subclass from containment and part_of;
    only genuine broader habitats belong in parent_habitats.
  snapshot_sha256: adebcc96ed6fc4875712a5bb7a8e84ade83ce294350b46aa2a64a1264c79c54b
- evidence_id: ETAXON
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1408271,1408272,1408273,1408274,1408275,1408276,1408277,2098,353153,554915
  locator: Top-level Taxon entries for NCBITaxon:2098
  accessed_at: '2026-10-15T02:27:41Z'
  support: supports
  summary: NCBI canonical identities and ranks inspected for every displayed target
    taxon; historical Mycoplasma hominis nomenclature reconciled where applicable.
  snapshot_sha256: 9c177420cf4d21729c2b5f604220caff180ce97ca3f438e7638e76fe1b57d314
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: extract_prego, lines 338-437
  accessed_at: '2026-10-15T02:43:47Z'
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
- evidence_id: EPAPER
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:25637842%20AND%20SRC:MED&format=json&resultType=core
  locator: PMID25637842; DOI10.1016/j.ajog.2015.01.032; primary abstract study design
  accessed_at: '2026-10-15T02:27:48Z'
  support: partial
  summary: Allen-Daniels et al. report two M. hominis amniotic-fluid isolates and
    one placental isolate from preterm pregnancies. This independently supports infection-associated
    occurrence in the compartment, not a normal resident microbiome or the identity
    of PREGO original pairs.
  snapshot_sha256: edab3ba7bec8774bd7947bf40781cd331c1eac366a97512a28ce953ef8b8a1a4
- evidence_id: ENEIGHBOR
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000173
  locator: label, description and cross references
  accessed_at: '2026-10-15T02:27:38Z'
  support: supports
  summary: Current cross-ontology definition supports the cavity/fluid distinction;
    it does not authorize a source merge.
  snapshot_sha256: 3b7e39b615eb36e9c690dd07a2b45180ce0c03a1dcab79a7f01607959d46b5b2
assessments:
- assessment_id: A1
  area: schema
  topic: Native validation and generated reproducibility
  outcome: supported
  summary: Target schema and nine-record strict validation passed. Current 3,208-record
    corpus reproduces exactly; 726 session histories, 32 graphs and 110 term requests
    validate. These are structural gates, not biological approval.
  target_ids:
  - BTO:0000068
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
  - BTO:0000068
  evidence_ids:
  - E1
  - ESEARCH
- assessment_id: A3
  area: quantity
  topic: Source counts, taxon identities and ranking
  outcome: supported
  summary: The frozen PREGO row has one distinct TAXON association and one direct
    assertion; the displayed taxon retains score 3, rank 1, candidate_pool 1 and annotated_genomes_isolates
    channel. No corroborated_by or is_characteristic claim is present. Equal-score
    order does not establish ecological prominence.
  target_ids:
  - BTO:0000068
  evidence_ids:
  - EPREGO
  - ETAXAROWS
  - ETAXON
  - E4
  - EEXTRACT
  metrics:
  - name: Retained source taxa
    value: 1
    unit: distinct PREGO TAXON identifiers
    definition: Displayed taxon associations divided by the frozen PREGO candidate
      pool; not prevalence or abundance.
    denominator: 1
  dimensions:
  - name: source-curation-key
    value: habitatmech:PREGO.d55bca41f4
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
  - BTO:0000068
  evidence_ids:
  - E1
  - EPREGO
  - E3
  - ESEARCH
- assessment_id: A5
  area: identity
  topic: Anatomical compartment or body fluid
  outcome: supported
  summary: Exact BTO identity, canonical label and definition agree with the current
    authority and frozen source. The cavity is a space within the amnion; fluid is
    its liquid content. They are neither the enclosing membrane nor the whole fetus.
    Anatomical host sites are eligible habitats under the native rules.
  target_ids:
  - BTO:0000068
  evidence_ids:
  - EONTO
  - ENEIGHBOR
  - EPREGO
  - E2
- assessment_id: A6
  area: graph
  topic: No invented subclass from containment
  outcome: supported
  summary: No parent_habitats is emitted. The frozen subclass table and current typed
    BTO graph do not provide a direct broader habitat class for this term; part_of/contained_in
    relations are not silently converted to is-a. Separate GOLD sac and fluid paths
    do not feed this BTO record.
  target_ids:
  - BTO:0000068
  evidence_ids:
  - E1
  - EGRAPH
  - E3
- assessment_id: A7
  area: evidence
  topic: Occurrence support versus characteristic microbiome
  outcome: supported
  summary: NCBITaxon:2098 is currently Metamycoplasma hominis; the historical Mycoplasma
    name in the primary study is consistent. Source-reported association is biologically
    supported in infection context, without promoting is_characteristic or inferring
    normal prenatal colonization.
  target_ids:
  - BTO:0000068
  evidence_ids:
  - ETAXON
  - EPAPER
  - ETAXAROWS
  - E4
- assessment_id: A8
  area: provenance
  topic: Original pair citation
  outcome: unknown
  summary: The independent paper is not proven to be the original PREGO evidence.
    That limits provenance confidence, but no current assertion is demonstrated false
    and optional citation absence alone is not a classified defect.
  target_ids:
  - BTO:0000068
  evidence_ids:
  - EEXTRACT
  - EPAPER
  - ELEGACY
- assessment_id: A9
  area: scope
  topic: Source definition versus measured parameters
  outcome: supported
  summary: The developmental description and 500-1500 mL term-volume wording are copied
    BTO definition prose. They are not target measurements, a universal all-species
    range, or evidence of microbial presence. No environmental parameter is generated
    from them.
  target_ids:
  - BTO:0000068
  evidence_ids:
  - EONTO
  - ESLICE
  - E1
findings: []
actions:
- action_id: ACT1
  description: As a bounded provenance follow-up, recover the original PREGO evidence
    for this exact source pair and retain sample/infection context. No corrective
    domain edit is established by the present review.
  finding_ids: []
  target_ids:
  - BTO:0000068
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained curation input or implementation; never patch generated habitat
      YAML
  acceptance_checks:
  - Match BTO:0000068 with NCBITaxon:2098 in the pinned source release before attributing
    the independent paper; do not infer normal flora, merge cavity with fluid, or
    automatically promote REVIEWED.
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
- The primary study was inspected through its full abstract/metadata; the Europe PMC
  fullTextXML request for PMC4457590 returned HTTP500. It is not represented as a
  successful full-text read.
notes:
- All target fields were read. Source input hashes were captured before assessment
  and rechecked unchanged during supplemental inspection at 2026-10-15T02:36:59Z.
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
