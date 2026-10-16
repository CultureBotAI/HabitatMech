# Record review: Cell Line (habitatmech:GOLD.975b14f252)

- Review: 20261015T235745Z-cell_line__d7fc8c60-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T23:40:00Z
- Finished UTC: 2026-10-15T23:57:45Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The human Cell line source is conservatively minted UNGROUNDED/SEEDED and has a human-associated-environment parent, not a whole-human identity. Primary HeLa culture evidence supports host-cell biological meaning without claiming these exact GOLD samples. Fourteen supplemental biosamples and two study memberships are separate measures from the zero frozen tree count; they must not be summed.

## Scope And Provenance

Full field-by-field scientific assessment of this exact generated target at 0eb609a7ddb34925067116af806e26c165e10678.

Selection: Stale cecum individual observation plus the next 23 identifiers lacking completed individual-kind reviews in the ignored-inclusive 3209-record census. This bundle assesses one resolved record; previous batch reviews remain valid history.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 0eb609a7ddb34925067116af806e26c165e10678.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.975b14f252 | data/habitats/host_associated/cell_line__d7fc8c60.yaml | generated | Cell Line |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.975b14f252 | Finished 2026-10-15T23:44:54Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/cell_line__d7fc8c60.yaml |
| validate-strict | passed | True | habitatmech:GOLD.975b14f252 | Finished 2026-10-15T23:45:51Z. uv run python scripts/validate_strict.py data/habitats/host_associated/cecum.yaml data/habitats/host_associated/cardiac_stomach.yaml data/habitats/host_associated/cecum__d677e5d7.yaml data/habitats/host_associated/cecum_intestinal_cecum.yaml data/habitats/host_associated/cecum_mucosa.yaml data/habitats/host_associated/cell_culture.yaml data/habitats/host_associated/cell_line.yaml data/habitats/host_associated/cell_line__59b8224e.yaml data/habitats/host_associated/cell_line__d7fc8c60.yaml data/habitats/host_associated/cellulitis.yaml data/habitats/host_associated/central_nervous_system.yaml data/habitats/host_associated/cephalochordata.yaml data/habitats/host_associated/cephalothorax.yaml data/habitats/host_associated/cerebellum.yaml data/habitats/host_associated/cerebrospinal_fluid.yaml data/habitats/host_associated/cerebrospinal_fluid__93998265.yaml data/habitats/host_associated/cerebrospinal_fluid__b2fc1889.yaml data/habitats/host_associated/cerebrospinal_fluid__e3d236b3.yaml data/habitats/host_associated/cerebrospinal_fluid__f9e9497c.yaml data/habitats/host_associated/ceros.yaml data/habitats/host_associated/cerumen.yaml data/habitats/host_associated/cerumen_gland.yaml data/habitats/host_associated/cervical.yaml data/habitats/host_associated/cervical_adenocarcinoma_cell.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | habitatmech:GOLD.975b14f252 | Finished 2026-10-15T23:46:04Z. No issues found<br>829 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | habitatmech:GOLD.975b14f252 | Finished 2026-10-15T23:46:05Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | habitatmech:GOLD.975b14f252 | Finished 2026-10-15T23:46:28Z. expected 3209 records, found 3209 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | habitatmech:GOLD.975b14f252 | Finished 2026-10-15T23:46:34Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | habitatmech:GOLD.975b14f252 | Finished 2026-10-15T23:46:59Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | habitatmech:GOLD.975b14f252 | Finished 2026-10-15T23:48:03Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1173<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2063<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-baseline native QC | passed | True | habitatmech:GOLD.975b14f252 | Verified 2026-10-15T23:55:08Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38822113212 |
| Standalone evidence-reference validator applicability | not_applicable | False | habitatmech:GOLD.975b14f252 | No standalone citation/reference validator is documented for these evidence-free generated records. Target EvidenceItems and causal edges are absent. Stable source and ontology/taxon references were checked manually and with documented native gates; current-decision primary citations were separately verified where present. |

## Scientific And Domain Assessments

### Identity, definition, category, aliases and hierarchy

identity: supported. Targets: habitatmech:GOLD.975b14f252.

The human Cell line source is conservatively minted UNGROUNDED/SEEDED and has a human-associated-environment parent, not a whole-human identity. Primary HeLa culture evidence supports host-cell biological meaning without claiming these exact GOLD samples. Fourteen supplemental biosamples and two study memberships are separate measures from the zero frozen tree count; they must not be summed.

### Source assertions, pools, ranks and supplementary context

quantity: supported. Targets: habitatmech:GOLD.975b14f252.

All emitted counts/units, labels, ranks, scores and candidate pools match exact frozen rows. [{"source": "GOLD", "count": 0, "unit": "ORGANISM"}]. Zero tree counts are omitted; later biosamples and study memberships are not added. Current taxonomy resolves displayed identifiers including explicit aliases.

### Biological support and bounded source uncertainty

evidence: supported. Targets: habitatmech:GOLD.975b14f252.

The human Cell line source is conservatively minted UNGROUNDED/SEEDED and has a human-associated-environment parent, not a whole-human identity. Primary HeLa culture evidence supports host-cell biological meaning without claiming these exact GOLD samples. Fourteen supplemental biosamples and two study memberships are separate measures from the zero frozen tree count; they must not be summed.

### Native status, optional parameters and causal mechanisms

completeness: supported. Targets: habitatmech:GOLD.975b14f252.

Executed native resolution reproduces UNGROUNDED/SEEDED. No environmental parameters, causal graphs, discussions, datasets or is_characteristic=true claims are present. Missing optional fields and SEEDED status alone are not defects; parent mechanisms are not inherited.

### Native validation and reproduction

schema: supported. Targets: habitatmech:GOLD.975b14f252.

Target schema/strict checks, 829 histories, source provenance, exact 3209-record reproduction, 32 causal overlays, 110 term requests and configured label checks passed. Exact-base remote full QC passed. Deterministic validity is separate from scientific support; reference-check applicability is stated explicitly.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/cell_line__d7fc8c60.yaml; Entire target YAML | supports | All fields, attestations, taxa and generated history read. |
| ERULE | docs/CURATION.md; Identity, strict broader hierarchy and evidence rules | supports | Organism, disease, material and habitat identities remain distinct. Parents must be strictly broader, not merely containing sites. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; HabitatRecord, SourceAttestation and TaxonAssociation | supports | Mapping predicate endpoint is source-to-record; source association is weaker than characteristic presence. Optional fields and native review status have distinct contracts. |
| ESEED | src/habitatmech/seed.py; Executed native source routes and complete document reproduction | supports | [{"mint": "habitatmech:GOLD.975b14f252", "automatic": {"identifier": "habitatmech:GOLD.975b14f252", "grounding_status": "UNGROUNDED", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "gold_unmatched", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "habitatmech:GOLD.975b14f252", "grounding_status": "UNGROUNDED", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "curated_confirm_ungrounded_from_gold_unmatched", "category": null, "reviewed": false, "decision": {"identifier": "habitatmech:GOLD.975b14f252", "decision": "CONFIRM_UNGROUNDED", "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-12", "notes": "Class-level sweep (see docs/HARMONIZATION.md#class-level-sweep): no term in the vendored slice matched this label by any search route. Whether the concept is a habitat at all was NOT assessed, so this is not yet a term-request candidate.", "review_depth": "CLASS", "category": "", "relation": "parent"}}}] |
| EEXTRACT | src/habitatmech/extract.py; Source counts, channels and taxon ranking | supports | Exact frozen rows reproduce counts/units and ranked taxon scores. The committed projection does not retain original PREGO pair citation links. |
| ET5 | data/raw/gold_ecosystem_paths.tsv; Physical TSV rows 2187 | supports | [{"row": 2187, "data": {"canonical_path": "Host-associated &gt; Mammals: Human &gt; Cell Line", "ecosystem": "Host-associated", "ecosystem_category": "Mammals: Human", "ecosystem_type": "Cell Line", "ecosystem_subtype": "", "specific_ecosystem": "", "leaf_label": "Cell Line", "depth": "3", "gold_node_count": "3", "organism_count": "0", "study_count": "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids": "gold.ecosystem:4830&#124;gold.ecosystem:5459&#124;gold.ecosystem:5460"}}] |
| ET6 | data/raw/gold_path_biosamples.tsv; Physical TSV rows 573 | supports | [{"row": 573, "data": {"canonical_path": "Host-associated &gt; Mammals: Human &gt; Cell Line", "ecosystem_path_id": "5460", "biosample_count": "14"}}] |
| ET7 | data/raw/gold_studies.tsv; Physical TSV rows 1926,3806 | supports | [{"row": 1926, "data": {"study_gold_id": "Gs0133340", "path_count": "12", "paths": "Engineered &gt; Industrial production &gt; Chemical products &gt; Reagent blank&#124;Host-associated &gt; Mammals: Human &gt; Abdominal/Peritoneal cavity &gt; Ascites &gt; Malignant ascites&#124;Host-associated &gt; Mammals: Human &gt; Cell Line&#124;Host-associated &gt; Mammals: Human &gt; Circulatory system &gt; Blood&#124;Host-associated &gt; Mammals: Human &gt; Malignant tumor &gt; Carcinoma &gt; Basal cell carcinoma&#124;Host-associated &gt; Mammals: Human &gt; Malignant tumor &gt; Carcinoma &gt; Breast cancer&#124;Host-associated &gt; Mammals: Human &gt; Malignant tumor &gt; Carcinoma &gt; Colon cancer&#124;Host-associated &gt; Mammals: Human &gt; Malignant tumor &gt; Carcinoma &gt; Squamous cell carcinoma&#124;Host-associated &gt; Mammals: Human &gt; Malignant tumor &gt; Carcinoma &gt; Testicular cancer&#124;Host-associated &gt; Mammals: Human &gt; Malignant tumor &gt; Carcinoma &gt; Urothelial carcinoma/Transitional cell carcinoma (TCC)&#124;Host-associated &gt; Mammals: Human &gt; Malignant tumor &gt; Lymphoma &gt; Mycosis fungoides/Cutaneous T-cell lymphoma&#124;Host-associated &gt; Mammals: Human &gt; Malignant tumor &gt; Melanoma"}}, {"row": 3806, "data": {"study_gold_id": "Gs0153894", "path_count": "1", "paths": "Host-associated &gt; Mammals: Human &gt; Cell Line"}}] |
| ET8 | curation/decisions.tsv; Physical TSV rows 893 | supports | [{"row": 893, "data": {"identifier": "habitatmech:GOLD.975b14f252", "decision": "CONFIRM_UNGROUNDED", "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-12", "notes": "Class-level sweep (see docs/HARMONIZATION.md#class-level-sweep): no term in the vendored slice matched this label by any search route. Whether the concept is a habitat at all was NOT assessed, so this is not yet a term-request candidate.", "review_depth": "CLASS", "category": "", "relation": ""}}] |
| EP9 | data/habitats/host_associated/mammals_human.yaml; Full immediate-parent record; context only | supports | {"identifier": "habitatmech:GOLD.cd0b0940e5", "label": "human-associated environment", "definition": "An environmental system determined by a human.", "definition_source": "HabitatMech", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED", "synonyms": [{"synonym_text": "Human", "synonym_type": "EXACT_SYNONYM", "source": "BacDive"}, {"synonym_text": "Mammals: Human", "synonym_type": "EXACT_SYNONYM", "source": "HabitatMech curation"}, {"synonym_text": "human host", "synonym_type": "EXACT_SYNONYM", "source": "HabitatMech curation"}], "parent_habitats": ["ENVO:01001000", "ENVO:01001002"], "source_attestations": [{"source": "BACDIVE", "source_id": "bacdive.isolation_source:human", "source_label": "Human", "assertion_count": 11697, "assertion_unit": "STRAIN", "notes": "kg-microbe's isolation-source mapping table has no ontology target for this source; the automatic route leaves it ungrounded. The explicit curator decision SAME_AS overrides that route; this source is emitted on habitatmech:GOLD.cd0b0940e5."}, {"source": "GOLD", "source_id": "gold.ecosystem:3381", "source_label": "Mammals: Human", "source_path": "Host-associated &gt; Mammals: Human", "assertion_count": 40432, "assertion_unit": "ORGANISM", "notes": "4 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "characteristic_taxa": [{"taxon_id": "NCBITaxon:562", "source": "BACDIVE", "taxon_label": "Escherichia coli", "association_count": 222, "rank": 1, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:1313", "source": "BACDIVE", "taxon_label": "Streptococcus pneumoniae", "association_count": 197, "rank": 2, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:197", "source": "BACDIVE", "taxon_label": "Campylobacter jejuni", "association_count": 175, "rank": 3, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:1280", "source": "BACDIVE", "taxon_label": "Staphylococcus aureus", "association_count": 156, "rank": 4, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:1328", "source": "BACDIVE", "taxon_label": "Streptococcus anginosus", "association_count": 155, "rank": 5, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:730", "source": "BACDIVE", "taxon_label": "[Haemophilus] ducreyi", "association_count": 125, "rank": 6, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:287", "source": "BACDIVE", "taxon_label": "Pseudomonas aeruginosa", "association_count": 113, "rank": 7, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:727", "source": "BACDIVE", "taxon_label": "Haemophilus influenzae", "association_count": 110, "rank": 8, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:28188", "source": "BACDIVE", "taxon_label": "Capnocytophaga canimorsus", "association_count": 108, "rank": 9, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:1656", "source": "BACDIVE", "taxon_label": "Actinomyces viscosus", "association_count": 105, "rank": 10, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:47715", "source": "BACDIVE", "taxon_label": "Lacticaseibacillus rhamnosus", "association_count": 105, "rank": 11, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:1352", "source": "BACDIVE", "taxon_label": "Enterococcus faecium", "association_count": 100, "rank": 12, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:2702", "source": "BACDIVE", "taxon_label": "Gardnerella vaginalis", "association_count": 95, "rank": 13, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:28901", "source": "BACDIVE", "taxon_label": "Salmonella enterica", "association_count": 88, "rank": 14, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:2", "source": "BACDIVE", "taxon_label": "Bacteria", "association_count": 87, "rank": 15, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:1660", "source": "BACDIVE", "taxon_label": "Schaalia odontolytica", "association_count": 76, "rank": 16, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:59505", "source": "BACDIVE", "taxon_label": "Actinotignum schaalii", "association_count": 76, "rank": 17, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:46124", "source": "BACDIVE", "taxon_label": "Granulicatella adiacens", "association_count": 75, "rank": 18, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:520", "source": "BACDIVE", "taxon_label": "Bordetella pertussis", "association_count": 71, "rank": 19, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:1720", "source": "BACDIVE", "taxon_label": "Corynebacterium sp.", "association_count": 69, "rank": 20, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:40324", "source": "BACDIVE", "taxon_label": "Stenotrophomonas maltophilia", "association_count": 69, "rank": 21, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:732", "source": "BACDIVE", "taxon_label": "Aggregatibacter aphrophilus", "association_count": 68, "rank": 22, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:1655", "source": "BACDIVE", "taxon_label": "Actinomyces naeslundii", "association_count": 66, "rank": 23, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:1305", "source": "BACDIVE", "taxon_label": "Streptococcus sanguinis", "association_count": 65, "rank": 24, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:1596", "source": "BACDIVE", "taxon_label": "Lactobacillus gasseri", "association_count": 64, "rank": 25, "candidate_pool": 2068}], "curation_history": [{"timestamp": "2026-08-12T00:00:00Z", "curator": "claude-opus-5", "action": "CONFIRM_UNGROUNDED", "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term ENVO:01001002 'animal-associated environment' attached as a parent. Humans as host, the single largest ungrounded concept at 40432 GOLD organisms. No human-associated environment term exists in ENVO. Deliberately not grounded to animal-associated environment: every host clade would then merge onto one record and the host distinction is the entire content. Highest-value ENVO term request. (source concept habitatmech:GOLD.cd0b0940e5)"}, {"timestamp": "2026-08-16T00:00:00Z", "curator": "claude-opus-5", "action": "DEFINED", "changes": "Defined as 'human-associated environment' under ENVO:01001002 'animal-associated environment'. The habitat is the host clade, and it is the entire content of the concept: GOLD and BacDive both organise host-associated isolates by host, and every downstream anatomical path hangs off it. HabitatMech deliberately does not ground these to animal-associated environment, because every clade would then merge onto one record and the distinction the sources are making would be lost. ENVO already has this shape at plant-, animal- and fungi-associated environment; this asks for the same pattern one level down. This is the single largest ungrounded concept in the corpus."}, {"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by BACDIVE, GOLD. Grounding: UNGROUNDED."}, {"timestamp": "2026-08-17T00:00:00Z", "curator": "claude-opus-5", "action": "SAME_AS", "changes": "Merged into habitatmech:GOLD.cd0b0940e5 'Mammals: Human': the same concept under another source's name. Novel-concept merge (#116): BacDive's 'Human' and GOLD's 'Mammals: Human' are the same habitat \u2014 a human acting as host \u2014 and both are novel, so neither has an ontology term to merge on. Before SAME_AS they were two permanent records holding 40,432 and 11,697 assertions for one concept, published as two pages, and the largest habitat in the corpus appeared nowhere as such. Merged onto the GOLD identifier because it carries the larger attestation and the deeper path; the choice of which id survives is arbitrary between two minted ids and is recorded here rather than left to ordering. Both keep their attestations on the merged record, so no evidence is lost. (source concept habitatmech:BACDIVE.c9b246fcbb)"}, {"timestamp": "2026-10-10T00:00:00Z", "curator": "seed_from_sources", "action": "SOURCE_ATTESTATION_CORRECTED", "changes": "Corrected bacdive.isolation_source:human provenance wording to distinguish the declined automatic mapping from the final curator override (#1889)."}]} |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000/graph; ENVO_01001000-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001000", "target": "http://purl.obolibrary.org/obo/ENVO_01000254", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001000", "target": "http://purl.obolibrary.org/obo/NCBITaxon_131567", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000; ENVO_01001000.json | context_only | Current term identity, active status and definition: {"obo_id": "ENVO:01001000", "label": "environmental system determined by an organism", "is_obsolete": false, "description": ["An environmental system which is determined by a living organism."]} |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002/graph; ENVO_01001002-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001002", "target": "http://purl.obolibrary.org/obo/ENVO_01001000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001002", "target": "http://purl.obolibrary.org/obo/NCBITaxon_33208", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002; ENVO_01001002.json | context_only | Current term identity, active status and definition: {"obo_id": "ENVO:01001002", "label": "animal-associated environment", "is_obsolete": false, "description": ["An environmental system determined by an animal."]} |
| EX5 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6343517/fullTextXML; PMC6343517.xml | context_only | PMID:30700982, DOI:10.3389/fmicb.2018.03269. Cell-culture methods and infection results explicitly use HeLa 229, ATCC CCL-2.1, with Nigg and Weiss laboratory stocks. Supports in vitro cervical adenocarcinoma-cell association only; stock lineage is narrower than all historical isolates. |
| ESEARCH | Local maintained inputs and review archive; rg --no-ignore --hidden -l -F -e habitatmech:GOLD.975b14f252 -e 'Cell Line' -e cell_line__d7fc8c60 -e habitatmech:GOLD.975b14f252 curation history research reports data/raw build reviews | context_only | Identifier/label/slug search and full structured-YAML traversal; exact TSV rows were parsed separately. Broad search matches are leads, not all independently reviewed. |

## Limits And Additional Notes

- Source counts, ranks and scores do not establish prevalence, viability or characteristic presence. Original specimen-level evidence for every source member has not been reconstructed.
- Configured label validation skipped 2063 no-adapter pairs; displayed TaxIds were separately resolved against current NCBI including aliases.
- Exact-base full QC was verified remotely, not newly executed locally. New saved bundles require a separate archive check.
- iModulonDB is not applicable: target assertions contain no gene, regulator or expression-module claim. No paid research or native status promotion was performed.
- Captured input hashes match both working bytes and exact committed base blobs.
- This observation proposes curation but does not itself mutate inputs. The separately authorized PR workflow may address supported findings in later commits.
- Ignored-inclusive archive traversal found no earlier structured target observation. Historical prose does not count as a formal predecessor.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T235745Z-cell_line__d7fc8c60-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: Cell Line (habitatmech:GOLD.975b14f252)'
started_at: '2026-10-15T23:40:00Z'
finished_at: '2026-10-15T23:57:45Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent inspected record and sources; not independent human
    or second-agent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The human Cell line source is conservatively minted UNGROUNDED/SEEDED and
  has a human-associated-environment parent, not a whole-human identity. Primary HeLa
  culture evidence supports host-cell biological meaning without claiming these exact
  GOLD samples. Fourteen supplemental biosamples and two study memberships are separate
  measures from the zero frozen tree count; they must not be summed.
source:
  git_revision: 0eb609a7ddb34925067116af806e26c165e10678
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
    sha256: e5cb2e09f72dd4b18e069c0e2576e25e13e56c9991f4eb5ae47416345e247578
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 37dc4b40642d19e7b5c3262f368d12daa82e03115e7731a2326ae88785ceff5b
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 7158cb696b7e2ac84a8d594a03015711424ff56e21c07a4648ffc6fb2e84a107
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: a56f07a45fb743fb7b0e61f83ef70fa5ed61a3c892cfaf36e3428967c548dc5e
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: bc7a13d922c179cd9bcd4d37b348bc90a39b08a4dafba7af4ed0039ad99621c3
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: ee559f7b45b4af2d72a078c45d1a3b676785d34305f286e9738f95771dbaccfd
    role: context
  - path: data/habitats/RETIRED.tsv
    sha256: 747e6a5612dc0b7ed881b9fb323fd57ab3c75794d9ee5ebb9d59b2be57dbf8cd
    role: context
  - path: data/habitats/host_associated/cell_line__d7fc8c60.yaml
    sha256: be327d491ca97a9a7635c2353b3e032e77b182d57dad971641a3b31904974982
    role: target
  - path: data/habitats/host_associated/mammals_human.yaml
    sha256: 6d3fba8ddf0a933b0e22f94b17e2df356eb2d297b1d96a7f960575e81d50d4d1
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
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
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
targets:
- target_id: habitatmech:GOLD.975b14f252
  path: data/habitats/host_associated/cell_line__d7fc8c60.yaml
  label: Cell Line
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
  description: Full field-by-field scientific assessment of this exact generated target
    at 0eb609a7ddb34925067116af806e26c165e10678.
  selection: Stale cecum individual observation plus the next 23 identifiers lacking
    completed individual-kind reviews in the ignored-inclusive 3209-record census.
    This bundle assesses one resolved record; previous batch reviews remain valid
    history.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.975b14f252
  exclusions:
  - target: Other records, original source specimens and SSSOM/KGX products
    reason: Parent and source context do not add reviewed targets; exports and every
      original source specimen are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/cell_line__d7fc8c60.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.975b14f252
  summary: "Finished 2026-10-15T23:44:54Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/cell_line__d7fc8c60.yaml"
  scope_note: Individual schema; strict check covers all 24 named targets; other native
    checks have full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/cecum.yaml data/habitats/host_associated/cardiac_stomach.yaml
    data/habitats/host_associated/cecum__d677e5d7.yaml data/habitats/host_associated/cecum_intestinal_cecum.yaml
    data/habitats/host_associated/cecum_mucosa.yaml data/habitats/host_associated/cell_culture.yaml
    data/habitats/host_associated/cell_line.yaml data/habitats/host_associated/cell_line__59b8224e.yaml
    data/habitats/host_associated/cell_line__d7fc8c60.yaml data/habitats/host_associated/cellulitis.yaml
    data/habitats/host_associated/central_nervous_system.yaml data/habitats/host_associated/cephalochordata.yaml
    data/habitats/host_associated/cephalothorax.yaml data/habitats/host_associated/cerebellum.yaml
    data/habitats/host_associated/cerebrospinal_fluid.yaml data/habitats/host_associated/cerebrospinal_fluid__93998265.yaml
    data/habitats/host_associated/cerebrospinal_fluid__b2fc1889.yaml data/habitats/host_associated/cerebrospinal_fluid__e3d236b3.yaml
    data/habitats/host_associated/cerebrospinal_fluid__f9e9497c.yaml data/habitats/host_associated/ceros.yaml
    data/habitats/host_associated/cerumen.yaml data/habitats/host_associated/cerumen_gland.yaml
    data/habitats/host_associated/cervical.yaml data/habitats/host_associated/cervical_adenocarcinoma_cell.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.975b14f252
  summary: "Finished 2026-10-15T23:45:51Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/cecum.yaml data/habitats/host_associated/cardiac_stomach.yaml\
    \ data/habitats/host_associated/cecum__d677e5d7.yaml data/habitats/host_associated/cecum_intestinal_cecum.yaml\
    \ data/habitats/host_associated/cecum_mucosa.yaml data/habitats/host_associated/cell_culture.yaml\
    \ data/habitats/host_associated/cell_line.yaml data/habitats/host_associated/cell_line__59b8224e.yaml\
    \ data/habitats/host_associated/cell_line__d7fc8c60.yaml data/habitats/host_associated/cellulitis.yaml\
    \ data/habitats/host_associated/central_nervous_system.yaml data/habitats/host_associated/cephalochordata.yaml\
    \ data/habitats/host_associated/cephalothorax.yaml data/habitats/host_associated/cerebellum.yaml\
    \ data/habitats/host_associated/cerebrospinal_fluid.yaml data/habitats/host_associated/cerebrospinal_fluid__93998265.yaml\
    \ data/habitats/host_associated/cerebrospinal_fluid__b2fc1889.yaml data/habitats/host_associated/cerebrospinal_fluid__e3d236b3.yaml\
    \ data/habitats/host_associated/cerebrospinal_fluid__f9e9497c.yaml data/habitats/host_associated/ceros.yaml\
    \ data/habitats/host_associated/cerumen.yaml data/habitats/host_associated/cerumen_gland.yaml\
    \ data/habitats/host_associated/cervical.yaml data/habitats/host_associated/cervical_adenocarcinoma_cell.yaml\n\
    Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      24\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Individual schema; strict check covers all 24 named targets; other native
    checks have full-corpus scope.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.975b14f252
  summary: 'Finished 2026-10-15T23:46:04Z. No issues found

    829 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Individual schema; strict check covers all 24 named targets; other native
    checks have full-corpus scope.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.975b14f252
  summary: "Finished 2026-10-15T23:46:05Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Individual schema; strict check covers all 24 named targets; other native
    checks have full-corpus scope.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.975b14f252
  summary: "Finished 2026-10-15T23:46:28Z. expected 3209 records, found 3209 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Individual schema; strict check covers all 24 named targets; other native
    checks have full-corpus scope.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.975b14f252
  summary: "Finished 2026-10-15T23:46:34Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Individual schema; strict check covers all 24 named targets; other native
    checks have full-corpus scope.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.975b14f252
  summary: "Finished 2026-10-15T23:46:59Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Individual schema; strict check covers all 24 named targets; other native
    checks have full-corpus scope.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.975b14f252
  summary: "Finished 2026-10-15T23:48:03Z. id↔label correspondence summary:\n    \
    \      OK_CANONICAL: 1173\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2063\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Individual schema; strict check covers all 24 named targets; other native
    checks have full-corpus scope.
- check_id: CCI
  name: Exact-baseline native QC
  status: passed
  required: true
  command: gh run view 38822113212 --repo CultureBotAI/HabitatMech --json headSha,conclusion,url,jobs
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.975b14f252
  summary: Verified 2026-10-15T23:55:08Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38822113212
  scope_note: Unchanged committed scientific-input baseline; new output bundles are
    outside this run.
- check_id: CREF
  name: Standalone evidence-reference validator applicability
  status: not_applicable
  required: false
  target_ids:
  - habitatmech:GOLD.975b14f252
  summary: No standalone citation/reference validator is documented for these evidence-free
    generated records. Target EvidenceItems and causal edges are absent. Stable source
    and ontology/taxon references were checked manually and with documented native
    gates; current-decision primary citations were separately verified where present.
  scope_note: No command or exit code is invented for an unavailable/nonapplicable
    checker. Full-corpus causal validation ran separately.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/cell_line__d7fc8c60.yaml
  locator: Entire target YAML
  accessed_at: '2026-10-15T23:57:45Z'
  support: supports
  summary: All fields, attestations, taxa and generated history read.
  snapshot_sha256: be327d491ca97a9a7635c2353b3e032e77b182d57dad971641a3b31904974982
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, strict broader hierarchy and evidence rules
  accessed_at: '2026-10-15T23:57:45Z'
  support: supports
  summary: Organism, disease, material and habitat identities remain distinct. Parents
    must be strictly broader, not merely containing sites.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: HabitatRecord, SourceAttestation and TaxonAssociation
  accessed_at: '2026-10-15T23:57:45Z'
  support: supports
  summary: Mapping predicate endpoint is source-to-record; source association is weaker
    than characteristic presence. Optional fields and native review status have distinct
    contracts.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native source routes and complete document reproduction
  accessed_at: '2026-10-15T23:57:45Z'
  support: supports
  summary: '[{"mint": "habitatmech:GOLD.975b14f252", "automatic": {"identifier": "habitatmech:GOLD.975b14f252",
    "grounding_status": "UNGROUNDED", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "gold_unmatched", "category":
    null, "reviewed": false, "decision": null}, "final": {"identifier": "habitatmech:GOLD.975b14f252",
    "grounding_status": "UNGROUNDED", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "curated_confirm_ungrounded_from_gold_unmatched",
    "category": null, "reviewed": false, "decision": {"identifier": "habitatmech:GOLD.975b14f252",
    "decision": "CONFIRM_UNGROUNDED", "object_id": "", "object_label": "", "grounding_status":
    "", "curator": "claude-opus-5", "date": "2026-08-12", "notes": "Class-level sweep
    (see docs/HARMONIZATION.md#class-level-sweep): no term in the vendored slice matched
    this label by any search route. Whether the concept is a habitat at all was NOT
    assessed, so this is not yet a term-request candidate.", "review_depth": "CLASS",
    "category": "", "relation": "parent"}}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: Source counts, channels and taxon ranking
  accessed_at: '2026-10-15T23:57:45Z'
  support: supports
  summary: Exact frozen rows reproduce counts/units and ranked taxon scores. The committed
    projection does not retain original PREGO pair citation links.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Physical TSV rows 2187
  accessed_at: '2026-10-15T23:57:45Z'
  support: supports
  summary: '[{"row": 2187, "data": {"canonical_path": "Host-associated > Mammals:
    Human > Cell Line", "ecosystem": "Host-associated", "ecosystem_category": "Mammals:
    Human", "ecosystem_type": "Cell Line", "ecosystem_subtype": "", "specific_ecosystem":
    "", "leaf_label": "Cell Line", "depth": "3", "gold_node_count": "3", "organism_count":
    "0", "study_count": "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids":
    "gold.ecosystem:4830|gold.ecosystem:5459|gold.ecosystem:5460"}}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: ET6
  kind: database
  reference: data/raw/gold_path_biosamples.tsv
  locator: Physical TSV rows 573
  accessed_at: '2026-10-15T23:57:45Z'
  support: supports
  summary: '[{"row": 573, "data": {"canonical_path": "Host-associated > Mammals: Human
    > Cell Line", "ecosystem_path_id": "5460", "biosample_count": "14"}}]'
  snapshot_sha256: 97cd7c8d0e731d07a85db6986dbcf9e49096a3c7988bd90a855599f492fe619e
- evidence_id: ET7
  kind: database
  reference: data/raw/gold_studies.tsv
  locator: Physical TSV rows 1926,3806
  accessed_at: '2026-10-15T23:57:45Z'
  support: supports
  summary: '[{"row": 1926, "data": {"study_gold_id": "Gs0133340", "path_count": "12",
    "paths": "Engineered > Industrial production > Chemical products > Reagent blank|Host-associated
    > Mammals: Human > Abdominal/Peritoneal cavity > Ascites > Malignant ascites|Host-associated
    > Mammals: Human > Cell Line|Host-associated > Mammals: Human > Circulatory system
    > Blood|Host-associated > Mammals: Human > Malignant tumor > Carcinoma > Basal
    cell carcinoma|Host-associated > Mammals: Human > Malignant tumor > Carcinoma
    > Breast cancer|Host-associated > Mammals: Human > Malignant tumor > Carcinoma
    > Colon cancer|Host-associated > Mammals: Human > Malignant tumor > Carcinoma
    > Squamous cell carcinoma|Host-associated > Mammals: Human > Malignant tumor >
    Carcinoma > Testicular cancer|Host-associated > Mammals: Human > Malignant tumor
    > Carcinoma > Urothelial carcinoma/Transitional cell carcinoma (TCC)|Host-associated
    > Mammals: Human > Malignant tumor > Lymphoma > Mycosis fungoides/Cutaneous T-cell
    lymphoma|Host-associated > Mammals: Human > Malignant tumor > Melanoma"}}, {"row":
    3806, "data": {"study_gold_id": "Gs0153894", "path_count": "1", "paths": "Host-associated
    > Mammals: Human > Cell Line"}}]'
  snapshot_sha256: fa7aaa46f288d10c453bb723e6cf486cde646a003559414b5523cc3883a84c8c
- evidence_id: ET8
  kind: database
  reference: curation/decisions.tsv
  locator: Physical TSV rows 893
  accessed_at: '2026-10-15T23:57:45Z'
  support: supports
  summary: '[{"row": 893, "data": {"identifier": "habitatmech:GOLD.975b14f252", "decision":
    "CONFIRM_UNGROUNDED", "object_id": "", "object_label": "", "grounding_status":
    "", "curator": "claude-opus-5", "date": "2026-08-12", "notes": "Class-level sweep
    (see docs/HARMONIZATION.md#class-level-sweep): no term in the vendored slice matched
    this label by any search route. Whether the concept is a habitat at all was NOT
    assessed, so this is not yet a term-request candidate.", "review_depth": "CLASS",
    "category": "", "relation": ""}}]'
  snapshot_sha256: e5cb2e09f72dd4b18e069c0e2576e25e13e56c9991f4eb5ae47416345e247578
- evidence_id: EP9
  kind: record_content
  reference: data/habitats/host_associated/mammals_human.yaml
  locator: Full immediate-parent record; context only
  accessed_at: '2026-10-15T23:57:45Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.cd0b0940e5", "label": "human-associated
    environment", "definition": "An environmental system determined by a human.",
    "definition_source": "HabitatMech", "habitat_category": "HOST_ASSOCIATED", "grounding_status":
    "UNGROUNDED", "mapping_status": "REVIEWED", "synonyms": [{"synonym_text": "Human",
    "synonym_type": "EXACT_SYNONYM", "source": "BacDive"}, {"synonym_text": "Mammals:
    Human", "synonym_type": "EXACT_SYNONYM", "source": "HabitatMech curation"}, {"synonym_text":
    "human host", "synonym_type": "EXACT_SYNONYM", "source": "HabitatMech curation"}],
    "parent_habitats": ["ENVO:01001000", "ENVO:01001002"], "source_attestations":
    [{"source": "BACDIVE", "source_id": "bacdive.isolation_source:human", "source_label":
    "Human", "assertion_count": 11697, "assertion_unit": "STRAIN", "notes": "kg-microbe''s
    isolation-source mapping table has no ontology target for this source; the automatic
    route leaves it ungrounded. The explicit curator decision SAME_AS overrides that
    route; this source is emitted on habitatmech:GOLD.cd0b0940e5."}, {"source": "GOLD",
    "source_id": "gold.ecosystem:3381", "source_label": "Mammals: Human", "source_path":
    "Host-associated > Mammals: Human", "assertion_count": 40432, "assertion_unit":
    "ORGANISM", "notes": "4 GOLD ecosystem node ids share this path; first shown.
    See data/raw/gold_ecosystem_paths.tsv."}], "characteristic_taxa": [{"taxon_id":
    "NCBITaxon:562", "source": "BACDIVE", "taxon_label": "Escherichia coli", "association_count":
    222, "rank": 1, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:1313", "source":
    "BACDIVE", "taxon_label": "Streptococcus pneumoniae", "association_count": 197,
    "rank": 2, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:197", "source": "BACDIVE",
    "taxon_label": "Campylobacter jejuni", "association_count": 175, "rank": 3, "candidate_pool":
    2068}, {"taxon_id": "NCBITaxon:1280", "source": "BACDIVE", "taxon_label": "Staphylococcus
    aureus", "association_count": 156, "rank": 4, "candidate_pool": 2068}, {"taxon_id":
    "NCBITaxon:1328", "source": "BACDIVE", "taxon_label": "Streptococcus anginosus",
    "association_count": 155, "rank": 5, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:730",
    "source": "BACDIVE", "taxon_label": "[Haemophilus] ducreyi", "association_count":
    125, "rank": 6, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:287", "source":
    "BACDIVE", "taxon_label": "Pseudomonas aeruginosa", "association_count": 113,
    "rank": 7, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:727", "source": "BACDIVE",
    "taxon_label": "Haemophilus influenzae", "association_count": 110, "rank": 8,
    "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:28188", "source": "BACDIVE",
    "taxon_label": "Capnocytophaga canimorsus", "association_count": 108, "rank":
    9, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:1656", "source": "BACDIVE",
    "taxon_label": "Actinomyces viscosus", "association_count": 105, "rank": 10, "candidate_pool":
    2068}, {"taxon_id": "NCBITaxon:47715", "source": "BACDIVE", "taxon_label": "Lacticaseibacillus
    rhamnosus", "association_count": 105, "rank": 11, "candidate_pool": 2068}, {"taxon_id":
    "NCBITaxon:1352", "source": "BACDIVE", "taxon_label": "Enterococcus faecium",
    "association_count": 100, "rank": 12, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:2702",
    "source": "BACDIVE", "taxon_label": "Gardnerella vaginalis", "association_count":
    95, "rank": 13, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:28901", "source":
    "BACDIVE", "taxon_label": "Salmonella enterica", "association_count": 88, "rank":
    14, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:2", "source": "BACDIVE",
    "taxon_label": "Bacteria", "association_count": 87, "rank": 15, "candidate_pool":
    2068}, {"taxon_id": "NCBITaxon:1660", "source": "BACDIVE", "taxon_label": "Schaalia
    odontolytica", "association_count": 76, "rank": 16, "candidate_pool": 2068}, {"taxon_id":
    "NCBITaxon:59505", "source": "BACDIVE", "taxon_label": "Actinotignum schaalii",
    "association_count": 76, "rank": 17, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:46124",
    "source": "BACDIVE", "taxon_label": "Granulicatella adiacens", "association_count":
    75, "rank": 18, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:520", "source":
    "BACDIVE", "taxon_label": "Bordetella pertussis", "association_count": 71, "rank":
    19, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:1720", "source": "BACDIVE",
    "taxon_label": "Corynebacterium sp.", "association_count": 69, "rank": 20, "candidate_pool":
    2068}, {"taxon_id": "NCBITaxon:40324", "source": "BACDIVE", "taxon_label": "Stenotrophomonas
    maltophilia", "association_count": 69, "rank": 21, "candidate_pool": 2068}, {"taxon_id":
    "NCBITaxon:732", "source": "BACDIVE", "taxon_label": "Aggregatibacter aphrophilus",
    "association_count": 68, "rank": 22, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:1655",
    "source": "BACDIVE", "taxon_label": "Actinomyces naeslundii", "association_count":
    66, "rank": 23, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:1305", "source":
    "BACDIVE", "taxon_label": "Streptococcus sanguinis", "association_count": 65,
    "rank": 24, "candidate_pool": 2068}, {"taxon_id": "NCBITaxon:1596", "source":
    "BACDIVE", "taxon_label": "Lactobacillus gasseri", "association_count": 64, "rank":
    25, "candidate_pool": 2068}], "curation_history": [{"timestamp": "2026-08-12T00:00:00Z",
    "curator": "claude-opus-5", "action": "CONFIRM_UNGROUNDED", "changes": "Confirmed
    UNGROUNDED: no ontology term fits this concept. Nearest broader term ENVO:01001002
    ''animal-associated environment'' attached as a parent. Humans as host, the single
    largest ungrounded concept at 40432 GOLD organisms. No human-associated environment
    term exists in ENVO. Deliberately not grounded to animal-associated environment:
    every host clade would then merge onto one record and the host distinction is
    the entire content. Highest-value ENVO term request. (source concept habitatmech:GOLD.cd0b0940e5)"},
    {"timestamp": "2026-08-16T00:00:00Z", "curator": "claude-opus-5", "action": "DEFINED",
    "changes": "Defined as ''human-associated environment'' under ENVO:01001002 ''animal-associated
    environment''. The habitat is the host clade, and it is the entire content of
    the concept: GOLD and BacDive both organise host-associated isolates by host,
    and every downstream anatomical path hangs off it. HabitatMech deliberately does
    not ground these to animal-associated environment, because every clade would then
    merge onto one record and the distinction the sources are making would be lost.
    ENVO already has this shape at plant-, animal- and fungi-associated environment;
    this asks for the same pattern one level down. This is the single largest ungrounded
    concept in the corpus."}, {"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources",
    "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories;
    attested by BACDIVE, GOLD. Grounding: UNGROUNDED."}, {"timestamp": "2026-08-17T00:00:00Z",
    "curator": "claude-opus-5", "action": "SAME_AS", "changes": "Merged into habitatmech:GOLD.cd0b0940e5
    ''Mammals: Human'': the same concept under another source''s name. Novel-concept
    merge (#116): BacDive''s ''Human'' and GOLD''s ''Mammals: Human'' are the same
    habitat \u2014 a human acting as host \u2014 and both are novel, so neither has
    an ontology term to merge on. Before SAME_AS they were two permanent records holding
    40,432 and 11,697 assertions for one concept, published as two pages, and the
    largest habitat in the corpus appeared nowhere as such. Merged onto the GOLD identifier
    because it carries the larger attestation and the deeper path; the choice of which
    id survives is arbitrary between two minted ids and is recorded here rather than
    left to ordering. Both keep their attestations on the merged record, so no evidence
    is lost. (source concept habitatmech:BACDIVE.c9b246fcbb)"}, {"timestamp": "2026-10-10T00:00:00Z",
    "curator": "seed_from_sources", "action": "SOURCE_ATTESTATION_CORRECTED", "changes":
    "Corrected bacdive.isolation_source:human provenance wording to distinguish the
    declined automatic mapping from the final curator override (#1889)."}]}'
  snapshot_sha256: 6d3fba8ddf0a933b0e22f94b17e2df356eb2d297b1d96a7f960575e81d50d4d1
- evidence_id: EX1
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000/graph
  locator: ENVO_01001000-graph.json
  accessed_at: '2026-10-15T23:42:30Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001000",
    "target": "http://purl.obolibrary.org/obo/ENVO_01000254", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001000",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_131567", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: e11b34dbd0a626083d5d0bbbb364469ef95831fb61cb81da5377d59715b272ca
- evidence_id: EX2
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000
  locator: ENVO_01001000.json
  accessed_at: '2026-10-15T23:42:29Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "ENVO:01001000",
    "label": "environmental system determined by an organism", "is_obsolete": false,
    "description": ["An environmental system which is determined by a living organism."]}'
  snapshot_sha256: 8bd797929d18bf28171af7fd10f358db9b093f752d20b99f665779bb2e6b504e
- evidence_id: EX3
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002/graph
  locator: ENVO_01001002-graph.json
  accessed_at: '2026-10-15T23:42:32Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001002",
    "target": "http://purl.obolibrary.org/obo/ENVO_01001000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001002",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_33208", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 882375d994d0dea7166097328c56e0e22362848e68aba0125d1b128a24ebf1b0
- evidence_id: EX4
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002
  locator: ENVO_01001002.json
  accessed_at: '2026-10-15T23:42:31Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "ENVO:01001002",
    "label": "animal-associated environment", "is_obsolete": false, "description":
    ["An environmental system determined by an animal."]}'
  snapshot_sha256: c3c90d5e91cc85727658222c907f7747f34861ad80bf1ceac5ce209f7e170907
- evidence_id: EX5
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6343517/fullTextXML
  locator: PMC6343517.xml
  accessed_at: '2026-10-15T23:45:13Z'
  support: context_only
  summary: PMID:30700982, DOI:10.3389/fmicb.2018.03269. Cell-culture methods and infection
    results explicitly use HeLa 229, ATCC CCL-2.1, with Nigg and Weiss laboratory
    stocks. Supports in vitro cervical adenocarcinoma-cell association only; stock
    lineage is narrower than all historical isolates.
  snapshot_sha256: 0ef49a02fe2d88f6874f739aacab2206943106a4d1f619d862d122a5918c55d0
- evidence_id: ESEARCH
  kind: search
  reference: Local maintained inputs and review archive
  locator: rg --no-ignore --hidden -l -F -e habitatmech:GOLD.975b14f252 -e 'Cell Line'
    -e cell_line__d7fc8c60 -e habitatmech:GOLD.975b14f252 curation history research
    reports data/raw build reviews
  accessed_at: '2026-10-15T23:41:33Z'
  support: context_only
  summary: Identifier/label/slug search and full structured-YAML traversal; exact
    TSV rows were parsed separately. Broad search matches are leads, not all independently
    reviewed.
  search_scope: curation, history, research, reports, data/raw, build and reviews,
    including hidden/ignored content; structured traversal independent of gitignore.
assessments:
- assessment_id: A1
  area: identity
  topic: Identity, definition, category, aliases and hierarchy
  outcome: supported
  summary: The human Cell line source is conservatively minted UNGROUNDED/SEEDED and
    has a human-associated-environment parent, not a whole-human identity. Primary
    HeLa culture evidence supports host-cell biological meaning without claiming these
    exact GOLD samples. Fourteen supplemental biosamples and two study memberships
    are separate measures from the zero frozen tree count; they must not be summed.
  target_ids:
  - habitatmech:GOLD.975b14f252
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - EP9
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
- assessment_id: A2
  area: quantity
  topic: Source assertions, pools, ranks and supplementary context
  outcome: supported
  summary: 'All emitted counts/units, labels, ranks, scores and candidate pools match
    exact frozen rows. [{"source": "GOLD", "count": 0, "unit": "ORGANISM"}]. Zero
    tree counts are omitted; later biosamples and study memberships are not added.
    Current taxonomy resolves displayed identifiers including explicit aliases.'
  target_ids:
  - habitatmech:GOLD.975b14f252
  evidence_ids:
  - E1
  - EEXTRACT
  - ESEED
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
- assessment_id: A3
  area: evidence
  topic: Biological support and bounded source uncertainty
  outcome: supported
  summary: The human Cell line source is conservatively minted UNGROUNDED/SEEDED and
    has a human-associated-environment parent, not a whole-human identity. Primary
    HeLa culture evidence supports host-cell biological meaning without claiming these
    exact GOLD samples. Fourteen supplemental biosamples and two study memberships
    are separate measures from the zero frozen tree count; they must not be summed.
  target_ids:
  - habitatmech:GOLD.975b14f252
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - EP9
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
- assessment_id: A4
  area: completeness
  topic: Native status, optional parameters and causal mechanisms
  outcome: supported
  summary: Executed native resolution reproduces UNGROUNDED/SEEDED. No environmental
    parameters, causal graphs, discussions, datasets or is_characteristic=true claims
    are present. Missing optional fields and SEEDED status alone are not defects;
    parent mechanisms are not inherited.
  target_ids:
  - habitatmech:GOLD.975b14f252
  evidence_ids:
  - E1
  - ESCHEMA
  - ESEED
- assessment_id: A5
  area: schema
  topic: Native validation and reproduction
  outcome: supported
  summary: Target schema/strict checks, 829 histories, source provenance, exact 3209-record
    reproduction, 32 causal overlays, 110 term requests and configured label checks
    passed. Exact-base remote full QC passed. Deterministic validity is separate from
    scientific support; reference-check applicability is stated explicitly.
  target_ids:
  - habitatmech:GOLD.975b14f252
  evidence_ids:
  - E1
  - ERULE
findings: []
actions: []
limitations:
- Source counts, ranks and scores do not establish prevalence, viability or characteristic
  presence. Original specimen-level evidence for every source member has not been
  reconstructed.
- Configured label validation skipped 2063 no-adapter pairs; displayed TaxIds were
  separately resolved against current NCBI including aliases.
- Exact-base full QC was verified remotely, not newly executed locally. New saved
  bundles require a separate archive check.
- 'iModulonDB is not applicable: target assertions contain no gene, regulator or expression-module
  claim. No paid research or native status promotion was performed.'
notes:
- Captured input hashes match both working bytes and exact committed base blobs.
- This observation proposes curation but does not itself mutate inputs. The separately
  authorized PR workflow may address supported findings in later commits.
- Ignored-inclusive archive traversal found no earlier structured target observation.
  Historical prose does not count as a formal predecessor.
tags:
- individual-scientific-review
- host-associated
```
