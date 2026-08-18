---
provider: claude_code
model: claude-opus-5[1m]
cached: false
start_time: '2026-08-18T04:05:15.201993'
end_time: '2026-08-18T04:20:13.889206'
duration_seconds: 898.69
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Fungi
  habitat_identifier: habitatmech:GOLD.1ab59245f7
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Endosymbionts > Fungi'
  assertions: '0'
  parent_terms: (none)
  xrefs: FOODON:03411261
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Nearest
    broader term FOODON:03411261 ''fungus'' attached as a parent. Organism-identity
    screen (#109): carried FOODON:03411261 ''fungus'' as a parent, a taxonomic grouping
    rather than a place, reached by the ambiguous-leaf rule. The concept is fungi
    acting as host to an endosymbiont, so it is the same family as the sponge and
    nematode term requests: it keeps its own identity, and the taxon term is kept
    as an xref (#99). (source concept habitatmech:GOLD.1ab59245f7)'
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
  - claude-opus-5[1m]
  web_search_requests: 4
  num_turns: 42
  total_cost_usd: 2.9784960000000003
  session_id: d148e191-d6c4-4231-b221-0411a7c0b4f3
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 27
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Fungi
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.1ab59245f7
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Endosymbionts > Fungi
- **Upstream assertion volume:** 0
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** FOODON:03411261

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term FOODON:03411261 'fungus' attached as a parent. Organism-identity screen (#109): carried FOODON:03411261 'fungus' as a parent, a taxonomic grouping rather than a place, reached by the ambiguous-leaf rule. The concept is fungi acting as host to an endosymbiont, so it is the same family as the sponge and nematode term requests: it keeps its own identity, and the taxon term is kept as an xref (#99). (source concept habitatmech:GOLD.1ab59245f7)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Fungi** as a microbial habitat, with citations.

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

# Deep-research report — `habitatmech:GOLD.1ab59245f7` "Fungi" (Host-associated > Endosymbionts > Fungi)

> **Proposed definition (conditional — see §1 and §6):**
> A fungi-associated environment which is the interior of a living fungal cell or hypha, in which the resident bacteria persist as heritable or facultative endosymbionts of the fungus.

**Read this first:** the source path is ambiguous in a way that changes the definition, and the evidence available does not resolve it cleanly. My recommendation is **not to mint a new term**: under the reading the definition above assumes, ENVO already supplies both the genus and — for the sibling record — an exact match (`ENVO:01001041` *fungi-associated environment*, already present in the vendored slice); under the competing reading the path names the isolate's taxon rather than a place and there is nothing to define. The path carries **zero upstream assertions**, so nothing in the corpus depends on getting a definition here.

---

## 1. What the concept denotes

### 1.1 The two readings

The label is `Fungi` at the third level of `Host-associated > Endosymbionts > Fungi`. Two mutually exclusive readings are grammatically available, and they place the *habitat* in different organisms:

| | Reading **A** — "endosymbionts **of** fungi" | Reading **B** — "endosymbionts **that are** fungi" |
|---|---|---|
| Sample is | a bacterium (or archaeon) living inside a fungus | a fungus living inside some unnamed host |
| Habitat denoted | the interior of a fungal cell/hypha | the interior of an unspecified host — a place the label does not name |
| Definable as a habitat? | yes | no (the leaf names the symbiont's kingdom, not a place) |

### 1.2 Evidence for each

**For A** — the only explicit machine-readable annotation of this path. The GOLD path ontology served by OLS annotates `https://w3id.org/gold.path/4734` ("Host-associated > Endosymbionts > Fungi") with `host_taxon: Fungi; mixs_extension: MIXS:HostAssociated; partial`, and links `NCBITaxon:4751` (Fungi) as the referenced entity ([OLS4, gold ontology, class 4734](https://www.ebi.ac.uk/ols4/ontologies/gold/classes?obo_id=4734)). This is what the current curation note relied on. Its weight is limited: the **sibling** path `Host-associated > Endosymbionts > Bacteria` (gold.path/4732) is annotated the same way as `host_taxon: Bacteria`, i.e. "endosymbionts of bacteria" — a claim with essentially no microbiological support and no plausible curated sample behind it. That strongly suggests the `host_taxon` slot was filled mechanically from the leaf label rather than from GOLD's intent. *(Inference, mine.)*

**For B** — GOLD's own structural convention, visible in the same path table. When GOLD means "endosymbionts of host X", it puts the host at the category level and the relation at the type level:

- `Host-associated > Arthropoda > Intracellular endosymbionts` (and `> Primary`, `> Primary > Bacteriomes`, `> Secondary`)
- `Host-associated > Annelida > Intracellular endosymbionts` (and `> Trophosome`)

Under that convention, "endosymbionts of fungi" would be spelled `Host-associated > Fungi > Intracellular endosymbionts`. It is not. Furthermore, GOLD **already has a full fungus-as-host branch** — `Host-associated > Fungi` with 635 organism assertions and children *Mycelium* (260), *Fruiting body* (140), *Spore* (135), *Lichen* (66), *Fruiting body > Inner tissue* (63), plus *Appressorium*, *Germ tube*, *Mycorrhiza*, *Sclerotium*, *Stroma* — so a second fungus-as-host path would be redundant. (All counts from this repo's own extraction, `data/raw/gold_ecosystem_paths.tsv`; `Host-associated > Endosymbionts` sits in the ecosystem-**category** slot, where every one of its 26 siblings is a host taxon: Algae, Amphibia, Annelida, Birds, Cnidaria, **Fungi**, Mammals, Microbial, Plants, Porifera, …) *(Inference, mine, from repo data.)*

**What no evidence settles it:** the path has **0 organisms, 0 studies, 0 biosamples** in the extracted GOLD inventory. `Host-associated > Endosymbionts` as a whole holds 3 organisms and `> Bacteria` holds 1; `> Fungi` holds none. There is therefore no attested sample whose identity could disambiguate the leaf. GOLD's own documentation notes that the classification "is not a comprehensive list of all possible paths … it is primarily driven by the samples curated, and the paths are periodically reviewed and revised" ([JGI GOLD, Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification); Mukherjee et al. 2023, *Nucleic Acids Res* 51:D957–D963, [doi:10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974), PMID 36318257) — an unpopulated path is exactly the kind of scaffolding that convention describes.

### 1.3 The boundary, if reading A is taken

**Inside the concept:** the intracellular/intrahyphal compartment of a living fungal thallus — cytoplasm of hyphae, spores and sporangia — occupied by bacteria that are maintained inside fungal cells, whether vertically transmitted and unculturable (*Ca.* Glomeribacter gigasporarum, *Ca.* Moeniiplasma glomeromycotorum) or facultative and horizontally acquired (*Mycetohabitans*/*Paraburkholderia rhizoxinica*, *Mycoavidus cysteinexigens*, and the diverse endohyphal proteobacteria of foliar endophytes).

**Outside it (neighbouring concepts):**
- **Fungal surfaces and epibiotic biofilms** — `ENVO:01001035` *environment determined by a biofilm on a fungal surface*; the mycosphere/hyphosphere generally (Deveau et al. 2018).
- **Fungal tissue sampled as material** — `Host-associated > Fungi > Mycelium / Fruiting body / Spore` and `ENVO:01001058` *environment associated with a fungal tissue*.
- **Lichens** — a fungus–photobiont thallus, GOLD's own `Host-associated > Fungi > Lichen`, not an endosymbiont-in-fungus concept.
- **Mycorrhizal root tissue** — the fungus inside a *plant*; the plant is the host there.
- **Fungi as food substrate** — `FOODON:03411261` and the mushroom/food branch of FOODON.
- **Host organs that house fungal symbionts** — `ENVO:01000166` *mycetome* ("A specialized organ that is linked to the gut in beetles and host to a symbiotic yeast"), `BTO:0006243` *bacteriocyte*. These are the concepts reading **B** would actually be about, and they already exist.

---

## 2. Genus — the broader kind

**Recommended genus: `ENVO:01001041` *fungi-associated environment*** — "An environmental system determined by a fungal structure." Synonyms in ENVO: *fungus environment*, *fungus-associated environment*.

This term **is already in the vendored slice** (`data/raw/ontology_terms.tsv`, marked `directly_referenced TRUE`), so a `GROUND` or `GROUND_AS_PARENT` against it will pass the label check. Its position is exactly the pattern this corpus's own term requests keep citing as precedent: it is a direct child of `ENVO:01001000` *environmental system determined by an organism*, alongside `ENVO:01001001` *plant-associated environment* and `ENVO:01001002` *animal-associated environment*. Its OWL axioms are not merely lexical — it is asserted `part_of some FAO:0000001` (*fungal structure*) and `part_of some NCBITaxon:4751` (*Fungi*), with parallel `RO:0002507 (determined by)` restrictions (OLS4, ENVO release; [ENVO:01001041](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001041)).

**⚠ Corpus-consistency finding.** The curation note on this record says "no ontology term fits this concept", and the note on the sibling record `habitatmech:GOLD.a8fc5001d1` (`Host-associated > Fungi`, 635 organisms) says the same while *itself citing* "ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment". `ENVO:01001041` exists, is in the slice, and is the fungal member of that trio. For the sibling record it is not a near-miss, it is the concept — a plain `GROUND`. This is worth a separate issue independent of whatever is decided here. *(Inference, mine, from repo state.)*

### Near-misses and why each fails

| Term | Label | Why it is not the match |
|---|---|---|
| `ENVO:01001058` | environment associated with a fungal tissue | **Narrower/different axis** — "determined by part of a living or dead fungus"; the endosymbiont niche is defined by being *inside* living cells, not by tissue-part-hood, and it includes dead-fungus material this concept excludes. |
| `ENVO:01001035` | environment determined by a biofilm on a fungal surface | **Wrong side of the wall** — explicitly epibiotic; the differentia here is endo-. |
| `ENVO:01001000` | environmental system determined by an organism | **Too broad** — covers every host clade; grounding here collapses fungi into plants and animals, which is precisely the merge the corpus's `<X>-associated environment` requests were written to avoid. |
| `FOODON:03411261` | fungus | **Not a place** — a taxonomic grouping ("a member of the group of eukaryotic organisms in the kingdom Fungi…"); correctly held as `xref` on the record under #99. |
| `NCBITaxon:4751` | Fungi | Same objection; a class of organisms. |
| `FAO:0000001` | fungal structure | An anatomical structure, not an environment; also **not vendored** in this repo's slice. |
| `ENVO:01000166` | mycetome | **Host-side, and animal** — the beetle organ housing a symbiotic yeast. Relevant to reading **B**, not A. |
| `BTO:0006243` | bacteriocyte | Same: the host cell that houses symbionts, in insects. |
| *(no term)* | mycorrhizosphere / hyphosphere / mycosphere | ENVO has **none** of these (0 hits, OLS4). A real ENVO gap, but a gap on the *external* fungal-influence axis, not this one. |

---

## 3. Differentia — what distinguishes it from its siblings

Under `ENVO:01001041`, the siblings are the fungal surface (`ENVO:01001035`), fungal tissue as material (`ENVO:01001058`), and the sampled anatomical parts GOLD enumerates. The distinguishing properties, all observable:

1. **Location: intracellular, within living hyphae or spores.** Endosymbiotic bacteria "dwell inside fungal cells" and are demonstrated by fluorescence/electron microscopy inside living hyphae, not on them (Bonfante & Desirò 2017, [doi:10.1038/ismej.2017.21](https://doi.org/10.1038/ismej.2017.21); Hoffman & Arnold 2010, [doi:10.1128/AEM.02928-09](https://doi.org/10.1128/AEM.02928-09)).
2. **Mode of transmission: heritable (vertical) or facultative-horizontal.** The heritable pole — Betaproteobacteria and Mollicutes passed between fungal generations in Mucoromycota — is the defining case (Pawlowska et al. 2018, [doi:10.1146/annurev-phyto-080417-045914](https://doi.org/10.1146/annurev-phyto-080417-045914)); the facultative pole shows frequent loss on subculture (Hoffman & Arnold 2010).
3. **Host range: concentrated in, but not restricted to, early-diverging fungi.** Endobacteria "mostly occur in fungi of the phylum Mucoromycota" (Bonfante & Desirò 2017), while endohyphal bacteria are also documented across Ascomycota classes (Pezizomycetes, Dothideomycetes, Eurotiomycetes, Sordariomycetes) and Basidiomycota (Hoffman & Arnold 2010; Richter, Büttner & Hertweck 2025, [doi:10.1093/ismejo/wraf128](https://doi.org/10.1093/ismejo/wraf128)).
4. **Physiological signature: reduced symbiont genomes and host dependency.** Genome sequencing of fungal endobacteria "revealed a significant reduction in genome size, particularly in endosymbionts of Glomeromycotina, as expected by their uncultivability and host dependency" (Bonfante & Desirò 2017); convergent reductive evolution is documented for *Mycoavidus* in Mortierellaceae (Amses et al. 2023, [doi:10.1016/j.fgb.2023.103838](https://doi.org/10.1016/j.fgb.2023.103838)). Note the counterexample: facultative endohyphal bacteria show **no** genome reduction (Baltrus et al. 2017, [doi:10.1099/mgen.0.000101](https://doi.org/10.1099/mgen.0.000101)) — so genome reduction is characteristic of one pole, not criterial for the habitat.
5. **Functional signature: the compartment's chemistry can be the symbiont's, not the fungus's.** The phytotoxin rhizoxin that makes *Rhizopus* the agent of rice seedling blight is biosynthesised by intracellular *Burkholderia*, not by the fungus (Partida-Martínez & Hertweck 2005, *Nature* 437:884–888, [doi:10.1038/nature03997](https://doi.org/10.1038/nature03997)). This is the single strongest argument that the fungal interior is a *habitat* with distinct occupants rather than a label on the fungus.

**Do not build the definition on prevalence figures.** Available numbers are population statistics, not habitat criteria: in surface-sterilised AMF spores from natural populations, *Ca.* Moeniiplasma glomeromycotorum was found at 80% and *Ca.* Glomeribacter gigasporarum at 2%, with bacteria from 10 further phyla detected (Lastovetsky et al. 2024, *New Phytologist* 242:1785–1797, [doi:10.1111/nph.19605](https://doi.org/10.1111/nph.19605)).

---

## 4. Sources

**Ontology and standards**
- ENVO `ENVO:01001041` *fungi-associated environment*; `ENVO:01001000`, `ENVO:01001001`, `ENVO:01001002`, `ENVO:01001035`, `ENVO:01001058`, `ENVO:01000166` — retrieved from OLS4, 18 Aug 2026: https://www.ebi.ac.uk/ols4/ontologies/envo ; ENVO project: Buttigieg et al. 2016, *J Biomed Semantics* 7:57, [doi:10.1186/s13326-016-0097-6](https://doi.org/10.1186/s13326-016-0097-6); Buttigieg et al. 2013, [doi:10.1186/2041-1480-4-43](https://doi.org/10.1186/2041-1480-4-43).
- FOODON `FOODON:03411261` *fungus* — OLS4, retrieved 18 Aug 2026.
- GOLD path `gold.path/4734` and siblings — OLS4 "gold" ontology, retrieved 18 Aug 2026: https://www.ebi.ac.uk/ols4/ontologies/gold
- JGI GOLD Ecosystem Classification (5 levels; Host-associated / Environmental / Engineered): https://gold.jgi.doe.gov/ecosystem_classification ; Mukherjee et al. 2023, *Nucleic Acids Res* 51(D1):D957–D963, [doi:10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974), PMID 36318257.
- MIxS host-associated package (the `MIXS:HostAssociated` extension tagged on this path): Yilmaz et al. 2011, *Nat Biotechnol* 29:415–420, [doi:10.1038/nbt.1823](https://doi.org/10.1038/nbt.1823), PMID 21552244.

**Primary and review literature on the habitat (reading A)**
- Partida-Martínez LP & Hertweck C. 2005. Pathogenic fungus harbours endosymbiotic bacteria for toxin production. *Nature* 437:884–888. [doi:10.1038/nature03997](https://doi.org/10.1038/nature03997), PMID 16208371.
- Bianciotto V et al. 2003. '*Candidatus* Glomeribacter gigasporarum' gen. nov., sp. nov., an endosymbiont of arbuscular mycorrhizal fungi. *IJSEM* 53:121–124. [doi:10.1099/ijs.0.02382-0](https://doi.org/10.1099/ijs.0.02382-0), PMID 12656162.
- Naito M et al. 2017. '*Candidatus* Moeniiplasma glomeromycotorum', an endobacterium of arbuscular mycorrhizal fungi. *IJSEM* 67:1177–1184. [doi:10.1099/ijsem.0.001785](https://doi.org/10.1099/ijsem.0.001785), PMID 28073398.
- Hoffman MT & Arnold AE. 2010. Diverse bacteria inhabit living hyphae of phylogenetically diverse fungal endophytes. *Appl Environ Microbiol* 76:4063–4075. [doi:10.1128/AEM.02928-09](https://doi.org/10.1128/AEM.02928-09), PMID 20435775. *(414 endophyte isolates screened; 8 families / 15 genotypes of endohyphal bacteria recovered.)*
- Ohshima S et al. 2016. *Mycoavidus cysteinexigens* gen. nov., sp. nov., an endohyphal bacterium isolated from *Mortierella elongata*. *IJSEM* 66:2052–2057. [doi:10.1099/ijsem.0.000990](https://doi.org/10.1099/ijsem.0.000990), PMID 26920389.
- Uehling J et al. 2017. Comparative genomics of *Mortierella elongata* and its bacterial endosymbiont *Mycoavidus cysteinexigens*. *Environ Microbiol* 19:2964–2983. [doi:10.1111/1462-2920.13669](https://doi.org/10.1111/1462-2920.13669), PMID 28076891.
- Lackner G et al. 2011. Evolution of an endofungal lifestyle: deductions from the *Burkholderia rhizoxinica* genome. *BMC Genomics* 12:210. [doi:10.1186/1471-2164-12-210](https://doi.org/10.1186/1471-2164-12-210), PMID 21539752.
- Salvioli A et al. 2016. Symbiosis with an endobacterium increases the fitness of a mycorrhizal fungus, raising its bioenergetic potential. *ISME J* 10:130–144. [doi:10.1038/ismej.2015.91](https://doi.org/10.1038/ismej.2015.91), PMID 26046255.
- Bonfante P & Desirò A. 2017. Who lives in a fungus? *ISME J* 11:1727–1735. [doi:10.1038/ismej.2017.21](https://doi.org/10.1038/ismej.2017.21), PMID 28387771.
- Pawlowska TE et al. 2018. Biology of fungi and their bacterial endosymbionts. *Annu Rev Phytopathol* 56:289–309. [doi:10.1146/annurev-phyto-080417-045914](https://doi.org/10.1146/annurev-phyto-080417-045914), PMID 30149793.
- Baltrus DA et al. 2017. Absence of genome reduction in diverse, facultative endohyphal bacteria. *Microb Genom* 3:e000101. [doi:10.1099/mgen.0.000101](https://doi.org/10.1099/mgen.0.000101), PMID 28348879.
- Deveau A et al. 2018. Bacterial–fungal interactions: ecology, mechanisms and challenges. *FEMS Microbiol Rev* 42:335–352. [doi:10.1093/femsre/fuy008](https://doi.org/10.1093/femsre/fuy008), PMID 29471481.
- Amses KR et al. 2023. Convergent reductive evolution and host adaptation in *Mycoavidus* bacterial endosymbionts of Mortierellaceae fungi. *Fungal Genet Biol* 169:103838. [doi:10.1016/j.fgb.2023.103838](https://doi.org/10.1016/j.fgb.2023.103838), PMID 37716699.
- Lastovetsky OA et al. 2024. Spores of arbuscular mycorrhizal fungi host surprisingly diverse communities of endobacteria. *New Phytol* 242:1785–1797. [doi:10.1111/nph.19605](https://doi.org/10.1111/nph.19605), PMID 38403930.
- Richter I, Büttner H, Hertweck C. 2025. Endofungal bacteria as hidden facilitators of biotic interactions. *ISME J* 19:wraf128. [doi:10.1093/ismejo/wraf128](https://doi.org/10.1093/ismejo/wraf128), PMID 40581745.
- *(Reading B, for completeness)* Matsuura Y et al. 2018. Recurrent symbiont recruitment from fungal parasites in cicadas. *PNAS* 115:E5970–E5979. [doi:10.1073/pnas.1803245115](https://doi.org/10.1073/pnas.1803245115), PMID 29891654. Siehl R et al. 2024. Friendly fungi: tropical insect families form partnerships with intracellular fungi related to pathogens. *iScience* 27:110674. [doi:10.1016/j.isci.2024.110674](https://doi.org/10.1016/j.isci.2024.110674), PMID 39252957.

**Repo-internal (not external evidence; stated as such)**
- `data/raw/gold_ecosystem_paths.tsv` — path structure and assertion counts quoted in §1.
- `data/raw/ontology_terms.tsv` — confirms `ENVO:01001041` is vendored with label *fungi-associated environment*.
- `data/habitats/host_associated/fungi.yaml`, `fungi__136600ff.yaml`, `endosymbionts.yaml`; `curation/decisions.tsv`; `curation/term_requests.tsv`; `data/habitats/RETIRED.tsv`.

**Explicitly my inference, not any source's claim:** the reading-A/reading-B analysis in §1.2; the judgement that `gold.path`'s `host_taxon` annotations are mechanical; the observation that `ENVO:01001041` is an unused exact match for the sibling record; and every disposition recommendation in §6.

---

## 5. Synonyms, and what not to conflate

**Names in real use for the habitat (reading A):**
- endofungal habitat / endofungal niche
- endohyphal environment; endohyphal bacterial habitat (the term of art in the endophyte literature — Hoffman & Arnold 2010)
- intrahyphal / intracellular fungal compartment
- fungal endobacterial habitat; "inside a fungus" (Bonfante & Desirò 2017)
- fungal cytoplasmic environment (of spores and hyphae)

**Wrongly treated as the same thing:**
- **`Host-associated > Fungi` (`habitatmech:GOLD.a8fc5001d1`)** — the fungus as habitat *in general*, including surfaces and sampled tissue. Broader; overlaps but is not identical.
- **Mycosphere / hyphosphere / mycorrhizosphere** — the soil or substrate zone *influenced by* hyphae; external, and absent from ENVO entirely.
- **Fungal surface biofilm** (`ENVO:01001035`) — epibiotic.
- **Mycorrhiza / lichen** — fungus-in-plant and fungus-plus-alga associations; different partner and different location.
- **Mycobiome** — the fungal *component of* a microbiome (fungi as inhabitants), the inverse relation.
- **Mycetome / bacteriocyte** (`ENVO:01000166`, `BTO:0006243`) — animal organs and cells that house symbionts; the host is the insect.
- **Mycosis / fungal infection** — a disease process, not a place.
- **`FOODON:03411261` fungus / `NCBITaxon:4751`** — taxonomic groupings; correctly `xref` on this record under #99.
- **Endophyte** — a fungus (or bacterium) inside a *plant*; frequently confused with endohyphal bacteria in abstracts, because endohyphal bacteria are most often studied *in* fungal endophytes.

---

## 6. Should it be a term at all?

**My recommendation: do not mint a HabitatMech definition for this record, and do not file an ENVO term request for it.** Reasons, in order of weight:

1. **The concept it would define is either already covered or empty.** Under reading A the genus `ENVO:01001041` *fungi-associated environment* exists and is vendored; the extra content ("endo-") is a property of how the *symbiont* lives, not of a distinct physical setting, and it duplicates the well-populated `Host-associated > Fungi` record. Under reading B the leaf names the isolate's kingdom and denotes no place at all.
2. **Zero attestations.** 0 organisms, 0 studies, 0 biosamples. Nothing in the corpus hangs off it, and `just report` ranks the backlog by assertion volume for exactly this reason.
3. **The ambiguity cannot be resolved from available evidence**, and a definition written from the losing reading is precisely the plausible-sounding unverifiable claim `tests/test_decisions.py` exists to catch.

**Concrete dispositions, in preference order:**

- **Preferred — `GROUND_AS_PARENT ENVO:01001041` "fungi-associated environment"** on `habitatmech:GOLD.1ab59245f7`, keeping `FOODON:03411261` as `xref`, with a note recording the reading-A/B ambiguity and the zero attestation count. This is strictly better than the present state (whose only ontology link is a taxon xref and whose note asserts "no ontology term fits", which is not accurate — `ENVO:01001041` fits as a genus).
- **Also file separately (out of scope for this record but the higher-value finding): `GROUND ENVO:01001041` on `habitatmech:GOLD.a8fc5001d1`** (`Host-associated > Fungi`, 635 organisms), which is currently `UNGROUNDED` while `ENVO:01001041` sits unused in the slice and is cited *by name* in that record's own note and in a dozen `curation/term_requests.tsv` rows as the precedent for the `<X>-associated environment` pattern.
- **Not recommended: `NOT_APPLICABLE`.** Even under reading B this would be wrong per the repo rule — the target is an organism term, `tests/test_decisions.py` fails on that, and `NOT_APPLICABLE` is reserved for diseases, qualities, processes and procedures. Reading B makes the path a *classification artefact*, which is a different thing from "not a habitat", and `CONFIRM_UNGROUNDED` with an explicit note is the honest disposition if a curator prefers to leave it alone.
- **Worth an upstream note to GOLD:** the `Host-associated > Endosymbionts > {Bacteria, Fungi}` branch conflicts with GOLD's own `Host-associated > <host> > Intracellular endosymbionts` convention and holds 1 organism between its two leaves. Asking GOLD which it means would settle this record permanently at negligible cost.

**If a curator nevertheless decides reading A is right and wants a sentence,** use the one at the top of this report, cite Bonfante & Desirò 2017 and Partida-Martínez & Hertweck 2005 for the differentia, and do **not** write genome reduction or vertical transmission into the definition as criterial — Baltrus et al. 2017 documents facultative endohyphal bacteria with neither.

## Citations

1. https://w3id.org/gold.path/4734`
2. https://www.ebi.ac.uk/ols4/ontologies/gold/classes?obo_id=4734
3. https://gold.jgi.doe.gov/ecosystem_classification
4. https://doi.org/10.1093/nar/gkac974
5. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001041
6. https://doi.org/10.1038/ismej.2017.21
7. https://doi.org/10.1128/AEM.02928-09
8. https://doi.org/10.1146/annurev-phyto-080417-045914
9. https://doi.org/10.1093/ismejo/wraf128
10. https://doi.org/10.1016/j.fgb.2023.103838
11. https://doi.org/10.1099/mgen.0.000101
12. https://doi.org/10.1038/nature03997
13. https://doi.org/10.1111/nph.19605
14. https://www.ebi.ac.uk/ols4/ontologies/envo
15. https://doi.org/10.1186/s13326-016-0097-6
16. https://doi.org/10.1186/2041-1480-4-43
17. https://www.ebi.ac.uk/ols4/ontologies/gold
18. https://doi.org/10.1038/nbt.1823
19. https://doi.org/10.1099/ijs.0.02382-0
20. https://doi.org/10.1099/ijsem.0.001785
21. https://doi.org/10.1099/ijsem.0.000990
22. https://doi.org/10.1111/1462-2920.13669
23. https://doi.org/10.1186/1471-2164-12-210
24. https://doi.org/10.1038/ismej.2015.91
25. https://doi.org/10.1093/femsre/fuy008
26. https://doi.org/10.1073/pnas.1803245115
27. https://doi.org/10.1016/j.isci.2024.110674