# YAML Record Review: Attached/Keratinized gingiva

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/attached_keratinized_gingiva.yaml`
- Started UTC: 2026-10-04T08:29:46Z
- Finished UTC: 2026-10-04T08:34:27Z
- Verdict: needs curation

## Target

Read the complete generated HabitatRecord `habitatmech:GOLD.1b82504233`:
HOST_ASSOCIATED, UNGROUNDED, SEEDED. This is the human GOLD source, not
the general-mammal record with the same label. It has one Oral cavity
parent, one attestation, a CLASS-level decision event and a seed event.
No definition, synonyms, positive assertion count, taxa, parameters,
causal graph or dataset is emitted. PATHS.tsv:1487 pins the filename.
The actual mint helper reproduces the ID from the complete source path.

## Validation

- `just validate data/habitats/host_associated/attached_keratinized_gingiva.yaml`:
  passed, no issues.
- `just validate-strict data/habitats/host_associated/attached_keratinized_gingiva.yaml`:
  one file, zero errors.
- Fresh batch `just validate-products`: passed; 1,179 canonical pairs,
  one synonym, five configured exceptions and 2,054 no-adapter skips.
- Fresh batch `just qc`: lint, documentation and provenance passed;
  tests are still running at report completion. No terminal full-QC
  result is claimed. Its remaining gates cover history, strict schema,
  references, overlays, corpus reproduction, site, redirects and requests.
- Unchanged scientific baseline `a7acd01cd4958003420b697f1c2ef859a9b369f9`
  passed [required queue QC](https://github.com/CultureBotAI/HabitatMech/actions/runs/37188207641).
  This does not substitute for final-head CI on the new report.
- Current official OLS term metadata and typed gingiva graph inspected;
  original HMP protocol inspected. Live GOLD study pages returned request
  errors, so sample-level source reconciliation remains unverified.
- Actual full-context semantic-adapter comparison confirms removing the
  cavity parent changes semantic text.

## Identity and Grounding

`curation/decisions.tsv:253` is CLASS-level CONFIRM_UNGROUNDED, based on
lexical nonmatching rather than habitat eligibility. The limited status
and emitted historical note are mechanically honest. Attached gingival
tissue is a plausible physical habitat, not a disease or whole host taxon.

Current [UBERON:0001828 gingiva](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0001828)
is active and describes fibrous tissue investing teeth; its definition
agrees with ontology_terms.tsv:13075. The typed graph subclasses it to
[UBERON:0003729 mouth mucosa](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0003729),
matching vendored subclass row 11262. It also contains separately typed
part-of and adjacency relations, which must not be flattened into is-a.

Bounded current OLS searches for attached gingiva, keratinized gingiva
and the full compound label in BTO/UBERON/ENVO found contextual or broader
candidates, not an exact full-label match. Even exact-query mode returned
alveolar-mucosa and dentogingival-junction description hits for attached
gingiva. These are not synonyms of the target. Generic gingiva, gingival
epithelium, groove and adjacent alveolar mucosa are not automatically the
same thing as the compound source site. No global absence claim is made.

The complete parent `oral_cavity__7cca2853.yaml`,
`habitatmech:GOLD.99880772e1`, denotes whole human Oral cavity, NARROW
under current [UBERON:0000167](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0000167).
That active term defines an anatomical cavity, matching vendored row
12911. The parent has no authored oral-surface-environment definition.
Gingival tissue is not a subtype of this cavity. The minted rather than
exact parent identity does not repair the type error.

`src/habitatmech/seed.py:898-907` adds the edge because of GOLD nesting.
The strictly-broader rule applies to that route as well as ontology and
curator-authored parents. Source-path provenance is not an is-a proof.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:2217` supplies the exact human path,
node 3910, one node and zero tree organism/study/biosample assertions.
The emitted record correctly does not invent a positive ORGANISM count.
The parent's 1,032 organisms are not this leaf's observations.

Separate maintained inventories add bounded context:

- `gold_path_biosamples.tsv:711`: seven biosamples for the exact path.
- `gold_studies.tsv:119`: Gs0046820 has one path, this target.
- `gold_studies.tsv:378`: Gs0063646 includes this target among 15 paths;
  it is one study membership, not 15 target studies.
- `gold_path_triads.tsv:1433-1435`: one sample and one study in each
  slot. Broad is UBERON:0001007 digestive system, local is UBERON:0001828
  gingiva, and medium is UBERON:0001836 saliva. Current official metadata
  verifies all three labels; raw ontology rows 12983/13075/13077 agree.

Counts belong to different inventories and units; seven bulk biosamples
must not become seven tree organisms. The triad's local site and sampled
medium have different roles. A saliva medium is not an identity override
for gingival tissue, and the broad anatomical annotation does not
automatically justify an ecosystem parent. The GOLD study pages for both
accessions returned request errors. Their committed memberships were
verified, but no current sample-level source text is claimed inspected.

The original [HMP Manual of Procedures, version 9.0, section 7.3.1.6](https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/document.cgi?phd=2235&study_id=phs000228.v3.p1)
lists keratinized/attached gingiva as a distinct soft-tissue sampling
surface. It samples maxillary anterior attached gingiva separately from
other sites and separates soft-tissue swabs from saliva and dental plaque.
This historical protocol supports the anatomical site interpretation;
the hosting study version is superseded, not misrepresented as current.
It is not proof that every GOLD specimen followed that protocol.

The inspected primary analysis [PMID:38127919](https://pubmed.ncbi.nlm.nih.gov/38127919/),
DOI:10.1371/journal.pone.0295058, compares seven HMP oral sample types
across a 300-person dataset. That is not a gingiva-only denominator or
evidence for GOLD's seven biosamples. The inspected
[HOMD site-abundance view](https://v31a.homd.org/taxa/abundance_by_site/phylum)
also separates attached keratinized gingiva from other oral sites;
its abundance values are not imported into this record.

## Completeness

Ignored-inclusive searches covered identifier, source node, parent key,
label and stem in curation, history, research, PATHS, RETIRED and reports.
They found the CLASS decision and pinned path but no target ITEM decision,
definition request, overlay, session history, research report or redirect.
Exact prior-report metadata traversal including ignored files found no
previous review of this target.

All 12 non-ontology inventories were scanned fully with the target key,
node and attached/keratinized-gingiva wording. The two GOLD host paths
and human-only side-table matches are distinguished above. No matching
row was found in the eight BacDive/Madin/PREGO/mapping/parameter tables
(162, 3,081, 770, 358, 58, 1,378, 719 and 8,807 rows respectively).
This bounded wording search is not absence under every possible synonym.
No optional taxon, mechanism or parameter must be filled for coverage.
No gene, regulator, pathway or expression claim is present; iModulonDB
is not applicable.

## Findings

1. **Major - HM-GINGIVA-1B82504233-001:** source containment is emitted
   as an is-a edge to the whole Oral cavity. The contribution originates
   in `src/habitatmech/seed.py`; a supported definition in
   `curation/term_requests.tsv` can own its replacement as described below.
   Scoped source-parent handling is an alternative. Filed as
   [#1363](https://github.com/CultureBotAI/HabitatMech/issues/1363).

No blocker or minor finding established. Lack of an exact term or an
optional definition is not itself evidence that the source is non-habitat.

## Recommended Edits

Remove or correct the exact false cavity contribution through maintained
rules/inputs. Preserve the human source identity, path/node and count
semantics. An ITEM judgment and explicit source-site definition may
establish defensible tissue/surface ancestry; verify its exact scope
before selecting a genus. The existing `curation/term_requests.tsv`
`parent_mode=REPLACE` route is available once that definition and genus
are supported and its notes establish that every inherited parent is
false. Here the complete current parent set consists only of the false
cavity edge. `docs/CURATION.md:152-164` and
`src/habitatmech/seed.py:423-447` already govern this route; new exclusion
machinery is not a prerequisite. Without an authored definition, use
scoped source-parent handling instead. Do not invent a genus merely to
use REPLACE or use it when any inherited parent is valid.

Do not merge the mammal record by label,
automatically equate the source with all gingiva, or convert containment
into an equivalence xref. Do not hand-edit generated records or pages.

The actual adapter comparison removes `broader habitat: Oral cavity`
and changes text. Require the governed map/site rebuild tracked in
[#1217](https://github.com/CultureBotAI/HabitatMech/issues/1217), without
altering pins or freshness checks. Draft #1218 remains unmerged and
untouched; its proposed mechanism is not available on main and is not
required for the existing definition-owned REPLACE route.

## Follow-up Checks

Regress the precise false edge and retained source facts. Append history
for actual curation, run a dry seed and guarded canary, inspect the emitted
target and require ordinary/strict schema, OAK, provenance/history, exact
corpus reproduction, semantic/site freshness and full QC. Reconcile live
study/sample metadata before importing new evidence or changing identity.

## Additional Notes

All 508 returned issue titles, bodies and returned comments were searched.
Candidate #503 is a separate buccal-mucosa report-count correction;
#1314 concerns PREGO alveolar-bone occurrence and #43 over-generic mappings.
Their inspected scopes do not cover this hierarchy repair. #1363 begins
with this human witness, without claiming the mammal sibling was reviewed.

No scientific input, generated artifact, status, event or history changed.
No paid research ran. The full-corpus review remains ongoing.
