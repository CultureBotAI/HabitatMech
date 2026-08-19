---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T02:59:21.176304'
end_time: '2026-08-18T03:10:40.328992'
duration_seconds: 679.15
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Stone
  habitat_identifier: habitatmech:GOLD.8c6192908f
  habitat_category: ENGINEERED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Engineered > Built environment > Monument > Stone'
  assertions: '0'
  parent_terms: (none)
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Stale-sweep
    review (#12): NCIT:C35708 ''Stone'' matches the label, but the path is Built environment
    > Monument > Stone, and NCIT''s term is not the building material. Stonework is
    a real habitat with no term in the slice. Path: Engineered > Built environment
    > Monument > Stone (source concept habitatmech:GOLD.8c6192908f)'
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
  web_search_requests: 6
  num_turns: 42
  total_cost_usd: 2.7242699999999993
  session_id: 56e38671-4eed-4d04-a87f-47cb8618fbd2
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 27
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Stone
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.8c6192908f
- **Category:** ENGINEERED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Engineered > Built environment > Monument > Stone
- **Upstream assertion volume:** 0
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Stale-sweep review (#12): NCIT:C35708 'Stone' matches the label, but the path is Built environment > Monument > Stone, and NCIT's term is not the building material. Stonework is a real habitat with no term in the slice. Path: Engineered > Built environment > Monument > Stone (source concept habitatmech:GOLD.8c6192908f)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Stone** as a microbial habitat, with citations.

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

# Stone (`habitatmech:GOLD.8c6192908f`) — novel-term definition research

> **Proposed definition:** A rock which has been quarried and worked into the fabric of a constructed monument, and whose atmosphere-exposed surface and near-surface pore space are colonised by subaerial microbial biofilms.

If the curator prefers ENVO's composition idiom for anthropogenic built materials (the pattern used by *stone exterior wall*, *stone building floor*), the same content reads: *"An anthropogenic environmental material, composed primarily of rock, which forms the atmosphere-exposed fabric of a constructed monument."* Both are one sentence; the second avoids asserting that a dressed block is still an instance of `ENVO:00001995 rock` (see §2 for why that assertion is defensible but arguable).

---

## 1. What the concept denotes

**The reading the data supports.** GOLD's path is `Engineered > Built environment > Monument > Stone`, and the corpus's own raw inventory settles the ambiguity two ways:

- **Its only child is a rock type.** `Engineered > Built environment > Monument > Stone > Sandstone` (`gold.ecosystem:7127`, 1 organism), already grounded in this corpus to `ENVO:00002055 sandstone` (`data/habitats/engineered/sandstone.yaml`). A node whose children are lithologies is a **material** node, not a monument-object node.
- **Its only sibling is a building element.** `Engineered > Built environment > Monument > Interior wall` (`gold.ecosystem:7676|7677`). So GOLD partitions a monument by *which part/material you swabbed*: the stonework, or the interior wall (the latter typically plastered/painted, the mural-painting habitat).

So **Stone here = the worked natural stone that constitutes a monument's fabric** — the substratum a heritage-microbiology sample is taken from, whether by swabbing/scraping the exposed surface biofilm or crust, or by drilling/chipping into the sub-surface (endolithic) zone. It is "stonework" in the curator's phrasing.

**Inside the concept:** dressed and undressed masonry stone, carved stone (statues, stelae, reliefs, sculpted rock-cut surfaces), stone facing and paving of monuments; all common heritage lithologies — limestone, marble, sandstone, granite, basalt ([Li et al. 2016](https://doi.org/10.1371/journal.pone.0163287); [Ma et al. 2025](https://doi.org/10.3389/fmicb.2025.1600865); [Zhang et al. 2026](https://doi.org/10.1186/s40168-025-02324-2)). Both the epilithic (on-surface) and endolithic (within-pore) microhabitats of that stone: the same sampled block hosts both, and endolithic communities in monument stone are taxonomically distinct from epiliths at the same site ([Scheerer, Ortega-Morales & Gaylarde 2009](https://doi.org/10.1016/S0065-2164(08)00805-8)).

**Neighbouring concepts, explicitly outside:**

| Neighbour | Why it is not this |
|---|---|
| **Natural rock outcrop / subaerial rock biofilm** | GOLD gives these their own, far better-attested branches under a *different* top-level ecosystem: `Environmental > Terrestrial > Rock-dwelling (subaerial biofilms)` (103 organisms) and `Rock-dwelling (endoliths)` (88 organisms). The ENGINEERED node exists precisely because the substratum is a human construction. |
| **Deep-subsurface rock** | `Environmental > Terrestrial > Deep subsurface > Rock` (49) — aphotic, water-saturated, no atmosphere interface. |
| **Interior wall / mural painting / fresco** | GOLD's sibling node; plaster and paint layers, not stone, and usually indoor. |
| **Concrete, mortar, brick, plaster, stucco** | Manufactured masonry materials with their own bioreceptivity and corrosion chemistry (`ENVO:00002870 adobe`, `ENVO:01000476 plaster`, `ENVO:01000487 brick building floor`). Mortar joints often carry the densest colonisation, but they are not stone. |
| **Show caves and rock-cut cave sanctuaries** (Lascaux, Altamira) | Subterranean, low-light, high-humidity; sometimes overlapping with rock-cut heritage such as grottoes, which is a genuine grey zone — the Longmen Grottoes and Beishiku Temple studies below sit on the boundary between "monument stone" and "cave wall". |
| **Building stone in ordinary (non-commemorative) buildings** | GOLD's parent node is *Monument*, and ENVO's `constructed monument` requires a memorial function. The microbiology is the same; the concept boundary is functional, not biological. This is the single weakest edge of the concept. |

**A residual ambiguity worth recording:** GOLD's own node label is a bare "Stone", and the concept could in principle be read as *the monument-as-stone-object*. The child-is-a-lithology evidence above makes the material/substratum reading much stronger, and it is also the reading under which the concept has literature. I recommend the material reading; I do not think the object reading should be silently discarded, because a curator writing "A constructed monument which is composed primarily of rock…" would produce a defensible term too — just one that duplicates the parent record `Monument` (`habitatmech:GOLD.a8b8ee2424`) rather than complementing it.

---

## 2. Genus — the broader kind

**Nothing in the vendored slice names this concept.** I checked `data/raw/ontology_terms.tsv` directly as well as OLS4. The candidates and why each fails:

| Candidate | Status in slice | Verdict |
|---|---|---|
| `ENVO:00001995` **rock** — "a naturally occurring solid aggregate of one or more minerals or mineraloids" | present, directly referenced | **Best genus, not a match.** Far broader: covers all natural rock, which GOLD deliberately keeps in a separate branch. Grounding here would merge monument stonework with desert varnish, endolith, and deep-subsurface rock records. Also note the friction between "naturally occurring" and a quarried, dressed block — the rock's *material* is natural, its *form and placement* are not. Using it as genus is defensible (a marble block is still marble); using it as identity is not. |
| `ENVO:0010001` **anthropogenic environmental material** — "anthropogenic material in or on which organisms may live" | present, directly referenced | **Alternative genus.** Correct kind for a human-emplaced building material, but far too broad on its own. |
| `ENVO:02000132` **constructed monument** — "A human construction which serves as a memorial" (synonym: *monument*; subclass of `ENVO:00000070 human construction`) | **present in slice** | **Not the genus for this record — but it is very likely the right grounding or parent for the *parent* record** `Monument` (`habitatmech:GOLD.a8b8ee2424`), which is currently UNGROUNDED with only `mesh:D000076624` as parent. Worth raising as a separate finding. For *Stone*, the relation is part-of/composed-of, not is-a, so it belongs in `relation: xref`. |
| `ENVO:01000495` **stone exterior wall** — "an exterior wall that is composed primarily of rock" (syn. *stone wall*) | present | **Narrower**, and asserts building-wall-hood. A stele or a statue is not a wall. Records the exact composition pattern ENVO uses, though. |
| `ENVO:01000493` **stone building floor** (syn. *stone floor*, *rock floor*) | present | Narrower still; floors only. |
| `ENVO:01000457` **masonry unit** — "a solid piece of material… used as a component in the construction of buildings… brick, stone, marble, granite, travertine, limestone, cast stone, concrete block…" | present | **Closest single artefact term, still a near-miss.** It is a countable *unit* (a block), it is material-agnostic (brick and concrete included), and it asserts building-construction use. It does not cover carved monolithic sculpture or rock-cut surfaces. Good `xref`. |
| `ENVO:00000339` **piece of rock** | present | A detached mass of rock; says nothing about human working or emplacement. |
| `ENVO:00000073` **building**, `ENVO:01000420` **building part** | present | Wrong level and asserts building-hood. |
| `ENVO:00000359` **natural monument**, `ENVO:01001165` **IUCN natural monument or feature**, `ENVO:00000375` **world heritage site**, `ENVO:03501273` **listed building** | present/available | Protected-area and legal-designation terms. The `natural monument` trap was already caught on the parent record (#67). |
| `NCIT:C35708` **Stone** | — | **Confirmed a false friend**, as the existing note says: NCIT defines it as "Accumulated material from the secretions of an organ… gallbladder stones, kidney stones" — synonyms CALCULUS, Calculi. Nothing to do with building material. |

**Conclusion:** the missing intermediate class is *building stone / monument stone / stonework* — a rock-composed anthropogenic environmental material forming the fabric of a construction. ENVO has the wall and the floor made of it, and the monument that is made of it, but not the material itself. That is a clean, small ENVO new-term request (see §6).

---

## 3. Differentia — what distinguishes it

Ranked by how observable each property is at sampling time.

1. **Substratum is worked natural stone emplaced by humans in a monument.** This is the sortal difference from `Rock-dwelling (subaerial biofilms)`: quarrying and dressing change surface roughness, porosity, and exposed mineral faces, which is the *primary bioreceptivity* of Guillitte's framework — "the ability of a material to be colonised by living organisms" ([Guillitte 1995, *Sci Total Environ* 167:215–220](https://doi.org/10.1016/0048-9697(95)04582-L); revisited by [Vázquez-Nion et al. 2021](https://doi.org/10.1016/j.scitotenv.2021.145314)).
2. **Atmosphere–mineral interface, subaerially exposed.** The characteristic community form is the **subaerial biofilm (SAB)** — a term coined for microbial communities developing on solid mineral surfaces in direct contact with the atmosphere and solar radiation, patchy and dominated by associations of fungi, algae, cyanobacteria and heterotrophic bacteria ([Gorbushina 2007, *Environ Microbiol* 9:1613–1631](https://doi.org/10.1111/j.1462-2920.2007.01301.x); PMID [17564597](https://pubmed.ncbi.nlm.nih.gov/17564597/)).
3. **Oligotrophic, self-sufficient, photoautotroph-founded.** Nutrients come from atmospheric deposition, not the substratum; cyanobacteria are the main organic-carbon producer that supports the rest of the community ([Zhang et al. 2026, *Microbiome*](https://doi.org/10.1186/s40168-025-02324-2)). Cyanobacteria dominated newly formed biofilms at Beishiku Temple ([Zhang et al. 2024, *Environ Res*](https://pubmed.ncbi.nlm.nih.gov/38432571/)) and made up ~50% of bacterial communities at Hangzhou monuments, rising to 63–69% on white marble ([Li et al. 2016](https://doi.org/10.1371/journal.pone.0163287)).
4. **Extreme physical stress regime: desiccation–rehydration cycling, UV, temperature swings, salt.** This is what selects the characteristic taxa — melanised microcolonial/rock-inhabiting fungi, *Geodermatophilus*-type actinobacteria, desiccation-tolerant cyanobacteria ([Gorbushina 2007](https://doi.org/10.1111/j.1462-2920.2007.01301.x); [Gorbushina & Broughton 2009, *Annu Rev Microbiol* 63:431–450](https://doi.org/10.1146/annurev.micro.091208.073349)). Desiccation measurably reprograms SAB metabolism and alters water dynamics in the limestone itself ([Villa et al. 2023, *Sci Total Environ*](https://doi.org/10.1016/j.scitotenv.2023.161666)). A named example: the desiccation-tolerant cyanobacterium *Lyngbya corticicola* on the 7th-century Parsurameswara monument, India ([Parvin et al. 2024, *Biofouling*](https://pubmed.ncbi.nlm.nih.gov/38359904/)).
5. **Anthropogenic nutrient and pollutant loading.** Colonisation intensity is governed by climate plus atmospheric eutrophication, and microbes metabolise anthropogenic pollutants (NOₓ, SOₓ) deposited on the surface ([Warscheid & Braams 2000, *Int Biodeterior Biodegrad* 46:343–368](https://doi.org/10.1016/S0964-8305(00)00109-8)). Site-to-site differences in NO₂/SO₂ tracked community differences among Hangzhou monuments ([Li et al. 2016](https://doi.org/10.1371/journal.pone.0163287)). Nitrifying bacteria are a classic monument-stone guild whose nitric-acid output dissolves carbonate binder ([Mansch & Bock 1998, *Biodegradation* 9:47–64](https://doi.org/10.1023/A:1008381525192)); nitrification and ammonia oxidation are identified as the main driver of biodeterioration dynamics at Longmen ([Zhang et al. 2026](https://doi.org/10.1186/s40168-025-02324-2)), and *Nitrososphaeraceae* exceeded 90% of archaea in most Leizhou biofilms ([Ma et al. 2025](https://doi.org/10.3389/fmicb.2025.1600865)).
6. **Lithology-conditioned community structure.** Chemical nature, mechanical strength, solubility and porosity of the substratum are among the strongest controls, alongside humidity, temperature, light and air-pollutant composition ([Warscheid & Braams 2000](https://doi.org/10.1016/S0964-8305(00)00109-8); [Scheerer et al. 2009](https://doi.org/10.1016/S0065-2164(08)00805-8)). This is why GOLD's own child node is a lithology.
7. **Management as an active environmental variable — distinctive to this habitat and to no natural one.** Conservation interventions (biocides, consolidants, shade structures, ornamental floodlighting) restructure the community: protective shading shifted Beishiku Temple biofilms to cyanobacterial dominance ([Zhang et al. 2024](https://pubmed.ncbi.nlm.nih.gov/38432571/)), and ornamental lighting of granite façades measurably shifted the microbiome ([Méndez et al. 2024, *J Photochem Photobiol B*](https://pubmed.ncbi.nlm.nih.gov/39549663/)). *This point is my synthesis across those two studies; neither states it as a general definitional property.*

**Typical taxa, for the curator's notes rather than the definition sentence:** cyanobacteria (*Leptolyngbya*, *Chroococcidiopsis*), Actinomycetota (*Pseudonocardia*, *Rubrobacter*, *Geodermatophilus*), Pseudomonadota (*Sphingomonas*, *Massilia* — 28.3% of bacteria across Leizhou samples), ammonia-oxidising archaea (*Nitrososphaeraceae*), Ascomycota including black meristematic fungi (*Devriesia*, *Rhinocladiella*), and lichens (*Lepraria*, *Verrucaria*, *Dirina*, *Xanthoria*) ([Li et al. 2016](https://doi.org/10.1371/journal.pone.0163287); [Ma et al. 2025](https://doi.org/10.3389/fmicb.2025.1600865)).

---

## 4. Sources

Primary and review literature

- Warscheid T, Braams J (2000). Biodeterioration of stone: a review. *Int Biodeterior Biodegrad* 46:343–368. https://doi.org/10.1016/S0964-8305(00)00109-8 — foundational; bioreceptivity, EPS-driven mechanical stress, atmospheric eutrophication. [Open PDF mirror](http://awarticles.s3.amazonaws.com/Warscheid2000.pdf)
- Gorbushina AA (2007). Life on the rocks. *Environ Microbiol* 9(7):1613–1631. https://doi.org/10.1111/j.1462-2920.2007.01301.x — **the source for the "subaerial biofilm" concept**, which is the closest thing to a definition of this habitat in the literature.
- Gorbushina AA, Broughton WJ (2009). Microbiology of the atmosphere–rock interface. *Annu Rev Microbiol* 63:431–450. https://doi.org/10.1146/annurev.micro.091208.073349
- Scheerer S, Ortega-Morales O, Gaylarde C (2009). Microbial deterioration of stone monuments — an updated overview. *Adv Appl Microbiol* 66:97–139. https://doi.org/10.1016/S0065-2164(08)00805-8 — epilithic vs. true-endolithic distinction on monuments.
- Guillitte O (1995). Bioreceptivity: a new concept for building ecology studies. *Sci Total Environ* 167:215–220. https://doi.org/10.1016/0048-9697(95)04582-L
- Vázquez-Nion D, Silva B, Prieto B (2021). Revisiting and reanalysing the concept of bioreceptivity 25 years on. *Sci Total Environ* 770:145314. https://doi.org/10.1016/j.scitotenv.2021.145314
- Mansch R, Bock E (1998). Biodeterioration of natural stone with special reference to nitrifying bacteria. *Biodegradation* 9:47–64. https://doi.org/10.1023/A:1008381525192
- Liu X, Koestler RJ, Warscheid T, Katayama Y, Gu J-D (2020). Microbial deterioration and sustainable conservation of stone monuments and buildings. *Nature Sustainability* 3:991–1004. https://doi.org/10.1038/s41893-020-00602-5 — the standard recent review.
- Gadd GM (2017). Geomicrobiology of the built environment. *Nature Microbiology* 2:16275. https://doi.org/10.1038/nmicrobiol.2016.275
- Li Q, Zhang B, He Z, Yang X (2016). Distribution and diversity of bacteria and fungi colonization in stone monuments analyzed by high-throughput sequencing. *PLoS ONE* 11(9):e0163287. https://doi.org/10.1371/journal.pone.0163287 · [PMC5033376](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5033376/)
- Villa F, Ludwig N, Mazzini S, et al. (2023). A desiccated dual-species subaerial biofilm reprograms its metabolism and affects water dynamics in limestone. *Sci Total Environ* 861:161666. https://doi.org/10.1016/j.scitotenv.2023.161666
- Ma C, Zhang X, Wu F, Liu X (2025). Identifying keystone taxa and metabolisms of epilithic biofilms is crucial to the conservation of stone heritage from biodeterioration. *Front Microbiol* 16:1600865. https://doi.org/10.3389/fmicb.2025.1600865 · [PMC12150296](https://pmc.ncbi.nlm.nih.gov/articles/PMC12150296/)
- Zhang X, Ma C, Wu F, Liu X (2026). Unraveling the microbiomes contributing to biodeterioration dynamics of limestone heritage at the Longmen Grottoes archeological site. *Microbiome*. https://doi.org/10.1186/s40168-025-02324-2 · PMID [41736163](https://pubmed.ncbi.nlm.nih.gov/41736163/)
- Zhang Y, Wu F, Gu J-D, et al. (2024). Dominance by cyanobacteria in the newly formed biofilms on stone monuments under a protective shade at the Beishiku Temple in China. *Environ Res*. PMID [38432571](https://pubmed.ncbi.nlm.nih.gov/38432571/)
- Parvin N, Mandal S, Rath J (2024). Microbiome of seventh-century old Parsurameswara stone monument of India and role of desiccation-tolerant *Lyngbya corticicola* on its biodeterioration. *Biofouling*. PMID [38359904](https://pubmed.ncbi.nlm.nih.gov/38359904/)
- Méndez A, Maisto F, Pavlović J, et al. (2024). Microbiome shifts elicited by ornamental lighting of granite facades identified by MinION sequencing. *J Photochem Photobiol B*. PMID [39549663](https://pubmed.ncbi.nlm.nih.gov/39549663/)
- Diversity and biodeterioration potential of culturable microorganisms in Beishiku Temple sandstone: [PMC9965415](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9965415/)
- Community assembly on red sandstone shaped by dispersal limitation and heterogeneous selection (2025): [PMC12817949](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12817949/)

Standards and vocabularies

- GOLD Ecosystem Classification, JGI — https://gold.jgi.doe.gov/ecosystem_classification (source of the path; the five-level scheme is sample-driven, not an exhaustive enumeration)
- MIxS built-environment extension: Glass EM, et al. (2013/2014). MIxS-BE. *ISME J* 8:1–3. https://doi.org/10.1038/ismej.2013.176 — the GSC package under which such samples are reported.
- ENVO — https://obofoundry.org/ontology/envo.html; terms verified via OLS4 and against this repo's `data/raw/ontology_terms.tsv`.
- NCIT:C35708 verified via OLS4 (`http://purl.obolibrary.org/obo/NCIT_C35708`).

**Explicitly my inference, not sourced:** (a) the claim that GOLD's `Stone` node denotes the material rather than the monument-object — inferred from its child (Sandstone) and sibling (Interior wall) in `data/raw/gold_ecosystem_paths.tsv`; (b) the conservation-intervention differentia in §3.7; (c) the judgement that no ENVO term matches — an exhaustive-search claim, and exhaustive-search claims are the ones that age worst.

---

## 5. Synonyms and what not to conflate

**Names in real use** (candidate `RELATED_SYNONYM`s; none is an exact-match label I would promote to the primary label):

- monument stone; stonework; building stone; heritage stone; stone heritage; stone cultural heritage; ornamental stone; dimension stone (trade term); masonry stone; stone monument surface; historic/monumental stone.
- Habitat-form names for what grows on it, which are frequently used as if they named the habitat: **subaerial biofilm (SAB)**, epilithic biofilm, lithobiontic community, biological patina/soiling, black crust.

**Commonly but wrongly treated as the same thing:**

- **`NCIT:C35708 Stone`** = calculus (kidney/gallbladder stone). Already caught in the record's note; the strongest label collision in the whole space.
- **Natural rock / rock outcrop** (`ENVO:00001995`). Same microbiology in large part, different concept and a different GOLD branch.
- **Stone *tools* / lithic artefacts** in archaeology — a "stone artefact" microbiome is a different (usually excavated, buried) habitat.
- **Black crust as a synonym for stone.** A black crust is a gypsum-rich alteration layer *on* the stone; it is a product, not the substratum.
- **Biofilm as a synonym for stone.** The biofilm is the community; the stone is the habitat. Conflating them is what the `env_medium` vs `env_local_scale` split in MIxS exists to prevent.
- **Concrete/mortar biodeterioration.** Shares the nitrifying- and sulfur-oxidiser literature (e.g. Sand & Bock) but is a manufactured material.
- **Cave and catacomb walls.** Overlapping taxa and adjacent literature; low-light subterranean conditions make it a distinct habitat. Rock-cut grottoes (Longmen, Beishiku) genuinely straddle the line and should be called out in the note rather than resolved silently.
- **`ENVO:00000359 natural monument` / `ENVO:01001165 IUCN natural monument or feature`.** Protected-area designations for natural formations — the exact error already corrected on the parent record.

---

## 6. Should it be a term at all — yes

This is a habitat, not a process, quality, disease, taxon or sampling artefact. It is a physical place a sample is taken from, it has a substantial dedicated literature under the names *stone heritage microbiology* and *subaerial biofilm*, and it is separated from natural rock by a real, measurable property (bioreceptivity of worked stone plus anthropogenic nutrient loading), not merely by provenance labelling.

Recommended disposition:

- **Keep the minted identity** `habitatmech:GOLD.8c6192908f` and treat it as an **ENVO new-term-request candidate**. The requested term is the missing material class — *"building stone"* or *"monument stone"*: an anthropogenic environmental material composed primarily of rock, forming the fabric of a human construction. ENVO already has `stone exterior wall` and `stone building floor` "composed primarily of rock", so the request slots into an existing pattern rather than opening a new branch.
- **`relation: xref`, not parent:** `ENVO:02000132 constructed monument` (the stone is *part of* a monument, not a kind of one) and `ENVO:01000457 masonry unit` (countable block; material-agnostic).
- **Defensible parent:** `ENVO:00001995 rock`, or `ENVO:0010001 anthropogenic environmental material` if the curator judges that a quarried, dressed block strains ENVO rock's "naturally occurring". Both are in the vendored slice, with the labels quoted above. Do **not** use `ENVO:00000359 natural monument`.
- **Do not use `NOT_APPLICABLE`.** Nothing here is a quality, process or disease.

**One finding outside this record's scope, for triage.** The parent record `Monument` (`habitatmech:GOLD.a8b8ee2424`) is UNGROUNDED with `mesh:D000076624` as its only parent, and its note says "the slice has no term for it" — but `ENVO:02000132 constructed monument` ("A human construction which serves as a memorial", synonym *monument*, subclass of `ENVO:00000070 human construction`) **is present in `data/raw/ontology_terms.tsv`** and looks like an exact match for GOLD's `Engineered > Built environment > Monument`. That note was written during the #67 sweep that removed the wrong `natural monument` grounding; it appears the correct constructed-monument term was not re-checked afterwards. Worth a separate decision, and it also fixes this record's parentage upward.

## Citations

1. https://doi.org/10.1371/journal.pone.0163287
2. https://doi.org/10.3389/fmicb.2025.1600865
3. https://doi.org/10.1186/s40168-025-02324-2
4. https://doi.org/10.1016/S0065-2164(08
5. https://doi.org/10.1016/0048-9697(95
6. https://doi.org/10.1016/j.scitotenv.2021.145314
7. https://doi.org/10.1111/j.1462-2920.2007.01301.x
8. https://pubmed.ncbi.nlm.nih.gov/17564597/
9. https://pubmed.ncbi.nlm.nih.gov/38432571/
10. https://doi.org/10.1146/annurev.micro.091208.073349
11. https://doi.org/10.1016/j.scitotenv.2023.161666
12. https://pubmed.ncbi.nlm.nih.gov/38359904/
13. https://doi.org/10.1016/S0964-8305(00
14. https://doi.org/10.1023/A:1008381525192
15. https://pubmed.ncbi.nlm.nih.gov/39549663/
16. http://awarticles.s3.amazonaws.com/Warscheid2000.pdf
17. https://doi.org/10.1038/s41893-020-00602-5
18. https://doi.org/10.1038/nmicrobiol.2016.275
19. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5033376/
20. https://pmc.ncbi.nlm.nih.gov/articles/PMC12150296/
21. https://pubmed.ncbi.nlm.nih.gov/41736163/
22. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9965415/
23. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12817949/
24. https://gold.jgi.doe.gov/ecosystem_classification
25. https://doi.org/10.1038/ismej.2013.176
26. https://obofoundry.org/ontology/envo.html
27. http://purl.obolibrary.org/obo/NCIT_C35708`