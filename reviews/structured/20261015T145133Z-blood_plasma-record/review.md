# Record review: blood plasma (BTO:0000131)

- Review: 20261015T145133Z-blood_plasma-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T14:33:26Z
- Finished UTC: 2026-10-15T14:51:33Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The BTO plasma definition denotes the fluid component of blood; its part-of relation is correctly not emitted as subclass ancestry. Fifteen score-three PREGO associations are faithfully projected. The inspected CECT8145 genome article concerns probiotic ingestion and metabolic outcomes, not plasma isolation. Original pair evidence is unavailable, so this is a provisional localization-evidence concern, not proof that the strain can never occur in plasma.

## Scope And Provenance

Full scientific assessment of one exact target at b558fd561286d1fe3ba133784776f7be1f9f49fb.

Selection: One of the next 21 path-ordered unreviewed records, blood through bone marrow; this bundle assesses only this identifier.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base b558fd561286d1fe3ba133784776f7be1f9f49fb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0000131 | data/habitats/host_associated/blood_plasma.yaml | generated | blood plasma |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0000131 | Completed 2026-10-15T14:34:52Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/blood_plasma.yaml |
| validate-strict | passed | True | BTO:0000131 | Completed 2026-10-15T14:36:08Z. uv run python scripts/validate_strict.py data/habitats/host_associated/blood.yaml data/habitats/host_associated/blood__070ce7aa.yaml data/habitats/host_associated/blood__5ca8064f.yaml data/habitats/host_associated/blood__5ef3f2f4.yaml data/habitats/host_associated/blood__c1b484fe.yaml data/habitats/host_associated/blood__d6f5ae05.yaml data/habitats/host_associated/blood_plasma.yaml data/habitats/host_associated/blood_plasma__00b70c6a.yaml data/habitats/host_associated/blood_serum.yaml data/habitats/host_associated/blood_vessel.yaml data/habitats/host_associated/bone.yaml data/habitats/host_associated/bone__169c3d9e.yaml data/habitats/host_associated/bone__234001be.yaml data/habitats/host_associated/bone__71064238.yaml data/habitats/host_associated/bone__8430e16e.yaml data/habitats/host_associated/bone__8d0df242.yaml data/habitats/host_associated/bone__b47efce2.yaml data/habitats/host_associated/bone_element.yaml data/habitats/host_associated/bone_marrow.yaml data/habitats/host_associated/bone_marrow__9387f1a6.yaml data/habitats/host_associated/bone_marrow__c1fc5dec.yaml<br>Validating 21 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      21<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | BTO:0000131 | Completed 2026-10-15T14:36:40Z. No issues found<br>813 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | BTO:0000131 | Completed 2026-10-15T14:36:43Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | BTO:0000131 | Completed 2026-10-15T14:37:37Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | BTO:0000131 | Completed 2026-10-15T14:37:45Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | BTO:0000131 | Completed 2026-10-15T14:38:11Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | BTO:0000131 | Completed 2026-10-15T14:39:21Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-baseline full QC | passed | True | BTO:0000131 | Verified 2026-10-15T14:33:14Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38748091185 |

## Scientific And Domain Assessments

### Identity and hierarchy

identity: supported. Targets: BTO:0000131.

The BTO plasma definition denotes the fluid component of blood; its part-of relation is correctly not emitted as subclass ancestry. Fifteen score-three PREGO associations are faithfully projected. The inspected CECT8145 genome article concerns probiotic ingestion and metabolic outcomes, not plasma isolation. Original pair evidence is unavailable, so this is a provisional localization-evidence concern, not proof that the strain can never occur in plasma.

### Frozen source units, ranks and parameters

quantity: supported. Targets: BTO:0000131.

Count/unit, first GOLD node, channel, score and displayed taxon ranks/labels reproduce exact source rows. Verification: [{"source": "PREGO", "count": 15, "unit": "TAXON"}]. Zero counts are omitted, never interpreted as absence. Side-table biosamples/studies and MIxS slots are not added to tree ORGANISM counts.

### Scientific support and source limits

evidence: concern. Targets: BTO:0000131.

The BTO plasma definition denotes the fluid component of blood; its part-of relation is correctly not emitted as subclass ancestry. Fifteen score-three PREGO associations are faithfully projected. The inspected CECT8145 genome article concerns probiotic ingestion and metabolic outcomes, not plasma isolation. Original pair evidence is unavailable, so this is a provisional localization-evidence concern, not proof that the strain can never occur in plasma.

### Native status and optional assertions

completeness: supported. Targets: BTO:0000131.

Executed routes reproduce EXACT/SEEDED. No causal edge or is_characteristic=true assertion is made. Optional absent fields and SEEDED status alone are not scientific defects; this review does not promote native status.

### Deterministic native gates

schema: supported. Targets: BTO:0000131.

Schema, strict, history, provenance, 3,208-record reproduction, causal, term-request, configured-label and exact-baseline full QC checks passed; these prove fidelity, not biological truth.

## Findings

### F1: Original pair evidence is needed to establish site localization

major / open / provisional; issue key: blood-plasma-prego-pair-scope.

The BTO plasma definition denotes the fluid component of blood; its part-of relation is correctly not emitted as subclass ancestry. Fifteen score-three PREGO associations are faithfully projected. The inspected CECT8145 genome article concerns probiotic ingestion and metabolic outcomes, not plasma isolation. Original pair evidence is unavailable, so this is a provisional localization-evidence concern, not proof that the strain can never occur in plasma. Recover manifest-matching pair citations, distinguish patient/outcome context from sampled site, and correct or qualify only supported mismatches through a governed source contract. Do not delete taxa or decrement totals by hand.

## Recommended Actions And Acceptance Checks

### ACT1

The BTO plasma definition denotes the fluid component of blood; its part-of relation is correctly not emitted as subclass ancestry. Fifteen score-three PREGO associations are faithfully projected. The inspected CECT8145 genome article concerns probiotic ingestion and metabolic outcomes, not plasma isolation. Original pair evidence is unavailable, so this is a provisional localization-evidence concern, not proof that the strain can never occur in plasma. Recover manifest-matching pair citations, distinguish patient/outcome context from sampled site, and correct or qualify only supported mismatches through a governed source contract. Do not delete taxa or decrement totals by hand. No repair is performed by this review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history. Do not change source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/blood_plasma.yaml; Entire target YAML | supports | Full target read, including every source attestation, taxon, parent, parameter and history entry. |
| ERULE | docs/CURATION.md; Strict ancestry and maintained-input ownership | supports | Parent means strictly broader, not containing organ, body or system. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation, EnvironmentalParameter, CharacteristicTaxon | supports | Source-to-record mapping contract; qualified parameters and observed associations are not universal conditions or characteristic presence. |
| ESEED | src/habitatmech/seed.py; Executed build_corpus and apply_decision routes | supports | Whole generated document equality verified; source-specific resolutions: [{"mint": "habitatmech:PREGO.cedc68741c", "automatic": {"identifier": "BTO:0000131", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "BTO:0000131", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}}] |
| EEXTRACT | src/habitatmech/extract.py; Source projection | supports | PREGO projects counts, scores, channels and ranked taxa without original pair citations. |
| ET5 | data/raw/prego_habitat_taxa.tsv; Physical TSV rows 143,144,145,146,147,148,149,150,151,152,153,154,155,156,157 | supports | [{"row": 143, "data": {"prego_id": "BTO:0000131", "rank": "1", "taxon_id": "NCBITaxon:1322345", "taxon_label": "Escherichia coli ATCC 25922", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 144, "data": {"prego_id": "BTO:0000131", "rank": "2", "taxon_id": "NCBITaxon:1415606", "taxon_label": "Bifidobacterium animalis subsp. lactis CECT 8145", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 145, "data": {"prego_id": "BTO:0000131", "rank": "3", "taxon_id": "NCBITaxon:1718", "taxon_label": "Corynebacterium glutamicum", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 146, "data": {"prego_id": "BTO:0000131", "rank": "4", "taxon_id": "NCBITaxon:203119", "taxon_label": "Acetivibrio thermocellus ATCC 27405", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 147, "data": {"prego_id": "BTO:0000131", "rank": "5", "taxon_id": "NCBITaxon:214092", "taxon_label": "Yersinia pestis CO92", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 148, "data": {"prego_id": "BTO:0000131", "rank": "6", "taxon_id": "NCBITaxon:273075", "taxon_label": "Thermoplasma acidophilum DSM 1728", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 149, "data": {"prego_id": "BTO:0000131", "rank": "7", "taxon_id": "NCBITaxon:287", "taxon_label": "Pseudomonas aeruginosa", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 150, "data": {"prego_id": "BTO:0000131", "rank": "8", "taxon_id": "NCBITaxon:316407", "taxon_label": "Escherichia coli str. K-12 substr. W3110", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 151, "data": {"prego_id": "BTO:0000131", "rank": "9", "taxon_id": "NCBITaxon:32002", "taxon_label": "Achromobacter denitrificans", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 152, "data": {"prego_id": "BTO:0000131", "rank": "10", "taxon_id": "NCBITaxon:354242", "taxon_label": "Campylobacter jejuni subsp. jejuni 81-176", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 153, "data": {"prego_id": "BTO:0000131", "rank": "11", "taxon_id": "NCBITaxon:47885", "taxon_label": "Pseudomonas oryzihabitans", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 154, "data": {"prego_id": "BTO:0000131", "rank": "12", "taxon_id": "NCBITaxon:51665", "taxon_label": "Aerococcus urinaeequi", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 155, "data": {"prego_id": "BTO:0000131", "rank": "13", "taxon_id": "NCBITaxon:525919", "taxon_label": "Anaerococcus prevotii DSM 20548", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 156, "data": {"prego_id": "BTO:0000131", "rank": "14", "taxon_id": "NCBITaxon:76759", "taxon_label": "Pseudomonas monteilii", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 157, "data": {"prego_id": "BTO:0000131", "rank": "15", "taxon_id": "NCBITaxon:83655", "taxon_label": "Leclercia adecarboxylata", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}] |
| ET6 | data/raw/prego_habitats.tsv; Physical TSV rows 306 | supports | [{"row": 306, "data": {"prego_id": "BTO:0000131", "ontology": "BTO", "biolink_category": "biolink:GrossAnatomicalStructure", "taxon_count": "15", "direct_assertion_count": "16", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms": "blood plasma&#124;blood plasmal&#124;blood plasmas&#124;plasma&#124;plasmal&#124;plasmas"}}] |
| ET7 | data/raw/ontology_terms.tsv; Physical TSV rows 133 | supports | [{"row": 133, "data": {"term_id": "BTO:0000131", "ontology": "BTO", "label": "blood plasma", "definition": "The fluid portion of the blood in which the particulate components are suspended.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}] |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000131/graph; BTO_0000131-graph.json | context_only | Typed outgoing relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0000131", "target": "http://purl.obolibrary.org/obo/BTO_0000089", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000131; BTO_0000131.json | context_only | Inspected current ID, label, active status and definition for scope; {"obo_id": "BTO:0000131", "label": "blood plasma", "is_obsolete": false} |
| EX3 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3968331/fullTextXML; PMC3968331.xml | context_only | Full genome announcement, DOI:10.1128/genomeA.00183-14, PMID:24675853: CECT8145 ingestion was studied for metabolic effects in C. elegans and obese rats; CBWX000000000 identifies the genome. This inspected article does not report plasma isolation. The original PREGO evidence is not recovered by reading this article. |
| EX4 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML; PMC8879827.xml | context_only | PREGO methods section 2.3, DOI:10.3390/microorganisms10020293, PMID:35208748: confidence-three BioProject associations connect assigned taxa to entities mined from linked abstracts. Such co-mention is not independently verified localization. |
| EX5 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1000935,1000936,1000937,1000938,1000939,1002339,1003201,1005704,1005705,1008452,1008453,102684,1028806,1032071,1035187,1035189,103855,1051654,106654,1069609,1069614,1069618,1069621,1069623,1069627,1073382,1094555,1120932,1121020,1121098,1121364,1122173,1122921,1122925,1122931,1122988,1123034,1219017,123899,1265311,1267000,1280,1283,1296,1304,1322345,1328,1329902,1336208,1341644,1402,1408438,1408440,1408452,1415606,1448136,147802,154288,1578,1601,1659,168808,1707330,171549,1718,1747,186802,203119,214092,220341,273075,287,29318,29394,306537,316407,32002,33010,33028,354242,38284,43770,46124,47885,47920,504,51665,525919,598660,61645,66228,717,732,76759,83655&amp;retmode=xml; taxonomy.xml | context_only | Every displayed ID was resolved, including current merged aliases; source labels are preserved, not falsely certified current preferred names. [{"id": "NCBITaxon:1322345", "source": "PREGO", "label": "Escherichia coli ATCC 25922", "current_id": "1322345", "current_name": "Escherichia coli ATCC 25922", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1415606", "source": "PREGO", "label": "Bifidobacterium animalis subsp. lactis CECT 8145", "current_id": "1415606", "current_name": "Bifidobacterium animalis subsp. lactis CECT 8145", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1718", "source": "PREGO", "label": "Corynebacterium glutamicum", "current_id": "1718", "current_name": "Corynebacterium glutamicum", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:203119", "source": "PREGO", "label": "Acetivibrio thermocellus ATCC 27405", "current_id": "203119", "current_name": "Acetivibrio thermocellus ATCC 27405", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:214092", "source": "PREGO", "label": "Yersinia pestis CO92", "current_id": "214092", "current_name": "Yersinia pestis CO92", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:273075", "source": "PREGO", "label": "Thermoplasma acidophilum DSM 1728", "current_id": "273075", "current_name": "Thermoplasma acidophilum DSM 1728", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:287", "source": "PREGO", "label": "Pseudomonas aeruginosa", "current_id": "287", "current_name": "Pseudomonas aeruginosa", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:316407", "source": "PREGO", "label": "Escherichia coli str. K-12 substr. W3110", "current_id": "316407", "current_name": "Escherichia coli str. K-12 substr. W3110", "rank": "no rank", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:32002", "source": "PREGO", "label": "Achromobacter denitrificans", "current_id": "32002", "current_name": "Achromobacter denitrificans", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:354242", "source": "PREGO", "label": "Campylobacter jejuni subsp. jejuni 81-176", "current_id": "354242", "current_name": "Campylobacter jejuni subsp. jejuni 81-176", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:47885", "source": "PREGO", "label": "Pseudomonas oryzihabitans", "current_id": "47885", "current_name": "Pseudomonas oryzihabitans", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:51665", "source": "PREGO", "label": "Aerococcus urinaeequi", "current_id": "51665", "current_name": "Aerococcus urinaeequi", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:525919", "source": "PREGO", "label": "Anaerococcus prevotii DSM 20548", "current_id": "525919", "current_name": "Anaerococcus prevotii DSM 20548", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:76759", "source": "PREGO", "label": "Pseudomonas monteilii", "current_id": "76759", "current_name": "Pseudomonas monteilii", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:83655", "source": "PREGO", "label": "Leclercia adecarboxylata", "current_id": "83655", "current_name": "Leclercia adecarboxylata", "rank": "species", "direct_match": true, "recognized_alias": true}] |
| ESEARCH | Local inputs and review archive; rg --no-ignore --hidden -l -F -e BTO:0000131 -e 'blood plasma' -e blood_plasma -e habitatmech:PREGO.cedc68741c curation history research reports data/raw build reviews | context_only | Exact TSV parsing and ignored-inclusive target/mint/label/slug search establish the bounded row inventory. Structured archive traversal found no predecessor; not every broad textual lead was inspected. |
| EAVAIL | Configured kg-microbe checkout; find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe -type f -path '*/prego/*' -name '*.tsv' | context_only | No prego-directory TSVs found in this configured checkout. The expected original pair exports could not be inspected; this is not global nonexistence. |

## Limits And Additional Notes

- Every historical specimen and original source pair has not been independently reidentified. Source counts are not prevalence, viability or characteristic presence.
- Configured label checks skip 2,061 no-adapter pairs and taxon labels; independent current NCBI lookup is recorded for displayed taxa.
- Full QC evidence is a verified remote run at the exact captured baseline, not a newly executed local QC. New review outputs require subsequent publication checks.
- iModulonDB is not applicable: no gene, regulator or expression-module assertion is made. No paid research was used.
- Original PREGO pair exports are unavailable in the configured checkout. Primary-paper witnesses cannot reconstruct every original pair or prove the extraction cause.
- Captured hashes were rechecked against both working bytes and the exact Git base; no scientific inputs were silently refreshed.
- Ignored-inclusive searches and parsed structured archive found no prior structured observation of this exact target. Legacy Markdown is a lead, not structured lineage.
- This immutable observation precedes separately authorized curation and does not claim repairs.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T145133Z-blood_plasma-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: blood plasma (BTO:0000131)'
started_at: '2026-10-15T14:33:26Z'
finished_at: '2026-10-15T14:51:33Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent assesses the target and evidence; not independent
    reviewer approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: The BTO plasma definition denotes the fluid component of blood; its part-of
  relation is correctly not emitted as subclass ancestry. Fifteen score-three PREGO
  associations are faithfully projected. The inspected CECT8145 genome article concerns
  probiotic ingestion and metabolic outcomes, not plasma isolation. Original pair
  evidence is unavailable, so this is a provisional localization-evidence concern,
  not proof that the strain can never occur in plasma.
source:
  git_revision: b558fd561286d1fe3ba133784776f7be1f9f49fb
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
    sha256: b01c55614780f2eba62e1dc7b47f30d40fb783fe388e75761ca2639769b9c5de
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 6d5cbfd0f5ad911fbb074ee8ec253625d1fa13d94117759b1f25a1cd2e6576bc
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 1e1c576daaee3c5055437ef42ba46363f5776210eef2e4182fe6fd3c87a7fe4d
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: a56f07a45fb743fb7b0e61f83ef70fa5ed61a3c892cfaf36e3428967c548dc5e
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: dfde49f64273cb94b4162170a5542c94880fa36015ccaac6edfa248820492a23
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
  - path: data/habitats/host_associated/blood_plasma.yaml
    sha256: c447fcdd7a29acad2e5014f4fc3e030ce8cb2315bc50994da7028c11a1f5235b
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
  - path: reports/yaml_record_review/20260922T014256Z-blood_plasma.md
    sha256: 1cf0e88e7089e9a2b090cc442ed826bb1a995930f4bc076355b14c9d2744a008
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
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
    role: context
targets:
- target_id: BTO:0000131
  path: data/habitats/host_associated/blood_plasma.yaml
  label: blood plasma
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
  description: Full scientific assessment of one exact target at b558fd561286d1fe3ba133784776f7be1f9f49fb.
  selection: One of the next 21 path-ordered unreviewed records, blood through bone
    marrow; this bundle assesses only this identifier.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - BTO:0000131
  exclusions:
  - target: Other records and export products
    reason: Parent context is not additional coverage. SSSOM/KGX readiness is not
      certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/blood_plasma.yaml
  exit_code: 0
  target_ids:
  - BTO:0000131
  summary: "Completed 2026-10-15T14:34:52Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/blood_plasma.yaml"
  scope_note: Individual ordinary schema; strict for all 21 selected records; remaining
    gates full-corpus as documented.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/blood.yaml data/habitats/host_associated/blood__070ce7aa.yaml
    data/habitats/host_associated/blood__5ca8064f.yaml data/habitats/host_associated/blood__5ef3f2f4.yaml
    data/habitats/host_associated/blood__c1b484fe.yaml data/habitats/host_associated/blood__d6f5ae05.yaml
    data/habitats/host_associated/blood_plasma.yaml data/habitats/host_associated/blood_plasma__00b70c6a.yaml
    data/habitats/host_associated/blood_serum.yaml data/habitats/host_associated/blood_vessel.yaml
    data/habitats/host_associated/bone.yaml data/habitats/host_associated/bone__169c3d9e.yaml
    data/habitats/host_associated/bone__234001be.yaml data/habitats/host_associated/bone__71064238.yaml
    data/habitats/host_associated/bone__8430e16e.yaml data/habitats/host_associated/bone__8d0df242.yaml
    data/habitats/host_associated/bone__b47efce2.yaml data/habitats/host_associated/bone_element.yaml
    data/habitats/host_associated/bone_marrow.yaml data/habitats/host_associated/bone_marrow__9387f1a6.yaml
    data/habitats/host_associated/bone_marrow__c1fc5dec.yaml
  exit_code: 0
  target_ids:
  - BTO:0000131
  summary: "Completed 2026-10-15T14:36:08Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/blood.yaml data/habitats/host_associated/blood__070ce7aa.yaml\
    \ data/habitats/host_associated/blood__5ca8064f.yaml data/habitats/host_associated/blood__5ef3f2f4.yaml\
    \ data/habitats/host_associated/blood__c1b484fe.yaml data/habitats/host_associated/blood__d6f5ae05.yaml\
    \ data/habitats/host_associated/blood_plasma.yaml data/habitats/host_associated/blood_plasma__00b70c6a.yaml\
    \ data/habitats/host_associated/blood_serum.yaml data/habitats/host_associated/blood_vessel.yaml\
    \ data/habitats/host_associated/bone.yaml data/habitats/host_associated/bone__169c3d9e.yaml\
    \ data/habitats/host_associated/bone__234001be.yaml data/habitats/host_associated/bone__71064238.yaml\
    \ data/habitats/host_associated/bone__8430e16e.yaml data/habitats/host_associated/bone__8d0df242.yaml\
    \ data/habitats/host_associated/bone__b47efce2.yaml data/habitats/host_associated/bone_element.yaml\
    \ data/habitats/host_associated/bone_marrow.yaml data/habitats/host_associated/bone_marrow__9387f1a6.yaml\
    \ data/habitats/host_associated/bone_marrow__c1fc5dec.yaml\nValidating 21 files\
    \ with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      21\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Individual ordinary schema; strict for all 21 selected records; remaining
    gates full-corpus as documented.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - BTO:0000131
  summary: 'Completed 2026-10-15T14:36:40Z. No issues found

    813 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Individual ordinary schema; strict for all 21 selected records; remaining
    gates full-corpus as documented.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - BTO:0000131
  summary: "Completed 2026-10-15T14:36:43Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Individual ordinary schema; strict for all 21 selected records; remaining
    gates full-corpus as documented.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - BTO:0000131
  summary: "Completed 2026-10-15T14:37:37Z. expected 3208 records, found 3208 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Individual ordinary schema; strict for all 21 selected records; remaining
    gates full-corpus as documented.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - BTO:0000131
  summary: "Completed 2026-10-15T14:37:45Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Individual ordinary schema; strict for all 21 selected records; remaining
    gates full-corpus as documented.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - BTO:0000131
  summary: "Completed 2026-10-15T14:38:11Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Individual ordinary schema; strict for all 21 selected records; remaining
    gates full-corpus as documented.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - BTO:0000131
  summary: "Completed 2026-10-15T14:39:21Z. id↔label correspondence summary:\n   \
    \       OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Individual ordinary schema; strict for all 21 selected records; remaining
    gates full-corpus as documented.
- check_id: CCI
  name: Exact-baseline full QC
  status: passed
  required: true
  command: gh run view 38748091185 --json status,conclusion,headSha,url,jobs
  exit_code: 0
  target_ids:
  - BTO:0000131
  summary: Verified 2026-10-15T14:33:14Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38748091185
  scope_note: Exact unchanged scientific input baseline; these new review outputs
    require later checks.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/blood_plasma.yaml
  locator: Entire target YAML
  accessed_at: '2026-10-15T14:51:33Z'
  support: supports
  summary: Full target read, including every source attestation, taxon, parent, parameter
    and history entry.
  snapshot_sha256: c447fcdd7a29acad2e5014f4fc3e030ce8cb2315bc50994da7028c11a1f5235b
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Strict ancestry and maintained-input ownership
  accessed_at: '2026-10-15T14:51:33Z'
  support: supports
  summary: Parent means strictly broader, not containing organ, body or system.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation, EnvironmentalParameter, CharacteristicTaxon
  accessed_at: '2026-10-15T14:51:33Z'
  support: supports
  summary: Source-to-record mapping contract; qualified parameters and observed associations
    are not universal conditions or characteristic presence.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed build_corpus and apply_decision routes
  accessed_at: '2026-10-15T14:51:33Z'
  support: supports
  summary: 'Whole generated document equality verified; source-specific resolutions:
    [{"mint": "habitatmech:PREGO.cedc68741c", "automatic": {"identifier": "BTO:0000131",
    "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded",
    "category": null, "reviewed": false, "decision": null}, "final": {"identifier":
    "BTO:0000131", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded",
    "category": null, "reviewed": false, "decision": null}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: Source projection
  accessed_at: '2026-10-15T14:51:33Z'
  support: supports
  summary: PREGO projects counts, scores, channels and ranked taxa without original
    pair citations.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/prego_habitat_taxa.tsv
  locator: Physical TSV rows 143,144,145,146,147,148,149,150,151,152,153,154,155,156,157
  accessed_at: '2026-10-15T14:51:33Z'
  support: supports
  summary: '[{"row": 143, "data": {"prego_id": "BTO:0000131", "rank": "1", "taxon_id":
    "NCBITaxon:1322345", "taxon_label": "Escherichia coli ATCC 25922", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 144, "data": {"prego_id": "BTO:0000131", "rank": "2", "taxon_id":
    "NCBITaxon:1415606", "taxon_label": "Bifidobacterium animalis subsp. lactis CECT
    8145", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates",
    "corroborated_by": ""}}, {"row": 145, "data": {"prego_id": "BTO:0000131", "rank":
    "3", "taxon_id": "NCBITaxon:1718", "taxon_label": "Corynebacterium glutamicum",
    "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates",
    "corroborated_by": ""}}, {"row": 146, "data": {"prego_id": "BTO:0000131", "rank":
    "4", "taxon_id": "NCBITaxon:203119", "taxon_label": "Acetivibrio thermocellus
    ATCC 27405", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates",
    "corroborated_by": ""}}, {"row": 147, "data": {"prego_id": "BTO:0000131", "rank":
    "5", "taxon_id": "NCBITaxon:214092", "taxon_label": "Yersinia pestis CO92", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 148, "data": {"prego_id": "BTO:0000131", "rank": "6", "taxon_id":
    "NCBITaxon:273075", "taxon_label": "Thermoplasma acidophilum DSM 1728", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 149, "data": {"prego_id": "BTO:0000131", "rank": "7", "taxon_id":
    "NCBITaxon:287", "taxon_label": "Pseudomonas aeruginosa", "prego_score": "3",
    "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 150, "data": {"prego_id": "BTO:0000131", "rank": "8", "taxon_id":
    "NCBITaxon:316407", "taxon_label": "Escherichia coli str. K-12 substr. W3110",
    "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates",
    "corroborated_by": ""}}, {"row": 151, "data": {"prego_id": "BTO:0000131", "rank":
    "9", "taxon_id": "NCBITaxon:32002", "taxon_label": "Achromobacter denitrificans",
    "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates",
    "corroborated_by": ""}}, {"row": 152, "data": {"prego_id": "BTO:0000131", "rank":
    "10", "taxon_id": "NCBITaxon:354242", "taxon_label": "Campylobacter jejuni subsp.
    jejuni 81-176", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates",
    "corroborated_by": ""}}, {"row": 153, "data": {"prego_id": "BTO:0000131", "rank":
    "11", "taxon_id": "NCBITaxon:47885", "taxon_label": "Pseudomonas oryzihabitans",
    "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates",
    "corroborated_by": ""}}, {"row": 154, "data": {"prego_id": "BTO:0000131", "rank":
    "12", "taxon_id": "NCBITaxon:51665", "taxon_label": "Aerococcus urinaeequi", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 155, "data": {"prego_id": "BTO:0000131", "rank": "13", "taxon_id":
    "NCBITaxon:525919", "taxon_label": "Anaerococcus prevotii DSM 20548", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 156, "data": {"prego_id": "BTO:0000131", "rank": "14", "taxon_id":
    "NCBITaxon:76759", "taxon_label": "Pseudomonas monteilii", "prego_score": "3",
    "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 157, "data": {"prego_id": "BTO:0000131", "rank": "15", "taxon_id":
    "NCBITaxon:83655", "taxon_label": "Leclercia adecarboxylata", "prego_score": "3",
    "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}]'
  snapshot_sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
- evidence_id: ET6
  kind: database
  reference: data/raw/prego_habitats.tsv
  locator: Physical TSV rows 306
  accessed_at: '2026-10-15T14:51:33Z'
  support: supports
  summary: '[{"row": 306, "data": {"prego_id": "BTO:0000131", "ontology": "BTO", "biolink_category":
    "biolink:GrossAnatomicalStructure", "taxon_count": "15", "direct_assertion_count":
    "16", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms":
    "blood plasma|blood plasmal|blood plasmas|plasma|plasmal|plasmas"}}]'
  snapshot_sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
- evidence_id: ET7
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 133
  accessed_at: '2026-10-15T14:51:33Z'
  support: supports
  summary: '[{"row": 133, "data": {"term_id": "BTO:0000131", "ontology": "BTO", "label":
    "blood plasma", "definition": "The fluid portion of the blood in which the particulate
    components are suspended.", "synonyms": "", "deprecated": "", "directly_referenced":
    "TRUE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EX1
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000131/graph
  locator: BTO_0000131-graph.json
  accessed_at: '2026-10-15T14:36:15Z'
  support: context_only
  summary: 'Typed outgoing relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0000131",
    "target": "http://purl.obolibrary.org/obo/BTO_0000089", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 672534b38b44746f11e81bdb8b6f9c565e0bea933430b2c4b9a7d7d25e53d85b
- evidence_id: EX2
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000131
  locator: BTO_0000131.json
  accessed_at: '2026-10-15T14:36:15Z'
  support: context_only
  summary: 'Inspected current ID, label, active status and definition for scope; {"obo_id":
    "BTO:0000131", "label": "blood plasma", "is_obsolete": false}'
  snapshot_sha256: 1014f7a2d2209ce72a67448e8475903400a6dc613fb4365e4cde87c05632a00f
- evidence_id: EX3
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3968331/fullTextXML
  locator: PMC3968331.xml
  accessed_at: '2026-10-15T14:40:11Z'
  support: context_only
  summary: 'Full genome announcement, DOI:10.1128/genomeA.00183-14, PMID:24675853:
    CECT8145 ingestion was studied for metabolic effects in C. elegans and obese rats;
    CBWX000000000 identifies the genome. This inspected article does not report plasma
    isolation. The original PREGO evidence is not recovered by reading this article.'
  snapshot_sha256: ce58a30cc5ef1693ffc19af5e4c714013c14b11fbbcc2118d5a3d19d45dd9dd3
- evidence_id: EX4
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML
  locator: PMC8879827.xml
  accessed_at: '2026-10-15T14:40:13Z'
  support: context_only
  summary: 'PREGO methods section 2.3, DOI:10.3390/microorganisms10020293, PMID:35208748:
    confidence-three BioProject associations connect assigned taxa to entities mined
    from linked abstracts. Such co-mention is not independently verified localization.'
  snapshot_sha256: 375f0fde4d07bb823cb9106aa4567bc0ef03c2866af0b2a7740b543f50687c25
- evidence_id: EX5
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1000935,1000936,1000937,1000938,1000939,1002339,1003201,1005704,1005705,1008452,1008453,102684,1028806,1032071,1035187,1035189,103855,1051654,106654,1069609,1069614,1069618,1069621,1069623,1069627,1073382,1094555,1120932,1121020,1121098,1121364,1122173,1122921,1122925,1122931,1122988,1123034,1219017,123899,1265311,1267000,1280,1283,1296,1304,1322345,1328,1329902,1336208,1341644,1402,1408438,1408440,1408452,1415606,1448136,147802,154288,1578,1601,1659,168808,1707330,171549,1718,1747,186802,203119,214092,220341,273075,287,29318,29394,306537,316407,32002,33010,33028,354242,38284,43770,46124,47885,47920,504,51665,525919,598660,61645,66228,717,732,76759,83655&retmode=xml
  locator: taxonomy.xml
  accessed_at: '2026-10-15T14:36:36Z'
  support: context_only
  summary: 'Every displayed ID was resolved, including current merged aliases; source
    labels are preserved, not falsely certified current preferred names. [{"id": "NCBITaxon:1322345",
    "source": "PREGO", "label": "Escherichia coli ATCC 25922", "current_id": "1322345",
    "current_name": "Escherichia coli ATCC 25922", "rank": "strain", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:1415606", "source": "PREGO",
    "label": "Bifidobacterium animalis subsp. lactis CECT 8145", "current_id": "1415606",
    "current_name": "Bifidobacterium animalis subsp. lactis CECT 8145", "rank": "strain",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1718", "source":
    "PREGO", "label": "Corynebacterium glutamicum", "current_id": "1718", "current_name":
    "Corynebacterium glutamicum", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:203119", "source": "PREGO", "label": "Acetivibrio thermocellus
    ATCC 27405", "current_id": "203119", "current_name": "Acetivibrio thermocellus
    ATCC 27405", "rank": "strain", "direct_match": true, "recognized_alias": true},
    {"id": "NCBITaxon:214092", "source": "PREGO", "label": "Yersinia pestis CO92",
    "current_id": "214092", "current_name": "Yersinia pestis CO92", "rank": "strain",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:273075", "source":
    "PREGO", "label": "Thermoplasma acidophilum DSM 1728", "current_id": "273075",
    "current_name": "Thermoplasma acidophilum DSM 1728", "rank": "strain", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:287", "source": "PREGO", "label":
    "Pseudomonas aeruginosa", "current_id": "287", "current_name": "Pseudomonas aeruginosa",
    "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:316407",
    "source": "PREGO", "label": "Escherichia coli str. K-12 substr. W3110", "current_id":
    "316407", "current_name": "Escherichia coli str. K-12 substr. W3110", "rank":
    "no rank", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:32002",
    "source": "PREGO", "label": "Achromobacter denitrificans", "current_id": "32002",
    "current_name": "Achromobacter denitrificans", "rank": "species", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:354242", "source": "PREGO",
    "label": "Campylobacter jejuni subsp. jejuni 81-176", "current_id": "354242",
    "current_name": "Campylobacter jejuni subsp. jejuni 81-176", "rank": "strain",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:47885", "source":
    "PREGO", "label": "Pseudomonas oryzihabitans", "current_id": "47885", "current_name":
    "Pseudomonas oryzihabitans", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:51665", "source": "PREGO", "label": "Aerococcus urinaeequi",
    "current_id": "51665", "current_name": "Aerococcus urinaeequi", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:525919", "source":
    "PREGO", "label": "Anaerococcus prevotii DSM 20548", "current_id": "525919", "current_name":
    "Anaerococcus prevotii DSM 20548", "rank": "strain", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:76759", "source": "PREGO", "label": "Pseudomonas monteilii",
    "current_id": "76759", "current_name": "Pseudomonas monteilii", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:83655", "source":
    "PREGO", "label": "Leclercia adecarboxylata", "current_id": "83655", "current_name":
    "Leclercia adecarboxylata", "rank": "species", "direct_match": true, "recognized_alias":
    true}]'
  snapshot_sha256: 69f4f3dd5dd6e1a629f412ced9f307fe813a670f8088da1d3ac7471ed7b109bb
- evidence_id: ESEARCH
  kind: search
  reference: Local inputs and review archive
  locator: rg --no-ignore --hidden -l -F -e BTO:0000131 -e 'blood plasma' -e blood_plasma
    -e habitatmech:PREGO.cedc68741c curation history research reports data/raw build
    reviews
  accessed_at: '2026-10-15T14:33:45Z'
  support: context_only
  summary: Exact TSV parsing and ignored-inclusive target/mint/label/slug search establish
    the bounded row inventory. Structured archive traversal found no predecessor;
    not every broad textual lead was inspected.
  search_scope: curation, history, research, reports, data/raw, build, reviews including
    ignored/hidden files; all structured review.yaml files parsed.
- evidence_id: EAVAIL
  kind: search
  reference: Configured kg-microbe checkout
  locator: find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe
    -type f -path '*/prego/*' -name '*.tsv'
  accessed_at: '2026-10-15T14:33:48Z'
  support: context_only
  summary: No prego-directory TSVs found in this configured checkout. The expected
    original pair exports could not be inspected; this is not global nonexistence.
  search_scope: find across the entire configured checkout, including ignored and
    hidden files.
assessments:
- assessment_id: A1
  area: identity
  topic: Identity and hierarchy
  outcome: supported
  summary: The BTO plasma definition denotes the fluid component of blood; its part-of
    relation is correctly not emitted as subclass ancestry. Fifteen score-three PREGO
    associations are faithfully projected. The inspected CECT8145 genome article concerns
    probiotic ingestion and metabolic outcomes, not plasma isolation. Original pair
    evidence is unavailable, so this is a provisional localization-evidence concern,
    not proof that the strain can never occur in plasma.
  target_ids:
  - BTO:0000131
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
- assessment_id: A2
  area: quantity
  topic: Frozen source units, ranks and parameters
  outcome: supported
  summary: 'Count/unit, first GOLD node, channel, score and displayed taxon ranks/labels
    reproduce exact source rows. Verification: [{"source": "PREGO", "count": 15, "unit":
    "TAXON"}]. Zero counts are omitted, never interpreted as absence. Side-table biosamples/studies
    and MIxS slots are not added to tree ORGANISM counts.'
  target_ids:
  - BTO:0000131
  evidence_ids:
  - E1
  - ESEED
  - EEXTRACT
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
- assessment_id: A3
  area: evidence
  topic: Scientific support and source limits
  outcome: concern
  summary: The BTO plasma definition denotes the fluid component of blood; its part-of
    relation is correctly not emitted as subclass ancestry. Fifteen score-three PREGO
    associations are faithfully projected. The inspected CECT8145 genome article concerns
    probiotic ingestion and metabolic outcomes, not plasma isolation. Original pair
    evidence is unavailable, so this is a provisional localization-evidence concern,
    not proof that the strain can never occur in plasma.
  target_ids:
  - BTO:0000131
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
- assessment_id: A4
  area: completeness
  topic: Native status and optional assertions
  outcome: supported
  summary: Executed routes reproduce EXACT/SEEDED. No causal edge or is_characteristic=true
    assertion is made. Optional absent fields and SEEDED status alone are not scientific
    defects; this review does not promote native status.
  target_ids:
  - BTO:0000131
  evidence_ids:
  - E1
  - ERULE
  - ESEED
- assessment_id: A5
  area: schema
  topic: Deterministic native gates
  outcome: supported
  summary: Schema, strict, history, provenance, 3,208-record reproduction, causal,
    term-request, configured-label and exact-baseline full QC checks passed; these
    prove fidelity, not biological truth.
  target_ids:
  - BTO:0000131
  evidence_ids:
  - E1
  - ERULE
findings:
- finding_id: F1
  issue_key: blood-plasma-prego-pair-scope
  category: evidence
  severity: major
  status: open
  certainty: provisional
  title: Original pair evidence is needed to establish site localization
  description: The BTO plasma definition denotes the fluid component of blood; its
    part-of relation is correctly not emitted as subclass ancestry. Fifteen score-three
    PREGO associations are faithfully projected. The inspected CECT8145 genome article
    concerns probiotic ingestion and metabolic outcomes, not plasma isolation. Original
    pair evidence is unavailable, so this is a provisional localization-evidence concern,
    not proof that the strain can never occur in plasma. Recover manifest-matching
    pair citations, distinguish patient/outcome context from sampled site, and correct
    or qualify only supported mismatches through a governed source contract. Do not
    delete taxa or decrement totals by hand.
  target_ids:
  - BTO:0000131
  field_paths:
  - characteristic_taxa
  - source_attestations
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EAVAIL
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/MANIFEST.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or source-evidence claim;
    deterministic validity does not establish scientific support.
  external_issues: []
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - BTO:0000131
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/MANIFEST.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  description: The BTO plasma definition denotes the fluid component of blood; its
    part-of relation is correctly not emitted as subclass ancestry. Fifteen score-three
    PREGO associations are faithfully projected. The inspected CECT8145 genome article
    concerns probiotic ingestion and metabolic outcomes, not plasma isolation. Original
    pair evidence is unavailable, so this is a provisional localization-evidence concern,
    not proof that the strain can never occur in plasma. Recover manifest-matching
    pair citations, distinguish patient/outcome context from sampled site, and correct
    or qualify only supported mismatches through a governed source contract. Do not
    delete taxa or decrement totals by hand. No repair is performed by this review.
  generator: Controlled source refresh when required, then just seed, guarded just
    seed-canary, just seed-apply, and dependent term-request/map/site/redirect regeneration.
  acceptance_checks:
  - Regress the exact reported claim and preserve independently valid identifiers,
    source counts/units, raw provenance, native status and history. Do not change
    source totals by hand.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
limitations:
- Every historical specimen and original source pair has not been independently reidentified.
  Source counts are not prevalence, viability or characteristic presence.
- Configured label checks skip 2,061 no-adapter pairs and taxon labels; independent
  current NCBI lookup is recorded for displayed taxa.
- Full QC evidence is a verified remote run at the exact captured baseline, not a
  newly executed local QC. New review outputs require subsequent publication checks.
- 'iModulonDB is not applicable: no gene, regulator or expression-module assertion
  is made. No paid research was used.'
- Original PREGO pair exports are unavailable in the configured checkout. Primary-paper
  witnesses cannot reconstruct every original pair or prove the extraction cause.
notes:
- Captured hashes were rechecked against both working bytes and the exact Git base;
  no scientific inputs were silently refreshed.
- Ignored-inclusive searches and parsed structured archive found no prior structured
  observation of this exact target. Legacy Markdown is a lead, not structured lineage.
- This immutable observation precedes separately authorized curation and does not
  claim repairs.
tags:
- individual-scientific-review
- host-associated
```
