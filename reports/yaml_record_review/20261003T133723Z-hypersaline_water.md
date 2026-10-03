# YAML Record Review: hypersaline water

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/hypersaline_water.yaml`
- Started UTC: 2026-10-03T13:33:46Z
- Finished UTC: 2026-10-03T13:37:23Z
- Verdict: needs curation

## Target

Read the entire generated `HabitatRecord`, `ENVO:00002012`, hypersaline water,
`AQUATIC`, `EXACT`, `SEEDED`: definition, synonym, one parent, three source
attestations, eight qualitative parameters, 38 displayed taxa, a five-node,
four-edge osmoadaptation graph, and two history events. Read its complete
maintained overlay `curation/causal_graphs/hypersaline_water.yaml`.
`PATHS.tsv:618` locks the stem. The adjacent water-environment record is a
different entity class, not an alias of this material.

## Validation

- `just validate data/habitats/aquatic/hypersaline_water.yaml`: pass.
- `just validate-strict data/habitats/aquatic/hypersaline_water.yaml`:
  one record, zero errors.
- `just validate-causal curation/causal_graphs/hypersaline_water.yaml`: pass.
- Current OLS checks verified the active water term and saline-water parent.
- NCBI Taxonomy EFetch returned all 38 requested taxa, including two redirected
  IDs. Every emitted primary-source taxon label, rank, and score was compared
  with the complete matching source rows.
- Both cited PMIDs and the counterevidence PMID were verified using structured
  Europe PMC title/DOI/abstract responses; no snippet mismatch was found.
- Full corpus/schema/history/site QC is successful at unchanged base
  `ce53c21e8be841478dfdc730cef28ad2ca4bf462`,
  [run 37125963812](https://github.com/CultureBotAI/HabitatMech/actions/runs/37125963812).
  This reuses baseline gates, not a fresh full suite for this report.
- The shared source CLI initially failed in HabitatMech's environment because
  `dotenv` was missing. Retrying with the claw checkout's own interpreter
  succeeded and enumerated 28 iModulonDB datasets. No dataset matched the
  record's named taxa; genus-only Bacillus/Pseudomonas similarities do not
  identify a matching species or strain. No component is claimed as evidence.

## Identity and Grounding

The material definition and exact self-groundings agree. Active
`ENVO:00002010` saline water is the direct parent in both the vendored edge
and live ontology. The environment, lake, and brine classes are not exact
replacements.
[Hypersaline water](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002012),
[saline water](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002010).

Recomputed source keys are `habitatmech:PREGO.8ebf6af96a`,
`habitatmech:MADIN.c1fd482c68`, and
`habitatmech:ENVIRONMENTS_TABLE.ad612431da`. Ignored-inclusive searches found
no ITEM decisions for them; the graph event does not make all contributing
source identities reviewed, so `SEEDED` is correct.

## Evidence

| Claim | Verification |
|---|---|
| MADIN attestation | `madin_habitats.tsv:17` supplies 416 TAXON associations, not 416 isolates. The raw selected-taxon table retains 25 candidates; one is also in PREGO, leaving 24 MADIN-primary displayed entries. |
| PREGO attestation | `prego_habitats.tsv:315` supplies 14 taxa, maximum score 3, both stated channels, and the related plural synonym. The 14 selected rows preserve rank, score, and source labels. |
| Corroboration | `NCBITaxon:31910` occurs in both source tables; its PREGO-primary displayed entry carries MADIN corroboration. Promotion in display order does not change its source rank of five. |
| Parameters | `environment_parameters.tsv:270-277` supplies exactly eight single-term `water_hypersaline` rows. Nine sediment-plus-water rows are correctly excluded. These are source qualitative bands, not universal quantitative laws. Low available water and permanently wet are different axes. |
| Osmotic alternatives | The three snippets from PMID:29529204 are exact abstract substrings. The source describes KCl accumulation and compatible solutes as alternative strategies, not requirements of every listed taxon. |
| Acidic proteome | PMID:18412960 supports the older generalization quoted by the graph, but primary genomic analysis PMID:22527048 provides important counterevidence to a universal requirement. |

[Gunde-Cimerman et al., PMID:29529204](https://europepmc.org/article/MED/29529204),
[Oren, PMID:18412960](https://europepmc.org/article/MED/18412960),
[Elevi Bardavid and Oren, PMID:22527048](https://europepmc.org/article/MED/22527048).

The latter study examined three Halanaerobiales genomes and did not find the
predicted excess of acidic residues. It explains how earlier bulk hydrolysis
measurements could create that impression. This is a scoped exception, not
evidence against acidic proteomes in all salt-in organisms.

NCBI EFetch resolves `230105 -> 40223` (Methylophaga thalassica) and
`158080 -> 141390` (Chromohalobacter israelensis); the source rows and emitted
entries lack names. Unlabeled `48547` resolves to Ophiura at genus rank. This
observational PREGO association is not a microbial-trait or characteristic
claim and should not be silently relabeled as a bacterium or deleted.
[40223](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=40223),
[141390](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=141390),
[48547](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=48547).

Other current-name differences include `1069073` Haloechinothrix halophila,
`1114856` Natronorubrum tibetense GA33, `1121087` Alkalicoccus chagannorensis
DSM 18086, `1121317` Maledivibacter halophilus DSM 5387, and `1121463`
Desulfobaculum senezii DSM 8436. The Madin spellings `thialkalivibrio_nitratis`
and `thialkalivibrio_denitrificans` refer to current Thioalkalivibrio names.
These are source-label/reference maintenance concerns, not proof of different
habitat associations.

## Completeness

Ignored-inclusive searches of curation, history, research, configuration,
source inventories, path lock, and review reports covered ID, label, stem,
graph name, citations, and all three source keys. They found the graph overlay
and incidental neighboring mentions but no target term request, standalone
session history, or prior exact-target report. The existing graph event is
present in the generated record; append standalone history during any fix.

`conf/id_label_targets.yaml` explicitly excludes source taxon labels from the
blocking OAK gate. Passing it cannot disprove the taxonomy maintenance finding.
All taxon entries are observational under the schema; none claims
`is_characteristic`. iModulonDB absence is not negative biological evidence.

## Findings

1. **Major: universal acidic-proteome dependency is over-scoped.**
   `salt_in_requires_acidic_proteome` asserts necessity for the entire salt-in
   strategy, while PMID:22527048 reports exceptions. Owner:
   `curation/causal_graphs/hypersaline_water.yaml`. Preserve the supported
   requirement for intracellular machinery compatible with high salt, or
   explicitly scope any acidity association; do not erase the conflicting
   evidence or attach it to all 38 taxa.
2. **Minor: the first edge's polarity is malformed.** High salinity `lowers`
   a node already labeled low water activity. The intended effect is to
   promote that low-activity condition, not lower it. Owner: the same overlay.
3. **Minor: source taxonomy maintenance is incomplete.** Two redirected IDs,
   three missing labels, and several dated source names reduce reference
   clarity. Owner: the source-label/alias extraction in
   `src/habitatmech/extract.py` and governed PREGO/Madin snapshots. Investigate
   the Ophiura association at its source rather than guessing a replacement.

Zero blockers, one major finding, two minor findings.

## Recommended Edits

Correct the two graph issues in the maintained overlay, retain exact bounded
evidence, add regressions and append-only history, then regenerate the target
and its page. Separately refresh taxonomy with versioned alias provenance,
preserving original source IDs, ranks, scores, pools, and corroboration; test
deduplication if an alias and replacement coexist. Never patch generated taxa
or silently reinterpret quoted source names as curator-authored taxonomy.

## Follow-up Checks

Validate the overlay, dry-run and canary the seeder, inspect every graph edge
and evidence item, run strict validation and corpus reproduction, regenerate
site output, and pass full QC. Check semantic-map input fingerprints; taxonomy
label changes may require a map rebuild even though a graph-only fix does not.
Verify current taxonomy aliases and snapshot manifests before any source fix.

## Additional Notes

This is the pre-fix review. No record, source inventory, graph, history, or
generated page was modified. All 416 returned open/closed issues were searched
for the target, graph, and affected taxon IDs; only a different PREGO alias
case (#1237) was found, not an existing issue for these exact findings.
