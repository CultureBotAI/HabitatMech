---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T00:21:31.044976'
end_time: '2026-08-18T00:28:16.518264'
duration_seconds: 405.47
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Echinodermata
  habitat_identifier: habitatmech:GOLD.e1f435d44b
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Invertebrates > Echinodermata'
  assertions: '21'
  parent_terms: (none)
  xrefs: FOODON:03412115
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term FOODON:03412115 'echinoderm' attached as a parent. Host-taxon reversal\
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
    \ not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.e1f435d44b)"
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
  web_search_requests: 10
  num_turns: 27
  total_cost_usd: 2.6447920000000003
  session_id: 1221d989-2b20-4dcc-8599-e04667a806b8
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 34
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Echinodermata
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.e1f435d44b
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Invertebrates > Echinodermata
- **Upstream assertion volume:** 21
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** FOODON:03412115

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term FOODON:03412115 'echinoderm' attached as a parent. Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it — the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE while its own child Porifera > Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM — a phylum is a class of organisms, not a place — so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.e1f435d44b)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Echinodermata** as a microbial habitat, with citations.

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

# Echinodermata as a microbial habitat — definition research

**Target:** `habitatmech:GOLD.e1f435d44b` · label *Echinodermata* · category HOST_ASSOCIATED · UNGROUNDED
**Source path:** GOLD `Host-associated > Invertebrates > Echinodermata` (21 upstream assertions)
**Upstream xref:** `FOODON:03412115` *echinoderm*

---

## Proposed definition

> An **environment associated with an aquatic invertebrate** which **is determined by a living or dead marine animal of the phylum Echinodermata, comprising the body surface and subcuticular space, the gut lumen and its contents, and the coelomic fluid that such an animal presents to microorganisms**.

Genus CURIE: `ENVO:01001176` (*environment associated with an aquatic invertebrate*).
Taxon term `NCBITaxon:7586` / `FOODON:03412115` → `relation: xref`, per the #99/#114 disposition.

**One-sentence adequacy check:** the sentence holds, but only because the compartment list is enumerative rather than a genuine differentia. If the corpus later mints per-compartment children (echinoderm gut, echinoderm coelomic fluid, echinoderm surface), the enumeration should be dropped from this definition and pushed down. Flagging that now is more useful than a longer sentence — see §3.

---

## 1. What the concept denotes

**The reading the data means.** The GOLD path is `Host-associated > Invertebrates > Echinodermata`, i.e. the *Ecosystem Category* is `Invertebrates` and the *Ecosystem Type* slot is filled by a host phylum name. GOLD's five-level scheme (Ecosystem → Ecosystem Category → Ecosystem Type → Ecosystem Subtype → Specific Ecosystem) puts the host organism at the top of the host-associated branch and organ/tissue below it, e.g. `Host-associated → mammals → digestive system → foregut → rumen` ([GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification); [Mukherjee et al. 2019, *NAR* 47:D649](https://doi.org/10.1093/nar/gky977); [Mukherjee et al. 2023, *NAR* 51:D957](https://doi.org/10.1093/nar/gkac974)). So this record denotes **the whole echinoderm host as a place a microbe lives, with no organ specified** — samples classified here are ones where the recorded provenance is "from an echinoderm" and nothing finer.

**The physical thing sampled.** In practice, material assigned to this concept comes from one of four echinoderm compartments, each demonstrably microbially distinct:

| Compartment | What it is | Evidence |
|---|---|---|
| Gut lumen / digesta / faeces | Contents of the digestive tract, incl. ingested sediment or algae | [Yamazaki et al. 2016, *Sci Rep* 6:21631](https://doi.org/10.1038/srep21631); [Gao et al. 2014, *PLoS ONE* 9:e100092](https://doi.org/10.1371/journal.pone.0100092) |
| Gut tissue / epithelium | Mucosa, distinct from digesta in the same animal | [Hakim et al. 2019, *Microorganisms* 7:35](https://doi.org/10.3390/microorganisms7020035) |
| Coelomic fluid and coelomocytes | The fluid filling the main body cavity | [Vergnes et al. 2025, *Biology* 14:430](https://doi.org/10.3390/biology14040430) |
| Body surface / subcuticular space | Extracellular space beneath the epidermal cuticle | [Holland & Nealson 1978, *Acta Zool* 59:169–185](https://doi.org/10.1111/j.1463-6395.1978.tb01031.x); [Kelly & McKenzie 1995, *Mar Biol* 123:741–756](https://doi.org/10.1007/BF00349117) |

**Boundary — inside the concept:** any of the above compartments of any member of Echinodermata (Crinoidea, Asteroidea, Ophiuroidea, Echinoidea, Holothuroidea), at any life stage including planktonic larvae, and whether wild-caught or aquacultured.

**Boundary — outside / neighbouring:**

- **Ambient seawater and sediment around the animal.** These are the environmental reservoir, not the host habitat, and are consistently *more* diverse than the host: gut OTU richness in three tropical holothurians was 1,628–2,489 vs 4,162 in their habitat sediment (p < 0.01) ([Zhang et al. 2023, *Diversity* 15:855](https://doi.org/10.3390/d15070855)); coelomic-fluid communities shared only 12.7% of OTUs with ambient seawater ([Vergnes et al. 2025](https://doi.org/10.3390/biology14040430)).
- **Echinoderm-derived food products.** `FOODON:00003318` *echinoderm food product* and the EFSA FoodEx2 classes (`FOODON:03542570/71/72`) are processed food, a different habitat category.
- **Holothurian digestive tract specifically.** ENVO already names this (`ENVO:01001187`); it is a *child*, not this concept.
- **Sea star wasting disease.** A disease state, not a habitat — see §6.

**Ambiguity:** minimal. "Echinodermata" is unambiguous as a taxon name. The only real ambiguity is *compartment underspecification*, which is inherent to the GOLD level and is not a reason to split the concept.

---

## 2. Genus — the broader kind

**Recommended genus: `ENVO:01001176` — *environment associated with an aquatic invertebrate***

> "An environment which has its properties and composition largely determined by the presence of a metazoan which lacks a vetebral column and which has a habitat that is found in an aquatic environmental system." *(verbatim from ENVO via OLS4; note the typo `vetebral` is in the source. xref `MEO_0000871`.)*

This is the tightest existing fit. It is exact on both conditions — echinoderms are invertebrates, and the phylum is **exclusively marine, with no freshwater or terrestrial members** ([Digital Atlas of Ancient Life, Echinodermata](https://www.digitalatlasofancientlife.org/learn/echinodermata/); [OpenStax/Lumen, *Phylum Echinodermata*](https://courses.lumenlearning.com/wm-biology2/chapter/phylum-echinodermata/)) — so every echinoderm-associated environment is necessarily an aquatic-invertebrate-associated one. It sits under `ENVO:01001002` *animal-associated environment* and `ENVO:01001055`, and **currently has no children in ENVO** (verified: `descendants` and `hierarchicalDescendants` both return zero).

**Precedent for phylum-level granularity:** ENVO already carries `ENVO:01001179` *cnidarian-associated environment* — "An environmental system determined by a cnidarian or part of a cnidarian" — asserted directly under `ENVO:01001002`. That is exactly the shape this term request would take for a second invertebrate phylum. (Verified via OLS4 `parents`; it is *not* under `ENVO:01001176`, so a term request should say which parent it wants and why.)

### Near-misses and why each fails

| Term | Why it is not a match |
|---|---|
| `ENVO:01001002` *animal-associated environment* — "An environmental system determined by an animal." | Correct kind, far too broad. Grounding here loses the host phylum, which is the only information the source path carries. |
| `ENVO:01001055` *environment associated with an animal part or small animal* | Asserts **part-hood or small size**. The source concept is whole organisms across five classes spanning millimetre brittle stars to metre-long holothurians; the assertion is not supported. |
| `ENVO:01001176` *environment associated with an aquatic invertebrate* | **The genus, not the match.** Broader by many phyla — it equally covers the sponge-, cnidarian-, mollusc-, annelid- and ascidian-associated concepts that already exist as sibling records in this corpus. |
| `ENVO:01001187` *holothurian digestive tract* — "A digestive tract environment which has its properties and dynamics determined by the digestive tract of an echinoderm from the class Holothuroidea." | Narrower on **two** axes at once: one class of five, and one organ. It is the closest ENVO comes to naming an echinoderm habitat, and it is the strongest single piece of evidence that ENVO has *not* named the phylum-level concept. |
| `FOODON:03412115` *echinoderm* — "the common name given to any member of the phylum Echinodermata of marine animals…" | An **organism class in a food vocabulary**, not an environment. Keep as `relation: xref` (#99), never as identity or `parent`. |
| `NCBITaxon:7586` *Echinodermata*; `SNOMED:106903008` *Phylum Echinodermata*; `MeSH:D004447` | Taxonomic groupings — a class of organisms, not a place. Same disposition. |
| `UBERON:0009855` *echinoderm gastric caecum*; `UBERON:0008248` *echinoderm pyloric cecum*; `UBERON:0008251` *water vascular system*; `BTO:0002856` *coelomocyte* | Anatomical **parts**. Under the repo's part/whole rule these would correctly ground *narrower* habitat concepts (echinoderm gut, coelom) — they cannot ground the whole-organism concept. |

**Conclusion: no existing term names this concept.** CONFIRM_UNGROUNDED with `ENVO:01001176` as `parent` and `FOODON:03412115` / `NCBITaxon:7586` as `xref` is the defensible disposition, plus a term request for *echinoderm-associated environment*.

---

## 3. Differentia — what distinguishes it

Siblings under the genus are the other invertebrate-phylum-associated environments already in this corpus (Porifera, Cnidaria, Mollusca/bivalves, Annelida, Arthropoda-crustaceans, Ascidiacea, Nematoda). The separating properties, in decreasing order of how well they are attested:

**(a) Host identity — the primary differentia.** The host is a member of Echinodermata: a pentaradially symmetric deuterostome with a calcareous (high-Mg calcite) endoskeleton of ossicles and a **water vascular system**, the phylum's diagnostic character, comprising a ring canal, radial canals, tube feet and a madreporite ([Lumen/OpenStax, *Phylum Echinodermata*](https://courses.lumenlearning.com/wm-biology2/chapter/phylum-echinodermata/); [Digital Atlas of Ancient Life](https://www.digitalatlasofancientlife.org/learn/echinodermata/)). Five extant classes; WoRMS organises them as subphyla Crinozoa, Asterozoa, Echinozoa ([WoRMS AphiaID 1806](https://www.marinespecies.org/aphia.php?p=taxdetails&id=1806)).

**(b) Physical setting: exclusively marine and predominantly benthic.** This is the differentia that separates echinoderm-associated environments from, e.g., insect- or nematode-associated ones, and it is a hard constraint rather than a tendency — no freshwater or terrestrial echinoderms are known (sources as in §2). Salinity, temperature and depth of the surrounding environment therefore always fall in the marine range.

**(c) A subcuticular extracellular symbiont niche that is a phylum-level peculiarity.** Bacteria living **beneath the epidermal cuticle** were first described by [Holland & Nealson (1978), *Acta Zool* 59:169–185](https://doi.org/10.1111/j.1463-6395.1978.tb01031.x) and have since been reported from all five extant classes. Quantitatively: subcuticular bacteria were found in **17 of 19 brittlestar species** surveyed, at **3.7 × 10⁸ – 4.6 × 10⁹ cells per gram ash-free arm tissue**, with morphology tracking host phylogeny rather than host ecology ([Kelly & McKenzie 1995, *Mar Biol* 123:741–756](https://doi.org/10.1007/BF00349117); [McKenzie & Kelly 1994, *Mar Biol* 120:65–80](https://doi.org/10.1007/BF00381943)). The *Ophiactis balli* symbiont is a distinct alphaproteobacterial lineage, separate in origin from other marine symbiont clades ([Burnett & McKenzie 1997, *Appl Environ Microbiol* 63:1721–1724](https://doi.org/10.1128/aem.63.5.1721-1724.1997)). A subcuticular symbiont is universal in the crown-of-thorns starfish *Acanthaster* across the Indo-Pacific ([Høj et al. 2020, *Microbiome* 8:60](https://doi.org/10.1186/s40168-020-00880-3)). *Caveat:* [Carrier & Reitzel (2020), *Front Ecol Evol* 7:509](https://doi.org/10.3389/fevo.2019.00509) tabulate subcuticular bacteria in **developmental stages** from only three asteroids, one echinoid and one ophiuroid — the all-five-classes claim is for adults; do not merge the two.

**(d) Coelomic fluid as a high-load internal microbial habitat.** Unlike vertebrate blood, echinoderm coelomic fluid carries a resident community that is largely not shared with seawater. [Vergnes et al. (2025), *Biology* 14:430](https://doi.org/10.3390/biology14040430) (16 Apr 2025) sampled *Holothuria forskali*, *Marthasterias glacialis* and *Sphaerechinus granularis* from one site over four time points across two years: Proteobacteria 54–70%; culturable loads 3.9 × 10⁴ CFU/mL (holothurian), 1.0 × 10³ (asteroid), 49 (echinoid) against 810 CFU/mL in seawater; **87.3% of OTUs not shared with ambient seawater**; a cross-class core of 10 families / 16 OTUs (Comamonadaceae, Pseudoalteromonadaceae, Oxalobacteraceae, Vibrionaceae).

**(e) Strong internal compartmentalisation — the reason (a) alone is not enough.** *Strongylocentrotus purpuratus* gut **tissue** is dominated by Epsilonproteobacteria (*Arcobacter*, *Sulfurimonas*) while gut **digesta** from the same animals is dominated by *Psychromonas*, *Propionigenium* and Flavobacteriales ([Hakim et al. 2019, *Microorganisms* 7:35](https://doi.org/10.3390/microorganisms7020035)). In *Holothuria glaberrima*, the anterior intestine is Proteobacteria 61% / Bacteroidetes 22%, the posterior intestine Firmicutes 48% / Bacteroidetes 35% ([Pagán-Jiménez et al. 2019, *PLoS ONE* 14:e0208011](https://doi.org/10.1371/journal.pone.0208011)). In *Paracentrotus lividus* and *Arbacia lixula*, faeces cluster apart from coelomic fluid and coelomocytes, which overlap ([Front Mar Sci 2025, 12:1615711](https://doi.org/10.3389/fmars.2025.1615711)). **This is my inference, not a source's claim:** because the between-compartment difference is as large as the between-species difference, the definition should name the compartments it covers rather than imply a single homogeneous milieu — and it is why an intermediate per-compartment layer will eventually be wanted.

**(f) Characteristic function — dietary complementation of a low-enzyme host.** Sea urchins have limited innate gut digestive enzymes, and the microbiota supplies degradation of complex polysaccharides and cellulose ([Zheng et al. 2024, *Aquaculture Research* 2024:7363987](https://doi.org/10.1155/2024/7363987)). N₂ fixation in the sea-urchin gut is long-established and widespread across species and latitudes, confirmed by ¹⁵N incorporation ([Guerinot & Patriquin 1981, *Mar Biol* 62:197–207](https://doi.org/10.1007/BF00388183); [Guerinot & Patriquin 1981, *Can J Microbiol* 27:311–317](https://doi.org/10.1139/m81-048)), and led to the description of *Vibrio diazotrophicus* ([Guerinot et al. 1982, *IJSB* 32:350–357](https://doi.org/10.1099/00207713-32-3-350)); *nifH* has now been recovered from urchin intestinal communities on a seaweed diet ([FEMS Microbiol Ecol 2025, 101:fiaf006](https://doi.org/10.1093/femsec/fiaf006)). Deposit-feeding holothurians ingest sediment yet assemble a gut community markedly less diverse than that sediment (Zhang et al. 2023; Gao et al. 2014, above), i.e. the host selects rather than passively accumulates. **Do not put (f) in the definition sentence** — it is a property of the microbiota, not of the place, and it is class-specific rather than phylum-wide.

---

## 4. Sources

Ordered as cited. All claims above are attributed; the two sentences that are my own inference are marked inline in §1 (boundary drawing) and §3(e).

- Mukherjee A. *et al.* (2019) Genomes OnLine Database (GOLD) v.7. *Nucleic Acids Research* 47:D649–D659. https://doi.org/10.1093/nar/gky977
- Mukherjee A. *et al.* (2023) Twenty-five years of GOLD: v.9. *Nucleic Acids Research* 51:D957–D963. https://doi.org/10.1093/nar/gkac974
- JGI GOLD Ecosystem Classification. https://gold.jgi.doe.gov/ecosystem_classification (accessed 18 Aug 2026)
- Buttigieg P.L. *et al.* (2016) The environment ontology in 2016. *J Biomed Semantics* 7:57. https://doi.org/10.1186/s13326-016-0097-6
- Buttigieg P.L. *et al.* (2013) The environment ontology. *J Biomed Semantics* 4:43. https://doi.org/10.1186/2041-1480-4-43
- ENVO term records retrieved from EBI OLS4, 18 Aug 2026: `ENVO:01001176`, `ENVO:01001002`, `ENVO:01001055`, `ENVO:01001179`, `ENVO:01001187`. https://www.ebi.ac.uk/ols4/ontologies/envo
- FoodOn `FOODON:03412115` via OLS4. https://www.ebi.ac.uk/ols4/ontologies/foodon
- WoRMS, *Echinodermata* AphiaID 1806. https://www.marinespecies.org/aphia.php?p=taxdetails&id=1806
- Digital Atlas of Ancient Life, *Echinodermata*. https://www.digitalatlasofancientlife.org/learn/echinodermata/
- OpenStax/Lumen Learning, *Phylum Echinodermata*. https://courses.lumenlearning.com/wm-biology2/chapter/phylum-echinodermata/
- Holland N.D. & Nealson K.H. (1978) *Acta Zoologica* 59:169–185. https://doi.org/10.1111/j.1463-6395.1978.tb01031.x
- McKenzie J.D. & Kelly M.S. (1994) *Marine Biology* 120:65–80. https://doi.org/10.1007/BF00381943
- Kelly M.S. & McKenzie J.D. (1995) *Marine Biology* 123:741–756. https://doi.org/10.1007/BF00349117
- Burnett W.J. & McKenzie J.D. (1997) *Appl Environ Microbiol* 63:1721–1724. https://doi.org/10.1128/aem.63.5.1721-1724.1997
- Høj L. *et al.* (2020) *Microbiome* 8:60. https://doi.org/10.1186/s40168-020-00880-3
- Carrier T.J. & Reitzel A.M. (2020) Symbiotic life of echinoderm larvae. *Front Ecol Evol* 7:509. https://doi.org/10.3389/fevo.2019.00509
- Vergnes A. *et al.* (2025) The cœlomic microbiota among three echinoderms. *Biology* 14:430, 16 Apr 2025. https://doi.org/10.3390/biology14040430 (PMC12024532)
- Hakim J.A. *et al.* (2019) *Microorganisms* 7:35. https://doi.org/10.3390/microorganisms7020035
- Hakim J.A. *et al.* (2015) Epsilonproteobacteria in *Lytechinus variegatus*. PMC4602345. https://pmc.ncbi.nlm.nih.gov/articles/PMC4602345/
- Pagán-Jiménez M. *et al.* (2019) Intestinal microbiota of *Holothuria glaberrima*. *PLoS ONE* 14:e0208011. https://doi.org/10.1371/journal.pone.0208011
- Ortiz-Cruz *et al.* (2025) *H. glaberrima* intestinal microbiome, ITS + 16S. *Microbiol Resour Announc* https://doi.org/10.1128/mra.00293-25 (PMC12243471)
- Gao F. *et al.* (2014) *Apostichopus japonicus* gut vs. sediment. *PLoS ONE* 9:e100092. https://doi.org/10.1371/journal.pone.0100092
- Yamazaki Y. *et al.* (2016) *Scientific Reports* 6:21631. https://doi.org/10.1038/srep21631
- Zhang X. *et al.* (2023) Three tropical sea cucumbers vs. sediment. *Diversity* 15:855. https://doi.org/10.3390/d15070855
- Zheng *et al.* (2024) Gut microbiota in sea urchin digestion. *Aquaculture Research* 2024:7363987. https://doi.org/10.1155/2024/7363987
- Guerinot M.L. & Patriquin D.G. (1981) *Marine Biology* 62:197–207. https://doi.org/10.1007/BF00388183
- Guerinot M.L. & Patriquin D.G. (1981) *Can J Microbiol* 27:311–317. https://doi.org/10.1139/m81-048
- Guerinot M.L. *et al.* (1982) *Vibrio diazotrophicus* sp. nov. *Int J Syst Bacteriol* 32:350–357. https://doi.org/10.1099/00207713-32-3-350
- Fernández-Boo *et al.* (2025) Sea urchin holobionts. *Front Mar Sci* 12:1615711. https://doi.org/10.3389/fmars.2025.1615711
- Ruiz *et al.* (2025) Urchin intestinal communities and N-fixing symbionts. *FEMS Microbiol Ecol* 101:fiaf006. https://doi.org/10.1093/femsec/fiaf006 (PMC11797059)
- Prentice *et al.* (2025) *Vibrio pectenicida* FHCF-3 causes sea star wasting disease. *Nat Ecol Evol.* https://doi.org/10.1038/s41559-025-02797-2
- McCracken A.R. *et al.* (2023) Microbial dysbiosis precedes SSWD in *Pycnopodia helianthoides*. *Front Mar Sci* 10:1130912. https://doi.org/10.3389/fmars.2023.1130912
- Lloyd M.M. & Pespeni M.H. (2018) Microbiome shifts with SSWD. *Sci Rep* 8:16476. https://doi.org/10.1038/s41598-018-34697-w
- Wahltinez S.J. *et al.* (2023) Coelomic fluid of asteroid echinoderms. *Vet Pathol* 60:547–559. https://doi.org/10.1177/03009858231185107

---

## 5. Synonyms and what not to conflate

**Synonyms / names in real use** (candidates for `synonyms`):

- *echinoderm-associated environment* — the ENVO-house-style form, matching `cnidarian-associated environment`; **recommended as the term-request label**
- *echinoderm-associated habitat*
- *echinoderm host* / *echinoderm host environment*
- *echinoderm holobiont* — widely used in the 2020s literature (Carrier & Reitzel 2020; Front Mar Sci 2025), but note it denotes host + microbiota **as a biological unit**, not the environment; acceptable as a related synonym, not an exact one
- *Echinodermata* — the bare source label; keep as the GOLD-attested form

**Do NOT conflate with:**

| Not the same | Why |
|---|---|
| `NCBITaxon:7586` / `FOODON:03412115` / `SNOMED:106903008` **Echinodermata** | The taxon is a class of organisms, not a place. `relation: xref`, never identity or `parent`. |
| `ENVO:01001187` *holothurian digestive tract* | One class, one organ — a child. |
| `FOODON:00003318` *echinoderm food product*, `FOODON:03542570/71/72` | Food commodity classes; a different habitat category. |
| Marine sediment / seawater surrounding the animal | The environmental reservoir. Shown quantitatively distinct from the host communities (Zhang 2023; Gao 2014; Vergnes 2025). |
| "Sea urchin barren" | A benthic **habitat state** created by urchin grazing — an environmental (not host-associated) concept. |
| `UBERON:0008264` *echinopluteus larval stage* | A life stage of the host organism, not a habitat term; under the repo's own rule (#112) this is a whole organism at a stage. |
| Sea star wasting disease / SSWD | A disease state — see §6. |
| Coelomocytes (`BTO:0002856`, `UBERON` cell terms) | Host cells that may harbour microbes; a cell type, not the concept. |
| Aquaculture ponds/tanks rearing *Apostichopus japonicus* | Engineered environment; the animal in it is this concept, the water is not. |

---

## 6. Should this be a term at all?

**Yes.** This is a genuine microbial habitat, and the argument is stronger here than for many host-taxon records:

1. **Microbes demonstrably live in and on echinoderms**, in at least four structurally distinct compartments, with community composition distinct from the surrounding water and sediment (87.3% of coelomic OTUs unshared with seawater; gut communities less diverse than the sediment the animal eats). It is a *place*, and the host selects its occupants.
2. **A phylum-restricted niche exists** — the subcuticular space is an echinoderm-specific extracellular habitat with no close analogue in the sibling phyla, at loads up to ~10⁹ cells g⁻¹ tissue.
3. **ENVO already models the pattern** at exactly this granularity, both at the phylum (`ENVO:01001179` cnidarian-associated environment) and at a narrower echinoderm compartment (`ENVO:01001187` holothurian digestive tract). A phylum-level echinoderm term is the obvious gap between them.
4. **The corpus already treats sibling invertebrate phyla as habitats** (Porifera/Sponge, Nematoda, Cnidaria, Annelida, Ascidiacea, bivalves), so `NOT_APPLICABLE` here would reintroduce exactly the #114 inconsistency the curator's note is unwinding.

**Two caveats a curator should record rather than suppress:**

- **The concept is compartment-underspecified by construction.** It aggregates gut digesta, gut tissue, coelomic fluid and body surface, which differ from each other as much as they differ between host species (§3e). That is a property of the GOLD level, not a defect in the record, but it means `assertion_count: 21` should not be read as 21 samples of one milieu.
- **Disease-context material is not this concept.** SSWD studies sample sea star coelomic fluid, and the disease now has a proven bacterial aetiology — *Vibrio pectenicida* strain FHCF-3, satisfying causation by culture and re-injection ([Prentice et al. 2025, *Nat Ecol Evol*](https://doi.org/10.1038/s41559-025-02797-2)). The **fluid** is this habitat; the **disease** is a process/state and would be `NOT_APPLICABLE` if it ever appears as its own source concept.

**Recommended disposition:** `CONFIRM_UNGROUNDED`, `parent_habitats: ENVO:01001176` (*environment associated with an aquatic invertebrate*), `relation: xref` on `FOODON:03412115` (*echinoderm*) and optionally `NCBITaxon:7586`, plus a term request for **echinoderm-associated environment** under `ENVO:01001176`, citing `ENVO:01001179` as the pattern and `ENVO:01001187` as evidence of the gap.

## Citations

1. https://gold.jgi.doe.gov/ecosystem_classification
2. https://doi.org/10.1093/nar/gky977
3. https://doi.org/10.1093/nar/gkac974
4. https://doi.org/10.1038/srep21631
5. https://doi.org/10.1371/journal.pone.0100092
6. https://doi.org/10.3390/microorganisms7020035
7. https://doi.org/10.3390/biology14040430
8. https://doi.org/10.1111/j.1463-6395.1978.tb01031.x
9. https://doi.org/10.1007/BF00349117
10. https://doi.org/10.3390/d15070855
11. https://www.digitalatlasofancientlife.org/learn/echinodermata/
12. https://courses.lumenlearning.com/wm-biology2/chapter/phylum-echinodermata/
13. https://www.marinespecies.org/aphia.php?p=taxdetails&id=1806
14. https://doi.org/10.1007/BF00381943
15. https://doi.org/10.1128/aem.63.5.1721-1724.1997
16. https://doi.org/10.1186/s40168-020-00880-3
17. https://doi.org/10.3389/fevo.2019.00509
18. https://doi.org/10.1371/journal.pone.0208011
19. https://doi.org/10.3389/fmars.2025.1615711
20. https://doi.org/10.1155/2024/7363987
21. https://doi.org/10.1007/BF00388183
22. https://doi.org/10.1139/m81-048
23. https://doi.org/10.1099/00207713-32-3-350
24. https://doi.org/10.1093/femsec/fiaf006
25. https://doi.org/10.1186/s13326-016-0097-6
26. https://doi.org/10.1186/2041-1480-4-43
27. https://www.ebi.ac.uk/ols4/ontologies/envo
28. https://www.ebi.ac.uk/ols4/ontologies/foodon
29. https://pmc.ncbi.nlm.nih.gov/articles/PMC4602345/
30. https://doi.org/10.1128/mra.00293-25
31. https://doi.org/10.1038/s41559-025-02797-2
32. https://doi.org/10.3389/fmars.2023.1130912
33. https://doi.org/10.1038/s41598-018-34697-w
34. https://doi.org/10.1177/03009858231185107