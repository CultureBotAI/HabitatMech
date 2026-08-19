---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T02:47:58.205194'
end_time: '2026-08-18T02:59:16.655788'
duration_seconds: 678.45
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Bacteria
  habitat_identifier: habitatmech:GOLD.a89688e0ba
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Endosymbionts > Bacteria'
  assertions: '1'
  parent_terms: (none)
  xrefs: NCBITaxon:2
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term NCBITaxon:2 'Bacteria' attached as a parent. Host-taxon reversal\
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
    \ not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.a89688e0ba)"
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
  num_turns: 30
  total_cost_usd: 3.3662025
  session_id: 310fb1f5-3acf-440e-95e2-e32c0030259c
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 29
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Bacteria
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.a89688e0ba
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Endosymbionts > Bacteria
- **Upstream assertion volume:** 1
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** NCBITaxon:2

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term NCBITaxon:2 'Bacteria' attached as a parent. Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it — the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE while its own child Porifera > Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM — a phylum is a class of organisms, not a place — so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.a89688e0ba)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Bacteria** as a microbial habitat, with citations.

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

# Bacteria (GOLD: *Host-associated > Endosymbionts > Bacteria*) — definition research

**Target:** `habitatmech:GOLD.a89688e0ba` · HOST_ASSOCIATED · UNGROUNDED · 1 GOLD organism · xref `NCBITaxon:2`

---

## Proposed definition

> **An environmental system determined by an organism in which the determining organism is a bacterium, comprising the cytoplasm, periplasm and outer cell surface of living bacterial cells as inhabited by other, taxonomically distinct microorganisms.**

Genus = `ENVO:01001000` *environmental system determined by an organism* (exact synonym: *host-associated environment*). Differentia = the determining organism is a bacterium rather than a plant, animal, fungus or cnidarian — the four host kinds ENVO already names.

**On the one-sentence rule.** The GOLD path puts this concept under *Endosymbionts*, so the fully faithful definition would also say "…bacterial cells that are themselves endosymbionts within a further host organism." That clause does not belong in this sentence: it is the differentia of the **parent** record, `habitatmech:GOLD.895a2372e5` ("Endosymbionts", currently `SEEDED` and undefined). The intermediate class is the missing piece. Define the parent as *an environmental system determined by an organism which is itself living as a symbiont inside another organism*, and this record's differentia collapses to the single word "bacterium." Recommend doing that rather than lengthening this sentence.

---

## 1. What the concept denotes

### The label is ambiguous — three readings, and they do not fully collapse

"Bacteria" sitting at Ecosystem Type under Ecosystem Category *Endosymbionts* can be read as:

**(A) Host-slot reading — the bacterium is the host.** The habitat is the interior (and surface) of a bacterial cell that harbours another microorganism. This is the reading every other Host-associated Ecosystem Category in the dump supports: `Algae, Amoebozoa, Amphibia, Annelida, Arthropoda: Chelicerates/Crustaceans/Insects/Myriapoda, Birds, Bryozoa, Cephalochordata, Ciliophora, Cnidaria, Endosymbionts, Fish, Fungi, Invertebrates, Mammals, Mammals: Human, Microbial, Mollusca, Plants, Porifera, Protists, Protozoa, Reptilia, Tunicates` — all host taxa except *Endosymbionts* (`data/raw/gold_ecosystem_paths.tsv`).

**(B) Compartment reading — the bacterial endosymbiont population of an unspecified host, considered as a place.** GOLD uses exactly this shape elsewhere in the same file: `Host-associated > Annelida > Intracellular endosymbionts > Trophosome` and `Host-associated > Microbial > Dinoflagellates > Endosymbionts`, where "endosymbionts" names a location *within* a host and the surrounding levels name the host. Under (B), `Endosymbionts > Bacteria` = the bacterial-endosymbiont compartment of some host, and `Endosymbionts > Fungi` = the fungal-endosymbiont compartment.

**(C) Sample-taxon reading — "Bacteria" names what was sequenced, not where it came from.** The sequenced organism is a bacterial endosymbiont of an unstated host, and the path is a taxonomic tag rather than a place.

Reading (B) is the strongest on internal evidence, for one specific reason: `Fungi` already exists as a Host-associated **Category** in its own right (`Host-associated > Fungi`, 635 assertions, sibling record `habitatmech:GOLD.a8fc5001d1`). If the type level under *Endosymbionts* named the **host**, `Endosymbionts > Fungi` would duplicate it. Naming the endosymbiont's own kingdom gives a clean, non-redundant partition of `{Bacteria, Fungi}`.

**Readings (A) and (B) converge on the same environmental entity and the same definition.** Under both, the thing a sample is taken from is *a living bacterial cell that other microorganisms occupy*; (B) merely adds that this bacterium is itself inside a further host. The definition above is true under both, and the parent record carries (B)'s extra restriction. Reading (C) is the one that would break the term — see §6.

I could not settle the ambiguity from GOLD itself: `gold.jgi.doe.gov/ecosystem_classification` and `/ecosystemtree` both return HTTP 403 to automated fetch, and the GOLD v.9/v.10 papers describe the five levels generically without documenting the *Endosymbionts* category ([Mukherjee et al. 2023](https://doi.org/10.1093/nar/gkac974); [GOLD v.10, NAR 2025](https://academic.oup.com/nar/article/53/D1/D989/7875979)). **The reading argument above is my inference from the path structure in `data/raw/gold_ecosystem_paths.tsv`, not a statement any source makes.** A curator with GOLD portal access can settle it in one query against `gold.ecosystem:4383`, `:4731`, `:4732`.

### What is inside the concept

The living bacterial cell as an occupied space, in its three documented compartments:

- **Cytoplasm of the host bacterium.** *Ca.* Moranella endobia (γ-proteobacterium) lives in the cytoplasm of *Ca.* Tremblaya princeps (β-proteobacterium), which in turn lives in mealybug bacteriocytes ([von Dohlen et al. 2001, *Nature* 412:433–436](https://doi.org/10.1038/35086563); [McCutcheon & von Dohlen 2011, *Curr Biol* 21:1366–1372](https://doi.org/10.1016/j.cub.2011.06.051), PMID 21835622).
- **Periplasm of the host bacterium.** *Bdellovibrio bacteriovorus* invades the periplasm of Gram-negative prey and converts the prey cell into a bdelloplast, in which it grows filamentously before lysing it ([Sockett 2009, *Annu Rev Microbiol*](https://doi.org/10.1146/annurev.micro.091208.073346)).
- **Outer surface of the host bacterium.** *Nanosynbacter lyticus* TM7x on *Schaalia (Actinomyces) odontolytica* XH001 ([He et al. 2015, *PNAS* 112:244–249](https://doi.org/10.1073/pnas.1419038112)); *Ca.* Vampirococcus lugosii on purple sulfur bacteria ([Moreira et al. 2021, *Nat Commun*](https://doi.org/10.1038/s41467-021-22762-4), PMID 33911080).

Strictly, the GOLD path says *endo*symbionts, so the epibiotic cases are arguably a neighbouring concept. The proposed sentence includes "outer cell surface" because HabitatMech's own `<X>-associated environment` pattern (ENVO's *plant-/animal-/fungi-associated environment*) covers surface and interior alike. **Drop "and outer cell surface" if you want the definition to track the GOLD path exactly** — that is a curator's call, and it is the only substantive open choice in the sentence.

### Neighbouring concepts explicitly outside it

- The **animal/insect** host that contains the bacterial host — `ENVO:01001002` *animal-associated environment*, and the insect bacteriocyte (`BTO:0006243`). In every known nested case this habitat is physically nested inside one of those; it is not identical to it.
- **Fungal cells as hosts of endobacteria** — the sibling path `Host-associated > Endosymbionts > Fungi` (e.g. *Mycetohabitans rhizoxinica* in *Rhizopus microsporus*; [Giger et al. 2024, *Nature*](https://doi.org/10.1038/s41586-024-08010-x)).
- **Protist cells as hosts** — `Host-associated > Microbial`, `> Protists`, `> Amoebozoa`, `> Ciliophora`; the large majority of "bacteria inside a cell" literature is this, not bacteria inside bacteria ([Husnik et al. 2021, *Curr Biol*](https://www.cell.com/current-biology/fulltext/S0960-9822(21)00747-8)).
- **Multi-cell microbial assemblages** — biofilm (`ENVO:00002034`), microbial mat (`ENVO:01000008`), and the biofilm-determined environments `ENVO:01001032/01001034/01001035/01001051/01001056`. These are determined by a *community on a surface*, not by an individual bacterial cell acting as host.

---

## 2. Genus — the broader kind

**`ENVO:01001000` *environmental system determined by an organism*** — "An environmental system which is determined by a living organism"; exact synonym *host-associated environment*; in subsets `envoEmpo`, `envoOmics`; active. Verified against the EBI OLS4 API (`https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO:01001000`) and present in this repo's vendored slice (`data/raw/ontology_terms.tsv`). This is the genus, and it is already the parent of the record's own parent (`habitatmech:GOLD.895a2372e5` → `ENVO:01001000`).

**No ENVO term expresses "bacterium-determined environment."** An OLS4 search of ENVO for `associated environment` (60 rows) returns exactly four organism-kind children: `ENVO:01001001` plant-associated, `ENVO:01001002` animal-associated, `ENVO:01001041` fungi-associated, `ENVO:01001179` cnidarian-associated. There is no bacterium-, prokaryote-, or microbe-associated environment. The vendored slice agrees.

### Near-misses and why each fails

| Term | Why it is not a match |
|---|---|
| `ENVO:01001000` environmental system determined by an organism | The genus, correctly — but **broader**: it covers every host kind, so grounding here would lose the "the host is a bacterium" content. |
| `ENVO:01001002` animal-associated environment | The *outer* host in the mealybug case, not this one. Asserts a metazoan determiner that the concept does not claim. |
| `ENVO:01001041` fungi-associated environment | Sibling, and the correct target for `Endosymbionts > Fungi` under reading (A). Wrong kingdom here. |
| `NCBITaxon:2` Bacteria | A taxon — a class of organisms, not a place. Correct exactly as the record already has it: `relation: xref`, per this repo's #99/#114 rules. Grounding here would publish the host-taxon over-claim the curation note exists to prevent. |
| `BTO:0006243` bacteriocyte | The **insect** cell that houses endosymbionts. Different organism, different level of nesting; also anatomy of the animal host. |
| `ENVO:00002034` biofilm, `ENVO:01000156` biofilm material | A multi-species aggregate, not a single cell serving as host. Under-specifies and mis-specifies. |
| `ENVO:01001032/34/35` environment determined by a biofilm on a plant/animal/fungal surface | Structurally the closest ENVO pattern (an environment determined by *microbes*), but the determiner is a biofilm on a **eukaryote's** surface — the eukaryote, not a bacterial cell, supplies the substrate. |
| `ENVO:00005757` bacteria enriched soil | A soil, mentioning bacteria. Unrelated. |
| GO cellular-component terms (`GO:0005737` cytoplasm, `GO:0042597` periplasmic space, `GO:0009279` cell outer membrane) | Cell components, not environmental systems; not in the vendored slice. Usable as sub-compartment xrefs on a future child term, not as the identity of this habitat. *(This suggestion is my inference, not a source claim.)* |

**Recommendation:** keep `UNGROUNDED` and raise an ENVO term request for **`bacterium-associated environment`** (alt.: *prokaryote-associated environment*) as a child of `ENVO:01001000`, mirroring `fungi-associated environment` exactly. ENVO has an open discussion of precisely this axis — host-associated biome terms and the reasoning that "if the material is host-derived, then for the microbial community the host organism is the biome" ([ENVO issue #1029](https://github.com/EnvironmentOntology/envo/issues/1029)).

---

## 3. Differentia — what distinguishes it from its siblings

The determining organism is a **bacterium**, and that single fact produces observable consequences that separate this habitat from plant-, animal-, fungus- and protist-determined ones:

1. **Scale.** The habitat is one prokaryotic cell, so its occupants are ultrasmall or extremely genome-reduced. *Tremblaya princeps* holds a 139 kb genome — the smallest reported for a bacterium — while its resident *Moranella endobia* is ~538 kb ([McCutcheon & von Dohlen 2011](https://doi.org/10.1016/j.cub.2011.06.051)). TM7x cells are 200–300 nm ([He et al. 2015](https://doi.org/10.1073/pnas.1419038112)). Contrast: a eukaryotic host cell routinely holds thousands of full-sized bacteria.
2. **Membrane architecture, directly observed.** In *Planococcus citri* bacteriomes, the β-proteobacterial spheres are bounded by a three-membrane bilayer and the γ-proteobacteria within them by a two-membrane bilayer — a signature of entry without phagocytosis, which prokaryotes cannot perform ([López-Madrigal et al. 2013, *BMC Microbiol* 13:74](https://doi.org/10.1186/1471-2180-13-74)).
3. **Measurable remodelling of the host cell wall.** In the *Bdellovibrio* bdelloplast, prey peptidoglycan is N-deacetylated to lysozyme resistance and acylated with long-chain fatty acids (~60 % palmitic, ~20 % oleic), and Braun lipoprotein is largely removed ([Thomashow & Rittenberg 1978, *J Bacteriol* 135(3):1008](https://pubmed.ncbi.nlm.nih.gov/357410/), PMID 357410; companion paper PMID 357411). This is the physicochemistry of the habitat, not merely of the occupant.
4. **Obligate metabolic dependency in both directions.** Tremblaya and Moranella run interdependent, non-duplicated segments of single amino-acid biosynthesis pathways — a "metabolic patchwork" spanning host insect and both bacteria ([McCutcheon & von Dohlen 2011](https://doi.org/10.1016/j.cub.2011.06.051); dispatch: [Keeling 2011, *Curr Biol*](https://doi.org/10.1016/j.cub.2011.06.061)). Acquiring the inner symbiont appears to have *caused* the outer one's extreme genome degeneracy.
5. **Narrow occupant range.** TM7x stably colonises only a specific *Actinomyces/Schaalia* clade — 13 of 27 tested strains, split into permissive and non-permissive ([Murugkar et al. 2020, *ISME J*](https://doi.org/10.1038/s41396-020-00736-6), PMID 32839546) — and TM7x is a specialist parasite rather than a broad predator ([Bor et al. 2018, *PNAS*](https://doi.org/10.1073/pnas.1810625115)).
6. **Turnover of the occupant.** The intra-*Tremblaya* γ-proteobacterium has been replaced repeatedly over evolutionary time by independent *Sodalis*-clade lineages ([Husnik & McCutcheon 2016, *PNAS*](https://doi.org/10.1073/pnas.1603910113)). The habitat persists; the resident does not.
7. **Nesting.** In every documented endosymbiotic case the bacterial host is itself inside a eukaryotic host, so this environment is normally a proper sub-part of an animal-associated environment. *(Statement of the current evidence base; sources report only Pseudococcinae mealybugs for the nested endosymbiotic form.)*

---

## 4. Sources

**Vocabularies and standards**
- ENVO `ENVO:01001000` — http://purl.obolibrary.org/obo/ENVO_01001000 (via OLS4 API, retrieved 2026-08-18).
- Buttigieg PL et al. "The environment ontology: contextualising biological and biomedical entities." *J Biomed Semantics* 2013;4:43. https://doi.org/10.1186/2041-1480-4-43
- Buttigieg PL et al. "The environment ontology in 2016…" *J Biomed Semantics* 2016;7:57. https://pmc.ncbi.nlm.nih.gov/articles/PMC5035502/
- ENVO issue #1029, host-associated biome terms — https://github.com/EnvironmentOntology/envo/issues/1029
- GSC MIxS host-associated extension — https://genomicsstandardsconsortium.github.io/mixs/0016002/
- **MIxS-SA**: "a MIxS extension defining the minimum information standard for sequence data from symbiont-associated micro-organisms." *ISME Communications* 2022. https://doi.org/10.1038/s43705-022-00092-w — directly relevant: it covers organisms that "establish a physical interaction with at least one other organism," explicitly names *"hyperparasite species X (parasite of the parasite)"*, treats the microbiota of symbionts nested within hosts as central, and adds "host of the symbiont" descriptors. **This is the standards-level warrant that a symbiont can itself be the host slot.**
- Yilmaz P et al. "Minimum information about a marker gene sequence (MIMARKS)…" *Nat Biotechnol* 2011;29:415–420. https://doi.org/10.1038/nbt.1823
- Mukherjee S et al. "Twenty-five years of GOLD: v.9." *Nucleic Acids Res* 2023;51:D957–D963. https://doi.org/10.1093/nar/gkac974 (PMID 36318257); GOLD v.10, *NAR* 2025;53:D989. https://academic.oup.com/nar/article/53/D1/D989/7875979
- GOLD ecosystem classification — https://gold.jgi.doe.gov/ecosystem_classification and https://gold.jgi.doe.gov/ecosystemtree *(both HTTP 403 to automated fetch on 2026-08-18; not read directly)*

**Primary literature — bacteria as hosts of bacteria**
- von Dohlen CD, Kohler S, Alsop ST, McManus WR. "Mealybug β-proteobacterial endosymbionts contain γ-proteobacterial symbionts." *Nature* 2001;412:433–436. https://doi.org/10.1038/35086563
- McCutcheon JP, von Dohlen CD. "An interdependent metabolic patchwork in the nested symbiosis of mealybugs." *Curr Biol* 2011;21(16):1366–1372. https://doi.org/10.1016/j.cub.2011.06.051 (PMID 21835622)
- Keeling PJ. "Endosymbiosis: bacteria sharing the load." *Curr Biol* 2011;21(16):R623–R624. https://doi.org/10.1016/j.cub.2011.06.061
- López-Madrigal S et al. "Mealybugs nested endosymbiosis: going into the 'matryoshka' system in *Planococcus citri* in depth." *BMC Microbiol* 2013;13:74. https://doi.org/10.1186/1471-2180-13-74
- Husnik F, McCutcheon JP. "Repeated replacement of an intrabacterial symbiont in the tripartite nested mealybug symbiosis." *PNAS* 2016. https://doi.org/10.1073/pnas.1603910113
- Husnik F et al. "Horizontal gene transfer from diverse bacteria to an insect genome enables a tripartite nested mealybug symbiosis." *Cell* 2013. https://scholarship.miami.edu/esploro/outputs/journalArticle/Horizontal-Gene-Transfer-from-Diverse-Bacteria/991031560853602976 *(DOI not verified in this session)*
- Husnik F, Keeling PJ. "The fate of obligate endosymbionts: reduction, integration, or extinction." *Curr Opin Genet Dev* 2019. PMID 31470232 — https://pubmed.ncbi.nlm.nih.gov/31470232/
- Husnik F, Tashyreva D, Boscaro V, George EE, Lukeš J, Keeling PJ. "Bacterial and archaeal symbioses with protists." *Curr Biol* 2021. https://www.cell.com/current-biology/fulltext/S0960-9822(21)00747-8

**Primary literature — periplasmic and epibiotic occupation of bacterial cells**
- Thomashow MF, Rittenberg SC. "Intraperiplasmic growth of *Bdellovibrio bacteriovorus* 109J: N-deacetylation of *Escherichia coli* peptidoglycan amino sugars." *J Bacteriol* 1978;135(3):1008. PMID 357410 — https://pmc.ncbi.nlm.nih.gov/articles/PMC222477/ (companion: PMID 357411, long-chain fatty-acid attachment)
- Sockett RE. "Predatory lifestyle of *Bdellovibrio bacteriovorus*." *Annu Rev Microbiol* 2009. https://doi.org/10.1146/annurev.micro.091208.073346
- He X, McLean JS, Edlund A et al. "Cultivation of a human-associated TM7 phylotype reveals a reduced genome and epibiotic parasitic lifestyle." *PNAS* 2015;112:244–249. https://doi.org/10.1073/pnas.1419038112
- Bor B et al. "Rapid evolution of decreased host susceptibility drives a stable relationship between ultrasmall parasite TM7x and its bacterial host." *PNAS* 2018. https://doi.org/10.1073/pnas.1810625115
- Murugkar P et al. "The saccharibacterium TM7x elicits differential responses across its host range." *ISME J* 2020. https://doi.org/10.1038/s41396-020-00736-6 (PMID 32839546)
- Moreira D et al. "Reductive evolution and unique predatory mode in the CPR bacterium *Vampirococcus lugosii*." *Nat Commun* 2021. https://doi.org/10.1038/s41467-021-22762-4 (PMID 33911080)

**Contrast case (the sibling path)**
- Giger GH et al. "Inducing novel endosymbioses by implanting bacteria in fungi." *Nature* 2024. https://doi.org/10.1038/s41586-024-08010-x

### Explicitly flagged as inference, not source claims
1. That GOLD's `Endosymbionts > Bacteria` denotes a bacterium-determined environment (readings A/B) rather than a sample taxon (reading C). Inferred from the sibling-path structure in `data/raw/gold_ecosystem_paths.tsv`; GOLD's own documentation was unreachable.
2. That the duplication with `Host-associated > Fungi` favours reading (B). My argument.
3. That the concept warrants an ENVO term request. Follows this repo's policy plus ENVO's existing four-way pattern; no source says ENVO should mint it.
4. That GO cellular-component terms are candidate sub-compartment xrefs. My suggestion.
5. Claim 7 in §3 (universal nesting inside a eukaryote) is a summary of the *current* evidence base, not a demonstrated necessity.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**
- *bacterium-associated environment* / *prokaryote-associated environment* (the proposed ENVO-pattern label)
- *intrabacterial* environment / niche — used in the primary literature ("intrabacterial symbiont", Husnik & McCutcheon 2016)
- *nested endosymbiosis*, *matryoshka symbiosis*, *"bug in a bug"*, *"bugs within bugs"* — informal but standard for the mealybug system
- *intraperiplasmic* growth environment; *bdelloplast* (the specific, remodelled form of it)
- *basibiont* — the bacterial host of an epibiont (used for *S. odontolytica* XH001 relative to TM7x)
- GOLD path string: `Host-associated > Endosymbionts > Bacteria`

**Commonly but wrongly treated as the same thing**
- **`NCBITaxon:2` Bacteria, the taxon.** A class of organisms, not a place. Keep as `relation: xref` (#99); do not ground and do not parent.
- **"Bacterial endosymbiont" in its ordinary sense** — *Wolbachia*, *Buchnera*, *Rickettsia*, *Cardinium*, *Spiroplasma* in animals. Here the bacterium is the *occupant* and the host is a eukaryote; that is `ENVO:01001002` territory. This is the single most likely conflation, and it is exactly reading (C).
- **Bacteriocyte / bacteriome** (`BTO:0006243`) — insect cells and tissue that house endosymbionts. Animal anatomy.
- **Endohyphal / endofungal bacteria** — *Mycetohabitans*, *Ca.* Glomeribacter. That is the sibling path `Endosymbionts > Fungi`.
- **Biofilm, microbial mat, microbial consortium** — determined by a community, not by one host cell.
- **Bacteriophage host cell.** A phage is a virus, not an endosymbiont; if GOLD applied this path to a phage genome the record would need re-scoping, not this definition.
- **Bacterial culture / axenic culture** (`BTO:0001091`) — a laboratory setting.
- **`ENVO:00005757` bacteria enriched soil** — a soil.

---

## 6. Should it be a term at all?

**Yes, under readings (A) and (B) — and both the corpus's own rules and the standards literature support it.**

The concept names a place: a bacterial cell whose cytoplasm, periplasm or surface is where another organism lives. Bdellovibrio's periplasmic niche, TM7x's basibiont, and Moranella's residence inside Tremblaya are habitats in exactly the sense the repo's rule states — *an organism acting as a host IS a habitat*. MIxS-SA makes this explicit at standards level: it covers hyperparasites and the microbiota of symbionts nested within hosts, and adds a "host of the symbiont" field (https://doi.org/10.1038/s43705-022-00092-w). ENVO already has the pattern (`plant-/animal-/fungi-/cnidarian-associated environment`) and simply lacks the bacterial member. So: keep `UNGROUNDED`, keep `NCBITaxon:2` as `xref`, and raise the ENVO term request.

**The one thing that would make it not a term is reading (C).** If GOLD's *Endosymbionts > Bacteria* is a taxonomic tag on the sequenced organism — "this genome is a bacterial endosymbiont of something" — then the path is a sampling/annotation artefact and the actual habitat is the unnamed eukaryotic host. In that case the correct disposition is not `NOT_APPLICABLE` (the concept would still not be a disease, quality, process or procedure) but a `REVIEW` noting that the path does not identify an environment. Given a single organism behind the path, this is a live possibility, and it is cheap to settle: look up `gold.ecosystem:4383` / `:4731` / `:4732` in the GOLD portal and read what organism was classified there. **Recommend doing that before filing the ENVO request** — the request text differs materially between "a bacterium can be a host" and "GOLD tagged one endosymbiont genome by kingdom."

Two smaller notes for the curator:
- Assertion volume is 1 (`ORGANISM`), which is thin. The definition above does not rest on that single record — it rests on the published bacterium-as-host systems — but the term request should say so rather than lean on GOLD's count.
- Fixing the parent (`habitatmech:GOLD.895a2372e5`, "Endosymbionts", still `SEEDED`) is the higher-yield move: it is the intermediate class that lets this record's definition stay one clause long, and it is shared with the `Endosymbionts > Fungi` sibling.

---

**Sources:** [ENVO:01001000 (OLS4)](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO:01001000) · [ENVO 2013](https://doi.org/10.1186/2041-1480-4-43) · [ENVO 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC5035502/) · [ENVO issue #1029](https://github.com/EnvironmentOntology/envo/issues/1029) · [MIxS host-associated](https://genomicsstandardsconsortium.github.io/mixs/0016002/) · [MIxS-SA](https://doi.org/10.1038/s43705-022-00092-w) · [MIMARKS/MIxS](https://doi.org/10.1038/nbt.1823) · [GOLD v.9](https://doi.org/10.1093/nar/gkac974) · [GOLD v.10](https://academic.oup.com/nar/article/53/D1/D989/7875979) · [GOLD ecosystem classification](https://gold.jgi.doe.gov/ecosystem_classification) · [von Dohlen et al. 2001](https://doi.org/10.1038/35086563) · [McCutcheon & von Dohlen 2011](https://doi.org/10.1016/j.cub.2011.06.051) · [Keeling 2011](https://doi.org/10.1016/j.cub.2011.06.061) · [López-Madrigal et al. 2013](https://doi.org/10.1186/1471-2180-13-74) · [Husnik & McCutcheon 2016](https://doi.org/10.1073/pnas.1603910113) · [Husnik et al. 2013](https://scholarship.miami.edu/esploro/outputs/journalArticle/Horizontal-Gene-Transfer-from-Diverse-Bacteria/991031560853602976) · [Husnik & Keeling 2019](https://pubmed.ncbi.nlm.nih.gov/31470232/) · [Husnik et al. 2021](https://www.cell.com/current-biology/fulltext/S0960-9822(21)00747-8) · [Thomashow & Rittenberg 1978](https://pmc.ncbi.nlm.nih.gov/articles/PMC222477/) · [Sockett 2009](https://doi.org/10.1146/annurev.micro.091208.073346) · [He et al. 2015](https://doi.org/10.1073/pnas.1419038112) · [Bor et al. 2018](https://doi.org/10.1073/pnas.1810625115) · [Murugkar et al. 2020](https://doi.org/10.1038/s41396-020-00736-6) · [Moreira et al. 2021](https://doi.org/10.1038/s41467-021-22762-4) · [Giger et al. 2024](https://doi.org/10.1038/s41586-024-08010-x)

## Citations

1. https://doi.org/10.1093/nar/gkac974
2. https://academic.oup.com/nar/article/53/D1/D989/7875979
3. https://doi.org/10.1038/35086563
4. https://doi.org/10.1016/j.cub.2011.06.051
5. https://doi.org/10.1146/annurev.micro.091208.073346
6. https://doi.org/10.1073/pnas.1419038112
7. https://doi.org/10.1038/s41467-021-22762-4
8. https://doi.org/10.1038/s41586-024-08010-x
9. https://www.cell.com/current-biology/fulltext/S0960-9822(21
10. https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO:01001000`
11. https://github.com/EnvironmentOntology/envo/issues/1029
12. https://doi.org/10.1186/1471-2180-13-74
13. https://pubmed.ncbi.nlm.nih.gov/357410/
14. https://doi.org/10.1016/j.cub.2011.06.061
15. https://doi.org/10.1038/s41396-020-00736-6
16. https://doi.org/10.1073/pnas.1810625115
17. https://doi.org/10.1073/pnas.1603910113
18. http://purl.obolibrary.org/obo/ENVO_01001000
19. https://doi.org/10.1186/2041-1480-4-43
20. https://pmc.ncbi.nlm.nih.gov/articles/PMC5035502/
21. https://genomicsstandardsconsortium.github.io/mixs/0016002/
22. https://doi.org/10.1038/s43705-022-00092-w
23. https://doi.org/10.1038/nbt.1823
24. https://gold.jgi.doe.gov/ecosystem_classification
25. https://gold.jgi.doe.gov/ecosystemtree
26. https://scholarship.miami.edu/esploro/outputs/journalArticle/Horizontal-Gene-Transfer-from-Diverse-Bacteria/991031560853602976
27. https://pubmed.ncbi.nlm.nih.gov/31470232/
28. https://pmc.ncbi.nlm.nih.gov/articles/PMC222477/
29. https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO:01001000