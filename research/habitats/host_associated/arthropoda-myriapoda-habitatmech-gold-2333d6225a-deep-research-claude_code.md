---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T16:36:50.124488'
end_time: '2026-08-17T16:46:14.907127'
duration_seconds: 564.78
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: 'Arthropoda: Myriapoda'
  habitat_identifier: habitatmech:GOLD.2333d6225a
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Arthropoda: Myriapoda'
  assertions: '569'
  parent_terms: ENVO:01001000, ENVO:01001002
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Nearest
    broader term ENVO:01001002 ''animal-associated environment'' attached as a parent.
    Myriapods as host. Parented to animal-associated environment; not grounded there
    because every host clade would merge onto one record. ENVO term request. (source
    concept habitatmech:GOLD.2333d6225a)'
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
  num_turns: 39
  total_cost_usd: 3.8930895000000003
  session_id: 34a73e67-23d7-412b-91db-54fd2a65ce7d
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 25
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Arthropoda: Myriapoda
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.2333d6225a
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Arthropoda: Myriapoda
- **Upstream assertion volume:** 569
- **Nearest broader term already on the record:** ENVO:01001000, ENVO:01001002
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term ENVO:01001002 'animal-associated environment' attached as a parent. Myriapods as host. Parented to animal-associated environment; not grounded there because every host clade would merge onto one record. ENVO term request. (source concept habitatmech:GOLD.2333d6225a)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Arthropoda: Myriapoda** as a microbial habitat, with citations.

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

# Definition research: `habitatmech:GOLD.2333d6225a` — "Arthropoda: Myriapoda"

> **Proposed definition:** An animal-associated environment which is determined by a myriapod (Myriapoda) or by a part of a myriapod.

Proposed label: **myriapod-associated environment**. Genus: `ENVO:01001002` *animal-associated environment*. Differentia: host clade = Myriapoda (`NCBITaxon:61985`). The sentence is deliberately isomorphic to ENVO's one existing clade-level sibling, `ENVO:01001179` *cnidarian-associated environment* — "An environmental system determined by a cnidarian or part of a cnidarian" — which is the strongest single argument for the request being accepted in this form, and the same form recommended for the sibling record `habitatmech:GOLD.dba2a83b95` ("Arthropoda: Insects").

---

## 1. What the concept denotes

**The thing sampled is a myriapod body, or a site, tissue or product within one.** In GOLD's five-level ecosystem classification, `Host-associated` is the Ecosystem, `Arthropoda: Myriapoda` is the Ecosystem Category, and every level below it (Ecosystem Type / Subtype / Specific Ecosystem) is a body system, body site or product of that host ([Mukherjee et al. 2023, *Nucleic Acids Research* 51:D957–D963, GOLD v.9](https://academic.oup.com/nar/article/51/D1/D957/6786204); PMID [36318257](https://pubmed.ncbi.nlm.nih.gov/36318257/)). The label names a host clade because in GOLD the host **is** the environmental category — the classification is of the sample's environment, not of the organism sequenced.

The repo's own copy of the GOLD path table settles the scope empirically. `data/raw/gold_ecosystem_paths.tsv` holds **21 paths** rooted at `Host-associated > Arthropoda: Myriapoda`, carrying **605 assertions** across the subtree, of which **569 sit on the bare two-level node itself** — isolates and samples recorded as "from a myriapod" with no body site given. Only 36 assertions are distributed below it:

| Path | Assertions |
|---|---|
| `Host-associated > Arthropoda: Myriapoda` (bare node) | 569 |
| `… > Digestive system > Gut` | 23 |
| `… > Digestive system > Hindgut` | 10 |
| `… > Digestive system > Hindgut > Fecal` | 2 |
| `… > Digestive system` | 1 |
| 16 further paths (Foregut, Midgut, Hindgut > P1/P3 segment, Integument > Cuticle [> Thoracic segments], Integumentary system > Cuticle [> Prothorax], Reproductive system [> Ovaries], Respiratory system [> Gills], Tissue) | 0 |

Two things follow. First, **94% of the volume is on the undifferentiated node**, so this record has to be able to hold "isolated from a myriapod, body site unspecified" — it cannot be quietly narrowed to the gut. Second, the populated children are almost entirely **digestive tract**, which is exactly where the myriapod microbiome literature is (§3), so the concept as *used* is dominated by gut and gut-product samples even though the concept as *defined* is broader.

**Inside the concept:** the lumen and wall of the digestive tract (foregut, midgut, hindgut, hindgut sub-segments), egested faecal material while still attributable to the host, the cuticle/integument surface, reproductive organs (the route by which vertically transmitted symbionts such as *Wolbachia* are carried), the tracheal system, and whole-body homogenates.

**Outside the concept (neighbouring concepts):**
- The **soil and leaf litter the animal lives in and eats** — `ENVO:00001998` *soil*, `ENVO:03501259` *litter*. This is a live boundary, not a formality: millipede gut communities overlap heavily with the ingested litter, and a 2024 inhibitor/¹³C-SIP study concluded that litter-*associated* microbes, rather than a resident fermenting gut community, carry much of the nutritional work ([Nweze et al. 2024, *Communications Biology* 7:1204, doi:10.1038/s42003-024-06821-2](https://www.nature.com/articles/s42003-024-06821-2)). A faecal pellet lying in the soil for a week is a soil/litter sample; a faecal pellet taken from the hindgut is this concept.
- The **sibling GOLD host categories**: `Arthropoda: Insects` (1,833 assertions), `Arthropoda: Crustaceans` (598), `Arthropoda: Chelicerates`, and the catch-all `Invertebrates` (621). Myriapoda is a coordinate subphylum-level category in that scheme, not a subset of any of them.
- The **myriapod as an organism**, i.e. the taxon `NCBITaxon:61985`. See §6.

**Ambiguity — one reading, with an internal heterogeneity caveat.** The label itself is unambiguous as to *what kind of thing* it names (a host clade), and the source path `Host-associated > Arthropoda: Myriapoda` fixes the reading. What is genuinely heterogeneous is the clade: Myriapoda comprises four extant classes — Diplopoda (millipedes, >12,000 described spp.), Chilopoda (centipedes, ~3,000–5,000 spp.), Pauropoda (~835 spp.) and Symphyla (~195 spp.) ([Wright, *eLS*, "Myriapoda (Including Centipedes and Millipedes)", doi:10.1002/9780470015902.a0001607.pub3](https://onlinelibrary.wiley.com/doi/10.1002/9780470015902.a0001607.pub3); [Bergeron et al. 2019, "Myriapoda of Canada", *ZooKeys*, PMC6355731](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6355731/)). These differ fundamentally in trophic biology — millipedes are saprophagous detritivores, centipedes are obligate predators with venomous forcipules — and therefore in gut chemistry and microbiome. **My inference, flagged as such:** that heterogeneity is an argument for keeping the differentia at the host clade and *not* writing any physicochemistry into the definition sentence, because any physicochemical claim true of a millipede hindgut is false for a centipede. It is not an argument against the term, which sits at the level GOLD asserts.

---

## 2. Genus — the broader kind

**Recommended genus: `ENVO:01001002` *animal-associated environment*** — "An environmental system determined by an animal." This is already on the record as a parent, and it is the correct genus: a myriapod is an animal, and the environment determined by one is a species of environment determined by an animal. Its own parent `ENVO:01001000` *environmental system determined by an organism* (also on the record) is one level too broad to serve as the genus.

Checked against ENVO (via the vendored slice in `data/raw/ontology_terms.tsv` and the EBI OLS4 ENVO index) — **no term names this concept.** Near-misses, and why each fails:

| Candidate | Label / definition | Why it is not a match |
|---|---|---|
| `ENVO:01001179` | cnidarian-associated environment — "An environmental system determined by a cnidarian or part of a cnidarian" | Wrong clade. Its value here is as a **template**: it proves ENVO already accepts clade-level organism-associated classes, so a myriapod sibling is a pattern-conforming request, not a novel modelling move. |
| `ENVO:01001176` | environment associated with an aquatic invertebrate | Myriapods are invertebrates but are almost entirely **terrestrial** — the group's tracheal respiration with largely non-closable spiracles is a terrestrialisation trait, and the ENVO definition explicitly requires "a habitat that is found in an aquatic environmental system." Grounding here would assert an aquatic setting the sources never claim. (Note that GOLD's `… > Respiratory system > Gills` child, at 0 assertions, is a template artefact — myriapods have tracheae and spiracles, not gills; see §5.) |
| `ENVO:01001055` | environment associated with an animal part or small animal | Genuinely close, and arguably *would* cover many myriapod samples. It fails as a grounding for two reasons: it is defined by **size and partonomy, not by clade**, so it says nothing about which host the sample came from and would merge Myriapoda with every other small animal; and it under-covers, since *Archispirostreptus gigas* and *Scolopendra* are not "small animals" on any ordinary reading. |
| `ENVO:01001002` | animal-associated environment | The genus, not the species. Grounding the record here is what the curator's note already rejected, and correctly: every host clade in GOLD would collapse onto one record. |
| `ENVO:01001001` / `ENVO:01001041` | plant-associated / fungi-associated environment | Wrong kingdom; listed only to show the sibling pattern ENVO uses at this level. |
| UBERON anatomy terms | e.g. `UBERON:0001046` *hindgut*, `UBERON:0001002` *cuticle* | These are the right targets for the **child** records (`… > Hindgut`, `… > Integument > Cuticle`), not for this one. Per the repo rule, a host's parts ground to the anatomy term; the whole host organism does not. |

ENVO general references: [Buttigieg et al. 2013, *J Biomed Semantics* 4:43, doi:10.1186/2041-1480-4-43](https://link.springer.com/article/10.1186/2041-1480-4-43); [Buttigieg et al. 2016, *J Biomed Semantics* 7:57, PMC5035502](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035502/). GOLD's conformance to GSC/MIxS minimum-information standards, which is why these host-category paths exist at all: [Yilmaz et al. 2011, *Nature Biotechnology* 29:415–420, doi:10.1038/nbt.1823](https://www.nature.com/articles/nbt.1823).

---

## 3. Differentia — what distinguishes it

**The formal differentia is the host clade: Myriapoda (`NCBITaxon:61985`).** That is how ENVO differentiates every sibling under `ENVO:01001002`, and it is the entire content of what GOLD asserts at this node. Everything below is **supporting evidence that the class carves a real, distinctive microbial habitat** — it is not additional differentiae to write into the sentence.

**(a) The gut is a structured, physicochemically distinctive habitat, not a passing tube.** Microsensor profiling of two tropical millipedes (*Epibolus pulchripes*, *Archispirostreptus gigas*) found the lumen **strictly anoxic throughout midgut and hindgut**, **strongly reducing (−114 to −243 mV)** along the entire tract, with a **sharp pH discontinuity — acidic midgut (pH 4.4–6.1) giving way to slightly alkaline hindgut (pH 7.3–7.9)** — and H₂ rising through the posterior midgut to a maximum in the anterior hindgut. Weight-specific methane emission averaged 17.4 nmol g fw⁻¹ h⁻¹ in *E. pulchripes* versus 6.5 in *A. gigas*, with the hindgut the site of methanogenesis ([Šustr/Nweze et al. 2021, *Applied and Environmental Microbiology*, doi:10.1128/AEM.00614-21](https://journals.asm.org/doi/full/10.1128/aem.00614-21); PMC8276800).

**(b) It is spatially compartmentalised, with an adherent cuticle-associated biofilm.** Millipede hindgut cuticle is regionally differentiated along the anterior–posterior axis and carries correspondingly differentiated microbiomes: trichomycete fungi of the genus *Enterobryus* occupy only the anterior hindgut while filamentous bacteria dominate the posterior half; microbes form stable adherent films on the cuticular lining secreted by the hindgut epithelium, whereas foregut and midgut microbes are largely unattached ([Nardi, Bee & Taylor 2016, *Arthropod Structure & Development* 45:462–474, PMID 27597263](https://pubmed.ncbi.nlm.nih.gov/27597263/)). This is a habitat with attachment surfaces and internal zonation — the property that distinguishes a colonised organ from a transit corridor. It also explains the GOLD children `Hindgut > P1 segment` and `Hindgut > P3 segment`.

**(c) The resident community is taxonomically distinctive and largely undescribed.** Comparative metagenomics/metatranscriptomics of *E. pulchripes* and *Glomeris connexa* on identical diets recovered **282 MAGs from the former versus 33 from the latter, including 90 novel bacterial taxa**, with Bacteroidota dominating *E. pulchripes* hindguts and Pseudomonadota dominating *G. connexa* — yet with shared functional repertoires (carbohydrate hydrolysis, sulfate reduction, nitrogen cycling) pointing to a common trophic strategy ([Nweze, Šustr, Brune & Angel 2024, *Microbiome* 12:16, doi:10.1186/s40168-023-01731-7](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-023-01731-7); PMID 38287457). Methanogens (Methanobacteriales, Methanomassiliicoccales) occur as ecto- and endosymbionts of hindgut ciliates in the methane-emitting species — a three-level symbiosis specific to this host group.

**(d) It supports a distinct viral and eukaryotic compartment too**, not just bacteria: gut virome ([Nweze et al. 2024, *Environmental Microbiology*, doi:10.1111/1462-2920.16586](https://enviromicro-journals.onlinelibrary.wiley.com/doi/full/10.1111/1462-2920.16586); PMID 38356108) and CAZyme-expressing eukaryotes and bacteria in the holobiont of *Telodeinopus aoutii*, where the hindgut was the hotspot of cellulose/hemicellulose degradation and Proteobacteria and Bacteroidetes were the major CAZyme producers ([*Frontiers in Ecology and Evolution* 2022, doi:10.3389/fevo.2022.931986](https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2022.931986/full)).

**(e) The non-gut sites are attested habitats in their own right.** The cuticle surface hosts Laboulbeniales ascomycetes — obligate arthropod ectobionts, with the millipede-associated fauna growing from ~8 species before 2014 to ~30, including nine new *Rickia* spp. described from Diplopoda ([Santamaría, Enghoff & Reboleira 2016, *Phytotaxa* 243:101–127](https://www.biotaxa.org/Phytotaxa/article/view/phytotaxa.243.2.1); [Enghoff & Santamaría 2015, *Organisms Diversity & Evolution*, doi:10.1007/s13127-015-0208-8](https://link.springer.com/article/10.1007/s13127-015-0208-8); [Santamaría et al. 2018, *PLOS ONE*, doi:10.1371/journal.pone.0206900](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0206900)). Centipedes carry maternally inherited symbionts (*Wolbachia*, Rickettsiaceae) alongside a variable, often single-taxon-dominated community, with population of origin — not sex — structuring composition ([Vahtera, Rezola & Duplouy 2024, *Annales Zoologici Fennici* 61:33–45, doi:10.5735/086.061.0104](https://bioone.org/journals/annales-zoologici-fennici/volume-61/issue-1/086.061.0104/); [open text](https://www.utupub.fi/server/api/core/bitstreams/794bf3ea-9ed2-406b-a79e-9e40e90a5f44/content)). Centipede forcipules carry their own characterised surface and internal community ([*PLOS ONE*, doi:10.1371/journal.pone.0341165](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0341165); PMC12810838).

**(f) It is a source of named novel taxa — which is very likely what most of the 569 bare-node assertions are.** *Streptomyces kronopolitis* sp. nov. ([IJSEM, doi:10.1099/ijsem.0.001520](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.001520)), *Rhodococcus kronopolitis* sp. nov. (*Antonie van Leeuwenhoek* 106:1207–1214, 2014) and *Streptosporangium kronopolitis* sp. nov. were all described from the millipede *Kronopolites svenhedini*; antibiotic-producing actinobacteria have been isolated from the digestive tract of *Nedyopus dawydoffiae* ([PMC6315555](https://pmc.ncbi.nlm.nih.gov/articles/PMC6315555/)); and millipede gut isolates are an active source of cellulolytic enzymes ([*World J Microbiol Biotechnol* 2023, doi:10.1007/s11274-023-03620-5](https://link.springer.com/article/10.1007/s11274-023-03620-5)). **My inference, flagged:** the pattern of "isolate genome, host recorded, body site not recorded" matches the 569-assertion bare node exactly; I have not verified the individual GOLD records.

**(g) A caveat the curator should know, and should *not* put in the definition.** The assumption that millipedes depend on gut-microbial cellulose fermentation is contested. Sterile or antibiotic-treated litter reduced faecal production and microbial load without major effects on survival or weight; BES treatment halted CH₄ emission reversibly; and ¹³C-litter RNA-SIP showed slow, gradual prokaryotic labelling with a significant density shift only by day 21 — leading the authors to conclude that microbial fermentation and methanogenesis are **non-essential** for millipede nutrition, with litter-associated microbes (bacteriovory/fungivory) the more likely nutritional route ([Nweze et al. 2024, *Communications Biology* 7:1204, doi:10.1038/s42003-024-06821-2](https://www.nature.com/articles/s42003-024-06821-2); PMID 39342029; preprint [doi:10.1101/2024.03.01.582937](https://www.biorxiv.org/content/10.1101/2024.03.01.582937v1)). This does not weaken the case for the term — the habitat is real and demonstrably colonised either way — but it means **no functional/mutualistic claim ("in which litter cellulose is fermented", "which digests plant polymers for its host") belongs in the definition**. That would be the one sentence in this report a curator could turn into an unsupportable ontology assertion.

---

## 4. Sources

Grouped by what they support. All are primary literature, reference works, or standards, except where noted.

**Concept scope and classification scheme**
- Mukherjee S. et al. (2023) Twenty-five years of Genomes OnLine Database (GOLD)… v.9. *Nucleic Acids Research* 51:D957–D963. https://academic.oup.com/nar/article/51/D1/D957/6786204 — PMID 36318257. *(five-level Host-associated → Ecosystem Category structure)*
- GOLD Ecosystem Classification. https://gold.jgi.doe.gov/ecosystem_classification
- Yilmaz P. et al. (2011) Minimum information about a marker gene sequence (MIxS). *Nature Biotechnology* 29:415–420. doi:10.1038/nbt.1823
- `data/raw/gold_ecosystem_paths.tsv` in this repository *(21 paths; 569 bare-node / 605 subtree assertions — counts computed for this report)*

**Ontology**
- Buttigieg P.L. et al. (2013) The environment ontology. *J Biomed Semantics* 4:43. doi:10.1186/2041-1480-4-43
- Buttigieg P.L. et al. (2016) The environment ontology in 2016. *J Biomed Semantics* 7:57. PMC5035502
- ENVO term records via EBI OLS4: `ENVO:01001000`, `ENVO:01001002`, `ENVO:01001055`, `ENVO:01001176`, `ENVO:01001179`, `ENVO:01001041`, `ENVO:01001001`
- NCBI Taxonomy (verified via E-utilities esummary, 2026-08-17): Myriapoda **61985** (subphylum); Diplopoda **7553**, Chilopoda **7540**, Symphyla **61986**, Pauropoda **63448** (classes)

**Host biology and diversity**
- Wright J. (eLS) Myriapoda (Including Centipedes and Millipedes). doi:10.1002/9780470015902.a0001607.pub3
- Bergeron M.D. et al. (2019) Myriapoda of Canada. *ZooKeys*. PMC6355731
- *Millipede genomes reveal unique adaptations during myriapod evolution* (2020), PMC7523956 / bioRxiv doi:10.1101/2020.01.09.900019 *(ozadene defensive gland; antimicrobial gene sets)*

**Habitat physicochemistry, structure and community**
- Šustr V./Nweze J.E. et al. (2021) Methanogenesis in the digestive tracts of *Archispirostreptus gigas* and *Epibolus pulchripes*. *Appl Environ Microbiol*. doi:10.1128/AEM.00614-21 / PMC8276800
- Nardi J.B., Bee C.M., Taylor S.J. (2016) Compartmentalization of microbial communities that inhabit the hindguts of millipedes. *Arthropod Struct Dev* 45:462–474. PMID 27597263
- Nweze J.E., Šustr V., Brune A., Angel R. (2024) Functional similarity, despite taxonomical divergence… *Microbiome* 12:16. doi:10.1186/s40168-023-01731-7 / PMID 38287457
- Nweze J.E. et al. (2024) Disruption of millipede-gut microbiota… *Commun Biol* 7:1204. doi:10.1038/s42003-024-06821-2 / PMID 39342029
- Nweze J.E. et al. (2024) Viral communities in millipede guts. *Environ Microbiol*. doi:10.1111/1462-2920.16586 / PMID 38356108
- Metatranscriptomic holobiont analysis of CAZymes in *Telodeinopus aoutii*. *Front Ecol Evol* (2022). doi:10.3389/fevo.2022.931986
- Vahtera V., Rezola U., Duplouy A. (2024) Bacterial diversity associated with *Lithobius forficatus*. *Ann Zool Fennici* 61:33–45. doi:10.5735/086.061.0104
- Bacterial community associated with the surface and inside of centipede forcipules. *PLOS ONE*. doi:10.1371/journal.pone.0341165 / PMC12810838

**Non-gut sites, isolates, and the litter boundary**
- Santamaría S., Enghoff H., Reboleira A.S.P.S. (2016) …Laboulbeniales in millipedes: genus *Rickia*. *Phytotaxa* 243:101–127
- Enghoff H., Santamaría S. (2015) Infectious intimacy and contaminated caves… *Org Divers Evol*. doi:10.1007/s13127-015-0208-8
- Santamaría S. et al. (2018) …Laboulbeniales on the millipede order Chordeumatida. *PLOS ONE*. doi:10.1371/journal.pone.0206900
- *Streptomyces kronopolitis* sp. nov. *IJSEM*. doi:10.1099/ijsem.0.001520
- Antibiotic activity of actinobacteria from the digestive tract of *Nedyopus dawydoffiae*. PMC6315555
- Millipede gut-derived microbes as a potential source of cellulolytic enzymes. *World J Microbiol Biotechnol* (2023). doi:10.1007/s11274-023-03620-5
- Litter-type specific microbial responses to the transformation of leaf litter into millipede feces. *Soil Biol Biochem* (2015). https://www.sciencedirect.com/science/article/abs/pii/S0038071715001054
- Chemical defence in *Pachyiulus hungaricus*: antimicrobial activity of defensive secretions. PMC5132186; Ilić et al. (2018) *J Appl Entomol*. doi:10.1111/jen.12526

**Statements in this report that are my inference, not a source's claim**, are flagged inline in §1 (heterogeneity as an argument against physicochemical differentia), §3(f) (what the 569 bare-node assertions consist of), and §5 (GOLD template artefacts).

---

## 5. Synonyms, and what NOT to conflate

**Names in real use for this concept (candidate exact/related synonyms):**
- myriapod-associated environment
- myriapod-associated habitat
- myriapod host-associated environment
- millipede-associated environment / centipede-associated environment *(narrower — see below)*
- "Arthropoda: Myriapoda" *(GOLD's own string; a related synonym at best, since it is a taxon label doing duty as an environment label)*

**Do not conflate with:**

| Thing | Why it is different |
|---|---|
| **Myriapoda the taxon** (`NCBITaxon:61985`) | A class of organisms, not a place. Per the repo rule and #114, this goes in `relation: xref`; the *environment determined by* a myriapod is the habitat. |
| **Diplopoda / Chilopoda** (`NCBITaxon:7553` / `7540`) | Proper subsets. A millipede-hindgut sample is a myriapod-associated sample; the converse does not hold, and their trophic biology and gut chemistry differ sharply. If a curator later needs them, they are child term requests, not this one. |
| **Insect-, crustacean-, chelicerate-associated environments** | Coordinate GOLD host categories (`Arthropoda: Insects`, 1,833; `Arthropoda: Crustaceans`, 598; `Arthropoda: Chelicerates`). Sibling concepts, not the same concept. Merging on "arthropod" would discard exactly the distinction GOLD records. |
| **Soil / leaf litter** (`ENVO:00001998`, `ENVO:03501259`) | The surrounding environment the animal inhabits and ingests. Compositional overlap is high and real (§1, §3g), which makes the boundary worth stating explicitly rather than assuming. |
| **`ENVO:01001176` environment associated with an aquatic invertebrate** | Asserts an aquatic setting; myriapods are terrestrial. |
| **The millipede defensive-secretion system** (ozadenes, benzoquinones) | A chemical-defence apparatus with demonstrated antimicrobial activity — a *constraint on* the habitat, not a habitat, and no part of the definition. |
| **GOLD sub-paths that are template artefacts** | `… > Respiratory system > Gills` (myriapods respire via tracheae and spiracles, not gills), `… > Integument > Cuticle > Thoracic segments` and `… > Integumentary system > Cuticle > Prothorax` (myriapods have a head + undifferentiated trunk of iterated segments; they have no thorax). All carry **0 assertions**, so nothing is lost, but they should not be read as evidence about myriapod anatomy. *(That these are artefacts of a shared arthropod template is my inference; the anatomy is standard — see the eLS chapter and the millipede-genome paper.)* |

---

## 6. Whether it should be a term at all

**Yes — as a habitat term, with the taxon kept separate.**

This is the exact case CLAUDE.md and issues #112/#114 legislate. Two distinct claims must not be merged:

1. **A myriapod acting as a host is a place where microbes live.** That is well supported: a compartmentalised, anoxic, strongly reducing gut with a pH discontinuity and an adherent cuticle-associated biofilm; 90 novel bacterial taxa from two species alone; named type strains described from millipede hosts; an ectobiont fungal fauna on the cuticle; inherited symbionts in centipedes. ENVO already models exactly this shape at plant-, animal-, fungi- and cnidarian-associated environment.
2. **The taxon Myriapoda is not a place.** A subphylum is a class of organisms.

So: **keep the minted identity, do not mark `NOT_APPLICABLE`.** `NOT_APPLICABLE` is the stronger and wrong claim here — it is reserved for diseases, qualities, processes and procedures, and `tests/test_decisions.py` fails on a `NOT_APPLICABLE` whose target is an organism term. The existing `CONFIRM_UNGROUNDED` + parent `ENVO:01001002` + ENVO term request is the right disposition, and this report supports it rather than revising it.

**One practical warning for the curator.** `NCBITaxon:61985` (*Myriapoda*) is **not in the vendored ontology slice** — `data/raw/ontology_terms.tsv` carries only 31 NCBITaxon terms, including `NCBITaxon:6656` *Arthropoda* and `NCBITaxon:50557` *Insecta*, but no Myriapoda, Diplopoda, Chilopoda, Symphyla or Pauropoda. An `xref` to `NCBITaxon:61985` will therefore fail the slice/label check that guards every decision target. Either vendor the term (cf. #10) or use `NCBITaxon:6656` *Arthropoda* as the xref with the myriapod restriction stated in the note — the first is better, because the second discards the very distinction this record exists to hold.

---

## Curator hand-off — what to record

- **Decision:** `CONFIRM_UNGROUNDED` on `habitatmech:GOLD.2333d6225a` *(unchanged)*
- **Parent:** `ENVO:01001002` *animal-associated environment* — `relation: parent` (genuinely broader: a myriapod is an animal)
- **Xref:** `NCBITaxon:61985` *Myriapoda* — `relation: xref`, **contingent on vendoring the term first**
- **ENVO NTR:** label *myriapod-associated environment*; definition "An animal-associated environment which is determined by a myriapod (Myriapoda) or by a part of a myriapod."; genus `ENVO:01001002`; differentia referencing `NCBITaxon:61985`; modelled verbatim on `ENVO:01001179` *cnidarian-associated environment*; cite Nweze et al. 2024 (*Microbiome* 12:16), Nardi et al. 2016 and Šustr/Nweze et al. 2021 as the evidence that the class carves a real habitat. **Per the standing rule, do not submit this or any other term request without explicit per-request permission.**
- **Do not** encode gut physicochemistry, cellulose fermentation, or any mutualism claim in the definition — §1 (clade heterogeneity) and §3(g) (contested nutritional role) both cut against it.

## Citations

1. https://academic.oup.com/nar/article/51/D1/D957/6786204
2. https://pubmed.ncbi.nlm.nih.gov/36318257/
3. https://www.nature.com/articles/s42003-024-06821-2
4. https://onlinelibrary.wiley.com/doi/10.1002/9780470015902.a0001607.pub3
5. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6355731/
6. https://link.springer.com/article/10.1186/2041-1480-4-43
7. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035502/
8. https://www.nature.com/articles/nbt.1823
9. https://journals.asm.org/doi/full/10.1128/aem.00614-21
10. https://pubmed.ncbi.nlm.nih.gov/27597263/
11. https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-023-01731-7
12. https://enviromicro-journals.onlinelibrary.wiley.com/doi/full/10.1111/1462-2920.16586
13. https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2022.931986/full
14. https://www.biotaxa.org/Phytotaxa/article/view/phytotaxa.243.2.1
15. https://link.springer.com/article/10.1007/s13127-015-0208-8
16. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0206900
17. https://bioone.org/journals/annales-zoologici-fennici/volume-61/issue-1/086.061.0104/
18. https://www.utupub.fi/server/api/core/bitstreams/794bf3ea-9ed2-406b-a79e-9e40e90a5f44/content
19. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0341165
20. https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.001520
21. https://pmc.ncbi.nlm.nih.gov/articles/PMC6315555/
22. https://link.springer.com/article/10.1007/s11274-023-03620-5
23. https://www.biorxiv.org/content/10.1101/2024.03.01.582937v1
24. https://gold.jgi.doe.gov/ecosystem_classification
25. https://www.sciencedirect.com/science/article/abs/pii/S0038071715001054