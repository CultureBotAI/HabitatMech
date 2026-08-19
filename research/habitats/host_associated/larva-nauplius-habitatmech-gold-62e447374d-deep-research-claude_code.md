---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T02:40:51.019485'
end_time: '2026-08-18T02:47:51.999395'
duration_seconds: 420.98
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: 'Larva: Nauplius'
  habitat_identifier: habitatmech:GOLD.62e447374d
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Arthropoda: Crustaceans > Larva: Nauplius'
  assertions: '1'
  parent_terms: (none)
  xrefs: UBERON:0002548
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term UBERON:0002548 'larva' attached as a parent. Life-stage review\
    \ (#112): carried UBERON:0002548 'larva' as a parent, reached by the ambiguous-leaf\
    \ rule rather than the path \u2014 several GOLD paths end in the same leaf, so\
    \ the ones that do not claim the term keep it as a parent. parent_habitats asserts\
    \ the parent is BROADER, and a larva or embryo is a whole organism rather than\
    \ a broader kind of place, so this is the same over-claim the identity cases had\
    \ one level up. Kept as an xref (#99). Per the rule #114 settled: the whole host\
    \ organism gets its own identity and an <X>-associated environment term; parts\
    \ of a host ground to the anatomy term. (source concept habitatmech:GOLD.62e447374d)"
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
  num_turns: 26
  total_cost_usd: 2.4244805
  session_id: c04997a8-29d3-4797-909b-91df1e4f7916
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 24
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Larva: Nauplius
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.62e447374d
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Arthropoda: Crustaceans > Larva: Nauplius
- **Upstream assertion volume:** 1
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** UBERON:0002548

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term UBERON:0002548 'larva' attached as a parent. Life-stage review (#112): carried UBERON:0002548 'larva' as a parent, reached by the ambiguous-leaf rule rather than the path — several GOLD paths end in the same leaf, so the ones that do not claim the term keep it as a parent. parent_habitats asserts the parent is BROADER, and a larva or embryo is a whole organism rather than a broader kind of place, so this is the same over-claim the identity cases had one level up. Kept as an xref (#99). Per the rule #114 settled: the whole host organism gets its own identity and an <X>-associated environment term; parts of a host ground to the anatomy term. (source concept habitatmech:GOLD.62e447374d)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Larva: Nauplius** as a microbial habitat, with citations.

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

# Nauplius (crustacean naupliar larva) as a microbial habitat

**Target:** `habitatmech:GOLD.62e447374d` — "Larva: Nauplius"
**GOLD path:** Host-associated > Arthropoda: Crustaceans > Larva: Nauplius
**Category:** HOST_ASSOCIATED · **Status:** UNGROUNDED · **Assertions:** 1

---

## Proposed definition

> An environment associated with an aquatic invertebrate which is determined by a crustacean nauplius — the unsegmented first larval instar bearing three pairs of cephalic appendages — and which comprises the chitinous cuticular surface of that larva together with, in feeding instars, its gut lumen.

Genus: `ENVO:01001176` *environment associated with an aquatic invertebrate*. Differentia: determined by a nauplius specifically (not any aquatic invertebrate), with the compartments named because the nauplius is, for much of its duration, an **exclusively epibiotic** habitat.

**Caveat on the genus (read section 2 before adopting):** the honest genus is *crustacean-associated environment*, which does not exist in ENVO. `ENVO:01001176` is the nearest existing ancestor and is two conceptual steps up. If a term request is filed, requesting the intermediate class alongside the leaf is the better move than stretching one sentence to cover the gap.

---

## 1. What the concept denotes

### The physical thing sampled

A **nauplius** is the earliest larval stage of most crustaceans: a small, essentially unsegmented, free-swimming larva with three pairs of appendages (uniramous first antennae, biramous second antennae, mandibles) and a single median naupliar eye ([Williams 1994, *Am Zool* 34:562–569, doi:10.1093/icb/34.4.562](https://doi.org/10.1093/icb/34.4.562); [Dahms, Fornshell & Fornshell 2006, *Org Divers Evol* 6:47–56, doi:10.1016/j.ode.2005.04.002](https://doi.org/10.1016/j.ode.2005.04.002); [Britannica, "nauplius"](https://www.britannica.com/science/nauplius)). Free-living nauplii occur in Cephalocarida, Branchiopoda, Ostracoda, Mystacocarida, Copepoda, Thecostraca, Euphausiacea and Penaeidea; most Malacostraca pass the stage embryonically.

As a **microbial habitat**, what a sample actually captures is a whole small animal — typically a pooled catch of tens to thousands of individuals, since a single copepod nauplius is roughly 90–200 µm long ([Dahl et al. 2012, *PLoS ONE* 7:e33107, doi:10.1371/journal.pone.0033107](https://doi.org/10.1371/journal.pone.0033107)). Two habitable compartments exist, and their relative weight is what makes this concept distinct from its later-stage siblings:

1. **The chitinous cuticle surface (epibiota).** The dominant compartment. Chitin–protein exoskeleton overlain by a wax epicuticle; colonised by attached and biofilm-forming bacteria.
2. **The gut lumen (endobiota) — present only in feeding instars, and absent entirely in some taxa.** In penaeids the mouth does not open until the zoea stage, so penaeid nauplii feed on yolk reserves and have no functional gut lumen at all; the authors of the *Litopenaeus stylirostris* work explicitly note that rearing water can therefore only modulate the **epibiota** at this stage ([Giraud et al. 2022, *Front Microbiol* 13:886752, doi:10.3389/fmicb.2022.886752](https://doi.org/10.3389/fmicb.2022.886752); [Angthong et al. 2020, *Sci Rep* 10:4896, doi:10.1038/s41598-020-61559-1](https://doi.org/10.1038/s41598-020-61559-1)). In barnacles, first-instar nauplii do not feed and moult within 1–2 h; instars II–VI are phytoplanktotrophic ([Qian et al., FEMS Microbiol Ecol 58:425](https://doi.org/10.1111/j.1574-6941.2006.00190.x)).

*Inference, not a sourced claim:* it follows from the above that a "nauplius" sample from a penaeid hatchery and a "nauplius" sample from a copepod culture are not the same habitat in compartment terms — one has no gut, the other may. Sources state each fact separately; the comparison is mine.

### Boundary — what is inside and what is next door

| Inside the concept | Neighbouring concept, not this one |
|---|---|
| All naupliar instars N1–N6 / NI–NVI, including **metanauplius** (a late naupliar substage) | **Zoea, protozoea, mysis, postlarva** (decapods); **copepodite** (`UBERON:0014860`); **cyprid/cypris** (thecostracans) — all post-naupliar |
| The larva's cuticle surface and gut lumen | The **egg / cyst** it hatched from (a distinct GOLD-level and ENVO-level concept; *Artemia* cysts are also a traded food product) |
| The living larva | **Exuviae** — the shed cuticle after ecdysis. Chemically similar chitin, but a detrital particle, not a host |
| The larva as sampled | **Rearing water / bacterioplankton** — the community source, repeatedly shown to be a *separate* compartment |
| Nauplii of any crustacean taxon | The **adult** copepod/barnacle/shrimp, and the "Arthropoda: Crustaceans" parent concept |

### Ambiguity

The label is **taxon-ambiguous, not sense-ambiguous**. "Nauplius" unambiguously denotes the larval form; what the GOLD path does not say is *which crustacean*. The realistic readings, all consistent with the path:

- **(a) Copepod nauplii from natural plankton** — the cholera-reservoir literature ([Huq et al. 1983, *Appl Environ Microbiol* 45:275–283, PMID 6337551](https://pubmed.ncbi.nlm.nih.gov/6337551/); [Rawlings, Ruiz & Colwell 2007, *AEM* 73:7926–7933, doi:10.1128/AEM.01238-07](https://doi.org/10.1128/AEM.01238-07)).
- **(b) Penaeid shrimp nauplii from hatchery larviculture** — the largest body of 16S work ([Giraud et al. 2022](https://doi.org/10.3389/fmicb.2022.886752); [Wang et al. 2020, *Microbiome* 8:106, doi:10.1186/s40168-020-00879-w](https://doi.org/10.1186/s40168-020-00879-w); [Angthong et al. 2020](https://doi.org/10.1038/s41598-020-61559-1)).
- **(c) *Artemia* (brine shrimp) nauplii as live feed / gnotobiotic model** ([Marques et al. 2005, *AEM* 71:4307–4317, doi:10.1128/AEM.71.8.4307-4317.2005](https://doi.org/10.1128/AEM.71.8.4307-4317.2005)).
- **(d) Barnacle nauplii** — least represented; barnacle microbiome work concentrates on the *cyprid*, not the nauplius ([PMID 31164063](https://pubmed.ncbi.nlm.nih.gov/31164063/)).

The path's own evidence is thin in a specific way: **"Arthropoda: Crustaceans" is the parent, with no genus-level qualifier**, and the assertion volume is **1**. GOLD's ecosystem paths are explicitly a finite, curator-maintained list rather than an exhaustive classification ([Mukherjee et al. 2023, *NAR* 51:D957–D963, doi:10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974)). The reading the data supports is therefore the **taxon-agnostic** one: *a crustacean nauplius, unspecified taxon*. Do not silently narrow it to *Artemia* or to penaeids — a definition that names a genus would over-claim relative to one assertion.

---

## 2. Genus — the broader kind

**Recommended:** `ENVO:01001176` **environment associated with an aquatic invertebrate** — *"An environment whose properties and composition are largely shaped by the presence of a spineless aquatic animal organism."* Verified via [OLS4/ENVO](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001176). It is a direct child of `ENVO:01001002` *animal-associated environment* and currently has **no children**, so a nauplius-associated environment would be its first. All nauplii are aquatic and all crustaceans are invertebrates, so the subsumption holds without qualification.

**The missing intermediate.** `ENVO:01001176` jumps from "any aquatic invertebrate" straight to the leaf. ENVO has no *crustacean-associated environment*, no *arthropod-associated environment* — a search of ENVO for "arthropod" returns only an NCBITaxon cross-reference and an unrelated UBERON epithelium term. This matters because GOLD's own parent level is exactly "Arthropoda: Crustaceans". Recommend filing the intermediate with the leaf.

### Near-misses and why each fails

| Term | Why it is not the genus |
|---|---|
| **`BTO:0000915` nauplius** — *"A crustacean larva in usually the first stage after leaving the egg and with three pairs of appendages, a median eye, and little or no segmentation."* | **This names the concept exactly**, and BTO is in HabitatMech's grounding vocabulary. It is nonetheless not a grounding target here: it denotes the **whole organism at a life stage**, which is precisely the case #112/#114 settled — the organism keeps its own minted identity and carries the term as `relation: xref`. **Correction to the record's stated rationale:** "no ontology term names the concept" is not accurate; a term names it and the right reason to stay UNGROUNDED is the whole-organism rule. |
| **`UBERON:0014406` nauplius stage** — *"The free-swimming first stage of the larva of certain crustaceans, having an unsegmented body with three pairs of appendages and a single median eye."* | Also names the concept, but it is a **life-cycle stage** — a temporal entity. Grounding a place to an interval of developmental time is a category error independent of the whole-organism rule. Correct disposition: `relation: xref`. |
| **`UBERON:0002548` larva** (currently on the record) | *"A distinct juvenile form many animals undergo before metamorphosis into adults."* Far **broader** than the concept — it subsumes insect, amphibian and nematode larvae — and is still a whole organism, so it cannot serve as `parent_habitats`. The existing note's decision to demote it to xref is right; `UBERON:0018378` *crustacean larval stage* and `BTO:0000915` are both tighter and belong in the xref set. |
| **`ENVO:01001055` environment associated with an animal part or small animal** — *"An environmental system determined by part of a living or dead animal, or a whole small animal."* | A genuine near-miss and arguably usable: a nauplius **is** a whole small animal. It fails as the preferred genus because it is a mixed-bag class (part-of-an-animal ∪ whole-small-animal, alt-label "Animal corpus") that also admits dead animals, and it does not assert the aquatic character every nauplius has. `ENVO:01001176` is cleaner. |
| **`ENVO:01001002` animal-associated environment** | Correct but too broad — the parent of `ENVO:01001176`, so it loses the aquatic-invertebrate constraint for nothing. |
| **`ENVO:01001179` cnidarian-associated environment** | The only existing sibling pattern under this branch; wrong phylum, but a useful **naming precedent** for a "nauplius-associated environment" request. |
| **A "zooplankton" environment term** | **Does not exist in ENVO** — a search of ENVO for "zooplankton" returns zero hits ([OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo)). Worth recording, since "zooplankton-associated" is how the cholera literature frames this habitat. |
| **`UBERON:0015170` nauplius eye** | An organ of the larva, not the larva. Pure lexical trap. |

---

## 3. Differentia — what distinguishes it

Ranked by how observable and how discriminating each property is.

**(1) It is a chitin habitat with a wax barrier.** The naupliar cuticle is chitin–protein and supports chitinolytic colonisation; *Vibrio cholerae* attaches via the MSHA type IV pilus and catabolises chitin via the extracellular chitinases ChiA1/ChiA2 feeding a GlcNAc-oligosaccharide uptake cascade ([Meibom et al. 2004, *PNAS* 101:2524–2529, doi:10.1073/pnas.0308707101](https://doi.org/10.1073/pnas.0308707101); [Pruzzo, Vezzulli & Colwell 2008, *Environ Microbiol* 10:1400–1410, doi:10.1111/j.1462-2920.2007.01559.x](https://doi.org/10.1111/j.1462-2920.2007.01559.x)). Notably, adhesion to live copepods is **less efficient** than to bare chitin particles, attributed to the wax epicuticle preventing close contact (Pruzzo et al. 2008) — so the living larva is not interchangeable with a chitin flake, which is exactly why the exuvia is a neighbouring concept.

**(2) It is predominantly an external-surface habitat.** See §1. In penaeids the mouth opens only at zoea, making the nauplius the one larval stage with essentially no internal compartment ([Giraud et al. 2022](https://doi.org/10.3389/fmicb.2022.886752); [Angthong et al. 2020](https://doi.org/10.1038/s41598-020-61559-1)). Source-tracking across the penaeid developmental cycle divides larval communities into two phases, **before and after mouth opening**, with the pre-opening phase dominated by external sources and the post-opening phase by internal succession ([Wang et al. 2020](https://doi.org/10.1186/s40168-020-00879-w)).

**(3) It is ephemeral and repeatedly reset by ecdysis.** Six naupliar instars pass in roughly 5–7 days in *Nitocra spinipes*, growing 0.09 → 0.20 mm, each moult shedding the colonised surface ([Dahl et al. 2012](https://doi.org/10.1371/journal.pone.0033107)). The habitat is destroyed and re-formed on a scale of hours to a day — a strong contrast with adult or sessile hosts, and a plausible mechanism for why naupliar surfaces accumulate less biofilm than copepodite surfaces (the epibiont-load comparison is protistan, [Sci Rep 2022, doi:10.1038/s41598-022-26004-5](https://doi.org/10.1038/s41598-022-26004-5); the extension to bacteria is my inference).

**(4) Its community is seeded both vertically and from the water column.** In *L. stylirostris*, families including Colwelliaceae, Alteromonadaceae, Pseudoalteromonadaceae, Saccharospirillaceae, Oceanospirillaceae, Vibrionaceae, Rhodobacteraceae and Flavobacteriaceae are shared with the environment, while specific Arcobacteraceae, Rhodobacteraceae, Comamonadaceae and Colwelliaceae lineages occur only in breeders and their offspring — evidence of vertical transmission from broodstock ([Giraud et al. 2022](https://doi.org/10.3389/fmicb.2022.886752); [Giraud et al. 2021, *PeerJ* 9:e12241, doi:10.7717/peerj.12241](https://doi.org/10.7717/peerj.12241)).

**(5) Its diversity signature differs from later stages.** Alpha-diversity across the *L. vannamei* cycle follows a **U-shape with zoea and mysis at the valley**, so nauplius and early-postlarval communities are the more complex ones; at nauplius, γ-Proteobacteria 43.6%, Bacteroidetes 20.0%, α-Proteobacteria 15.7%, Firmicutes 8.5% ([Wang et al. 2020](https://doi.org/10.1186/s40168-020-00879-w)). *P. monodon* nauplius, zoea and mysis communities each differ from one another while postlarval communities converge ([Angthong et al. 2020](https://doi.org/10.1038/s41598-020-61559-1)).

**(6) Salinity spans nearly the full aquatic range.** Freshwater (cyclopoid copepods, branchiopods) → marine (calanoids, barnacles, penaeids) → hypersaline (*Artemia*). This is a property of the concept as a class, not a differentia against siblings, and a definition should therefore **not** assert a salinity.

**(7) Applied significance — two well-established roles.** (a) **Cholera reservoir:** attachment to living copepods keeps *V. cholerae* culturable at least 10 days longer than on dead copepods and protects it from nanoflagellate grazing, alum and chlorine (Pruzzo et al. 2008); SEM localises heaviest colonisation to the oral region and egg sac of adults (Huq et al. 1983). (b) **Aquaculture vector and model:** *Artemia* nauplii carry potentially harmful *Vibrio* into hatchery tanks, and gnotobiotic *Artemia* nauplii (the GART system, from Sorgeloos et al. 1986 and Marques et al. 2004) are a standard host–microbe test bed ([Marques et al. 2005](https://doi.org/10.1128/AEM.71.8.4307-4317.2005)).

---

## 4. Sources

**Concept and morphology**
- Williams TA (1994) The nauplius larva of crustaceans: functional diversity and the phylotypic stage. *Am Zool* 34(4):562–569. [doi:10.1093/icb/34.4.562](https://doi.org/10.1093/icb/34.4.562)
- Dahms H-U, Fornshell JA, Fornshell BJ (2006) Key for the identification of crustacean nauplii. *Org Divers Evol* 6(1):47–56. [doi:10.1016/j.ode.2005.04.002](https://doi.org/10.1016/j.ode.2005.04.002)
- Encyclopædia Britannica, "nauplius". https://www.britannica.com/science/nauplius
- Natural History Museum LA, *Crustacea Glossary*, "naupliar eye". https://research.nhm.org/glossary/define.html?termID=484

**Ontology terms (all verified against OLS4, August 2026)**
- `ENVO:01001176`, `ENVO:01001055`, `ENVO:01001002`, `ENVO:01001179` — https://www.ebi.ac.uk/ols4/ontologies/envo
- `BTO:0000915` nauplius — https://www.ebi.ac.uk/ols4/ontologies/bto
- `UBERON:0014406` nauplius stage; `UBERON:0002548` larva; `UBERON:0018378` crustacean larval stage; `UBERON:0014860` copepodite stage; `UBERON:0015170` nauplius eye — https://www.ebi.ac.uk/ols4/ontologies/uberon

**Vocabulary / provenance**
- Mukherjee S et al. (2023) Twenty-five years of Genomes OnLine Database (GOLD). *Nucleic Acids Res* 51(D1):D957–D963. [doi:10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974) — the source of the five-level path, and the statement that GOLD terms are a finite curated list rather than an exhaustive ontology.
- AGROVOC/ASFA concept "nauplius": https://agrovoc.fao.org/skosmosAsfa/asfa/en/page/c_f8dac7e4

**Primary microbiology**
- Huq A, Small EB, West PA, Huq MI, Rahman R, Colwell RR (1983) Ecological relationships between *Vibrio cholerae* and planktonic crustacean copepods. *Appl Environ Microbiol* 45(1):275–283. [PMID 6337551](https://pubmed.ncbi.nlm.nih.gov/6337551/)
- Rawlings TK, Ruiz GM, Colwell RR (2007) Association of *Vibrio cholerae* O1 El Tor and O139 Bengal with the copepods *Acartia tonsa* and *Eurytemora affinis*. *Appl Environ Microbiol* 73(24):7926–7933. [doi:10.1128/AEM.01238-07](https://doi.org/10.1128/AEM.01238-07) — the one study that separates naupliar from adult and egg colonisation.
- Meibom KL et al. (2004) The *Vibrio cholerae* chitin utilization program. *PNAS* 101(8):2524–2529. [doi:10.1073/pnas.0308707101](https://doi.org/10.1073/pnas.0308707101)
- Pruzzo C, Vezzulli L, Colwell RR (2008) Global impact of *Vibrio cholerae* interactions with chitin. *Environ Microbiol* 10(6):1400–1410. [doi:10.1111/j.1462-2920.2007.01559.x](https://doi.org/10.1111/j.1462-2920.2007.01559.x)
- Nahar S et al. (2011) Role of shrimp chitin in the ecology of toxigenic *Vibrio cholerae* and cholera transmission. *Front Microbiol* 2:260. [doi:10.3389/fmicb.2011.00260](https://doi.org/10.3389/fmicb.2011.00260)
- Wang Y et al. (2020) Fine-scale succession patterns and assembly mechanisms of bacterial community of *Litopenaeus vannamei* larvae across the developmental cycle. *Microbiome* 8:106. [doi:10.1186/s40168-020-00879-w](https://doi.org/10.1186/s40168-020-00879-w); PMID 32620132
- Giraud C et al. (2022) The active microbiota of the eggs and the nauplii of the Pacific blue shrimp *Litopenaeus stylirostris* partially shaped by a potential vertical transmission. *Front Microbiol* 13:886752. [doi:10.3389/fmicb.2022.886752](https://doi.org/10.3389/fmicb.2022.886752)
- Giraud C et al. (2021) Potential lineage transmission within the active microbiota of the eggs and the nauplii of the shrimp *Litopenaeus stylirostris*. *PeerJ* 9:e12241. [doi:10.7717/peerj.12241](https://doi.org/10.7717/peerj.12241)
- Angthong P et al. (2020) Bacterial analysis in the early developmental stages of the black tiger shrimp (*Penaeus monodon*). *Sci Rep* 10:4896. [doi:10.1038/s41598-020-61559-1](https://doi.org/10.1038/s41598-020-61559-1)
- Marques A et al. (2005) Effects of bacteria on *Artemia franciscana* cultured in different gnotobiotic environments. *Appl Environ Microbiol* 71(8):4307–4317. [doi:10.1128/AEM.71.8.4307-4317.2005](https://doi.org/10.1128/AEM.71.8.4307-4317.2005)
- Dahl U et al. (2012) Antibiotic-induced change of bacterial communities associated with the copepod *Nitocra spinipes*. *PLoS ONE* 7(3):e33107. [doi:10.1371/journal.pone.0033107](https://doi.org/10.1371/journal.pone.0033107)
- Microbiome acquisition during larval settlement of the barnacle *Semibalanus balanoides*. [PMID 31164063](https://pubmed.ncbi.nlm.nih.gov/31164063/) — **cyprid**, not nauplius; cited only as the boundary case.

**Claims that are my inference, not a source's statement:** (i) that the compartment structure differs enough between penaeid and copepod nauplii to make them non-interchangeable samples; (ii) that rapid ecdysis limits bacterial biofilm accumulation on naupliar surfaces — the measured stage-comparison is for protistan epibionts only; (iii) the subsumption of nauplius-associated environment under `ENVO:01001176`. Do not cite a source for any of these.

---

## 5. Synonyms, and what not to conflate

**In real use for this concept**
- nauplius larva; naupliar larva; nauplii (pl.); nauplius stage larva
- **orthonauplius** — a nauplius with exactly three appendage pairs, i.e. the strict sense
- **metanauplius** — a late naupliar instar in which post-mandibular appendages are externally visible; **a sub-kind of this concept, inside the boundary**
- Instar designations: N1–N6, NI–NVI, N5 (as used in penaeid hatchery sampling)
- Domain-specific: "*Artemia* nauplii", "brine shrimp nauplii", "instar I nauplii" (live-feed literature); "copepod nauplii" (plankton ecology)

**Commonly but wrongly treated as the same thing**
- **`UBERON:0002548` larva** — genus-level, spans insects and amphibians; not a synonym.
- **cyprid / cypris larva** — the *post*-naupliar settling stage of thecostracans. Most "barnacle larva microbiome" papers are about the cyprid. Frequent conflation.
- **copepodite**, **zoea**, **protozoea**, **mysis**, **postlarva** — sibling later stages.
- **egg / cyst / decapsulated cyst** — the pre-hatch embryo. *Artemia* cysts are also a commercial food product and belong in a different branch entirely.
- **exuvia / molt / chitin particle / marine snow** — shed cuticle; a detrital substrate. The wax-epicuticle finding shows empirically that live nauplii and bare chitin behave differently as attachment surfaces (Pruzzo et al. 2008).
- **`UBERON:0015170` nauplius eye** — an organ, not the larva.
- **Homonyms that will poison a text-mining pass:** *Nauplius* is a former plant genus in Asteraceae (species now in *Asteriscus*) and appears as a butterfly epithet in *Eresia*; OLS returns sixteen such taxonomic entries. *Nauplius* is also the journal of the Brazilian Crustacean Society — a very common false positive in citation-based evidence gathering.

---

## 6. Should this be a term at all?

**Yes — as a HabitatMech-minted concept with a term request for `nauplius-associated environment`, and it should stay UNGROUNDED.** It is a real physical setting from which microbial samples are taken, not a process, quality, disease state or sampling artefact, and it has an independent, well-characterised microbiology in two separate literatures (cholera ecology; larviculture).

But the recorded rationale needs one factual correction, and the disposition benefits from two additions:

1. **"No ontology term fits this concept" is not accurate.** `BTO:0000915` *nauplius* and `UBERON:0014406` *nauplius stage* both name it exactly, and BTO is one of the five vocabularies HabitatMech grounds against. The defensible reason to remain UNGROUNDED is the rule #112/#114 settled — **a nauplius is the whole host organism at a life stage, not a part of one** — reinforced for the UBERON term by the fact that a *stage* is a temporal entity and cannot be a place. Recording the real reason matters: `tests/test_decisions.py` checks a note's claims, and "no term exists" is a checkable claim that happens to be false.

2. **Tighten the xref set.** `UBERON:0002548` *larva* is the loosest available handle. `BTO:0000915` *nauplius* (exact), `UBERON:0014406` *nauplius stage* (exact, temporal) and `UBERON:0018378` *crustacean larval stage* (one level up, taxon-correct) are all better xrefs and none of them is a grounding target. The upstream-suggested `UBERON:0002548` should stay as an xref for provenance, not as the only one.

3. **File the missing intermediate with the leaf.** ENVO has *cnidarian-associated environment* but nothing between *environment associated with an aquatic invertebrate* and any arthropod. A request for **crustacean-associated environment** (matching GOLD's own "Arthropoda: Crustaceans" level) plus **nauplius-associated environment** under it gives a clean two-step genus chain and serves the sibling records in this branch, rather than making one term stretch across the gap.

**What weakens the case, stated plainly:** upstream assertion volume is **1**. The concept is scientifically solid, but at that volume the corpus is describing a habitat class on the strength of a single GOLD path entry, and the definition should therefore stay taxon-agnostic and assert nothing about salinity, host genus, or gut presence beyond the hedged "in feeding instars".

## Citations

1. https://doi.org/10.1093/icb/34.4.562
2. https://doi.org/10.1016/j.ode.2005.04.002
3. https://www.britannica.com/science/nauplius
4. https://doi.org/10.1371/journal.pone.0033107
5. https://doi.org/10.3389/fmicb.2022.886752
6. https://doi.org/10.1038/s41598-020-61559-1
7. https://doi.org/10.1111/j.1574-6941.2006.00190.x
8. https://pubmed.ncbi.nlm.nih.gov/6337551/
9. https://doi.org/10.1128/AEM.01238-07
10. https://doi.org/10.1186/s40168-020-00879-w
11. https://doi.org/10.1128/AEM.71.8.4307-4317.2005
12. https://pubmed.ncbi.nlm.nih.gov/31164063/
13. https://doi.org/10.1093/nar/gkac974
14. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001176
15. https://www.ebi.ac.uk/ols4/ontologies/envo
16. https://doi.org/10.1073/pnas.0308707101
17. https://doi.org/10.1111/j.1462-2920.2007.01559.x
18. https://doi.org/10.1038/s41598-022-26004-5
19. https://doi.org/10.7717/peerj.12241
20. https://research.nhm.org/glossary/define.html?termID=484
21. https://www.ebi.ac.uk/ols4/ontologies/bto
22. https://www.ebi.ac.uk/ols4/ontologies/uberon
23. https://agrovoc.fao.org/skosmosAsfa/asfa/en/page/c_f8dac7e4
24. https://doi.org/10.3389/fmicb.2011.00260