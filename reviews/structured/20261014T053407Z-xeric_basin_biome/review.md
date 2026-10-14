# Scientific record review: xeric basin biome

- Review: 20261014T053407Z-xeric_basin_biome
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-14T05:19:09.200634Z
- Finished UTC: 2026-10-14T05:34:07.737887Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The freshwater-biome identity is compatible with limited permanent surface water and must not be reclassified as terrestrial merely from xeric. The retained PREGO associations are source observations, not a characteristic microbial community.

## Scope And Provenance

One entire generated HabitatRecord and every contributing source concept. Parent records supply bounded hierarchy context only.

Selection: One of the 23 remaining aquatic targets lacking a completed individual scientific review in an ignored-independent census of 3208 current records.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 471f0b0b55721a1ba566525ae6e510dca644b892.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| ENVO:00000893 | data/habitats/aquatic/xeric_basin_biome.yaml | generated | xeric basin biome |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native validate | passed | True | ENVO:00000893 | Actual successful execution from 2026-10-14T05:19:24.346861Z to 2026-10-14T05:19:26.875770Z. Record-specific or full-corpus command scope is explicit. Reproduction and validation are not scientific approval. |
| Native validate-strict | passed | True | ENVO:00000893 | Actual successful execution from 2026-10-14T05:19:26.876441Z to 2026-10-14T05:19:35.258415Z. Record-specific or full-corpus command scope is explicit. Reproduction and validation are not scientific approval. |
| Native validate-history | passed | True | ENVO:00000893 | Actual successful execution from 2026-10-14T05:19:35.259097Z to 2026-10-14T05:19:43.590897Z. Record-specific or full-corpus command scope is explicit. Reproduction and validation are not scientific approval. |
| Native provenance-check | passed | True | ENVO:00000893 | Actual successful execution from 2026-10-14T05:19:43.591669Z to 2026-10-14T05:19:44.179190Z. Record-specific or full-corpus command scope is explicit. Reproduction and validation are not scientific approval. |
| Native verify-corpus | passed | True | ENVO:00000893 | Actual successful execution from 2026-10-14T05:19:44.179802Z to 2026-10-14T05:19:59.207478Z. Record-specific or full-corpus command scope is explicit. Reproduction and validation are not scientific approval. |
| Native validate-causal-all | passed | True | ENVO:00000893 | Actual successful execution from 2026-10-14T05:19:59.208144Z to 2026-10-14T05:20:03.719611Z. Record-specific or full-corpus command scope is explicit. Reproduction and validation are not scientific approval. |
| Native term-requests-check | passed | True | ENVO:00000893 | Actual successful execution from 2026-10-14T05:20:03.720302Z to 2026-10-14T05:20:23.391843Z. Record-specific or full-corpus command scope is explicit. Reproduction and validation are not scientific approval. |
| Native validate-products | passed | True | ENVO:00000893 | Actual successful execution from 2026-10-14T05:20:23.392546Z to 2026-10-14T05:21:30.920465Z. Record-specific or full-corpus command scope is explicit. Label gate: 1178 canonical, one synonym, five accepted exceptions and 2057 configured no-adapter skips; no taxon occurrence validation. |
| Complete document reproduction and input hash recheck | passed | True | ENVO:00000893 | Native build_corpus/build_document equality for all 23 complete target documents and captured-input hash equality passed; draft preparation rechecks all extended captures. |
| Exact-base hosted authoritative QC | passed | True | ENVO:00000893 | Successful hosted checks cover the exact unchanged scientific-input base, not these new bundles or a newly executed local full QC. |
| Expression-module adapter | not_applicable | False | ENVO:00000893 | No gene, regulator, protein or transcriptomic-module assertion occurs in this target. iModulonDB non-use is not evidence of biological absence. |

## Scientific And Domain Assessments

### Entity, grounding, strict hierarchy and source scope

identity: supported. Targets: ENVO:00000893.

ENVO:00000893 describes little permanent surface water and relatively few springs, with ENVO:00000873 freshwater biome as genus. Official FEOW listings include xeric freshwaters and endorheic basins, supporting the aquatic scope rather than a generic desert identity. The two PREGO alternate spellings remain related; no ENVO synonym is asserted.

### Claim-level scientific support, taxa, MIxS and source-unit limits

evidence: supported. Targets: ENVO:00000893.

PREGO row 247 has 36 TAXON/direct assertions, score 4 and environmental_samples; 25 ranked rows are retained. All nonempty labels resolve. The two omitted labels resolve to Coptotermes formosanus (36987, species) and Oryza sativa Indica Group (39946, no rank). The dataset includes nonmicrobial taxa and ranks; source associations do not assert microbial-only or is_characteristic status. Their original environmental-sample occurrences were not reconstructed, and no drought tolerance is inferred from membership.

### Generated status, history and optional-field completeness

provenance: supported. Targets: ENVO:00000893.

The complete record reproduces from maintained inputs, including EXACT/SEEDED, all source attestations and 1 historical events. REVIEWED requires all contributing ITEM decisions; CLASS decisions remain seeded. No review is a status promotion. The target asserts no causal graph or environmental-parameter block; source triads and external examples are not promoted into these optional slots.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| RECORD | data/habitats/aquatic/xeric_basin_biome.yaml | supports | The entire target was read before judgment, including all attestations, associations and generated events. Complete parsed-document reproduction and captured hash checks passed. The freshwater-biome identity is compatible with limited permanent surface water and must not be reclassified as terrestrial merely from xeric. The retained PREGO associations are source observations, not a characteristic microbial community. |
| RAW | data/raw/prego_habitat_taxa.tsv:5288,5289,5290,5291,5292,5293,5294,5295,5296,5297,5298,5299,5300,5301,5302,5303,5304,5305,5306,5307,5308,5309,5310,5311,5312; data/raw/prego_habitats.tsv:247; data/raw/ontology_subclass_edges.tsv:5247,5248,5255; data/raw/ontology_terms.tsv:7146,7153 | supports | Locators are logical TSV records counted with header as row 1. Structured scans and native document reproduction verify the emitted source paths, collapsed-node notes, count units, score channels, displayed association ranking and historical events. The source inventory is not independent experimental evidence. Exact emitted attestations: [{"source": "PREGO", "source_id": "ENVO:00000893", "source_label": "xeric basin biome", "assertion_count": 36, "assertion_unit": "TAXON", "score": 4.0, "evidence_channels": "environmental_samples"}] |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; docs/record-review-profile.md; .claude/skills/curate-yaml-record/references/review-checklist.md | supports | Applied habitat identity, strict genus, typed synonym, MIxS-role, source-unit, taxon-association and lifecycle rules. Optional missing fields are not automatically defects. Scientific review does not create ITEM decisions or promote native status. |
| OWNERS | curation/decisions.tsv; curation/gold_parent_exclusions.tsv; curation/term_requests.tsv; src/habitatmech/seed.py; src/habitatmech/extract.py; src/habitatmech/schema/habitatmech.yaml | supports | Read contributing maintained rows and source construction. The schema defines strictly broader parent_habitats and a source-to-record mapping predicate. Ontology ingestion retains an untyped synonym pipe; ConceptStore.get assigns exact scope to ontology aliases. Guarded GOLD exclusions remove only named source contributions. Source lifecycle requires every contributing source to have ITEM review before REVIEWED is emitted. |
| SEARCH | curation; history; research; conf; reviews/structured; reports/yaml_record_review; data/raw | supports | Bounded rg --no-ignore --hidden searches included ignored and hidden files and exact identifier, source IDs/mints, label and slug. Structured TSV scans and the recursive review census also ignore no files. No structured finding affecting these target IDs was found in the 1343-bundle census; legacy reports are historical leads, not successor-disposition lineage. Original sample membership was not reconstructed; no whole-filesystem absence is claimed. |
| ENVO | https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl; Named classes ENVO:00000873, ENVO:00000893 | supports | Official current file commit a2455d1a77e46bb8a664d65a157166b539269042, SHA256 a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c. Inspected definitions, named parents, deprecated flags and typed synonyms. Target/genus classes are active; historical triad annotations are checked separately, not silently promoted to current record assertions: {"ENVO:00000873": {"label": "freshwater biome", "definition": "An aquatic biome which is determined by a body of freshwater.", "deprecated": null, "synonyms": {"hasExactSynonym": [], "hasBroadSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": ["freshwater realm"]}, "parents": ["http://purl.obolibrary.org/obo/ENVO_00002030", "http://purl.obolibrary.org/obo/ENVO_01001789"]}, "ENVO:00000893": {"label": "xeric basin biome", "definition": "A biome which has little permanent surface water and a low relative abundance of springs.", "deprecated": null, "synonyms": {"hasExactSynonym": [], "hasBroadSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": []}, "parents": ["http://purl.obolibrary.org/obo/ENVO_00000873"]}} |
| BASE_QC | https://github.com/CultureBotAI/HabitatMech/actions/runs/38513776724 | supports | Fresh gh run view confirmed completed success on exact base 471f0b0b55721a1ba566525ae6e510dca644b892, with separate structured-contract and authoritative-QC steps successful. This verifies unchanged scientific inputs, not newly authored review files. Full QC was not rerun locally for these review-only additions. |
| TAXA | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;retmode=xml&amp;id=34,54,56,57,100,103,128,147,245,287,294,303,306,670,674,882,1026,1063,1270,1399,1724,1736,1833,1855,2047,13243,28034,28092,28115,28122,28251,29290,29346,29355,29539,32012,34073,36987,37919,39946,44576,45465,94122,102129,102232,103810,112248,114715,119641,120377,140314,158751,158899,180441,184914,186497,194373,196162,199684,204536,205918,210512,211457,211586,214688,215918,217068,218208,223390,231024,265072,265599,266940,267374,272624,298386,309807,312286,314282,326298,330214,335284,365044,379066,395960,395964,402880,406817,411485,419542,423350,428125,441153,456442,457427,469383,471857,474950,474952,475253,479432,484019,521011,523850,525898,547558,551760,589924,663321,675813,675814,714943,742013,798130,945550,1002689,1037355,1052844,1052848,1070866,1089549,1104584,1111733,1111735,1121085,1121122,1121266,1121278,1121291,1121362,1121398,1121451,1121480,1121484,1121884,1121885,1121928,1121929,1121943,1122124,1122133,1122603,1122612,1122920,1122922,1122928,1122946,1123061,1123487,1173263,1397695,1397698,1869227; Taxon and AkaTaxIds elements for the target associations | supports | Alias-aware official NCBI XML resolution; every nonempty stored name matches. An omitted optional label or a valid merged ID is not a broken reference. Identity verification does not independently validate occurrence or characteristic presence. SHA256 5d47d13bde7b62410a1a15a8818464cc3bb7bb1ba3c09a3e463c347b96b1a210. Results: [{"source_id": "NCBITaxon:112248", "stored_label": "Seinonella peptonophila", "current_id": "112248", "name": "Seinonella peptonophila", "rank": "species"}, {"source_id": "NCBITaxon:1399", "stored_label": "Cytobacillus firmus", "current_id": "1399", "name": "Cytobacillus firmus", "rank": "species"}, {"source_id": "NCBITaxon:194373", "stored_label": "uncultured Hyphomicrobium sp.", "current_id": "194373", "name": "uncultured Hyphomicrobium sp.", "rank": "species"}, {"source_id": "NCBITaxon:196162", "stored_label": "Nocardioides sp. JS614", "current_id": "196162", "name": "Nocardioides sp. JS614", "rank": "species"}, {"source_id": "NCBITaxon:199684", "stored_label": "uncultured Bradyrhizobium sp.", "current_id": "199684", "name": "uncultured Bradyrhizobium sp.", "rank": "species"}, {"source_id": "NCBITaxon:231024", "stored_label": "Streptomyces africanus", "current_id": "231024", "name": "Streptomyces africanus", "rank": "species"}, {"source_id": "NCBITaxon:266940", "stored_label": "Kineococcus radiotolerans SRS30216 = ATCC BAA-149", "current_id": "266940", "name": "Kineococcus radiotolerans SRS30216 = ATCC BAA-149", "rank": "strain"}, {"source_id": "NCBITaxon:28034", "stored_label": "Sulfobacillus thermosulfidooxidans", "current_id": "28034", "name": "Sulfobacillus thermosulfidooxidans", "rank": "species"}, {"source_id": "NCBITaxon:28115", "stored_label": "Porphyromonas macacae", "current_id": "28115", "name": "Porphyromonas macacae", "rank": "species"}, {"source_id": "NCBITaxon:29290", "stored_label": "Candidatus Magnetobacterium bavaricum", "current_id": "29290", "name": "Candidatus Magnetobacterium bavaricum", "rank": "species"}, {"source_id": "NCBITaxon:29346", "stored_label": "Alkalithermobacter thermoalcaliphilus", "current_id": "29346", "name": "Alkalithermobacter thermoalcaliphilus", "rank": "species"}, {"source_id": "NCBITaxon:29355", "stored_label": "Ruminiclostridium cellobioparum", "current_id": "29355", "name": "Ruminiclostridium cellobioparum", "rank": "species"}, {"source_id": "NCBITaxon:29539", "stored_label": "Thermoleophilum album", "current_id": "29539", "name": "Thermoleophilum album", "rank": "species"}, {"source_id": "NCBITaxon:330214", "stored_label": "Nitrospira defluvii", "current_id": "330214", "name": "Nitrospira defluvii", "rank": "species"}, {"source_id": "NCBITaxon:34073", "stored_label": "Variovorax paradoxus", "current_id": "34073", "name": "Variovorax paradoxus", "rank": "species"}, {"source_id": "NCBITaxon:36987", "stored_label": null, "current_id": "36987", "name": "Coptotermes formosanus", "rank": "species"}, {"source_id": "NCBITaxon:379066", "stored_label": "Gemmatimonas aurantiaca T-27", "current_id": "379066", "name": "Gemmatimonas aurantiaca T-27", "rank": "strain"}, {"source_id": "NCBITaxon:39946", "stored_label": null, "current_id": "39946", "name": "Oryza sativa Indica Group", "rank": "no rank"}, {"source_id": "NCBITaxon:411485", "stored_label": "Faecalibacterium prausnitzii M21/2", "current_id": "411485", "name": "Faecalibacterium prausnitzii M21/2", "rank": "strain"}, {"source_id": "NCBITaxon:428125", "stored_label": "[Clostridium] leptum DSM 753", "current_id": "428125", "name": "[Clostridium] leptum DSM 753", "rank": "strain"}, {"source_id": "NCBITaxon:44576", "stored_label": "Nitrosomonas halophila", "current_id": "44576", "name": "Nitrosomonas halophila", "rank": "species"}, {"source_id": "NCBITaxon:45465", "stored_label": "Vogesella indigofera", "current_id": "45465", "name": "Vogesella indigofera", "rank": "species"}, {"source_id": "NCBITaxon:457427", "stored_label": "Streptomyces himastatinicus ATCC 53653", "current_id": "457427", "name": "Streptomyces himastatinicus ATCC 53653", "rank": "strain"}, {"source_id": "NCBITaxon:469383", "stored_label": "Conexibacter woesei DSM 14684", "current_id": "469383", "name": "Conexibacter woesei DSM 14684", "rank": "strain"}, {"source_id": "NCBITaxon:479432", "stored_label": "Streptosporangium roseum DSM 43021", "current_id": "479432", "name": "Streptosporangium roseum DSM 43021", "rank": "strain"}] |
| XERIC | https://feow.org/ecoregions/list?page=13; Major Habitat Type column, ecoregions 436-450 | context_only | The official inventory includes xeric freshwaters and endorheic basins. It supports the aquatic classification context, not PREGO taxon occurrences. |

## Limits And Additional Notes

- Same-agent review, not independent approval or full-corpus certification.
- Original upstream sample/organism membership and study-to-sample crosswalks were not reconstructed. Frozen counters reproduce; public GOLD terminal paths do not verify every historical internal node or population.
- NCBI identity checks do not validate habitat occurrence. Configured native label checks retain five accepted exceptions and 2057 no-adapter skips.
- No browser visual QA, new local full-QC run, SSSOM/KGX conformance audit, source refresh, curation edit or scientific-status promotion was performed.
- Legacy reports are historical leads; changed old parent or rationale findings are compared with current maintained inputs, not silently assigned terminal structured dispositions. New bundles require their own native archive check after saving.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T053407Z-xeric_basin_biome
kind: record
repository: CultureBotAI/HabitatMech
title: 'Scientific record review: xeric basin biome'
started_at: '2026-10-14T05:19:09.200634Z'
finished_at: '2026-10-14T05:34:07.737887Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Same agent participated in repository work; this assessment
    is not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
scientific_review: true
verdict: pass_with_limitations
summary: The freshwater-biome identity is compatible with limited permanent surface
  water and must not be reclassified as terrestrial merely from xeric. The retained
  PREGO associations are source observations, not a characteristic microbial community.
source:
  git_revision: 471f0b0b55721a1ba566525ae6e510dca644b892
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
    sha256: c7017ce7889ebfce889eb6f2c6a6c12510428be4b8a4370e2e4e165231e1af25
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
  - path: data/habitats/aquatic/drinking_water.yaml
    sha256: 3f187464d080b31d6c5b32922d7ade01bb7e120c65b6f991f9211c7e25c88d2e
    role: context
  - path: data/habitats/aquatic/drinking_water__6d6ef579.yaml
    sha256: 821c4708dec6412d2654cd7066623c5574264f17660a57f78678961d86eb1df3
    role: context
  - path: data/habitats/aquatic/fresh_water.yaml
    sha256: 99bd93c6173c2ccf7b59645a131ae41c88c45246b45265034a8275053b3745b7
    role: context
  - path: data/habitats/aquatic/xeric_basin_biome.yaml
    sha256: 3bdcd3ca4db8e24c208fc5ba97d00a9f15be3addb3ff762ce082153dd0ba9676
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
  - path: history/mappings/white_smoker/2026-10-07T004938Z-codex-gpt-5-1b23b5.yaml
    sha256: dd111d6915e7705e37a7061658dd35bc8e3f1c7bde4120341b419b2cfff8ada0
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260926T075729Z-untreated.md
    sha256: 78c320708f6d125e4a6ef403cfefc2b5cd47d1c23725ec1e2035fe525b82fbff
    role: context
  - path: reports/yaml_record_review/20260926T082617Z-waste__ae37fc5e.md
    sha256: f924cb5fc215d62146f5d4a333ea1613809b77a4a245b5e60f0e659c2692d013
    role: context
  - path: reports/yaml_record_review/20261003T054751Z-waterfall.md
    sha256: db0b11e485718184fb679bb2e5f06d9899a027339ba8d60e5f966c98982bfdc2
    role: context
  - path: reports/yaml_record_review/20261006T182127Z-unchlorinated.md
    sha256: 1c9baf056eee034b5a89e8f736ce62fe08089e47d60e82dff7879b8acf6906b8
    role: context
  - path: reports/yaml_record_review/20261006T203103Z-volcanic.md
    sha256: 34a0a3918a8600afb53ce1d386c4f8984a86eabde4f1cd1aa4a5a24c7dabc878
    role: context
  - path: reports/yaml_record_review/20261006T212917Z-water_ice_core.md
    sha256: a18461295bfa7465dc5f8662bf0cfd57c0ef294c60d340098d38d51aaf5cf262
    role: context
  - path: reports/yaml_record_review/20261007T003619Z-white_smoker.md
    sha256: 7f818b371800d3cb0675b5a3cf2a19d9d2d3f5fe76f810e06c98b9c3d07ee331
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
targets:
- target_id: ENVO:00000893
  path: data/habitats/aquatic/xeric_basin_biome.yaml
  label: xeric basin biome
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Grounding and ITEM review
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Authored definition and genus
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Scoped context-parent exclusions
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Frozen ontology assertions
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_subclass_edges.tsv
    role: Frozen ontology hierarchy
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Source harmonization and generation
scope:
  description: One entire generated HabitatRecord and every contributing source concept.
    Parent records supply bounded hierarchy context only.
  selection: One of the 23 remaining aquatic targets lacking a completed individual
    scientific review in an ignored-independent census of 3208 current records.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - ENVO:00000893
checks:
- check_id: C0
  name: Native validate
  required: true
  status: passed
  target_ids:
  - ENVO:00000893
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/aquatic/xeric_basin_biome.yaml
  exit_code: 0
  summary: Actual successful execution from 2026-10-14T05:19:24.346861Z to 2026-10-14T05:19:26.875770Z.
    Record-specific or full-corpus command scope is explicit. Reproduction and validation
    are not scientific approval.
- check_id: C1
  name: Native validate-strict
  required: true
  status: passed
  target_ids:
  - ENVO:00000893
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/aquatic/tubeworm_bush.yaml data/habitats/aquatic/unchlorinated.yaml
    data/habitats/aquatic/underground_water.yaml data/habitats/aquatic/undersea_feature.yaml
    data/habitats/aquatic/untreated.yaml data/habitats/aquatic/urban_floodwater.yaml
    data/habitats/aquatic/vernal_pools__dc503f3c.yaml data/habitats/aquatic/volcanic.yaml
    data/habitats/aquatic/warm_34_42c.yaml data/habitats/aquatic/waste__ae37fc5e.yaml
    data/habitats/aquatic/water_body.yaml data/habitats/aquatic/water_ice_core.yaml
    data/habitats/aquatic/water_tank.yaml data/habitats/aquatic/watercourse.yaml data/habitats/aquatic/waterfall.yaml
    data/habitats/aquatic/well.yaml data/habitats/aquatic/well_biofilm.yaml data/habitats/aquatic/well_sediment.yaml
    data/habitats/aquatic/wetland_area.yaml data/habitats/aquatic/whale_fall.yaml
    data/habitats/aquatic/white_smoker.yaml data/habitats/aquatic/wood_fall.yaml data/habitats/aquatic/xeric_basin_biome.yaml
  exit_code: 0
  summary: Actual successful execution from 2026-10-14T05:19:26.876441Z to 2026-10-14T05:19:35.258415Z.
    Record-specific or full-corpus command scope is explicit. Reproduction and validation
    are not scientific approval.
- check_id: C2
  name: Native validate-history
  required: true
  status: passed
  target_ids:
  - ENVO:00000893
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  summary: Actual successful execution from 2026-10-14T05:19:35.259097Z to 2026-10-14T05:19:43.590897Z.
    Record-specific or full-corpus command scope is explicit. Reproduction and validation
    are not scientific approval.
- check_id: C3
  name: Native provenance-check
  required: true
  status: passed
  target_ids:
  - ENVO:00000893
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  summary: Actual successful execution from 2026-10-14T05:19:43.591669Z to 2026-10-14T05:19:44.179190Z.
    Record-specific or full-corpus command scope is explicit. Reproduction and validation
    are not scientific approval.
- check_id: C4
  name: Native verify-corpus
  required: true
  status: passed
  target_ids:
  - ENVO:00000893
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  summary: Actual successful execution from 2026-10-14T05:19:44.179802Z to 2026-10-14T05:19:59.207478Z.
    Record-specific or full-corpus command scope is explicit. Reproduction and validation
    are not scientific approval.
- check_id: C5
  name: Native validate-causal-all
  required: true
  status: passed
  target_ids:
  - ENVO:00000893
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  summary: Actual successful execution from 2026-10-14T05:19:59.208144Z to 2026-10-14T05:20:03.719611Z.
    Record-specific or full-corpus command scope is explicit. Reproduction and validation
    are not scientific approval.
- check_id: C6
  name: Native term-requests-check
  required: true
  status: passed
  target_ids:
  - ENVO:00000893
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  summary: Actual successful execution from 2026-10-14T05:20:03.720302Z to 2026-10-14T05:20:23.391843Z.
    Record-specific or full-corpus command scope is explicit. Reproduction and validation
    are not scientific approval.
- check_id: C7
  name: Native validate-products
  required: true
  status: passed
  target_ids:
  - ENVO:00000893
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  summary: 'Actual successful execution from 2026-10-14T05:20:23.392546Z to 2026-10-14T05:21:30.920465Z.
    Record-specific or full-corpus command scope is explicit. Label gate: 1178 canonical,
    one synonym, five accepted exceptions and 2057 configured no-adapter skips; no
    taxon occurrence validation.'
- check_id: REPRO
  name: Complete document reproduction and input hash recheck
  required: true
  status: passed
  target_ids:
  - ENVO:00000893
  command: .venv/bin/python /private/tmp/habitatmech-review-bl.py crosscheck
  exit_code: 0
  summary: Native build_corpus/build_document equality for all 23 complete target
    documents and captured-input hash equality passed; draft preparation rechecks
    all extended captures.
- check_id: QC
  name: Exact-base hosted authoritative QC
  required: true
  status: passed
  target_ids:
  - ENVO:00000893
  command: gh run view 38513776724 --json headSha,conclusion,status,url,jobs
  exit_code: 0
  evidence_ids:
  - BASE_QC
  summary: Successful hosted checks cover the exact unchanged scientific-input base,
    not these new bundles or a newly executed local full QC.
- check_id: IMOD
  name: Expression-module adapter
  required: false
  status: not_applicable
  target_ids:
  - ENVO:00000893
  summary: No gene, regulator, protein or transcriptomic-module assertion occurs in
    this target. iModulonDB non-use is not evidence of biological absence.
evidence:
- evidence_id: RECORD
  kind: record_content
  reference: data/habitats/aquatic/xeric_basin_biome.yaml
  accessed_at: '2026-10-14T05:34:07.737501Z'
  support: supports
  summary: The entire target was read before judgment, including all attestations,
    associations and generated events. Complete parsed-document reproduction and captured
    hash checks passed. The freshwater-biome identity is compatible with limited permanent
    surface water and must not be reclassified as terrestrial merely from xeric. The
    retained PREGO associations are source observations, not a characteristic microbial
    community.
- evidence_id: RAW
  kind: record_content
  reference: data/raw/prego_habitat_taxa.tsv:5288,5289,5290,5291,5292,5293,5294,5295,5296,5297,5298,5299,5300,5301,5302,5303,5304,5305,5306,5307,5308,5309,5310,5311,5312;
    data/raw/prego_habitats.tsv:247; data/raw/ontology_subclass_edges.tsv:5247,5248,5255;
    data/raw/ontology_terms.tsv:7146,7153
  accessed_at: '2026-10-14T05:34:07.737501Z'
  support: supports
  summary: 'Locators are logical TSV records counted with header as row 1. Structured
    scans and native document reproduction verify the emitted source paths, collapsed-node
    notes, count units, score channels, displayed association ranking and historical
    events. The source inventory is not independent experimental evidence. Exact emitted
    attestations: [{"source": "PREGO", "source_id": "ENVO:00000893", "source_label":
    "xeric basin biome", "assertion_count": 36, "assertion_unit": "TAXON", "score":
    4.0, "evidence_channels": "environmental_samples"}]'
- evidence_id: RULES
  kind: record_content
  reference: docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; docs/record-review-profile.md;
    .claude/skills/curate-yaml-record/references/review-checklist.md
  accessed_at: '2026-10-14T05:34:07.737501Z'
  support: supports
  summary: Applied habitat identity, strict genus, typed synonym, MIxS-role, source-unit,
    taxon-association and lifecycle rules. Optional missing fields are not automatically
    defects. Scientific review does not create ITEM decisions or promote native status.
- evidence_id: OWNERS
  kind: record_content
  reference: curation/decisions.tsv; curation/gold_parent_exclusions.tsv; curation/term_requests.tsv;
    src/habitatmech/seed.py; src/habitatmech/extract.py; src/habitatmech/schema/habitatmech.yaml
  accessed_at: '2026-10-14T05:34:07.737501Z'
  support: supports
  summary: Read contributing maintained rows and source construction. The schema defines
    strictly broader parent_habitats and a source-to-record mapping predicate. Ontology
    ingestion retains an untyped synonym pipe; ConceptStore.get assigns exact scope
    to ontology aliases. Guarded GOLD exclusions remove only named source contributions.
    Source lifecycle requires every contributing source to have ITEM review before
    REVIEWED is emitted.
- evidence_id: SEARCH
  kind: record_content
  reference: curation; history; research; conf; reviews/structured; reports/yaml_record_review;
    data/raw
  accessed_at: '2026-10-14T05:18:08.578668Z'
  support: supports
  summary: Bounded rg --no-ignore --hidden searches included ignored and hidden files
    and exact identifier, source IDs/mints, label and slug. Structured TSV scans and
    the recursive review census also ignore no files. No structured finding affecting
    these target IDs was found in the 1343-bundle census; legacy reports are historical
    leads, not successor-disposition lineage. Original sample membership was not reconstructed;
    no whole-filesystem absence is claimed.
- evidence_id: ENVO
  kind: database
  reference: https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl
  locator: Named classes ENVO:00000873, ENVO:00000893
  accessed_at: '2026-10-14T05:18:11.169812Z'
  support: supports
  summary: 'Official current file commit a2455d1a77e46bb8a664d65a157166b539269042,
    SHA256 a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c. Inspected
    definitions, named parents, deprecated flags and typed synonyms. Target/genus
    classes are active; historical triad annotations are checked separately, not silently
    promoted to current record assertions: {"ENVO:00000873": {"label": "freshwater
    biome", "definition": "An aquatic biome which is determined by a body of freshwater.",
    "deprecated": null, "synonyms": {"hasExactSynonym": [], "hasBroadSynonym": [],
    "hasNarrowSynonym": [], "hasRelatedSynonym": ["freshwater realm"]}, "parents":
    ["http://purl.obolibrary.org/obo/ENVO_00002030", "http://purl.obolibrary.org/obo/ENVO_01001789"]},
    "ENVO:00000893": {"label": "xeric basin biome", "definition": "A biome which has
    little permanent surface water and a low relative abundance of springs.", "deprecated":
    null, "synonyms": {"hasExactSynonym": [], "hasBroadSynonym": [], "hasNarrowSynonym":
    [], "hasRelatedSynonym": []}, "parents": ["http://purl.obolibrary.org/obo/ENVO_00000873"]}}'
- evidence_id: BASE_QC
  kind: record_content
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38513776724
  accessed_at: '2026-10-14T05:34:07.737501Z'
  support: supports
  summary: Fresh gh run view confirmed completed success on exact base 471f0b0b55721a1ba566525ae6e510dca644b892,
    with separate structured-contract and authoritative-QC steps successful. This
    verifies unchanged scientific inputs, not newly authored review files. Full QC
    was not rerun locally for these review-only additions.
- evidence_id: TAXA
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&retmode=xml&id=34,54,56,57,100,103,128,147,245,287,294,303,306,670,674,882,1026,1063,1270,1399,1724,1736,1833,1855,2047,13243,28034,28092,28115,28122,28251,29290,29346,29355,29539,32012,34073,36987,37919,39946,44576,45465,94122,102129,102232,103810,112248,114715,119641,120377,140314,158751,158899,180441,184914,186497,194373,196162,199684,204536,205918,210512,211457,211586,214688,215918,217068,218208,223390,231024,265072,265599,266940,267374,272624,298386,309807,312286,314282,326298,330214,335284,365044,379066,395960,395964,402880,406817,411485,419542,423350,428125,441153,456442,457427,469383,471857,474950,474952,475253,479432,484019,521011,523850,525898,547558,551760,589924,663321,675813,675814,714943,742013,798130,945550,1002689,1037355,1052844,1052848,1070866,1089549,1104584,1111733,1111735,1121085,1121122,1121266,1121278,1121291,1121362,1121398,1121451,1121480,1121484,1121884,1121885,1121928,1121929,1121943,1122124,1122133,1122603,1122612,1122920,1122922,1122928,1122946,1123061,1123487,1173263,1397695,1397698,1869227
  accessed_at: '2026-10-14T05:18:13.506822Z'
  locator: Taxon and AkaTaxIds elements for the target associations
  support: supports
  summary: 'Alias-aware official NCBI XML resolution; every nonempty stored name matches.
    An omitted optional label or a valid merged ID is not a broken reference. Identity
    verification does not independently validate occurrence or characteristic presence.
    SHA256 5d47d13bde7b62410a1a15a8818464cc3bb7bb1ba3c09a3e463c347b96b1a210. Results:
    [{"source_id": "NCBITaxon:112248", "stored_label": "Seinonella peptonophila",
    "current_id": "112248", "name": "Seinonella peptonophila", "rank": "species"},
    {"source_id": "NCBITaxon:1399", "stored_label": "Cytobacillus firmus", "current_id":
    "1399", "name": "Cytobacillus firmus", "rank": "species"}, {"source_id": "NCBITaxon:194373",
    "stored_label": "uncultured Hyphomicrobium sp.", "current_id": "194373", "name":
    "uncultured Hyphomicrobium sp.", "rank": "species"}, {"source_id": "NCBITaxon:196162",
    "stored_label": "Nocardioides sp. JS614", "current_id": "196162", "name": "Nocardioides
    sp. JS614", "rank": "species"}, {"source_id": "NCBITaxon:199684", "stored_label":
    "uncultured Bradyrhizobium sp.", "current_id": "199684", "name": "uncultured Bradyrhizobium
    sp.", "rank": "species"}, {"source_id": "NCBITaxon:231024", "stored_label": "Streptomyces
    africanus", "current_id": "231024", "name": "Streptomyces africanus", "rank":
    "species"}, {"source_id": "NCBITaxon:266940", "stored_label": "Kineococcus radiotolerans
    SRS30216 = ATCC BAA-149", "current_id": "266940", "name": "Kineococcus radiotolerans
    SRS30216 = ATCC BAA-149", "rank": "strain"}, {"source_id": "NCBITaxon:28034",
    "stored_label": "Sulfobacillus thermosulfidooxidans", "current_id": "28034", "name":
    "Sulfobacillus thermosulfidooxidans", "rank": "species"}, {"source_id": "NCBITaxon:28115",
    "stored_label": "Porphyromonas macacae", "current_id": "28115", "name": "Porphyromonas
    macacae", "rank": "species"}, {"source_id": "NCBITaxon:29290", "stored_label":
    "Candidatus Magnetobacterium bavaricum", "current_id": "29290", "name": "Candidatus
    Magnetobacterium bavaricum", "rank": "species"}, {"source_id": "NCBITaxon:29346",
    "stored_label": "Alkalithermobacter thermoalcaliphilus", "current_id": "29346",
    "name": "Alkalithermobacter thermoalcaliphilus", "rank": "species"}, {"source_id":
    "NCBITaxon:29355", "stored_label": "Ruminiclostridium cellobioparum", "current_id":
    "29355", "name": "Ruminiclostridium cellobioparum", "rank": "species"}, {"source_id":
    "NCBITaxon:29539", "stored_label": "Thermoleophilum album", "current_id": "29539",
    "name": "Thermoleophilum album", "rank": "species"}, {"source_id": "NCBITaxon:330214",
    "stored_label": "Nitrospira defluvii", "current_id": "330214", "name": "Nitrospira
    defluvii", "rank": "species"}, {"source_id": "NCBITaxon:34073", "stored_label":
    "Variovorax paradoxus", "current_id": "34073", "name": "Variovorax paradoxus",
    "rank": "species"}, {"source_id": "NCBITaxon:36987", "stored_label": null, "current_id":
    "36987", "name": "Coptotermes formosanus", "rank": "species"}, {"source_id": "NCBITaxon:379066",
    "stored_label": "Gemmatimonas aurantiaca T-27", "current_id": "379066", "name":
    "Gemmatimonas aurantiaca T-27", "rank": "strain"}, {"source_id": "NCBITaxon:39946",
    "stored_label": null, "current_id": "39946", "name": "Oryza sativa Indica Group",
    "rank": "no rank"}, {"source_id": "NCBITaxon:411485", "stored_label": "Faecalibacterium
    prausnitzii M21/2", "current_id": "411485", "name": "Faecalibacterium prausnitzii
    M21/2", "rank": "strain"}, {"source_id": "NCBITaxon:428125", "stored_label": "[Clostridium]
    leptum DSM 753", "current_id": "428125", "name": "[Clostridium] leptum DSM 753",
    "rank": "strain"}, {"source_id": "NCBITaxon:44576", "stored_label": "Nitrosomonas
    halophila", "current_id": "44576", "name": "Nitrosomonas halophila", "rank": "species"},
    {"source_id": "NCBITaxon:45465", "stored_label": "Vogesella indigofera", "current_id":
    "45465", "name": "Vogesella indigofera", "rank": "species"}, {"source_id": "NCBITaxon:457427",
    "stored_label": "Streptomyces himastatinicus ATCC 53653", "current_id": "457427",
    "name": "Streptomyces himastatinicus ATCC 53653", "rank": "strain"}, {"source_id":
    "NCBITaxon:469383", "stored_label": "Conexibacter woesei DSM 14684", "current_id":
    "469383", "name": "Conexibacter woesei DSM 14684", "rank": "strain"}, {"source_id":
    "NCBITaxon:479432", "stored_label": "Streptosporangium roseum DSM 43021", "current_id":
    "479432", "name": "Streptosporangium roseum DSM 43021", "rank": "strain"}]'
- evidence_id: XERIC
  kind: database
  reference: https://feow.org/ecoregions/list?page=13
  locator: Major Habitat Type column, ecoregions 436-450
  accessed_at: '2026-10-14T05:34:07.737501Z'
  support: context_only
  summary: The official inventory includes xeric freshwaters and endorheic basins.
    It supports the aquatic classification context, not PREGO taxon occurrences.
assessments:
- assessment_id: IDENTITY
  area: identity
  topic: Entity, grounding, strict hierarchy and source scope
  outcome: supported
  target_ids:
  - ENVO:00000893
  evidence_ids:
  - RECORD
  - ENVO
  - RAW
  - OWNERS
  - RULES
  - XERIC
  summary: ENVO:00000893 describes little permanent surface water and relatively few
    springs, with ENVO:00000873 freshwater biome as genus. Official FEOW listings
    include xeric freshwaters and endorheic basins, supporting the aquatic scope rather
    than a generic desert identity. The two PREGO alternate spellings remain related;
    no ENVO synonym is asserted.
- assessment_id: SCIENCE
  area: evidence
  topic: Claim-level scientific support, taxa, MIxS and source-unit limits
  outcome: supported
  target_ids:
  - ENVO:00000893
  evidence_ids:
  - RECORD
  - RAW
  - ENVO
  - XERIC
  - TAXA
  summary: PREGO row 247 has 36 TAXON/direct assertions, score 4 and environmental_samples;
    25 ranked rows are retained. All nonempty labels resolve. The two omitted labels
    resolve to Coptotermes formosanus (36987, species) and Oryza sativa Indica Group
    (39946, no rank). The dataset includes nonmicrobial taxa and ranks; source associations
    do not assert microbial-only or is_characteristic status. Their original environmental-sample
    occurrences were not reconstructed, and no drought tolerance is inferred from
    membership.
- assessment_id: STATUS
  area: provenance
  topic: Generated status, history and optional-field completeness
  outcome: supported
  target_ids:
  - ENVO:00000893
  evidence_ids:
  - RECORD
  - RAW
  - OWNERS
  - SEARCH
  summary: The complete record reproduces from maintained inputs, including EXACT/SEEDED,
    all source attestations and 1 historical events. REVIEWED requires all contributing
    ITEM decisions; CLASS decisions remain seeded. No review is a status promotion.
    The target asserts no causal graph or environmental-parameter block; source triads
    and external examples are not promoted into these optional slots.
findings: []
actions: []
limitations:
- Same-agent review, not independent approval or full-corpus certification.
- Original upstream sample/organism membership and study-to-sample crosswalks were
  not reconstructed. Frozen counters reproduce; public GOLD terminal paths do not
  verify every historical internal node or population.
- NCBI identity checks do not validate habitat occurrence. Configured native label
  checks retain five accepted exceptions and 2057 no-adapter skips.
- No browser visual QA, new local full-QC run, SSSOM/KGX conformance audit, source
  refresh, curation edit or scientific-status promotion was performed.
- Legacy reports are historical leads; changed old parent or rationale findings are
  compared with current maintained inputs, not silently assigned terminal structured
  dispositions. New bundles require their own native archive check after saving.
tags:
- habitatmech
- record-review
- aquatic
```
