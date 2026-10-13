# Adversarial Review: Benzene Publication

- PR: https://github.com/CultureBotAI/HabitatMech/pull/1621
- Scientific baseline: `93b9b08ec54baf01b024171b5e3d346a48d2a919`
- Review-only commit: `23f9eb4553fd1916518e4f5ba3e2c3d4dd43018d`
- Fix and Linux build input: `d9f3e58382e391c5103dcfb1c2e97559618f1da7`
- Finding: one major, no blocker or minor established; tracked in #1622.

## Finding and Correction

The complete Benzene report and maintained inputs were rechecked. Its sole
broader-habitat parent was explicitly ITEM NOT_APPLICABLE and chemical-valued.
Primary [ChEBI hydrocarbon](https://www.ebi.ac.uk/chebi/CHEBI:24632) confirms the
compound class, not a habitat genus. All-state Benzene issue search found no
existing issue; related #1235 concerns four different source keys.

One guarded row in `curation/gold_parent_exclusions.tsv` removes that source
contribution. The original report remains unchanged as a pre-fix assessment.
The generated record loses only the parent and gains a deterministic audit
event. Source path/node, identity, CLASS/SEEDED status, empty counts, previous
events and all other records are unchanged. No replacement genus, definition,
chemical grounding, treatment matrix or identity-review promotion is asserted.
Session provenance explicitly attributes the curation to Codex.

## Verification

- The new regression failed before the row; all 31 exclusion tests then passed.
- Dry seed and inspected target canary passed; all 3,207 records reproduce.
- Open and strict target validation passed; all 138 history records validated.
- OAK passed: 1,178 canonical, one synonym, five accepted exceptions and 2,056
  no-adapter skips. This does not establish Benzene's unresolved source scope.
- All 18 governed artifacts match the pinned revision after retrying the
  sandbox-blocked network fetch with network access. Lint and curation floor pass.
- Full semantic-input comparison changes only Benzene. The locked Linux
  [build](https://github.com/CultureBotAI/HabitatMech/actions/runs/37583614395)
  encoded its changed text once, reused it on repeat, then reused all 3,207
  vectors for the full build. A 32-record projection canary also passed.
- Downloaded bundle `df9403802cf718fe56e93943bb1c20fe30c65f82c9f27ffb2e874df35e3823c8`
  validates locally against byte-identical fresh full inputs and its vector
  cache. It displays 3,207 records with none omitted. Only Benzene's text hash
  changes in map metadata; all coordinates were legitimately reprojected.
- Render completed: 3,207 habitat pages, 249 redirects, eight categories and
  126 displayed term requests. The only habitat-page diff is Benzene's removed
  parent and appended event. The temporary build workflow is removed.

## Remaining Gates and Limits

Full local QC is running at this report's timestamp. Final-head CI and merge
queue checks must pass before merge; their terminal receipts belong on the PR.
Local locked inference is unavailable on Intel macOS because the pinned Torch
release has no wheel for that platform; the successful Linux build replaces
that execution, not any validator. Original GOLD source scope remains unresolved
under the curation backlog (#12). This PR does not certify SSSOM/KGX readiness
or complete the ongoing all-record review goal. No further fix regression was
established in the final scientific and structured generated-product diff.
