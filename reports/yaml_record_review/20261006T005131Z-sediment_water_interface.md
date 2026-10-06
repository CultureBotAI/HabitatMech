# YAML Record Review: Sediment-water interface

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/sediment_water_interface.yaml`
- Started UTC: 2026-10-06T00:46:45Z
- Finished UTC: 2026-10-06T00:51:31Z
- Verdict: needs curation; 0 blocker, 1 major, 0 minor findings.

## Target

The entire generated HabitatRecord was read. habitatmech:GOLD.1218ad430c
is the sediment-water interface in Environmental > Aquatic > Non-marine
Saline and Alkaline > Hypersaline lake, not an unqualified sediment, the
whole lake, a microbial mat or the separately reviewed hypersaline-lake
sediment. The source uses an en dash in its verbatim leaf label.

It is AQUATIC, UNGROUNDED and SEEDED, with one parent, one GOLD attestation,
one ORGANISM assertion and two history events. No definition, synonym,
parameter, taxon, evidence, graph or discussion is emitted.
PATHS.tsv:1411 pins sediment_water_interface.

## Validation

- `just validate data/habitats/aquatic/sediment_water_interface.yaml`:
  pass, no issues.
- `just validate-strict data/habitats/aquatic/sediment_water_interface.yaml`:
  one record, zero errors.
- Actual build_corpus/build_document whole-document equality: pass;
  one source, zero reviewed sources, zero taxa and two history events.
- Fresh `just verify-corpus`: 3,206 expected/found, zero missing, extra
  or differing; exact reproduction.
- Fresh `just validate-history`: all 90 existing history records valid.
- Complete source/parent resolver execution, all 14 raw TSV inventories,
  whole rendered page and actual full-context semantic text were checked.
- Full QC baseline at unchanged scientific inputs:
  [merge-group run 37394437897](https://github.com/CultureBotAI/HabitatMech/actions/runs/37394437897)
  passed with 457 tests, three skips, two dependency warnings, 90 valid
  histories and exact corpus reproduction. Main-push run 37395337654 was
  freshly confirmed COMPLETED/SUCCESS during this review. This is reused
  full-QC evidence, not a new full local suite for this report.
- The unchanged-input ontology-label baseline passed in run 37393180315:
  1,179 canonical pairs, one synonym, five exceptions, 2,054 configured
  no-adapter skips and zero flagged pairs. Current official candidate
  lookups below are additional bounded checks, not an all-ontology proof.
- No standalone reference validator is exposed by justfile. This target
  has no reference-bearing scientific entries to validate individually.

## Identity and Grounding

The repository mint function reproduces GOLD.1218ad430c. The actual
default route is gold_unmatched. The CLASS CONFIRM_UNGROUNDED decision at
curation/decisions.tsv:196 yields
curated_confirm_ungrounded_from_gold_unmatched, still UNGROUNDED,
unreviewed, with no mapping predicate. Its note explicitly says that
habitat validity was not assessed by the class sweep. The two generated
events correctly retain that class decision and the later seed event.

Omission of mapping_predicate agrees with the declared source-to-record
contract at habitatmech.yaml:317-322 because the retained record is its
source concept. This is not another NARROW/skos:narrowMatch witness for
#1398. Lack of an ITEM decision is correctly disclosed as SEEDED, not a
separate emitted status defect.

The sole strict parent, ENVO:01001020 hypersaline lake, comes from the
independent GOLD parent pass at seed.py:898-907. Parent source
GOLD.ac077b806e takes gold_leaf_label to EXACT/skos:exactMatch in both
default and applied execution, without an ITEM override.
The full parent YAML and its 20261003T131028Z review were read as context:
115 ORGANISM assertions, two source nodes, ontology definition, two parents
and one seed event. That older pass verdict does not endorse an incoming
interface-to-lake edge.

Current official and typed [hypersaline lake](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001020)
describe a whole lake with water saltier than ocean water, subclassing
saline lake ENVO:00000019. Fresh saline-lake and lake lookups retain
whole-waterbody meaning. Inventory term/subclass locators are
8515/6815, 6616/4647-4648 and 6617/4649.
An interface between sediment and overlying water is not a subtype of the
whole containing lake. This is a category/scope judgment, not a formal OWL
disjointness assertion or a denial of hypersaline context.

Exact current ENVO searches for sediment-water interface, sediment water
interface and hypersaline lake sediment water interface each returned zero.
Ignored-inclusive inventory searches recovered
[interface layer ENVO:01001684](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001684)
and [lake bed ENVO:00000268](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000268);
both were freshly checked against official text and typed OWL.
Interface layer separates environmentally distinct material portions and
is a plausible broader-genus candidate, not an exact match to this
hypersaline-qualified source. A curator must resolve whether the source
denotes a finite interfacial layer or a sampled boundary-associated
microenvironment. Lake bed denotes the ground surface beneath a lake;
its exact lake-bottom alias and RELATED lake alias do not establish
interface equivalence. Locators: terms 9177/6857, subclass 7539/4902.

## Evidence

All 14 committed raw TSVs were parsed for exact path/node membership.
Only gold_ecosystem_paths.tsv:962 matched: node 8101, depth five,
one organism, zero study/biosample counters, total one. The positive-count
rule at seed.py:892-895 faithfully emits 1 ORGANISM. This is not one
identified sample, taxon or mechanism observation.

No exact child bulk-sample, API-triad, study, parameter, BacDive, PREGO or
Madin row was found. These are snapshot misses, not biological absence.
No original study accession was recovered, so no study-page request or
crosswalk was fabricated. The parent row at :180 contains nodes 7892/7893
and 115 organisms; those assertions are not the child's cohort.

Current GOLD vocabulary requests for 8101, 7892 and 7893 returned 404,
not proof of retirement. Browser-tool ENVO API requests failed, while
direct structured API retrieval succeeded for the named terms and exact
searches. Those access outcomes are distinguished from biological evidence.

[Burke 1995, PMID:24186721](https://pubmed.ncbi.nlm.nih.gov/24186721/),
DOI 10.1007/BF00167162, was inspected in PubMed metadata and the full
abstract, not full text. At hypersaline Lake Hayward it distinguishes
benthic microbial communities, sediment-water exchange and overlying
bottom water. This supports the bounded compartment distinction.
It is not provenance for GOLD node 8101 and does not supply its taxon,
site, oxygen measurement, salinity value or a universal causal graph.

The complete generated page faithfully shows the source path, one
ORGANISM, UNGROUNDED/SEEDED warning and class-level caveat, but calls the
whole hypersaline lake a broader habitat.

## Completeness

Hidden/ignored-inclusive ID, node, label variants and stem searches covered
curation, history, research, configuration, docs, source/tests, reports,
PATHS and RETIRED. They recovered the CLASS row, path lock, incidental
parent-research enumeration and sibling context, but no child ITEM
decision, definition, overlay, dedicated research/history, retirement or
previous individual review. The marine-sediment overlay's generic interface
wording does not belong to this exact hypersaline source.

The full 20261005T193824Z-sediment__bf1216c6 sibling report was read, not
reused as this target's review. Its 85 organisms and NARROW endpoint finding
do not transfer. Optional blanks are not extra defects; no gene, regulator,
protein or expression dataset is asserted, so iModulonDB is not applicable.

## Findings

| Severity | Finding | Maintained owner / scope |
| --- | --- | --- |
| Major | Sediment-water interface inherits its whole hypersaline lake as a strict superclass. | Exact GOLD.1218ad430c parent contribution in src/habitatmech/seed.py, or governed source-specific controls/definition after ITEM assessment. |

No blocker or minor finding was established. Counts, source identity,
predicate omission, SEEDED status and two-event history are faithful.

## Recommended Edits

1. ITEM-assess this exact qualified source and suppress its false whole-lake
   parent through maintained inputs. Preserve mint, path/node, one ORGANISM,
   category/stem, omitted predicate and existing history.
2. Assess interface layer as a broader genus, with a source-scoped authored
   definition if justified; do not ground exactly to the generic layer,
   lake bed, sediment, microbial mat or whole lake from lexical proximity.
   Do not infer alkalinity from the saline-or-alkaline ancestor.
3. This minted UNGROUNDED record meets the current status guard for authored
   definitions (curate/definitions.py:149-167), unlike the NARROW sibling.
   A future REPLACE is legitimate only after ITEM evidence establishes that
   every inherited parent is false and supports the replacement genus and
   definition. Eligibility is not evidence; do not invent a definition merely
   to bypass the parent pass. A leaf-only decision does not itself suppress it.

## Follow-up Checks

Regress exact false-parent exclusion, qualified interface identity, chosen
genus semantics, source count/unit and predicate omission. Preserve the
parent lake's true ancestry and unrelated valid source parents.
Append required correction history, dry-seed, inspect the exact forced
canary and use guarded regeneration; run schema/strict, labels,
provenance/floor/history, full reproduction, site/redirect, term-request
checks and full QC. Do not hand-edit generated outputs or prune partial runs.

Removing the actual sole parent changes full-context semantic text; genuine
map/site refresh under #1217 is required for that future curation.
The no-op predicate-omission probe is text-neutral, not export validation.
Preserve protected draft #1218 and runtime pins. This report does not
certify current kg-microbe SSSOM/KGX readiness.

## Additional Notes

All 623 open/closed issue titles/bodies were checked for the exact source,
node, stem and interface wording; no exact owner was found.
Complete #1514 plus its zero comments concerns separate sediment children.
Complete #1245 concerns hypersaline water environment and hypolimnion,
not this interface. Repository-wide comments were not exhaustively searched.
The overbroad CLASS-row search was truncated; the exact child decision was
then retrieved separately and is the basis for the decision assessment.

No GitHub mutation, scientific edit, regeneration, status promotion or
historical-report rewrite occurred during this individual review.
Typed ENVO SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.

