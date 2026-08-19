---
provider: claude_code
model: claude-opus-5
cached: false
start_time: '2026-08-17T16:33:58.096872'
end_time: '2026-08-17T16:43:16.486843'
duration_seconds: 558.39
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: 'Arthropoda: Crustaceans'
  habitat_identifier: habitatmech:GOLD.2959225799
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Arthropoda: Crustaceans'
  assertions: '598'
  parent_terms: ENVO:01001000, ENVO:01001002
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Nearest
    broader term ENVO:01001002 ''animal-associated environment'' attached as a parent.
    Crustaceans as host. ENVO:01001176 environment associated with an aquatic invertebrate
    is close but excludes terrestrial crustaceans, so it is not a safe identity either.
    ENVO term request. (source concept habitatmech:GOLD.2959225799)'
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
  - claude-opus-5
  web_search_requests: 18
  num_turns: 27
  total_cost_usd: 3.6750805
  session_id: 303ce7f1-d5e3-4907-ba89-495cbd945e2f
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 50
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Arthropoda: Crustaceans
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.2959225799
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Arthropoda: Crustaceans
- **Upstream assertion volume:** 598
- **Nearest broader term already on the record:** ENVO:01001000, ENVO:01001002
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term ENVO:01001002 'animal-associated environment' attached as a parent. Crustaceans as host. ENVO:01001176 environment associated with an aquatic invertebrate is close but excludes terrestrial crustaceans, so it is not a safe identity either. ENVO term request. (source concept habitatmech:GOLD.2959225799)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Arthropoda: Crustaceans** as a microbial habitat, with citations.

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

# Definition research: *Arthropoda: Crustaceans* (`habitatmech:GOLD.2959225799`)

> **Proposed definition:** An animal-associated environment [ENVO:01001002] which is determined by a living crustacean [NCBITaxon:6657], comprising that animal's body surfaces and internal compartments as sites of microbial colonisation.

Suggested label for the term request: **crustacean-associated environment** (sibling of the existing `ENVO:01001179` *cnidarian-associated environment*, and of the parallel request for `habitatmech:GOLD.dba2a83b95` *Arthropoda: Insects*).

The enumeration of compartments (cuticle, branchial chamber, gut, hepatopancreas, haemolymph) belongs in a term comment or in the child records, not in the definition sentence — see §3, where I argue the compartment list is corroborating evidence for the class being useful, not part of its differentia.

---

## 1. What the concept denotes

**The concept is a host organism acting as an environment, not a taxon and not a body part.** The thing a sample is taken from is a living crustacean — the animal's surfaces and interior — sampled either whole or by compartment.

### Evidence from the source path itself

The GOLD ecosystem classification is a five-level hierarchy (`Ecosystem > Ecosystem Category > Ecosystem Type > Ecosystem Subtype > Specific Ecosystem`) in which *Host-associated* is one of three top-level ecosystems, and the second level names the host group ([Mukherjee et al. 2023, *NAR* 51:D957–D963, doi:10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974)). `Arthropoda: Crustaceans` sits at that second level, so it is structurally the same kind of thing as `Mammals`, `Fish`, `Plants` — a host group, expanded downward by organ system.

`data/raw/gold_ecosystem_paths.tsv` carries **47 paths** under this node. Their shape settles what the concept denotes:

| Sub-branch | Leaves present | Assertions on that exact path |
|---|---|---|
| `Digestive system` | Foregut (cardiac/pyloric stomach, oesophagus), Midgut (caeca, **hepatopancreas**), Hindgut (anterior chamber, papillate region, rectum, fecal), Gut > Intestine, Mouth | gut 30, digestive system 5, hepatopancreas 5, intestine 3, hindgut 1, stomach 1 |
| `Circulatory system` | Heart, **Hemolymph** | hemolymph 6 |
| `Respiratory system` | (gill; grounded separately as `UBERON:0002535`) | 0 |
| `Excretory system` | Antennal/Green glands, Maxillary glands | 0 |
| `Integumentary system` | **Cuticle** > Setae | 0 |
| `Reproductive system` | Ovaries, Gonopore | 0 |
| `Whole body` | Cephalothorax, Head/Cephalon, Thorax/Pereon, Abdomen/Pleon | 0 |
| Life stages | Larva (> Gut, Whole body), Larva: Nauplius, Larva: Zoea, Post-larva | nauplius 1 |
| **The clade node itself** | — | **598** |

The 598 assertions are `organism_count` on the *exact* path `Host-associated > Arthropoda: Crustaceans`, i.e. sequenced organisms whose recorded environment is "a crustacean" with no compartment resolution at all; the compartment-resolved paths together carry only ~52. So the dominant real-world usage of this concept is *microorganism isolated from a crustacean*, host clade being the only environmental fact recorded.

### Boundary — what is inside

- Living crustaceans of any habitat: marine, freshwater and terrestrial (see §3 on terrestrial forms).
- All compartments of the individual animal, when a compartment is not separately named: cuticular surfaces and setae, branchial (gill) chamber, foregut/midgut/hindgut, midgut gland (hepatopancreas), haemolymph and haemocoel, antennal and maxillary glands, gonads.
- All post-embryonic life stages of that animal (nauplius, zoea, post-larva, adult). Per this repo's rule, a *larva* is the whole organism at a life stage, so `Larva`, `Larva: Nauplius`, `Larva: Zoea` and `Post-larva` are themselves organism-as-habitat concepts nested inside this one, not anatomical parts.

### Boundary — what is a neighbouring concept

- **Body parts with their own anatomy terms.** `gill` (`UBERON:0002535`), `antennal gland` (`UBERON:0009963`), `crustacean maxillary gland` (`UBERON:0009964`), `abdomen` (`UBERON:0000916`), `thorax` (`BTO:0001368`) are already grounded in `curation/decisions.tsv` for the child paths. They ground to the anatomy term; the whole animal does not.
- **The water the animal lives in.** `shrimp pond` (`ENVO:01000905`), `saline shrimp pond water` (`ENVO:01001257`) and `coastal shrimp pond` (`ENVO:01001256`) are environmental water bodies, not host-associated environments, even though the sampled microbes overlap heavily.
- **Crustacean-derived material after death or processing.** Shed exuviae, carcasses, shell waste and seafood are FoodOn/environmental-material territory (`FOODON:00005683` *aquatic invertebrate material*, `FOODON:00001176` *invertebrate food product*), not this class. This matters ecologically: exuviae and carcasses support distinct chitin-degrading communities from the live animal ([Helgoland Mar. Res., doi:10.1007/BF02368350](https://link.springer.com/article/10.1007/BF02368350)).
- **Insects.** The sibling GOLD node `Host-associated > Arthropoda: Insects` (1,833 assertions, `habitatmech:GOLD.dba2a83b95`). Phylogenetically insects sit *inside* the crustacean radiation (§5), but GOLD's two nodes are mutually exclusive in use.

### Ambiguity — three readings, and which one the data means

1. **The crustacean host as an environment** (the individual animal as the place microbes live). *This is the reading the GOLD path supports*: the node is under `Host-associated`, is expanded by organ system, and takes assertions directly.
2. **The taxon Crustacea** (a class of organisms). Not a place; this is the reading that must *not* be adopted as the term's identity, per the repo's rule that the taxon term goes in `relation: xref`.
3. **Crustacean material as a substrate** (chitin, shell waste, seafood). Reachable from the bare label; excluded by the `Host-associated` prefix.

I record reading 1 as the intended one and readings 2–3 as excluded. This is an inference from the path structure and the GOLD schema paper, not a statement any source makes about this label.

---

## 2. Genus — the broader kind

**Genus: `ENVO:01001002` *animal-associated environment***, defined in ENVO as an environmental system determined by an animal, and itself a child of `ENVO:01001000` *environmental system determined by an organism* ([ENVO, OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002); [Buttigieg et al. 2013, *J. Biomed. Semantics* 4:43, PMC3904460](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3904460/); [Buttigieg et al. 2016, *J. Biomed. Semantics* 7:57, PMC5035502](https://pmc.ncbi.nlm.nih.gov/articles/PMC5035502/)). This is already the parent on the record, and it is the right genus.

**There is no crustacean-, arthropod- or insect-associated class in ENVO.** Queried against OLS4 on 2026-08-17, `ENVO:01001002` has exactly three asserted children: `ENVO:01001176`, `ENVO:01001179`, and `ENVO:01001829` *human settlement*. A text search of ENVO for "crustacean" returns only `ENVO:01001249` *crustacean farming process*, `ENVO:01000905` *shrimp pond* and relatives; for "arthropod", nothing in ENVO at all.

### Near-misses and why each fails

| Candidate | Why it is not the identity |
|---|---|
| **`ENVO:01001176` *environment associated with an aquatic invertebrate*** | Defined as "An environment which has its properties and composition largely determined by the presence of a metazoan which lacks a vetebral column and which has a habitat that is found in an aquatic environmental system" (typo is ENVO's). Two failures: (a) **too narrow** — it excludes the terrestrial crustaceans (§3), which are a real and microbiologically studied part of the concept; (b) **too broad in the other direction** — it covers molluscs, cnidarians, echinoderms, aquatic worms. It is also asserted under `ENVO:01001055` *environment associated with an animal part or small animal*, so adopting it as parent would additionally assert the host is a *small animal or a part*, which is false for lobsters and land crabs. It has **no children**, so nothing about crustacean sub-structure is available there. The curator's existing note reaches the same conclusion; this research confirms it and adds the second reason. |
| **`ENVO:01001179` *cnidarian-associated environment*** | Not a match, but the **most useful precedent**: its definition is "An environmental system determined by a cnidarian or part of a cnidarian" — a clade-level host-associated environment class asserted directly under `ENVO:01001002`. It establishes both that ENVO admits clade-level host environments and the definitional pattern the new term should copy. |
| **`ENVO:01001055` *environment associated with an animal part or small animal*** | Asserts "part or small animal". Decapods are neither; and the concept covers whole animals. |
| **`NCBITaxon:6657` Crustacea (subphylum)** | A class of organisms, not a place. Correct disposition: `relation: xref` on the record, per the repo's host-vs-taxon rule. |
| **`UBERON:0002535` gill, `UBERON:0009963` antennal gland, `UBERON:0009964` crustacean maxillary gland** | Anatomical parts; already used for the child paths. Narrower than the concept. |
| **`ENVO:01000905` shrimp pond / `ENVO:01001257` saline shrimp pond water** | Aquaculture water bodies. Environmental, not host-associated; asserts a built structure the concept does not. |
| **`ENVO:01001249` crustacean farming process** | A process, not an environment. |
| **`FOODON:00005683` aquatic invertebrate material / `CHEBI:83039` crustacean metabolite** | Material and chemical entities respectively; wrong upper-level branch. |

All five of the ENVO CURIEs above (`01001000`, `01001002`, `01001055`, `01001176`, `01001179`) plus `UBERON:0002535` are present in this repo's vendored slice (`data/raw/ontology_terms.tsv`), so the label check on a `GROUND`/parent assertion will resolve.

**On where the request should go:** ENVO's own tracker already carries [issue #1029, "EnvO terms for host-associated samples"](https://github.com/EnvironmentOntology/envo/issues/1029), asking for host-associated / animal-associated / plant-associated environmental-context terms, and the related [GSC MIxS issue #196](https://github.com/GenomicsStandardsConsortium/mixs/issues/196) on symbiont-host `env_medium` values. Neither requests a crustacean or arthropod class. *(No submission has been made and none should be made without explicit per-request permission.)*

---

## 3. Differentia — what distinguishes it

**The differentia is the host clade: the environment is determined by a crustacean rather than by some other animal.** That is the only property that is definitionally necessary and sufficient, and it is what separates this class from its would-be siblings (`cnidarian-associated`, an insect-associated class, `fish-associated`, and so on). Everything below is *corroborating* — it shows the class carves at a real joint and that its members share observable structure — but writing any of it into the definition would over-claim, because none of it holds of every crustacean.

### 3a. Host clade and its scope

Crustacea comprises roughly **66,914 described Recent species in 9,522 genera and 1,003 families** ([Ahyong et al. 2011, in Zhang (ed.), *Zootaxa* 3148:165–191](https://www.mapress.com/zt/article/view/zootaxa.3148.1.33)), with Decapoda alone now at **17,229 species in 2,550 genera** ([De Grave et al. 2023, *J. Crustacean Biol.* 43(3):ruad042](https://academic.oup.com/jcb/article/43/3/ruad042/7234762)). The group spans marine, freshwater and terrestrial systems; Oniscidea (woodlice) alone comprise **>3,700 species** and are the only crustaceans that complete their entire life cycle on land ([Broly et al. 2013, *Evol. Ecol.* 27:461–476](https://link.springer.com/article/10.1007/s10682-012-9625-8); [phylogenomic support for a single terrestrialisation, 2024, PMC11521608](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11521608/)). **This is the fact that kills `ENVO:01001176` as an identity.**

### 3b. Mineralised cuticle — a surface habitat unlike the insect one

The crustacean cuticle is a chitin–protein composite **mineralised with calcium carbonate** (calcite plus amorphous CaCO₃), layered as epicuticle / exocuticle / endocuticle over an uncalcified membranous layer ([Roer & Dillaman 1984, *Integr. Comp. Biol.* 24:893](https://academic.oup.com/icb/article/24/4/893/116464); [Luquet 2012, PMID 22201907](https://pubmed.ncbi.nlm.nih.gov/22201907/); [structural diversity review, PMC11008965](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11008965/)). Insects instead harden cuticle by **sclerotisation** — laccase-catalysed catecholamine crosslinking — and essentially do not calcify ([Asano 2023, *Physiol. Entomol.*, doi:10.1111/phen.12406](https://resjournals.onlinelibrary.wiley.com/doi/10.1111/phen.12406)). Chitin is ~4% of krill dry weight and, because crustaceans dominate zooplankton biomass, crustacean chitin is arguably the most abundant biopolymer in the sea ([Pruzzo, Vezzulli & Colwell 2008, *Environ. Microbiol.* 10:1400, doi:10.1111/j.1462-2920.2007.01559.x](https://enviromicro-journals.onlinelibrary.wiley.com/doi/full/10.1111/j.1462-2920.2007.01559.x)).

Microbiologically this surface is a defined habitat, not an incidental boundary: *Vibrio cholerae* attaches specifically to live copepod surfaces — heaviest at the oral region and egg sac — while *Pseudomonas* and *E. coli* do not, and this attachment underpins the environmental-reservoir model of cholera ([Huq et al. 1983, *Appl. Environ. Microbiol.* 45:275–283, doi:10.1128/aem.45.1.275-283.1983](https://journals.asm.org/doi/10.1128/aem.45.1.275-283.1983); PMID [6337551](https://pubmed.ncbi.nlm.nih.gov/6337551/)).

### 3c. Moult-driven turnover

Because the cuticle — including the lining of the branchial chamber — is shed at each moult, the surface-associated community is periodically reset, and epibiont acquisition is a recurring life-cycle event rather than a one-off colonisation ([Guri et al. 2012, "Acquisition of epibiotic bacteria along the life cycle of *Rimicaris exoculata*", PMID 21993397 / PMC3280129](https://ncbi.nlm.nih.gov/pmc/articles/PMC3280129); krill epibionts and moult, [Sci. Rep. 6:36496](https://www.nature.com/articles/srep36496)). I have not found a source asserting that moult-driven reset is *unique* to crustaceans among arthropods — it is not — so this is a characteristic, not a discriminator.

### 3d. The branchial chamber as a compartment

The enlarged gill chamber of vent shrimp houses dense chemoautotrophic ectosymbionts — Campylobacteria (rTCA carbon fixation) and Gammaproteobacteria (CBB cycle), plus iron-oxidising Zetaproteobacteria — with nutrition transferred to the host by transtegumental absorption of soluble bacterial products ([Jan et al. 2014, *Environ. Microbiol.* 16:2723, doi:10.1111/1462-2920.12406](https://enviromicro-journals.onlinelibrary.wiley.com/doi/10.1111/1462-2920.12406); ["*Ca.* Desulfobulbus rimicarensis*", PMID 32060020](https://pubmed.ncbi.nlm.nih.gov/32060020/); [*R. chacei* gill chamber and gut, PMC6214521](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6214521/)). This is the clearest case of a crustacean-specific organ that is itself a microbial habitat, and GOLD's `Respiratory system` sub-branch reflects it.

### 3e. Gut and hepatopancreas

A meta-analysis of 627 Illumina datasets from 25 studies across 11 cultured decapod species (crab, crayfish, lobster, prawn, shrimp) found *Vibrio* as effectively the only core genus (95.5% relative population frequency at a 1% threshold), with *Bacilloplasma* in 78.4% and *Aeromonas* in 67.5% of samples, and salinity of the host's habitat structuring the community ([Zhang et al. 2023, *Heliyon*, PMC10238905](https://pmc.ncbi.nlm.nih.gov/articles/PMC10238905/)). The midgut gland (hepatopancreas) houses named lineage-specific symbionts in terrestrial isopods — "*Candidatus* Hepatoplasma crinochetorum" (Mollicutes, ~657 kb reduced genome) and "*Ca.* Hepatincola porcellionum" ([Leclercq et al. 2014, *Genome Biol. Evol.* 6:407](https://academic.oup.com/gbe/article/6/2/407/536054); [Collingro et al. 2015, *Genome Announc.*, doi:10.1128/genomea.00674-15](https://journals.asm.org/doi/10.1128/genomea.00674-15); [Hepatoplasmataceae MAGs, *Access Microbiol.*, doi:10.1099/acmi.0.000592.v3](https://www.microbiologyresearch.org/content/journal/acmi/10.1099/acmi.0.000592.v3); [*Ca.* Hepatincola genome, PMC9992710](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9992710/)). Mangrove brachyuran crabs show phylosymbiosis and codiversification in gut communities ([*Mol. Ecol.* 2024, doi:10.1111/mec.17377](https://onlinelibrary.wiley.com/doi/full/10.1111/mec.17377)); spiny lobster GI communities are dominated by *Vibrio*, *Pseudomonas*, *Aeromonas*, *Pseudoalteromonas*, *Photobacterium*, *Plesiomonas* ([*Fishes* 7:108, doi:10.3390/fishes7030108](https://doi.org/10.3390/fishes7030108)).

### 3f. Haemolymph — a compartment GOLD names and that is not sterile

Crustacean haemolymph, long assumed sterile, carries endemic communities under tight host immune control, dominated by Bacteroidota, Pseudomonadota, Bacillota and Planctomycetota, apparently seeded from the gut across the open circulatory system ([Wang & Wang 2015, *Dev. Comp. Immunol.*, PMID 26153452](https://pubmed.ncbi.nlm.nih.gov/26153452/); [Zhang et al. 2018, *Appl. Environ. Microbiol.*, PMC5881060](https://pmc.ncbi.nlm.nih.gov/articles/PMC5881060/); [*ISME J* 2025 review, wraf133](https://academic.oup.com/ismej/article/19/1/wraf133/8177086)). Six of the 598-adjacent assertions sit on the `Circulatory system > Hemolymph` path, so this is attested usage, not a curiosity.

### 3g. Fitness dependence — the host is a habitat in the strong sense

Germ-free *Daphnia magna* grow and reproduce less than conventionalised animals, with the strength of the mutualism depending on food availability ([Callens et al. 2016, *ISME J* 10:911](https://www.nature.com/articles/ismej2015166)); microbiota inoculum composition determines holobiont assembly and host growth ([Callens et al. 2018, *Microbiome* 6:56, doi:10.1186/s40168-018-0444-1](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-018-0444-1)); and host-genotype-dependent gut microbiota drives tolerance to toxic cyanobacteria ([Macke et al. 2017, *Nat. Commun.* 8:1608](https://www.nature.com/articles/s41467-017-01714-x)). In aquaculture, AHPND-causing *Vibrio parahaemolyticus* induces measurable gut dysbiosis in *Penaeus vannamei* within 6 h ([Chang et al. 2023, *Microbiol. Spectr.*, doi:10.1128/spectrum.01180-23](https://journals.asm.org/doi/10.1128/spectrum.01180-23)).

### 3h. Ecosystem-scale relevance

Copepod-associated communities express chitinases and other CAZymes that convert recalcitrant host- and diet-derived polymers into assimilable carbon, linking this habitat to the biological carbon pump ([Calbet et al. 2026, *Environ. Microbiol.*, doi:10.1111/1462-2920.70271](https://enviromicro-journals.onlinelibrary.wiley.com/doi/full/10.1111/1462-2920.70271); [mesopelagic copepod gut isolates, *J. Plankton Res.* 46:48, doi:10.1093/plankt/fbad049](https://doi.org/10.1093/plankt/fbad049)).

---

## 4. Sources

Grouped by what they support. Publication dates in parentheses.

**Ontology and standards**
- ENVO classes as served by OLS4, queried 2026-08-17: [`ENVO:01001002`](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002), [`ENVO:01001176`](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001176), [`ENVO:01001179`](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001179), [`ENVO:01001055`](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001055).
- Buttigieg et al. (2013) *J. Biomed. Semantics* 4:43 — [PMC3904460](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3904460/); Buttigieg et al. (2016) *J. Biomed. Semantics* 7:57 — [PMC5035502](https://pmc.ncbi.nlm.nih.gov/articles/PMC5035502/).
- ENVO issue [#1029, host-associated sample terms](https://github.com/EnvironmentOntology/envo/issues/1029); GSC MIxS issue [#196, symbiont hosts in `env_medium`](https://github.com/GenomicsStandardsConsortium/mixs/issues/196).
- Mukherjee et al. (2023) *NAR* 51:D957–D963, GOLD v.9 — [doi:10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974).

**Host clade scope and phylogeny**
- Ahyong et al. (2011) *Zootaxa* 3148:165–191 — [mapress](https://www.mapress.com/zt/article/view/zootaxa.3148.1.33).
- De Grave et al. (2023) *J. Crustacean Biol.* 43(3):ruad042 — [OUP](https://academic.oup.com/jcb/article/43/3/ruad042/7234762).
- Broly, Deville & Maillet (2013) *Evol. Ecol.* 27:461–476 — [Springer](https://link.springer.com/article/10.1007/s10682-012-9625-8); single origin of isopod terrestriality (2024) — [PMC11521608](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11521608/).
- Regier et al. (2010) *Nature* 463:1079–1083; von Reumont et al. (2012) *Mol. Biol. Evol.* 29:1031–1045 — [OUP](https://academic.oup.com/mbe/article/29/3/1031/1007908); Lozano-Fernandez et al. (2019) *Genome Biol. Evol.* 11:2055 — [OUP](https://academic.oup.com/gbe/article/11/8/2055/5528088); Bernot et al. (2023) *Mol. Biol. Evol.* 40:msad175 — [PMC10414812](https://pmc.ncbi.nlm.nih.gov/articles/PMC10414812/).

**Cuticle**
- Roer & Dillaman (1984) *Integr. Comp. Biol.* 24:893 — [OUP](https://academic.oup.com/icb/article/24/4/893/116464); Luquet (2012) — [PMID 22201907](https://pubmed.ncbi.nlm.nih.gov/22201907/); structural diversity review — [PMC11008965](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11008965/); Asano (2023) *Physiol. Entomol.* — [doi:10.1111/phen.12406](https://resjournals.onlinelibrary.wiley.com/doi/10.1111/phen.12406).

**Microbial communities by compartment**
- Surface/chitin: Huq et al. (1983) *AEM* 45:275–283 — [doi:10.1128/aem.45.1.275-283.1983](https://journals.asm.org/doi/10.1128/aem.45.1.275-283.1983); Pruzzo et al. (2008) *Environ. Microbiol.* 10:1400 — [doi:10.1111/j.1462-2920.2007.01559.x](https://enviromicro-journals.onlinelibrary.wiley.com/doi/full/10.1111/j.1462-2920.2007.01559.x); copepod surface colonisation — [doi:10.1007/BF02368350](https://link.springer.com/article/10.1007/BF02368350).
- Gill chamber: Jan et al. (2014) — [doi:10.1111/1462-2920.12406](https://enviromicro-journals.onlinelibrary.wiley.com/doi/10.1111/1462-2920.12406); Guri et al. (2012) — [PMC3280129](https://ncbi.nlm.nih.gov/pmc/articles/PMC3280129); *Ca.* Desulfobulbus rimicarensis (2020) — [PMID 32060020](https://pubmed.ncbi.nlm.nih.gov/32060020/); *R. chacei* (2018) — [PMC6214521](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6214521/); dual digestive symbiosis — [PMC9636832](https://pmc.ncbi.nlm.nih.gov/articles/PMC9636832/).
- Gut/hepatopancreas: decapod meta-analysis (2023) — [PMC10238905](https://pmc.ncbi.nlm.nih.gov/articles/PMC10238905/); spiny lobster review (2022) — [doi:10.3390/fishes7030108](https://doi.org/10.3390/fishes7030108); mangrove crabs (2024) — [doi:10.1111/mec.17377](https://onlinelibrary.wiley.com/doi/full/10.1111/mec.17377); Leclercq et al. (2014) — [OUP](https://academic.oup.com/gbe/article/6/2/407/536054); Collingro et al. (2015) — [doi:10.1128/genomea.00674-15](https://journals.asm.org/doi/10.1128/genomea.00674-15); Hepatoplasmataceae MAGs — [doi:10.1099/acmi.0.000592.v3](https://www.microbiologyresearch.org/content/journal/acmi/10.1099/acmi.0.000592.v3); *Ca.* Hepatincola — [PMC9992710](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9992710/); *Armadillidium* tissue microhabitats — [*FEMS Microbiol. Ecol.* 92:fiw063](https://academic.oup.com/femsec/article/92/5/fiw063/2470073); feminising *Wolbachia* and microbiota — [*Sci. Rep.* 8, doi:10.1038/s41598-018-25450-4](https://www.nature.com/articles/s41598-018-25450-4).
- Haemolymph: Wang & Wang (2015) — [PMID 26153452](https://pubmed.ncbi.nlm.nih.gov/26153452/); Zhang et al. (2018) — [PMC5881060](https://pmc.ncbi.nlm.nih.gov/articles/PMC5881060/); *ISME J* (2025) — [wraf133](https://academic.oup.com/ismej/article/19/1/wraf133/8177086); *E. sinensis* infection — [PMC10571569](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10571569/).
- Host dependence and disease: Callens et al. (2016) — [*ISME J* 10:911](https://www.nature.com/articles/ismej2015166); Callens et al. (2018) — [doi:10.1186/s40168-018-0444-1](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-018-0444-1); Macke et al. (2017) — [doi:10.1038/s41467-017-01714-x](https://www.nature.com/articles/s41467-017-01714-x); Chang et al. (2023) — [doi:10.1128/spectrum.01180-23](https://journals.asm.org/doi/10.1128/spectrum.01180-23).
- Ecosystem scale: krill microorganisms — [*Sci. Rep.* 6:36496](https://www.nature.com/articles/srep36496); Calbet et al. (2026) — [doi:10.1111/1462-2920.70271](https://enviromicro-journals.onlinelibrary.wiley.com/doi/full/10.1111/1462-2920.70271); mesopelagic copepod gut — [doi:10.1093/plankt/fbad049](https://doi.org/10.1093/plankt/fbad049).

**Stated plainly as my inference, not sourced:** (a) that GOLD's `Arthropoda: Crustaceans` means reading 1 of §1 — inferred from the path's position under `Host-associated` and the GOLD schema paper, not asserted anywhere; (b) that the host clade alone should carry the differentia — an ontological judgement; (c) the claim that the 598 assertions are compartment-unresolved — read off the `organism_count` column of `data/raw/gold_ecosystem_paths.tsv`, which counts organisms annotated to that exact path.

---

## 5. Synonyms, and what NOT to conflate

**Names in real use for this concept**
- crustacean-associated environment; crustacean host environment
- crustacean microbiome / crustacean holobiont (community-centric phrasing of the same habitat)
- crustacean-associated microbial habitat
- GOLD's own string: `Host-associated > Arthropoda: Crustaceans`
- narrower usages that fall inside it: shrimp-associated, crab-associated, copepod-associated, zooplankton-associated (partly), *Daphnia*-associated, woodlouse/isopod-associated

**Do not conflate**
- **Crustacea the taxon (`NCBITaxon:6657`).** A class of organisms, not a place. Correct disposition here: `relation: xref`. Making it the identity is the error #114 records.
- **Insect-associated environments.** Distinct in GOLD and in practice — *and* the phylogenetic relationship is the reverse of the intuitive one: Hexapoda nests *inside* the crustacean radiation (Pancrustacea), so traditional "Crustacea" is paraphyletic ([Regier et al. 2010](https://www.nature.com/articles/nature08742); [von Reumont et al. 2012](https://academic.oup.com/mbe/article/29/3/1031/1007908); [Lozano-Fernandez et al. 2019](https://academic.oup.com/gbe/article/11/8/2055/5528088)). A definition that says "crustacean" is naming the traditional grouping, not a clade; if the curator wants to be exact, `Pancrustacea excluding Hexapoda` is the extension GOLD means. Flagging this is important because an ontology reasoner given both a crustacean-associated and an insect-associated class plus NCBITaxon axioms could otherwise be led to subsume one under the other.
- **"Shellfish" and seafood.** Conflates crustaceans with bivalve molluscs and routes to FoodOn; see the sibling `Mollusca` record.
- **Aquatic-invertebrate-associated environments (`ENVO:01001176`).** Overlapping but neither broader nor narrower: it excludes terrestrial crustaceans and includes non-crustacean phyla.
- **Shrimp pond / aquaculture water (`ENVO:01000905`, `ENVO:01001257`).** The surrounding environmental medium, not the host.
- **Chitin as an environmental material, exuviae, carcasses, shell waste.** Shed or dead material; distinct communities and distinct upper-level branch.
- **Marine/freshwater biomes generally.** Where the host lives is not what the host is; the `Environmental` GOLD branch already covers those.
- **Crustacean farming (`ENVO:01001249`) and crustacean metabolite (`CHEBI:83039`).** A process and a chemical entity.

---

## 6. Should this be a term at all?

**Yes.** The evidence supports minting it, and supports `CONFIRM_UNGROUNDED` + parent `ENVO:01001002` as the current disposition, exactly as recorded:

1. **It is a place, not a taxon, process, quality or disease.** The concept picks out a living animal's surfaces and compartments as the site of microbial life. ENVO already models this pattern for animals, plants, fungi and cnidarians; `ENVO:01001179` *cnidarian-associated environment* is the direct precedent for a clade-level host environment class.
2. **Nothing in ENVO, UBERON, FoodOn, BTO or PO names it.** `ENVO:01001002` has three children and none is arthropod-related; `ENVO:01001176` fails on terrestrial crustaceans and on its "part or small animal" superclass; no ENVO class matches "arthropod" at all.
3. **It carries real volume and real sub-structure.** 598 assertions on the clade node itself, 47 GOLD paths beneath it covering seven organ systems and four life stages, and an independent literature demonstrating distinct microbial communities in at least four of those compartments (cuticle, branchial chamber, gut/hepatopancreas, haemolymph).
4. **`NOT_APPLICABLE` would be wrong here** — that disposition is reserved for diseases, qualities, processes and procedures, and `tests/test_decisions.py` fails on a `NOT_APPLICABLE` whose target is an organism term. This is a host acting as a habitat.

**Caveats a curator should carry forward.** The class is defined by host taxonomy, and taxonomic differentiae are weaker than physicochemical ones: the physical habitats a copepod's egg sac, a lobster's hepatopancreas and a woodlouse's midgut gland present to microbes have little in common beyond being crustacean. That is a general property of the whole `Host-associated > <clade>` level of GOLD, not a defect specific to this record — the same objection applies verbatim to the `Insects`, `Fish` and `Mammals` siblings, which is an argument for minting the set consistently rather than for withholding this one. If ENVO ever adds an intermediate `arthropod-associated environment`, this class and the insect one become its children with no change to either definition; proposing that intermediate alongside the two requests would be a reasonable move and I'd recommend mentioning it in the request text.

## Citations

1. https://doi.org/10.1093/nar/gkac974
2. https://link.springer.com/article/10.1007/BF02368350
3. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002
4. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3904460/
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC5035502/
6. https://github.com/EnvironmentOntology/envo/issues/1029
7. https://github.com/GenomicsStandardsConsortium/mixs/issues/196
8. https://www.mapress.com/zt/article/view/zootaxa.3148.1.33
9. https://academic.oup.com/jcb/article/43/3/ruad042/7234762
10. https://link.springer.com/article/10.1007/s10682-012-9625-8
11. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11521608/
12. https://academic.oup.com/icb/article/24/4/893/116464
13. https://pubmed.ncbi.nlm.nih.gov/22201907/
14. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11008965/
15. https://resjournals.onlinelibrary.wiley.com/doi/10.1111/phen.12406
16. https://enviromicro-journals.onlinelibrary.wiley.com/doi/full/10.1111/j.1462-2920.2007.01559.x
17. https://journals.asm.org/doi/10.1128/aem.45.1.275-283.1983
18. https://pubmed.ncbi.nlm.nih.gov/6337551/
19. https://ncbi.nlm.nih.gov/pmc/articles/PMC3280129
20. https://www.nature.com/articles/srep36496
21. https://enviromicro-journals.onlinelibrary.wiley.com/doi/10.1111/1462-2920.12406
22. https://pubmed.ncbi.nlm.nih.gov/32060020/
23. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6214521/
24. https://pmc.ncbi.nlm.nih.gov/articles/PMC10238905/
25. https://academic.oup.com/gbe/article/6/2/407/536054
26. https://journals.asm.org/doi/10.1128/genomea.00674-15
27. https://www.microbiologyresearch.org/content/journal/acmi/10.1099/acmi.0.000592.v3
28. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9992710/
29. https://onlinelibrary.wiley.com/doi/full/10.1111/mec.17377
30. https://doi.org/10.3390/fishes7030108
31. https://pubmed.ncbi.nlm.nih.gov/26153452/
32. https://pmc.ncbi.nlm.nih.gov/articles/PMC5881060/
33. https://academic.oup.com/ismej/article/19/1/wraf133/8177086
34. https://www.nature.com/articles/ismej2015166
35. https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-018-0444-1
36. https://www.nature.com/articles/s41467-017-01714-x
37. https://journals.asm.org/doi/10.1128/spectrum.01180-23
38. https://enviromicro-journals.onlinelibrary.wiley.com/doi/full/10.1111/1462-2920.70271
39. https://doi.org/10.1093/plankt/fbad049
40. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001176
41. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001179
42. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001055
43. https://academic.oup.com/mbe/article/29/3/1031/1007908
44. https://academic.oup.com/gbe/article/11/8/2055/5528088
45. https://pmc.ncbi.nlm.nih.gov/articles/PMC10414812/
46. https://pmc.ncbi.nlm.nih.gov/articles/PMC9636832/
47. https://academic.oup.com/femsec/article/92/5/fiw063/2470073
48. https://www.nature.com/articles/s41598-018-25450-4
49. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10571569/
50. https://www.nature.com/articles/nature08742