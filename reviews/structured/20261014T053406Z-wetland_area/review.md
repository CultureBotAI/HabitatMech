# Scientific record review: wetland area

- Review: 20261014T053406Z-wetland_area
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-14T05:18:56.544848Z
- Finished UTC: 2026-10-14T05:34:06.025546Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The corrected vegetated-area hierarchy and four-source review lifecycle reproduce. WetlandRegion is related in ENVO but emitted as exact. Qualified GOLD source equivalence and original PREGO occurrence keys remain limitations.

## Scope And Provenance

One entire generated HabitatRecord and every contributing source concept. Parent records supply bounded hierarchy context only.

Selection: One of the 23 remaining aquatic targets lacking a completed individual scientific review in an ignored-independent census of 3208 current records.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 471f0b0b55721a1ba566525ae6e510dca644b892.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| ENVO:00000043 | data/habitats/aquatic/wetland_area.yaml | generated | wetland area |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native validate | passed | True | ENVO:00000043 | Actual successful execution from 2026-10-14T05:19:14.243705Z to 2026-10-14T05:19:17.056462Z. Record-specific or full-corpus command scope is explicit. Reproduction and validation are not scientific approval. |
| Native validate-strict | passed | True | ENVO:00000043 | Actual successful execution from 2026-10-14T05:19:26.876441Z to 2026-10-14T05:19:35.258415Z. Record-specific or full-corpus command scope is explicit. Reproduction and validation are not scientific approval. |
| Native validate-history | passed | True | ENVO:00000043 | Actual successful execution from 2026-10-14T05:19:35.259097Z to 2026-10-14T05:19:43.590897Z. Record-specific or full-corpus command scope is explicit. Reproduction and validation are not scientific approval. |
| Native provenance-check | passed | True | ENVO:00000043 | Actual successful execution from 2026-10-14T05:19:43.591669Z to 2026-10-14T05:19:44.179190Z. Record-specific or full-corpus command scope is explicit. Reproduction and validation are not scientific approval. |
| Native verify-corpus | passed | True | ENVO:00000043 | Actual successful execution from 2026-10-14T05:19:44.179802Z to 2026-10-14T05:19:59.207478Z. Record-specific or full-corpus command scope is explicit. Reproduction and validation are not scientific approval. |
| Native validate-causal-all | passed | True | ENVO:00000043 | Actual successful execution from 2026-10-14T05:19:59.208144Z to 2026-10-14T05:20:03.719611Z. Record-specific or full-corpus command scope is explicit. Reproduction and validation are not scientific approval. |
| Native term-requests-check | passed | True | ENVO:00000043 | Actual successful execution from 2026-10-14T05:20:03.720302Z to 2026-10-14T05:20:23.391843Z. Record-specific or full-corpus command scope is explicit. Reproduction and validation are not scientific approval. |
| Native validate-products | passed | True | ENVO:00000043 | Actual successful execution from 2026-10-14T05:20:23.392546Z to 2026-10-14T05:21:30.920465Z. Record-specific or full-corpus command scope is explicit. Label gate: 1178 canonical, one synonym, five accepted exceptions and 2057 configured no-adapter skips; no taxon occurrence validation. |
| Complete document reproduction and input hash recheck | passed | True | ENVO:00000043 | Native build_corpus/build_document equality for all 23 complete target documents and captured-input hash equality passed; draft preparation rechecks all extended captures. |
| Exact-base hosted authoritative QC | passed | True | ENVO:00000043 | Successful hosted checks cover the exact unchanged scientific-input base, not these new bundles or a newly executed local full QC. |
| Expression-module adapter | not_applicable | False | ENVO:00000043 | No gene, regulator, protein or transcriptomic-module assertion occurs in this target. iModulonDB non-use is not evidence of biological absence. |

## Scientific And Domain Assessments

### Entity, grounding, strict hierarchy and source scope

identity: supported. Targets: ENVO:00000043.

ENVO:00000043 is a vegetated area overlapping a wetland ecosystem, with ENVO:01001305 as its genus. Exclusions 137-139 already remove soil, whole marine water body and fresh-water material. Four ITEM decisions explain REVIEWED, but the generic wetland definition does not independently establish exact equivalence of freshwater, marine and soil-qualified source extensions. Retain each path and this limitation rather than declaring the prefixes immaterial. GOLD Wetlands has independent source provenance; ENVO WetlandRegion must be related.

### Claim-level scientific support, taxa, MIxS and source-unit limits

evidence: supported. Targets: ENVO:00000043.

The three GOLD paths retain 3, 61 and 29 ORGANISM assertions separately. PREGO row 223 has 50 TAXON, 63 direct assertions, score 4 and 25 retained associations; distinct taxa must not be conflated with direct assertions. Bulk marine/freshwater/soil counts are 115/75/793, while complete-triad populations are 5/22/316. Forty-eight study rows are path memberships, not 48 independent experiments. Modal ecosystem, wetland and material terms serve different roles. EPA supports the area-versus-water/soil distinction, not every merged-source equivalence.

### Generated status, history and optional-field completeness

provenance: supported. Targets: ENVO:00000043.

The complete record reproduces from maintained inputs, including EXACT/REVIEWED, all source attestations and 8 historical events. REVIEWED requires all contributing ITEM decisions; CLASS decisions remain seeded. No review is a status promotion. The target asserts no causal graph or environmental-parameter block; source triads and external examples are not promoted into these optional slots.

### Non-exact ontology synonyms are emitted as exact

grounding: concern. Targets: ENVO:00000043.

Current official ENVO types these aliases non-exact: {"hasRelatedSynonym": ["WetlandRegion"]}. The generated record emits each as EXACT_SYNONYM. The frozen ontology_terms pipe loses scope and ConceptStore.get promotes all ontology aliases to exact. Source-label repairs do not fix this ontology-source defect. Preserve genuine exact assertions and multiple scopes when supplied.

## Findings

### F1: Non-exact ontology synonyms are emitted as exact

major / open / confirmed; issue key: envo-00000043-synonym-scope.

Current official ENVO types these aliases non-exact: {"hasRelatedSynonym": ["WetlandRegion"]}. The generated record emits each as EXACT_SYNONYM. The frozen ontology_terms pipe loses scope and ConceptStore.get promotes all ontology aliases to exact. Source-label repairs do not fix this ontology-source defect. Preserve genuine exact assertions and multiple scopes when supplied.

## Recommended Actions And Acceptance Checks

### A1

Preserve typed synonym assertions through governed upstream extraction, the ontology inventory contract and generation. Test exact, broad, narrow, related, mixed-source and multiple-scope cases. Regenerate from real source provenance without checksum patches or a global downgrade.

- Address the exact evidence and source contribution described in F1; preserve independent valid parents, source IDs, paths, count units and historical events.
- Use maintained owners, append required curation history, inspect an exact canary, and pass schema, labels, provenance, reproduction, term requests, generated site and full QC. Rebuild genuinely affected semantic products.
- Do not edit generated YAML or immutable reviews. Any later disposition needs a new review retaining this issue key and exact previous occurrence; publication alone does not resolve it.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| RECORD | data/habitats/aquatic/wetland_area.yaml | supports | The entire target was read before judgment, including all attestations, associations and generated events. Complete parsed-document reproduction and captured hash checks passed. The corrected vegetated-area hierarchy and four-source review lifecycle reproduce. WetlandRegion is related in ENVO but emitted as exact. Qualified GOLD source equivalence and original PREGO occurrence keys remain limitations. |
| RAW | data/raw/gold_ecosystem_paths.tsv:276,359,718; data/raw/prego_habitat_taxa.tsv:3438,3439,3440,3441,3442,3443,3444,3445,3446,3447,3448,3449,3450,3451,3452,3453,3454,3455,3456,3457,3458,3459,3460,3461,3462; data/raw/prego_habitats.tsv:223; data/raw/gold_path_triads.tsv:416,417,418,680,681,682,1211,1212,1213; data/raw/gold_path_biosamples.tsv:44,212,283; data/raw/gold_studies.tsv:165,474,525,542,591,626,685,827,859,887,1003,1151,1177,1331,1527,1821,1876,1976,2163,2165,2167,2168,2219,2288,2306,2443,2498,2869,3004,3327,3335,3504,3564,3565,3864,4086,4142,4200,4260,4322,4328,4390,4407,4441,4491,4555,4570,4584; data/raw/ontology_subclass_edges.tsv:4673,7153; data/raw/ontology_terms.tsv:6633,8793; curation/gold_parent_exclusions.tsv:137,138,139; curation/decisions.tsv:588,852,967,1504 | supports | Locators are logical TSV records counted with header as row 1. Structured scans and native document reproduction verify the emitted source paths, collapsed-node notes, count units, score channels, displayed association ranking and historical events. The source inventory is not independent experimental evidence. Exact emitted attestations: [{"source": "GOLD", "source_id": "gold.ecosystem:3783", "source_label": "Wetlands", "source_path": "Environmental &gt; Aquatic &gt; Marine &gt; Wetlands", "mapping_predicate": "skos:exactMatch", "assertion_count": 3, "assertion_unit": "ORGANISM", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}, {"source": "GOLD", "source_id": "gold.ecosystem:3795", "source_label": "Wetlands", "source_path": "Environmental &gt; Aquatic &gt; Freshwater &gt; Wetlands", "mapping_predicate": "skos:exactMatch", "assertion_count": 61, "assertion_unit": "ORGANISM", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}, {"source": "GOLD", "source_id": "gold.ecosystem:3815", "source_label": "Wetlands", "source_path": "Environmental &gt; Terrestrial &gt; Soil &gt; Wetlands", "mapping_predicate": "skos:exactMatch", "assertion_count": 29, "assertion_unit": "ORGANISM", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}, {"source": "PREGO", "source_id": "ENVO:00000043", "source_label": "wetland area", "assertion_count": 50, "assertion_unit": "TAXON", "score": 4.0, "evidence_channels": "annotated_genomes_isolates"}] |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; docs/record-review-profile.md; .claude/skills/curate-yaml-record/references/review-checklist.md | supports | Applied habitat identity, strict genus, typed synonym, MIxS-role, source-unit, taxon-association and lifecycle rules. Optional missing fields are not automatically defects. Scientific review does not create ITEM decisions or promote native status. |
| OWNERS | curation/decisions.tsv; curation/gold_parent_exclusions.tsv; curation/term_requests.tsv; src/habitatmech/seed.py; src/habitatmech/extract.py; src/habitatmech/schema/habitatmech.yaml | supports | Read contributing maintained rows and source construction. The schema defines strictly broader parent_habitats and a source-to-record mapping predicate. Ontology ingestion retains an untyped synonym pipe; ConceptStore.get assigns exact scope to ontology aliases. Guarded GOLD exclusions remove only named source contributions. Source lifecycle requires every contributing source to have ITEM review before REVIEWED is emitted. |
| SEARCH | curation; history; research; conf; reviews/structured; reports/yaml_record_review; data/raw | supports | Bounded rg --no-ignore --hidden searches included ignored and hidden files and exact identifier, source IDs/mints, label and slug. Structured TSV scans and the recursive review census also ignore no files. No structured finding affecting these target IDs was found in the 1343-bundle census; legacy reports are historical leads, not successor-disposition lineage. Original sample membership was not reconstructed; no whole-filesystem absence is claimed. |
| ENVO | https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl; Named classes ENVO:00000043, ENVO:00000446, ENVO:00000447, ENVO:00001998, ENVO:00001999, ENVO:00002007, ENVO:00002011, ENVO:00002030, ENVO:01001305 | supports | Official current file commit a2455d1a77e46bb8a664d65a157166b539269042, SHA256 a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c. Inspected definitions, named parents, deprecated flags and typed synonyms. Target/genus classes are active; historical triad annotations are checked separately, not silently promoted to current record assertions: {"ENVO:00000043": {"label": "wetland area", "definition": "An vegetated area which overlaps a wetland ecosystem.", "deprecated": null, "synonyms": {"hasExactSynonym": [], "hasBroadSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": ["WetlandRegion"]}, "parents": ["http://purl.obolibrary.org/obo/ENVO_01001305"]}, "ENVO:00000446": {"label": "terrestrial biome", "definition": "A biome which is  primarily or completely situated on a landmass.", "deprecated": null, "synonyms": {"hasExactSynonym": [], "hasBroadSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": ["terrestrial realm"]}, "parents": ["http://purl.obolibrary.org/obo/ENVO_00000428", "http://purl.obolibrary.org/obo/ENVO_01001790"]}, "ENVO:00000447": {"label": "marine biome", "definition": "An aquatic biome which is determined by a marine water body.", "deprecated": null, "synonyms": {"hasExactSynonym": [], "hasBroadSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": ["marine realm"]}, "parents": ["http://purl.obolibrary.org/obo/ENVO_00002030", "http://purl.obolibrary.org/obo/ENVO_01001788"]}, "ENVO:00001998": {"label": "soil", "definition": "An environmental material which is primarily composed of minerals, varying proportions of sand, silt, and clay, organic material such as humus, interstitial gases, liquids, and a broad range of resident micro- and macroorganisms.", "deprecated": null, "synonyms": {"hasExactSynonym": [], "hasBroadSynonym": ["regolith"], "hasNarrowSynonym": [], "hasRelatedSynonym": []}, "parents": ["http://purl.obolibrary.org/obo/ENVO_00010483", "http://purl.obolibrary.org/obo/ENVO_01000813"]}, "ENVO:00001999": {"label": "marine water body", "definition": "A lentic water body which is composed primarily of marine water.", "deprecated": null, "synonyms": {"hasExactSynonym": ["body of marine water", "marine waterbody"], "hasBroadSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": []}, "parents": ["http://purl.obolibrary.org/obo/ENVO_01000617"]}, "ENVO:00002007": {"label": "sediment", "definition": "Particulate environmental material which is formed as a result of the transport and deposition of particles by flowing liquid.", "deprecated": null, "synonyms": {"hasExactSynonym": [], "hasBroadSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": []}, "parents": ["http://purl.obolibrary.org/obo/ENVO_01000060"]}, "ENVO:00002011": {"label": "fresh water", "definition": "Water which has a low concentration of dissolved solutes, particularly that of sodium chloride.", "deprecated": null, "synonyms": {"hasExactSynonym": ["freshwater"], "hasBroadSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": ["sweet water"]}, "parents": ["http://purl.obolibrary.org/obo/ENVO_00002006"]}, "ENVO:00002030": {"label": "aquatic biome", "definition": "A biome which is determined by a water body and which has ecological climax communities adapted to life in or on water.", "deprecated": null, "synonyms": {"hasExactSynonym": [], "hasBroadSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": []}, "parents": ["http://purl.obolibrary.org/obo/ENVO_00000428", "http://purl.obolibrary.org/obo/ENVO_01001787"]}, "ENVO:01001305": {"label": "vegetated area", "definition": "A vegetated area is a geographic feature which has ground cover dominated by plant communities.", "deprecated": null, "synonyms": {"hasExactSynonym": [], "hasBroadSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": []}, "parents": ["http://purl.obolibrary.org/obo/ENVO_01001199"]}} |
| BASE_QC | https://github.com/CultureBotAI/HabitatMech/actions/runs/38513776724 | supports | Fresh gh run view confirmed completed success on exact base 471f0b0b55721a1ba566525ae6e510dca644b892, with separate structured-contract and authoritative-QC steps successful. This verifies unchanged scientific inputs, not newly authored review files. Full QC was not rerun locally for these review-only additions. |
| GOLD | https://gold.jgi.doe.gov/download?mode=ecosystempaths; Workbook rows 666, 808, 1153 | supports | The complete public workbook has 2422 rows including its header; incorrect worksheet dimensions were reset before reading. SHA256 f13652be516a0f1482bf0abbb44d7d8e9acb17c5d401cd7e0474af949b447611. Exact matching vocabulary rows: [{"row": 666, "values": ["4181", "Environmental", "Aquatic", "Freshwater", "Wetlands", "Unclassified"]}, {"row": 808, "values": ["4055", "Environmental", "Aquatic", "Marine", "Wetlands", "Unclassified"]}, {"row": 1153, "values": ["4235", "Environmental", "Terrestrial", "Soil", "Wetlands", "Unclassified"]}]. Terminal vocabulary rows do not verify every historical internal node or original sample population. |
| GOLD_SCOPE | https://gold.jgi.doe.gov/ecosystem_classification; Classification purpose and five-level descriptions | context_only | The sample-driven classification describes collection surroundings. A path edge is not automatically a strict ontology subclass, and study membership does not establish every sample's habitat. |
| TAXA | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;retmode=xml&amp;id=34,54,56,57,100,103,128,147,245,287,294,303,306,670,674,882,1026,1063,1270,1399,1724,1736,1833,1855,2047,13243,28034,28092,28115,28122,28251,29290,29346,29355,29539,32012,34073,36987,37919,39946,44576,45465,94122,102129,102232,103810,112248,114715,119641,120377,140314,158751,158899,180441,184914,186497,194373,196162,199684,204536,205918,210512,211457,211586,214688,215918,217068,218208,223390,231024,265072,265599,266940,267374,272624,298386,309807,312286,314282,326298,330214,335284,365044,379066,395960,395964,402880,406817,411485,419542,423350,428125,441153,456442,457427,469383,471857,474950,474952,475253,479432,484019,521011,523850,525898,547558,551760,589924,663321,675813,675814,714943,742013,798130,945550,1002689,1037355,1052844,1052848,1070866,1089549,1104584,1111733,1111735,1121085,1121122,1121266,1121278,1121291,1121362,1121398,1121451,1121480,1121484,1121884,1121885,1121928,1121929,1121943,1122124,1122133,1122603,1122612,1122920,1122922,1122928,1122946,1123061,1123487,1173263,1397695,1397698,1869227; Taxon and AkaTaxIds elements for the target associations | supports | Alias-aware official NCBI XML resolution; every nonempty stored name matches. An omitted optional label or a valid merged ID is not a broken reference. Identity verification does not independently validate occurrence or characteristic presence. SHA256 5d47d13bde7b62410a1a15a8818464cc3bb7bb1ba3c09a3e463c347b96b1a210. Results: [{"source_id": "NCBITaxon:102232", "stored_label": "Gloeocapsa sp. PCC 73106", "current_id": "102232", "name": "Gloeocapsa sp. PCC 73106", "rank": "species"}, {"source_id": "NCBITaxon:1121291", "stored_label": "Clostridium acidisoli DSM 12555", "current_id": "1121291", "name": "Clostridium acidisoli DSM 12555", "rank": "strain"}, {"source_id": "NCBITaxon:1122133", "stored_label": "Kaistia soli DSM 19436", "current_id": "1122133", "name": "Kaistia soli DSM 19436", "rank": "strain"}, {"source_id": "NCBITaxon:1122603", "stored_label": "Nevskia ramosa DSM 11499", "current_id": "1122603", "name": "Nevskia ramosa DSM 11499", "rank": "strain"}, {"source_id": "NCBITaxon:1122612", "stored_label": "Novosphingobium acidiphilum DSM 19966", "current_id": "1122612", "name": "Novosphingobium acidiphilum DSM 19966", "rank": "strain"}, {"source_id": "NCBITaxon:1122928", "stored_label": "Paludibacterium yongneupense DSM 18731", "current_id": "1122928", "name": "Paludibacterium yongneupense DSM 18731", "rank": "strain"}, {"source_id": "NCBITaxon:1122946", "stored_label": "Pelobacter seleniigenes DSM 18267", "current_id": "1122946", "name": "Pelobacter seleniigenes DSM 18267", "rank": "strain"}, {"source_id": "NCBITaxon:1123487", "stored_label": "Uliginosibacterium gangwonense DSM 18521", "current_id": "1123487", "name": "Uliginosibacterium gangwonense DSM 18521", "rank": "strain"}, {"source_id": "NCBITaxon:1173263", "stored_label": "Pseudanabaenococcus habilitatus PCC 7502", "current_id": "1173263", "name": "Pseudanabaenococcus habilitatus PCC 7502", "rank": "strain"}, {"source_id": "NCBITaxon:119641", "stored_label": "Clostridium uliginosum", "current_id": "119641", "name": "Clostridium uliginosum", "rank": "species"}, {"source_id": "NCBITaxon:1397695", "stored_label": "Exiguobacterium undae 190-11", "current_id": "1397695", "name": "Exiguobacterium undae 190-11", "rank": "strain"}, {"source_id": "NCBITaxon:1397698", "stored_label": "Exiguobacterium artemiae 7-3", "current_id": "1397698", "name": "Exiguobacterium artemiae 7-3", "rank": "strain"}, {"source_id": "NCBITaxon:140314", "stored_label": "Trichococcus palustris", "current_id": "140314", "name": "Trichococcus palustris", "rank": "species"}, {"source_id": "NCBITaxon:217068", "stored_label": "Ancylobacter tetraedralis", "current_id": "217068", "name": "Ancylobacter tetraedralis", "rank": "species"}, {"source_id": "NCBITaxon:267374", "stored_label": "Marinobacterium halophilum", "current_id": "267374", "name": "Marinobacterium halophilum", "rank": "species"}, {"source_id": "NCBITaxon:395960", "stored_label": "Rhodopseudomonas palustris TIE-1", "current_id": "395960", "name": "Rhodopseudomonas palustris TIE-1", "rank": "strain"}, {"source_id": "NCBITaxon:395964", "stored_label": "Methylocapsa acidiphila B2", "current_id": "395964", "name": "Methylocapsa acidiphila B2", "rank": "strain"}, {"source_id": "NCBITaxon:402880", "stored_label": "Methanococcus maripaludis C5", "current_id": "402880", "name": "Methanococcus maripaludis C5", "rank": "strain"}, {"source_id": "NCBITaxon:423350", "stored_label": "Mucilaginibacter gracilis", "current_id": "423350", "name": "Mucilaginibacter gracilis", "rank": "species"}, {"source_id": "NCBITaxon:456442", "stored_label": "Methanoregula boonei 6A8", "current_id": "456442", "name": "Methanoregula boonei 6A8", "rank": "strain"}, {"source_id": "NCBITaxon:471857", "stored_label": "Saccharomonospora viridis DSM 43017", "current_id": "471857", "name": "Saccharomonospora viridis DSM 43017", "rank": "strain"}, {"source_id": "NCBITaxon:474950", "stored_label": "Granulicella pectinivorans", "current_id": "474950", "name": "Granulicella pectinivorans", "rank": "species"}, {"source_id": "NCBITaxon:474952", "stored_label": "Granulicella rosea", "current_id": "474952", "name": "Granulicella rosea", "rank": "species"}, {"source_id": "NCBITaxon:521011", "stored_label": "Methanosphaerula palustris E1-9c", "current_id": "521011", "name": "Methanosphaerula palustris E1-9c", "rank": "strain"}, {"source_id": "NCBITaxon:714943", "stored_label": "Mucilaginibacter paludis DSM 18603", "current_id": "714943", "name": "Mucilaginibacter paludis DSM 18603", "rank": "strain"}] |
| WETLAND | https://www.epa.gov/wetlands/what-wetland; Wetland description | context_only | Wetlands are areas where water covers or saturates soil, supporting an area distinct from its water or soil material. |

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
review_id: 20261014T053406Z-wetland_area
kind: record
repository: CultureBotAI/HabitatMech
title: 'Scientific record review: wetland area'
started_at: '2026-10-14T05:18:56.544848Z'
finished_at: '2026-10-14T05:34:06.025546Z'
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
verdict: needs_curation
summary: The corrected vegetated-area hierarchy and four-source review lifecycle reproduce.
  WetlandRegion is related in ENVO but emitted as exact. Qualified GOLD source equivalence
  and original PREGO occurrence keys remain limitations.
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
  - path: data/habitats/aquatic/wetland_area.yaml
    sha256: 9b69cd8a60e7d7b828686e42ce29ddb9c82bcefac719aeb844496b69cf4e238b
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
- target_id: ENVO:00000043
  path: data/habitats/aquatic/wetland_area.yaml
  label: wetland area
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
  - ENVO:00000043
checks:
- check_id: C0
  name: Native validate
  required: true
  status: passed
  target_ids:
  - ENVO:00000043
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/aquatic/wetland_area.yaml
  exit_code: 0
  summary: Actual successful execution from 2026-10-14T05:19:14.243705Z to 2026-10-14T05:19:17.056462Z.
    Record-specific or full-corpus command scope is explicit. Reproduction and validation
    are not scientific approval.
- check_id: C1
  name: Native validate-strict
  required: true
  status: passed
  target_ids:
  - ENVO:00000043
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
  - ENVO:00000043
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
  - ENVO:00000043
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
  - ENVO:00000043
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
  - ENVO:00000043
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
  - ENVO:00000043
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
  - ENVO:00000043
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
  - ENVO:00000043
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
  - ENVO:00000043
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
  - ENVO:00000043
  summary: No gene, regulator, protein or transcriptomic-module assertion occurs in
    this target. iModulonDB non-use is not evidence of biological absence.
evidence:
- evidence_id: RECORD
  kind: record_content
  reference: data/habitats/aquatic/wetland_area.yaml
  accessed_at: '2026-10-14T05:34:06.024731Z'
  support: supports
  summary: The entire target was read before judgment, including all attestations,
    associations and generated events. Complete parsed-document reproduction and captured
    hash checks passed. The corrected vegetated-area hierarchy and four-source review
    lifecycle reproduce. WetlandRegion is related in ENVO but emitted as exact. Qualified
    GOLD source equivalence and original PREGO occurrence keys remain limitations.
- evidence_id: RAW
  kind: record_content
  reference: data/raw/gold_ecosystem_paths.tsv:276,359,718; data/raw/prego_habitat_taxa.tsv:3438,3439,3440,3441,3442,3443,3444,3445,3446,3447,3448,3449,3450,3451,3452,3453,3454,3455,3456,3457,3458,3459,3460,3461,3462;
    data/raw/prego_habitats.tsv:223; data/raw/gold_path_triads.tsv:416,417,418,680,681,682,1211,1212,1213;
    data/raw/gold_path_biosamples.tsv:44,212,283; data/raw/gold_studies.tsv:165,474,525,542,591,626,685,827,859,887,1003,1151,1177,1331,1527,1821,1876,1976,2163,2165,2167,2168,2219,2288,2306,2443,2498,2869,3004,3327,3335,3504,3564,3565,3864,4086,4142,4200,4260,4322,4328,4390,4407,4441,4491,4555,4570,4584;
    data/raw/ontology_subclass_edges.tsv:4673,7153; data/raw/ontology_terms.tsv:6633,8793;
    curation/gold_parent_exclusions.tsv:137,138,139; curation/decisions.tsv:588,852,967,1504
  accessed_at: '2026-10-14T05:34:06.024731Z'
  support: supports
  summary: 'Locators are logical TSV records counted with header as row 1. Structured
    scans and native document reproduction verify the emitted source paths, collapsed-node
    notes, count units, score channels, displayed association ranking and historical
    events. The source inventory is not independent experimental evidence. Exact emitted
    attestations: [{"source": "GOLD", "source_id": "gold.ecosystem:3783", "source_label":
    "Wetlands", "source_path": "Environmental > Aquatic > Marine > Wetlands", "mapping_predicate":
    "skos:exactMatch", "assertion_count": 3, "assertion_unit": "ORGANISM", "notes":
    "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."},
    {"source": "GOLD", "source_id": "gold.ecosystem:3795", "source_label": "Wetlands",
    "source_path": "Environmental > Aquatic > Freshwater > Wetlands", "mapping_predicate":
    "skos:exactMatch", "assertion_count": 61, "assertion_unit": "ORGANISM", "notes":
    "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."},
    {"source": "GOLD", "source_id": "gold.ecosystem:3815", "source_label": "Wetlands",
    "source_path": "Environmental > Terrestrial > Soil > Wetlands", "mapping_predicate":
    "skos:exactMatch", "assertion_count": 29, "assertion_unit": "ORGANISM", "notes":
    "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."},
    {"source": "PREGO", "source_id": "ENVO:00000043", "source_label": "wetland area",
    "assertion_count": 50, "assertion_unit": "TAXON", "score": 4.0, "evidence_channels":
    "annotated_genomes_isolates"}]'
- evidence_id: RULES
  kind: record_content
  reference: docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; docs/record-review-profile.md;
    .claude/skills/curate-yaml-record/references/review-checklist.md
  accessed_at: '2026-10-14T05:34:06.024731Z'
  support: supports
  summary: Applied habitat identity, strict genus, typed synonym, MIxS-role, source-unit,
    taxon-association and lifecycle rules. Optional missing fields are not automatically
    defects. Scientific review does not create ITEM decisions or promote native status.
- evidence_id: OWNERS
  kind: record_content
  reference: curation/decisions.tsv; curation/gold_parent_exclusions.tsv; curation/term_requests.tsv;
    src/habitatmech/seed.py; src/habitatmech/extract.py; src/habitatmech/schema/habitatmech.yaml
  accessed_at: '2026-10-14T05:34:06.024731Z'
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
  accessed_at: '2026-10-14T05:18:07.433199Z'
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
  locator: Named classes ENVO:00000043, ENVO:00000446, ENVO:00000447, ENVO:00001998,
    ENVO:00001999, ENVO:00002007, ENVO:00002011, ENVO:00002030, ENVO:01001305
  accessed_at: '2026-10-14T05:18:11.169812Z'
  support: supports
  summary: 'Official current file commit a2455d1a77e46bb8a664d65a157166b539269042,
    SHA256 a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c. Inspected
    definitions, named parents, deprecated flags and typed synonyms. Target/genus
    classes are active; historical triad annotations are checked separately, not silently
    promoted to current record assertions: {"ENVO:00000043": {"label": "wetland area",
    "definition": "An vegetated area which overlaps a wetland ecosystem.", "deprecated":
    null, "synonyms": {"hasExactSynonym": [], "hasBroadSynonym": [], "hasNarrowSynonym":
    [], "hasRelatedSynonym": ["WetlandRegion"]}, "parents": ["http://purl.obolibrary.org/obo/ENVO_01001305"]},
    "ENVO:00000446": {"label": "terrestrial biome", "definition": "A biome which is  primarily
    or completely situated on a landmass.", "deprecated": null, "synonyms": {"hasExactSynonym":
    [], "hasBroadSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": ["terrestrial
    realm"]}, "parents": ["http://purl.obolibrary.org/obo/ENVO_00000428", "http://purl.obolibrary.org/obo/ENVO_01001790"]},
    "ENVO:00000447": {"label": "marine biome", "definition": "An aquatic biome which
    is determined by a marine water body.", "deprecated": null, "synonyms": {"hasExactSynonym":
    [], "hasBroadSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": ["marine
    realm"]}, "parents": ["http://purl.obolibrary.org/obo/ENVO_00002030", "http://purl.obolibrary.org/obo/ENVO_01001788"]},
    "ENVO:00001998": {"label": "soil", "definition": "An environmental material which
    is primarily composed of minerals, varying proportions of sand, silt, and clay,
    organic material such as humus, interstitial gases, liquids, and a broad range
    of resident micro- and macroorganisms.", "deprecated": null, "synonyms": {"hasExactSynonym":
    [], "hasBroadSynonym": ["regolith"], "hasNarrowSynonym": [], "hasRelatedSynonym":
    []}, "parents": ["http://purl.obolibrary.org/obo/ENVO_00010483", "http://purl.obolibrary.org/obo/ENVO_01000813"]},
    "ENVO:00001999": {"label": "marine water body", "definition": "A lentic water
    body which is composed primarily of marine water.", "deprecated": null, "synonyms":
    {"hasExactSynonym": ["body of marine water", "marine waterbody"], "hasBroadSynonym":
    [], "hasNarrowSynonym": [], "hasRelatedSynonym": []}, "parents": ["http://purl.obolibrary.org/obo/ENVO_01000617"]},
    "ENVO:00002007": {"label": "sediment", "definition": "Particulate environmental
    material which is formed as a result of the transport and deposition of particles
    by flowing liquid.", "deprecated": null, "synonyms": {"hasExactSynonym": [], "hasBroadSynonym":
    [], "hasNarrowSynonym": [], "hasRelatedSynonym": []}, "parents": ["http://purl.obolibrary.org/obo/ENVO_01000060"]},
    "ENVO:00002011": {"label": "fresh water", "definition": "Water which has a low
    concentration of dissolved solutes, particularly that of sodium chloride.", "deprecated":
    null, "synonyms": {"hasExactSynonym": ["freshwater"], "hasBroadSynonym": [], "hasNarrowSynonym":
    [], "hasRelatedSynonym": ["sweet water"]}, "parents": ["http://purl.obolibrary.org/obo/ENVO_00002006"]},
    "ENVO:00002030": {"label": "aquatic biome", "definition": "A biome which is determined
    by a water body and which has ecological climax communities adapted to life in
    or on water.", "deprecated": null, "synonyms": {"hasExactSynonym": [], "hasBroadSynonym":
    [], "hasNarrowSynonym": [], "hasRelatedSynonym": []}, "parents": ["http://purl.obolibrary.org/obo/ENVO_00000428",
    "http://purl.obolibrary.org/obo/ENVO_01001787"]}, "ENVO:01001305": {"label": "vegetated
    area", "definition": "A vegetated area is a geographic feature which has ground
    cover dominated by plant communities.", "deprecated": null, "synonyms": {"hasExactSynonym":
    [], "hasBroadSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": []}, "parents":
    ["http://purl.obolibrary.org/obo/ENVO_01001199"]}}'
- evidence_id: BASE_QC
  kind: record_content
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38513776724
  accessed_at: '2026-10-14T05:34:06.024731Z'
  support: supports
  summary: Fresh gh run view confirmed completed success on exact base 471f0b0b55721a1ba566525ae6e510dca644b892,
    with separate structured-contract and authoritative-QC steps successful. This
    verifies unchanged scientific inputs, not newly authored review files. Full QC
    was not rerun locally for these review-only additions.
- evidence_id: GOLD
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=ecosystempaths
  accessed_at: '2026-10-14T05:18:15.162224Z'
  locator: Workbook rows 666, 808, 1153
  support: supports
  summary: 'The complete public workbook has 2422 rows including its header; incorrect
    worksheet dimensions were reset before reading. SHA256 f13652be516a0f1482bf0abbb44d7d8e9acb17c5d401cd7e0474af949b447611.
    Exact matching vocabulary rows: [{"row": 666, "values": ["4181", "Environmental",
    "Aquatic", "Freshwater", "Wetlands", "Unclassified"]}, {"row": 808, "values":
    ["4055", "Environmental", "Aquatic", "Marine", "Wetlands", "Unclassified"]}, {"row":
    1153, "values": ["4235", "Environmental", "Terrestrial", "Soil", "Wetlands", "Unclassified"]}].
    Terminal vocabulary rows do not verify every historical internal node or original
    sample population.'
- evidence_id: GOLD_SCOPE
  kind: database
  reference: https://gold.jgi.doe.gov/ecosystem_classification
  accessed_at: '2026-10-14T05:26:14Z'
  locator: Classification purpose and five-level descriptions
  support: context_only
  summary: The sample-driven classification describes collection surroundings. A path
    edge is not automatically a strict ontology subclass, and study membership does
    not establish every sample's habitat.
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
    [{"source_id": "NCBITaxon:102232", "stored_label": "Gloeocapsa sp. PCC 73106",
    "current_id": "102232", "name": "Gloeocapsa sp. PCC 73106", "rank": "species"},
    {"source_id": "NCBITaxon:1121291", "stored_label": "Clostridium acidisoli DSM
    12555", "current_id": "1121291", "name": "Clostridium acidisoli DSM 12555", "rank":
    "strain"}, {"source_id": "NCBITaxon:1122133", "stored_label": "Kaistia soli DSM
    19436", "current_id": "1122133", "name": "Kaistia soli DSM 19436", "rank": "strain"},
    {"source_id": "NCBITaxon:1122603", "stored_label": "Nevskia ramosa DSM 11499",
    "current_id": "1122603", "name": "Nevskia ramosa DSM 11499", "rank": "strain"},
    {"source_id": "NCBITaxon:1122612", "stored_label": "Novosphingobium acidiphilum
    DSM 19966", "current_id": "1122612", "name": "Novosphingobium acidiphilum DSM
    19966", "rank": "strain"}, {"source_id": "NCBITaxon:1122928", "stored_label":
    "Paludibacterium yongneupense DSM 18731", "current_id": "1122928", "name": "Paludibacterium
    yongneupense DSM 18731", "rank": "strain"}, {"source_id": "NCBITaxon:1122946",
    "stored_label": "Pelobacter seleniigenes DSM 18267", "current_id": "1122946",
    "name": "Pelobacter seleniigenes DSM 18267", "rank": "strain"}, {"source_id":
    "NCBITaxon:1123487", "stored_label": "Uliginosibacterium gangwonense DSM 18521",
    "current_id": "1123487", "name": "Uliginosibacterium gangwonense DSM 18521", "rank":
    "strain"}, {"source_id": "NCBITaxon:1173263", "stored_label": "Pseudanabaenococcus
    habilitatus PCC 7502", "current_id": "1173263", "name": "Pseudanabaenococcus habilitatus
    PCC 7502", "rank": "strain"}, {"source_id": "NCBITaxon:119641", "stored_label":
    "Clostridium uliginosum", "current_id": "119641", "name": "Clostridium uliginosum",
    "rank": "species"}, {"source_id": "NCBITaxon:1397695", "stored_label": "Exiguobacterium
    undae 190-11", "current_id": "1397695", "name": "Exiguobacterium undae 190-11",
    "rank": "strain"}, {"source_id": "NCBITaxon:1397698", "stored_label": "Exiguobacterium
    artemiae 7-3", "current_id": "1397698", "name": "Exiguobacterium artemiae 7-3",
    "rank": "strain"}, {"source_id": "NCBITaxon:140314", "stored_label": "Trichococcus
    palustris", "current_id": "140314", "name": "Trichococcus palustris", "rank":
    "species"}, {"source_id": "NCBITaxon:217068", "stored_label": "Ancylobacter tetraedralis",
    "current_id": "217068", "name": "Ancylobacter tetraedralis", "rank": "species"},
    {"source_id": "NCBITaxon:267374", "stored_label": "Marinobacterium halophilum",
    "current_id": "267374", "name": "Marinobacterium halophilum", "rank": "species"},
    {"source_id": "NCBITaxon:395960", "stored_label": "Rhodopseudomonas palustris
    TIE-1", "current_id": "395960", "name": "Rhodopseudomonas palustris TIE-1", "rank":
    "strain"}, {"source_id": "NCBITaxon:395964", "stored_label": "Methylocapsa acidiphila
    B2", "current_id": "395964", "name": "Methylocapsa acidiphila B2", "rank": "strain"},
    {"source_id": "NCBITaxon:402880", "stored_label": "Methanococcus maripaludis C5",
    "current_id": "402880", "name": "Methanococcus maripaludis C5", "rank": "strain"},
    {"source_id": "NCBITaxon:423350", "stored_label": "Mucilaginibacter gracilis",
    "current_id": "423350", "name": "Mucilaginibacter gracilis", "rank": "species"},
    {"source_id": "NCBITaxon:456442", "stored_label": "Methanoregula boonei 6A8",
    "current_id": "456442", "name": "Methanoregula boonei 6A8", "rank": "strain"},
    {"source_id": "NCBITaxon:471857", "stored_label": "Saccharomonospora viridis DSM
    43017", "current_id": "471857", "name": "Saccharomonospora viridis DSM 43017",
    "rank": "strain"}, {"source_id": "NCBITaxon:474950", "stored_label": "Granulicella
    pectinivorans", "current_id": "474950", "name": "Granulicella pectinivorans",
    "rank": "species"}, {"source_id": "NCBITaxon:474952", "stored_label": "Granulicella
    rosea", "current_id": "474952", "name": "Granulicella rosea", "rank": "species"},
    {"source_id": "NCBITaxon:521011", "stored_label": "Methanosphaerula palustris
    E1-9c", "current_id": "521011", "name": "Methanosphaerula palustris E1-9c", "rank":
    "strain"}, {"source_id": "NCBITaxon:714943", "stored_label": "Mucilaginibacter
    paludis DSM 18603", "current_id": "714943", "name": "Mucilaginibacter paludis
    DSM 18603", "rank": "strain"}]'
- evidence_id: WETLAND
  kind: database
  reference: https://www.epa.gov/wetlands/what-wetland
  locator: Wetland description
  accessed_at: '2026-10-14T05:34:06.024731Z'
  support: context_only
  summary: Wetlands are areas where water covers or saturates soil, supporting an
    area distinct from its water or soil material.
assessments:
- assessment_id: IDENTITY
  area: identity
  topic: Entity, grounding, strict hierarchy and source scope
  outcome: supported
  target_ids:
  - ENVO:00000043
  evidence_ids:
  - RECORD
  - ENVO
  - RAW
  - OWNERS
  - RULES
  - WETLAND
  summary: ENVO:00000043 is a vegetated area overlapping a wetland ecosystem, with
    ENVO:01001305 as its genus. Exclusions 137-139 already remove soil, whole marine
    water body and fresh-water material. Four ITEM decisions explain REVIEWED, but
    the generic wetland definition does not independently establish exact equivalence
    of freshwater, marine and soil-qualified source extensions. Retain each path and
    this limitation rather than declaring the prefixes immaterial. GOLD Wetlands has
    independent source provenance; ENVO WetlandRegion must be related.
- assessment_id: SCIENCE
  area: evidence
  topic: Claim-level scientific support, taxa, MIxS and source-unit limits
  outcome: supported
  target_ids:
  - ENVO:00000043
  evidence_ids:
  - RECORD
  - RAW
  - ENVO
  - WETLAND
  - TAXA
  summary: The three GOLD paths retain 3, 61 and 29 ORGANISM assertions separately.
    PREGO row 223 has 50 TAXON, 63 direct assertions, score 4 and 25 retained associations;
    distinct taxa must not be conflated with direct assertions. Bulk marine/freshwater/soil
    counts are 115/75/793, while complete-triad populations are 5/22/316. Forty-eight
    study rows are path memberships, not 48 independent experiments. Modal ecosystem,
    wetland and material terms serve different roles. EPA supports the area-versus-water/soil
    distinction, not every merged-source equivalence.
- assessment_id: STATUS
  area: provenance
  topic: Generated status, history and optional-field completeness
  outcome: supported
  target_ids:
  - ENVO:00000043
  evidence_ids:
  - RECORD
  - RAW
  - OWNERS
  - SEARCH
  summary: The complete record reproduces from maintained inputs, including EXACT/REVIEWED,
    all source attestations and 8 historical events. REVIEWED requires all contributing
    ITEM decisions; CLASS decisions remain seeded. No review is a status promotion.
    The target asserts no causal graph or environmental-parameter block; source triads
    and external examples are not promoted into these optional slots.
- assessment_id: FINDING
  area: grounding
  topic: Non-exact ontology synonyms are emitted as exact
  outcome: concern
  target_ids:
  - ENVO:00000043
  evidence_ids:
  - RECORD
  - RAW
  - OWNERS
  - RULES
  - ENVO
  - WETLAND
  summary: 'Current official ENVO types these aliases non-exact: {"hasRelatedSynonym":
    ["WetlandRegion"]}. The generated record emits each as EXACT_SYNONYM. The frozen
    ontology_terms pipe loses scope and ConceptStore.get promotes all ontology aliases
    to exact. Source-label repairs do not fix this ontology-source defect. Preserve
    genuine exact assertions and multiple scopes when supplied.'
findings:
- finding_id: F1
  issue_key: envo-00000043-synonym-scope
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Non-exact ontology synonyms are emitted as exact
  description: 'Current official ENVO types these aliases non-exact: {"hasRelatedSynonym":
    ["WetlandRegion"]}. The generated record emits each as EXACT_SYNONYM. The frozen
    ontology_terms pipe loses scope and ConceptStore.get promotes all ontology aliases
    to exact. Source-label repairs do not fix this ontology-source defect. Preserve
    genuine exact assertions and multiple scopes when supplied.'
  target_ids:
  - ENVO:00000043
  field_paths:
  - synonyms
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained owner for a separately authorized correction
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained owner for a separately authorized correction
  evidence_ids:
  - RECORD
  - RAW
  - OWNERS
  - RULES
  - ENVO
  - WETLAND
  rule_id: docs/CURATION.md; docs/record-review-profile.md
  native_severity: major
  normalization_reason: Material scope inflation, false strict genus, or mapping contract
    mismatch, not style; identity remains resolved and no new wrong-identity blocker
    is asserted.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1249
actions:
- action_id: A1
  description: Preserve typed synonym assertions through governed upstream extraction,
    the ontology inventory contract and generation. Test exact, broad, narrow, related,
    mixed-source and multiple-scope cases. Regenerate from real source provenance
    without checksum patches or a global downgrade.
  finding_ids:
  - F1
  target_ids:
  - ENVO:00000043
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained owner for a separately authorized correction
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained owner for a separately authorized correction
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Address the exact evidence and source contribution described in F1; preserve independent
    valid parents, source IDs, paths, count units and historical events.
  - Use maintained owners, append required curation history, inspect an exact canary,
    and pass schema, labels, provenance, reproduction, term requests, generated site
    and full QC. Rebuild genuinely affected semantic products.
  - Do not edit generated YAML or immutable reviews. Any later disposition needs a
    new review retaining this issue key and exact previous occurrence; publication
    alone does not resolve it.
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
