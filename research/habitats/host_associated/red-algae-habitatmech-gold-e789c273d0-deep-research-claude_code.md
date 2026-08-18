---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T21:22:49.538073'
end_time: '2026-08-17T21:32:20.479632'
duration_seconds: 570.94
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Red algae
  habitat_identifier: habitatmech:GOLD.e789c273d0
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Algae > Red algae'
  assertions: '73'
  parent_terms: (none)
  xrefs: FOODON:03411743
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term FOODON:03411743 'red algae' attached as a parent. Non-habitat screen\
    \ (#12): grounded EXACT to FOODON:03411743 'red algae', which FOODON uses for\
    \ the TAXON \u2014 red algae is defined there as 'one of the oldest groups of\
    \ eukaryotic algae, and one of the largest phyla' \u2014 not for a habitat. An\
    \ organism group is not a place, and the GOLD path says host-associated, so the\
    \ concept is the environment the alga provides. Same family as the sponge, nematode\
    \ and reptile requests. The FOODON term is kept as an xref (#99), which records\
    \ what the label matched without asserting the record is a phylum. (source concept\
    \ habitatmech:GOLD.e789c273d0)"
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
  web_search_requests: 17
  num_turns: 40
  total_cost_usd: 4.192077000000001
  session_id: 42d398fd-8004-4432-a790-ba8235310003
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 22
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Red algae
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.e789c273d0
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Algae > Red algae
- **Upstream assertion volume:** 73
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** FOODON:03411743

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term FOODON:03411743 'red algae' attached as a parent. Non-habitat screen (#12): grounded EXACT to FOODON:03411743 'red algae', which FOODON uses for the TAXON — red algae is defined there as 'one of the oldest groups of eukaryotic algae, and one of the largest phyla' — not for a habitat. An organism group is not a place, and the GOLD path says host-associated, so the concept is the environment the alga provides. Same family as the sponge, nematode and reptile requests. The FOODON term is kept as an xref (#99), which records what the label matched without asserting the record is a phylum. (source concept habitatmech:GOLD.e789c273d0)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Red algae** as a microbial habitat, with citations.

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

# Red algae (habitatmech:GOLD.e789c273d0) — definition research

> **Proposed definition:** An environmental system determined by an organism which is determined by a red alga (Rhodophyta), comprising the thallus surface, internal tissues and diffusive boundary layer available to microbial colonists, and distinguished by a cell wall of sulfated galactans (agars, carrageenans, porphyran) as the dominant colonisable and degradable substrate.

If that reads long, it is because one class is missing between this concept and its genus: ENVO has `plant-associated environment`, `animal-associated environment`, `fungi-associated environment` and `cnidarian-associated environment`, but **no algae-associated environment**. The clean form is `An algae-associated environment which is determined by a red alga (Rhodophyta), whose cell wall is composed of sulfated galactans rather than the alginates of brown algae or the ulvans of green algae.` That requires the sibling record for *Algae* (`habitatmech:GOLD.02383c20a7`) to carry the intermediate class. Recommending the intermediate is more useful than lengthening this sentence.

---

## 1. What the concept denotes

**The reading the data means.** The GOLD path is `Host-associated > Algae > Red algae`, and the node has five children in the extracted GOLD table: `Sporeling`, `Blade`, `Ectosymbionts`, `Embryo`, `Whole body` (`data/raw/gold_ecosystem_paths.tsv`). Those children are decisive: a classification that files *Blade* (a thallus part), *Whole body*, and two life stages under a node is treating the node as **an organism serving as host**, not as a taxon and not as a water body. GOLD's ecosystem classification is explicitly a five-level habitat hierarchy — Ecosystem → Ecosystem Category → Ecosystem Type → Ecosystem Subtype → Specific Ecosystem — in which `Host-associated` is a top-level ecosystem alongside `Environmental` and `Engineered` ([Mukherjee et al. 2023, *Nucleic Acids Research* 51:D957–D963, doi:10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974)).

So the thing a sample is taken from is **a living red alga**, and in practice one of three physical compartments:

- **The thallus surface** — the epiphytic/epibiotic biofilm, sampled by swabbing the tissue ([Nahor et al. 2024, *Sci Rep* 14:18631, doi:10.1038/s41598-024-69362-y](https://doi.org/10.1038/s41598-024-69362-y)) or by vortexing thallus pieces in sterile seawater and filtering at 0.22 µm ([Gu et al. 2023, *IJMS* 24:11019, doi:10.3390/ijms241311019](https://doi.org/10.3390/ijms241311019)). Wahl et al. call this compartment the host's "second skin": macroalgae are especially susceptible to epibiosis and are typically covered by diverse microbial communities of bacteria, microalgae, fungi and protists ([Wahl et al. 2012, *Front Microbiol* 3:292, doi:10.3389/fmicb.2012.00292](https://doi.org/10.3389/fmicb.2012.00292)).
- **The internal tissue** — endophytic bacteria within the thallus, e.g. 16S-identified endophytes of *Kappaphycus alvarezii*, where healthy tissue was dominated by *Bacillus*, *Cytobacillus* and *Priestia* while *Vibrio* and *Micrococcus* occurred only in diseased thalli ([Data in Brief, PMC10694040](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10694040/)). Bacterial penetration of the epidermal layer is documented in *Delisea pulchra* bleaching ([Case et al. 2011, *Environ Microbiol*, PMID 20946533](https://pubmed.ncbi.nlm.nih.gov/20946533/)).
- **The boundary layer / exudate zone** immediately around the thallus, chemically distinct from bulk seawater; CCA species-specific exudates measurably restructure adjacent bacterioplankton ([Quinlan et al. 2019, *Front Microbiol* 10:2397, doi:10.3389/fmicb.2019.02397](https://doi.org/10.3389/fmicb.2019.02397)).

**Inside the concept:** any life stage or part of any red alga acting as host — fleshy foliose blades (*Porphyra*/*Neopyropia*, *Palmaria*), branched turf and understorey species (*Gracilaria*, *Gelidium*, *Grateloupia*, *Laurencia*, *Delisea*), and calcified crustose coralline algae (*Hydrolithon*, *Neogoniolithon*, *Amphiroa*), plus sporelings and embryos.

**Neighbouring concepts, outside it:**

| Neighbour | Why it is outside |
|---|---|
| Brown algae (`habitatmech:GOLD.3e4ecbed63`), green algae (`habitatmech:GOLD.184cc9e802`) | Sibling hosts under the same parent; different wall chemistry and, empirically, different epiphytic communities (§3) |
| Surrounding seawater / sediment | Sampled as controls precisely because they are different habitats; most seawater ASVs do not appear on the algae ([Nahor et al. 2024](https://doi.org/10.1038/s41598-024-69362-y); [Lu et al. 2023, *Microbiome* 11:126, doi:10.1186/s40168-023-01559-1](https://doi.org/10.1186/s40168-023-01559-1)) |
| The reef or rocky substratum a coralline alga encrusts | ENVO:01000050 `marine subtidal rocky reef biome` is a biome that *contains* turf-forming calcareous red algae; the biome is not the alga |
| A seaweed farm | ENVO:03600074 `aquaculture farm`, ENVO:01001252 `seaweed farming process` — the engineered setting, not the host |
| The gut of an animal that eats red algae | The porphyranase-carrying *Bacteroides plebeius* lives in a human gut, not on an alga ([Hehemann et al. 2010, *Nature* 464:908–912, doi:10.1038/nature08937](https://doi.org/10.1038/nature08937)) |
| Nori sheets, agar, carrageenan | Food and processed-material readings; FOODON's territory |

**Genuine ambiguity in the label, stated rather than resolved silently.** "Red algae" has at least four readings:

1. **Macroalgal (seaweed) thallus as host** — the reading the GOLD path supports, and the reading that carries the 73 assertions.
2. **Unicellular red algae** — Cyanidiophyceae (11 living species), Porphyridiophyceae (9), Rhodellophyceae (8) out of 7,276 living Rhodophyta ([Guiry 2024, *J Phycol*, Table 7, doi:10.1111/jpy.13431](https://doi.org/10.1111/jpy.13431)). These are microorganisms in their own right; their setting is acidic hot springs and endolithic rock at pH 0.5–3.0 and 50–56 °C ([Yoon et al. 2006, *BMC Evol Biol* 6:78, doi:10.1186/1471-2148-6-78](https://doi.org/10.1186/1471-2148-6-78); [Gross et al. 1998, *Eur J Phycol* 33:25–31, doi:10.1080/09670269810001736503](https://doi.org/10.1080/09670269810001736503)). GOLD would file that as an environmental, not host-associated, habitat. It is 0.4% of the phylum and is **not** what a `Host-associated` path means.
3. **The taxon Rhodophyta** — what FOODON:03411743 actually names, and what the curation note already rejects.
4. **Red algal food/hydrocolloid material** — FOODON:03412266 `seaweed`, FOODON:00001184 `algae material`.

Reading 1 is the one to define. Reading 2 deserves a one-line exclusion in the definition's comment, because "red algae" is not obviously restricted to macroalgae to a reader.

---

## 2. Genus — the broader kind

**Recommended genus: `ENVO:01001000` "environmental system determined by an organism"** — *"An environmental system which is determined by a living organism"*, exact synonym *host-associated environment*. It is present in the vendored slice (`data/raw/ontology_terms.tsv`), so a `GROUND_AS_PARENT`-style attachment passes the label check. This is also the parent already recorded on the sibling *Algae* record.

**The intermediate class that does not exist.** ENVO's children of `ENVO:01001000` follow one pattern — `plant-associated environment` (ENVO:01001001), `animal-associated environment` (ENVO:01001002), `fungi-associated environment` (ENVO:01001041), `cnidarian-associated environment` (ENVO:01001179), plus part-level variants such as `environment associated with a plant part or small plant` (ENVO:01001057) and `environment associated with an aquatic invertebrate` (ENVO:01001176). An OLS4 query of ENVO for `algae-associated` returns **zero** results (`https://www.ebi.ac.uk/ols4/api/search?q=algae-associated&ontology=envo`, checked 2026-08-17), and a query for `algae`/`algal` returns only bloom terms, `algal material`, `raceway pond` and `periphytic biofilm`. Algae — the third most species-rich plant-like grouping on Earth, ~50,589 living species ([Guiry 2024](https://doi.org/10.1111/jpy.13431)) — have no organism-determined-environment class. That gap is the real finding of this section.

**Near-misses and why each fails:**

| Term | Why it is not a match |
|---|---|
| `ENVO:01001001` plant-associated environment | Definition says *"determined by a green plant"*; the synonym is literally *Viridiplantae-associated environment*. Red algae are Archaeplastida but not Viridiplantae. Worth recording because AlgaeBase assigns Rhodophyta to kingdom **Plantae** ([Guiry 2024, Table 2](https://doi.org/10.1111/jpy.13431)), so a label-level match on "plant" is exactly the kind of over-claim #99 exists to prevent. |
| `ENVO:01001057` environment associated with a plant part or small plant | Same green-plant restriction, and part-level — narrower than a whole-host concept. |
| `ENVO:01001189` algal material | A *material entity* ("organic material primarily composed of living or dead algae, along with their exudates"), not an environmental system. Right stuff, wrong upper category. Usable in an axiom (*has part some algal material*), not as genus. |
| `ENVO:03605000` periphytic biofilm | "Biofilm consisting of a mixture of algae, cyanobacteria, microbes, and detritus" — here the alga is a *member* of the community, not the host that determines the environment. Inverts the relation. |
| `ENVO:2000004` algal bloom / `ENVO:01000057` marine algal bloom | Features arising from planktonic microalgal proliferation in a water body; not host-associated. Note `marine algal bloom` carries the synonym *red tide* — a false friend (§5). |
| `ENVO:01000411` infralittoral zone | A marine zone "dominated by algae" — a place where red algae live, not the alga as a place. |
| `ENVO:01000050` marine subtidal rocky reef biome | Mentions "turf-forming calcareous red algae" in its definition; a biome, orders of magnitude coarser. |
| `FOODON:03411743` red algae | The taxon (already the xref). An organism group is not a place. |
| `FOODON:03412266` seaweed / `FOODON:00001184` algae material | Polyphyletic organism grouping and material respectively; also both broader than Rhodophyta. |
| PO | Plant Ontology's scope is green plants; it holds no red algal anatomy. |
| UBERON | Animal anatomy; no thallus. |
| BTO | Holds red-algal *structures and cultures* only — `BTO:0004989` monospore, `BTO:0001290` sporocarp, `BTO:0005595` microplantlet suspension culture. Anatomy and culture systems, not environments. |

---

## 3. Differentia — what distinguishes it from its siblings

The sibling hosts under an algae-associated genus are brown algae and green algae. Four observable properties separate red algae, in decreasing order of how well they are sourced.

### 3a. Cell-wall chemistry — the strongest, best-supported differentia

Red algal walls are built on **sulfated galactans of the agar and carrageenan families**: "the commonest and most abundant cell wall constituents encountered in the Rhodophyta are families of galactans referred to informally as the agars and carrageenans"; cellulose is present in most species but usually **<10%**, and polysaccharides make up roughly **40–50% of cell-wall dry weight**; yields reach agar up to 52% dw and carrageenan up to 75% dw ([Usov 2011, *Adv Carbohydr Chem Biochem* 65:115–217, PMID 21763512](https://pubmed.ncbi.nlm.nih.gov/21763512/)). Agarans have a β(1→3)-D-galactose / α(1→4)-3,6-anhydro-**L**-galactose backbone; carrageenans use the **D**-enantiomer and carry 20–50% sulfate, giving κ-, ι- and λ- forms. *Porphyra*/*Neopyropia* carry the hybrid sulfated galactan **porphyran**. Some Rhodophyta substitute sulfated mannans or neutral xylans (same source) — a real caveat against over-claiming universality.

This is not merely chemistry; it is the differentiating **microbial resource**, and it shows up directly in the metagenomes of red algal surfaces. Nine red algae from Antarctica, Indonesia and China yielded 939 (China) / 1,076 (Antarctica) / 41 (Indonesia) agarase genes in GH16, GH50, GH86 and GH117, and 759 / 940 / 33 carrageenase genes in GH16 and GH82 ([Gu et al. 2023, doi:10.3390/ijms241311019](https://doi.org/10.3390/ijms241311019)). The porphyranase story is the canonical demonstration that this substrate defines a distinct enzymatic niche: β-porphyranases PorA and PorB from the red-algal-associated marine Bacteroidetes *Zobellia galactanivorans* were active only against *Porphyra* extracts, and porphyranase genes were found solely in marine bacterial genomes — the sole exception being the human gut symbiont *Bacteroides plebeius* ([Hehemann et al. 2010, doi:10.1038/nature08937](https://doi.org/10.1038/nature08937)).

Contrast for the definition's differentia: brown algae are alginate/fucoidan/laminarin, green algae are ulvan. *(The contrast itself is standard phycology; the red-algal half is cited above. The brown/green half is asserted here from general reference knowledge and should be cited from the corresponding sibling reports rather than from this one.)*

### 3b. Storage and low-molecular-weight carbon

Red algae store **floridean starch** — an α-1,4 glucan with frequent α-1,6 branches, average chain ~15 glucose residues, stored in the *cytoplasm* rather than the plastid — and the galactosylglycerol **floridoside** (2-O-α-D-galactopyranosylglycerol), though floridoside "is by no means universal in the Rhodophyta" ([Usov 2011](https://pubmed.ncbi.nlm.nih.gov/21763512/); [Simon-Colin et al. 2008, *Biochimie*, doi:10.1016/j.biochi.2008.09.008](https://doi.org/10.1016/j.biochi.2008.09.008)). **Inference, not sourced here:** that these compounds are a significant carbon source for surface microbes is plausible and consistent with the exudate work cited in §1, but I did not find a study measuring floridoside uptake by red-algal epibionts. Do not put it in the definition.

### 3c. Halogenated chemical defence structuring the surface community

Red algae are unusually rich producers of halogenated metabolites that act *on the surface*, which is a defensible differentia at genus level even though it is not universal:

- *Asparagopsis armata* produces bromoform (0.58–4.3% of dry weight) and dibromoacetic acid (0.02–2.6% dw), stores them in gland cells with a release mechanism to the surface, and — the ecological test — **epiphytic bacterial densities were significantly lower on algae producing these metabolites**, while bacteria isolated from those surfaces were more tolerant of them than bacteria from metabolite-free algae ([Paul et al. 2006, *Mar Ecol Prog Ser* 306:87–101, doi:10.3354/meps306087](https://doi.org/10.3354/meps306087)).
- *Delisea pulchra* uses halogenated furanones to inhibit bacterial colonisation; furanone concentrations fall in summer, and reduced furanone plus elevated temperature (24 °C vs 19 °C) permits *Nautella italica* R11 and *Phaeobacter gallaeciensis* LSS9 to biofilm, invade the epidermis and bleach the thallus ([Case et al. 2011, PMID 20946533](https://pubmed.ncbi.nlm.nih.gov/20946533/); [Fernandes et al. 2011, *PLoS ONE* 6:e27387, doi:10.1371/journal.pone.0027387](https://doi.org/10.1371/journal.pone.0027387)).
- *Laurencia* spp. are a prolific source of brominated C15-acetogenins and terpenoids with documented antibacterial activity ([Vairappan et al. 2010, *Mar Drugs* 8:1743–1749, PMC2901821](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2901821/)).

### 3d. Community composition measurably keyed to host phylum

The claim that "red alga" (rather than just "macroalga") picks out a real microbial habitat has direct empirical support: epiphytic bacterial communities on 17 red, plus brown and green, intertidal specimens from Achziv, Israel **clustered by host phylum (FDR 0.002)**, with red and brown more similar to each other than to green; **39% of ASVs were phylum specialists**, 7.5% shared across all three; and most seawater ASVs did not appear on the algae ([Nahor et al. 2024, doi:10.1038/s41598-024-69362-y](https://doi.org/10.1038/s41598-024-69362-y)). At the same time there is a strong cross-host core: across co-located *Ulva*, *Saccharina*, *Grateloupia* and *Gelidium* sampled all four seasons at Weihai, **14 core genera — 0.7% of all genera — accounted for on average 51.1% of bacterial abundance** ([Lu et al. 2023, doi:10.1186/s40168-023-01559-1](https://doi.org/10.1186/s40168-023-01559-1)). Dominant phyla on red algal surfaces are Proteobacteria, Bacteroidetes and Actinobacteria across Antarctic, Indonesian and Chinese sites ([Gu et al. 2023](https://doi.org/10.3390/ijms241311019)).

Read honestly, this supports the term *and* bounds it: the host-phylum signal is real but sits on top of a shared macroalgal core, so "red algae" is a meaningful habitat class, not a maximally distinctive one.

### 3e. Physical setting (useful context, weak differentia)

Rhodophyta comprise **7,554 species (7,276 living) in 1,094 genera**, marine-dominated with freshwater and terrestrial as less-favoured habitats; Florideophyceae alone hold 6,879 living species ([Guiry 2024, Tables 2 and 7, doi:10.1111/jpy.13431](https://doi.org/10.1111/jpy.13431)). The habitat spans the intertidal to the deepest known macrophyte population on Earth — an undescribed purple crustose coralline alga at **268 m** on San Salvador Seamount, the predominant organism between 210 and 268 m ([Littler et al. 1985, *Science* 227:57–59, doi:10.1126/science.227.4682.57](https://doi.org/10.1126/science.227.4682.57)). Calcified coralline thalli are a special case worth a comment: their surface biofilms are ecologically load-bearing, with tetrabromopyrrole from CCA-associated *Pseudoalteromonas* (isolated from *Neogoniolithon fosliei* and *Hydrolithon onkodes*) inducing coral larval metamorphosis ([Tebben et al. 2011, *PLoS ONE* 6:e19082, PMC3084748](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3084748/)).

I would **not** put depth, salinity or calcification in the definition: they vary within the concept rather than distinguishing it from siblings.

---

## 4. Sources

Primary literature, standards and reference works used above, with identifiers:

1. Guiry, M.D. (2024). How many species of algae are there? A reprise. Four kingdoms, 14 phyla, 63 classes and still growing. *Journal of Phycology*. doi:[10.1111/jpy.13431](https://doi.org/10.1111/jpy.13431). — Rhodophyta counts (Tables 2, 7); habitat codes; kingdom assignment.
2. Usov, A.I. (2011). Polysaccharides of the red algae. *Advances in Carbohydrate Chemistry and Biochemistry* 65:115–217. PMID [21763512](https://pubmed.ncbi.nlm.nih.gov/21763512/). — Agars/carrageenans, sulfation, cellulose <10%, floridean starch, floridoside.
3. Hehemann, J.-H. et al. (2010). Transfer of carbohydrate-active enzymes from marine bacteria to Japanese gut microbiota. *Nature* 464:908–912. doi:[10.1038/nature08937](https://doi.org/10.1038/nature08937). — Porphyranases; red-algal galactan as a niche-defining substrate.
4. Gu, X. et al. (2023). Metagenomic insights reveal the microbial diversity and associated algal-polysaccharide-degrading enzymes on the surface of red algae among remote regions. *IJMS* 24(13):11019. doi:[10.3390/ijms241311019](https://doi.org/10.3390/ijms241311019). — Sampling protocol; dominant phyla; agarase/carrageenase gene counts.
5. Lu, D.-C. et al. (2023). Epiphytic common core bacteria in the microbiomes of co-located green (*Ulva*), brown (*Saccharina*) and red (*Grateloupia*, *Gelidium*) macroalgae. *Microbiome* 11:126. doi:[10.1186/s40168-023-01559-1](https://doi.org/10.1186/s40168-023-01559-1). PMID 37264413. — 14 core genera, 51.1% of abundance; seawater and sediment controls.
6. Nahor, O. et al. (2024). Epiphytic microbiome associated with intertidal seaweeds in the Mediterranean Sea. *Scientific Reports* 14:18631. doi:[10.1038/s41598-024-69362-y](https://doi.org/10.1038/s41598-024-69362-y). — Host-phylum clustering (FDR 0.002); 39% phylum specialists; swab sampling.
7. Wahl, M. et al. (2012). The second skin: ecological role of epibiotic biofilms on marine organisms. *Frontiers in Microbiology* 3:292. doi:[10.3389/fmicb.2012.00292](https://doi.org/10.3389/fmicb.2012.00292). PMID 22936927. — Macroalgal surfaces as a colonised compartment; host role in shaping it.
8. Paul, N.A., de Nys, R., Steinberg, P.D. (2006). Chemical defence against bacteria in the red alga *Asparagopsis armata*: linking structure with function. *MEPS* 306:87–101. doi:[10.3354/meps306087](https://doi.org/10.3354/meps306087). — Bromoform/DBA content; lower epiphytic density on producing algae.
9. Case, R.J. et al. (2011). Temperature induced bacterial virulence and bleaching disease in a chemically defended marine macroalga. *Environmental Microbiology*. PMID [20946533](https://pubmed.ncbi.nlm.nih.gov/20946533/). — *Delisea pulchra* furanone defence; epidermal invasion at 24 °C.
10. Fernandes, N. et al. (2011). Genomes and virulence factors of novel bacterial pathogens causing bleaching disease in the marine red alga *Delisea pulchra*. *PLoS ONE* 6:e27387. doi:[10.1371/journal.pone.0027387](https://doi.org/10.1371/journal.pone.0027387).
11. Littler, M.M. et al. (1985). Deepest known plant life discovered on an uncharted seamount. *Science* 227:57–59. doi:[10.1126/science.227.4682.57](https://doi.org/10.1126/science.227.4682.57). — CCA at 268 m.
12. Tebben, J. et al. (2011). Induction of larval metamorphosis of the coral *Acropora millepora* by tetrabromopyrrole isolated from a *Pseudoalteromonas* bacterium. *PLoS ONE* 6:e19082. [PMC3084748](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3084748/).
13. Quinlan, Z.A. et al. (2019). Species-specific differences in the microbiomes and organic exudates of crustose coralline algae influence bacterioplankton communities. *Frontiers in Microbiology* 10:2397. doi:[10.3389/fmicb.2019.02397](https://doi.org/10.3389/fmicb.2019.02397).
14. Yoon, H.S. et al. (2006). Establishment of endolithic populations of extremophilic Cyanidiales (Rhodophyta). *BMC Evolutionary Biology* 6:78. doi:[10.1186/1471-2148-6-78](https://doi.org/10.1186/1471-2148-6-78). — Unicellular red algal reading; pH 0.5–3.0, 50–55 °C.
15. Gross, W. et al. (1998). Cryptoendolithic growth of the red alga *Galdieria sulphuraria* in volcanic areas. *European Journal of Phycology* 33:25–31. doi:[10.1080/09670269810001736503](https://doi.org/10.1080/09670269810001736503).
16. Mukherjee, S. et al. (2023). Twenty-five years of Genomes OnLine Database (GOLD). *NAR* 51:D957–D963. doi:[10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974). — The five-level ecosystem classification that produced the source path.
17. Kim, G.H. et al. / Qiu, L. et al. — red rot disease of *Pyropia yezoensis* caused by *Pythium chondricola* and *P. porphyrae*, and shifts in associated bacterial communities: [Front Microbiol 2019, PMC6664831](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6664831/); [Plant Disease, doi:10.1094/PDIS-07-21-1494-SC](https://doi.org/10.1094/PDIS-07-21-1494-SC).
18. ENVO term records checked via OLS4 on 2026-08-17: `ENVO:01001000`, `ENVO:01001001`, `ENVO:01001002`, `ENVO:01001041`, `ENVO:01001179`, `ENVO:01001189`, `ENVO:03605000`, `ENVO:2000004`. Zero hits for `algae-associated` in ENVO (`https://www.ebi.ac.uk/ols4/api/search?q=algae-associated&ontology=envo`). Labels and definitions cross-checked against this repo's vendored slice, `data/raw/ontology_terms.tsv`.

**Explicitly flagged as my inference, not source statements:** (a) that floridean starch and floridoside are meaningful carbon sources for red-algal epibionts; (b) that the brown/green wall-chemistry contrast (alginate/fucoidan vs ulvan) is as I state it — standard phycology, but not cited from a source I read here; (c) that GOLD's `Blade`/`Sporeling`/`Embryo`/`Whole body` children imply the host reading — a reading of the data, though a well-founded one.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept (the alga as habitat):**
- red macroalga-associated environment; red seaweed–associated environment
- rhodophyte thallus surface; red algal surface / red algal epiphytic (epibiotic) microbiome
- red algal phycosphere *(used loosely; strictly the phycosphere is the diffusive zone around algal cells)*
- red algal holobiont *(names host + microbiota together, so it is a related concept rather than a clean synonym for the habitat)*
- *Rhodophyta*-associated environment; "red algae" as GOLD writes it
- Common instances by trade name: nori (*Neopyropia/Pyropia*), Irish moss (*Chondrus crispus*), dulse (*Palmaria palmata*), *Gracilaria*, *Kappaphycus*, coralline/maerl

**Commonly but wrongly treated as the same thing:**

| Confusable | Why it is different |
|---|---|
| **Rhodophyta the taxon** (FOODON:03411743, NCBITaxon:2763) | A class of organisms, not a place. Keep as `relation: xref` per #99. |
| **"Red tide"** | A synonym on ENVO:01000057 `marine algal bloom`, but red tides are dinoflagellate (or cyanobacterial) blooms — nothing to do with Rhodophyta. The single most likely lexical trap on this label. |
| **Red algal food products** — nori sheets, agar, carrageenan, agarose | Processed material; microbiologically a food habitat, not a host. FOODON:03412266, FOODON:00001184. |
| **Seaweed farm / cultivation water** | ENVO:03600074 `aquaculture farm`, ENVO:01001252 `seaweed farming process`. Farmed *Pyropia* studies routinely sample both; they are distinct habitats. |
| **Cyanidiales habitats** — acidic hot springs, endolithic volcanic rock | The alga there is itself a microorganism; the habitat is environmental, not host-associated ([Yoon et al. 2006](https://doi.org/10.1186/1471-2148-6-78)). |
| **Coralline algal reef / maerl bed as substratum** | The mineral framework and the biome (ENVO:01000050) are not the living alga. |
| **Periphyton / biofilm containing algae** (ENVO:03605000) | Alga is a community member, not the host — relation inverted. |
| **Gut of a red-algae-eating animal** | *B. plebeius* porphyranases are a gut-habitat fact ([Hehemann 2010](https://doi.org/10.1038/nature08937)); the alga is diet. |
| **Eukaryotic endophytes of red algae** (e.g. *Acrochaete* green algae in *Chondrus crispus*) | Inhabitants, not the habitat. |
| **Brown/green algae** | Sibling records; wall chemistry and epiphytic communities differ measurably (§3). |

---

## 6. Should it be a term at all?

**Yes — with one structural caveat.**

It passes the repo's own line. A red alga acting as host *is* where microbes live: the surface is a colonised, chemically defended, sampled compartment ([Wahl 2012](https://doi.org/10.3389/fmicb.2012.00292); [Paul 2006](https://doi.org/10.3354/meps306087)), the tissue supports endophytes ([PMC10694040](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10694040/)), and ENVO already models exactly this relation for plants, animals, fungi and cnidarians via `ENVO:01001000`. What is not a place is the taxon Rhodophyta — and that is already handled as the xref. This is the same disposition as the sponge, nematode and reptile cases, and `NOT_APPLICABLE` would be the wrong call: it asserts the concept is not a habitat, which the evidence contradicts.

It also survives the sharper test of whether the *phylum-level* cut carries microbial signal rather than merely taxonomic tidiness. It does: host-phylum explains community structure at FDR 0.002 with 39% phylum-specialist ASVs ([Nahor 2024](https://doi.org/10.1038/s41598-024-69362-y)), and the sulfated-galactan wall gives red algal surfaces a distinctive CAZyme profile — agarases, carrageenases, porphyranases ([Gu 2023](https://doi.org/10.3390/ijms241311019); [Hehemann 2010](https://doi.org/10.1038/nature08937)). That is a differentia a curator can defend.

**The caveat, and my recommendation.** The missing class is not *this* one; it is the one above it. Requesting `red algae–associated environment` while `algae-associated environment` does not exist forces the term to hang directly off `ENVO:01001000` alongside the whole of Plantae and Metazoa, which loses the very grouping the GOLD path asserts (`Host-associated > Algae > Red algae`). I would request the intermediate first — or request the pair together — and let this term's definition be the short form: *An algae-associated environment which is determined by a red alga (Rhodophyta), whose sulfated-galactan (agar, carrageenan, porphyran) cell wall distinguishes it from the alginate-walled brown algae and ulvan-walled green algae.*

Two things to record in the term's comment rather than the definition: that the concept covers macroalgal hosts and **not** the unicellular Cyanidiophyceae in acid hot springs (an exclusion, because the label does not make it obvious), and that within-phylum variation — calcified crustose coralline vs. fleshy foliose vs. filamentous turf — is large enough that the phylum-level term is deliberately coarse.

## Citations

1. https://doi.org/10.1093/nar/gkac974
2. https://doi.org/10.1038/s41598-024-69362-y
3. https://doi.org/10.3390/ijms241311019
4. https://doi.org/10.3389/fmicb.2012.00292
5. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10694040/
6. https://pubmed.ncbi.nlm.nih.gov/20946533/
7. https://doi.org/10.3389/fmicb.2019.02397
8. https://doi.org/10.1186/s40168-023-01559-1
9. https://doi.org/10.1038/nature08937
10. https://doi.org/10.1111/jpy.13431
11. https://doi.org/10.1186/1471-2148-6-78
12. https://doi.org/10.1080/09670269810001736503
13. https://www.ebi.ac.uk/ols4/api/search?q=algae-associated&ontology=envo`
14. https://pubmed.ncbi.nlm.nih.gov/21763512/
15. https://doi.org/10.1016/j.biochi.2008.09.008
16. https://doi.org/10.3354/meps306087
17. https://doi.org/10.1371/journal.pone.0027387
18. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2901821/
19. https://doi.org/10.1126/science.227.4682.57
20. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3084748/
21. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6664831/
22. https://doi.org/10.1094/PDIS-07-21-1494-SC