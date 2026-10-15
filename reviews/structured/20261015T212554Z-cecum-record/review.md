# Record review: cecum (BTO:0000166)

- Review: 20261015T212554Z-cecum-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T21:14:58Z
- Finished UTC: 2026-10-15T21:25:54Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Blocker: an ITEM decision merges the molluscan Cecum/Intestinal cecum source into BTO:0000166, defined through ileum, colon and vermiform appendix. The anatomical scopes are not equivalent. This also introduces a molluscan whole-Hindgut superclass into the generic PREGO record. Preserve the 549-taxon PREGO pool and its top 25 associations while separating source identity; the optional absent Lawsonia label is not a broken TaxId.

## Scope And Provenance

Full field-by-field scientific assessment of this exact target at 62952fb7cdf223af9d1ffbf1cc2f556b22f7ee6b.

Selection: One of the next 24 path-ordered unreviewed identifiers in the ignored-inclusive 3208-record census. This bundle assesses one exact identifier, not a proxy sample.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 62952fb7cdf223af9d1ffbf1cc2f556b22f7ee6b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0000166 | data/habitats/host_associated/cecum.yaml | generated | cecum |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0000166 | Finished 2026-10-15T21:15:01Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/cecum.yaml |
| validate-strict | passed | True | BTO:0000166 | Finished 2026-10-15T21:15:16Z. uv run python scripts/validate_strict.py data/habitats/host_associated/carcinoid.yaml data/habitats/host_associated/carcinoma.yaml data/habitats/host_associated/carcinoma_cell.yaml data/habitats/host_associated/carcinosarcoma.yaml data/habitats/host_associated/cardiac_atrium.yaml data/habitats/host_associated/cardiac_septum.yaml data/habitats/host_associated/cardiac_skeleton.yaml data/habitats/host_associated/cardiac_stomach.yaml data/habitats/host_associated/cardiovascular_system.yaml data/habitats/host_associated/carposphere.yaml data/habitats/host_associated/cartilage.yaml data/habitats/host_associated/cartilage__bd8c407c.yaml data/habitats/host_associated/cartilage__c54322c6.yaml data/habitats/host_associated/caryopsis.yaml data/habitats/host_associated/caski.yaml data/habitats/host_associated/catarrh.yaml data/habitats/host_associated/catarrh__1e78e51c.yaml data/habitats/host_associated/caulosphere.yaml data/habitats/host_associated/ceca.yaml data/habitats/host_associated/ceca__2f9665ca.yaml data/habitats/host_associated/ceca__d15faa5d.yaml data/habitats/host_associated/cecotropes_night_fecs.yaml data/habitats/host_associated/cecum.yaml data/habitats/host_associated/cecum__79e270ae.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | BTO:0000166 | Finished 2026-10-15T21:15:30Z. No issues found<br>824 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | BTO:0000166 | Finished 2026-10-15T21:15:32Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | BTO:0000166 | Finished 2026-10-15T21:16:11Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | BTO:0000166 | Finished 2026-10-15T21:16:19Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | BTO:0000166 | Finished 2026-10-15T21:16:50Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | BTO:0000166 | Finished 2026-10-15T21:17:56Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-baseline native QC | passed | True | BTO:0000166 | Verified 2026-10-15T21:13:04Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38805081742 |

## Scientific And Domain Assessments

### Identity, definition, category and ancestry

identity: concern. Targets: BTO:0000166.

Blocker: an ITEM decision merges the molluscan Cecum/Intestinal cecum source into BTO:0000166, defined through ileum, colon and vermiform appendix. The anatomical scopes are not equivalent. This also introduces a molluscan whole-Hindgut superclass into the generic PREGO record. Preserve the 549-taxon PREGO pool and its top 25 associations while separating source identity; the optional absent Lawsonia label is not a broken TaxId.

### Frozen source counts, units, ranks, channels and pool

quantity: supported. Targets: BTO:0000166.

Exact source rows reproduce all emitted counts and displayed taxon rows. [{"source": "GOLD", "count": 0, "unit": "ORGANISM"}, {"source": "PREGO", "count": 549, "unit": "TAXON"}]. Zero GOLD counts are omitted; supplemental biosamples and study memberships are not added to tree ORGANISM counts.

### Biological support and bounded uncertainty

evidence: supported. Targets: BTO:0000166.

Blocker: an ITEM decision merges the molluscan Cecum/Intestinal cecum source into BTO:0000166, defined through ileum, colon and vermiform appendix. The anatomical scopes are not equivalent. This also introduces a molluscan whole-Hindgut superclass into the generic PREGO record. Preserve the 549-taxon PREGO pool and its top 25 associations while separating source identity; the optional absent Lawsonia label is not a broken TaxId.

### Native status, optional fields and mechanisms

completeness: supported. Targets: BTO:0000166.

Executed resolution reproduces EXACT/REVIEWED. No target environmental parameters, causal graphs, discussions, datasets or is_characteristic=true claims are present. Optional absence and SEEDED status alone do not warrant findings; parent mechanisms are not inherited.

### Deterministic validity and source fidelity

schema: supported. Targets: BTO:0000166.

Ordinary/strict target validation, 824 histories, source provenance, exact 3208-record reproduction, 32 causal overlays, 110 term requests, configured labels and exact-base remote QC passed. These are not substitutes for scientific identity assessment.

## Findings

### F1: Containing anatomy is emitted as a broader habitat class

major / open / confirmed; issue key: cecum-context-parent.

Exclude only the exact GOLD source-path/expected-parent contribution habitatmech:GOLD.c336fb0bb7. Blocker: an ITEM decision merges the molluscan Cecum/Intestinal cecum source into BTO:0000166, defined through ileum, colon and vermiform appendix. The anatomical scopes are not equivalent. This also introduces a molluscan whole-Hindgut superclass into the generic PREGO record. Preserve the 549-taxon PREGO pool and its top 25 associations while separating source identity; the optional absent Lawsonia label is not a broken TaxId. Preserve independent valid ontology genera and raw source paths.

### F2: Molluscan cecum is merged into incompatible large-intestinal anatomy

blocker / open / confirmed; issue key: cecum-molluscan-vertebrate-cecum-merge.

Blocker: an ITEM decision merges the molluscan Cecum/Intestinal cecum source into BTO:0000166, defined through ileum, colon and vermiform appendix. The anatomical scopes are not equivalent. This also introduces a molluscan whole-Hindgut superclass into the generic PREGO record. Preserve the 549-taxon PREGO pool and its top 25 associations while separating source identity; the optional absent Lawsonia label is not a broken TaxId. Reassess GOLD mint habitatmech:GOLD.37d9cdc188 and PREGO mint habitatmech:PREGO.35b3d0b858 separately. Reverse only unsupported equivalence through maintained decisions; preserve all PREGO associations/counts and original source identity. No exact replacement genus is established here.

### F3: Maintained grounding note truncates the source name

minor / open / confirmed; issue key: cecum-decision-note-truncated-path.

The maintained ITEM note ends Cecum/Intest rather than the full source leaf Cecum/Intestinal cecum. Correct the maintained explanation as part of a history-preserving reassessment; do not rewrite committed history. The complete attestation path is already retained.

## Recommended Actions And Acceptance Checks

### ACT1

Exclude only the exact GOLD source-path/expected-parent contribution habitatmech:GOLD.c336fb0bb7. Blocker: an ITEM decision merges the molluscan Cecum/Intestinal cecum source into BTO:0000166, defined through ileum, colon and vermiform appendix. The anatomical scopes are not equivalent. This also introduces a molluscan whole-Hindgut superclass into the generic PREGO record. Preserve the 549-taxon PREGO pool and its top 25 associations while separating source identity; the optional absent Lawsonia label is not a broken TaxId. Preserve independent valid ontology genera and raw source paths. No repair is performed by this review.

- Regress the exact claim, preserving independent valid genera, raw provenance and source counts/units. Change native status or mappings only when supported by the authorized ITEM assessment; never decrement source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

### ACT2

Blocker: an ITEM decision merges the molluscan Cecum/Intestinal cecum source into BTO:0000166, defined through ileum, colon and vermiform appendix. The anatomical scopes are not equivalent. This also introduces a molluscan whole-Hindgut superclass into the generic PREGO record. Preserve the 549-taxon PREGO pool and its top 25 associations while separating source identity; the optional absent Lawsonia label is not a broken TaxId. Reassess GOLD mint habitatmech:GOLD.37d9cdc188 and PREGO mint habitatmech:PREGO.35b3d0b858 separately. Reverse only unsupported equivalence through maintained decisions; preserve all PREGO associations/counts and original source identity. No exact replacement genus is established here. No repair is performed by this review.

- Regress the exact claim, preserving independent valid genera, raw provenance and source counts/units. Change native status or mappings only when supported by the authorized ITEM assessment; never decrement source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

### ACT3

The maintained ITEM note ends Cecum/Intest rather than the full source leaf Cecum/Intestinal cecum. Correct the maintained explanation as part of a history-preserving reassessment; do not rewrite committed history. The complete attestation path is already retained. No repair is performed by this review.

- Regress the exact claim, preserving independent valid genera, raw provenance and source counts/units. Change native status or mappings only when supported by the authorized ITEM assessment; never decrement source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/cecum.yaml; Entire target YAML | supports | All fields, displayed taxa, source attestations and complete generated history read. |
| ERULE | docs/CURATION.md; Identity, strictly broader hierarchy and source evidence rules | supports | All parent contributions must be strictly broader. Disease, organism, sampled material and habitat meanings are distinct. Optional absence is not automatically a defect. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; HabitatRecord, SourceAttestation, TaxonAssociation and category semantics | supports | Source mapping endpoints are source-to-record. Reported associations do not imply characteristic presence. Native category and optional-field contracts retained. |
| ESEED | src/habitatmech/seed.py; Executed source resolution and full generated-document reproduction | supports | [{"mint": "habitatmech:GOLD.37d9cdc188", "automatic": {"identifier": "habitatmech:GOLD.37d9cdc188", "grounding_status": "UNGROUNDED", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "gold_unmatched", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "BTO:0000166", "grounding_status": "EXACT", "mapping_predicate": "skos:exactMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "curated_ground_from_gold_unmatched", "category": null, "reviewed": true, "decision": {"identifier": "habitatmech:GOLD.37d9cdc188", "decision": "GROUND", "object_id": "BTO:0000166", "object_label": "cecum", "grounding_status": "EXACT", "curator": "claude-opus-5", "date": "2026-08-12", "notes": "Slash alternative naming one structure. Path: Host-associated &gt; Mollusca &gt; Digestive system &gt; Hindgut &gt; Cecum/Intest", "review_depth": "ITEM", "category": "", "relation": "parent"}}}, {"mint": "habitatmech:PREGO.35b3d0b858", "automatic": {"identifier": "BTO:0000166", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "BTO:0000166", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "curated_review_of_prego_self_grounded", "category": null, "reviewed": true, "decision": {"identifier": "habitatmech:PREGO.35b3d0b858", "decision": "REVIEW", "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-13", "notes": "Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date.", "review_depth": "ITEM", "category": "", "relation": "parent"}}}] |
| EEXTRACT | src/habitatmech/extract.py; Source projections, taxon ranking and counts | supports | Frozen counts/units, maximum scores, channels, candidate pools and top taxon rows were traced to exact source rows. Original PREGO pair citation links are not retained in this projection. |
| ET5 | data/raw/gold_ecosystem_paths.tsv; Physical TSV rows 2479 | supports | [{"row": 2479, "data": {"canonical_path": "Host-associated &gt; Mollusca &gt; Digestive system &gt; Hindgut &gt; Cecum/Intestinal cecum", "ecosystem": "Host-associated", "ecosystem_category": "Mollusca", "ecosystem_type": "Digestive system", "ecosystem_subtype": "Hindgut", "specific_ecosystem": "Cecum/Intestinal cecum", "leaf_label": "Cecum/Intestinal cecum", "depth": "5", "gold_node_count": "1", "organism_count": "0", "study_count": "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids": "gold.ecosystem:7832"}}] |
| ET6 | data/raw/prego_habitat_taxa.tsv; Physical TSV rows 214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238 | supports | [{"row": 214, "data": {"prego_id": "BTO:0000166", "rank": "1", "taxon_id": "NCBITaxon:100176", "taxon_label": "Papillibacter cinnamivorans", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 215, "data": {"prego_id": "BTO:0000166", "rank": "2", "taxon_id": "NCBITaxon:100883", "taxon_label": "Coprobacillus", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 216, "data": {"prego_id": "BTO:0000166", "rank": "3", "taxon_id": "NCBITaxon:102106", "taxon_label": "Collinsella", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 217, "data": {"prego_id": "BTO:0000166", "rank": "4", "taxon_id": "NCBITaxon:102234", "taxon_label": "Cyanobacterium", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 218, "data": {"prego_id": "BTO:0000166", "rank": "5", "taxon_id": "NCBITaxon:1032526", "taxon_label": "Pedosphaera", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 219, "data": {"prego_id": "BTO:0000166", "rank": "6", "taxon_id": "NCBITaxon:1091138", "taxon_label": "", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 220, "data": {"prego_id": "BTO:0000166", "rank": "7", "taxon_id": "NCBITaxon:109326", "taxon_label": "Anaerovorax", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 221, "data": {"prego_id": "BTO:0000166", "rank": "8", "taxon_id": "NCBITaxon:1117", "taxon_label": "Cyanobacteriota", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 222, "data": {"prego_id": "BTO:0000166", "rank": "9", "taxon_id": "NCBITaxon:113286", "taxon_label": "Pseudoramibacter", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 223, "data": {"prego_id": "BTO:0000166", "rank": "10", "taxon_id": "NCBITaxon:117563", "taxon_label": "Granulicatella", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 224, "data": {"prego_id": "BTO:0000166", "rank": "11", "taxon_id": "NCBITaxon:118747", "taxon_label": "Bulleidia", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 225, "data": {"prego_id": "BTO:0000166", "rank": "12", "taxon_id": "NCBITaxon:119852", "taxon_label": "Oscillospira", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 226, "data": {"prego_id": "BTO:0000166", "rank": "13", "taxon_id": "NCBITaxon:1249", "taxon_label": "Weissella paramesenteroides", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 227, "data": {"prego_id": "BTO:0000166", "rank": "14", "taxon_id": "NCBITaxon:1253", "taxon_label": "Pediococcus", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 228, "data": {"prego_id": "BTO:0000166", "rank": "15", "taxon_id": "NCBITaxon:1263", "taxon_label": "Ruminococcus", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 229, "data": {"prego_id": "BTO:0000166", "rank": "16", "taxon_id": "NCBITaxon:1265", "taxon_label": "Ruminococcus flavefaciens", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 230, "data": {"prego_id": "BTO:0000166", "rank": "17", "taxon_id": "NCBITaxon:1266", "taxon_label": "Sarcina", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 231, "data": {"prego_id": "BTO:0000166", "rank": "18", "taxon_id": "NCBITaxon:1268", "taxon_label": "Micrococcaceae", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 232, "data": {"prego_id": "BTO:0000166", "rank": "19", "taxon_id": "NCBITaxon:1269", "taxon_label": "Micrococcus", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 233, "data": {"prego_id": "BTO:0000166", "rank": "20", "taxon_id": "NCBITaxon:1279", "taxon_label": "Staphylococcus", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 234, "data": {"prego_id": "BTO:0000166", "rank": "21", "taxon_id": "NCBITaxon:1280", "taxon_label": "Staphylococcus aureus", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 235, "data": {"prego_id": "BTO:0000166", "rank": "22", "taxon_id": "NCBITaxon:1282", "taxon_label": "Staphylococcus epidermidis", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 236, "data": {"prego_id": "BTO:0000166", "rank": "23", "taxon_id": "NCBITaxon:128827", "taxon_label": "Erysipelotrichaceae", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 237, "data": {"prego_id": "BTO:0000166", "rank": "24", "taxon_id": "NCBITaxon:1296", "taxon_label": "Mammaliicoccus sciuri", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 238, "data": {"prego_id": "BTO:0000166", "rank": "25", "taxon_id": "NCBITaxon:1300", "taxon_label": "Streptococcaceae", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}] |
| ET7 | data/raw/prego_habitats.tsv; Physical TSV rows 96 | supports | [{"row": 96, "data": {"prego_id": "BTO:0000166", "ontology": "BTO", "biolink_category": "biolink:GrossAnatomicalStructure", "taxon_count": "549", "direct_assertion_count": "551", "max_prego_score": "4", "channels": "annotated_genomes_isolates&#124;environmental_samples", "prego_synonyms": "blind intestine&#124;blind intestines&#124;blind intestinous&#124;blindgut&#124;blindguts&#124;caeca&#124;caecal&#124;caecum&#124;caecums&#124;ceca&#124;cecal&#124;cecum&#124;cecums&#124;intestinum caeca&#124;intestinum caecal&#124;intestinum caecum&#124;intestinum caecums&#124;intestinum crassum caeca&#124;intestinum crassum caecal&#124;intestinum crassum caecum&#124;intestinum crassum caecums&#124;intestinum crassum ceca&#124;intestinum crassum cecal&#124;intestinum crassum cecum&#124;intestinum crassum cecums"}}] |
| ET8 | data/raw/ontology_terms.tsv; Physical TSV rows 168 | supports | [{"row": 168, "data": {"term_id": "BTO:0000166", "ontology": "BTO", "label": "cecum", "definition": "The first part of the large intestine, forming a dilated pouch into which open the ileum, colon, and appendix vermiformis.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}] |
| ET9 | curation/decisions.tsv; Physical TSV rows 411,1433 | supports | [{"row": 411, "data": {"identifier": "habitatmech:GOLD.37d9cdc188", "decision": "GROUND", "object_id": "BTO:0000166", "object_label": "cecum", "grounding_status": "EXACT", "curator": "claude-opus-5", "date": "2026-08-12", "notes": "Slash alternative naming one structure. Path: Host-associated &gt; Mollusca &gt; Digestive system &gt; Hindgut &gt; Cecum/Intest", "review_depth": "ITEM", "category": "", "relation": ""}}, {"row": 1433, "data": {"identifier": "habitatmech:PREGO.35b3d0b858", "decision": "REVIEW", "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-13", "notes": "Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date.", "review_depth": "ITEM", "category": "", "relation": ""}}] |
| EP10 | data/habitats/host_associated/hindgut__baf4e5ab.yaml; Entire immediate parent record; context only | supports | {"identifier": "habitatmech:GOLD.c336fb0bb7", "label": "Hindgut", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0001046", "habitatmech:GOLD.3baeffe4f8"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:7830", "source_label": "Hindgut", "source_path": "Host-associated &gt; Mollusca &gt; Digestive system &gt; Hindgut", "mapping_predicate": "skos:narrowMatch", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NARROW."}]} |
| ELEGACY | reports/yaml_record_review/20261002T213538Z-cecum.md; Findings and proposed edits; historical lead | supports | The earlier accepted report verified reproducibility of the GOLD/PREGO merge but did not establish cross-host anatomical equivalence. The current assessment rejects that scientific inference while preserving the correctly reproduced source provenance. |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000166/graph; BTO_0000166-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000166", "target": "http://purl.obolibrary.org/obo/BTO_0000706", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/BTO_0000166", "target": "http://purl.obolibrary.org/obo/BTO_0002273", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000166; BTO_0000166.json | context_only | Current term identity, active status and definition: {"obo_id": "BTO:0000166", "label": "cecum", "is_obsolete": false, "description": ["The first part of the large intestine, forming a dilated pouch into which open the ileum, colon, and appendix vermiformis."]} |
| EX3 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11413930/fullTextXML; PMC11413930.xml | context_only | PMID:39140156, DOI:10.1242/bio.060429. Octopus maya dissection methods inspected: digestive juice was obtained in the region between distal cecum and crop, with separate digestive-gland sampling. This is a bounded nonvertebrate anatomical witness, not identification of the particular GOLD mollusc or a proposed replacement ontology term. |
| EX4 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML; PMC8879827.xml | context_only | PMID:35208748, DOI:10.3390/microorganisms10020293. PREGO methods 2.3 and source-channel/score paragraphs inspected. BioProject-associated abstract mining yields score-three associations; genomic metadata and environmental channels have different scoring. The source channel and score are not proof of direct localization, characteristic presence or prevalence. This does not establish the exact extraction route of any individual retained pair. |
| EX5 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001046/graph; UBERON_0001046-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001046", "target": "http://purl.obolibrary.org/obo/UBERON_0004921", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001046", "target": "http://purl.obolibrary.org/obo/RO_0002577", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001046", "target": "http://purl.obolibrary.org/obo/UBERON_0001045", "uri": "http://purl.obolibrary.org/obo/uberon/core#proximally_connected_to", "label": "proximally connected to"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001046", "target": "http://purl.obolibrary.org/obo/UBERON_0003104", "uri": "http://purl.obolibrary.org/obo/RO_0002202", "label": "develops from"}] |
| EX6 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001046; UBERON_0001046.json | context_only | Current term identity, active status and definition: {"obo_id": "UBERON:0001046", "label": "hindgut", "is_obsolete": false, "description": ["The caudalmost subdivision of a digestive tract."]} |
| EX7 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=100176,100883,102106,102234,1032526,1091138,109326,1117,113286,1150864,117563,118747,119852,1249,1253,1263,1265,1266,1268,1269,1276220,1276221,1279,1280,1282,128827,1296,1300,1329250&amp;retmode=xml; taxonomy.xml | context_only | Current NCBI identities and source-label comparisons: [{"id": "NCBITaxon:100176", "source": "PREGO", "label": "Papillibacter cinnamivorans", "current_id": "100176", "current_name": "Papillibacter cinnamivorans", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:100883", "source": "PREGO", "label": "Coprobacillus", "current_id": "100883", "current_name": "Coprobacillus", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:102106", "source": "PREGO", "label": "Collinsella", "current_id": "102106", "current_name": "Collinsella", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:102234", "source": "PREGO", "label": "Cyanobacterium", "current_id": "102234", "current_name": "Cyanobacterium", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1032526", "source": "PREGO", "label": "Pedosphaera", "current_id": "1032526", "current_name": "Pedosphaera", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1091138", "source": "PREGO", "label": null, "current_id": "1091138", "current_name": "Lawsonia", "rank": "genus", "direct_match": false, "recognized_alias": false}, {"id": "NCBITaxon:109326", "source": "PREGO", "label": "Anaerovorax", "current_id": "109326", "current_name": "Anaerovorax", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1117", "source": "PREGO", "label": "Cyanobacteriota", "current_id": "1117", "current_name": "Cyanobacteriota", "rank": "phylum", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:113286", "source": "PREGO", "label": "Pseudoramibacter", "current_id": "113286", "current_name": "Pseudoramibacter", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:117563", "source": "PREGO", "label": "Granulicatella", "current_id": "117563", "current_name": "Granulicatella", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:118747", "source": "PREGO", "label": "Bulleidia", "current_id": "118747", "current_name": "Bulleidia", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:119852", "source": "PREGO", "label": "Oscillospira", "current_id": "119852", "current_name": "Oscillospira", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1249", "source": "PREGO", "label": "Weissella paramesenteroides", "current_id": "1249", "current_name": "Weissella paramesenteroides", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1253", "source": "PREGO", "label": "Pediococcus", "current_id": "1253", "current_name": "Pediococcus", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1263", "source": "PREGO", "label": "Ruminococcus", "current_id": "1263", "current_name": "Ruminococcus", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1265", "source": "PREGO", "label": "Ruminococcus flavefaciens", "current_id": "1265", "current_name": "Ruminococcus flavefaciens", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1266", "source": "PREGO", "label": "Sarcina", "current_id": "1266", "current_name": "Sarcina", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1268", "source": "PREGO", "label": "Micrococcaceae", "current_id": "1268", "current_name": "Micrococcaceae", "rank": "family", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1269", "source": "PREGO", "label": "Micrococcus", "current_id": "1269", "current_name": "Micrococcus", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1279", "source": "PREGO", "label": "Staphylococcus", "current_id": "1279", "current_name": "Staphylococcus", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1280", "source": "PREGO", "label": "Staphylococcus aureus", "current_id": "1280", "current_name": "Staphylococcus aureus", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1282", "source": "PREGO", "label": "Staphylococcus epidermidis", "current_id": "1282", "current_name": "Staphylococcus epidermidis", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:128827", "source": "PREGO", "label": "Erysipelotrichaceae", "current_id": "128827", "current_name": "Erysipelotrichaceae", "rank": "family", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1296", "source": "PREGO", "label": "Mammaliicoccus sciuri", "current_id": "1296", "current_name": "Mammaliicoccus sciuri", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1300", "source": "PREGO", "label": "Streptococcaceae", "current_id": "1300", "current_name": "Streptococcaceae", "rank": "family", "direct_match": true, "recognized_alias": true}] |
| ESEARCH | Local maintained inputs and structured archive; rg --no-ignore --hidden -l -F -e BTO:0000166 -e cecum -e cecum -e habitatmech:GOLD.37d9cdc188 -e habitatmech:PREGO.35b3d0b858 curation history research reports data/raw build reviews | context_only | Exact source rows were parsed separately; no formal structured target predecessor was found. Broad label matches were treated as leads, not all read. |
| EAVAIL | Configured kg-microbe checkout; find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe -type f -path '*/prego/*' -name '*.tsv' | context_only | No prego-directory TSV files were found in this checkout. Original pair-level exports remain unavailable; this is not a global absence claim. |

## Limits And Additional Notes

- Individual source specimens and all original pair-level citations have not been independently reconstructed. Counts, ranks and source scores are not prevalence or characteristic presence.
- Configured label validation skips 2061 no-adapter pairs. Displayed TaxIds were separately checked against current NCBI Taxonomy.
- Full QC evidence is a successful remote run at the exact unchanged scientific input base, not a new local full-QC execution. These new bundles require their own post-save archive check.
- iModulonDB is not applicable to target claims: no gene, regulator, expression module or causal mechanism is asserted. Papers mentioning genes are used only for source context. No paid research was used.
- Original PREGO pair-level exports are unavailable locally. Inspected primary witnesses do not reconstruct every original pair or establish its exact extraction route.
- All captured local inputs were compared with both current bytes and exact Git-base blobs. The review explicitly assesses that committed revision.
- Ignored-inclusive archive search found no previous structured observation targeting this identifier. Legacy prose is a lead, not formal predecessor lineage or automatic closure.
- Read-only review: no curation, generation, native status/history promotion or GitHub mutation.
- The earlier accepted report verified reproducibility of the GOLD/PREGO merge but did not establish cross-host anatomical equivalence. The current assessment rejects that scientific inference while preserving the correctly reproduced source provenance.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T212554Z-cecum-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: cecum (BTO:0000166)'
started_at: '2026-10-15T21:14:58Z'
finished_at: '2026-10-15T21:25:54Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent assesses target and evidence; not independent reviewer
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Blocker: an ITEM decision merges the molluscan Cecum/Intestinal cecum source
  into BTO:0000166, defined through ileum, colon and vermiform appendix. The anatomical
  scopes are not equivalent. This also introduces a molluscan whole-Hindgut superclass
  into the generic PREGO record. Preserve the 549-taxon PREGO pool and its top 25
  associations while separating source identity; the optional absent Lawsonia label
  is not a broken TaxId.'
source:
  git_revision: 62952fb7cdf223af9d1ffbf1cc2f556b22f7ee6b
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
    sha256: 490d3478aadc1dc3c4f04770d06db02fead4964d2e40ff339bfa389d46a5918a
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 37dc4b40642d19e7b5c3262f368d12daa82e03115e7731a2326ae88785ceff5b
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 12be4a7eccfcc6a9b9ef89fc1cb009e8f5e9ab87005bd6eb7ba93c910abf8f6d
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
    sha256: b0135af0aa4deed0f3824a2f491d5a742c1b7de4775c533f283761d22e805821
    role: context
  - path: data/habitats/RETIRED.tsv
    sha256: a2a0496837ea75e487d7fc5d35317a890262a941d8fffe9babcd39f2f332c6db
    role: context
  - path: data/habitats/host_associated/cecum.yaml
    sha256: 623da28718fc205e72e52b35719ed08693a1d8b5850f49df7b38ebff5438815c
    role: target
  - path: data/habitats/host_associated/hindgut__baf4e5ab.yaml
    sha256: 6e72dd4a24120d31e4146a5f1a827adea23d1867f3325fe729c485f5e0084154
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
  - path: reports/yaml_record_review/20261002T213538Z-cecum.md
    sha256: aa685ea691fab134ed520e1446b7f273a8f1440329e75d876afdf9cc8721aca5
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
- target_id: BTO:0000166
  path: data/habitats/host_associated/cecum.yaml
  label: cecum
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
  description: Full field-by-field scientific assessment of this exact target at 62952fb7cdf223af9d1ffbf1cc2f556b22f7ee6b.
  selection: One of the next 24 path-ordered unreviewed identifiers in the ignored-inclusive
    3208-record census. This bundle assesses one exact identifier, not a proxy sample.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - BTO:0000166
  exclusions:
  - target: Other records and SSSOM/KGX products
    reason: Parent context and source witnesses do not add reviewed identifiers. Export
      conformance and individual source specimens are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/cecum.yaml
  exit_code: 0
  target_ids:
  - BTO:0000166
  summary: "Finished 2026-10-15T21:15:01Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/cecum.yaml"
  scope_note: Ordinary schema for this target; strict check covers all 24 named targets;
    other documented checks have full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/carcinoid.yaml data/habitats/host_associated/carcinoma.yaml
    data/habitats/host_associated/carcinoma_cell.yaml data/habitats/host_associated/carcinosarcoma.yaml
    data/habitats/host_associated/cardiac_atrium.yaml data/habitats/host_associated/cardiac_septum.yaml
    data/habitats/host_associated/cardiac_skeleton.yaml data/habitats/host_associated/cardiac_stomach.yaml
    data/habitats/host_associated/cardiovascular_system.yaml data/habitats/host_associated/carposphere.yaml
    data/habitats/host_associated/cartilage.yaml data/habitats/host_associated/cartilage__bd8c407c.yaml
    data/habitats/host_associated/cartilage__c54322c6.yaml data/habitats/host_associated/caryopsis.yaml
    data/habitats/host_associated/caski.yaml data/habitats/host_associated/catarrh.yaml
    data/habitats/host_associated/catarrh__1e78e51c.yaml data/habitats/host_associated/caulosphere.yaml
    data/habitats/host_associated/ceca.yaml data/habitats/host_associated/ceca__2f9665ca.yaml
    data/habitats/host_associated/ceca__d15faa5d.yaml data/habitats/host_associated/cecotropes_night_fecs.yaml
    data/habitats/host_associated/cecum.yaml data/habitats/host_associated/cecum__79e270ae.yaml
  exit_code: 0
  target_ids:
  - BTO:0000166
  summary: "Finished 2026-10-15T21:15:16Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/carcinoid.yaml data/habitats/host_associated/carcinoma.yaml\
    \ data/habitats/host_associated/carcinoma_cell.yaml data/habitats/host_associated/carcinosarcoma.yaml\
    \ data/habitats/host_associated/cardiac_atrium.yaml data/habitats/host_associated/cardiac_septum.yaml\
    \ data/habitats/host_associated/cardiac_skeleton.yaml data/habitats/host_associated/cardiac_stomach.yaml\
    \ data/habitats/host_associated/cardiovascular_system.yaml data/habitats/host_associated/carposphere.yaml\
    \ data/habitats/host_associated/cartilage.yaml data/habitats/host_associated/cartilage__bd8c407c.yaml\
    \ data/habitats/host_associated/cartilage__c54322c6.yaml data/habitats/host_associated/caryopsis.yaml\
    \ data/habitats/host_associated/caski.yaml data/habitats/host_associated/catarrh.yaml\
    \ data/habitats/host_associated/catarrh__1e78e51c.yaml data/habitats/host_associated/caulosphere.yaml\
    \ data/habitats/host_associated/ceca.yaml data/habitats/host_associated/ceca__2f9665ca.yaml\
    \ data/habitats/host_associated/ceca__d15faa5d.yaml data/habitats/host_associated/cecotropes_night_fecs.yaml\
    \ data/habitats/host_associated/cecum.yaml data/habitats/host_associated/cecum__79e270ae.yaml\n\
    Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      24\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Ordinary schema for this target; strict check covers all 24 named targets;
    other documented checks have full-corpus scope.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - BTO:0000166
  summary: 'Finished 2026-10-15T21:15:30Z. No issues found

    824 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Ordinary schema for this target; strict check covers all 24 named targets;
    other documented checks have full-corpus scope.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - BTO:0000166
  summary: "Finished 2026-10-15T21:15:32Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Ordinary schema for this target; strict check covers all 24 named targets;
    other documented checks have full-corpus scope.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - BTO:0000166
  summary: "Finished 2026-10-15T21:16:11Z. expected 3208 records, found 3208 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Ordinary schema for this target; strict check covers all 24 named targets;
    other documented checks have full-corpus scope.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - BTO:0000166
  summary: "Finished 2026-10-15T21:16:19Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Ordinary schema for this target; strict check covers all 24 named targets;
    other documented checks have full-corpus scope.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - BTO:0000166
  summary: "Finished 2026-10-15T21:16:50Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Ordinary schema for this target; strict check covers all 24 named targets;
    other documented checks have full-corpus scope.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - BTO:0000166
  summary: "Finished 2026-10-15T21:17:56Z. id↔label correspondence summary:\n    \
    \      OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Ordinary schema for this target; strict check covers all 24 named targets;
    other documented checks have full-corpus scope.
- check_id: CCI
  name: Exact-baseline native QC
  status: passed
  required: true
  command: gh run view 38805081742 --json status,conclusion,headSha,url,jobs
  exit_code: 0
  target_ids:
  - BTO:0000166
  summary: Verified 2026-10-15T21:13:04Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38805081742
  scope_note: Unchanged committed scientific-input baseline. New output bundles are
    outside this remote execution.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/cecum.yaml
  locator: Entire target YAML
  accessed_at: '2026-10-15T21:25:54Z'
  support: supports
  summary: All fields, displayed taxa, source attestations and complete generated
    history read.
  snapshot_sha256: 623da28718fc205e72e52b35719ed08693a1d8b5850f49df7b38ebff5438815c
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, strictly broader hierarchy and source evidence rules
  accessed_at: '2026-10-15T21:25:54Z'
  support: supports
  summary: All parent contributions must be strictly broader. Disease, organism, sampled
    material and habitat meanings are distinct. Optional absence is not automatically
    a defect.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: HabitatRecord, SourceAttestation, TaxonAssociation and category semantics
  accessed_at: '2026-10-15T21:25:54Z'
  support: supports
  summary: Source mapping endpoints are source-to-record. Reported associations do
    not imply characteristic presence. Native category and optional-field contracts
    retained.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed source resolution and full generated-document reproduction
  accessed_at: '2026-10-15T21:25:54Z'
  support: supports
  summary: '[{"mint": "habitatmech:GOLD.37d9cdc188", "automatic": {"identifier": "habitatmech:GOLD.37d9cdc188",
    "grounding_status": "UNGROUNDED", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "gold_unmatched", "category":
    null, "reviewed": false, "decision": null}, "final": {"identifier": "BTO:0000166",
    "grounding_status": "EXACT", "mapping_predicate": "skos:exactMatch", "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "curated_ground_from_gold_unmatched",
    "category": null, "reviewed": true, "decision": {"identifier": "habitatmech:GOLD.37d9cdc188",
    "decision": "GROUND", "object_id": "BTO:0000166", "object_label": "cecum", "grounding_status":
    "EXACT", "curator": "claude-opus-5", "date": "2026-08-12", "notes": "Slash alternative
    naming one structure. Path: Host-associated > Mollusca > Digestive system > Hindgut
    > Cecum/Intest", "review_depth": "ITEM", "category": "", "relation": "parent"}}},
    {"mint": "habitatmech:PREGO.35b3d0b858", "automatic": {"identifier": "BTO:0000166",
    "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded",
    "category": null, "reviewed": false, "decision": null}, "final": {"identifier":
    "BTO:0000166", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "curated_review_of_prego_self_grounded",
    "category": null, "reviewed": true, "decision": {"identifier": "habitatmech:PREGO.35b3d0b858",
    "decision": "REVIEW", "object_id": "", "object_label": "", "grounding_status":
    "", "curator": "claude-opus-5", "date": "2026-08-13", "notes": "Multi-source review
    pass: this record is attested by more than one independent vocabulary, and this
    source''s label or path was read against the record''s ontology term to check
    the merge is right. It agrees. Source concepts in the same pass whose labels did
    not agree were re-decided rather than endorsed; see the pass''s other decisions
    of the same date.", "review_depth": "ITEM", "category": "", "relation": "parent"}}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: Source projections, taxon ranking and counts
  accessed_at: '2026-10-15T21:25:54Z'
  support: supports
  summary: Frozen counts/units, maximum scores, channels, candidate pools and top
    taxon rows were traced to exact source rows. Original PREGO pair citation links
    are not retained in this projection.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Physical TSV rows 2479
  accessed_at: '2026-10-15T21:25:54Z'
  support: supports
  summary: '[{"row": 2479, "data": {"canonical_path": "Host-associated > Mollusca
    > Digestive system > Hindgut > Cecum/Intestinal cecum", "ecosystem": "Host-associated",
    "ecosystem_category": "Mollusca", "ecosystem_type": "Digestive system", "ecosystem_subtype":
    "Hindgut", "specific_ecosystem": "Cecum/Intestinal cecum", "leaf_label": "Cecum/Intestinal
    cecum", "depth": "5", "gold_node_count": "1", "organism_count": "0", "study_count":
    "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids": "gold.ecosystem:7832"}}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: ET6
  kind: database
  reference: data/raw/prego_habitat_taxa.tsv
  locator: Physical TSV rows 214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238
  accessed_at: '2026-10-15T21:25:54Z'
  support: supports
  summary: '[{"row": 214, "data": {"prego_id": "BTO:0000166", "rank": "1", "taxon_id":
    "NCBITaxon:100176", "taxon_label": "Papillibacter cinnamivorans", "prego_score":
    "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}, {"row": 215, "data": {"prego_id": "BTO:0000166", "rank": "2", "taxon_id":
    "NCBITaxon:100883", "taxon_label": "Coprobacillus", "prego_score": "4", "direct_flag":
    "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row":
    216, "data": {"prego_id": "BTO:0000166", "rank": "3", "taxon_id": "NCBITaxon:102106",
    "taxon_label": "Collinsella", "prego_score": "4", "direct_flag": "TRUE", "channels":
    "environmental_samples", "corroborated_by": ""}}, {"row": 217, "data": {"prego_id":
    "BTO:0000166", "rank": "4", "taxon_id": "NCBITaxon:102234", "taxon_label": "Cyanobacterium",
    "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples",
    "corroborated_by": ""}}, {"row": 218, "data": {"prego_id": "BTO:0000166", "rank":
    "5", "taxon_id": "NCBITaxon:1032526", "taxon_label": "Pedosphaera", "prego_score":
    "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}, {"row": 219, "data": {"prego_id": "BTO:0000166", "rank": "6", "taxon_id":
    "NCBITaxon:1091138", "taxon_label": "", "prego_score": "4", "direct_flag": "TRUE",
    "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 220, "data":
    {"prego_id": "BTO:0000166", "rank": "7", "taxon_id": "NCBITaxon:109326", "taxon_label":
    "Anaerovorax", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples",
    "corroborated_by": ""}}, {"row": 221, "data": {"prego_id": "BTO:0000166", "rank":
    "8", "taxon_id": "NCBITaxon:1117", "taxon_label": "Cyanobacteriota", "prego_score":
    "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}, {"row": 222, "data": {"prego_id": "BTO:0000166", "rank": "9", "taxon_id":
    "NCBITaxon:113286", "taxon_label": "Pseudoramibacter", "prego_score": "4", "direct_flag":
    "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row":
    223, "data": {"prego_id": "BTO:0000166", "rank": "10", "taxon_id": "NCBITaxon:117563",
    "taxon_label": "Granulicatella", "prego_score": "4", "direct_flag": "TRUE", "channels":
    "environmental_samples", "corroborated_by": ""}}, {"row": 224, "data": {"prego_id":
    "BTO:0000166", "rank": "11", "taxon_id": "NCBITaxon:118747", "taxon_label": "Bulleidia",
    "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples",
    "corroborated_by": ""}}, {"row": 225, "data": {"prego_id": "BTO:0000166", "rank":
    "12", "taxon_id": "NCBITaxon:119852", "taxon_label": "Oscillospira", "prego_score":
    "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}, {"row": 226, "data": {"prego_id": "BTO:0000166", "rank": "13", "taxon_id":
    "NCBITaxon:1249", "taxon_label": "Weissella paramesenteroides", "prego_score":
    "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}, {"row": 227, "data": {"prego_id": "BTO:0000166", "rank": "14", "taxon_id":
    "NCBITaxon:1253", "taxon_label": "Pediococcus", "prego_score": "4", "direct_flag":
    "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row":
    228, "data": {"prego_id": "BTO:0000166", "rank": "15", "taxon_id": "NCBITaxon:1263",
    "taxon_label": "Ruminococcus", "prego_score": "4", "direct_flag": "TRUE", "channels":
    "environmental_samples", "corroborated_by": ""}}, {"row": 229, "data": {"prego_id":
    "BTO:0000166", "rank": "16", "taxon_id": "NCBITaxon:1265", "taxon_label": "Ruminococcus
    flavefaciens", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples",
    "corroborated_by": ""}}, {"row": 230, "data": {"prego_id": "BTO:0000166", "rank":
    "17", "taxon_id": "NCBITaxon:1266", "taxon_label": "Sarcina", "prego_score": "4",
    "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}, {"row": 231, "data": {"prego_id": "BTO:0000166", "rank": "18", "taxon_id":
    "NCBITaxon:1268", "taxon_label": "Micrococcaceae", "prego_score": "4", "direct_flag":
    "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row":
    232, "data": {"prego_id": "BTO:0000166", "rank": "19", "taxon_id": "NCBITaxon:1269",
    "taxon_label": "Micrococcus", "prego_score": "4", "direct_flag": "TRUE", "channels":
    "environmental_samples", "corroborated_by": ""}}, {"row": 233, "data": {"prego_id":
    "BTO:0000166", "rank": "20", "taxon_id": "NCBITaxon:1279", "taxon_label": "Staphylococcus",
    "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples",
    "corroborated_by": ""}}, {"row": 234, "data": {"prego_id": "BTO:0000166", "rank":
    "21", "taxon_id": "NCBITaxon:1280", "taxon_label": "Staphylococcus aureus", "prego_score":
    "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}, {"row": 235, "data": {"prego_id": "BTO:0000166", "rank": "22", "taxon_id":
    "NCBITaxon:1282", "taxon_label": "Staphylococcus epidermidis", "prego_score":
    "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}, {"row": 236, "data": {"prego_id": "BTO:0000166", "rank": "23", "taxon_id":
    "NCBITaxon:128827", "taxon_label": "Erysipelotrichaceae", "prego_score": "4",
    "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}, {"row": 237, "data": {"prego_id": "BTO:0000166", "rank": "24", "taxon_id":
    "NCBITaxon:1296", "taxon_label": "Mammaliicoccus sciuri", "prego_score": "4",
    "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}, {"row": 238, "data": {"prego_id": "BTO:0000166", "rank": "25", "taxon_id":
    "NCBITaxon:1300", "taxon_label": "Streptococcaceae", "prego_score": "4", "direct_flag":
    "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}]'
  snapshot_sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
- evidence_id: ET7
  kind: database
  reference: data/raw/prego_habitats.tsv
  locator: Physical TSV rows 96
  accessed_at: '2026-10-15T21:25:54Z'
  support: supports
  summary: '[{"row": 96, "data": {"prego_id": "BTO:0000166", "ontology": "BTO", "biolink_category":
    "biolink:GrossAnatomicalStructure", "taxon_count": "549", "direct_assertion_count":
    "551", "max_prego_score": "4", "channels": "annotated_genomes_isolates|environmental_samples",
    "prego_synonyms": "blind intestine|blind intestines|blind intestinous|blindgut|blindguts|caeca|caecal|caecum|caecums|ceca|cecal|cecum|cecums|intestinum
    caeca|intestinum caecal|intestinum caecum|intestinum caecums|intestinum crassum
    caeca|intestinum crassum caecal|intestinum crassum caecum|intestinum crassum caecums|intestinum
    crassum ceca|intestinum crassum cecal|intestinum crassum cecum|intestinum crassum
    cecums"}}]'
  snapshot_sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
- evidence_id: ET8
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 168
  accessed_at: '2026-10-15T21:25:54Z'
  support: supports
  summary: '[{"row": 168, "data": {"term_id": "BTO:0000166", "ontology": "BTO", "label":
    "cecum", "definition": "The first part of the large intestine, forming a dilated
    pouch into which open the ileum, colon, and appendix vermiformis.", "synonyms":
    "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: ET9
  kind: database
  reference: curation/decisions.tsv
  locator: Physical TSV rows 411,1433
  accessed_at: '2026-10-15T21:25:54Z'
  support: supports
  summary: '[{"row": 411, "data": {"identifier": "habitatmech:GOLD.37d9cdc188", "decision":
    "GROUND", "object_id": "BTO:0000166", "object_label": "cecum", "grounding_status":
    "EXACT", "curator": "claude-opus-5", "date": "2026-08-12", "notes": "Slash alternative
    naming one structure. Path: Host-associated > Mollusca > Digestive system > Hindgut
    > Cecum/Intest", "review_depth": "ITEM", "category": "", "relation": ""}}, {"row":
    1433, "data": {"identifier": "habitatmech:PREGO.35b3d0b858", "decision": "REVIEW",
    "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5",
    "date": "2026-08-13", "notes": "Multi-source review pass: this record is attested
    by more than one independent vocabulary, and this source''s label or path was
    read against the record''s ontology term to check the merge is right. It agrees.
    Source concepts in the same pass whose labels did not agree were re-decided rather
    than endorsed; see the pass''s other decisions of the same date.", "review_depth":
    "ITEM", "category": "", "relation": ""}}]'
  snapshot_sha256: 490d3478aadc1dc3c4f04770d06db02fead4964d2e40ff339bfa389d46a5918a
- evidence_id: EP10
  kind: record_content
  reference: data/habitats/host_associated/hindgut__baf4e5ab.yaml
  locator: Entire immediate parent record; context only
  accessed_at: '2026-10-15T21:25:54Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.c336fb0bb7", "label": "Hindgut", "habitat_category":
    "HOST_ASSOCIATED", "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats":
    ["UBERON:0001046", "habitatmech:GOLD.3baeffe4f8"], "source_attestations": [{"source":
    "GOLD", "source_id": "gold.ecosystem:7830", "source_label": "Hindgut", "source_path":
    "Host-associated > Mollusca > Digestive system > Hindgut", "mapping_predicate":
    "skos:narrowMatch", "notes": "2 GOLD ecosystem node ids share this path; first
    shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp":
    "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES",
    "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NARROW."}]}'
  snapshot_sha256: 6e72dd4a24120d31e4146a5f1a827adea23d1867f3325fe729c485f5e0084154
- evidence_id: ELEGACY
  kind: record_content
  reference: reports/yaml_record_review/20261002T213538Z-cecum.md
  locator: Findings and proposed edits; historical lead
  accessed_at: '2026-10-15T21:25:54Z'
  support: supports
  summary: The earlier accepted report verified reproducibility of the GOLD/PREGO
    merge but did not establish cross-host anatomical equivalence. The current assessment
    rejects that scientific inference while preserving the correctly reproduced source
    provenance.
  snapshot_sha256: aa685ea691fab134ed520e1446b7f273a8f1440329e75d876afdf9cc8721aca5
- evidence_id: EX1
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000166/graph
  locator: BTO_0000166-graph.json
  accessed_at: '2026-10-15T21:13:52Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000166",
    "target": "http://purl.obolibrary.org/obo/BTO_0000706", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/BTO_0000166",
    "target": "http://purl.obolibrary.org/obo/BTO_0002273", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 5a3b1f1eca1553a995153a1970d6cdf6e439879e0efa6f51d18c3d534a131cd9
- evidence_id: EX2
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000166
  locator: BTO_0000166.json
  accessed_at: '2026-10-15T21:13:51Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "BTO:0000166",
    "label": "cecum", "is_obsolete": false, "description": ["The first part of the
    large intestine, forming a dilated pouch into which open the ileum, colon, and
    appendix vermiformis."]}'
  snapshot_sha256: a1996ad92a59beb60230672c36476edd1ef43af133fc7a65b57dc75b2eb965b8
- evidence_id: EX3
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11413930/fullTextXML
  locator: PMC11413930.xml
  accessed_at: '2026-10-15T21:21:13Z'
  support: context_only
  summary: 'PMID:39140156, DOI:10.1242/bio.060429. Octopus maya dissection methods
    inspected: digestive juice was obtained in the region between distal cecum and
    crop, with separate digestive-gland sampling. This is a bounded nonvertebrate
    anatomical witness, not identification of the particular GOLD mollusc or a proposed
    replacement ontology term.'
  snapshot_sha256: 704feed586f3c8185b5884f39407ecd5c8c3ec73e8c736f79b673bb7f5268be5
- evidence_id: EX4
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML
  locator: PMC8879827.xml
  accessed_at: '2026-10-15T21:15:53Z'
  support: context_only
  summary: PMID:35208748, DOI:10.3390/microorganisms10020293. PREGO methods 2.3 and
    source-channel/score paragraphs inspected. BioProject-associated abstract mining
    yields score-three associations; genomic metadata and environmental channels have
    different scoring. The source channel and score are not proof of direct localization,
    characteristic presence or prevalence. This does not establish the exact extraction
    route of any individual retained pair.
  snapshot_sha256: 375f0fde4d07bb823cb9106aa4567bc0ef03c2866af0b2a7740b543f50687c25
- evidence_id: EX5
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001046/graph
  locator: UBERON_0001046-graph.json
  accessed_at: '2026-10-15T21:14:10Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001046",
    "target": "http://purl.obolibrary.org/obo/UBERON_0004921", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001046",
    "target": "http://purl.obolibrary.org/obo/RO_0002577", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001046",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001045", "uri": "http://purl.obolibrary.org/obo/uberon/core#proximally_connected_to",
    "label": "proximally connected to"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001046",
    "target": "http://purl.obolibrary.org/obo/UBERON_0003104", "uri": "http://purl.obolibrary.org/obo/RO_0002202",
    "label": "develops from"}]'
  snapshot_sha256: b2d6340b12c64d11d629c3bf222b46c51c5c6bcd4e68fa064f912bd198968e5e
- evidence_id: EX6
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001046
  locator: UBERON_0001046.json
  accessed_at: '2026-10-15T21:14:09Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "UBERON:0001046",
    "label": "hindgut", "is_obsolete": false, "description": ["The caudalmost subdivision
    of a digestive tract."]}'
  snapshot_sha256: f65ee5feea5c3a4fcfb07e6bc51713bd73c261363eaf039b32068d5a620d6fd9
- evidence_id: EX7
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=100176,100883,102106,102234,1032526,1091138,109326,1117,113286,1150864,117563,118747,119852,1249,1253,1263,1265,1266,1268,1269,1276220,1276221,1279,1280,1282,128827,1296,1300,1329250&retmode=xml
  locator: taxonomy.xml
  accessed_at: '2026-10-15T21:14:28Z'
  support: context_only
  summary: 'Current NCBI identities and source-label comparisons: [{"id": "NCBITaxon:100176",
    "source": "PREGO", "label": "Papillibacter cinnamivorans", "current_id": "100176",
    "current_name": "Papillibacter cinnamivorans", "rank": "species", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:100883", "source": "PREGO",
    "label": "Coprobacillus", "current_id": "100883", "current_name": "Coprobacillus",
    "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:102106",
    "source": "PREGO", "label": "Collinsella", "current_id": "102106", "current_name":
    "Collinsella", "rank": "genus", "direct_match": true, "recognized_alias": true},
    {"id": "NCBITaxon:102234", "source": "PREGO", "label": "Cyanobacterium", "current_id":
    "102234", "current_name": "Cyanobacterium", "rank": "genus", "direct_match": true,
    "recognized_alias": true}, {"id": "NCBITaxon:1032526", "source": "PREGO", "label":
    "Pedosphaera", "current_id": "1032526", "current_name": "Pedosphaera", "rank":
    "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1091138",
    "source": "PREGO", "label": null, "current_id": "1091138", "current_name": "Lawsonia",
    "rank": "genus", "direct_match": false, "recognized_alias": false}, {"id": "NCBITaxon:109326",
    "source": "PREGO", "label": "Anaerovorax", "current_id": "109326", "current_name":
    "Anaerovorax", "rank": "genus", "direct_match": true, "recognized_alias": true},
    {"id": "NCBITaxon:1117", "source": "PREGO", "label": "Cyanobacteriota", "current_id":
    "1117", "current_name": "Cyanobacteriota", "rank": "phylum", "direct_match": true,
    "recognized_alias": true}, {"id": "NCBITaxon:113286", "source": "PREGO", "label":
    "Pseudoramibacter", "current_id": "113286", "current_name": "Pseudoramibacter",
    "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:117563",
    "source": "PREGO", "label": "Granulicatella", "current_id": "117563", "current_name":
    "Granulicatella", "rank": "genus", "direct_match": true, "recognized_alias": true},
    {"id": "NCBITaxon:118747", "source": "PREGO", "label": "Bulleidia", "current_id":
    "118747", "current_name": "Bulleidia", "rank": "genus", "direct_match": true,
    "recognized_alias": true}, {"id": "NCBITaxon:119852", "source": "PREGO", "label":
    "Oscillospira", "current_id": "119852", "current_name": "Oscillospira", "rank":
    "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1249",
    "source": "PREGO", "label": "Weissella paramesenteroides", "current_id": "1249",
    "current_name": "Weissella paramesenteroides", "rank": "species", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:1253", "source": "PREGO", "label":
    "Pediococcus", "current_id": "1253", "current_name": "Pediococcus", "rank": "genus",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1263", "source":
    "PREGO", "label": "Ruminococcus", "current_id": "1263", "current_name": "Ruminococcus",
    "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1265",
    "source": "PREGO", "label": "Ruminococcus flavefaciens", "current_id": "1265",
    "current_name": "Ruminococcus flavefaciens", "rank": "species", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:1266", "source": "PREGO", "label":
    "Sarcina", "current_id": "1266", "current_name": "Sarcina", "rank": "genus", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:1268", "source": "PREGO", "label":
    "Micrococcaceae", "current_id": "1268", "current_name": "Micrococcaceae", "rank":
    "family", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1269",
    "source": "PREGO", "label": "Micrococcus", "current_id": "1269", "current_name":
    "Micrococcus", "rank": "genus", "direct_match": true, "recognized_alias": true},
    {"id": "NCBITaxon:1279", "source": "PREGO", "label": "Staphylococcus", "current_id":
    "1279", "current_name": "Staphylococcus", "rank": "genus", "direct_match": true,
    "recognized_alias": true}, {"id": "NCBITaxon:1280", "source": "PREGO", "label":
    "Staphylococcus aureus", "current_id": "1280", "current_name": "Staphylococcus
    aureus", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id":
    "NCBITaxon:1282", "source": "PREGO", "label": "Staphylococcus epidermidis", "current_id":
    "1282", "current_name": "Staphylococcus epidermidis", "rank": "species", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:128827", "source": "PREGO",
    "label": "Erysipelotrichaceae", "current_id": "128827", "current_name": "Erysipelotrichaceae",
    "rank": "family", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1296",
    "source": "PREGO", "label": "Mammaliicoccus sciuri", "current_id": "1296", "current_name":
    "Mammaliicoccus sciuri", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:1300", "source": "PREGO", "label": "Streptococcaceae",
    "current_id": "1300", "current_name": "Streptococcaceae", "rank": "family", "direct_match":
    true, "recognized_alias": true}]'
  snapshot_sha256: c551a5443e12b82516bb46ffbdca086137c0079452de57edc2884a991cd694a2
- evidence_id: ESEARCH
  kind: search
  reference: Local maintained inputs and structured archive
  locator: rg --no-ignore --hidden -l -F -e BTO:0000166 -e cecum -e cecum -e habitatmech:GOLD.37d9cdc188
    -e habitatmech:PREGO.35b3d0b858 curation history research reports data/raw build
    reviews
  accessed_at: '2026-10-15T21:13:37Z'
  support: context_only
  summary: Exact source rows were parsed separately; no formal structured target predecessor
    was found. Broad label matches were treated as leads, not all read.
  search_scope: curation, history, research, reports, data/raw, build and reviews;
    hidden/ignored content included, with structured review.yaml parsing independent
    of gitignore.
- evidence_id: EAVAIL
  kind: search
  reference: Configured kg-microbe checkout
  locator: find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe
    -type f -path '*/prego/*' -name '*.tsv'
  accessed_at: '2026-10-15T21:15:13Z'
  support: context_only
  summary: No prego-directory TSV files were found in this checkout. Original pair-level
    exports remain unavailable; this is not a global absence claim.
  search_scope: find across the configured checkout, including hidden and ignored
    files.
assessments:
- assessment_id: A1
  area: identity
  topic: Identity, definition, category and ancestry
  outcome: concern
  summary: 'Blocker: an ITEM decision merges the molluscan Cecum/Intestinal cecum
    source into BTO:0000166, defined through ileum, colon and vermiform appendix.
    The anatomical scopes are not equivalent. This also introduces a molluscan whole-Hindgut
    superclass into the generic PREGO record. Preserve the 549-taxon PREGO pool and
    its top 25 associations while separating source identity; the optional absent
    Lawsonia label is not a broken TaxId.'
  target_ids:
  - BTO:0000166
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - ET9
  - EP10
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  dimensions:
  - name: native_status
    value: EXACT/REVIEWED
    definition: Generated grounding and curation status, distinct from scientific
      review verdict.
    evidence_ids:
    - E1
    - ESEED
- assessment_id: A2
  area: quantity
  topic: Frozen source counts, units, ranks, channels and pool
  outcome: supported
  summary: 'Exact source rows reproduce all emitted counts and displayed taxon rows.
    [{"source": "GOLD", "count": 0, "unit": "ORGANISM"}, {"source": "PREGO", "count":
    549, "unit": "TAXON"}]. Zero GOLD counts are omitted; supplemental biosamples
    and study memberships are not added to tree ORGANISM counts.'
  target_ids:
  - BTO:0000166
  evidence_ids:
  - E1
  - EEXTRACT
  - ESEED
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  dimensions:
  - name: source_assertion_units
    value: '[{"source": "GOLD", "count": 0, "unit": "ORGANISM"}, {"source": "PREGO",
      "count": 549, "unit": "TAXON"}]'
    definition: Frozen counts with noninterchangeable source units; zero GOLD counts
      are verified in raw rows.
    evidence_ids:
    - E1
    - EEXTRACT
- assessment_id: A3
  area: evidence
  topic: Biological support and bounded uncertainty
  outcome: supported
  summary: 'Blocker: an ITEM decision merges the molluscan Cecum/Intestinal cecum
    source into BTO:0000166, defined through ileum, colon and vermiform appendix.
    The anatomical scopes are not equivalent. This also introduces a molluscan whole-Hindgut
    superclass into the generic PREGO record. Preserve the 549-taxon PREGO pool and
    its top 25 associations while separating source identity; the optional absent
    Lawsonia label is not a broken TaxId.'
  target_ids:
  - BTO:0000166
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - ET9
  - EP10
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
- assessment_id: A4
  area: completeness
  topic: Native status, optional fields and mechanisms
  outcome: supported
  summary: Executed resolution reproduces EXACT/REVIEWED. No target environmental
    parameters, causal graphs, discussions, datasets or is_characteristic=true claims
    are present. Optional absence and SEEDED status alone do not warrant findings;
    parent mechanisms are not inherited.
  target_ids:
  - BTO:0000166
  evidence_ids:
  - E1
  - ESCHEMA
  - ESEED
- assessment_id: A5
  area: schema
  topic: Deterministic validity and source fidelity
  outcome: supported
  summary: Ordinary/strict target validation, 824 histories, source provenance, exact
    3208-record reproduction, 32 causal overlays, 110 term requests, configured labels
    and exact-base remote QC passed. These are not substitutes for scientific identity
    assessment.
  target_ids:
  - BTO:0000166
  evidence_ids:
  - E1
  - ERULE
findings:
- finding_id: F1
  issue_key: cecum-context-parent
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Containing anatomy is emitted as a broader habitat class
  description: 'Exclude only the exact GOLD source-path/expected-parent contribution
    habitatmech:GOLD.c336fb0bb7. Blocker: an ITEM decision merges the molluscan Cecum/Intestinal
    cecum source into BTO:0000166, defined through ileum, colon and vermiform appendix.
    The anatomical scopes are not equivalent. This also introduces a molluscan whole-Hindgut
    superclass into the generic PREGO record. Preserve the 549-taxon PREGO pool and
    its top 25 associations while separating source identity; the optional absent
    Lawsonia label is not a broken TaxId. Preserve independent valid ontology genera
    and raw source paths.'
  target_ids:
  - BTO:0000166
  field_paths:
  - parent_habitats
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - ET9
  - EP10
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported hierarchy, mapping or source-evidence
    semantics; correct deterministic reproduction does not establish scientific support.
  external_issues: []
- finding_id: F2
  issue_key: cecum-molluscan-vertebrate-cecum-merge
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Molluscan cecum is merged into incompatible large-intestinal anatomy
  description: 'Blocker: an ITEM decision merges the molluscan Cecum/Intestinal cecum
    source into BTO:0000166, defined through ileum, colon and vermiform appendix.
    The anatomical scopes are not equivalent. This also introduces a molluscan whole-Hindgut
    superclass into the generic PREGO record. Preserve the 549-taxon PREGO pool and
    its top 25 associations while separating source identity; the optional absent
    Lawsonia label is not a broken TaxId. Reassess GOLD mint habitatmech:GOLD.37d9cdc188
    and PREGO mint habitatmech:PREGO.35b3d0b858 separately. Reverse only unsupported
    equivalence through maintained decisions; preserve all PREGO associations/counts
    and original source identity. No exact replacement genus is established here.'
  target_ids:
  - BTO:0000166
  field_paths:
  - identifier
  - definition
  - synonyms
  - source_attestations
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - ET9
  - EP10
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: blocker
  normalization_reason: Incompatible anatomical identities are treated as exact equivalents,
    causing a source concept to denote the wrong thing.
  external_issues: []
- finding_id: F3
  issue_key: cecum-decision-note-truncated-path
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Maintained grounding note truncates the source name
  description: The maintained ITEM note ends Cecum/Intest rather than the full source
    leaf Cecum/Intestinal cecum. Correct the maintained explanation as part of a history-preserving
    reassessment; do not rewrite committed history. The complete attestation path
    is already retained.
  target_ids:
  - BTO:0000166
  field_paths:
  - curation_history
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - ET9
  - EP10
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: minor
  normalization_reason: Bounded maintained-provenance wording error; the full source
    path is retained elsewhere.
  external_issues: []
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - BTO:0000166
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: 'Exclude only the exact GOLD source-path/expected-parent contribution
    habitatmech:GOLD.c336fb0bb7. Blocker: an ITEM decision merges the molluscan Cecum/Intestinal
    cecum source into BTO:0000166, defined through ileum, colon and vermiform appendix.
    The anatomical scopes are not equivalent. This also introduces a molluscan whole-Hindgut
    superclass into the generic PREGO record. Preserve the 549-taxon PREGO pool and
    its top 25 associations while separating source identity; the optional absent
    Lawsonia label is not a broken TaxId. Preserve independent valid ontology genera
    and raw source paths. No repair is performed by this review.'
  generator: Controlled source refresh when required, then just seed, guarded just
    seed-canary, just seed-apply, and dependent term-request/map/site/redirect regeneration.
  acceptance_checks:
  - Regress the exact claim, preserving independent valid genera, raw provenance and
    source counts/units. Change native status or mappings only when supported by the
    authorized ITEM assessment; never decrement source totals by hand.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
- action_id: ACT2
  finding_ids:
  - F2
  target_ids:
  - BTO:0000166
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  description: 'Blocker: an ITEM decision merges the molluscan Cecum/Intestinal cecum
    source into BTO:0000166, defined through ileum, colon and vermiform appendix.
    The anatomical scopes are not equivalent. This also introduces a molluscan whole-Hindgut
    superclass into the generic PREGO record. Preserve the 549-taxon PREGO pool and
    its top 25 associations while separating source identity; the optional absent
    Lawsonia label is not a broken TaxId. Reassess GOLD mint habitatmech:GOLD.37d9cdc188
    and PREGO mint habitatmech:PREGO.35b3d0b858 separately. Reverse only unsupported
    equivalence through maintained decisions; preserve all PREGO associations/counts
    and original source identity. No exact replacement genus is established here.
    No repair is performed by this review.'
  generator: Controlled source refresh when required, then just seed, guarded just
    seed-canary, just seed-apply, and dependent term-request/map/site/redirect regeneration.
  acceptance_checks:
  - Regress the exact claim, preserving independent valid genera, raw provenance and
    source counts/units. Change native status or mappings only when supported by the
    authorized ITEM assessment; never decrement source totals by hand.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
- action_id: ACT3
  finding_ids:
  - F3
  target_ids:
  - BTO:0000166
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: The maintained ITEM note ends Cecum/Intest rather than the full source
    leaf Cecum/Intestinal cecum. Correct the maintained explanation as part of a history-preserving
    reassessment; do not rewrite committed history. The complete attestation path
    is already retained. No repair is performed by this review.
  generator: Controlled source refresh when required, then just seed, guarded just
    seed-canary, just seed-apply, and dependent term-request/map/site/redirect regeneration.
  acceptance_checks:
  - Regress the exact claim, preserving independent valid genera, raw provenance and
    source counts/units. Change native status or mappings only when supported by the
    authorized ITEM assessment; never decrement source totals by hand.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
limitations:
- Individual source specimens and all original pair-level citations have not been
  independently reconstructed. Counts, ranks and source scores are not prevalence
  or characteristic presence.
- Configured label validation skips 2061 no-adapter pairs. Displayed TaxIds were separately
  checked against current NCBI Taxonomy.
- Full QC evidence is a successful remote run at the exact unchanged scientific input
  base, not a new local full-QC execution. These new bundles require their own post-save
  archive check.
- 'iModulonDB is not applicable to target claims: no gene, regulator, expression module
  or causal mechanism is asserted. Papers mentioning genes are used only for source
  context. No paid research was used.'
- Original PREGO pair-level exports are unavailable locally. Inspected primary witnesses
  do not reconstruct every original pair or establish its exact extraction route.
notes:
- All captured local inputs were compared with both current bytes and exact Git-base
  blobs. The review explicitly assesses that committed revision.
- Ignored-inclusive archive search found no previous structured observation targeting
  this identifier. Legacy prose is a lead, not formal predecessor lineage or automatic
  closure.
- 'Read-only review: no curation, generation, native status/history promotion or GitHub
  mutation.'
- The earlier accepted report verified reproducibility of the GOLD/PREGO merge but
  did not establish cross-host anatomical equivalence. The current assessment rejects
  that scientific inference while preserving the correctly reproduced source provenance.
tags:
- individual-scientific-review
- host-associated
```
