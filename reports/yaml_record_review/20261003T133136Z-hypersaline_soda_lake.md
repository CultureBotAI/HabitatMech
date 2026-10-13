# YAML Record Review: Hypersaline soda lake

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/hypersaline_soda_lake.yaml`
- Started UTC: 2026-10-03T13:30:14Z
- Finished UTC: 2026-10-03T13:31:36Z
- Verdict: pass

## Target

Read the complete generated `HabitatRecord`: `habitatmech:GOLD.3098ee8fe8`,
Hypersaline soda lake, `AQUATIC`, `UNGROUNDED`, `SEEDED`. It has one parent,
one GOLD attestation, and two history events. There is no authored definition,
taxon, parameter, literature citation, or mechanism claim. `PATHS.tsv:1646`
locks the filename. The spring, plain hypersaline lake, soda lake, brine, and
sediment descendants are different concepts.

## Validation

- `just validate data/habitats/aquatic/hypersaline_soda_lake.yaml`: pass.
- `just validate-strict data/habitats/aquatic/hypersaline_soda_lake.yaml`:
  one record, zero errors.
- `habitatmech.seed.mint` reproduces `habitatmech:GOLD.3098ee8fe8` from the
  exact GOLD path.
- Structured current OLS term and search responses were inspected for the
  two plausible lake candidates and saline lake.
- Full QC on the unchanged corpus at base
  `ce53c21e8be841478dfdc730cef28ad2ca4bf462` is verified successful in
  [merge-group run 37125963812](https://github.com/CultureBotAI/HabitatMech/actions/runs/37125963812).
  It covers corpus/schema/history/site gates; this is baseline reuse, not a
  claim of a fresh full suite for this one read-only review.

## Identity and Grounding

The source leaf denotes a lake combining hypersalinity with soda chemistry,
not a salt quality or an isolated water sample. Current active
`ENVO:00002121` is **alkaline salt lake**, with soda lake as a synonym;
`ENVO:01001020` is **hypersaline lake**. The first does not require
hypersalinity and the second does not require soda chemistry. Both are useful
broader candidates, not exact substitutes for this combined source concept.
Current ENVO search for the complete label returned alkaline salt lake,
not an exact-label class. This bounded search does not establish absence from
every ontology.
[Alkaline salt lake](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002121),
[hypersaline lake](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001020).

The maintained parent `habitatmech:GOLD.ce244e62cd` is inland saline **or**
alkaline aquatic environment, defined in `curation/term_requests.tsv:43`.
The full parent was inspected: its disjunction accommodates the combined
lake rather than requiring an unrelated chemical identity. The GOLD
parent-path pass owns this source-derived edge; it is not an ENVO assertion.

`curation/decisions.tsv:366` is explicitly `CLASS`, not `ITEM`, and says that
habitathood was not assessed in that sweep. `SEEDED` and the explanatory
history accurately preserve that limitation. This review supports habitat
meaning but does not silently promote the maintained decision or status.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:358` supplies the exact path
`Environmental > Aquatic > Non-marine Saline and Alkaline > Hypersaline soda lake`,
29 ORGANISM assertions, and nodes `gold.ecosystem:7884|gold.ecosystem:7885`.
The first-node display and two-node note are faithful. Separate sediment and
mat descendants have their own counts and are not added to 29.

An inspected primary study describes carbonate-rich alkaline hypersaline
brines and samples four Kulunda settings. It supports the combined habitat
meaning, not a crosswalk between those samples and these 29 GOLD organisms.
Its measured values and microbial communities must not be generalized into
this unqualified source record.
[Vavourakis et al., 2016, abstract and site description](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2016.00211/full).

Complete structured exact-path scans found zero rows in the committed
GOLD biosample, triad, and study crosswalks. That is snapshot coverage, not
proof that the habitat has no sampled organisms or studies.

## Completeness

Ignored-inclusive searches covered ID, label, and stem in curation, history,
research, configuration, path lock, raw inventories, and review reports.
They found the CLASS decision and incidental parent research, but no target
definition, overlay, session history, PREGO/Madin/parameter association, or
prior exact-target review. The parent's research is a lead, not independent
evidence or an extra source attestation.

An ITEM decision and definition would improve the record but are not required
to make its present explicitly seeded claims truthful. Optional taxa,
numeric pH/salinity, and mechanisms are correctly not inferred from neighboring
records or literature examples. iModulonDB is not applicable: this record
names no organism-specific gene, pathway, regulator, or expression claim.

## Findings

None found. Zero blockers, major findings, or minor findings. The pass is
bounded to the represented source and hierarchy claims, not all underlying
GOLD submissions or a completed ontology term request.

## Recommended Edits

None required for the current seeded representation. A later ITEM assessment
may define the combined lake and evaluate both broader-class candidates
through `curation/decisions.tsv` and `curation/term_requests.tsv`; do not
replace its identity with either broader class merely to obtain a grounding.

## Follow-up Checks

For actual curation, verify candidate scope and source nodes again, append
history, canary the seeder, and run strict validation, corpus reproduction,
ontology-product checks when applicable, semantic-map/site freshness, and
full QC. Do not hand-edit generated YAML or borrow a sibling's sample counts.

## Additional Notes

No corpus, maintained input, generated product, history, or older report was
changed. The current record remains `SEEDED`; the read-only pass is not an
ITEM curation event.
