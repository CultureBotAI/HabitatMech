# Scoped publication follow-up: anaerobic_sludge_blanket_reactor

- Review: 20261011T025344Z-anaerobic_sludge_blanket_reactor-followup
- Repository: culturebotai/HabitatMech
- Started UTC: 2026-10-11T02:53:24Z
- Finished UTC: 2026-10-11T02:53:44Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The missing-name finding remains a minor, open provenance gap for NCBITaxon:517543 alone, verified as Toxopoda sp. 2 RM-2008. Retains the prior #1895 correction to original review 20261011T024021Z-anaerobic_sludge_blanket_reactor F1, which copied an unrelated animal-house 147810-to-1606 alias clause (#1895). The UASB record and raw PREGO inventory have not changed; governed source refresh remains in #1897. Validation-target metadata (#1898) is corrected by retaining only the applicable single-record check; both original executions are preserved in the preceding observation.

## Scope And Provenance

Bounded successor reassessing the precise correction and retaining the unresolved finding.

Selection: One exact previously reviewed record; no additional unique-record coverage.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 4336705cdafb13a569044fd7df2313c10e82e3ed.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| ENVO:00002213 | data/habitats/engineered/anaerobic_sludge_blanket_reactor.yaml | generated | anaerobic sludge blanket reactor |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-uasb | passed | True | ENVO:00002213 | Actual run 2026-10-11T02:49:29Z to 2026-10-11T02:49:32Z. Native scope as commanded; full-corpus checks do not imply full-corpus scientific coverage. |
| strict | passed | True | ENVO:00002213 | Actual run 2026-10-11T02:49:32Z to 2026-10-11T02:49:38Z. Native scope as commanded; full-corpus checks do not imply full-corpus scientific coverage. |
| corpus | passed | True | ENVO:00002213 | Actual run 2026-10-11T02:49:38Z to 2026-10-11T02:49:57Z. Native scope as commanded; full-corpus checks do not imply full-corpus scientific coverage. |
| labels | passed | True | ENVO:00002213 | Actual run 2026-10-11T02:49:57Z to 2026-10-11T02:51:10Z. Native scope as commanded; full-corpus checks do not imply full-corpus scientific coverage. |
| history | passed | True | ENVO:00002213 | Actual run 2026-10-11T02:51:10Z to 2026-10-11T02:51:17Z. Native scope as commanded; full-corpus checks do not imply full-corpus scientific coverage. |
| causal | passed | True | ENVO:00002213 | Actual run 2026-10-11T02:51:17Z to 2026-10-11T02:51:24Z. Native scope as commanded; full-corpus checks do not imply full-corpus scientific coverage. |
| terms | passed | True | ENVO:00002213 | Actual run 2026-10-11T02:51:24Z to 2026-10-11T02:51:48Z. Native scope as commanded; full-corpus checks do not imply full-corpus scientific coverage. |
| Focused hierarchy regression | passed | True | ENVO:00002213 | 49 passed in 83.47 seconds. Whole-corpus with/without exclusion comparison changes exactly Anammox parent/history. |

## Scientific And Domain Assessments

### Preserved source identity and association scope

provenance: supported. Targets: ENVO:00002213.

Exact identity, source assertions, counts/units and native status are preserved. No observed taxon is promoted to characteristic ecology. The missing-name finding remains a minor, open provenance gap for NCBITaxon:517543 alone, verified as Toxopoda sp. 2 RM-2008. Retains the prior #1895 correction to original review 20261011T024021Z-anaerobic_sludge_blanket_reactor F1, which copied an unrelated animal-house 147810-to-1606 alias clause (#1895). The UASB record and raw PREGO inventory have not changed; governed source refresh remains in #1897. Validation-target metadata (#1898) is corrected by retaining only the applicable single-record check; both original executions are preserved in the preceding observation.

### Remaining predecessor finding

representation: concern. Targets: ENVO:00002213.

The exact PREGO association for NCBITaxon:517543 omits its taxon label in both the frozen inventory and generated UASB record. NCBI returns the exact same identifier with ScientificName Toxopoda sp. 2 RM-2008. No alias migration is involved for this target. The identifier resolves; the name omission is not a broken reference, serialization loss or characteristic-ecology claim.

## Findings

### F1: One resolvable PREGO taxon name remains omitted

minor / open / confirmed; issue key: envo-00002213-missing-resolvable-taxon-labels.

The exact PREGO association for NCBITaxon:517543 omits its taxon label in both the frozen inventory and generated UASB record. NCBI returns the exact same identifier with ScientificName Toxopoda sp. 2 RM-2008. No alias migration is involved for this target. The identifier resolves; the name omission is not a broken reference, serialization loss or characteristic-ecology claim.

## Recommended Actions And Acceptance Checks

### A1

Refresh names through governed taxonomy inputs with explicit alias handling. Preserve original source IDs and evidence; inspect canonicalization collisions before any identifier or rank changes.

- Missing names agree with versioned NCBI evidence; valid source aliases remain traceable.
- Ranks, candidate-pool sizes, scores and habitat scope remain unchanged unless separately justified.
- Use maintained inputs, never patch generated habitat YAML or pages.
- Preserve full source provenance, snapshot-specific counts/units and unrelated inputs; inspect an exact forced seed canary before authorized regeneration.
- Append required curation history, run full native QC and relevant ontology/provenance checks, and save an immutable linked reassessment. Actions are proposals, not executed fixes.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R | data/habitats/engineered/anaerobic_sludge_blanket_reactor.yaml; Entire current target YAML including all generated history | supports | Retained predecessor evidence, with its original access timestamp: Retained predecessor evidence, with its original access timestamp: The active ENVO identity, upward-flow sludge-blanket definition and anaerobic-bioreactor genus agree. Source ranks and scores are faithful, but the sixth taxon lacks an available NCBI name. Defects in the parent record do not refute this direct ontology genus edge or authorize copying the parent biological content. |
| RAW | data/raw/gold_ecosystem_paths.tsv; data/raw/prego_habitats.tsv; data/raw/bacdive_isolation_sources.tsv; Exact source IDs/full paths in target source_attestations; all captured GOLD rows | supports | Retained predecessor evidence, with its original access timestamp: Retained predecessor evidence, with its original access timestamp: Frozen GOLD rows=[]; emitted source assertions=[{"assertion_count": 6, "assertion_unit": "TAXON", "evidence_channels": "environmental_samples", "score": 1.11189, "source": "PREGO", "source_id": "ENVO:00002213", "source_label": "anaerobic sludge blanket reactor"}]. Exact aggregate counts and first-node convention checked against source tables. GOLD counts ORGANISM, PREGO TAXON and BacDive STRAIN. Zero frozen GOLD counts are omitted, not evidence that no samples exist; unlike units are never summed. |
| OWN | curation/decisions.tsv; curation/gold_parent_exclusions.tsv; curation/term_requests.tsv; Exact source-key rows with current line numbers | supports | Retained predecessor evidence, with its original access timestamp: Retained predecessor evidence, with its original access timestamp: {}. Empty target definition rows mean no maintained authored definition in these tables, not a global ontology absence. Other targets using this ID as parent are not target decisions. |
| CODE | src/habitatmech/seed.py; src/habitatmech/extract.py; src/habitatmech/schema/habitatmech.yaml; ConceptStore.get, _decided, resolve_gold, ingest_gold, source-specific attestation ingestion and SourceAttestation.mapping_predicate | supports | Retained predecessor evidence, with its original access timestamp: Retained predecessor evidence, with its original access timestamp: Schema endpoints are source concept -&gt; generated record identifier. The NARROW lexical route retains a source mint but emits a predicate to its implicit ontology parent. Ontology TSV synonyms lack scope and ConceptStore.get emits them exact. GOLD ancestor and CLOSE/BROAD guards do not repair all ontology scopes or condition adjectives. Current explicit PREGO GROUND-predicate and BacDive override-note fixes are not treated as still-unfixed bugs. |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; docs/record-review-profile.md; .claude/skills/curate-yaml-record/references/review-checklist.md; Local habitat identity, strict is-a, source units, optional fields and native lifecycle rules | supports | Retained predecessor evidence, with its original access timestamp: Retained predecessor evidence, with its original access timestamp: Parents must be strictly broader, not container, treatment output or feed. REVIEWED requires ITEM decisions for all contributing source concepts but is not scientific proof. CLASS/SEEDED and empty optional fields alone are not major defects; source associations do not establish characteristic taxa or mechanisms. |
| PARENTS | data/habitats/engineered/anaerobic_sludge_blanket_reactor.yaml; Each actual parent resolved through current corpus where present; external ontology parents checked separately | context_only | Retained predecessor evidence, with its original access timestamp: Retained predecessor evidence, with its original access timestamp: {"ENVO:00002124": {"definition": "A bioreactor in which the contained material is not oxygenated (i.e. void of biologically consequential free oxygen)", "identifier": "ENVO:00002124", "label": "anaerobic bioreactor", "parent_habitats": ["ENVO:00002123", "ENVO:03600010", "habitatmech:GOLD.24cf427e7d", "habitatmech:GOLD.32c2a98ae8", "habitatmech:GOLD.3af6ca6cc3"], "path": "data/habitats/engineered/anaerobic_bioreactor.yaml", "source_attestations": [{"assertion_count": 131, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:exactMatch", "notes": "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:4440", "source_label": "Anaerobic", "source_path": "Engineered &gt; Bioreactor &gt; Anaerobic"}, {"mapping_predicate": "skos:exactMatch", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:7768", "source_label": "Anaerobic", "source_path": "Engineered &gt; Bioreactor &gt; Semi-continuous &gt; Anaerobic"}, {"mapping_predicate": "skos:exactMatch", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:8151", "source_label": "Anaerobic", "source_path": "Engineered &gt; Bioreactor &gt; SSF (Solid state fermentation) &gt; Anaerobic"}, {"mapping_predicate": "skos:exactMatch", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:8271", "source_label": "Anaerobic", "source_path": "Engineered &gt; Bioreactor &gt; MBR (Membrane bioreactor) &gt; Anaerobic"}, {"mapping_predicate": "skos:exactMatch", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:8426", "source_label": "Anaerobic", "source_path": "Engineered &gt; Bioreactor &gt; DHS reactor &gt; Anaerobic"}, {"assertion_count": 81, "assertion_unit": "TAXON", "evidence_channels": "environmental_samples", "score": 4.0, "source": "PREGO", "source_id": "ENVO:00002124", "source_label": "anaerobic bioreactor"}]}}. Only parent identity and direct relationship scope assessed; no inherited taxon, parameter or mechanism claims and no full scientific parent review. |
| O-ENVO-00002124 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002124; Exact current official OLS identifier, label, definition and eligibility response | supports | Retained predecessor evidence, with its original access timestamp: Retained predecessor evidence, with its original access timestamp: {"description": ["A bioreactor in which the contained material is not oxygenated (i.e. void of biologically consequential free oxygen)"], "is_obsolete": false, "label": "anaerobic bioreactor", "obo_id": "ENVO:00002124", "term_replaced_by": null} |
| O-ENVO-00002213 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002213; Exact current official OLS identifier, label, definition and eligibility response | supports | Retained predecessor evidence, with its original access timestamp: Retained predecessor evidence, with its original access timestamp: {"description": ["An anaerobic bioreactor which is capable of treating wastewater through the action of methanogenic microbes which form a blanket of sludge due to the upward flow in the reactor."], "is_obsolete": false, "label": "anaerobic sludge blanket reactor", "obo_id": "ENVO:00002213", "term_replaced_by": null} |
| ENVO | https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.obo; Relevant complete term stanzas, typed synonyms and direct is-a assertions in official ENVO OBO | supports | Retained predecessor evidence, with its original access timestamp: Retained predecessor evidence, with its original access timestamp: Anaerobic bioreactor has bioreactor genus, not membrane/DHS/SSF/semi-continuous genera. Anaerobic sludge is sludge with anaerobic quality; digester sludge is below anaerobic sludge. Animal cage has manufactured-cage genus and BROAD cage alias. Animal waste has organic-waste genus and BROAD animal waste alias. Aquaculture farm has agricultural-ecosystem genus and BROAD aquaculture/aquafarming aliases. Target and parent terms were compared to the captured slice without rewriting either source. |
| GOLD | https://gold.jgi.doe.gov/ecosystem_classification; Five-level classification guidance, especially Ecosystem and Ecosystem Category | supports | Retained predecessor evidence, with its original access timestamp: Retained predecessor evidence, with its original access timestamp: GOLD describes sample surroundings, with progressively more specific environment categories. This supports reading the whole source path; an activity-like leaf need not denote only a process. It does not make every hierarchical link an is-a or resolve setting versus specimen material automatically. |
| CLASS | https://gold.jgi.doe.gov/; Retained classification workbook site data; SHA256 3933e5f0664915c1bbfa00212e17d013da360fb33dd52e509254050813135396 | supports | Retained predecessor evidence, with its original access timestamp: Retained predecessor evidence, with its original access timestamp: Exact filler-stripped path rows=[]. All 2422 classification rows scanned. No exact GOLD path is expected for a PREGO-only target. The retained workbook is not asserted to be a new live download. |
| BULK | https://gold.jgi.doe.gov/download?mode=site_excel; Retained later workbook exact-path member census and accession joins; SHA256 5f48b2f50fb2a9257754960a0f0e12dc6e8fa121e97c3e9f4497249e5fe6e439 | supports | Retained predecessor evidence, with its original access timestamp: Retained predecessor evidence, with its original access timestamp: Counts={"Biosample": 0, "Organism": 0, "SequencingProject": 0}; distinct joined studies=0; inspected examples={"Biosample": [], "Organism": []}; common collection-site values={"Biosample": [], "Organism": []}. Full Biosample, Organism, SequencingProject and Study sheets scanned, including headers: 244951, 532019, 636914 and 63806 rows. Counts are separate per unit and snapshot. This does not reconstruct frozen source members or establish ecological replication. |
| CONTEXT | data/raw/gold_path_biosamples.tsv; data/raw/gold_path_triads.tsv; data/raw/gold_studies.tsv; Exact canonical-path fields and pipe-delimited study-path memberships | supports | Retained predecessor evidence, with its original access timestamp: Retained predecessor evidence, with its original access timestamp: Biosample rows=[]; triads=[]; study IDs and lines=[]. MIxS broad, local and medium roles are separate. Triad rows that merely mention the target ontology ID for a different source path are not contributing target assertions. No descendant counts or claims are inherited. |
| TAX | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1000562%2C1004316%2C1004322%2C1004326%2C1005%2C1031541%2C103810%2C104102%2C104245%2C1045010%2C1046128%2C108486%2C1119058%2C1121001%2C1121025%2C1121275%2C1121423%2C1121921%2C1121950%2C1131567%2C114628%2C114707%2C1150776%2C1178540%2C1194427%2C121845%2C1264%2C1265%2C1270%2C1278308%2C1282%2C1286%2C1291048%2C1299%2C134533%2C1348%2C1352%2C1363%2C1366%2C1391%2C1397%2C1423814%2C1472%2C147810%2C148604%2C1494%2C149712%2C1502%2C1505%2C1511%2C1512%2C152%2C1530%2C1534%2C153496%2C153501%2C1553%2C156%2C1580%2C158192%2C164393%2C173%2C1855%2C186741%2C197222%2C200125%2C202748%2C214688%2C246432%2C258475%2C266940%2C28122%2C28251%2C28262%2C286698%2C288%2C29290%2C29355%2C295236%2C29549%2C31910%2C322009%2C330214%2C335543%2C33936%2C33954%2C411463%2C411467%2C412614%2C417399%2C42353%2C438%2C445335%2C457416%2C457431%2C469371%2C485916%2C492476%2C498761%2C517543%2C526588%2C53249%2C548474%2C55518%2C60890%2C644383%2C651%2C666%2C678%2C679937%2C85963%2C887929%2C946678%2C96773%2C99656&amp;retmode=xml; Exact target subset of NCBI Taxonomy efetch; TaxId, ScientificName and AkaTaxIds compared with all retained raw association rows | supports | Retained predecessor evidence, with its original access timestamp: Retained predecessor evidence, with its original access timestamp: Verified target rows=[{"line": 6299, "path": "data/raw/prego_habitat_taxa.tsv", "row": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002213", "prego_score": "1.11189", "rank": "1", "taxon_id": "NCBITaxon:202748", "taxon_label": "Saprospira sp. SS98-5"}}, {"line": 6300, "path": "data/raw/prego_habitat_taxa.tsv", "row": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002213", "prego_score": "1.10193", "rank": "2", "taxon_id": "NCBITaxon:417399", "taxon_label": "Vibrio cholerae NCTC 8457"}}, {"line": 6301, "path": "data/raw/prego_habitat_taxa.tsv", "row": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002213", "prego_score": "1.05112", "rank": "3", "taxon_id": "NCBITaxon:42353", "taxon_label": "Nitrosomonas sp."}}, {"line": 6302, "path": "data/raw/prego_habitat_taxa.tsv", "row": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002213", "prego_score": "1.04421", "rank": "4", "taxon_id": "NCBITaxon:85963", "taxon_label": "Helicobacter pylori J99"}}, {"line": 6303, "path": "data/raw/prego_habitat_taxa.tsv", "row": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002213", "prego_score": "1.03669", "rank": "5", "taxon_id": "NCBITaxon:96773", "taxon_label": "Thauera chlorobenzoica"}}, {"line": 6304, "path": "data/raw/prego_habitat_taxa.tsv", "row": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002213", "prego_score": "1.01893", "rank": "6", "taxon_id": "NCBITaxon:517543", "taxon_label": ""}}]. Every populated target name matches current NCBI. Unnamed 517543 resolves Toxopoda sp. 2 RM-2008; 121845 resolves Diaphorina citri; 147810 is an explicit alias of 1606 Ligilactobacillus aviarius where those IDs occur. Scores/counts/ranks and candidate pools match frozen inputs. No row is marked is_characteristic. This verifies source representation and identity, not all original ecological observations. |
| SEARCH | curation/; history/; research/; reports/; reviews/; data/raw/; data/habitats/; conf/; Saved ignored-inclusive support-search receipt, structured current-corpus/review inventory and exact TSV/overlay target scans | context_only | Retained predecessor evidence, with its original access timestamp: Retained predecessor evidence, with its original access timestamp: No completed structured review covered this exact target at the refreshed baseline. All 32 maintained overlay target IDs were parsed; none targets these selected records. No selected target has a maintained authored definition row. Legacy reports and relevant history were located; optional sparsity is not treated as a defect. |
| LEGACY | reports/yaml_record_review/20261007T032002Z-anaerobic_sludge_blanket_reactor.md; Exact-target prior report findings compared with current captured inputs | context_only | Retained predecessor evidence, with its original access timestamp: Retained predecessor evidence, with its original access timestamp: The legacy missing taxon-name finding is independently confirmed against the current raw row and NCBI response. It remains minor; no required identity field is broken. |
| VALID | justfile; Original gates 0-17 plus fresh resume gate logs; unchanged base/input hashes verified | supports | Retained predecessor evidence, with its original access timestamp: Retained predecessor evidence, with its original access timestamp: Sixteen target LinkML checks and the 16-record strict check passed; 3208 records reproduced exactly. Fresh label gate completed with 1178 canonical, 1 synonym, 5 accepted exceptions and 2057 no-adapter skips. All 293 histories, 32 causal overlays and 109 term requests passed. The earlier permission-interrupted label run is NOT a pass despite exit 0; all interrupted remaining gates were rerun. Deterministic validation is not scientific approval. |
| CURRENT | data/habitats/engineered/anaerobic_sludge_blanket_reactor.yaml; Complete current record, maintained owner rows and exact source assertions | supports | The missing-name finding remains a minor, open provenance gap for NCBITaxon:517543 alone, verified as Toxopoda sp. 2 RM-2008. Retains the prior #1895 correction to original review 20261011T024021Z-anaerobic_sludge_blanket_reactor F1, which copied an unrelated animal-house 147810-to-1606 alias clause (#1895). The UASB record and raw PREGO inventory have not changed; governed source refresh remains in #1897. Validation-target metadata (#1898) is corrected by retaining only the applicable single-record check; both original executions are preserved in the preceding observation. |
| PREDECESSOR | reviews/structured/20261011T025202Z-anaerobic_sludge_blanket_reactor-followup/review.yaml; F1 and its precise evidence/limitations | context_only | Immutable original retained; F1 remains open with exact lineage. |
| CORRECTION | reviews/structured/20261011T025202Z-anaerobic_sludge_blanket_reactor-followup/review.yaml; F1 description compared with exact raw taxon row and NCBI response | supports | The exact PREGO association for NCBITaxon:517543 omits its taxon label in both the frozen inventory and generated UASB record. NCBI returns the exact same identifier with ScientificName Toxopoda sp. 2 RM-2008. No alias migration is involved for this target. The identifier resolves; the name omission is not a broken reference, serialization loss or characteristic-ecology claim. |
| CHECKS | tests/test_anammox_review_fix.py; 49 focused tests plus fresh native validation receipts | supports | Full corpus comparison changes only Anammox parent/history; all source counts, units, identifiers, taxa and statuses are unchanged. Current native checks pass. These are deterministic results, not independent scientific review. |

## Limits And Additional Notes

- Adversarial self-review, not independent approval.
- Validation receipts precede this reporting correction; SHA256 comparisons establish that every captured input is unchanged since those runs. No gate is claimed to have rerun merely because its metadata was corrected.
- This observation does not claim full publication QC or map/site completion; those are required before merge.
- Original frozen GOLD member reconstruction is unavailable at the configured location. Later workbook evidence does not certify frozen member counts or exact source meaning.
- Configured taxon-label and unsupported-ontology adapter gaps remain; passing native gates do not repair them.
- Other open findings and shared issues #1249, #1398, #1614, #1896 and #1897 remain; no SSSOM/KGX readiness certification.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T025344Z-anaerobic_sludge_blanket_reactor-followup
kind: record
repository: culturebotai/HabitatMech
title: 'Scoped publication follow-up: anaerobic_sludge_blanket_reactor'
started_at: '2026-10-11T02:53:24Z'
finished_at: '2026-10-11T02:53:44Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Continuing agent that has participated in repository curation;
    not independent reviewer approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'The missing-name finding remains a minor, open provenance gap for NCBITaxon:517543
  alone, verified as Toxopoda sp. 2 RM-2008. Retains the prior #1895 correction to
  original review 20261011T024021Z-anaerobic_sludge_blanket_reactor F1, which copied
  an unrelated animal-house 147810-to-1606 alias clause (#1895). The UASB record and
  raw PREGO inventory have not changed; governed source refresh remains in #1897.
  Validation-target metadata (#1898) is corrected by retaining only the applicable
  single-record check; both original executions are preserved in the preceding observation.'
source:
  git_revision: 4336705cdafb13a569044fd7df2313c10e82e3ed
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
  - path: curation/causal_graphs/agricultural_soil.yaml
    sha256: 2f9c73b186d6b79df1d64098f929d8364a1768f732101edaf144dee7723c60f4
    role: context
  - path: curation/causal_graphs/aquatic_biome.yaml
    sha256: 03ba09d10f9a9d8d32060fc0208b511ef0d59e731fd7c63ca6c02296e70da5f5
    role: context
  - path: curation/causal_graphs/biofilm.yaml
    sha256: 37fae9d123c2edfb68376b6b4fe5441f72092d48d81dba6f60510087217c8680
    role: context
  - path: curation/causal_graphs/bioreactor.yaml
    sha256: 14eb020a26287751c86d1d6eab5c91cf606e0e8ea076832fce82e0646fb85cdd
    role: context
  - path: curation/causal_graphs/brackish_water.yaml
    sha256: b9d58082a53bef1143a3868918cfed7f6d74ba7e2330648069733d9ea2c76508
    role: context
  - path: curation/causal_graphs/building.yaml
    sha256: 9e9360775fdda554b285d7ecfb9b1729bf389b8241376a410eca60bd672eb235
    role: context
  - path: curation/causal_graphs/compost.yaml
    sha256: e0fd3ae54311115939f07ba1f3f158c5c44353bd0fab1dcdc1a9292ff0ad1de5
    role: context
  - path: curation/causal_graphs/deep_marine_sediment.yaml
    sha256: eb6a68290a58ec157a4c9895e082cbba760c47b5fbe35523d3bb163af3091d0c
    role: context
  - path: curation/causal_graphs/forest_soil.yaml
    sha256: faef7b6c26c25ba33110d362dc7e4351440bc08c1106f270e1e6f2decfb1e3f4
    role: context
  - path: curation/causal_graphs/forested_area.yaml
    sha256: eb96b992e1ee8fef7df2550c765a30f0d446082ce16592b6c1da44a54b34e427
    role: context
  - path: curation/causal_graphs/fresh_water.yaml
    sha256: e95ea96aa1912066d4c98cbff91e34528668d4c453d93dc4203c67e7769c691a
    role: context
  - path: curation/causal_graphs/fungi_associated_environment.yaml
    sha256: 45736893315a37e327c25d401ff8794fee47b1056347e52f4980bc3a58e8e0d8
    role: context
  - path: curation/causal_graphs/grassland_soil.yaml
    sha256: 81b2a9ea6255dfbd4b393102b9903dd3c9e8af12f7d3a9adc7c4649650542ae8
    role: context
  - path: curation/causal_graphs/hot_spring.yaml
    sha256: ee0f6d7f7eff179b44e1e934c1c801524062a7e71f3199e16e9ef35e7bad81ed
    role: context
  - path: curation/causal_graphs/hydrothermal_vent.yaml
    sha256: b5c101a93e724531cb7e50e8031203138230c09599855fe8a03bec945469efb0
    role: context
  - path: curation/causal_graphs/hypersaline_water.yaml
    sha256: e974d5e9cc241ac9daf3542ba11156915cfb7786e683ad5ad212af5b35006158
    role: context
  - path: curation/causal_graphs/intestine_environment.yaml
    sha256: 2ef766692eff55471a3322c0cd1cf82188decf37fd5ecd3535cb0ef612e2b725
    role: context
  - path: curation/causal_graphs/leaf.yaml
    sha256: fadc8027b39884bc16cf98f774804a84fd1b1d805876310a47a095f6019435cc
    role: context
  - path: curation/causal_graphs/liquid_water.yaml
    sha256: 12aac1021b9b51c6becc4ef8509bd63557b306e42c01d9b4443d69252ce29a81
    role: context
  - path: curation/causal_graphs/marine_sediment.yaml
    sha256: 8b230eb079171ab8134b648caa29878dc5015fb36362559a6a8c67fb2b433741
    role: context
  - path: curation/causal_graphs/marine_water_body.yaml
    sha256: b2f81102970e9541bf61978fabdd68b7db8f9459f1ef11b467fecfc2956f238b
    role: context
  - path: curation/causal_graphs/milk.yaml
    sha256: 049daa5b499096c61cb625b7bb9ac0f02ea216c96d6b5f7b77126c8709b2378d
    role: context
  - path: curation/causal_graphs/peat_soil.yaml
    sha256: 0f23fa02718b08e3607478ceaa2294320b320ae841a79e144e48ed3497db09e2
    role: context
  - path: curation/causal_graphs/plant_associated_environment.yaml
    sha256: 300044040f76234e7ed3bf373137ba224e55f48e3f3d6d505086b3830877cfcb
    role: context
  - path: curation/causal_graphs/plant_litter.yaml
    sha256: 25e10d6640992be2aa506490f763d8f9642fde125f599207dae7852b6a13b369
    role: context
  - path: curation/causal_graphs/root_nodule.yaml
    sha256: b363e5d418df93d6e44c9d3f3256c8b0ede7c4518125359ffb880020fc00721c
    role: context
  - path: curation/causal_graphs/sea_water.yaml
    sha256: 240ffc8ad2c0abf6f4cce41e01018679aca726816006c90ce329b8d1910d9cd7
    role: context
  - path: curation/causal_graphs/sediment.yaml
    sha256: 62b97afba9466dc64f8b5b1b3fd5d92f8b4b6bf96fe1c761af579ff7deca0e47
    role: context
  - path: curation/causal_graphs/sludge.yaml
    sha256: 55b9c9a27fd00c7b84a8780f2cedc83eeb31ebdda9a2e1029678d96a7fa4a06c
    role: context
  - path: curation/causal_graphs/soil.yaml
    sha256: 2a2bf4b1099b3bc69015f9530cf6e926c05c33667132234b3c52f06aacc957c2
    role: context
  - path: curation/causal_graphs/terrestrial_biome.yaml
    sha256: 239e6a2b711564ed12084cddd1295547d23858dd329c33c538251d5f53c88834
    role: context
  - path: curation/causal_graphs/waste_water.yaml
    sha256: 299b5128af6cf5f7a61ce53304f1084e6eb045414b47cbcfd8832de095142aef
    role: context
  - path: curation/decisions.tsv
    sha256: c2482c7441b08f593baa8bd59546ac68c6e5c7e4e1cb36c24c12a74592b9ff3c
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 2d41fc93db4939122b3909f2a412b84b679703948b10d9f02e12021442f71407
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 049c06712d6a8955abbccc1ae6d2ce81c63be9d144cb6327f5ce8e2a92826379
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: dab516ed83e20c01a1b537f4049cbfb2ce31b8a96ae90662a4a35ade3871a7bf
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: b59b9e800a918135e3915145d4d8098bb48dcea36a312b3004c594a57d221ae9
    role: context
  - path: data/habitats/engineered/anaerobic_bioreactor.yaml
    sha256: 7f19d345280589761e6d81807fbc2f00a96032befd90c8cecb17a0c8b835f837
    role: context
  - path: data/habitats/engineered/anaerobic_sludge_blanket_reactor.yaml
    sha256: 1b0c5cdd1dbacfab92fc561c3c14080584d12735a16bcd514e84d32071a44780
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
    sha256: f7aa39ee762d94f1902d9f08f328cb897bc543e4e226057eb4770d24bfcc6eb5
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20261007T032002Z-anaerobic_sludge_blanket_reactor.md
    sha256: d99b53ef6c533b97828e0494ecac77e4ab8a2fd04033571160c25017939ec394
    role: context
  - path: reviews/structured/20261011T024021Z-anaerobic_sludge_blanket_reactor/review.yaml
    sha256: abc6a9586d58153d79f59f40cd370211cae2bbe40cc379d994d83aa10e9d5659
    role: context
  - path: reviews/structured/20261011T025202Z-anaerobic_sludge_blanket_reactor-followup/review.yaml
    sha256: 2c3b5e58160f769ba55920edde8d7130a9fbdac5c3fb65fbf92ef9be97d58fb1
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/extract_gold_biosamples.py
    sha256: b6a2773c86fe718e1ca0b1d7b32709f0eee491ac813655e310aa0817c0fec31b
    role: context
  - path: scripts/extract_source_inventory.py
    sha256: 4bf5391d25ff48a2d81eb3821af6582de063fd0391440973d309dfd93016490c
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 52d2a22309a1f4a10728a663560bb4d918346c292221fd34139b99b4159d3fe5
    role: context
  - path: src/habitatmech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/habitatmech/seed.py
    sha256: 4adf105e23d75c3563a516a0c160623d1065df7fcb2f31b7a0a0a8303d0401be
    role: context
targets:
- target_id: ENVO:00002213
  path: data/habitats/engineered/anaerobic_sludge_blanket_reactor.yaml
  label: anaerobic sludge blanket reactor
  kind: generated
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/decisions.tsv
    role: Source-concept identity and broader grounding
  - repository: culturebotai/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Guarded GOLD context-parent correction
  - repository: culturebotai/HabitatMech
    path: curation/term_requests.tsv
    role: Authored habitat definition and genus
  - repository: culturebotai/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Frozen GOLD source concepts and unit-specific counts
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained generation and harmonization
scope:
  description: Bounded successor reassessing the precise correction and retaining
    the unresolved finding.
  selection: One exact previously reviewed record; no additional unique-record coverage.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - ENVO:00002213
checks:
- check_id: C2
  name: validate-uasb
  command: just validate data/habitats/engineered/anaerobic_sludge_blanket_reactor.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - ENVO:00002213
  summary: Actual run 2026-10-11T02:49:29Z to 2026-10-11T02:49:32Z. Native scope as
    commanded; full-corpus checks do not imply full-corpus scientific coverage.
- check_id: C3
  name: strict
  command: just validate-strict data/habitats/engineered/anammox.yaml data/habitats/engineered/anaerobic_sludge_blanket_reactor.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - ENVO:00002213
  summary: Actual run 2026-10-11T02:49:32Z to 2026-10-11T02:49:38Z. Native scope as
    commanded; full-corpus checks do not imply full-corpus scientific coverage.
- check_id: C4
  name: corpus
  command: just verify-corpus
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - ENVO:00002213
  summary: Actual run 2026-10-11T02:49:38Z to 2026-10-11T02:49:57Z. Native scope as
    commanded; full-corpus checks do not imply full-corpus scientific coverage.
- check_id: C5
  name: labels
  command: just validate-products
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - ENVO:00002213
  summary: Actual run 2026-10-11T02:49:57Z to 2026-10-11T02:51:10Z. Native scope as
    commanded; full-corpus checks do not imply full-corpus scientific coverage.
- check_id: C6
  name: history
  command: just validate-history
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - ENVO:00002213
  summary: Actual run 2026-10-11T02:51:10Z to 2026-10-11T02:51:17Z. Native scope as
    commanded; full-corpus checks do not imply full-corpus scientific coverage.
- check_id: C7
  name: causal
  command: just validate-causal-all
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - ENVO:00002213
  summary: Actual run 2026-10-11T02:51:17Z to 2026-10-11T02:51:24Z. Native scope as
    commanded; full-corpus checks do not imply full-corpus scientific coverage.
- check_id: C8
  name: terms
  command: just term-requests-check
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - ENVO:00002213
  summary: Actual run 2026-10-11T02:51:24Z to 2026-10-11T02:51:48Z. Native scope as
    commanded; full-corpus checks do not imply full-corpus scientific coverage.
- check_id: C9
  name: Focused hierarchy regression
  command: .venv/bin/python -m pytest -q tests/test_anammox_review_fix.py tests/test_gold_parent_exclusions.py
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - ENVO:00002213
  summary: 49 passed in 83.47 seconds. Whole-corpus with/without exclusion comparison
    changes exactly Anammox parent/history.
evidence:
- evidence_id: R
  kind: record_content
  reference: data/habitats/engineered/anaerobic_sludge_blanket_reactor.yaml
  locator: Entire current target YAML including all generated history
  summary: 'Retained predecessor evidence, with its original access timestamp: Retained
    predecessor evidence, with its original access timestamp: The active ENVO identity,
    upward-flow sludge-blanket definition and anaerobic-bioreactor genus agree. Source
    ranks and scores are faithful, but the sixth taxon lacks an available NCBI name.
    Defects in the parent record do not refute this direct ontology genus edge or
    authorize copying the parent biological content.'
  support: supports
  accessed_at: '2026-10-11T02:40:21.000000Z'
- evidence_id: RAW
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv; data/raw/prego_habitats.tsv; data/raw/bacdive_isolation_sources.tsv
  locator: Exact source IDs/full paths in target source_attestations; all captured
    GOLD rows
  summary: 'Retained predecessor evidence, with its original access timestamp: Retained
    predecessor evidence, with its original access timestamp: Frozen GOLD rows=[];
    emitted source assertions=[{"assertion_count": 6, "assertion_unit": "TAXON", "evidence_channels":
    "environmental_samples", "score": 1.11189, "source": "PREGO", "source_id": "ENVO:00002213",
    "source_label": "anaerobic sludge blanket reactor"}]. Exact aggregate counts and
    first-node convention checked against source tables. GOLD counts ORGANISM, PREGO
    TAXON and BacDive STRAIN. Zero frozen GOLD counts are omitted, not evidence that
    no samples exist; unlike units are never summed.'
  support: supports
  accessed_at: '2026-10-11T02:40:21.000000Z'
- evidence_id: OWN
  kind: record_content
  reference: curation/decisions.tsv; curation/gold_parent_exclusions.tsv; curation/term_requests.tsv
  locator: Exact source-key rows with current line numbers
  summary: 'Retained predecessor evidence, with its original access timestamp: Retained
    predecessor evidence, with its original access timestamp: {}. Empty target definition
    rows mean no maintained authored definition in these tables, not a global ontology
    absence. Other targets using this ID as parent are not target decisions.'
  support: supports
  accessed_at: '2026-10-11T02:40:21.000000Z'
- evidence_id: CODE
  kind: record_content
  reference: src/habitatmech/seed.py; src/habitatmech/extract.py; src/habitatmech/schema/habitatmech.yaml
  locator: ConceptStore.get, _decided, resolve_gold, ingest_gold, source-specific
    attestation ingestion and SourceAttestation.mapping_predicate
  summary: 'Retained predecessor evidence, with its original access timestamp: Retained
    predecessor evidence, with its original access timestamp: Schema endpoints are
    source concept -> generated record identifier. The NARROW lexical route retains
    a source mint but emits a predicate to its implicit ontology parent. Ontology
    TSV synonyms lack scope and ConceptStore.get emits them exact. GOLD ancestor and
    CLOSE/BROAD guards do not repair all ontology scopes or condition adjectives.
    Current explicit PREGO GROUND-predicate and BacDive override-note fixes are not
    treated as still-unfixed bugs.'
  support: supports
  accessed_at: '2026-10-11T02:40:21.000000Z'
- evidence_id: RULES
  kind: authority
  reference: docs/CURATION.md; docs/HARMONIZATION.md; docs/record-review-profile.md;
    .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Local habitat identity, strict is-a, source units, optional fields and
    native lifecycle rules
  summary: 'Retained predecessor evidence, with its original access timestamp: Retained
    predecessor evidence, with its original access timestamp: Parents must be strictly
    broader, not container, treatment output or feed. REVIEWED requires ITEM decisions
    for all contributing source concepts but is not scientific proof. CLASS/SEEDED
    and empty optional fields alone are not major defects; source associations do
    not establish characteristic taxa or mechanisms.'
  support: supports
  accessed_at: '2026-10-11T02:40:21.000000Z'
- evidence_id: PARENTS
  kind: record_content
  reference: data/habitats/engineered/anaerobic_sludge_blanket_reactor.yaml
  locator: Each actual parent resolved through current corpus where present; external
    ontology parents checked separately
  summary: 'Retained predecessor evidence, with its original access timestamp: Retained
    predecessor evidence, with its original access timestamp: {"ENVO:00002124": {"definition":
    "A bioreactor in which the contained material is not oxygenated (i.e. void of
    biologically consequential free oxygen)", "identifier": "ENVO:00002124", "label":
    "anaerobic bioreactor", "parent_habitats": ["ENVO:00002123", "ENVO:03600010",
    "habitatmech:GOLD.24cf427e7d", "habitatmech:GOLD.32c2a98ae8", "habitatmech:GOLD.3af6ca6cc3"],
    "path": "data/habitats/engineered/anaerobic_bioreactor.yaml", "source_attestations":
    [{"assertion_count": 131, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:exactMatch",
    "notes": "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.",
    "source": "GOLD", "source_id": "gold.ecosystem:4440", "source_label": "Anaerobic",
    "source_path": "Engineered > Bioreactor > Anaerobic"}, {"mapping_predicate": "skos:exactMatch",
    "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.",
    "source": "GOLD", "source_id": "gold.ecosystem:7768", "source_label": "Anaerobic",
    "source_path": "Engineered > Bioreactor > Semi-continuous > Anaerobic"}, {"mapping_predicate":
    "skos:exactMatch", "notes": "2 GOLD ecosystem node ids share this path; first
    shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id":
    "gold.ecosystem:8151", "source_label": "Anaerobic", "source_path": "Engineered
    > Bioreactor > SSF (Solid state fermentation) > Anaerobic"}, {"mapping_predicate":
    "skos:exactMatch", "notes": "2 GOLD ecosystem node ids share this path; first
    shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id":
    "gold.ecosystem:8271", "source_label": "Anaerobic", "source_path": "Engineered
    > Bioreactor > MBR (Membrane bioreactor) > Anaerobic"}, {"mapping_predicate":
    "skos:exactMatch", "notes": "2 GOLD ecosystem node ids share this path; first
    shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id":
    "gold.ecosystem:8426", "source_label": "Anaerobic", "source_path": "Engineered
    > Bioreactor > DHS reactor > Anaerobic"}, {"assertion_count": 81, "assertion_unit":
    "TAXON", "evidence_channels": "environmental_samples", "score": 4.0, "source":
    "PREGO", "source_id": "ENVO:00002124", "source_label": "anaerobic bioreactor"}]}}.
    Only parent identity and direct relationship scope assessed; no inherited taxon,
    parameter or mechanism claims and no full scientific parent review.'
  support: context_only
  accessed_at: '2026-10-11T02:40:21.000000Z'
- evidence_id: O-ENVO-00002124
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002124
  locator: Exact current official OLS identifier, label, definition and eligibility
    response
  summary: 'Retained predecessor evidence, with its original access timestamp: Retained
    predecessor evidence, with its original access timestamp: {"description": ["A
    bioreactor in which the contained material is not oxygenated (i.e. void of biologically
    consequential free oxygen)"], "is_obsolete": false, "label": "anaerobic bioreactor",
    "obo_id": "ENVO:00002124", "term_replaced_by": null}'
  support: supports
  accessed_at: '2026-10-10T23:51:38.534785Z'
  snapshot_sha256: 100dc16e36bbc3c0c495513c57c8ec0219cb408f5c82dc2a97975f1d03c80bd9
- evidence_id: O-ENVO-00002213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002213
  locator: Exact current official OLS identifier, label, definition and eligibility
    response
  summary: 'Retained predecessor evidence, with its original access timestamp: Retained
    predecessor evidence, with its original access timestamp: {"description": ["An
    anaerobic bioreactor which is capable of treating wastewater through the action
    of methanogenic microbes which form a blanket of sludge due to the upward flow
    in the reactor."], "is_obsolete": false, "label": "anaerobic sludge blanket reactor",
    "obo_id": "ENVO:00002213", "term_replaced_by": null}'
  support: supports
  accessed_at: '2026-10-10T23:51:39.714277Z'
  snapshot_sha256: 5aa3cb720ba515baa39a380f1d9a14997a90bdc55e5de2fb07cf5b370b21fa0c
- evidence_id: ENVO
  kind: authority
  reference: https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.obo
  locator: Relevant complete term stanzas, typed synonyms and direct is-a assertions
    in official ENVO OBO
  summary: 'Retained predecessor evidence, with its original access timestamp: Retained
    predecessor evidence, with its original access timestamp: Anaerobic bioreactor
    has bioreactor genus, not membrane/DHS/SSF/semi-continuous genera. Anaerobic sludge
    is sludge with anaerobic quality; digester sludge is below anaerobic sludge. Animal
    cage has manufactured-cage genus and BROAD cage alias. Animal waste has organic-waste
    genus and BROAD animal waste alias. Aquaculture farm has agricultural-ecosystem
    genus and BROAD aquaculture/aquafarming aliases. Target and parent terms were
    compared to the captured slice without rewriting either source.'
  support: supports
  accessed_at: '2026-10-10T23:51:45.598388Z'
  snapshot_sha256: 7f5a6580d1b59166da07a54f9aa907a76f86079b7082e089192f04df91fd7d5b
- evidence_id: GOLD
  kind: authority
  reference: https://gold.jgi.doe.gov/ecosystem_classification
  locator: Five-level classification guidance, especially Ecosystem and Ecosystem
    Category
  summary: 'Retained predecessor evidence, with its original access timestamp: Retained
    predecessor evidence, with its original access timestamp: GOLD describes sample
    surroundings, with progressively more specific environment categories. This supports
    reading the whole source path; an activity-like leaf need not denote only a process.
    It does not make every hierarchical link an is-a or resolve setting versus specimen
    material automatically.'
  support: supports
  accessed_at: '2026-10-11T02:40:21.000000Z'
- evidence_id: CLASS
  kind: database
  reference: https://gold.jgi.doe.gov/
  locator: Retained classification workbook site data; SHA256 3933e5f0664915c1bbfa00212e17d013da360fb33dd52e509254050813135396
  summary: 'Retained predecessor evidence, with its original access timestamp: Retained
    predecessor evidence, with its original access timestamp: Exact filler-stripped
    path rows=[]. All 2422 classification rows scanned. No exact GOLD path is expected
    for a PREGO-only target. The retained workbook is not asserted to be a new live
    download.'
  support: supports
  accessed_at: '2026-10-10T23:54:14.965506Z'
- evidence_id: BULK
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=site_excel
  locator: Retained later workbook exact-path member census and accession joins; SHA256
    5f48b2f50fb2a9257754960a0f0e12dc6e8fa121e97c3e9f4497249e5fe6e439
  summary: 'Retained predecessor evidence, with its original access timestamp: Retained
    predecessor evidence, with its original access timestamp: Counts={"Biosample":
    0, "Organism": 0, "SequencingProject": 0}; distinct joined studies=0; inspected
    examples={"Biosample": [], "Organism": []}; common collection-site values={"Biosample":
    [], "Organism": []}. Full Biosample, Organism, SequencingProject and Study sheets
    scanned, including headers: 244951, 532019, 636914 and 63806 rows. Counts are
    separate per unit and snapshot. This does not reconstruct frozen source members
    or establish ecological replication.'
  support: supports
  accessed_at: '2026-10-10T23:54:14.965506Z'
- evidence_id: CONTEXT
  kind: database
  reference: data/raw/gold_path_biosamples.tsv; data/raw/gold_path_triads.tsv; data/raw/gold_studies.tsv
  locator: Exact canonical-path fields and pipe-delimited study-path memberships
  summary: 'Retained predecessor evidence, with its original access timestamp: Retained
    predecessor evidence, with its original access timestamp: Biosample rows=[]; triads=[];
    study IDs and lines=[]. MIxS broad, local and medium roles are separate. Triad
    rows that merely mention the target ontology ID for a different source path are
    not contributing target assertions. No descendant counts or claims are inherited.'
  support: supports
  accessed_at: '2026-10-11T02:40:21.000000Z'
- evidence_id: TAX
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1000562%2C1004316%2C1004322%2C1004326%2C1005%2C1031541%2C103810%2C104102%2C104245%2C1045010%2C1046128%2C108486%2C1119058%2C1121001%2C1121025%2C1121275%2C1121423%2C1121921%2C1121950%2C1131567%2C114628%2C114707%2C1150776%2C1178540%2C1194427%2C121845%2C1264%2C1265%2C1270%2C1278308%2C1282%2C1286%2C1291048%2C1299%2C134533%2C1348%2C1352%2C1363%2C1366%2C1391%2C1397%2C1423814%2C1472%2C147810%2C148604%2C1494%2C149712%2C1502%2C1505%2C1511%2C1512%2C152%2C1530%2C1534%2C153496%2C153501%2C1553%2C156%2C1580%2C158192%2C164393%2C173%2C1855%2C186741%2C197222%2C200125%2C202748%2C214688%2C246432%2C258475%2C266940%2C28122%2C28251%2C28262%2C286698%2C288%2C29290%2C29355%2C295236%2C29549%2C31910%2C322009%2C330214%2C335543%2C33936%2C33954%2C411463%2C411467%2C412614%2C417399%2C42353%2C438%2C445335%2C457416%2C457431%2C469371%2C485916%2C492476%2C498761%2C517543%2C526588%2C53249%2C548474%2C55518%2C60890%2C644383%2C651%2C666%2C678%2C679937%2C85963%2C887929%2C946678%2C96773%2C99656&retmode=xml
  locator: Exact target subset of NCBI Taxonomy efetch; TaxId, ScientificName and
    AkaTaxIds compared with all retained raw association rows
  summary: 'Retained predecessor evidence, with its original access timestamp: Retained
    predecessor evidence, with its original access timestamp: Verified target rows=[{"line":
    6299, "path": "data/raw/prego_habitat_taxa.tsv", "row": {"channels": "environmental_samples",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002213", "prego_score":
    "1.11189", "rank": "1", "taxon_id": "NCBITaxon:202748", "taxon_label": "Saprospira
    sp. SS98-5"}}, {"line": 6300, "path": "data/raw/prego_habitat_taxa.tsv", "row":
    {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE",
    "prego_id": "ENVO:00002213", "prego_score": "1.10193", "rank": "2", "taxon_id":
    "NCBITaxon:417399", "taxon_label": "Vibrio cholerae NCTC 8457"}}, {"line": 6301,
    "path": "data/raw/prego_habitat_taxa.tsv", "row": {"channels": "environmental_samples",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002213", "prego_score":
    "1.05112", "rank": "3", "taxon_id": "NCBITaxon:42353", "taxon_label": "Nitrosomonas
    sp."}}, {"line": 6302, "path": "data/raw/prego_habitat_taxa.tsv", "row": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:00002213", "prego_score": "1.04421", "rank": "4", "taxon_id": "NCBITaxon:85963",
    "taxon_label": "Helicobacter pylori J99"}}, {"line": 6303, "path": "data/raw/prego_habitat_taxa.tsv",
    "row": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "ENVO:00002213", "prego_score": "1.03669", "rank": "5", "taxon_id":
    "NCBITaxon:96773", "taxon_label": "Thauera chlorobenzoica"}}, {"line": 6304, "path":
    "data/raw/prego_habitat_taxa.tsv", "row": {"channels": "environmental_samples",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002213", "prego_score":
    "1.01893", "rank": "6", "taxon_id": "NCBITaxon:517543", "taxon_label": ""}}].
    Every populated target name matches current NCBI. Unnamed 517543 resolves Toxopoda
    sp. 2 RM-2008; 121845 resolves Diaphorina citri; 147810 is an explicit alias of
    1606 Ligilactobacillus aviarius where those IDs occur. Scores/counts/ranks and
    candidate pools match frozen inputs. No row is marked is_characteristic. This
    verifies source representation and identity, not all original ecological observations.'
  support: supports
  accessed_at: '2026-10-10T23:51:46.526466Z'
  snapshot_sha256: 08ed4bae47d8c7a6639fa0dc13cf222e1e838dd06485b1bf17025ce1b862ddab
- evidence_id: SEARCH
  kind: search
  reference: curation/; history/; research/; reports/; reviews/; data/raw/; data/habitats/;
    conf/
  locator: Saved ignored-inclusive support-search receipt, structured current-corpus/review
    inventory and exact TSV/overlay target scans
  summary: 'Retained predecessor evidence, with its original access timestamp: Retained
    predecessor evidence, with its original access timestamp: No completed structured
    review covered this exact target at the refreshed baseline. All 32 maintained
    overlay target IDs were parsed; none targets these selected records. No selected
    target has a maintained authored definition row. Legacy reports and relevant history
    were located; optional sparsity is not treated as a defect.'
  support: context_only
  accessed_at: '2026-10-11T02:40:21.000000Z'
  search_scope: rg --no-ignore --hidden -F for target identifiers, labels, slugs,
    source IDs and full paths across named roots; Path.rglob includes ignored/hidden
    corpus/reviews/history. Original GOLD data/raw/gold directory was unavailable
    at the configured kg-microbe root; no whole-filesystem absence claim.
- evidence_id: LEGACY
  kind: prior_review
  reference: reports/yaml_record_review/20261007T032002Z-anaerobic_sludge_blanket_reactor.md
  locator: Exact-target prior report findings compared with current captured inputs
  summary: 'Retained predecessor evidence, with its original access timestamp: Retained
    predecessor evidence, with its original access timestamp: The legacy missing taxon-name
    finding is independently confirmed against the current raw row and NCBI response.
    It remains minor; no required identity field is broken.'
  support: context_only
  accessed_at: '2026-10-11T02:40:21.000000Z'
- evidence_id: VALID
  kind: validation
  reference: justfile
  locator: Original gates 0-17 plus fresh resume gate logs; unchanged base/input hashes
    verified
  summary: 'Retained predecessor evidence, with its original access timestamp: Retained
    predecessor evidence, with its original access timestamp: Sixteen target LinkML
    checks and the 16-record strict check passed; 3208 records reproduced exactly.
    Fresh label gate completed with 1178 canonical, 1 synonym, 5 accepted exceptions
    and 2057 no-adapter skips. All 293 histories, 32 causal overlays and 109 term
    requests passed. The earlier permission-interrupted label run is NOT a pass despite
    exit 0; all interrupted remaining gates were rerun. Deterministic validation is
    not scientific approval.'
  support: supports
  accessed_at: '2026-10-11T02:40:21.000000Z'
- evidence_id: CURRENT
  kind: record_content
  reference: data/habitats/engineered/anaerobic_sludge_blanket_reactor.yaml
  locator: Complete current record, maintained owner rows and exact source assertions
  accessed_at: '2026-10-11T02:53:44Z'
  support: supports
  summary: 'The missing-name finding remains a minor, open provenance gap for NCBITaxon:517543
    alone, verified as Toxopoda sp. 2 RM-2008. Retains the prior #1895 correction
    to original review 20261011T024021Z-anaerobic_sludge_blanket_reactor F1, which
    copied an unrelated animal-house 147810-to-1606 alias clause (#1895). The UASB
    record and raw PREGO inventory have not changed; governed source refresh remains
    in #1897. Validation-target metadata (#1898) is corrected by retaining only the
    applicable single-record check; both original executions are preserved in the
    preceding observation.'
- evidence_id: PREDECESSOR
  kind: prior_review
  reference: reviews/structured/20261011T025202Z-anaerobic_sludge_blanket_reactor-followup/review.yaml
  locator: F1 and its precise evidence/limitations
  accessed_at: '2026-10-11T02:53:44Z'
  support: context_only
  summary: Immutable original retained; F1 remains open with exact lineage.
- evidence_id: CORRECTION
  kind: record_content
  reference: reviews/structured/20261011T025202Z-anaerobic_sludge_blanket_reactor-followup/review.yaml
  locator: F1 description compared with exact raw taxon row and NCBI response
  accessed_at: '2026-10-11T02:53:44Z'
  support: supports
  summary: The exact PREGO association for NCBITaxon:517543 omits its taxon label
    in both the frozen inventory and generated UASB record. NCBI returns the exact
    same identifier with ScientificName Toxopoda sp. 2 RM-2008. No alias migration
    is involved for this target. The identifier resolves; the name omission is not
    a broken reference, serialization loss or characteristic-ecology claim.
- evidence_id: CHECKS
  kind: validation
  reference: tests/test_anammox_review_fix.py
  locator: 49 focused tests plus fresh native validation receipts
  accessed_at: '2026-10-11T02:53:44Z'
  support: supports
  summary: Full corpus comparison changes only Anammox parent/history; all source
    counts, units, identifiers, taxa and statuses are unchanged. Current native checks
    pass. These are deterministic results, not independent scientific review.
assessments:
- assessment_id: A1
  area: provenance
  topic: Preserved source identity and association scope
  outcome: supported
  target_ids:
  - ENVO:00002213
  evidence_ids:
  - CURRENT
  - RAW
  - CORRECTION
  summary: 'Exact identity, source assertions, counts/units and native status are
    preserved. No observed taxon is promoted to characteristic ecology. The missing-name
    finding remains a minor, open provenance gap for NCBITaxon:517543 alone, verified
    as Toxopoda sp. 2 RM-2008. Retains the prior #1895 correction to original review
    20261011T024021Z-anaerobic_sludge_blanket_reactor F1, which copied an unrelated
    animal-house 147810-to-1606 alias clause (#1895). The UASB record and raw PREGO
    inventory have not changed; governed source refresh remains in #1897. Validation-target
    metadata (#1898) is corrected by retaining only the applicable single-record check;
    both original executions are preserved in the preceding observation.'
- assessment_id: A2
  area: representation
  topic: Remaining predecessor finding
  outcome: concern
  target_ids:
  - ENVO:00002213
  evidence_ids:
  - CURRENT
  - PREDECESSOR
  - CORRECTION
  summary: The exact PREGO association for NCBITaxon:517543 omits its taxon label
    in both the frozen inventory and generated UASB record. NCBI returns the exact
    same identifier with ScientificName Toxopoda sp. 2 RM-2008. No alias migration
    is involved for this target. The identifier resolves; the name omission is not
    a broken reference, serialization loss or characteristic-ecology claim.
findings:
- finding_id: F1
  issue_key: envo-00002213-missing-resolvable-taxon-labels
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: One resolvable PREGO taxon name remains omitted
  description: The exact PREGO association for NCBITaxon:517543 omits its taxon label
    in both the frozen inventory and generated UASB record. NCBI returns the exact
    same identifier with ScientificName Toxopoda sp. 2 RM-2008. No alias migration
    is involved for this target. The identifier resolves; the name omission is not
    a broken reference, serialization loss or characteristic-ecology claim.
  target_ids:
  - ENVO:00002213
  field_paths:
  - characteristic_taxa
  evidence_ids:
  - R
  - TAX
  - CURRENT
  - PREDECESSOR
  - CORRECTION
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator for proposed correction
  - repository: culturebotai/HabitatMech
    path: data/raw/prego_habitat_taxa.tsv
    role: Maintained input or generator for proposed correction
  rule_id: HabitatMech:provenance
  native_severity: minor
  normalization_reason: Bounded source-label completeness gap; identifier and habitat
    identity remain resolvable.
  previous_occurrences:
  - repository: culturebotai/HabitatMech
    review_id: 20261011T025202Z-anaerobic_sludge_blanket_reactor-followup
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1897
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - ENVO:00002213
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator for proposed correction
  - repository: culturebotai/HabitatMech
    path: data/raw/prego_habitat_taxa.tsv
    role: Maintained input or generator for proposed correction
  generator: src/habitatmech/seed.py
  description: Refresh names through governed taxonomy inputs with explicit alias
    handling. Preserve original source IDs and evidence; inspect canonicalization
    collisions before any identifier or rank changes.
  acceptance_checks:
  - Missing names agree with versioned NCBI evidence; valid source aliases remain
    traceable.
  - Ranks, candidate-pool sizes, scores and habitat scope remain unchanged unless
    separately justified.
  - Use maintained inputs, never patch generated habitat YAML or pages.
  - Preserve full source provenance, snapshot-specific counts/units and unrelated
    inputs; inspect an exact forced seed canary before authorized regeneration.
  - Append required curation history, run full native QC and relevant ontology/provenance
    checks, and save an immutable linked reassessment. Actions are proposals, not
    executed fixes.
limitations:
- Adversarial self-review, not independent approval.
- Validation receipts precede this reporting correction; SHA256 comparisons establish
  that every captured input is unchanged since those runs. No gate is claimed to have
  rerun merely because its metadata was corrected.
- This observation does not claim full publication QC or map/site completion; those
  are required before merge.
- Original frozen GOLD member reconstruction is unavailable at the configured location.
  Later workbook evidence does not certify frozen member counts or exact source meaning.
- Configured taxon-label and unsupported-ontology adapter gaps remain; passing native
  gates do not repair them.
- 'Other open findings and shared issues #1249, #1398, #1614, #1896 and #1897 remain;
  no SSSOM/KGX readiness certification.'
related_reviews:
- repository: culturebotai/HabitatMech
  review_id: 20261011T025202Z-anaerobic_sludge_blanket_reactor-followup
  relationship: Scoped successor preserving original bytes and exact open-finding
    lineage.
```
