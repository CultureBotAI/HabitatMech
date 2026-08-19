---
provider: claude_code
model: claude-opus-5
cached: false
start_time: '2026-08-17T17:02:29.925124'
end_time: '2026-08-17T17:10:45.727742'
duration_seconds: 495.8
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Brown Algae
  habitat_identifier: habitatmech:GOLD.3e4ecbed63
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Algae > Brown Algae'
  assertions: '231'
  parent_terms: (none)
  xrefs: FOODON:03412395
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term FOODON:03412395 'brown algae' attached as a parent. Non-habitat\
    \ screen (#12): grounded EXACT to FOODON:03412395 'brown algae', which FOODON\
    \ uses for the TAXON \u2014 red algae is defined there as 'one of the oldest groups\
    \ of eukaryotic algae, and one of the largest phyla' \u2014 not for a habitat.\
    \ An organism group is not a place, and the GOLD path says host-associated, so\
    \ the concept is the environment the alga provides. Same family as the sponge,\
    \ nematode and reptile requests. The FOODON term is kept as an xref (#99), which\
    \ records what the label matched without asserting the record is a phylum. (source\
    \ concept habitatmech:GOLD.3e4ecbed63)"
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
  web_search_requests: 13
  num_turns: 26
  total_cost_usd: 3.109168
  session_id: 658b37bb-d65a-4386-a9af-ede3f2dcd2af
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 29
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Brown Algae
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.3e4ecbed63
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Algae > Brown Algae
- **Upstream assertion volume:** 231
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** FOODON:03412395

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term FOODON:03412395 'brown algae' attached as a parent. Non-habitat screen (#12): grounded EXACT to FOODON:03412395 'brown algae', which FOODON uses for the TAXON — red algae is defined there as 'one of the oldest groups of eukaryotic algae, and one of the largest phyla' — not for a habitat. An organism group is not a place, and the GOLD path says host-associated, so the concept is the environment the alga provides. Same family as the sponge, nematode and reptile requests. The FOODON term is kept as an xref (#99), which records what the label matched without asserting the record is a phylum. (source concept habitatmech:GOLD.3e4ecbed63)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Brown Algae** as a microbial habitat, with citations.

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

# Brown Algae as a microbial habitat — definition research

**Target:** `habitatmech:GOLD.3e4ecbed63` — "Brown Algae" (HOST_ASSOCIATED, UNGROUNDED, 231 upstream assertions)
**Source path:** GOLD `Host-associated > Algae > Brown Algae`

---

## Proposed definition

> An algae-associated environment which is determined by a brown alga (Phaeophyceae), comprising the alginate- and fucoidan-walled thallus — its surface biofilm, internal tissues, and the exudate-enriched boundary layer immediately surrounding it — as a setting inhabited by microorganisms.

If the genus must be an already-existing ontology term rather than the HabitatMech-minted sibling `Host-associated > Algae`, substitute the grounded ancestor:

> An environmental system determined by an organism ([ENVO:01001000](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001000)) which is determined by a brown alga (Phaeophyceae) — its thallus surfaces, internal tissues, and adjacent exudate-enriched boundary layer.

The one-sentence form is achievable here, but note that the intermediate class **algae-associated environment** does not exist in ENVO (§2). HabitatMech is already minting it as `habitatmech:GOLD.02383c20a7` ("Algae"), so the genus above is the sibling-consistent choice; ENVO lacks the rung.

---

## 1. What the concept denotes

**The physical thing a sample is taken from:** a living, macroscopic brown alga (class Phaeophyceae) and the microbial habitat it constitutes — principally the thallus surface, on which a dense bacterial biofilm develops, and secondarily the interior tissues (endophytic/endobiotic compartment) and the diffusive boundary layer of algal exudates. Samples in this class are swabs or scrapes of blade/stipe/holdfast surfaces, excised thallus discs, whole-thallus homogenates, or cultured juvenile stages.

Two things make this reading near-certain for the GOLD data:

- The path prefix is **`Host-associated`**, not `Environmental > Aquatic > Marine`. GOLD files the alga as a *host*, i.e. the alga's own body is the place sampled, not the water column or seabed around it ([Mukherjee et al. 2023, *NAR* 51:D957–D963, doi:10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974)).
- Its own children in `data/raw/gold_ecosystem_paths.tsv` are anatomical/organismal sub-locations — `Brown Algae > Blade`, `Brown Algae > Whole body`, `Brown Algae > Embryo` — which only make sense if the parent denotes the organism-as-place.

**Taxonomic extent.** Phaeophyceae comprises ~2,000 described species in 19 orders, multicellular photosynthetic stramenopiles (Ochrophyta) whose plastid derives from a secondary endosymbiosis with a red alga; they are overwhelmingly marine, with a handful of freshwater exceptions (e.g. *Heribaudiella*) ([Bringloe et al. 2020, *Crit Rev Plant Sci* 39:281–321, doi:10.1080/07352689.2020.1787679](https://doi.org/10.1080/07352689.2020.1787679)). Within the concept: kelps (Laminariales — *Laminaria*, *Saccharina*, *Macrocystis*), fucoids (Fucales — *Fucus*, *Ascophyllum*, *Gongolaria*, benthic and holopelagic *Sargassum*), Dictyotales, and the filamentous model *Ectocarpus*.

**Boundary — what is inside:**
- attached benthic kelp and fucoid thalli, living, sampled at any thallus part;
- holopelagic *Sargassum* mats in the open ocean, which are brown algae acting as host ([Cox et al. 2025, *Harmful Algae*, doi:10.1016/j.hal.2025.102904](https://doi.org/10.1016/j.hal.2025.102904));
- endophytic communities inside the thallus, which cluster separately from epiphytes and seawater and are therefore a compartment of the same host, not a different habitat ([Zhang et al. 2024, *Front Microbiol*, PMC11016019](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11016019/));
- laboratory-cultured brown algal hosts (*Ectocarpus* cultures, kelp embryos/gametophytes), which the GOLD `Embryo` child attests.

**Boundary — neighbouring concepts that are outside:**

| Neighbour | Why it is not this concept |
|---|---|
| **kelp forest** ([ENVO:01000058](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01000058)) | An underwater *area* of high kelp density, including water column, rock and sediment; a kelp-forest sample need not be on an alga at all. Also Laminariales-only, so it excludes fucoids and *Sargassum*. |
| Surrounding seawater | Epibacterial communities on brown algae differ significantly from those in ambient seawater and on abiotic surfaces (§3). |
| **Detached/decaying kelp, wrack, kelp detritus** | Arguably a distinct habitat: succession on decaying *Saccharina japonica* shifts from alginate-degrading Gammaproteobacteria to fucoidan-degrading Verrucomicrobiota/Planctomycetota/Kiritimatiellota/Bacteroidota ([Zhang Y-S et al. 2024, *Appl Environ Microbiol* 90:e02025-23, doi:10.1128/aem.02025-23](https://doi.org/10.1128/aem.02025-23)). "Host-associated" implies a living host; dead thallus is better described as **algal material** ([ENVO:01001189](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001189), "an organic material which is primarily composed of living or dead algae, along with their exudates"). *This split is my inference from the GOLD path prefix, not a statement any source makes.* |
| GOLD siblings `Diatoms`, `Golden Algae`, `Yellow-green algae`, `Dinoflagellates`, `Microalgae`, `Phycosphere` | Diatoms, chrysophytes and xanthophytes are also stramenopiles, and GOLD gives them their own nodes — so `Brown Algae` here means Phaeophyceae specifically, not "ochrophyte" or "brown-pigmented alga". |
| `Engineered > Lab culture > Culture media > Algae` (`GOLD.5b8e5eddd2`) | A medium for growing algae, already dispositioned to BTO:0000316. |
| Brown seaweed as food/feed | FOODON's domain; a food product, not a host environment. |

**Residual ambiguity worth recording (not resolvable from the data):** GOLD's `Brown Algae` is used both for whole-organism sampling and, via its children, for specific thallus parts. Within-thallus variation is large and real — bacterial density on *Laminaria hyperborea* ranged from ~8.3 × 10² cells cm⁻² on new growing tissue in March to ~1.0 × 10⁷ cells cm⁻² on non-growing tissue from July to February ([Bengtsson, Sjøtun & Øvreås 2010, *Aquat Microb Ecol* 60:71–83, doi:10.3354/ame01409](https://doi.org/10.3354/ame01409)) — so the parent concept should be written as *the alga as habitat in general*, with compartments left to its children.

---

## 2. Genus — the broader kind

**Smallest well-established kind:** an *organism-determined environmental system* — specifically, an alga-determined one. ENVO has the general rung but **not** the algal one.

ENVO's `-associated environment` family, queried live via OLS4 (8 classes total): `plant-associated environment`, `animal-associated environment`, `fungi-associated environment`, `cnidarian-associated environment`, `environment associated with a fungal tissue`, `environment associated with an aquatic invertebrate`, `environment associated with an animal part or small animal`, `environment associated with a plant part or small plant`. **There is no algae-associated, macroalgae-associated, or seaweed-associated environment.** An unauthenticated title search of the ENVO issue tracker (`EnvironmentOntology/envo`) returned no open request for one either — worth re-checking with a full-text search before filing.

**Near-misses and why each fails:**

| Candidate | Definition (from OLS4) | Verdict |
|---|---|---|
| **ENVO:01001000** *environmental system determined by an organism* (syn. "host-associated environment") | "An environmental system which is determined by a living organism." | **Correct but too broad** — it is the root of the entire host-associated branch. Usable as the genus of last resort; it is present in the vendored slice (`data/raw/ontology_terms.tsv`). |
| **ENVO:01001001** *plant-associated environment* | "An environmental system determined by a **green plant**." Exact synonym: "Viridiplantae-associated environment". | **Asserts something false.** Brown algae are stramenopiles, not Archaeplastida; their plastid is a secondarily-acquired red-algal one (Bringloe et al. 2020). Grounding or parenting here publishes "brown algae are green plants". |
| **ENVO:01001002** *animal-associated environment* / **ENVO:01001041** *fungi-associated environment* | Metazoa / fungal structure | Wrong lineage; same failure mode. |
| **ENVO:01000058** *kelp forest* | "Underwater areas with a high density of kelp… Smaller areas of anchored kelp are called kelp beds." Term comment explicitly warns it should not be treated as a "bed". | **Narrower and a different kind** — an ecosystem/area, not an organism-determined system; Laminariales-only; a sample from it may be water, rock or sediment. |
| **ENVO:01001189** *algal material* | "An organic material which is primarily composed of living or dead algae, along with their exudates." | **Wrong upper category** — an environmental *material*, not an environmental *system*/place, and it spans micro- and macroalgae. Useful as `environmental_material` or an xref for the decaying-thallus reading, not as the genus. |
| **FOODON:03412395** *brown algae* | **No textual definition at all**; synonyms `phaeophyceae`, `phaeophycophyta`, `phaeophyta`; xref LanguaL B2395; curation status "requires discussion" (IAO:0000428). | **A taxon/food-source term, not a habitat**, exactly as the existing curator note says. Keep as `relation: xref`. Note for the record: the note's quoted rationale ("one of the oldest groups of eukaryotic algae…") is copied from the *red algae* sibling note and does not appear on FOODON:03412395, which carries no definition — the disposition is right, the quoted evidence is misattributed. |
| **NCBITaxon:2870** *Phaeophyceae* (verified via Ensembl taxonomy REST) | The class rank itself | A taxon, not a place. Better xref than the LanguaL-derived FOODON term if the vendored slice is ever extended — it is **not** in the current slice (31 NCBITaxon rows, none Phaeophyceae). |

**Recommendation:** genus = the HabitatMech-minted `Host-associated > Algae` concept (`habitatmech:GOLD.02383c20a7`, already `CONFIRM_UNGROUNDED` with FOODON:03411301 as xref), grounded transitively under ENVO:01001000. This keeps `Brown Algae`, `Red algae` (`GOLD.e789c273d0`) and `Green algae` (`GOLD.184cc9e802`) parallel — all three already carry the identical disposition — and is the shape ENVO itself uses for plants, animals and fungi. A term request to ENVO for *algae-associated environment* + *brown algae-associated environment* is the natural upstream ask (subject to the standing per-request permission rule).

---

## 3. Differentia — what distinguishes it from its siblings

Four families of observable property separate a brown alga's habitat from a red or green alga's, and from ambient seawater.

**(a) Substrate chemistry — the strongest and most measurable differentia.**
Brown algal walls are built from **alginate** (a 1,4-linked β-D-mannuronate / α-L-guluronate polymer, up to ~40% of dry weight) and **fucose-containing sulfated polysaccharides (fucoidan)**; carbon is stored as **laminarin**, a vacuolar β-1,3-glucan whose abundant M-series chains terminate in a mannitol residue, and as free **mannitol**, which can be 20–30% of dry weight ([Michel et al. 2010, *New Phytol* 188:67–81, doi:10.1111/j.1469-8137.2010.03345.x](https://doi.org/10.1111/j.1469-8137.2010.03345.x)). Red algae instead present agars and carrageenans; green algae present ulvan. This split is mirrored one-for-one in the polysaccharide utilization loci (PULs) of the resident bacteria: alginate and laminarin PULs on browns, ulvan PULs on greens, porphyran PULs on reds. Brown-algal-specific enzymology is well characterised — PL6/PL7/PL17 alginate lyases in early kelp colonisers, GH168 endo-fucanases upregulated during fucoidan digestion by marine Planctomycetota ([Zhang Y-S et al. 2024, doi:10.1128/aem.02025-23](https://doi.org/10.1128/aem.02025-23); [Sichert et al./Dutschei et al. 2024, *Nat Commun* 15, doi:10.1038/s41467-024-55268-w](https://doi.org/10.1038/s41467-024-55268-w)).

**(b) Host chemical defence — a distinctive halogen/redox microenvironment.**
Brown algae mount an oxidative burst on recognising oligoguluronate alginate fragments, and blocking it with the NAD(P)H-oxidase inhibitor DPI leaves kelp sporophytes readily degraded by their own bacterial epiflora — direct evidence that the host actively regulates its epibiome ([Küpper et al. 2002, *J Chem Ecol* 28:2057–2081, doi:10.1023/A:1020706129624](https://doi.org/10.1023/A:1020706129624)). *Laminaria* accumulates apoplastic iodide via vanadium haloperoxidase and releases it as an inorganic antioxidant at the thallus surface, explicitly in response to oxidative bursts triggered by alginate-degrading biofilm bacteria ([Küpper et al. 2008, *PNAS* 105:6954–6958, doi:10.1073/pnas.0709959105](https://doi.org/10.1073/pnas.0709959105)). Phlorotannins — polyphenolics restricted to brown algae — are cross-linked into the wall by the same haloperoxidase/H₂O₂/halide system ([Leblanc et al. 2010, *Mar Drugs* 8:988–1010, doi:10.3390/md8040988](https://doi.org/10.3390/md8040988)).

**(c) Community signature and host specificity.**
Host identity outranks season as the driver of epibacterial composition across co-located brown, red and green algae; a core of 10 genera persists year-round on all of them, with *Granulosicoccus* the only genus in every sample ([Brunet, Le Duff, Barbeyron & Thomas 2025, *Environ Microbiol Rep* 17:e70077, doi:10.1111/1758-2229.70077](https://doi.org/10.1111/1758-2229.70077)). Community composition is more similar within than between seaweed phyla ([Nahor et al. 2024, *Sci Rep* 14, doi:10.1038/s41598-024-69362-y](https://doi.org/10.1038/s41598-024-69362-y)), and brown algae often show the lowest alpha diversity of the three phyla. On *Saccharina latissima*, nearly every individual hosted *Granulosicoccus* (~12% of sequences), with tissue type (apex vs meristem) the strongest structuring factor, ahead of geography, season and host health ([Burgunter-Delamare et al. 2022, *Front Microbiol* 13:1050939, doi:10.3389/fmicb.2022.1050939](https://doi.org/10.3389/fmicb.2022.1050939)). On *L. hyperborea*, Planctomycetes accounted for 51–53% of biofilm cells in July/September and 24% in February by FISH ([Bengtsson & Øvreås 2010, *BMC Microbiol* 10:261, doi:10.1186/1471-2180-10-261](https://doi.org/10.1186/1471-2180-10-261)). *Caveat for curation: FISH/DGGE-era Planctomycetes percentages are not reproduced by later amplicon studies; cite the method with the number.*

**(d) Physical setting.**
Macroscopic, mostly perennial, benthic-attached (holdfast → stipe → blade) or holopelagic; marine, photic, intertidal to subtidal; an oxygenated, DOC-enriched surface with steep micron-scale structure ([Ramírez-Puebla et al. 2022, *Microbiome* 10:52, doi:10.1186/s40168-022-01235-w](https://doi.org/10.1186/s40168-022-01235-w)); biofilm density varies ~4 orders of magnitude with the host's seasonal growth cycle (Bengtsson et al. 2010).

**Recommended differentia for the definition sentence:** the host lineage (Phaeophyceae) plus the wall/storage chemistry (alginate, fucoidan, laminarin), because these are what actually separate the microbial habitat from its red- and green-algal siblings and are directly measurable. Host defence chemistry belongs in a `comment`, not the differentia.

---

## 4. Sources

Primary literature and reference vocabularies used above:

- Egan S, Harder T, Burke C, Steinberg P, Kjelleberg S, Thomas T (2013) The seaweed holobiont: understanding seaweed–bacteria interactions. *FEMS Microbiol Rev* 37:462–476. [doi:10.1111/1574-6976.12011](https://doi.org/10.1111/1574-6976.12011) — PMID 23157386
- Saha M et al. (2024) Progress and future directions for seaweed holobiont research. *New Phytol*. [doi:10.1111/nph.20018](https://doi.org/10.1111/nph.20018)
- Bringloe TT et al. (2020) Phylogeny and evolution of the brown algae. *Crit Rev Plant Sci* 39:281–321. [doi:10.1080/07352689.2020.1787679](https://doi.org/10.1080/07352689.2020.1787679)
- Michel G, Tonon T, Scornet D, Cock JM, Kloareg B (2010) Central and storage carbon metabolism of *Ectocarpus siliculosus*. *New Phytol* 188:67–81. [doi:10.1111/j.1469-8137.2010.03345.x](https://doi.org/10.1111/j.1469-8137.2010.03345.x)
- Zhang Y-S et al. (2024) Metagenomic insights into the dynamic degradation of brown algal polysaccharides by kelp-associated microbiota. *Appl Environ Microbiol* 90:e02025-23. [doi:10.1128/aem.02025-23](https://doi.org/10.1128/aem.02025-23) — PMID 38259074
- Dutschei T et al. (2024) Mechanisms of recalcitrant fucoidan breakdown in marine Planctomycetota. *Nat Commun* 15. [doi:10.1038/s41467-024-55268-w](https://doi.org/10.1038/s41467-024-55268-w)
- Lu D-C et al. (2023) Epiphytic common core bacteria in the microbiomes of co-located green (*Ulva*), brown (*Saccharina*) and red (*Grateloupia*, *Gelidium*) macroalgae. *Microbiome* 11:126. [doi:10.1186/s40168-023-01559-1](https://doi.org/10.1186/s40168-023-01559-1) — PMID 37264413
- Brunet M, Le Duff N, Barbeyron T, Thomas F (2025) Year-round quantification, structure and dynamics of epibacterial communities from diverse macroalgae. *Environ Microbiol Rep* 17:e70077. [doi:10.1111/1758-2229.70077](https://doi.org/10.1111/1758-2229.70077)
- Nahor O et al. (2024) Epiphytic microbiome associated with intertidal seaweeds in the Mediterranean Sea. *Sci Rep* 14. [doi:10.1038/s41598-024-69362-y](https://doi.org/10.1038/s41598-024-69362-y)
- Burgunter-Delamare B et al. (2022) The *Saccharina latissima* microbiome: effects of region, season, and physiology. *Front Microbiol* 13:1050939. [doi:10.3389/fmicb.2022.1050939](https://doi.org/10.3389/fmicb.2022.1050939) — PMID 36687663
- Bengtsson MM, Sjøtun K, Øvreås L (2010) Seasonal dynamics of bacterial biofilms on the kelp *Laminaria hyperborea*. *Aquat Microb Ecol* 60:71–83. [doi:10.3354/ame01409](https://doi.org/10.3354/ame01409)
- Bengtsson MM, Øvreås L (2010) Planctomycetes dominate biofilms on surfaces of the kelp *Laminaria hyperborea*. *BMC Microbiol* 10:261. [doi:10.1186/1471-2180-10-261](https://doi.org/10.1186/1471-2180-10-261) — PMID 20950420
- Ramírez-Puebla ST, Weigel BL, Jack L, et al. (2022) Spatial organization of the kelp microbiome at micron scales. *Microbiome* 10:52. [doi:10.1186/s40168-022-01235-w](https://doi.org/10.1186/s40168-022-01235-w)
- Weigel BL et al. (2022) Functional insights into the kelp microbiome from metagenome-assembled genomes. *mSystems* 7:e01422-21. [doi:10.1128/msystems.01422-21](https://doi.org/10.1128/msystems.01422-21)
- Küpper FC, Müller DG, Peters AF, Kloareg B, Potin P (2002) Oligoalginate recognition and oxidative burst play a key role in natural and induced resistance of sporophytes of Laminariales. *J Chem Ecol* 28:2057–2081. [doi:10.1023/A:1020706129624](https://doi.org/10.1023/A:1020706129624)
- Küpper FC et al. (2008) Iodide accumulation provides kelp with an inorganic antioxidant impacting atmospheric chemistry. *PNAS* 105:6954–6958. [doi:10.1073/pnas.0709959105](https://doi.org/10.1073/pnas.0709959105) — PMID 18458346
- Leblanc C et al. (2010) The halogenated metabolism of brown algae (Phaeophyta), its biological importance and its environmental significance. *Mar Drugs* 8:988–1010. [doi:10.3390/md8040988](https://doi.org/10.3390/md8040988)
- Cox CE, Stiffler A, Hervé V, Léger-Pigout M, et al. (2025) Sailing together: a review of the pelagic *Sargassum* microbiome. *Harmful Algae*. [doi:10.1016/j.hal.2025.102904](https://doi.org/10.1016/j.hal.2025.102904)
- Zhang X et al. (2024) Community structure of endophytic bacteria of *Sargassum thunbergii* in the intertidal zone of Qingdao. [PMC11016019](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11016019/)
- Dittami SM et al. (2014) Genome and metabolic network of "*Candidatus* Phaeomarinobacter ectocarpi" Ec32. [PMC4110880](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4110880/)
- Mukherjee S et al. (2023) Twenty-five years of Genomes OnLine Database (GOLD): data updates and new features in v.9. *Nucleic Acids Res* 51:D957–D963. [doi:10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974)
- ENVO classes as retrieved from EBI OLS4 on 2026-08-17: [ENVO:01001000](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001000), [ENVO:01001001](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001001), [ENVO:01001002](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002), [ENVO:01001041](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001041), [ENVO:01000058](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01000058), [ENVO:01001189](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001189); [FOODON:03412395](https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?obo_id=FOODON:03412395); NCBITaxon:2870 via [Ensembl taxonomy REST](https://rest.ensembl.org/taxonomy/id/Phaeophyceae?content-type=application/json).

**Explicitly flagged as inference, not sourced:** (i) that the living/decaying-thallus split follows from GOLD's `Host-associated` prefix; (ii) that GOLD's `Brown Algae` means Phaeophyceae *sensu stricto* — inferred from the existence of sibling `Golden Algae`, `Yellow-green algae` and `Diatoms` nodes in `data/raw/gold_ecosystem_paths.tsv`, not from GOLD documentation; (iii) that no ENVO term request exists for an algae-associated environment — based on an unauthenticated title-only GitHub search.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept:**
- brown alga-associated environment; Phaeophyceae-associated environment
- brown seaweed surface / macroalgal surface (of a brown alga)
- brown algal epibiotic (epiphytic) habitat; brown algal thallus surface
- brown algal holobiont environment; brown seaweed epimicrobiota habitat
- *phaeophyte-associated environment* (rare, but unambiguous)
- **narrower, not synonyms:** kelp-associated environment, kelp surface biofilm, *Sargassum*-associated environment

**Commonly but wrongly treated as the same thing:**

| Confusable | Distinction |
|---|---|
| **brown algae the taxon** (FOODON:03412395, NCBITaxon:2870) | A class of organisms, not a place. This is precisely why the record stays UNGROUNDED with the term as `relation: xref`. |
| **kelp forest** (ENVO:01000058) | The ecosystem/area, not the alga's body; also excludes non-Laminariales browns. |
| **phycosphere** | In standard usage the diffusive nutrient shell around a *microalgal/phytoplankton* cell; GOLD places `Phycosphere` under `Algae > Diatoms`, not under brown algae. |
| **algal bloom / marine algal bloom** (ENVO:2000004, ENVO:01000057) | Bloom-forming taxa are microalgae/cyanobacteria; a bloom is a process/event. |
| **algal material** (ENVO:01001189), wrack, beach-cast kelp, kelp detritus | An environmental material, dominated by decomposers rather than a host-regulated epibiome. |
| **seaweed** (FOODON:03412266) | Polyphyletic, spanning red + green + brown; the parent-level concept, and the corpus already treats it separately (`GOLD.0e7a5162bb`). |
| **Sargasso Sea** | A marine region named for the alga, not the alga. |
| **algal culture medium** (`GOLD.5b8e5eddd2`, BTO:0000316) | Engineered growth medium. |
| **diatom-, chrysophyte-, xanthophyte-associated environments** | Also stramenopiles, also "brownish"; separate GOLD nodes and unicellular. |
| **brown seaweed food products** | FOODON's LanguaL-derived branch — the same string, a different universe of discourse. |

---

## 6. Should it be a term at all?

**Yes — keep it as a habitat term-request candidate, exactly as dispositioned.** The reasoning tracks CLAUDE.md's host/taxon rule and the sponge/nematode/reptile family:

1. **An organism acting as host is a place.** ENVO already models this pattern for plants, animals, fungi and cnidarians; the alga is where the microbe lives. `NOT_APPLICABLE` would be the wrong call — that is for diseases, qualities, processes and procedures.
2. **The taxon term is not the place.** FOODON:03412395 is a LanguaL-derived food-source/taxon term with no definition and curation status "requires discussion"; it stays `relation: xref`.
3. **It earns its own term rather than collapsing into the parent `Algae` concept**, because the differentia is chemical and measurable, not merely taxonomic: brown algae present alginate/fucoidan/laminarin where reds present agar/carrageenan and greens present ulvan, and the associated bacterial PUL repertoires and community composition track that split (Zhang et al. 2024; Nahor et al. 2024; Brunet et al. 2025). A definition written on host chemistry is defensible independently of the host clade name.
4. **Volume supports it:** 231 GOLD assertions across 3 ecosystem ids, more than the Green algae (108) and Red algae (73) siblings combined.

**One caveat the curator should decide explicitly.** The concept as GOLD uses it mixes living-host sampling with what may include decaying/detached thallus. If the record is to mean the living host only, say so in the definition or a comment; otherwise the record silently spans two habitats with demonstrably different communities (Zhang Y-S et al. 2024). I would write the term for the living host and let decaying material sit with ENVO:01001189 *algal material*.

## Citations

1. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001000
2. https://doi.org/10.1093/nar/gkac974
3. https://doi.org/10.1080/07352689.2020.1787679
4. https://doi.org/10.1016/j.hal.2025.102904
5. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11016019/
6. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01000058
7. https://doi.org/10.1128/aem.02025-23
8. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001189
9. https://doi.org/10.3354/ame01409
10. https://doi.org/10.1111/j.1469-8137.2010.03345.x
11. https://doi.org/10.1038/s41467-024-55268-w
12. https://doi.org/10.1023/A:1020706129624
13. https://doi.org/10.1073/pnas.0709959105
14. https://doi.org/10.3390/md8040988
15. https://doi.org/10.1111/1758-2229.70077
16. https://doi.org/10.1038/s41598-024-69362-y
17. https://doi.org/10.3389/fmicb.2022.1050939
18. https://doi.org/10.1186/1471-2180-10-261
19. https://doi.org/10.1186/s40168-022-01235-w
20. https://doi.org/10.1111/1574-6976.12011
21. https://doi.org/10.1111/nph.20018
22. https://doi.org/10.1186/s40168-023-01559-1
23. https://doi.org/10.1128/msystems.01422-21
24. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4110880/
25. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001001
26. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002
27. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001041
28. https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?obo_id=FOODON:03412395
29. https://rest.ensembl.org/taxonomy/id/Phaeophyceae?content-type=application/json