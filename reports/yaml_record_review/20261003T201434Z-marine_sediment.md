# YAML Record Review: marine sediment

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/marine_sediment.yaml`
- Started UTC: 2026-10-03T20:08:57Z
- Finished UTC: 2026-10-03T20:14:34Z
- Verdict: needs curation

## Target

Read the entire generated HabitatRecord for `ENVO:03000033`, marine sediment,
and the complete maintained `curation/causal_graphs/marine_sediment.yaml`.
The record is AQUATIC, EXACT, SEEDED, with GOLD, MADIN and ENVIRONMENTS_TABLE
attestations, seven parameter bands, 25 observational taxa, and one graph with
14 nodes and 14 edges. `data/habitats/PATHS.tsv:912` pins its stem.

## Validation

- `just validate data/habitats/aquatic/marine_sediment.yaml`: passed.
- `just validate-strict data/habitats/aquatic/marine_sediment.yaml`: one file,
  zero errors.
- `just validate-causal curation/causal_graphs/marine_sediment.yaml`: passed.
- Structured comparison proved the graph and its original curation event are
  copied exactly from the maintained overlay.
- Fresh `just qc` has passed lint, documentation and raw provenance and is
  still in its test stage at report finish. No final result is claimed here.
- Current ENVO, all 25 displayed NCBI taxon IDs, all four PMIDs and the DOI
  were inspected. Full-text passages and whole-XML snippet searches were used
  for the four PMC papers. The Lin paper's published PDF was inspected.
- OAK checks record and graph-node identity, not taxon source labels or
  scientific entailment of causal edges. Required CI remains necessary.

## Identity and Grounding

`ontology_terms.tsv:9583` and current ENVO support the label, definition and
exact plural synonym. Marine sediment is deposited particulate material, not a
whole water body. `ontology_subclass_edges.tsv:7974` and current OWL support
the true parent `ENVO:00002007` sediment. The generated extra parent
`ENVO:00001999` marine water body is false: overlap/adjacency restrictions in
the OWL do not establish subclass identity with that water body.

The extra parent follows GOLD's `Environmental > Aquatic > Marine > Sediment`
path through `seed.py`'s second parent pass. The composed marine-sediment
identity is supported; a bare GOLD synonym Sediment must be interpreted with
its source path, not as a claim that all sediment is marine. Issue #67's
path-aware lexical-screen correction does not validate the false parent.

Source keys are `habitatmech:GOLD.ee38841e3d`,
`habitatmech:MADIN.09b886e043`, and
`habitatmech:ENVIRONMENTS_TABLE.9c315d57d6`. Ignored-inclusive exact searches
found no matching ITEM decisions or term request. SEEDED remains appropriate;
an added graph is not a review of every source concept.

## Evidence

`gold_ecosystem_paths.tsv:39` has nodes 4563/4564 and 1,035 organism
assertions; the first node, two-node note, full path and ORGANISM unit match.
The tree's study/biosample counts are zero, not evidence that no samples exist.
Exact-path scans found `gold_path_biosamples.tsv:66` with 533 bulk samples and
`gold_path_triads.tsv:665-667` with 286 API samples across 40 studies:

| Role | Source term | Top share | Agreeing studies |
|---|---|---:|---:|
| broad | ENVO:01000024 marine benthic biome | 0.92 | 38 |
| local | ENVO:01000105 marine benthic feature | 0.92 | 37 |
| medium | ENVO:03000033 marine sediment | 0.93 | 39 |

The local-scale term is a known obsolete-source annotation, not a replacement
identity to adopt. All 4,587 committed study rows were scanned by exact path
membership: 44 matches span physical rows 529-4077. Their live study pages
were not inspected. Bulk, tree and API snapshots have different units and
coverage; do not force their counts to agree or borrow other paths in a study.

`madin_habitats.tsv:10` supplies 837 TAXON assertions. All 25 displayed rows
match `madin_habitat_taxa.tsv:997-1021`, including source spellings and pool.
No invented rank, score or corroboration is present. NCBI resolves 24 IDs
directly and aliases `1017277` to `296995`; 14 supplied names match exactly.
The other eleven comprise five capitalization/underscore differences and six
taxonomy updates, including the alias. Original taxon-habitat observations
were not independently verified.

`environment_parameters.tsv:95-101` uses the single target term for
`sediment_marine`. All seven generated bands match: high salinity, medium
structural complexity, high water availability, high pH, small salinity
variability, low temperature variability, and permanently wet water status.
These are attributed qualitative source bands, not universal measurements or
numeric bounds. Qualified multi-term rows are not evidence for the generic
record.

The following inspected sources ground the causal audit:

- **D:** [D'Hondt et al., PMID:31388058](https://pmc.ncbi.nlm.nih.gov/articles/PMC6684631/),
  introduction, Fig. 1 and discussion of redox zonation. It contrasts oxic
  slowly accumulating sediment with anoxic faster-accumulating settings and
  explicitly discusses co-occurring redox processes.
- **J:** [Jorgensen et al., PMID:31105660](https://pmc.ncbi.nlm.nih.gov/articles/PMC6492693/),
  introduction, organic-matter degradation, pyrite formation and oxidation
  sections. Its stated emphasis is fine-grained continental-shelf sediment,
  not every deep-sea, seep or hydrothermal setting.
- **W:** [Wasmund et al., PMID:28419734](https://pmc.ncbi.nlm.nih.gov/articles/PMC5573963/),
  introduction and sulfate-reducer discussion. Substrates and temperature also
  constrain communities; sulfate alone is not a sufficient ecological cause.
- **N:** [Nagakura et al., PMID:35308366](https://pmc.ncbi.nlm.nih.gov/articles/PMC8927301/),
  abstract and introduction. The experiments concern organic-rich Guaymas
  Basin sediment and temperature-dependent sulfate-reducing activity.
- **L:** [Lin et al., DOI:10.1016/j.epsl.2022.117841](https://api.repository.cam.ac.uk/server/api/core/bitstreams/da5d036c-2344-4ffc-8494-216f2fee4429/content),
  abstract and Results/Discussion, especially pp. 4-8. The experiments concern
  clay-surface effects on Desulfovibrio bizertensis sulfate reduction, with
  explicit laboratory-to-natural-environment limitations.

Every edge was checked; a real title excerpt is not a fabricated quotation,
but it is generally a poor claim-bearing snippet:

| Edge ID | Claim-level judgment |
|---|---|
| marine_sediment_receives_particles | Supported by ENVO and D's deposition discussion; the attached title alone does not express particle deposition. |
| particles_bury_marine_organic_matter | D explicitly describes deposition of solid organic matter. The attached redox-topic phrase is real but not the relevant passage. |
| buried_organic_matter_depletes_oxygen | Conditional respiratory interpretation is supported; J's title is not the causal passage. Do not imply inevitable anoxia. |
| oxygen_depletion_creates_anoxic_porewater | Over-scoped. D explicitly documents oxygen penetration through some entire sediment columns. |
| seawater_supplies_sulfate | Supported by J's seawater penetration and porewater-exchange discussion; improve the topic-only snippet. |
| sulfate_selects_sulfate_reducers | W supports ecological opportunity under suitable substrates and conditions, not sulfate as a sufficient selector. The title fragment is weak evidence placement. |
| anoxic_porewater_enables_sulfate_reduction | N supports activity in anoxic Guaymas sediment, not a universal prerequisite that all competing acceptors be exhausted. D and J document overlap. |
| sulfate_reducers_perform_sulfate_reduction | W supports the metabolic guild and pathway; replace title-derived text with a claim-bearing passage. |
| sulfate_reduction_mineralizes_carbon | Supported by J for organic-carbon oxidation in the stated anoxic setting. |
| sulfate_reduction_produces_sulfide | W supports the conversion, but the stored snippet is not verbatim in the full XML, including after whitespace normalization. |
| sulfide_selects_sulfur_oxidizers | J supports sulfide utilization near available oxidants; selection wording is a bounded interpretation, not an isolated sufficiency experiment. |
| sulfur_oxidizers_perform_sulfide_oxidation | Supported by W; the attached text is from the title rather than the supporting mechanism passage. |
| reactive_iron_traps_sulfide | L's inspected claim concerns clay effects on sulfate reduction, not the attached iron-trapping reaction. J's pyrite section offers an appropriate replacement source. |
| sulfide_reaction_forms_iron_sulfides | Supported by J's pyrite-formation discussion; replace its title excerpt with that passage. |

The graph summary also incorrectly describes carbon mineralization to sulfide.
Carbon oxidation and sulfate reduction are coupled but have different
products; the summary must distinguish them.

## Completeness

The 812 undisplayed Madin taxa were not individually checked. Taxa remain
observational, with no `is_characteristic` claim. Parameter bands have no
numeric measurements to verify. No dataset should be fabricated from GOLD
study membership alone.

Ignored-inclusive searches by identifier, label, stem, source keys, graph ID
and citations covered curation, history, research and prior reports. They found
the overlay and related deep-sediment reports, but no prior report for this
exact target, authored term request or separate graph-session history. Related
reports and research were leads only, not source evidence for this verdict.
The overlay's valid 2026-09-04 event does not replace session provenance under
`history/`; its absence is advisory under `history/README.md`.

## Findings

1. **Major - HM-MARINE-SEDIMENT-001:** unsupported whole-waterbody parent.
   Owner: source-specific parent control in curation and `src/habitatmech/seed.py`.
   [#1293](https://github.com/CultureBotAI/HabitatMech/issues/1293).
2. **Major - HM-MARINE-SEDIMENT-002:** graph scope and claim-evidence defects,
   including generalized anoxia, overstrict sequencing, non-verbatim snippet,
   mismatched iron-reaction evidence, weak title-only snippets and the coupled
   carbon/sulfur wording error. Owner: `curation/causal_graphs/marine_sediment.yaml`.
   [#1294](https://github.com/CultureBotAI/HabitatMech/issues/1294).
3. **Minor - HM-MARINE-SEDIMENT-003:** legacy Madin taxonomy aliases/names.
   Canonical names include Micromonospora maris (1003110), Flagellimonas
   taeanensis (1005926), Marivirga tractuosa (1006), Exiguobacterium indicum
   (1017277 -> 296995), Pontixanthobacter gangjinensis (1028742), and
   Christiangramia aestuarii (1028746). NCBI synonym/authority fields preserve
   the old names. Owner: versioned taxonomy/Madin inputs and `extract.py`.
   [#1295](https://github.com/CultureBotAI/HabitatMech/issues/1295).
4. **Minor - HM-MARINE-SEDIMENT-004:** missing graph-session history. Add fresh
   corrective provenance with the next overlay correction, not a backdated
   claim about the original session. Tracked with #1294.

No blocker was established. Resolvable taxon aliases are not broken references.

## Recommended Edits

1. Suppress only the unsupported GOLD parent contribution; retain the true
   sediment genus, supported identity, source counts and seven parameter bands.
2. Repair the maintained overlay using exact short passages and section
   locators. Qualify applicability, retain supported processes and distinguish
   carbon oxidation from sulfur reduction. Do not delete valid mechanisms
   merely because their original snippet was poorly chosen.
3. Refresh taxonomy through governed inputs with original identifiers and
   spellings retained as provenance; preserve pool and observational semantics.
4. Append a real current session-history record when those curation edits are
   performed. Do not rewrite the existing generated event.

## Follow-up Checks

Add source-parent regressions; validate each changed edge against inspected
source context and all graph endpoints. Run overlay validation, seed dry run,
canaries, strict/OAK checks, provenance checks and exact corpus reproduction.
Regenerate changed map/site products using supported runtime #1217, then run
full QC. Test alias/replacement deduplication and preserve taxon provenance.
Draft #1218 is not modified; these three issues remain scientifically unfixed.

## Additional Notes

Current official [ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl)
SHA256 is `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
All 457 issues and returned comments were searched before filing the findings.
The source keys were checked with the actual ENVIRONMENTS_TABLE prefix after
an exploratory display used the abbreviation ENV. No conclusion relies on
that abbreviation. Broad full-text output was truncated; relevant complete
paragraphs were retrieved again before judging. Normal/strict validation was
confirmed again after the earlier processes were verified absent.

iModulonDB was not applicable: the record has no gene, locus, strain-specific
regulatory or expression-module claim. No paid research was used. The record,
overlay, scientific inputs, history and generated products were not edited.
