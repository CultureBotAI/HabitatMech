# YAML Record Review: Seagrass bed sediment

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/seagrass_bed_sediment.yaml`
- Started UTC: 2026-10-05T08:50:41Z
- Finished UTC: 2026-10-05T08:54:56Z
- Verdict: needs curation; 0 blocker, 1 major, 0 minor findings.

## Target

The entire generated HabitatRecord was read. habitatmech:GOLD.e63a1a61c3
Seagrass bed sediment is AQUATIC, UNGROUNDED and SEEDED. It has one
Intertidal zone parent, one GOLD attestation without count/unit/predicate,
and two events including an explicitly CLASS-level CONFIRM_UNGROUNDED.
Definition, synonyms, xrefs, parameters, taxa, evidence, graphs, discussions
and datasets are empty. PATHS.tsv:3000 pins the stem. It is sediment,
not the seagrass organism, its root surface or the entire vegetated bed.
No scientific input or generated output was changed.

## Validation

- `just validate data/habitats/aquatic/seagrass_bed_sediment.yaml`: pass.
- `just validate-strict data/habitats/aquatic/seagrass_bed_sediment.yaml`:
  pass, one file and zero errors.
- Complete build_corpus/build_document equality: pass, one source,
  zero reviewed sources, no taxa and two events.
- Fresh `just validate-products`: pass, 1179 canonical, one synonym,
  five exceptions and 2054 no-adapter skips. It does not prove that the
  source-path parent is scientifically broader.
- Exact child and parent resolver routes were independently executed.
  `just worklist --status all --limit 5` is still running at report close;
  no terminal result is claimed for it.
- First fresh `just qc` exited 2 before any gate because uv could not
  access its cache. The authorized retry is live in tests after lint,
  documentation and raw provenance passed. Later gates are not claimed.
  Log: /private/tmp/habitatmech-seagrass-sediments-qc-retry-20261005.log.
- Previous publication main-push QC 37285767845 has now passed; that is
  separate from the current batch's local QC.
- Removing the sole parent changes real full-context semantic text.
  Predicate omission is neutral because the record has no predicate.
  No map or export was regenerated.

## Identity and Grounding

Actual minting reproduces GOLD.e63a1a61c3. The default is gold_unmatched;
the CLASS CONFIRM_UNGROUNDED at curation/decisions.tsv:1271 applies
curated_confirm_ungrounded_from_gold_unmatched, still reviewed=False.
The source denotes a real microbial habitat, but that does not retroactively
turn the historical class sweep into an ITEM assessment. No #1398 narrowMatch
is asserted on this record.

The sole parent habitatmech:GOLD.115edc36f8 denotes Environmental > Aquatic
> Marine > Intertidal zone. Its complete record was read: NARROW/SEEDED,
ENVO:00000316 and marine-waterbody parents, 77 ORGANISM assertions, two
collapsed GOLD nodes and one event. Those counts and its own ancestry
findings are not inherited target evidence. Actual parent resolution takes
gold_narrower_than_leaf_match with ENVO:00000316 as extra parent, without
an ITEM override. The GOLD second pass at seed.py:898-907 independently
adds the parent mint to the sediment.

Current official [intertidal zone](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000316)
and typed ENVO describe a geographic area between tide marks. Sediment
located in that area is not a kind of the area. This material-versus-region
defect does not depend on proving that this particular GOLD source also
contains subtidal samples; retain its stated intertidal context.

Candidate terms were checked in current official ENVO and typed OWL:

| Candidate | Scope |
| --- | --- |
| [ENVO:00002179 intertidal sediment](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002179) | Active sediment superclass candidate; no textual definition in the inspected sources, and not seagrass-specific. |
| [ENVO:03000033 marine sediment](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A03000033) | Sediment deposited through the marine water column; broader candidate, not an exact qualified identity. |
| [ENVO:01000059 sea grass bed](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000059) | The vegetated bed, not its sediment material; do not substitute it as an exact identity or material genus. |

Current OLS search for seagrass sediment returned zero terms. A full typed
ENVO class-label scan for seagrass/sea grass found the bed, not an exact
sediment material. This is bounded to the inspected ENVO sources, not
proof that no ontology anywhere can represent the concept. The official
GOLD node 7941 returned 404, which is not a retirement ruling.

## Evidence

All 14 raw inventories were scanned for exact source path/node membership.
Physical gold_ecosystem_paths.tsv:1529 records the depth-five path
Environmental > Aquatic > Marine > Intertidal zone > Seagrass bed sediment,
one node 7941 and zero organism/study/biosample counters. The emitted
count/unit omission is faithful; zero does not establish microbial absence.

Separate gold_path_biosamples.tsv:834 records three bulk samples for
path ID 7941. No exact API-triad aggregate was found. The complete
gold_studies.tsv:4305 row associates Gs0159291 with six paths: generic
Marine, Estuary: Sediment, Mangrove sediment, Seagrass bed sediment,
Sediment and Tidal flats. Shared study membership does not merge those
materials or transfer all observations to each path. The original
[GOLD study](https://gold.jgi.doe.gov/study?id=Gs0159291) returned 403;
sample/accession-level membership was not recovered. The three bulk
samples are not three organisms or independent studies. No exact
BacDive/PREGO/MADIN/parameter contribution feeds this target.

The original [Jensen, Kuhl and Prieme study](https://academic.oup.com/femsec/article/62/1/108/521339),
DOI 10.1111/j.1574-6941.2007.00373.x and PMID 17825072, was inspected in
the publisher abstract and sampling/microsensor/DNA methods. PubMed EFetch
verified the identifiers and abstract. It separately sampled Zostera marina
roots and surrounding sediment at two Danish sites and compared bacterial
communities using molecular methods. It establishes that the sediment is
a microbial habitat and that root-associated communities must not simply
be assigned to bulk sediment. Its approximately one-metre-deep, low-tidal-
range sites are not original evidence for GOLD's intertidal cohort. No
site temperatures, salinities, community fractions or mechanism were
imported as universal target claims.

The full rendered page faithfully displays the exact source path,
UNGROUNDED/SEEDED and CLASS-not-ITEM warning, but reproduces the geographic
parent in Broader habitats. Page agreement is not independent support.

## Completeness

Ignored/hidden-inclusive exact identifier, node, source path, label and
stem searches covered curation, history, research, conf, individual reports,
inventories, PATHS/RETIRED, docs, source and tests. The class decision and
path lock exist; no target-owned ITEM decision, authored definition,
causal overlay, dedicated research, separate history, retirement or prior
individual target review was found. Broader seagrass/sediment searches
found contextual seaweed and bivalve research, not target-owned curation.

An optional definition could clarify the qualified material but its absence
is not a second major finding. Keep unsupported taxa, measurements and
mechanisms empty. iModulonDB is not applicable: the target asserts no
gene, regulator, protein or expression dataset.

## Findings

| Severity | Finding | Maintained owner / scope |
| --- | --- | --- |
| Major | Sediment material inherits a geographic Intertidal zone as its sole strict broader habitat. | Exact GOLD.e63a1a61c3 source-parent contribution in src/habitatmech/seed.py and governed source-specific parent controls; compatible authored material definition if justified. |

No blocker or minor finding was established. Preserve the identity and
source context rather than merging with generic bed, root or zone records.

## Recommended Edits

1. ITEM-assess the exact source in curation/decisions.tsv and remove only
   its unsupported geographic parent contribution. A CONFIRM_UNGROUNDED
   decision alone does not disable the separate parent pass.
2. A source-qualified definition in curation/term_requests.tsv can keep
   the compatible minted UNGROUNDED route and a verified sediment genus.
   REPLACE is defensible only after confirming that the sole old parent
   is false and the new material parent is supported; do not use it to
   discard a genuine parent elsewhere. Keep tidal context in the source
   path/definition, not as a region-as-material subclass assertion.
3. Preserve node/path, omitted organism count, three-sample provenance,
   stem/category and old events. Append correction history only during
   authorized scientific curation; recover original cohorts before enrichment.

## Follow-up Checks

Regress the exact false-parent removal, retained mint and source fields,
material-versus-bed/root/zone boundaries and valid geographic controls.
Dry-seed and inspect a GOLD.e63a1a61c3 canary before guarded regeneration;
require schema, labels, provenance/history, exact reproduction, site/redirect
and full QC. Never prune a partial run.

Parent/definition edits change semantic inputs: perform genuine #1217
map/site refresh when needed and leave protected #1218/runtime pins alone.
No actual SSSOM/KGX product or current kg-microbe modeling audit was performed.

## Additional Notes

All 587 open/closed issue titles and bodies were searched for the exact
source, node, stem and seagrass-sediment wording. #1253 concerns the parent's
own waterbody edge and #1470 the generic sea grass bed, not this sediment
material edge; their full bodies were inspected. No exact repair owner was
found. Comments were not exhaustively searched. No GitHub mutation occurred
during this individual review.

Typed ENVO snapshot SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
