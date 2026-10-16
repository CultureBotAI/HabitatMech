# Record review: Cecum/Intestinal cecum (habitatmech:GOLD.37d9cdc188)

- Review: 20261015T235742Z-cecum_intestinal_cecum-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T23:39:40Z
- Finished UTC: 2026-10-15T23:57:42Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The molluscan Cecum/Intestinal cecum now remains minted and UNGROUNDED/REVIEWED, separated from vertebrate ileocecal anatomy and PREGO taxa. Primary Octopus maya dissection describes a cecum in different digestive context. This bounded witness is not exact identification of the GOLD specimen or a proposed replacement genus. The prior multi-target remediation remains unchanged.

## Scope And Provenance

Full field-by-field scientific assessment of this exact generated target at 0eb609a7ddb34925067116af806e26c165e10678.

Selection: Stale cecum individual observation plus the next 23 identifiers lacking completed individual-kind reviews in the ignored-inclusive 3209-record census. This bundle assesses one resolved record; previous batch reviews remain valid history.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 0eb609a7ddb34925067116af806e26c165e10678.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.37d9cdc188 | data/habitats/host_associated/cecum_intestinal_cecum.yaml | generated | Cecum/Intestinal cecum |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.37d9cdc188 | Finished 2026-10-15T23:44:39Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/cecum_intestinal_cecum.yaml |
| validate-strict | passed | True | habitatmech:GOLD.37d9cdc188 | Finished 2026-10-15T23:45:51Z. uv run python scripts/validate_strict.py data/habitats/host_associated/cecum.yaml data/habitats/host_associated/cardiac_stomach.yaml data/habitats/host_associated/cecum__d677e5d7.yaml data/habitats/host_associated/cecum_intestinal_cecum.yaml data/habitats/host_associated/cecum_mucosa.yaml data/habitats/host_associated/cell_culture.yaml data/habitats/host_associated/cell_line.yaml data/habitats/host_associated/cell_line__59b8224e.yaml data/habitats/host_associated/cell_line__d7fc8c60.yaml data/habitats/host_associated/cellulitis.yaml data/habitats/host_associated/central_nervous_system.yaml data/habitats/host_associated/cephalochordata.yaml data/habitats/host_associated/cephalothorax.yaml data/habitats/host_associated/cerebellum.yaml data/habitats/host_associated/cerebrospinal_fluid.yaml data/habitats/host_associated/cerebrospinal_fluid__93998265.yaml data/habitats/host_associated/cerebrospinal_fluid__b2fc1889.yaml data/habitats/host_associated/cerebrospinal_fluid__e3d236b3.yaml data/habitats/host_associated/cerebrospinal_fluid__f9e9497c.yaml data/habitats/host_associated/ceros.yaml data/habitats/host_associated/cerumen.yaml data/habitats/host_associated/cerumen_gland.yaml data/habitats/host_associated/cervical.yaml data/habitats/host_associated/cervical_adenocarcinoma_cell.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | habitatmech:GOLD.37d9cdc188 | Finished 2026-10-15T23:46:04Z. No issues found<br>829 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | habitatmech:GOLD.37d9cdc188 | Finished 2026-10-15T23:46:05Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | habitatmech:GOLD.37d9cdc188 | Finished 2026-10-15T23:46:28Z. expected 3209 records, found 3209 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | habitatmech:GOLD.37d9cdc188 | Finished 2026-10-15T23:46:34Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | habitatmech:GOLD.37d9cdc188 | Finished 2026-10-15T23:46:59Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | habitatmech:GOLD.37d9cdc188 | Finished 2026-10-15T23:48:03Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1173<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2063<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-baseline native QC | passed | True | habitatmech:GOLD.37d9cdc188 | Verified 2026-10-15T23:55:08Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38822113212 |
| Standalone evidence-reference validator applicability | not_applicable | False | habitatmech:GOLD.37d9cdc188 | No standalone citation/reference validator is documented for these evidence-free generated records. Target EvidenceItems and causal edges are absent. Stable source and ontology/taxon references were checked manually and with documented native gates; current-decision primary citations were separately verified where present. |

## Scientific And Domain Assessments

### Identity, definition, category, aliases and hierarchy

identity: supported. Targets: habitatmech:GOLD.37d9cdc188.

The molluscan Cecum/Intestinal cecum now remains minted and UNGROUNDED/REVIEWED, separated from vertebrate ileocecal anatomy and PREGO taxa. Primary Octopus maya dissection describes a cecum in different digestive context. This bounded witness is not exact identification of the GOLD specimen or a proposed replacement genus. The prior multi-target remediation remains unchanged.

### Source assertions, pools, ranks and supplementary context

quantity: supported. Targets: habitatmech:GOLD.37d9cdc188.

All emitted counts/units, labels, ranks, scores and candidate pools match exact frozen rows. [{"source": "GOLD", "count": 0, "unit": "ORGANISM"}]. Zero tree counts are omitted; later biosamples and study memberships are not added. Current taxonomy resolves displayed identifiers including explicit aliases.

### Biological support and bounded source uncertainty

evidence: supported. Targets: habitatmech:GOLD.37d9cdc188.

The molluscan Cecum/Intestinal cecum now remains minted and UNGROUNDED/REVIEWED, separated from vertebrate ileocecal anatomy and PREGO taxa. Primary Octopus maya dissection describes a cecum in different digestive context. This bounded witness is not exact identification of the GOLD specimen or a proposed replacement genus. The prior multi-target remediation remains unchanged.

### Native status, optional parameters and causal mechanisms

completeness: supported. Targets: habitatmech:GOLD.37d9cdc188.

Executed native resolution reproduces UNGROUNDED/REVIEWED. No environmental parameters, causal graphs, discussions, datasets or is_characteristic=true claims are present. Missing optional fields and SEEDED status alone are not defects; parent mechanisms are not inherited.

### Native validation and reproduction

schema: supported. Targets: habitatmech:GOLD.37d9cdc188.

Target schema/strict checks, 829 histories, source provenance, exact 3209-record reproduction, 32 causal overlays, 110 term requests and configured label checks passed. Exact-base remote full QC passed. Deterministic validity is separate from scientific support; reference-check applicability is stated explicitly.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/cecum_intestinal_cecum.yaml; Entire target YAML | supports | All fields, attestations, taxa and generated history read. |
| ERULE | docs/CURATION.md; Identity, strict broader hierarchy and evidence rules | supports | Organism, disease, material and habitat identities remain distinct. Parents must be strictly broader, not merely containing sites. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; HabitatRecord, SourceAttestation and TaxonAssociation | supports | Mapping predicate endpoint is source-to-record; source association is weaker than characteristic presence. Optional fields and native review status have distinct contracts. |
| ESEED | src/habitatmech/seed.py; Executed native source routes and complete document reproduction | supports | [{"mint": "habitatmech:GOLD.37d9cdc188", "automatic": {"identifier": "habitatmech:GOLD.37d9cdc188", "grounding_status": "UNGROUNDED", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "gold_unmatched", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "habitatmech:GOLD.37d9cdc188", "grounding_status": "UNGROUNDED", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "curated_confirm_ungrounded_from_gold_unmatched", "category": null, "reviewed": true, "decision": {"identifier": "habitatmech:GOLD.37d9cdc188", "decision": "CONFIRM_UNGROUNDED", "object_id": "", "object_label": "", "grounding_status": "", "curator": "codex-gpt-5", "date": "2026-10-15", "notes": "ITEM reassessment https://github.com/CultureBotAI/HabitatMech/issues/2208 : This molluscan source does not denote the vertebrate ileocecal or large-intestinal anatomy of UBERON:0001153 or BTO:0000166. Current OLS definitions and Uberon taxon notes distinguish invertebrate homonyms; octopus dissection (https://pubmed.ncbi.nlm.nih.gov/39140156/ ; DOI:10.1242/bio.060429) is a bounded anatomical witness, not identification of the exact GOLD specimen. Retain the source mint UNGROUNDED without inventing an alternative genus. Separate only this GOLD source from PREGO BTO:0000166; retain PREGO identity, 549-taxon pool and displayed associations unchanged. This supersedes the 2026-08-12 grounding and its truncated path; the prior decision is preserved in Git, immutable baseline review and the regression fixture. The whole-organ context contribution is excluded under #2206. Path: Host-associated &gt; Mollusca &gt; Digestive system &gt; Hindgut &gt; Cecum/Intestinal cecum", "review_depth": "ITEM", "category": "", "relation": "parent"}}}] |
| EEXTRACT | src/habitatmech/extract.py; Source counts, channels and taxon ranking | supports | Exact frozen rows reproduce counts/units and ranked taxon scores. The committed projection does not retain original PREGO pair citation links. |
| ET5 | data/raw/gold_ecosystem_paths.tsv; Physical TSV rows 2479 | supports | [{"row": 2479, "data": {"canonical_path": "Host-associated &gt; Mollusca &gt; Digestive system &gt; Hindgut &gt; Cecum/Intestinal cecum", "ecosystem": "Host-associated", "ecosystem_category": "Mollusca", "ecosystem_type": "Digestive system", "ecosystem_subtype": "Hindgut", "specific_ecosystem": "Cecum/Intestinal cecum", "leaf_label": "Cecum/Intestinal cecum", "depth": "5", "gold_node_count": "1", "organism_count": "0", "study_count": "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids": "gold.ecosystem:7832"}}] |
| ET6 | curation/gold_parent_exclusions.tsv; Physical TSV rows 15 | supports | [{"row": 15, "data": {"identifier": "habitatmech:GOLD.37d9cdc188", "source_path": "Host-associated &gt; Mollusca &gt; Digestive system &gt; Hindgut &gt; Cecum/Intestinal cecum", "parent_id": "habitatmech:GOLD.c336fb0bb7", "curator": "codex-gpt-5", "date": "2026-10-15", "notes": "Review https://github.com/CultureBotAI/HabitatMech/issues/2206 : This anatomical component or derived material is not a subtype of the containing organ or system. Exclude only the exact GOLD contribution; retain independent valid genera and original source observations. This does not resolve the separate catarrh condition/material scope or shared mapping endpoint #1398."}}] |
| ET7 | curation/decisions.tsv; Physical TSV rows 413 | supports | [{"row": 413, "data": {"identifier": "habitatmech:GOLD.37d9cdc188", "decision": "CONFIRM_UNGROUNDED", "object_id": "", "object_label": "", "grounding_status": "", "curator": "codex-gpt-5", "date": "2026-10-15", "notes": "ITEM reassessment https://github.com/CultureBotAI/HabitatMech/issues/2208 : This molluscan source does not denote the vertebrate ileocecal or large-intestinal anatomy of UBERON:0001153 or BTO:0000166. Current OLS definitions and Uberon taxon notes distinguish invertebrate homonyms; octopus dissection (https://pubmed.ncbi.nlm.nih.gov/39140156/ ; DOI:10.1242/bio.060429) is a bounded anatomical witness, not identification of the exact GOLD specimen. Retain the source mint UNGROUNDED without inventing an alternative genus. Separate only this GOLD source from PREGO BTO:0000166; retain PREGO identity, 549-taxon pool and displayed associations unchanged. This supersedes the 2026-08-12 grounding and its truncated path; the prior decision is preserved in Git, immutable baseline review and the regression fixture. The whole-organ context contribution is excluded under #2206. Path: Host-associated &gt; Mollusca &gt; Digestive system &gt; Hindgut &gt; Cecum/Intestinal cecum", "review_depth": "ITEM", "category": "", "relation": "parent"}}] |
| EH8 | history/mappings/cardiac_cartilage_cecum_review/2026-10-15T214400Z-codex-gpt-5-909775.yaml; Historical context; not independent primary evidence | supports | Inspected history, research or prior assessment informs provenance only. Historical unavailability and broad negative claims are not adopted as current facts. No previous finding is closed or narrowed by this new individual observation. |
| EH9 | history/mappings/cardiac_molluscan_citation_format/2026-10-15T221623Z-codex-gpt-5-cea5ff.yaml; Historical context; not independent primary evidence | supports | Inspected history, research or prior assessment informs provenance only. Historical unavailability and broad negative claims are not adopted as current facts. No previous finding is closed or narrowed by this new individual observation. |
| EH10 | history/mappings/cardiac_stomach/2026-10-15T214401Z-codex-gpt-5-ac65b1.yaml; Historical context; not independent primary evidence | supports | Inspected history, research or prior assessment informs provenance only. Historical unavailability and broad negative claims are not adopted as current facts. No previous finding is closed or narrowed by this new individual observation. |
| EH11 | history/mappings/cecum/2026-10-15T214403Z-codex-gpt-5-cf5c53.yaml; Historical context; not independent primary evidence | supports | Inspected history, research or prior assessment informs provenance only. Historical unavailability and broad negative claims are not adopted as current facts. No previous finding is closed or narrowed by this new individual observation. |
| EH12 | reviews/structured/20261015T224445Z-cecum-remediation/review.yaml; Historical context; not independent primary evidence | supports | Inspected history, research or prior assessment informs provenance only. Historical unavailability and broad negative claims are not adopted as current facts. No previous finding is closed or narrowed by this new individual observation. |
| EX1 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11413930/fullTextXML; PMC11413930.xml | context_only | PMID:39140156, DOI:10.1242/bio.060429. Octopus maya dissection methods describe juice collected between distal cecum and crop and separately sampled digestive glands. Bounded molluscan anatomy witness, not a replacement ontology identity. |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001153; UBERON_0001153.json | context_only | Current term identity, active status and definition: {"obo_id": "UBERON:0001153", "label": "caecum", "is_obsolete": false, "description": ["Taxon notes: in some herbivorous lizards, a cecum is present between small and large intestines[Kardong]", "A pouch in the digestive tract that connects the ileum with the ascending colon of the large intestine. It is separated from the ileum by the ileocecal valve, and is the beginning of the large intestine. It is also separated from the colon by the cecocolic junction."]} |
| ESEARCH | Local maintained inputs and review archive; rg --no-ignore --hidden -l -F -e habitatmech:GOLD.37d9cdc188 -e 'Cecum/Intestinal cecum' -e cecum_intestinal_cecum -e habitatmech:GOLD.37d9cdc188 curation history research reports data/raw build reviews | context_only | Identifier/label/slug search and full structured-YAML traversal; exact TSV rows were parsed separately. Broad search matches are leads, not all independently reviewed. |

## Limits And Additional Notes

- Source counts, ranks and scores do not establish prevalence, viability or characteristic presence. Original specimen-level evidence for every source member has not been reconstructed.
- Configured label validation skipped 2063 no-adapter pairs; displayed TaxIds were separately resolved against current NCBI including aliases.
- Exact-base full QC was verified remotely, not newly executed locally. New saved bundles require a separate archive check.
- iModulonDB is not applicable: target assertions contain no gene, regulator or expression-module claim. No paid research or native status promotion was performed.
- Captured input hashes match both working bytes and exact committed base blobs.
- This observation proposes curation but does not itself mutate inputs. The separately authorized PR workflow may address supported findings in later commits.
- Prior structured target observations: [{"path": "reviews/structured/20261015T224445Z-cecum-remediation/review.yaml", "review_id": "20261015T224445Z-cecum-remediation", "kind": "batch", "findings": [{"finding_id": "F1", "issue_key": "cecum-context-parent", "category": "grounding", "severity": "major", "status": "resolved", "certainty": "confirmed", "title": "Containing anatomy is emitted as a broader habitat class", "description": "Corrected through maintained inputs and native regeneration. Excluded only the exact GOLD containing-anatomy contribution habitatmech:GOLD.c336fb0bb7; independent valid genera and source paths remain.", "target_ids": ["BTO:0000166"], "field_paths": ["parent_habitats"], "evidence_ids": ["EX1", "EX2", "EX3", "EX4", "EX5", "EX6", "EX7", "EAFTER0", "EAFTER1", "EPREV", "ETEST", "EFIXTURE", "ERULE", "EHISTORY", "EI14", "EI15"], "owner_paths": [{"repository": "CultureBotAI/HabitatMech", "path": "curation/gold_parent_exclusions.tsv", "role": "Maintained input or generator; never patch generated habitat YAML"}], "rule_id": "docs/CURATION.md and native record-review checklist", "native_severity": "major", "normalization_reason": "Materially unsupported hierarchy, mapping or source-evidence semantics; correct deterministic reproduction does not establish scientific support.", "external_issues": ["https://github.com/CultureBotAI/HabitatMech/issues/2206"], "previous_occurrences": [{"repository": "CultureBotAI/HabitatMech", "review_id": "20261015T212554Z-cecum-record", "finding_id": "F1"}], "disposition_reason": "Excluded only the exact GOLD containing-anatomy contribution habitatmech:GOLD.c336fb0bb7; independent valid genera and source paths remain."}, {"finding_id": "F2", "issue_key": "cecum-molluscan-vertebrate-cecum-merge", "category": "identity", "severity": "blocker", "status": "resolved", "certainty": "confirmed", "title": "Molluscan cecum is merged into incompatible large-intestinal anatomy", "description": "Corrected through maintained inputs and native regeneration. Separated the molluscan GOLD source into habitatmech:GOLD.37d9cdc188. The original BTO:0000166 record now contains only its PREGO source, with the same 549-taxon pool and unchanged displayed taxa. No replacement ontology identity is invented.", "target_ids": ["BTO:0000166"], "field_paths": ["identifier", "definition", "synonyms", "source_attestations"], "evidence_ids": ["EX1", "EX2", "EX3", "EX4", "EX5", "EX6", "EX7", "EAFTER0", "EAFTER1", "EPREV", "ETEST", "EFIXTURE", "ERULE", "EHISTORY", "EI14", "EI15"], "owner_paths": [{"repository": "CultureBotAI/HabitatMech", "path": "curation/decisions.tsv", "role": "Maintained input or generator; never patch generated habitat YAML"}, {"repository": "CultureBotAI/HabitatMech", "path": "src/habitatmech/seed.py", "role": "Maintained input or generator; never patch generated habitat YAML"}], "rule_id": "docs/CURATION.md and native record-review checklist", "native_severity": "blocker", "normalization_reason": "Incompatible anatomical identities are treated as exact equivalents, causing a source concept to denote the wrong thing.", "external_issues": ["https://github.com/CultureBotAI/HabitatMech/issues/2208"], "previous_occurrences": [{"repository": "CultureBotAI/HabitatMech", "review_id": "20261015T212554Z-cecum-record", "finding_id": "F2"}], "disposition_reason": "Separated the molluscan GOLD source into habitatmech:GOLD.37d9cdc188. The original BTO:0000166 record now contains only its PREGO source, with the same 549-taxon pool and unchanged displayed taxa. No replacement ontology identity is invented."}, {"finding_id": "F3", "issue_key": "cecum-decision-note-truncated-path", "category": "provenance", "severity": "minor", "status": "resolved", "certainty": "confirmed", "title": "Maintained grounding note truncates the source name", "description": "Corrected through maintained inputs and native regeneration. The superseding ITEM decision carries the complete Cecum/Intestinal cecum path, current attribution and date. The old decision remains in Git and the regression fixture; immutable review/session files are not rewritten. Generated history is a current-input projection, not the append-only session archive.", "target_ids": ["BTO:0000166"], "field_paths": ["curation_history"], "evidence_ids": ["EX1", "EX2", "EX3", "EX4", "EX5", "EX6", "EX7", "EAFTER0", "EAFTER1", "EPREV", "ETEST", "EFIXTURE", "ERULE", "EHISTORY", "EI14", "EI15"], "owner_paths": [{"repository": "CultureBotAI/HabitatMech", "path": "curation/decisions.tsv", "role": "Maintained input or generator; never patch generated habitat YAML"}], "rule_id": "docs/CURATION.md and native record-review checklist", "native_severity": "minor", "normalization_reason": "Bounded maintained-provenance wording error; the full source path is retained elsewhere.", "external_issues": ["https://github.com/CultureBotAI/HabitatMech/issues/2208"], "previous_occurrences": [{"repository": "CultureBotAI/HabitatMech", "review_id": "20261015T212554Z-cecum-record", "finding_id": "F3"}], "disposition_reason": "The superseding ITEM decision carries the complete Cecum/Intestinal cecum path, current attribution and date. The old decision remains in Git and the regression fixture; immutable review/session files are not rewritten. Generated history is a current-input projection, not the append-only session archive."}]}]. Earlier multi-target dispositions retain their complete scope; this review neither supersedes nor closes them.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T235742Z-cecum_intestinal_cecum-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: Cecum/Intestinal cecum (habitatmech:GOLD.37d9cdc188)'
started_at: '2026-10-15T23:39:40Z'
finished_at: '2026-10-15T23:57:42Z'
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
summary: The molluscan Cecum/Intestinal cecum now remains minted and UNGROUNDED/REVIEWED,
  separated from vertebrate ileocecal anatomy and PREGO taxa. Primary Octopus maya
  dissection describes a cecum in different digestive context. This bounded witness
  is not exact identification of the GOLD specimen or a proposed replacement genus.
  The prior multi-target remediation remains unchanged.
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
  - path: data/habitats/host_associated/cecum_intestinal_cecum.yaml
    sha256: cbbd708e719fba4e5dc123f4ea0fe9860bad218bb3b338d74f909dd4c7a4dbec
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
  - path: history/mappings/cardiac_cartilage_cecum_review/2026-10-15T214400Z-codex-gpt-5-909775.yaml
    sha256: 98f4d839aa9a9361d5167448a3425842998d8b1d3de14f11af61df5ce0657b52
    role: context
  - path: history/mappings/cardiac_molluscan_citation_format/2026-10-15T221623Z-codex-gpt-5-cea5ff.yaml
    sha256: 66ff55b4feec04542c81ca5b3ba004d2966dd915c1331a0e1901478d2e25b967
    role: context
  - path: history/mappings/cardiac_stomach/2026-10-15T214401Z-codex-gpt-5-ac65b1.yaml
    sha256: ca808e9e8293f2a2794605c6bb0459ced388b0b8f5e21cab7f8a4c6450aad762
    role: context
  - path: history/mappings/cecum/2026-10-15T214403Z-codex-gpt-5-cf5c53.yaml
    sha256: 58234fcca34d0117048ee812c4319ed63453aa6add6d158ba89a41baefee9104
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reviews/structured/20261015T224445Z-cecum-remediation/review.yaml
    sha256: 52e089000e29ec17a0f0ec74b4ba6de28f352da34b81b8a79cf181ecd4ea9255
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
- target_id: habitatmech:GOLD.37d9cdc188
  path: data/habitats/host_associated/cecum_intestinal_cecum.yaml
  label: Cecum/Intestinal cecum
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
  - habitatmech:GOLD.37d9cdc188
  exclusions:
  - target: Other records, original source specimens and SSSOM/KGX products
    reason: Parent and source context do not add reviewed targets; exports and every
      original source specimen are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/cecum_intestinal_cecum.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.37d9cdc188
  summary: "Finished 2026-10-15T23:44:39Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/cecum_intestinal_cecum.yaml"
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
  - habitatmech:GOLD.37d9cdc188
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
  - habitatmech:GOLD.37d9cdc188
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
  - habitatmech:GOLD.37d9cdc188
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
  - habitatmech:GOLD.37d9cdc188
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
  - habitatmech:GOLD.37d9cdc188
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
  - habitatmech:GOLD.37d9cdc188
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
  - habitatmech:GOLD.37d9cdc188
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
  - habitatmech:GOLD.37d9cdc188
  summary: Verified 2026-10-15T23:55:08Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38822113212
  scope_note: Unchanged committed scientific-input baseline; new output bundles are
    outside this run.
- check_id: CREF
  name: Standalone evidence-reference validator applicability
  status: not_applicable
  required: false
  target_ids:
  - habitatmech:GOLD.37d9cdc188
  summary: No standalone citation/reference validator is documented for these evidence-free
    generated records. Target EvidenceItems and causal edges are absent. Stable source
    and ontology/taxon references were checked manually and with documented native
    gates; current-decision primary citations were separately verified where present.
  scope_note: No command or exit code is invented for an unavailable/nonapplicable
    checker. Full-corpus causal validation ran separately.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/cecum_intestinal_cecum.yaml
  locator: Entire target YAML
  accessed_at: '2026-10-15T23:57:42Z'
  support: supports
  summary: All fields, attestations, taxa and generated history read.
  snapshot_sha256: cbbd708e719fba4e5dc123f4ea0fe9860bad218bb3b338d74f909dd4c7a4dbec
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, strict broader hierarchy and evidence rules
  accessed_at: '2026-10-15T23:57:42Z'
  support: supports
  summary: Organism, disease, material and habitat identities remain distinct. Parents
    must be strictly broader, not merely containing sites.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: HabitatRecord, SourceAttestation and TaxonAssociation
  accessed_at: '2026-10-15T23:57:42Z'
  support: supports
  summary: Mapping predicate endpoint is source-to-record; source association is weaker
    than characteristic presence. Optional fields and native review status have distinct
    contracts.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native source routes and complete document reproduction
  accessed_at: '2026-10-15T23:57:42Z'
  support: supports
  summary: '[{"mint": "habitatmech:GOLD.37d9cdc188", "automatic": {"identifier": "habitatmech:GOLD.37d9cdc188",
    "grounding_status": "UNGROUNDED", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "gold_unmatched", "category":
    null, "reviewed": false, "decision": null}, "final": {"identifier": "habitatmech:GOLD.37d9cdc188",
    "grounding_status": "UNGROUNDED", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "curated_confirm_ungrounded_from_gold_unmatched",
    "category": null, "reviewed": true, "decision": {"identifier": "habitatmech:GOLD.37d9cdc188",
    "decision": "CONFIRM_UNGROUNDED", "object_id": "", "object_label": "", "grounding_status":
    "", "curator": "codex-gpt-5", "date": "2026-10-15", "notes": "ITEM reassessment
    https://github.com/CultureBotAI/HabitatMech/issues/2208 : This molluscan source
    does not denote the vertebrate ileocecal or large-intestinal anatomy of UBERON:0001153
    or BTO:0000166. Current OLS definitions and Uberon taxon notes distinguish invertebrate
    homonyms; octopus dissection (https://pubmed.ncbi.nlm.nih.gov/39140156/ ; DOI:10.1242/bio.060429)
    is a bounded anatomical witness, not identification of the exact GOLD specimen.
    Retain the source mint UNGROUNDED without inventing an alternative genus. Separate
    only this GOLD source from PREGO BTO:0000166; retain PREGO identity, 549-taxon
    pool and displayed associations unchanged. This supersedes the 2026-08-12 grounding
    and its truncated path; the prior decision is preserved in Git, immutable baseline
    review and the regression fixture. The whole-organ context contribution is excluded
    under #2206. Path: Host-associated > Mollusca > Digestive system > Hindgut > Cecum/Intestinal
    cecum", "review_depth": "ITEM", "category": "", "relation": "parent"}}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: Source counts, channels and taxon ranking
  accessed_at: '2026-10-15T23:57:42Z'
  support: supports
  summary: Exact frozen rows reproduce counts/units and ranked taxon scores. The committed
    projection does not retain original PREGO pair citation links.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Physical TSV rows 2479
  accessed_at: '2026-10-15T23:57:42Z'
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
  reference: curation/gold_parent_exclusions.tsv
  locator: Physical TSV rows 15
  accessed_at: '2026-10-15T23:57:42Z'
  support: supports
  summary: '[{"row": 15, "data": {"identifier": "habitatmech:GOLD.37d9cdc188", "source_path":
    "Host-associated > Mollusca > Digestive system > Hindgut > Cecum/Intestinal cecum",
    "parent_id": "habitatmech:GOLD.c336fb0bb7", "curator": "codex-gpt-5", "date":
    "2026-10-15", "notes": "Review https://github.com/CultureBotAI/HabitatMech/issues/2206
    : This anatomical component or derived material is not a subtype of the containing
    organ or system. Exclude only the exact GOLD contribution; retain independent
    valid genera and original source observations. This does not resolve the separate
    catarrh condition/material scope or shared mapping endpoint #1398."}}]'
  snapshot_sha256: 7158cb696b7e2ac84a8d594a03015711424ff56e21c07a4648ffc6fb2e84a107
- evidence_id: ET7
  kind: database
  reference: curation/decisions.tsv
  locator: Physical TSV rows 413
  accessed_at: '2026-10-15T23:57:42Z'
  support: supports
  summary: '[{"row": 413, "data": {"identifier": "habitatmech:GOLD.37d9cdc188", "decision":
    "CONFIRM_UNGROUNDED", "object_id": "", "object_label": "", "grounding_status":
    "", "curator": "codex-gpt-5", "date": "2026-10-15", "notes": "ITEM reassessment
    https://github.com/CultureBotAI/HabitatMech/issues/2208 : This molluscan source
    does not denote the vertebrate ileocecal or large-intestinal anatomy of UBERON:0001153
    or BTO:0000166. Current OLS definitions and Uberon taxon notes distinguish invertebrate
    homonyms; octopus dissection (https://pubmed.ncbi.nlm.nih.gov/39140156/ ; DOI:10.1242/bio.060429)
    is a bounded anatomical witness, not identification of the exact GOLD specimen.
    Retain the source mint UNGROUNDED without inventing an alternative genus. Separate
    only this GOLD source from PREGO BTO:0000166; retain PREGO identity, 549-taxon
    pool and displayed associations unchanged. This supersedes the 2026-08-12 grounding
    and its truncated path; the prior decision is preserved in Git, immutable baseline
    review and the regression fixture. The whole-organ context contribution is excluded
    under #2206. Path: Host-associated > Mollusca > Digestive system > Hindgut > Cecum/Intestinal
    cecum", "review_depth": "ITEM", "category": "", "relation": "parent"}}]'
  snapshot_sha256: e5cb2e09f72dd4b18e069c0e2576e25e13e56c9991f4eb5ae47416345e247578
- evidence_id: EH8
  kind: record_content
  reference: history/mappings/cardiac_cartilage_cecum_review/2026-10-15T214400Z-codex-gpt-5-909775.yaml
  locator: Historical context; not independent primary evidence
  accessed_at: '2026-10-15T23:57:42Z'
  support: supports
  summary: Inspected history, research or prior assessment informs provenance only.
    Historical unavailability and broad negative claims are not adopted as current
    facts. No previous finding is closed or narrowed by this new individual observation.
  snapshot_sha256: 98f4d839aa9a9361d5167448a3425842998d8b1d3de14f11af61df5ce0657b52
- evidence_id: EH9
  kind: record_content
  reference: history/mappings/cardiac_molluscan_citation_format/2026-10-15T221623Z-codex-gpt-5-cea5ff.yaml
  locator: Historical context; not independent primary evidence
  accessed_at: '2026-10-15T23:57:42Z'
  support: supports
  summary: Inspected history, research or prior assessment informs provenance only.
    Historical unavailability and broad negative claims are not adopted as current
    facts. No previous finding is closed or narrowed by this new individual observation.
  snapshot_sha256: 66ff55b4feec04542c81ca5b3ba004d2966dd915c1331a0e1901478d2e25b967
- evidence_id: EH10
  kind: record_content
  reference: history/mappings/cardiac_stomach/2026-10-15T214401Z-codex-gpt-5-ac65b1.yaml
  locator: Historical context; not independent primary evidence
  accessed_at: '2026-10-15T23:57:42Z'
  support: supports
  summary: Inspected history, research or prior assessment informs provenance only.
    Historical unavailability and broad negative claims are not adopted as current
    facts. No previous finding is closed or narrowed by this new individual observation.
  snapshot_sha256: ca808e9e8293f2a2794605c6bb0459ced388b0b8f5e21cab7f8a4c6450aad762
- evidence_id: EH11
  kind: record_content
  reference: history/mappings/cecum/2026-10-15T214403Z-codex-gpt-5-cf5c53.yaml
  locator: Historical context; not independent primary evidence
  accessed_at: '2026-10-15T23:57:42Z'
  support: supports
  summary: Inspected history, research or prior assessment informs provenance only.
    Historical unavailability and broad negative claims are not adopted as current
    facts. No previous finding is closed or narrowed by this new individual observation.
  snapshot_sha256: 58234fcca34d0117048ee812c4319ed63453aa6add6d158ba89a41baefee9104
- evidence_id: EH12
  kind: record_content
  reference: reviews/structured/20261015T224445Z-cecum-remediation/review.yaml
  locator: Historical context; not independent primary evidence
  accessed_at: '2026-10-15T23:57:42Z'
  support: supports
  summary: Inspected history, research or prior assessment informs provenance only.
    Historical unavailability and broad negative claims are not adopted as current
    facts. No previous finding is closed or narrowed by this new individual observation.
  snapshot_sha256: 52e089000e29ec17a0f0ec74b4ba6de28f352da34b81b8a79cf181ecd4ea9255
- evidence_id: EX1
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11413930/fullTextXML
  locator: PMC11413930.xml
  accessed_at: '2026-10-15T23:50:00Z'
  support: context_only
  summary: PMID:39140156, DOI:10.1242/bio.060429. Octopus maya dissection methods
    describe juice collected between distal cecum and crop and separately sampled
    digestive glands. Bounded molluscan anatomy witness, not a replacement ontology
    identity.
  snapshot_sha256: 704feed586f3c8185b5884f39407ecd5c8c3ec73e8c736f79b673bb7f5268be5
- evidence_id: EX2
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001153
  locator: UBERON_0001153.json
  accessed_at: '2026-10-15T23:50:03Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "UBERON:0001153",
    "label": "caecum", "is_obsolete": false, "description": ["Taxon notes: in some
    herbivorous lizards, a cecum is present between small and large intestines[Kardong]",
    "A pouch in the digestive tract that connects the ileum with the ascending colon
    of the large intestine. It is separated from the ileum by the ileocecal valve,
    and is the beginning of the large intestine. It is also separated from the colon
    by the cecocolic junction."]}'
  snapshot_sha256: 707179115a5ffd698135f53ab3a4246ab0127d4c073b8bf16d89ff71ccc53107
- evidence_id: ESEARCH
  kind: search
  reference: Local maintained inputs and review archive
  locator: rg --no-ignore --hidden -l -F -e habitatmech:GOLD.37d9cdc188 -e 'Cecum/Intestinal
    cecum' -e cecum_intestinal_cecum -e habitatmech:GOLD.37d9cdc188 curation history
    research reports data/raw build reviews
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
  summary: The molluscan Cecum/Intestinal cecum now remains minted and UNGROUNDED/REVIEWED,
    separated from vertebrate ileocecal anatomy and PREGO taxa. Primary Octopus maya
    dissection describes a cecum in different digestive context. This bounded witness
    is not exact identification of the GOLD specimen or a proposed replacement genus.
    The prior multi-target remediation remains unchanged.
  target_ids:
  - habitatmech:GOLD.37d9cdc188
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - EX1
  - EX2
- assessment_id: A2
  area: quantity
  topic: Source assertions, pools, ranks and supplementary context
  outcome: supported
  summary: 'All emitted counts/units, labels, ranks, scores and candidate pools match
    exact frozen rows. [{"source": "GOLD", "count": 0, "unit": "ORGANISM"}]. Zero
    tree counts are omitted; later biosamples and study memberships are not added.
    Current taxonomy resolves displayed identifiers including explicit aliases.'
  target_ids:
  - habitatmech:GOLD.37d9cdc188
  evidence_ids:
  - E1
  - EEXTRACT
  - ESEED
  - EX1
  - EX2
- assessment_id: A3
  area: evidence
  topic: Biological support and bounded source uncertainty
  outcome: supported
  summary: The molluscan Cecum/Intestinal cecum now remains minted and UNGROUNDED/REVIEWED,
    separated from vertebrate ileocecal anatomy and PREGO taxa. Primary Octopus maya
    dissection describes a cecum in different digestive context. This bounded witness
    is not exact identification of the GOLD specimen or a proposed replacement genus.
    The prior multi-target remediation remains unchanged.
  target_ids:
  - habitatmech:GOLD.37d9cdc188
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - EX1
  - EX2
- assessment_id: A4
  area: completeness
  topic: Native status, optional parameters and causal mechanisms
  outcome: supported
  summary: Executed native resolution reproduces UNGROUNDED/REVIEWED. No environmental
    parameters, causal graphs, discussions, datasets or is_characteristic=true claims
    are present. Missing optional fields and SEEDED status alone are not defects;
    parent mechanisms are not inherited.
  target_ids:
  - habitatmech:GOLD.37d9cdc188
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
  - habitatmech:GOLD.37d9cdc188
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
- 'Prior structured target observations: [{"path": "reviews/structured/20261015T224445Z-cecum-remediation/review.yaml",
  "review_id": "20261015T224445Z-cecum-remediation", "kind": "batch", "findings":
  [{"finding_id": "F1", "issue_key": "cecum-context-parent", "category": "grounding",
  "severity": "major", "status": "resolved", "certainty": "confirmed", "title": "Containing
  anatomy is emitted as a broader habitat class", "description": "Corrected through
  maintained inputs and native regeneration. Excluded only the exact GOLD containing-anatomy
  contribution habitatmech:GOLD.c336fb0bb7; independent valid genera and source paths
  remain.", "target_ids": ["BTO:0000166"], "field_paths": ["parent_habitats"], "evidence_ids":
  ["EX1", "EX2", "EX3", "EX4", "EX5", "EX6", "EX7", "EAFTER0", "EAFTER1", "EPREV",
  "ETEST", "EFIXTURE", "ERULE", "EHISTORY", "EI14", "EI15"], "owner_paths": [{"repository":
  "CultureBotAI/HabitatMech", "path": "curation/gold_parent_exclusions.tsv", "role":
  "Maintained input or generator; never patch generated habitat YAML"}], "rule_id":
  "docs/CURATION.md and native record-review checklist", "native_severity": "major",
  "normalization_reason": "Materially unsupported hierarchy, mapping or source-evidence
  semantics; correct deterministic reproduction does not establish scientific support.",
  "external_issues": ["https://github.com/CultureBotAI/HabitatMech/issues/2206"],
  "previous_occurrences": [{"repository": "CultureBotAI/HabitatMech", "review_id":
  "20261015T212554Z-cecum-record", "finding_id": "F1"}], "disposition_reason": "Excluded
  only the exact GOLD containing-anatomy contribution habitatmech:GOLD.c336fb0bb7;
  independent valid genera and source paths remain."}, {"finding_id": "F2", "issue_key":
  "cecum-molluscan-vertebrate-cecum-merge", "category": "identity", "severity": "blocker",
  "status": "resolved", "certainty": "confirmed", "title": "Molluscan cecum is merged
  into incompatible large-intestinal anatomy", "description": "Corrected through maintained
  inputs and native regeneration. Separated the molluscan GOLD source into habitatmech:GOLD.37d9cdc188.
  The original BTO:0000166 record now contains only its PREGO source, with the same
  549-taxon pool and unchanged displayed taxa. No replacement ontology identity is
  invented.", "target_ids": ["BTO:0000166"], "field_paths": ["identifier", "definition",
  "synonyms", "source_attestations"], "evidence_ids": ["EX1", "EX2", "EX3", "EX4",
  "EX5", "EX6", "EX7", "EAFTER0", "EAFTER1", "EPREV", "ETEST", "EFIXTURE", "ERULE",
  "EHISTORY", "EI14", "EI15"], "owner_paths": [{"repository": "CultureBotAI/HabitatMech",
  "path": "curation/decisions.tsv", "role": "Maintained input or generator; never
  patch generated habitat YAML"}, {"repository": "CultureBotAI/HabitatMech", "path":
  "src/habitatmech/seed.py", "role": "Maintained input or generator; never patch generated
  habitat YAML"}], "rule_id": "docs/CURATION.md and native record-review checklist",
  "native_severity": "blocker", "normalization_reason": "Incompatible anatomical identities
  are treated as exact equivalents, causing a source concept to denote the wrong thing.",
  "external_issues": ["https://github.com/CultureBotAI/HabitatMech/issues/2208"],
  "previous_occurrences": [{"repository": "CultureBotAI/HabitatMech", "review_id":
  "20261015T212554Z-cecum-record", "finding_id": "F2"}], "disposition_reason": "Separated
  the molluscan GOLD source into habitatmech:GOLD.37d9cdc188. The original BTO:0000166
  record now contains only its PREGO source, with the same 549-taxon pool and unchanged
  displayed taxa. No replacement ontology identity is invented."}, {"finding_id":
  "F3", "issue_key": "cecum-decision-note-truncated-path", "category": "provenance",
  "severity": "minor", "status": "resolved", "certainty": "confirmed", "title": "Maintained
  grounding note truncates the source name", "description": "Corrected through maintained
  inputs and native regeneration. The superseding ITEM decision carries the complete
  Cecum/Intestinal cecum path, current attribution and date. The old decision remains
  in Git and the regression fixture; immutable review/session files are not rewritten.
  Generated history is a current-input projection, not the append-only session archive.",
  "target_ids": ["BTO:0000166"], "field_paths": ["curation_history"], "evidence_ids":
  ["EX1", "EX2", "EX3", "EX4", "EX5", "EX6", "EX7", "EAFTER0", "EAFTER1", "EPREV",
  "ETEST", "EFIXTURE", "ERULE", "EHISTORY", "EI14", "EI15"], "owner_paths": [{"repository":
  "CultureBotAI/HabitatMech", "path": "curation/decisions.tsv", "role": "Maintained
  input or generator; never patch generated habitat YAML"}], "rule_id": "docs/CURATION.md
  and native record-review checklist", "native_severity": "minor", "normalization_reason":
  "Bounded maintained-provenance wording error; the full source path is retained elsewhere.",
  "external_issues": ["https://github.com/CultureBotAI/HabitatMech/issues/2208"],
  "previous_occurrences": [{"repository": "CultureBotAI/HabitatMech", "review_id":
  "20261015T212554Z-cecum-record", "finding_id": "F3"}], "disposition_reason": "The
  superseding ITEM decision carries the complete Cecum/Intestinal cecum path, current
  attribution and date. The old decision remains in Git and the regression fixture;
  immutable review/session files are not rewritten. Generated history is a current-input
  projection, not the append-only session archive."}]}]. Earlier multi-target dispositions
  retain their complete scope; this review neither supersedes nor closes them.'
tags:
- individual-scientific-review
- host-associated
```
