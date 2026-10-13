# YAML Record Review: marine water body

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/marine_water_body.yaml`
- Started UTC: 2026-10-03T20:21:41Z
- Finished UTC: 2026-10-03T20:57:49Z
- Verdict: needs curation

## Target

Read the complete generated HabitatRecord and maintained
`curation/causal_graphs/marine_water_body.yaml`. The record is `ENVO:00001999`,
marine water body: AQUATIC, EXACT, REVIEWED, with three source attestations,
50 observational taxon entries, a 15-node/15-edge carbon-pump graph and five
generated history events. `data/habitats/PATHS.tsv:609` pins its stem.
The audit resumed after an intervening report-publication turn; scientific
inputs and the target remained unchanged.

## Validation

- `just validate data/habitats/aquatic/marine_water_body.yaml`: passed.
- `just validate-strict data/habitats/aquatic/marine_water_body.yaml`: one
  file, zero errors.
- `just validate-causal curation/causal_graphs/marine_water_body.yaml`: passed.
- Structured comparison proved exact graph and overlay-event projection.
- All 50 displayed taxon entries match their source rows; all IDs were
  queried against current NCBI Taxonomy. All four cited PMIDs and both cited
  DOIs were resolved through primary article or deposited citation metadata.
- Fresh `just qc` passed lint, documentation and raw provenance and is still
  running tests at report finish. No final result from this run is claimed.
- Required OAK checks cover record and graph-node identity, not source taxon
  labels, ecological associations or causal entailment. CI remains required.

## Identity and Grounding

Physical lines `data/raw/ontology_terms.tsv:7164,8118` and current official
ENVO agree on the target and its true parent, `ENVO:01000617` lentic water
body. `ontology_subclass_edges.tsv:5261` asserts that named superclass.
Both ENVO synonyms are genuinely exact; the PREGO plural remains related.

The extra parent `ENVO:00002030` aquatic biome is unsupported. Its definition
at `ontology_terms.tsv:7182` and current OWL describes a biome determined by
a water body, not the water body itself. The GOLD second parent pass in
`seed.py:898-908` converts the Aquatic path context into this false is-a edge.
Do not delete the genuine lentic-waterbody parent.

BacDive Marine maps to the target with medium-confidence lexical closeMatch
at `isolation_source_groundings.tsv:192`; GOLD also retains closeMatch.
The record's EXACT status reflects the merged direct PREGO ontology identity,
not a silent upgrade of those two predicates. The separately attributed GOLD
source-label synonym is not an ENVO axiom overriding its mapping predicate.

ITEM REVIEW decisions at `curation/decisions.tsv:26,550,1488` cover
`habitatmech:BACDIVE.407144fe70`, `habitatmech:GOLD.5856c699e4` and
`habitatmech:PREGO.a653eb2a85`. Their three events explain REVIEWED; the
seeding and graph-addition events do not independently certify scientific
correctness.

## Evidence

`bacdive_isolation_sources.tsv:16` supplies 2,040 STRAIN assertions and a pool
of 1,805 taxa. `gold_ecosystem_paths.tsv:8` supplies 6,420 ORGANISM assertions
from nodes 3487/3768/4003 under `Environmental > Aquatic > Marine`; the first
node and three-node note are preserved. `prego_habitats.tsv:158` supplies 171
taxa, 171 direct assertions, maximum score 4 and environmental-samples evidence.
These units and snapshots must not be summed or forced to agree.

Exact-path scans covered all 1,040 bulk, 1,587 triad and 4,587 study rows:

- `gold_path_biosamples.tsv:8`: 5,248 bulk samples at node 4003.
- `gold_path_triads.tsv:434-436`: 3,749 API samples across 141 studies.
  Broad-scale marine biome has top share 0.96 and 128 agreeing studies;
  local-scale marine water body has 0.79 and 113; medium sea water has 0.87
  and 109. Biome, whole body and material are distinct roles.
- There are 171 exact-path study memberships at physical lines 26-4572.
  Identifiers and membership were inspected, not their live study pages or
  every other path in those studies. The tree's zero study/biosample fields
  are not evidence that no observations exist.

All 25 BacDive rows at `bacdive_source_taxa.tsv:1723-1747` and 25 PREGO rows
at `prego_habitat_taxa.tsv:5366-5390` match IDs, optional labels, counts/scores,
ranks and pools. PREGO rows are direct environmental-samples assertions.
Five entries retain cross-source corroboration: BacDive 28108 and 28258 by
PREGO; PREGO 172371, 180542 and 184914 by BACDIVE. Extraction computes
corroboration against full source sets before top-25 truncation; a missing
reciprocal displayed row is not a contradiction. Original full-set ecological
evidence was not inspected.

NCBI resolves 49 displayed IDs directly and aliases `158080` to `141390`,
Chromohalobacter israelensis, explicitly retaining 158080 in AkaTaxIds.
All 46 supplied names match. Other blank names resolve to Monodelphis
domestica (13616), Nephroselmis pyriformis (156128) and Prasinoderma coloniale
(156133). This is taxonomic identification, not ecological validation.
The unusual 13616 association needs original-source inspection; neither a
replacement organism nor a habitat error is inferred from its name alone.

The six cited publications were checked with these access limits:

- **A:** [Arrigo, PMID:16163345](https://pangea.stanford.edu/research/Oceans/GES205/Arrigo_Nature_Global%20Ocean%20Nutrients.pdf),
  inspected introduction, remineralization discussion and resource-limitation
  text, pp. 349-351. These support light/nutrient context and N/P recycling.
  The PDF's printed DOI is erroneous; the
  [publisher erratum](https://www.nature.com/articles/nature04265) confirms
  `10.1038/nature04159`. The record's PMID is correct.
- **H:** [Herndl and Reinthaler, DOI:10.1038/ngeo1921](https://pmc.ncbi.nlm.nih.gov/articles/PMC3972885/),
  abstract, introduction/Fig. 1, Microbial activity in the dark and energy-demand
  discussion. These support oceanic carbon export and microbial processing,
  while identifying additional carbon sources and uncertainty. All attached
  snippets are observable title/topic fragments, not claim-specific quotations.
- **F:** [Falkowski et al., PMID:18497287](https://pubmed.ncbi.nlm.nih.gov/18497287/),
  NCBI abstract and DOI metadata inspected. The abstract is a general redox
  overview. Publisher and institutional-copy retrieval did not provide the
  full text; the two specific attached claims were not fully source-verified.
- **E:** [Arnosti, PMID:21329211](https://www.annualreviews.org/content/journals/10.1146/annurev-marine-120709-142731),
  publisher abstract inspected. It supports extracellular hydrolysis before
  cellular uptake, but not by itself every particle-specific release detail.
- **Z:** [Azam et al., DOI:10.3354/meps010257](https://doi.org/10.3354/meps010257),
  publisher-deposited Crossref identity and the abstract on
  [coauthor-uploaded content](https://www.researchgate.net/publication/200146439_The_Ecological_Role_of_Water-Column_Microbes_in_the_Sea)
  inspected. The abstract supports bacterial use of photosynthetically fixed
  carbon. Publisher PDF returned 401 and the coauthor download 404; detailed
  particle-leakage entailment remains unverified.
- **U:** [PMID:23139690](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=23139690&retmode=xml)
  is an unrelated visual-memory study in children/adolescents, as verified by
  its title and complete abstract. It is not the Simon aggregate review named
  in the overlay notes. The likely intended Simon paper is
  [DOI:10.3354/ame028175](https://researchprofiles.ku.dk/en/publications/microbial-ecology-of-organic-aggregates-in-aquatic-ecosystems/);
  institution and deposited metadata verify its identity, not claim-level
  support. Its full text was not accessible in this audit.

| Edge ID | Claim-level judgment |
|---|---|
| marine_body_contains_euphotic_zone | A supports illuminated production context; qualify applicability rather than imply every water body has this full vertical structure. |
| euphotic_zone_supports_marine_phytoplankton | A supports resource-dependent production; the attached short topic phrase is weak evidence placement. |
| phytoplankton_perform_oxygenic_photosynthesis | F's inspected abstract is insufficient for the precise claim; full-text verification remains necessary. |
| photosynthesis_generates_particulate_carbon | Supported by H's introduction; replace the generic topic snippet. |
| particulate_carbon_forms_sinking_particles | H supports aggregation, mortality and grazing products; not all particulate carbon sinks. |
| sinking_particles_enter_dark_ocean | Supported by H for exported oceanic particles, within an appropriately deep-water scope. |
| sinking_particles_select_particle_bacteria | U is unrelated. H offers relevant habitat evidence; distinguish enrichment/adaptation from experimentally established selection sufficiency. |
| particle_bacteria_express_extracellular_enzymes | E supports general hydrolysis; H supplies more direct particle-associated enzyme context. |
| enzymes_release_dissolved_organic_matter | E's abstract supports substrate hydrolysis, not all described leakage details; inspect full text or substitute inspected claim-level evidence. |
| dissolved_organic_matter_supports_free_living_heterotrophs | Z's exact leakage claim remains partially verified; H discusses free-living access to dissolved substrates. |
| heterotrophs_drive_microbial_remineralization | H supports dark-ocean heterotrophy; the attached title phrase is not the causal passage. |
| dark_ocean_hosts_remineralization | Supported by H; a pathway depiction must not imply an exhaustive carbon budget. |
| remineralization_consumes_oxygen | Retain the explicit aerobic qualifier; H's oxygen-use context is compatible, but the single-word snippet is weak. |
| remineralization_releases_dic | F's full passage remains unverified; H's introduction directly supports respiratory carbon return. |
| remineralization_regenerates_nutrients | A supports N/P return during degradation; replace the title excerpt with a precise passage. |

## Completeness

The 1,780 undisplayed BacDive and 146 undisplayed PREGO taxa were not reviewed
individually. No entry is promoted to `is_characteristic`. Original ecological
observations, including 13616 and full-source corroboration, remain unverified.

Ignored-inclusive searches by target identifier, label, stem, source keys and
citation IDs covered curation, history, research and prior reports. They found
the three ITEM decisions and overlay, but no exact-target authored term request,
research report, prior target review or identifiable graph-session history.
History's generic marine-waterbody mentions concern gulf, not this graph.
Structured scans found no target field among 109 term requests or 770 parameter
rows. Empty parameter/discussion/dataset slots are not automatic defects.

`KG_MICROBE_ROOT` is unset. An ignored-inclusive search of the configured
kg-microbe checkout found no PREGO files. This does not establish absence from
other checkouts; original transformed evidence remains unavailable here.
The valid 2026-09-04 overlay event is not a substitute for separate session
provenance under `history/`.

## Findings

1. **Major - HM-MARINE-WATERBODY-001:** aquatic-biome context is promoted to
   waterbody ancestry. Owner: source-parent controls and `src/habitatmech/seed.py`.
   [#1300](https://github.com/CultureBotAI/HabitatMech/issues/1300).
2. **Major - HM-MARINE-WATERBODY-002:** unrelated PMID on a causal edge,
   weak claim-level snippets and insufficient graph-scope qualification.
   Owner: `curation/causal_graphs/marine_water_body.yaml`.
   [#1301](https://github.com/CultureBotAI/HabitatMech/issues/1301).
3. **Minor - HM-MARINE-WATERBODY-003:** resolvable PREGO taxonomy alias.
   Owner: governed taxonomy inputs and `src/habitatmech/extract.py`. Added as
   a witness to [#1244](https://github.com/CultureBotAI/HabitatMech/issues/1244).
4. **Minor - HM-MARINE-WATERBODY-004:** missing identifiable graph-session
   history; include current corrective provenance with the #1301 repair.

No blocker was established. An unrelated resolved publication is an evidence
defect, not a dead reference or a wrong habitat identity. Inaccessible full
text is an audit limitation, not proof that its underlying mechanism is false.

## Recommended Edits

1. Suppress only the false GOLD parent contribution; preserve the true lentic
   parent, source predicates, distinct units and reviewed provenance.
2. Correct the maintained graph with inspected claim-level sources. Read the
   intended Simon paper before adopting it or use an appropriate already
   inspected source. Add exact short snippets/locators and explicit scope;
   preserve supported conditional mechanisms and the aerobic qualifier.
3. Refresh the taxon alias through versioned inputs while retaining original
   identifiers and names; inspect unusual ecological assertions before
   deletion, relabeling or characteristic-status promotion.
4. Append actual current session history during curation, not this review.

## Follow-up Checks

Add a source-parent regression, manually verify all changed citations and
edge endpoints, validate the overlay, dry seed and canary the target. Compare
source provenance, counts, ranks, pools and corroboration after any taxonomy
refresh. Run strict/OAK/provenance checks and exact corpus reproduction.
Regenerate affected map/site products with supported runtime #1217 and run
full QC. Draft #1218 remains unchanged; report publication fixes none of these
scientific findings.

## Additional Notes

Current [official ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl)
SHA256: `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
All 463 existing issues and returned comments were searched before filing.
Ontology locators above are physical lines, not logical TSV row numbers.
An exploratory structured scan had a syntax error and was rerun successfully.
Broad search/browser output was truncated; targeted searches and the relevant
source passages were inspected separately. A Europe PMC full-XML attempt for
H returned HTTP 500; no complete-XML snippet search is claimed.

iModulonDB was not applicable to these generic community-process claims;
no strain-specific gene, regulator or expression-module assertion is present.
No paid research, scientific-input mutation or product generation was used.
