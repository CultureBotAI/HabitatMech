# PR Review: Aquarium Through Bench Surface

- PR: https://github.com/CultureBotAI/HabitatMech/pull/1616
- Scientific baseline: `ca366555ec4e19694bec1154e1d892c4242bc6c0`
- Report commit: `ba7374bba687176c49f942c4baad22d59c1463bc`
- Correction/build commit: `b84544019edfc8c9bff28d060a411458c57f4074`
- Reviewer: Codex, separate adversarial pass; no independent approval claimed.

## Scope and Method

Publish the seven completed individual reports for Aquarium, Archaea,
Artificial seawater, aviation fuel, laboratory Bacteria, bagasse and Bench
surface unchanged. Benzene's interrupted investigation is not a completed
report and is not included. Historical report verdicts and no-edit statements
describe their baseline, not this subsequently authorized curation session.

Read the maintained curation guidance, full reports, corrected generated
records and immediate hierarchy, importer, tests, changed diffs and rendered
claims. Challenge scope, ontology currency, provenance, preservation and
product freshness. Search open and closed issue titles and bodies for exact
target IDs before filing; reuse #282 and #1249. Local absence searches include
ignored files. The configured original BTO and ontology inputs were not found
under the bounded local source paths; this is not global evidence of absence.

Recheck primary BTO OWL, NLM MeSH concept M0568791, the FAO sugarcane byproducts
chapter and Gohli et al. DOI:10.1186/s40168-019-0772-9 surface-sampling methods.
These support class distinctions, not attribution of every GOLD sample to
those studies. No paid research, subagent approval or cross-repository
scientific edit occurred.

## Findings and Disposition

1. **Major hierarchy error, #1617, corrected.** A guarded GOLD exclusion
   removes MeSH Solid Waste from generic bagasse. Retained bagasse used as
   fuel or feedstock need not satisfy MeSH's discarded-material scope.
   Preserve ENVO:00002264 waste material, the definition, exact synonym,
   three GOLD node IDs, 23 ORGANISM assertions and existing SEEDED status.
   Do not infer a narrower discarded-bagasse identity from source placement.
2. **Major hierarchy error, part of #282, corrected.** Remove only Bench
   surface's immediate subway-environment location parent, without inventing
   a definition or replacement genus. Preserve gold.ecosystem:5464, source
   path, count omissions and UNGROUNDED/SEEDED. The five other surface
   members of #282 are outside this review and remain open.
3. **Major importer defect, #1618, corrected.** `_load_bto` initialized an
   empty deprecated field without reading `owl:deprecated`. It now retains
   semsql literal values for labeled BTO subjects. Tests cover true, false,
   1, 0 and surrounding whitespace, plus absent flags, unrelated/unlabeled
   subjects, preserved definitions/hierarchy and an absent database.
   This corrects future extraction, not the current committed source slice.
4. **Minor provenance defect, #1620, corrected append-only.** The history
   scaffold defaulted three actor names to claude-code despite the correct
   codex-gpt-5 model and codex tool. Three new audit entries explicitly name
   Codex and reference the original sessions; no original history was edited.
5. **Shared deprecated parent, #1619, unresolved.** Archaea inherits
   BTO:0000316 and laboratory Bacteria both inherits and explicitly selects
   it. Current primary BTO marks that term obsolete without an exact
   replacement. BTO:0002233 is filtered liquid culture medium, not a safe
   general-medium replacement. Governed source refresh and reconciliation
   of the parent and eight explicit dependent decisions remain necessary.
   No raw inventory or checksum was patched and no mapping is guessed.
6. **Shared synonym contract, #1249, unresolved.** Added the aviation-fuel
   witness: jet fuel is an ENVO related synonym but is emitted exact. The
   flat source inventory cannot recover predicates it does not store. The
   governed typed-source repair remains open; no one-term generated patch
   or blanket downgrade was applied.

No further blocking defect introduced by this scoped correction was found.
Unresolved baseline science is not converted into a pass by successful CI.
This PR does not certify SSSOM/KGX readiness against current kg-microbe.

## Regression and Preservation

The new focused tests first failed in six expected cases, with the missing-DB
control passing. After the fix, the complete BTO/exclusion suite passed all
36 tests. A full-corpus before/after regression proves identical membership
and changes to only bagasse and Bench surface, limited to parents and new
audit events. All other fields and every other record remain unchanged.

Both regenerated canaries were read after a successful dry seed. Exact
reproduction finds 3,207 expected and actual records, zero missing, extra or
differing. Strict validation of both targets passes. All seven original
report contracts pass, with two pass verdicts and five major baseline findings.
The evidence URLs in the rendered bagasse note have the exact intended hrefs.

## Generated Products

Complete semantic input comparison has unchanged membership and exactly two
changed rows, bagasse and Bench surface:

- Before SHA-256: `9b09960700db33d361e73e617daa33c5a27f4628f1dc53c9253f7ddd42a0ea5a`.
- After SHA-256: `88dd28208dd405a82d97aab4deb30d4114ce63d0a603ca2db9bba58e05d72e5a`.
- New bundle: `4f6ef74fc6d77b4c1c12f2b5829290ca645fe2178de5e6efd9a5c2ea4e35c541`.

[Map build 37579784580](https://github.com/CultureBotAI/HabitatMech/actions/runs/37579784580)
used the unchanged locked Linux runtime and verified the previous profile-bound
cache. The changed-record canary encoded two vectors and reused both on repeat.
The projection canary passed; the full embedding step reused all 3,207 vectors,
then real PaCMAP generated all 3,207 coordinates with zero omitted records.
Downloaded input bytes exactly match the local export. Both downloaded and
imported bundles validate against the actual vector cache and fresh full inputs.

Rendering produced 3,207 habitat pages, 249 redirects, eight categories and
126 displayed term requests. Only the two habitat pages and map assets change;
no URL or identity is retired. Prior immutable bundles, map enablement, runtime
pins, raw inputs and manifests are unchanged. The temporary read-only branch
workflow is removed from the final diff. Browser visual QA was not performed.

## Validation and Remaining Gates

Completed: lint, focused tests, dry seed, inspected canaries, strict target
validation, exact corpus reproduction, seven report contracts, 137 valid
history sessions, semantic/cache validation, site rendering and diff checks.
OAK passed with 1,178 canonical matches, one synonym, five accepted exceptions
and 2,056 no-adapter skips; those skips and the known obsolete class are not
scientific endorsements. Vendored sync passed for all 18 governed artifacts
after retrying a sandbox DNS failure with network access.

The first rendering attempt correctly refused the stale map before rebuilding;
no freshness check was weakened. Full local QC is running at audit creation.
Final-head CI and exact merge-queue candidate checks remain required, and their
terminal receipts will be posted on the PR. No admin bypass or fabricated
approval is permitted. The corpus-wide review remains unfinished; this is
publication of seven completed reviews, not completion of every record.
