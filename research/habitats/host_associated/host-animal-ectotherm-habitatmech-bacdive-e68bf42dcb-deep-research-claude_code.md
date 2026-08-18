---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T16:18:03.713819'
end_time: '2026-08-17T16:27:19.432854'
duration_seconds: 555.72
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: host_animal_ectotherm
  habitat_identifier: habitatmech:BACDIVE.e68bf42dcb
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'MADIN: host_animal_ectotherm'
  assertions: '999'
  parent_terms: (none)
  xrefs: (none)
  decision_note: "Reviewed and endorsed the seeder's own resolution. Category override\
    \ (#57): a minted identifier gives infer_category nothing to read \u2014 no ontology\
    \ term, no GOLD path \u2014 so every Madin habitat named in the BacDive vocabulary\
    \ fell to OTHER. A cold-blooded animal host is HOST_ASSOCIATED for the same reason\
    \ as the endotherm one; the thermal distinction is a property of the host, not\
    \ a different kind of habitat. (source concept habitatmech:BACDIVE.e68bf42dcb)"
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
  web_search_requests: 11
  num_turns: 35
  total_cost_usd: 3.736293000000001
  session_id: f05f17c1-6811-4f26-a1a0-0d0b171b4650
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 40
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** host_animal_ectotherm
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.e68bf42dcb
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** MADIN: host_animal_ectotherm
- **Upstream assertion volume:** 999
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Reviewed and endorsed the seeder's own resolution. Category override (#57): a minted identifier gives infer_category nothing to read — no ontology term, no GOLD path — so every Madin habitat named in the BacDive vocabulary fell to OTHER. A cold-blooded animal host is HOST_ASSOCIATED for the same reason as the endotherm one; the thermal distinction is a property of the host, not a different kind of habitat. (source concept habitatmech:BACDIVE.e68bf42dcb)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **host_animal_ectotherm** as a microbial habitat, with citations.

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

# Definition research: `host_animal_ectotherm` (`habitatmech:BACDIVE.e68bf42dcb`)

## Proposed definition

> An **animal-associated environment** which is determined by an ectothermic animal host, and whose temperature therefore tracks that of the host's surroundings rather than being held at a metabolically regulated set point.

Genus: `ENVO:01001002` *animal-associated environment*. Differentia: the host's thermal strategy, stated as an observable property of the environment (temperature conforms to ambient, no characteristic set point), not as a taxonomic claim about the host.

**Recommended disposition:** `GROUND_AS_PARENT` → `ENVO:01001002` *animal-associated environment*, keeping the minted identifier. Do **not** `GROUND` to `ENVO:01001002`: that term is already the identity of an existing record in this corpus (`data/habitats/other/animal_associated_environment.yaml`, carrying Madin's `host_animal` bucket at 144 taxa), and grounding here would pour 999 ectotherm taxa into it and destroy the very distinction the label exists to make.

**One caveat the curator must read before writing the sentence (§1.3, §6.2).** The label names a thermal property, but the 335 upstream strings behind it are overwhelmingly *invertebrates* — 125 arthropod/insect, 46 mollusc, 21 worm/nematode, 21 cnidarian, 19 sponge, 15 echinoderm, 5 tunicate, against 46 fish and only 11 reptile/amphibian. In practice this bucket is the **complement of the endotherm bucket** — "an animal host that is not a mammal or a bird" — not a set of hosts selected for their thermal biology. The definition above is still correct extensionally (all of those hosts are ectotherms), but the note should say the concept is a residual pooling.

---

## 1. What the concept denotes

### 1.1 Provenance of the label

`host_animal_ectotherm` is not a BacDive free-text string. It is a **level-3 label in the Madin et al. (2020) environment scheme**, a controlled vocabulary built to normalise free-text isolation sources across 26 trait databases. The paper states the structure and names this concept's own sibling in the example:

> "a one-term label is 'host', a two-term is 'host_animal', a three-term is 'host_animal_endotherm', and a four-term is 'host_animal_endotherm_intestinal'"
> — Madin JS et al. (5 Jun 2020) *A synthesis of bacterial and archaeal phenotypic trait data*, **Scientific Data** 7:170. [doi:10.1038/s41597-020-0497-4](https://doi.org/10.1038/s41597-020-0497-4) · PMID 32503990 · [PMC7275036](https://pmc.ncbi.nlm.nih.gov/articles/PMC7275036/)

The same paper explains why some labels stop at level 3: *"If no dominant term could be found at a given level (not resolved), the process was stopped at that level."* Unlike its endotherm sibling, which has ten level-4 children (`_oral`, `_intestinal`, `_blood`, `_rumen`, `_feces`, `_surface`, `_vagina`, `_nasopharyngeal`, `_intracellullar` [sic], `_intratissue`), **`host_animal_ectotherm` has no level-4 children at all** in [`environments.csv`](https://github.com/bacteria-archaea-traits/bacteria-archaea-traits/blob/master/data/conversion_tables/environments.csv). Everything from a termite hindgut to a sponge mesohyl to a fish kidney collapses into this one label.

### 1.2 What is actually in it — the 335 mapped strings

Counted directly from upstream's [`renaming_isolation_source.csv`](https://github.com/bacteria-archaea-traits/bacteria-archaea-traits/blob/master/data/conversion_tables/renaming_isolation_source.csv) (335 rows map to this label; classification by regex over host words is mine):

| Host group | Strings | Representative strings |
|---|---:|---|
| Insects & other arthropods | 125 | `termite hindgut`, `gut of a honeybee`, `hostassociated, nymphal deer tick, ixodes scapularis`, `host-associated, pea aphid, acyrthosiphon pisum`, `Obligate endosymbiont of armoured scale insects.`, `haemolymph of shrimp` |
| Molluscs | 46 | `other, oyster`, `intestinal tract of an abalone`, `host-associated, mollusca, respiratory system, gills, symbiotic`, `aquatic, accessory nidamental gland` |
| Fish | 46 | `host-associated, fish, digestive system, intestine`, `other, farmed atlantic salmon`, `kidney of pufferfish`, `aquatic, brown trout with furunculosis` |
| Worms & nematodes | 21 | `other, termite gut`… `nephridia of earthworm`, `entomopathogenic nematode`, `skin of the medical leech hirudo verbana` |
| Cnidarians | 21 | `other, mucus of coral`, `reef-building coral`, `other, sea anemone`, `octocoral` |
| Sponges | 19 | `host-associated, porifera, sponge`, `Sponge symbiont nonthermophilic crenarchaeota.` |
| Echinoderms | 15 | `gut of a sea urchin`, `intestine of a sea cucumber`, `coelomic fluid of a sand dollar` |
| Protists / amoebae | 12 | `host-associated, protozoa`, `other, amoebae cytoplasm`, `Obligate intracellular parasite of Acanthamoeba castellanii.` — **not animals; see §6.2** |
| Reptiles & amphibians | 11 | `bearded dragon`, `Isolated from the intestine of the reticulated python`, `host-associated, amphibia`, `other, frog` |
| Tunicates | 5 | `host-associated, tunicates, ascidians`, `other, sea squirt` |
| Unclassifiable / mismapped | 14 | `host-associated, plants, rhizosphere, soil`; `other, isolated from air`; `environmental, aquatic, marine, symbiotic, commensal` |

Three readings follow, and they are not the same concept:

**(a) Thermal reading (what the label says).** The environment determined by any animal whose body temperature is set by heat exchange with its surroundings. This is what the name asserts and what the proposed definition captures.

**(b) Complement reading (what the data is).** "Animal host, not a mammal or bird." 75% of the strings are invertebrates; reptiles and amphibians — the textbook ectotherms — are 3%. Nothing in the strings suggests the curator was reasoning about thermal physiology; they were reasoning about which animal phylum, and routing everything non-avian, non-mammalian here.

**(c) Site-unresolved reading.** As with the endotherm sibling, the label is also where strings land when the body site could not be resolved to a level-4 term — except that here there *are* no level-4 terms, so even `termite hindgut` and `fish intestine`, which do name a site, have nowhere else to go.

Readings (a) and (b) are extensionally near-identical (every host named is in fact an ectotherm), so the thermal definition is defensible. **Reading (c) is why the record can never be more precise than "host, site unresolved."**

### 1.3 A recorded observation, not an inference: upstream declined to give this label a temperature

The rows in upstream's `environments.csv`, verbatim (header: `Main group,Type,Water,water variability,Nutrients,Gradients,Organic,Structural,Pressure,Temperature,temp variability,Salinity,salinity variability,pH,Cobo-Simon habitat,WvS,CSadj,ENVO_terms,ENVO_ids`):

```
Host_associated,host_animal,           …,low,NA,    low,NA,NA,    NA,    host,NA,NA,           animal-associated environment,ENVO:01001002
Host_associated,host_animal_ectotherm, …,low,NA,    NA, NA,small, medium,host,NA,host_internal,,
Host_associated,host_animal_endotherm, …,low,medium,low,NA,small, medium,host,NA,host_internal,,
```

Two facts a curator can lean on:

1. **`Temperature` and `temp variability` are both `NA` for the ectotherm label**, while the endotherm label carries `Temperature: medium` and `temp variability: low`. Upstream's own curators, forced to assign a thermal band, assigned one to the endotherm and refused to assign one to the ectotherm. That refusal *is* the differentia: an ectotherm-associated environment has no characteristic temperature. This corpus preserves exactly that — `data/raw/environment_parameters.tsv` holds only `Pressure: low`, `pH: medium`, `salinity variability: small` for this label, and no temperature parameter at all.
2. **The `ENVO_terms`/`ENVO_ids` cells are empty**, as they are for `host_animal_endotherm` and the level-4 labels, while `host_animal`, `host_fungus`, `host_algae` and `host_plant` all carry one. The paper explains the gaps: *"ENVO annotations do not currently appear in the data products because most environmental terms required the union of multiple ENVO terms."* That empty cell is independent upstream corroboration that no single ENVO term names this concept. The kg-microbe mapping row in `data/raw/isolation_source_groundings.tsv` is likewise empty — which under this repo's rules means UNGROUNDED stands, not that a weaker lexical grounding should be attempted.

### 1.4 Boundary

**Inside:** any site on or in an ectothermic animal treated as a microbial habitat — insect gut and bacteriome, tick, sponge mesohyl, coral mucus, mollusc gill, fish intestine/skin/kidney, reptile or amphibian gut — where the host's failure to regulate its own temperature is the salient environmental property.

**Outside (neighbouring concepts):**

| Neighbour | Why it is not this |
|---|---|
| `host_animal_endotherm` (`habitatmech:BACDIVE.3d543e6b49`, 5,130 taxa) | Sibling; host holds a regulated elevated temperature |
| `host_animal` → `ENVO:01001002` (144 taxa, already a record in this corpus) | Parent; thermal strategy unstated |
| `fish` (`habitatmech:GOLD.3d529a667e`, 1,350), `arthropoda_insects` (`GOLD.dba2a83b95`, 1,833), `mollusca` (`GOLD.6acc0797e9`, 784), `invertebrates` (`GOLD.4d792ac724`, 621), `porifera`, `cnidaria`, `nematoda`, `reptilia`, `amphibia` | **Constituents.** Every major host group pooled here already exists as its own UNGROUNDED, REVIEWED record in `data/habitats/host_associated/`. This concept is a coarser cross-cut over them — see §6.2 |
| Protists and amoebae | Not animals at all; upstream mismapping (§6.2) |
| `UBERON:0000468` *multicellular organism* (Madin's level-1 `host`, 1,249 taxa) | Grandparent in the source scheme, and an organism term, not a place |

---

## 2. Genus — the broader kind

### 2.1 The match

**`ENVO:01001002` — *animal-associated environment*** · "An environmental system determined by an animal." Synonyms: *Metazoan-associated environment*, *animal environment*. [OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002). Present and `directly_referenced` in this repo's vendored slice (`data/raw/ontology_terms.tsv`).

This is the smallest well-established kind the concept falls under, and it is exactly the term upstream itself assigned to the parent label `host_animal`. It is *strictly broader*: it subsumes the endotherm sibling too.

### 2.2 Near-misses, and why each fails

Exhaustive OLS4 sweep of ENVO's organism-associated branch (retrieved 17 Aug 2026) returns only eight classes; every one is checked below. All CURIEs named here were verified present in this repo's vendored slice.

| Term | Verdict |
|---|---|
| `ENVO:01001176` *environment associated with an aquatic invertebrate* — "An environment which has its properties and composition largely determined by the presence of a metazoan which lacks a vetebral column [sic] and which has a habitat that is found in an aquatic environmental system." | **The strongest near-miss, and it still fails.** It covers a large share of the strings (molluscs, sponges, cnidarians, echinoderms, tunicates, marine worms ≈ 106/335) but is **narrower on two axes** — it excludes the 46 fish, the 11 reptiles/amphibians, and every terrestrial insect (termite, honeybee, tick, aphid, beetle), which is the single largest group here. It also asserts *aquatic* and *invertebrate*, neither of which the sources claim for the label as a whole. Worth recording as an `xref` candidate at most. |
| `ENVO:01001000` *environmental system determined by an organism*, exact synonym **"host-associated environment"** | **Too broad by two levels.** Subsumes plant-, fungus- and alga-associated. It is what several sibling records in this corpus (`porifera`, `mollusca`, `reptilia`, `amphibia`) already carry as parent, so it is available — but `ENVO:01001002` is tighter and equally safe. |
| `ENVO:01001055` *environment associated with an animal part or small animal* | **Asserts what the sources do not.** "Part of" and "small" are claims the label does not make; `reef-building coral` and `reticulated python` are neither. |
| `ENVO:01001179` *cnidarian-associated environment* | **Narrower** — covers 21 of 335 strings. It does demonstrate that ENVO subdivides `ENVO:01001002` **by host clade, never by thermal physiology**. |
| `ENVO:01001001` *plant-associated environment*, `ENVO:01001041` *fungi-associated environment*, `ENVO:01001057`/`01001058` (plant/fungal part) | Wrong kingdom. |
| `UBERON:0000468` *multicellular organism* | An organism class, not a place. Per CLAUDE.md the organism term goes in `relation: xref`, never as identity. |
| A taxon term for "ectotherms" (NCBITaxon) | **Does not exist and cannot.** Ectothermy is the ancestral condition across all animal phyla; no clade corresponds to it. |
| A PATO quality for ectothermy | **None found.** OLS4 searches for *ectotherm*, *ectothermy*, *poikilotherm*, *cold-blooded* return no PATO class. The only near-anything is `NCIT:C14320` *Poikilotherms* — "Animals which have a body temperature which is largely controlled by external factors of the environment" — an **organism grouping**, in the wrong ontology for this corpus, and describing poikilothermy (variability) rather than ectothermy (heat source). `SNOMED:56173004` *Poikilothermia* is a human clinical sign. |

**There is no ectotherm-, invertebrate-, insect-, fish-, reptile- or amphibian-associated environment term in ENVO.**

---

## 3. Differentia — what distinguishes it

### 3.1 The primary differentia: temperature conforms to ambient

The authoritative definitions are in the IUPS Thermal Commission's *Glossary of Terms for Thermal Physiology*, 3rd edn, **Japanese Journal of Physiology** 51(2):245–280 (April 2001) — [record](https://www.oalib.com/references/5710552), [Semantic Scholar](https://www.semanticscholar.org/paper/254ca3285e5ee8bb5bf73d0bd31d4a8576fc3b7d); 2nd edn [PMID 3324054](https://pubmed.ncbi.nlm.nih.gov/3324054/). Ectothermy is the pattern of thermoregulation in which body temperature depends on behaviourally controlled heat exchange with the environment rather than on a high, controlled rate of metabolic heat production. **Caveat, stated plainly: I could not open the glossary PDF (the hosting site returned HTTP 403), and search snippets indicate the substantive entry is filed under "Temperature regulator, ectothermic" rather than as a standalone "ectothermy" headword. Verify the exact wording against the printed glossary before quoting it in a definition.**

The operational consequence for a habitat is what Sepulveda & Moeller state in their review: temperature is *"a prominent abiotic environmental variable that drives the adaptive trajectories of animal lineages"* and *"temperature variation shapes the composition and function of animal gut microbiomes."* — Sepulveda J & Moeller AH (10 Mar 2020) *The Effects of Temperature on Animal Gut Microbiomes*, **Front Microbiol** 11:384. [doi:10.3389/fmicb.2020.00384](https://doi.org/10.3389/fmicb.2020.00384) · [PMID 32210948](https://pubmed.ncbi.nlm.nih.gov/32210948/). Their review spans Chordata, Arthropoda and Mollusca — the same phyla that dominate this bucket.

Because an ectotherm does not defend a set point, the environment it determines has **no characteristic temperature and high thermal variability** — daily, seasonal and latitudinal. That is a directly measurable property, and it is the mirror image of what upstream recorded for the endotherm sibling (`temp variability: low`). See Huus KE & Ley RE (28 Sep 2021) *Blowing Hot and Cold: Body Temperature and the Microbiome*, **mSystems** 6(5):e00707-21, [doi:10.1128/mSystems.00707-21](https://doi.org/10.1128/msystems.00707-21) · [PMID 34581596](https://pubmed.ncbi.nlm.nih.gov/34581596/) · [PMC8552956](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8552956/), which makes the general case that body temperature varies across the animal kingdom and is a core control on microbial growth. *(Note: this review is by Huus & Ley, not Fontaine & Kohl — the sibling `host_animal_endotherm` report in `research/habitats/host_associated/` attributes it to the wrong authors, and any claim taken from it should be re-checked.)*

### 3.2 Consequence 1: the habitat lacks the thermal exclusion filter that defines the endotherm sibling

This is the strongest published contrast, and it is stated in exactly these terms. Casadevall's thermal-barrier work quantified the filter on the endotherm side:

> "We analyzed the thermal tolerance of 4802 fungal strains from 144 genera and found that most cannot grow at mammalian temperatures. Fungi from insects and mammals had greater thermal tolerances than did isolates from soils and plants. Every 1 degrees C increase in the 30 degrees C–40 degrees C range excluded an additional 6% of fungal isolates…"
> — Robert VA & Casadevall A (15 Nov 2009) *Vertebrate endothermy restricts most fungi as potential pathogens*, **J Infect Dis** 200(10):1623–1626. [doi:10.1086/644642](https://doi.org/10.1086/644642) · [PMID 19827944](https://pubmed.ncbi.nlm.nih.gov/19827944/) (abstract verified verbatim)

And the ectotherm side is named explicitly: amphibians *"like mammals … have adaptive immunity, but unlike mammals they are ectotherms and lack a thermal environment that is exclusionary to fungi,"* and can be cured of chytridiomycosis by being held at 37 °C — Casadevall A (2012) *Fungi and the Rise of Mammals*, **PLoS Pathog** 8(8):e1002808. [doi:10.1371/journal.ppat.1002808](https://doi.org/10.1371/journal.ppat.1002808). The originating argument — that fungi are frequent pathogens of insects, amphibians and plants but rare systemic pathogens of mammals — is Casadevall A (2005) *Fungal virulence, vertebrate endothermy, and dinosaur extinction: is there a connection?*, **Fungal Genet Biol** ([PMID 15670708](https://pubmed.ncbi.nlm.nih.gov/15670708/)); the metabolic-cost optimum is modelled in Bergman A & Casadevall A (2010) **mBio** 1:e00212-10 ([doi:10.1128/mBio.00212-10](https://doi.org/10.1128/mbio.00212-10)).

**This is a genuine, citable, observable difference in the habitat itself** — an ectotherm-associated environment admits a mesophilic microbiota that an endotherm-associated one excludes.

### 3.3 Consequence 2: the microbiota is thermally labile

Experimental manipulation in ectotherms repeatedly shifts community composition and diversity — for example Fontaine SS, Novarro AJ & Kohl KD (2018) *Environmental temperature alters the digestive performance and gut microbiota of a terrestrial amphibian*, **J Exp Biol** 221:jeb187559 ([journal](https://journals.biologists.com/jeb/article/221/20/jeb187559/19674/Environmental-temperature-alters-the-digestive)); Moeller AH et al. (2020) *The lizard gut microbiome changes with temperature and is associated with heat tolerance*, **Appl Environ Microbiol** 86(17); and, on the fish side, *Gut microbiota of two invasive fishes respond differently to temperature*, **Front Microbiol** 14:1087777 (2023), [PMC10088563](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10088563/). Effects are not uniform — see §3.5.

### 3.4 Consequence 3: compositional distinctness across the endotherm/ectotherm split

Youngblut ND, Reischer GH, Walters W, Schuster N, Walzer C, Stalder G, Ley RE & Farnleitner AH (2019) *Host diet and evolutionary history explain different aspects of gut microbiome diversity among vertebrate clades*, **Nat Commun** 10:2200 ([doi:10.1038/s41467-019-10191-3](https://doi.org/10.1038/s41467-019-10191-3), [PMID 31097702](https://pubmed.ncbi.nlm.nih.gov/31097702/)) analysed a dataset that is 80% wild animals and spans Mammalia, Aves, Reptilia, Amphibia and Actinopterygii. **Stated honestly: the abstract does not itself frame results as ectotherm-vs-endotherm** — cite it for the cross-class dataset, not for a thermal conclusion. The taxonomic-sampling bias that makes such comparisons hard is documented in Colston TJ & Jackson CR (2016) *Microbiome evolution along divergent branches of the vertebrate tree of life: what is known and unknown*, **Mol Ecol** 25(16):3776–3800 ([doi:10.1111/mec.13730](https://doi.org/10.1111/mec.13730), [PMID 27297628](https://pubmed.ncbi.nlm.nih.gov/27297628/)): >90% of microbiome studies address mammals, which are 8% of described vertebrate species.

For the invertebrate majority of this bucket, the relevant habitat literature is not thermal at all: insect guts are *"distinctive environments for microbial colonization"* whose morphology and physicochemistry structure the community, and most contain few species compared with mammalian guts — Engel P & Moran NA (2013) *The gut microbiota of insects – diversity in structure and function*, **FEMS Microbiol Rev** 37(5):699–735 ([doi:10.1111/1574-6976.12025](https://doi.org/10.1111/1574-6976.12025)). Sponges host dense, host-species-specific communities markedly distinct from surrounding seawater — Thomas T et al. (2016) *Diversity, structure and convergent evolution of the global sponge microbiome*, **Nat Commun** 7:11870 ([doi:10.1038/ncomms11870](https://doi.org/10.1038/ncomms11870), [PMC4912640](https://pmc.ncbi.nlm.nih.gov/articles/PMC4912640)).

### 3.5 Honest counter-evidence

The differentia should rest on the **physical property** (no regulated temperature; high thermal variability), not on a claim that ectotherm microbiomes respond differently to warming. A meta-analysis found that microbiome changes under thermal treatment were *"determined by host habitat rather than host biological traits, and endotherms experienced a similar level of microbiome diversity decrease as ectotherms"* — *Experimental temperatures shape host microbiome diversity and composition*, **Glob Change Biol** (2022), [doi:10.1111/gcb.16429](https://onlinelibrary.wiley.com/doi/full/10.1111/gcb.16429). And individual studies dissent: *Xenopus tropicalis* showed no alpha-diversity effect ([PMID 31686318](https://pubmed.ncbi.nlm.nih.gov/31686318/)), and wood frog gut microbiomes were largely unchanged at CTmax ([PMID 39855620](https://pubmed.ncbi.nlm.nih.gov/39855620/)).

### 3.6 Measurability

The differentia is recordable in standard metadata: MIxS defines `host_body_temp` in the host-associated extension ([`MIXS:0016002`](https://genomicsstandardsconsortium.github.io/mixs/0016002/)) and `temp` ([`MIXS:0000113`](https://genomicsstandardsconsortium.github.io/mixs/0000113/)) as a general environment field. MIxS/ENVO guidance routes host-associated `env_medium` ([`MIXS:0000014`](https://genomicsstandardsconsortium.github.io/mixs/0000014/)) to UBERON/PO tissue terms — which is precisely why the site-unspecified level of this concept has no MIxS home and needs an ENVO-style habitat term. ([Using ENVO with MIxS](https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS))

---

## 4. Sources

1. Madin JS et al. (5 Jun 2020) **Sci Data** 7:170. [doi:10.1038/s41597-020-0497-4](https://doi.org/10.1038/s41597-020-0497-4) · PMID 32503990 · [PMC7275036](https://pmc.ncbi.nlm.nih.gov/articles/PMC7275036/) — the scheme, the four-level hierarchy, the "not resolved" rule, the ENVO-annotation gap. Quotes in §1.1 and §1.3 verified against PMC full text.
2. bacteria-archaea-traits [conversion tables](https://github.com/bacteria-archaea-traits/bacteria-archaea-traits/tree/master/data/conversion_tables) v1.0.0 (2020) — [`environments.csv`](https://github.com/bacteria-archaea-traits/bacteria-archaea-traits/blob/master/data/conversion_tables/environments.csv) (label set, physicochemical bands, empty ENVO cell, no level-4 children); [`renaming_isolation_source.csv`](https://github.com/bacteria-archaea-traits/bacteria-archaea-traits/blob/master/data/conversion_tables/renaming_isolation_source.csv) (the 335 strings; counted directly). Data release: [doi:10.6084/m9.figshare.c.4843290](https://doi.org/10.6084/m9.figshare.c.4843290).
3. IUPS Thermal Commission (2001) *Glossary of terms for thermal physiology*, 3rd edn, **Jpn J Physiol** 51:245–280 — [record](https://www.oalib.com/references/5710552) · 2nd edn [PMID 3324054](https://pubmed.ncbi.nlm.nih.gov/3324054/). **Full text not retrieved (403); wording unverified.**
4. Robert VA & Casadevall A (2009) **J Infect Dis** 200:1623–1626. [doi:10.1086/644642](https://doi.org/10.1086/644642) · [PMID 19827944](https://pubmed.ncbi.nlm.nih.gov/19827944/) — abstract verified verbatim.
5. Casadevall A (2012) **PLoS Pathog** 8:e1002808. [doi:10.1371/journal.ppat.1002808](https://doi.org/10.1371/journal.ppat.1002808) — the ectotherms-lack-a-thermal-exclusion-zone statement.
6. Casadevall A (2005) **Fungal Genet Biol**. [PMID 15670708](https://pubmed.ncbi.nlm.nih.gov/15670708/) · Bergman A & Casadevall A (2010) **mBio** 1:e00212-10. [doi:10.1128/mBio.00212-10](https://doi.org/10.1128/mbio.00212-10)
7. Sepulveda J & Moeller AH (2020) **Front Microbiol** 11:384. [doi:10.3389/fmicb.2020.00384](https://doi.org/10.3389/fmicb.2020.00384) · [PMID 32210948](https://pubmed.ncbi.nlm.nih.gov/32210948/)
8. Huus KE & Ley RE (2021) **mSystems** 6:e00707-21. [doi:10.1128/mSystems.00707-21](https://doi.org/10.1128/msystems.00707-21) · [PMID 34581596](https://pubmed.ncbi.nlm.nih.gov/34581596/)
9. Fontaine SS, Novarro AJ & Kohl KD (2018) **J Exp Biol** 221:jeb187559. [link](https://journals.biologists.com/jeb/article/221/20/jeb187559/19674/Environmental-temperature-alters-the-digestive) · Moeller AH et al. (2020) **Appl Environ Microbiol** 86(17) · *Front Microbiol* 14:1087777 (2023), [PMC10088563](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10088563/)
10. Youngblut ND et al. (2019) **Nat Commun** 10:2200. [doi:10.1038/s41467-019-10191-3](https://doi.org/10.1038/s41467-019-10191-3) · [PMID 31097702](https://pubmed.ncbi.nlm.nih.gov/31097702/)
11. Colston TJ & Jackson CR (2016) **Mol Ecol** 25:3776–3800. [doi:10.1111/mec.13730](https://doi.org/10.1111/mec.13730) · [PMID 27297628](https://pubmed.ncbi.nlm.nih.gov/27297628/)
12. Engel P & Moran NA (2013) **FEMS Microbiol Rev** 37:699–735. [doi:10.1111/1574-6976.12025](https://doi.org/10.1111/1574-6976.12025) · Thomas T et al. (2016) **Nat Commun** 7:11870. [doi:10.1038/ncomms11870](https://doi.org/10.1038/ncomms11870)
13. *Experimental temperatures shape host microbiome diversity and composition* (2022) **Glob Change Biol**. [doi:10.1111/gcb.16429](https://onlinelibrary.wiley.com/doi/full/10.1111/gcb.16429) — counter-evidence.
14. ENVO via OLS4 (retrieved 17 Aug 2026): [ENVO:01001002](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002), [ENVO:01001000](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001000), [ENVO:01001055](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001055), [ENVO:01001176](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001176), [ENVO:01001179](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001179); `NCIT:C14320`, `SNOMED:56173004` via OLS4 search.
15. GSC MIxS: [`MIXS:0016002`](https://genomicsstandardsconsortium.github.io/mixs/0016002/), [`MIXS:0000014`](https://genomicsstandardsconsortium.github.io/mixs/0000014/), [Using ENVO with MIxS](https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS).

**Explicitly flagged as my inference, not sourced:** (i) the host-group tally in §1.2 (my regex classification of upstream's 335 strings — reproducible, but not an upstream statement); (ii) the reading that this bucket is the *complement* of the endotherm bucket rather than a thermally-motivated class; (iii) that the `Temperature: NA` cell reflects a deliberate refusal rather than an oversight — the pattern is consistent but upstream never says so; (iv) that `ENVO:01001002` is the correct genus (a modelling judgement, though it is the term upstream itself chose for the parent label); (v) the recommended `GROUND_AS_PARENT` disposition. **No source defines `host_animal_ectotherm`** — Madin et al. define the scheme's structure but never gloss the individual labels. The definition has to be constructed, which is why the term exists.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**
- ectotherm-associated environment; ectothermic host environment
- cold-blooded animal host (colloquial; deprecated in thermal physiology)
- non-avian, non-mammalian animal host (the extensional gloss, and honestly the most accurate one for this data)
- "host_internal" in the Cobo-Simón habitat coarsening carried in the same upstream row (a *coarser* grouping, not a synonym)

**Do NOT conflate**

| Confusable | Why it differs |
|---|---|
| **poikilotherm** | Ectothermy = *source* of heat (external); poikilothermy = *variability* of body temperature. Not coextensive: a deep-sea or cave ectotherm at constant ambient is near-homeothermic; a hibernating mammal is an endotherm that is not homeothermic. `NCIT:C14320` *Poikilotherms* is the poikilothermy concept and is an organism grouping, not a place. |
| **"cold-blooded"** | Pre-theoretical; replaced by the ectotherm/endotherm pair in thermal physiology. Acceptable as an exact synonym on the record; not in the definition text. |
| **invertebrates** | 75% of the strings, but a proper part — fish, reptiles and amphibians are vertebrate ectotherms, and this corpus already carries `invertebrates` (`habitatmech:GOLD.4d792ac724`) as its own record. |
| **`ENVO:01001176` environment associated with an aquatic invertebrate** | Narrower on two axes (aquatic, invertebrate); excludes terrestrial insects, the largest group here. Candidate `xref`, not identity. |
| **The clade-specific records already in this corpus** (`fish`, `arthropoda_insects`, `mollusca`, `porifera`, `cnidaria`, `nematoda`, `reptilia`, `amphibia`) | Constituents, not synonyms. This concept is a cross-cutting pooling over all of them. |
| **`host_animal` / `ENVO:01001002`** | The genus, one level up; includes endotherm hosts. Already an existing record. |
| **protists, protozoa, amoebae** | Not animals. Their presence in this bucket is an upstream mismapping (§6.2), and grounding decisions must not inherit it. |
| **`ENVO:01001000`'s synonym "host-associated environment"** | Attaches to the *organism-determined* superclass and covers plants and fungi. |

---

## 6. Should it be a term at all?

### 6.1 Yes — it is a habitat, and `NOT_APPLICABLE` would be wrong

It denotes a place where microbes live (the body of a cold-blooded animal), not a process, disease, quality, procedure, or taxon. It fits this repo's settled line exactly: *"An organism acting as a host IS a habitat; the taxon term is not."* And `ectotherm` is a physiological predicate, not a clade — so the organism-term trap does not even arise, and `tests/test_decisions.py` would (correctly) reject a `NOT_APPLICABLE` here. At 999 taxa it is the seventh-largest habitat in the Madin scheme carried by this corpus, and it is the point at which ENVO's `animal-associated environment` branch stops resolving.

### 6.2 Three caveats the curator should record in `notes`

**(a) It is a residual class, not a natural kind.** Every major constituent already exists as a separate, REVIEWED record in `data/habitats/host_associated/` — `fish` (1,350 GOLD organisms), `arthropoda_insects` (1,833), `mollusca` (784), `invertebrates` (621), `reptilia` (133), `cnidaria` (102), `porifera` (90), `nematoda`, `amphibia` (41). This concept pools them under a thermal predicate no upstream curator was actually applying. The term is defensible; it is also low-yield, and if an ENVO term request is ever made, the constituent groups are the better investment.

**(b) The thermal differentia is the one thing upstream declined to state.** `environments.csv` gives the endotherm label a temperature band and a variability band and gives this one neither. The definition turns that absence into the differentia, which is logically right but should be recorded as a curator's reading, not as an upstream assertion.

**(c) Documented upstream mismappings, not to be propagated.** Twelve strings are protists, protozoa or amoebae (`other, amoebae cytoplasm`, `Obligate intracellular parasite of Acanthamoeba castellanii.`) — not animals at all, so they do not belong under `ENVO:01001002`. Two are plant rhizosphere (`host-associated, plants, rhizosphere, soil`). One is `other, isolated from air`. Two are bare marine environmental strings with no host named. That is ~17/335 (5%) demonstrably wrong at the level of the genus.

### 6.3 Concrete recommendation for `curation/decisions.tsv`

| Field | Value |
|---|---|
| key | `habitatmech:BACDIVE.e68bf42dcb` |
| decision | `GROUND_AS_PARENT` |
| target | `ENVO:01001002` |
| expected label | `animal-associated environment` |
| relation | `parent` (genuinely broader — an ectotherm-associated environment *is* an animal-associated environment) |

Optionally add `ENVO:01001176` *environment associated with an aquatic invertebrate* with `relation: xref` — it covers roughly a third of the attested strings and records the link without asserting an is-a. Do **not** attach `UBERON:0000468` or any clade term as `parent`; if a host-kind link is wanted, it belongs in `relation: xref`. This mirrors the disposition recommended for the endotherm sibling, which keeps the two records parallel and keeps the 999 ectotherm assertions out of the existing 144-taxon `animal_associated_environment` record.

The concept remains a **term-request candidate** — proposed label *ectothermic animal-associated environment*, exact synonym *cold-blooded animal-associated environment*, genus `ENVO:01001002`, natural companion to the `host_animal_endotherm` request. Per the standing rule in this project's memory, **nothing goes to ENVO without your explicit per-request approval**; this report only records that the gap exists and what the request would say.

**Sources:** [Madin et al. 2020 Sci Data](https://doi.org/10.1038/s41597-020-0497-4) · [PMC7275036](https://pmc.ncbi.nlm.nih.gov/articles/PMC7275036/) · [bacteria-archaea-traits conversion tables](https://github.com/bacteria-archaea-traits/bacteria-archaea-traits/tree/master/data/conversion_tables) · [IUPS Thermal Glossary record](https://www.oalib.com/references/5710552) · [Robert & Casadevall 2009 JID](https://doi.org/10.1086/644642) · [Casadevall 2012 PLoS Pathog](https://doi.org/10.1371/journal.ppat.1002808) · [Bergman & Casadevall 2010 mBio](https://doi.org/10.1128/mbio.00212-10) · [Sepulveda & Moeller 2020 Front Microbiol](https://doi.org/10.3389/fmicb.2020.00384) · [Huus & Ley 2021 mSystems](https://doi.org/10.1128/msystems.00707-21) · [Fontaine et al. 2018 JEB](https://journals.biologists.com/jeb/article/221/20/jeb187559/19674/Environmental-temperature-alters-the-digestive) · [Youngblut et al. 2019 Nat Commun](https://doi.org/10.1038/s41467-019-10191-3) · [Colston & Jackson 2016 Mol Ecol](https://doi.org/10.1111/mec.13730) · [Engel & Moran 2013 FEMS](https://doi.org/10.1111/1574-6976.12025) · [Thomas et al. 2016 Nat Commun](https://doi.org/10.1038/ncomms11870) · [Glob Change Biol 2022](https://onlinelibrary.wiley.com/doi/full/10.1111/gcb.16429) · [ENVO:01001002 (OLS4)](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002) · [ENVO:01001176 (OLS4)](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001176) · [MIxS host-associated](https://genomicsstandardsconsortium.github.io/mixs/0016002/) · [MIxS env_medium](https://genomicsstandardsconsortium.github.io/mixs/0000014/) · [Using ENVO with MIxS](https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS)

## Citations

1. https://doi.org/10.1038/s41597-020-0497-4
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC7275036/
3. https://github.com/bacteria-archaea-traits/bacteria-archaea-traits/blob/master/data/conversion_tables/environments.csv
4. https://github.com/bacteria-archaea-traits/bacteria-archaea-traits/blob/master/data/conversion_tables/renaming_isolation_source.csv
5. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002
6. https://www.oalib.com/references/5710552
7. https://www.semanticscholar.org/paper/254ca3285e5ee8bb5bf73d0bd31d4a8576fc3b7d
8. https://pubmed.ncbi.nlm.nih.gov/3324054/
9. https://doi.org/10.3389/fmicb.2020.00384
10. https://pubmed.ncbi.nlm.nih.gov/32210948/
11. https://doi.org/10.1128/msystems.00707-21
12. https://pubmed.ncbi.nlm.nih.gov/34581596/
13. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8552956/
14. https://doi.org/10.1086/644642
15. https://pubmed.ncbi.nlm.nih.gov/19827944/
16. https://doi.org/10.1371/journal.ppat.1002808
17. https://pubmed.ncbi.nlm.nih.gov/15670708/
18. https://doi.org/10.1128/mbio.00212-10
19. https://journals.biologists.com/jeb/article/221/20/jeb187559/19674/Environmental-temperature-alters-the-digestive
20. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10088563/
21. https://doi.org/10.1038/s41467-019-10191-3
22. https://pubmed.ncbi.nlm.nih.gov/31097702/
23. https://doi.org/10.1111/mec.13730
24. https://pubmed.ncbi.nlm.nih.gov/27297628/
25. https://doi.org/10.1111/1574-6976.12025
26. https://doi.org/10.1038/ncomms11870
27. https://pmc.ncbi.nlm.nih.gov/articles/PMC4912640
28. https://onlinelibrary.wiley.com/doi/full/10.1111/gcb.16429
29. https://pubmed.ncbi.nlm.nih.gov/31686318/
30. https://pubmed.ncbi.nlm.nih.gov/39855620/
31. https://genomicsstandardsconsortium.github.io/mixs/0016002/
32. https://genomicsstandardsconsortium.github.io/mixs/0000113/
33. https://genomicsstandardsconsortium.github.io/mixs/0000014/
34. https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
35. https://github.com/bacteria-archaea-traits/bacteria-archaea-traits/tree/master/data/conversion_tables
36. https://doi.org/10.6084/m9.figshare.c.4843290
37. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001000
38. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001055
39. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001176
40. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001179