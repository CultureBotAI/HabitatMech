# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/breast_cancer_ductal.yaml`
- Started UTC: 2026-09-22T11:15:50Z
- Finished UTC: 2026-09-22T11:15:50Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.1064d1667e` |
| Label | `Breast cancer: Ductal` |
| Class | `HabitatRecord` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Maintained owner | Generated from `data/raw/gold_ecosystem_paths.tsv` plus the class-level `curation/decisions.tsv` row |
| Locked slug | `data/habitats/PATHS.tsv:1399` maps `habitatmech:GOLD.1064d1667e` to `breast_cancer_ductal` |

This is the GOLD path record for `Host-associated > Mammals: Human > Malignant tumor > Carcinoma > Breast cancer: Ductal`. The generated YAML faithfully retains it as an ungrounded, minted HabitatMech source concept because the maintained decision is still only a class-level sweep row. The leaf now needs item-level curation: the path names a ductal breast-cancer disease bucket under the already reviewed non-habitat `Carcinoma` GOLD parent, so leaving the source concept class-swept is materially weaker than the evidence in the path itself.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/breast_cancer_ductal.yaml` | Pass; `linkml-validate` reported `No issues found` |
| `just validate-strict data/habitats/host_associated/breast_cancer_ductal.yaml` | Pass; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate-causal-all` | Pass; 32 causal-graph curation files with 32 graphs validated |
| `just term-requests-check` | Pass; term-request table is current with 109 terms |
| `just validate-history` | Pass; 77 history records are valid against `src/habitatmech/schema/history.yaml` |
| `just verify-corpus --max-diffs 1` | Pass; expected 3206 records, found 3206, with 0 missing, 0 extra, 0 differing |
| `git diff --check` | Pass; no whitespace or patch errors after this report was written |

## Identity and Grounding

The generated identifier, label, host-associated category, GOLD path parent, path lock, zero-assertion source attestation, and class-level grounding decision are supported by maintained inputs:

- `data/raw/gold_ecosystem_paths.tsv:2328` is the raw GOLD row for this record. Its canonical path is `Host-associated > Mammals: Human > Malignant tumor > Carcinoma > Breast cancer: Ductal`; its leaf label is `Breast cancer: Ductal`; it is a depth-5 path with one GOLD node id, `gold.ecosystem:6174`, and zero organism, study, biosample, and total assertions.
- `curation/decisions.tsv:187` addresses the same minted source concept, `habitatmech:GOLD.1064d1667e`, and records a `CLASS`-depth `CONFIRM_UNGROUNDED` decision by `claude-opus-5` on 2026-08-12.
- `data/habitats/PATHS.tsv:1399` pins `habitatmech:GOLD.1064d1667e` to slug `breast_cancer_ductal`, matching the reviewed YAML path.
- The parent path `Host-associated > Mammals: Human > Malignant tumor > Carcinoma` mints to `habitatmech:GOLD.9bb307824f`; `data/habitats/PATHS.tsv:2445` pins that parent to `carcinoma`.
- `data/raw/gold_ecosystem_paths.tsv:2323` is the parent Carcinoma path that feeds `habitatmech:GOLD.9bb307824f` and carries GOLD node ids `gold.ecosystem:6172|gold.ecosystem:6173`.
- `curation/decisions.tsv:901` independently reviews the immediate GOLD `Carcinoma` parent as `NOT_APPLICABLE`, with an item-level note that the source concept names a disease, intervention, sampling artifact, or no-value filler rather than a place.

`mapping_status: SEEDED` is mechanically correct because the only maintained target decision has `review_depth: CLASS`; by design, class-level rows do not promote generated records to `REVIEWED`. `grounding_status: UNGROUNDED` is also faithful to the current `CONFIRM_UNGROUNDED` decision: that sweep established that no vendored ontology term matched the label by the documented lexical routes, not that this disease-labeled GOLD leaf had been item-reviewed as a term-request candidate. That is also the unresolved curation gap for this record: the target should be pulled out of the class-level sweep and decided individually.

## Evidence

Every generated claim in this record is source-derived or maintained:

| Claim | Nearest source | Review |
|---|---|---|
| Minted record identifier `habitatmech:GOLD.1064d1667e` | `src/habitatmech/seed.py`, `data/raw/gold_ecosystem_paths.tsv:2328` | Supported exactly by `mint("GOLD", canonical_path)` |
| Label `Breast cancer: Ductal`, host-associated category, GOLD source id, and source path | `data/raw/gold_ecosystem_paths.tsv:2328` | Supported exactly |
| Omitted `assertion_count` and `assertion_unit` | `data/raw/gold_ecosystem_paths.tsv:2328`, `src/habitatmech/seed.py` | Supported; GOLD attestation counts are emitted from nonzero `organism_count`, and this exact path has `organism_count=0` |
| `UNGROUNDED` status and the first curation-history event | `curation/decisions.tsv:187` | Supported exactly |
| `SEEDED` mapping status | `curation/decisions.tsv:187`, `docs/HARMONIZATION.md` | Supported; the decision is class-depth, not item-depth |
| Parent `habitatmech:GOLD.9bb307824f` | GOLD parent-path emission in `src/habitatmech/seed.py`, backed by `data/raw/gold_ecosystem_paths.tsv:2323` | Supported exactly |
| Locked filename | `data/habitats/PATHS.tsv:1399` | Supported exactly |

The record has no xrefs, definition, synonyms, environmental parameters, characteristic taxa, record-level evidence, causal graphs, discussion links, assertion count, assertion unit, or datasets. Those absences are consistent with the class-level decision and zero-organism raw GOLD row. Exact side-table lookups found `data/raw/gold_path_biosamples.tsv:639`, which records 10 biosamples for ecosystem path `6174`, and `data/raw/gold_studies.tsv:3099`, a multi-path study set that includes the exact target path; they found no exact target row in `data/raw/gold_path_triads.tsv`.

## Completeness

The generated slots are faithful to the maintained inputs that feed this record, but one maintained input is consequentially underfilled:

- The sole `source_attestations` entry captures the complete target GOLD path and exact upstream node id.
- No `assertion_count` is emitted because `data/raw/gold_ecosystem_paths.tsv:2328` records 0 organism assertions for the canonical GOLD path; supplemental biosample and study rows do not currently materialize into generated record fields.
- The parent list preserves the immediate GOLD path parent, `Carcinoma`, so this sparse leaf remains browsable in its source hierarchy.
- `mapping_status` stays `SEEDED` because the class-level row is a reproducible lexical miss, not an item-level habitat judgement; this is correct generated output, but not complete curation for a disease-labeled GOLD leaf whose parent is already item-reviewed as non-habitat.
- The unsuffixed `Breast cancer` and `Breast cancer: Lobular` GOLD rows at `data/raw/gold_ecosystem_paths.tsv:2327` and `:2329` are sibling targets with their own locked slugs and do not feed this Ductal record.

Ignored/hidden-inclusive exact searches covered `curation`, `history`, `research`, `reports`, `data/raw`, `data/habitats/PATHS.tsv`, and the generated target, excluding generated `build`, `data/text_map`, and `pages` trees. They found the maintained target decision, raw GOLD row, biosample side-table row, study side-table row, path lock, generated YAML, Carcinoma parent record, adjacent Breast cancer siblings, and the existing review report for the unsuffixed Breast cancer sibling; they found no target-specific term request, causal overlay, history record, research report, GOLD triad row, or prior exact YAML review report.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | `Breast cancer: Ductal` remains under a `CLASS`-depth `CONFIRM_UNGROUNDED` row even though the GOLD path is a disease branch, `Host-associated > Mammals: Human > Malignant tumor > Carcinoma > Breast cancer: Ductal`, and its immediate `Carcinoma` parent has already been item-reviewed as `NOT_APPLICABLE`. The generated `UNGROUNDED` / `SEEDED` state is faithful to the table, but it leaves an obvious disease-labeled source concept in the lexical-miss bucket instead of deciding whether it is a non-habitat diagnosis bucket. | Replace `curation/decisions.tsv:187` for `habitatmech:GOLD.1064d1667e` with an `ITEM`-depth row, most likely `NOT_APPLICABLE` for the same disease-category reason used on `Carcinoma`. |

## Recommended Edits

- Replace the `CLASS`-depth `curation/decisions.tsv` row for `habitatmech:GOLD.1064d1667e` with an item-level curation row. The expected disposition is `NOT_APPLICABLE` if the curator confirms the GOLD leaf denotes the ductal breast-cancer diagnosis bucket rather than a sampled tumor microenvironment.
- Regenerate from maintained inputs with `just seed` and preview `data/habitats/host_associated/breast_cancer_ductal.yaml` with `just seed-canary habitatmech:GOLD.1064d1667e` before applying the full generated corpus.

## Follow-up Checks

After replacing the class-level Ductal Breast cancer decision, re-run the same focused validation set and confirm the regenerated YAML is `mapping_status: REVIEWED` with a first curation-history event that points at an `ITEM`-depth `curation/decisions.tsv` row:

- `just validate data/habitats/host_associated/breast_cancer_ductal.yaml`
- `just validate-strict data/habitats/host_associated/breast_cancer_ductal.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `git diff --check`

Also verify the GOLD attestation and Carcinoma parent stay attached to the surviving record or its replacement.

## Additional Notes

- `find reports/yaml_record_review -name '*breast_cancer_ductal*' -print` found no pre-existing exact review report for this record before this file was written.
- Exact ignored/hidden-inclusive content searches for `Breast cancer: Ductal`, `breast_cancer_ductal`, `gold.ecosystem:6174`, and `habitatmech:GOLD.1064d1667e` found the maintained source and decision rows cited above. The same broader GOLD Carcinoma search found disease sibling paths; those rows share the same source parent but do not feed this target.
