# YAML Record Review: Amniotic fluid

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/amniotic_fluid__ff65cb2e.yaml`
- Started UTC: 2026-10-04T00:03:20Z
- Finished UTC: 2026-10-04T00:04:48Z
- Verdict: needs curation

## Target

Read the complete generated HabitatRecord for `habitatmech:GOLD.73051a70cb`,
Amniotic fluid: HOST_ASSOCIATED, NARROW, SEEDED. It contains two parents,
one GOLD attestation with three ORGANISM assertions and one seed event.
This is the Mammals: Human > Fetus > Amniotic sac path, not the mammal
fluid record or the PREGO/BTO fluid record. `data/habitats/PATHS.tsv:2139`
pins the stem, and the actual repository `mint` function reproduces the ID.

## Validation

- `just validate data/habitats/host_associated/amniotic_fluid__ff65cb2e.yaml`:
  passed, no issues.
- `just validate-strict data/habitats/host_associated/amniotic_fluid__ff65cb2e.yaml`:
  one file, zero errors.
- Fresh batch `just validate-products`: passed, 1,179 canonical pairs,
  one synonym, five configured exceptions and 2,054 no-adapter skips.
- Current official OLS term/typed-graph responses and the CDC glossary were
  inspected. The IUPAC sac page returned a challenge and its amnion page
  returned 403; their search snippets are not used as inspected evidence.
- Batch full QC is running. Unchanged scientific baseline `6cd30f38c` passed
  head and queue full QC in #1317, with 457 tests passed, three skipped and
  two dependency warnings. Final branch receipts must be recorded separately.

## Identity and Grounding

[UBERON:0000173, amniotic fluid](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0000173)
is non-obsolete and agrees with `data/raw/ontology_terms.tsv:12922`. Human
amniotic fluid is compatible with that broader fluid identity. The two GOLD
fluid leaves tie at depth five, so `leaf_claimants`/`resolve_gold` preserves
minted identities and supplies the fluid term as a parent. NARROW reflects
that automatic anti-conflation rule, not an item-level judgment of how host
qualification should affect identity. No target ITEM decision was found.

The second parent, `habitatmech:GOLD.433d96f0dd`, is the complete referenced
`amniotic_sac.yaml` record, an ungrounded human Amniotic sac. Its class-sweep
decision at `curation/decisions.tsv:456` does not define the sac as fluid.
The second GOLD pass at `src/habitatmech/seed.py:898-907` turns its path
container into a strictly-broader parent of the contained material.

Current OLS separates the [amnion membrane](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0000305)
from the [amniotic cavity](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0000301).
Both terms are non-obsolete. The typed fluid graph gives located-in amnion
(`RO:0001025`) and the inverse cavity location-of fluid (`RO:0001015`),
whereas its subclass parent is organism substance (`UBERON:0000463`), also
recorded at `ontology_subclass_edges.tsv:11034`. Location is not subclass.

The inspected [CDC glossary](https://archive.cdc.gov/www_cdc_gov/ncbddd/birthdefects/surveillancemanual/resource-library/glossary.html)
describes amnion/chorion as membranes but also uses amniotic cavity or sac for
the fluid-filled space. This terminology requires care in the separate sac
review. It does not undermine the present finding: neither a containing
membrane nor its cavity is a superclass of the liquid it contains.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:757` supplies node `gold.ecosystem:6329`,
the exact human path, one source node, three organisms and zero study/sample
assertions in that inventory. The emitted source node, label, path, count and
ORGANISM unit match. Three organism assertions do not establish three samples,
specific taxa, normal colonization or collection methods.

Full structured amniotic scans covered 2,562 original GOLD path rows,
1,040 bulk-count rows, 4,587 study rows and 1,587 triad rows. The latter
three tables had no amniotic rows. No current study page or sample membership
is therefore claimed. Counts from the mammal source are not added here.

The separate PREGO fluid row at `prego_habitats.tsv:529`, its retained taxon
row at `prego_habitat_taxa.tsv:36`, and the BacDive mapping at
`isolation_source_groundings.tsv:14` are nearby source concepts, not emitted
attestations or taxa of this GOLD-only target. Direct ontology leaf matching
precedes the independent mapping fallback.

## Completeness

Ignored-inclusive exact source-key, stem, label, node and path searches
covered curation, history, research, prior reviews, raw inventories, PATHS
and RETIRED. No target decision, authored definition, overlay, session record
or earlier exact-target review was found. Earlier amniotic-cavity and PREGO
fluid reports identify this record as a follow-up, not a completed review.

Full scans of 719 PREGO habitats, 8,807 taxon rows, 770 parameter rows,
358 mapping rows and 58 Madin rows located only the neighboring PREGO/mapping
support noted above; no amniotic-fluid parameter or Madin match occurred.
Optional absent fields are not automatic defects. iModulonDB is not
applicable because no gene, regulator or expression claim is asserted.

## Findings

1. **Major - HM-AMNIOTIC-FLUID-HUMAN-001:** contained amniotic fluid is
   represented as a subtype of its sac. Maintained owner: the GOLD
   source-parent pass at `src/habitatmech/seed.py:898-907` or a governed
   source-specific exclusion consumed there. This separately inspected
   witness is tracked in [#1318](https://github.com/CultureBotAI/HabitatMech/issues/1318).

No blocker or minor finding established. Fluid identity, category and source
copying remain supported; the sac's own grounding is a separate review.

## Recommended Edits

Exclude the fluid-to-sac is-a contribution while preserving the full source
path, the valid fluid parent and the three-organism provenance. Do not encode
containment as an equivalent xref. Review exact versus human-qualified fluid
identity explicitly before merging sources or changing NARROW to EXACT.

Keep the mammal and PREGO witnesses separate until their own identity and
source scope are compared. Use maintained inputs, not generated YAML; draft
#1218's exclusion mechanism is not yet on main. Append session history,
inspect a canary, compare semantic inputs and regenerate map/site through
the supported runtime where required (#1217). Preserve published URLs if
an identity change moves the output.

## Follow-up Checks

Regress this human edge independently of the mammal fetal-tissue edge.
Verify source IDs, host contexts, count units, valid parents and status after
seeding. Require strict validation, ontology correspondence, history, corpus
reproduction, genuine map/site freshness, redirects when needed and full QC.
Any new occurrence claim needs source evidence beyond a source-vocabulary count.

## Additional Notes

All 477 existing issues and returned comments were searched for the IDs and
amniotic wording. #1318 already owns the source-parent mechanism; its title
was broadened and this second witness added instead of filing a duplicate.
No generated record, scientific input or history was edited. No paid research
ran. No healthy prenatal microbiome, sterility or tissue-isolation claim is made.
