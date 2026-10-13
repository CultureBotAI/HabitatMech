# YAML Record Review: swamp ecosystem

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/swamp_ecosystem.yaml`
- Started UTC: 2026-10-06T15:27:57Z
- Finished UTC: 2026-10-06T15:31:06Z
- Verdict: needs curation; 0 blocker, 2 major, 0 minor findings.

## Target

The entire generated HabitatRecord was read. ENVO:00000233 swamp ecosystem
is AQUATIC/EXACT/REVIEWED, with an ENVO definition, ten scoped/source-tagged
synonyms, two parents, three source attestations, 26 taxa and four events.
PATHS.tsv:531 pins this target. Baseline:
4157ac2b3935aa8a5ab6d018df5acc15fd5214b6. This is an ecosystem record, not
the wetland area that overlaps it or a universal freshwater-only class.

## Validation

- `just validate data/habitats/aquatic/swamp_ecosystem.yaml`: pass.
- `just validate-strict data/habitats/aquatic/swamp_ecosystem.yaml`: pass,
  one file and zero errors.
- Full actual build_corpus/build_document equality: pass, three contributing
  sources, three ITEM-reviewed sources, 26 taxa and four events.
- Executed default/applied GOLD child/parent, BacDive and PREGO resolutions;
  inspected rendered HTML text and actual semantic-text counterfactual.
- Same-day shared gates on this identical scientific baseline passed:
  `just verify-corpus --max-diffs 1` (3,206 exact records),
  `just validate-history` (95), `just validate-causal-all` (32),
  `just term-requests-check` (109), `just provenance-check` (14 inventories,
  two GOLD sources), `just worklist --limit 3`, and `just report`.
- Shared `just validate-products`: pass, 1,179 canonical, one synonym,
  five exceptions and 2,054 configured no-adapter skips. This checks label
  correspondence, not synonym scope or ecosystem/area subsumption.
- `git diff HEAD --exit-code` over guidance, code, curation, raw data,
  generated corpus/site, history and README confirmed unchanged baseline.
- Official NCBI taxonomy batch: all 26 IDs returned unchanged and all supplied
  names agree. Full tests/QC and browser visual QA were not rerun for reports.
  No standalone citation validator is exposed for a record without citations
  or mechanism edges; source and identifier checks were performed directly.

## Identity and Grounding

The actual source keys and decisions are:

| Source key | Maintained decision row | Actual resolution |
| --- | --- | --- |
| BACDIVE.278819888e | decisions.tsv:18, ITEM REVIEW | bacdive_mapping_table, CLOSE/skos:closeMatch |
| GOLD.0f3918255c | decisions.tsv:184, ITEM REVIEW | gold_leaf_synonym, CLOSE/skos:closeMatch |
| PREGO.738ced258a | decisions.tsv:1463, ITEM REVIEW | prego_self_grounded, EXACT, predicate omitted |

All land on ENVO:00000233. PREGO supplies the exact ontology identity;
record-level EXACT must not be read as upgrading the other two mappings.
Three ITEM decisions explain REVIEWED and the three August 13 events, followed
by the August 16 seed event. These are existing attributions, not new sign-off.

Vendored ontology_terms.tsv:6822 and current official
[ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
agree on the term, definition and genuine named parent ENVO:01001209 wetland
ecosystem. The other emitted parent, ENVO:00000043 wetland area, denotes a
vegetated area overlapping a wetland ecosystem. All three classes are active.
An overlapping area is not the ecosystem's strict superclass.

The extra area parent comes from the exact GOLD path Environmental > Aquatic
> Freshwater > Wetlands > Swamp. Its immediate Wetlands source is automatically
unmatched but an ITEM GROUND resolves GOLD.a981586d10 to ENVO:00000043. The
independent path-parent pass then attaches the area to this ecosystem. The
complete wetland_area.yaml was read as context, not inherited evidence.

Current typed ENVO synonyms versus emitted scopes:

| Text | ENVO scope | Generated scope |
| --- | --- | --- |
| Swamp; swamp | exact | exact |
| wetland | broad | exact |
| cienaga | related | exact |

extract.py:_load_tsv_ontology retains an untyped synonym pipe, and
seed.py:ConceptStore.get promotes every ontology synonym to exact. The two
inflated scopes are a concrete witness of the shared issue, not evidence that
all aliases are wrong. PREGO's five related variants remain correctly related.
The separate BacDive alias retains source provenance; its exact alias scope
deserves review alongside the explicitly CLOSE source mapping, not a forced
upgrade of that mapping.

## Evidence

Structured exact key/path/node and label searches covered all 14 raw TSVs:

- bacdive_isolation_sources.tsv:59 gives 171 STRAIN and 149 taxa for
  Wetland-Swamp. The 25 retained rows at bacdive_source_taxa.tsv:3024-3048
  reproduce their strain counts, ranks and pool of 149; no characteristic flag.
- gold_ecosystem_paths.tsv:565 gives gold.ecosystem:4182, eight ORGANISM
  assertions and zero KGX study/biosample counters. The separate bulk row
  gold_path_biosamples.tsv:792 has four biosamples. These units are not summed.
- prego_habitats.tsv:675 gives one TAXON, one direct assertion, score four,
  annotated_genomes_isolates channel. prego_habitat_taxa.tsv:4359 supplies
  Trichococcus palustris, rank/pool 1/1 and BacDive corroboration. The generated
  record preserves this observational source claim, not ecological typicality.

Exact GOLD triad rows 431-433 describe one sample/one study: freshwater lake
biome ENVO:01000252, freshwater lake ENVO:00000021 and lake water ENVO:04000007,
each with top share 1.00. These are contextual roles, not a reason to replace
swamp identity. The other swamp-ID hit at triad row 882 belongs to a terrestrial
sediment-core path and is not this source's triad.

Study memberships are Gs0114588 at row 844 (ten paths) and Gs0150547 at row
3363 (two paths). Both live study URLs were inaccessible through the web tool.
No whole-study sample/taxon crosswalk or independent replication is claimed.
The source mapping row at isolation_source_groundings.tsv:346 independently
records the BacDive close match; it is not an exact-equivalence assertion.

The official
[NCBI taxonomy batch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=140314,184914,54,83428,150053,2,382514,83453,1267,56,1066,1069,1069475,1082,1108595,1117702,1117703,1118379,1121022,1121291,1121343,1122133,1122612,1122928,1122946,1123043&retmode=xml)
verified every taxon ID/name. The list mixes taxonomic ranks; its rank field
is source ranking, not taxonomic rank, and 26 entries are not 26 species.
[BacDive 2282](https://bacdive.dsmz.de/strain/2282) and
[DSMZ DSM 9172](https://www.dsmz.de/collection/catalogue/details/culture/DSM-9172)
were inspected in identity/isolation fields: both link Trichococcus palustris
Z-7189 to a swamp isolate near Abramtsevo. BacDive identifies NCBITaxon:140314
and the Wetland (Swamp) category. This supports the bounded association, not
that all source taxa typify swamps. These linked catalogue accounts are not
independent ecological experiments, nor a reconstruction of all 171 strains.

[EPA's classification](https://www.epa.gov/wetlands/classification-and-types-wetlands),
Description of Swamps, distinguishes woody-plant wetlands and permits seasonal
standing water. This is broader in hydroperiod than ENVO's permanent-inundation
definition. Preserve the source-scope disagreement for ontology/source review;
do not silently rewrite the ENVO definition or infer universal hydroperiod,
vegetation, salinity or methane-production parameters for every source member.

The full rendered text faithfully distinguishes source units and associated
versus characteristic taxa; it explicitly shows 25 of 26 kept associations.
It nevertheless repeats wetland area as a broader habitat. Removing just that
parent in memory changes actual semantic text; no product was edited.

## Completeness

Ignored/hidden-inclusive identity, three source keys, label/stem searches
covered curation, history, research, reports/manifest, conf, docs, src, tests,
PATHS and RETIRED. They found the three ITEM rows and contextual research,
but no target definition overlay, causal overlay or parent exclusion in those
scopes. Broad label hits in other records were not treated as target support.
No parameter or MADIN contribution was found in the structured raw scan.

Empty optional measurements, literature evidence, datasets, discussions and
mechanisms are not additional defects. iModulonDB is not applicable: taxon
occurrence and strain identifiers do not themselves assert a gene, regulator,
pathway or expression module requiring that adapter.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | GOLD's wetland-area context becomes an is-a parent of a swamp ecosystem. | curation/gold_parent_exclusions.tsv, exact GOLD.0f3918255c/path/ENVO:00000043 contribution. |
| Major | ENVO's broad wetland and related cienaga synonyms are promoted to exact. | Governed ontology/extraction input, src/habitatmech/extract.py and seed.py; shared #1249. |

No blocker or minor finding was established. Source hydroperiod/scope questions
and access limits are retained uncertainties, not additional counted defects.

## Recommended Edits

1. Exclude only the exact GOLD area-parent contribution, preserving the genuine
   wetland-ecosystem genus and every source's identity, predicate, count/unit,
   rank/pool, corroboration and prior attribution. No authored definition is
   necessary merely to suppress this edge.
2. Recover typed synonym scopes through governed extraction and emit the two
   verified weaker scopes. Preserve genuinely exact ENVO synonyms and source
   provenance; do not globally downgrade or hand-edit generated YAML.
3. Reassess source-class hydroperiod and the BacDive label's scope when source
   evidence is available. Keep the current close-match qualifications until
   an explicit ITEM judgement justifies anything stronger.

## Follow-up Checks

Add exact-parent and mixed-synonym-scope regressions. Dry-seed, inspect the
exact canary, append required session history and run schema/strict, labels,
provenance, curation-floor, history, reproduction, site and full QC. The parent
change demonstrably affects semantic inputs and requires a real map rebuild.
Do not manufacture count equality across strains, organisms and taxa.

## Additional Notes

[Issue #1249](https://github.com/CultureBotAI/HabitatMech/issues/1249) was read
directly and remains OPEN; no comment or issue was created. Current typed
ENVO retrieval parsed 106,817 triples. No exhaustive GitHub deduplication,
full source-matrix re-extraction, paid research, scientific edit, status change
or new curation event occurred. These checks do not certify SSSOM/KGX products.
