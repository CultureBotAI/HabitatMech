---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T21:15:17.518740'
end_time: '2026-08-17T21:22:42.802680'
duration_seconds: 445.28
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Ascidians
  habitat_identifier: habitatmech:GOLD.34c28836da
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Tunicates > Ascidians'
  assertions: '79'
  parent_terms: ENVO:01001002
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Nearest
    broader term ENVO:01001002 ''animal-associated environment'' attached as a parent.
    Ascidians as host. BTO:0000090 is a biological-source term rather than a habitat;
    treated as the other host clades are, parented to animal-associated environment.
    ENVO term request. (source concept habitatmech:GOLD.34c28836da)'
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
  web_search_requests: 15
  num_turns: 23
  total_cost_usd: 3.046614
  session_id: fd0e81c5-4757-4c92-aa10-606fd7f8dbcb
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 33
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Ascidians
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.34c28836da
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Tunicates > Ascidians
- **Upstream assertion volume:** 79
- **Nearest broader term already on the record:** ENVO:01001002
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term ENVO:01001002 'animal-associated environment' attached as a parent. Ascidians as host. BTO:0000090 is a biological-source term rather than a habitat; treated as the other host clades are, parented to animal-associated environment. ENVO term request. (source concept habitatmech:GOLD.34c28836da)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Ascidians** as a microbial habitat, with citations.

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

# Ascidians (`habitatmech:GOLD.34c28836da`) — definition research

> **Proposed definition:** An environment associated with an aquatic invertebrate which is determined by an ascidian (Chordata: Tunicata: Ascidiacea) — a sessile, benthic, filter-feeding tunicate — and which comprises the animal's cellulosic tunic, its seawater-processing branchial sac and gut, and its internal cavities and fluids.

**Proposed label for an ENVO request:** *ascidian-associated environment* (exact synonym: *sea squirt-associated environment*), by direct analogy with the sole existing sibling, `ENVO:01001179` *cnidarian-associated environment*.

---

## 1. What the concept denotes

**The place a sample comes from.** An individual ascidian — or, for the ~60% of described species that are colonial ([Shenkar & Swalla 2011](https://doi.org/10.1371/journal.pone.0020657)), a colony — considered as the physical setting a microbial community occupies. The material a curator should picture behind an attestation on this record is one of:

- **the tunic**, a rubbery-to-cartilaginous extracellular matrix built primarily of cellulose (tunicin) that encloses the whole animal and, in colonial forms, the whole colony ([UBERON:0011302 definition](https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON:0011302); [Britannica, "Sea squirt"](https://www.britannica.com/animal/sea-squirt));
- **the branchial sac / pharyngeal basket**, through which the animal actively pumps seawater to filter suspended plankton, and which is therefore continuously loaded with seawater-derived cells ([Britannica](https://www.britannica.com/animal/sea-squirt); [Hutchings et al. 2024](https://doi.org/10.1111/1758-2229.13242));
- **the gut and hepatic/digestive gland** ([Dishaw et al. 2014](https://doi.org/10.1371/journal.pone.0093386));
- **internal cavities and fluids** — peribranchial and cloacal cavities, hemolymph and blood cells — including the intracellular compartments in which reduced-genome endosymbionts live ([Schofield et al. 2015](https://doi.org/10.1111/1462-2920.12908); [Frontiers in Microbiology 2012](https://doi.org/10.3389/fmicb.2012.00402));
- or, most commonly for genome-sequence records, **a whole homogenised specimen** with no compartment recorded.

**Inside the boundary:** solitary, social and colonial ascidians across the three orders in current use (Aplousobranchia, Phlebobranchia, Stolidobranchia — [WoRMS: Ascidiacea](https://www.marinespecies.org/aphia.php?p=taxdetails&id=1839)); all of the compartments above; obligate symbionts, facultative associates and transient filtered cells alike; and the colony-level structures (common tunic, shared cloacal cavity) of compound forms.

**Just outside the boundary — neighbouring concepts:**

| Neighbour | Why it is a different concept |
|---|---|
| Pelagic tunicates — Thaliacea (salps, doliolids, pyrosomes) and Appendicularia (larvaceans) | Free-swimming, not benthic; larvacean mucous "houses" are discarded into the water column and become marine snow, a physically distinct habitat. These sit under the *parent* GOLD node "Tunicates", not under "Ascidians". |
| The seawater the animal filters | `ENVO:00002010` *seawater*. Ascidian microbiota are demonstrably differentiated from ambient seawater, with some rare seawater taxa enriched 200–700-fold inside the tunic ([Erwin et al. 2014](https://doi.org/10.1038/ismej.2013.188)). |
| The fouling community / hard substratum the ascidian is attached to | Ascidians are themselves conspicuous epibionts on pilings, hulls, shells and aquaculture gear ([Britannica](https://www.britannica.com/animal/sea-squirt)). A biofilm scraped from a dock next to an ascidian is a built-environment marine biofouling sample, not this concept. |
| The outer tunic *surface* biofilm | Genuinely a boundary case. Some acidic-tunic species carry no macroscopic epibionts at all ([Stoecker 1980, *MEPS* 3:257–265](https://www.int-res.com/articles/meps/3/m003p257.pdf); [Hirose et al. 2001](https://doi.org/10.2108/zsj.18.309)); most surveys sample the *inner* tunic deliberately to exclude surface contaminants. I would keep surface and matrix inside one concept unless GOLD ever splits them. |

**Is the label ambiguous?** Two readings exist and should be recorded rather than silently resolved:

1. **Ascidiacea sensu stricto** — the sessile benthic tunicates. This is what the source path means: GOLD nests `Ascidians` *under* `Tunicates`, so the parent node already carries the broad tunicate reading and the child must be the narrower one.
2. **"Ascidian" used loosely for any tunicate** — common in the natural-products and biofouling literature. This reading is excluded by the path structure.

A third, weaker ambiguity: whether an attestation means "sampled from an ascidian" or "an ascidian symbiont's genome". With 79 upstream assertions counted as *organisms* (GOLD's unit), most are almost certainly isolate or metagenome-assembled genomes whose recorded isolation source is an ascidian host, without compartment resolution. **This is my inference from the assertion unit and volume, not something a source states.**

---

## 2. Genus — the broader kind

**Recommended genus: `ENVO:01001176` *environment associated with an aquatic invertebrate*.**

> "An environment which has its properties and composition largely determined by the presence of a metazoan which lacks a vetebral column and which has a habitat that is found in an aquatic environmental system." — [ENVO:01001176 via OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001176) (the "vetebral" typo is ENVO's, verbatim)

Ascidians satisfy this definition on its own terms: they are marine metazoans and they lack a vertebral column. The one thing a curator should note in the record is that ascidians are *chordates* — so "invertebrate" here is the paraphyletic convenience grouping, exactly as ENVO's wording ("lacks a vertebral column") allows. This is a tighter and better-supported genus than the `ENVO:01001002` currently on the record.

I verified the subclass structure directly. `ENVO:01001002` *animal-associated environment* ("An environmental system determined by an animal") has exactly **three** asserted children: `ENVO:01001176`, `ENVO:01001179` *cnidarian-associated environment*, and `ENVO:01001829` *human settlement*. `ENVO:01001176` has **zero** children. So the branch is real but almost entirely undeveloped — the gap is genuine, not an artefact of a bad search. ([OLS4 children query, ENVO:01001002](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002))

### Near-misses and why each fails

| Candidate | Why it is not a match |
|---|---|
| `ENVO:01001002` *animal-associated environment* | Correct but too broad — it is the grandparent once `ENVO:01001176` is interposed. Currently on the record; recommend re-parenting. |
| `ENVO:01001179` *cnidarian-associated environment* | Sibling, not parent. Its existence is the **strongest precedent** for the requested term: ENVO already models a clade-level marine-invertebrate host as an environment, at exactly the granularity this concept needs. |
| `BTO:0000090` *ascidian* — "Any of a class (Ascidiacea) of solitary or colonial sessile tunicates that have an oral and an atrial siphon" ([OLS4](https://www.ebi.ac.uk/ols4/ontologies/bto/classes?obo_id=BTO:0000090)) | A biological-source / organism term, not a place. The curator's existing note has this right. Keep as `relation: xref` at most. |
| `FOODON:03414467` *ascidian* ([OLS4](https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?obo_id=FOODON:03414467)) | A food-source organism term (ascidians *are* eaten — *Halocynthia roretzi*, *Microcosmus* spp.). Grounding here would import a food-commodity assertion that no GOLD attestation makes. Not a habitat. |
| `NCBITaxon:7713` *Ascidiacea* | A taxon — a class of organisms, not a place. Per this repo's rule, belongs in `relation: xref`, and `NOT_APPLICABLE` would be the wrong disposition. |
| `UBERON:0011302` *tunicate tunic* | Fails on **both** axes simultaneously: anatomically **narrower** (excludes gut, branchial sac, hemolymph, whole-animal samples) and taxonomically **broader** (covers salps and larvaceans too). It is the right ground for a future `ascidian tunic` habitat if GOLD ever splits the node, but not for this one. |
| `UBERON:0009860` *ascidian digestive gland*, `UBERON:0009474` *ascidian ampulla*, and the other seven `ascidian *` UBERON terms | Parts, far narrower than the concept. Useful evidence that UBERON models ascidian anatomy but has no whole-organism-as-environment term. |

An OLS4 search for `ascidian` across ENVO, UBERON, PO, FOODON, BTO and NCBITaxon returned **19 hits and not one environmental class** — the ENVO hits are UBERON terms imported into ENVO's slice (e.g. `UBERON:0015228`), not ENVO-native environments. Nothing in ENVO names this concept.

---

## 3. Differentia — what distinguishes it from its siblings

Five properties, all observable or measurable, separate an ascidian-associated environment from other aquatic-invertebrate-associated environments (sponge, cnidarian, mollusc, echinoderm):

**a. A cellulose-based extracellular matrix as the principal habitat compartment.** The tunic is built primarily of tunicin, a cellulose — a polymer essentially unique among animals and one that a sponge's spongin/silica skeleton or a cnidarian's mesoglea does not provide ([UBERON:0011302](https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON:0011302); [FOODON:03414467 definition](https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?obo_id=FOODON:03414467)). It is the dominant sampled material in the ascidian microbiome literature.

**b. Sessile, benthic, attached to hard substrata, from the intertidal to the deep sea, in all seas** ([Britannica](https://www.britannica.com/animal/sea-squirt); [Shenkar & Swalla 2011](https://doi.org/10.1371/journal.pone.0020657)). This is precisely the property that separates the concept from its pelagic tunicate siblings.

**c. Active high-volume seawater filtration through a pharyngeal basket, producing a compartment gradient.** Compartments hold measurably distinct communities: in *Styela plicata* the tunic, branchial sac and gut microbiomes are each specialised, with the passive tunic differentiated from the branchial sac that actively traps particulates from seawater (Galià-Camps et al. 2023, as reported and reproduced in [Hutchings et al. 2024, *Environ Microbiol Rep*](https://doi.org/10.1111/1758-2229.13242)). A 2025 depuration study adds the hepatic gland as a further distinct compartment ([FEMS Microbiol Ecol 101:fiaf078](https://doi.org/10.1093/femsec/fiaf078)).

**d. Distinctive, often extreme physicochemistry — acidity and vanadium.**
- Tunic fluids in many species are strongly acidic. In *Phallusia nigra* the tunic interior measures pH ~1, stable at pH 1–2 for over five minutes after electrode insertion, with sulfate as the dominant anion (SO₄²⁻/Cl⁻ = 4.63); the acid is held in vacuolated tunic bladder cells concentrated just beneath the surface ([Hirose et al. 2001, *Zoological Science* 18(3):309–314](https://doi.org/10.2108/zsj.18.309)). A survey of 65 species across 11 families found bladder cells restricted to Didemnidae, Holozoinae, Diazoninae and Ascidiidae ([Hirose 2001, *Zoological Science* 18(5):723](https://doi.org/10.2108/zsj.18.723)). Across Bermudian ascidians, tunic acidity was significantly associated with habitat and with the absence of epibionts ([Stoecker 1980, *MEPS* 3:257–265](https://www.int-res.com/articles/meps/3/m003p257.pdf)).
- Phlebobranch ascidians hyperaccumulate vanadium in specialised blood cells (vanadocytes), where ~97.6% is V(III) at an internal pH of ~1.9 ([Michibata et al. 2002, *Microsc Res Tech*](https://doi.org/10.1002/jemt.10042)).

These make the ascidian host a selective chemical filter unlike any sibling host clade, though note the caveat: both acidity and vanadium are **clade-restricted, not universal** across Ascidiacea, so a definition should not assert them of the class as a whole.

**e. Characteristic, host-specific, and functionally distinctive microbiota.**
- 16S tag pyrosequencing of 42 Great Barrier Reef samples across 25 species recovered 3,217 OTUs from 19 described and 14 candidate phyla; 71% were rare and host-specific; symbiont community similarity tracked host relatedness; ammonia-oxidising Thaumarchaeota were present in 24 of 25 host species ([Erwin et al. 2014, *ISME J* 8(3):575–588](https://doi.org/10.1038/ismej.2013.188), PMID [24152714](https://pubmed.ncbi.nlm.nih.gov/24152714/)). Active nitrification inside colonial ascidian tissue had been shown earlier (PMID [18793310](https://pubmed.ncbi.nlm.nih.gov/18793310/)).
- The only known **obligate photosymbiosis in the phylum Chordata**: uncultivated *Prochloron* spp. — chlorophyll *b*-containing cyanobacteria, unusually large at 10–20 µm — fill the peribranchial and cloacal cavities of didemnid hosts (*Lissoclinum*, *Didemnum*, *Trididemnum*, *Diplosoma*) ([Frontiers in Microbiology 3:402, 2012](https://doi.org/10.3389/fmicb.2012.00402); [Donia et al. 2011, *PNAS* 108:E1423](https://doi.org/10.1073/pnas.1111712108)).
- Extreme genome-reduced intracellular symbiosis: *Candidatus* Endoecteinascidia frumentensis, a ~631 kb gammaproteobacterial genome in *Ecteinascidia turbinata* specialised for biosynthesis of the approved chemotherapeutic ET-743 / trabectedin ([Schofield et al. 2015, *Environ Microbiol*](https://doi.org/10.1111/1462-2920.12908), PMID [26013440](https://pubmed.ncbi.nlm.nih.gov/26013440/)).
- A reproducible core gut community, demonstrated across geographically disparate *Ciona intestinalis* populations ([Dishaw et al. 2014, *PLoS ONE* 9:e93386](https://doi.org/10.1371/journal.pone.0093386)), with germ-free *Ciona* available as an experimental system ([Leigh et al. 2016, *Front Microbiol* 7:2092](https://doi.org/10.3389/fmicb.2016.02092)).

**Note on paraphyly.** Ascidiacea is accepted by WoRMS as a class, but molecular phylogenies place Thaliacea within it, making it paraphyletic. This does **not** undermine the habitat concept: the grouping is coherent on exactly the properties a habitat definition uses — sessile, benthic, tunic-enclosed, hard-substratum-attached — which is why the definition above leads with those and not with a clade claim. *(This reconciliation is my inference; WoRMS states the classification, the phylogenetic caveat is standard in the literature.)*

---

## 4. Sources

Grouped by what they support. All DOIs/PMIDs verified resolvable during this research; where I could not confirm a primary DOI I say so.

**Concept scope, taxonomy, natural history**
- Shenkar N. & Swalla B.J. (2011) Global diversity of Ascidiacea. *PLoS ONE* 6(6):e20657. https://doi.org/10.1371/journal.pone.0020657 — ~3,000 described species (their verified list: 2,815); 60% colonial; all marine habitats, shallow to deep sea; Aplousobranchia most speciose.
- WoRMS / Ascidiacea World Database, Ascidiacea (AphiaID 1839). https://www.marinespecies.org/aphia.php?p=taxdetails&id=1839 — class, accepted; three orders in current use.
- Encyclopædia Britannica, "Sea squirt". https://www.britannica.com/animal/sea-squirt — sessility, branchial/atrial siphons, ciliary pumping, filter feeding, tadpole larva, solitary/social/compound forms.

**Ontology terms (all retrieved live from EBI OLS4, August 2026)**
- `ENVO:01001002` animal-associated environment — https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002
- `ENVO:01001176` environment associated with an aquatic invertebrate — https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001176
- `ENVO:01001179` cnidarian-associated environment — https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001179
- `UBERON:0011302` tunicate tunic; `BTO:0000090` ascidian; `FOODON:03414467` ascidian — all via https://www.ebi.ac.uk/ols4/
- ENVO issue #1029, "EnvO terms for host-associated samples" — https://github.com/EnvironmentOntology/envo/issues/1029 — background on how ENVO intends host-associated environments to be modelled.

**Microbial community structure**
- Erwin P.M., Pineda M.C., Webster N., Turon X., López-Legentil S. (2014) Down under the tunic. *ISME J* 8(3):575–588. https://doi.org/10.1038/ismej.2013.188
- Hutchings et al. (2024) Distinct microbial communities in an ascidian–crustacean symbiosis. *Environ Microbiol Rep* 16:e13242. https://doi.org/10.1111/1758-2229.13242 (PMC10881349)
- Galià-Camps et al. (2023), *Styela plicata* compartment-specific microbiomes — **DOI not verified in this pass**; cite via Hutchings et al. 2024, which reproduces the finding, until confirmed.
- Tianero M.D. et al. (2015) Species specificity of symbiosis and secondary metabolism in ascidians. *ISME J*. https://doi.org/10.1038/ismej.2014.152
- Casso M. et al. (2017) Introduced ascidians harbor highly diverse and host-specific symbiotic microbial assemblages. *Sci Rep* 7:11441. https://doi.org/10.1038/s41598-017-11441-4
- Casso M. et al. (2020) The microbiome of the worldwide invasive ascidian *Didemnum vexillum*. *Front Mar Sci* 7:201. https://doi.org/10.3389/fmars.2020.00201
- Depuration of a solitary ascidian… (2025) *FEMS Microbiol Ecol* 101:fiaf078. https://doi.org/10.1093/femsec/fiaf078 — first characterisation of the hepatic-gland microbiome.

**Symbionts and function**
- Schmidt E.W. et al. (2005) Patellamide A and C biosynthesis in *Prochloron didemni*. *PNAS* 102:7315–7320. https://doi.org/10.1073/pnas.0501424102
- Donia M.S. et al. (2011) Complex microbiome underlying secondary and primary metabolism in the tunicate–*Prochloron* symbiosis. *PNAS* 108:E1423. https://doi.org/10.1073/pnas.1111712108
- Kühl M. et al. (2012) Microenvironmental ecology of *Prochloron* in *Lissoclinum patella*. *Front Microbiol* 3:402. https://doi.org/10.3389/fmicb.2012.00402
- Schofield M.M. et al. (2015) Identification and analysis of the bacterial endosymbiont specialized for production of ET-743. *Environ Microbiol*. https://doi.org/10.1111/1462-2920.12908; PMID 26013440
- Martínez-García M. et al. (2008) Ammonia-oxidizing Crenarchaeota and nitrification inside the tissue of a colonial ascidian. PMID [18793310](https://pubmed.ncbi.nlm.nih.gov/18793310/)
- Dishaw L.J. et al. (2014) The gut of geographically disparate *Ciona intestinalis* harbors a core microbiota. *PLoS ONE* 9:e93386. https://doi.org/10.1371/journal.pone.0093386
- Leigh B.A., Liberti A., Dishaw L.J. (2016) Generation of germ-free *Ciona intestinalis*. *Front Microbiol* 7:2092. https://doi.org/10.3389/fmicb.2016.02092
- López-Legentil S. (2023) Ascidians and their microbial symbionts. *genesis*. https://doi.org/10.1002/dvg.23534 — current review framing.
- Symbiotic associations in ascidians: relevance for functional innovation and bioactive potential (2021) *Mar Drugs* 19:370. https://doi.org/10.3390/md19070370

**Physicochemistry**
- Hirose E., Yamashiro H., Mori Y. (2001) Properties of tunic acid in *Phallusia nigra*. *Zoological Science* 18(3):309–314. https://doi.org/10.2108/zsj.18.309
- Hirose E. (2001) Acid containers and cellular networks in the ascidian tunic. *Zoological Science* 18(5):723. https://doi.org/10.2108/zsj.18.723
- Stoecker D. (1980) Relationships between chemical defense and ecology in benthic ascidians. *Mar Ecol Prog Ser* 3:257–265. https://www.int-res.com/articles/meps/3/m003p257.pdf
- Michibata H. et al. (2002) Vanadocytes. *Microsc Res Tech*. https://doi.org/10.1002/jemt.10042

**Standards / source vocabulary**
- JGI GOLD Ecosystem Classification. https://gold.jgi.doe.gov/ecosystem_classification — five-level Ecosystem → Category → Type → Subtype → Specific Ecosystem; paths are sample-driven and revised periodically, and the published documentation does **not** enumerate the Tunicates/Ascidians node. I could not independently confirm the exact GOLD path from a public page; I am taking `Host-associated > Tunicates > Ascidians` from the record's own attestation.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**
- sea squirt (the dominant common name; recorded as a related synonym on `BTO:0000090`)
- ascidian / ascidians
- Ascidiacea (scientific class name)
- "ascidian holobiont", "ascidian host" (literature usage)
- "tunicate" — **broad synonym only**, and only when context makes the sessile reading clear
- Regional food names for the same animals: *hoya* / sea pineapple (*Halocynthia roretzi*), *piure* (*Microcosmus* spp.) — relevant to the FOODON near-miss, not to the habitat.

**Commonly but wrongly treated as the same thing**
- **Tunicata / Urochordata** — the subphylum, which also contains the pelagic Thaliacea and Appendicularia. Broader; in GOLD it is the explicit parent node.
- **Salps, doliolids, pyrosomes, larvaceans** — tunicates, not ascidians. A larvacean's discarded mucous house is a completely different microbial habitat.
- **The taxon *Ascidiacea* (`NCBITaxon:7713`)** — a class of organisms. The organism-as-host is a habitat; the taxon term is not. Keep as `relation: xref`.
- **`UBERON:0011302` tunicate tunic** — one compartment of one reading, and taxonomically broader. Not interchangeable with the host-level concept.
- **"Tunicate-associated bacteria" as a source label** — e.g. *Pseudoalteromonas tunicata* is named for a tunicate isolation but is a generalist marine surface coloniser; the name is not evidence of an ascidian-specific habitat.
- **Marine biofouling / dock-piling community** — ascidians are prominent members of it, but the fouling assemblage is a built-environment concept, not this one.
- **Sponge-associated environment** — the closest ecological analogue (sessile marine filter-feeder with dense, host-specific symbionts) and the reason ascidian data are often analysed alongside sponge data, but a different host phylum with a different matrix chemistry.

---

## 6. Should this be a term at all?

**Yes.** This is a habitat, and the current `CONFIRM_UNGROUNDED` + ENVO term request is the right disposition. Three points support it:

1. **It is a place, not a taxon claim.** The concept is an organism *acting as a host*: a physical, bounded, sampleable setting with its own materials (cellulose matrix, seawater-perfused branchial sac, gut lumen, hemolymph) and its own physicochemistry. What would not be a habitat is the taxon term `NCBITaxon:7713` — and that belongs in `relation: xref`, exactly as the repo's rule for host clades prescribes. `NOT_APPLICABLE` would be the wrong call: it says the concept is not a habitat, which is a stronger claim the evidence contradicts.

2. **It is the whole host, not a part.** Per the rule that a host's parts ground to anatomy terms while the whole organism keeps its own minted identity: `Ascidians` denotes the whole animal or colony, so it should keep `habitatmech:GOLD.34c28836da` and carry `UBERON:0011302` and `NCBITaxon:7713` as xrefs rather than grounding to either.

3. **The gap in ENVO is real and precedented.** `ENVO:01001002` has exactly three children and `ENVO:01001176` has none; the only clade-level marine-invertebrate host environment ENVO models is `ENVO:01001179` *cnidarian-associated environment*. An *ascidian-associated environment* term is the same pattern applied to a host clade with 79 upstream assertions, a class-wide microbiome literature, the phylum's only obligate photosymbiosis, and a clinically approved drug produced by one of its endosymbionts.

### Two concrete recommendations for the record

1. **Re-parent from `ENVO:01001002` to `ENVO:01001176`** *environment associated with an aquatic invertebrate*. It is a strictly tighter, still-defensible parent, and it is the genus the proposed definition starts from. Keep `ENVO:01001002` only if the curator prefers not to lean on ENVO's paraphyletic "invertebrate", in which case note the reason explicitly — because on ENVO's own wording ("lacks a vertebral column") ascidians do qualify.
2. **Add `NCBITaxon:7713` (Ascidiacea) and `UBERON:0011302` (tunicate tunic) as `relation: xref`**, not as parents. Neither is broader than this concept: the taxon is a class of organisms rather than a place, and the tunic is simultaneously a narrower compartment and a broader taxonomic scope.

### One thing that will need saying if GOLD ever splits this node

If compartment-resolved children ever appear (`Ascidians > Tunic`, `> Gut`, `> Branchial sac`), *those* ground cleanly — the tunic to `UBERON:0011302`, the gut to `UBERON:0001555`. The reason this parent node cannot be grounded is precisely that it is compartment-agnostic. Worth recording in the note, because it is the question a reviewer will ask.

## Citations

1. https://doi.org/10.1371/journal.pone.0020657
2. https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON:0011302
3. https://www.britannica.com/animal/sea-squirt
4. https://doi.org/10.1111/1758-2229.13242
5. https://doi.org/10.1371/journal.pone.0093386
6. https://doi.org/10.1111/1462-2920.12908
7. https://doi.org/10.3389/fmicb.2012.00402
8. https://www.marinespecies.org/aphia.php?p=taxdetails&id=1839
9. https://doi.org/10.1038/ismej.2013.188
10. https://www.int-res.com/articles/meps/3/m003p257.pdf
11. https://doi.org/10.2108/zsj.18.309
12. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001176
13. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002
14. https://www.ebi.ac.uk/ols4/ontologies/bto/classes?obo_id=BTO:0000090
15. https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?obo_id=FOODON:03414467
16. https://doi.org/10.1093/femsec/fiaf078
17. https://doi.org/10.2108/zsj.18.723
18. https://doi.org/10.1002/jemt.10042
19. https://pubmed.ncbi.nlm.nih.gov/24152714/
20. https://pubmed.ncbi.nlm.nih.gov/18793310/
21. https://doi.org/10.1073/pnas.1111712108
22. https://pubmed.ncbi.nlm.nih.gov/26013440/
23. https://doi.org/10.3389/fmicb.2016.02092
24. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001179
25. https://www.ebi.ac.uk/ols4/
26. https://github.com/EnvironmentOntology/envo/issues/1029
27. https://doi.org/10.1038/ismej.2014.152
28. https://doi.org/10.1038/s41598-017-11441-4
29. https://doi.org/10.3389/fmars.2020.00201
30. https://doi.org/10.1073/pnas.0501424102
31. https://doi.org/10.1002/dvg.23534
32. https://doi.org/10.3390/md19070370
33. https://gold.jgi.doe.gov/ecosystem_classification