---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T20:58:29.945703'
end_time: '2026-08-17T21:06:32.590057'
duration_seconds: 482.64
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Larva
  habitat_identifier: habitatmech:GOLD.1cbfc76870
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Arthropoda: Insects > Larva'
  assertions: '94'
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
    \ of a host ground to the anatomy term. (source concept habitatmech:GOLD.1cbfc76870)"
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
  web_search_requests: 13
  num_turns: 27
  total_cost_usd: 2.9545405000000002
  session_id: e3412a01-e778-437d-acc5-93e6873f4210
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 36
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Larva
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.1cbfc76870
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Arthropoda: Insects > Larva
- **Upstream assertion volume:** 94
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** UBERON:0002548

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term UBERON:0002548 'larva' attached as a parent. Life-stage review (#112): carried UBERON:0002548 'larva' as a parent, reached by the ambiguous-leaf rule rather than the path — several GOLD paths end in the same leaf, so the ones that do not claim the term keep it as a parent. parent_habitats asserts the parent is BROADER, and a larva or embryo is a whole organism rather than a broader kind of place, so this is the same over-claim the identity cases had one level up. Kept as an xref (#99). Per the rule #114 settled: the whole host organism gets its own identity and an <X>-associated environment term; parts of a host ground to the anatomy term. (source concept habitatmech:GOLD.1cbfc76870)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Larva** as a microbial habitat, with citations.

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

# Larva (`habitatmech:GOLD.1cbfc76870`) — definition research

## Proposed definition

> An insect-associated environment which is determined by an insect in its larval stage — the actively feeding, post-embryonic form that precedes pupation — comprising that larva's gut lumen, haemocoel and cuticular surface.

If the curator prefers to start from an ENVO term rather than from the parent HabitatMech record, the equivalent is: *An animal-associated environment (ENVO:01001002) which is determined by an insect in its larval stage …*. Both forms are one sentence; the first is preferable because `habitatmech:GOLD.dba2a83b95` ("Arthropoda: Insects") is already the record's parent and already carries ENVO:01001002 as its own parent, so the insect restriction does not have to be repeated in the differentia.

---

## 1. What the concept denotes

**The thing sampled is an insect that is at the larval stage of its development, treated as the place the microbes live.** Not the stage as a period of time, and not the medium the larva is growing in.

The source path settles this. In GOLD, `Larva` is an **Ecosystem Type** (level 3) sitting directly under `Host-associated > Arthropoda: Insects`, in the same slot that `Digestive system`, `Circulatory system`, `Respiratory system`, `Fat body`, `Head` and `Whole body` occupy ([GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification)). It is itself subdivided into body compartments — verified against `data/raw/gold_ecosystem_paths.tsv`:

| Path | Assertions |
|---|---|
| `… > Insects > Larva` | 94 |
| `… > Insects > Larva > Gut` | 21 |
| `… > Insects > Larva > Gut > Frass` | 0 |
| `… > Insects > Larva > Gut > Gastric caeca` | 0 |
| `… > Insects > Larva > Whole body` | 0 |
| `… > Insects > Larva > Head` / `Thorax` / `Abdomen` | 0 |

So GOLD models a larva the way it models an organ system: as a partitioning of the host body that is then cut finer. The 94 assertions attached to the node itself are records where nothing finer than "larva" was stated — in practice a surface-sterilised whole-larva homogenate or an undissected larval sample. The concept, however, is the larval host as a habitat; the gut, head and cuticle of that larva are *inside* it, expressed as child nodes.

**Boundaries.**

- **Inside:** the larva's gut lumen and gut wall, haemolymph/haemocoel, fat body and bacteriomes, and the cuticle surface. Whole-larva homogenates measurably include all of these — in *Hermetia illucens*, gut-only samples show significantly lower diversity than whole larvae, the difference being cuticle- and body-resident taxa ([meta-analysis, PMC9453823](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9453823/)); in *Anopheles albimanus*, internal and cuticle-surface communities are compositionally distinct (*Leucobacter*, *Thorsellia*, *Chryseobacterium* internally vs. *Acidovorax*, *Paucibacter*, Comamonadaceae on the cuticle) ([PMC8542342](https://pmc.ncbi.nlm.nih.gov/articles/PMC8542342/)).
- **Immediately outside — the neighbouring concepts, all of which exist as separate GOLD nodes:** `Nymph/Instar` (3 assertions), `Prepupa` (2), `Pupa` (0), `Ootheca/Egg mass > Eggs` (19), and the adult-inclusive `Whole body` (60). Also outside: the substrate or water the larva develops in, which under GOLD is an `Environmental` path, not a `Host-associated` one.
- **A different record entirely:** `Host-associated > Arthropoda: Crustaceans > Larva` is a separate GOLD node (`gold.ecosystem:7343`) with its own HabitatMech identifier. This record is *insect* larva only. That is what the "ambiguous leaf" note in the decision refers to — several GOLD paths terminate in the string "Larva".

**Ambiguity — three readings, only one of them intended.**

1. **The larval insect as host** — intended, per the `Host-associated >` prefix and the body-part children.
2. **The larval rearing environment** (mosquito "larval habitat", "breeding-site water", BSFL rearing substrate). This is the dominant reading of the bare phrase "larval habitat" in the vector-biology literature and it is *not* what this node means. See §5.
3. **The larval stage as a period of the life cycle** (UBERON:0000069 `larval stage`). A temporal occurrent, not a place. Not what this node means either.

Whether GOLD's `Larva` is restricted to Holometabola is **my inference, not something GOLD states**: the existence of a sibling `Nymph/Instar` node — which HabitatMech already grounds to `BTO:0000954` "nymph" — implies that hemimetabolous immatures are routed there and that `Larva` carries the holometabolous reading. A curator who wants to avoid the inference can drop "that precedes pupation" and write "the post-embryonic feeding form that precedes the adult".

---

## 2. Genus — the broader kind

**Smallest well-established kind: an insect-associated environment.** No ontology term expresses it.

- **`habitatmech:GOLD.dba2a83b95` "Arthropoda: Insects"** — already the record's parent, itself UNGROUNDED, itself parented to ENVO:01001000 and ENVO:01001002. This is the right genus and it is a HabitatMech mint, which is consistent: the whole set of insect-host habitat classes is missing from ENVO.
- **`ENVO:01001002` "animal-associated environment"** — *"An environmental system determined by an animal."* The nearest **existing** ontology genus, verified present in `data/raw/ontology_terms.tsv`. Correct but two steps too broad on the taxon axis (all Metazoa) and silent on developmental stage.

**Near-misses checked and rejected:**

| Term | Why it fails |
|---|---|
| `UBERON:0002548` **larva** (verified label via [OLS4](https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON:0002548)) | An organism class, not an environment — "a distinct juvenile form many animals undergo before metamorphosis". Also broader on the taxon axis (tadpoles, trochophores, planulae). Correctly held as `relation: xref` under the #114 rule. |
| `UBERON:0000069` **larval stage** | A life-cycle stage, i.e. a temporal occurrent. Worse than the above: it is not a material entity at all. |
| `ENVO:01001055` **environment associated with an animal part or small animal** — *"determined by part of a living or dead animal, or a whole small animal"* | The single most tempting near-miss: an insect larva **is** a whole small animal. But (a) it is a disjunctive class that also covers detached animal parts, and (b) in the vendored slice it is `subClassOf ENVO:01001110` **ecosystem** ("includes both living and non-living components"), so adopting it imports an ecosystem commitment GOLD's node never makes. Genuinely broader, so defensible as an *additional* parent; not an identity. |
| `ENVO:01001176` **environment associated with an aquatic invertebrate** | Narrower on an axis the concept does not have — right for a mosquito or chironomid larva, wrong for a caterpillar or scarab grub. Its value here is structural: in the slice it is `subClassOf` **both** ENVO:01001002 and ENVO:01001055, which is exactly the multi-parent shape a new "insect-associated environment" term would take. |
| `ENVO:01001041` fungi-associated, `ENVO:01001179` cnidarian-associated | Sibling patterns, wrong taxon. Their existence shows ENVO accepts taxon-scoped `<X>-associated environment` classes but has simply never minted one for arthropods. |
| `BTO:0000954` **nymph** | The sibling concept, already the identity of the `Nymph/Instar` record. Conflating the two would merge holo- and hemimetabolous immatures. |
| `FOODON:00001177` insect food product | Larvae *as food*, not larvae as habitat. Listed because the BSFL/edible-insect literature makes this an easy slip. |

An ENVO search for `insect`, `arthropod`, `larva`-scoped **environment** classes returns nothing usable — the only ENVO hits mentioning insects are `ENVO:01001636` "insect conservation process" and incidental mentions inside unrelated definitions.

---

## 3. Differentia — what distinguishes it from its siblings

Ranked by how observable each is, and by how well it separates `Larva` from `Pupa`, `Nymph/Instar`, `Ootheca/Egg mass` and adult `Whole body`.

**(a) The host is at a defined, externally recognisable developmental stage — and the microbial community turns over at its boundaries.** In holometabolous insects the entire larval gut and its contents are eliminated at pupation as the meconium, so larval and adult communities are decoupled rather than continuous. Hammer & Moran frame this as the defining constraint on holometabolous symbiosis: microbes in larvae "encounter a radical transformation of their habitat" ([*Phil. Trans. R. Soc. B* 374:20190068, 2019](https://royalsocietypublishing.org/doi/10.1098/rstb.2019.0068), doi:10.1098/rstb.2019.0068). A subsequent 18-species test across five holometabolous and three hemimetabolous orders found significantly higher larva-to-adult beta diversity in the holometabolous hosts ([*Molecular Ecology*, 2022](https://onlinelibrary.wiley.com/doi/10.1111/mec.16673), doi:10.1111/mec.16673). **This is the strongest differentia**: it makes "larva" a distinct habitat rather than merely a younger version of the adult.

**(b) Distinctive and often extreme gut physicochemistry.** Lepidopteran larval midgut is among the most alkaline biological compartments known, pH ~10–12, generated by a V-ATPase-energised K⁺ transport system, with a longitudinal gradient from strongly alkaline anterior to near-neutral posterior ([Dow, *J. Exp. Biol.* 172:355–375, 1992](https://journals.biologists.com/jeb/article/172/1/355/6581/pH-gradients-in-lepidopteran-midgut); [PMID 9874748](https://pubmed.ncbi.nlm.nih.gov/9874748/)). The humus-feeding scarab larva *Pachnoda ephippiata* shows midgut pH > 11 with microsensor-measured redox and O₂ gradients, and segregates most of its fermentative community into a near-neutral, anoxic hindgut ([Lemke et al., *Appl. Environ. Microbiol.* 69:6650–6658, 2003](https://journals.asm.org/doi/10.1128/aem.69.11.6650-6658.2003), doi:10.1128/AEM.69.11.6650-6658.2003). Gut physicochemistry is the standard explanatory axis for insect gut community structure generally ([Engel & Moran, *FEMS Microbiol. Rev.* 37:699–735, 2013](https://academic.oup.com/femsre/article/37/5/699/542120), doi:10.1111/1574-6976.12025, PMID 23692388).

**(c) The larva eats the growth substrate; the conspecific adult usually does not.** This is why larval communities track the rearing medium. In *Hermetia illucens*, substrate type is the dominant driver of microbiota composition, above developmental stage ([Frontiers in Microbiology editorial, 2024](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2024.1441577/full), doi:10.3389/fmicb.2024.1441577). In mosquitoes the larval community is a filtered subset of the breeding-water community ([FEMS Microbiol. Ecol. 98:fiac016, 2022](https://academic.oup.com/femsec/article/98/1/fiac016/6526867), doi:10.1093/femsec/fiac016). Diet contrast between stages (leaf-chewing larva vs. nectar-feeding adult) is documented in *Heliconius erato*, *Bombus pascuorum*, *Musca domestica*.

**(d) Functional dependence that is stage-specific.** Axenic larvae of *Aedes aegypti*, *Anopheles gambiae* and *Georgecraigius atropalpus* arrest at the first instar and die; colonisation by viable bacteria — not a specific taxon — rescues development ([Coon et al., *Molecular Ecology* 23:2727–2739, 2014](https://onlinelibrary.wiley.com/doi/10.1111/mec.12771), doi:10.1111/mec.12771, PMID 24766707). Mechanistically the larval microbiota consumes O₂ and imposes midgut hypoxia that drives HIF-dependent growth signalling. Later work qualifies "requirement" — axenic *Ae. aegypti* can be reared on very high-nutrient diets, with delayed development and reduced fecundity ([*Nat. Commun.* 9:4464, 2018](https://www.nature.com/articles/s41467-018-07014-2), doi:10.1038/s41467-018-07014-2). **Report both; the requirement is real but not absolute.**

**(e) Colonisation density is highly clade-dependent, and one large clade is close to uncolonised.** Across 124 species from 15 families of wild leaf-feeding caterpillars, gut bacterial densities were orders of magnitude below other insects', >80 % of 16S reads were plant chloroplast/mitochondrial, there was no core phylotype set, and suppressing bacteria in *Manduca sexta* had no detectable effect on growth or survival ([Hammer et al., *PNAS* 114:9641–9646, 2017](https://www.pnas.org/doi/10.1073/pnas.1707186114), doi:10.1073/pnas.1707186114, PMID 28830993). **This matters for the definition**: it means "larva" cannot be defined by *having* a characteristic community. Define it by host stage and physical constitution, not by microbial content.

**Recommendation on what to put in the differentia clause:** host developmental stage plus the physical compartments (b, and the extent from §1). Leave (a), (c), (d) and (e) to the record's notes and `causal_graphs`, where each edge can carry its own evidence — the schema requires that, and these are exactly the mechanism claims no upstream source vouches for.

---

## 4. Sources

Primary and standards, with identifiers. Everything below was checked against the linked page or record.

- Engel P, Moran NA. The gut microbiota of insects – diversity in structure and function. *FEMS Microbiology Reviews* 37(5):699–735, Sept 2013. doi:[10.1111/1574-6976.12025](https://doi.org/10.1111/1574-6976.12025), PMID 23692388.
- Hammer TJ, Moran NA. Links between metamorphosis and symbiosis in holometabolous insects. *Phil. Trans. R. Soc. B* 374(1783):20190068, 14 Oct 2019. doi:[10.1098/rstb.2019.0068](https://doi.org/10.1098/rstb.2019.0068).
- Hammer TJ, Janzen DH, Hallwachs W, Jaffe SP, Fierer N. Caterpillars lack a resident gut microbiome. *PNAS* 114(36):9641–9646, 22 Aug 2017. doi:[10.1073/pnas.1707186114](https://doi.org/10.1073/pnas.1707186114), PMID 28830993.
- Complete metamorphosis and microbiota turnover in insects. *Molecular Ecology*, 2022. doi:[10.1111/mec.16673](https://doi.org/10.1111/mec.16673).
- Lemke T, Stingl U, Egert M, Friedrich MW, Brune A. Physicochemical conditions and microbial activities in the highly alkaline gut of the humus-feeding larva of *Pachnoda ephippiata*. *Appl. Environ. Microbiol.* 69(11):6650–6658, 2003. doi:[10.1128/AEM.69.11.6650-6658.2003](https://doi.org/10.1128/AEM.69.11.6650-6658.2003).
- Dow JAT. pH gradients in lepidopteran midgut. *J. Exp. Biol.* 172:355–375, 1992. [PMID 9874748](https://pubmed.ncbi.nlm.nih.gov/9874748/). (The frequently cited pH-11 figure originates in Dow 1984, *Am. J. Physiol.* — **I did not verify that 1984 record directly**; cite the 1992 paper, which I did verify.)
- Berenbaum M. Adaptive significance of midgut pH in larval Lepidoptera. *American Naturalist* 115(1):138–146, 1980. doi:[10.1086/283551](https://doi.org/10.1086/283551).
- Coon KL, Vogel KJ, Brown MR, Strand MR. Mosquitoes rely on their gut microbiota for development. *Molecular Ecology* 23:2727–2739, 2014. doi:[10.1111/mec.12771](https://doi.org/10.1111/mec.12771), PMID 24766707.
- Correa MA et al. Generation of axenic *Aedes aegypti* demonstrate live bacteria are not required for mosquito development. *Nat. Commun.* 9:4464, 2018. doi:[10.1038/s41467-018-07014-2](https://doi.org/10.1038/s41467-018-07014-2).
- Larval habitat determines the bacterial and fungal microbiota of *Aedes aegypti*. *FEMS Microbiology Ecology* 98(1):fiac016, 2022. doi:[10.1093/femsec/fiac016](https://doi.org/10.1093/femsec/fiac016).
- Editorial: Gut microbiome in black soldier fly (*Hermetia illucens* L.) larvae. *Front. Microbiol.*, 2024. doi:[10.3389/fmicb.2024.1441577](https://doi.org/10.3389/fmicb.2024.1441577); [PMC11224508](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11224508/).
- Meta-analysis of *Hermetia illucens* larval microbiota based on 16S amplicon sequencing. [PMC9453823](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9453823/) — source for gut-vs-whole-larva diversity difference.
- Comprehensive characterization of internal and cuticle surface microbiota of *Anopheles albimanus*. [PMC8542342](https://pmc.ncbi.nlm.nih.gov/articles/PMC8542342/).
- The ecological–evolutionary game of the insect gut microbiome. *Vet. Sci.* 12:866, 2025. doi:[10.3390/vetsci12090866](https://doi.org/10.3390/vetsci12090866) — recent synthesis of pH/O₂/osmolality gradients in insect guts.

Vocabularies and standards:

- GOLD Ecosystem Classification, five-level scheme (Ecosystem → Category → Type → Subtype → Specific Ecosystem): <https://gold.jgi.doe.gov/ecosystem_classification>; [IMG/GOLD terms glossary](https://sites.google.com/lbl.gov/imghelp/home/img-and-gold-terms).
- MIxS `host_life_stage`, MIXS:0000251, *"Description of life stage of host"*, string-valued, present in the Agriculture, HostAssociated, PlantAssociated and SymbiontAssociated extensions: <https://genomicsstandardsconsortium.github.io/mixs/0000251/>. **Directly relevant**: the GSC models life stage as a *host descriptor field* alongside `host_taxid` and `host_body_site`, not as an environment class. See §6.
- ENVO terms verified in `data/raw/ontology_terms.tsv` and via [OLS4](https://www.ebi.ac.uk/ols4/): ENVO:01001000, ENVO:01001001, ENVO:01001002, ENVO:01001041, ENVO:01001055, ENVO:01001110, ENVO:01001176, ENVO:01001179; UBERON:0002548, UBERON:0000069.

**Explicitly flagged as my inference, not sourced:** (i) that GOLD's `Larva` node is restricted to Holometabola — inferred from the sibling `Nymph/Instar` node; (ii) that the 94 direct assertions represent whole-larva or undissected samples — inferred from the node having its own body-part children; (iii) the reading of ENVO:01001055's placement under `ecosystem` as an over-commitment for this concept.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept:** insect larva; larval insect; larva (whole body); larval stage sample. Taxon-specific vernaculars that UBERON:0002548 carries as narrow synonyms and that appear in sample metadata: **caterpillar** (Lepidoptera), **grub** (Coleoptera, esp. Scarabaeidae), **maggot** (Diptera: Cyclorrhapha), **wriggler / wiggler** (Culicidae), **BSFL** (*Hermetia illucens* larvae, in the bioconversion literature). "Instar" / "*n*th-instar larva" names a sub-stage of the same concept.

**Commonly but wrongly treated as the same thing:**

1. **The mosquito "larval habitat" / "breeding site" / "larval water" / "container water" / "surface microlayer".** This is the single most dangerous conflation, because the phrase *"larval habitat"* in vector biology means the **water body**, not the larva. The literature keeps these strictly apart — larval microbiota are a filtered subset of the breeding-water community, and co-rearing experiments in shared larval water still recover distinct species-specific midgut communities ([*Sci. Rep.* 10:3352, 2020](https://www.nature.com/articles/s41598-020-60075-6), doi:10.1038/s41598-020-60075-6). Under GOLD, breeding water is an `Environmental > Aquatic` path, not a `Host-associated` one. A HabitatMech note on this record should say so explicitly.
2. **BSFL rearing substrate / frass.** Same error in the bioconversion literature. GOLD gives frass its own node (`… > Larva > Gut > Frass`).
3. **`Larva > Gut` (21 assertions).** A child, not a synonym. Grounding the parent to a gut anatomy term would collapse cuticle- and haemocoel-resident taxa into the gut.
4. **Nymph / naiad / instar (hemimetabolous immatures).** UBERON:0002548 lists `nymph` and `naiad` as *narrow synonyms* of `larva`, which is biologically defensible but **wrong for this record**: GOLD splits them, and HabitatMech already has a separate `Nymph/Instar` record grounded to BTO:0000954. Do not import UBERON's synonym list wholesale.
5. **Pupa, prepupa, ootheca/egg mass.** Separate GOLD nodes, separate habitats — the meconium event at pupation is precisely what makes them separate.
6. **`UBERON:0000069` larval stage** — the temporal stage, not the organism.
7. **Crustacean larva** (`Host-associated > Arthropoda: Crustaceans > Larva`, `gold.ecosystem:7343`) — a distinct HabitatMech record; nauplius/zoea stages, not insects.
8. **Edible insect larvae as a food product** (`FOODON:00001177` insect food product) — a food role, not a habitat.
9. **Insect cell lines** (GOLD has `Arthropoda: Chelicerates > Cell Line > ISE6`) — cultured cells, not an organism.

---

## 6. Should this be a term at all?

**Yes — keep the minted identity.** This is a host organism acting as a habitat, which is exactly the case CLAUDE.md's #114 rule says gets its own identity plus an `<X>-associated environment` term request. The existing decision (`CONFIRM_UNGROUNDED`, UBERON:0002548 as `relation: xref`) is correct as recorded and needs no change; what this research adds is the definition text and the evidence that would back an ENVO request.

Three points a curator should weigh before writing the record, in order of how much they could change the outcome:

**(a) There is a real argument that this is a host *attribute*, not a habitat, and it should be answered rather than ignored.** MIxS models developmental stage as `host_life_stage` (MIXS:0000251) — a free-text field in the host descriptor block, next to `host_taxid` and `host_body_site` — not as an environment. On that view, "larva" qualifies a host rather than naming a place, and a record for it is a modelling artefact of GOLD flattening two orthogonal axes (host stage × body site) into one path. The counter-argument, which I think wins, is empirical: metamorphosis eliminates the larval gut wholesale, larval and adult communities of the same species diverge measurably (§3a), and the larval gut's physicochemistry has no adult counterpart (§3b). A larval insect is not the same place as the adult it becomes. But this should be stated in the record's notes, because the next curator will otherwise re-litigate it.

**(b) The ENVO gap is two terms deep, not one.** There is no `insect-associated environment` and no `arthropod-associated environment` in ENVO at all — the taxon-scoped pattern exists (`plant-associated`, `fungi-associated`, `cnidarian-associated`, `environment associated with an aquatic invertebrate`) but stops before arthropods. A request for `insect larva-associated environment` without a parent `insect-associated environment` would dangle. The parent request belongs on `habitatmech:GOLD.dba2a83b95`, and this record's request depends on it. `ENVO:01001176` is the shape to copy: `subClassOf` both `ENVO:01001002` and `ENVO:01001055`.

**(c) `ENVO:01001055` is worth a deliberate decision.** "Environment associated with an animal part or small animal" is genuinely broader than an insect larva and could be added to `parent_habitats` today with no new ENVO term. I would *not* add it: it sits under `ENVO:01001110` ecosystem, and asserting that a single larva is an ecosystem "which includes both living and non-living components" is a claim GOLD's 94 assertions do not make. Recording the near-miss and the reason is more useful than the edge.

**No ENVO or FoodOn submission is implied by any of the above** — per the standing rule, a term request needs an explicit go-ahead for that specific request.

---

## Sources

- [GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification) · [IMG/GOLD Terms glossary](https://sites.google.com/lbl.gov/imghelp/home/img-and-gold-terms)
- [MIxS: host life stage (MIXS:0000251)](https://genomicsstandardsconsortium.github.io/mixs/0000251/) · [MIxS HostAssociated extension](https://genomicsstandardsconsortium.github.io/mixs/0016002/)
- [OLS4 — UBERON:0002548 larva](https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON:0002548) · [ENVO:01001002](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002) · [ENVO:01001055](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001055)
- [Engel & Moran 2013, FEMS Microbiol. Rev.](https://academic.oup.com/femsre/article/37/5/699/542120)
- [Hammer & Moran 2019, Phil. Trans. R. Soc. B](https://royalsocietypublishing.org/doi/10.1098/rstb.2019.0068)
- [Hammer et al. 2017, PNAS](https://www.pnas.org/doi/10.1073/pnas.1707186114) · [PubMed 28830993](https://pubmed.ncbi.nlm.nih.gov/28830993/)
- [Complete metamorphosis and microbiota turnover in insects, Mol. Ecol. 2022](https://onlinelibrary.wiley.com/doi/10.1111/mec.16673)
- [Lemke et al. 2003, Appl. Environ. Microbiol.](https://journals.asm.org/doi/10.1128/aem.69.11.6650-6658.2003)
- [Dow 1992, J. Exp. Biol.](https://journals.biologists.com/jeb/article/172/1/355/6581/pH-gradients-in-lepidopteran-midgut) · [PubMed 9874748](https://pubmed.ncbi.nlm.nih.gov/9874748/)
- [Berenbaum 1980, Am. Nat.](https://www.journals.uchicago.edu/doi/abs/10.1086/283551)
- [Coon et al. 2014, Mol. Ecol.](https://onlinelibrary.wiley.com/doi/10.1111/mec.12771) · [Correa et al. 2018, Nat. Commun.](https://www.nature.com/articles/s41467-018-07014-2)
- [Larval habitat determines Aedes aegypti microbiota, FEMS Microbiol. Ecol. 2022](https://academic.oup.com/femsec/article/98/1/fiac016/6526867) · [Co-rearing study, Sci. Rep. 2020](https://www.nature.com/articles/s41598-020-60075-6)
- [BSFL gut microbiome editorial, Front. Microbiol. 2024](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2024.1441577/full) · [BSFL 16S meta-analysis, PMC9453823](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9453823/)
- [Anopheles albimanus internal vs. cuticle microbiota, PMC8542342](https://pmc.ncbi.nlm.nih.gov/articles/PMC8542342/)
- [Insect gut microbiome ecological–evolutionary review, Vet. Sci. 2025](https://doi.org/10.3390/vetsci12090866)

## Citations

1. https://gold.jgi.doe.gov/ecosystem_classification
2. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9453823/
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC8542342/
4. https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON:0002548
5. https://royalsocietypublishing.org/doi/10.1098/rstb.2019.0068
6. https://onlinelibrary.wiley.com/doi/10.1111/mec.16673
7. https://journals.biologists.com/jeb/article/172/1/355/6581/pH-gradients-in-lepidopteran-midgut
8. https://pubmed.ncbi.nlm.nih.gov/9874748/
9. https://journals.asm.org/doi/10.1128/aem.69.11.6650-6658.2003
10. https://academic.oup.com/femsre/article/37/5/699/542120
11. https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2024.1441577/full
12. https://academic.oup.com/femsec/article/98/1/fiac016/6526867
13. https://onlinelibrary.wiley.com/doi/10.1111/mec.12771
14. https://www.nature.com/articles/s41467-018-07014-2
15. https://www.pnas.org/doi/10.1073/pnas.1707186114
16. https://doi.org/10.1111/1574-6976.12025
17. https://doi.org/10.1098/rstb.2019.0068
18. https://doi.org/10.1073/pnas.1707186114
19. https://doi.org/10.1111/mec.16673
20. https://doi.org/10.1128/AEM.69.11.6650-6658.2003
21. https://doi.org/10.1086/283551
22. https://doi.org/10.1111/mec.12771
23. https://doi.org/10.1038/s41467-018-07014-2
24. https://doi.org/10.1093/femsec/fiac016
25. https://doi.org/10.3389/fmicb.2024.1441577
26. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11224508/
27. https://doi.org/10.3390/vetsci12090866
28. https://sites.google.com/lbl.gov/imghelp/home/img-and-gold-terms
29. https://genomicsstandardsconsortium.github.io/mixs/0000251/
30. https://www.ebi.ac.uk/ols4/
31. https://www.nature.com/articles/s41598-020-60075-6
32. https://genomicsstandardsconsortium.github.io/mixs/0016002/
33. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002
34. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001055
35. https://pubmed.ncbi.nlm.nih.gov/28830993/
36. https://www.journals.uchicago.edu/doi/abs/10.1086/283551