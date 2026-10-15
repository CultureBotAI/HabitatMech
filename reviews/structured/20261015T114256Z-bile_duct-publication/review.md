# Publication follow-up: bile duct (BTO:0000122)

- Review: 20261015T114256Z-bile_duct-publication
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T11:41:53Z
- Finished UTC: 2026-10-15T11:42:56Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Issue URL punctuation is corrected under #2179. The full current target retains every scientific field and every prior scientific finding disposition; only the new curation-note URL boundaries differ. No new biological conclusion or resolved scientific finding is claimed.

## Scope And Provenance

Full current target re-read after an issue-URL punctuation-only correction; every scientific disposition reassessed.

Selection: One of fifteen repaired records or the unchanged biofilm target receiving a report-locator correction in this twenty-record PR cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 6e7f4baa9e2c8a5acc71e1af0b070cd82c84b798.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0000122 | data/habitats/host_associated/bile_duct.yaml | generated | bile duct |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate-strict data/habitats/host_associated/benign_tumor_tissue.yaml data/habitats/host_associated/bhk.yaml data/habitats/host_associated/bhk_21_cell.yaml data/habitats/host_associated/bile.yaml data/habitats/host_associated/bile__22fc0a7b.yaml data/habitats/host_associated/bile__57dd7796.yaml data/habitats/host_associated/bile__612af0df.yaml data/habitats/host_associated/bile__deca6de5.yaml data/habitats/host_associated/bile_duct.yaml data/habitats/host_associated/biliary_tract.yaml data/habitats/host_associated/biliary_tract__076692f7.yaml data/habitats/host_associated/biliary_tract__7bf9e820.yaml data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml data/habitats/host_associated/biliary_tract__d5e0bd1d.yaml data/habitats/host_associated/biliary_tract__e6019127.yaml data/habitats/host_associated/biocrust.yaml data/habitats/host_associated/biofilm.yaml data/habitats/host_associated/biofilm__465616a5.yaml data/habitats/host_associated/birds.yaml data/habitats/host_associated/bivalves.yaml | passed | True | BTO:0000122 | Actual execution 2026-10-15T11:40:21Z through 2026-10-15T11:40:29Z. uv run python scripts/validate_strict.py data/habitats/host_associated/benign_tumor_tissue.yaml data/habitats/host_associated/bhk.yaml data/habitats/host_associated/bhk_21_cell.yaml data/habitats/host_associated/bile.yaml data/habitats/host_associated/bile__22fc0a7b.yaml data/habitats/host_associated/bile__57dd7796.yaml data/habitats/host_associated/bile__612af0df.yaml data/habitats/host_associated/bile__deca6de5.yaml data/habitats/host_associated/bile_duct.yaml data/habitats/host_associated/biliary_tract.yaml data/habitats/host_associated/biliary_tract__076692f7.yaml data/habitats/host_associated/biliary_tract__7bf9e820.yaml data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml data/habitats/host_associated/biliary_tract__d5e0bd1d.yaml data/habitats/host_associated/biliary_tract__e6019127.yaml data/habitats/host_associated/biocrust.yaml data/habitats/host_associated/biofilm.yaml data/habitats/host_associated/biofilm__465616a5.yaml data/habitats/host_associated/birds.yaml data/habitats/host_associated/bivalves.yaml<br>Validating 20 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      20<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| just validate-history | passed | True | BTO:0000122 | Actual execution 2026-10-15T11:40:29Z through 2026-10-15T11:40:39Z. No issues found<br>808 history record(s) valid against src/habitatmech/schema/history.yaml |
| just verify-corpus | passed | True | BTO:0000122 | Actual execution 2026-10-15T11:40:39Z through 2026-10-15T11:40:56Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python -m pytest -q tests/test_biliary_review_links.py tests/test_biliary_bivalve_review_repairs.py | passed | True | BTO:0000122 | Actual execution 2026-10-15T11:40:56Z through 2026-10-15T11:41:03Z. ..                                                                       [100%]<br>2 passed in 6.38s |
| just render-check | passed | True | BTO:0000122 | Actual execution 2026-10-15T11:41:03Z through 2026-10-15T11:41:33Z. rendered 3208 habitat pages, 258 redirect stubs, 8 categories, 122 term requests -&gt; /var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/tmp7e571f_3/site<br>pages/ is in step with the corpus<br> uv run python scripts/render_pages.py --check |
| git diff --check 405ef4c51cf7aa4d0d2203aaf392ed5d773a7e87 | passed | True | BTO:0000122 | Actual execution 2026-10-15T11:41:33Z through 2026-10-15T11:41:35Z.  |

## Scientific And Domain Assessments

### Exact correction and whole-record preservation

consistency: supported. Targets: BTO:0000122.

The whole-corpus counterfactual and complete current YAML demonstrate bounded hierarchy/synonym changes, preserved source metadata and status, and repeatable generation.

### Retained scientific support

evidence: supported. Targets: BTO:0000122.

The target was rechecked against retained typed ontology and bounded primary evidence. No new characteristic-presence, prevalence or mechanism claim is added.

### Publication correction preserves scientific content

consistency: supported. Targets: BTO:0000122.

Complete target comparison permits only URL-boundary spacing in the new deterministic curation history. All scientific claims and unresolved limitations remain unchanged.

## Findings

### F1: Source context is asserted as a strictly broader habitat

major / resolved / confirmed; issue key: bile-duct-source-parent.

A duct is part of a biliary tract, not a subclass of the whole mammal tract. Exclude only the exact GOLD contribution habitatmech:GOLD.de5efc0eb8 using source-path and expected-parent guards. Preserve independent ontology genera, counts, identities and native status. The linked issue is related context; additional host witnesses expand its original examples.

Disposition: Exact source-path and expected-parent guards suppress only the reviewed GOLD context edge. Independent ontology parents, source attestations/counts/units, identity and status remain.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000122/graph; Current identity, definition and typed relations | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0000122", "target": "http://purl.obolibrary.org/obo/BTO_0000759", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000122; Current identity, definition and typed relations | supports | BTO:0000122 bile duct; inspected definition: ["Any of the ducts that convey bile in and from the liver."] |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001173/graph; Current identity, definition and typed relations | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001173", "target": "http://purl.obolibrary.org/obo/UBERON_0004119", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173", "target": "http://purl.obolibrary.org/obo/UBERON_0013765", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173", "target": "http://purl.obolibrary.org/obo/UBERON_0001246", "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173", "target": "http://purl.obolibrary.org/obo/UBERON_0001282", "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173", "target": "http://purl.obolibrary.org/obo/UBERON_0002294", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173", "target": "http://purl.obolibrary.org/obo/UBERON_0002394", "uri": "http://purl.obolibrary.org/obo/RO_0002473", "label": "composed primarily of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173", "target": "http://purl.obolibrary.org/obo/UBERON_0002423", "uri": "http://purl.obolibrary.org/obo/RO_0002433", "label": "contributes to morphology of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173", "target": "http://purl.obolibrary.org/obo/UBERON_0003703", "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173", "target": "http://purl.obolibrary.org/obo/UBERON_0004912", "uri": "http://purl.obolibrary.org/obo/RO_0002202", "label": "develops from"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001173; Current identity, definition and typed relations | supports | UBERON:0001173 biliary tree; inspected definition: ["The path in many species is as follows: Bile canaliculi -&gt; Canals of Hering (intralobar bile duct) -&gt; interlobular bile ducts -&gt; intrahepatic bile ducts -&gt; left and right hepatic ducts merge to form -&gt; common hepatic duct *exits liver* and joins -&gt; cystic duct (from gall bladder) forming -&gt; common bile duct -&gt; joins with pancreatic duct -&gt; forming ampulla of Vater -&gt; enters duodenum [WP]", "A complex network of conduits that begins with the canals of Hering (intralobar bile duct) and progressively merges into a system of interlobular, septal, and major ducts which then coalesce to form the extrahepatic bile ducts, which finally deliver bile to the intestine, and in some species to the gallbladder."] Typed synonyms: [{"name": "biliary tract", "scope": "hasRelatedSynonym", "type": null, "xrefs": [{"database": "MA", "id": "0001273", "description": null, "url": "http://www.informatics.jax.org/searches/AMA.cgi?id=MA:0001273"}]}] |
| EX5 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A27100044%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=12; Primary abstract and identifier metadata | supports | PMID:27100044; DOI:10.3109/23744235.2016.1157896. Three genome-identified S. pseudopneumoniae isolates came from blood cultures with an apparent liver or bile-duct origin of infection. This is contextual hepatobiliary association, not direct bile-duct specimen evidence. |
| EX6 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1000561,1110546,1123317,1177117,1191475,1233262,1236904,1238993,1257037,1257038,1257039,1257040,1257041,1257042,1280,1283,1292046,1321369,1367494,137591,1392869,1408271,1408272,1408273,1408274,1810840,257758,282199,440512,470&amp;retmode=xml; Exact TaxId, aliases, ScientificName, rank and lineage | supports | [{"id": "NCBITaxon:257758", "label": "Streptococcus pseudopneumoniae", "current_id": "257758", "current_name": "Streptococcus pseudopneumoniae", "current_rank": "species", "lineage": "cellular organisms; Bacteria; Bacillati; Bacillota; Bacilli; Lactobacillales; Streptococcaceae; Streptococcus"}] |
| EAFTER | data/habitats/host_associated/bile_duct.yaml; Entire current YAML | supports | Complete current target: {"identifier": "BTO:0000122", "label": "bile duct", "definition": "Any of the ducts that convey bile in and from the liver.", "definition_source": "BTO", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "EXACT", "mapping_status": "REVIEWED", "synonyms": [{"synonym_text": "Bile ducts", "synonym_type": "EXACT_SYNONYM", "source": "GOLD"}, {"synonym_text": "bile ducts", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "biliary duct", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "biliary ducts", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "gall duct", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "gall ducts", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6719", "source_label": "Bile ducts", "source_path": "Host-associated &gt; Mammals &gt; Digestive system &gt; Biliary tract &gt; Bile ducts", "mapping_predicate": "skos:exactMatch"}, {"source": "PREGO", "source_id": "BTO:0000122", "source_label": "bile duct", "assertion_count": 1, "assertion_unit": "TAXON", "score": 3.0, "evidence_channels": "annotated_genomes_isolates"}], "characteristic_taxa": [{"taxon_id": "NCBITaxon:257758", "source": "PREGO", "taxon_label": "Streptococcus pseudopneumoniae", "score": 3.0, "rank": 1, "candidate_pool": 1}], "curation_history": [{"timestamp": "2026-08-12T00:00:00Z", "curator": "claude-opus-5", "action": "GROUND", "changes": "Grounded to BTO:0000122 'bile duct' (EXACT). Leaf label equals the BTO label exactly and no other source concept claims it. Path: Host-associated &gt; Mammals &gt; Digestive system &gt; Biliary tract &gt; Bile ducts (source concept habitatmech:GOLD.ce334980d0)"}, {"timestamp": "2026-08-13T00:00:00Z", "curator": "claude-opus-5", "action": "REVIEW", "changes": "Reviewed and endorsed the seeder's own resolution. Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date. (source concept habitatmech:PREGO.27e62ea512)"}, {"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD, PREGO. Grounding: EXACT."}, {"timestamp": "2026-10-15T00:00:00Z", "curator": "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.de5efc0eb8 for habitatmech:GOLD.ce334980d0 (Host-associated &gt; Mammals &gt; Digestive system &gt; Biliary tract &gt; Bile ducts). Review https://github.com/CultureBotAI/HabitatMech/issues/2177 : A duct is part of, not a kind of, the whole mammal biliary tract. Suppress only the exact GOLD context contribution. Preserve independent parents, identity, source path/node/count/unit, taxa, native status and prior history. No source-scope or mapping-endpoint certification is implied."}]} |
| EPREV | reviews/structured/20261015T112625Z-bile_duct-remediation/review.yaml; Immediate immutable predecessor | supports | Scientific findings and dispositions remain unchanged. |
| ETEST | tests/test_biliary_bivalve_review_repairs.py; Whole-corpus counterfactual | supports | Restoring only prior rules changes exactly fifteen records. Identity, definitions, source observations/counts/units, taxa, native statuses, valid parents and prior history are preserved; regeneration is repeatable. |
| EI0 | curation/gold_parent_exclusions.tsv; Current maintained rows | supports | [[7, {"identifier": "habitatmech:GOLD.ce334980d0", "source_path": "Host-associated &gt; Mammals &gt; Digestive system &gt; Biliary tract &gt; Bile ducts", "parent_id": "habitatmech:GOLD.de5efc0eb8", "curator": "codex-gpt-5", "date": "2026-10-15", "notes": "Review https://github.com/CultureBotAI/HabitatMech/issues/2177 : A duct is part of, not a kind of, the whole mammal biliary tract. Suppress only the exact GOLD context contribution. Preserve independent parents, identity, source path/node/count/unit, taxa, native status and prior history. No source-scope or mapping-endpoint certification is implied."}]] |
| ELINK | tests/test_biliary_review_links.py; Issue URL boundary regression | supports | The regression failed before correction and passed afterward for all 18 new notes. Parsed generated HTML verifies 18 exact hrefs on 15 pages. Whole-record comparison permits only the expected whitespace before colon; all semantic JSONL bytes are identical. |

## Limits And Additional Notes

- Same-agent review is not independent approval. Review does not promote native scientific status.
- Original source-member and source-precision limitations from the predecessor remain; preserved assertions are not independently confirmed specimens.
- Final full QC, archive integrity and real semantic-map/site publication are subsequent gates, not claimed completed in this observation.
- Configured label correspondence retains documented no-adapter skips; this is not global identifier or semantic certification.
- Shared mapping endpoints #1398 and typed ontology extraction #1249 remain open. iModulonDB is not applicable; no gene/expression assertion is made.
- Publication repair https://github.com/CultureBotAI/HabitatMech/issues/2179; broader renderer issue #2046 remains open. Native seeding/site regeneration and whole-record comparison preserve all scientific fields and unchanged semantic-map input bytes. All earlier review bundles and session history remain immutable.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T114256Z-bile_duct-publication
repository: CultureBotAI/HabitatMech
kind: record
title: 'Publication follow-up: bile duct (BTO:0000122)'
started_at: '2026-10-15T11:41:53Z'
finished_at: '2026-10-15T11:42:56Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent inspected target and evidence; not independent human
    or second-agent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Issue URL punctuation is corrected under #2179. The full current target
  retains every scientific field and every prior scientific finding disposition; only
  the new curation-note URL boundaries differ. No new biological conclusion or resolved
  scientific finding is claimed.'
source:
  git_revision: 6e7f4baa9e2c8a5acc71e1af0b070cd82c84b798
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
    sha256: 6d5cbfd0f5ad911fbb074ee8ec253625d1fa13d94117759b1f25a1cd2e6576bc
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: a92f9003cc5f57c397ab5118474318f216077a8e9f90564d21dfa8089477a2eb
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: a56f07a45fb743fb7b0e61f83ef70fa5ed61a3c892cfaf36e3428967c548dc5e
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: dfde49f64273cb94b4162170a5542c94880fa36015ccaac6edfa248820492a23
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
  - path: data/habitats/host_associated/bile_duct.yaml
    sha256: f29c75f42d6d557df79a5116fb2e2e126f7cc8244e52e889471484e8463360ca
    role: target
  - path: data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml
    sha256: 100e3d311062851be06598d3c6d25df5cbfef28ef2bfd9033bad61d05159dc88
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
  - path: history/mappings/bile_duct/2026-10-15T112023Z-codex-gpt-5-91514b.yaml
    sha256: f5a6101966231eaee73f858cdf84c5def061353e4ba3d5f1c6eabc54279afbdf
    role: context
  - path: history/mappings/review-link-boundaries/2026-10-15T113917Z-codex-gpt-5-a9297b.yaml
    sha256: 3447b314e8c5b51bf844ad09a69a176a7cc11c363af8ba06ab5e8121e3b94791
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20261002T181521Z-bile_duct.md
    sha256: baacf148a2f4bd4b0d0f7d22b30e57c0f5636d18f273d026cc77cc70f1474409
    role: context
  - path: reviews/structured/20261015T110628Z-bile_duct-record/review.yaml
    sha256: 3bed04b26ae5ac098d7d63d94400ab5c3d7f08835705c1afd3cbe3be6e627669
    role: context
  - path: reviews/structured/20261015T112625Z-bile_duct-remediation/review.yaml
    sha256: 51baf5c0cec97364c5768aee78e78e1f925aae5db1a5245c274cb0d3ae5f565b
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
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
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
  - path: tests/test_biliary_bivalve_review_repairs.py
    sha256: 1412766b81259472012db4a0b75b171a12d854357f7c6d2d79289dcbcb1882d0
    role: context
  - path: tests/test_biliary_review_links.py
    sha256: c93aef11ddc15313ad428e63e6123483e9a78ba12149d734a2440dc25de439f8
    role: context
targets:
- target_id: BTO:0000122
  path: data/habitats/host_associated/bile_duct.yaml
  label: bile duct
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
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
scope:
  description: Full current target re-read after an issue-URL punctuation-only correction;
    every scientific disposition reassessed.
  selection: One of fifteen repaired records or the unchanged biofilm target receiving
    a report-locator correction in this twenty-record PR cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - BTO:0000122
  exclusions:
  - target: Global mapping, source contracts and other records
    reason: Only exact hierarchy/synonym witnesses are repaired; SSSOM/KGX readiness
      is not certified.
checks:
- check_id: C1
  name: just validate-strict data/habitats/host_associated/benign_tumor_tissue.yaml
    data/habitats/host_associated/bhk.yaml data/habitats/host_associated/bhk_21_cell.yaml
    data/habitats/host_associated/bile.yaml data/habitats/host_associated/bile__22fc0a7b.yaml
    data/habitats/host_associated/bile__57dd7796.yaml data/habitats/host_associated/bile__612af0df.yaml
    data/habitats/host_associated/bile__deca6de5.yaml data/habitats/host_associated/bile_duct.yaml
    data/habitats/host_associated/biliary_tract.yaml data/habitats/host_associated/biliary_tract__076692f7.yaml
    data/habitats/host_associated/biliary_tract__7bf9e820.yaml data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml
    data/habitats/host_associated/biliary_tract__d5e0bd1d.yaml data/habitats/host_associated/biliary_tract__e6019127.yaml
    data/habitats/host_associated/biocrust.yaml data/habitats/host_associated/biofilm.yaml
    data/habitats/host_associated/biofilm__465616a5.yaml data/habitats/host_associated/birds.yaml
    data/habitats/host_associated/bivalves.yaml
  status: passed
  required: true
  command: just validate-strict data/habitats/host_associated/benign_tumor_tissue.yaml
    data/habitats/host_associated/bhk.yaml data/habitats/host_associated/bhk_21_cell.yaml
    data/habitats/host_associated/bile.yaml data/habitats/host_associated/bile__22fc0a7b.yaml
    data/habitats/host_associated/bile__57dd7796.yaml data/habitats/host_associated/bile__612af0df.yaml
    data/habitats/host_associated/bile__deca6de5.yaml data/habitats/host_associated/bile_duct.yaml
    data/habitats/host_associated/biliary_tract.yaml data/habitats/host_associated/biliary_tract__076692f7.yaml
    data/habitats/host_associated/biliary_tract__7bf9e820.yaml data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml
    data/habitats/host_associated/biliary_tract__d5e0bd1d.yaml data/habitats/host_associated/biliary_tract__e6019127.yaml
    data/habitats/host_associated/biocrust.yaml data/habitats/host_associated/biofilm.yaml
    data/habitats/host_associated/biofilm__465616a5.yaml data/habitats/host_associated/birds.yaml
    data/habitats/host_associated/bivalves.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000122
  summary: "Actual execution 2026-10-15T11:40:21Z through 2026-10-15T11:40:29Z. uv\
    \ run python scripts/validate_strict.py data/habitats/host_associated/benign_tumor_tissue.yaml\
    \ data/habitats/host_associated/bhk.yaml data/habitats/host_associated/bhk_21_cell.yaml\
    \ data/habitats/host_associated/bile.yaml data/habitats/host_associated/bile__22fc0a7b.yaml\
    \ data/habitats/host_associated/bile__57dd7796.yaml data/habitats/host_associated/bile__612af0df.yaml\
    \ data/habitats/host_associated/bile__deca6de5.yaml data/habitats/host_associated/bile_duct.yaml\
    \ data/habitats/host_associated/biliary_tract.yaml data/habitats/host_associated/biliary_tract__076692f7.yaml\
    \ data/habitats/host_associated/biliary_tract__7bf9e820.yaml data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml\
    \ data/habitats/host_associated/biliary_tract__d5e0bd1d.yaml data/habitats/host_associated/biliary_tract__e6019127.yaml\
    \ data/habitats/host_associated/biocrust.yaml data/habitats/host_associated/biofilm.yaml\
    \ data/habitats/host_associated/biofilm__465616a5.yaml data/habitats/host_associated/birds.yaml\
    \ data/habitats/host_associated/bivalves.yaml\nValidating 20 files with 15 workers;\
    \ schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      20\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Strict check covers twenty targets; remaining documented native gates
    cover the corpus; pytest is the focused preservation/publication regression.
- check_id: C2
  name: just validate-history
  status: passed
  required: true
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000122
  summary: 'Actual execution 2026-10-15T11:40:29Z through 2026-10-15T11:40:39Z. No
    issues found

    808 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Strict check covers twenty targets; remaining documented native gates
    cover the corpus; pytest is the focused preservation/publication regression.
- check_id: C3
  name: just verify-corpus
  status: passed
  required: true
  command: just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000122
  summary: "Actual execution 2026-10-15T11:40:39Z through 2026-10-15T11:40:56Z. expected\
    \ 3208 records, found 3208 on disk\n  missing:   0\n  extra:     0\n  differing:\
    \ 0\n\ncorpus reproduces exactly from data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Strict check covers twenty targets; remaining documented native gates
    cover the corpus; pytest is the focused preservation/publication regression.
- check_id: C4
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_biliary_review_links.py tests/test_biliary_bivalve_review_repairs.py
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_biliary_review_links.py tests/test_biliary_bivalve_review_repairs.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000122
  summary: 'Actual execution 2026-10-15T11:40:56Z through 2026-10-15T11:41:03Z. ..                                                                       [100%]

    2 passed in 6.38s'
  scope_note: Strict check covers twenty targets; remaining documented native gates
    cover the corpus; pytest is the focused preservation/publication regression.
- check_id: C5
  name: just render-check
  status: passed
  required: true
  command: just render-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000122
  summary: "Actual execution 2026-10-15T11:41:03Z through 2026-10-15T11:41:33Z. rendered\
    \ 3208 habitat pages, 258 redirect stubs, 8 categories, 122 term requests -> /var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/tmp7e571f_3/site\n\
    pages/ is in step with the corpus\n uv run python scripts/render_pages.py --check"
  scope_note: Strict check covers twenty targets; remaining documented native gates
    cover the corpus; pytest is the focused preservation/publication regression.
- check_id: C6
  name: git diff --check 405ef4c51cf7aa4d0d2203aaf392ed5d773a7e87
  status: passed
  required: true
  command: git diff --check 405ef4c51cf7aa4d0d2203aaf392ed5d773a7e87
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000122
  summary: 'Actual execution 2026-10-15T11:41:33Z through 2026-10-15T11:41:35Z. '
  scope_note: Strict check covers twenty targets; remaining documented native gates
    cover the corpus; pytest is the focused preservation/publication regression.
evidence:
- evidence_id: EX1
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000122/graph
  locator: Current identity, definition and typed relations
  accessed_at: '2026-10-15T10:52:19Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0000122",
    "target": "http://purl.obolibrary.org/obo/BTO_0000759", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 972957e3ce0e6f9edad25716e7ef687885ea0d199a18ba0037455e8099e894ec
- evidence_id: EX2
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000122
  locator: Current identity, definition and typed relations
  accessed_at: '2026-10-15T10:52:19Z'
  support: supports
  summary: 'BTO:0000122 bile duct; inspected definition: ["Any of the ducts that convey
    bile in and from the liver."]'
  snapshot_sha256: 82a00cae8cbabc3e99b2a4b0887fa72201acb9d1ca94458de1d6bbd944d59eef
- evidence_id: EX3
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001173/graph
  locator: Current identity, definition and typed relations
  accessed_at: '2026-10-15T10:52:54Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001173",
    "target": "http://purl.obolibrary.org/obo/UBERON_0004119", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173",
    "target": "http://purl.obolibrary.org/obo/UBERON_0013765", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001246", "uri": "http://purl.obolibrary.org/obo/BFO_0000051",
    "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001282", "uri": "http://purl.obolibrary.org/obo/BFO_0000051",
    "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173",
    "target": "http://purl.obolibrary.org/obo/UBERON_0002294", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173",
    "target": "http://purl.obolibrary.org/obo/UBERON_0002394", "uri": "http://purl.obolibrary.org/obo/RO_0002473",
    "label": "composed primarily of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173",
    "target": "http://purl.obolibrary.org/obo/UBERON_0002423", "uri": "http://purl.obolibrary.org/obo/RO_0002433",
    "label": "contributes to morphology of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173",
    "target": "http://purl.obolibrary.org/obo/UBERON_0003703", "uri": "http://purl.obolibrary.org/obo/BFO_0000051",
    "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173",
    "target": "http://purl.obolibrary.org/obo/UBERON_0004912", "uri": "http://purl.obolibrary.org/obo/RO_0002202",
    "label": "develops from"}]'
  snapshot_sha256: c3f1f945a7973cdf4b8971cb0a7c773dfdfe5580aa6ca63ef0eaca5d34423cce
- evidence_id: EX4
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001173
  locator: Current identity, definition and typed relations
  accessed_at: '2026-10-15T10:52:53Z'
  support: supports
  summary: 'UBERON:0001173 biliary tree; inspected definition: ["The path in many
    species is as follows: Bile canaliculi -> Canals of Hering (intralobar bile duct)
    -> interlobular bile ducts -> intrahepatic bile ducts -> left and right hepatic
    ducts merge to form -> common hepatic duct *exits liver* and joins -> cystic duct
    (from gall bladder) forming -> common bile duct -> joins with pancreatic duct
    -> forming ampulla of Vater -> enters duodenum [WP]", "A complex network of conduits
    that begins with the canals of Hering (intralobar bile duct) and progressively
    merges into a system of interlobular, septal, and major ducts which then coalesce
    to form the extrahepatic bile ducts, which finally deliver bile to the intestine,
    and in some species to the gallbladder."] Typed synonyms: [{"name": "biliary tract",
    "scope": "hasRelatedSynonym", "type": null, "xrefs": [{"database": "MA", "id":
    "0001273", "description": null, "url": "http://www.informatics.jax.org/searches/AMA.cgi?id=MA:0001273"}]}]'
  snapshot_sha256: 37320ff91102de4a8c23a02276a955e085041a65dba3cb570e5d8a8c22dcb9f9
- evidence_id: EX5
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A27100044%20AND%20SRC%3AMED&format=json&resultType=core&pageSize=12
  locator: Primary abstract and identifier metadata
  accessed_at: '2026-10-15T10:53:28Z'
  support: supports
  summary: PMID:27100044; DOI:10.3109/23744235.2016.1157896. Three genome-identified
    S. pseudopneumoniae isolates came from blood cultures with an apparent liver or
    bile-duct origin of infection. This is contextual hepatobiliary association, not
    direct bile-duct specimen evidence.
  snapshot_sha256: 4d71b5e3098c5a51675374d2a0802612ee4cf5d8d19a14773f5e6baa014e2492
- evidence_id: EX6
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1000561,1110546,1123317,1177117,1191475,1233262,1236904,1238993,1257037,1257038,1257039,1257040,1257041,1257042,1280,1283,1292046,1321369,1367494,137591,1392869,1408271,1408272,1408273,1408274,1810840,257758,282199,440512,470&retmode=xml
  locator: Exact TaxId, aliases, ScientificName, rank and lineage
  accessed_at: '2026-10-15T10:52:57Z'
  support: supports
  summary: '[{"id": "NCBITaxon:257758", "label": "Streptococcus pseudopneumoniae",
    "current_id": "257758", "current_name": "Streptococcus pseudopneumoniae", "current_rank":
    "species", "lineage": "cellular organisms; Bacteria; Bacillati; Bacillota; Bacilli;
    Lactobacillales; Streptococcaceae; Streptococcus"}]'
  snapshot_sha256: c0e0525844dde33d0c1309b8876344c9404ef26c8769b279c3b5aae5f5a2a5df
- evidence_id: EAFTER
  kind: record_content
  reference: data/habitats/host_associated/bile_duct.yaml
  locator: Entire current YAML
  accessed_at: '2026-10-15T11:42:56Z'
  support: supports
  summary: 'Complete current target: {"identifier": "BTO:0000122", "label": "bile
    duct", "definition": "Any of the ducts that convey bile in and from the liver.",
    "definition_source": "BTO", "habitat_category": "HOST_ASSOCIATED", "grounding_status":
    "EXACT", "mapping_status": "REVIEWED", "synonyms": [{"synonym_text": "Bile ducts",
    "synonym_type": "EXACT_SYNONYM", "source": "GOLD"}, {"synonym_text": "bile ducts",
    "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "biliary
    duct", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text":
    "biliary ducts", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text":
    "gall duct", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text":
    "gall ducts", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}], "source_attestations":
    [{"source": "GOLD", "source_id": "gold.ecosystem:6719", "source_label": "Bile
    ducts", "source_path": "Host-associated > Mammals > Digestive system > Biliary
    tract > Bile ducts", "mapping_predicate": "skos:exactMatch"}, {"source": "PREGO",
    "source_id": "BTO:0000122", "source_label": "bile duct", "assertion_count": 1,
    "assertion_unit": "TAXON", "score": 3.0, "evidence_channels": "annotated_genomes_isolates"}],
    "characteristic_taxa": [{"taxon_id": "NCBITaxon:257758", "source": "PREGO", "taxon_label":
    "Streptococcus pseudopneumoniae", "score": 3.0, "rank": 1, "candidate_pool": 1}],
    "curation_history": [{"timestamp": "2026-08-12T00:00:00Z", "curator": "claude-opus-5",
    "action": "GROUND", "changes": "Grounded to BTO:0000122 ''bile duct'' (EXACT).
    Leaf label equals the BTO label exactly and no other source concept claims it.
    Path: Host-associated > Mammals > Digestive system > Biliary tract > Bile ducts
    (source concept habitatmech:GOLD.ce334980d0)"}, {"timestamp": "2026-08-13T00:00:00Z",
    "curator": "claude-opus-5", "action": "REVIEW", "changes": "Reviewed and endorsed
    the seeder''s own resolution. Multi-source review pass: this record is attested
    by more than one independent vocabulary, and this source''s label or path was
    read against the record''s ontology term to check the merge is right. It agrees.
    Source concepts in the same pass whose labels did not agree were re-decided rather
    than endorsed; see the pass''s other decisions of the same date. (source concept
    habitatmech:PREGO.27e62ea512)"}, {"timestamp": "2026-08-16T05:58:02Z", "curator":
    "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from
    data/raw/ inventories; attested by GOLD, PREGO. Grounding: EXACT."}, {"timestamp":
    "2026-10-15T00:00:00Z", "curator": "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED",
    "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.de5efc0eb8
    for habitatmech:GOLD.ce334980d0 (Host-associated > Mammals > Digestive system
    > Biliary tract > Bile ducts). Review https://github.com/CultureBotAI/HabitatMech/issues/2177
    : A duct is part of, not a kind of, the whole mammal biliary tract. Suppress only
    the exact GOLD context contribution. Preserve independent parents, identity, source
    path/node/count/unit, taxa, native status and prior history. No source-scope or
    mapping-endpoint certification is implied."}]}'
  snapshot_sha256: f29c75f42d6d557df79a5116fb2e2e126f7cc8244e52e889471484e8463360ca
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261015T112625Z-bile_duct-remediation/review.yaml
  locator: Immediate immutable predecessor
  accessed_at: '2026-10-15T11:42:56Z'
  support: supports
  summary: Scientific findings and dispositions remain unchanged.
  snapshot_sha256: 51baf5c0cec97364c5768aee78e78e1f925aae5db1a5245c274cb0d3ae5f565b
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_biliary_bivalve_review_repairs.py
  locator: Whole-corpus counterfactual
  accessed_at: '2026-10-15T11:26:25Z'
  support: supports
  summary: Restoring only prior rules changes exactly fifteen records. Identity, definitions,
    source observations/counts/units, taxa, native statuses, valid parents and prior
    history are preserved; regeneration is repeatable.
  snapshot_sha256: 1412766b81259472012db4a0b75b171a12d854357f7c6d2d79289dcbcb1882d0
- evidence_id: EI0
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: Current maintained rows
  accessed_at: '2026-10-15T11:42:56Z'
  support: supports
  summary: '[[7, {"identifier": "habitatmech:GOLD.ce334980d0", "source_path": "Host-associated
    > Mammals > Digestive system > Biliary tract > Bile ducts", "parent_id": "habitatmech:GOLD.de5efc0eb8",
    "curator": "codex-gpt-5", "date": "2026-10-15", "notes": "Review https://github.com/CultureBotAI/HabitatMech/issues/2177
    : A duct is part of, not a kind of, the whole mammal biliary tract. Suppress only
    the exact GOLD context contribution. Preserve independent parents, identity, source
    path/node/count/unit, taxa, native status and prior history. No source-scope or
    mapping-endpoint certification is implied."}]]'
  snapshot_sha256: a92f9003cc5f57c397ab5118474318f216077a8e9f90564d21dfa8089477a2eb
- evidence_id: ELINK
  kind: record_content
  reference: tests/test_biliary_review_links.py
  locator: Issue URL boundary regression
  accessed_at: '2026-10-15T11:42:56Z'
  support: supports
  summary: The regression failed before correction and passed afterward for all 18
    new notes. Parsed generated HTML verifies 18 exact hrefs on 15 pages. Whole-record
    comparison permits only the expected whitespace before colon; all semantic JSONL
    bytes are identical.
  snapshot_sha256: c93aef11ddc15313ad428e63e6123483e9a78ba12149d734a2440dc25de439f8
assessments:
- assessment_id: A1
  area: consistency
  topic: Exact correction and whole-record preservation
  outcome: supported
  summary: The whole-corpus counterfactual and complete current YAML demonstrate bounded
    hierarchy/synonym changes, preserved source metadata and status, and repeatable
    generation.
  target_ids:
  - BTO:0000122
  evidence_ids:
  - EAFTER
  - EPREV
  - ETEST
  - EI0
- assessment_id: A2
  area: evidence
  topic: Retained scientific support
  outcome: supported
  summary: The target was rechecked against retained typed ontology and bounded primary
    evidence. No new characteristic-presence, prevalence or mechanism claim is added.
  target_ids:
  - BTO:0000122
  evidence_ids:
  - EAFTER
  - EPREV
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
- assessment_id: A3
  area: consistency
  topic: Publication correction preserves scientific content
  outcome: supported
  summary: Complete target comparison permits only URL-boundary spacing in the new
    deterministic curation history. All scientific claims and unresolved limitations
    remain unchanged.
  target_ids:
  - BTO:0000122
  evidence_ids:
  - EAFTER
  - EPREV
  - ELINK
findings:
- finding_id: F1
  issue_key: bile-duct-source-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Source context is asserted as a strictly broader habitat
  description: A duct is part of a biliary tract, not a subclass of the whole mammal
    tract. Exclude only the exact GOLD contribution habitatmech:GOLD.de5efc0eb8 using
    source-path and expected-parent guards. Preserve independent ontology genera,
    counts, identities and native status. The linked issue is related context; additional
    host witnesses expand its original examples.
  target_ids:
  - BTO:0000122
  field_paths:
  - parent_habitats
  evidence_ids:
  - EAFTER
  - EPREV
  - ETEST
  - EI0
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or source-evidence claim;
    deterministic validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1380
  - https://github.com/CultureBotAI/HabitatMech/issues/2177
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261015T112625Z-bile_duct-remediation
    finding_id: F1
  disposition_reason: Exact source-path and expected-parent guards suppress only the
    reviewed GOLD context edge. Independent ontology parents, source attestations/counts/units,
    identity and status remain.
actions: []
limitations:
- Same-agent review is not independent approval. Review does not promote native scientific
  status.
- Original source-member and source-precision limitations from the predecessor remain;
  preserved assertions are not independently confirmed specimens.
- Final full QC, archive integrity and real semantic-map/site publication are subsequent
  gates, not claimed completed in this observation.
- Configured label correspondence retains documented no-adapter skips; this is not
  global identifier or semantic certification.
- 'Shared mapping endpoints #1398 and typed ontology extraction #1249 remain open.
  iModulonDB is not applicable; no gene/expression assertion is made.'
notes:
- 'Publication repair https://github.com/CultureBotAI/HabitatMech/issues/2179; broader
  renderer issue #2046 remains open. Native seeding/site regeneration and whole-record
  comparison preserve all scientific fields and unchanged semantic-map input bytes.
  All earlier review bundles and session history remain immutable.'
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261015T110628Z-bile_duct-record
  relationship: Exact predecessor; every original finding identity and lineage retained.
- repository: CultureBotAI/HabitatMech
  review_id: 20261015T112625Z-bile_duct-remediation
  relationship: Immediate predecessor; all finding identities and dispositions preserved
    after publication-only correction.
```
