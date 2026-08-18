---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T22:23:26.900458'
end_time: '2026-08-17T22:31:01.592396'
duration_seconds: 454.69
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Amphibia
  habitat_identifier: habitatmech:GOLD.0cd585a031
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Amphibia'
  assertions: '41'
  parent_terms: ENVO:01001000
  xrefs: NCBITaxon:8292
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term NCBITaxon:8292 'Amphibia' attached as a parent. Host-taxon reversal\
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
    \ not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.0cd585a031)"
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
  web_search_requests: 20
  num_turns: 28
  total_cost_usd: 3.4509499999999993
  session_id: 9c2bdbeb-23d8-4c39-bac9-418bacb21a07
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 34
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Amphibia
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.0cd585a031
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Amphibia
- **Upstream assertion volume:** 41
- **Nearest broader term already on the record:** ENVO:01001000
- **Cross-references upstream suggested:** NCBITaxon:8292

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term NCBITaxon:8292 'Amphibia' attached as a parent. Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it — the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE while its own child Porifera > Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM — a phylum is a class of organisms, not a place — so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.0cd585a031)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Amphibia** as a microbial habitat, with citations.

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

> **Proposed definition:** An animal-associated environment which is determined by an amphibian — an ectothermic, typically biphasic tetrapod vertebrate of class Amphibia — and which comprises the host's mucus-covered, scaleless and highly permeable integument together with its internal organ and gut surfaces.

Genus: `ENVO:01001002` *animal-associated environment*. Differentia: determined by a host of class Amphibia, whose defining habitat-relevant property is a lightly keratinised, glandular, water- and gas-permeable skin in continuous exchange with the surrounding aquatic or moist terrestrial environment, plus a life cycle that reorganises the internal habitat at metamorphosis.

---

## 1. What the concept denotes

**The reading the data means.** The source path is `Host-associated > Amphibia`, GOLD's second-level *Ecosystem Category* under the `Host-associated` *Ecosystem*. In GOLD's five-level scheme, this level names the host clade providing the environment; the levels below it name the host's organ system, organ, and specific material ([Mukherjee et al. 2023, *Nucleic Acids Research* 51:D957–D963, doi:10.1093/nar/gkac974](https://academic.oup.com/nar/article/51/D1/D957/6786204)). The concept therefore denotes **a living amphibian organism considered as the place a microbial sample was taken from** — not the clade as a taxonomic grouping.

The corpus's own raw table confirms this reading: the node has an organ-system subtree beneath it, and the 41 assertions on the node itself are the samples annotated only to the host and no further.

| GOLD path under `Host-associated > Amphibia` | assertions |
|---|---|
| `> Digestive system > Intestine > Fecal` | 67 |
| (the node itself, no organ given) | 41 |
| `> Urinary system` | 3 |
| `> Urinary system > Kidney` | 2 |
| `> Digestive system` / `> Digestive system > Biliary tract > Liver` | 1 each |
| `> Respiratory system`, `> Respiratory system > Lung`, `> Digestive system > Intestine`, `> ... > Biliary tract` | 0 |

(from `data/raw/gold_ecosystem_paths.tsv`, this repo)

**Inside the concept.** Any body site of a live amphibian host sampled for its microbiota: the cutaneous mucosal surface (by far the dominant sampling target in the literature, though not in this GOLD subtree), the gut lumen and faeces, the cloaca, and internal organs (kidney, liver, lung). All three orders — Anura (frogs and toads), Caudata (salamanders and newts), Gymnophiona (caecilians) — and all life stages, larval through adult.

**Neighbouring concepts, explicitly outside.**

- **The anatomical parts themselves.** `skin`, `intestine`, `lung`, `kidney` are UBERON classes and, under this repo's standing rule, a habitat naming a host *part* grounds to the anatomy term. The GOLD children above are those; this record is the whole-host node above them.
- **The environmental medium the host lives in.** Pond water, pond substrate and leaf litter are `ENVO` environmental materials. This matters because they are the *source pool* for the skin community and are frequently co-sampled — but sample-wise they are a different environment. Walke et al. found amphibian skin communities were distinct from co-sampled pond water and substrate, and enriched for taxa that are rare in those environmental reservoirs ([*ISME J* 8:2207–2217, doi:10.1038/ismej.2014.77](https://www.nature.com/articles/ismej201477), PMID [24858782](https://pubmed.ncbi.nlm.nih.gov/24858782/)).
- **The larval life stage as such.** UBERON:0004728 *amphibian larval stage* and HabitatMech's own `larva` record cover the ontogenetic stage; per issue #112 a life stage is a whole organism, so it keeps its own identity rather than grounding to a part term. The Amphibia node subsumes larvae as hosts but is not the stage term.
- **The taxon term.** `NCBITaxon:8292` *Amphibia* is a class of organisms, not a place. It belongs in `relation: xref` (#99), which is what the record does.

**Residual ambiguity, stated rather than resolved:** "Amphibia" is used in three ways in sample metadata — (i) the clade, (ii) an amphibian host as a habitat, (iii) an amphibian-derived tissue or fluid specimen. The GOLD path forces reading (ii). No further disambiguation is needed for this record, but a curator writing synonyms should not import reading (i) or (iii).

## 2. Genus — the broader kind

**Recommended genus: `ENVO:01001002` *animal-associated environment*** — "An environmental system determined by an animal." It is in the vendored slice (`data/raw/ontology_terms.tsv`), it is exactly one level too broad, and it is the pattern ENVO itself uses for host clades.

The full set of "-associated environment" classes in the vendored ENVO slice is small:

| CURIE | label | verdict |
|---|---|---|
| `ENVO:01001000` | environmental system determined by an organism | **too broad** — includes plants and fungi; this is the record's current parent |
| `ENVO:01001002` | animal-associated environment | **best available genus** — correct kind, one step broader than the concept |
| `ENVO:01001001` | plant-associated environment | wrong branch |
| `ENVO:01001041` | fungi-associated environment | wrong branch |
| `ENVO:01001179` | cnidarian-associated environment | **near-miss of high value** — proves ENVO accepts taxon-scoped associated-environment classes; wrong clade |
| `ENVO:01001055` | environment associated with an animal part or small animal | **near-miss** — asserts *part-hood or small body size*, neither of which the sources claim for an adult frog or salamander |
| `ENVO:01001176` | environment associated with an aquatic invertebrate | **near-miss** — Amphibia are vertebrates; also asserts obligate aquatic habit, false for terrestrial adults and direct developers |

Confirmed against OLS4 and Ontobee (queried 2026-08-17): `http://www.ontobee.org/ontology/ENVO?iri=http://purl.obolibrary.org/obo/ENVO_01001000` gives label *environmental system determined by an organism*, parent `ENVO:01000254` *environmental system*, with *host-associated environment* as a related synonym.

**There is no ENVO class for an amphibian-, vertebrate-, or tetrapod-associated environment.** An OLS4 search of ENVO for `amphibian` returns nothing on-target (the sole hit is UBERON:0002535 *gill*, whose definition merely mentions amphibians). ENVO's intermediate ranks between `animal-associated environment` and a clade-specific class simply do not exist yet for vertebrates. The general need was raised on the ENVO tracker as [issue #1029, "EnvO terms for host-associated samples"](https://github.com/EnvironmentOntology/envo/issues/1029).

**Recommendation to the curator:** re-parent this record from `ENVO:01001000` to `ENVO:01001002`, keep `NCBITaxon:8292` as `relation: xref`, and file an ENVO term request for *amphibian-associated environment* as a sibling of `ENVO:01001179`. This is the same disposition the corpus already gives Reptilia, Birds, Fish and Mammals, and — per the decision note — is the whole point of the #114 reversal.

*One inconsistency worth flagging:* the recorded decision note says "Nearest broader term NCBITaxon:8292 'Amphibia' attached as a parent," which contradicts the #99 xref rule stated in the same note. The record itself carries `ENVO:01001000` as parent and `NCBITaxon:8292` as xref, which is correct; the note's wording is the error, not the data.

## 3. Differentia — what distinguishes it

Ranked by how well each separates Amphibia from its siblings under `animal-associated environment` (Fish, Reptilia, Birds, Mammals, Insecta, Porifera …) and by how observable each is.

**(a) Host clade identity — the primary differentia.** Class Amphibia, `NCBITaxon:8292`: extant Lissamphibia, comprising Anura, Caudata and Gymnophiona. AmphibiaWeb records **9,081 described species as of 16 August 2026** — Anura 8,011 (88%), Caudata 837 (9%), Gymnophiona 233 (3%) ([AmphibiaWeb species counts](https://amphibiaweb.org/amphibian/speciesnums.html); [species lists](https://amphibiaweb.org/lists/)). This is the differentia that actually does the work: everything below is an elaboration of what having an amphibian host implies for a microbe.

**(b) A permeable, scaleless, mucus-glandular integument — the physicochemically distinctive one.** Amphibians are exceptional among tetrapods in having very little keratin and a thin stratum corneum; effective lipid barriers, where present at all, lie *external* to the epidermis rather than as the lipid–keratin complex found within the amniote stratum corneum ([Lillywhite 2006, *J Exp Biol* 209:202–226, doi:10.1242/jeb.02007](https://journals.biologists.com/jeb/article/209/2/202/16270/Water-relations-of-tetrapod-integument), PMID [16391344](https://pubmed.ncbi.nlm.nih.gov/16391344/)). The same skin is a major respiratory surface: in many lower vertebrates the skin is the major or sole avenue for respiration, and cutaneous exchange is diffusion-limited ([Feder & Burggren 1985, *Biological Reviews* 60:1–45, doi:10.1111/j.1469-185X.1985.tb00416.x](https://onlinelibrary.wiley.com/doi/10.1111/j.1469-185X.1985.tb00416.x), PMID [3919777](https://pubmed.ncbi.nlm.nih.gov/3919777/)). *Inference (mine, not stated as such by these two sources):* it follows that the amphibian body surface is a habitat continuously wetted and in unusually open material exchange with its surroundings, which is why environmental transmission dominates its microbiology — but that consequence *is* independently supported by (c).

**(c) A skin community drawn from, but not equal to, the environmental pool.** Amphibian skin-associated microbiomes are host-species-specific, vary with life-history stage, and are distinct from co-sampled soil, lake substrate and lake water ([Kueneman et al. 2014, *Molecular Ecology* 23:1238–1250, doi:10.1111/mec.12510](https://onlinelibrary.wiley.com/doi/10.1111/mec.12510)); skin selects for taxa rare in the surrounding environment ([Walke et al. 2014, doi:10.1038/ismej.2014.77](https://www.nature.com/articles/ismej201477)). Dominant phyla reported across studies are Pseudomonadota (Proteobacteria), Bacteroidota, Actinomycetota and Bacillota. Bacterial community richness on amphibian skin correlates with bioclimate at global scale ([Kueneman et al. 2019, *Nature Ecology & Evolution* 3:381–389, doi:10.1038/s41559-019-0798-1](https://www.nature.com/articles/s41559-019-0798-1)).

**(d) A chemically defended mucosal surface.** The skin secretes host antimicrobial peptides into mucus, so the resident community is one that tolerates them; the combined host- and microbially-derived layer is termed the *mucosome*. Skin peptide composition correlates with skin bacterial composition, indicating bidirectional peptide–microbiome interaction ([Woodhams et al. 2025, *npj Biofilms and Microbiomes*, doi:10.1038/s41522-025-00837-0](https://www.nature.com/articles/s41522-025-00837-0)). The conceptual framing — microbiome shifts as reactive homeostasis rather than dysbiosis — is set out in [Woodhams et al. 2023, *Developmental & Comparative Immunology*, doi:10.1016/j.dci.2023.104690](https://www.sciencedirect.com/science/article/abs/pii/S0145305X23000605).

**(e) A biphasic life cycle that reorganises the internal habitat.** The gut microbiota is restructured through metamorphosis: tadpole communities resemble those of fish, post-metamorphic frog communities resemble those of amniotes, with lower phylogenetic diversity in frogs than tadpoles, attributed to the dietary switch and the wholesale reorganisation of the intestine ([Kohl et al. 2013, *Environmental Microbiology Reports* 5:899–903, doi:10.1111/1758-2229.12092](https://onlinelibrary.wiley.com/doi/10.1111/1758-2229.12092)). Manipulative and gnotobiotic follow-up across *Lithobates* species from egg to unfed juvenile confirmed variation across both species and age class ([Warne et al. 2017, *Integrative and Comparative Biology* 57:786–794, doi:10.1093/icb/icx100](https://academic.oup.com/icb/article/57/4/786/4037364)); in *Notophthalmus viridescens*, metamorphosing individuals are compositionally intermediate between paedomorphic and post-metamorphic stages ([Fontaine, Mineo & Kohl 2021, *FEMS Microbiology Ecology* 97:fiab021, doi:10.1093/femsec/fiab021](https://academic.oup.com/femsec/article/97/4/fiab021/6132262)). *This makes life stage a genuine axis of variation within the concept, not a nuisance* — a curator should expect the record to cover materially different communities at different Gosner stages.

**(f) Ectothermy.** Body temperature and therefore habitat temperature track the environment. This aligns the concept with BacDive's `host animal ectotherm` grouping already in the corpus, and separates it from the Birds and Mammals siblings. *Inference (mine):* the pairing of ectothermy with the physiology in (b) is what makes environmental temperature and moisture direct, not buffered, drivers of this habitat's physicochemistry; a supporting synthesis is [Bletz et al. / Rebollar et al. 2023, *FEMS Microbiology Reviews* 47:fuad002, doi:10.1093/femsre/fuad002](https://academic.oup.com/femsre/article/47/1/fuad002/7022318) — "From the organismal to biosphere levels: environmental impacts on the amphibian microbiota."

**(g) Disease context as a driver of sampling effort.** A large fraction of amphibian microbiome sampling exists because of chytridiomycosis. *Batrachochytrium dendrobatidis* (Bd) was implicated in the decline of at least 501 amphibian species including 90 presumed extinctions ([Scheele et al. 2019, *Science* 363:1459–1463, doi:10.1126/science.aav0379](https://www.science.org/doi/10.1126/science.aav0379), PMID [30923224](https://pubmed.ncbi.nlm.nih.gov/30923224/)) — a figure formally contested in a technical comment ([doi:10.1126/science.aay1838](https://www.science.org/doi/10.1126/science.aay1838), PMID [32193293](https://pubmed.ncbi.nlm.nih.gov/32193293/)), to which the authors responded; cite the number with that caveat or not at all. The cultured resource is substantial: ~2,000 bacterial isolates from 37 amphibian host species across 18 studies on five continents, with antifungal-activity metadata ([Woodhams et al. 2015, *Ecology* 96:595, doi:10.1890/14-1837.1](https://esajournals.onlinelibrary.wiley.com/doi/abs/10.1890/14-1837.1); data at [Ecological Archives E096-059](https://esapubs.org/archive/ecol/E096/059/)). **Do not put this in the definition** — disease is a state of the habitat's occupants, not a differentia of the habitat.

## 4. Sources

Grouped by what they support. All URLs checked 2026-08-17.

**Concept scope and the source vocabulary**
- Mukherjee S. et al. (2023) Twenty-five years of Genomes OnLine Database (GOLD): data updates and new features in v.9. *Nucleic Acids Research* 51(D1):D957–D963. [doi:10.1093/nar/gkac974](https://academic.oup.com/nar/article/51/D1/D957/6786204), PMID 36318257. *(Defines the five-level classification; `Host-associated` is one of three top-level Ecosystems.)* Correction: *NAR* 52(6):3483, doi:10.1093/nar/gkae162.
- `data/raw/gold_ecosystem_paths.tsv`, this repository — the ten GOLD paths under `Host-associated > Amphibia` and their assertion counts.

**Ontology status**
- ENVO term records via Ontobee and OLS4: `ENVO:01001000`, `ENVO:01001002`, `ENVO:01001179`, `ENVO:01001055`, `ENVO:01001176`. [http://www.ontobee.org/ontology/ENVO](http://www.ontobee.org/ontology/ENVO); [https://www.ebi.ac.uk/ols4/ontologies/envo](https://www.ebi.ac.uk/ols4/ontologies/envo).
- Buttigieg P.L. et al. (2016) The environment ontology in 2016. *Journal of Biomedical Semantics* 7:57. [PMC5035502](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035502/). Buttigieg P.L. et al. (2013) The environment ontology: contextualising biological and biomedical entities. *J Biomed Semantics* 4:43. [PMC3904460](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3904460/).
- ENVO issue #1029, "EnvO terms for host-associated samples." [github.com/EnvironmentOntology/envo/issues/1029](https://github.com/EnvironmentOntology/envo/issues/1029).

**Host physiology (the differentia)**
- Lillywhite H.B. (2006) Water relations of tetrapod integument. *J Exp Biol* 209:202–226. [doi:10.1242/jeb.02007](https://journals.biologists.com/jeb/article/209/2/202/16270/Water-relations-of-tetrapod-integument), PMID 16391344.
- Feder M.E. & Burggren W.W. (1985) Cutaneous gas exchange in vertebrates: design, patterns, control and implications. *Biological Reviews* 60:1–45. [doi:10.1111/j.1469-185X.1985.tb00416.x](https://onlinelibrary.wiley.com/doi/10.1111/j.1469-185X.1985.tb00416.x), PMID 3919777.

**Microbial ecology of the habitat**
- Kueneman J.G. et al. (2014) The amphibian skin-associated microbiome across species, space and life history stages. *Molecular Ecology* 23:1238–1250. [doi:10.1111/mec.12510](https://onlinelibrary.wiley.com/doi/10.1111/mec.12510).
- Walke J.B. et al. (2014) Amphibian skin may select for rare environmental microbes. *ISME J* 8:2207–2217. [doi:10.1038/ismej.2014.77](https://www.nature.com/articles/ismej201477), PMID 24858782.
- Kueneman J.G. et al. (2019) Community richness of amphibian skin bacteria correlates with bioclimate at the global scale. *Nature Ecology & Evolution* 3:381–389. [doi:10.1038/s41559-019-0798-1](https://www.nature.com/articles/s41559-019-0798-1).
- Kohl K.D. et al. (2013) Restructuring of the amphibian gut microbiota through metamorphosis. *Environmental Microbiology Reports* 5:899–903. [doi:10.1111/1758-2229.12092](https://onlinelibrary.wiley.com/doi/10.1111/1758-2229.12092).
- Warne R.W. et al. (2017) Manipulation of gut microbiota reveals shifting community structure shaped by host developmental windows in amphibian larvae. *Integr Comp Biol* 57:786–794. [doi:10.1093/icb/icx100](https://academic.oup.com/icb/article/57/4/786/4037364).
- Fontaine S.S., Mineo P.M. & Kohl K.D. (2021) Changes in the gut microbial community of the eastern newt across its three distinct life stages. *FEMS Microbiol Ecol* 97:fiab021. [doi:10.1093/femsec/fiab021](https://academic.oup.com/femsec/article/97/4/fiab021/6132262).
- Colombo B.M., Scalvenzi T., Benlamara S. & Pollet N. (2015) Microbiota and mucosal immunity in amphibians. *Frontiers in Immunology* 6:111. [doi:10.3389/fimmu.2015.00111](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2015.00111/full).
- Xu L. et al. (2024) From skin to gut: understanding microbial diversity in *Rana amurensis* and *R. dybowskii*. *Current Microbiology* 81:340. [doi:10.1007/s00284-024-03868-6](https://link.springer.com/article/10.1007/s00284-024-03868-6), PMID 39269482. *(Documents that cutaneous and gut communities within one host differ in both diversity and assembly process — direct evidence the concept spans heterogeneous sub-habitats.)*

**Reviews and syntheses (2023–2025, most recent first)**
- *FEMS Microbiology Reviews* 47:fuad002 (2023), "From the organismal to biosphere levels: environmental impacts on the amphibian microbiota." [doi:10.1093/femsre/fuad002](https://academic.oup.com/femsre/article/47/1/fuad002/7022318).
- Woodhams D.C. et al. (2023) The adaptive microbiome hypothesis and immune interactions in amphibian mucus. *Developmental & Comparative Immunology* 145:104690. [doi:10.1016/j.dci.2023.104690](https://www.sciencedirect.com/science/article/abs/pii/S0145305X23000605).
- Wang et al. (2025) Research status and prospect of amphibian symbiotic microbiota. *Animals* 15(7):934. [doi:10.3390/ani15070934](https://www.mdpi.com/2076-2615/15/7/934).
- Jiménez R.R. & Sommer S. (2017) The amphibian microbiome: natural range of variation, pathogenic dysbiosis, and role in conservation. *Biodiversity and Conservation* 26:763–786. [doi:10.1007/s10531-016-1272-x](https://link.springer.com/article/10.1007/s10531-016-1272-x).

**Reference works and data resources**
- AmphibiaWeb, University of California, Berkeley. Species counts as of 2026-08-16: 9,081 total. [https://amphibiaweb.org/amphibian/speciesnums.html](https://amphibiaweb.org/amphibian/speciesnums.html). Companion resource: [Amphibian Species of the World, AMNH](https://amphibiansoftheworld.amnh.org/).
- Woodhams D.C. et al. (2015) Antifungal isolates database of amphibian skin-associated bacteria and function against emerging fungal pathogens. *Ecology* 96:595. [doi:10.1890/14-1837.1](https://esajournals.onlinelibrary.wiley.com/doi/abs/10.1890/14-1837.1).
- Scheele B.C. et al. (2019) *Science* 363:1459–1463. [doi:10.1126/science.aav0379](https://www.science.org/doi/10.1126/science.aav0379) — **cite with** the technical comment [doi:10.1126/science.aay1838](https://www.science.org/doi/10.1126/science.aay1838).

**Claims that are my inference, not a source's statement**, flagged again for the record: (i) that permeable, cutaneously respiring skin *therefore* makes the amphibian body surface an unusually open habitat — the physiology papers state the permeability and the respiration, not the habitat consequence, though Walke 2014 and Kueneman 2014 independently establish the environmental-transmission pattern; (ii) that ectothermy makes environmental temperature a direct rather than buffered driver of this habitat; (iii) the recommendation to re-parent to `ENVO:01001002` and to request an ENVO term. None of the three belongs in the definition sentence as written.

## 5. Synonyms and what NOT to conflate

**Names in real use for this concept**
- amphibian-associated environment *(the ENVO-pattern name a term request should use)*
- amphibian host-associated environment; amphibian-associated habitat
- amphibian microbiome / amphibian microbiota *(used for the community, not the place — acceptable as a RELATED synonym at most)*
- Lissamphibia-associated environment *(precise for the extant clade; rare in sample metadata)*
- Order-scoped narrower names in common use: frog-associated, toad-associated, salamander-associated, newt-associated, caecilian-associated, tadpole-associated. These are **narrower**, not synonyms.

**Do not conflate**
- **`NCBITaxon:8292` *Amphibia*.** The taxon is a class of organisms; the habitat is the environment an individual host provides. `relation: xref`, never `parent`, never a grounding target (#99, #114).
- **`UBERON:0004728` *amphibian larval stage* / `UBERON:0002548` *larva* / BTO:0001347 *tadpole*.** Life-stage and larval-organism terms. A tadpole is a whole organism at a stage, so per #112 it keeps its own identity; it is not this concept and this concept is not it.
- **Herptile / herpetofauna / "amphibians and reptiles."** A convenience grouping, not a clade. Amphibia and Reptilia are separate HabitatMech records with separate assertion sets; the Reptilia record's own note documents that even upstream mapping to `NCBITaxon:8504` (Lepidosauria) was over-narrow. Do not merge them under a "herp-associated" label.
- **Anamniote / "lower vertebrate" / "cold-blooded vertebrate."** Fish are anamniotes and ectotherms too; these names are broader and would silently pull in the Fish record.
- **`ENVO:01001176` *environment associated with an aquatic invertebrate*.** Wrong on both counts — vertebrate, and not obligately aquatic.
- **`ENVO:01001055` *environment associated with an animal part or small animal*.** Grounding here would assert part-hood or small body size that no source claims for the concept.
- **The amphibian's pond or terrarium.** Freshwater, sediment, and captive-enclosure environments are `ENVO` environmental materials and features. They are the transmission source, and studies routinely co-sample them precisely *because* they are a different environment (Walke 2014).
- **Chytridiomycosis, ranavirosis, red-leg.** Disease states. `NOT_APPLICABLE` is the corpus's disposition for diseases; they are not this concept and should not appear in its definition.
- **Amphibian skin secretions / frog skin peptides as a substance.** A product of the habitat, extensively studied as a pharmacological resource. Not a habitat.

## 6. Whether it should be a term at all

**Yes — mint it, define it, and file the ENVO request.**

The evidence is unambiguous that this is a habitat and not one of the dispositions that would argue against a term:

- It is **not a process, quality, disease state or procedure.** It is a physical setting from which samples are drawn, with 114 upstream assertions across a ten-node organ subtree.
- It is **not merely a taxonomic grouping** in the sense that would make it not-a-place. The label names a taxon, but the GOLD path uses it to name *the host that provides the environment*, and ENVO models exactly this relation at `plant-associated environment`, `animal-associated environment`, `fungi-associated environment` and — decisively for the precedent — `cnidarian-associated environment`, a clade-scoped associated-environment class ENVO already accepted.
- It is **not a sampling artefact.** There is a coherent, well-characterised, and distinctive microbial ecology here: host-species-specific communities distinguishable from the surrounding environment (Kueneman 2014; Walke 2014), a chemically defended mucosal interface with bidirectional peptide–microbe interaction (Woodhams 2023, 2025), and an ontogenetic restructuring of the internal habitat at metamorphosis (Kohl 2013; Warne 2017; Fontaine 2021). Two decades of literature and a ~2,000-isolate cultured collection from 37 host species (Woodhams 2015) attest to it.

The prior `NOT_APPLICABLE` was the #114 error the decision note describes: it asserted that the concept is not a habitat, which the literature contradicts. The correct disposition is `CONFIRM_UNGROUNDED` with `NCBITaxon:8292` as `relation: xref`, `ENVO:01001002` as the parent, and a term request for *amphibian-associated environment* — the same treatment given Reptilia, Birds, Fish, Mammals, Nematoda and Sponge.

Per the standing rule in this repo's memory, **submitting that ENVO term request needs your explicit yes for this specific request** — this report does not authorise it.

**On the one-sentence constraint:** the proposed definition holds in one sentence, but note that the missing intermediate class is real. `animal-associated environment` → *amphibian-associated environment* skips over any vertebrate- or tetrapod-associated rank, so Amphibia, Reptilia, Birds, Fish and Mammals will all sit as direct siblings under `ENVO:01001002` alongside sponges, cnidarians and insects. That is ENVO's current shape, not a defect in this definition, but it is worth raising in the same term request as a grouping-class suggestion.

## Citations

1. https://academic.oup.com/nar/article/51/D1/D957/6786204
2. https://www.nature.com/articles/ismej201477
3. https://pubmed.ncbi.nlm.nih.gov/24858782/
4. http://www.ontobee.org/ontology/ENVO?iri=http://purl.obolibrary.org/obo/ENVO_01001000`
5. https://github.com/EnvironmentOntology/envo/issues/1029
6. https://amphibiaweb.org/amphibian/speciesnums.html
7. https://amphibiaweb.org/lists/
8. https://journals.biologists.com/jeb/article/209/2/202/16270/Water-relations-of-tetrapod-integument
9. https://pubmed.ncbi.nlm.nih.gov/16391344/
10. https://onlinelibrary.wiley.com/doi/10.1111/j.1469-185X.1985.tb00416.x
11. https://pubmed.ncbi.nlm.nih.gov/3919777/
12. https://onlinelibrary.wiley.com/doi/10.1111/mec.12510
13. https://www.nature.com/articles/s41559-019-0798-1
14. https://www.nature.com/articles/s41522-025-00837-0
15. https://www.sciencedirect.com/science/article/abs/pii/S0145305X23000605
16. https://onlinelibrary.wiley.com/doi/10.1111/1758-2229.12092
17. https://academic.oup.com/icb/article/57/4/786/4037364
18. https://academic.oup.com/femsec/article/97/4/fiab021/6132262
19. https://academic.oup.com/femsre/article/47/1/fuad002/7022318
20. https://www.science.org/doi/10.1126/science.aav0379
21. https://pubmed.ncbi.nlm.nih.gov/30923224/
22. https://www.science.org/doi/10.1126/science.aay1838
23. https://pubmed.ncbi.nlm.nih.gov/32193293/
24. https://esajournals.onlinelibrary.wiley.com/doi/abs/10.1890/14-1837.1
25. https://esapubs.org/archive/ecol/E096/059/
26. http://www.ontobee.org/ontology/ENVO
27. https://www.ebi.ac.uk/ols4/ontologies/envo
28. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035502/
29. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3904460/
30. https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2015.00111/full
31. https://link.springer.com/article/10.1007/s00284-024-03868-6
32. https://www.mdpi.com/2076-2615/15/7/934
33. https://link.springer.com/article/10.1007/s10531-016-1272-x
34. https://amphibiansoftheworld.amnh.org/