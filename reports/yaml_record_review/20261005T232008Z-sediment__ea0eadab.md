# YAML Record Review: Sediment (marine strait)

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/sediment__ea0eadab.yaml`
- Started UTC: 2026-10-05T23:16:40Z
- Finished UTC: 2026-10-05T23:20:08Z
- Verdict: needs curation; 0 blocker, 2 major, 0 minor findings.

## Target

The complete generated HabitatRecord was read. habitatmech:GOLD.62cda1b482
Sediment is AQUATIC/NARROW/SEEDED, specifically
Environmental > Aquatic > Marine > Strait > Sediment. It has two parents,
one uncounted GOLD attestation and one seed event; other optional scientific
fields are empty. PATHS.tsv:2013 pins the stem. The source denotes sediment
in a strait context, not the entire geographic passage or its water.

## Validation

- `just validate data/habitats/aquatic/sediment__ea0eadab.yaml`: pass.
- `just validate-strict data/habitats/aquatic/sediment__ea0eadab.yaml`:
  pass, one file and zero errors.
- Fresh complete actual build_corpus/build_document equality: pass;
  one source, zero reviewed sources, zero taxa and one history event.
- Actual child/parent routes with complete mappings, all 14 raw inventories,
  whole rendered page and full-context semantic probes inspected.
- Earlier completed local `just qc` is reused: 457 passed, three skipped,
  two warnings; 90 histories, all 3206 schemas, 32 causal overlays,
  reproduction, site and remaining gates passed. Log:
  /private/tmp/habitatmech-sediment-aquifer-qc-approved-20261005.log.
  All tracked non-report files match tested
  f031f0dd4e20fd1ae386442756cf4fa0a2ad53ab. No new local full-QC run is
  claimed; latest main CI 37386142771 also completed successfully.
- Shared earlier `just validate-products` passed: 1179 canonical, one
  synonym, five exceptions and 2054 configured no-adapter skips. Relevant
  current official meanings and typed OWL were independently checked here.
- Original GOLD study Gs0154244 returned HTTP 403. Current child 5904
  and parent 4515 returned 404, not proof of retirement. Parent 4516 resolved.
- No standalone reference validator is exposed in justfile. The child has
  no reference-bearing evidence, parameter, taxon or causal-edge entry.

## Identity and Grounding

The mint reproduces. Default and applied child routes both take
gold_narrower_than_leaf_match, retaining the qualified source identity and
ENVO:00002007 sediment with NARROW/skos:narrowMatch. No child ITEM decision
applies; the mapping-table fallback is not reached.

Current official/typed
[sediment](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002007)
is particulate environmental material (ontology_terms.tsv:7170;
ontology_subclass_edges.tsv:5268). This true material genus should remain
without collapsing the qualified source into every other sediment record.

The independent GOLD parent pass at src/habitatmech/seed.py:898-907 adds
ENVO:00000394 strait. Parent source GOLD.f02c676b23 defaults through
gold_leaf_label to EXACT; ITEM REVIEW at decisions.tsv:1327 yields
curated_review_of_gold_leaf_label, reviewed=True. An endorsed parent
identity does not independently validate every incoming is-a edge.

Current [strait](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000394)
describes a narrow connecting passage between larger waterbodies.
Typed OWL places it under ENVO:00000395 channel of a watercourse
(terms/subclass:6980/5046), separately from a waterbody-related restriction.
Current [channel of a watercourse](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000395)
is a confining depressed landform with bed and banks (6981/5047).
The child deposit is not the complete passage/channel. This is a
material-versus-geographic-feature distinction, not a claim that strait
is a class of liquid water, or that OWL formally declares disjointness.
The ontology's channel-refactoring editorial note does not justify this
sediment-to-strait edge.

The complete strait.yaml parent was read through PATHS.tsv:571. It has
GOLD/PREGO attestations, an uncounted GOLD source, 2 TAXON assertions,
two displayed PREGO taxa and three events. Its own synonyms, outgoing
parents and taxon-source chains were not independently reviewed here;
none is an additional child finding or inherited evidence. This context
read is not counted as an individual review of the parent record.

Exact current ENVO queries for strait sediment, marine strait sediment
and channel sediment returned zero: bounded searches, not proof of absence
from every ontology. Current/typed
[marine sediment](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A03000033)
is a material candidate with marine-water-column transport and seafloor-
settling conditions (terms/subclass:9589/7974). Assess those conditions
before using it as a tighter genus; do not exact-merge solely on context
or substitute a whole coastal waterbody.

SourceAttestation.mapping_predicate at habitatmech.yaml:317-322 declares
source-to-record endpoints and omission when the source is the record;
GroundingStatusEnum:776-790 likewise compares source and record. Actual
resolution instead compares the retained mint to an implicit ontology
parent, reproducing #1398. A global predicate reversal cannot supply
the missing endpoint; no formal SKOS self-link prohibition is asserted.

## Evidence

gold_ecosystem_paths.tsv:1552 records node 5904, depth five and zero
organism, study, biosample and total counters. The positive-organism rule
at seed.py:892-895 correctly omits assertion_count and assertion_unit.
Zero tree counters are not biological absence. In particular, do not
substitute the three samples below for missing organism assertions.

gold_path_biosamples.tsv:838 separately lists three bulk samples.
API gold_path_triads.tsv:671-673 covers three samples in one study:

| Role | Cached modal term | Distinct terms | Top share | Agreeing studies |
| --- | --- | --- | --- | --- |
| Broad | ENVO:00000447 marine biome | 1 | 1.00 | 1 |
| Local | ENVO:02000049 coastal water body | 1 | 1.00 | 1 |
| Medium | ENVO:00002007 sediment | 1 | 1.00 | 1 |

Current/typed marine biome is an ecosystem (terms/subclass:7031/5104-5105).
Current [coastal water body](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A02000049)
is a whole marine waterbody bordering a coast (9451/7834). The material
medium is distinct from both context slots. Unanimity within this small
single-study subset is not universal source equivalence, and equal API/bulk
totals are not a verified sample-level crosswalk.

The one complete gold_studies.tsv membership row was read:

| Physical row | Study accession | Distinct paths in study |
| --- | --- | --- |
| 3938 | Gs0154244 | 53 |

The 53 paths span engineered, terrestrial, aquatic and host-associated
material, including both Strait and Strait > Sediment. They are not 53
strait samples or interchangeable observations. The original
https://gold.jgi.doe.gov/study?id=Gs0154244 returned 403, so current
study contents and exact sample/publication provenance remain unavailable.
Across all 14 structured raw TSV scans, no exact child parameter, BacDive,
PREGO or MADIN contribution was found.

Fresh parent gold_ecosystem_paths.tsv:1551 records the depth-four Strait
path, actual nodes 4515/4516 and all-zero tree counters. Current 4515
returned 404; active [GOLD 4516](https://www.ebi.ac.uk/ols4/api/ontologies/gold/terms/https%253A%252F%252Fw3id.org%252Fgold.path%252F4516)
preserves the exact path with marine-biome context, local strait and an
exact ENVO:00000394 annotation. A preliminary neighboring-node probe of
5903 was discarded as unrelated: the raw row, not numeric adjacency,
determines the collapsed parent nodes. Child 5904 returned 404, so no
current child vocabulary projection was recovered. None of those failures
authorizes deleting the historical source or inferring retirement.

The entire rendered page faithfully displays count omission, the full
path and NARROW/SEEDED warning, but calls strait a broader habitat.
No comparison literature or parent-taxon origin was imported as child
evidence. Exact inventory roles and ontology meanings establish the
material/context distinction without a fabricated sample crosswalk.

## Completeness

Ignored/hidden-inclusive exact child/parent identifiers, node, path, stem
and Strait/compound-label searches covered curation, history, research,
conf, docs, source/tests, reports and PATHS/RETIRED. They found the path
lock and generic channel/neighboring-habitat mentions, but no child-owned
ITEM decision, definition, overlay, dedicated research/history, retirement
or prior individual review. Contextual reads are not extra review coverage.

Optional blanks are not additional defects. The child asserts no gene,
regulator, protein or expression dataset; iModulonDB is not applicable.
The parent PREGO rows and unrelated paths within Gs0154244 cannot fill
those slots without exact child evidence.

## Findings

| Severity | Finding | Maintained owner / scope |
| --- | --- | --- |
| Major | Strait sediment material inherits its geographic passage/channel as a strict superclass. | Exact GOLD.62cda1b482 source-parent contribution to ENVO:00000394 in src/habitatmech/seed.py or governed source-specific controls. |
| Major | Retained-source NARROW/skos:narrowMatch compares an implicit ontology parent rather than the declared record endpoint. | Shared #1398 schema/resolver/attestation-consumer contract; automatic-route witness. |

No blocker or minor finding was established. Source identity, sediment
genus, omitted count/unit, SEEDED status and one-event history are faithful.
Parent-owned concerns and source-access limits are not extra child findings.

## Recommended Edits

1. ITEM-assess this exact source and suppress only its false strait-parent
   contribution. Preserve the true sediment genus, qualified mint, full
   path/node, pinned category/stem, omitted organism count/unit and history.
   A leaf REVIEW/GROUND_AS_PARENT alone does not bypass the second pass.
2. Assess a tighter marine-material genus from source-wide evidence before
   adoption. Do not promote the coastal waterbody local term to identity,
   transfer parent taxa or assign all 53 study paths to this child.
3. Reconcile explicit source/record/ontology-parent mapping endpoints under
   #1398, without global predicate reversal or collapsing source identities.

## Follow-up Checks

Regress exact strait exclusion, true material retention, count/unit omission,
the one 53-path study membership, distinct observation denominators,
honest status/history and explicit mapping endpoints. Dry-seed and inspect
the exact forced canary, append required new history and run ordinary/
strict/label validation, provenance/floor/history, complete reproduction,
site/redirect, term-request checks and full QC. Never manually patch
generated YAML/pages or prune a partial generation.

Authored definitions require minted UNGROUNDED records
(src/habitatmech/curate/definitions.py:149-167). Do not force this NARROW
child's status or use blanket REPLACE merely to remove one source edge.
Actual full-context strait-parent removal changes semantic text and requires
genuine #1217 map/site refresh. Predicate-only omission is text-neutral,
not SSSOM/KGX compatibility validation. Audit current kg-microbe consumers
separately; preserve protected draft #1218 and runtime pins.

## Additional Notes

All 620 open/closed issue titles/bodies were searched for exact child and
parent keys, node, stem and strait/sediment wording; no exact owner was
found. #1398's body was read earlier in this review sequence; all 32
current comments were freshly searched for this exact witness without
a hit. Repository-wide comments were not exhaustively searched.
No GitHub mutation, scientific edit or old-report/history rewrite occurred
during this individual review.

Typed ENVO SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
