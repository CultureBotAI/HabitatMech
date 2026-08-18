---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T22:53:35.169243'
end_time: '2026-08-17T23:01:03.893542'
duration_seconds: 448.72
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Tunicates
  habitat_identifier: habitatmech:GOLD.78c645fff9
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Tunicates'
  assertions: '23'
  parent_terms: ENVO:01001000
  xrefs: FOODON:03414466
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term FOODON:03414466 'tunicate' attached as a parent. Host-taxon reversal\
    \ (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a\
    \ habitat'. That reasoning is wrong, and the corpus already contradicted it \u2014\
    \ the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia,\
    \ Mammals, Birds and Fish, which keep their own identity and a term request for\
    \ an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE\
    \ while its own child Porifera > Sponge was a term request.An organism acting\
    \ as a host IS a habitat: it is where the microbe lives, and ENVO models exactly\
    \ this at plant-associated, animal-associated and fungi-associated environment.\
    \ What is not a habitat is the TAXON TERM \u2014 a phylum is a class of organisms,\
    \ not a place \u2014 so the taxon stays an xref (#99) and the concept keeps its\
    \ own identity as a term-request candidate. NOT_APPLICABLE said the concept is\
    \ not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.78c645fff9)"
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
  web_search_requests: 13
  num_turns: 27
  total_cost_usd: 2.993454
  session_id: 30168686-54d5-490d-8b09-2fd724466257
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 27
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Tunicates
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.78c645fff9
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Tunicates
- **Upstream assertion volume:** 23
- **Nearest broader term already on the record:** ENVO:01001000
- **Cross-references upstream suggested:** FOODON:03414466

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term FOODON:03414466 'tunicate' attached as a parent. Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it — the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE while its own child Porifera > Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM — a phylum is a class of organisms, not a place — so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.78c645fff9)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Tunicates** as a microbial habitat, with citations.

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

# Tunicates (`habitatmech:GOLD.78c645fff9`) — definition research

> **Proposed definition:** An animal-associated environment which is determined by a tunicate (Chordata: Tunicata) or a part of one, comprising the cellulose-bearing tunic and the internal cavities through which the animal continuously pumps and filters seawater.

If a curator prefers ENVO's terser house style for taxon-scoped host environments, the parallel to `ENVO:01001179` is exact: *"An environmental system determined by a tunicate or part of a tunicate."* The longer form above is preferred because the tunic and the filter-feeding cavity are what actually distinguish this habitat from other animal-associated environments, and both are observable.

---

## 1. What the concept denotes

**The sampled thing.** A tunicate individual or colony considered as the place a microbial sample is taken from. In practice a "Tunicates" sample is one of a small, well-attested set of compartments:

| Compartment | What it is | Representative study |
|---|---|---|
| Tunic (surface + matrix) | The acellular cellulose–protein exoskeleton secreted by the epidermis | [Erwin et al. 2014, *ISME J*](https://doi.org/10.1038/ismej.2013.188); [Blasiak et al. 2014, *ISME J*](https://doi.org/10.1038/ismej.2013.156) |
| Branchial sac / pharynx | The filter-feeding basket water passes through | [Ascidia sydneiensis compartment study, PMC10881349](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10881349/) |
| Gut / digestive tract | Distinct from tunic and from seawater | [Dishaw et al. 2014, *PLOS ONE*](https://doi.org/10.1371/journal.pone.0093386); [Yang et al. 2022, *Mar Life Sci Technol*](https://doi.org/10.1007/s42995-022-00131-4) |
| Cloacal cavity | Houses the photosymbiont *Prochloron* in didemnids | [Kühl et al. 2012, *Front Microbiol* 3:402](https://doi.org/10.3389/fmicb.2012.00402) |
| Light organs (pyrosomes) | Bacteriocyte-like structures holding luminous *Photobacterium* | [Berger et al. 2021, *Front Mar Sci*](https://doi.org/10.3389/fmars.2021.606818) |
| Secreted houses (larvaceans) | Discarded mucus/cellulose filter houses that become colonized marine snow | Davoll & Silver 1986, *MEPS* 33:111–120; [Alldredge 1976, *Limnol Oceanogr* 21:14–23](https://doi.org/10.4319/lo.1976.21.1.0014) |

**The boundary.** Inside the concept: the tunic and its embedded consortium, the internal cavities and gut, the vertically transmitted intracellular symbionts, and secreted structures made and inhabited by the animal. Neighbouring concepts, outside it:

- **Surrounding seawater.** Not a boundary of convenience — the ascidian consortium is compositionally distinct from ambient seawater, and several rare seawater taxa are enriched 200–700-fold in the tunic ([Erwin et al. 2014](https://doi.org/10.1038/ismej.2013.188)).
- **The substratum.** Most adult ascidians are attached to rock or artificial structures; the rock is a separate habitat.
- **The taxon `NCBITaxon:7712` Tunicata.** A class of organisms, not a place. This is the distinction the curation note already makes and is why the taxon and `FOODON:03414466` belong in `xrefs`.
- **The child concept `Ascidians` (`habitatmech:GOLD.34c28836da`, GOLD path `Host-associated > Tunicates > Ascidians`, 79 organisms).** "Tunicates" is the parent; the residual 23 organisms on the parent path are tunicate hosts GOLD did not resolve to Ascidiacea.

**Is the label ambiguous?** Only mildly, and the source path resolves it. Two readings exist:

1. **Subphylum-wide (the reading the data means).** Tunicata comprises Ascidiacea (sessile benthic sea squirts), Thaliacea (salps, doliolids, pyrosomes) and Appendicularia (larvaceans) — all marine filter feeders with a tunic ([FoodOn definition of `FOODON:03414466`](https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?obo_id=FOODON:03414466); [Inoue & Satoh 2019, *Genes*](https://doi.org/10.3390/genes10040294)). GOLD's own tree forces this reading: `Ascidians` is a *child* of `Tunicates`, so the parent must be broader than Ascidiacea.
2. **Colloquial "tunicate" = "sea squirt" = ascidian.** Common in the natural-products literature, where "tunicate-derived" compounds are almost always ascidian-derived. This reading would collapse the concept into its own child and should be rejected.

**A wrinkle worth recording:** the corpus holds a second GOLD path, `Host-associated > Invertebrates > Tunicates` (`habitatmech:GOLD.6afe6868a8`, 0 assertions, 3 node ids). It is the same concept filed under a different parent. Tunicates are chordates, so "Invertebrates" there is a folk grouping, not a clade. Any term minted here covers both paths; whether they should be merged is a separate curation question (the corpus has a same-concept mechanism for exactly this).

## 2. Genus — the broader kind

**Recommended genus: `ENVO:01001002` "animal-associated environment"** — *"An environmental system determined by an animal"* (synonyms: *Metazoan-associated environment*, *animal environment*; verified against [OLS4, August 2026](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002)). Tunicates are metazoans (subphylum of Chordata), so this holds without additional assertion.

**Note a live inconsistency in the corpus.** This record currently carries `parent_habitats: ENVO:01001000` — *"environmental system determined by an organism"*, exact synonym *host-associated environment* — while its own child `Ascidians` carries the narrower `ENVO:01001002`. `ENVO:01001000` is true but not the smallest well-established kind, and it puts the parent record one level *broader* than its child's parent. Switching this record to `ENVO:01001002` is a one-line seeder-input change and makes the two consistent.

**Near-misses checked in ENVO (nothing matches):**

| Term | Why it fails |
|---|---|
| `ENVO:01001000` environmental system determined by an organism | Broader — covers plant, fungal and prokaryote-determined systems too. Currently on the record. |
| `ENVO:01001002` animal-associated environment | The genus, not the species — broader than tunicates by all of Metazoa. |
| `ENVO:01001001` plant-associated environment | Wrong kingdom. |
| `ENVO:01001179` cnidarian-associated environment | Not a match, but the **precedent that matters**: it is the only taxon-scoped `X-associated environment` in ENVO, and it shows the pattern this concept needs. |
| `FOODON:03414466` tunicate | An organism/food-source term, not an environmental system; adopting it would ground a place to a class of animals. Correct as the existing `xref`. |
| `NCBITaxon:7712` Tunicata | Taxon; same objection. |
| `BTO:0000090` ascidian | Biological-source term, *and* narrower (Ascidiacea only). Already rejected on the `Ascidians` record for the source/habitat reason. |
| `UBERON:0009719` tunicate siphon | An anatomical part. Under the project's parts-vs-whole rule, parts ground to anatomy — but this concept denotes the whole host, not the siphon. |
| ENVO marine water-body terms | Would assert a water-mass location the GOLD path does not make; the concept is host-determined, not water-body-determined. Also wrong for aquacultured and fouling-community hosts. |

**No `tunicate-associated environment` or `ascidian-associated environment` exists in ENVO.** A full OLS4 query for ENVO terms whose label ends in *-associated environment* returns exactly four: `01001041` fungi, `01001001` plant, `01001002` animal, `01001179` cnidarian (queried August 2026). This is the direct evidence for `CONFIRM_UNGROUNDED` and for a term request.

## 3. Differentia — what distinguishes it from sibling animal-associated environments

Ordered by how observable each property is.

**a) A cellulose exoskeleton — structurally unique among animals.** The tunic is an acellular covering of cellulose ("tunicin") microfibrils in a protein/proteoglycan matrix. Tunicates are the **only metazoans that synthesize cellulose**: `CesA` orthologs are present in all sequenced tunicate genomes and absent from all other animal genomes, the gene having been acquired by horizontal transfer from an actinobacterial donor and fused with a GH6 cellulase domain ([Inoue & Satoh 2019, *Genes* 10:294](https://doi.org/10.3390/genes10040294); [Sasakura et al. 2016, *Proc R Soc B*](https://doi.org/10.1098/rspb.2016.1712)). This gives the habitat a substrate no other host clade offers, and is the single most defensible differentia.

**b) Obligate, continuous filtration of seawater.** All tunicates feed by drawing water through a mucus filter — an incurrent siphon to a branchial basket to an excurrent siphon in ascidians, mucus houses in larvaceans ([FoodOn/Tunicata description](https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?obo_id=FOODON:03414466); Alldredge 1976). The habitat is therefore continuously inoculated from the water column *and* continuously selective — which is why the resulting communities are distinct from seawater rather than a passive sample of it ([Erwin et al. 2014](https://doi.org/10.1038/ismej.2013.188); [Yang et al. 2022](https://doi.org/10.1007/s42995-022-00131-4)).

**c) High, host-specific microbial diversity, compartmentalized within the holobiont.** 16S surveys of 42 Great Barrier Reef samples across 25 ascidian species recovered **3,217 OTUs across 33 phyla**, with communities differing markedly from seawater, most taxa host-specific, and ammonia-oxidizing Thaumarchaeota present in **24 of 25 host species** — the authors attribute the nitrifier signal to ammonia-rich host waste ([Erwin et al. 2014, *ISME J* 8:575–588](https://doi.org/10.1038/ismej.2013.188)). Tunic, gut and seawater form three separable communities in *Ciona intestinalis* ([Blasiak et al. 2014](https://doi.org/10.1038/ismej.2013.156); [Utermann et al. 2020, *Microorganisms* 8:2022](https://doi.org/10.3390/microorganisms8122022); [Dishaw et al. 2014](https://doi.org/10.1371/journal.pone.0093386)).

**d) Extreme, light-driven physicochemical swings in hospite.** Microsensor work in the cloacal cavity of *Lissoclinum patella* shows the *Prochloron*-bearing zone goes anoxic and acidic within minutes of darkness and O₂-supersaturated and strongly alkaline within minutes of illumination, spanning roughly **pH 6 to pH 10** on a diel cycle ([Kühl et al. 2012, *Front Microbiol* 3:402](https://doi.org/10.3389/fmicb.2012.00402)). Separately, phlebobranch ascidian blood cells (vanadocytes) sequester vanadium at ~10⁷× seawater concentration in vacuoles of pH ~1.8–4.2 with high sulfate ([Michibata et al. 1996, *Zool Sci* 13:489](https://doi.org/10.2108/zsj.13.489)). Both are compartment-level, not whole-organism, properties — sound as supporting text, too specific for the definition sentence.

**e) Vertically transmitted, uncultivated, genome-reduced symbionts.** *Prochloron didemni*, an obligate didemnid photosymbiont uncultivated since its 1975 discovery, supplies 60–100% of host organic carbon ([Kühl et al. 2012](https://doi.org/10.3389/fmicb.2012.00402); [Donia et al. 2011, *PNAS* 108:E1423–E1432](https://doi.org/10.1073/pnas.1111712108)). *Candidatus* Endoecteinascidia frumentensis, the ET-743 (trabectedin) producer in *Ecteinascidia turbinata*, has a **~631 kb** genome assembled directly from tunicate metagenomic DNA and is specialized for that one pathway ([Schofield et al. 2015, *Environ Microbiol*, PMID 26013440](https://doi.org/10.1111/1462-2920.12908); [Rath et al. 2011, *ACS Chem Biol* 6:1244–1256](https://doi.org/10.1021/cb200244t)).

**f) Pelagic sub-habitats that no ascidian-scoped term would cover.** Pyrosome light organs contain intracellular *Photobacterium* Pa-1 in bacteriocyte-like structures, with >50% of reads from bioluminescent Vibrionaceae ([Berger et al. 2021](https://doi.org/10.3389/fmars.2021.606818)). Doliolid guts hold a low-biomass, low-diversity resident community cored on *Pseudoalteromonas* and *Shimia*, distinct from both seawater and the animal's own faecal pellets ([Pereira et al. 2022, *Mol Ecol*](https://doi.org/10.1111/mec.16668)). Discarded larvacean houses are colonized by bacteria and protozoa and become a major marine-snow class (Davoll & Silver 1986, *MEPS* 33:111–120; Alldredge 1976). **This is the strongest argument that the parent term must be tunicate-scoped rather than ascidian-scoped** — my inference from the cited studies, not a claim any one of them makes.

## 4. Sources

Primary literature (all DOIs verified against the publisher or PMC record during this research):

- Erwin PM, Pineda MC, Webster N, Turon X, López-Legentil S (2014) "Down under the tunic: bacterial biodiversity hotspots and widespread ammonia-oxidizing archaea in coral reef ascidians." *ISME J* 8(3):575–588. [doi:10.1038/ismej.2013.188](https://doi.org/10.1038/ismej.2013.188) · [PMID 24152714](https://pubmed.ncbi.nlm.nih.gov/24152714/)
- Blasiak LC, Zinder SH, Buckley DH, Hill RT (2014) "Bacterial diversity associated with the tunic of the model chordate *Ciona intestinalis*." *ISME J*. [doi:10.1038/ismej.2013.156](https://doi.org/10.1038/ismej.2013.156)
- Dishaw LJ et al. (2014) "The gut of geographically disparate *Ciona intestinalis* harbors a core microbiota." *PLOS ONE* 9(4):e93386. [doi:10.1371/journal.pone.0093386](https://doi.org/10.1371/journal.pone.0093386)
- Utermann C et al. (2020) "Comparative microbiome and metabolome analyses of the marine tunicate *Ciona intestinalis* from native and invaded habitats." *Microorganisms* 8:2022. [doi:10.3390/microorganisms8122022](https://doi.org/10.3390/microorganisms8122022)
- Kühl M, Behrendt L, Trampe E, Qvortrup K, Schreiber U, Borisov SM, Klimant I, Larkum AWD (2012) "Microenvironmental ecology of the chlorophyll *b*-containing symbiotic cyanobacterium *Prochloron* in the didemnid ascidian *Lissoclinum patella*." *Front Microbiol* 3:402. [doi:10.3389/fmicb.2012.00402](https://doi.org/10.3389/fmicb.2012.00402)
- Donia MS et al. (2011) "Complex microbiome underlying secondary and primary metabolism in the tunicate–*Prochloron* symbiosis." *PNAS* 108(51):E1423–E1432. [doi:10.1073/pnas.1111712108](https://doi.org/10.1073/pnas.1111712108) · PMID 22123943
- Schofield MM, Jain S, Porat D, Dick GJ, Sherman DH (2015) "Identification and analysis of the bacterial endosymbiont specialized for production of the chemotherapeutic natural product ET-743." *Environ Microbiol*. [doi:10.1111/1462-2920.12908](https://doi.org/10.1111/1462-2920.12908) · [PMID 26013440](https://pubmed.ncbi.nlm.nih.gov/26013440/)
- Rath CM et al. (2011) "Meta-omic characterization of the marine invertebrate microbial consortium that produces the chemotherapeutic natural product ET-743." *ACS Chem Biol* 6:1244–1256. [doi:10.1021/cb200244t](https://doi.org/10.1021/cb200244t)
- Berger A et al. (2021) "Microscopic and genetic characterization of bacterial symbionts with bioluminescent potential in *Pyrosoma atlanticum*." *Front Mar Sci* 8:606818. [doi:10.3389/fmars.2021.606818](https://doi.org/10.3389/fmars.2021.606818)
- Pereira RE et al. (2022) "The microbiome of the pelagic tunicate *Dolioletta gegenbauri*: a potential link between the grazing and microbial food web." *Mol Ecol*. [doi:10.1111/mec.16668](https://doi.org/10.1111/mec.16668)
- Yang Y, Zhu Y, Liu H, Wei J, Yu H, Dong B (2022) "Cultivation of gut microorganisms of the marine ascidian *Halocynthia roretzi*…" *Mar Life Sci Technol* 4(2):201–207. [doi:10.1007/s42995-022-00131-4](https://doi.org/10.1007/s42995-022-00131-4)
- Inoue J, Satoh N (2019) "ORTHOSCOPE analysis reveals the presence of the cellulose synthase gene in all tunicate genomes but not in other animal genomes." *Genes* 10:294. [doi:10.3390/genes10040294](https://doi.org/10.3390/genes10040294)
- Sasakura Y et al. (2016) "Transcriptional regulation of a horizontally transferred gene from bacterium to chordate." *Proc R Soc B*. [doi:10.1098/rspb.2016.1712](https://doi.org/10.1098/rspb.2016.1712)
- Michibata H et al. (1996) "The mechanism of accumulation of vanadium by ascidians." *Zool Sci* 13:489. [doi:10.2108/zsj.13.489](https://doi.org/10.2108/zsj.13.489)
- Davoll PJ, Silver MW (1986) "Marine snow aggregates: life history sequence and microbial community of abandoned larvacean houses from Monterey Bay, California." *Mar Ecol Prog Ser* 33:111–120. Alldredge AL (1976) *Limnol Oceanogr* 21:14–23, [doi:10.4319/lo.1976.21.1.0014](https://doi.org/10.4319/lo.1976.21.1.0014). *(Both cited from secondary sources; I did not fetch the primary PDFs — verify before quoting numbers from them.)*
- Waterhouse J et al. / Palanisamy SK et al. (2021) "Marine natural products from tunicates and their associated microbes." *Mar Drugs* 19:308. [doi:10.3390/md19060308](https://doi.org/10.3390/md19060308)

Vocabularies and standards:

- ENVO term records verified live via [OLS4](https://www.ebi.ac.uk/ols4/): `ENVO:01001000`, `ENVO:01001001`, `ENVO:01001002`, `ENVO:01001041`, `ENVO:01001179`; `FOODON:03414466`. Buttigieg PL et al. (2016) "The environment ontology in 2016…" *J Biomed Semantics*, [PMC5035502](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035502/).
- Mukherjee S et al. (2023) "Twenty-five years of Genomes OnLine Database (GOLD): data updates and new features in v.9." *Nucleic Acids Res* 51(D1):D957–D963. [doi:10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974) — the source of the five-level `Host-associated > …` path this record is seeded from.
- MIxS host-associated package: Yilmaz P et al. (2011) *Nat Biotechnol* 29:415–420, [doi:10.1038/nbt.1823](https://doi.org/10.1038/nbt.1823) — the standard under which a tunicate sample's `host` and environmental triad are recorded.

**Explicitly marked as inference, not sourced claims:** (i) that GOLD's `Host-associated > Tunicates` path means the subphylum rather than "sea squirts" — inferred from the tree's own `> Ascidians` child, not from GOLD documentation; (ii) that pelagic-tunicate sub-habitats require a tunicate-scoped rather than ascidian-scoped term; (iii) the recommendation to move `parent_habitats` from `ENVO:01001000` to `ENVO:01001002` — an ontological judgement, not a published statement.

## 5. Synonyms, and what not to conflate

**Names in real use for the concept or its parts:** tunicate-associated environment; urochordate host; Tunicata (subphylum; formerly Urochordata); sea squirt (for ascidians); sea pork (colonial ascidians); tunic / tunicin matrix; ascidian holobiont; hoya / maboya (ホヤ) and meongge (멍게) for *Halocynthia roretzi*; salp, doliolid, pyrosome (Thaliacea); larvacean, appendicularian (Appendicularia); "house" (larvacean feeding filter). AGROVOC carries species-level entries such as [*Halocynthia roretzi*](https://agrovoc.fao.org/browse/agrovoc/en/page/c_49437).

**Do not conflate:**

- **Tunicates ≠ Ascidians.** Ascidiacea is one of three classes and is already a separate, more heavily attested record (79 vs 23 organisms). Most "tunicate" natural-products literature is really ascidian literature.
- **Tunicates ≠ the taxon `NCBITaxon:7712`.** The habitat is a host organism acting as a place; the taxon is a class of organisms.
- **Tunicates ≠ the food commodity.** `FOODON:03414466` sits in a food-source context, and *H. roretzi* is a real aquaculture commodity (~21,500 t globally in 2006 per FAO figures, via [Wikipedia: sea pineapple](https://en.wikipedia.org/wiki/Halocynthia_roretzi)). A gut microbiome sample from a live sea squirt and a microbial survey of raw *meongge* on a market stall are different habitats. Keep `FOODON:03414466` as an `xref`, never as a ground or a parent.
- **Tunic ≠ biofouling community on the tunic surface.** Ascidians are themselves notorious foulers of hulls and aquaculture gear. Surface biofilm and tunic-matrix consortium are frequently sampled together and are not the same compartment; the tunic-surface reading also blurs into `ENVO` biofilm terms.
- **Tunicate-associated ≠ marine water column.** Even for pelagic thaliaceans, the host is the environmental determinant, not the water mass.
- **"Tunicate-derived" natural products ≠ tunicate-produced.** Trabectedin and the patellamides are symbiont pathways expressed in hospite ([Schofield et al. 2015](https://doi.org/10.1111/1462-2920.12908); [Donia et al. 2011](https://doi.org/10.1073/pnas.1111712108)). Not a habitat question, but it is the most common misstatement in this literature and would corrupt any mechanism claim written from it.
- **Tunicata ≠ "invertebrates."** Tunicates are chordates. The corpus's second path files them under Invertebrates; that is GOLD's folk grouping, not a clade.

## 6. Should it be a term at all?

**Yes.** This is a genuine host-determined environment, not a process, quality, disease or artefact:

- It is a **place microbes live**, with named, spatially resolved compartments (tunic matrix, branchial sac, gut, cloacal cavity, light organ, bacteriocyte) and measurable in-situ physicochemistry ([Kühl et al. 2012](https://doi.org/10.3389/fmicb.2012.00402)).
- It **selects** — its communities are reproducibly distinct from ambient seawater across ascidians, doliolids and pyrosomes ([Erwin et al. 2014](https://doi.org/10.1038/ismej.2013.188); [Pereira et al. 2022](https://doi.org/10.1111/mec.16668); [Berger et al. 2021](https://doi.org/10.3389/fmars.2021.606818)).
- ENVO **already models this pattern** at `ENVO:01001179` cnidarian-associated environment; a tunicate sibling is the same construction, not a novel one.
- It has **real sampling volume**: 23 organisms on this path and 79 on its own child, plus 4 GOLD ecosystem node ids sharing this path.

`NOT_APPLICABLE` would be the wrong disposition — it asserts the concept is not a habitat, which the literature above contradicts. `CONFIRM_UNGROUNDED` plus an ENVO term request for **`tunicate-associated environment`** is the right one, and is what the record already records.

**Two follow-ups for the curator, both outside this report's scope:**

1. Change `parent_habitats` from `ENVO:01001000` to `ENVO:01001002` in the seeder input, to match the child `Ascidians` record and to use the smallest correct genus.
2. Decide whether `habitatmech:GOLD.6afe6868a8` (`Host-associated > Invertebrates > Tunicates`, 0 assertions) is the same concept as this one. It looks like a duplicate under a mistaken parent, and the corpus has a same-concept mechanism for that case.

**Nothing in this report authorizes an ENVO submission.** Per the standing rule, a term request needs an explicit yes for this specific request.

## Citations

1. https://doi.org/10.1038/ismej.2013.188
2. https://doi.org/10.1038/ismej.2013.156
3. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10881349/
4. https://doi.org/10.1371/journal.pone.0093386
5. https://doi.org/10.1007/s42995-022-00131-4
6. https://doi.org/10.3389/fmicb.2012.00402
7. https://doi.org/10.3389/fmars.2021.606818
8. https://doi.org/10.4319/lo.1976.21.1.0014
9. https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?obo_id=FOODON:03414466
10. https://doi.org/10.3390/genes10040294
11. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002
12. https://doi.org/10.1098/rspb.2016.1712
13. https://doi.org/10.3390/microorganisms8122022
14. https://doi.org/10.2108/zsj.13.489
15. https://doi.org/10.1073/pnas.1111712108
16. https://doi.org/10.1111/1462-2920.12908
17. https://doi.org/10.1021/cb200244t
18. https://doi.org/10.1111/mec.16668
19. https://pubmed.ncbi.nlm.nih.gov/24152714/
20. https://pubmed.ncbi.nlm.nih.gov/26013440/
21. https://doi.org/10.3390/md19060308
22. https://www.ebi.ac.uk/ols4/
23. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035502/
24. https://doi.org/10.1093/nar/gkac974
25. https://doi.org/10.1038/nbt.1823
26. https://agrovoc.fao.org/browse/agrovoc/en/page/c_49437
27. https://en.wikipedia.org/wiki/Halocynthia_roretzi