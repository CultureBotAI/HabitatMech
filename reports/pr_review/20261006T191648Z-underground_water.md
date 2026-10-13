# Underground Water Publication Review

- PR: [#1578](https://github.com/CultureBotAI/HabitatMech/pull/1578)
- Reviewed head: `d65c85fa32ec4c4052169584f27b89dd63276be0`
- Evidence checked UTC: 2026-10-06T19:16:48Z
- Original: [Underground water record review](../yaml_record_review/20261006T190411Z-underground_water.md)

This is an append-only publication correction, not another completed record
review or a scientific curation. The original timestamped report is unchanged.

## Corrections

1. **Minor, source locator ([#1579](https://github.com/CultureBotAI/HabitatMech/issues/1579)).**
   The original `ontology_terms.tsv:7477` is logical TSV row 7477 including
   the header. The correct physical file locator is
   `data/raw/ontology_terms.tsv:7483`; quoted multiline fields explain the
   difference. Use the stable key `ENVO:00005792` to identify the row. The
   definition, synonym text and scientific finding are unchanged.
2. **Minor, primary-source inconsistency ([#1580](https://github.com/CultureBotAI/HabitatMech/issues/1580)).**
   The [PREGO paper](https://imbbc.hcmr.gr/wp-content/uploads/2022/03/2022-Zafeiropoulos-Micro-12.pdf)
   gives an environmental-samples range of `(0,5]` in section 2.4, but
   Appendix C.3 explicitly caps its formula at four. The original report's
   cap-four statement should be read as attributed specifically to Appendix
   C.3, not as agreement between both sections or independent verification of
   the deployed implementation. The stored maximum 1.33759 is compatible with
   either range. Neither establishes a probability or ecological prevalence;
   no source score or taxon assertion is changed.

## Adversarial Checks

- Read the complete report and the complete generated Underground water YAML.
- Rechecked physical source locators with ignored-inclusive `rg`: PREGO
  habitat line 75, retained-taxon lines 6998-7022, ontology superclass line
  5606, groundwater-child line 6799, GOLD medium-triad lines 199 and 280, and
  PATHS line 736 all match the original report.
- Inspected `extract_prego` and `ConceptStore.get`: ranking and count semantics
  match the report; untyped ontology synonyms are still promoted to exact.
- Reparsed the cited [official ENVO snapshot](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl):
  the target, liquid water, groundwater and underground water body are active;
  the target's direct parent and related synonym agree with the report.
- Repeated ignored-inclusive searches across curation, history, research,
  conf, docs, src, tests, PATHS, RETIRED and the research manifest for the ID,
  mint, label, slug and subterranean-water wording. Only PATHS matched;
  bytecode was excluded. This is a bounded maintained-surface search, not an
  assertion that no external source exists.
- Inspected the paper's environmental-samples methods and scoring appendix.
  Original sample keys and the deployed scoring implementation remain
  unverified. The report correctly avoids characteristic-presence claims.

## Remaining Scientific Work

- [#1249](https://github.com/CultureBotAI/HabitatMech/issues/1249) remains open.
  The new witness was added there; correcting this report does not repair the
  governed typed-synonym extraction and emission contract.
- [#1581](https://github.com/CultureBotAI/HabitatMech/issues/1581) tracks the
  process-location wording ambiguity. [Upstream discussion](https://github.com/EnvironmentOntology/envo/issues/523#issuecomment-314476415)
  supports broader underground water versus narrower groundwater, but does
  not resolve the crust/surface wording. No unsupported definition replacement
  or identity change is warranted. The [legacy groundwater issue](https://github.com/EnvironmentOntology/envo/issues/924)
  concerns a different identifier.

The two publication findings are addressed by this note. The original
scientific verdict remains needs curation, with one major and one minor
finding. Full local and hosted QC receipts belong to the PR and are not
claimed complete by this timestamped note. No SSSOM/KGX readiness or
full-corpus completion is implied.
