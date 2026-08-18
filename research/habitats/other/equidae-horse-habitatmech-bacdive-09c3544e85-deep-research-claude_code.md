---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T17:06:10.546499'
end_time: '2026-08-17T17:14:31.999438'
duration_seconds: 501.45
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Equidae-Horse
  habitat_identifier: habitatmech:BACDIVE.09c3544e85
  habitat_category: OTHER
  grounding_status: UNGROUNDED
  attestations: 'BACDIVE: Equidae-Horse'
  assertions: '269'
  parent_terms: (none)
  xrefs: (none)
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Host-taxon\
    \ reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon\
    \ is not a habitat'. That reasoning is wrong, and the corpus already contradicted\
    \ it \u2014 the same kind of concept was treated as a habitat for Sponge, Nematoda,\
    \ Reptilia, Mammals, Birds and Fish, which keep their own identity and a term\
    \ request for an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE\
    \ while its own child Porifera > Sponge was a term request.An organism acting\
    \ as a host IS a habitat: it is where the microbe lives, and ENVO models exactly\
    \ this at plant-associated, animal-associated and fungi-associated environment.\
    \ What is not a habitat is the TAXON TERM \u2014 a phylum is a class of organisms,\
    \ not a place \u2014 so the taxon stays an xref (#99) and the concept keeps its\
    \ own identity as a term-request candidate. NOT_APPLICABLE said the concept is\
    \ not a habitat, which is a stronger and false claim. (source concept habitatmech:BACDIVE.09c3544e85)"
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
  web_search_requests: 9
  num_turns: 30
  total_cost_usd: 2.695919
  session_id: f45f311b-e255-4c78-bfd1-9ec087945ff9
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 27
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Equidae-Horse
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.09c3544e85
- **Category:** OTHER
- **Grounding status:** UNGROUNDED
- **Source attestations:** BACDIVE: Equidae-Horse
- **Upstream assertion volume:** 269
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it — the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE while its own child Porifera > Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM — a phylum is a class of organisms, not a place — so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. (source concept habitatmech:BACDIVE.09c3544e85)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Equidae-Horse** as a microbial habitat, with citations.

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

# HabitatMech novel-term research — `habitatmech:BACDIVE.09c3544e85` "Equidae-Horse"

## Proposed definition

> An animal-associated environment which is determined by a living or dead horse or other equid (family Equidae), a monogastric hindgut-fermenting herbivore, considered as a whole host organism rather than as one of its named body sites or body products.

If the curator prefers a narrower, more defensible scope (see §1.3 on the label's ambiguity), the horse-only reading is:

> An animal-associated environment which is determined by a living or dead domestic horse (*Equus caballus*), a monogastric hindgut-fermenting herbivore, considered as a whole host organism rather than as one of its named body sites or body products.

The "whole organism rather than a body site" clause is not stylistic — it is the differentia that upstream actually encodes, and it is what separates this record from a `gut`/`skin`/`blood` record (§3.1). The genus term used, `ENVO:01001002 animal-associated environment`, is two levels too broad; see §2.3 for the missing intermediate class.

---

## 1. What the concept denotes

### 1.1 Provenance of the label

"Equidae-Horse" is not free prose. It is a slugified BacDive isolation-source tag. BacDive classifies isolation sources with a controlled vocabulary (the Microbial Isolation Source ontology, MISO) that is **hierarchically ordered into exactly three levels of tags**, with eight top-level classes: `#Environmental`, `#Engineered`, `#Host`, `#Host body-site`, `#Host body-product`, `#Medical`, `#Condition`, `#Climate` ([Reimer et al., *BacDive in 2019*, Nucleic Acids Res 47:D631–D636, doi:10.1093/nar/gky879](https://academic.oup.com/nar/article/47/D1/D631/5106998)). Browsing the live vocabulary confirms the path for this concept is:

**`#Host` → `#Mammals` → `#Equidae (Horse)`** ([BacDive isolation-sources browser](https://bacdive.dsmz.de/isolation-sources))

This path is the single most important piece of evidence in this report, for two reasons.

### 1.2 What a sample tagged this way is

Because BacDive keeps `#Host`, `#Host body-site` and `#Host body-product` as **three sibling top-level classes**, the `#Host` branch names *which organism the strain came out of*, and the anatomical site or product is recorded separately on the same strain record. A strain tagged `#Equidae (Horse)` is therefore a strain isolated **from a horse** — the horse being the sampled body, whatever the specific site. The concept denotes the horse's body as a colonisable environment: its gut lumen and mucosa, respiratory tract, skin and hair coat, urogenital tract, milk, blood and internal tissues, and clinical lesions therein.

The 269 strains and 124 distinct taxa on this record bear this out. The top-ranked attested taxa span at least four distinct anatomical compartments:

| Attested taxon (rank, strains) | Compartment implied |
|---|---|
| *Nicoletella semolina* (1, 19) | upper/lower airway ([Kuhnert et al. 2004, J Clin Microbiol 42:5542–5548, PMID 15583279](https://pubmed.ncbi.nlm.nih.gov/15583279/) — type strain from the **trachea of a horse**, Bern) |
| *Pasteurella caballi* (2, 17) | respiratory tract / wounds |
| *Dermatophilus congolensis* (4, 10) | skin |
| *Prescottella (Rhodococcus) equi* (6, 8) | lung, foals ([Merck Veterinary Manual, *Rhodococcus equi* pneumonia in foals](https://www.merckvetmanual.com/respiratory-system/respiratory-diseases-of-horses/rhodococcus-equi-pneumonia-in-foals)) |
| *Taylorella equigenitalis* (10, 6) | external genitalia / uterus ([Hébert et al. 2012, PLoS ONE, PMC3250509](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3250509/)) |
| *Streptococcus equi* + subsp. *zooepidemicus* (12–13, 9) | upper respiratory tract, lymph nodes ([PMC11067117](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11067117/)) |
| *Corynebacterium uterequi* (17, 3) | uterus |
| *Myxococcus fulvus / virescens / stipitatus*, *Corallococcus coralloides* (3, 8, 11, 25; 26 strains combined) | **soil myxobacteria — see §5.2** |

*Ranking, counts and taxon labels are read directly from `data/habitats/other/equidae_horse.yaml` and `data/raw/bacdive_source_taxa.tsv`. Compartment attributions for* Dermatophilus congolensis *and* Pasteurella caballi *are standard veterinary-microbiology knowledge that I did not verify against a source in this pass; the other rows are cited.*

### 1.3 The label is ambiguous, and the two readings differ

**Reading A — the domestic horse.** BacDive's own gloss is "(Horse)", and the attested taxon list is overwhelmingly horse-specific: *Taylorella equigenitalis* "is a pathogen of equids and does not affect other livestock or people"; *Streptococcus equi* subsp. *equi* is the agent of strangles, an equine URT disease; *Nicoletella semolina* was described from horses with airway disease; *Corynebacterium uterequi* and *Actinobacillus equuli* are named for the horse. Reading A is what the data means in practice.

**Reading B — the family Equidae.** The tag's first token is the family name, and the family contains not just the horse but domestic donkeys, and wild asses and zebras — one extant genus, *Equus*, with seven living species by the [IUCN Equid Specialist Group's reckoning](https://portals.iucn.org/library/node/8130) (some schemes give eight to ten, disagreeing over whether domestic forms are split from their wild ancestors). Reading B is not empty: donkey and wild-ass hindgut communities are separately characterised and **measurably differ from the horse's** — ponies, donkeys and pony×donkey hybrids on an identical forage diet had significantly different prokaryotic and anaerobic-fungal community composition, with *Lachnoclostridium 10* and a Lachnospiraceae genus enriched in donkeys, attributed in part to the donkey's longer feed retention time ([Edwards et al. 2020, *Animal Microbiome* 2:8, doi:10.1186/s42523-020-00027-7](https://link.springer.com/article/10.1186/s42523-020-00027-7)); Tibetan wild asses and domestic donkeys differ sharply in beta diversity ([PMC7276150](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7276150/)).

**Recommendation:** do not silently pick. The upstream grounding row that suggested `NCBITaxon:9788` Equidae is machine-generated — `semapv:LexicalMatching`, `ols4_auto`, `medium` confidence, `skos:closeMatch` (`data/raw/isolation_source_groundings.tsv`). It is an artefact of matching the label *string*, not a curator's statement that donkeys and zebras are in scope. The defensible move is to define on Reading A (horse), keep `NCBITaxon:9788` as an `xref` recording what upstream matched, and add `NCBITaxon:9796` *Equus caballus* as the more precise host xref. This is my recommendation, not a claim any source makes.

### 1.4 Boundary — what is inside and what is next door

| Inside | Neighbouring concept |
|---|---|
| A strain isolated from a horse, at any body site | A strain isolated from *horse manure once it is a substrate in its own right* — that is `ENVO:00003859 horse manure`, a material, and in a compost or field context an environmental sample, not a host sample |
| Horse tissues, fluids and surfaces as colonised habitat | The **anatomical site** as such — `gut`, `skin`, `lung`, `blood` ground to UBERON and are separate HabitatMech records; per CLAUDE.md, a host's *parts* ground to the anatomy term |
| The horse as a host organism | The **taxon** *Equidae* / *Equus caballus* — a class of organisms, not a place (`relation: xref`, per #99/#114) |
| Live and recently dead horse | The **stable, paddock or pasture** the horse stands in — `ENVO:03501287 livestock house`, `ENVO:00000266 pasture` |
| Bacteria from horse tissue | Bacteria that merely *transited* the horse from soil or bedding — see §5.2 |

---

## 2. Genus — the broader kind

### 2.1 The one term that fits

**`ENVO:01001002` — animal-associated environment**, *"An environmental system determined by an animal."* Synonyms: *Metazoan-associated environment*, *animal environment*; alternative label *Animal*; in the `envoEmpo`, `envoMeo` and `envoOmics` subsets ([OLS4/ENVO](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002)). Its parent is `ENVO:01001000 environmental system determined by an organism`.

This is the correct genus and it is exactly the modelling pattern the curation note appeals to: ENVO already asserts that an organism acting as a host constitutes an environmental system. It is, however, **very** broad — every metazoan host in the corpus lands on it, which is the reason the sibling `Mammals` record (`habitatmech:GOLD.e889967f4f`) was parented there rather than grounded there.

### 2.2 Near-misses and why each fails

| Term | Why it is not the match |
|---|---|
| `ENVO:01001055` *environment associated with an animal part or small animal* — "An environmental system determined by **part** of a living or dead animal, or a **whole small animal**." | Scope-wrong in both disjuncts. A horse is neither a part nor a small animal; adopting it would assert the sample is a body part, which BacDive's separate `#Host body-site` branch specifically denies. |
| `ENVO:01001179` *cnidarian-associated environment* — "An environmental system determined by a cnidarian or part of a cnidarian." | Not a match, but the **most useful precedent in the report**: it is the one place ENVO has already minted a clade-specific child of `animal-associated environment`, and its definition string is a ready-made template — "An environmental system determined by a ⟨clade member⟩ or part of a ⟨clade member⟩." |
| `ENVO:00003859` *horse manure* | The only ENVO term whose label contains "horse". It has **no textual definition at all** (only an `oboInOwl:hasDbXref` to the Wikipedia article) and is a *material*, narrower than and categorially distinct from the host organism. Useful as a `see also`, not as genus or identity. |
| `ENVO:03501287` *livestock house*, `ENVO:00000266` *pasture*, `ENVO:01000627` *feedlot*, `ENVO:01001207` *ranch* | These are the horse's *surroundings*, not the horse. Adopting one asserts a built or land environment the BacDive strains were not sampled from. |
| `NCBITaxon:9788` *Equidae*, `NCBITaxon:9796` *Equus caballus* | Taxon terms. A family is a class of organisms, not a place — this is the #99/#114 line. Correct as `relation: xref`; wrong as identity or as `parent_habitats`. |
| `FOODON:00001111` *equine dairy food product*, `FOODON:00001121` *equine milk beverage* | The only other "equine" terms in the OBO space. These are food products, an entirely different genus, and they assert processing for human consumption that no BacDive strain record claims. |
| `UBERON:*` (`skin of body`, `lung`, …) | Parts, not the whole host. Grounding here is right for the sibling body-site records and wrong here. |

**Searches run:** OLS4 over ENVO for `horse`, `equine`, `equus`, `livestock`, `domestic animal`, `mammal`, `dung`, `vertebrate-associated`; OLS4 across all ontologies for `horse-associated`, `equine-associated`, `cattle-associated environment`, `host-associated environment`. **No `<clade>-associated environment` term exists for any mammal, and none exists for the horse.** The `UNGROUNDED` status is correct.

### 2.3 An intermediate class is missing, and that is the more useful finding

Enumerating the children of `ENVO:01001002` returns essentially one clade child (`ENVO:01001179 cnidarian-associated environment`), alongside `ENVO:01001176 environment associated with an aquatic invertebrate` and `ENVO:01001829 human settlement`. **There is no `mammal-associated environment`, no `vertebrate-associated environment`, and no `domesticated animal-associated environment`.** So the definition above has to jump from "horse" straight to "animal", which is exactly the symptom the output brief describes.

This is a corpus-level, not a record-level, problem. BacDive's `#Host → #Mammals` level-2 tag has seven mammal-family level-3 siblings in `data/raw/bacdive_isolation_sources.tsv`, all with the same shape and all in the same position:

| BacDive tag | Strains |
|---|---|
| Bovinae-Cow,-Cattle | 619 |
| Suidae-Pig,Swine | 521 |
| Caprinae-Sheep/Goat | 412 |
| Canidae-Dog | 344 |
| Muridae-Mouse/Rat | 325 |
| **Equidae-Horse** | **269** |
| Leporidae-Rabbit/Hare | 217 |

Whatever ENVO request comes out of this record should be made for the set, with `mammal-associated environment` requested as the shared intermediate, not seven flat siblings hanging off `animal-associated environment`. *(This is my recommendation; no source states it. Note the standing memory constraint: any actual ENVO submission needs its own explicit per-request permission.)*

---

## 3. Differentia — what distinguishes a horse from its siblings under that genus

Two differentiae are available. Prefer the first; it is what the source data encodes. The second is what makes the concept biologically non-arbitrary.

### 3.1 Structural differentia (from the source vocabulary)

The sample is the **whole host organism**, not a body site or body product. This is directly readable off MISO's three sibling top-level classes `#Host` / `#Host body-site` / `#Host body-product` ([Reimer et al. 2019](https://academic.oup.com/nar/article/47/D1/D631/5106998)). It is the clause that keeps this record from colliding with `gut`, `skin`, `oral cavity and airways` and `feces` records, which are separately attested in the same BacDive inventory (`Oral-cavity-and-airways` 2102, `Feces-Stool` 2421, `Skin,-Nail,-Hair` 260).

### 3.2 Physiological differentia (observable, measurable, and the real content)

The horse is a **monogastric, herbivorous, hindgut fermenter** — and this is precisely what separates it from the two largest sibling tags, *Bovinae* and *Caprinae*, which are foregut-fermenting ruminants.

- The equine digestive system "differs from that of ruminants, particularly in the absence of a rumen, reticulum, omasum, and abomasum"; equines compensate through cecal and colonic anaerobic fermentation ([Li et al. 2025, *Front Microbiol* 16:1602258, doi:10.3389/fmicb.2025.1602258, PMID 41070119](https://pmc.ncbi.nlm.nih.gov/articles/PMC12504203/)).
- Fermentation is localised to the cecum and colon, contributes **≈30–40% of total energy requirements** via short-chain fatty acids, and the cecum is weakly acidic at **pH 6–7** (Li et al. 2025, ibid.). The hindgut is roughly **62% of total GI volume** ([Rutgers NJAES E375, *The Equine Hindgut Microbiome*](https://njaes.rutgers.edu/e375/)).
- Sampling seven regions (dorsal stomach, antral stomach, jejunum, ileum, cecum, ventral colon, dorsal colon), luminal and mucosal, in healthy adult horses: Proteobacteria and Firmicutes dominate the upper tract; Firmicutes and Bacteroidetes dominate the lower tract with lower Verrucomicrobia, Tenericutes, Spirochaetes and Fibrobacteres; the cecum and colon carry the highest bacterial densities and the most uniform composition, and a **distinct compositional divide** separates upper from lower ([Ericsson et al. 2016, *PLoS ONE* 11(11):e0166523, doi:10.1371/journal.pone.0166523](https://pmc.ncbi.nlm.nih.gov/articles/PMC5112786/)).
- Firmicutes + Bacteroidetes together are ≈**78.50%** of the horse gut community, versus ≈**87.91%** in the donkey (Li et al. 2025, ibid.) — a quantitative reason not to collapse Reading A and Reading B.
- Internal structure is finer still: the **pelvic flexure separates distinct microbial communities** within the hindgut ([Sci Rep 11:4085, 2021, doi:10.1038/s41598-021-83783-z](https://www.nature.com/articles/s41598-021-83783-z)).
- Skin: 30 samples from five body sites of healthy ponies (V3–V4) recovered **18 phyla, 29 classes, 119 families**, dominated by Proteobacteria (30.8 ± 9.1%), Actinobacteriota (20.4 ± 7.6%), Firmicutes (19.5 ± 10.1%), Bacteroidota (8.5 ± 5.0%) and Deinococcota ([Strompfová & Štempelová 2024, *Vet Res Commun*, PMC11315781](https://pmc.ncbi.nlm.nih.gov/articles/PMC11315781/)); a culture-based study from southern Germany reaches complementary conclusions and flags Deinococcota as the point of disagreement between studies ([*Microorganisms* 2025, 13(3):623](https://www.mdpi.com/2076-2607/13/3/623)).
- Scale of current sampling: **2,362 equine faecal microbiomes** from veterinary teaching hospitals in three countries ([PMC12676801](https://pmc.ncbi.nlm.nih.gov/articles/PMC12676801/)).

### 3.3 Host-restricted microbiota as supporting evidence

Several taxa on this record are effectively unknown outside equids, which is the strongest available argument that this is a *distinct habitat* rather than an arbitrary slice of "mammal":

- *Taylorella equigenitalis* — agent of contagious equine metritis, a WOAH-notifiable disease; a Gram-negative capnophilic coccobacillus of *Alcaligenaceae*, colonising stallion external genitalia asymptomatically and causing endometritis/cervicitis in mares; **a pathogen of equids that does not affect other livestock or people** ([PMC3250509](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3250509/); [Czech WGS study, PMC11698419](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11698419/)).
- *Nicoletella semolina* — described from horse airways; screening of 1,770 nose swabs and 1,132 tracheal aspirates found it at similar frequency in diseased and healthy horses, so it reads as an **equine airway commensal**, not a primary pathogen ([Kuhnert et al. 2004, PMID 15583279](https://pubmed.ncbi.nlm.nih.gov/15583279/); [*Vet Microbiol* screening study](https://www.sciencedirect.com/science/article/abs/pii/S0378113512005147)).
- *Streptococcus equi* subsp. *equi* — strangles, an acute contagious URT infection with lymphadenitis and abscessation, high morbidity/low mortality in naive populations ([PMC11067117](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11067117/)).
- *Prescottella equi* (= *Rhodococcus equi*) — chronic suppurative bronchopneumonia in foals 1–5 months old, the most common serious pneumonia of that age class; virulence determined by pVAP plasmids encoding VapA ([Merck Vet Manual](https://www.merckvetmanual.com/respiratory-system/respiratory-diseases-of-horses/rhodococcus-equi-pneumonia-in-foals)). Nomenclature is unstable: the binomial *Prescottella equi* gen. nov., comb. nov. was validly published following Judicial Commission Opinion 106 ([Sangal et al., *IJSEM*, doi:10.1099/ijsem.0.005551](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.005551)), and reclassification back into *Rhodococcus* has since been proposed. **Do not "correct" the record's `Prescottella equi` label to `Rhodococcus equi` or vice versa without checking which NCBI Taxonomy node `NCBITaxon:43767` currently carries.**

### 3.4 A differentia deliberately *not* used

The horse is domesticated, and the domestication history is well resolved — modern domestic horses derive from the lower Volga-Don region of the Western Eurasian steppes, spreading from ≈4,200 years ago and replacing other lineages by ≈3,000 years ago, on 273 ancient genomes ([Librado et al. 2021, *Nature* 598:634–640, doi:10.1038/s41586-021-04018-9](https://www.nature.com/articles/s41586-021-04018-9)). I recommend **against** putting "domesticated" in the definition: it is an origin claim about the host population, not an observable property of the habitat, it would exclude feral and Przewalski's horses that legitimately fall under the concept, and the semi-feral-versus-managed foal comparison shows management is a *modifier* of the community, not a boundary of it ([PMC7807438](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7807438/)).

---

## 4. Sources

Consolidated, with what each supports.

**Source vocabulary and ontology**
- Reimer LC et al. *BacDive in 2019: bacterial phenotypic data for high-throughput biodiversity analysis.* Nucleic Acids Res 47:D631–D636. doi:[10.1093/nar/gky879](https://academic.oup.com/nar/article/47/D1/D631/5106998) — MISO three-level structure, eight top-level classes.
- [BacDive isolation-sources browser](https://bacdive.dsmz.de/isolation-sources) — the `#Host → #Mammals → #Equidae (Horse)` path.
- ENVO via OLS4: [`ENVO:01001002`](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002), `ENVO:01001000`, `ENVO:01001055`, `ENVO:01001179`, `ENVO:00003859`, `ENVO:03501287`, `ENVO:00000266`.
- ENA Taxonomy REST: [taxon 9788 *Equidae*](https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/9788) (rank: family; GenBank common name "horses"); [taxon 9796 *Equus caballus*](https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/9796) (rank: species; synonyms *Equus ferus caballus*, *Equus przewalskii f. caballus*).

**Habitat physiology and community composition**
- Ericsson AC, Johnson PJ, Lopes MA, Perry SC, Lanter HR (2016) *A microbiological map of the healthy equine gastrointestinal tract.* PLoS ONE 11(11):e0166523. doi:[10.1371/journal.pone.0166523](https://pmc.ncbi.nlm.nih.gov/articles/PMC5112786/)
- Li F et al. (2025) *Gut microbiome regulation in equine animals.* Front Microbiol 16:1602258. doi:[10.3389/fmicb.2025.1602258](https://pmc.ncbi.nlm.nih.gov/articles/PMC12504203/), PMID 41070119
- [Sci Rep 11:4085 (2021)](https://www.nature.com/articles/s41598-021-83783-z) — pelvic flexure separates hindgut communities
- Julliand V, Grimm P (2016) *HORSE SPECIES SYMPOSIUM: The microbiome of the horse hindgut.* J Anim Sci — field history; culture-only through the 2000s, first 16S in 2001
- [Rutgers NJAES E375](https://njaes.rutgers.edu/e375/) — hindgut ≈62% of GI volume
- Strompfová V, Štempelová L (2024) *Composition and diversity of 16S rRNA based skin bacterial microbiome in healthy horses.* Vet Res Commun. [PMC11315781](https://pmc.ncbi.nlm.nih.gov/articles/PMC11315781/)
- [*Microorganisms* 13(3):623 (2025)](https://www.mdpi.com/2076-2607/13/3/623) — culturable equine skin microbiome
- [PMC12676801](https://pmc.ncbi.nlm.nih.gov/articles/PMC12676801/) — 2,362-sample equine faecal microbiome resource
- Edwards JE et al. (2020) *Domesticated equine species and their derived hybrids differ in their fecal microbiota.* Animal Microbiome 2:8. doi:[10.1186/s42523-020-00027-7](https://link.springer.com/article/10.1186/s42523-020-00027-7)
- [PMC7276150](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7276150/) — Tibetan wild ass vs domestic donkey
- [PMC7807438](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7807438/) — semi-feral vs conventionally managed foals

**Host-restricted taxa**
- Kuhnert P et al. (2004) J Clin Microbiol 42:5542–5548, PMID [15583279](https://pubmed.ncbi.nlm.nih.gov/15583279/); [*Vet Microbiol* clinical-significance screen](https://www.sciencedirect.com/science/article/abs/pii/S0378113512005147); [JVIM case report, doi:10.1111/jvim.12349](https://doi.org/10.1111/jvim.12349)
- [PMC3250509](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3250509/), [PMC11698419](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11698419/), [PMC5870977](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5870977/) — *Taylorella equigenitalis* / CEM
- [PMC11067117](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11067117/) — *Streptococcus equi* / strangles
- Sangal V, Goodfellow M, Jones AL, Sutcliffe IC, IJSEM. doi:[10.1099/ijsem.0.005551](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.005551); [Merck Vet Manual](https://www.merckvetmanual.com/respiratory-system/respiratory-diseases-of-horses/rhodococcus-equi-pneumonia-in-foals); [PMC12278488](https://pmc.ncbi.nlm.nih.gov/articles/PMC12278488/) — *Prescottella / Rhodococcus equi*

**Host taxonomy and history**
- [IUCN SSC Equid Specialist Group, *Equids: zebras, asses and horses — status survey and conservation action plan*](https://portals.iucn.org/library/node/8130) — seven extant *Equus* species
- Librado P et al. (2021) *Nature* 598:634–640. doi:[10.1038/s41586-021-04018-9](https://www.nature.com/articles/s41586-021-04018-9) — domestication origin (open access, PMC8550961)

**Explicitly flagged as inference, not sourced:** the recommendation to define on Reading A; the recommendation to request `mammal-associated environment` as a shared intermediate; the reading of the `#Host` vs `#Host body-site` split as encoding "whole organism" (this follows from the vocabulary's structure as documented, but no source states the inference in those words); the compartment attributions for *Dermatophilus congolensis* and *Pasteurella caballi*; and the §5.2 transient-soil-taxon interpretation.

---

## 5. Synonyms, and what not to conflate

### 5.1 Names in real use for this concept

- horse, domestic horse, *Equus caballus*, *Equus ferus caballus* (NCBI synonym), *Equus przewalskii f. caballus* (NCBI synonym)
- equid, equine (adjectival, and standard in the veterinary literature: "equine hindgut", "equine microbiome")
- pony, foal, mare, stallion, gelding — age/sex/size classes of the same host, not distinct habitats. Note that much of the skin and comparative-microbiome literature uses ponies (Shetlands) as the model.
- BacDive tag forms: `#Equidae (Horse)`, `Equidae-Horse`, `equidae-horse`
- MSW/IUCN family name: Equidae; order Perissodactyla

### 5.2 Commonly but wrongly treated as the same thing

1. **The taxon `Equidae` / `Equus caballus`.** The single most likely error, and the one #99 and #114 were about. The family is a class of organisms; the host is a place. `relation: xref`, never identity, never `parent_habitats`.
2. **Horse manure (`ENVO:00003859`), horse dung, stable bedding, mushroom compost (`ENVO:03033`, which is composted partly *from* horse manure).** These are host-derived *materials* that become environmental substrates. A strain from a manure heap is not a strain from a horse.
3. **The horse's premises** — stable, stall, paddock, pasture, feedlot, racing yard. `ENVO:03501287 livestock house` and friends. Different genus entirely.
4. **Horse body sites and body products.** `gut`, `skin`, `lung`, `blood`, `milk` ground to UBERON and are separate records under the corpus's part/whole rule. BacDive keeps them in separate top-level branches, so the split is upstream, not invented here.
5. **Donkey, mule, hinny, zebra, wild ass.** Same family; measurably different communities (§1.3). Conflating them is exactly the Reading A / Reading B error.
6. **Ruminant livestock** — cattle, sheep, goats. Sibling BacDive tags, and physiologically the *opposite* fermentation architecture (§3.2). "Livestock" or "farm animal" as a grouping conflates a foregut and a hindgut fermenter and should not be used as this record's parent.
7. **Transient environmental taxa.** Four soil-dwelling myxobacteria — *Corallococcus coralloides*, *Myxococcus virescens*, *M. fulvus*, *M. stipitatus* — total 26 strains on this record, ranks 3, 8, 11 and 25. Myxobacteria are canonical soil and dung organisms; their presence almost certainly reflects strains isolated from horse dung or a horse's soil-contaminated coat rather than from horse tissue. This is a **caution about how to read the `assertion_count` of 269**, not a reason to change the definition; it is my interpretation, and I did not verify the individual strain records. *Neomoorella thermoacetica* (rank 21) and *Sutcliffiella cohnii* (rank 15) are similarly environmental.

---

## 6. Should this be a term at all?

**Yes.** The disposition on the record (`CONFIRM_UNGROUNDED`, with the taxon as an xref and the concept kept as a term-request candidate) is correct, and the evidence supports it on three independent grounds:

1. **ENVO already models the pattern.** `ENVO:01001002 animal-associated environment` — "An environmental system determined by an animal" — asserts in ENVO's own voice that a host organism constitutes an environment. `ENVO:01001179 cnidarian-associated environment` shows ENVO is willing to make a clade-specific child of it. Nothing about "horse-associated environment" is a category error.
2. **The habitat is physically and chemically distinctive, not just administratively labelled.** Monogastric hindgut fermentation, cecal pH 6–7, 30–40% of energy from SCFAs, a compositional divide at the ileocecal junction and again at the pelvic flexure, a skin community of 18 phyla / 119 families, and a set of taxa (*Taylorella equigenitalis*, *Nicoletella semolina*, *Streptococcus equi*) that are essentially unknown outside equids.
3. **It is not any of the things that should be `NOT_APPLICABLE`.** It is not a disease, a quality, a process or a procedure. The previous `NOT_APPLICABLE` said "the concept is not a habitat", which is stronger than the evidence and, on the citations above, false.

Two caveats the curator should carry forward:

- **Volume is modest and partly environmental.** 269 strains across 124 taxa, with ~26 strains plausibly soil-transient (§5.2). This is a real habitat with a moderate attestation base, not a high-confidence heavyweight.
- **The record's `habitat_category` is `OTHER`.** Given the definition above and the corpus's treatment of the sibling `Mammals`, `Fish`, `Birds` and `Sponge` records, `HOST_ASSOCIATED` looks like the right category. That is a seeder-owned field and therefore a separate change from the definition — flagging it, not assuming it.

## Citations

1. https://academic.oup.com/nar/article/47/D1/D631/5106998
2. https://bacdive.dsmz.de/isolation-sources
3. https://pubmed.ncbi.nlm.nih.gov/15583279/
4. https://www.merckvetmanual.com/respiratory-system/respiratory-diseases-of-horses/rhodococcus-equi-pneumonia-in-foals
5. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3250509/
6. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11067117/
7. https://portals.iucn.org/library/node/8130
8. https://link.springer.com/article/10.1186/s42523-020-00027-7
9. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7276150/
10. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC12504203/
12. https://njaes.rutgers.edu/e375/
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC5112786/
14. https://www.nature.com/articles/s41598-021-83783-z
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC11315781/
16. https://www.mdpi.com/2076-2607/13/3/623
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC12676801/
18. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11698419/
19. https://www.sciencedirect.com/science/article/abs/pii/S0378113512005147
20. https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.005551
21. https://www.nature.com/articles/s41586-021-04018-9
22. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7807438/
23. https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/9788
24. https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/9796
25. https://doi.org/10.1111/jvim.12349
26. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5870977/
27. https://pmc.ncbi.nlm.nih.gov/articles/PMC12278488/