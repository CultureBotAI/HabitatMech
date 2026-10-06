# YAML Record Review: Subterranean lake (freshwater)

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/subterranean_lake.yaml`
- Started UTC: 2026-10-06T13:49:12Z
- Finished UTC: 2026-10-06T13:55:15Z
- Verdict: needs curation; 0 blocker, 1 major, 0 minor findings.

## Target

The complete generated HabitatRecord was read. GOLD.51eb0120ab denotes
Environmental > Aquatic > Freshwater > Subterranean lake, not the separately
minted deep-subsurface lake or Cave lake. It is AQUATIC/UNGROUNDED/SEEDED,
with one parent, one uncounted GOLD attestation and two historical events.
All other optional scientific fields are empty. The actual seed.mint API
reproduces habitatmech:GOLD.51eb0120ab; PATHS.tsv:1885 pins its stem.

## Validation

- `just validate data/habitats/aquatic/subterranean_lake.yaml`: passed.
- `just validate-strict data/habitats/aquatic/subterranean_lake.yaml`:
  one file, zero errors.
- Actual full build_corpus/build_document equality: passed for the entire
  target; one source concept, zero reviewed sources, zero taxa, two events.
- Fresh shared gates on unchanged scientific baseline bdee3d006 passed:
  `just verify-corpus --max-diffs 1` (3206 expected/found, zero missing,
  extra or differing); `just validate-history` (92); `just validate-causal-all`
  (32 overlays/graphs); `just term-requests-check` (109 current terms);
  `just provenance-check` (14 inventories, two GOLD sources).
- `just validate-products`: 1179 canonical, one synonym, five accepted
  exceptions, zero flagged pairs and 2054 configured no-adapter skips.
  This checks identifiers/labels, not whether a parent relation is true.
- `just worklist --limit 2000`: zero undecided ungrounded records,
  1810 decisions. This is not evidence of ITEM review.
- `just report`: completed; 3206 records, 686 REVIEWED and 2520 SEEDED.
- No standalone citation validator is documented for this citation-free
  child. No child causal overlay requires a focused graph validation.
- Browser OLS API retrieval failed, but fresh direct JSON retrieval and
  typed official ENVO OWL inspection succeeded. The live GOLD study page
  could not be opened; its source membership is verified only in the
  committed, provenance-checked inventory. No fresh full test suite or
  browser-based page QA was run for this read-only report.

## Identity and Grounding

The exact raw path at gold_ecosystem_paths.tsv:1497 collapses GOLD4561 and
GOLD4562, depth four, with zero organism/study/biosample/total counters.
The first-node attestation and two-node note are correct; omission of count
and unit follows the positive-organism rule in seed.py:900-903.

Actual resolution with the complete ontology and upstream mapping index is
gold_unmatched, followed by CLASS CONFIRM_UNGROUNDED from decisions.tsv:519.
The result remains unreviewed. Neither the sweep nor this generated history
establishes a comprehensive absence of fitting ontology terms.

The parent-path source independently resolves GOLD.ad12f0169a Freshwater by
gold_leaf_synonym to ENVO:00002011, CLOSE/skos:closeMatch, then receives its
own ITEM REVIEW. The second GOLD pass at seed.py:906-935 adds that resolved
identifier to the child's strictly broader parents. The parent's review
does not review the child or make a containing water material its genus.

Fresh [official OLS](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002011)
and typed [official ENVO OWL at a2455d1](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
confirm that ENVO:00002011 denotes low-solute water material. In contrast,
[ENVO:00000058 underground lake](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000058)
denotes a below-surface lake and has direct named parents lake and underground
water body. The relevant definitions and parents agree with the vendored
ontology rows. A freshwater underground lake contains fresh water; it is not
therefore a subtype of that material. This is a semantic category distinction,
not an argument from an absent ontology edge or claimed formal disjointness.

The freshwater qualifier may make the source narrower than generic underground
lake. ENVO:00000058 is a supported genus candidate, not automatic permission
to erase that qualifier, adopt exact identity or merge similarly named records.

## Evidence

Exact membership parsing across all 14 raw TSVs found the source path in four:

| Input | Target-specific support |
|---|---|
| gold_ecosystem_paths.tsv:1497 | Two node IDs, exact path/label and zero KGX counters |
| gold_path_biosamples.tsv:889 | Two bulk-export biosamples, ecosystem path ID 4562 |
| gold_path_triads.tsv:410-412 | Two samples, one study, one term per slot, share 1.00 and one agreeing study |
| gold_studies.tsv:2428 | Gs0142421, one path, exactly this freshwater lake path |

The triad assigns ENVO:01000252 freshwater lake biome at broad scale,
ENVO:00000058 underground lake at local scale and ENVO:04000007 lake water
as medium. Fresh OLS/typed OWL checks confirm all three labels and entity
types. These are complementary contexts, not three interchangeable identities;
one study with two samples is not independent multi-study corroboration.
The separate bulk-sample count does not replace the zero KGX organism count.

[Hershey et al. 2018](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2018.02823/full),
DOI 10.3389/fmicb.2018.02823, was inspected in publisher metadata, abstract,
introduction and sampling methods. It directly studies microbial communities
in Wind Cave aquifer lakes and distinguishes cave-lake access from well and
spring sampling. This supports habitat plausibility, not attribution to
Gs0142421/GOLD4561, universal taxa, chemical ranges or causal mechanisms.
No full-methods or supplementary-data audit is claimed.

The complete fresh_water parent and both similarly named lake records were
read as scope controls. No parent taxa, parameters, graph, references or
counts are inherited as evidence for this child. Earlier Cave lake and
lake-sediment review reports are leads, not independent biological evidence.

## Completeness

The consequential gap is the unsupported material superclass and unresolved
ITEM-level waterbody grounding. A definition or exact merge must await a
bounded assessment of freshwater versus generic/deep-subsurface lake scope.
An empty optional definition alone is not counted as another finding.

No target-specific taxon or parameter contribution was recovered from the
other ten raw inventories. No curator-owned definition, causal overlay,
session history, research report, dataset or discussion was found in the
searched maintained/research surfaces. Those fields should remain empty
rather than borrow the fresh-water parent's claims. A study accession and
triad are not a general mechanism citation or a characteristic-taxon list.
iModulonDB is not applicable: this child names no organism, gene, regulator
or transcriptomics dataset.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | The freshwater subterranean lake is emitted as a subtype of fresh-water material, while a supported underground-lake genus is unrepresented. The class-level sweep did not resolve this waterbody/material distinction. | The exact GOLD.51eb0120ab source-parent contribution in seed.py and curation/gold_parent_exclusions.tsv; ITEM grounding in curation/decisions.tsv and any justified definition/genus in curation/term_requests.tsv. |

Blockers: none found. Minor findings: none found. Candidate selection and
the false parent are treated as one coherent hierarchy-curation task, not
double-counted as a status defect. SEEDED truthfully reports the current state.

## Recommended Edits

1. Assess this exact freshwater source at ITEM depth. Prefer a justified
   narrower-than-underground-lake representation unless exact coextension is
   demonstrated. Do not merge with GOLD.937bf682c4 or GOLD.d9fb6dd542 merely
   because their labels resemble this one.
2. Remove only the unsupported GOLD source-context contribution through the
   guarded exclusion table, or a justified authored replacement after proving
   every inherited parent false. Adding a correct genus alone leaves the
   incorrect fresh-water edge in place. Reassess an exclusion's expected
   parent deliberately if the Freshwater source is later re-grounded.
3. Preserve both node IDs in the authoritative row, displayed first-node
   provenance, path, pinned stem, count semantics and old audit events. Any
   actual curation needs new history and generator-produced audit events.

## Follow-up Checks

After maintained-input curation: dry seed; inspect a guarded target canary;
test exact parent/source preservation and retained independent hierarchy;
run strict schema, labels, history, provenance and full corpus reproduction.
Regenerate term requests only when their maintained inputs change.

An in-memory full-context semantic probe changes the broader-habitat text
from fresh water to underground lake when the illustrative corrected genus
is used. Real curation therefore requires a genuine map rebuild and normal
site regeneration, followed by redirects, render-check and full QC. The
working Linux route is proven by PR #1560; no stale-map or runtime-pin bypass
is justified. No generated record or product was edited in this review.

## Additional Notes

Absence searches used rg --no-ignore --hidden for the identifier, label,
stem, node and study across curation, history, research, workspace, reports,
PATHS and raw inventories. Structured raw parsing checked all 14 TSVs.
No ENVO:00000058 use was found in curation or generated habitat YAML/TSV
inputs, with ignored files included. No earlier report targets this exact
file; older reports only discuss it as context. Generated HTML, SQLite/DB,
OWL/OBO bytes and git internals were not used as negative-search authority.
The initially requested references directory does not exist; actual top-level
directories were inventoried and the search repeated over existing surfaces.

The pinned ontology source was parsed by RDF predicate, separating formal
definitions from OLS descriptive comments. No GOLD live-page content, exact
literature-to-study mapping, comprehensive ontology absence, product readiness
or completion of the full corpus review is claimed. This report alone is new;
no curation, history, generated product or GitHub item was changed.
