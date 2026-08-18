---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T15:50:32.590597'
end_time: '2026-08-17T16:00:25.963164'
duration_seconds: 593.37
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: 'Mammals: Human'
  habitat_identifier: habitatmech:GOLD.cd0b0940e5
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'BACDIVE: Human; GOLD: Host-associated > Mammals: Human'
  assertions: '52129'
  parent_terms: ENVO:01001000, ENVO:01001002
  xrefs: (none)
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term ENVO:01001002 'animal-associated environment' attached as a parent.\
    \ Humans as host, the single largest ungrounded concept at 40432 GOLD organisms.\
    \ No human-associated environment term exists in ENVO. Deliberately not grounded\
    \ to animal-associated environment: every host clade would then merge onto one\
    \ record and the host distinction is the entire content. Highest-value ENVO term\
    \ request. (source concept habitatmech:GOLD.cd0b0940e5) Merged into habitatmech:GOLD.cd0b0940e5\
    \ 'Mammals: Human': the same concept under another source's name. Novel-concept\
    \ merge (#116): BacDive's 'Human' and GOLD's 'Mammals: Human' are the same habitat\
    \ \u2014 a human acting as host \u2014 and both are novel, so neither has an ontology\
    \ term to merge on. Before SAME_AS they were two permanent records holding 40,432\
    \ and 11,697 assertions for one concept, published as two pages, and the largest\
    \ habitat in the corpus appeared nowhere as such. Merged onto the GOLD identifier\
    \ because it carries the larger attestation and the deeper path; the choice of\
    \ which id survives is arbitrary between two minted ids and is recorded here rather\
    \ than left to ordering. Both keep their attestations on the merged record, so\
    \ no evidence is lost. (source concept habitatmech:BACDIVE.c9b246fcbb)"
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
  total_cost_usd: 3.4973205000000003
  session_id: a9e53994-9cd7-4c12-a036-7be66ed8be8c
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 24
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Mammals: Human
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.cd0b0940e5
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** BACDIVE: Human; GOLD: Host-associated > Mammals: Human
- **Upstream assertion volume:** 52129
- **Nearest broader term already on the record:** ENVO:01001000, ENVO:01001002
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term ENVO:01001002 'animal-associated environment' attached as a parent. Humans as host, the single largest ungrounded concept at 40432 GOLD organisms. No human-associated environment term exists in ENVO. Deliberately not grounded to animal-associated environment: every host clade would then merge onto one record and the host distinction is the entire content. Highest-value ENVO term request. (source concept habitatmech:GOLD.cd0b0940e5) Merged into habitatmech:GOLD.cd0b0940e5 'Mammals: Human': the same concept under another source's name. Novel-concept merge (#116): BacDive's 'Human' and GOLD's 'Mammals: Human' are the same habitat — a human acting as host — and both are novel, so neither has an ontology term to merge on. Before SAME_AS they were two permanent records holding 40,432 and 11,697 assertions for one concept, published as two pages, and the largest habitat in the corpus appeared nowhere as such. Merged onto the GOLD identifier because it carries the larger attestation and the deeper path; the choice of which id survives is arbitrary between two minted ids and is recorded here rather than left to ordering. Both keep their attestations on the merged record, so no evidence is lost. (source concept habitatmech:BACDIVE.c9b246fcbb)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Mammals: Human** as a microbial habitat, with citations.

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

# Definition research: *Mammals: Human* (`habitatmech:GOLD.cd0b0940e5`)

> **Proposed definition:** An animal-associated environment which is determined by a human being (*Homo sapiens*).

That wording is deliberately parallel to the existing ENVO siblings ("An environmental system determined by an animal" / "…determined by a green plant" / "…determined by a cnidarian or part of a cnidarian"), so it slots into the pattern without inventing new machinery. If the curator wants the host role made explicit rather than left to the genus, the minimal expansion is:

> An animal-associated environment which is determined by a human being (*Homo sapiens*) acting as host to the organisms living on or within it.

Anything longer than this is a sign that the missing piece is an **intermediate class** (there is no *vertebrate-* or *mammal-associated environment* in ENVO at all — see §2), not a longer sentence.

---

## 1. What the concept denotes

**The denotation.** The environmental system constituted by an individual living human body considered as a place where microorganisms live: the skin surface, and the cavities and lumens continuous with the exterior (oral cavity, airways, gastrointestinal tract, urogenital tract), together with the body fluids and body products sampled from them. Operationally, it is the thing a sample is taken *from* when the recorded provenance is "a person" and no narrower site is stated.

**How the sources scope it.** Both attestations are host-role classifications, not anatomy:

- **GOLD** places this at Ecosystem = `Host-associated`, Ecosystem Category = `Mammals`, Ecosystem Type = `Human`, with Ecosystem Subtype and Specific Ecosystem (which is where `Digestive system` → `Large intestine`, `Skin`, `Saliva` etc. live) left unfilled. GOLD's five-level scheme is explicitly sample-driven rather than a complete enumeration of possible paths ([GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification); [Mukherjee et al. 2019, *NAR* 47:D649, doi:10.1093/nar/gky977](https://academic.oup.com/nar/article/47/D1/D649/5144132); [Reddy et al. 2015, *NAR* 43:D1099, doi:10.1093/nar/gku950](https://academic.oup.com/nar/article/43/D1/D1099/2439522)).
- **BacDive** places it in a three-level isolation-source ontology of 387 terms (`#Host > #Human > …`, structurally identical to the illustrated `#Environmental > #Aquatic > #Marine`) ([Reimer et al. 2022, *NAR* 50:D741, doi:10.1093/nar/gkab961](https://academic.oup.com/nar/article/50/D1/D741/6414049)).

**Boundary — inside the concept:** any human individual acting as host, healthy or diseased, of any age, and any body site *when the site is not separately recorded*; clinical specimens (blood, sputum, wound, urine) taken from a person; body products sampled *in situ* from a person.

**Boundary — neighbouring concepts, outside:**

| Neighbour | Why it is not this concept |
|---|---|
| `ENVO:01001829` *human settlement*, `ENVO:01000744` *human dwelling*, `ENVO:00000070` *human construction* | Human-**determined** but by presence and constructions; the built environment, not the body |
| Sewage, wastewater, sludge | Human-**derived material** in an engineered system; MIxS treats these under the wastewater/sludge package |
| Human gut, human skin, oral cavity as such | **Narrower parts** of this concept; per this repo's rule these ground to UBERON anatomy terms and are subordinate records |
| `NCBITaxon:9606` *Homo sapiens* | A class of **organisms**, not a place — belongs in `relation: xref` |
| Human food, drinking water | Materials humans consume, not environments humans determine |
| Human cadaver / decomposition environments | Post-mortem successional systems; a distinct habitat with its own literature. *(My judgement, not a sourced distinction — ENVO's related "animal-associated habitat" phrasing does say "living or dead", so this boundary is a choice the curator should make explicitly.)* |

**Ambiguity to state rather than resolve silently.** The label "Human" is used in three genuinely different senses across microbiology metadata: (a) human-as-host — the reading the GOLD path and the BacDive `#Host` parent both force, and the one meant here; (b) human-as-taxon (a *Homo sapiens* isolate identity); (c) human-as-influence (anthropogenic/built environments). Only (a) is this concept. There is a fourth, subtler issue that is **granularity, not ambiguity**: this record is simultaneously the general class *and* the roll-up bucket for samples where the submitter recorded no body site. The 52,129 assertions therefore mix genuinely site-unspecified samples with samples that simply were not curated deeper. That is worth a `comment` on the record; it does not change the definition.

---

## 2. Genus — the broader kind

**Smallest well-established kind: `ENVO:01001002` *animal-associated environment*** — "An environmental system determined by an animal" (synonyms: *Metazoan-associated environment*, *animal environment*). Verified against ENVO release **2026-06-26** (6,936 terms) via [EBI OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002).

Its **only three direct subclasses** in that release are `ENVO:01001176` *environment associated with an aquatic invertebrate*, `ENVO:01001179` *cnidarian-associated environment*, and `ENVO:01001829` *human settlement*. There is no vertebrate-, mammal-, or human-associated class. A full-text ENVO search for "mammal" returns only `ENVO:00000547` *waterhole*, `ENVO:02000025` *sweat material*, `ENVO:02000028` *ear wax material* and `ENVO:02000004` *nesting material* — no environmental system class.

**The pattern the genus belongs to is documented.** ENVO models environments organised around a single entity with strong causal influence on the surrounding space; the 2013 ENVO paper uses *the human gut environment, determined by the human gut* as one of its worked examples of exactly this construction ([Buttigieg et al. 2013, *J Biomed Semantics* 4:43, doi:10.1186/2041-1480-4-43](https://link.springer.com/article/10.1186/2041-1480-4-43); [Buttigieg et al. 2016, *J Biomed Semantics* 7:57, doi:10.1186/s13326-016-0097-6](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035502/)). The proposed term is a straight instantiation of it.

### Near-misses and why each fails

- **`ENVO:01001000` *environmental system determined by an organism*** (synonym: *host-associated environment*) — the correct grandparent, and already on the record. Too broad: it merges plant, fungal and animal hosts.
- **`ENVO:01001829` *human settlement*** — "An anthropised ecosystem which is determined by the presence of humans and their constructions." This is the *only* human-specific descendant of the genus, and it is the wrong kind of human-determination entirely: it asserts constructions and habitation. Grounding here would publish "human host = village".
- **`MIXS:0016003` *HumanAssociated*** — the GSC MIxS environmental package, "A collection of terms appropriate when collecting samples and sequencing samples obtained from a person to examine their human-associated microbiome or genome, that does not have a specific extension" ([MIxS 0016003](https://genomicsstandardsconsortium.github.io/mixs/0016003/)). Semantically the same concept, and the strongest evidence that the concept is standard — but it is a **metadata checklist that types a sample record, not a class of place**, so it cannot serve as an ENVO-style grounding target. Record it as an xref.
- **`NCBITaxon:9606` *Homo sapiens*** — an organism class. Per this repo's established line (#114), the taxon is not the habitat; it goes in `relation: xref`, and `NOT_APPLICABLE` would be the wrong disposition.
- **UBERON anatomy terms** (`skin of body`, `gut`, `oral cavity`, `blood`) — narrower: parts of the host, and the correct targets for the sibling records that *do* name a body site.
- **`ENVO:02000025` sweat material, `ENVO:02000028` ear wax material** — human/mammalian body products, but environmental *materials*, narrower and of the wrong ontological kind (material, not system).
- **EMPO "Animal"** — `ENVO:01001002` is mapped into ENVO's EMPO subset as the *Animal* category; EMPO likewise has no human class, so it offers no alternative target.

**Existing request on file.** [ENVO issue #1029, "EnvO terms for host-associated samples"](https://github.com/EnvironmentOntology/envo/issues/1029) (opened 20 Oct 2020) requested exactly *host-associated biome*, *animal-associated biome*, **human-associated biome** and *plant-associated biome*, on the reasoning that for a host-derived sample the biome is the host organism. The issue is **closed**, and no such class exists in the 2026-06-26 release — that release check is the verifiable fact; I could not retrieve the thread's replies from the rendered page, so I cannot say *why* it closed, and a curator filing a new request should read the thread first.

---

## 3. Differentia — what distinguishes it from its siblings

The differentia is **host species identity: *Homo sapiens***. That alone is sufficient and defensible. The observable properties below support *why* host identity carves a real habitat rather than an arbitrary label, and are the material for `comment` / `causal_graphs` rather than for the definition sentence:

1. **The human body is a structured set of habitats, and site identity dominates community composition.** Surveying up to 27 sites in 7–9 adults on four occasions, community composition was determined primarily by body habitat — more than by time or by which person was sampled ([Costello et al. 2009, *Science* 326:1694, doi:10.1126/science.1177486](https://www.science.org/doi/10.1126/science.1177486); PMID 19892944). Confirmed at scale by the HMP: diversity is "strongly determined by microbial habitat", with strong niche specialisation within and among individuals ([HMP Consortium 2012, *Nature* 486:207, doi:10.1038/nature11234](https://www.nature.com/articles/nature11234)).
2. **Measurable biomass.** ~3.8 × 10¹³ bacteria in a 70-kg reference adult, overwhelmingly colonic, against ~3.0 × 10¹³ human cells — a B/H ratio of ~1.3, replacing the folkloric 10:1 ([Sender, Fuchs & Milo 2016, *PLoS Biol* 14:e1002533, doi:10.1371/journal.pbio.1002533](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002533)).
3. **At least one site is quantitatively human-specific among mammals.** Across 26 mammal species and 50 studies, *Lactobacillus* relative abundance in the human vagina is typically >70%, whereas in other mammals lactobacilli rarely exceed 1%, with correspondingly low pH ([Miller, Beasley, Dunn & Archie 2016, *Front Microbiol* 7:1936, doi:10.3389/fmicb.2016.01936](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5143676/)).
4. **Distinctive physicochemistry of the skin compartment** — a desiccated, nutrient-poor, acidic surface partitioned into sebaceous, moist and dry site types ([Byrd, Belkaid & Segre 2018, *Nat Rev Microbiol* 16:143, doi:10.1038/nrmicro.2017.157](https://www.nature.com/articles/nrmicro.2017.157); PMID 29332945).
5. **Host identity is not incidental: some resident lineages co-speciated with the host.** Clades within Bacteroidaceae and Bifidobacteriaceae have been maintained exclusively within host lineages across hundreds of thousands of host generations, with divergence times congruent with hominid divergence over ~15 Myr ([Moeller et al. 2016, *Science* 353:380, doi:10.1126/science.aaf3951](https://www.science.org/doi/10.1126/science.aaf3951); PMID 27463672).

**The honest counterweight, and it belongs in the record.** Do **not** write a definition asserting that the human microbiota is globally unique among mammals. A 60-species mammalian survey found that diet and host phylogeny jointly structure gut communities and that *the gut microbiota of humans living a modern lifestyle is typical of omnivorous primates* ([Ley et al. 2008, *Science* 320:1647, doi:10.1126/science.1155725](https://www.science.org/doi/10.1126/science.1155725); PMID 18497261). The claim the sources support is that **this is a distinct host and therefore a distinct habitat**, not that every compartment of it is compositionally unlike every other mammal's.

---

## 4. Sources

All claims above are cited inline. Consolidated, by role:

**Reference vocabularies and standards**
- ENVO, release 2026-06-26, via EBI OLS4 — `ENVO:01001002`, `ENVO:01001000`, `ENVO:01001001`, `ENVO:01001041`, `ENVO:01001179`, `ENVO:01001829`: https://www.ebi.ac.uk/ols4/ontologies/envo
- ENVO issue #1029 (human-associated biome request, closed): https://github.com/EnvironmentOntology/envo/issues/1029
- ENVO term-request requirements (definitions must cite resolvable references): https://github.com/EnvironmentOntology/envo/wiki/Creating-good-definitions
- GSC MIxS `HumanAssociated` package (`MIXS:0016003`), plus HumanGut/HumanOral/HumanSkin/HumanVaginal extensions: https://genomicsstandardsconsortium.github.io/mixs/0016003/
- MIxS-SA extension, on the 17 environmental packages and the human-package family — [Dheilly et al. 2022, *ISME Commun* 2:104, doi:10.1038/s43705-022-00092-w](https://www.nature.com/articles/s43705-022-00092-w)
- GOLD five-level ecosystem classification: https://gold.jgi.doe.gov/ecosystem_classification; GOLD v.5 [doi:10.1093/nar/gku950](https://academic.oup.com/nar/article/43/D1/D1099/2439522), v.7 [doi:10.1093/nar/gky977](https://academic.oup.com/nar/article/47/D1/D649/5144132), v.8 [doi:10.1093/nar/gkaa983](https://academic.oup.com/nar/article/49/D1/D723/5957166), v.9 [doi:10.1093/nar/gkac974](https://academic.oup.com/nar/article/51/D1/D957/6786204)
- BacDive isolation-source ontology, 387 terms on three levels — [doi:10.1093/nar/gkab961](https://academic.oup.com/nar/article/50/D1/D741/6414049); BacDive 2025 — [doi:10.1093/nar/gkae959](https://academic.oup.com/nar/article/53/D1/D748/7848838)

**ENVO methodology**
- [Buttigieg et al. 2013, *J Biomed Semantics* 4:43, doi:10.1186/2041-1480-4-43](https://link.springer.com/article/10.1186/2041-1480-4-43) — the "determined by" pattern, with *human gut environment* as a worked example
- [Buttigieg et al. 2016, *J Biomed Semantics* 7:57, doi:10.1186/s13326-016-0097-6](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035502/)

**Primary literature on the habitat**
- Costello et al. 2009, *Science* 326:1694 — doi:10.1126/science.1177486
- HMP Consortium 2012, *Nature* 486:207 — doi:10.1038/nature11234
- Sender, Fuchs & Milo 2016, *PLoS Biol* 14:e1002533 — doi:10.1371/journal.pbio.1002533
- Miller et al. 2016, *Front Microbiol* 7:1936 — doi:10.3389/fmicb.2016.01936
- Byrd, Belkaid & Segre 2018, *Nat Rev Microbiol* 16:143 — doi:10.1038/nrmicro.2017.157
- Moeller et al. 2016, *Science* 353:380 — doi:10.1126/science.aaf3951
- Ley et al. 2008, *Science* 320:1647 — doi:10.1126/science.1155725

**Community practice (human separated from animal by convention)**
- [Kasmanas et al. 2021, *NAR* 49:D743, doi:10.1093/nar/gkaa1031](https://academic.oup.com/nar/article/49/D1/D743/5998395) — HumanMetagenomeDB, ~70,000 curated human metagenome samples
- [AnimalAssociatedMetagenomeDB, 2023, PMC10552293](https://pmc.ncbi.nlm.nih.gov/articles/PMC10552293/) — scoped to "non-human, animal-associated metagenomic data", human samples filtered out during curation; v1.0 holds 10,885 samples

**Explicitly my inference, not any source's statement:** (a) that the human-cadaver/decomposition environment sits outside this concept; (b) that this record functions as a body-site roll-up as well as a general class; (c) the near-miss verdicts in §2 — those are ontological judgements built on the definitions quoted, not claims made by ENVO.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**
- *human-associated environment* — the ENVO-pattern form; the label I would request
- *human-associated habitat*, *human host-associated environment*, *human-associated biome* (the last as filed in ENVO #1029)
- *human host* (BacDive `#Host > #Human`; GOLD Ecosystem Category `Human`)
- GOLD paths: `Host-associated > Mammals > Human` and `Host-associated > Human`
- MIxS `human-associated` environmental package (`MIXS:0016003`)
- SRA/BioSample `host: Homo sapiens`
- *human body habitat* (Costello et al. 2009's own phrasing)
- *human microbiome habitat* — common but loose; the microbiome is the community, not the place

**Commonly but wrongly treated as the same thing**
1. **`NCBITaxon:9606` *Homo sapiens*** — the taxon. A class of organisms is not a place. `relation: xref`.
2. **The human microbiome / human microbiota** — the resident community. Naming a habitat after its inhabitants is the same error as defining "soil" as "soil bacteria".
3. **`ENVO:01001829` human settlement**, human dwelling, indoor/built environment — human-determined by construction, not by hosting.
4. **Sewage, wastewater, sludge** — human-derived material in an engineered habitat.
5. **Human gut / human skin / oral cavity** — proper parts, narrower, and separately grounded to UBERON in this corpus.
6. **Clinical/disease categories** ("clinical isolate", "patient", "infection", "contamination") — a health state or provenance annotation, not a habitat; note the precedent in #99 where an over-claiming parent was reduced to an xref.
7. **`ENVO:01001002` animal-associated environment used *as the grounding*** — this is the genus, and grounding here is precisely the merge the curator's note refuses: every host clade collapses onto one record and the host distinction, which is the entire content, disappears.
8. **`ENVO:01001000` "host-associated environment"** — that synonym is attached to the *organism*-level class, which spans plants and fungi. It is a trap for anyone matching on the string "host-associated".

---

## 6. Should this be a term at all?

**Yes, and it is the strongest candidate in the corpus.** It is not a process, quality, disease state, sampling artefact, or a taxon masquerading as a place. It is a place under this repo's own settled rule — an organism acting as host *is* a habitat, while the taxon term is not — and it is precisely the construction ENVO already uses for plants, fungi, cnidarians and animals.

The supporting case:

- **Structural precedent inside the genus.** `ENVO:01001179` *cnidarian-associated environment* shows ENVO is willing to mint clade-specific children of `ENVO:01001002`. A human child is not a new kind of ask.
- **Standards precedent outside ENVO.** GSC MIxS gives the human-associated case its own environmental package plus four body-site extensions; GOLD gives it an Ecosystem Category; BacDive gives it a second-level node under `#Host`. Three independent vocabularies partition human-as-host as a first-class category, and the metagenome-database community does the same in practice (HumanMetagenomeDB ~70,000 samples vs 10,885 in the explicitly non-human animal counterpart).
- **Evidential weight here.** 52,129 upstream assertions (per the record: 40,432 GOLD organisms + 11,697 BacDive strains), the largest single ungrounded concept in HabitatMech.

**Two things the curator should carry into the request:**

1. **Ask for the intermediates too.** The gap is not one term but a chain: `ENVO:01001002` has no vertebrate- or mammal-associated child, so a human class would hang directly off *animal-associated environment* with nothing between. Requesting *mammal-associated environment* (or *vertebrate-associated environment*) alongside *human-associated environment* is the more defensible ask, and it would also give this corpus a target for the sibling GOLD category `Mammals`.
2. **Read ENVO #1029 before filing.** The same request was made in 2020 and closed without the class being created; whatever the objection was, a new request that does not address it will meet it again.

**Record disposition** — consistent with the existing note and #114/#116:

```
identity      : minted, habitatmech:GOLD.cd0b0940e5
parent        : ENVO:01001002  'animal-associated environment'   (relation: parent)
xref          : NCBITaxon:9606 'Homo sapiens'                    (relation: xref)
xref          : MIXS:0016003   'HumanAssociated'                 (relation: xref)
status        : CONFIRM_UNGROUNDED + ENVO term-request candidate
```

Note that `ENVO:01001000` is currently also on the record as a nearest-broader term; once `ENVO:01001002` is asserted as the parent it is redundant, since it is the genus's own superclass.

One procedural point: filing anything with ENVO is an outward-facing submission, so it needs your explicit go-ahead for that specific request — this report stops at preparing it.

## Citations

1. https://gold.jgi.doe.gov/ecosystem_classification
2. https://academic.oup.com/nar/article/47/D1/D649/5144132
3. https://academic.oup.com/nar/article/43/D1/D1099/2439522
4. https://academic.oup.com/nar/article/50/D1/D741/6414049
5. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002
6. https://link.springer.com/article/10.1186/2041-1480-4-43
7. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035502/
8. https://genomicsstandardsconsortium.github.io/mixs/0016003/
9. https://github.com/EnvironmentOntology/envo/issues/1029
10. https://www.science.org/doi/10.1126/science.1177486
11. https://www.nature.com/articles/nature11234
12. https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002533
13. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5143676/
14. https://www.nature.com/articles/nrmicro.2017.157
15. https://www.science.org/doi/10.1126/science.aaf3951
16. https://www.science.org/doi/10.1126/science.1155725
17. https://www.ebi.ac.uk/ols4/ontologies/envo
18. https://github.com/EnvironmentOntology/envo/wiki/Creating-good-definitions
19. https://www.nature.com/articles/s43705-022-00092-w
20. https://academic.oup.com/nar/article/49/D1/D723/5957166
21. https://academic.oup.com/nar/article/51/D1/D957/6786204
22. https://academic.oup.com/nar/article/53/D1/D748/7848838
23. https://academic.oup.com/nar/article/49/D1/D743/5998395
24. https://pmc.ncbi.nlm.nih.gov/articles/PMC10552293/