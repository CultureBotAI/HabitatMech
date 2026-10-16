# Record review: cephalothorax (BTO:0001906)

- Review: 20261015T235747Z-cephalothorax-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T23:40:17Z
- Finished UTC: 2026-10-15T23:57:47Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

BTO cephalothorax denotes united head and thorax, coherent with the crustacean source. Current BTO itself asserts head and thorax as subclass parents; this is not an importer conversion of part_of edges. The independent GOLD whole-Body superclass is unsupported. Remove only that source contribution, preserving the ontology-owned parents and zero-count semantics.

## Scope And Provenance

Full field-by-field scientific assessment of this exact generated target at 0eb609a7ddb34925067116af806e26c165e10678.

Selection: Stale cecum individual observation plus the next 23 identifiers lacking completed individual-kind reviews in the ignored-inclusive 3209-record census. This bundle assesses one resolved record; previous batch reviews remain valid history.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 0eb609a7ddb34925067116af806e26c165e10678.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0001906 | data/habitats/host_associated/cephalothorax.yaml | generated | cephalothorax |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0001906 | Finished 2026-10-15T23:45:06Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/cephalothorax.yaml |
| validate-strict | passed | True | BTO:0001906 | Finished 2026-10-15T23:45:51Z. uv run python scripts/validate_strict.py data/habitats/host_associated/cecum.yaml data/habitats/host_associated/cardiac_stomach.yaml data/habitats/host_associated/cecum__d677e5d7.yaml data/habitats/host_associated/cecum_intestinal_cecum.yaml data/habitats/host_associated/cecum_mucosa.yaml data/habitats/host_associated/cell_culture.yaml data/habitats/host_associated/cell_line.yaml data/habitats/host_associated/cell_line__59b8224e.yaml data/habitats/host_associated/cell_line__d7fc8c60.yaml data/habitats/host_associated/cellulitis.yaml data/habitats/host_associated/central_nervous_system.yaml data/habitats/host_associated/cephalochordata.yaml data/habitats/host_associated/cephalothorax.yaml data/habitats/host_associated/cerebellum.yaml data/habitats/host_associated/cerebrospinal_fluid.yaml data/habitats/host_associated/cerebrospinal_fluid__93998265.yaml data/habitats/host_associated/cerebrospinal_fluid__b2fc1889.yaml data/habitats/host_associated/cerebrospinal_fluid__e3d236b3.yaml data/habitats/host_associated/cerebrospinal_fluid__f9e9497c.yaml data/habitats/host_associated/ceros.yaml data/habitats/host_associated/cerumen.yaml data/habitats/host_associated/cerumen_gland.yaml data/habitats/host_associated/cervical.yaml data/habitats/host_associated/cervical_adenocarcinoma_cell.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | BTO:0001906 | Finished 2026-10-15T23:46:04Z. No issues found<br>829 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | BTO:0001906 | Finished 2026-10-15T23:46:05Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | BTO:0001906 | Finished 2026-10-15T23:46:28Z. expected 3209 records, found 3209 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | BTO:0001906 | Finished 2026-10-15T23:46:34Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | BTO:0001906 | Finished 2026-10-15T23:46:59Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | BTO:0001906 | Finished 2026-10-15T23:48:03Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1173<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2063<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-baseline native QC | passed | True | BTO:0001906 | Verified 2026-10-15T23:55:08Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38822113212 |
| Standalone evidence-reference validator applicability | not_applicable | False | BTO:0001906 | No standalone citation/reference validator is documented for these evidence-free generated records. Target EvidenceItems and causal edges are absent. Stable source and ontology/taxon references were checked manually and with documented native gates; current-decision primary citations were separately verified where present. |

## Scientific And Domain Assessments

### Identity, definition, category, aliases and hierarchy

identity: concern. Targets: BTO:0001906.

BTO cephalothorax denotes united head and thorax, coherent with the crustacean source. Current BTO itself asserts head and thorax as subclass parents; this is not an importer conversion of part_of edges. The independent GOLD whole-Body superclass is unsupported. Remove only that source contribution, preserving the ontology-owned parents and zero-count semantics.

### Source assertions, pools, ranks and supplementary context

quantity: supported. Targets: BTO:0001906.

All emitted counts/units, labels, ranks, scores and candidate pools match exact frozen rows. [{"source": "GOLD", "count": 0, "unit": "ORGANISM"}]. Zero tree counts are omitted; later biosamples and study memberships are not added. Current taxonomy resolves displayed identifiers including explicit aliases.

### Biological support and bounded source uncertainty

evidence: supported. Targets: BTO:0001906.

BTO cephalothorax denotes united head and thorax, coherent with the crustacean source. Current BTO itself asserts head and thorax as subclass parents; this is not an importer conversion of part_of edges. The independent GOLD whole-Body superclass is unsupported. Remove only that source contribution, preserving the ontology-owned parents and zero-count semantics.

### Native status, optional parameters and causal mechanisms

completeness: supported. Targets: BTO:0001906.

Executed native resolution reproduces EXACT/SEEDED. No environmental parameters, causal graphs, discussions, datasets or is_characteristic=true claims are present. Missing optional fields and SEEDED status alone are not defects; parent mechanisms are not inherited.

### Native validation and reproduction

schema: supported. Targets: BTO:0001906.

Target schema/strict checks, 829 histories, source provenance, exact 3209-record reproduction, 32 causal overlays, 110 term requests and configured label checks passed. Exact-base remote full QC passed. Deterministic validity is separate from scientific support; reference-check applicability is stated explicitly.

## Findings

### F1: Source context is not a supported broader habitat class

major / open / confirmed; issue key: cephalothorax-context-parent.

BTO cephalothorax denotes united head and thorax, coherent with the crustacean source. Current BTO itself asserts head and thorax as subclass parents; this is not an importer conversion of part_of edges. The independent GOLD whole-Body superclass is unsupported. Remove only that source contribution, preserving the ontology-owned parents and zero-count semantics. Suppress only source-path/expected-parent guarded GOLD contribution habitatmech:GOLD.bd9662fadb; retain valid independent genera and all raw provenance.

## Recommended Actions And Acceptance Checks

### ACT1

BTO cephalothorax denotes united head and thorax, coherent with the crustacean source. Current BTO itself asserts head and thorax as subclass parents; this is not an importer conversion of part_of edges. The independent GOLD whole-Body superclass is unsupported. Remove only that source contribution, preserving the ontology-owned parents and zero-count semantics. Suppress only source-path/expected-parent guarded GOLD contribution habitatmech:GOLD.bd9662fadb; retain valid independent genera and all raw provenance. No repair is performed by this review.

- Regress the exact claim, preserving independent valid genera, raw provenance and source counts/units. Change native status or mappings only when supported by the authorized ITEM assessment; never decrement source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/cephalothorax.yaml; Entire target YAML | supports | All fields, attestations, taxa and generated history read. |
| ERULE | docs/CURATION.md; Identity, strict broader hierarchy and evidence rules | supports | Organism, disease, material and habitat identities remain distinct. Parents must be strictly broader, not merely containing sites. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; HabitatRecord, SourceAttestation and TaxonAssociation | supports | Mapping predicate endpoint is source-to-record; source association is weaker than characteristic presence. Optional fields and native review status have distinct contracts. |
| ESEED | src/habitatmech/seed.py; Executed native source routes and complete document reproduction | supports | [{"mint": "habitatmech:GOLD.60a0f24d46", "automatic": {"identifier": "BTO:0001906", "grounding_status": "EXACT", "mapping_predicate": "skos:exactMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "gold_leaf_label", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "BTO:0001906", "grounding_status": "EXACT", "mapping_predicate": "skos:exactMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "gold_leaf_label", "category": null, "reviewed": false, "decision": null}}] |
| EEXTRACT | src/habitatmech/extract.py; Source counts, channels and taxon ranking | supports | Exact frozen rows reproduce counts/units and ranked taxon scores. The committed projection does not retain original PREGO pair citation links. |
| ET5 | data/raw/gold_ecosystem_paths.tsv; Physical TSV rows 1787 | supports | [{"row": 1787, "data": {"canonical_path": "Host-associated &gt; Arthropoda: Crustaceans &gt; Whole body &gt; Cephalothorax", "ecosystem": "Host-associated", "ecosystem_category": "Arthropoda: Crustaceans", "ecosystem_type": "Whole body", "ecosystem_subtype": "Cephalothorax", "specific_ecosystem": "", "leaf_label": "Cephalothorax", "depth": "4", "gold_node_count": "2", "organism_count": "0", "study_count": "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids": "gold.ecosystem:7310&#124;gold.ecosystem:7311"}}] |
| ET6 | data/raw/ontology_subclass_edges.tsv; Physical TSV rows 1284,1285 | supports | [{"row": 1284, "data": {"subject": "BTO:0001906", "predicate": "rdfs:subClassOf", "object": "BTO:0000282"}}, {"row": 1285, "data": {"subject": "BTO:0001906", "predicate": "rdfs:subClassOf", "object": "BTO:0001368"}}] |
| ET7 | data/raw/ontology_terms.tsv; Physical TSV rows 284,1369,1906 | supports | [{"row": 284, "data": {"term_id": "BTO:0000282", "ontology": "BTO", "label": "head", "definition": "The upper or anterior division of the animal body that contains the brain, the chief sense organs, and the mouth.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}, {"row": 1369, "data": {"term_id": "BTO:0001368", "ontology": "BTO", "label": "thorax", "definition": "1: The part of the mammalian body between the neck and the abdomen; also: its cavity in which the heart and lungs lie. 2: The middle of the three chief divisions of the body of an insect; also: the corresponding part of a crustacean or an arachnid.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}, {"row": 1906, "data": {"term_id": "BTO:0001906", "ontology": "BTO", "label": "cephalothorax", "definition": "The united head and thorax of an arachnid or higher crustacean.", "synonyms": "", "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}}] |
| EP8 | data/habitats/host_associated/head.yaml; Full immediate-parent record; context only | supports | {"identifier": "BTO:0000282", "label": "head", "definition": "The upper or anterior division of the animal body that contains the brain, the chief sense organs, and the mouth.", "definition_source": "BTO", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "EXACT", "mapping_status": "SEEDED", "source_attestations": [{"source": "PREGO", "source_id": "BTO:0000282", "source_label": "head", "assertion_count": 48, "assertion_unit": "TAXON", "score": 4.0, "evidence_channels": "environmental_samples"}], "characteristic_taxa": [{"taxon_id": "NCBITaxon:102234", "source": "PREGO", "taxon_label": "Cyanobacterium", "score": 4.0, "rank": 1, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:1117", "source": "PREGO", "taxon_label": "Cyanobacteriota", "score": 4.0, "rank": 2, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:117563", "source": "PREGO", "taxon_label": "Granulicatella", "score": 4.0, "rank": 3, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:1279", "source": "PREGO", "taxon_label": "Staphylococcus", "score": 4.0, "rank": 4, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:1301", "source": "PREGO", "taxon_label": "Streptococcus", "score": 4.0, "rank": 5, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:1716", "source": "PREGO", "taxon_label": "Corynebacterium", "score": 4.0, "rank": 6, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:32008", "source": "PREGO", "taxon_label": "Burkholderia", "score": 4.0, "rank": 7, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:469", "source": "PREGO", "taxon_label": "Acinetobacter", "score": 4.0, "rank": 8, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:475", "source": "PREGO", "taxon_label": "Moraxella", "score": 4.0, "rank": 9, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:48736", "source": "PREGO", "taxon_label": "Ralstonia", "score": 4.0, "rank": 10, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:68287", "source": "PREGO", "taxon_label": "Mesorhizobium", "score": 4.0, "rank": 11, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:68892", "source": "PREGO", "taxon_label": "Streptococcus infantis", "score": 4.0, "rank": 12, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:69277", "source": "PREGO", "taxon_label": "Phyllobacteriaceae", "score": 4.0, "rank": 13, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:712", "source": "PREGO", "taxon_label": "Pasteurellaceae", "score": 4.0, "rank": 14, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:724", "source": "PREGO", "taxon_label": "Haemophilus", "score": 4.0, "rank": 15, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:727", "source": "PREGO", "taxon_label": "Haemophilus influenzae", "score": 4.0, "rank": 16, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:75682", "source": "PREGO", "taxon_label": "Oxalobacteraceae", "score": 4.0, "rank": 17, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:1578", "source": "PREGO", "taxon_label": "Lactobacillus", "score": 1.79042, "rank": 18, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:1867933", "source": "PREGO", "taxon_label": "Aggregatibacter pneumotropica (nom. nud.)", "score": 1.77924, "rank": 19, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:1386", "source": "PREGO", "taxon_label": "Bacillus &lt;firmicutes&gt;", "score": 1.76788, "rank": 20, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:55087", "source": "PREGO", "score": 1.76788, "rank": 21, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:665874", "source": "PREGO", "taxon_label": "Limnohabitans", "score": 1.70823, "rank": 22, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:374", "source": "PREGO", "taxon_label": "Bradyrhizobium", "score": 1.69569, "rank": 23, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:713", "source": "PREGO", "taxon_label": "Actinobacillus", "score": 1.6432, "rank": 24, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:468", "source": "PREGO", "taxon_label": "Moraxellaceae", "score": 1.60117, "rank": 25, "candidate_pool": 48}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by PREGO. Grounding: EXACT."}]} |
| EP9 | data/habitats/host_associated/thorax.yaml; Full immediate-parent record; context only | supports | {"identifier": "BTO:0001368", "label": "thorax", "definition": "1: The part of the mammalian body between the neck and the abdomen; also: its cavity in which the heart and lungs lie. 2: The middle of the three chief divisions of the body of an insect; also: the corresponding part of a crustacean or an arachnid.", "definition_source": "BTO", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "EXACT", "mapping_status": "REVIEWED", "synonyms": [{"synonym_text": "Thorax/Pereon", "synonym_type": "EXACT_SYNONYM", "source": "GOLD"}, {"synonym_text": "chest", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "chests", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "thoraxes", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "thoraxic", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}], "parent_habitats": ["habitatmech:GOLD.bd9662fadb", "habitatmech:GOLD.dba2a83b95"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:7163", "source_label": "Thorax", "source_path": "Host-associated &gt; Arthropoda: Insects &gt; Thorax", "mapping_predicate": "skos:exactMatch", "notes": "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}, {"source": "GOLD", "source_id": "gold.ecosystem:7306", "source_label": "Thorax/Pereon", "source_path": "Host-associated &gt; Arthropoda: Crustaceans &gt; Whole body &gt; Thorax/Pereon", "mapping_predicate": "skos:exactMatch", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}, {"source": "PREGO", "source_id": "BTO:0001368", "source_label": "thorax", "assertion_count": 2, "assertion_unit": "TAXON", "score": 3.0, "evidence_channels": "annotated_genomes_isolates"}], "characteristic_taxa": [{"taxon_id": "NCBITaxon:1330043", "source": "PREGO", "taxon_label": "Bacillus bombysepticus str. Wang", "score": 3.0, "rank": 1, "candidate_pool": 2}, {"taxon_id": "NCBITaxon:1773", "source": "PREGO", "taxon_label": "Mycobacterium tuberculosis", "score": 3.0, "rank": 2, "candidate_pool": 2}], "curation_history": [{"timestamp": "2026-08-12T00:00:00Z", "curator": "claude-opus-5", "action": "GROUND", "changes": "Grounded to BTO:0001368 'thorax' (EXACT). Slash alternative naming one thing; grounded to the head term. Pereon is the crustacean thorax. Pulled out of the class-level sweep, whose note wrongly claimed no term matched. Label: 'Thorax/Pereon'. (source concept habitatmech:GOLD.be1c317f16)"}, {"timestamp": "2026-08-13T00:00:00Z", "curator": "claude-opus-5", "action": "REVIEW", "changes": "Reviewed and endorsed the seeder's own resolution. Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date. (source concept habitatmech:GOLD.6dc8b64fca)"}, {"timestamp": "2026-08-13T00:00:00Z", "curator": "claude-opus-5", "action": "REVIEW", "changes": "Reviewed and endorsed the seeder's own resolution. Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date. (source concept habitatmech:PREGO.a150350ee1)"}, {"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD, PREGO. Grounding: EXACT."}]} |
| EP10 | data/habitats/host_associated/whole_body__e6584d8d.yaml; Full immediate-parent record; context only | supports | {"identifier": "habitatmech:GOLD.bd9662fadb", "label": "Whole body", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats": ["BTO:0001489", "habitatmech:GOLD.2959225799"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:7236", "source_label": "Whole body", "source_path": "Host-associated &gt; Arthropoda: Crustaceans &gt; Whole body", "mapping_predicate": "skos:narrowMatch", "notes": "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NARROW."}]} |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000282/graph; BTO_0000282-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000282", "target": "http://purl.obolibrary.org/obo/BTO_0001489", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000282; BTO_0000282.json | context_only | Current term identity, active status and definition: {"obo_id": "BTO:0000282", "label": "head", "is_obsolete": false, "description": ["The upper or anterior division of the animal body that contains the brain, the chief sense organs, and the mouth."]} |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001368/graph; BTO_0001368-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0001368", "target": "http://purl.obolibrary.org/obo/BTO_0001493", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001368; BTO_0001368.json | context_only | Current term identity, active status and definition: {"obo_id": "BTO:0001368", "label": "thorax", "is_obsolete": false, "description": ["1: The part of the mammalian body between the neck and the abdomen; also: its cavity in which the heart and lungs lie. 2: The middle of the three chief divisions of the body of an insect; also: the corresponding part of a crustacean or an arachnid."]} |
| EX5 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001489/graph; BTO_0001489-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0001489", "target": "http://purl.obolibrary.org/obo/BTO_0000042", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX6 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001489; BTO_0001489.json | context_only | Current term identity, active status and definition: {"obo_id": "BTO:0001489", "label": "whole body", "is_obsolete": false, "description": ["The main part of an animal body especially as distinguished from limbs and head."]} |
| EX7 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001906/graph; BTO_0001906-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0001906", "target": "http://purl.obolibrary.org/obo/BTO_0000282", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/BTO_0001906", "target": "http://purl.obolibrary.org/obo/BTO_0001368", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX8 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001906; BTO_0001906.json | context_only | Current term identity, active status and definition: {"obo_id": "BTO:0001906", "label": "cephalothorax", "is_obsolete": false, "description": ["The united head and thorax of an arachnid or higher crustacean."]} |
| ESEARCH | Local maintained inputs and review archive; rg --no-ignore --hidden -l -F -e BTO:0001906 -e cephalothorax -e cephalothorax -e habitatmech:GOLD.60a0f24d46 curation history research reports data/raw build reviews | context_only | Identifier/label/slug search and full structured-YAML traversal; exact TSV rows were parsed separately. Broad search matches are leads, not all independently reviewed. |

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
review_id: 20261015T235747Z-cephalothorax-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: cephalothorax (BTO:0001906)'
started_at: '2026-10-15T23:40:17Z'
finished_at: '2026-10-15T23:57:47Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent inspected record and sources; not independent human
    or second-agent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: BTO cephalothorax denotes united head and thorax, coherent with the crustacean
  source. Current BTO itself asserts head and thorax as subclass parents; this is
  not an importer conversion of part_of edges. The independent GOLD whole-Body superclass
  is unsupported. Remove only that source contribution, preserving the ontology-owned
  parents and zero-count semantics.
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
  - path: data/habitats/host_associated/cephalothorax.yaml
    sha256: 5c0d66e13b57e4210a3bb75dc655efefaba7af889734da40d0af151264aa9d95
    role: target
  - path: data/habitats/host_associated/head.yaml
    sha256: 52a23ed29f99bf09798a1ca7bad875b68408c7a2aa052b1efdb8dd48e6fe6e45
    role: context
  - path: data/habitats/host_associated/thorax.yaml
    sha256: 020b548ccdc5f6e0f15049bfc7d754958b286ce2238edf4df5fc98e4b1c51b75
    role: context
  - path: data/habitats/host_associated/whole_body__e6584d8d.yaml
    sha256: 4786bff3120d4b33bd5d5f701f54f892a3a8f18f3cfcb7f962ab6338fcdba23a
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
- target_id: BTO:0001906
  path: data/habitats/host_associated/cephalothorax.yaml
  label: cephalothorax
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
  - BTO:0001906
  exclusions:
  - target: Other records, original source specimens and SSSOM/KGX products
    reason: Parent and source context do not add reviewed targets; exports and every
      original source specimen are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/cephalothorax.yaml
  exit_code: 0
  target_ids:
  - BTO:0001906
  summary: "Finished 2026-10-15T23:45:06Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/cephalothorax.yaml"
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
  - BTO:0001906
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
  - BTO:0001906
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
  - BTO:0001906
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
  - BTO:0001906
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
  - BTO:0001906
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
  - BTO:0001906
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
  - BTO:0001906
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
  - BTO:0001906
  summary: Verified 2026-10-15T23:55:08Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38822113212
  scope_note: Unchanged committed scientific-input baseline; new output bundles are
    outside this run.
- check_id: CREF
  name: Standalone evidence-reference validator applicability
  status: not_applicable
  required: false
  target_ids:
  - BTO:0001906
  summary: No standalone citation/reference validator is documented for these evidence-free
    generated records. Target EvidenceItems and causal edges are absent. Stable source
    and ontology/taxon references were checked manually and with documented native
    gates; current-decision primary citations were separately verified where present.
  scope_note: No command or exit code is invented for an unavailable/nonapplicable
    checker. Full-corpus causal validation ran separately.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/cephalothorax.yaml
  locator: Entire target YAML
  accessed_at: '2026-10-15T23:57:47Z'
  support: supports
  summary: All fields, attestations, taxa and generated history read.
  snapshot_sha256: 5c0d66e13b57e4210a3bb75dc655efefaba7af889734da40d0af151264aa9d95
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, strict broader hierarchy and evidence rules
  accessed_at: '2026-10-15T23:57:47Z'
  support: supports
  summary: Organism, disease, material and habitat identities remain distinct. Parents
    must be strictly broader, not merely containing sites.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: HabitatRecord, SourceAttestation and TaxonAssociation
  accessed_at: '2026-10-15T23:57:47Z'
  support: supports
  summary: Mapping predicate endpoint is source-to-record; source association is weaker
    than characteristic presence. Optional fields and native review status have distinct
    contracts.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native source routes and complete document reproduction
  accessed_at: '2026-10-15T23:57:47Z'
  support: supports
  summary: '[{"mint": "habitatmech:GOLD.60a0f24d46", "automatic": {"identifier": "BTO:0001906",
    "grounding_status": "EXACT", "mapping_predicate": "skos:exactMatch", "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "gold_leaf_label", "category":
    null, "reviewed": false, "decision": null}, "final": {"identifier": "BTO:0001906",
    "grounding_status": "EXACT", "mapping_predicate": "skos:exactMatch", "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "gold_leaf_label", "category":
    null, "reviewed": false, "decision": null}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: Source counts, channels and taxon ranking
  accessed_at: '2026-10-15T23:57:47Z'
  support: supports
  summary: Exact frozen rows reproduce counts/units and ranked taxon scores. The committed
    projection does not retain original PREGO pair citation links.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Physical TSV rows 1787
  accessed_at: '2026-10-15T23:57:47Z'
  support: supports
  summary: '[{"row": 1787, "data": {"canonical_path": "Host-associated > Arthropoda:
    Crustaceans > Whole body > Cephalothorax", "ecosystem": "Host-associated", "ecosystem_category":
    "Arthropoda: Crustaceans", "ecosystem_type": "Whole body", "ecosystem_subtype":
    "Cephalothorax", "specific_ecosystem": "", "leaf_label": "Cephalothorax", "depth":
    "4", "gold_node_count": "2", "organism_count": "0", "study_count": "0", "biosample_count":
    "0", "total_assertions": "0", "gold_node_ids": "gold.ecosystem:7310|gold.ecosystem:7311"}}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: ET6
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: Physical TSV rows 1284,1285
  accessed_at: '2026-10-15T23:57:47Z'
  support: supports
  summary: '[{"row": 1284, "data": {"subject": "BTO:0001906", "predicate": "rdfs:subClassOf",
    "object": "BTO:0000282"}}, {"row": 1285, "data": {"subject": "BTO:0001906", "predicate":
    "rdfs:subClassOf", "object": "BTO:0001368"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET7
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 284,1369,1906
  accessed_at: '2026-10-15T23:57:47Z'
  support: supports
  summary: '[{"row": 284, "data": {"term_id": "BTO:0000282", "ontology": "BTO", "label":
    "head", "definition": "The upper or anterior division of the animal body that
    contains the brain, the chief sense organs, and the mouth.", "synonyms": "", "deprecated":
    "", "directly_referenced": "TRUE", "label_only": "FALSE"}}, {"row": 1369, "data":
    {"term_id": "BTO:0001368", "ontology": "BTO", "label": "thorax", "definition":
    "1: The part of the mammalian body between the neck and the abdomen; also: its
    cavity in which the heart and lungs lie. 2: The middle of the three chief divisions
    of the body of an insect; also: the corresponding part of a crustacean or an arachnid.",
    "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only":
    "FALSE"}}, {"row": 1906, "data": {"term_id": "BTO:0001906", "ontology": "BTO",
    "label": "cephalothorax", "definition": "The united head and thorax of an arachnid
    or higher crustacean.", "synonyms": "", "deprecated": "", "directly_referenced":
    "FALSE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EP8
  kind: record_content
  reference: data/habitats/host_associated/head.yaml
  locator: Full immediate-parent record; context only
  accessed_at: '2026-10-15T23:57:47Z'
  support: supports
  summary: '{"identifier": "BTO:0000282", "label": "head", "definition": "The upper
    or anterior division of the animal body that contains the brain, the chief sense
    organs, and the mouth.", "definition_source": "BTO", "habitat_category": "HOST_ASSOCIATED",
    "grounding_status": "EXACT", "mapping_status": "SEEDED", "source_attestations":
    [{"source": "PREGO", "source_id": "BTO:0000282", "source_label": "head", "assertion_count":
    48, "assertion_unit": "TAXON", "score": 4.0, "evidence_channels": "environmental_samples"}],
    "characteristic_taxa": [{"taxon_id": "NCBITaxon:102234", "source": "PREGO", "taxon_label":
    "Cyanobacterium", "score": 4.0, "rank": 1, "candidate_pool": 48}, {"taxon_id":
    "NCBITaxon:1117", "source": "PREGO", "taxon_label": "Cyanobacteriota", "score":
    4.0, "rank": 2, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:117563", "source":
    "PREGO", "taxon_label": "Granulicatella", "score": 4.0, "rank": 3, "candidate_pool":
    48}, {"taxon_id": "NCBITaxon:1279", "source": "PREGO", "taxon_label": "Staphylococcus",
    "score": 4.0, "rank": 4, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:1301",
    "source": "PREGO", "taxon_label": "Streptococcus", "score": 4.0, "rank": 5, "candidate_pool":
    48}, {"taxon_id": "NCBITaxon:1716", "source": "PREGO", "taxon_label": "Corynebacterium",
    "score": 4.0, "rank": 6, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:32008",
    "source": "PREGO", "taxon_label": "Burkholderia", "score": 4.0, "rank": 7, "candidate_pool":
    48}, {"taxon_id": "NCBITaxon:469", "source": "PREGO", "taxon_label": "Acinetobacter",
    "score": 4.0, "rank": 8, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:475",
    "source": "PREGO", "taxon_label": "Moraxella", "score": 4.0, "rank": 9, "candidate_pool":
    48}, {"taxon_id": "NCBITaxon:48736", "source": "PREGO", "taxon_label": "Ralstonia",
    "score": 4.0, "rank": 10, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:68287",
    "source": "PREGO", "taxon_label": "Mesorhizobium", "score": 4.0, "rank": 11, "candidate_pool":
    48}, {"taxon_id": "NCBITaxon:68892", "source": "PREGO", "taxon_label": "Streptococcus
    infantis", "score": 4.0, "rank": 12, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:69277",
    "source": "PREGO", "taxon_label": "Phyllobacteriaceae", "score": 4.0, "rank":
    13, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:712", "source": "PREGO", "taxon_label":
    "Pasteurellaceae", "score": 4.0, "rank": 14, "candidate_pool": 48}, {"taxon_id":
    "NCBITaxon:724", "source": "PREGO", "taxon_label": "Haemophilus", "score": 4.0,
    "rank": 15, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:727", "source": "PREGO",
    "taxon_label": "Haemophilus influenzae", "score": 4.0, "rank": 16, "candidate_pool":
    48}, {"taxon_id": "NCBITaxon:75682", "source": "PREGO", "taxon_label": "Oxalobacteraceae",
    "score": 4.0, "rank": 17, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:1578",
    "source": "PREGO", "taxon_label": "Lactobacillus", "score": 1.79042, "rank": 18,
    "candidate_pool": 48}, {"taxon_id": "NCBITaxon:1867933", "source": "PREGO", "taxon_label":
    "Aggregatibacter pneumotropica (nom. nud.)", "score": 1.77924, "rank": 19, "candidate_pool":
    48}, {"taxon_id": "NCBITaxon:1386", "source": "PREGO", "taxon_label": "Bacillus
    <firmicutes>", "score": 1.76788, "rank": 20, "candidate_pool": 48}, {"taxon_id":
    "NCBITaxon:55087", "source": "PREGO", "score": 1.76788, "rank": 21, "candidate_pool":
    48}, {"taxon_id": "NCBITaxon:665874", "source": "PREGO", "taxon_label": "Limnohabitans",
    "score": 1.70823, "rank": 22, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:374",
    "source": "PREGO", "taxon_label": "Bradyrhizobium", "score": 1.69569, "rank":
    23, "candidate_pool": 48}, {"taxon_id": "NCBITaxon:713", "source": "PREGO", "taxon_label":
    "Actinobacillus", "score": 1.6432, "rank": 24, "candidate_pool": 48}, {"taxon_id":
    "NCBITaxon:468", "source": "PREGO", "taxon_label": "Moraxellaceae", "score": 1.60117,
    "rank": 25, "candidate_pool": 48}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z",
    "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded
    from data/raw/ inventories; attested by PREGO. Grounding: EXACT."}]}'
  snapshot_sha256: 52a23ed29f99bf09798a1ca7bad875b68408c7a2aa052b1efdb8dd48e6fe6e45
- evidence_id: EP9
  kind: record_content
  reference: data/habitats/host_associated/thorax.yaml
  locator: Full immediate-parent record; context only
  accessed_at: '2026-10-15T23:57:47Z'
  support: supports
  summary: '{"identifier": "BTO:0001368", "label": "thorax", "definition": "1: The
    part of the mammalian body between the neck and the abdomen; also: its cavity
    in which the heart and lungs lie. 2: The middle of the three chief divisions of
    the body of an insect; also: the corresponding part of a crustacean or an arachnid.",
    "definition_source": "BTO", "habitat_category": "HOST_ASSOCIATED", "grounding_status":
    "EXACT", "mapping_status": "REVIEWED", "synonyms": [{"synonym_text": "Thorax/Pereon",
    "synonym_type": "EXACT_SYNONYM", "source": "GOLD"}, {"synonym_text": "chest",
    "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "chests",
    "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "thoraxes",
    "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "thoraxic",
    "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}], "parent_habitats": ["habitatmech:GOLD.bd9662fadb",
    "habitatmech:GOLD.dba2a83b95"], "source_attestations": [{"source": "GOLD", "source_id":
    "gold.ecosystem:7163", "source_label": "Thorax", "source_path": "Host-associated
    > Arthropoda: Insects > Thorax", "mapping_predicate": "skos:exactMatch", "notes":
    "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."},
    {"source": "GOLD", "source_id": "gold.ecosystem:7306", "source_label": "Thorax/Pereon",
    "source_path": "Host-associated > Arthropoda: Crustaceans > Whole body > Thorax/Pereon",
    "mapping_predicate": "skos:exactMatch", "notes": "2 GOLD ecosystem node ids share
    this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}, {"source": "PREGO",
    "source_id": "BTO:0001368", "source_label": "thorax", "assertion_count": 2, "assertion_unit":
    "TAXON", "score": 3.0, "evidence_channels": "annotated_genomes_isolates"}], "characteristic_taxa":
    [{"taxon_id": "NCBITaxon:1330043", "source": "PREGO", "taxon_label": "Bacillus
    bombysepticus str. Wang", "score": 3.0, "rank": 1, "candidate_pool": 2}, {"taxon_id":
    "NCBITaxon:1773", "source": "PREGO", "taxon_label": "Mycobacterium tuberculosis",
    "score": 3.0, "rank": 2, "candidate_pool": 2}], "curation_history": [{"timestamp":
    "2026-08-12T00:00:00Z", "curator": "claude-opus-5", "action": "GROUND", "changes":
    "Grounded to BTO:0001368 ''thorax'' (EXACT). Slash alternative naming one thing;
    grounded to the head term. Pereon is the crustacean thorax. Pulled out of the
    class-level sweep, whose note wrongly claimed no term matched. Label: ''Thorax/Pereon''.
    (source concept habitatmech:GOLD.be1c317f16)"}, {"timestamp": "2026-08-13T00:00:00Z",
    "curator": "claude-opus-5", "action": "REVIEW", "changes": "Reviewed and endorsed
    the seeder''s own resolution. Multi-source review pass: this record is attested
    by more than one independent vocabulary, and this source''s label or path was
    read against the record''s ontology term to check the merge is right. It agrees.
    Source concepts in the same pass whose labels did not agree were re-decided rather
    than endorsed; see the pass''s other decisions of the same date. (source concept
    habitatmech:GOLD.6dc8b64fca)"}, {"timestamp": "2026-08-13T00:00:00Z", "curator":
    "claude-opus-5", "action": "REVIEW", "changes": "Reviewed and endorsed the seeder''s
    own resolution. Multi-source review pass: this record is attested by more than
    one independent vocabulary, and this source''s label or path was read against
    the record''s ontology term to check the merge is right. It agrees. Source concepts
    in the same pass whose labels did not agree were re-decided rather than endorsed;
    see the pass''s other decisions of the same date. (source concept habitatmech:PREGO.a150350ee1)"},
    {"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action":
    "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested
    by GOLD, PREGO. Grounding: EXACT."}]}'
  snapshot_sha256: 020b548ccdc5f6e0f15049bfc7d754958b286ce2238edf4df5fc98e4b1c51b75
- evidence_id: EP10
  kind: record_content
  reference: data/habitats/host_associated/whole_body__e6584d8d.yaml
  locator: Full immediate-parent record; context only
  accessed_at: '2026-10-15T23:57:47Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.bd9662fadb", "label": "Whole body", "habitat_category":
    "HOST_ASSOCIATED", "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats":
    ["BTO:0001489", "habitatmech:GOLD.2959225799"], "source_attestations": [{"source":
    "GOLD", "source_id": "gold.ecosystem:7236", "source_label": "Whole body", "source_path":
    "Host-associated > Arthropoda: Crustaceans > Whole body", "mapping_predicate":
    "skos:narrowMatch", "notes": "3 GOLD ecosystem node ids share this path; first
    shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp":
    "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES",
    "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NARROW."}]}'
  snapshot_sha256: 4786bff3120d4b33bd5d5f701f54f892a3a8f18f3cfcb7f962ab6338fcdba23a
- evidence_id: EX1
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000282/graph
  locator: BTO_0000282-graph.json
  accessed_at: '2026-10-15T23:42:07Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000282",
    "target": "http://purl.obolibrary.org/obo/BTO_0001489", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 39585dae16e6f807d87d6946f457afdbe9641c0a826565d8c465d0962f446ab2
- evidence_id: EX2
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000282
  locator: BTO_0000282.json
  accessed_at: '2026-10-15T23:42:06Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "BTO:0000282",
    "label": "head", "is_obsolete": false, "description": ["The upper or anterior
    division of the animal body that contains the brain, the chief sense organs, and
    the mouth."]}'
  snapshot_sha256: f18c95f23cc5be4079921c2caccc7d989df8b30570d05cc87543d530f36ec385
- evidence_id: EX3
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001368/graph
  locator: BTO_0001368-graph.json
  accessed_at: '2026-10-15T23:42:15Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0001368",
    "target": "http://purl.obolibrary.org/obo/BTO_0001493", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: b42e831cb16064b2db6ff39b996fec36053643242620f13df3592de5fe776eeb
- evidence_id: EX4
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001368
  locator: BTO_0001368.json
  accessed_at: '2026-10-15T23:42:15Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "BTO:0001368",
    "label": "thorax", "is_obsolete": false, "description": ["1: The part of the mammalian
    body between the neck and the abdomen; also: its cavity in which the heart and
    lungs lie. 2: The middle of the three chief divisions of the body of an insect;
    also: the corresponding part of a crustacean or an arachnid."]}'
  snapshot_sha256: b9f045d3ee0e01a10d48e2dac3670c0338c3f3383799787b1a3a43e3607c510c
- evidence_id: EX5
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001489/graph
  locator: BTO_0001489-graph.json
  accessed_at: '2026-10-15T23:42:18Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0001489",
    "target": "http://purl.obolibrary.org/obo/BTO_0000042", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: 5b2acbf2f68e0816d9b5636faa97f5118e7c60c62812ee10aacc76a40403b8b2
- evidence_id: EX6
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001489
  locator: BTO_0001489.json
  accessed_at: '2026-10-15T23:42:17Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "BTO:0001489",
    "label": "whole body", "is_obsolete": false, "description": ["The main part of
    an animal body especially as distinguished from limbs and head."]}'
  snapshot_sha256: 4fea6f60d02e8b9c1e037e67462291d0d41f6716ba47e465c8f800e64a75227d
- evidence_id: EX7
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001906/graph
  locator: BTO_0001906-graph.json
  accessed_at: '2026-10-15T23:42:19Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0001906",
    "target": "http://purl.obolibrary.org/obo/BTO_0000282", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/BTO_0001906",
    "target": "http://purl.obolibrary.org/obo/BTO_0001368", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: cd4ed99dba2125936dead62620ca441cf0750fd285484e010a932abf4798a936
- evidence_id: EX8
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001906
  locator: BTO_0001906.json
  accessed_at: '2026-10-15T23:42:18Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "BTO:0001906",
    "label": "cephalothorax", "is_obsolete": false, "description": ["The united head
    and thorax of an arachnid or higher crustacean."]}'
  snapshot_sha256: ea9953f97817a9c95a12a10b04712183395f5915460dd4c62b7d34069286c422
- evidence_id: ESEARCH
  kind: search
  reference: Local maintained inputs and review archive
  locator: rg --no-ignore --hidden -l -F -e BTO:0001906 -e cephalothorax -e cephalothorax
    -e habitatmech:GOLD.60a0f24d46 curation history research reports data/raw build
    reviews
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
  outcome: concern
  summary: BTO cephalothorax denotes united head and thorax, coherent with the crustacean
    source. Current BTO itself asserts head and thorax as subclass parents; this is
    not an importer conversion of part_of edges. The independent GOLD whole-Body superclass
    is unsupported. Remove only that source contribution, preserving the ontology-owned
    parents and zero-count semantics.
  target_ids:
  - BTO:0001906
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - EP8
  - EP9
  - EP10
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
- assessment_id: A2
  area: quantity
  topic: Source assertions, pools, ranks and supplementary context
  outcome: supported
  summary: 'All emitted counts/units, labels, ranks, scores and candidate pools match
    exact frozen rows. [{"source": "GOLD", "count": 0, "unit": "ORGANISM"}]. Zero
    tree counts are omitted; later biosamples and study memberships are not added.
    Current taxonomy resolves displayed identifiers including explicit aliases.'
  target_ids:
  - BTO:0001906
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
  - EX8
- assessment_id: A3
  area: evidence
  topic: Biological support and bounded source uncertainty
  outcome: supported
  summary: BTO cephalothorax denotes united head and thorax, coherent with the crustacean
    source. Current BTO itself asserts head and thorax as subclass parents; this is
    not an importer conversion of part_of edges. The independent GOLD whole-Body superclass
    is unsupported. Remove only that source contribution, preserving the ontology-owned
    parents and zero-count semantics.
  target_ids:
  - BTO:0001906
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - EP8
  - EP9
  - EP10
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
- assessment_id: A4
  area: completeness
  topic: Native status, optional parameters and causal mechanisms
  outcome: supported
  summary: Executed native resolution reproduces EXACT/SEEDED. No environmental parameters,
    causal graphs, discussions, datasets or is_characteristic=true claims are present.
    Missing optional fields and SEEDED status alone are not defects; parent mechanisms
    are not inherited.
  target_ids:
  - BTO:0001906
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
  - BTO:0001906
  evidence_ids:
  - E1
  - ERULE
findings:
- finding_id: F1
  issue_key: cephalothorax-context-parent
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Source context is not a supported broader habitat class
  description: BTO cephalothorax denotes united head and thorax, coherent with the
    crustacean source. Current BTO itself asserts head and thorax as subclass parents;
    this is not an importer conversion of part_of edges. The independent GOLD whole-Body
    superclass is unsupported. Remove only that source contribution, preserving the
    ontology-owned parents and zero-count semantics. Suppress only source-path/expected-parent
    guarded GOLD contribution habitatmech:GOLD.bd9662fadb; retain valid independent
    genera and all raw provenance.
  target_ids:
  - BTO:0001906
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
  - EP8
  - EP9
  - EP10
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported hierarchy, mapping or source-evidence
    semantics; correct deterministic reproduction does not establish scientific support.
  external_issues: []
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - BTO:0001906
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: BTO cephalothorax denotes united head and thorax, coherent with the
    crustacean source. Current BTO itself asserts head and thorax as subclass parents;
    this is not an importer conversion of part_of edges. The independent GOLD whole-Body
    superclass is unsupported. Remove only that source contribution, preserving the
    ontology-owned parents and zero-count semantics. Suppress only source-path/expected-parent
    guarded GOLD contribution habitatmech:GOLD.bd9662fadb; retain valid independent
    genera and all raw provenance. No repair is performed by this review.
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
