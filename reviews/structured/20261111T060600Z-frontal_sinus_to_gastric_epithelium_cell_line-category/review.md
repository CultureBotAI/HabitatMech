# Category cohort review: host_associated slice frontal_sinus through gastric_epithelium_cell_line (24 records)

- Review: 20261111T060600Z-frontal_sinus_to_gastric_epithelium_cell_line-category
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-11T05:35:00Z
- Finished UTC: 2026-11-11T06:06:00Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Full 24-record category boundary and cohort review of the contiguous unreviewed host_associated slice (frontal_sinus.yaml through gastric_epithelium_cell_line.yaml) at commit 83aa5f212521389cb9c3507ded58d0bcd0a22ee0. All 24 records represent distinct paranasal-sinus, frozen-remains, plant fruit/juice/gall/gametophyte, fungal fruiting-body/endosymbiont/host-environment, gallbladder/gallstone, hymenopteran gaster, insect gastric-caeca, and human cyst/carcinoma/gastric-epithelium source concepts (retain decisions; no cross-record lumping or splitting). Record-level open findings (17 total across 11 records) are recorded in the 24 linked kind: record bundles for Stage 5 remediation.

## Scope And Provenance

Contiguous 24-record cohort boundary review of previously unreviewed records in data/habitats/host_associated/ (indices 554-577 in path order).

Selection: Next 24 unreviewed records in data/habitats/host_associated/ immediately following 20261109T181033Z-free_living_state-record.
Coverage: full; 24 reviewed / 24 in the declared population.
Source: git_commit at Git base 83aa5f212521389cb9c3507ded58d0bcd0a22ee0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| UBERON:0001760 | data/habitats/host_associated/frontal_sinus.yaml | generated | frontal sinus |
| habitatmech:GOLD.112979e260 | data/habitats/host_associated/frozen_remains.yaml | generated | frozen avian remains |
| habitatmech:GOLD.4be243a2b8 | data/habitats/host_associated/frozen_remains__584db35c.yaml | generated | frozen human remains |
| habitatmech:GOLD.7e21c19f98 | data/habitats/host_associated/frozen_remains__aa25d597.yaml | generated | frozen fish remains |
| BTO:0000486 | data/habitats/host_associated/fruit.yaml | generated | fruit |
| BTO:0004057 | data/habitats/host_associated/fruit_juice.yaml | generated | fruit juice |
| habitatmech:GOLD.92cbc36828 | data/habitats/host_associated/fruiting_body.yaml | generated | fungal fruiting body |
| habitatmech:GOLD.1ab59245f7 | data/habitats/host_associated/fungi.yaml | generated | Fungi |
| ENVO:01001041 | data/habitats/host_associated/fungi_associated_environment.yaml | generated | fungi-associated environment |
| BTO:0004108 | data/habitats/host_associated/g_cell.yaml | generated | G cell |
| BTO:0000493 | data/habitats/host_associated/gall_bladder.yaml | generated | gall bladder |
| habitatmech:GOLD.0ec3770763 | data/habitats/host_associated/gallbladder.yaml | generated | Gallbladder |
| habitatmech:GOLD.a84ac69a45 | data/habitats/host_associated/gallbladder__d157697c.yaml | generated | Gallbladder |
| habitatmech:GOLD.7c37c0e048 | data/habitats/host_associated/gallbladder_stones.yaml | generated | mammalian gallstone |
| habitatmech:GOLD.97738241e1 | data/habitats/host_associated/gallbladder_stones__a31ee838.yaml | generated | human gallstone |
| habitatmech:GOLD.fa99e76de1 | data/habitats/host_associated/galls.yaml | generated | Galls |
| BTO:0000495 | data/habitats/host_associated/gametophyte.yaml | generated | gametophyte |
| UBERON:0000045 | data/habitats/host_associated/ganglion.yaml | generated | ganglion |
| habitatmech:GOLD.623ff8e506 | data/habitats/host_associated/gaster.yaml | generated | gaster environment |
| habitatmech:GOLD.8f1269c14c | data/habitats/host_associated/gastric_caeca.yaml | generated | insect midgut gastric cecum |
| habitatmech:GOLD.ace43986bc | data/habitats/host_associated/gastric_caeca__12108999.yaml | generated | insect larval gastric caecum |
| habitatmech:GOLD.85aabc4062 | data/habitats/host_associated/gastric_carcinoma.yaml | generated | Gastric carcinoma |
| BTO:0000500 | data/habitats/host_associated/gastric_epithelium.yaml | generated | gastric epithelium |
| BTO:0004493 | data/habitats/host_associated/gastric_epithelium_cell_line.yaml | generated | gastric epithelium cell line |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | UBERON:0001760, habitatmech:GOLD.112979e260, habitatmech:GOLD.4be243a2b8, habitatmech:GOLD.7e21c19f98, BTO:0000486, BTO:0004057, habitatmech:GOLD.92cbc36828, habitatmech:GOLD.1ab59245f7, ENVO:01001041, BTO:0004108, BTO:0000493, habitatmech:GOLD.0ec3770763, habitatmech:GOLD.a84ac69a45, habitatmech:GOLD.7c37c0e048, habitatmech:GOLD.97738241e1, habitatmech:GOLD.fa99e76de1, BTO:0000495, UBERON:0000045, habitatmech:GOLD.623ff8e506, habitatmech:GOLD.8f1269c14c, habitatmech:GOLD.ace43986bc, habitatmech:GOLD.85aabc4062, BTO:0000500, BTO:0004493 | Completed 2026-11-11T05:58:55Z. No issues found. |
| validate-strict | passed | True | UBERON:0001760, habitatmech:GOLD.112979e260, habitatmech:GOLD.4be243a2b8, habitatmech:GOLD.7e21c19f98, BTO:0000486, BTO:0004057, habitatmech:GOLD.92cbc36828, habitatmech:GOLD.1ab59245f7, ENVO:01001041, BTO:0004108, BTO:0000493, habitatmech:GOLD.0ec3770763, habitatmech:GOLD.a84ac69a45, habitatmech:GOLD.7c37c0e048, habitatmech:GOLD.97738241e1, habitatmech:GOLD.fa99e76de1, BTO:0000495, UBERON:0000045, habitatmech:GOLD.623ff8e506, habitatmech:GOLD.8f1269c14c, habitatmech:GOLD.ace43986bc, habitatmech:GOLD.85aabc4062, BTO:0000500, BTO:0004493 | Completed 2026-11-11T05:59:01Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | UBERON:0001760, habitatmech:GOLD.112979e260, habitatmech:GOLD.4be243a2b8, habitatmech:GOLD.7e21c19f98, BTO:0000486, BTO:0004057, habitatmech:GOLD.92cbc36828, habitatmech:GOLD.1ab59245f7, ENVO:01001041, BTO:0004108, BTO:0000493, habitatmech:GOLD.0ec3770763, habitatmech:GOLD.a84ac69a45, habitatmech:GOLD.7c37c0e048, habitatmech:GOLD.97738241e1, habitatmech:GOLD.fa99e76de1, BTO:0000495, UBERON:0000045, habitatmech:GOLD.623ff8e506, habitatmech:GOLD.8f1269c14c, habitatmech:GOLD.ace43986bc, habitatmech:GOLD.85aabc4062, BTO:0000500, BTO:0004493 | Completed 2026-11-11T05:59:08Z. No issues found; 881 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | UBERON:0001760, habitatmech:GOLD.112979e260, habitatmech:GOLD.4be243a2b8, habitatmech:GOLD.7e21c19f98, BTO:0000486, BTO:0004057, habitatmech:GOLD.92cbc36828, habitatmech:GOLD.1ab59245f7, ENVO:01001041, BTO:0004108, BTO:0000493, habitatmech:GOLD.0ec3770763, habitatmech:GOLD.a84ac69a45, habitatmech:GOLD.7c37c0e048, habitatmech:GOLD.97738241e1, habitatmech:GOLD.fa99e76de1, BTO:0000495, UBERON:0000045, habitatmech:GOLD.623ff8e506, habitatmech:GOLD.8f1269c14c, habitatmech:GOLD.ace43986bc, habitatmech:GOLD.85aabc4062, BTO:0000500, BTO:0004493 | Completed 2026-11-11T05:59:09Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | UBERON:0001760, habitatmech:GOLD.112979e260, habitatmech:GOLD.4be243a2b8, habitatmech:GOLD.7e21c19f98, BTO:0000486, BTO:0004057, habitatmech:GOLD.92cbc36828, habitatmech:GOLD.1ab59245f7, ENVO:01001041, BTO:0004108, BTO:0000493, habitatmech:GOLD.0ec3770763, habitatmech:GOLD.a84ac69a45, habitatmech:GOLD.7c37c0e048, habitatmech:GOLD.97738241e1, habitatmech:GOLD.fa99e76de1, BTO:0000495, UBERON:0000045, habitatmech:GOLD.623ff8e506, habitatmech:GOLD.8f1269c14c, habitatmech:GOLD.ace43986bc, habitatmech:GOLD.85aabc4062, BTO:0000500, BTO:0004493 | Completed 2026-11-11T05:59:26Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | UBERON:0001760, habitatmech:GOLD.112979e260, habitatmech:GOLD.4be243a2b8, habitatmech:GOLD.7e21c19f98, BTO:0000486, BTO:0004057, habitatmech:GOLD.92cbc36828, habitatmech:GOLD.1ab59245f7, ENVO:01001041, BTO:0004108, BTO:0000493, habitatmech:GOLD.0ec3770763, habitatmech:GOLD.a84ac69a45, habitatmech:GOLD.7c37c0e048, habitatmech:GOLD.97738241e1, habitatmech:GOLD.fa99e76de1, BTO:0000495, UBERON:0000045, habitatmech:GOLD.623ff8e506, habitatmech:GOLD.8f1269c14c, habitatmech:GOLD.ace43986bc, habitatmech:GOLD.85aabc4062, BTO:0000500, BTO:0004493 | Completed 2026-11-11T05:59:32Z. validated 113 causal-graph curation file(s) with 113 graph(s). |
| term-requests-check | passed | True | UBERON:0001760, habitatmech:GOLD.112979e260, habitatmech:GOLD.4be243a2b8, habitatmech:GOLD.7e21c19f98, BTO:0000486, BTO:0004057, habitatmech:GOLD.92cbc36828, habitatmech:GOLD.1ab59245f7, ENVO:01001041, BTO:0004108, BTO:0000493, habitatmech:GOLD.0ec3770763, habitatmech:GOLD.a84ac69a45, habitatmech:GOLD.7c37c0e048, habitatmech:GOLD.97738241e1, habitatmech:GOLD.fa99e76de1, BTO:0000495, UBERON:0000045, habitatmech:GOLD.623ff8e506, habitatmech:GOLD.8f1269c14c, habitatmech:GOLD.ace43986bc, habitatmech:GOLD.85aabc4062, BTO:0000500, BTO:0004493 | Completed 2026-11-11T05:59:47Z. term-request table is current (676 terms). |
| validate-products | passed | True | UBERON:0001760, habitatmech:GOLD.112979e260, habitatmech:GOLD.4be243a2b8, habitatmech:GOLD.7e21c19f98, BTO:0000486, BTO:0004057, habitatmech:GOLD.92cbc36828, habitatmech:GOLD.1ab59245f7, ENVO:01001041, BTO:0004108, BTO:0000493, habitatmech:GOLD.0ec3770763, habitatmech:GOLD.a84ac69a45, habitatmech:GOLD.7c37c0e048, habitatmech:GOLD.97738241e1, habitatmech:GOLD.fa99e76de1, BTO:0000495, UBERON:0000045, habitatmech:GOLD.623ff8e506, habitatmech:GOLD.8f1269c14c, habitatmech:GOLD.ace43986bc, habitatmech:GOLD.85aabc4062, BTO:0000500, BTO:0004493 | Completed 2026-11-11T06:00:30Z. OK_CANONICAL: 1211, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2106. All id&lt;-&gt;label pairs correspond. |

## Scientific And Domain Assessments

### Native validity and reproduction

schema: supported. Targets: UBERON:0001760, habitatmech:GOLD.112979e260, habitatmech:GOLD.4be243a2b8, habitatmech:GOLD.7e21c19f98, BTO:0000486, BTO:0004057, habitatmech:GOLD.92cbc36828, habitatmech:GOLD.1ab59245f7, ENVO:01001041, BTO:0004108, BTO:0000493, habitatmech:GOLD.0ec3770763, habitatmech:GOLD.a84ac69a45, habitatmech:GOLD.7c37c0e048, habitatmech:GOLD.97738241e1, habitatmech:GOLD.fa99e76de1, BTO:0000495, UBERON:0000045, habitatmech:GOLD.623ff8e506, habitatmech:GOLD.8f1269c14c, habitatmech:GOLD.ace43986bc, habitatmech:GOLD.85aabc4062, BTO:0000500, BTO:0004493.

All 24 cohort records pass LinkML schema validation, strict closed-schema validation, history validation (881 records), provenance verification, exact 3,209-record corpus reproduction, causal-graph validation (113 graphs), term-request check (676 terms), and OAK id-label correspondence.

### Cohort boundary and lumping/splitting evaluation

scope: supported. Targets: UBERON:0001760, habitatmech:GOLD.112979e260, habitatmech:GOLD.4be243a2b8, habitatmech:GOLD.7e21c19f98, BTO:0000486, BTO:0004057, habitatmech:GOLD.92cbc36828, habitatmech:GOLD.1ab59245f7, ENVO:01001041, BTO:0004108, BTO:0000493, habitatmech:GOLD.0ec3770763, habitatmech:GOLD.a84ac69a45, habitatmech:GOLD.7c37c0e048, habitatmech:GOLD.97738241e1, habitatmech:GOLD.fa99e76de1, BTO:0000495, UBERON:0000045, habitatmech:GOLD.623ff8e506, habitatmech:GOLD.8f1269c14c, habitatmech:GOLD.ace43986bc, habitatmech:GOLD.85aabc4062, BTO:0000500, BTO:0004493.

All 24 records represent distinct anatomical-site, frozen-remains, plant-organ/gall/gametophyte, fungal-environment, gallbladder/gallstone, hymenopteran-gaster, insect gastric-caeca, or human cyst/carcinoma/gastric-epithelium source concepts; no cross-record lumping or splitting is warranted across the cohort.

### Cohort hierarchy, synonym, and mapping-endpoint summary

grounding: supported. Targets: UBERON:0001760, habitatmech:GOLD.112979e260, habitatmech:GOLD.4be243a2b8, habitatmech:GOLD.7e21c19f98, BTO:0000486, BTO:0004057, habitatmech:GOLD.92cbc36828, habitatmech:GOLD.1ab59245f7, ENVO:01001041, BTO:0004108, BTO:0000493, habitatmech:GOLD.0ec3770763, habitatmech:GOLD.a84ac69a45, habitatmech:GOLD.7c37c0e048, habitatmech:GOLD.97738241e1, habitatmech:GOLD.fa99e76de1, BTO:0000495, UBERON:0000045, habitatmech:GOLD.623ff8e506, habitatmech:GOLD.8f1269c14c, habitatmech:GOLD.ace43986bc, habitatmech:GOLD.85aabc4062, BTO:0000500, BTO:0004493.

13 records pass with limitations; 11 records have 17 open findings (2 blocker identity findings, 9 major grounding findings, 2 major nomenclature findings, and 4 major #1398 mapping-endpoint contract findings) recorded in their respective kind: record bundles (linked in related_reviews) and carried forward to Stage 5 grouped remediation.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: UBERON:0001760, habitatmech:GOLD.112979e260, habitatmech:GOLD.4be243a2b8, habitatmech:GOLD.7e21c19f98, BTO:0000486, BTO:0004057, habitatmech:GOLD.92cbc36828, habitatmech:GOLD.1ab59245f7, ENVO:01001041, BTO:0004108. Retain frontal sinus (UBERON:0001760), the 3 host-clade frozen-remains records (avian, human, and fish), fruit (BTO:0000486), fruit juice (BTO:0004057), fungal fruiting body (habitatmech:GOLD.92cbc36828), endofungal endosymbiont niche (habitatmech:GOLD.1ab59245f7), fungi-associated environment (ENVO:01001041), and G cell (BTO:0004108) as distinct source-attested bins.
- retain: BTO:0000493, habitatmech:GOLD.0ec3770763, habitatmech:GOLD.a84ac69a45, habitatmech:GOLD.7c37c0e048, habitatmech:GOLD.97738241e1, habitatmech:GOLD.fa99e76de1, BTO:0000495. Retain cross-vertebrate/fish gall bladder (BTO:0000493), human and mammalian Gallbladder bins (habitatmech:GOLD.0ec3770763, habitatmech:GOLD.a84ac69a45), mammalian and human gallstone bins (habitatmech:GOLD.7c37c0e048, habitatmech:GOLD.97738241e1), plant root Galls (habitatmech:GOLD.fa99e76de1), and moss Gametophytes (currently grounded to BTO:0000495) as distinct anatomical and plant-associated bins.
- retain: UBERON:0000045, habitatmech:GOLD.623ff8e506, habitatmech:GOLD.8f1269c14c, habitatmech:GOLD.ace43986bc, habitatmech:GOLD.85aabc4062, BTO:0000500, BTO:0004493. Retain human benign-tumor ganglion cyst (currently grounded to UBERON:0000045 ganglion), hymenopteran gaster environment (habitatmech:GOLD.623ff8e506), insect midgut and larval gastric caeca (habitatmech:GOLD.8f1269c14c, habitatmech:GOLD.ace43986bc), NOT_APPLICABLE Gastric carcinoma (habitatmech:GOLD.85aabc4062), gastric epithelium (BTO:0000500), and gastric epithelium cell line (BTO:0004493) as distinct source-attested records.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon, organism-form, and disease-classification terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator resolution routes and parent/synonym assembly verified across all 24 cohort target records. |
| EREC1 | data/habitats/host_associated/frontal_sinus.yaml; Entire YAML | supports | The GOLD-attested record UBERON:0001760 (frontal sinus, 'Host-associated &gt; Mammals: Human &gt; Respiratory system &gt; Nasal cavity &gt; Paranasal sinuses: Frontal', habitatmech:GOLD.e8d686e00d, EXACT/REVIEWED) asserts the whole human Nasal cavity (habitatmech:GOLD.bcb2f8b7f3) in parent_habitats alongside UBERON:0001825 (paranasal sinus) and promotes the compound GOLD leaf 'Paranasal sinuses: Frontal' as an EXACT_SYNONYM. |
| EREC2 | data/habitats/host_associated/frozen_remains.yaml; Entire YAML | supports | The curated GOLD frozen-remains record habitatmech:GOLD.112979e260 (frozen avian remains, 'Host-associated &gt; Birds &gt; Remains &gt; Frozen remains', UNGROUNDED/REVIEWED) is coherently defined under ENVO:00002033 (carcass) with parent_mode REPLACE and source-label exclusion for bare 'Frozen remains'. |
| EREC3 | data/habitats/host_associated/frozen_remains__584db35c.yaml; Entire YAML | supports | The curated GOLD frozen-remains record habitatmech:GOLD.4be243a2b8 (frozen human remains, 'Host-associated &gt; Mammals: Human &gt; Remains &gt; Frozen remains', UNGROUNDED/REVIEWED) is coherently defined under ENVO:00002033 (carcass) with parent_mode REPLACE and source-label exclusion for bare 'Frozen remains'. |
| EREC4 | data/habitats/host_associated/frozen_remains__aa25d597.yaml; Entire YAML | supports | The curated GOLD frozen-remains record habitatmech:GOLD.7e21c19f98 (frozen fish remains, 'Host-associated &gt; Fish &gt; Remains &gt; Frozen remains', UNGROUNDED/REVIEWED) is coherently defined under ENVO:00002033 (carcass) with parent_mode REPLACE and source-label exclusion for bare 'Frozen remains'. |
| EREC5 | data/habitats/host_associated/fruit.yaml; Entire YAML | supports | The PREGO-attested record BTO:0000486 (fruit, EXACT/SEEDED, 42 TAXON assertions) is coherently grounded to BRENDA Tissue Ontology term BTO:0000486 ('The mature ovary or ovaries of a seed-bearing plant, together with accessory parts, containing the seeds and occurring in a wide variety of forms.') with 1 PREGO RELATED_SYNONYM ('fruits') and 25 displayed characteristic taxa from the 42-row PREGO pool. |
| EREC6 | data/habitats/host_associated/fruit_juice.yaml; Entire YAML | supports | The PREGO-attested record BTO:0004057 (fruit juice, EXACT/SEEDED, 2 TAXON assertions for Leuconostoc citreum and Leuconostoc pseudomesenteroides) is coherently grounded to BRENDA Tissue Ontology term BTO:0004057 under strictly broader BTO:0000659 (juice, 'The extractable fluid contents of cells or tissues.') with 1 PREGO RELATED_SYNONYM ('fruit juices'). |
| EREC7 | data/habitats/host_associated/fruiting_body.yaml; Entire YAML | supports | The curated GOLD record habitatmech:GOLD.92cbc36828 (fungal fruiting body, 'Host-associated &gt; Fungi &gt; Fruiting body', UNGROUNDED/REVIEWED, 140 ORGANISM assertions) is coherently defined under ENVO:01001041 (fungi-associated environment) with bare 'Fruiting body' excluded from exact_synonyms and an evidence-backed 5-node/4-edge causal mechanism graph (PMID:38692852, PMID:23426012, PMID:35237850, PMID:33943006). |
| EREC8 | data/habitats/host_associated/fungi.yaml; Entire YAML | supports | The curated GOLD fungal-endosymbiont record habitatmech:GOLD.1ab59245f7 (Fungi, 'Host-associated &gt; Endosymbionts &gt; Fungi', NARROW/REVIEWED, 5 ORGANISM assertions) coherently places the endofungal endosymbiont niche under ENVO:01001041 (fungi-associated environment) and habitatmech:GOLD.895a2372e5 (host endosymbiont microhabitat), but emits mapping_predicate skos:narrowMatch on a minted source-path record (#1398). |
| EREC9 | data/habitats/host_associated/fungi_associated_environment.yaml; Entire YAML | supports | The multi-source record ENVO:01001041 (fungi-associated environment, attested by ENVIRONMENTS_TABLE, GOLD 'Host-associated &gt; Fungi' 635 ORGANISM assertions, and MADIN ENVO:01001041 38 TAXON assertions, EXACT/REVIEWED, 10 environmental parameters, 1 causal graph) promotes the bare host kingdom name 'Fungi' as an EXACT_SYNONYM from GOLD decision row 1580 (grounding_status=EXACT on habitatmech:GOLD.a8fc5001d1), conflating the fungal host kingdom with its associated environment. |
| EREC10 | data/habitats/host_associated/g_cell.yaml; Entire YAML | supports | The PREGO-attested record BTO:0004108 (G cell, EXACT/SEEDED, 1 TAXON assertion for Helicobacter pylori) is coherently grounded to BRENDA Tissue Ontology term BTO:0004108 ('Endocrine cells found in the pyloric gland mucosa (antral mucosa) of the stomach and responsible for the secretion of gastrin.'). |
| EREC11 | data/habitats/host_associated/gall_bladder.yaml; Entire YAML | supports | The multi-source record BTO:0000493 (gall bladder, attested by GOLD 'Host-associated &gt; Fish &gt; Digestive system &gt; Biliary tract &gt; Gall bladder' and PREGO BTO:0000493 2 TAXON assertions, EXACT/REVIEWED) asserts the whole fish Biliary tract (habitatmech:GOLD.004065681a, 'Host-associated &gt; Fish &gt; Digestive system &gt; Biliary tract') in parent_habitats alongside BTO:0000123 (bladder), conflating part_of biliary-tract composition and fish-only host scope with is_a subtyping on the cross-vertebrate gallbladder class. |
| EREC12 | data/habitats/host_associated/gallbladder.yaml; Entire YAML | supports | The human Gallbladder record habitatmech:GOLD.0ec3770763 ('Host-associated &gt; Mammals: Human &gt; Digestive system &gt; Biliary tract &gt; Gallbladder', NARROW/SEEDED) asserts the whole human Biliary tract (habitatmech:GOLD.133311ddf9, 'Host-associated &gt; Mammals: Human &gt; Digestive system &gt; Biliary tract') in parent_habitats alongside UBERON:0002110 (gallbladder), conflating part_of biliary-tract composition with is_a subtyping, and emits mapping_predicate skos:narrowMatch on a minted source-path record (#1398). |
| EREC13 | data/habitats/host_associated/gallbladder__d157697c.yaml; Entire YAML | supports | The mammalian Gallbladder record habitatmech:GOLD.a84ac69a45 ('Host-associated &gt; Mammals &gt; Digestive system &gt; Biliary tract &gt; Gallbladder', NARROW/SEEDED) asserts the whole mammalian Biliary tract (habitatmech:GOLD.de5efc0eb8, 'Host-associated &gt; Mammals &gt; Digestive system &gt; Biliary tract') in parent_habitats alongside UBERON:0002110 (gallbladder), conflating part_of biliary-tract composition with is_a subtyping, and emits mapping_predicate skos:narrowMatch on a minted source-path record (#1398). |
| EREC14 | data/habitats/host_associated/gallbladder_stones.yaml; Entire YAML | supports | The curated GOLD gallstone record habitatmech:GOLD.7c37c0e048 (mammalian gallstone, 'Host-associated &gt; Mammals &gt; Digestive system &gt; Biliary tract &gt; Gallbladder stones', UNGROUNDED/REVIEWED) is coherently defined under ENVO:2100000 (anatomical entity environment) with parent_mode REPLACE and source-label exclusion for bare 'Gallbladder stones'. |
| EREC15 | data/habitats/host_associated/gallbladder_stones__a31ee838.yaml; Entire YAML | supports | The curated GOLD gallstone record habitatmech:GOLD.97738241e1 (human gallstone, 'Host-associated &gt; Mammals: Human &gt; Digestive system &gt; Biliary tract &gt; Gallbladder stones', UNGROUNDED/REVIEWED) is coherently defined under ENVO:2100000 (anatomical entity environment) with parent_mode REPLACE and source-label exclusion for bare 'Gallbladder stones'. |
| EREC16 | data/habitats/host_associated/galls.yaml; Entire YAML | supports | The plant root-gall record habitatmech:GOLD.fa99e76de1 (Galls, 'Host-associated &gt; Plants &gt; Roots &gt; Galls', NARROW/REVIEWED, 4 ORGANISM assertions) asserts the whole plant root organ PO:0009005 (root) in parent_habitats alongside PO:0025626 (plant gall), conflating anatomical host-organ location with is_a subtyping, and emits mapping_predicate skos:narrowMatch on a minted source-path record (#1398). |
| EREC17 | data/habitats/host_associated/gametophyte.yaml; Entire YAML | supports | The GOLD-attested record BTO:0000495 (gametophyte, 'Host-associated &gt; Plants &gt; Bryophytes &gt; Moss &gt; Gametophytes', habitatmech:GOLD.b66efd9c93, EXACT/REVIEWED) grounds a moss-specific gametophyte host environment to the generic whole-plant generation/form class BTO:0000495 ('The individual or generation of a plant exhibiting alternation of generations that bears sex organs.'), importing both morphological BTO:0000720 (plant form) and macro-scale biome ENVO:01000890 (area of moss-dominated vegetation) in parent_habitats. |
| EREC18 | data/habitats/host_associated/ganglion.yaml; Entire YAML | supports | The GOLD-attested record UBERON:0000045 (ganglion, 'Host-associated &gt; Mammals: Human &gt; Benign tumor &gt; Ganglion', habitatmech:GOLD.dd1dd7acb8, EXACT/SEEDED) lexically grounds a human benign-tumor ganglion cyst source path to neural tissue mass UBERON:0000045 ('A biological tissue mass, most commonly a mass of nerve cell bodies.') and asserts NOT_APPLICABLE disease parent habitatmech:GOLD.333c18201f (Benign tumor) in parent_habitats. |
| EREC19 | data/habitats/host_associated/gaster.yaml; Entire YAML | supports | The curated GOLD hymenopteran gaster record habitatmech:GOLD.623ff8e506 (gaster environment, 'Host-associated &gt; Arthropoda: Insects &gt; Abdomen &gt; Metasoma &gt; Gaster', UNGROUNDED/REVIEWED) asserts the whole metasoma environment (habitatmech:GOLD.93f0f7b66d, 'Host-associated &gt; Arthropoda: Insects &gt; Abdomen &gt; Metasoma') in parent_habitats alongside ENVO:01001002 (animal-associated environment), conflating anatomical part_of subdivision of the metasoma with is_a subtyping. |
| EREC20 | data/habitats/host_associated/gastric_caeca.yaml; Entire YAML | supports | The curated GOLD record habitatmech:GOLD.8f1269c14c (insect midgut gastric cecum, 'Host-associated &gt; Arthropoda: Insects &gt; Digestive system &gt; Midgut &gt; Gastric caeca', UNGROUNDED/REVIEWED, 1 ORGANISM assertion) is coherently defined under UBERON:0001045 (midgut) and insect Midgut (habitatmech:GOLD.67c565f695) with source-label exclusion for bare 'Gastric caeca', matching sibling filter_chamber.yaml and mixed_segment.yaml. |
| EREC21 | data/habitats/host_associated/gastric_caeca__12108999.yaml; Entire YAML | supports | The curated GOLD record habitatmech:GOLD.ace43986bc (insect larval gastric caecum, 'Host-associated &gt; Arthropoda: Insects &gt; Larva &gt; Gut &gt; Gastric caeca', UNGROUNDED/REVIEWED, 2 ORGANISM assertions) is coherently defined under UBERON:0001045 (midgut) with parent_mode REPLACE and source-label exclusion for bare 'Gastric caeca'. |
| EREC22 | data/habitats/host_associated/gastric_carcinoma.yaml; Entire YAML | supports | The GOLD record habitatmech:GOLD.85aabc4062 (Gastric carcinoma, 'Host-associated &gt; Mammals: Human &gt; Malignant tumor &gt; Carcinoma &gt; Gastric carcinoma', NOT_APPLICABLE/REVIEWED) is rightly marked NOT_APPLICABLE as a malignant neoplasm disease classification with MONDO:0001056 in xrefs, but retains NOT_APPLICABLE disease parent habitatmech:GOLD.9bb307824f (Carcinoma) in parent_habitats. |
| EREC23 | data/habitats/host_associated/gastric_epithelium.yaml; Entire YAML | supports | The PREGO-attested record BTO:0000500 (gastric epithelium, EXACT/SEEDED, 2 TAXON assertions for Helicobacter pylori) is coherently grounded to BRENDA Tissue Ontology term BTO:0000500 ('Epithelium of the stomach.') under strictly broader BTO:0000416 (epithelium). |
| EREC24 | data/habitats/host_associated/gastric_epithelium_cell_line.yaml; Entire YAML | supports | The PREGO-attested record BTO:0004493 (gastric epithelium cell line, EXACT/SEEDED, 2 TAXON assertions for Helicobacter pylori) is coherently grounded to BRENDA Tissue Ontology term BTO:0004493 under strictly broader BTO:0001088 (gastric cell line) and BTO:0001120 (epithelial cell line). |

## Limits And Additional Notes

- Only the stated primary evidence and current ontology/taxonomy authorities were independently inspected; original specimen-level support for every source-bin member is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism, or characteristic presence.
- Configured label correspondence skipped 2,106 no-adapter pairs; this is not whole-corpus identifier certification.
- Record-specific open findings (17 across 11 records: 2 blocker identity defects, 9 major grounding/hierarchy defects, 2 major nomenclature synonym defects, and 4 major #1398 mapping-endpoint contract defects) are recorded on their respective kind: record bundles in related_reviews so each issue_key has a single authoritative open owner for Stage 5 remediation.
- All 24 cohort target files and context inputs were captured at clean git commit 83aa5f212521389cb9c3507ded58d0bcd0a22ee0.
- Each of the 24 targets has a dedicated kind: record bundle in reviews/structured/.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261111T060600Z-frontal_sinus_to_gastric_epithelium_cell_line-category
repository: CultureBotAI/HabitatMech
kind: category
title: 'Category cohort review: host_associated slice frontal_sinus through gastric_epithelium_cell_line
  (24 records)'
started_at: '2026-11-11T05:35:00Z'
finished_at: '2026-11-11T06:06:00Z'
reviewer:
  identity: antigravity
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Same agent inspected all 24 cohort target records and source
    evidence; not independent human or second-agent approval.
skill: .claude/skills/review-yaml-category/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Full 24-record category boundary and cohort review of the contiguous unreviewed
  host_associated slice (frontal_sinus.yaml through gastric_epithelium_cell_line.yaml)
  at commit 83aa5f212521389cb9c3507ded58d0bcd0a22ee0. All 24 records represent distinct
  paranasal-sinus, frozen-remains, plant fruit/juice/gall/gametophyte, fungal fruiting-body/endosymbiont/host-environment,
  gallbladder/gallstone, hymenopteran gaster, insect gastric-caeca, and human cyst/carcinoma/gastric-epithelium
  source concepts (retain decisions; no cross-record lumping or splitting). Record-level
  open findings (17 total across 11 records) are recorded in the 24 linked kind: record
  bundles for Stage 5 remediation.'
source:
  git_revision: 83aa5f212521389cb9c3507ded58d0bcd0a22ee0
  state: git_commit
  inputs:
  - path: curation/causal_graphs/fruiting_body.yaml
    sha256: 86758f4d02ac5b1726bdf970d1be8ffa8029221d953a1d98110f5ed3ceca249e
    role: context
  - path: curation/causal_graphs/fungi_associated_environment.yaml
    sha256: 5ae74157d3c39e9a1d8dee4cd78b54361ccc36abc763ad3d0f86cc593d0d2805
    role: context
  - path: curation/decisions.tsv
    sha256: 8e0c9ea50c453b9b0eb86e9a6cf246dbc188714ec7a8cc37b2918d5373e6d2ae
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 84e5214713a21033312eb9c512fe38f44865662f934a4e679d45e827b16ff780
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 21c90040f7616f5ecc103716597d65b899f433eee24e880ac3f2fd802ff624c6
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: c1207270bb0ae2031e42de6cb8220b20f98886f65e40d48793bfd7e9d757d83a
    role: context
  - path: curation/term_requests.tsv
    sha256: 3703ae74d7565abdfb5a1fab47718b05c4fd02447b4ed60bbeb3bde65e1d8792
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: 779e0cf7e829e3ec74b5a898b6ed70d54d930b7da726c1611225902c00915388
    role: context
  - path: data/habitats/food/juice.yaml
    sha256: ebafd3723346610c3d0b1055d2b5e275b35eb9ca5f5152d0255e9e2667f95822
    role: context
  - path: data/habitats/host_associated/area_of_moss_dominated_vegetation.yaml
    sha256: a52c635630077a391160742c533af7e5fb0eaaf2f5c5da7779e9d66b203eb243
    role: context
  - path: data/habitats/host_associated/basal_cell_carcinoma.yaml
    sha256: b5cdc0a52aacf5c73c2c6ebc063e6eb969545da4998f0519434a01fd4fc6af51
    role: context
  - path: data/habitats/host_associated/benign_tumor.yaml
    sha256: b3790a29cf132d738552651b146b7cdc79a9da4345088af5156865aed41c683d
    role: context
  - path: data/habitats/host_associated/biliary_tract.yaml
    sha256: d1c412d18dede379989569aeb8642bc1c0d7192541009aea474c7a6d22711b31
    role: context
  - path: data/habitats/host_associated/biliary_tract__076692f7.yaml
    sha256: 85d1cca5cedd9b189ae4d559a283ce30f822fa2553495efc31ae627dc031fe40
    role: context
  - path: data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml
    sha256: 100e3d311062851be06598d3c6d25df5cbfef28ef2bfd9033bad61d05159dc88
    role: context
  - path: data/habitats/host_associated/bladder.yaml
    sha256: 9035b57715f4f6980ee00734b52991cc3fd4ce36c034f3a967512db8e64dd802
    role: context
  - path: data/habitats/host_associated/carcinoma.yaml
    sha256: 7eae8fe197c614d3c985fd20ee22c71f561c209433bf33c544a774ddb37b8fe8
    role: context
  - path: data/habitats/host_associated/endosymbionts.yaml
    sha256: 552e6941a0f96665c0486e9bf8fba0351fdd4165cc09497aaeb0770875eac2a0
    role: context
  - path: data/habitats/host_associated/environmental_system_determined_by_an_organism.yaml
    sha256: d3b79ef9436a87fbce8e6b204b0113e170fa758e4a66efb592543bf934c67270
    role: context
  - path: data/habitats/host_associated/epidermoid.yaml
    sha256: 5a07695d2e0c025d9a1ee578d5a242d41ab0d09c100d3826db41141cb242f582
    role: context
  - path: data/habitats/host_associated/epithelium.yaml
    sha256: 3842bb5461603ad2188db6eec103fd1bee09a08bb5ace94e45c4022434e2d68b
    role: context
  - path: data/habitats/host_associated/ethmoid_bone.yaml
    sha256: e406e59cf9e099828db610c838af4d413af1da9f57d9d2723b518d236188db8a
    role: context
  - path: data/habitats/host_associated/frontal_sinus.yaml
    sha256: 16bc7e83da615599319babd3c50e9ee12f44a415fe89f1a0e1a368b53f64c121
    role: target
  - path: data/habitats/host_associated/frozen_remains.yaml
    sha256: 84ac3b30e18b8b0175ad85c9703920c043980ba2d87e1c5c3f0efdb5400dd8cd
    role: target
  - path: data/habitats/host_associated/frozen_remains__584db35c.yaml
    sha256: d065abdc911ef64f0784bf8bbcd8edd3dc0620f9215b4204656cb78f7b8c05d4
    role: target
  - path: data/habitats/host_associated/frozen_remains__aa25d597.yaml
    sha256: 3d9aa8ae8d3ac7df600d2d8cddb45ff7dfa8a3ba73646b897bcf6a7844255083
    role: target
  - path: data/habitats/host_associated/fruit.yaml
    sha256: 7d668722a4d581f791f76d299872e7129fdab23fc0daba2b2687049f150ce5be
    role: target
  - path: data/habitats/host_associated/fruit_juice.yaml
    sha256: 1ae7408229392df98be954513b3a820c24d5d39c486f3aae00f59816e2faa439
    role: target
  - path: data/habitats/host_associated/fruiting_body.yaml
    sha256: d4d18d1693fa24b535953d970d9f2d4603f7685f2343eab2c35b3d6bcbfe2597
    role: target
  - path: data/habitats/host_associated/fungi.yaml
    sha256: a94d2c1a2e502490f2bcc20445701600899be0ec3c5f65cbeef63c3157abf933
    role: target
  - path: data/habitats/host_associated/fungi_associated_environment.yaml
    sha256: 11b83dd57a7f805d6330e4a3054673dc72dc325456bd520942a359645eb56734
    role: target
  - path: data/habitats/host_associated/g_cell.yaml
    sha256: 0b06ac2e7824a8ba7ad066fcf7a7eee3ae80cf83a23e04ccf33727ca3354be2a
    role: target
  - path: data/habitats/host_associated/gall_bladder.yaml
    sha256: f61449421a483e738a30b16ed9fa444af60f17e45598c5c7ca0d5868d4524c92
    role: target
  - path: data/habitats/host_associated/gallbladder.yaml
    sha256: 60a598bf70d54d17d13d60962e70768c1bb43c370ba0bf0a07bef7b4d7e42122
    role: target
  - path: data/habitats/host_associated/gallbladder__d157697c.yaml
    sha256: 4e9b91ea514d4d1f0617a76abe46721afd2773192cdd051db20aef1c77137e5c
    role: target
  - path: data/habitats/host_associated/gallbladder_stones.yaml
    sha256: 661066689cf60513ece8fed247b5274db16cd65837a3a3b44076786f28153f6d
    role: target
  - path: data/habitats/host_associated/gallbladder_stones__a31ee838.yaml
    sha256: 8e0198617a663ee8bf04dd344600eb5e90d0d236da577d529d8482543c7dc5cc
    role: target
  - path: data/habitats/host_associated/galls.yaml
    sha256: 9b3d44162a9d6dd499461e9c3a0b4beeda5d27bd1b189f6a7a49720c19495d91
    role: target
  - path: data/habitats/host_associated/gametophyte.yaml
    sha256: 259dc02d4625e3abc226bc6d62a0b20b046a7564ffcb3fa8d3af71595a6b305a
    role: target
  - path: data/habitats/host_associated/ganglion.yaml
    sha256: e39ddd3161ba10522b1c13bf08c1720dd0bc3a5ad42586fe647fb8cd2814bd1a
    role: target
  - path: data/habitats/host_associated/gaster.yaml
    sha256: c34203639b107c6028119754515374089e25a79a8563faea8f7f8d62cd2adf97
    role: target
  - path: data/habitats/host_associated/gastric_caeca.yaml
    sha256: ef03bef1ca1dc6ce4524e4b2f6232651c9fd27e22ddd3e96e8302129554d0735
    role: target
  - path: data/habitats/host_associated/gastric_caeca__12108999.yaml
    sha256: 86e0224ec28ee9284cb9b59a46e5a9f5ea951a777fc9197fd07980ea19bc110c
    role: target
  - path: data/habitats/host_associated/gastric_carcinoma.yaml
    sha256: de961f575d2d6e0dba70b2fdfc2c17eb210df89cd940b5af9909a5c3ade55bdf
    role: target
  - path: data/habitats/host_associated/gastric_epithelium.yaml
    sha256: f15265925866e67517bc6ab20c308e4b75988683e58e910a0fc9f75ea224821c
    role: target
  - path: data/habitats/host_associated/gastric_epithelium_cell_line.yaml
    sha256: a100192f6a41e5e5e0071272da9318fdcec451ca8c95bd0e5a43eb0faa9b5adb
    role: target
  - path: data/habitats/host_associated/metasoma.yaml
    sha256: 23d18cac807fab29b04c768b3ddcc3af7f7910d2f55a7ce484341c33c6de60c1
    role: context
  - path: data/habitats/host_associated/midgut__7677107b.yaml
    sha256: 9c571b883d0c28d1a414756615f8b67adbfdbc1a791a9e693ee510b6475b13a4
    role: context
  - path: data/habitats/host_associated/nasal_cavity__ae9d5dba.yaml
    sha256: 116dfa610057a262f4cb5e1de5cebde11dcc291bc821e56202c64fff1424dca8
    role: context
  - path: data/habitats/host_associated/plant_gall.yaml
    sha256: 1b51e1ff7745d233005952066048b2c0caf822981a00c38c0e02a64fe6008ce8
    role: context
  - path: data/habitats/host_associated/root__722ce44f.yaml
    sha256: d482fa8fb6b9171716e524da67c6022a8839c5ddbea4d2b3117eb73b771aa7db
    role: context
  - path: data/habitats/other/animal_associated_environment.yaml
    sha256: a1cf41f43f9bece44dfb3e5d6ab0ca86858df67b88ee25d6ada260cccac69e16
    role: context
  - path: data/habitats/other/carcass__24623a85.yaml
    sha256: 9cce81df5671b106fb73e3dd58815969461bcf2c9d363d211ef1fe6c53eb6dfc
    role: context
  - path: data/raw/bacdive_isolation_sources.tsv
    sha256: fb1645dd899a43130be9cf38b0e8b27ffbaa0175306917bff20e20ee225875fc
    role: context
  - path: data/raw/environment_parameters.tsv
    sha256: a75d0f565d8ee2498188ff98b17d0ab325ae4f782601bf4414eff6e86c13e0f9
    role: context
  - path: data/raw/gold_ecosystem_paths.tsv
    sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
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
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
    role: context
  - path: src/habitatmech/seed.py
    sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
    role: context
targets:
- target_id: UBERON:0001760
  path: data/habitats/host_associated/frontal_sinus.yaml
  label: frontal sinus
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
    path: curation/term_requests_excluded.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
- target_id: habitatmech:GOLD.112979e260
  path: data/habitats/host_associated/frozen_remains.yaml
  label: frozen avian remains
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
    path: curation/term_requests_excluded.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
- target_id: habitatmech:GOLD.4be243a2b8
  path: data/habitats/host_associated/frozen_remains__584db35c.yaml
  label: frozen human remains
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
    path: curation/term_requests_excluded.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
- target_id: habitatmech:GOLD.7e21c19f98
  path: data/habitats/host_associated/frozen_remains__aa25d597.yaml
  label: frozen fish remains
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
    path: curation/term_requests_excluded.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
- target_id: BTO:0000486
  path: data/habitats/host_associated/fruit.yaml
  label: fruit
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
    path: curation/term_requests_excluded.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
- target_id: BTO:0004057
  path: data/habitats/host_associated/fruit_juice.yaml
  label: fruit juice
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
    path: curation/term_requests_excluded.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
- target_id: habitatmech:GOLD.92cbc36828
  path: data/habitats/host_associated/fruiting_body.yaml
  label: fungal fruiting body
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
    path: curation/term_requests_excluded.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
- target_id: habitatmech:GOLD.1ab59245f7
  path: data/habitats/host_associated/fungi.yaml
  label: Fungi
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
    path: curation/term_requests_excluded.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
- target_id: ENVO:01001041
  path: data/habitats/host_associated/fungi_associated_environment.yaml
  label: fungi-associated environment
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
    path: curation/term_requests_excluded.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
- target_id: BTO:0004108
  path: data/habitats/host_associated/g_cell.yaml
  label: G cell
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
    path: curation/term_requests_excluded.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
- target_id: BTO:0000493
  path: data/habitats/host_associated/gall_bladder.yaml
  label: gall bladder
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
    path: curation/term_requests_excluded.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
- target_id: habitatmech:GOLD.0ec3770763
  path: data/habitats/host_associated/gallbladder.yaml
  label: Gallbladder
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
    path: curation/term_requests_excluded.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
- target_id: habitatmech:GOLD.a84ac69a45
  path: data/habitats/host_associated/gallbladder__d157697c.yaml
  label: Gallbladder
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
    path: curation/term_requests_excluded.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
- target_id: habitatmech:GOLD.7c37c0e048
  path: data/habitats/host_associated/gallbladder_stones.yaml
  label: mammalian gallstone
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
    path: curation/term_requests_excluded.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
- target_id: habitatmech:GOLD.97738241e1
  path: data/habitats/host_associated/gallbladder_stones__a31ee838.yaml
  label: human gallstone
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
    path: curation/term_requests_excluded.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
- target_id: habitatmech:GOLD.fa99e76de1
  path: data/habitats/host_associated/galls.yaml
  label: Galls
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
    path: curation/term_requests_excluded.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
- target_id: BTO:0000495
  path: data/habitats/host_associated/gametophyte.yaml
  label: gametophyte
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
    path: curation/term_requests_excluded.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
- target_id: UBERON:0000045
  path: data/habitats/host_associated/ganglion.yaml
  label: ganglion
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
    path: curation/term_requests_excluded.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
- target_id: habitatmech:GOLD.623ff8e506
  path: data/habitats/host_associated/gaster.yaml
  label: gaster environment
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
    path: curation/term_requests_excluded.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
- target_id: habitatmech:GOLD.8f1269c14c
  path: data/habitats/host_associated/gastric_caeca.yaml
  label: insect midgut gastric cecum
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
    path: curation/term_requests_excluded.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
- target_id: habitatmech:GOLD.ace43986bc
  path: data/habitats/host_associated/gastric_caeca__12108999.yaml
  label: insect larval gastric caecum
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
    path: curation/term_requests_excluded.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
- target_id: habitatmech:GOLD.85aabc4062
  path: data/habitats/host_associated/gastric_carcinoma.yaml
  label: Gastric carcinoma
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
    path: curation/term_requests_excluded.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
- target_id: BTO:0000500
  path: data/habitats/host_associated/gastric_epithelium.yaml
  label: gastric epithelium
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
    path: curation/term_requests_excluded.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
- target_id: BTO:0004493
  path: data/habitats/host_associated/gastric_epithelium_cell_line.yaml
  label: gastric epithelium cell line
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
    path: curation/term_requests_excluded.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
scope:
  description: Contiguous 24-record cohort boundary review of previously unreviewed
    records in data/habitats/host_associated/ (indices 554-577 in path order).
  selection: Next 24 unreviewed records in data/habitats/host_associated/ immediately
    following 20261109T181033Z-free_living_state-record.
  coverage: full
  population_size: 24
  reviewed_target_ids:
  - UBERON:0001760
  - habitatmech:GOLD.112979e260
  - habitatmech:GOLD.4be243a2b8
  - habitatmech:GOLD.7e21c19f98
  - BTO:0000486
  - BTO:0004057
  - habitatmech:GOLD.92cbc36828
  - habitatmech:GOLD.1ab59245f7
  - ENVO:01001041
  - BTO:0004108
  - BTO:0000493
  - habitatmech:GOLD.0ec3770763
  - habitatmech:GOLD.a84ac69a45
  - habitatmech:GOLD.7c37c0e048
  - habitatmech:GOLD.97738241e1
  - habitatmech:GOLD.fa99e76de1
  - BTO:0000495
  - UBERON:0000045
  - habitatmech:GOLD.623ff8e506
  - habitatmech:GOLD.8f1269c14c
  - habitatmech:GOLD.ace43986bc
  - habitatmech:GOLD.85aabc4062
  - BTO:0000500
  - BTO:0004493
  exclusions:
  - target: Other habitat records outside indices 554-577 of data/habitats/host_associated/
    reason: Bounded 24-record cohort slice for Cycle 9 Stage 4 record/category review;
      direct parents and relevant siblings are inspected as context.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: .venv/bin/python -m linkml.validator.cli -s src/habitatmech/schema/habitatmech.yaml
    --target-class HabitatRecord data/habitats/host_associated/frontal_sinus.yaml
    data/habitats/host_associated/frozen_remains.yaml data/habitats/host_associated/frozen_remains__584db35c.yaml
    data/habitats/host_associated/frozen_remains__aa25d597.yaml data/habitats/host_associated/fruit.yaml
    data/habitats/host_associated/fruit_juice.yaml data/habitats/host_associated/fruiting_body.yaml
    data/habitats/host_associated/fungi.yaml data/habitats/host_associated/fungi_associated_environment.yaml
    data/habitats/host_associated/g_cell.yaml data/habitats/host_associated/gall_bladder.yaml
    data/habitats/host_associated/gallbladder.yaml data/habitats/host_associated/gallbladder__d157697c.yaml
    data/habitats/host_associated/gallbladder_stones.yaml data/habitats/host_associated/gallbladder_stones__a31ee838.yaml
    data/habitats/host_associated/galls.yaml data/habitats/host_associated/gametophyte.yaml
    data/habitats/host_associated/ganglion.yaml data/habitats/host_associated/gaster.yaml
    data/habitats/host_associated/gastric_caeca.yaml data/habitats/host_associated/gastric_caeca__12108999.yaml
    data/habitats/host_associated/gastric_carcinoma.yaml data/habitats/host_associated/gastric_epithelium.yaml
    data/habitats/host_associated/gastric_epithelium_cell_line.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0001760
  - habitatmech:GOLD.112979e260
  - habitatmech:GOLD.4be243a2b8
  - habitatmech:GOLD.7e21c19f98
  - BTO:0000486
  - BTO:0004057
  - habitatmech:GOLD.92cbc36828
  - habitatmech:GOLD.1ab59245f7
  - ENVO:01001041
  - BTO:0004108
  - BTO:0000493
  - habitatmech:GOLD.0ec3770763
  - habitatmech:GOLD.a84ac69a45
  - habitatmech:GOLD.7c37c0e048
  - habitatmech:GOLD.97738241e1
  - habitatmech:GOLD.fa99e76de1
  - BTO:0000495
  - UBERON:0000045
  - habitatmech:GOLD.623ff8e506
  - habitatmech:GOLD.8f1269c14c
  - habitatmech:GOLD.ace43986bc
  - habitatmech:GOLD.85aabc4062
  - BTO:0000500
  - BTO:0004493
  summary: Completed 2026-11-11T05:58:55Z. No issues found.
  scope_note: Individual schema; strict command covers the 24 named cohort targets;
    other documented gates have full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/habitats/host_associated/frontal_sinus.yaml
    data/habitats/host_associated/frozen_remains.yaml data/habitats/host_associated/frozen_remains__584db35c.yaml
    data/habitats/host_associated/frozen_remains__aa25d597.yaml data/habitats/host_associated/fruit.yaml
    data/habitats/host_associated/fruit_juice.yaml data/habitats/host_associated/fruiting_body.yaml
    data/habitats/host_associated/fungi.yaml data/habitats/host_associated/fungi_associated_environment.yaml
    data/habitats/host_associated/g_cell.yaml data/habitats/host_associated/gall_bladder.yaml
    data/habitats/host_associated/gallbladder.yaml data/habitats/host_associated/gallbladder__d157697c.yaml
    data/habitats/host_associated/gallbladder_stones.yaml data/habitats/host_associated/gallbladder_stones__a31ee838.yaml
    data/habitats/host_associated/galls.yaml data/habitats/host_associated/gametophyte.yaml
    data/habitats/host_associated/ganglion.yaml data/habitats/host_associated/gaster.yaml
    data/habitats/host_associated/gastric_caeca.yaml data/habitats/host_associated/gastric_caeca__12108999.yaml
    data/habitats/host_associated/gastric_carcinoma.yaml data/habitats/host_associated/gastric_epithelium.yaml
    data/habitats/host_associated/gastric_epithelium_cell_line.yaml --out .temp/c9s4_24_strict.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0001760
  - habitatmech:GOLD.112979e260
  - habitatmech:GOLD.4be243a2b8
  - habitatmech:GOLD.7e21c19f98
  - BTO:0000486
  - BTO:0004057
  - habitatmech:GOLD.92cbc36828
  - habitatmech:GOLD.1ab59245f7
  - ENVO:01001041
  - BTO:0004108
  - BTO:0000493
  - habitatmech:GOLD.0ec3770763
  - habitatmech:GOLD.a84ac69a45
  - habitatmech:GOLD.7c37c0e048
  - habitatmech:GOLD.97738241e1
  - habitatmech:GOLD.fa99e76de1
  - BTO:0000495
  - UBERON:0000045
  - habitatmech:GOLD.623ff8e506
  - habitatmech:GOLD.8f1269c14c
  - habitatmech:GOLD.ace43986bc
  - habitatmech:GOLD.85aabc4062
  - BTO:0000500
  - BTO:0004493
  summary: 'Completed 2026-11-11T05:59:01Z. Validated 24 files; files with ERROR:
    0; total ERROR rows: 0.'
  scope_note: Closed-schema strict validation across all 24 cohort target files (and
    3,209 full-corpus files).
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_history.py history
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0001760
  - habitatmech:GOLD.112979e260
  - habitatmech:GOLD.4be243a2b8
  - habitatmech:GOLD.7e21c19f98
  - BTO:0000486
  - BTO:0004057
  - habitatmech:GOLD.92cbc36828
  - habitatmech:GOLD.1ab59245f7
  - ENVO:01001041
  - BTO:0004108
  - BTO:0000493
  - habitatmech:GOLD.0ec3770763
  - habitatmech:GOLD.a84ac69a45
  - habitatmech:GOLD.7c37c0e048
  - habitatmech:GOLD.97738241e1
  - habitatmech:GOLD.fa99e76de1
  - BTO:0000495
  - UBERON:0000045
  - habitatmech:GOLD.623ff8e506
  - habitatmech:GOLD.8f1269c14c
  - habitatmech:GOLD.ace43986bc
  - habitatmech:GOLD.85aabc4062
  - BTO:0000500
  - BTO:0004493
  summary: Completed 2026-11-11T05:59:08Z. No issues found; 881 history record(s)
    valid against src/habitatmech/schema/history.yaml.
  scope_note: Full-corpus curation history validation.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: .venv/bin/python scripts/check_provenance.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0001760
  - habitatmech:GOLD.112979e260
  - habitatmech:GOLD.4be243a2b8
  - habitatmech:GOLD.7e21c19f98
  - BTO:0000486
  - BTO:0004057
  - habitatmech:GOLD.92cbc36828
  - habitatmech:GOLD.1ab59245f7
  - ENVO:01001041
  - BTO:0004108
  - BTO:0000493
  - habitatmech:GOLD.0ec3770763
  - habitatmech:GOLD.a84ac69a45
  - habitatmech:GOLD.7c37c0e048
  - habitatmech:GOLD.97738241e1
  - habitatmech:GOLD.fa99e76de1
  - BTO:0000495
  - UBERON:0000045
  - habitatmech:GOLD.623ff8e506
  - habitatmech:GOLD.8f1269c14c
  - habitatmech:GOLD.ace43986bc
  - habitatmech:GOLD.85aabc4062
  - BTO:0000500
  - BTO:0004493
  summary: 'Completed 2026-11-11T05:59:09Z. provenance current: 14 committed inventories,
    2 GOLD sources.'
  scope_note: Full-corpus raw inventory provenance verification.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: .venv/bin/python scripts/verify_corpus.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0001760
  - habitatmech:GOLD.112979e260
  - habitatmech:GOLD.4be243a2b8
  - habitatmech:GOLD.7e21c19f98
  - BTO:0000486
  - BTO:0004057
  - habitatmech:GOLD.92cbc36828
  - habitatmech:GOLD.1ab59245f7
  - ENVO:01001041
  - BTO:0004108
  - BTO:0000493
  - habitatmech:GOLD.0ec3770763
  - habitatmech:GOLD.a84ac69a45
  - habitatmech:GOLD.7c37c0e048
  - habitatmech:GOLD.97738241e1
  - habitatmech:GOLD.fa99e76de1
  - BTO:0000495
  - UBERON:0000045
  - habitatmech:GOLD.623ff8e506
  - habitatmech:GOLD.8f1269c14c
  - habitatmech:GOLD.ace43986bc
  - habitatmech:GOLD.85aabc4062
  - BTO:0000500
  - BTO:0004493
  summary: 'Completed 2026-11-11T05:59:26Z. expected 3209 records, found 3209 on disk;
    missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/.'
  scope_note: Full-corpus deterministic reproduction from raw inventories and curation
    tables.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_causal_graph_curations.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0001760
  - habitatmech:GOLD.112979e260
  - habitatmech:GOLD.4be243a2b8
  - habitatmech:GOLD.7e21c19f98
  - BTO:0000486
  - BTO:0004057
  - habitatmech:GOLD.92cbc36828
  - habitatmech:GOLD.1ab59245f7
  - ENVO:01001041
  - BTO:0004108
  - BTO:0000493
  - habitatmech:GOLD.0ec3770763
  - habitatmech:GOLD.a84ac69a45
  - habitatmech:GOLD.7c37c0e048
  - habitatmech:GOLD.97738241e1
  - habitatmech:GOLD.fa99e76de1
  - BTO:0000495
  - UBERON:0000045
  - habitatmech:GOLD.623ff8e506
  - habitatmech:GOLD.8f1269c14c
  - habitatmech:GOLD.ace43986bc
  - habitatmech:GOLD.85aabc4062
  - BTO:0000500
  - BTO:0004493
  summary: Completed 2026-11-11T05:59:32Z. validated 113 causal-graph curation file(s)
    with 113 graph(s).
  scope_note: Full-corpus causal-graph overlay validation.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: .venv/bin/python scripts/build_term_requests.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0001760
  - habitatmech:GOLD.112979e260
  - habitatmech:GOLD.4be243a2b8
  - habitatmech:GOLD.7e21c19f98
  - BTO:0000486
  - BTO:0004057
  - habitatmech:GOLD.92cbc36828
  - habitatmech:GOLD.1ab59245f7
  - ENVO:01001041
  - BTO:0004108
  - BTO:0000493
  - habitatmech:GOLD.0ec3770763
  - habitatmech:GOLD.a84ac69a45
  - habitatmech:GOLD.7c37c0e048
  - habitatmech:GOLD.97738241e1
  - habitatmech:GOLD.fa99e76de1
  - BTO:0000495
  - UBERON:0000045
  - habitatmech:GOLD.623ff8e506
  - habitatmech:GOLD.8f1269c14c
  - habitatmech:GOLD.ace43986bc
  - habitatmech:GOLD.85aabc4062
  - BTO:0000500
  - BTO:0004493
  summary: Completed 2026-11-11T05:59:47Z. term-request table is current (676 terms).
  scope_note: Full-corpus term-request table currency check.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0001760
  - habitatmech:GOLD.112979e260
  - habitatmech:GOLD.4be243a2b8
  - habitatmech:GOLD.7e21c19f98
  - BTO:0000486
  - BTO:0004057
  - habitatmech:GOLD.92cbc36828
  - habitatmech:GOLD.1ab59245f7
  - ENVO:01001041
  - BTO:0004108
  - BTO:0000493
  - habitatmech:GOLD.0ec3770763
  - habitatmech:GOLD.a84ac69a45
  - habitatmech:GOLD.7c37c0e048
  - habitatmech:GOLD.97738241e1
  - habitatmech:GOLD.fa99e76de1
  - BTO:0000495
  - UBERON:0000045
  - habitatmech:GOLD.623ff8e506
  - habitatmech:GOLD.8f1269c14c
  - habitatmech:GOLD.ace43986bc
  - habitatmech:GOLD.85aabc4062
  - BTO:0000500
  - BTO:0004493
  summary: 'Completed 2026-11-11T06:00:30Z. OK_CANONICAL: 1211, OK_SYNONYM: 1, OK_EXCEPTION:
    5, SKIPPED_NO_ADAPTER: 2106. All id<->label pairs correspond.'
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
evidence:
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-11T06:06:00Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon, organism-form,
    and disease-classification terms cannot substitute for associated environments;
    parent_habitats must be strictly broader across all contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-11T06:06:00Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-11T06:06:00Z'
  support: supports
  summary: Seed generator resolution routes and parent/synonym assembly verified across
    all 24 cohort target records.
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EREC1
  kind: record_content
  reference: data/habitats/host_associated/frontal_sinus.yaml
  locator: Entire YAML
  accessed_at: '2026-11-11T06:06:00Z'
  support: supports
  summary: 'The GOLD-attested record UBERON:0001760 (frontal sinus, ''Host-associated
    > Mammals: Human > Respiratory system > Nasal cavity > Paranasal sinuses: Frontal'',
    habitatmech:GOLD.e8d686e00d, EXACT/REVIEWED) asserts the whole human Nasal cavity
    (habitatmech:GOLD.bcb2f8b7f3) in parent_habitats alongside UBERON:0001825 (paranasal
    sinus) and promotes the compound GOLD leaf ''Paranasal sinuses: Frontal'' as an
    EXACT_SYNONYM.'
  snapshot_sha256: 16bc7e83da615599319babd3c50e9ee12f44a415fe89f1a0e1a368b53f64c121
- evidence_id: EREC2
  kind: record_content
  reference: data/habitats/host_associated/frozen_remains.yaml
  locator: Entire YAML
  accessed_at: '2026-11-11T06:06:00Z'
  support: supports
  summary: The curated GOLD frozen-remains record habitatmech:GOLD.112979e260 (frozen
    avian remains, 'Host-associated > Birds > Remains > Frozen remains', UNGROUNDED/REVIEWED)
    is coherently defined under ENVO:00002033 (carcass) with parent_mode REPLACE and
    source-label exclusion for bare 'Frozen remains'.
  snapshot_sha256: 84ac3b30e18b8b0175ad85c9703920c043980ba2d87e1c5c3f0efdb5400dd8cd
- evidence_id: EREC3
  kind: record_content
  reference: data/habitats/host_associated/frozen_remains__584db35c.yaml
  locator: Entire YAML
  accessed_at: '2026-11-11T06:06:00Z'
  support: supports
  summary: 'The curated GOLD frozen-remains record habitatmech:GOLD.4be243a2b8 (frozen
    human remains, ''Host-associated > Mammals: Human > Remains > Frozen remains'',
    UNGROUNDED/REVIEWED) is coherently defined under ENVO:00002033 (carcass) with
    parent_mode REPLACE and source-label exclusion for bare ''Frozen remains''.'
  snapshot_sha256: d065abdc911ef64f0784bf8bbcd8edd3dc0620f9215b4204656cb78f7b8c05d4
- evidence_id: EREC4
  kind: record_content
  reference: data/habitats/host_associated/frozen_remains__aa25d597.yaml
  locator: Entire YAML
  accessed_at: '2026-11-11T06:06:00Z'
  support: supports
  summary: The curated GOLD frozen-remains record habitatmech:GOLD.7e21c19f98 (frozen
    fish remains, 'Host-associated > Fish > Remains > Frozen remains', UNGROUNDED/REVIEWED)
    is coherently defined under ENVO:00002033 (carcass) with parent_mode REPLACE and
    source-label exclusion for bare 'Frozen remains'.
  snapshot_sha256: 3d9aa8ae8d3ac7df600d2d8cddb45ff7dfa8a3ba73646b897bcf6a7844255083
- evidence_id: EREC5
  kind: record_content
  reference: data/habitats/host_associated/fruit.yaml
  locator: Entire YAML
  accessed_at: '2026-11-11T06:06:00Z'
  support: supports
  summary: The PREGO-attested record BTO:0000486 (fruit, EXACT/SEEDED, 42 TAXON assertions)
    is coherently grounded to BRENDA Tissue Ontology term BTO:0000486 ('The mature
    ovary or ovaries of a seed-bearing plant, together with accessory parts, containing
    the seeds and occurring in a wide variety of forms.') with 1 PREGO RELATED_SYNONYM
    ('fruits') and 25 displayed characteristic taxa from the 42-row PREGO pool.
  snapshot_sha256: 7d668722a4d581f791f76d299872e7129fdab23fc0daba2b2687049f150ce5be
- evidence_id: EREC6
  kind: record_content
  reference: data/habitats/host_associated/fruit_juice.yaml
  locator: Entire YAML
  accessed_at: '2026-11-11T06:06:00Z'
  support: supports
  summary: The PREGO-attested record BTO:0004057 (fruit juice, EXACT/SEEDED, 2 TAXON
    assertions for Leuconostoc citreum and Leuconostoc pseudomesenteroides) is coherently
    grounded to BRENDA Tissue Ontology term BTO:0004057 under strictly broader BTO:0000659
    (juice, 'The extractable fluid contents of cells or tissues.') with 1 PREGO RELATED_SYNONYM
    ('fruit juices').
  snapshot_sha256: 1ae7408229392df98be954513b3a820c24d5d39c486f3aae00f59816e2faa439
- evidence_id: EREC7
  kind: record_content
  reference: data/habitats/host_associated/fruiting_body.yaml
  locator: Entire YAML
  accessed_at: '2026-11-11T06:06:00Z'
  support: supports
  summary: The curated GOLD record habitatmech:GOLD.92cbc36828 (fungal fruiting body,
    'Host-associated > Fungi > Fruiting body', UNGROUNDED/REVIEWED, 140 ORGANISM assertions)
    is coherently defined under ENVO:01001041 (fungi-associated environment) with
    bare 'Fruiting body' excluded from exact_synonyms and an evidence-backed 5-node/4-edge
    causal mechanism graph (PMID:38692852, PMID:23426012, PMID:35237850, PMID:33943006).
  snapshot_sha256: d4d18d1693fa24b535953d970d9f2d4603f7685f2343eab2c35b3d6bcbfe2597
- evidence_id: EREC8
  kind: record_content
  reference: data/habitats/host_associated/fungi.yaml
  locator: Entire YAML
  accessed_at: '2026-11-11T06:06:00Z'
  support: supports
  summary: The curated GOLD fungal-endosymbiont record habitatmech:GOLD.1ab59245f7
    (Fungi, 'Host-associated > Endosymbionts > Fungi', NARROW/REVIEWED, 5 ORGANISM
    assertions) coherently places the endofungal endosymbiont niche under ENVO:01001041
    (fungi-associated environment) and habitatmech:GOLD.895a2372e5 (host endosymbiont
    microhabitat), but emits mapping_predicate skos:narrowMatch on a minted source-path
    record (#1398).
  snapshot_sha256: a94d2c1a2e502490f2bcc20445701600899be0ec3c5f65cbeef63c3157abf933
- evidence_id: EREC9
  kind: record_content
  reference: data/habitats/host_associated/fungi_associated_environment.yaml
  locator: Entire YAML
  accessed_at: '2026-11-11T06:06:00Z'
  support: supports
  summary: The multi-source record ENVO:01001041 (fungi-associated environment, attested
    by ENVIRONMENTS_TABLE, GOLD 'Host-associated > Fungi' 635 ORGANISM assertions,
    and MADIN ENVO:01001041 38 TAXON assertions, EXACT/REVIEWED, 10 environmental
    parameters, 1 causal graph) promotes the bare host kingdom name 'Fungi' as an
    EXACT_SYNONYM from GOLD decision row 1580 (grounding_status=EXACT on habitatmech:GOLD.a8fc5001d1),
    conflating the fungal host kingdom with its associated environment.
  snapshot_sha256: 11b83dd57a7f805d6330e4a3054673dc72dc325456bd520942a359645eb56734
- evidence_id: EREC10
  kind: record_content
  reference: data/habitats/host_associated/g_cell.yaml
  locator: Entire YAML
  accessed_at: '2026-11-11T06:06:00Z'
  support: supports
  summary: The PREGO-attested record BTO:0004108 (G cell, EXACT/SEEDED, 1 TAXON assertion
    for Helicobacter pylori) is coherently grounded to BRENDA Tissue Ontology term
    BTO:0004108 ('Endocrine cells found in the pyloric gland mucosa (antral mucosa)
    of the stomach and responsible for the secretion of gastrin.').
  snapshot_sha256: 0b06ac2e7824a8ba7ad066fcf7a7eee3ae80cf83a23e04ccf33727ca3354be2a
- evidence_id: EREC11
  kind: record_content
  reference: data/habitats/host_associated/gall_bladder.yaml
  locator: Entire YAML
  accessed_at: '2026-11-11T06:06:00Z'
  support: supports
  summary: The multi-source record BTO:0000493 (gall bladder, attested by GOLD 'Host-associated
    > Fish > Digestive system > Biliary tract > Gall bladder' and PREGO BTO:0000493
    2 TAXON assertions, EXACT/REVIEWED) asserts the whole fish Biliary tract (habitatmech:GOLD.004065681a,
    'Host-associated > Fish > Digestive system > Biliary tract') in parent_habitats
    alongside BTO:0000123 (bladder), conflating part_of biliary-tract composition
    and fish-only host scope with is_a subtyping on the cross-vertebrate gallbladder
    class.
  snapshot_sha256: f61449421a483e738a30b16ed9fa444af60f17e45598c5c7ca0d5868d4524c92
- evidence_id: EREC12
  kind: record_content
  reference: data/habitats/host_associated/gallbladder.yaml
  locator: Entire YAML
  accessed_at: '2026-11-11T06:06:00Z'
  support: supports
  summary: 'The human Gallbladder record habitatmech:GOLD.0ec3770763 (''Host-associated
    > Mammals: Human > Digestive system > Biliary tract > Gallbladder'', NARROW/SEEDED)
    asserts the whole human Biliary tract (habitatmech:GOLD.133311ddf9, ''Host-associated
    > Mammals: Human > Digestive system > Biliary tract'') in parent_habitats alongside
    UBERON:0002110 (gallbladder), conflating part_of biliary-tract composition with
    is_a subtyping, and emits mapping_predicate skos:narrowMatch on a minted source-path
    record (#1398).'
  snapshot_sha256: 60a598bf70d54d17d13d60962e70768c1bb43c370ba0bf0a07bef7b4d7e42122
- evidence_id: EREC13
  kind: record_content
  reference: data/habitats/host_associated/gallbladder__d157697c.yaml
  locator: Entire YAML
  accessed_at: '2026-11-11T06:06:00Z'
  support: supports
  summary: The mammalian Gallbladder record habitatmech:GOLD.a84ac69a45 ('Host-associated
    > Mammals > Digestive system > Biliary tract > Gallbladder', NARROW/SEEDED) asserts
    the whole mammalian Biliary tract (habitatmech:GOLD.de5efc0eb8, 'Host-associated
    > Mammals > Digestive system > Biliary tract') in parent_habitats alongside UBERON:0002110
    (gallbladder), conflating part_of biliary-tract composition with is_a subtyping,
    and emits mapping_predicate skos:narrowMatch on a minted source-path record (#1398).
  snapshot_sha256: 4e9b91ea514d4d1f0617a76abe46721afd2773192cdd051db20aef1c77137e5c
- evidence_id: EREC14
  kind: record_content
  reference: data/habitats/host_associated/gallbladder_stones.yaml
  locator: Entire YAML
  accessed_at: '2026-11-11T06:06:00Z'
  support: supports
  summary: The curated GOLD gallstone record habitatmech:GOLD.7c37c0e048 (mammalian
    gallstone, 'Host-associated > Mammals > Digestive system > Biliary tract > Gallbladder
    stones', UNGROUNDED/REVIEWED) is coherently defined under ENVO:2100000 (anatomical
    entity environment) with parent_mode REPLACE and source-label exclusion for bare
    'Gallbladder stones'.
  snapshot_sha256: 661066689cf60513ece8fed247b5274db16cd65837a3a3b44076786f28153f6d
- evidence_id: EREC15
  kind: record_content
  reference: data/habitats/host_associated/gallbladder_stones__a31ee838.yaml
  locator: Entire YAML
  accessed_at: '2026-11-11T06:06:00Z'
  support: supports
  summary: 'The curated GOLD gallstone record habitatmech:GOLD.97738241e1 (human gallstone,
    ''Host-associated > Mammals: Human > Digestive system > Biliary tract > Gallbladder
    stones'', UNGROUNDED/REVIEWED) is coherently defined under ENVO:2100000 (anatomical
    entity environment) with parent_mode REPLACE and source-label exclusion for bare
    ''Gallbladder stones''.'
  snapshot_sha256: 8e0198617a663ee8bf04dd344600eb5e90d0d236da577d529d8482543c7dc5cc
- evidence_id: EREC16
  kind: record_content
  reference: data/habitats/host_associated/galls.yaml
  locator: Entire YAML
  accessed_at: '2026-11-11T06:06:00Z'
  support: supports
  summary: The plant root-gall record habitatmech:GOLD.fa99e76de1 (Galls, 'Host-associated
    > Plants > Roots > Galls', NARROW/REVIEWED, 4 ORGANISM assertions) asserts the
    whole plant root organ PO:0009005 (root) in parent_habitats alongside PO:0025626
    (plant gall), conflating anatomical host-organ location with is_a subtyping, and
    emits mapping_predicate skos:narrowMatch on a minted source-path record (#1398).
  snapshot_sha256: 9b3d44162a9d6dd499461e9c3a0b4beeda5d27bd1b189f6a7a49720c19495d91
- evidence_id: EREC17
  kind: record_content
  reference: data/habitats/host_associated/gametophyte.yaml
  locator: Entire YAML
  accessed_at: '2026-11-11T06:06:00Z'
  support: supports
  summary: The GOLD-attested record BTO:0000495 (gametophyte, 'Host-associated > Plants
    > Bryophytes > Moss > Gametophytes', habitatmech:GOLD.b66efd9c93, EXACT/REVIEWED)
    grounds a moss-specific gametophyte host environment to the generic whole-plant
    generation/form class BTO:0000495 ('The individual or generation of a plant exhibiting
    alternation of generations that bears sex organs.'), importing both morphological
    BTO:0000720 (plant form) and macro-scale biome ENVO:01000890 (area of moss-dominated
    vegetation) in parent_habitats.
  snapshot_sha256: 259dc02d4625e3abc226bc6d62a0b20b046a7564ffcb3fa8d3af71595a6b305a
- evidence_id: EREC18
  kind: record_content
  reference: data/habitats/host_associated/ganglion.yaml
  locator: Entire YAML
  accessed_at: '2026-11-11T06:06:00Z'
  support: supports
  summary: 'The GOLD-attested record UBERON:0000045 (ganglion, ''Host-associated >
    Mammals: Human > Benign tumor > Ganglion'', habitatmech:GOLD.dd1dd7acb8, EXACT/SEEDED)
    lexically grounds a human benign-tumor ganglion cyst source path to neural tissue
    mass UBERON:0000045 (''A biological tissue mass, most commonly a mass of nerve
    cell bodies.'') and asserts NOT_APPLICABLE disease parent habitatmech:GOLD.333c18201f
    (Benign tumor) in parent_habitats.'
  snapshot_sha256: e39ddd3161ba10522b1c13bf08c1720dd0bc3a5ad42586fe647fb8cd2814bd1a
- evidence_id: EREC19
  kind: record_content
  reference: data/habitats/host_associated/gaster.yaml
  locator: Entire YAML
  accessed_at: '2026-11-11T06:06:00Z'
  support: supports
  summary: 'The curated GOLD hymenopteran gaster record habitatmech:GOLD.623ff8e506
    (gaster environment, ''Host-associated > Arthropoda: Insects > Abdomen > Metasoma
    > Gaster'', UNGROUNDED/REVIEWED) asserts the whole metasoma environment (habitatmech:GOLD.93f0f7b66d,
    ''Host-associated > Arthropoda: Insects > Abdomen > Metasoma'') in parent_habitats
    alongside ENVO:01001002 (animal-associated environment), conflating anatomical
    part_of subdivision of the metasoma with is_a subtyping.'
  snapshot_sha256: c34203639b107c6028119754515374089e25a79a8563faea8f7f8d62cd2adf97
- evidence_id: EREC20
  kind: record_content
  reference: data/habitats/host_associated/gastric_caeca.yaml
  locator: Entire YAML
  accessed_at: '2026-11-11T06:06:00Z'
  support: supports
  summary: 'The curated GOLD record habitatmech:GOLD.8f1269c14c (insect midgut gastric
    cecum, ''Host-associated > Arthropoda: Insects > Digestive system > Midgut > Gastric
    caeca'', UNGROUNDED/REVIEWED, 1 ORGANISM assertion) is coherently defined under
    UBERON:0001045 (midgut) and insect Midgut (habitatmech:GOLD.67c565f695) with source-label
    exclusion for bare ''Gastric caeca'', matching sibling filter_chamber.yaml and
    mixed_segment.yaml.'
  snapshot_sha256: ef03bef1ca1dc6ce4524e4b2f6232651c9fd27e22ddd3e96e8302129554d0735
- evidence_id: EREC21
  kind: record_content
  reference: data/habitats/host_associated/gastric_caeca__12108999.yaml
  locator: Entire YAML
  accessed_at: '2026-11-11T06:06:00Z'
  support: supports
  summary: 'The curated GOLD record habitatmech:GOLD.ace43986bc (insect larval gastric
    caecum, ''Host-associated > Arthropoda: Insects > Larva > Gut > Gastric caeca'',
    UNGROUNDED/REVIEWED, 2 ORGANISM assertions) is coherently defined under UBERON:0001045
    (midgut) with parent_mode REPLACE and source-label exclusion for bare ''Gastric
    caeca''.'
  snapshot_sha256: 86e0224ec28ee9284cb9b59a46e5a9f5ea951a777fc9197fd07980ea19bc110c
- evidence_id: EREC22
  kind: record_content
  reference: data/habitats/host_associated/gastric_carcinoma.yaml
  locator: Entire YAML
  accessed_at: '2026-11-11T06:06:00Z'
  support: supports
  summary: 'The GOLD record habitatmech:GOLD.85aabc4062 (Gastric carcinoma, ''Host-associated
    > Mammals: Human > Malignant tumor > Carcinoma > Gastric carcinoma'', NOT_APPLICABLE/REVIEWED)
    is rightly marked NOT_APPLICABLE as a malignant neoplasm disease classification
    with MONDO:0001056 in xrefs, but retains NOT_APPLICABLE disease parent habitatmech:GOLD.9bb307824f
    (Carcinoma) in parent_habitats.'
  snapshot_sha256: de961f575d2d6e0dba70b2fdfc2c17eb210df89cd940b5af9909a5c3ade55bdf
- evidence_id: EREC23
  kind: record_content
  reference: data/habitats/host_associated/gastric_epithelium.yaml
  locator: Entire YAML
  accessed_at: '2026-11-11T06:06:00Z'
  support: supports
  summary: The PREGO-attested record BTO:0000500 (gastric epithelium, EXACT/SEEDED,
    2 TAXON assertions for Helicobacter pylori) is coherently grounded to BRENDA Tissue
    Ontology term BTO:0000500 ('Epithelium of the stomach.') under strictly broader
    BTO:0000416 (epithelium).
  snapshot_sha256: f15265925866e67517bc6ab20c308e4b75988683e58e910a0fc9f75ea224821c
- evidence_id: EREC24
  kind: record_content
  reference: data/habitats/host_associated/gastric_epithelium_cell_line.yaml
  locator: Entire YAML
  accessed_at: '2026-11-11T06:06:00Z'
  support: supports
  summary: The PREGO-attested record BTO:0004493 (gastric epithelium cell line, EXACT/SEEDED,
    2 TAXON assertions for Helicobacter pylori) is coherently grounded to BRENDA Tissue
    Ontology term BTO:0004493 under strictly broader BTO:0001088 (gastric cell line)
    and BTO:0001120 (epithelial cell line).
  snapshot_sha256: a100192f6a41e5e5e0071272da9318fdcec451ca8c95bd0e5a43eb0faa9b5adb
assessments:
- assessment_id: A1
  area: schema
  topic: Native validity and reproduction
  outcome: supported
  summary: All 24 cohort records pass LinkML schema validation, strict closed-schema
    validation, history validation (881 records), provenance verification, exact 3,209-record
    corpus reproduction, causal-graph validation (113 graphs), term-request check
    (676 terms), and OAK id-label correspondence.
  target_ids:
  - UBERON:0001760
  - habitatmech:GOLD.112979e260
  - habitatmech:GOLD.4be243a2b8
  - habitatmech:GOLD.7e21c19f98
  - BTO:0000486
  - BTO:0004057
  - habitatmech:GOLD.92cbc36828
  - habitatmech:GOLD.1ab59245f7
  - ENVO:01001041
  - BTO:0004108
  - BTO:0000493
  - habitatmech:GOLD.0ec3770763
  - habitatmech:GOLD.a84ac69a45
  - habitatmech:GOLD.7c37c0e048
  - habitatmech:GOLD.97738241e1
  - habitatmech:GOLD.fa99e76de1
  - BTO:0000495
  - UBERON:0000045
  - habitatmech:GOLD.623ff8e506
  - habitatmech:GOLD.8f1269c14c
  - habitatmech:GOLD.ace43986bc
  - habitatmech:GOLD.85aabc4062
  - BTO:0000500
  - BTO:0004493
  evidence_ids:
  - ERULE
  - ESCHEMA
  - ESEED
- assessment_id: A2
  area: scope
  topic: Cohort boundary and lumping/splitting evaluation
  outcome: supported
  summary: All 24 records represent distinct anatomical-site, frozen-remains, plant-organ/gall/gametophyte,
    fungal-environment, gallbladder/gallstone, hymenopteran-gaster, insect gastric-caeca,
    or human cyst/carcinoma/gastric-epithelium source concepts; no cross-record lumping
    or splitting is warranted across the cohort.
  target_ids:
  - UBERON:0001760
  - habitatmech:GOLD.112979e260
  - habitatmech:GOLD.4be243a2b8
  - habitatmech:GOLD.7e21c19f98
  - BTO:0000486
  - BTO:0004057
  - habitatmech:GOLD.92cbc36828
  - habitatmech:GOLD.1ab59245f7
  - ENVO:01001041
  - BTO:0004108
  - BTO:0000493
  - habitatmech:GOLD.0ec3770763
  - habitatmech:GOLD.a84ac69a45
  - habitatmech:GOLD.7c37c0e048
  - habitatmech:GOLD.97738241e1
  - habitatmech:GOLD.fa99e76de1
  - BTO:0000495
  - UBERON:0000045
  - habitatmech:GOLD.623ff8e506
  - habitatmech:GOLD.8f1269c14c
  - habitatmech:GOLD.ace43986bc
  - habitatmech:GOLD.85aabc4062
  - BTO:0000500
  - BTO:0004493
  evidence_ids:
  - EREC1
  - EREC2
  - EREC3
  - EREC4
  - EREC5
  - EREC6
  - EREC7
  - EREC8
  - EREC9
  - EREC10
  - EREC11
  - EREC12
  - EREC13
  - EREC14
  - EREC15
  - EREC16
  - EREC17
  - EREC18
  - EREC19
  - EREC20
  - EREC21
  - EREC22
  - EREC23
  - EREC24
  - ERULE
- assessment_id: A3
  area: grounding
  topic: Cohort hierarchy, synonym, and mapping-endpoint summary
  outcome: supported
  summary: '13 records pass with limitations; 11 records have 17 open findings (2
    blocker identity findings, 9 major grounding findings, 2 major nomenclature findings,
    and 4 major #1398 mapping-endpoint contract findings) recorded in their respective
    kind: record bundles (linked in related_reviews) and carried forward to Stage
    5 grouped remediation.'
  target_ids:
  - UBERON:0001760
  - habitatmech:GOLD.112979e260
  - habitatmech:GOLD.4be243a2b8
  - habitatmech:GOLD.7e21c19f98
  - BTO:0000486
  - BTO:0004057
  - habitatmech:GOLD.92cbc36828
  - habitatmech:GOLD.1ab59245f7
  - ENVO:01001041
  - BTO:0004108
  - BTO:0000493
  - habitatmech:GOLD.0ec3770763
  - habitatmech:GOLD.a84ac69a45
  - habitatmech:GOLD.7c37c0e048
  - habitatmech:GOLD.97738241e1
  - habitatmech:GOLD.fa99e76de1
  - BTO:0000495
  - UBERON:0000045
  - habitatmech:GOLD.623ff8e506
  - habitatmech:GOLD.8f1269c14c
  - habitatmech:GOLD.ace43986bc
  - habitatmech:GOLD.85aabc4062
  - BTO:0000500
  - BTO:0004493
  evidence_ids:
  - EREC1
  - EREC2
  - EREC3
  - EREC4
  - EREC5
  - EREC6
  - EREC7
  - EREC8
  - EREC9
  - EREC10
  - EREC11
  - EREC12
  - EREC13
  - EREC14
  - EREC15
  - EREC16
  - EREC17
  - EREC18
  - EREC19
  - EREC20
  - EREC21
  - EREC22
  - EREC23
  - EREC24
  - ERULE
  - ESCHEMA
  - ESEED
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - UBERON:0001760
  - habitatmech:GOLD.112979e260
  - habitatmech:GOLD.4be243a2b8
  - habitatmech:GOLD.7e21c19f98
  - BTO:0000486
  - BTO:0004057
  - habitatmech:GOLD.92cbc36828
  - habitatmech:GOLD.1ab59245f7
  - ENVO:01001041
  - BTO:0004108
  rationale: Retain frontal sinus (UBERON:0001760), the 3 host-clade frozen-remains
    records (avian, human, and fish), fruit (BTO:0000486), fruit juice (BTO:0004057),
    fungal fruiting body (habitatmech:GOLD.92cbc36828), endofungal endosymbiont niche
    (habitatmech:GOLD.1ab59245f7), fungi-associated environment (ENVO:01001041), and
    G cell (BTO:0004108) as distinct source-attested bins.
  evidence_ids:
  - EREC1
  - EREC2
  - EREC3
  - EREC4
  - EREC5
  - EREC6
  - EREC7
  - EREC8
  - EREC9
  - EREC10
  - ERULE
- action: retain
  target_ids:
  - BTO:0000493
  - habitatmech:GOLD.0ec3770763
  - habitatmech:GOLD.a84ac69a45
  - habitatmech:GOLD.7c37c0e048
  - habitatmech:GOLD.97738241e1
  - habitatmech:GOLD.fa99e76de1
  - BTO:0000495
  rationale: Retain cross-vertebrate/fish gall bladder (BTO:0000493), human and mammalian
    Gallbladder bins (habitatmech:GOLD.0ec3770763, habitatmech:GOLD.a84ac69a45), mammalian
    and human gallstone bins (habitatmech:GOLD.7c37c0e048, habitatmech:GOLD.97738241e1),
    plant root Galls (habitatmech:GOLD.fa99e76de1), and moss Gametophytes (currently
    grounded to BTO:0000495) as distinct anatomical and plant-associated bins.
  evidence_ids:
  - EREC11
  - EREC12
  - EREC13
  - EREC14
  - EREC15
  - EREC16
  - EREC17
  - ERULE
- action: retain
  target_ids:
  - UBERON:0000045
  - habitatmech:GOLD.623ff8e506
  - habitatmech:GOLD.8f1269c14c
  - habitatmech:GOLD.ace43986bc
  - habitatmech:GOLD.85aabc4062
  - BTO:0000500
  - BTO:0004493
  rationale: Retain human benign-tumor ganglion cyst (currently grounded to UBERON:0000045
    ganglion), hymenopteran gaster environment (habitatmech:GOLD.623ff8e506), insect
    midgut and larval gastric caeca (habitatmech:GOLD.8f1269c14c, habitatmech:GOLD.ace43986bc),
    NOT_APPLICABLE Gastric carcinoma (habitatmech:GOLD.85aabc4062), gastric epithelium
    (BTO:0000500), and gastric epithelium cell line (BTO:0004493) as distinct source-attested
    records.
  evidence_ids:
  - EREC18
  - EREC19
  - EREC20
  - EREC21
  - EREC22
  - EREC23
  - EREC24
  - ERULE
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261111T060510Z-frontal_sinus-record
  relationship: Component individual record review in this 24-record Cycle-9 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261111T060511Z-frozen_remains-record
  relationship: Component individual record review in this 24-record Cycle-9 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261111T060512Z-frozen_remains__584db35c-record
  relationship: Component individual record review in this 24-record Cycle-9 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261111T060513Z-frozen_remains__aa25d597-record
  relationship: Component individual record review in this 24-record Cycle-9 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261111T060514Z-fruit-record
  relationship: Component individual record review in this 24-record Cycle-9 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261111T060515Z-fruit_juice-record
  relationship: Component individual record review in this 24-record Cycle-9 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261111T060516Z-fruiting_body-record
  relationship: Component individual record review in this 24-record Cycle-9 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261111T060517Z-fungi-record
  relationship: Component individual record review in this 24-record Cycle-9 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261111T060518Z-fungi_associated_environment-record
  relationship: Component individual record review in this 24-record Cycle-9 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261111T060519Z-g_cell-record
  relationship: Component individual record review in this 24-record Cycle-9 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261111T060520Z-gall_bladder-record
  relationship: Component individual record review in this 24-record Cycle-9 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261111T060521Z-gallbladder-record
  relationship: Component individual record review in this 24-record Cycle-9 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261111T060522Z-gallbladder__d157697c-record
  relationship: Component individual record review in this 24-record Cycle-9 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261111T060523Z-gallbladder_stones-record
  relationship: Component individual record review in this 24-record Cycle-9 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261111T060524Z-gallbladder_stones__a31ee838-record
  relationship: Component individual record review in this 24-record Cycle-9 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261111T060525Z-galls-record
  relationship: Component individual record review in this 24-record Cycle-9 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261111T060526Z-gametophyte-record
  relationship: Component individual record review in this 24-record Cycle-9 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261111T060527Z-ganglion-record
  relationship: Component individual record review in this 24-record Cycle-9 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261111T060528Z-gaster-record
  relationship: Component individual record review in this 24-record Cycle-9 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261111T060529Z-gastric_caeca-record
  relationship: Component individual record review in this 24-record Cycle-9 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261111T060530Z-gastric_caeca__12108999-record
  relationship: Component individual record review in this 24-record Cycle-9 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261111T060531Z-gastric_carcinoma-record
  relationship: Component individual record review in this 24-record Cycle-9 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261111T060532Z-gastric_epithelium-record
  relationship: Component individual record review in this 24-record Cycle-9 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261111T060533Z-gastric_epithelium_cell_line-record
  relationship: Component individual record review in this 24-record Cycle-9 Stage-4
    cohort.
limitations:
- Only the stated primary evidence and current ontology/taxonomy authorities were
  independently inspected; original specimen-level support for every source-bin member
  is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism,
  or characteristic presence.
- Configured label correspondence skipped 2,106 no-adapter pairs; this is not whole-corpus
  identifier certification.
- 'Record-specific open findings (17 across 11 records: 2 blocker identity defects,
  9 major grounding/hierarchy defects, 2 major nomenclature synonym defects, and 4
  major #1398 mapping-endpoint contract defects) are recorded on their respective
  kind: record bundles in related_reviews so each issue_key has a single authoritative
  open owner for Stage 5 remediation.'
notes:
- All 24 cohort target files and context inputs were captured at clean git commit
  83aa5f212521389cb9c3507ded58d0bcd0a22ee0.
- 'Each of the 24 targets has a dedicated kind: record bundle in reviews/structured/.'
tags:
- category-cohort-review
- host-associated
```
