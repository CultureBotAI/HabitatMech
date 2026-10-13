# YAML Record Review: Microbialites

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/microbialites__a38bc21d.yaml`
- Started UTC: 2026-10-04T18:40:53Z
- Finished UTC: 2026-10-04T18:43:22Z
- Verdict: needs curation

## Target

Entire generated HabitatRecord habitatmech:GOLD.e53e2c6e8e, Microbialites,
AQUATIC, NARROW/REVIEWED. Two parents, one uncounted GOLD attestation with
skos:narrowMatch and a two-node note, and two history events are present.
Definition, synonyms, xrefs, parameters, taxa, citations, graphs, discussions,
datasets and replacement links are not emitted.

The exact source path is
`Environmental > Aquatic > Freshwater > Microbialites`.
The displayed source node is gold.ecosystem:3798; the collapsed second node
is gold.ecosystem:4191. The actual mint matches; PATHS.tsv:2995 pins the
stem. This is a depth-four microbialite source, not water or a crater lake.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/microbialites__a38bc21d.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/microbialites__a38bc21d.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Fresh shared run PASS: 1,179 canonical pairs, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | PASS: 953 ungrounded records, 1,810 decisions. |
| `just qc` | Still active at retired-URL checks. 457 tests passed, three skipped, two warnings in 635.50 seconds; 90 history records, 3,206 strict records, 32 graph curations, exact reproduction and generated-site checks passed. No terminal outcome claimed. |
| Source/reference checks | Full target, maintained row, all 14 raw tables with exact path membership, actual resolver, typed OWL/current OLS for both source nodes, four study attempts and full page/semantic comparisons inspected. |

Later terminal QC belongs in the publication receipt, not a backdated
completion-time observation. No SSSOM/KGX export audit was executed.

## Identity and Grounding

`curation/decisions.tsv:1265` is a genuine ITEM GROUND_AS_PARENT decision
dated 2026-08-12 for ENVO:03600064 microbialite. The retained identity,
REVIEWED state and two events follow it faithfully.

Current official ENVO defines microbialite as sedimentary rock formed from
carbonate mud through benthic microbial mediation. Its named parent
ENVO:00002016 is sedimentary rock. Current GOLD node 4191 explicitly
annotates this microbialite term, supporting the curated interpretation
without establishing every individual sample's carbonate composition.
The intact structure is not automatically interchangeable with a microbial mat.

Current [ENVO:00002011 fresh water](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002011)
is water with low dissolved-solute concentration, particularly sodium
chloride. It is a material, not the broad class of all freshwater-associated
habitats. A microbialite occurring in freshwater is not itself a kind of
water. No universal salinity threshold is inferred for the microbialite
from the ontology's explanatory comment or GOLD branch label.

The source context, lake-biome annotation, local lake feature and sampled
rock remain different roles. Substituting a crater lake or freshwater lake
biome for the material parent is not justified by the triad modes alone.

## Evidence

Physical `gold_ecosystem_paths.tsv:1484` gives the exact depth-four path,
nodes 3798 and 4191, two collapsed nodes, zero organism/study/biosample
counters and zero total. The first-node display, two-node note and omitted
count/unit are faithful. Zero tree organisms are not biological absence.

`gold_path_biosamples.tsv:567` separately gives 14 bulk samples under
path ID 4191. Triad rows 362-364 cover nine complete-triad samples across
three studies:

| Role | Modal term | Share | Distinct terms | Agreeing studies |
| --- | --- | ---: | ---: | ---: |
| Broad | ENVO:01000252 freshwater lake biome | 1.00 | 1 | 3 |
| Local | ENVO:01001062 crater lake | 0.56 | 4 | 1 |
| Medium | ENVO:00001995 rock | 0.56 | 4 | 1 |

Fresh current typed ENVO verifies the lake-determined biome, lake within
a crater and solid mineral/mineraloid aggregate rock. The crater term does
not specify crater origin. Modal local and medium values each have one
agreeing study and four distinct terms; their separate marginals do not
prove a paired crater-lake/rock majority. The aggregator counts studies
containing the top term, not independently verified experimental replication.
There is no inspected sample crosswalk establishing the nine API samples
as a particular subset of the 14 bulk samples. Neither replaces the zero
tree-organism count; generic rock does not prove carbonate composition.

Four exact study memberships each have one path:
`gold_studies.tsv:130` Gs0046965, `:301` Gs0060786, `:538` Gs0099924 and
`:2567` Gs0144662. All four original GOLD study-page requests returned 403.
Committed memberships are verified, not current experimental contents;
four memberships are not the three-study complete-triad cohort.

Current official GOLD node 3798 returned 404 without proving retirement.
Node 4191 is active with the full exact path. Its structured annotations
contain broad ENVO:00002030 aquatic biome and medium ENVO:03600064
microbialite, but no local-scale field. The provider's description says
complete despite that missing field; no local annotation is invented here.
These vocabulary annotations differ from the sample-summary lake-biome,
crater-lake and generic-rock modes, and are not a new sample cohort.

The complete 14-table scan used exact canonical-path equality and exact
pipe-separated study-path membership, not descendant substring matching.
It found no exact-target parameter, PREGO or BacDive taxon rows. No numerical
condition, characteristic taxon or causal mechanism is established for this bin.

Actual full normalized-table resolution gives default
gold_unmatched/UNGROUNDED/no predicate. The maintained ITEM row yields
curated_ground_as_parent_from_gold_unmatched, NARROW/skos:narrowMatch,
extra parent ENVO:03600064 and reviewed=True. `seed.py:554-566` and
`:839-843` own that route; the independent parent pass at `:898-907` adds
fresh water. Emission at `:890-891` reproduces #1398: the ontology parent
comparison is not the source/record endpoint contract declared by schema
`habitatmech.yaml:317-322` and `:776-790`.

## Completeness

Ignored-inclusive exact ID/node/path, stem, shared microbialite-label and
freshwater filename searches covered curation, history, research, reports,
PATHS and RETIRED. The decision and path lock exist, but no target-owned
definition, overlay, dedicated research, session history, retirement or
prior individual review was found. Adjacent water/biome reports are not
source-specific mineralogical or microbial evidence.

The inspected header of `curation/causal_graphs/fresh_water.yaml` targets
ENVO:00002011 and models freshwater hypoosmotic response, not this microbialite.
It is not attached here and must not be copied as a universal mechanism.
No full new audit of that graph is claimed. Optional omissions are not defects;
iModulonDB is inapplicable without a gene, regulator or expression claim.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | A freshwater-associated microbialite is emitted as a kind of fresh water material. | GOLD parent pass or governed exclusion for GOLD.e53e2c6e8e and expected parent ENVO:00002011. |
| Major | Curated NARROW/skos:narrowMatch use ontology-parent endpoints rather than the declared source/record comparison. | Resolver, attestation emitter, schema and consumers, #1398. |

Counts: zero blockers, two major, zero minor. Identity, two-node provenance,
count omission and ITEM-derived review/history remain faithful. No formal
SKOS inconsistency or observed downstream export failure is asserted.

## Recommended Edits

1. Suppress the false water-material contribution, preserving both source
   nodes and their collapse note, exact path/identity and count omission.
   Assess any future replacement source-parent identity independently;
   neither a lake nor a biome mode automatically supplies a valid genus.
2. Reconcile mapping endpoints/status semantics across actual routes;
   preserve the microbialite reference and legitimate imported mappings.
3. Add exact-source/edge/endpoint and node-preservation regressions, append
   required correction history and regenerate through maintained inputs.

## Follow-up Checks

After correction run `just seed`, then
`just seed-canary habitatmech:GOLD.e53e2c6e8e --force`. Inspect the whole
canary, both nodes/note, absent count/unit, selected genus, REVIEWED derivation
and prior events plus required new history before `just seed-apply --force`.
Never prune partial runs. These are future commands, not executed review edits.

Require ordinary/strict schema, labels, source/history and mapping-consumer
tests, `just verify-corpus` and `just qc`. The full page lists fresh water
under Broader habitats. Its isolated removal changes full-context semantic
text by removing `broader habitat: fresh water`; scientific repair needs
genuine map/site refresh under #1217. Predicate-only omission was separately
text-neutral. Protect #1218/runtime pins and inspect actual SSSOM/KGX products
before claiming compatibility.

## Additional Notes

All-state exact-key and freshwater/microbialite searches returned no matches.
Track the bounded microbialite hierarchy witness and extend #1398; publication
does not implement either scientific repair. The maintained decision includes
the complete source path. Official typed ENVO OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No scientific input, generated product, prior report/history or paid research changed.
