---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T21:33:10.512438'
end_time: '2026-08-17T21:41:47.774983'
duration_seconds: 517.26
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Aquatic-mammal
  habitat_identifier: habitatmech:BACDIVE.15180e7ff9
  habitat_category: OTHER
  grounding_status: UNGROUNDED
  attestations: 'BACDIVE: Aquatic-mammal'
  assertions: '69'
  parent_terms: (none)
  xrefs: FOODON:03411134
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term FOODON:03411134 'mammal' attached as a parent. Host-taxon reversal\
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
    \ not a habitat, which is a stronger and false claim. (source concept habitatmech:BACDIVE.15180e7ff9)"
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
  num_turns: 33
  total_cost_usd: 3.6783639999999993
  session_id: 405bd10b-6489-4a55-ba99-920cf999f40c
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 26
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Aquatic-mammal
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.15180e7ff9
- **Category:** OTHER
- **Grounding status:** UNGROUNDED
- **Source attestations:** BACDIVE: Aquatic-mammal
- **Upstream assertion volume:** 69
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** FOODON:03411134

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term FOODON:03411134 'mammal' attached as a parent. Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it — the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE while its own child Porifera > Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM — a phylum is a class of organisms, not a place — so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. (source concept habitatmech:BACDIVE.15180e7ff9)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Aquatic-mammal** as a microbial habitat, with citations.

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

I'll research this concept now.

# Definition research: **Aquatic-mammal** (`habitatmech:BACDIVE.15180e7ff9`)

## Proposed definition

> An **animal-associated environment** (ENVO:01001002) which is determined by a living mammal that inhabits water — a cetacean, sirenian, pinniped, or aquatic carnivoran — and which comprises that host's body sites and body products as a microbial habitat.

One-sentence caveat on scope: as delivered, BacDive's tag is *not* clean on this definition — roughly a quarter of its top-ranked strains come from **whale-fall sediment**, not from a living host (§1.3). The definition above deliberately excludes those; §6 gives the alternative if the curator prefers to define the concept as the source actually populated it.

---

## 1. What the concept denotes

### 1.1 The source concept

`bacdive.isolation_source:aquatic-mammal` is a tag in BacDive's **Microbial Isolation Source Ontology (MISO)**, a three-level controlled vocabulary used to manually index BacDive isolation-source free text. Its eight category-1 classes are `#Environmental`, `#Engineered`, `#Host`, `#Host body-site`, `#Host body-product`, `#Medical`, `#Condition` and `#Climate` ([Reimer et al. 2019, *NAR* 47:D631–D636, doi:10.1093/nar/gky879](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323973/); [BacDive isolation-source search](https://bacdive.dsmz.de/isolation-sources)). Omnicrobe puts the vocabulary at 376 terms ([Dérozier et al. 2023, *PLOS ONE* 18(1):e0272473, doi:10.1371/journal.pone.0272473](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0272473)).

`Aquatic-mammal` sits in the `#Host` branch — it names *which organism the microbe was taken from*, not a body site (that is a separate category) and not a water body. In this repo's own extract of the vocabulary, its co-tags at the same granularity are all mammal-family tags: `Bovinae-Cow,-Cattle`, `Suidae-Pig,Swine`, `Caprinae-Sheep/Goat`, `Canidae-Dog`, `Felidae-Cat`, `Equidae-Horse`, `Muridae-Mouse/Rat`, `Leporidae-Rabbit/Hare`, `Rodentia-Other` (`data/raw/bacdive_isolation_sources.tsv`). That places it as a **host-clade tag under a mammal parent**, exactly parallel to `Cnidaria-Corals`, `Porifera-Sponges` and `Invertebrates-Other`, and distinct from the *environmental* tags `Aquatic` (6,002 strains), `Marine` (2,040) and `Freshwater` — which name water bodies, not hosts. This is the strongest evidence for the host reading, and it is internal to the source. *(The parent-tag chain `#Host > #Mammals > Aquatic-mammal` reported by the BacDive UI is consistent with this but I could not verify it against the API; treat the exact parent label as unconfirmed.)*

### 1.2 What a sample is taken from — the attested taxa

The 69 strains resolve to 46 taxa; the 25 top-ranked (from `data/raw/bacdive_source_taxa.tsv`) are almost entirely **host-derived isolates from pinnipeds and cetaceans**, and their species descriptions name the body site directly:

| Taxon | Host and site as published |
|---|---|
| *Arcanobacterium phocae* (4 strains) | seals; pathogenic in marine mammals ([Ramos et al. 1997, *IJSB* 47:46–53, doi:10.1099/00207713-47-1-46](https://en.wikipedia.org/wiki/Arcanobacterium_phocae)) |
| *Streptococcus phocae* (3) | clinical specimens, harbour seal *Phoca vitulina* (Skaar et al. 1994); type strain ATCC 51973 ([genome announcement, PMC4653777](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4653777/)) |
| *Brevibacterium otitidis* (4) | CCUG 51715 / 51717 from **harbour porpoise lung** ([BacDive strain 153939](https://bacdive.dsmz.de/strain/153939)) — note the *type* strain is a human ear isolate (Pascual et al. 1996) |
| *Helicobacter cetorum* (1) | main stomach of stranded *Lagenorhynchus acutus*; also bottlenose dolphin, Pacific white-sided dolphin, beluga ([Harper et al. 2002, *JCM* 40:4536–43, PMID 12454148](https://pmc.ncbi.nlm.nih.gov/articles/PMC154630/)) |
| *Oceanivirga miroungae* (1) | oral cavity, northern elephant seal *Mirounga angustirostris* ([Volokhov et al. 2020, *IJSEM* 70:3037–48, doi:10.1099/ijsem.0.004127](https://pubmed.ncbi.nlm.nih.gov/32223835/)) |
| *Ureaplasma miroungigenitalium* (1) | northern elephant seal, urogenital |
| *Ligilactobacillus ceti* (1) | lungs and liver, stranded Cuvier's beaked whale *Ziphius cavirostris* ([Vela et al. 2008, *IJSEM* 58:891–4, PMID 18398189](https://pubmed.ncbi.nlm.nih.gov/18398189/)) |
| *Paenimyroides ceti* (3) | basonym *Flavobacterium ceti*, Vela et al. 2007, from beaked whales ([LPSN](https://lpsn.dsmz.de/species/myroides-ceti)) |
| *Corynebacterium caspium* (1) | penis of a **Caspian seal** *Pusa (Phoca) caspica* ([Collins et al. 2004, *IJSEM* 54:925–8, doi:10.1099/ijs.0.02950-0](https://pubmed.ncbi.nlm.nih.gov/15143043/)) |
| *Atopobacter phocae* (1) | common seals ([Lawson et al. 2000, *IJSEM* 50:1755–60](https://www.researchgate.net/publication/12288902_Atopobacter_phocae_gen_nov_sp_nov_a_novel_bacterium_isolated_from_common_seals)) |
| *Staphylococcus delphini* (2) | dolphin |
| *Granulicatella balaenopterae* (1) | *Balaenoptera* (baleen whale) |
| *Streptococcus iniae* (2), *Boudabousia marimammalium*, *Streptococcus marimammalium*, *Arcanobacterium pluranimalium*, *Bisgaardia hudsonensis*, *Mycoplasma* / *Ureaplasma* spp. | see §3 and §5 |

So the material a sample is taken from is: **skin, oral cavity, blowhole/respiratory tract, stomach and forestomach fluid, rectum/faeces, urogenital tract, lung, liver, wounds and abscesses of a live or freshly-stranded aquatic mammal.** These are the body sites sampled in the reference microbiome studies as well ([Bik et al. 2016, *Nat Commun* 7:10516, doi:10.1038/ncomms10516](https://www.nature.com/articles/ncomms10516) — mouth, gastric fluid, blowhole, chuff, rectum in 38 *Tursiops truncatus* and mouth/stomach/rectum in 18 *Zalophus californianus*).

### 1.3 The boundary problem — whale falls are inside the tag but should not be inside the definition

**Six of the 25 top-ranked taxa are not host-associated at all.** *Psychromonas macrocephali*, *P. ossibalaenae*, *P. aquimarina*, *Amphritea japonica*, *A. balenae* and *Neptunomonas japonica* were all isolated from **sediment adjacent to sperm whale carcasses off Kagoshima, Japan, at 228–250 m depth** ([Miyazaki et al. 2008, *IJSEM* 58:1709–14, PMID 18599721](https://pubmed.ncbi.nlm.nih.gov/18599721/); [*Amphritea* spp., *IJSEM* 58:2815–20](https://en.wikipedia.org/wiki/Amphritea_balenae)). Despite the epithet, *ossibalaenae* ("of whale bone") was published from the sediment, not the bone.

That is a **whale fall** — a deep-sea chemosynthetic sediment environment which ENVO already names as `ENVO:01000140 'whale fall'` (present in this repo's vendored slice). It is a *neighbouring concept*, not part of this one: the microbes there are free-living deep-sea psychrophiles feeding on a carcass, not symbionts or pathogens of a living mammal. Grouping them under a `#Host` tag conflates "living in a mammal" with "living on the remains of one."

**Inside the concept:** microbial communities of the body sites and body products of living (or freshly stranded/necropsied) aquatic mammals.
**Neighbouring, outside:** `ENVO:01000140` whale fall; the surrounding seawater (BacDive `Marine`, `Aquatic`); `Decomposing-animal`; `Seafood` and marine-mammal *meat* products; the mammal's captive-pool or enclosure water.

---

## 2. Genus — the broader kind

**Recommended genus: `ENVO:01001002` — "animal-associated environment"**, defined as *"An environmental system determined by an animal"*, with synonyms "Metazoan-associated environment" and "animal environment". It is in the vendored slice (`data/raw/ontology_terms.tsv`) and is the term ENVO uses for the host-as-environment pattern, alongside plant-associated and fungi-associated environment. Using it here also matches what this corpus already did for the structurally identical sibling concepts:

- `habitatmech:GOLD.e889967f4f` (Mammals as host) → `CONFIRM_UNGROUNDED`, parent `ENVO:01001002`
- `habitatmech:GOLD.3d529a667e` (Fish), `habitatmech:GOLD.47e603cf4f` (Birds), `habitatmech:GOLD.affd2445ea` (Sponges) — same disposition, same parent

**Aquatic-mammal is a proper subclass of the GOLD "Mammals" record**, so the corpus already contains its immediate genus as a HabitatMech-minted concept. Naming `habitatmech:GOLD.e889967f4f` as the direct parent and `ENVO:01001002` as the grandparent is more informative than jumping straight to ENVO.

### Near-misses in ENVO, and why each fails

I enumerated the descendants of `ENVO:01001002` via OLS. Its only *biotic* children are `ENVO:01001176` "environment associated with an aquatic invertebrate" and `ENVO:01001179` "cnidarian-associated environment"; the remaining 21 descendants are the human-settlement branch (city, village, slum, …). **ENVO has no vertebrate-associated, mammal-associated, or marine-mammal-associated environment term.** Searches of ENVO for "mammal", "vertebrate" and "marine mammal" return only unrelated hits (waterhole, sweat material, ear wax material, bile material).

| Candidate | Why it fails |
|---|---|
| `ENVO:01001002` animal-associated environment | Correct genus, far too broad for identity — grounding here would merge every host clade in the corpus onto one record. This is the reasoning already recorded on the Fish/Birds/Mammals records. |
| `ENVO:01001055` "environment associated with an animal part or small animal" | Explicitly scoped to *parts* or *small* animals; a whale is neither. Also admits dead animals, which the definition above excludes. |
| `ENVO:01001176` environment associated with an aquatic invertebrate | Disjoint — invertebrate. |
| `ENVO:01000140` whale fall | A marine sediment environment around a *carcass*. Correct for six of the attested strains (§1.3), wrong for the concept. Keep as a `see-also`/related note, not a parent. |
| `FOODON:03411134` "mammal" (current xref) | The **taxon**, not a place — correctly held as `relation: xref` per the record's decision row and the corpus rule. Also over-broad: it covers all Mammalia. |
| `FOODON:03411122` "Marine mammal" — *"A mammal that is primarily ocean-dwelling or depends on the ocean for its food"* | Closer than the current xref, but **(a)** it is a taxon-ish organism term, not an environment; **(b)** it is *narrower* than "aquatic" (§3); **(c)** its FoodOn synonym is "Cetacea", which is plainly wrong and would import a bad synonym; and **(d)** **it is not in the vendored slice** — I checked `data/raw/ontology_terms.tsv` and only `FOODON:03411134` is present. Per `CLAUDE.md`, a target outside the slice means vendoring, not weakening the check. Recommend replacing the xref with it *only* if the slice is extended. |
| `ENVO:01000161` marine sponge reef | Not applicable here; noted because the Sponges record's decision already used it as a worked example of a reef environment ≠ host. |

**ENVO's own tracker records the gap**: [issue #1029](https://github.com/EnvironmentOntology/envo/issues/1029) requests host-associated biome/feature terms on the argument that "the biome is the host organism"; it was closed without the requested terms being added. So the absence is a known, unresolved gap rather than a deliberate exclusion — which supports a term request here.

---

## 3. Differentia — what distinguishes it

Under the genus "animal-associated environment", the differentiae that separate this concept from its siblings:

**(a) Host clade — mammals, and specifically the water-dwelling ones.** Extant marine mammals are polyphyletic: they descend from terrestrial ancestors that recolonised the sea and belong to Cetacea, Sirenia, or Carnivora (Bik et al. 2016, doi:10.1038/ncomms10516). "Aquatic mammals" are explicitly *not a taxon* — they are unified by dependence on aquatic ecosystems, not by descent ([Wikipedia, *Aquatic mammal*](https://en.wikipedia.org/wiki/Aquatic_mammal), a tertiary source; the polyphyly claim itself is in Bik et al.). **This is why the concept needs an environment term rather than a taxon grounding**: no single taxon term covers it.

**(b) Aquatic, not merely marine.** This is a load-bearing distinction and the attested strains settle it:
- *Streptococcus iniae* — type strain ATCC 29178, from subcutaneous abscesses ("golf ball disease") in a captive **Amazon freshwater dolphin, *Inia geoffrensis*** ([Pier & Madin 1976, *IJSB* 26:545–553, doi:10.1099/00207713-26-4-545](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-26-4-545)).
- *Corynebacterium caspium* — from a **Caspian seal**, an endorheic brackish-lake pinniped (Collins et al. 2004, doi:10.1099/ijs.0.02950-0).

Fully freshwater aquatic mammals include river dolphins (Platanistidae, Iniidae, Lipotidae, Pontoporiidae) and the Amazonian manatee *Trichechus inunguis*; the Baikal seal *Pusa sibirica* is an exclusively freshwater pinniped ([River dolphin](https://en.wikipedia.org/wiki/River_dolphin); [Baikal seal](https://en.wikipedia.org/wiki/Baikal_seal) — tertiary sources, cited for the enumeration only). Defining this concept as "marine" would exclude two of its own attested type strains.

**(c) The habitat is compositionally distinct from both the surrounding water and from other mammals.** This is the single strongest published warrant for the concept existing as a habitat at all, rather than being reducible to "seawater" or to "mammal":
- Across 337 samples from 5 body sites in 48 dolphins and 18 sea lions, bacterial compositions were **distinct from those of other mammals, from dietary fish, and from adjacent seawater**, and varied by body site and host species; ~70% of near-full-length 16S rRNA sequences from dolphins were unique; dolphins showed a **paucity of Bacteroidetes in the distal gut** (<1%) despite Bacteroidetes dominating the distal gut of most other mammals including dugong and pinnipeds; and abundant, poorly characterised Tenericutes occurred in gastric fluid (Bik et al. 2016, doi:10.1038/ncomms10516, PMID 26839246).
- Skin microbiota across nine marine mammal species in four families (Physeteridae, Delphinidae, Balaenopteridae, Phocidae) are **structured by host species identity and host phylogeny** ([Apprill et al., *Environ Microbiol*; NOAA repository copy](https://repository.library.noaa.gov/view/noaa/52489/noaa_52489_DS1.pdf)).
- In captivity, cetacean skin microbiota is **more diverse than the planktonic community** of the pool water, differs between bottlenose dolphin and killer whale, and varies more between individuals than between body parts ([Chiarello et al. 2017, *Sci Rep* 7:15269, doi:10.1038/s41598-017-15220-z](https://www.nature.com/articles/s41598-017-15220-z)).
- Cetacean gut microbiomes show **phylosymbiosis**, with diet further shaping diversity in toothed vs. baleen whales ([Cetacea gut microbiome meta-analysis 2024, *Sci Total Environ*, doi:10.1016/j.scitotenv.2024.173628](https://www.sciencedirect.com/science/article/pii/S0048969724030900)).

**(d) One physiologically distinctive body site.** The **blowhole** is a habitat with no terrestrial-mammal counterpart: the cetacean respiratory tract is directly exposed to both the surface-water and air microbiomes at each breath ([Vlasova-St. Louis et al. / Frontiers review, *Front Microbiol* 12:567408, doi:10.3389/fmicb.2021.567408](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2021.567408/full)). Useful as a supporting example in the term's comment field; too narrow for the differentia proper.

**(e) Sampling regime, which shapes the attested taxa.** Access to gut samples is constrained because most species are rare, endangered and deep-diving, so the standard approach is environmental faecal collection with sampling of the uncontaminated centre (same Frontiers review). Combined with the fact that most named taxa above were described from **stranded or clinically ill animals**, this means the strain-level evidence under this tag is enriched for pathogens and opportunists relative to the amplicon literature. Worth a comment on the term; it is an artefact of ascertainment, not a property of the habitat.

---

## 4. Confidence and provenance of each claim

| Claim | Basis |
|---|---|
| MISO structure, `#Host` category | Reimer et al. 2019 (primary), BacDive site |
| `Aquatic-mammal` is a host tag, sibling of mammal-family tags | **My inference** from `data/raw/bacdive_isolation_sources.tsv` co-tags + the `#Host` category definition. The exact parent tag is unverified. |
| Each species' host and body site | Primary species descriptions, cited individually above |
| Whale-fall strains are sediment isolates | Miyazaki et al. 2008 (primary), explicit in the title |
| ENVO has no mammal/vertebrate-associated environment term | **My finding**, from exhaustive OLS4 enumeration of `ENVO:01001002` descendants (23 terms, all listed) + keyword searches. Negative evidence — reproducible but not published. |
| `FOODON:03411122` absent from the vendored slice | Direct grep of `data/raw/ontology_terms.tsv` |
| Habitat is distinct from seawater and from other mammals | Bik et al. 2016, Apprill et al., Chiarello et al. 2017 (all primary) |
| Aquatic ⊋ marine | Pier & Madin 1976 and Collins et al. 2004 (primary, for the two freshwater/brackish type strains); enumeration of freshwater taxa from tertiary sources |
| Sampling bias toward stranded/diseased animals | **My inference** from the pattern across the 25 species descriptions, corroborated by the Frontiers review's statement on sampling constraints |

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept (candidate exact/related synonyms):**
- aquatic mammal host
- aquatic mammal-associated environment
- marine mammal host / marine-mammal-associated environment *(related, narrower — see below)*
- aquatic mammal microbiome / marine mammal microbiome *(the community, used loosely for the habitat)*
- cetacean-associated environment, pinniped-associated environment *(narrower; both are children)*

**Do NOT conflate:**

1. **"Marine mammal" ≠ "aquatic mammal".** Marine mammal is the narrower, better-established term; it excludes river dolphins, the Amazonian manatee, and the Baikal and Caspian seals. Two of this record's own type strains come from freshwater/brackish hosts. If a `marine mammal` synonym is added, mark it **NARROW**, never EXACT. Separately, FoodOn's `FOODON:03411122` carries the synonym "Cetacea", which is wrong — cetaceans are one of at least four independent lineages.

2. **Whale fall (`ENVO:01000140`) is a different habitat.** Deep-sea sediment supporting a chemosynthetic community around a carcass, over decades. Six attested strains here belong to it. Related, not the same.

3. **The surrounding water is a different habitat.** BacDive's own `Marine`, `Aquatic`, `Freshwater` and `Brackish` tags are `#Environmental`. The whole point of Bik et al. 2016 and Chiarello et al. 2017 is that the host communities are *not* the water's communities.

4. **`FOODON:03411134` "mammal" is the taxon, not the habitat.** Already correctly held as `relation: xref` on this record. Do not promote it to `parent_habitats` — it is a class of organisms, and per the corpus rule (#99) that would publish an is-a over-claim.

5. **Aquatic mammals as *food* ≠ aquatic mammals as *host*.** BacDive's `Seafood`, `Animal-produced-food-natural`, and FoodOn's `FOODON:00005681 marine mammal material` / `FOODON:00001006 mammalian meat food product` are the food-product reading. Relevant precedent: *Arcanobacterium phocae* moved from seals into farmed mink because seal meat was used as mink feed, causing fur animal epidemic necrotic pyoderma ([Nordgren et al. 2016, PMC5156405](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5156405/)) — same organism, three different habitats.

6. **Semi-aquatic terrestrial mammals are a judgement call, and the definition should say which way it falls.** Hippopotamus, capybara, beaver, muskrat and river otter are conventionally called semi-aquatic ([Wikipedia, *Aquatic mammal*](https://en.wikipedia.org/wiki/Aquatic_mammal)). No strain under this tag is attested from any of them; the polar bear and sea otter (*Enhydra lutris*, cf. *Mycoplasma enhydrae*) are borderline but are conventionally counted as marine mammals. **Recommendation: include obligate/marine carnivorans (sea otter, polar bear), exclude terrestrial semi-aquatic mammals, and state the exclusion in the term's comment** — otherwise the boundary will be re-litigated. This is my recommendation, not a source's ruling.

7. **Host-clade tag ≠ body site.** BacDive keeps `#Host` and `#Host body-site` as separate categories, so a dolphin blowhole swab carries *both* `Aquatic-mammal` and `Airways`. This concept is the host axis only; the anatomy grounds separately (per the parts-vs-whole rule in `CLAUDE.md`).

---

## 6. Should it be a term at all?

**Yes — as an ENVO term request for an aquatic-mammal-associated environment, exactly matching the disposition already recorded for Fish, Birds, Mammals and Sponges.**

The concept survives every screen the corpus applies:

- It is **not a taxon term**. There is no taxon for aquatic mammals; the group is polyphyletic across Cetacea, Sirenia and Carnivora (Bik et al. 2016). The taxon reading is already parked as an xref.
- It is **not a quality, process, disease or procedure** — the categories `NOT_APPLICABLE` is reserved for.
- It is **not a sampling artefact**. 69 strains, 46 taxa, and at least fourteen validly-published species whose names encode this host group as their defining ecology: *phocae* (×3 genera), *marimammalium* (×2), *ceti* (×2), *miroungae*/*miroungigenitalium* (×2), *cetorum*, *balaenopterae*, *delphini*, *caspium*, *iniae*. Naming that many species after a habitat is about as strong an attestation of habitat-hood as microbiology produces.
- **No ontology names it.** Verified by enumerating all 23 descendants of `ENVO:01001002`; ENVO issue #1029 shows the gap is known and unfilled.

**Three flags for the curator:**

1. **The whale-fall contamination (§1.3) must be handled explicitly.** Either (a) define the term as the *living-host* environment, as proposed above, and add a comment that six BacDive strains under this tag are whale-fall sediment isolates properly belonging to `ENVO:01000140` — this is what I recommend, since it keeps the definition true to what "host" means and to how the other host-clade records in this corpus are defined; or (b) define it as "an environment determined by an aquatic mammal, living or dead", which matches BacDive's actual tag extension but merges two ecologically unrelated habitats and would make the term's genus `ENVO:01001055` ("living or dead animal") rather than `ENVO:01001002`. Option (b) is defensible only if the corpus values source fidelity over ecological coherence here; nothing else in the corpus makes that trade.

2. **`habitat_category` is `OTHER`, but the sibling records (Fish, Birds, Mammals) are `HOST_ASSOCIATED`.** If the host-taxon reversal (#114) is being applied consistently, this record's category is now inconsistent with its own decision. That is a seeder question, not a definition question, but it will look like an error in `just report`.

3. **The xref should arguably move from `FOODON:03411134` "mammal" to `FOODON:03411122` "Marine mammal"** — closer, though still narrower than the concept and carrying a wrong "Cetacea" synonym. Blocked on vendoring: `FOODON:03411122` is not in `data/raw/ontology_terms.tsv`. If the slice is not extended, keeping `FOODON:03411134` as the xref is the correct conservative choice, since it is broader rather than wrong.

---

## Sources

- [Bik EM et al. (2016) Marine mammals harbor unique microbiotas shaped by and yet distinct from the sea. *Nat Commun* 7:10516. doi:10.1038/ncomms10516, PMID 26839246](https://www.nature.com/articles/ncomms10516)
- [Chiarello M et al. (2017) Captive bottlenose dolphins and killer whales harbor a species-specific skin microbiota. *Sci Rep* 7:15269. doi:10.1038/s41598-017-15220-z](https://www.nature.com/articles/s41598-017-15220-z)
- [Apprill A et al. Marine mammal skin microbiotas are influenced by host phylogeny (NOAA repository copy)](https://repository.library.noaa.gov/view/noaa/52489/noaa_52489_DS1.pdf)
- [Meta-analysis of the Cetacea gut microbiome (2024) *Sci Total Environ*](https://www.sciencedirect.com/science/article/pii/S0048969724030900)
- [Microbiome Composition and Function in Aquatic Vertebrates (2021) *Front Microbiol* 12:567408. doi:10.3389/fmicb.2021.567408](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2021.567408/full)
- [Miyazaki M et al. (2008) *Psychromonas* spp. from sediment adjacent to sperm whale carcasses. *IJSEM* 58:1709–14. PMID 18599721](https://pubmed.ncbi.nlm.nih.gov/18599721/)
- [Pier GB & Madin SH (1976) *Streptococcus iniae* sp. nov. from an Amazon freshwater dolphin. *IJSB* 26:545–553. doi:10.1099/00207713-26-4-545](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-26-4-545)
- [Collins MD et al. (2004) *Corynebacterium caspium* sp. nov. from a Caspian seal. *IJSEM* 54:925–8. doi:10.1099/ijs.0.02950-0](https://pubmed.ncbi.nlm.nih.gov/15143043/)
- [Harper CG et al. (2002) *Helicobacter cetorum* sp. nov. *J Clin Microbiol* 40:4536–43. PMID 12454148](https://pmc.ncbi.nlm.nih.gov/articles/PMC154630/)
- [Volokhov DV et al. (2020) *Oceanivirga miroungae* sp. nov. *IJSEM* 70:3037–48. doi:10.1099/ijsem.0.004127](https://pubmed.ncbi.nlm.nih.gov/32223835/)
- [Vela AI et al. (2008) *Lactobacillus ceti* sp. nov. from beaked whales. *IJSEM* 58:891–4. PMID 18398189](https://pubmed.ncbi.nlm.nih.gov/18398189/)
- [Genome of *Streptococcus phocae* subsp. *phocae* ATCC 51973ᵀ from harbor seal](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4653777/)
- [Nordgren H et al. (2016) *Arcanobacterium phocae* as causative agent of fur animal epidemic necrotic pyoderma](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5156405/)
- [Reimer LC et al. (2019) BacDive in 2019. *NAR* 47:D631–D636. doi:10.1093/nar/gky879](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323973/)
- [Reimer LC et al. (2022) BacDive in 2022. *NAR* 50:D741–D746. doi:10.1093/nar/gkab961](https://pmc.ncbi.nlm.nih.gov/articles/PMC8728306/)
- [BacDive isolation sources search](https://bacdive.dsmz.de/isolation-sources) · [BacDive strain 153939, *Brevibacterium otitidis* CCUG 51715](https://bacdive.dsmz.de/strain/153939)
- [Dérozier S et al. (2023) Omnicrobe. *PLOS ONE* 18(1):e0272473. doi:10.1371/journal.pone.0272473](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0272473)
- [ENVO issue #1029 — EnvO terms for host-associated samples](https://github.com/EnvironmentOntology/envo/issues/1029)
- [Wikipedia: Aquatic mammal](https://en.wikipedia.org/wiki/Aquatic_mammal) · [River dolphin](https://en.wikipedia.org/wiki/River_dolphin) · [Baikal seal](https://en.wikipedia.org/wiki/Baikal_seal) — tertiary, cited only for enumerations of aquatic mammal groups
- ENVO term records verified via EBI OLS4 API: `ENVO:01001002`, `ENVO:01001055`, `ENVO:01001176`, `ENVO:01001179`, `ENVO:01000140`; FoodOn `FOODON:03411122`, `FOODON:03411134`

## Citations

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC6323973/
2. https://bacdive.dsmz.de/isolation-sources
3. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0272473
4. https://en.wikipedia.org/wiki/Arcanobacterium_phocae
5. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4653777/
6. https://bacdive.dsmz.de/strain/153939
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC154630/
8. https://pubmed.ncbi.nlm.nih.gov/32223835/
9. https://pubmed.ncbi.nlm.nih.gov/18398189/
10. https://lpsn.dsmz.de/species/myroides-ceti
11. https://pubmed.ncbi.nlm.nih.gov/15143043/
12. https://www.researchgate.net/publication/12288902_Atopobacter_phocae_gen_nov_sp_nov_a_novel_bacterium_isolated_from_common_seals
13. https://www.nature.com/articles/ncomms10516
14. https://pubmed.ncbi.nlm.nih.gov/18599721/
15. https://en.wikipedia.org/wiki/Amphritea_balenae
16. https://github.com/EnvironmentOntology/envo/issues/1029
17. https://en.wikipedia.org/wiki/Aquatic_mammal
18. https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-26-4-545
19. https://en.wikipedia.org/wiki/River_dolphin
20. https://en.wikipedia.org/wiki/Baikal_seal
21. https://repository.library.noaa.gov/view/noaa/52489/noaa_52489_DS1.pdf
22. https://www.nature.com/articles/s41598-017-15220-z
23. https://www.sciencedirect.com/science/article/pii/S0048969724030900
24. https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2021.567408/full
25. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5156405/
26. https://pmc.ncbi.nlm.nih.gov/articles/PMC8728306/