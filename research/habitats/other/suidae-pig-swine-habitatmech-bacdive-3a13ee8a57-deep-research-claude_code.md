---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T16:50:10.206290'
end_time: '2026-08-17T16:57:40.733204'
duration_seconds: 450.53
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Suidae-Pig,Swine
  habitat_identifier: habitatmech:BACDIVE.3a13ee8a57
  habitat_category: OTHER
  grounding_status: UNGROUNDED
  attestations: 'BACDIVE: Suidae-Pig,Swine'
  assertions: '521'
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
    \ not a habitat, which is a stronger and false claim. (source concept habitatmech:BACDIVE.3a13ee8a57)"
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
  web_search_requests: 15
  num_turns: 26
  total_cost_usd: 3.0006579999999996
  session_id: 4c228316-558c-46ac-a567-08e026e1943a
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 45
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Suidae-Pig,Swine
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.3a13ee8a57
- **Category:** OTHER
- **Grounding status:** UNGROUNDED
- **Source attestations:** BACDIVE: Suidae-Pig,Swine
- **Upstream assertion volume:** 521
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it — the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE while its own child Porifera > Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM — a phylum is a class of organisms, not a place — so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. (source concept habitatmech:BACDIVE.3a13ee8a57)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Suidae-Pig,Swine** as a microbial habitat, with citations.

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

> **A mammal-associated environment which is determined by a suid (family Suidae), in practice almost always the domestic pig *Sus scrofa domesticus*.**

If `mammal-associated environment` is not minted, substitute the existing ENVO parent: *An animal-associated environment which is determined by a suid (family Suidae), in practice almost always the domestic pig* Sus scrofa domesticus.

Recommended term label: **pig-associated environment** (exact synonyms: `Suidae-Pig,Swine`, `swine-associated environment`, `porcine-associated environment`).

---

## 1. What the concept denotes

`Suidae-Pig,Swine` is **not** a free-text isolation source; it is a **level-3 classification tag** in BacDive's Microbial Isolation Source Ontology (MISO), sitting at the path:

> `#Host` → `#Mammals` → `#Suidae (Pig,Swine)`

I verified this path directly against BacDive's isolation-source browser ([bacdive.dsmz.de/isolation-sources](https://bacdive.dsmz.de/isolation-sources), retrieved 2026-08-17). MISO is described as "hierarchically ordered into three levels of tags (category 1–3)" with eight top-level classes (`#Environmental`, `#Engineered`, `#Host`, `#Host body-site`, `#Host body-product`, `#Medical`, `#Condition`, `#Climate`), and each isolation source is annotated with up to four such triplets — Reimer et al., *BacDive in 2019*, **Nucleic Acids Research** 47:D631–D636, [doi:10.1093/nar/gky879](https://doi.org/10.1093/nar/gky879); Reimer et al., *BacDive in 2022*, **NAR** 50:D741–D746, [doi:10.1093/nar/gkab961](https://doi.org/10.1093/nar/gkab961).

**What the sample is, therefore:** the tag records *the host organism a strain was recovered from*, not a body site and not a body product — those are separate top-level MISO classes (`#Host body-site`, `#Host body-product`) carried on the *same* strain record in an adjacent triplet. So this concept denotes **the living pig considered as the environmental system that hosts the microbe**: the sum of its colonisable surfaces, lumina and tissues, prior to any statement about which one was sampled.

**Boundary — inside the concept:**
- Any microbial community sampled from a live or freshly-slaughtered suid, at any body site, where the record's *host* is a pig.
- Both commensal carriage (tonsil, nasal cavity, gut) and clinical isolation from a diseased pig — MISO's `#Infection` is a separate top-level class, so disease state does not remove the host tag.
- Domestic pigs, wild boar and other suids alike, as far as the tag's label goes.

**Boundary — neighbouring concepts, outside:**
- The **anatomical site** (gut, tonsil, nasal cavity, skin, lung, blood). Per HabitatMech's standing rule these ground to UBERON and are separate records; they are `#Host body-site` in MISO, a different tag axis.
- **Pig manure / feces once voided** — `ENVO:00003860 'pig manure'` ("Manure which is primarily composed of pig feces."), an *environmental material* derived from but no longer part of the host.
- **The pig house** — `ENVO:00003042 'piggery'` ("An animal house which is used to house pigs."), a built environment; the corpus already has `habitatmech:GOLD.019799304e swine_confinement_building` for this.
- **Pig-derived food** — `FOODON:00001132 'swine food product'`, `FOODON:02021649 'pig material'`, `FOODON:00001038 'pork meat food product'`.
- **Porcine cell lines** — `BTO:0001865 'PK-15 cell'`, `BTO:0006402 'IPEC-J2 cell'`, `BTO:0004921 'swine testicular cell line'`. These are laboratory-propagated cells, not the host animal.

### The one real ambiguity: Suidae vs *Sus scrofa*

The label is internally inconsistent and this needs a curator decision, not a silent pick.

- **Reading A (family):** *Suidae* = NCBI Taxonomy **taxid 9821**, the family, which includes warthogs (*Phacochoerus*), babirusas (*Babyrousa*), bushpigs (*Potamochoerus*) and *Sus*.
- **Reading B (the gloss):** "Pig, Swine" in ordinary usage means *Sus scrofa* (taxid 9823, NCBI GenBank common name "pig"; lineage …Artiodactyla; Suina; **Suidae**; *Sus*; *Sus scrofa*), overwhelmingly the domestic subspecies *S. s. domesticus*. NCBI Taxonomy Browser, [taxid 9821](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=9821) and [taxid 9823](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=9823); Schoch et al. 2020, **Database** baaa062, [doi:10.1093/database/baaa062](https://doi.org/10.1093/database/baaa062).

The upstream evidence favours **Reading B in practice, Reading A in name**. `data/raw/isolation_source_groundings.tsv:304` maps this concept to `NCBITaxon:9823 Sus scrofa` with `skos:closeMatch`, `medium` confidence, `semapv:LexicalMatching` via `ols4_search_synonym` — a species-level target for a family-level label, which is exactly the kind of lexical near-miss `closeMatch` is for. The characteristic taxa on the record settle it: `Moraxella porci`, `Actinobaculum suis`, `Streptococcus suis`, `Campylobacter hyointestinalis`, `Staphylococcus hyicus`, `Schaalia hyovaginalis`, `Actinobacillus suis`, `[Pasteurella] aerogenes` — every one of these is a *domestic-pig* organism from veterinary or abattoir work, not from wild suids.

**Recommendation:** define the term at family scope (so the label is honest) and add a scope note that the attestations are essentially all domestic pig. Do not narrow the definition to *S. scrofa* — that would make the term's own label wrong.

## 2. Genus — the broader kind

**Nothing in ENVO expresses this.** I checked the current ENVO via OLS4 on 2026-08-17: a search for `pig` across ENVO returns exactly **two** classes — `ENVO:00003042 piggery` and `ENVO:00003860 pig manure` — and a search for `swine` returns **no ENVO class at all** (only FoodOn's `swine food product` and `swine material`). There is no `pig-associated environment`, `swine-associated environment`, or `Suidae-associated environment`.

**The genus to use:**

| Candidate | CURIE | Verdict |
|---|---|---|
| `mammal-associated environment` | *(requested)* `habitatmech:GOLD.e889967f4f` | **Preferred genus.** Already a pending term request in `curation/term_requests.tsv`, defined "An environmental system determined by a mammal.", parented to `ENVO:01001002`. A pig is a mammal, so this is the smallest well-established kind. It does not exist yet, so the request row must carry the ENVO fallback. |
| `animal-associated environment` | `ENVO:01001002` | **Correct but one level too coarse.** Definition verified via OLS4: "An environmental system determined by an animal." (synonyms: *Metazoan-associated environment*, *animal environment*). Use as the parent in the term request, exactly as every sibling in this batch does; do **not** ground here, because doing so merges every host clade — pig, cow, sheep, dog, horse, mouse, human — onto one record and destroys the distinction BacDive's tag axis is making. |
| `environmental system determined by an organism` | `ENVO:01001000` | Grandparent; carries the exact synonym *host-associated environment*. Too coarse. |

**Near-misses worth recording as such:**

- **`ENVO:00003042 piggery`** — a *building*. Grounding here would assert that the microbe was sampled from the animal house rather than the animal, and would exclude every wild boar and every abattoir isolate. It also asserts a human construction the tag never claims. **Xref at most.**
- **`ENVO:00003860 pig manure`** — an *environmental material* downstream of the host. Most of BacDive's pig strains are from tonsil, nasal cavity, lung, fetus and urogenital tract, not manure; and manure is post-excretion, which changes oxygen tension, temperature and community composition. **Narrower and material-typed; not a match.**
- **`NCBITaxon:9823 Sus scrofa` / `NCBITaxon:9821 Suidae`** — a *class of organisms*, not a place. Per this repo's `#99`/`#114` disposition these belong in `relation: xref`, never as identity or parent.
- **`ENVO:01000626 drylot` / `ENVO:01000627 feedlot` / `ENVO:00000266 pasture`** — production settings, not the host.
- **`FOODON:02021649 pig material`** — a food/material role, not a habitat.

## 3. Differentia — what distinguishes a pig from its sibling host clades

These are the observable, sourced properties that separate `pig-associated environment` from `bovine-`, `equine-`, `murid-` and `human-associated environment` under the same genus.

**(a) Gut physiology: a monogastric, colon-fermenting omnivore.** This is the single most load-bearing differentium, because it determines the community. Pigs and humans are omnivores and **colon fermenters**, whereas rodents ferment in the caecum and ruminants (cattle, sheep, goats — the two largest sibling categories in BacDive after human) ferment pre-gastrically in the rumen. Pigs are "a human-sized omnivorous animal with comparable nutritional requirements" with gut anatomy giving analogous transit time and digestion/absorption. — Heinritz, Mosenthin & Weiss, *Use of pigs as a potential model for research into dietary modulation of the human gut microbiota*, **Nutrition Research Reviews** 26:191–209 (2013), [doi:10.1017/S0954422413000152](https://doi.org/10.1017/S0954422413000152), PMID [24134811](https://pubmed.ncbi.nlm.nih.gov/24134811/).

**(b) A *Prevotella*-dominated core community, independently characterised at reference-catalogue scale.** The pig gut has its own gene catalogue and core taxon set, which is what makes the habitat separable rather than merely a label:
- Xiao et al., *A reference gene catalogue of the pig gut microbiome*, **Nature Microbiology** 1:16161 (2016), [doi:10.1038/nmicrobiol.2016.161](https://doi.org/10.1038/nmicrobiol.2016.161) — 4,430 non-redundant genes and 36 metagenomic species shared by 100% of 287 pig samples; *Prevotella* the most-annotated genus, then *Ruminococcus*, *Eubacterium*, *Lactobacillus*, *Helicobacter*.
- Chen et al., *Expanded catalog of microbial genes and metagenome-assembled genomes from the pig gut microbiome* (PIGC), **Nature Communications** 12:1106 (2021), [doi:10.1038/s41467-021-21295-0](https://doi.org/10.1038/s41467-021-21295-0) — core defined at >90% sample detection: 19 phyla, 234 genera, 254 species; 97 species detected in all 500 samples accounting for >92% of species abundance.
- *Characterizing core microbiota and regulatory functions of the pig gut microbiome*, **ISME Journal** 18:wrad037 (2024), [doi:10.1093/ismejo/wrad037](https://doi.org/10.1093/ismejo/wrad037), PMID [38366194](https://pubmed.ncbi.nlm.nih.gov/38366194/) — 17,020,160 genes, 4,910 MAGs across seven breeds; three core-predominant species (*Phascolarctobacterium succinatutens*, *Prevotella copri*, *Oscillibacter valericigenes*).
- UPGG, **npj Biofilms and Microbiomes** (2025), [doi:10.1038/s41522-025-00828-1](https://doi.org/10.1038/s41522-025-00828-1) — >78 million non-redundant proteins from 5,784 metagenomes.

**(c) A distinctive set of host-restricted or host-named taxa.** The record's own top-25 characteristic taxa are dominated by organisms whose species epithets *are* the host — the strongest available evidence that this is a real, separable habitat and not a bookkeeping label:
- **`[Pasteurella] aerogenes`** (41 strains, rank 1) — first isolated from porcine intestine, resident in the pig digestive tract, associated with swine gastroenteritis and abortion; its type strain (ATCC 27884) comes from aborted swine fetuses. Fodor, Hajtós & Glávits, **Acta Vet Hung** (1991), PMID [1750360](https://pubmed.ncbi.nlm.nih.gov/1750360/); Kuhnert et al., *Emended description of porcine [Pasteurella] aerogenes, [Pasteurella] mairii and [Actinobacillus] rossii*, **IJSEM** (2005), [doi:10.1099/ijs.0.63119-0](https://doi.org/10.1099/ijs.0.63119-0).
- **`Moraxella porci`** (8 strains) — described from nine strains isolated from pigs, type strain from the brain of a pig with meningitis. Vela et al., **IJSEM** 60:2446–2450 (2010), [doi:10.1099/ijs.0.016626-0](https://doi.org/10.1099/ijs.0.016626-0).
- **`Streptococcus suis`** (6 strains) — early coloniser of swine, a "natural niche" in the tonsil, normal inhabitant of the upper respiratory tract of clinically healthy pigs; 98% of surveyed Ontario herds PCR-positive. Prevalence survey: **Can J Vet Res**, PMC[2327245](https://pmc.ncbi.nlm.nih.gov/articles/PMC2327245/).
- **`Actinobacillus pleuropneumoniae`** (7 strains) — 78% of the same Ontario herds positive by *apxIV* PCR; agent of porcine pleuropneumonia.
- Plus `Campylobacter hyointestinalis`, `Actinobaculum suis`, `Staphylococcus hyicus`, `Schaalia hyovaginalis`, `Streptococcus hyovaginalis`, `Actinobacillus suis`, `Erysipelothrix rhusiopathiae`.

**(d) Pigs are the principal reservoir for specific zoonotic lineages** — a property of the host habitat, not of any one body site:
- ***Campylobacter coli***: "poultry has been recognized as the primary reservoir of *C. jejuni*, while pigs are mostly implicated as reservoirs of *C. coli*"; reported herd prevalence 50–100%, faecal shedding 10²–10⁷ CFU/g. Payot et al. / Thakur & Gebreyes, **J Clin Microbiol** 43:5705–5714 (2005), [doi:10.1128/JCM.43.11.5705-5714.2005](https://doi.org/10.1128/JCM.43.11.5705-5714.2005), PMC[1287812](https://pmc.ncbi.nlm.nih.gov/articles/PMC1287812/). *C. coli* is BacDive's rank-2 taxon here (18 strains).
- **LA-MRSA CC398**: the European pig industry is "the main reservoir" for this lineage, found on >70% of European pig farms and ~95% of Danish pig farms; nasal carriage exceeds 80% among German pig farmers. Ingham et al., **Appl Environ Microbiol** 87 (2021), [doi:10.1128/AEM.01225-21](https://doi.org/10.1128/AEM.01225-21), PMID [34191530](https://pubmed.ncbi.nlm.nih.gov/34191530/).

**(e) Scale and accessibility.** Pigs are among the most numerous large mammals on Earth (order 10⁸–10⁹ head globally; FAO Livestock Systems, [fao.org/livestock-systems/global-distributions/pigs/en/](https://www.fao.org/livestock-systems/global-distributions/pigs/en/); Our World in Data, [Number of pigs](https://ourworldindata.org/grapher/pig-livestock-count-heads), from FAOSTAT "Production: Crops and livestock products"). *I did not read the exact FAOSTAT 2023 stock figure directly — secondary sources put it around 780 million head, and Eurostat gives 133 million in the EU at end-2023 and USDA 72.9 million in the US on 1 March 2023. Treat the global number as approximate unless the curator queries FAOSTAT QCL (Element = Stocks, Item = Swine/pigs, Area = World).* This explains the 521 strains without needing to be part of the definition.

**Explicitly my inference, not a source's:** that (a)–(d) taken together justify a *separate* class rather than parenting all suid isolates directly to `animal-associated environment`. No source argues about ontology design. What the sources establish is that the pig gut has its own reference catalogue and core taxon set, and that a set of bacterial species is named for and largely restricted to this host — which is the factual basis for the design choice.

## 4. Should it be a term at all?

**Yes.** This is a habitat, and the record's existing `CONFIRM_UNGROUNDED` reasoning is right. The concept is a *host organism acting as an environmental system* — precisely what `ENVO:01001000` calls out with its exact synonym *host-associated environment*, and what ENVO already models at `plant-associated environment`, `animal-associated environment` and `fungi-associated environment`.

It is **not** any of the dispositions that would argue against a term: not a process, not a quality (contrast the repo's `PATO:0001429` case), not a disease state (MISO keeps `#Infection` on a separate axis), and not a sampling artefact (521 strains across 300 candidate taxa, drawn from decades of veterinary microbiology).

The one thing it must **not** become is a grounding to the taxon. `NCBITaxon:9821 Suidae` and `NCBITaxon:9823 Sus scrofa` name *classes of organisms*, not places. The standards world agrees these are different fields: MIxS keeps `host_taxid` ("The NCBI taxon id of the host, e.g. 9606", required in the host-associated extension) separate from `env_medium`, and ENVO's own MIxS guidance says to fill the host taxonomy fields *and* use ENVO/UBERON terms for the environment — two slots, not one. GSC MIxS host-associated extension, [genomicsstandardsconsortium.github.io/mixs/0016002/](https://genomicsstandardsconsortium.github.io/mixs/0016002/); ENVO wiki, [Using ENVO with MIxS](https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS); Yilmaz et al., **Nature Biotechnology** 29:415–420 (2011), [doi:10.1038/nbt.1823](https://doi.org/10.1038/nbt.1823).

The MIxS host-associated scope note also supports the boundary drawn in §1: "nucleic acids from soil sampled from a cow's hoof fit the soil extension, whereas soil embedded in a wound on a cow's leg belongs in the host-associated extension" — i.e. the host-associated framing turns on whether the host is causally determining the sampled community, which is exactly what distinguishes this concept from `pig manure` and `piggery`.

## 5. Synonyms, and what not to conflate

**Names in real use for this concept:**
- pig-associated environment / swine-associated environment / porcine-associated environment
- pig host, swine host, porcine host
- `Suidae-Pig,Swine` (BacDive MISO level-3 tag, verbatim)
- `Host-associated > Mammals > Pig` (the equivalent shape in the GOLD ecosystem path vocabulary)
- pig microbiome / swine microbiome / porcine microbiota (community-level names; commonly stand in for the habitat in the literature)
- hog-associated (US usage; "hogs and pigs" is the USDA inventory category)

**Commonly but wrongly treated as the same thing:**

| Wrongly conflated | Why it differs |
|---|---|
| `ENVO:00003860 pig manure` | Excreted material, post-host; different oxygen tension, temperature, community. Downstream of, not identical to, the host. |
| `ENVO:00003884 farmyard manure` | Mixed-species and bedding-inclusive. |
| `ENVO:00003042 piggery` | The animal house. A built environment; asserts human construction the tag never claims, and excludes wild suids. |
| `habitatmech:GOLD.019799304e swine_confinement_building` | Same problem, already a separate corpus record. |
| `habitatmech:GOLD.288559828e swine_waste_with_corn` | An engineered waste stream. |
| `FOODON:00001132 swine food product`, `FOODON:02021649 pig material`, `FOODON:00001038 pork meat food product` | Post-slaughter food matrices; the community is that of a processed product, not a live host. |
| `BTO:0001865 PK-15 cell`, `BTO:0006402 IPEC-J2 cell`, `BTO:0004921 swine testicular cell line`, `BTO:0004007 porcine aortic endothelial cell` | Cultured cell lines of porcine origin. Not the animal. |
| UBERON anatomical parts of a pig (gut, tonsil, skin, lung, blood) | These are the `#Host body-site` axis and ground to UBERON as their own records, per this repo's parts-vs-whole rule. |
| **Guinea pig** (*Cavia porcellus*, family Caviidae, rodent) | Not a suid. A pure lexical trap: any string match on "pig" catches it. Also "sea pig" (*Scotoplanes*, a holothurian) and "pygmy hog" is a suid but "hedgehog" is not. |
| **Peccaries** (*Tayassu*, *Pecari*; family **Tayassuidae**) | Pig-like New World artiodactyls, sister family to Suidae — outside the concept under either reading. |
| "Pig" as a slaughterhouse/carcass sample | Italian abattoir data show *C. coli* prevalence higher on carcasses (50.4%) than in faeces (32.9%) because of cross-contamination during slaughter — so carcass swabs are not clean evidence of the host habitat. PMC[7074678](https://pmc.ncbi.nlm.nih.gov/articles/PMC7074678/). |

## 6. Concrete recommendations for the curator

**Term request row** (matching the batch's established shape in `curation/term_requests.tsv`):

```
habitatmech:BACDIVE.3a13ee8a57	pig-associated environment	ENVO:01001002	animal-associated environment	An environmental system determined by a suid.	Suidae-Pig,Swine|swine-associated environment|porcine-associated environment
```

Parent it to `ENVO:01001002` for the same reason `bacterium-associated environment` was: its natural parent `mammal-associated environment` (`habitatmech:GOLD.e889967f4f`) is requested in the same batch and does not exist yet — note in the request that editors should re-parent if both are minted.

**Xref:** `NCBITaxon:9823 Sus scrofa` with `relation: xref`, per `#99`/`#114`. Consider adding `NCBITaxon:9821 Suidae` as a second xref, since it is the taxon the label actually names and the upstream `skos:closeMatch` is species-level only through lexical matching.

**Two things to check in the record itself, which I could not resolve from the data:**
1. `data/habitats/other/suidae_pig_swine.yaml` has **no `parent_habitats` at all**, while the sibling host-clade records (Fish, Mammals, Birds) carry `ENVO:01001002`. Attaching it here would be consistent.
2. The source attestation note reads `Upstream mapping targets a non-habitat ontology (); kept as an xref.` — the ontology name is **empty**, and no xref appears on the record even though `isolation_source_groundings.tsv:304` supplies `NCBITaxon:9823`. Worth a look at whether the seeder drops NCBITaxon xrefs.
3. `habitat_category` is `OTHER`, not `HOST_ASSOCIATED`, unlike every sibling host-clade record. If the category is derived from the grounding target, the missing xref may be the cause.

---

### Sources

- [BacDive isolation sources browser](https://bacdive.dsmz.de/isolation-sources) — MISO tag hierarchy, path verified 2026-08-17
- Reimer et al., *BacDive in 2019*, **NAR** 47:D631 — [doi:10.1093/nar/gky879](https://doi.org/10.1093/nar/gky879) · [PMC6323973](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323973/)
- Reimer et al., *BacDive in 2022*, **NAR** 50:D741 — [doi:10.1093/nar/gkab961](https://doi.org/10.1093/nar/gkab961) · [PMC8728306](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8728306/)
- ENVO `ENVO:01001002` — [OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002); ENVO repo — [github.com/EnvironmentOntology/envo](https://github.com/EnvironmentOntology/envo); [Using ENVO with MIxS](https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS); host-associated term discussion — [envo#1029](https://github.com/EnvironmentOntology/envo/issues/1029)
- GSC MIxS host-associated extension — [genomicsstandardsconsortium.github.io/mixs/0016002/](https://genomicsstandardsconsortium.github.io/mixs/0016002/); `host_taxid` — [TDWG terms wiki](https://terms.tdwg.org/wiki/mixs:host_taxid); Yilmaz et al. **Nat Biotechnol** 29:415 — [doi:10.1038/nbt.1823](https://doi.org/10.1038/nbt.1823)
- NCBI Taxonomy — [Suidae 9821](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=9821), [*Sus scrofa* 9823](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=9823), [NCBI Datasets 9823](https://www.ncbi.nlm.nih.gov/datasets/taxonomy/9823/); Schoch et al. **Database** 2020:baaa062 — [doi:10.1093/database/baaa062](https://doi.org/10.1093/database/baaa062)
- Xiao et al., **Nat Microbiol** 1:16161 (2016) — [doi:10.1038/nmicrobiol.2016.161](https://doi.org/10.1038/nmicrobiol.2016.161)
- Chen et al., **Nat Commun** 12:1106 (2021) — [doi:10.1038/s41467-021-21295-0](https://www.nature.com/articles/s41467-021-21295-0)
- **ISME J** 18:wrad037 (2024) — [doi:10.1093/ismejo/wrad037](https://academic.oup.com/ismej/article/18/1/wrad037/7517691) · [PMC10873858](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10873858/)
- UPGG, **npj Biofilms Microbiomes** (2025) — [doi:10.1038/s41522-025-00828-1](https://www.nature.com/articles/s41522-025-00828-1)
- Heinritz et al., **Nutr Res Rev** 26:191 (2013) — [Cambridge Core](https://www.cambridge.org/core/journals/nutrition-research-reviews/article/use-of-pigs-as-a-potential-model-for-research-into-dietary-modulation-of-the-human-gut-microbiota/9A2097DC0550A9B551AFFB3CF2AB07DC) · PMID [24134811](https://pubmed.ncbi.nlm.nih.gov/24134811/)
- Thakur & Gebreyes, **J Clin Microbiol** 43:5705 (2005) — [PMC1287812](https://pmc.ncbi.nlm.nih.gov/articles/PMC1287812/); Italian abattoir survey — [PMC7074678](https://pmc.ncbi.nlm.nih.gov/articles/PMC7074678/)
- Ingham et al., **Appl Environ Microbiol** 87 (2021) — [doi:10.1128/aem.01225-21](https://journals.asm.org/doi/10.1128/aem.01225-21) · PMID [34191530](https://pubmed.ncbi.nlm.nih.gov/34191530/)
- Ontario swine respiratory pathogen survey — [PMC2327245](https://pmc.ncbi.nlm.nih.gov/articles/PMC2327245/)
- Vela et al., *Moraxella porci* sp. nov., **IJSEM** (2010) — [doi:10.1099/ijs.0.016626-0](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.016626-0); piglet nasal *Moraxella* — [BMC Vet Res 16:22](https://bmcvetres.biomedcentral.com/articles/10.1186/s12917-020-2250-9)
- Kuhnert et al., emended description of porcine *[Pasteurella] aerogenes* — [doi:10.1099/ijs.0.63119-0](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.63119-0); Fodor et al. **Acta Vet Hung** (1991) — PMID [1750360](https://pubmed.ncbi.nlm.nih.gov/1750360/); occupational human cases — PMID [9060058](https://pubmed.ncbi.nlm.nih.gov/9060058/)
- FAO Livestock Systems — [Pigs](https://www.fao.org/livestock-systems/global-distributions/pigs/en/); Our World in Data — [Number of pigs](https://ourworldindata.org/grapher/pig-livestock-count-heads); FAO **Statistical Yearbook 2023** — [openknowledge.fao.org](https://openknowledge.fao.org/server/api/core/bitstreams/28cfd24e-81a9-4ebc-b2b5-4095fe5b1dab/content/cc8166en.html)

## Citations

1. https://bacdive.dsmz.de/isolation-sources
2. https://doi.org/10.1093/nar/gky879
3. https://doi.org/10.1093/nar/gkab961
4. https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=9821
5. https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=9823
6. https://doi.org/10.1093/database/baaa062
7. https://doi.org/10.1017/S0954422413000152
8. https://pubmed.ncbi.nlm.nih.gov/24134811/
9. https://doi.org/10.1038/nmicrobiol.2016.161
10. https://doi.org/10.1038/s41467-021-21295-0
11. https://doi.org/10.1093/ismejo/wrad037
12. https://pubmed.ncbi.nlm.nih.gov/38366194/
13. https://doi.org/10.1038/s41522-025-00828-1
14. https://pubmed.ncbi.nlm.nih.gov/1750360/
15. https://doi.org/10.1099/ijs.0.63119-0
16. https://doi.org/10.1099/ijs.0.016626-0
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC2327245/
18. https://doi.org/10.1128/JCM.43.11.5705-5714.2005
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC1287812/
20. https://doi.org/10.1128/AEM.01225-21
21. https://pubmed.ncbi.nlm.nih.gov/34191530/
22. https://www.fao.org/livestock-systems/global-distributions/pigs/en/
23. https://ourworldindata.org/grapher/pig-livestock-count-heads
24. https://genomicsstandardsconsortium.github.io/mixs/0016002/
25. https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
26. https://doi.org/10.1038/nbt.1823
27. https://pmc.ncbi.nlm.nih.gov/articles/PMC7074678/
28. https://pmc.ncbi.nlm.nih.gov/articles/PMC6323973/
29. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8728306/
30. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002
31. https://github.com/EnvironmentOntology/envo
32. https://github.com/EnvironmentOntology/envo/issues/1029
33. https://terms.tdwg.org/wiki/mixs:host_taxid
34. https://www.ncbi.nlm.nih.gov/datasets/taxonomy/9823/
35. https://www.nature.com/articles/s41467-021-21295-0
36. https://academic.oup.com/ismej/article/18/1/wrad037/7517691
37. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10873858/
38. https://www.nature.com/articles/s41522-025-00828-1
39. https://www.cambridge.org/core/journals/nutrition-research-reviews/article/use-of-pigs-as-a-potential-model-for-research-into-dietary-modulation-of-the-human-gut-microbiota/9A2097DC0550A9B551AFFB3CF2AB07DC
40. https://journals.asm.org/doi/10.1128/aem.01225-21
41. https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.016626-0
42. https://bmcvetres.biomedcentral.com/articles/10.1186/s12917-020-2250-9
43. https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.63119-0
44. https://pubmed.ncbi.nlm.nih.gov/9060058/
45. https://openknowledge.fao.org/server/api/core/bitstreams/28cfd24e-81a9-4ebc-b2b5-4095fe5b1dab/content/cc8166en.html