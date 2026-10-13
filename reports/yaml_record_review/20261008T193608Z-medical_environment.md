# YAML Record Review: Medical-environment

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/clinical/medical_environment.yaml`
- Started UTC: 2026-10-08T19:32:42Z
- Finished UTC: 2026-10-08T19:36:08Z
- Verdict: pass (0 blocker, 0 major, 0 minor)

## Target

Read the complete generated HabitatRecord `habitatmech:BACDIVE.5e52ea1bba`,
Medical-environment, CLINICAL / UNGROUNDED / REVIEWED. One BacDive attestation,
25 associated-taxon entries and two generated events; no definition, parent,
xref, synonym, parameter or causal graph. Baseline:
`c6c94db6f5fe79e1b9d55a98d9cd2a3bfb2b5602`.
This reviews the newly separated source record, not the earlier merged Hospital
record. The complete prior Hospital report and both relevant session receipts
were read as context, without treating them as primary scientific evidence.

## Validation

- `UV_CACHE_DIR=build/uv-cache just validate data/habitats/clinical/medical_environment.yaml`:
  passed, no issues.
- `UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/clinical/medical_environment.yaml`:
  passed, one file, zero errors.
- `UV_CACHE_DIR=build/uv-cache just validate-history history/mappings/medical_environment`:
  passed, both receipts valid.
- `UV_CACHE_DIR=build/uv-cache uv run pytest -q tests/test_hay_hospital_curation.py::test_medical_environment_split_preserves_source_evidence`:
  one test passed. Its full-corpus comparison checks source separation and
  preservation of unrelated records, not original strain membership.
- Fresh full-index construction exactly reproduces the complete parsed target:
  one contributor, one ITEM-reviewed contributor, no parent, authored definition
  or exclusion. Default and applied BacDive routes were evaluated directly.
- Full QC is reused from the immediately preceding publication preparation,
  not rerun in this read-only review. Fresh diff against the stated baseline is
  empty for guidance, code, inputs, generated corpus and tests. The inspected
  `build/pr1743-qc.log` records 597 passes, three skips, 201 valid histories,
  3,208 strict-valid/reproduced records and all local gates passed.
  [Publication receipt](https://github.com/CultureBotAI/HabitatMech/pull/1743#issuecomment-6067512009).
  PR #1743 remained OPEN with required CI pending when polled; local success
  is not misrepresented as a merged or CI-approved publication.
- Direct taxon and ontology checks below supplement the prior OAK gate and its
  no-adapter skips. Original source joins and SSSOM/KGX compatibility were not
  verified. No record graph or literature-reference collection needs a separate
  focused validator.

## Identity and Grounding

`PATHS.tsv:1203` agrees with the mint and slug. Hashing
`bacdive.isolation_source:medical-environment` produces the retained source ID.
The automatic `bacdive_declined_upstream` route honors the empty ontology target
in mapping row 196. The ITEM CONFIRM_UNGROUNDED decision at
`curation/decisions.tsv:39` produces
`curated_confirm_ungrounded_from_bacdive_declined_upstream`, CLINICAL, without
a mapping predicate, parent or xref. The table's explicit `parent` relation is
the default placement mode; with an empty object it contributes no edge.

The source describes clinical isolation context, not the hospital building
identity or a claim that every isolate came from the same facility/material.
The inspected source example includes patient-derived material. The broader
clinical tag must not become an exact hospital synonym or import its observations
into the narrower hospital identity. The current mint avoids that conflation.

The three named ENVO candidates are real and correctly labeled: hospital
`ENVO:00002173` and healthcare facility `ENVO:03501134` denote constructions;
healthcare environment `ENVO:03501331` explicitly requires a facility-bounded
environment. The source tag alone does not establish those identity conditions.
No exact replacement or strictly broader candidate has been demonstrated here.
REVIEWED reflects the maintained item-level identity assessment, not proof of
every historical strain association or a complete source-equivalent definition.

## Evidence

- `bacdive_isolation_sources.tsv:34` supplies the label, source ID, 438 STRAIN
  assertions and 269-taxon candidate pool. `bacdive_source_taxa.tsv:1798-1822`
  supplies every displayed ID, label, rank and association count. The 25 entries
  are a ranked subset, not all 269 taxa, 438 named strains or a prevalence study.
  No `is_characteristic`, mechanism or independent corroboration is asserted.
- `isolation_source_groundings.tsv:196` contains an explicitly empty target,
  manual-review provenance and source date 2026-05-02. The record's ungrounded
  note now agrees with both the default and applied result.
- `data/raw/MANIFEST.yaml` identifies the 2026-08-16 extraction from
  kg-microbe `7698351a54b48f2e917635fdf51cd0a6b323135d`, with mappings separately
  pinned at `bfd350e`. Reproduction validates those inventories, not a fresh
  recount of the original transformed BacDive node/edge files.
- Fresh [BacDive 153714](https://bacdive.dsmz.de/strain/153714), isolation section,
  places a human lavage isolate under Medical environment / Medical practice
  alongside patient and body-site categories. This supports clinical context,
  not membership in the frozen 438-strain extraction, a specific building
  location or the entire source category's extent. Its growth and biochemical
  results are not transferred into habitat conditions or mechanisms.
- Fresh [NCBI Taxonomy batch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=562,287,47715,1280,1313,446,47885,1352,573,144185,43767,529,756689,759851,210,37637,60552,817,85698,13689,1443941,1496,151416,151454,37329&retmode=xml)
  resolves all 25 IDs at species rank. Twenty-four labels are current scientific
  names; Prescottella equi is a recognized alternative for Rhodococcus (subgen.
  Prescottella) equi, ID 43767, not an invalid identifier. Response: 158,851 bytes,
  SHA256 `b1b8823de5a62116b339c4b1641a28c9da1665134a10e79410ab11563bc1c4f9`.
  Name validation is not validation of the isolation-source association.
- Fresh [pinned ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
  confirms all three candidate labels and scope conditions above. Response:
  9,614,229 bytes, SHA256
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
  This is a pinned identity check, not a claim to refresh every ontology.

## Completeness

Ignored-inclusive identifier, label, source-ID and slug searches covered raw
inventories, curation, configuration, docs, tests, PATHS/RETIRED, histories,
research and individual reports. They found the decision, regression, two
session receipts and earlier Hospital report. No target-owned authored
definition, overlay, exclusion, research report or prior individual review of
this new file was found within those bounds. The Contamination research file
only mentions a category placement and is not independent target evidence.

A completed CSV exact-field/pipe-member traversal of every raw TSV found only
the source aggregate, 25 source-taxon rows and mapping row for the target keys.
An initial DictReader probe stopped on a list-valued surplus field elsewhere;
the repeated CSV-row traversal completed before drawing the bounded absence
conclusion. No direct target environmental-parameter or additional-source row
was found. Ignored-inclusive find under build, data/raw and the configured
kg-microbe data directory found no files under a BacDive source directory.
The original source-to-strain-to-taxon joins remain unavailable in those bounds.

Optional definition, conditions, graphs, discussions and datasets should not be
invented. iModulonDB is not applicable: occurrence at species level is not a
named gene, regulator, strain-expression or transcriptomic claim.

## Findings

None found: zero blockers, zero major findings, zero minor findings.
The pass is bounded to the corrected source identity and faithful retained
inventory provenance, not recovered original members or exact ENVO equivalence.
The prior Hospital report remains a valid historical baseline finding.

## Recommended Edits

No immediate correction is established. Preserve the mint, clinical category,
counts, associations and absence of unsupported facility relations. Any future
exact grounding belongs in `curation/decisions.tsv` after source-level equivalence
is shown; a supported novel definition belongs in `curation/term_requests.tsv`.
Original-join recovery and a reviewed definition are follow-up research, not a
reason to re-merge the source or invent a broader parent.

## Follow-up Checks

Recover the manifest-bound BacDive source files before a cohort-level claim.
Any curation should retain the complete inventory-backed associations and unit,
recheck all contributors, inspect both source and hospital canaries, and run
schema/history/label checks, exact reproduction, map/site freshness, redirects
and full QC. Verify source membership separately from taxonomic identity.

## Additional Notes

Only this new review report was written. Scientific/generated inputs, statuses,
old reports and session histories remain unchanged. The second existing session
receipt explicitly corrects the first receipt's inherited actor-name default;
the correction was read, not silently rewritten or counted as a new defect.
Fresh issue-status reads encountered a transient GitHub connection failure;
no issue-closure claim follows. The pending PR was not changed by this review.
