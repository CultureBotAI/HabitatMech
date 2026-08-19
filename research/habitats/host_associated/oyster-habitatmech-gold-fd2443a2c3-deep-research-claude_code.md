---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T21:59:02.591236'
end_time: '2026-08-17T22:06:03.094114'
duration_seconds: 420.5
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Oyster
  habitat_identifier: habitatmech:GOLD.fd2443a2c3
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Mollusca > Oyster'
  assertions: '61'
  parent_terms: (none)
  xrefs: FOODON:03411224
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term FOODON:03411224 'oyster' attached as a parent. Organism-identity\
    \ screen (#109): grounded EXACT to FOODON:03411224 'oyster', which is a bivalve\
    \ mollusc \u2014 an organism, not a place. The screen that exists to catch exactly\
    \ this reported 0 for months because it tested only NCIT and mesh ancestry and\
    \ only the record's identity; widening it to UBERON:0000468 and to parent_habitats\
    \ surfaced this family. The GOLD path says host-associated, so the concept is\
    \ the environment the organism provides, which is the same family as the sponge,\
    \ nematode and reptile term requests. The organism term is kept as an xref (#99)\
    \ rather than an identity. (source concept habitatmech:GOLD.fd2443a2c3)"
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
  - claude-opus-5[1m]
  web_search_requests: 15
  num_turns: 32
  total_cost_usd: 3.020091
  session_id: 02f93696-e06a-4dfe-8292-e4fe885bce95
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 20
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Oyster
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.fd2443a2c3
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Mollusca > Oyster
- **Upstream assertion volume:** 61
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** FOODON:03411224

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term FOODON:03411224 'oyster' attached as a parent. Organism-identity screen (#109): grounded EXACT to FOODON:03411224 'oyster', which is a bivalve mollusc — an organism, not a place. The screen that exists to catch exactly this reported 0 for months because it tested only NCIT and mesh ancestry and only the record's identity; widening it to UBERON:0000468 and to parent_habitats surfaced this family. The GOLD path says host-associated, so the concept is the environment the organism provides, which is the same family as the sponge, nematode and reptile term requests. The organism term is kept as an xref (#99) rather than an identity. (source concept habitatmech:GOLD.fd2443a2c3)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Oyster** as a microbial habitat, with citations.

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

I'll research this now.

# Definition research: **Oyster** (`habitatmech:GOLD.fd2443a2c3`)

> **Proposed definition:** An environment associated with an aquatic invertebrate which is determined by a living oyster — a sessile, suspension-feeding marine or estuarine bivalve mollusc of the family Ostreidae — and which comprises the tissues, body fluids and shell surfaces of that animal as inhabited by microorganisms.

Genus term: `ENVO:01001176` *environment associated with an aquatic invertebrate*. If curation prefers the tighter genus, the intermediate class ("mollusc-associated environment" / "bivalve-associated environment") does **not** exist in ENVO — HabitatMech's own `habitatmech:GOLD.6acc0797e9` *Mollusca* and the GOLD `Bivalves` node occupy those slots, and the honest report is that the intermediate is missing (see §2).

---

## 1. What the concept denotes

**The reading the data means.** The single attestation is the GOLD path `Host-associated > Mollusca > Oyster` (61 assertions, GOLD ecosystem ids 5196/5197/5198, per `data/raw/`). Three structural facts from the GOLD table constrain the reading:

- **It is a leaf.** Unlike `Mollusca > Digestive system > …` or `Mollusca > Respiratory system > Gills > …`, the `Oyster` node has no children. GOLD carries anatomical resolution on a *parallel* branch keyed to the phylum, not underneath the host name. So a biosample classified to `Oyster` is **host-identified but not organ-resolved** — the whole animal is the stated habitat. *(Inference from the path structure, not a GOLD statement.)*
- **It is a host-organism node, sibling to another host-organism node.** `Host-associated > Mollusca > Bivalves` (59 assertions) sits alongside it rather than above it, even though oysters *are* bivalves. GOLD documents that its paths are sample-driven and periodically revised rather than a complete or strictly nested classification ([GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification)), so the non-nesting is a vocabulary artefact, not a claim that oysters are not bivalves.
- **It is `Host-associated`,** so the denotation is the living animal as an environment, not oyster meat as a commodity and not the water it came from.

**What is inside the concept.** The oyster body as a set of microbial habitats: gill, gut/stomach, digestive gland (hepatopancreas), mantle, pallial fluid, hemolymph, the extrapallial/calcifying fluid, and the inner and outer shell surfaces — the compartments that oyster-microbiome studies actually sample. All of these are documented as microbially distinct from one another within single animals ([Arfken et al. 2021, *mSphere*, doi:10.1128/mSphere.00227-21](https://journals.asm.org/doi/10.1128/msphere.00227-21); [King et al. 2012, *PLoS ONE*](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3520802/); [Pierce & Ward 2018, *J. Shellfish Res.* 37:793–806, doi:10.2983/035.037.0410](https://bioone.org/journals/journal-of-shellfish-research/volume-37/issue-4/035.037.0410/Microbial-Ecology-of-the-Bivalvia-with-an-Emphasis-on-the/10.2983/035.037.0410.short)).

**What is a neighbouring concept, not this one.**

| Neighbour | Why it is outside |
|---|---|
| **Oyster reef / oyster bed** | A biogenic environmental feature built largely of dead shell, hosting a whole benthic community. ENVO models this shape for mussels (`ENVO:01001386` *mussel reef*, `ENVO:01001380/01001381` neritic/oceanic mussel reef) and has `ENVO:01001899` *reef*, `ENVO:01000143` *marine reef* — but **no oyster reef term** (OLS search, ENVO, Aug 2026). The reef is the place the oysters are in; this concept is the oyster. |
| **Oyster as food** | `FOODON:03411224` *oyster* and `FOODON:00005711` *oyster material* — shucked meat sampled for *Vibrio* or norovirus is a food matrix, and the `Host-associated` prefix excludes it. |
| **The taxon** | `NCBITaxon:6563` Ostreidae, `FOODON:03412113` *bivalve*. A family is a class of organisms, not a place — the repo's #114/#99 line. |
| **Named oyster body parts** | GOLD already carries these under `Mollusca > Respiratory system > Gills`, `> Digestive system > Gut`, `> Integumentary system > Shell > Surface`, etc.; those ground to anatomy terms (BTO/UBERON) under the part/whole rule. |
| **Surrounding seawater and sediment** | Environmental, and empirically a different community (§3). |
| **Oyster larvae / spat** | `Host-associated > Mollusca > Larvae > Spat` is a separate life-stage concept, handled under the #112 rule. |
| **Hatchery / depuration tank water** | Engineered aquatic, even when the oysters are in it. |

**The label is ambiguous, in two ways worth recording.**

1. **Which family.** "Oyster" is a common name covering *true* oysters (Ostreidae — *Crassostrea*/*Magallana*, *Ostrea*, *Saccostrea*) and the unrelated *pearl* oysters (Pteriidae — *Pinctada*). FOODON's own definition says exactly this, and lists both families as synonyms of `FOODON:03411224`. Both have published microbiomes; pearl oyster work exists (e.g. multi-tissue profiling of *Pinctada margaritifera*, [PMC6624473](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6624473/)). GOLD's path does not disambiguate. **Recommendation:** scope the definition to Ostreidae (the overwhelming share of oyster microbiome and aquaculture sampling — see the FAO figure in §3) and state pearl oysters explicitly as an excluded/adjacent reading rather than silently absorbing them. *That the 61 GOLD assertions are predominantly Ostreidae is my inference from the literature and production balance, not something GOLD states; a curator can settle it by resolving the three GOLD ecosystem ids to their biosamples.*
2. **Which state of the animal.** Live host versus post-harvest shucked meat. `Host-associated` settles it for this record: live animal.

---

## 2. Genus — the broader kind

**Recommended: `ENVO:01001176` *environment associated with an aquatic invertebrate***
> "An environment which has its properties and composition largely determined by the presence of a metazoan which lacks a vetebral column and which has a habitat that is found in an aquatic environmental system." (ENVO, via OLS4; typo `vetebral` is in the source definition.)

It is a direct child of `ENVO:01001002` *animal-associated environment* and currently has **no children in ENVO** (OLS4 children endpoint, Aug 2026) — so an oyster-associated environment would be its first, alongside the sibling pattern already established at `ENVO:01001179` *cnidarian-associated environment* ("An environmental system determined by a cnidarian or part of a cnidarian"). That sibling is the precedent that matters: **ENVO does mint taxon-scoped `<X>-associated environment` classes**, so the term request this report supports is in-pattern, not novel modelling.

**Near-misses and why each fails:**

| Candidate | Verdict |
|---|---|
| `ENVO:01001002` *animal-associated environment* | Correct but two levels too broad; it is the genus the sibling Sponge record used. Use `ENVO:01001176` instead — it is narrower and still uncontroversially true of an oyster. |
| `ENVO:01001000` *environmental system determined by an organism* | Broader still (the grandparent line); the parent used on the Mollusca record. |
| `ENVO:01001179` *cnidarian-associated environment* | Sibling, not ancestor — asserts a cnidarian host. |
| `FOODON:03411224` *oyster* | The current xref. An organism/food material, not an environment; grounding to it was the #109 over-claim this record already corrected. Keep as `relation: xref`. |
| `ENVO:01000412` *circalittoral zone* | The **only** ENVO term whose text mentions oysters ("dominated by sessile animals such as oysters"), and it is a depth zone. Mentioning a taxon is not being about it. |
| `ENVO:01001386` *mussel reef* and the reef family | Biogenic structure built by bivalves; asserts reef-hood, geographic feature status and (for the mussel terms) mussel shell composition. A microbe in an oyster's gut is not in a reef. Also: the absence of an *oyster reef* term is a genuine ENVO gap and a **separate** term request from this one. |
| UBERON | Holds oyster *parts* (`gill`, `mantle`) but no whole-organism oyster class usable as an environment; using a part term here is exactly the part/whole error the CLAUDE.md rule names. |
| BTO | Molluscan tissue and cell terms only (e.g. `BTO:0005483` *molluscan catch muscle*); no organism-as-environment class. |
| **Missing intermediate** | No `mollusc-associated environment` / `bivalve-associated environment` anywhere in ENVO (OLS search for mollusc/mollusk/bivalve/shellfish in ENVO: **0 hits**). HabitatMech's `habitatmech:GOLD.6acc0797e9` *Mollusca* (784 assertions) and the GOLD `Bivalves` node (59) are the natural intermediates. If those are minted, **Oyster's parent should be the bivalve/mollusc concept**, with `ENVO:01001176` as the ENVO anchor above it. |

---

## 3. Differentia — what distinguishes it from its siblings

Ordered from most to least defensible; each is observable or measurable.

**(a) The host is a sessile, cemented, euryhaline suspension feeder of intertidal–shallow subtidal marine and estuarine waters.** FOODON's own definition: "salt-water bivalve molluscs that live in marine or brackish habitats… valves are highly calcified" ([FOODON:03411224](https://www.ebi.ac.uk/ols4/ontologies/foodon)). This is what separates the oyster habitat from other aquatic-invertebrate habitats (a cnidarian, a sponge, an ascidian).

**(b) The habitat is continuously inoculated and dose-loaded by high-volume filtration.** Clearance rates for *Crassostrea virginica* are reported at **1.5–10.0 L h⁻¹ g⁻¹ dry tissue weight** ([NOAA/NMFS Status Review of the Eastern Oyster, NMFS-F/SPO-88](https://spo.nmfs.noaa.gov/sites/default/files/TMSPO88.pdf), citing Stanley & Sellers 1986; Newell & Langdon 1996). The widely quoted "up to 50 gallons (≈190 L) per day" figure is a near-maximum laboratory rate; field estimates are more like 3–12.5 gal/day ([Bay Journal, 2020, quoting M. Gray, UMCES Horn Point](https://www.bayjournal.com/news/fisheries/pumped-up-performance-oysters-filtering-feat-overstated/article_bbe67d38-8f09-11ea-a5ab-5fd7465dee21.html)) — cite the NOAA range, not the outreach number.

**(c) It concentrates waterborne bacteria above ambient levels — measurably.** In Delaware Bay, presumptive *V. parahaemolyticus* peaked at **9.63 × 10³ CFU/g in oysters vs 1.85 × 10³ CFU/mL in seawater**, and potentially pathogenic (*tdh*/*trh*) isolates were **39 % of oyster isolates vs 15.6 % of seawater isolates** ([Parveen et al. 2020, *PLoS ONE*, doi:10.1371/journal.pone.0242229](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0242229)). FDA states the organism "concentrates, colonizes, and multiplies in the gut of filter-feeding molluscan shellfish" ([FDA *V. parahaemolyticus* QRA](https://www.fda.gov/food/risk-and-safety-assessments-food/quantitative-risk-assessment-public-health-impact-pathogenic-vibrio-parahaemolyticus-raw-oysters)). *Caveat: I found no source supporting a fixed ~100× concentration factor; measured ratios vary — do not put a multiplier in the definition.*

**(d) Despite (b) and (c), the community is host-selected, not a seawater sample.** Oyster tissue communities are consistently distinct from surrounding seawater and sediment, are tissue-specific, and are dominated by resident rather than transient members that track host population rather than immediate surroundings ([Unzueta-Martínez, Welch & Bowen 2022, *Front. Microbiol.* 12:828692, doi:10.3389/fmicb.2021.828692](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2021.828692/full); [Unzueta-Martínez & Bowen 2024, *Environ. Microbiol. Rep.*, doi:10.1111/1758-2229.70026](https://enviromicro-journals.onlinelibrary.wiley.com/doi/full/10.1111/1758-2229.70026)). **This is the single strongest justification that the concept is a habitat in its own right rather than a proxy for coastal seawater.**

**(e) It is internally compartmentalised, and characteristically so.** Alpha diversity is significantly higher in the inner shell than in gut, gill, mantle and pallial fluid; gut composition is distinct from all other tissues ([Arfken et al. 2021, doi:10.1128/mSphere.00227-21](https://journals.asm.org/doi/10.1128/msphere.00227-21)). Stomach communities can be overwhelmingly *Mycoplasma*-related Mollicutes while the gut of the same animals is far richer (44 OTUs/12 phyla core vs 5 OTUs/3 phyla) ([King et al. 2012, PMC3520802](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3520802/)). The calcifying/extrapallial fluid is a further distinct niche dominated by Pseudomonadota, Planctomycetota and Bacteroidota ([*Appl. Environ. Microbiol.* 2024, doi:10.1128/aem.01094-24](https://journals.asm.org/doi/full/10.1128/aem.01094-24)).

**(f) Hemolymph is an internal *aquatic* niche, not a sterile compartment.** It hosts bacteria, protists and viruses simultaneously and behaves as a within-host ecosystem ([Dupont et al. 2020, *Animal Microbiome* 2:12, doi:10.1186/s42523-020-00032-w](https://animalmicrobiome.biomedcentral.com/articles/10.1186/s42523-020-00032-w)); its diversity correlates positively with seawater temperature and shifts under thermal stress and *Vibrio* challenge ([Lokmer & Wegner 2015, *ISME J* 9:670–682, doi:10.1038/ismej.2014.160](https://www.nature.com/articles/ismej2014160)). This is a useful contrast with terrestrial-host habitats: the oyster's internal fluid is a seawater-derived, temperature-tracking medium.

**(g) Functional signature: enriched denitrification relative to surrounding sediment.** Digestive-gland and shell microbiomes are distinct from each other and from adjacent reef sediment, with denitrifiers relatively more abundant in oysters and shells than in sediments ([Arfken et al. 2017, *PLoS ONE* 12:e0185071](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5608302/)).

**(h) Microbial state is coupled to host disease.** Pacific Oyster Mortality Syndrome is a two-step polymicrobial disease: OsHV-1 µVar infects haemocytes and immunocompromises the host, followed by fatal opportunistic bacteraemia ([de Lorgeril et al. 2018, *Nat. Commun.* 9:4215, doi:10.1038/s41467-018-06659-3](https://www.nature.com/articles/s41467-018-06659-3)). Useful context for the record; **do not put it in the definition** — a definition should not assert a disease state.

**Contrast with the nearest sibling habitats** *(my synthesis of the sources above; state as rationale, not as a cited claim)*: unlike sponge-associated environments, the oyster habitat is organ-compartmentalised with a circulatory fluid; unlike cnidarian-associated environments, it has no photosymbiotic algal partner structuring it; unlike chemosymbiotic bivalves (*Bathymodiolus*, *Solemya*), oysters host no gill-endosymbiont system, so their gill community is an open, environment-exchanging one rather than a vertically maintained symbiosis.

**Why the term earns its keep at all:** cupped oysters (*Crassostrea* spp.) were the **second-largest aquaculture species item globally at 6.2 million tonnes in 2022** ([FAO SOFIA 2024](https://www.fao.org/3/cd0683en/online/sofia/2024/world-fisheries-aquaculture-production.html)) — so a large, growing, and food-safety-relevant body of sampling resolves to exactly this host and no finer.

---

## 4. Sources

Ontology lookups (EBI OLS4, queried 2026-08-17): `ENVO:01001176`, `ENVO:01001002`, `ENVO:01001179`, `ENVO:01001000`, `ENVO:01000412`, reef family, `FOODON:03411224`, `NCBITaxon:6563`. Searches for `mollusc|mollusk|bivalve|shellfish` and `oyster reef` in ENVO returned **0** matching classes.

Primary and reference literature:

- Pierce ML & Ward JE (2018) *Microbial Ecology of the Bivalvia, with an Emphasis on the Family Ostreidae.* J Shellfish Res 37(4):793–806. doi:[10.2983/035.037.0410](https://doi.org/10.2983/035.037.0410) — the authoritative review.
- Arfken A et al. (2021) *Microbiome Analysis Reveals Diversity and Function of Mollicutes Associated with the Eastern Oyster.* mSphere 6:e00227-21. doi:[10.1128/mSphere.00227-21](https://journals.asm.org/doi/10.1128/msphere.00227-21) (PMID 33980678)
- Arfken A et al. (2017) *Denitrification potential of the eastern oyster microbiome…* PLoS ONE 12(9):e0185071. [PMC5608302](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5608302/)
- King GM et al. (2012) *Analysis of Stomach and Gut Microbiomes of the Eastern Oyster.* PLoS ONE 7(12):e51475. [PMC3520802](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3520802/)
- Unzueta-Martínez A, Welch H, Bowen JL (2022) *Determining the Composition of Resident and Transient Members of the Oyster Microbiome.* Front Microbiol 12:828692. doi:[10.3389/fmicb.2021.828692](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2021.828692/full)
- Unzueta-Martínez A & Bowen JL (2024) *Persistent tissue-specific resident microbiota in oysters across a broad geographical range.* Environ Microbiol Rep. doi:[10.1111/1758-2229.70026](https://enviromicro-journals.onlinelibrary.wiley.com/doi/full/10.1111/1758-2229.70026)
- Pierce ML & Ward JE (2019) *Gut Microbiomes of the Eastern Oyster and the Blue Mussel…* mSphere 4:e00730-19. doi:[10.1128/mSphere.00730-19](https://journals.asm.org/doi/10.1128/msphere.00730-19)
- Lokmer A & Wegner KM (2015) *Hemolymph microbiome of Pacific oysters…* ISME J 9:670–682. doi:[10.1038/ismej.2014.160](https://www.nature.com/articles/ismej2014160) (PMID 25180968)
- Dupont S et al. (2020) *Oyster hemolymph is a complex and dynamic ecosystem…* Animal Microbiome 2:12. doi:[10.1186/s42523-020-00032-w](https://animalmicrobiome.biomedcentral.com/articles/10.1186/s42523-020-00032-w) (2020-04-28)
- de Lorgeril J et al. (2018) *Immune-suppression by OsHV-1 viral infection causes fatal bacteraemia in Pacific oysters.* Nat Commun 9:4215. doi:[10.1038/s41467-018-06659-3](https://www.nature.com/articles/s41467-018-06659-3)
- *Taxonomic diversity and functional potential of microbial communities in oyster calcifying fluid* (2024) Appl Environ Microbiol. doi:[10.1128/aem.01094-24](https://journals.asm.org/doi/full/10.1128/aem.01094-24)
- Parveen S et al. (2020) *Assessment of Vibrio parahaemolyticus levels in oysters and seawater in Delaware Bay…* PLoS ONE. doi:[10.1371/journal.pone.0242229](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0242229)
- NOAA/NMFS, *Status Review of the Eastern Oyster (Crassostrea virginica)*, NMFS-F/SPO-88. [PDF](https://spo.nmfs.noaa.gov/sites/default/files/TMSPO88.pdf)
- FDA, *Quantitative Risk Assessment on the Public Health Impact of Pathogenic Vibrio parahaemolyticus in Raw Oysters.* [FDA](https://www.fda.gov/food/risk-and-safety-assessments-food/quantitative-risk-assessment-public-health-impact-pathogenic-vibrio-parahaemolyticus-raw-oysters)
- FAO, *The State of World Fisheries and Aquaculture 2024* — production by species item. [FAO](https://www.fao.org/3/cd0683en/online/sofia/2024/world-fisheries-aquaculture-production.html)
- JGI GOLD, *Ecosystem Classification* (five-level scheme; Ivanova et al., PMID 20653767). [gold.jgi.doe.gov](https://gold.jgi.doe.gov/ecosystem_classification)

**Explicitly marked as inference, not sourced:** that GOLD's `Oyster` node denotes whole-animal/organ-unspecified samples (read off the path structure); that the 61 assertions are predominantly Ostreidae rather than Pteriidae; the sibling-contrast paragraph in §3. The GSC **MIxS host-associated environmental package** is the checklist such a sample is described with — noted as a pointer; I did not fetch and verify its current field list in this pass.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**
- oyster-associated environment; oyster host; oyster microbiome habitat (informal); Ostreidae-associated environment
- By species, all of which resolve here: *Crassostrea virginica* (eastern/American oyster), *Magallana gigas* = *Crassostrea gigas* (Pacific/cupped oyster; FAO reports it within "cupped oysters nei"), *Ostrea edulis* (European flat oyster), *Ostrea lurida* (Olympia oyster), *Saccostrea glomerata* (Sydney rock oyster)
- GOLD-side: `Host-associated > Mollusca > Oyster`

**Commonly but wrongly treated as the same thing**
1. **Oyster reef / oyster bed / shellfish bed** — an environmental feature and benthic community; ENVO has no term for it (a separate, legitimate request). A sample from reef sediment is not from this habitat.
2. **`FOODON:03411224` *oyster*, `FOODON:00005711` *oyster material*** — the organism and the food material. Retain as `relation: xref` per #99; the label match here is what produced the original #109 over-claim.
3. **`NCBITaxon:6563` Ostreidae / `FOODON:03412113` bivalve / `FOODON:03412112` mollusc** — taxon groupings. Worth adding `NCBITaxon:6563` as a second xref: it is more precise about *which* oysters than FOODON's family-straddling term.
4. **Pearl oysters (*Pinctada*, Pteriidae)** — a different family under the same common name; excluded by the recommended Ostreidae scoping, and a distinct habitat if ever needed.
5. **Oyster mushroom (*Pleurotus*)** — pure lexical collision; FOODON contains several such terms and a label match will find them.
6. **Oyster organs as anatomy terms** — `gill`, `mantle`, `digestive gland`, `hemolymph`; these are *parts* and ground normally on GOLD's `Mollusca > <organ system>` branch. Grounding *this* record to any of them would repeat the part/whole error.
7. **Oyster larvae and spat** — `Mollusca > Larvae > Spat`; a life-stage concept under the #112 rule, not this one.
8. **"Shellfish"** in the regulatory sense — FOODON notes it is a regulatory grouping of filter-feeding molluscs; it is a food-safety category, not a habitat kind.
9. **Coastal seawater the oyster filtered** — empirically a different community (§3d); conflating the two is the specific error the resident/transient work rules out.
10. **Oyster aquaculture gear, hatchery tanks, depuration water** — engineered aquatic environments.

---

## 6. Should this be a term at all?

**Yes — mint it.** It is a host organism acting as a habitat, which is the case CLAUDE.md settles: "A host is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment." It is not a disease, quality, process or procedure, so `NOT_APPLICABLE` would be the wrong and stronger claim; and it is not a bare taxon term, because the concept denotes the animal-as-place, with `FOODON:03411224` / `NCBITaxon:6563` staying as xrefs. The existing decision (`CONFIRM_UNGROUNDED`, xref) is correct as it stands; this report supports the term request that follows from it.

Three caveats a curator should carry into the request:

1. **Scope the definition to Ostreidae** and say so, rather than inheriting FOODON's two-family common name silently. Otherwise the term asserts a grouping (Ostreidae + Pteriidae) that is polyphyletic and that no source treats as one habitat.
2. **The genus chain has a hole.** `ENVO:01001176` is the nearest real ENVO ancestor, but the natural parent is a mollusc- or bivalve-associated environment that does not exist. Requesting `oyster-associated environment` alone leaves the intermediate unrequested; requesting *mollusc-associated environment* (or *bivalve-associated environment*) at the same time would give this record, `Mollusca` (784 assertions) and `Bivalves` (59) a coherent chain in one pass. Flagging this to ENVO as a small family of requests, in the shape `cnidarian-associated environment` already establishes, is the higher-yield move.
3. **`Oyster` and `Bivalves` are siblings in GOLD but not in reality.** Whatever HabitatMech mints should record the true subsumption (oyster ⊂ bivalve ⊂ mollusc) rather than mirroring GOLD's flat arrangement — otherwise the corpus reproduces an upstream vocabulary artefact as an ontological claim.

**Sources:** [BioOne — Pierce & Ward 2018](https://bioone.org/journals/journal-of-shellfish-research/volume-37/issue-4/035.037.0410/Microbial-Ecology-of-the-Bivalvia-with-an-Emphasis-on-the/10.2983/035.037.0410.short) · [mSphere — Arfken 2021](https://journals.asm.org/doi/10.1128/msphere.00227-21) · [PMC5608302 — Arfken 2017](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5608302/) · [PMC3520802 — King 2012](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3520802/) · [Frontiers — Unzueta-Martínez 2022](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2021.828692/full) · [Wiley — Unzueta-Martínez 2024](https://enviromicro-journals.onlinelibrary.wiley.com/doi/full/10.1111/1758-2229.70026) · [mSphere — Pierce & Ward 2019](https://journals.asm.org/doi/10.1128/msphere.00730-19) · [ISME J — Lokmer & Wegner 2015](https://www.nature.com/articles/ismej2014160) · [Animal Microbiome — Dupont 2020](https://animalmicrobiome.biomedcentral.com/articles/10.1186/s42523-020-00032-w) · [Nat Commun — de Lorgeril 2018](https://www.nature.com/articles/s41467-018-06659-3) · [AEM — oyster calcifying fluid 2024](https://journals.asm.org/doi/full/10.1128/aem.01094-24) · [PLoS ONE — Delaware Bay Vibrio](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0242229) · [NOAA NMFS-F/SPO-88](https://spo.nmfs.noaa.gov/sites/default/files/TMSPO88.pdf) · [FDA Vibrio QRA](https://www.fda.gov/food/risk-and-safety-assessments-food/quantitative-risk-assessment-public-health-impact-pathogenic-vibrio-parahaemolyticus-raw-oysters) · [FAO SOFIA 2024](https://www.fao.org/3/cd0683en/online/sofia/2024/world-fisheries-aquaculture-production.html) · [JGI GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification) · [Bay Journal — filtration caveat](https://www.bayjournal.com/news/fisheries/pumped-up-performance-oysters-filtering-feat-overstated/article_bbe67d38-8f09-11ea-a5ab-5fd7465dee21.html) · [PMC6624473 — pearl oyster multi-tissue](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6624473/)

## Citations

1. https://gold.jgi.doe.gov/ecosystem_classification
2. https://journals.asm.org/doi/10.1128/msphere.00227-21
3. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3520802/
4. https://bioone.org/journals/journal-of-shellfish-research/volume-37/issue-4/035.037.0410/Microbial-Ecology-of-the-Bivalvia-with-an-Emphasis-on-the/10.2983/035.037.0410.short
5. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6624473/
6. https://www.ebi.ac.uk/ols4/ontologies/foodon
7. https://spo.nmfs.noaa.gov/sites/default/files/TMSPO88.pdf
8. https://www.bayjournal.com/news/fisheries/pumped-up-performance-oysters-filtering-feat-overstated/article_bbe67d38-8f09-11ea-a5ab-5fd7465dee21.html
9. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0242229
10. https://www.fda.gov/food/risk-and-safety-assessments-food/quantitative-risk-assessment-public-health-impact-pathogenic-vibrio-parahaemolyticus-raw-oysters
11. https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2021.828692/full
12. https://enviromicro-journals.onlinelibrary.wiley.com/doi/full/10.1111/1758-2229.70026
13. https://journals.asm.org/doi/full/10.1128/aem.01094-24
14. https://animalmicrobiome.biomedcentral.com/articles/10.1186/s42523-020-00032-w
15. https://www.nature.com/articles/ismej2014160
16. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5608302/
17. https://www.nature.com/articles/s41467-018-06659-3
18. https://www.fao.org/3/cd0683en/online/sofia/2024/world-fisheries-aquaculture-production.html
19. https://doi.org/10.2983/035.037.0410
20. https://journals.asm.org/doi/10.1128/msphere.00730-19