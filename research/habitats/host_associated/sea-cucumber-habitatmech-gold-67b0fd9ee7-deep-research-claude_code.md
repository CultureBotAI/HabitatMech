---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T00:41:32.449019'
end_time: '2026-08-18T00:49:31.061532'
duration_seconds: 478.61
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Sea cucumber
  habitat_identifier: habitatmech:GOLD.67b0fd9ee7
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Invertebrates > Echinodermata > Sea cucumber'
  assertions: '17'
  parent_terms: (none)
  xrefs: FOODON:02022154
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term FOODON:02022154 'sea cucumber' attached as a parent. Organism-identity\
    \ screen (#109): grounded EXACT to FOODON:02022154 'sea cucumber', which is an\
    \ echinoderm \u2014 an organism, not a place. The screen that exists to catch\
    \ exactly this reported 0 for months because it tested only NCIT and mesh ancestry\
    \ and only the record's identity; widening it to UBERON:0000468 and to parent_habitats\
    \ surfaced this family. The GOLD path says host-associated, so the concept is\
    \ the environment the organism provides, which is the same family as the sponge,\
    \ nematode and reptile term requests. The organism term is kept as an xref (#99)\
    \ rather than an identity. (source concept habitatmech:GOLD.67b0fd9ee7)"
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
  web_search_requests: 12
  num_turns: 36
  total_cost_usd: 3.197369
  session_id: 1ba40ed9-7906-46ac-bea0-61a11837a85d
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 29
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Sea cucumber
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.67b0fd9ee7
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Invertebrates > Echinodermata > Sea cucumber
- **Upstream assertion volume:** 17
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** FOODON:02022154

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term FOODON:02022154 'sea cucumber' attached as a parent. Organism-identity screen (#109): grounded EXACT to FOODON:02022154 'sea cucumber', which is an echinoderm — an organism, not a place. The screen that exists to catch exactly this reported 0 for months because it tested only NCIT and mesh ancestry and only the record's identity; widening it to UBERON:0000468 and to parent_habitats surfaced this family. The GOLD path says host-associated, so the concept is the environment the organism provides, which is the same family as the sponge, nematode and reptile term requests. The organism term is kept as an xref (#99) rather than an identity. (source concept habitatmech:GOLD.67b0fd9ee7)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Sea cucumber** as a microbial habitat, with citations.

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

# Sea cucumber — `habitatmech:GOLD.67b0fd9ee7`

## Proposed definition

> An animal-associated environment which is determined by a living sea cucumber (Holothuroidea), in which microorganisms inhabit the compartments the host provides — principally the sediment-processing digestive tract and its digesta, the coelomic fluid, and the body-wall surface.

ENVO house-style variant, matching the phrasing ENVO used for the one existing host-clade sibling `ENVO:01001179` *cnidarian-associated environment* ("An environmental system determined by a cnidarian or part of a cnidarian"), if the term request is written for ENVO rather than for HabitatMech:

> An environmental system determined by a sea cucumber or part of a sea cucumber.

**Three structural findings up front, because they change what the curator should do:**

1. **ENVO already reaches partway into this concept, and only into this one.** `ENVO:01001187` *holothurian digestive tract* and `ENVO:01001188` *holothurian digestive tract contents* both exist, both are **already in this repo's vendored slice** (`data/raw/ontology_terms.tsv` lines 8681–8682), and `ENVO:01001187` carries the exact synonyms *sea cucumber digestive tract* and *sea cucumber gut*. No comparable term exists for the sibling records `Sea Urchin` or `Sea Star`. This is the strongest possible evidence that the concept family is in ENVO's scope — and it is still **not a match** for this record (§2).
2. **The near-miss is narrower, not broader — so it cannot go in `parent_habitats`.** `ENVO:01001187` is scoped to one organ; this record is whole-host, with 17 `ORGANISM`-unit assertions and no compartment breakdown recorded upstream. Attaching a narrower term as a parent is the same class of over-claim `#99` was filed about, run in the opposite direction. It belongs in `relation: xref`.
3. **This is not the Porifera/Sponge situation.** `Sea cucumber` (17 organisms) is a genuine proper subset of its parent `Echinodermata` (21 organisms), with two attested siblings — `Sea Urchin` (53) and `Sea Star` (16). It warrants its own term, not a `SAME_AS` merge. (Counts from `data/raw/gold_ecosystem_paths.tsv` lines 300/409/446/455; repo data, not literature.)

---

## 1. What the concept denotes

### The reading the data means

GOLD's path is `Ecosystem = Host-associated → Ecosystem Category = Invertebrates → Ecosystem Type = Echinodermata → Ecosystem Subtype = Sea cucumber`. GOLD's five-level scheme is `Ecosystem → Ecosystem Category → Ecosystem Type → Ecosystem Subtype → Specific Ecosystem`, describing "the environment from which an environmental sample or an organism was collected" ([JGI GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification); [Mukherjee et al. 2023, *NAR* 51:D957–D963](https://doi.org/10.1093/nar/gkac974)). The `Host-associated` root fixes the frame: the place is the host body, not the seawater or seabed around it. The Ecosystem Type level is the host phylum; the Subtype level narrows it to one of its classes by vernacular name.

So **"Sea cucumber" denotes the body of a living holothuroid animal, sampled as the place a microbial community lives** — a piece of gut wall, gut content, coelomic fluid, body wall or faeces, from which DNA is extracted or from which a strain is isolated. All 17 upstream assertions are `assertion_unit: ORGANISM` (isolate/genome records attributed to this node), with no compartment breakdown recorded upstream, so the record must cover the whole host, not any one organ.

### The compartments inside the concept

The holothurian body is not one habitat but several, and the literature treats them as such. A culture-based review lists isolation from "the body wall, body surface, inner body tissue, coelomic fluid, stomach, intestines, brown gastrointestinal tissue, and feces" ([Chen et al. 2021, *Mar Drugs* 19:461](https://doi.org/10.3390/md19080461)).

| Compartment | What it is | Evidence |
|---|---|---|
| **Digestive tract wall and lumen** | The best-characterised compartment; strongly regionalised along the tract | In *Holothuria glaberrima*, anterior intestine = Proteobacteria 61% / Bacteroidetes 22%; medial = *Vibrio* 64%; posterior = **Firmicutes 48% / Bacteroidetes 35%, Proteobacteria only 7%** ([Pagán-Jiménez et al. 2019, *PLoS ONE* 14:e0208011](https://doi.org/10.1371/journal.pone.0208011)) |
| **Gut digesta (ingested sediment in transit)** | Selectively filtered sediment, not sediment | 188,623 reads / 15,527 OTUs across foregut, hindgut and ambient sediment of *A. japonicus*; richness and Shannon diversity both **higher in sediment than in gut** ([Gao et al. 2014, *PLoS ONE* 9:e100092](https://doi.org/10.1371/journal.pone.0100092)) |
| **Coelomic fluid** | An internal liquid compartment, once assumed sterile; it is not | Unique bacteria in holothurian coelomic fluid, incl. Epsilonproteobacteria and Rickettsiales ([Enomoto, Nakagawa & Sawabe 2012, *Microbes Environ* 27:300–305](https://doi.org/10.1264/jsme2.ME12020)); in *Holothuria forskali*, 3.9 × 10⁴ CFU mL⁻¹ and Proteobacteria 61.8% mean abundance ([Laguerre et al. 2025, *Biology* 14:430](https://doi.org/10.3390/biology14040430)) |
| **Body wall / external surface** | The epidermal interface with sediment and water | Isolation source in [Chen et al. 2021](https://doi.org/10.3390/md19080461); the tissue that fails in skin ulceration syndrome (below) |
| **Respiratory tree and cloaca** | A water-filled internal cavity flushed with ambient seawater through the cloaca | Tracer work found microfibres attached to **all** undigested respiratory trees examined and in the coelomic fluid of 100% of exposed *H. cinerascens* ([Mohsen et al. 2021, *Environ Pollut* 273:115463](https://doi.org/10.1016/j.envpol.2020.115463)) — direct evidence the cavity is open to environmental particles |
| **Faeces / egested pellets** | Sampled as a proxy for the gut community | ([Yamazaki et al. 2016, *Sci Rep* 6:21631](https://doi.org/10.1038/srep21631)) |
| **Regenerating gut** | A transient state of the same compartment, experimentally accessible because holothurians eviscerate and regrow the tract | ([Weigel 2020, *Appl Environ Microbiol* 86:e00489-20](https://doi.org/10.1128/AEM.00489-20)) |

**Salinity is safely in the definition.** Echinoderms are exclusively marine; there are no freshwater or terrestrial holothurians ([Animal Diversity Web, Holothuroidea](https://animaldiversity.org/accounts/Holothuroidea/)). Depth is *not* restrictive and should not be written in: attested hosts run from shallow reef flats (most sampling is at <20 m — [Chen et al. 2021](https://doi.org/10.3390/md19080461)) through abyssal species ([Roberts et al. 2001, *Prog Oceanogr* 50:443–458](https://doi.org/10.1016/S0079-6611(01)00065-9)) to cold-seep holothurians with chemosynthetic gut symbionts ([Marine Life Science & Technology 2026](https://doi.org/10.1007/s42995-026-00368-3)).

### The boundary: what is inside, what is next door

**Inside:** gut wall, gut contents and faeces; coelomic fluid and coelomocytes; body wall and external surface; respiratory tree and cloacal cavity; regenerating tissue post-evisceration; wild, aquaculture-held, healthy and diseased animals; all orders of Holothuroidea, shallow to abyssal.

| Neighbour | Why it is outside |
|---|---|
| **Ambient marine sediment** | The routine reference environment, sampled precisely *because* it differs — and it demonstrably does (§3b). Once faecal pellets are voided they become sediment/detritus. |
| **Sediment reworked by sea cucumber grazing** | A seafloor state *shaped by* holothurians, not a place that *is* one. Grazing cut sediment 16S rRNA gene abundance by ~75% in French Polynesian reefs ([Loeffler et al. 2025, PMC12201990](https://pmc.ncbi.nlm.nih.gov/articles/PMC12201990/)); removal increases coral disease ([Shaver et al. 2024, *Nat Commun* 15:1338](https://doi.org/10.1038/s41467-024-45730-0)). ENVO has no term for this either — a separate, real gap. |
| **Sea cucumber aquaculture pond water/sediment** | An engineered aquatic habitat, not the host body. |
| **`Sea Urchin` `habitatmech:GOLD.b19422ad27`, `Sea Star`** | Sibling GOLD nodes; different echinoderm classes. |
| **`Echinodermata` `habitatmech:GOLD.e1f435d44b`** | The parent record, and genuinely broader — three attested children. |
| **`FOODON:02022154` sea cucumber (the current xref) and bêche-de-mer / trepang** | The food-commodity reading of the string. §5. |
| **Pearlfish (Carapidae) inhabiting the cloaca** | A metazoan inquiline. It confirms the cloacal cavity is an inhabitable space but is not itself a microbial-habitat concept. |

### Ambiguity in the label

The bare string "sea cucumber" has two live readings: (i) the living holothuroid as a host organism; (ii) the seafood commodity — dried *bêche-de-mer*/*trepang*, which is FOODON's reading and the reading behind `FOODON:03310117` *sea cucumber (salted)* and `FOODON:03542572` *Sea-cucumbers (EFSA FoodEx2)*. **The GOLD path `Host-associated > Invertebrates > Echinodermata > Sea cucumber` settles it unambiguously on (i).** A processed, salted, dried commodity is not a `Host-associated` environment.

A narrower ambiguity does *not* arise here, unlike the sea urchin case: the vernacular "sea cucumber" and the class Holothuroidea coincide closely enough that no attested sub-group is excluded. **Recommendation: scope the term to class Holothuroidea and say so.**

---

## 2. Genus — the broader kind

**Recommended genus: `ENVO:01001002` *animal-associated environment*** — "An environmental system determined by an animal" (synonyms *Metazoan-associated environment*, *animal environment*). **It is in this repo's vendored slice with exactly that label** (`data/raw/ontology_terms.tsv:8497`), so a `GROUND_AS_PARENT` decision naming it passes the slice-and-label check.

The modelling precedent is `ENVO:01001179` *cnidarian-associated environment* (also in slice, line 8673): ENVO already accepts a host clade as an environment class under *animal-associated environment*. **A holothurian-associated environment would be its sibling.**

### Near-misses, and why each fails

| Term | Verified content | Verdict |
|---|---|---|
| `ENVO:01001187` **holothurian digestive tract** *(in slice, line 8681)* | "A digestive tract environment which has its properties and dynamics determined by the digestive tract of an echinoderm from the class Holothuroidea." Synonyms: *sea cucumber digestive tract*, *sea cucumber gut*. ([OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001187)) | **The single closest term in any ontology — and still narrower.** Right host class, wrong scope: one organ versus a whole host whose attested sampling also covers coelomic fluid, body wall and faeces. Grounding here would silently assert all 17 GOLD organisms came from gut. **Record as `relation: xref`, not `parent`** — it is narrower than the concept, so `parent_habitats` would be false (repo rule on *broader*). It is also the natural target for a future `Sea cucumber > Gut` child record, should GOLD add one. |
| `ENVO:01001188` **holothurian digestive tract contents** *(in slice, line 8682)* | "A bodily fluid which is present in the digestive tract of a member of the Holothuroidea." | Narrower still, and typed as a *fluid* (a material entity) rather than an environment. Same disposition: xref at most. |
| `ENVO:01001176` **environment associated with an aquatic invertebrate** *(in slice, line 8670)* | "An environment which has its properties and composition largely determined by the presence of a metazoan which lacks a vetebral column and which has a habitat that is found in an aquatic environmental system." | **True of holothurians but broader, and structurally awkward.** It sits under `ENVO:01001055` *environment associated with an animal part or small animal*, importing a "part or small animal" implication that a 1 m *Synapta maculata* does not satisfy. ENVO did not route *cnidarian-associated environment* through it. Recommend against as genus; record as near-miss. |
| `ENVO:01001055` **environment associated with an animal part or small animal** *(in slice, line 8550)* | "An environmental system determined by part of a living or dead animal, or a whole small animal." | Same over-claim; and the whole host, not a part, is what is denoted. |
| `FOODON:02022154` **sea cucumber** *(current xref, in slice, line 10630)* | Definition on the term is simply "A whole sea cucumber." | **An organism/food-source term, not a place** — exactly what the `#109` organism-identity screen exists to catch. Keeping it as `relation: xref` per `#99` is correct. Note the record's own curation note says it was "attached as a parent"; the record as written correctly carries it under `xrefs`, so the discrepancy is in the note text only and should not be re-litigated. |
| `FOODON:03412115` **echinoderm**, `FOODON:03310117` **sea cucumber (salted)**, `FOODON:03542570/03542572` **sea-cucumbers (ISSCAAP/EFSA FoodEx2)** | Food-source and food-commodity classes. | The commodity reading. `FOODON:03412115` is also phylum-level, hence broader. |
| `NCBITaxon:7705` **Holothuroidea** | Taxon. **Not in the vendored slice** (only `NCBITaxon:7586` Echinodermata is, line 10762). | A class of organisms, not a place. Per repo policy (`#99`, `#114`): xref only, never grounding, never `parent_habitats`. If a taxon xref is wanted and must come from the slice, `NCBITaxon:7586` is the only available one and is broader than the concept. |
| `NCBITaxon:2798575` **sea cucumber metagenome** | A metagenome taxon placeholder. | Names a sequence collection, not a habitat. Do not use. |
| **UBERON** | OLS4 search returns no holothurian-specific classes; `UBERON:0001555` *digestive tract* is the generic organ. | A *part*, not the host. Under the repo's part-versus-whole rule this would ground a hypothetical `Sea cucumber > Gut` child, not this record. |
| **BTO** | `BTO:0001708` coelomic fluid, `BTO:0002856` coelomocyte are generic echinoderm/invertebrate parts. | None names this concept. |
| **ENVO, whole-ontology search for "sea cucumber" / "holothurian"** | Only `ENVO:01001187` and `ENVO:01001188`; both organ-scoped ([OLS4 ENVO search](https://www.ebi.ac.uk/ols4/index)). | **No existing ENVO term names the whole-host concept.** |

**Conclusion: `CONFIRM_UNGROUNDED` is correct and should stand.** Recommended additions: `GROUND_AS_PARENT` on `ENVO:01001002` *animal-associated environment* (the record currently carries no ontology parent at all — only the HabitatMech `Echinodermata` record), and `relation: xref` on `ENVO:01001187`. The term request — *holothurian-associated environment* / *sea cucumber-associated environment* — is well founded, and unusually easy to argue to ENVO because ENVO has already minted two Holothuroidea-scoped environment classes and only needs the whole-host parent that would sit above them.

---

## 3. Differentia — what distinguishes it from its siblings

Ordered by how observable and how load-bearing each is. Any one of the first two carries the definition sentence; the rest belong in the term-request comment.

**(a) The host is a deposit-feeding holothuroid — a soft-bodied, benthic, exclusively marine animal that eats the sediment it lives on, with a complete through-gut.** This is the decisive contrast with the two nearest modelled host-clade environments: a **sponge** is a sessile filter pump with no gut, and a **cnidarian** has a blind gastrovascular cavity; the holothurian has a mouth and an anus and therefore a true directional gut-lumen habitat. It also contrasts with its own sibling **sea urchin**, whose regular forms are algal grazers with a rigid calcite test and Aristotle's lantern. Deposit-feeding is the defining ecological role: bioturbation and sediment reworking by tropical holothuroids influences grain size, microalgal productivity, nutrient cycling, oxygen profiles and benthic biogeochemistry ([Purcell et al. 2023, in *The World of Sea Cucumbers*, ch. 28](https://doi.org/10.1016/B978-0-323-95377-1.00028-X); [Animal Diversity Web, Holothuroidea](https://animaldiversity.org/accounts/Holothuroidea/)).

**(b) The gut is a selective filter, not a sediment sample — the single best-supported differentia, and what makes the concept a habitat rather than a sampling artefact.** This claim is hard to make for a deposit feeder and is nonetheless well supported:
- In *A. japonicus*, bacterial richness and Shannon diversity were both significantly **higher in ambient sediment than in gut contents** ([Gao et al. 2014](https://doi.org/10.1371/journal.pone.0100092)).
- Across three tropical species (*Holothuria atra*, *Stichopus chloronotus*, *S. monotuberculatus*), gut-content OTU counts were ~1,600–2,500 against ~4,200 in the sediments they ingest ([Wang et al. 2023, *Diversity* 15:855](https://doi.org/10.3390/d15070855)).
- In *H. atra* and *H. leucospilota*, 66.2% of 5,584 OTUs were shared between gut contents and surrounding sediment, yet sediment richness and diversity remained significantly higher ([*J Oceanol Limnol* 2021](https://doi.org/10.1007/s00343-021-1001-5)).
- The strongest single test: after induced evisceration, *Sclerodactyla briareus* regrew its gut in a common tank and the community reassembled **deterministically** — regenerating stomach and intestine communities were distinct from both seawater and sediment and highly similar across replicates, despite immersion in a diverse environmental pool ([Weigel 2020](https://doi.org/10.1128/AEM.00489-20)). Host selection, not passive sediment carry-over.

**(c) The gut community is functionally required by the host, and is co-adapted to a sediment diet.** Whole-genome and enzyme work on *Holothuria leucospilota* found an expansion of digestive carbohydrase genes and contraction of digestive protease genes, and a **dual role for gut bacteria: some supply the digestive enzymes the host genome lacks, while others are themselves digested as assimilable nutrients** — mediated in part by Holothuroidea-specific intestinal i-type lysozymes ([Pan et al. 2024, *Nat Commun* 15:8825](https://doi.org/10.1038/s41467-024-53205-5)). Cellulase activity in particular is attributed to gut genera rather than the host genome.

**(d) The tract is longitudinally zoned, so "the gut" is several habitats.** The near-total turnover between medial intestine (*Vibrio* 64%, Proteobacteria-dominated) and posterior intestine (Firmicutes 48%, Bacteroidetes 35%, Proteobacteria 7%) in *H. glaberrima* is a stronger gradient than most animal guts show ([Pagán-Jiménez et al. 2019](https://doi.org/10.1371/journal.pone.0208011)); fatty-acid composition changes measurably between ambient sediment, foregut, midgut, hindgut and faecal pellets ([Wen et al. 2016, *J Lipids* 2016:4579794](https://doi.org/10.1155/2016/4579794)); and gut sediment distribution and enzyme profiles differ significantly among abyssal species ([Roberts et al. 2001](https://doi.org/10.1016/S0079-6611(01)00065-9)).

**(e) A populated internal liquid compartment — coelomic fluid — that is the immune interface.** Holothurians carry the richest coelomic microbiota of the three echinoderm classes compared side by side from one site: *H. forskali* at 3.9 × 10⁴ CFU mL⁻¹ against 1.0 × 10³ for the sea star *Marthasterias glacialis* and 4.9 × 10¹ for the sea urchin *Sphaerechinus granularis*, with a per-host core microbiota varying over time and 20 antibacterial isolates recovered, mostly from the sea cucumber ([Laguerre et al. 2025](https://doi.org/10.3390/biology14040430)); unique Epsilonproteobacteria and Rickettsiales were reported here first ([Enomoto et al. 2012](https://doi.org/10.1264/jsme2.ME12020)).

**(f) The host regenerates the habitat, which is an experimentally distinctive property.** Evisceration followed by rapid gut regeneration decouples host ontogeny from gut-tissue development and permits experimental manipulation of the gut microbiome in mature animals ([Weigel 2020](https://doi.org/10.1128/AEM.00489-20)); intestinal microbiota composition differs significantly across regeneration stages in *A. japonicus*, with only 14 OTUs shared across all stages ([Zhang et al. 2019, *Front Microbiol* 10:1165](https://doi.org/10.3389/fmicb.2019.01165)).

**(g) Aquaculture and disease give the concept practical weight.** *A. japonicus* is the dominant study species (~41% of sampled animals in the culturable-microorganism review — [Chen et al. 2021](https://doi.org/10.3390/md19080461)), and skin ulceration syndrome, with *Vibrio splendidus* as a principal pathogen, causes mortality reported up to 90–100% in culture ([Zhang et al. 2016, *Sci Rep*, PMC4906609](https://pmc.ncbi.nlm.nih.gov/articles/PMC4906609/)). Diseased and probiotic-treated animals are part of the attested habitat, not a separate concept.

---

## 4. Sources — and what is inference rather than sourced

### Primary literature

- [Pan W, Wang X, Ren C, et al. (2024) *Nat Commun* 15:8825](https://doi.org/10.1038/s41467-024-53205-5) — genomic/enzymatic basis of deposit feeding; dual role of gut microbes. PMID [39394205](https://pubmed.ncbi.nlm.nih.gov/39394205/).
- [Pagán-Jiménez M, Ruiz-Calderón JF, Dominguez-Bello MG, García-Arrarás JE (2019) *PLoS ONE* 14:e0208011](https://doi.org/10.1371/journal.pone.0208011) — regional gut microbiota of *H. glaberrima*; wild vs aquarium.
- [Weigel BL (2020) *Appl Environ Microbiol* 86:e00489-20](https://doi.org/10.1128/AEM.00489-20) — deterministic assembly after evisceration; distinct from seawater and sediment.
- [Gao F, Li F, Tan J, Yan J, Sun H (2014) *PLoS ONE* 9:e100092](https://doi.org/10.1371/journal.pone.0100092) — gut content vs ambient sediment, *A. japonicus*.
- [Laguerre H, Noël C, Jégou C, Fleury Y, Le Chevalier P (2025) *Biology* 14:430](https://doi.org/10.3390/biology14040430) — coelomic microbiota of *H. forskali* vs sea star vs sea urchin.
- [Enomoto M, Nakagawa S, Sawabe T (2012) *Microbes Environ* 27:300–305](https://doi.org/10.1264/jsme2.ME12020) — unique bacteria in holothurian coelomic fluid. PMID 22446312.
- [Chen L, Wang X-Y, Liu R-Z, Wang G-Y (2021) *Mar Drugs* 19:461](https://doi.org/10.3390/md19080461) — culturable microorganisms by body compartment; sampling depth and species coverage.
- [Wang et al. (2023) *Diversity* 15:855](https://doi.org/10.3390/d15070855) — three tropical species, gut vs sediment OTU counts.
- [*J Oceanol Limnol* (2021) 39:2188–2201](https://doi.org/10.1007/s00343-021-1001-5) — *H. atra* / *H. leucospilota* gut vs ambient sediment.
- [Zhang et al. (2019) *Front Microbiol* 10:1165](https://doi.org/10.3389/fmicb.2019.01165) — regenerating intestine microbiome; SRA PRJNA512056, PRJNA518164.
- [Yamazaki Y, et al. (2016) *Sci Rep* 6:21631](https://doi.org/10.1038/srep21631) — individual faecal microbiome and host growth; PHB producers.
- [Wen J, et al. (2016) *J Lipids* 2016:4579794](https://doi.org/10.1155/2016/4579794) — fatty-acid change along the gut of deposit-feeding holothurians.
- [Roberts D, et al. (2001) *Prog Oceanogr* 50:443–458](https://doi.org/10.1016/S0079-6611(01)00065-9) — abyssal holothurian gut compartments, enzymes, bacterial activity.
- [Mohsen M, et al. (2021) *Environ Pollut* 273:115463](https://doi.org/10.1016/j.envpol.2020.115463) — microplastic uptake routes via gut, respiratory tree and coelomic fluid.
- [Shaver EC, et al. (2024) *Nat Commun* 15:1338](https://doi.org/10.1038/s41467-024-45730-0) — removal of detritivore sea cucumbers increases coral disease.
- [Loeffler Z, et al. (2025) PMC12201990](https://pmc.ncbi.nlm.nih.gov/articles/PMC12201990/) — grazing reduces sediment 16S abundance ~75%; anaerobic metabolism enrichment.
- [*Mar Life Sci Technol* (2026)](https://doi.org/10.1007/s42995-026-00368-3) — specialised gut symbionts of the cold-seep holothurian *Chiridota hydrothermica*; 145 MAGs across 35 phyla.
- [Zhang P, et al. (2016) *Sci Rep*, PMC4906609](https://pmc.ncbi.nlm.nih.gov/articles/PMC4906609/) — skin ulceration syndrome transcriptome; mortality and pathogen context.

### Ontology and standards sources (all verified live against OLS4 and against `data/raw/ontology_terms.tsv`)

- `ENVO:01001187` *holothurian digestive tract* — [OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001187); slice line 8681.
- `ENVO:01001188` *holothurian digestive tract contents* — slice line 8682.
- `ENVO:01001002` *animal-associated environment* — slice line 8497.
- `ENVO:01001179` *cnidarian-associated environment* — slice line 8673.
- `ENVO:01001176`, `ENVO:01001055` — slice lines 8670, 8550.
- `FOODON:02022154` *sea cucumber* ("A whole sea cucumber") — slice line 10630.
- `NCBITaxon:7705` Holothuroidea — [OLS4](https://www.ebi.ac.uk/ols4/); **absent from the vendored slice**.
- [JGI GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification) and [ecosystem tree](https://gold.jgi.doe.gov/ecosystemtree); [Mukherjee et al. 2023, *NAR* 51:D957](https://doi.org/10.1093/nar/gkac974).
- [WoRMS, Holothuroidea AphiaID 123083](https://www.marinespecies.org/aphia.php?p=taxdetails&id=123083) — authoritative species list.
- [Animal Diversity Web, Holothuroidea](https://animaldiversity.org/accounts/Holothuroidea/) — ~1,100 described extant species, benthic, detritivorous, marine-only. Note: species counts vary by source; [Chen et al. 2021](https://doi.org/10.3390/md19080461) says ~1,500. **Do not put a species count in the definition.**

### What is inference, not a sourced claim

- **That the whole-host concept is the right scope for this record** is inference from the GOLD path plus `assertion_unit: ORGANISM` in `data/raw/gold_ecosystem_paths.tsv` — no source states it.
- **That `ENVO:01001187` is narrower than this record rather than equivalent** is my reading of its definition text against the record's scope. It is a strong reading, but it is a reading.
- **That the respiratory tree is a microbial habitat** is inferred from the microfibre tracer result plus its open connection to seawater via the cloaca. I found **no study profiling the respiratory-tree microbiome directly**. Do not assert it in the definition; the phrase "principally the digestive tract…, the coelomic fluid, and the body-wall surface" deliberately omits it.
- **That the body-wall/epidermal surface carries a characterised community** rests on it being an isolation source in [Chen et al. 2021](https://doi.org/10.3390/md19080461) and on the SUS literature. I found no dedicated amplicon survey of holothurian body-wall surface as a distinct compartment comparable to the sea-urchin spine work. It is safe to name as a sampled compartment; it is not safe to characterise its composition.
- **Contrasts with sponge and cnidarian body plans** are standard invertebrate zoology, cited here to ADW rather than to a specialist source.

---

## 5. Synonyms, and what not to conflate

### Names in real use for this concept

- **sea cucumber** (GOLD's spelling; note GOLD lowercases the noun here while capitalising `Sea Urchin` and `Sea Star` — a source inconsistency, not a semantic one)
- **holothurian**, **holothuroid** — the standard scientific vernacular; both appear in ENVO term labels and in the primary literature
- **Holothuroidea-associated environment**, **sea cucumber-associated environment**, **holothurian-associated environment** — the shapes a term request should take
- **sea cucumber holobiont** — the literature's framing of host-plus-microbiota ([*Curr Microbiol* 2026](https://doi.org/10.1007/s00284-026-04888-0))
- Compartment names in real use: **sea cucumber gut**, **sea cucumber digestive tract** (ENVO synonyms of `ENVO:01001187`), **coelomic fluid**

### Commonly but wrongly treated as the same thing

| Not the same | Why |
|---|---|
| **`ENVO:01001187` holothurian digestive tract** | One organ, not the host. It is the most likely wrong grounding a curator would reach for, precisely because its synonym is literally "sea cucumber gut". |
| **`FOODON:02022154` sea cucumber / `FOODON:03310117` salted sea cucumber / bêche-de-mer, trepang, hai shen** | The dried, salted, processed food commodity. A different entity class entirely, and the reason the `#109` screen fired on this record. |
| **`NCBITaxon:7705` Holothuroidea** | A taxon — a class of organisms, not a place. xref only, per `#99`. |
| **`NCBITaxon:2798575` sea cucumber metagenome** | A sequence-collection placeholder taxon. |
| **Ambient marine sediment / reef sediment** | The reference environment. Empirically higher-diversity and compositionally distinct in every study above. Conflating them erases the finding that the gut is a filter. |
| **Sea-cucumber-grazed sediment** | A seafloor state shaped by the animal. A real gap, but a *different* term. |
| **Sea cucumber aquaculture pond** | Engineered aquatic, not host-associated. |
| **Sea star, sea urchin, brittle star** | Sibling echinoderm classes with measurably different microbiota, including a two-to-three-order-of-magnitude difference in coelomic bacterial load ([Laguerre et al. 2025](https://doi.org/10.3390/biology14040430)). |
| **"Sea cucumber" as a marine cucumber-shaped alga or as *Cucumaria* the genus** | Occasional colloquial slippage; not attested in this data. |

---

## 6. Should it be a term at all?

**Yes.** It clears every test the repo applies:

- **It is a place, not an organism-as-taxon.** The claim is not "Holothuroidea is a habitat" (it is not — a class of organisms is not a place); the claim is that a living holothuroid *provides* an environment that microbes inhabit. That is exactly the distinction `#114` was filed to fix, and exactly what ENVO already models at `ENVO:01001002`, at `ENVO:01001179`, and — decisively for this record — at `ENVO:01001187`, which is a Holothuroidea-scoped *environment* class. The taxon stays an xref.
- **It is not a process, quality, disease or procedure**, so `NOT_APPLICABLE` would be a false and stronger claim.
- **It is not a sampling artefact.** The [Weigel 2020](https://doi.org/10.1128/AEM.00489-20) regeneration result and the consistent gut-versus-sediment diversity gap establish host selection independently of how the sample was taken.
- **It is a proper subset of its parent with attested siblings**, so it is not a vernacular restatement (contrast the Sponge/Porifera case) and should not be merged.

### Recommended disposition

| Field | Value | Rationale |
|---|---|---|
| `grounding_status` | **`UNGROUNDED` — unchanged** | No ontology term names the whole-host concept. `CONFIRM_UNGROUNDED` stands. |
| `parent_habitats` | **add `ENVO:01001002` *animal-associated environment*** via `GROUND_AS_PARENT` | Genuinely broader; in the vendored slice with a matching label; the record currently has no ontology parent at all. |
| `xrefs` | keep `FOODON:02022154`; **add `ENVO:01001187`** (and optionally `ENVO:01001188`) with `relation: xref` | Both are narrower or non-environmental; `xref` records the link without asserting identity or is-a. **Do not put `ENVO:01001187` in `parent_habitats`** — it is narrower, and that would be the same over-claim as `#99` in reverse. |
| Term request | **holothurian-associated environment** (label), definition as proposed above, parent `ENVO:01001002`, sibling of `ENVO:01001179` | The strongest of the echinoderm family's three requests: ENVO has already minted two Holothuroidea environment classes and this request supplies the whole-host parent they currently lack. Worth filing to ENVO alongside the sea urchin and sea star requests as one coordinated set. |

**Sources:** as listed in §4; ontology assertions additionally verified against [EBI OLS4](https://www.ebi.ac.uk/ols4/) and this repo's `data/raw/ontology_terms.tsv` and `data/raw/gold_ecosystem_paths.tsv`.

## Citations

1. https://gold.jgi.doe.gov/ecosystem_classification
2. https://doi.org/10.1093/nar/gkac974
3. https://doi.org/10.3390/md19080461
4. https://doi.org/10.1371/journal.pone.0208011
5. https://doi.org/10.1371/journal.pone.0100092
6. https://doi.org/10.1264/jsme2.ME12020
7. https://doi.org/10.3390/biology14040430
8. https://doi.org/10.1016/j.envpol.2020.115463
9. https://doi.org/10.1038/srep21631
10. https://doi.org/10.1128/AEM.00489-20
11. https://animaldiversity.org/accounts/Holothuroidea/
12. https://doi.org/10.1016/S0079-6611(01
13. https://doi.org/10.1007/s42995-026-00368-3
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC12201990/
15. https://doi.org/10.1038/s41467-024-45730-0
16. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001187
17. https://www.ebi.ac.uk/ols4/index
18. https://doi.org/10.1016/B978-0-323-95377-1.00028-X
19. https://doi.org/10.3390/d15070855
20. https://doi.org/10.1007/s00343-021-1001-5
21. https://doi.org/10.1038/s41467-024-53205-5
22. https://doi.org/10.1155/2016/4579794
23. https://doi.org/10.3389/fmicb.2019.01165
24. https://pmc.ncbi.nlm.nih.gov/articles/PMC4906609/
25. https://pubmed.ncbi.nlm.nih.gov/39394205/
26. https://www.ebi.ac.uk/ols4/
27. https://gold.jgi.doe.gov/ecosystemtree
28. https://www.marinespecies.org/aphia.php?p=taxdetails&id=123083
29. https://doi.org/10.1007/s00284-026-04888-0