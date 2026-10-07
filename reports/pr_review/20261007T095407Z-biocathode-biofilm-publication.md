# Biocathode biofilm publication review

- PR: https://github.com/CultureBotAI/HabitatMech/pull/1630
- Baseline: `344719b7cd2c69a84aa764fb38f112650c8fe879`
- Reviewed fix: `6e5aed81f2c74abfc659dae729a0530c6462fd83`
- Actor correction: `5a521d1f4868b7da8c2f9c8639bfd209a56d465f`
- Status at 2026-10-07T09:54:07Z: fixes implemented; publication checks pending.

## Scope and Method

Publish the completed individual review of `biofilm__3aa782aa.yaml` only.
The interrupted MFC/Anode biofilm review is not part of this PR. This is a
separate adversarial pass by Codex, not an independent human or agent approval.

Re-read the complete generated target and Biocathode parent, inspected the
maintained exclusion route, neighboring regression tests, primary Nevin abstract,
source inventory row, complete scientific diff and both session histories.
Ignored-inclusive searches covered maintained inputs, histories, configuration,
docs, tests, research, its manifest and PATHS. The original record-review report
remains an immutable assessment of the pre-correction baseline.

## Findings and Fixes

1. **Major, #1631:** biofilm microbial material was asserted to be a kind of
   its biocathode substrate. One row in `curation/gold_parent_exclusions.tsv`
   guards source `habitatmech:GOLD.5eaebd18a7`, the exact industrial-product
   Biocathode/Biofilm path and expected parent `habitatmech:GOLD.a06aa6619e`.
   Only that GOLD contribution and the resulting audit event change.
   Independent ENVO:00002034, identity, source5682, zero-count omissions,
   skos:narrowMatch and NARROW/SEEDED status remain intact. The inspected
   [Nevin et al. abstract](https://pubmed.ncbi.nlm.nih.gov/20714445/),
   DOI:10.1128/mBio.00103-10, supports the biofilm/substrate distinction,
   not a GOLD study crosswalk or transfer of experimental conditions.
2. **Minor, #1632:** history scaffolding defaulted the actor name to
   `claude-code` despite the explicit Codex tool field. An append-only history
   correction explicitly names Codex and references the original record.
   The committed original is retained; no second scientific change is implied.

No additional defect was established in the inspected fix. This does not
certify products that are still awaiting regeneration or final CI.

## Completed Checks

- New full-corpus differential regression failed before the exclusion existed.
  All 34 exclusion tests then passed with the correction.
- Dry seed and target canary passed; the entire generated canary was inspected.
  No bulk write was needed: all 3,207 records already reproduced exactly.
- Open and strict target validation passed; strict validation reported zero errors.
- Full before/after semantic input comparison changed only the target record.
  New full input SHA: `6538fc181f505dd24905aabb50c62ab92590fa1d28a2dc3ae8d1191900af7dad`.
- All 146 session histories validate. Curation floor and focused lint pass.
- OAK passed: 1,178 canonical, one synonym, five accepted exceptions and
  2,056 explicitly skipped pairs without adapters.
- All 18 governed artifacts match the pinned CLAW revision. The first fetch
  failed under sandbox DNS; the network-enabled rerun passed.
- The prior full map and profile-bound vector cache validate against the
  unchanged baseline inputs. Raw inventories, PATHS, RETIRED, schema and
  application behavior are unchanged.

## Publication Blocker and Remaining Gates

The temporary Linux map build
[37602085441](https://github.com/CultureBotAI/HabitatMech/actions/runs/37602085441)
was still queued without a runner after approximately 15 minutes. No steps,
startup diagnostics or pending environment approvals were reported. Required
PR QC, OAK and vendored-sync jobs were also queued. No check was bypassed.

The local Intel macOS machine cannot use the pinned ARM-only macOS Torch
wheel. Installed Docker Desktop reports running, but its Linux API returns
EOF and its status command hangs. It was not restarted or reconfigured.

After the queued build completes, download its artifact, verify full input
identity/cache/coverage and finite coordinates, stage the generated bundle,
remove the temporary workflow, and render the site. Run the extended exact
PubMed-link regression and fresh complete `just qc`; they have not yet passed
for this publication. Commit and push products and verify required final-head
and combined merge-queue checks before merging. Then verify merge integrity,
close both linked issues and delete the local and remote feature branches.

The PR remains draft, both issues remain open pending merge, and the branch
must not be deleted yet. The stale map/site are intentionally not certified.
The complete review goal remains active: 1,108 of 3,207 current records have
reports (1,109 report files), with 2,099 records remaining. No SSSOM or KGX
readiness certification is implied.
