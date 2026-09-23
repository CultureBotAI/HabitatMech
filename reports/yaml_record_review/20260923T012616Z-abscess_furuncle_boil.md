# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/abscess_furuncle_boil.yaml`
- Started UTC: 2026-09-23T01:21:00Z
- Finished UTC: 2026-09-23T01:26:16Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/habitats/host_associated/abscess_furuncle_boil.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.ef667faebd` |
| Label | `Abscess: Furuncle/Boil` |
| Habitat category | `HOST_ASSOCIATED` |
| Grounding status | `NOT_APPLICABLE` |
| Mapping status | `REVIEWED` |
| Record status | Generated from one GOLD source concept with an item-level `NOT_APPLICABLE` decision |
| GOLD source id | `gold.ecosystem:7010` |
| GOLD source path | `Host-associated > Mammals: Human > Integumentary system > Skin > Abscess: Furuncle/Boil` |
| Decision row | `curation/decisions.tsv:1321` |
| Locked slug | `data/habitats/PATHS.tsv:3066` maps `habitatmech:GOLD.ef667faebd` to `abscess_furuncle_boil` |

This is the generated record for the GOLD skin `Abscess: Furuncle/Boil` path. The GOLD source-concept key is `habitatmech:GOLD.ef667faebd`, computed as `sha1("GOLD:Host-associated > Mammals: Human > Integumentary system > Skin > Abscess: Furuncle/Boil")[:10]`. The current record faithfully reflects the maintained decision row, but that row needs curation review: the committed rationale does not explain why this specific skin abscess leaf is non-habitat while the sibling GOLD `Host-associated > Mammals: Human > Integumentary system > Skin > Abscess` record is retained as a `NARROW` habitat under `mesh:D000038`.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/habitats/host_associated/abscess_furuncle_boil.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/host_associated/abscess_furuncle_boil.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; validated 32 causal-graph curation files with 32 graphs. |
| `just term-requests-check` | Passed; the term-request table is current at 109 terms. |
| `just validate-history` | Passed; 77 history records validated. |
| `just verify-corpus --max-diffs 1` | Passed; all 3,206 generated records reproduced exactly from `data/raw/`, with 0 missing, 0 extra, and 0 differing. |
| `just worklist --limit 2000` | Passed when rerun outside the sandbox; reported 0 undecided ungrounded records and 1,810 decisions on file. The target is absent, as expected for a `REVIEWED` item-level `NOT_APPLICABLE` concept rather than undecided backlog. |
| `just report` | Passed; the corpus summary still reports 0 risky groundings not yet reviewed, 0 contradicted sweeps, and 0 current records claiming a non-habitat organism/process term as a habitat. |
| `git diff --check` | Passed before this report was written. |

## Identity and Grounding

The minted identity is reproducible. `data/raw/gold_ecosystem_paths.tsv:2279` is exactly the GOLD path `Host-associated > Mammals: Human > Integumentary system > Skin > Abscess: Furuncle/Boil`, and the path hashes to `ef667faebd`. `data/habitats/host_associated/abscess_furuncle_boil.yaml:1-13` preserves the minted identifier, label, `gold.ecosystem:7010` source id, source label, and full source path.

The locked slug is also correct: `data/habitats/PATHS.tsv:3066` maps `habitatmech:GOLD.ef667faebd` to `abscess_furuncle_boil`, and an ignored-file-inclusive `find data/habitats -name 'abscess_furuncle_boil.yaml' -print` found exactly one generated target.

The raw source row has 0 organism assertions, 0 study assertions, 0 biosample assertions, and 0 total assertions. The generated source attestation therefore correctly omits `assertion_count`, `assertion_unit`, and a multi-node note while preserving the one GOLD node id `gold.ecosystem:7010`.

The source-path parent is mechanically traceable: `data/habitats/PATHS.tsv:1848` maps `habitatmech:GOLD.4b37ab4b76` to `skin__621b7871`, `data/raw/gold_ecosystem_paths.tsv:49` records the immediate parent path `Host-associated > Mammals: Human > Integumentary system > Skin`, and `data/habitats/host_associated/skin__621b7871.yaml:1-16` is the generated parent record for that path.

`mapping_status: REVIEWED` follows the maintained item-level decision. `curation/decisions.tsv:1321` records `NOT_APPLICABLE` with `review_depth: ITEM` for `habitatmech:GOLD.ef667faebd`, and the generated `curation_history` mirrors that action in `data/habitats/host_associated/abscess_furuncle_boil.yaml:14-25`.

The `NOT_APPLICABLE` grounding is the unsupported part. The decision note says the leaf names "a disease, an intervention, a sampling artefact or a no-value filler rather than a place", but it does not choose which of those incompatible explanations applies, and it does not explain why this skin-specific abscess subtype should be excluded while the sibling GOLD skin `Abscess` path remains a minted `NARROW` habitat under generic `mesh:D000038`.

## Evidence

| Claim | Source | Assessment |
| --- | --- | --- |
| The record represents the GOLD path `Host-associated > Mammals: Human > Integumentary system > Skin > Abscess: Furuncle/Boil`. | `data/raw/gold_ecosystem_paths.tsv:2279`; `data/habitats/host_associated/abscess_furuncle_boil.yaml:8-13` | Supported exactly. |
| The path is an empty GOLD leaf with no organism, study, or biosample assertions. | `data/raw/gold_ecosystem_paths.tsv:2279`; `data/habitats/host_associated/abscess_furuncle_boil.yaml:8-13` | Supported exactly. |
| `habitatmech:GOLD.4b37ab4b76` is the immediate GOLD source-path parent. | `data/raw/gold_ecosystem_paths.tsv:49`; `data/habitats/PATHS.tsv:1848`; `data/habitats/host_associated/skin__621b7871.yaml:1-16` | Supported as the generated parent from the GOLD path hierarchy. |
| `curation/decisions.tsv` intentionally marks this source concept `NOT_APPLICABLE`. | `curation/decisions.tsv:1321`; `data/habitats/host_associated/abscess_furuncle_boil.yaml:14-25` | Supported mechanically. |
| The source concept is not a habitat. | `curation/decisions.tsv:1321` | Needs curation. The row is item-level, but the rationale is generic and conflicts with the accepted skin `Abscess` sibling at `data/habitats/host_associated/abscess.yaml` and with the existing lesional-skin research report's recommendation to reopen this exact decision. |
| The vendored ontology slice has a broader abscess term but no exact furuncle, boil, or pilonidal sinus term. | `data/raw/ontology_terms.tsv:13554`; exact ignored/hidden-inclusive search of `data/raw/ontology_terms.tsv` for `furuncle`, `boil`, `pilonidal`, and `abscess` | Supported. `mesh:D000038` labels generic `Abscess`; exact disease-subtype labels are not vendored. |

Unsupported or over-scoped claims: the `NOT_APPLICABLE` decision is under-supported for this source path. No environmental parameters, characteristic taxa, causal graphs, definitions, xrefs, datasets, or literature evidence are asserted by the generated record.

## Completeness

The record is intentionally sparse: a current `NOT_APPLICABLE` decision leaves it without a definition, exact ontology identity, external xrefs, environmental parameters, characteristic taxa, causal graphs, discussion links, datasets, and assertion counts.

Exact ignored/hidden-inclusive content searches for `habitatmech:GOLD.ef667faebd`, `gold.ecosystem:7010`, `Abscess: Furuncle/Boil`, and `abscess_furuncle_boil` found the maintained `curation/decisions.tsv` row, the raw GOLD row, the locked `PATHS.tsv` row, a `docs/HARMONIZATION.md` example of GOLD colon splitting, the `src/habitatmech/proposals.py` variant-splitting example, sibling Abscess review mentions, and one lesional-skin research report mention. The same search found no target-specific `curation/term_requests.tsv`, `curation/term_requests_excluded.tsv`, `curation/causal_graphs`, or `history` entry.

Filename searches found no target-specific maintained overlay or prior report: `find curation/causal_graphs history research/habitats reports/yaml_record_review \( -name '*abscess_furuncle_boil*' -o -name '*ef667faebd*' -o -name '*gold-ef667faebd*' \) -print` returned no rows before this report was written. Those `find` checks include ignored files beneath the checked directories.

The consequential gap is the curation decision itself. `research/habitats/host_associated/lesion-habitatmech-gold-5caa9dd47f-deep-research-claude_code.md:319` already identifies `habitatmech:GOLD.ef667faebd` as a skin-lesion sibling whose August 12 `NOT_APPLICABLE` disposition is hard to reconcile with lesional-skin habitats, but no maintained follow-up decision has been committed.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The `NOT_APPLICABLE` decision for `Abscess: Furuncle/Boil` needs reopening. The current row uses the shared "disease, intervention, sampling artefact or no-value filler" rationale without explaining why this child of `Skin > Abscess` is outside HabitatMech, and the record is inconsistent with the accepted `Skin > Abscess` source concept unless a curator writes a target-specific distinction. | `curation/decisions.tsv:1321` marks `habitatmech:GOLD.ef667faebd` `NOT_APPLICABLE`; `data/raw/gold_ecosystem_paths.tsv:448` and `data/habitats/host_associated/abscess.yaml` keep the sibling skin `Abscess` as a `NARROW` habitat under `mesh:D000038`; `research/habitats/host_associated/lesion-habitatmech-gold-5caa9dd47f-deep-research-claude_code.md:319` calls out this exact row as part of the skin abscess, ulcer, and lesion disposition inconsistency. | `curation/decisions.tsv` |

No blocker findings.

No minor findings.

## Recommended Edits

Reopen `curation/decisions.tsv:1321` for `habitatmech:GOLD.ef667faebd`.

If item-level review confirms that `Abscess: Furuncle/Boil` denotes a specific skin abscess habitat, replace the row with a `GROUND_AS_PARENT` decision targeting `mesh:D000038` / `Abscess`, with `grounding_status: NARROW`, `review_depth: ITEM`, and notes that quote the full source path. After reseeding, the generated record should keep the minted identifier, keep the GOLD skin source-path parent, add generic `mesh:D000038` as a broader parent, and change its GOLD attestation to `skos:narrowMatch`.

If item-level review instead retains `NOT_APPLICABLE`, replace the generic disease/intervention/artifact/filler note with target-specific evidence that explains why a GOLD `Skin > Abscess: Furuncle/Boil` source concept is outside the HabitatMech habitat model while `Skin > Abscess` is inside it.

Review `Abscess: Pilonidal sinus` in the same family pass if this row changes; it sits at the adjacent GOLD skin path and carries the same style of `NOT_APPLICABLE` decision for `habitatmech:GOLD.628407fcc7`.

## Follow-up Checks

After the maintained decision row changes, run:

- `just seed`
- `just seed-canary habitatmech:GOLD.ef667faebd`
- `just validate data/habitats/host_associated/abscess_furuncle_boil.yaml`
- `just validate-strict data/habitats/host_associated/abscess_furuncle_boil.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000`
- `just report`
- `git diff --check`

Also re-run the exact ignored/hidden-inclusive search for `habitatmech:GOLD.ef667faebd`, `gold.ecosystem:7010`, and `Abscess: Furuncle/Boil` to confirm the new decision is the only maintained curation input for this source concept unless a term request or causal overlay is intentionally added.

## Additional Notes

- The pre-report exact filename check `find reports/yaml_record_review -maxdepth 1 -type f -name '*-abscess_furuncle_boil.md' -print` returned no previous exact report; `find` includes ignored files.
- The pre-report exact record check `find data/habitats -name 'abscess_furuncle_boil.yaml' -print` found exactly one generated target; `find` includes ignored files.
- The first sandboxed `just worklist --limit 2000` attempt failed because `uv` could not open `/Users/marcin/.cache/uv/sdists-v9/.git`; the unsandboxed rerun completed successfully.
- Existing sibling reports for plain `Abscess` records correctly treated the `Abscess: Furuncle/Boil` row as specific to this colon-expanded skin leaf, not as a decision about every GOLD `Abscess` leaf.
