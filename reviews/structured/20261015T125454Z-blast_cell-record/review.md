# Record review: blast cell (BTO:0000125)

- Review: 20261015T125454Z-blast_cell-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T12:40:55Z
- Finished UTC: 2026-10-15T12:54:54Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The BTO blast-cell identity is current; its blood relation is part-of and correctly is not emitted as subclass ancestry. PREGO faithfully emits eighteen score-three associations, but original pair citations are unavailable and the inspected DSM9442 source concerns oil-reservoir thermophiles. This warrants evidence recovery, not unsupported deletion or a claim that BLAST caused the association.

## Scope And Provenance

Scientific review of one exact target at 68ceabb7039a537f65be44ac6aaa913116a154f5.

Selection: First seven records in the prepared next-twenty path-ordered cohort; this bundle assesses exactly one resolved identifier.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 68ceabb7039a537f65be44ac6aaa913116a154f5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0000125 | data/habitats/host_associated/blast_cell.yaml | generated | blast cell |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0000125 | Completed 2026-10-15T12:40:57Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/blast_cell.yaml |
| validate-strict | passed | True | BTO:0000125 | Completed 2026-10-15T12:41:35Z. uv run python scripts/validate_strict.py data/habitats/host_associated/bl_3_cell.yaml data/habitats/host_associated/bladder.yaml data/habitats/host_associated/bladder__9a6dd80c.yaml data/habitats/host_associated/bladder_stone.yaml data/habitats/host_associated/blade.yaml data/habitats/host_associated/blade__f83a64ca.yaml data/habitats/host_associated/blast_cell.yaml data/habitats/host_associated/blood.yaml data/habitats/host_associated/blood__070ce7aa.yaml data/habitats/host_associated/blood__5ca8064f.yaml data/habitats/host_associated/blood__5ef3f2f4.yaml data/habitats/host_associated/blood__c1b484fe.yaml data/habitats/host_associated/blood__d6f5ae05.yaml data/habitats/host_associated/blood_plasma.yaml data/habitats/host_associated/blood_plasma__00b70c6a.yaml data/habitats/host_associated/blood_serum.yaml data/habitats/host_associated/blood_vessel.yaml data/habitats/host_associated/bone.yaml data/habitats/host_associated/bone__169c3d9e.yaml data/habitats/host_associated/bone__234001be.yaml<br>Validating 20 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      20<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | BTO:0000125 | Completed 2026-10-15T12:41:43Z. No issues found<br>808 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | BTO:0000125 | Completed 2026-10-15T12:41:44Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | BTO:0000125 | Completed 2026-10-15T12:41:58Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | BTO:0000125 | Completed 2026-10-15T12:42:02Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | BTO:0000125 | Completed 2026-10-15T12:42:18Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | BTO:0000125 | Completed 2026-10-15T12:42:59Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-revision baseline full QC | passed | True | BTO:0000125 | Verified 2026-10-15T12:40:46Z: https://github.com/CultureBotAI/HabitatMech/actions/runs/38733485444 |

## Scientific And Domain Assessments

### Native validation and reproduction

schema: supported. Targets: BTO:0000125.

Schema, strict, history, provenance, 3,208-record reproduction, causal overlays, term requests and configured labels passed. These establish deterministic fidelity, not scientific support.

### Identity, hierarchy and nomenclature

identity: supported. Targets: BTO:0000125.

The BTO blast-cell identity is current; its blood relation is part-of and correctly is not emitted as subclass ancestry. PREGO faithfully emits eighteen score-three associations, but original pair citations are unavailable and the inspected DSM9442 source concerns oil-reservoir thermophiles. This warrants evidence recovery, not unsupported deletion or a claim that BLAST caused the association.

### Source count, unit and ranking

quantity: supported. Targets: BTO:0000125.

Exact source projections retain [{"source": "PREGO", "source_id": "BTO:0000125", "source_label": "blast cell", "assertion_count": 18, "assertion_unit": "TAXON", "score": 3.0, "evidence_channels": "annotated_genomes_isolates"}]. All 18 displayed taxa were resolved against current NCBI IDs/labels. Ranks and candidate pools are source-specific; unlike units are never summed.

### Native status and optional fields

completeness: supported. Targets: BTO:0000125.

Executed source decisions reproduce EXACT/SEEDED. No causal mechanism or is_characteristic assertion is present. Missing optional fields or SEEDED status are not automatic scientific defects.

## Findings

### F1: Blast-cell associations lack recoverable localization evidence

major / open / provisional; issue key: blast-cell-prego-pair-scope.

Recover the exact PREGO evidence for the eighteen BTO:0000125 taxon pairs, beginning with NCBITaxon:1123383/DSM9442. Distinguish blood-cell localization from bioinformatics or other abstract context. A BLAST lexical collision is only a hypothesis, not an established cause. Preserve source provenance and counts; any qualified displayed pool needs a maintained source contract and exact-pair regressions.

## Recommended Actions And Acceptance Checks

### ACT1

Recover the exact PREGO evidence for the eighteen BTO:0000125 taxon pairs, beginning with NCBITaxon:1123383/DSM9442. Distinguish blood-cell localization from bioinformatics or other abstract context. A BLAST lexical collision is only a hypothesis, not an established cause. Preserve source provenance and counts; any qualified displayed pool needs a maintained source contract and exact-pair regressions. No repair is performed by this review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history. Do not change source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/blast_cell.yaml; Entire target YAML | supports | Read the full target including source paths, taxa, hierarchy and history. |
| ERULE | docs/CURATION.md; Identity, broader-parent and ownership rules | supports | Context, containment and whole-host identity differ from strictly broader habitat ancestry. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation and CharacteristicTaxon | supports | Mapping endpoints, assertion units and association versus characteristic-presence semantics. |
| ESEED | src/habitatmech/seed.py; Executed native source resolution | supports | Exact routes: [{"source": "PREGO", "mint": "habitatmech:PREGO.35c7ff17db", "automatic": {"identifier": "BTO:0000125", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "BTO:0000125", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}}] |
| EEXTRACT | src/habitatmech/extract.py; extract_prego | supports | Projection preserves distinct-taxon totals and score/channel ranking but not original pair citations. |
| ET5 | data/raw/prego_habitat_taxa.tsv; Physical TSV rows 113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130 | supports | [{"row": 113, "data": {"prego_id": "BTO:0000125", "rank": "1", "taxon_id": "NCBITaxon:1123383", "taxon_label": "Pseudothermotoga elfii DSM 9442 = NBRC 107921", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 114, "data": {"prego_id": "BTO:0000125", "rank": "2", "taxon_id": "NCBITaxon:1123384", "taxon_label": "Pseudothermotoga hypogea DSM 11164 = NBRC 106472", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 115, "data": {"prego_id": "BTO:0000125", "rank": "3", "taxon_id": "NCBITaxon:1189612", "taxon_label": "Indibacter alkaliphilus LW1", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 116, "data": {"prego_id": "BTO:0000125", "rank": "4", "taxon_id": "NCBITaxon:1322346", "taxon_label": "Glaesserella parasuis ZJ0906", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 117, "data": {"prego_id": "BTO:0000125", "rank": "5", "taxon_id": "NCBITaxon:1408159", "taxon_label": "Pseudothermotoga caldifontis AZM44c09", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 118, "data": {"prego_id": "BTO:0000125", "rank": "6", "taxon_id": "NCBITaxon:1408160", "taxon_label": "Thermotoga profunda AZM34c06", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 119, "data": {"prego_id": "BTO:0000125", "rank": "7", "taxon_id": "NCBITaxon:1497681", "taxon_label": "Paenilisteria newyorkensis", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 120, "data": {"prego_id": "BTO:0000125", "rank": "8", "taxon_id": "NCBITaxon:1552123", "taxon_label": "Listeria booriae", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 121, "data": {"prego_id": "BTO:0000125", "rank": "9", "taxon_id": "NCBITaxon:1585974", "taxon_label": "Beduini massiliensis", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 122, "data": {"prego_id": "BTO:0000125", "rank": "10", "taxon_id": "NCBITaxon:187452", "taxon_label": "Pediococcus claussenii", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 123, "data": {"prego_id": "BTO:0000125", "rank": "11", "taxon_id": "NCBITaxon:240427", "taxon_label": "Secundilactobacillus paracollinoides", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 124, "data": {"prego_id": "BTO:0000125", "rank": "12", "taxon_id": "NCBITaxon:375175", "taxon_label": "Loigolactobacillus backii", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 125, "data": {"prego_id": "BTO:0000125", "rank": "13", "taxon_id": "NCBITaxon:478010", "taxon_label": "Microterricola pindariensis", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 126, "data": {"prego_id": "BTO:0000125", "rank": "14", "taxon_id": "NCBITaxon:51663", "taxon_label": "Pediococcus damnosus", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 127, "data": {"prego_id": "BTO:0000125", "rank": "15", "taxon_id": "NCBITaxon:53444", "taxon_label": "Fructilactobacillus lindneri", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 128, "data": {"prego_id": "BTO:0000125", "rank": "16", "taxon_id": "NCBITaxon:562", "taxon_label": "Escherichia coli", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 129, "data": {"prego_id": "BTO:0000125", "rank": "17", "taxon_id": "NCBITaxon:582", "taxon_label": "Morganella morganii", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 130, "data": {"prego_id": "BTO:0000125", "rank": "18", "taxon_id": "NCBITaxon:758793", "taxon_label": "Caballeronia insecticola", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}] |
| ET6 | data/raw/prego_habitats.tsv; Physical TSV rows 294 | supports | [{"row": 294, "data": {"prego_id": "BTO:0000125", "ontology": "BTO", "biolink_category": "biolink:GrossAnatomicalStructure", "taxon_count": "18", "direct_assertion_count": "18", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms": "blast&#124;blast cell&#124;blast cells&#124;blastic&#124;blasts&#124;hematoblast&#124;hematoblastic&#124;hematoblasts&#124;hematocytoblast&#124;hematocytoblastic&#124;hematocytoblasts&#124;hemocytoblast&#124;hemocytoblastic&#124;hemocytoblasts"}}] |
| ET7 | data/raw/ontology_terms.tsv; Physical TSV rows 127 | supports | [{"row": 127, "data": {"term_id": "BTO:0000125", "ontology": "BTO", "label": "blast cell", "definition": "In the monophyletic theory, the least differentiated, totipotential blood cell without commitment as to its particular series, from which all blood cells are derived, preceding a stem cell.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}] |
| EL8 | reports/yaml_record_review/20260921T234045Z-blast_cell.md; Historical complete review | supports | Read as a source/issue lead. Current severity and verdict are reassessed independently; legacy prose does not close or create structured lineage. |
| EX9 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000125/graph; BTO_0000125-graph.json | context_only | Inspected outgoing typed ontology relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0000125", "target": "http://purl.obolibrary.org/obo/BTO_0000089", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX10 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000125?lang=en; BTO_0000125.json | context_only | Inspected current identifier, label, active status and full definition for the scope assessment: {"obo_id": "BTO:0000125", "label": "blast cell", "is_obsolete": false} |
| EX11 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10057702/fullTextXML; PMC10057702.xml | context_only | Primary methods/abstract, PMID:36985346, DOI:10.3390/microorganisms11030773: Pseudothermotoga elfii DSM9442 is an oil-well isolate grown anaerobically at 65 C in pressure experiments. This contrasts with a blood-cell habitat assertion. It is not the recovered PREGO pair citation and cannot establish the cause of an extraction or exclude other experimental contexts. |
| EX12 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML; PMC8879827.xml | context_only | PREGO methods section 2.3, PMID:35208748, DOI:10.3390/microorganisms10020293: genome-sequencing BioProject taxa are linked by mining associated abstracts; confidence three of five does not independently establish physical localization. |
| EX13 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1123383,1123384,1189612,1206108,1282,1286329,1286330,1286331,1286332,1286333,1286334,1286335,1286336,1286337,1286338,1286339,1286340,1286341,1286342,1286343,1286344,1286345,1286346,1286347,1286348,1286350,1286351,1286352,1286353,1322346,1408159,1408160,1497681,1552123,1585974,187452,240427,2702,375175,43771,478010,504474,508451,51663,53444,562,574375,582,588,758793,827&amp;retmode=xml; taxonomy.xml | context_only | All displayed taxon identifiers and labels resolve to current NCBI identities: [{"record_id": "1123383", "current_id": "1123383", "record_label": "Pseudothermotoga elfii DSM 9442 = NBRC 107921", "current_label": "Pseudothermotoga elfii DSM 9442 = NBRC 107921", "rank": "strain"}, {"record_id": "1123384", "current_id": "1123384", "record_label": "Pseudothermotoga hypogea DSM 11164 = NBRC 106472", "current_label": "Pseudothermotoga hypogea DSM 11164 = NBRC 106472", "rank": "strain"}, {"record_id": "1189612", "current_id": "1189612", "record_label": "Indibacter alkaliphilus LW1", "current_label": "Indibacter alkaliphilus LW1", "rank": "strain"}, {"record_id": "1322346", "current_id": "1322346", "record_label": "Glaesserella parasuis ZJ0906", "current_label": "Glaesserella parasuis ZJ0906", "rank": "strain"}, {"record_id": "1408159", "current_id": "1408159", "record_label": "Pseudothermotoga caldifontis AZM44c09", "current_label": "Pseudothermotoga caldifontis AZM44c09", "rank": "strain"}, {"record_id": "1408160", "current_id": "1408160", "record_label": "Thermotoga profunda AZM34c06", "current_label": "Thermotoga profunda AZM34c06", "rank": "strain"}, {"record_id": "1497681", "current_id": "1497681", "record_label": "Paenilisteria newyorkensis", "current_label": "Paenilisteria newyorkensis", "rank": "species"}, {"record_id": "1552123", "current_id": "1552123", "record_label": "Listeria booriae", "current_label": "Listeria booriae", "rank": "species"}, {"record_id": "1585974", "current_id": "1585974", "record_label": "Beduini massiliensis", "current_label": "Beduini massiliensis", "rank": "species"}, {"record_id": "187452", "current_id": "187452", "record_label": "Pediococcus claussenii", "current_label": "Pediococcus claussenii", "rank": "species"}, {"record_id": "240427", "current_id": "240427", "record_label": "Secundilactobacillus paracollinoides", "current_label": "Secundilactobacillus paracollinoides", "rank": "species"}, {"record_id": "375175", "current_id": "375175", "record_label": "Loigolactobacillus backii", "current_label": "Loigolactobacillus backii", "rank": "species"}, {"record_id": "478010", "current_id": "478010", "record_label": "Microterricola pindariensis", "current_label": "Microterricola pindariensis", "rank": "species"}, {"record_id": "51663", "current_id": "51663", "record_label": "Pediococcus damnosus", "current_label": "Pediococcus damnosus", "rank": "species"}, {"record_id": "53444", "current_id": "53444", "record_label": "Fructilactobacillus lindneri", "current_label": "Fructilactobacillus lindneri", "rank": "species"}, {"record_id": "562", "current_id": "562", "record_label": "Escherichia coli", "current_label": "Escherichia coli", "rank": "species"}, {"record_id": "582", "current_id": "582", "record_label": "Morganella morganii", "current_label": "Morganella morganii", "rank": "species"}, {"record_id": "758793", "current_id": "758793", "record_label": "Caballeronia insecticola", "current_label": "Caballeronia insecticola", "rank": "species"}] |
| ESEARCH | Local maintained inputs and structured archive; rg --no-ignore --hidden -l -F -e BTO:0000125 -e 'blast cell' -e blast_cell -e habitatmech:PREGO.35c7ff17db curation history research reports data/raw build reviews | context_only | Ignored-inclusive search plus exact TSV parsing identified the stated source rows and no structured predecessor. |
| EPREGOSEARCH | Configured kg-microbe checkout; find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe -type f -path '*/prego/*' -name '*.tsv' | context_only | No PREGO-directory TSV payload found in this configured checkout. Committed HabitatMech projections are present; no global/upstream absence claim is made. |

## Limits And Additional Notes

- Every historical specimen and original PREGO pair has not been independently reidentified. Counts/scores/ranks are not prevalence, viability or characteristic presence.
- Configured label checks skip 2,061 pairs without adapters; deterministic validity does not certify biological semantics.
- Full baseline QC is verified remote evidence at the captured revision, not a new local execution. Post-save archive and publication gates are subsequent.
- iModulonDB is not applicable: the target asserts no gene, regulator or expression module. No paid research was performed.
- Original PREGO pair evidence was not recovered. Source-specific publications support only their stated strain/site comparisons, not all retained associations or a demonstrated extraction cause.
- All captured local input hashes were rechecked against both the working tree and exact Git revision. No input bytes were silently refreshed.
- Ignored-inclusive archive traversal found no structured predecessor for this target; legacy Markdown is context, not independent approval or successor lineage.
- This observation precedes separately authorized curation/publication and does not claim a repair.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T125454Z-blast_cell-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: blast cell (BTO:0000125)'
started_at: '2026-10-15T12:40:55Z'
finished_at: '2026-10-15T12:54:54Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent inspected the record and evidence; not independent
    human or second-agent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: The BTO blast-cell identity is current; its blood relation is part-of and
  correctly is not emitted as subclass ancestry. PREGO faithfully emits eighteen score-three
  associations, but original pair citations are unavailable and the inspected DSM9442
  source concerns oil-reservoir thermophiles. This warrants evidence recovery, not
  unsupported deletion or a claim that BLAST caused the association.
source:
  git_revision: 68ceabb7039a537f65be44ac6aaa913116a154f5
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
    sha256: ca42d86b6040df1c0c6e6ed36573bb51975a5e8daade262113bce547f1b6fd8b
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 6d5cbfd0f5ad911fbb074ee8ec253625d1fa13d94117759b1f25a1cd2e6576bc
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: a92f9003cc5f57c397ab5118474318f216077a8e9f90564d21dfa8089477a2eb
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
  - path: data/habitats/host_associated/blast_cell.yaml
    sha256: a26f91cbdfd1a16aa0f4024e87e3895523f3df61616646472c29bd90e7afa7f1
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
  - path: reports/yaml_record_review/20260921T234045Z-blast_cell.md
    sha256: 56273ad13c9d8ff8be52d8b4fc6fcc5e09b055b68be7dc7279f335e2a81a3115
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
- target_id: BTO:0000125
  path: data/habitats/host_associated/blast_cell.yaml
  label: blast cell
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
  description: Scientific review of one exact target at 68ceabb7039a537f65be44ac6aaa913116a154f5.
  selection: First seven records in the prepared next-twenty path-ordered cohort;
    this bundle assesses exactly one resolved identifier.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - BTO:0000125
  exclusions:
  - target: Other records and SSSOM/KGX products
    reason: Parent context is not additional reviewed coverage. Export readiness is
      not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/blast_cell.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000125
  summary: "Completed 2026-10-15T12:40:57Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/blast_cell.yaml"
  scope_note: Individual schema; strict run includes all twenty prepared targets;
    other gates are full-corpus as documented.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/bl_3_cell.yaml data/habitats/host_associated/bladder.yaml
    data/habitats/host_associated/bladder__9a6dd80c.yaml data/habitats/host_associated/bladder_stone.yaml
    data/habitats/host_associated/blade.yaml data/habitats/host_associated/blade__f83a64ca.yaml
    data/habitats/host_associated/blast_cell.yaml data/habitats/host_associated/blood.yaml
    data/habitats/host_associated/blood__070ce7aa.yaml data/habitats/host_associated/blood__5ca8064f.yaml
    data/habitats/host_associated/blood__5ef3f2f4.yaml data/habitats/host_associated/blood__c1b484fe.yaml
    data/habitats/host_associated/blood__d6f5ae05.yaml data/habitats/host_associated/blood_plasma.yaml
    data/habitats/host_associated/blood_plasma__00b70c6a.yaml data/habitats/host_associated/blood_serum.yaml
    data/habitats/host_associated/blood_vessel.yaml data/habitats/host_associated/bone.yaml
    data/habitats/host_associated/bone__169c3d9e.yaml data/habitats/host_associated/bone__234001be.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000125
  summary: "Completed 2026-10-15T12:41:35Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/bl_3_cell.yaml data/habitats/host_associated/bladder.yaml\
    \ data/habitats/host_associated/bladder__9a6dd80c.yaml data/habitats/host_associated/bladder_stone.yaml\
    \ data/habitats/host_associated/blade.yaml data/habitats/host_associated/blade__f83a64ca.yaml\
    \ data/habitats/host_associated/blast_cell.yaml data/habitats/host_associated/blood.yaml\
    \ data/habitats/host_associated/blood__070ce7aa.yaml data/habitats/host_associated/blood__5ca8064f.yaml\
    \ data/habitats/host_associated/blood__5ef3f2f4.yaml data/habitats/host_associated/blood__c1b484fe.yaml\
    \ data/habitats/host_associated/blood__d6f5ae05.yaml data/habitats/host_associated/blood_plasma.yaml\
    \ data/habitats/host_associated/blood_plasma__00b70c6a.yaml data/habitats/host_associated/blood_serum.yaml\
    \ data/habitats/host_associated/blood_vessel.yaml data/habitats/host_associated/bone.yaml\
    \ data/habitats/host_associated/bone__169c3d9e.yaml data/habitats/host_associated/bone__234001be.yaml\n\
    Validating 20 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      20\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Individual schema; strict run includes all twenty prepared targets;
    other gates are full-corpus as documented.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000125
  summary: 'Completed 2026-10-15T12:41:43Z. No issues found

    808 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Individual schema; strict run includes all twenty prepared targets;
    other gates are full-corpus as documented.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000125
  summary: "Completed 2026-10-15T12:41:44Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Individual schema; strict run includes all twenty prepared targets;
    other gates are full-corpus as documented.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000125
  summary: "Completed 2026-10-15T12:41:58Z. expected 3208 records, found 3208 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Individual schema; strict run includes all twenty prepared targets;
    other gates are full-corpus as documented.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000125
  summary: "Completed 2026-10-15T12:42:02Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Individual schema; strict run includes all twenty prepared targets;
    other gates are full-corpus as documented.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000125
  summary: "Completed 2026-10-15T12:42:18Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Individual schema; strict run includes all twenty prepared targets;
    other gates are full-corpus as documented.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000125
  summary: "Completed 2026-10-15T12:42:59Z. id↔label correspondence summary:\n   \
    \       OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Individual schema; strict run includes all twenty prepared targets;
    other gates are full-corpus as documented.
- check_id: CCI
  name: Exact-revision baseline full QC
  status: passed
  required: true
  command: gh run view 38733485444 --json status,conclusion,headSha,url,jobs
  exit_code: 0
  target_ids:
  - BTO:0000125
  summary: 'Verified 2026-10-15T12:40:46Z: https://github.com/CultureBotAI/HabitatMech/actions/runs/38733485444'
  scope_note: Remote full-QC execution at the exact unchanged scientific baseline;
    new review outputs are not yet covered.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/blast_cell.yaml
  locator: Entire target YAML
  accessed_at: '2026-10-15T12:54:54Z'
  support: supports
  summary: Read the full target including source paths, taxa, hierarchy and history.
  snapshot_sha256: a26f91cbdfd1a16aa0f4024e87e3895523f3df61616646472c29bd90e7afa7f1
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, broader-parent and ownership rules
  accessed_at: '2026-10-15T12:54:54Z'
  support: supports
  summary: Context, containment and whole-host identity differ from strictly broader
    habitat ancestry.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation and CharacteristicTaxon
  accessed_at: '2026-10-15T12:54:54Z'
  support: supports
  summary: Mapping endpoints, assertion units and association versus characteristic-presence
    semantics.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native source resolution
  accessed_at: '2026-10-15T12:54:54Z'
  support: supports
  summary: 'Exact routes: [{"source": "PREGO", "mint": "habitatmech:PREGO.35c7ff17db",
    "automatic": {"identifier": "BTO:0000125", "grounding_status": "EXACT", "mapping_predicate":
    null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route":
    "prego_self_grounded", "category": null, "reviewed": false, "decision": null},
    "final": {"identifier": "BTO:0000125", "grounding_status": "EXACT", "mapping_predicate":
    null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route":
    "prego_self_grounded", "category": null, "reviewed": false, "decision": null}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: extract_prego
  accessed_at: '2026-10-15T12:54:54Z'
  support: supports
  summary: Projection preserves distinct-taxon totals and score/channel ranking but
    not original pair citations.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/prego_habitat_taxa.tsv
  locator: Physical TSV rows 113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130
  accessed_at: '2026-10-15T12:54:54Z'
  support: supports
  summary: '[{"row": 113, "data": {"prego_id": "BTO:0000125", "rank": "1", "taxon_id":
    "NCBITaxon:1123383", "taxon_label": "Pseudothermotoga elfii DSM 9442 = NBRC 107921",
    "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates",
    "corroborated_by": ""}}, {"row": 114, "data": {"prego_id": "BTO:0000125", "rank":
    "2", "taxon_id": "NCBITaxon:1123384", "taxon_label": "Pseudothermotoga hypogea
    DSM 11164 = NBRC 106472", "prego_score": "3", "direct_flag": "TRUE", "channels":
    "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 115, "data": {"prego_id":
    "BTO:0000125", "rank": "3", "taxon_id": "NCBITaxon:1189612", "taxon_label": "Indibacter
    alkaliphilus LW1", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates",
    "corroborated_by": ""}}, {"row": 116, "data": {"prego_id": "BTO:0000125", "rank":
    "4", "taxon_id": "NCBITaxon:1322346", "taxon_label": "Glaesserella parasuis ZJ0906",
    "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates",
    "corroborated_by": ""}}, {"row": 117, "data": {"prego_id": "BTO:0000125", "rank":
    "5", "taxon_id": "NCBITaxon:1408159", "taxon_label": "Pseudothermotoga caldifontis
    AZM44c09", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates",
    "corroborated_by": ""}}, {"row": 118, "data": {"prego_id": "BTO:0000125", "rank":
    "6", "taxon_id": "NCBITaxon:1408160", "taxon_label": "Thermotoga profunda AZM34c06",
    "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates",
    "corroborated_by": ""}}, {"row": 119, "data": {"prego_id": "BTO:0000125", "rank":
    "7", "taxon_id": "NCBITaxon:1497681", "taxon_label": "Paenilisteria newyorkensis",
    "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates",
    "corroborated_by": ""}}, {"row": 120, "data": {"prego_id": "BTO:0000125", "rank":
    "8", "taxon_id": "NCBITaxon:1552123", "taxon_label": "Listeria booriae", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 121, "data": {"prego_id": "BTO:0000125", "rank": "9", "taxon_id":
    "NCBITaxon:1585974", "taxon_label": "Beduini massiliensis", "prego_score": "3",
    "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 122, "data": {"prego_id": "BTO:0000125", "rank": "10", "taxon_id":
    "NCBITaxon:187452", "taxon_label": "Pediococcus claussenii", "prego_score": "3",
    "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 123, "data": {"prego_id": "BTO:0000125", "rank": "11", "taxon_id":
    "NCBITaxon:240427", "taxon_label": "Secundilactobacillus paracollinoides", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 124, "data": {"prego_id": "BTO:0000125", "rank": "12", "taxon_id":
    "NCBITaxon:375175", "taxon_label": "Loigolactobacillus backii", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 125, "data": {"prego_id": "BTO:0000125", "rank": "13", "taxon_id":
    "NCBITaxon:478010", "taxon_label": "Microterricola pindariensis", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 126, "data": {"prego_id": "BTO:0000125", "rank": "14", "taxon_id":
    "NCBITaxon:51663", "taxon_label": "Pediococcus damnosus", "prego_score": "3",
    "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 127, "data": {"prego_id": "BTO:0000125", "rank": "15", "taxon_id":
    "NCBITaxon:53444", "taxon_label": "Fructilactobacillus lindneri", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 128, "data": {"prego_id": "BTO:0000125", "rank": "16", "taxon_id":
    "NCBITaxon:562", "taxon_label": "Escherichia coli", "prego_score": "3", "direct_flag":
    "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row":
    129, "data": {"prego_id": "BTO:0000125", "rank": "17", "taxon_id": "NCBITaxon:582",
    "taxon_label": "Morganella morganii", "prego_score": "3", "direct_flag": "TRUE",
    "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 130,
    "data": {"prego_id": "BTO:0000125", "rank": "18", "taxon_id": "NCBITaxon:758793",
    "taxon_label": "Caballeronia insecticola", "prego_score": "3", "direct_flag":
    "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}]'
  snapshot_sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
- evidence_id: ET6
  kind: database
  reference: data/raw/prego_habitats.tsv
  locator: Physical TSV rows 294
  accessed_at: '2026-10-15T12:54:54Z'
  support: supports
  summary: '[{"row": 294, "data": {"prego_id": "BTO:0000125", "ontology": "BTO", "biolink_category":
    "biolink:GrossAnatomicalStructure", "taxon_count": "18", "direct_assertion_count":
    "18", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms":
    "blast|blast cell|blast cells|blastic|blasts|hematoblast|hematoblastic|hematoblasts|hematocytoblast|hematocytoblastic|hematocytoblasts|hemocytoblast|hemocytoblastic|hemocytoblasts"}}]'
  snapshot_sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
- evidence_id: ET7
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 127
  accessed_at: '2026-10-15T12:54:54Z'
  support: supports
  summary: '[{"row": 127, "data": {"term_id": "BTO:0000125", "ontology": "BTO", "label":
    "blast cell", "definition": "In the monophyletic theory, the least differentiated,
    totipotential blood cell without commitment as to its particular series, from
    which all blood cells are derived, preceding a stem cell.", "synonyms": "", "deprecated":
    "", "directly_referenced": "TRUE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EL8
  kind: record_content
  reference: reports/yaml_record_review/20260921T234045Z-blast_cell.md
  locator: Historical complete review
  accessed_at: '2026-10-15T12:54:54Z'
  support: supports
  summary: Read as a source/issue lead. Current severity and verdict are reassessed
    independently; legacy prose does not close or create structured lineage.
  snapshot_sha256: 56273ad13c9d8ff8be52d8b4fc6fcc5e09b055b68be7dc7279f335e2a81a3115
- evidence_id: EX9
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000125/graph
  locator: BTO_0000125-graph.json
  accessed_at: '2026-10-15T12:46:41Z'
  support: context_only
  summary: 'Inspected outgoing typed ontology relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0000125",
    "target": "http://purl.obolibrary.org/obo/BTO_0000089", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 8e899a0e4e9f71613be2c84f6702fceb59465008d1a931ebde5e2a645dab87c0
- evidence_id: EX10
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000125?lang=en
  locator: BTO_0000125.json
  accessed_at: '2026-10-15T12:46:40Z'
  support: context_only
  summary: 'Inspected current identifier, label, active status and full definition
    for the scope assessment: {"obo_id": "BTO:0000125", "label": "blast cell", "is_obsolete":
    false}'
  snapshot_sha256: 030e5f5b349db58bf497253f95f04b2ec6688e44fa9c2ae95bee61461cee91f5
- evidence_id: EX11
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10057702/fullTextXML
  locator: PMC10057702.xml
  accessed_at: '2026-10-15T12:48:10Z'
  support: context_only
  summary: 'Primary methods/abstract, PMID:36985346, DOI:10.3390/microorganisms11030773:
    Pseudothermotoga elfii DSM9442 is an oil-well isolate grown anaerobically at 65
    C in pressure experiments. This contrasts with a blood-cell habitat assertion.
    It is not the recovered PREGO pair citation and cannot establish the cause of
    an extraction or exclude other experimental contexts.'
  snapshot_sha256: 5cf8fa3c1feec7399b45dc9a800cf7d0679ba16555f60b8e7d84f2281c759b9c
- evidence_id: EX12
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML
  locator: PMC8879827.xml
  accessed_at: '2026-10-15T12:48:05Z'
  support: context_only
  summary: 'PREGO methods section 2.3, PMID:35208748, DOI:10.3390/microorganisms10020293:
    genome-sequencing BioProject taxa are linked by mining associated abstracts; confidence
    three of five does not independently establish physical localization.'
  snapshot_sha256: 375f0fde4d07bb823cb9106aa4567bc0ef03c2866af0b2a7740b543f50687c25
- evidence_id: EX13
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1123383,1123384,1189612,1206108,1282,1286329,1286330,1286331,1286332,1286333,1286334,1286335,1286336,1286337,1286338,1286339,1286340,1286341,1286342,1286343,1286344,1286345,1286346,1286347,1286348,1286350,1286351,1286352,1286353,1322346,1408159,1408160,1497681,1552123,1585974,187452,240427,2702,375175,43771,478010,504474,508451,51663,53444,562,574375,582,588,758793,827&retmode=xml
  locator: taxonomy.xml
  accessed_at: '2026-10-15T12:47:05Z'
  support: context_only
  summary: 'All displayed taxon identifiers and labels resolve to current NCBI identities:
    [{"record_id": "1123383", "current_id": "1123383", "record_label": "Pseudothermotoga
    elfii DSM 9442 = NBRC 107921", "current_label": "Pseudothermotoga elfii DSM 9442
    = NBRC 107921", "rank": "strain"}, {"record_id": "1123384", "current_id": "1123384",
    "record_label": "Pseudothermotoga hypogea DSM 11164 = NBRC 106472", "current_label":
    "Pseudothermotoga hypogea DSM 11164 = NBRC 106472", "rank": "strain"}, {"record_id":
    "1189612", "current_id": "1189612", "record_label": "Indibacter alkaliphilus LW1",
    "current_label": "Indibacter alkaliphilus LW1", "rank": "strain"}, {"record_id":
    "1322346", "current_id": "1322346", "record_label": "Glaesserella parasuis ZJ0906",
    "current_label": "Glaesserella parasuis ZJ0906", "rank": "strain"}, {"record_id":
    "1408159", "current_id": "1408159", "record_label": "Pseudothermotoga caldifontis
    AZM44c09", "current_label": "Pseudothermotoga caldifontis AZM44c09", "rank": "strain"},
    {"record_id": "1408160", "current_id": "1408160", "record_label": "Thermotoga
    profunda AZM34c06", "current_label": "Thermotoga profunda AZM34c06", "rank": "strain"},
    {"record_id": "1497681", "current_id": "1497681", "record_label": "Paenilisteria
    newyorkensis", "current_label": "Paenilisteria newyorkensis", "rank": "species"},
    {"record_id": "1552123", "current_id": "1552123", "record_label": "Listeria booriae",
    "current_label": "Listeria booriae", "rank": "species"}, {"record_id": "1585974",
    "current_id": "1585974", "record_label": "Beduini massiliensis", "current_label":
    "Beduini massiliensis", "rank": "species"}, {"record_id": "187452", "current_id":
    "187452", "record_label": "Pediococcus claussenii", "current_label": "Pediococcus
    claussenii", "rank": "species"}, {"record_id": "240427", "current_id": "240427",
    "record_label": "Secundilactobacillus paracollinoides", "current_label": "Secundilactobacillus
    paracollinoides", "rank": "species"}, {"record_id": "375175", "current_id": "375175",
    "record_label": "Loigolactobacillus backii", "current_label": "Loigolactobacillus
    backii", "rank": "species"}, {"record_id": "478010", "current_id": "478010", "record_label":
    "Microterricola pindariensis", "current_label": "Microterricola pindariensis",
    "rank": "species"}, {"record_id": "51663", "current_id": "51663", "record_label":
    "Pediococcus damnosus", "current_label": "Pediococcus damnosus", "rank": "species"},
    {"record_id": "53444", "current_id": "53444", "record_label": "Fructilactobacillus
    lindneri", "current_label": "Fructilactobacillus lindneri", "rank": "species"},
    {"record_id": "562", "current_id": "562", "record_label": "Escherichia coli",
    "current_label": "Escherichia coli", "rank": "species"}, {"record_id": "582",
    "current_id": "582", "record_label": "Morganella morganii", "current_label": "Morganella
    morganii", "rank": "species"}, {"record_id": "758793", "current_id": "758793",
    "record_label": "Caballeronia insecticola", "current_label": "Caballeronia insecticola",
    "rank": "species"}]'
  snapshot_sha256: f8419452b360c25eb644e679b18e320a164cb1dadcd7177218469368fe9cd7dd
- evidence_id: ESEARCH
  kind: search
  reference: Local maintained inputs and structured archive
  locator: rg --no-ignore --hidden -l -F -e BTO:0000125 -e 'blast cell' -e blast_cell
    -e habitatmech:PREGO.35c7ff17db curation history research reports data/raw build
    reviews
  accessed_at: '2026-10-15T12:45:44Z'
  support: context_only
  summary: Ignored-inclusive search plus exact TSV parsing identified the stated source
    rows and no structured predecessor.
  search_scope: curation, history, research, reports, data/raw, build and reviews,
    including ignored and hidden files; pathlib traversal of all structured review.yaml
    files.
- evidence_id: EPREGOSEARCH
  kind: search
  reference: Configured kg-microbe checkout
  locator: find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe
    -type f -path '*/prego/*' -name '*.tsv'
  accessed_at: '2026-10-15T12:45:47Z'
  support: context_only
  summary: No PREGO-directory TSV payload found in this configured checkout. Committed
    HabitatMech projections are present; no global/upstream absence claim is made.
  search_scope: All matching files under the configured checkout, including ignored/hidden
    paths.
assessments:
- assessment_id: A1
  area: schema
  topic: Native validation and reproduction
  outcome: supported
  summary: Schema, strict, history, provenance, 3,208-record reproduction, causal
    overlays, term requests and configured labels passed. These establish deterministic
    fidelity, not scientific support.
  target_ids:
  - BTO:0000125
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Identity, hierarchy and nomenclature
  outcome: supported
  summary: The BTO blast-cell identity is current; its blood relation is part-of and
    correctly is not emitted as subclass ancestry. PREGO faithfully emits eighteen
    score-three associations, but original pair citations are unavailable and the
    inspected DSM9442 source concerns oil-reservoir thermophiles. This warrants evidence
    recovery, not unsupported deletion or a claim that BLAST caused the association.
  target_ids:
  - BTO:0000125
  evidence_ids:
  - E1
  - ERULE
  - ESEED
  - EX9
  - EX10
  - EX11
  - EX12
  - EX13
- assessment_id: A3
  area: quantity
  topic: Source count, unit and ranking
  outcome: supported
  summary: 'Exact source projections retain [{"source": "PREGO", "source_id": "BTO:0000125",
    "source_label": "blast cell", "assertion_count": 18, "assertion_unit": "TAXON",
    "score": 3.0, "evidence_channels": "annotated_genomes_isolates"}]. All 18 displayed
    taxa were resolved against current NCBI IDs/labels. Ranks and candidate pools
    are source-specific; unlike units are never summed.'
  target_ids:
  - BTO:0000125
  evidence_ids:
  - E1
  - ESEED
  - EEXTRACT
  - EX9
  - EX10
  - EX11
  - EX12
  - EX13
- assessment_id: A4
  area: completeness
  topic: Native status and optional fields
  outcome: supported
  summary: Executed source decisions reproduce EXACT/SEEDED. No causal mechanism or
    is_characteristic assertion is present. Missing optional fields or SEEDED status
    are not automatic scientific defects.
  target_ids:
  - BTO:0000125
  evidence_ids:
  - E1
  - ESEED
  - ESCHEMA
findings:
- finding_id: F1
  issue_key: blast-cell-prego-pair-scope
  category: evidence
  severity: major
  status: open
  certainty: provisional
  title: Blast-cell associations lack recoverable localization evidence
  description: Recover the exact PREGO evidence for the eighteen BTO:0000125 taxon
    pairs, beginning with NCBITaxon:1123383/DSM9442. Distinguish blood-cell localization
    from bioinformatics or other abstract context. A BLAST lexical collision is only
    a hypothesis, not an established cause. Preserve source provenance and counts;
    any qualified displayed pool needs a maintained source contract and exact-pair
    regressions.
  target_ids:
  - BTO:0000125
  field_paths:
  - characteristic_taxa
  - source_attestations
  evidence_ids:
  - E1
  - ERULE
  - ESEED
  - EX9
  - EX10
  - EX11
  - EX12
  - EX13
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
  - BTO:0000125
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
  description: Recover the exact PREGO evidence for the eighteen BTO:0000125 taxon
    pairs, beginning with NCBITaxon:1123383/DSM9442. Distinguish blood-cell localization
    from bioinformatics or other abstract context. A BLAST lexical collision is only
    a hypothesis, not an established cause. Preserve source provenance and counts;
    any qualified displayed pool needs a maintained source contract and exact-pair
    regressions. No repair is performed by this review.
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
- Every historical specimen and original PREGO pair has not been independently reidentified.
  Counts/scores/ranks are not prevalence, viability or characteristic presence.
- Configured label checks skip 2,061 pairs without adapters; deterministic validity
  does not certify biological semantics.
- Full baseline QC is verified remote evidence at the captured revision, not a new
  local execution. Post-save archive and publication gates are subsequent.
- 'iModulonDB is not applicable: the target asserts no gene, regulator or expression
  module. No paid research was performed.'
- Original PREGO pair evidence was not recovered. Source-specific publications support
  only their stated strain/site comparisons, not all retained associations or a demonstrated
  extraction cause.
notes:
- All captured local input hashes were rechecked against both the working tree and
  exact Git revision. No input bytes were silently refreshed.
- Ignored-inclusive archive traversal found no structured predecessor for this target;
  legacy Markdown is context, not independent approval or successor lineage.
- This observation precedes separately authorized curation/publication and does not
  claim a repair.
tags:
- individual-scientific-review
- host-associated
```
