---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T16:44:53.982590'
end_time: '2026-08-17T16:53:30.681892'
duration_seconds: 516.7
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Microbial
  habitat_identifier: habitatmech:GOLD.184623c963
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Microbial'
  assertions: '465'
  parent_terms: ENVO:01001000
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. GOLD''s
    Host-associated > Microbial: a microorganism as host. Same gap as the Bacteria
    child; ENVO has no microbial-host environment term. (source concept habitatmech:GOLD.184623c963)'
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
  web_search_requests: 15
  num_turns: 32
  total_cost_usd: 3.3420639999999997
  session_id: e5b6ed1c-094c-4da9-941f-68f1dd8833ff
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 20
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Microbial
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.184623c963
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Microbial
- **Upstream assertion volume:** 465
- **Nearest broader term already on the record:** ENVO:01001000
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. GOLD's Host-associated > Microbial: a microorganism as host. Same gap as the Bacteria child; ENVO has no microbial-host environment term. (source concept habitatmech:GOLD.184623c963)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Microbial** as a microbial habitat, with citations.

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

# Definition research — GOLD *Host-associated > Microbial* (`habitatmech:GOLD.184623c963`)

> **Proposed definition:** An environmental system determined by an organism which is determined by a single-celled microorganism, such that the space available to the microbes it hosts is the surface, cytoplasm, or nuclear compartment of one cell.

Suggested label: **microorganism-associated environment** (parallel to ENVO's *plant-associated environment* / *animal-associated environment* / *fungi-associated environment*). The bare source label "Microbial" is too ambiguous to publish as a term label — see §5.

---

## 1. What the concept denotes

**The place is another microorganism's cell.** In GOLD's five-level scheme (Ecosystem → Ecosystem Category → Ecosystem Type → Ecosystem Subtype → Specific Ecosystem), level 1 is where the sample came from and level 2 for `Host-associated` is *the host*: "an Organism isolated from human sputum will have Ecosystem: Host-associated, Ecosystem Category: Human, Ecosystem Type: Respiratory system…" ([Mukherjee et al. 2019, *NAR* 47:D649–D659, doi:10.1093/nar/gky977](https://doi.org/10.1093/nar/gky977); [GOLD ecosystem classification page](https://gold.jgi.doe.gov/ecosystem_classification) — the JGI page returns HTTP 403 to automated fetch, so it is cited from the paper and from JGI's own summary text, not read directly). So `Host-associated > Microbial` denotes **a microorganism occupying the position that "Human", "Plants" or "Mammals" occupies in sibling paths: the host organism is itself a microbe.**

The corpus's own raw inventory settles the reading (`data/raw/gold_ecosystem_paths.tsv`):

| GOLD path | depth | organism assertions |
|---|---|---|
| `Host-associated > Microbial` | 2 (category) | 465 |
| `Host-associated > Microbial > Bacteria` | 3 (type) | 3,017 |
| `Host-associated > Microbial > Dinoflagellates` | 3 | 0 |
| `Host-associated > Microbial > Dinoflagellates > Endosymbionts` | 4 | 0 |

The children are **host taxa** (Bacteria, Dinoflagellates), not sample materials — which is what a category-level host slot predicts, and is the single strongest piece of evidence for the reading. The 465 assertions on the bare path are submissions that recorded only "the host is a microbe" without naming which.

**Inside the concept:** a bacterial, archaeal, or unicellular-eukaryotic cell considered as the living space of other microorganisms — its outer surface (ecto-/epibionts), its cytoplasm, its symbiosome-like host-derived membranes, and its nuclear apparatus. Husnik et al. list exactly this range of positions for prokaryotic symbionts of protists: most inhabit the cytoplasm, "some are surrounded by host-derived membranes, some associate with mitochondria…, some colonize the outer surface in orderly arrangements, and some have invaded the host nuclear apparatus" ([Husnik et al. 2021, *Curr Biol* 31:R862–R877, doi:10.1016/j.cub.2021.05.049](https://doi.org/10.1016/j.cub.2021.05.049); [PMID 34256922](https://pubmed.ncbi.nlm.nih.gov/34256922/)).

**Outside the concept (neighbours), with evidence that GOLD keeps them separate:**

- **Microbial mats, biofilms, microbialites** — a multicellular *assemblage* is the habitat, not a host cell. GOLD files all 20+ of these under `Environmental > Aquatic > … > Microbial mats` / `Microbialites`, never under `Host-associated`. ENVO already covers them: *biofilm* `ENVO:00002034`, *microbial mat* `ENVO:01000008`, *organic object formed through microbial activity* `ENVO:01000007`.
- **Fungal hosts** — GOLD has a separate `Host-associated > Fungi` category (635 assertions), and ENVO has *fungi-associated environment* `ENVO:01001041`.
- **Other microbial-eukaryote host categories GOLD lists as siblings, not children:** `Algae` (394), `Protists` (40), `Protozoa` (32), `Amoebozoa` (13), `Ciliophora` (0). GOLD's own "Microbial" is therefore in practice *prokaryotic hosts + dinoflagellates*, not "every microbial host".
- **`Host-associated > Endosymbionts` (3 assertions)** — names the *symbiont's role*, not the host; a different axis.

**Ambiguity, stated rather than resolved silently.** Two further readings exist and both are weaker:

1. *"the sample is a microbial community/consortium"* — ruled out by GOLD's placement of mats and consortia under `Environmental` and `Engineered > Modeled > Simulated communities (microbial mixture)`.
2. *"host is a microbe" including viruses of bacteria* — the 3,017-assertion `Bacteria` child is large for microbe-in-microbe symbioses, and phage/virus genome entries carrying a bacterial host is a plausible contributor. **I could not verify this**: gold.jgi.doe.gov blocks automated fetch, and the raw table records only node ids and counts. Treat "what those 3,017 organisms actually are" as an open question for the curator; it does not change the genus or differentia, but it does affect whether the definition should say "microorganisms" or "microorganisms and viruses".

**The scope decision this forces:** if HabitatMech defines the term as *any* microorganism as host, the term is **broader than GOLD's usage** and properly subsumes GOLD's sibling `Protists`, `Protozoa`, `Amoebozoa`, `Ciliophora`, and unicellular `Algae` categories. That is defensible in an ontology (they become children) but should be written down, because the source path alone does not license it.

---

## 2. Genus — the broader kind

**Genus: `ENVO:01001000` *environmental system determined by an organism*** — "An environmental system which is determined by a living organism" (verified via [OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001000)). This is already the record's `parent_habitats` value and it is the correct genus: a microorganism is a living organism, and the pattern ENVO uses for hosts is exactly this branch.

**Its direct children (verified, OLS4):**

| CURIE | Label | Definition |
|---|---|---|
| ENVO:01001001 | plant-associated environment | An environmental system determined by a green plant. |
| ENVO:01001002 | animal-associated environment | An environmental system determined by an animal. |
| ENVO:01001041 | fungi-associated environment | An environmental system determined by a fungal structure. |
| ENVO:2100000 | anatomical entity environment | An environment which is determined by an anatomical entity. |

**There is no microbe/microorganism/bacterium/archaeon/protist/alga sibling.** Two independent OLS4 queries confirm this: a search for ENVO labels containing "associated environment" returns only plant, animal, fungi, cnidarian, aquatic-invertebrate, and the animal-/plant-/fungal-*part* variants; a search over ENVO definitions containing "determined by a" returns 51 terms, none of them determined by an alga, protist, bacterium, archaeon, or microorganism. The curator's original note ("ENVO has no microbial-host environment term") is correct as of this check.

**Near-misses and why each fails:**

| Candidate | Why it is not a match |
|---|---|
| `ENVO:01001041` *fungi-associated environment* | Narrower, and asserts fungal identity. It *does* already cover unicellular fungi (yeasts) as hosts — the one genuine overlap with the proposed term (see §6). |
| `ENVO:01001002` *animal-associated environment* | Narrower; asserts animal identity. Some hosts of microbes are microscopic animals, but GOLD files those under its animal categories. |
| `ENVO:00002034` *biofilm*; `ENVO:01000008` *microbial mat*; `ENVO:01000007` *organic object formed through microbial activity* | These are environments **made by** microbial assemblages, not environments **that are** an individual microbial cell. Asserting a matrix-secreting multicellular aggregate is an over-claim for a single-cell epibiont habitat. |
| `ENVO:01001032/01001034/01001035` *environment determined by a biofilm on a plant / animal / fungal surface* | Notably, ENVO stops at plant/animal/fungal surfaces here too — there is no "biofilm on a microbial surface". Same gap, different pattern. |
| `ENVO:2100000` *anatomical entity environment* | A single-celled organism has no anatomical entity in the UBERON sense; parenting here would misapply the anatomy axis. |
| `PCO:microbial community` (see [ENVO issue #807](https://github.com/EnvironmentOntology/envo/issues/807)) | A community, not a place; the relevant class for *microbiome*, a different concept. |
| NCBITaxon / taxon terms | A taxon is a class of organisms, not a place — the corpus rule (`relation: xref`, not `parent`, and not `NOT_APPLICABLE`). |

Related open ENVO tracker context, useful for a term request: [#1029 "EnvO terms for host-associated samples"](https://github.com/EnvironmentOntology/envo/issues/1029) and [#807 "envo microbiome"](https://github.com/EnvironmentOntology/envo/issues/807). Neither requests a microbial-host environment, so this would be a new request rather than a duplicate.

---

## 3. Differentia — what distinguishes it from its siblings

The determining organism is **a single cell**, and that is the observable that does the work. Consequences that are measurable and that no sibling under `ENVO:01001000` shares:

1. **Spatial scale of micrometres.** The whole habitat is one cell. *Nanoarchaeum equitans* cells are ~400 nm and grow attached to the surface of a single *Ignicoccus* cell ([Huber et al. 2002, *Nature* 417:63–67, doi:10.1038/417063a](https://doi.org/10.1038/417063a)). The oral epibiont TM7x (*Nanosynbacter lyticus*) is a 200–300 nm cell living on the surface of its *Actinomyces odontolyticus* basibiont ([He et al. 2015, *PNAS* 112:244–249, doi:10.1073/pnas.1419038112](https://doi.org/10.1073/pnas.1419038112)).
2. **A size filter on who can live there.** Occupants are ultrasmall and typically genome-reduced obligates — a selection pressure a gut or a rhizosphere does not impose. TM7x encodes only ~705 CDS (He et al. 2015).
3. **Compartments that are organelles rather than organs.** Husnik et al. describe protist hosts carrying communities "whose richness and functional complexity are not very different from some model animal 'microbiomes'", spatially compartmentalised "with organelles playing the role of tissues" (doi:10.1016/j.cub.2021.05.049). Positions include cytoplasm, host-derived membranes, association with mitochondria, cell surface, and the nuclear apparatus.
4. **A membrane-bounded, host-provisioned chemistry.** "The host offers protection and nutrients, while the algal symbiont supplies sugars" ([Karnkowska, García-Cunchillos & Sałek 2026, *microLife* 7:uqag013, doi:10.1093/femsml/uqag013](https://doi.org/10.1093/femsml/uqag013)). Archaeal (methanogen) symbionts of protists are restricted to *anaerobic* hosts — the host cell's redox state, not the surrounding water's, sets the habitat (same source; Husnik et al. 2021).
5. **Recursion — a microbial habitat can nest inside another host's habitat.** A bacterium inside a bacterium inside an insect bacteriocyte: γ-proteobacterial symbionts live *within* the β-proteobacterial *Candidatus* Tremblaya princeps cells of mealybugs ([von Dohlen et al. 2001, *Nature* 412:433–436, doi:10.1038/35086563](https://doi.org/10.1038/35086563)). This is the case that shows the concept is not reducible to the outer host's anatomy.
6. **Predation/parasitism as a formation process, not just mutualism.** Free-living amoebae act as hosts and reservoirs for *Legionella*, *Mycobacterium avium*, *Parachlamydia* and others — some lytic for the amoebal host, others behaving as stable endosymbionts, with the encysted amoeba shielding internalised bacteria from chlorine and biocides ([Greub & Raoult 2004, *Clin Microbiol Rev* 17:413–433, doi:10.1128/CMR.17.2.413-433.2004](https://doi.org/10.1128/CMR.17.2.413-433.2004); [PMC387402](https://pmc.ncbi.nlm.nih.gov/articles/PMC387402/)).
7. **The dinoflagellate case, matching GOLD's own `Dinoflagellates` child.** Cultured *Symbiodinium* carry bacteria at nearly two orders of magnitude greater numerical abundance than the dinoflagellate cells themselves, with a three-OTU core (*Labrenzia*, *Marinobacter*, Chromatiaceae) across 18 types spanning 5 clades ([Lawson et al. 2018, *Environ Microbiol Rep*, doi:10.1111/1758-2229.12599](https://doi.org/10.1111/1758-2229.12599)).

*Inference, flagged:* items 1–7 are each sourced, but the claim that "single-cellness is the right differentia" — rather than, say, "prokaryote-ness" — is my synthesis. It is chosen because it is what actually separates the concept from all four existing siblings and because it accommodates GOLD's own mixed usage (bacteria + dinoflagellates).

---

## 4. Sources

**Standards, vocabularies, and the source scheme**
- Mukherjee S. et al. Genomes OnLine Database (GOLD) v.7: updates and new features. *Nucleic Acids Research* 47(D1):D649–D659, 2019. doi:[10.1093/nar/gky977](https://doi.org/10.1093/nar/gky977) — defines the five-level scheme and the host-as-Ecosystem-Category pattern. *Verified by fetching [PMC6323969](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323969/).*
- Ivanova N. et al. A call for standardized classification of metagenome projects. *Environmental Microbiology* 12(7):1803–1805, 2010. doi:[10.1111/j.1462-2920.2010.02270.x](https://doi.org/10.1111/j.1462-2920.2010.02270.x) — origin of the scheme. *Citation from search results; not fetched.*
- JGI GOLD Ecosystem Classification: https://gold.jgi.doe.gov/ecosystem_classification — **HTTP 403 to automated fetch; not read directly.**
- Yilmaz P. et al. Minimum information about a marker gene sequence (MIMARKS) and minimum information about any (x) sequence (MIxS) specifications. *Nature Biotechnology* 29:415–420, 2011. doi:[10.1038/nbt.1823](https://doi.org/10.1038/nbt.1823) — the host-associated environmental package.
- MIxS-SA: a MIxS extension defining the minimum information standard for sequence data from symbiont-associated **micro-organisms**. *ISME Communications*, 2022. doi:[10.1038/s43705-022-00092-w](https://doi.org/10.1038/s43705-022-00092-w) — Parasite Microbiome Project / GSC extension of the host-associated package covering symbionts of one or multiple hosts along the mutualism–parasitism continuum. Relevant precedent that the standards community treats microbe-in-host reporting as needing its own vocabulary.
- ENVO term records verified live via OLS4: `ENVO:01001000`, `01001001`, `01001002`, `01001041`, `2100000`, `00002034`, `01000008`, `01000007`, `01001032/34/35`.
- NCIT:C14329 *Microorganism*: "A microscopic organism. The term microorganism may refer to a prokaryote or eukaryote, and may be a unicellular or multicellular organism." (via OLS4) — the only exact-label "microorganism" class with a usable definition across OLS; NCBITaxon and ENVO have none. Useful as a definition source, but note its "may be multicellular" clause is looser than the differentia proposed here.

**Primary literature**
- Husnik F., Tashyreva D., Boscaro V., George E.E., Lukeš J., Keeling P.J. Bacterial and archaeal symbioses with protists. *Current Biology* 31(13):R862–R877, 2021. doi:[10.1016/j.cub.2021.05.049](https://doi.org/10.1016/j.cub.2021.05.049)
- Karnkowska A., García-Cunchillos Í., Sałek M. Living together: evolutionary and ecological dimensions of protist endosymbiosis. *microLife* 7:uqag013, 2026. doi:[10.1093/femsml/uqag013](https://doi.org/10.1093/femsml/uqag013)
- Huber H. et al. A new phylum of Archaea represented by a nanosized hyperthermophilic symbiont. *Nature* 417:63–67, 2002. doi:[10.1038/417063a](https://doi.org/10.1038/417063a)
- He X. et al. Cultivation of a human-associated TM7 phylotype reveals a reduced genome and epibiotic parasitic lifestyle. *PNAS* 112:244–249, 2015. doi:[10.1073/pnas.1419038112](https://doi.org/10.1073/pnas.1419038112)
- von Dohlen C.D., Kohler S., Alsop S.T., McManus W.R. Mealybug β-proteobacterial endosymbionts contain γ-proteobacterial symbionts. *Nature* 412:433–436, 2001. doi:[10.1038/35086563](https://doi.org/10.1038/35086563)
- Greub G., Raoult D. Microorganisms resistant to free-living amoebae. *Clinical Microbiology Reviews* 17(2):413–433, 2004. doi:[10.1128/CMR.17.2.413-433.2004](https://doi.org/10.1128/CMR.17.2.413-433.2004)
- Lawson C.A. et al. Defining the core microbiome of the symbiotic dinoflagellate, *Symbiodinium*. *Environmental Microbiology Reports*, 2018. doi:[10.1111/1758-2229.12599](https://doi.org/10.1111/1758-2229.12599)
- Cellular interactions and evolutionary origins of endosymbiotic relationships with ciliates. *The ISME Journal* 18(1):wrae117, 2024. https://academic.oup.com/ismej/article/18/1/wrae117/7698271 — ciliate hosts, incl. *Zoothamnium niveum* / "*Ca.* Thiobios zoothamnicoli" thiotrophic epibionts. *Citation from search results; abstract-level only.*

**Repository evidence (not external, but decisive for the reading)**
- `data/raw/gold_ecosystem_paths.tsv` — the four `Host-associated > Microbial*` rows and their assertion counts; the 27 `Host-associated` sibling categories; the 20+ `Environmental > … > Microbial mats` rows.
- `curation/decisions.tsv:229`, `curation/term_requests.tsv:14`, `data/habitats/host_associated/{microbial__50f690f2,bacteria}.yaml`.

**Provenance note on the two DOIs I could not open directly:** the Ivanova 2010 DOI and the MIxS-SA DOI come from search-result metadata rather than a fetched landing page. Everything else above was either fetched or returned with matching title/venue from the publisher's own page in results.

---

## 5. Synonyms and what NOT to conflate

**Names in real use for this concept:**
- microbial host (the host side); *basibiont* (the larger partner in an epibiotic pair — He et al. 2015; McLean et al., *Genome Announc*, doi:[10.1128/genomeA.01685-15](https://doi.org/10.1128/genomeA.01685-15))
- host cell / host cytoplasm as habitat; symbiosome (Karnkowska et al. 2026)
- "microbial microbiome" / "the microbiome of a microbe" — informal but used for the protist case (Husnik et al. 2021)
- protist-associated environment; bacteria-associated environment (would be narrower children)
- GOLD's own string: `Host-associated > Microbial`

**Commonly but wrongly treated as the same thing:**
- **Microbial mat / biofilm / biocrust / microbialite** — habitats *built by* microbial assemblages. Distinct ENVO classes exist; conflating them would put a lithifying carbonate structure and a 400 nm archaeal cell in one class.
- **Microbiome / microbial community** — a community of organisms, not a place (`PCO`, ENVO issue #807).
- **The symbiont, or "endosymbiont" as a category** — GOLD's `Host-associated > Endosymbionts` and `… > Dinoflagellates > Endosymbionts` name the occupant's role. Occupant ≠ habitat.
- **Bacteria / Dinoflagellata as taxa** — `NCBITaxon` classes. Per the corpus rule, these go in `relation: xref`; they are not the habitat and they are not `NOT_APPLICABLE`.
- **Microbial fuel cell, microbial enhanced oil recovery** — the word "microbial" as a process modifier; GOLD files these under `Engineered`.
- **"Microbial" as a sample-type qualifier on a metagenome** — a description of the assay, not of a place.

---

## 6. Should it be a term at all — yes

This is a place: it is where a sample is taken from (an *Ignicoccus* cell, a *Symbiodinium* culture, a *Tremblaya* cytoplasm), it has a physical boundary, a characteristic chemistry, and a size-based filter on its inhabitants. It is not a process, quality, disease state, or sampling artefact. And it is **not** a taxon term dressed as a habitat: the taxon (`Bacteria`, `Dinoflagellata`) belongs in `relation: xref` while the concept keeps its minted identity — the disposition the corpus settled in #114/#112, and the same shape ENVO already publishes at plant-, animal- and fungi-associated environment.

The gap is real and independently confirmed: ENVO's organism-determined branch has exactly four children and none of them is a microorganism, despite microorganisms being, by count, the commonest hosts in the sources this repo harmonises (465 + 3,017 GOLD organism assertions on this branch alone).

**Three things the curator should decide explicitly, because the sources do not decide them:**

1. **Overlap with `ENVO:01001041` fungi-associated environment.** A yeast host is both a microorganism and a fungal structure. The four existing siblings partition by taxon; a fifth partitioning by cell count is not disjoint with them. Either (a) accept a non-disjoint sibling and add a comment routing fungal hosts to `ENVO:01001041`, or (b) write the differentia as "…a single-celled organism that is not a fungus". I recommend (a) with an explicit comment — (b) buries a routing rule inside a definition and will read as arbitrary in five years.
2. **Scope relative to GOLD.** As defined, the term is broader than GOLD's usage and would subsume GOLD's `Protists`, `Protozoa`, `Amoebozoa`, `Ciliophora` and unicellular `Algae` host categories. Say so in the record note rather than letting it be inferred.
3. **Viruses.** If a material share of the 3,017 `Host-associated > Microbial > Bacteria` assertions are phage genomes, the definition's "microbes it hosts" should be widened to "microorganisms and viruses" — or deliberately left narrow, with the phage case routed elsewhere. **This is the one factual question I could not resolve**; gold.jgi.doe.gov blocks automated access and the raw table carries only counts.

The draft already in `curation/term_requests.tsv:14` ("An environmental system determined by a microorganism", label *microbe-associated environment*, parent `ENVO:01001000`) is on the right genus and the right pattern. The change I would make is to add the single-cell differentia — without it, the definition is a bare taxon-scope restatement that gives a submitter no way to decide the yeast case, the microbial-mat case, or the microscopic-animal case.

**Sources:**
- [GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification) · [GOLD v.7, *NAR* 2019](https://doi.org/10.1093/nar/gky977) · [PMC6323969](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323969/)
- [Ivanova et al. 2010](https://doi.org/10.1111/j.1462-2920.2010.02270.x) · [Yilmaz et al. 2011 MIxS](https://doi.org/10.1038/nbt.1823) · [MIxS-SA 2022](https://doi.org/10.1038/s43705-022-00092-w)
- [Husnik et al. 2021](https://doi.org/10.1016/j.cub.2021.05.049) · [Karnkowska et al., *microLife*](https://doi.org/10.1093/femsml/uqag013) · [ISME J 2024, ciliate endosymbioses](https://academic.oup.com/ismej/article/18/1/wrae117/7698271)
- [Huber et al. 2002](https://doi.org/10.1038/417063a) · [He et al. 2015](https://doi.org/10.1073/pnas.1419038112) · [von Dohlen et al. 2001](https://doi.org/10.1038/35086563) · [Greub & Raoult 2004](https://doi.org/10.1128/CMR.17.2.413-433.2004) · [Lawson et al. 2018](https://doi.org/10.1111/1758-2229.12599)
- [ENVO issue #1029](https://github.com/EnvironmentOntology/envo/issues/1029) · [ENVO issue #807](https://github.com/EnvironmentOntology/envo/issues/807) · [OLS4 ENVO:01001000](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001000)

## Citations

1. https://doi.org/10.1093/nar/gky977
2. https://gold.jgi.doe.gov/ecosystem_classification
3. https://doi.org/10.1016/j.cub.2021.05.049
4. https://pubmed.ncbi.nlm.nih.gov/34256922/
5. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001000
6. https://github.com/EnvironmentOntology/envo/issues/807
7. https://github.com/EnvironmentOntology/envo/issues/1029
8. https://doi.org/10.1038/417063a
9. https://doi.org/10.1073/pnas.1419038112
10. https://doi.org/10.1093/femsml/uqag013
11. https://doi.org/10.1038/35086563
12. https://doi.org/10.1128/CMR.17.2.413-433.2004
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC387402/
14. https://doi.org/10.1111/1758-2229.12599
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC6323969/
16. https://doi.org/10.1111/j.1462-2920.2010.02270.x
17. https://doi.org/10.1038/nbt.1823
18. https://doi.org/10.1038/s43705-022-00092-w
19. https://academic.oup.com/ismej/article/18/1/wrae117/7698271
20. https://doi.org/10.1128/genomeA.01685-15