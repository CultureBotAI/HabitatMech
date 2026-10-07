# Adversarial Review: Engineered Biofilm Publication

- PR: https://github.com/CultureBotAI/HabitatMech/pull/1626
- Scientific baseline: `67e23dba664c23b7a628406893a3be597238aeac`
- Review-only commit: `335692bf9b91b10df9e941eeff4819dc3aadc65f`
- Fix and Linux build input: `94c52589697d12cd85c3206a541a04a3f1269105`
- Findings: two major (#1627/#1628), one minor (#1629), no blocker established.

## Scope and Findings

This is a same-agent adversarial pass, not independent human approval. Re-read
the three completed individual reports, target records, relevant full context
parents, maintained hierarchy rules, exact raw source rows and complete
scientific/test/provenance diff. The waste-qualified Biochar report supports
no immediate correction at its provisional scope; its feedstock-versus-discarded
material uncertainty remains unresolved. The unfinished industrial-product
Biocathode biofilm review is outside this publication and is not counted.

- #1627: `habitatmech:GOLD.6b1f16702e` denotes biofilm material, not a subtype
  of ENVO:00002126 aerobic bioreactor. Retain the independent ENVO:00002034
  genus. Current ENVO definitions and the freshly inspected primary abstract
  [de Beer et al. 1994](https://pubmed.ncbi.nlm.nih.gov/18615526/) distinguish
  biofilm structure from its surrounding liquid/system; the experiment does
  not identify the GOLD source or imply uniform oxygen conditions.
- #1628: `habitatmech:GOLD.b77f846671` denotes attached biofilm, not a subtype
  of `habitatmech:GOLD.5d36b86f15` Cathode. The freshly inspected primary abstract
  [Nevin et al. 2010](https://pubmed.ncbi.nlm.nih.gov/20714445/) distinguishes
  biofilms from cathode surfaces. This adjacent electrosynthesis experiment
  does not establish a GOLD MFC crosswalk, electrode composition or organism.

Ignored-inclusive ID/path/slug searches covered curation, history, configuration,
tests, research and the research manifest before adding rows. No prior target
exclusion was found there. The all-state GitHub biofilm issue search was
inspected; #1423 and the other listed issues concern different source keys.
Exact-field scans of all 14 raw TSVs reconfirmed the two ecosystem rows and
no other target-key contributions. Searches are bounded, not global absence
claims. The original source-data access limits remain in the individual reports.

## Corrections and Regression

Two exact mint/path/expected-parent rows in
`curation/gold_parent_exclusions.tsv` remove only the unsupported GOLD
contributions. No identity, category, grounding decision, definition, source
inventory, source predicate, count/unit or review-status change occurs.
Both records stay NARROW/SEEDED with ENVO:00002034. The aerobic record retains
GOLD5472/5473 and one ORGANISM assertion; the cathode record retains GOLD7659
and count omissions. Deterministic record events and two append-only Codex
session records document the corrections. Original reviews remain unchanged
pre-fix assessments, not verdicts on the corrected branch.

The new full-corpus differential regression failed before the rows were added;
all 33 exclusion tests pass afterward. It proves exactly these two records
change, and only their parent/audit fields. All other records, including the
unfinished Biocathode biofilm, context parents and waste-qualified Biochar,
are unchanged. No blanket Biofilm rule or unsupported replacement relation
was added.

## Verification

- Dry seed and both inspected canaries passed. All 3,207 records reproduce
  exactly, with zero missing, extra or differing records; no bulk write or
  pruning was needed after the two canaries.
- Open and strict validation passed for both targets; all 144 session history
  records validate. Lint, whitespace and curation-floor checks passed.
- OAK passed: 1,178 canonical labels, one synonym, five accepted exceptions,
  2,056 no-adapter skips. All 18 governed artifacts match the pinned revision.
  These checks do not establish the truth of source scope or is-a semantics.
- Full semantic-input comparison changes only the two reviewed biofilms.
  The locked [Linux map build](https://github.com/CultureBotAI/HabitatMech/actions/runs/37595658815)
  passed: two records encoded, both reused on repeat, then all 3,207 vectors
  reused for the full build. The 32-record projection canary and full artifact
  checks passed without changing runtime/model pins.
- Downloaded inputs are byte-identical to the local fresh export. Bundle
  `5cd77a9391b2addc1a9ff2000ea3fe1b024e4dba15faf09087ece6dd91d598d7`
  passes local artifact/cache validation. All 3,207 points are finite and have
  existing page targets; only the two target point metadata entries change,
  while all coordinates are genuinely reprojected.
- Rendering passed for 3,207 habitat pages, 249 redirects, eight categories
  and 126 displayed term requests. Only the two target habitat pages and map
  products changed. The temporary build workflow is removed before publication.

## Remaining Gates and Limits

The rendered-diff pass additionally found both new PubMed hrefs incorrectly
included a trailing semicolon (#1629). A failing page-link regression confirmed
it. The maintained notes now independently delimit each URL; both records/pages
were regenerated. All seven website-audit tests pass with exact parsed hrefs;
the full semantic inputs remain byte-identical. Two appended follow-up session
records preserve the original committed history without alteration.
The obsolete pre-link-fix local QC run was deliberately stopped during pytest
before regeneration; that run is not a passing gate. A fresh full run is required.

Full local QC, final-head CI and combined merge-queue validation are required
before merge; their terminal receipts belong on PR #1626. No additional
actionable defect was established in this bounded pass. This publication does
not certify SSSOM/KGX readiness or complete the all-record review goal.
Fresh ignored-inclusive census: 1,108 reports cover 1,107 of 3,207 current
records; 2,100 records remain without a completed individual report.
