# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/breast_abscess.yaml`
- Started UTC: 2026-09-22T10:36:41Z
- Finished UTC: 2026-09-22T10:36:41Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.0e7950bba4` |
| Label | `Breast abscess` |
| Class | `HabitatRecord` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `NOT_APPLICABLE` |
| Mapping status | `REVIEWED` |
| Maintained owner | Generated from `data/raw/gold_ecosystem_paths.tsv` plus the item-level `curation/decisions.tsv` row |
| Locked slug | `data/habitats/PATHS.tsv:1384` maps `habitatmech:GOLD.0e7950bba4` to `breast_abscess` |

This is the GOLD path record for `Host-associated > Mammals: Human > Integumentary system > Mammary gland > Breast abscess`. It is correctly retained as a minted HabitatMech source concept and marked `NOT_APPLICABLE`: the GOLD leaf is a pathological abscess context rather than a microbial habitat identity that should be grounded to an ontology class.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/breast_abscess.yaml` | Pass; `linkml-validate` reported `No issues found` |
| `just validate-strict data/habitats/host_associated/breast_abscess.yaml` | Pass; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate-causal-all` | Pass; 32 causal-graph curation files with 32 graphs validated |
| `just term-requests-check` | Pass; term-request table is current with 109 terms |
| `just validate-history` | Pass; 77 history records are valid against `src/habitatmech/schema/history.yaml` |
| `just verify-corpus --max-diffs 1` | Pass; expected 3206 records, found 3206, with 0 missing, 0 extra, 0 differing |
| `git diff --check` | Pass; no whitespace or patch errors after this report was written |

## Identity and Grounding

The generated identifier, label, `NOT_APPLICABLE` decision, GOLD path parent, path lock, and source attestation are supported by maintained inputs:

- `data/raw/gold_ecosystem_paths.tsv:555` is the raw GOLD row for this record. Its canonical path is `Host-associated > Mammals: Human > Integumentary system > Mammary gland > Breast abscess`; its leaf label is `Breast abscess`; it is a depth-5 path with one GOLD node id, `gold.ecosystem:6322`, 9 organism assertions, and no study or biosample assertions.
- `curation/decisions.tsv:178` addresses the same minted source concept, `habitatmech:GOLD.0e7950bba4`, and records an item-level `NOT_APPLICABLE` decision by `claude-opus-5` on 2026-08-12.
- `data/habitats/PATHS.tsv:1384` pins `habitatmech:GOLD.0e7950bba4` to slug `breast_abscess`, matching the reviewed YAML path.
- The parent path `Host-associated > Mammals: Human > Integumentary system > Mammary gland` mints to `habitatmech:GOLD.89cf14e129`; `data/habitats/PATHS.tsv:2315` pins that parent to `mammary_gland__cf1c47fb`.
- `data/raw/gold_ecosystem_paths.tsv:684` is the parent Mammary gland path that feeds `habitatmech:GOLD.89cf14e129` and carries GOLD node ids `gold.ecosystem:6119|gold.ecosystem:6505`.

`mapping_status: REVIEWED` is correct because the only source concept that feeds this record has an `ITEM`-depth maintained decision. `grounding_status: NOT_APPLICABLE` is correct because the decision explicitly rules the GOLD Breast abscess leaf out as a habitat identity rather than merely failing to find an ontology match.

## Evidence

Every generated claim in this record is source-derived:

| Claim | Nearest source | Review |
|---|---|---|
| Minted record identifier `habitatmech:GOLD.0e7950bba4` | `src/habitatmech/seed.py`, `data/raw/gold_ecosystem_paths.tsv:555` | Supported exactly by `mint("GOLD", canonical_path)` |
| Label `Breast abscess`, host-associated category, GOLD source id, source path, 9-organism assertion count, and no study or biosample assertions | `data/raw/gold_ecosystem_paths.tsv:555` | Supported exactly |
| `NOT_APPLICABLE` / `REVIEWED` status and the first curation-history event | `curation/decisions.tsv:178` | Supported exactly |
| Parent `habitatmech:GOLD.89cf14e129` | GOLD parent-path emission in `src/habitatmech/seed.py`, backed by `data/raw/gold_ecosystem_paths.tsv:684` | Supported exactly |
| Locked filename | `data/habitats/PATHS.tsv:1384` | Supported exactly |

The record has no xrefs, definition, synonyms, environmental parameters, characteristic taxa, record-level evidence, causal graphs, discussion links, or datasets. Those absences are consistent with exact ignored/hidden-inclusive searches that found no maintained term-request row, causal-graph overlay, history entry, target-specific external xref, environment-parameter row, dataset row, or prior exact YAML review report for `habitatmech:GOLD.0e7950bba4`, `gold.ecosystem:6322`, `breast_abscess`, or `Breast abscess`.

## Completeness

No consequential slot is underfilled for the maintained inputs that feed this record:

- The item-level decision captures the full curator judgement needed for a `NOT_APPLICABLE` generated record.
- The sole GOLD source attestation carries the path's first and only GOLD node id, canonical path, leaf label, and 9-organism assertion count with the correct `ORGANISM` assertion unit.
- The parent list preserves the immediate GOLD path parent, `Mammary gland`, so the generated record remains browsable in its source hierarchy even though its own leaf is not a valid habitat identity.
- A contextual lesion research report under `research/habitats/host_associated/` mentions `habitatmech:GOLD.0e7950bba4` and Breast abscess as examples that remained `NOT_APPLICABLE`; it does not introduce a competing maintained decision or target-specific causal/evidence artifact for this record.

Ignored/hidden-inclusive exact searches covered `curation`, `history`, `research`, `reports`, `data/raw`, `data/habitats/PATHS.tsv`, and the generated target, excluding generated `build`, `data/text_map`, and `pages` trees. They found the maintained decision, raw GOLD row, path lock, generated YAML, Mammary gland parent record, and the contextual lesion research mention cited above, and no target-specific term request, causal overlay, external xref, environment parameter, dataset, history record, or exact prior YAML review report.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the same focused validation set if future curation changes the GOLD Breast abscess decision, raw GOLD rollup, GOLD path parent emission, or path lock:

- `just validate data/habitats/host_associated/breast_abscess.yaml`
- `just validate-strict data/habitats/host_associated/breast_abscess.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `git diff --check`

If future review changes this decision away from `NOT_APPLICABLE`, update `curation/decisions.tsv` for `habitatmech:GOLD.0e7950bba4`, regenerate with `just seed`, and verify the GOLD attestation and Mammary gland parent stay attached to the surviving record or its replacement.

## Additional Notes

- `find reports/yaml_record_review -name '*breast_abscess*' -print` found no pre-existing exact review report for this record before this file was written.
- Exact ignored/hidden-inclusive content searches for `Breast abscess`, `breast_abscess`, `gold.ecosystem:6322`, and `habitatmech:GOLD.0e7950bba4` found the maintained source and decision rows cited above. The same broader GOLD Mammary gland search found sibling Milk, Breast cyst, and Discharge paths; those rows share the same source parent but do not feed this target.
