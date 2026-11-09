# Category cohort review: host_associated slice finger through free_living_state (24 records)

- Review: 20261109T181100Z-finger_to_free_living_state-category
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-09T18:08:00Z
- Finished UTC: 2026-11-09T18:11:00Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Full 24-record category boundary and cohort review of the contiguous unreviewed host_associated slice (finger.yaml through free_living_state.yaml) at commit 19d3ccb65e6b5128b9b0a5ae39cb509bf3f2bf39. All 24 records represent distinct anatomical-site, host-environment, cellular/organism-form, foregut, lymph-node, forestomach, fossil-remains, or insect-frass source concepts (retain decisions; no cross-record lumping or splitting). Record-level open findings (23 total across 13 records) are recorded in the 24 linked kind: record bundles for Stage 5 remediation.

## Scope And Provenance

Contiguous 24-record cohort boundary review of previously unreviewed records in data/habitats/host_associated/ (indices 530-553 in path order).

Selection: Next 24 unreviewed records in data/habitats/host_associated/ immediately following 20261108T114933Z-fin-record.
Coverage: full; 24 reviewed / 24 in the declared population.
Source: git_commit at Git base 19d3ccb65e6b5128b9b0a5ae39cb509bf3f2bf39.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0004669 | data/habitats/host_associated/finger.yaml | generated | finger |
| habitatmech:GOLD.3d529a667e | data/habitats/host_associated/fish.yaml | generated | fish-associated environment |
| BTO:0000464 | data/habitats/host_associated/flagellate.yaml | generated | flagellate |
| BTO:0002292 | data/habitats/host_associated/flagellum.yaml | generated | flagellum |
| habitatmech:GOLD.79193f14f9 | data/habitats/host_associated/flat_warts.yaml | generated | human flat wart |
| BTO:0000469 | data/habitats/host_associated/flower.yaml | generated | flower |
| BTO:0000476 | data/habitats/host_associated/foot.yaml | generated | foot |
| habitatmech:GOLD.0a9f2ca319 | data/habitats/host_associated/foraminifera.yaml | generated | foraminiferan-associated environment |
| BTO:0001447 | data/habitats/host_associated/forearm.yaml | generated | forearm |
| BTO:0000507 | data/habitats/host_associated/foregut.yaml | generated | foregut |
| habitatmech:GOLD.52f22e84ee | data/habitats/host_associated/foregut__6bc8c43a.yaml | generated | Foregut |
| habitatmech:GOLD.cd6e81f421 | data/habitats/host_associated/foregut__c14450a8.yaml | generated | Foregut |
| habitatmech:GOLD.bd1664969c | data/habitats/host_associated/foregut__ce63e8ab.yaml | generated | Foregut |
| habitatmech:GOLD.8997340b18 | data/habitats/host_associated/foregut__d14a54ae.yaml | generated | Foregut |
| habitatmech:GOLD.fe78a4c113 | data/habitats/host_associated/foregut__ee6a8f74.yaml | generated | Foregut |
| BTO:0006514 | data/habitats/host_associated/foreleg.yaml | generated | foreleg |
| BTO:0000480 | data/habitats/host_associated/forestomach.yaml | generated | forestomach |
| habitatmech:GOLD.4af8939c1f | data/habitats/host_associated/fossilized_remains.yaml | generated | fossilized avian remains |
| habitatmech:GOLD.76df031f74 | data/habitats/host_associated/fossilized_remains__19772eb4.yaml | generated | fossilized fish remains |
| habitatmech:GOLD.f1a2eca320 | data/habitats/host_associated/fossilized_remains__8b01c49f.yaml | generated | fossilized hominin remains |
| habitatmech:GOLD.c5640eadf7 | data/habitats/host_associated/fossilized_remains__eec3c6e8.yaml | generated | fossilized mammalian remains |
| habitatmech:GOLD.319c3f351e | data/habitats/host_associated/frass.yaml | generated | Frass |
| habitatmech:GOLD.67f3cde908 | data/habitats/host_associated/frass__c029dd2b.yaml | generated | Frass |
| BTO:0001551 | data/habitats/host_associated/free_living_state.yaml | generated | free-living state |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0004669, habitatmech:GOLD.3d529a667e, BTO:0000464, BTO:0002292, habitatmech:GOLD.79193f14f9, BTO:0000469, BTO:0000476, habitatmech:GOLD.0a9f2ca319, BTO:0001447, BTO:0000507, habitatmech:GOLD.52f22e84ee, habitatmech:GOLD.cd6e81f421, habitatmech:GOLD.bd1664969c, habitatmech:GOLD.8997340b18, habitatmech:GOLD.fe78a4c113, BTO:0006514, BTO:0000480, habitatmech:GOLD.4af8939c1f, habitatmech:GOLD.76df031f74, habitatmech:GOLD.f1a2eca320, habitatmech:GOLD.c5640eadf7, habitatmech:GOLD.319c3f351e, habitatmech:GOLD.67f3cde908, BTO:0001551 | Completed 2026-11-09T18:08:48Z. No issues found. |
| validate-strict | passed | True | BTO:0004669, habitatmech:GOLD.3d529a667e, BTO:0000464, BTO:0002292, habitatmech:GOLD.79193f14f9, BTO:0000469, BTO:0000476, habitatmech:GOLD.0a9f2ca319, BTO:0001447, BTO:0000507, habitatmech:GOLD.52f22e84ee, habitatmech:GOLD.cd6e81f421, habitatmech:GOLD.bd1664969c, habitatmech:GOLD.8997340b18, habitatmech:GOLD.fe78a4c113, BTO:0006514, BTO:0000480, habitatmech:GOLD.4af8939c1f, habitatmech:GOLD.76df031f74, habitatmech:GOLD.f1a2eca320, habitatmech:GOLD.c5640eadf7, habitatmech:GOLD.319c3f351e, habitatmech:GOLD.67f3cde908, BTO:0001551 | Completed 2026-11-09T18:08:54Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | BTO:0004669, habitatmech:GOLD.3d529a667e, BTO:0000464, BTO:0002292, habitatmech:GOLD.79193f14f9, BTO:0000469, BTO:0000476, habitatmech:GOLD.0a9f2ca319, BTO:0001447, BTO:0000507, habitatmech:GOLD.52f22e84ee, habitatmech:GOLD.cd6e81f421, habitatmech:GOLD.bd1664969c, habitatmech:GOLD.8997340b18, habitatmech:GOLD.fe78a4c113, BTO:0006514, BTO:0000480, habitatmech:GOLD.4af8939c1f, habitatmech:GOLD.76df031f74, habitatmech:GOLD.f1a2eca320, habitatmech:GOLD.c5640eadf7, habitatmech:GOLD.319c3f351e, habitatmech:GOLD.67f3cde908, BTO:0001551 | Completed 2026-11-09T18:09:00Z. No issues found; 876 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | BTO:0004669, habitatmech:GOLD.3d529a667e, BTO:0000464, BTO:0002292, habitatmech:GOLD.79193f14f9, BTO:0000469, BTO:0000476, habitatmech:GOLD.0a9f2ca319, BTO:0001447, BTO:0000507, habitatmech:GOLD.52f22e84ee, habitatmech:GOLD.cd6e81f421, habitatmech:GOLD.bd1664969c, habitatmech:GOLD.8997340b18, habitatmech:GOLD.fe78a4c113, BTO:0006514, BTO:0000480, habitatmech:GOLD.4af8939c1f, habitatmech:GOLD.76df031f74, habitatmech:GOLD.f1a2eca320, habitatmech:GOLD.c5640eadf7, habitatmech:GOLD.319c3f351e, habitatmech:GOLD.67f3cde908, BTO:0001551 | Completed 2026-11-09T18:09:01Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | BTO:0004669, habitatmech:GOLD.3d529a667e, BTO:0000464, BTO:0002292, habitatmech:GOLD.79193f14f9, BTO:0000469, BTO:0000476, habitatmech:GOLD.0a9f2ca319, BTO:0001447, BTO:0000507, habitatmech:GOLD.52f22e84ee, habitatmech:GOLD.cd6e81f421, habitatmech:GOLD.bd1664969c, habitatmech:GOLD.8997340b18, habitatmech:GOLD.fe78a4c113, BTO:0006514, BTO:0000480, habitatmech:GOLD.4af8939c1f, habitatmech:GOLD.76df031f74, habitatmech:GOLD.f1a2eca320, habitatmech:GOLD.c5640eadf7, habitatmech:GOLD.319c3f351e, habitatmech:GOLD.67f3cde908, BTO:0001551 | Completed 2026-11-09T18:09:16Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | BTO:0004669, habitatmech:GOLD.3d529a667e, BTO:0000464, BTO:0002292, habitatmech:GOLD.79193f14f9, BTO:0000469, BTO:0000476, habitatmech:GOLD.0a9f2ca319, BTO:0001447, BTO:0000507, habitatmech:GOLD.52f22e84ee, habitatmech:GOLD.cd6e81f421, habitatmech:GOLD.bd1664969c, habitatmech:GOLD.8997340b18, habitatmech:GOLD.fe78a4c113, BTO:0006514, BTO:0000480, habitatmech:GOLD.4af8939c1f, habitatmech:GOLD.76df031f74, habitatmech:GOLD.f1a2eca320, habitatmech:GOLD.c5640eadf7, habitatmech:GOLD.319c3f351e, habitatmech:GOLD.67f3cde908, BTO:0001551 | Completed 2026-11-09T18:09:22Z. validated 103 causal-graph curation file(s) with 103 graph(s). |
| term-requests-check | passed | True | BTO:0004669, habitatmech:GOLD.3d529a667e, BTO:0000464, BTO:0002292, habitatmech:GOLD.79193f14f9, BTO:0000469, BTO:0000476, habitatmech:GOLD.0a9f2ca319, BTO:0001447, BTO:0000507, habitatmech:GOLD.52f22e84ee, habitatmech:GOLD.cd6e81f421, habitatmech:GOLD.bd1664969c, habitatmech:GOLD.8997340b18, habitatmech:GOLD.fe78a4c113, BTO:0006514, BTO:0000480, habitatmech:GOLD.4af8939c1f, habitatmech:GOLD.76df031f74, habitatmech:GOLD.f1a2eca320, habitatmech:GOLD.c5640eadf7, habitatmech:GOLD.319c3f351e, habitatmech:GOLD.67f3cde908, BTO:0001551 | Completed 2026-11-09T18:09:36Z. term-request table is current (674 terms). |
| validate-products | passed | True | BTO:0004669, habitatmech:GOLD.3d529a667e, BTO:0000464, BTO:0002292, habitatmech:GOLD.79193f14f9, BTO:0000469, BTO:0000476, habitatmech:GOLD.0a9f2ca319, BTO:0001447, BTO:0000507, habitatmech:GOLD.52f22e84ee, habitatmech:GOLD.cd6e81f421, habitatmech:GOLD.bd1664969c, habitatmech:GOLD.8997340b18, habitatmech:GOLD.fe78a4c113, BTO:0006514, BTO:0000480, habitatmech:GOLD.4af8939c1f, habitatmech:GOLD.76df031f74, habitatmech:GOLD.f1a2eca320, habitatmech:GOLD.c5640eadf7, habitatmech:GOLD.319c3f351e, habitatmech:GOLD.67f3cde908, BTO:0001551 | Completed 2026-11-09T18:10:17Z. OK_CANONICAL: 1213, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2094. All id&lt;-&gt;label pairs correspond. |

## Scientific And Domain Assessments

### Native validity and reproduction

schema: supported. Targets: BTO:0004669, habitatmech:GOLD.3d529a667e, BTO:0000464, BTO:0002292, habitatmech:GOLD.79193f14f9, BTO:0000469, BTO:0000476, habitatmech:GOLD.0a9f2ca319, BTO:0001447, BTO:0000507, habitatmech:GOLD.52f22e84ee, habitatmech:GOLD.cd6e81f421, habitatmech:GOLD.bd1664969c, habitatmech:GOLD.8997340b18, habitatmech:GOLD.fe78a4c113, BTO:0006514, BTO:0000480, habitatmech:GOLD.4af8939c1f, habitatmech:GOLD.76df031f74, habitatmech:GOLD.f1a2eca320, habitatmech:GOLD.c5640eadf7, habitatmech:GOLD.319c3f351e, habitatmech:GOLD.67f3cde908, BTO:0001551.

All 24 cohort records pass LinkML schema validation, strict closed-schema validation, history validation (876 records), provenance verification, exact 3,209-record corpus reproduction, causal-graph validation (103 graphs), term-request check (674 terms), and OAK id-label correspondence.

### Cohort boundary and lumping/splitting evaluation

scope: supported. Targets: BTO:0004669, habitatmech:GOLD.3d529a667e, BTO:0000464, BTO:0002292, habitatmech:GOLD.79193f14f9, BTO:0000469, BTO:0000476, habitatmech:GOLD.0a9f2ca319, BTO:0001447, BTO:0000507, habitatmech:GOLD.52f22e84ee, habitatmech:GOLD.cd6e81f421, habitatmech:GOLD.bd1664969c, habitatmech:GOLD.8997340b18, habitatmech:GOLD.fe78a4c113, BTO:0006514, BTO:0000480, habitatmech:GOLD.4af8939c1f, habitatmech:GOLD.76df031f74, habitatmech:GOLD.f1a2eca320, habitatmech:GOLD.c5640eadf7, habitatmech:GOLD.319c3f351e, habitatmech:GOLD.67f3cde908, BTO:0001551.

All 24 records represent distinct anatomical-site, host-environment, organism-form/organelle, host-scoped foregut, forelimb lymph-node, forestomach, fossilized-remains, or insect-frass source concepts; no cross-record lumping or splitting is warranted across the cohort.

### Cohort hierarchy, synonym, and mapping-endpoint summary

grounding: supported. Targets: BTO:0004669, habitatmech:GOLD.3d529a667e, BTO:0000464, BTO:0002292, habitatmech:GOLD.79193f14f9, BTO:0000469, BTO:0000476, habitatmech:GOLD.0a9f2ca319, BTO:0001447, BTO:0000507, habitatmech:GOLD.52f22e84ee, habitatmech:GOLD.cd6e81f421, habitatmech:GOLD.bd1664969c, habitatmech:GOLD.8997340b18, habitatmech:GOLD.fe78a4c113, BTO:0006514, BTO:0000480, habitatmech:GOLD.4af8939c1f, habitatmech:GOLD.76df031f74, habitatmech:GOLD.f1a2eca320, habitatmech:GOLD.c5640eadf7, habitatmech:GOLD.319c3f351e, habitatmech:GOLD.67f3cde908, BTO:0001551.

11 records pass with limitations; 13 records have 23 open findings (4 blocker identity findings, 11 major grounding findings, 1 major nomenclature finding, and 7 major #1398 mapping-endpoint contract findings) recorded in their respective kind: record bundles (linked in related_reviews) and carried forward to Stage 5 grouped remediation.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: BTO:0004669, habitatmech:GOLD.3d529a667e, BTO:0000464, BTO:0002292, habitatmech:GOLD.79193f14f9, BTO:0000469, BTO:0000476, habitatmech:GOLD.0a9f2ca319, BTO:0001447. Retain finger (BTO:0004669), fish-associated environment (habitatmech:GOLD.3d529a667e), PREGO flagellate (BTO:0000464), PREGO flagellum (BTO:0002292), human flat wart (habitatmech:GOLD.79193f14f9), flower (BTO:0000469), foot (BTO:0000476), foraminiferan-associated environment (habitatmech:GOLD.0a9f2ca319), and forearm (BTO:0001447) as distinct source-attested bins (with item-level identity/synonym remediations tracked on fish, flagellate, and flagellum).
- retain: BTO:0000507, habitatmech:GOLD.52f22e84ee, habitatmech:GOLD.cd6e81f421, habitatmech:GOLD.bd1664969c, habitatmech:GOLD.8997340b18, habitatmech:GOLD.fe78a4c113, BTO:0006514, BTO:0000480. Retain cross-host PREGO foregut (BTO:0000507), the 5 host-scoped GOLD Foregut bins (fish, mammalian, insect, myriapod, and crustacean), mammalian forelimb lymph node (currently grounded to BTO:0006514 foreleg), and mammalian forestomach (BTO:0000480) as distinct anatomical and host-scoped digestive/lymphatic bins.
- retain: habitatmech:GOLD.4af8939c1f, habitatmech:GOLD.76df031f74, habitatmech:GOLD.f1a2eca320, habitatmech:GOLD.c5640eadf7, habitatmech:GOLD.319c3f351e, habitatmech:GOLD.67f3cde908, BTO:0001551. Retain the 4 host-clade fossilized-remains records (avian, fish, hominin, and mammalian), the 2 insect Frass records (larval gut and insect hindgut origin), and PREGO free-living state (BTO:0001551) as distinct source-attested records.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon, organism-form, and subcellular organelle terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator resolution routes and parent/synonym assembly verified across all 24 cohort target records. |
| EREC1 | data/habitats/host_associated/finger.yaml; Entire YAML | supports | The PREGO-attested record BTO:0004669 (finger, EXACT/SEEDED, 9 TAXON assertions) is coherently grounded to BRENDA Tissue Ontology term BTO:0004669 with its vendored anatomical definition, 4 PREGO RELATED_SYNONYMs ('digits', 'fingers', 'forelimb digit', 'forelimb digits'), and 9 displayed characteristic taxa. |
| EREC2 | data/habitats/host_associated/fish.yaml; Entire YAML | supports | The curated GOLD host-environment record habitatmech:GOLD.3d529a667e (fish-associated environment, UNGROUNDED/REVIEWED, 1,350 ORGANISM assertions) has a sound definition and parent_habitats (ENVO:01001000, ENVO:01001002), but curation/term_requests.tsv row 9 retains the bare host clade name 'Fish' in exact_synonym, emitting 'Fish' as an EXACT_SYNONYM on the environment record. |
| EREC3 | data/habitats/host_associated/flagellate.yaml; Entire YAML | supports | The PREGO-attested record BTO:0000464 (flagellate, 'A flagellate protozoan or alga.', EXACT/SEEDED, 9 TAXON assertions) uses a morphological whole-organism form class as a microbial habitat identity and imports organism-form classes BTO:0000720 (plant form) and BTO:0002503 (protozoan form) in parent_habitats. |
| EREC4 | data/habitats/host_associated/flagellum.yaml; Entire YAML | supports | The PREGO-attested record BTO:0002292 (flagellum, biolink:CellularComponent in data/raw/prego_habitats.tsv row 497, 140 TAXON assertions across flagellated bacteria such as Escherichia coli, Salmonella enterica, and Bacillus) uses a subcellular motility organelle identity as a host-associated microbial habitat and imports whole-organism form BTO:0000464 (flagellate) in parent_habitats. |
| EREC5 | data/habitats/host_associated/flat_warts.yaml; Entire YAML | supports | The curated GOLD record habitatmech:GOLD.79193f14f9 (human flat wart, 'Host-associated &gt; Mammals: Human &gt; Benign tumor &gt; Wart &gt; Flat warts', UNGROUNDED/REVIEWED) is coherently defined as a human cutaneous wart habitat under BTO:0001859 (wart) with parent_mode REPLACE and source-label exclusion for bare 'Flat warts'. |
| EREC6 | data/habitats/host_associated/flower.yaml; Entire YAML | supports | The PREGO-attested record BTO:0000469 (flower, EXACT/SEEDED, 6 TAXON assertions) is coherently grounded to BRENDA Tissue Ontology term BTO:0000469 ('The reproductive structure of angiosperms.') with 1 PREGO RELATED_SYNONYM ('flowers') and 6 displayed characteristic taxa. |
| EREC7 | data/habitats/host_associated/foot.yaml; Entire YAML | supports | The BacDive-attested record BTO:0000476 (foot, 'bacdive.isolation_source:foot', EXACT/REVIEWED, 114 STRAIN assertions) is coherently grounded to BRENDA Tissue Ontology term BTO:0000476 ('The terminal part of the vertebrate leg upon which an individual stands.') under BTO:0001492 (lower limb) with 10 displayed characteristic taxa from the 107-row BacDive pool. |
| EREC8 | data/habitats/host_associated/foraminifera.yaml; Entire YAML | supports | The curated GOLD host-environment record habitatmech:GOLD.0a9f2ca319 (foraminiferan-associated environment, 'Host-associated &gt; Protists &gt; Rhizaria &gt; Foraminifera', UNGROUNDED/REVIEWED, 6 ORGANISM assertions) is coherently defined under ENVO:01001000 (environmental system determined by an organism) and habitatmech:GOLD.6b259c237e (rhizarian-associated environment) with exact_synonym 'foraminiferal host environment' and source-label exclusion for bare 'Foraminifera'. |
| EREC9 | data/habitats/host_associated/forearm.yaml; Entire YAML | supports | The PREGO-attested record BTO:0001447 (forearm, EXACT/SEEDED, 404 TAXON assertions) is coherently grounded to BRENDA Tissue Ontology term BTO:0001447 ('The part of the superior limb between the elbow and the wrist.') with 2 PREGO RELATED_SYNONYMs ('forearmic', 'forearms') and 10 displayed characteristic taxa from the 404-row PREGO pool. |
| EREC10 | data/habitats/host_associated/foregut.yaml; Entire YAML | supports | The PREGO-attested record BTO:0000507 (foregut, EXACT/SEEDED, 92 TAXON assertions) is coherently grounded to BRENDA Tissue Ontology term BTO:0000507 with its vendored anatomical definition, 1 PREGO RELATED_SYNONYM ('foreguts'), and 10 displayed characteristic taxa from the 92-row PREGO pool. |
| EREC11 | data/habitats/host_associated/foregut__6bc8c43a.yaml; Entire YAML | supports | The fish foregut record habitatmech:GOLD.52f22e84ee ('Host-associated &gt; Fish &gt; Digestive system &gt; Foregut', NARROW/SEEDED) asserts the whole fish Digestive system (habitatmech:GOLD.8a68d0f6f5, 'Host-associated &gt; Fish &gt; Digestive system') in parent_habitats alongside UBERON:0001041 (foregut), conflating part_of digestive-system composition with is_a habitat subtyping, and emits mapping_predicate skos:narrowMatch on a minted source-path record (#1398). |
| EREC12 | data/habitats/host_associated/foregut__c14450a8.yaml; Entire YAML | supports | The mammalian foregut record habitatmech:GOLD.cd6e81f421 ('Host-associated &gt; Mammals &gt; Digestive system &gt; Foregut', NARROW/SEEDED) asserts the whole mammalian Digestive system (habitatmech:GOLD.c8e85f3c84, 'Host-associated &gt; Mammals &gt; Digestive system') in parent_habitats alongside UBERON:0001041 (foregut), conflating part_of digestive-system composition with is_a habitat subtyping, and emits mapping_predicate skos:narrowMatch on a minted source-path record (#1398). |
| EREC13 | data/habitats/host_associated/foregut__ce63e8ab.yaml; Entire YAML | supports | The insect foregut record habitatmech:GOLD.bd1664969c ('Host-associated &gt; Arthropoda: Insects &gt; Digestive system &gt; Foregut', NARROW/SEEDED) asserts the whole insect Digestive system (habitatmech:GOLD.d7cff86ce8, 'Host-associated &gt; Arthropoda: Insects &gt; Digestive system') in parent_habitats alongside UBERON:0001041 (foregut), conflating part_of digestive-system composition with is_a habitat subtyping, and emits mapping_predicate skos:narrowMatch on a minted source-path record (#1398). |
| EREC14 | data/habitats/host_associated/foregut__d14a54ae.yaml; Entire YAML | supports | The myriapod foregut record habitatmech:GOLD.8997340b18 ('Host-associated &gt; Arthropoda: Myriapoda &gt; Digestive system &gt; Foregut', NARROW/SEEDED) asserts the whole myriapod Digestive system (habitatmech:GOLD.acc41d1792, 'Host-associated &gt; Arthropoda: Myriapoda &gt; Digestive system') in parent_habitats alongside UBERON:0001041 (foregut), conflating part_of digestive-system composition with is_a habitat subtyping, and emits mapping_predicate skos:narrowMatch on a minted source-path record (#1398). |
| EREC15 | data/habitats/host_associated/foregut__ee6a8f74.yaml; Entire YAML | supports | The crustacean foregut record habitatmech:GOLD.fe78a4c113 ('Host-associated &gt; Arthropoda: Crustaceans &gt; Digestive system &gt; Foregut', NARROW/SEEDED) asserts the whole crustacean Digestive system (habitatmech:GOLD.6eecdf150d, 'Host-associated &gt; Arthropoda: Crustaceans &gt; Digestive system') in parent_habitats alongside UBERON:0001041 (foregut), conflating part_of digestive-system composition with is_a habitat subtyping, and emits mapping_predicate skos:narrowMatch on a minted source-path record (#1398). |
| EREC16 | data/habitats/host_associated/foreleg.yaml; Entire YAML | supports | The GOLD-attested record BTO:0006514 (foreleg, 'A front leg.', EXACT/REVIEWED) grounds GOLD path 'Host-associated &gt; Mammals &gt; Lymphatic system &gt; Lymph nodes &gt; Forelegs' (habitatmech:GOLD.80220dc4d4) to the whole front limb BTO:0006514 rather than a mammalian forelimb lymph node (parallel to hind_legs.yaml habitatmech:GOLD.ca4882ca81), causing BTO:0006514 to assert both BTO:0000721 (limb) and UBERON:0000029 (lymph node) in parent_habitats. |
| EREC17 | data/habitats/host_associated/forestomach.yaml; Entire YAML | supports | The multi-source record BTO:0000480 (forestomach, attested by GOLD 'Host-associated &gt; Mammals &gt; Digestive system &gt; Stomach &gt; Forestomach' and PREGO BTO:0000480, EXACT/REVIEWED, 1 TAXON assertion) asserts the whole mammalian Stomach (habitatmech:GOLD.d3869ad37f, 'Host-associated &gt; Mammals &gt; Digestive system &gt; Stomach') in parent_habitats alongside BTO:0001307 (stomach), conflating anatomical compartment part_of composition with is_a subtyping. |
| EREC18 | data/habitats/host_associated/fossilized_remains.yaml; Entire YAML | supports | The curated GOLD fossil-remains record habitatmech:GOLD.4af8939c1f (fossilized avian remains, 'Host-associated &gt; Birds &gt; Remains &gt; Fossilized remains', UNGROUNDED/REVIEWED) is coherently defined under ENVO:00002164 (fossil material) with parent_mode REPLACE and source-label exclusion for bare 'Fossilized remains'. |
| EREC19 | data/habitats/host_associated/fossilized_remains__19772eb4.yaml; Entire YAML | supports | The curated GOLD fossil-remains record habitatmech:GOLD.76df031f74 (fossilized fish remains, 'Host-associated &gt; Fish &gt; Remains &gt; Fossilized remains', UNGROUNDED/REVIEWED) is coherently defined under ENVO:00002164 (fossil material) with parent_mode REPLACE and source-label exclusion for bare 'Fossilized remains'. |
| EREC20 | data/habitats/host_associated/fossilized_remains__8b01c49f.yaml; Entire YAML | supports | The curated GOLD fossil-remains record habitatmech:GOLD.f1a2eca320 (fossilized hominin remains, 'Host-associated &gt; Mammals: Human &gt; Remains &gt; Fossilized remains', UNGROUNDED/REVIEWED) is coherently defined under ENVO:00002164 (fossil material) with parent_mode REPLACE and source-label exclusion for bare 'Fossilized remains'. |
| EREC21 | data/habitats/host_associated/fossilized_remains__eec3c6e8.yaml; Entire YAML | supports | The curated GOLD fossil-remains record habitatmech:GOLD.c5640eadf7 (fossilized mammalian remains, 'Host-associated &gt; Mammals &gt; Remains &gt; Fossilized remains', UNGROUNDED/REVIEWED) is coherently defined under ENVO:00002164 (fossil material) with parent_mode REPLACE and source-label exclusion for bare 'Fossilized remains'. |
| EREC22 | data/habitats/host_associated/frass.yaml; Entire YAML | supports | The insect frass record habitatmech:GOLD.319c3f351e ('Host-associated &gt; Arthropoda: Insects &gt; Larva &gt; Gut &gt; Frass', NARROW/SEEDED) asserts the anatomical organ habitatmech:GOLD.d4e02cf775 ('Host-associated &gt; Arthropoda: Insects &gt; Larva &gt; Gut') in parent_habitats alongside ENVO:00002003 (fecal material), conflating anatomical origin with is_a habitat subtyping, and emits mapping_predicate skos:narrowMatch on a minted source-path record (#1398). |
| EREC23 | data/habitats/host_associated/frass__c029dd2b.yaml; Entire YAML | supports | The insect frass record habitatmech:GOLD.67f3cde908 ('Host-associated &gt; Arthropoda: Insects &gt; Digestive system &gt; Hindgut &gt; Frass', NARROW/SEEDED) asserts the anatomical organ habitatmech:GOLD.50722c7871 ('Host-associated &gt; Arthropoda: Insects &gt; Digestive system &gt; Hindgut') in parent_habitats alongside ENVO:00002003 (fecal material), conflating anatomical origin with is_a habitat subtyping, and emits mapping_predicate skos:narrowMatch on a minted source-path record (#1398). |
| EREC24 | data/habitats/host_associated/free_living_state.yaml; Entire YAML | supports | The PREGO-attested record BTO:0001551 (free-living state, definition: null, child of BTO:0000284 organism form, 3 TAXON assertions for Bradyrhizobium sp. DOA9, Escherichia coli str. K-12 substr. W3110, and Azorhizobium caulinodans ORS 571) uses a microbial physiological/lifestyle organism-form state as a host-associated habitat identity and asserts BTO:0000284 (organism form) in parent_habitats. |

## Limits And Additional Notes

- Only the stated primary evidence and current ontology/taxonomy authorities were independently inspected; original specimen-level support for every source-bin member is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism, or characteristic presence.
- Configured label correspondence skipped 2,094 no-adapter pairs; this is not whole-corpus identifier certification.
- Record-specific open findings (23 across 13 records: 4 blocker identity defects, 11 major grounding/hierarchy defects, 1 major nomenclature exact_synonyms defect, and 7 major #1398 mapping-endpoint contract defects) are recorded on their respective kind: record bundles in related_reviews so each issue_key has a single authoritative open owner for Stage 5 remediation.
- All 24 cohort target files and context inputs were captured at clean git commit 19d3ccb65e6b5128b9b0a5ae39cb509bf3f2bf39.
- Each of the 24 targets has a dedicated kind: record bundle in reviews/structured/.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T181100Z-finger_to_free_living_state-category
repository: CultureBotAI/HabitatMech
kind: category
title: 'Category cohort review: host_associated slice finger through free_living_state
  (24 records)'
started_at: '2026-11-09T18:08:00Z'
finished_at: '2026-11-09T18:11:00Z'
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
  host_associated slice (finger.yaml through free_living_state.yaml) at commit 19d3ccb65e6b5128b9b0a5ae39cb509bf3f2bf39.
  All 24 records represent distinct anatomical-site, host-environment, cellular/organism-form,
  foregut, lymph-node, forestomach, fossil-remains, or insect-frass source concepts
  (retain decisions; no cross-record lumping or splitting). Record-level open findings
  (23 total across 13 records) are recorded in the 24 linked kind: record bundles
  for Stage 5 remediation.'
source:
  git_revision: 19d3ccb65e6b5128b9b0a5ae39cb509bf3f2bf39
  state: git_commit
  inputs:
  - path: curation/decisions.tsv
    sha256: d3bf0a3ca3570e8f318898db92f800a1e13220f64112fe5c1ce1edc9181c3ae2
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: f53415b9d57f351620a1722c7c83414983899dd9a4559d42e9a094a3e8f501e8
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: f004c15e7d206d673bdd9e6d051f6fce93c8a06ebe4db6026149d4d00c49cc9e
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: c1207270bb0ae2031e42de6cb8220b20f98886f65e40d48793bfd7e9d757d83a
    role: context
  - path: curation/term_requests.tsv
    sha256: ad853d6290dd72b2451d945a0545a5dc5272cc37c2296eaab78c99d2872d4b0c
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: ee559f7b45b4af2d72a078c45d1a3b676785d34305f286e9738f95771dbaccfd
    role: context
  - path: data/habitats/host_associated/adult.yaml
    sha256: 91c41fc8a4d72c43682756d0e29562fbf92e27e198d386fc5847a6c8961e4e04
    role: context
  - path: data/habitats/host_associated/birds.yaml
    sha256: 2de4c694d7ca103897d519fd7fbef6d955a9c2502f6045aa8c56d4af09204aae
    role: context
  - path: data/habitats/host_associated/digestive_system__2589c8ce.yaml
    sha256: bdaf3728a500b6956b691f5f9da8e0140f529d60b992870a5bcba2111bd4aaf1
    role: context
  - path: data/habitats/host_associated/digestive_system__46d403bb.yaml
    sha256: e8b58e033a3731b328a56df296015aee853c301a13a80079bae9fa1f2d4baeb8
    role: context
  - path: data/habitats/host_associated/digestive_system__4f205b4d.yaml
    sha256: 4be309cbf443304471b37ef96cb6b6243eacf6b9247c70efa710a52dfe03336c
    role: context
  - path: data/habitats/host_associated/digestive_system__c5da4fa6.yaml
    sha256: 6363cb0e898fd5bebe327d8b7ebd0e46a39b672f5ec4f184865efb5c84fbb4fc
    role: context
  - path: data/habitats/host_associated/digestive_system__efdbeca1.yaml
    sha256: 68f12a08d60a0a350f532b270582ae5e3b8c4419b6c95b1da4a9efdeb085d7a6
    role: context
  - path: data/habitats/host_associated/environmental_system_determined_by_an_organism.yaml
    sha256: d3b79ef9436a87fbce8e6b204b0113e170fa758e4a66efb592543bf934c67270
    role: context
  - path: data/habitats/host_associated/finger.yaml
    sha256: b8e1cdb77d2c9e9241e6345107f5a8adcaac14044c43bdeeb77031fa2b32a66a
    role: target
  - path: data/habitats/host_associated/fish.yaml
    sha256: 511e15b9761796b18df95ffb1befb025a6e4e8f6c68a8b85fb5ffa2710cd0308
    role: target
  - path: data/habitats/host_associated/flagellate.yaml
    sha256: a5e603770f5f62f2c6fbe21cbc2d8e1fdda39413fd1ea89890aa30e337ae5c85
    role: target
  - path: data/habitats/host_associated/flagellum.yaml
    sha256: 422b4809a97c9be0e12071ef03fde30df19bcac0c194fe51e1a7c7c1267fa079
    role: target
  - path: data/habitats/host_associated/flat_warts.yaml
    sha256: 13a97a0d2adc69ecdb313de39e957504e0badf89a9f6547a22b269cad69d53f3
    role: target
  - path: data/habitats/host_associated/flower.yaml
    sha256: 289d9282ee2a422ce7ff1cdf687243199e3a66ff8e2484ec2138f3410faba447
    role: target
  - path: data/habitats/host_associated/foot.yaml
    sha256: 6351c0e6cfbc652a577e079985b1e49924d4c74889aae9abfa2fd50245458d24
    role: target
  - path: data/habitats/host_associated/foraminifera.yaml
    sha256: 3b72eb77f5dbba2cd4f9c5ea7ae4c0d183a241b1aa3dfc68d6d2743c84cc523f
    role: target
  - path: data/habitats/host_associated/forearm.yaml
    sha256: c35832eab7f2a07a9137b7781a0ccbcf02aa1309cc57e1206fab550f355e37ad
    role: target
  - path: data/habitats/host_associated/foregut.yaml
    sha256: 758e75bd694555864a93bdc1030484e414142d5eebf628ed6ed1c8e5f319ddb0
    role: target
  - path: data/habitats/host_associated/foregut__6bc8c43a.yaml
    sha256: 50b8e2128df8652c85b446272543277a000568d44b3008a15c84e61cba928175
    role: target
  - path: data/habitats/host_associated/foregut__c14450a8.yaml
    sha256: 888c404f0cb848560b2bbb35c53436110f630a173cf27e91bcd6045b17a1bc44
    role: target
  - path: data/habitats/host_associated/foregut__ce63e8ab.yaml
    sha256: c2e259b437506873d31f861f1ab6b3172a320578aab5a3dfeebc16f9c710860c
    role: target
  - path: data/habitats/host_associated/foregut__d14a54ae.yaml
    sha256: d77c22a55c0e3f5c7b3251633ed1f611dfb4d438672562862936e83c380eabeb
    role: target
  - path: data/habitats/host_associated/foregut__ee6a8f74.yaml
    sha256: 2619ce5143958abbf90e574dd50e36654baf7a0e1425caa5fa3b483cb7a11daa
    role: target
  - path: data/habitats/host_associated/foreleg.yaml
    sha256: f1e0b2a6ac736a093fcfd5f854ea35fd3b2480f77e5192db26bf357decd22625
    role: target
  - path: data/habitats/host_associated/forestomach.yaml
    sha256: aac81e3abdc93a37f2318c1c307b58459786daf253d8d7ea5352e01717d6f3ee
    role: target
  - path: data/habitats/host_associated/fossilized_remains.yaml
    sha256: 61ff1ccb14021822e2770b914ff319afa8957ba6a4c708812564bcc8c9157455
    role: target
  - path: data/habitats/host_associated/fossilized_remains__19772eb4.yaml
    sha256: 08cd1d3d38ca358878017c13f22b61833c7fab2a6f397f98f603f1b31c6ffcf7
    role: target
  - path: data/habitats/host_associated/fossilized_remains__8b01c49f.yaml
    sha256: 0ac8f692b30749fb574eadee696e55b541e78ac41d946a593ee4dacf128b5d7b
    role: target
  - path: data/habitats/host_associated/fossilized_remains__eec3c6e8.yaml
    sha256: 00fbe0798c954aea8f29e0a9d20d933a249ebb54ecef519fbb8ed89c840014f6
    role: target
  - path: data/habitats/host_associated/frass.yaml
    sha256: 8dc3d1d5d77df7ae003cf25983c624e9f79fc31639f6f3bb8de1295692b1e6e2
    role: target
  - path: data/habitats/host_associated/frass__c029dd2b.yaml
    sha256: 87b17530c8e1f7b1dadeaea71cebd21ce0bd6f72ed1ccce6bb19fbd2116e66f9
    role: target
  - path: data/habitats/host_associated/free_living_state.yaml
    sha256: bf05feb76f4b54210559ef260fa396868d13d4270756f8c4e7af31234afe53f4
    role: target
  - path: data/habitats/host_associated/gut__bf7dab67.yaml
    sha256: 34252ab6fd06f683fc8990780b9d3f618764cd6d28f5c1a4f0b5641136ef678b
    role: context
  - path: data/habitats/host_associated/hind_legs.yaml
    sha256: 92f64b32540428e126f0d371ed83553b36e4f1429458c855dfde6753ccc7d088
    role: context
  - path: data/habitats/host_associated/hindgut__f414b618.yaml
    sha256: d9e6476df58f7b510f568e8c374b1f6173570da79653f246e76f023b0cb5fd0e
    role: context
  - path: data/habitats/host_associated/lymph_node__7af26c8b.yaml
    sha256: 2ad5c08889ffa33811bb6d9e2cf48891e13376d441f51fdacac76aa2456288b7
    role: context
  - path: data/habitats/host_associated/rhizaria.yaml
    sha256: 2d7f2f70423e11a7ef655fac6222c3751c70f39e02c8d513c992105a239ef199
    role: context
  - path: data/habitats/host_associated/stomach.yaml
    sha256: 00c90419bef787f7615e08b66f473bce09a23aed328e45127dfac2cdff968cc2
    role: context
  - path: data/habitats/host_associated/stomach__0260a3a9.yaml
    sha256: 112f083fc13038eb46b4cefe6b7a668ec9ef29b6023d17d77b07a8eb97911bf4
    role: context
  - path: data/habitats/host_associated/wart.yaml
    sha256: 8dfbd965bef25cc428f75623bf410a7697050bbdb8609f8ec5e636eb45b1e559
    role: context
  - path: data/habitats/other/animal_associated_environment.yaml
    sha256: a1cf41f43f9bece44dfb3e5d6ab0ca86858df67b88ee25d6ada260cccac69e16
    role: context
  - path: data/raw/bacdive_isolation_sources.tsv
    sha256: fb1645dd899a43130be9cf38b0e8b27ffbaa0175306917bff20e20ee225875fc
    role: context
  - path: data/raw/gold_ecosystem_paths.tsv
    sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
    role: context
  - path: data/raw/isolation_source_groundings.tsv
    sha256: ab6a997359aab961c40928f9b13e06adb6dc43124fa3de821819570dd87f43b8
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
- target_id: BTO:0004669
  path: data/habitats/host_associated/finger.yaml
  label: finger
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
- target_id: habitatmech:GOLD.3d529a667e
  path: data/habitats/host_associated/fish.yaml
  label: fish-associated environment
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
- target_id: BTO:0000464
  path: data/habitats/host_associated/flagellate.yaml
  label: flagellate
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
- target_id: BTO:0002292
  path: data/habitats/host_associated/flagellum.yaml
  label: flagellum
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
- target_id: habitatmech:GOLD.79193f14f9
  path: data/habitats/host_associated/flat_warts.yaml
  label: human flat wart
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
- target_id: BTO:0000469
  path: data/habitats/host_associated/flower.yaml
  label: flower
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
- target_id: BTO:0000476
  path: data/habitats/host_associated/foot.yaml
  label: foot
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
- target_id: habitatmech:GOLD.0a9f2ca319
  path: data/habitats/host_associated/foraminifera.yaml
  label: foraminiferan-associated environment
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
- target_id: BTO:0001447
  path: data/habitats/host_associated/forearm.yaml
  label: forearm
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
- target_id: BTO:0000507
  path: data/habitats/host_associated/foregut.yaml
  label: foregut
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
- target_id: habitatmech:GOLD.52f22e84ee
  path: data/habitats/host_associated/foregut__6bc8c43a.yaml
  label: Foregut
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
- target_id: habitatmech:GOLD.cd6e81f421
  path: data/habitats/host_associated/foregut__c14450a8.yaml
  label: Foregut
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
- target_id: habitatmech:GOLD.bd1664969c
  path: data/habitats/host_associated/foregut__ce63e8ab.yaml
  label: Foregut
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
- target_id: habitatmech:GOLD.8997340b18
  path: data/habitats/host_associated/foregut__d14a54ae.yaml
  label: Foregut
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
- target_id: habitatmech:GOLD.fe78a4c113
  path: data/habitats/host_associated/foregut__ee6a8f74.yaml
  label: Foregut
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
- target_id: BTO:0006514
  path: data/habitats/host_associated/foreleg.yaml
  label: foreleg
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
- target_id: BTO:0000480
  path: data/habitats/host_associated/forestomach.yaml
  label: forestomach
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
- target_id: habitatmech:GOLD.4af8939c1f
  path: data/habitats/host_associated/fossilized_remains.yaml
  label: fossilized avian remains
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
- target_id: habitatmech:GOLD.76df031f74
  path: data/habitats/host_associated/fossilized_remains__19772eb4.yaml
  label: fossilized fish remains
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
- target_id: habitatmech:GOLD.f1a2eca320
  path: data/habitats/host_associated/fossilized_remains__8b01c49f.yaml
  label: fossilized hominin remains
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
- target_id: habitatmech:GOLD.c5640eadf7
  path: data/habitats/host_associated/fossilized_remains__eec3c6e8.yaml
  label: fossilized mammalian remains
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
- target_id: habitatmech:GOLD.319c3f351e
  path: data/habitats/host_associated/frass.yaml
  label: Frass
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
- target_id: habitatmech:GOLD.67f3cde908
  path: data/habitats/host_associated/frass__c029dd2b.yaml
  label: Frass
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
- target_id: BTO:0001551
  path: data/habitats/host_associated/free_living_state.yaml
  label: free-living state
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
    records in data/habitats/host_associated/ (indices 530-553 in path order).
  selection: Next 24 unreviewed records in data/habitats/host_associated/ immediately
    following 20261108T114933Z-fin-record.
  coverage: full
  population_size: 24
  reviewed_target_ids:
  - BTO:0004669
  - habitatmech:GOLD.3d529a667e
  - BTO:0000464
  - BTO:0002292
  - habitatmech:GOLD.79193f14f9
  - BTO:0000469
  - BTO:0000476
  - habitatmech:GOLD.0a9f2ca319
  - BTO:0001447
  - BTO:0000507
  - habitatmech:GOLD.52f22e84ee
  - habitatmech:GOLD.cd6e81f421
  - habitatmech:GOLD.bd1664969c
  - habitatmech:GOLD.8997340b18
  - habitatmech:GOLD.fe78a4c113
  - BTO:0006514
  - BTO:0000480
  - habitatmech:GOLD.4af8939c1f
  - habitatmech:GOLD.76df031f74
  - habitatmech:GOLD.f1a2eca320
  - habitatmech:GOLD.c5640eadf7
  - habitatmech:GOLD.319c3f351e
  - habitatmech:GOLD.67f3cde908
  - BTO:0001551
  exclusions:
  - target: Other habitat records outside indices 530-553 of data/habitats/host_associated/
    reason: Bounded 24-record cohort slice for Cycle 8 Stage 4 record/category review;
      direct parents and relevant siblings are inspected as context.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: .venv/bin/python -m linkml.validator.cli -s src/habitatmech/schema/habitatmech.yaml
    --target-class HabitatRecord data/habitats/host_associated/finger.yaml data/habitats/host_associated/fish.yaml
    data/habitats/host_associated/flagellate.yaml data/habitats/host_associated/flagellum.yaml
    data/habitats/host_associated/flat_warts.yaml data/habitats/host_associated/flower.yaml
    data/habitats/host_associated/foot.yaml data/habitats/host_associated/foraminifera.yaml
    data/habitats/host_associated/forearm.yaml data/habitats/host_associated/foregut.yaml
    data/habitats/host_associated/foregut__6bc8c43a.yaml data/habitats/host_associated/foregut__c14450a8.yaml
    data/habitats/host_associated/foregut__ce63e8ab.yaml data/habitats/host_associated/foregut__d14a54ae.yaml
    data/habitats/host_associated/foregut__ee6a8f74.yaml data/habitats/host_associated/foreleg.yaml
    data/habitats/host_associated/forestomach.yaml data/habitats/host_associated/fossilized_remains.yaml
    data/habitats/host_associated/fossilized_remains__19772eb4.yaml data/habitats/host_associated/fossilized_remains__8b01c49f.yaml
    data/habitats/host_associated/fossilized_remains__eec3c6e8.yaml data/habitats/host_associated/frass.yaml
    data/habitats/host_associated/frass__c029dd2b.yaml data/habitats/host_associated/free_living_state.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0004669
  - habitatmech:GOLD.3d529a667e
  - BTO:0000464
  - BTO:0002292
  - habitatmech:GOLD.79193f14f9
  - BTO:0000469
  - BTO:0000476
  - habitatmech:GOLD.0a9f2ca319
  - BTO:0001447
  - BTO:0000507
  - habitatmech:GOLD.52f22e84ee
  - habitatmech:GOLD.cd6e81f421
  - habitatmech:GOLD.bd1664969c
  - habitatmech:GOLD.8997340b18
  - habitatmech:GOLD.fe78a4c113
  - BTO:0006514
  - BTO:0000480
  - habitatmech:GOLD.4af8939c1f
  - habitatmech:GOLD.76df031f74
  - habitatmech:GOLD.f1a2eca320
  - habitatmech:GOLD.c5640eadf7
  - habitatmech:GOLD.319c3f351e
  - habitatmech:GOLD.67f3cde908
  - BTO:0001551
  summary: Completed 2026-11-09T18:08:48Z. No issues found.
  scope_note: Individual schema; strict command covers the 24 named cohort targets;
    other documented gates have full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/habitats/host_associated/finger.yaml
    data/habitats/host_associated/fish.yaml data/habitats/host_associated/flagellate.yaml
    data/habitats/host_associated/flagellum.yaml data/habitats/host_associated/flat_warts.yaml
    data/habitats/host_associated/flower.yaml data/habitats/host_associated/foot.yaml
    data/habitats/host_associated/foraminifera.yaml data/habitats/host_associated/forearm.yaml
    data/habitats/host_associated/foregut.yaml data/habitats/host_associated/foregut__6bc8c43a.yaml
    data/habitats/host_associated/foregut__c14450a8.yaml data/habitats/host_associated/foregut__ce63e8ab.yaml
    data/habitats/host_associated/foregut__d14a54ae.yaml data/habitats/host_associated/foregut__ee6a8f74.yaml
    data/habitats/host_associated/foreleg.yaml data/habitats/host_associated/forestomach.yaml
    data/habitats/host_associated/fossilized_remains.yaml data/habitats/host_associated/fossilized_remains__19772eb4.yaml
    data/habitats/host_associated/fossilized_remains__8b01c49f.yaml data/habitats/host_associated/fossilized_remains__eec3c6e8.yaml
    data/habitats/host_associated/frass.yaml data/habitats/host_associated/frass__c029dd2b.yaml
    data/habitats/host_associated/free_living_state.yaml --out .temp/c8s4_24_strict.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0004669
  - habitatmech:GOLD.3d529a667e
  - BTO:0000464
  - BTO:0002292
  - habitatmech:GOLD.79193f14f9
  - BTO:0000469
  - BTO:0000476
  - habitatmech:GOLD.0a9f2ca319
  - BTO:0001447
  - BTO:0000507
  - habitatmech:GOLD.52f22e84ee
  - habitatmech:GOLD.cd6e81f421
  - habitatmech:GOLD.bd1664969c
  - habitatmech:GOLD.8997340b18
  - habitatmech:GOLD.fe78a4c113
  - BTO:0006514
  - BTO:0000480
  - habitatmech:GOLD.4af8939c1f
  - habitatmech:GOLD.76df031f74
  - habitatmech:GOLD.f1a2eca320
  - habitatmech:GOLD.c5640eadf7
  - habitatmech:GOLD.319c3f351e
  - habitatmech:GOLD.67f3cde908
  - BTO:0001551
  summary: 'Completed 2026-11-09T18:08:54Z. Validated 24 files; files with ERROR:
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
  - BTO:0004669
  - habitatmech:GOLD.3d529a667e
  - BTO:0000464
  - BTO:0002292
  - habitatmech:GOLD.79193f14f9
  - BTO:0000469
  - BTO:0000476
  - habitatmech:GOLD.0a9f2ca319
  - BTO:0001447
  - BTO:0000507
  - habitatmech:GOLD.52f22e84ee
  - habitatmech:GOLD.cd6e81f421
  - habitatmech:GOLD.bd1664969c
  - habitatmech:GOLD.8997340b18
  - habitatmech:GOLD.fe78a4c113
  - BTO:0006514
  - BTO:0000480
  - habitatmech:GOLD.4af8939c1f
  - habitatmech:GOLD.76df031f74
  - habitatmech:GOLD.f1a2eca320
  - habitatmech:GOLD.c5640eadf7
  - habitatmech:GOLD.319c3f351e
  - habitatmech:GOLD.67f3cde908
  - BTO:0001551
  summary: Completed 2026-11-09T18:09:00Z. No issues found; 876 history record(s)
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
  - BTO:0004669
  - habitatmech:GOLD.3d529a667e
  - BTO:0000464
  - BTO:0002292
  - habitatmech:GOLD.79193f14f9
  - BTO:0000469
  - BTO:0000476
  - habitatmech:GOLD.0a9f2ca319
  - BTO:0001447
  - BTO:0000507
  - habitatmech:GOLD.52f22e84ee
  - habitatmech:GOLD.cd6e81f421
  - habitatmech:GOLD.bd1664969c
  - habitatmech:GOLD.8997340b18
  - habitatmech:GOLD.fe78a4c113
  - BTO:0006514
  - BTO:0000480
  - habitatmech:GOLD.4af8939c1f
  - habitatmech:GOLD.76df031f74
  - habitatmech:GOLD.f1a2eca320
  - habitatmech:GOLD.c5640eadf7
  - habitatmech:GOLD.319c3f351e
  - habitatmech:GOLD.67f3cde908
  - BTO:0001551
  summary: 'Completed 2026-11-09T18:09:01Z. provenance current: 14 committed inventories,
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
  - BTO:0004669
  - habitatmech:GOLD.3d529a667e
  - BTO:0000464
  - BTO:0002292
  - habitatmech:GOLD.79193f14f9
  - BTO:0000469
  - BTO:0000476
  - habitatmech:GOLD.0a9f2ca319
  - BTO:0001447
  - BTO:0000507
  - habitatmech:GOLD.52f22e84ee
  - habitatmech:GOLD.cd6e81f421
  - habitatmech:GOLD.bd1664969c
  - habitatmech:GOLD.8997340b18
  - habitatmech:GOLD.fe78a4c113
  - BTO:0006514
  - BTO:0000480
  - habitatmech:GOLD.4af8939c1f
  - habitatmech:GOLD.76df031f74
  - habitatmech:GOLD.f1a2eca320
  - habitatmech:GOLD.c5640eadf7
  - habitatmech:GOLD.319c3f351e
  - habitatmech:GOLD.67f3cde908
  - BTO:0001551
  summary: 'Completed 2026-11-09T18:09:16Z. expected 3209 records, found 3209 on disk;
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
  - BTO:0004669
  - habitatmech:GOLD.3d529a667e
  - BTO:0000464
  - BTO:0002292
  - habitatmech:GOLD.79193f14f9
  - BTO:0000469
  - BTO:0000476
  - habitatmech:GOLD.0a9f2ca319
  - BTO:0001447
  - BTO:0000507
  - habitatmech:GOLD.52f22e84ee
  - habitatmech:GOLD.cd6e81f421
  - habitatmech:GOLD.bd1664969c
  - habitatmech:GOLD.8997340b18
  - habitatmech:GOLD.fe78a4c113
  - BTO:0006514
  - BTO:0000480
  - habitatmech:GOLD.4af8939c1f
  - habitatmech:GOLD.76df031f74
  - habitatmech:GOLD.f1a2eca320
  - habitatmech:GOLD.c5640eadf7
  - habitatmech:GOLD.319c3f351e
  - habitatmech:GOLD.67f3cde908
  - BTO:0001551
  summary: Completed 2026-11-09T18:09:22Z. validated 103 causal-graph curation file(s)
    with 103 graph(s).
  scope_note: Full-corpus causal-graph overlay validation.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: .venv/bin/python scripts/build_term_requests.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0004669
  - habitatmech:GOLD.3d529a667e
  - BTO:0000464
  - BTO:0002292
  - habitatmech:GOLD.79193f14f9
  - BTO:0000469
  - BTO:0000476
  - habitatmech:GOLD.0a9f2ca319
  - BTO:0001447
  - BTO:0000507
  - habitatmech:GOLD.52f22e84ee
  - habitatmech:GOLD.cd6e81f421
  - habitatmech:GOLD.bd1664969c
  - habitatmech:GOLD.8997340b18
  - habitatmech:GOLD.fe78a4c113
  - BTO:0006514
  - BTO:0000480
  - habitatmech:GOLD.4af8939c1f
  - habitatmech:GOLD.76df031f74
  - habitatmech:GOLD.f1a2eca320
  - habitatmech:GOLD.c5640eadf7
  - habitatmech:GOLD.319c3f351e
  - habitatmech:GOLD.67f3cde908
  - BTO:0001551
  summary: Completed 2026-11-09T18:09:36Z. term-request table is current (674 terms).
  scope_note: Full-corpus term-request table currency check.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0004669
  - habitatmech:GOLD.3d529a667e
  - BTO:0000464
  - BTO:0002292
  - habitatmech:GOLD.79193f14f9
  - BTO:0000469
  - BTO:0000476
  - habitatmech:GOLD.0a9f2ca319
  - BTO:0001447
  - BTO:0000507
  - habitatmech:GOLD.52f22e84ee
  - habitatmech:GOLD.cd6e81f421
  - habitatmech:GOLD.bd1664969c
  - habitatmech:GOLD.8997340b18
  - habitatmech:GOLD.fe78a4c113
  - BTO:0006514
  - BTO:0000480
  - habitatmech:GOLD.4af8939c1f
  - habitatmech:GOLD.76df031f74
  - habitatmech:GOLD.f1a2eca320
  - habitatmech:GOLD.c5640eadf7
  - habitatmech:GOLD.319c3f351e
  - habitatmech:GOLD.67f3cde908
  - BTO:0001551
  summary: 'Completed 2026-11-09T18:10:17Z. OK_CANONICAL: 1213, OK_SYNONYM: 1, OK_EXCEPTION:
    5, SKIPPED_NO_ADAPTER: 2094. All id<->label pairs correspond.'
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
evidence:
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-09T18:11:00Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon, organism-form,
    and subcellular organelle terms cannot substitute for associated environments;
    parent_habitats must be strictly broader across all contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-09T18:11:00Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-09T18:11:00Z'
  support: supports
  summary: Seed generator resolution routes and parent/synonym assembly verified across
    all 24 cohort target records.
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EREC1
  kind: record_content
  reference: data/habitats/host_associated/finger.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T18:11:00Z'
  support: supports
  summary: The PREGO-attested record BTO:0004669 (finger, EXACT/SEEDED, 9 TAXON assertions)
    is coherently grounded to BRENDA Tissue Ontology term BTO:0004669 with its vendored
    anatomical definition, 4 PREGO RELATED_SYNONYMs ('digits', 'fingers', 'forelimb
    digit', 'forelimb digits'), and 9 displayed characteristic taxa.
  snapshot_sha256: b8e1cdb77d2c9e9241e6345107f5a8adcaac14044c43bdeeb77031fa2b32a66a
- evidence_id: EREC2
  kind: record_content
  reference: data/habitats/host_associated/fish.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T18:11:00Z'
  support: supports
  summary: The curated GOLD host-environment record habitatmech:GOLD.3d529a667e (fish-associated
    environment, UNGROUNDED/REVIEWED, 1,350 ORGANISM assertions) has a sound definition
    and parent_habitats (ENVO:01001000, ENVO:01001002), but curation/term_requests.tsv
    row 9 retains the bare host clade name 'Fish' in exact_synonym, emitting 'Fish'
    as an EXACT_SYNONYM on the environment record.
  snapshot_sha256: 511e15b9761796b18df95ffb1befb025a6e4e8f6c68a8b85fb5ffa2710cd0308
- evidence_id: EREC3
  kind: record_content
  reference: data/habitats/host_associated/flagellate.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T18:11:00Z'
  support: supports
  summary: The PREGO-attested record BTO:0000464 (flagellate, 'A flagellate protozoan
    or alga.', EXACT/SEEDED, 9 TAXON assertions) uses a morphological whole-organism
    form class as a microbial habitat identity and imports organism-form classes BTO:0000720
    (plant form) and BTO:0002503 (protozoan form) in parent_habitats.
  snapshot_sha256: a5e603770f5f62f2c6fbe21cbc2d8e1fdda39413fd1ea89890aa30e337ae5c85
- evidence_id: EREC4
  kind: record_content
  reference: data/habitats/host_associated/flagellum.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T18:11:00Z'
  support: supports
  summary: The PREGO-attested record BTO:0002292 (flagellum, biolink:CellularComponent
    in data/raw/prego_habitats.tsv row 497, 140 TAXON assertions across flagellated
    bacteria such as Escherichia coli, Salmonella enterica, and Bacillus) uses a subcellular
    motility organelle identity as a host-associated microbial habitat and imports
    whole-organism form BTO:0000464 (flagellate) in parent_habitats.
  snapshot_sha256: 422b4809a97c9be0e12071ef03fde30df19bcac0c194fe51e1a7c7c1267fa079
- evidence_id: EREC5
  kind: record_content
  reference: data/habitats/host_associated/flat_warts.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T18:11:00Z'
  support: supports
  summary: 'The curated GOLD record habitatmech:GOLD.79193f14f9 (human flat wart,
    ''Host-associated > Mammals: Human > Benign tumor > Wart > Flat warts'', UNGROUNDED/REVIEWED)
    is coherently defined as a human cutaneous wart habitat under BTO:0001859 (wart)
    with parent_mode REPLACE and source-label exclusion for bare ''Flat warts''.'
  snapshot_sha256: 13a97a0d2adc69ecdb313de39e957504e0badf89a9f6547a22b269cad69d53f3
- evidence_id: EREC6
  kind: record_content
  reference: data/habitats/host_associated/flower.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T18:11:00Z'
  support: supports
  summary: The PREGO-attested record BTO:0000469 (flower, EXACT/SEEDED, 6 TAXON assertions)
    is coherently grounded to BRENDA Tissue Ontology term BTO:0000469 ('The reproductive
    structure of angiosperms.') with 1 PREGO RELATED_SYNONYM ('flowers') and 6 displayed
    characteristic taxa.
  snapshot_sha256: 289d9282ee2a422ce7ff1cdf687243199e3a66ff8e2484ec2138f3410faba447
- evidence_id: EREC7
  kind: record_content
  reference: data/habitats/host_associated/foot.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T18:11:00Z'
  support: supports
  summary: The BacDive-attested record BTO:0000476 (foot, 'bacdive.isolation_source:foot',
    EXACT/REVIEWED, 114 STRAIN assertions) is coherently grounded to BRENDA Tissue
    Ontology term BTO:0000476 ('The terminal part of the vertebrate leg upon which
    an individual stands.') under BTO:0001492 (lower limb) with 10 displayed characteristic
    taxa from the 107-row BacDive pool.
  snapshot_sha256: 6351c0e6cfbc652a577e079985b1e49924d4c74889aae9abfa2fd50245458d24
- evidence_id: EREC8
  kind: record_content
  reference: data/habitats/host_associated/foraminifera.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T18:11:00Z'
  support: supports
  summary: The curated GOLD host-environment record habitatmech:GOLD.0a9f2ca319 (foraminiferan-associated
    environment, 'Host-associated > Protists > Rhizaria > Foraminifera', UNGROUNDED/REVIEWED,
    6 ORGANISM assertions) is coherently defined under ENVO:01001000 (environmental
    system determined by an organism) and habitatmech:GOLD.6b259c237e (rhizarian-associated
    environment) with exact_synonym 'foraminiferal host environment' and source-label
    exclusion for bare 'Foraminifera'.
  snapshot_sha256: 3b72eb77f5dbba2cd4f9c5ea7ae4c0d183a241b1aa3dfc68d6d2743c84cc523f
- evidence_id: EREC9
  kind: record_content
  reference: data/habitats/host_associated/forearm.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T18:11:00Z'
  support: supports
  summary: The PREGO-attested record BTO:0001447 (forearm, EXACT/SEEDED, 404 TAXON
    assertions) is coherently grounded to BRENDA Tissue Ontology term BTO:0001447
    ('The part of the superior limb between the elbow and the wrist.') with 2 PREGO
    RELATED_SYNONYMs ('forearmic', 'forearms') and 10 displayed characteristic taxa
    from the 404-row PREGO pool.
  snapshot_sha256: c35832eab7f2a07a9137b7781a0ccbcf02aa1309cc57e1206fab550f355e37ad
- evidence_id: EREC10
  kind: record_content
  reference: data/habitats/host_associated/foregut.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T18:11:00Z'
  support: supports
  summary: The PREGO-attested record BTO:0000507 (foregut, EXACT/SEEDED, 92 TAXON
    assertions) is coherently grounded to BRENDA Tissue Ontology term BTO:0000507
    with its vendored anatomical definition, 1 PREGO RELATED_SYNONYM ('foreguts'),
    and 10 displayed characteristic taxa from the 92-row PREGO pool.
  snapshot_sha256: 758e75bd694555864a93bdc1030484e414142d5eebf628ed6ed1c8e5f319ddb0
- evidence_id: EREC11
  kind: record_content
  reference: data/habitats/host_associated/foregut__6bc8c43a.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T18:11:00Z'
  support: supports
  summary: The fish foregut record habitatmech:GOLD.52f22e84ee ('Host-associated >
    Fish > Digestive system > Foregut', NARROW/SEEDED) asserts the whole fish Digestive
    system (habitatmech:GOLD.8a68d0f6f5, 'Host-associated > Fish > Digestive system')
    in parent_habitats alongside UBERON:0001041 (foregut), conflating part_of digestive-system
    composition with is_a habitat subtyping, and emits mapping_predicate skos:narrowMatch
    on a minted source-path record (#1398).
  snapshot_sha256: 50b8e2128df8652c85b446272543277a000568d44b3008a15c84e61cba928175
- evidence_id: EREC12
  kind: record_content
  reference: data/habitats/host_associated/foregut__c14450a8.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T18:11:00Z'
  support: supports
  summary: The mammalian foregut record habitatmech:GOLD.cd6e81f421 ('Host-associated
    > Mammals > Digestive system > Foregut', NARROW/SEEDED) asserts the whole mammalian
    Digestive system (habitatmech:GOLD.c8e85f3c84, 'Host-associated > Mammals > Digestive
    system') in parent_habitats alongside UBERON:0001041 (foregut), conflating part_of
    digestive-system composition with is_a habitat subtyping, and emits mapping_predicate
    skos:narrowMatch on a minted source-path record (#1398).
  snapshot_sha256: 888c404f0cb848560b2bbb35c53436110f630a173cf27e91bcd6045b17a1bc44
- evidence_id: EREC13
  kind: record_content
  reference: data/habitats/host_associated/foregut__ce63e8ab.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T18:11:00Z'
  support: supports
  summary: 'The insect foregut record habitatmech:GOLD.bd1664969c (''Host-associated
    > Arthropoda: Insects > Digestive system > Foregut'', NARROW/SEEDED) asserts the
    whole insect Digestive system (habitatmech:GOLD.d7cff86ce8, ''Host-associated
    > Arthropoda: Insects > Digestive system'') in parent_habitats alongside UBERON:0001041
    (foregut), conflating part_of digestive-system composition with is_a habitat subtyping,
    and emits mapping_predicate skos:narrowMatch on a minted source-path record (#1398).'
  snapshot_sha256: c2e259b437506873d31f861f1ab6b3172a320578aab5a3dfeebc16f9c710860c
- evidence_id: EREC14
  kind: record_content
  reference: data/habitats/host_associated/foregut__d14a54ae.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T18:11:00Z'
  support: supports
  summary: 'The myriapod foregut record habitatmech:GOLD.8997340b18 (''Host-associated
    > Arthropoda: Myriapoda > Digestive system > Foregut'', NARROW/SEEDED) asserts
    the whole myriapod Digestive system (habitatmech:GOLD.acc41d1792, ''Host-associated
    > Arthropoda: Myriapoda > Digestive system'') in parent_habitats alongside UBERON:0001041
    (foregut), conflating part_of digestive-system composition with is_a habitat subtyping,
    and emits mapping_predicate skos:narrowMatch on a minted source-path record (#1398).'
  snapshot_sha256: d77c22a55c0e3f5c7b3251633ed1f611dfb4d438672562862936e83c380eabeb
- evidence_id: EREC15
  kind: record_content
  reference: data/habitats/host_associated/foregut__ee6a8f74.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T18:11:00Z'
  support: supports
  summary: 'The crustacean foregut record habitatmech:GOLD.fe78a4c113 (''Host-associated
    > Arthropoda: Crustaceans > Digestive system > Foregut'', NARROW/SEEDED) asserts
    the whole crustacean Digestive system (habitatmech:GOLD.6eecdf150d, ''Host-associated
    > Arthropoda: Crustaceans > Digestive system'') in parent_habitats alongside UBERON:0001041
    (foregut), conflating part_of digestive-system composition with is_a habitat subtyping,
    and emits mapping_predicate skos:narrowMatch on a minted source-path record (#1398).'
  snapshot_sha256: 2619ce5143958abbf90e574dd50e36654baf7a0e1425caa5fa3b483cb7a11daa
- evidence_id: EREC16
  kind: record_content
  reference: data/habitats/host_associated/foreleg.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T18:11:00Z'
  support: supports
  summary: The GOLD-attested record BTO:0006514 (foreleg, 'A front leg.', EXACT/REVIEWED)
    grounds GOLD path 'Host-associated > Mammals > Lymphatic system > Lymph nodes
    > Forelegs' (habitatmech:GOLD.80220dc4d4) to the whole front limb BTO:0006514
    rather than a mammalian forelimb lymph node (parallel to hind_legs.yaml habitatmech:GOLD.ca4882ca81),
    causing BTO:0006514 to assert both BTO:0000721 (limb) and UBERON:0000029 (lymph
    node) in parent_habitats.
  snapshot_sha256: f1e0b2a6ac736a093fcfd5f854ea35fd3b2480f77e5192db26bf357decd22625
- evidence_id: EREC17
  kind: record_content
  reference: data/habitats/host_associated/forestomach.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T18:11:00Z'
  support: supports
  summary: The multi-source record BTO:0000480 (forestomach, attested by GOLD 'Host-associated
    > Mammals > Digestive system > Stomach > Forestomach' and PREGO BTO:0000480, EXACT/REVIEWED,
    1 TAXON assertion) asserts the whole mammalian Stomach (habitatmech:GOLD.d3869ad37f,
    'Host-associated > Mammals > Digestive system > Stomach') in parent_habitats alongside
    BTO:0001307 (stomach), conflating anatomical compartment part_of composition with
    is_a subtyping.
  snapshot_sha256: aac81e3abdc93a37f2318c1c307b58459786daf253d8d7ea5352e01717d6f3ee
- evidence_id: EREC18
  kind: record_content
  reference: data/habitats/host_associated/fossilized_remains.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T18:11:00Z'
  support: supports
  summary: The curated GOLD fossil-remains record habitatmech:GOLD.4af8939c1f (fossilized
    avian remains, 'Host-associated > Birds > Remains > Fossilized remains', UNGROUNDED/REVIEWED)
    is coherently defined under ENVO:00002164 (fossil material) with parent_mode REPLACE
    and source-label exclusion for bare 'Fossilized remains'.
  snapshot_sha256: 61ff1ccb14021822e2770b914ff319afa8957ba6a4c708812564bcc8c9157455
- evidence_id: EREC19
  kind: record_content
  reference: data/habitats/host_associated/fossilized_remains__19772eb4.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T18:11:00Z'
  support: supports
  summary: The curated GOLD fossil-remains record habitatmech:GOLD.76df031f74 (fossilized
    fish remains, 'Host-associated > Fish > Remains > Fossilized remains', UNGROUNDED/REVIEWED)
    is coherently defined under ENVO:00002164 (fossil material) with parent_mode REPLACE
    and source-label exclusion for bare 'Fossilized remains'.
  snapshot_sha256: 08cd1d3d38ca358878017c13f22b61833c7fab2a6f397f98f603f1b31c6ffcf7
- evidence_id: EREC20
  kind: record_content
  reference: data/habitats/host_associated/fossilized_remains__8b01c49f.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T18:11:00Z'
  support: supports
  summary: 'The curated GOLD fossil-remains record habitatmech:GOLD.f1a2eca320 (fossilized
    hominin remains, ''Host-associated > Mammals: Human > Remains > Fossilized remains'',
    UNGROUNDED/REVIEWED) is coherently defined under ENVO:00002164 (fossil material)
    with parent_mode REPLACE and source-label exclusion for bare ''Fossilized remains''.'
  snapshot_sha256: 0ac8f692b30749fb574eadee696e55b541e78ac41d946a593ee4dacf128b5d7b
- evidence_id: EREC21
  kind: record_content
  reference: data/habitats/host_associated/fossilized_remains__eec3c6e8.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T18:11:00Z'
  support: supports
  summary: The curated GOLD fossil-remains record habitatmech:GOLD.c5640eadf7 (fossilized
    mammalian remains, 'Host-associated > Mammals > Remains > Fossilized remains',
    UNGROUNDED/REVIEWED) is coherently defined under ENVO:00002164 (fossil material)
    with parent_mode REPLACE and source-label exclusion for bare 'Fossilized remains'.
  snapshot_sha256: 00fbe0798c954aea8f29e0a9d20d933a249ebb54ecef519fbb8ed89c840014f6
- evidence_id: EREC22
  kind: record_content
  reference: data/habitats/host_associated/frass.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T18:11:00Z'
  support: supports
  summary: 'The insect frass record habitatmech:GOLD.319c3f351e (''Host-associated
    > Arthropoda: Insects > Larva > Gut > Frass'', NARROW/SEEDED) asserts the anatomical
    organ habitatmech:GOLD.d4e02cf775 (''Host-associated > Arthropoda: Insects > Larva
    > Gut'') in parent_habitats alongside ENVO:00002003 (fecal material), conflating
    anatomical origin with is_a habitat subtyping, and emits mapping_predicate skos:narrowMatch
    on a minted source-path record (#1398).'
  snapshot_sha256: 8dc3d1d5d77df7ae003cf25983c624e9f79fc31639f6f3bb8de1295692b1e6e2
- evidence_id: EREC23
  kind: record_content
  reference: data/habitats/host_associated/frass__c029dd2b.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T18:11:00Z'
  support: supports
  summary: 'The insect frass record habitatmech:GOLD.67f3cde908 (''Host-associated
    > Arthropoda: Insects > Digestive system > Hindgut > Frass'', NARROW/SEEDED) asserts
    the anatomical organ habitatmech:GOLD.50722c7871 (''Host-associated > Arthropoda:
    Insects > Digestive system > Hindgut'') in parent_habitats alongside ENVO:00002003
    (fecal material), conflating anatomical origin with is_a habitat subtyping, and
    emits mapping_predicate skos:narrowMatch on a minted source-path record (#1398).'
  snapshot_sha256: 87b17530c8e1f7b1dadeaea71cebd21ce0bd6f72ed1ccce6bb19fbd2116e66f9
- evidence_id: EREC24
  kind: record_content
  reference: data/habitats/host_associated/free_living_state.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T18:11:00Z'
  support: supports
  summary: 'The PREGO-attested record BTO:0001551 (free-living state, definition:
    null, child of BTO:0000284 organism form, 3 TAXON assertions for Bradyrhizobium
    sp. DOA9, Escherichia coli str. K-12 substr. W3110, and Azorhizobium caulinodans
    ORS 571) uses a microbial physiological/lifestyle organism-form state as a host-associated
    habitat identity and asserts BTO:0000284 (organism form) in parent_habitats.'
  snapshot_sha256: bf05feb76f4b54210559ef260fa396868d13d4270756f8c4e7af31234afe53f4
assessments:
- assessment_id: A1
  area: schema
  topic: Native validity and reproduction
  outcome: supported
  summary: All 24 cohort records pass LinkML schema validation, strict closed-schema
    validation, history validation (876 records), provenance verification, exact 3,209-record
    corpus reproduction, causal-graph validation (103 graphs), term-request check
    (674 terms), and OAK id-label correspondence.
  target_ids:
  - BTO:0004669
  - habitatmech:GOLD.3d529a667e
  - BTO:0000464
  - BTO:0002292
  - habitatmech:GOLD.79193f14f9
  - BTO:0000469
  - BTO:0000476
  - habitatmech:GOLD.0a9f2ca319
  - BTO:0001447
  - BTO:0000507
  - habitatmech:GOLD.52f22e84ee
  - habitatmech:GOLD.cd6e81f421
  - habitatmech:GOLD.bd1664969c
  - habitatmech:GOLD.8997340b18
  - habitatmech:GOLD.fe78a4c113
  - BTO:0006514
  - BTO:0000480
  - habitatmech:GOLD.4af8939c1f
  - habitatmech:GOLD.76df031f74
  - habitatmech:GOLD.f1a2eca320
  - habitatmech:GOLD.c5640eadf7
  - habitatmech:GOLD.319c3f351e
  - habitatmech:GOLD.67f3cde908
  - BTO:0001551
  evidence_ids:
  - ERULE
  - ESCHEMA
  - ESEED
- assessment_id: A2
  area: scope
  topic: Cohort boundary and lumping/splitting evaluation
  outcome: supported
  summary: All 24 records represent distinct anatomical-site, host-environment, organism-form/organelle,
    host-scoped foregut, forelimb lymph-node, forestomach, fossilized-remains, or
    insect-frass source concepts; no cross-record lumping or splitting is warranted
    across the cohort.
  target_ids:
  - BTO:0004669
  - habitatmech:GOLD.3d529a667e
  - BTO:0000464
  - BTO:0002292
  - habitatmech:GOLD.79193f14f9
  - BTO:0000469
  - BTO:0000476
  - habitatmech:GOLD.0a9f2ca319
  - BTO:0001447
  - BTO:0000507
  - habitatmech:GOLD.52f22e84ee
  - habitatmech:GOLD.cd6e81f421
  - habitatmech:GOLD.bd1664969c
  - habitatmech:GOLD.8997340b18
  - habitatmech:GOLD.fe78a4c113
  - BTO:0006514
  - BTO:0000480
  - habitatmech:GOLD.4af8939c1f
  - habitatmech:GOLD.76df031f74
  - habitatmech:GOLD.f1a2eca320
  - habitatmech:GOLD.c5640eadf7
  - habitatmech:GOLD.319c3f351e
  - habitatmech:GOLD.67f3cde908
  - BTO:0001551
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
  summary: '11 records pass with limitations; 13 records have 23 open findings (4
    blocker identity findings, 11 major grounding findings, 1 major nomenclature finding,
    and 7 major #1398 mapping-endpoint contract findings) recorded in their respective
    kind: record bundles (linked in related_reviews) and carried forward to Stage
    5 grouped remediation.'
  target_ids:
  - BTO:0004669
  - habitatmech:GOLD.3d529a667e
  - BTO:0000464
  - BTO:0002292
  - habitatmech:GOLD.79193f14f9
  - BTO:0000469
  - BTO:0000476
  - habitatmech:GOLD.0a9f2ca319
  - BTO:0001447
  - BTO:0000507
  - habitatmech:GOLD.52f22e84ee
  - habitatmech:GOLD.cd6e81f421
  - habitatmech:GOLD.bd1664969c
  - habitatmech:GOLD.8997340b18
  - habitatmech:GOLD.fe78a4c113
  - BTO:0006514
  - BTO:0000480
  - habitatmech:GOLD.4af8939c1f
  - habitatmech:GOLD.76df031f74
  - habitatmech:GOLD.f1a2eca320
  - habitatmech:GOLD.c5640eadf7
  - habitatmech:GOLD.319c3f351e
  - habitatmech:GOLD.67f3cde908
  - BTO:0001551
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
  - BTO:0004669
  - habitatmech:GOLD.3d529a667e
  - BTO:0000464
  - BTO:0002292
  - habitatmech:GOLD.79193f14f9
  - BTO:0000469
  - BTO:0000476
  - habitatmech:GOLD.0a9f2ca319
  - BTO:0001447
  rationale: Retain finger (BTO:0004669), fish-associated environment (habitatmech:GOLD.3d529a667e),
    PREGO flagellate (BTO:0000464), PREGO flagellum (BTO:0002292), human flat wart
    (habitatmech:GOLD.79193f14f9), flower (BTO:0000469), foot (BTO:0000476), foraminiferan-associated
    environment (habitatmech:GOLD.0a9f2ca319), and forearm (BTO:0001447) as distinct
    source-attested bins (with item-level identity/synonym remediations tracked on
    fish, flagellate, and flagellum).
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
  - ERULE
- action: retain
  target_ids:
  - BTO:0000507
  - habitatmech:GOLD.52f22e84ee
  - habitatmech:GOLD.cd6e81f421
  - habitatmech:GOLD.bd1664969c
  - habitatmech:GOLD.8997340b18
  - habitatmech:GOLD.fe78a4c113
  - BTO:0006514
  - BTO:0000480
  rationale: Retain cross-host PREGO foregut (BTO:0000507), the 5 host-scoped GOLD
    Foregut bins (fish, mammalian, insect, myriapod, and crustacean), mammalian forelimb
    lymph node (currently grounded to BTO:0006514 foreleg), and mammalian forestomach
    (BTO:0000480) as distinct anatomical and host-scoped digestive/lymphatic bins.
  evidence_ids:
  - EREC10
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
  - habitatmech:GOLD.4af8939c1f
  - habitatmech:GOLD.76df031f74
  - habitatmech:GOLD.f1a2eca320
  - habitatmech:GOLD.c5640eadf7
  - habitatmech:GOLD.319c3f351e
  - habitatmech:GOLD.67f3cde908
  - BTO:0001551
  rationale: Retain the 4 host-clade fossilized-remains records (avian, fish, hominin,
    and mammalian), the 2 insect Frass records (larval gut and insect hindgut origin),
    and PREGO free-living state (BTO:0001551) as distinct source-attested records.
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
  review_id: 20261109T181010Z-finger-record
  relationship: Component individual record review in this 24-record Cycle-8 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261109T181011Z-fish-record
  relationship: Component individual record review in this 24-record Cycle-8 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261109T181012Z-flagellate-record
  relationship: Component individual record review in this 24-record Cycle-8 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261109T181013Z-flagellum-record
  relationship: Component individual record review in this 24-record Cycle-8 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261109T181014Z-flat_warts-record
  relationship: Component individual record review in this 24-record Cycle-8 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261109T181015Z-flower-record
  relationship: Component individual record review in this 24-record Cycle-8 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261109T181016Z-foot-record
  relationship: Component individual record review in this 24-record Cycle-8 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261109T181017Z-foraminifera-record
  relationship: Component individual record review in this 24-record Cycle-8 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261109T181018Z-forearm-record
  relationship: Component individual record review in this 24-record Cycle-8 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261109T181019Z-foregut-record
  relationship: Component individual record review in this 24-record Cycle-8 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261109T181020Z-foregut__6bc8c43a-record
  relationship: Component individual record review in this 24-record Cycle-8 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261109T181021Z-foregut__c14450a8-record
  relationship: Component individual record review in this 24-record Cycle-8 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261109T181022Z-foregut__ce63e8ab-record
  relationship: Component individual record review in this 24-record Cycle-8 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261109T181023Z-foregut__d14a54ae-record
  relationship: Component individual record review in this 24-record Cycle-8 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261109T181024Z-foregut__ee6a8f74-record
  relationship: Component individual record review in this 24-record Cycle-8 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261109T181025Z-foreleg-record
  relationship: Component individual record review in this 24-record Cycle-8 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261109T181026Z-forestomach-record
  relationship: Component individual record review in this 24-record Cycle-8 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261109T181027Z-fossilized_remains-record
  relationship: Component individual record review in this 24-record Cycle-8 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261109T181028Z-fossilized_remains__19772eb4-record
  relationship: Component individual record review in this 24-record Cycle-8 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261109T181029Z-fossilized_remains__8b01c49f-record
  relationship: Component individual record review in this 24-record Cycle-8 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261109T181030Z-fossilized_remains__eec3c6e8-record
  relationship: Component individual record review in this 24-record Cycle-8 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261109T181031Z-frass-record
  relationship: Component individual record review in this 24-record Cycle-8 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261109T181032Z-frass__c029dd2b-record
  relationship: Component individual record review in this 24-record Cycle-8 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261109T181033Z-free_living_state-record
  relationship: Component individual record review in this 24-record Cycle-8 Stage-4
    cohort.
limitations:
- Only the stated primary evidence and current ontology/taxonomy authorities were
  independently inspected; original specimen-level support for every source-bin member
  is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism,
  or characteristic presence.
- Configured label correspondence skipped 2,094 no-adapter pairs; this is not whole-corpus
  identifier certification.
- 'Record-specific open findings (23 across 13 records: 4 blocker identity defects,
  11 major grounding/hierarchy defects, 1 major nomenclature exact_synonyms defect,
  and 7 major #1398 mapping-endpoint contract defects) are recorded on their respective
  kind: record bundles in related_reviews so each issue_key has a single authoritative
  open owner for Stage 5 remediation.'
notes:
- All 24 cohort target files and context inputs were captured at clean git commit
  19d3ccb65e6b5128b9b0a5ae39cb509bf3f2bf39.
- 'Each of the 24 targets has a dedicated kind: record bundle in reviews/structured/.'
tags:
- category-cohort-review
- host-associated
```
