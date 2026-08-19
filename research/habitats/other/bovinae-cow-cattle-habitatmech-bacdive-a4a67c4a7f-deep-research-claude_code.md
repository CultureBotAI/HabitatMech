---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T16:32:52.790917'
end_time: '2026-08-17T16:41:20.049117'
duration_seconds: 507.26
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Bovinae-Cow,-Cattle
  habitat_identifier: habitatmech:BACDIVE.a4a67c4a7f
  habitat_category: OTHER
  grounding_status: UNGROUNDED
  attestations: 'BACDIVE: Bovinae-Cow,-Cattle'
  assertions: '619'
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
    \ not a habitat, which is a stronger and false claim. (source concept habitatmech:BACDIVE.a4a67c4a7f)"
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
  web_search_requests: 16
  num_turns: 32
  total_cost_usd: 3.4733555000000007
  session_id: 9921baad-9ee8-4edb-82d9-4cff9845238c
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 28
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Bovinae-Cow,-Cattle
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.a4a67c4a7f
- **Category:** OTHER
- **Grounding status:** UNGROUNDED
- **Source attestations:** BACDIVE: Bovinae-Cow,-Cattle
- **Upstream assertion volume:** 619
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it — the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE while its own child Porifera > Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM — a phylum is a class of organisms, not a place — so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. (source concept habitatmech:BACDIVE.a4a67c4a7f)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Bovinae-Cow,-Cattle** as a microbial habitat, with citations.

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

# Bovinae‑Cow,‑Cattle (`habitatmech:BACDIVE.a4a67c4a7f`) — definition research

> **Proposed definition**
>
> **An animal-associated environment which is determined by a domesticated ruminant of the subfamily Bovinae — chiefly cattle, *Bos taurus* and *Bos indicus* — whose foregut-fermenting digestive anatomy, endothermic body temperature and managed husbandry distinguish it from environments determined by other animals.**

Shorter alternative if the curator prefers the minimal differentia:

> An animal-associated environment which is determined by an animal of the subfamily Bovinae, chiefly domestic cattle.

A note on why the sentence is at the edge of one clause is in §2: there is no `mammal-associated environment` or `vertebrate-associated environment` intermediate in ENVO, so the differentia has to carry the whole distance from "animal" down to "cattle" in a single step. That missing intermediate is worth recording as a separate observation, not worth lengthening this definition for.

---

## 1. What the concept denotes

### The source path

The label is a **BacDive Microbial Isolation Source Ontology (MISO)** category-3 tag. MISO is "hierarchically ordered into three levels of tags (category 1–3)", with eight top-level classes: `#Environmental`, `#Engineered`, `#Host`, `#Host body-site`, `#Host body-product`, `#Medical`, `#Condition` and `#Climate` ([Reimer et al., *Nucleic Acids Res.* 47:D631, 2019](https://academic.oup.com/nar/article/47/D1/D631/5106998), doi:10.1093/nar/gky879). Fetching the live BacDive isolation-source browser confirms the path for this tag:

```
#Host  ▸  #Mammals  ▸  Bovinae (Cow, Cattle)
```
([https://bacdive.dsmz.de/isolation-sources](https://bacdive.dsmz.de/isolation-sources), retrieved 2026-08-17)

**This matters for the definition**, because MISO separates `#Host` from `#Host body-site` and `#Host body-product` as sibling top-level classes. The tag therefore denotes **the animal itself as the environment a strain was recovered from** — the host organism as a place — and *not* the rumen (a body site), *not* the milk (a body product), and *not* the barn or the pasture (`#Engineered` / `#Environmental`). In practice a strain record carries the `#Host` tag alongside a body-site tag where the depositor recorded one; the `#Host` tag alone is what a record says when the host organism is the strongest statement available about where the microbe lived.

The current BacDive release maintains this framing: "For understanding the ecological role of a microbial strain, its isolation source is of major importance," with environmental categorization into "aquatic, soil, animal and plant" ([Schober et al., *Nucleic Acids Res.* 53:D748, 2025](https://academic.oup.com/nar/article/53/D1/D748/7848838), doi:10.1093/nar/gkae959, PMID 39470737).

### What is inside the concept

Any body site, tissue, surface, secretion or luminal content of a live or recently slaughtered bovine, as the setting in which the microorganism was living when sampled. Empirically this spans at least:

- **reticulorumen and forestomachs** — the dominant contributor ([Seshadri et al., *Nat. Biotechnol.* 36:359, 2018](https://www.nature.com/articles/nbt.4110), doi:10.1038/nbt.4110; [Stewart et al., *Nat. Biotechnol.* 37:953, 2019](https://www.nature.com/articles/s41587-019-0202-3), doi:10.1038/s41587-019-0202-3)
- **lower gut and feces** ([Holman & Gzyl meta-analysis, *FEMS Microbiol. Ecol.* 95:fiz072, 2019](https://academic.oup.com/femsec/article/95/6/fiz072/5497297), doi:10.1093/femsec/fiz072)
- **udder, teat canal and milk** ([Derakhshani et al., invited review, *J. Dairy Sci.* 101:10605, 2018](https://www.sciencedirect.com/science/article/pii/S0022030218309147), doi:10.3168/jds.2018-14860, PMID 30292553)
- **hide and skin** ([Bonardi et al., *Int. J. Food Microbiol.*, 2015](https://pubmed.ncbi.nlm.nih.gov/26392887/), PMID 26392887)
- **upper respiratory tract, vagina and uterus** ([Lima et al., *PLoS ONE* 14:e0208014, 2019](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0208014), doi:10.1371/journal.pone.0208014)
- **lesions and abscesses** — e.g. three *Leucobacter holotrichiae* strains from bovine actinomycotic abscesses ([PMC12738856](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12738856/))

### What is a neighbouring concept, not this one

| Neighbour | Why it is outside |
|---|---|
| Rumen / rumen fluid | A body site (`UBERON:0007365`, `UBERON:0010228`); MISO's `#Host body-site` class |
| Milk, colostrum, dairy products | A body product / food material; FOODON territory |
| Cow dung, manure, slurry, lagoon | Environmental material derived from cattle (`ENVO:01001116` *bovine dairy liquid manure*) — the microbes there are no longer in the host |
| Cow shed, feedlot, drylot, pasture | Built or managed settings *around* cattle (`ENVO:00003041`, `ENVO:01000627`, `ENVO:01000626`, `ENVO:00000266`) |
| Hide as a commodity | `ENVO:02000053` *hide* is a material for leather production, not the living integument |
| Beef, carcass, cured meat | `FOODON:00001696` etc. — post-slaughter food materials |

The MIxS host-associated extension draws exactly this line with a cattle example in its own scope note: soil sampled from a cow's hoof is better described by soil terms, whereas soil embedded in a wound on a cow's leg fits the host-associated extension ([GSC MIxS HostAssociated extension](https://genomicsstandardsconsortium.github.io/mixs/0016002/)).

### Ambiguity: how wide is "Bovinae"?

The label is internally inconsistent and the curator must resolve it explicitly rather than silently.

- **Reading A — the parenthetical (recommended).** "Cow, Cattle" names domestic cattle: *Bos taurus* (`NCBITaxon:9913`; NCBI exact synonyms include *bovine*, *cow*, *dairy cow*, *domestic cattle*, *ox*) and by extension zebu, *Bos indicus*.
- **Reading B — the head noun.** Bovinae (`NCBITaxon:27592`) is a subfamily of Bovidae containing ten genera: *Bison*, *Bos*, *Boselaphus*, *Bubalus*, *Pseudonovibos*, *Pseudoryx*, *Syncerus*, *Taurotragus*, *Tetracerus*, *Tragelaphus* ([NCBI Taxonomy Browser, taxid 27592](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=27592)). That takes in water buffalo, bison, African buffalo, yak, nilgai, eland, kudu and saola.

BacDive itself resolves this by putting the vernacular gloss in the tag, which is the strongest evidence available that the tag is *used* for cattle strains. **My recommendation** (this is inference, not a sourced claim): scope the term to domestic cattle and closely related domesticated bovines, name it *cattle-associated environment*, and record `NCBITaxon:27592` as an `xref` with an explicit note that the source label's head noun is broader than the concept as used. Adopting "Bovinae" verbatim would silently assert that a bison or water-buffalo isolate belongs to this record, which the source data does not support and which HabitatMech cannot verify from the tag alone.

---

## 2. Genus — the broader kind

### The match

**`ENVO:01001002` — *animal-associated environment***
Definition: *"An environmental system determined by an animal."* Synonyms: metazoan-associated environment, animal environment. It sits under `ENVO:01001000` *environmental system determined by an organism*.
([OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002))

This is the correct genus and the pattern is already established in ENVO for taxon-scoped children:

| CURIE | Label |
|---|---|
| `ENVO:01001001` | plant-associated environment |
| `ENVO:01001041` | fungi-associated environment |
| `ENVO:01001179` | cnidarian-associated environment |
| `ENVO:01001176` | environment associated with an aquatic invertebrate |

So `<X>-associated environment` is not an invented pattern — ENVO already mints classes of exactly this shape, including one scoped to a single animal phylum (Cnidaria). A *cattle-associated environment* sibling is a well-formed request against ENVO's own design.

### Near-misses and why each fails

| Candidate | Why it is not a match |
|---|---|
| `ENVO:01001002` *animal-associated environment* | **Broader.** This is the genus, not the term. Grounding here loses everything the 619 BacDive assertions actually say. |
| `ENVO:01001055` *environment associated with an animal part or small animal* | **Different, not broader.** "Part of a living or dead animal, or a whole small animal" — cattle are neither a part nor a small animal. |
| `ENVO:01001033` *digestive tract environment* (EMPO "Animal proximal gut") | **Narrower and host-agnostic.** One body site across all animals; would drop hide, milk, respiratory-tract and lesion isolates, and would falsely assert gut origin. |
| `ENVO:01001034` *environment determined by a biofilm on an animal surface* | Narrower and host-agnostic, same failure in the other direction. |
| `NCBITaxon:27592` *Bovinae*, `NCBITaxon:9913` *Bos taurus* | **A class of organisms, not a place.** This is the #99/#114 line exactly: keep as `relation: xref`, never as identity or `parent_habitats`. |
| `UBERON:0007365` *rumen*, `UBERON:0007364` *reticulorumen*, `UBERON:0010228` *ruminal fluid* | Anatomical structures, and narrower than the concept. Correct targets for a *rumen* habitat record; wrong for a whole-host record. |
| `ENVO:01001116` *bovine dairy liquid manure* | A derived environmental material, outside the host. Narrower and asserts a collection process the source does not claim. |
| `ENVO:00003041` *cow shed*, `ENVO:01000627` *feedlot*, `ENVO:00000266` *pasture*, `ENVO:01000247` *rangeland biome*, `ENVO:03501287` *livestock house* | Built or managed environments where cattle are kept — a different environmental system from the animal. |
| `ENVO:02000053` *hide* | A material obtained from animals for leather; asserts post-slaughter processing. |

**No intermediate exists.** Querying ENVO for every label of the form `*-associated environment` returns only the six classes listed above — there is no `mammal-associated environment`, `vertebrate-associated environment`, or `ruminant-associated environment`. ENVO has an open discussion of precisely this gap for host-associated samples ([EnvironmentOntology/envo issue #1029](https://github.com/EnvironmentOntology/envo/issues/1029)), which proposes host-associated / animal-associated / human-associated / plant-associated biome terms. **Recommendation (inference):** file the cattle term under `ENVO:01001002` and note the missing mammalian intermediate in the request rather than blocking on it.

---

## 3. Differentia — what distinguishes cattle from sibling animal hosts

Prefer these, in roughly descending order of how observable and unambiguous they are.

**(a) Host identity — the primary differentia.** The determining organism is a bovine of subfamily Bovinae, chiefly *Bos taurus* / *Bos indicus*. This is directly recordable and is the field the standards use: MIxS `host_taxid` (`MIXS:0000250`, an NCBI taxid) and `host scientific name` / `specific_host` (`MIXS:0000029`) ([GSC MIxS](https://genomicsstandardsconsortium.github.io/mixs/0000250/)). Lineage: Artiodactyla ▸ Ruminantia ▸ Pecora ▸ Bovidae ▸ Bovinae ([NCBI Taxonomy 27592](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=27592)).

**(b) Foregut fermentation — the functional differentia.** Cattle are foregut-fermenting ruminants: the stomach has four compartments (rumen, reticulum, omasum, abomasum; `UBERON:0007366`), of which the reticulorumen is a large pre-gastric anaerobic fermentation chamber. This is what makes the cattle-associated environment ecologically distinct from environments determined by monogastric mammals, and it is *why* the concept carries a distinctive microbiota rather than merely a distinctive host name:

- **Anaerobic and strongly reducing.** "The rumen is a complex ecosystem composed of mainly anaerobic bacteria, protozoa, fungi, methanogenic archaea and phages" ([Huws et al., *Front. Microbiol.* 9:2161, 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC6167468/), doi:10.3389/fmicb.2018.02161). Redox potential is uniformly and markedly negative; a systematic review across 15 studies and 24 diets found all recorded Eh values negative, "reflecting the absence of oxygen and strong reducing power," with method and diet the main sources of variation ([Huang et al., *J. Anim. Physiol. Anim. Nutr.* 102:e100, 2018](https://onlinelibrary.wiley.com/doi/10.1111/jpn.12855), doi:10.1111/jpn.12855, PMID 29352497). *Caveat:* the frequently quoted −250 to −400 mV figure traces to Hobson & Wallace (1982) via secondary citation and I did not verify it against the original; in-situ dairy-cattle measurements give −173 to −217 mV under oxygen-free sampling and −111 to −139 mV with a conventional suction device ([Marden et al., *J. Dairy Sci.* 88:277, 2005](https://www.sciencedirect.com/science/article/pii/S0022030205726850), doi:10.3168/jds.S0022-0302(05)72685-0). Use the qualitative claim ("strongly reducing, effectively anoxic"), not a single number.
- **Near-neutral to mildly acidic pH.** Measured ruminal pH in dairy cattle: 6.37–6.70 (oxygen-free sampling) and 6.49–6.93 (suction device) (Marden et al. 2005, above). Cellulolytic isolation work reports ruminal liquid at pH 6.9 ([Sahiwal cattle isolation study, PMC11055587](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11055587/)).
- **Mesophilic, host-thermostatted.** Rumen isolation and cultivation are routinely performed at 39 °C, matching bovine body temperature (PMC11055587, above).
- **Community structure.** Bacteria dominate (largely Bacteroidota and Bacillota); archaea are chiefly methanogenic Euryarchaeota (*Methanobrevibacter*, *Methanosphaera*, Methanosarcinales); ciliate protozoa are ~20% and up to 50% of microbial biomass under some conditions; anaerobic fungi are 10–20% (Huws et al. 2018). Cell densities commonly cited as 10⁹–10¹⁰ bacteria/mL and 10⁵–10⁶ protozoa/mL trace to Hungate (1966) — **secondary attribution I did not verify against the primary source**; treat as approximate.
- **Rumen-specific genomic signal.** The Hungate1000 catalog (501 genomes, ~75% of rumen genus-level taxa) showed rumen-specific enrichment for de novo vitamin B12 synthesis, ongoing evolution by gene loss, and underrepresentation of environmental-stress markers consistent with vertical inheritance ([Seshadri et al. 2018](https://www.nature.com/articles/nbt.4110), doi:10.1038/nbt.4110, PMID 29553575). A further 4,941 MAGs from 283 cattle extend the same picture ([Stewart et al. 2019](https://www.nature.com/articles/s41587-019-0202-3), doi:10.1038/s41587-019-0202-3).

**(c) Domestication and scale — the reason this habitat is so heavily sampled.** Cattle are managed livestock at a scale no wild animal host matches: ~1,575.8 million head worldwide in 2023, from FAOSTAT live-animal stocks ([FAOSTAT via Statista compilation](https://www.statista.com/statistics/263979/global-cattle-population-since-1990/); primary series: [FAOSTAT Crops and livestock products](https://www.fao.org/faostat/en/#data/QCL)). This is the plausible explanation for 619 upstream BacDive assertions on a single host tag — but the causal link between herd size and strain count is **my inference**, not a sourced claim.

**(d) Veterinary and zoonotic sampling context.** A substantial fraction of cattle-derived strains come from disease investigation rather than ecology. Cattle are the primary reservoir of *Escherichia coli* O157:H7, colonising the lower GI tract and shed asymptomatically in feces, with hides a documented slaughterhouse contamination route ([Bonardi et al. 2015](https://pubmed.ncbi.nlm.nih.gov/26392887/), PMID 26392887; [Elder et al., *PNAS* 97:2999, 2000](https://www.pnas.org/doi/10.1073/pnas.97.7.2959), doi:10.1073/pnas.97.7.2959; [non-O157 systematic review, *Anim. Health Res. Rev.*](https://www.cambridge.org/core/journals/animal-health-research-reviews/article/systematic-review-and-metaanalysis-of-published-literature-on-prevalence-of-nono157-shiga-toxinproducing-escherichia-coli-serogroups-o26-o45-o103-o111-o121-and-o145-and-virulence-genes-in-feces-hides-and-carcasses-of-pre-and-periharvest-cattle-worldwide/40F1FEF53A1824A68DC76B97C7DD7A4A)). Cattle are also natural hosts of *Mycobacterium bovis* ([Ramos et al., *Pathogens* 11:715, 2022](https://www.mdpi.com/2076-0817/11/7/715), doi:10.3390/pathogens11070715; [risk-factor review, PMC9150416](https://pmc.ncbi.nlm.nih.gov/articles/PMC9150416/)) and of the abortifacient zoonoses *Brucella abortus* and *Coxiella burnetii* ([multiplex assay paper, *Sci. Rep.* 13, 2023](https://www.nature.com/articles/s41598-023-39447-1), doi:10.1038/s41598-023-39447-1), and mastitis pathogens (*Staphylococcus*, *Streptococcus*, Corynebacteriaceae) dominate udder isolates (Derakhshani et al. 2018, above).

**Suggested differentia for the record's prose:** host taxon + foregut-fermenting ruminant anatomy is sufficient and defensible. The physicochemistry above belongs in a `rumen` record, not this one — it describes one compartment of the host, and quoting it here would over-narrow the whole-host concept to its most-studied part.

---

## 4. Sources

Grouped by what they support. All URLs retrieved 2026-08-17.

**The source vocabulary and the path**
- Reimer LC, et al. BacDive in 2019: bacterial phenotypic data for high-throughput biodiversity analysis. *Nucleic Acids Res.* 47(D1):D631–D636. doi:[10.1093/nar/gky879](https://academic.oup.com/nar/article/47/D1/D631/5106998) — MISO, three levels, eight top-level classes including `#Host`, `#Host body-site`, `#Host body-product`.
- Schober I, Koblitz J, Sardà Carbasse J, et al. BacDive in 2025: the core database for prokaryotic strain data. *Nucleic Acids Res.* 53(D1):D748–D756. doi:[10.1093/nar/gkae959](https://academic.oup.com/nar/article/53/D1/D748/7848838). PMID 39470737.
- BacDive isolation-source browser: [https://bacdive.dsmz.de/isolation-sources](https://bacdive.dsmz.de/isolation-sources) — confirms `#Host ▸ #Mammals ▸ Bovinae (Cow, Cattle)`.

**Ontology and standards**
- ENVO `ENVO:01001002` *animal-associated environment*; `ENVO:01001000`, `ENVO:01001001`, `ENVO:01001041`, `ENVO:01001179`, `ENVO:01001176`, `ENVO:01001055`, `ENVO:01001033`, `ENVO:01001034` — via [OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo).
- ENVO issue #1029, "EnvO terms for host-associated samples": [https://github.com/EnvironmentOntology/envo/issues/1029](https://github.com/EnvironmentOntology/envo/issues/1029).
- NCBI Taxonomy: [Bovinae, taxid 27592](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=27592); *Bos taurus*, taxid 9913.
- UBERON: `UBERON:0007365` rumen, `UBERON:0007364` reticulorumen, `UBERON:0007366` ruminant stomach, `UBERON:0010228` ruminal fluid.
- GSC MIxS: [HostAssociated extension `MIXS:0016002`](https://genomicsstandardsconsortium.github.io/mixs/0016002/); [`host_taxid` `MIXS:0000250`](https://genomicsstandardsconsortium.github.io/mixs/0000250/); [`specific_host` `MIXS:0000029`](https://genomicsstandardsconsortium.github.io/mixs/0000029/).

**Microbiology of the habitat**
- Huws SA, Creevey CJ, Oyama LB, et al. Addressing global ruminant agricultural challenges through understanding the rumen microbiome. *Front. Microbiol.* 9:2161, 2018. doi:[10.3389/fmicb.2018.02161](https://pmc.ncbi.nlm.nih.gov/articles/PMC6167468/). PMID 30319557.
- Seshadri R, Leahy SC, Attwood GT, et al. Cultivation and sequencing of rumen microbiome members from the Hungate1000 Collection. *Nat. Biotechnol.* 36:359–367, 2018. doi:[10.1038/nbt.4110](https://www.nature.com/articles/nbt.4110). PMID 29553575.
- Stewart RD, Auffret MD, Warr A, et al. Compendium of 4,941 rumen metagenome-assembled genomes. *Nat. Biotechnol.* 37:953–961, 2019. doi:[10.1038/s41587-019-0202-3](https://www.nature.com/articles/s41587-019-0202-3).
- Huang Y, et al. Redox potential: an intrinsic parameter of the rumen environment. *J. Anim. Physiol. Anim. Nutr.* 102:e100, 2018. doi:[10.1111/jpn.12855](https://onlinelibrary.wiley.com/doi/10.1111/jpn.12855). PMID 29352497.
- Marden JP, et al. A new device for measuring kinetics of ruminal pH and redox potential in dairy cattle. *J. Dairy Sci.* 88:277–281, 2005. doi:[10.3168/jds.S0022-0302(05)72685-0](https://www.sciencedirect.com/science/article/pii/S0022030205726850).
- Derakhshani H, et al. Invited review: microbiota of the bovine udder. *J. Dairy Sci.* 101:10605–10625, 2018. doi:[10.3168/jds.2018-14860](https://www.sciencedirect.com/science/article/pii/S0022030218309147). PMID 30292553.
- Holman DB, Gzyl KE. A meta-analysis of the bovine gastrointestinal tract microbiota. *FEMS Microbiol. Ecol.* 95:fiz072, 2019. doi:[10.1093/femsec/fiz072](https://academic.oup.com/femsec/article/95/6/fiz072/5497297).
- Lima SF, et al. The *Bos taurus* maternal microbiome. *PLoS ONE* 14:e0208014, 2019. doi:[10.1371/journal.pone.0208014](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0208014).
- Elder RO, et al. *E. coli* O157:H7 in beef cattle presented for slaughter. *PNAS* 97:2999–3003, 2000. doi:[10.1073/pnas.97.7.2959](https://www.pnas.org/doi/10.1073/pnas.97.7.2959).
- Ramos B, et al. Review on bovine tuberculosis. *Pathogens* 11:715, 2022. doi:[10.3390/pathogens11070715](https://www.mdpi.com/2076-0817/11/7/715).

**Scale**
- FAOSTAT live animal stocks, cattle, 2023: 1,575.8 million head — primary domain [FAOSTAT QCL](https://www.fao.org/faostat/en/#data/QCL); the figure as compiled is at [Statista](https://www.statista.com/statistics/263979/global-cattle-population-since-1990/). **Pull the number from FAOSTAT directly before citing it in the record** — I read it from a secondary compilation.

**Explicitly my inference, not sourced**
- That the "(Cow, Cattle)" gloss, not the head noun "Bovinae", reflects how the tag is actually used.
- That the 619-assertion volume is driven by cattle's economic scale and veterinary sampling.
- That the missing `mammal-associated environment` intermediate should be noted rather than blocked on.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**
cattle, cow, cows, bovine, bovine host, cattle host, domestic cattle, *Bos taurus*, *Bos indicus*, zebu, dairy cow, dairy cattle, beef cattle, calf, heifer, steer, bull, ox, bovine-associated, cattle-associated. (NCBI Taxonomy lists *bovine*, *cow*, *dairy cow*, *domestic cattle*, *domestic cow* and *ox* as exact synonyms of *Bos taurus*, `NCBITaxon:9913`.)

**Commonly but wrongly treated as the same thing**

| Not this | What it actually is |
|---|---|
| Rumen, rumen fluid, reticulorumen | A body site of the host (`UBERON:0007365`, `UBERON:0010228`). The most-sampled part, so most likely to be silently substituted for the whole. |
| Cow dung, cattle manure, slurry, dairy lagoon | Environmental materials outside the host (`ENVO:01001116`); a distinct microbial habitat with an aerobic/anoxic interface the rumen does not have. |
| Raw milk, colostrum, cheese, yoghurt | Body products and food materials — FOODON/`#Host body-product`, not `#Host`. |
| Beef, carcass, hide, leather | Post-slaughter materials (`FOODON:00001696`, `ENVO:02000053`). |
| Cow shed, byre, feedlot, drylot, pasture, rangeland | Built and managed settings around cattle (`ENVO:00003041`, `ENVO:01000627`, `ENVO:01000626`, `ENVO:00000266`, `ENVO:01000247`). |
| Bovine mastitis, bovine tuberculosis, bovine respiratory disease | Disease states — processes/conditions, not places. MISO puts these under `#Condition`/`#Medical`. |
| Water buffalo (*Bubalus*), bison, yak, African buffalo, nilgai, eland, saola | Other Bovinae genera. Included by the label's head noun, almost certainly not by the data. |
| "Ruminant" generally — sheep, goat, deer | Sibling host concepts sharing the foregut anatomy but not the host taxon. |
| Fetal bovine serum, bovine cell lines, bovine serum albumin | Laboratory reagents of bovine origin; a strain "isolated from FBS" is a contamination finding about a reagent, not a cattle habitat. |
| `NCBITaxon:27592` *Bovinae* / `NCBITaxon:9913` *Bos taurus* | A class of organisms. Belongs as `relation: xref`, never as identity or as a `parent_habitats` entry. |

---

## 6. Should it be a term at all?

**Yes — keep it as a habitat with its own minted identity, and treat the taxon as an xref.** The evidence supports the curator's recorded reasoning rather than the earlier `NOT_APPLICABLE`:

1. **It is a place where microbes live.** 619 upstream strain assertions, plus reference genome catalogs built explicitly on cattle as the sampling context (501 Hungate1000 genomes; 4,941 MAGs from 283 animals), plus an entire literature on site-specific bovine microbiotas. Nothing here is a process, quality, disease state or sampling artefact.
2. **The standards already model host-as-context.** MIxS provides a whole host-associated extension keyed on `host_taxid`, and its scope note uses a cow to draw the boundary. BacDive's MISO gives `#Host` a top-level class of its own, coordinate with `#Environmental`. Both treat the host organism as a legitimate environmental context for a sequenced or deposited strain.
3. **ENVO models the pattern and lacks the specific term.** `ENVO:01001002` *animal-associated environment* is the genus; `plant-associated`, `fungi-associated` and `cnidarian-associated` children show ENVO mints taxon-scoped subclasses of exactly this form. There is no cattle-, bovine-, ruminant-, mammal- or vertebrate-associated environment. So the concept is real, the genus exists, and the term does not — which is precisely HabitatMech's minting condition.
4. **The `NOT_APPLICABLE` was the stronger and wrong claim.** "Cattle are not a habitat" is contradicted by the corpus's own treatment of Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, and by ENVO's `animal-associated environment` branch. What is not a habitat is the *taxon term* — a subfamily is a class of organisms, not a place — which is handled by `relation: xref` per #99.

**Practical notes for the curator**

- Suggested term-request label: **`cattle-associated environment`**, genus `ENVO:01001002`. Prefer this over "Bovinae-associated environment"; see §1.
- Xrefs to carry: `NCBITaxon:9913` (*Bos taurus*) as the primary host taxon, `NCBITaxon:27592` (Bovinae) as the source label's literal scope, with a note that the two differ.
- **The record's category is `OTHER` but its source path is `#Host ▸ #Mammals`.** Worth checking whether the category assignment should be `host_associated`, consistent with the sibling records named in the decision note (Sponge, Nematoda, Reptilia, Mammals, Birds, Fish). That is a seeder/categorisation question, not a definition question, but it will look like an inconsistency in the published record if left as is.

## Citations

1. https://academic.oup.com/nar/article/47/D1/D631/5106998
2. https://bacdive.dsmz.de/isolation-sources
3. https://academic.oup.com/nar/article/53/D1/D748/7848838
4. https://www.nature.com/articles/nbt.4110
5. https://www.nature.com/articles/s41587-019-0202-3
6. https://academic.oup.com/femsec/article/95/6/fiz072/5497297
7. https://www.sciencedirect.com/science/article/pii/S0022030218309147
8. https://pubmed.ncbi.nlm.nih.gov/26392887/
9. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0208014
10. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12738856/
11. https://genomicsstandardsconsortium.github.io/mixs/0016002/
12. https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=27592
13. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002
14. https://github.com/EnvironmentOntology/envo/issues/1029
15. https://genomicsstandardsconsortium.github.io/mixs/0000250/
16. https://pmc.ncbi.nlm.nih.gov/articles/PMC6167468/
17. https://onlinelibrary.wiley.com/doi/10.1111/jpn.12855
18. https://www.sciencedirect.com/science/article/pii/S0022030205726850
19. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11055587/
20. https://www.statista.com/statistics/263979/global-cattle-population-since-1990/
21. https://www.fao.org/faostat/en/#data/QCL
22. https://www.pnas.org/doi/10.1073/pnas.97.7.2959
23. https://www.cambridge.org/core/journals/animal-health-research-reviews/article/systematic-review-and-metaanalysis-of-published-literature-on-prevalence-of-nono157-shiga-toxinproducing-escherichia-coli-serogroups-o26-o45-o103-o111-o121-and-o145-and-virulence-genes-in-feces-hides-and-carcasses-of-pre-and-periharvest-cattle-worldwide/40F1FEF53A1824A68DC76B97C7DD7A4A
24. https://www.mdpi.com/2076-0817/11/7/715
25. https://pmc.ncbi.nlm.nih.gov/articles/PMC9150416/
26. https://www.nature.com/articles/s41598-023-39447-1
27. https://www.ebi.ac.uk/ols4/ontologies/envo
28. https://genomicsstandardsconsortium.github.io/mixs/0000029/