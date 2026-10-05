# YAML Record Review: saline water body

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/saline_water_body.yaml`
- Started UTC: 2026-10-05T05:36:45Z
- Finished UTC: 2026-10-05T05:40:20Z
- Verdict: needs curation; 0 blocker, 2 major, 0 minor findings.

## Target

The complete generated HabitatRecord was read. ENVO:01001319 denotes a
saline water body, not saline water material or only inland saline settings.
The record is AQUATIC, CLOSE and REVIEWED, with an ENVO definition, two
synonyms, two parents, BACDIVE and GOLD attestations, 25 BacDive taxa and
three history events. Parameters, xrefs, curated evidence, graphs,
discussions and datasets are absent. PATHS.tsv:886 pins the stem.
No scientific input or generated artifact was edited.

## Validation

- `just validate data/habitats/aquatic/saline_water_body.yaml`: pass.
- `just validate-strict data/habitats/aquatic/saline_water_body.yaml`: pass,
  one file and zero errors.
- Complete build_corpus/build_document dictionary equality: pass; two
  source concepts, both ITEM-reviewed, 25 taxa and three events.
- Fresh `just validate-products`: pass, 1179 canonical, one synonym, five
  exceptions and 2054 no-adapter skips. Source attestations and taxa are
  explicitly outside the configured gate; a pass is not ecological validation.
- `just worklist --status all --limit 5`: pass, 953 ungrounded records and
  1810 decisions. The two exact source routes were separately executed.
- Fresh `just qc` is live during tests; lint, documentation and provenance
  passed. Log: /private/tmp/habitatmech-waterbody-crust-qc-20261005.log.
  Remaining gates and terminal success are not claimed here. Prior main-push
  QC 37267872835 is SUCCESS but is distinct from this fresh local run.
- Actual full-context semantic comparisons: removing the inland parent
  changes text; removing the GOLD source synonym also changes text; changing
  only that synonym's scope does not. No map/site or export was regenerated.

## Identity and Grounding

Current official [ENVO:01001319 saline water body](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001319)
is active, with the stored definition and a true named superclass,
[ENVO:00000063 water body](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000063).
Typed OWL distinguishes the water body from saline water through a primarily
composed-of restriction. Inventory rows are ontology_terms.tsv:8813 and
ontology_subclass_edges.tsv:7175. The typed exact synonym saline body of
water is correctly preserved and supplies no witness for #1249.

The complete second-parent record, habitatmech:GOLD.ce244e62cd, was read
as context only. Its authored definition at curation/term_requests.tsv:43
explicitly requires an inland water-determined environment and is disjunctive
between salinity and alkalinity. It is not a broader class of every saline
water body. Current typed ENVO and official OLS confirm ocean,
ENVO:00000015, as a marine subclass of saline water body; physical
ontology_subclass_edges.tsv:4643 records that relationship. The source-parent
pass incorrectly attaches an inland-only source context to the global
ontology class. Neither broadening the parent's definition nor deleting the
true water-body superclass is an appropriate repair for this edge.

The actual source keys are habitatmech:BACDIVE.1f236a4c29 and
habitatmech:GOLD.a5eb3e9d4f. ITEM REVIEW rows at decisions.tsv:16 and :952
endorse the automatic resolutions. Both actual routes take the maintained
mapping-table target ENVO:01001319 with CLOSE/skos:closeMatch; they are
curated_review_of_bacdive_mapping_table and
curated_review_of_gold_mapping_table, not exact lexical identity. The
source map at isolation_source_groundings.tsv:269 records Saline, medium
confidence, semapv:LexicalMatching and ols4_auto. Current REVIEWED status and
the two 2026-08-13 events faithfully represent those decisions, without
proving all source members are water bodies.

The terse source category Saline need not be a bare quality or non-habitat.
Equally, its close mapping does not license an exact synonym of the ontology
class. GOLD ingestion at seed.py:870 and BacDive ingestion at :948 both
request EXACT_SYNONYM for their source labels. Concept.add_synonym at
:364-367 retains the first source for the same spelling/scope, explaining
why only GOLD appears on the emitted Saline synonym. The absence of a second
BacDive synonym is not an omitted attestation; the unsupported exact scope
is the problem. Preserve both original source labels in their attestations.

## Evidence

Physical data/raw/bacdive_isolation_sources.tsv:21 records source
bacdive.isolation_source:saline, 899 STRAIN assertions and 795 candidate taxa.
The 25 retained rows at bacdive_source_taxa.tsv:2375-2399 agree with the YAML
names, ranks and association counts. Extraction follows source-to-strain and
strain-to-taxon links; the taxon tally counts distinct strain identifiers,
then sorts by decreasing count and ID before the 25-row cap. It is not a
PREGO confidence score, relative abundance or universal characteristic claim.
No corroborated_by or is_characteristic field is emitted.

All 25 current NCBI Taxonomy identifiers, names and ranks were inspected in
the primary EFetch response. Every stored name matches; no alias, missing
label or taxonomic correction was found:

| Source ID | Current name, matching stored label | Rank | Association count |
| --- | --- | --- | --- |
| 1570 | Halobacillus halophilus | species | 13 |
| 83428 | uncultured Bacillus sp. | species | 11 |
| 1872700 | Virgibacillus sp. | species | 7 |
| 2013 | Nocardiopsis | genus | 7 |
| 1871618 | Gracilibacillus sp. | species | 5 |
| 1931 | Streptomyces sp. | species | 5 |
| 195064 | Ectothiorhodospira mobilis | species | 4 |
| 2037 | Actinomycetales | order | 4 |
| 50741 | Marinobacter sp. | species | 4 |
| 54063 | Actinopolyspora sp. | species | 4 |
| 1057 | Thiococcus pfennigii | species | 3 |
| 1486246 | Halomonas sp. | species | 3 |
| 1874361 | Idiomarina sp. | species | 3 |
| 1898027 | Ornithinibacillus sp. | species | 3 |
| 1930901 | Spiribacter sp. | species | 3 |
| 2242 | Halobacterium salinarum | species | 3 |
| 268735 | Halonotius pteroides | species | 3 |
| 2746 | Halomonas elongata | species | 3 |
| 933063 | Dichotomicrobium thermohalophilum | species | 3 |
| 94136 | Alkalibacillus haloalkaliphilus | species | 3 |
| 1126236 | Halobellus inordinatus | species | 2 |
| 1186196 | Natrinema salaciae | species | 2 |
| 1329370 | Franzmannia qiaohouensis | species | 2 |
| 1505232 | Chitinivibrio alkaliphilus | species | 2 |
| 168379 | Halorhodospira neutriphila | species | 2 |

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1570,83428,1872700,2013,1871618,1931,195064,2037,50741,54063,1057,1486246,1874361,1898027,1930901,2242,268735,2746,933063,94136,1126236,1186196,1329370,1505232,168379)
confirms identity, not the original isolation site. Uncultured/species,
genus and order labels are retained as source granularity, not guessed
strain identities. An ignored-inclusive configured kg-microbe filename search
did not recover the original transformed BacDive nodes/edges. Older BacDive
notebooks/pickles are not demonstrated substitutes for the manifest's source
bytes. The original 899-strain chain and the full 795-taxon pool remain
unrecovered, so source-category membership is not point-level validation of
every water-body assertion.

Physical gold_ecosystem_paths.tsv:150 contains
Environmental > Aquatic > Non-marine Saline and Alkaline > Saline, depth four,
nodes 3753 and 3973, 150 ORGANISM assertions and zero tree study/biosample
counts. The collapse note and displayed first node are faithful. Current
official [GOLD 3973](https://www.ebi.ac.uk/ols4/api/ontologies/gold/terms/https%253A%252F%252Fw3id.org%252Fgold.path%252F3973)
is active with the complete path and a partial broad aquatic-biome annotation;
3753 returned 404, not proven retirement.

The complete 14-table exact GOLD-path/node scan separately found 899 bulk
biosamples at gold_path_biosamples.tsv:37. API triad rows 719-721 describe
893 complete-triad samples in 25 studies: broad aquatic biome, share 1.00;
local saline lake, share 0.82 among ten terms, six studies agreeing; medium
saline water, share 0.84 among seven terms, 18 studies agreeing. Local water
body and sampled material are different roles. Neither a modal triad nor
the equal numerical value 899 makes these GOLD samples the BacDive strains.
No inspected crosswalk establishes that the API cohort is a specific subset
of the bulk count, and none should be summed with 150 organisms.

There are 28 exact study memberships in the committed table, not the
25-study triad cohort. Three original single-path study requests,
Gs0060782, Gs0060788 and Gs0111411, returned 403; the other original study
pages were not individually fetched. Membership counts are verified from
the table, but study contents and sample-level ecological support remain
unrecovered. No exact parameter or PREGO/Madin source contribution was found.

The entire rendered page was inspected. Counts/units, 25-of-795 ranking,
observational wording and review events agree. It also exposes the false
inland broader link and bare Saline under Also called. Rendering is not an
independent source validating either claim.

## Completeness

Ignored/hidden-inclusive ID, both source keys, label and stem searches covered
curation, conf, history, research, prior reports, inventories, PATHS and
RETIRED. Both decisions and the path lock exist; no target-owned definition,
causal overlay, separate session history or prior individual target report
was found. Other records' references to this class are not reviews of it.
No new authored definition belongs on this ontology-owned identity.

Empty mechanism, numerical parameter and dataset slots are appropriate
without direct support. iModulonDB is not applicable: there are no gene,
regulator or expression claims. Source-mapping evidence remains incomplete;
do not infer a false taxon association merely because its original chain is
unavailable, or infer universal habitat membership from taxonomy identity.

## Findings

| Severity | Finding | Maintained owner / scope |
| --- | --- | --- |
| Major | An inland-only environment is emitted as a strict broader class of global saline water body, including its marine subclasses. | Exact GOLD.a5eb3e9d4f source-parent contribution in `src/habitatmech/seed.py`; preserve ENVO:00000063. |
| Major | The close-mapped, context-qualified source label Saline is unconditionally promoted to an exact synonym of the ontology identity. | GOLD and BacDive source-label ingestion plus Concept.add_synonym in `src/habitatmech/seed.py`; source decisions/mapping evidence govern any justified stronger equivalence. |

No blocker or minor finding was established. The ontology identity and
definition, actual close-match status, true water-body parent, count units,
taxon names and mechanical review-history derivation are supported. The
original source mapping needs evidence review, not an invented replacement.

## Recommended Edits

1. Remove only the false inland source-parent edge through maintained,
   source-specific machinery. Do not redefine all saline water bodies as
   inland, weaken the parent's definition or remove the true ontology parent.
2. Preserve source labels as provenance without asserting exact equivalence
   solely because ingestion encountered them. Use a justified weaker synonym
   scope or attestation-only representation for this close-mapped label;
   preserve the verified exact ENVO synonym and genuinely exact controls.
   This is distinct from #1249's loss of typed ontology synonym scope.
3. Reassess both maintained ITEM REVIEW decisions against original
   source-category/strain/sample evidence before strengthening or splitting
   mappings. Do not rewrite every Saline source to water material, declare it
   a non-habitat quality, or infer a replacement from one modal triad.
4. Preserve source paths/nodes, 899 STRAIN and 150 ORGANISM assertions,
   distinct pool/count semantics, stable path and old events. Append required
   new correction history rather than modifying the prior review events.

## Follow-up Checks

Add regressions for the exact source-parent edge, retained ontology parent,
marine descendant control, CLOSE-versus-EXACT source-label handling and
same-spelling provenance behavior. Retain all source/taxon counts unless a
governed original-source refresh proves a correction. Dry-seed and inspect a
forced ENVO:01001319 canary before guarded wider regeneration; do not prune
partial runs. Require schema, labels, provenance/history, complete corpus
reproduction, generated-site/redirect and full QC gates.

Parent removal and synonym removal change actual semantic text; a scope-only
correction is text-neutral. Compare the implemented result and perform genuine
map/site refresh under #1217 where needed, preserving #1218/runtime pins.
No SSSOM/KGX compatibility conclusion follows without actual product audits.

## Additional Notes

All 572 open/closed issue titles and bodies were searched for the exact keys,
stem and ENVO identity. #1445 concerns a different deep-groundwater source
mapped to this term; it does not fix this record's inland parent or synonym.
#1249's body was inspected and is a distinct ontology-scope code path.
No exact follow-up was found in that bounded search; comments were not
exhaustively searched. No GitHub mutation occurred in this individual review.

Typed ENVO snapshot SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
