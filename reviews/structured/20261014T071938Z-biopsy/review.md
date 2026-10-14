# Scientific record review: Biopsy

- Review: 20261014T071938Z-biopsy
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-14T07:06:32.751552Z
- Finished UTC: 2026-10-14T07:19:38.697311Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The corrected NOT_APPLICABLE source mint preserves a collection-method grouping without treating a procedure as a habitat or discarding observed strains. The procedure xref is appropriate; neither a shared anatomical site nor the original full source membership is established.

## Scope And Provenance

Complete current record and every contributing source concept, with all displayed associations assessed.

Selection: Next unreviewed target in the clinical category from an ignored-inclusive census: 963/3208 current targets had completed individual scientific reviews; clinical was 0/4. This bundle covers exactly one record, not a sampled or whole-corpus pass.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 67732dd433da5dce91dbd771d6dd0c138775a11b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:BACDIVE.3d4fdc29fb | data/habitats/clinical/biopsy.yaml | generated | Biopsy |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native validate | passed | True | habitatmech:BACDIVE.3d4fdc29fb | Executed 2026-10-14T07:06:57.339736Z to 2026-10-14T07:07:00.293264Z. No issues found. |
| Native validate-strict | passed | True | habitatmech:BACDIVE.3d4fdc29fb | Executed 2026-10-14T07:07:09.611582Z to 2026-10-14T07:07:15.437010Z. Four clinical records scanned, zero ERROR rows. |
| Native validate-history | passed | True | habitatmech:BACDIVE.3d4fdc29fb | Executed 2026-10-14T07:07:15.437751Z to 2026-10-14T07:07:25.598348Z. 648 valid history records. |
| Native provenance-check | passed | True | habitatmech:BACDIVE.3d4fdc29fb | Executed 2026-10-14T07:07:25.598994Z to 2026-10-14T07:07:26.332226Z. 14 committed inventories and two GOLD source receipts current. |
| Native verify-corpus | passed | True | habitatmech:BACDIVE.3d4fdc29fb | Executed 2026-10-14T07:07:26.332987Z to 2026-10-14T07:07:47.892693Z. All 3,208 records reproduce exactly; zero missing, extra or differing records. |
| Native validate-causal-all | passed | True | habitatmech:BACDIVE.3d4fdc29fb | Executed 2026-10-14T07:07:47.893286Z to 2026-10-14T07:07:52.787835Z. 32 overlays and 32 graphs valid; no target-owned clinical overlay found. |
| Native term-requests-check | passed | True | habitatmech:BACDIVE.3d4fdc29fb | Executed 2026-10-14T07:07:52.788536Z to 2026-10-14T07:08:17.578375Z. Term-request table current: 109 terms. |
| Native validate-products | passed | True | habitatmech:BACDIVE.3d4fdc29fb | Executed 2026-10-14T07:08:17.579139Z to 2026-10-14T07:09:32.527722Z. 1,178 canonical matches, one synonym match, five accepted exceptions and 2,057 no-adapter skips. NCIT and taxon semantics are verified separately. |
| Clinical identity preservation regressions | passed | True | habitatmech:BACDIVE.3d4fdc29fb | ..                                                                       [100%]<br>2 passed in 10.40s Actual execution 2026-10-14T07:10:47.852501Z to 2026-10-14T07:10:59.612182Z. |
| Exact-base hosted authoritative QC | passed | True | habitatmech:BACDIVE.3d4fdc29fb | Verified success and exact base SHA; reuses the completed native full-QC execution rather than rerunning it locally for four report additions. |
| Original source-member reconstruction | unavailable | False | habitatmech:BACDIVE.3d4fdc29fb | Original frozen BacDive node/edge dumps were not found in the explicit ignored-inclusive search roots; complete strain-level claims are outside the established evidence. |
| Structured expression cross-check applicability | not_applicable | False | habitatmech:BACDIVE.3d4fdc29fb | No named gene, regulator, pathway, expression module or transcriptomic dataset is claimed. Taxon/source occurrence alone is not an iModulonDB functional assertion. |

## Scientific And Domain Assessments

### Source meaning and material/procedure boundary

identity: supported. Targets: habitatmech:BACDIVE.3d4fdc29fb.

Biopsy is the exact BacDive source grouping, not NCIT:C15189 itself. The native mint is habitatmech:BACDIVE.3d4fdc29fb. NCI distinguishes removal for examination (C15189) from the material obtained (C18202). BacDive 154980 simultaneously supplies a biopsy tag and maxillary bone/site information. This supports the collection-method interpretation without asserting that all source sites are unknown, all specimens are solid tissue, or specimens cannot host microbes.

### Source decision, predicate and scientific status

grounding: supported. Targets: habitatmech:BACDIVE.3d4fdc29fb.

The sole ITEM NOT_APPLICABLE decision at curation/decisions.tsv:1739 overrides the lexical CLOSE procedure mapping at isolation_source_groundings.tsv:38. It retains C15189 only as an xref, pins CLINICAL, and produces REVIEWED. No exact mapping predicate or parent is emitted. This agrees with the decision semantics and term-request exclusion, not the historical CONFIRM_UNGROUNDED recommendation.

### Strictly broader parents and nearby candidate boundaries

grounding: supported. Targets: habitatmech:BACDIVE.3d4fdc29fb.

No parent is asserted. A diagnostic procedure or an assumed generic animal tissue is not a justified superclass of this source grouping. The current record does not import the procedure superclass C18020. The separately defined biopsy specimen C18202 is a nearby material concept, not automatic identity evidence.

### Definition and source-synonym scope

nomenclature: supported. Targets: habitatmech:BACDIVE.3d4fdc29fb.

No definition or synonym is emitted. The existing research lead proposes unspecified host tissue but acknowledges it is not a biopsy definition; its old CONFIRM_UNGROUNDED recommendation and stronger claims about specimens/sites are not adopted. No supported definition or genus should be invented to populate an optional field.

### Source counts, distinct-strain ranking and truncation

quantity: supported. Targets: habitatmech:BACDIVE.3d4fdc29fb.

The single attestation retains 95 STRAIN assertions. The 25 displayed taxon rows come from a pool of 73; retained association counts sum to 47. All displayed IDs, labels, counts and ranks exactly match their frozen raw rows. Aggregate source edges and distinct-strain taxon joins are different computations; no patient, prevalence, publication or independent-site interpretation is asserted. No count is replaced by a current illustrative source page.

### Every displayed taxon identity and observation scope

nomenclature: supported. Targets: habitatmech:BACDIVE.3d4fdc29fb.

All 25 displayed IDs resolve directly. Current taxonomic ranks: {'species': 17, 'subspecies': 1, 'strain': 7}. The numeric association rank is distinct from taxonomic rank. No is_characteristic or independent corroboration is asserted; taxonomy verification does not validate isolation membership, disease causation or typical ecology.

NCBITaxon:210: Helicobacter pylori -&gt; Helicobacter pylori [species]
NCBITaxon:84112: Eggerthella lenta -&gt; Eggerthella lenta [species]
NCBITaxon:46124: Granulicatella adiacens -&gt; Granulicatella adiacens [species]
NCBITaxon:199: Campylobacter concisus -&gt; Campylobacter concisus [species]
NCBITaxon:1177574: Prevotella jejuni -&gt; Prevotella jejuni [species]
NCBITaxon:1506: Clostridium sp. -&gt; Clostridium sp. [species]
NCBITaxon:1747: Cutibacterium acnes -&gt; Cutibacterium acnes [species]
NCBITaxon:32021: Campylobacter jejuni subsp. doylei -&gt; Campylobacter jejuni subsp. doylei [subspecies]
NCBITaxon:102618: Helicobacter pylori NCTC 11637 = CCUG 17874 = ATCC 43504 = JCM 12093 -&gt; Helicobacter pylori NCTC 11637 = CCUG 17874 = ATCC 43504 = JCM 12093 [strain]
NCBITaxon:1031752: Campylobacter hyointestinalis subsp. lawsonii CCUG 27631 -&gt; Campylobacter hyointestinalis subsp. lawsonii CCUG 27631 [strain]
NCBITaxon:110505: Mycobacterium heckeshornense -&gt; Mycobacterium heckeshornense [species]
NCBITaxon:1210078: Nocardia kruczakiae NBRC 101016 -&gt; Nocardia kruczakiae NBRC 101016 [strain]
NCBITaxon:1223489: Nocardia niwae NBRC 108934 = DSM 45340 -&gt; Nocardia niwae NBRC 108934 = DSM 45340 [strain]
NCBITaxon:1254: Pediococcus acidilactici -&gt; Pediococcus acidilactici [species]
NCBITaxon:1265311: Mycobacterium arosiense ATCC BAA-1401 = DSM 45069 -&gt; Mycobacterium arosiense ATCC BAA-1401 = DSM 45069 [strain]
NCBITaxon:1302: Streptococcus gordonii -&gt; Streptococcus gordonii [species]
NCBITaxon:1306: Streptococcus sp. -&gt; Streptococcus sp. [species]
NCBITaxon:131111: Schaalia turicensis -&gt; Schaalia turicensis [species]
NCBITaxon:132249: Nocardia veterana -&gt; Nocardia veterana [species]
NCBITaxon:134034: Corynebacterium freneyi -&gt; Corynebacterium freneyi [species]
NCBITaxon:1380685: Kroppenstedtia pulmonis -&gt; Kroppenstedtia pulmonis [species]
NCBITaxon:141349: Mycobacterium lentiflavum -&gt; Mycobacterium lentiflavum [species]
NCBITaxon:1423749: Limosilactobacillus gastricus DSM 16045 -&gt; Limosilactobacillus gastricus DSM 16045 [strain]
NCBITaxon:1423763: Lactobacillus kalixensis DSM 16043 -&gt; Lactobacillus kalixensis DSM 16043 [strain]
NCBITaxon:1430326: Mycobacterium decipiens -&gt; Mycobacterium decipiens [species]

### Environmental measurements and contextual facets

evidence: supported. Targets: habitatmech:BACDIVE.3d4fdc29fb.

No environmental parameters or MIxS triad values are emitted or supported by a matching target inventory row. Culture temperatures, physiology and host attributes of an illustrative strain are not habitat-wide measurements. Optional conditions are not invented.

### Literature, mechanism edges and datasets

graph: supported. Targets: habitatmech:BACDIVE.3d4fdc29fb.

No causal graph, record literature collection, discussion or dataset is emitted. Missing optional fields are not a defect by themselves. Inspected primary sources support only the bounded identity/context claims stated here; neither occurrence nor a study abstract supplies generic causal edges.

### Generated events, source provenance and status

provenance: supported. Targets: habitatmech:BACDIVE.3d4fdc29fb.

The 2026-10-07 ITEM correction and append-only biopsy session explain the earlier status inconsistency. The generated seed and current decision events agree with maintained inputs. The historical ad hoc review remains historical; this observation does not rewrite it or fabricate structured predecessor finding IDs.

### Original extension and optional enrichment

completeness: unknown. Targets: habitatmech:BACDIVE.3d4fdc29fb.

The complete current artifact was reviewed, but original source-member reconstruction remains unavailable. Preserve the source-qualified observations and their limits. Any later source refresh belongs in manifest-bound extraction inputs; decisions and optional supported definitions belong in maintained curation inputs, followed by native reproduction, schema/history/labels, semantic-map/site checks and full QC. No scientific or generated file is edited by this review.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| RECORD | data/habitats/clinical/biopsy.yaml; Entire HabitatRecord | supports | Read the complete current YAML, including every attestation, taxon and event; no projection is substituted for the target. |
| INPUTS | data/raw/; curation/decisions.tsv; data/raw/bacdive_source_taxa.tsv:239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263; data/raw/isolation_source_groundings.tsv:38; data/raw/bacdive_isolation_sources.tsv:72; data/raw/ontology_subclass_edges.tsv:9071; data/raw/ontology_terms.tsv:10778; curation/term_requests_excluded.tsv:7; curation/decisions.tsv:1739 | supports | Parsed every raw/curation TSV and inspected each exact-key matched row. Source mint, count/unit, all displayed taxon fields and ITEM decision agree. Rows below distinguish raw ontology parents of neighbors from the target's own parent. |
| RULES | docs/CURATION.md; Decision model; hosts/anatomy; evidence; local record checklist | supports | Applied habitat identity, decision semantics, strict-superclass, source-predicate, unit, observation and ITEM-status rules; used the local checklist and harmonization/research guides. |
| TRANSFORM | src/habitatmech/extract.py; extract_bacdive; src/habitatmech/seed.py:mint, resolve_bacdive | supports | extract_bacdive counts source outgoing edges for aggregate strain_count, but uses a distinct-strain set for the source-to-strain-to-taxon join; retained taxa are sorted by descending count then CURIE and truncated to top 25. seed.mint includes the BACDIVE namespace, and resolve_bacdive honors blank upstream targets and mapping predicates. |
| TAXONOMY | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;retmode=xml&amp;id=199,210,287,446,469,529,550,562,573,817,1254,1280,1282,1283,1295,1302,1304,1306,1313,1352,1381,1496,1506,1559,1590,1596,1686,1747,13689,32021,33889,34062,37329,37637,40324,43767,43771,46124,47312,47715,47885,60552,76832,84112,85698,102618,110505,119206,131111,132249,134034,141349,144185,151416,151454,170994,756689,759851,1031752,1177574,1210078,1223489,1265311,1341646,1380685,1423749,1423763,1430326,1443941,1671023; EFetch Taxon: TaxId, ScientificName, Rank, OtherNames, AkaTaxIds | supports | All 70 distinct requested IDs resolve directly; every target label matches a scientific name or recognized alternative. This verifies taxonomy, not isolation, infection or characteristic ecology. |
| BACDIVE | https://bacdive.dsmz.de/strain/154980; Isolation source categories and Isolation table | supports | The isolation section identifies a human maxillary bone biopsy and supplies independent body-site categories alongside Patient/Biopsy. This is an illustrative source-facet witness, not recovery of any particular member of the frozen 95-strain aggregate. |
| C15189 | https://api-evsrest.nci.nih.gov/api/v1/concept/ncit/C15189?include=full; Release 26.09d; code/name, definitions, synonyms and direct parents | supports | Biopsy Procedure denotes diagnostic removal of tissue or fluid and has Diagnostic Procedure as its direct parent. This supports the procedure xref, not habitat identity. |
| C18202 | https://api-evsrest.nci.nih.gov/api/v1/concept/ncit/C18202?include=full; Release 26.09d; code/name, definitions, synonyms and direct parents | supports | Biopsy Specimen denotes material obtained through biopsy and has Biospecimen as its direct parent. This is distinct from the procedure and does not determine a shared anatomical site. |
| HISTORY | history/mappings/; curation/decisions.tsv; Target-specific sessions where present; all current generated events and ITEM source decision | supports | The 2026-10-07 ITEM correction and append-only biopsy session explain the earlier status inconsistency. The generated seed and current decision events agree with maintained inputs. The historical ad hoc review remains historical; this observation does not rewrite it or fabricate structured predecessor finding IDs. |
| SEARCH | HabitatMech local filesystem | supports | Ignored-inclusive ID/label/slug/mint searches and structured inventory traversal identify the maintained owners. No matching target-owned causal overlay or authored term request was found in those maintained locations. Biopsy has an exclusion row and a research lead, not an authored habitat definition. |
| SOURCE_GAP | conf/sources.yaml; data/raw/MANIFEST.yaml | context_only | The ignored-inclusive search found the two committed BacDive aggregate inventories, but no original BacDive nodes.tsv/edges.tsv in the searched roots. The full frozen strain joins and aggregate distinctness were not reconstructed. |
| BASE_QC | https://github.com/CultureBotAI/HabitatMech/actions/runs/38523709970; Build and test, merge_group; Run the authoritative quality gate | supports | Completed successful authoritative QC on exact captured base 67732dd433da5dce91dbd771d6dd0c138775a11b: 1,065 tests passed, three skipped, four separate contract tests passed. Reused exact-base execution, not a new local full-QC run. Scientific inputs remain unchanged by git diff; this does not validate future saved reports. |
| PRIOR | reports/yaml_record_review/20261007T024737Z-biopsy.md; Historical target assessment and limitations; ignored-inclusive structured review census | context_only | Historical target reviews were used as leads and checked against fresh primary sources/current inputs, not copied as proof or migrated as current scientific review. No structured predecessor for this exact target was found in the complete review census. |
| RESEARCH | research/habitats/clinical/biopsy-habitatmech-bacdive-3d4fdc29fb-deep-research-claude_code.md; Scientific report sections 1, 2, 5 and 6; a research lead, not a maintained definition | context_only | The inspected recommendation identifies a method-defined grouping but recommends the old habitat-confirmation enum and makes stronger unsupported material/site generalizations. Its proposed unspecified-tissue definition and inference that specimens cease to be habitats are not adopted. The current ITEM correction is evaluated against primary sources instead. |

## Limits And Additional Notes

- Original frozen BacDive strain-level joins, aggregate duplicate-edge behavior and complete source membership were not reconstructed. Preserved inventory counts are not an independently recounted cohort.
- Current primary source examples establish only the identified record facets; they do not demonstrate membership of the frozen extraction or universal clinical ecology.
- NCI/NCBI identifiers and selected study abstracts were inspected directly. This is not a full-text systematic clinical review, diagnostic advice or a claim of generic mechanism evidence.
- Label correspondence retains five configured exceptions and 2,057 no-adapter skips. Direct checks supplement only the terms and taxa named in this review.
- Full QC is reused from the exact captured base; fresh native target/corpus gates are recorded separately. Archive validation follows saving and is not preclaimed in this immutable bundle.
- No SSSOM/KGX conformance certification, shared-issue closure, habitat-wide prevalence or native scientific-status promotion is implied.
- No curation, generated records, prior reports or history were edited. No paid research or GitHub mutation was performed in this review phase.
- Earlier unsaved clinical captures used base 471f0b0b. Fresh native inspection uses 67732dd4; the only previously captured input change is three unrelated aquatic rows in gold_parent_exclusions.tsv, inspected in the preceding publication. Supplemental input capture preserved every current prior hash and the actual assessment start.
- A temporary ledger initially omitted the namespace from mint hashing; it was corrected to the repository mint function and rerun before interpreting searches. The corrected exact decision rows and source keys are used throughout.
- Browser NCI requests were unavailable, but official REST retrieval succeeded. A temporary optional BeautifulSoup parser import failed before reading source data; the standard-library HTML parser retrieved and exposed the actual BacDive isolation sections. Neither fallback altered project dependencies.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T071938Z-biopsy
kind: record
repository: CultureBotAI/HabitatMech
title: 'Scientific record review: Biopsy'
started_at: '2026-10-14T07:06:32.751552Z'
finished_at: '2026-10-14T07:19:38.697311Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Same agent participated in earlier repository work; this is
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
scientific_review: true
verdict: pass_with_limitations
summary: The corrected NOT_APPLICABLE source mint preserves a collection-method grouping
  without treating a procedure as a habitat or discarding observed strains. The procedure
  xref is appropriate; neither a shared anatomical site nor the original full source
  membership is established.
source:
  git_revision: 67732dd433da5dce91dbd771d6dd0c138775a11b
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
    sha256: eb82cec48508912622b452ae78bb1ad199c93cb0591ce534bb8f25273da4e220
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 2d41fc93db4939122b3909f2a412b84b679703948b10d9f02e12021442f71407
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 27ba9a5fe34ef636e764af44c6a43f025e86d59fc25634e24d9c179a18322808
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: 331a7d9eb8a8909fc37402c0a776838979a8065644504d5c4f2a1c39bce5c24d
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: b59b9e800a918135e3915145d4d8098bb48dcea36a312b3004c594a57d221ae9
    role: context
  - path: data/habitats/clinical/biopsy.yaml
    sha256: 3081943ef8ffca6245365e5f77d0932265d229655ebf466c8dec7e4d20042cfe
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
    sha256: 105b3c8e10f43ce689b05d3089d3a8be1d713a98dd6806e11be37ebd85b10590
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/mappings/biopsy/2026-10-07T033538Z-codex-gpt-5-d9a381.yaml
    sha256: c9c150f51e2c2919def5d94ebd8833daf639424ac1c612acdd10b5959dda9c94
    role: context
  - path: history/mappings/medical_environment/2026-10-08T185937Z-claude-code-2693a1.yaml
    sha256: 8fb5e531d94a9c1559046ccf6446aa38dc29c8576505a6ba1bd28a0cffa6e5d3
    role: context
  - path: history/mappings/medical_environment/2026-10-08T190027Z-codex-42ea18.yaml
    sha256: bf4c33bcbdea6c9cce878a8199fc5ff762cc0f664c0a6004a5a238699fe70e6d
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20261007T024737Z-biopsy.md
    sha256: 9a919ca2b089f2a56d9ee6e089b890593d4bbda0bd82e9e85b8bc8b840670649
    role: context
  - path: reports/yaml_record_review/20261007T025146Z-catheter.md
    sha256: 77265026656eae2ec759de7c4b58a5c7d88d210cff3ac33daaeacf83e9d8c121
    role: context
  - path: reports/yaml_record_review/20261007T025511Z-tracheal_aspirate.md
    sha256: 016f50102818e9ac68e1fa6f0c256ad6f52955c755f837a87fcc7dd7a370852f
    role: context
  - path: reports/yaml_record_review/20261008T183330Z-hospital.md
    sha256: bbd02d563f8a8e5ccd03103b077e6bc307483fc6a3023b0e9f31c5904492bc13
    role: context
  - path: reports/yaml_record_review/20261008T193608Z-medical_environment.md
    sha256: 617a06554245d38090bcd4bc8fc30d89424fb51715f704417b12afc3f3110047
    role: context
  - path: research/habitats/clinical/biopsy-habitatmech-bacdive-3d4fdc29fb-deep-research-claude_code.md
    sha256: 2fa3792bf3d3c4e176a18f112a85a77f790863b51b04d5694ae2692ed47a6356
    role: context
  - path: reviews/structured/20261011T120147Z-hospital/review.yaml
    sha256: c4605a3a31acaefc46b73e7431acb2f09a8d801d895ec5f2c4d98b06a6dd1f5a
    role: context
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
    role: context
  - path: src/habitatmech/seed.py
    sha256: 4adf105e23d75c3563a516a0c160623d1065df7fcb2f31b7a0a0a8303d0401be
    role: context
  - path: tests/test_clinical_anaerobic_curation.py
    sha256: abf17eeb5a28b22c85dd55f8a5a7de6c40de7a201a9d0b91d931ec529217934c
    role: context
  - path: tests/test_hay_hospital_curation.py
    sha256: 0e5cc31805d1a1e3eaff84be41756fea2e7fd7eb26f39f52f0c4c30058cd7290
    role: context
targets:
- target_id: habitatmech:BACDIVE.3d4fdc29fb
  path: data/habitats/clinical/biopsy.yaml
  label: Biopsy
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: ITEM source-concept decision and status owner
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Optional authored definition owner
  - repository: CultureBotAI/HabitatMech
    path: data/raw/bacdive_isolation_sources.tsv
    role: Frozen source aggregate inventory
  - repository: CultureBotAI/HabitatMech
    path: data/raw/bacdive_source_taxa.tsv
    role: Frozen source-to-taxon association inventory
  - repository: CultureBotAI/HabitatMech
    path: data/raw/isolation_source_groundings.tsv
    role: Frozen upstream mapping inventory
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Governed ontology label and definition inventory
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_subclass_edges.tsv
    role: Governed ontology hierarchy inventory
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Source inventory extraction owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Generated-record resolution and emission owner
scope:
  description: Complete current record and every contributing source concept, with
    all displayed associations assessed.
  selection: 'Next unreviewed target in the clinical category from an ignored-inclusive
    census: 963/3208 current targets had completed individual scientific reviews;
    clinical was 0/4. This bundle covers exactly one record, not a sampled or whole-corpus
    pass.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:BACDIVE.3d4fdc29fb
checks:
- check_id: C0
  name: Native validate
  status: passed
  required: true
  target_ids:
  - habitatmech:BACDIVE.3d4fdc29fb
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/clinical/biopsy.yaml
  exit_code: 0
  summary: Executed 2026-10-14T07:06:57.339736Z to 2026-10-14T07:07:00.293264Z. No
    issues found.
  scope_note: Record-specific validate, four-record strict check, otherwise full-corpus
    native gate. Label checks retain five exceptions and 2,057 no-adapter skips; direct
    NCI and NCBI checks supplement, not universalize, this coverage.
- check_id: C4
  name: Native validate-strict
  status: passed
  required: true
  target_ids:
  - habitatmech:BACDIVE.3d4fdc29fb
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/clinical/biopsy.yaml data/habitats/clinical/catheter.yaml data/habitats/clinical/medical_environment.yaml
    data/habitats/clinical/tracheal_aspirate.yaml
  exit_code: 0
  summary: Executed 2026-10-14T07:07:09.611582Z to 2026-10-14T07:07:15.437010Z. Four
    clinical records scanned, zero ERROR rows.
  scope_note: Record-specific validate, four-record strict check, otherwise full-corpus
    native gate. Label checks retain five exceptions and 2,057 no-adapter skips; direct
    NCI and NCBI checks supplement, not universalize, this coverage.
- check_id: C5
  name: Native validate-history
  status: passed
  required: true
  target_ids:
  - habitatmech:BACDIVE.3d4fdc29fb
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  summary: Executed 2026-10-14T07:07:15.437751Z to 2026-10-14T07:07:25.598348Z. 648
    valid history records.
  scope_note: Record-specific validate, four-record strict check, otherwise full-corpus
    native gate. Label checks retain five exceptions and 2,057 no-adapter skips; direct
    NCI and NCBI checks supplement, not universalize, this coverage.
- check_id: C6
  name: Native provenance-check
  status: passed
  required: true
  target_ids:
  - habitatmech:BACDIVE.3d4fdc29fb
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  summary: Executed 2026-10-14T07:07:25.598994Z to 2026-10-14T07:07:26.332226Z. 14
    committed inventories and two GOLD source receipts current.
  scope_note: Record-specific validate, four-record strict check, otherwise full-corpus
    native gate. Label checks retain five exceptions and 2,057 no-adapter skips; direct
    NCI and NCBI checks supplement, not universalize, this coverage.
- check_id: C7
  name: Native verify-corpus
  status: passed
  required: true
  target_ids:
  - habitatmech:BACDIVE.3d4fdc29fb
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  summary: Executed 2026-10-14T07:07:26.332987Z to 2026-10-14T07:07:47.892693Z. All
    3,208 records reproduce exactly; zero missing, extra or differing records.
  scope_note: Record-specific validate, four-record strict check, otherwise full-corpus
    native gate. Label checks retain five exceptions and 2,057 no-adapter skips; direct
    NCI and NCBI checks supplement, not universalize, this coverage.
- check_id: C8
  name: Native validate-causal-all
  status: passed
  required: true
  target_ids:
  - habitatmech:BACDIVE.3d4fdc29fb
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  summary: Executed 2026-10-14T07:07:47.893286Z to 2026-10-14T07:07:52.787835Z. 32
    overlays and 32 graphs valid; no target-owned clinical overlay found.
  scope_note: Record-specific validate, four-record strict check, otherwise full-corpus
    native gate. Label checks retain five exceptions and 2,057 no-adapter skips; direct
    NCI and NCBI checks supplement, not universalize, this coverage.
- check_id: C9
  name: Native term-requests-check
  status: passed
  required: true
  target_ids:
  - habitatmech:BACDIVE.3d4fdc29fb
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  summary: 'Executed 2026-10-14T07:07:52.788536Z to 2026-10-14T07:08:17.578375Z. Term-request
    table current: 109 terms.'
  scope_note: Record-specific validate, four-record strict check, otherwise full-corpus
    native gate. Label checks retain five exceptions and 2,057 no-adapter skips; direct
    NCI and NCBI checks supplement, not universalize, this coverage.
- check_id: C10
  name: Native validate-products
  status: passed
  required: true
  target_ids:
  - habitatmech:BACDIVE.3d4fdc29fb
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  summary: Executed 2026-10-14T07:08:17.579139Z to 2026-10-14T07:09:32.527722Z. 1,178
    canonical matches, one synonym match, five accepted exceptions and 2,057 no-adapter
    skips. NCIT and taxon semantics are verified separately.
  scope_note: Record-specific validate, four-record strict check, otherwise full-corpus
    native gate. Label checks retain five exceptions and 2,057 no-adapter skips; direct
    NCI and NCBI checks supplement, not universalize, this coverage.
- check_id: FOCUSED
  name: Clinical identity preservation regressions
  status: passed
  required: true
  target_ids:
  - habitatmech:BACDIVE.3d4fdc29fb
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache uv run pytest -q tests/test_clinical_anaerobic_curation.py::test_biopsy_and_parent_curation_has_exact_scope
    tests/test_hay_hospital_curation.py::test_medical_environment_split_preserves_source_evidence
  exit_code: 0
  summary: '..                                                                       [100%]

    2 passed in 10.40s Actual execution 2026-10-14T07:10:47.852501Z to 2026-10-14T07:10:59.612182Z.'
  scope_note: Existing before/after preservation tests, not proof of original BacDive
    membership.
- check_id: QC
  name: Exact-base hosted authoritative QC
  status: passed
  required: true
  target_ids:
  - habitatmech:BACDIVE.3d4fdc29fb
  command: gh run view 38523709970 --json headSha,status,conclusion,url
  exit_code: 0
  summary: Verified success and exact base SHA; reuses the completed native full-QC
    execution rather than rerunning it locally for four report additions.
  evidence_ids:
  - BASE_QC
- check_id: MEMBERS
  name: Original source-member reconstruction
  status: unavailable
  required: false
  target_ids:
  - habitatmech:BACDIVE.3d4fdc29fb
  summary: Original frozen BacDive node/edge dumps were not found in the explicit
    ignored-inclusive search roots; complete strain-level claims are outside the established
    evidence.
  evidence_ids:
  - SOURCE_GAP
- check_id: IMODULON
  name: Structured expression cross-check applicability
  status: not_applicable
  required: false
  target_ids:
  - habitatmech:BACDIVE.3d4fdc29fb
  summary: No named gene, regulator, pathway, expression module or transcriptomic
    dataset is claimed. Taxon/source occurrence alone is not an iModulonDB functional
    assertion.
evidence:
- evidence_id: RECORD
  kind: record_content
  reference: data/habitats/clinical/biopsy.yaml
  accessed_at: '2026-10-14T07:19:38.696808Z'
  support: supports
  summary: Read the complete current YAML, including every attestation, taxon and
    event; no projection is substituted for the target.
  locator: Entire HabitatRecord
- evidence_id: INPUTS
  kind: record_content
  reference: data/raw/; curation/decisions.tsv
  accessed_at: '2026-10-14T07:19:38.696808Z'
  support: supports
  summary: Parsed every raw/curation TSV and inspected each exact-key matched row.
    Source mint, count/unit, all displayed taxon fields and ITEM decision agree. Rows
    below distinguish raw ontology parents of neighbors from the target's own parent.
  locator: data/raw/bacdive_source_taxa.tsv:239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263;
    data/raw/isolation_source_groundings.tsv:38; data/raw/bacdive_isolation_sources.tsv:72;
    data/raw/ontology_subclass_edges.tsv:9071; data/raw/ontology_terms.tsv:10778;
    curation/term_requests_excluded.tsv:7; curation/decisions.tsv:1739
- evidence_id: RULES
  kind: authority
  reference: docs/CURATION.md
  accessed_at: '2026-10-14T07:19:38.696808Z'
  support: supports
  summary: Applied habitat identity, decision semantics, strict-superclass, source-predicate,
    unit, observation and ITEM-status rules; used the local checklist and harmonization/research
    guides.
  locator: Decision model; hosts/anatomy; evidence; local record checklist
- evidence_id: TRANSFORM
  kind: record_content
  reference: src/habitatmech/extract.py
  accessed_at: '2026-10-14T07:19:38.696808Z'
  support: supports
  summary: extract_bacdive counts source outgoing edges for aggregate strain_count,
    but uses a distinct-strain set for the source-to-strain-to-taxon join; retained
    taxa are sorted by descending count then CURIE and truncated to top 25. seed.mint
    includes the BACDIVE namespace, and resolve_bacdive honors blank upstream targets
    and mapping predicates.
  locator: extract_bacdive; src/habitatmech/seed.py:mint, resolve_bacdive
- evidence_id: TAXONOMY
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&retmode=xml&id=199,210,287,446,469,529,550,562,573,817,1254,1280,1282,1283,1295,1302,1304,1306,1313,1352,1381,1496,1506,1559,1590,1596,1686,1747,13689,32021,33889,34062,37329,37637,40324,43767,43771,46124,47312,47715,47885,60552,76832,84112,85698,102618,110505,119206,131111,132249,134034,141349,144185,151416,151454,170994,756689,759851,1031752,1177574,1210078,1223489,1265311,1341646,1380685,1423749,1423763,1430326,1443941,1671023
  accessed_at: '2026-10-14T07:06:55.480811Z'
  support: supports
  summary: All 70 distinct requested IDs resolve directly; every target label matches
    a scientific name or recognized alternative. This verifies taxonomy, not isolation,
    infection or characteristic ecology.
  locator: 'EFetch Taxon: TaxId, ScientificName, Rank, OtherNames, AkaTaxIds'
  snapshot_sha256: 3921d1421fd709748d99c4b2814025cf572ed28fcfd58b6cbdab3c040b966600
- evidence_id: BACDIVE
  kind: database
  reference: https://bacdive.dsmz.de/strain/154980
  accessed_at: '2026-10-14T07:11:14.242622Z'
  support: supports
  summary: The isolation section identifies a human maxillary bone biopsy and supplies
    independent body-site categories alongside Patient/Biopsy. This is an illustrative
    source-facet witness, not recovery of any particular member of the frozen 95-strain
    aggregate.
  locator: Isolation source categories and Isolation table
  snapshot_sha256: fcd5339f94a986da58df81e89bce8df60f3195672730c4a44630bd832f72a139
- evidence_id: C15189
  kind: authority
  reference: https://api-evsrest.nci.nih.gov/api/v1/concept/ncit/C15189?include=full
  accessed_at: '2026-10-14T07:06:54.537701Z'
  support: supports
  summary: Biopsy Procedure denotes diagnostic removal of tissue or fluid and has
    Diagnostic Procedure as its direct parent. This supports the procedure xref, not
    habitat identity.
  locator: Release 26.09d; code/name, definitions, synonyms and direct parents
  snapshot_sha256: 320b869c0101d59c7d6d40b5c34036e6f69dfdcd016d81fd45046ace26fa75e3
- evidence_id: C18202
  kind: authority
  reference: https://api-evsrest.nci.nih.gov/api/v1/concept/ncit/C18202?include=full
  accessed_at: '2026-10-14T07:06:55.048956Z'
  support: supports
  summary: Biopsy Specimen denotes material obtained through biopsy and has Biospecimen
    as its direct parent. This is distinct from the procedure and does not determine
    a shared anatomical site.
  locator: Release 26.09d; code/name, definitions, synonyms and direct parents
  snapshot_sha256: 10495abca9fb4dc306dc607c1cabd27ab3a39dc512d2d1439386c6f10515997b
- evidence_id: HISTORY
  kind: record_content
  reference: history/mappings/; curation/decisions.tsv
  accessed_at: '2026-10-14T07:19:38.696808Z'
  support: supports
  summary: The 2026-10-07 ITEM correction and append-only biopsy session explain the
    earlier status inconsistency. The generated seed and current decision events agree
    with maintained inputs. The historical ad hoc review remains historical; this
    observation does not rewrite it or fabricate structured predecessor finding IDs.
  locator: Target-specific sessions where present; all current generated events and
    ITEM source decision
- evidence_id: SEARCH
  kind: search
  reference: HabitatMech local filesystem
  accessed_at: '2026-10-14T07:19:38.696808Z'
  support: supports
  summary: Ignored-inclusive ID/label/slug/mint searches and structured inventory
    traversal identify the maintained owners. No matching target-owned causal overlay
    or authored term request was found in those maintained locations. Biopsy has an
    exclusion row and a research lead, not an authored habitat definition.
  search_scope: rg --no-ignore --hidden -l -i -F -e Biopsy -e NCIT:C15189 -e bacdive.isolation_source:biopsy
    -e biopsy -e habitatmech:BACDIVE.3d4fdc29fb curation history research conf reviews/structured
    reports/yaml_record_review data/raw; raw/curation TSV exact-field scan; complete
    Path.rglob census of current habitat YAML and retained review YAML, including
    ignored files.
- evidence_id: SOURCE_GAP
  kind: search
  reference: conf/sources.yaml; data/raw/MANIFEST.yaml
  accessed_at: '2026-10-14T07:19:38.696808Z'
  support: context_only
  summary: The ignored-inclusive search found the two committed BacDive aggregate
    inventories, but no original BacDive nodes.tsv/edges.tsv in the searched roots.
    The full frozen strain joins and aggregate distinctness were not reconstructed.
  search_scope: rg --files --no-ignore --hidden build data/raw /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data
    -g *bacdive* -g *BacDive* -g nodes.tsv -g edges.tsv; no claim about other directories
    or remote archives.
- evidence_id: BASE_QC
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38523709970
  accessed_at: '2026-10-14T07:19:38.696808Z'
  support: supports
  summary: 'Completed successful authoritative QC on exact captured base 67732dd433da5dce91dbd771d6dd0c138775a11b:
    1,065 tests passed, three skipped, four separate contract tests passed. Reused
    exact-base execution, not a new local full-QC run. Scientific inputs remain unchanged
    by git diff; this does not validate future saved reports.'
  locator: Build and test, merge_group; Run the authoritative quality gate
- evidence_id: PRIOR
  kind: prior_review
  reference: reports/yaml_record_review/20261007T024737Z-biopsy.md
  accessed_at: '2026-10-14T07:19:38.696808Z'
  support: context_only
  summary: Historical target reviews were used as leads and checked against fresh
    primary sources/current inputs, not copied as proof or migrated as current scientific
    review. No structured predecessor for this exact target was found in the complete
    review census.
  locator: Historical target assessment and limitations; ignored-inclusive structured
    review census
- evidence_id: RESEARCH
  kind: record_content
  reference: research/habitats/clinical/biopsy-habitatmech-bacdive-3d4fdc29fb-deep-research-claude_code.md
  accessed_at: '2026-10-14T07:19:38.696808Z'
  support: context_only
  summary: The inspected recommendation identifies a method-defined grouping but recommends
    the old habitat-confirmation enum and makes stronger unsupported material/site
    generalizations. Its proposed unspecified-tissue definition and inference that
    specimens cease to be habitats are not adopted. The current ITEM correction is
    evaluated against primary sources instead.
  locator: Scientific report sections 1, 2, 5 and 6; a research lead, not a maintained
    definition
assessments:
- assessment_id: IDENTITY
  area: identity
  topic: Source meaning and material/procedure boundary
  outcome: supported
  summary: Biopsy is the exact BacDive source grouping, not NCIT:C15189 itself. The
    native mint is habitatmech:BACDIVE.3d4fdc29fb. NCI distinguishes removal for examination
    (C15189) from the material obtained (C18202). BacDive 154980 simultaneously supplies
    a biopsy tag and maxillary bone/site information. This supports the collection-method
    interpretation without asserting that all source sites are unknown, all specimens
    are solid tissue, or specimens cannot host microbes.
  target_ids:
  - habitatmech:BACDIVE.3d4fdc29fb
  evidence_ids:
  - RECORD
  - INPUTS
  - RULES
  - BACDIVE
  - C15189
  - C18202
  dimensions:
  - name: grounding_status
    value: NOT_APPLICABLE
    definition: Native relationship between source meaning and ontology identity,
      not scientific-review confidence.
    evidence_ids:
    - RECORD
    - INPUTS
  - name: source_scope
    value: BACDIVE isolation-source aggregate
    definition: One frozen source concept; not a single sampling site or a complete
      independently verified strain cohort.
    evidence_ids:
    - INPUTS
    - SOURCE_GAP
- assessment_id: GROUNDING
  area: grounding
  topic: Source decision, predicate and scientific status
  outcome: supported
  summary: The sole ITEM NOT_APPLICABLE decision at curation/decisions.tsv:1739 overrides
    the lexical CLOSE procedure mapping at isolation_source_groundings.tsv:38. It
    retains C15189 only as an xref, pins CLINICAL, and produces REVIEWED. No exact
    mapping predicate or parent is emitted. This agrees with the decision semantics
    and term-request exclusion, not the historical CONFIRM_UNGROUNDED recommendation.
  target_ids:
  - habitatmech:BACDIVE.3d4fdc29fb
  evidence_ids:
  - RECORD
  - INPUTS
  - RULES
  - TRANSFORM
  - C15189
  - C18202
- assessment_id: HIERARCHY
  area: grounding
  topic: Strictly broader parents and nearby candidate boundaries
  outcome: supported
  summary: No parent is asserted. A diagnostic procedure or an assumed generic animal
    tissue is not a justified superclass of this source grouping. The current record
    does not import the procedure superclass C18020. The separately defined biopsy
    specimen C18202 is a nearby material concept, not automatic identity evidence.
  target_ids:
  - habitatmech:BACDIVE.3d4fdc29fb
  evidence_ids:
  - RECORD
  - INPUTS
  - RULES
  - C15189
  - C18202
- assessment_id: LEXICAL
  area: nomenclature
  topic: Definition and source-synonym scope
  outcome: supported
  summary: No definition or synonym is emitted. The existing research lead proposes
    unspecified host tissue but acknowledges it is not a biopsy definition; its old
    CONFIRM_UNGROUNDED recommendation and stronger claims about specimens/sites are
    not adopted. No supported definition or genus should be invented to populate an
    optional field.
  target_ids:
  - habitatmech:BACDIVE.3d4fdc29fb
  evidence_ids:
  - RECORD
  - INPUTS
  - RULES
  - C15189
  - C18202
  - RESEARCH
- assessment_id: COUNTS
  area: quantity
  topic: Source counts, distinct-strain ranking and truncation
  outcome: supported
  summary: The single attestation retains 95 STRAIN assertions. The 25 displayed taxon
    rows come from a pool of 73; retained association counts sum to 47. All displayed
    IDs, labels, counts and ranks exactly match their frozen raw rows. Aggregate source
    edges and distinct-strain taxon joins are different computations; no patient,
    prevalence, publication or independent-site interpretation is asserted. No count
    is replaced by a current illustrative source page.
  target_ids:
  - habitatmech:BACDIVE.3d4fdc29fb
  evidence_ids:
  - RECORD
  - INPUTS
  - TRANSFORM
  - SOURCE_GAP
  metrics:
  - name: displayed_taxon_rows
    value: 25
    unit: taxon rows
    denominator: 73
    definition: Retained observational entries divided by the frozen source taxon
      pool; not a biological prevalence.
- assessment_id: TAXA
  area: nomenclature
  topic: Every displayed taxon identity and observation scope
  outcome: supported
  summary: 'All 25 displayed IDs resolve directly. Current taxonomic ranks: {''species'':
    17, ''subspecies'': 1, ''strain'': 7}. The numeric association rank is distinct
    from taxonomic rank. No is_characteristic or independent corroboration is asserted;
    taxonomy verification does not validate isolation membership, disease causation
    or typical ecology.'
  target_ids:
  - habitatmech:BACDIVE.3d4fdc29fb
  evidence_ids:
  - RECORD
  - INPUTS
  - TAXONOMY
  details: 'NCBITaxon:210: Helicobacter pylori -> Helicobacter pylori [species]

    NCBITaxon:84112: Eggerthella lenta -> Eggerthella lenta [species]

    NCBITaxon:46124: Granulicatella adiacens -> Granulicatella adiacens [species]

    NCBITaxon:199: Campylobacter concisus -> Campylobacter concisus [species]

    NCBITaxon:1177574: Prevotella jejuni -> Prevotella jejuni [species]

    NCBITaxon:1506: Clostridium sp. -> Clostridium sp. [species]

    NCBITaxon:1747: Cutibacterium acnes -> Cutibacterium acnes [species]

    NCBITaxon:32021: Campylobacter jejuni subsp. doylei -> Campylobacter jejuni subsp.
    doylei [subspecies]

    NCBITaxon:102618: Helicobacter pylori NCTC 11637 = CCUG 17874 = ATCC 43504 = JCM
    12093 -> Helicobacter pylori NCTC 11637 = CCUG 17874 = ATCC 43504 = JCM 12093
    [strain]

    NCBITaxon:1031752: Campylobacter hyointestinalis subsp. lawsonii CCUG 27631 ->
    Campylobacter hyointestinalis subsp. lawsonii CCUG 27631 [strain]

    NCBITaxon:110505: Mycobacterium heckeshornense -> Mycobacterium heckeshornense
    [species]

    NCBITaxon:1210078: Nocardia kruczakiae NBRC 101016 -> Nocardia kruczakiae NBRC
    101016 [strain]

    NCBITaxon:1223489: Nocardia niwae NBRC 108934 = DSM 45340 -> Nocardia niwae NBRC
    108934 = DSM 45340 [strain]

    NCBITaxon:1254: Pediococcus acidilactici -> Pediococcus acidilactici [species]

    NCBITaxon:1265311: Mycobacterium arosiense ATCC BAA-1401 = DSM 45069 -> Mycobacterium
    arosiense ATCC BAA-1401 = DSM 45069 [strain]

    NCBITaxon:1302: Streptococcus gordonii -> Streptococcus gordonii [species]

    NCBITaxon:1306: Streptococcus sp. -> Streptococcus sp. [species]

    NCBITaxon:131111: Schaalia turicensis -> Schaalia turicensis [species]

    NCBITaxon:132249: Nocardia veterana -> Nocardia veterana [species]

    NCBITaxon:134034: Corynebacterium freneyi -> Corynebacterium freneyi [species]

    NCBITaxon:1380685: Kroppenstedtia pulmonis -> Kroppenstedtia pulmonis [species]

    NCBITaxon:141349: Mycobacterium lentiflavum -> Mycobacterium lentiflavum [species]

    NCBITaxon:1423749: Limosilactobacillus gastricus DSM 16045 -> Limosilactobacillus
    gastricus DSM 16045 [strain]

    NCBITaxon:1423763: Lactobacillus kalixensis DSM 16043 -> Lactobacillus kalixensis
    DSM 16043 [strain]

    NCBITaxon:1430326: Mycobacterium decipiens -> Mycobacterium decipiens [species]'
- assessment_id: PARAMETERS
  area: evidence
  topic: Environmental measurements and contextual facets
  outcome: supported
  summary: No environmental parameters or MIxS triad values are emitted or supported
    by a matching target inventory row. Culture temperatures, physiology and host
    attributes of an illustrative strain are not habitat-wide measurements. Optional
    conditions are not invented.
  target_ids:
  - habitatmech:BACDIVE.3d4fdc29fb
  evidence_ids:
  - RECORD
  - INPUTS
  - SEARCH
  - BACDIVE
- assessment_id: MECHANISMS
  area: graph
  topic: Literature, mechanism edges and datasets
  outcome: supported
  summary: No causal graph, record literature collection, discussion or dataset is
    emitted. Missing optional fields are not a defect by themselves. Inspected primary
    sources support only the bounded identity/context claims stated here; neither
    occurrence nor a study abstract supplies generic causal edges.
  target_ids:
  - habitatmech:BACDIVE.3d4fdc29fb
  evidence_ids:
  - RECORD
  - SEARCH
- assessment_id: HISTORY
  area: provenance
  topic: Generated events, source provenance and status
  outcome: supported
  summary: The 2026-10-07 ITEM correction and append-only biopsy session explain the
    earlier status inconsistency. The generated seed and current decision events agree
    with maintained inputs. The historical ad hoc review remains historical; this
    observation does not rewrite it or fabricate structured predecessor finding IDs.
  target_ids:
  - habitatmech:BACDIVE.3d4fdc29fb
  evidence_ids:
  - RECORD
  - INPUTS
  - HISTORY
  - PRIOR
  - BASE_QC
- assessment_id: LIMITS
  area: completeness
  topic: Original extension and optional enrichment
  outcome: unknown
  summary: The complete current artifact was reviewed, but original source-member
    reconstruction remains unavailable. Preserve the source-qualified observations
    and their limits. Any later source refresh belongs in manifest-bound extraction
    inputs; decisions and optional supported definitions belong in maintained curation
    inputs, followed by native reproduction, schema/history/labels, semantic-map/site
    checks and full QC. No scientific or generated file is edited by this review.
  target_ids:
  - habitatmech:BACDIVE.3d4fdc29fb
  evidence_ids:
  - INPUTS
  - SOURCE_GAP
  - RULES
findings: []
actions: []
limitations:
- Original frozen BacDive strain-level joins, aggregate duplicate-edge behavior and
  complete source membership were not reconstructed. Preserved inventory counts are
  not an independently recounted cohort.
- Current primary source examples establish only the identified record facets; they
  do not demonstrate membership of the frozen extraction or universal clinical ecology.
- NCI/NCBI identifiers and selected study abstracts were inspected directly. This
  is not a full-text systematic clinical review, diagnostic advice or a claim of generic
  mechanism evidence.
- Label correspondence retains five configured exceptions and 2,057 no-adapter skips.
  Direct checks supplement only the terms and taxa named in this review.
- Full QC is reused from the exact captured base; fresh native target/corpus gates
  are recorded separately. Archive validation follows saving and is not preclaimed
  in this immutable bundle.
- No SSSOM/KGX conformance certification, shared-issue closure, habitat-wide prevalence
  or native scientific-status promotion is implied.
notes:
- No curation, generated records, prior reports or history were edited. No paid research
  or GitHub mutation was performed in this review phase.
- Earlier unsaved clinical captures used base 471f0b0b. Fresh native inspection uses
  67732dd4; the only previously captured input change is three unrelated aquatic rows
  in gold_parent_exclusions.tsv, inspected in the preceding publication. Supplemental
  input capture preserved every current prior hash and the actual assessment start.
- A temporary ledger initially omitted the namespace from mint hashing; it was corrected
  to the repository mint function and rerun before interpreting searches. The corrected
  exact decision rows and source keys are used throughout.
- Browser NCI requests were unavailable, but official REST retrieval succeeded. A
  temporary optional BeautifulSoup parser import failed before reading source data;
  the standard-library HTML parser retrieved and exposed the actual BacDive isolation
  sections. Neither fallback altered project dependencies.
tags:
- clinical
- record-review
- source-scope
```
