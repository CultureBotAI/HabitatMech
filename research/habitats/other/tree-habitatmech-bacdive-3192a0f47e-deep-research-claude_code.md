---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T16:22:38.613429'
end_time: '2026-08-17T16:33:49.233837'
duration_seconds: 670.62
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Tree
  habitat_identifier: habitatmech:BACDIVE.3192a0f47e
  habitat_category: OTHER
  grounding_status: UNGROUNDED
  attestations: 'BACDIVE: Tree'
  assertions: '872'
  parent_terms: ENVO:01001001
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Nearest
    broader term ENVO:01001001 ''plant-associated environment'' attached as a parent.
    A tree as host. No tree-associated environment term exists; BTO:0005516 wood is
    the material, not the living host. Parented to plant-associated environment as
    the nearest broader term. ENVO term request. (source concept habitatmech:BACDIVE.3192a0f47e)'
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-5
  web_search_requests: 22
  num_turns: 40
  total_cost_usd: 4.336958500000001
  session_id: f5428903-5a2b-4701-b8be-f563ef3782a1
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 22
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Tree
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.3192a0f47e
- **Category:** OTHER
- **Grounding status:** UNGROUNDED
- **Source attestations:** BACDIVE: Tree
- **Upstream assertion volume:** 872
- **Nearest broader term already on the record:** ENVO:01001001
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term ENVO:01001001 'plant-associated environment' attached as a parent. A tree as host. No tree-associated environment term exists; BTO:0005516 wood is the material, not the living host. Parented to plant-associated environment as the nearest broader term. ENVO term request. (source concept habitatmech:BACDIVE.3192a0f47e)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Tree** as a microbial habitat, with citations.

This is a definition for an ontology term, not a literature review. The output is judged
on whether a curator can write one defensible sentence from it and cite the sources.

## Required findings

### 1. What the concept denotes

State what physical place, material or setting the label refers to **as a habitat for
microorganisms** — the thing a sample is taken from. Be explicit about the boundary: what
is inside the concept and what is a neighbouring concept.

If the label is ambiguous, say so and give the readings. Do not pick one silently. The
source path above is the strongest evidence of which reading the data means.

### 2. Genus — the broader kind

Name the smallest well-established kind this concept falls under, and say whether an
existing ontology term expresses it (give the CURIE if so). The genus is what the
definition will start from: "A ⟨genus⟩ which ...".

Check ENVO in particular before concluding nothing fits. Report the near-misses and why
each fails — a term that is *narrower* than the concept, or that asserts something the
sources do not, is a near-miss worth recording, not a match.

### 3. Differentia — what distinguishes it

What separates this concept from its siblings under that genus. Prefer properties that
are observable or measurable: physical setting, dominant material, host, formation
process, characteristic physicochemistry.

### 4. Sources

Every claim above needs a citation — a DOI, PubMed ID, or a resolvable URL. Prefer:

- primary literature describing the habitat and its microbial communities
- standards and reference vocabularies (MIxS, GSC, ENVO, SNOMED, AGROVOC)
- authoritative reference works

Say plainly when a claim is your inference rather than something a source states. An
unsupported sentence in a definition is worse than a missing one, because it is
indistinguishable from a supported one once it is in the ontology.

### 5. Synonyms and what NOT to conflate

List names in real use for this concept, and separately list terms that are commonly but
wrongly treated as the same thing.

### 6. Whether it should be a term at all

Say so if the evidence suggests this is not a habitat — a process, a quality, a disease
state, an organism as a taxonomic grouping, or a sampling artefact. That is a useful
answer and the corpus has an established disposition for it. Do not manufacture a
definition for something that should not have one.

## Output format

Plain markdown. Lead with a single proposed definition sentence of the form

> A ⟨genus⟩ which ⟨differentia⟩.

then the supporting sections. Keep the proposed definition to one sentence; if it needs
more, that usually means an intermediate class is missing, and saying so is more useful
than a longer sentence.


## Output

# Research report — `habitatmech:BACDIVE.3192a0f47e` "Tree"

## Proposed definition

> A **plant-associated environment** which is determined by a tree — a woody perennial plant with a single elongated main stem and a more or less definite crown — or by a part of one.

Genus: `ENVO:01001001` *plant-associated environment*. Differentia: the determining plant has the tree growth form, as opposed to the herbaceous, shrub or aquatic-plant hosts that BacDive files as its siblings.

If a single sentence has to carry the ENVO pattern verbatim, the closest existing model is `ENVO:01001179` *cnidarian-associated environment* — "An environmental system determined by a cnidarian or part of a cnidarian" — which is what the draft already in `curation/term_requests.tsv` ("An environmental system determined by a tree.") is reaching for. The version above is the same shape with the growth-form clause added, because "tree" is not a taxon and cannot be left undefined the way "cnidarian" can.

---

## 1. What the concept denotes

**It denotes a host organism, not a material and not a land cover.** This is not an inference from the label — BacDive's own tagging says it. BacDive describes each isolation source with up to four `Cat1/Cat2/Cat3` triplets ([BacDive 2019, *NAR*, PMC6323973](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323973/)). For a representative strain in this bin, DSM 52582 (*Myxococcales* unclassified, Ar10394, BacDive ID 18242, "isolated from bark of cut trees", near Steyr, Austria, 1997-05-01), the categories are exactly:

| Cat1 | Cat2 | Cat3 |
|---|---|---|
| `#Host` | `#Plants` | `#Tree` |
| `#Host Body-Site` | `#Plant` | `#Bark` |

([BacDive strain 18242](https://bacdive.dsmz.de/strain/18242), retrieved 2026-08-17)

So the concept sits on the **host axis**: *what kind of organism the microbe was living on/in*. The anatomical compartment — bark, leaf, root, wood, sap, exudate — is recorded on a **separate, parallel triplet**. That is decisive for the boundary:

**Inside the concept.** The living (or recently felled) tree considered as a place: its bark surfaces and rhytidome fissures, phyllosphere/canopy, sapwood and heartwood, cambium, roots and rhizosphere, exudates, resin, sap flows, cankers and rot columns, and water-filled cavities in the trunk — all of them as *this individual woody host's* environment.

**Outside the concept — neighbouring records that already exist in this corpus.**

| Neighbour | Why it is not this concept |
|---|---|
| `forested area` / `forest ecosystem` (`ENVO:00000109`, `ENVO:01001243`; corpus record `terrestrial/forested_area.yaml`) | A land-cover / ecosystem scale unit. BacDive has its **own separate** `Forest` Cat3 bin already mapped there. A single tree is not a forest. |
| `wood` (`BTO:0005516`; corpus record `host_associated/wood.yaml`, from BacDive `Timber`) | The xylem tissue as material, including processed timber, detached from any host. The curator's existing note on this record is correct. |
| `leaf` (`PO:0006001`; from BacDive `Leaf-Phyllosphere`) | A body-site, on the other axis. Co-occurs with `#Tree` rather than competing with it. |
| `plant resin` (`PO:0025161`; from BacDive `Plant-Exudate-Resin`) | Likewise a body-site/product. |
| `plant litter` (`ENVO:00000628`) | Shed, dead, on the ground — no longer the host. |
| `scrubland area` (`ENVO:00000300`; from BacDive `Shrub-Scrub`) | See §6 — this sibling was grounded to a land-cover term, and that decision should **not** be mirrored here. |

**Ambiguity — two readings, and which one the data means.**

1. *Tree as host organism* (the whole living woody plant as a habitat). **This is the reading the data means**, on the evidence of the `#Host / #Plants / #Tree` triplet and of the strain records themselves.
2. *Tree as a stand or wooded place* (colloquially "sampled from trees" ≈ "sampled in woodland"). BacDive already has a distinct `Forest` bin for this, so reading 2 is spoken for.

A third, purely lexical reading — MIxS `ShadingDeviceTypeEnum#tree`, a built-environment shading-device value — is a false friend and shares nothing but the string ([OLS4 search for exact label "tree"](https://www.ebi.ac.uk/ols4/api/search?q=%22tree%22&exact=true), retrieved 2026-08-17).

**The strain evidence agrees.** The record's top characteristic taxa are *Sorangium cellulosum* (77), *Corallococcus coralloides* (72), *Myxococcus fulvus* (42), *Nannocystis exedens* (38), plus *Archangium*, *Cystobacter*, *Melittangium lichenicola*, *Stigmatella* — i.e. the Reichenbach myxobacterial collection at DSMZ, whose classical substrates are soil, dung, and **bark of living and dead trees**. Reichenbach states this directly: myxobacteria "colonize decaying plant material including rotting wood and bark from dead and living trees" ([Reichenbach 1999, *Environ. Microbiol.* 1:15–21, doi:10.1046/j.1462-2920.1999.00016.x](https://enviromicro-journals.onlinelibrary.wiley.com/doi/10.1046/j.1462-2920.1999.00016.x); PMID 11207714). The habitat was established by J. E. Peterson: 1,081 random bark collections from 95 trees of 32 species in Missouri yielded myxobacteria on 267 pieces (24.7%), and 30 species, six of them new ([Peterson 1959, "New species of myxobacteria from the bark of living trees", *Mycologia* 51:163–172](https://www.tandfonline.com/doi/abs/10.1080/00275514.1959.12024789); see also Peterson 1969, *Methods in Microbiology* 3B:185–210). The second cohort in the taxa list — *Pseudomonas syringae* (19), *Xanthomonas campestris* (12), *Erwinia pyrifoliae* (4, Asian pear fire blight), *Lonsdalea populi* (3, poplar bark canker) — are tree pathogens isolated from diseased woody tissue. Both cohorts are "the tree as host", from bark and wood.

*Caveat required by this repo:* `assertion_count: 872` is in `STRAIN` units and is not comparable to GOLD organism counts or PREGO taxon counts.

---

## 2. Genus — the broader kind

**Recommended genus: `ENVO:01001001` *plant-associated environment*** — "An environmental system determined by a green plant." It is a subclass of `ENVO:01001000` *environmental system determined by an organism* ("An environmental system which is determined by a living organism"), which in turn sits under `ENVO:01001110` *ecosystem*. Confirmed live via OLS4, 2026-08-17: [ENVO:01001001](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01001001). Alternative labels on that class include "Plant" and "Viridiplantae-associated environment".

**ENVO has no term for this concept.** Two checks:

- Exact-label search across all OLS ontologies for "tree" returns **no** ENVO, UBERON, PO, FOODON or BTO class labelled "tree" — only `MIXS:ShadingDeviceTypeEnum#tree` (an unrelated built-environment enum), plus MeSH genus entries and `UBERON:0004999` *mucosa of biliary tree* (retrieved 2026-08-17).
- `ENVO:01001001` currently has **no asserted subclasses at all** (`has_children: false`), so there is nothing narrower to fall back on.

**The pattern already exists in ENVO one level over.** `ENVO:01001002` *animal-associated environment* has taxon-restricted children: `ENVO:01001179` *cnidarian-associated environment* ("An environmental system determined by a cnidarian or part of a cnidarian") and `ENVO:01001176` *environment associated with an aquatic invertebrate*. There is also `ENVO:01001041` *fungi-associated environment* and `ENVO:01001058` *environment associated with a fungal tissue*. A `tree-associated environment` under `plant-associated environment` is the same move on the plant branch — this is the strongest single argument for the request, and it is structural, not rhetorical.

**Near-misses, and why each fails:**

| Candidate | Verdict |
|---|---|
| `ENVO:01001001` plant-associated environment | **Broader**, not equal. Correct as genus/parent; wrong as identity, because it also covers grasses, crops and aquatic macrophytes. |
| `ENVO:01001057` environment associated with a plant part or small plant | Near-miss on both ends. Its definition — "determined by **part** of a living or dead plant, or a whole **small** plant" — excludes the whole-large-plant reading that "Tree" is precisely about. It is also filed under *ecosystem*, not under plant-associated environment. |
| `ENVO:01000999` rhizosphere environment | Narrower — one compartment of one tree, and applies equally to herbs. Filed directly under `ENVO:01000254` environmental system. |
| `ENVO:00000109` forested area / `ENVO:01001243` forest ecosystem | Wrong scale (land cover / ecosystem, not host) **and** already occupied by BacDive's separate `Forest` bin. |
| `ENVO:01001242` canopy / `ENVO:01001239` forest canopy | A vegetation *layer* formed by many crowns — a stand-level structure, not an individual host. (Note `ENVO:00000047` "canopy" is **obsolete**; older sources still cite it.) |
| `ENVO:01001121` plant matter / `ENVO:00000628` plant litter | Environmental *material*, dead and detached. |
| `BTO:0005516` wood | Material, not host — as the existing curation note says. (Its BTO parent is `BTO:0001468` *xylem*.) |
| `PO:0004518` bark, `BTO:0000148` branch, `BTO:0004903` plant crown, `BTO:0001597` sapling | Parts / developmental stages of the host, i.e. the *other* BacDive axis. PO has no "tree" (nearest is `PO:0000003` whole plant). |
| `AGRO:00010164` scattered trees | A landscape-management class about trees in a landscape, not a habitat determined by one tree. |
| NCBITaxon | **Nothing to xref.** "Tree" is not a taxon (§3), so unlike `Mollusca` or `Porifera`, this concept has *no* organism term to park in `relation: xref`. |

---

## 3. Differentia — what distinguishes it

The differentia is the **growth form of the determining plant**, and it is directly what BacDive is partitioning on. The Cat3 siblings under `#Host / #Plants` present in this corpus are: `Tree`, `Shrub-Scrub`, `Herbaceous-plants-Grass,Crops`, `Aquatic-plant` — a life-form partition, not a taxonomic one.

**The growth form itself (observable, measurable, standardised).** FAO's Global Forest Resources Assessment defines a tree as "A woody perennial with a single main stem, or in the case of coppice with several stems, having a more or less definite crown", with the explanatory note that it includes bamboos, palms and other woody plants meeting the criterion; a shrub, by contrast, is "generally more than 0.5 m and less than 5 m in height at maturity and without a single main stem and definite crown" ([FAO, *Terms and Definitions — FRA 2025*, Working Paper 194](https://openknowledge.fao.org/server/api/core/bitstreams/a6e225da-4a31-4e06-818d-ca3aeadfd635/content); wording unchanged since FRA 2005 and registered in [AGROVOC c_7887 "trees"](https://agrovoc.fao.org/browse/agrovoc/en/page/c_7887)).

**Consequences of that growth form that make it a *microbiologically* distinct habitat** — this is where the differentia earns its keep, and each is sourced:

1. **Longevity and seasonal stability of the colonisable surface.** Unlike leaves, flowers and fruits, bark is a long-lived, seasonally stable substrate; the Central European survey states bark surfaces "constitute one of the largest forest compartments" and offer "a multitude of micro niches" under low nutrient and water availability ([Kalkhoff et al. 2024, *ISME Communications* 4:ycae012, doi:10.1093/ismeco/ycae012](https://academic.oup.com/ismecommun/article/4/1/ycae012/7589767), 25 Jan 2024; >750 trees, 133 plots, three regions of Germany, *Fagus sylvatica* / *Pinus sylvestris* / *Picea abies*).
2. **Community distinctness from soil, leaves and roots** — i.e. it is not a proxy for the soil it stands in. Bark microbiota "were distinct from surrounding soils and waters" ([Leung, Jeffrey, Bay et al. 2025, *Science*, doi:10.1126/science.adu2182](https://www.science.org/doi/10.1126/science.adu2182)); heartwood and sapwood microbiomes show "minimal overlap" with roots, bark, leaves or leaf litter ([Arnold, Gewirtzman et al. 2025, *Nature* 644(8078):1039–1048, doi:10.1038/s41586-025-09316-0](https://www.nature.com/articles/s41586-025-09316-0), online 6 Aug 2025).
3. **Secondary growth creates internal compartments no herb has.** The Nature 2025 study defines heartwood as the innermost 5 cm and sapwood as the outermost 5 cm of woody tissue, finds ~10¹² bacteria per tree in wood, with aerobes outside and **anaerobes including methanogens** in the anoxic heartwood, across ~150 trees of 16 species.
4. **Host-species and bark-texture filtering.** Rough-barked oak and linden vs smooth-barked maple support measurably different canopy bark microbiomes (~1,500 genera), attributed to differing protection from UV and desiccation ([*ISME J* 2024, doi:10.1093/ismejo/wrae206](https://academic.oup.com/ismej/article/doi/10.1093/ismejo/wrae206/7825411)).
5. **Age/size as an assembly driver** — only possible in a decades-to-millennia-lived host: tree size (as an age proxy) drives bark community diversity in beech, while management intensity does not ([Frontiers in Forests and Global Change 2022, doi:10.3389/ffgc.2022.858382](https://www.frontiersin.org/journals/forests-and-global-change/articles/10.3389/ffgc.2022.858382/full)).
6. **Stemflow as a vertical transport mechanism down the trunk** ([*Microbiology Spectrum* 2023, doi:10.1128/spectrum.03562-23](https://journals.asm.org/doi/10.1128/spectrum.03562-23), PMID 37971233).
7. **Distinctive canopy phyllosphere.** In Atlantic forest canopies each tree species selected a distinct community, ~97% of sequences were unknown species, 95–671 species per host species ([Lambais et al. 2006, *Science* 312(5782):1917, doi:10.1126/science.1124696](https://www.science.org/doi/10.1126/science.1124696), PMID 16809531).
8. **Scale.** ~3.04 × 10¹² trees globally ([Crowther et al. 2015, *Nature* 525:201–205, doi:10.1038/nature14967](https://www.nature.com/articles/nature14967)) across ~73,300 species ([Cazzolla Gatti et al. 2022, *PNAS* 119(6):e2115329119, doi:10.1073/pnas.2115329119](https://www.pnas.org/doi/10.1073/pnas.2115329119); correction doi:10.1073/pnas.2202784119).

**Explicit inference flag.** Points 1–8 are each individually sourced, but the *joint* claim — "these differences are attributable to the tree growth form as such, rather than to the particular species studied" — is **my synthesis**, not a statement any one source makes. A defensible definition should rest on the FAO growth-form criterion (which is a standard) plus the ENVO host-determined pattern (which is structural), and cite 1–3 as evidence that the class is microbiologically non-vacuous.

**A boundary decision the curator must make explicitly.** FAO's definition includes bamboos and palms, which lack secondary growth and true bark. Several of the differentia above (bark rhytidome, heartwood/sapwood) do not apply to them. Two options: (a) adopt FAO verbatim and accept palms/bamboo, treating the bark/heartwood evidence as typical rather than criterial; (b) restrict to "woody perennial with secondary growth" and lose FAO's exact wording. I recommend (a) — the definition should follow the standard, and BacDive's own usage (Reichenbach bark isolates, temperate broadleaf and conifer) makes the palm/bamboo edge case vanishingly rare in this data. This choice is mine to recommend, not a source's.

---

## 4. Sources

Ontology terms (all retrieved live from EBI OLS4, 2026-08-17):

- `ENVO:01001001` plant-associated environment — https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001001
- `ENVO:01001000`, `ENVO:01001002`, `ENVO:01001041`, `ENVO:01001055`, `ENVO:01001057`, `ENVO:01001058`, `ENVO:01001176`, `ENVO:01001179` — the organism-determined-environment family
- `ENVO:00000109` forested area, `ENVO:01001243` forest ecosystem, `ENVO:01001242` canopy, `ENVO:01001239` forest canopy, `ENVO:00000047` **obsolete** canopy, `ENVO:00000628` plant litter, `ENVO:01001121` plant matter, `ENVO:01000999` rhizosphere environment, `ENVO:00000300` scrubland area
- `BTO:0005516` wood (parent `BTO:0001468` xylem), `PO:0004518` bark, `PO:0006001` leaf, `PO:0000003` whole plant, `PO:0025161` plant resin, `AGRO:00010164` scattered trees
- ENVO paper of record: Buttigieg et al. 2013, *J. Biomed. Semantics* 4:43, doi:10.1186/2041-1480-4-43 — https://link.springer.com/article/10.1186/2041-1480-4-43 ; Buttigieg et al. 2016, *J. Biomed. Semantics* 7:57 — https://pmc.ncbi.nlm.nih.gov/articles/PMC5035502/
- ENVO NTR requirements (definitions must cite URLs/URIs): https://github.com/EnvironmentOntology/envo/wiki/Creating-good-definitions

Standards / reference vocabularies:

- FAO, *Terms and Definitions — FRA 2025*, Forest Resources Assessment Working Paper 194 — https://openknowledge.fao.org/server/api/core/bitstreams/a6e225da-4a31-4e06-818d-ca3aeadfd635/content
- AGROVOC concept c_7887 "trees" — https://agrovoc.fao.org/browse/agrovoc/en/page/c_7887
- BacDive isolation-source category system: Reimer et al. 2019, *Nucleic Acids Res.* 47:D631–D636, doi:10.1093/nar/gky879 — https://pmc.ncbi.nlm.nih.gov/articles/PMC6323973/ ; browsable at https://bacdive.dsmz.de/isolation-sources
- BacDive strain 18242 (DSM 52582), the triplet evidence — https://bacdive.dsmz.de/strain/18242

Primary microbiology:

- Arnold W, Gewirtzman J, et al. 2025. A diverse and distinct microbiome inside living trees. *Nature* 644(8078):1039–1048. doi:10.1038/s41586-025-09316-0. PMID 40770104 — https://www.nature.com/articles/s41586-025-09316-0
- Leung PM, Jeffrey L, Bay S, et al. 2025. Bark microbiota modulate climate-active gas fluxes in Australian forests. *Science*. doi:10.1126/science.adu2182 — https://www.science.org/doi/10.1126/science.adu2182 (accompanying Perspective: Gauci V., "Tree bark microbes for climate management", *Science* 2025)
- Kalkhoff et al. 2024. Biotic interactions outweigh abiotic factors as drivers of bark microbial communities in Central European forests. *ISME Communications* 4(1):ycae012. doi:10.1093/ismeco/ycae012 — https://academic.oup.com/ismecommun/article/4/1/ycae012/7589767
- 2024. Algae–fungi symbioses and bacteria–fungi co-exclusion drive tree species-specific differences in canopy bark microbiomes. *ISME J*. doi:10.1093/ismejo/wrae206 — https://academic.oup.com/ismej/article/doi/10.1093/ismejo/wrae206/7825411
- 2022. Tree size drives diversity and community structure of microbial communities on the bark of beech. *Front. For. Glob. Change* 5:858382. doi:10.3389/ffgc.2022.858382
- 2023. Mapping bark bacteria: initial insights of stemflow-induced changes in bark surface phyla. *Microbiol. Spectr.* doi:10.1128/spectrum.03562-23. PMID 37971233
- 2026. Barking up the right tree: ecological insights into the microbiome of bald cypress tree bark. *Environmental Microbiome*. doi:10.1186/s40793-026-00862-2. PMID 41645302
- Lambais MR, Crowley DE, Cury JC, Büll RC, Rodrigues RR. 2006. Bacterial diversity in tree canopies of the Atlantic forest. *Science* 312(5782):1917. doi:10.1126/science.1124696. PMID 16809531
- Lambais MR, Lucheta AR, Crowley DE. 2014. *Microb. Ecol.* 68(3):567–574. PMID 24889284 (phyllosphere/dermosphere/rhizosphere of trees are host-taxon dependent)
- Reichenbach H. 1999. The ecology of the myxobacteria. *Environ. Microbiol.* 1(1):15–21. doi:10.1046/j.1462-2920.1999.00016.x. PMID 11207714
- Dawid W. 2000. Biology and global distribution of myxobacteria in soils. *FEMS Microbiol. Rev.* 24(4):403–427. doi:10.1111/j.1574-6976.2000.tb00548.x. PMID 10978544
- Peterson JE. 1959. New species of myxobacteria from the bark of living trees. *Mycologia* 51:163–172 — https://www.tandfonline.com/doi/abs/10.1080/00275514.1959.12024789 ; Peterson JE. 1969. Isolation, cultivation and maintenance of the myxobacteria. In *Methods in Microbiology* 3B:185–210
- Crowther TW, et al. 2015. Mapping tree density at a global scale. *Nature* 525:201–205. doi:10.1038/nature14967
- Cazzolla Gatti R, Reich PB, et al. 2022. The number of tree species on Earth. *PNAS* 119(6):e2115329119. doi:10.1073/pnas.2115329119 (correction: doi:10.1073/pnas.2202784119)
- Groover AT. 2005. What genes make a tree a tree? *Trends Plant Sci.* 10(5):210–214. doi:10.1016/j.tplants.2005.03.001. PMID 15882652 (updated perspective: *Trends Plant Sci.* 2025, doi:10.1016/j.tplants.2025.10.010)
- Kitching RL. 2000. *Food Webs and Container Habitats: the natural history and ecology of phytotelmata.* Cambridge University Press (dendrotelmata)

---

## 5. Synonyms, and what not to conflate

**Exact / near-exact synonyms in real use:**
- `Tree` (BacDive Cat3 label — the source form; keep as `EXACT_SYNONYM`, source BacDive)
- `tree-associated environment` (the proposed ENVO-style label)
- `tree host`, `tree-associated habitat`, `woody host plant`
- `arborescent plant` (botanical); `trees` (AGROVOC `c_7887`, plural per thesaurus convention)

**Related but narrower — should be their own records / body-site terms, not synonyms:**
bark surface / bark microbiome; phyllosphere and canopy of a tree; sapwood; heartwood; cambium; tree rhizosphere; sap and exudate; resin; canker; dendrotelma (water-filled tree hole, a phytotelma subtype — Kitching 2000). Several already have records here (`leaf`, `plant resin`, `wood`).

**Commonly but wrongly treated as the same thing:**

| Confused with | Why it is different |
|---|---|
| **Forest / woodland / forested area** | Land cover at stand scale; BacDive has a separate `Forest` bin. Grounding `Tree` to `ENVO:00000109` would collapse two distinct source bins into one record. |
| **Wood / timber / lumber** | Material (`BTO:0005516`), detached and often processed; already a separate record from BacDive `Timber`. |
| **Bark** | A body-site on BacDive's *other* axis, co-asserted with `#Tree`, not equivalent to it. |
| **Deadwood / coarse woody debris / plant litter** | No longer a living host; a decomposition substrate with a different community regime (see PMID 31594501 on bark coverage and dead-wood decomposer assembly). |
| **Tree plantation / orchard / grove** | Managed land use. GOLD files *Terrestrial > Soil > Tree plantation*, and this repo has already recorded (decision on `habitatmech:GOLD.c3fa7fc4c2`) that a plantation is not `ENVO:01000951` *natural environment*. |
| **A tree taxon** (*Quercus*, *Populus*, Pinaceae) | "Tree" is a **polyphyletic growth form**, not a clade: woody growth "has been gained and lost multiple times in plant evolution", and the regulating genes "are not unique to woody plants" (Groover 2005). Consequently there is no NCBITaxon xref to attach — a difference from `Mollusca`/`Porifera`, where the taxon term exists and goes in `relation: xref`. |
| **MIxS `tree` (shading device)** | A built-environment enum value. Pure string collision. |
| **Phylogenetic tree, biliary tree, vascular tree** | Homonyms; `UBERON:0004999` and `CL:0002139` surface in naive lexical search. Worth an explicit "do not map" note, because a lexical grounder will hit them. |

---

## 6. Should this be a term at all?

**Yes — and this is the clean case, not the marginal one.**

It is not a process, quality, disease, or sampling artefact. It is a place where microbes live: a long-lived woody host with its own compartments and its own communities, demonstrated distinct from soil, leaves and roots ([*Science* 2025](https://www.science.org/doi/10.1126/science.adu2182); [*Nature* 2025](https://www.nature.com/articles/s41586-025-09316-0)). It is not a taxon term either — trees are a growth form (Groover 2005), so the `NOT_APPLICABLE`-for-taxon-terms concern does not even arise. Under this repo's rule that "an organism acting as a host IS a habitat", `Tree` is a host and therefore a habitat; and unlike `Mollusca` or `Porifera`, it has no taxon term that could tempt an over-claim.

Three points the curator should carry into the term request and the decision note:

1. **Do not ground to `ENVO:01001001` as identity.** It is genuinely broader — "determined by a green plant" — and this repo has already used it as the identity for a *different* BacDive bin. `habitatmech:BACDIVE.d3209b6b2d` (`Herbaceous-plants-Grass,Crops`) is `GROUND ENVO:01001001 ... BROAD`, producing `data/habitats/host_associated/plant_associated_environment.yaml` with `Herbaceous-plants-Grass,Crops` as an EXACT synonym of *plant-associated environment*. Grounding `Tree` there too would merge trees with grasses and crops on one record — precisely the collapse the existing term-request note warns against. **Worth filing separately:** the herbaceous record's `BROAD` self-grounding is the mirror-image over-claim and is arguably the one that should be revisited, since it makes a herb-specific bin the identity of the whole plant branch.

2. **Do not mirror the `Shrub-Scrub` precedent.** That Cat3 sibling — same axis, same partition — was grounded `CLOSE` to `ENVO:00000300` *scrubland area*, a land-cover term, which converts a plant-host growth form into an area of land. The analogous move here would be `forested area`, and it is wrong for two independent reasons (scale, and the pre-existing `Forest` bin). The inconsistency between the two siblings is worth a separate issue regardless of what happens to `Tree`.

3. **The request is a pattern extension, not a novel shape.** ENVO already carries `cnidarian-associated environment` and `environment associated with an aquatic invertebrate` under *animal-associated environment*. Filing `tree-associated environment` under *plant-associated environment* asks ENVO for the class of subdivision it already makes on the animal branch, on a branch that currently has **zero** children. That framing, plus the FAO growth-form definition and the *Science*/*Nature* 2025 evidence of community distinctness, is what an ENVO NTR needs (definitions must cite resolvable references — [ENVO wiki, Creating good definitions](https://github.com/EnvironmentOntology/envo/wiki/Creating-good-definitions)).

Until such a term exists, the current disposition on the record — `CONFIRM_UNGROUNDED`, minted identity `habitatmech:BACDIVE.3192a0f47e`, `parent_habitats: [ENVO:01001001]` — is correct as written.

*Note on the standing rule about external submissions: nothing here has been sent anywhere. If an ENVO new-term request is to be filed for this concept, that needs your explicit go-ahead for this specific request.*

## Citations

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC6323973/
2. https://bacdive.dsmz.de/strain/18242
3. https://www.ebi.ac.uk/ols4/api/search?q=%22tree%22&exact=true
4. https://enviromicro-journals.onlinelibrary.wiley.com/doi/10.1046/j.1462-2920.1999.00016.x
5. https://www.tandfonline.com/doi/abs/10.1080/00275514.1959.12024789
6. https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01001001
7. https://openknowledge.fao.org/server/api/core/bitstreams/a6e225da-4a31-4e06-818d-ca3aeadfd635/content
8. https://agrovoc.fao.org/browse/agrovoc/en/page/c_7887
9. https://academic.oup.com/ismecommun/article/4/1/ycae012/7589767
10. https://www.science.org/doi/10.1126/science.adu2182
11. https://www.nature.com/articles/s41586-025-09316-0
12. https://academic.oup.com/ismej/article/doi/10.1093/ismejo/wrae206/7825411
13. https://www.frontiersin.org/journals/forests-and-global-change/articles/10.3389/ffgc.2022.858382/full
14. https://journals.asm.org/doi/10.1128/spectrum.03562-23
15. https://www.science.org/doi/10.1126/science.1124696
16. https://www.nature.com/articles/nature14967
17. https://www.pnas.org/doi/10.1073/pnas.2115329119
18. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001001
19. https://link.springer.com/article/10.1186/2041-1480-4-43
20. https://pmc.ncbi.nlm.nih.gov/articles/PMC5035502/
21. https://github.com/EnvironmentOntology/envo/wiki/Creating-good-definitions
22. https://bacdive.dsmz.de/isolation-sources