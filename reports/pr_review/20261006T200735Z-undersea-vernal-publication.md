# PR Review: Undersea Feature and Vernal Pools

- Repository: CultureBotAI/HabitatMech
- PR: https://github.com/CultureBotAI/HabitatMech/pull/1582
- Reviewed head: e7d52c3c10b03d02dc600d31b0c981bac9245397
- Scientific baseline: de3b61e4a6610b56a775a21e0bd78a5e8b31feec
- Review completed UTC: 2026-10-06T20:07:35Z
- Method: separate adversarial self-review; not independent approval
- Verdict: one minor publication defect, corrected below; scientific issues remain open

## Scope

Read both complete new reports and both complete target YAML documents:

- `reports/yaml_record_review/20261006T194744Z-undersea_feature.md`
- `reports/yaml_record_review/20261006T195345Z-vernal_pools__dc503f3c.md`

The original reports remain unchanged. This note is an append-only correction
and publication audit, not another record review or scientific curation event.
The unfinished Volcanic review is not included or counted as complete.

## Publication Correction

[Issue #1583](https://github.com/CultureBotAI/HabitatMech/issues/1583): in the
Undersea feature report's Identity and Grounding section, the preferred label
of ENVO:00000000 is **geographic feature**, not "geographical feature".
The CURIE and asserted hierarchy are correct. This is label precision only;
it does not alter either report's scientific verdict or finding count.

Confirmed against `data/raw/ontology_terms.tsv:6598`,
`data/habitats/other/geographic_feature.yaml`, and the
[official ENVO snapshot](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl).
The hydrographic-feature definition uses the adjective "geographical" in
prose; that wording is not the ancestor's preferred label.

## Adversarial Checks

- Parsed both report contracts: all nine required headings in order, valid
  unique target paths, ASCII text, ordered UTC timestamps matching filenames,
  final newlines and no trailing whitespace. Passed.
- Reparsed official ENVO revision a2455d1a77e46bb8a664d65a157166b539269042:
  106,817 triples; Undersea feature has 59 narrow and ten related synonyms,
  zero exact/broad, and the stated hydrographic-feature parent. The wetland
  area and vegetated-area definitions and superclass chain also agree.
- Rechecked the extractor's score/direct/identifier ordering, untyped
  ontology synonym input, unconditional exact-synonym emission and exact-ID
  taxon-label lookup. These support the reports' maintained-owner analysis.
- CSV-aware source checks confirmed physical locators: PREGO habitats 191;
  taxa 3895-3919, including the unlabeled row at 3896; ontology terms 6639
  and 6697; ontology edges 4734, 4822 and 5696; GOLD paths 276, 1501 and
  1719. Ontology physical line 6697 is logical TSV row 6691, not vice versa.
- Confirmed PATHS entries 486 and 2997 and decision rows 966 and 1269.
  Fresh bounded searches of maintained curation, histories and research
  included hidden/ignored files. No target-owned authored definition or
  causal overlay was found on those surfaces; this is not a whole-disk claim.
- Reopened the primary PREGO paper, section 2.3, and the NCBI old-ID page.
  The paper supports annotation/abstract associations, not proof of direct
  isolation. NCBI resolves 1037355 to 879969. The report's full 25-ID efetch
  check is a prior receipt, not a new 25-ID check in this publication pass.
- Reopened both EPA vernal-pool accounts and the seasonal-pool manual.
  Sparse in-pool vegetation alone does not exclude surrounding forest
  cover. The finding remains an unsupported universal genus claim needing
  exact-source ITEM assessment, not demonstrated disjointness or a mandate
  to replace the genus from the label alone.
- Verified the reused baseline queue QC was successful on the exact
  de3b61e4a6610b56a775a21e0bd78a5e8b31feec commit. Fresh local full QC and
  PR checks were still running when this note was written; their eventual
  results belong in the PR receipt, not as a premature pass here.

Network restrictions initially blocked the ENVO and issue-history reads;
authorized retries succeeded. No source-access failure was used as negative
scientific evidence. No browser visual QA was needed for this Markdown-only
change, and no website/product regeneration was performed.

## Scientific Tracking

- [#1249](https://github.com/CultureBotAI/HabitatMech/issues/1249): shared
  ontology synonym-scope loss, with this target's 69 assertions as a witness.
- [#1584](https://github.com/CultureBotAI/HabitatMech/issues/1584): the missing
  PREGO taxon name and merged alias; requires versioned full-pool handling.
- [#1585](https://github.com/CultureBotAI/HabitatMech/issues/1585): freshwater
  Vernal pools source-parent scope assessment and guarded hierarchy repair.

All 652 pre-existing open/closed issue titles and bodies were searched before
filing; the shared #1249 body and its 31 returned comments were also checked.
Other issue comments were not exhaustively searched. Related record-specific
taxonomy and wetland issues are not fixes for these exact witnesses.

Only the publication-label issue is resolved by this note. Generated records,
inputs, code, site, and prior history/reports are unchanged. There is no
SSSOM/KGX readiness claim, no closure of shared scientific issues, and no
change to the separate draft #1218 or the full-corpus review objective.
