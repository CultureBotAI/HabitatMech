# YAML Record Review: subglacial lake

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/subglacial_lake.yaml`
- Started UTC: 2026-10-06T11:13:35Z
- Finished UTC: 2026-10-06T11:17:25Z
- Verdict: needs curation

## Target

Read the entire generated HabitatRecord ENVO:03000120, subglacial lake,
AQUATIC, EXACT, REVIEWED. It merges two GOLD source concepts, has an
ENVO definition, one synonym, three parents and three generated events.
There are no taxa, parameters, evidence items or causal graphs.
`data/habitats/PATHS.tsv:915` fixes its stem. The existing retired
Freshwater minted URL points to this merged identity; it is not an
unresolved duplicate record.

## Validation

- `just validate data/habitats/aquatic/subglacial_lake.yaml`: passed.
- `just validate-strict data/habitats/aquatic/subglacial_lake.yaml`:
  one file, zero errors.
- Actual full `build_corpus` / `build_document` equality passed for
  every field: two source concepts, both reviewed, zero taxa, three events.
- Executed default/applied routes for both source concepts and both
  immediate GOLD parents. Scanned all 14 raw inventories separately for
  each exact source path/node; read the full page and semantic text.
- [Main QC on unchanged base 7c8d28437](https://github.com/CultureBotAI/HabitatMech/actions/runs/37452730923)
  passed every gate: 463 tests passed, three skipped, two dependency
  warnings, 90 valid histories, zero strict errors and exact reproduction
  of 3,206 records, current site, redirects and term requests. Required
  merge-candidate label correspondence also passed with zero flagged
  pairs and 2,054 no-adapter skips. This is baseline reuse; the separate
  new local publication QC was still running when this report finished.
- No emitted taxon, evidence or graph references require separate checks.

## Identity and Grounding

Current [ENVO:03000120](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A03000120)
is active and matches the record's label and definition. Typed official
OWL verifies the exact plural synonym subglacial lakes and named parent
[ice-covered lake, ENVO:00000198](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000198).
The local term and subclass rows are `ontology_terms.tsv:9666` and
`ontology_subclass_edges.tsv:8060`. OWL adjacency restrictions are not
additional named superclasses. No synonym-scope defect was found here.

The Freshwater key habitatmech:GOLD.c5a94d7484 and Deep subsurface key
habitatmech:GOLD.7a082e8e9f both default to minted NARROW identities by
gold_narrower_than_leaf_match. ITEM GROUND rows at
`curation/decisions.tsv:1800-1801` change both to the ontology identity,
EXACT/skos:exactMatch and reviewed=True. Thus the generated merge,
REVIEWED status and events faithfully implement the decisions. A faulty
rationale can nevertheless remain in an item-reviewed record.

Current [GOLD4737](https://www.ebi.ac.uk/ols4/api/ontologies/gold/terms/https%253A%252F%252Fw3id.org%252Fgold.path%252F4737)
is active and supplies the exact Freshwater path, local ENVO:03000120
and an explicit exact-match annotation to it. Its broad aquatic-biome
and medium fresh-water annotations are contextual slots, not identity.
This is supporting vocabulary evidence for the Freshwater mapping,
not a substitute for original sample provenance. GOLD3794, GOLD7670
and GOLD7672 returned HTTP 404, which does not establish retirement.

The immediate Freshwater source actually resolves through an ITEM-reviewed
CLOSE synonym route to [fresh water, ENVO:00002011](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002011).
The independent GOLD parent-path pass then adds that water material as
a superclass of the whole lake. A lake is not a kind of its contents.
This is a new witness for [#1220](https://github.com/CultureBotAI/HabitatMech/issues/1220);
retain the true ice-covered-lake parent and both source attestations.

The entire minted aquatic Deep subsurface parent and its prior individual
review were read. Its CLASS-level decision at line 282 remains
UNGROUNDED/SEEDED with no definition. It in turn inherits aquatic biome
ENVO:00002030, whose current definition and OWL describe a biome rather
than every subsurface lake or setting. The exact ancestry is
`ENVO:03000120 -> GOLD.21222434e2 -> ENVO:00002030`.
The parent scope and false biome ancestry are already owned by
[#1226](https://github.com/CultureBotAI/HabitatMech/issues/1226). This
is a descendant witness, not proof that every possible definition makes
the direct lake-to-Deep-subsurface edge false. Do not delete that edge
merely because the parent awaits an item-level scope decision.

## Evidence

| Source path suffix | Exact raw provenance | Distinct denominator |
|---|---|---|
| Freshwater > Subglacial lake | Tree line 711; nodes 3794/4737 | 3 ORGANISM assertions; tree study/biosample counters zero |
| Freshwater > Subglacial lake | Bulk line 699; node 4737 | 7 biosamples |
| Freshwater > Subglacial lake | Triads lines 407-409 | 7 API samples, 3 studies |
| Deep subsurface > Subglacial lake | Tree line 1441; nodes 7670/7672 | All counters zero; count/unit omission is faithful |
| Deep subsurface > Subglacial lake | Bulk line 826; node 7672 | 3 biosamples |
| Deep subsurface > Subglacial lake | Triads lines 218-220 | 3 API samples, 1 study |

Both local triads unanimously use subglacial lake. Both broad slots
unanimously use freshwater lake biome ENVO:01000252. Freshwater's
medium has two terms, top lake water ENVO:04000007 at 0.86 with two
studies agreeing; Deep subsurface's medium is unanimously lake water.
Both contextual terms and their labels are present in the local slice.
They do not turn a biome or sampled water into the lake identity.

Exact study memberships were parsed, including declared-versus-distinct
path-count checks: Freshwater has Gs0114735 (one path), Gs0128895 (two),
and Gs0154581 (one); Deep subsurface has only Gs0112339 (two).
These are memberships, not sample counts, and the individual study
webpages and original sample-to-summary crosswalks were not audited.

The Deep subsurface decision nevertheless states that its path has
three independent studies. Its three are samples, not studies. The
Freshwater path genuinely has three studies, but those cannot be
transferred to the other path. The erroneous path-specific rationale
is reproduced in the generated history and page. The current inventory
still supplies one-study local-scale support; this finding does not by
itself prove the mapping false or justify automatic unmerging.

The retrieved primary abstract of
[Christner et al. 2014](https://pubmed.ncbi.nlm.nih.gov/25143114/),
DOI 10.1038/nature13667, PMID 25143114, reports direct sampling of Lake
Whillans water and surficial sediment, metabolically active microorganisms
and production/sequencing evidence for a microbial ecosystem. This
supports habitat plausibility, not universal taxon composition or the
identity of these GOLD studies. The publisher full-text request failed,
and repeat PubMed open returned incomplete content; no claim depends
on having read the full paper. A hypersaline-lake search lead was also
inaccessible and is not used as evidence here.

## Completeness

Ignored-inclusive exact ID, source-key, label/stem and path searches
covered curation, history, reports, research, documentation, configuration,
source, scripts, tests and path/retirement registries. The two decisions,
path lock and older Freshwater redirect exist; no target-owned term
request, overlay, session history or prior individual review was found.
The sediment-child review and aquatic Deep subsurface review are context,
not omitted target inputs. No exact taxon or parameter feed was found
in the 14 raw inventories for either path.

Empty optional biological and chemical fields are not defects. Do not
borrow the broader parents' organisms or literature taxa. iModulonDB is
not applicable without a gene, regulator or expression claim.

## Findings

Zero blockers, three majors, zero minors:

1. **Major: false fresh-water material parent.** Exact source contribution
   from GOLD.c5a94d7484 adds ENVO:00002011 to a whole lake. Extend #1220.
   Maintained owner: `src/habitatmech/seed.py:898-907`, governed
   source-specific controls and regressions.
2. **Major: inherited unsupported biome ancestry.** The aquatic
   Deep subsurface parent supplies ENVO:00002030. Extend #1226 with
   this descendant and preserve the direct edge until scope adjudication.
   Owners: the parent's `curation/decisions.tsv` and
   `curation/term_requests.tsv` inputs and source-parent generation.
3. **Major: overstated independent-study rationale.** GOLD.7a082e8e9f
   claims three studies but its raw triads and study memberships show
   one. Owner: `curation/decisions.tsv:1801`, with a new append-only
   corrective history entry and regenerated outputs. Track independently
   of the hierarchy defects; do not alter old committed history records.

## Recommended Edits

Suppress only the scientifically invalid freshwater-material contribution;
retain ENVO:00000198, identity, definition, exact plural synonym, both
source paths, counts/units, node-collapse notes and pinned stem. Resolve
Deep subsurface's intended genus through its own maintained curation
before changing the child's direct relation.

Correct the Deep subsurface rationale to its actual three samples and
one study, explaining separately any Freshwater evidence used to justify
the merge. Reassess the mapping at ITEM scope with original provenance;
do not invent two missing studies or mechanically downgrade a mapping
solely because the old evidence count was wrong. Preserve the accurate
Freshwater denominator. Correct maintained decisions and append history,
never hand-edit the generated record or a committed historical record.

## Follow-up Checks

Add exact source-parent and study-denominator regressions, preserving
legitimate water-material children and all supported subglacial-lake
fields. Compare each path's study IDs rather than treating source labels
as evidence of independent replication. Recheck the original samples
before claiming the two populations have identical scope.

Actual in-memory direct-parent removals each changed full-context
semantic text; neither probe is blanket permission to remove a parent.
Predicate omission was text-neutral. Decision-note corrections require
page/history regeneration and a fresh semantic-input comparison; this
review did not test them as an implemented change. Genuine changed map
inputs need #1217 regeneration. Keep draft #1218 and runtime pins isolated.

Future curation requires append-only history, dry seed, inspected guarded
canaries, provenance/schema/labels, exact corpus reproduction and complete
site, redirect, term-request and QC gates. No scientific input, generated
product or SSSOM/KGX artifact was changed or certified in this review.

## Additional Notes

All 634 open/closed issue titles and bodies were searched for exact
keys, subglacial/deep-subsurface wording and study-count/provenance
patterns. #1226's full body has no comments and covers the parent issue;
#126's body and closure comment concern the delivered triad pipeline,
not this erroneous curation rationale. No existing owner for this exact
rationale was found on those surfaces. Every repository issue comment
was not exhaustively searched.

Typed official ENVO snapshot SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
