# Adversarial Review: Engineered Habitat Publication

- PR: https://github.com/CultureBotAI/HabitatMech/pull/1623
- Scientific baseline: `92c7c270dbbece1ce5d7db810f41f429822d3704`
- Review-only commit: `ea568c326adbe1158135d4984e366a0bfab3dd2c`
- Fix and Linux build input: `9c30591a0b9e385a954a6cd89fc1211c2ffbb994`
- Finding: one major, no blocker or separate minor established; issue #1624.

## Scope and Finding

Separately re-read all four completed reports, the maintained hierarchy rules,
the target and parent records, and the scientific/test/generated-product diff.
This is a same-agent adversarial pass, not independent human approval.
BGW, Bioanode and Biocathode have no established actionable direct-record defect
at their reports' limited scope. Their parent references are not full reviews
of every ancestor. Missing optional fields do not justify fabricated findings.

Biochar is a material, not a kind of its industrial-production context.
The independent ENVO charcoal parent remains supported. The freshly inspected
[US Forest Service biochar page](https://research.fs.usda.gov/forestproducts/bioeconomy/biochar)
distinguishes product, production technologies and use. All-state GitHub biochar
issue search found no existing issue; ignored-inclusive maintained-input search
found no prior target exclusion. The defect is tracked in #1624.

## Correction and Regression

One exact mint/path/expected-parent row in `curation/gold_parent_exclusions.tsv`
removes only the GOLD context contribution. No source inventory, grounding
decision, definition, identity, category or review status changes. The charcoal
genus, exact predicate, three-node provenance, source path and count omissions
remain intact. The deterministic audit event and append-only Codex session
record document the reason. Original review reports remain unchanged pre-fix
assessments, not claims about the corrected branch.

The new regression failed before the row; all 32 exclusion tests then passed.
Its full before/after corpus comparison proves only ENVO:2000007 changes, and
only its parent and audit fields. The separately minted waste-qualified Biochar
record stays unchanged; its individual review is unfinished and not counted.

## Verification

- Dry seed and inspected canary passed; all 3,207 records reproduce exactly.
- Open and strict target validation passed. History validation passed for all
  139 records; the final Codex-attributed session also passed individually.
- OAK passed: 1,178 canonical labels, one synonym, five accepted exceptions
  and 2,056 no-adapter skips. It does not establish original GOLD source scope.
- All 18 vendored artifacts match after retrying a sandbox-blocked network
  fetch with network access. Lint, whitespace and curation-floor checks passed.
- The full semantic-input comparison changes only ENVO:2000007. The locked
  [Linux build](https://github.com/CultureBotAI/HabitatMech/actions/runs/37589862138)
  encoded it once, reused it on repeat and reused all 3,207 vectors for the full
  build. The 32-record projection canary and full artifact checks passed.
- Bundle `a260d54e79712fc84c77f53030d5055a68b6ed2ee7a9e9b630172c8c9e757abd`
  validates locally against byte-identical fresh inputs and its vector cache.
  All 3,207 records are displayed, with finite coordinates and existing page
  targets. Only biochar's point metadata changes; all coordinates reproject.
- Rendering completed: 3,207 habitat pages, 249 redirects, eight categories and
  126 displayed term requests. Only biochar's habitat page changes. The temporary
  build workflow is removed before the final publication commit.

## Remaining Gates and Limits

Full local QC is still running. Final-head CI and merge-queue checks must pass
before merge; terminal receipts belong on the PR. The successful locked Linux
build supplies inference unavailable with the pinned Torch on Intel macOS.
Original GOLD dump/study access limits and source-scope questions remain as
documented in the individual reviews. No further actionable regression was
established. This PR does not certify SSSOM/KGX readiness or complete the broader
all-record review goal: 1,104 of 3,207 current records have reports, with 2,103
remaining (fresh ignored-inclusive census; 1,105 reports total).
