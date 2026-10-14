# Scientific follow-up: Egg

- Review: 20261014T102058Z-egg_food_product-followup
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-14T10:02:08.856907Z
- Finished UTC: 2026-10-14T10:20:58.141913Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

BacDive Egg now retains its native source identity and HOST_ASSOCIATED coarse category without the false food/vertebrate definition or parent. All 35 STRAIN-unit source assertions and 25 displayed taxon observations/ranks from the 30-taxon pool are preserved. Exact-strain evidence supports rejecting the food-only mapping; it does not reconstruct all original members or supply a complete egg-associated definition. ITEM/REVIEWED is a workflow status, not an exact ontology claim.

## Scope And Provenance

Complete corrected record and exact predecessor finding disposition.

Selection: Explicit source-preserving correction follow-up, not sampling. Includes current native record and former ontology identity as a maintained mapping-row claim to preserve all predecessor targets.
Coverage: full; 2 reviewed / 2 in the declared population.
Source: working_tree at Git base 0e966aec8a12892973dd15c536f89d90ab0c2c70.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:BACDIVE.d48ce9485d | data/habitats/host_associated/egg.yaml | generated | Egg (BacDive host-product source) |
| FOODON:00001274 | curation/decisions.tsv # identifier=habitatmech:BACDIVE.d48ce9485d; former FOODON:00001274 identity now rejected by CONFIRM_UNGROUNDED | snapshot_row | Former egg-food identity claim retained as a mapping disposition |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate | passed | True | habitatmech:BACDIVE.d48ce9485d, FOODON:00001274 | Executed 2026-10-14T10:02:24.768716Z to 2026-10-14T10:02:27.124209Z. No issues found |
| just validate-strict | passed | True | habitatmech:BACDIVE.d48ce9485d, FOODON:00001274 | Executed 2026-10-14T10:02:29.375588Z to 2026-10-14T10:02:34.192584Z. uv run python scripts/validate_strict.py data/habitats/food/cheese.yaml data/habitats/food/cooked_meat.yaml data/habitats/food/dairy_food_product.yaml data/habitats/host_associated/egg.yaml data/habitats/food/egg_products.yaml<br>Validating 5 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      5<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| just validate-history | passed | True | habitatmech:BACDIVE.d48ce9485d, FOODON:00001274 | Executed 2026-10-14T10:02:34.193195Z to 2026-10-14T10:02:41.329829Z. No issues found<br>659 history record(s) valid against src/habitatmech/schema/history.yaml |
| just provenance-check | passed | True | habitatmech:BACDIVE.d48ce9485d, FOODON:00001274 | Executed 2026-10-14T10:02:41.330400Z to 2026-10-14T10:02:41.842199Z. provenance current: 14 committed inventories, 2 GOLD sources |
| just verify-corpus | passed | True | habitatmech:BACDIVE.d48ce9485d, FOODON:00001274 | Executed 2026-10-14T10:02:41.842688Z to 2026-10-14T10:02:57.759857Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ |
| just validate-causal-all | passed | True | habitatmech:BACDIVE.d48ce9485d, FOODON:00001274 | Executed 2026-10-14T10:02:57.760640Z to 2026-10-14T10:03:01.979292Z. validated 32 causal-graph curation file(s) with 32 graph(s) |
| just term-requests-check | passed | True | habitatmech:BACDIVE.d48ce9485d, FOODON:00001274 | Executed 2026-10-14T10:03:01.979839Z to 2026-10-14T10:03:17.947037Z. term-request table is current (109 terms) |
| just validate-products | passed | True | habitatmech:BACDIVE.d48ce9485d, FOODON:00001274 | Executed 2026-10-14T10:03:17.947566Z to 2026-10-14T10:04:03.215199Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1176<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2059<br><br>✅ All id↔label pairs correspond. |
| uv run | passed | True | habitatmech:BACDIVE.d48ce9485d, FOODON:00001274 | Executed 2026-10-14T10:04:03.215881Z to 2026-10-14T10:05:25.219804Z. ........................................................................ [ 80%]<br>..................                                                       [100%]<br>90 passed in 81.08s (0:01:21) |
| uv run | passed | True | habitatmech:BACDIVE.d48ce9485d, FOODON:00001274 | Executed 2026-10-14T10:05:25.220422Z to 2026-10-14T10:05:25.351468Z. All checks passed! |
| Exact corrected-base hosted authoritative QC | passed | True | habitatmech:BACDIVE.d48ce9485d, FOODON:00001274 | Verified success on the captured corrected base. Post-save archive and final PR checks remain required. |
| Original source-member reconstruction | unavailable | False | habitatmech:BACDIVE.d48ce9485d, FOODON:00001274 | Original source dumps/member crosswalks remain unavailable; predecessor GOLD access returned 403. No new access success or complete membership claim. |
| Expression-source applicability | not_applicable | False | habitatmech:BACDIVE.d48ce9485d, FOODON:00001274 | No gene, regulator, protein or transcriptomics assertion. Habitat source identity is not expression-module evidence. |

## Scientific And Domain Assessments

### Identity, parent correction and exact finding disposition

grounding: supported. Targets: habitatmech:BACDIVE.d48ce9485d, FOODON:00001274.

BacDive Egg now retains its native source identity and HOST_ASSOCIATED coarse category without the false food/vertebrate definition or parent. All 35 STRAIN-unit source assertions and 25 displayed taxon observations/ranks from the 30-taxon pool are preserved. Exact-strain evidence supports rejecting the food-only mapping; it does not reconstruct all original members or supply a complete egg-associated definition. ITEM/REVIEWED is a workflow status, not an exact ontology claim.

### Source scope, counts, rank semantics and optional claims

evidence: supported. Targets: habitatmech:BACDIVE.d48ce9485d, FOODON:00001274.

Re-read the entire current record. Source assertions remain distinct from bulk biosamples and complete-triad samples. No new environmental parameter, causal graph, citation, discussion or dataset assertion is introduced. All 25 taxonomy IDs/names remain verified against the predecessor NCBI receipt; counts/ranks/candidate pool are observational, not characteristic presence. The new source mint has no fabricated definition or exact ontology synonym. Native history is regenerated for the corrected identity; the rejected former endorsement remains in Git and the predecessor, not in the new record as an active decision.

## Findings

### F1: Host egg source is assigned a vertebrate food-product identity

blocker / resolved / confirmed; issue key: bacdive-egg-food-only-identity.

BacDive Egg is not food-only. Exact stored strain NCBITaxon:1122175 (DSM 19883, BacDive 7355) comes from an insect egg mass in a waste-stabilization pond and is explicitly categorized Host Body Product &gt; Urogenital tract &gt; Egg. Stored strain 1123347 (DSM 18103, BacDive 5652) comes from halibut egg epiflora. Assigning this source to a vertebrate egg food product is a wrong identity; CLOSE and a RELATED synonym do not repair it.

Disposition: BacDive Egg now retains its native source identity and HOST_ASSOCIATED coarse category without the false food/vertebrate definition or parent. All 35 STRAIN-unit source assertions and 25 displayed taxon observations/ranks from the 30-taxon pool are preserved. Exact-strain evidence supports rejecting the food-only mapping; it does not reconstruct all original members or supply a complete egg-associated definition. ITEM/REVIEWED is a workflow status, not an exact ontology claim.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| CURRENT | data/habitats/host_associated/egg.yaml; Complete corrected YAML, all source and taxon assertions and history | supports | BacDive Egg now retains its native source identity and HOST_ASSOCIATED coarse category without the false food/vertebrate definition or parent. All 35 STRAIN-unit source assertions and 25 displayed taxon observations/ranks from the 30-taxon pool are preserved. Exact-strain evidence supports rejecting the food-only mapping; it does not reconstruct all original members or supply a complete egg-associated definition. ITEM/REVIEWED is a workflow status, not an exact ontology claim. |
| OWNERS | curation/decisions.tsv; curation/gold_parent_exclusions.tsv; tests/test_food_egg_scope.py; curation/decisions.tsv:1718 identifier=habitatmech:BACDIVE.d48ce9485d | supports | Read the complete maintained rows, five append-only histories and counterfactual regression. Full corpus comparison changes only four common records (parent/history) and replaces the former food-egg identity with the BacDive source mint. Raw observations are unchanged. |
| PREVIOUS | reviews/structured/20261014T095321Z-egg_food_product/review.yaml | context_only | Read the immutable predecessor, exact finding, evidence receipts and limitations. Its baseline decision rows are historical, not current line references. |
| QC | https://github.com/CultureBotAI/HabitatMech/actions/runs/38547107819 | supports | Verified full hosted QC success on exact corrected commit 0e966aec8a12892973dd15c536f89d90ab0c2c70. Initial corrected scientific inputs were rehashed without change after map/site publication. New successor bundles still require post-save and final PR checks. |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md | supports | Applied strict-superclass, source identity, count-unit, MIxS role, optional-field and ITEM status rules from the local record checklist. |
| TRANSFORM | src/habitatmech/seed.py; src/habitatmech/extract.py; extract_gold; extract_bacdive; ingest_gold; ingest_bacdive; build_document; scripts/extract_gold_biosamples.py; scripts/aggregate_gold_triads.py | supports | GOLD counts outgoing occurrence edges by subject prefix, not proven distinct organisms. Bulk biosamples and study path unions are different inventories. BacDive aggregate strain_count counts source outgoing edges; taxon associations deduplicate strain joins and retain top-25 ranks/candidate_pool. Neither ranking implies characteristic presence. |
| FOODON | https://raw.githubusercontent.com/FoodOntology/foodon/cd73540243a84bcd511a500d9a497d12d7dc02f6/foodon.owl; FOODON:00001274; relevant FoodOn parents and candidate context | supports | Historical external evidence retained from the predecessor, not a description of the corrected record. Read definitions, typed synonyms, active status and direct named parents in the pinned official RDF/XML. SHA256 b897bf64c1b265c422db9ee01e1235c10c0b809e7f02326ef810a52068347edf. BacDive Egg is not food-only. Exact stored strain NCBITaxon:1122175 (DSM 19883, BacDive 7355) comes from an insect egg mass in a waste-stabilization pond and is explicitly categorized Host Body Product &gt; Urogenital tract &gt; Egg. Stored strain 1123347 (DSM 18103, BacDive 5652) comes from halibut egg epiflora. Assigning this source to a vertebrate egg food product is a wrong identity; CLOSE and a RELATED synonym do not repair it. |
| AVAILABILITY | conf/sources.yaml | context_only | {"accessed_at": "2026-10-14T09:44:16.995506Z", "command": ["rg", "--no-ignore", "--hidden", "--files", ".", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data"], "enumerated_files": 41045, "exit_code": 0, "interpretation": "Ignored files included. Bounded to this repository and the configured kg-microbe data root, not all disks. No exact original member crosswalk is inferred from inventory presence.", "matches": []} |
| GOLD_ACCESS | https://gold.jgi.doe.gov/ | context_only | All 25 retrieved study URLs for this cohort returned HTTP 403; no page contents inferred. {"Gs0111397": {"accessed_at": "2026-10-14T09:41:44.844987Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0111397"}, "Gs0117939": {"accessed_at": "2026-10-14T09:41:44.917192Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0117939"}, "Gs0121311": {"accessed_at": "2026-10-14T09:41:44.946799Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0121311"}, "Gs0127428": {"accessed_at": "2026-10-14T09:41:44.984453Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0127428"}, "Gs0132999": {"accessed_at": "2026-10-14T09:41:45.015413Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0132999"}, "Gs0133059": {"accessed_at": "2026-10-14T09:41:45.135671Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0133059"}, "Gs0133061": {"accessed_at": "2026-10-14T09:41:45.168420Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0133061"}, "Gs0133297": {"accessed_at": "2026-10-14T09:41:45.211877Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0133297"}, "Gs0135057": {"accessed_at": "2026-10-14T09:41:45.248222Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0135057"}, "Gs0144921": {"accessed_at": "2026-10-14T09:41:45.279258Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0144921"}, "Gs0144994": {"accessed_at": "2026-10-14T09:41:45.325246Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0144994"}, "Gs0145069": {"accessed_at": "2026-10-14T09:41:45.359515Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0145069"}, "Gs0150357": {"accessed_at": "2026-10-14T09:41:45.403531Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150357"}, "Gs0150359": {"accessed_at": "2026-10-14T09:41:45.534775Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150359"}, "Gs0150613": {"accessed_at": "2026-10-14T09:41:45.657223Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150613"}, "Gs0150615": {"accessed_at": "2026-10-14T09:41:45.694287Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150615"}, "Gs0153752": {"accessed_at": "2026-10-14T09:41:45.728601Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153752"}, "Gs0153769": {"accessed_at": "2026-10-14T09:41:45.759538Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153769"}, "Gs0153860": {"accessed_at": "2026-10-14T09:41:45.793390Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153860"}, "Gs0153898": {"accessed_at": "2026-10-14T09:41:45.825210Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153898"}, "Gs0154236": {"accessed_at": "2026-10-14T09:41:45.874324Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154236"}, "Gs0154282": {"accessed_at": "2026-10-14T09:41:45.906640Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154282"}, "Gs0156793": {"accessed_at": "2026-10-14T09:41:45.940030Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0156793"}, "Gs0159152": {"accessed_at": "2026-10-14T09:41:45.985158Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0159152"}, "Gs0161780": {"accessed_at": "2026-10-14T09:41:46.016628Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0161780"}} |
| TAXONOMY | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;retmode=xml&amp;id=33036,109790,216816,2702,1114867,1121116,1122175,1123347,1215111,1340529,1352,1381081,1470200,147802,1596,1682,2051,2098,28125,28229,293,294,306,358592,37734; All characteristic_taxa entries | supports | All 25 requested taxon IDs resolve with exact stored names; no current label drift. SHA256 613cc4284e20254d01236af61d16c68803e9ef5babb1070ec0e2c3c433f2a5c2. [{"current": {"identifier": "33036", "name": "Anaerococcus tetradius", "names": ["Gaffkya anaerobius", "Peptostreptococcus tetradius", "Tetracoccus anaerobius"], "rank": "species"}, "stored": {"association_count": 3, "candidate_pool": 30, "rank": 1, "source": "BACDIVE", "taxon_id": "NCBITaxon:33036", "taxon_label": "Anaerococcus tetradius"}}, {"current": {"identifier": "109790", "name": "Lactobacillus jensenii", "names": [], "rank": "species"}, "stored": {"association_count": 2, "candidate_pool": 30, "rank": 2, "source": "BACDIVE", "taxon_id": "NCBITaxon:109790", "taxon_label": "Lactobacillus jensenii"}}, {"current": {"identifier": "216816", "name": "Bifidobacterium longum", "names": ["Bifidobacterium sp. 12_1_47BFAA"], "rank": "species"}, "stored": {"association_count": 2, "candidate_pool": 30, "rank": 3, "source": "BACDIVE", "taxon_id": "NCBITaxon:216816", "taxon_label": "Bifidobacterium longum"}}, {"current": {"identifier": "2702", "name": "Gardnerella vaginalis", "names": ["Corynebacterium vaginale", "Gardnerella vaginalis (Gardner and Dukes 1955) Greenwood and Pickett 1980", "Haemophilus hemolyticus vaginalis", "Haemophilus vaginalis", "Gardnerella genomic species 1", "s__Bifidobacterium vaginale"], "rank": "species"}, "stored": {"association_count": 2, "candidate_pool": 30, "rank": 4, "source": "BACDIVE", "taxon_id": "NCBITaxon:2702", "taxon_label": "Gardnerella vaginalis"}}, {"current": {"identifier": "1114867", "name": "Flavobacterium plurextorum", "names": ["Flavobacterium sp. 1084B-08", "Flavobacterium sp. 1126-1H-08", "Flavobacterium sp. 424-08", "Flavobacterium sp. 51B-09", "Flavobacterium sp. 986-08"], "rank": "species"}, "stored": {"association_count": 1, "candidate_pool": 30, "rank": 5, "source": "BACDIVE", "taxon_id": "NCBITaxon:1114867", "taxon_label": "Flavobacterium plurextorum"}}, {"current": {"identifier": "1121116", "name": "Allobrachymonas chironomi DSM 19884", "names": ["Allobrachymonas sp. AImA4"], "rank": "strain"}, "stored": {"association_count": 1, "candidate_pool": 30, "rank": 6, "source": "BACDIVE", "taxon_id": "NCBITaxon:1121116", "taxon_label": "Allobrachymonas chironomi DSM 19884"}}, {"current": {"identifier": "1122175", "name": "Leucobacter chironomi DSM 19883", "names": [], "rank": "strain"}, "stored": {"association_count": 1, "candidate_pool": 30, "rank": 7, "source": "BACDIVE", "taxon_id": "NCBITaxon:1122175", "taxon_label": "Leucobacter chironomi DSM 19883"}}, {"current": {"identifier": "1123347", "name": "Tenacibaculum ovolyticum DSM 18103", "names": [], "rank": "strain"}, "stored": {"association_count": 1, "candidate_pool": 30, "rank": 8, "source": "BACDIVE", "taxon_id": "NCBITaxon:1123347", "taxon_label": "Tenacibaculum ovolyticum DSM 18103"}}, {"current": {"identifier": "1215111", "name": "Pseudomonas mucidolens NBRC 103159", "names": [], "rank": "strain"}, "stored": {"association_count": 1, "candidate_pool": 30, "rank": 9, "source": "BACDIVE", "taxon_id": "NCBITaxon:1215111", "taxon_label": "Pseudomonas mucidolens NBRC 103159"}}, {"current": {"identifier": "1340529", "name": "Photobacterium panuliri", "names": ["Photobacterium panuliri Deep et al. 2015", "Photobacterium sp. LBS5"], "rank": "species"}, "stored": {"association_count": 1, "candidate_pool": 30, "rank": 10, "source": "BACDIVE", "taxon_id": "NCBITaxon:1340529", "taxon_label": "Photobacterium panuliri"}}, {"current": {"identifier": "1352", "name": "Enterococcus faecium", "names": ["Streptococcus faecium", "Enterococcus sp. LMG 19843"], "rank": "species"}, "stored": {"association_count": 1, "candidate_pool": 30, "rank": 11, "source": "BACDIVE", "taxon_id": "NCBITaxon:1352", "taxon_label": "Enterococcus faecium"}}, {"current": {"identifier": "1381081", "name": "Vibrio panuliri", "names": ["Vibrio sp. CAIM 703", "Vibrio sp. LBS2"], "rank": "species"}, "stored": {"association_count": 1, "candidate_pool": 30, "rank": 12, "source": "BACDIVE", "taxon_id": "NCBITaxon:1381081", "taxon_label": "Vibrio panuliri"}}, {"current": {"identifier": "1470200", "name": "Neisseria arctica", "names": ["Neisseria sp. KH1479", "Neisseria sp. KH1503", "Neisseria sp. KH1705", "Neisseria sp. KH1744", "Neisseria sp. KH2123", "Neisseria sp. KH2164"], "rank": "species"}, "stored": {"association_count": 1, "candidate_pool": 30, "rank": 13, "source": "BACDIVE", "taxon_id": "NCBITaxon:1470200", "taxon_label": "Neisseria arctica"}}, {"current": {"identifier": "147802", "name": "Lactobacillus iners", "names": ["Lactobacillus sp. EF (Enevold Falsen) group 47", "Lactobacillus sp. 7_1_47FAA"], "rank": "species"}, "stored": {"association_count": 1, "candidate_pool": 30, "rank": 14, "source": "BACDIVE", "taxon_id": "NCBITaxon:147802", "taxon_label": "Lactobacillus iners"}}, {"current": {"identifier": "1596", "name": "Lactobacillus gasseri", "names": ["Lactobacillus sp. JCM 1131"], "rank": "species"}, "stored": {"association_count": 1, "candidate_pool": 30, "rank": 15, "source": "BACDIVE", "taxon_id": "NCBITaxon:1596", "taxon_label": "Lactobacillus gasseri"}}, {"current": {"identifier": "1682", "name": "Bifidobacterium longum subsp. infantis", "names": ["Bifidobacterium lactentis", "Bifidobacterium liberorum", "Bifidobacterium longum bv. Infantis", "Bifidobacterium longum infantis"], "rank": "subspecies"}, "stored": {"association_count": 1, "candidate_pool": 30, "rank": 16, "source": "BACDIVE", "taxon_id": "NCBITaxon:1682", "taxon_label": "Bifidobacterium longum subsp. infantis"}}, {"current": {"identifier": "2051", "name": "Mobiluncus curtisii", "names": ["Falcivibrio vaginalis"], "rank": "species"}, "stored": {"association_count": 1, "candidate_pool": 30, "rank": 17, "source": "BACDIVE", "taxon_id": "NCBITaxon:2051", "taxon_label": "Mobiluncus curtisii"}}, {"current": {"identifier": "2098", "name": "Metamycoplasma hominis", "names": ["Asterococcus hominis", "Micromyces hominis", "Mycoplasma hominis (Freundt 1953) Edward 1955 (Approved Lists 1980)"], "rank": "species"}, "stored": {"association_count": 1, "candidate_pool": 30, "rank": 18, "source": "BACDIVE", "taxon_id": "NCBITaxon:2098", "taxon_label": "Metamycoplasma hominis"}}, {"current": {"identifier": "28125", "name": "Prevotella bivia", "names": ["Bacteroides bivius"], "rank": "species"}, "stored": {"association_count": 1, "candidate_pool": 30, "rank": 19, "source": "BACDIVE", "taxon_id": "NCBITaxon:28125", "taxon_label": "Prevotella bivia"}}, {"current": {"identifier": "28229", "name": "Colwellia psychrerythraea", "names": ["Colwellia psychroerythrus", "Vibrio psychroerythrus", "Vibrio psychroerythus", "Colwellia psychroerythraea", "Colwellia psychroerythrea", "Vibrio psychroerythreus"], "rank": "species"}, "stored": {"association_count": 1, "candidate_pool": 30, "rank": 20, "source": "BACDIVE", "taxon_id": "NCBITaxon:28229", "taxon_label": "Colwellia psychrerythraea"}}, {"current": {"identifier": "293", "name": "Brevundimonas diminuta", "names": ["Bacterium parvulum", "Pseudomonas diminuta"], "rank": "species"}, "stored": {"association_count": 1, "candidate_pool": 30, "rank": 21, "source": "BACDIVE", "taxon_id": "NCBITaxon:293", "taxon_label": "Brevundimonas diminuta"}}, {"current": {"identifier": "294", "name": "Pseudomonas fluorescens", "names": ["Bacillus fluorescens", "Bacillus fluorescens liquefaciens", "Bacterium fluorescen", "Liquidomonas fluorescens", "Pseudomonas sp. AU2390", "Pseudomonas sp. BZ64", "Pseudomonas sp. FY32", "Pseudomonas sp. HSA2/2016", "Pseudomonas sp. HSA3/2016", "Pseudomonas sp. ISSDS-433", "Pseudomonas sp. JCM 17186", "Pseudomonas sp. JCM 2779", "Pseudomonas sp. KH-20150KS3", "Pseudomonas sp. LBUM223", "Pseudomonas sp. LBUM636", "Pseudomonas sp. SM2/2016", "bacterium P1-1"], "rank": "species"}, "stored": {"association_count": 1, "candidate_pool": 30, "rank": 22, "source": "BACDIVE", "taxon_id": "NCBITaxon:294", "taxon_label": "Pseudomonas fluorescens"}}, {"current": {"identifier": "306", "name": "Pseudomonas sp.", "names": ["Achromobacter georgiopolitanum"], "rank": "species"}, "stored": {"association_count": 1, "candidate_pool": 30, "rank": 23, "source": "BACDIVE", "taxon_id": "NCBITaxon:306", "taxon_label": "Pseudomonas sp."}}, {"current": {"identifier": "358592", "name": "Rheinheimera chironomi", "names": ["Pararheinheimera chironomi", "chironomid egg mass bacterium K19414"], "rank": "species"}, "stored": {"association_count": 1, "candidate_pool": 30, "rank": 24, "source": "BACDIVE", "taxon_id": "NCBITaxon:358592", "taxon_label": "Rheinheimera chironomi"}}, {"current": {"identifier": "37734", "name": "Enterococcus casseliflavus", "names": ["Enterococcus flavescens", "Streptococcus casseliflavus", "Streptococcus faecium subsp. casseliflavus", "Streptococcus faecium var. casseliflavus", "Streptococcus flavescens", "Enterococcus sp. LMG 12310", "Enterococcus sp. VTT E-96690"], "rank": "species"}, "stored": {"association_count": 1, "candidate_pool": 30, "rank": 25, "source": "BACDIVE", "taxon_id": "NCBITaxon:37734", "taxon_label": "Enterococcus casseliflavus"}}] |
| BACDIVE-7355 | https://bacdive.dsmz.de/strain/7355; Names and IDs; Isolation source categories; Isolation | refutes | Exact type strain DSM 19883 / taxid 1122175: chironomid egg mass from Tivon waste-stabilization pond. Isolation categories include Host Body Product &gt; Urogenital tract &gt; Egg and Host &gt; Arthropoda &gt; Insecta. This refutes food-only and vertebrate-only source scope. SHA256 026b7ba7c9046c6b2a10e89903dca1f13c3719bc1d456b26f946f6a6e9612c41 |
| BACDIVE-5652 | https://bacdive.dsmz.de/strain/5652; Names and IDs; Isolation source categories; Isolation | refutes | Exact type strain DSM 18103 / taxid 1123347: Atlantic halibut egg epiflora. Isolation category Host Body Product &gt; Urogenital tract &gt; Egg establishes a host-product category, not a food-only vocabulary branch. SHA256 5023563ccb6f2266e9257d30ade74a4ce4e5a1369c8886d4896311b5ab083fb3 |
| RAW | reviews/structured/20261014T095321Z-egg_food_product/review.yaml; evidence_id=RAW; assessments SCIENCE | context_only | Frozen source tables are byte-unchanged; baseline curation rows are superseded by OWNERS. BacDive isolation row 105 carries 35 STRAIN-unit source assertions and a 30-taxon candidate pool; mapping row 99 supplies a medium-confidence lexical closeMatch. ITEM decision row 1718 wrongly asserts that this vocabulary branch consists of foods. All 25 displayed taxon IDs and names resolve in fresh NCBI taxonomy; ranks/counts follow the frozen join, not prevalence or characteristic presence. The 25 rows sum to 30 associations, not 35 distinct organisms; five candidate taxa are not displayed. Two exact-strain witnesses refute food-only scope but do not reconstruct all 35 frozen source members. |

## Limits And Additional Notes

- Same-agent review and adversarial pass, not independent approval.
- Original source membership remains unavailable. Cheese source identity versus fermentation context and fuller egg-source scope are not resolved by bounded corrections.
- No latest-ontology refresh or SSSOM/KGX conformance certification. Native label checks retain configured exceptions and unsupported-prefix skips.
- Only exact predecessor findings receive the shown dispositions; adjacent Fish products, Meat products and Fermented dairy products records are not silently curated.
- Corrected-base full QC predates new successor bundles; post-save archive and final publication gates remain required.
- Initial corrected capture at 09bb13f857d3e634f4a8cb295d7b847b10612a4b; reinspection after map/site publication proved every scientific input hash unchanged before recording the final corrected base. The explicit empty-target relation default is semantically inactive and was captured before this review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T102058Z-egg_food_product-followup
kind: batch
repository: CultureBotAI/HabitatMech
title: 'Scientific follow-up: Egg'
started_at: '2026-10-14T10:02:08.856907Z'
finished_at: '2026-10-14T10:20:58.141913Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Same agent participated in repository work; not independent
    approval.
skill: .claude/skills/curate-yaml-record/SKILL.md
completion: completed
scientific_review: true
verdict: pass_with_limitations
summary: BacDive Egg now retains its native source identity and HOST_ASSOCIATED coarse
  category without the false food/vertebrate definition or parent. All 35 STRAIN-unit
  source assertions and 25 displayed taxon observations/ranks from the 30-taxon pool
  are preserved. Exact-strain evidence supports rejecting the food-only mapping; it
  does not reconstruct all original members or supply a complete egg-associated definition.
  ITEM/REVIEWED is a workflow status, not an exact ontology claim.
source:
  git_revision: 0e966aec8a12892973dd15c536f89d90ab0c2c70
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
  - path: conf/record_review.yaml
    sha256: c2f5d0eb4c5744f5fe354c92184ddab144dc2688dba952b032b4f3d597bc08d6
    role: context
  - path: conf/sources.yaml
    sha256: a8e069f9278068b57fa234f43e03c8d893f857827b83fd10cfa92d6815aed642
    role: context
  - path: curation/decisions.tsv
    sha256: 05aee2989e186bba8ae0ecb5eca6c1f2ad3c1e6977c3aaf0aea6977bccd6f900
    role: target
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 2d41fc93db4939122b3909f2a412b84b679703948b10d9f02e12021442f71407
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: ffde12786b35a791272a202f26d3baa0a36879c63a97dbdc2d11d38683d7fe0f
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/samples/class_swept_unscreened-20260814.tsv
    sha256: 27fce2849781b21f8fdb434aaaffac0f55e51bef84f1c1ea7d7feecd11d8471e
    role: context
  - path: curation/term_requests.tsv
    sha256: 331a7d9eb8a8909fc37402c0a776838979a8065644504d5c4f2a1c39bce5c24d
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: 3781420be8a7a6de4f44c9be1bc3a0d256824fb44b8dbbb56c6b3c99e21a6014
    role: context
  - path: data/habitats/food/cheese.yaml
    sha256: 16174620ee9ed816c5edce647beda782cbe1709a576d4222e3718990342cc3d5
    role: context
  - path: data/habitats/food/cold_smoked_fish.yaml
    sha256: ea4db4c6c2d849efc11464ef0373492ccb6e3b0aac284415ce87140a22223939
    role: context
  - path: data/habitats/food/cooked_blood.yaml
    sha256: e0a358f58f554a0e652187d63d5399a8f3c36516b0c96d791adbcbe59ae8aa28
    role: context
  - path: data/habitats/food/cooked_fish.yaml
    sha256: 7a1a29ec27659c2d48296a6b09e9d29a48d6c86f4ca48ea2ab2c0bd06c81a4a8
    role: context
  - path: data/habitats/food/cooked_meat.yaml
    sha256: 80e2f39391b2d20f587b21dfc95c1e9fb9b3217c75c7adcfec1758d9389be0bc
    role: context
  - path: data/habitats/food/dairy_food_product.yaml
    sha256: 36c6b5dde12d0d75eca04ac0f91200e839763e14e2ff813ebb85fb7242fb3001
    role: context
  - path: data/habitats/food/egg_products.yaml
    sha256: bb5fcdf9504b49c4163294fbb90685165a091798bf66da0a633bc4419de77a74
    role: context
  - path: data/habitats/food/fermented_dairy_products.yaml
    sha256: 9ed59912b37facdd56bb980f312ad3f131d13a6a604f8294574f94477e889ae4
    role: context
  - path: data/habitats/food/fish_products.yaml
    sha256: 5435e216e51f243842916c2e4199123992c81ab166b0746963ffeee71f5253b3
    role: context
  - path: data/habitats/food/mammalian_meat_food_product.yaml
    sha256: fab8fbd8e3352bfe93aefac2761dded407774e918244be3e6b8a87ae45ec27b5
    role: context
  - path: data/habitats/host_associated/egg.yaml
    sha256: 4442ae82f9df6071c9c46f1f0ce6db9210ed6b836e497ccfbb22525c11ee2781
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
  - path: history/mappings/cheese/2026-10-14T095757Z-codex-gpt-5-78213b.yaml
    sha256: 6b4153ee37290c15aca5f066f991c4a9f87c75fe8c31f92d9142c40e66e28996
    role: context
  - path: history/mappings/cooked_meat/2026-10-14T095758Z-codex-gpt-5-a6b320.yaml
    sha256: 5a6022050f294ca92d740f5bf2fb356aae1712cea5a05b7b400e56fe1ee04719
    role: context
  - path: history/mappings/dairy_food_product/2026-10-14T095759Z-codex-gpt-5-857556.yaml
    sha256: 713d9f40c7aeddef2a7030b6c4d1569a6691aa63fa721ad06ebb61920977121c
    role: context
  - path: history/mappings/egg_food_product/2026-10-14T095800Z-codex-gpt-5-f76776.yaml
    sha256: 5fa3a42ef9295f98e2c07bc1aa4e7ac1f1da6a0ed93a2789422c7631dd9dac32
    role: context
  - path: history/mappings/egg_products/2026-10-14T095801Z-codex-gpt-5-1e0c57.yaml
    sha256: 7d1d265ed407ab60770b12884a8e7c64eb8493b9bd85c662842d9f0ea06a2ac4
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260928T023452Z-fermented_dairy_products.md
    sha256: 97780165ab7bf28e671769c7f4b43d60edb3d5e0d2b96fb7a1143c3a42d5c561
    role: context
  - path: reviews/structured/20261014T095321Z-egg_food_product/review.yaml
    sha256: ee8369f320d49232e42f8a7f393e8156792ee4132dccad7f51761377111b78ee
    role: context
  - path: scripts/aggregate_gold_triads.py
    sha256: 0e25179dbecd7c73cbedd99a0ae44e56e4992afb9e1ec02d2411439f643b8e54
    role: context
  - path: scripts/extract_gold_biosamples.py
    sha256: b6a2773c86fe718e1ca0b1d7b32709f0eee491ac813655e310aa0817c0fec31b
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
  - path: tests/test_food_egg_scope.py
    sha256: 9f6fbc43fef08aa610cecf31d956f83e30d9aeb9b74eebda525b890924ad1ab8
    role: context
  - path: tests/test_food_review_fixes.py
    sha256: bc798ddc7027b09b4300ef507ae62eea8037d25ce0b7a623ef605ec86ef1e94f
    role: context
targets:
- target_id: habitatmech:BACDIVE.d48ce9485d
  path: data/habitats/host_associated/egg.yaml
  label: Egg (BacDive host-product source)
  kind: generated
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input owner; generated records are read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input owner; generated records are read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input owner; generated records are read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Maintained input owner; generated records are read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/bacdive_isolation_sources.tsv
    role: Maintained input owner; generated records are read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/bacdive_source_taxa.tsv
    role: Maintained input owner; generated records are read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Maintained input owner; generated records are read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input owner; generated records are read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input owner; generated records are read-only
- target_id: FOODON:00001274
  path: curation/decisions.tsv
  selector: identifier=habitatmech:BACDIVE.d48ce9485d; former FOODON:00001274 identity
    now rejected by CONFIRM_UNGROUNDED
  label: Former egg-food identity claim retained as a mapping disposition
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input owner; generated records are read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input owner; generated records are read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input owner; generated records are read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Maintained input owner; generated records are read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/bacdive_isolation_sources.tsv
    role: Maintained input owner; generated records are read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/bacdive_source_taxa.tsv
    role: Maintained input owner; generated records are read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Maintained input owner; generated records are read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input owner; generated records are read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input owner; generated records are read-only
scope:
  description: Complete corrected record and exact predecessor finding disposition.
  selection: Explicit source-preserving correction follow-up, not sampling. Includes
    current native record and former ontology identity as a maintained mapping-row
    claim to preserve all predecessor targets.
  coverage: full
  population_size: 2
  reviewed_target_ids:
  - habitatmech:BACDIVE.d48ce9485d
  - FOODON:00001274
evidence:
- evidence_id: CURRENT
  kind: record_content
  reference: data/habitats/host_associated/egg.yaml
  accessed_at: '2026-10-14T10:20:58.127942Z'
  support: supports
  locator: Complete corrected YAML, all source and taxon assertions and history
  summary: BacDive Egg now retains its native source identity and HOST_ASSOCIATED
    coarse category without the false food/vertebrate definition or parent. All 35
    STRAIN-unit source assertions and 25 displayed taxon observations/ranks from the
    30-taxon pool are preserved. Exact-strain evidence supports rejecting the food-only
    mapping; it does not reconstruct all original members or supply a complete egg-associated
    definition. ITEM/REVIEWED is a workflow status, not an exact ontology claim.
- evidence_id: OWNERS
  kind: record_content
  reference: curation/decisions.tsv; curation/gold_parent_exclusions.tsv; tests/test_food_egg_scope.py
  accessed_at: '2026-10-14T10:20:58.127942Z'
  support: supports
  summary: Read the complete maintained rows, five append-only histories and counterfactual
    regression. Full corpus comparison changes only four common records (parent/history)
    and replaces the former food-egg identity with the BacDive source mint. Raw observations
    are unchanged.
  locator: curation/decisions.tsv:1718 identifier=habitatmech:BACDIVE.d48ce9485d
- evidence_id: PREVIOUS
  kind: prior_review
  reference: reviews/structured/20261014T095321Z-egg_food_product/review.yaml
  accessed_at: '2026-10-14T10:20:58.127942Z'
  support: context_only
  summary: Read the immutable predecessor, exact finding, evidence receipts and limitations.
    Its baseline decision rows are historical, not current line references.
- evidence_id: QC
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38547107819
  accessed_at: '2026-10-14T10:20:58.127942Z'
  support: supports
  summary: Verified full hosted QC success on exact corrected commit 0e966aec8a12892973dd15c536f89d90ab0c2c70.
    Initial corrected scientific inputs were rehashed without change after map/site
    publication. New successor bundles still require post-save and final PR checks.
- evidence_id: RULES
  kind: authority
  reference: docs/CURATION.md; docs/HARMONIZATION.md
  summary: Applied strict-superclass, source identity, count-unit, MIxS role, optional-field
    and ITEM status rules from the local record checklist.
  accessed_at: '2026-10-14T09:53:21.461639Z'
  support: supports
- evidence_id: TRANSFORM
  kind: record_content
  reference: src/habitatmech/seed.py; src/habitatmech/extract.py
  summary: GOLD counts outgoing occurrence edges by subject prefix, not proven distinct
    organisms. Bulk biosamples and study path unions are different inventories. BacDive
    aggregate strain_count counts source outgoing edges; taxon associations deduplicate
    strain joins and retain top-25 ranks/candidate_pool. Neither ranking implies characteristic
    presence.
  accessed_at: '2026-10-14T09:53:21.461639Z'
  support: supports
  locator: extract_gold; extract_bacdive; ingest_gold; ingest_bacdive; build_document;
    scripts/extract_gold_biosamples.py; scripts/aggregate_gold_triads.py
- evidence_id: FOODON
  kind: database
  reference: https://raw.githubusercontent.com/FoodOntology/foodon/cd73540243a84bcd511a500d9a497d12d7dc02f6/foodon.owl
  summary: Historical external evidence retained from the predecessor, not a description
    of the corrected record. Read definitions, typed synonyms, active status and direct
    named parents in the pinned official RDF/XML. SHA256 b897bf64c1b265c422db9ee01e1235c10c0b809e7f02326ef810a52068347edf.
    BacDive Egg is not food-only. Exact stored strain NCBITaxon:1122175 (DSM 19883,
    BacDive 7355) comes from an insect egg mass in a waste-stabilization pond and
    is explicitly categorized Host Body Product > Urogenital tract > Egg. Stored strain
    1123347 (DSM 18103, BacDive 5652) comes from halibut egg epiflora. Assigning this
    source to a vertebrate egg food product is a wrong identity; CLOSE and a RELATED
    synonym do not repair it.
  accessed_at: '2026-10-14T09:41:41.574451Z'
  support: supports
  locator: FOODON:00001274; relevant FoodOn parents and candidate context
- evidence_id: AVAILABILITY
  kind: record_content
  reference: conf/sources.yaml
  summary: '{"accessed_at": "2026-10-14T09:44:16.995506Z", "command": ["rg", "--no-ignore",
    "--hidden", "--files", ".", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data"],
    "enumerated_files": 41045, "exit_code": 0, "interpretation": "Ignored files included.
    Bounded to this repository and the configured kg-microbe data root, not all disks.
    No exact original member crosswalk is inferred from inventory presence.", "matches":
    []}'
  accessed_at: '2026-10-14T09:53:21.461639Z'
  support: context_only
- evidence_id: GOLD_ACCESS
  kind: database
  reference: https://gold.jgi.doe.gov/
  summary: 'All 25 retrieved study URLs for this cohort returned HTTP 403; no page
    contents inferred. {"Gs0111397": {"accessed_at": "2026-10-14T09:41:44.844987Z",
    "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0111397"},
    "Gs0117939": {"accessed_at": "2026-10-14T09:41:44.917192Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0117939"}, "Gs0121311":
    {"accessed_at": "2026-10-14T09:41:44.946799Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0121311"}, "Gs0127428": {"accessed_at":
    "2026-10-14T09:41:44.984453Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0127428"},
    "Gs0132999": {"accessed_at": "2026-10-14T09:41:45.015413Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0132999"}, "Gs0133059":
    {"accessed_at": "2026-10-14T09:41:45.135671Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0133059"}, "Gs0133061": {"accessed_at":
    "2026-10-14T09:41:45.168420Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0133061"},
    "Gs0133297": {"accessed_at": "2026-10-14T09:41:45.211877Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0133297"}, "Gs0135057":
    {"accessed_at": "2026-10-14T09:41:45.248222Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0135057"}, "Gs0144921": {"accessed_at":
    "2026-10-14T09:41:45.279258Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0144921"},
    "Gs0144994": {"accessed_at": "2026-10-14T09:41:45.325246Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0144994"}, "Gs0145069":
    {"accessed_at": "2026-10-14T09:41:45.359515Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0145069"}, "Gs0150357": {"accessed_at":
    "2026-10-14T09:41:45.403531Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150357"},
    "Gs0150359": {"accessed_at": "2026-10-14T09:41:45.534775Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150359"}, "Gs0150613":
    {"accessed_at": "2026-10-14T09:41:45.657223Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0150613"}, "Gs0150615": {"accessed_at":
    "2026-10-14T09:41:45.694287Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150615"},
    "Gs0153752": {"accessed_at": "2026-10-14T09:41:45.728601Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153752"}, "Gs0153769":
    {"accessed_at": "2026-10-14T09:41:45.759538Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0153769"}, "Gs0153860": {"accessed_at":
    "2026-10-14T09:41:45.793390Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153860"},
    "Gs0153898": {"accessed_at": "2026-10-14T09:41:45.825210Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153898"}, "Gs0154236":
    {"accessed_at": "2026-10-14T09:41:45.874324Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0154236"}, "Gs0154282": {"accessed_at":
    "2026-10-14T09:41:45.906640Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154282"},
    "Gs0156793": {"accessed_at": "2026-10-14T09:41:45.940030Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0156793"}, "Gs0159152":
    {"accessed_at": "2026-10-14T09:41:45.985158Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0159152"}, "Gs0161780": {"accessed_at":
    "2026-10-14T09:41:46.016628Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0161780"}}'
  accessed_at: '2026-10-14T09:53:21.461639Z'
  support: context_only
- evidence_id: TAXONOMY
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&retmode=xml&id=33036,109790,216816,2702,1114867,1121116,1122175,1123347,1215111,1340529,1352,1381081,1470200,147802,1596,1682,2051,2098,28125,28229,293,294,306,358592,37734
  summary: 'All 25 requested taxon IDs resolve with exact stored names; no current
    label drift. SHA256 613cc4284e20254d01236af61d16c68803e9ef5babb1070ec0e2c3c433f2a5c2.
    [{"current": {"identifier": "33036", "name": "Anaerococcus tetradius", "names":
    ["Gaffkya anaerobius", "Peptostreptococcus tetradius", "Tetracoccus anaerobius"],
    "rank": "species"}, "stored": {"association_count": 3, "candidate_pool": 30, "rank":
    1, "source": "BACDIVE", "taxon_id": "NCBITaxon:33036", "taxon_label": "Anaerococcus
    tetradius"}}, {"current": {"identifier": "109790", "name": "Lactobacillus jensenii",
    "names": [], "rank": "species"}, "stored": {"association_count": 2, "candidate_pool":
    30, "rank": 2, "source": "BACDIVE", "taxon_id": "NCBITaxon:109790", "taxon_label":
    "Lactobacillus jensenii"}}, {"current": {"identifier": "216816", "name": "Bifidobacterium
    longum", "names": ["Bifidobacterium sp. 12_1_47BFAA"], "rank": "species"}, "stored":
    {"association_count": 2, "candidate_pool": 30, "rank": 3, "source": "BACDIVE",
    "taxon_id": "NCBITaxon:216816", "taxon_label": "Bifidobacterium longum"}}, {"current":
    {"identifier": "2702", "name": "Gardnerella vaginalis", "names": ["Corynebacterium
    vaginale", "Gardnerella vaginalis (Gardner and Dukes 1955) Greenwood and Pickett
    1980", "Haemophilus hemolyticus vaginalis", "Haemophilus vaginalis", "Gardnerella
    genomic species 1", "s__Bifidobacterium vaginale"], "rank": "species"}, "stored":
    {"association_count": 2, "candidate_pool": 30, "rank": 4, "source": "BACDIVE",
    "taxon_id": "NCBITaxon:2702", "taxon_label": "Gardnerella vaginalis"}}, {"current":
    {"identifier": "1114867", "name": "Flavobacterium plurextorum", "names": ["Flavobacterium
    sp. 1084B-08", "Flavobacterium sp. 1126-1H-08", "Flavobacterium sp. 424-08", "Flavobacterium
    sp. 51B-09", "Flavobacterium sp. 986-08"], "rank": "species"}, "stored": {"association_count":
    1, "candidate_pool": 30, "rank": 5, "source": "BACDIVE", "taxon_id": "NCBITaxon:1114867",
    "taxon_label": "Flavobacterium plurextorum"}}, {"current": {"identifier": "1121116",
    "name": "Allobrachymonas chironomi DSM 19884", "names": ["Allobrachymonas sp.
    AImA4"], "rank": "strain"}, "stored": {"association_count": 1, "candidate_pool":
    30, "rank": 6, "source": "BACDIVE", "taxon_id": "NCBITaxon:1121116", "taxon_label":
    "Allobrachymonas chironomi DSM 19884"}}, {"current": {"identifier": "1122175",
    "name": "Leucobacter chironomi DSM 19883", "names": [], "rank": "strain"}, "stored":
    {"association_count": 1, "candidate_pool": 30, "rank": 7, "source": "BACDIVE",
    "taxon_id": "NCBITaxon:1122175", "taxon_label": "Leucobacter chironomi DSM 19883"}},
    {"current": {"identifier": "1123347", "name": "Tenacibaculum ovolyticum DSM 18103",
    "names": [], "rank": "strain"}, "stored": {"association_count": 1, "candidate_pool":
    30, "rank": 8, "source": "BACDIVE", "taxon_id": "NCBITaxon:1123347", "taxon_label":
    "Tenacibaculum ovolyticum DSM 18103"}}, {"current": {"identifier": "1215111",
    "name": "Pseudomonas mucidolens NBRC 103159", "names": [], "rank": "strain"},
    "stored": {"association_count": 1, "candidate_pool": 30, "rank": 9, "source":
    "BACDIVE", "taxon_id": "NCBITaxon:1215111", "taxon_label": "Pseudomonas mucidolens
    NBRC 103159"}}, {"current": {"identifier": "1340529", "name": "Photobacterium
    panuliri", "names": ["Photobacterium panuliri Deep et al. 2015", "Photobacterium
    sp. LBS5"], "rank": "species"}, "stored": {"association_count": 1, "candidate_pool":
    30, "rank": 10, "source": "BACDIVE", "taxon_id": "NCBITaxon:1340529", "taxon_label":
    "Photobacterium panuliri"}}, {"current": {"identifier": "1352", "name": "Enterococcus
    faecium", "names": ["Streptococcus faecium", "Enterococcus sp. LMG 19843"], "rank":
    "species"}, "stored": {"association_count": 1, "candidate_pool": 30, "rank": 11,
    "source": "BACDIVE", "taxon_id": "NCBITaxon:1352", "taxon_label": "Enterococcus
    faecium"}}, {"current": {"identifier": "1381081", "name": "Vibrio panuliri", "names":
    ["Vibrio sp. CAIM 703", "Vibrio sp. LBS2"], "rank": "species"}, "stored": {"association_count":
    1, "candidate_pool": 30, "rank": 12, "source": "BACDIVE", "taxon_id": "NCBITaxon:1381081",
    "taxon_label": "Vibrio panuliri"}}, {"current": {"identifier": "1470200", "name":
    "Neisseria arctica", "names": ["Neisseria sp. KH1479", "Neisseria sp. KH1503",
    "Neisseria sp. KH1705", "Neisseria sp. KH1744", "Neisseria sp. KH2123", "Neisseria
    sp. KH2164"], "rank": "species"}, "stored": {"association_count": 1, "candidate_pool":
    30, "rank": 13, "source": "BACDIVE", "taxon_id": "NCBITaxon:1470200", "taxon_label":
    "Neisseria arctica"}}, {"current": {"identifier": "147802", "name": "Lactobacillus
    iners", "names": ["Lactobacillus sp. EF (Enevold Falsen) group 47", "Lactobacillus
    sp. 7_1_47FAA"], "rank": "species"}, "stored": {"association_count": 1, "candidate_pool":
    30, "rank": 14, "source": "BACDIVE", "taxon_id": "NCBITaxon:147802", "taxon_label":
    "Lactobacillus iners"}}, {"current": {"identifier": "1596", "name": "Lactobacillus
    gasseri", "names": ["Lactobacillus sp. JCM 1131"], "rank": "species"}, "stored":
    {"association_count": 1, "candidate_pool": 30, "rank": 15, "source": "BACDIVE",
    "taxon_id": "NCBITaxon:1596", "taxon_label": "Lactobacillus gasseri"}}, {"current":
    {"identifier": "1682", "name": "Bifidobacterium longum subsp. infantis", "names":
    ["Bifidobacterium lactentis", "Bifidobacterium liberorum", "Bifidobacterium longum
    bv. Infantis", "Bifidobacterium longum infantis"], "rank": "subspecies"}, "stored":
    {"association_count": 1, "candidate_pool": 30, "rank": 16, "source": "BACDIVE",
    "taxon_id": "NCBITaxon:1682", "taxon_label": "Bifidobacterium longum subsp. infantis"}},
    {"current": {"identifier": "2051", "name": "Mobiluncus curtisii", "names": ["Falcivibrio
    vaginalis"], "rank": "species"}, "stored": {"association_count": 1, "candidate_pool":
    30, "rank": 17, "source": "BACDIVE", "taxon_id": "NCBITaxon:2051", "taxon_label":
    "Mobiluncus curtisii"}}, {"current": {"identifier": "2098", "name": "Metamycoplasma
    hominis", "names": ["Asterococcus hominis", "Micromyces hominis", "Mycoplasma
    hominis (Freundt 1953) Edward 1955 (Approved Lists 1980)"], "rank": "species"},
    "stored": {"association_count": 1, "candidate_pool": 30, "rank": 18, "source":
    "BACDIVE", "taxon_id": "NCBITaxon:2098", "taxon_label": "Metamycoplasma hominis"}},
    {"current": {"identifier": "28125", "name": "Prevotella bivia", "names": ["Bacteroides
    bivius"], "rank": "species"}, "stored": {"association_count": 1, "candidate_pool":
    30, "rank": 19, "source": "BACDIVE", "taxon_id": "NCBITaxon:28125", "taxon_label":
    "Prevotella bivia"}}, {"current": {"identifier": "28229", "name": "Colwellia psychrerythraea",
    "names": ["Colwellia psychroerythrus", "Vibrio psychroerythrus", "Vibrio psychroerythus",
    "Colwellia psychroerythraea", "Colwellia psychroerythrea", "Vibrio psychroerythreus"],
    "rank": "species"}, "stored": {"association_count": 1, "candidate_pool": 30, "rank":
    20, "source": "BACDIVE", "taxon_id": "NCBITaxon:28229", "taxon_label": "Colwellia
    psychrerythraea"}}, {"current": {"identifier": "293", "name": "Brevundimonas diminuta",
    "names": ["Bacterium parvulum", "Pseudomonas diminuta"], "rank": "species"}, "stored":
    {"association_count": 1, "candidate_pool": 30, "rank": 21, "source": "BACDIVE",
    "taxon_id": "NCBITaxon:293", "taxon_label": "Brevundimonas diminuta"}}, {"current":
    {"identifier": "294", "name": "Pseudomonas fluorescens", "names": ["Bacillus fluorescens",
    "Bacillus fluorescens liquefaciens", "Bacterium fluorescen", "Liquidomonas fluorescens",
    "Pseudomonas sp. AU2390", "Pseudomonas sp. BZ64", "Pseudomonas sp. FY32", "Pseudomonas
    sp. HSA2/2016", "Pseudomonas sp. HSA3/2016", "Pseudomonas sp. ISSDS-433", "Pseudomonas
    sp. JCM 17186", "Pseudomonas sp. JCM 2779", "Pseudomonas sp. KH-20150KS3", "Pseudomonas
    sp. LBUM223", "Pseudomonas sp. LBUM636", "Pseudomonas sp. SM2/2016", "bacterium
    P1-1"], "rank": "species"}, "stored": {"association_count": 1, "candidate_pool":
    30, "rank": 22, "source": "BACDIVE", "taxon_id": "NCBITaxon:294", "taxon_label":
    "Pseudomonas fluorescens"}}, {"current": {"identifier": "306", "name": "Pseudomonas
    sp.", "names": ["Achromobacter georgiopolitanum"], "rank": "species"}, "stored":
    {"association_count": 1, "candidate_pool": 30, "rank": 23, "source": "BACDIVE",
    "taxon_id": "NCBITaxon:306", "taxon_label": "Pseudomonas sp."}}, {"current": {"identifier":
    "358592", "name": "Rheinheimera chironomi", "names": ["Pararheinheimera chironomi",
    "chironomid egg mass bacterium K19414"], "rank": "species"}, "stored": {"association_count":
    1, "candidate_pool": 30, "rank": 24, "source": "BACDIVE", "taxon_id": "NCBITaxon:358592",
    "taxon_label": "Rheinheimera chironomi"}}, {"current": {"identifier": "37734",
    "name": "Enterococcus casseliflavus", "names": ["Enterococcus flavescens", "Streptococcus
    casseliflavus", "Streptococcus faecium subsp. casseliflavus", "Streptococcus faecium
    var. casseliflavus", "Streptococcus flavescens", "Enterococcus sp. LMG 12310",
    "Enterococcus sp. VTT E-96690"], "rank": "species"}, "stored": {"association_count":
    1, "candidate_pool": 30, "rank": 25, "source": "BACDIVE", "taxon_id": "NCBITaxon:37734",
    "taxon_label": "Enterococcus casseliflavus"}}]'
  accessed_at: '2026-10-14T09:41:38.246876Z'
  support: supports
  locator: All characteristic_taxa entries
- evidence_id: BACDIVE-7355
  kind: database
  reference: https://bacdive.dsmz.de/strain/7355
  summary: 'Exact type strain DSM 19883 / taxid 1122175: chironomid egg mass from
    Tivon waste-stabilization pond. Isolation categories include Host Body Product
    > Urogenital tract > Egg and Host > Arthropoda > Insecta. This refutes food-only
    and vertebrate-only source scope. SHA256 026b7ba7c9046c6b2a10e89903dca1f13c3719bc1d456b26f946f6a6e9612c41'
  accessed_at: '2026-10-14T09:44:20.348670Z'
  support: refutes
  locator: Names and IDs; Isolation source categories; Isolation
- evidence_id: BACDIVE-5652
  kind: database
  reference: https://bacdive.dsmz.de/strain/5652
  summary: 'Exact type strain DSM 18103 / taxid 1123347: Atlantic halibut egg epiflora.
    Isolation category Host Body Product > Urogenital tract > Egg establishes a host-product
    category, not a food-only vocabulary branch. SHA256 5023563ccb6f2266e9257d30ade74a4ce4e5a1369c8886d4896311b5ab083fb3'
  accessed_at: '2026-10-14T09:44:21.740503Z'
  support: refutes
  locator: Names and IDs; Isolation source categories; Isolation
- evidence_id: RAW
  kind: prior_review
  reference: reviews/structured/20261014T095321Z-egg_food_product/review.yaml
  locator: evidence_id=RAW; assessments SCIENCE
  accessed_at: '2026-10-14T10:20:58.127942Z'
  support: context_only
  summary: Frozen source tables are byte-unchanged; baseline curation rows are superseded
    by OWNERS. BacDive isolation row 105 carries 35 STRAIN-unit source assertions
    and a 30-taxon candidate pool; mapping row 99 supplies a medium-confidence lexical
    closeMatch. ITEM decision row 1718 wrongly asserts that this vocabulary branch
    consists of foods. All 25 displayed taxon IDs and names resolve in fresh NCBI
    taxonomy; ranks/counts follow the frozen join, not prevalence or characteristic
    presence. The 25 rows sum to 30 associations, not 35 distinct organisms; five
    candidate taxa are not displayed. Two exact-strain witnesses refute food-only
    scope but do not reconstruct all 35 frozen source members.
checks:
- check_id: C3
  name: just validate
  status: passed
  required: true
  target_ids:
  - habitatmech:BACDIVE.d48ce9485d
  - FOODON:00001274
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/egg.yaml
  exit_code: 0
  summary: Executed 2026-10-14T10:02:24.768716Z to 2026-10-14T10:02:27.124209Z. No
    issues found
- check_id: C5
  name: just validate-strict
  status: passed
  required: true
  target_ids:
  - habitatmech:BACDIVE.d48ce9485d
  - FOODON:00001274
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/food/cheese.yaml data/habitats/food/cooked_meat.yaml data/habitats/food/dairy_food_product.yaml
    data/habitats/host_associated/egg.yaml data/habitats/food/egg_products.yaml
  exit_code: 0
  summary: "Executed 2026-10-14T10:02:29.375588Z to 2026-10-14T10:02:34.192584Z. uv\
    \ run python scripts/validate_strict.py data/habitats/food/cheese.yaml data/habitats/food/cooked_meat.yaml\
    \ data/habitats/food/dairy_food_product.yaml data/habitats/host_associated/egg.yaml\
    \ data/habitats/food/egg_products.yaml\nValidating 5 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      5\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
- check_id: C6
  name: just validate-history
  status: passed
  required: true
  target_ids:
  - habitatmech:BACDIVE.d48ce9485d
  - FOODON:00001274
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  summary: 'Executed 2026-10-14T10:02:34.193195Z to 2026-10-14T10:02:41.329829Z. No
    issues found

    659 history record(s) valid against src/habitatmech/schema/history.yaml'
- check_id: C7
  name: just provenance-check
  status: passed
  required: true
  target_ids:
  - habitatmech:BACDIVE.d48ce9485d
  - FOODON:00001274
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  summary: 'Executed 2026-10-14T10:02:41.330400Z to 2026-10-14T10:02:41.842199Z. provenance
    current: 14 committed inventories, 2 GOLD sources'
- check_id: C8
  name: just verify-corpus
  status: passed
  required: true
  target_ids:
  - habitatmech:BACDIVE.d48ce9485d
  - FOODON:00001274
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  summary: "Executed 2026-10-14T10:02:41.842688Z to 2026-10-14T10:02:57.759857Z. expected\
    \ 3208 records, found 3208 on disk\n  missing:   0\n  extra:     0\n  differing:\
    \ 0\n\ncorpus reproduces exactly from data/raw/"
- check_id: C9
  name: just validate-causal-all
  status: passed
  required: true
  target_ids:
  - habitatmech:BACDIVE.d48ce9485d
  - FOODON:00001274
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  summary: Executed 2026-10-14T10:02:57.760640Z to 2026-10-14T10:03:01.979292Z. validated
    32 causal-graph curation file(s) with 32 graph(s)
- check_id: C10
  name: just term-requests-check
  status: passed
  required: true
  target_ids:
  - habitatmech:BACDIVE.d48ce9485d
  - FOODON:00001274
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  summary: Executed 2026-10-14T10:03:01.979839Z to 2026-10-14T10:03:17.947037Z. term-request
    table is current (109 terms)
- check_id: C11
  name: just validate-products
  status: passed
  required: true
  target_ids:
  - habitatmech:BACDIVE.d48ce9485d
  - FOODON:00001274
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  summary: "Executed 2026-10-14T10:03:17.947566Z to 2026-10-14T10:04:03.215199Z. id↔label\
    \ correspondence summary:\n          OK_CANONICAL: 1176\n            OK_SYNONYM:\
    \ 1\n          OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2059\n\n✅ All id↔label\
    \ pairs correspond."
- check_id: C12
  name: uv run
  status: passed
  required: true
  target_ids:
  - habitatmech:BACDIVE.d48ce9485d
  - FOODON:00001274
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache uv run pytest -q tests/test_food_egg_scope.py
    tests/test_food_review_fixes.py tests/test_gold_parent_exclusions.py tests/test_ontology_labels.py
  exit_code: 0
  summary: 'Executed 2026-10-14T10:04:03.215881Z to 2026-10-14T10:05:25.219804Z. ........................................................................
    [ 80%]

    ..................                                                       [100%]

    90 passed in 81.08s (0:01:21)'
- check_id: C13
  name: uv run
  status: passed
  required: true
  target_ids:
  - habitatmech:BACDIVE.d48ce9485d
  - FOODON:00001274
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache uv run ruff check .
  exit_code: 0
  summary: Executed 2026-10-14T10:05:25.220422Z to 2026-10-14T10:05:25.351468Z. All
    checks passed!
- check_id: QC
  name: Exact corrected-base hosted authoritative QC
  status: passed
  required: true
  target_ids:
  - habitatmech:BACDIVE.d48ce9485d
  - FOODON:00001274
  command: gh run view 38547107819 --json headSha,status,conclusion,url
  exit_code: 0
  summary: Verified success on the captured corrected base. Post-save archive and
    final PR checks remain required.
  evidence_ids:
  - QC
- check_id: MEMBERS
  name: Original source-member reconstruction
  status: unavailable
  required: false
  target_ids:
  - habitatmech:BACDIVE.d48ce9485d
  - FOODON:00001274
  summary: Original source dumps/member crosswalks remain unavailable; predecessor
    GOLD access returned 403. No new access success or complete membership claim.
  evidence_ids:
  - AVAILABILITY
  - GOLD_ACCESS
- check_id: IMODULON
  name: Expression-source applicability
  status: not_applicable
  required: false
  target_ids:
  - habitatmech:BACDIVE.d48ce9485d
  - FOODON:00001274
  summary: No gene, regulator, protein or transcriptomics assertion. Habitat source
    identity is not expression-module evidence.
assessments:
- assessment_id: FIX
  area: grounding
  topic: Identity, parent correction and exact finding disposition
  outcome: supported
  target_ids:
  - habitatmech:BACDIVE.d48ce9485d
  - FOODON:00001274
  evidence_ids:
  - CURRENT
  - OWNERS
  - PREVIOUS
  - QC
  - RULES
  - FOODON
  - TAXONOMY
  - BACDIVE-7355
  - BACDIVE-5652
  summary: BacDive Egg now retains its native source identity and HOST_ASSOCIATED
    coarse category without the false food/vertebrate definition or parent. All 35
    STRAIN-unit source assertions and 25 displayed taxon observations/ranks from the
    30-taxon pool are preserved. Exact-strain evidence supports rejecting the food-only
    mapping; it does not reconstruct all original members or supply a complete egg-associated
    definition. ITEM/REVIEWED is a workflow status, not an exact ontology claim.
- assessment_id: SCIENCE
  area: evidence
  topic: Source scope, counts, rank semantics and optional claims
  outcome: supported
  target_ids:
  - habitatmech:BACDIVE.d48ce9485d
  - FOODON:00001274
  evidence_ids:
  - CURRENT
  - RAW
  - TRANSFORM
  - OWNERS
  - TAXONOMY
  - BACDIVE-7355
  - BACDIVE-5652
  summary: Re-read the entire current record. Source assertions remain distinct from
    bulk biosamples and complete-triad samples. No new environmental parameter, causal
    graph, citation, discussion or dataset assertion is introduced. All 25 taxonomy
    IDs/names remain verified against the predecessor NCBI receipt; counts/ranks/candidate
    pool are observational, not characteristic presence. The new source mint has no
    fabricated definition or exact ontology synonym. Native history is regenerated
    for the corrected identity; the rejected former endorsement remains in Git and
    the predecessor, not in the new record as an active decision.
findings:
- finding_id: F1
  issue_key: bacdive-egg-food-only-identity
  category: grounding
  severity: blocker
  status: resolved
  certainty: confirmed
  title: Host egg source is assigned a vertebrate food-product identity
  description: BacDive Egg is not food-only. Exact stored strain NCBITaxon:1122175
    (DSM 19883, BacDive 7355) comes from an insect egg mass in a waste-stabilization
    pond and is explicitly categorized Host Body Product > Urogenital tract > Egg.
    Stored strain 1123347 (DSM 18103, BacDive 5652) comes from halibut egg epiflora.
    Assigning this source to a vertebrate egg food product is a wrong identity; CLOSE
    and a RELATED synonym do not repair it.
  target_ids:
  - habitatmech:BACDIVE.d48ce9485d
  - FOODON:00001274
  field_paths:
  - identifier
  - definition
  - habitat_category
  - grounding_status
  - parent_habitats
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input owner; generated records are read-only
  evidence_ids:
  - CURRENT
  - OWNERS
  - PREVIOUS
  - QC
  - RULES
  - FOODON
  - TAXONOMY
  - BACDIVE-7355
  - BACDIVE-5652
  rule_id: 'docs/CURATION.md: identity and strict parent rules'
  native_severity: blocker
  normalization_reason: Wrong food/vertebrate identity denotes the wrong thing.
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261014T095321Z-egg_food_product
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2051
  disposition_reason: BacDive Egg now retains its native source identity and HOST_ASSOCIATED
    coarse category without the false food/vertebrate definition or parent. All 35
    STRAIN-unit source assertions and 25 displayed taxon observations/ranks from the
    30-taxon pool are preserved. Exact-strain evidence supports rejecting the food-only
    mapping; it does not reconstruct all original members or supply a complete egg-associated
    definition. ITEM/REVIEWED is a workflow status, not an exact ontology claim.
actions: []
limitations:
- Same-agent review and adversarial pass, not independent approval.
- Original source membership remains unavailable. Cheese source identity versus fermentation
  context and fuller egg-source scope are not resolved by bounded corrections.
- No latest-ontology refresh or SSSOM/KGX conformance certification. Native label
  checks retain configured exceptions and unsupported-prefix skips.
- Only exact predecessor findings receive the shown dispositions; adjacent Fish products,
  Meat products and Fermented dairy products records are not silently curated.
- Corrected-base full QC predates new successor bundles; post-save archive and final
  publication gates remain required.
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261014T095321Z-egg_food_product
  relationship: Exact immutable predecessor finding reassessed without rewriting its
    report.
notes:
- Initial corrected capture at 09bb13f857d3e634f4a8cb295d7b847b10612a4b; reinspection
  after map/site publication proved every scientific input hash unchanged before recording
  the final corrected base. The explicit empty-target relation default is semantically
  inactive and was captured before this review.
tags:
- habitatmech
- record-review
- food
- followup
```
