# Composting Variants Publication Adversarial Review

- PR: https://github.com/CultureBotAI/HabitatMech/pull/1669
- Baseline: `9cfd3bc25bee54dcadb31fabc0be848266de9dd5`
- Reviewed report commit: `16cdc1d8d`
- Snapshot UTC: 2026-10-08T00:23:02Z
- Disposition: one report recommendation corrected below; source-scope and
  mapping-contract findings remain unresolved. Required CI is pending.

## Scope and Method

Separate adversarial self-review by Codex, not an independent reviewer. Read
both complete reports and generated records, the actual seeder fallback and
attestation construction, schema endpoint/status descriptions, and lifecycle
derivation. Re-executed exact resolution with complete claimant/mapping indexes
and compared each complete generated document with its committed YAML.

The immutable individual reviews are:

- [Bagasse-qualified Composting](../yaml_record_review/20261008T000835Z-composting__0995fad8.md)
- [Feedstock-qualified Composting](../yaml_record_review/20261008T001124Z-composting__17c06daf.md)

Ignored-inclusive exact-key searches covered curation, history, conf, tests,
docs, research, raw inventories and path registries. All 712 then-existing
open/closed GitHub issue titles and bodies were searched for the exact source
keys and related titles; #1398's comments were checked for these witnesses.
No earlier exact-source issue was found. Repository-wide issue comments were
not exhaustively searched.

## Findings and Disposition

1. **Major, [#1670](https://github.com/CultureBotAI/HabitatMech/issues/1670),
   unresolved:** Bagasse-qualified GOLD.edeecbabed lacks verified exact-source
   scope sufficient to assess its compost and bagasse parents. Source nodes
   4926/4927, one ORGANISM assertion, five separate BIOSAMPLE observations and
   study Gs0144819 remain distinct provenance facts, not a material definition.
   This is not proof that either parent is false. The generic bagasse correction
   in #1617 does not resolve this child's meaning.
2. **Major, [#1671](https://github.com/CultureBotAI/HabitatMech/issues/1671),
   unresolved:** Feedstock-qualified GOLD.5948923b46 likewise lacks an ITEM
   assessment separating material, process and input context. Its undefined
   Feedstock parent and that parent's CLASS screening do not settle strict
   subsumption. Preserve nodes 4892/4893 and two ORGANISM assertions separately
   from six BIOSAMPLE observations and study Gs0053053.
3. **Major, shared [#1398](https://github.com/CultureBotAI/HabitatMech/issues/1398),
   unresolved:** both actual routes retain their source mint while assigning
   NARROW/skos:narrowMatch and the ENVO compost parent. The schema declares
   source-to-record mapping endpoints and source-relative grounding status;
   the implementation's comparison instead uses an ontology parent. A global
   predicate reversal does not resolve that endpoint mismatch. These are two
   additional witnesses to the existing issue, not new independent defects.
4. **Minor, [#1672](https://github.com/CultureBotAI/HabitatMech/issues/1672),
   corrected by this addendum:** the Feedstock report's Recommended Edits asks
   to preserve SEEDED while also recommending future ITEM curation. The
   lifecycle instruction needs the qualification immediately below.

## Superseding Lifecycle Recommendation

This section supersedes only the instruction to preserve SEEDED in the
Feedstock review's Recommended Edits. It does not change that review's
time-bounded observations, source-scope verdict or evidence limitations.

Preserve the source mint, nodes/path, counts with their units, and historical
provenance. While no ITEM decision exists, SEEDED accurately reflects this
record's state. After evidence-backed curation, let `build_document` derive
`mapping_status` from the contributing sources: REVIEWED when every source is
reviewed, otherwise SEEDED. Never hand-edit generated status or keep it frozen
at SEEDED after the review criterion is met. Report publication alone supplies
no ITEM decision and therefore does not promote either record.

The owning implementation is `src/habitatmech/seed.py:1441-1445`; no schema or
generator change is needed for this wording correction.

## Remediation Attempts and Evidence Limits

The [Gs0144819 study request](https://gold.jgi.doe.gov/study?id=Gs0144819)
remained inaccessible through the browser tool. The
[Gs0053053 request](https://gold.jgi.doe.gov/study?id=Gs0053053) returned GOLD's
request-processing error page, not study metadata. Fresh exact-accession and
NCBI-scoped searches did not recover a verified source-to-sample/paper crosswalk.
Generic composting articles returned by broad searches were not imported.
The current shell has no exported GOLD API credential, and the documented
`build/gold_cache` directory is absent; authenticated API recovery was not run.

The freshly inspected [EPA definitions](https://www.epa.gov/sustainable-management-food/composting)
distinguish inputs, composting activity and finished compost. They do not
define these exact GOLD categories. Fresh OLS browser requests failed; the
individual reports explicitly record their earlier successful API checks.
No inaccessible source is treated as absent, and no scientific replacement
identity, definition, exclusion or review-status promotion is justified here.

Future supported fixes belong in maintained decisions and, where justified,
definitions or exact source/path/expected-parent exclusions. They require
source-preservation regressions, append-only history, dry seed, an inspected
canary, guarded regeneration and all affected product checks. The shared
mapping contract additionally needs explicit endpoints and consumer tests.

## Verification and Merge Conditions

- Fresh strict validation: two files scanned, zero errors.
- Both complete target documents reproduce exactly; each has one source,
  zero reviewed sources, no applied decision and a matching recomputed mint.
- Both default and applied routes are `gold_narrower_than_mapping_match`.
- Structured exact-field/pipe-member scans cover all 14 raw TSVs and recover
  exactly the three source rows per target stated in the original reports.
- No scientific input, generated YAML/page, history, code, schema or runtime
  pin is changed. No semantic map rebuild is necessary for report-only edits.
- The preceding publication's 552-test full-QC baseline is unchanged code/data
  evidence, not a fresh local full-QC run for this PR. Final-head PR checks and
  native merge-queue checks must pass before merge; their receipts belong on
  the PR after completion, not in a rewritten snapshot.

Only #1672 is resolved by this correction. Keep #1670, #1671 and #1398 open
after report publication. No SSSOM/KGX execution, current kg-microbe modeling
certification or full-corpus scientific approval is claimed. No unrelated
pending individual review is included in this publication.
