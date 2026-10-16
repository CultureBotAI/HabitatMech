# Record review: cob (BTO:0000266)

- Review: 20261016T035436Z-cob-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-16T03:35:20Z
- Finished UTC: 2026-10-16T03:54:36Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The identity denotes the maize-ear axis/core, not an entire inflorescence. BTO nevertheless imports spike as a superclass; its own spike definition denotes the whole inflorescence, exposing a component/class conflict. The GOLD phyllosphere context is compatible with broad above-ground plant association and is not rejected by treating phyllosphere as only leaves. PREGO retains two score-three taxa: exact XZL9 has positive growth evidence on processed corncob molasses but soil isolation, while exact 6Ac is described from a wastewater reactor. Distinguish feedstock use, isolation source and anatomical cob association before reclassifying either pair.

## Scope And Provenance

Full field-by-field assessment of this one resolved generated record.

Selection: One of the next 24 unreviewed records selected in deterministic path order from the ignored-inclusive 3209-record census. This bundle assesses exactly one target, not a proxy sample.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 67cde35918d7361de3a1164fb22756cba5d20e30.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0000266 | data/habitats/host_associated/cob.yaml | generated | cob |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0000266 | Finished 2026-10-16T03:35:52Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/cob.yaml |
| validate-strict | passed | True | BTO:0000266 | Finished 2026-10-16T03:36:32Z. uv run python scripts/validate_strict.py data/habitats/host_associated/clasper.yaml data/habitats/host_associated/claw.yaml data/habitats/host_associated/cloaca.yaml data/habitats/host_associated/cloaca__f527d4ff.yaml data/habitats/host_associated/cnidarian_associated_environment.yaml data/habitats/host_associated/cob.yaml data/habitats/host_associated/cocoon.yaml data/habitats/host_associated/coelom.yaml data/habitats/host_associated/coelom__d65ea80b.yaml data/habitats/host_associated/colon.yaml data/habitats/host_associated/colon__a0dd5461.yaml data/habitats/host_associated/colon__ff534087.yaml data/habitats/host_associated/colon_cancer.yaml data/habitats/host_associated/colon_mucosa.yaml data/habitats/host_associated/colon_mucosa__7a8e4588.yaml data/habitats/host_associated/colon_mucosa__b687aead.yaml data/habitats/host_associated/colon_mucosa__de31f03f.yaml data/habitats/host_associated/colonic.yaml data/habitats/host_associated/colonic_cancer_cell.yaml data/habitats/host_associated/colonic_epithelium.yaml data/habitats/host_associated/colonic_mucosa.yaml data/habitats/host_associated/colorectal_polyps.yaml data/habitats/host_associated/colorectum.yaml data/habitats/host_associated/colostrum.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | BTO:0000266 | Finished 2026-10-16T03:36:40Z. No issues found<br>831 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | BTO:0000266 | Finished 2026-10-16T03:36:40Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | BTO:0000266 | Finished 2026-10-16T03:37:54Z. expected 3209 records, found 3209 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | BTO:0000266 | Finished 2026-10-16T03:38:04Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | BTO:0000266 | Finished 2026-10-16T03:38:23Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | BTO:0000266 | Finished 2026-10-16T03:39:05Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1173<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2063<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-base hosted native QC | passed | True | BTO:0000266 | Verified 2026-10-16T03:43:47Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38843593114 |
| Displayed candidate-pool correspondence | passed | False | BTO:0000266 | Finished 2026-10-16T03:54:30Z. All 60 displayed candidate pools equal exact source taxon totals. |
| Standalone citation validation applicability | not_applicable | False | BTO:0000266 | No standalone citation checker is documented for these evidence-free generated targets. Stable references were checked with native gates and current authorities; causal validation ran globally. |

## Scientific And Domain Assessments

### Identity, grounding, aliases and strictly broader hierarchy

identity: concern. Targets: BTO:0000266.

The identity denotes the maize-ear axis/core, not an entire inflorescence. BTO nevertheless imports spike as a superclass; its own spike definition denotes the whole inflorescence, exposing a component/class conflict. The GOLD phyllosphere context is compatible with broad above-ground plant association and is not rejected by treating phyllosphere as only leaves. PREGO retains two score-three taxa: exact XZL9 has positive growth evidence on processed corncob molasses but soil isolation, while exact 6Ac is described from a wastewater reactor. Distinguish feedstock use, isolation source and anatomical cob association before reclassifying either pair.

### Native source units, ranks, scores and candidate pools

quantity: supported. Targets: BTO:0000266.

Exact source rows reproduce every emitted count/unit and displayed taxon rank/score/pool. Zero tree counts are omitted; supplemental biosamples, study memberships and triads are nonadditive. {"assertions": [{"source": "GOLD", "count": 0, "unit": "ORGANISM", "row": {"row": 2518, "data": {"canonical_path": "Host-associated &gt; Plants &gt; Phyllosphere &gt; Cob", "ecosystem": "Host-associated", "ecosystem_category": "Plants", "ecosystem_type": "Phyllosphere", "ecosystem_subtype": "Cob", "specific_ecosystem": "", "leaf_label": "Cob", "depth": "4", "gold_node_count": "2", "organism_count": "0", "study_count": "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids": "gold.ecosystem:5739&#124;gold.ecosystem:5740"}}}, {"source": "PREGO", "count": 2, "unit": "TAXON", "row": {"row": 470, "data": {"prego_id": "BTO:0000266", "ontology": "BTO", "biolink_category": "biolink:GrossAnatomicalStructure", "taxon_count": "2", "direct_assertion_count": "2", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms": "cob&#124;corn cob&#124;corn cobs&#124;corncob&#124;corncobs&#124;maize cob&#124;maize cobs"}}}], "taxa": [{"id": "NCBITaxon:1110509", "source": "PREGO", "label": "Methanothrix harundinacea 6Ac", "current_id": "1110509", "current_name": "Methanothrix harundinacea 6Ac", "rank": "strain", "direct_match": true, "recognized_alias": true, "other_names": ["Methanosaeta harundinacea 6Ac", "Methanosaeta sp. 6Ac"], "source_row": {"row": 376, "data": {"prego_id": "BTO:0000266", "rank": "1", "taxon_id": "NCBITaxon:1110509", "taxon_label": "Methanothrix harundinacea 6Ac", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}}, {"id": "NCBITaxon:1245026", "source": "PREGO", "label": "Heyndrickxia coagulans XZL9", "current_id": "1245026", "current_name": "Heyndrickxia coagulans XZL9", "rank": "strain", "direct_match": true, "recognized_alias": true, "other_names": ["Bacillus coagulans XZL9", "Weizmannia coagulans XZL9"], "source_row": {"row": 377, "data": {"prego_id": "BTO:0000266", "rank": "2", "taxon_id": "NCBITaxon:1245026", "taxon_label": "Heyndrickxia coagulans XZL9", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}}]}

### Association evidence and claim scope

evidence: concern. Targets: BTO:0000266.

Current ontology/TaxId identities and source attestations were verified. The identity denotes the maize-ear axis/core, not an entire inflorescence. BTO nevertheless imports spike as a superclass; its own spike definition denotes the whole inflorescence, exposing a component/class conflict. The GOLD phyllosphere context is compatible with broad above-ground plant association and is not rejected by treating phyllosphere as only leaves. PREGO retains two score-three taxa: exact XZL9 has positive growth evidence on processed corncob molasses but soil isolation, while exact 6Ac is described from a wastewater reactor. Distinguish feedstock use, isolation source and anatomical cob association before reclassifying either pair. Individual papers support only the stated scope; original source pairs were not exhaustively reconstructed.

### Native lifecycle, optional content and mechanism limits

completeness: supported. Targets: BTO:0000266.

Executed native routes reproduce EXACT/REVIEWED. Required content is present. No optional environmental parameters, causal graph, discussion, dataset or characteristic-presence claim is fabricated. Missing ITEM status alone is not a defect; no status or history promotion is performed.

### Native validation and reproducibility

schema: supported. Targets: BTO:0000266.

31 baseline commands passed: target schema, cohort strict, 831 histories, source provenance, exact 3209-record reproduction, 32 causal overlays, 110 term requests and configured labels. Exact-base hosted QC passed. Deterministic validity is not scientific approval.

## Findings

### F1: Imported ontology parent conflicts with the class definition

major / open / confirmed; issue key: cob-ontology-parent-scope.

The identity denotes the maize-ear axis/core, not an entire inflorescence. BTO nevertheless imports spike as a superclass; its own spike definition denotes the whole inflorescence, exposing a component/class conflict. The GOLD phyllosphere context is compatible with broad above-ground plant association and is not rejected by treating phyllosphere as only leaves. PREGO retains two score-three taxa: exact XZL9 has positive growth evidence on processed corncob molasses but soil isolation, while exact 6Ac is described from a wastewater reactor. Distinguish feedstock use, isolation source and anatomical cob association before reclassifying either pair. Resolve the upstream BTO class scope and true relation before a controlled ontology refresh or explicit supported local correction. GOLD-parent exclusions cannot remove this independently imported ontology edge.

### F2: Recover original pair evidence before interpreting localization

major / open / provisional; issue key: cob-prego-pair-evidence.

The identity denotes the maize-ear axis/core, not an entire inflorescence. BTO nevertheless imports spike as a superclass; its own spike definition denotes the whole inflorescence, exposing a component/class conflict. The GOLD phyllosphere context is compatible with broad above-ground plant association and is not rejected by treating phyllosphere as only leaves. PREGO retains two score-three taxa: exact XZL9 has positive growth evidence on processed corncob molasses but soil isolation, while exact 6Ac is described from a wastewater reactor. Distinguish feedstock use, isolation source and anatomical cob association before reclassifying either pair. Recover manifest-matching original pair, channel and dictionary/citation provenance. Competing origins, feedstocks and assay contexts are evidence questions, not proof of biological absence or a demonstrated extraction bug.

## Recommended Actions And Acceptance Checks

### ACT1

The identity denotes the maize-ear axis/core, not an entire inflorescence. BTO nevertheless imports spike as a superclass; its own spike definition denotes the whole inflorescence, exposing a component/class conflict. The GOLD phyllosphere context is compatible with broad above-ground plant association and is not rejected by treating phyllosphere as only leaves. PREGO retains two score-three taxa: exact XZL9 has positive growth evidence on processed corncob molasses but soil isolation, while exact 6Ac is described from a wastewater reactor. Distinguish feedstock use, isolation source and anatomical cob association before reclassifying either pair. Resolve the upstream BTO class scope and true relation before a controlled ontology refresh or explicit supported local correction. GOLD-parent exclusions cannot remove this independently imported ontology edge. Proposed work only; no repair or status promotion is performed by this review.

- Regress the exact target claim and preserve valid genera, identifiers, source counts/units and taxon associations. Recover original evidence before deleting a provisional pair; do not decrement frozen totals by hand.
- Record authorized curation history; require schema, strict, provenance, history, label, corpus, site and full QC gates.
- Save an immutable successor with the same issue key and exact predecessor finding identity.

### ACT2

The identity denotes the maize-ear axis/core, not an entire inflorescence. BTO nevertheless imports spike as a superclass; its own spike definition denotes the whole inflorescence, exposing a component/class conflict. The GOLD phyllosphere context is compatible with broad above-ground plant association and is not rejected by treating phyllosphere as only leaves. PREGO retains two score-three taxa: exact XZL9 has positive growth evidence on processed corncob molasses but soil isolation, while exact 6Ac is described from a wastewater reactor. Distinguish feedstock use, isolation source and anatomical cob association before reclassifying either pair. Recover manifest-matching original pair, channel and dictionary/citation provenance. Competing origins, feedstocks and assay contexts are evidence questions, not proof of biological absence or a demonstrated extraction bug. Proposed work only; no repair or status promotion is performed by this review.

- Regress the exact target claim and preserve valid genera, identifiers, source counts/units and taxon associations. Recover original evidence before deleting a provisional pair; do not decrement frozen totals by hand.
- Record authorized curation history; require schema, strict, provenance, history, label, corpus, site and full QC gates.
- Save an immutable successor with the same issue key and exact predecessor finding identity.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/cob.yaml; Entire generated target YAML | supports | All fields, source attestations, displayed taxa, aliases and complete generated history read. |
| ERULE | docs/CURATION.md; Identity, evidence and strictly broader parents | supports | All parent contributions must be strictly broader; source context, anatomy, host and diagnosis are distinct. Optional absence is not a required-field defect. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation and GroundingStatusEnum | supports | The mapping contract compares source concept to record identifier; source-is-record omits the predicate. Native status and association rules are preserved. |
| ESEED | src/habitatmech/seed.py; Executed source routes and entire document reproduction | supports | [{"mint": "habitatmech:GOLD.2ec4ea245f", "automatic": {"identifier": "BTO:0000266", "grounding_status": "EXACT", "mapping_predicate": "skos:exactMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "gold_leaf_label", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "BTO:0000266", "grounding_status": "EXACT", "mapping_predicate": "skos:exactMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "curated_review_of_gold_leaf_label", "category": null, "reviewed": true, "decision": {"identifier": "habitatmech:GOLD.2ec4ea245f", "decision": "REVIEW", "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-13", "notes": "Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date.", "review_depth": "ITEM", "category": "", "relation": "parent"}}}, {"mint": "habitatmech:PREGO.9795ca3c95", "automatic": {"identifier": "BTO:0000266", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "BTO:0000266", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "curated_review_of_prego_self_grounded", "category": null, "reviewed": true, "decision": {"identifier": "habitatmech:PREGO.9795ca3c95", "decision": "REVIEW", "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-13", "notes": "Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date.", "review_depth": "ITEM", "category": "", "relation": "parent"}}}] |
| EEXTRACT | src/habitatmech/extract.py; Source counts, source-strain-taxon join and PREGO scoring/ranking | supports | Inspected native projections. Original BacDive source-strain join and PREGO pair citation evidence are not retained in the compact per-habitat taxon tables. |
| ET5 | data/raw/gold_ecosystem_paths.tsv; Physical TSV rows 2518 | supports | [{"row": 2518, "data": {"canonical_path": "Host-associated &gt; Plants &gt; Phyllosphere &gt; Cob", "ecosystem": "Host-associated", "ecosystem_category": "Plants", "ecosystem_type": "Phyllosphere", "ecosystem_subtype": "Cob", "specific_ecosystem": "", "leaf_label": "Cob", "depth": "4", "gold_node_count": "2", "organism_count": "0", "study_count": "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids": "gold.ecosystem:5739&#124;gold.ecosystem:5740"}}] |
| ET6 | data/raw/prego_habitat_taxa.tsv; Physical TSV rows 376,377 | supports | [{"row": 376, "data": {"prego_id": "BTO:0000266", "rank": "1", "taxon_id": "NCBITaxon:1110509", "taxon_label": "Methanothrix harundinacea 6Ac", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 377, "data": {"prego_id": "BTO:0000266", "rank": "2", "taxon_id": "NCBITaxon:1245026", "taxon_label": "Heyndrickxia coagulans XZL9", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}] |
| ET7 | data/raw/prego_habitats.tsv; Physical TSV rows 470 | supports | [{"row": 470, "data": {"prego_id": "BTO:0000266", "ontology": "BTO", "biolink_category": "biolink:GrossAnatomicalStructure", "taxon_count": "2", "direct_assertion_count": "2", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms": "cob&#124;corn cob&#124;corn cobs&#124;corncob&#124;corncobs&#124;maize cob&#124;maize cobs"}}] |
| ET8 | data/raw/gold_path_biosamples.tsv; Physical TSV rows 1034 | supports | [{"row": 1034, "data": {"canonical_path": "Host-associated &gt; Plants &gt; Phyllosphere &gt; Cob", "ecosystem_path_id": "5740", "biosample_count": "1"}}] |
| ET9 | data/raw/gold_studies.tsv; Physical TSV rows 2106 | supports | [{"row": 2106, "data": {"study_gold_id": "Gs0135140", "path_count": "1", "paths": "Host-associated &gt; Plants &gt; Phyllosphere &gt; Cob"}}] |
| ET10 | data/raw/ontology_subclass_edges.tsv; Physical TSV rows 183,878 | supports | [{"row": 183, "data": {"subject": "BTO:0000266", "predicate": "rdfs:subClassOf", "object": "BTO:0001278"}}, {"row": 878, "data": {"subject": "BTO:0001278", "predicate": "rdfs:subClassOf", "object": "BTO:0000469"}}] |
| ET11 | data/raw/ontology_terms.tsv; Physical TSV rows 268,1279 | supports | [{"row": 268, "data": {"term_id": "BTO:0000266", "ontology": "BTO", "label": "cob", "definition": "The central axis/core of the ear (distal end of the lateral branch/ear shoot) upon which the kernels (caryopses) are borne. The cob is similar to the central spike of the tassel (male inflorescence) in that it produces multiple rows of paired spikelets (polystichous phyllotaxy).", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}, {"row": 1279, "data": {"term_id": "BTO:0001278", "ontology": "BTO", "label": "spike", "definition": "An elongated inflorescence similar to a raceme but having the flowers sessile on the main axis.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}] |
| ET12 | curation/decisions.tsv; Physical TSV rows 368,1493 | supports | [{"row": 368, "data": {"identifier": "habitatmech:GOLD.2ec4ea245f", "decision": "REVIEW", "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-13", "notes": "Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date.", "review_depth": "ITEM", "category": "", "relation": ""}}, {"row": 1493, "data": {"identifier": "habitatmech:PREGO.9795ca3c95", "decision": "REVIEW", "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-13", "notes": "Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date.", "review_depth": "ITEM", "category": "", "relation": ""}}] |
| EP13 | data/habitats/host_associated/spike.yaml; Immediate parent record, context only | supports | {"identifier": "BTO:0001278", "label": "spike", "definition": "An elongated inflorescence similar to a raceme but having the flowers sessile on the main axis.", "definition_source": "BTO", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "EXACT", "mapping_status": "SEEDED", "synonyms": [{"synonym_text": "spikes", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}], "parent_habitats": ["BTO:0000469"], "source_attestations": [{"source": "PREGO", "source_id": "BTO:0001278", "source_label": "spike", "assertion_count": 228, "assertion_unit": "TAXON", "score": 3.0, "evidence_channels": "annotated_genomes_isolates&#124;environmental_samples"}], "characteristic_taxa": [{"taxon_id": "NCBITaxon:11146", "source": "PREGO", "score": 3.0, "rank": 1, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:11149", "source": "PREGO", "score": 3.0, "rank": 2, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:1498172", "source": "PREGO", "score": 3.0, "rank": 3, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:422139", "source": "PREGO", "score": 3.0, "rank": 4, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:422140", "source": "PREGO", "score": 3.0, "rank": 5, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:422141", "source": "PREGO", "score": 3.0, "rank": 6, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:422214", "source": "PREGO", "score": 3.0, "rank": 7, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:422215", "source": "PREGO", "score": 3.0, "rank": 8, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:422217", "source": "PREGO", "score": 3.0, "rank": 9, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:422218", "source": "PREGO", "score": 3.0, "rank": 10, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:422219", "source": "PREGO", "score": 3.0, "rank": 11, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:422220", "source": "PREGO", "score": 3.0, "rank": 12, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:46170", "source": "PREGO", "score": 3.0, "rank": 13, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:930166", "source": "PREGO", "taxon_label": "Pseudomonas brassicacearum", "score": 3.0, "rank": 14, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:948870", "source": "PREGO", "score": 3.0, "rank": 15, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:1107", "source": "PREGO", "taxon_label": "Chloroflexus", "score": 1.38108, "rank": 16, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:1236", "source": "PREGO", "taxon_label": "Gammaproteobacteria", "score": 1.38108, "rank": 17, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:219686", "source": "PREGO", "taxon_label": "Gemmatimonadales", "score": 1.38108, "rank": 18, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:28211", "source": "PREGO", "taxon_label": "Alphaproteobacteria", "score": 1.38108, "rank": 19, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:28216", "source": "PREGO", "taxon_label": "Betaproteobacteria", "score": 1.38108, "rank": 20, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:543", "source": "PREGO", "taxon_label": "Enterobacteriaceae", "score": 1.38108, "rank": 21, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:582", "source": "PREGO", "taxon_label": "Morganella morganii", "score": 1.38108, "rank": 22, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:84642", "source": "PREGO", "taxon_label": "Aeromonadaceae", "score": 1.38108, "rank": 23, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:1030", "source": "PREGO", "taxon_label": "Thiothrix", "score": 1.35163, "rank": 24, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:1386", "source": "PREGO", "taxon_label": "Bacillus &lt;firmicutes&gt;", "score": 1.35163, "rank": 25, "candidate_pool": 228}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by PREGO. Grounding: EXACT."}]} |
| EP14 | data/habitats/host_associated/phyllosphere.yaml; Immediate parent record, context only | supports | {"identifier": "habitatmech:GOLD.7406232b7e", "label": "Phyllosphere", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "UNGROUNDED", "mapping_status": "SEEDED", "parent_habitats": ["ENVO:01001001"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:4458", "source_label": "Phyllosphere", "source_path": "Host-associated &gt; Plants &gt; Phyllosphere", "assertion_count": 149, "assertion_unit": "ORGANISM", "notes": "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp": "2026-08-12T00:00:00Z", "curator": "claude-opus-5", "action": "CONFIRM_UNGROUNDED", "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. [CLASS-level] Class-level sweep (see docs/HARMONIZATION.md#class-level-sweep): no term in the vendored slice matched this label by any search route. Whether the concept is a habitat at all was NOT assessed, so this is not yet a term-request candidate. (source concept habitatmech:GOLD.7406232b7e)"}, {"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED."}]} |
| EX15 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000266/graph; BTO_0000266-graph.json | context_only | Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000266", "target": "http://purl.obolibrary.org/obo/BTO_0001278", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX16 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000266; BTO_0000266.json | context_only | Current identity, active status, definition and typed synonyms: {"obo_id": "BTO:0000266", "label": "cob", "is_obsolete": false, "description": ["Zea mays.", "The central axis/core of the ear (distal end of the lateral branch/ear shoot) upon which the kernels (caryopses) are borne. The cob is similar to the central spike of the tassel (male inflorescence) in that it produces multiple rows of paired spikelets (polystichous phyllotaxy)."], "obo_synonym": null, "annotation": {"has_obo_namespace": ["BrendaTissueOBO"], "id": ["BTO:0000266"]}} |
| EX17 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000469/graph; BTO_0000469-graph.json | context_only | Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000469", "target": "http://purl.obolibrary.org/obo/BTO_0000628", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX18 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000469; BTO_0000469.json | context_only | Current identity, active status, definition and typed synonyms: {"obo_id": "BTO:0000469", "label": "flower", "is_obsolete": false, "description": ["The reproductive structure of the anthophyta or angiosperms."], "obo_synonym": null, "annotation": {"has_obo_namespace": ["BrendaTissueOBO"], "id": ["BTO:0000469"]}} |
| EX19 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001278/graph; BTO_0001278-graph.json | context_only | Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0001278", "target": "http://purl.obolibrary.org/obo/BTO_0000469", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX20 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001278; BTO_0001278.json | context_only | Current identity, active status, definition and typed synonyms: {"obo_id": "BTO:0001278", "label": "spike", "is_obsolete": false, "description": ["An elongated inflorescence similar to a raceme but having the flowers sessile on the main axis."], "obo_synonym": null, "annotation": {"has_obo_namespace": ["BrendaTissueOBO"], "id": ["BTO:0001278"]}} |
| EX21 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001001/graph; ENVO_01001001-graph.json | context_only | Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001001", "target": "http://purl.obolibrary.org/obo/ENVO_01001000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001001", "target": "http://purl.obolibrary.org/obo/NCBITaxon_33090", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX22 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001001; ENVO_01001001.json | context_only | Current identity, active status, definition and typed synonyms: {"obo_id": "ENVO:01001001", "label": "plant-associated environment", "is_obsolete": false, "description": ["An environmental system determined by a green plant."], "obo_synonym": null, "annotation": {"alternative label": ["Plant"]}} |
| EX23 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3349665/fullTextXML; PMC3349665.xml | context_only | PMID:22590603; DOI:10.1371/journal.pone.0036756. Strain origin and genome methods inspected: exact 6Ac came from a UASB reactor treating beer-manufacturing wastewater. This does not prove absence from every cob-related environment or identify the original PREGO pair citation. |
| EX24 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3656213/fullTextXML; PMC3656213.xml | context_only | PMID:23682151; DOI:10.1128/genomeA.00254-13. Exact XZL9 genome announcement abstract and strain-origin paragraph: soil isolate, not direct isolation from maize cob. |
| EX25 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML; PMC8879827.xml | context_only | PMID:35208748; DOI:10.3390/microorganisms10020293. Methods and scoring appendix inspected: channels have different evidence and scoring; score-three BioProject associations can derive from abstract mining. This does not identify the extraction route of any particular retained pair. |
| EX26 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A20627714%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=50; paper-corn-molasses.json | context_only | PMID:20627714; DOI:10.1016/j.biortech.2010.05.031. Primary abstract inspected: exact XZL9 ferments sugars in processed corncob molasses. Positive feedstock use is distinct from living-plant or anatomical-cob localization. |
| EX27 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=102234,1027273,1048357,1069963,1074311,1110509,1117,1120968,1120983,1121027,1150864,1173995,119852,1216969,1224163,1234143,1234144,1245026,1263,1280004,1292046,1297579,1342794,1342818,1348114,1385512,1401264,141693,1449351,1452538,1453497,1479025,1481923,1485,1578,1590,171549,171550,171552,186802,186803,189330,248039,31979,33038,33042,375288,384676,411459,411460,444103,51514,541000,560080,572511,816,830,838,85831,872&amp;retmode=xml; taxonomy.xml | context_only | Current exact TaxId resolutions, including merged IDs and labels: [{"id": "NCBITaxon:1110509", "source": "PREGO", "label": "Methanothrix harundinacea 6Ac", "current_id": "1110509", "current_name": "Methanothrix harundinacea 6Ac", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1245026", "source": "PREGO", "label": "Heyndrickxia coagulans XZL9", "current_id": "1245026", "current_name": "Heyndrickxia coagulans XZL9", "rank": "strain", "direct_match": true, "recognized_alias": true}] |
| ESEARCH | Local source/curation/review corpus; rg --no-ignore --hidden -l -F -e BTO:0000266 -e cob -e cob -e habitatmech:GOLD.2ec4ea245f -e habitatmech:PREGO.9795ca3c95 curation history research reports data/raw build reviews | context_only | Source rows were parsed by exact keys; broad name hits were leads, not all inspected. No formal structured target predecessor. |
| EAVAIL | Configured kg-microbe checkout; find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe -type f '(' -ipath '*prego*' -o -ipath '*bacdive*' ')' | context_only | Search found BacDive notebooks and Git metadata, but no manifest-matching BacDive/PREGO transformed node/edge exports. No claim of global absence. |

## Limits And Additional Notes

- Original specimen-level evidence and every pair-level citation were not exhaustively reconstructed. Source associations, counts, ranks and scores are not prevalence, viability or characteristic presence.
- Configured label validation skips 2063 no-adapter pairs; target TaxIds were separately resolved with current NCBI.
- Exact-base hosted QC covers unchanged scientific inputs, not a new local full-QC execution or these new review files. Each new bundle requires native validation/save and the subsequent archive check.
- iModulonDB is not applicable: no gene, regulator or expression-module claim is asserted. Cited experiments are used only for identity and context, not imported causal mechanisms.
- Original source-strain or PREGO pair exports were unavailable in the configured checkout; no uncertain association is removed or source count rewritten.
- Captured working_tree provenance is retained. All local input hashes were additionally checked against exact base 67cde35918d7361de3a1164fb22756cba5d20e30.
- Read-only review: no source, curation, generated record, status or history edit; no GitHub mutation or paid research.
- Ignored-inclusive structured archive traversal found no previous structured target review. Legacy prose is contextual evidence, not formal predecessor lineage or issue closure.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T035436Z-cob-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: cob (BTO:0000266)'
started_at: '2026-10-16T03:35:20Z'
finished_at: '2026-10-16T03:54:36Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent assessed all evidence and target; not independent
    reviewer approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'The identity denotes the maize-ear axis/core, not an entire inflorescence.
  BTO nevertheless imports spike as a superclass; its own spike definition denotes
  the whole inflorescence, exposing a component/class conflict. The GOLD phyllosphere
  context is compatible with broad above-ground plant association and is not rejected
  by treating phyllosphere as only leaves. PREGO retains two score-three taxa: exact
  XZL9 has positive growth evidence on processed corncob molasses but soil isolation,
  while exact 6Ac is described from a wastewater reactor. Distinguish feedstock use,
  isolation source and anatomical cob association before reclassifying either pair.'
source:
  git_revision: 67cde35918d7361de3a1164fb22756cba5d20e30
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
    sha256: e5cb2e09f72dd4b18e069c0e2576e25e13e56c9991f4eb5ae47416345e247578
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 37dc4b40642d19e7b5c3262f368d12daa82e03115e7731a2326ae88785ceff5b
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 04ba048af6f93b69c127bc3d47e2403dbe153452c75f9e26939188fc5daa52d7
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
  - path: data/habitats/host_associated/cob.yaml
    sha256: efea1f8e2432ec993665ac33bc8de85e6db66491ff561038586ff8f0dbb03dc0
    role: target
  - path: data/habitats/host_associated/phyllosphere.yaml
    sha256: 87a5a16f77734636f96a13c33755a800cc9bb71f4ace3a390c43e79f76ee994d
    role: context
  - path: data/habitats/host_associated/spike.yaml
    sha256: 4141f5956931c7009d44d6d0a858b4a988066da7bb335a1c0b2798c3a4a26433
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
- target_id: BTO:0000266
  path: data/habitats/host_associated/cob.yaml
  label: cob
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
  description: Full field-by-field assessment of this one resolved generated record.
  selection: One of the next 24 unreviewed records selected in deterministic path
    order from the ignored-inclusive 3209-record census. This bundle assesses exactly
    one target, not a proxy sample.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - BTO:0000266
  exclusions:
  - target: Other records, individual source specimens and SSSOM/KGX products
    reason: Parent context is not additional review coverage; original specimens and
      exports are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/cob.yaml
  exit_code: 0
  target_ids:
  - BTO:0000266
  summary: "Finished 2026-10-16T03:35:52Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/cob.yaml"
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/clasper.yaml data/habitats/host_associated/claw.yaml
    data/habitats/host_associated/cloaca.yaml data/habitats/host_associated/cloaca__f527d4ff.yaml
    data/habitats/host_associated/cnidarian_associated_environment.yaml data/habitats/host_associated/cob.yaml
    data/habitats/host_associated/cocoon.yaml data/habitats/host_associated/coelom.yaml
    data/habitats/host_associated/coelom__d65ea80b.yaml data/habitats/host_associated/colon.yaml
    data/habitats/host_associated/colon__a0dd5461.yaml data/habitats/host_associated/colon__ff534087.yaml
    data/habitats/host_associated/colon_cancer.yaml data/habitats/host_associated/colon_mucosa.yaml
    data/habitats/host_associated/colon_mucosa__7a8e4588.yaml data/habitats/host_associated/colon_mucosa__b687aead.yaml
    data/habitats/host_associated/colon_mucosa__de31f03f.yaml data/habitats/host_associated/colonic.yaml
    data/habitats/host_associated/colonic_cancer_cell.yaml data/habitats/host_associated/colonic_epithelium.yaml
    data/habitats/host_associated/colonic_mucosa.yaml data/habitats/host_associated/colorectal_polyps.yaml
    data/habitats/host_associated/colorectum.yaml data/habitats/host_associated/colostrum.yaml
  exit_code: 0
  target_ids:
  - BTO:0000266
  summary: "Finished 2026-10-16T03:36:32Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/clasper.yaml data/habitats/host_associated/claw.yaml\
    \ data/habitats/host_associated/cloaca.yaml data/habitats/host_associated/cloaca__f527d4ff.yaml\
    \ data/habitats/host_associated/cnidarian_associated_environment.yaml data/habitats/host_associated/cob.yaml\
    \ data/habitats/host_associated/cocoon.yaml data/habitats/host_associated/coelom.yaml\
    \ data/habitats/host_associated/coelom__d65ea80b.yaml data/habitats/host_associated/colon.yaml\
    \ data/habitats/host_associated/colon__a0dd5461.yaml data/habitats/host_associated/colon__ff534087.yaml\
    \ data/habitats/host_associated/colon_cancer.yaml data/habitats/host_associated/colon_mucosa.yaml\
    \ data/habitats/host_associated/colon_mucosa__7a8e4588.yaml data/habitats/host_associated/colon_mucosa__b687aead.yaml\
    \ data/habitats/host_associated/colon_mucosa__de31f03f.yaml data/habitats/host_associated/colonic.yaml\
    \ data/habitats/host_associated/colonic_cancer_cell.yaml data/habitats/host_associated/colonic_epithelium.yaml\
    \ data/habitats/host_associated/colonic_mucosa.yaml data/habitats/host_associated/colorectal_polyps.yaml\
    \ data/habitats/host_associated/colorectum.yaml data/habitats/host_associated/colostrum.yaml\n\
    Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      24\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - BTO:0000266
  summary: 'Finished 2026-10-16T03:36:40Z. No issues found

    831 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - BTO:0000266
  summary: "Finished 2026-10-16T03:36:40Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - BTO:0000266
  summary: "Finished 2026-10-16T03:37:54Z. expected 3209 records, found 3209 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - BTO:0000266
  summary: "Finished 2026-10-16T03:38:04Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - BTO:0000266
  summary: "Finished 2026-10-16T03:38:23Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - BTO:0000266
  summary: "Finished 2026-10-16T03:39:05Z. id↔label correspondence summary:\n    \
    \      OK_CANONICAL: 1173\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2063\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: CCI
  name: Exact-base hosted native QC
  status: passed
  required: true
  command: gh run view 38843593114 --repo CultureBotAI/HabitatMech --json headSha,conclusion,url,jobs
  exit_code: 0
  target_ids:
  - BTO:0000266
  summary: Verified 2026-10-16T03:43:47Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38843593114
  scope_note: Unchanged scientific-input base only. Not a claim that the new output
    bundles were part of the earlier run.
- check_id: CPOOL
  name: Displayed candidate-pool correspondence
  status: passed
  required: false
  command: .venv/bin/python /private/tmp/habitatmech-review-cq-author.py pool_check
  exit_code: 0
  target_ids:
  - BTO:0000266
  summary: Finished 2026-10-16T03:54:30Z. All 60 displayed candidate pools equal exact
    source taxon totals.
  scope_note: Supplemental mechanical cross-check of all 60 displayed taxon entries;
    not a replacement for native validators or scientific evidence.
- check_id: CREF
  name: Standalone citation validation applicability
  status: not_applicable
  required: false
  target_ids:
  - BTO:0000266
  summary: No standalone citation checker is documented for these evidence-free generated
    targets. Stable references were checked with native gates and current authorities;
    causal validation ran globally.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/cob.yaml
  locator: Entire generated target YAML
  accessed_at: '2026-10-16T03:54:36Z'
  support: supports
  summary: All fields, source attestations, displayed taxa, aliases and complete generated
    history read.
  snapshot_sha256: efea1f8e2432ec993665ac33bc8de85e6db66491ff561038586ff8f0dbb03dc0
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, evidence and strictly broader parents
  accessed_at: '2026-10-16T03:54:36Z'
  support: supports
  summary: All parent contributions must be strictly broader; source context, anatomy,
    host and diagnosis are distinct. Optional absence is not a required-field defect.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation and GroundingStatusEnum
  accessed_at: '2026-10-16T03:54:36Z'
  support: supports
  summary: The mapping contract compares source concept to record identifier; source-is-record
    omits the predicate. Native status and association rules are preserved.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed source routes and entire document reproduction
  accessed_at: '2026-10-16T03:54:36Z'
  support: supports
  summary: '[{"mint": "habitatmech:GOLD.2ec4ea245f", "automatic": {"identifier": "BTO:0000266",
    "grounding_status": "EXACT", "mapping_predicate": "skos:exactMatch", "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "gold_leaf_label", "category":
    null, "reviewed": false, "decision": null}, "final": {"identifier": "BTO:0000266",
    "grounding_status": "EXACT", "mapping_predicate": "skos:exactMatch", "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "curated_review_of_gold_leaf_label",
    "category": null, "reviewed": true, "decision": {"identifier": "habitatmech:GOLD.2ec4ea245f",
    "decision": "REVIEW", "object_id": "", "object_label": "", "grounding_status":
    "", "curator": "claude-opus-5", "date": "2026-08-13", "notes": "Multi-source review
    pass: this record is attested by more than one independent vocabulary, and this
    source''s label or path was read against the record''s ontology term to check
    the merge is right. It agrees. Source concepts in the same pass whose labels did
    not agree were re-decided rather than endorsed; see the pass''s other decisions
    of the same date.", "review_depth": "ITEM", "category": "", "relation": "parent"}}},
    {"mint": "habitatmech:PREGO.9795ca3c95", "automatic": {"identifier": "BTO:0000266",
    "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded",
    "category": null, "reviewed": false, "decision": null}, "final": {"identifier":
    "BTO:0000266", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "curated_review_of_prego_self_grounded",
    "category": null, "reviewed": true, "decision": {"identifier": "habitatmech:PREGO.9795ca3c95",
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
  locator: Source counts, source-strain-taxon join and PREGO scoring/ranking
  accessed_at: '2026-10-16T03:54:36Z'
  support: supports
  summary: Inspected native projections. Original BacDive source-strain join and PREGO
    pair citation evidence are not retained in the compact per-habitat taxon tables.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Physical TSV rows 2518
  accessed_at: '2026-10-16T03:54:36Z'
  support: supports
  summary: '[{"row": 2518, "data": {"canonical_path": "Host-associated > Plants >
    Phyllosphere > Cob", "ecosystem": "Host-associated", "ecosystem_category": "Plants",
    "ecosystem_type": "Phyllosphere", "ecosystem_subtype": "Cob", "specific_ecosystem":
    "", "leaf_label": "Cob", "depth": "4", "gold_node_count": "2", "organism_count":
    "0", "study_count": "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids":
    "gold.ecosystem:5739|gold.ecosystem:5740"}}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: ET6
  kind: database
  reference: data/raw/prego_habitat_taxa.tsv
  locator: Physical TSV rows 376,377
  accessed_at: '2026-10-16T03:54:36Z'
  support: supports
  summary: '[{"row": 376, "data": {"prego_id": "BTO:0000266", "rank": "1", "taxon_id":
    "NCBITaxon:1110509", "taxon_label": "Methanothrix harundinacea 6Ac", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 377, "data": {"prego_id": "BTO:0000266", "rank": "2", "taxon_id":
    "NCBITaxon:1245026", "taxon_label": "Heyndrickxia coagulans XZL9", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}]'
  snapshot_sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
- evidence_id: ET7
  kind: database
  reference: data/raw/prego_habitats.tsv
  locator: Physical TSV rows 470
  accessed_at: '2026-10-16T03:54:36Z'
  support: supports
  summary: '[{"row": 470, "data": {"prego_id": "BTO:0000266", "ontology": "BTO", "biolink_category":
    "biolink:GrossAnatomicalStructure", "taxon_count": "2", "direct_assertion_count":
    "2", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms":
    "cob|corn cob|corn cobs|corncob|corncobs|maize cob|maize cobs"}}]'
  snapshot_sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
- evidence_id: ET8
  kind: database
  reference: data/raw/gold_path_biosamples.tsv
  locator: Physical TSV rows 1034
  accessed_at: '2026-10-16T03:54:36Z'
  support: supports
  summary: '[{"row": 1034, "data": {"canonical_path": "Host-associated > Plants >
    Phyllosphere > Cob", "ecosystem_path_id": "5740", "biosample_count": "1"}}]'
  snapshot_sha256: 97cd7c8d0e731d07a85db6986dbcf9e49096a3c7988bd90a855599f492fe619e
- evidence_id: ET9
  kind: database
  reference: data/raw/gold_studies.tsv
  locator: Physical TSV rows 2106
  accessed_at: '2026-10-16T03:54:36Z'
  support: supports
  summary: '[{"row": 2106, "data": {"study_gold_id": "Gs0135140", "path_count": "1",
    "paths": "Host-associated > Plants > Phyllosphere > Cob"}}]'
  snapshot_sha256: fa7aaa46f288d10c453bb723e6cf486cde646a003559414b5523cc3883a84c8c
- evidence_id: ET10
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: Physical TSV rows 183,878
  accessed_at: '2026-10-16T03:54:36Z'
  support: supports
  summary: '[{"row": 183, "data": {"subject": "BTO:0000266", "predicate": "rdfs:subClassOf",
    "object": "BTO:0001278"}}, {"row": 878, "data": {"subject": "BTO:0001278", "predicate":
    "rdfs:subClassOf", "object": "BTO:0000469"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET11
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 268,1279
  accessed_at: '2026-10-16T03:54:36Z'
  support: supports
  summary: '[{"row": 268, "data": {"term_id": "BTO:0000266", "ontology": "BTO", "label":
    "cob", "definition": "The central axis/core of the ear (distal end of the lateral
    branch/ear shoot) upon which the kernels (caryopses) are borne. The cob is similar
    to the central spike of the tassel (male inflorescence) in that it produces multiple
    rows of paired spikelets (polystichous phyllotaxy).", "synonyms": "", "deprecated":
    "", "directly_referenced": "TRUE", "label_only": "FALSE"}}, {"row": 1279, "data":
    {"term_id": "BTO:0001278", "ontology": "BTO", "label": "spike", "definition":
    "An elongated inflorescence similar to a raceme but having the flowers sessile
    on the main axis.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE",
    "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: ET12
  kind: database
  reference: curation/decisions.tsv
  locator: Physical TSV rows 368,1493
  accessed_at: '2026-10-16T03:54:36Z'
  support: supports
  summary: '[{"row": 368, "data": {"identifier": "habitatmech:GOLD.2ec4ea245f", "decision":
    "REVIEW", "object_id": "", "object_label": "", "grounding_status": "", "curator":
    "claude-opus-5", "date": "2026-08-13", "notes": "Multi-source review pass: this
    record is attested by more than one independent vocabulary, and this source''s
    label or path was read against the record''s ontology term to check the merge
    is right. It agrees. Source concepts in the same pass whose labels did not agree
    were re-decided rather than endorsed; see the pass''s other decisions of the same
    date.", "review_depth": "ITEM", "category": "", "relation": ""}}, {"row": 1493,
    "data": {"identifier": "habitatmech:PREGO.9795ca3c95", "decision": "REVIEW", "object_id":
    "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date":
    "2026-08-13", "notes": "Multi-source review pass: this record is attested by more
    than one independent vocabulary, and this source''s label or path was read against
    the record''s ontology term to check the merge is right. It agrees. Source concepts
    in the same pass whose labels did not agree were re-decided rather than endorsed;
    see the pass''s other decisions of the same date.", "review_depth": "ITEM", "category":
    "", "relation": ""}}]'
  snapshot_sha256: e5cb2e09f72dd4b18e069c0e2576e25e13e56c9991f4eb5ae47416345e247578
- evidence_id: EP13
  kind: record_content
  reference: data/habitats/host_associated/spike.yaml
  locator: Immediate parent record, context only
  accessed_at: '2026-10-16T03:54:36Z'
  support: supports
  summary: '{"identifier": "BTO:0001278", "label": "spike", "definition": "An elongated
    inflorescence similar to a raceme but having the flowers sessile on the main axis.",
    "definition_source": "BTO", "habitat_category": "HOST_ASSOCIATED", "grounding_status":
    "EXACT", "mapping_status": "SEEDED", "synonyms": [{"synonym_text": "spikes", "synonym_type":
    "RELATED_SYNONYM", "source": "PREGO"}], "parent_habitats": ["BTO:0000469"], "source_attestations":
    [{"source": "PREGO", "source_id": "BTO:0001278", "source_label": "spike", "assertion_count":
    228, "assertion_unit": "TAXON", "score": 3.0, "evidence_channels": "annotated_genomes_isolates|environmental_samples"}],
    "characteristic_taxa": [{"taxon_id": "NCBITaxon:11146", "source": "PREGO", "score":
    3.0, "rank": 1, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:11149", "source":
    "PREGO", "score": 3.0, "rank": 2, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:1498172",
    "source": "PREGO", "score": 3.0, "rank": 3, "candidate_pool": 228}, {"taxon_id":
    "NCBITaxon:422139", "source": "PREGO", "score": 3.0, "rank": 4, "candidate_pool":
    228}, {"taxon_id": "NCBITaxon:422140", "source": "PREGO", "score": 3.0, "rank":
    5, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:422141", "source": "PREGO",
    "score": 3.0, "rank": 6, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:422214",
    "source": "PREGO", "score": 3.0, "rank": 7, "candidate_pool": 228}, {"taxon_id":
    "NCBITaxon:422215", "source": "PREGO", "score": 3.0, "rank": 8, "candidate_pool":
    228}, {"taxon_id": "NCBITaxon:422217", "source": "PREGO", "score": 3.0, "rank":
    9, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:422218", "source": "PREGO",
    "score": 3.0, "rank": 10, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:422219",
    "source": "PREGO", "score": 3.0, "rank": 11, "candidate_pool": 228}, {"taxon_id":
    "NCBITaxon:422220", "source": "PREGO", "score": 3.0, "rank": 12, "candidate_pool":
    228}, {"taxon_id": "NCBITaxon:46170", "source": "PREGO", "score": 3.0, "rank":
    13, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:930166", "source": "PREGO",
    "taxon_label": "Pseudomonas brassicacearum", "score": 3.0, "rank": 14, "candidate_pool":
    228}, {"taxon_id": "NCBITaxon:948870", "source": "PREGO", "score": 3.0, "rank":
    15, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:1107", "source": "PREGO",
    "taxon_label": "Chloroflexus", "score": 1.38108, "rank": 16, "candidate_pool":
    228}, {"taxon_id": "NCBITaxon:1236", "source": "PREGO", "taxon_label": "Gammaproteobacteria",
    "score": 1.38108, "rank": 17, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:219686",
    "source": "PREGO", "taxon_label": "Gemmatimonadales", "score": 1.38108, "rank":
    18, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:28211", "source": "PREGO",
    "taxon_label": "Alphaproteobacteria", "score": 1.38108, "rank": 19, "candidate_pool":
    228}, {"taxon_id": "NCBITaxon:28216", "source": "PREGO", "taxon_label": "Betaproteobacteria",
    "score": 1.38108, "rank": 20, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:543",
    "source": "PREGO", "taxon_label": "Enterobacteriaceae", "score": 1.38108, "rank":
    21, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:582", "source": "PREGO", "taxon_label":
    "Morganella morganii", "score": 1.38108, "rank": 22, "candidate_pool": 228}, {"taxon_id":
    "NCBITaxon:84642", "source": "PREGO", "taxon_label": "Aeromonadaceae", "score":
    1.38108, "rank": 23, "candidate_pool": 228}, {"taxon_id": "NCBITaxon:1030", "source":
    "PREGO", "taxon_label": "Thiothrix", "score": 1.35163, "rank": 24, "candidate_pool":
    228}, {"taxon_id": "NCBITaxon:1386", "source": "PREGO", "taxon_label": "Bacillus
    <firmicutes>", "score": 1.35163, "rank": 25, "candidate_pool": 228}], "curation_history":
    [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action":
    "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested
    by PREGO. Grounding: EXACT."}]}'
  snapshot_sha256: 4141f5956931c7009d44d6d0a858b4a988066da7bb335a1c0b2798c3a4a26433
- evidence_id: EP14
  kind: record_content
  reference: data/habitats/host_associated/phyllosphere.yaml
  locator: Immediate parent record, context only
  accessed_at: '2026-10-16T03:54:36Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.7406232b7e", "label": "Phyllosphere",
    "habitat_category": "HOST_ASSOCIATED", "grounding_status": "UNGROUNDED", "mapping_status":
    "SEEDED", "parent_habitats": ["ENVO:01001001"], "source_attestations": [{"source":
    "GOLD", "source_id": "gold.ecosystem:4458", "source_label": "Phyllosphere", "source_path":
    "Host-associated > Plants > Phyllosphere", "assertion_count": 149, "assertion_unit":
    "ORGANISM", "notes": "3 GOLD ecosystem node ids share this path; first shown.
    See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp":
    "2026-08-12T00:00:00Z", "curator": "claude-opus-5", "action": "CONFIRM_UNGROUNDED",
    "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. [CLASS-level]
    Class-level sweep (see docs/HARMONIZATION.md#class-level-sweep): no term in the
    vendored slice matched this label by any search route. Whether the concept is
    a habitat at all was NOT assessed, so this is not yet a term-request candidate.
    (source concept habitatmech:GOLD.7406232b7e)"}, {"timestamp": "2026-08-16T05:58:02Z",
    "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded
    from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED."}]}'
  snapshot_sha256: 87a5a16f77734636f96a13c33755a800cc9bb71f4ace3a390c43e79f76ee994d
- evidence_id: EX15
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000266/graph
  locator: BTO_0000266-graph.json
  accessed_at: '2026-10-16T03:36:36Z'
  support: context_only
  summary: 'Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000266",
    "target": "http://purl.obolibrary.org/obo/BTO_0001278", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: 7dc116b2e39c5a27b85ea99d2aee68a9de2e582ddb3db9d7ae463ced8e0157a7
- evidence_id: EX16
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000266
  locator: BTO_0000266.json
  accessed_at: '2026-10-16T03:36:36Z'
  support: context_only
  summary: 'Current identity, active status, definition and typed synonyms: {"obo_id":
    "BTO:0000266", "label": "cob", "is_obsolete": false, "description": ["Zea mays.",
    "The central axis/core of the ear (distal end of the lateral branch/ear shoot)
    upon which the kernels (caryopses) are borne. The cob is similar to the central
    spike of the tassel (male inflorescence) in that it produces multiple rows of
    paired spikelets (polystichous phyllotaxy)."], "obo_synonym": null, "annotation":
    {"has_obo_namespace": ["BrendaTissueOBO"], "id": ["BTO:0000266"]}}'
  snapshot_sha256: 56a0e36840a57922d6cb662109505a649e06b12e9997b6f3138f274a0e01fb52
- evidence_id: EX17
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000469/graph
  locator: BTO_0000469-graph.json
  accessed_at: '2026-10-16T03:36:42Z'
  support: context_only
  summary: 'Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000469",
    "target": "http://purl.obolibrary.org/obo/BTO_0000628", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: e1a6101a25b1e923369572698f9f451cfaa64be546890cee391c32cc8bd06df7
- evidence_id: EX18
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000469
  locator: BTO_0000469.json
  accessed_at: '2026-10-16T03:36:41Z'
  support: context_only
  summary: 'Current identity, active status, definition and typed synonyms: {"obo_id":
    "BTO:0000469", "label": "flower", "is_obsolete": false, "description": ["The reproductive
    structure of the anthophyta or angiosperms."], "obo_synonym": null, "annotation":
    {"has_obo_namespace": ["BrendaTissueOBO"], "id": ["BTO:0000469"]}}'
  snapshot_sha256: 6fe64c06acaf068b5a66a4794255c2798b590f10c3392a3e62a495ccf7bd1070
- evidence_id: EX19
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001278/graph
  locator: BTO_0001278-graph.json
  accessed_at: '2026-10-16T03:36:49Z'
  support: context_only
  summary: 'Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0001278",
    "target": "http://purl.obolibrary.org/obo/BTO_0000469", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: 684274716091005cd0253038a29e5d27c5fd9fe38dee07daffd4533a6fa2ed0e
- evidence_id: EX20
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001278
  locator: BTO_0001278.json
  accessed_at: '2026-10-16T03:36:48Z'
  support: context_only
  summary: 'Current identity, active status, definition and typed synonyms: {"obo_id":
    "BTO:0001278", "label": "spike", "is_obsolete": false, "description": ["An elongated
    inflorescence similar to a raceme but having the flowers sessile on the main axis."],
    "obo_synonym": null, "annotation": {"has_obo_namespace": ["BrendaTissueOBO"],
    "id": ["BTO:0001278"]}}'
  snapshot_sha256: 9c4035cb1a49fcba7ea9f2d42b80451957027e970ab0df6e9a50665e79e815aa
- evidence_id: EX21
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001001/graph
  locator: ENVO_01001001-graph.json
  accessed_at: '2026-10-16T03:37:05Z'
  support: context_only
  summary: 'Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001001",
    "target": "http://purl.obolibrary.org/obo/ENVO_01001000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001001",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_33090", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 43b7f7cee8e27c64685cea0193012a2cc71851b91d19a2a7052fa1e6548a6a71
- evidence_id: EX22
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001001
  locator: ENVO_01001001.json
  accessed_at: '2026-10-16T03:37:04Z'
  support: context_only
  summary: 'Current identity, active status, definition and typed synonyms: {"obo_id":
    "ENVO:01001001", "label": "plant-associated environment", "is_obsolete": false,
    "description": ["An environmental system determined by a green plant."], "obo_synonym":
    null, "annotation": {"alternative label": ["Plant"]}}'
  snapshot_sha256: b1623e2f33257c2fadc5bf06670bcc7e95384c210301e901f7faa8059c5ed815
- evidence_id: EX23
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3349665/fullTextXML
  locator: PMC3349665.xml
  accessed_at: '2026-10-16T03:46:24Z'
  support: context_only
  summary: 'PMID:22590603; DOI:10.1371/journal.pone.0036756. Strain origin and genome
    methods inspected: exact 6Ac came from a UASB reactor treating beer-manufacturing
    wastewater. This does not prove absence from every cob-related environment or
    identify the original PREGO pair citation.'
  snapshot_sha256: 2999566bed8b3644c5ad1a0ab19f3c5f050ee0626f7b78e289c165e665d89087
- evidence_id: EX24
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3656213/fullTextXML
  locator: PMC3656213.xml
  accessed_at: '2026-10-16T03:52:51Z'
  support: context_only
  summary: 'PMID:23682151; DOI:10.1128/genomeA.00254-13. Exact XZL9 genome announcement
    abstract and strain-origin paragraph: soil isolate, not direct isolation from
    maize cob.'
  snapshot_sha256: e3bb415802bc9e4f5c9dbcf08c1d21599a55422fd5ce9e2136bbb670e087c862
- evidence_id: EX25
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML
  locator: PMC8879827.xml
  accessed_at: '2026-10-16T03:52:56Z'
  support: context_only
  summary: 'PMID:35208748; DOI:10.3390/microorganisms10020293. Methods and scoring
    appendix inspected: channels have different evidence and scoring; score-three
    BioProject associations can derive from abstract mining. This does not identify
    the extraction route of any particular retained pair.'
  snapshot_sha256: 375f0fde4d07bb823cb9106aa4567bc0ef03c2866af0b2a7740b543f50687c25
- evidence_id: EX26
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A20627714%20AND%20SRC%3AMED&format=json&resultType=core&pageSize=50
  locator: paper-corn-molasses.json
  accessed_at: '2026-10-16T03:46:36Z'
  support: context_only
  summary: 'PMID:20627714; DOI:10.1016/j.biortech.2010.05.031. Primary abstract inspected:
    exact XZL9 ferments sugars in processed corncob molasses. Positive feedstock use
    is distinct from living-plant or anatomical-cob localization.'
  snapshot_sha256: 14756fe7efd76a95a0600d753572260e0e9dfb9500e0c0aabc2eef1927accc5d
- evidence_id: EX27
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=102234,1027273,1048357,1069963,1074311,1110509,1117,1120968,1120983,1121027,1150864,1173995,119852,1216969,1224163,1234143,1234144,1245026,1263,1280004,1292046,1297579,1342794,1342818,1348114,1385512,1401264,141693,1449351,1452538,1453497,1479025,1481923,1485,1578,1590,171549,171550,171552,186802,186803,189330,248039,31979,33038,33042,375288,384676,411459,411460,444103,51514,541000,560080,572511,816,830,838,85831,872&retmode=xml
  locator: taxonomy.xml
  accessed_at: '2026-10-16T03:37:40Z'
  support: context_only
  summary: 'Current exact TaxId resolutions, including merged IDs and labels: [{"id":
    "NCBITaxon:1110509", "source": "PREGO", "label": "Methanothrix harundinacea 6Ac",
    "current_id": "1110509", "current_name": "Methanothrix harundinacea 6Ac", "rank":
    "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1245026",
    "source": "PREGO", "label": "Heyndrickxia coagulans XZL9", "current_id": "1245026",
    "current_name": "Heyndrickxia coagulans XZL9", "rank": "strain", "direct_match":
    true, "recognized_alias": true}]'
  snapshot_sha256: 8cc30a816c5940897a93cd10094f921f070f1378c3dab63db865fd736db4f15b
- evidence_id: ESEARCH
  kind: search
  reference: Local source/curation/review corpus
  locator: rg --no-ignore --hidden -l -F -e BTO:0000266 -e cob -e cob -e habitatmech:GOLD.2ec4ea245f
    -e habitatmech:PREGO.9795ca3c95 curation history research reports data/raw build
    reviews
  accessed_at: '2026-10-16T03:36:40Z'
  support: context_only
  summary: Source rows were parsed by exact keys; broad name hits were leads, not
    all inspected. No formal structured target predecessor.
  search_scope: curation, history, research, reports, data/raw, build and reviews
    including hidden/ignored files; structured YAML archive parsed independently of
    gitignore.
- evidence_id: EAVAIL
  kind: search
  reference: Configured kg-microbe checkout
  locator: find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe
    -type f '(' -ipath '*prego*' -o -ipath '*bacdive*' ')'
  accessed_at: '2026-10-16T03:46:37Z'
  support: context_only
  summary: Search found BacDive notebooks and Git metadata, but no manifest-matching
    BacDive/PREGO transformed node/edge exports. No claim of global absence.
  search_scope: find across the configured checkout, including hidden and ignored
    files.
assessments:
- assessment_id: A1
  area: identity
  topic: Identity, grounding, aliases and strictly broader hierarchy
  outcome: concern
  summary: 'The identity denotes the maize-ear axis/core, not an entire inflorescence.
    BTO nevertheless imports spike as a superclass; its own spike definition denotes
    the whole inflorescence, exposing a component/class conflict. The GOLD phyllosphere
    context is compatible with broad above-ground plant association and is not rejected
    by treating phyllosphere as only leaves. PREGO retains two score-three taxa: exact
    XZL9 has positive growth evidence on processed corncob molasses but soil isolation,
    while exact 6Ac is described from a wastewater reactor. Distinguish feedstock
    use, isolation source and anatomical cob association before reclassifying either
    pair.'
  target_ids:
  - BTO:0000266
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EEXTRACT
  - ET5
  - ET6
  - ET7
  - ET8
  - ET9
  - ET10
  - ET11
  - ET12
  - EP13
  - EP14
  - EX15
  - EX16
  - EX17
  - EX18
  - EX19
  - EX20
  - EX21
  - EX22
  - EX23
  - EX24
  - EX25
  - EX26
  - EX27
- assessment_id: A2
  area: quantity
  topic: Native source units, ranks, scores and candidate pools
  outcome: supported
  summary: 'Exact source rows reproduce every emitted count/unit and displayed taxon
    rank/score/pool. Zero tree counts are omitted; supplemental biosamples, study
    memberships and triads are nonadditive. {"assertions": [{"source": "GOLD", "count":
    0, "unit": "ORGANISM", "row": {"row": 2518, "data": {"canonical_path": "Host-associated
    > Plants > Phyllosphere > Cob", "ecosystem": "Host-associated", "ecosystem_category":
    "Plants", "ecosystem_type": "Phyllosphere", "ecosystem_subtype": "Cob", "specific_ecosystem":
    "", "leaf_label": "Cob", "depth": "4", "gold_node_count": "2", "organism_count":
    "0", "study_count": "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids":
    "gold.ecosystem:5739|gold.ecosystem:5740"}}}, {"source": "PREGO", "count": 2,
    "unit": "TAXON", "row": {"row": 470, "data": {"prego_id": "BTO:0000266", "ontology":
    "BTO", "biolink_category": "biolink:GrossAnatomicalStructure", "taxon_count":
    "2", "direct_assertion_count": "2", "max_prego_score": "3", "channels": "annotated_genomes_isolates",
    "prego_synonyms": "cob|corn cob|corn cobs|corncob|corncobs|maize cob|maize cobs"}}}],
    "taxa": [{"id": "NCBITaxon:1110509", "source": "PREGO", "label": "Methanothrix
    harundinacea 6Ac", "current_id": "1110509", "current_name": "Methanothrix harundinacea
    6Ac", "rank": "strain", "direct_match": true, "recognized_alias": true, "other_names":
    ["Methanosaeta harundinacea 6Ac", "Methanosaeta sp. 6Ac"], "source_row": {"row":
    376, "data": {"prego_id": "BTO:0000266", "rank": "1", "taxon_id": "NCBITaxon:1110509",
    "taxon_label": "Methanothrix harundinacea 6Ac", "prego_score": "3", "direct_flag":
    "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}}, {"id":
    "NCBITaxon:1245026", "source": "PREGO", "label": "Heyndrickxia coagulans XZL9",
    "current_id": "1245026", "current_name": "Heyndrickxia coagulans XZL9", "rank":
    "strain", "direct_match": true, "recognized_alias": true, "other_names": ["Bacillus
    coagulans XZL9", "Weizmannia coagulans XZL9"], "source_row": {"row": 377, "data":
    {"prego_id": "BTO:0000266", "rank": "2", "taxon_id": "NCBITaxon:1245026", "taxon_label":
    "Heyndrickxia coagulans XZL9", "prego_score": "3", "direct_flag": "TRUE", "channels":
    "annotated_genomes_isolates", "corroborated_by": ""}}}]}'
  target_ids:
  - BTO:0000266
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EEXTRACT
  - ET5
  - ET6
  - ET7
  - ET8
  - ET9
  - ET10
  - ET11
  - ET12
  - EP13
  - EP14
  - EX15
  - EX16
  - EX17
  - EX18
  - EX19
  - EX20
  - EX21
  - EX22
  - EX23
  - EX24
  - EX25
  - EX26
  - EX27
- assessment_id: A3
  area: evidence
  topic: Association evidence and claim scope
  outcome: concern
  summary: 'Current ontology/TaxId identities and source attestations were verified.
    The identity denotes the maize-ear axis/core, not an entire inflorescence. BTO
    nevertheless imports spike as a superclass; its own spike definition denotes the
    whole inflorescence, exposing a component/class conflict. The GOLD phyllosphere
    context is compatible with broad above-ground plant association and is not rejected
    by treating phyllosphere as only leaves. PREGO retains two score-three taxa: exact
    XZL9 has positive growth evidence on processed corncob molasses but soil isolation,
    while exact 6Ac is described from a wastewater reactor. Distinguish feedstock
    use, isolation source and anatomical cob association before reclassifying either
    pair. Individual papers support only the stated scope; original source pairs were
    not exhaustively reconstructed.'
  target_ids:
  - BTO:0000266
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EEXTRACT
  - ET5
  - ET6
  - ET7
  - ET8
  - ET9
  - ET10
  - ET11
  - ET12
  - EP13
  - EP14
  - EX15
  - EX16
  - EX17
  - EX18
  - EX19
  - EX20
  - EX21
  - EX22
  - EX23
  - EX24
  - EX25
  - EX26
  - EX27
- assessment_id: A4
  area: completeness
  topic: Native lifecycle, optional content and mechanism limits
  outcome: supported
  summary: Executed native routes reproduce EXACT/REVIEWED. Required content is present.
    No optional environmental parameters, causal graph, discussion, dataset or characteristic-presence
    claim is fabricated. Missing ITEM status alone is not a defect; no status or history
    promotion is performed.
  target_ids:
  - BTO:0000266
  evidence_ids:
  - E1
  - ESCHEMA
  - ESEED
- assessment_id: A5
  area: schema
  topic: Native validation and reproducibility
  outcome: supported
  summary: '31 baseline commands passed: target schema, cohort strict, 831 histories,
    source provenance, exact 3209-record reproduction, 32 causal overlays, 110 term
    requests and configured labels. Exact-base hosted QC passed. Deterministic validity
    is not scientific approval.'
  target_ids:
  - BTO:0000266
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
findings:
- finding_id: F1
  issue_key: cob-ontology-parent-scope
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Imported ontology parent conflicts with the class definition
  description: 'The identity denotes the maize-ear axis/core, not an entire inflorescence.
    BTO nevertheless imports spike as a superclass; its own spike definition denotes
    the whole inflorescence, exposing a component/class conflict. The GOLD phyllosphere
    context is compatible with broad above-ground plant association and is not rejected
    by treating phyllosphere as only leaves. PREGO retains two score-three taxa: exact
    XZL9 has positive growth evidence on processed corncob molasses but soil isolation,
    while exact 6Ac is described from a wastewater reactor. Distinguish feedstock
    use, isolation source and anatomical cob association before reclassifying either
    pair. Resolve the upstream BTO class scope and true relation before a controlled
    ontology refresh or explicit supported local correction. GOLD-parent exclusions
    cannot remove this independently imported ontology edge.'
  target_ids:
  - BTO:0000266
  field_paths:
  - definition
  - parent_habitats
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EEXTRACT
  - ET5
  - ET6
  - ET7
  - ET8
  - ET9
  - ET10
  - ET11
  - ET12
  - EP13
  - EP14
  - EX15
  - EX16
  - EX17
  - EX18
  - EX19
  - EX20
  - EX21
  - EX22
  - EX23
  - EX24
  - EX25
  - EX26
  - EX27
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator; never hand-edit generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never hand-edit generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never hand-edit generated habitat YAML
  rule_id: docs/CURATION.md and native field-by-field review checklist
  native_severity: major
  normalization_reason: Material hierarchy, grounding, representation or pair-evidence
    mismatch. Source reproduction alone does not establish scientific support.
  external_issues: []
- finding_id: F2
  issue_key: cob-prego-pair-evidence
  category: evidence
  severity: major
  status: open
  certainty: provisional
  title: Recover original pair evidence before interpreting localization
  description: 'The identity denotes the maize-ear axis/core, not an entire inflorescence.
    BTO nevertheless imports spike as a superclass; its own spike definition denotes
    the whole inflorescence, exposing a component/class conflict. The GOLD phyllosphere
    context is compatible with broad above-ground plant association and is not rejected
    by treating phyllosphere as only leaves. PREGO retains two score-three taxa: exact
    XZL9 has positive growth evidence on processed corncob molasses but soil isolation,
    while exact 6Ac is described from a wastewater reactor. Distinguish feedstock
    use, isolation source and anatomical cob association before reclassifying either
    pair. Recover manifest-matching original pair, channel and dictionary/citation
    provenance. Competing origins, feedstocks and assay contexts are evidence questions,
    not proof of biological absence or a demonstrated extraction bug.'
  target_ids:
  - BTO:0000266
  field_paths:
  - characteristic_taxa
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EEXTRACT
  - ET5
  - ET6
  - ET7
  - ET8
  - ET9
  - ET10
  - ET11
  - ET12
  - EP13
  - EP14
  - EX15
  - EX16
  - EX17
  - EX18
  - EX19
  - EX20
  - EX21
  - EX22
  - EX23
  - EX24
  - EX25
  - EX26
  - EX27
  - EAVAIL
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator; never hand-edit generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/MANIFEST.yaml
    role: Maintained input or generator; never hand-edit generated habitat YAML
  rule_id: docs/CURATION.md and native field-by-field review checklist
  native_severity: major
  normalization_reason: Material hierarchy, grounding, representation or pair-evidence
    mismatch. Source reproduction alone does not establish scientific support.
  external_issues: []
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - BTO:0000266
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator; never hand-edit generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never hand-edit generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never hand-edit generated habitat YAML
  description: 'The identity denotes the maize-ear axis/core, not an entire inflorescence.
    BTO nevertheless imports spike as a superclass; its own spike definition denotes
    the whole inflorescence, exposing a component/class conflict. The GOLD phyllosphere
    context is compatible with broad above-ground plant association and is not rejected
    by treating phyllosphere as only leaves. PREGO retains two score-three taxa: exact
    XZL9 has positive growth evidence on processed corncob molasses but soil isolation,
    while exact 6Ac is described from a wastewater reactor. Distinguish feedstock
    use, isolation source and anatomical cob association before reclassifying either
    pair. Resolve the upstream BTO class scope and true relation before a controlled
    ontology refresh or explicit supported local correction. GOLD-parent exclusions
    cannot remove this independently imported ontology edge. Proposed work only; no
    repair or status promotion is performed by this review.'
  generator: Controlled source/input correction, just seed, inspected just seed-canary,
    guarded just seed-apply, and dependent term-request/map/site/redirect regeneration
    where required.
  acceptance_checks:
  - Regress the exact target claim and preserve valid genera, identifiers, source
    counts/units and taxon associations. Recover original evidence before deleting
    a provisional pair; do not decrement frozen totals by hand.
  - Record authorized curation history; require schema, strict, provenance, history,
    label, corpus, site and full QC gates.
  - Save an immutable successor with the same issue key and exact predecessor finding
    identity.
- action_id: ACT2
  finding_ids:
  - F2
  target_ids:
  - BTO:0000266
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator; never hand-edit generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/MANIFEST.yaml
    role: Maintained input or generator; never hand-edit generated habitat YAML
  description: 'The identity denotes the maize-ear axis/core, not an entire inflorescence.
    BTO nevertheless imports spike as a superclass; its own spike definition denotes
    the whole inflorescence, exposing a component/class conflict. The GOLD phyllosphere
    context is compatible with broad above-ground plant association and is not rejected
    by treating phyllosphere as only leaves. PREGO retains two score-three taxa: exact
    XZL9 has positive growth evidence on processed corncob molasses but soil isolation,
    while exact 6Ac is described from a wastewater reactor. Distinguish feedstock
    use, isolation source and anatomical cob association before reclassifying either
    pair. Recover manifest-matching original pair, channel and dictionary/citation
    provenance. Competing origins, feedstocks and assay contexts are evidence questions,
    not proof of biological absence or a demonstrated extraction bug. Proposed work
    only; no repair or status promotion is performed by this review.'
  generator: Controlled source/input correction, just seed, inspected just seed-canary,
    guarded just seed-apply, and dependent term-request/map/site/redirect regeneration
    where required.
  acceptance_checks:
  - Regress the exact target claim and preserve valid genera, identifiers, source
    counts/units and taxon associations. Recover original evidence before deleting
    a provisional pair; do not decrement frozen totals by hand.
  - Record authorized curation history; require schema, strict, provenance, history,
    label, corpus, site and full QC gates.
  - Save an immutable successor with the same issue key and exact predecessor finding
    identity.
limitations:
- Original specimen-level evidence and every pair-level citation were not exhaustively
  reconstructed. Source associations, counts, ranks and scores are not prevalence,
  viability or characteristic presence.
- Configured label validation skips 2063 no-adapter pairs; target TaxIds were separately
  resolved with current NCBI.
- Exact-base hosted QC covers unchanged scientific inputs, not a new local full-QC
  execution or these new review files. Each new bundle requires native validation/save
  and the subsequent archive check.
- 'iModulonDB is not applicable: no gene, regulator or expression-module claim is
  asserted. Cited experiments are used only for identity and context, not imported
  causal mechanisms.'
- Original source-strain or PREGO pair exports were unavailable in the configured
  checkout; no uncertain association is removed or source count rewritten.
notes:
- Captured working_tree provenance is retained. All local input hashes were additionally
  checked against exact base 67cde35918d7361de3a1164fb22756cba5d20e30.
- 'Read-only review: no source, curation, generated record, status or history edit;
  no GitHub mutation or paid research.'
- Ignored-inclusive structured archive traversal found no previous structured target
  review. Legacy prose is contextual evidence, not formal predecessor lineage or issue
  closure.
tags:
- individual-scientific-review
- host-associated
```
